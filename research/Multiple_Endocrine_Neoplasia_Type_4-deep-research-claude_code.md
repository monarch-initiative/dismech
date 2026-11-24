---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5
cached: false
start_time: '2026-11-19T19:43:02.870003'
end_time: '2026-11-19T19:58:10.610286'
duration_seconds: 907.74
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Multiple Endocrine Neoplasia Type 4
  mondo_id: MONDO:0012552
  category: Mendelian
  causal_genes: CDKN1B
  omim_id: OMIM:610755
  synonyms: CDKN1B multiple endocrine neoplasia; MEN4; multiple endocrine neoplasia
    caused by mutation in CDKN1B; multiple endocrine neoplasia, type IV
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
  web_search_requests: 19
  num_turns: 40
  total_cost_usd: 4.408921235000001
  session_id: 905ee8c5-7df1-41eb-81fb-4b7b88e84f6c
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 163
  retrieval_calls: 161
  assistant_text_blocks: 26
citation_count: 64
reference_validation:
  total_references: 64
  verified: 64
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 1
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMC:PMC1920168
  relevance_assessed: 64
  on_topic: 45
  off_topic: 1
  off_topic_references:
  - PMID:25741868
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 131
  verified: 120
  not_found: 0
  obsolete: 0
  unverifiable: 11
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 8
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0012552
    reported_labels:
    - HTTP 200.** Returned `"has_phenotype_count":44` in `has_phenotype
    - multiple endocrine neoplasia type 4
    ontology_label: multiple endocrine neoplasia type 4
  - term_id: DOID:0080137
    reported_labels:
    - DOID
    ontology_label: multiple endocrine neoplasia type 4
  - term_id: NCIT:C157449
    reported_labels:
    - NCIT
    ontology_label: Multiple Endocrine Neoplasia Type 4
  labels_variant: 2
  unresolvable_prefixes:
  - GARD
  - OMIM
  - Orphanet
  - SCTID
  - UMLS
  - MGI
  - RGD
  - NCBIGene
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Multiple Endocrine Neoplasia Type 4
- **MONDO ID:** MONDO:0012552 (if available)
- **Causal gene(s):** CDKN1B
- **OMIM:** OMIM:610755
- **Synonyms:** CDKN1B multiple endocrine neoplasia; MEN4; multiple endocrine neoplasia caused by mutation in CDKN1B; multiple endocrine neoplasia, type IV
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Multiple Endocrine Neoplasia Type 4** covering all of the
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

I'll research MEN4 (CDKN1B) comprehensively. Let me start with a broad set of searches.

None of the four pages returned the content you asked for, so I have no OMIM, NCBI Gene, or Orphanet data to report. I did not fill any gaps from memory.

- **OMIM entry, https://www.omim.org/entry/610755:** HTTP 403 Forbidden, no body returned. This is a permanent refusal, so sending the URL again would fail the same way.
- **OMIM API, https://api.omim.org/entry?mimNumber=610755:** HTTP 403 Forbidden, no body returned. The API needs a key, which I don't have. Retrying would fail the same way.
- **NCBI Gene, https://www.ncbi.nlm.nih.gov/gene/1027:** HTTP 200, but the response is a reCAPTCHA browser-check page ("Checking your browser before accessing www.ncbi.nlm.nih.gov"), not the gene record. I did not retry or try variants, since the page is an automated bot challenge.
- **Orphanet, https://www.orpha.net/en/disease/detail/276152:** HTTP 200, but the response is a bot-check interstitial ("Vérification de la connexion... protégé par haphash"), not the disease record. I did not retry.

To get these, you would need to open the URLs in a browser, or use an authenticated OMIM/NCBI E-utilities or Orphadata route that does not sit behind these challenges.

The server redirected to the same article on the PMC host, so I'll follow it.

I could not read either chapter, so I have no content to report for the MEN4 topics you listed.

1. **EndoText PDF**, https://www.endotext.org/wp-content/uploads/pdfs/multiple-endocrine-neoplasia-type-4.pdf: HTTP 429 Too Many Requests with `Retry-After: 300`. I did not retry, because a retry before that 300-second wait would ignore the server's request. Sending the URL again after the wait may work.

2. **NCBI Bookshelf NBK589717** (your fallback for the PDF), https://www.ncbi.nlm.nih.gov/books/NBK589717/: HTTP 200, but the body is a reCAPTCHA "Checking your browser" interstitial with no chapter text.

3. **StatPearls NBK568728**, https://www.ncbi.nlm.nih.gov/books/NBK568728/: the same reCAPTCHA interstitial, HTTP 200, no chapter text.

Both NCBI pages are gated by a bot check, so retrying them will probably fail the same way. Reading them would need a browser session or an authenticated tool. I did not search NCBI Bookshelf as a further fallback, because that would hit the same gate.

**Source:** https://academic.oup.com/jcem/article/109/7/e1482/7591647. OUP did not block the fetch (HTTP 200), so I did not try PubMed. The page was truncated at about 40,000 of 164,838 characters. The final ~24,900 characters were not read. The variant, carrier, phenotype, and literature-review details below come from a model-extracted summary of the rest of the page, not verbatim text. The abstract, authors, DOI, and journal details come from the verbatim part.

**Bibliographic details**
- **Title:** Beyond MEN1, When to Think About MEN4? Retrospective Study on 5600 Patients in the French Population and Literature Review
- **Journal:** The Journal of Clinical Endocrinology & Metabolism, vol. 109, no. 7, July 2024, pp. e1482–e1493
- **Year:** 2024 (published online 30 January 2024)
- **DOI:** 10.1210/clinem/dgae055
- **PMID:** Not shown on the page. I did not fetch PubMed because the OUP page did not block.
- **Authors (37):** Benjamin Chevalier, Lucie Coppin, Pauline Romanet, Thomas Cuny, Jean-Christophe Maïza, Juliette Abeillon, Julien Forestier, Thomas Walter, Olivier Gilly, Maëlle Le Bras, Sarra Smati, Marie Laure Nunes, Aurore Geslot, Solange Grunenwald, Céline Mouly, Gwenaelle Arnault, Kathy Wagner, Eugénie Koumakis, Christine Cortet-Rudelli, Émilie Merlen, Arnaud Jannin, Stéphanie Espiard, Isabelle Morange, Éric Baudin, Mathias Cavaille, Igor Tauveron, Marie-Pierre Teissier, Françoise Borson-Chazot, Delphine Mirebeau-Prunier, Frédérique Savagner, Éric Pasmant, Sophie Giraud, Marie-Christine Vantyghem, Pierre Goudet, Anne Barlier, Catherine Cardot-Bauters, Marie Françoise Odou. Chevalier, Coppin, and Romanet are co-first authors; Cardot-Bauters and Odou are co-last authors.

**Abstract:** I cannot give the full abstract verbatim. The source is non-preapproved, so quotes are capped at 125 characters and the rest must be paraphrased. Short quotes and a paraphrase:
- Context: CDKN1B germline variants cause MEN4, which the abstract describes as "a rare MEN1-like syndrome." The abstract also notes the "<100 reported cases since its discovery in 2006."
- Design: a retrospective nationwide study of French patients, with a literature review and variant class reassessment.
- Patients: adults with class 3/4/5 CDKN1B variants from the French TENGEN laboratory network, 2015–2022, tested for MEN1 suspicion. Symptomatic class 4/5 patients were compared with 66 matched MEN1 patients from the UMD-MEN1 database.
- Results: of 5,600 MEN1-suspected patients, 4 had class 4/5 variants (0.07%). The abstract also lists 29 literature patients and states that MEN4 patients had lower NET incidence and older age at PHPT diagnosis than matched MEN1 patients.
- Conclusion: the abstract says MEN4 prevalence is low, PHPT and pituitary adenoma are the main lesions, and NETs are rare. Quote: "Our results suggest a milder and later phenotype than in MEN1."

**CDKN1B variants (reference NM_004064.5, from the summary)**
- Class 4/5 (the 4 French carriers): c.313G>T p.(Glu105*); c.320del p.(Gln107Argfs*12); c.201_202del p.(His67Glnfs*57); c.285del p.(Gly97Valfs*22)
- Class 3 (VUS, 18 variants listed in the phenotype analysis): c.-465G>C, c.-317G>A, c.-231C>T, c.-29_-26del, c.25G>A/c.236T>G, c.31C>T, c.154A>G, c.155T>C, c.195G>T, c.206C>T, c.232G>A, c.272C>T, c.341C>G, c.386A>G, c.402G>C, c.475+18A>T, c.476A>G, c.586C>T

**Carriers and frequency**
- About 50 of 5,600 NGS analyses (about 0.9%) had a variant initially classed 3, 4, or 5. After reclassification, 4 (0.07%) were class 4/5.

**Phenotype of the 4 French class 4/5 carriers (from the summary)**
- **c.313G>T:** woman, diagnosed at 68 with 3 localized, asymptomatic, nonfunctional duodenal G1 NETs.
- **c.320del:** man, PHPT at 63 from a 6-mm parathyroid adenoma. Also an 18-mm benign adrenal nodule at 62 and urinary lithiasis at 21.
- **c.201_202del:** man, PHPT (known since about age 30) from a 15-mm parathyroid adenoma. Suspected acromegaly with no MRI abnormality. Age at last assessment was 71.
- **c.285del:** woman, 22-mm nonfunctional G1 pNET at 42, and a parathyroid adenoma found at thyroid surgery at 50.

**Literature review conclusions (from the summary)**
- 77 patients were reported in 26 studies. After excluding 23 asymptomatic carriers and reclassifying variants, 29 symptomatic class 4/5 patients were analyzed (17 women).
- The first manifestation among the 15 probands was PHPT (53%, median age 40.5), pituitary adenoma (33%, median age 30), or NET (13%, median age 39).
- Tumors among the 29 patients:
  - PHPT: 25 (86%), median age 47 (range 29–71)
  - Pituitary adenoma: 13 (44%), median age 40 (range 12–67)
  - NET: 8 (27%), median age 56 (range 31–70)
  - Adrenal lesions: 3 (listed as 7%; 3/29 is about 10%, so this figure may be wrong)
- Authors' conclusions: MEN4 is rare among MEN1-suspected patients (<0.1%). NETs are less frequent and occur later than in MEN1, and PHPT occurs later in MEN4. More data are needed before guidelines can be written.

Because the summary is the only source for the variant, carrier, and literature figures, check them against the full text or the PDF (https://academic.oup.com/jcem/article-pdf/109/7/e1482/58235492/dgae055.pdf) before relying on them. I did not fetch the PDF.

I could not read either article, so I have no bibliographic details, abstract, or content to report for either one.

1. **Springer (Endocrine 2023), https://link.springer.com/article/10.1007/s12020-023-03497-2:** The server returned HTTP 303 redirecting to a login page at `https://idp.springer.com/authorize?...`. That is an authentication gate, not the article, so I did not follow it. The article appears to require a Springer login or institutional access. Sending the same URL again would hit the same redirect.

2. **Bioscientifica (Endocrine Connections 2023), https://ec.bioscientifica.com/view/journals/ec/12/2/EC-22-0411.xml:** The server returned HTTP 403 Forbidden, so the body was not retrieved. This is a permanent refusal for this URL, and sending it again would fail the same way.

To get the content, the article would need to be made available through a session with access, such as an authenticated fetch tool or a copy of the text supplied directly. I did not try other mirrors or guessed URLs, since the instructions bar constructing URLs to work around failed fetches.

## Clinical Features of Multiple Endocrine Neoplasia Type 4 (MEN4): Novel Pathogenic Variant and Review of Published Cases

**Source:** Redirected from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6637788/ (301) to https://pmc.ncbi.nlm.nih.gov/articles/PMC6637788/ (200). Read at the second URL.

**Coverage limit:** The page was truncated. I read about 39,900 of 72,900 characters verbatim, which covers the abstract, introduction, index case, Tables 1 and 3, and the first part of the discussion. The rest was returned only as a model summary, which I did not rely on. The LOH results and the final discussion and conclusion are therefore not verified.

**Bibliographic details**
- PMID: 30990521
- DOI: 10.1210/jc.2019-00082
- First author: Anja Frederiksen (corresponding author: Morten Frost)
- Journal: J Clin Endocrinol Metab. 2019 Apr 16;104(9):3637–3646
- Year: 2019

**Abstract:** The full abstract exceeds the quotation limit for this source, so I cannot reproduce it verbatim. Its structure is Context, Objective, Design, Patients, Main Outcome/Result, and Conclusion. Key points:
- Design: a case report of a large Danish family plus a brief review of published MEN4 cases.
- Index case: primary hyperparathyroidism and Cushing disease. Variant c.121_122delTT, p.Leu41Asnfs*83.
- Family: 12 further carriers of the same variant. Hypercalcemia from primary hyperparathyroidism occurred in all 13 available carriers. Four had pituitary adenomas, and one had a metastatic neuroendocrine tumor.
- Loss of heterozygosity was found in 2 of 5 tumors, the parathyroid adenomas.
- Previously reported: the abstract says "Thirty cases representing 16 different CDKN1B variants," but the Results say 29 (see below).
- Conclusion: hypercalcemia from primary hyperparathyroidism and pituitary tumors are common. Gastrointestinal neuroendocrine tumors appear less prevalent in MEN4 than in MEN1. The Conclusion sentence is a short quote: "Gastrointestinal neuroendocrine tumors appear to be less prevalent in MEN4 than in MEN1."

**Total published MEN4 cases reviewed:** The paper gives 29 CDKN1B-positive individuals with 16 variants in the Results and introduction. The abstract and discussion say 30. The paper does not reconcile this.

**Reported CDKN1B variants (Table 3, previously reported)**

| Reference | cDNA | Protein | Variant type (as labeled) | Phenotype(s) | Carriers |
|---|---|---|---|---|---|
| Costa-Guda et al. (18) | c.25G>A | p.G9R | Missense | PHPT | 1 |
| Belar et al. (19) | c.163G>A | p.A55T | Missense | Zollinger-Ellison; PHPT | 1 |
| Esteban-Jurado et al. (20) | c.195G>T | p.Q65H | Missense | Colon cancer | 4 |
| Molatore et al. (13) | c.206C>G | p.P69L | Missense | Bronchial carcinoid; PHPT; pituitary microadenoma; papillary thyroid carcinoma | 1 |
| Pellegata et al. (6) | c.227G>A | p.W76X | Labeled missense (nonsense by notation) | Acromegaly; PHPT; renal angiomyolipoma | 4 |
| Agarwal et al. (7) | c.283C>T | p.P95S | Missense | Zollinger-Ellison; PHPT | 1 |
| Tichomorowa et al. (21) | c.286A>C | p.P96Q | Missense | Acromegaly | 1 |
| Tichomorowa et al. (21) | c.356T>C | p.I119T | Missense | Acromegaly | 1 |
| Elston et al. (22) | c.378G>C | p.E126D | Missense | Nephrocalcinosis; PHPT | 3 |
| Costa-Guda et al. (18) and Bugalho et al. (23) | c.397C>A | p.P133T | Missense | PHPT; papillary thyroid carcinoma | 1 |
| Bugalho et al. (23) | (not given) | (not given) | Missense (row unlabeled) | PHPT; papillary thyroid carcinoma; meningioma | 1 |
| Agarwal et al. (7) | "ATG-7G>C" (as printed) | (not given) | Missense (as printed) | PHPT | 3 |
| Agarwal et al. (7) | c.595T>C | p.*199Q | Missense | PHPT | 3 |
| Occhi et al. (8) | c.-456_-453delCCTT | 5′ UTR | Small deletion | Acromegaly; nonfunctioning pancreatic tumor | 1 |
| Malanga et al. (14) | c.-32_-29delGAGA | 5′ UTR | Small deletion | Gastric carcinoid; PHPT | 1 |
| Tonelli et al. (12) and Pardi et al. (24) | c.374_375delCT | p.S125X | Small deletion | Hashimoto thyroiditis; PHPT; pancreatic NET (Zollinger-Ellison); duodenal NE neoplasia | 2 |
| Georgitsi et al. (15) | c.59_77dup19 | (not given) | Duplication | Neuroendocrine cervical carcinoma; Cushing disease; PHPT | 1 |

This is 16 rows, matching the stated 16 variants. The index variant, c.121_122delTT (p.Leu41Asnfs*83), is novel and not in this list.

**Tumor frequencies across reviewed cases**

The paper does not give a pooled table of percentages, so these are its stated counts.
- **Primary hyperparathyroidism:** 11 cases in 16 mutation carriers (Results). Per the paper, this is the most common manifestation. The denominator is carriers, not all listed rows. In the index family, 13 of 13 carriers had it (Table 1).
- **Pituitary adenomas:** five cases in previous reports (four acromegaly, one Cushing). The discussion instead says "three cases of acromegaly and two cases of Cushing," which conflicts with the Results. Pituitary tumor penetrance is estimated at about 10% (acromegaly) and 5% (Cushing). In the index family, four carriers had pituitary tumors: the proband (ACTH-producing microadenoma, Cushing disease), two nonfunctioning microadenomas, and one nonfunctioning macroadenoma. No prolactinomas were reported.
- **Gastroenteropancreatic NETs:** six cases in previous reports, including two gastrinomas (in five patients). The discussion estimates prevalence at about 25%. In the index family, one pancreatic carcinoid (Table 1).
- **Other NETs:** one metastatic carcinoid in the family, site unknown. The Results text attributes it to the mother (III:4), but Table 1 lists the pancreatic carcinoid under III:2. This conflicts within the paper.
- **Adrenal:** no adrenal tumors are reported in the portions I read.
- **Thyroid:** papillary thyroid carcinoma (Molatore; Bugalho) and Hashimoto thyroiditis (Tonelli). One goiter and one hypothyroidism case in the family.
- **Other:** bronchial carcinoid, meningioma, cervical neuroendocrine carcinoma, renal angiomyolipoma, and colon cancer (one family, not confirmed as MEN4).

**Age at diagnosis**

The paper gives no pooled median or mean. From Table 3, I calculated these for the 14 previously reported probands with a listed age. This is my own calculation, not the paper's, and it uses the age at the first listed diagnosis.
- Ages: 15, 30, 41, 42, 45, 47, 50, 50, 50, 53, 56, 62, 68, 69, 79 (wait, 15 values). Corrected list of 14: 15, 30, 41, 42, 45, 47, 50, 50, 53, 56, 62, 68, 69, 79.
- Median: 50 years. Mean: about 50.5 years.
- Index family: the index case was 38 at referral. Primary hyperparathyroidism was found at about 36 to 37.

**Sex distribution:** Table 3 lists 17 variant rows of probands: 15 female, 2 male, with 2 not stated. This is by table row, not a pooled count of individuals.

**Authors' conclusions on screening (Discussion, verbatim short quotes)**
- Calcium and PTH: "it appears prudent to initiate screening of calcium and PTH levels in patients with MEN4 from the age of 15 years."
- Pituitary: screening "with measurements of prolactin and IGF-1 and MRI may begin in adolescents and not in children as suggested in patients with MEN1."
- Gastroenteropancreatic and other tumors: "it appears prudent to screen for manifestations of MEN4 with biochemical tests and imaging," as in MEN1 guidance.
- Penetrance: the authors state that "all previous adult CDKN1B mutation carriers had MEN4-related disease, indicating a complete penetrance."

The model summary of the unread portion quoted conclusions such as "the main features of MEN4 are primary hyperparathyroidism." I could not confirm those wordings in the verbatim text, so I have not used them.

## Europe PMC results (2 queries, both HTTP 200)

**Limits on this report:** Europe PMC is a non-preapproved source, so I can't reproduce abstracts verbatim. I can quote at most 125 characters from any one source, and the rest is paraphrased. I also read only part of query 1. The rest of it came back as a model-written summary, which I flag below.

### Query 1 (core, `hitCount` 373)
URL read: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22multiple%20endocrine%20neoplasia%20type%204%22%20OR%20%22MEN4%22%20AND%20CDKN1B&format=json&pageSize=50&resultType=core

I read the first 39,800 of 341,049 characters verbatim. The page was then cut, and the rest was a model-extracted summary (untrusted, and it contains a wrong claim that the response has no `hitCount`). Records 1 to 7 below come from the verbatim part, and their abstracts are paraphrased.

1. **33760487** – "Multiple Endocrine Neoplasia Type 4" (StatPearls). Ahmed FW et al., 2026. Study guide. The abstract covers MEN1, MEN2, and MEN4 (CDKN1B loss-of-function). It also includes a MEN5 (MAX) figure: a systematic review of 127 patients, median age at first tumor 29 years (IQR 23–39).
2. **42093859** – MEN4 variant of unknown significance in two generations with Cushing disease. Gambino S et al., *JCEM Case Rep* 2026. A father and daughter both had Cushing disease with the CDKN1B variant c.280 C>T (p.P94S). Both were treated surgically and are in remission. The authors suggest the variant could be pathogenic despite in silico predictions.
3. **42971718** – Genetic testing for hereditary duodenopancreatic NETs. Charnay T et al., *J Neuroendocrinol* 2026. Of 410 patients (301 isolated, 109 syndromic), 38 carried a (L)PV: MEN1 in 27, NF1 in 8, VHL in 3. No TSC1, TSC2, or CDKN1B (L)PVs were found. The paper proposes extended MEN1 testing for isolated dpNETs only with gastrinoma, multiple dpNETs, or diagnosis before age 40. Quote (under 125 characters): "Patients with syndromic dpNETs exhibited significantly higher positive rates (29.4%) compared to isolated dpNETs (<2%)."
4. **42720556** – Role of the surgical pathologist in recognizing hereditary NETs. Uccella S et al., *Adv Anat Pathol* 2026. Review. About 10% of NETs occur in hereditary syndromes. It covers pituitary, parathyroid, thoracic, and digestive NETs.
5. **40443455** – Pituitary macroadenoma cosecreting prolactin and GH in MEN4. Green L et al., *JCEM Case Rep* 2025. A 54-year-old woman with a GH/prolactin macroadenoma and primary hyperparathyroidism. Genetics showed CDKN1B c.410del. Histology was a mixed somatotroph-lactotroph adenoma.
6. **PMC12545434** – SUN-287, CDKN1B mutation found during bilateral breast cancer workup. *J Endocr Soc* 2025 (conference abstract). No abstract text in the response.
7. **42993098** – Structural modelling of CDKN1B and CDKN2C variants in MEN-like phenotypes. Papadopoulou-Marketou N et al., *Endocr Relat Cancer* 2026. Proband 1 had a CDKN1B frameshift, p.Lys96GlnfsTer29. Proband 2 had CDKN2C p.Leu107Val, a VUS. The abstract was cut off in the verbatim text.

**From the model-written summary (unverified against source text):** Mercè F et al. 2025 (40009226, novel CDKN1B variant with MTC); Desrosiers-Battu 2025 (39985924, anaplastic meningioma in a 6-year-old with MEN4); Yuke L 2026 (42221412, acromegaly and prolactinoma); Ruggeri RM 2023 (37632635, MEN4 review); Chevalier B 2024 (38288531, French 5,600-patient study; the summary says low MEN4 prevalence and a milder, later phenotype); De Sousa SMC and Daly AF 2026 (41965096, familial acromegaly genetics); Mignone E 2026 (42141904, pituitary adenoma germline genes).

**Not found in query 1 (either response):** Pellegata 2006 PNAS, Frederiksen 2019 JCEM. Halperin 2023 appears only as metadata in query 2 (see below), and I could not confirm the "74 cases" figure.

### Query 2 (lite, title "MEN4", `hitCount` 21)
URL read: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22MEN4%22&format=json&pageSize=50&resultType=lite

All 21 hits were returned. This response has no abstracts. Key metadata:
- **PMID 23555276**, Occhi G et al., *PLoS Genet* 2013, "A novel mutation in the upstream open reading frame of the CDKN1B gene causes a MEN4 phenotype." This is the uORF paper you asked about. Abstract not retrieved.
- **PMID 36256846**, Halperin R et al., *Endocr Relat Cancer* 2023, "Germline CDKN1B variant type and site are associated with phenotype in MEN4." Abstract not retrieved.
- **PMID 32232325**, Chasseloup F et al., *JCEM* 2020, "Germline CDKN1B Loss-of-Function Variants Cause Pediatric Cushing's Disease With or Without an MEN4 Phenotype." Abstract not retrieved.
- **PMID 35323929**, Seabrook A et al., *JCEM* 2022, "MEN4, the MEN1 Mimicker: A Case Series of three Phenotypically Heterogenous Patients With Unique CDKN1B Mutations." Abstract not retrieved.
- **PMID 38288531**, Chevalier B et al., *JCEM* 2024, "Beyond MEN1, When to Think About MEN4? Retrospective Study on 5600 Patients in the French Population and Literature Review." Abstract not retrieved. Erratum: PMID 38470411.
- **PMID 37632635**, Ruggeri RM et al., *Endocrine* 2023, review.
- **PMID 28824003**, Alrezk R et al., *Endocr Relat Cancer* 2017, "MEN4 and CDKN1B mutations: the latest of the MEN syndromes" (115 citations).
- **PMID 23933118**, Thakker RV, *Mol Cell Endocrinol* 2014, review (257 citations).
- **PMID 25592387**, Schernthaner-Reiter MH et al., *Neuroendocrinology* 2016, MEN1, MEN4, and Carney complex.
- **PMID 25416039**, Pardi E et al., *Endocr Connect* 2015, functional characterization of a CDKN1B mutation in a Sardinian kindred.
- **PMID 24819502**, Tonelli F et al., *Eur J Endocrinol* 2014, frameshift in exon 1 of CDKN1B.
- **PMID 22584700**, Pellegata NS, *Clinics* 2012, "MENX and MEN4" review.
- **PMID 40009226**, Mercè F et al., *Fam Cancer* 2025 (not open access).
- **PMID 39985924**, Desrosiers-Battu LR et al., *Cancer Genet* 2025.
- **PMID 39936980**, Bencivenga D et al., *Cells* 2025, p27Kip1 and CDKN1B variants in MEN4 and breast cancer.
- **PMID 42093859**, Gambino S et al., *JCEM Case Rep* 2026.
- **PMID 42221412**, Yuke L et al., *AACE Endocrinol Diabetes* 2026.
- **PMC11454903**, "7940 Insulinoma as a Rare Manifestation of MEN4," *J Endocr Soc* 2024 (conference abstract).
- **PMID 30665551**, Cristina EV and Alberto F, *Best Pract Res Clin Endocrinol Metab* 2018, familial hyperparathyroidism syndromes review.
- **PMID 26651534** is a false positive (a JACS paper on "MeN4" metal-nitrogen carbon catalysts) and is not MEN4-related.

