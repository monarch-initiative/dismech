---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-11-11T20:08:42.065012'
end_time: '2026-11-11T20:25:05.606682'
duration_seconds: 983.54
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Ectomesenchymoma
  mondo_id: MONDO:0002855
  category: ''
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: malignant ectomesenchymoma; rhabdomyosarcoma with ganglionic differentiation
    (morphologic abnormality); sarcoma with ganglionic or neuroectodermal differentiation
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
  web_search_requests: 16
  num_turns: 77
  total_cost_usd: 7.560400750000004
  session_id: b84a448a-c58e-4924-b4dc-628f2307eec4
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 7
citation_count: 18
reference_validation:
  total_references: 67
  verified: 66
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.015
  relevance_assessed: 66
  on_topic: 32
  off_topic: 2
  off_topic_references:
  - PMID:41317384
  - PMID:40979140
  unresolved_references:
  - DOI:10.3760/cma.j.cn112151-20260315-00174
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 49
  verified: 44
  not_found: 1
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.022
  labels_checked: 32
  labels_matching: 11
  labels_mismatched: 19
  mislabelled_terms:
  - term_id: MONDO:0002855
    reported_labels:
    - MONDO
    - disease_term
    ontology_label: ectomesenchymoma
  - term_id: NCIT:C4716
    reported_labels:
    - NCIT
    - cross-ref
    ontology_label: Ectomesenchymoma
  - term_id: NCIT:C188984
    reported_labels:
    - NCIT (paediatric)
    ontology_label: Childhood Ectomesenchymoma
  - term_id: NCIT:C173815
    reported_labels:
    - NCIT (recurrent)
    ontology_label: Recurrent Ectomesenchymoma
  - term_id: DOID:4055
    reported_labels:
    - DOID
    ontology_label: ectomesenchymoma
  - term_id: HP:0031500
    reported_labels:
    - phenotype
    ontology_label: Abdominal mass
  - term_id: HP:0002859
    reported_labels:
    - phenotype
    ontology_label: Rhabdomyosarcoma
  - term_id: HP:0006743
    reported_labels:
    - phenotype
    ontology_label: Embryonal rhabdomyosarcoma
  - term_id: HP:0006779
    reported_labels:
    - phenotype
    ontology_label: Alveolar rhabdomyosarcoma
  - term_id: HP:0500092
    reported_labels:
    - phenotype
    ontology_label: Orbital rhabdomyosarcoma
  - term_id: HP:0004376
    reported_labels:
    - phenotype
    ontology_label: Neuroblastic tumor
  - term_id: GO:0007265
    reported_labels:
    - biological process
    ontology_label: Ras protein signal transduction
  - term_id: GO:0046579
    reported_labels:
    - biological process
    ontology_label: positive regulation of Ras protein signal transduction
  - term_id: GO:0035914
    reported_labels:
    - biological process
    ontology_label: skeletal muscle cell differentiation
  - term_id: CL:0000056
    reported_labels:
    - cell type
    ontology_label: myoblast
  - term_id: GO:0001755
    reported_labels:
    - biological process
    ontology_label: neural crest cell migration
  - term_id: CL:0000333
    reported_labels:
    - cell type
    ontology_label: migratory neural crest cell
  - term_id: CL:0002573
    reported_labels:
    - cell type
    ontology_label: Schwann cell
  - term_id: CL:0011103
    reported_labels:
    - cell type
    ontology_label: sympathetic neuron
  labels_variant: 2
  unresolved_terms:
  - RO:0004003
  unresolvable_prefixes:
  - ICDO
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ectomesenchymoma
- **MONDO ID:** MONDO:0002855 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** malignant ectomesenchymoma; rhabdomyosarcoma with ganglionic differentiation (morphologic abnormality); sarcoma with ganglionic or neuroectodermal differentiation
- **Category:** 

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Ectomesenchymoma** covering all of the
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

I'll research this now. Let me load the web tools and check the local reference cache in parallel.

I have the key molecular paper in full text. Now let me research the clinical, epidemiological, and model literature.

PubMed blocks direct fetch. Let me use the Europe PMC API instead.

Strong literature map. Let me pull the key recent molecular and classification papers.

Now let me verify ontology identifiers rather than writing them from memory.

Bash approval isn't available non-interactively; I'll verify terms through the OLS API instead.

I have a solid evidence base. Writing the report now.

---

# Ectomesenchymoma (MONDO:0002855) — Comprehensive Disease Research Report

**Prepared:** 11 November 2026 · **Target entry:** `kb/disorders/Ectomesenchymoma.yaml`

> **Causal gene (first-paragraph requirement).** Ectomesenchymoma has **no germline causal gene**; the MONDO record carries no `RO:0004003` gene, and the template's "causal gene(s): not recorded" is correct in the Mendelian sense. The disease is defined instead by a **recurrent somatic driver: `HRAS` (HGNC:5173)**, mutated at codons 13 and 61 in the large majority of cases, with `NRAS` (HGNC:7989) as the main alternative. In a minority of patients the *HRAS* variant is **postzygotic/mosaic**, present in clinically normal tissue, making those cases tumours arising on a **mosaic RASopathy** background. This is the gene to anchor the entry on.

> **⚠️ Snippet-verification caveat for the curator.** Only two references were read from the committed cache (`PMID:26872011`, full text; `PMID:42851199`, abstract) — quotes from those are byte-reliable. Every other quotation below was retrieved through Europe PMC / publisher web pages via a summarising fetch layer and **must be re-fetched with `just fetch-reference <ID>` and re-checked with `just count-verified-snippets` before being used as an evidence `snippet:`.** Treat them as leads, not as verified quotes.

---

## 1. Disease Information

### 1.1 Overview

Ectomesenchymoma (EMS), more often written **malignant ectomesenchymoma (MEM)**, is an exceedingly rare **biphasic (biphenotypic) malignant soft-tissue tumour** in which a **mesenchymal component — almost always rhabdomyosarcoma, usually embryonal (ERMS)** — is intimately admixed with a **neuroectodermal component drawn from the neuroblastic/neural-crest spectrum**: scattered ganglion cells, mature ganglioneuroma, ganglioneuroblastoma, or primitive neuroblastoma, and in a minority Schwannian differentiation.

From the committed full text of Huang et al. 2016 (PMID:26872011), exact:

> "Malignant ectomesenchymoma (MEM) is an exceedingly rare pediatric sarcoma with a predilection for infants and young children and is composed of dual malignant mesenchymal and neuroectodermal components. Microscopically, MEM displays areas of rhabdomyosarcoma (RMS) with intermixed neuronal/neuroblastic foci."

> "The MEM nomenclature derives from its possible tumorigenesis from the pluripotential neural crest remnants, the so-called ectomesenchyme."

The central biological conclusion of the modern literature — and the one that should frame the whole dismech entry — is that **EMS is genetically, transcriptomically and epigenetically a form of embryonal rhabdomyosarcoma with divergent neuroectodermal differentiation, not a nerve-sheath tumour** (PMID:26872011; PMID:42504917).

### 1.2 Key identifiers (all verified by lookup, not from memory)

| Resource | Identifier | Label |
|---|---|---|
| **MONDO** | `MONDO:0002855` | ectomesenchymoma |
| MONDO parents | `MONDO:0005089` (sarcoma); `MONDO:0005872` (nervous system cancer) | *verified via OLS `/parents`* |
| **NCIT** | `NCIT:C4716` | Ectomesenchymoma |
| NCIT (paediatric) | `NCIT:C188984` | Childhood Ectomesenchymoma |
| NCIT (recurrent) | `NCIT:C173815` | Recurrent Ectomesenchymoma |
| **ICD-O-3** | **8921/3** | (morphology code, from MONDO xref `ICDO:8921/3`) |
| DOID | `DOID:4055` | — |
| UMLS | `C0431111` | — |
| MedGen | `98123` | — |
| GARD | `0012279` | — |
| ICD-10 | **not established** — no dedicated code; coded as soft-tissue sarcoma by site (e.g. C49.*) | ⚠️ *verify before binding* |
| ICD-11 | **not established** for this entity | ⚠️ |
| **Orphanet** | **No dedicated ORPHA code found.** Searches returned only the generic `ORPHA:71209` *rare soft tissue tumor* branch. | ⚠️ Record as absent |
| MeSH | **No dedicated descriptor.** PubMed indexes these papers under **Mesenchymoma** (and, for the newer series, *Rhabdomyosarcoma, Embryonal*) — see the MeSH keyword block of `PMID:26872011` in the cache: `"Mesenchymoma/genetics, pathology"` | — |

NCIT definition (verbatim from OLS, `NCIT:C4716`):

> "An exceedingly rare, aggressive malignant mesenchymal neoplasm characterized by the presence of a sarcomatous component and a ganglionic or a neuroectodermal component."

MONDO definition (verbatim from OLS, `MONDO:0002855`):

> "An aggressive malignant mesenchymal neoplasm of the nervous system or soft tissues. It is characterized by the presence of a sarcomatous component (most often rhabdomyosarcoma) and a ganglionic or a neuroectodermal component."

### 1.3 Synonyms and alternative names

- **malignant ectomesenchymoma (MEM)** — the dominant usage in the clinical literature
- **gangliorhabdomyosarcoma** — the original 1971 designation
- **sarcoma with ganglionic or neuroectodermal differentiation** (MONDO/NCIT synonym)
- **rhabdomyosarcoma with ganglionic differentiation** (morphologic abnormality) (MONDO synonym)
- **embryonal rhabdomyosarcoma with heterologous neuroectodermal differentiation (ERMS-HND)** — the designation used by the largest published series (17 cases, PMID:42851199, 2026). This is a *naming shift that reflects the reclassification* and the curator should record it as a synonym.
- "malignant ectodermal mesenchymoma" — a variant rendering used in the 2025 adult review (PMID:41465905); likely a translation artefact rather than a distinct concept.

### 1.4 Nomenclature history

- **1971** — Holimon & Rosenblum described a tumour of the cerebellopontine angle in a 15-month-old boy with combined rhabdomyosarcoma and ganglioneuroma, calling it **"gangliorhabdomyosarcoma"** (PMID:5313338). Quoted in PMID:26872011: *"The first description of a tumor with dual RMS and ganglioneuroma components was in the cerebellopontine angle of a 15 month-old boy under the designation of 'gangliorhabdomyosarcoma'."*
- **1975** — Naka et al. proposed the term **malignant ectomesenchymoma** for a retroperitoneal tumour in a 2-year-old girl showing ganglioneuroblastoma plus RMS, liposarcoma and chondroid tissue (cited as ref 1 of PMID:26872011).
- **1977** — Karcioglu et al. used "ectomesenchymoma" for a facial tumour in a 6-month-old (PMID:872048).
- **2013 (WHO 4th ed.)** — classified under **peripheral nerve sheath tumours**. From PMID:26872011: *"the latest edition of World Health Organization classification of soft tissue and bone tumors categorized MEM under nerve sheath tumors."*
- **2020 (WHO 5th ed.)** — **reclassified into the skeletal muscle tumour chapter.** Milano et al. 2023 state EMS is *"currently included in the category of skeletal muscle malignancies"* (PMID:36440693); the 2024 review concurs that WHO 2020 categorised MEM under "Skeletal Muscle Tumor" rather than nerve sheath tumours (PMID:38496756).
- **2026 (WHO 6th ed., STB6)** — published (PMID:42839882, Hornick et al., *Am J Surg Pathol*). ⚠️ **The placement of ectomesenchymoma in STB6 could not be confirmed from the overview paper's abstract.** The curator should check the printed volume before asserting the current chapter.

