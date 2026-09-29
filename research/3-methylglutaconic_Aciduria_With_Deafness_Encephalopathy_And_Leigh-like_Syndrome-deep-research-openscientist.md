---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T22:00:08.291947'
end_time: '2026-09-01T22:42:27.425990'
duration_seconds: 2539.13
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: 3-methylglutaconic Aciduria With Deafness Encephalopathy And Leigh-like
    Syndrome
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
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 14
  quotes_valid: 12
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:39592976
  - PMID:35943861
  relevance_assessed: 22
  on_topic: 21
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 55
  verified: 53
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 28
  labels_matching: 10
  labels_mismatched: 13
  mislabelled_terms:
  - term_id: HP:0003535
    reported_labels:
    - Lab
    ontology_label: 3-Methylglutaconic aciduria
  - term_id: HP:0000407
    reported_labels:
    - Sign
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0001332
    reported_labels:
    - Sign
    ontology_label: Dystonia
  - term_id: HP:0001252
    reported_labels:
    - Sign
    ontology_label: Hypotonia
  - term_id: HP:0001987
    reported_labels:
    - Lab
    ontology_label: Hyperammonemia
  - term_id: HP:0001943
    reported_labels:
    - Lab
    ontology_label: Hypoglycemia
  - term_id: HP:0000252
    reported_labels:
    - Sign
    ontology_label: Microcephaly
  - term_id: HP:0000648
    reported_labels:
    - Sign
    ontology_label: Optic atrophy
  - term_id: HP:0001999
    reported_labels:
    - Sign
    ontology_label: Abnormal facial shape
  - term_id: HP:0001249
    reported_labels:
    - Sign
    ontology_label: Intellectual disability
  - term_id: HP:0002650
    reported_labels:
    - Sign
    ontology_label: Scoliosis
  - term_id: CL:0000540
    reported_labels:
    - neuron; medium spiny/striatal neurons
    ontology_label: neuron
  - term_id: CL:0000598
    reported_labels:
    - cochlear hair cell
    ontology_label: pyramidal neuron
  labels_variant: 5
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
  path: 3-methylglutaconic_Aciduria_With_Deafness_Encephalopathy_And_Leigh-like_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: 3-methylglutaconic_Aciduria_With_Deafness_Encephalopathy_And_Leigh-like_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** 3-methylglutaconic Aciduria With Deafness Encephalopathy And Leigh-like Syndrome
- **MONDO ID:**  (if available)
- **Category:** Disease

## Research Objectives

Please provide a comprehensive research report on **3-methylglutaconic Aciduria With Deafness Encephalopathy And Leigh-like Syndrome** covering all of the
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

# MEGDEL / MEGD(H)EL Syndrome — Comprehensive Disease Characterization

**Disease:** 3-Methylglutaconic Aciduria with Deafness, Encephalopathy, and Leigh-like syndrome (MEGDEL); with hepatopathy = MEGD(H)EL / MEGDHEL
**Causal gene:** *SERAC1* (serine active site-containing protein 1)
**Category:** Rare autosomal-recessive inborn error of metabolism (secondary 3-methylglutaconic aciduria / mitochondrial phospholipid-remodeling disorder)

> Evidence base: This report is compiled from disease-level resources (OMIM, Orphanet) and primary human clinical literature (case reports and small case series), the landmark gene-discovery study, one large systematic MRI series, in-vitro fibroblast/functional studies, and one naturally occurring animal (canine) model. No population EHR cohort or large registry natural-history dataset was available; most clinical detail derives from aggregated individual patient reports (~100 patients reported worldwide).

---

## 1. Disease Information

MEGDEL syndrome is a rare autosomal-recessive neurometabolic disorder defined by the constellation **3-M**ethylglutaconic aciduria, **D**eafness (sensorineural, with dystonia), **E**ncephalopathy, and **L**eigh-**l**ike changes on brain MRI. When infantile **h**epatopathy is present (it is a cardinal feature), the disorder is termed **MEGD(H)EL / MEGDHEL**. It is caused by biallelic pathogenic variants in *SERAC1* and is one of the "secondary" 3-methylglutaconic acidurias caused by defective mitochondrial phospholipid remodeling.

- "MEGDEL syndrome is an autosomal recessive disorder, clinically characterized by 3-methylglutaconic aciduria, psychomotor delay, muscle hypotonia, sensorineural deafness, and Leigh-like lesions on brain magnetic resonance imaging" (PMID 32684373).
- "This disorder is caused by biallelic mutations in serine active site-containing protein 1 (SERAC1) gene. When these patients experience hepatopathy (H)…the syndrome is referred to as MEGD(H)EL" (PMID 39592976).