### Suggested next step
To get the abstracts you asked for in full (Pellegata 2006, Frederiksen 2019, Occhi 2013, Halperin 2023, and the others), the Europe PMC REST call would need `resultType=core` with a query for each PMID or DOI, or you can open the PMC or DOI links directly. I did not construct those URLs myself, since they would embed identifiers taken from the results.

I could not read the article. None of the three sources returned its content, so I have no abstract, cohort data, risk estimates, or conclusions to report.

1. **PubMed** (https://pubmed.ncbi.nlm.nih.gov/36256846/) returned HTTP 203 with a cookie-enablement interstitial ("Cookies must be enabled ... Enable cookies for pubmed.ncbi.nlm.nih.gov and reload this page to continue."). The article text was not included. This is a gate page, not the record, and I did not try to get around it.
2. **ScienceDirect** (https://www.sciencedirect.com/org/science/article/pii/S1479682122000078) returned HTTP 403 Forbidden. The body was not retrieved.
3. **Endocrine-Related Cancer** (https://erc.bioscientifica.com/view/journals/erc/30/1/ERC-22-0174.xml) returned HTTP 403 Forbidden. The body was not retrieved.

The 403 responses are permanent for these URLs, so requesting them again would fail the same way. I did not guess alternative URLs such as a DOI resolver or a PMC copy, since you gave me these three to try.

To get the content, you could open the DOI (10.1530/ERC-22-0174) in a browser with institutional access, or check PubMed Central for an open-access version if one exists. If you can supply the text or a different URL, I can read it and produce the report you asked for.

## 1. Seabrook et al., JCEM 2022: MEN4 case series

**Citation:** PMID 35323929. DOI 10.1210/clinem/dgac162. First author Amanda Seabrook (Kolling Institute, Sydney). Published 2022 Mar 22 in *J Clin Endocrinol Metab* 107(8):2339–2349. Received 2021 Sep 30. Open access, CC BY.

**Abstract (paraphrased):** Three unrelated families, each with a unique germline CDKN1B variant (two novel), were described and compared with the literature. Family A had multiglandular primary hyperparathyroidism (PHPT), a microprolactinoma, and a multifocal nonfunctioning duodenopancreatic NET. Family B had PHPT from a single parathyroid adenoma. Family C had a nonfunctioning pituitary microadenoma and ectopic Cushing syndrome from an atypical thymic carcinoid. Conclusions: the phenotype ranges from isolated PHPT to the full endocrine spectrum, and the authors report the first MEN4 cases of a prolactinoma and an atypical thymic carcinoid.

**Variants (from the verbatim Table 1 and text):**

| Family / patient | cDNA | Protein | Status and classification | Somatic findings |
|---|---|---|---|---|
| A (proband II.2) | c.179G>A | p.Trp60Ter (text: p.Trp60*) | Novel. Nonsense in exon 1, predicted NMD. "Likely pathogenic" (PVS1, PM2). CADD 38. | Same variant in all sampled tumors, no LOH, no second hit found |
| B (proband III.2) | c.475G>A | p.Asp159Asn | Novel. Missense at the last codon of exon 1. Predicted to remove a splice donor (Alamut). "Likely pathogenic" (PVS1, PM2). SIFT 0.005, CADD 29.1. | Same variant in the parathyroid adenoma, no LOH. Somatic ATRX c.6406G>A (p.Asp2136Asn) |
| C (proband II.1) | c.374_375delCT | p.Ser125* | Previously reported. Frameshift/nonsense. | Same variant, no LOH. Somatic MEN1 c.974C>T (p.Pro325Leu) |

The methods cite NM_004064.4 and NG_016341.1. Variant classification follows ACMG.

**Functional characterization:** The paper has no in vitro functional assays. The only functional data are tumor p27Kip1 immunohistochemistry (Family A) and tumor sequencing for second hits. In Family A, parathyroid adenoma showed loss of p27 staining, read as an acquired second hit. The adrenal adenoma result was uninformative (no positive internal control). The pancreatic NET showed loss, but the authors judged it noncontributory because all non-neoplastic islets had the same pattern. Family B's parathyroid adenoma showed "somewhat decreased" p27 expression. The verbatim text cuts off there, so the rest of that result is unknown to me.

**Phenotypes and ages:**

- **Patient A (female, Family A):** Presented at 32 (text) or 33 (Table 1) with PHPT, corrected Ca 2.92 mmol/L, PTH 12.4 pmol/L. Single left superior parathyroid adenoma resected. Recurrent PHPT at 45 with a second adenoma. Osteopenia and asymptomatic renal calculi.
  - Prolactinoma at 39: 8×6×3 mm microadenoma, prolactin 1898 mIU/L, oligomenorrhea, normalized on cabergoline.
  - Hypercortisolemia at 43 with weight gain, possibly cyclical Cushing. Repeat testing was normal.
  - Adrenal lesions found on screening MRI (left 59×49 mm, right 26×21 mm). Left adrenalectomy showed a 53 mm cortical adenoma (Table 1 gives age 47).
  - Multifocal pancreatic NETs (largest 15×13×10 mm) on 68Ga-DOTATATE PET. Distal pancreatectomy at about 47 showed three well-differentiated NETs (2, 4, 11 mm, Ki67 <1%). Recurrence led to total pancreaticoduodenectomy with two NETs (13×12×12 mm and 5×5×5 mm).
  - Also PCOS and antiphospholipid syndrome. A sister had a parathyroid adenoma at 50.
- **Patient B (female, Family B):** PHPT at 26. Peak corrected Ca 3.06 mmol/L, PTH 20 pmol/L. Single right inferior parathyroid adenoma resected, no recurrence at 3 years. Pituitary MRI and pituitary/pancreatic hormones were normal, and pancreatic imaging had not been done. History of PCOS and depression. Her mother was wild-type on predictive testing.
- **Patient C (proband, Family C):** Atypical thymic carcinoid at 31 causing ectopic Cushing syndrome. Preoperative 24-h UFC 438 nmol/24 h (ref <150), ACTH 21 pmol/L (ref <14). Also a nonfunctioning pituitary microadenoma. The summary reports a 7 mm pituitary focus, inferior petrosal sinus sampling confirming an ectopic source, and a 66×45 mm mediastinal mass. The resected tumor was 59 mm, pT3pN0M0, with postoperative radiotherapy of 60 Gy in 30 fractions. Other summary-only details: SBP 199/80 mm Hg, type 2 diabetes that resolved after surgery, and no recurrence at 2 years.

**Sources of uncertainty:** The page text was truncated at about 40% of its length. Everything after the Family B p27 result comes from a model-generated summary of the remaining text, not verbatim. Those summary-only claims include the Family C details above, the literature figures (34+ reported MEN4 cases, 21 unique variants, penetrance estimates, screening proposals), and the claim that the Family C variant is ACMG pathogenic with PS3 evidence. Two summary statements conflict with verbatim text: it says Patient A's age is not given (the text gives 32/33, 39, 43, 45, and 47), and it describes Family C's relative as a "paternal aunt" where Table 1 says "second-degree relative."

## 2. Occhi et al., PLoS Genetics 2013: CDKN1B 5′UTR uORF variant

**Citation:** PMID 23555276. DOI 10.1371/journal.pgen.1003350. First author Gianluca Occhi (University of Padova). Published 2013 Mar 21 in *PLoS Genet* 9(3):e1003350. Received 2012 Jul 19, accepted 2013 Jan 16.

**Abstract (paraphrased):** The authors found a 4-bp deletion in a highly conserved regulatory uORF in the CDKN1B 5′UTR. It was found in a patient with a pituitary adenoma and a well-differentiated pancreatic neoplasm. The deletion moves the uORF stop codon, lengthening the uORF peptide and sharply shortening the intercistronic space. Immunohistochemistry on the pancreatic lesion, dual-luciferase assays, site-directed mutagenesis, and polysome profiling all pointed to reduced translation reinitiation at the CDKN1B start site and lower p27Kip1 expression. The authors conclude that uORF mutations can modulate p27 expression.

**Variant:** c.-456_-453delCCTT (4-bp deletion in the 5′UTR, referenced to NM_004064). It has no p. (protein) notation because it is outside the coding sequence. It was absent from 600 chromosomes and from dbSNP and 1000 Genomes. Other 5′UTR changes tested were c.-469C>T (silent in the uORF, found in one of 41 additional patients and not in controls), c.-428A>T (stop-codon restoration), and c.-74insC (creates an in-frame uORF–CDKN1B fusion).

**Mechanism (verbatim text):**
- The uORF peptide grows from 29 to 158 amino acids, and the intercistronic space shrinks from 429 to 38 bp. The authors propose that long uORFs and short intercistronic spaces stop 40S subunits from re-acquiring cofactors for reinitiation at the downstream ATG.
- The mRNA is not reduced. Wild-type and mutant alleles were expressed at "almost equal amounts" in blood (Figure 3a), and a single promoter was used. The authors conclude transcription and mRNA stability are not affected.
- In lymphoblastoid cells, about 90% of each allele's mRNA was in polysomes (fractions 7–11). The summary says wild-type mRNA showed about threefold greater polysomal loading across three experiments, but I could not verify that figure in the verbatim text, so treat it as summary-derived.

**Experimental evidence:**
- **Dual-luciferase assays (Figure 6A, 6B):** GH3 and HeLa cells, lovastatin-synchronized or asynchronous. The deletion "significantly reduced" luciferase activity (p<0.01) in a cell-cycle-independent manner. c.-469C>T did not. Qualitative effects were also reported in SH-SY5Y and HEK293 (Figure S1). No effect sizes appear in the text.
- **Luciferase mRNA qRT-PCR (Figure 6C):** The effect was attributed mainly to translation rate, not mRNA level.
- **Western blot (Figure 6D):** HEK293 cells transfected with wild-type or mutant 5′UTR–CDKN1B constructs. The authors report a "significant reduction in p27KIP1 protein levels" with the deletion. No numbers appear in the text.
- **Rescue (Figure 7):** c.-428A>T restores the stop codon, and the double mutant almost completely recovers uORF regulatory activity in GH3 and HeLa cells.
- **Chimeric product (Figure 6E):** c.-74insC fuses the uORF in frame with CDKN1B. The fusion product was detected only in the double-mutant transfection, along with a significant drop in p27. The authors describe this as the first direct evidence of uORF translation in a cellular system.
- **Figure 6 legend typo:** it says "c.-456_-459delCCTT+c.-74insC," but the deletion elsewhere is c.-456_-453.

**Patient and tumors:**
- The carrier is a 62-year-old female with acromegaly and a well-differentiated nonfunctioning pancreatic endocrine neoplasm (Ki-67 about 1%, text says <1%). The abstract also reports a pituitary adenoma.
- The screened cohort was 25 consecutive patients with two or more MEN1-like features. A second group of 41 was screened for the uORF only.
- Pancreatic tumor IHC: weak cytoplasmic p27 staining, with low nuclear staining. Endothelial cells served as internal controls and showed strong nuclear staining. Sporadic well-differentiated pancreatic tumors had intermediate-to-high nuclear p27.
- LOH: no loss of the wild-type allele. Both alleles were transcribed in the pancreatic lesion. The authors suggest p27 may be haploinsufficient.
- The text gives no numbers for the carrier's pituitary tumor, and no quantitative western or luciferase values.

The chapter was readable on the first URL, so I did not need the fallbacks. The first fetch returned the first 39,940 characters verbatim and a model-written summary of the rest. I then re-fetched the same URL at offset 39940 to read the remainder verbatim. The summary's "page status" note says the captured text omits the Summary through Management sections. That is wrong: the verbatim text contains them, so I relied on the verbatim text only.

Quotes are kept short because this source is non-preapproved. Everything else is paraphrased.

## Source
- URL read: https://www.ncbi.nlm.nih.gov/sites/books/NBK594826/ (both fetches, HTTP 200)
- Title: Multiple Endocrine Neoplasia Type 4 (synonyms MEN4, CDKN1B-related multiple endocrine neoplasia). GeneReviews, Bookshelf ID NBK594826, PMID 37733893.

## Authors and dates
- Authors: Pamela Brock, MS, CGC, and Lawrence Kirschner, MD, PhD, both at The Ohio State University Comprehensive Cancer Center, Columbus, Ohio.
- Original submission: 3 March 2023. Review posted live: 21 September 2023. These are the only two revision-history entries.
- No later update is listed. The cite-as date is 2023 Sep 21.

## Clinical characteristics

**Summary:** MEN4 is characterized by endocrine tumors, especially parathyroid and/or pituitary. The clinical picture overlaps substantially with MEN1, but MEN4 is described as more attenuated, with lower penetrance and later diagnosis.

**Age and case count:**
- Mean age at first endocrine tumor: 43.5 years (range 5–76), versus 31.8 years (range 9–71) in MEN1 (Singeisen 2023; Marini 2018).
- The chapter states "To date, 65 individuals have been identified" with a CDKN1B disease-causing variant (Singeisen 2023).
- 13 of those 65 belong to one large Danish family (Frederiksen 2019).
- Prevalence: "MEN4 is likely both rare and underdiagnosed."

**Tumor spectrum (Table 2 of the chapter, paraphrased):**

| Tumor type | Reported prevalence in MEN4 | Notes |
|---|---|---|
| Parathyroid tumor / PHPT | 55%–80% | 86% single adenomas; hyperplasia in 14% |
| Anterior pituitary | 30%–45% | Of these: 33% ACTH, 24% prolactin, 19% GH, 24% nonfunctioning |
| Well-differentiated GEP-NET | 14%–25% | Of these: 33% gastrinomas, 66% nonfunctioning |
| Carcinoid (thymus/lung, small bowel) | 4%–7% | Non-hormone-secreting in the table |
| Adrenocortical | 4%–7% | Cortisol-secreting or nonfunctioning |

**Details by tumor type:**
- **PHPT:** Often mild, frequently found in asymptomatic people. First manifestation in about 56%. Median age at diagnosis 51 years (range 15–74). Multiglandular disease in 14% and recurrence in 6%, both less common than in MEN1. Reported more often in women (80% vs 58%).
- **Pituitary:** Second most common feature, first presentation in about 23%. More likely to be microadenomas. Median age at diagnosis 39 years (range 5–79). ACTH adenomas are most common, then prolactinomas, then nonfunctioning tumors. A Cushing disease study found CDKN1B variants in up to 2.6% of individuals, mostly children (Chasseloup 2020).
- **GEP-NETs:** Nonfunctioning pancreatic tumors are the most frequent, followed by gastrinomas. Less likely to be multifocal. The youngest reported pancreatic NET was diagnosed at age 42. About half are metastatic at diagnosis (Singeisen 2023).
- **Carcinoid:** About 4%–7% (thymus, bronchus, ileum), some metastatic at diagnosis.
- **Other reported:** Papillary thyroid cancer in 8% (4 women, 3 multifocal, diagnosed in their 50s–60s; "may represent an emerging association"). Breast, colon, testicular, prostate, cervical neuroendocrine carcinoma, meningioma, and renal angiomyolipoma have been reported, with the chapter stating further research is needed. A possible link to autoimmune disease was raised (Chevalier 2020). Cutaneous MEN1-type tumors have not been reported.

**Genotype-phenotype:** Indels are associated with higher PHPT incidence. Variants in codons 94–96 carry a higher risk of PHPT and pituitary adenomas (Halperin 2022).

**Penetrance:** "Penetrance is reduced and age related."

## Diagnosis

**Suggestive findings:** MEN4 should be suspected in multiple/multifocal or early-onset endocrine tumors, especially parathyroid and/or pituitary. No clinical criteria capture all affected individuals. An autosomal dominant family history is supportive, but its absence does not exclude the diagnosis.

**Establishing the diagnosis:** Diagnosis is established in a proband with a germline heterozygous pathogenic (or likely pathogenic) CDKN1B variant. The chapter states that pathogenic and likely pathogenic are treated as synonymous per ACMG/AMP (Richards 2015). A heterozygous variant of uncertain significance neither establishes nor rules out the diagnosis.

**Testing approaches:**
- **Single-gene testing:** Sequence CDKN1B first (small indels, missense, nonsense, splice). If one or no variant is found, add deletion/duplication analysis for exon and whole-gene deletions or duplications.
- **Multigene panel:** The chapter says a panel including CDKN1B and other genes may be considered. Gene content and sensitivity vary by laboratory.

**Table 1 (detection):**
- Sequence analysis: about 95% of probands with a pathogenic variant (from HGMD via Stenson 2020).
- Gene-targeted deletion/duplication analysis: 2 individuals (Grey 2013; unpublished authors' data).

## Differential diagnosis

**Table 3a (hereditary syndromes):**

| Gene / disorder | MOI | Overlap | Distinguishing features |
|---|---|---|---|
| AIP (AIP-related pituitary adenoma predisposition, PITA1) | AD | Pituitary adenomas | Earlier pituitary onset than MEN4; MEN4 tumors mostly ACTH, AIP tumors mostly GH |
| GPR101 (PITA2) | XL | GH adenoma | No other MEN4-typical endocrinopathies; no GEP-NETs |
| CDH23 (PITA5) | AD | GH and nonfunctioning adenomas (familial) | No other MEN4-typical endocrinopathies; no GEP-NETs |
| CASR, CDC73, GCM2, MEN1 (familial isolated PHPT, FIHP) | AD | Parathyroid adenoma or hyperplasia | No other endocrinopathies; no pituitary tumors or GEP-NETs |
| MEN1 | AD | All features | See the clinical description comparison |
| RET (MEN2A) | AD | PHPT in ~20%–30% | MEN2A also involves medullary thyroid carcinoma and pheochromocytoma; its PHPT is less penetrant than MEN4 PHPT |

Footnotes: 14%–18% of FIHP families have identifiable CASR variants (Simonds 2002; Warner 2004). CDC73 variants are associated with hyperparathyroidism-jaw tumor syndrome. Warner 2004 found no CDC73 variants in 22 FIHP individuals. FIHP means parathyroid disease without other endocrinopathies in two or more family members.

Sporadic PHPT (usually a single adenoma) peaks in the sixth decade, similar to the MEN4 mean age.

**Table 3b (individual features):**
- Pituitary tumors: if multiple, see Table 3a.
- Zollinger-Ellison syndrome: gastrinomas can also occur in MEN1, tuberous sclerosis, and NF1.
- Nonfunctioning NETs: also seen in MEN1 (20%–55%), VHL (10%–17%), and NF1.
- Carcinoids not associated with MEN4: usually midgut or hindgut origin, secrete serotonin.

## Management

**Guidelines:** No consensus clinical practice guidelines exist for MEN4. MEN1 screening is suggested as a guide, with the caveat that MEN4 is more attenuated.

**Evaluations after diagnosis (Table 4):**
- Referral to an endocrinologist experienced in MEN.
- Assess for endocrine manifestations (kidney stones; signs of cortisol, GH, or prolactin excess; nausea, vomiting, diarrhea).
- Serum calcium in those aged 25 or older. If abnormal, PTH, vitamin D, 24-hour urine calcium, and surgical referral.
- Pituitary MRI and hormone testing (ACTH, cortisol, IGF-1, prolactin) guided by suspicion, in those aged 25 or older. Dynamic GH or cortisol testing if screening is abnormal.
- Abdominal imaging (contrast CT or MRI) in those aged 25 or older. Endoscopic ultrasound is more sensitive but more invasive.
- Genetic counseling by a genetics professional.

**Treatment (Table 5):**
- PHPT: parathyroidectomy. Cinacalcet may be considered for symptomatic hypercalcemia in non-surgical candidates. Details are referred to the MEN1 chapter.
- Pituitary: surgery for ACTH- or GH-secreting tumors, by a surgeon with pituitary expertise. Cabergoline for prolactinomas.
- NETs and carcinoids: surgical resection if possible. Consider a medical oncologist. Some may receive somatostatin analogs. Gastrin-secreting tumors can be treated with proton pump inhibitors.

**Surveillance (Table 6, frequency as stated):**

| System | Test | Start age | Interval |
|---|---|---|---|
| PHPT | Serum calcium (PTH and vitamin D may also be considered) | 25 | Biennially (every 2 years) |
| Pituitary | Serum IGF-1 and prolactin | 25 | Every 3–5 years or as symptoms indicate |
| Pituitary | Pituitary MRI | 25 | Every 5 years |
| Pituitary | If Cushing concern: 24-hour urine free cortisol, late-night salivary cortisol, and/or 1 mg overnight dexamethasone suppression | As indicated | As indicated |
| NETs/carcinoids | Serum gastrin | 25 | "Biannually" in Table 6 |
| NETs/carcinoids | Abdominal MRI or CT | 25 | Every 5 years, increasing to every 2.5 years at age 40 |

Abnormal findings warrant more frequent follow-up, using MEN1 guidelines as a guide.

The Management narrative says "Biennial serum calcium and gastrin." The table says "Biannually" for gastrin. Those two words can mean different intervals, so the source is ambiguous on gastrin frequency.

**At-risk relatives:** Molecular testing of the family's CDKN1B variant is recommended to identify who should start surveillance early. Where testing is not possible or uninformative, first-degree relatives (50% risk) should undergo surveillance. The chapter says early detection and treatment "should reduce the morbidity and mortality of MEN4."

**Therapies under investigation:** The chapter refers readers to ClinicalTrials.gov and the EU Clinical Trials Register and notes there may not be trials.

## Genetic counseling
- **Mode of inheritance:** Autosomal dominant.
- **Parents of a proband:** Most probands have an affected parent. Some are de novo. "The proportion of MEN4 caused by a de novo pathogenic variant is unknown." Simplex cases should have parental testing. Negative family history cannot be confirmed unless molecular testing shows neither parent carries the variant. Non-paternity or mosaicism are noted as possibilities.
- **Sibs:** If a parent is affected or carries the variant, sibs have 50% risk, with reduced penetrance and variable tumor types. If the variant is not detected in either parent's leukocyte DNA, sibs' recurrence risk is estimated at 1% because of possible germline mosaicism (Rahbari 2016). If parents are untested and unaffected, sibs are still presumed at increased risk.
- **Offspring:** "Each child of an individual with MEN4 has a 50% chance of inheriting the CDKN1B pathogenic variant."
- **Testing of at-risk relatives:** Strongly recommended for all first-degree relatives once a variant is identified. The chapter notes that ASCO (2003) suggested delaying testing until age 18, given low childhood risk.
- **Family planning:** Discuss before pregnancy. Offer counseling to affected or at-risk young adults.
- **Prenatal and preimplantation testing:** "Once the CDKN1B pathogenic variant has been identified in an affected family member, prenatal and preimplantation genetic testing are possible." The chapter notes that views differ among professionals and families.

## Molecular genetics

**Genes and databases (Table A):** CDKN1B, chromosome locus 12p13.1, protein cyclin-dependent kinase inhibitor 1B. Links are given to a locus-specific CDKN1B database, HGMD, and ClinVar. The chapter also cites gene ID 1027 and UniProt P46527 in its links.

**OMIM (Table B):** 600778 (CDKN1B) and 610755 (MEN4).

**Gene function:** CDKN1B encodes p27, a nuclear cyclin-dependent kinase inhibitor that blocks progression from G1 to S phase. It acts as a tumor suppressor gene.

**Mechanism:**
- Most reports suggest tumorigenesis results from loss or reduction of p27.
- Many MEN4 tumors show no loss of heterozygosity or acquired second hit.
- Whether the mechanism is haploinsufficiency or loss of function through epigenetic silencing, in addition to the germline variant, needs further research.
- Pathogenic variants outside the coding region, such as the 5' UTR, have functional evidence (Chasseloup 2020; Singeisen 2023).

**Variant table:** The chapter has no CDKN1B variant table with HGVS nomenclature. Table A lists only genes and databases, and the variant listing is delegated to external databases. The HGVS-level variant list cannot be reported from this chapter.

**Somatic tumors:** Sporadic tumors (breast, prostate, NETs, others) that occur without other MEN4 findings often carry a somatic CDKN1B variant absent from the germline, so these are not heritable.

**Allelic disorder:** Grey 2013 described a child with overgrowth/macrocephaly, strabismus, and neurodevelopmental delay. The child had reduced CDKN1B expression from biallelic loss, a maternal contiguous deletion plus a de novo promoter variant on the paternal allele. The authors proposed an autosomal recessive mechanism.

## Number of reported individuals or families
- 65 individuals with a disease-causing CDKN1B variant (Singeisen 2023).
- 13 of the 65 are from one Danish family (Frederiksen 2019).
- Disease-causing variants occur in under 5% of people with MEN1-like features and negative MEN1 testing (Georgitsi 2007; Agarwal 2009; Molatore 2010).
- Many case reports involve variants currently classed as uncertain significance.

## PMIDs cited for key claims
- Singeisen 2023 (case series, tumor spectrum, 65 individuals): 36520683
- Alrezk 2017 (review, penetrance): 28824003
- Marini 2018 (MEN1 comparison age data): 30428914
- Frederiksen 2019 (Danish family, 13 individuals): 30990521
- Halperin 2022 (genotype-phenotype): 36256846
- Chasseloup 2020 (pediatric Cushing, 5' UTR): 32232325
- Chevalier 2020 (autoimmune association): 32386678
- Grey 2013 (allelic disorder): 23505216
- Georgitsi 2007 (MEN1-like cases): 17519308
- Agarwal 2009 (MEN1-like cases): 19141585
- Molatore 2010 (MEN1-like cases): 20824794
- Simonds 2002 (FIHP families, CASR): 11807402
- Warner 2004 (FIHP genetic testing): 14985373
- Rahbari 2016 (germline mutation rates; sib 1% estimate): 26656846
- Richards 2015 (ACMG/AMP interpretation): 25741868
- Stenson 2020 (HGMD, detection rate): 32596782
- Jensen 1999 (EUS sensitivity in MEN1): 10436815
- ASCO 2003 (testing delay to age 18): 12692171
- Chapter PMID: 37733893

Other references in the list (Agarwal, Alrezk, Chasseloup, and others) are included above where cited. The chapter's own "Similar articles" lists include GeneReviews chapters on MEN1, AIP, CDC73, MEN2, and Carney complex.

All 8 records came back (hitCount 8), and I read the full response by fetching the remainder with an offset. I could not give you the abstracts verbatim. Europe PMC is a non-preapproved source, so I'm limited to quotes of 125 characters or fewer, and the abstracts are paraphrased below. The metadata is complete. The abstractText fields contain HTML markup (`<h4>`, `<sup>`, `<i>`), which I've left out of the summaries.

| PMID | Title | First author | Journal | Year | PMCID / access |
|---|---|---|---|---|---|
| 39936980 | p27Kip1 and Tumors: Characterization of CDKN1B Variants Identified in MEN4 and Breast Cancer. | Bencivenga D | Cells | 2025 | PMC11817124, open access (CC BY) |
| 37632635 | Multiple endocrine neoplasia type 4 (MEN4): a thorough update on the latest and least known men syndrome. | Ruggeri RM | Endocrine | 2023 | not in PMC, subscription |
| 36256846 | Germline CDKN1B variant type and site are associated with phenotype in MEN4. | Halperin R | Endocrine-related cancer | 2023 (epub 2022-12-12) | not in PMC, subscription |
| 35323929 | MEN4, the MEN1 Mimicker: A Case Series of three Phenotypically Heterogenous Patients With Unique CDKN1B Mutations. | Seabrook A | J Clin Endocrinol Metab | 2022 | PMC9282358, open access (CC BY) |
| 32232325 | Germline CDKN1B Loss-of-Function Variants Cause Pediatric Cushing's Disease With or Without an MEN4 Phenotype. | Chasseloup F | J Clin Endocrinol Metab | 2020 | PMC7190031, free |
| 28824003 | MEN4 and CDKN1B mutations: the latest of the MEN syndromes. | Alrezk R | Endocr Relat Cancer | 2017 | PMC5623937, free |
| 23555276 | A novel mutation in the upstream open reading frame of the CDKN1B gene causes a MEN4 phenotype. | Occhi G | PLoS Genet | 2013 | PMC3605397, open access (CC BY) |
| 17030811 | Germ-line mutations in p27Kip1 cause a multiple endocrine neoplasia syndrome in rats and humans. | Pellegata NS | PNAS | 2006 | PMC1622862, free |

**Abstract content (paraphrased)**

- **39936980 (Bencivenga, 2025):** Describes p27Kip1 as a cell-cycle regulator. Four CDKN1B mutations from MEN4 or cancer patients increased growth and motility of breast cancer cell lines. The mutants also showed altered phosphorylation, localization or degradation, and weaker binding to cyclin/CDK complexes, which partly explains the loss of growth inhibition.
- **37632635 (Ruggeri, 2023, review):** Reviews MEN4 genetics and clinical features. Primary hyperparathyroidism is the most common feature, followed by pituitary adenomas and neuroendocrine tumors. MEN4 is less common than MEN1 and tends to present later with a more indolent course. The authors call for more study of oncological risk and a standardized screening protocol. The literature search covered MEDLINE and Scopus.
- **36256846 (Halperin, 2023):** Pooled 74 MEN4 cases. Estimated risk by age 60 was 53.4% for primary hyperparathyroidism, 23.2% for pituitary adenoma and 16.2% for neuroendocrine tumor. The most common variant was p.Q107fs (4/41 kindreds). Indels were linked to higher hyperparathyroidism risk than point mutations (log-rank P = 0.029). Variants in codons 94–96 were linked to higher hyperparathyroidism risk (P < 0.001) and pituitary adenoma risk (P = 0.031).
- **35323929 (Seabrook, 2022):** Three unrelated families, each with a unique germline CDKN1B variant (two of them novel). Phenotypes ranged from isolated primary hyperparathyroidism to ectopic Cushing's syndrome from an atypical thymic carcinoid. The authors report the first described prolactinoma and atypical thymic carcinoid in MEN4.
- **32232325 (Chasseloup, 2020):** Screened 211 Cushing's disease patients (94.3% pediatric). Five variants were found in one patient each: one truncating and four non-truncating, including three missense changes and a 5' UTR deletion. Two were of uncertain significance and three pathogenic or likely pathogenic, accounting for 2.6% of patients. All variants tested showed protein instability in vitro.
- **28824003 (Alrezk, 2017, review):** Reviews MEN1 and MEN4 (CDKN1B). At the time, 19 MEN4 cases had been described, most often with primary hyperparathyroidism followed by pituitary adenomas. CDKN1B mutations were also reported in sporadic hyperparathyroidism, small-intestine neuroendocrine tumors, lymphoma and breast cancer.
- **23555276 (Occhi, 2013):** A 4-bp deletion in a conserved regulatory upstream ORF in the CDKN1B 5' UTR was found in a patient with a pituitary adenoma and a pancreatic neoplasm. It shifts the uORF stop codon and reduces p27(KIP1) expression through impaired translation reinitiation.
- **17030811 (Pellegata, 2006):** A homozygous frameshift in Cdkn1b causes the MENX syndrome in rats, with reduced p27 protein. A germline nonsense mutation in human CDKN1B was found in a MEN1-negative patient with pituitary and parathyroid tumors. The MEN1-like phenotype appeared across several generations of that family.

An earlier model-generated summary of the truncated part of the response contained errors, so the table and summaries above are based only on the verbatim JSON. If you need exact abstract wording, the Europe PMC or PubMed pages for each PMID are the place to get it. The open-access records can be read in full at the PMCID links.

URL read (both calls): https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A36256846%20OR%20EXT_ID%3A17030811%20OR%20EXT_ID%3A23555276%20OR%20EXT_ID%3A32232325%20OR%20EXT_ID%3A35323929%20OR%20EXT_ID%3A37632635%20OR%20EXT_ID%3A28824003%20OR%20EXT_ID%3A39936980&format=json&pageSize=25&resultType=core

**Summary:** Endpoints 1 (MONDO term), 3 (search), and 4 (HGNC) succeeded. Endpoint 2 failed on all three HPO URLs, so I have no HPO phenotype list, frequencies, or onsets.

## 1. MONDO term: https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMONDO_0012552 (HTTP 200)

- **obo_id / short_form / iri:** MONDO:0012552 / MONDO_0012552 / http://purl.obolibrary.org/obo/MONDO_0012552
- **label:** multiple endocrine neoplasia type 4
- **description (definition):** "Multiple endocrine neoplasia type 4 (MEN4) is a very rare form of MEN, an inherited cancer syndrome, characterized by parathyroid and anterior pituitary tumors, possibly associated with adrenal, renal, and reproductive organ tumors."
- **Exact synonyms:** "CDKN1B multiple endocrine neoplasia", "MEN4" (abbreviation), "multiple endocrine neoplasia caused by mutation in CDKN1B", "multiple endocrine neoplasia type 4", "multiple endocrine neoplasia, type IV"
- **Related synonyms:** none listed
- **Database cross-references (raw):** DOID:0080137, GARD:0017275, MEDGEN:373469, MESH:C567059, NCIT:C157449, OMIM:610755, Orphanet:276152, SCTID:715907003, UMLS:C1970712, icd11.foundation:157945677
- **ICD codes:** only the ICD-11 foundation ID above (157945677). No ICD-10 or ICD-9 code is listed.
- **Parent terms** (from the `/parents` link in the response, which I fetched as a same-host follow-up; totalElements = 2):
  - MONDO:0000426, "autosomal dominant disease" (MONDO_0000426)
  - MONDO:0017169, "multiple endocrine neoplasia" (MONDO_0017169)
- **Other:** is_obsolete false; has_children false; in_subsets include clingen, gard_rare, nord_rare, ordo_disorder, orphanet_rare, otar, rare.

## 2. HPO annotations for MEN4 / OMIM:610755: all three endpoints failed (HTTP 404)

- https://ontology.jax.org/api/network/annotation/MONDO:0012552: 404
- https://ontology.jax.org/api/hp/diseases/OMIM:610755: 404
- https://hpo.jax.org/api/hpo/disease/OMIM:610755: 404

These are permanent failures, so retrying them would return the same 404. I have no HP IDs, term names, frequencies, or onsets to report.

## 3. Search: https://www.ebi.ac.uk/ols4/api/search?q=multiple%20endocrine%20neoplasia%20type%204&ontology=mondo&rows=10 (HTTP 200)

- numFound: 1
- Single doc: obo_id MONDO:0012552; label "multiple endocrine neoplasia type 4"; short_form MONDO_0012552; ontology_name mondo; type class; iri http://purl.obolibrary.org/obo/MONDO_0012552
- Exact synonyms match the endpoint 1 list.

## 4. HGNC: https://rest.genenames.org/fetch/symbol/CDKN1B (HTTP 200)

The Accept header could not be set through this tool. The server returned XML (text/xml), not JSON. The fields are still complete, so I did not need the search fallback.

- **hgnc_id:** HGNC:1785
- **symbol:** CDKN1B
- **name (approved name):** cyclin dependent kinase inhibitor 1B
- **status:** Approved
- **location:** 12p13.1 (no location_sortable field present)
- **ensembl_gene_id:** ENSG00000111276
- **uniprot_ids:** P46527
- **refseq_accession:** NM_004064
- **mane_select:** ENST00000228872.9, NM_004064.5
- **omim_id:** 600778 (this is the gene's OMIM entry, not the MEN4 disease entry 610755)
- **Other identifiers:** entrez_id 1027; vega_id OTTHUMG00000149914; ucsc_id uc001rat.3; ccds_id CCDS8653; mgd_id MGI:104565; rgd_id RGD:69062; agr HGNC:1785; gencc HGNC:1785; orphanet 200995; ena AF480891; pubmed_id 8033212; cosmic CDKN1B
- **alias_symbol:** KIP1, P27KIP1
- **prev_name:** cyclin-dependent kinase inhibitor 1B (p27, Kip1)
- **gene_group:** Cyclin dependent kinase inhibitor 1 family
- **locus_type:** gene with protein product; locus_group: protein-coding gene

I'll run each query as its own OLS4 search, since the search endpoint takes one query per request. Starting with the HPO queries.

The first 14 HPO queries are back. Next batch of HPO queries.

HPO is complete. Now the UBERON queries.

UBERON is complete. Now the Cell Ontology queries.

CL is complete. Next are the GO queries.

GO is complete. One GO query ("negative regulation of cyclin-dependent protein serine/threonine kinase activity") returned zero hits, so it is reported as not found. Next are the CHEBI queries.

CHEBI is complete. Last set is the NCIT queries.

## Report

Both pages were read. The first is a review (PMC5623937), where the first ~40k characters were verbatim and the rest is a model summary. Its summary contradicts the verbatim text, so I used only the verbatim part. The second is Singeisen 2023, where the Europe PMC abstract is verbatim and the PMC full text's first ~40k characters are verbatim. Its summary also contradicts the verbatim text, so I used only the verbatim part there too. Both sources are non-preapproved, so quotes are kept short and the rest is paraphrased.

### 1. Alrezk R et al., Endocr Relat Cancer 2017 (PMID 28824003)
URL read: https://pmc.ncbi.nlm.nih.gov/articles/PMC5623937/

**Germline CDKN1B variants (Table 1, 19 rows, all in the verbatim text):**

| # | Variant (as printed) | Age/sex | Clinical manifestations |
|---|---|---|---|
| 1 | p.W76X (c.692G>A) | 48 F | Acromegaly, PHPT |
| 2 | p.K25fs (c.59_77dup) | 47 F | Small-cell NE cervical carcinoma (45), ACTH-dependent Cushing, PHPT, MS (46) |
| 3 | ATG-7G>C, 5'UTR | 61 F | Bilateral nonfunctional adrenal masses, uterine fibroids, PHPT |
| 4 | p.P95S (c.283C>T) | 50 F | ZES with duodenal and pancreatic-tail masses, PHPT |
| 5 | Stop>Q (c.595T>C) | 50 F | PHPT (monozygotic twin also carries it) |
| 6 | p.P69L (c.678C>T) | 79 F | Papillary thyroid carcinoma with nodal metastases, metastatic bronchial carcinoid, PHPT, nonfunctioning pituitary microadenoma, T2DM |
| 7 | p.G9R (c.25G>A) | 68 M | PHPT |
| 8 | p.P133T (c.397C>A) | 58 F | PHPT |
| 9 | 5'UTR GAGA deletion (c.32_29delGAGA) | 69 F | Gastric NET, PHPT |
| 10 | p.A55T (c.163G>A) | 42 F | ZES with gastrinoma and hepatic metastases, PHPT |
| 11 | p.S125X (c.374_375delCT) | 53 F | GI NET, PHPT |
| 12 | p.E126D (c.378G>C) | 15 F | Early-onset PHPT, renal calculi, hypercalcemia |
| 13 | c.-456_-453delCCTT (5'UTR) | 62 F | Acromegaly (somatotropinoma), nonfunctional pNET |
| 14 | c.-29_-26delAGAG (5'UTR) | 6 F | Gigantism (somatotropinoma) |
| 15 | p.I119T (c.356T>C) | NA | AIP-negative FIPA, GH adenoma |
| 16 | p.K96Q (c.286A>C) | NA | AIP-negative FIPA, hyperprolactinemia, breast cancer at 41 |
| 17 | c.-80C>T | NA | PHPT |
| 18 | c.-29_-26delAGAG | NA | PHPT |
| 19 | c.397C>A | NA | PHPT |

Phenotype counts from the text: 19 cases in the literature; PHPT in 15/19 (~80%), pituitary adenomas in 7/19 (~37%), duodeno-pancreatic/gastric NETs in 7/19. Mean PHPT age is about 56 years in MEN4 versus about 25 in MEN1, with female predominance. CDKN1B mutations are estimated at 1.5–3.7% of MEN1-like patients without MEN1 mutations.

**p27 domains (CDK inhibitory domain, NLS, scatter domain, Thr187, SKP2):** Not in the verbatim text. The summary's claim that these are absent is unverified, so I cannot confirm them from this fetch.

**Somatic CDKN1B in sporadic tumors (parathyroid, breast, prostate, small-intestine NET, lymphoma):** The verbatim text gives only general statements: point mutations in the coding region are "not common" in sporadic tumors, with LOH in some tumors and reduced expression or degradation in others. The tumor-specific findings and counts are not in the verbatim text. The summary's tumor-specific claims (including breast p.Q104X and adult T-cell lymphoma p.W76X) are unverified and I am not reporting them as facts.

**Screening and management (verbatim):**
- Confirming MEN4 "should only be made with genetic testing for CDKN1B mutations."
- Menin-negative MEN1 cases should be carefully assessed for possible MEN4.
- Pituitary surveillance is case-by-case, following existing MEN guidelines.
- Parathyroid surgery should be individualized; some patients may be treated like MEN1 with 3.5-gland resection. No reported MEN4 case had recurrence after resection.

### 2. Singeisen H et al., Endocr Connect 2023 (PMID 36520683)
Europe PMC metadata and abstract read: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A36520683&format=json&resultType=core
Full text read: https://pmc.ncbi.nlm.nih.gov/articles/PMC9874964/ (PMCID PMC9874964, DOI 10.1530/EC-22-0411, 12(2):e220411, published 2023-01-24, CC BY-NC-ND)

**Abstract numbers:**
- 48 symptomatic patients met the criteria (PRISMA 2020; MEDLINE and Web of Science, January 2006 to August 2022).
- 28 different CDKN1B variants: missense 21/48 (44%), frameshift 17/48 (35%).
- Women 36/48 (75%). Men's median age at symptom onset 32.5 (range 10–68); women's 49.5 (range 5–76), P = 0.25.
- Parathyroid 36/48 (75%), uniglandular 31/36 (86%). Pituitary 21/48 (44%), hormone-secreting 16/21 (76%). Endocrine pancreas 7/48 (15%). Thyroid 4/48 (8%). Adrenal 3, thymus 2.
- First presenting organ: parathyroid 27/48 (56%), pituitary 11/48 (23%).
- Number of affected organs: 1 in 27/48 (56%), 2 in 13/48 (27%), 3 in 3/48 (6%), 4 in 5/48 (10%).
- Prevalence is estimated at less than one per million.

**Full text (verbatim portion):**
- Inclusion: 20 publications with 64 patients, plus one case from the authors' hospital (a 54-year-old woman with c.349C>T, p.P117S, plus MEN1-like features and papillary thyroid cancer) gives 65 individuals. These were 48 symptomatic and 17 asymptomatic carriers (median age 47.5, range 16–76).
- Variant types across 65: missense 29/65 (45%), frameshift 22/65 (34%), nonsense 8/65 (12%), small deletions 6/65 (9%), unspecified 1/65.
- Sex across 65: women 47/65 (72%), men 16/65 (25%).
- Symptomatic age at first presentation: median 43.5 (range 5–76, mean 42.2 ± 20.8). Women's median 49 (range 5–76); men's median 34 (range 10–70) in the 65-case set.
- Sporadic vs. familial: 24 sporadic; 24 in 11 families, median 3 affected members (range 2–13).
- Per-organ, from the text:
  - PHPT 36/48 (75%): multiglandular 5/36 (14%), recurrent 2/36 (6%); women 29/36 (81%); median age at PHPT diagnosis 51 (range 15–74).
  - Pituitary 21/48 (44%): nonfunctioning 5, hormone-secreting 16 (7 ACTH, 5 prolactin, 4 GH); 10 microadenomas, 5 macroadenomas, 6 unspecified; median age 39 (range 5–79).
  - GEP-NET 9/48 (19%): nonfunctioning pancreatic NET 4 (1 metastatic); gastrinoma 3 (2 metastatic); stomach NET 1 (nonmetastatic) and ileal NET 1 (metastatic). Total metastatic: 4 of 9.
  - Papillary thyroid carcinoma 4/48 (8%): all women, median age 57.5 (range 55–64), 3 multifocal.
  - Adrenal 3; thymus 2 (one thymic hyperplasia with myasthenia gravis, one atypical carcinoid with ectopic Cushing); lung carcinoid metastatic 1; renal angiomyolipoma 2.
- Conclusion (verbatim): "MEN4 is an extremely rare disease, which most frequently affects women around 50 years of age."

**Table 2 variant list (48 symptomatic rows, distinct variants with reference and phenotype).** The 48-row table is in the verbatim text. Listed below by variant as printed:
- c.227G>A, p.W76* (Pellegata; PHPT, GH adenoma; age 30)
- c.59_77dup19 (p.K25fs) (Georgitsi; PHPT, ACTH adenoma)
- c.-7G>C (PHPT)
- c.283C>T, p.P95S (PHPT, gastrinoma)
- c.595T>C, p.*199Qext60 (2 rows, PHPT)
- c.678C>T, p.P69L (PHPT, nonfunctioning adenoma, papillary cancer)
- c.206C>T, p.P69L (PHPT, nonfunctioning adenoma)
- c.25G>A, p.G9R (PHPT)
- c.397C>A, p.P133T (3 rows, PHPT, one with papillary cancer)
- c.163G>A, p.A55T (PHPT, gastrinoma)
- c.286A>C, p.K96Q (PRL adenoma)
- c.356C>T or T>C, p.I119T (3 rows, GH or ACTH adenoma)
- c.-32_-29delGAGA (PHPT)
- c.-456_-453delCCTT (GH adenoma, nonfunctioning NET)
- c.374_375delCT, p.S125* (PHPT, gastrinoma; the second row is a nonsense call with a p.S125c label)
- c.378G>C, p.E126D (PHPT)
- c.-29_-26delAGAG (3 rows, GH or ACTH adenoma, PHPT)
- c.-80C>7 (typo as printed, PHPT)
- c.121_122delTT, p.L41Nfs*83 (13 rows, all from the Danish family; mostly PHPT, some nonfunctioning adenoma or NET)
- c.285dupC, p.K96Qfs*29 (PHPT)
- c.407A>G, p.D136G (ACTH adenoma)
- c.376G>C, p.E126Q (ACTH adenoma)
- c.320delA, p.Q107Rfs*12 (ACTH adenoma)
- c.281C>T, p.P94L (PHPT, papillary cancer)
- c.482C>G, p.S161C (NET)
- c.179G>A, p.W60* (PHPT, adenoma, NET)
- c.475G>A, p.D159N (PHPT)
- c.349C>T, p.P117S (the authors' case)

Note the cDNA discrepancies between the two papers. The W76X variant is c.692G>A in Table 1 of the 2017 review but c.227G>A in Table 2 of the 2023 paper. The P69L variant is c.678C>T in one row and c.206C>T in another.

**Not retrieved:**
- The per-variant HGVS counts are not fully tallied here; the 48 rows are listed above, but row counts for some variants are from my own tally.
- Supplementary Tables 1–3 and Table A (supplemental online material) were not fetched.
- The PRISMA flow diagram (Figure 1) was not read, so record counts are unknown.
- The full Discussion beyond the first ~40k characters was not verified.

**Summary:** Endpoints 1, 2, 3, and 4 all returned HTTP 200. The Monarch association list (endpoint 3) was truncated, so the full 50-record list is not verified. I have verbatim data for about a dozen records and model-extracted summaries for most of the rest.

## Endpoint results

**1. https://ontology.jax.org/api/network/annotation/OMIM:610755: HTTP 200.** Returned disease `OMIM:610755`, name "Multiple endocrine neoplasia, type IV", mondoId `MONDO:0012552`. The HPO terms are grouped by category, with frequency and onset metadata:
- Neoplasm: HP:0002893 Pituitary adenoma (no frequency; OMIM); HP:0030405 Pancreatic endocrine tumor (frequency "1/1", PMID:24819502); HP:0030731 Carcinoma (no frequency); HP:0006772 Renal angiomyolipoma (no frequency); HP:0100570 Carcinoid tumor (no frequency); HP:0002897 Parathyroid adenoma (frequency "1/1", PMID:24819502)
- Inheritance: HP:0000006 Autosomal dominant inheritance
- Endocrine: HP:0000821 Hypothyroidism ("1/1"); HP:0008200 Primary hyperparathyroidism ("1/1"); HP:0000843 Hyperparathyroidism ("1/1"); HP:0000845 Elevated circulating growth hormone concentration (no frequency); HP:0000872 Hashimoto thyroiditis ("1/1")
- Gene: NCBIGene:1027 CDKN1B

Onset is empty in every record. The "1/1" values are case counts from one publication, not HPO frequency terms.

**2. https://api-v3.monarchinitiative.org/v3/api/entity/MONDO:0012552: HTTP 200.** Returned `"has_phenotype_count":44` in `has_phenotype` (an ID array) and `has_phenotype_label` (a separate label array). The two arrays are not explicitly paired, so I have not matched IDs to labels from this endpoint alone. The 44 IDs are: HP:0002574, HP:0008208, HP:0002044, HP:0000854, HP:0001031, HP:0000843, HP:0000821, HP:0007449, HP:0008283, HP:0100633, HP:0003165, HP:0006767, HP:0010615, HP:0012197, HP:0000872, HP:0008256, HP:0010783, HP:0012334, HP:0000845, HP:0030688, HP:0100634, HP:0000825, HP:0012030, HP:0004398, HP:0003118, HP:0008291, HP:0030079, HP:0003072, HP:0100522, HP:0100570, HP:0002014, HP:0011761, HP:0002893, HP:0008200, HP:0030405, HP:0030445, HP:0000818, HP:0002897, HP:0011760, HP:0030731, HP:0006772, HP:0012091, HP:0006780, HP:0010788.

The same record shows `association_counts` with "Disease to Phenotype" count 50. The 44 versus 50 difference is unexplained by the response. It also returned the parent terms, the causal gene HGNC:1785, and the mappings.

**3. https://api-v3.monarchinitiative.org/v3/api/association?subject=MONDO:0012552&category=biolink:DiseaseToPhenotypicFeatureAssociation&limit=100: HTTP 200, truncated.** The response reports `"total":50` and `"limit":100`. The page is about 351k characters, so I read it in three windows.

- Verbatim records, no frequency qualifier (`frequency_qualifier` null): HP:0002893 Pituitary adenoma; HP:0008200 Primary hyperparathyroidism (PMID:24819502); HP:0100570 Carcinoid tumor; HP:0000821 Hypothyroidism (PMID:24819502); HP:0030405 Pancreatic endocrine tumor (PMID:24819502); HP:0030731 Carcinoma; HP:0006772 Renal angiomyolipoma.
- Verbatim records, with frequency (Orphanet-sourced): HP:0000843 Hyperparathyroidism, `HP:0040281`; HP:0006780 Parathyroid carcinoma, `HP:0040283` ("Occasional"); HP:0007449 Confetti-like hypopigmented macules, `HP:0040283` ("Occasional"); HP:0012030 Increased urinary cortisol level, `HP:0040283` ("Occasional"); HP:0012334 Extrahepatic cholestasis, `HP:0040283` ("Occasional").
- Summary only (model-extracted, not verbatim, so unverified): HP:0002897 Parathyroid adenoma (Very frequent); HP:0008208 Parathyroid hyperplasia (Very frequent); HP:0000818 Abnormality of the endocrine system (Very frequent); HP:0003072 Hypercalcemia (Very frequent); HP:0003165 Elevated circulating parathyroid hormone level (Very frequent); HP:0002014 Diarrhea, HP:0002044 Zollinger-Ellison syndrome, HP:0002574 Episodic abdominal pain, HP:0006767 Pituitary prolactin cell adenoma, HP:0011761 Pituitary null cell adenoma, HP:0012091 Abnormality of pancreas physiology, HP:0100634 Neuroendocrine neoplasm, HP:0002893 Pituitary adenoma, HP:0008256 Adrenocortical adenoma, HP:0008283 Fasting hyperinsulinemia, HP:0010615 Angiofibromas, HP:0011760 Pituitary growth hormone cell adenoma, HP:0012197 Insulinoma, HP:0030445 Pulmonary carcinoid tumor, HP:0100633 Esophagitis (all Frequent); HP:0030079 Cervix cancer (Occasional); HP:0100522 Thymoma (Very rare); HP:0003118 Increased circulating cortisol level (Occasional, label not visible).

Not read: the window from about character 39,842 to 139,842, and the last 71,192 characters. The model summary covers those parts, so records 13 to 50 are not verified. Frequency labels in the summary follow the HPO scheme (HP:0040281 Very frequent, HP:0040282 Frequent, HP:0040283 Occasional, HP:0040284 Very rare). I did not verify those mappings against the response.

**4. https://ontology.jax.org/api/hp/terms/HP:0008207: HTTP 200.** `"id":"HP:0008207"`, `"name":"Primary adrenal insufficiency"`. Definition: "Insufficient production of steroid hormones (primarily cortisol) by the adrenal glands as a result of a primary defect in the glands themselves." The API base is working.

## Failures from the first round

The earlier HPO URLs (`ontology.jax.org/api/network/annotation/MONDO:0012552`, `ontology.jax.org/api/hp/diseases/OMIM:610755`, `hpo.jax.org/api/hpo/disease/OMIM:610755`) returned HTTP 404 each. Those are permanent failures.

## Gap

The complete 50-record list with frequency and onset is not yet verified. The remaining records can be retrieved with a smaller page or a different offset on the Monarch association endpoint. The 44-ID entity list and the endpoint 1 categories are the cleanest sources for the set of HP terms. Onset qualifiers were null in every record I read.

All 100 queries were run against the OLS4 search endpoint (`rows=5`, `exact=false`), one request per query because the API takes one query per call. Each line is query -> OBO ID -> label. Where the label differs from the query, the match came through a synonym, or the top hit is weak, I say so.

**HPO**
- primary hyperparathyroidism -> HP:0008200 -> Primary hyperparathyroidism
- hypercalcemia -> HP:0003072 -> Hypercalcemia
- elevated circulating parathyroid hormone level -> HP:0003165 -> Elevated circulating parathyroid hormone level
- parathyroid adenoma -> HP:0002897 -> Parathyroid adenoma
- pituitary adenoma -> HP:0002893 -> Pituitary adenoma
- growth hormone excess -> HP:0000845 -> Elevated circulating growth hormone concentration (matched via exact synonym "Growth hormone excess")
- acromegaly -> HP:0033794 -> Acral overgrowth (weak: "Acromegaly" is only a related synonym of this term). The closer match is HP:0000845, which is listed above; I'd use that one.
- prolactinoma -> HP:0006767 -> Pituitary prolactin cell adenoma (matched via exact synonym "Prolactinoma")
- hyperprolactinemia -> HP:0000870 -> Increased circulating prolactin concentration (matched via exact synonym "Hyperprolactinemia")
- Cushing syndrome -> HP:0003118 -> Increased circulating cortisol level (matched via exact synonym "Cushing syndrome"). No term labelled "Cushing syndrome" came back.
- ACTH-secreting pituitary adenoma -> HP:0008291 -> Pituitary corticotropic cell adenoma (matched via exact synonym "ACTH-producing pituitary adenoma")
- nephrolithiasis -> HP:0000787 -> Kidney stone (matched via exact synonym "Nephrolithiasis")
- nephrocalcinosis -> HP:0000121 -> Nephrocalcinosis
- osteoporosis -> HP:0000939 -> Osteoporosis
- neuroendocrine neoplasm -> HP:0100634 -> Neuroendocrine neoplasm
- pancreatic endocrine tumor -> HP:0030405 -> Pancreatic endocrine tumor
- gastrinoma -> HP:0034953 -> Duodenal gastrinoma (no plain "Gastrinoma" term came back; this is a narrower term)
- Zollinger-Ellison syndrome -> HP:0002044 -> Zollinger-Ellison syndrome
- carcinoid tumor -> HP:0100570 -> Carcinoid tumor
- thymoma -> HP:0100522 -> Thymoma
- bronchial carcinoid -> not found. The only hit was HP:0033377 "Increased airway neuroendocrine cells", which is not a match. HP:0030445 "Pulmonary carcinoid tumor" appeared in the "carcinoid tumor" query and may be what you want, but I did not see it in this query's results.
- adrenocortical adenoma -> HP:0008256 -> Adrenocortical adenoma
- papillary thyroid carcinoma -> HP:0002895 -> Papillary thyroid carcinoma
- medullary thyroid carcinoma -> HP:0002865 -> Medullary thyroid carcinoma
- meningioma -> HP:0002858 -> Meningioma
- multiple endocrine neoplasia -> not found. The only hit was HP:0002044 Zollinger-Ellison syndrome, which is not a match.
- autosomal dominant inheritance -> HP:0000006 -> Autosomal dominant inheritance
- incomplete penetrance -> HP:0003829 -> Typified by incomplete penetrance (matched via exact synonym "Incomplete penetrance")

**UBERON**
- parathyroid gland -> UBERON:0001132 -> parathyroid gland
- adenohypophysis -> UBERON:0002196 -> adenohypophysis
- pituitary gland -> UBERON:0000007 -> pituitary gland
- pancreas -> UBERON:0001264 -> pancreas
- duodenum -> UBERON:0002114 -> duodenum
- thymus -> UBERON:0002370 -> thymus
- adrenal cortex -> UBERON:0001235 -> adrenal cortex
- adrenal gland -> UBERON:0002369 -> adrenal gland
- thyroid gland -> UBERON:0002046 -> thyroid gland
- ileum -> UBERON:0002116 -> ileum
- stomach -> UBERON:0000945 -> stomach
- lung -> UBERON:0002048 -> lung
- kidney -> UBERON:0002113 -> kidney
- bone -> not found. The top hit was UBERON:0004251 "hindlimb zeugopod bone", which is not a match.
- meninx -> UBERON:0002360 -> meninx

**Cell Ontology**
- parathyroid chief cell -> CL:0000446 -> chief cell of parathyroid gland (matched via exact synonym "parathyroid chief cell")
- corticotroph -> CL:0002309 -> corticotroph
- somatotroph -> CL:0002312 -> somatotroph
- lactotroph -> CL:0002311 -> mammotroph (matched via exact synonym "lactotroph")
- gonadotroph -> CL:0000437 -> gonadtroph (the label is misspelled in OLS; the exact synonym "gonadotroph" is spelled correctly)
- pancreatic endocrine cell -> CL:0008024 -> pancreatic endocrine cell
- enteroendocrine cell -> CL:0000164 -> enteroendocrine cell
- chromaffin cell -> CL:0000166 -> chromaffin cell
- parafollicular cell -> CL:0000570 -> parafollicular cell
- adrenal cortex cell -> CL:0002097 -> cortical cell of adrenal gland (matched via exact synonym "adrenal cortex cell")

**GO**
- negative regulation of cyclin-dependent protein serine/threonine kinase activity -> not found. The query returned zero results.
- G1/S transition of mitotic cell cycle -> GO:0000082 -> G1/S transition of mitotic cell cycle
- cyclin-dependent protein kinase holoenzyme complex -> GO:0000307 -> cyclin-dependent protein kinase holoenzyme complex
- negative regulation of cell population proliferation -> GO:0008285 -> negative regulation of cell population proliferation
- cell cycle arrest -> not found as a label. The top hit was GO:0051726 "regulation of cell cycle", where "cell cycle arrest" appears only as a narrow synonym.
- nucleus -> GO:0005634 -> nucleus
- cytoplasm -> GO:0005737 -> cytoplasm
- protein kinase inhibitor activity -> GO:0004860 -> protein kinase inhibitor activity
- regulation of translational initiation -> GO:0006446 -> regulation of translational initiation

**CHEBI**
- cinacalcet -> CHEBI:48390 -> cinacalcet
- cabergoline -> CHEBI:3286 -> cabergoline
- lanreotide -> CHEBI:135901 -> lanreotide
- octreotide -> CHEBI:7726 -> octreotide
- pasireotide -> CHEBI:72312 -> pasireotide
- everolimus -> CHEBI:68478 -> everolimus
- calcium(2+) -> CHEBI:29108 -> calcium(2+)

**NCIT**
- Parathyroidectomy -> NCIT:C51593 -> Parathyroidectomy
- Transsphenoidal Hypophysectomy -> not found. The query returned zero results.
- Cabergoline -> NCIT:C47428 -> Cabergoline
- Cinacalcet -> NCIT:C74100 -> Cinacalcet (NCIT:C47450 "Cinacalcet Hydrochloride" is also present)
- Somatostatin Analogue -> not found as an exact label. The top hit was NCIT:C74034 "Gallium Ga 68-DOTANOC", which is not a match. NCIT:C15449 "Somatostatin Analog Therapy" is the closest title, but it is a therapy term, not a drug-class term.
- Proton Pump Inhibitor -> NCIT:C29723 -> Proton Pump Inhibitor
- Genetic Counseling -> NCIT:C15240 -> Genetic Counseling
- Magnetic Resonance Imaging -> NCIT:C16809 -> Magnetic Resonance Imaging
- Pancreatectomy -> NCIT:C15294 -> Pancreatectomy
- Everolimus -> NCIT:C48387 -> Everolimus

Every ID above is one the search returned; none were filled in from memory. The "not found" entries (bronchial carcinoid, multiple endocrine neoplasia, bone, cell cycle arrest, the GO kinase query, Transsphenoidal Hypophysectomy, and Somatostatin Analogue) may need a different query wording or a browser check on OLS4.

## Report 1: Chasseloup et al., JCEM 2020 (PMC7190031): retrieved, with caveats

**Final URL read:** https://pmc.ncbi.nlm.nih.gov/articles/PMC7190031/ (DOI 10.1210/clinem/dgaa160; J Clin Endocrinol Metab 2020 Mar 31;105(6):1983–2005; PMID 32232325)

**Caveat:** The page was cut at about 39,942 of 138,554 characters. The rest came as a model-extracted summary, so the patient table, functional percentages, IHC percentages, and conclusions below rest partly on that summary. Where the verbatim text was available, it is marked as such.

**Cohort (verbatim abstract and results):**
- 211 CD patients screened, of whom 199 were pediatric (≤18 years at onset) and 12 adult. The abstract states 94.3% pediatric.
- 117 female (55.5%) and 94 male (44.5%).
- Screening methods: germline WES only (n=157), germline plus tumor WES (n=27), Sanger (n=6), and/or germline CNV analysis (n=194).
- The denominator for the variant rate is 190 patients tested by WES or Sanger. Five variant carriers gives 2.6%.
- Pediatric age at onset was 10 (IQR 8–12.9) years. Adult onset was 38.8 ± 9.5 years.
- Mean age at onset of the five carriers was 10.5 ± 1.3 years (abstract).
- No CNVs were found.

**The five CDKN1B variants (verbatim Table 3, which is cut off partway through the E126Q row):**

| HGVS (cDNA; protein) | Location | Notes |
|---|---|---|
| c.-29_-26delAGAG; p.? | 5′ UTR, intronic | rs774454456; VarSome ACMG "Likely benign" |
| c.320delA; p.Q107Rfs*12 | Exon 1, frameshift | rs755301027; VarSome ACMG "Likely pathogenic" |
| c.356T>C; p.I119T | Exon 1, missense | rs142833529; MAF 0.0545%; VarSome ACMG "Likely benign" |
| c.376G>C; p.E126Q | Exon 1, missense | Not in gnomAD; VarSome ACMG "VUS" |
| c.407A>G; p.D136G | Exon 1, missense | MAF 0.0075% (per the text); ACMG not visible in retrieved text |

The abstract describes the classifications as "variants of uncertain significance (n = 2) or pathogenic/likely pathogenic (n = 3)". The verbatim Table 3 values do not clearly match that split. The model summary gave different classifications (c.320delA "Pathogenic", c.407A>G "VUS", I119T "VUS", E126Q "Likely pathogenic", c.-29 "Likely pathogenic"). I could not resolve this from the verbatim text. Treat the per-variant ACMG labels as unverified and check the full article or Table 3 directly.

**Patients (from the model summary only; not verbatim):**

| Case | Sex | Onset / diagnosis (years) | Other MEN4 features |
|---|---|---|---|
| 1 | M | 10 / 13.6 | None reported |
| 2 | M | 12.5 / 15.8 | None in the patient; mother had colon adenocarcinoma and carried the variant |
| 3 | F | 10 / 13.8 | None reported; somatic USP8 p.P720R also present |
| 4 | F | 9 / 12 | None reported; family history of obesity, diabetes, hypertension |
| 5 | M | 11 / 15.6 | None reported |

The summary also says the authors consider these patients "MEN4 cases," with CD as the only MEN4 feature so far. The summary and the paper disagree on which case's mother had the colon adenocarcinoma (Case 2 or Case 3).

**In vitro functional findings:**
- Verbatim abstract: "In vitro assays demonstrated protein instability and disruption of the scatter domain of CDKN1B for all variants tested."
- Verbatim methods: AtT20 cells (POMC/ACTH and localization), cycloheximide chase at 25 µM, HEK293 coimmunoprecipitation with RHOA and CDKs, and half-life analysis by one-phase decay with extra sum-of-squares F test.
- Summary only: localization in AtT20 cells. WT, I119T, and D136G were exclusively nuclear. E126Q was nuclear-predominant with moderate cytoplasmic staining. Q107Rfs*12 was purely cytoplasmic.
- Summary only: Q107Rfs*12 had the shortest half-life, and all missense variants degraded significantly faster than WT. Exact half-lives are only in a figure, which I could not read.
- Summary only: scatter domain (residues 118–158). RHOA binding reduced by 70% (Q107Rfs*12), 30% (I119T), 70% (E126Q), and 60% (D136G). CDK2 binding changed by +10% (Q107Rfs*12) and by −40%, −80%, and −50% (I119T, E126Q, D136G).
- Summary only: Q107Rfs*12 raised POMC (1.62 vs 1.08 for WT, P = .0451). Missense variants had no effect on POMC or ACTH.

**CDKN1B IHC in corticotropinomas (summary only):**
- Case 1: moderate to strong nuclear staining in about 30% of cells.
- Case 3: weak to moderate nuclear staining in about 20% of cells.
- Case 5: moderate to strong nuclear staining in about 55% of cells.
- Occasional moderate cytoplasmic staining in all three.
- Cases 2 and 4: not available. Case 4's tumor was classified as a PitNET without IHC.
- The antibody was BD Biosciences 610242, mouse monoclonal, at 1:1000 (verbatim methods).

**Authors' conclusions:**
- Verbatim abstract: the finding that germline CDKN1B loss-of-function "may present as apparently sporadic, isolated pediatric CD has important implications for clinical screening and genetic counselling."
- Summary only: the variants are a putative pathogenic cause of MEN4, and the carriers should be followed as MEN4 cases. CDKN1B variants are "a rare cause of CD" to keep in mind, especially in young patients. Broad screening is not recommended. Family screening is justified only for people at risk of carrying a pathogenic or likely pathogenic variant.

## Report 2: Bencivenga et al., Cells 2025 (PMC11817124): not retrieved

**URL attempted:** https://pmc.ncbi.nlm.nih.gov/articles/PMC11817124/

**Result:** HTTP 200, but the response was a reCAPTCHA browser check ("Checking your browser before accessing pmc.ncbi.nlm.nih.gov"), not the article. This is a permanent block for this request, so sending the same URL again would likely return the same challenge. I did not try other hosts or mirrors, since the instructions bar working around a failed fetch.

**Not retrieved:** the four CDKN1B variants and their HGVS names, the cell lines, the proliferation, migration, and phosphorylation results (Thr187, Ser10, Thr198, Tyr88), subcellular localization, stability and half-life, cyclin/CDK binding, the statements on the CDK inhibitory domain, NLS, and scatter domain, and the statements on non-canonical cytoplasmic and oncogenic p27 functions.

**Suggested next step:** retrieve the article from the publisher's site (DOI and PMID 39936980 are known to the caller), or provide the article text directly.

## CDKN1B (P46527) report

All five endpoints returned HTTP 200. The only blocked endpoint was the ClinVar web page, which is bot-gated. The UniProt and EBI responses were truncated, so some fields rest on a model-extracted summary, noted below.

### 1. UniProt P46527 (https://rest.uniprot.org/uniprotkb/P46527.json)

The response was truncated at 39,938 of 79,867 characters. Everything below is verbatim from the readable part unless marked as summary.

- **Name:** Cyclin-dependent kinase inhibitor 1B (aliases p27Kip1, p27). Entry CDN1B_HUMAN, reviewed (Swiss-Prot).
- **Length:** 198 aa (the Chain feature runs 1–198). The summary gives MW 22,073 Da.
- **Subcellular location:** Nucleus, Cytoplasm, Endosome (Endosome is ECO:0000250, by similarity). Nuclear and cytoplasmic in quiescent cells.
- **CC FUNCTION:** "Important regulator of cell cycle progression." It inhibits CDK2 bound to cyclin A and is a potent inhibitor of cyclin E– and cyclin A–CDK2. It is involved in G1 arrest and acts on cyclin D–CDK4 as either an inhibitor or activator, depending on phosphorylation state or stoichiometry.
- **Domains and regions:**
  - DOMAIN comment: a peptide containing only AA 28–79 retains substantial cyclin A/CDK2 inhibitory activity. No feature is named "CDK inhibitory domain," "scatter domain," or "kinase inhibitory domain."
  - Region 51–91: "Interaction with CDK2."
  - Motif 153–169: "Nuclear localization signal."
  - Disordered regions: 1–34 and 85–198.
- **Modified residues (verbatim feature positions):**
  - Ser10: phosphoserine, by UHMK1.
  - Tyr74: phosphotyrosine, by SRC.
  - Tyr88: phosphotyrosine, by ABL, LYN, SRC and JAK2.
  - Tyr89: phosphotyrosine.
  - Thr157: phosphothreonine, by CaMK1, PKB/AKT1 and PIM1.
  - Thr170: phosphothreonine (ECO:0000250, from P46414).
  - Thr187: phosphothreonine, by PKB/AKT1, CDK1 and CDK2.
  - Thr198: phosphothreonine, by CaMK1, PKB/AKT1, RPS6KA1, RPS6KA3 and PIM1.
- **Interaction partners:** The CC INTERACTION table, which is verbatim, includes CDK2 (32 experiments), CCNA2 (21), CCNE1 (12), CDK4, CDK1, SKP2 (4) and CDK5, among others. CKS1B is not in the INTERACTION table, but the SUBUNIT text says "Identified in a complex with SKP1, SKP2 and CKS1B." GRB2 is named in SUBUNIT as "Interacts with GRB2."
- **Involvement in disease (verbatim):** "Multiple endocrine neoplasia 4" (acronym MEN4, DI-02004, MIM 610755). The description is "MEN4 is a MEN-like syndrome with a phenotypic overlap of both MEN1 and MEN2." It is supported by PubMed 17030811.
- **Natural variants (verbatim, 3 in the readable part):**
  - Arg15Trp (rs2066828). No disease association is listed.
  - Pro69Leu (rs777354267). "found in a patient with multiple endocrine tumors; germline mutation; reduced expression levels; shows impaired binding to CDK2."
  - Val109Gly (rs2066827). No disease association is listed.

### 2. EBI variation API (https://www.ebi.ac.uk/proteins/api/variation/P46527)

The response is 2,236,566 characters. The first 39,933 were read, and the final 2,096,633 were not read. Total variant count and total disease-associated count could not be determined from this read.

- **Verbatim, readable part:** several MEN4-annotated entries at the start:
  - Asn3fs (rs2497403571): Pathogenic, disease flag true, MEN4.
  - Arg5Ter (rs1349668409): Likely pathogenic, disease flag true. Its association is "Hereditary cancer-predisposing syndrome," and it also carries a MEN4 association.
  - Val4Ala, Val4Leu and Val4Met: Variants of uncertain significance, MEN4 association.
- **Summary, not verbatim:** the model-extracted summary of the rest reports about 31 visible entries at positions 5–12, with 25 annotated as MEN4. Its table reports Val6fs and Ser7fs as Pathogenic and Likely pathogenic, and Asn8Ter as Pathogenic. The summary's table starts at position 5 and omits the position 3–4 entries above, so treat its counts as approximate.
- To read further, the tool suggests offset 139933.

### 3. ClinVar

- **Web page:** https://www.ncbi.nlm.nih.gov/clinvar/?term=CDKN1B%5Bgene%5D returned HTTP 200 with a reCAPTCHA interstitial ("Checking your browser before accessing www.ncbi.nlm.nih.gov"). It is bot-gated, so no records were read.
- **Total CDKN1B records:** https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=clinvar&term=CDKN1B%5Bgene%5D&retmax=0&retmode=json returned HTTP 200 with `"count":"1210"`.
- **P/LP subset:** the query with `"pathogenic"` OR `"likely pathogenic"` returned HTTP 200 with `"count":"275"`. The query translation shows these phrases matched under [All Fields], not [clinical significance], so 275 is not a strict clinical-significance count. The translation shows no phrases not found.

**Scope note / interpretation:** This report covers **MONDO:0012552 — multiple endocrine neoplasia type 4 (MEN4)**, the autosomal dominant tumor-predisposition syndrome caused by germline heterozygous pathogenic variants in **CDKN1B** (HGNC:1785, 12p13.1, encoding p27^Kip1), OMIM:610755 (phenotype) / OMIM:600778 (gene). The identifiers were verified against the MONDO record and HGNC. Throughout, I keep the **germline syndrome** separate from **somatic CDKN1B-mutant sporadic tumors** (§4, §6) and from the **biallelic CDKN1B-deficiency overgrowth/neurodevelopmental phenotype** (§4), which is allelic but a different entity.

**Retrieval limitations, stated up front (attribution integrity):** OMIM (610755, 600778), Orphanet (ORPHA:276152), NCBI Gene, StatPearls (NBK568728), EndoText, ClinVar's web interface, and the Bencivenga 2025 full text were **not retrievable in this session** (HTTP 403, reCAPTCHA interstitials, or HTTP 429). Where I cite content normally found in those resources, I cite the source I actually read instead, and I flag gaps explicitly rather than filling them from memory. Several full texts were read only partially (publisher pages truncate); I mark those claims. **Primary anchor retrieved in full: GeneReviews "Multiple Endocrine Neoplasia Type 4" (Brock P, Kirschner L; posted 21 Sep 2023; PMID 37733893; NBK594826).**

---

# 1. Disease Information

## Overview

MEN4 is a rare autosomal dominant multiple endocrine neoplasia syndrome caused by germline loss-of-function variants in **CDKN1B**, which encodes the cyclin-dependent kinase inhibitor **p27^Kip1**. Its core tumor spectrum is **primary hyperparathyroidism (PHPT)** and **anterior pituitary adenomas**, with a smaller contribution from **gastroenteropancreatic neuroendocrine tumors (GEP-NETs)** and thoracic/intestinal carcinoids. It phenocopies MEN1 but, in every cohort retrieved, is **more attenuated, lower-penetrance, and later-onset**.

GeneReviews states the condition is "characterized by endocrine tumors, especially parathyroid and/or pituitary," with substantial MEN1 overlap but a more attenuated course (GeneReviews NBK594826, PMID 37733893 — *source class: curated clinical-genetics guideline/expert review*).

The syndrome was defined in 2006 when Pellegata et al. mapped the spontaneous rat **MENX** syndrome to a homozygous *Cdkn1b* frameshift and then identified a germline **CDKN1B nonsense variant (p.W76\*)** in a MEN1-mutation-negative human with pituitary and parathyroid tumors, segregating with MEN1-like features across generations (PNAS 2006;103(42):15558–63, PMID 17030811; https://pubmed.ncbi.nlm.nih.gov/17030811/ — *primary literature*).

## Key identifiers (retrieved from MONDO via EBI OLS4 and HGNC REST)

| Resource | Identifier |
|---|---|
| MONDO | **MONDO:0012552** — "multiple endocrine neoplasia type 4" |
| OMIM (phenotype) | **610755** |
| OMIM (gene, CDKN1B) | **600778** |
| Orphanet | **ORPHA:276152** |
| DOID | DOID:0080137 |
| NCIT | NCIT:C157449 |
| MeSH | C567059 |
| UMLS | C1970712 |
| MedGen | 373469 (UID), CUI C1970712 |
| SNOMED CT | 715907003 |
| GARD | 0017275 |
| ICD-11 Foundation | 157945677 |
| HGNC (gene) | **HGNC:1785**, CDKN1B, 12p13.1 |
| Ensembl / MANE Select | ENSG00000111276 / ENST00000228872.9, **NM_004064.5** |
| UniProt | **P46527** (CDN1B_HUMAN) |
| NCBI Gene | 1027; CCDS8653 |

MONDO definition (verbatim from the OLS4 record): *"Multiple endocrine neoplasia type 4 (MEN4) is a very rare form of MEN, an inherited cancer syndrome, characterized by parathyroid and anterior pituitary tumors, possibly associated with adrenal, renal, and reproductive organ tumors."* (https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?iri=...MONDO_0012552 — *structured ontology*)

MONDO parents: MONDO:0000426 (autosomal dominant disease), MONDO:0017169 (multiple endocrine neoplasia).

**Gap:** A discrete **ICD-10** code and a billable **ICD-11** stem code for MEN4 were **not retrieved**. MONDO carries only the ICD-11 Foundation URI (157945677). Do not assume "E31.2" (which is MEN type 1 territory in ICD-10) applies — that was not confirmed in this session.

## Synonyms (exact synonyms from MONDO:0012552)

- MEN4 (abbreviation)
- CDKN1B multiple endocrine neoplasia
- multiple endocrine neoplasia caused by mutation in CDKN1B
- multiple endocrine neoplasia, type IV
- *CDKN1B-related multiple endocrine neoplasia* (GeneReviews chapter synonym)
- *MEN1B* appears as a legacy alias in MedGen-derived listings (low confidence; retrieved only from a search snippet, not the primary record)

## Data provenance for this entry

Information is **almost entirely aggregated disease-level**: published case reports, two systematic reviews (Singeisen 2023; Halperin 2023), and one national laboratory-network retrospective (Chevalier 2024). There is **no MEN4 registry, no EHR-derived cohort, and no natural-history study**. The largest single-family dataset is a Danish 13-carrier kindred (Frederiksen 2019). This is the dominant limitation on every frequency, penetrance, and prognosis figure below.

---

# 2. Etiology

## Disease causal factors

**Monogenic, germline, autosomal dominant.** The sole established cause is a heterozygous loss-of-function germline variant in **CDKN1B** (GeneReviews NBK594826). UniProt P46527 records the disease association verbatim: *"Multiple endocrine neoplasia 4"* (acronym MEN4, DI-02004, MIM 610755), described as *"MEN4 is a MEN-like syndrome with a phenotypic overlap of both MEN1 and MEN2,"* supported by PubMed 17030811 (https://rest.uniprot.org/uniprotkb/P46527.json — *structured database*).

No environmental, infectious, or toxic cause is established or implicated. No multifactorial or polygenic contribution has been demonstrated.

## Genetic risk factors

**Causal:** germline heterozygous CDKN1B pathogenic/likely pathogenic variants — missense, frameshift, nonsense, small deletions, and non-coding 5′UTR/uORF variants (see §4). Detection yield in MEN1-like, MEN1-negative patients:

- Georgitsi 2007 / Agarwal 2009 / Molatore 2010, as summarized by GeneReviews: disease-causing CDKN1B variants in **<5%** of individuals with MEN1-like features and negative MEN1 testing (PMIDs 17519308, 19141585, 20824794).
- Alrezk 2017 (review, PMC5623937): **1.5–3.7%** of MEN1-like patients without MEN1 mutations (PMID 28824003).
- Chevalier 2024 (French TENGEN network, n=5,600 referred for MEN1 suspicion, 2015–2022): class 4/5 CDKN1B variants in **4/5,600 = 0.07%**; ~50/5,600 (~0.9%) had any class 3/4/5 variant before reclassification (JCEM 2024;109(7):e1482–e1493, PMID 38288531, DOI 10.1210/clinem/dgae055 — *retrospective national cohort*). Erratum: PMID 38470411.
- Chasseloup 2020 (pediatric Cushing disease cohort): CDKN1B variants in **2.6%** (5/190 tested) of a 211-patient Cushing disease cohort, 94.3% pediatric (JCEM 2020;105(6):1983–2005, PMID 32232325).
- Charnay 2026 (n=410 duodenopancreatic NET patients): **zero** CDKN1B (likely) pathogenic variants found; MEN1 in 27, NF1 in 8, VHL in 3 (J Neuroendocrinol, PMID 42971718 — *Europe PMC record; abstract-level*).

**Genotype-phenotype (modifier-like effects within CDKN1B itself)** — Halperin 2023 (Endocr Relat Cancer, PMID 36256846, DOI 10.1530/ERC-22-0174), pooled 74 MEN4 cases:
- Indels confer higher PHPT risk than point mutations (**log-rank P = 0.029**).
- Variants in **codons 94–96** confer higher risk of PHPT (**P < 0.001**) and pituitary adenoma (**P = 0.031**).
- Most common recurrent variant: **p.Q107fs**, in 4/41 kindreds.
(Abstract-level retrieval via Europe PMC + search snippets; **full text not retrieved** — ERC and ScienceDirect both returned HTTP 403.)

**Modifier genes:** none established. **Gap.**

**Susceptibility loci / GWAS:** no GWAS Catalog signal for MEN4 was retrieved; given monogenic etiology and extreme rarity, none is expected. Not assessed.

## Environmental risk factors

**None established.** Within the syndrome, the only consistently reported non-genetic risk modifiers are demographic:

- **Sex:** strong female excess. Singeisen 2023: **36/48 symptomatic (75%)** female; **47/65 (72%)** across all carriers (Endocr Connect 2023;12(2):e220411, PMID 36520683, PMC9874964). GeneReviews notes PHPT reported more often in women (**80% vs 58%**). Chevalier 2024 literature set: 17/29 women. Whether this is biological or ascertainment (women are calcium-screened more) is **not resolved in any retrieved source — this is an acknowledged gap, not a settled finding.**
- **Age:** age-dependent penetrance (§9).
- **Family history:** first-degree relatives of a carrier carry 50% a priori risk.

No toxin, radiation, occupational, dietary, or lifestyle exposure has been linked to MEN4 in any source I retrieved. CTD/TOXNET were not queried directly; **I found no literature signal in PubMed-indexed searches.**

## Protective factors

**No genetic or environmental protective factor is documented.** No protective allele, modifier, or dietary/lifestyle factor was found in any retrieved source. gnomAD-derived constraint (via a third-party mirror, GeneBe: LoF o/e ≈ 0.136–0.14, LoF Z ≈ 2.17, 1 observed vs ~7.36 expected LoF; pLI not reported) indicates CDKN1B is LoF-depleted in the population, which argues against common protective LoF alleles — but **this came from a mirror, not the gnomAD browser, and gnomAD v2/v4 constraint methods differ; treat as a lead, not a verified value.**

## Gene–environment interactions

**None demonstrated.** The only interaction-like finding retrieved is **gene–gene/somatic**: most MEN4 tumors lack a classical second hit (§6), so the rate-limiting event beyond the germline variant is unidentified. GeneReviews states explicitly that whether the mechanism is haploinsufficiency or loss of function through epigenetic silencing in addition to the germline variant "needs further research."

---

# 3. Phenotypes

## 3.1 Pooled tumor frequencies

Two independent pooled datasets, with different inclusion rules. **I present both rather than averaging them**, since denominators differ (symptomatic-only vs all carriers vs reclassified class 4/5 only).

**A. GeneReviews Table 2 (prevalence ranges, 2023) — *curated review*:**

| Tumor | Reported prevalence in MEN4 | Subtype breakdown |
|---|---|---|
| Parathyroid / PHPT | **55–80%** | single adenoma 86%; hyperplasia 14% |
| Anterior pituitary adenoma | **30–45%** | ACTH 33%, prolactin 24%, GH 19%, nonfunctioning 24% |
| Well-differentiated GEP-NET | **14–25%** | gastrinoma 33%, nonfunctioning 66% |
| Carcinoid (thymus/lung/small bowel) | **4–7%** | non-hormone-secreting |
| Adrenocortical | **4–7%** | cortisol-secreting or nonfunctioning |

**B. Singeisen 2023 systematic review (PRISMA 2020; MEDLINE + Web of Science, Jan 2006–Aug 2022; 20 publications + 1 institutional case = 65 individuals; 48 symptomatic, 17 asymptomatic carriers)** — *systematic review, the most rigorous denominator available*:

| Tumor | n/48 symptomatic | % | Median age at dx (range) |
|---|---|---|---|
| Parathyroid (PHPT) | 36/48 | **75%** | **51 y (15–74)**; uniglandular 31/36 (86%); multiglandular 5/36 (14%); recurrent 2/36 (6%); women 29/36 (81%) |
| Anterior pituitary adenoma | 21/48 | **44%** | **39 y (5–79)**; hormone-secreting 16/21 (76%): ACTH 7, PRL 5, GH 4; nonfunctioning 5; micro 10 / macro 5 / unspecified 6 |
| GEP-NET | 9/48 | **19%** | nonfunctioning pNET 4 (1 metastatic); gastrinoma 3 (2 metastatic); gastric NET 1; ileal NET 1 (metastatic) — **4/9 metastatic** |
| Endocrine pancreas (abstract framing) | 7/48 | 15% | — |
| Papillary thyroid carcinoma | 4/48 | **8%** | **57.5 y (55–64)**; all women; 3/4 multifocal |
| Adrenal | 3/48 | ~6% | — |
| Thymus | 2/48 | ~4% | thymic hyperplasia + myasthenia gravis (1); atypical carcinoid with ectopic Cushing (1) |
| Lung carcinoid | 1 | — | metastatic |
| Renal angiomyolipoma | 2 | — | — |

Organ burden: **1 organ in 27/48 (56%), 2 in 13/48 (27%), 3 in 3/48 (6%), 4 in 5/48 (10%)**. First presenting organ: parathyroid 27/48 (56%), pituitary 11/48 (23%). Verbatim conclusion: *"MEN4 is an extremely rare disease, which most frequently affects women around 50 years of age."*

**C. Chevalier 2024 (29 symptomatic class-4/5 patients after variant reclassification of 77 published patients in 26 studies):** PHPT 25/29 (**86%**, median 47 y, range 29–71); pituitary adenoma 13/29 (**44%**, median 40 y, range 12–67); NET 8/29 (**27%**, median 56 y, range 31–70); adrenal lesions 3/29. First manifestation among 15 probands: PHPT 53% (median 40.5 y), pituitary 33% (median 30 y), NET 13% (median 39 y). *(Variant/phenotype detail from a model-extracted portion of a truncated page — treat these specific numbers as a lead pending full-text check; the abstract-level conclusions were read verbatim.)*

**D. Alrezk 2017 (19 cases, earliest pooled set):** PHPT 15/19 (~80%); pituitary adenoma 7/19 (~37%); duodenopancreatic/gastric NET 7/19. Mean PHPT age **~56 y in MEN4 vs ~25 y in MEN1**.

## 3.2 Per-phenotype detail with HPO terms

All HP IDs below were **retrieved** from EBI OLS4 and/or the HPO/Monarch APIs in this session.

### Primary hyperparathyroidism — the cardinal feature
- **Type:** clinical sign + laboratory abnormality (hypercalcemia, elevated PTH) + neoplasm.
- **HPO:** **HP:0008200** Primary hyperparathyroidism; **HP:0000843** Hyperparathyroidism; **HP:0002897** Parathyroid adenoma; **HP:0008208** Parathyroid hyperplasia; **HP:0003072** Hypercalcemia; **HP:0003165** Elevated circulating parathyroid hormone level; **HP:0006780** Parathyroid carcinoma (Orphanet-sourced frequency HP:0040283 "Occasional").
- **Onset:** adult-predominant; median 51 y (Singeisen), **range extends to 15 y** (Elston kindred, c.378G>C p.E126D — Alrezk Table 1 lists a 15-year-old female with early-onset PHPT, renal calculi, hypercalcemia).
- **Severity/course:** GeneReviews: "often mild, frequently found in asymptomatic people"; progressive but indolent. Multiglandular 14%, recurrence 6% — **both markedly lower than MEN1**.
- **Frequency:** 55–86% depending on dataset.
- **QoL:** nephrolithiasis (**HP:0000787** Kidney stone), nephrocalcinosis (**HP:0000121**), osteopenia/osteoporosis (**HP:0000939**) documented in individual cases (Seabrook 2022 Patient A: osteopenia + asymptomatic renal calculi; Elston kindred: nephrocalcinosis). **No EQ-5D/SF-36/PROMIS data exist for MEN4 — formal QoL instrumentation has never been applied to this disease. This is a hard gap.**

### Anterior pituitary adenoma
- **Type:** neoplasm + endocrine signs.
- **HPO:** **HP:0002893** Pituitary adenoma; **HP:0008291** Pituitary corticotropic cell adenoma (ACTH-producing); **HP:0006767** Pituitary prolactin cell adenoma (prolactinoma); **HP:0011760** Pituitary growth hormone cell adenoma; **HP:0011761** Pituitary null cell adenoma; **HP:0000845** Elevated circulating growth hormone concentration (exact synonym "Growth hormone excess"); **HP:0000870** Increased circulating prolactin concentration; **HP:0003118** Increased circulating cortisol level (exact synonym "Cushing syndrome"); **HP:0012030** Increased urinary cortisol level.
  - Note: HPO has **no good term labelled "acromegaly"** — the closest retrieved hit, HP:0033794 "Acral overgrowth," carries "acromegaly" only as a *related* synonym. Use HP:0000845. **Flagging this as a lump/split call for the KB.**
- **Onset:** median 39 y (Singeisen), **range 5–79 y** — i.e., **pediatric onset is within the reported range**.
- **Subtype distribution:** ACTH most common (GeneReviews: 33% of pituitary tumors; Singeisen: 7/16 secreting), then prolactin, then GH, then nonfunctioning. Predominantly **microadenomas**.
- **Frequency:** 30–45%; first presentation in ~23%.
- **Pediatric specificity (substantive):** Chasseloup 2020 found CDKN1B variants in **2.6%** of a predominantly pediatric Cushing disease cohort; the five carriers had **mean age at CD onset 10.5 ± 1.3 y**, and in that series CD was the *only* MEN4 feature. Alrezk Table 1 includes a **6-year-old female with gigantism from a somatotropinoma** carrying the 5′UTR variant c.-29_-26delAGAG. **MEN4 in childhood is, on current evidence, predominantly a pituitary disease — not a parathyroid one.** That is a different entity in practice from adult MEN4.

### Gastroenteropancreatic and thoracic NETs
- **HPO:** **HP:0100634** Neuroendocrine neoplasm; **HP:0030405** Pancreatic endocrine tumor; **HP:0002044** Zollinger-Ellison syndrome; **HP:0034953** Duodenal gastrinoma (no generic "Gastrinoma" term was returned by OLS — **split call to surface**); **HP:0100570** Carcinoid tumor; **HP:0030445** Pulmonary carcinoid tumor; **HP:0012197** Insulinoma; **HP:0100522** Thymoma (Orphanet frequency "Very rare"); **HP:0012091** Abnormality of pancreas physiology; **HP:0008283** Fasting hyperinsulinemia; **HP:0002014** Diarrhea; **HP:0002574** Episodic abdominal pain; **HP:0100633** Esophagitis.
- **Onset:** latest of the three core lesions. GeneReviews: **youngest reported pancreatic NET at age 42**. Chevalier: median 56 y (31–70).
- **Severity:** GeneReviews, citing Singeisen 2023: **about half are metastatic at diagnosis** — Singeisen's own text gives 4/9. Less likely to be multifocal than in MEN1.
- **Frequency:** 14–27%. Explicitly **lower and later than MEN1** — Frederiksen 2019 conclusion, verbatim: *"Gastrointestinal neuroendocrine tumors appear to be less prevalent in MEN4 than in MEN1."*
- An **insulinoma** has been reported as a rare MEN4 manifestation (J Endocr Soc 2024 conference abstract, PMC11454903 — *conference abstract, lowest evidence tier; lead only*).

### Adrenocortical lesions
- **HPO:** **HP:0008256** Adrenocortical adenoma.
- Frequency 4–7% (GeneReviews); cortisol-secreting or nonfunctioning. Seabrook 2022 Patient A had bilateral adrenal lesions (left 59×49 mm, right 26×21 mm) with a 53 mm cortical adenoma resected at ~47 y.

### Thyroid
- **HPO:** **HP:0002895** Papillary thyroid carcinoma; **HP:0002865** Medullary thyroid carcinoma; **HP:0000821** Hypothyroidism; **HP:0000872** Hashimoto thyroiditis.
- **PTC in 8%** (4/48, all women, median 57.5 y, 3/4 multifocal — Singeisen). GeneReviews calls this a possible **"emerging association"** — not established. *Evidence class: pooled case series, no case-control.*
- **MTC:** a single 2025 case report (59-year-old woman, MTC without pathogenic RET, heterozygous **c.536del**, protein change reported secondarily as p.Pro179GlnfsTer46, with weak nuclear p27 in pituitary and thyroid tumors and a somatic HRAS variant; Fam Cancer 2025, DOI 10.1007/s10689-025-00449-9; PMID 40009226, Mercè F et al.). **One case. RET must be excluded before attributing MTC to CDKN1B. Label as a lead, not an established association.**

### Non-endocrine and uncertain associations
- **HPO:** **HP:0002858** Meningioma; **HP:0006772** Renal angiomyolipoma; **HP:0030079** Cervix cancer (Orphanet "Occasional"); **HP:0010615** Angiofibromas; **HP:0007449** Confetti-like hypopigmented macules; **HP:0012334** Extrahepatic cholestasis; **HP:0030731** Carcinoma; **HP:0000818** Abnormality of the endocrine system.
- GeneReviews lists breast, colon, testicular, prostate, cervical neuroendocrine carcinoma, meningioma, and renal angiomyolipoma as reported, **with the explicit caveat that further research is needed**. Cutaneous MEN1-type tumors have *not* been reported in MEN4.
- **Pediatric CNS tumor:** Desrosiers-Battu et al. reported **anaplastic meningioma (WHO grade 3) in a 6-year-old boy** carrying a maternally transmitted germline CDKN1B pathogenic frameshift, with a somatic **YAP1::MAML2** fusion and **no somatic loss of the wild-type allele**; the authors state the role of the germline variant without a second hit is unclear (Cancer Genet 2025;292–293:106–110, PMID 39985924, DOI 10.1016/j.cancergen.2025.01.009). *Single case; causal attribution uncertain by the authors' own statement.*
- **Autoimmunity:** a possible link was raised (Chevalier 2020, PMID 32386678, per GeneReviews citation). Not independently verified here.

### Inheritance / penetrance HPO modifiers
- **HP:0000006** Autosomal dominant inheritance (annotated to OMIM:610755 in the HPO network API).
- **HP:0003829** "Typified by incomplete penetrance" (exact synonym "Incomplete penetrance").

**Important provenance note on HPO annotations:** The official HPO annotation set for OMIM:610755 retrieved from `ontology.jax.org/api/network/annotation/OMIM:610755` is **thin and partly derived from a single publication** — several terms carry frequency "1/1" sourced to **PMID 24819502** (Tonelli 2014). Monarch's MONDO:0012552 record lists **44 HP IDs** with a reported "Disease to Phenotype" association count of **50** (the 44 vs 50 discrepancy is unexplained by the API). Most richer frequency qualifiers ("Very frequent," "Frequent," "Occasional," "Very rare") are **Orphanet-sourced, not literature-recomputed**. **The HPO frequency layer for MEN4 should not be treated as equivalent to the Singeisen/Halperin cohort frequencies above.**

---

# 4. Genetic / Molecular Information

## Causal gene

**CDKN1B** — HGNC:1785; approved name *cyclin dependent kinase inhibitor 1B*; locus **12p13.1**; NCBI Gene 1027; Ensembl ENSG00000111276; MANE Select **NM_004064.5 / ENST00000228872.9**; CCDS8653; UniProt **P46527**; OMIM 600778; aliases **KIP1, P27KIP1**; previous name "cyclin-dependent kinase inhibitor 1B (p27, Kip1)"; gene group "Cyclin dependent kinase inhibitor 1 family"; mouse ortholog MGI:104565, rat RGD:69062; COSMIC gene CDKN1B. (Retrieved from https://rest.genenames.org/fetch/symbol/CDKN1B — *structured database*.)

Protein: **198 aa**, ~22,073 Da (UniProt P46527).

## Pathogenic variants

**Detection rates (GeneReviews Table 1):** sequence analysis detects **~95%** of probands with a pathogenic variant (derived from HGMD, Stenson 2020, PMID 32596782); gene-targeted deletion/duplication analysis has identified **2 individuals** (Grey 2013 + the chapter authors' unpublished data).

**Variant-type distribution across 65 individuals (Singeisen 2023):** missense **29/65 (45%)**, frameshift **22/65 (34%)**, nonsense **8/65 (12%)**, small deletions **6/65 (9%)**, unspecified 1/65. Among the 48 symptomatic: missense 21/48 (44%), frameshift 17/48 (35%). **28 different variants** across the symptomatic set.

### Representative variant table (compiled from retrieved primary/review tables)

Reference transcript: **NM_004064** (Singeisen/Seabrook cite NM_004064.4/.5; NG_016341.1).

| cDNA | Protein | Class | Phenotype reported | Source |
|---|---|---|---|---|
| c.227G>A | p.Trp76Ter (W76\*) | nonsense | PHPT, acromegaly, renal angiomyolipoma | Pellegata 2006, PMID 17030811 |
| c.59_77dup19 | p.Lys25fs | duplication/fs | PHPT, ACTH adenoma/Cushing, small-cell NE cervical carcinoma | Georgitsi 2007 (via Frederiksen Table 3 / Alrezk Table 1) |
| c.25G>A | p.Gly9Arg | missense | PHPT | Costa-Guda (via Frederiksen Table 3) |
| c.163G>A | p.Ala55Thr | missense | PHPT, Zollinger-Ellison/gastrinoma with hepatic mets | Belar (via Frederiksen Table 3) |
| c.195G>T | p.Gln65His | missense | colon cancer family (MEN4 attribution uncertain) | Esteban-Jurado (via Frederiksen Table 3) |
| c.206C>T (also printed c.678C>T) | p.Pro69Leu | missense | PHPT, bronchial carcinoid, nonfunctioning pituitary microadenoma, papillary thyroid carcinoma | Molatore 2010; UniProt natural variant rs777354267 |
| c.281C>T | p.Pro94Leu | missense | PHPT, papillary thyroid carcinoma | via Singeisen Table 2 |
| c.280C>T | p.Pro94Ser | missense (VUS) | Cushing disease in father and daughter | Gambino 2026, PMID 42093859 |
| c.283C>T | p.Pro95Ser | missense | PHPT, Zollinger-Ellison | Agarwal (via Frederiksen Table 3) |
| c.285del / c.285dupC | p.Gly97Valfs\*22 / p.Lys96Glnfs\*29 | frameshift | nonfunctioning pNET at 42, parathyroid adenoma at 50 / PHPT | Chevalier 2024; Singeisen Table 2 |
| c.286A>C | p.Lys96Gln (also printed P96Q) | missense | GH adenoma / prolactin excess, breast cancer at 41 | Tichomirowa (via Frederiksen / Alrezk) |
| — | p.Lys96Glnfs\*29 | frameshift | MEN-like phenotype; structural modelling | Papadopoulou-Marketou 2026, PMID 42993098 |
| c.320del(A) | p.Gln107Argfs\*12 | frameshift | PHPT (parathyroid adenoma, 63 y); separately pediatric Cushing disease | Chevalier 2024; Chasseloup 2020 |
| c.313G>T | p.Glu105Ter | nonsense | 3 localized nonfunctional duodenal G1 NETs at 68 | Chevalier 2024 |
| c.201_202del | p.His67Glnfs\*57 | frameshift | PHPT from ~30 y; suspected acromegaly, normal MRI | Chevalier 2024 |
| c.349C>T | p.Pro117Ser | missense | MEN1-like features + papillary thyroid cancer (54 y) | Singeisen 2023 index case |
| c.356T>C | p.Ile119Thr | missense | AIP-negative FIPA, GH adenoma; also pediatric CD | Tichomirowa; Chasseloup 2020 (rs142833529, MAF 0.0545%) |
| c.374_375delCT | p.Ser125Ter | fs/nonsense | PHPT, gastrinoma/ZES, duodenal NE neoplasia, Hashimoto thyroiditis; also nonfunctioning pituitary microadenoma + atypical thymic carcinoid with ectopic Cushing | Tonelli 2014 (PMID 24819502); Pardi 2015 (PMID 25416039); Seabrook 2022 Family C |
| c.376G>C | p.Glu126Gln | missense (VUS) | pediatric Cushing disease; not in gnomAD | Chasseloup 2020 |
| c.378G>C | p.Glu126Asp | missense | PHPT from 15 y, nephrocalcinosis, renal calculi | Elston (via Frederiksen Table 3) |
| c.397C>A | p.Pro133Thr | missense | PHPT, papillary thyroid carcinoma, meningioma | Costa-Guda / Bugalho (via Frederiksen Table 3) |
| c.407A>G | p.Asp136Gly | missense | pediatric Cushing disease (MAF 0.0075%) | Chasseloup 2020 |
| c.410del | — | frameshift | GH/PRL co-secreting macroadenoma + PHPT at 54 | Green 2025, PMID 40443455 |
| c.475G>A | p.Asp159Asn | missense at last codon of exon 1; predicted splice-donor loss | PHPT at 26 (single adenoma) | Seabrook 2022 Family B (novel; LP: PVS1, PM2; SIFT 0.005, CADD 29.1) |
| c.179G>A | p.Trp60Ter | nonsense, predicted NMD | multiglandular PHPT, microprolactinoma, multifocal nonfunctioning duodenopancreatic NET, adrenocortical adenoma | Seabrook 2022 Family A (novel; LP: PVS1, PM2; CADD 38) |
| c.482C>G | p.Ser161Cys | missense | NET | via Singeisen Table 2 |
| c.536del | p.Pro179GlnfsTer46 (secondary source) | frameshift | medullary thyroid carcinoma, RET-negative | Mercè 2025, PMID 40009226 |
| c.595T>C | p.Ter199Gln (\*199Qext60) | stop-loss | PHPT (incl. monozygotic twins) | Agarwal (via Frederiksen / Alrezk) |
| c.121_122delTT | p.Leu41Asnfs\*83 | frameshift | Danish kindred: PHPT in 13/13 carriers, 4 pituitary adenomas, 1 metastatic NET | Frederiksen 2019, PMID 30990521 |
| **c.-456_-453delCCTT** | 5′UTR uORF | non-coding | acromegaly/somatotropinoma + nonfunctioning pancreatic NET (62 y F) | Occhi 2013, PMID 23555276 |
| **c.-32_-29delGAGA** / **c.-29_-26delAGAG** | 5′UTR | non-coding | gastric NET + PHPT; gigantism/somatotropinoma at 6 y; pediatric CD | Malanga (via Frederiksen); Alrezk Table 1; Chasseloup 2020 (rs774454456) |
| c.-7G>C ("ATG-7G>C") | 5′UTR | non-coding | PHPT, bilateral nonfunctional adrenal masses, uterine fibroids | Agarwal (via Frederiksen / Alrezk) |
| c.-80C>T | 5′UTR | non-coding | PHPT | via Alrezk Table 1 |

**⚠ Nomenclature caution, flagged as a defect in the literature, not resolved here:** the cDNA coordinates for the same variants are **inconsistent across publications**. p.W76\* is printed as **c.692G>A** in Alrezk 2017 Table 1 but **c.227G>A** in Singeisen 2023 Table 2. p.P69L appears as both **c.678C>T** and **c.206C>T**. Several 5′UTR deletions are printed with transposed coordinates (c.-32_-29delGAGA vs c.-29_-26delAGAG; Occhi's own Figure 6 legend misprints c.-456_-459). **Any KB ingestion must normalize to NM_004064.5 and re-derive HGVS from genomic coordinates; do not trust the published cDNA strings.**

### Variant classification
- GeneReviews treats "pathogenic" and "likely pathogenic" as synonymous per ACMG/AMP (Richards 2015, PMID 25741868); a heterozygous **VUS neither establishes nor excludes** the diagnosis.
- **A large fraction of published MEN4 "cases" rest on variants currently classified VUS** — GeneReviews says so explicitly, and Chevalier 2024 demonstrated it quantitatively: of ~50 class 3/4/5 variants in 5,600 patients, only **4 survived reclassification as class 4/5**, and of 77 published patients only **29** remained after excluding asymptomatic carriers and reclassifying. **This is the single most important caveat for the KB: the published MEN4 phenotype is inflated by VUS-driven case reports.**
- ClinVar (via E-utilities esearch, retrieved): **1,210 total CDKN1B records**. A P/LP-filtered query returned **count 275**, but the query translation matched the phrases under `[All Fields]`, not `[clinical significance]` — **so 275 is not a valid P/LP count and should not be cited as one.**

### Allele frequency
- UniProt natural variants retrieved: **p.Arg15Trp (rs2066828)** and **p.Val109Gly (rs2066827)** — common polymorphisms with no disease association listed; **p.Pro69Leu (rs777354267)** annotated verbatim as *"found in a patient with multiple endocrine tumors; germline mutation; reduced expression levels; shows impaired binding to CDK2."*
- Specific MAFs retrieved from Chasseloup 2020: p.Ile119Thr rs142833529 MAF **0.0545%**; p.Asp136Gly MAF **0.0075%**; p.Glu126Gln **absent from gnomAD**. Occhi's c.-456_-453delCCTT was absent from 600 control chromosomes, dbSNP, and 1000 Genomes.
- **Population carrier frequency for pathogenic CDKN1B variants has not been estimated in any retrieved source. Gap.**

### Somatic vs germline — *keep separate (lump/split call)*
MEN4 is defined by the **germline** variant. **Somatic** CDKN1B alterations occur in sporadic tumors that are *not* MEN4:
- **Small-intestine NETs:** Francis et al., Nature Genetics 2013;45:1483–6 (PMID 24185511) — WES/WGS of 55 SI-NETs; **recurrent heterozygous inactivating frameshift CDKN1B indels in 14/180 SI-NETs (~8%)**, plus **hemizygous deletions spanning CDKN1B in 7/50**. A follow-up (Ann Surg Oncol, Springer 10.1245/s10434-014-4351-9) found p27 protein expression did **not** correlate with mutation status and framed CDKN1B as a **potential haploinsufficient tumor suppressor**.
- **Luminal breast cancer:** CDKN1B alterations enriched in premenopausal luminal breast cancer at ~4% (search-level retrieval; *lead, primary source not opened*).
- GeneReviews states plainly that sporadic tumors (breast, prostate, NETs, others) occurring without other MEN4 findings often carry a **somatic** CDKN1B variant absent from the germline, and **these are not heritable.**

### Functional consequences
**Loss of function / reduced p27 dosage** is the unifying mechanism. Demonstrated routes:
1. **Nonsense/frameshift → NMD or truncated unstable protein** (Seabrook 2022 p.Trp60Ter predicted NMD; Pellegata 2006 rat mutant p27 "barely detectable").
2. **Missense → accelerated degradation, mislocalization, impaired partner binding.** Chasseloup 2020, verbatim abstract: *"In vitro assays demonstrated protein instability and disruption of the scatter domain of CDKN1B for all variants tested."* Localization in AtT20 cells: WT, p.I119T and p.D136G exclusively nuclear; p.E126Q nuclear-predominant with moderate cytoplasmic staining; **p.Q107Rfs\*12 purely cytoplasmic**; p.Q107Rfs\*12 had the shortest half-life (cycloheximide chase). *(Localization/half-life/binding percentages came from a model-extracted portion of a truncated page — lead-grade, verify against the full text.)*
3. **5′UTR uORF variants → reduced translational reinitiation** (Occhi 2013 — see §6).
4. **Reduced binding to CDK complexes:** Bencivenga 2025 (Cells, PMID 39936980, PMC11817124) reports that four MEN4/cancer-derived CDKN1B mutants increased breast cancer cell growth and motility with altered phosphorylation, localization or degradation and weaker cyclin/CDK binding. **Abstract only — full text blocked by reCAPTCHA in this session.**
5. **Possible gain of non-canonical cytoplasmic function.** Mislocalized cytoplasmic p27 promotes migration via RhoA (§6). Whether MEN4 missense variants act purely as LoF or partly as cytoplasmic GoF is **unresolved** — I am flagging this as model-level reasoning beyond what any retrieved MEN4 paper demonstrates.

## Modifier genes
**None identified.** Candidate somatic cooperating events reported in individual MEN4 tumors: **ATRX c.6406G>A (p.Asp2136Asn)** in a parathyroid adenoma and **MEN1 c.974C>T (p.Pro325Leu)** in a thymic carcinoid (Seabrook 2022); **USP8 p.P720R** somatic in a CDKN1B-carrier corticotropinoma (Chasseloup 2020); somatic **HRAS** in the MTC case (Mercè 2025); somatic **YAP1::MAML2** in the pediatric meningioma (Desrosiers-Battu 2025). *These are n=1 observations, not modifiers.*

## Epigenetic information
GeneReviews raises epigenetic silencing of the wild-type allele as one of two candidate mechanisms (vs haploinsufficiency) to explain the absent second hit, and states this **"needs further research."** **No ENCODE/Roadmap/DiseaseMeth data specific to MEN4 were retrieved. Genuine gap.**

## Chromosomal abnormalities
- Whole-gene/exon deletions at 12p13.1 are rare but real: GeneReviews reports **2 individuals** detected by deletion/duplication analysis.
- **Allelic but distinct entity (split call):** Grey et al. 2013 (Hum Mutat, PMID 23505216) described a child with **overgrowth, macrocephaly, strabismus, and neurodevelopmental delay** caused by **biallelic** reduction of CDKN1B expression — a maternally inherited contiguous 12p13.1 deletion plus a *de novo* promoter variant on the paternal allele — proposing an **autosomal recessive** mechanism. **This is not MEN4 and should be curated as a separate disease entity.**

---

# 5. Environmental Information

- **Environmental factors:** none established. No toxin, radiation, pollutant, or occupational exposure has been associated with MEN4 in any retrieved source.
- **Lifestyle factors:** none established. No smoking, diet, exercise, or alcohol association retrieved.
- **Infectious agents:** not applicable. No pathogen is implicated.

For a monogenic, fully penetrant-at-the-genotype-level tumor predisposition of this rarity, the absence of environmental literature reflects both biology and the near-total absence of epidemiological study. **I found no negative studies either — this is an untested area, not a tested-and-negative one.**

---

# 6. Mechanism / Pathophysiology

## 6.1 Ordered causal chain

**Trunk (parathyroid/pituitary/NET arm):**

1. A **germline heterozygous loss-of-function variant in CDKN1B** (12p13.1) is inherited or arises *de novo*, and is present in every cell. *(Demonstrated — Pellegata 2006, PMID 17030811.)*
2. That variant **reduces the functional dose of p27^Kip1 protein**, by one of four demonstrated routes: nonsense/frameshift transcript degradation or protein truncation; missense-driven accelerated proteasomal turnover; 5′UTR uORF disruption that lowers translational reinitiation at the CDKN1B AUG; or missense-driven mislocalization out of the nucleus. *(Demonstrated — Occhi 2013 PMID 23555276; Chasseloup 2020 PMID 32232325.)*
3. Reduced nuclear p27 **weakens inhibition of cyclin E–CDK2 and cyclin A–CDK2 complexes**. UniProt P46527 records p27 as *"a potent inhibitor of cyclin E– and cyclin A–CDK2"* and as *"important regulator of cell cycle progression"*; residues **51–91** mediate CDK2 interaction, and a peptide of **AA 28–79** retains substantial cyclin A/CDK2 inhibitory activity. *(Demonstrated at the protein level; inferred for MEN4 tumors specifically.)*
4. Loss of CDK2 restraint **leads to** unopposed RB phosphorylation and **release of the G1→S restriction point** (GO:0000082, G1/S transition of mitotic cell cycle). *(Inferred for MEN4 tissue — this step is canonical p27 biology but has not been directly measured in human MEN4 tumors in any source I retrieved.)*
5. Released proliferative drive in **hormone-producing endocrine progenitor/secretory cells** results in clonal expansion — **branching by cell lineage** (see 6.2).
6. Clonal expansion in a given lineage **results in** a monoclonal adenoma, which, because the parent cell is a hormone-secreting endocrine cell, **leads to** autonomous hormone output: PTH (hypercalcemia), ACTH (Cushing disease), GH (acromegaly/gigantism), prolactin, gastrin (ZES), or no hormone (nonfunctioning).
7. Autonomous hormone excess **causes** the end-organ phenotypes: hypercalcemia → nephrolithiasis, nephrocalcinosis, bone loss; hypercortisolism → Cushing phenotype, hypertension, diabetes; GH excess → acromegaly, or gigantism if before epiphyseal fusion.

**Critical branch at step 5 — the "missing second hit":**

5a. In **a minority** of tumors, a somatic second hit inactivates the wild-type allele. Frederiksen 2019 found **LOH in 2 of 5 tumors**, both parathyroid adenomas. Seabrook 2022 found loss of p27 immunostaining in a parathyroid adenoma, read as an acquired second hit.

5b. In **most** tumors, **no second hit is found**. Occhi 2013: no loss of the wild-type allele; both alleles transcribed in the pancreatic lesion. Seabrook 2022: same variant in all sampled tumors, no LOH, no second hit. Desrosiers-Battu 2025: explicitly no somatic loss of the other allele. GeneReviews states: many MEN4 tumors show **no LOH or acquired second hit**, and whether the operative mechanism is **haploinsufficiency** or epigenetic silencing of the wild-type allele is unresolved.

➜ **The branch that applies to most MEN4 tumors is therefore haploinsufficiency — a dosage mechanism, not classical two-hit tumor suppression. This is the single most mechanistically distinctive feature of MEN4 relative to MEN1 and should be recorded as such.** Independent support for CDKN1B haploinsufficiency comes from the somatic SI-NET literature: p27 protein expression did not correlate with CDKN1B mutation status (Ann Surg Oncol follow-up to Francis 2013).

**Secondary branch — cytoplasmic/non-canonical p27 (migration/invasion):**

8. Variants that **mislocalize p27 to the cytoplasm** (e.g. p.Q107Rfs\*12, purely cytoplasmic — Chasseloup 2020) or disrupt the **"scatter domain"** remove p27's normal restraint on **RhoA**.
9. Besson et al. (Genes Dev 2004;18:862) demonstrated **higher Rho–GTP in p27^−/− cells than wild type**, with Rac and Cdc42 unaffected; p27 binds Rho irrespective of its GTP/GDP state and **interferes with Rho binding to its GEFs but not its effectors**; unlike p21, p27 **does not directly inhibit ROCK**, and ROCK inhibition rescues the migration defect of p27-null cells — placing p27 **upstream of ROCK**.
10. Loss of that restraint **results in** increased RhoA–ROCK signalling and increased motility/invasiveness. The scatter domain was mapped by the Dowdy lab to the **C-terminal region between residues 118 and 158** (truncation mutants at 158 and 118), requires **cytoplasmic localization via Ser-10 phosphorylation**, and operates **independently of cell-cycle arrest**. *(Conflicting mapping: an NMR study localized direct RhoA binding to residues 55–95 and found the affinity low, with a later report proposing an unidentified factor associating with the p27 C-terminus to enhance the RhoA interaction. **Unsettled — report both.**)*
11. Chasseloup 2020 reported reduced RHOA binding for all four tested CDKN1B variants (by ~70%, 30%, 70%, 60%) alongside altered CDK2 binding — *model-extracted from a truncated page; lead-grade*.

➜ This branch is a candidate explanation for why some MEN4 NETs are **metastatic at presentation (~4/9, Singeisen)** despite an otherwise indolent syndrome. **I am labeling that linkage as model inference — no retrieved source makes it.**

**Pituitary-specific branch (step 5, corticotroph):**

5c. In corticotrophs, reduced p27 **leads to** corticotroph expansion and ACTH excess. Chasseloup 2020 found p.Q107Rfs\*12 raised POMC expression (**1.62 vs 1.08 for WT, P = .0451**) while missense variants did not alter POMC or ACTH — i.e. a **frameshift-specific** effect on the corticotroph program. Corticotropinoma IHC in three carriers showed only partial p27 retention (moderate–strong nuclear staining in ~30%, ~20%, and ~55% of cells). *(IHC and POMC percentages: model-extracted from truncated text — lead-grade.)*

## 6.2 Cell-type branching at step 5 (with CL terms)

| Lineage | Cell Ontology | Resulting lesion |
|---|---|---|
| Parathyroid chief cell | **CL:0000446** (chief cell of parathyroid gland) | parathyroid adenoma → PHPT |
| Corticotroph | **CL:0002309** | ACTH adenoma → Cushing disease |
| Somatotroph | **CL:0002312** | GH adenoma → acromegaly / pediatric gigantism |
| Lactotroph / mammotroph | **CL:0002311** | prolactinoma |
| Gonadotroph | **CL:0000437** (label spelled "gonadtroph" in OLS) | nonfunctioning adenoma (the MENX rat pituitary lineage) |
| Pancreatic endocrine cell | **CL:0008024** | pNET, insulinoma |
| Enteroendocrine cell | **CL:0000164** | gastrinoma, duodenal/gastric/ileal NET |
| Parafollicular (C) cell | **CL:0000570** | MTC (rat model; single human case) |
| Adrenal cortical cell | **CL:0002097** (cortical cell of adrenal gland) | adrenocortical adenoma |
| Chromaffin cell | **CL:0000166** | pheochromocytoma — **rat only; not a human MEN4 feature** |

## 6.3 Molecular pathways, processes, protein, and GO terms

**Pathways:** G1/S cell-cycle control (cyclin E/A–CDK2, cyclin D–CDK4), SCF^SKP2 ubiquitin–proteasome degradation, RhoA–ROCK cytoskeletal signalling, cap-dependent translational reinitiation.

**p27 degradation module (demonstrated, general cell biology):** CDK2–cyclin E phosphorylates p27 at **Thr187**, which marks it for SCF^SKP2 recognition and ubiquitination (Curr Biol 1999, ScienceDirect S0960982299802905). In Skp2-knockout cells, p27 accumulates, binds cyclin E, and **nearly abolishes** its kinase activity (Genes Dev 2004;18:2602). A 2023 cryo-EM structure resolved **CDK2–cyclin A–CKS1–p27–SKP1–SKP2 at 3.4 Å** (Sci Rep, https://www.nature.com/articles/s41598-023-37609-9; PMC10318019).

**Protein architecture (UniProt P46527, verbatim features):**
- Chain 1–198; disordered regions **1–34** and **85–198** (p27 is an intrinsically disordered protein).
- Region **51–91**: "Interaction with CDK2."
- Motif **153–169**: "Nuclear localization signal."
- Domain comment: AA **28–79** retains substantial cyclin A/CDK2 inhibitory activity.
- **UniProt contains no feature named "scatter domain"** — the 118–158 scatter domain is a literature construct (Dowdy lab), not a UniProt annotation. *Flagging this so the KB does not attribute it to UniProt.*
- Phosphosites: **Ser10** (UHMK1), **Tyr74** (SRC), **Tyr88** (ABL, LYN, SRC, JAK2), **Tyr89**, **Thr157** (CaMK1, AKT1, PIM1), **Thr170**, **Thr187** (AKT1, CDK1, CDK2), **Thr198** (CaMK1, AKT1, RPS6KA1, RPS6KA3, PIM1).
- Subcellular location: **nucleus, cytoplasm, endosome** (endosome by similarity); nuclear and cytoplasmic in quiescent cells.
- Interactors (CC INTERACTION, experiment counts): **CDK2 (32), CCNA2 (21), CCNE1 (12)**, CDK4, CDK1, **SKP2 (4)**, CDK5; SUBUNIT text: *"Identified in a complex with SKP1, SKP2 and CKS1B"* and *"Interacts with GRB2."*

**Suggested GO terms (all retrieved from OLS4):**
- **GO:0000082** G1/S transition of mitotic cell cycle
- **GO:0008285** negative regulation of cell population proliferation
- **GO:0004860** protein kinase inhibitor activity
- **GO:0000307** cyclin-dependent protein kinase holoenzyme complex
- **GO:0006446** regulation of translational initiation (for the uORF mechanism)
- **GO:0005634** nucleus (CC); **GO:0005737** cytoplasm (CC)
- *Not retrieved:* "negative regulation of cyclin-dependent protein serine/threonine kinase activity" returned zero OLS hits, and "cell cycle arrest" returned only GO:0051726 (regulation of cell cycle), where it is a narrow synonym. **Do not cite GO IDs for these two concepts without re-checking.**

## 6.4 The uORF mechanism in detail (Occhi 2013, PMID 23555276 / PMC3605397)

A distinct, demonstrated non-coding route to reduced p27:

1. **c.-456_-453delCCTT** removes 4 bp from a highly conserved regulatory upstream ORF in the CDKN1B 5′UTR.
2. The deletion **shifts the uORF stop codon**, lengthening the uORF peptide from **29 to 158 amino acids** and shrinking the intercistronic space from **429 bp to 38 bp**.
3. A long uORF plus a short intercistronic space **prevents 40S subunits from re-acquiring reinitiation cofactors** before reaching the downstream CDKN1B AUG.
4. This **reduces translational reinitiation**, lowering p27 protein without reducing mRNA: wild-type and mutant alleles were expressed in *"almost equal amounts"* in blood, with a single promoter used; the authors concluded transcription and mRNA stability are unaffected.
5. Evidence: dual-luciferase assays in GH3 and HeLa (lovastatin-synchronized and asynchronous) showed **significantly reduced** activity (**p<0.01**) in a cell-cycle-independent manner, while the silent uORF change **c.-469C>T** did not; luciferase mRNA qRT-PCR attributed the effect to translation rate; western blot in HEK293 showed **significant reduction in p27^KIP1 protein**; a rescue mutant **c.-428A>T** restoring the stop codon **almost completely recovered** uORF regulatory activity; and **c.-74insC**, creating an in-frame uORF–CDKN1B fusion, produced a detectable chimeric product — described as the **first direct evidence of uORF translation in a cellular system**.
6. Patient: 62-year-old woman with acromegaly and a well-differentiated nonfunctioning pancreatic endocrine neoplasm (Ki-67 ~1%). Tumor IHC: **weak cytoplasmic and low nuclear p27**, with strong nuclear staining in endothelial internal controls. **No LOH; both alleles transcribed** — the authors suggest **p27 haploinsufficiency**.

## 6.5 Categories with no MEN4-specific data

- **Metabolic changes:** no MEN4-specific metabolomic or metabolic-pathway data retrieved. Secondary metabolic consequences (hypercalcemia, cortisol-driven diabetes) are hormone-mediated, not primary.
- **Immune system involvement:** only anecdotal — thymic hyperplasia with **myasthenia gravis** in one Singeisen case, multiple sclerosis in one Alrezk case, Hashimoto thyroiditis (HP:0000872) in the Tonelli kindred, and a raised but unverified autoimmune association (Chevalier 2020, PMID 32386678). **No mechanism proposed. Insufficient evidence.**
- **Tissue damage mechanisms:** not applicable in the oxidative-stress/ischemia/fibrosis sense; tissue injury is downstream of hormone excess (nephrocalcinosis, bone resorption).
- **Transcriptomics / proteomics / metabolomics / lipidomics / single-cell / spatial / multi-omics / CRISPR screens in human MEN4:** **none retrieved.** The only comparative transcriptomic work found is in the rat: *"Pheochromocytoma in rats with multiple endocrine neoplasia (MENX) shares gene expression patterns with human pheochromocytoma."* **This is a genuine and complete gap for human MEN4.**

---

# 7. Anatomical Structures Affected

## Organ level

**Primary (core spectrum):**
- **Parathyroid gland** — **UBERON:0001132** (most frequent, 55–86%)
- **Anterior pituitary / adenohypophysis** — **UBERON:0002196**; pituitary gland **UBERON:0000007** (30–45%)
- **Pancreas** (endocrine) — **UBERON:0001264** (GEP-NET)
- **Duodenum** — **UBERON:0002114** (gastrinoma, duodenal NET)

**Secondary / less frequent:**
- **Adrenal gland UBERON:0002369**, **adrenal cortex UBERON:0001235** (4–7%)
- **Thyroid gland UBERON:0002046** (PTC ~8%; MTC single case)
- **Thymus UBERON:0002370** (atypical carcinoid, hyperplasia)
- **Lung UBERON:0002048** (bronchial/pulmonary carcinoid)
- **Stomach UBERON:0000945**, **ileum UBERON:0002116** (NETs)
- **Kidney UBERON:0002113** (angiomyolipoma; also end-organ: nephrolithiasis, nephrocalcinosis)
- **Meninx UBERON:0002360** (meningioma — rare; one pediatric anaplastic case)
- **Bone** — end-organ target of PTH excess (osteopenia/osteoporosis). *UBERON ID for generic "bone" was **not cleanly retrieved** — the OLS top hit was UBERON:0004251 "hindlimb zeugopod bone," which is wrong. Do not use that ID.*

**Body systems:** **endocrine** (primary); **urinary/renal**, **skeletal**, **gastrointestinal**, and **cardiovascular** (hypertension in Cushing) as secondary; **nervous/meningeal** rarely.

## Tissue and cell level

Tissue type: **endocrine epithelium / neuroendocrine tissue** throughout. Cell populations are listed with CL terms in §6.2.

## Subcellular level

- **Nucleus — GO:0005634**: the compartment of canonical p27 CDK-inhibitory action; loss of nuclear p27 staining is the IHC correlate of MEN4 tumors (Occhi 2013; Seabrook 2022; Mercè 2025).
- **Cytoplasm — GO:0005737**: compartment of mislocalized p27 and of the RhoA-dependent pro-migratory function; p.Q107Rfs\*12 is purely cytoplasmic (Chasseloup 2020).
- **Cyclin-dependent protein kinase holoenzyme complex — GO:0000307**: the physical target of p27 inhibition.
- Endosome is annotated in UniProt by similarity only.

## Localization and lateralization

- Parathyroid disease in MEN4 is **predominantly uniglandular (86%)** — i.e. typically a **single, unilateral** adenoma — in explicit contrast to MEN1's multiglandular disease; multiglandular 14%, recurrence 6% (Singeisen 2023, GeneReviews).
- Pituitary lesions are typically **solitary microadenomas**.
- GEP-NETs are **less likely to be multifocal than in MEN1** (GeneReviews), though multifocality does occur (Seabrook 2022 Family A: three well-differentiated pancreatic NETs of 2, 4, and 11 mm, Ki67 <1%, with later recurrence).
- Adrenal involvement can be **bilateral** (Seabrook 2022 Family A; Alrezk case 3 "bilateral nonfunctional adrenal masses").
- In the **rat model only**, lesions are characteristically bilateral and symmetric (bilateral pheochromocytoma, bilateral C-cell neoplasia, bilateral parathyroid hyperplasia).

---

# 8. Temporal Development

## Onset

- **Typical age at first endocrine tumor: 43.5 years** (GeneReviews, citing Singeisen 2023), **range 5–76 years**, versus **31.8 years (range 9–71) in MEN1** (Marini 2018, PMID 30428914). Singeisen's own text gives median 43.5, mean 42.2 ± 20.8.
- **Sex-stratified onset (Singeisen 2023, 65-individual set):** women median **49 y** (range 5–76); men median **34 y** (range 10–70). In the 48-symptomatic abstract set: men median 32.5 (10–68) vs women 49.5 (5–76), **P = 0.25** (not significant).
- **Onset pattern: insidious and chronic.** PHPT is frequently detected in asymptomatic people on biochemical screening.
- **Pediatric onset is real but lineage-restricted.** The youngest reported presentations are **pituitary** (age 5 in Singeisen's range; gigantism at age 6 with the c.-29_-26delAGAG 5′UTR variant per Alrezk Table 1; mean CD onset 10.5 ± 1.3 y in Chasseloup's five carriers) and, in one case, **CNS** (anaplastic meningioma at age 6, Desrosiers-Battu 2025). The youngest PHPT retrieved is **15 years** (p.E126D kindred). The youngest **pancreatic NET** is **42 years** (GeneReviews, citing Singeisen). ➜ **Age-specific organ risk is not uniform: a child with MEN4 is at pituitary risk, essentially not at pancreatic NET risk.** This is the key pediatric framing for the KB.

## Progression

- **Stages:** no MEN4-specific staging system exists. Individual tumors are staged by their own systems (e.g. the Seabrook thymic carcinoid was **pT3pN0M0**). Pancreatic/GEP-NETs by WHO grade (the reported cases are **G1**, Ki-67 <1–1%).
- **Rate:** slow/indolent for parathyroid and pituitary disease. **Faster and more consequential for NETs:** about half metastatic at diagnosis (GeneReviews citing Singeisen; Singeisen's text: 4/9), including the ileal NET, one pNET, two of three gastrinomas, and a metastatic lung carcinoid.
- **Course:** **progressive and chronic/lifelong**, with sequential organ involvement over decades. Majority (56%) have only one organ affected at the time of report — but this is a **snapshot of a cross-sectional literature, not a completed natural history**, so single-organ status may reflect short follow-up rather than true disease limitation. *(This caveat is mine; no retrieved source states it.)*
- **Duration:** lifelong predisposition.

## Patterns

- **Remission:** treatment-induced only. Parathyroidectomy and transsphenoidal surgery achieve durable remission; Alrezk 2017 states that **no reported MEN4 case had recurrence after parathyroid resection** (verbatim-sourced from the review's readable text), and Singeisen found recurrence in only 2/36 (6%). Gambino 2026: a father and daughter with Cushing disease and the p.P94S variant were both treated surgically and are in remission. Seabrook Family C: no recurrence at 2 years after thymic carcinoid resection + 60 Gy in 30 fractions. Seabrook Family B: no PHPT recurrence at 3 years. **No spontaneous remission is reported.**
- **Cyclical/fluctuating features:** Seabrook 2022 Patient A had hypercortisolemia at 43 with repeat testing normal, raising possible **cyclical Cushing** — relevant to screening design.
- **Critical periods:** adolescence through the fifth decade is the window in which the great majority of first manifestations appear, which is the basis for the surveillance start-age debate in §10/§13. For GH-secreting tumors, the pre-epiphyseal-fusion window determines gigantism vs acromegaly.

---

# 9. Inheritance and Population

## Epidemiology

- **Prevalence: <1 per 1,000,000** (Singeisen 2023, attributing the figure to Orphanet). *Note: I could not open the Orphanet record itself to verify the primary estimate — this is a secondary citation.*
- GeneReviews: *"MEN4 is likely both rare and underdiagnosed."*
- **Number of reported individuals:** GeneReviews states, as of 2023, *"To date, 65 individuals have been identified"* with a disease-causing CDKN1B variant (citing Singeisen 2023) — of whom **13 belong to one Danish family** (Frederiksen 2019). Halperin 2023 pooled **74** cases across **41 kindreds** (published + unpublished). Chevalier 2024's abstract references **<100 reported cases since its discovery in 2006**. Alrezk 2017 counted **19**; NCI PDQ (per search snippet) also cites 19 at its update.
- **Incidence:** **no incidence estimate exists.** Not computable from available data.
- **Detection yield as a proxy for population burden:** 0.07% of 5,600 MEN1-suspected French patients (Chevalier 2024); <5% of MEN1-like, MEN1-negative individuals (GeneReviews); 1.5–3.7% (Alrezk 2017); 0% of 410 duodenopancreatic NET patients (Charnay 2026).

## Genetic parameters

- **Inheritance: autosomal dominant** (HP:0000006; MONDO parent MONDO:0000426). GeneReviews: *"Each child of an individual with MEN4 has a 50% chance of inheriting the CDKN1B pathogenic variant."*
- **Penetrance: reduced and age-related.** GeneReviews states this directly: *"Penetrance is reduced and age related."* Published estimates **conflict sharply** and should not be reconciled:

| Source | Estimate | Evidence basis |
|---|---|---|
| **Halperin 2023** (PMID 36256846), n=74 | **PHPT 53.4%, pituitary adenoma 23.2%, NET 16.2% by age 60** | pooled actuarial analysis — *the best available cohort-level estimate* |
| **Chevalier 2024** (PMID 38288531) | PHPT cumulative incidence **0% at 20 y, 22.6% at 40 y (95% CI 11.4–41.6), 63% at 60 y** | French + reclassified literature cohort — *different cohort; do not mix with Halperin's numbers* |
| **Frederiksen 2019** (PMID 30990521) | *"all previous adult CDKN1B mutation carriers had MEN4-related disease, indicating a complete penetrance"* — hypercalcemia from PHPT in **13/13** available carriers in the Danish family | single large kindred — *ascertainment-biased upward* |
| **Singeisen 2023** | **17/65 carriers asymptomatic** (median age 47.5, range 16–76) | systematic review — *directly contradicts complete penetrance* |
| **Chasseloup 2020** | Noted that a published pituitary-disease penetrance of **28.3%** "might not be an accurate calculation," given case scarcity and inconsistent screening | explicit author caveat |

➜ **KB guidance: cite Halperin's 53.4/23.2/16.2% by age 60 as the primary penetrance figures, with the explicit note that single-kindred reports of near-complete penetrance are ascertainment-inflated and that 17/65 reported carriers are asymptomatic.**

- **Genotype-specific penetrance:** indels > point mutations for PHPT (log-rank P=0.029); codons **94–96** confer higher PHPT (P<0.001) and pituitary adenoma (P=0.031) risk. GeneReviews summarizes codons 94–96 as a critical region for protein structure and function; a 2025 overview adds that this effect was **not** seen for duodenopancreatic NET risk (search-level retrieval).
- **Expressivity: highly variable**, including within families. Seabrook 2022 titled their series around exactly this ("three phenotypically heterogenous patients"), with phenotypes ranging from isolated PHPT (Family B) to the full spectrum (Family A). Within the Danish kindred, all 13 carriers had PHPT but only 4 had pituitary adenomas and 1 a metastatic NET.
- **Genetic anticipation: not reported, not expected** (no repeat expansion mechanism).
- **De novo rate:** GeneReviews, verbatim: *"The proportion of MEN4 caused by a de novo pathogenic variant is unknown."* Most probands have an affected parent. Simplex cases warrant parental testing; non-paternity and mosaicism are noted possibilities.
- **Germline mosaicism:** not directly documented in MEN4. GeneReviews applies a general estimate: if the variant is undetectable in either parent's leukocyte DNA, sib recurrence risk is **~1%** because of possible germline mosaicism (citing Rahbari 2016, PMID 26656846). *Source class: extrapolated general estimate, not MEN4-specific data.*
- **Founder effects:** **none identified.** The most recurrent variant is **p.Q107fs (4/41 kindreds, Halperin)**, and the largest single cluster is one Danish family with **c.121_122delTT (p.Leu41Asnfs\*83)** — a family effect, not a demonstrated founder haplotype. A Sardinian kindred has been functionally characterized (Pardi 2015, PMID 25416039) but was not reported as a founder population.
- **Consanguinity:** no role in the dominant syndrome. *Relevant only to the separate biallelic CDKN1B-deficiency entity (Grey 2013), which arose from a deletion plus a de novo promoter variant, not consanguinity.*
- **Carrier frequency:** **not estimated.** Gap.

## Population demographics

- **Sex ratio:** marked female predominance — **72–75% female** (Singeisen); PHPT reported in 80% of affected women vs 58% of affected men (GeneReviews); 17/29 women (Chevalier). Frederiksen's Table 3 of previously reported probands listed 15 female, 2 male, 2 not stated. **Whether this is biological or ascertainment is unresolved.**
- **Ethnic/geographic distribution:** **no population-specific enrichment identified.** Reported cases come from Europe (Italy, Denmark, France, Spain, Portugal, Germany), Australia, the USA, and New Zealand. Orphanet lists the disorder in rare-disease subsets (clingen, gard_rare, nord_rare, ordo_disorder, orphanet_rare, otar, rare). **No geographic clustering of specific variants was retrieved.**
- **Age distribution:** see §8. Adults predominate; the 5–76-year range includes a small but important pediatric tail.
- **Familial vs sporadic (Singeisen 2023):** **24 sporadic** cases vs **24 cases within 11 families** (median 3 affected members per family, range 2–13).

---

# 10. Diagnostics

## Clinical/laboratory tests

**Biochemistry (parathyroid):** albumin-corrected serum calcium, PTH, 25-OH vitamin D, 24-hour urine calcium. GeneReviews recommends serum calcium first, with PTH/vitamin D/24-h urine calcium and surgical referral if abnormal. Illustrative values from Seabrook 2022: corrected Ca 2.92 mmol/L with PTH 12.4 pmol/L (Patient A); peak corrected Ca 3.06 mmol/L with PTH 20 pmol/L (Patient B).

**Biochemistry (pituitary):** IGF-1, prolactin, ACTH, cortisol. For suspected Cushing: **24-hour urine free cortisol, late-night salivary cortisol, and/or 1 mg overnight dexamethasone suppression**, with dynamic GH or cortisol testing if screening is abnormal (GeneReviews Table 4/6). Seabrook Patient C: preoperative 24-h UFC 438 nmol/24 h (ref <150), ACTH 21 pmol/L (ref <14). Seabrook Patient A prolactin 1898 mIU/L.

**Biochemistry (NET):** **serum gastrin** (GeneReviews surveillance table). Chromogranin A was not specified in the retrieved guidance.

**Imaging:**
- **Pituitary MRI** (NCIT:C16809 Magnetic Resonance Imaging) — GeneReviews surveillance.
- **Abdominal contrast CT or MRI** for pancreatic/duodenal lesions; GeneReviews notes **endoscopic ultrasound is more sensitive but more invasive** (citing Jensen 1999, PMID 10436815).
- **⁶⁸Ga-DOTATATE PET** was used to detect multifocal pancreatic NETs in Seabrook 2022 Patient A.
- Parathyroid localization imaging is standard of care but was not specified in the retrieved MEN4 guidance.

**Functional/invasive:** **inferior petrosal sinus sampling** confirmed an ectopic ACTH source in Seabrook Patient C — relevant because MEN4 can produce *both* a pituitary microadenoma and an ectopic ACTH source in the same patient, a diagnostic trap.

**Electrophysiology:** not applicable.

**Histopathology / IHC:**
- **p27 immunohistochemistry** is the key tissue correlate: loss or marked reduction of **nuclear** p27 staining in tumor with retained strong nuclear staining in internal controls (endothelium). Documented in Occhi 2013 (weak cytoplasmic, low nuclear p27 in the pNET, with strong endothelial nuclear control), Seabrook 2022 (loss in a parathyroid adenoma), Chasseloup 2020 (corticotropinomas retaining nuclear staining in only ~20–55% of cells; antibody BD Biosciences 610242, mouse monoclonal, 1:1000), and Mercè 2025 (weak nuclear p27 in pituitary and thyroid tumors). **Caveat from Seabrook: p27 IHC is frequently uninterpretable — their adrenal result lacked a positive internal control, and the pancreatic NET result was non-contributory because non-neoplastic islets showed the same pattern.**
- Tumor histology is otherwise conventional: parathyroid adenoma (usually single); well-differentiated pituitary adenoma by lineage (Green 2025 reported a **mixed somatotroph–lactotroph adenoma**); well-differentiated G1 NETs; atypical thymic carcinoid.
- **LOH analysis** on tumor DNA: informative in a minority (2/5 tumors, both parathyroid, in Frederiksen 2019).

## Genetic testing

**GeneReviews establishes the diagnosis by identification of a germline heterozygous pathogenic or likely pathogenic CDKN1B variant. A VUS neither establishes nor excludes the diagnosis.** Alrezk 2017, verbatim: confirming MEN4 *"should only be made with genetic testing for CDKN1B mutations."*

**Recommended approach (GeneReviews):**
1. **Single-gene testing:** sequence CDKN1B first (small indels, missense, nonsense, splice-site), then **deletion/duplication analysis** if one or no variant is found.
2. **Multigene panel** including CDKN1B and other MEN/parathyroid/pituitary genes may be considered; gene content and sensitivity vary by laboratory.

**Detection sensitivity:** sequencing ~95% of probands with a pathogenic variant; del/dup has identified 2 individuals.

**Critical coverage point:** several pathogenic MEN4 variants are in the **5′UTR / uORF** (c.-456_-453delCCTT, c.-29_-26delAGAG, c.-7G>C, c.-80C>T). GeneReviews notes that non-coding variants, including 5′UTR variants, have functional evidence. **Many panels and standard exomes do not reliably cover the 5′UTR — a negative CDKN1B result from a coding-only assay does not exclude MEN4.** *(This inference is mine, drawn directly from the retrieved variant list plus GeneReviews' statement; no retrieved source states it in those words, but it follows.)*

- **WES:** used as the primary screening modality in Chasseloup 2020 (157 germline-only, 27 germline + tumor). Useful; 5′UTR coverage is the limitation.
- **WGS:** no MEN4-specific utility data retrieved.
- **CMA / karyotype / FISH:** indicated only for suspected 12p13.1 contiguous deletions; CMA detected the maternal deletion in the Grey 2013 biallelic case. Not a routine MEN4 test.
- **mtDNA testing, repeat expansion testing:** **not applicable.**
- **Omics-based diagnostics (RNA-seq, proteomics, metabolomics, epigenomics, liquid biopsy):** **no established diagnostic role in MEN4; none retrieved.** RNA studies would be mechanistically apt for splice-predicted variants such as c.475G>A (p.Asp159Asn, predicted to abolish the exon 1 splice donor — Seabrook 2022), but no such assay is described in MEN4.

## Clinical criteria and differential diagnosis

GeneReviews: MEN4 should be suspected in **multiple/multifocal or early-onset endocrine tumors, especially parathyroid and/or pituitary**. **No clinical criteria capture all affected individuals.** An AD family history is supportive, but its absence does not exclude the diagnosis. Alrezk: menin-negative MEN1 cases should be carefully assessed for possible MEN4.

**Differential diagnosis (GeneReviews Table 3a):**

| Gene / disorder | MOI | Overlap | Distinguishing features |
|---|---|---|---|
| **MEN1** | AD | All features | Earlier onset (31.8 vs 43.5 y mean), multiglandular parathyroid disease, higher NET burden, cutaneous tumors (absent in MEN4) |
| **AIP** (PITA1) | AD | Pituitary adenoma | Earlier pituitary onset than MEN4; AIP tumors mostly **GH**, MEN4 pituitary tumors mostly **ACTH** |
| **GPR101** (PITA2) | XL | GH adenoma | No other MEN4-typical endocrinopathies; no GEP-NETs |
| **CDH23** (PITA5) | AD | GH and nonfunctioning adenomas | No other MEN4-typical endocrinopathies; no GEP-NETs |
| **CASR, CDC73, GCM2, MEN1** (FIHP) | AD | Parathyroid adenoma/hyperplasia | Parathyroid-only; no pituitary tumors or GEP-NETs. 14–18% of FIHP families have CASR variants (Simonds 2002, PMID 11807402; Warner 2004, PMID 14985373); CDC73 → HPT-JT |
| **RET** (MEN2A) | AD | PHPT in ~20–30% | MTC + pheochromocytoma; MEN2A PHPT is less penetrant than MEN4 PHPT |

**Sporadic PHPT** (usually a single adenoma) peaks in the sixth decade — **similar to the MEN4 mean age**, which is precisely why MEN4 is hard to recognize clinically. (GeneReviews.)

**Feature-level differential (Table 3b):** gastrinomas also occur in MEN1, tuberous sclerosis, and NF1; nonfunctioning NETs occur in MEN1 (20–55%), VHL (10–17%), and NF1; carcinoids *not* associated with MEN4 are usually midgut/hindgut and serotonin-secreting.

## Screening of asymptomatic individuals

- **Cascade (predictive) genetic testing** of first-degree relatives once a familial variant is identified — GeneReviews calls this **strongly recommended**. Seabrook Family B illustrates its value: the proband's mother tested **wild-type**, ending her surveillance.
- GeneReviews notes ASCO (2003, PMID 12692171) suggested delaying predictive testing until **age 18**, given low childhood risk. ➜ **This sits in direct tension with the pediatric Cushing data (mean CD onset 10.5 y; gigantism at 6 y; meningioma at 6 y). I am flagging this as an unresolved conflict in the guidance, not endorsing either position.**
- Where testing is unavailable or uninformative, first-degree relatives (50% risk) should undergo clinical surveillance.
- **No newborn screening, no population carrier screening, no biochemical population screening** exists or is proposed.

---

# 11. Outcome / Prognosis

**Overall framing:** there is **no survival study, no registry-based mortality analysis, and no life-expectancy estimate for MEN4.** Everything below is extrapolated from lesion-level outcomes in small case series. I state this plainly rather than supplying a number.

## Survival and mortality

- **5-year/10-year/overall survival: not available.** No SEER or registry data exist for MEN4.
- **Life expectancy: not estimated.**
- **Disease-specific mortality: not quantified.**
- The dominant mortality risk is inferable from one finding: GeneReviews, citing Singeisen 2023, states **about half of GEP-NETs are metastatic at diagnosis** (Singeisen's text: 4/9), including metastatic gastrinoma, metastatic ileal NET, and metastatic lung carcinoid. *Inference (mine): NET metastasis, not PHPT or pituitary disease, is the plausible driver of MEN4-attributable mortality. No retrieved source states this.*
- GeneReviews states that early detection and treatment **"should reduce the morbidity and mortality of MEN4"** — note the conditional "should"; this is an expectation, not a measured outcome.

## Morbidity and function

- PHPT morbidity: nephrolithiasis, nephrocalcinosis, osteopenia/osteoporosis, hypercalcemic symptoms. Generally **mild**; GeneReviews describes PHPT as often found in asymptomatic people.
- Cushing disease morbidity: in Seabrook Patient C, SBP 199/80 mmHg and **type 2 diabetes that resolved after surgery** — i.e. reversible with cure.
- Acromegaly/gigantism morbidity: standard GH-excess sequelae; pediatric cases risk permanent excessive stature.
- NET morbidity: dominated by metastatic disease and by the surgical burden — Seabrook Patient A required **distal pancreatectomy and then total pancreaticoduodenectomy** for recurrence, which carries permanent exocrine and endocrine pancreatic insufficiency.
- **Disability outcomes:** no ICF-coded or registry disability data. **Gap.**
- **Quality of life:** **no EQ-5D, SF-36, PROMIS, or disease-specific QoL instrument has ever been applied to MEN4 in any retrieved source. Complete gap.**

## Disease course and recovery

- **Recovery potential is good for the individual lesion:** parathyroidectomy is typically curative with low recurrence (2/36, 6%, Singeisen; Alrezk: no reported recurrence after resection); pituitary surgery achieved remission in the Gambino father–daughter pair; Seabrook Family C had no recurrence at 2 years post-resection and radiotherapy; Seabrook Family B no PHPT recurrence at 3 years.
- **But the predisposition persists:** Seabrook Patient A had recurrent PHPT at 45 from a *second* adenoma after resection at 32–33, and recurrent pancreatic NET after partial pancreatectomy. Lifelong surveillance is therefore required despite excellent per-lesion outcomes.
- **Complications:** hypercalcemic crisis, renal impairment from stones/nephrocalcinosis, fragility fracture, Cushing-related cardiometabolic disease, ZES-related peptic complications, metastatic NET, and surgical complications (hypoparathyroidism, hypopituitarism, pancreatic insufficiency).

## Prognostic factors

- **Genotype:** indels and codon 94–96 variants predict higher PHPT and pituitary adenoma risk (Halperin 2023). **This is the only validated genotype-based prognostic stratifier in MEN4.**
- **Organ involved:** NET involvement is the adverse prognostic feature; isolated PHPT is benign.
- **Age at first manifestation and number of organs involved** are plausible but **unvalidated** prognostic factors (56% single-organ, 10% four-organ in Singeisen).
- **Prognostic biomarkers:** none validated. **p27 IHC loss has not been evaluated as a prognostic marker in MEN4** — and the SI-NET literature found p27 expression did *not* track with CDKN1B mutation status, which argues against its prognostic utility.

---

# 12. Treatment

**Framing, stated explicitly by the primary source:** GeneReviews states there are **no consensus clinical practice guidelines for MEN4**, and that MEN1 protocols are used as a guide, with the caveat that MEN4 is more attenuated. Ruggeri 2023 (PMID 37632635) similarly calls for a standardized screening protocol and more study of oncological risk.

## Surgical and interventional (the mainstay)

| Manifestation | Treatment | NCIT |
|---|---|---|
| PHPT | **Parathyroidectomy** — GeneReviews Table 5 | **NCIT:C51593** Parathyroidectomy |
| PHPT, extent | Alrezk 2017: parathyroid surgery **should be individualized**; some patients may be treated like MEN1 with **3.5-gland resection**. *Note the tension with the 86%-uniglandular data — focused/targeted parathyroidectomy is biologically defensible in MEN4, unlike MEN1. I am flagging this as an unsettled management question, not a recommendation.* | — |
| ACTH- or GH-secreting pituitary adenoma | **Surgery, by a surgeon with pituitary expertise** (GeneReviews) | Transsphenoidal hypophysectomy — **NCIT term not retrieved**; OLS returned zero hits for this string. Do not assign an ID without re-checking. |
| NETs and carcinoids | **Surgical resection if possible**; refer to medical oncology | **NCIT:C15294** Pancreatectomy (for pancreatic lesions) |
| Thymic carcinoid | Resection + adjuvant radiotherapy (Seabrook Family C: 60 Gy in 30 fractions) | — |

## Pharmacotherapy

| Agent | Indication in MEN4 | Identifiers |
|---|---|---|
| **Cabergoline** | Prolactinoma (GeneReviews Table 5). Seabrook Patient A's microprolactinoma normalized on cabergoline. | **CHEBI:3286**; **NCIT:C47428** |
| **Cinacalcet** (calcimimetic, CaSR agonist) | "May be considered for symptomatic hypercalcemia in non-surgical candidates" (GeneReviews) | **CHEBI:48390**; **NCIT:C74100** (also NCIT:C47450 Cinacalcet Hydrochloride) |
| **Proton pump inhibitors** | Gastrin-secreting tumors (GeneReviews) | **NCIT:C29723** Proton Pump Inhibitor |
| **Somatostatin analogs** | "Some may receive somatostatin analogs" for NETs (GeneReviews) | **CHEBI:7726** octreotide; **CHEBI:135901** lanreotide; **CHEBI:72312** pasireotide. *NCIT: a drug-class term was not retrieved; the closest title returned was NCIT:C15449 "Somatostatin Analog Therapy," which is a therapy, not a class term — flagging as a lump/split call.* |
| **Everolimus** (mTOR inhibitor) | **Not named in any MEN4-specific guidance I retrieved.** Standard in sporadic advanced pNET; I include the identifiers only because the KB asked for candidate NCIT/CHEBI terms. **Do not record as a MEN4 treatment.** | CHEBI:68478; NCIT:C48387 |
| Calcium ion (analyte, not a drug) | monitoring | **CHEBI:29108** calcium(2+) |

## Pharmacogenomics
**No MEN4-specific pharmacogenomic data retrieved.** PharmGKB/CPIC were not queried directly; I found no literature signal. **Gap.**

## Advanced therapeutics
- **Gene therapy, cell therapy, RNA-based therapy, targeted therapy against p27 restoration, immunotherapy: none exist for MEN4.** No MEN4-specific trial was retrieved.
- Mechanistically, **restoring p27 dosage** (rather than inhibiting a driver) is the implied therapeutic target, which is a hard problem — loss-of-function tumor suppressors are not directly druggable. CDK4/6 or CDK2 inhibition is the obvious pharmacological logic given the mechanism. **I found no study testing this in MEN4 or in CDKN1B-mutant endocrine tumors. This is model reasoning, explicitly labeled as such, not a retrieved finding.**

## Supportive and rehabilitative
- Symptom management of hypercalcemia; post-surgical hormone replacement (hypoparathyroidism, hypopituitarism); pancreatic enzyme replacement after extensive pancreatic resection. **No MEN4-specific supportive-care or rehabilitation literature retrieved.**

## Experimental treatments
GeneReviews directs readers to ClinicalTrials.gov and the EU Clinical Trials Register and **notes there may not be trials**. **I retrieved no NCT identifier for a MEN4-specific interventional trial.** (NCT00001595, "An Investigation of Pituitary Tumors and Related Hypothalamic Disorders," appeared in search results as an NIH natural-history/observational protocol relevant to the Chasseloup cohort context — *observational, not a MEN4 treatment trial*.)

## Treatment outcomes
- **Response rates:** no systematic data. Per-lesion outcomes are summarized in §11.
- **Adverse events:** no MEN4-specific FAERS or trial safety data. Risks are those of the respective surgeries and drugs.

## Treatment strategy / personalized medicine
- No MEN4 treatment algorithm exists. The operative strategy is **surveillance-driven early detection → lesion-directed surgery → lifelong continued surveillance.**
- The one genuinely genotype-informed element available is **Halperin's variant-type and codon 94–96 stratification**, which could in principle intensify parathyroid and pituitary surveillance in indel and codon-94–96 carriers. **No guideline has adopted this. Recording it as a research-grade stratifier.**

**Genetic counseling as intervention:** **NCIT:C15240** Genetic Counseling. **NCIT:C16809** Magnetic Resonance Imaging (surveillance intervention).

---

# 13. Prevention

## Primary prevention
**Not possible** — the causal variant is germline and constitutional. No vaccination, risk-factor modification, or behavioral intervention prevents MEN4. The only true primary-prevention options are **reproductive**: GeneReviews states *"Once the CDKN1B pathogenic variant has been identified in an affected family member, prenatal and preimplantation genetic testing are possible,"* noting that views on their use differ among professionals and families. The chapter recommends discussing family planning **before pregnancy** and offering counseling to affected or at-risk young adults.

## Secondary prevention — surveillance (the core of MEN4 management)

**GeneReviews Table 6 — the only published surveillance schedule specific to MEN4:**

| System | Test | Start age | Interval |
|---|---|---|---|
| Parathyroid | Serum calcium (±PTH, vitamin D) | **25** | **Every 2 years** |
| Pituitary | Serum IGF-1 and prolactin | **25** | Every 3–5 years, or as symptoms indicate |
| Pituitary | **Pituitary MRI** | **25** | **Every 5 years** |
| Pituitary | If Cushing concern: 24-h UFC, late-night salivary cortisol, and/or 1 mg overnight DST | As indicated | As indicated |
| GEP-NET | Serum gastrin | **25** | Table says "biannually"; chapter narrative says "biennial" — **the source is internally ambiguous on this interval** |
| GEP-NET | Abdominal MRI or CT | **25** | **Every 5 years, increasing to every 2.5 years at age 40** |

Abnormal findings warrant more frequent follow-up, using MEN1 guidelines as a guide.

**Evaluations at initial diagnosis (GeneReviews Table 4):** referral to an endocrinologist experienced in MEN; clinical assessment for kidney stones, cortisol/GH/prolactin excess, nausea/vomiting/diarrhea; serum calcium if ≥25 y; pituitary MRI and hormone testing (ACTH, cortisol, IGF-1, prolactin) guided by suspicion if ≥25 y; abdominal contrast CT or MRI if ≥25 y; genetic counseling.

**⚠ The start-age question is genuinely contested, and the sources disagree:**

| Source | Proposed start |
|---|---|
| **GeneReviews 2023** | **Age 25** for all modalities |
| **Frederiksen 2019** (verbatim) | *"it appears prudent to initiate screening of calcium and PTH levels in patients with MEN4 from the age of 15 years"*; pituitary screening with prolactin, IGF-1 and MRI *"may begin in adolescents and not in children as suggested in patients with MEN1"* |
| **NCI PDQ** (search-level) | Surveillance begins at **adolescence** for known CDKN1B carriers |
| **A 2024 MEN review** (search-level) | Biochemical PitNET screening at **age 5**, annual, with imaging every 3 years — *this is an MEN1-derived schedule applied to MEN, not MEN4-specific* |
| **Alrezk 2017** | Pituitary surveillance case-by-case, following existing MEN guidelines |

➜ **Pediatric judgment call to surface for the KB, not to resolve silently:** the GeneReviews age-25 start is justified by the adult-weighted median ages (PHPT 51, pituitary 39, pNET ≥42), but it would **miss every pediatric case in the literature** — Chasseloup's five Cushing disease carriers (mean onset 10.5 y), the gigantism case at age 6, the youngest pituitary adenoma at age 5, the youngest PHPT at 15, and the anaplastic meningioma at 6. The conflict is not an error in GeneReviews; it is a real tension between population-level yield and the pediatric tail. **A defensible middle position — pituitary-directed clinical vigilance and symptom-triggered testing from childhood, with the formal biochemical/imaging program from adolescence — is my inference, not a retrieved recommendation.**

**Breast surveillance:** one StatPearls statement (retrieved only via search snippet, *source not directly readable in this session*) says mammographic breast surveillance is appropriate in women with MEN4. **GeneReviews does not include breast in its surveillance table.** Given that CDKN1B's breast-cancer association rests on somatic enrichment in luminal breast cancer plus isolated germline case reports (e.g. PMC12545434, a 2025 conference abstract of bilateral breast cancer with a CDKN1B mutation), **I would record the breast-cancer link as unestablished and the surveillance recommendation as non-consensus.**

## Tertiary prevention
Post-treatment management to prevent complications: ongoing surveillance after parathyroidectomy for metachronous adenomas (Seabrook Patient A's recurrence at 45); pituitary hormone monitoring post-surgery; NET surveillance post-resection; bone and renal protection in PHPT.

## Genetic screening and risk stratification
- **Cascade testing** of all first-degree relatives — GeneReviews: strongly recommended.
- **Risk stratification candidates:** variant type (indel vs point) and codon 94–96 location (Halperin 2023). **No validated risk prediction model or clinical calculator exists for MEN4.**

## Immunization, behavioral interventions, public health, environmental interventions, prophylaxis
**None applicable.** No vaccine, lifestyle intervention, public-health measure, environmental control, or chemoprophylaxis is relevant to or proposed for MEN4. Prophylactic surgery (as practiced in MEN2A) is **not** recommended in MEN4 by any retrieved source.

---

# 14. Other Species / Natural Disease

## Taxonomy and genes

| Species | NCBI Taxon | Ortholog | Database ID |
|---|---|---|---|
| *Homo sapiens* | NCBI:txid9606 | CDKN1B | NCBI Gene 1027, HGNC:1785 |
| *Rattus norvegicus* | NCBI:txid10116 | Cdkn1b | **RGD:69062** (from HGNC record) |
| *Mus musculus* | NCBI:txid10090 | Cdkn1b | **MGI:104565** (from HGNC record) |

*Taxon IDs are the standard NCBI identifiers for these species; the gene-level ortholog IDs above came from the HGNC record retrieved in this session. **I did not retrieve the NCBI Taxonomy records themselves.***

## Natural disease in other species — the MENX rat

**MENX is the only naturally occurring animal homolog of MEN4, and it is historically the entity that defined the gene.** It arose spontaneously in a Sprague-Dawley-derived rat colony.

- **Genetics:** homozygous **Cdkn1b frameshift — a tandem duplication of 8 nucleotides in exon 2**; mutant p27 is highly unstable and barely detectable in mutant tissue (Pellegata 2006, PMID 17030811).
- **Tumor spectrum (homozygous):** **bilateral adrenal pheochromocytoma**, **multifocal anterior pituitary adenoma** (gonadotroph lineage, nonfunctioning), **extra-adrenal pheochromocytoma/paraganglioma**, **thyroid C-cell hyperplasia**, **parathyroid hyperplasia**, **pancreatic islet hyperplasia**. Adrenomedullary hyperplasia appears at 3–4 months and progresses to pheochromocytoma by 6–8 months, with full penetrance.
- **Heterozygous MENX rats** develop **invasive medullary thyroid carcinoma** and have been proposed as a novel MTC model (Endocr Relat Cancer 2018;25(2):145).
- **Pseudohypoxic pheochromocytoma:** MENX rats develop pheochromocytomas recapitulating key features of human **pseudohypoxic PPGLs**, and the authors propose MENX as the best available model of these tumors (PMID 33401758).
- **Transcriptomics:** MENX rat pheochromocytoma **shares gene expression patterns with human pheochromocytoma**.
- Reviewed by Pellegata NS, "MENX and MEN4," *Clinics* 2012 (PMID 22584700).

## Comparative pathology — a substantive divergence

| Lesion | MENX rat | Human MEN4 |
|---|---|---|
| Zygosity required | **Homozygous** (recessive in the rat) | **Heterozygous** (dominant in humans) |
| Pheochromocytoma / paraganglioma | **Hallmark, bilateral, fully penetrant** | **Not a recognized feature** |
| Medullary thyroid carcinoma | Yes (C-cell neoplasia; MTC in heterozygotes) | **Single uncertain case report** (Mercè 2025) |
| Pituitary adenoma | Yes, nonfunctioning gonadotroph | Yes, but predominantly **ACTH**, then PRL, then GH |
| Parathyroid | **Hyperplasia** | **Adenoma, usually single (86%)** |
| Pancreatic islets | Hyperplasia | Well-differentiated NETs |

➜ **The rat is an excellent model of p27 loss and a poor model of the human MEN4 phenotype.** The zygosity difference alone (recessive rat / dominant human) means the rat models **complete p27 loss**, whereas human MEN4 is predominantly a **haploinsufficiency** disease. **This limits the rat's utility for modeling the human tumor spectrum and should be recorded explicitly in the KB.**

## Evolutionary conservation
p27^Kip1 and the CDK-inhibitory G1/S checkpoint are deeply conserved across vertebrates; the uORF in the CDKN1B 5′UTR disrupted by c.-456_-453delCCTT is described by Occhi 2013 as **"highly conserved."**

## Veterinary relevance, zoonotic potential, cross-species susceptibility
- **Veterinary relevance:** essentially nil outside research. MENX exists only in a laboratory colony. **I found no OMIA record or companion-animal/wildlife natural disease report for CDKN1B-related MEN** — OMIA was not directly queried and returned no hits in my literature searches. **Stated as not found, not as absent.**
- **Zoonotic potential: not applicable** (germline genetic disease).
- **Cross-species susceptibility: not applicable.**

---

# 15. Model Organisms

## Rat — MENX (the defining model)
- **Type:** spontaneous (not engineered) germline *Cdkn1b* 8-bp exon 2 tandem duplication; **mammalian, in vivo**.
- **Phenotype recapitulation:** excellent for **multiple endocrine neoplasia as a concept** and for **p27-loss tumor biology**; it directly enabled the discovery of human MEN4 (Pellegata 2006). Poor for the specific human MEN4 tumor spectrum (see §14 table).
- **Limitations:** recessive/homozygous requirement; pheochromocytoma-dominant; no human MEN4 counterpart for the PPGL phenotype; does not model haploinsufficiency.
- **Applications:** pheochromocytoma and pseudohypoxic PPGL biology; MTC (heterozygotes); comparative transcriptomics; preclinical NET therapeutics.
- **Database:** RGD:69062.

## Mouse — *Cdkn1b* knockouts
Three 1996 *Cell* papers established the p27-null mouse: **Fero et al.** (85:733), **Kiyokawa et al.** (85:721), and **Nakayama et al.** (85:707, "Mice lacking p27Kip1 display increased body size, multiple organ hyperplasia, retinal dysplasia, and pituitary tumors"). **⚠ Provenance: I confirmed these titles and the phenotype summaries only through search snippets and secondary reviews; I did not retrieve the primary full texts or abstracts in this session. Treat the following as review-level, not primary-verified.**

- **p27^−/−:** gigantism/increased body size, multiorgan hyperplasia (including brain), retinal dysplasia, **intermediate-lobe pituitary adenomas/nodular hyperplasia**, female sterility. Kiyokawa reported that increased growth occurs **without an increase in GH or IGF-I**.
- **p27^+/−:** pituitary **hyperplasia**; gigantism and multiorgan hyperplasia are **not** seen in heterozygotes — a notable mismatch with the human dominant syndrome.
- **Mechanistic extension:** one study reported that p27 absence drives gigantism via **increased Sox2**, as p27 directly inhibits Sox2 expression (*search-level retrieval; primary source not opened*).
- **Compound mutants:** *Rb1^G/G; Cdkn1b^−/−* mice develop pituitary tumors with complete penetrance, with the hypomorphic *Rb1^G* allele cooperating preferentially with p27 loss (*search-level retrieval*). *Rb1^+/−* mice alone develop pituitary and thyroid C-cell neuroendocrine tumors.
- **Oncogenic p27:** a knock-in model revealed "an oncogenic activity in p27Kip1 that causes stem cell expansion and a multiple tumor phenotype" (PMC1920168) — relevant to the non-canonical/cytoplasmic p27 branch in §6.
- **Database:** MGI:104565. **I did not retrieve the MGI allele list or IMPC/KOMP/IMSR records in this session** — any specific allele designation should be looked up directly.

**Gap flagged:** I searched specifically for a **Cdkn1b^+/− mouse model of duodenal or parathyroid neoplasia** and **found no such report**. The mouse heterozygote does not appear to phenocopy human MEN4.

## In vitro and cellular models (all retrieved from primary MEN4 papers)

| System | Use | Source |
|---|---|---|
| **AtT20** (mouse corticotroph) | p27 variant subcellular localization; POMC/ACTH output | Chasseloup 2020 |
| **HEK293** | co-immunoprecipitation with RHOA and CDKs; half-life; 5′UTR–CDKN1B construct western blot | Chasseloup 2020; Occhi 2013 |
| **GH3** (rat pituitary) and **HeLa** | dual-luciferase uORF reporter assays, lovastatin-synchronized and asynchronous | Occhi 2013 |
| **SH-SY5Y, HEK293** | secondary uORF reporter confirmation | Occhi 2013 (Figure S1) |
| **Patient lymphoblastoid cell lines** | allele-specific expression; **polysome profiling** (~90% of each allele's mRNA in polysomes, fractions 7–11) | Occhi 2013 |
| **Breast cancer cell lines** | proliferation, motility, phosphorylation, localization, degradation, cyclin/CDK binding of four MEN4/cancer CDKN1B mutants | Bencivenga 2025, PMID 39936980 — **abstract only; full text blocked** |
| **Cycloheximide chase (25 µM)** | protein half-life, one-phase decay with extra sum-of-squares F test | Chasseloup 2020 methods |

**Not available:** no MEN4 **iPSC**, **organoid**, **zebrafish**, **Drosophila**, **C. elegans**, or **yeast** model was retrieved. No MEN4 patient-derived xenograft. **These are genuine gaps.**

## In silico / structural
Papadopoulou-Marketou et al. 2026 (Endocr Relat Cancer, PMID 42993098) performed **structural modelling of CDKN1B and CDKN2C variants in MEN-like phenotypes** — proband 1 with CDKN1B **p.Lys96GlnfsTer29**, proband 2 with CDKN2C p.Leu107Val (VUS). *Abstract-level retrieval via Europe PMC; computational evidence class.*

---

# Summary of evidence quality and gaps

**Strongest evidence (curated guideline + systematic review):** tumor spectrum, inheritance, diagnostic approach, differential diagnosis, surveillance schedule — GeneReviews NBK594826 (PMID 37733893); Singeisen 2023 (PMID 36520683).

**Moderate (pooled cohort analysis, not independently replicated):** penetrance estimates (Halperin 2023, PMID 36256846: 53.4% / 23.2% / 16.2% by age 60) and genotype-phenotype (indels; codons 94–96). **Full text not retrieved — abstract-level only.**

**Moderate-to-strong (mechanistic, in vitro):** the uORF translational-reinitiation mechanism (Occhi 2013, PMID 23555276) and variant-specific protein instability/mislocalization (Chasseloup 2020, PMID 32232325).

**Weak / lead-grade only — do NOT record as established:** medullary thyroid carcinoma association (n=1); breast cancer association (somatic enrichment + case reports); meningioma and CNS tumors (n=1 pediatric, no second hit); papillary thyroid carcinoma (GeneReviews calls it "emerging"); autoimmune association; insulinoma (conference abstract).

**Complete gaps with no data in any retrieved source:**
- Survival, life expectancy, mortality, disease-specific mortality
- Any formal quality-of-life measurement
- Incidence; carrier frequency; population-specific or founder effects
- Environmental, lifestyle, infectious, or gene–environment contributions (untested, not tested-negative)
- Protective factors of any kind
- Epigenomic, transcriptomic, proteomic, metabolomic, single-cell, spatial, or functional-genomics data in human MEN4
- Pharmacogenomics; any MEN4-specific interventional clinical trial (no NCT retrieved)
- Validated prognostic model or biomarker
- iPSC/organoid/non-mammalian models
- OMIA record for a naturally occurring CDKN1B-related MEN in a companion or wild animal

**Sources that could not be opened in this session and whose content is therefore not represented:** OMIM 610755 and 600778 (HTTP 403, including the allelic-variant table), Orphanet ORPHA:276152 (bot challenge — so the "<1/1,000,000" prevalence is cited secondhand via Singeisen 2023), NCBI Gene and ClinVar web pages and NCBI Bookshelf /books/ URLs (reCAPTCHA), StatPearls NBK568728, EndoText MEN4 (HTTP 429), Ruggeri 2023 *Endocrine* full text (Springer login gate), Halperin 2023 full text (HTTP 403 at both ERC and ScienceDirect), and Bencivenga 2025 full text (reCAPTCHA). Several PMC full texts (Frederiksen, Seabrook, Occhi, Chasseloup, Singeisen, Alrezk, Chevalier) were read only to ~40,000 characters, and I have marked every claim drawn from the model-summarized remainder as lead-grade.

---

## Sources

- [GeneReviews: Multiple Endocrine Neoplasia Type 4 (NBK594826, PMID 37733893)](https://www.ncbi.nlm.nih.gov/sites/books/NBK594826/)
- [Pellegata et al., PNAS 2006 (PMID 17030811)](https://pubmed.ncbi.nlm.nih.gov/17030811/) · [PNAS full text](https://www.pnas.org/doi/10.1073/pnas.0603877103)
- [Singeisen et al., Endocr Connect 2023 (PMID 36520683, PMC9874964)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9874964/)
- [Halperin et al., Endocr Relat Cancer 2023 (PMID 36256846)](https://pubmed.ncbi.nlm.nih.gov/36256846/?dopt=Abstract)
- [Chevalier et al., JCEM 2024 (PMID 38288531, DOI 10.1210/clinem/dgae055)](https://academic.oup.com/jcem/article/109/7/e1482/7591647)
- [Frederiksen et al., JCEM 2019 (PMID 30990521, PMC6637788)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6637788/)
- [Seabrook et al., JCEM 2022 (PMID 35323929, PMC9282358)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9282358/)
- [Chasseloup et al., JCEM 2020 (PMID 32232325, PMC7190031)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7190031/)
- [Occhi et al., PLoS Genet 2013 (PMID 23555276, PMC3605397)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3605397/)
- [Alrezk et al., Endocr Relat Cancer 2017 (PMID 28824003, PMC5623937)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5623937/)
- [Ruggeri et al., Endocrine 2023 (PMID 37632635)](https://link.springer.com/article/10.1007/s12020-023-03497-2)
- [Bencivenga et al., Cells 2025 (PMID 39936980)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11817124/)
- [Francis et al., Nat Genet 2013 — somatic CDKN1B in SI-NET (PMID 24185511)](https://www.nature.com/articles/ng.2821)
- [Grey et al., Hum Mutat 2013 — biallelic CDKN1B deficiency (PMID 23505216)](https://onlinelibrary.wiley.com/doi/10.1002/humu.22314)
- [Desrosiers-Battu et al., Cancer Genet 2025 (PMID 39985924)](https://pubmed.ncbi.nlm.nih.gov/39985924/)
- [Mercè et al., Fam Cancer 2025 (PMID 40009226)](https://link.springer.com/article/10.1007/s10689-025-00449-9)
- [Besson et al., Genes Dev 2004 — p27 and RhoA](https://genesdev.cshlp.org/content/18/8/862.full.html)
- [Skp2-dependent degradation of p27, Genes Dev 2004](https://genesdev.cshlp.org/content/18/21/2602.full.html)
- [Thr187 phosphorylation and SCF-Skp2, Curr Biol 1999](https://www.sciencedirect.com/science/article/pii/S0960982299802905)
- [Cryo-EM SKP1-SKP2-CKS1 / CDK2-cyclin A-p27, Sci Rep 2023](https://www.nature.com/articles/s41598-023-37609-9)
- [MENX heterozygous rats / invasive MTC, Endocr Relat Cancer 2018](https://erc.bioscientifica.com/view/journals/erc/25/2/ERC-17-0456.xml)
- [p27 mutation drives pseudohypoxic pheochromocytoma (PMID 33401758)](https://pubmed.ncbi.nlm.nih.gov/33401758/)
- [Pellegata, "MENX and MEN4," Clinics 2012 (PMID 22584700)](https://www.elsevier.es/en-revista-clinics-22-articulo-menx-men4-S1807593222023900)
- [Oncogenic activity in p27Kip1 (PMC1920168)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1920168/)
- [UniProt P46527 (CDKN1B / p27Kip1)](https://rest.uniprot.org/uniprotkb/P46527.json)
- [HGNC:1785 CDKN1B](https://rest.genenames.org/fetch/symbol/CDKN1B)
- [MONDO:0012552 via EBI OLS4](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMONDO_0012552)
- [HPO annotations for OMIM:610755](https://ontology.jax.org/api/network/annotation/OMIM:610755) · [Monarch MONDO:0012552](https://api-v3.monarchinitiative.org/v3/api/entity/MONDO:0012552)
- [NCI PDQ: Genetics of Endocrine and Neuroendocrine Neoplasias](https://www.cancer.gov/types/thyroid/hp/medullary-thyroid-genetics-pdq)
- [Multiple Endocrine Neoplasia and HPT-JT: surveillance in childhood, Clin Cancer Res 2017](https://dx.doi.org/10.1158/1078-0432.CCR-17-0548)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 64 |
| Resolved | 64 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 64 |
| On topic | 45 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC1920168` *(abstract only)*: "an oncogenic activity in p27Kip1 that causes stem cell expansion and a multiple tumor phenotype"
  - closest text in source: "Therefore, independently of its role as a CDK inhibitor, p27Kip1 promoted stem cell expansion and functioned as a dominant oncogene in vivo"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:25741868` (1 mention) - Standards and guidelines for the interpretation of sequence variants: a joint consensus recommendation of the American College of Medical Genetics and Genomics and the Association for Molecular Pathology.
  - shared terms: variant

Weighed against this report's own most characteristic terms: `men4`, `cdkn1b`, `variant`, `tumor`, `pituitary`, `endocrine`, `disease`, `parathyroid`, `adenoma`, `found`, `patient`, `phpt`, `singeisen`, `p27`, `men1`, `family`, `germline`, `verbatim`, `age`, `cancer`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 131 |
| Resolved | 120 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 11 |
| Terms whose name was checked | 13 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012552` (21 mentions) - the report calls it "HTTP 200.** Returned `"has_phenotype_count":44` in `has_phenotype", "multiple endocrine neoplasia type 4"; MONDO calls it **multiple endocrine neoplasia type 4**
- `DOID:0080137` (2 mentions) - the report calls it "DOID"; DOID calls it **multiple endocrine neoplasia type 4**
- `NCIT:C157449` (2 mentions) - the report calls it "NCIT"; NCIT calls it **Multiple Endocrine Neoplasia Type 4**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0002311` (2 mentions) - the report calls it "Lactotroph / mammotroph"; CL calls it **mammotroph**
- `CL:0000570` (2 mentions) - the report calls it "Parafollicular (C) cell"; CL calls it **parafollicular cell**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0012552` - called "HTTP 200.** Returned `"has_phenotype_count":44` in `has_phenotype", "multiple endocrine neoplasia type 4"
- `OMIM:610755` - called "all three endpoints failed", "phenotype"
- `ORPHA:276152` - called "Orphanet", "bot challenge — so the "<1/1,000,000" prevalence is cited secondhand via Singeisen 2023"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `GARD`, `OMIM`, `Orphanet`, `SCTID`, `UMLS`, `MGI`, `RGD`, `NCBIGene`, `ORPHA`.