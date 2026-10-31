---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-20T19:17:46.090891'
end_time: '2026-10-20T19:32:07.237255'
duration_seconds: 861.15
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Progressive Myoclonic Epilepsy Type 11
  mondo_id: MONDO:0030034
  category: Mendelian
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 12
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 7
  validator_version: 0.3.0
term_validation:
  total_terms: 33
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 10
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0030034
    reported_labels:
    - MONDO
    ontology_label: epilepsy, progressive myoclonic, 11
  - term_id: HP:0007334
    reported_labels:
    - Progressive myoclonic epilepsy
    ontology_label: Bilateral tonic-clonic seizure with focal onset
  - term_id: HP:0011146
    reported_labels:
    - Non-convulsive status epilepticus
    ontology_label: Dialeptic seizure
  - term_id: NCIT:C935
    reported_labels:
    - Mainstay for GTCS and myoclonus
    ontology_label: Vindesine Sulfate
  - term_id: NCIT:C577
    reported_labels:
    - Mainstay anti-myoclonic
    ontology_label: Industrial Waste
  - term_id: NCIT:C29102
    reported_labels:
    - Effective add-on for myoclonus
    ontology_label: Hydroxypropyl Methylcellulose D
  - term_id: NCIT:C921
    reported_labels:
    - Add-on option
    ontology_label: Uricosuric Agent
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Progressive_Myoclonic_Epilepsy_Type_11-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Progressive_Myoclonic_Epilepsy_Type_11-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Progressive Myoclonic Epilepsy Type 11
- **MONDO ID:** MONDO:0030034 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Progressive Myoclonic Epilepsy Type 11** covering all of the
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

# Progressive Myoclonic Epilepsy Type 11 (EPM11): A Comprehensive Disease Characteristics Report

**Disease:** Progressive Myoclonic Epilepsy Type 11 (EPM11)
**MONDO ID:** MONDO:0030034 · **OMIM:** #618876 · **Causal gene:** *SEMA6B* (HGNC:7357)
**Category:** Mendelian (monogenic), autosomal dominant

---

## Summary