### 1.5 Data provenance

**Aggregated, disease-level, literature-derived only.** There is **no EHR, registry-incidence or claims-based dataset** for this entity. The evidence base is:
- ~100–150 published cases, overwhelmingly single case reports;
- four cooperative-group / institutional series: IRS-III/IV (15 cases, 2000), CWS (6 cases, PMID:22535600), EpSSG (10 cases, PMID:36440693), Beijing Children's Hospital (11 cases, PMID:40221922);
- three pathology/molecular series: MSKCC+Padova (7 cases, PMID:26872011), Northwestern (6 cases, PMID:28994342), Foshan (17 cases, PMID:42851199);
- one methylation study (2 cases, PMID:42504917) and one mosaicism study (5 cases, PMID:40629179).

---

## 2. Etiology

### 2.1 Primary causal factor — somatic RAS-pathway activation

**EMS is a sporadic somatic neoplasm.** The dominant and recurrent driver is an activating point mutation in **`HRAS`**.

**Huang et al. 2016 (PMID:26872011)** — the landmark study, full text in cache. Exact quotes:

> "By Sanger sequencing, 6 of 7 (86%) MEMs had HRAS mutations, with no additional case harboring PTPRD or FBXW7 mutations."

> "In total, 6 of 7 (86%) MEMs harbored HRAS mutations, 4 with p.G13R mutation and 2 with p.Q61L. Three of the p.G13R mutations demonstrated nearly homozygous pattern; but no normal DNA was available to confirm their germline genotype."

> "The only case lacking HRAS mutation showed neuroblastic micronodules without ganglion cells."

> "In addition, HRAS mutations were detected in both naive and treated MEMs, suggesting an intrinsic event rather than a chemotherapy-induced process."

**Subsequent confirmation and extension of the RAS spectrum:**

| Study | n | RAS findings |
|---|---|---|
| Huang 2016, PMID:26872011 | 7 | HRAS 6/7 (86%): p.G13R ×4, p.Q61L ×2 |
| Salomatina 2025, PMID:40629179 | 5 | *"In 4 out of 5 cases, mutations in HRAS typical for ME were detected."* |
| Pellegrino 2024, PMID:38496756 | 1 | `HRAS NM_176795:exon2:c.G37C:p.G13R`, VAF 72% |
| Caporalini 2026, PMID:42504917 | 2 | *"Both tumors harbored RAS-pathway mutations (HRAS p.Gly13Arg; NRAS p.Gln61His)."* |
| Zeng 2026, PMID:42851199 (cached, exact) | 17 | *"RAS mutations were detected in 3 cases (HRAS mutation in 1 case and NRAS mutations in 2 cases)."* |

⚠️ **Note the discrepancy to record honestly in the entry:** the 17-case Chinese series found RAS mutations in only **3/17 (18%)**, far below the 86% of the MSKCC series. Possible explanations — different case definition (ERMS-HND is a broader net), platform sensitivity, or genuine population/biological heterogeneity. Do **not** write "HRAS mutations occur in ~86% of ectomesenchymoma" as an unqualified disease-level claim; state the per-series figures.

**How the mutation acts (mechanistic quote, PMID:26872011, exact):**

> "The Ras family, including HRAS, KRAS and NRAS, belongs to the small G protein superfamily and involves the Ras/MAPK (mitogen-activated protein kinase) pathway, which transduces the extracellular input to the intracellular compartment through the GDP/GTP-regulated switches. The cancer-related somatic mutations in Ras members often occur at amino acids 12, 13, or 61, which are the conserved sites for modulating GDP/GTP binding and hydrolysis."

### 2.2 Postzygotic mosaicism — a genuine predisposition mechanism

The single most important recent etiological finding. **Salomatina et al. 2025 (PMID:40629179, *J Hum Genet* 70(10):497–501, doi:10.1038/s10038-025-01363-9)** reported EMS arising in two children with **mosaic RASopathy** phenotypes:

> "Two patients with HRAS mutation and phenotypic features of neurocutaneous epidermal nevus syndrome and nevus sebaceous syndrome had the pathogenic HRAS variant in a spectrum of biological materials including healthy tissues with different varying allele frequency (VAF). The molecular genetic findings indicate a post-zygotic origin of the pathogenic mutation in HRAS, associated with the mosaic phenotype, in both cases."

> "...that exposed the driver event as postzygotic, occurring not later than the stage of migrating ectomesenchyme originating from the neural crest. These are the first descriptions of ME against a somatic mosaicism background."

**Strong corroborating parallel:** Zuntini et al. 2023 (PMID:37636262, *Front Genet*) reported a 7-year-old boy with Blaschko-linear epidermal nevi who developed paratesticular ERMS at 18 months carrying the **same `HRAS` c.37G>C p.Gly13Arg** variant in nevus and tumour but not in blood or buccal cells — *"indicating its postzygotic origin"* — with VAF 33% in nevus and 92% in tumour, plus gain of the paternal chromosome 11 carrying the mutant allele.

**Curation implication:** this supports encoding a mosaic arm via `HP:0001442` (Typified by somatic mosaicism) per the repo's `somatic-mosaicism` skill, and recording the epidermal nevus / nevus sebaceous (Schimmelpenning) association as a **mosaic RASopathy predisposition** rather than a classical germline cancer-predisposition syndrome.

### 2.3 Genetic risk factors

- **Germline:** none established. No familial clustering, no reported germline *HRAS* (Costello syndrome) case. Huang et al. explicitly note the mutational spectrum differs from Costello syndrome (exact, PMID:26872011): *"Interestingly, the HRAS mutations seen in MEM are different than the ones described in Costello syndrome, a rare multisystem disorder caused by heterozygous germline HRAS mutation..."* — while also noting Costello syndrome does confer predisposition to *"RMS, neuroblastoma, and urothelial cell carcinoma of urinary bladder."* So Costello syndrome is a plausible but **unreported** predisposition; record as a knowledge gap, not a fact.
- **Mosaic RASopathy:** established (§2.2).
- **NF1 / neurofibromatosis type 1:** **no documented association with EMS was found.** `NF1` is, however, the second most frequent genetic event in ERMS generally (PMID:38603649), and *NF1*-associated malignant triton tumour is the key differential. Do not assert an NF1–EMS link.
- **DICER1:** one adult uterine case carried `TP53`, `PTEN` and `DICER1` mutations (PMID:33595736). A single case; do not generalise.

### 2.4 Demographic risk factors

- **Male sex** — the strongest and most consistent non-molecular risk factor. All 7 MSKCC patients male (PMID:26872011); 15/17 male (PMID:42851199); 9/11 male (PMID:40221922); 8:3 male in adults (PMID:41465905); literature-wide M:F ≈ 1.38–1.4.
- **Infancy / very young age** — see §8 and §9.

### 2.5 Environmental risk factors, protective factors, gene–environment interaction

**None established.** No toxicant, radiation, infectious, dietary or lifestyle association has been reported for EMS. No protective genetic or environmental factor is known. No gene–environment interaction has been studied. Huang et al.'s observation that *HRAS* mutations were present in chemotherapy-naive tumours argues against a therapy-induced origin for the driver.

> **Curation note:** this is a legitimate `environmental:` absence. If an `environmental[]` entry is added at all, it will need the `Left deliberately uncited.` + ≥20 words `review_notes` waiver described in CLAUDE.md, recording which searches were run.

---

## 3. Phenotypes

EMS has **no constitutional phenotype**. Its clinical manifestations are entirely the **mass effect and local invasion of a soft-tissue sarcoma at its primary site**, plus metastasis. Phenotype therefore stratifies by site, which is the right way to curate it.

### 3.1 Site-driven presenting features

| Site (frequency) | Presenting phenotype | Suggested HP term | Verification |
|---|---|---|---|
| Pelvis / perineum / genitourinary (most common) | Abdominal or pelvic mass | `HP:0031500` **Abdominal mass** | ✅ verified via OLS |
| Paratesticular / spermatic cord | Painless scrotal or inguinal swelling; **masqueraded as inguinal hernia in two infants** (PMID:33648897) | no exact HP term confirmed | ⚠️ look up |
| Bladder / prostate | Urinary obstruction, retention, haematuria | ⚠️ look up | |
| Pelvic mass → ureteric compression | Hydronephrosis (bilateral grade IV reported, PMID:38496756) | ⚠️ look up `Hydronephrosis` | |
| Orbit | Proptosis | `HP:0000520` **Proptosis** | ✅ verified via OLS |
| Head & neck / submandibular | Neck mass with airway compression and **respiratory distress at birth** (PMID:40310147) | ⚠️ look up | |
| Parapharyngeal | Mass with intracranial extension (PMID:36913073) | — | |
| Extremity | Painful swelling (PMID:25405050: *"Left leg swelling and pain for one month"*) | — | |
| Tongue | Recurrent lingual lesion (PMID:24650353) | — | |
| Intracranial | Raised intracranial pressure, posterior-fossa signs | — | |

**Generic phenotype anchors worth considering for the pathograph:**
- `HP:0002859` **Rhabdomyosarcoma** ✅ verified
- `HP:0006743` **Embryonal rhabdomyosarcoma** ✅ verified
- `HP:0006779` **Alveolar rhabdomyosarcoma** ✅ verified (only for the disputed FOXO1-positive cases)
- `HP:0500092` **Orbital rhabdomyosarcoma** ✅ verified
- `HP:0004376` **Neuroblastic tumor** ✅ verified — *"A family of tumors arising in the embryonal remnants of the sympathetic nervous system, which includes neuroblastoma, ganglioneuroblastoma, and ganglioneuroma."* This is the **best single HP anchor for the neuroectodermal component**, because it covers the whole observed spectrum in one term rather than forcing a choice between neuroblastoma and ganglioneuroma.

> **Coarse-binding warning.** `HP:0004376` is a family-level term. If used, check `just check-coarse-phenotypes`; the honest `coarse_binding_basis` here is **`VARIABLE_SPECTRUM`** — the neuroectodermal component genuinely ranges from scattered ganglion cells to primitive neuroblastoma *within the same entity and sometimes the same tumour*, which is exactly what that value is for.

### 3.2 Phenotype characteristics

- **Onset:** congenital to adult; modal onset **infancy** (see §8).
- **Severity:** uniformly **severe** — a malignant sarcoma requiring multimodal therapy.
- **Progression:** **rapidly progressive** if untreated. Wikipedia/NCI-derived descriptions characterise it as "fast-growing". The 2025 adult index case grew to 30 × 19 cm over 13 months (PMID:41465905).
- **Frequency among affected individuals:** the biphasic histology is 100% by definition (*"All cases exhibited biphasic differentiation"* — PMID:42851199, exact). Mesenchymal component is ERMS in 16/17 (PMID:42851199, exact) and in all 7 MSKCC cases.
- **Quality-of-life impact:** no EQ-5D, SF-36, PROMIS or disease-specific QoL instrument has been applied to EMS. ⚠️ **Not available — record as a gap.** Inferred QoL burden derives from RMS survivorship generally (growth impairment, endocrine late effects, second malignancy after radiotherapy).

