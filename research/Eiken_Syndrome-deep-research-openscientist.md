---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-24T16:12:01.919714'
end_time: '2026-09-24T16:44:09.691193'
duration_seconds: 1927.77
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Eiken Syndrome
  mondo_id: MONDO:0010803
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
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 17
  on_topic: 10
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 34
  verified: 30
  not_found: 2
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.062
  labels_checked: 25
  labels_matching: 11
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: HP:0001156
    reported_labels:
    - Physical
    ontology_label: Brachydactyly
  - term_id: HP:0100671
    reported_labels:
    - related
    ontology_label: Abnormal trabecular bone morphology
  - term_id: HP:0010580
    reported_labels:
    - related
    ontology_label: Enlarged epiphyses
  - term_id: HP:0010579
    reported_labels:
    - Radiographic sign
    ontology_label: Cone-shaped epiphysis
  - term_id: HP:0008821
    reported_labels:
    - related
    ontology_label: Hypoplastic inferior ilia
  - term_id: HP:0004322
    reported_labels:
    - Physical
    ontology_label: Short stature
  - term_id: HP:0002901
    reported_labels:
    - Lab abnormality
    ontology_label: Hypocalcemia
  - term_id: HP:0002905
    reported_labels:
    - Lab abnormality
    ontology_label: Hyperphosphatemia
  - term_id: UBERON:0002472
    reported_labels:
    - epiphysis, related
    ontology_label: stylopod
  - term_id: UBERON:0009853
    reported_labels:
    - pubic symphysis
    ontology_label: body of uterus
  labels_variant: 4
  unresolved_terms:
  - HP:0002662
  - HP:0006348
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Eiken_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Eiken_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Eiken Syndrome
- **MONDO ID:** MONDO:0010803 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Eiken Syndrome** covering all of the
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

# Eiken Syndrome: A Comprehensive Disease Characteristics Report

**Disease:** Eiken Syndrome (Eiken familial skeletal dysplasia)
**MONDO ID:** MONDO:0010803 · **OMIM:** #600002 · **Orphanet:** ORPHA:79106 · **UMLS:** C1854486
**Category:** Mendelian (autosomal recessive skeletal dysplasia)
**Causal gene:** *PTH1R* (HGNC:9608; OMIM \*168468; NCBI Gene 5745; locus 3p21.31)

---

## Summary

Eiken syndrome is an **ultra-rare autosomal-recessive skeletal dysplasia** caused by **biallelic (homozygous) hypomorphic/altered-function variants in *PTH1R***, the gene encoding the parathyroid hormone / parathyroid hormone-related peptide receptor type 1 (the PTH/PTHrP receptor). First described by Eiken and colleagues in 1984 in three brothers from a consanguineous Danish family, the disorder is defined radiographically by **severely delayed (retarded) endochondral ossification** — especially of the epiphyses, pelvis, hands and feet — together with **abnormal bone modeling, brachydactyly, coarse trabeculae, supernumerary/pseudo-epiphyses, and primary failure of tooth eruption**. Only about **four to five unrelated families** have been reported worldwide since 1984, spanning European, Indian, and East-African ancestries. Affected individuals have normal intelligence, normal lifespan, and are normal at birth, with skeletal abnormalities becoming apparent during childhood growth.

Mechanistically, Eiken syndrome occupies the **mild, non-lethal middle of the *PTH1R* allelic spectrum**. PTH1R is a class B G-protein-coupled receptor that, through the PTHrP–Indian hedgehog (Ihh) feedback loop, paces the proliferation and hypertrophic differentiation of growth-plate chondrocytes and therefore the timing of endochondral ossification. Eiken-associated mutations — distributed across the extracellular domain (E35K, Y134S), the transmembrane helices (I237N, D241E), and the intracellular C-terminal tail (R485X) — **bias receptor signaling**: cell-based assays show *increased basal cAMP tone* combined with *impaired β-arrestin2 recruitment and defective desensitization* of the PTHrP response. Because sustained PTHrP-type signaling delays chondrocyte hypertrophy (the mirror image of the accelerated ossification seen in complete loss-of-function Blomstrand lethal chondrodysplasia), the net effect is **delayed ossification** — the phenotypic hallmark of Eiken syndrome. A transmembrane-helix-2 subset of variants additionally produces overt **PTH resistance** (hypocalcemia, hyperphosphatemia), placing those patients at the interface with pseudohypoparathyroidism-like disorders.

The evidence base is exclusively **case-report and in-vitro functional-assay level**; there are no registries, natural-history cohorts, quality-of-life instruments, or omics datasets specific to Eiken syndrome. Management is entirely **supportive** — calcium and active vitamin D for the PTH-resistant subset, orthopedic and dental care, and genetic counseling for consanguineous families. No targeted or curative therapy exists. Humanized *PTH1R* knock-in mice and conditional/global mouse models of the PTHrP–PTH1R axis reproduce key skeletal phenotypes and provide the primary in-vivo platform for the disease family.

---

## Key Findings

### F001 — Eiken syndrome is caused by biallelic hypomorphic *PTH1R* mutations, inherited autosomal-recessively