**Key identifiers**
- **OMIM:** #614739 (MEGDEL syndrome) — confirmed in PMID 25642805 ("MEGDEL syndrome … MIM #614739").
- **Gene:** *SERAC1*, HGNC:21061; NCBI Gene 84947; Ensembl ENSG00000122335; UniProt Q96JX3; locus 6q25.3 (homozygosity mapping candidate region 6q25.2–6q26, PMID 23918762).
- **Orphanet:** ORPHA:352328 (MEGD(H)EL syndrome) *(database identifier; confirm in current Orphanet)*.
- **MONDO:** MONDO:0013875 *(database identifier; confirm in current MONDO release)*.
- **MeSH:** no dedicated descriptor; indexed under "3-Methylglutaconic aciduria," "Mitochondrial Diseases," "Leigh Disease."
- **ICD-11:** 5C50.4-class (disorders of mitochondrial/energy metabolism) / ICD-10 E71.1-class *(no specific code)*.

**Synonyms / alternative names:** MEGDEL syndrome; MEGD(H)EL / MEGDHEL syndrome; 3-methylglutaconic aciduria with deafness, encephalopathy and Leigh-like syndrome; 3-methylglutaconic aciduria type IV with sensorineural deafness, encephalopathy and Leigh-like syndrome (PMID 23918762); SERAC1 deficiency; "dystonia–deafness syndrome" (SERAC1-related).

**MONDO suggestion:** MONDO:0013875 (3-methylglutaconic aciduria with deafness, encephalopathy, and Leigh-like syndrome).

---

## 2. Etiology

**Primary cause — genetic.** MEGDEL is monogenic and recessive: biallelic loss-of-function of *SERAC1* is necessary and sufficient. "Using exome sequencing, we identify SERAC1 mutations as the cause of MEGDEL syndrome" (PMID 22683713).

**Genetic risk factors.**
- Causal variants: biallelic *SERAC1* pathogenic variants (see §4). No susceptibility loci or GWAS signals exist (Mendelian disorder).
- **Consanguinity** is a major risk factor — most reported families are consanguineous and homozygous (e.g., Tunisia PMID 35943861; Saudi Arabia PMID 38559521; Palestine PMID 25051967; Turkey PMID 27186703; Egypt PMID 40821445).

**Environmental risk factors.** None established as causal. As in other mitochondrial disorders, **intercurrent catabolic stress** (infection, fasting, fever, surgery/anesthesia) can precipitate metabolic decompensation/crises but does not cause the disease. No toxin, occupational, or infectious cause.

**Protective factors.** No genetic or environmental protective factors identified. Within the *SERAC1* spectrum, **residual protein function** (hypomorphic missense/splice alleles) is associated with milder disease (see §4/§8), functioning as an intrinsic genetic modifier of severity rather than a protective allele per se.

**Gene–environment interactions.** Not formally studied. Clinically, catabolic triggers interact with the underlying energy-metabolism defect to provoke crises; avoidance of fasting and prompt treatment of infections is protective against decompensation.

---

## 3. Phenotypes

Phenotype type key: **Sign/symptom**, **Lab abnormality**, **Imaging**, **Behavioral**. Onset is predominantly **neonatal–infantile**; course is **progressive** for the neurological features. Frequencies below are qualitative (derived from aggregated case reports; large-cohort percentages are limited).

| Phenotype | Type | HPO term | Onset | Frequency | Notes |
|---|---|---|---|---|---|
| 3-methylglutaconic aciduria | Lab | HP:0003535 | Neonatal | Universal (defining) | Persistent; with 3-methylglutaric aciduria |
| Sensorineural hearing loss / deafness | Sign | HP:0000407 | Infancy | Very frequent (near-universal, "D") | Often severe; progressive; managed with cochlear implants |
| Dystonia | Sign | HP:0001332 | Infancy–childhood | Very frequent ("D") | Progressive, often generalized |
| Spasticity / spastic tetraparesis | Sign | HP:0001257 / HP:0001285 | Childhood, progressive | Frequent | Basis of the cHSP-like milder phenotype |
| Severe psychomotor/developmental delay & regression | Sign | HP:0011344 / HP:0002376 | Infancy | Very frequent ("E") | Encephalopathy |
| Muscle hypotonia (truncal) | Sign | HP:0001252 | Infancy | Frequent | Early feature |
| Leigh-like basal ganglia lesions | Imaging | HP:0002518/HP:0002134 | Infancy | Very frequent ("L") | "Putaminal eye" pathognomonic |
| Infantile hepatopathy / acute liver failure | Sign/Lab | HP:0001410 / HP:0001392 | Neonatal | Cardinal (defining "H") | May have normal transaminases, no cholestasis |
| Elevated lactate (blood/CSF) | Lab | HP:0002151 / HP:0003128 | Neonatal | Frequent (variable) | Can be normal in some |
| Elevated plasma alanine | Lab | HP:0500181-class | Neonatal | Frequent | Marker of lactic acidosis |
| Hyperammonemia | Lab | HP:0001987 | Neonatal | Subset (severe cases) | Can dominate neonatal crisis |
| Hypoglycemia | Lab | HP:0001943 | Neonatal | Subset | During crisis |
| Seizures / epilepsy (incl. myoclonic) | Sign | HP:0001250 / HP:0002123 | Variable | Subset | |
| Microcephaly | Sign | HP:0000252 | Infancy | Subset | |
| Optic atrophy | Sign | HP:0000648 | Childhood | Subset (expanding phenotype) | |
| Feeding difficulties / failure to thrive / growth retardation | Sign | HP:0011968 / HP:0001508 | Infancy | Frequent | |
| Dysmorphic features | Sign | HP:0001999 | Congenital | Subset | |
| Intellectual disability | Sign | HP:0001249 | Childhood | Frequent | |
| Autistic behavior | Behavioral | HP:0000729 | Variable | Subset (milder/adult) | |
| Scoliosis | Sign | HP:0002650 | Childhood | Subset | |

