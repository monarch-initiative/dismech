---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T10:38:07.473806'
end_time: '2026-10-30T10:52:25.268533'
duration_seconds: 857.79
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Pseudohypoaldosteronism Type IB3 Autosomal Recessive
  mondo_id: MONDO:0859318
  category: Mendelian
  causal_genes: SCNN1G
  omim_id: OMIM:620126
  synonyms: not recorded
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
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 25
  on_topic: 16
  validator_version: 0.4.0
term_validation:
  total_terms: 50
  verified: 47
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 28
  labels_matching: 9
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: HP:0002902
    reported_labels:
    - Lab abnormality
    ontology_label: Hyponatremia
  - term_id: HP:0002153
    reported_labels:
    - Lab abnormality
    ontology_label: Hyperkalemia
  - term_id: HP:0001942
    reported_labels:
    - Lab abnormality
    ontology_label: Metabolic acidosis
  - term_id: HP:0000859
    reported_labels:
    - Lab abnormality
    ontology_label: Increased circulating aldosterone concentration
  - term_id: HP:0001944
    reported_labels:
    - Clinical sign
    ontology_label: Dehydration
  - term_id: HP:0002013
    reported_labels:
    - Symptom
    ontology_label: Vomiting
  - term_id: HP:0001254
    reported_labels:
    - Symptom
    ontology_label: Lethargy
  - term_id: HP:0002028
    reported_labels:
    - Clinical sign
    ontology_label: Chronic diarrhea
  - term_id: NCIT:C83164
    reported_labels:
    - sodium chloride
    ontology_label: Birth Year
  labels_variant: 10
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
  path: Pseudohypoaldosteronism_Type_IB3_Autosomal_Recessive-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Pseudohypoaldosteronism_Type_IB3_Autosomal_Recessive-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pseudohypoaldosteronism Type IB3 Autosomal Recessive
- **MONDO ID:** MONDO:0859318 (if available)
- **Causal gene(s):** SCNN1G
- **OMIM:** OMIM:620126
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Pseudohypoaldosteronism Type IB3 Autosomal Recessive** covering all of the
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

# Pseudohypoaldosteronism Type IB3, Autosomal Recessive (PHA1B3)
### Comprehensive Disease Characterization Report

**MONDO:** MONDO:0859318 · **OMIM:** 620126 · **Causal gene:** **SCNN1G** (HGNC:10601; γ-subunit of the epithelial sodium channel, ENaC) · **Category:** Mendelian, autosomal recessive

---

## Summary (Answer to the Research Question)

Pseudohypoaldosteronism type IB3, autosomal recessive (**PHA1B3**, OMIM 620126) is the subtype of **systemic (generalized) pseudohypoaldosteronism type 1 caused by biallelic loss-of-function variants in *SCNN1G***, the gene encoding the **γ (gamma) subunit of the amiloride-sensitive epithelial sodium channel (ENaC)**. ENaC is a heterotrimer of α (SCNN1A), β (SCNN1B) and γ (SCNN1G) subunits that reabsorbs Na⁺ across the apical membrane of tight epithelia (distal nephron, distal colon, sweat and salivary gland ducts, and airway). When the γ-subunit is non-functional, aldosterone cannot drive Na⁺ reabsorption — producing **target-organ aldosterone resistance** despite very high circulating aldosterone. PHA1B3 is one of three genetically distinct systemic PHA1B subtypes: **PHA1B1 (SCNN1A, OMIM 264350), PHA1B2 (SCNN1B, OMIM 620125), PHA1B3 (SCNN1G, OMIM 620126)**. It manifests in the **neonatal period** with life-threatening salt-wasting crises: **hyponatremia, hyperkalemia, and metabolic acidosis with markedly elevated plasma renin and aldosterone**. Unlike the milder renal/autosomal-dominant form (PHA1A, *NR3C2*), the systemic form affects multiple organs, does not remit with age, and requires lifelong therapy with high-dose sodium supplementation and potassium-lowering measures.

> ⚠️ **Gene-identity check:** The serial-number name "type IB3" does *not* itself name the gene. The MONDO/OMIM identifiers above specify the **SCNN1G** γ-ENaC subtype. Do not confuse with PHA1A (*NR3C2*, renal/dominant), PHA1B1 (*SCNN1A*), PHA1B2 (*SCNN1B*), or PHA2/Gordon syndrome (*WNK1/WNK4/KLHL3/CUL3*). Note also the **allelic mirror-image** disease: *gain*-of-function *SCNN1G* variants cause **Liddle syndrome** (hypertension, hypokalemia), OMIM 177200.

---

## 1. Disease Information

