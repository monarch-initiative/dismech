---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-11-20T20:12:06.415261'
end_time: '2026-11-20T20:31:34.446216'
duration_seconds: 1168.03
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Cribriform Neuroepithelial Tumor
  mondo_id: MONDO:1060254
  category: ''
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: CRINET
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
  web_search_requests: 17
  num_turns: 111
  total_cost_usd: 6.795088249999999
  session_id: 466caebc-9ba0-4d41-8128-b1f3e205c0c6
  stop_reason: end_turn
  tool_calls: 109
  retrieval_calls: 109
  assistant_text_blocks: 1
citation_count: 47
reference_validation:
  total_references: 78
  verified: 77
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.013
  quotes_checked: 21
  quotes_valid: 12
  quotes_unsupported: 9
  unsupported_quote_references:
  - PMID:33532948
  - DOI:10.1007/s10689-021-00229-1
  - PMID:35673730
  - PMID:42753289
  - PMID:36884098
  - PMID:34151393
  quotes_not_checkable: 2
  relevance_assessed: 77
  on_topic: 41
  unresolved_references:
  - DOI:10.3760/cma.j.cn112151-20211104-00799
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 34
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 5
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 12
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:1060254
    reported_labels:
    - Mondo
    - EBI OLS4
    ontology_label: cribriform neuroepithelial tumor
  - term_id: NCIT:C121963
    reported_labels:
    - NCI Thesaurus
    - EBI OLS4
    ontology_label: Cribriform Neuroepithelial Tumor
  - term_id: HP:0001251
    reported_labels:
    - Ataxia / gait disturbance, motor regression
    ontology_label: Ataxia
  - term_id: GO:0071565
    reported_labels:
    - verified
    ontology_label: nBAF complex
  labels_variant: 4
  unresolvable_prefixes:
  - MGI
  - RGD
  - SGD
  - EXT_ID
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cribriform Neuroepithelial Tumor
- **MONDO ID:** MONDO:1060254 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** CRINET
- **Category:** 

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Cribriform Neuroepithelial Tumor** covering all of the
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

# Cribriform Neuroepithelial Tumor (CRINET) — MONDO:1060254

## Comprehensive Disease Characteristics Report

**Prepared:** 20 November 2026 · **Target entity:** cribriform neuroepithelial tumor (CRINET), MONDO:1060254