---

## 4. Genetic / Molecular Information

### 4.1 Driver genes (HGNC IDs verified via the HGNC REST API)

| Gene | HGNC | Role in EMS | Evidence |
|---|---|---|---|
| **HRAS** | `hgnc:5173` | **Principal somatic driver.** p.G13R (c.37G>C) and p.Q61L hotspots | PMID:26872011; 40629179; 38496756; 42504917 |
| **NRAS** | `hgnc:7989` | Alternative RAS driver; p.Q61H | PMID:42504917; 42851199 |
| **KRAS** | `hgnc:6407` | Seen in control ERMS, **not** reported as an EMS driver | PMID:26872011 |
| **PTPRD** | `hgnc:9668` | Co-occurring; p.V892A, p.V847L (fibronectin type III domain), index cases only | PMID:26872011 |
| **FBXW7** | `hgnc:16712` | Co-occurring; p.R505H, one case | PMID:26872011 |
| **MYOD1** | `hgnc:7611` | p.Leu122Arg in one aggressive adolescent case | PMID:36913073 |
| **CDKN2A** | `hgnc:1787` | p.Ala34Gly, same case | PMID:36913073 |
| **CDK4** | `hgnc:1773` | Amplification, same case | PMID:36913073 |
| **TP53** | `hgnc:11998` | Adult uterine case | PMID:33595736 |
| **PTEN** | `hgnc:9588` | Adult uterine case | PMID:33595736 |
| **DICER1** | `hgnc:17098` | Adult uterine case | PMID:33595736 |
| **FOXO1** | `hgnc:3819` | **Disputed** — see §4.4 | PMID:28994342 vs PMID:26872011/42851199 |
| **NF1** | `hgnc:7765` | Not implicated in EMS; relevant only to the MTT differential | PMID:38603649; PMID:42851199 |
| **PHOX2B** | `hgnc:9143` | **Characteristically low/absent** — a differential-diagnostic marker | PMID:42851199 |
| **MYCN** | `hgnc:7559` | **Not amplified** — tested and negative | PMID:26872011 |
| **ALK** | `hgnc:427` | **Not mutated** (exons 23/25) — tested and negative | PMID:26872011 |
| **SOX10** | `hgnc:11190` | Marks Schwannian differentiation when present | PMID:42851199 |

### 4.2 Variant characterisation

- **Variant type:** missense point mutations at canonical RAS hotspots. `HRAS` **c.37G>C p.(Gly13Arg)** is the single most frequent (4/7 in PMID:26872011; the Pellegrino case; one Caporalini case; the Zuntini mosaic ERMS case).
- **Functional consequence:** **gain of function** — impaired intrinsic and GAP-stimulated GTP hydrolysis, locking RAS in the GTP-bound active state. For dismech: `functional_impact_category: GAIN_OF_FUNCTION` on the `genetic_context`, and `modifier: GAIN_OF_FUNCTION` on the RAS-signalling node (the *Gain/Loss of Function: which slot?* rule in CLAUDE.md — both may co-occur here because the activity state *is* mutation-driven).
- **Origin:** **somatic** in the majority; **postzygotic/mosaic** in a documented minority (PMID:40629179). No germline case reported. `variant_origin: SOMATIC`.
- **Zygosity / allelic state:** three of four p.G13R cases showed a *"nearly homozygous pattern"* (PMID:26872011, exact) — consistent with loss of the wild-type allele or copy gain of the mutant. The Zuntini case demonstrated the mechanism directly: gain of the paternal chromosome 11 carrying the mutant *HRAS* allele, i.e. **mutant-allele dosage increase as a second hit**.
- **Population allele frequency:** not applicable — somatic hotspot mutations; gnomAD frequency is irrelevant and should not be recorded.
- **ACMG/AMP classification:** `HRAS` p.G13R and p.Q61L are oncogenic/pathogenic somatic variants; Salomatina et al. interpreted their variants *"in accordance with the AMP/ASCO/CAP Guideline recommendations"* — the correct framework for somatic variants (not ACMG/AMP germline).

### 4.3 Epigenetics — the most important 2026 finding

**Caporalini et al. 2026 (PMID:42504917, *Pediatr Blood Cancer*, doi:10.1002/1545-5017.70592)** — first genome-wide DNA methylation profiling of EMS:

> "Methylation analysis, including microdissected components, consistently aligned ectomesenchymoma with the embryonal rhabdomyosarcoma superfamily, revealing a shared myogenic epigenetic program despite neural differentiation. Shared copy-number profiles across distinct histological regions supported a monoclonal origin."

Two load-bearing conclusions:
1. **Monoclonality** — the rhabdomyoblastic and neuroectodermal components share copy-number profile, so they are **one clone differentiating two ways**, not a collision tumour.
2. **ERMS epigenetic identity persists despite neural differentiation** — the neural phenotype is layered on a myogenic epigenome.

**H3K27me3 is retained** in both components in every case tested — the discriminator from MPNST/malignant triton tumour (PMID:26872011, exact: *"All cases retained H3K27me3 expression in both RMS and neuroectodermal regions."*; corroborated PMID:42851199: *"retained H3K27me3 expression in Schwann cell areas, in contrast to the loss of H3K27me3 observed in malignant triton tumor."*). No PRC2 (`EED`, `SUZ12`) alterations were found.

### 4.4 The FOXO1 controversy — flag this explicitly in the entry

Two incompatible positions in the literature:

- **Griffin et al. 2018 (PMID:28994342)** reported *"the first demonstration of FOXO1 gene rearrangements in malignant ectomesenchymoma with alveolar rhabdomyosarcoma subtype"*, in a 6-case series where *"Embryonal and alveolar morphologies showed equal distribution, with all alveolar cases harboring characteristic translocations."* The Beijing series likewise reported FOXO1 fusion-positive in 2/11, with worse survival (PMID:40221922).
- **Huang et al. 2016 (PMID:26872011)** argue the alveolar-looking areas are **"dense pattern" ERMS**, FOXO1-negative, and a recognised ARMS mimic (exact): *"Our current results strongly suggest that the ARMS-like pattern described in MEM represents the dense ERMS."* The 17-case 2026 series supports this (exact, PMID:42851199): *"The tumor cells were all negative for FOXO1, PAX3 and PAX7."*

**Recommended curation:** model this as a `mechanistic_hypotheses` / `discussions` `KNOWLEDGE_GAP` rather than asserting either. The practical question — whether a FOXO1-rearranged biphasic tumour is "EMS" at all or is fusion-positive ARMS with neural differentiation — is unresolved and has treatment consequences (FOXO1 status is the dominant RMS risk-stratifier per NCI PDQ).

### 4.5 Expression profiling

From PMID:26872011 (exact):

> "The unsupervised hierarchical clustering using the RNAseq dataset of a large panel of >100 different soft tissue tumors showed MEM and RMS tightly grouped together, separate from all other tumor types."

> "Among the top upregulated genes in both MEM and RMS, there were many involved in skeletal muscle-function, such as MYOG (Myogenin), CHRND (Cholinergic Receptor, Nicotinic, Delta), MRLN (Myoregulin), and MEGF10 (Multiple EGF-Like-Domains 10). When comparing MEM to RMS, there were several neuronal developmental genes among the top-ranked gene list, such as EPHA3 (EPH Receptor A3), ADM (Adrenomedullin), NEFM (Neurofilament, Medium Polypeptide), SPOCK2..."

Critically — and this is a strong argument that the neural component is **not** neuroblastoma:

> "However, the main neuronal developmental genes described as up-regulated in neuroblastomas, such as MEIS1, PHOX2B, CHGA, and NTRK1, were not overexpressed in MEM."

This dovetails with the 2026 immunohistochemical finding (exact, PMID:42851199): *"Only 2 cases showed focal PHOX2B positivity... Low PHOX2B expression in the neuroblastoma component may serve as an important marker for the differential diagnosis."*

**An earlier contradicted claim:** a single "intracranial MEM" expression study clustered with MPNST. Huang et al. tested and refuted it (exact): *"Nearly all of the reported top overexpressed genes in the intracranial MEM were not detected as upregulated in our MEM and RMS group."*

### 4.6 Chromosomal abnormalities

- No recurrent translocation. Exact (PMID:26872011): *"No candidate fusion genes were detected by FusionSeq analysis."*
- **No `MYCN` amplification**, no `ALK` exon 23/25 mutation (PMID:26872011).
- **Chromosome 11 gain carrying the mutant *HRAS* allele** demonstrated as a second hit in the mosaic-ERMS parallel case (PMID:37636262).
- Shared copy-number profiles across histological regions (PMID:42504917).
- No chromosomal microarray signature is diagnostic.

---

## 5. Environmental Information

**Not applicable / none established.**

- **Environmental factors:** no toxicant, radiation or pollution exposure has been linked to EMS. CTD/TOXNET searches return nothing specific.
- **Lifestyle factors:** not applicable — the disease presents in infants, often congenitally.
- **Infectious agents:** none. No viral association reported.
- One study of maternal prenatal alcohol/tobacco/illicit drug use and childhood cancer subtypes (PMID:38112788) appears in the ectomesenchymoma citation neighbourhood but does **not** report an EMS-specific association; do not cite it as one.

---

## 6. Mechanism / Pathophysiology

### 6.1 Ordered causal chain

> Steps marked **[D]** are demonstrated in EMS tissue; **[I]** are inferred from RAS biology or from ERMS; **[H]** are hypothesis.

1. **A gain-of-function point mutation arises in `HRAS` (codon 13 or 61) — or less often `NRAS` codon 61 — in a progenitor cell during embryonic development.** **[D]** (PMID:26872011; 42504917). In a subset the mutation is **postzygotic and mosaic**, arising *"not later than the stage of migrating ectomesenchyme originating from the neural crest"* **[D]** (PMID:40629179).
   - *Branch A (mosaic):* the same variant populates skin and other tissues → **epidermal nevus / nevus sebaceous (Schimmelpenning) phenotype**, with the tumour emerging from one clone within that field. **[D]** (PMID:40629179)
   - *Branch B (sporadic):* the mutation is confined to the tumour clone. **[D]**

2. **The mutant HRAS protein cannot efficiently hydrolyse GTP**, because codons 12/13/61 are *"the conserved sites for modulating GDP/GTP binding and hydrolysis"* **[D/I]** (PMID:26872011) → **leads to** constitutive accumulation of RAS-GTP.
   - GO: `GO:0007265` **Ras protein signal transduction** ✅ verified; `GO:0046579` positive regulation of Ras protein signal transduction ✅ verified; `GO:0007264` small GTPase-mediated signal transduction ✅ verified.

