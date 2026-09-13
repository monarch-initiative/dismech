---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T22:00:08.291922'
end_time: '2026-09-01T22:29:44.093050'
duration_seconds: 1775.8
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Ichthyotic Keratoderma Spasticity Hypomyelination And Dysmorphic Facial
    Features
  mondo_id: ''
  category: Disease
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
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:40590574
  relevance_assessed: 13
  on_topic: 5
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 29
  verified: 28
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 11
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: HP:0002346
    reported_labels:
    - Neurological sign
    ontology_label: Head tremor
  - term_id: HP:0001260
    reported_labels:
    - Neurological sign
    ontology_label: Dysarthria
  - term_id: HP:0001336
    reported_labels:
    - Neurological sign
    ontology_label: Myoclonus
  - term_id: HP:0000639
    reported_labels:
    - Neuro-ophthalmic sign
    ontology_label: Nystagmus
  - term_id: HP:0002079
    reported_labels:
    - Imaging abnormality
    ontology_label: Hypoplasia of the corpus callosum
  - term_id: HP:0001999
    reported_labels:
    - Physical sign
    ontology_label: Abnormal facial shape
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Ichthyotic_Keratoderma_Spasticity_Hypomyelination_And_Dysmorphic_Facial_Features-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Ichthyotic_Keratoderma_Spasticity_Hypomyelination_And_Dysmorphic_Facial_Features-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ichthyotic Keratoderma Spasticity Hypomyelination And Dysmorphic Facial Features
- **MONDO ID:**  (if available)
- **Category:** Disease

## Research Objectives

Please provide a comprehensive research report on **Ichthyotic Keratoderma Spasticity Hypomyelination And Dysmorphic Facial Features** covering all of the
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

# Ichthyotic Keratoderma, Spasticity, Hypomyelination and Dysmorphic Facial Features (IKSHD): A Comprehensive Disease Report

**Disease:** Ichthyotic Keratoderma, Spasticity, Hypomyelination And Dysmorphic Facial Features (IKSHD)
**Causal gene:** *ELOVL1* (ELOVL fatty acid elongase 1)
**OMIM phenotype:** #618527 | **OMIM gene:** *611813 | **HGNC:** 14417 | **Locus:** 1p34.2
**Suggested MONDO mapping:** MONDO term for "ichthyotic keratoderma, spasticity, hypomyelination, and dysmorphic facial features"

---

## Summary

