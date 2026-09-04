---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-04T02:42:07.166077'
end_time: '2026-09-04T02:47:14.542076'
duration_seconds: 307.38
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Emanuel Syndrome
  mondo_id: ''
  category: Chromosomal
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
  web_search_requests: 15
  num_turns: 24
  total_cost_usd: 1.2868964000000003
  session_id: fab9582c-86c5-587f-8c13-07e30530b023
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 22
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 7
  validator_version: 0.2.1
term_validation:
  total_terms: 60
  verified: 58
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 9
  labels_mismatched: 12
  mislabelled_terms:
  - term_id: MONDO:0009301
    reported_labels:
    - Emanuel syndrome
    ontology_label: 46,XY sex reversal 7
  - term_id: HP:0011344
    reported_labels:
    - Severe intellectual disability
    ontology_label: Severe global developmental delay
  - term_id: HP:0000252
    reported_labels:
    - Universal in GeneReviews cohort
    ontology_label: Microcephaly
  - term_id: HP:0001252
    reported_labels:
    - Universal
    ontology_label: Hypotonia
  - term_id: HP:0001385
    reported_labels:
    - Common
    ontology_label: Hip dysplasia
  - term_id: HP:0000365
    reported_labels:
    - Documented feature
    ontology_label: Hearing impairment
  - term_id: HP:0002020
    reported_labels:
    - Common
    ontology_label: Gastroesophageal reflux
  - term_id: HP:0001250
    reported_labels:
    - Documented in a subset
    ontology_label: Seizure
  - term_id: GO:0007126
    reported_labels:
    - meiotic nuclear division
    ontology_label: GO_0007126
  - term_id: UBERON:0002616
    reported_labels:
    - cerebellar cortex
    ontology_label: regional part of brain
  - term_id: UBERON:0002417
    reported_labels:
    - hard palate
    ontology_label: abdominal segment of trunk
  - term_id: UBERON:0000151
    reported_labels:
    - ear
    ontology_label: pectoral fin
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0007126
    ontology_label: GO_0007126
    replaced_by: GO:0051321
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Emanuel Syndrome
- **MONDO ID:**  (if available)
- **Category:** Chromosomal

## Research Objectives

Please provide a comprehensive research report on **Emanuel Syndrome** covering all of the
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

I now have comprehensive material across all sections. Let me compile the final research report.

I have sufficient material now to compile the comprehensive report.

# Emanuel Syndrome: Comprehensive Research Report

## 1. Disease Information

### Overview