Supporting quotes:
- "microcephaly, growth retardation, dysmorphic features, severe sensorineural deafness, progressive spasticity, dystonia, seizures, basal ganglia involvement. Metabolic acidosis, mild hyperammonemia and lactic acidemia were accompanied with clinical findings in newborn period" (PMID 27186703).
- "sensorineural hearing loss, encephalopathy, and Leigh-like pattern on MRI (MEGDEL syndrome), as well as developmental delay and developmental regression, bilateral optic nerve atrophy, microcephaly, and myoclonic epilepsy" (PMID 24997715).

**Quality-of-life impact.** Severe: combined profound deafness, movement disorder (dystonia/spasticity), intellectual disability, epilepsy and feeding problems produce major dependence for daily functioning; most severely affected children are non-ambulatory and non-verbal with high care needs. Formal QoL instruments (EQ-5D/SF-36/PROMIS) have not been reported for this ultra-rare disease.

---

## 4. Genetic / Molecular Information

**Causal gene:** *SERAC1* (HGNC:21061; OMIM *614725; gene product Q96JX3), chromosome 6q25.3. It is the **only** gene associated with MEGDEL. "Homozygosity mapping identified a candidate locus on 6q25.2-6q26" (PMID 23918762).

**Pathogenic variant spectrum (germline; predominantly loss-of-function).** Reported biallelic variants include:
- Nonsense: **c.1379G>A (p.Trp460*)** homozygous, Tunisia (PMID 35943861); **c.442C>T (p.Arg148*)** (PMID 24997715).
- Frameshift: **c.1018delT** homozygous, Palestine (PMID 25051967); **c.438delC (p.Thr147Argfs*22)** (PMID 24997715).
- Splice-site: novel splice variant causing juvenile cHSP in a large family (PMID 28916646).
- Insertion: **rs797045105** (c...CATG insertion), homozygous (PMID 33613893).
- Structural / exonic deletion: deletion of ≥ exons 2–4 (pathogenic) (PMID 35781780); a homozygous deletion variant (PMID 38559521).
- Missense (often milder/hypomorphic): **c.1495A>G (p.Met499Val)** in complicated HSP (PMID 35223715); **c.1601A>T (p.His534Leu)** likely pathogenic (PMID 35781780). Note: **p.Phe471 (rs112780453)** is considered **benign** (PMID 37711114).

"Whole exome sequencing revealed two loss-of-function mutations in SERAC1 in trans: c.438delC (p.T147Rfs*22) and c.442C>T (p.R148X)" (PMID 24997715).

**Variant classification (ACMG/AMP):** most reported truncating/frameshift/large-deletion variants are Pathogenic; several missense are Likely pathogenic or VUS; rs112780453 (p.F471) benign. **Functional consequence:** loss of function — "Both mutations were found to lead to decreased or absent expression of SERAC1" (PMID 35943861); a C-terminal truncation mislocalizes the protein away from mitochondria (PMID 34751152).

**Allele frequency:** individual pathogenic alleles are extremely rare in gnomAD (mostly absent or singleton); no common founder allele established, though recurrent homozygous alleles occur in specific consanguineous pedigrees. Carrier frequency is not precisely established (ultra-rare).

**Somatic vs germline:** exclusively germline. **Modifier genes:** none defined; the principal modifier of severity is the *SERAC1* genotype itself (LoF vs hypomorphic). **Epigenetic information:** none reported. **Chromosomal abnormalities:** none characteristic (large intragenic deletions detectable by CMA/CNV analysis occur, e.g., exon 2–4 deletion).

**Gene/GO annotations:** *SERAC1* — GO:0006655 (phosphatidylglycerol biosynthetic process) / GO:0032048 (cardiolipin metabolic process); GO:0044233 (mitochondria-associated ER membrane); GO:0030299 (intestinal cholesterol absorption)/cholesterol transport; molecular function serine hydrolase / phospholipid remodeling (transacylase) activity.

---

## 5. Environmental Information

