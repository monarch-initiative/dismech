---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-02T05:29:16.094700'
end_time: '2026-09-02T05:44:03.549292'
duration_seconds: 887.45
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hennekam lymphangiectasia-lymphedema syndrome 2
  mondo_id: ''
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
citation_count: 19
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 18
  quotes_valid: 18
  relevance_assessed: 19
  on_topic: 13
  validator_version: 0.2.1
term_validation:
  total_terms: 25
  verified: 23
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 5
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: HP:0002593
    reported_labels:
    - Lab/imaging/pathology
    ontology_label: Intestinal lymphangiectasia
  - term_id: HP:0002243
    reported_labels:
    - Lab abnormality
    ontology_label: Protein-losing enteropathy
  - term_id: HP:0001256
    reported_labels:
    - Behavioral/cognitive
    ontology_label: Mild intellectual disability
  - term_id: HP:0003073
    reported_labels:
    - Lab abnormality
    ontology_label: Hypoalbuminemia
  - term_id: HP:0004313
    reported_labels:
    - Lab abnormality
    ontology_label: Decreased circulating immunoglobulin concentration
  - term_id: HP:0000365
    reported_labels:
    - Sensory
    ontology_label: Hearing impairment
  - term_id: HP:0012385
    reported_labels:
    - Physical
    ontology_label: Camptodactyly
  - term_id: HP:0001252
    reported_labels:
    - Neurological
    ontology_label: Hypotonia
  labels_variant: 1
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
  path: Hennekam_Lymphangiectasia-Lymphedema_Syndrome_2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hennekam_Lymphangiectasia-Lymphedema_Syndrome_2-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hennekam lymphangiectasia-lymphedema syndrome 2
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hennekam lymphangiectasia-lymphedema syndrome 2** covering all of the
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

# Hennekam Lymphangiectasia–Lymphedema Syndrome 2 (HKLLS2): Comprehensive Disease Characteristics Report

**Disease:** Hennekam lymphangiectasia-lymphedema syndrome 2 (HKLLS2)
**OMIM:** #616006 · **MONDO:** MONDO:0014217 · **Orphanet:** ORPHA:2136 (Hennekam syndrome) · **ICD-10:** Q82.0 (hereditary lymphedema)
**Causal gene:** *FAT4* (FAT atypical cadherin 4; HGNC:23109; 4q28.1) · **Inheritance:** Autosomal recessive
**Category:** Mendelian

---

## Summary

