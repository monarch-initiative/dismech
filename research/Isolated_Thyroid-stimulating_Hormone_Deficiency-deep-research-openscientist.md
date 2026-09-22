---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-21T04:14:49.762596'
end_time: '2026-09-21T04:42:25.739367'
duration_seconds: 1655.98
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Isolated Thyroid-stimulating Hormone Deficiency
  mondo_id: MONDO:0010139
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
citation_count: 26
reference_validation:
  total_references: 26
  verified: 25
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.038
  relevance_assessed: 25
  on_topic: 20
  unresolved_references:
  - PMID:25248602
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 27
  verified: 25
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 2
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: HP:0000851
    reported_labels:
    - Lab/clinical
    ontology_label: Congenital hypothyroidism
  - term_id: HP:0006579
    reported_labels:
    - Clinical sign
    ontology_label: Prolonged neonatal jaundice
  - term_id: HP:0001508
    reported_labels:
    - Clinical sign
    ontology_label: Failure to thrive
  - term_id: HP:0007430
    reported_labels:
    - Physical
    ontology_label: Generalized edema
  - term_id: HP:0001252
    reported_labels:
    - Clinical sign
    ontology_label: Hypotonia
  - term_id: HP:0004322
    reported_labels:
    - Clinical
    ontology_label: Short stature
  - term_id: HP:0000407
    reported_labels:
    - Clinical
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0000053
    reported_labels:
    - Physical
    ontology_label: Macroorchidism
  labels_variant: 4
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
  path: Isolated_Thyroid-stimulating_Hormone_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Isolated_Thyroid-stimulating_Hormone_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Isolated Thyroid-stimulating Hormone Deficiency
- **MONDO ID:** MONDO:0010139 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Isolated Thyroid-stimulating Hormone Deficiency** covering all of the
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

# Isolated Thyroid-stimulating Hormone Deficiency (i-TSHD) — Comprehensive Disease Characteristics Report

**Target disease:** Isolated Thyroid-stimulating Hormone Deficiency
**MONDO ID:** MONDO:0010139 · **Category:** Mendelian
**OMIM:** 275100 (TSH deficiency, isolated) · **Orphanet:** ORPHA:90673 (Central congenital hypothyroidism) · **ICD-10:** E03.1 (Congenital hypothyroidism without goiter) / E23.0 (Hypopituitarism) · **MeSH:** Hypothyroidism, Congenital

---

## Summary

Isolated Thyroid-stimulating Hormone Deficiency (i-TSHD) is a rare **Mendelian congenital central hypothyroidism** in which the hypothalamic–pituitary unit fails to deliver sufficient **bioactive thyroid-stimulating hormone (TSH/thyrotropin)** to an intrinsically normal thyroid gland. The consequence is thyroid hormone deficiency (low free T4 and free T3) accompanied — paradoxically — by a TSH level that is **low, normal, or undetectable** rather than elevated. This biochemical signature is the defining feature of the disorder and its central clinical danger: **TSH-based newborn screening programs miss these patients entirely**, because they screen for the *high* TSH that characterizes far more common primary (thyroid-gland) hypothyroidism.

The disorder is genetically heterogeneous. The paradigmatic and most severe cause is **biallelic (autosomal recessive) loss-of-function of *TSHB***, the gene encoding the beta subunit of TSH — this is the *direct* lesion that abolishes bioactive hormone. Four additional genes cause isolated central hypothyroidism through *regulatory* (upstream) mechanisms: **IGSF1** (X-linked, the most prevalent single genetic cause), **TBL1X**, **TRHR**, and **IRS4**. Central hypothyroidism as a whole is roughly 1,000-fold rarer than primary hypothyroidism; the TSHB-based isolated form specifically is ultra-rare, with only dozens of families reported worldwide. Untreated, i-TSHD causes profound congenital hypothyroidism — historically termed **cretinism** — with severe mental and growth retardation. Yet it is one of the most gratifying diseases in endocrinology: **early levothyroxine replacement fully prevents the neurodevelopmental catastrophe**, and long-term follow-up confirms normal cognition when treatment begins in the neonatal period.

The therapeutic and monitoring paradigm has a critical twist. Because pituitary TSH is intrinsically deficient, it **cannot** be used to titrate replacement (unlike in primary hypothyroidism). Dosing must instead be guided by **free T4 targeted to the mid-to-upper reference range** plus clinical parameters. Prevention is necessarily secondary/tertiary: **T4-based (or T4+TSH) newborn screening** as practiced in the Netherlands, **cascade family genetic testing** once a familial variant is known, and **genetic counseling** (25% recurrence risk for recessive TSHB; consanguinity elevates risk). A key differential — and a subtle trap — is the **TSHB p.R75G assay-interference variant**, which produces spuriously "low" TSH on some immunoassays in clinically **euthyroid** people, mimicking hyperthyroidism rather than causing true deficiency.

---

## Key Findings

### 1. Genetic architecture: five genes, one direct cause

