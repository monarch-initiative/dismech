---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5
cached: false
start_time: '2026-11-18T15:00:18.188980'
end_time: '2026-11-18T15:16:31.102002'
duration_seconds: 972.91
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: PBRM1-Related BAFopathy
  mondo_id: MONDO:0700122
  category: Mendelian
  causal_genes: PBRM1
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
  - claude-opus-5
  web_search_requests: 23
  num_turns: 56
  total_cost_usd: 6.3396438800000015
  session_id: 0d92cf0b-dcaa-46f9-a566-0dcdaab2a201
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 257
  retrieval_calls: 255
  assistant_text_blocks: 38
citation_count: 93
reference_validation:
  total_references: 143
  verified: 143
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  quotes_not_checkable: 2
  relevance_assessed: 143
  on_topic: 49
  off_topic: 2
  off_topic_references:
  - PMID:42748234
  - DOI:10.1126/sciadv.aei0972
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 139
  verified: 128
  not_found: 1
  obsolete: 0
  unverifiable: 10
  confabulation_rate: 0.008
  labels_checked: 99
  labels_matching: 80
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0700122
    reported_labels:
    - 'Title: "Curate PBRM1-related BAFopathy'
    - Mondo
    ontology_label: PBRM1-related BAFopathy
  - term_id: GO:2000781
    reported_labels:
    - NAS, PMID 25066234
    ontology_label: positive regulation of double-strand break repair
  - term_id: HP:0001629
    reported_labels:
    - Ventricular septal defect
    - a feature that should be actively looked for if more human cases accrue
    ontology_label: Ventricular septal defect
  - term_id: UBERON:0001885
    reported_labels:
    - dentate gyrus of hippocampal formation
    - site of the excessive neurogenesis phenotype
    ontology_label: dentate gyrus of hippocampal formation
  - term_id: UBERON:0003053
    reported_labels:
    - ventricular zone
    - "PBRM1\u2011rich germinal zone at E14.5"
    ontology_label: ventricular zone
  - term_id: UBERON:0002336
    reported_labels:
    - corpus callosum
    - white matter, given the oligodendrocyte phenotype
    ontology_label: corpus callosum
  - term_id: NCIT:C159273
    reported_labels:
    - so the intended term should be selected deliberately rather than assumed
    ontology_label: Speech Language Therapy
  labels_variant: 12
  unresolved_terms:
  - RO:0004003
  unresolvable_prefixes:
  - MGI
  - RGD
  - Chr3
  - Chr14
  - EXT_ID
  - BRD7
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PBRM1-Related BAFopathy
- **MONDO ID:** MONDO:0700122 (if available)
- **Causal gene(s):** PBRM1
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **PBRM1-Related BAFopathy** covering all of the
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

All four sources agree on the core facts, but none lists OMIM, Orphanet, MedGen, DOID, UMLS, or synonym IDs for this term. The fallback OLS page was not needed because the API call succeeded.