3. **Constitutive RAS-GTP drives unregulated RAS/MAPK (ERK) signalling** → **results in** ligand-independent proliferative signalling in the progenitor. **[I]** — this step is standard RAS biology, not measured in EMS tissue; grade any evidence item `directness: INDIRECT`.

4. **Mutant-allele dosage is increased by a second genomic event** (loss of wild type / chromosome gain), amplifying the signal. **[D in the mosaic-ERMS parallel, PMID:37636262; D-adjacent in EMS via the "nearly homozygous" p.G13R pattern, PMID:26872011]** → **leads to** full transformation.

5. **The transformed clone adopts and retains an embryonal-rhabdomyosarcoma epigenetic program** — *"a shared myogenic epigenetic program despite neural differentiation"* **[D]** (PMID:42504917) → **results in** rhabdomyoblastic differentiation (desmin⁺, MyoD1⁺, myogenin⁺) and a skeletal-muscle gene signature (`MYOG`, `CHRND`, `MRLN`, `MEGF10`) **[D]** (PMID:26872011).
   - GO: `GO:0035914` **skeletal muscle cell differentiation** ✅ verified.
   - CL: `CL:0000056` **myoblast** ✅ verified.

6. **In parallel, within the same clone, a subpopulation executes neuroectodermal differentiation** — *"Shared copy-number profiles across distinct histological regions supported a monoclonal origin"* **[D]** (PMID:42504917) → **produces** the ganglionic/neuroblastic component, with upregulation of neuronal developmental genes (`EPHA3`, `NEFM`, `SPOCK2`) **[D]** (PMID:26872011).
   - **Branch:** the degree of neural maturation varies — scattered ganglion cells → ganglioneuroma → ganglioneuroblastoma → neuroblastoma → Schwannian (S100⁺/SOX10⁺) **[D]** (PMID:42851199; 26872011). **Critically, this neural program is *not* the sympathoadrenal neuroblastoma program**: `MEIS1`, `PHOX2B`, `CHGA`, `NTRK1` are not upregulated **[D]** (PMID:26872011) and PHOX2B is at most focally expressed **[D]** (PMID:42851199).
   - GO: `GO:0001755` **neural crest cell migration** ✅ verified (for the histogenetic hypothesis).
   - CL: `CL:0000333` **migratory neural crest cell** ✅ verified; `CL:0011012` neural crest cell ✅; `CL:0002573` **Schwann cell** ✅; `CL:0011103` **sympathetic neuron** ✅ (for the ganglionic element).

7. **The two differentiation programs remain intimately intermixed** — *"the RMS and neuroectodermal components were intimately intermixed in all cases. Even when sharp demarcation of the two elements was discerned at low power, the high magnification disclosed both scattered ganglion cells in RMS areas, as well as rhabdomyoblasts within the ganglioneuroma area"* **[D, exact, PMID:26872011]**.

8. **The RMS component supplies the malignant drive** — brisk mitotic activity (>10/10 HPF) and necrosis **[D]** (PMID:26872011) → **leads to** local invasion, regional lymph-node and haematogenous spread (lung, bone; one documented cerebellar metastasis, PMID:25405050).

9. **Mass effect and invasion at the primary site produce the clinical phenotype** (§3.1). **[D]**

**Secondary / modifying branch — treatment-induced maturation.** Ganglioneuromatous differentiation can appear or increase *after* chemotherapy: Sebire et al. 2003 described *"Extensive Posttreatment Ganglioneuromatous Differentiation of Rhabdomyosarcoma: Malignant Ectomesenchymoma in an Infant."* Huang et al. observed post-chemotherapy specimens showing *"decreased cellularity, more prominent rhabdomyoblastic maturation, and stromal hyalinization"* **[D, exact]**. This is a genuine alternative explanation for a neural component found only in a resection specimen, and should be recorded as a competing hypothesis.

### 6.2 Checklist coverage

- **Molecular pathways:** RAS/MAPK (KEGG hsa04010; Reactome "Signaling by RAS mutants"). PI3K/AKT implicated only in the MYOD1-mutant case, where the authors *"recommend combining PI3K/AKT pathway inhibitors"* (PMID:36913073).
- **Cellular processes:** dysregulated proliferation; **divergent/aberrant differentiation of a single clone** — the defining cellular abnormality; apoptosis evasion (inferred).
- **Protein dysfunction:** gain of function by impaired GTP hydrolysis (HRAS, UniProt P01112). `PTPRD` (a candidate tumour-suppressor phosphatase) and `FBXW7` (SCF ubiquitin-ligase substrate recognition) mutations are each single-case, affecting the fibronectin type III domain and the R505 substrate-binding arginine respectively (PMID:26872011).
- **Metabolic changes:** **not studied.** No metabolomics in EMS.
- **Immune involvement:** **not studied.** B7-H3 is noted as a target across extracranial paediatric solid tumours (PMID:37110590) but not EMS-specifically.
- **Tissue damage:** by tumour invasion and compression, not by a distinct injury mechanism.
- **Biochemical abnormalities:** none diagnostic; no enzyme deficiency, receptor or channel defect.
- **Epigenetic changes:** ERMS-like methylation class, H3K27me3 retained (§4.3).
- **Transcriptomics:** §4.5. **Proteomics / metabolomics / lipidomics / single-cell / spatial transcriptomics: all absent for EMS — record as knowledge gaps.** No EMS entry exists in DepMap, and no EMS cell line is catalogued in Cellosaurus to my knowledge (⚠️ verify).
- **Functional genomics screens:** none in EMS. Adjacent: rigosertib induces mitotic arrest and apoptosis in **RAS-mutated rhabdomyosarcoma and neuroblastoma** (PMID:33158997) — a directly relevant preclinical lead; and direct KRAS(G12C) inhibitors were assessed in preclinical paediatric cancer models (PMID:41340466), though G12C is not an EMS hotspot.

---

## 7. Anatomical Structures Affected

### 7.1 Primary site distribution

**Literature-wide (from the review inside PMID:26872011, exact):**

> "The majority (82%) of cases occurred in the first decade of life, with a slight male preponderance (M:F ratio of 1.38). The most common anatomic site is pelvic/perineal or intra-abdominal/retroperitoneal region (50%), followed by intra-cranial site (17%), head and neck (17%), extremities (14%), and mediastinum (2%)."

**Per-series, showing real heterogeneity the entry should not flatten:**

| Series | Dominant site |
|---|---|
| MSKCC/Padova, n=7 (PMID:26872011) | *"All except 1 occurred in the pelvic/urogenital region"* — 2 paratesticular, 1 bladder, 1 prostate, 2 pelvic soft tissue, 1 hand |
| Foshan, n=17 (PMID:42851199, exact) | *"The pelvic/genitourinary region was the most frequently involved site (8/17)"* |
| Pellegrino review, n=34 new cases (PMID:38496756) | Genitourinary/pelvic 23/34 (67%) |
| Beijing, n=11 (PMID:40221922) | **Head and neck 45.6%**, limbs 27.2%, pelvis/abdomen 27.2% |
| CWS, n=6 (PMID:22535600) | 3 limbs, 2 trunk, 1 orbit |
| Adults, n=11 (PMID:41465905) | **Head and neck 8/11** (nasal cavity/paranasal sinuses in 5); urogenital 3 |

**Pattern worth stating explicitly:** paediatric EMS is predominantly pelvic/genitourinary; **adult EMS is predominantly head and neck**. The anatomical distribution is conventionally explained by neural-crest migration routes (PMID:28994342: *"These tumors manifest at various sites due to neural crest cell migration patterns"*).

### 7.2 UBERON terms (verified via OLS)

| Site | UBERON | Status |
|---|---|---|
| pelvic region of trunk | `UBERON:0002355` | ✅ verified |
| perineum | `UBERON:0002356` | ✅ verified |
| urinary bladder | `UBERON:0001255` | ✅ verified |
| prostate gland | `UBERON:0002367` | ✅ verified |
| spermatic cord | `UBERON:0005352` | ✅ verified |
| inguinal canal | `UBERON:0003702` | ✅ verified |
| orbit, head/neck, retroperitoneal space, mediastinum, tongue, cerebrum, cerebellum | — | ⚠️ look up before binding |

### 7.3 Tissue, cell and subcellular level

- **Tissues:** skeletal muscle / soft tissue (mesenchymal component); peripheral autonomic nervous tissue (neuroectodermal component).
- **Cell populations (CL, verified):** `CL:0000056` myoblast; `CL:0011103` sympathetic neuron (ganglion cells); `CL:0002573` Schwann cell (Schwannian areas, S100⁺/SOX10⁺); `CL:0000333` migratory neural crest cell / `CL:0011012` neural crest cell (the histogenetic hypothesis).
- **Subcellular:** HRAS function requires plasma-membrane localisation (GO cellular component "plasma membrane"); no other compartment is specifically implicated. ⚠️ look up the exact GO CC CURIE before binding.
- **Lateralisation:** unilateral, as expected for a solitary soft-tissue mass. No bilateral or symmetric pattern reported.

> **Cancer cell-of-origin curation note.** Per CLAUDE.md, the cell of origin is **derived** from the pathograph node carrying `genetic_context.variant_origin: SOMATIC`. For EMS that node is the HRAS-activation node. **Which `cell_types` to bind there is genuinely unresolved** — the historical "ectomesenchyme"/neural-crest hypothesis (`CL:0000333`) versus the myogenic-progenitor reading implied by the methylation and expression data. Do **not** force a single binding; either leave `cell_types` absent on that node with a `notes:` recording the dispute, or bind the neural crest cell and state in `notes` that the expression/methylation evidence argues for a myogenic progenitor. A second derived origin would be reported by `just check-cancer-origin` as a lump/split signal, which here would be a false alarm — the ambiguity is epistemic, not two diseases.

---

## 8. Temporal Development

### 8.1 Onset