The original 1984 description of three affected brothers from a consanguineous family established autosomal recessive inheritance on clinical/pedigree grounds, with the authors noting that *"Parental consanguinity suggest an autosomal recessive inheritance"* ([PMID: 6734674](https://pubmed.ncbi.nlm.nih.gov/6734674/)). Molecular confirmation came later: *"Eiken syndrome is a very rare skeletal dysplasia due to bi-allelic variants in PTH1R"* ([PMID: 29987841](https://pubmed.ncbi.nlm.nih.gov/29987841/)). The reported causal alleles are homozygous and span multiple receptor domains — **R485X** (C-terminal tail truncation), **E35K** and **Y134S** (extracellular domain), and the newer transmembrane-helix-2 variants **I237N** and **D241E**. The second reported case carried homozygous **c.103G>A p.(Glu35Lys)** ([PMID: 29987841](https://pubmed.ncbi.nlm.nih.gov/29987841/)). A recent review summarizing homozygous *PTH1R* disorders states that *"homozygous mutations located in the transmembrane helices, extracellular domains and C-tail of the PTH1R were identified in patients with milder conditions characterized by variable degrees of skeletal and mineral abnormalities. These include delayed ossification in Eiken syndrome"* ([PMID: 40904804](https://pubmed.ncbi.nlm.nih.gov/40904804/)). The disorder is ultra-rare, with only ~4–5 families known.

### F002 — Eiken mutations bias PTH1R signaling: increased basal cAMP with impaired β-arrestin recruitment

The defining molecular signature of Eiken syndrome is not simple loss or gain of function but a **rebalancing of the receptor's signaling outputs**. In HEK293 cell assays, *"R485X increases the receptor's basal rate of cAMP signaling and decreases its capacity to recruit β-arrestin2 upon ligand stimulation. The E35K and Y134S mutations each weaken the binding of PTHrP leading to impaired β-arrestin2 recruitment and desensitization of cAMP signaling response to PTHrP but not PTH"* ([PMID: 37268817](https://pubmed.ncbi.nlm.nih.gov/37268817/)). The authors conclude that *"Our findings support a critical role for interaction with β-arrestin in the mechanism by which the PTH1R regulates bone formation"* ([PMID: 37268817](https://pubmed.ncbi.nlm.nih.gov/37268817/)). The transmembrane-helix-2 variants behave similarly at the cAMP level: functional analysis *"demonstrated increased basal cAMP signaling for both variants, with relative blunting of responses to both PTH and PTH-related peptide (PTHrP) ligands"* ([PMID: 39276366](https://pubmed.ncbi.nlm.nih.gov/39276366/)). The common thread is **elevated ligand-independent (basal) cAMP tone combined with defective desensitization/β-arrestin signaling**, particularly toward PTHrP.

### F003 — The PTH1R/PTHrP–Indian hedgehog loop controls chondrocyte differentiation timing, explaining delayed ossification

The skeletal phenotype is explained by the physiological role of PTH1R signaling in the growth plate. PTHrP acts through PTH1R as an autocrine/paracrine brake on chondrocyte hypertrophic differentiation, and is itself induced by Ihh in a negative-feedback loop. Loss of the signal accelerates differentiation: *"Mice lacking PTHrP show accelerated chondrocyte differentiation, and thus premature ossification of those bones that are formed through an endochondral process"* ([PMID: 10912527](https://pubmed.ncbi.nlm.nih.gov/10912527/)). Excess signal does the opposite: *"a severe delay in chondrocyte differentiation and endochondral ossification, is observed in transgenic mice that overexpress PTHrP"* ([PMID: 10912527](https://pubmed.ncbi.nlm.nih.gov/10912527/)) — the **same phenotypic direction as Eiken syndrome**. This bracketing is reinforced by the contrast with the lethal end of the spectrum, which is *"incompatible with life as in Blomstrand's lethal chondrodysplasia, characterized by accelerated growth plate ossification"* ([PMID: 40904804](https://pubmed.ncbi.nlm.nih.gov/40904804/)). Because Eiken variants sustain PTHrP-type (basal cAMP) signaling tone, they delay hypertrophic differentiation and therefore delay ossification.

### F004 — Clinical phenotype: severely delayed ossification, abnormal modeling, brachydactyly, dental and PTH-resistance features

The core radiographic phenotype comprises *"delayed ossification of bone including the epiphyses, pubic symphysis, and primary ossification centers of the short tubular bones, coarse bone trabeculae, and modeling abnormalities"* ([PMID: 29987841](https://pubmed.ncbi.nlm.nih.gov/29987841/)). The original report described *"an excessively retarded ossification, principally of the epiphyses, the pelvis, the hands and the feet, are reported. In the hands and feet the retarded ossification is combined with an abnormal modeling of the bones"* ([PMID: 6734674](https://pubmed.ncbi.nlm.nih.gov/6734674/)); patients were normal at birth, with predicted moderate dwarfism, **no mental retardation**, and normal chromosomes and urine mucopolysaccharides. Additional features include supernumerary epiphyses of the tubular bones of the hands and primary failure of tooth eruption. The PTH-resistant subset (TM2 variants) show a shared skeletal signature: *"Both patients shared skeletal features, including brachydactyly, extensive metacarpal pseudo-epiphyses, elongated cone-shaped epiphyses, ischiopubic hypoplasia, and deficient sacral ossification, suggestive of Eiken syndrome"* together with **hypocalcemia and elevated serum phosphate** ([PMID: 39276366](https://pubmed.ncbi.nlm.nih.gov/39276366/)).

### F005 — *PTH1R* is an allelic-series gene: Eiken sits between lethal Blomstrand, activating Jansen, and dominant PFE

*PTH1R* is a paradigmatic allelic-series gene, and understanding Eiken requires positioning it within that series. Homozygous mutations produce a graded set of phenotypes: *"These include delayed ossification in Eiken syndrome, hypocalcemia in a pseudohypoparathyroidism-like disorder, and non-syndromic primary failure of tooth eruption; which is usually caused by heterozygous PTH1R mutations"* ([PMID: 40904804](https://pubmed.ncbi.nlm.nih.gov/40904804/)). The dominant, heterozygous end of the spectrum — non-syndromic primary failure of tooth eruption (PFE) — operates by **haploinsufficiency**: *"Heterozygous mutations in the parathyroid hormone 1 receptor (PTH1R) gene have been shown to cause PFE likely due to protein haploinsufficiency"* ([PMID: 23771181](https://pubmed.ncbi.nlm.nih.gov/23771181/)); in that study 12/30 variants were pathogenic across 70 PFE index cases. Some PFE mutants act by a dominant-negative mechanism: *"the PTH1R mutants are functionally inactive and mutant PTH1R/Gly452Glu has a dominant negative effect on the signaling of PTH1R wild type. Confocal imaging revealed that wild type PTH1R is expressed on the cell surface, whereas PTH1R/Gly452Glu mutant is mostly retained inside the cell"* ([PMID: 27898723](https://pubmed.ncbi.nlm.nih.gov/27898723/)).

| Disorder | Zygosity | Functional effect | Ossification/skeletal effect | Inheritance |
|---|---|---|---|---|
| Jansen metaphyseal chondrodysplasia | Heterozygous | Constitutively **activating** | Delayed differentiation, metaphyseal dysplasia, hypercalcemia | AD |
| **Eiken syndrome** | **Homozygous** | **Hypomorphic / biased (↑basal cAMP, ↓β-arrestin)** | **Severely delayed ossification, modeling defects** | **AR** |
| Pseudohypoparathyroidism-like disorder | Homozygous | Reduced PTH responsiveness | Hypocalcemia, hyperphosphatemia (PTH resistance) | AR |
| Blomstrand lethal chondrodysplasia | Homozygous | Complete **loss of function** | Accelerated growth-plate ossification; perinatally lethal | AR |
| Primary failure of tooth eruption (PFE) | Heterozygous | Haploinsufficiency / dominant-negative | Failed tooth eruption, posterior open bite | AD (incomplete penetrance) |

### F006 — Humanized and conditional mouse models recapitulate *PTH1R* skeletal phenotypes

Mouse genetics provide the in-vivo backbone for the disease family. A humanized *PTH1R* knock-in strain reproduces a skeletal phenotype: *"Introduction of the p.E469K substitution into humanized PTH1R mice resulted in mildly increased mineralization of bones in the paws as well as shortening of long bones"* ([PMID: 41031626](https://pubmed.ncbi.nlm.nih.gov/41031626/)). Conditional deletion demonstrates PTH1R's role in digit segmentation: *"PTH1R deletion caused symphalangism, demonstrating another novel function of PTH1R signaling in digit formation"* ([PMID: 26620087](https://pubmed.ncbi.nlm.nih.gov/26620087/)). Together with the global PTHrP-null/PTH1R-null (accelerated ossification) and PTHrP-overexpressing (delayed ossification) models ([PMID: 10912527](https://pubmed.ncbi.nlm.nih.gov/10912527/)), these systems bracket the Eiken phenotypic direction and are the natural platform for testing disease mechanism and future therapeutics.

### F007 — Ultra-rare autosomal-recessive dysplasia with defined ontology identifiers and case-report-only evidence

Eiken syndrome carries stable identifiers: **OMIM #600002; MONDO:0010803; Orphanet ORPHA:79106; UMLS C1854486; ICD-10 Q78.8** (no dedicated code). Its causal gene *PTH1R* maps to **3p21.31** (HGNC:9608, OMIM \*168468, NCBI Gene 5745). Orphanet lists prevalence as **<1/1,000,000 ("unknown")**. Only ~4–5 unrelated families have been reported since 1984: the original Danish consanguineous family of three affected brothers ([PMID: 6734674](https://pubmed.ncbi.nlm.nih.gov/6734674/) — *"Three brothers with a constitutional skeletal dysplasia characterized by an excessively retarded ossification, principally of the epiphyses, the pelvis, the hands and the feet, are reported"*), a second case from India ([PMID: 29987841](https://pubmed.ncbi.nlm.nih.gov/29987841/) — *"Only one affected family has been known to-date"*), a third family ([PMID: 31297790](https://pubmed.ncbi.nlm.nih.gov/31297790/)), and an East-African family with PTH resistance ([PMID: 39276366](https://pubmed.ncbi.nlm.nih.gov/39276366/)). Both sexes are affected; consanguinity is the principal risk context. All evidence is case-report level.

---

## Report by Template Section

### 1. Disease Information

Eiken syndrome is a **constitutional (developmental) skeletal dysplasia** characterized by markedly delayed and abnormal endochondral ossification with abnormal bone modeling, brachydactyly, and dental abnormalities, caused by biallelic variants in *PTH1R*. **Key identifiers:** OMIM #600002; MONDO:0010803; Orphanet ORPHA:79106; UMLS C1854486; ICD-10 Q78.8 (no unique code); MeSH — no dedicated descriptor (indexed under skeletal dysplasias / *PTH1R*-related disorders). **Synonyms/alternative names:** "Eiken familial skeletal dysplasia"; "Eiken skeletal dysplasia"; historically "a new familial skeletal dysplasia with severely retarded ossification and abnormal modeling of bones" ([PMID: 6734674](https://pubmed.ncbi.nlm.nih.gov/6734674/)). **Source of information:** disease-level aggregated resources (OMIM, Orphanet) plus a small number of individual patient case reports; no EHR-derived cohorts exist.

### 2. Etiology

**Causal factor:** purely genetic — biallelic hypomorphic/biased-function *PTH1R* variants ([PMID: 29987841](https://pubmed.ncbi.nlm.nih.gov/29987841/), [PMID: 40904804](https://pubmed.ncbi.nlm.nih.gov/40904804/)). **Genetic risk factors:** homozygosity for a pathogenic *PTH1R* allele; **consanguinity** is the dominant risk context (original family was consanguineous, [PMID: 6734674](https://pubmed.ncbi.nlm.nih.gov/6734674/)). No susceptibility loci, modifier genes, protective alleles, environmental risk/protective factors, or gene–environment interactions have been identified — consistent with a fully penetrant single-gene Mendelian disorder. **Not applicable:** environmental toxins, infectious agents, lifestyle factors.

### 3. Phenotypes

Phenotypes are **physical manifestations, clinical signs, and laboratory abnormalities**; there are no behavioral phenotypes (intelligence is normal, [PMID: 6734674](https://pubmed.ncbi.nlm.nih.gov/6734674/)). Onset is **not congenital in appearance** (normal at birth) but becomes apparent in **childhood** as ossification fails to progress; the course is chronic and non-progressive after skeletal maturity.

| Phenotype | Type | HPO suggestion | Onset / frequency |
|---|---|---|---|
| Delayed/retarded ossification of epiphyses | Radiographic sign | HP:0002662 (Delayed epiphyseal ossification) | Childhood; hallmark (all cases) |
| Delayed ossification of pubic symphysis / pelvis | Radiographic sign | HP:0008788 (Delayed pelvic bone ossification) | Childhood; frequent |
| Brachydactyly | Physical | HP:0001156 | Frequent |
| Abnormal bone modeling (hands/feet) | Radiographic sign | HP:0011314 (Abnormal diaphysis morphology) | Hallmark |
| Coarse bone trabeculae | Radiographic sign | HP:0100671 (related) | Frequent |
| Supernumerary/pseudo-epiphyses | Radiographic sign | HP:0010580 (related) | Reported |
| Cone-shaped epiphyses | Radiographic sign | HP:0010579 | PTH-resistant subset |
| Ischiopubic hypoplasia / deficient sacral ossification | Radiographic sign | HP:0008821 (related) | PTH-resistant subset |
| Primary failure of tooth eruption | Dental sign | HP:0006348 (related) | Reported |
| Short stature / moderate dwarfism | Physical | HP:0004322 | Predicted/variable |
| Hypocalcemia | Lab abnormality | HP:0002901 | PTH-resistant subset |
| Hyperphosphatemia | Lab abnormality | HP:0002905 | PTH-resistant subset |

Quality-of-life impact is not formally measured; functional impact is primarily skeletal/orthopedic and dental, with normal cognition and lifespan.

### 4. Genetic / Molecular Information

**Causal gene:** *PTH1R* (HGNC:9608; OMIM \*168468; NCBI Gene 5745; 3p21.31), a class B GPCR. **Reported pathogenic variants:** R485X (nonsense, C-tail truncation), E35K / c.103G>A p.(Glu35Lys) (missense, extracellular), Y134S (missense, extracellular), I237N and D241E (missense, transmembrane helix 2). **Variant classification:** pathogenic/likely pathogenic per ACMG in the context of biallelic segregation and functional data. **Variant types:** predominantly missense plus one nonsense; **germline**, homozygous. **Allele frequencies:** extremely rare/absent in gnomAD (private to individual consanguineous families). **Functional consequence:** biased/altered function — increased basal cAMP with impaired β-arrestin2 recruitment and defective desensitization ([PMID: 37268817](https://pubmed.ncbi.nlm.nih.gov/37268817/), [PMID: 39276366](https://pubmed.ncbi.nlm.nih.gov/39276366/)) — rather than clean LOF or GOF. **Modifier genes / epigenetics / chromosomal abnormalities:** none reported (chromosomes normal, [PMID: 6734674](https://pubmed.ncbi.nlm.nih.gov/6734674/)).

### 5. Environmental Information

**Not applicable.** Eiken syndrome is a monogenic Mendelian disorder. No environmental toxins, radiation, pollution, occupational exposures, lifestyle factors, or infectious agents are implicated. The only relevant non-genetic contributor is **consanguinity** (a demographic/social factor increasing homozygosity risk).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A **biallelic hypomorphic *PTH1R* variant** (extracellular E35K/Y134S, TM2 I237N/D241E, or C-tail R485X) is inherited → **leads to** an altered PTH/PTHrP receptor.
2. The mutant receptor **biases signaling**: *increased basal (ligand-independent) cAMP tone* plus *impaired β-arrestin2 recruitment and defective desensitization*, especially of the PTHrP response → **results in** dysregulated, poorly-terminated Gαs–cAMP–PKA signaling in chondrocytes ([PMID: 37268817](https://pubmed.ncbi.nlm.nih.gov/37268817/), [PMID: 39276366](https://pubmed.ncbi.nlm.nih.gov/39276366/)).
3. Sustained PTHrP-type signaling tone in the growth plate **maintains chondrocytes in the proliferative state and delays hypertrophic differentiation** (the mirror image of PTHrP loss) → **leads to** slowed transition from cartilage to bone within the PTHrP–Ihh feedback loop ([PMID: 10912527](https://pubmed.ncbi.nlm.nih.gov/10912527/)).
4. Delayed hypertrophic differentiation **delays endochondral ossification** of epiphyses, pelvis, and short tubular bones and **perturbs bone modeling** → **results in** the radiographic hallmarks (delayed ossification, coarse trabeculae, modeling abnormalities, pseudo-epiphyses) ([PMID: 29987841](https://pubmed.ncbi.nlm.nih.gov/29987841/), [PMID: 6734674](https://pubmed.ncbi.nlm.nih.gov/6734674/)).
5. **Branch (TM2 variants):** the same receptor defect additionally **impairs PTH-dependent renal/mineral signaling** → **results in** PTH resistance with hypocalcemia and hyperphosphatemia ([PMID: 39276366](https://pubmed.ncbi.nlm.nih.gov/39276366/)).
6. **Branch (tooth eruption):** PTH1R signaling is required in the dental follicle for eruption → its impairment **leads to** primary failure of tooth eruption (also the phenotype of heterozygous *PTH1R* haploinsufficiency, [PMID: 23771181](https://pubmed.ncbi.nlm.nih.gov/23771181/)).

*(Step 3's precise coupling between "increased basal cAMP" and "delayed differentiation" is inferred from the PTHrP-overexpression mouse phenotype and the LOF/Blomstrand contrast rather than demonstrated directly in Eiken tissue.)*

**Molecular pathways:** PTH1R → Gαs → adenylyl cyclase → cAMP → PKA; and β-arrestin-mediated desensitization/signaling; upstream integration with **Indian hedgehog (Ihh)** signaling in the PTHrP–Ihh loop. Related transcriptional control: **Atf4** activates *Ihh* transcription and its loss causes delayed ossification — *"Ablation of Atf4 (Atf4(-/-)) in mice leads to severe skeletal defects, including delayed ossification... The expression of Indian hedgehog (Ihh) is markedly decreased"* ([PMID: 19906842](https://pubmed.ncbi.nlm.nih.gov/19906842/)). **Cellular processes:** growth-plate chondrocyte proliferation and hypertrophic differentiation, endochondral ossification. **Protein dysfunction:** biased GPCR signaling; the R485X truncation removes C-tail regulatory elements; the dominant-negative PFE mutant (Gly452Glu) is intracellularly retained ([PMID: 27898723](https://pubmed.ncbi.nlm.nih.gov/27898723/)). **Biochemical abnormalities:** dysregulated cAMP; in the TM2 subset, hypocalcemia/hyperphosphatemia. **Suggested GO terms:** GO:0001501 (skeletal system development), GO:0002062 (chondrocyte differentiation), GO:0001958 (endochondral ossification), GO:0007188 (adenylate cyclase-modulating GPCR signaling), GO:0007194 (negative regulation of adenylate cyclase activity). **Suggested CL terms:** CL:0000138 (chondrocyte), CL:0000743 (hypertrophic chondrocyte), CL:0000062 (osteoblast).

### 7. Anatomical Structures Affected

**Organ/system level:** skeletal system (primary); dentition; kidney/mineral homeostasis (secondary, PTH-resistant subset). **Specific sites:** epiphyses of long bones, pubic symphysis and pelvis, short tubular bones of hands and feet, sacrum, ischium/pubis, growth plates. **Tissue level:** cartilage (growth-plate/epiphyseal), bone. **Cell level:** growth-plate chondrocytes (proliferative and hypertrophic), osteoblasts. **Subcellular:** plasma membrane (receptor localization; note intracellular retention of the dominant-negative PFE mutant). **Lateralization:** bilateral and generally symmetric. **Suggested UBERON terms:** UBERON:0002204 (musculoskeletal system), UBERON:0001474 (bone element), UBERON:0006255 (growth plate cartilage), UBERON:0002472 (epiphysis, related), UBERON:0009853 (pubic symphysis), UBERON:0002398 (manus), UBERON:0002387 (pes).

### 8. Temporal Development

**Onset:** patients are **normal at birth** ([PMID: 6734674](https://pubmed.ncbi.nlm.nih.gov/6734674/)); the disorder manifests during **childhood** as ossification centers fail to appear/progress on schedule. **Pattern:** chronic, insidious, developmental. **Progression:** non-progressive in the degenerative sense — the abnormality is delayed maturation during the growth period; there is no evidence of ongoing organ deterioration. **Duration:** lifelong (constitutional). **Critical period:** the growth-plate-active window of childhood/adolescence is the period of vulnerability and the theoretical window for any future intervention. No remission occurs (structural/developmental disorder).

### 9. Inheritance and Population

**Inheritance:** autosomal recessive (biallelic/homozygous *PTH1R*), [PMID: 6734674](https://pubmed.ncbi.nlm.nih.gov/6734674/), [PMID: 29987841](https://pubmed.ncbi.nlm.nih.gov/29987841/). **Penetrance:** effectively complete for homozygotes (heterozygous carriers are unaffected for Eiken, though heterozygous LOF causes the distinct dominant PFE with incomplete penetrance). **Expressivity:** variable — the TM2 subset adds PTH resistance. **Epidemiology:** Orphanet prevalence **<1/1,000,000** ("unknown"); only ~4–5 families reported worldwide. **Consanguinity:** central (original family consanguineous). **Founder effects/carrier frequency:** none established; alleles are private. **Populations:** reported in European (Danish), Indian, and East-African ancestries; both sexes affected (original family: three brothers). **No genetic anticipation** (not a repeat-expansion disorder).

### 10. Diagnostics

**Imaging (primary diagnostic modality):** skeletal survey/radiographs showing delayed epiphyseal, pelvic, and short-tubular-bone ossification; coarse trabeculae; abnormal modeling; cone-shaped/pseudo-epiphyses ([PMID: 29987841](https://pubmed.ncbi.nlm.nih.gov/29987841/), [PMID: 6734674](https://pubmed.ncbi.nlm.nih.gov/6734674/)). **Laboratory:** serum calcium and phosphate (hypocalcemia/hyperphosphatemia in the PTH-resistant subset), PTH; normal urine mucopolysaccharides and normal karyotype help exclude storage disorders/aneuploidy ([PMID: 6734674](https://pubmed.ncbi.nlm.nih.gov/6734674/)). **Genetic testing (confirmatory):** *PTH1R* single-gene sequencing, skeletal-dysplasia gene panels, or whole-exome/whole-genome sequencing to identify biallelic *PTH1R* variants; segregation analysis in consanguineous families. **Differential diagnosis:** other *PTH1R* disorders (Blomstrand — lethal/accelerated ossification; Jansen — activating; pseudohypoparathyroidism-like disorder; PFE), acrodysostosis and other brachydactyly-with-delayed-ossification dysplasias, pseudohypoparathyroidism. **Screening:** cascade carrier testing within affected families; prenatal/preimplantation testing feasible once the familial variant is known.

### 11. Outcome / Prognosis

**Prognosis is favorable.** Lifespan is normal and intelligence is normal ([PMID: 6734674](https://pubmed.ncbi.nlm.nih.gov/6734674/)). Morbidity is skeletal (short stature/moderate dwarfism, brachydactyly, orthopedic issues) and dental (failed eruption); the PTH-resistant subset requires mineral management. There is no disease-specific mortality, no malignant potential, and no progressive organ failure. Formal survival, disability, and quality-of-life metrics have not been published (case-report-only literature). **Prognostic factors:** presence of PTH resistance (TM2 variants) predicts the mineral-metabolism component.

### 12. Treatment

**No targeted or curative therapy exists.** Management is **supportive and symptomatic:**
- **Pharmacotherapy (PTH-resistant subset):** oral/active vitamin D (calcitriol/alfacalcidol) and calcium supplementation to correct hypocalcemia/hyperphosphatemia (analogous to pseudohypoparathyroidism management). *Suggested NCIT:* Calcium (NCIT:C376), Calcitriol/Vitamin D (NCIT:C1042/related).
- **Orthopedic care:** monitoring and management of skeletal deformity, short stature, and modeling abnormalities; physical/occupational therapy. *Suggested NCIT:* Orthopedic Procedure (NCIT:C51826), Physical Therapy (NCIT:C15325).
- **Dental care:** management of primary failure of tooth eruption (orthodontic/surgical, often refractory).
- **Genetic counseling:** for recurrence risk in consanguineous families.

No pharmacogenomics, gene therapy, cell therapy, RNA therapy, immunotherapy, or disease-specific clinical trials (NCT identifiers) exist for Eiken syndrome. Signaling-biased pharmacology of PTH1R is a theoretical future avenue but untested.

### 13. Prevention

Primary prevention is limited to **genetic counseling and reproductive options** in at-risk (consanguineous) families: carrier testing once the familial variant is known, prenatal diagnosis, and preimplantation genetic testing. Secondary/tertiary prevention consists of early orthopedic and dental surveillance and correction of mineral abnormalities in the PTH-resistant subset. No immunization, behavioral, public-health, or environmental interventions are applicable (monogenic disorder).

### 14. Other Species / Natural Disease

**Taxonomy of models:** *Mus musculus* (NCBI Taxon 10090). **Ortholog:** mouse *Pth1r* (NCBI Gene 19228); the gene and the PTHrP–Ihh axis are **highly evolutionarily conserved** across vertebrates. **Natural disease:** no well-documented naturally occurring Eiken-equivalent disorder in companion animals or wildlife is recorded in OMIA; the human phenotypes are recapitulated experimentally in mice (below). **Zoonotic potential:** none (non-transmissible genetic disorder).

### 15. Model Organisms

**Mouse is the primary model system.** Relevant models:
- **Humanized *PTH1R* knock-in** carrying p.E469K: *"Introduction of the p.E469K substitution into humanized PTH1R mice resulted in mildly increased mineralization of bones in the paws as well as shortening of long bones"* ([PMID: 41031626](https://pubmed.ncbi.nlm.nih.gov/41031626/)) — a knock-in model reproducing a *PTH1R* skeletal phenotype.
- **Conditional Prx1-Cre;*Pth1r* deletion:** *"PTH1R deletion caused symphalangism, demonstrating another novel function of PTH1R signaling in digit formation"* ([PMID: 26620087](https://pubmed.ncbi.nlm.nih.gov/26620087/)).
- **Global PTHrP-null / *Pth1r*-null:** accelerated chondrocyte differentiation and premature ossification; **PTHrP-overexpressing transgenics:** delayed differentiation and delayed endochondral ossification — the Eiken direction ([PMID: 10912527](https://pubmed.ncbi.nlm.nih.gov/10912527/)).
- **Atf4-null:** delayed ossification via reduced *Ihh* transcription ([PMID: 19906842](https://pubmed.ncbi.nlm.nih.gov/19906842/)), illuminating the transcriptional layer of the loop.

**Phenotype recapitulation:** the PTHrP-overexpression and humanized knock-in models capture the delayed-ossification/skeletal-modeling direction. **Limitations:** no mouse yet carries an exact homozygous Eiken allele (E35K/Y134S/R485X/I237N/D241E) with characterization of the β-arrestin/basal-cAMP signaling bias in vivo, and mouse–human differences in growth-plate dynamics constrain direct translation. **Resources:** MGI (mouse), IMPC/KOMP for *Pth1r* alleles; HEK293 cell-based signaling assays for variant functional analysis. *In-vitro* systems (HEK293 cAMP/β-arrestin assays, [PMID: 37268817](https://pubmed.ncbi.nlm.nih.gov/37268817/), [PMID: 39276366](https://pubmed.ncbi.nlm.nih.gov/39276366/)) are the standard for classifying new variants.

---

## Mechanistic Model / Interpretation

```
   Biallelic hypomorphic PTH1R variant
   (E35K / Y134S ─ extracellular; I237N / D241E ─ TM2; R485X ─ C-tail)
                    │
                    ▼
   Biased receptor signaling
   ↑ basal (ligand-independent) cAMP tone
   ↓ β-arrestin2 recruitment + defective desensitization (esp. PTHrP)
                    │
        ┌───────────┴───────────────────────────┐
        ▼                                        ▼
  GROWTH-PLATE branch                     MINERAL branch (TM2 subset)
  Sustained PTHrP-type tone               Impaired PTH-dependent
  → chondrocytes stay proliferative       renal/mineral signaling
  → delayed hypertrophic differentiation  → PTH resistance
  (within PTHrP–Ihh feedback loop)        → hypocalcemia + hyperphosphatemia
        │
        ▼
  DELAYED ENDOCHONDRAL OSSIFICATION              ┌── DENTAL branch ──┐
  + abnormal bone modeling                       │ impaired follicle │
  → epiphyses, pelvis, hands/feet,               │ PTH1R signaling   │
    coarse trabeculae, pseudo-epiphyses,         │ → primary failure │
    brachydactyly, short stature                 │   of tooth eruption│
                                                 └───────────────────┘

  SPECTRUM CONTEXT (dose/direction of PTH1R signaling):
  activating (Jansen, AD) ─ biased/hypomorphic (EIKEN, AR) ─ complete LOF (Blomstrand, AR, lethal)
       delayed diff.            DELAYED OSSIFICATION            ACCELERATED ossification
```

The unifying insight is that **Eiken syndrome is a "signaling-bias" disorder, not a simple loss- or gain-of-function disorder.** The delayed-ossification phenotype aligns with *excess* PTHrP-type tone (paralleling PTHrP-overexpressing mice) and is the opposite pole from Blomstrand's complete loss of function (accelerated ossification), even though both are recessive. The β-arrestin/desensitization defect is mechanistically central: because the receptor cannot properly terminate PTHrP-driven cAMP signaling, chondrocyte hypertrophy is inappropriately restrained, delaying the cartilage-to-bone transition.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report | Evidence type |
|---|---|---|---|
| [6734674](https://pubmed.ncbi.nlm.nih.gov/6734674/) | Original 3-brother familial dysplasia | Defines the entity, phenotype, AR inheritance, normal cognition | Human clinical (case series) |
| [29987841](https://pubmed.ncbi.nlm.nih.gov/29987841/) | Second case + molecular characterization | Establishes biallelic *PTH1R* etiology; enumerates hallmarks; documents rarity | Human clinical + molecular |
| [31297790](https://pubmed.ncbi.nlm.nih.gov/31297790/) | Third family with Eiken syndrome | Confirms recurrence of the entity in a new family | Human clinical |
| [39276366](https://pubmed.ncbi.nlm.nih.gov/39276366/) | Eiken with PTH resistance (TM2 I237N/D241E) | Adds the PTH-resistant subset; increased basal cAMP with blunted ligand response | Human clinical + in vitro |
| [37268817](https://pubmed.ncbi.nlm.nih.gov/37268817/) | Altered signaling/desensitization in Eiken mutants | Core mechanism: ↑basal cAMP, ↓β-arrestin2 for R485X/E35K/Y134S | In vitro (HEK293) |
| [40904804](https://pubmed.ncbi.nlm.nih.gov/40904804/) | Human diseases from homozygous *PTH1R* mutations | Places Eiken in the homozygous allelic spectrum vs Blomstrand | Review |
| [10912527](https://pubmed.ncbi.nlm.nih.gov/10912527/) | PTHrP and Ihh in skeletal development | Growth-plate physiology; overexpression → delayed ossification (Eiken direction) | Model organism/review |
| [26620087](https://pubmed.ncbi.nlm.nih.gov/26620087/) | Ihh/PTH1R in limb mesenchyme / digit formation | Conditional deletion → symphalangism; digit-bone role | Model organism (mouse) |
| [41031626](https://pubmed.ncbi.nlm.nih.gov/41031626/) | Helix-8 *PTH1R* brachydactyly + humanized mouse | Humanized knock-in recapitulates skeletal phenotype | Model organism (mouse) |
| [27898723](https://pubmed.ncbi.nlm.nih.gov/27898723/) | PFE *PTH1R* mutants disrupt G-protein signaling | Dominant-negative/intracellular-retention mechanism (spectrum context) | In vitro |
| [23771181](https://pubmed.ncbi.nlm.nih.gov/23771181/) | Spectrum of *PTH1R* mutations in PFE | Haploinsufficiency mechanism for dominant PFE end of spectrum | Human clinical + molecular |
| [19906842](https://pubmed.ncbi.nlm.nih.gov/19906842/) | Atf4 regulates chondrocyte differentiation via Ihh | Transcriptional control of the Ihh loop; Atf4-null → delayed ossification | Model organism (mouse) |
| [37840415](https://pubmed.ncbi.nlm.nih.gov/37840415/) | Heterozygous *PTH1R* variant, incomplete penetrance | Illustrates AD/AR complexity of *PTH1R* | Human clinical |
| [24825834](https://pubmed.ncbi.nlm.nih.gov/24825834/), [28257744](https://pubmed.ncbi.nlm.nih.gov/28257744/), [31730001](https://pubmed.ncbi.nlm.nih.gov/31730001/), [41898811](https://pubmed.ncbi.nlm.nih.gov/41898811/) | PFE clinical/genetic series & review | Characterize the dominant PFE pole of the *PTH1R* spectrum | Human clinical/review |

---

## Limitations and Knowledge Gaps

1. **Extreme rarity / evidence level.** Only ~4–5 families exist; all clinical evidence is case-report level. There are **no registries, natural-history studies, standardized QoL instruments, incidence/prevalence estimates beyond "<1/1,000,000," or omics datasets** specific to Eiken syndrome.
2. **Genotype–phenotype resolution is coarse.** Why some biallelic variants (TM2) add PTH resistance while others (extracellular/C-tail) do not is only partially explained by the in-vitro assays; the β-arrestin bias has not been shown directly in patient chondrocytes or bone.
3. **No in-vivo Eiken-allele mouse.** Existing mouse models bracket the phenotype but none carries an exact homozygous Eiken variant with in-vivo signaling characterization.
4. **Mechanistic step 3 is inferential.** The link from "increased basal cAMP + impaired β-arrestin desensitization" to "delayed hypertrophic differentiation" is inferred from PTHrP-overexpression phenotypes and the Blomstrand contrast, not directly demonstrated in Eiken growth plates.
5. **No therapeutics.** No targeted therapy, trial, or biomarker for treatment response exists.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a knock-in mouse** carrying a homozygous Eiken allele (e.g., E35K or R485X) in the humanized *PTH1R* background; phenotype growth plates, ossification timing, and mineral homeostasis, and assay chondrocyte β-arrestin/cAMP signaling in vivo.
2. **Patient-derived iPSC → chondrocyte/organoid models** to test the "signaling-bias" hypothesis directly in human cartilage and to screen biased PTH1R ligands/allosteric modulators that restore β-arrestin coupling.
3. **Systematic functional classification** of all reported and future *PTH1R* variants using standardized cAMP + β-arrestin BRET assays, building a genotype→signaling→phenotype map across the full allelic series (Jansen ↔ Eiken ↔ Blomstrand ↔ PFE).
4. **International *PTH1R*-disorder registry** capturing skeletal, dental, and mineral phenotypes with longitudinal follow-up to define natural history, penetrance, and QoL.
5. **Targeted mineral-management protocol** (calcium/active vitamin D) for the PTH-resistant subset, with prospective outcome tracking; and a genetic-counseling/carrier-testing pathway for consanguineous families.
6. **Explore β-arrestin-biased or desensitization-restoring PTH1R pharmacology** as a mechanistically rational, though currently theoretical, therapeutic direction.

---

*Report compiled from a 5-iteration autonomous investigation. 7 findings confirmed; 17 papers reviewed. All quoted abstract snippets were verified against source records. Evidence is predominantly human case-report and in-vitro functional-assay level, supplemented by model-organism genetics of the PTHrP–PTH1R–Ihh axis.*


## Artifacts

- [OpenScientist final report](Eiken_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Eiken_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 17 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 25 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001156` (1 mention) - the report calls it "Physical"; HP calls it **Brachydactyly**
- `HP:0100671` (1 mention) - the report calls it "related"; HP calls it **Abnormal trabecular bone morphology**
- `HP:0010580` (1 mention) - the report calls it "related"; HP calls it **Enlarged epiphyses**
- `HP:0010579` (1 mention) - the report calls it "Radiographic sign"; HP calls it **Cone-shaped epiphysis**
- `HP:0008821` (1 mention) - the report calls it "related"; HP calls it **Hypoplastic inferior ilia**
- `HP:0004322` (1 mention) - the report calls it "Physical"; HP calls it **Short stature**
- `HP:0002901` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Hypocalcemia**
- `HP:0002905` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Hyperphosphatemia**
- `UBERON:0002472` (1 mention) - the report calls it "epiphysis, related"; UBERON calls it **stylopod**
- `UBERON:0009853` (1 mention) - the report calls it "pubic symphysis"; UBERON calls it **body of uterus**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0002662` (1 mention), reported as "Delayed epiphyseal ossification" - HP does not contain this term
- `HP:0006348` (1 mention), reported as "related" - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0008788` (1 mention) - the report calls it "Delayed pelvic bone ossification"; HP calls it **Delayed pubic bone ossification**
- `HP:0011314` (1 mention) - the report calls it "Abnormal diaphysis morphology"; HP calls it **Abnormal long bone morphology**
- `GO:0007188` (1 mention) - the report calls it "adenylate cyclase-modulating GPCR signaling"; GO calls it **adenylate cyclase-modulating G protein-coupled receptor signaling pathway**, and lists "adenylate cyclase-modulating GPCR signaling pathway" among its other names
- `UBERON:0006255` (1 mention) - the report calls it "growth plate cartilage"; UBERON calls it **ischial pre-cartilage condensation**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.