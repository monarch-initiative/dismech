---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-16T15:55:56.151251'
end_time: '2026-11-16T16:13:23.692277'
duration_seconds: 1047.54
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: MTSS2-Related Neurodevelopmental Disorder
  mondo_id: MONDO:0859303
  category: Mendelian
  causal_genes: MTSS2
  omim_id: OMIM:620086
  synonyms: IDDOF; MTSS2-related disorder
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    save_artifacts: true
    artifact_max_bytes: 5242880
    artifact_keep_runtime: false
    artifact_extra_extensions: []
    artifact_include_globs: []
    artifact_exclude_globs: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
run_metadata:
  job_id: 19b28f41-63bb-459b-b2fc-486108cefe96
citation_count: 8
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 8
  quotes_valid: 7
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:36067766
  relevance_assessed: 8
  on_topic: 4
  off_topic: 2
  off_topic_references:
  - PMID:36871754
  - PMID:31232686
  needs_review: true
  validator_version: 0.6.0
term_validation:
  total_terms: 54
  verified: 50
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 29
  labels_matching: 9
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: MONDO:0859303
    reported_labels:
    - MONDO
    ontology_label: intellectual developmental disorder with ocular anomalies and
      distinctive facial features
  - term_id: HP:0000252
    reported_labels:
    - Clinical sign
    ontology_label: Microcephaly
  - term_id: HP:0000478
    reported_labels:
    - Clinical sign
    ontology_label: Abnormality of the eye
  - term_id: HP:0001999
    reported_labels:
    - Physical
    ontology_label: Abnormal facial shape
  - term_id: HP:0002011
    reported_labels:
    - Non-specific brain MRI findings
    ontology_label: Morphological central nervous system abnormality
  - term_id: UBERON:0002113
    reported_labels:
    - kidney/genitourinary tract
    ontology_label: kidney
  - term_id: NCIT:C15402
    reported_labels:
    - Speech and language therapy
    ontology_label: Conization
  - term_id: NCIT:C15339
    reported_labels:
    - occupational therapy
    ontology_label: Tissue Collection
  - term_id: NCIT:C15417
    reported_labels:
    - physical therapy
    ontology_label: Randomized Clinical Trial
  labels_variant: 11
  obsolete_terms:
  - term_id: HP:0002370
    ontology_label: obsolete Poor coordination
    replaced_by: HP:0002311
  unresolvable_prefixes:
  - OMIM
  - NC_000016.10
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: MTSS2-Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: MTSS2-Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MTSS2-Related Neurodevelopmental Disorder
- **MONDO ID:** MONDO:0859303 (if available)
- **Causal gene(s):** MTSS2
- **OMIM:** OMIM:620086
- **Synonyms:** IDDOF; MTSS2-related disorder
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **MTSS2-Related Neurodevelopmental Disorder** covering all of the
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

# MTSS2-Related Neurodevelopmental Disorder (IDDOF): Comprehensive Disease Characteristics Report

**Disease:** MTSS2-Related Neurodevelopmental Disorder
**Causal gene:** **MTSS2** (also known as *MTSS1L* / *ABBA*), chromosome 16q22.1
**Identifiers:** OMIM:620086 · MONDO:0859303 · Synonyms: IDDOF (Intellectual developmental disorder with ocular anomalies and facial dysmorphism); MTSS2-related disorder
**Inheritance:** Autosomal dominant (recurrent de novo missense)
**Report date:** 2026-11-16

---

## Summary

**MTSS2-Related Neurodevelopmental Disorder is an ultra-rare, autosomal-dominant Mendelian condition caused by a single recurrent de novo missense variant, NM_138383.3:c.2011C>T, p.(Arg671Trp), in the gene MTSS2** (also called *MTSS1L* or *ABBA*), located at chromosome 16q22.1. The gene symbol should not be confused with its paralog *MTSS1* (the tumour-suppressor "missing-in-metastasis"); this report concerns *MTSS2*, which encodes the inverse-BAR (I-BAR) membrane-deforming protein ABBA. Despite more than 50 MTSS2 variants being catalogued in ClinVar, p.Arg671Trp is the **only established pathogenic allele** — every reported patient to date (approximately 10 individuals across three clinical reports) carries this identical heterozygous change, which arises de novo and has been confirmed by trio exome sequencing. The disease is listed in OMIM under the acronym **IDDOF** (Intellectual Developmental Disorder with Ocular anomalies and Facial dysmorphism).

The clinical phenotype is a recognizable, mostly non-progressive neurodevelopmental syndrome: **global developmental delay with language-predominant impairment, mild intellectual disability, microcephaly (or relative microcephaly), ophthalmological anomalies, and mild facial dysmorphism**, with variable additional features including hypotonia, seizures, autism/behavioral disorders, feeding difficulties, poor coordination, and rare cardiac, renal/genitourinary, and gastrointestinal malformations. Brain MRI typically shows non-specific findings. The disorder is lifelong but not neurodegenerative, and management is entirely supportive and multidisciplinary; no targeted or disease-modifying therapy exists.