- **Age:** congenital through adulthood, but strongly skewed to infancy.
  - PMID:26872011 (abstract, exact): *"All 7 MEM patients were male, with a mean age of 7.5 months (range, 0.6 to 17 mo)."* (Note: the body text of the same paper says "median age of 7.5 months" — an internal inconsistency; prefer the abstract's "mean" if quoting.)
  - PMID:22535600 (exact): *"The median age of three females and three males was 0.6 years (range, 0.2-13.5)."*
  - PMID:42851199 (cached, exact): *"Their age was 24.0 (12.0, 46.5) months, ranging from 0.5 months to 22 years. Fourteen patients were children aged ≤5 years."*
  - PMID:40221922: median 3 years (range 1.5–11).
  - PMID:38496756 review: *"Median age: 12 months; 18 patients (53%) developed tumors in first year of life"*; overall range 0.6 months to 72 years.
  - Adults (PMID:41465905): median age of onset 46 years — a distinct, much rarer population.
  - **Congenital presentation is documented** (PMID:40310147: resection on day six of life).
- **Onset pattern:** **subacute to rapid** — a growing mass over weeks to a few months.

### 8.2 Progression and staging

- **Staging system:** EMS is staged and grouped **as rhabdomyosarcoma** — TNM stage plus IRS Clinical Group. Worked examples: `T2bN0M0`, `T1aN0M0`, `T2bN1M0` in PMID:26872011 Table 1; *"classified as Stage I, Clinical Group II"* in PMID:40310147. **Do not invent an EMS-specific staging system.**
- **Disease course:** aggressive and **relapse-prone**. The Beijing series is the starkest datapoint: **5-year OS 79% but 5-year EFS only 14%**, with relapse in 6/11 at a median of 2 years (PMID:40221922). CWS: all 6 achieved first complete remission but *"three recurrences occurred"* (PMID:22535600, exact). EpSSG: *"six patients were alive in first remission, two in second remission and one after second tumor"* (PMID:36440693).
- **Progression rate:** rapid locally; metastasis to lung, bone, and regional (retroperitoneal, inguinal) lymph nodes.
- **Duration:** not chronic — either cured by multimodal therapy or fatal. No self-limited course.

### 8.3 Patterns

- **Remission:** treatment-induced only; **no spontaneous regression reported** (contrast with infantile neuroblastoma, where it is well described — a useful differential point).
- **Critical periods:** the only window of therapeutic opportunity is early, complete local control. Resectability is repeatedly identified as the dominant modifiable prognostic variable (PMID:25405050: resectability is the *"most important independent prognostic factor"*; PMID:41465905: *"Treatment approaches and prognosis are correlated with the completeness of tumor resection and the differentiation degree of both components."*).
- **A diagnostic timing pattern specific to EMS:** the diagnosis is frequently made only on the resection specimen, because a small biopsy samples only the RMS areas. PMID:26872011 (exact): *"Two cases were diagnosed as RMS on the biopsy, and subsequently recognized as MEM on the resection specimen."* EpSSG: *"seven had an initial local diagnosis of rhabdomyosarcoma"* (7/10). This has real clinical consequences — see PMID:32769567, *"More Than Meets the Eye? A Cautionary Tale of Malignant Ectomesenchymoma Treated as Low-risk Orbital Rhabdomyosarcoma."*

---

## 9. Inheritance and Population

### 9.1 Epidemiology

- **Incidence / prevalence:** **no population-based incidence or prevalence figure exists.** EMS is not separately coded in SEER or any national cancer registry. The only denominator-anchored figure located is from EpSSG — reportedly 10 of 1321 (0.8%) patients enrolled in the EpSSG NRSTS 2005 study (⚠️ **this denominator came from a web search summary, not from the abstract; verify against the full text of PMID:36440693 before recording it**).
- **Cumulative case count** — the honest way to express rarity, and it has moved over time:
  - ~50 cases (2013, PMID:22535600, exact: *"To date merely 50 cases have been published"*)
  - ~64 cases (2016, PMID:26872011, exact: *"Approximately 64 cases of MEM have been so far documented in the literature, mostly as single case reports."*)
  - **98 cases** (2024, PMID:38496756 — 40 pre-1998, 24 in 1998–2014, 33 new since 2014)
  - "<150 cases" (2025, PMID:41465905)
- **Prevalence class for dismech:** `BELOW_1_IN_1000000` with `measure_type: CASES_IN_LITERATURE` is the defensible encoding. Do **not** fabricate a `rate_per_100000`.

### 9.2 Inheritance

- **Inheritance pattern:** **none — sporadic somatic neoplasm.** The only heritable-adjacent mechanism is **postzygotic mosaicism**, which is not transmitted.
  - For the mosaic arm, the appropriate HPO mode-of-inheritance binding is **`HP:0001442` Typified by somatic mosaicism** (per the repo's `somatic-mosaicism` skill), supported by PMID:40629179.
- **Penetrance, expressivity, anticipation, germline mosaicism, founder effects, consanguinity, carrier frequency:** **all not applicable.** No germline allele exists to characterise.

### 9.3 Population demographics

- **Sex ratio:** consistently **male-predominant**. Literature-wide M:F 1.38 (PMID:26872011, exact); 7/7 male in MSKCC; 15/17 male (88%) in Foshan; 9/11 male (82%) in Beijing; 8:3 in adults; but **3M:3F in the CWS series** (PMID:22535600) — so the male excess is real but not absolute, and small-series variance is large.
- **Age distribution:** 82% in the first decade (PMID:26872011); 53% in the first year of life (PMID:38496756); a separate, much smaller adult peak at median 46 years (PMID:41465905).
- **Ethnic / geographic distribution:** **no population-specific predilection reported.** Cases come from Europe, North America, China, Russia, Japan and the Middle East. No founder effect, no variant geography. The Beijing (PMID:40221922), Foshan (PMID:42851199) and Moscow (PMID:40629179) series simply reflect where large paediatric centres publish.

---

## 10. Diagnostics

### 10.1 Diagnostic criterion — the entity is defined histologically

The operative criterion, from PMID:26872011 (exact):

> "The diagnosis of MEM was confirmed by the presence of a biphasic tumor, with histologic evidence of RMS and neuroectodermal elements. The latter component included variable ganglion cells, ganglioneuroma, ganglioneuroblastoma, or neuroblastoma foci, following the criteria of the International Neuroblastoma Pathology Classification."

And a crucial negative criterion (exact):

> "Immunohistochemical staining for neural markers alone without morphologic evidence of neural / neuronal differentiation was considered insufficient for diagnosis."

The 2026 series adds a counterbalancing refinement (PMID:42851199, cached, exact):

> "S-100 and SOX10 are key and reliable markers for confirming the neuroectodermal component, while negativity of neuroendocrine markers such as SYN does not exclude this differentiation."

The authors also describe **two previously unrecognised architectural patterns**: *"In addition to the classic configuration, two distinctive architectural patterns, namely micronest and inverted, were identified."*

### 10.2 Histopathology

- **Mesenchymal component:** ERMS in essentially all cases, with classic alternating myxoid–cellular, spindle-cell, or **"dense"** patterns (PMID:26872011). Brisk mitoses >10/10 HPF, necrosis.
- **Neuroectodermal component (frequencies, PMID:26872011):** ganglioneuroma 4/7 (most prevalent), scattered ganglion cells 1, ganglioneuroblastoma 1, neuroblastoma 1. **Foshan series differs materially (PMID:42851199, exact):** *"neuroblastoma in 12 cases, ganglioneuroma/ganglion cells in 2 cases, composite ganglioneuroblastoma in 1 case, and Schwann cell differentiation in 2 cases."* Record both distributions; do not average them.
- **Post-chemotherapy changes:** decreased cellularity, rhabdomyoblastic maturation, stromal hyalinisation (PMID:26872011).

### 10.3 Immunohistochemistry

| Component | Positive | Source |
|---|---|---|
| Rhabdomyosarcomatous | **desmin, MyoD1, myogenin** — *"The mesenchymal component uniformly expressed desmin, MyoD1, and Myogenin"* (PMID:42851199, cached, exact) | |
| Neuroblastic | synaptophysin, NSE, chromogranin A, CD56; also PGP9.5, tyrosine hydroxylase (PMID:25405050) | PMID:42851199 |
| Schwannian | **S-100 and/or SOX10 only** (PMID:42851199, exact) | |
| Neuropil | GFAP (PMID:26872011) | |
| **H3K27me3** | **RETAINED** in both components (vs lost in MPNST/MTT) | PMID:26872011; 42851199 |
| **PHOX2B** | **negative or only focal** — only 2/17 focally positive | PMID:42851199 |
| **FOXO1 / PAX3 / PAX7** | negative (disputed — §4.4) | PMID:42851199 |

### 10.4 Molecular diagnostics

**Recommended approach, as stated by the field:**
- **RAS-pathway hotspot testing** (`HRAS` exons 2–3, `NRAS` exons 2–3, `KRAS` exon 2) — PMID:42504917: *"RAS-pathway testing and methylation profiling can significantly refine diagnostic precision."*
- **FOXO1 FISH** to exclude fusion-positive ARMS.
- **H3K27me3 IHC** to exclude MPNST / malignant triton tumour.
- **DNA methylation profiling** — now shown to classify EMS within the ERMS superfamily (PMID:42504917). This is the most discriminating ancillary test described to date.
- **Germline/normal-tissue testing in the presence of a cutaneous nevus phenotype**, to detect mosaic *HRAS* (PMID:40629179).
- PMID:38496756 explicitly recommends that *"The future diagnostic approach should routinely include molecular analysis and the use of bioinformatic mutation detection tools."*

**Not useful / negative:** `MYCN` amplification, `ALK` mutation (both tested and absent — PMID:26872011); no diagnostic karyotype, CMA signature, mtDNA or repeat-expansion test applies.

**Omics diagnostics:** RNA-seq is useful (expression clustering with RMS; RNA-seq-based classifiers such as CanID, PMID:41317384, include EMS in their neighbourhood). Proteomics, metabolomics and liquid biopsy are **not established** for EMS — though patient-specific ctDNA panels have been shown to work in rhabdomyosarcoma independent of genetic profile (PMID:41120703), an approach directly transferable to EMS.

### 10.5 Imaging

No EMS-specific imaging signature exists. Reported features (⚠️ all from case reports; verify each quote):
- **MRI:** isointense to hypointense on T1, heterogeneous on T2, patchy contrast enhancement; MR angiography may show prominent feeding arteries.
- **CT/US:** solid, heterogeneous mass, often with cystic and necrotic components and heterogeneous enhancement; enlarged regional nodes with similar appearance, suggesting metastasis (PMID:25405050: *"heterogeneous partially cystic enhancing bilobed mass at the left side of the pelvis, measuring 5.7 × 4.3 × 4.0 cm"*).
- Site-specific consequences: bilateral grade IV hydronephrosis from an abdomino-pelvic mass (PMID:38496756); airway compression from a submandibular mass (PMID:40310147).
- FAPI PET in soft-tissue sarcoma is under systematic review (PMID:40979140) but has no EMS-specific data.

### 10.6 Differential diagnosis

| Entity | Discriminator |
|---|---|
| **Embryonal rhabdomyosarcoma** (pure) | Absence of a morphologically demonstrable neuroectodermal component. *This is the hardest and most consequential distinction* — and the two are now understood to be biologically continuous. |
| **Alveolar RMS** | FOXO1 rearrangement; the "dense pattern" ERMS of EMS is FOXO1-negative (PMID:26872011) |
| **Malignant triton tumour / MPNST with rhabdomyoblastic differentiation** | **Loss of H3K27me3**, PRC2 (EED/SUZ12) alterations, `NF1` alterations, CDKN2A/B loss — all *absent* in EMS (PMID:26872011; 42851199; 38603649). Prognosis differs sharply: 5-year survival 70% for NF1-mutant RMS vs 33% for MTT (PMID:38603649). |
| **Neuroblastoma / ganglioneuroblastoma** | EMS lacks MYCN amplification and the sympathoadrenal transcriptional program; **PHOX2B is negative or only focal** (PMID:42851199; 26872011) |
| **Teratoma** | Absence of a third germ layer; EMS is monoclonal and biphenotypic, not tri-germinal. (Note one reported collision: teratoma with malignant ectomesenchymoma in the pineal region, PMID:36081970.) |
| **Benign triton tumour / neuromuscular choristoma** | Benign, mature; but one reported case blurs the line (PMID:24650353) |
| **Other small round blue cell tumours** (Ewing, DSRCT, Wilms) | Marker panels; see PMID:28968263, *"Malignant Ectomesenchymoma: A Potential Pitfall of Diagnosis in the Spectrum of Pediatric Small Blue Round Cell Tumors."* |

### 10.7 Screening

**No screening programme exists or is warranted** — the disease is far too rare for population screening, there is no newborn-screening analyte, and no carrier state exists. The one defensible surveillance context is a child with a **mosaic RASopathy phenotype (epidermal nevus, nevus sebaceous/Schimmelpenning)**, where soft-tissue tumour risk is now documented (PMID:40629179; PMID:37636262). ⚠️ No published surveillance protocol for that indication was located.

---

## 11. Outcome / Prognosis

### 11.1 Survival

**The headline finding of the modern literature: outcomes are far better than the historical "uniformly poor prognosis" framing, when patients are treated on rhabdomyosarcoma protocols.**

| Series | n | Outcome |
|---|---|---|
| MSKCC/Padova (PMID:26872011, exact) | 7 | *"No recurrence or metastasis occurred in 6 cases with available follow-up data during a median period of 5.4 years (range, 0.9–16.7)."* 1 died of other causes. |
| CWS (PMID:22535600, exact) | 6 | *"All patients achieved first complete remission, but three recurrences occurred. The individual with metastatic MEM did not survive, but all five patients with localized MEM are currently alive in CR with a median follow-up of 5 years (range: 2.1-13.7)."* |
| EpSSG (PMID:36440693) | 10 | *"Overall, six patients were alive in first remission, two in second remission and one after second tumor. Only the patient with initially metastatic tumor died of disease."* |
| Beijing (PMID:40221922) | 11 | **5-year OS 79%; 5-year EFS 14%**; relapse 6/11 at median 2 years |
| Pellegrino review (PMID:38496756) | 28 with follow-up | 23 NED, 4 died of disease, 1 alive with metastatic disease; mean follow-up 38.5 months |
| Literature reviews (PMID:25405050) | — | survival *"71%"* to *"83%"* with multimodality treatment |
| Adults (PMID:41465905) | 11 | Resectable + well-differentiated → no recurrence/death over 7 months–6 years; poorly differentiated → fatal |

**The crucial nuance to carry into the entry:** the Beijing series' **OS 79% / EFS 14%** split means most patients relapse but many are salvaged. Do not report OS alone.

### 11.2 Mortality and complications

- **Disease-specific mortality** concentrates in: metastatic disease at presentation (fatal in both the CWS and EpSSG metastatic cases), unresectable disease, and poorly differentiated neuroblastic components in adults.
- **Metastatic pattern:** haematogenous to **lung and bone**; lymphatic to **retroperitoneal and inguinal nodes**; one reported **cerebellar metastasis** at 21 months (PMID:25405050); one adult paratesticular case with post-operative lung-metastasis flare (PMID:26793539). PMID:26872011 documented locoregional nodal metastasis in which *"the lymph node mets revealed both RMS and neuroblastoma areas"* — i.e. **both components metastasise**.
- **Second tumours:** one EpSSG patient was alive *"after second tumor"* (PMID:36440693). Radiotherapy-associated late malignancy risk applies as for RMS.
- **Morbidity / disability:** driven by site and local therapy — orbital exenteration, cystectomy/prostatectomy sequelae, limb function, airway management in congenital neck disease. **No ICF-coded or disability-registry data exists for EMS.**
- **Quality of life:** ⚠️ **no EMS-specific QoL data.** Record as a gap.

### 11.3 Prognostic factors

Ranked by the strength of evidence actually available:

1. **Metastatic disease at diagnosis** — the clearest adverse factor; fatal in both series' metastatic cases.
2. **Complete resection** — *"the most important independent prognostic factor"* (PMID:25405050); *"prognosis are correlated with the completeness of tumor resection"* (PMID:41465905).
3. **Receipt of local radiotherapy** — Beijing series: relapse 2/6 with RT+chemo vs 5/5 with chemo alone, **P = 0.046** (PMID:40221922). Note: small n, retrospective, unadjusted.
4. **Differentiation grade of the neuroectodermal component** — poorly differentiated/undifferentiated neuroblastoma associated with worse outcome in adults (PMID:41465905).
5. **FOXO1 fusion status** — associated with worse survival in the Beijing series (PMID:40221922); consistent with RMS risk stratification generally, but entangled in the §4.4 dispute about whether such cases are EMS at all.
6. **Prognostic biomarkers:** none validated. No FDA-recognised biomarker for EMS.

---

## 12. Treatment

### 12.1 Overall strategy

**Treat as rhabdomyosarcoma.** This is the single clearest therapeutic statement the literature supports, and it is stated by every cooperative group.

PMID:22535600 (exact): *"Risk-factors and outcome of MEM appear comparable with other highly malignant pediatric soft tissue sarcoma when multimodal treatment strategy including chemotherapy and adequate local treatment is pursued."*

PMID:36440693: *"All patients received chemotherapy according to rhabdomyosarcoma strategy, four had radiotherapy."*

PMID:38496756: *"General consensus for the management and therapeutic regimen for MEM seems to be a multimodal treatment strategy, including a combination of surgery and chemotherapy."*

NCI PDQ (Childhood Soft Tissue Sarcoma Treatment, health-professional version, last updated 04/21/2025) lists ectomesenchymoma under **skeletal muscle tumours** and states that treatment *"may include surgery, chemotherapy, and radiation therapy."*

### 12.2 Chemotherapy regimens actually used

| Regimen / protocol | Drugs | Reported in |
|---|---|---|
| **VAC** | vincristine, dactinomycin (actinomycin D), cyclophosphamide | PMID:40310147; COG standard |
| **VIT / VI** | vincristine, irinotecan (± temozolomide) | PMID:40310147 (after VAC failure); COG intermediate-risk |
| **IVA / IVADo** | ifosfamide, vincristine, dactinomycin (± doxorubicin) | PMID:38496756; EpSSG RMS2005 |
| **VDC/IE** | vincristine, doxorubicin, cyclophosphamide / ifosfamide, etoposide | PMID:41465905 |
| **COG ARST0531** | — | PMID:26872011 Table 1 (2 patients) |
| **EpSSG 2005**, **RMS96**, **MSKCC P6** | — | PMID:26872011 Table 1 |
| Maintenance | cyclophosphamide + vinorelbine | PMID:38496756 |
| Neuroblastoma-directed | COG-ANBL0532, after RMS-directed COG-ARST08P1 | PMID:25405050 — a **rare** strategy of treating both components |

CWS description (PMID:36440693 context): *"systemic therapy typically consisted of regimens with dactinomycin, ifosfamide or cyclophosphamide, and vincristine, with or without doxorubicin."*

**Verified CHEBI identifiers for `therapeutic_agent`:**

| Drug | CHEBI | Status |
|---|---|---|
| vincristine | `CHEBI:28445` | ✅ verified via OLS |
| dactinomycin / actinomycin D | `CHEBI:27666` (**label is "actinomycin D"**) | ✅ verified — note the label is *not* "dactinomycin"; `preferred_term` should carry the clinical name |
| cyclophosphamide | `CHEBI:4027` | ✅ verified |
| ifosfamide | `CHEBI:5864` | ✅ verified |
| doxorubicin | `CHEBI:28748` | from the repo's own CLAUDE.md worked example |
| irinotecan | `CHEBI:80630` | from the repo's own CLAUDE.md worked example |
| vinorelbine, etoposide, temozolomide | — | ⚠️ look up |

**NCIT treatment-action terms** (taken from the documented list in this repository's CLAUDE.md, still to be confirmed with `just validate-terms`):
- `NCIT:C15986` Pharmacotherapy — with `therapeutic_agent` for each drug
- `NCIT:C15632` Chemotherapy — for the combination regimens
- `NCIT:C15329` Surgical Procedure — resection
- `NCIT:C15313` Radiation Therapy
- `NCIT:C15747` Supportive Care
- ⚠️ No named-regimen NCIT `regimen_term` was verified for VAC/IVA/VIT. **Do not invent one** — the CLAUDE.md rule is explicit that `regimen_term` requires an NCIT identity reachable from `NCIT:C15697`. Look up "VAC Regimen" before using it; otherwise leave `regimen_term` absent and list the agents.

### 12.3 Surgery and radiotherapy

- **Surgery is the primary local modality**; complete resection is the dominant modifiable prognostic variable (§11.3). Reported procedures include radical orchiectomy (paratesticular), wide local excision with parotidectomy and neck dissection (PMID:41465905), and neonatal neck-mass resection on day 6 of life (PMID:40310147). Robotic-assisted approaches have been described in paediatric surgical oncology generally (PMID:38197107).
- **Radiotherapy** is used for residual/unresectable disease and is associated with significantly lower relapse in the one series that tested it (PMID:40221922). `therapeutic_modality: RADIOTHERAPY`.

### 12.4 Targeted, immuno- and advanced therapies

**None approved or established for EMS.** Rational leads, all preclinical or extrapolated:

- **RAS-pathway inhibition.** Rigosertib induces mitotic arrest and apoptosis in **RAS-mutated rhabdomyosarcoma and neuroblastoma** (PMID:33158997) — the most directly relevant preclinical result. Broader context: *"Targeting RAS in pediatric cancer: is it becoming a reality?"* (PMID:31815779) and the NCI-sponsored RAS/RASopathy therapy collaboration (PMID:31913576). Direct KRAS(G12C) inhibitors have been assessed in paediatric preclinical models (PMID:41340466) — **not applicable to EMS hotspots** (G13R/Q61L are not G12C).
- **MEK inhibition** is the obvious mechanistic candidate for an HRAS-driven tumour but ⚠️ **no EMS case treated with a MEK inhibitor was found.** State this as a gap, not a recommendation.
- **PI3K/AKT inhibition** was recommended by the authors of the MYOD1-mutant case (PMID:36913073), on the basis of that genotype rather than EMS generally.
- **B7-H3** is proposed as a target across extracranial paediatric solid tumours (PMID:37110590).
- **Gene therapy, cell therapy (CAR-T), RNA-based therapy, checkpoint inhibition:** **no EMS data.**

### 12.5 Pharmacogenomics, adverse events, treatment algorithms

- **Pharmacogenomics:** no EMS-specific PGx. General RMS-protocol PGx applies (e.g. cyclophosphamide/ifosfamide metabolism, anthracycline cardiotoxicity risk alleles) — not EMS-specific, do not curate as such.
- **Adverse events:** those of the RMS backbone — myelosuppression, ifosfamide nephro/neurotoxicity, anthracycline cardiomyopathy, cyclophosphamide gonadal toxicity and haemorrhagic cystitis, radiotherapy growth/endocrine late effects and second malignancy. See PMID:28333415 (chemotherapy-induced toxicities in metastatic RMS) and PMID:33815276 (endocrine complications in children with non-CNS solid tumours) for the relevant literature, bearing in mind neither is EMS-specific.
- **Clinical trials:** ⚠️ **No EMS-specific trial (NCT) was identified.** Patients are enrolled on RMS trials. If a `clinical_trials:` block is added, it should cite RMS protocols the published EMS patients were actually treated on (COG ARST0531, EpSSG RMS2005) rather than a trial that enrolled EMS as such — and each NCT must be fetched with `just fetch-reference`.
- **Personalised medicine:** the actionable step today is **molecular profiling at diagnosis** (PMID:38496756; PMID:42504917; PMID:41373618 on targeted DNA sequencing for tailored therapies in children with extracranial solid tumours).

---

## 13. Prevention

**No prevention is possible or applicable**, and the entry should say so plainly rather than leave the section empty.

- **Primary prevention:** none. The driver is a sporadic (often prezygotically-undetectable, postzygotic) somatic mutation with no known environmental contributor. No vaccine, no modifiable risk factor.
- **Secondary prevention / early detection:** no screening programme (§10.7). The one actionable early-detection context is **a child with a mosaic RASopathy cutaneous phenotype** — clinical vigilance for soft-tissue masses is reasonable but no protocol is published (PMID:40629179; PMID:37636262; PMID:42959308 on mosaic RASopathy management).
- **Tertiary prevention:** complete resection plus protocol-directed chemotherapy ± radiotherapy to prevent relapse (§12), and standard RMS survivorship surveillance for late effects.
- **Genetic counselling:** **recurrence risk is not increased for siblings or offspring** in sporadic cases. In a mosaic *HRAS* case, counselling should address the **postzygotic** nature of the variant — it is not inherited, and gonadal involvement would need separate assessment before any statement about offspring risk. Prenatal testing and PGD are not applicable.
- **Immunisation, public-health and environmental interventions:** not applicable.

---

## 14. Other Species / Natural Disease

- **Species affected:** **Homo sapiens (`NCBITaxon:9606`) only.** ⚠️ No naturally occurring ectomesenchymoma has been reported in any other species in the literature searched. No OMIA entry was located.
- **Breed (VBO):** not applicable.
- **Orthologous genes:** *HRAS* has orthologues across vertebrates (mouse *Hras*, rat *Hras*, zebrafish *hrasa/hrasb*) — ⚠️ **look up the MGI/RGD/ZFIN identifiers before binding; CLAUDE.md requires MOD identifiers for non-human genes, and the term validator does not check them.**
- **Comparative pathology:** nothing published for this entity. Broadly comparable "mixed" sarcomas with divergent differentiation occur in veterinary oncology, but no equivalence has been established.
- **Evolutionary conservation of mechanism:** the RAS/MAPK pathway and neural-crest developmental program are deeply conserved, which is the basis for the model-organism approaches below — but this is general biology, not an EMS-specific comparative finding.
- **Zoonotic potential / cross-species transmission:** not applicable (non-infectious neoplasm).

---

## 15. Model Organisms

### 15.1 The honest headline

**There is no published animal or cell-line model of ectomesenchymoma.** Searches for EMS-specific mouse, zebrafish, organoid, iPSC or cell-line models returned nothing. This is the single largest experimental gap for this entity and should be recorded as a `KNOWLEDGE_GAP` discussion, not glossed over.

### 15.2 Adjacent models that cover parts of the biology

| Model | Covers | Does not cover | Reference |
|---|---|---|---|
| **Nf1/Ink4a-Arf loss GEMM of ERMS** — described as *"the first animal model of NF1-mutated RMS"* | Myogenic sarcomagenesis under RAS-pathway activation | Wrong gene (NF1 not HRAS); **no neuroectodermal component reported** | PMC9955904 (⚠️ get PMID) |
| **MyoD-Cre; Kras^G12D; p53 GEMM of RMS** | Myogenic-lineage-restricted RAS-driven RMS | Lineage is restricted to MyoD⁺ cells by design, so it **cannot** produce the biphasic phenotype; wrong RAS isoform | PMC8844455 (⚠️ get PMID) |
| **kRAS-induced zebrafish ERMS** — *"zebrafish rhabdomyosarcoma is highly similar to human embryonal rhabdomyosarcoma"* | ERMS histogenesis, live imaging of tumour-propagating cells | Wrong RAS isoform; no neural component | PMID:21951539 |
| **Tg(HRAS^G12V) zebrafish (Costello syndrome model)** | Germline-equivalent HRAS activation; tumour-prone (lymphoma, melanoma, sarcoma) | Wrong codon (G12V vs G13R/Q61L); not lineage-targeted; no EMS phenotype reported | (see zebrafish cancer model reviews) |
| **PAX3-FOXO1 transgenic zebrafish** | Fusion-positive ARMS | Irrelevant to fusion-negative EMS | PMID:29618609 ⚠️ verify |

### 15.3 What a real EMS model would need — and why none exists

The defining feature of EMS is **one clone executing two differentiation programs**. Every existing model activates RAS in a *lineage-committed* compartment (MyoD⁺ myoblasts, satellite cells), which structurally precludes the neuroectodermal arm. The mosaicism data (PMID:40629179) point directly at the experiment that has not been done: **conditional activation of `Hras` p.G13R in migratory neural crest or in a bipotent ectomesenchymal progenitor** (e.g. a Wnt1-Cre or Sox10-CreER driver), which would test whether the biphasic phenotype is a property of the cell of origin rather than of the mutation.

**For dismech `ModelMechanismLink` curation:** every model above would need `relationship: PARTIALLY_RECAPITULATES` at best, `fidelity: LOW`, and a `divergences` entry — most naturally `BOUNDARY_OMISSION` with `materiality: QUALIFYING` (the neuroectodermal compartment is simply not in the model) plus `SPECIES_MISMATCH`. None should be linked with `RECAPITULATES`.

### 15.4 Resources

MGI, RGD, ZFIN, IMPC, IMSR, Cellosaurus, DepMap — **none holds an ectomesenchymoma-designated model or line.** ⚠️ Verify Cellosaurus and DepMap directly before asserting absence in the entry.

---

## Appendix A — Reference list with PMIDs

**Read from the committed cache (quotes are exact):**
- **PMID:26872011** — Huang SC, Alaggio R, Sung YS, Chen CL, Zhang L, Kao YC, Agaram NP, Wexler LH, Antonescu CR. *Frequent HRAS Mutations in Malignant Ectomesenchymoma: Overlapping Genetic Abnormalities With Embryonal Rhabdomyosarcoma.* Am J Surg Pathol 2016;40(7):876–85. doi:10.1097/PAS.0000000000000612 — **full text in cache**
- **PMID:42851199** — Zeng M, Li HL, Xu YY, Xie L, Mao RJ. *[Clinicopathological and molecular genetic characteristics of embryonal rhabdomyosarcoma with divergent neuroectodermal differentiation: an analysis of 17 cases].* Zhonghua Bing Li Xue Za Zhi 2026. doi:10.3760/cma.j.cn112151-20260315-00174 — **abstract in cache**

**Retrieved via Europe PMC / publisher — ⚠️ re-fetch before quoting:**
- PMID:42504917 — Caporalini C, et al. *DNA Methylation Profiling of Pediatric Ectomesenchymoma Supports Embryonal Rhabdomyosarcoma-Like Epigenetic Identity.* Pediatr Blood Cancer 2026. doi:10.1002/1545-5017.70592
- PMID:40629179 — Salomatina AS, et al. *Somatic and mosaic HRAS mutations in pediatric malignant ectomesenchymoma.* J Hum Genet 2025;70(10):497–501. doi:10.1038/s10038-025-01363-9
- PMID:36440693 — Milano GM, Orbach D, Casanova M, et al. *Malignant ectomesenchymoma in children: The European pediatric Soft tissue sarcoma Study Group experience.* Pediatr Blood Cancer 2023;70(2):e30116. doi:10.1002/pbc.30116
- PMID:22535600 — Dantonello TM, Leuschner I, Vokuhl C, et al. *Malignant ectomesenchymoma in children and adolescents: report from the Cooperative Weichteilsarkom Studiengruppe (CWS).* Pediatr Blood Cancer 2013;60(2):224–9. doi:10.1002/pbc.24174
- PMID:40221922 — Meng Y, Su Y, Zhang G, et al. *A single-center retrospective study of malignant ectomesenchymoma in children.* Jpn J Clin Oncol 2025;55(6):621–5. doi:10.1093/jjco/hyaf040
- PMID:38496756 — Pellegrino F, Tirtei E, et al. *An integrative morpho-molecular approach in malignant ectomesenchymoma diagnosis: report of a new paediatric case and a review of the literature.* Front Oncol 2024. doi:10.3389/fonc.2024.1320541
- PMID:28994342 — Griffin BB, Chou PM, George D, Jennings LJ, Arva NC. *Malignant Ectomesenchymoma: Series Analysis of a Histologically and Genetically Heterogeneous Tumor.* Int J Surg Pathol 2018. doi:10.1177/1066896917734915
- PMID:36913073 — Pena-Burgos EM, et al. *First Reported Case of Malignant Ectomesenchymoma with p.Leu122Arg Mutation in MYOD1 Gene.* Head Neck Pathol 2023. doi:10.1007/s12105-023-01542-0
- PMID:33595736 — Davidson B, et al. *Primary uterine ectomesenchymoma harboring a DICER1 mutation.* Virchows Arch 2021. doi:10.1007/s00428-021-03057-x
- PMID:40310147 — Blanchard ISC, et al. *Congenital Malignant Ectomesenchymoma Presenting as a Neck Mass in a Newborn.* Children (Basel) 2025;12(4):480. doi:10.3390/children12040480
- PMID:37636262 — Zuntini R, et al. *Case Report: Sequential postzygotic HRAS mutation and gains of the paternal chromosome 11...* Front Genet 2023. doi:10.3389/fgene.2023.1231434
- PMID:38603649 — de Traux de Wardin H, et al. *NF1-Driven Rhabdomyosarcoma Phenotypes.* JCO Precis Oncol 2024. doi:10.1200/PO.23.00597
- PMID:24650353 — VandenHeuvel KA, et al. *Ectomesenchymoma with embryonal rhabdomyosarcoma and ganglioneuroma, arising in association with benign triton tumor of the tongue.* Pediatr Dev Pathol 2014.
- PMID:25405050 — Nael A, et al. *Metastatic malignant ectomesenchymoma initially presenting as a pelvic mass.* Case Rep Pediatr 2014.
- PMID:41465905 — *Clinicopathological observation of adult malignant ectodermal mesenchymoma: case report and literature review.* Medicine (Baltimore) 2025.
- PMID:28968263 · PMID:32769567 · PMID:33648897 · PMID:30907031 · PMID:26793539 · PMID:36097907 · PMID:36081970 · PMID:42839882 (WHO STB6) · PMID:33158997 (rigosertib) · PMID:34755412 (RAS/RAF-driven ERMS) · PMID:21951539 (zebrafish RMS)
- Historical: PMID:5313338 (Holimon & Rosenblum 1971) · PMID:872048 (Karcioglu 1977) · PMID:4947980 (Shuangshoti & Netsky 1971) · Boué DR et al. *Clinicopathologic Study of Ectomesenchymomas from IRS Groups III and IV.* Pediatr Dev Pathol 2000;3:290–300 (⚠️ PMID not confirmed)

---

## Appendix B — Ontology suggestions, with verification status

| Slot | CURIE | Label | Verified? |
|---|---|---|---|
| `disease_term` | `MONDO:0002855` | ectomesenchymoma | ✅ OLS |
| cross-ref | `NCIT:C4716` | Ectomesenchymoma | ✅ OLS |
| phenotype | `HP:0002859` | Rhabdomyosarcoma | ✅ OLS |
| phenotype | `HP:0006743` | Embryonal rhabdomyosarcoma | ✅ OLS |
| phenotype | `HP:0006779` | Alveolar rhabdomyosarcoma | ✅ OLS |
| phenotype | `HP:0500092` | Orbital rhabdomyosarcoma | ✅ OLS |
| phenotype | `HP:0004376` | Neuroblastic tumor | ✅ OLS — coarse, needs `VARIABLE_SPECTRUM` basis |
| phenotype | `HP:0031500` | Abdominal mass | ✅ OLS |
| phenotype | `HP:0000520` | Proptosis | ✅ OLS |
| inheritance (mosaic arm) | `HP:0001442` | Typified by somatic mosaicism | from repo CLAUDE.md — ⚠️ confirm label |
| gene | `hgnc:5173` | HRAS | ✅ HGNC REST |
| gene | `hgnc:7989` / `hgnc:6407` / `hgnc:9668` / `hgnc:16712` / `hgnc:7611` / `hgnc:3819` / `hgnc:17098` / `hgnc:11998` / `hgnc:9588` / `hgnc:1787` / `hgnc:1773` / `hgnc:7765` / `hgnc:9143` / `hgnc:7559` / `hgnc:427` / `hgnc:11190` | NRAS / KRAS / PTPRD / FBXW7 / MYOD1 / FOXO1 / DICER1 / TP53 / PTEN / CDKN2A / CDK4 / NF1 / PHOX2B / MYCN / ALK / SOX10 | ✅ HGNC REST |
| biological process | `GO:0007265` | Ras protein signal transduction | ✅ OLS |
| biological process | `GO:0046579` | positive regulation of Ras protein signal transduction | ✅ OLS |
| biological process | `GO:0035914` | skeletal muscle cell differentiation | ✅ OLS |
| biological process | `GO:0001755` | neural crest cell migration | ✅ OLS |
| cell type | `CL:0000056` | myoblast | ✅ OLS |
| cell type | `CL:0000333` | migratory neural crest cell | ✅ OLS |
| cell type | `CL:0002573` | Schwann cell | ✅ OLS |
| cell type | `CL:0011103` | sympathetic neuron | ✅ OLS |
| anatomy | `UBERON:0002355` / `UBERON:0002356` / `UBERON:0001255` / `UBERON:0002367` / `UBERON:0005352` / `UBERON:0003702` | pelvic region of trunk / perineum / urinary bladder / prostate gland / spermatic cord / inguinal canal | ✅ OLS |
| chemical | `CHEBI:28445` / `CHEBI:27666` / `CHEBI:4027` / `CHEBI:5864` | vincristine / actinomycin D / cyclophosphamide / ifosfamide | ✅ OLS |
| treatment | `NCIT:C15986`, `C15632`, `C15329`, `C15313`, `C15747` | Pharmacotherapy, Chemotherapy, Surgical Procedure, Radiation Therapy, Supportive Care | from repo CLAUDE.md — run `just validate-terms` |

**Every CURIE above marked ✅ was read from a live OLS or HGNC lookup performed while writing this report; none was written from memory. The ⚠️ rows were not resolved and must be looked up before binding.**

---

## Appendix C — Recorded knowledge gaps

1. **Cell of origin is unresolved** — migratory neural crest ("ectomesenchyme") vs a myogenic progenitor with latent neural competence. The methylation and expression data favour the latter; the mosaicism timing data favour the former. No experiment discriminates them.
2. **No animal model, no cell line, no organoid.** The key untried experiment is lineage-restricted *Hras* p.G13R activation in neural crest.
3. **Is FOXO1-rearranged "ectomesenchymoma" the same disease?** (§4.4) — this has treatment consequences and is actively disputed.
4. **Why does RAS-mutation frequency differ so much between series** (86% vs 18%)? Case definition, assay sensitivity, or real biology?
5. **No MEK or other RAS-pathway inhibitor has been reported in an EMS patient**, despite a near-universal RAS driver.
6. **No quality-of-life, disability, or survivorship data** specific to EMS.
7. **No population-based incidence figure**; the EpSSG 0.8% denominator needs verification from the full text.
8. **Placement of ectomesenchymoma in WHO STB6 (2026) is unconfirmed** — check the printed volume.
9. **No proteomic, metabolomic, single-cell or spatial data** exists for this tumour.

---

**Sources:**
- [Frequent HRAS Mutations in Malignant Ectomesenchymoma (PMC4905780)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4905780/)
- [Somatic and mosaic HRAS mutations in pediatric malignant ectomesenchymoma](https://pubmed.ncbi.nlm.nih.gov/40629179/)
- [Malignant ectomesenchymoma in children: EpSSG experience](https://pubmed.ncbi.nlm.nih.gov/36440693)
- [Malignant ectomesenchymoma in children and adolescents: CWS report](https://pubmed.ncbi.nlm.nih.gov/22535600/)
- [A single-center retrospective study of malignant ectomesenchymoma in children (JJCO)](https://academic.oup.com/jjco/article/55/6/621/8113027)
- [An integrative morpho-molecular approach in malignant ectomesenchymoma diagnosis (PMC10940369)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10940369/)
- [Clinicopathological observation of adult malignant ectodermal mesenchymoma (PMC12746915)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12746915/)
- [Metastatic Malignant Ectomesenchymoma Initially Presenting as a Pelvic Mass (PMC4227373)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4227373/)
- [Congenital Malignant Ectomesenchymoma Presenting as a Neck Mass in a Newborn](https://doi.org/10.3390/children12040480)
- [NF1-Driven Rhabdomyosarcoma Phenotypes (JCO Precision Oncology)](https://doi.org/10.1200/po.23.00597)
- [Case Report: Sequential postzygotic HRAS mutation and gains of the paternal chromosome 11](https://doi.org/10.3389/fgene.2023.1231434)
- [Loss of Nf1 and Ink4a/Arf in a Mouse Model of Embryonal Rhabdomyosarcoma (PMC9955904)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9955904/)
- [MyoD-Cre K-Ras/p53 mouse model of rhabdomyosarcoma (PMC8844455)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8844455/)
- [Childhood Soft Tissue Sarcoma Treatment (PDQ®) — NCI](https://www.cancer.gov/types/soft-tissue-sarcoma/hp/child-soft-tissue-treatment-pdq)
- [WHO classification of soft tissue tumours 2020: an update for radiologists](https://www.sciencedirect.com/science/article/pii/S0720048X21004186)
- [Pathology Outlines — Ectomesenchymoma](https://www.pathologyoutlines.com/topic/softtissueectomes.html)
- [Clinicopathologic Study of Ectomesenchymomas from IRS Groups III and IV](https://link.springer.com/article/10.1007/s100249910039)
- [Malignant ectomesenchymoma — Wikipedia](https://en.wikipedia.org/wiki/Malignant_ectomesenchymoma)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 67 |
| Resolved | 66 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 66 |
| On topic | 32 |
| Off topic | 2 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.3760/cma.j.cn112151-20260315-00174` (1 mention) - Identifier did not resolve to a record

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:41317384` (1 mention) - CanID: A Robust and Accurate RNA-seq Expression-based Diagnostic Classification Scheme for Pediatric Malignancies.
  - shared terms: tumor
- `PMID:40979140` (1 mention) - Exploring the Diagnostic and Theranostic Role of FAPI PET in Soft Tissue Sarcoma: A Systematic Review.
  - shared terms: tumor

Weighed against this report's own most characteristic terms: `ems`, `exact`, `rhabdomyosarcoma`, `cell`, `component`, `ectomesenchymoma`, `tumour`, `hras`, `rms`, `tumor`, `differentiation`, `malignant`, `serie`, `mutation`, `phenotype`, `neuroectodermal`, `neural`, `erms`, `adult`, `neuroblastoma`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 49 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 32 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 19 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0002855` (4 mentions) - the report calls it "MONDO", "disease_term"; MONDO calls it **ectomesenchymoma**
- `NCIT:C4716` (3 mentions) - the report calls it "NCIT", "cross-ref"; NCIT calls it **Ectomesenchymoma**
- `NCIT:C188984` (1 mention) - the report calls it "NCIT (paediatric)"; NCIT calls it **Childhood Ectomesenchymoma**
- `NCIT:C173815` (1 mention) - the report calls it "NCIT (recurrent)"; NCIT calls it **Recurrent Ectomesenchymoma**
- `DOID:4055` (1 mention) - the report calls it "DOID"; DOID calls it **ectomesenchymoma**
- `HP:0031500` (2 mentions) - the report calls it "phenotype"; HP calls it **Abdominal mass**
- `HP:0002859` (2 mentions) - the report calls it "phenotype"; HP calls it **Rhabdomyosarcoma**
- `HP:0006743` (2 mentions) - the report calls it "phenotype"; HP calls it **Embryonal rhabdomyosarcoma**
- `HP:0006779` (2 mentions) - the report calls it "phenotype"; HP calls it **Alveolar rhabdomyosarcoma**
- `HP:0500092` (2 mentions) - the report calls it "phenotype"; HP calls it **Orbital rhabdomyosarcoma**
- `HP:0004376` (3 mentions) - the report calls it "phenotype"; HP calls it **Neuroblastic tumor**
- `GO:0007265` (2 mentions) - the report calls it "biological process"; GO calls it **Ras protein signal transduction**
- `GO:0046579` (2 mentions) - the report calls it "biological process"; GO calls it **positive regulation of Ras protein signal transduction**
- `GO:0035914` (2 mentions) - the report calls it "biological process"; GO calls it **skeletal muscle cell differentiation**
- `CL:0000056` (3 mentions) - the report calls it "cell type"; CL calls it **myoblast**
- `GO:0001755` (2 mentions) - the report calls it "biological process"; GO calls it **neural crest cell migration**
- `CL:0000333` (4 mentions) - the report calls it "cell type"; CL calls it **migratory neural crest cell**
- `CL:0002573` (3 mentions) - the report calls it "cell type"; CL calls it **Schwann cell**
- `CL:0011103` (3 mentions) - the report calls it "cell type"; CL calls it **sympathetic neuron**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `RO:0004003` (1 mention) - RO does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001442` (3 mentions) - the report calls it "inheritance (mosaic arm)"; HP calls it **Typified by somatic mosaicism**, and lists "Somatic mosaicism" among its other names
- `HP:0000520` (2 mentions) - the report calls it "phenotype"; HP calls it **Proptosis**, and lists "Prominent eyes" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0002855` - called "MONDO", "disease_term"
- `NCIT:C4716` - called "NCIT", "cross-ref"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ICDO`, `ORPHA`.