- **Environmental/toxic factors:** none causal.
- **Lifestyle factors:** not applicable (congenital genetic disease).
- **Infectious agents:** none causal. Infections act only as non-specific catabolic **triggers** of metabolic decompensation; neonates may present with a **sepsis-like** metabolic crisis that mimics infection.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic *SERAC1* loss-of-function variants** → **absent or non-functional SERAC1 protein** (demonstrated: no protein detected in patient fibroblasts, PMID 34751152; decreased/absent expression, PMID 35943861).
2. Loss of SERAC1 at the **mitochondria-associated ER membrane (MAM)/ER–mitochondria contact site** → **impaired phosphatidylglycerol (PG) remodeling** (elevated PG-34:1, decreased PG-36:1) (demonstrated in vitro, PMID 22683713).
3. Altered PG pool → **abnormal cardiolipin subspecies composition** → **impaired assembly/stability and function of OXPHOS complexes** (branch A; inferred from cardiolipin's role, with measured complex I/III/IV reduction in liver mitochondria, PMID 34751152).
4. In parallel (branch B): reduced **bis(monoacylglycerol)phosphate (BMP)** → **accumulation of free/unesterified cholesterol** and defective **intracellular cholesterol trafficking** (demonstrated by abnormal filipin staining, PMID 22683713; PMID 34751152).
5. In parallel (branch C): disrupted ER–mitochondria interplay → **fragmented mitochondrial network + abnormal (circular) cristae** and **deficient Ca²⁺ transfer** from cytoplasm to mitochondria (demonstrated, PMID 34751152; ultrastructure PMID 35781780).
6. Convergence → **mitochondrial energy (OXPHOS) failure / bioenergetic insufficiency** → secondary **3-methylglutaconic aciduria and lactic acidosis** (biomarkers of mitochondrial dysfunction).
7. Bioenergetic failure in high-energy-demand tissues → **selective vulnerability**: basal-ganglia (putamen>caudate>pallidus) neurodegeneration → **dystonia/spasticity/Leigh-like MRI**; cochlear/auditory neurons → **sensorineural deafness**; hepatocytes → **infantile hepatopathy/liver failure**; brain broadly → **encephalopathy/developmental delay**.
8. (Additional/inferred) SERAC1 participates in a **mitochondrial serine transporter complex required for mtDNA maintenance**, providing a further route to mitochondrial dysfunction (PMID 35235340; some patients show hepatic mtDNA depletion, PMID 23918762).

Upstream nodes = SERAC1 LoF and MAM phospholipid-remodeling defect; downstream = cardiolipin/OXPHOS failure, cholesterol mistrafficking, Ca²⁺ dysregulation, and tissue-specific neuro-/hepatodegeneration.

### Detail by category
- **Molecular pathways / biochemistry:** phosphatidylglycerol → cardiolipin remodeling pathway (glycerophospholipid metabolism, KEGG hsa00564); intracellular cholesterol transport (LDL/lysosomal → ER). Secondary block manifests as leucine-independent 3-MGA-uria (distinct from primary AUH defect).
- **Cellular processes:** disrupted ER–mitochondria contact, mitochondrial fission/fusion imbalance (network fragmentation), impaired mitochondrial Ca²⁺ uptake, and downstream apoptosis/neurodegeneration; bioenergetic failure.
- **Protein dysfunction:** loss of function via truncation/degradation or mislocalization ("the mutant protein with a 45-amino acid C-terminal truncation was distributed throughout the cell, whereas wild-type SERAC1 partially colocalized with the mitochondrial marker MT-CO1," PMID 34751152).
- **Metabolic changes:** impaired oxidative phosphorylation (complexes I/III/IV ↓), lactic acidosis, elevated alanine, 3-methylglutaconic/3-methylglutaric aciduria; altered phospholipid/cholesterol homeostasis.
- **Lipidomics:** ↑PG-34:1, ↓PG-36:1 (increased PG34:1/PG36:1 ratio), altered cardiolipin subspecies, ↓BMP, ↑free cholesterol.
- **Immune involvement:** none primary.
- **Tissue-damage mechanisms:** energy-deprivation neurodegeneration (Leigh-like), mitochondrial hepatopathy; oxidative/bioenergetic stress inferred.
- **Molecular profiling:** dedicated transcriptomic/proteomic/GEO datasets are limited; mechanistic data derive from patient fibroblasts, COS-1 transfection, and one functional cell model (PMID 35235340).

**GO term suggestions:** GO:0044233 (mitochondria-associated ER membrane), GO:0032048 (cardiolipin metabolic process), GO:0006655 (phosphatidylglycerol biosynthesis), GO:0006874 (cellular Ca²⁺ homeostasis), GO:0007005 (mitochondrion organization), GO:0006119 (oxidative phosphorylation), GO:0008203 (cholesterol metabolic process).
**Cell types (CL):** CL:0000540 (neuron; medium spiny/striatal neurons), CL:0000598 (cochlear hair cell)/auditory neurons, CL:0000182 (hepatocyte).

---

## 7. Anatomical Structures Affected

**Organ level (primary):** brain — especially **basal ganglia (putamen UBERON:0001874 > caudate nucleus UBERON:0001873 > globus pallidus UBERON:0002477)**; inner ear / **cochlea (UBERON:0001844)** (auditory system); **liver (UBERON:0002107)**. Secondary/other: eye/**optic nerve (UBERON:0000941/UBERON:0000941)**, skeletal muscle, peripheral nerves, heart, endocrine organs, skeleton (scoliosis) — reflecting the broadening multisystem spectrum (PMID 32684373).

**Body systems:** nervous (central — extrapyramidal/basal ganglia, and sensory — auditory), digestive/hepatobiliary, and (variably) ophthalmologic, musculoskeletal, cardiac, endocrine.

**Tissue/cell level:** nervous tissue (striatal neurons), sensory epithelium/neurons of the cochlea, hepatic parenchyma (hepatocytes with granular cytoplasm, fine lipid droplets — PMID 35781780).

**Subcellular level:** **mitochondrion (GO:0005739)**, **mitochondrial inner membrane/cristae (GO:0005743)**, **ER membrane (GO:0005789)**, and the **mitochondria-associated ER membrane (GO:0044233)**; abnormal circular mitochondrial cristae and fragmented mitochondrial network.

**Localization/lateralization:** basal-ganglia lesions and hearing loss are **bilateral and symmetric** (PMID 35223715: "symmetric flake abnormal signal shadow in the bilateral basal ganglia").

---

## 8. Temporal Development

- **Onset:** typically **neonatal to early-infantile**; often an **acute** neonatal metabolic/hepatic crisis (sepsis-like). Milder hypomorphic genotypes present later (juvenile complicated HSP; rarely adult-onset dystonia).
- **Two-phase natural history (classic/severe):**
  1. **Neonatal decompensation** — lactic acidosis, hepatopathy ± hyperammonemia/hypoglycemia (can be lethal; PMID 38445077, PMID 34751152).
  2. **Chronic progressive neurodegeneration** — infantile sensorineural deafness, truncal hypotonia, severe psychomotor delay/regression, then progressive spasticity and dystonia with basal-ganglia degeneration (PMID 27186703).
- **MRI staging (5 stages):** stage 1 pallidal T2 change → stage 2 putaminal/caudate swelling with spared dorsal-putaminal "eye" → later progressive putaminal involvement (PMID 25642805).
- **Progression rate/course:** chronic, progressive; **variable** by genotype. **Duration:** lifelong/chronic; often shortened by early death in severe cases.
- **Remission:** no true remission; however, some milder patients **stabilize or partially improve** ("her verbal and motor development has progressively improved…exceeding clinical expectations," PMID 35781780).
- **Critical period / intervention window:** the **neonatal metabolic crisis** is the key window where aggressive metabolic/supportive management can be life-saving.

**HPO onset modifiers:** HP:0003623 (Neonatal onset), HP:0011463 (Childhood onset), HP:0003577 (Congenital onset for some features), HP:0003676 (Progressive).

---

## 9. Inheritance and Population

- **Inheritance:** **autosomal recessive** (AR). "MEGDEL syndrome is an autosomal recessive disorder" (PMID 32684373).
- **Penetrance:** essentially complete for biallelic LoF; **expressivity variable** (severity graded by genotype/residual function).
- **Epidemiology:** ultra-rare — "about 100 cases reported worldwide" (PMID 35943861); "at least 102 patients have been reported" since 2006 (PMID 32684373). Precise prevalence/incidence are **not established** (Orphanet: prevalence <1/1,000,000; unknown).
- **Consanguinity / founder effects:** strong role of consanguinity; recurrent homozygous variants in individual pedigrees; **no single global founder allele** established. Over-representation of reported families from the **Middle East/North Africa** (Tunisia, Saudi Arabia, Palestine, Turkey, Egypt, Iran) plus reports from Europe, China, and elsewhere.
- **Carrier frequency:** not precisely defined; individual alleles are very rare in gnomAD.
- **Sex ratio:** ~1:1 (AR; no sex predilection reported). **Age distribution:** predominantly infants/children; milder cases into adolescence–adulthood.
- **Genetic anticipation / germline mosaicism:** not applicable / not reported.

---

## 10. Diagnostics

**Laboratory (biochemical):**
- **Urine organic acids (GC/MS):** persistently elevated **3-methylglutaconic acid and 3-methylglutaric acid** (defining) — LOINC organic acids panel.
- **Plasma:** elevated **lactate** and **alanine** (variable); crisis: **hyperammonemia, hypoglycemia**, metabolic acidosis. "elevated urinary 3-metilglutaconic and 3-metilglutaric acids, high lactate and alanine in serum" (PMID 37711114). Note lactate/OXPHOS can be **normal** in some (PMID 25051967).
- **Disease-specific cell biomarkers (fibroblasts):** increased **PG34:1/PG36:1** ratio; abnormal **filipin staining** (free cholesterol) (PMID 22683713, PMID 28916646).

**Imaging:** brain **MRI** is central — staged **basal-ganglia/putaminal pattern** with the **pathognomonic dorsal-putaminal "eye"** enabling pattern-recognition diagnosis (PMID 25642805); generalized atrophy in older/advanced disease.

**Biopsy/pathology:** liver — hepatocytes with granular cytoplasm and fine intracytoplasmic lipid droplets; ultrastructure with **abnormal circular mitochondrial cristae** (PMID 35781780). Muscle respiratory-chain findings variable.

**Genetic testing (confirmatory):** identify **biallelic pathogenic *SERAC1* variants**. Recommended approach: **WES or WGS** (most reported diagnoses), gene panels (mitochondrial/3-MGA-uria/leukodystrophy panels including *SERAC1*), single-gene sequencing when phenotype is classic, and **CMA/CNV/deletion analysis** to detect intragenic deletions (e.g., exon 2–4 deletion). mtDNA testing may show secondary depletion in liver in some (PMID 23918762). "Diagnosis is confirmed when biallelic pathogenic variants in SERAC1 gene are found" (PMID 37711114).

**Clinical criteria / differential diagnosis:** no formal consensus criteria; diagnosis rests on the biochemical + MRI + genetic triad. **Differential:** other Leigh/Leigh-like syndromes and primary mitochondrial disorders; other 3-methylglutaconic acidurias — primary (AUH/3-methylglutaconyl-CoA hydratase deficiency), Barth syndrome (*TAZ*), *TMEM70*, *ATAD3A*, *OPA3* (Costeff), *DNAJC19* (DCMA), *CLPB*, and **HTRA2 defect** (neonatal movement disorder + epilepsy + 3-MGA-uria, PMID 30114719); neonatal acute liver failure/urea cycle defects (hyperammonemia); dystonia–deafness syndromes; complicated hereditary spastic paraplegias (milder SERAC1 phenotype). Distinguishing feature: **putaminal "eye" MRI sign** + PG34:1/PG36:1 + *SERAC1* genetics.

**Screening:** not on standard newborn-screening panels (3-MGA is not a routine NBS analyte). **Cascade/carrier testing** of relatives once the familial variants are known; **prenatal/preimplantation genetic testing** feasible for known biallelic variants.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** generally **poor with early death** in classic severe disease; neonatal multiorgan failure can be lethal within days (PMID 34751152, PMID 38445077). "Treatment is supportive, and the outcome is usually poor with early death, except for the juvenile-onset type" (PMID 32684373). No formal 5-/10-year survival statistics exist.
- **Morbidity/disability:** severe, lifelong — deafness, dystonia/spasticity, intellectual disability, epilepsy, feeding difficulty; most severely affected are non-ambulatory/non-verbal.
- **Complications:** recurrent metabolic crises, aspiration/respiratory infections, liver failure, feeding failure, status dystonicus, epilepsy.
- **Recovery potential:** limited in severe cases; milder (hypomorphic) patients may stabilize or improve (PMID 35781780; PMID 28916646).
- **Prognostic factors:** **genotype** (complete LoF → severe/early death; hypomorphic missense/splice → milder, later-onset, better survival), **age/severity of neonatal crisis**, degree of hepatic and neurological involvement. Biochemical/lipid markers (3-MGA, PG34:1/PG36:1) confirm diagnosis but are not validated quantitative prognostic biomarkers.

---

## 12. Treatment

**No disease-modifying or curative therapy exists; management is supportive, symptomatic, and multidisciplinary** (NCIT:C15277 Supportive Care).

- **Acute metabolic crisis (neonatal):** treat as suspected inborn error of metabolism — stop protein intake, promote anabolism with IV glucose, correct acidosis; **continuous hemodialysis/CRRT** for severe hyperammonemia (PMID 38445077). (NCIT: Hemodialysis; Intravenous glucose.)
- **Pharmacotherapy (symptomatic):** anticonvulsants for seizures; agents for dystonia/spasticity (e.g., trihexyphenidyl, baclofen, benzodiazepines, botulinum toxin) — no MEGDEL-specific efficacy data; "mitochondrial cocktail" supplements (coenzyme Q10, riboflavin, thiamine, L-carnitine) are commonly used empirically without proven benefit.
- **Sensorineural deafness:** hearing amplification and **cochlear implantation** (PMID 39592976). (NCIT: Cochlear Implantation.)
- **Nutrition/GI:** feeding support, gastrostomy for failure to thrive/dysphagia.
- **Rehabilitation:** physiotherapy, occupational and speech/communication therapy; orthopedic management of scoliosis/contractures.
- **Anaesthetic considerations (mitochondrial disease):** avoid triggering agents; **dexmedetomidine** (± ketamine) used as a non-triggering approach for sedation/anesthesia (PMID 39592976). Caution with prolonged fasting, propofol infusion, and mitochondrial-toxic drugs.
- **Advanced/experimental therapeutics:** **no** approved gene, cell, RNA, or targeted therapies; **no** MEGDEL-specific clinical trials (no NCT identifiers). Gene-replacement is a theoretical future avenue (recessive LoF, defined single gene).
- **Pharmacogenomics:** not applicable beyond general mitochondrial-drug avoidance (e.g., valproate hepatotoxicity risk, aminoglycoside ototoxicity caution).

**Treatment strategy:** genotype/phenotype-guided supportive algorithm — neonatal metabolic stabilization → long-term multidisciplinary care (neurology, metabolic, audiology/ENT, hepatology, rehabilitation, palliative). Personalized medicine currently limited to genetic counseling and prognostication by genotype.

---

## 13. Prevention

- **Primary prevention:** not possible for a congenital genetic disease; risk reduction via **genetic counseling** in consanguineous/carrier families and reproductive options (**carrier testing, prenatal diagnosis, preimplantation genetic testing** for known familial variants).
- **Secondary prevention:** early recognition of the neonatal metabolic/hepatic crisis and prompt metabolic management; early diagnosis via MRI pattern + organic acids + *SERAC1* testing to enable supportive interventions and family counseling.
- **Tertiary prevention:** prevent complications — avoid fasting/mitochondrial-toxic drugs, treat infections promptly, manage seizures/dystonia, cochlear implantation for deafness, nutritional support, physiotherapy to limit contractures.
- **Immunization / public-health / environmental interventions:** routine childhood vaccination to prevent infection-triggered crises; no vector/sanitation measures applicable.
- **Counseling:** AR recurrence risk 25% for future offspring of carrier couples; cascade testing of relatives (NSGC/ACMG guidance).
- **Screening:** not part of population newborn screening; targeted testing in at-risk families.

---

## 14. Other Species / Natural Disease

- **Naturally occurring animal disease:** **Canine Multiple System Degeneration (CMSD)** — an early-onset, progressive, autosomal-recessive movement disorder of **Kerry Blue Terriers** and **Chinese Crested dogs** with degeneration of the **cerebellum, caudate nucleus, and substantia nigra**, caused by a homozygous nonsense variant in the **SERAC1 ortholog** (canine chromosome 1) (PMID 39596578).
  - "Canine multiple system degeneration (CMSD) is an early onset, progressive movement disorder affecting Kerry Blue Terriers and Chinese Crested dogs. The associated pathologic lesions include degeneration of the cerebellum, caudate nucleus, and substantia nigra" (PMID 39596578).
- **Taxonomy:** *Canis lupus familiaris* (NCBI:txid9615). **Breeds (VBO):** Kerry Blue Terrier, Chinese Crested.
- **Orthologous gene:** canine *SERAC1* (NCBI Gene ortholog). Human *SERAC1* NCBI Gene 84947.
- **Comparative biology / conservation:** the shared caudate (basal-ganglia) degeneration and movement-disorder phenotype from *SERAC1* loss demonstrates **evolutionary conservation** of the disease mechanism; recognized in **OMIA**.
- **Veterinary relevance:** important heritable neurodegenerative disease in these breeds; carrier testing relevant to breeding programs.
- **Zoonotic potential:** none (genetic disease).

---

## 15. Model Organisms

- **In-vitro / cellular models (principal):** **patient-derived fibroblasts** (lipidomics, filipin, mitochondrial network/Ca²⁺ studies; PMID 22683713, PMID 34751152); **lentiviral WT-SERAC1 complementation** rescuing the PG34:1/PG36:1 ratio (PMID 22683713); **COS-1 transfection** for localization of mutant vs WT protein (PMID 34751152); an engineered cellular model probing SERAC1 in a **mitochondrial serine-transporter complex / mtDNA maintenance** (PMID 35235340).
- **Naturally occurring mammalian model:** canine CMSD (Kerry Blue Terrier, Chinese Crested) — SERAC1-ortholog nonsense variant (PMID 39596578); a spontaneous large-animal model of SERAC1 neurodegeneration.
- **Genetically engineered rodent (mouse) models:** no well-characterized published *Serac1* knockout mouse recapitulating MEGDEL was identified in this review (a notable gap; consult MGI/IMPC for current alleles).
- **Phenotype recapitulation:** cellular models faithfully reproduce the **biochemical/lipid and mitochondrial-structural** phenotype; the canine model reproduces the **basal-ganglia movement-disorder/neurodegeneration**. **Limitations:** cellular models cannot capture organ-level (deafness, hepatopathy) or developmental features; the canine model's full biochemical concordance (3-MGA-uria, deafness, hepatopathy) is not fully documented.
- **Applications:** studying phospholipid remodeling, ER–mitochondria contact biology, cholesterol trafficking, and testing candidate therapeutics.
- **Resources:** Cellosaurus (patient fibroblast lines), OMIA (canine CMSD), MGI/IMPC (for any mouse alleles), Alliance of Genome Resources.

---

## Supported vs. Refuted Hypotheses

**Supported (evidence-backed):**
- *SERAC1* biallelic LoF is the cause of MEGDEL/MEGDHEL (PMID 22683713).
- Core mechanism = defective phosphatidylglycerol→cardiolipin remodeling at the MAM, with cholesterol-trafficking defect and secondary OXPHOS failure (PMID 22683713, PMID 34751152).
- MEGDEL is a **secondary** 3-MGA-uria (phospholipid remodeling), grouped with Barth syndrome (PMID 23296368).
- Pathognomonic "putaminal eye" MRI sign; staged basal-ganglia disease (PMID 25642805).
- Infantile hepatopathy is a cardinal feature (MEGDHEL) (PMID 23918762).
- Genotype–phenotype gradient: LoF → severe infantile MEGDHEL; hypomorphic → juvenile cHSP/adult dystonia (PMID 28916646, PMID 35223715, PMID 37711114).
- Naturally occurring canine SERAC1 model (PMID 39596578).

**Refuted / not supported:**
- MEGDEL is **not** a primary defect of leucine catabolism (that is AUH/3-MGA type I) — the 3-MGA-uria here is secondary (PMID 23296368).
- 3-MGA-uria/lactate elevation is **not obligate in muscle OXPHOS assays** — respiratory-chain activity can be normal, so a negative muscle biopsy does not exclude the diagnosis (PMID 25051967).
- No environmental/infectious primary etiology; catabolic stress is a trigger, not a cause.

## Limitations and Future Directions
- No large registry/natural-history cohort with quantitative phenotype frequencies was available; percentages here are qualitative from aggregated case reports (~100 patients).
- Precise prevalence/incidence, carrier frequency, and survival statistics are undefined.
- A robust *Serac1* mouse model and disease-modifying therapy (e.g., gene replacement, lipid-targeted therapy) are key gaps.
- Standardized diagnostic criteria and validated prognostic/QoL measures are lacking.

## Key References (PMIDs)
22683713 (gene discovery/mechanism); 23296368 (3-MGA classification); 25642805 (MRI "eye", OMIM #614739); 23918762 (MEGDHEL/hepatopathy); 34751152 (ER–mito contact, Ca²⁺, OXPHOS); 35235340 (mtDNA maintenance); 35781780 (liver histology); 38445077 (neonatal ALF/hyperammonemia); 27186703, 24997715, 25051967 (phenotype/variants); 35943861, 33613893, 38559521 (variants/consanguinity); 28916646, 35223715, 37711114 (milder/cHSP spectrum); 39592976 (anesthesia/cochlear implant); 39596578 (canine model); 30114719 (HTRA2 differential); 32684373 (review).


## Artifacts

- [OpenScientist final report](3-methylglutaconic_Aciduria_With_Deafness_Encephalopathy_And_Leigh-like_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](3-methylglutaconic_Aciduria_With_Deafness_Encephalopathy_And_Leigh-like_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 14 |
| Quoted claims found in source | 12 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 22 |
| On topic | 21 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:39592976` *(abstract only)*: "This disorder is caused by biallelic mutations in serine active site-containing protein 1 (SERAC1) gene. When these patients experience hepatopathy (H)…the syndrome is referred to as MEGD(H)EL"
  - closest text in source: "This disorder is caused by biallelic mutations in serine active site-containing protein 1 (SERAC1) gene"
- `PMID:35943861` *(abstract only)*: "Both mutations were found to lead to decreased or absent expression of SERAC1"
  - closest text in source: "Mutations in SERAC1 gene encoding a serine active site containing 1 protein were described in patients affected by this syndrome"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 55 |
| Resolved | 53 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 28 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 13 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0003535` (1 mention) - the report calls it "Lab"; HP calls it **3-Methylglutaconic aciduria**
- `HP:0000407` (1 mention) - the report calls it "Sign"; HP calls it **Sensorineural hearing impairment**
- `HP:0001332` (1 mention) - the report calls it "Sign"; HP calls it **Dystonia**
- `HP:0001252` (1 mention) - the report calls it "Sign"; HP calls it **Hypotonia**
- `HP:0001987` (1 mention) - the report calls it "Lab"; HP calls it **Hyperammonemia**
- `HP:0001943` (1 mention) - the report calls it "Lab"; HP calls it **Hypoglycemia**
- `HP:0000252` (1 mention) - the report calls it "Sign"; HP calls it **Microcephaly**
- `HP:0000648` (1 mention) - the report calls it "Sign"; HP calls it **Optic atrophy**
- `HP:0001999` (1 mention) - the report calls it "Sign"; HP calls it **Abnormal facial shape**
- `HP:0001249` (1 mention) - the report calls it "Sign"; HP calls it **Intellectual disability**
- `HP:0002650` (1 mention) - the report calls it "Sign"; HP calls it **Scoliosis**
- `CL:0000540` (1 mention) - the report calls it "neuron; medium spiny/striatal neurons"; CL calls it **neuron**
- `CL:0000598` (1 mention) - the report calls it "cochlear hair cell"; CL calls it **pyramidal neuron**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000729` (1 mention) - the report calls it "Behavioral"; HP calls it **Autistic behavior**
- `GO:0006655` (2 mentions) - the report calls it "phosphatidylglycerol biosynthetic process", "phosphatidylglycerol biosynthesis"; GO calls it **phosphatidylglycerol biosynthetic process**, and lists "phosphatidylglycerol biosynthesis" among its other names
- `GO:0044233` (3 mentions) - the report calls it "mitochondria-associated ER membrane"; GO calls it **mitochondria-associated endoplasmic reticulum membrane contact site**, and lists "mitochondria-associated ER membrane" among its other names
- `GO:0006874` (1 mention) - the report calls it "cellular Ca²⁺ homeostasis"; GO calls it **intracellular calcium ion homeostasis**, and lists "cellular calcium ion homeostasis" among its other names
- `HP:0003577` (1 mention) - the report calls it "Congenital onset for some features"; HP calls it **Congenital onset**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0006655` - called "phosphatidylglycerol biosynthetic process", "phosphatidylglycerol biosynthesis"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.