Mechanistically, MTSS2/ABBA is a neuronal **inverse-BAR (I-BAR) membrane-deforming protein** of the IRSp53–MIM (IMD) family that binds PI(4,5)P₂-rich membranes and ATP-actin monomers to generate negative membrane curvature, filopodia, and dendritic-spine protrusions. The p.Arg671Trp residue lies in the protein's C-terminal region, **adjacent to the WH2 actin-binding domain and outside the membrane-deforming I-BAR domain**. Functional studies in *Drosophila* show the variant is a **partial loss-of-function allele that also behaves as a toxic/dominant-negative** when over-expressed, consistent with gnomAD constraint data that argue against simple haploinsufficiency. MTSS2 is strongly brain-enriched (GTEx: highest expression in cerebellum, cortex, and hippocampus), and ABBA is especially abundant in GABAergic parvalbumin-positive interneurons and radial glia — cell types whose dysfunction plausibly links the molecular lesion to the neurodevelopmental phenotype.

---

## Section-by-Section Report

### 1. Disease Information

MTSS2-Related Neurodevelopmental Disorder is a **monogenic (Mendelian) syndromic intellectual disability** first delineated in 2022. It is characterized by the combination of developmental delay, mild intellectual disability, ocular anomalies, microcephaly, and facial dysmorphism, which gave rise to its OMIM designation IDDOF.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | 620086 (IDDOF) |
| OMIM (gene) | 616951 (MTSS2) |
| MONDO | MONDO:0859303 |
| Gene (HGNC) | HGNC:25094 (MTSS2) |
| Entrez Gene | 92154 |
| Ensembl | ENSG00000132613 |
| dbSNP (variant) | rs753688777 |
| ClinVar (variant) | Variation ID 977756 |
| OMIM allelic variant | 616951.0001 |

**Synonyms / alternative names:** IDDOF; MTSS2-related disorder; MTSS2-related neurodevelopmental disorder. The gene itself has alternative symbols *MTSS1L* and *ABBA* (Actin-Bundling protein with BAIAP2 homology, Actin-regulator A).

**Source of information:** All knowledge is derived from **aggregated disease-level resources and individual patient case reports** (OMIM, ClinVar, and ~3 peer-reviewed clinical reports describing ~10 patients), not from large EHR or registry datasets. This is an ultra-rare disorder with a small, well-characterized patient population.

---

### 2. Etiology

**Primary cause — genetic.** The disorder is caused exclusively by a **recurrent de novo heterozygous missense variant** in MTSS2: NM_138383.2/3:c.2011C>T, p.(Arg671Trp). There is no known environmental, infectious, or multifactorial contribution.