Emanuel syndrome (ES), also known as supernumerary der(22)t(11;22) syndrome or "derivative 22 syndrome," is a constitutional genomic disorder caused by the presence of an extra (supernumerary) marker chromosome — a derivative chromosome 22 [der(22)] — that carries duplicated segments from the long arms of both chromosome 11 and chromosome 22. This produces partial trisomy for 11q23-qter and partial trisomy for 22q11 (specifically the proximal 22q11.1–22q11.21 region), superimposed on the normal diploid chromosome complement (47 chromosomes total: two normal 11s, two normal 22s, plus the der(22) marker) (GeneReviews, NBK1263; OMIM #609029).

The condition is characterized by severe-to-profound intellectual disability, characteristic craniofacial dysmorphism (micrognathia/microretrognathia, hooded eyelids, up- or down-slanting palpebral fissures, deep-set eyes, low-hanging columella, long philtrum, ear anomalies with preauricular tags/pits), congenital heart defects, renal anomalies, cleft/high-arched palate, hypotonia, and pre- and postnatal growth deficiency (Orphanet ORPHA:96170; NORD; GeneReviews).

### Key Identifiers
- **OMIM:** #609029 (added November 2004)
- **Orphanet:** ORPHA:96170
- **MONDO:** MONDO:0009301 (Emanuel syndrome)
- **GeneReviews:** NBK1263 (Emanuel & Boyar, first published 2007, periodically updated)
- **ICD-10:** Q92.8 / Q95.1 (chromosomal abnormality NEC, balanced rearrangement/derivative chromosome — not separately coded)

### Synonyms
- Supernumerary der(22)t(11;22) syndrome
- Derivative 22 syndrome / der(22) syndrome
- Supernumerary der(22) syndrome
- +der(22)t(11;22)(q23;q11.2) syndrome
- t(11;22) syndrome
- Partial trisomy 11q/partial trisomy 22 syndrome (older nomenclature)

### Data Source Type
The overwhelming majority of published knowledge on Emanuel syndrome derives from **aggregated case-series and cohort reports** rather than large-scale EHR data — a natural consequence of its rarity. The GeneReviews chapter synthesizes data from "well over 400 individuals" reported in the literature (Carter et al. 2009 phenotypic delineation of 63 individuals is the largest single cohort; Ohye et al. 2014 provides Japanese national surveillance/registry-based prevalence data). Some more recent findings (e.g., ZAP70 differential expression) derive from reanalysis of public transcriptomic datasets (GEO GSE13122).

**Sources:**
- [Emanuel Syndrome - GeneReviews®](https://www.ncbi.nlm.nih.gov/books/NBK1263/)
- [OMIM #609029 - EMANUEL SYNDROME](https://omim.org/entry/609029)
- [Orphanet: Emanuel syndrome](https://www.orpha.net/en/disease/detail/96170)
- [NORD - Emanuel syndrome](https://rarediseases.org/mondo-disease/emanuel-syndrome/)

---

## 2. Etiology

### Disease Causal Factors — Genetic (Chromosomal)

Emanuel syndrome is caused exclusively by a **chromosomal structural rearrangement**: unbalanced 3:1 meiotic malsegregation of a parental balanced reciprocal translocation, t(11;22)(q23.3;q11.2). This is not a single-gene disorder but a **contiguous gene/segmental dosage disorder** driven by trisomic gene dosage across the duplicated 11q23-qter and 22q11 segments.

- **In >99% of cases**, one parent is a phenotypically normal balanced carrier of t(11;22)(q23;q11.2) (GeneReviews).
- t(11;22)(q23;q11.2) is **the most common recurrent non-Robertsonian reciprocal translocation in humans**, arising independently and recurrently in the population due to a shared genomic architecture rather than being inherited from a common ancestor in most families.
- A minority of cases arise from **de novo formation** of the translocation or, rarely, from other complex/unusual segregation patterns (e.g., 3:1 malsegregation of a paternal complex rearrangement, or unusual non-Robertsonian events producing a similar unbalanced karyotype — see PMC8962060, t(20;22) case).

### Genetic Risk Factors

- **Parental balanced t(11;22) carrier status** is the dominant, essentially sole, genetic risk factor.
- **Sex-of-transmitting-parent effect:** recurrence/live-birth risk of an unbalanced conceptus is **higher when the mother is the carrier than when the father is the carrier** (GeneReviews) — consistent with differential selection against unbalanced gametes/embryos in spermatogenesis versus oogenesis.
- **Molecular basis for translocation formation (not transmission) risk:** the palindromic AT-rich repeat (PATRR) sequences at 11q23 (PATRR11) and 22q11 (PATRR22) predispose these loci to double-strand breaks via hairpin/cruciform extrusion, explaining why this exact translocation recurs independently across unrelated families rather than being a single ancient founder event (Kurahashi & Emanuel, Hum Mol Genet 2001, PMID cited in search results; Kato et al., PMC4940405).

### Environmental Risk Factors
No environmental, toxin, infectious, or lifestyle risk factors have been identified for the formation or transmission of the t(11;22) translocation or for Emanuel syndrome. As with other chromosomal rearrangement disorders, there is no established association with parental age (unlike trisomy from nondisjunction such as Down syndrome), smoking, or teratogen exposure.

### Protective Factors
- **Genetic:** None specific to Emanuel syndrome are described; the "protective" event during gametogenesis is production of a balanced, normal, or non-viable unbalanced gamete rather than the specific 3:1 malsegregant that produces a viable der(22).
- **Environmental/Reproductive:** **Preimplantation genetic testing for structural rearrangements (PGT-SR)** functions as a reproductive/preventive intervention for known carrier couples, allowing selection of balanced or normal embryos for transfer (see Section 13, Prevention).

### Gene-Environment Interactions
None reported; this is a purely chromosomal mechanism with no known gene-environment interaction contributing to occurrence or severity.

**Sources:**
- [GeneReviews NBK1263](https://www.ncbi.nlm.nih.gov/books/NBK1263/)
- [Kurahashi & Emanuel — palindrome-mediated translocation mechanism, PMC4940405](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4940405/)
- [Supernumerary derivative 22 from novel non-Robertsonian translocation t(20;22), PMC8962060](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8962060/)

---

## 3. Phenotypes

Emanuel syndrome phenotypes are drawn primarily from GeneReviews (NBK1263, synthesizing >400 published cases) and the Carter et al. 63-individual phenotypic delineation study, supplemented by Orphanet and case reports.

| Phenotype | Frequency | HPO Term (suggested) |
|---|---|---|
| Severe developmental delay / intellectual disability | ~100% (universal) | HP:0011344 (Severe intellectual disability) |
| Pre- and postnatal growth deficiency | Common/near-universal | HP:0001511 (Intrauterine growth retardation), HP:0004325 (Decreased body weight) |
| Microcephaly | Universal in GeneReviews cohort | HP:0000252 |
| Hypotonia (centrally based) | Universal | HP:0001252 |
| Micrognathia/microretrognathia | ~60% | HP:0000347 |
| Preauricular tags/pits, ear anomalies | ~76% (ear pits) | HP:0000384 (Preauricular skin tag), HP:0004467 (Preauricular pit) |
| Cleft or high-arched palate | ~50–54% | HP:0000175 (Cleft palate), HP:0002705 (High palate) |
| Congenital heart defects (ASD, VSD, tetralogy of Fallot, others) | ~60% | HP:0001629 (ASD), HP:0001629/HP:0001636 (VSD), HP:0001636, HP:0001636 |
| Renal/kidney malformations | ~30% | HP:0000077 (Abnormality of the kidney) |
| Anal atresia | ~20% | HP:0002023 |
| Genital abnormalities (males): cryptorchidism, micropenis | Frequent in males | HP:0000028 (Cryptorchidism), HP:0000054 (Micropenis) |
| Hip dysplasia | Common | HP:0001385 |
| Hearing loss | Documented feature | HP:0000365 |
| Hooded eyelids, deep-set eyes, up/down-slanting palpebral fissures | Common facial gestalt | HP:0000414 (hooded eyelid), HP:0000490 (deep-set eyes), HP:0000582/HP:0000601 |
| Long philtrum, low-hanging columella | Common | HP:0000343, HP:0009914 |
| Feeding difficulties / failure to thrive | Common in infancy | HP:0011968, HP:0001508 |
| Gastroesophageal reflux, aspiration risk | Common | HP:0002020 |
| Seizures / abnormal EEG | Documented in a subset | HP:0001250 |
| Structural brain anomalies (corpus callosum hypoplasia/maldevelopment, cerebellar hypoplasia, infratentorial involution) | Reported in imaging studies | HP:0002079 (CC hypoplasia), HP:0001321 (cerebellar hypoplasia) |
| Immunologic abnormalities (immunoglobulin deficiency, thymic-dependent immunodeficiency) | Reported subset | HP:0002721 |

### Onset, Severity, Progression
- **Onset:** Congenital — features are present from birth (growth deficiency often detectable prenatally), with developmental delay becoming evident in infancy.
- **Severity:** Uniformly severe with respect to cognitive/developmental outcome ("adults function in the spectrum of severe-to-profound intellectual disability" — GeneReviews); somatic malformation burden (cardiac, renal, palate) is variable across individuals.
- **Progression:** Largely **stable/static** developmental disability rather than progressive/degenerative; medical complications (cardiac, renal, respiratory) drive most of the morbidity and mortality risk, concentrated in infancy.
- **Course:** Most affected individuals achieve independent sitting; "only a small number learn to walk" (GeneReviews). Expressive verbal language is typically very limited, often requiring augmentative/alternative communication.

### Quality of Life Impact
Structured EQ-5D/SF-36-type QOL instruments have not been specifically validated in Emanuel syndrome cohorts (a common gap for ultra-rare chromosomal disorders). Qualitatively, quality of life is shaped by: severe communication limitation (requiring AAC), motor limitation (majority non-ambulatory), recurrent medical/surgical needs (cardiac, GI, orthopedic), and dependence on caregivers for all activities of daily living — consistent with parent/caregiver-reported burden captured by advocacy organizations (emanuelsyndrome.org) rather than formal psychometric QOL studies in the peer-reviewed literature.

**Sources:**
- [GeneReviews NBK1263](https://www.ncbi.nlm.nih.gov/books/NBK1263/)
- [Phenotypic Delineation of Emanuel Syndrome: Clinical Features of 63 Individuals](https://www.researchgate.net/publication/26674827_Phenotypic_Delineation_of_Emanuel_Syndrome_Supernumerary_Derivative_22_Syndrome_Clinical_Features_of_63_Individuals)
- [Derivative 11;22 (Emanuel) Syndrome: A Case Report and Review, PMC3652044](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3652044/)
- [Emanuel syndrome due to unusual pattern, Egypt J Med Hum Genet 2024](https://link.springer.com/article/10.1186/s43042-024-00494-6)

---

## 4. Genetic/Molecular Information

### Causal Chromosomal Abnormality
- **Karyotype:** 47,XX or XY,+der(22)t(11;22)(q23;q11.2)pat/mat
- The der(22) is a **supernumerary marker chromosome** consisting of the centromere and proximal short/long arm of chromosome 22, fused to distal 11q material, resulting in:
  - **Partial trisomy for 11q23→qter** (distal long arm of chromosome 11)
  - **Partial trisomy for 22q11.1→22q11.21** (proximal long arm of chromosome 22, specifically the region duplicated in "22q11 duplication syndrome" and overlapping the DiGeorge/velocardiofacial critical region)
- This is **not a simple reciprocal translocation** producing two derivative chromosomes replacing normal homologs (which would be balanced); Emanuel syndrome results when the **der(22) is retained as a THIRD, extra chromosome** alongside two structurally normal pairs of chromosomes 11 and 22 (46 + 1 = 47 chromosomes total), via 3:1 meiotic segregation of the parental balanced quadrivalent.

### Breakpoint Region / Molecular Mechanism (PATRR11/PATRR22)
- The t(11;22)(q23;q11.2) translocation breakpoints cluster within **palindromic AT-rich repeats (PATRRs)** — PATRR11 on chromosome 11q23 and PATRR22 on chromosome 22q11 — long, near-perfect palindromic sequences capable of forming hairpin/cruciform secondary structures in single- or double-stranded DNA.
- These non-B DNA structures are thought to be substrates for **double-strand breaks**, which are then repaired via **illegitimate (non-homologous) recombination** joining 11q23 to 22q11, producing the recurrent, nearly identical breakpoint (breakpoints differ by only a few nucleotides across unrelated families) (Kurahashi & Emanuel 2001; Kato et al., PMC4940405; PMID:17264116 — cruciform extrusion propensity studies).
- This palindrome-mediated mechanism explains why t(11;22) is the **most frequent recurrent non-Robertsonian translocation in humans**, arising independently in many families rather than through common descent.

### Genes in the Duplicated Regions and Dosage-Sensitive Candidates
- The duplicated 22q11 segment (22q10-22q11) **overlaps the 22q11.2 deletion/duplication (DiGeorge/velocardiofacial) critical region**, sharing an approximately **1.5-Mb region of overlap** with classic VCFS/DiGeorge syndrome (der(22) syndrome and VCFS/DGS share this 1.5-Mb overlap — ScienceDirect/Am J Hum Genet).
  - **TBX1** (T-box transcription factor 1) lies in this region and is the leading candidate dosage-sensitive gene for the cardiac (conotruncal) and craniofacial phenotype: TBX1 haploinsufficiency is the major driver of DiGeorge/VCFS deletion phenotypes, and reciprocal TBX1 dosage increase (as in 22q11.2 duplication syndrome and, by extension, the duplicated segment on der(22)) has been shown in mouse models to produce **congenital heart disease resembling the 22q11.2 duplication phenotype** by disrupting the normal anterior heart field gene-expression balance (Hum Mol Genet 2018).
  - **HIRA**, also within this region, is independently predicted to be haploinsufficient/dosage-sensitive and is implicated in chromatin/nucleosome assembly relevant to cardiac and craniofacial development in the DiGeorge/VCFS spectrum.
- The duplicated distal 11q23-qter segment is gene-dense but no single "master" dosage-sensitive gene has been definitively established for the 11q-related phenotypic contribution; the phenotype is generally attributed to **combined trisomic dosage effects across many genes** in both segments rather than a single causal gene (unlike, e.g., Down syndrome's DSCR).
- **ZAP70** (Zeta-chain-associated protein kinase 70) was recently identified via bioinformatic differential-expression/WGCNA analysis of a public transcriptomic dataset (GEO GSE13122; 9 balanced-carrier, 4 Emanuel syndrome, 13 control samples) as significantly upregulated in Emanuel syndrome fetal samples and proposed as a **candidate noninvasive prenatal screening (NIPS) biomarker**; ZAP70 is a protein kinase implicated in spindle assembly/chromosome segregation in oocytes, mechanistically connecting it to the meiotic malsegregation origin of the disorder (Hu, Wang, Xiang, *Biochem Genet* 2024, PMID:38687434).

### Variant Classification / Population Frequency
- This is a **structural chromosomal rearrangement**, not a point variant, so standard ACMG/AMP SNV classification and gnomAD-style allele-frequency data do not apply.
- **Balanced t(11;22) carrier population prevalence is unknown** but is inferred to be relatively common among identified reciprocal translocations given how frequently the unbalanced (Emanuel syndrome) and balanced forms recur across unrelated ascertainments worldwide.
- **Somatic vs. germline:** Constitutional (germline) only; no described role in acquired/somatic disease.
- **Functional consequence:** Copy-number/dosage-gain (trisomic dosage) of genes within the two duplicated segments — a gene-dosage-imbalance mechanism analogous to other partial-trisomy/segmental duplication syndromes, rather than loss-of-function or dominant-negative single-gene mechanisms.

### Epigenetics
No Emanuel-syndrome-specific epigenetic (DNA methylation/histone modification) studies were identified in the literature search; this remains an unexplored area for this disorder.

**Sources:**
- [Der(22) Syndrome and VCFS/DiGeorge Syndrome Share a 1.5-Mb Region of Overlap on Chromosome 22q11, Am J Hum Genet](https://www.sciencedirect.com/science/article/pii/S0002929707617121)
- [Dysregulation of TBX1 dosage in the anterior heart field, Hum Mol Genet 2018](https://academic.oup.com/hmg/article/27/11/1847/4917554)
- [ZAP70: differential expression analysis for Emanuel syndrome, PMC12144060](https://pmc.ncbi.nlm.nih.gov/articles/PMC12144060/)
- [Kurahashi/Kato palindrome-mediated translocation, PMC4940405](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4940405/)

---

## 5. Environmental Information

No environmental toxins, occupational exposures, infectious agents, or lifestyle factors have been identified as causal or contributory to Emanuel syndrome. As a purely constitutional chromosomal-rearrangement disorder with a well-characterized meiotic origin (3:1 malsegregation of a parental balanced translocation via a PATRR-mediated recurrent breakpoint), there is no evidence base implicating CTD-catalogued chemicals, radiation, maternal illness, or infection in either translocation formation or in modifying phenotypic expression/severity in affected individuals. This is consistent with the broader literature on recurrent PATRR-mediated translocations (e.g., t(11;22)), which are attributed to intrinsic sequence-driven genomic instability rather than exogenous mutagenic exposure.

---

## 6. Mechanism / Pathophysiology

### Ordered Causal Chain

1. A **PATRR11–PATRR22 palindromic AT-rich repeat pair** at 11q23 and 22q11 is intrinsically prone to forming hairpin/cruciform secondary DNA structures during meiosis. → *This leads to* double-strand DNA breaks at these loci.
2. Illegitimate, non-homologous repair of these breaks joins 11q23 material to 22q11 material (and vice versa) in one parental germ cell lineage. → *This results in* formation of a **balanced reciprocal translocation, t(11;22)(q23;q11.2)**, in that parent (who is phenotypically normal because no genetic material is gained or lost — this step can also occur de novo in the proband's own lineage, but is inherited from a carrier parent in >99% of Emanuel syndrome cases).
3. During gametogenesis in the balanced carrier parent, the four translocation-involved chromosomes (normal 11, normal 22, der(11), der(22)) form a **quadrivalent** at meiosis I and can segregate in multiple ways, including the abnormal **3:1 pattern** (three chromosomes to one gamete, one to the other) rather than the normal 2:2 pattern. → *This leads to* production of a gamete carrying an extra der(22) chromosome alongside a normal haploid set.
4. Fertilization by a normal gamete produces a **conceptus with 47 chromosomes**: two normal 11s, two normal 22s, plus the supernumerary der(22). → *This results in* **partial trisomy for distal 11q (11q23→qter) and partial trisomy for proximal 22q11** simultaneously, in every cell of the embryo (constitutional, not mosaic, in the great majority of cases). Note: this specific 3:1 outcome is the *rarer* viable unbalanced product among several theoretically possible segregation outcomes of the quadrivalent — most other unbalanced products (e.g., trisomy 11q only, monosomy patterns) are not compatible with term survival, which is why Emanuel syndrome (the der(22)-supernumerary product specifically) is the unbalanced outcome actually observed in liveborn infants; competing outcomes are lost predominantly to early miscarriage (spontaneous abortion risk 23–37% is elevated in these pregnancies overall).
5. Trisomic gene dosage across the duplicated 22q11 segment — which overlaps the DiGeorge/VCFS 1.5-Mb critical region containing **TBX1** and **HIRA** — disrupts the normal balance of anterior heart field transcriptional programs. → *This leads to* (inferred from mouse TBX1-dosage models, extrapolated to human trisomic dosage) **conotruncal and septal congenital heart defects** (ASD, VSD, tetralogy of Fallot), and contributes to the **craniofacial dysmorphism and palatal anomalies** that phenocopy features of 22q11.2 duplication syndrome.
6. Combined trisomic dosage across the gene-dense duplicated 11q23-qter segment (no single dominant gene identified) acts in parallel, and together with the 22q11 dosage effect → *results in* **global neurodevelopmental disruption** (severe intellectual disability, hypotonia, microcephaly), **growth deficiency** (pre- and postnatal), **renal maldevelopment**, and **genital anomalies** in males — the multisystem congenital malformation pattern characteristic of Emanuel syndrome. The mechanistic link from specific 11q23-qter genes to each of these individual organ phenotypes is **largely inferred from the deletion/duplication-syndrome dosage paradigm** rather than gene-by-gene demonstrated in Emanuel syndrome itself; this is an area with a genuine knowledge gap (no systematic 11q gene-phenotype dissection has been published for this disorder).
7. In a subset of cases, disrupted spindle assembly/chromosome segregation machinery (implicated via **ZAP70** upregulation, a kinase normally regulating oocyte spindle assembly) may reflect a downstream transcriptional signature of, or contributor to, the meiotic malsegregation event itself — this is a recent hypothesis-generating finding (2024) rather than an established causal step, proposed chiefly as a biomarker rather than a mechanistic driver of the postnatal phenotype.

### Molecular Pathways
- **TBX1/anterior heart field transcriptional network** — implicated in cardiac outflow tract and craniofacial development (GO:0003170 heart valve development-adjacent pathways; anterior heart field specification). Dosage disruption (both loss in DiGeorge and gain in duplication/Emanuel) perturbs this network.
- No KEGG/Reactome pathway is specifically annotated to "Emanuel syndrome"; pathway involvement is inferred from the overlapping 22q11.2 deletion/duplication syndrome literature.

### Cellular Processes
- **Meiotic chromosome segregation defect** (upstream, in parental gametogenesis) — GO:0007126 (meiotic nuclear division), GO:0051321 (meiotic cell cycle).
- **Dosage-driven transcriptional dysregulation** in developing tissues (heart, craniofacial mesenchyme, kidney, brain) — downstream, in the conceptus.
- **Neurodevelopmental process disruption** contributing to intellectual disability and hypotonia (largely inferred by analogy to other segmental-dosage neurodevelopmental disorders; not specifically dissected at the cellular level in Emanuel syndrome).

### Protein Dysfunction
- Not a "misfolding" or single-protein-dysfunction disorder; the pathophysiology is **gene-dosage** (too much of many gene products simultaneously), not altered protein structure/function of any single protein.

### Tissue Damage / Structural Anomalies
- Cardiac septal and outflow-tract malformation (structural, developmental — not degenerative).
- Renal dysplasia/malformation.
- CNS structural anomalies on imaging: cerebellar hypoplasia, infratentorial brain involution, maldeveloped/hypoplastic corpus callosum, reported in a subset of neuroimaging case series.

### Immune System Involvement
Given the overlap with the DiGeorge/VCFS 22q11 critical region (a region whose *deletion* causes thymic aplasia and T-cell immunodeficiency in classic DiGeorge syndrome), a subset of Emanuel syndrome patients have documented **immunoglobulin deficiency and thymic-dependent immunodeficiency** — plausibly reflecting a dosage effect on the same 22q11 developmental pathway (thymic/parathyroid organogenesis), though this is less systematically characterized than in deletion-type 22q11.2 syndrome.

### Molecular Profiling
- **Transcriptomics:** GEO dataset GSE13122 has been used for differential expression analysis comparing Emanuel syndrome, balanced-carrier, and control samples (Hu et al. 2024), identifying ZAP70 and other hub genes via WGCNA/Lasso regression — this is the only systematic transcriptomic characterization identified in the literature search.
- **Proteomics, metabolomics, lipidomics, single-cell, spatial transcriptomics:** No disease-specific studies identified; this represents an unexplored area for Emanuel syndrome, consistent with its status as an ultra-rare disorder with limited tissue-availability for such studies.

**Suggested GO terms:** GO:0007126 (meiotic nuclear division), GO:0000724 (double-strand break repair via homologous recombination — for contrast with illegitimate/non-homologous repair implicated here), GO:0003007 (heart morphogenesis), GO:0060412 (ventricular septum morphogenesis).
**Suggested CL terms:** CL:0000746 (cardiac muscle cell), CL:0002327 (mammary luminal progenitor cell — N/A), more relevantly CL:0000000-level developmental progenitor populations of anterior heart field and neural crest-derived craniofacial mesenchyme (no single well-established CL term captures "anterior heart field cell" precisely; UBERON:0003922 anterior heart field is the anatomical structure term).

**Sources:**
- [Dysregulation of TBX1 dosage, Hum Mol Genet 2018](https://academic.oup.com/hmg/article/27/11/1847/4917554)
- [Der(22)/VCFS 1.5-Mb overlap, Am J Hum Genet](https://www.sciencedirect.com/science/article/pii/S0002929707617121)
- [ZAP70 hub gene analysis, PMC12144060](https://pmc.ncbi.nlm.nih.gov/articles/PMC12144060/)
- [Kurahashi & Emanuel PATRR mechanism, PMC4940405](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4940405/)

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary:** Heart (conotruncal/septal defects), kidney (structural malformation), craniofacial skeleton/palate, brain (microcephaly, structural anomalies), external ear, genitalia (males).
- **Secondary/complications:** Respiratory system (aspiration risk secondary to swallowing dysfunction and cleft palate), musculoskeletal system (hip dysplasia secondary to hypotonia/joint laxity), gastrointestinal tract (anal atresia, gastroesophageal reflux).
- **Body systems involved:** Cardiovascular, renal/urinary, craniofacial/skeletal, nervous (central), digestive, genitourinary (male), immune (subset), auditory.

### Tissue and Cell Level
- Cardiac septal and outflow-tract tissue (neural-crest-derived and second heart field-derived mesenchyme; UBERON:0003922 anterior heart field, UBERON:0002094 outflow tract).
- Palatal shelf mesenchyme (cleft/high palate).
- Renal parenchyma (dysplastic/malformed kidney tissue; UBERON:0002113 kidney).
- CNS gray/white matter, cerebellum, corpus callosum (UBERON:0002616 cerebellar cortex; UBERON:0002336 corpus callosum).
- Skeletal muscle (generalized hypotonia; UBERON:0001134 skeletal muscle tissue).

### Subcellular Level
No subcellular/organelle-specific pathology has been described; the mechanism is chromosomal/genomic (nuclear, GO:0005634) rather than involving a specific organelle dysfunction (e.g., mitochondria, lysosome).

### Localization
- Craniofacial anomalies are typically **bilateral/symmetric** (facial gestalt); ear anomalies (preauricular tags/pits) may be unilateral or bilateral.
- Cardiac defects are structural/midline-related (septal defects) rather than laterality-defect syndromes.
- No described laterality (situs) defects.

**Suggested UBERON terms:** UBERON:0000948 (heart), UBERON:0002113 (kidney), UBERON:0001456 (face), UBERON:0002417 (hard palate), UBERON:0002616 (cerebellar cortex), UBERON:0002336 (corpus callosum), UBERON:0000151 (ear).

---

## 8. Temporal Development

### Onset
- **Congenital** in all cases — the chromosomal imbalance is present from conception; growth deficiency is often detectable **prenatally** (intrauterine growth restriction, nuchal translucency thickening reported on first-trimester screening in some cases — PMC12527601).
- Developmental delay and hypotonia typically become clinically evident in **early infancy**.

### Progression
- Not a progressive/degenerative disorder in the classic sense; the underlying genomic imbalance is static and present in every cell from conception.
- **Disease course pattern:** Chronic, lifelong, non-progressive with respect to the core neurodevelopmental disability; medically, the **highest-risk period is the first months of life**, when life-threatening structural malformations (cardiac, potentially with associated conditions such as congenital diaphragmatic hernia in rare co-occurring cases) drive most mortality.
- Beyond infancy, the disease course stabilizes into **chronic, lifelong severe-to-profound intellectual disability** with ongoing but generally non-escalating medical management needs (feeding, orthopedic, audiologic, ophthalmologic).

### Patterns
- No spontaneous or treatment-induced remission (this is a structural/dosage disorder, not a relapsing-remitting condition).
- **Critical period for intervention:** the neonatal/infancy period for surgical correction of life-threatening cardiac and gastrointestinal anomalies (e.g., anal atresia repair, cardiac surgery), and early childhood for initiation of intensive developmental therapies (physical/occupational/speech, AAC) to optimize functional outcome.

**Sources:**
- [GeneReviews NBK1263](https://www.ncbi.nlm.nih.gov/books/NBK1263/)
- [Emanuel Syndrome: A Case Report with Isolated Nuchal Translucency Thickening, PMC12527601](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12527601/)

---

## 9. Inheritance and Population

### Epidemiology
- **Theoretical/estimated prevalence:** ~**1 in 110,000** live births, based on Japanese national theoretical-frequency and surveillance data (Ohye et al., *Pediatrics International* 2014, vol 56, pp 462–466).
- **Case count:** "Well over 400 individuals" reported in the medical literature to date (GeneReviews); true population prevalence is otherwise stated as "unknown" by GeneReviews given ascertainment limitations for a condition this rare.
- Balanced t(11;22) carrier frequency in the general population is **unknown** but presumed non-negligible given how often the unbalanced (Emanuel) and balanced forms are independently ascertained worldwide via recurrent, sequence-driven translocation formation.

### Inheritance Pattern
- Chromosomal (not classic Mendelian); functionally behaves as an **autosomal, unbalanced structural rearrangement** transmitted from a balanced-translocation-carrier parent via abnormal 3:1 meiotic segregation.
- **>99% of Emanuel syndrome probands have a parent who is a balanced t(11;22)(q23;q11.2) carrier** (GeneReviews); a minority arise de novo.
- In most familial cases, the carrier parent inherited the translocation from a parent, i.e., the balanced translocation itself can be transmitted stably across generations in a family (as a balanced state) before eventually producing an unbalanced (Emanuel syndrome) conceptus in a given generation.

### Penetrance / Expressivity
- The **unbalanced chromosomal state (der(22) supernumerary) is fully "penetrant"** for the Emanuel syndrome phenotype — i.e., essentially all liveborn individuals with the characteristic +der(22)t(11;22) karyotype manifest the syndrome, though **expressivity is variable** across organ systems (e.g., not all patients have cardiac defects [~60%] or renal anomalies [~30%] or cleft palate [~50%]), while the core neurodevelopmental/growth/craniofacial features are near-universal.
- **Balanced carriers are phenotypically normal** (complete "non-penetrance" of the balanced state itself, aside from reproductive risk).

### Genetic Anticipation
Not applicable — this is a structural chromosomal rearrangement, not a repeat-expansion disorder; there is no described anticipation phenomenon.

### Germline Mosaicism
Rare/atypical parental mosaicism for the translocation has been reported as a mechanism in a minority of families where recurrence occurs despite an apparently normal parental karyotype on standard testing, though this is not the predominant mechanism (most carrier parents show a full, non-mosaic balanced translocation on karyotype).

### Founder Effects
No founder effect has been established; t(11;22) is understood to arise **recurrently and independently** in unrelated families worldwide due to the intrinsic PATRR-mediated genomic instability at the 11q23/22q11 loci, rather than through descent from a common ancestral rearrangement event. This is a defining and somewhat unusual feature relative to most "founder" chromosomal syndromes.

### Consanguinity
No specific role for consanguinity is described (mechanism is unrelated to autosomal recessive single-gene inheritance).

### Recurrence Risk (Carrier Couples)
- **Live-born infant with Emanuel syndrome:** 1.8%–5.6% per pregnancy for a known balanced-carrier parent (GeneReviews), with risk **higher when the mother is the carrier**.
- **Spontaneous abortion risk** in these pregnancies: 23%–37%.
- **Unaffected siblings of a proband:** ~50% chance of being a balanced translocation carrier themselves; ~50% chance of normal chromosomes.

### Population Demographics
- No specific ethnic, geographic, or racial predilection has been established; cases have been reported worldwide across diverse populations.
- **Sex ratio:** No strong sex bias in occurrence has been reported (autosomal mechanism); however, genital anomalies are specifically observed in **affected males** (cryptorchidism, micropenis) as part of the phenotype, not as a differential occurrence rate between sexes.
- **Age distribution:** Ascertained predominantly in infancy/early childhood at diagnosis; survival into adulthood is documented, with some reported patients living **more than 50 years**.

**Sources:**
- [Ohye et al. — Prevalence of Emanuel syndrome, Pediatr Int 2014](https://onlinelibrary.wiley.com/doi/10.1111/ped.12437)
- [GeneReviews NBK1263](https://www.ncbi.nlm.nih.gov/books/NBK1263/)
- [Emanuel Syndrome FAQ — emanuelsyndrome.org](https://emanuelsyndrome.org/emanuel-syndrome/commonly-asked-questions-faq/)

---

## 10. Diagnostics

### Clinical/Cytogenetic Tests
| Test | Sensitivity/Utility |
|---|---|
| **Conventional karyotype (G-banding)** | Detects the supernumerary der(22) marker chromosome; ~100% sensitivity for the gross abnormality, though may require follow-up FISH to confirm origin |
| **Chromosomal microarray analysis (CMA)** — oligonucleotide or SNP array | ~100% sensitivity; identifies and precisely sizes the 11q and 22q copy-number gains |
| **FISH** with probes targeting 22q11 and 11q23 | 100% sensitivity when probes for **both** regions are used; confirms the dual-segment composition of the der(22) |
| **Diagnostic hallmark** | Duplication of 22q10-22q11 **and** duplication of 11q23-qter co-occurring on a single supernumerary derivative chromosome 22 |

### Prenatal Diagnostics
- **cfDNA (NIPS) screening**: retrospective laboratory experience shows cfDNA screening can detect Emanuel syndrome and other unbalanced products of conception in known t(11;22) carrier pregnancies (PMC10606745), though it is not a substitute for diagnostic testing.
- **ZAP70 expression** in maternal peripheral blood has been proposed (2024, hypothesis-generating) as a potential future noninvasive biomarker, but is not yet clinically validated or implemented.
- **Ultrasound findings:** IUGR, and case reports describe **isolated nuchal translucency thickening** detected on first-trimester screening prompting diagnostic workup (PMC12527601).
- Amniocentesis/CVS with karyotype/FISH/CMA remains the diagnostic standard for confirming or excluding Emanuel syndrome in a known carrier pregnancy.

### Genetic Testing Strategy
- **Family history of a known t(11;22) balanced carrier parent:** targeted karyotype/FISH is the recommended first-line diagnostic approach in the fetus/newborn.
- **De novo/unexplained developmental delay presentation:** CMA is typically first-line for undiagnosed developmental delay generally, and would detect the 11q/22q copy-number gain; karyotype is then used to characterize the structural configuration (supernumerary marker vs. other mechanism) and to test parents for a balanced translocation.
- Once a proband is diagnosed, **parental karyotyping is essential** to determine recurrence risk and identify at-risk extended family members (for cascade/carrier testing).

### Clinical Criteria and Differential Diagnosis
No formal consensus diagnostic clinical-criteria scoring system (akin to DSM/ICD criteria sets) exists for Emanuel syndrome — diagnosis is definitively cytogenetic/molecular, with clinical features prompting the genetic workup. **Differential diagnoses** to consider given phenotypic overlap include:
- 22q11.2 deletion syndrome (DiGeorge/VCFS) and 22q11.2 duplication syndrome (phenotypic overlap via the shared 1.5-Mb region)
- Other supernumerary marker chromosome syndromes
- Other multiple congenital anomaly/intellectual disability syndromes with overlapping craniofacial gestalt (e.g., Smith-Magenis, Cornelia de Lange) — distinguished definitively by karyotype/CMA.

### Screening
- No population-based newborn screening program exists for Emanuel syndrome (as with virtually all rare structural chromosomal syndromes).
- **Targeted carrier/cascade screening** is recommended for relatives of a known balanced t(11;22) carrier, and **prenatal diagnostic testing** is offered to known carrier couples in subsequent pregnancies.

**Sources:**
- [GeneReviews NBK1263 — Testing section](https://www.ncbi.nlm.nih.gov/books/NBK1263/)
- [Prenatal cfDNA Screening for Emanuel Syndrome, PMC10606745](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10606745/)
- [Emanuel Syndrome: Isolated Nuchal Translucency Thickening, PMC12527601](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12527601/)

---

## 11. Outcome/Prognosis

### Survival and Mortality
- **True population life expectancy is unknown**, but mortality risk is **highest in the first months of life**, driven by life-threatening congenital malformations (predominantly cardiac).
- In one published cohort analysis: **17/21 patients (80.95%) died at pediatric age**, **3/21 (14.28%) died at adult age**, and 1 (4.76%) had unknown age at death; **mortality was attributed to cardiac causes in 71.42%** of deaths.
- **Survival into adulthood is well documented**, including reported individuals **living more than 50 years**, particularly with modern surgical/medical management of the cardiac and other structural anomalies.
- With improved neonatal and pediatric cardiac/surgical care and time, survival prospects for infants who survive the neonatal period improve substantially.

### Morbidity and Function
- **Uniform severe-to-profound intellectual disability** in surviving adults.
- Majority achieve independent sitting; **only a minority learn to walk independently**.
- **Verbal communication is typically very limited**, commonly requiring augmentative and alternative communication strategies.
- No validated disease-specific quality-of-life instrument has been applied in the literature; functional outcome data are largely descriptive/qualitative from case series.

### Disease Course / Complications
- Major complications requiring ongoing management: recurrent respiratory issues (aspiration risk from swallowing dysfunction), orthopedic complications (hip dysplasia), gastrointestinal issues (reflux, feeding difficulty, post-surgical sequelae of anal atresia repair), sensory impairment (hearing loss, ophthalmologic issues requiring monitoring), and in a subset, seizure disorders.
- **Congenital diaphragmatic hernia** has been reported as a co-occurring, life-threatening complication in a subset of cases (systematic review, ScienceDirect, S0022346821007776).

### Prognostic Factors
- **Presence and severity of congenital heart disease** is the dominant prognostic determinant for early mortality.
- Presence of additional major structural anomalies (renal, gastrointestinal) compounds perioperative and long-term medical risk.
- No molecular/biomarker-based prognostic stratification currently exists.

**Sources:**
- [GeneReviews NBK1263 — Prognosis](https://www.ncbi.nlm.nih.gov/books/NBK1263/)
- [Emanuel syndrome due to unusual pattern — mortality cohort data, Egypt J Med Hum Genet 2024](https://link.springer.com/article/10.1186/s43042-024-00494-6)
- [Emanuel syndrome and congenital diaphragmatic hernia: systematic review](https://www.sciencedirect.com/science/article/abs/pii/S0022346821007776)
- [Emanuel Syndrome FAQ](https://emanuelsyndrome.org/emanuel-syndrome/commonly-asked-questions-faq/)

---

## 12. Treatment

There is **no disease-modifying or curative treatment** for Emanuel syndrome — management is entirely **multidisciplinary, supportive, and directed at individual malformations and complications**, per GeneReviews management guidelines.

### Diagnostic/Screening Evaluations at Diagnosis (Baseline Workup)
- Cardiac echocardiography
- Renal ultrasound
- Orthopedic evaluation (hip dysplasia screening)
- Audiology evaluation
- Ophthalmologic evaluation
- Palatal/ENT assessment
- Feeding/swallowing evaluation (to assess aspiration risk, given palate anomalies and hypotonia)

### Pharmacotherapy / Supportive Care
- **Gastroesophageal reflux management** — standard pharmacologic/positional management (NCIT:C49236 Therapeutic Procedure-level; specific agents not disease-specific)
  - NCIT term: `NCIT:C15986` (Pharmacotherapy, generic)
- **Nutritional support** — supplementary formulas; consideration of enteral (gastrostomy tube) feeding for failure to thrive or unsafe oral feeding
  - NCIT term: `NCIT:C15447` (Dietary Intervention) / gastrostomy under `NCIT:C15329` (Surgical Procedure)
- No gene therapy, RNA-based therapy, cell therapy, or targeted molecular therapy exists or is in development for Emanuel syndrome, consistent with its nature as a multi-gene dosage disorder rather than a single-gene target.

### Surgical/Interventional
- **Cardiac surgical correction** for structural heart defects (ASD/VSD closure, tetralogy of Fallot repair, etc.) — `NCIT:C15329` (Surgical Procedure) / more specifically cardiac surgical procedure terms.
- **Anal atresia surgical repair**
- **Inguinal hernia repair**
- **Gastrostomy tube placement** for feeding support
- **Orthopedic surgical intervention** for hip dysplasia as indicated — `NCIT:C16186` (Orthopedic Surgical Procedure)
- **Critical safety consideration:** GeneReviews specifically emphasizes that "care during sedation and/or operative procedures should be provided by a pediatric anesthesiologist," reflecting airway/craniofacial anesthesia risk considerations (micrognathia, hypotonia).

### Supportive and Rehabilitative
- **Physical therapy** — `NCIT:C15302` (Physical Therapy)
- **Occupational therapy**
- **Speech-language therapy**, including **augmentative and alternative communication (AAC)** strategies given very limited verbal skills
- **Genetic counseling** for the family — `NCIT:C15240` (Genetic Counseling)

### Experimental / Clinical Trials
No disease-specific clinical trials (interventional) for Emanuel syndrome were identified in the search (consistent with its ultra-rare status and multisystem, non-single-gene-targetable nature). Management follows general pediatric multidisciplinary and cardiac/renal/orthopedic surgical standards rather than syndrome-specific trial-based protocols.

### Treatment Strategy
Management follows an **individualized, malformation-driven multidisciplinary care pathway** rather than a standardized algorithm specific to Emanuel syndrome — coordinated among cardiology, nephrology, genetics, orthopedics, otolaryngology, audiology, ophthalmology, gastroenterology, and developmental/rehabilitation specialists.

**Sources:**
- [GeneReviews NBK1263 — Management section](https://www.ncbi.nlm.nih.gov/books/NBK1263/)
- [Emanuel Syndrome — Gastrointestinal Feeding Issues, emanuelsyndrome.org](https://emanuelsyndrome.org/emanuel-syndrome/medical-emanuel-syndrome/gastrointestinal/)

---

## 13. Prevention

### Primary Prevention
There is no way to prevent formation of the recurrent t(11;22) translocation itself (it arises from intrinsic PATRR sequence instability). Primary prevention of Emanuel syndrome therefore centers on **reproductive risk management** in known or newly identified balanced-carrier families:

- **Genetic counseling** for identified balanced translocation carriers and their at-risk relatives regarding the 1.8–5.6% live-birth recurrence risk (higher with maternal transmission) and the ~23–37% spontaneous abortion risk.
- **Preimplantation genetic testing for structural rearrangements (PGT-SR):** IVF with ICSI followed by embryo biopsy and testing allows selection of chromosomally normal or balanced embryos for transfer, distinguishing them from unbalanced (Emanuel syndrome-causing) embryos before implantation. Outcomes vary by rearrangement type; reciprocal translocations such as t(11;22) yield a lower proportion of normal/balanced blastocysts (~45.7% in one comparative study) than non-reciprocal rearrangements (~89.9%), reflecting the larger number of possible unbalanced segregation products from a reciprocal-translocation quadrivalent.

### Secondary Prevention (Early Detection)
- **Prenatal diagnostic testing** (CVS/amniocentesis with karyotype, FISH, and/or CMA) in known carrier pregnancies, and diagnostic follow-up of screening findings (e.g., abnormal cfDNA/NIPS result, ultrasound findings such as IUGR or increased nuchal translucency).
- **Cascade carrier testing** of at-risk relatives once a balanced translocation is identified in a family, to inform their own reproductive planning before pregnancy occurs.

### Tertiary Prevention (Preventing Complications in Affected Individuals)
- Early, systematic multidisciplinary baseline evaluation (cardiac, renal, orthopedic, audiologic, ophthalmologic, feeding/swallowing) at diagnosis to detect and proactively manage complications before they become life-threatening (e.g., early echocardiography to catch cardiac defects driving the majority of mortality).
- Pediatric-anesthesiologist-supervised perioperative care to reduce anesthesia-related risk given craniofacial/airway anatomy.

### Genetic Counseling
Central to prevention at every stage: risk assessment for carrier couples, explanation of the 3:1 malsegregation mechanism and recurrence-risk figures, discussion of reproductive options (natural conception with prenatal diagnosis, PGT-SR/IVF, use of donor gametes, or adoption), and family cascade-testing coordination.

### Public Health / Screening Programs
No population-level public health screening or immunization strategy applies, as this is a non-infectious, non-preventable-at-the-population-level constitutional chromosomal disorder; prevention operates exclusively at the level of individual/family reproductive genetics.

**Sources:**
- [Impact of Chromosomal Structural Rearrangements on IVF Laboratory Outcomes in PGT-SR Cycles, PMC12387454](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12387454/)
- [GeneReviews NBK1263 — Genetic Counseling section](https://www.ncbi.nlm.nih.gov/books/NBK1263/)

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary/companion-animal or wildlife disease directly analogous to Emanuel syndrome (i.e., a spontaneous t(11;22)-equivalent recurrent translocation producing a supernumerary derivative chromosome with this specific phenotype) was identified in the literature search. This is consistent with the disorder's basis in a **human-specific recurrent breakpoint hotspot** (PATRR11/PATRR22) rather than a broadly conserved genomic vulnerability; no OMIA (Online Mendelian Inheritance in Animals) entry or comparable veterinary literature was found for this specific translocation. Comparative genomic mapping of the human 11q23/22q11 breakpoint regions to other species' syntenic loci was not addressed in the sources reviewed.

---

## 15. Model Organisms

### Direct Disease Models
**No dedicated mouse, zebrafish, or other animal model of the t(11;22) translocation or the der(22) supernumerary chromosome/Emanuel syndrome karyotype was identified** in the literature search. This is a significant gap consistent with the technical difficulty of engineering a segmental-duplication/supernumerary-chromosome model recapitulating a human-specific recurrent palindrome-mediated rearrangement, combined with the disorder's rarity limiting research investment relative to more common chromosomal syndromes (e.g., Down syndrome, 22q11.2 deletion syndrome, both of which have extensive mouse-model literature).

### Related/Indirect Models Informing Mechanism
- **TBX1 dosage mouse models:** Mouse models engineered for **increased TBX1 dosage** in the anterior heart field reproduce **congenital heart disease resembling the 22q11.2 duplication syndrome phenotype** (Hum Mol Genet 2018), providing the strongest indirect functional evidence for how trisomic dosage of the duplicated 22q11 segment in Emanuel syndrome could drive its cardiac phenotype — though this model targets TBX1 dosage specifically, not the full der(22) segmental composition, and does not model the 11q23-qter component at all.
- **PATRR/palindrome biophysical models:** In vitro and bacterial/yeast-based studies of PATRR11 and PATRR22 cruciform-extrusion propensity (not organismal models, but biochemical/molecular models) have been used to characterize the DNA secondary-structure mechanism underlying breakpoint formation (PMID:17264116).
- **Unrelated translocation-disruption mouse model (context only):** A mouse model of a different chromosomal translocation, t(1;11), disrupting *DISC1* (relevant to psychiatric illness risk, not Emanuel syndrome) illustrates the general feasibility of engineering translocation-breakpoint mouse models, but is not itself an Emanuel syndrome model (PMC7895946).

### Applications and Limitations
- Existing indirect models (TBX1-dosage mice) can inform study of the **cardiac phenotype component** and validate the dosage-sensitivity hypothesis for genes in the 22q11 duplicated segment.
- **No model currently exists** to study the neurodevelopmental (intellectual disability), renal, or craniofacial phenotype components, or to study the combined dual-segment (11q + 22q) trisomic dosage effect that defines the full Emanuel syndrome phenotype — representing a clear unmet need in the field, likely reflecting both the syndrome's rarity and the technical complexity of modeling a supernumerary marker chromosome (as opposed to a simple gene knockout/knock-in) in a laboratory animal.

**Sources:**
- [Dysregulation of TBX1 dosage — mouse model, Hum Mol Genet 2018](https://academic.oup.com/hmg/article/27/11/1847/4917554)
- [Cruciform extrusion propensity of PATRRs, PMID:17264116](https://pubmed.ncbi.nlm.nih.gov/17264116/)
- [Functional brain defects in DISC1 t(1;11) mouse model, PMC7895946](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7895946/)

---

## Summary and Key Curation Notes

Emanuel syndrome is a well-characterized, mechanistically well-understood **chromosomal dosage disorder** (partial trisomy 11q23-qter + partial trisomy 22q11 via a supernumerary der(22) marker chromosome), arising from 3:1 meiotic malsegregation of the most common recurrent human reciprocal translocation, t(11;22)(q23;q11.2). The molecular origin of the translocation itself (PATRR-mediated hairpin/cruciform-driven double-strand breaks) is unusually well elucidated for a rare chromosomal syndrome. However, **gene-level dissection of the phenotype is markedly asymmetric**: the cardiac/craniofacial component is reasonably well linked to TBX1/HIRA dosage within the shared 22q11 DiGeorge/VCFS critical region (supported by mouse dosage models), while the neurodevelopmental, renal, and growth phenotypes attributable to the 11q23-qter trisomic segment remain **mechanistically underexplored**, with no dominant candidate gene identified and no animal model available. This asymmetry — strong mechanistic grounding for one duplicated segment, essentially absent mechanistic dissection for the other — is the most important knowledge gap for a dismech-style pathophysiology entry to flag explicitly, likely via a `HUMAN_MODEL_MISMATCH` or `KNOWLEDGE_GAP` discussion node distinguishing the well-evidenced TBX1-dosage cardiac branch from the inferred-only 11q-driven branches of the causal chain.

Sources:
- [Emanuel Syndrome - GeneReviews®](https://www.ncbi.nlm.nih.gov/books/NBK1263/)
- [OMIM #609029 - EMANUEL SYNDROME](https://omim.org/entry/609029)
- [Orphanet: Emanuel syndrome](https://www.orpha.net/en/disease/detail/96170)
- [NORD - Emanuel syndrome](https://rarediseases.org/mondo-disease/emanuel-syndrome/)
- [Ohye et al., Prevalence of Emanuel syndrome, Pediatr Int 2014](https://onlinelibrary.wiley.com/doi/10.1111/ped.12437)
- [Der(22)/VCFS 1.5-Mb region overlap, Am J Hum Genet](https://www.sciencedirect.com/science/article/pii/S0002929707617121)
- [Dysregulation of TBX1 dosage, Hum Mol Genet 2018](https://academic.oup.com/hmg/article/27/11/1847/4917554)
- [Kurahashi & Emanuel — palindrome-mediated translocation mechanism, PMC4940405](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4940405/)
- [ZAP70 differential expression analysis, PMC12144060 (PMID:38687434)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12144060/)
- [Prenatal cfDNA Screening for Emanuel Syndrome, PMC10606745](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10606745/)
- [Phenotypic Delineation of Emanuel Syndrome: 63 Individuals](https://www.researchgate.net/publication/26674827_Phenotypic_Delineation_of_Emanuel_Syndrome_Supernumerary_Derivative_22_Syndrome_Clinical_Features_of_63_Individuals)
- [Derivative 11;22 (Emanuel) Syndrome Case Report and Review, PMC3652044](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3652044/)
- [Emanuel syndrome due to unusual pattern, Egypt J Med Hum Genet 2024](https://link.springer.com/article/10.1186/s43042-024-00494-6)
- [Impact of Chromosomal Structural Rearrangements on PGT-SR Outcomes, PMC12387454](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12387454/)
- [Cruciform extrusion propensity of PATRRs, PMID:17264116](https://pubmed.ncbi.nlm.nih.gov/17264116/)
- [Functional brain defects in DISC1 t(1;11) mouse model, PMC7895946](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7895946/)
- [Emanuel syndrome and congenital diaphragmatic hernia: systematic review](https://www.sciencedirect.com/science/article/abs/pii/S0022346821007776)
- [Emanuel Syndrome: Isolated Nuchal Translucency Thickening, PMC12527601](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12527601/)
- [Supernumerary derivative 22 from novel translocation t(20;22), PMC8962060](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8962060/)
- [Emanuel Syndrome — patient organization, emanuelsyndrome.org](https://emanuelsyndrome.org/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 60 |
| Resolved | 58 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 22 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 12 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009301` (1 mention) - the report calls it "Emanuel syndrome"; MONDO calls it **46,XY sex reversal 7**
- `HP:0011344` (1 mention) - the report calls it "Severe intellectual disability"; HP calls it **Severe global developmental delay**
- `HP:0000252` (1 mention) - the report calls it "Universal in GeneReviews cohort"; HP calls it **Microcephaly**
- `HP:0001252` (1 mention) - the report calls it "Universal"; HP calls it **Hypotonia**
- `HP:0001385` (1 mention) - the report calls it "Common"; HP calls it **Hip dysplasia**
- `HP:0000365` (1 mention) - the report calls it "Documented feature"; HP calls it **Hearing impairment**
- `HP:0002020` (1 mention) - the report calls it "Common"; HP calls it **Gastroesophageal reflux**
- `HP:0001250` (1 mention) - the report calls it "Documented in a subset"; HP calls it **Seizure**
- `GO:0007126` (2 mentions) - the report calls it "meiotic nuclear division"; GO calls it **GO_0007126**
- `UBERON:0002616` (2 mentions) - the report calls it "cerebellar cortex"; UBERON calls it **regional part of brain**
- `UBERON:0002417` (1 mention) - the report calls it "hard palate"; UBERON calls it **abdominal segment of trunk**
- `UBERON:0000151` (1 mention) - the report calls it "ear"; UBERON calls it **pectoral fin**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0007126` (GO_0007126) (2 mentions) - replaced by `GO:0051321`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0002327` (1 mention) - the report calls it "mammary luminal progenitor cell — N/A"; CL calls it **mammary gland epithelial cell**, and lists "mammary epithelial cell" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.