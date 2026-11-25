---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5
cached: false
start_time: '2026-11-20T17:39:50.311470'
end_time: '2026-11-20T17:49:29.253713'
duration_seconds: 578.94
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Neurodevelopmental Disorder Nonprogressive With Spasticity And Transient
    Opisthotonus
  mondo_id: MONDO:0859212
  category: Mendelian
  causal_genes: TNR
  omim_id: OMIM:619653
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
  web_search_requests: 9
  num_turns: 27
  total_cost_usd: 3.1467650950000006
  session_id: 5ece72e7-bcfa-4dfb-87df-0d77766e18dc
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  tool_calls: 61
  retrieval_calls: 58
  assistant_text_blocks: 11
citation_count: 38
reference_validation:
  total_references: 41
  verified: 41
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 41
  on_topic: 9
  validator_version: 0.8.0
term_validation:
  total_terms: 69
  verified: 52
  not_found: 1
  obsolete: 0
  unverifiable: 16
  confabulation_rate: 0.019
  labels_checked: 28
  labels_matching: 0
  labels_mismatched: 25
  mislabelled_terms:
  - term_id: MONDO:0859212
    reported_labels:
    - HTTP 200, JSON
    ontology_label: neurodevelopmental disorder, nonprogressive, with spasticity and
      transient opisthotonus
  - term_id: HP:0000514
    reported_labels:
    - Eye
    ontology_label: Slow saccadic eye movements
  - term_id: HP:0008959
    reported_labels:
    - Limbs
    ontology_label: Distal upper limb muscle weakness
  - term_id: HP:0007149
    reported_labels:
    - Limbs
    ontology_label: Distal upper limb amyotrophy
  - term_id: HP:0001347
    reported_labels:
    - Nervous System
    ontology_label: Hyperreflexia
  - term_id: HP:0002395
    reported_labels:
    - Nervous System
    ontology_label: Lower limb hyperreflexia
  - term_id: HP:0007305
    reported_labels:
    - Nervous System
    - CNS demyelination
    ontology_label: CNS demyelination
  - term_id: HP:0001300
    reported_labels:
    - Nervous System
    ontology_label: Parkinsonism
  - term_id: HP:0002188
    reported_labels:
    - Nervous System
    ontology_label: Delayed CNS myelination
  - term_id: HP:0007325
    reported_labels:
    - Nervous System
    ontology_label: Generalized dystonia
  - term_id: HP:0001332
    reported_labels:
    - Nervous System
    ontology_label: Dystonia
  - term_id: HP:0033725
    reported_labels:
    - Nervous System
    ontology_label: Thin corpus callosum
  - term_id: HP:0001263
    reported_labels:
    - Nervous System
    ontology_label: Global developmental delay
  - term_id: HP:0001270
    reported_labels:
    - Nervous System
    ontology_label: Motor delay
  - term_id: HP:0001266
    reported_labels:
    - Nervous System
    ontology_label: Choreoathetosis
  - term_id: HP:0000750
    reported_labels:
    - Nervous System
    ontology_label: Delayed speech and language development
  - term_id: HP:0001338
    reported_labels:
    - Nervous System
    ontology_label: Partial agenesis of the corpus callosum
  - term_id: HP:0007350
    reported_labels:
    - Nervous System
    ontology_label: Upper limb hyperreflexia
  - term_id: HP:0002540
    reported_labels:
    - Nervous System
    ontology_label: Inability to walk
  - term_id: HP:0002186
    reported_labels:
    - Nervous System
    ontology_label: Apraxia
  - term_id: HP:0001260
    reported_labels:
    - Nervous System
    ontology_label: Dysarthria
  - term_id: HP:0002179
    reported_labels:
    - Musculature
    - HTTP 200, JSON
    ontology_label: Opisthotonus
  - term_id: HP:0008936
    reported_labels:
    - Musculature
    ontology_label: Axial hypotonia
  - term_id: HP:0001285
    reported_labels:
    - Musculature
    ontology_label: Spastic tetraparesis
  - term_id: HP:0002375
    reported_labels:
    - hypokinesia; ID **not retrieved this session
    ontology_label: Hypokinesia
  labels_variant: 3
  unresolved_terms:
  - RO:0004003
  unresolvable_prefixes:
  - MIM
  - OMIM
  - MGI
  - PubMed
  - NCBIGene
  - UMLS
  - Chr1
  service_unreachable: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder Nonprogressive With Spasticity And Transient Opisthotonus
- **MONDO ID:** MONDO:0859212 (if available)
- **Causal gene(s):** TNR
- **OMIM:** OMIM:619653
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder Nonprogressive With Spasticity And Transient Opisthotonus** covering all of the
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

Neither OMIM page could be read. Both fetches returned HTTP 403 Forbidden, so I have no content from either entry.

1. https://omim.org/entry/619653 (NEDSTO): HTTP 403 Forbidden. The response body was not retrieved.
2. https://omim.org/entry/601995 (TNR): HTTP 403 Forbidden. The response body was not retrieved.

The 403 is a permanent refusal from omim.org, so retrying these URLs or trying variants of them would fail the same way. Because both failed, there is no partial result for either page. I have not filled any section from memory.

To get the data, you could:
- Paste the page text or the relevant sections here, and I can organize it into the format you asked for.
- Use the OMIM API with your own API key, if you have one. I have not tried it, since it needs credentials and is outside what you asked me to fetch.

I could not extract the paper's content. The PDF loaded (HTTP 200, application/pdf, about 272 KB), but WebFetch returned raw compressed PDF data (FlateDecode streams and object headers) rather than readable text. The first 39,903 of 263,887 characters were unreadable, and the remainder was summarized by a model that also found no readable text. Nothing below comes from the paper.

**Status by requested item:**
1. Citation: not extracted.
2. Abstract: not extracted.
3. Cohort: not extracted.
4. TNR variants: not extracted.
5. Phenotype table: not extracted.
6. Functional work and mechanism: not extracted.
7. Treatment and outcome: not extracted.
8. Differential diagnosis: not extracted.

The fetch tool also reported that the binary PDF was saved to a local file. I can't read that file with my tools, and I have not fetched the URL again, since a retry would return the same compressed data.

**Next steps:**
- Run `pdftotext -layout` on the locally saved PDF. The harness will tell you where it is. Tables such as the phenotype counts usually come through better with `-layout`. If it returns nothing, the PDF may be image-only, so rasterize the pages and OCR them.
- Or send me the article's text from the UCL Discovery landing page or the journal's HTML version. I can then do the full extraction, keeping quotes within the reporting limits.

Neither page yielded its content, so I have nothing to report on the paper itself.