> "Here we report five individuals with the same heterozygous de novo variant in MTSS2 (GenBank: NM_138383.2: c.2011C>T [p.Arg671Trp]) identified by exome sequencing." — [PMID: 36067766](https://pubmed.ncbi.nlm.nih.gov/36067766/)

**Genetic risk factors.** The single causal variant is the only genetic risk factor. No susceptibility loci or modifier genes have been reported. Because every patient carries the identical allele, the disorder is best described as a **specific-allele (hypermutable site / recurrent de novo) disorder** rather than an allelic series.

**Environmental risk factors, protective factors, and gene–environment interactions.** **Not applicable / none identified.** As a de novo Mendelian disorder, there are no documented environmental risk or protective factors, no dietary or lifestyle modifiers, and no reported gene–environment interactions. Parental-origin and parental-age effects have not been formally established in the small cohort, though de novo missense variants in general show a paternal-age bias (not demonstrated specifically here).

---

### 3. Phenotypes

The phenotype is a **syndromic neurodevelopmental disorder** with a consistent core and a variable periphery.

> "The individuals present with global developmental delay, mild intellectual disability, ophthalmological anomalies, microcephaly or relative microcephaly, and shared mild facial dysmorphisms." — [PMID: 36067766](https://pubmed.ncbi.nlm.nih.gov/36067766/)

> "Common clinical features included developmental delay (particularly affecting language skills), mild intellectual disability, learning disabilities, microcephaly, non-specific brain MR findings and facial dysmorphisms." — [PMID: 39890443](https://pubmed.ncbi.nlm.nih.gov/39890443/)

**Core phenotype (highly consistent across patients):**

| Phenotype | Type | Suggested HPO term | Onset | Frequency | Severity |
|---|---|---|---|---|---|
| Global developmental delay (language-predominant) | Developmental | HP:0001263; HP:0000750 (Delayed speech/language) | Infancy/childhood | Most/all | Mild–moderate |
| Intellectual disability | Cognitive/behavioral | HP:0001249; HP:0001256 (mild) | Childhood | Most | Mild |
| Microcephaly / relative microcephaly | Clinical sign | HP:0000252 | Congenital/early | Frequent | Mild |
| Ophthalmological anomalies | Clinical sign | HP:0000478 | Congenital/childhood | Frequent | Variable |
| Facial dysmorphism | Physical | HP:0001999 | Congenital | Most | Mild |

**Variable / less frequent features:**

| Phenotype | Suggested HPO term | Notes |
|---|---|---|
| Hypotonia | HP:0001252 | Variable |
| Seizures (generalized febrile/afebrile; generalized EEG anomalies) | HP:0001250; HP:0002197 | Subset of patients |
| Autism spectrum disorder / psychiatric disorders | HP:0000717; HP:0000708 | Subset |
| Growth delay | HP:0001510 | Variable |
| Feeding / chewing difficulties | HP:0011968 | Variable |
| Skeletal anomalies | HP:0000924 | Variable |
| Poor coordination | HP:0002370 | Variable |
| Learning disabilities | HP:0001328 | Common |
| Non-specific brain MRI findings | HP:0002011 | Common |
| Hearing loss (rare) | HP:0000365 | Rare |
| Cardiac malformations (rare) | HP:0001627 | Rare |
| Renal/genitourinary malformations (rare) | HP:0000119 | Rare |
| Gastrointestinal anomalies (rare) | HP:0011024 | Rare |

**Onset, progression, severity:** Onset is **congenital to early childhood**. The disorder is **static/non-progressive** (developmental, not neurodegenerative), with intellectual disability generally in the **mild** range. A monozygotic-twin report ([PMID: 37657631](https://pubmed.ncbi.nlm.nih.gov/37657631/)) confirmed the recurrent variant and further delineated the phenotype.

**Quality-of-life impact:** No formal EQ-5D/SF-36/PROMIS data exist for this ultra-rare disorder. Based on phenotype, impact is driven chiefly by language delay, learning disability, and (in a subset) seizures and behavioral/autistic features; most individuals require educational support and multidisciplinary follow-up but have mild cognitive impairment compatible with substantial functional independence.

---

### 4. Genetic / Molecular Information

**Causal gene:** MTSS2 / MTSS1L / ABBA (HGNC:25094; Entrez 92154; Ensembl ENSG00000132613; gene MIM 616951). The gene maps to **chromosome 16q22.1** (GRCh38 chr16:70,661,204–70,686,086, minus strand).

**The pathogenic variant:**

| Attribute | Detail |
|---|---|
| cDNA / protein | NM_138383.3:c.2011C>T, p.(Arg671Trp) |
| Variant type | Missense (single-nucleotide substitution) |
| ClinVar classification | **Pathogenic / Likely pathogenic** (criteria provided, multiple submitters, no conflicts; last evaluated 2026-01-26) |
| ClinVar Variation ID | 977756 |
| dbSNP | rs753688777 |
| OMIM allelic variant | 616951.0001 |
| ClinGen allele | CA283508188 |
| GRCh38 SPDI | NC_000016.10:70663909:G:A (chr16:70,663,910) |
| Zygosity / origin | Heterozygous; **de novo** (germline) |
| Functional consequence | **Partial loss-of-function + dominant-negative/toxic** |

Of more than 50 other MTSS2 variants in ClinVar, essentially all are classified as **Uncertain significance** or **Likely benign** — no other pathogenic allele is established, making this a true single-variant disorder.

**Allele frequency:** The variant is extremely rare (present in dbSNP as rs753688777 but effectively absent/ultra-rare in population databases such as gnomAD), consistent with a recurrent de novo origin.

**gnomAD constraint (mechanistic inference):** MTSS2 (ENSG00000132613) shows **pLI = 0.43** and **LOEUF = 0.55** (observed/expected LoF = 27/67.1 = 0.40), i.e., only *moderate* LoF constraint, and it is **not missense-constrained overall** (missense z = −1.35; oe_mis = 1.10). The fact that a single recurrent missense is pathogenic while the gene tolerates loss-of-function reasonably well argues **against simple haploinsufficiency** and in favor of a **specific-missense / dominant-negative** mechanism.

**Modifier genes, epigenetic information, chromosomal abnormalities:** **None reported.** No modifier loci, methylation signatures, or large structural/cytogenetic changes are associated with this specific disorder.

**Somatic vs germline:** The variant is **germline** (de novo, confirmed absent in unaffected parents and co-twin). No somatic/oncogenic role for this allele is described.

---

### 5. Environmental Information

**Not applicable.** As a purely genetic de novo disorder, there are no established environmental factors, lifestyle factors, or infectious agents that cause, trigger, or modify MTSS2-Related Neurodevelopmental Disorder. No toxicological (CTD), occupational, or dietary contributions are documented.

---

### 6. Mechanism / Pathophysiology

#### Ordered causal chain (initiating lesion → clinical manifestation)

1. **De novo substitution c.2011C>T in MTSS2** introduces **p.Arg671Trp** into the ABBA protein — the initiating molecular lesion. *(Demonstrated.)*
2. **→ leads to** an altered ABBA protein in which the C-terminal region **adjacent to the WH2 actin-binding domain** (not the I-BAR domain) is perturbed; protein abundance is essentially unchanged (fibroblast immunoblots show no significant level change). *(Demonstrated.)*
3. **→ results in** impaired ABBA function — the variant **partially fails to rescue** loss of the *Drosophila* ortholog *mim*, i.e., it is a **partial loss-of-function allele**, AND when over-expressed it **reproduces the mim-LoF defects**, i.e., it is **toxic / dominant-negative**. *(Demonstrated in vivo in Drosophila.)*
4. **→ leads to** dysregulated **PI(4,5)P₂-dependent membrane deformation and ATP-actin–dependent protrusion dynamics** (I-BAR/WH2 coupling), the normal biochemical activities of ABBA. *(Inferred from biochemistry of ABBA; the exact biophysical effect of Arg671Trp is not directly demonstrated.)*
5. **→ results in** disturbed formation/initiation of **filopodia, lamellipodia-like protrusions, and dendritic spines** in neurons, and impaired radial-glia process extension. *(Inferred from ABBA cell-biology studies.)*
6. **→ leads to** altered **synaptic transmission and neuronal/circuit connectivity**, especially in brain-enriched cell types (GABAergic parvalbumin-positive interneurons; radial glia). In *Drosophila*, mim loss reduces synaptic transmission, impairs locomotion, and shortens lifespan. *(Demonstrated in model; extrapolated to human.)*
7. **→ results in** the clinical neurodevelopmental phenotype: developmental delay, mild intellectual disability, microcephaly, ocular anomalies, and facial dysmorphism. *(Clinical correlation; causal link inferred.)*

```
 c.2011C>T (de novo)
        │
        ▼
 p.Arg671Trp  ──►  C-terminal / WH2-adjacent perturbation (protein level preserved)
        │
        ├──► PARTIAL LOSS-OF-FUNCTION  (reduced rescue of mim)
        └──► DOMINANT-NEGATIVE / TOXIC (overexpression mimics LoF)
        │
        ▼
 Dysregulated I-BAR (PI(4,5)P2) membrane bending  +  WH2 (ATP-actin) dynamics
        │
        ▼
 Impaired filopodia / dendritic-spine / radial-glia protrusion dynamics
        │
        ▼
 Altered synaptic transmission & circuit wiring
 (PV+ interneurons, radial glia; brain-enriched MTSS2)
        │
        ▼
 Neurodevelopmental syndrome (DD, mild ID, microcephaly, ocular, dysmorphism)
```

#### Molecular and cellular detail

**Molecular pathways / protein function.** MTSS2/ABBA is a member of the **IRSp53–MIM (IMD / I-BAR) family**. Its N-terminal **IMD (I-BAR) domain (aa 1–252)** senses and generates **negative membrane curvature** by clustering **PI(4,5)P₂** and (for MIM/ABBA specifically) inserting an amphipathic helix into the bilayer; its C-terminal **WH2 domain (aa 719–736)** binds **ATP-actin monomers**.

> "ABBA binds ATP-actin monomers with high affinity and deforms PtdIns(4,5)P(2)-rich membranes in vitro through its WH2 and IM domains, respectively." — [PMID: 18413296](https://pubmed.ncbi.nlm.nih.gov/18413296/)

> "I-BAR domains induce strong PI(4,5)P(2) clustering upon membrane binding, bend the membrane through electrostatic interactions ... MIM and ABBA I-BARs additionally insert an amphipathic helix into the membrane bilayer, resulting in larger tubule diameter in vitro and more efficient filopodia formation in vivo." — [PMID: 19150238](https://pubmed.ncbi.nlm.nih.gov/19150238/)

**Position of Arg671.** UniProt Q765P7 (canonical 747 aa) places Arg671 in the **intrinsically disordered C-terminal moiety (between disordered stretches aa 638–664 and 691–720), just N-terminal to the WH2 domain and well outside the I-BAR domain** (sequence context QLAAN**R**HSLVE). This locates the lesion in a **regulatory region coupling membrane deformation to actin dynamics**, rather than in the core membrane-binding module — refining the mechanism toward disrupted WH2/actin regulation.

**Cellular processes.** Actin-driven membrane protrusion, filopodia initiation, dendritic-spine formation, and radial-glia extension. ABBA localizes to the **edges of membrane protrusions** and promotes dendritic-spine/filopodia initiation; MTSS1 (paralog) similarly cooperates with the **WAVE-2 and Arp2/3 complexes** at dynamic actin protrusions ([PMID: 36871754](https://pubmed.ncbi.nlm.nih.gov/36871754/)).

**Cell types (CL suggestions).** GABAergic parvalbumin-positive interneuron (CL:0000617 / neuron CL:0000540), radial glial cell (CL:0000681), hippocampal neuron.

> "we found that ABBA was highly expressed in GABAergic inhibitory neurons, such as parvalbumin-positive interneurons in the hippocampus" — [PMID: 41359239](https://pubmed.ncbi.nlm.nih.gov/41359239/)

> "elevated expression of the variant, but not the reference MTSS2 cDNA, led to similar defects as observed by mim LoF, suggesting that the variant is toxic and may act as a dominant-negative allele" — [PMID: 36067766](https://pubmed.ncbi.nlm.nih.gov/36067766/)

**Suggested GO terms:** plasma membrane bending (GO:0097320), positive regulation of filopodium assembly (GO:0051491), dendritic spine development (GO:0060996), actin filament bundle assembly (GO:0051017), regulation of synaptic transmission (GO:0050804), phosphatidylinositol-4,5-bisphosphate binding (GO:0005546), actin monomer binding (GO:0003785).

**Metabolic changes, immune involvement, epigenetics:** No metabolic, immune, or epigenetic dysregulation is implicated — the mechanism is a **cytoskeletal/membrane-dynamics defect**, not a metabolic or inflammatory one.

---

### 7. Anatomical Structures Affected

**Organ / system level.** The disorder is predominantly a disease of the **central nervous system** (nervous system; UBERON:0001016). Primary structure: **brain** (UBERON:0000955), with brain-enriched MTSS2 expression highest in **cerebellum** (UBERON:0002037), **cerebral cortex** (UBERON:0000956), and **hippocampus** (UBERON:0002421). Secondary/variable involvement: **eye** (UBERON:0000970; ocular anomalies), **skull/craniofacial skeleton** (microcephaly, dysmorphism; UBERON:0003129), and rarely **heart** (UBERON:0000948), **kidney/genitourinary tract** (UBERON:0002113), and **gastrointestinal tract** (UBERON:0001555).

**Tissue / cell level.** Nervous tissue; affected cell populations include **GABAergic parvalbumin-positive interneurons** (CL:0000617), **radial glial cells** (CL:0000681), and neurons broadly (CL:0000540).

**Subcellular level.** The pathology centers on the **plasma membrane** (GO:0005886) and the **actin cytoskeleton / cortical cytoskeleton** (GO:0015629), particularly at **membrane protrusions / filopodia / dendritic spines** (GO:0030175; GO:0043197).

**Localization / lateralization.** CNS involvement is **bilateral and symmetric**; microcephaly is global. No consistent lateralization is reported.

---

### 8. Temporal Development

- **Onset:** Congenital to early childhood; a **chronic, insidious** neurodevelopmental onset (developmental delay recognized in infancy/toddlerhood).
- **Progression:** **Static/non-progressive** developmental disorder — not neurodegenerative. Intellectual disability is stable and generally mild; brain MRI findings are non-specific and non-progressive.
- **Course / duration:** **Lifelong (chronic).** Seizures, where present, may follow their own course but the core cognitive phenotype is stable.
- **Remission:** No spontaneous remission; features are developmental and persistent.
- **Critical periods:** Early childhood is the key window for developmental/educational intervention (speech, occupational, physical therapy), though no disease-modifying intervention exists.

---

### 9. Inheritance and Population

- **Inheritance pattern:** **Autosomal dominant**, arising as a **recurrent de novo** event. All reported cases are de novo; the variant is absent in unaffected parents and in a co-twin ([PMID: 37657631](https://pubmed.ncbi.nlm.nih.gov/37657631/)).

> "Exome sequencing identified the recurrent c.2011C>T (p.Arg671Trp) variant in the MTSS2 gene. The mother and the other twin tested negative for the pathogenic variant" — [PMID: 37657631](https://pubmed.ncbi.nlm.nih.gov/37657631/)

- **Penetrance / expressivity:** Among carriers of p.Arg671Trp, penetrance appears **complete** for the neurodevelopmental phenotype, with **variable expressivity** in the peripheral features (seizures, autism, organ malformations).
- **Epidemiology:** **Ultra-rare.** Only ~10 individuals have been reported worldwide; prevalence and incidence are not formally estimable (far below Orphanet's practical reporting thresholds). No prevalence/incidence per 100,000 can be stated.
- **Genetic anticipation / mosaicism / founder effects / consanguinity / carrier frequency:** **Not applicable.** As a recurrent de novo dominant variant: no anticipation, no founder effect, no role for consanguinity, and effectively no carrier frequency. Germline mosaicism has not been reported but is theoretically possible for recurrence counseling.
- **Population demographics:** No ethnic predilection, no geographic clustering, and no established sex bias have emerged from the small cohort. Cases reported across multiple populations/countries.

---

### 10. Diagnostics

**Primary diagnostic modality — genetic testing.** Diagnosis rests on **identifying the recurrent de novo variant NM_138383.3:c.2011C>T, p.(Arg671Trp)** in MTSS2.

- **Whole-exome sequencing (WES):** The method by which the disorder was discovered and by which essentially all cases are diagnosed; **trio WES** establishes de novo status. High utility.
- **Whole-genome sequencing (WGS):** Equally capable of detecting the variant; used where WES is non-diagnostic.
- **Gene panels / single-gene testing:** MTSS2 should be included on intellectual-disability/neurodevelopmental-disorder panels. Targeted single-gene/single-variant testing for p.Arg671Trp is appropriate for confirmation or cascade purposes.
- **Chromosomal microarray, karyotyping, FISH, mtDNA, repeat-expansion testing:** Not diagnostic for this single-nucleotide missense disorder (negative/non-contributory).

**Clinical / laboratory / imaging tests.** No specific biomarker, blood/urine test, enzyme assay, or metabolic abnormality is diagnostic. **Brain MRI** typically shows **non-specific findings** and is used to exclude alternatives. **EEG** is indicated where seizures are present (may show generalized anomalies). Ophthalmologic examination documents ocular anomalies.

**Clinical criteria / differential diagnosis.** There are no formal consensus diagnostic criteria; diagnosis is molecular. The differential includes other syndromic mild intellectual-disability disorders with microcephaly, ocular anomalies, and facial dysmorphism — distinguished definitively by identifying the MTSS2 variant.

**Screening.** No newborn or population carrier screening exists or is warranted given the de novo origin and rarity.

---

### 11. Outcome / Prognosis

- **Survival / mortality:** No evidence of reduced life expectancy or disease-specific mortality; the disorder is **not life-limiting** based on reported cases. (Note: the *Drosophila* mim-LoF model shows reduced lifespan, but this does not translate to a documented human mortality signal.)
- **Morbidity / disability:** Morbidity is driven by **mild intellectual disability, language/learning impairment**, and, in subsets, **seizures, autism/behavioral issues, and feeding/coordination difficulties**. Long-term functional impairment is generally **mild**, compatible with substantial independence with support.
- **Disease course / complications:** Static developmental course; complications relate to epilepsy management and rare organ malformations (cardiac, renal, GI) where present.
- **Prognostic factors:** Presence and control of seizures, degree of language impairment, and any organ malformations modulate individual outcome. No molecular prognostic biomarkers exist (single invariant allele).
- **Quality-of-life measures:** No validated disease-specific QoL instruments have been applied.

---

### 12. Treatment

**There is no targeted, disease-modifying, or curative therapy.** Management is **entirely supportive, symptomatic, and multidisciplinary.**

- **Pharmacotherapy:** No specific drug. **Antiseizure medications** (NCIT:C264 Anticonvulsant Agent) for patients with epilepsy, chosen per seizure type; standard management of behavioral/psychiatric symptoms as needed. No pharmacogenomic guidance specific to this disorder.
- **Advanced therapeutics (gene/cell/RNA/targeted/immuno):** **None available or in trials.** No gene therapy, ASO, or targeted agent exists; the dominant-negative/partial-LoF mechanism would complicate simple gene-replacement strategies.
- **Surgical/interventional:** Only as needed for associated malformations (e.g., cardiac, genitourinary) — not disorder-specific.
- **Supportive & rehabilitative (mainstay):** **Speech and language therapy** (NCIT:C15402), **occupational therapy** (NCIT:C15339), **physical therapy** (NCIT:C15417), special educational support, developmental follow-up, nutritional/feeding support, and ophthalmologic and audiologic management.
- **Experimental treatments:** No registered clinical trials (ClinicalTrials.gov) for MTSS2-Related Neurodevelopmental Disorder as of this report.
- **Treatment strategy:** Individualized, symptom-directed, with coordinated neurodevelopmental, neurological, ophthalmologic, and (as needed) cardiac/renal/GI care.

---

### 13. Prevention

- **Primary prevention:** None possible — the causal variant is **de novo**, so there are no modifiable risk factors and no way to prevent occurrence.
- **Secondary prevention / screening:** No population or newborn screening is applicable. Early developmental screening enables early supportive intervention but does not alter the underlying disorder.
- **Genetic counseling:** For families, **recurrence risk is low** (de novo event), though **germline mosaicism** cannot be entirely excluded, so empiric recurrence risk is slightly above background. **Prenatal / preimplantation genetic testing** for the specific variant is feasible for a known familial case. Counseling should convey the de novo nature, low (but non-zero) recurrence risk, and the variable expressivity of peripheral features.
- **Tertiary prevention:** Standard management of complications (seizure control, developmental/educational support) to minimize disability.

---

### 14. Other Species / Natural Disease

- **Orthologs / comparative biology:** The disorder's mechanism is studied through orthologs rather than naturally occurring animal disease. The *Drosophila melanogaster* ortholog is **mim** (*Missing in metastasis*), expressed in most CNS neurons and a subset of glia; its loss reduces lifespan, impairs locomotion, and reduces synaptic transmission — providing the functional assay that classified p.Arg671Trp as a partial LoF/dominant-negative allele. Mammalian orthologs exist in mouse (*Mtss1l/Mtss2*/Abba) and other vertebrates.
- **Natural disease in other species / breeds / zoonosis:** **None reported.** No naturally occurring MTSS2-related disease is described in companion animals, livestock, or wildlife (no OMIA entry for a natural MTSS2 disorder), and there is no transmission/zoonotic component (genetic disorder).
- **Evolutionary conservation:** The I-BAR (IMD) and WH2 domain architecture and membrane-deforming/actin-binding functions are **conserved across metazoans**, underpinning cross-species functional-rescue experiments.

**Suggested NCBI Taxonomy references:** *Homo sapiens* (9606); *Drosophila melanogaster* (7227); *Mus musculus* (10090).

---

### 15. Model Organisms

| Model | System | What it showed | Reference |
|---|---|---|---|
| *Drosophila melanogaster* (*mim* ortholog) | Invertebrate, in vivo | *mim* is expressed in most CNS neurons and a subset of glia; **loss shortens lifespan, impairs locomotion, reduces synaptic transmission**. Human reference MTSS2 cDNA **rescues** mim-LoF; **c.2011C>T shows decreased rescue (partial LoF)** and **toxic/dominant-negative overexpression**. | [PMID: 36067766](https://pubmed.ncbi.nlm.nih.gov/36067766/) |
| Cultured neurons / cells (ABBA) | In vitro | ABBA binds ATP-actin and deforms PI(4,5)P₂ membranes; localizes to protrusion edges; promotes dendritic-spine/filopodia initiation; highly expressed in PV+ interneurons. | [PMID: 18413296](https://pubmed.ncbi.nlm.nih.gov/18413296/); [PMID: 41359239](https://pubmed.ncbi.nlm.nih.gov/41359239/) |
| Mouse (Mtss1L) | Mammalian, in vivo | Mtss1L is an exercise-induced I-BAR protein that enhances hippocampal synaptic function (structural plasticity), supporting a synaptic role. | [PMID: 31232686](https://pubmed.ncbi.nlm.nih.gov/31232686/) |
| MDCK epithelial cells (MTSS1 paralog) | In vitro | Establishes I-BAR/WAVE-2/Arp2/3 protrusion biology relevant to the family. | [PMID: 36871754](https://pubmed.ncbi.nlm.nih.gov/36871754/) |

**Genetic model types available:** *Drosophila* LoF/rescue and overexpression lines; cell-based overexpression/localization systems. **No dedicated knock-in mouse carrying p.Arg671Trp has been reported** — a clear gap.

**Phenotype recapitulation / limitations:** The *Drosophila* model recapitulates **neuronal/synaptic dysfunction** and discriminates allele behavior (partial LoF vs dominant-negative), but does not model the human syndromic features (microcephaly, ocular anomalies, facial dysmorphism). A mammalian knock-in model would be needed to study those.

---

## Mechanistic Model / Interpretation

MTSS2-Related Neurodevelopmental Disorder is a **monoallelic, single-variant cytoskeletal/membrane-dynamics disorder of the developing brain.** The unifying model is:

> A de novo p.Arg671Trp substitution in the C-terminal, WH2-adjacent regulatory region of the brain-enriched I-BAR protein ABBA/MTSS2 produces a protein that is both partially non-functional and actively interfering (dominant-negative), degrading the normal coupling between PI(4,5)P₂ membrane deformation and ATP-actin–driven protrusion formation. In neurons — especially GABAergic PV+ interneurons and radial glia that express MTSS2 most highly — this impairs filopodia, dendritic-spine, and process dynamics, perturbing synaptic connectivity and brain growth, and manifesting as developmental delay, mild ID, microcephaly, ocular anomalies, and facial dysmorphism.

Two independent lines of evidence converge on a **non-haploinsufficiency** mechanism: (1) *functional* — the variant both under-rescues and is toxic on overexpression in *Drosophila*; and (2) *population-genetic* — gnomAD shows MTSS2 is only moderately LoF-constrained (LOEUF 0.55) and not missense-constrained, so a tolerated-LoF gene producing disease via one recurrent missense points to a specific gain-of-abnormal-function/dominant-negative effect rather than dosage loss. The structural localization of Arg671 **beside the WH2 actin module** (not in the I-BAR membrane domain) sharpens this: the lesion likely disrupts actin-regulatory output rather than membrane binding per se. Brain-predominant expression (GTEx) — highest in cerebellum, cortex, and hippocampus, with near-zero expression in blood and lymphocytes — provides the tissue specificity that confines an otherwise generic cytoskeletal defect to a neurodevelopmental phenotype.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [36067766](https://pubmed.ncbi.nlm.nih.gov/36067766/) | *The recurrent de novo c.2011C>T missense variant in MTSS2 causes syndromic intellectual disability* | **Primary/landmark.** Defines the disorder, the recurrent de novo variant, the core 5-feature phenotype, CNS-high expression, and the partial-LoF + dominant-negative functional mechanism in *Drosophila*. |
| [39890443](https://pubmed.ncbi.nlm.nih.gov/39890443/) | *MTSS2-Related Disorder: Refining the Phenotype in Four New Cases and Literature Review* | Confirms and refines the recurrent phenotype (language-predominant DD, mild ID, microcephaly, non-specific MRI, dysmorphism). |
| [37657631](https://pubmed.ncbi.nlm.nih.gov/37657631/) | *MTSS2-related neurodevelopmental disorder: Further delineation of the phenotype* | Independent confirmation of the recurrent variant and its de novo nature (twin study). |
| [41359239](https://pubmed.ncbi.nlm.nih.gov/41359239/) | *Expression, Subcellular Localization, and Mechanistic Analysis of ABBA* | Identifies PV+ interneurons as a key ABBA-expressing cell type; protrusion-edge localization. |
| [18413296](https://pubmed.ncbi.nlm.nih.gov/18413296/) | *ABBA regulates plasma-membrane and actin dynamics to promote radial glia extension* | Defines ABBA's dual biochemical activities (WH2 actin-binding; IM/I-BAR membrane deformation). |
| [19150238](https://pubmed.ncbi.nlm.nih.gov/19150238/) | *Molecular mechanisms of membrane deformation by I-BAR domain proteins* | Mechanism of I-BAR PI(4,5)P₂ clustering and filopodia induction; MIM/ABBA amphipathic-helix insertion. |
| [31232686](https://pubmed.ncbi.nlm.nih.gov/31232686/) | *Exercise-induced enhancement of synaptic function triggered by Mtss1L* | Mammalian evidence for Mtss1L's synaptic/structural-plasticity role in hippocampus. |
| [36871754](https://pubmed.ncbi.nlm.nih.gov/36871754/) | *Actin-rich lamellipodia-like protrusions contribute to epithelial junction integrity* | I-BAR/WAVE-2/Arp2/3 protrusion biology (paralog MTSS1) contextualizing the family. |

---

## Limitations and Knowledge Gaps

1. **Tiny cohort (~10 patients).** All phenotype frequencies, prognosis, and QoL statements are based on case reports, not registries — effect sizes and penetrance are provisional.
2. **Single allele.** Because only p.Arg671Trp is pathogenic, there is no allelic series to map genotype–phenotype correlations, and the generalizability of the mechanism to hypothetical other MTSS2 variants is unknown.
3. **Mechanism partly inferred.** The biophysical effect of Arg671Trp on WH2/actin coupling is **inferred from protein-structure localization and Drosophila rescue data**, not directly measured in human neurons; direct demonstration (e.g., in patient iPSC-derived neurons) is lacking.
4. **No mammalian knock-in model** of p.Arg671Trp exists to test syndromic features (microcephaly, ocular, craniofacial).
5. **No biomarkers, no QoL/natural-history data, no trials, no targeted therapy.**
6. **Epidemiology unquantified** (no prevalence/incidence; no sex ratio).

---

## Proposed Follow-up Experiments / Actions

1. **Generate a knock-in mouse (Mtss2^R671W/+)** to test recapitulation of microcephaly, cortical/cerebellar development, PV+-interneuron function, and behavior.
2. **Patient iPSC-derived cortical and PV-interneuron models** to measure dendritic-spine density, filopodia dynamics, and synaptic physiology — directly testing the dominant-negative hypothesis in human neurons.
3. **Structure–function assays** of recombinant ABBA^R671W: in vitro PI(4,5)P₂ membrane deformation, ATP-actin binding (WH2), and co-assembly, to localize the functional defect to the actin-regulatory arm.
4. **Establish an international patient registry** (GeneMatcher/MatchMaker Exchange) to refine phenotype frequencies, natural history, penetrance, and QoL, and to detect any additional pathogenic MTSS2 alleles.
5. **Deep-mutational-scanning** of MTSS2 to define which residues (if any) beyond Arg671 could be pathogenic, and to clarify why this site is uniquely recurrent.
6. **Dominant-negative rescue strategies** (e.g., allele-specific knockdown of the mutant transcript) as a conceptual therapeutic proof-of-principle, given that haploinsufficiency appears tolerated.

---

*Report compiled from OMIM, ClinVar, gnomAD, GTEx, UniProt, and primary literature (8 papers, 7 confirmed findings). Evidence types span human clinical case reports, Drosophila and mouse in-vivo models, in-vitro biochemistry, and computational/constraint analysis.*


## Artifacts

- [OpenScientist final report](MTSS2-Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](MTSS2-Related_Neurodevelopmental_Disorder-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.6.0.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 8 |
| Quoted claims found in source | 7 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 8 |
| On topic | 4 |
| Off topic | 2 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:36067766` *(abstract only)*: "Here we report five individuals with the same heterozygous de novo variant in MTSS2 (GenBank: NM_138383.2: c.2011C>T [p.Arg671Trp]) identified by exome sequencing."
  - closest text in source: "Here we report five individuals with the same heterozygous de novo variant in MTSS2 (GenBank: NM_138383.2: c.2011C>T [p.Arg671Trp]) identified by exome sequencing."

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:36871754` (6 mentions) - Actin-rich lamellipodia-like protrusions contribute to the integrity of epithelial cell-cell junctions.
  - shared terms: membrane
- `PMID:31232686` (4 mentions) - Exercise-induced enhancement of synaptic function triggered by the inverse BAR protein, Mtss1L.
  - shared terms: gene, membrane

Weighed against this report's own most characteristic terms: `disorder`, `mtss2`, `variant`, `abba`, `novo`, `phenotype`, `microcephaly`, `neurodevelopmental`, `developmental`, `arg671trp`, `recurrent`, `allele`, `dominant-negative`, `dysmorphism`, `gene`, `mild`, `anomalie`, `drosophila`, `membrane`, `ocular`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 54 |
| Resolved | 50 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 29 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 11 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0859303` (2 mentions) - the report calls it "MONDO"; MONDO calls it **intellectual developmental disorder with ocular anomalies and distinctive facial features**
- `HP:0000252` (1 mention) - the report calls it "Clinical sign"; HP calls it **Microcephaly**
- `HP:0000478` (1 mention) - the report calls it "Clinical sign"; HP calls it **Abnormality of the eye**
- `HP:0001999` (1 mention) - the report calls it "Physical"; HP calls it **Abnormal facial shape**
- `HP:0002011` (1 mention) - the report calls it "Non-specific brain MRI findings"; HP calls it **Morphological central nervous system abnormality**
- `UBERON:0002113` (1 mention) - the report calls it "kidney/genitourinary tract"; UBERON calls it **kidney**
- `NCIT:C15402` (1 mention) - the report calls it "Speech and language therapy"; NCIT calls it **Conization**
- `NCIT:C15339` (1 mention) - the report calls it "occupational therapy"; NCIT calls it **Tissue Collection**
- `NCIT:C15417` (1 mention) - the report calls it "physical therapy"; NCIT calls it **Randomized Clinical Trial**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0002370` (obsolete Poor coordination) (1 mention) - replaced by `HP:0002311`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0011968` (1 mention) - the report calls it "Feeding / chewing difficulties"; HP calls it **Feeding difficulties**
- `HP:0002370` (1 mention) - the report calls it "Poor coordination"; HP calls it **obsolete Poor coordination**
- `HP:0001328` (1 mention) - the report calls it "Learning disabilities"; HP calls it **Specific learning disability**
- `HP:0000365` (1 mention) - the report calls it "Hearing loss (rare)"; HP calls it **Hearing impairment**, and lists "Hearing loss" among its other names
- `HP:0001627` (1 mention) - the report calls it "Cardiac malformations (rare)"; HP calls it **Abnormal heart morphology**, and lists "Cardiac abnormality" among its other names
- `HP:0000119` (1 mention) - the report calls it "Renal/genitourinary malformations (rare)"; HP calls it **Abnormality of the genitourinary system**, and lists "Genitourinary tract malformation" among its other names
- `HP:0011024` (1 mention) - the report calls it "Gastrointestinal anomalies (rare)"; HP calls it **Abnormality of the gastrointestinal tract**, and lists "Gastrointestinal disease" among its other names
- `CL:0000617` (2 mentions) - the report calls it "GABAergic parvalbumin-positive interneurons"; CL calls it **GABAergic neuron**
- `UBERON:0002421` (1 mention) - the report calls it "hippocampus"; UBERON calls it **hippocampal formation**, and lists "hippocampus" among its other names
- `UBERON:0001555` (1 mention) - the report calls it "gastrointestinal tract"; UBERON calls it **digestive tract**
- `GO:0015629` (1 mention) - the report calls it "actin cytoskeleton / cortical cytoskeleton"; GO calls it **actin cytoskeleton**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `NC_000016.10`.