**1. OLS4 API** (https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0700122), HTTP 200
- Label: `PBRM1-related BAFopathy`
- IRI: `http://purl.obolibrary.org/obo/MONDO_0700122`; short_form `MONDO_0700122`; obo_id `MONDO:0700122`
- Definition (verbatim): "Any BAFopathy in which the cause of the disease is a mutation in the PBRM1 gene."
- Synonyms: none (empty list)
- Xrefs: none in `obo_xref`, which is null. The `annotation` field gives `id: MONDO:0700122` and a term tracker item, https://github.com/monarch-initiative/mondo/issues/3939.
- Definition citation: `patterns/OMIM_disease_series_by_gene` (MONDO) and PMID 30580808 (https://pubmed.ncbi.nlm.nih.gov/30580808)
- Flags: is_obsolete false, is_root false, has_children false, is_defining_ontology true
- Ontology IRI: `http://purl.obolibrary.org/obo/mondo/mondo-international.owl`
- Parents are not inlined; the response links to a `/parents` endpoint that I did not fetch.
- Relation link: `RO_0004003` ("has material basis in germline mutation in").

**2. Monarch website** (https://monarchinitiative.org/MONDO:0700122), HTTP 200, but the page is JavaScript-rendered. The only text returned was "Monarch Initiative", so it gave no term data.

**3. Monarch API v3** (https://api.monarchinitiative.org/v3/api/entity/MONDO:0700122), HTTP 200
- id `MONDO:0700122`; category `biolink:Disease`; namespace `MONDO`
- name: `PBRM1-related BAFopathy`
- description (verbatim): "Any BAFopathy in which the cause of the disease is a mutation in the PBRM1 gene."
- xref: null; synonym: null (all exact, broad, narrow, related synonym fields null); mappings: []; external_links: []; equivalent IDs: none
- Superclass: `MONDO:0700120` BAFopathy (no description returned)
- Subclasses: none (sub_classes []; has_descendant_count 1, which is the term itself)
- Associated gene: `HGNC:30064` PBRM1 (biolink:Gene, Homo sapiens, NCBITaxon:9606), via `RO:0004003` "has material basis in germline mutation in". causal_gene is an empty list.
- has_phenotype_count 0.

**4. GitHub issue** (https://github.com/monarch-initiative/dismech/issues/16131), HTTP 200
- Title: "Curate PBRM1-related BAFopathy (MONDO:0700122) #16131"
- State: open. Opened by aleixpuigb on Oct 31, 2026. Assigned to aleixpuigb. Labels: claim, curation, enhancement, high_effort. Linked PR #18384 (open).
- The issue body is a curation request. It describes the disorder as "a neurodevelopmental disorder caused by germline PBRM1 variants." It also names the stub `stubs/PBRM1-related_BAFopathy.yaml` and says the decision on entry type is still open.
- A github-actions bot comment says the stub's `entry_type` is still `UNDECIDED`. It states the MONDO parent as `MONDO:0700120` BAFopathy and the causal gene as `hgnc:30064` PBRM1.
- The issue contains no OMIM, Orphanet, MedGen, DOID, or UMLS IDs.

**Sibling and related terms**
- The only BAFopathy-related MONDO term visible is the parent, `MONDO:0700120` BAFopathy. No other BAFopathy children or siblings are visible in any source.
- The GitHub issue mentions KB entries `Coffin_Siris_Syndrome` and `Nicolaides-Baraitser_Syndrome` as related BAF-complex disorders. It gives no MONDO IDs for them, and I did not fetch them.

Only the HGNC REST page returned usable data. The NCBI Gene, UniProt, and OMIM pages did not return their content, so items 1, 3, and 4 are unanswered.

**1. NCBI Gene (https://www.ncbi.nlm.nih.gov/gene/55193): blocked.** The server returned HTTP 200, but the body was a reCAPTCHA "Checking your browser" interstitial with no gene data. Nothing from this page is reported. This is a permanent block for this fetch, so retrying the same URL would return the same interstitial.

**2. HGNC REST (https://rest.genenames.org/fetch/symbol/PBRM1): read (HTTP 200, XML despite the request for JSON).**
- HGNC ID: HGNC:30064
- Symbol: PBRM1, status Approved
- Approved name: "polybromo 1" (field `name`)
- Previous symbols: none listed in the record
- Alias symbols: BAF180, PB1, SMARCH1
- Locus type: gene with protein product; locus group: protein-coding gene
- UniProt ID: Q86U86
- OMIM ID: 606083
- Ensembl gene ID: ENSG00000163939
- Entrez gene ID: 55193
- RefSeq accession (`refseq_accession`): NM_018165
- MANE Select: ENST00000707071.1 and NM_001405607.1
- CCDS IDs: CCDS2859, CCDS2860, CCDS43099, CCDS87087, CCDS93285, CCDS93286
- Location: 3p21.1
- Gene groups: "Bromodomain containing" and "PBAF complex subunits" (group IDs 1232 and 1605)
- Other IDs: MGI:1923998 (mouse), RGD:1565549 (rat), Vega OTTHUMG00000152663, Orphanet 434716, UCSC uc003des.3
- Date approved: 2007-03-29; date modified: 2023-01-20

**3. UniProt (https://www.uniprot.org/uniprotkb/Q86U86/entry): not read.** The page returned HTTP 200 but only a "UniProt website fallback message" with troubleshooting text. It contained no entry data, so I have no protein name, length, domains, function text, location, disease, or variants.

**4. OMIM (https://www.omim.org/entry/606083): blocked.** The server returned HTTP 403 Forbidden, so no entry title, allelic variants, or phenotype table were retrieved. Retrying would fail the same way.

I did not fill any of the unread fields from memory. Items 1, 3, and 4 would need another source, such as an authenticated or different access route, or a direct check of the NCBI, UniProt, and OMIM pages in a browser.

The gnomAD gene page returned only a 6-character JavaScript shell, so it has no readable data. I'll try the gnomAD API URL you listed and the two fallback pages.

I could not get the gnomAD constraint numbers you asked for. The only constraint values I retrieved come from a ClinGen mirror of gnomAD v4.0, not from gnomAD itself.

**Values retrieved (source: ClinGen gene page, which labels them gnomAD v4.0 and DECIPHER)**
- pLI: 1
- LOEUF: 0.23
- %HI (DECIPHER Haploinsufficiency Index): 9.54
- ClinGen says the pLI and LOEUF are "based on ENST00000296302 transcript." The MANE Select transcript it lists is NM_001405607.1 / ENST00000707071.1, so the constraint transcript differs from MANE Select.

**Not retrieved (no value given)**
- LOEUF confidence interval
- o/e missense and its Z score
- Observed vs expected pLoF counts
- Total pLoF variant count

**Source-by-source results**
1. gnomAD gene page (https://gnomad.broadinstitute.org/gene/ENSG00000163939?dataset=gnomad_r4): HTTP 200, but the body was only 6 characters ("gnomAD"). It is a JavaScript shell with no gene data.
2. gnomAD API (https://gnomad.broadinstitute.org/api): HTTP 400. My tool only does GET requests and this is a GraphQL endpoint, so a query-based request is needed. Retrying would fail the same way.
   - DECIPHER (https://www.deciphergenomics.org/gene/PBRM1/overview/protein-genomic-info): HTTP 500. Permanent for this tool, so I did not retry.
   - GeneCards (https://www.genecards.org/cgi-bin/carddisp.pl?gene=PBRM1): HTTP 403. Permanent, so I did not retry.
   - gnomAD v2.1.1 mirror: not fetched. You did not give a URL for it, and I did not guess one.
3. ClinGen (https://search.clinicalgenome.org/kb/genes/HGNC:30064): HTTP 200. Gene symbol and HGNC ID match. Cytoband is 3p21.1. The page shows:
   - Gene-Disease Validity classifications: 0
   - Dosage Sensitivity classifications: 0
   - Clinical Actionability assertions: 0
   - Variant Pathogenicity assertions: 0
   - Statement: "ClinGen has not yet published curations for PBRM1 (HGNC:30064)."
   - So there is no validity classification, haploinsufficiency or triplosensitivity score, dosage date, or associated disease entity.

To get the full gnomAD numbers, someone with access to the gnomAD v4.x GraphQL API, or a local gnomAD download, would need to query the gene. This tool cannot do that.

I could not get the article content. The PMC URL returned an HTTP 200 page that is a browser verification interstitial ("Checking your browser before accessing pmc.ncbi.nlm.nih.gov... reCAPTCHA"), not the paper. I did not retry or try variants, since a bot-check page is a permanent block for this fetch.

Because I read none of the article, I have nothing to report on the citation, abstract, mouse model, behavior, neurogenesis, CCL5/CCR1/CCR5 mechanism, rescue experiments, human data, or GEO accessions. I did not fill any of these from memory.

Options to get the content:
- Open the PMC URL in a normal browser and paste the text or abstract here.
- Give me the article's DOI or the publisher's full-text URL (Advanced Science) so I can try that host instead.
- Provide the full text as a file, if you have it locally.

URL read: https://pmc.ncbi.nlm.nih.gov/articles/PMC13676817/ (status 200, but the content is the verification page only).

## Report: Machol/Chen et al., BAFopathy clinical exome cohort (PMC8957292)

**Source status:** I read the PMC page (https://pmc.ncbi.nlm.nih.gov/articles/PMC8957292/). The first ~40,000 of ~90,000 characters are verbatim. The rest came back only as a model-extracted summary, so I treat anything from that part as unverified. The PubMed URL (https://pubmed.ncbi.nlm.nih.gov/34906496/) returned HTTP 203 with a cookie-consent page and no article metadata. The PDF link (https://pmc.ncbi.nlm.nih.gov/articles/PMC8957292/pdf/nihms-1784438.pdf) returned a download interstitial with no content. Both failed permanently, so I did not retry them.

**Quoting limit:** The source is not on the preapproved list, so I could not reproduce the abstract or table text in full. Quotes below are short and the rest is paraphrased. For the exact wording, read the abstract at the PMC URL above.

### Citation
- Title: "Retrospective analysis of a clinical exome sequencing cohort reveals the mutational spectrum and identifies candidate disease-associated loci for BAFopathies"
- Authors: Chun-An Chen and John Lattier (equal contribution), Wenmiao Zhu, Jill Rosenfeld, Lei Wang, Tiana M Scott, Haowei Du, Vipulkumar Patel, Anh Dang, Pilar Magoulas, Haley Streff, Jessica Sebastian, Shayna Svihovec, Kathryn Curry, Mauricio R Delgado, Neil Hanchard, Seema Lalani, Ronit Marom, Suneeta Madan-Khetarpal, Margarita Saenz, Hongzheng Dai, Linyan Meng, Fan Xia, Weimin Bi, Pengfei Liu, Jennifer E Posey, Daryl A Scott, James R Lupski, Christine M Eng, Rui Xiao, Bo Yuan (corresponding).
- Journal: Genetics in Medicine. Published 2021 Nov 30, 24(2):364–373. Author manuscript issue date 2022 Feb.
- DOI: 10.1016/j.gim.2021.09.017. PMID 34906496 (from the PMC page; PubMed itself was not read).

### Abstract (paraphrased)
- **Purpose:** The BAF complex is a chromatin remodeler, and defects in its subunit genes cause BAFopathies, neurodevelopmental disorders with wide locus and phenotypic heterogeneity.
- **Methods:** Retrospective analysis of 16,243 patients referred for clinical exome sequencing, focused on the BAF complex, using a genotype-first approach with predicted genic constraints. The page quotes the phrase "We retrospectively analyzed data from 16,243 patients."
- **Results:** 127 patients carried pathogenic/likely pathogenic variants or de novo VUS in 11 known BAFopathy genes. Of these, 34 were diagnosed by exome reanalysis: 21 through new gene-disease evidence and 13 through variant reclassification. De novo or predicted loss-of-function variants were found in four candidate genes: ACTL6A, BICRA, PBRM1, and SMARCC1.
- **Conclusion:** The authors report the BAFopathy mutational spectrum in this cohort and propose candidate genes, saying further mechanistic and phenotypic work is needed to confirm them.

### PBRM1 (verbatim text read, plus Table 1)
- **Cases:** One. Patient N5 is the only PBRM1 case, and the text describes it as a single patient.
- **Variant:** c.1542–3C>G (NM_018313.4), intron 14, hg19 Chr3:52651557, splicing type. The page uses an en dash in "c.1542–3C>G."
- **Zygosity:** Heterozygous (Het).
- **Inheritance:** De novo. The text says "A de novo heterozygous c.1542–3C>G variant in PBRM1 was identified in Patient N5."
- **Predicted effect:** Multiple algorithms predicted the variant activates a cryptic splice acceptor 2 bp 5' of the canonical acceptor. SpliceAI predicted loss of the canonical acceptor (score 0.91) and gain of a cryptic acceptor 1 bp upstream (score 0.98). No RNA was available, so the splicing change was not confirmed.
- **Table 1 gene-level values for PBRM1:** pLI 1.00, gnomAD allele frequency 0.00.
- **Phenotype, age, sex:** Not given in the text I read verbatim. Unlike N4 (BICRA), no clinical description is given for N5. The unread remainder was summarized as containing no PBRM1 phenotype data, but I could not verify that.
- **HPO-style features:** None reported in what I read.

### Candidate vs. established status and evidence
- **Selection:** The authors filtered for BAF genes without an established gene-disease association and with gnomAD pLI ≥ 0.98. The verbatim list is ACTL6A, BRD7, BICRA, BICRAL, DPF1, PBRM1, SMARCC1, and SS18L1.
- **Candidate status:** PBRM1 is a candidate, not established. The abstract lists it among four candidate genes.
- **Burden/statistics:** The verbatim text gives no PBRM1-specific burden statistic and no o/e or LOEUF value. The only constraint value is the pLI of 1.00 in Table 1. The summary says DDD and denovo-db were checked and a large trio study did not associate PBRM1 with developmental disorders, but this is unverified and I give no p-values for it.

### Cohort and methods
- **Cohort:** 16,243 patients referred for clinical exome sequencing at Baylor Genetics, March 2012 to December 2019. About 87.8% had neurologic disorders, per the text.
- **Methods:** Trio and proband exome sequencing. Variants were classified under ACMG/AMP guidelines. Large CNVs were detected with SNP arrays, and homozygous deletions with an in-house read-depth pipeline. The authors note no homozygous or heterozygous gene-disrupting CNVs were found in the candidate genes, but small heterozygous CNVs cannot be excluded.
- **Results summary:** 127 patients: 81 pathogenic, 38 likely pathogenic, 8 de novo VUS. Inheritance: 103 de novo, 21 likely autosomal dominant with one parent untested, 3 inherited (two ACTL6B biallelic, one ARID1B from a mosaic father).

### ACTL6A, BICRA, SMARCC1 (verbatim portion)
- **ACTL6A:** Three de novo heterozygous missense variants in Patients N1–N3 (c.377C>T, c.1129C>T, c.1165C>T). All three were predicted damaging by CADD. Only N1's row has pLI 1.00 in Table 1.
- **BICRA:** One de novo frameshift, c.2479_2480delinsA (p.Ala827Thrfs*15), in Patient N4. The patient had DD/ID, hypotonia, short stature, and feeding difficulties, and was later included in a separate BICRA case series.
- **SMARCC1:** A nonsense variant in N6 (c.3013C>T, p.Gln1005*) and a frameshift in N7 (c.2463del). Neither was maternal and paternal samples were unavailable. Two exonic deletions were found in an independent CMA cohort of about 70,000 patients (N8, N9). The authors say haploinsufficiency is plausible but a definitive gene-disease link is not established.

The summary of the unread part gives conflicting SMARCC1 counts (one place says four pLoF variants, another says eight pLoF SNVs/indels). I did not rely on it.

### Table rows
The only PBRM1 row is in Table 1, reproduced in the section above. Supplementary Tables 1, 4–8 were not accessible, so I cannot confirm any other PBRM1 entries.

### Caveats
- The Discussion and most of the reference-related content were not read verbatim. Everything I attributed to them (DDD/denovo-db, the trio study, the PBRM1 "compelling evidence" wording) comes from the summary and needs checking against the paper.
- Verify the abstract and Discussion text directly at https://pmc.ncbi.nlm.nih.gov/articles/PMC8957292/ or the publisher DOI, since I could not quote them in full.

Wiley returned HTTP 403, so I'm trying the three fallback URLs you listed.

Europe PMC and Crossref returned the metadata and abstract. The doi.org link redirects to the Wiley host that already returned 403, so I won't follow it. The Europe PMC record lists an open-access full text (PMC13676817), which I'll try for the mouse, behavior, and mechanism details.

I'm stopping here on full text. The Europe PMC article page returned 403, which is a permanent failure under the fetch rules, so I won't try variants of it.

## Report: Duan et al., Advanced Science (DOI 10.1002/advs.78086)

**Sources**
- Wiley (`https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.78086`): **blocked**, HTTP 403.
- Europe PMC REST search (`https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1002/advs.78086%22&format=json&resultType=core`): **worked**, HTTP 200.
- Crossref (`https://api.crossref.org/works/10.1002/advs.78086`): **worked**, HTTP 200.
- doi.org (`https://doi.org/10.1002/advs.78086`): **redirected** (302) to the Wiley URL above. I did not follow it, since Wiley already returned 403.
- Europe PMC article page (`https://europepmc.org/articles/PMC13676817`): **blocked**, HTTP 403. This is the open-access full text, so the full-text sections are not available to me.

**Full citation**
- Authors: Yang-Yang Duan, Lin-Fei Jiao, Pei-Pei Liu, Chun-Hui Duan, Xiao Li, Zi-Han Zhang, Yue-Qi Zhang, Xin-Li Ouyang, Hong-Zhen Du, Sha Liu, Yi Tang, Zhao-Qian Teng, Chang-Mei Liu.
- Journal: Advanced Science (Adv Sci (Weinh)), ISSN 2198-3844.
- Year: 2026. Issue date October 2026 (print publication date 2026-10-01).
- Article number: e78086. Volume and issue are not given in the records I read.
- DOI: 10.1002/advs.78086
- PMID: 42893407
- PMCID: PMC13676817
- Dates: created 2026-10-18; accepted 2026-09-17; received 2026-02-02; published online 2026-10-18.
- License: CC BY 4.0 (open access per Europe PMC).
- Affiliations: Institute of Zoology, Chinese Academy of Sciences, Beijing (corresponding group, with Liu CM as last author); VIB-KU Leuven (Sha Liu); Xuanwu Hospital, Capital Medical University (Yi Tang).

**Abstract (verbatim, from Crossref and Europe PMC; the two records match)**
"The prevalence of autism spectrum disorder (ASD), a heterogeneous neurodevelopmental disorder with limited effective therapeutic drugs, has been rising worldwide. Missense mutations in Polybromo 1 (Pbrm1), a core component of the SWI/SNF (switch/sucrose non-fermentable) chromatin remodeling complex, have been identified as a risk factor for ASD; however, whether PBRM1 loss of function contributes to the pathogenesis remains elusive. Here we provide direct evidence that microglial PBRM1 deficiency leads to altered microglial clusters, excessive neurogenesis, and ASD-like behaviors in mice. Integrated molecular analyses reveal that PBRM1 directly binds to the Ccl5 promoter and represses the expression of CCL5. Elevated CCL5 promotes the proliferation and neuronal differentiation of neural stem/progenitor cells (NSPCs) via the CCR1/5-β-catenin signaling pathway. Importantly, pharmacological blockade of CCR1/5 ameliorates behavioral deficits in Pbrm1 cKO mice. Together, these findings identify a previously unrecognized microglia–NSPC communication mechanism linking PBRM1 dysfunction to aberrant neurodevelopment and suggest the CCL5–CCR1/5 axis as a potential therapeutic target for ASD."

**Keywords (Europe PMC):** Neurogenesis; Autism Spectrum Disorder; Ccl5; Pbrm1; Microglial Homeostasis.

**Items not obtained (full text blocked)**
- Mouse model details (Cre driver, cKO genotype, induction, sex, age): not available. The abstract confirms a conditional knockout ("Pbrm1 cKO mice") and microglial deficiency, but not the driver line.
- Behavioral tests and results: not available. The abstract says only that the pharmacological blockade "ameliorates behavioral deficits."
- Dentate gyrus and neurogenesis markers and cell-type details: not available beyond the abstract's "excessive neurogenesis" and "proliferation and neuronal differentiation of NSPCs."
- Rescue/pharmacology specifics (drug names, doses, route): not available. The abstract confirms "pharmacological blockade of CCR1/5" only.
- Human genetic data on PBRM1 in ASD: not available. The abstract says only that missense mutations in Pbrm1 "have been identified as a risk factor for ASD." The reference list cites a PBRM1 rs2251219 association study in major depressive disorder, not ASD, and I did not verify any ASD cohort.

**Mechanistic sentences the abstract does state**
- "PBRM1 directly binds to the Ccl5 promoter and represses the expression of CCL5."
- "Elevated CCL5 promotes the proliferation and neuronal differentiation of neural stem/progenitor cells (NSPCs) via the CCR1/5-β-catenin signaling pathway."

To get the methods and results, the full text would need to be read from an authenticated or institutional session, or from a copy that is not blocked for automated fetches.

I'll start with the MGI marker page, the Alliance page, IMPC, and SFARI, since none of them depend on each other.

The marker page gave the location, human ortholog, and phenotype summary, but not the allele list. The Alliance page returned only an app shell, and Europe PMC returned HTTP 503. I'll fetch the allele summary, ZFIN, and FlyBase next.

## Pbrm1 model-organism report (partial: several sources failed)

### 1. MGI marker page (https://www.informatics.jax.org/marker/MGI:1923998, read; MGI 6.29, last updated 11/10/2026)
- **Symbol/name:** Pbrm1, "polybromo 1". Synonyms: 2310032M22Rik, 2610016F04Rik, BAF180, Pb1. NCBI Gene 66923.
- **Mouse location:** Chr14:30741095-30843549 bp, + strand (GRCm39). Genetic map: Chromosome 14, 19.09 cM, cytoband B.
- **Human ortholog:** PBRM1, polybromo 1. HGNC:30064, NCBI Gene 55193, UniProt Q86U86. Located at 3p21.1, chr3:52544735-52685966 (-) on GRCh38.
- **Vertebrate orthologs listed:** 1 human, 1 mouse, 1 rat, 2 zebrafish.
- **Human disease associations (MGI):** 4 — extrahepatic bile duct adenocarcinoma (DOID:3495), lung non-small cell carcinoma (DOID:3908), lung small cell carcinoma (DOID:5409), renal cell carcinoma (DOID:4450).
- **Allele counts, not allele list:** 40 total: 1 Chemically induced (ENU), 5 Endonuclease-mediated, 29 Gene trapped, 5 Targeted. The page gives 92 IMSR strains or lines.
- **Phenotype summary:** 18 phenotypes from 3 alleles in 3 genetic backgrounds, from 33 phenotype references. The page's summary text says "homozygous null mice display embryonic lethality with hypoplastic cardiac ventricular chambers and malformation of the placenta" (paraphrased here to respect quote limits).
- **Latest phenotype reference:** J:391376, Li J et al., "Loss of PBRM1 accelerates pancreatic cancer progression…", Cancer Lett 2026 Aug 22. Abstract not retrieved.

### 2. MGI allele summary (https://www.informatics.jax.org/allele/summary?markerId=MGI:1923998, read)
The page loaded only the search header; the allele table did not render. **No allele symbols or MGI allele IDs (MGI:xxxxxxx) were retrieved.** The counts above come from the marker page. To get the list, the MGI allele export (Text/Excel link on the summary page) or the marker's allele table would need to be read directly.

### 3. Alliance Genome page (https://www.alliancegenome.org/gene/MGI:1923998)
Returned a 29-character app shell with no content. **Phenotypes (MP terms) and disease associations were not retrieved.**

### 4. IMPC (https://www.mousephenotype.org/data/genes/MGI:1923998, read; Data Release 25.0)
- Physiological systems: 20 of 24 tested. Systems listed as "Significantly impacted by the knock-out": Nervous system; Behavior/neurological; Mortality/aging; Hematopoietic system. 16 systems listed as no significant impact; 4 not tested.
- Gene metrics: "4 Significant phenotypes", "2 Associated diseases".
- **Inconsistency:** the phenotype table itself shows "Significant Phenotypes (0)" and did not render any rows. The 4 significant systems therefore lack parameter-level detail, allele, zygosity, or p-value.
- Viability and body-weight data are linked but were not fetched.
- Nothing about IMPC viability status was stated in the page text. The MGI summary above points to embryonic lethality for homozygous nulls.

### 5. Europe PMC searches (not retrieved)
The Europe PMC REST query (Baf180 AND (heart OR cardiac) AND mouse) returned **HTTP 503 Service Unavailable** with no Retry-After. That is a permanent failure under my rules, so I did not retry it or try other Europe PMC queries. **No abstracts were retrieved** for Wang Z 2004, Huang X 2008, Gu YF 2017, Nargund AM 2017, Espana-Agusti J 2017, PMC4991371, or any neural/brain query. Re-sending the same URL will likely fail the same way; the Europe PMC host should be checked later.

### 6. Zebrafish and Drosophila
- **ZFIN:** The MGI page links ZFIN gene ZDB-GENE-080926-4 for pbrm1. I then fetched a path I built myself (…/ZDB-GENE-080926-4/phenotype), which returned **HTTP 404**. That was a variant I constructed after the link, so I should not have tried it. The ZDB-GENE ID is from the MGI page, but no ZFIN phenotype, morpholino, or allele data was retrieved. The ZFIN expression link on the MGI page (…/expression) was not fetched.
- **FlyBase:** I fetched https://flybase.org/reports/FBgn0023210, an FBgn ID I supplied from memory and did not verify. The page returned only a HitList shell with no gene record, so **it does not show that this is polybromo, and no Drosophila phenotype or allele data was retrieved.** A verified polybromo FBgn would need to come from a FlyBase search or the Alliance page.

### 7. SFARI Gene (https://gene.sfari.org/database/human-gene/PBRM1, read)
The page states: "PBRM1 is not in the SFARI:Gene database". So there is no SFARI score (1, 2, 3, S, or none). Release shown: 2026 Q2.

### Could not retrieve
- Alliance gene page (JS shell): MP phenotypes, DO associations
- MGI allele symbols and MGI allele IDs
- Europe PMC: all abstracts, including the mechanistic claims the caller asked for verbatim
- ZFIN phenotype data (404 on the constructed URL)
- FlyBase polybromo data (unverified ID, no gene content)

No file paths were involved in this task.

## ClinVar PBRM1 via E-utilities: results and flags

**Main flag:** the classification counts in steps 2 to 3 are not reliable. The `[Clinical Significance]` field tag was silently translated to `[All Fields]`, so those queries matched any ClinVar record mentioning the word anywhere. The sample in step 5 confirms this: it included a "Likely benign" record.

### 1. Total ClinVar records for PBRM1
- `PBRM1[gene]`: **count = 180** (query translation: `PBRM1[gene]`)

### 2 and 3. Classification counts (as returned, with the caveat above)

| Query term | Count | Query translation |
|---|---|---|
| "pathogenic" | 18 | `PBRM1[gene] AND "pathogenic"[All Fields]` |
| "likely pathogenic" | 1 | `PBRM1[gene] AND "likely pathogenic"[All Fields]` |
| "uncertain significance" | 99 | `PBRM1[gene] AND "uncertain significance"[All Fields]` |
| "benign" | 94 | `PBRM1[gene] AND "benign"[All Fields]` |

The `errorlist` was empty for these queries, so ClinVar did not flag the tag as invalid. Its translation shows `[All Fields]`, which is why the counts are unreliable. The pathogenic OR likely-pathogenic query also returned 18, the same as "pathogenic" alone. A reliable tally would need the `germline_classification.description` field from esummary for all 180 IDs, which I did not fetch.

### 4. Germline filter
- `PBRM1[gene] AND "germline"[prop]`: **count = 0**. The `[prop]` tag is not valid; `errorlist.phrasesnotfound` contains `germline[prop]`.

### 5. Sample records (pathogenic OR likely pathogenic, retmax=20)
- ESearch returned 18 IDs in total: 4682581, 4298856, 4298852, 4298833, 4298832, 4298829, 4288304, 3764511, 3391879, 3062680, 687764, 625696, 442401, 442400, 253632, 218955, 155564, 57771.
- The ESummary response was truncated. I read only the first 8 records in full detail. Records 442400 onward were not read, so I cannot report them.
- Records read:
  - **4682581**: copy number gain, GRCh37 3p26.3-14.3 (x3), a large region rather than a PBRM1-specific variant. Germline: Pathogenic, "criteria provided, single submitter", condition "not provided".
  - **4298856**: NM_001405607.1(PBRM1):c.900-220G>T, intron variant. No germline classification block; 1 SCV.
  - **4298852**: NM_001405607.1(PBRM1):c.996-5T>A, intron variant. No germline classification block; 8 SCVs.
  - **4298833**: NM_001405607.1(PBRM1):c.3169-60G>T, intron variant. No germline classification block; 4 SCVs.
  - **4298832**: NM_001405607.1(PBRM1):c.3169-59A>T, intron variant. No germline classification block; 5 SCVs.
  - **4298829**: NM_001405607.1(PBRM1):c.3598C>A (p.Arg1200=), synonymous. Details were cut off in the page text.
  - **4288304**: Deletion, NM_001405607.1(PBRM1):c.4942+2_4942+3del, frameshift and splice donor. No germline description or trait listed.
  - **3764511**: NM_001405607.1(PBRM1):c.3997G>A (p.Glu1333Lys), missense. **Germline: Likely benign** (2025/02/04, "criteria provided, single submitter"). Trait: "Hereditary cancer". This record does not belong in a pathogenic/likely-pathogenic search, which confirms the tag problem.
- Other records in that visible range:
  - **3391879**: copy number loss, GRCh37 3p21.2-21.1. Pathogenic, "criteria provided, single submitter". Trait "not provided".
  - **3062680**: copy number loss, GRCh37 3p21.2-14.2. Pathogenic. Trait "not specified".
  - **687764**: copy number loss, GRCh37 3p21.2-21.1. Pathogenic, "no assertion criteria provided". Trait "not provided".
  - **625696**: copy number gain, GRCh37 3p21.31-21.1. Pathogenic. Trait "not provided".
  - **442401**: copy number gain, GRCh37 3p26.3-q29 (whole-arm). Pathogenic, "no assertion criteria provided". Trait "See cases".
- **Conditions and review status:** the condition names are "not provided", "not specified", "See cases", and "Hereditary cancer" (the last one on the likely-benign record). I did not see any cancer-specific condition attached to a pathogenic PBRM1 SNV in this sample. Several records show a placeholder `last_evaluated` of "1/01/01 00:00".

### 6. NCBI Gene record 55193 (PBRM1)
- Official symbol and name: PBRM1, "polybromo 1". Chromosome 3, map location **3p21.1**, 39 exons, RefSeq chromosome NC_000003.12.
- Other aliases: BAF180, PB1, RCC, SMARCH1. OMIM: 606083.
- **Summary (RefSeq, Feb 2012), not verbatim:** the summary contains two sentences, quoted here as allowed for non-preapproved sources. The first sentence reads "This locus encodes a subunit of ATP-dependent chromatin-remodeling complexes." The second reads "Mutations at this locus have been associated with primary clear cell renal cell carcinoma." The rest of the summary (about the encoded protein and nuclear hormone receptor complexes) is paraphrased rather than quoted, because of the 125-character limit on quotes from this source. The full text is available at the Gene record for 55193.

### 7. MedGen search for PBRM1
- Search `db=medgen&term=PBRM1`: count 3.
- Concepts (titles and CUIs as returned):
  - **1805915**: "PBRM1 Gene Mutation", conceptid **C5670648**. Defined as a change in the nucleotide sequence of the PBRM1 gene.
  - **989976**: "PBRM1-related BAFopathy", conceptid **CN306939** (MONDO_0700122). Defined as a BAFopathy caused by a PBRM1 mutation.
  - **449382**: "Nonpapillary renal cell carcinoma", conceptid **CN074294**. Lists PBRM1 among its associated genes; the record also includes a long definition that I did not reproduce.
- Whether these are the CUIs you need depends on the use. The first two are PBRM1-specific concepts. The third is a broader renal cell carcinoma concept that lists PBRM1 as an associated gene.

### Failures and gaps
- Steps 2 and 3 used a field tag that was silently remapped, so those counts should not be treated as classification totals.
- Step 4 returned 0 because `[prop]` is not a valid filter.
- Step 5 was truncated at 8 of 18 records, and the first record in the visible page was also cut mid-record.
- Step 6 summary was reported partly paraphrased because of the source quote limit.
- No HTTP errors or rate limits occurred.

### URLs read
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=clinvar&term=PBRM1%5Bgene%5D&retmax=0&retmode=json
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=clinvar&term=PBRM1%5Bgene%5D+AND+%22pathogenic%22%5BClinical+Significance%5D&retmax=0&retmode=json
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=clinvar&term=PBRM1%5Bgene%5D+AND+%22likely+pathogenic%22%5BClinical+Significance%5D&retmax=0&retmode=json
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=clinvar&term=PBRM1%5Bgene%5D+AND+%22uncertain+significance%22%5BClinical+Significance%5D&retmax=0&retmode=json
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=clinvar&term=PBRM1%5Bgene%5D+AND+%22benign%22%5BClinical+Significance%5D&retmax=0&retmode=json
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=clinvar&term=PBRM1%5Bgene%5D+AND+%22germline%22%5Bprop%5D&retmax=0&retmode=json
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=clinvar&term=PBRM1%5Bgene%5D+AND+%28%22pathogenic%22%5BClinical+Significance%5D+OR+%22likely+pathogenic%22%5BClinical+Significance%5D%29&retmax=20&retmode=json
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=clinvar&id=4682581,4298856,4298852,4298833,4298832,4298829,4288304,3764511,3391879,3062680,687764,625696,442401,442400,253632,218955,155564,57771&retmode=json (read up to about 40,000 of 283,531 characters, then a model-extracted summary of the rest)
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&id=55193&retmode=json
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=medgen&term=PBRM1&retmode=json
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=medgen&id=1805915,989976,449382&retmode=json

I could not get the curator-level details for PBRM1 from the HTML page. The only PBRM1 data came from the PanelApp JSON API.

**HTML page** (https://panelapp.genomicsengland.co.uk/panels/285/gene/PBRM1/, HTTP 200)
- I read it twice, the second time from character offset 39930. Both reads returned only the page's "Genes in panel" sidebar, an alphabetical list of gene symbols with numbers. The page is truncated and the rest is summarised.
- Not found on the page: the confidence rating, mode of inheritance, curator comments or evidence reviews (no dates or authors), the sources list, phenotypes with OMIM/Mondo IDs, and the panel version and date. The sidebar numbers are not labelled, so I cannot tell what they mean.
- The gene-detail content is probably loaded by JavaScript, so a plain fetch does not see it.

**PanelApp API v1** (https://panelapp.genomicsengland.co.uk/api/v1/genes/PBRM1/, HTTP 200, browsable HTML view of the JSON)
- Result count: 1. Only one panel is listed for PBRM1:
  - Panel: id 285, name "Intellectual disability", status "public", version "11.97", version_created "2026-11-12T18:40:48.976954Z".
  - `confidence_level`: "1"
  - `evidence`: ["Expert Review Red"]
  - `mode_of_inheritance`: "" (empty)
  - `phenotypes`: [] (empty)
  - `mode_of_pathogenicity`: "" (empty)
  - `penetrance`: "Complete"
  - `publications`: [] and `tags`: []
  - `transcript`: null
- The evidence string reads "Expert Review Red", so the rating is Red. The page does not say how the numeric `confidence_level` maps to colours, so I cannot confirm that "1" means Red from the page itself.
- The panel's `relevant_disorders` list includes "Intellectual disability - microarray and sequencing", the panel name you gave. The panel's own `name` field is just "Intellectual disability".
- Gene identifiers from the same record: HGNC:30064, OMIM gene 606083, Ensembl ENSG00000163939. Aliases: BAF180, PB1. GRCh38 location: 3:52545352-52685917.

**PanelApp Australia API** (https://panelapp-aus.org/api/v1/genes/PBRM1/)
- HTTP 403 Forbidden, response body not retrieved. This is a permanent refusal, so retrying the URL would fail the same way. I did not try other variants.

Not fetched: the gene-level pages for other panels, since none were listed.

The Europe PMC request timed out, which is one of the failures worth a single retry. I'll retry that same URL once.

The Europe PMC result was truncated, and the summary paraphrased the PBAF structure paper (Wang 2022) rather than quoting it. That is the key structural record, so I'll run one targeted search to verify its metadata.

I'll run the seven Europe PMC queries in parallel.

## Europe PMC results for PBRM1 queries

**Verbatim abstracts are not included.** The Europe PMC responses came from a non-preapproved source, so I can only quote up to 125 characters at a time. The abstracts below are paraphrased, with identifiers and metadata from the JSON.

### Fetch status

| # | URL (query) | Result |
|---|---|---|
| 1 | `PBRM1 AND "neurodevelopmental"`, pageSize 25 | HTTP 503 Service Unavailable. Not retried. Resending it would likely fail the same way. |
| 2 | `PBRM1 AND BAFopathy`, pageSize 25 | HTTP 503 Service Unavailable. Not retried. Resending it would likely fail the same way. |
| 3 | `EXT_ID:34906496` | HTTP 200, complete JSON, hitCount 1. |
| 4 | `PBRM1 AND autism`, pageSize 25 | HTTP 200, but truncated. The raw JSON shows `"hitCount":144`. Two of three chunks were not read verbatim; see the end of this report. |

### 1. PMID 34906496 (requested as "Machol et al.")

The record is not by Machol et al. The first author is Chen CA and the last author is Yuan B.

- **Title:** Retrospective analysis of a clinical exome sequencing cohort reveals the mutational spectrum and identifies candidate disease-associated loci for BAFopathies.
- **Authors:** Chen CA … Yuan B (first and last author as listed)
- **Journal:** Genetics in Medicine, vol 24, issue 2, pp 364-373 (Genet Med)
- **Year:** 2022 (published online 2021-11-30)
- **PMID:** 34906496
- **PMCID:** PMC8957292
- **DOI:** 10.1016/j.gim.2021.09.017
- **Abstract (paraphrase):** The authors reviewed exome sequencing data from 16,243 patients, focusing on BAF complex genes. They found 127 patients with pathogenic, likely pathogenic, or de novo variants of unknown significance in 11 known BAFopathy genes. They also reported de novo or predicted loss-of-function variants in four candidate genes, including PBRM1. They conclude that a genotype-driven reanalysis supports new candidate genes, and that further study is needed to confirm them.
- **Short quote:** "a group of neurodevelopmental disorders with extensive locus and phenotypic heterogeneity" (from the Background section)

This is the only PBRM1-relevant paper with a human germline finding that I could read in full.

### 2. PBRM1 and autism (query 4)

**a) PMID 42893407**
- **Title:** PBRM1 Deficiency in Microglia Leads to Excessive Neurogenesis and Autism-Like Behaviors via the CCL5-CCR1/5-β-catenin Signaling Axis.
- **Authors:** Duan YY … Liu CM
- **Journal:** Advanced Science (Adv Sci, Weinh), 2026 (Oct)
- **PMID:** 42893407 | **PMCID:** PMC13676817 | **DOI:** 10.1002/advs.78086
- **Abstract (paraphrase, read verbatim in the JSON):** The authors note that PBRM1 missense mutations have been linked to autism risk, but whether loss of PBRM1 function causes disease was unknown. In mice, microglial PBRM1 deficiency altered microglial clusters, increased neurogenesis, and produced autism-like behaviors. PBRM1 binds the Ccl5 promoter and represses CCL5. CCL5 then promotes proliferation and neuronal differentiation of neural progenitors through CCR1/5-β-catenin signaling. Blocking CCR1/5 improved behavior in Pbrm1 conditional knockout mice.
- **Note:** This is a mouse study, not a human germline variant study.

**b) PMID 41390837 (peripheral)**
- **Title:** Cell type-specific functions of the PBAF chromatin-remodeling complex in neuronal diversification.
- **Authors:** Osuma A … Kratsios P
- **Journal:** Nature Communications, vol 17, 2025 (Dec)
- **PMID:** 41390837 | **PMCID:** PMC12820340 | **DOI:** 10.1038/s41467-025-67434-9
- **Abstract (paraphrase):** This C. elegans study describes PBAF functions in motor neuron identity and says BAF and PBAF mutations cause neurodevelopmental conditions. It is not PBRM1-specific.

### 3. Other records seen in the truncated JSON (verbatim part)

- **PMID 41692879:** Azieva A … Marakhonov A, "Cooperation of Transcription Factor PAX6 with Chromatin-Remodeling Complex BAF During Embryonic Development in Mammals." Cell Mol Neurobiol 2026. DOI 10.1007/s10571-026-01692-z, PMCID PMC12988092. Abstract was cut off in the fetch. Not PBRM1-specific.
- **PMID 33811077:** Karki M … Tripathi DN, "A cytoskeletal function for PBRM1 reading methylated microtubules." Sci Adv 2021. DOI 10.1126/sciadv.abf2866, PMCID PMC11059954. This is PBRM1 biology in cancer and cell-cycle contexts, not neurodevelopment. Its abstract describes PBRM1 binding SETD2 methyl marks on microtubules and says this is needed for normal mitosis.

### 4. Other records from the model-extracted summary (unverified)

The summary covers parts of the response I did not read verbatim, so treat these as leads only. Confirm them before relying on them.

- **PMID 37500730:** Valencia AM and Kadoch C, "Landscape of mSWI/SNF chromatin remodeling complex perturbations in neurodevelopmental disorders." Nat Genet 2023. PMCID PMC10412456, DOI 10.1038/s41588-023-01451-6. This is likely the most relevant BAFopathy-type review in the set.
- Several other records in the summary were not PBRM1-specific. These include reviews of chromatin remodelers, an ASD review of RNA-binding proteins, and a ZMIZ1 review that mentions ASD. None of them were confirmed verbatim.

### Coverage and limits

- **Exhaustive listing is not possible from these responses.** Queries 1 and 2 returned 503 errors, so I have no hit counts or records for them. Query 4 reports 144 hits, but I read only about 40 percent of the response verbatim, so most hits are unlisted.
- **Full abstracts were not reproduced verbatim** because of the source restrictions above.
- **Endpoints not reached:** The JSON for query 4 has a `nextCursorMark` value. I did not follow it because it was not in the verbatim text I read.
- **Suggested next step:** Retry queries 1 and 2 later, or use the Europe PMC web interface for them. Then fetch full abstracts for specific PMIDs (for example, 42893407 or 34906496). Open-access full texts are linked from the records (PMC13676817 and PMC8957292).

Three queries timed out (queries 2, 4 and 5), so I'll retry each once. I'm also running exact-title searches for the three papers that haven't appeared yet.

## PBRM1 in cancer: Europe PMC research report

**Important limit on verbatim text:** Europe PMC pages came back as non-preapproved sources, so I can quote only short fragments (125 characters or fewer) and must paraphrase the rest. I could not reproduce the full abstracts verbatim. The full text is at the DOIs below.

### Fetch failures
- **Germline PBRM1 search** (Europe PMC, query "PBRM1 germline AND cancer"): HTTP 503, no Retry-After. Permanent per my rules, so I did not retry. **Germline PBRM1 evidence is therefore unretrieved**, including the breast cancer susceptibility query.
- **Miao follow-up search** (Europe PMC, PBRM1 with immunotherapy and kidney terms): HTTP 503, no Retry-After. Not retried. **Later confirmation or refutation is unretrieved.**
- **Other-tumour search** (Europe PMC, PBRM1 with cholangiocarcinoma, mesothelioma, bladder, meningioma and mutation): first attempt timed out, retry succeeded. Results were partly truncated and partly model-summarized.
- **cBioPortal**: an endpoint I tried returned HTTP 404 (not retried). **No cBioPortal or COSMIC mutation frequency was retrieved.**

### 1. Varela et al., Nature 2011 (ccRCC)
- Title: "Exome sequencing identifies frequent mutation of the SWI/SNF complex gene PBRM1 in renal carcinoma."
- Nature 2011; 469(7331): 539-542. PMID 21248752. DOI 10.1038/nature09639. PMC3030920 (open access). Erratum: Nature 2012; 484(7392): 130.
- Abstract, short quote: PBRM1 is identified "as a second major ccRCC cancer gene, with truncating mutations in 41% (92/227) of cases."
- **Confirmed frequency: 41% (92/227) of exome-sequenced ccRCC cases had truncating PBRM1 mutations.** Your ~40% estimate matches.
- Paraphrase: the authors sequenced the protein-coding exome of a primary ccRCC series, found PBRM1 (a SWI/SNF chromatin-remodelling gene) as the second major ccRCC cancer gene after VHL, and noted that UTX, JARID1C and SETD2 together cover fewer than 15% of ccRCC.
- Cited by 1,016 (Europe PMC record, retrieved 2026-11-18).

### 2. Germline PBRM1 and cancer predisposition
- **Not retrieved** because of the 503 failure described above. I cannot report on any PBRM1 germline syndrome or susceptibility evidence from this session.
- Related but not PBRM1-specific: Lu W et al., Sci Rep 2026 (PMID 42259884, DOI 10.1038/s41598-026-56230-0) reports "Germline variants were detected in 7.0% (18/258)" of biliary tract cancer patients. It does not name PBRM1 as a germline finding.

### 3. PBRM1 in other tumours
- **Cholangiocarcinoma (CCA):** Lu W et al., Sci Rep 2026 (PMID 42259884): PBRM1 mutations were "10.1% vs. 0%, P = 0.003" in CCA versus gallbladder cancer. In an MSKCC external cohort, PBRM1 mutations were associated with improved survival (HR 0.50, P = 0.02). Shi J et al., Mod Pathol 2026 (PMID 42660428, DOI 10.1016/j.modpat.2026.101078) notes PBRM1 as a characteristic CCA alteration, but gives no frequency in the visible text.
- **Sarcomatoid carcinoma of the upper urinary tract:** Jaime-Casas S et al., Cancers 2026; 18(14): 2352 (PMID 42512413, DOI 10.3390/cancers18142352). In 121 sarcomatoid cases, PBRM1 was 12% and was enriched versus conventional UTUC (all p < 0.05). Their conclusion mentions "enrichment in NF2, SETD2, PBRM1, and PTEN."
- **Bladder/urothelial:** no PBRM1-specific frequency was retrieved from abstract text. One model-summarized (not verbatim) result, Zhang J et al., Front Immunol 2025 (PMID 41438758, DOI 10.3389/fimmu.2025.1708324), reports SWI/SNF alterations in 42.8% of urothelial bladder cancers, with PBRM1 among the top genes. That is not a PBRM1-only frequency, and I did not verify the figure against the source.
- **Mesothelioma:** the 2026 abstracts retrieved (Samuels M, Life 2026, PMID 41900904; Bader JM, NPJ Precis Oncol 2026, PMID 42426379) were not read for PBRM1 frequency. **No mesothelioma PBRM1 frequency retrieved.**
- **Meningioma:** only case-level evidence. Reusch E et al., Front Oncol 2025 (PMID 41199851, DOI 10.3389/fonc.2025.1587752) describes a grade 2 meningioma with "PBRM1 and BAP1 functional loss" and a prolonged response to pembrolizumab. No population frequency was retrieved.
- **Cholangiocarcinoma case:** Pedregal M, NPJ Precis Oncol 2025 (PMID 41136536, DOI 10.1038/s41698-025-01113-2) reports a PBRM1-mutant metastatic CCA responding to tazemetostat. This is a single patient, taken from the model-summarized portion.

### 4. Miao et al., Science 2018 (PBRM1 loss and immune checkpoint response)
- Title: "Genomic correlates of response to immune checkpoint therapies in clear cell renal cell carcinoma."
- Science 2018; 359(6377): 801-806. PMID 29301960. DOI 10.1126/science.aan5951. PMC6035749 (free).
- Short quotes: "clinical benefit was associated with loss-of-function mutations in the PBRM1 gene (P = 0.012)" and "We confirmed this finding in an independent validation cohort of 63 ccRCC patients" (P = 0.0071 in the validation cohort).
- Design: whole-exome sequencing of 35 metastatic ccRCC patients on anti-PD-1 monotherapy, then a validation cohort of 63 patients treated with PD-1 or PD-L1 blockade, alone or with anti-CTLA-4. Gene-expression work on PBRM1-deficient tumours and cell lines pointed to JAK-STAT, hypoxia and immune signalling.
- Three Science and Nature journal comments on the paper are listed in the record (PMIDs 29355171, 29358781, 29449480). They are commentaries, not replication studies.
- **Confirmation or refutation by later studies: not retrieved.** The follow-up search failed.

### 5. COSMIC and cBioPortal
- **Not retrieved.** The cBioPortal endpoint returned 404. COSMIC was not accessed.

### Items I could not verify in full
- Bader JM 2026, Pedregal M 2025 and the Zhang J 2025 bladder figure come from the model-summarized part of the search result. Their details are not verbatim.
- The Oncol Rep 2026 PBRM1 knockdown study (Zhang D, PMID 42885299, DOI 10.3892/or.2026.9212) reports no mutation frequency. It is a mechanistic study in HCCC-9810 cells.

### URLs read
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:21248752%20AND%20SRC:MED&format=json&resultType=core
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:29301960%20AND%20SRC:MED&format=json&resultType=core
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PBRM1%20AND%20(cholangiocarcinoma%20OR%20mesothelioma%20OR%20bladder%20OR%20meningioma)%20AND%20mutation&format=json&resultType=core&pageSize=25
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PBRM1%20AND%20(bladder%20OR%20urothelial)%20AND%20(mutation%20OR%20frequency)&format=json&resultType=core&pageSize=10

## PBRM1 (UniProt Q86U86) protein-level report

**Source caveat:** The UniProt JSON came back truncated (39,938 of 120,983 characters). Everything marked "verbatim" below is from the raw text that did arrive. Items marked "summary" come from a model-extracted summary of the unread remainder and should be checked. The copyright rule limits quotes from these non-preapproved sources to 125 characters, so the longer comments are paraphrased with short quoted fragments.

### 1. UniProt entry (Q86U86, PB1_HUMAN, reviewed Swiss-Prot)
- **Recommended name:** "Protein polybromo-1" (short name hPB1). Alternative names: "BRG1-associated factor 180" (BAF180) and "Polybromo-1D". Gene PBRM1, synonyms BAF180 and PB1.
- **Length:** 1,689 aa (Chain 1–1689, verbatim). Isoforms: 9 listed in the entry.
- **Entry version:** 199. Last annotation update 2026-11-04. Sequence version 1 (2003-06-01). Protein existence level 1.
- **Subcellular location:** Nucleus (SL-0191), citing PMID 25593309.
- **Tissue specificity:** "Widely expressed" (PMID 12487023).

### 2. Function (paraphrased, short verbatim fragments)
UniProt says PBRM1 is involved in transcriptional activation and repression of select genes through chromatin remodeling (altering DNA–nucleosome topology). It is required for the stability of the SWI/SNF-B (PBAF) complex and acts as a negative regulator of cell proliferation.

### 3. Subunit / complex (paraphrased)
UniProt places PBRM1 in the SWI/SNF-B (PBAF) complex. Listed members are SMARCA4/BRG1, SMARCB1/BAF47/SNF5, ACTL6A/BAF53A or ACTL6B/BAF53B, SMARCE1/BAF57, SMARCD1/BAF60A, SMARCD2/BAF60B, perhaps SMARCD3/BAF60C, SMARCC1/BAF155, SMARCC2/BAF170, ARID2/BAF200, and actin. The entry also says it interacts with acetylated H3K14 (H3K14ac). Binary interactions with IntAct experiment counts (verbatim): ARID2 (5), SMARCA4 (7), CHD7 (4), BRD1 (2), HIV-1 Tat (2).

### 4. Domains and regions (verbatim coordinates)
- **Bromodomains (6):** Bromo 1 41–151; Bromo 2 177–287; Bromo 3 381–487; Bromo 4 518–625; Bromo 5 653–763; Bromo 6 769–879.
- **BAH domains (2):** BAH 1 956–1074; BAH 2 1156–1272.
- **HMG box (DNA binding):** 1379–1447.
- **Disordered regions:** 1–39; 155–177; 487–517; 625–646; 902–941; 1106–1133; 1354–1378; 1431–1460.
- No Repeat, Zinc finger, or Motif features appeared in the retrieved text.

### 5. PTMs (verbatim, from the retrieved part)
- **Phosphorylation (phosphoserine unless noted):** Ser10, Ser39, Ser131, Tyr134 (phosphotyrosine), Ser178, Ser316, Ser319, Ser353, Ser355, Ser371, Ser375, Ser498, Ser509, Ser636, Ser648, Ser689, Ser948, Ser987, Ser1119, Ser1405, Ser1453. Tyr1289 is phosphotyrosine, inferred from Mouse Q8BSQ9.
- **Acetylation:** N6-acetyllysine at Lys414 (inferred from Mouse Q8BSQ9).
- **SUMO2 Lys-Gly cross-links:** 96, 154, 210, 425, 471, 511, 591, 638, 653, 1106, 1111, 1167, 1293 (also SUMO1), 1308, 1398, 1642, 1654, 1656.

### 6. Disease
- **Renal cell carcinoma** (DI-02254, MIM 144700), with the note that the disease is caused by variants affecting this gene. Evidence is PMID 21248752.
- The retrieved natural variants include somatic changes found in clear cell renal carcinoma at residues 57, 232, 540, 597, 621, 661, 674, and 1204. Also present are variants in cancer cell lines. The variant list was truncated after residue 1204.

### 7. Cross-references
- **Verbatim:** Swiss-Prot EMBL-style IDs were not fully retrieved. The Reactome entity is R-HSA-389254 (PBRM1, ReferenceGeneProduct, referenceIdentifier Q86U86). The GO term list is in section 8.
- **Summary only (not verified verbatim):**
  - **PDB (30):** 2KTB, 3G0J, 3HMF, 3IU5, 3IU6, 3K2J, 3LJW, 3MB4, 3TLP, 4Q0N, 4Q0O, 4Y03, 5E7D, 5FH6, 5FH7, 5FH8, 5HRV, 5HRW, 5HRX, 5II1, 5II2, 5IID, 6OXB, 6ZN6, 6ZNV, 6ZS3, 6ZS4, 7VDV, 7Y8R, 8FTA.
  - **Pfam:** PF01426 (BAH), PF00439 (bromodomain), PF00505 (HMG_box).
  - **InterPro:** IPR001025 (BAH), IPR001487 (bromodomain), IPR043151, IPR036427, IPR018359, IPR009071, IPR036910, IPR037968, IPR037382.
  - **Reactome (from UniProt cross-refs):** R-HSA-3214858, R-HSA-8939243, R-HSA-9932451, R-HSA-9933939. The Reactome search below did not return R-HSA-9933939, so these four are unverified.

### 8. GO annotations (QuickGO, verbatim IDs and evidence; 44 annotations, 23 distinct terms)
QuickGO returned null for term names. Names below come from the UniProt summary, except where noted.

**Molecular function**
- GO:0003682 chromatin binding: IEA (InterPro), IBA (GO_Central), NAS (PMID 11078522).
- GO:0005515 protein binding (name not in retrieved text): 10 IPI annotations from IntAct, from PMIDs 11780067, 12368262, 15985610, 20130577, 22140357, 27142060, and 35271311.

**Biological process**
- GO:0000278 mitotic cell cycle: TAS (PMID 11078522)
- GO:0006338 chromatin remodeling: IEA, IBA, NAS (ComplexPortal, PMID 10078207), TAS
- GO:0006357 regulation of transcription by RNA polymerase II: NAS (ComplexPortal, PMID 18809673)
- GO:0008285 negative regulation of cell population proliferation: IMP (PMID 21248752)
- GO:0030071 regulation of mitotic metaphase/anaphase transition: NAS (PMID 25066234)
- GO:0045582 positive regulation of T cell differentiation: NAS (PMID 12110891)
- GO:0045597 positive regulation of cell differentiation: NAS (PMID 11790558)
- GO:0045663 positive regulation of myoblast differentiation: NAS (PMID 15985610)
- GO:0070316 regulation of G0 to G1 transition: NAS (PMID 11790558)
- GO:2000045 regulation of G1/S transition of mitotic cell cycle: NAS (PMID 10778858)
- GO:2000781 positive regulation of double-strand break repair: NAS (PMID 25066234)
- GO:2000819 regulation of nucleotide-excision repair: NAS (PMID 12215535)
- GO:0006357 and the other ComplexPortal-sourced annotations are NAS, ECO:0005547.

**Cellular component**
- GO:0000228 nuclear chromosome: NAS (PMID 11078522)
- GO:0000776 kinetochore: NAS (PMID 11078522)
- GO:0000785 chromatin: NAS (PMID 12192000)
- GO:0005634 nucleus: IDA (PMID 25593309), NAS (PMIDs 22952240, 26601204), IEA (SL-0191)
- GO:0005654 nucleoplasm: IDA (HPA), TAS (Reactome R-HSA-9933237)
- GO:0005694 chromosome (name not in retrieved text): IEA (ARBA)
- GO:0016363 nuclear matrix: NAS (PMID 9128241)
- GO:0016514 SWI/SNF complex: IDA (PMID 8895581), IBA
- GO:0016586 RSC-type complex: NAS (PMID 8804307), IBA, IEA

### 9. Reactome search (R-HSA, five matches)
- **R-HSA-389254**: PBRM1 (protein, nucleoplasm)
- **R-HSA-9932829**: PBRM1 ATPase complex (complex)
- **R-HSA-9933237**: PBRM1-containing ATPase complex binds SMARCC dimer:SMARCDs:SMARCE1:SMARCB1:ARID2:BRD&:PHF10 (reaction). The summation says cryo-EM studies (Yuan et al 2022; Wang et al 2022) place PBRM1 in a BRD7:PHF10:PBRM1 module. The Yuan 2022 paper was not retrieved.
- **R-HSA-9824981**: MITF-M and the SWI/SNF complex bind the TYR promoter (reaction; cites PBAF with PBRM1 in 501MEL cells, Laurette et al 2015)
- **R-HSA-9988507**: PHF6 binds SWI/SNF complexes (reaction; PHF6 associates with PBRM1)

### 10. Europe PMC cryo-EM literature
The first query ("cryo-EM" AND "PBAF") returned hitCount **92**. I read only the first ~40,000 characters of that response, and the summary of the rest was not verified. Abstract text is paraphrased, with only short quotes.

- **Wang L et al., Nat Commun 2022.** "Structure of nucleosome-bound human PBAF complex." PMID **36496390**, DOI **10.1038/s41467-022-34859-5**, published 2022-12. Preprint: bioRxiv PPR496460, DOI 10.1101/2022.05.20.492795 (2022).
  - Abstract, paraphrased: the authors solved the cryo-EM structure of a 13-subunit human PBAF complex bound to an acetylated nucleosome. Four PBAF-specific subunits and nine shared subunits form a PBAF-specific architecture. The structure shows six histone-binding and four DNA-binding modules.
  - Short quote: "Here we determined structure of 13-subunit human PBAF in complex with acetylated nucleosome". The abstract does not name PBRM1.
- **Ma S et al., Sci Adv 2026.** PMID 42748234, DOI 10.1126/sciadv.aei0972, published 2026-09. Cryo-EM of SWI/SNF and RSC from the fungus *Chaetomium thermophilum*. Not human, and no PBRM1 placement.
- **Sun F et al., Nucleic Acids Res 2026.** PMID 41657245, DOI 10.1093/nar/gkag092, published 2026-02. Cryo-EM of ncBAF bound to a nucleosome (BCL7B). Does not concern PBAF or PBRM1.
- **Xu W et al., J Mol Cell Biol 2026.** PMID 42377898, DOI 10.1093/jmcb/mjag020, published 2026-06. Cryo-EM of ncBAF bound to a nucleosome. Its abstract contrasts ncBAF with the canonical nucleosome-binding module of cBAF and PBAF.
- **Martin F and Bergamin E, Biochem Soc Trans 2026 (review).** PMID 42305078, DOI 10.1042/bst20250117. BCL7 proteins as SWI/SNF components. Does not concern PBRM1 directly.

The summary of the rest of the response also listed these items, which I did not verify verbatim:
- Hao F et al., Epigenetics & Chromatin 2025 (PMID 40269969, DOI 10.1186/s13072-025-00590-w). Review of ARID1A/B, PBRM1, SMARCB1, and SMARCA2/4 in cancer. This is the only item in that list that mentions PBRM1.
- Several BCL7A and ncBAF papers.

### Not retrieved or unverified
- Full UniProt JSON after residue 1204 of the variant list, including the complete PTM and variant lists and the cross-reference block. The PDB, Pfam, InterPro, and Reactome IDs in section 7 are from the summary only.
- The UniProt full recommended name and comment texts are verbatim, but the EMBL and RefSeq cross-references were not retrieved.
- Reactome R-HSA-3214858, R-HSA-8939243, R-HSA-9932451, R-HSA-9933939: unverified. The Reactome search did not return them.
- Yuan et al 2022 (cited by Reactome for the PBRM1 module): not retrieved.
- Europe PMC results after the first ~40,000 characters: not read. The total hitCount of 92 is verbatim, but later records are unknown.
- The ComplexPortal complex IDs CPX-1196 and CPX-1199 appeared only in the summary.

### URLs read
- https://rest.uniprot.org/uniprotkb/Q86U86.json (truncated)
- https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB:Q86U86&limit=100
- https://reactome.org/ContentService/search/query?query=PBRM1&species=Homo%20sapiens
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22cryo-EM%22%20AND%20%22PBAF%22&format=json&resultType=core (truncated; first request timed out, one retry succeeded)
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22nucleosome-bound%20human%20PBAF%22&format=json&resultType=core&pageSize=5

I could not deliver what you asked for in full. Three of the five Europe PMC searches returned HTTP 503, and two of the successful searches returned only partial records. Also, source rules limit me to quoting at most 125 characters from Europe PMC text, so I have paraphrased the abstracts rather than reproducing them verbatim. The entries below come from the fetched JSON; where a record came only from the model-extracted summary of the truncated response, I say so.

**Fetch status**
- BAFopathies query: timed out once, then succeeded on retry. Read at offset 0 and offset 139883. The page reports more content at offset 279766, which I did not read.
- BAF complex / Coffin-Siris query: timed out once, then succeeded on retry. Read at offset 0 only.
- ARID2 / Coffin-Siris query, episignature query, PBRM1 de novo query: HTTP 503 Service Unavailable. I did not retry or change the query. Re-sending these would likely fail the same way until the service recovers.

**1. BAFopathies: definition and gene list**
- Not found: Bögershausen & Wollnik, Valencia & Crabtree, and Sokpor et al. did not appear in any record I could read. The BAFopathies query returned 76 hits, and I read only about 4 records fully and a summary of the rest.
- Usable definition text: Tanaka et al. 2025 (Eur J Med Genet, PMID 40962111, DOI 10.1016/j.ejmg.2025.105048) says "Germline variants in ARID1A have been associated with the so-called BAFopathies, including Coffin-Siris syndrome". Schuhmann et al. 2026 (Eur J Med Genet, PMID 42173440, DOI 10.1016/j.ejmg.2026.105084) says "Pathogenic variants in BAF complex genes are linked to neurodevelopmental disorders, termed BAFopathies."
- Gene list: I could not confirm your canonical list from a fetched source. The records I read name ARID1A, ARID1B, SMARCA4, SMARCB1, SMARCC1, SMARCC2, SOX11, and BICRA. Chen et al. 2022 (Genet Med, PMID 34906496, DOI 10.1016/j.gim.2021.09.017), which I read only from the model summary, reports 127 of 16,243 exome patients with variants in known BAFopathy genes, and proposes BICRA among candidate genes. ARID2, DPF2, ACTL6A/B, and SMARCD1 were not confirmed in anything I read.
- Other BAFopathy records I saw are listed in section 2.

**2. Coffin-Siris syndrome clinical features**
- No single review abstract was retrieved. The closest is Bhanushali et al. 2026 (Clin Case Rep, PMID 42707522, DOI 10.1002/ccr3.73083), a SMARCB1 case report. Its abstract states CSS is "characterized by global developmental delay (GDD), speech impediment, coarse facial features" and describes hypoplastic or absent fifth fingernails/toenails. It also reports SMARCB1 with a GNE co-variant in two siblings.
- Kolkiran et al. 2026 (Eur J Pediatr, PMID 41795723, DOI 10.1007/s00431-026-06830-9), an 8-patient series, reports: developmental delay and dysmorphic features as the main referral reasons; hypertrichosis in 5 of 8; mild terminal fifth phalanx hypoplasia in 3; short stature, hypothyroidism, transient hypercalcemia, cryptorchidism, and recurrent fractures in individual patients. Seven patients had ARID1B variants and one had SMARCA4.
- Chen et al. 2026 (Front Genet, PMID 42703436, DOI 10.3389/fgene.2026.1925563), a SMARCA4 review of 40 CSS4 cases, reports intellectual disability in 100%, autism spectrum features in 42.5%, and fifth digit hypoplasia in 55.0%.
- Not found in what I read: hypotonia, agenesis of corpus callosum, feeding difficulties, and hypertrichosis frequencies in a single review. You will need an HPO/review source for those.

**3. ARID2-related ID (CSS6)**
- Not retrieved. The ARID2 query returned HTTP 503. Bramswig, Shang, and Van Paemel were not checked.

**4. DNA methylation episignatures**
- Aref-Eshghi / EpiSign CSS paper: not retrieved. The episignature query returned HTTP 503.
- PBRM1 and ARID2 episignature status: not found in any record I read.
- Related records seen (summary-derived unless noted):
  - Schuhmann et al. 2026 (PMID 42173440): a case with a deep intronic ARID1A deletion showed a BAFopathy-like methylation profile. Verbatim-visible part.
  - Tanaka et al. 2025 (PMID 40962111): an ARID1A fetal hydrocephalus case mapped to the BAFopathy episignature group. Verbatim-visible part.
  - Trajkova et al. 2024 (HGG Advances, PMID 38751117, DOI 10.1016/j.xhgg.2024.100309): a 97-patient NDD episignature study; SMARCB1 variants showed an exception. Summary only.
  - Al-Jawahiri et al. 2022 (Genet Med, PMID 35341651): SOX11 variants with a distinct methylation profile. Summary only.
  - Singh et al. 2024 (Brain, PMID 38128548): SMARCC1 BAFopathy with hydrocephalus. Summary only.

**5. PBRM1 de novo variants in autism or DD cohorts**
- Not retrieved. The PBRM1 de novo query returned HTTP 503. Iossifov, De Rubeis, Satterstrom, DDD, and Kaplanis were not checked.

**Other records seen (summary-derived unless noted)**
- Bosch et al. 2023 (Genet Med, PMID 37551667, DOI 10.1016/j.gim.2023.100950; medRxiv preprint version PPR639752): 65 SMARCC2 individuals. Loss-of-function variants were mostly inherited with mild or normal cognition; non-truncating variants were mostly de novo with severe delay. Summary only.
- Ou et al. 2026 (PMID 41532374); Ibrahim et al. 2025 (PMID 41291750); Li et al. 2025 (PMID 39901255): SMARCC2 case series and reports. Summary only.
- Chesneau et al. 2026 (Clin Genet, PMID 41568967): loss-of-function SMARCA4 and eye anomalies in three individuals. Summary only.
- Ge et al. 2026 (Eur J Pediatr, PMID 41545737): ARID1B variants in CSS. Summary only.
- Chu et al. 2026 (BMC Pediatr, PMID 42168980, DOI 10.1186/s12887-026-06974-5): SOX11 variants in hypogonadotropic hypogonadism; 25 of 26 phenotyped individuals had CSS-compatible features. Verbatim-visible.
- Wang 2026 (Genes, PMID 41595501, DOI 10.3390/genes17010081): BICRA-related CSS12, with systemic features. Verbatim-visible.
- Guerrero-Flores et al. 2026 (CRONDEX, Clin Epigenetics, PMID 42271442, DOI 10.1186/s13148-026-02176-z): a web resource for chromatin-related NDD genes that includes BAFopathies as a gene module. Verbatim-visible.

**Final URLs read**
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=BAFopathies&format=json&resultType=core (offsets 0 and 139883)
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=BAF%20complex%20neurodevelopmental%20disorder%20Coffin-Siris&format=json&resultType=core (offset 0)

**Not fetched**
- Any PMC or PubMed URLs, per your instruction.
- Records named only in summaries were not checked against their full text or against the DOI.

I'll start with the HPO terms, using exact matching first and the label+synonym fallback where needed.

The HPO results so far are raw JSON with exact labels and OBO IDs. Continuing with the rest of the HPO list.

The broad query returned a 503, so I'm retrying it once in XML format. In the same batch I'm fetching the full text of PMC10412456 to check for PBRM1.

Six of the seven queries returned data. Query 7 returned HTTP 503 with no Retry-After, so it is a permanent failure and I will not retry it. Query 6 has 100 hits and only the first page was read verbatim, so I'll read the next section and look up the C. elegans candidate from the summary (PMCID PMC8506967) to get its title and PMID.

HPO is complete except one miss. "Neoplasm of the kidney" returned no exact hit, so I'll retry it without exact matching and with label+synonym fields, alongside the CL batch.

CL is complete. The HPO "Neoplasm of the kidney" retry without exact matching returned "Renal neoplasm" as its top hit, and the queryFields variant returned zero docs. Next, UBERON.

UBERON is done. Two requested labels returned no exact label match, so I'll report the closest synonym hits for those. Next, GO biological process terms.

GO biological process is complete. Next, the GO cellular component terms and the two CHEBI terms.

The broad query returned 503 in both JSON and XML, so I'm not retrying it again. The full-text fetch was cut off, and the PBRM1 sentences I have so far come from a model summary, not verbatim text. I'm reading the next section the page points to.

GO cellular component and CHEBI are done. "beta-catenin" returned no exact CHEBI hit, so I'll also try it without exact matching, per the fallback rule. Next, the NCIT batch.

Six of the seven queries returned records. Query 7 failed, so there are no HIF or interferon mechanism papers to report.

**Limit on abstracts:** I could not return the abstracts verbatim. This source is not pre-approved, so I may quote at most 125 characters at a time. The summaries below are paraphrased, with short quotes only where needed. The full abstracts are at the DOI links listed for each item.

**1. Waldhauser et al., Pbrm1 in oligodendrocytes (PMCID PMC10296403)**
- Title: "PBAF Subunit Pbrm1 Selectively Influences the Transition from Progenitors to Pre-Myelinating Cells during Oligodendrocyte Development."
- Authors: Waldhauser V, Baroti T, Fröb F, Wegner M (4 authors)
- Journal: Cells, 2023, vol 12, issue 12, article 1556
- PMID 37371026; PMCID PMC10296403; DOI 10.3390/cells12121556
- Abstract (paraphrased): Pbrm1 was deleted in the oligodendrocyte lineage at different developmental stages. Deletion in late progenitors had little effect. Loss shortly after specification reduced the number of cells entering the pre-myelinating state, and that reduction carried through to fewer myelinating oligodendrocytes.
- Mouse allele and Cre driver: not named in the abstract. The abstract says only that Pbrm1 was "specifically deleted it in the oligodendrocyte lineage at different times of development in the mouse."

**2. Sokpor et al., ATP-dependent chromatin remodeling in cortical neurogenesis (PMCID PMC5900035)**
- Title: "ATP-Dependent Chromatin Remodeling During Cortical Neurogenesis."
- Authors: Sokpor G, Castro-Hernandez R, Rosenbusch J, Staiger JF, Tuoc T (5 authors)
- Journal: Frontiers in Neuroscience, 2018, vol 12, article 226
- PMID 29686607; DOI 10.3389/fnins.2018.00226
- Abstract (paraphrased): This is a review of how ATP-dependent chromatin remodelers shape cortical development. It covers progenitor proliferation, neuronal subtype specification, and neuronal migration and maturation.
- PBRM1: not mentioned in the abstract. I did not access the full text, so I cannot say whether PBRM1 expression in the ventricular or subventricular zone is discussed in the body.

**3. Osuma et al., cell type-specific PBAF functions (2025)**
- Exact title: "Cell type-specific functions of the PBAF chromatin-remodeling complex in neuronal diversification."
- Authors: Osuma A, Destain H, Mann J, Li Y, Taylor SR, Prahlad M, Weigle IQ, Marques F, Schulz NG, Mathies LD, Islam P, Brown AEX, Smith JJ, Kratsios P (14 authors)
- Journal: Nature Communications, 2025, vol 17, article 741 (print December 2025; online 2025-12-14)
- PMID 41390837; PMCID PMC12820340; DOI 10.1038/s41467-025-67434-9
- Abstract (paraphrased): The study uses C. elegans. PBAF represses gene expression in nerve cord motor neurons by opposing the UNC-3 terminal selector, and activates gene expression in caudal motor neurons. PBAF loss causes locomotion defects. The authors propose that MAB-9/TBX20 recruits PBAF to specific loci.

**4. Lane et al., PBRM1 and pericentromeres (DOI 10.1038/s41467-025-57277-9)**
- Title: "PBRM1 directs PBAF to pericentromeres and protects centromere integrity."
- Authors: Lane KA, Harrod A, Wu L, Roumeliotis TI, Feng H, Foo S, Begg KAG, Schiavoni F, Amin N, Zenke FT, Melcher AA, Choudhary JS, Downs JA (13 authors)
- Journal: Nature Communications, 2025, vol 16, article 1980 (print February 2025)
- PMID 40011561; PMCID PMC11865495
- Abstract (paraphrased): PBRM1 loss compromises centromere and pericentromere integrity, even without other perturbations. PBAF is present at these regions, and PBAF and H3K9 methylation binding patterns shift when PBRM1 is absent. Quote: "PBRM1 loss creates a dependence on the spindle assembly checkpoint" (a therapeutic vulnerability).

**5. De Silva et al., PBRM1 bromodomains and RNA (PMCID PMC10164552)**
- Title: "PBRM1 bromodomains associate with RNA to facilitate chromatin association."
- Authors: De Silva SM, Dhiman A, Sood S, Mercedes KF, Simmons WJ, Henen MA, Vögeli B, Dykhuizen EC, Musselman CA (9 authors listed in the metadata)
- Journal: Nucleic Acids Research, 2023, vol 51, issue 8, pages 3631-3649
- PMID 36808431; DOI 10.1093/nar/gkad072
- Bromodomains: the second and fourth (BD2 and BD4). The abstract says they bind double-stranded RNA elements. Quote: "the second and fourth bromodomains from PBRM1 also bind nucleic acids" (70 characters).
- H3K14ac: the abstract mentions it only as background. It says the six tandem bromodomains "cooperate in binding of nucleosomes acetylated at histone H3 lysine 14." The new finding is RNA binding by BD2 and BD4, not H3K14ac binding by those domains.

**6. C. elegans pbrm-1 studies**
- Enríquez et al., J Biol Chem 2021, "Binding specificity and function of the SWI/SNF subunit SMARCA4 bromodomain interaction with acetylated histone H3K14." PMID 34473995; PMCID PMC8506967; DOI 10.1016/j.jbc.2021.101145; authors Enríquez P, Krajewski K, Strahl BD, Rothbart SB, Dowen RH, Rose RB (6 authors).
  - This is the developmental study. Quote: "knockdown of the SWI/SNF accessory subunit PBRM-1 resulted in severe developmental defects" (90 characters). The abstract says these defects appeared only when SMARCA4 bromodomain mutations were combined with PBRM-1 knockdown.
- Osuma et al. (item 3) is a C. elegans PBAF study, but its visible abstract does not name pbrm-1.
- Not verified: the 100-hit result set was not fully read. The model summary of the unread part mentions Smith JJ et al., PLoS Genet 2022 (PMID 34982771, PMCID PMC8759636, DOI 10.1371/journal.pgen.1009981) on BAF and PBAF in C. elegans anchor-cell invasion. I did not read that abstract verbatim, so treat it as a lead, not a confirmed match.

**7. PBRM1 loss, HIF or interferon, and ccRCC (not obtained)**
- WebFetch returned HTTP 503 Service Unavailable for this query. No Retry-After header was given, so I did not retry. Sending the same URL again will likely fail the same way.
- No HIF or interferon mechanism papers were retrieved.

**Final URLs read**
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PMCID%3APMC10296403&format=json&resultType=core
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PMCID%3APMC5900035&format=json&resultType=core
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22PBAF%22%20AND%20%22cell%20type-specific%22%20AND%20JOURNAL%3A%22Nat%20Commun%22%20AND%20PUB_YEAR%3A2025&format=json&resultType=core
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fs41467-025-57277-9&format=json&resultType=core
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PMCID%3APMC10164552&format=json&resultType=core
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=Pbrm1%20AND%20(%22C.%20elegans%22%20OR%20%22pbrm-1%22)&format=json&resultType=core (first 39,840 characters, a continuation at offset 139,840, and model summaries for the rest)
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PMCID%3APMC8506967&format=json&resultType=core
- https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PBRM1%20AND%20(interferon%20OR%20HIF)%20AND%20renal&format=json&resultType=core (HTTP 503, not retried)

Only "Speech Therapy" is still unresolved in NCIT. I'll run its non-exact fallback.

I could not deliver full verbatim abstracts. Europe PMC came back as a non-preapproved source, so I can only quote up to 125 characters per source and paraphrase the rest. The metadata below is from the API JSON. You can get full abstracts from the DOI or Europe PMC links, or from the `abstractText` field of the same API responses.

Pan D et al. 2018 was not found. Its exact-title search returned HTTP 503 with no Retry-After, so under my fetch rules I did not retry it. You can rerun that title query yourself.

Each query's raw JSON was only partly read verbatim (about 40k characters per response). The rest was summarised by a model, so "not found" means not in the read portion or the summary. Queries 2, 4 and 5 timed out on the first attempt. Their single retries succeeded.

**1. Cardiac (Baf180 / Polybromo-1)**
- **Found:** Wang Z, Zhai W, Richardson JA, Olson EN, Meneses JJ, Firpo MT, Kang C, Skarnes WC, Tjian R. "Polybromo protein BAF180 functions in mammalian cardiac chamber maturation." *Genes Dev* 18(24):3106-3116, 2004. PMID 15601824. DOI 10.1101/gad.1238104. PMC535920.
- **Abstract content:** BAF180 ablation in mouse embryos gives "severe hypoplastic ventricle development and trophoblast placental defects". Aggregation analyses suggest the heart defect is a direct effect, not secondary to the placental defect. Candidate targets include S100A13, RARβ2 and CRABPII.
- **Not in the abstract:** embryonic lethality timing (so E12.5–E15.5 is unconfirmed), trabeculation, and myocardial thinning. I have not read the full text.
- **Huang X et al. 2008 (coronary vessel/epicardium):** not found in any result. The nearest hit is Vieira JM et al. 2017 (PMID 28737171), which concerns BRG1 rather than BAF180.

**2. Kidney (Pbrm1)**
- **Found:** Espana-Agusti J, Warren A, Chew SK, Adams DJ, Matakidou A. "Loss of PBRM1 rescues VHL dependent replication stress to promote renal carcinogenesis." *Nat Commun* 8:2026, 2017. PMID 29229903. DOI 10.1038/s41467-017-02245-1. PMC5725450.
- **Abstract content:** loss of VHL alone causes replication stress that constrains growth. Concomitant PBRM1 loss rescues this. Combined Vhl and Pbrm1 deletion in mouse kidney gives "fully-penetrant, multifocal carcinomas".
- **Gu YF et al. 2017 (Cancer Discov)** and **Nargund AM et al. 2017 (Cell Rep):** not found in any result read.

**3. Senescence / HSC / p21 (BAF180)**
- **Lee H, Dai F, Zhuang L, Xiao ZD, Kim J, Zhang Y, Ma L, You MJ, Wang Z, Gan B.** "BAF180 regulates cellular senescence and hematopoietic stem cell homeostasis through p21." *Oncotarget* 2016. PMID 26992241. DOI 10.18632/oncotarget.8102.
- **Source caveat:** these metadata come only from the model-extracted summary, not the raw JSON. The abstract was not retrieved.

**4. Neural (Pbrm1)**
- **Duan YY et al. 2026**, "PBRM1 Deficiency in Microglia Leads to Excessive Neurogenesis and Autism-Like Behaviors via the CCL5-CCR1/5-β-catenin Signaling Axis." *Adv Sci*. PMID 42893407. DOI 10.1002/advs.78086. The abstract was read in the raw JSON. Quote: "PBRM1 directly binds to the Ccl5 promoter and represses the expression of CCL5". Paraphrase: PBRM1 loss in microglia drives neural stem/progenitor proliferation and neurogenesis through CCL5–CCR1/5, and CCR1/5 blockade improves behaviour in Pbrm1 cKO mice.
- **Osuma A et al. 2025**, "Cell type-specific functions of the PBAF chromatin-remodeling complex in neuronal diversification." *Nat Commun* 17:741. PMID 41390837. DOI 10.1038/s41467-025-67434-9. This is a C. elegans study of PBAF in motor neuron identity, not Pbrm1 and not mouse.
- **Incidental Pbrm1 mouse study (not neural):** Chiou LW et al. 2026, "Pbrm1 Loss Induces a Permissive Chromatin State for Cholangiocytic Differentiation and Cholangiocarcinoma Formation." *Cell Mol Gastroenterol Hepatol* 20(6). PMID 41513002. DOI 10.1016/j.jcmgh.2025.101720.
- **Li BE et al. 2023**, "In vivo CRISPR/Cas9 screening identifies Pbrm1 as a regulator of myeloid leukemia development in mice." *Blood Adv* 7(18). PMID 37428871. DOI 10.1182/bloodadvances.2022009455. Seen only in the summary, so unverified.

**5. Zebrafish (Pbrm1)**
- **Nothing Pbrm1-specific found** in the read portion or summary.
- **Near miss:** Park DD et al. 2026, "Smarca4 maintains mitochondrial homeostasis and energy metabolism during cardiac development." *Cell Mol Life Sci* 83:167. PMID 41794942. DOI 10.1007/s00018-026-06168-3. This concerns smarca4a, not Pbrm1.

**6. T cell exhaustion / CRISPR screen (PBAF)**
- **Pan D et al. 2018 (Science):** not found. The title search returned HTTP 503 and was not retried. The 28-hit Pbrm1 query did not surface it in the read portion or summary.
- **Related, verified in raw JSON (not Pbrm1, not Pan 2018):**
  - Battistello E et al. 2023, *Mol Cell* 83(8). PMID 36944333. DOI 10.1016/j.molcel.2023.02.026. mSWI/SNF complexes in T-cell activation and exhaustion.
  - Mondal J et al. 2025, *Nat Commun* 16:1378. PMID 39910049. DOI 10.1038/s41467-025-56347-2. Brd7 (a PBAF subunit) loss in breast cancer metastasis, with CD8+ exhausted T cells increased.

**Other near misses:** Carulli N et al. 2026 (PMID 42246576, DOI 10.1093/mtomcs/mfag019) studies Baf180 in myoblast metal homeostasis, not heart or senescence.

## Summary

Two of the four Europe PMC searches returned data. The broad PBRM1 germline search returned HTTP 503 twice (JSON, then XML), so it is not retrieved. The three paper lookups succeeded. Europe PMC content is from a non-preapproved source, so I could not reproduce the abstracts verbatim. Quotes are limited to 125 characters, and the abstracts below are paraphrased.

## 1. PMID 37500730: Valencia AM et al., Nat Genet 2023

- **Citation:** Valencia AM, Sankar A, van der Sluijs PJ, Satterstrom FK, Fu J, Talkowski ME, Vergano SAS, Santen GWE, Kadoch C. "Landscape of mSWI/SNF chromatin remodeling complex perturbations in neurodevelopmental disorders." Nat Genet. 2023 Aug;55(8):1400-1412. DOI 10.1038/s41588-023-01451-6. PMID 37500730. PMCID PMC10412456. Open access (CC BY).
- **Abstract (paraphrased):** The mSWI/SNF (BAF) complex genes carry the most de novo missense and protein-truncating variants among nuclear protein complexes in neurodevelopmental disorders (NDDs). Non-truncating NDD variants mostly disrupt the cBAF subcomplex and cluster in four structural regions. Over 70% of NDD-perturbed residues overlap with cancer-mutated residues, but about 60% of amino acid changes are NDD-specific.
- **Study size (verbatim from full text):** "The 29 genes encoding the mSWI/SNF complex are affected in the greatest percentage" (of 55,645 DECIPHER cases). The integrated analysis contains 2,539 mSWI/SNF variants (described as "2539 variants in mSWI/SNF genes" in Results and "2,539 total cases" in the Introduction). Missense/in-frame variants number 1,703.
- **PBRM1 sentences:**
  - Verbatim, Results (Par8): "genes encoding PBAF and ncBAF components such as PBRM1, ARID2, BICRAL" are "found to be more frequently mutated in cancer than in NDD." The full sentence is longer than 125 characters, so only the quoted portion is reproduced here.
  - From a model-extracted summary, not verbatim (the page was truncated, so these are unverified): one sentence says shared NDD and cancer recurrent mutations occur "within PBRM1 and ACTB subunits," and another says the analysis "resolved 20 additional PBAF-specific subunit mutations across ARID2, PBRM1 and BRD7."
- **Answers to your questions:**
  - **PBRM1 included among analysed subunits?** Not confirmed verbatim. The verbatim text names the 29-gene mSWI/SNF set but does not list it. The summary says PBRM1 has mapped mutations, which suggests inclusion, but I could not verify this.
  - **Number of genes/variants:** 29 mSWI/SNF genes; 2,539 variants (see above).
  - **PBRM1 NDD enrichment?** No. The verbatim text says PBRM1 (with ARID2 and BICRAL) was more frequently mutated in cancer than in NDD.
- **Not read:** Full text offsets 39,913 to 139,913 were only summarized, and the last ~80,000 characters were not read. Supplementary Tables 1 to 3, which may list the analysed genes, were not accessible.

## 2. J Med Genet 2015: "A germline mutation in PBRM1 predisposes to renal cell carcinoma"

- **Citation:** Benusiglio PR et al. J Med Genet. 2015;52(6):426-430. PMID 25911086. DOI 10.1136/jmedgenet-2014-102912. Not open access.
- **Abstract (paraphrased):** Familial RCC is often unexplained. The authors screened PBRM1 in 35 unrelated patients with a personal history of clear-cell RCC (ccRCC) and at least one affected first-degree relative. They found one germline frameshift, c.3998_4005del (p.Asp1333Glyfs), in one patient. Tumour analysis showed loss of heterozygosity and loss of protein expression.
- **Family:** The proband's mother, sister and one niece also had ccRCC. The three affected relatives carried the variant, and an unaffected sister did not, consistent with autosomal-dominant transmission. The abstract gives no further pedigree detail.
- **Segregation:** Co-segregation with disease in the family, as above.
- **Authors' conclusions on penetrance (paraphrased):** The authors state for the first time that an inherited PBRM1 mutation predisposes to RCC. They say international studies are needed to estimate PBRM1's contribution to RCC susceptibility and to "estimate penetrance" before clinical use. They do not give a penetrance estimate.

## 3. PMID 33811077: Karki M et al., Sci Adv 2021

- **Citation:** Karki M, Jangid RK, Anish R, et al. (Tripathi DN, last author). "A cytoskeletal function for PBRM1 reading methylated microtubules." Sci Adv. 2021;7(14):eabf2866. DOI 10.1126/sciadv.abf2866. PMID 33811077. PMCID PMC11059954. Open access (CC BY-NC).
- **Abstract (paraphrased):** PBRM1, within the PBAF remodeling complex, reads SETD2-written methyl marks on microtubules. It binds these marks through its BAH domains and recruits PBAF components to the mitotic spindle. Loss of SETD2 methylation, or pathogenic BAH-domain mutations, disrupts PBRM1 microtubule binding and PBAF recruitment and causes genomic instability. The short quote "PBRM1 binds SETD2 methyl marks via BAH domains" is verbatim.

## Europe PMC query: PBRM1 AND "renal cell carcinoma" AND germline AND (susceptibility OR predisposition)

- **Not retrieved.** Both the JSON and XML queries returned HTTP 503. I did not retry further. Re-running later may succeed.
- The only germline PBRM1 RCC study I retrieved is item 2 above (PMID 25911086). I found no negative studies, because the search did not run.

## Not retrieved or limited

- Full abstract text verbatim for all three papers (paraphrased, per the 125-character rule).
- The broad germline-PBRM1 search (503 twice).
- Whether PBRM1 is one of the 29 analysed mSWI/SNF genes (not confirmed verbatim).
- The PBRM1 sentences from the summarized portion of the PMC full text (unverified).

All requested labels were queried against OLS4. Three exact-label misses are NOT FOUND, and one more needs a caveat. Every lookup used the URL template you gave with `exact=true`, and retries used no `exact` flag, with the `queryFields=label,synonym` variant also tried for the kidney neoplasm label. No rate limiting occurred. Where the returned label differs from the requested one, the match came through an exact synonym, which the API reports in `exact_synonyms`.

**HPO**

| Requested label | Returned label | OBO ID |
|---|---|---|
| Global developmental delay | Global developmental delay | HP:0001263 |
| Intellectual disability | Intellectual disability | HP:0001249 |
| Autistic behavior | Autistic behavior | HP:0000729 |
| Autism | Autism | HP:0000717 |
| Seizure | Seizure | HP:0001250 |
| Muscular hypotonia | Hypotonia (exact synonym "Muscular hypotonia") | HP:0001252 |
| Hypotonia | Hypotonia | HP:0001252 |
| Feeding difficulties | Feeding difficulties | HP:0011968 |
| Short stature | Short stature | HP:0004322 |
| Microcephaly | Microcephaly | HP:0000252 |
| Macrocephaly | Macrocephaly | HP:0000256 |
| Delayed speech and language development | Delayed speech and language development | HP:0000750 |
| Abnormality of the corpus callosum | Abnormal corpus callosum morphology (exact synonym) | HP:0001273 |
| Agenesis of corpus callosum | Agenesis of corpus callosum | HP:0001274 |
| Coarse facial features | Coarse facial features | HP:0000280 |
| Hypertrichosis | Hypertrichosis | HP:0000998 |
| Aplasia/Hypoplasia of the distal phalanges of the hand | Aplasia/Hypoplasia of the distal phalanges of the hand | HP:0009835 |
| Hypoplastic fifth fingernail | Hypoplastic fifth fingernail | HP:0008398 |
| Abnormal heart morphology | Abnormal heart morphology | HP:0001627 |
| Ventricular septal defect | Ventricular septal defect | HP:0001629 |
| Renal cell carcinoma | Renal cell carcinoma | HP:0005584 |
| Clear cell renal cell carcinoma | Clear cell renal cell carcinoma | HP:0006770 |
| Neoplasm of the kidney | NOT FOUND (exact). Non-exact top hit "Renal neoplasm" HP:0009726 is not a verbatim match. The label+synonym query returned 0 docs. | - |
| Behavioral abnormality | Atypical behavior (exact synonym) | HP:0000708 |
| Motor delay | Motor delay | HP:0001270 |
| Abnormality of brain morphology | Abnormal brain morphology (exact synonym) | HP:0012443 |
| Hearing impairment | Hearing impairment | HP:0000365 |
| Strabismus | Strabismus | HP:0000486 |
| Scoliosis | Scoliosis | HP:0002650 |
| Cryptorchidism | Cryptorchidism | HP:0000028 |
| Gastroesophageal reflux | Gastroesophageal reflux | HP:0002020 |
| Constipation | Constipation | HP:0002019 |
| Autosomal dominant inheritance | Autosomal dominant inheritance | HP:0000006 |
| Sporadic | Sporadic | HP:0003745 |
| Variable expressivity | Variable expressivity | HP:0003828 |
| Incomplete penetrance | Typified by incomplete penetrance (exact synonym) | HP:0003829 |

**GO biological process**

| Requested label | Returned label | OBO ID |
|---|---|---|
| chromatin remodeling | chromatin remodeling | GO:0006338 |
| ATP-dependent chromatin remodeler activity | ATP-dependent chromatin remodeler activity | GO:0140658 |
| nucleosome binding | nucleosome binding | GO:0031491 |
| regulation of transcription by RNA polymerase II | regulation of transcription by RNA polymerase II | GO:0006357 |
| negative regulation of transcription by RNA polymerase II | negative regulation of transcription by RNA polymerase II | GO:0000122 |
| neurogenesis | neurogenesis | GO:0022008 |
| neural precursor cell proliferation | neural precursor cell proliferation | GO:0061351 |
| canonical Wnt signaling pathway | canonical Wnt signaling pathway | GO:0060070 |
| cellular response to DNA damage stimulus | DNA damage response (exact synonym) | GO:0006974 |
| mitotic cell cycle | mitotic cell cycle | GO:0000278 |
| cellular senescence | cellular senescence | GO:0090398 |
| chemokine-mediated signaling pathway | chemokine-mediated signaling pathway | GO:0070098 |
| microglial cell activation | microglial cell activation | GO:0001774 |
| oligodendrocyte differentiation | oligodendrocyte differentiation | GO:0048709 |
| heart development | heart development | GO:0007507 |
| cardiac muscle tissue morphogenesis | cardiac muscle tissue morphogenesis | GO:0055008 |

**GO cellular component**

| Requested label | Returned label | OBO ID |
|---|---|---|
| nucleus | nucleus | GO:0005634 |
| chromatin | chromatin | GO:0000785 |
| nucleosome | nucleosome | GO:0000786 |
| SWI/SNF complex | SWI/SNF complex | GO:0016514 |
| nBAF complex | nBAF complex | GO:0071565 |
| npBAF complex | npBAF complex | GO:0071564 |
| microtubule | microtubule | GO:0005874 |
| pericentric heterochromatin | pericentric heterochromatin | GO:0005721 |

**CL**

| Requested label | Returned label | OBO ID |
|---|---|---|
| microglial cell | microglial cell | CL:0000129 |
| neural stem cell | neural stem cell | CL:0000047 |
| neuronal stem cell | neural stem cell (exact synonym) | CL:0000047 |
| oligodendrocyte precursor cell | oligodendrocyte precursor cell | CL:0002453 |
| oligodendrocyte | oligodendrocyte | CL:0000128 |
| neuron | neuron | CL:0000540 |
| radial glial cell | radial glial cell | CL:0000681 |
| cardiac muscle cell | cardiac muscle cell | CL:0000746 |
| kidney epithelial cell | kidney epithelial cell | CL:0002518 |
| granule cell | granule cell | CL:0000120 |

**UBERON**

| Requested label | Returned label | OBO ID |
|---|---|---|
| brain | brain | UBERON:0000955 |
| hippocampus | NOT FOUND (exact label). Synonym hits: "Ammon's horn" UBERON:0001954, "hippocampal formation" UBERON:0002421, "archicortex" UBERON:0002961. None is labelled "hippocampus". | - |
| dentate gyrus of hippocampal formation | dentate gyrus of hippocampal formation | UBERON:0001885 |
| cerebral cortex | cerebral cortex | UBERON:0000956 |
| ventricular zone | ventricular zone | UBERON:0003053 |
| subventricular zone | NOT FOUND (exact label). Exact-synonym hit: "postnatal subventricular zone" UBERON:0004922. A second hit, "ganglionic eminence" UBERON:0004023, carries it only as a broad synonym. | - |
| corpus callosum | corpus callosum | UBERON:0002336 |
| heart | heart | UBERON:0000948 |
| cardiac ventricle | cardiac ventricle | UBERON:0002082 |
| kidney | kidney | UBERON:0002113 |
| central nervous system | central nervous system | UBERON:0001017 |

**NCIT**

| Requested label | Returned label | OBO ID |
|---|---|---|
| Physical Therapy | Physical Therapy | NCIT:C15302 |
| Occupational Therapy | Occupational Therapy | NCIT:C121351 |
| Speech Therapy | NOT FOUND (exact). Non-exact top hits were "Speech Therapist" NCIT:C19177 and "Speech Language Therapy" NCIT:C159273. Neither is a verbatim match. | - |
| Genetic Counseling | Genetic Counseling | NCIT:C15240 |
| Anticonvulsant Agent | Anticonvulsant Agent | NCIT:C264 |
| Gastrostomy | Gastrostomy | NCIT:C52006 |
| Supportive Care | Supportive Care | NCIT:C15747 |
| Maraviroc | Maraviroc | NCIT:C73144 |
| Pembrolizumab | Pembrolizumab | NCIT:C106432 |
| Nivolumab | Nivolumab | NCIT:C68814 |
| Tazemetostat | Tazemetostat | NCIT:C107506 |
| Magnetic Resonance Imaging | Magnetic Resonance Imaging | NCIT:C16809 |
| Whole Exome Sequencing | Whole Exome Sequencing | NCIT:C101295 |
| Whole Genome Sequencing | Whole Genome Sequencing | NCIT:C101294 |

**CHEBI**

| Requested label | Returned label | OBO ID |
|---|---|---|
| maraviroc | maraviroc | CHEBI:63608 |
| beta-catenin | NOT FOUND. Exact query returned 0 docs. The non-exact top hit, PNU-74654 (CHEBI:228251), is a beta-catenin/TCF interaction inhibitor, not beta-catenin itself. | - |

The "Neoplasm of the kidney", "Speech Therapy", "hippocampus", "subventricular zone" and "beta-catenin" entries are the ones to check by hand before use. The "subventricular zone" entry is a synonym match to a postnatal-specific term, so pick between UBERON:0004922 and a more general term yourself. This report contains no file paths.

# PBRM1‑Related BAFopathy (MONDO:0700122) — Comprehensive Research Report

**Interpretation statement (read first).** This report covers the disease entity **MONDO:0700122, "PBRM1‑related BAFopathy," whose causal gene is *PBRM1* (polybromo 1 / BAF180, HGNC:30064, NCBI Gene 55193, Ensembl ENSG00000163939, UniProt Q86U86, 3p21.1)** — the PBAF‑specific subunit of the mammalian SWI/SNF (BAF) ATP‑dependent chromatin‑remodelling complex. It is *not* the same as *ARID2*‑related Coffin‑Siris syndrome 6, *SMARCC1*‑ or *BICRA*‑related BAFopathy, or any OMIM‑numbered Coffin‑Siris subtype; those are separate MONDO entities with different genes.

**A second, essential framing point, established by retrieval in this session:** MONDO:0700122 is a *pattern‑generated placeholder term*, not a clinically delineated syndrome. Its MONDO definition is entirely formulaic, it carries **zero cross‑references, zero synonyms and zero phenotype annotations**, and the human germline evidence linking *PBRM1* to a neurodevelopmental disorder currently amounts to **one single reported patient**. ClinGen has published no curation for *PBRM1*; Genomics England PanelApp rates *PBRM1* **Red (lowest confidence)** on its Intellectual disability panel; SFARI Gene does not list *PBRM1* at all; and the largest systematic analysis of mSWI/SNF variants in neurodevelopmental disorders explicitly places *PBRM1* among subunits "more frequently mutated in cancer than in NDD." Accordingly, many sections below legitimately read "no data exist," and I say so rather than importing features from better‑characterised BAFopathies. Where I draw on *ARID2* (the other PBAF‑specific subunit) or Coffin‑Siris syndrome, it is flagged explicitly as **analogy, not evidence for this entity**.

---

## 1. Disease Information

### 1.1 Overview

MONDO:0700122 is defined, verbatim, as: **"Any BAFopathy in which the cause of the disease is a mutation in the PBRM1 gene."** This definition was retrieved identically from two independent endpoints — the EBI OLS4 API (`https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0700122`) and the Monarch Initiative API v3 (`https://api.monarchinitiative.org/v3/api/entity/MONDO:0700122`). Both record the label **"PBRM1-related BAFopathy"**, IRI `http://purl.obolibrary.org/obo/MONDO_0700122`.

The definition is generated from the MONDO design pattern `patterns/OMIM_disease_series_by_gene`, with definition citation PMID 30580808 (the pattern's reference, listed in the OLS4 annotation block). This is the standard MONDO mechanism for minting a gene‑keyed disease term; it does **not** imply that a clinical syndrome has been delineated.

**Parent class:** MONDO:0700120 "BAFopathy" (superclass, per Monarch API v3). **Subclasses:** none (`sub_classes: []`; `has_descendant_count: 1`, i.e. the term itself). **Associated gene:** HGNC:30064 *PBRM1* (*Homo sapiens*, NCBITaxon:9606) via relation **RO:0004003 "has material basis in germline mutation in."** Notably, the Monarch `causal_gene` slot is an **empty list**, and **`has_phenotype_count` is 0** — there are no HPO annotations attached to this disease in Monarch.

BAFopathies as a class are, in the words of the primary clinical cohort paper on them, "a group of neurodevelopmental disorders with extensive locus and phenotypic heterogeneity" (Chen CA et al., *Genet Med* 2022;24(2):364–373, **PMID 34906496**, DOI 10.1016/j.gim.2021.09.017 — exact phrase retrieved from the Background section). A second, independent definitional phrasing retrieved from the literature: "Pathogenic variants in BAF complex genes are linked to neurodevelopmental disorders, termed BAFopathies" (Schuhmann et al., *Eur J Med Genet* 2026, **PMID 42173440**, DOI 10.1016/j.ejmg.2026.105084).

### 1.2 Key identifiers

| Resource | Identifier | Retrieval status |
|---|---|---|
| **Mondo** | **MONDO:0700122** | Confirmed, OLS4 + Monarch API v3 |
| **MedGen** | **CN306939** (MedGen UID 989976), title "PBRM1-related BAFopathy", definition "a BAFopathy caused by a PBRM1 mutation", explicitly mapped to MONDO_0700122 | Confirmed via NCBI E‑utilities `esummary.fcgi?db=medgen` |
| **OMIM (phenotype)** | **None.** No OMIM phenotype MIM number exists for a *PBRM1* neurodevelopmental phenotype | OLS4/Monarch xref lists are null/empty; omim.org returned HTTP 403 so the gene entry itself could not be read |
| **OMIM (gene)** | **606083** (*PBRM1*) | Confirmed via HGNC REST and NCBI Gene esummary |
| **Orphanet (disorder)** | **None found.** ORPHA 434716 is the Orphanet **gene** identifier for *PBRM1*, listed in the HGNC record — not a disorder code | HGNC REST `other_ids`; no Orphanet disorder page retrieved |
| **ICD‑10 / ICD‑11** | **No specific code.** Not retrieved; no evidence any exists | Not found |
| **MeSH** | **No specific disease descriptor.** Not retrieved | Not found |
| **DOID / UMLS CUI** | **None in MONDO.** `obo_xref` is null; Monarch `mappings: []`, `external_links: []` | Confirmed absent |
| **MONDO term tracker** | github.com/monarch-initiative/mondo/issues/3939 | From OLS4 annotation block |

**Related MedGen concepts retrieved:** C5670648 "PBRM1 Gene Mutation"; CN074294 "Nonpapillary renal cell carcinoma" (lists *PBRM1* among associated genes).

### 1.3 Synonyms and alternative names

**None are recorded.** OLS4 returns an empty synonym list; Monarch API v3 returns `synonym: null` with all exact/broad/narrow/related synonym fields null. Descriptive phrases used in the literature and in curation (not ontology synonyms) include "PBRM1‑related neurodevelopmental disorder" and "candidate BAFopathy gene PBRM1." The gene itself has the alias symbols **BAF180, PB1, SMARCH1** (HGNC) and **BAF180, PB1, RCC, SMARCH1** (NCBI Gene).

### 1.4 Provenance of the information

This entity is derived from **aggregated, ontology‑level resources** (MONDO pattern generation + MedGen mirroring), **not** from EHR or patient‑level registry data. The only patient‑level human evidence in the world literature that I could retrieve is a single case in a clinical exome cohort (§4.2). The curation stub in the Monarch `dismech` knowledge base (`stubs/PBRM1-related_BAFopathy.yaml`) is recorded with `entry_type: UNDECIDED`, MONDO parent MONDO:0700120, causal gene hgnc:30064 — i.e. even the curating resource has not yet decided whether this is a bona fide disease entry.

---

## 2. Etiology

### 2.1 Disease causal factors

**Primary cause (as asserted by the ontology):** heterozygous **germline** variation in *PBRM1*, encoded by the MONDO relation **RO:0004003 "has material basis in germline mutation in."** Mode of action inferred from gene constraint and BAFopathy precedent: **haploinsufficiency / loss of function**, autosomal dominant, typically *de novo*.

**Strength of evidence — stated plainly:**

- **One human case.** Chen CA et al. (*Genet Med* 2022, PMID 34906496) identified, in 16,243 clinical exomes, a single patient (Patient N5) with "A de novo heterozygous c.1542–3C>G variant in PBRM1." The authors classified *PBRM1* as a **candidate**, not established, disease gene, and concluded that further mechanistic and phenotypic study is needed to confirm the candidate loci.
- **No ClinGen curation.** The ClinGen gene page for HGNC:30064 states verbatim: **"ClinGen has not yet published curations for PBRM1 (HGNC:30064)."** Gene–Disease Validity classifications: 0. Dosage Sensitivity classifications: 0. Clinical Actionability: 0. Variant Pathogenicity: 0.
- **Genomics England PanelApp rates it Red.** *PBRM1* appears on exactly one panel — panel 285 "Intellectual disability" (version 11.97, created 2026‑11‑12) — with `confidence_level: "1"` and `evidence: ["Expert Review Red"]`, `mode_of_inheritance: ""` (empty), `phenotypes: []` (empty), `publications: []` (empty). In PanelApp, Red = lowest evidence, not recommended for diagnostic reporting.
- **Counter‑evidence from the largest mSWI/SNF NDD analysis.** Valencia AM, Sankar A, van der Sluijs PJ, Satterstrom FK, Fu J, Talkowski ME, Schrier Vergano SA, Santen GWE, Kadoch C. "Landscape of mSWI/SNF chromatin remodeling complex perturbations in neurodevelopmental disorders." *Nat Genet* 2023;55(8):1400–1412 (**PMID 37500730**, DOI 10.1038/s41588-023-01451-6, PMC10412456). This study integrated **2,539 variants across 29 mSWI/SNF genes** (with a DECIPHER denominator of 55,645 cases). Its verbatim statement on PBAF subunits: *"genes encoding PBAF and ncBAF components such as PBRM1, ARID2, BICRAL"* are *"found to be more frequently mutated in cancer than in NDD."* The paper's headline finding is that *"Genes encoding the mammalian SWI/SNF (mSWI/SNF or BAF) family of ATP-dependent chromatin remodeling protein complexes harbor the greatest number of de novo missense and protein-truncating variants among nuclear protein complexes"*, but that **"Non-truncating NDD-associated protein variants predominantly disrupt the cBAF subcomplex"** — i.e. the burden is concentrated in cBAF, not in PBRM1's subcomplex.
- **SFARI Gene (autism gene curation) does not list *PBRM1*.** The SFARI Gene page for PBRM1 returns: **"PBRM1 is not in the SFARI:Gene database"** (2026 Q2 release). This directly qualifies the claim in the 2026 mouse paper (§6) that "Missense mutations in Polybromo 1 (Pbrm1) … have been identified as a risk factor for ASD" — I could find **no** primary human ASD cohort study supporting that premise in this session.

**Conclusion on etiology:** *PBRM1* is a **biologically plausible but genetically unproven** BAFopathy gene. The plausibility rests on (a) extreme constraint against loss of function, (b) membership in a complex whose other subunits cause well‑established NDDs, and (c) mouse/invertebrate developmental phenotypes — not on human case accrual.

### 2.2 Risk factors

**Genetic risk factors**

- **Causal/candidate variant:** `NM_018313.4:c.1542-3C>G` (intron 14; hg19 chr3:52651557), heterozygous, *de novo* — the only reported germline NDD‑associated *PBRM1* variant (PMID 34906496).
- **Constraint as a risk indicator:** *PBRM1* is among the most LoF‑intolerant genes in the genome. **pLI = 1.00** (reported in Table 1 of PMID 34906496; independently mirrored on the ClinGen gene page as gnomAD v4.0 **pLI 1, LOEUF 0.23**, computed on transcript ENST00000296302; and on GeneBe as **pLI 1.00, pHI 0.904**). **DECIPHER %HI = 9.54** (i.e. in the most haploinsufficiency‑prone decile), per the ClinGen mirror. The gnomAD browser itself is a JavaScript shell and could not be read directly in this session; the LOEUF confidence interval, missense o/e and Z score, and observed/expected pLoF counts **were not retrieved**.
- Chen et al.'s gene‑selection filter was explicitly constraint‑driven: BAF genes lacking an established gene–disease association **with gnomAD pLI ≥ 0.98**, which yielded *ACTL6A, BRD7, BICRA, BICRAL, DPF1, PBRM1, SMARCC1, SS18L1*.
- **Susceptibility loci (common variation, different phenotype):** the synonymous *PBRM1* SNP **rs2251219** reached genome‑wide significance for major mood disorders in a five‑GWAS meta‑analysis (>13,600 individuals; P = 3.63 × 10⁻⁸, OR 0.87), and was replicated for bipolar disorder (OR = 0.89, p = 0.003; combined meta‑analysis OR = 0.875, p = 2.68 × 10⁻⁹) with **no** significant schizophrenia association (OR = 0.97, p = 0.21) — Vassos et al., *Biol Psychiatry* 2012;72(8):645–650, **PMID 22560537**. **Important caveat retrieved with the finding:** the 3p21.1 region sits in a large high‑LD haplotype block spanning many genes, so *PBRM1* is not established as the causal gene at this locus. **This is a psychiatric common‑variant signal, not evidence for MONDO:0700122.**
- **Modifier genes:** **No data.** None reported for this entity.

**Environmental risk factors**

- **No data.** No toxin, radiation, occupational, dietary, infectious or lifestyle risk factor has been reported for *PBRM1*‑related germline disease. For a *de novo* dominant mechanism, **advanced paternal age** is the generic population‑level correlate of *de novo* mutation rate, but **no study specific to *PBRM1* exists**, and I did not retrieve one; it should not be entered as an annotation for this disease.
- **Sex/family history:** no sex bias and no familial recurrence reported (n = 1).

### 2.3 Protective factors

**No data — genetic or environmental.** No protective allele, modifier, dietary or lifestyle factor has been described. (Note that the one common *PBRM1* variant with a directional effect, rs2251219, carries a *protective* odds ratio (OR 0.87) for mood disorders — but for a different phenotype and with the LD caveat above.)

### 2.4 Gene–environment interactions

**No data.** Nothing retrievable in CTD, PheGenI or the primary literature describes a GxE interaction for germline *PBRM1*. (In the *somatic/oncologic* setting there is a well‑documented **gene–treatment** interaction — PBRM1 loss‑of‑function and immune checkpoint blockade response — described in §12.)

---

## 3. Phenotypes

### 3.1 The honest position

**MONDO:0700122 has no phenotype annotations.** Monarch API v3 returns `has_phenotype_count: 0`. The one published patient (N5, PMID 34906496) is reported **without a clinical description** in the text that could be read verbatim: unlike Patient N4 (*BICRA*, who had DD/ID, hypotonia, short stature and feeding difficulties), **no phenotype, age or sex is given for the *PBRM1* patient N5**. PanelApp's *PBRM1* record has an empty `phenotypes` field. Therefore:

> **There are currently no evidence‑based, disease‑specific phenotype frequencies, severities, ages of onset, progression patterns, or quality‑of‑life data for PBRM1‑related BAFopathy. Any phenotype list entered into a knowledge base for this entity must be labelled as *expected/inferred by analogy to other BAFopathies*, not observed.**

### 3.2 Contextual inference only — what a PBRM1 BAFopathy would be expected to look like

The only defensible inference is from the **cohort ascertainment** (Chen et al. sequenced patients referred for clinical exome sequencing, of whom **~87.8% had neurologic disorders**) and from the sibling BAFopathies. The closest analogue is **ARID2**, the *other* PBAF‑specific subunit, which causes Coffin‑Siris syndrome 6. From Schrier Vergano S et al., "ARID2, a milder cause of Coffin‑Siris Syndrome? Broadening the phenotype with 17 additional individuals," *Am J Med Genet A* 2024;194(6):e63540 (**PMID 38243407**), quoted from the abstract:

> "Although individuals with ARID2 have been reported to have classic features of CSS including hypertrichosis, coarse facial features, short stature, and fifth digit anomalies, as with many of the other CSS genes, there appears to be a spectrum of phenotypes."

and

> "Feeding difficulties, hypotonia, and short stature occur often, and hip dysplasia appears to occur more often than with other genes, however more severe medical challenges such as significant brain and cardiac malformations are rarer."

and

> "Individuals appear to have mild to moderate intellectual impairment and may carry additional diagnoses such as ADHD."

Additional BAFopathy frequency data retrieved (again: **other genes, not PBRM1**):

| Feature | Frequency | Gene / source |
|---|---|---|
| Intellectual disability | 100% | *SMARCA4* CSS4, 40 cases (Chen et al., *Front Genet* 2026, PMID 42703436) |
| Autism spectrum features | 42.5% | same |
| Fifth digit hypoplasia | 55.0% | same |
| Hypertrichosis | 5/8 | mixed CSS cohort (Kolkiran et al., *Eur J Pediatr* 2026, PMID 41795723) |
| Mild terminal fifth phalanx hypoplasia | 3/8 | same |
| Global developmental delay, speech impediment, coarse facial features | characteristic | *SMARCB1* CSS (Bhanushali et al., *Clin Case Rep* 2026, PMID 42707522) |

### 3.3 Suggested HPO terms (all IDs verified against EBI OLS4 in this session)

For a knowledge‑base entry these should be entered with **frequency = "unknown"** and an explicit "inferred by analogy / not observed in PBRM1 cases" qualifier.

**Neurodevelopmental (highest prior):**
- Global developmental delay — **HP:0001263**
- Intellectual disability — **HP:0001249**
- Delayed speech and language development — **HP:0000750**
- Motor delay — **HP:0001270**
- Hypotonia (syn. Muscular hypotonia) — **HP:0001252**
- Autistic behavior — **HP:0000729**; Autism — **HP:0000717**
- Atypical behavior (syn. Behavioral abnormality) — **HP:0000708**
- Seizure — **HP:0001250**
- Abnormal brain morphology — **HP:0012443**; Abnormal corpus callosum morphology — **HP:0001273**; Agenesis of corpus callosum — **HP:0001274**

**Growth / craniofacial / skeletal (CSS‑pattern, speculative here):**
- Short stature — **HP:0004322**; Microcephaly — **HP:0000252**; Macrocephaly — **HP:0000256**
- Coarse facial features — **HP:0000280**; Hypertrichosis — **HP:0000998**
- Aplasia/Hypoplasia of the distal phalanges of the hand — **HP:0009835**; Hypoplastic fifth fingernail — **HP:0008398**
- Scoliosis — **HP:0002650**

**Systemic (CSS‑pattern):**
- Feeding difficulties — **HP:0011968**; Gastroesophageal reflux — **HP:0002020**; Constipation — **HP:0002019**
- Abnormal heart morphology — **HP:0001627**; Ventricular septal defect — **HP:0001629** *(this one has specific mechanistic support from the mouse null — see §6/§15)*
- Hearing impairment — **HP:0000365**; Strabismus — **HP:0000486**; Cryptorchidism — **HP:0000028**

**Oncologic (relevant to the gene, uncertain for the germline NDD entity):**
- Renal cell carcinoma — **HP:0005584**; Clear cell renal cell carcinoma — **HP:0006770**

**Inheritance / modifier terms:**
- Autosomal dominant inheritance — **HP:0000006**; Sporadic — **HP:0003745**; Variable expressivity — **HP:0003828**; Typified by incomplete penetrance — **HP:0003829**

*(Lookup note: "Neoplasm of the kidney" has no exact HPO label; the nearest term is "Renal neoplasm" HP:0009726, returned as a non‑exact match and therefore flagged rather than asserted.)*

### 3.4 Quality‑of‑life impact

**No data.** No EQ‑5D, SF‑36, PROMIS or disease‑specific instrument has been applied to *PBRM1*‑related disease. No per‑phenotype QoL data exist. (Even for the far better‑characterised Coffin‑Siris syndrome, GeneReviews states that in the absence of long‑term studies, information on life span is not available.)

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene

**PBRM1** — "polybromo 1" (HGNC approved name). Identifiers confirmed from the HGNC REST record (`rest.genenames.org/fetch/symbol/PBRM1`, approved 2007‑03‑29, modified 2023‑01‑20) and NCBI Gene esummary (ID 55193):

| Field | Value |
|---|---|
| HGNC ID | **HGNC:30064** |
| Status | Approved; locus type "gene with protein product" |
| Alias symbols | BAF180, PB1, SMARCH1 (HGNC); BAF180, PB1, RCC, SMARCH1 (NCBI) |
| Previous symbols | none |
| Cytogenetic location | **3p21.1** |
| GRCh38 coordinates | chr3:52,544,735–52,685,966, minus strand (per MGI human‑ortholog record); PanelApp gives 3:52,545,352–52,685,917 |
| Exons | **39** (NCBI Gene); RefSeq chromosome NC_000003.12 |
| Ensembl gene | **ENSG00000163939** |
| MANE Select | **ENST00000707071.1 / NM_001405607.1** |
| Legacy RefSeq (HGNC `refseq_accession`) | NM_018165 |
| Transcript used in the one NDD case report | NM_018313.4 |
| Transcript used for gnomAD constraint (ClinGen mirror) | ENST00000296302 |
| CCDS | CCDS2859, CCDS2860, CCDS43099, CCDS87087, CCDS93285, CCDS93286 |
| UniProt | **Q86U86** (PB1_HUMAN) |
| OMIM gene | **606083** |
| HGNC gene groups | "Bromodomain containing" (1232); **"PBAF complex subunits" (1605)** |
| Orthologue IDs | mouse **MGI:1923998**; rat **RGD:1565549**; zebrafish **ZDB-GENE-080926-4** |
| Vega / UCSC / Orphanet gene | OTTHUMG00000152663 / uc003des.3 / ORPHA 434716 |

**NCBI RefSeq gene summary (Feb 2012), key sentences:** "This locus encodes a subunit of ATP-dependent chromatin-remodeling complexes." and "Mutations at this locus have been associated with primary clear cell renal cell carcinoma."

**Note on the OMIM gene–phenotype table:** omim.org returned HTTP 403 and could **not** be read in this session, so I cannot report whether OMIM lists allelic variants or any phenotype relationship for 606083. UniProt's disease block (below) lists only renal cell carcinoma.

**Chromosomal abnormalities:** No *PBRM1*‑specific recurrent CNV syndrome exists. ClinVar's pathogenic records overlapping *PBRM1* that I sampled were all **large 3p copy‑number events** (e.g. 3p26.3‑14.3 gain, 3p21.2‑21.1 loss, 3p21.2‑14.2 loss, 3p26.3‑q29 whole‑arm gain), i.e. contiguous‑gene events in which *PBRM1* is one of dozens of genes, with conditions listed as "not provided"/"not specified"/"See cases." Chen et al. explicitly state that **no homozygous or heterozygous gene‑disrupting CNVs were found in the candidate genes**, though small heterozygous CNVs could not be excluded. A targeted search for a 3p21.1 microdeletion syndrome implicating *PBRM1* returned nothing; published 3p21.31 deletion cases implicate *SETD2* and are framed as contiguous‑gene effects.

### 4.2 Pathogenic variants

**The single germline NDD‑associated variant (human):**

| Attribute | Value (Chen CA et al., *Genet Med* 2022, PMID 34906496, Patient N5) |
|---|---|
| Variant | **c.1542‑3C>G** (NM_018313.4), intron 14 |
| Genomic (hg19) | chr3:52,651,557 |
| Type | **Splice region (intronic, −3 acceptor)** |
| Zygosity | Heterozygous |
| Inheritance | ***De novo*** — "A de novo heterozygous c.1542–3C>G variant in PBRM1 was identified in Patient N5" |
| Predicted effect | Activates a cryptic splice acceptor 2 bp 5′ of the canonical acceptor. **SpliceAI: acceptor loss 0.91; acceptor gain (1 bp upstream) 0.98** |
| Functional confirmation | **None.** No RNA was available; the splicing change was not experimentally confirmed |
| Gene‑level constraint in that table | **pLI 1.00** |
| gnomAD allele frequency | **0.00** |
| ACMG/AMP classification in the paper | *de novo* **VUS** in a candidate gene (the paper's P/LP tallies — 81 pathogenic, 38 likely pathogenic, 8 *de novo* VUS — apply to the 11 *known* BAFopathy genes) |

**ClinVar status (NCBI E‑utilities, retrieved this session):** `PBRM1[gene]` returns **180 records total**. Conditions attached to the records sampled were "not provided," "not specified," "See cases," and "Hereditary cancer." **No ClinVar record was found that asserts a *PBRM1* neurodevelopmental condition.** *(Methodological caveat: my classification‑stratified counts are unreliable — the `[Clinical Significance]` field tag was silently remapped by Entrez to `[All Fields]`, which is why the "pathogenic" query returned a record classified Likely benign. The 180 total is sound; the per‑class breakdown is not, and I am not reporting it as a result.)*

**Population allele frequency:** The causative variant has gnomAD AF 0.00. Gene‑level LoF counts in gnomAD could not be retrieved (browser is JS‑only; GraphQL requires POST; DECIPHER returned 500; GeneCards returned 403).

**Somatic vs germline — this distinction is central to *PBRM1*:**

*PBRM1* is overwhelmingly characterised as a **somatic** tumour‑suppressor gene.

- **Clear cell renal cell carcinoma (ccRCC):** Varela I et al., "Exome sequencing identifies frequent mutation of the SWI/SNF complex gene PBRM1 in renal carcinoma," *Nature* 2011;469(7331):539–542 (**PMID 21248752**, DOI 10.1038/nature09639, PMC3030920; erratum *Nature* 2012;484(7392):130). Verbatim from the abstract: *PBRM1* is identified **"as a second major ccRCC cancer gene, with truncating mutations in 41% (92/227) of cases."** This is the second most frequently mutated gene in ccRCC after *VHL*.
- **UniProt disease annotation** for Q86U86 is **"Renal cell carcinoma" (DI‑02254, MIM 144700)**, with the note that the disease is caused by variants affecting this gene; evidence **PMID 21248752**. The retrieved natural‑variant list includes somatic ccRCC changes at residues 57, 232, 540, 597, 621, 661, 674 and 1204 (list truncated at 1204 in the retrieved JSON).
- **Other tumours (frequencies retrieved this session):** cholangiocarcinoma **10.1%** vs 0% in gallbladder cancer (p = 0.003), with PBRM1 mutation associated with improved survival in an MSKCC external cohort (HR 0.50, P = 0.02) — Lu W et al., *Sci Rep* 2026, **PMID 42259884**; sarcomatoid carcinoma of the upper urinary tract **12%** in 121 cases, enriched vs conventional UTUC (p < 0.05) — Jaime‑Casas S et al., *Cancers* 2026;18(14):2352, **PMID 42512413**. Meningioma: case‑level only (PBRM1 + BAP1 functional loss with prolonged pembrolizumab response, Reusch E et al., *Front Oncol* 2025, **PMID 41199851**). *Mesothelioma and bladder PBRM1‑specific frequencies were not retrieved.* COSMIC and cBioPortal could not be queried (cBioPortal endpoint 404).

**Germline *PBRM1* and cancer predisposition (distinct from the NDD entity):** Benusiglio PR et al., "A germline mutation in PBRM1 predisposes to renal cell carcinoma," *J Med Genet* 2015;52(6):426–430 (**PMID 25911086**, DOI 10.1136/jmedgenet-2014-102912). Screening 35 unrelated patients with ccRCC plus ≥1 affected first‑degree relative identified one germline frameshift, **c.3998_4005del (p.Asp1333Glyfs)**. The proband's mother, sister and one niece also had ccRCC; **the three affected relatives were carriers and an unaffected sister was not**, consistent with autosomal‑dominant transmission. Tumours showed **loss of heterozygosity and loss of PBRM1 protein expression** — a classic two‑hit tumour‑suppressor pattern. The authors state that international studies are needed to estimate *PBRM1*'s contribution to RCC susceptibility **and to estimate penetrance**; they provide no penetrance figure.

> **Knowledge‑base implication:** a germline *PBRM1* LoF allele has documented evidence for **RCC predisposition** (one family) and for a **neurodevelopmental disorder** (one patient). Whether these are two phenotypes of one allelic series, or two independent weak associations, is unresolved. No patient has been reported with both.

**Functional consequences:** The expected mechanism is **loss of function → haploinsufficiency**, supported by (i) pLI 1.00 / LOEUF 0.23 / %HI 9.54; (ii) the predominance of **truncating** somatic mutations in ccRCC (41% truncating, PMID 21248752); (iii) UniProt's functional annotation that PBRM1 "is required for the stability of the SWI/SNF-B (PBAF) complex" and "acts as a negative regulator of cell proliferation"; and (iv) GO:0008285 (negative regulation of cell population proliferation) annotated **IMP from PMID 21248752**. **No dominant‑negative or gain‑of‑function mechanism has been demonstrated for PBRM1.** This contrasts with *SMARCA4*, where GeneReviews lists dominant‑negative/gain‑of‑function as the CSS mechanism, and matches *ARID2*, listed as loss of function.

### 4.3 Modifier genes

**No data.**

### 4.4 Epigenetic information

- *PBRM1*'s protein product is itself an **epigenetic reader/effector** (§6), so "epigenetic changes" and "molecular mechanism" are the same axis for this disease.
- **DNA methylation episignature:** A **BAFopathy episignature exists** and is used clinically (EpiSign). Retrieved supporting examples: a deep intronic *ARID1A* deletion case showed a BAFopathy‑like methylation profile (Schuhmann et al. 2026, PMID 42173440); an *ARID1A* fetal hydrocephalus case mapped to the BAFopathy episignature group (Tanaka et al., *Eur J Med Genet* 2025, PMID 40962111, DOI 10.1016/j.ejmg.2025.105048); a 97‑patient NDD episignature study found *SMARCB1* variants to be an exception (Trajkova et al., *HGG Adv* 2024, **PMID 38751117**, DOI 10.1016/j.xhgg.2024.100309); *SOX11* has its own distinct profile (Al‑Jawahiri et al., *Genet Med* 2022, **PMID 35341651**).
- **No PBRM1‑specific (or ARID2‑specific) episignature has been reported.** I searched specifically and found none. This is a concrete, tractable gap: establishing whether the single reported patient's methylome falls within the BAFopathy episignature would be the single most informative next experiment for validating this disease entity.

---

## 5. Environmental Information

- **Environmental factors:** **Not applicable / no data.** This is a Mendelian, germline‑variant‑caused entity. No toxin, radiation, pollution or occupational exposure has been linked to it. CTD/TOXNET content specific to germline *PBRM1* disease was not retrieved and I have no evidence any exists.
- **Lifestyle factors:** **Not applicable / no data.** No smoking, diet, exercise or alcohol association reported. (Smoking is an established ccRCC risk factor generally, but no interaction with *PBRM1* genotype was retrieved and none should be asserted.)
- **Infectious agents:** **Not applicable.** No infectious trigger.

One mechanistically interesting but non‑clinical environmental link: PBAF, via Baf180, participates in **metal‑responsive transcription through MTF1** (Carulli N et al., 2026, **PMID 42246576**, DOI 10.1093/mtomcs/mfag019; and a PBAF–MTF1 metal‑homeostasis study, PMC13294679), with the principle that transcription‑factor binding alone is insufficient for activation without appropriate chromatin remodelling. This is in vitro/myoblast work with **no demonstrated clinical relevance** to this disease.

---

## 6. Mechanism / Pathophysiology

### 6.1 Ordered causal chain

Steps marked **[D]** are demonstrated in some system (human, mouse, worm or in vitro, as noted); steps marked **[I]** are **inferred** and have not been shown for germline *PBRM1* disease.

1. A **heterozygous germline loss‑of‑function or splice‑disrupting variant arises *de novo* in *PBRM1*** (e.g. c.1542‑3C>G, SpliceAI acceptor loss 0.91 / cryptic gain 0.98) — **[D, human, n = 1]** (PMID 34906496) — which **leads to** aberrant splicing of the *PBRM1* transcript. **[I — no RNA study was performed; the authors state the lack of RNA studies obscured the biological significance.]**
2. Aberrant splicing **results in** a premature termination codon or in‑frame disruption and, via nonsense‑mediated decay or protein destabilisation, **reduced functional PBRM1/BAF180 protein to ~50%** — **[I]**, supported by *PBRM1*'s extreme LoF intolerance (pLI 1.00, LOEUF 0.23, %HI 9.54) which implies haploinsufficiency is not tolerated.
3. Reduced PBRM1 **leads to** destabilisation and mis‑targeting of the **PBAF (polybromo‑associated BAF) chromatin‑remodelling complex** — **[D, in vitro/biochemical]**. UniProt states PBRM1 "is required for the stability of the SWI/SNF-B (PBAF) complex." PBAF is the SMARCA4/BRG1‑containing assembly defined by its unique subunits PBRM1, ARID2 and BRD7, alongside SMARCB1, ACTL6A/B, SMARCE1, SMARCD1/2/3, SMARCC1/2 and actin (UniProt Q86U86 subunit comment; GO:0016514 SWI/SNF complex, IDA, PMID 8895581). Cryo‑EM has resolved the **13‑subunit human PBAF bound to an acetylated nucleosome**, revealing six histone‑binding and four DNA‑binding modules (Wang L et al., *Nat Commun* 2022, **PMID 36496390**, DOI 10.1038/s41467-022-34859-5), and Reactome places PBRM1 in a BRD7:PHF10:PBRM1 module (reaction **R-HSA-9933237**).
4. PBAF mis‑targeting **results in** failure of **nucleosome recognition and placement at specific loci**. PBRM1 is the complex's targeting/reader subunit: its **six tandem bromodomains** "cooperate in binding of nucleosomes acetylated at histone H3 lysine 14" (H3K14ac), and **BD2 and BD4 additionally bind double‑stranded RNA elements**, which facilitates chromatin association — **[D, in vitro]** (De Silva SM et al., *Nucleic Acids Res* 2023;51(8):3631–3649, **PMID 36808431**, DOI 10.1093/nar/gkad072). PBRM1's **two BAH domains** read SETD2‑written methyl marks — **[D]** ("PBRM1 binds SETD2 methyl marks via BAH domains"; Karki M et al., *Sci Adv* 2021;7(14):eabf2866, **PMID 33811077**).
5. **Branch A — transcriptional.** Loss of PBAF targeting **leads to** dysregulated RNA Pol II transcription at PBAF‑dependent loci (GO:0006357 regulation of transcription by RNA polymerase II; GO:0000122 negative regulation). **[D, model systems.]** In the specific neurodevelopmental case worked out to date, PBRM1 acts as a **direct transcriptional repressor of *Ccl5***: "PBRM1 directly binds to the Ccl5 promoter and represses the expression of CCL5" — **[D, mouse]** (Duan YY et al., *Adv Sci* 2026;e78086, **PMID 42893407**, PMC13676817, DOI 10.1002/advs.78086).
6. **Branch A continued — the microglia→NSPC axis (the only worked‑out neurodevelopmental mechanism).** PBRM1 loss in **microglia** (CL:0000129) **leads to** de‑repression and elevated secretion of **CCL5**, which **acts on CCR1/CCR5 on neural stem/progenitor cells** and **activates β‑catenin signalling**, which **results in** excessive NSPC proliferation and neuronal differentiation — i.e. **excessive neurogenesis** — which **leads to** ASD‑like behaviour. **[D, mouse conditional knockout.]** Verbatim from the abstract: *"Elevated CCL5 promotes the proliferation and neuronal differentiation of neural stem/progenitor cells (NSPCs) via the CCR1/5-β-catenin signaling pathway."* And: *"microglial PBRM1 deficiency leads to altered microglial clusters, excessive neurogenesis, and ASD-like behaviors in mice."* Critically, the chain is **pharmacologically reversible**: *"pharmacological blockade of CCR1/5 ameliorates behavioral deficits in Pbrm1 cKO mice."* The authors frame this as *"a previously unrecognized microglia–NSPC communication mechanism linking PBRM1 dysfunction to aberrant neurodevelopment."* **[I for humans — the human premise cited by that paper ("Missense mutations in Polybromo 1 (Pbrm1) … have been identified as a risk factor for ASD") is not supported by any primary human cohort I could retrieve, and SFARI Gene does not list PBRM1.]**
7. **Branch B — genome/centromere stability.** PBRM1 loss **leads to** failure to direct PBAF to **pericentromeric chromatin** (GO:0005721), which **results in** compromised centromere and pericentromere integrity and a shift in PBAF and H3K9‑methylation binding patterns, which **creates a dependence on the spindle assembly checkpoint**. **[D, human cells]** (Lane KA et al., "PBRM1 directs PBAF to pericentromeres and protects centromere integrity," *Nat Commun* 2025;16:1980, **PMID 40011561**, PMC11865495, DOI 10.1038/s41467-025-57277-9).
8. **Branch B continued — cytoskeletal.** PBRM1's BAH domains read SETD2 methyl marks **on microtubules** (not only on histones) and **recruit PBAF components to the mitotic spindle**; loss of SETD2 methylation or pathogenic BAH‑domain mutation **leads to** loss of this recruitment and **results in genomic instability**. **[D]** (PMID 33811077). GO support: GO:0000776 kinetochore (NAS, PMID 11078522); GO:0030071 regulation of mitotic metaphase/anaphase transition and GO:2000781 positive regulation of double‑strand break repair (both NAS, PMID 25066234).
9. **Branch C — proliferation/senescence.** PBRM1 loss **leads to** loss of negative regulation of proliferation (GO:0008285, IMP, PMID 21248752) and altered G0→G1 and G1/S control (GO:0070316, GO:2000045, NAS from PMIDs 11790558 and 10778858), and **BAF180 regulates cellular senescence and hematopoietic stem cell homeostasis through p21** **[D, mouse]** (Lee H et al., *Oncotarget* 2016, **PMID 26992241** — *flag: metadata retrieved from a model‑extracted summary of the Europe PMC response, abstract not read verbatim*).
10. **Branch D — the oncogenic branch (somatic, well established).** Biallelic somatic PBRM1 loss in a renal tubule cell, **on a *VHL*‑null background**, **rescues VHL‑dependent replication stress** that would otherwise constrain growth, which **permits** proliferation and **leads to** multifocal ccRCC — **[D, mouse + human]**: "Loss of PBRM1 rescues VHL dependent replication stress to promote renal carcinogenesis"; combined *Vhl*/*Pbrm1* deletion in mouse kidney produced **"fully-penetrant, multifocal carcinomas"** (Espana‑Agusti J, Warren A, Chew SK, Adams DJ, Matakidou A, *Nat Commun* 2017;8:2026, **PMID 29229903**, PMC5725450, DOI 10.1038/s41467-017-02245-1).
11. **Branch E — immune.** PBAF loss (Pbrm1/Arid2/Brd7) **leads to** increased tumour‑cell sensitivity to **interferon‑γ**, which **results in** enhanced secretion of effector‑T‑cell‑recruiting chemokines and **sensitisation to T‑cell–mediated killing** — **[D, mouse genome‑scale CRISPR screen]** (Pan D et al., "A major chromatin regulator determines resistance of tumor cells to T cell–mediated killing," *Science* 2018, **PMID 29301958**). Note the mechanistic convergence with step 6: in both branches, **PBRM1 loss de‑represses chemokine output**.
12. **Branch F — cardiac development (the strongest organ‑level phenotype of complete loss).** Homozygous *Baf180/Pbrm1* ablation in mouse **leads to** "severe hypoplastic ventricle development and trophoblast placental defects" and mid‑gestation lethality — **[D, mouse]** (Wang Z, Zhai W, Richardson JA, Olson EN, Meneses JJ, Firpo MT, Kang C, Skarnes WC, Tjian R. "Polybromo protein BAF180 functions in mammalian cardiac chamber maturation," *Genes Dev* 2004;18(24):3106–3116, **PMID 15601824**, DOI 10.1101/gad.1238104, PMC535920). Candidate downstream targets named by the authors: **retinoic‑acid response genes CRABPII and RARβ2, and S100A13**. Aggregation analyses indicated the cardiac defect is a **direct** consequence of BAF180 ablation rather than secondary to the placental defect.

**Where the chain breaks:** steps 1–2 (human variant → reduced protein) and step 6's human relevance are the unvalidated links. Everything from step 3 onward is solid *PBRM1/PBAF* biology; what is missing is the demonstration that **heterozygous** human loss produces any of it.

### 6.2 Molecular pathways

- **ATP‑dependent chromatin remodelling (SWI/SNF–PBAF)** — the core pathway. Reactome entities retrieved: **R‑HSA‑389254** (PBRM1 protein, nucleoplasm), **R‑HSA‑9932829** (PBRM1 ATPase complex), **R‑HSA‑9933237** (PBRM1‑containing ATPase complex binds SMARCC dimer:SMARCDs:SMARCE1:SMARCB1:ARID2:BRD7:PHF10), **R‑HSA‑9824981** (MITF‑M and the SWI/SNF complex bind the TYR promoter — PBAF with PBRM1 in 501MEL cells), **R‑HSA‑9988507** (PHF6 binds SWI/SNF complexes; PHF6 associates with PBRM1).
- **Canonical Wnt/β‑catenin** (GO:0060070) — downstream of CCL5/CCR1/5 in the microglia–NSPC axis (PMID 42893407).
- **Chemokine signalling** (GO:0070098) — CCL5→CCR1/CCR5.
- **Interferon‑γ response** — PBAF loss increases IFN‑γ sensitivity (PMID 29301958).
- **HIF axis** — PBRM1's effects in ccRCC are context‑dependent on HIF1α/HIF2α status, and one study concluded BAF180 is "not a clear-cut tumor suppressor or oncogene" in that setting (*Oncogenesis* 2016, oncsis201689). *I was unable to retrieve the PBRM1–HIF/interferon mechanism abstracts directly (Europe PMC returned HTTP 503 on that query), so this point is reported at lower confidence.*
- **Retinoic‑acid signalling** — CRABPII, RARβ2 as BAF180‑dependent cardiac targets (PMID 15601824).
- **Metal‑responsive transcription via MTF1** (PMID 42246576).

### 6.3 Cellular processes and GO terms

| Process | GO ID | Evidence note |
|---|---|---|
| chromatin remodeling | **GO:0006338** | IEA, IBA, NAS (PMID 10078207), TAS |
| ATP-dependent chromatin remodeler activity | **GO:0140658** | complex‑level |
| nucleosome binding | **GO:0031491** | H3K14ac nucleosomes, PMID 36808431 |
| regulation of transcription by RNA polymerase II | **GO:0006357** | NAS, ComplexPortal, PMID 18809673 |
| negative regulation of transcription by RNA Pol II | **GO:0000122** | CCL5 repression, PMID 42893407 |
| neurogenesis | **GO:0022008** | mouse, PMID 42893407 |
| neural precursor cell proliferation | **GO:0061351** | mouse, PMID 42893407 |
| canonical Wnt signaling pathway | **GO:0060070** | mouse, PMID 42893407 |
| chemokine-mediated signaling pathway | **GO:0070098** | mouse, PMID 42893407 |
| microglial cell activation | **GO:0001774** | mouse, PMID 42893407 |
| oligodendrocyte differentiation | **GO:0048709** | mouse, PMID 37371026 |
| DNA damage response | **GO:0006974** | — |
| mitotic cell cycle | **GO:0000278** | TAS, PMID 11078522 |
| cellular senescence | **GO:0090398** | mouse, PMID 26992241 |
| heart development | **GO:0007507** | mouse, PMID 15601824 |
| cardiac muscle tissue morphogenesis | **GO:0055008** | mouse, PMID 15601824 |

Additional directly annotated BPs from QuickGO (UniProtKB:Q86U86): GO:0008285 negative regulation of cell population proliferation (**IMP, PMID 21248752**); GO:0030071 and GO:2000781 (NAS, PMID 25066234); GO:0045582 positive regulation of T cell differentiation (NAS, PMID 12110891); GO:0045597 positive regulation of cell differentiation (NAS, PMID 11790558); GO:0045663 positive regulation of myoblast differentiation (NAS, PMID 15985610); GO:0070316 regulation of G0→G1 transition; GO:2000045 regulation of G1/S transition; GO:2000819 regulation of nucleotide‑excision repair (NAS, PMID 12215535).

### 6.4 Protein dysfunction

**PBRM1 / Protein polybromo‑1 (hPB1 / BAF180 / Polybromo‑1D), 1,689 aa, 9 isoforms** (UniProt Q86U86, entry version 199, last annotation update 2026‑11‑04, protein existence level 1). Domain architecture with verbatim coordinates:

- **Bromodomain 1:** 41–151 · **BD2:** 177–287 · **BD3:** 381–487 · **BD4:** 518–625 · **BD5:** 653–763 · **BD6:** 769–879 — six tandem bromodomains, more than any other human protein
- **BAH domain 1:** 956–1074 · **BAH 2:** 1156–1272
- **HMG box (DNA binding):** 1379–1447
- **Disordered regions:** 1–39, 155–177, 487–517, 625–646, 902–941, 1106–1133, 1354–1378, 1431–1460

Pfam: PF00439 (bromodomain), PF01426 (BAH), PF00505 (HMG_box). InterPro: IPR001487, IPR001025, IPR009071, plus IPR018359, IPR036427, IPR036910, IPR037382, IPR037968, IPR043151. **30 PDB entries** are cross‑referenced (including 2KTB, 3G0J, 3HMF, 3IU5/6, 3K2J, 3LJW, 3MB4, 3TLP, 4Q0N/O, 4Y03, 5E7D, 5FH6/7/8, 5HRV/W/X, 5II1/2, 5IID, 6OXB, 6ZN6, 6ZNV, 6ZS3/4, 7VDV, 7Y8R, 8FTA) — *flag: the PDB/Pfam/InterPro lists came from a model‑extracted summary of a truncated UniProt JSON and should be re‑verified before ingestion; the domain coordinates above were read verbatim.*

**Functional mode of dysfunction:** loss of function. UniProt: PBRM1 "is involved in transcriptional activation and repression of select genes through chromatin remodeling," "is required for the stability of the SWI/SNF-B (PBAF) complex," and "acts as a negative regulator of cell proliferation." No misfolding or aggregation mechanism is described. **No dominant‑negative mechanism has been demonstrated.**

**PTMs** (UniProt, retrieved portion): extensive phosphorylation (phosphoserine at S10, S39, S131, S178, S316, S319, S353, S355, S371, S375, S498, S509, S636, S648, S689, S948, S987, S1119, S1405, S1453; phosphotyrosine at Y134, and Y1289 inferred from mouse Q8BSQ9); N6‑acetyllysine at K414 (inferred from mouse); and a strikingly dense set of **SUMO2 cross‑links** at K96, K154, K210, K425, K471, K511, K591, K638, K653, K1106, K1111, K1167, K1293 (also SUMO1), K1308, K1398, K1642, K1654, K1656.

**Binary interactions** with IntAct experiment counts: ARID2 (5), SMARCA4 (7), CHD7 (4), BRD1 (2), HIV‑1 Tat (2).

### 6.5 Metabolic changes, immune involvement, tissue damage, biochemical abnormalities

- **Metabolic changes:** **No data** for the germline disease. The only metabolic link retrieved is PBAF/Baf180–MTF1 metal homeostasis in myoblasts (PMID 42246576) — in vitro, not clinical. No HMDB/metabolomics signature exists.
- **Immune system involvement:** PBAF loss increases IFN‑γ sensitivity and chemokine secretion in tumour cells (PMID 29301958); PBRM1 loss in microglia de‑represses CCL5 (PMID 42893407); GO:0045582 positive regulation of T cell differentiation is annotated (NAS, PMID 12110891); mSWI/SNF complexes regulate T‑cell activation and exhaustion (Battistello E et al., *Mol Cell* 2023;83(8), **PMID 36944333**). **However, no immunodeficiency, autoimmunity or chronic inflammation has been reported in any human with germline *PBRM1* variation.**
- **Tissue damage mechanisms:** the retrieved mechanisms are **replication stress** (PMID 29229903), **genomic/centromere instability** (PMIDs 40011561, 33811077) and **developmental hypoplasia** (PMID 15601824) — not oxidative stress, ischaemia, fibrosis or necrosis.
- **Biochemical abnormalities:** **None.** PBRM1 is not an enzyme, receptor or ion channel; there is **no enzyme assay, metabolite or biochemical marker** for this disease.

### 6.6 Molecular profiling and advanced technologies

- **Transcriptomics:** Human disease transcriptomics: **none.** Mouse: the microglial *Pbrm1* cKO study performed "integrated molecular analyses" including RNA‑level work (PMID 42893407) — **specific GEO accessions could not be retrieved**, because the PMC full text returned a reCAPTCHA interstitial and Wiley/Europe PMC full text returned HTTP 403 in this session. **Expression baseline:** Human Protein Atlas classifies *PBRM1* RNA as **low tissue specificity**, with protein annotated as **tissue enhanced (lymphoid tissue)** and cytoplasmic+nuclear expression in most tissues; HPA/GTEx brain coverage spans cerebral cortex, hippocampal formation, amygdala, basal ganglia, thalamus, hypothalamus, midbrain, cerebellum, pons, medulla oblongata and spinal cord (exact nTPM values not retrieved). PBRM1 protein is reported to be strongly present in the **E14.5 mouse cortical ventricular and subventricular zones and largely absent from the cortical plate** (secondary report in PMC5900035, Sokpor G, Castro‑Hernandez R, Rosenbusch J, Staiger JF, Tuoc T, *Front Neurosci* 2018;12:226, **PMID 29686607** — *flag: this expression statement appeared in a search snippet of the review, not in the abstract I retrieved verbatim*).
- **Proteomics:** no disease proteomics. Interactome data from IntAct/UniProt as above.
- **Metabolomics / lipidomics:** **no data.**
- **Single‑cell analysis:** the mouse microglial cKO study reports **"altered microglial clusters"** (PMID 42893407, abstract verbatim), implying single‑cell or cluster‑level profiling; details not retrievable.
- **Spatial transcriptomics:** **no data.**
- **Functional genomics screens:** *Pbrm1* is a hit in a **genome‑scale in vivo CRISPR‑Cas9 screen** for tumour‑cell resistance to T‑cell killing (PMID 29301958), and in an **in vivo CRISPR/Cas9 screen identifying Pbrm1 as a regulator of myeloid leukemia development in mice** (Li BE et al., *Blood Adv* 2023;7(18), **PMID 37428871** — *flag: summary‑derived metadata*). DepMap was not queried.
- **Multi‑omics integration:** the Valencia/Kadoch 2023 structural‑variant integration (PMID 37500730) is the relevant multi‑cohort resource; its finding for PBRM1 is **negative** for NDD enrichment.

---

## 7. Anatomical Structures Affected

**Caveat:** no human organ involvement has been documented for this entity (n = 1, phenotype unreported). The following is derived from model systems and from PBRM1 expression, and should be entered as **inferred**.

### 7.1 Organ level

**Primary (inferred, model‑derived):**
- **Brain** — UBERON:0000955; **central nervous system** — UBERON:0001017. Basis: ascertainment in a neurologic exome cohort (PMID 34906496) and the mouse ASD‑like phenotype (PMID 42893407).
- **Cerebral cortex** — UBERON:0000956; **ventricular zone** — UBERON:0003053 (PBRM1‑rich germinal zone at E14.5).
- **Hippocampal formation** — UBERON:0002421 (note: "hippocampus" has no exact UBERON label; the exact‑label query returned no match, with synonym hits "Ammon's horn" UBERON:0001954 and "hippocampal formation" UBERON:0002421); **dentate gyrus of hippocampal formation** — UBERON:0001885 (site of the excessive neurogenesis phenotype).
- **Corpus callosum** — UBERON:0002336 (white matter, given the oligodendrocyte phenotype).
- For "subventricular zone," the exact label is not in UBERON; the nearest exact‑synonym hit is **"postnatal subventricular zone" UBERON:0004922**, which should be chosen deliberately rather than assumed.

**Secondary / other organs with model‑system evidence:**
- **Heart** — UBERON:0000948; **cardiac ventricle** — UBERON:0002082. Basis: severe ventricular hypoplasia and ventricular septal defect in *Baf180*‑null mice (PMID 15601824). **No human cardiac phenotype has been reported.**
- **Kidney** — UBERON:0002113. Basis: ccRCC (somatic, PMID 21248752) and the one germline RCC family (PMID 25911086).
- **Placenta/trophoblast** — trophoblast placental defects in the mouse null, with strongest expression in labyrinthine‑layer trophoblast at mid‑gestation (PMID 15601824).

**Body systems:** nervous (primary, inferred); cardiovascular and renal/urinary (model‑ and oncology‑derived); haematopoietic (mouse HSC homeostasis, PMID 26992241; IMPC flags hematopoietic system).

### 7.2 Tissue and cell level

| Cell type | CL ID | Evidence |
|---|---|---|
| **microglial cell** | **CL:0000129** | The cell of origin in the only neurodevelopmental mechanism worked out (PMID 42893407, mouse cKO) |
| **neural stem cell** (syn. neuronal stem cell) | **CL:0000047** | Target of CCL5/CCR1‑5/β‑catenin; proliferation and differentiation both increased (PMID 42893407) |
| **neuron** | **CL:0000540** | Excessive neuronal differentiation (mouse); PBAF cell‑type‑specific roles in motor‑neuron identity (*C. elegans*, PMID 41390837) |
| **granule cell** | **CL:0000120** | Dentate gyrus neurogenesis product — *inferred, not directly stated* |
| **radial glial cell** | **CL:0000681** | *Inferred* from VZ/SVZ PBRM1 expression |
| **oligodendrocyte precursor cell** | **CL:0002453** | Pbrm1 co-localises with Pdgfra⁺ OPCs; early deletion reduces entry into the pre‑myelinating state (PMID 37371026) |
| **oligodendrocyte** | **CL:0000128** | Fewer myelinating oligodendrocytes after early Pbrm1 loss (PMID 37371026) |
| **cardiac muscle cell** | **CL:0000746** | Ventricular hypoplasia (PMID 15601824) |
| **kidney epithelial cell** | **CL:0002518** | ccRCC cell of origin; Pax8‑CreERT2 renal tubule models (PMID 29229903) |

*Note from the oligodendrocyte study: Pbrm1 is also found in astrocytes and neurons, not only oligodendroglial cells — i.e. expression is broad, and the phenotype is driven by cell‑type‑specific requirement rather than restricted expression.*

**Tissue types affected:** nervous tissue (primary, inferred); cardiac muscle and placental trophoblast (model); renal epithelium (oncologic).

### 7.3 Subcellular level

| Compartment | GO CC ID | Evidence |
|---|---|---|
| **nucleus** | **GO:0005634** | IDA (PMID 25593309); UniProt SL‑0191 |
| **chromatin** | **GO:0000785** | NAS (PMID 12192000) |
| **nucleosome** | **GO:0000786** | H3K14ac nucleosome binding (PMID 36808431) |
| **SWI/SNF complex** | **GO:0016514** | IDA (PMID 8895581) |
| **pericentric heterochromatin** | **GO:0005721** | PMID 40011561 |
| **microtubule** | **GO:0005874** | BAH‑domain reading of methylated microtubules; mitotic spindle recruitment (PMID 33811077) |
| nuclear chromosome / kinetochore / nucleoplasm / nuclear matrix / RSC‑type complex | GO:0000228 / GO:0000776 / GO:0005654 / GO:0016363 / GO:0016586 | QuickGO annotations (NAS/IDA/TAS; PMIDs 11078522, 9128241, 8804307) |

For completeness in a neural context: **npBAF complex GO:0071564** and **nBAF complex GO:0071565** are the developmentally switched neural BAF assemblies; *PBRM1 is a PBAF subunit and is not itself an npBAF/nBAF‑defining subunit*, so these terms should be used only as pathway context, not as PBRM1 localisations.

### 7.4 Localization and lateralization

**No data.** No lateralization (unilateral/bilateral/asymmetric) has been described, as no human imaging phenotype has been reported. By analogy to BAFopathies generally, CNS findings would be expected to be **bilateral and midline‑involving** (e.g. corpus callosum), but this is unsupported for *PBRM1*.

---

## 8. Temporal Development

**All content in this section is inferred; no natural‑history data exist for MONDO:0700122.**

### 8.1 Onset

- **Expected age of onset: congenital / infantile–early childhood**, by the nature of a *de novo* germline chromatin‑remodeller variant and by analogy to all other BAFopathies, where developmental delay is recognised in infancy. The single reported patient was ascertained through diagnostic exome sequencing in a predominantly paediatric neurologic cohort (Chen et al. studied referrals from March 2012 to December 2019, ~87.8% with neurologic disorders), but **their age is not reported**.
- **Onset pattern: insidious/chronic (developmental)** — inferred. There is no evidence of acute or episodic onset.
- **Mechanistic critical window (model‑derived, striking):** the *timing* of Pbrm1 loss determines the phenotype in the oligodendrocyte lineage — deletion in **late** OPCs produced no major change in differentiation or myelination, whereas deletion **shortly after progenitor specification** reduced the number of cells entering the pre‑myelinating state, with knock‑on reduction in myelinating oligodendrocytes (Waldhauser V, Baroti T, Fröb F, Wegner M. *Cells* 2023;12(12):1556, **PMID 37371026**, DOI 10.3390/cells12121556). This is direct evidence for a **narrow developmental critical period**.

### 8.2 Progression

- **Disease stages:** **not defined.** No staging system exists.
- **Progression rate:** **no data.** BAFopathies are generally static/non‑degenerative developmental disorders, but this has not been assessed for *PBRM1*.
- **Course pattern:** expected **stable (non‑progressive developmental)** — inferred only.
- **Duration:** expected **chronic, lifelong** — inferred only.

### 8.3 Patterns

- **Remission:** none expected; **no data.**
- **Critical periods:** the embryonic/early‑postnatal neurogenic window is the mechanistically implicated vulnerability period (PMIDs 42893407, 37371026). In the mouse, pharmacological CCR1/5 blockade **ameliorated** behavioural deficits — a demonstrated, if preclinical, **window of intervention opportunity**.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

- **Prevalence: unknown — no estimate exists.** There is no Orphanet prevalence class, no GBD entry, no registry.
- **Incidence: unknown.**
- The only denominator‑bearing datum available is from Chen et al.: **1 candidate *PBRM1* case in 16,243 clinical exomes (≈6 per 100,000 exome referrals; ≈0.006%)** — and this is an **ascertainment‑biased referral frequency in a cohort that was ~87.8% neurologic, not a population prevalence**. It should not be converted into a population rate.
- For scale, in the same cohort 127 patients had P/LP or *de novo* VUS across the 11 *known* BAFopathy genes, with **ARID1B accounting for 39%** and **SMARCA4 ~10%** of BAFopathy molecular diagnoses. *PBRM1* contributed **none** of the established diagnoses.
- For contrast, GeneReviews states that fewer than 200 individuals with molecularly confirmed Coffin‑Siris syndrome had been reported, with the diagnosis described as rare and that figure likely an underestimate.

### 9.2 Genetic parameters

- **Inheritance pattern: autosomal dominant**, asserted by the MONDO relation RO:0004003 (germline) and by the *de novo* heterozygous nature of the index variant. **PanelApp's `mode_of_inheritance` field for *PBRM1* is empty**, i.e. Genomics England has not assigned one. The *germline RCC* family showed AD transmission (PMID 25911086).
- **Penetrance: unknown.** PanelApp carries `penetrance: "Complete"` on its *PBRM1* record, but this is a default field on a **Red‑rated, zero‑publication** entry and should not be treated as a curated assertion. The germline RCC authors explicitly called for studies to "estimate penetrance" and gave no figure.
- **Expressivity: unknown.** Variable expressivity is the norm across BAFopathies (a 2023 Leiden thesis on BAFopathies notes that specific variants in a single gene can lead to different syndromes), but **n = 1** precludes any statement here.
- **Genetic anticipation: not applicable.** *PBRM1* is not a repeat‑expansion locus.
- **Germline mosaicism: no data.** (Mosaicism is documented in other BAFopathies — e.g. an *ARID1B* variant inherited from a mosaic father in the Chen et al. cohort, and low‑level germline mosaicism for a *SMARCA2* missense variant — so it is a plausible but unobserved mechanism here.)
- **Founder effects: none known.** The index variant is absent from gnomAD (AF 0.00).
- **Consanguinity: not applicable** to a *de novo* dominant mechanism; no biallelic *PBRM1* disease has been reported.
- **Carrier frequency: not applicable** (dominant); no recessive carrier state is defined.

### 9.3 Population demographics

- **Affected populations: no data.** No ethnic or ancestral enrichment reported.
- **Geographic distribution: no data.** The single case arose in a US clinical laboratory cohort (Baylor Genetics).
- **Geographic distribution of specific variants: no data.**
- **Sex ratio: unknown** — the sex of the single reported patient is not given. *(By contrast, Coffin‑Siris syndrome is reported to be diagnosed in females more frequently than in males, for reasons that are unknown — a different disease, noted only for context.)*
- **Age distribution: unknown.**

---

## 10. Diagnostics

### 10.1 Clinical tests

- **Laboratory tests / biomarkers: none exist.** There is **no** blood, urine, enzyme or circulating biomarker test for this disease. PBRM1 is not an enzyme and produces no measurable metabolite. No FDA‑listed biomarker.
- **Imaging:** No disease‑specific imaging finding is described. Brain MRI (**NCIT:C16809**) would be ordered in the standard workup of any child with developmental delay to look for structural anomalies (e.g. corpus callosum abnormality, HP:0001273), but **no *PBRM1*‑specific neuroimaging signature has been reported**.
- **Functional tests, electrophysiology (EEG/EMG/ECG/NCS):** no disease‑specific findings. EEG would be indicated only if seizures occur.
- **Biopsy / histopathology / immunohistochemistry:** not applicable to the germline NDD. *In the oncologic setting*, **PBRM1 immunohistochemistry** is informative — loss of PBRM1 protein expression in renal tumours, together with LOH, was the key corroborating evidence in the germline‑RCC family (PMID 25911086).

### 10.2 Genetic testing — the only diagnostic modality

**Recommended approach:** *PBRM1* variants are, in practice, found **incidentally by broad sequencing**, not by targeted testing. There is no indication‑based *PBRM1* test.

- **Whole exome sequencing (NCIT:C101295)** — the modality by which the only known case was found (trio and proband exome sequencing at Baylor Genetics, with ACMG/AMP variant classification; PMID 34906496). **This is the highest‑yield approach.** Trio design is essential, since *de novo* status is the main evidential lever for an unestablished gene.
- **Whole genome sequencing (NCIT:C101294)** — adds detection of deep intronic and structural variants. Directly relevant: a deep intronic deletion in *ARID1A* was shown to produce a BAFopathy methylation profile (PMID 42173440), illustrating that exome‑negative BAFopathies exist.
- **Gene panels** — *PBRM1* appears on **exactly one** curated panel worldwide that I could retrieve: **Genomics England PanelApp panel 285 "Intellectual disability"** (relevant disorder name "Intellectual disability - microarray and sequencing"), version 11.97, at **Red/low confidence with `evidence: ["Expert Review Red"]` and no publications attached**. In Genomics England's diagnostic pipeline, Red genes are **not** reported. PanelApp Australia returned HTTP 403 and could not be checked.
- **Single‑gene testing** — **not indicated.** There is no recognisable clinical gestalt that would prompt isolated *PBRM1* analysis.
- **Chromosomal microarray / karyotype / FISH** — useful only for detecting large 3p contiguous‑gene events involving *PBRM1*. Chen et al. detected large CNVs with SNP arrays and homozygous deletions with an in‑house read‑depth pipeline, and found **no gene‑disrupting CNVs in the candidate genes**; a separate CMA cohort of approximately 70,000 patients yielded exonic deletions for *SMARCC1*, not *PBRM1*.
- **Mitochondrial DNA testing, repeat expansion testing:** **not applicable.**

**Critical interpretive guidance for a laboratory encountering a germline *PBRM1* variant:** given that ClinGen has published no gene–disease validity or dosage curation, PanelApp rates the gene Red, and ClinVar lists no *PBRM1* neurodevelopmental condition, **a germline *PBRM1* LoF variant cannot currently be reported as a confirmed molecular diagnosis**. The appropriate handling is a **candidate/research finding**, with GeneMatcher submission and, ideally, RNA studies — precisely the study that was missing in the index case.

### 10.3 Omics‑based diagnostics

- **RNA sequencing / transcriptomics:** **the highest‑value unmet diagnostic need here.** The index variant is a predicted splice‑altering change (SpliceAI 0.91/0.98) whose consequence was never confirmed because **no RNA was available**. RNA‑seq of patient fibroblasts or blood would directly test step 1–2 of the causal chain.
- **Epigenomics (DNA methylation episignature):** the **second** highest‑value test. A validated **BAFopathy episignature** exists and is deployed clinically (EpiSign; see §4.4 for supporting studies). **No PBRM1 episignature has been established**, and testing whether a *PBRM1* patient's methylome clusters with the BAFopathy group is a concrete, feasible validation experiment.
- **Proteomics, metabolomics, liquid biopsy:** **not applicable / no data** for the germline disease. (Liquid biopsy for somatic *PBRM1* is an oncology application, outside this entity.)

### 10.4 Clinical criteria and differential diagnosis

- **Standardized diagnostic criteria: none exist.** There is no clinical criterion set, no DSM/ICD code, and no society guideline for *PBRM1*‑related BAFopathy. Diagnosis is **molecular‑only, and currently provisional**.
- **Differential diagnosis.** A germline *PBRM1* finding in a child with developmental delay must be weighed against the established BAFopathies, which share the clinical space:
  - **Coffin‑Siris syndrome** (GeneReviews NBK131811) — genes **ARID1A, ARID1B, ARID2, DPF2, PHF6, SMARCA2, SMARCA4, SMARCB1, SMARCE1, SOX11**; *ARID1B* the most common cause; distinguishing features include aplasia/hypoplasia of the fifth distal phalanx or nail (**HP:0009835, HP:0008398**), coarse facies (**HP:0000280**), hypertrichosis (**HP:0000998**), hypotonia (**HP:0001252**), microcephaly (**HP:0000252**).
  - **Nicolaides‑Baraitser syndrome** (*SMARCA2*).
  - **ARID2‑related CSS6 (PMID 38243407)** — the most instructive comparator, being the other PBAF‑specific subunit: milder, with feeding difficulties, hypotonia, short stature, more frequent hip dysplasia, rarer severe brain/cardiac malformation, mild‑to‑moderate intellectual impairment, possible ADHD.
  - **SMARCC2‑associated NDD** (Bosch et al., *Genet Med* 2023, **PMID 37551667**) — notable genotype–phenotype split: loss‑of‑function variants were mostly inherited with mild or normal cognition, while non‑truncating variants were mostly *de novo* with severe delay (*flag: summary‑derived*).
  - **SMARCC1‑mutant BAFopathy with hydrocephalus** (Singh et al., *Brain* 2024, **PMID 38128548** — *summary‑derived*).
  - **BICRA‑related CSS12** (Wang 2026, *Genes* 17(1):81, **PMID 41595501**).
  - **Contiguous 3p deletion** — must be excluded by CMA, as 3p interstitial deletions are an established cause of neurodevelopmental delay and intellectual disability and would explain the phenotype by multi‑gene mechanism rather than by *PBRM1* alone.

### 10.5 Screening

- **Newborn screening: not applicable** and not recommended — no treatment, no validated test, no defined phenotype.
- **Carrier screening: not applicable** (dominant, *de novo*).
- **Cascade screening: not currently justified** for the NDD entity. *Caveat:* if a germline *PBRM1* truncating variant is found in a family with clustering renal cell carcinoma, the Benusiglio family's LOH/protein‑loss data (PMID 25911086) provide a rationale for considering cascade testing and renal surveillance — **but those authors themselves stated that international studies are needed before clinical use**, and penetrance is unquantified. This decision belongs with a clinical cancer geneticist, not a knowledge‑base rule.

---

## 11. Outcome / Prognosis

**This section is almost entirely "no data." I am not going to populate it from other BAFopathies.**

### 11.1 Survival and mortality

- **Survival rate (5‑/10‑year/overall): no data.**
- **Life expectancy: no data.** Even for Coffin‑Siris syndrome, GeneReviews states that in the absence of long‑term studies, information on life span is not available.
- **Mortality rate / disease‑specific mortality: no data.** No deaths attributable to germline *PBRM1* variation have been reported.
- *Model‑organism datum, not transferable to heterozygous humans:* homozygous *Pbrm1* null mice die in mid‑gestation, most between **E12.5 and E15.5** (PMID 15601824; MGI summary states homozygous null mice display embryonic lethality with hypoplastic cardiac ventricular chambers and placental malformation). **Heterozygous mice are viable** — no heterozygous lethality is reported.

### 11.2 Morbidity and function

- **Morbidity, disability outcomes, ICF‑coded functional impairment: no data.**
- **Quality‑of‑life measures: none applied.** No EQ‑5D, SF‑36, PROMIS or disease‑specific instrument.

### 11.3 Disease course

- **Complications: no data.** The complications that would plausibly dominate (feeding difficulty, seizures, orthopaedic and ophthalmologic issues) are extrapolated from CSS and are **not documented for *PBRM1***.
- **Recovery potential: no data.** Developmental disorders of chromatin regulation are generally not "recovered from," though targeted intervention in a critical window is at least mechanistically conceivable given the mouse rescue data.

### 11.4 Prediction

- **Prognostic factors: none identified.**
- **Prognostic biomarkers: none for the germline disease.** *In oncology, by contrast, PBRM1 status is a well‑studied prognostic/predictive marker*: PBRM1 LoF mutation was associated with clinical benefit from immune checkpoint blockade in ccRCC — *"clinical benefit was associated with loss-of-function mutations in the PBRM1 gene (P = 0.012)"*, confirmed *"in an independent validation cohort of 63 ccRCC patients"* (P = 0.0071) (Miao D et al., *Science* 2018;359(6377):801–806, **PMID 29301960**, DOI 10.1126/science.aan5951, PMC6035749). Three journal commentaries accompany that paper (PMIDs 29355171, 29358781, 29449480); **I was unable to retrieve subsequent replication or refutation studies** (the Europe PMC follow‑up query returned HTTP 503), so the durability of that association should be checked before use. In cholangiocarcinoma, PBRM1 mutation was associated with improved survival (HR 0.50, P = 0.02; PMID 42259884). **None of this applies to the germline neurodevelopmental entity.**

---

## 12. Treatment

### 12.1 The current state

**There is no disease‑specific treatment, no approved therapy, no clinical trial, and no published management guideline for PBRM1‑related BAFopathy.** A ClinicalTrials.gov search specific to this entity would be expected to return nothing; none was retrieved. Management would, in practice, be **symptomatic and supportive**, following general BAFopathy/developmental‑disorder practice.

### 12.2 Pharmacotherapy

- **No pharmacological treatment exists.** The only medication class with a plausible indication is **anticonvulsants (NCIT:C264)**, and only if seizures occur — standard, non‑disease‑specific.
- **Pharmacogenomics: no data.** *PBRM1* is not on the FDA Table of Pharmacogenetic Associations and has no PharmGKB/CPIC guideline that I retrieved.

### 12.3 Advanced therapeutics

- **Gene therapy, gene editing, cell therapy, RNA‑based therapy: none; no programs.** *PBRM1* encodes a 1,689‑aa protein, exceeding single AAV cargo capacity, which is a structural obstacle to gene replacement.
- **Targeted therapy — one preclinical lead worth recording.** The microglial *Pbrm1* cKO study provides the only demonstrated pharmacological rescue of a *Pbrm1*‑driven neurobehavioural phenotype: *"pharmacological blockade of CCR1/5 ameliorates behavioral deficits in Pbrm1 cKO mice"*, and the authors *"suggest the CCL5–CCR1/5 axis as a potential therapeutic target for ASD"* (PMID 42893407). The clinically available CCR5 antagonist is **maraviroc (NCIT:C73144; CHEBI:63608)**. **Flag strongly:** the specific agent, dose and route used in that study could not be retrieved (PMC reCAPTCHA; Wiley HTTP 403), so I cannot state that maraviroc itself was the agent used. This is a **hypothesis‑generating mouse result in a conditional knockout, with no human germline *PBRM1* ASD cohort behind it, and no clinical trial.** It must not be presented as a treatment option.
- **Immunotherapy — oncology context only, flagged to prevent miscategorisation.** Checkpoint inhibitors (**pembrolizumab NCIT:C106432**, **nivolumab NCIT:C68814**) relate to **somatic** PBRM1 loss in ccRCC and other tumours (PMIDs 29301960, 29301958, 41199851), not to this germline entity. Likewise **tazemetostat (NCIT:C107506)**, reported in a single PBRM1‑mutant metastatic cholangiocarcinoma responder (Pedregal M et al., *NPJ Precis Oncol* 2025, **PMID 41136536** — *flag: summary‑derived, n = 1*), and the **spindle‑assembly‑checkpoint dependency** created by PBRM1 loss (PMID 40011561), are **cancer** vulnerabilities.

### 12.4 Surgical and interventional

**No disease‑specific surgery.** Procedures would be indication‑driven only (e.g. **gastrostomy NCIT:C52006** for refractory feeding difficulty, strabismus or cardiac repair if those features occur).

### 12.5 Supportive and rehabilitative care — the actual standard of care

By analogy to the Coffin‑Siris GeneReviews management section (which is the applicable standard for an undiagnosed/provisional BAFopathy): **occupational, physical, and/or speech therapies to optimize developmental outcomes**; **feeding therapy, nutritional supplementation and/or gastrostomy tube placement as needed to meet nutritional needs**; and standard treatment for strabismus, refractive error, hearing loss, congenital heart defects, obstructive sleep apnea, constipation, gastroesophageal reflux, cryptorchidism, scoliosis, and seizure disorders.

**NCIT terms:** Physical Therapy **NCIT:C15302**; Occupational Therapy **NCIT:C121351**; Supportive Care **NCIT:C15747**; Gastrostomy **NCIT:C52006**; Anticonvulsant Agent **NCIT:C264**; Genetic Counseling **NCIT:C15240**; Magnetic Resonance Imaging **NCIT:C16809**; Whole Exome Sequencing **NCIT:C101295**; Whole Genome Sequencing **NCIT:C101294**. *(Note: "Speech Therapy" has no exact NCIT label; the OLS4 query returned only non‑exact hits — "Speech Therapist" NCIT:C19177 and "Speech Language Therapy" NCIT:C159273 — so the intended term should be selected deliberately rather than assumed.)*

### 12.6 Treatment outcomes, algorithms, personalised medicine

- **Response rates, adverse events: no data** (no treatment).
- **Treatment algorithms, combination therapy: none exist.**
- **Personalised/genotype‑guided approaches: none for the germline entity.** The only genotype‑guided *PBRM1* medicine that exists is in oncology (PBRM1 LoF ↔ checkpoint‑inhibitor benefit; PMID 29301960).

---

## 13. Prevention

### 13.1 Prevention levels

- **Primary prevention: none available and none conceptually possible** for a *de novo* germline variant. There is no risk‑factor modification, no vaccination, no exposure to avoid.
- **Secondary prevention (early detection):** the only meaningful intervention is **early molecular diagnosis via trio exome/genome sequencing in a child with unexplained developmental delay**, enabling early enrolment in developmental therapies. Note that this is prevention of *disability accrual*, not of the disease.
- **Tertiary prevention:** standard complication‑directed surveillance and management as in §12.5. **There is no evidence base for *PBRM1*‑specific surveillance** — in particular, **no recommendation exists for tumour surveillance in a child with a germline *PBRM1* NDD variant.** The theoretical concern (given the gene's tumour‑suppressor role and the Benusiglio RCC family) is real but entirely unquantified; any surveillance decision requires specialist cancer‑genetics input and should not be encoded as a guideline.

### 13.2 Immunization

**Not applicable.** No infectious component; routine childhood immunisation per standard schedule.

### 13.3 Screening and early detection

- **Population screening programs: none, and none warranted.** *PBRM1* does not meet newborn‑screening criteria (no treatment, no validated test, no defined phenotype).
- **Genetic screening — carrier screening: not applicable** (dominant, *de novo*).
- **Prenatal testing / PGT:** technically feasible for a known familial variant. **However, for a Red‑rated, ClinGen‑uncurated gene with one reported patient and no phenotype description, prenatal testing or preimplantation genetic testing for a *PBRM1* variant would not be justifiable on current evidence**, and this should be stated plainly in counselling. Recurrence risk after a confirmed *de novo* event is low (the generic gonadal‑mosaicism figure, ~1%, is a counselling convention and is **not** *PBRM1*‑specific; I retrieved no *PBRM1* mosaicism data).
- **Risk stratification: no model exists.**

### 13.4 Behavioural interventions, public health, environmental interventions, prophylaxis

**All not applicable.** No lifestyle, sanitation, vector‑control, health‑education or environmental intervention bears on this Mendelian entity. **No prophylactic medication or procedure exists.**

### 13.5 Genetic counselling (NCIT:C15240)

This is the one prevention‑domain intervention that is genuinely indicated, and its content should be **calibrated to the weak evidence**:
1. Explain that *PBRM1* is a **candidate**, not established, disease gene — ClinGen has published no curation; PanelApp rates it Red; one patient is reported.
2. Explain that the index variant's splicing consequence was **never confirmed by RNA study**, and offer RNA analysis and/or methylation episignature testing where available.
3. Discuss *de novo* status and the attendant low recurrence risk, with the caveat that gonadal mosaicism cannot be excluded.
4. Separately discuss the **germline RCC literature** (PMID 25911086), explicitly noting that penetrance is unquantified and that the original authors called for international studies before clinical application.
5. Offer **GeneMatcher / matchmaking submission** — with n = 1, case accrual is the rate‑limiting step for this entire disease entity.

---

## 14. Other Species / Natural Disease

### 14.1 Taxonomy and orthologues

| Species | NCBI Taxon | Gene | Gene ID |
|---|---|---|---|
| *Homo sapiens* | NCBITaxon:9606 | PBRM1 | NCBI Gene **55193**; HGNC:30064 |
| *Mus musculus* | NCBITaxon:10090 | Pbrm1 | NCBI Gene **66923**; **MGI:1923998** |
| *Rattus norvegicus* | NCBITaxon:10116 | Pbrm1 | **RGD:1565549** |
| *Danio rerio* | NCBITaxon:7955 | pbrm1 | **ZFIN:ZDB-GENE-080926-4** (two zebrafish orthologues listed by MGI) |
| *Caenorhabditis elegans* | NCBITaxon:6239 | pbrm‑1 | FlyBase/WormBase ID not verified in this session |

**Mouse gene details (MGI 6.29, updated 2026‑11‑10):** Pbrm1, "polybromo 1," synonyms 2310032M22Rik, 2610016F04Rik, BAF180, Pb1; **Chr 14: 30,741,095–30,843,549 bp, + strand (GRCm39)**; genetic map 19.09 cM, cytoband 14B. MGI lists **1 human, 1 mouse, 1 rat and 2 zebrafish** vertebrate orthologues.

**Evolutionary conservation of the mechanism is strong and demonstrated at the functional level.** In *C. elegans*, PBAF has cell‑type‑specific roles in neuronal diversification: it represses gene expression in nerve‑cord motor neurons by opposing the UNC‑3 terminal selector and activates gene expression in caudal motor neurons, with PBAF loss causing locomotion defects and MAB‑9/TBX20 proposed as the recruiting factor (Osuma A, Destain H, Mann J, … Kratsios P. "Cell type-specific functions of the PBAF chromatin-remodeling complex in neuronal diversification." *Nat Commun* 2025;17:741, **PMID 41390837**, PMC12820340, DOI 10.1038/s41467-025-67434-9). Separately, **"knockdown of the SWI/SNF accessory subunit PBRM-1 resulted in severe developmental defects"** in *C. elegans* when combined with SMARCA4 bromodomain mutations (Enríquez P, Krajewski K, Strahl BD, Rothbart SB, Dowen RH, Rose RB. *J Biol Chem* 2021, **PMID 34473995**, PMC8506967, DOI 10.1016/j.jbc.2021.101145). A further *C. elegans* study of BAF/PBAF in anchor‑cell invasion exists (Smith JJ et al., *PLoS Genet* 2022, **PMID 34982771** — *flag: summary‑derived lead, not verified*).

### 14.2 Breed (VBO)

**Not applicable / no data.** No breed‑associated *PBRM1* condition is recorded. No VBO identifier.

### 14.3 Naturally occurring disease in other species

**None reported.** I found **no OMIA entry** and no naturally occurring *PBRM1*/Pbrm1 disease in companion animals, livestock or wildlife. All animal *Pbrm1* phenotypes in the literature are **experimentally induced**.

**Veterinary relevance: none established.**

### 14.4 Comparative pathology

MGI curates four **human disease** associations for mouse Pbrm1 — all neoplastic, none neurodevelopmental: extrahepatic bile duct adenocarcinoma (**DOID:3495**), lung non‑small‑cell carcinoma (**DOID:3908**), lung small‑cell carcinoma (**DOID:5409**), renal cell carcinoma (**DOID:4450**). This is an independent indicator that the gene's curated disease identity is oncologic, not developmental.

Cross‑species comparison of the mechanism:
- **Mouse** reproduces the cardiac/placental requirement (null; PMID 15601824), the renal tumour‑suppressor function (conditional; PMID 29229903), the oligodendroglial transition requirement (lineage‑conditional; PMID 37371026), the microglia‑driven neurobehavioural phenotype (microglial‑conditional; PMID 42893407), and senescence/HSC regulation (PMID 26992241).
- ***C. elegans*** reproduces the neuronal‑identity and developmental requirement (PMIDs 41390837, 34473995).
- **Zebrafish:** **no pbrm1 phenotype study was found.** ZFIN phenotype data could not be retrieved (a constructed ZFIN phenotype URL returned 404).
- **Drosophila:** the *polybromo*/*Bap180* orthologue exists, but **no verified FlyBase record or phenotype data was retrieved** in this session; a FlyBase lookup attempted with an unverified FBgn returned no gene record. **Do not record a Drosophila identifier from this report.**

### 14.5 Transmission

**Not applicable.** No zoonotic potential; no cross‑species transmission. This is a non‑communicable genetic disorder.

---

## 15. Model Organisms

### 15.1 Model types available

**Mammalian (mouse) — the principal system.** MGI records **40 alleles** of Pbrm1: **1 chemically induced (ENU), 5 endonuclease‑mediated, 29 gene‑trapped, 5 targeted**, with **92 strains or lines available through IMSR**. MGI aggregates **18 phenotypes from 3 alleles across 3 genetic backgrounds, from 33 phenotype references**. One allele identifier surfaced in this session: **MGI:3526660**. *(The MGI allele summary table did not render for automated retrieval, so the full allele‑ID list could not be captured; it should be pulled from the MGI allele export before ingestion.)*

**Invertebrate:** *C. elegans* **pbrm‑1** (RNAi knockdown and PBAF mutants; PMIDs 34473995, 41390837).

**Cellular / in vitro:** human cell lines used for PBRM1 chromatin and centromere work (PMIDs 40011561, 36808431, 33811077); B16F10 mouse melanoma for the CRISPR immune screen (PMID 29301958); HCCC‑9810 for a PBRM1 knockdown study (Zhang D et al., *Oncol Rep* 2026, **PMID 42885299**, DOI 10.3892/or.2026.9212). **No iPSC‑derived neuronal or organoid model of PBRM1‑related BAFopathy has been reported** — a conspicuous gap given that iPSC/organoid models are standard for other BAFopathies.

**Induced (non‑genetic) models:** none relevant.

### 15.2 Genetic models and their phenotypes

| Model | Design | Phenotype | Citation |
|---|---|---|---|
| **Pbrm1/Baf180 constitutive null** | germline KO | **Embryonic lethal**, most embryos dying **E12.5–E15.5**; "severe hypoplastic ventricle development and trophoblast placental defects"; hypoplasia of ventricular free walls and **ventricular septal defect** in >15 embryos; slower heart rate and reduced blood volume; strongest expression in labyrinthine trophoblast at mid‑gestation; aggregation analyses indicate the cardiac defect is **direct**, not secondary to the placental defect; candidate targets **CRABPII, RARβ2, S100A13** | Wang Z et al., *Genes Dev* 2004;18(24):3106–3116, **PMID 15601824**, PMC535920 |
| **Pbrm1 microglial conditional KO** | microglia‑specific cKO (**Cre driver not retrievable** — PMC and publisher full text blocked) | "altered microglial clusters, excessive neurogenesis, and ASD-like behaviors"; PBRM1 binds the *Ccl5* promoter and represses CCL5; elevated CCL5 drives NSPC proliferation and neuronal differentiation via CCR1/5–β‑catenin; **CCR1/5 blockade ameliorates behavioural deficits** | Duan YY et al., *Adv Sci* 2026;e78086, **PMID 42893407**, PMC13676817, DOI 10.1002/advs.78086 |
| **Pbrm1 oligodendrocyte‑lineage cKO** | stage‑specific deletion in the OL lineage (Cnp1‑Cre / Sox10::Cre per secondary report; **not Olig2‑Cre**) | Deletion in **late** OPCs: little effect. Deletion **shortly after specification**: fewer cells entering the pre‑myelinating state, fewer myelinating oligodendrocytes. Pbrm1 co‑localises with Pdgfra and is also present in astrocytes and neurons | Waldhauser V, Baroti T, Fröb F, Wegner M. *Cells* 2023;12(12):1556, **PMID 37371026** |
| **Vhl/Pbrm1 double conditional KO (kidney)** | **Pax8‑CreERT2** × conditional *Vhl* and *Pbrm1* | PBRM1 loss rescues VHL‑dependent replication stress; **"fully-penetrant, multifocal carcinomas"** closely resembling human ccRCC | Espana‑Agusti J et al., *Nat Commun* 2017;8:2026, **PMID 29229903**, PMC5725450 |
| **Baf180 loss (senescence/HSC)** | KO | Regulates cellular senescence and hematopoietic stem cell homeostasis **through p21** | Lee H et al., *Oncotarget* 2016, **PMID 26992241** — *flag: summary‑derived* |
| **Pbrm1 loss (biliary)** | mouse | "Pbrm1 Loss Induces a Permissive Chromatin State for Cholangiocytic Differentiation and Cholangiocarcinoma Formation" | Chiou LW et al., *Cell Mol Gastroenterol Hepatol* 2026;20(6), **PMID 41513002** |
| **Pbrm1 in vivo CRISPR screen (leukemia)** | in vivo CRISPR/Cas9 | Pbrm1 identified as a regulator of myeloid leukemia development | Li BE et al., *Blood Adv* 2023;7(18), **PMID 37428871** — *flag: summary‑derived* |
| **Pbrm1/Arid2/Brd7 KO (tumour immunity)** | genome‑scale CRISPR screen in B16F10 | Sensitises tumour cells to T‑cell killing; increased IFN‑γ sensitivity; enhanced effector‑T‑cell‑recruiting chemokine secretion; Pbrm1 inactivation renders resistant tumours responsive to immunotherapy; ARID2/PBRM1 mRNA negatively correlates with GZMB/PRF1 across TCGA cancer types | Pan D et al., *Science* 2018, **PMID 29301958** |

**IMPC (Data Release 25.0, MGI:1923998):** 20 of 24 physiological systems tested; systems reported as significantly impacted by the knockout are **nervous system; behaviour/neurological; mortality/aging; hematopoietic system**; 16 systems with no significant impact; 4 not tested. Gene metrics show "4 Significant phenotypes" and "2 Associated diseases." **Flag an internal inconsistency:** the IMPC phenotype table itself rendered "Significant Phenotypes (0)" with no rows, so parameter‑level detail, allele, zygosity and p‑values are **not available**, and the four significant systems should be treated as a pointer, not as curated phenotype calls. The Alliance of Genome Resources page returned a JavaScript shell, so **MP terms and Alliance disease associations could not be retrieved**.

**The IMPC nervous‑system and behaviour/neurological flags are, nonetheless, the most directly relevant independent corroboration that heterozygous or viable Pbrm1 perturbation affects the nervous system — and they warrant follow‑up at parameter level.**

### 15.3 Phenotype recapitulation and limitations

**What the models recapitulate well:**
- The **requirement for PBRM1 in neurodevelopment** — demonstrated at the cell‑type level (microglia, OPCs) and conserved to *C. elegans* motor neurons.
- A **behaviourally scoreable ASD‑like phenotype** with a defined, druggable mediating axis (CCL5→CCR1/5→β‑catenin) and pharmacological rescue.
- A **developmental critical‑period effect** (early vs late OPC deletion).
- **Cardiac malformation** including VSD, which maps onto HP:0001629 — a feature that should be actively looked for if more human cases accrue.

**What the models do not capture (limitations that matter for this disease entry):**
1. **Zygosity mismatch.** The informative mouse phenotypes come from **homozygous nulls or tissue‑specific conditional nulls** — i.e. complete loss in the relevant cells. The putative human disease is **heterozygous haploinsufficiency**. **No heterozygous Pbrm1 mouse neurodevelopmental phenotype has been reported**, and heterozygous mice are viable. This is the single largest gap between model and disease.
2. **Cell‑type attribution is unresolved in humans.** The mouse ASD‑like phenotype is driven by **microglial** PBRM1 loss, a non‑neuronal mechanism. Whether human germline haploinsufficiency acts through microglia, neural progenitors, oligodendroglia, or all three, is unknown.
3. **No model has the human variant.** No knock‑in of c.1542‑3C>G or any human‑equivalent allele exists.
4. **No cognitive/ID readout.** Mouse models score social behaviour and repetitive behaviour, not intellectual disability — the feature that would define the human disorder.
5. **No craniofacial/digital phenotype** analogous to the CSS gestalt has been assessed in any Pbrm1 model.
6. **The ASD premise is circular.** The mouse paper motivates itself on human *PBRM1* ASD missense variants, but SFARI Gene does not list *PBRM1*, and I could retrieve no primary human cohort supporting that premise. The model therefore validates a mechanism, not a human disease association.

### 15.4 Research applications

Available models support study of: PBAF‑dependent transcriptional programmes in neural and glial lineages; microglia–NSPC crosstalk and adult/embryonic hippocampal neurogenesis; developmental timing/critical windows in oligodendrogenesis; cardiac chamber maturation and retinoic‑acid target regulation; centromere/pericentromere integrity and spindle‑assembly‑checkpoint dependency; replication stress in the VHL/PBRM1 context; and tumour‑immune evasion via IFN‑γ sensitivity.

### 15.5 Resources

**MGI** (informatics.jax.org/marker/MGI:1923998) — 40 alleles, 92 IMSR strains/lines, 33 phenotype references; **IMSR** for strain acquisition; **IMPC** (mousephenotype.org/data/genes/MGI:1923998, DR25.0); **RGD:1565549** (rat); **ZFIN:ZDB-GENE-080926-4** (zebrafish; no phenotype data retrieved); **Alliance of Genome Resources** (page not machine‑readable in this session); **WormBase** for *pbrm‑1*. KOMP/EuMMCR/MMRRC/EMMA were not queried individually, but the 29 gene‑trap and 5 targeted alleles in MGI indicate substantial repository coverage.

---

## Summary Assessment for Knowledge‑Base Curation

| Dimension | Status |
|---|---|
| **Ontology entity** | Exists and is well‑formed: MONDO:0700122, MedGen CN306939, parent MONDO:0700120 BAFopathy, gene HGNC:30064 via RO:0004003 |
| **Gene identity** | Unambiguous and richly annotated: *PBRM1*/BAF180, 3p21.1, PBAF‑defining subunit, Q86U86, 1,689 aa, 6 bromodomains + 2 BAH + HMG box |
| **Human disease evidence** | **Minimal: one *de novo* splice‑region variant in one patient, phenotype unreported, RNA unconfirmed (PMID 34906496)** |
| **Independent curation** | **ClinGen: no curation published. PanelApp: Red. SFARI: not listed. ClinVar: no NDD condition. OMIM: no phenotype. Orphanet: no disorder. HPO annotations: zero.** |
| **Counter‑evidence** | Valencia/Kadoch 2023 (PMID 37500730): PBRM1, with ARID2 and BICRAL, is "more frequently mutated in cancer than in NDD"; NDD burden concentrates in cBAF |
| **Constraint** | Strongly supportive of haploinsufficiency intolerance: pLI 1.00, LOEUF 0.23, %HI 9.54 |
| **Mechanistic plausibility** | **High** — PBAF targeting subunit; mouse microglial cKO produces ASD‑like behaviour via a defined, reversible CCL5–CCR1/5–β‑catenin axis; conserved neuronal roles to *C. elegans* |
| **Alternative germline phenotype** | Autosomal dominant **renal cell carcinoma predisposition**, one family with segregation + LOH + protein loss (PMID 25911086), penetrance unquantified |
| **Overall** | A **provisional, pattern‑generated disease entity with strong gene‑level biology and weak disease‑level evidence.** The decisive next steps are (1) RNA studies on the index variant, (2) methylation episignature testing against the BAFopathy signature, (3) international case matchmaking, and (4) a heterozygous Pbrm1 mouse with cognitive/behavioural phenotyping. |

---

## Sources

**Primary literature**
- [Chen CA et al., Retrospective analysis of a clinical exome sequencing cohort… BAFopathies, *Genet Med* 2022;24(2):364–373, PMID 34906496](https://pmc.ncbi.nlm.nih.gov/articles/PMC8957292)
- [Valencia AM, … Kadoch C. Landscape of mSWI/SNF perturbations in NDDs, *Nat Genet* 2023;55(8):1400–1412, PMID 37500730](https://pmc.ncbi.nlm.nih.gov/articles/PMC10412456)
- [Duan YY et al., PBRM1 Deficiency in Microglia…, *Adv Sci* 2026;e78086, PMID 42893407](https://pmc.ncbi.nlm.nih.gov/articles/PMC13676817)
- [Varela I et al., *Nature* 2011;469:539–542, PMID 21248752](https://pubmed.ncbi.nlm.nih.gov/21248752/)
- [Benusiglio PR et al., *J Med Genet* 2015;52(6):426–430, PMID 25911086](https://jmg.bmj.com/content/52/6/426.full)
- [Miao D et al., *Science* 2018;359:801–806, PMID 29301960](https://pmc.ncbi.nlm.nih.gov/articles/pmid/29706634)
- [Pan D et al., *Science* 2018, PMID 29301958](https://www.pubmed.gov/29301958/)
- [Wang Z et al., *Genes Dev* 2004;18(24):3106–3116, PMID 15601824](https://genesdev.cshlp.org/content/18/24/3106.full)
- [Espana-Agusti J et al., *Nat Commun* 2017;8:2026, PMID 29229903](https://pmc.ncbi.nlm.nih.gov/articles/PMC5725450)
- [Waldhauser V et al., *Cells* 2023;12(12):1556, PMID 37371026](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10296403/)
- [Lane KA et al., *Nat Commun* 2025;16:1980, PMID 40011561](https://www.nature.com/articles/s41467-025-57277-9)
- [De Silva SM et al., *Nucleic Acids Res* 2023;51(8):3631–3649, PMID 36808431](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10164552/)
- [Karki M et al., *Sci Adv* 2021;7(14):eabf2866, PMID 33811077](https://blogs.bcm.edu/2021/10/14/from-the-labs-pbrm1s-new-function-supports-a-novel-cancer-promoting-mechanism/)
- [Osuma A et al., *Nat Commun* 2025;17:741, PMID 41390837](https://www.nature.com/articles/s41467-025-67434-9_reference.pdf)
- [Schrier Vergano S et al., ARID2 CSS, *Am J Med Genet A* 2024;194(6):e63540, PMID 38243407](https://onlinelibrary.wiley.com/doi/full/10.1002/ajmg.a.63540)
- [Vassos E et al., 3p21.1 and bipolar disorder, *Biol Psychiatry* 2012;72(8):645–650, PMID 22560537](https://pubmed.ncbi.nlm.nih.gov/22560537/)
- [Sokpor G et al., ATP-Dependent Chromatin Remodeling During Cortical Neurogenesis, *Front Neurosci* 2018;12:226, PMID 29686607](https://pmc.ncbi.nlm.nih.gov/articles/PMC5900035)
- [Context-dependent role for PBRM1/BAF180 in ccRCC, *Oncogenesis* 2016](https://www.nature.com/articles/oncsis201689)
- [PBAF contributes to metal homeostasis through MTF1](https://pmc.ncbi.nlm.nih.gov/articles/PMC13294679/)
- [BAF180 regulates senescence and HSC homeostasis through p21](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4991371/)

**Databases and curated resources**
- [EBI OLS4 — MONDO:0700122](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0700122) · [Monarch API v3](https://api.monarchinitiative.org/v3/api/entity/MONDO:0700122) · [Monarch dismech curation issue](https://github.com/monarch-initiative/dismech/issues/16131)
- [HGNC REST — PBRM1](https://rest.genenames.org/fetch/symbol/PBRM1) · [UniProt Q86U86](https://rest.uniprot.org/uniprotkb/Q86U86.json) · [QuickGO annotations](https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB:Q86U86&limit=100) · [Reactome](https://reactome.org/ContentService/search/query?query=PBRM1&species=Homo%20sapiens)
- [ClinGen — PBRM1 (HGNC:30064)](https://search.clinicalgenome.org/kb/genes/HGNC:30064) · [Genomics England PanelApp — PBRM1](https://panelapp.genomicsengland.co.uk/panels/285/gene/PBRM1/) · [SFARI Gene — PBRM1](https://gene.sfari.org/database/human-gene/PBRM1)
- [MGI — Pbrm1 (MGI:1923998)](https://www.informatics.jax.org/marker/MGI:1923998) · [IMPC — Pbrm1](https://www.mousephenotype.org/data/genes/MGI:1923998) · [MGI allele MGI:3526660](https://www.informatics.jax.org/allele/MGI:3526660)
- [GeneReviews — Coffin-Siris Syndrome](https://www.ncbi.nlm.nih.gov/sites/books/NBK131811/) · [MedlinePlus Genetics — Coffin-Siris syndrome](https://medlineplus.gov/genetics/condition/coffin-siris-syndrome)
- [Human Protein Atlas — PBRM1](https://www.proteinatlas.org/ENSG00000163939-PBRM1/brain) · [GeneBe — PBRM1 constraint](https://genebe.net/gene/hg38/PBRM1) · [gnomAD v4.0 constraint release notes](https://gnomad.broadinstitute.org/news/2024-03-gnomad-v4-0-gene-constraint)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 143 |
| Resolved | 143 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| Quoted claims with nothing to check against | 2 |
| References weighed for topical relevance | 143 |
| On topic | 49 |
| Off topic | 2 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:42748234` (1 mention) - Structural principles underlying the evolution of SWI/SNF chromatin remodelers.
  - shared terms: complex
- `DOI:10.1126/sciadv.aei0972` (1 mention) - Structural principles underlying the evolution of SWI/SNF chromatin remodelers
  - shared terms: complex

Weighed against this report's own most characteristic terms: `pbrm1`, `gene`, `disease`, `variant`, `cell`, `verbatim`, `germline`, `phenotype`, `read`, `returned`, `complex`, `abstract`, `loss`, `pbaf`, `list`, `human`, `mouse`, `disorder`, `clinical`, `patient`.

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.1016/j.gim.2021.09.017`: "a group of neurodevelopmental disorders with extensive locus and phenotypic heterogeneity"
  - Reference resolved but exposes no abstract or full text to search
- `DOI:10.1016/j.ejmg.2026.105084`: "Pathogenic variants in BAF complex genes are linked to neurodevelopmental disorders, termed BAFopathies"
  - Reference resolved but exposes no abstract or full text to search

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 139 |
| Resolved | 128 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 10 |
| Terms whose name was checked | 99 |
| Terms named correctly | 80 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 12 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0700122` (29 mentions) - the report calls it "Title: "Curate PBRM1-related BAFopathy", "Mondo"; MONDO calls it **PBRM1-related BAFopathy**
- `GO:2000781` (3 mentions) - the report calls it "NAS, PMID 25066234"; GO calls it **positive regulation of double-strand break repair**
- `HP:0001629` (3 mentions) - the report calls it "Ventricular septal defect", "a feature that should be actively looked for if more human cases accrue"; HP calls it **Ventricular septal defect**
- `UBERON:0001885` (2 mentions) - the report calls it "dentate gyrus of hippocampal formation", "site of the excessive neurogenesis phenotype"; UBERON calls it **dentate gyrus of hippocampal formation**
- `UBERON:0003053` (2 mentions) - the report calls it "ventricular zone", "PBRM1‑rich germinal zone at E14.5"; UBERON calls it **ventricular zone**
- `UBERON:0002336` (2 mentions) - the report calls it "corpus callosum", "white matter, given the oligodendrocyte phenotype"; UBERON calls it **corpus callosum**
- `NCIT:C159273` (2 mentions) - the report calls it "so the intended term should be selected deliberately rather than assumed"; NCIT calls it **Speech Language Therapy**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `RO:0004003` (5 mentions), reported as "germline" - RO does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001252` (4 mentions) - the report calls it "Hypotonia (exact synonym "Muscular hypotonia")", "Hypotonia"; HP calls it **Hypotonia**, and lists "Muscular hypotonia" among its other names
- `HP:0001273` (3 mentions) - the report calls it "Abnormal corpus callosum morphology (exact synonym)"; HP calls it **Abnormal corpus callosum morphology**
- `HP:0000708` (2 mentions) - the report calls it "Atypical behavior (exact synonym)"; HP calls it **Atypical behavior**
- `HP:0012443` (2 mentions) - the report calls it "Abnormal brain morphology (exact synonym)"; HP calls it **Abnormal brain morphology**
- `HP:0003829` (2 mentions) - the report calls it "Typified by incomplete penetrance (exact synonym)"; HP calls it **Typified by incomplete penetrance**
- `GO:0000122` (3 mentions) - the report calls it "negative regulation of transcription by RNA polymerase II", "negative regulation of transcription by RNA Pol II"; GO calls it **negative regulation of transcription by RNA polymerase II**
- `GO:0060070` (3 mentions) - the report calls it "canonical Wnt signaling pathway", "Canonical Wnt/β‑catenin"; GO calls it **canonical Wnt signaling pathway**, and lists "canonical Wnt-activated signaling pathway" among its other names
- `GO:0006974` (2 mentions) - the report calls it "DNA damage response (exact synonym)", "DNA damage response"; GO calls it **DNA damage response**
- `GO:0070098` (3 mentions) - the report calls it "chemokine-mediated signaling pathway", "Chemokine signalling"; GO calls it **chemokine-mediated signaling pathway**, and lists "chemokine-mediated signalling pathway" among its other names
- `GO:0005721` (3 mentions) - the report calls it "pericentric heterochromatin", "pericentromeric chromatin"; GO calls it **pericentric heterochromatin**
- `CL:0000129` (3 mentions) - the report calls it "microglial cell", "microglia"; CL calls it **microglial cell**, and lists "microglia" among its other names
- `CL:0000047` (3 mentions) - the report calls it "neural stem cell", "neural stem cell (exact synonym)", "neural stem cell** (syn. neuronal stem cell)"; CL calls it **neural stem cell**, and lists "neuronal stem cell" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0700122` - called "Title: "Curate PBRM1-related BAFopathy", "Mondo"
- `RGD:1565549` - called "rat", "Pbrm1"
- `HP:0001252` - called "Hypotonia (exact synonym "Muscular hypotonia")", "Hypotonia"
- `HP:0001629` - called "Ventricular septal defect", "a feature that should be actively looked for if more human cases accrue"
- `GO:0000122` - called "negative regulation of transcription by RNA polymerase II", "negative regulation of transcription by RNA Pol II"
- `GO:0060070` - called "canonical Wnt signaling pathway", "Canonical Wnt/β‑catenin"
- `GO:0006974` - called "DNA damage response (exact synonym)", "DNA damage response"
- `GO:0070098` - called "chemokine-mediated signaling pathway", "Chemokine signalling"
- `GO:0005721` - called "pericentric heterochromatin", "pericentromeric chromatin"
- `CL:0000129` - called "microglial cell", "microglia"
- `CL:0000047` - called "neural stem cell", "neural stem cell (exact synonym)", "neural stem cell** (syn. neuronal stem cell)"
- `UBERON:0001885` - called "dentate gyrus of hippocampal formation", "site of the excessive neurogenesis phenotype"
- `UBERON:0003053` - called "ventricular zone", "PBRM1‑rich germinal zone at E14.5"
- `UBERON:0002336` - called "corpus callosum", "white matter, given the oligodendrocyte phenotype"
- `NCIT:C101295` - called "Whole Exome Sequencing", "Whole exome sequencing"
- `NCIT:C101294` - called "Whole Genome Sequencing", "Whole genome sequencing"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`, `RGD`, `Chr3`, `Chr14`, `EXT_ID`, `BRD7`.