Progressive Myoclonic Epilepsy Type 11 (EPM11) is an ultra-rare, autosomal-dominant progressive myoclonic epilepsy / developmental-and-epileptic-encephalopathy caused by heterozygous, usually *de novo*, **truncating variants clustered in the last exon (exon 17) of *SEMA6B*** (semaphorin-6B). The defining molecular feature is that these variants fall within the nonsense-mediated mRNA decay (NMD)-insensitive region of the transcript. Rather than being degraded, the mutant mRNA is translated into a **stable truncated protein lacking the intracellular domain**, which acts through a **toxic gain-of-function / dominant-negative mechanism**. This distinguishes EPM11 from simple haploinsufficiency disorders and explains why the *de novo* truncating variant class is so tightly disease-associated ([PMID: 32169168](https://pubmed.ncbi.nlm.nih.gov/32169168/); [PMID: 36719163](https://pubmed.ncbi.nlm.nih.gov/36719163/)).

Mechanistically, SEMA6B is a transmembrane class-6 semaphorin that functions as an **axon-guidance receptor** binding floorplate-derived **PlexinA2** (and, in hippocampal mossy fibers, **PlexinA4**). The intracellular domain lost in disease truncations is essential for its receptor-signaling function. Disruption of SEMA6B signaling impairs axon guidance, dendritic-spine maturation, and synaptogenesis across cortical, hippocampal, and cerebellar circuits—including GABAergic interneurons—producing an excitation/inhibition imbalance that drives cortical hyperexcitability, seizures, and myoclonus, alongside developmental regression, intellectual disability, and ataxia ([PMID: 25209245](https://pubmed.ncbi.nlm.nih.gov/25209245/); [PMID: 35604360](https://pubmed.ncbi.nlm.nih.gov/35604360/); [PMID: 20484647](https://pubmed.ncbi.nlm.nih.gov/20484647/)).

Clinically, EPM11 typically presents with developmental regression around age 2 after relatively normal early development, followed by polymorphic and often refractory seizures, progressive myoclonus, ataxia, spasticity, loss of independent ambulation, and severe cognitive impairment. The known worldwide caseload is tiny—approximately **36 reported patients**—spanning a phenotypic spectrum from classic PME to non-syndromic intellectual disability. There is **no disease-modifying or curative therapy**; management is symptomatic anti-seizure/anti-myoclonic polytherapy with supportive care, and prognosis is poor with lifelong, progressive disability ([PMID: 39419291](https://pubmed.ncbi.nlm.nih.gov/39419291/); [PMID: 30999254](https://pubmed.ncbi.nlm.nih.gov/30999254/)).

---

## 1. Disease Information

**Overview.** EPM11 is a monogenic progressive myoclonic epilepsy (PME) belonging to the group of developmental and epileptic encephalopathies. It is characterized by infantile/early-childhood onset, developmental regression, progressive myoclonus, polymorphic and frequently pharmacoresistant seizures, cerebellar and pyramidal/extrapyramidal signs, and severe cognitive impairment.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM | #618876 (Epilepsy, progressive myoclonic, 11) |
| MONDO | MONDO:0030034 |
| Gene | *SEMA6B* (HGNC:7357); OMIM gene *608873 |
| Inheritance | Autosomal dominant (ClinGen gene–disease validity: **Definitive**) |
| ICD-11 | 8A62 (Progressive myoclonic epilepsy) category |
| MeSH | Myoclonic Epilepsies, Progressive (D020191) |

**Synonyms / alternative names:** EPM11; SEMA6B-related progressive myoclonic epilepsy; SEMA6B-related developmental and epileptic encephalopathy; progressive myoclonic epilepsy-11.

**Source of information.** Information is derived from **aggregated disease-level resources** (OMIM, Orphanet, ClinGen) and from **individual patient case reports and small case series** in the primary literature, rather than from large EHR cohorts. Given the extreme rarity, the evidence base is dominated by case-level descriptions.

---

## 2. Etiology

**Primary cause — genetic.** EPM11 is a purely monogenic disorder caused by heterozygous pathogenic variants in *SEMA6B*. The predominant and best-validated class is **truncating (frameshift/nonsense) variants clustered in the last exon (exon 17)**, which escape NMD and produce a toxic truncated protein ([PMID: 32169168](https://pubmed.ncbi.nlm.nih.gov/32169168/); [PMID: 36719163](https://pubmed.ncbi.nlm.nih.gov/36719163/)).

**Genetic risk factors.** The causal variants are themselves the disease determinant. Most arise *de novo*; variants are absent from population databases such as gnomAD, consistent with pathogenicity. No susceptibility loci or modifier genes have been established.

**Environmental risk factors.** None implicated. No toxic, infectious, lifestyle, occupational, dietary, radiation, or age/sex-related environmental risk factors are known to contribute. EPM11 is not triggered by environmental exposure.

**Protective factors.** No genetic or environmental protective factors or modifier alleles are known. The only outcome-modifying factor identified is effective seizure control (see Prognosis).

**Gene–environment interactions.** None known; as a Mendelian disorder with high penetrance of the classic truncating variants, no GxE interactions have been characterized.

---

## 3. Phenotypes

EPM11 is a multi-domain neurological disorder. Core phenotypes and suggested HPO terms:

| Phenotype | HPO term (suggested) | Type | Onset | Progression | Frequency |
|---|---|---|---|---|---|
| Myoclonic seizures / myoclonus | HP:0001336 / HP:0001337 | Clinical sign | Early childhood | Progressive, worsening | Core / near-universal |
| Progressive myoclonic epilepsy | HP:0007334 | Clinical syndrome | ~18 mo–6 yr | Progressive | 50% of spectrum (18/36) |
| Developmental regression | HP:0002376 | Sign | ~2 yr | Progressive | Common |
| Intellectual disability (severe) | HP:0010864 | Sign | Childhood | Progressive | Severe; often nonverbal |
| Polymorphic seizures (atonic, absence, focal, GTCS, negative myoclonus) | HP:0002197, HP:0002121, HP:0002384, HP:0002069 | Clinical sign | 18 mo–6 yr | Refractory in ~50% | Core |
| Ataxia / cerebellar signs | HP:0001251 | Sign | 1st–2nd decade | Progressive | Common |
| Spasticity / pyramidal signs | HP:0001257 | Sign | 1st–2nd decade | Progressive | Common |
| Tremor | HP:0001337 | Sign | 1st–2nd decade | Progressive | Common |
| Loss of ambulation | HP:0002540 | Functional | 1st–2nd decade | Progressive | Frequent |
| Non-convulsive status epilepticus | HP:0011146 | Clinical sign | Variable | Episodic | Reported |

**Phenotype characteristics.** Onset of developmental regression occurs around **2 years of age** after relatively normal early development; various seizure types emerge between 18 months and 6 years and are often refractory. Over the first and second decades, pyramidal, extrapyramidal, and cerebellar signs accumulate. Cognitive impairment is **severe** (few words or non-verbal). The phenotype is **progressive** and does not correlate with variant type or location ([PMID: 32169168](https://pubmed.ncbi.nlm.nih.gov/32169168/); [PMID: 36719163](https://pubmed.ncbi.nlm.nih.gov/36719163/); [PMID: 35604360](https://pubmed.ncbi.nlm.nih.gov/35604360/)).

**Phenotypic spectrum.** Cordovado et al. (2022) showed the spectrum extends beyond classic PME: *"until now, SEMA6B variants have mainly been reported in patients with progressive myoclonic epilepsy, our study indicates that the clinical spectrum is wider and also includes non-syndromic ID without epilepsy or myoclonus"* ([PMID: 35604360](https://pubmed.ncbi.nlm.nih.gov/35604360/)). The 2025 systematic review (n=36) subdivided presentations into **PME (50%, 18/36), developmental and epileptic encephalopathy (36%, 13/36), neurodevelopmental disorder (11%, 4/36), and epilepsy (3%, 1/36)** ([PMID: 39419291](https://pubmed.ncbi.nlm.nih.gov/39419291/)).

**Quality of life impact.** Severe. Progressive loss of ambulation, non-verbal status, refractory seizures, and myoclonus produce profound dependence in daily functioning and lifelong disability. EPM11 can clinically mimic Angelman syndrome ([PMID: 42125992](https://pubmed.ncbi.nlm.nih.gov/42125992/)).

---

## 4. Genetic / Molecular Information

**Causal gene.** *SEMA6B* (semaphorin-6B), HGNC:7357, located on chromosome 15q21.1, encoding a transmembrane class-6 semaphorin. UniProt: Q9H3T3.

**Pathogenic variants.**
- **Predominant class:** Truncating (frameshift and nonsense) variants clustered in the **last exon (exon 17)**, which fall in the NMD-insensitive region. These escape nonsense-mediated decay and produce a stable protein lacking the intracellular domain ([PMID: 32169168](https://pubmed.ncbi.nlm.nih.gov/32169168/); [PMID: 36719163](https://pubmed.ncbi.nlm.nih.gov/36719163/)).
- **Rarer classes:** Missense variants (e.g., c.432C>G p.Cys144Trp, reported in an adult-onset case) and non-last-exon splice-site variants (e.g., **c.1680-2A>G**, NM_032108.4) producing diverse aberrant transcripts with **incomplete penetrance** ([PMID: 42696975](https://pubmed.ncbi.nlm.nih.gov/42696975/)).

**Variant classification (ACMG/AMP).** Recurrent *de novo* exon-17 truncating variants are classified **pathogenic/likely pathogenic**, supported by genome-wide statistical enrichment in developmental and epileptic encephalopathy trios and absence from population databases.

**Allele frequency.** The causal *de novo* variants are **absent from gnomAD** and other population databases, consistent with pathogenicity.

**Somatic vs germline.** Variants are **germline** (constitutional), usually *de novo*; rare inherited (autosomal-dominant transmitted) cases exist.

**Functional consequences.** **Gain of function / dominant-negative.** Castellotti et al. state: *"The exon 17 is mainly involved, with truncating mutations causing the production of aberrant proteins with toxic gain of function"* ([PMID: 36719163](https://pubmed.ncbi.nlm.nih.gov/36719163/)). The truncated protein lacks the intracellular domain required for receptor signaling and mislocalizes subcellularly, reducing dendritic spine maturation ([PMID: 35604360](https://pubmed.ncbi.nlm.nih.gov/35604360/)).

**Modifier genes / epigenetics / chromosomal abnormalities.** None established. No DNA methylation or histone-modification changes have been characterized for EPM11, and no large-scale chromosomal rearrangements are implicated (though a 12p13.32 deletion appears in the broader PMA differential, unrelated to *SEMA6B*).

---

## 5. Environmental Information

Not applicable. EPM11 is a monogenic disorder with no identified environmental, lifestyle, toxic, occupational, radiation, or infectious contributing factors. No infectious agents trigger or cause the disease.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A **de novo (usually) truncating variant in the last exon (exon 17) of *SEMA6B*** arises → leads to a premature stop codon in the NMD-insensitive region.
2. Because the variant lies in the NMD(-) region, the mutant mRNA **escapes nonsense-mediated decay** → results in a **stable truncated SEMA6B protein lacking the intracellular domain** (*inferred from NMD rules + observed protein; demonstrated in overexpression systems*).
3. The truncated protein exerts a **dominant-negative / toxic gain-of-function effect** on SEMA6B signaling (and mislocalizes subcellularly) → results in disrupted SEMA6B–PlexinA2 (and PlexinA4) receptor signaling.
4. Disrupted semaphorin–plexin signaling → leads to **impaired axon guidance, reduced dendritic-spine density/maturation, and defective synaptogenesis**.
5. Faulty wiring across **cortical, hippocampal (mossy fiber), and cerebellar circuits, including GABAergic interneurons** → results in abnormal neural connectivity. **The mechanism branches here:**
   - **Branch 6a (epileptogenesis):** reduced inhibition / excitation–inhibition imbalance → **cortical hyperexcitability** → myoclonus, polymorphic and refractory seizures.
   - **Branch 6b (neurodevelopmental):** abnormal connectivity and ongoing circuit dysfunction → **developmental regression, severe intellectual disability, ataxia, and progressive pyramidal/extrapyramidal signs**.
7. Progressive accumulation of circuit dysfunction over the first two decades → leads to loss of ambulation, non-verbal status, and lifelong disability.

*(Steps 1–3 and the gain-of-function nature are directly supported; the GABAergic/E-I-imbalance link in branch 6a is partly inferred from expression data and general PME pathophysiology.)*

### Supporting detail

- **Molecular pathways:** Semaphorin–plexin axon-guidance signaling. SEMA6B binds **PlexinA2** at the midline and **PlexinA4** in the hippocampus. GO:0007411 (axon guidance); GO:0071526 (semaphorin-plexin signaling pathway). *"we demonstrate that Sema6B binds to floorplate-derived plexin A2 (PlxnA2) for navigation at the midline"* ([PMID: 25209245](https://pubmed.ncbi.nlm.nih.gov/25209245/)).
- **Protein dysfunction:** Loss of the intracellular domain abolishes receptor signaling: *"Truncated Sema6B lacking the intracellular domain was unable to rescue the loss-of-function phenotype, confirming a receptor function of Sema6B"* ([PMID: 25209245](https://pubmed.ncbi.nlm.nih.gov/25209245/)). Patient variants mislocalize and reduce spine density: *"The overexpression of some variants leads to a subcellular mislocalization of SEMA6B protein in HEK293T cells and to a reduced spine density owing to loss of mature spines in neuronal cultures"* ([PMID: 35604360](https://pubmed.ncbi.nlm.nih.gov/35604360/)).
- **Cellular processes:** Dendritic spine formation/maturation (GO:0060996, GO:0060997), synaptogenesis, neuronal migration/wiring. Cell types: cortical excitatory neurons (CL:0000679), GABAergic inhibitory interneurons (CL:0000617), cerebellar Purkinje cells (CL:0000121), hippocampal pyramidal neurons.
- **Subcellular compartments:** Plasma membrane (transmembrane receptor), dendritic spine, axonal growth cone; disease-associated mislocalization.
- **Metabolic / immune involvement:** None characterized; EPM11 is not a metabolic or immune-mediated PME.
- **Omics profiling:** No disease-specific transcriptomic, proteomic, metabolomic, or lipidomic signatures have been published; mechanistic data derive from targeted functional assays.

---

## 7. Anatomical Structures Affected

**Organ / system level.** Primary involvement is the **central nervous system** (UBERON:0001017). Key regions: **cerebral cortex** (UBERON:0000956), **cerebellum** (UBERON:0002037, Purkinje cells), **hippocampus** (UBERON:0002421, mossy fiber projections). Body system: **nervous system** (UBERON:0001016). No primary non-neurological organ involvement; secondary effects (e.g., immobility-related complications) follow from progressive disability.

**Tissue / cell level.** Nervous tissue. Affected cell populations: cortical excitatory neurons (CL:0000679), GABAergic interneurons (CL:0000617), cerebellar Purkinje cells (CL:0000121), hippocampal neurons. SEMA6B is highly expressed across these neuronal populations.

**Subcellular level.** Plasma membrane / transmembrane receptor localization; dendritic spines; axonal growth cones. GO cellular components: GO:0005886 (plasma membrane), GO:0043197 (dendritic spine).

**Localization / lateralization.** Diffuse, **bilateral** CNS involvement. EEG shows focal, multifocal, and diffuse abnormalities (see Diagnostics); brain MRI is often normal or non-specific.

---

## 8. Temporal Development

- **Onset:** Developmental regression around **age 2** after relatively normal early development; **insidious/subacute** onset. Seizures emerge between **18 months and 6 years**. A rare adult-onset missense case exists.
- **Progression:** Chronic and **progressive**. Over the first and second decades, pyramidal, extrapyramidal, and cerebellar signs worsen (spasticity, loss of ambulation, myoclonus, tremor, ataxia). Seizures frequently refractory (~50% pharmacoresistant). Course is lifelong.
- **Stages:** Early (regression + seizure onset) → intermediate (progressive myoclonus, motor decline) → advanced (loss of ambulation, non-verbal, severe disability).
- **Patterns:** No spontaneous remission; seizures episodic but underlying neurodegeneration is relentlessly progressive. The **critical window** for intervention is early seizure control, which is associated with improved neurodevelopmental outcomes ([PMID: 42696975](https://pubmed.ncbi.nlm.nih.gov/42696975/)).

---

## 9. Inheritance and Population

- **Epidemiology:** Ultra-rare. Only **~36 patients reported worldwide** (2025 systematic review); no prevalence/incidence estimates exist ([PMID: 39419291](https://pubmed.ncbi.nlm.nih.gov/39419291/)).
- **Inheritance:** **Autosomal dominant**, mostly **de novo**. ClinGen gene–disease validity **Definitive**. Rare inherited (AD-transmitted) families exist.
- **Penetrance:** High/complete for classic exon-17 truncating variants; **incomplete penetrance** documented for a splice-site variant family (c.1680-2A>G) — *"a novel heterozygous donor splice-site variant NM_032108.4 (SEMA6B): c.1680-2A>G segregating with autosomal dominant EPM1 in a family exhibiting marked incomplete penetrance"* ([PMID: 42696975](https://pubmed.ncbi.nlm.nih.gov/42696975/)).
- **Expressivity:** Variable (PME to non-syndromic ID), not correlated with variant type/location.
- **Anticipation / mosaicism / founder effects / consanguinity:** No genetic anticipation (not a repeat-expansion disorder); germline mosaicism theoretically possible but not systematically documented; no founder effect or geographic clustering. The original 4 patients were ethnically diverse (2 Japanese, 1 Israeli, 1 Malaysian).
- **Carrier frequency:** Not applicable for a mostly *de novo*, dominant disorder.
- **Sex ratio / age distribution:** No sex predilection reported; affected individuals are predominantly children and young adults.

---

## 10. Diagnostics

**Diagnostic approach — genetic.** Diagnosis relies on **molecular genetic testing**: exome (WES) or genome sequencing (WGS), or a multigene **epilepsy/PME panel** detecting the heterozygous *SEMA6B* truncating variant (typically exon 17, usually *de novo*). There is **no specific biochemical biomarker**, and brain MRI is often normal or non-specific ([PMID: 32169168](https://pubmed.ncbi.nlm.nih.gov/32169168/)).

| Test | Utility in EPM11 |
|---|---|
| WES / WGS | High — primary diagnostic modality |
| Epilepsy / PME multigene panel | High — *SEMA6B* now included on PME panels |
| Single-gene *SEMA6B* sequencing | Useful if phenotype strongly suggestive |
| EEG | Supportive — focal/multifocal spikes, diffuse irregular spike-wave, high-amplitude slow waves |
| Brain MRI | Often normal/non-specific; used to exclude other causes |
| Biochemical/metabolic biomarkers | Not informative (no metabolic signature) |
| CMA/karyotype/FISH | Low yield (not a copy-number/structural disorder) |
| mtDNA / repeat-expansion testing | Used to exclude PME mimics (e.g., MERRF, EPM1), not positive in EPM11 |

**Clinical criteria & differential diagnosis.** Diagnosis integrates the PME clinical syndrome with a confirmatory *SEMA6B* variant. Differential diagnosis includes other PMEs (Unverricht-Lundborg disease/EPM1, Lafora disease, MERRF, neuronal ceroid lipofuscinoses, sialidosis, North Sea PME/GOSR2) and **Angelman syndrome**, which EPM11 can mimic ([PMID: 42125992](https://pubmed.ncbi.nlm.nih.gov/42125992/)). Progressive myoclonus ataxia (PMA) overlaps on a PMA-PME spectrum ([PMID: 38844245](https://pubmed.ncbi.nlm.nih.gov/38844245/)).

**Screening.** No population newborn or carrier screening exists (ultra-rare, mostly *de novo*). Cascade testing is only relevant in the rare inherited families.

---

## 11. Outcome / Prognosis

**Prognosis is poor.** EPM11 is a progressive neurodegenerative disorder (OMIM #618876). Over the first and second decades, affected individuals develop worsening pyramidal, extrapyramidal, and cerebellar signs—spasticity, **loss of independent ambulation**, myoclonus, tremor, ataxia—and severe cognitive impairment, becoming **non-verbal** ([PMID: 32169168](https://pubmed.ncbi.nlm.nih.gov/32169168/)). Seizures are frequently **refractory/pharmacoresistant** (~half of 36 patients) ([PMID: 39419291](https://pubmed.ncbi.nlm.nih.gov/39419291/)).

- **Survival/mortality:** Specific survival and mortality statistics are **not established** given extreme rarity.
- **Morbidity/disability:** Severe, progressive, lifelong. Quality of life severely impaired.
- **Recovery potential:** None; the disorder does not remit and disability accumulates.
- **Prognostic factors:** The principal **modifiable** factor is seizure control — *"effective anti-seizure medication was associated with improved neurodevelopmental outcomes"* ([PMID: 42696975](https://pubmed.ncbi.nlm.nih.gov/42696975/)).
- **Prognostic biomarkers:** None validated. Cortical hyperexcitability (giant SEPs / EMG-EEG correlate of myoclonus) may have prognostic value within the broader PMA-PME spectrum ([PMID: 38844245](https://pubmed.ncbi.nlm.nih.gov/38844245/)).

---

## 12. Treatment

**No disease-modifying or curative therapy exists.** Management is **symptomatic**, centered on anti-seizure medications (ASMs), as for progressive myoclonus epilepsies generally ([PMID: 32169168](https://pubmed.ncbi.nlm.nih.gov/32169168/)).

**Pharmacotherapy (NCIT terms suggested):**

| Drug | Class | Role in PME/EPM11 | NCIT |
|---|---|---|---|
| Valproic acid | Broad-spectrum ASM | Mainstay for GTCS and myoclonus | NCIT:C935 |
| Clonazepam | Benzodiazepine | Mainstay anti-myoclonic | NCIT:C577 |
| Levetiracetam | SV2A modulator | Effective add-on for myoclonus | NCIT:C29102 |
| Topiramate | Broad-spectrum ASM | Add-on option | NCIT:C921 |

Lasek-Bal et al. describe the standard polytherapy strategy in PME: *"ULD patients require anti-epileptic polytherapy, mostly benefitting from managing GTCS and myoclonus with valproic acid and clonazepam treatment. Patients may benefit from add-on therapy with levetiracetam or topiramate"* ([PMID: 30999254](https://pubmed.ncbi.nlm.nih.gov/30999254/)).

**Drugs to avoid.** Sodium-channel blockers (phenytoin, carbamazepine, lamotrigine, vigabatrin) can **worsen myoclonus** and are generally avoided in PME.

**Emerging / cross-PME insights.** In related PME models, GABA-ergic agents (sodium barbital, clonazepam, and the neurosteroid **ganaxolone**) suppressed seizures more effectively than valproate/levetiracetam in a GOSR2 North Sea PME *Drosophila* model, highlighting a potential GABA-targeted direction ([PMID: 38781737](https://pubmed.ncbi.nlm.nih.gov/38781737/)). Combination levetiracetam + clonazepam is effective for myoclonus in MERRF ([PMID: 30334528](https://pubmed.ncbi.nlm.nih.gov/30334528/)). These are extrapolations, not EPM11-specific trials.

**Advanced/experimental therapeutics.** No gene therapy, RNA-based therapy, cell therapy, or targeted molecular therapy exists or is in trials for EPM11. The toxic gain-of-function mechanism in principle makes **allele-selective knockdown (ASO/siRNA)** a theoretically rational—but currently unexplored—strategy.

**Supportive/rehabilitative care.** Physical, occupational, and speech therapy; management of spasticity, nutrition, and mobility; multidisciplinary neurological care.

---

## 13. Prevention

- **Primary prevention:** Not possible for *de novo* disease. In rare inherited families, **genetic counseling** and reproductive options (preimplantation genetic testing, prenatal diagnosis) apply.
- **Secondary prevention:** Early molecular diagnosis and early effective seizure control, which may improve neurodevelopmental outcomes ([PMID: 42696975](https://pubmed.ncbi.nlm.nih.gov/42696975/)).
- **Tertiary prevention:** Avoiding myoclonus-aggravating ASMs; managing complications of progressive disability.
- **Counseling:** Genetic counseling is central—recurrence risk is low for confirmed *de novo* cases (with residual germline mosaicism risk) but up to 50% in autosomal-dominant transmitted families with variable/incomplete penetrance.
- **Immunization / public health / environmental interventions:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *SEMA6B* is conserved across vertebrates. Mouse *Sema6b* (NCBI Gene) and chick *Sema6B* orthologs have been functionally characterized.
- **Natural disease:** No naturally occurring EPM11-equivalent disease has been described in companion animals or wildlife (no OMIA entry for a *SEMA6B* epilepsy phenotype).
- **Comparative biology:** The axon-guidance function of SEMA6B is evolutionarily conserved—defined in **mouse** (hippocampal mossy fibers, PlexinA4-dependent) and **chick** (commissural axons, PlexinA2-dependent) ([PMID: 20484647](https://pubmed.ncbi.nlm.nih.gov/20484647/); [PMID: 25209245](https://pubmed.ncbi.nlm.nih.gov/25209245/)).
- **Transmission / zoonotic potential:** Not applicable (genetic, non-communicable).

---

## 15. Model Organisms

| Model | Type | Key finding | Relevance / limitation |
|---|---|---|---|
| *Sema6b*-null mouse | Mammalian knockout | Viable; aberrant hippocampal mossy fiber projections into stratum radiatum/oriens; additive with *Sema6a* | Models **loss-of-function**, not the human **gain-of-function** mechanism ([PMID: 20484647](https://pubmed.ncbi.nlm.nih.gov/20484647/)) |
| Chick commissural neurons | In vivo RNAi/rescue | SEMA6B acts as PlexinA2-binding axon-guidance receptor; intracellular domain essential | Established receptor role; not a disease model ([PMID: 25209245](https://pubmed.ncbi.nlm.nih.gov/25209245/)) |
| HEK293T overexpression | In vitro | Patient variants mislocalize subcellularly | Variant functional assay ([PMID: 35604360](https://pubmed.ncbi.nlm.nih.gov/35604360/)) |
| Primary neuronal culture (shRNA) | In vitro | Reduced dendritic spine density/maturation | Links SEMA6B to synaptic pathology ([PMID: 35604360](https://pubmed.ncbi.nlm.nih.gov/35604360/)) |
| Chick embryo rescue assay | In vivo | Patient variants fail to rescue commissural axon pathfinding | Demonstrates variant pathogenicity ([PMID: 35604360](https://pubmed.ncbi.nlm.nih.gov/35604360/)) |

Tawarayama et al.: *"In Sema6B-deficient mice several mossy fibers aberrantly project to the stratum radiatum and the stratum oriens. The number of aberrant mossy fibers is increased in Sema6A;Sema6B double knock-out mice, indicating that Sema6A and Sema6B function additively to regulate proper projection of mossy fibers"* ([PMID: 20484647](https://pubmed.ncbi.nlm.nih.gov/20484647/)).

**Key model limitation:** Existing knockouts recapitulate the **loss-of-function** axon-guidance phenotype but **do not model the dominant-negative/gain-of-function truncated protein** that drives human EPM11. A **knock-in mouse carrying a human exon-17 truncating variant** is the most important missing model.

---

## Mechanistic Model / Interpretation

```
 de novo SEMA6B exon-17 truncating variant (NMD-insensitive region)
                      │  escapes nonsense-mediated decay
                      ▼
   Stable truncated SEMA6B protein (lacks intracellular domain)
                      │  dominant-negative / toxic gain-of-function
                      ▼
   Disrupted SEMA6B–PlexinA2 / PlexinA4 receptor signaling
                      │  (intracellular domain required for signaling)
                      ▼
   Impaired axon guidance + reduced dendritic spine maturation + defective synaptogenesis
                      │
        ┌─────────────┴──────────────┐
        ▼                            ▼
 Aberrant GABAergic/excitatory     Abnormal cortical/hippocampal/
 cortical wiring → E/I imbalance   cerebellar connectivity
        ▼                            ▼
 Cortical hyperexcitability →      Developmental regression, severe ID,
 myoclonus, polymorphic            ataxia, pyramidal/extrapyramidal signs
 refractory seizures                        │
        └─────────────┬──────────────┘
                      ▼
   Progressive neurodegeneration → loss of ambulation, non-verbal,
   lifelong severe disability (poor prognosis)
```

The model's **hinge** is step 3: the loss of the intracellular domain abolishes SEMA6B receptor signaling ([PMID: 25209245](https://pubmed.ncbi.nlm.nih.gov/25209245/)), while NMD escape ensures the toxic protein is actually produced ([PMID: 32169168](https://pubmed.ncbi.nlm.nih.gov/32169168/)). Upstream events (variant → NMD escape → truncated protein) are genetic and well-demonstrated; downstream events (circuit mis-wiring → E/I imbalance → seizures) are supported by cellular/animal data but the specific GABAergic contribution to human epileptogenesis remains partly inferred.

---

## Evidence Base

| PMID | Title (abridged) | Evidence type | Contribution |
|---|---|---|---|
| [32169168](https://pubmed.ncbi.nlm.nih.gov/32169168/) | *De Novo Truncating Variants in the Last Exon of SEMA6B Cause Progressive Myoclonic Epilepsy* | Human genetics (trio cohort) | Defines disease; NMD escape; dominant-negative/GoF; original 4 patients |
| [36719163](https://pubmed.ncbi.nlm.nih.gov/36719163/) | *Progressive myoclonus epilepsies due to SEMA6B mutations* | Human clinical/genetic | Exon-17 clustering; toxic GoF; core phenotype |
| [35604360](https://pubmed.ncbi.nlm.nih.gov/35604360/) | *SEMA6B variants cause intellectual disability and alter dendritic spine density and axon guidance* | Human + in vitro/in vivo functional | Broad spectrum; spine density; mislocalization; chick rescue |
| [25209245](https://pubmed.ncbi.nlm.nih.gov/25209245/) | *Semaphorin 6B acts as a receptor in post-crossing commissural axon guidance* | Model (chick) | Receptor role; PlexinA2 binding; intracellular domain essential |
| [20484647](https://pubmed.ncbi.nlm.nih.gov/20484647/) | *Roles of semaphorin-6B and plexin-A2 in hippocampal mossy fibers* | Model (mouse) | KO phenotype; PlexinA4-dependent repulsion |
| [39419291](https://pubmed.ncbi.nlm.nih.gov/39419291/) | *Systematic Review of SEMA6B-related Disorders* | Human systematic review (n=36) | Caseload, phenotypic subgroups, pharmacoresistance |
| [42696975](https://pubmed.ncbi.nlm.nih.gov/42696975/) | *Novel SEMA6B splice-site variant (c.1680-2A>G)* | Human genetics/family | AD transmission; incomplete penetrance; ASM-outcome link |
| [42125992](https://pubmed.ncbi.nlm.nih.gov/42125992/) | *SEMA6B-Related PME Mimicking Angelman Syndrome* | Human case | Differential diagnosis |
| [30999254](https://pubmed.ncbi.nlm.nih.gov/30999254/) | *Unverricht-Lundborg disease: seizure management* | Human clinical | PME ASM polytherapy strategy |
| [38844245](https://pubmed.ncbi.nlm.nih.gov/38844245/) | *Natural history of progressive myoclonus ataxia* | Human cohort | PMA-PME spectrum; cortical hyperexcitability prognostic value |
| [38781737](https://pubmed.ncbi.nlm.nih.gov/38781737/) | *ASMs and GABA in North Sea PME* | Model (*Drosophila*) | GABA-targeted therapy direction (cross-PME) |
| [30334528](https://pubmed.ncbi.nlm.nih.gov/30334528/) | *Levetiracetam+clonazepam in MERRF* | Human clinical | Combination anti-myoclonic efficacy (cross-PME) |

**Convergence vs. challenge.** The genetic and functional lines of evidence converge strongly on the NMD-escape/gain-of-function model. The main internal tension is that the available **animal models are loss-of-function knockouts**, which demonstrate the gene's normal axon-guidance role but do not directly prove the *toxic gain-of-function* human mechanism—this is inferred from NMD biology, protein-domain rescue failure, and variant overexpression data.

---

## Limitations and Knowledge Gaps

1. **Tiny evidence base (~36 patients).** No epidemiological estimates (prevalence/incidence), no survival/mortality statistics, and limited natural-history data.
2. **Mechanism inferred, not fully demonstrated in vivo.** No animal model expresses the human truncated gain-of-function protein; the dominant-negative mechanism is supported by overexpression and domain-deletion rescue data, not by an endogenous knock-in.
3. **GABAergic/E-I imbalance link is partly inferred.** The specific contribution of SEMA6B dysfunction in GABAergic interneurons to human epileptogenesis has not been directly measured in patient tissue.
4. **No omics signatures.** No disease-specific transcriptomic, proteomic, or metabolomic profiles exist for EPM11.
5. **No disease-specific therapy or trial.** All treatment data are extrapolated from PME broadly; no NCT-registered EPM11 trial exists.
6. **Genotype–phenotype correlation is weak/absent**, complicating prognostic counseling, and incomplete penetrance in non-last-exon variants adds uncertainty.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a knock-in mouse (or human iPSC-neuron/organoid) carrying a recurrent exon-17 truncating *SEMA6B* variant** to directly test the dominant-negative/gain-of-function model and establish a translational model that recapitulates the human disease (not just loss of function).
2. **Characterize E/I balance and GABAergic interneuron wiring** in patient-derived iPSC cortical organoids with electrophysiology/MEA to validate the cortical-hyperexcitability branch.
3. **Test allele-selective knockdown (ASO/siRNA) of the mutant truncated transcript** as a mechanistically rational, disease-modifying strategy for a gain-of-function disorder.
4. **Screen GABA-targeted agents (e.g., ganaxolone, clonazepam) vs. standard ASMs** in an EPM11-specific model, building on cross-PME findings ([PMID: 38781737](https://pubmed.ncbi.nlm.nih.gov/38781737/)).
5. **Establish an international patient registry** to capture natural history, seizure-control-vs-outcome relationships, survival, and genotype–phenotype data.
6. **Systematic cortical-hyperexcitability phenotyping** (giant SEPs, EMG-EEG) across the SEMA6B PMA-PME spectrum to develop prognostic biomarkers.

---

*Report compiled from 11 confirmed findings across 5 investigation iterations and 14 reviewed primary papers. Evidence source types are indicated throughout: human clinical/genetic, model organism (mouse, chick, Drosophila), and in vitro functional.*


## Artifacts

- [OpenScientist final report](Progressive_Myoclonic_Epilepsy_Type_11-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Progressive_Myoclonic_Epilepsy_Type_11-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 20 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030034` (2 mentions) - the report calls it "MONDO"; MONDO calls it **epilepsy, progressive myoclonic, 11**
- `HP:0007334` (1 mention) - the report calls it "Progressive myoclonic epilepsy"; HP calls it **Bilateral tonic-clonic seizure with focal onset**
- `HP:0011146` (1 mention) - the report calls it "Non-convulsive status epilepticus"; HP calls it **Dialeptic seizure**
- `NCIT:C935` (1 mention) - the report calls it "Mainstay for GTCS and myoclonus"; NCIT calls it **Vindesine Sulfate**
- `NCIT:C577` (1 mention) - the report calls it "Mainstay anti-myoclonic"; NCIT calls it **Industrial Waste**
- `NCIT:C29102` (1 mention) - the report calls it "Effective add-on for myoclonus"; NCIT calls it **Hydroxypropyl Methylcellulose D**
- `NCIT:C921` (1 mention) - the report calls it "Add-on option"; NCIT calls it **Uricosuric Agent**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001251` (1 mention) - the report calls it "Ataxia / cerebellar signs"; HP calls it **Ataxia**, and lists "Cerebellar ataxia" among its other names
- `HP:0001257` (1 mention) - the report calls it "Spasticity / pyramidal signs"; HP calls it **Spasticity**
- `HP:0002540` (1 mention) - the report calls it "Loss of ambulation"; HP calls it **Inability to walk**, and lists "Non-ambulatory" among its other names