Hennekam lymphangiectasia-lymphedema syndrome 2 (HKLLS2) is an ultra-rare, autosomal recessive generalized lymphatic dysplasia caused by **biallelic loss-of-function variants in *FAT4***, an atypical Fat/Dachsous-family cadherin located at 4q28.1. It is the second genetically defined form of Hennekam syndrome — HKLLS1 is caused by *CCBE1* and HKLLS3 by *ADAMTS3* — and is **allelic to Van Maldergem syndrome (VMS)**, which arises from *FAT4* or *DCHS1* mutations and shares a facial gestalt and intellectual disability but generally lacks the lymphedema that defines Hennekam syndrome. The disease was molecularly delineated by Alders and colleagues in 2014 through homozygosity mapping and whole-exome sequencing of the original Hennekam family, in whom no *CCBE1* mutation had been found ([PMID: 24913602](https://pubmed.ncbi.nlm.nih.gov/24913602/)).

Mechanistically, FAT4 acts **cell-autonomously in lymphatic endothelial cells (LECs)** to establish planar cell polarity (PCP) in response to fluid flow, working with its binding partner Dachsous1 (DCHS1) to drive lymphatic valve and vessel morphogenesis. Loss of FAT4 disrupts LEC polarization, causing defective lymphatic valves and dysfunctional lymphatic drainage; this converges on the same **VEGF-C/VEGFR3 prolymphangiogenic axis** in which CCBE1 and ADAMTS3 operate (by proteolytically activating pro-VEGF-C). FAT4/DCHS1 signaling additionally regulates Hippo/YAP-dependent cortical neurogenesis, which explains the neurodevelopmental features. The downstream clinical consequences form a characteristic tetrad: **congenital/generalized lymphedema, intestinal lymphangiectasia with protein-losing enteropathy (PLE), facial dysmorphism, and variable (mild-to-moderate) intellectual disability**, with additional multisystem involvement (chylous effusions, pericardial effusion, hearing loss, hypogammaglobulinemia).

There is **no curative therapy**. Management is supportive and multidisciplinary: complete decongestive therapy for lymphedema, high-protein/low-fat/medium-chain-triglyceride nutrition and albumin/immunoglobulin support for intestinal lymphangiectasia and PLE, drainage/management of effusions, and symptomatic care of dysmorphic, cognitive, and sensory features. Diagnosis is established by **molecular genetic testing** (exome/genome sequencing or a primary-lymphedema gene panel including *CCBE1*, *FAT4*, *ADAMTS3*) within the standardized primary lymphatic dysplasia diagnostic pathway, supported by imaging (lymphoscintigraphy, MR lymphangiography), intestinal biopsy showing lymphangiectasia, and laboratory evidence of hypoalbuminemia and hypogammaglobulinemia. Prevention relies on genetic counseling with the option of prenatal or preimplantation genetic testing in at-risk families.

**Evidence base:** this is an ultra-rare disorder (~50 Hennekam-syndrome cases reported worldwide; the *FAT4* subtype a minority). Nearly all information derives from **individual patient case reports/small cohorts (human clinical)**, **model-organism** studies (mouse, *Drosophila*), and **in vitro** biochemistry — not from large aggregated registries or EHR datasets. Where data are absent, this is stated explicitly.

---

## Key Findings

### Finding 1 — HKLLS2 is caused by biallelic loss-of-function *FAT4* variants (autosomal recessive; OMIM #616006)

The genetic basis of HKLLS2 was established by Alders et al. (2014). Using homozygosity mapping combined with whole-exome sequencing in the original Hennekam family — in whom *CCBE1* mutations had been excluded — they identified a homozygous *FAT4* mutation, then confirmed the gene by targeted analysis of a *CCBE1*-negative cohort:

> "We used homozygosity mapping and whole-exome sequencing in the original HS family with multiple affected individuals in whom no CCBE1 mutation had been detected, and identified a homozygous mutation in the FAT4 gene. Subsequent targeted mutation analysis of FAT4 in a cohort of 24 CCBE1 mutation-negative Hennekam syndrome patients identified homozygous or compound heterozygous mutations in four additional families." — [PMID: 24913602](https://pubmed.ncbi.nlm.nih.gov/24913602/)

The autosomal recessive inheritance and the OMIM identifier #616006 for the *FAT4*-associated form are corroborated in the ADAMTS3 delineation paper:

> "It is an autosomal recessive condition caused by biallelic mutations in CCBE1 ... (HKLLS1; OMIM 235510) or FAT4 (HKLLS2; OMIM 616006)." — [PMID: 30450763](https://pubmed.ncbi.nlm.nih.gov/30450763/)

Reported *FAT4* variants are biallelic — homozygous in consanguineous families or compound heterozygous — and predominantly loss-of-function: missense, nonsense, frameshift, and splice-site changes. A 2026 report described a novel biallelic intron-14 splice variant (c.12479+3A>G) causing HKLLS2, with aberrant splicing confirmed by RT-PCR of patient fibroblasts ([PMID: 41992670](https://pubmed.ncbi.nlm.nih.gov/41992670/)). *FAT4* is allelic to Van Maldergem syndrome, so the same gene produces distinct but overlapping phenotypes depending on variant and modifier context.

### Finding 2 — FAT4 controls LEC polarity and lymphatic valve morphogenesis, converging on the VEGF-C/VEGFR3 pathway shared by all Hennekam genes

FAT4 is the molecular linchpin of HKLLS2 pathophysiology. Betterman et al. (2020) demonstrated that FAT4 functions within LECs to sense flow and establish polarity, and that it is a transcriptional target of the lymphatic master regulator GATA2:

> "we demonstrate that FAT4 functions in a lymphatic endothelial cell-autonomous manner to control cell polarity in response to flow and is required for lymphatic vessel morphogenesis throughout development" — [PMID: 32182215](https://pubmed.ncbi.nlm.nih.gov/32182215/)

Pujol et al. (2017) showed that the Dachsous1–Fat4 PCP module directs endothelial cell polarization specifically during **lymphatic valve morphogenesis**, and directly linked valve defects to the lymphedema seen in FAT4-Hennekam syndrome:

> "Our data demonstrate that Fat4 and Dachsous1 are critical regulators of valve morphogenesis. This study highlights that valve defects may contribute to lymphedema in Hennekam syndrome caused by Fat4 mutations." — [PMID: 28705793](https://pubmed.ncbi.nlm.nih.gov/28705793/)

Crucially, all three principal Hennekam genes act in a shared prolymphangiogenic pathway. CCBE1 (a matrix protein) and ADAMTS3 (a protease) proteolytically cleave and activate pro-VEGF-C, enabling VEGFR3 signaling, while FAT4 governs the endothelial polarity required to build functional vessels and valves:

> "encoding a matrix protein and protease, respectively, that regulate activity of the key prolymphangiogenic VEGF-C/VEGFR3 signaling axis by facilitating the proteolytic cleavage and activation of VEGF-C. The fact that FAT4, CCBE1, and ADAMTS3 mutations underlie Hennekam syndrome suggested that all 3 genes might function in a common pathway" — [PMID: 32182215](https://pubmed.ncbi.nlm.nih.gov/32182215/)

The VEGF-C activation mechanism is further supported by biochemical work showing that an ADAMTS3–CCBE1 complex is required to convert VEGF-C (but not VEGF-D) into an active VEGFR3 ligand ([PMID: 27159393](https://pubmed.ncbi.nlm.nih.gov/27159393/)) and that the two domains of CCBE1 promote VEGFR3 signaling by distinct mechanisms ([PMID: 28687807](https://pubmed.ncbi.nlm.nih.gov/28687807/)). PROX1 (master LEC identity factor) and VEGFR-3 form the developmental backbone of this system ([PMID: 29842991](https://pubmed.ncbi.nlm.nih.gov/29842991/)).

### Finding 3 — Core clinical phenotype: congenital lymphedema, intestinal lymphangiectasia/PLE, facial dysmorphism, and variable intellectual disability

Ivanovski, Alders, and Hennekam (2018) reviewed all reported *FAT4* patients (VMS n=11, HS n=40), delineating the shared and distinguishing features of the two allelic conditions:

> "Both conditions are characterized by a typical facial gestalt and mild to moderate intellectual disability, but differ in the occurrence of neonatal hypotonia and feeding problems, hearing loss, tracheal anomalies, and osteopenia in VMS, and lymphedema in HS." — [PMID: 29681106](https://pubmed.ncbi.nlm.nih.gov/29681106/)

Individual case reports document the full clinical spectrum: generalized/peripheral lymphedema, facial anomalies (hypertelorism, flat nasal bridge, flat facial profile), camptodactyly, hypotonia, and duodenal lymphangiectasia with hypoalbuminemia and hypogammaglobulinemia ([PMID: 25616299](https://pubmed.ncbi.nlm.nih.gov/25616299/), [PMID: 41992670](https://pubmed.ncbi.nlm.nih.gov/41992670/)). The intestinal lymphangiectasia (a form of Waldmann disease) drives protein-losing enteropathy as a downstream consequence:

> "Primary intestinal lymphangiectasia (WD) is a consequence of HS, which ultimately results in PLE and worsening interstitial lymph buildup." — [PMID: 38028107](https://pubmed.ncbi.nlm.nih.gov/38028107/)

### Finding 4 — Model organisms recapitulate PCP, kidney, neural, and lymphatic phenotypes

*Fat4*-null mice and *Drosophila fat* mutants provide strong cross-species mechanistic support. In mouse (NCBI Taxon 10090; gene *Fat4*), Saburi et al. (2008) established the PCP role:

> "Loss of Fat4 disrupts oriented cell divisions and tubule elongation during kidney development, leading to cystic kidney disease. Fat4 genetically interacts with the PCP genes Vangl2 and Fjx1 in cyst formation." — [PMID: 18604206](https://pubmed.ncbi.nlm.nih.gov/18604206/)

Cappello et al. (2013) recapitulated the neurodevelopmental component and linked FAT4/DCHS1 to Hippo/YAP signaling:

> "Reducing the expression of Dchs1 or Fat4 within mouse embryonic neuroepithelium increased progenitor cell numbers and reduced their differentiation into neurons, resulting in the heterotopic accumulation of cells below the neuronal layers in the neocortex, reminiscent of the human phenotype. These effects were countered by concurrent knockdown of Yap" — [PMID: 24056717](https://pubmed.ncbi.nlm.nih.gov/24056717/)

The lymphatic-specific phenotype is captured by *Fat4*-deficient mice with defective valve morphogenesis and endothelial polarity ([PMID: 28705793](https://pubmed.ncbi.nlm.nih.gov/28705793/), [PMID: 32182215](https://pubmed.ncbi.nlm.nih.gov/32182215/)). In *Drosophila* (Taxon 7227; ortholog *fat*), neuron-specific *fat* knockdown provides a model relevant to the intellectual-disability/neuronal features:

> "Neuron-specific knockdown of fat shortened the life span and induced the defect in locomotive abilities of adult flies... Both VMS and HS show mental retardation and neuronal defects. We therefore consider that these two rare human diseases could possibly be caused by the defect in FAT4 function in neuronal cells." — [PMID: 28488382](https://pubmed.ncbi.nlm.nih.gov/28488382/)

### Finding 5 — Management is supportive; no curative therapy exists

There is no disease-modifying or curative treatment for HKLLS2. Lee et al. (2018) summarize the rehabilitative approach:

> "There is no curative therapy at this time, but rehabilitative treatments including complete decongestive therapy for edema control appeared to be beneficial." — [PMID: 29560340](https://pubmed.ncbi.nlm.nih.gov/29560340/)

Management is therefore symptomatic and multidisciplinary: complete decongestive therapy (manual lymphatic drainage, compression, exercise, skin care) for lymphedema; nutritional management of intestinal lymphangiectasia/PLE with a high-protein, low-fat, medium-chain-triglyceride diet plus correction of hypoalbuminemia and hypogammaglobulinemia; drainage/management of chylous and pericardial effusions ([PMID: 26686525](https://pubmed.ncbi.nlm.nih.gov/26686525/)); and symptomatic care for facial dysmorphism, intellectual disability, hearing loss, and cardiac anomalies.

### Finding 6 — Gene/protein identifiers, variant spectrum, and epidemiology

*FAT4* (FAT atypical cadherin 4) identifiers: **HGNC:23109, NCBI Gene 79633, Ensembl ENSG00000196159, UniProt Q6V0I7, cytoband 4q28.1**. The gene encodes a very large (~4,981-aa) single-pass atypical cadherin — the vertebrate ortholog of *Drosophila* Fat — with 34 extracellular cadherin repeats, EGF-like domains, and laminin-G domains:

> "The FAT4 gene encodes a large protein with extracellular cadherin repeats, EGF-like domains and Laminin G-like domains." — [PMID: 28488382](https://pubmed.ncbi.nlm.nih.gov/28488382/)

Disease identifiers: OMIM #616006; MONDO:0014217; Orphanet ORPHA:2136 (Hennekam syndrome); ICD-10 Q82.0. Within Hennekam syndrome overall, *CCBE1* accounts for approximately 25% of cases, with *FAT4* and *ADAMTS3* explaining additional subsets:

> "It can be caused by mutations in CCBE1 which are found in approximately 25 % of cases." — [PMID: 24913602](https://pubmed.ncbi.nlm.nih.gov/24913602/)

Hennekam syndrome is ultra-rare (Orphanet prevalence <1/1,000,000). As of 2023, roughly 50 cases had been reported worldwide:

> "As far as we know, this is the 51st case of HS worldwide and the first one in an African American." — [PMID: 38028107](https://pubmed.ncbi.nlm.nih.gov/38028107/)

### Finding 7 — Diagnosis relies on molecular genetic testing within the primary lymphatic dysplasia workup

Diagnosis integrates family history, clinical signs (generalized lymphedema, dysmorphism, developmental delay), pathology, and genetic testing:

> "Diagnosis of the disease depends on the familial history, clinical signs, pathological findings and genetic tests." — [PMID: 25616299](https://pubmed.ncbi.nlm.nih.gov/25616299/)

Molecular confirmation is achieved by exome/genome sequencing or a primary-lymphedema gene panel including *CCBE1*, *FAT4*, and *ADAMTS3*, detecting biallelic variants; splice variants can be functionally confirmed by RT-PCR of patient fibroblasts ([PMID: 41992670](https://pubmed.ncbi.nlm.nih.gov/41992670/)). Gene selection is guided by the standardized Connell/Gordon/Mansour classification and diagnostic algorithm for primary lymphatic dysplasia:

> "In 2010, we introduced a new classification and diagnostic pathway as a clinical and research tool. This algorithm has been used to delineate specific primary lymphoedema phenotypes, facilitating the discovery of new causative genes." — [PMID: 23621851](https://pubmed.ncbi.nlm.nih.gov/23621851/)

Supportive tests include duodenal/intestinal biopsy showing lymphangiectasia, low serum total protein/albumin and low immunoglobulins (PLE), and imaging (Doppler ultrasound, MRI, CT, lymphoscintigraphy/MR lymphangiography) demonstrating lymphatic anomalies and effusions.

### Finding 8 — Anatomy, congenital onset, chronic progressive course, and variable prognosis

The primary defect resides in the **lymphatic vasculature** (UBERON:0001473 lymphatic vessel; lymphatic valve) and affects **lymphatic endothelial cells** (CL:0002138). Multisystem involvement is documented: limbs (peripheral/generalized lymphedema), intestine/duodenum (intestinal lymphangiectasia, UBERON:0000160), face/craniofacial skeleton (dysmorphism), brain/cerebral cortex (intellectual disability, periventricular heterotopia via FAT4/DCHS1; [PMID: 24056717](https://pubmed.ncbi.nlm.nih.gov/24056717/)), heart/pericardium (pericardial effusion, cardiac defects; [PMID: 38028107](https://pubmed.ncbi.nlm.nih.gov/38028107/)), ear (hearing loss), and serous cavities (chylous ascites, pleural/pericardial effusions):

> "whose clinical phenotype also includes protein losing enteropathy, painful relapsing chylous ascites, and hypogammaglobulinemia" — [PMID: 26686525](https://pubmed.ncbi.nlm.nih.gov/26686525/)

Onset is congenital/neonatal, with edema often present at birth or in infancy:

> "presented to our center with generalized edema, ascites, and hypoalbuminemia" — [PMID: 25925991](https://pubmed.ncbi.nlm.nih.gov/25925991/)

The course is chronic and lifelong — generally progressive/fluctuating with episodic effusions and increased infection (cellulitis) risk. Prognosis is variable and is largely determined by the severity of intestinal lymphangiectasia/PLE and of serous effusions ([PMID: 38028107](https://pubmed.ncbi.nlm.nih.gov/38028107/), [PMID: 29560340](https://pubmed.ncbi.nlm.nih.gov/29560340/)).

---

## Section-by-Section Report

### 1. Disease Information

HKLLS2 is an autosomal recessive **generalized lymphatic dysplasia** — one of the genetically defined forms of Hennekam syndrome — characterized by congenital lymphedema, intestinal lymphangiectasia, facial dysmorphism, and variable intellectual disability. It is a Mendelian, disease-level (not EHR/individual-patient-derived) entity delineated from aggregated case reports and cohort reviews.

**Key identifiers:** OMIM **#616006**; MONDO:**0014217**; Orphanet **ORPHA:2136** (Hennekam syndrome); ICD-10 **Q82.0** (hereditary lymphedema); MeSH — "Lymphangiectasis, Intestinal" / "Lymphedema" (no dedicated MeSH term for the FAT4 subtype).

**Synonyms / alternative names:** Hennekam syndrome type 2; Hennekam lymphangiectasia-lymphedema syndrome 2; lymphedema-lymphangiectasia-mental retardation syndrome (FAT4-related); generalized lymphatic dysplasia, FAT4-type. Allelic disorder: Van Maldergem syndrome 2 (VMS2, *FAT4*).

### 2. Etiology

**Causal factor:** purely genetic — biallelic loss-of-function variants in *FAT4* ([PMID: 24913602](https://pubmed.ncbi.nlm.nih.gov/24913602/)). No environmental or infectious cause.

**Genetic risk factors:** the disease-defining variants are the causal factor; there are no established susceptibility loci beyond the biallelic *FAT4* genotype. **Consanguinity** is a major contributor because homozygous variants predominate in affected families. A candidate fourth gene, *FBXL7*, has been proposed on the basis of a homozygous single-exon deletion in a Hennekam-like patient lacking *CCBE1/FAT4/ADAMTS3* variants; FBXL7 interacts with Fat in *Drosophila*, suggesting a shared pathway ([PMID: 31633297](https://pubmed.ncbi.nlm.nih.gov/31633297/)) — a potential modifier/allelic locus rather than a confirmed HKLLS2 gene.

**Environmental / protective factors:** none established. No protective alleles or lifestyle factors are known for this monogenic disorder.

**Gene–environment interactions:** not characterized. Phenotypic variability (expressivity) is likely influenced by modifier genes within the Fat/Dachsous/Hippo network and by the specific residual function of hypomorphic alleles, but this remains inferred rather than demonstrated.

### 3. Phenotypes

| Phenotype | Type | HPO suggestion | Onset | Frequency (qualitative) |
|---|---|---|---|---|
| Generalized/peripheral lymphedema | Physical sign | HP:0001004 (Lymphedema) | Congenital/neonatal | Defining feature; distinguishes HS from VMS |
| Intestinal lymphangiectasia | Lab/imaging/pathology | HP:0002593 | Infancy–childhood | Common |
| Protein-losing enteropathy | Lab abnormality | HP:0002243 | Childhood | Common |
| Facial dysmorphism (flat face, hypertelorism, flat nasal bridge) | Physical | HP:0001999 / HP:0000316 | Congenital | Typical facial gestalt |
| Intellectual disability (mild–moderate) | Behavioral/cognitive | HP:0001256 | Childhood | Frequent, variable |
| Hypoalbuminemia | Lab abnormality | HP:0003073 | Infancy | Common (secondary to PLE) |
| Hypogammaglobulinemia | Lab abnormality | HP:0004313 | Infancy | Reported |
| Chylous ascites / pleural / pericardial effusion | Sign/imaging | HP:0012019 / HP:0001541 | Variable | Reported |
| Hearing loss | Sensory | HP:0000365 | Variable | Reported (more typical of VMS) |
| Camptodactyly | Physical | HP:0012385 | Congenital | Reported |
| Hypotonia | Neurological | HP:0001252 | Neonatal | Reported |

Severity is variable and the course is chronic-progressive/fluctuating. Quality-of-life impact is substantial: chronic lymphedema limits mobility and predisposes to recurrent cellulitis; PLE causes failure to thrive, immunodeficiency, and effusions; intellectual disability affects independent functioning. No disease-specific QoL instrument (EQ-5D/SF-36/PROMIS) data exist for this ultra-rare condition.

### 4. Genetic / Molecular Information

**Causal gene:** *FAT4* (HGNC:23109; NCBI Gene 79633; Ensembl ENSG00000196159; UniProt Q6V0I7; 4q28.1). **Protein:** ~4,981-aa single-pass atypical cadherin with 34 extracellular cadherin repeats, EGF-like domains, and laminin-G domains — vertebrate ortholog of *Drosophila* Fat ([PMID: 28488382](https://pubmed.ncbi.nlm.nih.gov/28488382/)).

**Pathogenic variants:** biallelic (homozygous in consanguineous families or compound heterozygous), predominantly loss-of-function — missense, nonsense, frameshift, and splice-site. Example: novel intron-14 biallelic splice variant **c.12479+3A>G** with RT-PCR-confirmed aberrant splicing ([PMID: 41992670](https://pubmed.ncbi.nlm.nih.gov/41992670/)). Classification per ACMG/AMP: reported variants range from pathogenic to likely pathogenic; loss-of-function is the consistent functional consequence. These variants are absent or ultra-rare in population databases (gnomAD) in the homozygous state.

**Functional consequence:** loss of function / reduced FAT4 signaling.

**Modifier genes:** *DCHS1* (FAT4's cognate ligand) and downstream Hippo/YAP effectors; *FBXL7* proposed as a pathway member/candidate gene ([PMID: 31633297](https://pubmed.ncbi.nlm.nih.gov/31633297/)). **Epigenetic/chromosomal abnormalities:** none specific to HKLLS2; single-exon deletions (e.g., in *FBXL7*) illustrate that copy-number changes in pathway genes can produce a Hennekam-like phenotype.

### 5. Environmental Information

Not applicable — HKLLS2 is a monogenic disorder with no established environmental, lifestyle, or infectious contributors. Environmental factors may modulate secondary complications (e.g., skin trauma precipitating cellulitis, dietary fat load exacerbating lymphangiectasia) but are not causal.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic loss-of-function *FAT4* variants** → loss/reduction of functional FAT4 atypical cadherin protein. *(Demonstrated — [PMID: 24913602](https://pubmed.ncbi.nlm.nih.gov/24913602/))*
2. Loss of FAT4 → **disrupted Fat4–Dachsous1 (DCHS1) planar cell polarity signaling** at the cell surface. *(Demonstrated in mouse/fly — [PMID: 28705793](https://pubmed.ncbi.nlm.nih.gov/28705793/), [PMID: 18604206](https://pubmed.ncbi.nlm.nih.gov/18604206/))*
3. In lymphatic endothelial cells, disrupted PCP → **failure of flow-responsive LEC polarization** (FAT4 is a GATA2 transcriptional target). *(Demonstrated — [PMID: 32182215](https://pubmed.ncbi.nlm.nih.gov/32182215/))*
4. Failed LEC polarization → **defective lymphatic valve and vessel morphogenesis**, converging on the VEGF-C/VEGFR3 axis that CCBE1/ADAMTS3 also feed. *(Demonstrated — [PMID: 28705793](https://pubmed.ncbi.nlm.nih.gov/28705793/), [PMID: 32182215](https://pubmed.ncbi.nlm.nih.gov/32182215/))*
5. Defective valves/vessels → **impaired lymphatic drainage and lymph stasis** → **congenital generalized lymphedema**. *(Inferred from valve defects → clinical lymphedema)*
6. **Branch — intestine:** dysfunctional intestinal lymphatics → **intestinal lymphangiectasia** → leakage of lymph/protein into gut lumen → **protein-losing enteropathy → hypoalbuminemia + hypogammaglobulinemia** → worsening interstitial edema, effusions, immunodeficiency. *(Demonstrated as downstream consequence — [PMID: 38028107](https://pubmed.ncbi.nlm.nih.gov/38028107/))*
7. **Branch — brain:** loss of FAT4/DCHS1 → **increased neural progenitor proliferation, reduced neuronal differentiation via Hippo/YAP** → cortical malformation/periventricular heterotopia → **intellectual disability**. *(Demonstrated in mouse — [PMID: 24056717](https://pubmed.ncbi.nlm.nih.gov/24056717/))*
8. **Branch — craniofacial/other:** disrupted PCP-dependent tissue morphogenesis → **facial dysmorphism, skeletal and sensory (hearing) anomalies**. *(Inferred)*

```
   FAT4 biallelic LOF variants
             │
   ↓ loss of FAT4 atypical cadherin
             │
   ↓ disrupted FAT4–DCHS1 PCP + Hippo/YAP signaling
        ┌────────────┬───────────────┬─────────────┐
        ↓            ↓               ↓             ↓
   LEC polarity   neural progenitor  craniofacial   (kidney/PCP
   failure        overproliferation  morphogenesis   in models)
        ↓            ↓               ↓
   valve/vessel   ↓ neuronal diff.   facial
   defect         (YAP-dependent)    dysmorphism
        ↓            ↓
   lymph stasis   cortical heterotopia
   ┌──────┴──────┐   ↓
   ↓             ↓  intellectual disability
generalized   intestinal
lymphedema    lymphangiectasia
                  ↓
              protein-losing enteropathy
                  ↓
          hypoalbuminemia, hypogammaglobulinemia,
          chylous effusions, immunodeficiency
```

**Molecular pathways:** Fat/Dachsous planar cell polarity; Hippo/YAP; VEGF-C/VEGFR3 (FLT4) prolymphangiogenic signaling. **Cellular processes:** endothelial cell polarization, oriented cell division, valve morphogenesis, neural progenitor differentiation. **Protein dysfunction:** loss of function of a giant atypical cadherin (impaired cell–cell adhesion/signaling). **Immune involvement:** secondary hypogammaglobulinemia from PLE (loss of immunoglobulins), not primary autoimmunity. **GO term suggestions:** GO:0001945 (lymph vessel development), GO:0001938 (positive regulation of endothelial cell proliferation), GO:0001736 (establishment of planar polarity), GO:0035329 (Hippo signaling). **Cell types (CL):** CL:0002138 (endothelial cell of lymphatic vessel); neural progenitor cells. **CHEBI:** medium-chain triglycerides (therapeutic entity class).

### 7. Anatomical Structures Affected

- **Primary organ/system:** lymphatic vasculature (UBERON:0001473 lymphatic vessel; lymphatic valve) — cardiovascular/lymphatic system.
- **Secondary organs:** intestine/duodenum (UBERON:0000160; intestinal lymphangiectasia, PLE); brain/cerebral cortex (UBERON:0000956; intellectual disability, heterotopia); face/craniofacial skeleton (dysmorphism); heart/pericardium (effusions, cardiac defects); ear (hearing loss); serous cavities (peritoneal, pleural, pericardial — chylous effusions).
- **Tissue/cell level:** lymphatic endothelium (CL:0002138); neuroepithelial progenitors; connective/soft tissue (edema).
- **Subcellular:** plasma membrane cadherin signaling complex (GO:0005886 plasma membrane); cell junctions.
- **Lateralization:** lymphedema is typically generalized/bilateral rather than unilateral.

### 8. Temporal Development

- **Onset:** congenital/neonatal; edema frequently present at birth or in early infancy ([PMID: 25925991](https://pubmed.ncbi.nlm.nih.gov/25925991/), [PMID: 41992670](https://pubmed.ncbi.nlm.nih.gov/41992670/)).
- **Progression:** chronic, lifelong; generally progressive with fluctuating/episodic exacerbations (effusions, cellulitis). Intestinal lymphangiectasia/PLE may worsen over time.
- **Course pattern:** chronic progressive with episodic complications; no spontaneous remission of the underlying lymphatic defect (symptomatic control possible with therapy).
- **Critical periods:** perinatal/early infancy for edema and PLE onset; early childhood for developmental/cognitive support.

### 9. Inheritance and Population

- **Epidemiology:** ultra-rare. Hennekam syndrome overall has ~50 reported cases worldwide (as of 2023; [PMID: 38028107](https://pubmed.ncbi.nlm.nih.gov/38028107/)); Orphanet prevalence <1/1,000,000. *CCBE1* accounts for ~25% of Hennekam cases; *FAT4* explains a further genetically heterogeneous subset ([PMID: 24913602](https://pubmed.ncbi.nlm.nih.gov/24913602/)).
- **Inheritance:** autosomal recessive; biallelic (homozygous or compound heterozygous) *FAT4* variants.
- **Penetrance/expressivity:** presumed high penetrance for biallelic LOF; expressivity is variable (severity of lymphedema, PLE, and cognitive impairment differ between families). Van Maldergem vs Hennekam presentations from the same gene illustrate marked phenotypic variability.
- **Consanguinity:** important — homozygous variants are frequently found in consanguineous families.
- **Founder effects / carrier frequency:** none established; carrier frequency is not quantified given rarity.
- **Sex ratio:** no sex predilection (autosomal recessive; M≈F).

### 10. Diagnostics

- **Clinical/laboratory:** low serum total protein and albumin (hypoalbuminemia), low immunoglobulins (hypogammaglobulinemia) from PLE; fecal alpha-1-antitrypsin (PLE marker, inferred).
- **Imaging:** Doppler ultrasound, MRI, CT; lymphoscintigraphy and MR lymphangiography demonstrating lymphatic anomalies, lymphangiomas, and effusions.
- **Pathology/biopsy:** duodenal/intestinal biopsy showing dilated lacteals/lymphangiectasia ([PMID: 25616299](https://pubmed.ncbi.nlm.nih.gov/25616299/)).
- **Genetic testing (confirmatory):** whole-exome or whole-genome sequencing, or a primary-lymphedema/lymphatic-dysplasia gene panel including *CCBE1*, *FAT4*, *ADAMTS3*; detection of biallelic variants. Splice variants confirmed functionally by RT-PCR of patient fibroblasts ([PMID: 41992670](https://pubmed.ncbi.nlm.nih.gov/41992670/)). Chromosomal microarray can detect exon/CNV deletions in pathway genes ([PMID: 31633297](https://pubmed.ncbi.nlm.nih.gov/31633297/)).
- **Diagnostic framework:** the Connell/Gordon/Mansour classification and diagnostic algorithm for primary lymphatic dysplasia guides workup and gene selection ([PMID: 23621851](https://pubmed.ncbi.nlm.nih.gov/23621851/)).
- **Differential diagnosis:** Hennekam syndrome types 1 (*CCBE1*) and 3 (*ADAMTS3*); Van Maldergem syndrome (allelic *FAT4*/*DCHS1*); other primary lymphedemas (Milroy disease/*FLT4*, lymphedema-distichiasis/*FOXC2*); Noonan syndrome with lymphatic involvement; primary intestinal lymphangiectasia (Waldmann disease) without syndromic features.

### 11. Outcome / Prognosis

Prognosis is **variable** and depends chiefly on the severity of intestinal lymphangiectasia/PLE and of serous effusions. Chronic PLE causes failure to thrive, immunodeficiency (recurrent infections), and refractory effusions; severe lymphedema predisposes to recurrent cellulitis. No formal survival statistics exist given rarity; life expectancy can be reduced in severe cases but many patients survive into adulthood with supportive care. Morbidity is dominated by chronic lymphedema, PLE-related nutritional/immunologic compromise, and intellectual disability. Prognostic factors: severity/extent of lymphatic dysplasia, degree of hypoalbuminemia/hypogammaglobulinemia, and presence of cardiac/pericardial involvement ([PMID: 38028107](https://pubmed.ncbi.nlm.nih.gov/38028107/), [PMID: 29560340](https://pubmed.ncbi.nlm.nih.gov/29560340/)).

### 12. Treatment

No curative therapy exists ([PMID: 29560340](https://pubmed.ncbi.nlm.nih.gov/29560340/)). Management is supportive:

- **Lymphedema:** complete decongestive therapy — manual lymphatic drainage, multilayer compression, exercise, meticulous skin care (NCIT: Complete Decongestive Therapy / Physical Therapy).
- **Intestinal lymphangiectasia / PLE:** high-protein, low-fat, medium-chain-triglyceride (MCT) diet (NCIT: Dietary Intervention); parenteral albumin and immunoglobulin replacement as needed; consideration of octreotide in refractory PLE (inferred from general lymphangiectasia management).
- **Effusions:** drainage of chylous ascites/pleural/pericardial effusions; dietary fat restriction ([PMID: 26686525](https://pubmed.ncbi.nlm.nih.gov/26686525/)).
- **Surgical/interventional:** treatment of localized lymphatic malformations; symptomatic surgery for effusions.
- **Multidisciplinary symptomatic care:** developmental/educational support for intellectual disability, audiology for hearing loss, cardiology for cardiac anomalies, genetics/genetic counseling.
- **Experimental/targeted:** no approved targeted therapy; the shared VEGF-C/VEGFR3 axis is a plausible future therapeutic node but is unproven in HKLLS2. No pharmacogenomic considerations established.

### 13. Prevention

- **Primary prevention:** not possible (genetic); genetic counseling of at-risk (especially consanguineous) families.
- **Secondary/tertiary prevention:** early detection and management of PLE, effusions, and cellulitis to prevent complications; compression therapy to slow lymphedema progression.
- **Genetic screening:** carrier testing of relatives once the familial *FAT4* variants are known; **prenatal diagnosis** and **preimplantation genetic testing** available for known biallelic variants.
- **Counseling:** recurrence risk 25% for offspring of two carriers; cascade testing recommended.

### 14. Other Species / Natural Disease

- **Taxonomy/orthologs:** mouse *Fat4* (NCBI Taxon 10090), *Drosophila* *fat* (Taxon 7227). FAT4 is the vertebrate ortholog of *Drosophila* Fat.
- **Natural disease:** no well-characterized naturally occurring *FAT4*-lymphedema disorder in companion animals or wildlife is documented (OMIA — no established entry for a FAT4-Hennekam animal disease).
- **Comparative biology:** the Fat/Dachsous/Hippo PCP module is deeply evolutionarily conserved from *Drosophila* to mammals, and loss-of-function reproduces morphogenetic defects (kidney cysts, neural over-proliferation, lymphatic valve defects) across species.

### 15. Model Organisms

| Model | Type | Genetic manipulation | Phenotype recapitulated | Reference |
|---|---|---|---|---|
| Mouse (*Mus musculus*) | Mammalian | *Fat4* knockout / knockdown | Cystic kidney (PCP/oriented division defect); interacts with *Vangl2*, *Fjx1* | [PMID: 18604206](https://pubmed.ncbi.nlm.nih.gov/18604206/) |
| Mouse | Mammalian | *Dchs1*/*Fat4* neuroepithelial knockdown | Increased progenitors, reduced neuronal differentiation, periventricular heterotopia; rescued by *Yap* knockdown | [PMID: 24056717](https://pubmed.ncbi.nlm.nih.gov/24056717/) |
| Mouse | Mammalian | *Fat4*-deficient | Defective lymphatic valve morphogenesis and LEC polarity | [PMID: 28705793](https://pubmed.ncbi.nlm.nih.gov/28705793/), [PMID: 32182215](https://pubmed.ncbi.nlm.nih.gov/32182215/) |
| *Drosophila melanogaster* | Invertebrate | Neuron-specific *fat* knockdown | Shortened lifespan, impaired locomotion, motoneuron/axon-targeting defects (relevant to intellectual disability) | [PMID: 28488382](https://pubmed.ncbi.nlm.nih.gov/28488382/) |

**Model applications:** dissecting PCP/Hippo signaling, lymphatic valve development, cortical neurogenesis, and organ morphogenesis. **Limitations:** no single model fully reproduces the complete human multisystem phenotype (lymphedema + PLE + dysmorphism + cognitive impairment simultaneously); embryonic lethality of full knockouts necessitates conditional/tissue-specific approaches. **Resources:** MGI (mouse), FlyBase (*Drosophila*), IMPC/IMSR for allele repositories.

---

## Mechanistic Model / Interpretation

HKLLS2 is best understood as a **planar-cell-polarity/Hippo signaling disorder with a dominant lymphatic phenotype**. The unifying lesion is loss of the giant atypical cadherin FAT4, which normally partners with Dachsous1 to transmit tissue-level polarity information and to restrain YAP-driven proliferation. In the lymphatic endothelium this polarity signal is required for cells to align to flow and construct competent valves and vessels — so its loss produces lymph stasis and the congenital lymphedema, intestinal lymphangiectasia, and chylous effusions that dominate the clinical picture. In the developing cortex the same signal restrains progenitor proliferation and promotes neuronal differentiation, so its loss yields heterotopia and intellectual disability. Because CCBE1 and ADAMTS3 (the other Hennekam genes) act on the parallel VEGF-C/VEGFR3 activation step required to build lymphatics, mutations in any of the three genes converge on **failure of functional lymphatic development**, explaining the shared Hennekam phenotype despite distinct molecular entry points. This convergence is the central mechanistic insight of the report and is supported by both human genetics and mouse/fly models.

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [24913602](https://pubmed.ncbi.nlm.nih.gov/24913602/) | *FAT4 mutations cause Hennekam syndrome, allelic to VMS* | Establishes *FAT4* as causal gene; AR inheritance; CCBE1 ~25% |
| [30450763](https://pubmed.ncbi.nlm.nih.gov/30450763/) | *ADAMTS3 loss-of-function in Hennekam* | Confirms OMIM #616006 and AR; third gene |
| [32182215](https://pubmed.ncbi.nlm.nih.gov/32182215/) | *FAT4 orchestrates LEC polarity in response to flow* | Cell-autonomous LEC mechanism; VEGF-C/VEGFR3 convergence |
| [28705793](https://pubmed.ncbi.nlm.nih.gov/28705793/) | *Dachsous1-Fat4 signaling in lymphatic valve morphogenesis* | Links valve defects to lymphedema |
| [29681106](https://pubmed.ncbi.nlm.nih.gov/29681106/) | *VMS and HS allelic phenotypes* | Clinical spectrum; HS vs VMS distinctions |
| [38028107](https://pubmed.ncbi.nlm.nih.gov/38028107/) | *Newfound features of Hennekam Syndrome* | PLE consequence; ~50 cases worldwide |
| [24056717](https://pubmed.ncbi.nlm.nih.gov/24056717/) | *DCHS1/FAT4 disrupt cortical development* | Neurodevelopmental mechanism; Hippo/YAP |
| [18604206](https://pubmed.ncbi.nlm.nih.gov/18604206/) | *Loss of Fat4 disrupts PCP → cystic kidney* | Mouse PCP mechanism |
| [28488382](https://pubmed.ncbi.nlm.nih.gov/28488382/) | *Drosophila fat neuronal knockdown* | Protein domains; neuronal model |
| [29560340](https://pubmed.ncbi.nlm.nih.gov/29560340/) | *Hennekam Syndrome case report* | No curative therapy; CDT beneficial |
| [23621851](https://pubmed.ncbi.nlm.nih.gov/23621851/) | *Primary lymphatic dysplasia classification* | Diagnostic algorithm |
| [41992670](https://pubmed.ncbi.nlm.nih.gov/41992670/) | *FAT4 c.12479+3A>G splice variant* | Variant spectrum; RT-PCR confirmation |
| [25616299](https://pubmed.ncbi.nlm.nih.gov/25616299/) | *Complicated Hennekam case* | Multimodal diagnosis; biopsy |
| [26686525](https://pubmed.ncbi.nlm.nih.gov/26686525/) | *CCBE1 multiplex kindred* | Chylous ascites, hypogammaglobulinemia |
| [25925991](https://pubmed.ncbi.nlm.nih.gov/25925991/) | *Novel CCBE1 mutation, mild HS* | Neonatal onset with generalized edema |
| [27159393](https://pubmed.ncbi.nlm.nih.gov/27159393/) | *Proteolytic activation of VEGFC/VEGFD* | ADAMTS3-CCBE1 activates VEGF-C |
| [28687807](https://pubmed.ncbi.nlm.nih.gov/28687807/) | *VEGF-C activation requires CCBE1 domains* | Molecular detail of pathway |
| [29842991](https://pubmed.ncbi.nlm.nih.gov/29842991/) | *Key molecules in lymphatic development* | PROX1/VEGFR3/CCBE1/ADAMTS3 backbone |
| [31633297](https://pubmed.ncbi.nlm.nih.gov/31633297/) | *FBXL7 biallelic mutation, novel HS form* | Candidate 4th gene in FAT4 pathway |

## Limitations and Knowledge Gaps

1. **Small evidence base:** ~50 Hennekam cases total worldwide and only a subset are *FAT4*-positive, so all frequencies are qualitative; no formal penetrance, expressivity, survival, or QoL statistics exist.
2. **Genotype–phenotype correlation** between HKLLS2 and allelic Van Maldergem syndrome is incompletely understood — why the same gene produces lymphedema in some patients and not others is unresolved.
3. **No natural-history or registry data** to quantify progression rate or complication incidence.
4. **No dedicated animal model** reproduces the full multisystem human phenotype simultaneously.
5. **Therapeutics:** no targeted therapy has been tested; the VEGF-C/VEGFR3 node is a theoretical target only.
6. **Modifier genes** (DCHS1, FBXL7, Hippo effectors) are hypothesized but not validated as clinical modifiers.
7. Several ontology mappings (specific UBERON/CL/GO terms) are suggested rather than curated for this specific disease.

## Proposed Follow-up Experiments / Actions

1. **Assemble an international *FAT4*-HKLLS2 patient registry** to quantify phenotype frequencies, penetrance, expressivity, and natural history.
2. **Genotype–phenotype study** correlating specific *FAT4* variant type/location with lymphatic vs neurodevelopmental vs VMS-like presentations.
3. **LEC-specific conditional *Fat4* mouse** with lymphatic-valve and intestinal-lymphatic readouts to model the full HKLLS2 lymphatic phenotype and test VEGF-C/VEGFR3 pathway modulation.
4. **Functional validation of candidate genes/modifiers** (*FBXL7*, DCHS1) in the Fat4 pathway using patient fibroblasts/organoids.
5. **Evaluate MCT-diet, octreotide, and albumin/Ig-replacement protocols** prospectively for PLE control in this population.
6. **Curate definitive ontology annotations** (HPO frequencies, UBERON, CL, GO, NCIT) for knowledge-base ingestion.

---

*Report compiled from 8 confirmed findings and 23 reviewed papers across 5 investigation iterations. Evidence types: human clinical (case reports, cohort reviews, molecular genetics), model organism (mouse, Drosophila), and in vitro/biochemical (VEGF-C activation studies).*


## Artifacts

- [OpenScientist final report](Hennekam_Lymphangiectasia-Lymphedema_Syndrome_2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hennekam_Lymphangiectasia-Lymphedema_Syndrome_2-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 18 |
| Quoted claims found in source | 18 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 19 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 14 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002593` (1 mention) - the report calls it "Lab/imaging/pathology"; HP calls it **Intestinal lymphangiectasia**
- `HP:0002243` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Protein-losing enteropathy**
- `HP:0001256` (1 mention) - the report calls it "Behavioral/cognitive"; HP calls it **Mild intellectual disability**
- `HP:0003073` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Hypoalbuminemia**
- `HP:0004313` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Decreased circulating immunoglobulin concentration**
- `HP:0000365` (1 mention) - the report calls it "Sensory"; HP calls it **Hearing impairment**
- `HP:0012385` (1 mention) - the report calls it "Physical"; HP calls it **Camptodactyly**
- `HP:0001252` (1 mention) - the report calls it "Neurological"; HP calls it **Hypotonia**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0002138` (3 mentions) - the report calls it "lymphatic endothelial cells", "endothelial cell of lymphatic vessel", "Tissue/cell level:** lymphatic endothelium"; CL calls it **endothelial cell of lymphatic vessel**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0002138` - called "lymphatic endothelial cells", "endothelial cell of lymphatic vessel", "Tissue/cell level:** lymphatic endothelium"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.