Congenital isolated central hypothyroidism (i-TSHD / C-CH) is **genetically heterogeneous but caused by a small, defined set of genes**. Five genes are established: **IGSF1, IRS4, TBL1X, TRHR, and TSHB** (Sugisawa 2019, [PMID: 31504637](https://pubmed.ncbi.nlm.nih.gov/31504637/); Boelen 2021, [PMID: 34225927](https://pubmed.ncbi.nlm.nih.gov/34225927/)). Among these, **biallelic TSHB loss-of-function is the direct and most severe cause** — it removes the hormone itself and is inherited in an autosomal recessive pattern. TSHB maps to chromosome **1p13** (HGNC:12372; NCBI Gene 7252).

In a Japanese cohort of 13 i-TSHD patients, genetic screening identified a causative mutation in **6/13 (46%)** — five hemizygous **IGSF1** mutations and one hemizygous **TBL1X** mutation — establishing IGSF1 as the *most prevalent* genetic cause of the isolated syndrome even though TSHB is the most severe. As the authors state: *"Five genes (IGSF1, IRS4, TBL1X, TRHR, and TSHB) responsible for the disease have been identified"* and *"Genetic screening of the 13 study subjects revealed six mutation-carrying patients (46%), including five hemizygous IGSF1 mutation carriers and one hemizygous TBL1X mutation carrier"* ([PMID: 31504637](https://pubmed.ncbi.nlm.nih.gov/31504637/)). More than half of clinically diagnosed cases remain genetically unexplained, indicating additional causal loci await discovery.

### 2. TSHB c.373delT: a recurrent, worldwide founder-like mutation

The single most important TSHB allele is the frameshift **c.373delT in exon 3 (p.Cys105Valfs\*114)**. It has been reported in patients from **Brazil, Germany, Belgium, USA, Switzerland, Argentina, France, Portugal, the UK and Ireland** (Borges 2019, [PMID: 31166470](https://pubmed.ncbi.nlm.nih.gov/31166470/)): *"The c.373delT mutation has previously been reported in patients from Brazil, Germany, Belgium."* In the UK/Ireland series, affected individuals were **homozygous or compound heterozygous** for c.373delT combined with a **5.4-kb TSHB deletion** or a novel p.Met1? start-loss variant (Nicholas 2017, [PMID: 27362444](https://pubmed.ncbi.nlm.nih.gov/27362444/)): *"the affected individuals were compound heterozygous for TSHB c.373delT and either a 5·4-kB TSHB deletion."* This demonstrates that both point mutations and **large structural deletions** contribute to the TSHB mutational spectrum. Functionally, in vitro work shows the C105Vfs114X variant yields a **modified/abrogated signaling profile at the TSH receptor (TSHR)** (Kalveram 2019, [PMID: 31703413](https://pubmed.ncbi.nlm.nih.gov/31703413/)).

Other reported pathogenic TSHB variants include the **exon-2 missense** alleles first described in consanguineous Japanese families (Tatsumi & Miyai 1991, [PMID: 1762181](https://pubmed.ncbi.nlm.nih.gov/1762181/)), **p.E32K (c.94G>A)** in two homozygous siblings ([PMID: 28515030](https://pubmed.ncbi.nlm.nih.gov/28515030/)), and **p.Cys105Arg (c.313T>C)** in a consanguineous infant ([PMID: 42256321](https://pubmed.ncbi.nlm.nih.gov/42256321/)).

### 3. Invisible to TSH screening; curable with early levothyroxine

The biochemical hallmark is **low free T4 and free T3 with inappropriately low/normal/undetectable TSH** (Draidi 2026, [PMID: 42256321](https://pubmed.ncbi.nlm.nih.gov/42256321/); Asirvatham 2025, [PMID: 39875149](https://pubmed.ncbi.nlm.nih.gov/39875149/)). Because TSH is *not* elevated, **TSH-based congenital-hypothyroidism screening cannot detect these cases** — the central diagnostic pitfall: *"Isolated TSH deficiency is not detected by routine TSH-based neonatal screening, representing a clinical challenge"* ([PMID: 31166470](https://pubmed.ncbi.nlm.nih.gov/31166470/)). **T4-based** programs, such as the Netherlands' heel-prick T4 screen, detect both primary and central CH ([PMID: 34225927](https://pubmed.ncbi.nlm.nih.gov/34225927/)).

The clinical stakes of missing the diagnosis are severe but the treatment is curative. In one UK/Ireland kindred, *"the younger sibling in kindred 1 developed normally following genetic diagnosis and treatment from birth"* — while late-treated relatives had intellectual disability ([PMID: 27362444](https://pubmed.ncbi.nlm.nih.gov/27362444/)). A 25-year follow-up concluded: *"Despite having severe congenital hypothyroidism, timely initiation of levothyroxine averted neurocognitive sequelae"* ([PMID: 39875149](https://pubmed.ncbi.nlm.nih.gov/39875149/)). Early, adequate replacement therefore converts a devastating disorder into one with normal outcomes.

### 4. Two mechanistic classes: direct (TSHB) vs. regulatory (IGSF1/TBL1X/TRHR/IRS4)

The five genes fall into **two mechanistically distinct groups**:

- **TSHB (direct):** mutations abolish or modify bioactive TSH presented to TSHR ([PMID: 31703413](https://pubmed.ncbi.nlm.nih.gov/31703413/)). The lesion is at the hormone itself; the phenotype is the purest, most severe *isolated* deficiency.
- **IGSF1 (X-linked, Xq26; regulatory):** a hypothalamic/pituitary membrane glycoprotein. IGSF1 deficiency reduces TSH production, decreases TRHR expression, and lowers TSH biopotency. *"IGSF1 stimulates transcription of the thyrotropin-releasing hormone receptor (TRHR) by negative modulation of the TGFβ1-Smad signaling pathway, and enhances the synthesis and biopotency of TSH"* (García 2017, [PMID: 28262687](https://pubmed.ncbi.nlm.nih.gov/28262687/)). Clinically it is a **syndrome**: macroorchidism, variable prolactin deficiency, transient partial GH deficiency, increased waist circumference, and mild attentional deficits (Joustra 2016, [PMID: 26840047](https://pubmed.ncbi.nlm.nih.gov/26840047/); Brûlé 2022, [PMID: 35708735](https://pubmed.ncbi.nlm.nih.gov/35708735/)).
- **TBL1X (regulatory):** a subunit of the **NCoR/SMRT thyroid-hormone-receptor corepressor complex**; mutations cause mild central hypothyroidism **plus sensorineural hearing loss**. *"TBL1X mutations are associated with CeH and hearing loss"* (Heinen 2016, [PMID: 27603907](https://pubmed.ncbi.nlm.nih.gov/27603907/); Hu 2024, [PMID: 39316725](https://pubmed.ncbi.nlm.nih.gov/39316725/)).
- **TRHR (regulatory):** loss-of-function (e.g., p.I131T) reduces TRH affinity and Gq signaling. *"The I131T mutation, in TRHR intracellular loop 2, decreases TRH affinity and increases the half-maximal effective concentration for signaling"* (García 2017, [PMID: 28419241](https://pubmed.ncbi.nlm.nih.gov/28419241/)).
- **IRS4 (regulatory):** part of the hypothalamic insulin/leptin signaling cascade; mutations cause familial isolated central hypothyroidism (Heinen 2018, [PMID: 30061370](https://pubmed.ncbi.nlm.nih.gov/30061370/)).

### 5. TSHB p.R75G: an assay-interference variant, NOT a loss-of-function allele

A crucial diagnostic caveat: **homozygosity for TSHB p.R75G does not alter TSH bioactivity** but **abrogates its detection by some immunoassay platforms**, producing spurious "low/undetectable TSH" and erroneous diagnoses of **hyperthyroidism** in clinically euthyroid individuals (Shaki 2022, [PMID: 34981755](https://pubmed.ncbi.nlm.nih.gov/34981755/)): *"Homozygosity for the TSHB p.R75G variant... does not alter TSH function but abrogates its detection by some immune detection-based platforms, leading to erroneous diagnosis of hyperthyroidism."* The variant is a **founder allele** with an *"Extremely high carrier rate of p.R75G TSHB in Bene Israel Indian Jews (~4%)"*, sharing a 239.7-kb haplotype block with South Asian populations. This is the mirror image of true i-TSHD — same gene, opposite clinical meaning — and must be excluded when interpreting an unexpectedly low TSH.

### 6. Epidemiology: ~1,000-fold rarer than primary hypothyroidism

Central hypothyroidism (CeH) is *"about 1000-fold rarer than PH [primary hypothyroidism]"* (Persani & Bonomi 2014, [PMID: 25248602](https://pubmed.ncbi.nlm.nih.gov/25248602/)). Independent estimates place CeH at *"approximately 1:50,000"* (Benvenga 2018, [PMID: 30294553](https://pubmed.ncbi.nlm.nih.gov/30294553/)), while central congenital hypothyroidism as a whole *"may be more prevalent than previously thought, affecting up to 1:16,000 neonates in the Netherlands"* under T4-based screening (Schoenmakers 2015, [PMID: 26416826](https://pubmed.ncbi.nlm.nih.gov/26416826/)). The **isolated TSHB-based** subset is a small fraction of this — only dozens of families reported worldwide, with roughly **74 single-gene i-TSHD patients** reviewed by Sugisawa 2019 ([PMID: 31504637](https://pubmed.ncbi.nlm.nih.gov/31504637/)).

### 7. Severity: cretinism when untreated; recessive consanguineous origin

Congenital isolated TSH deficiency *"is rare disease causing hypothyroidism including cretinism, severe mental and growth retardation"* (Tatsumi & Miyai 1991, [PMID: 1762181](https://pubmed.ncbi.nlm.nih.gov/1762181/)). The disorder was first defined in **three consanguineous Japanese families sharing an exon-2 TSHB missense mutation**. Modern neonatal presentations include **prolonged unconjugated (neonatal) hyperbilirubinemia/jaundice**, failure to thrive, generalized edema, hypotonia, and global developmental delay when diagnosis is delayed (Asirvatham 2025, [PMID: 39875149](https://pubmed.ncbi.nlm.nih.gov/39875149/): *"a female term neonate presenting with prolonged unconjugated hyperbilirubinaemia"*; Draidi 2026, [PMID: 42256321](https://pubmed.ncbi.nlm.nih.gov/42256321/)). In the isolated form, **other anterior pituitary hormones and pituitary MRI are normal** ([PMID: 39875149](https://pubmed.ncbi.nlm.nih.gov/39875149/)).

### 8. Treatment: lifelong levothyroxine, monitored by free T4 (not TSH)

Treatment is **lifelong levothyroxine (L-T4)** replacement. The distinctive challenge is monitoring: because TSH is already low/inappropriate, it **cannot** be used to titrate dose. *"L-T4 replacement in CeH should rely on the combined evaluation of several biochemical and clinical parameters in order to overcome the lack of accuracy of the single index"* (Persani & Bonomi 2014, [PMID: 25248602](https://pubmed.ncbi.nlm.nih.gov/25248602/)) — with **free T4 targeted to the mid-to-upper reference range** as the chief guide. Schoenmakers 2015 emphasizes the monitoring gap: *"Since TSH cannot be used as an indicator of euthyroidism, adequacy of treatment can be difficult to monitor due to a paucity of alternative biomarkers"* ([PMID: 26416826](https://pubmed.ncbi.nlm.nih.gov/26416826/)). Early adequate L-T4 from birth yields normal neurodevelopment ([PMID: 27362444](https://pubmed.ncbi.nlm.nih.gov/27362444/); [PMID: 39875149](https://pubmed.ncbi.nlm.nih.gov/39875149/)). NCIT term: **Levothyroxine (NCIT:C29216)**.

### 9. Prevention: T4 screening, cascade testing, genetic counseling

Because the disorder is congenital and monogenic, **prevention is secondary/tertiary rather than primary**. Three pillars: (1) **T4- or T4+TSH-based newborn screening** (not TSH-only) for early detection ([PMID: 26416826](https://pubmed.ncbi.nlm.nih.gov/26416826/); [PMID: 34225927](https://pubmed.ncbi.nlm.nih.gov/34225927/)); (2) **cascade family testing** once a familial TSHB variant is known — *"Identification of affected and carriers allows the diagnosis, treatment and adequate genetic counseling"* ([PMID: 31166470](https://pubmed.ncbi.nlm.nih.gov/31166470/)); and (3) **genetic counseling**, noting the **25% per-pregnancy recurrence risk** for autosomal-recessive TSHB and elevated risk with consanguinity ([PMID: 1762181](https://pubmed.ncbi.nlm.nih.gov/1762181/)). The differential diagnosis must exclude the **p.R75G assay-interference** variant ([PMID: 34981755](https://pubmed.ncbi.nlm.nih.gov/34981755/)).

### 10. Model organisms and comparative biology

No animal model isolates TSHB deficiency cleanly, but dwarf mouse mutants validate the TSH-biosynthesis axis. **Snell (dw) and Jackson dwarf mice** carry *Pit1/Pou1f1* mutations causing **combined loss of GH, prolactin, and TSH**: *"Two nonallelic mouse mutations with severe dwarf phenotypes are characterized by a lack of growth hormone, prolactin, and thyroid stimulating hormone"* (Camper 1990, [PMID: 1981057](https://pubmed.ncbi.nlm.nih.gov/1981057/)). *"Mutations of the pituitary transcription factor gene POU1F1... are responsible for deficiencies of GH, prolactin and thyroid stimulating hormone (TSH) in Snell and Jackson dwarf mice and in man"* (Wu 1998, [PMID: 9462743](https://pubmed.ncbi.nlm.nih.gov/9462743/)). The **Ames dwarf (df)** mouse carries a *Prop1* mutation upstream of Pit1. These are **combined pituitary hormone deficiency** models (not isolated TSH deficiency) but demonstrate the thyrotrope-differentiation branch (POU1F1 → TSHB transcription → TSH). The **hyt/hyt** mouse (Tshr loss-of-function) models TSH *resistance* downstream. Human/mouse orthology: mouse *Tshb* (NCBI Gene 22094) ↔ human *TSHB* (NCBI Gene 7252). Naturally, **central hypothyroidism occurs in Miniature Schnauzer dogs**, some with disproportionate dwarfism and combined TSH/prolactin deficiency, though *"No disease-causing mutations were found in the TSHB gene and the exons of the TRHR gene of these Schnauzers"* — the canine genetic basis remains unresolved (Voorbij 2016, [PMID: 26696394](https://pubmed.ncbi.nlm.nih.gov/26696394/)).

---

## Detailed Section-by-Section Report

### 1. Disease Information

i-TSHD is a **congenital central (secondary/tertiary) hypothyroidism** in which the thyroid gland is intrinsically normal but receives inadequate bioactive TSH stimulation. **Identifiers:** MONDO:0010139; OMIM 275100 (TSH deficiency, isolated); Orphanet ORPHA:90673 (central congenital hypothyroidism); ICD-10 E03.1/E23.0; ICD-11 5A00.1 (central hypothyroidism); MeSH "Congenital Hypothyroidism." **Synonyms/alternatives:** isolated TSH deficiency; congenital central hypothyroidism (C-CH/CCH); isolated central hypothyroidism (CeH); thyrotropin deficiency; secondary hypothyroidism (when pituitary), tertiary (when hypothalamic). Information is derived largely from **aggregated disease-level resources** (OMIM, Orphanet) supplemented by **individual patient case reports and small kindred series** — this is a rare disease characterized case-by-case.

### 2. Etiology

**Causal factors are genetic** (monogenic Mendelian). Primary cause: biallelic **TSHB** loss-of-function (autosomal recessive). Additional causal genes: **IGSF1** (X-linked, most prevalent), **TBL1X**, **TRHR**, **IRS4** (Findings 1, 4). **Genetic risk factors:** consanguinity is a major risk factor for recessive TSHB disease ([PMID: 1762181](https://pubmed.ncbi.nlm.nih.gov/1762181/)); founder alleles (c.373delT worldwide; p.R75G in specific populations, though the latter is assay interference). **Environmental risk factors:** none established as causal for the Mendelian form. **Protective factors:** not applicable/not established (this is a monogenic disorder). **Gene–environment interactions:** the principal clinically relevant "interaction" is between the p.R75G genotype and the **immunoassay platform** used — an analytical, not biological, interaction that determines whether TSH appears falsely low ([PMID: 34981755](https://pubmed.ncbi.nlm.nih.gov/34981755/)).

### 3. Phenotypes

| Phenotype | Type | HPO term | Onset | Severity/Frequency |
|---|---|---|---|---|
| Central/secondary hypothyroidism (low FT4/FT3, low-normal TSH) | Lab abnormality | HP:0011787 (Central hypothyroidism) | Congenital/neonatal | Defining; severe if untreated |
| Congenital hypothyroidism | Lab/clinical | HP:0000851 | Congenital | Severe |
| Prolonged neonatal jaundice (unconjugated) | Clinical sign | HP:0006579 | Neonatal | Common presenting sign |
| Failure to thrive | Clinical sign | HP:0001508 | Neonatal/infancy | Common if delayed dx |
| Generalized edema / myxedema | Physical | HP:0007430 | Neonatal | In untreated cases |
| Hypotonia | Clinical sign | HP:0001252 | Neonatal/infancy | Common if delayed dx |
| Global developmental delay / intellectual disability ("cretinism") | Clinical | HP:0001263 / HP:0001249 | Infancy | Severe if untreated; preventable |
| Growth retardation / short stature | Clinical | HP:0004322 | Childhood | If untreated |
| Sensorineural hearing loss (TBL1X only) | Clinical | HP:0000407 | Congenital | TBL1X subtype |
| Macroorchidism (IGSF1 only) | Physical | HP:0000053 | Puberty/adult | IGSF1 syndrome |

**Quality of life:** With early treatment, QoL and cognition are essentially normal; IGSF1 patients may show mild attentional deficits and increased mental fatigue even when treated ([PMID: 26387489](https://pubmed.ncbi.nlm.nih.gov/26387489/)). Untreated disease produces lifelong severe disability.

### 4. Genetic/Molecular Information

**Causal genes:** TSHB (1p13, HGNC:12372, OMIM 188540), IGSF1 (Xq26, X-linked), TBL1X (Xp22.31), TRHR (8q23), IRS4 (Xq22). **Variant types in TSHB:** frameshift (c.373delT/p.C105Vfs\*114), missense (p.E32K, p.C105R, exon-2 missense), start-loss (p.Met1?), and structural (5.4-kb deletion) (Finding 2; [PMID: 27362444](https://pubmed.ncbi.nlm.nih.gov/27362444/)). **Classification:** pathogenic/likely pathogenic per ACMG for the recurrent alleles. **Functional consequence:** loss of function (absent/abrogated bioactive TSH); p.R75G is a special case of **assay non-detection without functional loss** (Finding 5). **Origin:** germline. **Allele frequency:** ultra-rare in gnomAD for pathogenic alleles; p.R75G reaches ~4% carrier frequency in Bene Israel Indian Jews (founder effect). **Modifier genes / epigenetics / chromosomal abnormalities:** none established for the isolated form.

### 5. Environmental Information

**Not applicable** as a primary cause — i-TSHD is monogenic. No toxins, infectious agents, or lifestyle factors are established causes. (Broader central hypothyroidism can be *acquired* via pituitary tumor, trauma, or infiltrative disease, but these fall outside the Mendelian i-TSHD entity and belong in the differential diagnosis.)

### 6. Mechanism / Pathophysiology — causal chain

**Direct (TSHB) branch:**
1. Biallelic loss-of-function TSHB mutation → **leads to** absent or bioinactive TSH beta subunit.
2. → **results in** failure to assemble functional heterodimeric TSH (α+β).
3. → **results in** no/insufficient bioactive TSH signaling at the thyroid TSHR (Gs/cAMP pathway).
4. → **leads to** failure of thyroid follicular cells to synthesize/secrete T4 and T3.
5. → **results in** low circulating free T4 and free T3 (with low/normal/undetectable, TRH-unresponsive TSH).
6. → **leads to** systemic thyroid hormone deficiency affecting CNS myelination/maturation, growth, and metabolism.
7. → **results in** congenital hypothyroidism (jaundice, edema, hypotonia, failure to thrive) and — if untreated — irreversible neurodevelopmental/growth retardation (cretinism).

**Regulatory (upstream) branches** feed into steps 2–4 from above the pituitary hormone itself:
- **TRHR** loss → reduced TRH signaling (Gq) in thyrotropes → decreased TSH synthesis/release (inferred to reduce both amount and biopotency).
- **IGSF1** loss → reduced TRHR transcription (via TGFβ1-Smad modulation) + reduced TSH synthesis/biopotency + reduced Tshb expression (demonstrated in Igsf1-knockout mice, [PMID: 35708735](https://pubmed.ncbi.nlm.nih.gov/35708735/)).
- **TBL1X** loss → disturbed NCoR/SMRT corepressor complex → altered thyroid-hormone-receptor–mediated transcription (context-dependent; [PMID: 39316725](https://pubmed.ncbi.nlm.nih.gov/39316725/)) → mild CeH + hearing loss.
- **IRS4** loss → impaired hypothalamic insulin/leptin signaling → reduced central drive to the HPT axis.

**Molecular pathways / GO terms:** GO:0002154 (thyroid hormone mediated signaling pathway), GO:0007186 (G-protein-coupled receptor signaling), GO:0038194 (thyroid-stimulating hormone signaling), GO:0007165 (signal transduction). **Cell types (CL):** thyrotrope/thyrotropic cell of pars distalis (CL:0000209), thyroid follicular cell (CL:0002258). **Upstream vs downstream:** TRHR/IGSF1/IRS4 (hypothalamic-pituitary regulatory) are upstream; TSHB (hormone) is central; thyroid follicular response and peripheral tissue effects are downstream.

### 7. Anatomical Structures Affected

- **Primary organ:** anterior pituitary gland (adenohypophysis, UBERON:0002196) — specifically thyrotropes; and/or hypothalamus (UBERON:0001898) for TRHR/IGSF1/IRS4.
- **Secondary:** thyroid gland (UBERON:0002046) — structurally normal but understimulated; downstream effects on brain (UBERON:0000955), skeleton, liver (neonatal jaundice), heart (reversible cardiomyopathy reported in a syndromic case, [PMID: 42256321](https://pubmed.ncbi.nlm.nih.gov/42256321/)).
- **Body system:** endocrine system (hypothalamic–pituitary–thyroid axis).
- **Subcellular (GO CC):** secretory granules/secretory pathway (GO:0030141), endoplasmic reticulum (GO:0005783) for hormone folding/assembly, plasma membrane (IGSF1, TRHR).
- **Localization/lateralization:** bilateral/systemic (endocrine), not lateralized. TBL1X-associated hearing loss is typically bilateral.

### 8. Temporal Development

- **Onset:** congenital; biochemical deficiency present from birth. Clinical signs (jaundice, hypotonia, poor feeding) appear in the neonatal period; developmental delay emerges over infancy if untreated.
- **Onset pattern:** chronic/insidious; the danger is that neonates may appear near-normal at birth, and some IGSF1 cases develop CeH over time ([PMID: 35350016](https://pubmed.ncbi.nlm.nih.gov/35350016/)).
- **Progression:** without treatment, progressive and irreversible neurodevelopmental damage; with treatment, stable and normal.
- **Disease course:** lifelong (chronic) requiring lifelong L-T4.
- **Critical period:** the **neonatal/early-infancy window** is decisive for neurodevelopmental outcome — the key opportunity for intervention.

### 9. Inheritance and Population

- **Epidemiology:** CeH ~1:50,000; CCH up to 1:16,000 neonates (Netherlands, T4 screening); isolated TSHB form ultra-rare (dozens of families; ~74 single-gene i-TSHD patients reviewed) (Finding 6).
- **Inheritance:** TSHB — autosomal recessive; IGSF1, TBL1X, IRS4 — X-linked; TRHR — autosomal recessive.
- **Penetrance/expressivity:** TSHB biallelic LoF — high penetrance, severe; IGSF1 — variable expressivity, even within families carrying identical deletions ([PMID: 27146357](https://pubmed.ncbi.nlm.nih.gov/27146357/)); female carriers of X-linked variants may show mild/subclinical FT4 reduction.
- **Consanguinity:** a major factor for recessive TSHB ([PMID: 1762181](https://pubmed.ncbi.nlm.nih.gov/1762181/)).
- **Founder effects:** c.373delT (widespread pathogenic); p.R75G (~4% carriers in Bene Israel Indian Jews — assay-interference allele).
- **Recurrence risk:** 25% per pregnancy for recessive TSHB carrier couples.
- **Sex ratio:** X-linked subtypes (IGSF1, TBL1X, IRS4) predominantly affect males; TSHB and TRHR affect both sexes equally.

### 10. Diagnostics

- **Laboratory (definitive):** low **free T4** (LOINC 3024-7) and low **free T3** with **low/normal/undetectable TSH** (LOINC 3016-3); blunted or absent TSH response to TRH stimulation; normal other anterior pituitary hormones in the isolated form.
- **Imaging:** normal pituitary MRI in isolated forms (distinguishes from combined pituitary hormone deficiency/structural hypopituitarism).
- **Genetic testing:** targeted **single-gene TSHB sequencing** (including deletion/CNV analysis to catch the 5.4-kb deletion), **gene panels** covering TSHB/IGSF1/TBL1X/TRHR/IRS4, or **whole-exome sequencing** for unexplained cases. WES/WGS increasingly first-line given heterogeneity.
- **Clinical criteria:** central hypothyroidism = low FT4 with non-elevated TSH; genetic confirmation defines the Mendelian subtype.
- **Differential diagnosis:** combined pituitary hormone deficiency/hypopituitarism (additional hormone deficits, abnormal MRI); acquired central hypothyroidism (tumor, trauma, infiltration); non-thyroidal illness (sick euthyroid); and critically the **TSHB p.R75G assay-interference variant** mimicking low TSH in euthyroid individuals (Finding 10 / 5).
- **Screening:** **T4-based newborn screening** detects it; **TSH-based screening misses it**; **cascade family testing** for known variants.

### 11. Outcome/Prognosis

- **Survival/life expectancy:** normal with treatment; the disorder is not directly life-limiting when managed.
- **Morbidity:** if untreated — severe, permanent intellectual disability and growth failure (cretinism). If treated early — minimal; near-normal function ([PMID: 39875149](https://pubmed.ncbi.nlm.nih.gov/39875149/)).
- **Complications:** neonatal — reversible cardiomyopathy and hypoglycemia in severe/syndromic cases ([PMID: 42256321](https://pubmed.ncbi.nlm.nih.gov/42256321/)); untreated — irreversible neurocognitive deficit.
- **Recovery potential:** neurodevelopmental damage is preventable but not reversible once established — hence the premium on early diagnosis.
- **Prognostic factors:** **age at treatment initiation is the dominant prognostic factor**; earlier = better. Free T4 adequacy during treatment predicts outcome.

### 12. Treatment

- **Pharmacotherapy:** **Levothyroxine (L-T4)** — lifelong oral thyroid hormone replacement (NCIT:C29216; DrugBank DB00451; ATC H03AA01). Mechanism: exogenous T4 restores circulating thyroid hormone, bypassing the deficient TSH-thyroid stimulation.
- **Monitoring:** **free T4 targeted to mid-to-upper reference range** plus clinical parameters — **NOT TSH** (Finding 8; [PMID: 25248602](https://pubmed.ncbi.nlm.nih.gov/25248602/)).
- **Advanced/experimental therapeutics:** none required or established; no gene/cell/RNA therapy — L-T4 is fully effective.
- **Pharmacogenomics:** not established for this disorder beyond standard L-T4 considerations.
- **Treatment outcomes:** excellent when started neonatally; normal neurodevelopment documented at 25-year follow-up.
- **Personalized medicine:** genotype-guided recognition matters chiefly for (a) recognizing screening-negative TSHB cases early and (b) avoiding mistreatment of p.R75G "pseudo-hyperthyroidism."

### 13. Prevention

- **Primary prevention:** not possible (congenital, monogenic).
- **Secondary prevention:** **T4-based newborn screening** (detects central CH); genetic **cascade/carrier screening** in affected families; prenatal/preimplantation testing where a familial variant is known.
- **Tertiary prevention:** early L-T4 to prevent neurodevelopmental complications; lifelong FT4-guided monitoring.
- **Counseling:** genetic counseling for recurrence risk (25% recessive TSHB; X-linked risk assessment for IGSF1/TBL1X/IRS4); *"Identification of affected and carriers allows the diagnosis, treatment and adequate genetic counseling"* ([PMID: 31166470](https://pubmed.ncbi.nlm.nih.gov/31166470/)).
- **Public health:** advocacy for adding T4 (or T4+TSH) to newborn screening panels where only TSH is measured.

### 14. Other Species / Natural Disease

- **Natural disease:** central hypothyroidism occurs naturally in **Miniature Schnauzer dogs** (*Canis lupus familiaris*, NCBI Taxon 9615), some with disproportionate dwarfism and combined TSH/prolactin deficiency; TSHB/TRHR coding mutations were excluded, so the canine basis is unresolved ([PMID: 26696394](https://pubmed.ncbi.nlm.nih.gov/26696394/)).
- **Orthologous genes:** mouse *Tshb* (NCBI Gene 22094), human *TSHB* (NCBI Gene 7252); canine ortholog exists.
- **Comparative biology:** the mammalian HPT axis and TSHB are evolutionarily conserved; dwarf-mouse models demonstrate cross-species conservation of the POU1F1→TSHB→TSH pathway.
- **Zoonotic potential:** none (non-communicable genetic disorder).

### 15. Model Organisms

- **Mouse (mammalian):** **Snell (dw)** and **Jackson** dwarfs (*Pit1/Pou1f1* mutations) and **Ames (df)** dwarf (*Prop1*) — combined GH/PRL/TSH deficiency; recapitulate the **thyrotrope-differentiation** and TSH-loss branch but **not** isolated TSHB deficiency ([PMID: 1981057](https://pubmed.ncbi.nlm.nih.gov/1981057/); [PMID: 9462743](https://pubmed.ncbi.nlm.nih.gov/9462743/)).
- **Igsf1-knockout mouse:** reduced pituitary Tshb and variably reduced Trhr; models the IGSF1 regulatory mechanism ([PMID: 35708735](https://pubmed.ncbi.nlm.nih.gov/35708735/)).
- **hyt/hyt mouse:** *Tshr* loss-of-function — models TSH *resistance* (downstream), not TSHB deficiency.
- **Model limitation:** **no model cleanly isolates TSHB deficiency**; dwarf models carry combined deficiencies, limiting attribution to the TSH axis alone.
- **Resources:** MGI, IMPC, IMSR for murine alleles.

---

## Mechanistic Model / Interpretation

```
              UPSTREAM (regulatory genes)                       DIRECT (hormone gene)
   ┌───────────────────────────────────────────┐      ┌──────────────────────────────┐
   │ TRHR loss  → ↓TRH→Gq signaling in           │      │ TSHB biallelic LoF           │
   │ IGSF1 loss → ↓TRHR transcription (TGFβ-Smad) │      │  → absent/bioinactive        │
   │           → ↓TSH synthesis & biopotency      │      │    TSH β subunit             │
   │ IRS4 loss  → ↓hypothalamic insulin/leptin    │      └──────────────┬───────────────┘
   │ TBL1X loss → NCoR/SMRT corepressor defect    │                     │
   └───────────────────────┬─────────────────────┘                     │
                           ▼                                            ▼
                 ↓ Thyrotrope output of BIOACTIVE TSH  ◄─────────────────┘
                           │
                           ▼
        ↓ TSHR (Gs/cAMP) stimulation of thyroid follicular cells
                           │
                           ▼
              ↓ Synthesis/secretion of T4 & T3
                           │
                           ▼
   LOW free T4 / free T3  +  LOW/normal/UNDETECTABLE TSH (TRH-unresponsive)
                           │
        ┌──────────────────┴───────────────────┐
        ▼                                       ▼
  INVISIBLE to TSH-based                 Systemic thyroid hormone deficiency
  newborn screening                      (CNS myelination, growth, metabolism)
        │                                       │
        ▼                                       ▼
  Delayed diagnosis ───────────────►  Untreated: cretinism (irreversible)
        │                             Early L-T4 (FT4-guided): NORMAL outcome
        ▼
  Prevention: T4-based screening + cascade genetic testing + counseling
```

**Key interpretive points:** (1) The disorder has a **two-tier genetic architecture** — a direct hormone defect (TSHB) and four regulatory defects (IGSF1/TBL1X/TRHR/IRS4) — that converge on a single final common pathway: insufficient bioactive TSH at the thyroid. (2) The **low-TSH biochemistry** is simultaneously the diagnostic signature and the reason the disease slips through TSH-only screening. (3) The **p.R75G paradox** shows that a TSHB variant can produce identical-*looking* biochemistry (low TSH) with the *opposite* clinical meaning (euthyroid), underscoring that assay behavior must be interpreted alongside genotype and free thyroid hormones. (4) Because the endpoint is a hormone that can be **replaced pharmacologically**, the disease is fully treatable — the entire prognosis hinges on **timing of diagnosis**, not on any limitation of therapy.

---

## Evidence Base

| PMID | Paper (abbrev.) | Supports finding(s) | Evidence type |
|---|---|---|---|
| [31504637](https://pubmed.ncbi.nlm.nih.gov/31504637/) | Sugisawa 2019 — Genetics of congenital i-TSHD | 1, 6 (five genes; IGSF1 predominance; ~74 patients) | Human cohort + review |
| [31166470](https://pubmed.ncbi.nlm.nih.gov/31166470/) | Borges 2019 — Recurrent TSHB mutation undetectable in screening | 2, 3, 9 (c.373delT worldwide; screening pitfall; cascade counseling) | Human clinical |
| [27362444](https://pubmed.ncbi.nlm.nih.gov/27362444/) | Nicholas 2017 — TSHβ defects UK/Ireland | 2, 3, 8 (compound het; 5.4-kb deletion; early tx normal) | Human clinical |
| [31703413](https://pubmed.ncbi.nlm.nih.gov/31703413/) | Kalveram 2019 — C105Vfs114X at TSHR | 2, 4 (modified TSHR signaling) | In vitro |
| [34981755](https://pubmed.ncbi.nlm.nih.gov/34981755/) | Shaki 2022 — TSHB R75G founder variant | 5, 9 (assay interference; ~4% carriers) | Human genetics |
| [39875149](https://pubmed.ncbi.nlm.nih.gov/39875149/) | Asirvatham 2025 — TSHB CCH 25-yr follow-up | 3, 7, 8 (jaundice; early tx averts sequelae) | Human clinical |
| [42256321](https://pubmed.ncbi.nlm.nih.gov/42256321/) | Draidi 2026 — ADAR+TSHB infant | 3, 7 (biochemistry; reversible cardiomyopathy) | Human case |
| [25248602](https://pubmed.ncbi.nlm.nih.gov/25248602/) | Persani & Bonomi 2014 — CeH substitution therapy | 6, 8 (1000-fold rarer; FT4-guided dosing) | Review |
| [26416826](https://pubmed.ncbi.nlm.nih.gov/26416826/) | Schoenmakers 2015 — CCH review | 6, 8 (1:16,000; monitoring gap) | Review |
| [30294553](https://pubmed.ncbi.nlm.nih.gov/30294553/) | Benvenga 2018 — CeH congenital etiologies | 6 (~1:50,000) | Review |
| [28262687](https://pubmed.ncbi.nlm.nih.gov/28262687/) | García 2017 — IGSF1 controls TRHR | 4 (IGSF1 regulatory mechanism) | Mechanistic |
| [28419241](https://pubmed.ncbi.nlm.nih.gov/28419241/) | García 2017 — TRHR mutation | 4 (TRHR ligand affinity/Gq) | Mechanistic |
| [27603907](https://pubmed.ncbi.nlm.nih.gov/27603907/) | Heinen 2016 — TBL1X | 4 (CeH + hearing loss) | Human genetics |
| [30061370](https://pubmed.ncbi.nlm.nih.gov/30061370/) | Heinen 2018 — IRS4 | 4 (IRS4 familial CeH) | Human genetics |
| [26840047](https://pubmed.ncbi.nlm.nih.gov/26840047/) | Joustra 2016 — IGSF1 case series | 4 (IGSF1 syndrome; most common genetic cause) | Human cohort |
| [35708735](https://pubmed.ncbi.nlm.nih.gov/35708735/) | Brûlé 2022 — Igsf1 KO mouse | 4, 10 (reduced Tshb) | Mouse model |
| [1762181](https://pubmed.ncbi.nlm.nih.gov/1762181/) | Tatsumi & Miyai 1991 — first TSHB cases | 7, 9 (cretinism; recessive consanguineous) | Human genetics |
| [1981057](https://pubmed.ncbi.nlm.nih.gov/1981057/) | Camper 1990 — Pit1/Snell dwarf | 10 (dwarf models) | Mouse model |
| [9462743](https://pubmed.ncbi.nlm.nih.gov/9462743/) | Wu 1998 — POU1F1/PROP1 | 10 (cross-species conservation) | Human/mouse |
| [26696394](https://pubmed.ncbi.nlm.nih.gov/26696394/) | Voorbij 2016 — Schnauzer CeH | 10 (natural canine disease) | Veterinary |
| [39316725](https://pubmed.ncbi.nlm.nih.gov/39316725/) | Hu 2024 — TBL1X in liver cells | 4 (TH-action mechanism) | In vitro |

---

## Limitations and Knowledge Gaps

1. **Case-based evidence.** Because the isolated TSHB form is ultra-rare (dozens of families worldwide), most clinical knowledge derives from case reports and small kindreds rather than powered cohorts. Frequency figures for individual phenotypes are qualitative.
2. **>50% of cases unexplained.** In Sugisawa's cohort only 46% carried an identifiable mutation; additional causal genes for isolated central hypothyroidism almost certainly remain undiscovered.
3. **No clean animal model.** All available mouse models (Snell, Jackson, Ames) carry *combined* pituitary hormone deficiencies; there is no widely used isolated *Tshb*-knockout that models the human disease purely. This limits mechanistic dissection of TSHB-specific effects.
4. **Monitoring biomarker gap.** Because TSH cannot indicate euthyroidism in CeH, and free T4 targets are imperfect, there is a genuine paucity of validated biomarkers to confirm adequate replacement — an open clinical problem.
5. **Canine genetic basis unresolved.** Natural central hypothyroidism in Miniature Schnauzers lacks an identified mutation, so comparative-biology insights are incomplete.
6. **p.R75G under-recognition.** The assay-interference variant is likely under-recognized outside the populations where it has been studied, risking misdiagnosis.
7. **Epigenetics, modifiers, environment.** No modifier genes, epigenetic mechanisms, or environmental contributors have been characterized for the isolated Mendelian form — this may reflect true absence or simply lack of study.

---

## Proposed Follow-up Experiments / Actions

1. **Advocate for T4-inclusive newborn screening.** Quantify how many i-TSHD cases are missed under TSH-only programs versus T4-based programs; use this to support policy change in jurisdictions screening TSH alone.
2. **Gene discovery in unexplained cases.** Apply whole-genome sequencing and transcriptomic/functional follow-up to the >50% of genetically unexplained isolated central hypothyroidism cohorts to identify novel causal loci.
3. **Generate an isolated Tshb-knockout mouse** (or conditional thyrotrope-specific line) to model the pure disease, enabling clean study of TSHB-specific biology and testing of early-replacement timing windows.
4. **Develop/validate alternative monitoring biomarkers** for CeH replacement adequacy (e.g., tissue-based markers of thyroid hormone action such as SHBG, ferritin, or ankle-reflex/metabolic indices) to overcome the "TSH-can't-be-used" problem.
5. **Population screening for TSHB p.R75G** on relevant immunoassay platforms in founder populations to prevent misdiagnosis of hyperthyroidism; consider laboratory flagging of discordant low-TSH/normal-FT4 results.
6. **Resolve the canine genetic basis** in Miniature Schnauzers via whole-genome sequencing, potentially revealing a novel HPT-axis regulator relevant to unexplained human cases.
7. **Establish a longitudinal i-TSHD registry** integrating genotype, screening method, age at treatment, FT4 trajectories, and neurodevelopmental outcomes to define natural history and optimize FT4 targets.

---

*Report compiled from 11 confirmed findings across 5 investigative iterations and 49 reviewed papers. Evidence types are labeled human clinical, human genetics, mechanistic/in vitro, mouse model, and veterinary throughout.*


## Artifacts

- [OpenScientist final report](Isolated_Thyroid-stimulating_Hormone_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Isolated_Thyroid-stimulating_Hormone_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 26 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 25 |
| On topic | 20 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:25248602` (8 mentions) - Identifier did not resolve to a record

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 14 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000851` (1 mention) - the report calls it "Lab/clinical"; HP calls it **Congenital hypothyroidism**
- `HP:0006579` (1 mention) - the report calls it "Clinical sign"; HP calls it **Prolonged neonatal jaundice**
- `HP:0001508` (1 mention) - the report calls it "Clinical sign"; HP calls it **Failure to thrive**
- `HP:0007430` (1 mention) - the report calls it "Physical"; HP calls it **Generalized edema**
- `HP:0001252` (1 mention) - the report calls it "Clinical sign"; HP calls it **Hypotonia**
- `HP:0004322` (1 mention) - the report calls it "Clinical"; HP calls it **Short stature**
- `HP:0000407` (1 mention) - the report calls it "Clinical"; HP calls it **Sensorineural hearing impairment**
- `HP:0000053` (1 mention) - the report calls it "Physical"; HP calls it **Macroorchidism**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0002154` (1 mention) - the report calls it "thyroid hormone mediated signaling pathway"; GO calls it **thyroid hormone receptor signaling pathway**, and lists "thyroid hormone mediated signalling pathway" among its other names
- `GO:0007186` (1 mention) - the report calls it "G-protein-coupled receptor signaling"; GO calls it **G protein-coupled receptor signaling pathway**
- `GO:0038194` (1 mention) - the report calls it "thyroid-stimulating hormone signaling"; GO calls it **thyroid-stimulating hormone signaling pathway**
- `UBERON:0002046` (1 mention) - the report calls it "Secondary:** thyroid gland"; UBERON calls it **thyroid gland**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `ORPHA:90673` - called "Central congenital hypothyroidism", "central congenital hypothyroidism"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.