**1. PubMed (https://pubmed.ncbi.nlm.nih.gov/41233622/)**
- The fetch returned HTTP 203 with a "Cookies must be enabled" interstitial (about 249 characters), not the article record.
- The page says cookies must be enabled to continue. WebFetch cannot supply cookies, so I did not try to work around this.
- Not obtained: title, citation, DOI, PMID confirmation, authors, abstract, keywords/MeSH, dates, TNR variants, ancestry, clinical features, and penetrance/expressivity/functional statements.

**2. Nature (https://www.nature.com/articles/s10038-025-01431-0)**
- The server answered HTTP 303 See Other with a redirect to an identity-provider login URL on a different host: https://idp.nature.com/authorize?response_type=cookie&client_id=grover&redirect_uri=https%3A%2F%2Fwww.nature.com%2Farticles%2Fs10038-025-01431-0
- That is a cookie/authorization step, not the article, so I did not follow it.
- Not obtained: any of the article content or metadata. I cannot tell from this whether the article is paywalled or only gated by the cookie check.

**Options**
- Retrieve the PubMed page and the Nature article in a browser with cookies enabled and paste the abstract and metadata here, or
- Use an authenticated route. The `gh` CLI does not cover these sites. A PubMed E-utilities query (efetch for PMID 41233622) may return the citation and abstract without the cookie interstitial, but I have not tried it because it would be a different endpoint from the one you specified.

I did not fill any gaps from memory.

**Results: 1 of 3 pages returned usable content.** Monarch rendered empty and the HPO page returned 404.

### 1. ClinGen, https://search.clinicalgenome.org/kb/genes/HGNC:11953 (HTTP 200, read)

**Gene-disease validity: one assertion**
- Disease: "neurodevelopmental disorder, nonprogressive, with spasticity and transient opisthotonus"
- MONDO: MONDO:0859212
- Classification: Definitive
- Expert panel: Cerebral Palsy GCEP (https://clinicalgenome.org/affiliation/40113)
- Mode of inheritance: AR
- Report date: 01/02/2025
- Assertion link: /kb/gene-validity/CGGV:assertion_fe529d03-c7e4-4638-8ce5-de4400a34fb0-2025-01-02T170000.000Z
- Lumping and splitting: included MIM:619653 ("Neurodevelopmental disorder, nonprogressive, with spasticity and transient opisthotonus"). No excluded MIM phenotypes. Evaluation date 11/18/2024.
- No PMIDs, rationales, or notes are listed. The "Other Stuff" field contains placeholder text ("Lorem Epsum").

**Other curation types: none.** The page summary counts are:
- Dosage sensitivity classifications: 0
- Clinical actionability assertions: 0
- Variant pathogenicity assertions: 0
- CPIC/PharmGKB records: 0/0

**Other gene facts shown (not ClinGen curations):**
- GenCC classifications: Definitive (1) and Strong (2)
- %HI: 5.9 (DECIPHER)
- pLI: 1; LOEUF: 0.37 (gnomAD v4.0, ENST00000367674)
- ACMG SF v3.2: No
- MANE Select: NM_003285.3 / ENST00000367674.7
- Location: 1q25.1; GRCh38 chr1:175315194-175743595

### 2. Monarch, https://monarchinitiative.org/HGNC:11953 (HTTP 200, empty)

The response is 28 characters: only the text "Monarch Initiative". It is a JavaScript app shell with no disease or HPO content, so I have no disease associations or HP IDs from this page.

### 3. HPO, https://hpo.jax.org/browse/disease/OMIM:619653 (HTTP 404, not read)

The server returned HTTP 404 Not Found, so I have no HPO annotations for OMIM:619653. This is a permanent error, so sending the URL again would fail the same way. I did not try a variant URL.

None of the three pages returned any gene or protein data, so I have nothing to report for the TNR gene, the tenascin-R protein, or the gnomAD constraint metrics.

1. **NCBI Gene 7143** (https://www.ncbi.nlm.nih.gov/gene/7143): HTTP 200, but the response is a reCAPTCHA browser-check interstitial ("Checking your browser before accessing www.ncbi.nlm.nih.gov"), not the gene record. I did not try to get past the challenge. Fetching it again would likely hit the same check.

2. **UniProt Q92752** (https://www.uniprot.org/uniprotkb/Q92752/entry): HTTP 200, but the response is UniProt's generic "website fallback message" page, which is a JavaScript-app fallback with no entry data. Nothing from the entry (name, length, domains, GO terms, and so on) was returned.

3. **gnomAD ENSG00000116147** (https://gnomad.broadinstitute.org/gene/ENSG00000116147): HTTP 200, but the body is just the word "gnomAD" (6 characters). This is a JavaScript shell, so no constraint metrics (pLI, LOEUF, o/e values, LoF counts, homozygous LoF) were rendered.

Because these failures are permanent for this fetch path, re-sending the same URLs would return the same results. To get the data, the caller would need a source that serves the content without JavaScript or a browser check. Options include the NCBI E-utilities or Datasets API, the UniProt REST endpoint (rest.uniprot.org), and the gnomAD GraphQL API. I have not tried any of these.

The MGI ID you gave is not tenascin-R. MGI:98501 is **Tcd3** (t-complex distorter 3), so the pages I read are about a different gene. I did not look up the correct Tnr ID, since that would mean guessing a URL. If you send me the correct MGI accession for mouse Tnr, I can fetch the same three pages for it.

**1. https://www.informatics.jax.org/marker/MGI:98501 (HTTP 200, read in full)**
- Symbol: Tcd3. Name: "t-complex distorter 3". Synonyms: Tcd-3, tcs-3, tcs3. Feature type: "unclassified gene".
- MGI accession: MGI:98501.
- NCBI Gene ID: 109870.
- Location: "Chromosome 17, Syntenic" (genetic map). The page says "Genome coordinates not available from the current reference assembly."
- Alleles: none listed on this page.
- Human ortholog and orthology assertion: not shown on this page.
- Phenotype categories and MP: terms: none shown on this page.
- Other accession IDs: MGD-MRK-14739, MGD-MRK-14744, MGD-MRK-14933, MGD-MRK-14936.
- Literature: 9 references. Earliest J:7443 (Lyon MF, 1984). Latest J:28831 (Sowden J, et al., 1995).
- Last database update: 11/10/2026, MGI 6.29.

**2. https://www.informatics.jax.org/allele/summary?markerId=MGI:98501 (HTTP 200, read in full)**
- The page renders only the search header with the single marker row "Tcd3 / t-complex distorter 3 / MGI:98501". It lists no alleles, so there are no knockout or other allele symbols or types to report.

**3. https://www.alliancegenome.org/gene/MGI:98501 (HTTP 200, but empty)**
- The response is a 29-character shell containing only "Alliance of Genome Resources". It has no ortholog, disease, or phenotype data. This is most likely a client-side rendering issue, and fetching it again would likely return the same shell.

All three endpoints returned HTTP 200, so no retries or fallback URL were needed.

**A caveat on verbatim text:** these pages came from non-preapproved sources, so I cannot reproduce the PubMed abstracts or the UniProt FUNCTION prose word for word. Below, the metadata and feature data are complete, the abstracts and prose are paraphrased, and the few quotes are under 125 characters. The JSON from endpoint 3 is reported in full.

## 1. PubMed efetch (PMIDs 41233622, 32066869, 28286006)

Final URL read: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=41233622,32066869,28286006&rettype=abstract&retmode=text

The three PMIDs are unrelated to each other. Only the first concerns TNR.

**PMID 41233622**
- Title: "Biallelic variants in TNR cause neurodevelopmental disorders with variable expressivity."
- Authors: Ozaki A, Sakamoto M, Kumada S, Hamada K, Ogata K, Ikezawa J, Tsuchida N, Uchiyama Y, Koshimizu E, Hamanaka K, Fujita A, Miyatake S, Mizuguchi T, Matsumoto N.
- Journal: J Hum Genet. 2026 Apr;71(4):231-237. Epub 2025 Nov 13.
- Year: 2026 (print); 2025 (epub). Volume 71, issue 4. Pages 231-237.
- DOI: 10.1038/s10038-025-01431-0
- Abstract (paraphrased): The authors describe two Japanese siblings with novel compound heterozygous TNR missense variants, NM_003285.3 c.[1783G>A];[3766C>T], p.(Asp595Asn);(Arg1256Cys). The brother had dystonia. The sister was asymptomatic apart from adult-onset restless legs syndrome. Both had normal development and intellect. Across 15 patients (13 previously reported), phenotypes varied even among people with the same variants, suggesting variable expressivity and reduced penetrance, possibly from genetic or environmental modifiers. The authors call for more cases and functional studies. The abstract frames TNR as essential for perineuronal net formation.
- Conflict of interest: none declared.

**PMID 32066869**
- Title: "Modulation in the elastic properties of gastrocnemius muscle heads in individuals with plantar fasciitis and its relationship with pain."
- Authors: Zhou JP, Yu JF, Feng YN, Liu CL, Su P, Shen SH, Zhang ZJ.
- Journal: Sci Rep. 2020 Feb 17;10(1):2770.
- Year: 2020. Volume 10, issue 1. Article number 2770, so no page range is given.
- DOI: 10.1038/s41598-020-59715-8. PMCID: PMC7026110.
- Abstract (paraphrased): Forty patients were studied with shear-wave elastography. Passive stiffness was higher in the medial gastrocnemius of patients with plantar fasciitis, but not the lateral head, at a relaxed ankle. Medial gastrocnemius stiffness correlated with pain, and plantar fascia thickness did not. The initial cut-off for medial stiffness was 29.08 kPa at a relaxed ankle. The authors conclude that the gastrocnemius heads do not stiffen uniformly.
- Conflict of interest: none declared.

**PMID 28286006**
- Title: "It's Not Just the Pills: A Qualitative Meta-Synthesis of HIV Antiretroviral Adherence Research."
- Authors: Barroso J, Leblanc NM, Flores D.
- Journal: J Assoc Nurses AIDS Care. 2017 Jul-Aug;28(4):462-478. Epub 2017 Feb 22.
- Year: 2017. Volume 28, issue 4. Pages 462-478.
- DOI: 10.1016/j.jana.2017.02.007. No PMCID listed.
- Abstract (paraphrased): A qualitative meta-synthesis of 127 studies on starting and staying on antiretroviral therapy until viral suppression. The authors argue that adherence guidelines rely too heavily on quantitative work and focus too narrowly on the individual. They propose including patients' wider communities, addressing systemic disparities, and demedicalizing care for healthy people living with HIV. The analysis uses Maslow's hierarchy of needs.

## 2. UniProt Q92752 (flat file)

Final URL read: https://rest.uniprot.org/uniprotkb/Q92752.txt

- Entry: TENR_HUMAN, reviewed (Swiss-Prot), entry version 206, sequence version 3.
- Protein name: Tenascin-R (short name TN-R). Alternative names: Janusin, Restrictin. Flagged as a precursor.
- Length: 1358 aa. Mass 149,562 Da. Signal peptide at residues 1-31.
- Gene: TNR (HGNC:11953). The GN line lists only "Name=TNR" and gives no synonyms.
- FUNCTION (paraphrased): A neural extracellular matrix protein that interacts with cells and matrix components. Depending on context, it either promotes stable adhesion and differentiation or repels cells and inhibits neurite growth. Binding cell-surface gangliosides inhibits RGD-dependent integrin adhesion and FAK phosphorylation. Binding sulfatides promotes oligodendrocyte adhesion and differentiation. Interaction with CNTN1 causes neuron repulsion. Interaction with SCN2B may help cluster sodium channels at nodes of Ranvier. The annotation is by similarity. A short verbatim opening: "Neural extracellular matrix (ECM) protein involved in interactions with different cells and matrix components."
- SUBCELLULAR LOCATION: Secreted, extracellular space, extracellular matrix.
- TISSUE SPECIFICITY: Brain specific (PubMed:8626505).
- DISEASE: NEDSTO (MIM:619653), an autosomal recessive neurodevelopmental disorder with delayed motor milestones, speech delay, axial hypotonia, peripheral spasticity, and transient opisthotonic posturing. Note that the disease comment is paraphrased.
- Glycosylation (from feature table and PTM comment):
  - O-linked GalNAc threonine at Thr36 and Thr37 (evidence PubMed:19838169).
  - N-linked GlcNAc asparagine at 12 sites: 55, 180, 198, 278, 392, 470, 581, 791, 874, 1036, 1046, 1261.
  - O-linked chondroitin sulfate serine at 3 sites: 176, 271, 302.
  - Also a phosphoserine at 724.
- Domain features (FT DOMAIN, residue ranges):
  - EGF-like 1: 188-199
  - EGF-like 2: 219-230
  - EGF-like 3: 250-261
  - EGF-like 4: 281-292
  - EGF-like 5: 312-323
  - Fibronectin type-III 1: 328-420
  - Fibronectin type-III 2: 421-505
  - Fibronectin type-III 3: 506-595
  - Fibronectin type-III 4: 596-687
  - Fibronectin type-III 5: 688-777
  - Fibronectin type-III 6: 778-865
  - Fibronectin type-III 7: 866-955
  - Fibronectin type-III 8: 956-1042
  - Fibronectin type-III 9: 1043-1130
  - Fibrinogen C-terminal: 1129-1344
- REPEAT features: none in this record.
- Other features: coiled-coil region 127-157; disulfide bonds 292-301, 297-312, 314-323.
- GO terms (11 in total, none in molecular function):
  - GO:0031012 extracellular matrix (cellular component; IBA:GO_Central)
  - GO:0005576 extracellular region (cellular component; TAS:Reactome)
  - GO:0072534 perineuronal net (cellular component; IEA:Ensembl)
  - GO:0090733 tenascin complex (cellular component; TAS:GO_Central)
  - GO:0007411 axon guidance (biological process; NAS:ProtInc)
  - GO:0007155 cell adhesion (biological process; NAS:ProtInc)
  - GO:0010977 negative regulation of neuron projection development (IEA:Ensembl)
  - GO:0007399 nervous system development (IBA:GO_Central)
  - GO:0030155 regulation of cell adhesion (IEA:Ensembl)
  - GO:0045595 regulation of cell differentiation (IEA:Ensembl)
  - GO:0030334 regulation of cell migration (IEA:Ensembl)
- Sequence: 1358 aa, CRC64 E4DE356B44D117E7. I have not reproduced the residue sequence.

## 3. HPO network annotation, OMIM:619653

Final URL read: https://ontology.jax.org/api/network/annotation/OMIM:619653

Endpoint 3 returned HTTP 200 (application/json), so the fallback at hpo.jax.org was not needed and was not fetched.

- Disease: OMIM:619653, "Neurodevelopmental disorder, nonprogressive, with spasticity and transient opisthotonus". MONDO:0859212. Description field empty.
- Gene: NCBIGene:7143, TNR.
- Medical actions: none.
- The JSON contains 26 HPO terms. Every onset field is an empty string. Frequency is given as a fraction, and it is the only metadata provided. Sources are PMID:28334938 and PMID:32099069.

| Category | HP ID | Term | Frequency | Source |
|---|---|---|---|---|
| Eye | HP:0000514 | Slow saccadic eye movements | 1/1 | PMID:28334938 |
| Limbs | HP:0008959 | Distal upper limb muscle weakness | 1/1 | PMID:28334938 |
| Limbs | HP:0007149 | Distal upper limb amyotrophy | 1/1 | PMID:28334938 |
| Clinical course | HP:0003593 | Infantile onset | (none) | PMID:32099069 |
| Nervous System | HP:0001347 | Hyperreflexia | 1/1 | PMID:28334938 |
| Nervous System | HP:0002395 | Lower limb hyperreflexia | 10/12 | PMID:32099069 |
| Nervous System | HP:0007305 | CNS demyelination | 1/1 | PMID:28334938 |
| Nervous System | HP:0001300 | Parkinsonism | (none) | PMID:32099069 |
| Nervous System | HP:0002188 | Delayed CNS myelination | 4/11 | PMID:32099069 |
| Nervous System | HP:0007325 | Generalized dystonia | 1/1 | PMID:28334938 |
| Nervous System | HP:0001332 | Dystonia | 7/13 | PMID:32099069 |
| Nervous System | HP:0033725 | Thin corpus callosum | 1/11 | PMID:32099069 |
| Nervous System | HP:0001263 | Global developmental delay | 7/11 | PMID:32099069 |
| Nervous System | HP:0001270 | Motor delay | 13/13 | PMID:32099069 |
| Nervous System | HP:0001266 | Choreoathetosis | 11/11 | PMID:32099069, PMID:28334938 |
| Nervous System | HP:0000750 | Delayed speech and language development | 12/13 | PMID:32099069 |
| Nervous System | HP:0001338 | Partial agenesis of the corpus callosum | 1/11 | PMID:32099069 |
| Nervous System | HP:0007350 | Upper limb hyperreflexia | 7/12 | PMID:32099069 |
| Nervous System | HP:0002540 | Inability to walk | 1/1 | PMID:28334938 |
| Nervous System | HP:0002186 | Apraxia | 7/13 | PMID:32099069 |
| Nervous System | HP:0001260 | Dysarthria | 1/1 | PMID:28334938 |
| Inheritance | HP:0000007 | Autosomal recessive inheritance | (none) | PMID:28334938 |
| Musculature | HP:0002179 | Opisthotonus | 6/12 | PMID:32099069, PMID:28334938 |
| Musculature | HP:0008936 | Axial hypotonia | 8/12 | PMID:32099069 |
| Musculature | HP:0001257 | Spasticity | 11/13 | PMID:32099069, PMID:28334938 |
| Musculature | HP:0001285 | Spastic tetraparesis | 1/1 | PMID:28334938 |

Category counts: Eye 1, Limbs 2, Clinical course 1, Nervous System 17, Inheritance 1, Musculature 4.

Final URLs read:
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=41233622,32066869,28286006&rettype=abstract&retmode=text
- https://rest.uniprot.org/uniprotkb/Q92752.txt
- https://ontology.jax.org/api/network/annotation/OMIM:619653

**Endpoints 2 and 3 failed, so the phenotype and gene lists are not available.** Both returned HTTP 422 (Unprocessable Entity), not 404. I did not try the fallback `/v3/api/association` URL, because your instruction was conditioned on a 404 and I should not try variants of a failed URL. I can try it if you want. A 422 is a client-side rejection, so resending the same URLs will likely fail the same way.

**1. Disease record: https://api.monarchinitiative.org/v3/api/entity/MONDO:0859212 (HTTP 200, JSON)**

- **id:** MONDO:0859212
- **category:** biolink:Disease
- **name:** "neurodevelopmental disorder, nonprogressive, with spasticity and transient opisthotonus"
- **description:** null
- **synonyms** (all synonym fields): null
- **xref / mappings:** MEDGEN:1794250, OMIM:619653, UMLS:C5562040 (no DOID, Orphanet, or other mappings present)
- **inheritance:** HP:0000007, "Autosomal recessive inheritance"
- **causal_gene:** HGNC:11953, "TNR"
- **node_relationships:** RO:0004003 ("has material basis in germline mutation in") → HGNC:11953 TNR (in_taxon NCBITaxon:9606, Homo sapiens)
- **node_hierarchy superclass:** MONDO:0100500, "Mendelian neurodevelopmental disorder" (no subclasses)
- **association_counts:** Disease to Phenotype 24; Gene to Phenotype 26; Causal Gene 1
- **provided_by:** phenio (phenio_nodes)
- **uri:** http://purl.obolibrary.org/obo/MONDO_0859212
- **has_phenotype_count:** 24. The record includes two separate 24-item lists, `has_phenotype` (HP IDs) and `has_phenotype_label` (labels), plus a large `has_phenotype_closure` list. The record does not pair IDs with labels. I could not match them by position: HP:0002179 is the first ID, but "Opisthotonus" is the 7th label. Per endpoint 4, HP:0002179 is Opisthotonus, so the two lists are not aligned. The HP IDs in `has_phenotype`, in order, are: HP:0002179, HP:0001266, HP:0002186, HP:0001263, HP:0002395, HP:0001332, HP:0008936, HP:0001338, HP:0001300, HP:0001260, HP:0000750, HP:0008959, HP:0002540, HP:0007325, HP:0000514, HP:0007305, HP:0002188, HP:0001285, HP:0007149, HP:0033725, HP:0001257, HP:0001347, HP:0001270, HP:0007350.
- **has_phenotype_label** (in record order): Slow saccadic eye movements; Lower limb hyperreflexia; Dystonia; Partial agenesis of the corpus callosum; Upper limb hyperreflexia; Distal upper limb muscle weakness; Opisthotonus; Delayed CNS myelination; Dysarthria; Thin corpus callosum; Spastic tetraparesis; Delayed speech and language development; CNS demyelination; Inability to walk; Spasticity; Generalized dystonia; Choreoathetosis; Axial hypotonia; Parkinsonism; Hyperreflexia; Apraxia; Motor delay; Global developmental delay; Distal upper limb amyotrophy.
- **Not in the record:** per-association frequency, onset, qualifiers, evidence, or publication references. Those would come from endpoint 2.

**2. Disease-to-phenotype (endpoint 2): HTTP 422.** Not read.

**3. Disease-to-gene (endpoint 3): HTTP 422.** Not read. The disease record itself names TNR as the causal gene (see above).

**4. HP term: https://ontology.jax.org/api/hp/terms/HP:0002179 (HTTP 200, JSON)**

- **id:** HP:0002179
- **name:** Opisthotonus
- Synonyms: "Arc de cercle", "Opisthotonos"
- publicationReferences: PMID:29972427

The API form works.

## 1. PubMed efetch (PMIDs 32099069, 28334938)

**PMID 32099069**
- **Title:** "Loss of TNR causes a nonprogressive neurodevelopmental disorder with spasticity and transient opisthotonus."
- **Authors (32):** Wagner M, Lévy J, Jung-Klawitter S, Bakhtiari S, Monteiro F, Maroofian R, Bierhals T, Hempel M, Elmaleh-Bergès M, Kitajima JP, Kim CA, Salomao JG, Amor DJ, Cooper MS, Perrin L, Pipiras E, Neu A, Doosti M, Karimiani EG, Toosi MB, Houlden H, Jin SC, Si YC, Rodan LH, Venselaar H, Kruer MC, Kok F, Hoffmann GF, Strom TM, Wortmann SB, Tabet AC, Opladen T. (Wagner M, Lévy J, Jung-Klawitter S, Tabet AC and Opladen T contributed equally.)
- **Journal:** Genetics in Medicine (Genet Med)
- **Year:** 2020 (Epub 26 Feb 2020)
- **Volume / issue / pages:** 22(6) / 1061-1068
- **DOI:** 10.1038/s41436-020-0768-7
- **Abstract (paraphrased):** Tenascin-R (TNR) is an extracellular matrix glycoprotein that is expressed only in the CNS and helps form perineuronal nets. Its role in human disease was unknown. The authors used exome sequencing and a matchmaking tool to find patients with biallelic TNR variants. They identified 13 individuals from 8 unrelated families with spastic para- or tetraparesis, axial hypotonia, developmental delay and transient opisthotonus. The variants were four homozygous loss-of-function variants and four different missense variants. They conclude that TNR is a disease gene for an autosomal recessive nonprogressive neurodevelopmental disorder with spasticity and transient opisthotonus.

**PMID 28334938**
- **Title:** "Clinical and genetic characterization of leukoencephalopathies in adults."
- **Authors (29):** Lynch DS, Rodrigues Brandão de Paiva A, Zhang WJ, Bugiardini E, Freua F, Tavares Lucato L, Macedo-Souza LI, Lakshmanan R, Kinsella JA, Merwick A, Rossor AM, Bajaj N, Herron B, McMonagle P, Morrison PJ, Hughes D, Pittman A, Laurà M, Reilly MM, Warren JD, Mummery CJ, Schott JM, Adams M, Fox NC, Murphy E, Davagnanam I, Kok F, Chataway J, Houlden H.
- **Journal:** Brain
- **Year:** 2017
- **Volume / issue / pages:** 140(5) / 1204-1211
- **DOI:** 10.1093/brain/awx045 (PMCID: PMC5405235)
- **Abstract (paraphrased):** Exome sequencing was used on 100 adults with undiagnosed leukoencephalopathy. Pathogenic or likely pathogenic variants were found in 26 cases, most often in NOTCH3, EIF2B5, AARS2 and CSF1R. Whole-exome sequencing of the negative cases, including four trios, found no further candidates. The authors conclude that focused and whole-exome sequencing are equivalent for diagnosing these disorders.

This paper does not concern TNR.

## 2. PubMed esearch, then the deletion paper

- **esearch** (`term=Dufresne+AND+tenascin-R+AND+deletion`): HTTP 200 on the second attempt. The first attempt returned HTTP 429 with Retry-After: 2. Result: count 1, retmax 1, retstart 0, idlist **["22730557"]**.
- **efetch** for 22730557: HTTP 200 on the second attempt. The first attempt returned HTTP 429 with Retry-After: 2.
  - **Title:** "Homozygous deletion of Tenascin-R in a patient with intellectual disability."
  - **Authors:** Dufresne D, Hamdan FF, Rosenfeld JA, Torchia B, Rosenblatt B, Michaud JL, Srour M.
  - **Journal:** J Med Genet
  - **Year:** 2012 (Epub 22 Jun 2012)
  - **Volume / issue / pages:** 49(7) / 451-4
  - **DOI:** 10.1136/jmedgenet-2012-100831 (PMCID: PMC3395313)
  - **Abstract (paraphrased):** A child with intellectual disability and transient choreoathetosis had a homozygous deletion of only two genes, one of them TNR, found by array genomic hybridisation. Sequencing TNR in 219 patients with intellectual disability found no pathogenic mutations. The authors report the first complete loss of TNR associated with intellectual disability and argue for a role for TNR in human brain development and cognition.

## 3. ClinVar esummary (IDs 691951-691958)

HTTP 200. All eight records share the trait "Non-progressive neurodevelopmental disorder with spasticity and transient opisthotonus", gene TNR (GeneID 7143), review status "criteria provided, single submitter", and last evaluated 2019/07/25. The esummary has no explicit submitter-count field. The count below is the number of SCV accessions in `supporting_submissions`.

| Variation ID | VCV accession | Variant name (HGVS) | Germline classification | SCVs | Molecular consequence |
|---|---|---|---|---|---|
| 691951 | VCV000691951.5 | NM_003285.3(TNR):c.2713C>T (p.Arg905Ter) | Pathogenic | 3 | nonsense |
| 691952 | VCV000691952.5 | NM_003285.3(TNR):c.2744_2745del (p.Val915fs) | Pathogenic | 3 | frameshift variant |
| 691953 | VCV000691953.5 | NM_003285.3(TNR):c.3574C>T (p.Arg1192Trp) | Pathogenic | 3 | missense variant |
| 691954 | VCV000691954.4 | NM_003285.3(TNR):c.1899del (p.Glu634fs) | Pathogenic | 2 | frameshift variant |
| 691955 | VCV000691955.4 | NM_003285.3(TNR):c.207C>G (p.Tyr69Ter) | Pathogenic | 2 | 5 prime UTR variant; nonsense |
| 691956 | VCV000691956.4 | NM_003285.3(TNR):c.3357C>G (p.Ser1119Arg) | Uncertain significance | 2 | missense variant |
| 691957 | VCV000691957.4 | NM_003285.3(TNR):c.1594G>A (p.Asp532Asn) | Likely pathogenic | 2 | missense variant |
| 691958 | VCV000691958.4 | NM_003285.3(TNR):c.1189G>A (p.Ala397Thr) | Likely pathogenic | 2 | missense variant |

Notes:
- 691952 has `obj_type` "Microsatellite" and `variant_type` "Microsatellite" in the record, though the title describes a deletion.
- `protein_change` lists more than one isoform for some records, for example "R572*, R905*" for 691951.

## 4. ClinVar esearch (TNR[gene])

HTTP 200. **Total count: 340** ClinVar records for TNR[gene].

## URLs read
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=32099069,28334938&rettype=abstract&retmode=text
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=Dufresne+AND+tenascin-R+AND+deletion&retmode=json
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22730557&rettype=abstract&retmode=text
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=clinvar&id=691951,691952,691953,691954,691955,691956,691957,691958&retmode=json
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=clinvar&term=TNR%5Bgene%5D&retmax=0&retmode=json

## Summary

I could not return full verbatim abstracts. These pages are from a non-preapproved source, so quotes are capped at 125 characters and I paraphrased the rest. All fetches returned HTTP 200. The correct mouse Tnr MGI ID is **MGI:99516**, not the two IDs you suggested.

## 1. Europe PMC: `TNR AND opisthotonus` (hitCount 6, all 6 returned)

1. **PMID 42297634**, PMCID PMC13339114, DOI 10.1002/mdc3.70683
   - Title: "Data-Driven Insights into Hyperkinetic Disorders in Neurodevelopmental Syndromes and Epileptic Encephalopathies."
   - Authors: Morales-Briceño H, Mohammad SS, Angiti RR, Han V, Tchan M, Dale RC, Fung VSC
   - Journal: Movement disorders clinical practice, 2026, vol 13(11), pp 2759-2776
   - isOpenAccess Y, inEPMC Y. License cc by-nc-nd.
   - Abstract: a review of 210 monogenic conditions with hyperkinetic movement disorders. The visible abstract does not mention TNR or tenascin.

2. **PMID 37372119**, PMCID PMC10295065, DOI 10.3390/biology12060834
   - Title: "Bilirubin-Induced Transcriptomic Imprinting in Neonatal Hyperbilirubinemia."
   - Authors: Llido JP, Fioriti E, Pascut D, Giuffrè M, Bottin C, Zanconati F, Tiribelli C, Gazzin S
   - Journal: Biology (Basel), 2023, vol 12(6), 834
   - isOpenAccess Y, inEPMC Y. License cc by.
   - Abstract (paraphrased): rat bilirubin neurotoxicity study with histology, transcriptomics and behavior. Behavioral tests confirmed a permanent motor disability. "Opisthotonus" is an author keyword, which is probably why it matched. No TNR content.

3. **PMID 32099069**, no PMCID, DOI 10.1038/s41436-020-0768-7. This is the only record that is about TNR.
   - Title: "Loss of TNR causes a nonprogressive neurodevelopmental disorder with spasticity and transient opisthotonus."
   - Authors: Wagner M, Lévy J, Jung-Klawitter S, … Opladen T (32 authors)
   - Journal: Genetics in Medicine, 2020, vol 22(6), pp 1061-1068
   - isOpenAccess N, inEPMC N, inPMC N.
   - Abstract (paraphrased): exome sequencing found biallelic TNR variants in 13 people from 8 families. The shared phenotype was spastic para- or tetraparesis, axial hypotonia, developmental delay and transient opisthotonus. Variants were 4 homozygous loss-of-function and 4 missense.

4. **PMID 38003185**, PMCID PMC10668755, DOI 10.3390/ani13223568. Canine inherited neurological disorders review (Cocostîrc V, Paștiu AI, Pusta DL; Animals, 2023). Not relevant. isOpenAccess Y, inEPMC Y.

5. **PMID 33488619**, PMCID PMC7820773, DOI 10.3389/fimmu.2020.612482. "Early Days of Tenascin-R Research: Two Approaches Discovered and Shed Light on Tenascin-R." (Rathjen FG, Hodge R; Frontiers in Immunology, 2020, vol 11, 612482). isOpenAccess Y, inEPMC Y. No abstract field in the record.

6. **PMCID PMC9771678**, no PMID or DOI. The title field is only "T". This is a Saunders Comprehensive Veterinary Dictionary entry (2020, pp 1077-1142). isOpenAccess Y, inEPMC Y. Not relevant.

Next page: nextCursorMark is present. I did not fetch it.

## 2. Europe PMC: `"tenascin-R" AND (knockout OR "deficient mice")` (hitCount 642)

I read the first part of this response verbatim and a later section verbatim. A model-extracted summary stood in for the rest, and I have not verified those records. The full page is not covered. Only the records below are relevant to mouse Tnr knockouts.

- **PMID 39953103**, PMCID PMC11828866, DOI 10.1038/s41598-025-89580-2 (verbatim abstract read). Mueller-Buehl C et al., Scientific Reports, 2025, vol 15(1), 5528. isOpenAccess Y.
  - Fear conditioning in mice lacking brevican, neurocan, tenascin-C and tenascin-R (4x KO) showed impaired fear memory consolidation. These mice could not retrieve learned fear memories, and perineuronal net density was reduced.
  - Quote: "tenascin single KOs showed intact fear behavior and memory". The single tenascin knockouts showed normal fear behavior and memory.
- **PMID 37370243**, PMCID PMC10527205, DOI 10.1002/ana.26730 (verbatim). Yang B et al., Annals of Neurology, 2023, vol 94(3), pp 502-507. Human case report of isolated tremor with anti-tenascin-R autoantibody. isOpenAccess N, but EPMC lists free full text.
- **PMID 40891036**, PMCID PMC12402400 (summary only, unverified). Wang B et al., Alzheimer's & Dementia, 2025. The summary says reducing Tnr in APP/PS1 mice lowered amyloid deposition and improved cognition.
- **PPR645600** (summary only, unverified). A bioRxiv preprint on combined brevican, neurocan, tenascin-C and tenascin-R knockout. The summary reports retinal dysfunction and impaired visual motion processing.
- **PMID 39837996**, PMCID PMC12185343 (summary only, unverified). Aggrecan knockout in PV+ neurons. The summary notes compensatory upregulation of neurocan and tenascin-R.
- Also seen, not relevant to Tnr knockouts: PMID 42610801 (pain ECM review), 42812881 and 41932623 (ECM reviews), 42100732 (CNTN6 review), 42394367 (meprins), 42650857 (bladder cancer review), 39348530 (PTX3 retina, PNAS 2024), 41221587 (hypertensive rat cerebral arteries), 34604231 (Hapln4, Nojima K et al., 2021, verbatim not readable).

## 3. MGI: correct ID and gene details

The search at `featureBucket?queryType=both&query=Tnr` returned this row (HTTP 200, `totalCount` 2):
- Symbol **Tnr**, name "tenascin R", detailUri **/marker/MGI:99516**, chromosome 1, location 159351339-159759299, + strand, protein coding gene, stars ****.
- The second hit is Cftr (MGI:88388), matched through a human synonym.

I did not fetch MGI:98502 or MGI:101922. The search did not return them as Tnr, so I have no evidence for either.

Gene page https://www.informatics.jax.org/marker/MGI:99516 (last database update 11/10/2026, MGI 6.29):
- Symbol Tnr. Name "tenascin R". Synonyms: J1-tenascin, janusin, restrictin, TN-R. NCBI Gene 21960. Ensembl ENSMUSG00000015829.
- Chr1:159351339-159759299 bp, + strand (GRCm39). Genetic map: Chromosome 1, 69.03 cM, cytoband E2.
- Human ortholog TNR (HGNC:11953), 1q25.1.
- Allele counts: All 12. Targeted 4. Endonuclease-mediated 5. Chemically induced (other) 2. Transgenic 1. Genomic mutations 2.
- Phenotype summary text, verbatim: "In spite of having decreased conduction velocity in the optic nerve and ultrastrucural alterations within the hippocampus, homozygous null mice are viable, fertile, and display normal behavior."

Allele list: https://www.informatics.jax.org/allele/summary?markerId=MGI:99516 returned HTTP 200 but no allele rows. Only the header rendered, so I could not list the 12 alleles.

MP annotations: https://www.informatics.jax.org/marker/phenotypes/MGI:99516 shows "11 phenotypes from 2 alleles in 2 genetic backgrounds."

| Allele | Allele ID | MP ID | MP term |
|---|---|---|---|
| Tnrem1(IMPC)Rbrc (homozygous; C57BL/6NJcl background) | MGI:6156164 | MP:0001565 | abnormal circulating phosphate level |
| | | MP:0003313 | abnormal locomotor activation |
| | | MP:0004952 | increased spleen weight |
| Tnrtm1Msch (homozygous; involves 129P2/OlaHsd × C57BL/6J) | MGI:2154583 | MP:0008263 | abnormal hippocampus CA1 region morphology |
| | | MP:0008284 | abnormal hippocampus pyramidal cell layer |
| | | MP:0003632 | abnormal nervous system morphology |
| | | MP:0015052 | abnormal presynaptic active zone morphology |
| | | MP:0009538 | abnormal synapse morphology |
| | | MP:0004769 | abnormal synaptic vesicle morphology |
| | | MP:0008814 | decreased nerve conduction velocity |
| | | MP:0015056 | increased synaptic vesicle number |

The Tnrtm1Msch allele is the one with the neurological phenotypes. Its annotations come from references J:81471 and J:55338. The allele type is not shown on the page, so I cannot confirm it is a targeted knockout from this source. Its "tm1" designation is standard MGI nomenclature for a targeted mutation, but that is my own knowledge, not something the page states.

Pages read: europepmc search 1 (the first URL you gave), europepmc search 2 (first and tail sections), MGI featureBucket search, MGI:99516 gene page, MGI allele summary, MGI MP phenotype page.

**Interpretation note:** This report covers the disease at **MONDO:0859212 / OMIM:619653 (NEDSTO)**, caused by biallelic variants in **TNR** (tenascin-R), per the identifiers supplied. Where I could not retrieve a source in this session, I say so rather than filling the gap. Direct fetches of omim.org returned HTTP 403, so no OMIM text is quoted below; OMIM-derived content appears only where it reached me through MedGen/other retrieved resources, and is labeled as such. The primary source — the full text of Wagner et al. (2020), including Table 1 — was retrieved and read directly (UCL Discovery author-accepted manuscript of the *Genetics in Medicine* paper).

---

# Neurodevelopmental Disorder, Nonprogressive, with Spasticity and Transient Opisthotonus (NEDSTO) — *TNR*

## 1. Disease Information

**Overview.** NEDSTO is an autosomal recessive, **non-progressive** neurodevelopmental disorder caused by biallelic loss-of-function or missense variants in **TNR**, which encodes **tenascin-R**, a CNS-restricted extracellular-matrix (ECM) glycoprotein that cross-links the lectican/hyaluronan lattice of **perineuronal nets**. The core phenotype is delayed motor milestones with **axial hypotonia plus appendicular (peripheral) spasticity** — spastic para- or tetraparesis — accompanied in roughly half of patients by **transient opisthotonic posturing in the first year of life**, variable extrapyramidal features (dystonia, hypokinesia, choreoathetosis, parkinsonism), speech delay, and mild-to-moderate cognitive impairment in a subset. The defining gene-discovery paper states the conclusion directly:

> "Hereby, we establish *TNR* as a disease gene for an autosomal recessive non-progressive neurodevelopmental disorder with spasticity and transient opisthotonus and highlight the role of central nervous system extracellular matrix proteins in the pathogenicity of spastic disorders." — Wagner et al., *Genet Med* 2020;22(6):1061–1068, PMID 32099069, DOI 10.1038/s41436-020-0768-7 ([author manuscript, UCL Discovery](https://discovery.ucl.ac.uk/id/eprint/10094729/1/TNR,%20Wagner,%20M%20et%20al..pdf))

**Pediatric framing.** This is substantively a pediatric entity. Presentation is in infancy/early childhood; the diagnostic context is almost always *investigation of a "cerebral palsy"-like picture* or unexplained global developmental delay. The authors' own keyword list reads "TNR, spastic tetraparesis, **cerebral palsy**, exome sequencing, developmental disorder" — and ClinGen's curation was performed by the **Cerebral Palsy GCEP**, which is the clinically meaningful framing: NEDSTO belongs with the genetic CP mimics, not with the progressive leukodystrophies or classical HSPs.

**Key identifiers** (all retrieved this session unless noted):

| Resource | Identifier | Source |
|---|---|---|
| MONDO | **MONDO:0859212** — "neurodevelopmental disorder, nonprogressive, with spasticity and transient opisthotonus" | [Monarch API entity record](https://api.monarchinitiative.org/v3/api/entity/MONDO:0859212) |
| OMIM | **619653** (NEDSTO) | Monarch xref; [ClinGen](https://search.clinicalgenome.org/kb/genes/HGNC:11953); [HPO annotation API](https://ontology.jax.org/api/network/annotation/OMIM:619653) |
| MedGen | **UID 1794250 / CUI C5562040** | Monarch xref (MEDGEN:1794250, UMLS:C5562040) |
| UMLS | **C5562040** | Monarch xref |
| KEGG DISEASE | **H03007** | [KEGG](https://www.kegg.jp/entry/H03007) (via search result) |
| ICD-11 | **LD20.Y** (as assigned by KEGG's mapping) | KEGG entry, via search result |
| Gene | **TNR**, HGNC:11953, NCBI Gene **7143**, MANE Select **NM_003285.3 / ENST00000367674.7**, protein NP_003276.3 | ClinGen gene page; Wagner et al. used NM_003285.2 |
| UniProt | **Q92752** (TENR_HUMAN) | [UniProt flat file](https://rest.uniprot.org/uniprotkb/Q92752.txt) |
| Cytogenetic locus | **1q25.1**; GRCh38 chr1:175,315,194–175,743,595 | ClinGen gene page |
| MONDO parent class | MONDO:0100500 "Mendelian neurodevelopmental disorder" | Monarch API |

**Synonyms / alternative names** (retrieved): **NEDSTO** (abbreviation used by OMIM/MedGen); "Non-progressive neurodevelopmental disorder with spasticity and transient opisthotonus" (ClinVar condition string; KEGG title). The Monarch record returns `synonyms: null` — no additional synonyms are registered there. **No Orphanet ORPHA code was found** in any retrieved resource, and the Monarch mapping list contains no Orphanet, DOID or MeSH cross-reference; I could not confirm whether an Orphanet entry exists. There is no disease-specific MeSH descriptor.

**Information provenance.** All disease-level knowledge derives from **aggregated case-series literature**, not EHR or registry data: essentially one multicenter case series (n=13, Wagner et al. 2020), two antecedent single-patient reports (Dufresne et al. 2012; Lynch et al. 2017), and one subsequent two-sibling report (Ozaki et al. 2025/2026). Total published individuals ≈ 17.

---

## 2. Etiology

### Disease causal factors
**Monogenic, autosomal recessive.** The causal factor is **biallelic (homozygous or compound heterozygous) pathogenic variation in *TNR***. ClinGen's **Cerebral Palsy GCEP** classified the *TNR* — NEDSTO relationship as **Definitive**, mode of inheritance **AR**, report date **01/02/2025** (assertion CGGV:assertion_fe529d03-c7e4-4638-8ce5-de4400a34fb0-2025-01-02T170000.000Z); the lumping/splitting evaluation (11/18/2024) included MIM:619653 with no excluded MIM phenotypes ([ClinGen](https://search.clinicalgenome.org/kb/genes/HGNC:11953)). The same page records GenCC classifications of Definitive (1) and Strong (2). This is a **structured-database expert-panel assertion** — a materially stronger evidence class than the single case reports that preceded it.

No environmental, infectious, or toxic etiology is implicated. Pregnancy, delivery and postnatal adaptation were explicitly **uneventful in most families** (Wagner et al.), which is the key discriminator from acquired perinatal CP.

### Risk factors
- **Genetic:** Biallelic *TNR* variants are causal, not merely risk-conferring. **Consanguinity is the dominant risk amplifier**: 7 of 8 families in the index cohort were consanguineous (Turkey, Morocco, "Arabian", Iraq, Brazil), with one non-consanguineous Indian family. Heterozygous carriers are unaffected.
- **Carrier/population data:** Wagner et al. state — "Heterozygous LoF variants in *TNR* are rare (40 in > 280 000 alleles) and homozygous variants absent in the gnomAD database, indicating that biallelic pathogenic variants in *TNR* are likely to cause disease." All eight variants were absent in homozygous state from >140,000 gnomAD NGS datasets and absent from the GME Variome and Iranome databases.
- **Environmental risk factors:** None identified in any retrieved source. No toxin, exposure, age, sex, or lifestyle association has been reported.

### Protective factors
No genetic or environmental protective factors have been reported. **gnomAD constraint** indicates *TNR* is strongly LoF-intolerant at the heterozygous level: **pLI = 1; LOEUF = 0.37** (gnomAD v4.0, ENST00000367674), DECIPHER **%HI = 5.9** (reported on the ClinGen gene page). I was unable to fetch gnomAD directly (JavaScript shell), so observed/expected LoF counts and homozygote counts are not reported here.

### Gene–environment interactions
No GxE data exist for this disorder. The only relevant published speculation is from the most recent report: Ozaki et al. observed discordant phenotypes between siblings sharing identical biallelic *TNR* missense variants and raised **variable expressivity and reduced penetrance, "possibly from genetic or environmental modifiers"** (PMID 41233622; *J Hum Genet* 2026;71(4):231–237, epub 2025-11-13, DOI 10.1038/s10038-025-01431-0). That is a hypothesis in a two-person pedigree, not a demonstrated interaction.

---

## 3. Phenotypes

### 3a. Phenotype frequencies from the primary cohort
Two frequency denominators coexist in Wagner et al. and should not be conflated: the **Results text** gives fractions for their own 13 patients (or the subset examined), whereas **Table 1's "All" column pools their 13 patients with the previously published Lynch and Dufresne patients (n=15)**. Both are given below.

| Feature | Table 1 "All" (n≈15 pooled) | Results-text figure (Wagner cohort) | Suggested HPO term |
|---|---|---|---|
| Motor developmental delay | — | **13/13 (100%)** ("motor developmental milestones were delayed in all patients") | HP:0001270 Motor delay *(HPO: 13/13)* |
| Axial hypotonia | **13/15 (87%)** | 8/12 examined (67%) | HP:0008936 Axial hypotonia *(HPO: 8/12)* |
| Spasticity (spastic para-/tetraparesis) | **13/15 (87%)** | 10/12 examined (83%) with "spastic tonus dysregulation of two or four extremities" | HP:0001257 Spasticity *(HPO: 11/13)*; HP:0001285 Spastic tetraparesis |
| Transient opisthotonus | **7/13 (54%)** | **5/11 (45%)** during the first year of life | HP:0002179 Opisthotonus *(HPO: 6/12)* |
| Delayed speech/language | — | **12/13 (92%)** | HP:0000750 Delayed speech and language development *(HPO: 12/13)* |
| Cognitive developmental delay | **9/13 (69%)** | 6/13 (46%) mild or moderate, "as judged by the caring physician, however, there is no formal neuropsychological testing available" | HP:0001263 Global developmental delay *(HPO: 7/11)* |
| Dyspraxia | **9/14 (64%)** | 7/13 (54%) | HP:0002186 Apraxia *(HPO: 7/13)* |
| Dystonia (incl. oromandibular) | **8/14 (57%)** | 7/13 (54%) | HP:0001332 Dystonia *(HPO: 7/13)*; HP:0007325 Generalized dystonia |
| Hypokinesia | **6/13 (46%)** | — | HP:0002375 (hypokinesia; ID **not retrieved this session**) |
| Dysarthria | **4/9 (44%)** | — | HP:0001260 Dysarthria |
| Choreoathetosis | **3/14 (21%)** | documented in some | HP:0001266 Choreoathetosis |
| Lower-limb hyperreflexia | — | **10/12 (83%)** | HP:0002395 Lower limb hyperreflexia *(HPO: 10/12)* |
| Upper-limb hyperreflexia | — | **7/12 (58%)** | HP:0007350 Upper limb hyperreflexia *(HPO: 7/12)* |
| Friendly/"happy" demeanor | **13/13 (100%)** | all patients | no precise HPO term retrieved; nearest concept "happy demeanor" |
| Long eyelashes | **3/10 (30%)** | — | — |
| Dysmorphic ears | **3/11 (27%)** | — | — |
| Parkinsonism | documented, fraction not tabulated | — | HP:0001300 Parkinsonism *(HPO: no frequency)* |
| Cerebellar signs | **0** — "Cerebellar symptoms were not observed in our patients" | — | — |

**Internal inconsistency to flag for curation:** the Results text states "No dysmorphic features were noted," yet Table 1 tabulates long eyelashes 3/10 and dysmorphic ears 3/11. Treat dysmorphism as **absent/non-specific**.

**HPO-annotation discordance to flag:** the HPO annotation file for OMIM:619653 lists **Choreoathetosis (HP:0001266) at 11/11** sourced to PMID:32099069, whereas Wagner Table 1 reports choreoathetosis in **3/14 (21%)**. The HPO frequency appears to be a curation error; the primary table should govern. Similarly, HPO lists Global developmental delay 7/11 against Table 1's 9/13 for cognitive delay.

### 3b. Developmental milestone data (Wagner Table 1, medians with IQR)
- **Unsupported sitting:** median **12 months (IQR 10–20)** — text: "12±9 months"
- **Standing without assistance:** median **24 months (IQR 18–29)** — text: "35±12 months" for standing without hold
- **Walking without assistance:** median **36 months (IQR 36–36)**; "Free standing was not achieved at all in 4 children"
- **First words ("mama"):** median **29 months (IQR 20–32)**
- **50-word vocabulary:** median **4 years (IQR 3–5)**
- Language impairment was highly variable: "patient 7 speaking fluently from the age of five years onwards, whereas patient 6 still had severe expressive language impairment at the age of eight years, yet with concomitant dysarthria."

### 3c. Phenotype characteristics
- **Age of onset:** infantile. HPO annotates **HP:0003593 Infantile onset** to OMIM:619653 (source PMID:32099069). Opisthotonic posturing begins in the **first year**; in the Dufresne patient opisthotonic posture started at **4–6 weeks of age**; in the Lynch patient, floppy head and opisthotonic spasms of neck and back with generalized dystonia and spasticity began at **three months**.
- **Severity:** variable. "While the cardinal clinical features did not differ significantly between the 8 families, the grades of phenotypic severity varied to a greater extend."
- **Progression:** **non-progressive, with partial catch-up.** "The three oldest patients (age > 12y) included in our study as well as the case reported largely caught up the delay in cognitive and motor development after infancy... none of our patients developed neurological system involvement over time not noted before and the severity of the neurological symptoms didn't increase over time. Spasticity did neither improve nor deteriorate. This indicates that *TNR*-associated disease is non-progressive in nature."
- **Opisthotonus is episodic and self-limited** — it is the only clearly transient feature; spasticity is stable/persistent.
- **Behavioral phenotype:** notably positive sociability — "all patients were very friendly (happy demeanor) in their interaction with their environment which was not related to lack of stranger anxiety as observed in children with autism and we did not observe inappropriate laughter." No autism or ADHD diagnoses were reported in the cohort.

### 3d. Quality-of-life impact
**No QoL instrument data exist** (no EQ-5D, SF-36, PROMIS or disease-specific measures published). Functional impact can only be inferred from milestones: delayed/absent independent ambulation (4/13 never achieved free standing), substantial expressive language burden in some, and persistent spastic tone requiring long-term mobility support. I found no retrievable study of caregiver burden or participation outcomes.

### 3e. Other retrieved HPO annotations (from the single Lynch adult patient, PMID 28334938, each 1/1 — low-weight, single-case evidence)
HP:0000514 Slow saccadic eye movements; HP:0008959 Distal upper limb muscle weakness; HP:0007149 Distal upper limb amyotrophy; HP:0001347 Hyperreflexia; HP:0007305 CNS demyelination; HP:0007325 Generalized dystonia; HP:0002540 Inability to walk; HP:0001260 Dysarthria; HP:0001285 Spastic tetraparesis; HP:0000007 Autosomal recessive inheritance. **Caveat the CNS demyelination annotation:** Wagner et al. argue that patient's MRI/CSF findings reflect **concomitant multiple sclerosis**, not *TNR* disease (see §10).

Neuroimaging phenotypes (from the 11 patients with MRI): HP:0002188 Delayed CNS myelination (4/11), HP:0033725 Thin corpus callosum (1/11), HP:0001338 Partial agenesis of the corpus callosum (1/11).

---

## 4. Genetic / Molecular Information

### Causal gene
**TNR** (tenascin R), HGNC:11953, NCBI Gene 7143, 1q25.1, GRCh38 chr1:175,315,194–175,743,595 (ClinGen). The transcript is a **21-exon** transcript (NM_003285.2 in the discovery paper; MANE Select NM_003285.3/ENST00000367674.7). The protein (UniProt **Q92752**, TENR_HUMAN) is **1358 aa, 149,562 Da**, with a signal peptide at residues 1–31; alternative names **Janusin, Restrictin**. OMIM gene entry 601995 could not be retrieved (403).

**Domain architecture (UniProt Q92752, retrieved):** coiled-coil 127–157; **EGF-like ×5** at 188–199, 219–230, 250–261, 281–292, 312–323; **fibronectin type-III ×9** at 328–420 (FN1), 421–505 (FN2), 506–595 (FN3), 596–687 (FN4), 688–777 (FN5), 778–865 (FN6), 866–955 (FN7), 956–1042 (FN8), 1043–1130 (FN9); **fibrinogen C-terminal domain 1129–1344**. Heavily glycosylated: 12 N-glycosylation sites (N55, 180, 198, 278, 392, 470, 581, 791, 874, 1036, 1046, 1261), O-GalNAc at T36/T37, and **O-linked chondroitin sulfate at S176, S271, S302**; phosphoserine at S724.

### Pathogenic variants (all from Wagner et al. 2020, with ClinVar classifications retrieved via NCBI E-utilities)

| cDNA (NM_003285.3) | Protein (NP_003276.3) | Type | Zygosity / family | ClinVar VCV | ClinVar germline classification |
|---|---|---|---|---|---|
| c.207C>G | p.(Tyr69Ter) | nonsense | homozygous, Family F (patients 9, 10; Iraq) | VCV000691955.4 | **Pathogenic** |
| c.1189G>A | p.(Ala397Thr) | missense (FN3 domain 1) | compound het with c.1594G>A, Family H (patient 13; India) | VCV000691958.4 | **Likely pathogenic** |
| c.1594G>A | p.(Asp532Asn) | missense (FN3 domain 3) | compound het, Family H | VCV000691957.4 | **Likely pathogenic** |
| c.1899del | p.(Glu634Serfs*20) | frameshift | homozygous, Family D (patient 6; Brazil) | VCV000691954.4 | **Pathogenic** |
| c.2713C>T | p.(Arg905Ter) | nonsense | homozygous, Family A (patient 1; Turkey) | VCV000691951.5 | **Pathogenic** |
| c.2744_2745del (text: c.2744_2745delTG; "Data availability" section of the same paper writes c.2742_2743del) | p.(Val915Aspfs*64) | frameshift | homozygous, Family B (patient 2) | VCV000691952.5 | **Pathogenic** |
| c.3357C>G | p.(Ser1119Arg) | missense (FN3 domain 9) | homozygous, Family G (patients 11, 12; Brazil) | VCV000691956.4 | **Uncertain significance** |
| c.3574C>T | p.(Arg1192Trp) | missense (fibrinogen C-terminal domain) | homozygous in Family C (patients 3–5; Morocco) **and** Family E (patients 7, 8; Iraq) — two unrelated families | VCV000691953.5 | **Pathogenic** |

All eight ClinVar records carry review status **"criteria provided, single submitter"** (2–3 SCVs each), last evaluated **2019-07-25**, condition "Non-progressive neurodevelopmental disorder with spasticity and transient opisthotonus." **Flag the c.2742_2743del vs c.2744_2745del discrepancy** between the paper's Results text/Table and its own Data-availability list; ClinVar and Table 1 both use **c.2744_2745del**. Total ClinVar records for *TNR[gene]*: **340** (most unrelated to this condition).

**Previously reported alleles (pre-dating the disease definition):**
- **c.1475delG, p.(Arg492Profs*45)**, homozygous, Turkish female — Lynch DS et al., *Brain* 2017;140(5):1204–1211, PMID 28334938, DOI 10.1093/brain/awx045. OMIM designates a *TNR* allelic variant 601995.0001 (per search result; OMIM not directly retrievable).
- **Homozygous 1q25.1 deletion** `arr[GRCh37] 1q25.1(175,141,389–175,535,502)x0`, encompassing all *TNR* protein-coding exons plus part of the 5′UTR of *KIAA0040* — Dufresne D, Hamdan FF, Rosenfeld JA, Torchia B, Rosenblatt B, Michaud JL, Srour M. "Homozygous deletion of Tenascin-R in a patient with intellectual disability." *J Med Genet* 2012;49(7):451–454, **PMID 22730557**, PMCID PMC3395313, DOI 10.1136/jmedgenet-2012-100831. That paper also sequenced *TNR* in **219 patients with intellectual disability** and found no pathogenic mutations.

**Most recent alleles:** Ozaki et al. reported two Japanese siblings with novel compound heterozygous missense variants **NM_003285.3 c.[1783G>A];[3766C>T], p.(Asp595Asn);(Arg1256Cys)** (PMID 41233622). *Mapping those to domains is my own inference from the UniProt coordinates above: Asp595 sits at the C-terminal boundary of FN3 domain 3 (506–595) and Arg1256 within the fibrinogen C-terminal domain (1129–1344); the paper's own domain assignment was not retrievable.*

### Functional consequences
**Loss of function is the unifying mechanism.** Wagner et al.: "There was no significant clinical difference between individuals with LoF and missense variants that would imply a genotype–phenotype correlation indicating a **LoF character of the missense variants**." Their 3D modelling (WHAT IF & YASARA Twinset; FN1 modelled on PDB 3TEU, FN9 on 4U3H, fibrinogen domain on 6QNV, FN3 from PDB 1TDQ) concluded:
- **p.(Ala397Thr)** — buried alanine in the FN1 core; "Mutation of this small and hydrophobic residue into a slightly larger one with an extra hydrophilic sidechain is predicted to affect the local structure."
- **p.(Asp532Asn)** — surface of FN3; charge loss (Asp negative → Asn neutral); "The variant might affect interaction with **brevican** in the formation of perineuronal nets."
- **p.(Ser1119Arg)** — surface of FN9; small/neutral → large/positive; "This could affect any interactions made on the surface of this domain."
- **p.(Arg1192Trp)** — fibrinogen domain; "The arginine at this position is necessary for hydrogen bonds that stabilize the structure."
- Importantly for expression: the C-terminal variants "are not affected by the proteolytic cleavage of the 180 kDa TNR protein into the 160 kDa isoform and therefore the variant should be expressed."

No gain-of-function or dominant-negative mechanism has been proposed. No **modifier genes** have been identified (Ozaki et al. hypothesize modifiers exist but name none). **No epigenetic data** (methylation signature, episignature, histone marks) exist for NEDSTO in any retrieved resource. **Chromosomal abnormalities:** the only one reported is the Dufresne homozygous 1q25.1 microdeletion (~394 kb) — relevant to CMA-based diagnosis. **Somatic origin is not applicable**; all variants are germline.

---

## 5. Environmental Information

**Not applicable.** No environmental factors, lifestyle factors, or infectious agents have been implicated in NEDSTO in any source retrieved. Consanguinity is a *population-structure* risk factor for biallelic disease, not an environmental exposure. One tangential, non-causal observation: a 2023 rat study of bilirubin neurotoxicity appeared in literature searches under the keyword "opisthotonus" (PMID 37372119) — kernicterus is an **acquired** differential for neonatal opisthotonus and extrapyramidal CP, not a *TNR* mechanism.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic *TNR* LoF or structurally destabilizing missense variants** (nonsense, frameshift, whole-gene deletion, or missense in FN1/FN3/FN9/fibrinogen domains) → **absent or non-functional tenascin-R protein** in the CNS extracellular space. *Demonstrated genetically; protein-level loss inferred — no patient-tissue western blot, immunostaining or expression assay was performed in any retrieved study.*
2. Loss of tenascin-R → **failure of cross-linking of the lectican–hyaluronan lattice** that constitutes perineuronal nets. Wagner et al.: "*TNR* encodes tenascin-R, a member of the tenascin family of ECM glycoproteins, that is crucial for the crosslinking of proteoglycan hyaluronan complexes." Because native TN-R is di-/trimeric, it bridges multiple chondroitin-sulfate proteoglycan–hyaluronan complexes; the p.(Asp532Asn) modelling specifically predicts disrupted **brevican** interaction. *Mechanism established in mouse and in vitro; in human patients it is inferred.*
3. Defective perineuronal nets → **abnormal maturation and stabilization of inhibitory interneuron ensembles**. Tenascin-R "is crucial in the formation of perineuronal nets that ensheath interneurons," and is "expressed in type-2 astrocytes and few neuronal cells in the spinal cord, retina, cerebellum, and hippocampus, especially in perineuronal nets surrounding inhibitory interneurons."
4. → **Disrupted synaptic plasticity and altered excitation/inhibition balance.** "As tenascins are a crucial integral part of perineuronal nets and involved in the maturation and maintenance of neuronal networks, a disruption of synaptic plasticity could explain the neurodevelopmental phenotype in our patients." *Explicitly framed by the authors as a proposed, not demonstrated, link.*
5. **Branch A — oligodendrocyte/myelination arm.** Independently, "*TNR* is highly expressed in oligodendrocyte precursors with a decreased expression during oligodendrocyte differentiation, suggesting a functional role during myelination. This might explain why 40% of our cases had delayed myelination as abnormal MRI findings." → delayed CNS myelination → contributes to motor delay; **resolves or improves over time**, consistent with the non-progressive course.
6. **Branch B — corticospinal/motor arm.** Loss of PNN scaffolding around motor-system interneurons and altered axonal conduction (Tnr^−/− mice show "decreased axonal conduction velocities in the CNS" and "reduced conduction velocity of the optic nerve") → **appendicular spasticity with axial hypotonia** and hyperreflexia. *Inferred; no direct corticospinal-tract study in patients.*
7. **Branch C — extrapyramidal arm.** "Movement disorders (dystonia, parkinsonism) indicate an affection of the **extrapyramidal motor system** in *TNR*-related disease." → dystonia, hypokinesia, choreoathetosis, and the **transient opisthotonic posturing** of infancy. *The specific circuit mechanism for opisthotonus is not established in any retrieved source — this is the biggest mechanistic gap in the entity.*
8. **Why non-progressive:** "The spatiotemporal expression pattern with the highest expression of TNR in the developing brain is in line with the observed non-progressive fashion of the disease." Tenascin-R is "exclusively expressed in the central nervous system with highest expression after birth" (with transient Schwann-cell expression during peripheral nerve development) — so the lesion is a **fixed developmental** one, not an ongoing degenerative one. Supporting clinical evidence: "The observations, that none of our patients developed novel neurological system involvement over time and that the MRI findings improved in follow-up investigations, argue against neurodegenerative aspect."

### Molecular pathways, cellular processes, protein function
Tenascin-R is **not a signaling-cascade component**; it is a structural/modulatory ECM glycoprotein. Retrieved UniProt FUNCTION annotation (abridged quote within limits): *"Neural extracellular matrix (ECM) protein involved in interactions with different cells and matrix components."* The annotation (by similarity) further describes: context-dependent promotion of stable adhesion and differentiation **or** cell repulsion and neurite-growth inhibition; binding to cell-surface gangliosides inhibits RGD-dependent integrin adhesion and **FAK phosphorylation**; binding to **sulfatides** promotes oligodendrocyte adhesion and differentiation; interaction with **CNTN1 (contactin-1)** causes neuron repulsion; interaction with **SCN2B** may contribute to **sodium-channel clustering at nodes of Ranvier**. Wagner et al. summarize the functional repertoire as "neurite outgrowth, neural cell adhesion, proliferation and migration, fate determination, axonal guidance, myelination, synaptic plasticity and modulation of sodium channel function."

**GO terms retrieved from UniProt Q92752:**
- Cellular component: **GO:0072534 perineuronal net**; **GO:0090733 tenascin complex**; GO:0031012 extracellular matrix; GO:0005576 extracellular region
- Biological process: **GO:0007411 axon guidance**; **GO:0007155 cell adhesion**; **GO:0010977 negative regulation of neuron projection development**; **GO:0007399 nervous system development**; GO:0030155 regulation of cell adhesion; GO:0045595 regulation of cell differentiation; GO:0030334 regulation of cell migration
- *No molecular-function GO terms are annotated to Q92752.*

**Processing:** "Proteolytic cleavage of the amino-terminal region from the 180kb [sic — 180 kDa] protein product gives rise to the smaller 160kD isoform."

**Not applicable / no data:** metabolic changes, immune involvement (no autoimmunity in NEDSTO — though note the unrelated finding of **anti-tenascin-R autoantibody in an adult with isolated tremor**, Yang B et al., *Ann Neurol* 2023;94(3):502–507, PMID 37370243, which is an acquired autoimmune phenocopy of interest, not NEDSTO), oxidative stress/fibrosis/necrosis mechanisms, epigenetic changes, transcriptomics, proteomics, metabolomics, lipidomics, single-cell or spatial data, and CRISPR/RNAi screens — **none retrieved for this disease**.

**Suggested ontology terms (labels verified; numeric IDs for CL/UBERON were NOT retrieved this session and should be looked up before curation):** cell types — inhibitory interneuron (notably parvalbumin-positive), oligodendrocyte precursor cell, oligodendrocyte, astrocyte (type-2), Schwann cell (transient, developmental); anatomical sites — cerebral white matter, corpus callosum, hippocampus (CA1), spinal cord, retina, cerebellum, optic nerve, node of Ranvier.

---

## 7. Anatomical Structures Affected

**Organ level.** Exclusively the **central nervous system**; no extraneural organ involvement has been reported. Wagner et al.: "*TNR* is exclusively expressed in the central nervous system with the exception of a transient expression in Schwann cells during peripheral nerve development." UniProt tissue specificity: **"Brain specific"** (PubMed:8626505). No cardiac, renal, hepatic, hematologic, endocrine or ophthalmologic structural involvement; growth parameters were assessed but no growth phenotype was described; microcephaly is **not** reported.

**Regional / imaging-defined involvement** (brain MRI, 11/13 patients evaluated by a single pediatric neuroradiologist; **6/11 = 65% abnormal**):
- **Subcortical/temporal white matter — delayed myelination** in 4 patients (patients 1, 3, 5, 9 at ages 4 months, 1 y 7 mo, 10 months and 2 y 8 mo). In patient 3 the temporal subcortical delay **persisted at age 5 years**; in patient 1 it **normalized** on follow-up at 2 years.
- **Corpus callosum** — thin corpus callosum (patient 6); **partial posterior agenesis with splenium agenesis** (patient 11, at 10 months).
- **Cerebellum — normal in all cases.** "Cerebellar abnormalities were not found in any of our cases."
- Normal MRI in patients 2, 4, 7, 12 and 13.
- The authors explicitly decline to define an imaging signature: "Given that delayed myelination and corpus callosum hypoplasia are rather unspecific findings, we could not establish a consistently recognizable MRI phenotype. Intrafamilial heterogeneity as assessed in Family C and G was considerable with individuals having both normal and pathologic MRIs at comparable ages within individual pedigrees."

**Functional systems involved:** corticospinal/pyramidal (spasticity, hyperreflexia), **extrapyramidal/basal ganglia** (dystonia, parkinsonism, choreoathetosis, hypokinesia), axial/postural control (axial hypotonia, opisthotonus), language/cognitive networks, praxis networks (dyspraxia). **Cerebellar system spared.**

**Tissue/cell level.** Perineuronal net ECM surrounding **inhibitory interneurons**; oligodendrocyte precursor cells and myelinating oligodendrocytes; type-2 astrocytes; a small population of neurons in spinal cord, retina, cerebellum and hippocampus. In mouse, the knockout shows **hippocampal CA1 pyramidal-layer** and **synaptic/presynaptic active-zone** abnormalities (see §15).

**Subcellular level.** Tenascin-R is **secreted into the extracellular space/extracellular matrix** (UniProt subcellular location); the disease compartment is therefore **GO:0031012 extracellular matrix** and **GO:0072534 perineuronal net**, with functional consequence at the **node of Ranvier** (sodium-channel clustering, via SCN2B) and the **synapse**. No intracellular organelle pathology (mitochondrial, lysosomal, ER) is implicated.

**Lateralization.** **Bilateral and symmetric.** Spasticity is described as para- or tetraparesis/diplegia (one patient recorded as "lower limb diparesis"); no asymmetric or hemiplegic presentation was reported.

---

## 8. Temporal Development

**Onset.** Congenital/infantile; HPO annotates **HP:0003593 Infantile onset**. Pregnancy, delivery and postnatal adaptation were uneventful in most families. Earliest documented sign is **opisthotonic posturing at 4–6 weeks** (Dufresne patient) and **3 months** (Lynch patient). Onset pattern is **insidious**, usually recognized as unexplained motor delay rather than as an acute event.

**Progression.** **Non-progressive, with partial catch-up** — this is the defining temporal feature and the reason the condition sits with the CP mimics rather than with the leukodystrophies or HSPs. Explicit statements from the primary paper are quoted in §3c and §6. Key points:
- Severity of neurological symptoms did not increase over time; spasticity "did neither improve nor deteriorate."
- No new neurological system involvement appeared during follow-up.
- MRI findings **improved** on follow-up (patient 1's delayed myelination normalized by 2 years).
- The three oldest study patients (>12 y) "largely caught up the delay in cognitive and motor development after infancy."
- MedGen's OMIM-derived summary (reached via search results, not direct fetch) states that many patients may catch up developmentally in the second or third decades.

**Disease course pattern.** Chronic, lifelong, **stable** after the early-childhood period. The one **episodic/transient** element is opisthotonus, confined to the first year of life (the Dufresne patient's choreoathetosis was likewise described as transient).

**Disease stages.** No formal staging system exists. Pragmatically: (i) infancy — hypotonia, opisthotonic episodes, emerging spasticity, delayed myelination on MRI; (ii) early childhood — delayed milestones, evolving spastic para-/tetraparesis, extrapyramidal features, speech delay; (iii) later childhood/adolescence/adulthood — plateau with partial catch-up, residual spasticity and movement disorder. *This staging is my own synthesis of the published course, not a published schema.*

**Remission.** Spontaneous resolution of opisthotonus; no treatment-induced remission documented. **Critical periods:** the window of highest *TNR* expression is postnatal brain development — biologically the period when any future intervention would need to act; no interventional window has been studied.

**Duration.** Lifelong. Oldest reported individuals: 24 years (patient 8) and 19 years (Lynch patient); median age at last examination in the pooled table **6.3 years (IQR 2–12)**.

---

## 9. Inheritance and Population

**Epidemiology.** **No prevalence or incidence estimate exists.** No Orphanet prevalence class, no registry, no GBD entry was found. The published literature totals roughly **17 individuals** (13 Wagner + 1 Lynch + 1 Dufresne + 2 Ozaki siblings); Ozaki et al. frame their analysis across **15 patients (13 previously reported)**. The disorder is ultra-rare; any quantitative prevalence statement would be unsupported.

**Inheritance pattern.** **Autosomal recessive** — OMIM 619653, Monarch (`inheritance: HP:0000007`), ClinGen (AR), UniProt disease comment, and HPO annotation (HP:0000007, source PMID:28334938) all concur. Heterozygous parents and sibs were unaffected in all pedigrees ("+/- are heterozygous carriers").

**Penetrance.** Complete penetrance was implicit in the original cohort. This is now **contested**: Ozaki et al. report a sibling pair sharing identical biallelic missense variants in which the sister had **normal development and intellect** and was asymptomatic apart from adult-onset restless legs syndrome, while the brother had dystonia; they conclude the data suggest **variable expressivity and reduced penetrance**, possibly modifier-driven (PMID 41233622). Curation should record penetrance as **incomplete/uncertain**, flagged to that 2025/2026 report, and note that it rests on one family.

**Expressivity.** **Variable**, including intrafamilially. Wagner et al.: cardinal features were consistent across families but "the grades of phenotypic severity varied to a greater extend"; intrafamilial MRI heterogeneity in Families C and G was "considerable." The authors suggest "these differences might be explained by the excess of homozygous variants in our consanguineous families."

**Genetic anticipation.** Not applicable — no repeat expansion; no anticipation reported.

**Germline mosaicism.** Not reported; no data.

**Founder effects.** None established. The recurrence of **c.3574C>T p.(Arg1192Trp)** in two unrelated families is notable — Wagner et al. state "The latter was found in a family from Iraq and Morocco and is absent from control databases." Whether this reflects a shared ancient haplotype or a mutational hotspot was **not tested** (no haplotype analysis reported).

**Consanguinity.** Central to ascertainment: 7 of 8 index families were consanguineous; 6 of 8 families carried **homozygous** variants.

**Carrier frequency.** Not formally calculated. The only quantitative anchor: "Heterozygous LoF variants in *TNR* are rare (**40 in > 280 000 alleles**)" in gnomAD, with no homozygotes.

**Population demographics.** Reported ancestries (Wagner Table 1 origin row): **Turkish, "Arabian", Moroccan ×3, Brazilian ×3, Iraqi ×4, Indian**, plus **Turkish** (Lynch) and **Lebanese** (Dufresne). The newest cases are **Japanese** (Ozaki). This spread reflects consanguinity-enriched referral populations and international matchmaking (GeneMatcher), **not** a true geographic restriction. No variant shows a documented geographic clustering.

**Sex ratio.** **8 F : 7 M** in the pooled Table 1 (no sex bias expected or observed; autosomal recessive).

**Age distribution of affected individuals reported:** 1 y 10 mo to 24 years at last examination; median 6.3 y.

---

## 10. Diagnostics

### Genetic testing — the only confirmatory modality
- **Approach:** NEDSTO is a **sequencing-based diagnosis**. All published cases but one were ascertained by **exome sequencing** in children with unexplained developmental delay/spasticity after other causes were excluded: "In all index patients, exome sequencing at the local genetic centres did not identify causative variants in established disease genes. Filtering for rare (MAF < 0.5% in the respective in-house databases) protein altering variants identified biallelic variants in *TNR* (NM_003285.2) in index patients from all families." Collaboration was assembled through **GeneMatcher**.
- **WES/WGS:** high-yield and appropriate first-tier for this phenotype. **Segregation by Sanger sequencing** was used to confirm biallelic status and compound-heterozygous phase in Family H.
- **Gene panels:** *TNR* must be on the panel to be found. Practical caution for curation — because the phenotype is read clinically as spastic CP or complicated HSP, *TNR* may be absent from older HSP/dystonia panels; **cerebral palsy / CP-mimic panels** are the appropriate panel class (reflected by ClinGen's assignment to the Cerebral Palsy GCEP). I found no retrievable GTR panel inventory this session.
- **Chromosomal microarray (CMA):** genuinely contributory — the first reported case was a **homozygous 1q25.1 deletion detected by array genomic hybridisation** (Dufresne et al. 2012, PMID 22730557). CMA will detect biallelic whole-gene deletions that exome calling may miss.
- **Karyotyping, FISH, mtDNA testing, repeat-expansion testing:** no role.
- **Variant interpretation:** ACMG/AMP classification is applied; current ClinVar status per variant is tabulated in §4 (five Pathogenic, two Likely pathogenic, one VUS). Note the **VUS** status of c.3357C>G p.(Ser1119Arg) — a family-G variant that the discovery paper itself flagged as VUS.

### Imaging
**Brain MRI** is supportive but **non-diagnostic**. Findings: delayed myelination of subcortical/temporal white matter (4/11), thin or partially agenetic corpus callosum (2/11), normal study in ~35%. The authors explicitly state no recognizable MRI phenotype could be established. Follow-up imaging showing **improvement** is itself a useful negative discriminator against neurodegenerative disease.

### Laboratory tests, biomarkers, electrophysiology, biopsy
**None established.** No biochemical biomarker, no enzyme assay, no CSF marker, no EMG/NCS protocol, no EEG signature, and no biopsy/histopathology findings have been published for NEDSTO. Notably, **CSF oligoclonal bands are NOT a feature** — see the MS discussion below. Tenascin-R is brain-specific, so no accessible-tissue protein assay is available; this is a real gap for functional variant interpretation (ClinGen lists **0** variant pathogenicity assertions for *TNR*).

### Omics-based diagnostics
No RNA-seq, proteomic, metabolomic, epigenomic (episignature) or liquid-biopsy diagnostic exists for this disorder. An episignature has not been sought.

### Clinical criteria and differential diagnosis
There are **no standardized diagnostic criteria**. Diagnosis = compatible phenotype + biallelic *TNR* variants. Differentials to exclude:
- **Cerebral palsy (spastic diplegic/tetraplegic, dyskinetic forms)** — the usual working diagnosis; distinguished by uneventful perinatal history and absence of a causative acquired lesion. The authors' own keywords name cerebral palsy; ClinGen curated this gene through the Cerebral Palsy GCEP. Broader context: biallelic variants in other genes (e.g. *SPAST*, *HPDL*, *RINT1*) similarly present as CP mimics.
- **Complicated hereditary spastic paraplegia (HSP)** — explicitly addressed: "It is difficult to confine *TNR* associated disease from complicated hereditary spastic paraplegia (HSP) which is characterized by progressive lower limb spasticity and weakness in combination with additional neurologic features such as cognitive deficits, movement disorder or neuropathy. However, based on the core phenotype, i.e. the spastic affection of **both upper and lower limbs** as well as this **non-progressive** nature of the symptoms, we regard *TNR*-related disease as different from HSP."
- **Leukodystrophy / multiple sclerosis** — the Lynch patient was recruited from a leukoencephalopathy cohort and was diagnosed with **MS at 19** on the basis of T2/FLAIR periventricular, brainstem and cerebellar hyperintensities with CSF oligoclonal bands. Wagner et al. argue these are **not** part of *TNR* disease: "since none of the individuals reported in the present study had MS-like MRI or CSF findings, the published patient potentially was suffering from both *TNR*-associated neurodevelopmental disease and concomitant MS and that the oligoclonal bands were not associated with the variant in *TNR*." **Curation consequence:** HPO's HP:0007305 (CNS demyelination) annotation to OMIM:619653 is probably attributable to that comorbidity and should be de-weighted.
- **Primary dystonia / combined dystonia syndromes** and **genetic parkinsonism** — overlapping extrapyramidal features.
- **Kernicterus/bilirubin encephalopathy** — acquired cause of neonatal opisthotonus plus extrapyramidal CP.

### Screening
**No newborn screening, no population carrier screening, and no cascade-screening program exists.** Cascade testing of at-risk relatives for known familial variants is possible and appropriate but no published protocol or uptake data exist.

---

## 11. Outcome / Prognosis

**Survival and mortality.** **No deaths have been reported** in any published individual. There are no survival curves, life-expectancy estimates, or mortality data. The absence of progression, the absence of reported seizures, bulbar failure or respiratory compromise in the cohort, and survival to at least 24 years all suggest life expectancy is not obviously curtailed — but this is an **inference from a tiny cohort with short follow-up**, not an established finding, and should be curated as "unknown."

**Morbidity and function.** The dominant burden is **motor**: median independent walking at 36 months, with **4/13 never achieving free standing**; persistent spastic para-/tetraparesis in ~87%; superimposed dystonia (~57%), dyspraxia (~64%) and hypokinesia (~46%). **Communication burden**: 92% with delayed language, 50-word vocabulary at a median of 4 years, dysarthria in ~44%; expressive impairment can be severe and persistent (patient 6 at 8 years). **Cognitive burden** is milder than the motor burden — mild-to-moderate impairment in 46–69% depending on denominator, with the caveat that "there is no formal neuropsychological testing available." No **intellectual disability severity distribution** has been formally measured.

**Behavioral/psychosocial outcome.** Uniformly sociable, friendly demeanor (13/13); no autism diagnoses, no inappropriate laughter. This is prognostically favorable for family and school integration.

**Recovery potential.** Partial: the three oldest study patients (>12 y) "largely caught up the delay in cognitive and motor development after infancy," and MedGen's OMIM-derived summary describes catch-up in the second or third decades. **Spasticity itself does not remit** — "Spasticity did neither improve nor deteriorate." Delayed myelination on MRI may normalize.

**Complications.** No complication set has been systematically reported. Complications expected in any chronic spastic condition — contractures, hip subluxation, scoliosis, feeding/communication difficulties — were **not tabulated** in the primary paper and I found no data on them; this is a genuine gap, not an absence.

**Prognostic factors and biomarkers.** **None identified.** Wagner et al. explicitly found no genotype–phenotype correlation: "There was no significant clinical difference between individuals with LoF and missense variants that would imply a genotype–phenotype correlation." No prognostic biomarker exists. The Ozaki sibling discordance suggests prognosis cannot currently be predicted from genotype.

**Quality-of-life measures.** None published (no EQ-5D, SF-36, PROMIS, CPCHILD or other instrument data).

---

## 12. Treatment

**There is no disease-specific, disease-modifying or published treatment for NEDSTO.** I searched for and did not find any treatment, management guideline, GeneReviews chapter, clinical trial, or therapeutic case report for this disorder. The primary paper contains **no treatment or management section**. This should be curated as an explicit evidence gap rather than populated with generic content.

- **Pharmacotherapy:** no drug has been reported as used or studied in *TNR*-related disease. Anti-spasticity and anti-dystonia agents would be used by analogy to spastic CP/dystonia management, but **no published evidence exists in this disorder** — any such annotation must be labeled as extrapolation, not as disease-specific evidence.
- **Pharmacogenomics:** ClinGen lists **0 CPIC and 0 PharmGKB records** for *TNR*.
- **Gene therapy, cell therapy, RNA-based therapy, targeted therapy, immunotherapy:** none exist, none in development that I could retrieve. Conceptually, a secreted brain-specific ECM structural protein whose critical expression window is early postnatal development is an unfavorable target for post-symptomatic replacement; the phenotype's non-progressive, partly self-correcting nature further limits the rationale. *That assessment is my inference from the biology, not a published position.*
- **Surgical/interventional:** no reported orthopedic or neurosurgical (e.g. selective dorsal rhizotomy, intrathecal baclofen, DBS) experience in *TNR* patients.
- **Supportive and rehabilitative care:** physiotherapy, occupational therapy, speech/language therapy and assistive mobility are the implied mainstays given the phenotype, but **no outcome data, protocol or guideline specific to this disorder has been published**.
- **Experimental treatments / clinical trials:** **no NCT identifiers** for NEDSTO or *TNR* were found.
- **Treatment outcomes, adverse events, algorithms, combination therapy, genotype-guided therapy:** no data.

**NCIT terms:** not supplied — I did not retrieve NCIT identifiers in this session and will not assert unverified codes. Relevant intervention *labels* for later NCIT lookup: physical therapy, occupational therapy, speech therapy, antispasmodic/antispasticity pharmacotherapy, orthotic device.

---

## 13. Prevention

**Primary prevention.** Not possible at the individual level — the disorder is germline and fully determined at conception. The only applicable measures are **reproductive**: genetic counseling for couples with a known biallelic risk (25% recurrence per pregnancy for carrier×carrier couples), **prenatal diagnosis** and **preimplantation genetic testing** for the known familial variants. These follow from the established AR inheritance (OMIM/ClinGen/Monarch); **no NEDSTO-specific reproductive-genetics guideline exists**, and I retrieved no ACMG/ACOG statement naming this gene.

**Secondary prevention.** No screening program, newborn screening panel, or early-detection pathway includes *TNR*. The practical secondary-prevention lever is **earlier molecular diagnosis** in children labeled with "cerebral palsy of unknown cause" — exome/genome sequencing in that population ends the diagnostic odyssey, enables accurate recurrence counseling, and avoids unnecessary investigation for progressive/metabolic disease. *This recommendation follows from the ClinGen Cerebral Palsy GCEP framing and the paper's own ascertainment route; it is not a published guideline recommendation specific to this gene.*

**Tertiary prevention.** No disorder-specific protocol published. Prevention of secondary musculoskeletal complications of spasticity would follow general spastic-CP practice, but — as in §12 — there is no NEDSTO-specific evidence.

**Immunization, behavioral interventions, public-health and environmental interventions, prophylaxis:** **not applicable** — the disorder has no infectious, behavioral or environmental component.

**Counseling.** Standard autosomal recessive counseling applies: unaffected obligate-heterozygote parents; 25% recurrence risk; sib carrier risk 2/3 if unaffected; carrier testing for extended family, with particular relevance in consanguineous kindreds where most reported families arose. Counseling should now incorporate the **penetrance/expressivity caveat** from Ozaki et al. — an identically genotyped sibling may be substantially less affected or essentially asymptomatic — which materially changes how recurrence outcomes should be framed to families.

---

## 14. Other Species / Natural Disease

**Taxonomy and orthology (retrieved).** Human *TNR* (NCBI Gene 7143, HGNC:11953) has a mouse ortholog **Tnr**, **MGI:99516**, NCBI Gene **21960**, Ensembl **ENSMUSG00000015829**, mouse chromosome 1:159,351,339–159,759,299 (GRCm39, + strand; 69.03 cM, cytoband 1E2); MGI asserts orthology to human TNR at 1q25.1 ([MGI](https://www.informatics.jax.org/marker/MGI:99516)). Mouse gene synonyms: **J1-tenascin, janusin, restrictin, TN-R**. *(NCBI Taxon IDs: human NCBITaxon:9606 appears in the Monarch record; the mouse taxon ID was not separately retrieved this session.)*

**Naturally occurring disease in other species.** **None identified.** I found no OMIA entry, no veterinary case reports, and no breed-associated *TNR* disorder; no VBO breed identifier applies. A canine inherited-neurological-disorders review surfaced in literature searching (PMID 38003185) but does not concern *TNR*. Curate as: **no known natural animal disease; no veterinary relevance.**

**Comparative biology.** All disease modeling is **induced** (engineered mouse alleles), not natural. Comparative pathology is informative but imperfect: the mouse null is far milder than the human disorder. Wagner et al.: "Even though the behavioural phenotype of TNR-deficient mice does not resemble the symptoms observed in our patients, the mouse model clearly indicates that loss of TNR results in a neurodevelopmental defect." **Evolutionary conservation** of the perineuronal-net mechanism is implied by the shared gene architecture and the conserved PNN biology across mammals; I did not retrieve HomoloGene/Alliance ortholog tables beyond mouse this session (the Alliance page returned an empty JavaScript shell).

**Transmission.** Not applicable — **no zoonotic potential, no cross-species transmission**; this is a Mendelian germline disorder.

---

## 15. Model Organisms

### Available models
**Mouse is the only established model system.** MGI records **12 alleles** of *Tnr*: 4 targeted, 5 endonuclease-mediated, 2 chemically induced (other), 1 transgenic, and 2 genomic mutations ([MGI:99516](https://www.informatics.jax.org/marker/MGI:99516)). The allele-summary page returned no rows on fetch, so I cannot list all 12 by symbol.

Two alleles carry phenotype annotations ("11 phenotypes from 2 alleles in 2 genetic backgrounds"):

| Allele | Allele ID | Background | MP annotations |
|---|---|---|---|
| **Tnr^tm1Msch** (Schachner lab targeted mutation) | **MGI:2154583** | 129P2/OlaHsd × C57BL/6J | **MP:0008263** abnormal hippocampus CA1 region morphology; **MP:0008284** abnormal hippocampus pyramidal cell layer; **MP:0003632** abnormal nervous system morphology; **MP:0015052** abnormal presynaptic active zone morphology; **MP:0009538** abnormal synapse morphology; **MP:0004769** abnormal synaptic vesicle morphology; **MP:0008814** decreased nerve conduction velocity; **MP:0015056** increased synaptic vesicle number |
| **Tnr^em1(IMPC)Rbrc** | **MGI:6156164** | C57BL/6NJcl | **MP:0001565** abnormal circulating phosphate level; **MP:0003313** abnormal locomotor activation; **MP:0004952** increased spleen weight |

*(The "tm1" designation conventionally denotes a targeted mutation; the MGI page itself did not state the allele type, so I flag that as nomenclature convention rather than a retrieved fact.)*

### Phenotype recapitulation
**Partial, and weaker than the human phenotype.** MGI's own summary states verbatim: *"In spite of having decreased conduction velocity in the optic nerve and ultrastrucural alterations within the hippocampus, homozygous null mice are viable, fertile, and display normal behavior."* Wagner et al. likewise: "Tenascin-R deficient mice are viable and fertile and do not show any obvious disease phenotype. However, they display increased anxiety and motor coordination impairment in specific tests."

Phenotypes described in the primary paper's literature synthesis (each cited there to a primary mouse study):
- **Increased anxiety and impaired motor coordination** in specific tests (Freitag S, Schachner M, Morellini F. *Behav Brain Res* 2003;145(1-2):189–207 — cited as reference 12; wire-hanging, Rotarod and pole-test deficits, and reduced exploratory motivation with a higher anxiety profile in free-choice open field, open field and elevated plus maze, per retrieved bibliographic records).
- **Altered synaptic activity, decreased extracellular space volume and tortuosity, and altered density of perineuronal nets** (Bruckner G et al. *J Comp Neurol* 2000;428(4):616–629).
- **Abnormal perineuronal net formation and reduced optic-nerve conduction velocity** (Weber P, Bartsch U, Rasband MN, et al. *J Neurosci* 1999;19(11):4245–4262 — "Mice deficient for tenascin-R display alterations of the extracellular matrix and decreased axonal conduction velocities in the CNS").
- **Abnormal hippocampal morphology and reduced coverage of symmetric synapses on pyramidal cells** (Nikonenko A et al. *J Comp Neurol* 2003;456(4):338–349).
- **Increased numbers of GABAergic interneurons during foetal development**, and regulation of neuronal differentiation in the dentate gyrus (Xu JC, Xiao MF, Jakovcevski I, et al. *J Cell Sci* 2014;127(Pt 3):641–652).

Mechanistic PNN work beyond the paper: tenascin-R and aggrecan are described as decisive contributors to PNN formation and stabilization, with TN-R acting by **clustering aggrecan** and cross-linking lectican–hyaluronan complexes (Morawski et al., 2014; [PMC4173296](https://pmc.ncbi.nlm.nih.gov/articles/PMC4173296)). Compound ECM knockouts are more informative than single knockouts: a **quadruple brevican/neurocan/tenascin-C/tenascin-R knockout** showed impaired fear-memory consolidation and reduced PNN density, while — importantly — *"tenascin single KOs showed intact fear behavior and memory"* (Mueller-Buehl C et al., *Sci Rep* 2025;15(1):5528, PMID 39953103, PMCID PMC11828866, DOI 10.1038/s41598-025-89580-2).

### Model limitations
1. **The mouse null does not reproduce the cardinal human features** — no spasticity, no opisthotonus, no gross developmental delay; gait and basic motor behavior are reported as normal, with deficits emerging only under demanding conditions. This is the single most important limitation for using the mouse as a preclinical efficacy model.
2. **Redundancy within the tenascin/lectican family** likely buffers single-gene loss in mouse (supported by the quadruple-knockout contrast above).
3. **No patient-derived model exists** — no iPSC line, no cerebral organoid, no neuron/OPC model, and no *in vitro* functional assay for *TNR* missense variants was reported in any retrieved study. Variant interpretation therefore rests on *in silico* prediction and 3D homology modelling (WHAT IF/YASARA; templates PDB **3TEU**, **4U3H**, **6QNV**, **1TDQ**), which is **computational evidence**, not functional evidence. This directly explains ClinGen's **0 variant pathogenicity assertions** and the persistence of a VUS among the reported alleles.
4. No zebrafish, Drosophila or C. elegans model of *tnr* was retrieved.

### Research applications
Existing models support study of PNN assembly, interneuron maturation, synaptic plasticity, axonal conduction and myelination — i.e. the upstream biology. They are poorly suited to modelling the human motor phenotype or to therapeutic efficacy testing.

### Resources
MGI (gene MGI:99516; alleles MGI:2154583, MGI:6156164); IMPC (the em1(IMPC)Rbrc allele indicates IMPC pipeline data exist — I did not retrieve the IMPC portal directly). Alliance of Genome Resources returned an empty page shell and yielded no data this session.

---

## Evidence summary and curation cautions

**Evidence classes used above:**
- *Primary human literature (case series):* Wagner et al. 2020, PMID 32099069 — the sole substantive clinical source; n=13; retrospective, multicenter, no formal neuropsychological testing, single-neuroradiologist MRI review.
- *Primary human literature (single cases):* Dufresne et al. 2012 PMID 22730557; Lynch et al. 2017 PMID 28334938 (ascertained for adult leukoencephalopathy; probable concomitant MS).
- *Primary human literature (most recent):* Ozaki et al., *J Hum Genet* 2026;71(4):231–237, PMID 41233622 — two siblings; the source of the penetrance/expressivity caveat. I retrieved its PubMed record; the full text was paywalled/cookie-gated, so variant and phenotype details come from the abstract record only.
- *Expert-panel structured assertion:* ClinGen Cerebral Palsy GCEP, Definitive/AR, 2025-01-02.
- *Structured databases:* ClinVar (E-utilities), UniProt Q92752, HPO annotation API, Monarch API, MGI.
- *Model organism:* mouse Tnr knockout literature, cited secondhand through Wagner et al.'s reference list except where a PMID is given directly.
- *Computational:* 3D homology modelling of missense variants; gnomAD constraint.

**Flags for the knowledge-base entry:**
1. **HPO frequency for HP:0001266 Choreoathetosis (11/11, sourced to PMID:32099069) contradicts the source paper's Table 1 (3/14, 21%).** Prefer the primary table; consider reporting the discrepancy to HPO.
2. **HP:0007305 CNS demyelination** is annotated from the Lynch patient, whose demyelinating findings the discovery authors attribute to **concomitant MS**, not to *TNR*. De-weight or annotate with that caveat.
3. **Variant nomenclature conflict** within Wagner et al.: c.2744_2745del (Results/Table/ClinVar) vs c.2742_2743del (Data-availability list). Use **c.2744_2745del, p.(Val915Aspfs*64)**.
4. **Internal conflict on dysmorphism**: text says none; Table reports long eyelashes 3/10 and dysmorphic ears 3/11.
5. **Denominator discipline**: Table 1's "All" column pools Wagner's 13 patients with the Lynch and Dufresne cases (n≈15); the Results text uses the 13-patient cohort or the examined subset. Record which denominator each frequency came from.
6. **Penetrance is no longer safely assumed complete** (Ozaki et al.).
7. **Not retrieved this session, and therefore not asserted:** OMIM 619653 and 601995 full text and clinical synopsis (HTTP 403); Orphanet entry/ORPHA code and prevalence; gnomAD observed/expected LoF counts; UBERON, CL and NCIT identifiers; GTR panel inventory; IMPC phenotype detail; OMIA records.

---

**Sources:**
- [Wagner M, et al. Loss of TNR causes a nonprogressive neurodevelopmental disorder with spasticity and transient opisthotonus. Genet Med 2020;22(6):1061–1068 (PMID 32099069) — full author manuscript, UCL Discovery](https://discovery.ucl.ac.uk/id/eprint/10094729/1/TNR,%20Wagner,%20M%20et%20al..pdf)
- [Genetics in Medicine article page](https://www.gimjournal.org/article/S1098-3600(21)00839-X/fulltext)
- [Ozaki A, et al. Biallelic variants in TNR cause neurodevelopmental disorders with variable expressivity. J Hum Genet 2026;71(4):231–237 (PMID 41233622)](https://pubmed.ncbi.nlm.nih.gov/41233622/)
- [Dufresne D, et al. Homozygous deletion of Tenascin-R in a patient with intellectual disability. J Med Genet 2012;49(7):451–454 (PMID 22730557)](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22730557&rettype=abstract&retmode=text)
- [Lynch DS, et al. Clinical and genetic characterization of leukoencephalopathies in adults. Brain 2017;140(5):1204–1211 (PMID 28334938)](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=28334938&rettype=abstract&retmode=text)
- [ClinGen — TNR curation results (HGNC:11953)](https://search.clinicalgenome.org/kb/genes/HGNC:11953)
- [HPO annotation API — OMIM:619653](https://ontology.jax.org/api/network/annotation/OMIM:619653)
- [Monarch Initiative API — MONDO:0859212](https://api.monarchinitiative.org/v3/api/entity/MONDO:0859212)
- [UniProt Q92752 (TENR_HUMAN)](https://rest.uniprot.org/uniprotkb/Q92752.txt)
- [ClinVar esummary, variation IDs 691951–691958](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=clinvar&id=691951,691952,691953,691954,691955,691956,691957,691958&retmode=json)
- [MGI — mouse Tnr, MGI:99516](https://www.informatics.jax.org/marker/MGI:99516)
- [Mueller-Buehl C, et al. Sci Rep 2025;15:5528 (PMID 39953103)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11828866)
- [Yang B, et al. Ann Neurol 2023;94(3):502–507 (PMID 37370243)](https://pubmed.ncbi.nlm.nih.gov/37370243/)
- [Morawski M, et al. — tenascin-R and aggrecan in perineuronal net formation](https://pmc.ncbi.nlm.nih.gov/articles/PMC4173296)
- [Rathjen FG, Hodge R. Early Days of Tenascin-R Research. Front Immunol 2020;11:612482](https://pmc.ncbi.nlm.nih.gov/articles/PMC7820773)
- [KEGG DISEASE H03007](https://www.kegg.jp/entry/H03007)
- [MedGen UID 1794250 (NEDSTO)](https://www.ncbi.nlm.nih.gov/medgen/1794250)
- [OMIM #619653 — entry page (direct fetch returned HTTP 403; not used as a source for any claim above)](https://omim.org/entry/619653)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 41 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 41 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 69 |
| Resolved | 52 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 16 |
| Terms whose name was checked | 28 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 25 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0859212` (12 mentions) - the report calls it "HTTP 200, JSON"; MONDO calls it **neurodevelopmental disorder, nonprogressive, with spasticity and transient opisthotonus**
- `HP:0000514` (3 mentions) - the report calls it "Eye"; HP calls it **Slow saccadic eye movements**
- `HP:0008959` (3 mentions) - the report calls it "Limbs"; HP calls it **Distal upper limb muscle weakness**
- `HP:0007149` (3 mentions) - the report calls it "Limbs"; HP calls it **Distal upper limb amyotrophy**
- `HP:0001347` (3 mentions) - the report calls it "Nervous System"; HP calls it **Hyperreflexia**
- `HP:0002395` (3 mentions) - the report calls it "Nervous System"; HP calls it **Lower limb hyperreflexia**
- `HP:0007305` (5 mentions) - the report calls it "Nervous System", "CNS demyelination"; HP calls it **CNS demyelination**
- `HP:0001300` (3 mentions) - the report calls it "Nervous System"; HP calls it **Parkinsonism**
- `HP:0002188` (3 mentions) - the report calls it "Nervous System"; HP calls it **Delayed CNS myelination**
- `HP:0007325` (4 mentions) - the report calls it "Nervous System"; HP calls it **Generalized dystonia**
- `HP:0001332` (3 mentions) - the report calls it "Nervous System"; HP calls it **Dystonia**
- `HP:0033725` (3 mentions) - the report calls it "Nervous System"; HP calls it **Thin corpus callosum**
- `HP:0001263` (3 mentions) - the report calls it "Nervous System"; HP calls it **Global developmental delay**
- `HP:0001270` (3 mentions) - the report calls it "Nervous System"; HP calls it **Motor delay**
- `HP:0001266` (5 mentions) - the report calls it "Nervous System"; HP calls it **Choreoathetosis**
- `HP:0000750` (3 mentions) - the report calls it "Nervous System"; HP calls it **Delayed speech and language development**
- `HP:0001338` (3 mentions) - the report calls it "Nervous System"; HP calls it **Partial agenesis of the corpus callosum**
- `HP:0007350` (3 mentions) - the report calls it "Nervous System"; HP calls it **Upper limb hyperreflexia**
- `HP:0002540` (3 mentions) - the report calls it "Nervous System"; HP calls it **Inability to walk**
- `HP:0002186` (3 mentions) - the report calls it "Nervous System"; HP calls it **Apraxia**
- `HP:0001260` (4 mentions) - the report calls it "Nervous System"; HP calls it **Dysarthria**
- `HP:0002179` (8 mentions) - the report calls it "Musculature", "HTTP 200, JSON"; HP calls it **Opisthotonus**
- `HP:0008936` (3 mentions) - the report calls it "Musculature"; HP calls it **Axial hypotonia**
- `HP:0001285` (4 mentions) - the report calls it "Musculature"; HP calls it **Spastic tetraparesis**
- `HP:0002375` (1 mention) - the report calls it "hypokinesia; ID **not retrieved this session"; HP calls it **Hypokinesia**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `RO:0004003` (1 mention), reported as "has material basis in germline mutation in" - RO does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003593` (3 mentions) - the report calls it "Clinical course"; HP calls it **Infantile onset**
- `HP:0000007` (5 mentions) - the report calls it "Inheritance"; HP calls it **Autosomal recessive inheritance**
- `HP:0001257` (3 mentions) - the report calls it "Musculature"; HP calls it **Spasticity**, and lists "Muscular spasticity" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HGNC:11953` - called "HTTP 200, read", "HTTP 200, empty", "Gene: TNR", "Human ortholog TNR"
- `MIM:619653` - called "Neurodevelopmental disorder, nonprogressive, with spasticity and transient opisthotonus", "DISEASE: NEDSTO"
- `OMIM:619653` - called "HTTP 404, not read", "NEDSTO"
- `MGI:98501` - called "HTTP 200, read in full", "HTTP 200, but empty"
- `PubMed:8626505` - called "TISSUE SPECIFICITY: Brain specific", "Brain specific"
- `HP:0007305` - called "Nervous System", "CNS demyelination"
- `HP:0002179` - called "Musculature", "HTTP 200, JSON"
- `MGI:6156164` - called "Tnrem1(IMPC)Rbrc (homozygous; C57BL/6NJcl background)", "Tnr^em1(IMPC)Rbrc"
- `MGI:2154583` - called "Tnrtm1Msch (homozygous; involves 129P2/OlaHsd × C57BL/6J)", "Tnr^tm1Msch** (Schachner lab targeted mutation)"

### Terms the ontology service could not be reached for

1 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `MEDGEN:1794250` (2 mentions)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MIM`, `OMIM`, `MGI`, `PubMed`, `NCBIGene`, `UMLS`, `Chr1`.