**Interpretation note (stated up front, per instruction):** The template lists "Causal gene(s): not recorded." Retrieval in this session establishes unambiguously that **the causal gene of CRINET is *SMARCB1*** (SWI/SNF related, matrix associated, actin dependent regulator of chromatin, subfamily B, member 1; HGNC:11103; Entrez Gene 6598; Ensembl ENSG00000099956; UniProt Q12824; OMIM \*601607; cytoband 22q11.23; GRCh38 chr22:23,786,931–23,838,009, + strand) — retrieved from the HGNC REST service (https://rest.genenames.org/fetch/symbol/SMARCB1) and the Ensembl REST lookup (https://rest.ensembl.org/lookup/symbol/homo_sapiens/SMARCB1). *SMARCB1* is also known as *SNF5*, *INI1*, *BAF47*, *hSNF5*, and *SNF5L1*. CRINET is a **tumor**, not a constitutional Mendelian disorder, so several template sections (inheritance pattern of the disease itself, anticipation, carrier frequency, infectious agents, immunization) are answered as "not applicable," while the *germline* predisposition dimension is covered under rhabdoid tumor predisposition syndrome type 1 (RTPS1).

A second disambiguation caution for knowledge-base curation: **PubMed queries for the string "CRINET" also retrieve a wholly unrelated bioinformatics tool** — "Crinet: A computational tool to infer genome-wide competing endogenous RNA (ceRNA) interactions" (Kesimoglu & Bozdag, *PLoS One* 2021; PMID 33983999; doi 10.1371/journal.pone.0251399). Do not conflate.

---

## 1. Disease Information

### 1.1 Overview

Cribriform neuroepithelial tumor is a **very rare, non-rhabdoid, intra-/para-ventricular embryonal CNS neoplasm of infants and young children, defined by loss of nuclear SMARCB1 (INI1) protein expression combined with a distinctive cribriform (sieve-like) architecture of strands, ribbons and trabeculae with EMA-positive luminal surfaces, and associated with a markedly more favorable outcome than atypical teratoid/rhabdoid tumor (AT/RT).**

The ontology definition shared verbatim by MONDO, NCI Thesaurus and MedGen (retrieved from EBI OLS4 and NCBI MedGen) is:

> "A very rare, nonrhabdoid, intraventricular tumor with relatively favorable prognosis. It is characterized by the presence of neuroepithelial cells forming cribriform patterns, trabeculae, epithelial membrane antigen immunopositivity on epithelial surfaces, and loss of nuclear INI 1 expression."
> — NCIT:C121963 / MONDO:1060254 / MedGen UID 888969

The entity was first delineated by Hasselblatt and colleagues in 2009 (*J Neuropathol Exp Neurol* 68:1249–1255; PMID 19915490; doi 10.1097/NEN.0b013e3181c06a51), who reported two young children with intracranial non-rhabdoid neuroectodermal tumors "within and around the third or fourth ventricle that are characterized by cribriform strands and trabeculae and well-defined epithelial membrane antigen-immunopositive surfaces and show INI1 protein loss," and proposed the designation of "a nonrhabdoid ventricular tumor that shows loss of tumoral INI1 protein and has a relatively favorable prognosis."

The definitive molecular characterization is Johann et al., *Brain Pathology* 2017;27(4):411–418 (PMID 27380723; doi 10.1111/bpa.12413; free full text at PMC8028967), which analyzed ten CRINETs against ten AT/RTs from each of the three molecular subgroups and concluded:

> "In conclusion, CRINET represents a SMARCB1 deficient non-rhabdoid tumor clustering with the AT/RT-TYR subgroup. Molecular alterations responsible for the relatively favorable outcome of CRINET as compared to AT/RT remain to be determined."

### 1.2 Key identifiers (all retrieved this session)

| Resource | Identifier | Notes |
|---|---|---|
| **Mondo** | **MONDO:1060254** | Label "Cribriform neuroepithelial tumor"; subsets `inferred_rare`, `rare`; term tracker https://github.com/monarch-initiative/mondo/issues/10359 |
| **NCI Thesaurus** | **NCIT:C121963** | Preferred name "Cribriform Neuroepithelial Tumor"; semantic type Neoplastic Process; neoplastic status "Undetermined" |
| **UMLS** | **C4053528** | |
| **MedGen** | **888969** | Cross-references listed: MONDO only |
| **Causal gene** | HGNC:11103 / Entrez 6598 / Ensembl ENSG00000099956 / OMIM \*601607 / UniProt Q12824 | *SMARCB1*, 22q11.23 |
| **Germline predisposition** | OMIM **609322** (RTPS1, *SMARCB1*); OMIM 613325 (RTPS2, *SMARCA4*) | From GeneReviews "Rhabdoid Tumor Predisposition Syndrome" (Nemes K, Bens S, Bourdeaut F, et al., last update 12 May 2022) |
| **Orphanet** | **Not retrieved** | No ORPHA code found in Orphanet or as a MONDO/MedGen xref |
| **OMIM (for the tumor itself)** | **Not retrieved / none identified** | CRINET has no dedicated OMIM phenotype entry that I could retrieve |
| **ICD-10 / ICD-11 / ICD-O** | **Not retrieved** | No dedicated code was found; MedGen lists no ICD cross-reference. WHO CNS5 lists CRINET as a *provisional* type (italicized, Table 1) under "Other CNS embryonal tumors" without a grade (see §1.4) |
| **MeSH** | No dedicated descriptor retrieved | PubMed indexing of the Johann 2017 paper uses "Neoplasms, Neuroepithelial (genetics)", "Rhabdoid Tumor (genetics)", "Brain Neoplasms (genetics)", "SMARCB1 Protein (deficiency/genetics)", "Mutation" (Europe PMC core record). The Tauziède-Espariat 2021 record is indexed to "Cerebral Ventricles" and "Neuroepithelial Neoplasms/diagnostic imaging" |
| **SNOMED CT** | Not retrieved | |

### 1.3 Synonyms and alternative names

- **CRINET** (standard abbreviation; exact synonym in MONDO/NCIT/MedGen)
- Cribriform neuroepithelial tumour (British spelling, used by Ibrahim et al., *Acta Neuropathol* 2011)
- **PICRINET** — "primary intracranial cribriform neuroepithelial tumor," a neologism introduced only by a 2025 systematic review (Qadri et al., *OncoDaily Medical Journal*, 19 Sep 2025; doi 10.69690/ODMJ-018-0915-5372); not in general use and not an ontology synonym
- Historically described in the literature as "a recently identified variant of atypical teratoid/rhabdoid tumor with a favorable prognosis" (Dahlback et al. 2011, PMID 21717527)

### 1.4 WHO classification status

CRINET entered formal classification in the **5th edition of the WHO Classification of Tumours of the CNS (CNS5, 2021)**. Per the official summary (Louis DN, Perry A, Wesseling P, et al. *Neuro-Oncology* 2021;23(8):1231–1251; PMID 34185076; doi 10.1093/neuonc/noab106), CRINET appears:
- in **Table 1** (the classification table), **in italics**, under **"Other CNS embryonal tumors"**;
- in **Table 7** ("Newly Recognized Tumor Types") as "*Cribriform neuroepithelial tumor* (provisional type)";
- in the text of the "Other Embryonal Tumors" section: "CRINET has been introduced as a provisional entity within this category."

A 2023 neuroradiology review of the CNS5 novelties states that **"Cribriform neuroepithelial tumor is a benign tumor that has not yet been assigned a WHO grade"** (Rigsby RK, Brahmbhatt P, Desai AB, et al. "Newly Recognized CNS Tumors in the 2021 World Health Organization Classification: Imaging Overview with Histopathologic and Genetic Correlation." *AJNR Am J Neuroradiol* 2023;44(4):367–380; PMID 36997287; PMC10084895; doi 10.3174/ajnr.a7827). Note this "benign" characterization is a radiology review's wording and sits uneasily with the tumor's embryonal histology and Ki-67 of ~29%; the primary literature consistently says "relatively favorable," not benign.

A 2026 biomarker review restates the current position (Eaton S, Almotairi A, Levine A, Hawkins C. *Neurotherapeutics* 2026; PMID 42753289; doi 10.1016/j.neurot.2026.e01066):

> "*Cribriform neuroepithelial tumor (CRINET)* is a provisional CNS WHO entity. It is a *SMARCB1*-altered, INI1-deficient tumor that shares molecular similarities with ATRT-TYR but lacks overt rhabdoid morphology and shows characteristic cribriform neuroepithelial architecture. Compared with classic ATRT, CRINET appears to be associated with significantly better long-term survival, making its distinction from ATRT clinically meaningful."

### 1.5 Provenance of the information (individual-patient vs aggregated)

**Entirely individual-patient derived, aggregated manually.** There is no EHR-linked cohort, no population registry entry, and no Orphanet epidemiology record. The evidence base is:
- one 10-patient international pathology-based case series with matched comparators (Johann 2017, PMID 27380723);
- a 3-case molecular series (Gessi M, Japp AS, Dreschmann V, et al. *J Neuropathol Exp Neurol* 2015;74(10):1012–1018; PMID 26352987; doi 10.1097/NEN.0000000000000239);
- single/double case reports (PMIDs 19915490, 21918902, 22239490, 23495723, 34151521, 35673730, 36884098) and incidental cases in genomic surveys (PMIDs 21717527, 24478045);
- one 2025 PRISMA systematic review pooling 18 published pediatric cases from 10 publications (Qadri et al., *OncoDaily Medical Journal*; doi 10.69690/ODMJ-018-0915-5372) — **note: this journal is not PubMed-indexed and its numbers conflict with the primary series on sex ratio; treat as low-tier evidence.**

---

## 2. Etiology

### 2.1 Disease causal factors

CRINET is a **genetic (somatic, two-hit) neoplasm**. The initiating and essentially sole recurrent driver is **biallelic inactivation of *SMARCB1***, producing complete loss of nuclear SMARCB1/INI1 protein in tumor cells — the defining diagnostic feature.

From Johann et al. 2017 (PMID 27380723), verbatim:

> "FISH and/or MLPA confirmed the presence of heterozygous SMARCB1 deletions (8/9 cases evaluable). In addition, truncating SMARCB1 mutations (c.367C > T, c.367C > T, c.492duplCCTT and c.986 + 1G > T) were identified, while two cases showed additional small SMARCB1 deletions on MLPA (delEx7,delEx7-Ex9). Furthermore, an exon 9 missense mutation (c.1142C > G) and an exon 6 duplication where encountered, both mutations also being present in the germline."

Copy-number analysis in the same cohort found "22q losses affecting the SMARCB1 region as the only recurrent alteration in CRINETs with a pattern very similar to that seen in ATRT-TYR tumors"; in 9/10 cases the first hit was a **large heterozygous 22q deletion**, and the single case without a 22q deletion instead carried a **homozygous truncating *SMARCB1* mutation**.

Independent confirmation:
- Hasselblatt 2009 (PMID 19915490): one of the two index cases had "a homozygous 4-bp duplication in exon 4 (492duplCCTT)."
- Arnold MA, Stallings-Archer K, Marlin E, et al. *Pediatr Dev Pathol* 2013;16(4):301–307 (PMID 23495723; doi 10.2350/12-12-1287-CR.1): "Genetic analysis of the tumor revealed deletion of 1 SMARCB1 allele, while the other contained an intronic point mutation predicted to disrupt splicing."
- Exception to the rule: Liu Y, Zhu K, Liu L, Tang HF. *Zhonghua Bing Li Xue Za Zhi* 2022 (PMID 35673730; doi 10.3760/cma.j.cn112151-20211104-00799) reported an 8-month-old with complete "INI1 expression absence" but **FISH showing no *SMARCB1* deletion** — i.e., protein loss without a detectable deletion, implying a sequence-level second mechanism.

The genome is otherwise remarkably quiet. Gessi et al. 2015 (PMID 26352987), verbatim:

> "Along with mutations and deletions of SMARCB1-INI1, molecular inversion profiling analysis revealed a stable genomic profile without significant large chromosomal changes. Focal alterations (gains) were observed in individual cases at chromosomes 4q12 (PDGFRA), 12q15 (MDM2), 7p15.1 (NPY), and 18q11.2 (CDH2). Genomic Identification of Significant Targets in Cancer analysis highlighted focal alterations, including gains at chromosomes 16q23.2 (MAF), 17q23 (AXIN2), and 8p12 (ADAM3A). No cases showed BRAF(V600E) or CTNNB1 mutations. These data indicate that CRINET present stable genetic features and lack alterations commonly identified in other pediatric brain tumors."

The first cytogenetic description (Dahlback HS, Brandal P, Gorunova L, et al. *Genes Chromosomes Cancer* 2011;50(10):788–799; PMID 21717527; doi 10.1002/gcc.20898) reported "a cribriform neuroepithelial tumor, a recently identified variant of atypical teratoid/rhabdoid tumor with a favorable prognosis, which showed loss of 1p33, 4q13.2, 10p12.31, 10q11.22, and 22q by aCGH."

### 2.2 Risk factors

**Genetic risk factors**
- **Germline *SMARCB1* pathogenic variants (RTPS1; OMIM 609322)** are the only established constitutional risk factor. In the Johann cohort, **2/10 CRINET patients carried the causative *SMARCB1* variant in the germline** (an exon 9 missense c.1142C>G "expected to result in disturbed splicing," and an exon 6 duplication), with documented family history of brain tumors and variable penetrance within one family.
- Per GeneReviews (Nemes K, Bens S, Bourdeaut F, et al., last update 12 May 2022): *SMARCB1* accounts for ~85–95% of RTPS; among newly diagnosed rhabdoid tumors generally, "25%-35% will have a disease-causing germline variant in SMARCB1"; "Penetrance of SMARCB1-related RTPS may be extremely high (>90% by age 5 years)"; inheritance is autosomal dominant with a 50% transmission risk; "The vast majority of individuals diagnosed with SMARCB1-related RTPS have the disorder as the result of a de novo germline disease-causing variant"; and "Germline mosaicism may account for up to half of the families with sibs affected by RTPS."
- The SIOPE Host Genome Working Group concurs: "Among newly diagnosed cases of MRT 25–35% carry a germline PV in *SMARCB1*" (Frühwald MC, et al. *Fam Cancer* 2021;20(4):305–316; PMID 33532948; doi 10.1007/s10689-021-00229-1).
- **Susceptibility loci / GWAS / modifier genes: none retrieved.** No GWAS exists for this entity (sample size makes one impossible).

**Environmental risk factors**
- **None identified.** No toxin, radiation, pollution, occupational, dietary, or parental exposure has been linked to CRINET in any retrieved source. Searches of the CRINET literature returned no environmental-etiology studies.
- The only demographic risk variables with any evidence are **very young age** (median 20 months) and possibly **sex** (conflicting — see §3.1, §9.3).

### 2.3 Protective factors

**No genetic or environmental protective factors have been reported for CRINET.** Nothing was retrievable on protective variants, gnomAD-level protective alleles, diet, or lifestyle. This is expected for a <30-case entity.

A mechanistically relevant observation from mouse genetics — not a human protective factor — is that **genetic inactivation of *Ezh2* blocks tumorigenesis driven by *Snf5* loss** (Wilson BG, Wang X, Shen X, et al. *Cancer Cell* 2010;18(4):316–328; PMID 20951942; doi 10.1016/j.ccr.2010.09.006): "using conditional mouse models, we show that inactivation of Ezh2 blocks tumor formation driven by Snf5 loss."

### 2.4 Gene–environment interactions

**No data.** No CTD, PheGenI, or GxE study addressing CRINET or *SMARCB1*-deficient CNS tumors and environmental co-factors was retrievable. The genomic quiescence documented by Gessi 2015 argues against a mutagen-driven component.

---

## 3. Phenotypes

### 3.1 Demographic phenotype

| Parameter | Value | Source |
|---|---|---|
| Median age at diagnosis | **20 months (range 10–129 months)** | Johann 2017, PMID 27380723 (n=10) |
| Median age (radiology review) | 1.7 years (range 0.8–10.8 years), "without a definite sex predilection" | AJNR 2023, PMID 36997287 |
| Mean age (pooled review) | 1.11 ± 0.45 years | Qadri 2025, doi 10.69690/ODMJ-018-0915-5372 (n=18) |
| NCI PDQ statement | "Like AT/RT, cribriform neuroepithelial tumor occurs in young children (median age, 1–2 years)." | NCI PDQ, Childhood AT/RT Treatment (Health Professional), updated 3 March 2025 |
| Sex | **6 boys : 4 girls** | Johann 2017 |
| Sex (conflicting) | "predominance of females (13, 72.2%)" | Qadri 2025 (low-tier source) |

**HPO:** onset is captured by HP:0003593 (Infantile onset) / HP:0011463 (Childhood onset) conceptually — *note: I did not individually verify those two HPO IDs in this session, so treat them as unconfirmed; all HPO IDs listed in §3.2 below were verified via EBI OLS4.*

### 3.2 Clinical phenotypes, with verified HPO terms

Presenting features reported across the primary case literature are those of an obstructing intraventricular mass in an infant. **Frequencies are not formally established**; the only pooled statement is that "Most patients presented with signs of raised intracranial pressure" (Qadri 2025).

| Phenotype | HPO term (verified via OLS4) | Type | Evidence / source |
|---|---|---|---|
| Increased intracranial pressure | **HP:0002516** | Clinical sign | "Most patients presented with signs of raised intracranial pressure" (Qadri 2025); "a 14-month-old male who presented with signs of increased intracranial pressure" (Arnold 2013, PMID 23495723) |
| Hydrocephalus (obstructive) | **HP:0000238** | Clinical sign / imaging | "MRI revealed a mixed signal fourth ventricular mass causing obstructive hydrocephalus" (Liu 2022, PMID 35673730) |
| Vomiting | **HP:0002013** | Symptom | Component of raised-ICP syndrome in infants; not individually enumerated per-case in retrieved CRINET reports — **frequency unknown** |
| Macrocephaly | **HP:0000256** | Physical manifestation | Expected consequence of infantile hydrocephalus; **not explicitly documented in retrieved CRINET case texts** |
| Papilledema | **HP:0001085** | Clinical sign | Component of raised ICP; **not explicitly documented per-case in retrieved CRINET texts** |
| Ataxia / gait disturbance, motor regression | **HP:0001251** | Clinical sign / behavioral change | "A 14-month-old boy had presented with gait imbalance and was crawling for the last 2 weeks" (Park JY, Kim E, Kim DW, Chang HW, Kim SP. *Neuropathology* 2012;32(3):308–313; PMID 22239490; doi 10.1111/j.1440-1789.2011.01293.x) |
| Abnormal eye movements (downward/forced downgaze, "setting sun" phenomenon) | **HP:0000639** (Nystagmus) is the nearest verified term; the specific sign reported was downgaze | Clinical sign | "An eight-month-old male presented with downward gaze and growth failure" (Liu 2022, PMID 35673730) |
| Failure to thrive / growth failure | **HP:0001508** | Laboratory/anthropometric | Liu 2022, PMID 35673730 |
| Lethargy | **HP:0001254** | Symptom | Component of raised-ICP syndrome; **not individually documented in retrieved CRINET texts** |

**Important curation caveat:** I found **no HPO disease-annotation record for CRINET**. The HPO terms above are *suggestions mapped from narrative case descriptions*, not curated annotations, and the only frequency datum retrievable is the qualitative "most patients" for raised ICP.

### 3.3 Phenotype characteristics

- **Age of onset:** infancy to early childhood; neonatal onset not reported; the oldest patient in the definitive series was 129 months (~10.8 years). Search snippets referenced an adult (22-year-old) INI1-deficient cribriform tumor, but **I could not retrieve a primary source for that case and therefore do not assert it.**
- **Severity:** severe at presentation (large mass, obstructive hydrocephalus requiring urgent neurosurgery) but **not severe in outcome** — see §11.
- **Progression:** acute-on-subacute mass effect before treatment; after resection ± chemotherapy the course is typically one of sustained remission. Hasselblatt 2009: both index patients achieved "complete remission longer than 5 years postoperatively." Johann 2017: "Except for one child, all patients are alive and well."
- **Frequency among affected individuals:** not quantifiable beyond the qualitative statements above.

### 3.4 Quality-of-life impact

**No disease-specific QoL instrument data exist** (no EQ-5D, SF-36, PROMIS, or PedsQL study of CRINET was retrievable). The only functional-outcome proxy is from the 2025 pooled review: **"77.8% were alive without any neurological deficit at last follow-up"** over a mean follow-up of 32.0 ± 33.7 months (Qadri 2025). Per-phenotype QoL mapping is not possible from the available evidence.

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene

**SMARCB1** — HGNC:11103; approved name "SWI/SNF related BAF chromatin remodeling complex subunit B1"; previous symbol *SNF5L1*; aliases *BAF47*, *Ini1*, *INI-1*, *Snr1*, *hSNFS*, *Sfh1p*, *RDT*, *PPP1R144*, *SNF5*; location 22q11.23; Ensembl ENSG00000099956 (GRCh38 chr22:23,786,931–23,838,009, + strand); Entrez 6598; OMIM \*601607; UniProt Q12824; RefSeq NM_003073.

No second causal gene has been implicated in CRINET. (In the related AT/RT spectrum, rare *SMARCA4*-driven cases exist; **no *SMARCA4*-driven CRINET was retrieved.**)

### 4.2 Pathogenic variants reported in CRINET

| Variant (HGVS as published) | Type | Zygosity/context | Source |
|---|---|---|---|
| Large heterozygous **22q deletion spanning *SMARCB1*** | Structural / CNV | First hit in **9/10** cases | Johann 2017, PMID 27380723 |
| **c.367C>T** (p.Gln123\*) ×2 independent cases | Nonsense / truncating | Second hit, somatic | Johann 2017 |
| **c.492duplCCTT** (p.Pro165Leufs\*6) | Frameshift duplication | Reported homozygous in the 2009 index case ("a homozygous 4-bp duplication in exon 4 (492duplCCTT)") | Hasselblatt 2009, PMID 19915490; Johann 2017 |
| **c.986+1G>T** | Canonical splice-donor | Second hit | Johann 2017 |
| **delEx7**, **delEx7–Ex9** | Small intragenic deletions (MLPA) | Additional second hits | Johann 2017 |
| **c.1142C>G** (exon 9 missense, "expected to result in disturbed splicing") | Missense/splice-affecting | **Germline** | Johann 2017 |
| **Exon 6 duplication** | Intragenic duplication | **Germline** | Johann 2017 |
| Intronic point mutation predicted to disrupt splicing (nomenclature not given in abstract) | Splice | Trans to a whole-allele deletion | Arnold 2013, PMID 23495723 |
| Protein loss **without** detectable *SMARCB1* deletion on FISH | — | Implies sequence-level biallelic event | Liu 2022, PMID 35673730 |

- **ACMG/AMP classification:** truncating/nonsense/frameshift/canonical-splice *SMARCB1* variants of this kind are conventionally pathogenic; **I did not retrieve individual ClinVar/VarSome classification records for these specific CRINET variants in this session**, so no per-variant ACMG call is asserted here.
- **Allele frequency in population databases:** these are tumor-driver loss-of-function alleles; **no gnomAD frequencies were retrieved.** Expect absence/extreme rarity.
- **Somatic vs germline:** predominantly **somatic two-hit**; **germline in 2/10 (20%) of the definitive CRINET series**, consistent with the 25–35% germline rate across rhabdoid tumors generally (GeneReviews; Frühwald 2021, PMID 33532948).
- **Functional consequence: loss of function** — complete loss of nuclear SMARCB1 protein by IHC in 10/10 CRINETs (Johann 2017).

### 4.3 Chromosomal abnormalities

- **Broad 22q loss** is the dominant and essentially the only recurrent large-scale change (Johann 2017), matching the ATRT-TYR pattern.
- **Otherwise genomically stable** — "a stable genomic profile without significant large chromosomal changes" (Gessi 2015, PMID 26352987), with scattered non-recurrent focal gains at 4q12 (*PDGFRA*), 12q15 (*MDM2*), 7p15.1 (*NPY*), 18q11.2 (*CDH2*), 16q23.2 (*MAF*), 17q23 (*AXIN2*), 8p12 (*ADAM3A*).
- One aCGH-characterized case showed additional losses of 1p33, 4q13.2, 10p12.31, 10q11.22 and 22q (Dahlback 2011, PMID 21717527).
- **Suggested DECIPHER/dbVar curation:** 22q11.23 deletion encompassing *SMARCB1*.

### 4.4 Epigenetic information (central to this entity)

CRINET is **epigenetically indistinguishable from the ATRT-TYR subgroup** by genome-wide DNA methylation. Johann 2017:

> "On unsupervised cluster analysis of Illumina Infinium Human Methylation 450k data, all 8 CRINET examined clustered with the AT/RT-TYR subgroup."

Methods, verbatim: "DNA methylation data were generated from FFPE tissue samples using 250 ng of DNA as input material… In total, 438 370 probes were kept for analysis. Unsupervised hierarchical clustering of the samples was performed using the 5000 most variably methylated probes across the dataset."

The ATRT-TYR reference subgroup derives from Johann PD, Erkek S, Zapatka M, et al. "Atypical Teratoid/Rhabdoid Tumors Are Comprised of Three Epigenetic Subgroups with Distinct Enhancer Landscapes." *Cancer Cell* 2016;29(3):379–393 (PMID 26923874; doi 10.1016/j.ccell.2016.02.001), which analyzed 192 ATRTs and found three subgroups that are "epigenetically distinct but genetically similar." Consensus nomenclature (ATRT-TYR, ATRT-SHH, ATRT-MYC) was fixed by an international working group (Ho B, Johann PD, Grabovska Y, et al. *Neuro-Oncology* 2020;22(5):613–624; PMID 31889194; doi 10.1093/neuonc/noz235).

The ATRT-TYR subgroup is characterized by overexpression of **melanosomal genes (*TYR*, *DCT*, *MITF*)**, predominantly infratentorial location, very young age, and broad 22q loss — characteristics reproduced by CRINET at the level of the methylome and the tyrosinase immunophenotype. *(ATRT-TYR descriptive percentages such as "~77% infratentorial," "monosomy 22 in ~80%," and "5-year OS ~48%" appeared in search-result summaries of the Cancer Cell paper; the full text was paywalled (HTTP 403) and I could not verify those specific figures against the primary source, so they are flagged as unverified.)*

### 4.5 Modifier genes

**None identified.** Johann et al. explicitly leave this open: the authors could not exclude "point mutations of genes putatively modifying the detrimental effects of SMARCB1-deficiency," and hypothesize that "the type of SMARCB1 mutation may determine tumor phenotype and prognosis," since genomic profiles are otherwise identical between CRINET and ATRT-TYR.

---

## 5. Environmental Information

- **Environmental factors:** none identified. No CTD/TOXNET/EPA-type association with CRINET or *SMARCB1*-deficient CNS tumors was retrievable.
- **Lifestyle factors:** not applicable — the patients are infants and toddlers; no parental-lifestyle association has been reported.
- **Infectious agents:** none. CRINET is not an infection-associated tumor; no pathogen has been implicated in any retrieved source.

This section is **genuinely empty rather than merely unsearched**: the tumor's near-diploid, mutationally silent genome (Gessi 2015) is itself evidence against a mutagenic environmental driver.

---

## 6. Mechanism / Pathophysiology

### 6.1 Ordered causal chain (initiating lesion → clinical manifestation)

1. **A first-hit *SMARCB1* lesion arises** — in ~90% of CRINETs a **large heterozygous deletion of chromosome 22q spanning *SMARCB1***, either somatically or (in ~20% of cases) as a constitutional/germline event — **which leads to** monoallelic *SMARCB1* loss in a susceptible neuroepithelial progenitor. *(Demonstrated: FISH/MLPA/CNV, Johann 2017.)*
2. **A second hit inactivates the remaining allele** — truncating (c.367C>T), frameshift (c.492dupCCTT), canonical-splice (c.986+1G>T), small intragenic deletion (delEx7, delEx7–9), or a splice-disrupting missense/duplication — **which results in** complete biallelic *SMARCB1* inactivation. *(Demonstrated: sequencing + MLPA, Johann 2017; Arnold 2013.)*
3. **Biallelic inactivation leads to total loss of nuclear SMARCB1/INI1 protein** in tumor cells (10/10 CRINETs by IHC) — the diagnostic read-out. *(Demonstrated.)*
4. **SMARCB1 loss destabilizes and mis-targets the SWI/SNF (BAF) chromatin-remodeling complex**, **which results in** collapse of SWI/SNF occupancy at *typical* enhancers — especially differentiation enhancers — while occupancy at *super-enhancers* is preserved. Wang X, Lee RS, Alver BH, et al. *Nat Genet* 2017;49(2):289–295 (PMID 27941797; doi 10.1038/ng.3746), verbatim: "We show that SMARCB1 is required for the integrity of SWI/SNF complexes and that its loss alters enhancer targeting-markedly impairing SWI/SNF binding to typical enhancers, particularly those required for differentiation, while maintaining SWI/SNF binding at super-enhancers." *(Demonstrated in rhabdoid tumor models — extrapolated to CRINET, which has not been studied directly at this level.)*
5. **Branch A — differentiation arrest and super-enhancer addiction:** the retained super-enhancers "are essential for rhabdoid tumor survival, including some that are shared by all subtypes, such as *SPRY1*, and other lineage-specific super-enhancers, such as *SOX2* in brain-derived rhabdoid tumors" (Wang 2017) — **which leads to** a self-sustaining undifferentiated progenitor state. *(Demonstrated in rhabdoid models; inferred for CRINET.)*
6. **Branch B — Polycomb de-repression:** SNF5/SMARCB1 loss **leads to** elevated *EZH2* expression and broad H3K27-trimethylation/repression of Polycomb targets. Wilson 2010 (PMID 20951942), verbatim: "loss of the SNF5 tumor suppressor leads to elevated expression of the Polycomb gene EZH2 and that Polycomb targets are broadly H3K27-trimethylated and repressed in SNF5-deficient fibroblasts and cancers… antagonism between SNF5 and EZH2 in the regulation of stem cell-associated programs… Snf5 loss activates those programs." This **results in** silencing of tumor-suppressive loci (notably the *CDKN2A*/p16–RB axis) and activation of stem-cell programs. *(Demonstrated in mouse/fibroblast models; causally validated by the Ezh2-knockout rescue.)*
7. **Branch C — convergent pathway dysregulation:** SMARCB1/INI1 interacts with "key proteins in various pathways related to tumor proliferation and progression: the p16-RB pathway, WNT signaling pathway, sonic hedgehog signaling pathway and Polycomb pathway" (Kohashi K, Oda Y. *Cancer Sci* 2017;108(4):547–552; PMID 28109176; doi 10.1111/cas.13173). Of note, in CRINET specifically, **canonical WNT activation via *CTNNB1* mutation was excluded** ("No cases showed BRAF(V600E) or CTNNB1 mutations," Gessi 2015) — a branch that is *closed* in this entity, although one case showed β-catenin immunopositivity (Liu 2022).
8. **Branch D — lineage/epigenetic context sets the subgroup:** within the ATRT-TYR/CRINET methylation class, an **MITF-driven melanosomal transcriptional program** is active, **which results in** expression of tyrosinase and DCT — manifest clinically as the **tyrosinase-positive immunophenotype present in 10/10 CRINETs** (Johann 2017) versus 1/10 each in ATRT-SHH and ATRT-MYC. *(Demonstrated at the IHC level in CRINET; the MITF-enhancer mechanism is demonstrated in ATRT, inferred for CRINET.)*
9. **The transformed progenitor adopts an epithelial-like cribriform architecture** rather than a rhabdoid one — strands, ribbons and trabeculae with **EMA-positive luminal surfaces**, **abundant basal lamina**, short rough ER and distinct intercellular junctions on electron microscopy — **which leads to** the defining histomorphology. Arnold 2013 (PMID 23495723): "Electron microscopy showed epithelial characteristics, including abundant basal lamina." Park 2012 (PMID 22239490): "the tumor cells were neuroepithelial cells that contained short linear rough endoplasmic reticula and distinct intercellular junctions." **Why the same genotype/methylome yields cribriform rather than rhabdoid morphology is unexplained — this step is the key unresolved inference in the chain.**
10. **Proliferation (median Ki-67 29%, range 15–35%) produces a bulky intra-/para-ventricular mass**, **which leads to** obstruction of CSF pathways → **obstructive hydrocephalus** → **raised intracranial pressure** → vomiting, gaze palsy, gait failure, lethargy, growth failure. *(Demonstrated clinically: Liu 2022; Arnold 2013; Park 2012.)*
11. **Terminal branch (prognostic divergence):** despite steps 1–8 being shared with ATRT-TYR, CRINET follows a far more favorable clinical trajectory (mean OS 125 vs 53 months). **The mechanism of this divergence is unknown.** Johann 2017, verbatim: "Molecular alterations responsible for the relatively favorable outcome of CRINET as compared to AT/RT remain to be determined." The authors offer two unproven hypotheses: that "the type of SMARCB1 mutation may determine tumor phenotype and prognosis," and an analogy to "desmoplastic medulloblastomas, which are also genetically and epigenetically indistinguishable from classic medulloblastomas of the SHH subtype, but still show a difference in outcome."

### 6.2 Component detail against the template checklist

- **Molecular pathways:** ATP-dependent chromatin remodeling (SWI/SNF/BAF); Polycomb repressive complex 2 / EZH2–H3K27me3; p16^INK4a^–RB; MITF-driven melanogenesis/melanosomal program; SHH and WNT interactions reported for SMARCB1 broadly but **WNT activation via *CTNNB1* is excluded in CRINET**. No KEGG/Reactome pathway curation specific to CRINET exists.
- **Cellular processes:** differentiation arrest of neuroepithelial progenitors; cell-cycle de-repression; stem-cell program activation; **not** genomic instability (the genome is stable).
- **Protein dysfunction:** pure **loss of function** of SMARCB1 (a core, non-catalytic BAF subunit). Not misfolding, not aggregation, not dominant-negative. Note that in other tumor types SMARCB1 IHC can show "three patterns: complete loss, mosaic expression and reduced expression" (Kohashi 2017) — **CRINET is defined by complete loss.**
- **Metabolic changes:** none reported. No metabolomics or lipidomics study of CRINET exists.
- **Immune system involvement:** none reported for CRINET.
- **Tissue damage mechanisms:** mass effect, CSF-flow obstruction and raised ICP — i.e., mechanical/hydrodynamic rather than oxidative, ischemic, fibrotic or inflammatory.
- **Biochemical abnormalities:** tyrosinase expression is an aberrant lineage marker, not a functional enzymopathy; no enzyme deficiency, receptor or ion-channel defect is implicated.
- **Molecular profiling:** **Transcriptomics, proteomics, metabolomics, lipidomics, single-cell, spatial transcriptomics, multi-omics integration, and CRISPR/RNAi functional screens specific to CRINET: none available.** The only CRINET-containing public omics resources I could identify are DNA-methylation/CNV based. A GEO query for "cribriform neuroepithelial OR CRINET" (db=gds) returns **GSE215240** ("Multiomic neuropathology improves diagnostic accuracy in pediatric neuro-oncology"; *Homo sapiens*; 1,124 samples; platforms GPL21145/GPL13534; submitted 2023-01-30) and **GSE27671** ("Genomic Aberrations in Paediatric Gliomas and Embryonal Tumours"; 13 samples; GPL10123; submitted 2011-07-01 — the Dahlback aCGH series containing the first cytogenetically characterized CRINET).

### 6.3 Suggested ontology terms for mechanism

- **GO biological process:** GO:0006338 chromatin remodeling (verified via OLS4)
- **GO cellular component:** GO:0070603 SWI/SNF superfamily-type complex; GO:0071565 nBAF complex (both verified via OLS4)
- **CL cell types:** CL:0000710 *neurecto-epithelial cell* (broad synonym "neuroepithelial cell"); CL:0000047 neural stem cell (both verified via OLS4). *The actual cell of origin of CRINET is unknown; these are inferential.*

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

- **Primary organ:** brain — specifically the **ventricular system and periventricular parenchyma**. Body system: **central nervous system**.
- Location distribution in the definitive cohort (Johann 2017), verbatim: *"CRINETs were either located supratentorially [midline in the vicinity of the third ventricle (4/10), near the lateral ventricles (2/10)], or infratentorially in the posterior fossa (4/10 cases)."*
- Pooled review (Qadri 2025, low-tier): all 18 lesions intraventricular; **fourth ventricle in 8 (44%)**.
- AJNR 2023: "These tumors occur in intraventricular or periventricular locations across lateral, third, and fourth ventricles without clear regional preference."
- **Secondary organ involvement:** obstructive hydrocephalus affects the entire ventricular system and, via raised ICP, global brain function. **CSF dissemination / leptomeningeal spread in CRINET: not documented in any source I retrieved** — searches returned only AT/RT and unrelated-tumor dissemination data, which I deliberately exclude. This is a genuine evidence gap, not a negative finding.
- **No extracranial organ involvement has been reported.**

### 7.2 UBERON terms (all verified via OLS4)

| Structure | UBERON |
|---|---|
| Lateral ventricle (label: telencephalic ventricle) | **UBERON:0002285** |
| Third ventricle | **UBERON:0002286** |
| Fourth ventricle | **UBERON:0002422** |
| Posterior cranial fossa | **UBERON:0008788** |
| Choroid plexus (differential-diagnostic structure; see below) | **UBERON:0001886** |

### 7.3 Tissue and cell level

- **Tissue type:** primitive **neuroepithelium** with epithelial differentiation features (basal lamina, intercellular junctions, EMA+ luminal surfaces) — an embryonal neuroepithelial neoplasm, not glial, not meningothelial.
- **Cell populations (inferred, CL):** CL:0000710 neurecto-epithelial cell; CL:0000047 neural stem cell. The tumor's periventricular origin and the frequent initial clinical impression of a choroid plexus tumor (see §10.5) raise — but do not establish — a tela choroidea / ventricular-zone progenitor origin.
- **Rhabdoid cells are characteristically ABSENT** — "Rhabdoid cells were absent" (Arnold 2013); "The typical rhabdoid feature of tumor cells was absent" (Park 2012).

### 7.4 Subcellular level

- **Nucleus (GO:0005634)** — the operative compartment: loss of *nuclear* SMARCB1 staining is the diagnostic criterion; SWI/SNF and PRC2 act on chromatin.
- **Chromatin / SWI/SNF complex:** GO:0070603, GO:0071565 (verified).
- Ultrastructurally relevant compartments: **rough endoplasmic reticulum** ("short linear rough endoplasmic reticula," Park 2012) and **basal lamina / cell junctions** (Arnold 2013).

### 7.5 Localization and lateralization

Midline and periventricular. Lesions near the third/fourth ventricle are **midline**; lateral-ventricle lesions are **unilateral** in the reported cases (e.g., "a large solid and cystic mass in the lateral ventricle," Arnold 2013). **No systematic lateralization analysis exists.**

---

## 8. Temporal Development

### 8.1 Onset

- **Typical age:** infancy/toddlerhood — **median 20 months, range 10–129 months** (Johann 2017); NCI PDQ: "median age, 1–2 years."
- **Pattern:** subacute, over weeks. Park 2012's patient had symptoms "for the last 2 weeks"; Liu 2022's presented with established obstructive hydrocephalus. Presentation is typically precipitated by CSF obstruction rather than by slow neurological decline.
- Congenital/neonatal presentation: **not reported** in retrieved sources.

### 8.2 Progression

- **Staging system:** **none exists** for CRINET. It is a provisional CNS5 type **with no assigned WHO grade** (AJNR 2023, PMID 36997287), no ICD-O morphology code retrieved, and no AJCC/ Chang-type staging.
- **Progression rate:** following resection ± chemotherapy, the course is dominated by durable remission. Hasselblatt 2009: both patients achieved "complete remission longer than 5 years postoperatively." Johann 2017: **9/10 alive in complete remission**; the single death was "from respiratory failure before therapy initiation" — i.e., a peri-diagnostic death, not disease progression.
- **Course pattern:** effectively **monophasic/treated-remission** rather than relapsing-remitting or progressive. **Relapse rate in CRINET is not established**; no retrieved CRINET-specific source reports recurrence rates. (Published relapse statistics circulating in search results pertain to AT/RT and are excluded here.)
- **Duration:** not a chronic lifelong disease in survivors; survivorship issues (post-treatment neurocognitive sequelae in infants treated with chemotherapy ± radiotherapy) are expected but **not studied in CRINET**.

### 8.3 Patterns

- **Remission:** treatment-induced, following gross-total or near-total resection plus (in half of pooled cases) chemotherapy. Mete EB, Eray HA, Orhan O, et al. (*Childs Nerv Syst* 2023;39(5):1123–1129; PMID 36884098; doi 10.1007/s00381-023-05897-1) achieved "Complete resection… without complications" in a 20-month-old using a transcallosal approach with endoscopic second-look. Spontaneous remission: not reported.
- **Critical period for intervention:** the window between symptomatic hydrocephalus and definitive resection. The one death in the definitive series occurred **before therapy could be started**, underscoring that the dominant early risk is mechanical (raised ICP), not oncological.
- **Critical period for predisposition surveillance:** birth to 5 years, when RTPS1 penetrance is >90% (GeneReviews) — see §13.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

- **Prevalence and incidence: not established.** There is **no Orphanet entry, no SEER category, no national-registry code, and no GBD estimate** for CRINET that I could retrieve. MONDO places it in the `rare`/`inferred_rare` subsets.
- **Best available denominator:** a PRISMA systematic review of PubMed and Google Scholar covering **2000–2025 identified only 10 publications reporting 18 patients** (Qadri HM, Najeeb ZU, Hassan SH, Bashir A. *OncoDaily Medical Journal*, 19 Sep 2025; doi 10.69690/ODMJ-018-0915-5372). The definitive pathology series assembled **10 cases from an international multi-institution network spanning Germany, Canada, USA, Korea, Norway, Czechia, Hungary and Russia** (Johann 2017). My own PubMed phrase search for "cribriform neuroepithelial" returned **20 records total**, most of which are reviews rather than new cases.
- **Context:** AT/RT itself is rare — per NCI PDQ, "approximately 10% of children aged 3 years or younger at diagnosis with brain tumors had AT/RTs" in two prospective North American studies. CRINET is a far smaller fraction of SMARCB1-deficient CNS tumors than AT/RT.

### 9.2 Genetic etiology parameters

CRINET as a *tumor* is usually sporadic (somatic two-hit). The heritable dimension is **RTPS1**:

| Parameter | Value | Source |
|---|---|---|
| Inheritance (RTPS) | **Autosomal dominant**; "Each child of an individual with a germline SMARCB1 or SMARCA4 disease-causing variant has a 50% chance of inheriting this variant." | GeneReviews (Nemes et al., updated 12 May 2022) |
| Germline rate in CRINET specifically | **2/10 (20%)** | Johann 2017, PMID 27380723 |
| Germline rate across rhabdoid tumors | **25–35%** | GeneReviews; Frühwald 2021, PMID 33532948 |
| Penetrance | "Penetrance of SMARCB1-related RTPS may be extremely high (>90% by age 5 years)." | GeneReviews |
| Expressivity | **Variable** — Johann 2017 documented one family in which some carriers died of brain tumors while others carrying the identical variant remained unaffected | Johann 2017 |
| De novo rate | "The vast majority of individuals diagnosed with SMARCB1-related RTPS have the disorder as the result of a de novo germline disease-causing variant." | GeneReviews |
| Germline mosaicism | "Germline mosaicism may account for up to half of the families with sibs affected by RTPS." | GeneReviews |
| Genetic anticipation | **Not applicable** — not a repeat-expansion disorder | — |
| Founder effects | **None reported** | — |
| Consanguinity | **No role reported** | — |
| Carrier frequency | **Not established**; no gnomAD-based estimate retrieved | — |
| Gene distribution within RTPS | *SMARCB1* ~85–95%; *SMARCA4* ~5–15% | GeneReviews |

Note the clinically important contrast: *SMARCA4*-related RTPS2 shows **incomplete penetrance** — "most individuals with SMARCA4-related RTPS have inherited the disease-causing variant from an unaffected, healthy parent" (GeneReviews) — whereas *SMARCB1*-related RTPS1 is near-fully penetrant in early childhood.

### 9.3 Population demographics

- **Ethnic/ancestry predilection: none identified.** Reported cases span German, North American, Canadian, Korean, Norwegian, Czech, Hungarian, Russian, Turkish and Chinese centres — consistent with a sporadic, globally distributed entity.
- **Geographic distribution:** no endemic clustering; no geographic clustering of specific *SMARCB1* variants reported.
- **Sex ratio: conflicting.** The definitive series reports **6 boys : 4 girls** (M:F 1.5:1; Johann 2017); the AJNR review reports "no definite sex predilection"; the 2025 pooled review reports **72.2% female**. Given the sample sizes (n=10 vs n=18 with overlapping cases) and the journal-quality gap, **no reliable sex ratio can be stated** — I would record this field as "indeterminate, conflicting evidence."
- **Age distribution:** heavily concentrated at 10–30 months; the single outlier in the definitive series was 129 months.

---

## 10. Diagnostics

### 10.1 Histopathology — the diagnostic core

The diagnosis rests on the **combination** of cribriform architecture + absence of rhabdoid cells + nuclear SMARCB1/INI1 loss.

- Johann 2017: "all CRINETs were characterized by the presence of cribriform strands and ribbons" with "small lumina… but rhabdoid tumor cells… were absent."
- Park 2012 (PMID 22239490): "the tumor was composed of relatively small undifferentiated neuroepithelial cells arranged in a cribriform pattern and intervening solid sheets with true rosettes."
- Arnold 2013 (PMID 23495723): "Tumor cells were small, primitive appearing, and arranged in cribriform and trabecular patterns with interspersed solid cellular areas. Rhabdoid cells were absent."
- Liu 2022 (PMID 35673730): tumor cells in "cribriform, trabecular, and papillary patterns" with "true rosette-like structures."
- AJNR 2023: "The key histologic features… are the presence of cribriform strands, ribbons, and nuclei with dense chromatin."
- Qadri 2025: "neuroepithelial cells were arranged in cribriform strands and ribbons in 16 (88.8%)."

### 10.2 Immunohistochemistry

| Marker | Finding | Source |
|---|---|---|
| **SMARCB1/INI1 (nuclear)** | **Lost in 100%** — "All CRINETs showed loss of tumoral SMARCB1 protein expression" (10/10) | Johann 2017 |
| **Tyrosinase** | **Positive in 10/10 CRINETs** (vs 9/10 ATRT-TYR, but only 1/10 each in ATRT-SHH and ATRT-MYC) | Johann 2017 |
| **EMA** | Positive along luminal/epithelial surfaces — "strong epithelial membrane antigen (EMA) immunoreactivity along luminal surfaces" (Arnold 2013); "distinct expression of epithelial membrane antigen (EMA) along the luminal borders of the tubules or glands" (Park 2012) | Arnold 2013; Park 2012; Hasselblatt 2009 |
| **Vimentin, MAP2C, synaptophysin** | Reported positive | AJNR 2023, PMID 36997287 |
| **Cytokeratin, β-catenin** | Positive in at least one reported case | Liu 2022, PMID 35673730 |
| **Ki-67/MIB-1** | **Median 29% (range 15–35%)** | Johann 2017; "Ki-67/MIB positivity in 11 (61.1%) cases" (Qadri 2025) |

### 10.3 Electron microscopy

Supportive but not required: "Electron microscopy showed epithelial characteristics, including abundant basal lamina" (Arnold 2013); "short linear rough endoplasmic reticula and distinct intercellular junctions" (Park 2012). Ibrahim GM, Huang A, Halliday W, et al. (*Acta Neuropathol* 2011;122(4):511–514; PMID 21918902; doi 10.1007/s00401-011-0872-5) contributed "novel clinicopathological, ultrastructural and cytogenetic findings" (letter format; no abstract available).

### 10.4 Imaging

- **AJNR 2023, verbatim:** "Imaging typically reveals a large mass with T1-hypointensity, T2-hyperintensity, heterogeneous enhancement, and diffusion restriction."
- Pooled: "Magnetic Resonance Imaging (MRI) was suggestive of heterogeneous enhancement in 14 (83.3%)" (Qadri 2025).
- Case-level: "a large, complex solid and cystic mass with dimensions of 55 × 55 × 50 mm in the vicinity of the third ventricle" (Park 2012); "a large solid and cystic mass in the lateral ventricle" (Arnold 2013); "a mixed signal fourth ventricular mass causing obstructive hydrocephalus" (Liu 2022).
- Suggested RadLex-type descriptors: intraventricular mass; cystic-solid; heterogeneous post-gadolinium enhancement; restricted diffusion; obstructive hydrocephalus.

### 10.5 Differential diagnosis

| Entity | Distinguishing features |
|---|---|
| **Choroid plexus papilloma / carcinoma** | **The most important mimic.** Johann 2017, verbatim: *"Based on neuroradiological findings and clinical features, the possibility of a choroid plexus tumor had been considered initially in the majority of patients (6/10)."* CPC retains SMARCB1; CPC has a complex, aneuploid genome. Ruland V, Hartung S, Kordes U, et al. (*Genes Chromosomes Cancer* 2014;53(5):373–380; PMID 24478045; doi 10.1002/gcc.22148) showed MIP SNP arrays resolve the problem: "The MIP SNP array profiles also contributed to the diagnosis of two difficult SMARCB1-negative tumors as choroid plexus carcinoma and cribriform neuroepithelial tumor (CRINET), respectively." |
| **AT/RT (esp. ATRT-TYR)** | Shares SMARCB1 loss, 22q deletion, tyrosinase positivity and methylation class; **distinguished by the presence of rhabdoid cells and by cribriform architecture in CRINET**. "Cribriform histology distinguishes CRINET from AT/RT. Prognosis is more favorable than AT/RT." (Eaton et al. 2026, PMID 42753289). The distinction was contested enough to generate a dedicated correspondence exchange: Dunham C, Yip S. "Cribriform neuroepithelial tumor or atypical teratoid/rhabdoid tumor?" *J Neurosurg Pediatr* 2013 (PMID 23394355; doi 10.3171/2012.3.PEDS12168), with reply (PMID 23667911). |
| **ETMR, ependymoma, medulloblastoma, CNS HGNET-BCOR, supratentorial PNET** | Covered in the posterior-fossa differential by Dunham C. *Childs Nerv Syst* 2015;31(10):1729–1737 (PMID 26351226; doi 10.1007/s00381-015-2735-1) and in the embryonal-tumor workup guide by Cotter JA, Judkins AR. *Pediatr Dev Pathol* 2022 (PMID 35168419; doi 10.1177/10935266211018554), which provides "a practical approach to workup and development of an integrated diagnosis for CNS embryonal tumors." |
| **Other SMARCB1-deficient neoplasms** (renal medullary carcinoma, epithelioid sarcoma, poorly differentiated chordoma, schwannomatosis-associated tumors) | Site and morphology; reviewed by Pawel BR. *Pediatr Dev Pathol* 2018 (PMID 29280680; doi 10.1177/1093526617749671) and Agaimy A. *Adv Anat Pathol* 2014 (PMID 25299309; doi 10.1097/PAP.0000000000000038). |
| **Diagnostic pitfall report** | Tauziède-Espariat A, Guerrini-Rousseau L, Puget S, et al. "A novel case of cribriform neuroepithelial tumor: A potential diagnostic pitfall in the ventricular system." *Pediatr Blood Cancer* 2021;68(9):e29037 (PMID 34151521; doi 10.1002/pbc.29037) — brief report; **no abstract is available in PubMed or Europe PMC and the full text is paywalled, so I cannot summarize its content.** |

### 10.6 Genetic and molecular testing

**Recommended tumor workup (synthesized from the retrieved primary literature):**
1. **SMARCB1/INI1 immunohistochemistry** — first-line, defining.
2. **Tyrosinase IHC** — supports the ATRT-TYR/CRINET lineage.
3. **FISH and/or MLPA for *SMARCB1*** (22q11.23) — detects the large heterozygous deletion and small intragenic deletions (delEx7, delEx7–9). Used in Johann 2017 and Gessi 2015.
4. **Sanger/NGS sequencing of *SMARCB1*** — detects the second-hit truncating, splice-site and missense variants.
5. **Genome-wide copy-number profiling** (MIP SNP array or methylation-array-derived CNV) — confirms the otherwise quiet genome and resolves the choroid-plexus-carcinoma differential (Ruland 2014; Gessi 2015).
6. **Genome-wide DNA methylation classification (Illumina 450k/EPIC)** — assigns the case to the ATRT-TYR methylation class; this is the modern integrative-diagnosis step (Johann 2017; see also the large multiomic pediatric neuropathology resource GSE215240).

**Germline testing (mandatory, not optional):** SIOPE Host Genome Working Group recommendation, verbatim — **"Evaluate all patients with a signal tumor (i.e. Rhabdoid Tumor or SCCOHT) for a germline mutation regardless of age"** (Frühwald 2021, PMID 33532948). For *SMARCB1*, testing must detect "nonsense, frameshift, whole and partial gene deletions," and the group recommends **NGS with copy-number analysis plus sequencing of intron 1**. First-degree relatives should be offered testing; "Siblings of children with RTPS should be offered genetic screening."

**Modality-by-modality utility for this disease:**

| Modality | Utility |
|---|---|
| Single-gene *SMARCB1* sequencing + CNV (MLPA) | **High — the core test**, tumor and germline |
| FISH (22q11.23 / *SMARCB1*) | **High** — detects the dominant first hit |
| Gene panel | Useful if it includes *SMARCB1* and *SMARCA4* with CNV calling |
| Chromosomal microarray / SNP array | **High** — 22q loss; genomic-stability signature; CPC differential |
| **DNA methylation array (epigenomics)** | **High and increasingly standard** — assigns ATRT-TYR class |
| WES | Adequate for the point mutations; **inferior for the large deletion and for intron 1** |
| WGS | Would capture both hit types; no CRINET-specific WGS literature retrieved |
| Karyotyping | Historical; detected the 22q loss in the first cytogenetic case (Dahlback 2011) |
| RNA-seq / proteomics / metabolomics / liquid biopsy | **No CRINET-specific diagnostic role established; no data** |
| Mitochondrial DNA testing, repeat-expansion testing | **Not applicable** |

### 10.7 Laboratory tests, biomarkers, functional tests, electrophysiology

- **Blood/urine/CSF laboratory biomarkers: none.** No circulating or CSF biomarker exists for CRINET. There is no FDA-qualified biomarker.
- **Functional tests (pulmonary, cardiac):** not applicable.
- **Electrophysiology (EEG/EMG/NCS):** no established role; not reported in any retrieved CRINET case.
- The only "biomarkers" in practical use are **tissue-based**: SMARCB1 loss, tyrosinase positivity, Ki-67, and the ATRT-TYR methylation class.

### 10.8 Screening of asymptomatic individuals

Applies only to germline *SMARCB1* carriers — see §13.2.

---

## 11. Outcome / Prognosis

### 11.1 Survival

The pivotal comparison (Johann 2017, PMID 27380723 / PMC8028967):

| Group | n | Mean overall survival | 95% CI |
|---|---|---|---|
| **CRINET** | 10 | **125 months** | 100–151 |
| ATRT-TYR (matched clustering cohort) | 10 | 37 months | 18–56 |
| **ATRT-TYR (larger comparator cohort)** | 27 | **53 months** | 33–74 |
| ATRT-SHH | 10 | 16 months | 8–25 |
| ATRT-MYC | 10 | 13 months | 5–22 |

Log-rank **P < 0.05** for CRINET vs ATRT-TYR. Verbatim from the abstract: *"Except for one child, all patients are alive and well with a mean overall survival of 125 months (95% confidence interval 100-151 months)."* Survival analysis used Kaplan–Meier estimation and the log-rank test in IBM SPSS 23.

Supporting data points:
- Hasselblatt 2009: both index patients responded to conventional chemotherapy with "complete remission longer than 5 years postoperatively."
- Qadri 2025 (pooled, n=18): **"77.8% were alive without any neurological deficit at last follow-up"**, mean follow-up 32.0 ± 33.7 months; authors conclude PICRINET shows "better three-year survival compared to atypical teratoid/rhabdoid tumors when treated with surgery and adjuvant therapy."
- NCI PDQ (updated 3 March 2025): **"The outcome of patients with cribriform neuroepithelial tumor is more favorable than the outcome of patients with AT/RT TYR."** For reference, PDQ cites "In the prospective European Rhabdoid Registry (EU-RHAB) series, patients aged 1 year and older with AT/RT TYR demonstrated a 5-year OS rate of 71%" — so the CRINET advantage is over a comparator that is itself the best-prognosis AT/RT subgroup.

**5- and 10-year survival rates are not published as such for CRINET** (the cohorts are too small); the mean-OS estimate of 125 months is the best available figure.

### 11.2 Mortality

- **Disease-specific mortality in the definitive series: 0/10 from tumor progression.** The one death was "from respiratory failure before therapy initiation" (Johann 2017) — a peri-diagnostic event attributable to mass effect/raised ICP rather than to treatment failure.
- No population mortality data exist (no registry coding).

### 11.3 Morbidity, disability, quality of life

- **"77.8% were alive without any neurological deficit at last follow-up"** (Qadri 2025) is the only functional-outcome statistic retrievable.
- **No ICF-coded disability data, no EQ-5D/SF-36/PROMIS data, no neurocognitive outcome study** of CRINET survivors exists. Given that patients are infants treated with multi-agent and sometimes high-dose chemotherapy ± radiotherapy (including 54 Gy conventional and proton radiation in the Johann cohort), **late neurocognitive and endocrine sequelae are expected but entirely unstudied in this entity** — a notable gap for a knowledge-base entry.

### 11.4 Complications

Documented: obstructive hydrocephalus and raised ICP (the proximate cause of the single death). Surgical complications: the Mete 2023 case achieved "Complete resection… without complications." **Recurrence/CSF dissemination rates: not established in CRINET.**

### 11.5 Prognostic factors and prognostic biomarkers

- **The single established prognostic discriminator is the diagnosis itself** — cribriform (non-rhabdoid) morphology within the SMARCB1-deficient/ATRT-TYR molecular class predicts markedly better survival. This is precisely why the WHO retained CRINET as a separate provisional type: "making its distinction from ATRT clinically meaningful" (Eaton 2026, PMID 42753289).
- **No within-CRINET prognostic factor has been validated** (extent of resection, age, germline status, Ki-67). Johann et al. hypothesize that "the type of SMARCB1 mutation may determine tumor phenotype and prognosis" but did not demonstrate it.
- Extrapolating from AT/RT, germline *SMARCB1* status is adverse — PDQ notes "Children with germline alterations in *SMARCB1* presented at an earlier age than did sporadic cases (median age, approximately 5 months vs. 18 months)" — **but this has not been shown to apply to CRINET.**
- **No prognostic molecular biomarker** (transcriptomic, proteomic, circulating) exists for CRINET.

---

## 12. Treatment

**There is no CRINET-specific clinical trial, no CRINET treatment guideline, and no randomized evidence.** Treatment has been extrapolated from malignant-brain-tumor and AT/RT protocols, applied heterogeneously. Johann et al. note that CRINET "responds well to chemotherapy protocols commonly employed for the treatment of malignant brain tumors and ATRT," while acknowledging the protocols were heterogeneous across institutions.

### 12.1 Surgery (primary modality)

- **Maximal safe resection** is the cornerstone. NCIT suggestion: use a surgical-resection/neurosurgical-procedure NCIT term — *I verified only NCIT:C15313 (Radiation Therapy) among procedure terms this session; I have not verified a specific resection NCIT code and therefore do not assert one.*
- Technique example: **transcallosal resection with endoscopic second-look**, in a 20-month-old male — "A twenty-month-old male underwent transcallosal resection and endoscopic second-look surgery… Complete resection was achieved without complications" (Mete 2023, PMID 36884098; doi 10.1007/s00381-023-05897-1). The authors emphasize "long courses of follow-up periods are required for establishing treatment modules."
- CSF diversion for obstructive hydrocephalus is implied by the presentations but not separately quantified.

### 12.2 Chemotherapy

Protocols actually used in the ten-patient CRINET cohort (Johann 2017): **CPT-SIOP-2000** (etoposide, cyclophosphamide, vincristine), **COG-99703** with high-dose chemotherapy, **HIT-SKK-2000**, and **EU-RHAB**.

Agent-level NCIT terms (verified via OLS4):
- **Etoposide — NCIT:C491** (topoisomerase II inhibitor)
- **Cyclophosphamide — NCIT:C405** (alkylating agent)
- **Vincristine — NCIT:C933** (vinca alkaloid, microtubule inhibitor)

The **EU-RHAB** backbone for rhabdoid tumors is "Doxorubicin plus Ifosfamide-Carboplatinum-Etoposide (ICE) plus Vincristine-Actinomycin D-Cyclophosphamide (VAC)" (EU-RHAB registry description via GPOH). Registry-level benchmarking for AT/RT under this framework: "6-year overall and event-free survival rates were 46% (±0.10) and 45% (±0.09), respectively… Treatment was feasible with significant but manageable toxicity" (Bartelheim K, Nemes K, Seeringer A, et al. "Improved 6-year overall survival in AT/RT – results of the registry study Rhabdoid 2007." *Cancer Med* 2016;5(8):1765–1775; PMID 27228363; doi 10.1002/cam4.741).

Chemotherapy use in the pooled literature: **9/18 patients (50%)** received chemotherapy (Qadri 2025).

### 12.3 Radiotherapy

- Used in the Johann cohort: **54 Gy conventional radiotherapy and proton radiation** in selected patients.
- Used in only **1/18 (5%)** of pooled published cases (Qadri 2025) — reflecting both the young age of patients and the entity's favorable behavior.
- **NCIT:C15313 — Radiation Therapy** (verified).
- Given CRINET's favorable outcome in largely radiotherapy-sparing series, **de-escalation (radiotherapy avoidance in infants) is a reasonable hypothesis but has never been formally tested**; Johann et al. do not explicitly recommend de-escalation.

### 12.4 Targeted, immuno-, gene, cell and RNA therapies

- **EZH2 inhibition is the mechanistically rational targeted strategy**, grounded in Wilson 2010's demonstration that Ezh2 inactivation blocks Snf5-loss-driven tumorigenesis. **Tazemetostat — NCIT:C107506** (verified; "an oral histone methyltransferase inhibitor… preventing methylation of histone H3 lysine 27"). Relevant trials: the pediatric phase 1 study in INI1-negative tumors and synovial sarcoma (**NCT02601937**) and the NCI-COG Pediatric MATCH arm **APEC1621C** (**NCT03213665**) for tumors with *SMARCB1*/*SMARCA4* or *EZH2* alterations. **No CRINET patient outcome on an EZH2 inhibitor has been reported**, and single-agent activity in SMARCB1-deficient pediatric tumors has been modest.
- **Nimotuzumab (anti-EGFR mAb):** a single-center retrospective series of 33 pediatric CNS tumor patients treated 2010–2015 **included one patient with cribriform neuroepithelial tumor**; across the whole series "An objective response was observed in 10 of 33 patients with four patients showing a complete response, three a partial response, and three patients had stable disease," with "2-year overall survival (OS) and progression-free survival (PFS) rates… 35 ± 9% and 19 ± 8%" (Susam-Sen H, Varan A, Bajin İ, et al. *Naunyn Schmiedebergs Arch Pharmacol* 2021;394(6):1163–1171; PMID 34151393; doi 10.1007/s00210-021-02109-y). **The CRINET patient's individual outcome is not separable from the pooled data**, and these pooled figures reflect a mixed, heavily pre-treated CNS-tumor population — they should not be read as CRINET outcomes.
- **Gene therapy, CRISPR/gene editing, ASO/siRNA/mRNA therapy, CAR-T or other cell therapy, checkpoint inhibition: none reported, none in trial for CRINET.**

### 12.5 Pharmacogenomics

**No CRINET-specific pharmacogenomic data.** Standard pediatric-oncology PGx considerations (e.g., *TPMT*/*NUDT15*, *DPYD*, *UGT1A1*) are not specifically indicated by the regimens above; no CPIC guideline applies to this entity. No PharmGKB entry for CRINET was retrieved.

### 12.6 Supportive and rehabilitative care

CSF diversion/shunting, perioperative ICP management, standard pediatric neuro-oncology supportive care, and developmental/physical/occupational/speech rehabilitation after infant brain surgery. **No CRINET-specific supportive-care or rehabilitation literature exists.**

### 12.7 Experimental / registry enrollment

- **NCT05711992 — "Rare Embryonal Tumors of the Central Nervous System: International Registry."** Observational; **RECRUITING**; estimated enrollment 300; sponsor Immune Oncology Research Institute; actual start 1 February 2023; primary outcomes 3-year and 5-year overall survival. **Cribriform neuroepithelial tumor is explicitly among the target conditions.** This is currently the most relevant prospective data-collection vehicle for CRINET.
- **EU-RHAB (European Rhabdoid Registry)** — the European framework "established to generate a common European database and to establish a standardized treatment regimen as the basis for phase I/II trials"; CRINET patients in the Johann cohort were treated on EU-RHAB among other protocols.

### 12.8 Treatment algorithm (as practiced, not as guideline)

1. Urgent management of raised ICP / obstructive hydrocephalus.
2. Maximal safe resection, with second-look surgery where residual disease is accessible.
3. Integrated diagnosis: SMARCB1 IHC → tyrosinase IHC → FISH/MLPA + sequencing → CNV/methylation classification; **exclude choroid plexus carcinoma and AT/RT.**
4. **Germline *SMARCB1* testing in every patient, regardless of age** (SIOPE).
5. Adjuvant chemotherapy on an AT/RT-type or infant-brain-tumor protocol (CPT-SIOP-2000, HIT-SKK, COG-99703, EU-RHAB), individualized.
6. Radiotherapy reserved for selected older/residual-disease cases.
7. Long-term surveillance of the patient and — if germline-positive — of the family.

---

## 13. Prevention

### 13.1 Primary prevention

**None possible.** CRINET arises from stochastic somatic *SMARCB1* inactivation or from an inherited/de novo germline variant. There is **no vaccine, no modifiable risk factor, no behavioral intervention, no public-health or environmental intervention, and no chemoprophylaxis.** Immunization is not applicable.

### 13.2 Secondary prevention — surveillance in germline *SMARCB1* carriers

This is the **only actionable prevention pathway**, and it applies to the ~20% of CRINET patients with germline variants and to their relatives.

**SIOPE Host Genome Working Group protocol for RTPS1** (Frühwald MC, et al. *Fam Cancer* 2021;20(4):305–316; PMID 33532948), verbatim elements:

| Age | Surveillance |
|---|---|
| 0–6 months | "Thorough clinical examination… at intervals of 4–6 weeks" plus "WBMRI and MRI of the CNS" at "4–6 weeks intervals… not exceeding 2–3 months" |
| 7–18 months | "MRI CNS incl. spine" and "Ultrasound abdomen plus soft tissues" — "Every 2–3 months" |
| 19 months – 5 years | Same imaging — "Every 3 months" |
| >5 years | "Yearly" whole-body MRI; physical examination "Every 6 to 12 months" |

**GeneReviews protocol** (Nemes et al., updated 12 May 2022) is closely concordant: birth–6 months, monthly-to-2-3-monthly clinical exam + abdominal/neck ultrasound + head ultrasound or brain/spine MRI; 7–18 months, every 2–3 months; 19 months–5 years, every 3 months with brain/spine MRI; after 5 years, 6-monthly clinical exam plus annual whole-body MRI.

**GeneReviews also notes:** "If a phenotypically healthy parent is found to have a SMARCB1 or SMARCA4 disease-causing germline variant, the parent should be offered surveillance, and siblings may develop rhabdoid tumors and should undergo surveillance."

### 13.3 Genetic screening and counseling

- **Cascade/germline testing:** "Evaluate all patients with a signal tumor… for a germline mutation regardless of age"; first-degree relatives offered testing; "Siblings of children with RTPS should be offered genetic screening" (SIOPE, PMID 33532948).
- **Technical requirement:** testing must cover truncating variants, whole- and partial-gene deletions, and **intron 1** of *SMARCB1* — a panel without CNV calling will miss the dominant lesion type.
- **Counseling content:** autosomal dominant transmission with 50% recurrence to offspring; **>90% penetrance by age 5** for *SMARCB1*; most probands have **de novo** variants; **germline mosaicism may explain up to half of families with affected siblings**, so apparently negative parental testing does not eliminate sibling recurrence risk; **variable expressivity within families is documented in CRINET specifically** (Johann 2017).
- **Prenatal testing / preimplantation genetic testing:** standard options for an autosomal dominant, highly penetrant, early-lethal-risk condition. **I did not retrieve CRINET- or RTPS-specific PGT practice statements in this session and therefore do not assert specific recommendations.**

### 13.4 Tertiary prevention

Early detection of recurrence via post-treatment MRI surveillance, plus long-term survivorship monitoring for treatment sequelae. **No CRINET-specific follow-up schedule has been published** — Mete et al. explicitly state that "long courses of follow-up periods are required for establishing treatment modules" (PMID 36884098).

### 13.5 Newborn and population screening

**Not applicable and not recommended.** The entity is far too rare for population screening; no newborn-screening or carrier-screening program includes *SMARCB1*.

---

## 14. Other Species / Natural Disease

- **Naturally occurring CRINET in non-human species: none reported.** I searched OMIA (Online Mendelian Inheritance in Animals) for both *SMARCB1* and "rhabdoid" and found **no entries** for either. There is **no veterinary counterpart, no breed predisposition (no VBO identifier applicable), and no zoonotic or cross-species transmission dimension** — CRINET is a sporadic somatic neoplasm, not a transmissible disease.

- **Orthologous genes** (retrieved from the Alliance of Genome Resources orthology service for HGNC:11103):

| Species | Gene | Identifier |
|---|---|---|
| Mouse (*Mus musculus*) | *Smarcb1* | MGI:1328366 |
| Rat (*Rattus norvegicus*) | *Smarcb1* | RGD:1308761 |
| Zebrafish (*Danio rerio*) | *smarcb1a* | ZFIN:ZDB-GENE-041114-5 |
| Zebrafish | *smarcb1b* | ZFIN:ZDB-GENE-991008-16 |
| *Drosophila melanogaster* | *Snr1* | FB:FBgn0011715 |
| *Xenopus laevis* | *smarcb1.L* / *smarcb1.S* | Xenbase:XB-GENE-17346118 / XB-GENE-866272 |
| *Xenopus tropicalis* | *smarcb1* | Xenbase:XB-GENE-493598 |
| *Caenorhabditis elegans* | *snfc-5* | WB:WBGene00011111 |
| *Saccharomyces cerevisiae* | *SNF5* / *SFH1* | SGD:S000000493 / S000004313 |

- **Evolutionary conservation of mechanism:** deep — the gene is conserved from budding yeast (*SNF5*, the founding member of the SWI/SNF nomenclature) through *Drosophila* (*Snr1*) to mammals, and the tumor-suppressive function of the SWI/SNF complex traces back to this conserved chromatin-remodeling machinery. "Identification of mutations and deletions in the SMARCB1 locus in chromosome band 22q11.2 in pediatric rhabdoid tumors provided the first evidence for the involvement of the SWI/SNF chromatin remodeling complex in cancer" (Biegel JA, Busse TM, Weissman BE. *Am J Med Genet C* 2014;166C(3):350–366; PMID 25169151; doi 10.1002/ajmg.c.31410).

- **NCBI Taxonomy:** the disease is described only in *Homo sapiens* (NCBI:txid9606). *(I did not separately fetch NCBI Taxonomy IDs for the model species in this session and therefore do not list them.)*

---

## 15. Model Organisms

### 15.1 Key point for curation

**There is no model of CRINET.** Every available model reproduces *SMARCB1/Snf5* loss and generates **rhabdoid tumors or AT/RT-like tumors — i.e., the aggressive counterpart — not the cribriform, non-rhabdoid, favorable-outcome phenotype.** This is arguably the single most important gap in the field, because the mechanistic question that matters clinically (why CRINET behaves better than molecularly identical ATRT-TYR) has no experimental system in which to be asked.

### 15.2 Available genetic mouse models of *Smarcb1* loss

| Model | Design | Phenotype | Source |
|---|---|---|---|
| ***Snf5* heterozygous knockout** | Germline haploinsufficiency | Mice "develop tumors consistent with MRT beginning at five weeks of age," establishing "Snf5, a core member of the Swi/Snf chromatin-remodeling complex, functions as a tumor suppressor gene" | Roberts CW, Galusha SA, McMenamin ME, Fletcher CD, Orkin SH. *PNAS* 2000;97(25):13796–13800; PMID 11095756; doi 10.1073/pnas.250492697 |
| **Conditional inversion ("reversibly inactivating") *Snf5* allele** | Conditional biallelic inactivation | "loss of Snf5/Ini1/Baf47/SmarcB1, a core subunit of SWI/SNF, results in highly penetrant cancer predisposition with 100% of mice developing mature CD8(+) T cell lymphoma or rare rhabdoid tumors with a median onset of only 11 weeks"; Snf5 remains "essential for nonmalignant cell survival" | Roberts CW, Leroux MM, Fleming MD, Orkin SH. *Cancer Cell* 2002;2(5):415–425; PMID 12450796; doi 10.1016/s1535-6108(02)00185-x |
| ***Snf5*/*p53* combined deletion in GFAP+ progenitors** | Conditional, CNS-targeted, with *Trp53* loss | **First genetically engineered mouse model of AT/RT.** "Gene expression analysis confirmed that the tumors that arose in Snf5/p53 mutant mice were distinct from other neural tumors and most closely resembled human AT/RT." Also revealed a role for Snf5 in oligodendrocyte generation/survival | Ng JM, Martinez D, Marsh ED, et al. *Cancer Res* 2015;75(21):4629–4639; PMID 26363008; doi 10.1158/0008-5472.CAN-15-0874 |
| **Developmental-timing conditional *Smarcb1* ± *Nf2* models** | Stage-specific Cre drivers | Timing determines outcome: "Smarcb1 loss in early neural crest was necessary to initiate tumorigenesis" producing rhabdoid tumors, whereas later loss with *Nf2* inactivation produced schwannomas — modeling the two distinct human *SMARCB1* germline syndromes (RTPS and schwannomatosis) | Vitte J, Gao F, Coppola G, Judkins AR, Giovannini M. *Nat Commun* 2017;8(1):300; PMID 28824165; doi 10.1038/s41467-017-00346-5 |
| **Pharmacologic/genetic rescue model** | *Ezh2* inactivation on a *Snf5*-loss background | "inactivation of Ezh2 blocks tumor formation driven by Snf5 loss" — the proof-of-principle for EZH2 inhibition | Wilson BG, et al. *Cancer Cell* 2010;18(4):316–328; PMID 20951942 |

### 15.3 In vitro / cellular systems

SMARCB1-deficient **malignant rhabdoid tumor cell lines** are the standard in vitro system and underpin the enhancer-biology work (Wang 2017, PMID 27941797) and EZH2-inhibitor sensitivity. **No CRINET-derived cell line, organoid, xenograft or iPSC model has been reported**, which is unsurprising given that most CRINET patients are cured and tumor material is scarce.

### 15.4 Phenotype recapitulation and limitations

- **What the models capture:** SWI/SNF-dependent tumor suppression; the two-hit requirement; the cell-of-origin/developmental-timing dependence; EZH2 dependency; the brain-localized AT/RT phenotype (Ng 2015).
- **What they do NOT capture:** cribriform architecture; EMA-positive luminal differentiation; the tyrosinase/MITF melanosomal program of the TYR lineage; the intraventricular localization; and above all **the favorable clinical behavior that defines CRINET.** The mouse AT/RT model also required concurrent *p53* loss, which is **not** a feature of human CRINET (whose genome is otherwise stable).
- **Research applications currently feasible:** SWI/SNF/PRC2 epigenetic biology, EZH2-inhibitor pharmacology, developmental cell-of-origin questions. **Not feasible:** anything about CRINET's distinctive morphology or prognosis.

### 15.5 Model resources

MGI (*Smarcb1*, MGI:1328366), RGD (RGD:1308761), ZFIN, FlyBase, WormBase, SGD and Xenbase hold the orthologs listed in §14; the Alliance of Genome Resources aggregates them. *I was unable to load the MGI allele/phenotype page directly in this session (HTTP 500), so I do not list specific allele symbols.*

---

## Summary of Evidence Gaps (explicit, for knowledge-base flagging)

The following template fields have **no retrievable evidence** for CRINET and should be recorded as "no data" rather than inferred:

1. Orphanet code, OMIM phenotype number, ICD-10/ICD-11/ICD-O codes, SNOMED CT concept, dedicated MeSH descriptor
2. Prevalence and incidence (any denominator-based estimate)
3. Any environmental, lifestyle, infectious or gene–environment etiologic factor
4. Any protective factor (genetic or environmental)
5. Curated HPO disease annotations with frequencies
6. Quality-of-life, neurocognitive and late-effects outcome data
7. Transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial and functional-genomics (CRISPR/RNAi) profiling of CRINET
8. Relapse rate, CSF-dissemination rate, and any within-CRINET prognostic factor
9. CRINET-specific treatment guideline, prospective trial, or pharmacogenomic data
10. Any animal model, cell line, organoid or xenograft of CRINET itself
11. Reliable sex ratio (primary and pooled sources conflict: 6M:4F vs 72% female)
12. The mechanism of CRINET's prognostic divergence from molecularly identical ATRT-TYR — explicitly stated as unresolved by the field's definitive paper

---

## Sources

- [Johann PD, et al. Cribriform neuroepithelial tumor: molecular characterization of a SMARCB1-deficient non-rhabdoid tumor with favorable long-term outcome. Brain Pathol. 2017;27(4):411-418. PMID 27380723 (PMC8028967)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8028967/)
- [Hasselblatt M, et al. Cribriform neuroepithelial tumor (CRINET): a nonrhabdoid ventricular tumor with INI1 loss and relatively favorable prognosis. J Neuropathol Exp Neurol. 2009;68(12):1249-55. PMID 19915490](https://academic.oup.com/jnen/article/68/12/1249/2609934)
- [Johann PD, et al. Atypical Teratoid/Rhabdoid Tumors Are Comprised of Three Epigenetic Subgroups with Distinct Enhancer Landscapes. Cancer Cell. 2016;29(3):379-393. PMID 26923874](https://www.cell.com/cancer-cell/fulltext/S1535-6108(16)30035-6)
- [Ho B, et al. Molecular subgrouping of atypical teratoid/rhabdoid tumors—a reinvestigation and current consensus. Neuro Oncol. 2020. PMID 31889194](https://pubmed.ncbi.nlm.nih.gov/31889194/)
- [Gessi M, et al. High-Resolution Genomic Analysis of Cribriform Neuroepithelial Tumors of the Central Nervous System. J Neuropathol Exp Neurol. 2015. PMID 26352987](https://pubmed.ncbi.nlm.nih.gov/26352987/)
- [Arnold MA, et al. Cribriform neuroepithelial tumor arising in the lateral ventricle. Pediatr Dev Pathol. 2013. PMID 23495723](https://journals.sagepub.com/doi/10.2350/12-12-1287-CR.1)
- [Park JY, et al. Cribriform neuroepithelial tumor in the third ventricle. Neuropathology. 2012. PMID 22239490](https://pubmed.ncbi.nlm.nih.gov/22239490/)
- [Liu Y, et al. Cribriform neuroepithelial tumor: report of a case. Zhonghua Bing Li Xue Za Zhi. 2022. PMID 35673730](https://pubmed.ncbi.nlm.nih.gov/35673730/)
- [Mete EB, et al. Transcallosal and endoscopic hybrid approach... cribriform neuroepithelial tumor. Childs Nerv Syst. 2023. PMID 36884098](https://link.springer.com/article/10.1007/s00381-023-05897-1)
- [Tauziède-Espariat A, et al. A novel case of cribriform neuroepithelial tumor: a potential diagnostic pitfall in the ventricular system. Pediatr Blood Cancer. 2021. PMID 34151521](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:34151521&resultType=core&format=json)
- [Dahlback HS, et al. Genomic aberrations in pediatric gliomas and embryonal tumors. Genes Chromosomes Cancer. 2011. PMID 21717527](https://pubmed.ncbi.nlm.nih.gov/21717527/)
- [Ruland V, et al. Choroid plexus carcinomas are characterized by complex chromosomal alterations... Genes Chromosomes Cancer. 2014. PMID 24478045](https://pubmed.ncbi.nlm.nih.gov/24478045/)
- [Louis DN, et al. The 2021 WHO Classification of Tumors of the Central Nervous System: a summary. Neuro Oncol. 2021;23(8):1231-1251. PMID 34185076](https://pmc.ncbi.nlm.nih.gov/articles/PMC8328013/)
- [Rigsby RK, et al. Newly Recognized CNS Tumors in the 2021 WHO Classification. AJNR Am J Neuroradiol. 2023;44(4):367. PMID 36997287 (PMC10084895)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10084895/)
- [Eaton S, Almotairi A, Levine A, Hawkins C. Updates on diagnostic and prognostic molecular biomarkers of CNS tumors. Neurotherapeutics. 2026. PMID 42753289](https://pmc.ncbi.nlm.nih.gov/articles/PMC13602056)
- [Qadri HM, et al. Primary Intracranial Cribriform Neuroepithelial Tumor (PICRINET): A Systematic Review of Cases From 2000–2025. OncoDaily Medical Journal. 2025](https://oncodailyjournal.com/10.69690/odmj-018-0915-5372/)
- [NCI PDQ. Childhood Atypical Teratoid/Rhabdoid Tumor Treatment (Health Professional Version), updated 3 March 2025](https://www.cancer.gov/types/brain/hp/child-cns-atrt-treatment-pdq)
- [Nemes K, Bens S, Bourdeaut F, et al. Rhabdoid Tumor Predisposition Syndrome. GeneReviews®, last update 12 May 2022](https://www.ncbi.nlm.nih.gov/sites/books/NBK469816/)
- [Frühwald MC, et al. Current recommendations for clinical surveillance and genetic testing in rhabdoid tumor predisposition: a report from the SIOPE Host Genome Working Group. Fam Cancer. 2021;20(4):305-316. PMID 33532948](https://pmc.ncbi.nlm.nih.gov/articles/PMC8484234/)
- [Wang X, et al. SMARCB1-mediated SWI/SNF complex function is essential for enhancer regulation. Nat Genet. 2017;49(2):289-295. PMID 27941797](https://pubmed.ncbi.nlm.nih.gov/27941797/)
- [Wilson BG, et al. Epigenetic antagonism between polycomb and SWI/SNF complexes during oncogenic transformation. Cancer Cell. 2010;18(4):316-328. PMID 20951942](https://pubmed.ncbi.nlm.nih.gov/20951942/)
- [Kohashi K, Oda Y. Oncogenic roles of SMARCB1/INI1 and its deficient tumors. Cancer Sci. 2017. PMID 28109176](https://pubmed.ncbi.nlm.nih.gov/28109176/)
- [Roberts CW, et al. Haploinsufficiency of Snf5 predisposes to malignant rhabdoid tumors in mice. PNAS. 2000. PMID 11095756](https://pubmed.ncbi.nlm.nih.gov/11095756/)
- [Roberts CW, et al. Highly penetrant, rapid tumorigenesis through conditional inversion of the tumor suppressor gene Snf5. Cancer Cell. 2002. PMID 12450796](https://www.sciencedirect.com/science/article/pii/S153561080200185X)
- [Ng JM, et al. Generation of a mouse model of AT/RT through combined deletion of Snf5 and p53. Cancer Res. 2015. PMID 26363008](https://pubmed.ncbi.nlm.nih.gov/26363008/)
- [Vitte J, et al. Timing of Smarcb1 and Nf2 inactivation determines schwannoma versus rhabdoid tumor development. Nat Commun. 2017. PMID 28824165](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5563506/)
- [Bartelheim K, et al. Improved 6-year overall survival in AT/RT – results of the registry study Rhabdoid 2007. Cancer Med. 2016. PMID 27228363](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4884635/)
- [Susam-Sen H, et al. Nimotuzumab therapy in pediatric CNS tumors. Naunyn Schmiedebergs Arch Pharmacol. 2021. PMID 34151393](https://pubmed.ncbi.nlm.nih.gov/34151393/)
- [Biegel JA, Busse TM, Weissman BE. SWI/SNF chromatin remodeling complexes and cancer. Am J Med Genet C. 2014. PMID 25169151](https://pubmed.ncbi.nlm.nih.gov/25169151/)
- [Cai C. SWI/SNF deficient central nervous system neoplasms. Semin Diagn Pathol. 2021. PMID 33762087](https://pubmed.ncbi.nlm.nih.gov/33762087/)
- [Pawel BR. SMARCB1-deficient Tumors of Childhood: A Practical Guide. Pediatr Dev Pathol. 2018. PMID 29280680](https://pubmed.ncbi.nlm.nih.gov/29280680/)
- [Agaimy A. The expanding family of SMARCB1(INI1)-deficient neoplasia. Adv Anat Pathol. 2014. PMID 25299309](https://pubmed.ncbi.nlm.nih.gov/25299309/)
- [Dunham C. Uncommon pediatric tumors of the posterior fossa. Childs Nerv Syst. 2015. PMID 26351226](https://pubmed.ncbi.nlm.nih.gov/26351226/)
- [Cotter JA, Judkins AR. Evaluation and Diagnosis of CNS Embryonal Tumors (Non-Medulloblastoma). Pediatr Dev Pathol. 2022. PMID 35168419](https://pubmed.ncbi.nlm.nih.gov/35168419/)
- [MONDO:1060254 — EBI OLS4](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:1060254)
- [NCIT:C121963 — EBI OLS4](https://www.ebi.ac.uk/ols4/api/ontologies/ncit/terms?obo_id=NCIT:C121963)
- [MedGen UID 888969 — Cribriform neuroepithelial tumor](https://www.ncbi.nlm.nih.gov/medgen/888969)
- [HGNC record for SMARCB1 (HGNC:11103)](https://rest.genenames.org/fetch/symbol/SMARCB1)
- [Ensembl lookup, SMARCB1 (ENSG00000099956)](https://rest.ensembl.org/lookup/symbol/homo_sapiens/SMARCB1?expand=0;content-type=application/json)
- [Alliance of Genome Resources — SMARCB1 orthologs](https://www.alliancegenome.org/api/gene/HGNC:11103/orthologs?limit=20)
- [ClinicalTrials.gov NCT05711992 — Rare Embryonal Tumors of the CNS: International Registry](https://clinicaltrials.gov/study/NCT05711992)
- [EU-RHAB protocol (GPOH)](https://www.gpoh.de/kinderkrebsinfo/content/e1676/e9032/e1758/e83294/download84621/EU-RHABProtokoll_2021_08_ger.pdf)
- [Tazemetostat pediatric phase 1, NCT02601937 (protocol)](https://cdn.clinicaltrials.gov/large-docs/37/NCT02601937/Prot_000.pdf)
- [Tazemetostat, NCI-COG Pediatric MATCH APEC1621C / NCT03213665](https://cdn.clinicaltrials.gov/large-docs/65/NCT03213665/Prot_SAP_000.pdf)
- [CRINET SIOP 2016 poster (Johann/Hasselblatt, University Hospital Münster)](http://simul-europe.com/2016/siop/Files/(hasselblatt@uni-muenster.de)CRINET_SIOP.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 78 |
| Resolved | 77 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 21 |
| Quoted claims found in source | 12 |
| Quoted claims **not** found in source | 9 |
| Quoted claims with nothing to check against | 2 |
| References weighed for topical relevance | 77 |
| On topic | 41 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.3760/cma.j.cn112151-20211104-00799` (1 mention) - Identifier did not resolve to a record

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:33532948` *(abstract only)*: "Among newly diagnosed cases of MRT 25–35% carry a germline PV in *SMARCB1*"
  - closest text in source: "In contrast to other genetic disorders related to PVs in SMARCB1 and SMARCA4 such as Coffin-Siris Syndrome, RTPS1&2 are characterized by a predominance of truncating PVs, terminating transcription thus explaining a specific cancer risk"
- `DOI:10.1007/s10689-021-00229-1` *(abstract only)*: "Among newly diagnosed cases of MRT 25–35% carry a germline PV in *SMARCB1*"
  - closest text in source: "In contrast to other genetic disorders related to PVs in SMARCB1 and SMARCA4 such as Coffin-Siris Syndrome, RTPS1&2 are characterized by a predominance of truncating PVs, terminating transcription thus explaining a specific cancer risk"
- `PMID:35673730` *(abstract only)*: "MRI revealed a mixed signal fourth ventricular mass causing obstructive hydrocephalus"
  - Text part not found as substring: 'MRI revealed a mixed signal fourth ventricular mass causing obstructive hydrocephalus' (note: only abstract available for PMID:35673730, full text may contain this excerpt)
- `PMID:35673730` *(abstract only)*: "An eight-month-old male presented with downward gaze and growth failure"
  - Text part not found as substring: 'An eight-month-old male presented with downward gaze and growth failure' (note: only abstract available for PMID:35673730, full text may contain this excerpt)
- `PMID:42753289` *(abstract only)*: "Cribriform histology distinguishes CRINET from AT/RT. Prognosis is more favorable than AT/RT."
  - closest text in source: "The diagnosis and classification of central nervous system (CNS) tumors has undergone a paradigm shift over the past decade, evolving from a purely histology-based approach to an integrated framework that incorporates molecular and epigenetic features"
- `PMID:42753289` *(abstract only)*: "making its distinction from ATRT clinically meaningful"
  - closest text in source: "In ependymomas, medulloblastomas, atypical teratoid/rhabdoid tumors, meningiomas, pineal tumors, and embryonal tumors, methylation profiling now defines biologically and clinically meaningful subgroups that inform risk stratification and treatment selection"
- `PMID:36884098` *(abstract only)*: "A twenty-month-old male underwent transcallosal resection and endoscopic second-look surgery… Complete resection was achieved without complications"
  - closest text in source: "METHODS: Twenty-month-old male with intraventricular tumor underwent transcallosal intraventricular tumor resection and endoscopic intraventricular second look stages"
- `PMID:34151393` *(abstract only)*: "2-year overall survival (OS) and progression-free survival (PFS) rates… 35 ± 9% and 19 ± 8%"
  - closest text in source: "The 2-year overall survival (OS) and progression-free survival (PFS) rates were 35 ±9% and 19 ±8%, respectively"
- `PMID:33532948` *(abstract only)*: "Siblings of children with RTPS should be offered genetic screening"
  - closest text in source: "The rhabdoid tumor (RT) predisposition syndromes 1 and 2 (RTPS1 and 2) are rare genetic conditions rendering young children vulnerable to an increased risk of RT, malignant neoplasms affecting the kidney, miscellaneous soft-part tissues, the liver and the central nervous system (Atypical Teratoid Rhabdoid Tumors, ATRT)"

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.1007/s00381-023-05897-1`: "A twenty-month-old male underwent transcallosal resection and endoscopic second-look surgery… Complete resection was achieved without complications"
  - Reference resolved but exposes no abstract or full text to search
- `DOI:10.1007/s00210-021-02109-y`: "2-year overall survival (OS) and progression-free survival (PFS) rates… 35 ± 9% and 19 ± 8%"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 5 |
| Terms whose name was checked | 20 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:1060254` (7 mentions) - the report calls it "Mondo", "EBI OLS4"; MONDO calls it **cribriform neuroepithelial tumor**
- `NCIT:C121963` (5 mentions) - the report calls it "NCI Thesaurus", "EBI OLS4"; NCIT calls it **Cribriform Neuroepithelial Tumor**
- `HP:0001251` (1 mention) - the report calls it "Ataxia / gait disturbance, motor regression"; HP calls it **Ataxia**
- `GO:0071565` (2 mentions) - the report calls it "verified"; GO calls it **nBAF complex**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000238` (1 mention) - the report calls it "Hydrocephalus (obstructive)"; HP calls it **Hydrocephalus**
- `HP:0001508` (1 mention) - the report calls it "Failure to thrive / growth failure"; HP calls it **Failure to thrive**
- `UBERON:0002285` (1 mention) - the report calls it "Lateral ventricle (label: telencephalic ventricle)"; UBERON calls it **telencephalic ventricle**
- `UBERON:0001886` (1 mention) - the report calls it "Choroid plexus (differential-diagnostic structure; see below)"; UBERON calls it **choroid plexus**, and lists "choroid plexus of cerebral hemisphere" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:1060254` - called "Mondo", "EBI OLS4"
- `NCIT:C121963` - called "NCI Thesaurus", "EBI OLS4"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`, `RGD`, `SGD`, `EXT_ID`.