- **What it is:** A rare hereditary channelopathy of **aldosterone resistance** (pseudohypoaldosteronism) in its **severe systemic form**, caused by defective ENaC. "Pseudo"-hypoaldosteronism because aldosterone levels are normal/high but its downstream effect (ENaC-mediated Na⁺ reabsorption) is absent. PMID 42549990: *"Pseudohypoaldosteronism type 1 (PHA1) is a rare hereditary disorder characterised by aldosterone resistance leading to salt wasting, hyperkalaemia, and metabolic acidosis… a severe systemic form (PHA1B) caused by biallelic mutations in epithelial sodium channel (ENaC) subunit genes."*
- **Key identifiers:**
  - OMIM: **620126** (Pseudohypoaldosteronism, type IB3, autosomal recessive)
  - MONDO: **MONDO:0859318**
  - Gene: **SCNN1G** (HGNC:10601; NCBI Gene 6340; Ensembl ENSG00000166828; UniProt P51170), chromosome **16p12.2**
  - Orphanet: PHA type 1 (ORPHA:171876 generalized/systemic PHA1; parent ORPHA:171871 for PHA1)
  - ICD-10: **E27.4** (other and unspecified adrenocortical insufficiency; PHA has no dedicated ICD-10 code); ICD-11: **5A71.Z**/5A7Y adrenal-related; often coded under disorders of mineralocorticoid action
  - MeSH: **D011546** "Pseudohypoaldosteronism"
- **Synonyms / alternative names:** Systemic pseudohypoaldosteronism type 1; generalized PHA1; multiple-target-organ defect PHA1; autosomal recessive PHA type 1 (γ-ENaC type); PHA1B3; gamma-ENaC–related systemic PHA.
- **Information source type:** Derived chiefly from **disease-level aggregated resources** (OMIM, Orphanet) and **individual-patient case reports/small case series** (ultra-rare disease; no large EHR cohorts).

---

## 2. Etiology

- **Primary cause — genetic:** Biallelic (homozygous or compound-heterozygous) **loss-of-function variants in *SCNN1G***. Inheritance is **autosomal recessive**. This is a monogenic Mendelian disease; there are **no infectious or acquired primary causes** of this specific (inherited) subtype. (A phenotypically similar but genetically distinct entity, *secondary/transient PHA*, is acquired — see §10 differentials.)
- **Genetic risk factors:**
  - Causal variants: biallelic *SCNN1G* null/hypomorphic alleles (see §4).
  - **Parental consanguinity** is a major risk factor (homozygosity for founder/private alleles). PMID 42549990: *"parental consanguinity was present in seven (78%)."* PMID 33690157: *"All parents were consanguineous and of South Asian, Middle Eastern or African ethnic origin."*
  - Family history of an affected sib (25% recurrence risk per pregnancy).
- **Environmental risk factors:** None cause the disease. However, **salt loss, intercurrent illness, vomiting/diarrhea, heat, and poor sodium intake** precipitate or worsen salt-wasting crises in genetically affected individuals (gene–environment interaction: dietary sodium availability modulates crisis frequency). Mouse data directly demonstrate diet dependence — a high-Na/low-K "rescue diet" normalizes the phenotype and reverting to regular diet reinstates severe disease (PMID 26701978).
- **Protective factors:** No genetic protective alleles described. **Aggressive dietary sodium supplementation** and potassium restriction are protective against crises (environmental/therapeutic). Residual ENaC function from hypomorphic missense alleles is "protective" relative to null alleles (milder disease; see §4/§9).
- **Gene–environment interaction:** Dietary Na⁺/K⁺ intake is the dominant modifiable factor interacting with the fixed genetic defect to set clinical severity and crisis risk.

---

## 3. Phenotypes

Onset is **neonatal** (congenital functional defect); presentation typically within the first **2 weeks of life** (median ~14 days; PMID 42549990, 33690157). Severity is usually **severe** in the classic systemic form; **variable/milder** with partial-function alleles. Course is **episodic/crisis-prone on a chronic lifelong baseline** (systemic form does not remit).