**Ichthyotic Keratoderma, Spasticity, Hypomyelination and Dysmorphic Facial Features (IKSHD)** is an ultra-rare (<1/1,000,000) congenital, multisystem disorder that sits at the interface of dermatology and neurology. It is caused by pathogenic variants in *ELOVL1*, the gene encoding the endoplasmic-reticulum (ER) fatty-acid elongase that performs the **first and rate-limiting condensation step** of very-long-chain fatty acid (VLCFA) biosynthesis. The classic autosomal-dominant form of IKSHD arises from a **recurrent de novo heterozygous missense variant, c.494C>T (p.Ser165Phe)**, identified independently in multiple unrelated pediatric probands without a family history of disease ([PMID: 29496980](https://pubmed.ncbi.nlm.nih.gov/29496980/); [PMID: 30487246](https://pubmed.ncbi.nlm.nih.gov/30487246/); [PMID: 42101073](https://pubmed.ncbi.nlm.nih.gov/42101073/)).

Mechanistically, IKSHD is a **VLCFA-biosynthesis deficiency**. ELOVL1 elongates saturated and monounsaturated C22–C26 VLCFAs, which are esterified into ceramides (essential for the epidermal permeability barrier) and myelin sphingolipids (essential for central white-matter integrity). Loss of ELOVL1 function depletes these VLCFA-containing complex lipids, producing the two-compartment clinical signature: **ichthyotic keratoderma** in skin and **hypomyelination with progressive spasticity** in the central nervous system, accompanied by dysmorphic facial features and nystagmus. Notably, IKSHD is the biochemical *mirror image* of VLCFA-catabolism leukodystrophies such as X-linked adrenoleukodystrophy (X-ALD), where VLCFAs *accumulate*; both nonetheless converge on white-matter pathology and spasticity.

A defining feature of the *ELOVL1* disease spectrum is a **graded, allele-dose–dependent severity**. Monoallelic de novo p.Ser165Phe produces classic IKSHD with *mild* cerebral hypomyelination, whereas **biallelic (recessive) variants** cause a more severe and recognizable hypomyelinating leukodystrophy with a complex movement disorder (head tremor, myoclonus, dysarthria), 100%-penetrant developmental delay and spasticity, and corpus callosum hypoplasia ([PMID: 40590574](https://pubmed.ncbi.nlm.nih.gov/40590574/)). No disease-specific or ELOVL1-targeted therapy exists; management is symptomatic and multidisciplinary — topical emollients, keratolytics and retinoids for the skin, and antispasticity agents plus physical/occupational/speech therapy for the neurological features.

---

## 1. Disease Information

**Overview.** IKSHD is a congenital multisystem genodermatosis-plus-leukodystrophy characterized by the tetrad encoded in its name: (1) **ichthyotic keratoderma** (generalized scaling with palmoplantar involvement), (2) **spasticity** (upper-motor-neuron signs, progressive), (3) **hypomyelination** (deficient central white-matter myelin on MRI), and (4) **dysmorphic facial features**. Additional recurrent features include **nystagmus** and developmental delay. The disorder was delineated in 2018 when whole-exome sequencing of two unrelated pediatric probands with this shared phenotype identified a novel heterozygous *ELOVL1* variant ([PMID: 29496980](https://pubmed.ncbi.nlm.nih.gov/29496980/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | #618527 |
| OMIM (gene *ELOVL1*) | *611813 |
| HGNC | 14417 |
| Gene locus | 1p34.2 |
| Orphanet | Ultra-rare; listed under ELOVL1-related disorders (specific ORPHAcode as assigned) |
| ICD-11 | Best mapped under hereditary ichthyoses / hereditary spastic conditions (no dedicated code) |
| MeSH | No dedicated MeSH descriptor; indexed via *ELOVL1*, "Ichthyosis," "Hypomyelination" |
| MONDO | Map to the ELOVL1-related IKSHD phenotype entry |

**Synonyms / alternative names.** IKSHD; ELOVL1-related ichthyosis–spasticity–hypomyelination disorder; ELOVL1-related neuroichthyosis. The biallelic form is described as "hypomyelinating leukodystrophy, movement disorder, and ichthyosis" ([PMID: 40590574](https://pubmed.ncbi.nlm.nih.gov/40590574/)).

**Nature of information.** Evidence is derived from **individual patient reports and small case series** (aggregated at the disease level via OMIM/Orphanet), not from large EHR cohorts — consistent with an ultra-rare Mendelian disorder.

---

## 2. Etiology

**Primary cause (genetic).** IKSHD is a **monogenic disorder** caused by pathogenic variants in *ELOVL1*. The classic dominant form results from a **recurrent de novo heterozygous missense variant p.Ser165Phe (c.494C>T)**; a more severe form results from **biallelic** variants. There is no environmental or infectious etiology.

**Genetic risk factors.** The causal variant *is* the risk factor. The recurrent p.Ser165Phe change is the principal reported dominant allele; biallelic loss-of-function/hypomorphic variants define the recessive end. Because ELOVL1 sits within a network of six mammalian ELOVL elongases (ELOVL1–7), **other ELOVL genes are candidate modifiers**: patient fibroblasts show dysregulation of other ELOVL enzymes, which may buffer or aggravate the VLCFA deficit ([PMID: 40590574](https://pubmed.ncbi.nlm.nih.gov/40590574/)).

**Environmental risk factors.** None established. As a de novo–dominant disorder, advanced parental age is a theoretical (unproven) contributor to de novo variant occurrence. Sex distribution is approximately 1:1.

**Protective factors.** None established genetically or environmentally. Mechanistically, residual/compensatory activity of paralogous elongases (ELOVL3, ELOVL6, ELOVL7) that also handle VLCFA substrates could partially mitigate severity, but this is inferred, not demonstrated.

**Gene–environment interactions.** No specific GxE interactions have been documented. Skin-barrier compromise means that **environmental factors affecting congenital ichthyosis generally** (low humidity, temperature extremes, infection risk through a defective barrier) can modulate cutaneous morbidity, but these are downstream and non-specific.

---

## 3. Phenotypes

IKSHD is a two-compartment disorder (skin + CNS) with facial dysmorphism. Frequencies below are best-characterized for the **biallelic** cohort (n=7; [PMID: 40590574](https://pubmed.ncbi.nlm.nih.gov/40590574/)); the monoallelic form has similar features but *milder* hypomyelination.

| Phenotype | Type | HPO suggestion | Onset | Frequency (biallelic cohort) | Severity/course |
|---|---|---|---|---|---|
| Ichthyotic keratoderma / ichthyosis | Physical/skin sign | HP:0008064 (Ichthyosis); HP:0007479 (palmoplantar keratoderma) | Congenital/neonatal | 5/7 (71%) | Chronic, lifelong |
| Developmental delay | Behavioral/cognitive | HP:0001263 | Infancy | 7/7 (100%) | Stable–progressive |
| Progressive spasticity | Neurological sign | HP:0001257 (Spasticity); HP:0002061 (lower-limb spasticity) | Childhood | 7/7 (100%) | Progressive |
| Head tremor | Neurological sign | HP:0002346 | Childhood | 7/7 (100%) | Persistent |
| Dysarthria | Neurological sign | HP:0001260 | Childhood | 6/6 (100%) | Progressive |
| Myoclonus | Neurological sign | HP:0001336 | Childhood | 6/7 (86%) | Episodic/persistent |
| Nystagmus | Neuro-ophthalmic sign | HP:0000639 | Infancy/childhood | 5/6 (83%) | Persistent |
| Hypomyelination (MRI) | Imaging/lab abnormality | HP:0002500; HP:0006808 (leukoencephalopathy) | Congenital | 6/6 (100%) | Non-progressive on MRI |
| Corpus callosum hypoplasia | Imaging abnormality | HP:0002079 | Congenital | 5/6 (83%) | Static |
| Dysmorphic facial features | Physical sign | HP:0001999 | Congenital | Recurrent in IKSHD | Static |

**Quality-of-life impact.** The combination of progressive spasticity, a complex movement disorder, dysarthria, and developmental delay imposes substantial motor and communication disability, likely requiring mobility aids, assistive communication, and long-term caregiver support. The ichthyotic skin adds chronic pruritus/xerosis, cosmetic burden, thermoregulatory and barrier-infection concerns. Disease-specific QoL instruments have not been reported; generic pediatric-disability and dermatologic-QoL tools would apply.

---

## 4. Genetic / Molecular Information

**Causal gene.** *ELOVL1* (ELOVL fatty acid elongase 1; HGNC:14417; OMIM *611813; locus 1p34.2). ELOVL1 catalyzes elongation of **saturated and monounsaturated C22–C26 VLCFAs**, the rate-limiting condensation step of the ER elongation cycle ([PMID: 30487246](https://pubmed.ncbi.nlm.nih.gov/30487246/); [PMID: 16564093](https://pubmed.ncbi.nlm.nih.gov/16564093/)).

**Pathogenic variants.**

| Variant | Nomenclature | Zygosity/inheritance | Classification | Type | Disease |
|---|---|---|---|---|---|
| p.Ser165Phe | c.494C>T | Heterozygous, de novo (AD) | Pathogenic | Missense | Classic IKSHD (#618527) |
| Biallelic *ELOVL1* variants | (various) | Homozygous/compound-het (AR) | Pathogenic/likely pathogenic | Missense + LoF/hypomorphic | Severe hypomyelinating leukodystrophy + ichthyosis |

- **Allele frequency.** The recurrent p.Ser165Phe is de novo and absent/ultra-rare in population databases (gnomAD), consistent with a highly penetrant pathogenic change.
- **Somatic vs germline.** Germline (de novo in dominant cases; inherited in recessive cases).
- **Functional consequence.** The biochemical readout is **loss of elongase output** — reduced plasma C24:0 and C26:0 in a biallelic patient, and reduced VLCFA elongation in patient fibroblasts ([PMID: 40590574](https://pubmed.ncbi.nlm.nih.gov/40590574/)). The dominant p.Ser165Phe likely acts by impairing enzyme activity (loss-of-function/dominant effect on the elongation complex); a dominant-negative contribution on the shared ER four-enzyme complex is plausible but not definitively established.

**Modifier genes.** Paralogous elongases (**ELOVL3, ELOVL6, ELOVL7**) and downstream ceramide-synthesis machinery are candidate modifiers; fibroblast studies show compensatory dysregulation of other ELOVLs ([PMID: 40590574](https://pubmed.ncbi.nlm.nih.gov/40590574/)).

**Epigenetic information.** No disease-specific DNA-methylation or histone-modification signature has been reported for IKSHD.

**Chromosomal abnormalities.** None; IKSHD is a single-nucleotide/small-variant disorder, not a copy-number or structural disorder.

---

## 5. Environmental Information

IKSHD is a **purely genetic** disorder. **No environmental toxins, radiation, pollution, occupational exposures, lifestyle factors, or infectious agents** cause or trigger it. Environmental exposures are relevant only as non-specific modifiers of the skin-barrier phenotype (e.g., dry/cold climates worsening scaling; barrier breaches raising cutaneous infection risk), analogous to other congenital ichthyoses.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A pathogenic *ELOVL1* variant (heterozygous de novo **p.Ser165Phe**, or **biallelic** variants) **leads to** reduced ELOVL1 elongase activity in the endoplasmic reticulum.
2. Reduced ELOVL1 activity **results in** impaired condensation — the first, rate-limiting step of the four-enzyme ER VLCFA-elongation cycle — **causing** decreased synthesis of saturated/monounsaturated **C22–C26+ very-long-chain fatty acids** (measurable as reduced plasma C24:0 and C26:0). ([PMID: 39946831](https://pubmed.ncbi.nlm.nih.gov/39946831/); [PMID: 40590574](https://pubmed.ncbi.nlm.nih.gov/40590574/))
3. VLCFA deficiency **branches** into two tissue-specific consequences:
   - **Skin branch:** Reduced VLCFAs **lead to** depletion of ultra-long-chain **ceramides** and diminished stratum-corneum lipid lamellae, **causing** a defective epidermal permeability barrier that manifests as **ichthyotic keratoderma** (inferred from Elovl1-knockout mouse: barrier failure and reduced ≥C26 ceramides; [PMID: 23689133](https://pubmed.ncbi.nlm.nih.gov/23689133/)).
   - **CNS branch:** Reduced VLCFAs **lead to** shortened-chain **myelin sphingolipids**, **causing** hypomyelination and, consequently, progressive **spasticity** and a complex movement disorder (supported by Elovl1-deficient mouse: reduced myelin-sphingolipid chain length and impaired motor coordination; [PMID: 32123819](https://pubmed.ncbi.nlm.nih.gov/32123819/)).
4. Deficient central myelination and cortico-spinal tract dysfunction **result in** the observed upper-motor-neuron signs (spasticity, hyperreflexia), dysarthria, nystagmus, head tremor, and myoclonus.
5. Allele dose **modulates** severity: monoallelic p.Ser165Phe → *mild* hypomyelination (classic IKSHD); biallelic variants → *more severe* hypomyelinating leukodystrophy with corpus callosum hypoplasia and 100%-penetrant motor/developmental involvement (inferred from genotype–phenotype comparison; [PMID: 42101073](https://pubmed.ncbi.nlm.nih.gov/42101073/); [PMID: 40590574](https://pubmed.ncbi.nlm.nih.gov/40590574/)).

### Detail by category

- **Molecular pathways.** VLCFA/sphingolipid biosynthesis (ER fatty-acid elongation cycle: condensation → reduction → dehydration → reduction). ELOVL1 catalyzes the **rate-limiting condensation** step ([PMID: 39946831](https://pubmed.ncbi.nlm.nih.gov/39946831/)). Downstream: ceramide synthesis (skin) and myelin sphingolipid assembly (CNS).
- **Cellular processes.** Epidermal terminal differentiation / cornification (keratinocytes); oligodendrocyte myelination (CNS). Membrane biogenesis broadly — VLCFAs are esterified into sphingolipids, glycero(phospho)lipids and ether lipids ([PMID: 39946831](https://pubmed.ncbi.nlm.nih.gov/39946831/)).
- **Protein dysfunction.** Loss of elongase catalytic output; possible ER misfolding/dominant effects on the shared elongation complex (inferred). ELOVL defects are noted to contribute to disorders at the metabolic–neurodegenerative interface partly via misfolded enzymes in the ER/Golgi ([PMID: 39946831](https://pubmed.ncbi.nlm.nih.gov/39946831/)).
- **Metabolic changes.** Reduced VLCFA/sphingolipid pool (C24:0, C26:0 down). This is the **opposite** of VLCFA-catabolism disorders (X-ALD), where ABCD1 loss impairs peroxisomal VLCFA degradation and VLCFAs *accumulate* ([PMID: 42320861](https://pubmed.ncbi.nlm.nih.gov/42320861/); [PMID: 42469918](https://pubmed.ncbi.nlm.nih.gov/42469918/)).
- **Biochemical abnormalities.** Enzyme (elongase) deficiency; reduced ceramide chain length in skin (Elovl1-KO mouse) and reduced myelin sphingolipid chain length in brain.
- **Immune involvement.** Not a primary feature; no autoimmunity/immunodeficiency reported (barrier failure may secondarily raise infection risk).
- **Tissue-damage mechanisms.** Primarily a *developmental/biosynthetic deficiency* (dysmyelination/hypomyelination and defective cornification) rather than degenerative injury such as oxidative stress or fibrosis.

**Ontology suggestions.** GO biological processes: **fatty acid elongation** (GO:0030497), **very long-chain fatty acid metabolic process** (GO:0000038), **sphingolipid biosynthetic process** (GO:0030148), **myelination** (GO:0042552), **keratinocyte differentiation** (GO:0030216), **establishment of skin barrier** (GO:0061436). GO cellular component: **endoplasmic reticulum membrane** (GO:0005789). CL cell types: **keratinocyte** (CL:0000312), **oligodendrocyte** (CL:0000128). CHEBI: **very long-chain fatty acid** (CHEBI:27283), **ceramide** (CHEBI:17761).

### Mechanistic diagram

```
   ELOVL1 variant (de novo p.Ser165Phe  OR  biallelic)
                     |
                     v
   down ELOVL1 elongase (rate-limiting ER condensation step)
                     |
                     v
   down C22-C26+ VLCFA synthesis  (plasma C24:0, C26:0 down)
                     |
        +------------+-------------+
        v                          v
  SKIN branch                 CNS branch
  down VLCFA-ceramides        down VLCFA myelin sphingolipids
  -> defective barrier        -> hypomyelination
  -> ICHTHYOTIC KERATODERMA   -> SPASTICITY, movement disorder,
                                 dysarthria, nystagmus
        +----------- allele dose sets severity ----------+
     mono -> mild hypomyelination | biallelic -> severe leukodystrophy
```

---

## 7. Anatomical Structures Affected

- **Organ level.** Primary: **skin** (integumentary system) and **brain/central white matter** (nervous system). Secondary: eyes/oculomotor pathways (nystagmus). Body systems: **integumentary** and **central nervous** systems predominate.
- **Tissue/cell level.** **Epidermis** — keratinocytes/stratum corneum (CL:0000312). **CNS white matter** — oligodendrocytes and myelin sheaths (CL:0000128). Corpus callosum hypoplasia indicates commissural white-matter involvement.
- **Subcellular level.** **Endoplasmic reticulum membrane** (GO:0005789) — site of the ELOVL1 elongation complex; downstream sphingolipid-rich plasma/myelin membranes.
- **Localization (UBERON).** Skin/epidermis (**UBERON:0001003 / UBERON:0001834**), palms and soles (palmoplantar keratoderma), brain white matter (**UBERON:0002316**), corpus callosum (**UBERON:0002336**). Involvement is **bilateral/generalized** (skin) and **symmetric** (central white matter).

---

## 8. Temporal Development

- **Onset.** **Congenital / neonatal** for ichthyosis and hypomyelination; neurological signs (spasticity, movement disorder, developmental delay) emerge and evolve through **infancy and childhood**. Onset pattern is **chronic/insidious**.
- **Progression.** Cutaneous disease is **chronic and lifelong**. **Spasticity is progressive**; developmental delay is 100% penetrant in the biallelic cohort. Notably, brain MRI **hypomyelination is described as non-progressive** ([PMID: 40590574](https://pubmed.ncbi.nlm.nih.gov/40590574/)) — i.e., a static hypomyelination rather than an actively demyelinating course, even as clinical motor signs progress.
- **Disease course pattern.** Progressive neuromotor disability on a background of static white-matter hypomyelination; chronic skin disease.
- **Duration.** Lifelong.
- **Remission / critical periods.** No spontaneous remission. Given that myelination is a developmental process, an **early developmental window** would be the theoretical opportunity for any future disease-modifying (e.g., substrate/lipid-supplementation) intervention — inferred, not demonstrated.

---

## 9. Inheritance and Population

- **Epidemiology.** **Ultra-rare, prevalence <1/1,000,000.** Only a small number of patients are reported worldwide (two founding probands plus subsequent case reports for the dominant form; a 7-patient series for the biallelic form). Precise incidence/prevalence figures are not established.
- **Inheritance patterns.**
  - **Autosomal dominant, de novo:** classic IKSHD via recurrent p.Ser165Phe (no family history in probands) ([PMID: 29496980](https://pubmed.ncbi.nlm.nih.gov/29496980/); [PMID: 42101073](https://pubmed.ncbi.nlm.nih.gov/42101073/)).
  - **Autosomal recessive:** biallelic variants → severe hypomyelinating leukodystrophy ([PMID: 40590574](https://pubmed.ncbi.nlm.nih.gov/40590574/)).
- **Penetrance / expressivity.** High/complete penetrance for the reported pathogenic genotypes; in the biallelic cohort, developmental delay, spasticity, and head tremor were **100% penetrant**. Expressivity is graded by allele dose (mono → milder; biallelic → more severe).
- **Genetic anticipation / mosaicism / founder effects.** Not reported; not a repeat-expansion disorder. Germline mosaicism theoretically possible for de novo cases but undocumented. Consanguinity is relevant for the recessive form (as for AR disorders generally).
- **Carrier frequency.** Not established; expected very low given ultra-rarity.
- **Demographics.** No ethnic predilection established. **Sex ratio ~1:1.** Age distribution: pediatric-onset; affected individuals present from birth/infancy.

---

## 10. Diagnostics

- **Clinical recognition.** The **combination of congenital ichthyosis + spasticity + MRI hypomyelination + dysmorphic facial features (± nystagmus)** should prompt consideration of IKSHD/ELOVL1-related disease.
- **Laboratory / biomarkers.** **Plasma VLCFA profiling** is the key biochemical test: IKSHD shows **reduced** C24:0 and C26:0 (a *deficiency* pattern), which distinguishes it from X-ALD's VLCFA *accumulation* ([PMID: 40590574](https://pubmed.ncbi.nlm.nih.gov/40590574/); [PMID: 42320861](https://pubmed.ncbi.nlm.nih.gov/42320861/)). Fibroblast elongation assays and stable-isotope substrate assays confirm reduced ELOVL1 activity ([PMID: 30487246](https://pubmed.ncbi.nlm.nih.gov/30487246/)).
- **Imaging.** **Brain MRI** demonstrating **hypomyelination** (± corpus callosum hypoplasia) is central; hypomyelination is non-progressive on serial imaging.
- **Genetic testing (definitive).** **Whole-exome (WES) or whole-genome sequencing (WGS)** is the diagnostic method of choice, given IKSHD was defined by WES ([PMID: 29496980](https://pubmed.ncbi.nlm.nih.gov/29496980/)). Targeted single-gene/panel testing for *ELOVL1* (in ichthyosis, leukodystrophy, or hereditary-spastic panels) can confirm the recurrent **c.494C>T (p.Ser165Phe)** or biallelic variants. Chromosomal microarray/karyotype/FISH/mtDNA/repeat-expansion testing are **not applicable** (single-nucleotide disorder).
- **Skin biopsy.** May show ichthyosis-consistent histology (hyperkeratosis); not specific.
- **Differential diagnosis.** X-linked adrenoleukodystrophy and other VLCFA-related leukodystrophies (distinguished by VLCFA *accumulation* vs *deficiency*); other congenital ichthyoses with neurological involvement (e.g., Sjögren–Larsson syndrome — ALDH3A2; MEDNIK; trichothiodystrophy; Chanarin–Dorfman); other hypomyelinating leukodystrophies (e.g., PLP1-related). Genetic testing resolves these.
- **Screening.** No newborn-screening program exists for IKSHD. Cascade genetic testing is relevant in recessive families. (X-ALD newborn screening, based on C26:0-lysoPC elevation, will *not* detect ELOVL1 deficiency, which lowers VLCFAs.)

---

## 11. Outcome / Prognosis

- **Survival/mortality.** No formal survival statistics are published. Unlike neonatal-lethal complete Elovl1 loss in mice (which die from barrier failure; [PMID: 23689133](https://pubmed.ncbi.nlm.nih.gov/23689133/)), human patients survive into childhood and beyond, indicating residual elongase function. Life expectancy is not well defined but the disorder is chronic rather than rapidly fatal.
- **Morbidity/function.** Substantial: progressive spasticity, complex movement disorder, dysarthria, developmental delay, and chronic skin disease produce combined motor, communication, and cognitive disability. Many patients likely require mobility and communication support.
- **Disease course.** Progressive neuromotor decline on static hypomyelination; lifelong ichthyosis. Complications include those of severe spasticity (contractures, mobility loss), swallowing/communication impairment, and skin-barrier–related issues (infection, dehydration).
- **Prognostic factors.** **Allele dose** is the dominant prognostic determinant — biallelic disease is more severe with 100%-penetrant developmental delay/spasticity and corpus callosum hypoplasia, versus milder monoallelic IKSHD. Plasma VLCFA depletion severity is a candidate biochemical prognostic marker (inferred).

---

## 12. Treatment

**No disease-specific or ELOVL1-targeted therapy exists.** Management is **symptomatic and multidisciplinary** ([PMID: 40590574](https://pubmed.ncbi.nlm.nih.gov/40590574/); dermatologic evidence base [PMID: 23870202](https://pubmed.ncbi.nlm.nih.gov/23870202/), [PMID: 36928932](https://pubmed.ncbi.nlm.nih.gov/36928932/)).

**Skin (congenital ichthyosis care).**

| Intervention | Class / mechanism | Evidence | NCIT suggestion |
|---|---|---|---|
| Topical emollients | Barrier repair/hydration | Therapeutic benefit, good safety in systematic review ([PMID: 23870202](https://pubmed.ncbi.nlm.nih.gov/23870202/)) | Emollient |
| Keratolytics (urea, propylene glycol, lactic acid) | Desquamation | Standard of care ([PMID: 36928932](https://pubmed.ncbi.nlm.nih.gov/36928932/)) | Keratolytic Agent |
| Calcipotriol ointment | Vitamin D analog | Benefit + good safety ([PMID: 23870202](https://pubmed.ncbi.nlm.nih.gov/23870202/)) | Calcipotriene |
| Topical retinoids (tazarotene, isotretinoin/TMB-001) | Retinoid; normalizes keratinization | Liarozole benefit ([PMID: 23870202](https://pubmed.ncbi.nlm.nih.gov/23870202/)); Phase IIb TMB-001 reduced scaling ([PMID: 36928932](https://pubmed.ncbi.nlm.nih.gov/36928932/)) | Retinoid |
| Systemic retinoids (acitretin) | Oral retinoid | Effective but limited by teratogenicity/adverse effects ([PMID: 36928932](https://pubmed.ncbi.nlm.nih.gov/36928932/)) | Acitretin |

**Neurological features (symptomatic).** Antispasticity agents (e.g., baclofen, botulinum toxin — NCIT: Baclofen, OnabotulinumtoxinA), physiotherapy, occupational therapy, speech/language therapy, orthopedic management of contractures, and supportive/movement-disorder management. **No controlled trials exist specifically for IKSHD**; neurological care follows generic spasticity/leukodystrophy pathways.

**Advanced/experimental therapeutics.** No approved gene, cell, RNA-based, or targeted therapy. Conceptually, because IKSHD is a *biosynthetic deficiency*, **substrate/lipid-supplementation or elongase-augmentation** strategies are rational future directions (untested). Note that this is opposite to X-ALD, where *substrate-reduction* (e.g., targeting ELOVL1) is a therapeutic goal ([PMID: 42469918](https://pubmed.ncbi.nlm.nih.gov/42469918/)) — highlighting ELOVL1's dual relevance across VLCFA disorders.

**Pharmacogenomics.** None specific to IKSHD.

---

## 13. Prevention

- **Primary prevention.** Not applicable to the genetic cause. **Genetic counseling** is central: recurrence risk is low for de novo dominant cases but ~25% for future pregnancies in recessive families. **Prenatal/preimplantation genetic testing** is feasible once the familial variant is known.
- **Secondary prevention.** Early genetic diagnosis (WES/WGS) enables early institution of skin-barrier care, spasticity management, and developmental/rehabilitation support to limit complications.
- **Tertiary prevention.** Prevent complications of spasticity (contracture prophylaxis via physiotherapy/orthotics), maintain skin-barrier integrity to reduce infection/dehydration, nutritional and communication support.
- **Immunization / public-health / prophylaxis.** Standard pediatric care; no disease-specific vaccine or prophylaxis. Routine infection-prevention measures are prudent given barrier compromise.
- **Counseling.** Genetic counseling for families is recommended, distinguishing de novo dominant (low sibling recurrence, but germline-mosaicism caveat) from recessive (25% recurrence) inheritance.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs.** *Elovl1* is conserved across mammals. Mouse *Elovl1* (NCBI Gene) is the principal experimental ortholog; the enzyme's elongation function is evolutionarily conserved.
- **Natural disease in other species.** No well-characterized naturally occurring *ELOVL1* disorder in companion animals or wildlife is documented (OMIA). The disease knowledge derives from human patients and engineered mouse models rather than spontaneous animal disease.
- **Comparative biology.** The mouse recapitulates key mechanisms: **Elovl1 knockout** causes lethal epidermal-barrier failure with reduced ≥C26 ceramides ([PMID: 23689133](https://pubmed.ncbi.nlm.nih.gov/23689133/)); **Elovl1-deficient mice** show reduced myelin-sphingolipid chain length and impaired motor coordination ([PMID: 32123819](https://pubmed.ncbi.nlm.nih.gov/32123819/)) — demonstrating strong cross-species conservation of both the skin and CNS mechanisms.
- **Transmission.** Not applicable (non-infectious, non-zoonotic).

---

## 15. Model Organisms

- **Mouse (*Mus musculus*)** is the primary model.
  - **Elovl1 knockout:** neonatal-lethal from epidermal permeability-barrier defects; diminished stratum-corneum lipid lamellae and reduced ≥C26 ceramides — establishing ELOVL1 as essential for barrier formation and ceramide chain length ([PMID: 23689133](https://pubmed.ncbi.nlm.nih.gov/23689133/)).
  - **Elovl1-deficient (hypomorphic/partial) mice:** reduced myelin-sphingolipid chain length and poorer motor coordination — modeling the CNS hypomyelination/motor phenotype of human IKSHD ([PMID: 32123819](https://pubmed.ncbi.nlm.nih.gov/32123819/)).
- **In vitro models.** Patient **fibroblasts** and **transfected HEK293 cells** with VLCFA GC-MS profiling and stable-isotope substrate assays quantify ELOVL1 activity and demonstrate the elongation defect and compensatory ELOVL dysregulation ([PMID: 30487246](https://pubmed.ncbi.nlm.nih.gov/30487246/); [PMID: 40590574](https://pubmed.ncbi.nlm.nih.gov/40590574/)).
- **Genetic-model types available.** Knockout and hypomorphic mouse lines; humanized knock-in models carrying p.Ser165Phe would be a valuable (not-yet-reported) resource.
- **Phenotype recapitulation.** Excellent for both compartments: skin-barrier/ceramide defect and myelin-sphingolipid/motor-coordination defect are both reproduced.
- **Limitations.** Complete knockout is neonatally lethal (barrier failure), limiting study of the CNS phenotype in nulls; dysmorphic facial features and the human dominant-variant–specific effects are not well captured by simple knockouts.

---

## Key Findings (with statistical evidence)

**F001 — IKSHD is caused by a recurrent de novo heterozygous *ELOVL1* p.Ser165Phe.** WES in two unrelated pediatric probands without family history identified a shared novel heterozygous *ELOVL1* variant; the same **c.494C>T (p.Ser165Phe)** de novo variant was independently confirmed in additional patients. *"To identify the cause of a similar phenotype of ichthyotic keratoderma, spasticity, mild hypomyelination (on MRI) and dysmorphic features (IKSHD)..."* ([PMID: 29496980](https://pubmed.ncbi.nlm.nih.gov/29496980/)); *"Genetic analysis identified the de novo pathogenic variant p.Ser165Phe in ELOVL1."* ([PMID: 42101073](https://pubmed.ncbi.nlm.nih.gov/42101073/)).

**F002 — ELOVL1 elongates C22–C26 VLCFAs required for skin barrier and myelin.** *"Elovl1 knockout mice died shortly after birth due to epidermal barrier defects"* and *"Elovl1 is a key determinant of epidermal Cer chain length and is essential for permeability barrier formation"* ([PMID: 23689133](https://pubmed.ncbi.nlm.nih.gov/23689133/)); *"ELOVL fatty acid elongase 1 catalyses elongation of saturated and monounsaturated C22-C26-VLCFAs"* ([PMID: 30487246](https://pubmed.ncbi.nlm.nih.gov/30487246/)).

**F003 — Elovl1-deficient mice recapitulate CNS features.** *"Reduced chain length in myelin sphingolipids and poorer motor coordination in mice deficient in the fatty acid elongase"* — linking Elovl1 loss to the hypomyelination/motor phenotype ([PMID: 32123819](https://pubmed.ncbi.nlm.nih.gov/32123819/)).

**F004 — Biallelic *ELOVL1* variants cause a more severe hypomyelinating leukodystrophy.** In 7 patients: *"Common clinical features included ichthyosis (5/7), developmental delay (7/7), progressive spasticity (7/7), nystagmus (5/6), and a complex movement disorder characterized by pronounced head tremor (7/7), myoclonus (6/7), and dysarthria (6/6)"*; *"Brain MRI revealed non-progressive hypomyelination (6/6) and hypoplasia of the corpus callosum (5/6)"*; *"Plasma VLCFA analysis in one patient showed reduced concentrations of C24:0 and C26:0"* ([PMID: 40590574](https://pubmed.ncbi.nlm.nih.gov/40590574/)).

**F005 — IKSHD is a VLCFA-biosynthesis defect, opposite to VLCFA-catabolism leukodystrophies.** *"Variants in genes encoding enzymes responsible for catalyzing the first and rate limiting step in the production of VLCFAs, elongation of VLCFAs (ELOVLs), underlie a novel group of metabolic disorders"* ([PMID: 40590574](https://pubmed.ncbi.nlm.nih.gov/40590574/)); contrast with *"X-linked adrenoleukodystrophy (ALD)... resulting in the systemic accumulation of very-long-chain fatty acids (VLCFAs)"* ([PMID: 42320861](https://pubmed.ncbi.nlm.nih.gov/42320861/)).

**F006 — ELOVL1 performs the rate-limiting condensation step of the ER four-enzyme elongation cycle.** *"Elongation occurs in the endoplasmic reticulum (ER) through the actions of a complex of four ER-embedded enzymes, which includes the ELOVL proteins"* and *"which catalyze the first and rate-limiting step of the FA elongation cycle"* ([PMID: 39946831](https://pubmed.ncbi.nlm.nih.gov/39946831/)); *"the fatty acid elongases can be divided into two major groups: (a) enzymes... involved in the elongation of saturated and monounsaturated VLCFA (ELOVL1, 3 and 6)"* ([PMID: 16564093](https://pubmed.ncbi.nlm.nih.gov/16564093/)).

**F007 — No disease-specific therapy; management is symptomatic.** *"Topical treatments including emollients, calcipotriol ointment, and liarozole cream seem to have therapeutic benefit and a good safety profile"* ([PMID: 23870202](https://pubmed.ncbi.nlm.nih.gov/23870202/)); *"Emollients and keratolytics are frequently used to manage symptoms of congenital ichthyosis... Systemic retinoid treatment is complicated by teratogenicity and dose-limiting adverse effects"* ([PMID: 36928932](https://pubmed.ncbi.nlm.nih.gov/36928932/)).

**F008 — Genotype–phenotype architecture is a graded severity spectrum.** *"Monoallelic pathogenic variants in ELOVL1 have been described in association to a condition characterized by ichthyosis, spasticity, nystagmus and cerebral hypomyelination, although a similar but more severe presentation has been reported in patients with biallelic variants"* ([PMID: 42101073](https://pubmed.ncbi.nlm.nih.gov/42101073/)); *"biallelic variants in ELOVL1 are associated with a unique and recognizable phenotype of hypomyelinating leukodystrophy, ichthyosis, and a complex movement disorder including progressive spastic..."* ([PMID: 40590574](https://pubmed.ncbi.nlm.nih.gov/40590574/)).

---

## Mechanistic Model / Interpretation

IKSHD is best understood as a **single upstream biochemical lesion — deficient VLCFA elongation — producing two downstream tissue-specific lipid deficiencies**. Because ELOVL1 catalyzes the rate-limiting condensation step of ER fatty-acid elongation, its dysfunction throttles the supply of C22–C26+ VLCFAs. Those VLCFAs are the acyl backbones of two critical lipid classes: **epidermal ceramides** (whose ultra-long chains build the stratum-corneum lipid lamellae) and **myelin sphingolipids** (whose chain length underpins white-matter integrity). Depleting the first yields **ichthyotic keratoderma**; depleting the second yields **hypomyelination**, from which upper-motor-neuron dysfunction (spasticity) and a complex movement disorder emerge. The mouse genetics cleanly separate and confirm both arms: complete knockout kills neonates through the skin arm, while partial deficiency reveals the myelin/motor arm.

The **allele-dose gradient** — mild monoallelic IKSHD versus severe biallelic leukodystrophy — is the disorder's most instructive genetic feature and implies a **quantitative threshold** relationship between residual elongase output and phenotype severity. This threshold logic also frames the therapeutic hypothesis: because the defect is a *deficiency*, restoring VLCFA supply (substrate/lipid supplementation, or enhancing residual/paralogous elongase activity) is mechanistically rational — the inverse of X-ALD, where the therapeutic aim is to *reduce* VLCFAs (even using ELOVL1 as a drug target). Positioning IKSHD opposite X-ALD on a single VLCFA axis is both diagnostically useful (plasma VLCFAs low vs high) and conceptually unifying.

---

## Evidence Base

| PMID | Contribution | Type |
|---|---|---|
| [29496980](https://pubmed.ncbi.nlm.nih.gov/29496980/) | Defines IKSHD; dominant *ELOVL1* variant in 2 unrelated probands | Human clinical |
| [30487246](https://pubmed.ncbi.nlm.nih.gov/30487246/) | De novo *ELOVL1* mutation; enzyme substrate specificity (C22–C26 VLCFA) | Human clinical + in vitro |
| [42101073](https://pubmed.ncbi.nlm.nih.gov/42101073/) | Confirms recurrent de novo p.Ser165Phe; states mono vs biallelic gradient | Human clinical |
| [40590574](https://pubmed.ncbi.nlm.nih.gov/40590574/) | Biallelic *ELOVL1* → severe leukodystrophy; phenotype frequencies; reduced plasma C24:0/C26:0 | Human clinical + in vitro |
| [23689133](https://pubmed.ncbi.nlm.nih.gov/23689133/) | Elovl1-KO mouse: barrier failure, reduced ≥C26 ceramides | Model organism |
| [32123819](https://pubmed.ncbi.nlm.nih.gov/32123819/) | Elovl1-deficient mouse: shortened myelin sphingolipids, motor deficits | Model organism |
| [39946831](https://pubmed.ncbi.nlm.nih.gov/39946831/) | ELOVL biology; ER four-enzyme complex; rate-limiting step | Review |
| [16564093](https://pubmed.ncbi.nlm.nih.gov/16564093/) | ELOVL1/3/6 elongate saturated/monounsaturated VLCFA | Review |
| [42320861](https://pubmed.ncbi.nlm.nih.gov/42320861/) | X-ALD VLCFA accumulation (contrast) | Human clinical |
| [42469918](https://pubmed.ncbi.nlm.nih.gov/42469918/) | ELOVL1 as substrate-reduction target in ALD (contrast/therapeutics) | Review |
| [23870202](https://pubmed.ncbi.nlm.nih.gov/23870202/) | Systematic review of congenital-ichthyosis treatments | Systematic review |
| [36928932](https://pubmed.ncbi.nlm.nih.gov/36928932/) | Topical isotretinoin (TMB-001) Phase IIb in congenital ichthyosis | Clinical trial |
| [41165046](https://pubmed.ncbi.nlm.nih.gov/41165046/) | Commentary on the biallelic *ELOVL1* series | Correspondence |

**Note on citation:** [PMID: 32123819](https://pubmed.ncbi.nlm.nih.gov/32123819/) was flagged as a snippet-abstract mismatch during investigation; the finding it supports (Elovl1 deficiency → shortened myelin sphingolipids and motor deficits) is corroborated by the broader mechanistic literature and the biallelic-patient VLCFA data, but the exact quote should be re-verified against the source.

---

## Limitations and Knowledge Gaps

1. **Very small evidence base.** The disorder rests on a handful of case reports (dominant form) and a single 7-patient series (biallelic form); frequencies, penetrance, and natural history are imprecise.
2. **Prognosis/survival data are absent.** No formal life-expectancy or survival statistics exist.
3. **Molecular mechanism of the dominant p.Ser165Phe** (simple loss-of-function vs dominant-negative on the ER complex) is not definitively resolved.
4. **Human brain lipidomics** directly demonstrating shortened myelin sphingolipids in patients are lacking; the CNS mechanism is largely inferred from mouse.
5. **No epigenetic, transcriptomic, or proteomic disease signatures** have been reported.
6. **No therapeutic trials** target the underlying VLCFA deficiency; all skin-treatment evidence is extrapolated from congenital ichthyosis generally.
7. **One key mouse citation had a snippet mismatch** and warrants source re-verification.
8. **Ontology mapping** (MONDO, ICD-11, Orphanet ORPHAcode) is incompletely standardized for this newly delineated entity.

---

## Proposed Follow-up Experiments / Actions

1. **Establish a patient registry** capturing dominant vs biallelic genotypes with longitudinal MRI, plasma VLCFA, motor, and dermatologic outcomes to define natural history and prognosis.
2. **Generate a humanized p.Ser165Phe knock-in mouse** to test whether the dominant variant acts by loss-of-function or dominant-negative mechanism and to model the CNS phenotype without neonatal lethality.
3. **Perform patient plasma/CSF and, where available, brain lipidomics** to directly confirm VLCFA-ceramide and myelin-sphingolipid depletion and to identify candidate biomarkers of severity.
4. **Test VLCFA/lipid-supplementation and elongase-augmentation strategies** in patient fibroblasts and mouse models as a mechanism-based therapeutic proof-of-concept (the inverse of X-ALD substrate reduction).
5. **Screen paralogous elongases (ELOVL3/6/7) and ceramide-synthesis genes** as modifiers to explain the mono-to-biallelic severity gradient.
6. **Standardize diagnostics:** promote plasma VLCFA profiling (deficiency pattern) plus *ELOVL1* sequencing as a combined diagnostic panel, and formalize MONDO/ICD-11/Orphanet coding.
7. **Re-verify the mouse myelin-sphingolipid citation** ([PMID: 32123819](https://pubmed.ncbi.nlm.nih.gov/32123819/)) against the primary source.

---

*Report compiled from a 5-iteration autonomous investigation: 8 confirmed findings, 24 papers reviewed. Evidence types span human clinical case reports/series, model-organism (mouse), and in vitro/biochemical studies.*


## Artifacts

- [OpenScientist final report](Ichthyotic_Keratoderma_Spasticity_Hypomyelination_And_Dysmorphic_Facial_Features-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Ichthyotic_Keratoderma_Spasticity_Hypomyelination_And_Dysmorphic_Facial_Features-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 13 |
| On topic | 5 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:40590574` *(abstract only)*: "hypomyelinating leukodystrophy, movement disorder, and ichthyosis"
  - closest text in source: "CONCLUSIONS: We show that biallelic variants in ELOVL1 are associated with a unique and recognizable phenotype of hypomyelinating leukodystrophy, ichthyosis, and a complex movement disorder including progressive spasticity, head tremor, and myoclonus"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 18 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002346` (1 mention) - the report calls it "Neurological sign"; HP calls it **Head tremor**
- `HP:0001260` (1 mention) - the report calls it "Neurological sign"; HP calls it **Dysarthria**
- `HP:0001336` (1 mention) - the report calls it "Neurological sign"; HP calls it **Myoclonus**
- `HP:0000639` (1 mention) - the report calls it "Neuro-ophthalmic sign"; HP calls it **Nystagmus**
- `HP:0002079` (1 mention) - the report calls it "Imaging abnormality"; HP calls it **Hypoplasia of the corpus callosum**
- `HP:0001999` (1 mention) - the report calls it "Physical sign"; HP calls it **Abnormal facial shape**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001263` (1 mention) - the report calls it "Behavioral/cognitive"; HP calls it **Global developmental delay**, and lists "Cognitive delay" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005789` - called "endoplasmic reticulum membrane", "Endoplasmic reticulum membrane"