| Phenotype | Type | HPO term | Onset / severity / frequency |
|---|---|---|---|
| Hyponatremia | Lab abnormality | **HP:0002902** | Neonatal; severe (median Na⁺ 124 mEq/L); ~100% |
| Hyperkalemia | Lab abnormality | **HP:0002153** | Neonatal; severe/life-threatening (median K⁺ 8.0 mEq/L); ~100% |
| Metabolic acidosis (hyperchloremic) | Lab abnormality | **HP:0001942** | Neonatal; moderate–severe; very frequent |
| Elevated plasma renin activity | Lab abnormality | **HP:0000848** (hyperaldosteronism); renin ↑ | ~100% |
| Hyperaldosteronism (secondary) | Lab abnormality | **HP:0000859** | ~100% |
| Salt wasting / renal sodium wasting | Clinical sign | **HP:0000127**/**HP:0012605** (natriuria) | ~100% |
| Dehydration / hypovolemia | Clinical sign | **HP:0001944** | Frequent during crises |
| Vomiting | Symptom | **HP:0002013** | Common presenting symptom |
| Failure to thrive / poor feeding / weight loss | Clinical sign | **HP:0001508** / **HP:0011471** | Common |
| Lethargy | Symptom | **HP:0001254** | Common at presentation |
| Cardiac arrhythmia / cardiac arrest (hyperkalemic) | Clinical sign | **HP:0011675** / **HP:0001695** | Life-threatening; drives mortality |
| Skin lesions (miliaria rubra–like, eczematous/seborrheic, folliculitis, generalized rash) | Physical manifestation | **HP:0011123** (inflammatory abnormality of the skin) / **HP:0000964** (eczema) | Occur during salt-depletion crises (PMID 3654220, 41275343) |
| Elevated sweat chloride / salivary sodium | Lab abnormality | **HP:0012236** (↑ sweat chloride) | Characteristic; CF-like |
| Recurrent respiratory symptoms / lower-airway disease | Clinical sign | **HP:0002783** (recurrent LRTI) | Reported; airway ENaC involvement |
| Intestinal salt wasting (diarrhea) | Clinical sign | **HP:0002028** | Reported (PMID 40398899) |

- **Quality-of-life impact:** High treatment burden (frequent oral medication/dose titration, salt supplements, resins, repeated electrolyte monitoring, risk of acute crises). PMID 42569709: *"This condition requires a lifelong close follow-up and treatment process."* Survivors with good control can achieve normal physical/neurological development and even pregnancy (PMID 33690157). No formal EQ-5D/SF-36 data for this ultra-rare disease.

---

## 4. Genetic / Molecular Information

- **Causal gene:** **SCNN1G** (sodium channel epithelial 1 gamma subunit), **chromosome 16p12.2** (historically mapped 16p12.2–13.11 alongside *SCNN1B*). HGNC:10601; OMIM gene *600761*; disease OMIM 620126. Encodes **γ-ENaC** (~649 aa; UniProt P51170).
- **Pathogenic variants (germline; this disease has no somatic basis):**
  - **Variant classes:** splice-site, nonsense, framesh4ift (frameshift), missense, and **large/gross deletions** — all converging on loss of function. Landmark: PMID 8640238 — SCNN1G **3′ splice-site 318-1 G→A**, truncating γ-ENaC from 649→134 aa. Recent: first homozygous **gross deletion** in a PHA1 ENaC gene (PMID 41275343); novel homozygous *SCNN1G* variants across case series (PMID 42549990).
  - **Classification:** per ACMG/AMP — pathogenic/likely pathogenic for null alleles; some novel variants remain VUS pending functional/segregation data (PMID 42549990).
  - **Allele frequency:** Pathogenic alleles are extremely rare in gnomAD (private/founder); loss-of-function constraint for SCNN1G is modest (recessive gene).
  - **Functional consequence:** **Loss of function** — reduced channel number and/or **reduced open probability**. Example: γ-ENaC **A635V** (c.1904C>T) reduced amiloride-sensitive current **~30%** with lower open probability (PMID 40153144); **G532S** → mild PHA-1B3 (PMID 40969802).
- **Modifier genes:** The other ENaC subunits (**SCNN1A, SCNN1B**) and regulators (NEDD4L, SGK1, CAP serine proteases, kallikrein-1) plausibly modify residual channel activity; co-expression/digenic contributions have been proposed in a network-medicine analysis (PMID 41569463). No validated clinical modifier locus specific to PHA1B3.
- **Epigenetic information:** No disease-specific DNA-methylation/histone data reported for PHA1B3. (Aldosterone/MR signaling epigenetically regulates ENaC transcription physiologically, but this is not altered as the primary lesion.)
- **Chromosomal abnormalities:** Point mutations and intragenic deletions predominate; a homozygous **gross (multi-exon) deletion** of an ENaC gene has been reported (PMID 41275343). No recurrent aneuploidy/translocation.
- **Allelic contrast:** **Gain-of-function** *SCNN1G* (PY-motif loss, e.g., Q591X) → **Liddle syndrome** (PMID 35661050) — demonstrating ENaC activity as the salt-retention↔salt-wasting axis.

**Ontology:** gene product GO:0034765 (regulation of ion transmembrane transport); protein class CHEBI/ion channel; variant effect "loss_of_function."

---

## 5. Environmental Information

- **Environmental/toxic/occupational factors:** None cause PHA1B3 (purely genetic). 
- **Lifestyle/dietary factors:** **Dietary sodium and potassium intake** are the key modifiable determinants of crisis frequency and severity (see §2 gene–environment interaction). Heat exposure → sweat Na⁺ loss can precipitate crises (sweat gland ENaC defect).
- **Infectious agents:** Not causal. Intercurrent infections (and, for the acquired mimic, **urinary tract infection/obstruction** in *secondary* PHA) can precipitate salt-wasting episodes but are not the cause of the inherited disease.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function variant in *SCNN1G*** → produces a **non-functional or hypomorphic γ-ENaC subunit** (truncation, misassembly, or reduced open probability). *(Demonstrated: in-vitro electrophysiology, PMID 40153144.)*
2. Defective γ-subunit → **impaired assembly/proteolytic activation of the αβγ-ENaC heterotrimer** at the apical membrane (γ-ENaC GRIP-domain cleavage is required to relieve autoinhibition and open the channel). *(Demonstrated mechanism of ENaC gating, PMID 42463047.)*
3. Non-functional ENaC → **loss of amiloride-sensitive apical Na⁺ reabsorption** in principal/epithelial cells of ENaC-expressing tissues. *(Demonstrated.)*
4. In the **distal nephron (connecting tubule/collecting duct)** → reduced Na⁺ reabsorption → **renal salt wasting → hyponatremia and hypovolemia**. Loss of the lumen-negative transepithelial potential → **reduced K⁺ and H⁺ secretion → hyperkalemia and metabolic acidosis**. *(Demonstrated; mirrored in conditional αENaC-KO mice, PMID 26701978.)*
5. Hypovolemia + hyperkalemia → **marked activation of renin–angiotensin–aldosterone system** → **very high plasma renin and aldosterone**, which **cannot act** because the effector channel is defective ("pseudo"-hypoaldosteronism). *(Demonstrated.)*
   - **Branch A (kidney/colon):** ongoing Na⁺ wasting via gut (intestinal salt wasting/diarrhea) compounds hyponatremia.
   - **Branch B (sweat/salivary glands):** failure of ductal Na⁺ reabsorption → **elevated sweat/saliva Na⁺/Cl⁻** (CF-like); hypertonic sweat → **sweat-gland inflammation and skin lesions** (miliaria-like, eczematous). *(Demonstrated histologically, PMID 3654220.)*
   - **Branch C (airway):** loss of ENaC-mediated airway surface liquid absorption → impaired mucus clearance / fluid handling → **recurrent respiratory symptoms**; neonatally, failure to clear fetal lung liquid is lethal in constitutive KO mice (PMID 9326675) — an *inferred* contributor to neonatal respiratory vulnerability in humans.
6. **Severe hyponatremia + hyperkalemia** → **cardiac arrhythmia/arrest, dehydration, shock** → **neonatal death or hypoxic-ischemic neurological injury** if untreated. *(Demonstrated clinically, PMID 33690157.)*

### Supporting detail
- **Molecular pathways:** Aldosterone–mineralocorticoid-receptor → ENaC Na⁺ transport pathway (Reactome R-HSA-1799339 "ENaC"; KEGG "aldosterone-regulated sodium reabsorption" hsa04960). Proteolytic activation by furin/CAPs/kallikrein-1 (PMID 42463047, 41671061).
- **Protein dysfunction:** Loss-of-function of a trimeric ion channel; cryo-EM structure of human αβγ-ENaC available (PMID 30251954) supports structural interpretation of variants.
- **Cellular processes:** Defective transepithelial Na⁺ transport; secondary sweat-gland inflammation (destructive inflammatory reaction, PMID 3654220).
- **Biochemical abnormality:** Ion-channel defect (not an enzyme deficiency) → electrolyte/acid-base derangement.
- **Immune/metabolic/epigenetic:** No primary autoimmune or metabolic component; skin inflammation is secondary to hypertonic sweat.
- **Molecular profiling:** No disease-specific transcriptomic/proteomic/metabolomic datasets; a systems-medicine interactome highlights sodium-ion-transport and aldosterone-regulated reabsorption processes (PMID 41569463).

**Ontology:** GO:0006814 (sodium ion transport), GO:0035725 (sodium ion transmembrane transport), GO:0050891 (multicellular organismal water homeostasis), GO:0003051 (angiotensin-mediated regulation of ECF volume); CL:1000714 (kidney collecting duct principal cell), CL:1000454 (kidney collecting duct epithelial cell), CL:0002254 (epithelial cell of distal tubule), CL:0000078 (epithelial cell of sweat gland duct / CL:1000296), CL:0002633 (respiratory epithelial cell).

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** **Kidney** (distal nephron: connecting tubule, cortical/medullary collecting duct) — UBERON:0001232 (collecting duct), UBERON:0004135 (connecting tubule). **Distal colon** (UBERON:0001157). **Sweat glands** (UBERON:0001820) and **salivary glands** (UBERON:0001044). **Lung/airway** (UBERON:0001005 respiratory airway; UBERON:0002186 bronchiole).
- **Secondary/complication organs:** **Heart** (hyperkalemic arrhythmia; UBERON:0000948), **brain** (hypoxic-ischemic injury post-arrest; UBERON:0000955), **skin** (UBERON:0002097) with sweat-gland inflammation.
- **Body systems:** Endocrine (mineralocorticoid signaling), renal/urinary, gastrointestinal, integumentary, respiratory; cardiovascular and nervous secondarily.
- **Tissue/cell level:** **Epithelial tissue** — Na⁺-reabsorbing **principal cells** of the collecting duct, distal colonic enterocytes, sweat/salivary **duct epithelial cells**, airway epithelial cells. CL terms as in §6.
- **Subcellular level:** **Apical plasma membrane** (GO:0016324) — ENaC resides on the apical membrane of multiciliated/epithelial cells (and in cilia; PMID 26772908); trafficking involves ER/Golgi (furin cleavage) and membrane recycling (NEDD4L/ubiquitin). GO CC: GO:0016324 (apical plasma membrane), GO:0034707 (chloride channel complex – N/A), GO:0005886 (plasma membrane).
- **Localization/lateralization:** Systemic and **bilateral/symmetric** (both kidneys, generalized skin/gland involvement).

---

## 8. Temporal Development

- **Onset:** **Congenital/neonatal**, typically **acute** salt-wasting crisis in the first days–2 weeks of life (median ~14 days; PMID 42549990). Milder hypomorphic alleles may present later or more insidiously (PMID 40153144).
- **Progression:** No formal staging. Natural history = **chronic lifelong** disease with **recurrent episodic crises** superimposed on a persistent requirement for sodium/potassium management. The most dangerous window is the **neonatal/infantile period** (highest mortality). Symptoms/medication needs often **ease but do not disappear with age** (PMID 41569463: *"symptoms tend to improve with age"*) — in contrast to renal PHA1A, which can remit in childhood.
- **Patterns:** No spontaneous remission in the systemic form; "improvement" reflects maturation of compensatory mechanisms and better tolerance, not cure. **Critical period / window of opportunity:** rapid neonatal recognition and correction of hyperkalemia/hyponatremia is life-saving (PMID 42569709).

---

## 9. Inheritance and Population

- **Epidemiology:** **Ultra-rare.** Orphanet classifies PHA type 1 as a rare disease (point prevalence <1/1,000,000); the **systemic (ENaC) form is rarer than the renal (NR3C2) form**, and PHA1B3 (*SCNN1G*) is one of three systemic subtypes. Precise incidence/prevalence figures are unavailable; data come from case reports/small series. Neonatal hyponatremia series find genetic hypo-/pseudo-hypoaldosteronism in a few percent of referred cases (PMID 31300884).
- **Inheritance:** **Autosomal recessive.** 25% recurrence risk for sibs of an affected child.
- **Penetrance / expressivity:** Essentially **complete penetrance** of the biochemical phenotype with biallelic null alleles; **variable expressivity** with partial-function alleles (§4).
- **Anticipation / mosaicism:** Not applicable (not a repeat disorder; no reported germline mosaicism relevant to AR transmission).
- **Founder effects:** Yes — a shared *SCNN1G* **318-1 G→A** haplotype in **Indian-subcontinent** families (PMID 8640238).
- **Consanguinity:** Strong driver (78%–100% of reported families; PMID 42549990, 33690157).
- **Carrier frequency:** Not formally established; carriers (parents) are **asymptomatic**.
- **Population demographics:** Higher among **South Asian, Middle Eastern, and African / consanguineous populations** (PMID 33690157). **Sex ratio ≈ 1:1** (autosomal). Age distribution: overwhelmingly **neonates/infants** at diagnosis.

---

## 10. Diagnostics

- **Laboratory (LOINC-codable):** Serum Na⁺ (LOINC 2951-2) ↓, K⁺ (2823-3) ↑, bicarbonate/CO₂ ↓ with hyperchloremic metabolic acidosis; **plasma renin activity** ↑↑ and **serum/plasma aldosterone** ↑↑ (hyperreninemic hyperaldosteronism); inappropriately high **urine sodium**; **elevated sweat chloride** (LOINC 2075-0) and salivary Na⁺. Normal **17-hydroxyprogesterone** (LOINC 1668-3) and **cortisol** help exclude CAH/adrenal insufficiency (PMID 42549990).
- **Biomarkers:** Aldosterone and renin (markedly elevated); sweat/salivary electrolytes; **SCNN1G genotype** is the definitive marker.
- **Imaging:** Non-specific; used to exclude adrenal pathology (adrenal ultrasound) and renal tract anomalies (to exclude secondary PHA from obstruction/reflux).
- **Electrophysiology:** **ECG** for hyperkalemic changes (peaked T waves, widened QRS) — critical acute monitoring. Research: Ussing-chamber/two-electrode voltage clamp confirm reduced amiloride-sensitive current for VUS (PMID 40153144).
- **Biopsy/pathology:** Not required for diagnosis; sweat-gland biopsy historically showed peri-ductal destructive inflammation (PMID 3654220).
- **Genetic testing (definitive):** **Clinical/whole-exome sequencing** or targeted **ENaC/PHA gene panels** covering **SCNN1A, SCNN1B, SCNN1G + NR3C2** (± secondary genes); single-gene or deletion/duplication (CNV/MLPA) analysis for gross deletions (PMID 41275343). PMID 42549990: *"Genetic testing was performed using clinical exome sequencing, and variants were classified according to… (ACMG) guidelines."* Early genetic testing is advocated because PHA1A vs PHA1B cannot be distinguished clinically/biochemically at presentation (PMID 31301676).
- **Clinical criteria:** No formal consensus criteria; diagnosis = neonatal salt wasting + hyperreninemic hyperaldosteronism + ENaC-gene biallelic variants.
- **Differential diagnosis:** salt-wasting **CAH** (21-hydroxylase deficiency — high 17-OHP; PMID 27485500); **aldosterone synthase deficiency** (CYP11B2); **primary adrenal insufficiency / adrenal hypoplasia congenita** (NR0B1); **familial glucocorticoid deficiency** (MC2R); **Bartter syndrome type II** (transient neonatal hyperkalemia then hypokalemic alkalosis; PMID 40630717); **renal PHA1A** (NR3C2, milder/remitting); **secondary/transient PHA** (UTI/obstructive uropathy).
- **Screening:** Not on routine newborn screening. **Cascade/carrier testing** for consanguineous families; prenatal/preimplantation testing possible once the familial variant is known.

---

## 11. Outcome / Prognosis

- **Mortality:** High in the neonatal/infantile period. **25%** mortality (3/12) with **16%** severe neurological impairment post-hyperkalemic cardiac arrest in a UK cohort (PMID 33690157); **67%** (6/9) died in an Indian series with limited resources (PMID 42549990). Deaths are driven by **hyperkalemic cardiac arrest** and crises.
- **Life expectancy / survival:** With early diagnosis and intensive lifelong management, **normal survival and development are achievable**; PMID 33690157: *"survival with normal physical and neurological outcome is possible, justifying intensive management."* One survivor had a **successful pregnancy at age 28**.
- **Morbidity / disability:** Recurrent electrolyte crises, growth faltering, skin disease, respiratory symptoms; neurodevelopmental sequelae mainly from hypoxic-ischemic events during crises.
- **Complications:** Hyperkalemic arrhythmia/arrest, hypovolemic shock, failure to thrive, recurrent infections/respiratory disease, nephrocalcinosis (from therapy) and treatment burden.
- **Prognostic factors:** **Residual ENaC function (allele type)** — null/truncating = severe; hypomorphic missense = milder (§4/§9); speed of neonatal recognition and adequacy of electrolyte control; access to care. No validated molecular prognostic biomarker beyond genotype.

---

## 12. Treatment

**No cure or disease-modifying/gene therapy exists; management is supportive and lifelong.** Mineralocorticoids (fludrocortisone) are **ineffective** because the defect is downstream of the receptor.

- **Acute crisis:** IV normal saline/volume resuscitation; aggressive **hyperkalemia management** (calcium gluconate for cardioprotection; insulin-glucose, β-agonists to shift K⁺; **cation-exchange resins** to remove K⁺); correction of acidosis with **sodium bicarbonate/citrate**. (NCIT: fluid resuscitation; electrolyte management.)
- **Chronic maintenance (mainstays):**
  - **High-dose oral sodium chloride (salt) supplementation** — CHEBI:26710 (sodium chloride); NCIT:C83164 (sodium chloride). Doses are high and require frequent titration (PMID 42569709).
  - **Sodium bicarbonate / sodium citrate** for metabolic acidosis (CHEBI:32139; NCIT sodium bicarbonate).
  - **Potassium-lowering therapy:** **sodium polystyrene sulfonate** (Kayexalate) or **calcium polystyrene sulfonate** resins, often decanted into feeds for infants (PMID 38288475: *"successfully managed with sodium polystyrene sulfonate decanted into feeds along with sodium supplementation"*). Newer K⁺ binders (patiromer, sodium zirconium cyclosilicate) are options in principle.
  - **Dietary potassium restriction.**
- **Pharmacogenomics:** Not applicable (no genotype-directed drug metabolism issue). Treatment *is* genotype-informed in that systemic (ENaC) disease mandates lifelong therapy vs potential weaning in renal PHA1A.
- **Advanced/experimental therapeutics:** No approved gene/cell/RNA therapy. ENaC biology is an active drug target in the **opposite** direction (ENaC *inhibitors* for cystic fibrosis; PMID 42184559) — not applicable to loss-of-function PHA. No disease-specific clinical trials (no NCT identifiers specific to PHA1B3).
- **Surgical/rehabilitative:** None specific; supportive nutrition/growth support; respiratory care as needed.
- **Treatment strategy:** Early molecular diagnosis → lifelong high-sodium + K⁺-binder regimen with frequent electrolyte-guided dose adjustment; multidisciplinary team (endocrinology, nephrology, dietetics) (PMID 35918792).

---

## 13. Prevention

- **Primary prevention:** Not possible for an inherited monogenic disease. **Genetic counseling** for consanguineous couples and families with an affected child; **carrier testing**, and where desired **prenatal diagnosis / preimplantation genetic testing** once the familial *SCNN1G* variant is known (25% recurrence risk).
- **Secondary prevention (early detection):** High index of suspicion for any neonate with hyponatremia + hyperkalemia + acidosis; **rapid genetic testing** to subtype and guide therapy (PMID 31301676). Not part of standard newborn blood-spot screening.
- **Tertiary prevention (complication avoidance):** Strict electrolyte control, written sick-day/crisis plans, prompt management of intercurrent illness, avoidance of K⁺-raising drugs and excessive heat/sweat losses, regular cardiac (ECG) and growth monitoring.
- **Immunization / public-health / environmental interventions:** Not applicable (non-infectious, non-environmental cause); routine childhood immunization and infection prevention reduce crisis triggers.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** ENaC subunits are conserved across tetrapods (PMID 26772908: four ENaC paralogs in most Sarcopterygii). Human **SCNN1G** orthologs: mouse **Scnn1g** (NCBI Gene 20278; *Mus musculus*, NCBI:txid10090), rat **Scnn1g** (*Rattus norvegicus*, NCBI:txid10116). 
- **Natural disease in animals:** No well-characterized spontaneous *SCNN1G*-PHA described in companion animals (not a recognized OMIA entry for γ-ENaC PHA). Disease knowledge is from **engineered** models, not natural occurrence.
- **Comparative biology:** ENaC's dual role in renal salt handling and airway/lung-liquid clearance is conserved; mouse knockouts reveal the lung-liquid role that is harder to observe clinically in humans. Evolutionary conservation of the αβγ architecture underpins model validity.
- **Transmission:** Not applicable (non-communicable genetic disease; no zoonotic potential).

---

## 15. Model Organisms

- **Mouse (primary model; *Mus musculus*, MGI):**
  - **Constitutive αENaC (Scnn1a) knockout** — neonatal lethal from **failure to clear fetal lung liquid** (PMID 9326675): *"inactivation of alphaENaC results in failure to clear fetal lung liquid at birth and in early neonatal death."*
  - **Transgenically rescued αENaC⁻/⁻Tg** — reproduces **systemic PHA-1**: *"alphaENaC(−/−)Tg mice showed clinical features of severe PHA-1 with metabolic acidosis, urinary salt-wasting, growth retardation, and 50% mortality"*; adults show **compensated PHA-1 with 6-fold elevated aldosterone** (PMID 9326675). This is the classic **mouse model for PHA-1**.
  - **Conditional, adult nephron-specific αENaC knockout (Scnn1a^Pax8/LC1)** — hyperkalemia and weight loss on normal diet, **rescued by high-Na/low-K diet**, *"thus mimicking PHA-1"* (PMID 26701978) — isolates the renal phenotype and demonstrates diet dependence.
  - **αENaC-deficient (rescued) mice** — impaired respiratory Na⁺ transport predisposing to **pulmonary oedema** (PMID 15308680) — models the airway dimension.
  - **γENaC-specific mouse mutants** (e.g., distal polybasic-tract/cleavage-site mutants) illuminate γ-subunit proteolytic activation and sodium conservation (PMID 42037165).
- **In-vitro / heterologous systems:** *Xenopus* oocytes and mammalian cells with two-electrode/patch-clamp electrophysiology are the standard for functionally classifying *SCNN1G* variants (PMID 40153144, 40969802); cryo-EM of human ENaC provides structural context (PMID 30251954).
- **Phenotype recapitulation:** Mouse models reproduce **salt wasting, hyperkalemia, acidosis, hyperaldosteronism** (renal/systemic PHA) and the **neonatal lung-liquid** phenotype. **Limitations:** constitutive KO lethality necessitates transgenic/conditional strategies; models are predominantly **αENaC**-based (direct biallelic *Scnn1g*-null disease models are less commonly reported); species differences in ENaC proteolysis exist.
- **Resources:** MGI (Scnn1g MGI gene), IMPC/KOMP, IMSR for strain availability.

---

## Supported vs Refuted Hypotheses

**Supported (evidence-based):**
- PHA1B3 is caused by biallelic LoF *SCNN1G* (γ-ENaC) variants → systemic aldosterone resistance. ✔ (PMID 42549990, 40969802, 8640238)
- Neonatal salt-wasting triad with hyperreninemic hyperaldosteronism. ✔ (PMID 42549990, 33690157)
- Multi-organ (systemic) involvement incl. sweat/salivary/skin/airway. ✔ (PMID 3654220, 26772908)
- Loss-of-function mechanism with genotype-severity correlation. ✔ (PMID 40153144, 31301676)
- Mouse ENaC-KO recapitulates PHA-1. ✔ (PMID 9326675, 26701978)
- Ultra-rare AR disease, consanguinity/founder effects. ✔ (PMID 33690157, 8640238)

**Refuted / excluded:**
- Mineralocorticoid (fludrocortisone) therapy is effective — **refuted**; defect is downstream of MR.
- Disease is renal-limited — **refuted**; systemic multi-organ disease (distinguishes from PHA1A/NR3C2).
- Caused by gain-of-function — **refuted**; GoF *SCNN1G* causes Liddle syndrome instead (PMID 35661050).

## Limitations & Future Directions
- Ultra-rarity → no large cohorts, no formal prevalence/QoL/natural-history statistics; evidence skewed to case reports.
- Most mechanistic/model data are **αENaC**-centric; **γENaC(Scnn1g)-null** disease models and SCNN1G-specific genotype-phenotype datasets are limited.
- No approved targeted therapy; LoF channelopathies are not yet correctable — potential future directions: read-through/ASO for specific alleles, channel-activating small molecules, or gene/base-editing (all pre-clinical).

*Evidence source types: human clinical (case series/reports, functional patient studies), model organism (mouse), in vitro (heterologous electrophysiology), computational/structural (cryo-EM, network medicine).*


## Artifacts

- [OpenScientist final report](Pseudohypoaldosteronism_Type_IB3_Autosomal_Recessive-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Pseudohypoaldosteronism_Type_IB3_Autosomal_Recessive-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 25 |
| On topic | 16 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 50 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 28 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 10 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002902` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Hyponatremia**
- `HP:0002153` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Hyperkalemia**
- `HP:0001942` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Metabolic acidosis**
- `HP:0000859` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Increased circulating aldosterone concentration**
- `HP:0001944` (1 mention) - the report calls it "Clinical sign"; HP calls it **Dehydration**
- `HP:0002013` (1 mention) - the report calls it "Symptom"; HP calls it **Vomiting**
- `HP:0001254` (1 mention) - the report calls it "Symptom"; HP calls it **Lethargy**
- `HP:0002028` (1 mention) - the report calls it "Clinical sign"; HP calls it **Chronic diarrhea**
- `NCIT:C83164` (1 mention) - the report calls it "sodium chloride"; NCIT calls it **Birth Year**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0050891` (1 mention) - the report calls it "multicellular organismal water homeostasis"; GO calls it **multicellular organismal-level water homeostasis**, and lists "multicellular organismal water homeostasis" among its other names
- `GO:0003051` (1 mention) - the report calls it "angiotensin-mediated regulation of ECF volume"; GO calls it **angiotensin-mediated drinking behavior**
- `CL:1000714` (1 mention) - the report calls it "kidney collecting duct principal cell"; CL calls it **kidney cortex collecting duct principal cell**
- `CL:0002254` (1 mention) - the report calls it "epithelial cell of distal tubule"; CL calls it **epithelial cell of small intestine**
- `CL:0002633` (1 mention) - the report calls it "respiratory epithelial cell"; CL calls it **respiratory basal cell**
- `UBERON:0004135` (1 mention) - the report calls it "connecting tubule"; UBERON calls it **distal tubule**, and lists "kidney distal tubule" among its other names
- `UBERON:0001157` (1 mention) - the report calls it "Distal colon"; UBERON calls it **transverse colon**
- `UBERON:0002097` (1 mention) - the report calls it "skin"; UBERON calls it **skin of body**, and lists "skin" among its other names
- `GO:0016324` (2 mentions) - the report calls it "Apical plasma membrane", "apical plasma membrane", "Subcellular level:** **Apical plasma membrane"; GO calls it **apical plasma membrane**
- `GO:0034707` (1 mention) - the report calls it "chloride channel complex – N/A"; GO calls it **chloride channel complex**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0016324` - called "Apical plasma membrane", "apical plasma membrane", "Subcellular level:** **Apical plasma membrane"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.