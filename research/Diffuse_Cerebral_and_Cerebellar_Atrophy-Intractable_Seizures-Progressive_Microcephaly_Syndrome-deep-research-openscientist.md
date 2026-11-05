---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-05T00:58:31.145970'
end_time: '2026-11-05T01:44:17.013145'
duration_seconds: 2745.87
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Diffuse Cerebral and Cerebellar Atrophy-Intractable Seizures-Progressive
    Microcephaly Syndrome
  mondo_id: MONDO:0014335
  category: Mendelian
  causal_genes: QARS1
  omim_id: OMIM:615760
  synonyms: microcephaly, progressive, seizures, and cerebral and cerebellar atrophy
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
  quotes_checked: 14
  quotes_valid: 13
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:24656866
  relevance_assessed: 19
  on_topic: 7
  off_topic: 5
  off_topic_references:
  - PMID:15845536
  - PMID:12691748
  - PMID:9562563
  - PMID:30248426
  - PMID:38402621
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 33
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 21
  labels_matching: 8
  labels_mismatched: 12
  mislabelled_terms:
  - term_id: MONDO:0014335
    reported_labels:
    - MONDO
    ontology_label: diffuse cerebral and cerebellar atrophy - intractable seizures
      - progressive microcephaly syndrome
  - term_id: HP:0000253
    reported_labels:
    - Physical/sign
    ontology_label: Progressive microcephaly
  - term_id: HP:0001250
    reported_labels:
    - Sign
    ontology_label: Seizure
  - term_id: HP:0200134
    reported_labels:
    - Clinical syndrome
    ontology_label: Epileptic encephalopathy
  - term_id: HP:0002120
    reported_labels:
    - Imaging/sign
    ontology_label: Cerebral cortical atrophy
  - term_id: HP:0001272
    reported_labels:
    - Imaging/sign
    ontology_label: Cerebellar atrophy
  - term_id: HP:0010864
    reported_labels:
    - Cognitive
    ontology_label: Severe intellectual disability
  - term_id: HP:0001263
    reported_labels:
    - Behavioral
    ontology_label: Global developmental delay
  - term_id: HP:0001257
    reported_labels:
    - Sign
    ontology_label: Spasticity
  - term_id: HP:0001252
    reported_labels:
    - Sign
    ontology_label: Hypotonia
  - term_id: HP:0004322
    reported_labels:
    - Sign
    ontology_label: Short stature
  - term_id: HP:0002072
    reported_labels:
    - Sign
    ontology_label: Chorea
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Diffuse_Cerebral_and_Cerebellar_Atrophy-Intractable_Seizures-Progressive_Microcephaly_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Diffuse_Cerebral_and_Cerebellar_Atrophy-Intractable_Seizures-Progressive_Microcephaly_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Diffuse Cerebral and Cerebellar Atrophy-Intractable Seizures-Progressive Microcephaly Syndrome
- **MONDO ID:** MONDO:0014335 (if available)
- **Causal gene(s):** QARS1
- **OMIM:** OMIM:615760
- **Synonyms:** microcephaly, progressive, seizures, and cerebral and cerebellar atrophy
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Diffuse Cerebral and Cerebellar Atrophy-Intractable Seizures-Progressive Microcephaly Syndrome** covering all of the
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

# Diffuse Cerebral and Cerebellar Atrophy–Intractable Seizures–Progressive Microcephaly Syndrome (QARS1-Related Disorder)

**Disease:** Diffuse Cerebral and Cerebellar Atrophy–Intractable Seizures–Progressive Microcephaly Syndrome (MSCCA)
**MONDO ID:** MONDO:0014335 · **OMIM:** 615760 · **Causal gene:** **QARS1** (glutaminyl-tRNA synthetase 1; HGNC:9751; formerly *QARS*)

---

## Summary

**Diffuse Cerebral and Cerebellar Atrophy–Intractable Seizures–Progressive Microcephaly Syndrome (MSCCA; MONDO:0014335, OMIM 615760) is an ultra-rare autosomal-recessive neurodevelopmental and neurodegenerative disorder caused by biallelic (compound-heterozygous or homozygous) hypomorphic loss-of-function variants in *QARS1*,** the gene encoding cytosolic glutaminyl-tRNA synthetase (GlnRS; EC 6.1.1.18). GlnRS is a ubiquitously expressed housekeeping enzyme that charges tRNA^Gln with glutamine, an obligatory step in cytoplasmic protein synthesis. The original disease-defining report identified compound-heterozygous *QARS1* mutations as the only candidate causative variants in two unrelated families presenting with progressive microcephaly, severe infantile-onset seizures, and atrophy of the cerebral cortex and cerebellar vermis ([PMID: 24656866](https://pubmed.ncbi.nlm.nih.gov/24656866/)).

The core mechanism is **reduced aminoacylation capacity combined with protein destabilization/misfolding**. Variants in the N-terminal domain (NTD) reduce catalytic activity >10-fold and decrease enzyme stability, whereas variants in the catalytic core (e.g., p.Arg403Trp, p.Arg515Trp) abolish aminoacylation entirely; truncating alleles (e.g., p.Lys496*) produce diminished, aggregation-prone protein ([PMID: 24656866](https://pubmed.ncbi.nlm.nih.gov/24656866/); [PMID: 26869582](https://pubmed.ncbi.nlm.nih.gov/26869582/); [PMID: 25471517](https://pubmed.ncbi.nlm.nih.gov/25471517/)). The resulting deficit in glutaminyl-tRNA^Gln impairs translation in the developing brain, which appears exquisitely dependent on QARS1, producing progressive postnatal microcephaly, intractable seizures, and cerebral/cerebellar atrophy with profound intellectual disability.

The phenotype is a **severity continuum governed by residual enzyme activity.** At the severe end are neonatal-onset epileptic encephalopathies with marked brain atrophy; at the milder end are patients with non-epileptic microcephaly/intellectual disability or late-childhood focal epilepsy with good seizure control. Management is entirely symptomatic — antiseizure medication, developmental support, nutrition — with no disease-modifying therapy. A mechanistically plausible but QARS1-unproven downstream effector linking aminoacyl-tRNA synthetase (ARS) deficiency to seizures and developmental delay is the **integrated stress response (ISR)**, demonstrated for other ARS disorders.

---

## 1. Disease Information

**Overview.** MSCCA is a Mendelian, autosomal-recessive disorder of cytoplasmic translation. Affected children typically present in the neonatal period or early infancy with intractable seizures, show progressive (postnatal) microcephaly, and develop diffuse cerebral and cerebellar atrophy on neuroimaging, accompanied by severe-to-profound global developmental delay/intellectual disability. The disorder was defined molecularly in 2014 ([PMID: 24656866](https://pubmed.ncbi.nlm.nih.gov/24656866/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0014335 |
| OMIM | 615760 |
| Causal gene | QARS1 (HGNC:9751), chromosome 3p21.31 |
| Gene OMIM | 603727 |
| Enzyme | Glutaminyl-tRNA synthetase, EC 6.1.1.18 |

**Synonyms / alternative names.** Microcephaly, progressive, seizures, and cerebral and cerebellar atrophy (MSCCA); QARS1-related (glutaminyl-tRNA synthetase) deficiency syndrome; QARS1-associated developmental and epileptic encephalopathy (DEE); QARS1 encephalopathy.

**Information source.** Disease-level knowledge is aggregated from OMIM/Orphanet and from a modest number of primary case reports and small case series (individual-patient data). There is no EHR-scale cohort; the evidence base is small-N clinical-genetics literature (~26 published patients as of the most recent review, [PMID: 40448856](https://pubmed.ncbi.nlm.nih.gov/40448856/)).

---

## 2. Etiology

**Primary cause — genetic.** MSCCA is caused exclusively by **biallelic loss-of-function variants in *QARS1***. There is no environmental or infectious cause of the disease itself. Both compound-heterozygous and homozygous (often consanguineous) genotypes are reported.

**Genetic risk factors.** The only established risk factor is inheritance of two pathogenic *QARS1* alleles. **Consanguinity** increases risk of homozygous presentation (e.g., the Pakistani family homozygous for c.1133G>A p.(Arg378His), [PMID: 40448856](https://pubmed.ncbi.nlm.nih.gov/40448856/)). No modifier genes have been formally identified; residual enzyme activity of the specific allele combination is the principal determinant of severity (functional, not a separate locus).

**Environmental risk / protective factors.** None established. As a monogenic translational disorder, there are no known dietary, lifestyle, occupational, or toxic risk or protective factors. One notable **gene–environment interaction at the phenotype level**: intercurrent infection can trigger acute para-infectious encephalopathy in milder QARS1 patients (steroid-responsive), suggesting reduced translational reserve lowers the threshold for metabolic decompensation during illness ([PMID: 39715963](https://pubmed.ncbi.nlm.nih.gov/39715963/)).

**Protective factors.** The only "protective" factor is retained residual QARS1 catalytic activity/solubility, which attenuates severity (e.g., variants with conserved aminoacylation but reduced solubility give milder disease, [PMID: 34774383](https://pubmed.ncbi.nlm.nih.gov/34774383/)).

---

## 3. Phenotypes

Phenotypes are drawn from OMIM, published case reports, and series. Frequencies are approximate given the small cohort.

| Phenotype | Type | HPO term | Onset | Frequency | Severity / course |
|---|---|---|---|---|---|
| Progressive microcephaly | Physical/sign | HP:0000253 | Postnatal (often normal OFC at birth) | Near-universal | Severe, progressive |
| Seizures / epilepsy | Sign | HP:0001250 | Neonatal–infancy (variable) | ~86% (drug-resistant in ~79%) | Severe; often intractable |
| Developmental and epileptic encephalopathy | Clinical syndrome | HP:0200134 | Infancy | Common | Severe |
| Cerebral cortical atrophy | Imaging/sign | HP:0002120 | Infancy, progressive | Common | Progressive |
| Cerebellar atrophy (vermis > hemispheres) | Imaging/sign | HP:0001272 | Infancy, progressive | Common | Progressive |
| Severe/profound intellectual disability | Cognitive | HP:0010864 | From infancy | Near-universal | Severe |
| Global developmental delay | Behavioral | HP:0001263 | Infancy | Near-universal | Severe |
| Spasticity / hypertonia | Sign | HP:0001257 | Infancy–childhood | Frequent | Variable |
| Muscular hypotonia (axial) | Sign | HP:0001252 | Infancy | Frequent | Variable |
| Feeding difficulties / failure to thrive | Sign | HP:0011968 / HP:0001508 | Infancy | Frequent | Variable |
| Short stature / growth failure | Sign | HP:0004322 | Postnatal | Reported subset | Severe in some |
| Movement disorder (orofacial dyskinesia, stereotypies) | Sign | HP:0002072 | Infancy | Reported | Variable |

**Age of onset.** Typically neonatal to early infantile for seizures; microcephaly is usually postnatal and progressive. Milder cases show later childhood-onset focal epilepsy (e.g., 3.5 years, [PMID: 39715963](https://pubmed.ncbi.nlm.nih.gov/39715963/)).

**Phenotypic spectrum (key finding).** The disorder spans a continuum:
- **Severe end:** neonatal/infantile drug-resistant epileptic encephalopathy with marked cerebral–cerebellar atrophy (classic, [PMID: 24656866](https://pubmed.ncbi.nlm.nih.gov/24656866/)).
- **Intermediate:** severe growth failure, microcephaly, characteristic facies, intellectual disability, with *absent* epilepsy and only minor MRI changes — "The clinical presentation of our patients differs from the original QARS-associated syndrome in the severe postnatal growth failure, absence of epilepsy, and minor MRI findings, thus further expanding the phenotypic spectrum" ([PMID: 28620870](https://pubmed.ncbi.nlm.nih.gov/28620870/)).
- **Non-epileptic end:** microcephaly and severe intellectual/developmental disability without epilepsy — "The phenotype in the affected individuals of the family was characterized by microcephaly, severe intellectual and developmental disability, but no epilepsy" ([PMID: 40448856](https://pubmed.ncbi.nlm.nih.gov/40448856/)).
- **Mild end:** controllable focal epilepsy (carbamazepine, levetiracetam) with minimal/absent cerebellar atrophy ([PMID: 34774383](https://pubmed.ncbi.nlm.nih.gov/34774383/); [PMID: 39715963](https://pubmed.ncbi.nlm.nih.gov/39715963/)).

**Quality-of-life impact.** Severe cases have profound impact: non-ambulatory status, no expressive language, dependence for all activities of daily living, and medically refractory epilepsy. No formal EQ-5D/SF-36/PROMIS data exist for this ultra-rare disease.

---

## 4. Genetic / Molecular Information

**Causal gene.** *QARS1* (glutaminyl-tRNA synthetase 1), HGNC:9751, chromosome 3p21.31; encodes a cytosolic class I aminoacyl-tRNA synthetase. Reference transcript NM_005051.2.

**Pathogenic variants (representative).**

| Variant (protein) | Domain | Functional effect | Source |
|---|---|---|---|
| p.Gly45Val | N-terminal domain | >10-fold reduced aminoacylation | [PMID: 24656866](https://pubmed.ncbi.nlm.nih.gov/24656866/) |
| p.Tyr57His | N-terminal domain | >10-fold reduced aminoacylation | [PMID: 24656866](https://pubmed.ncbi.nlm.nih.gov/24656866/) |
| p.Arg403Trp | Catalytic core | Aminoacylation abolished | [PMID: 24656866](https://pubmed.ncbi.nlm.nih.gov/24656866/) |
| p.Arg515Trp | Catalytic core | Aminoacylation abolished | [PMID: 24656866](https://pubmed.ncbi.nlm.nih.gov/24656866/) |
| p.Lys496* (truncating) | Catalytic domain | Diminished, aggregated protein (LoF) | [PMID: 25471517](https://pubmed.ncbi.nlm.nih.gov/25471517/) |
| p.Arg378His (homozygous) | — | Non-epileptic phenotype | [PMID: 40448856](https://pubmed.ncbi.nlm.nih.gov/40448856/) |
| p.Arg378Cys + p.Arg525Gln | — | Reduced solubility; mild ~2-fold ↓ efficiency; mild phenotype | [PMID: 34774383](https://pubmed.ncbi.nlm.nih.gov/34774383/) |
| p.Val476Ile (homozygous) | — | Growth failure, microcephaly, no epilepsy | [PMID: 28620870](https://pubmed.ncbi.nlm.nih.gov/28620870/) |
| p.Tyr435Cys + p.Arg267Trp | — | Mild focal epilepsy; para-infectious encephalopathy | [PMID: 39715963](https://pubmed.ncbi.nlm.nih.gov/39715963/) |

**Variant classification.** Pathogenic / likely pathogenic per ACMG/AMP; several were initially VUS and later upgraded after functional testing ([PMID: 34774383](https://pubmed.ncbi.nlm.nih.gov/34774383/)). **Variant types:** predominantly missense, plus nonsense/truncating alleles. The original report emphasized that "The four QARS mutations altered highly conserved amino acids, and the aminoacylation activity of QARS was significantly impaired in mutant cell lines" ([PMID: 24656866](https://pubmed.ncbi.nlm.nih.gov/24656866/)).

**Allele frequency.** Pathogenic alleles are extremely rare in gnomAD, consistent with recessive, severe disease. **Origin:** germline. **Functional consequence:** loss of function (reduced catalytic efficiency and/or protein destabilization/aggregation); no gain-of-function or dominant-negative mechanism.

**Modifier genes.** None established. Severity tracks with residual enzyme activity of the allele combination (genotype–phenotype correlation).

**Epigenetic / chromosomal abnormalities.** None implicated; this is a single-gene point-mutation disorder, not a copy-number/structural disorder.

**CHEBI entities relevant to the enzyme:** L-glutamine (CHEBI:18050), ATP (CHEBI:15422), aminoacyl-tRNA/Gln-tRNA^Gln (CHEBI:78527 family), AMP (CHEBI:16027), diphosphate/pyrophosphate (CHEBI:33019), Mg²⁺ (CHEBI:18420).

---

## 5. Environmental Information

**Environmental factors:** None causal. **Lifestyle factors:** Not applicable (onset in infancy; monogenic). **Infectious agents:** No infectious cause. However, intercurrent infection can precipitate acute para-infectious (steroid-responsive) encephalopathic decompensation in milder QARS1 patients, indicating reduced translational reserve under metabolic stress ([PMID: 39715963](https://pubmed.ncbi.nlm.nih.gov/39715963/)).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic hypomorphic *QARS1* variants** (NTD or catalytic-core missense, or truncating) → **reduced or absent GlnRS catalytic activity and/or destabilized, misfolded, aggregation-prone enzyme** (demonstrated in vitro; [PMID: 24656866](https://pubmed.ncbi.nlm.nih.gov/24656866/); [PMID: 26869582](https://pubmed.ncbi.nlm.nih.gov/26869582/); [PMID: 25471517](https://pubmed.ncbi.nlm.nih.gov/25471517/)).
2. Loss of GlnRS function **leads to** reduced charging of tRNA^Gln with glutamine → **diminished supply of glutaminyl-tRNA^Gln** for the ribosome.
3. Reduced aminoacylated tRNA^Gln **results in** impaired/slowed cytoplasmic protein synthesis, with the **developing brain being exceptionally sensitive** (high translational demand of neurogenesis and synaptogenesis) — *inferred* from tissue-selectivity of the phenotype.
4. **Branch A (translational insufficiency):** impaired translation **leads to** failure of normal brain growth and neuronal survival → **progressive postnatal microcephaly and cerebral/cerebellar atrophy** (clinically demonstrated).
5. **Branch B (integrated stress response — inferred):** undercharged tRNA and translational stress **plausibly activate the ISR** (GCN2→eIF2α-P→ATF4). Across ARS disorders ISR activation causally contributes to disease, and in a *PARS2* Drosophila model reproduces developmental delay and seizures ([PMID: 34516839](https://pubmed.ncbi.nlm.nih.gov/34516839/); [PMID: 41380592](https://pubmed.ncbi.nlm.nih.gov/41380592/)). *No QARS1-specific ISR demonstration exists — this step is inferred.*
6. Branches A + B **converge on** cortical neuronal dysfunction and loss → **intractable seizures, severe intellectual disability, and ongoing neurodegeneration** (clinically demonstrated).
7. **Modulating factor:** residual catalytic activity/solubility of the allele combination **determines** position along the severity continuum (neonatal DEE ↔ non-epileptic microcephaly).

```
QARS1 biallelic LoF variants
        │
        ▼
↓ GlnRS activity / misfolded enzyme ──► ↓ Gln-tRNA^Gln charging
        │
        ▼
Impaired brain protein synthesis
   ├── Branch A: failed neuronal growth/survival ──► microcephaly, cerebral/cerebellar atrophy
   └── Branch B (inferred): ISR activation (GCN2–eIF2α–ATF4) ──► developmental delay, seizures
        │
        ▼
Cortical neuronal dysfunction & loss ──► intractable seizures + severe ID
        │
   (residual activity sets severity: DEE ◄──► non-epileptic microcephaly)
```

### Supporting detail

**Enzymology (upstream lesion).** GlnRS is a **class I aminoacyl-tRNA synthetase** with a mechanistically unusual requirement: it **cannot activate glutamine with ATP until tRNA^Gln is bound** (tRNA-dependent amino-acid activation). "Glutaminyl-tRNA synthetase generates Gln-tRNA(Gln) 10(7)-fold more efficiently than Glu-tRNA(Gln) and requires tRNA to synthesize the activated aminoacyl adenylate in the first step of the reaction" ([PMID: 15845536](https://pubmed.ncbi.nlm.nih.gov/15845536/)). tRNA-mediated induced fit assembles the active site ([PMID: 16734422](https://pubmed.ncbi.nlm.nih.gov/16734422/)). Amino-acid discrimination uses a negative determinant — "Arg30 functions as a negative determinant to drive binding of non-cognate glutamate into a non-productive orientation" ([PMID: 12691748](https://pubmed.ncbi.nlm.nih.gov/12691748/)) — and Tyr211 hydrogen bonding ([PMID: 9562563](https://pubmed.ncbi.nlm.nih.gov/9562563/)). This intricate active-site architecture explains why catalytic-core substitutions (Arg403, Arg515) are catastrophic.

**Protein dysfunction (two mechanistic classes).** Crystal structures of human GlnRS show that "Pathological mutations mapping in the NTD alter the domain structure, and decrease catalytic activity and stability of GlnRS, whereas missense mutations in the catalytic domain induce misfolding of the enzyme" ([PMID: 26869582](https://pubmed.ncbi.nlm.nih.gov/26869582/)). Truncating p.Lys496* shows "diminished and aberrantly aggregated expression, indicating the loss-of-function nature of this mutant" ([PMID: 25471517](https://pubmed.ncbi.nlm.nih.gov/25471517/)). Milder alleles reduce **solubility** more than catalytic efficiency ([PMID: 34774383](https://pubmed.ncbi.nlm.nih.gov/34774383/)).

**Molecular pathways / cellular processes.** Core pathway: **aminoacyl-tRNA biosynthesis → cytoplasmic translation (GO:0006412)**; GlnRS is a component of the cytoplasmic multi-tRNA synthetase complex (MSC), assembled via leucine-zipper motifs with RARS1/AIMP1/AIMP2 ([PMID: 39542129](https://pubmed.ncbi.nlm.nih.gov/39542129/)). Downstream (inferred): **integrated stress response / eIF2α signaling** and neuronal apoptosis. ARSs also have moonlighting roles (transcription, apoptosis, angiogenesis, inflammation; [PMID: 37776328](https://pubmed.ncbi.nlm.nih.gov/37776328/)), raising the possibility that loss of a non-canonical QARS1 function contributes, though this is unproven for MSCCA.

**Immune involvement.** No primary autoimmune mechanism. Notably, in a related ARS disorder (mt-AspRS/DARS2 neuronal knockout), immune/stress pathways are upregulated *before* overt atrophy ([PMID: 31887305](https://pubmed.ncbi.nlm.nih.gov/31887305/)) — a possible parallel, not demonstrated for QARS1.

**Suggested ontology terms.** GO:0006425 (glutaminyl-tRNA aminoacylation), GO:0006412 (translation), GO:0004819 (glutamine-tRNA ligase activity), GO:0034198 / amino-acid-starvation response (ISR), GO:0006915 (apoptotic process); CL:0000540 (neuron), CL:0000121 (Purkinje cell), CL:0000127 (astrocyte).

---

## 7. Anatomical Structures Affected

**Organ level.** Primary: **brain** (central nervous system). The disorder is essentially neurological; other organs are largely spared, though growth failure/short stature occurs in a subset ([PMID: 28620870](https://pubmed.ncbi.nlm.nih.gov/28620870/)).

**Regional localization (bilateral, diffuse).**
- **Cerebral cortex** (UBERON:0000956) — diffuse atrophy (HP:0002120).
- **Cerebellum**, especially **vermis** (UBERON:0004720 / UBERON:0002037) with milder hemispheric atrophy — the defining report described "atrophy of the cerebral cortex and cerebellar vermis, and mild atrophy of the cerebellar hemispheres" ([PMID: 24656866](https://pubmed.ncbi.nlm.nih.gov/24656866/)).
- White matter: variable; acute T2 hyperintensities during para-infectious episodes ([PMID: 39715963](https://pubmed.ncbi.nlm.nih.gov/39715963/)).

**Tissue / cell level.** Nervous tissue; affected populations include cortical **neurons** (CL:0000540) and cerebellar neurons including **Purkinje cells** (CL:0000121). QARS1 is ubiquitously expressed; selective CNS vulnerability reflects high translational demand during brain development.

**Subcellular level.** **Cytoplasm / cytosol** (GO:0005829) — site of cytoplasmic aminoacylation and the multi-tRNA synthetase complex. (QARS1 is cytosolic, distinct from mitochondrial ARSs.)

**Lateralization.** Bilateral and diffuse/symmetric.

---

## 8. Temporal Development

**Onset.** Congenital-to-early-infantile. Seizures often begin in the neonatal period or first months; microcephaly is typically **postnatal and progressive** (head circumference may be normal at birth). Onset pattern is chronic/insidious for atrophy, with acute seizure presentation.

**Progression.** Progressive neurodegeneration: microcephaly worsens, and cerebral/cerebellar atrophy advances over infancy and childhood. Course is generally **progressive** in classic cases; milder cases may be relatively more static with controllable epilepsy ([PMID: 34774383](https://pubmed.ncbi.nlm.nih.gov/34774383/)).

**Patterns.** Seizures are frequently relapsing/intractable; some milder cases achieve sustained seizure freedom on monotherapy ([PMID: 39715963](https://pubmed.ncbi.nlm.nih.gov/39715963/)). **Critical period:** brain development in infancy — the window of greatest vulnerability and, theoretically, greatest potential benefit from any future intervention. Episodic **para-infectious encephalopathic decompensations** occur in some milder patients ([PMID: 39715963](https://pubmed.ncbi.nlm.nih.gov/39715963/)).

**Duration.** Chronic, lifelong.

---

## 9. Inheritance and Population

**Epidemiology.** Ultra-rare; prevalence/incidence not formally estimated. ~26 patients published to date ([PMID: 40448856](https://pubmed.ncbi.nlm.nih.gov/40448856/)). No reliable per-100,000 figures exist.

**Inheritance.** **Autosomal recessive.** Both compound-heterozygous and homozygous genotypes reported.

**Penetrance / expressivity.** Penetrance appears complete for biallelic loss-of-function genotypes; **expressivity is highly variable** (severe DEE to non-epileptic microcephaly), driven by residual enzyme activity.

**Genetic anticipation:** Not applicable (not a repeat-expansion disorder). **Germline mosaicism:** not specifically reported. **Consanguinity:** important for homozygous presentations (e.g., consanguineous families; [PMID: 40448856](https://pubmed.ncbi.nlm.nih.gov/40448856/); [PMID: 28620870](https://pubmed.ncbi.nlm.nih.gov/28620870/)). **Founder effects:** none well established; individual recurrent variants noted in specific families/populations. **Carrier frequency:** not established (expected very low given rarity).

**Population demographics.** Cases reported across multiple populations (Turkish, Pakistani, Ashkenazi-Jewish, East/Southeast Asian, European). No strong sex bias reported. Age distribution: predominantly pediatric given early onset and severe course.

---

## 10. Diagnostics

**Genetic testing (definitive).** Diagnosis rests on identification of **biallelic pathogenic *QARS1* variants**, typically via **trio whole-exome sequencing (WES)** or whole-genome sequencing; targeted epilepsy/neurodevelopmental gene panels including QARS1 are also used. Single-gene testing is appropriate when the phenotype is recognized. **Functional validation** (aminoacylation assays, solubility) has been pivotal to reclassify VUS to pathogenic ([PMID: 34774383](https://pubmed.ncbi.nlm.nih.gov/34774383/); [PMID: 24656866](https://pubmed.ncbi.nlm.nih.gov/24656866/)). Chromosomal microarray/karyotype/FISH are generally uninformative (point-mutation disorder). Mitochondrial DNA testing is not indicated (QARS1 is cytosolic).

**Imaging.** **Brain MRI** is central: progressive microcephaly with **cerebral cortical atrophy and cerebellar (vermian-predominant) atrophy** ([PMID: 24656866](https://pubmed.ncbi.nlm.nih.gov/24656866/)). Milder cases may show only minor volume loss ([PMID: 34774383](https://pubmed.ncbi.nlm.nih.gov/34774383/); [PMID: 28620870](https://pubmed.ncbi.nlm.nih.gov/28620870/)). Para-infectious episodes may show reversible white-matter T2 hyperintensity with diffusion restriction ([PMID: 39715963](https://pubmed.ncbi.nlm.nih.gov/39715963/)).

**Electrophysiology.** **EEG** shows epileptiform abnormalities (e.g., shifting/multifocal foci, occipital spikes); useful for seizure characterization but not specific ([PMID: 34774383](https://pubmed.ncbi.nlm.nih.gov/34774383/); [PMID: 39715963](https://pubmed.ncbi.nlm.nih.gov/39715963/)).

**Laboratory / biomarkers.** No specific blood/urine biomarker. Diagnosis is molecular; aminoacylation/solubility assays are research-grade functional confirmations. No validated omics diagnostic.

**Clinical criteria / differential diagnosis.** Diagnosis is genetic; the clinical gestalt (progressive microcephaly + intractable infantile seizures + cerebral–cerebellar atrophy + severe ID) prompts testing. Differential diagnosis includes other **ARS-related encephalopathies** (mitochondrial and cytosolic ARS disorders), congenital/postnatal microcephaly syndromes, pontocerebellar hypoplasias, and other genetic developmental and epileptic encephalopathies; distinguished by gene-specific testing.

**Screening.** No population newborn screening. Carrier/cascade testing within families and prenatal/preimplantation testing are feasible once the familial variants are known.

---

## 11. Outcome / Prognosis

**Severity and mortality.** Classic severe disease carries a poor prognosis: profound disability, intractable epilepsy, and risk of early death; precise survival statistics are unavailable for this ultra-rare condition. Milder genotypes have more favorable outcomes with controlled epilepsy and longer survival.

**Morbidity / function.** Severe cases are non-ambulatory, nonverbal, and fully dependent, with refractory seizures. Milder cases achieve seizure control and variable developmental progress ([PMID: 34774383](https://pubmed.ncbi.nlm.nih.gov/34774383/); [PMID: 39715963](https://pubmed.ncbi.nlm.nih.gov/39715963/)). No standardized QoL instruments have been applied.

**Complications.** Status epilepticus, aspiration/feeding complications, failure to thrive, and infection-triggered encephalopathic decompensations ([PMID: 39715963](https://pubmed.ncbi.nlm.nih.gov/39715963/)).

**Prognostic factors.** The strongest predictor is **residual QARS1 enzyme activity/solubility**: variants retaining function (reduced solubility but near-normal catalysis) predict milder phenotypes ([PMID: 34774383](https://pubmed.ncbi.nlm.nih.gov/34774383/)); catalytic-null alleles predict severe disease ([PMID: 24656866](https://pubmed.ncbi.nlm.nih.gov/24656866/)).

---

## 12. Treatment

**No disease-modifying therapy exists.** Management is **symptomatic and supportive.**

**Pharmacotherapy — antiseizure medications (NCIT: Anticonvulsant Agent / Antiepileptic Agent).** Seizures are often drug-resistant (~79% pharmaco-resistant historically; [PMID: 34774383](https://pubmed.ncbi.nlm.nih.gov/34774383/)). Nonetheless, some patients respond well:
- **Carbamazepine** achieved seizure control in a milder case ([PMID: 34774383](https://pubmed.ncbi.nlm.nih.gov/34774383/)).
- **Levetiracetam** monotherapy produced a year of seizure freedom in another milder patient ([PMID: 39715963](https://pubmed.ncbi.nlm.nih.gov/39715963/)).
- **Intravenous methylprednisolone / corticosteroids** for acute para-infectious encephalopathy episodes, with optimal response reported ([PMID: 39715963](https://pubmed.ncbi.nlm.nih.gov/39715963/)).

**Supportive / rehabilitative.** Developmental therapies (physical, occupational, speech), nutritional support/feeding management, management of spasticity and tone, and multidisciplinary neurodevelopmental care.

**Advanced / experimental therapeutics.** None approved. Conceptually, loss-of-function translational disorders are candidates for future strategies (gene replacement, allele-specific solubility rescue for misfolding alleles, ISR modulation), but **no gene, cell, or RNA therapy and no clinical trials** exist for QARS1 disease.

**Pharmacogenomics / personalized medicine.** Limited to genotype-informed prognostication (residual-activity–based severity prediction).

**Suggested NCIT terms:** Carbamazepine (C341), Levetiracetam (C29295), Methylprednisolone (C636), Anticonvulsant Agent (C264), Supportive Care (C45984).

---

## 13. Prevention

**Primary prevention.** Not applicable to the biological cause (monogenic). The principal preventive levers are **reproductive/genetic**: genetic counseling for at-risk (often consanguineous) families, carrier testing, cascade testing, and prenatal or preimplantation genetic testing once familial *QARS1* variants are known.

**Secondary/tertiary prevention.** Early genetic diagnosis enables anticipatory management, avoidance of unnecessary investigations, and vigilance for infection-triggered decompensation; prompt treatment of intercurrent illness and consideration of steroids for para-infectious encephalopathy ([PMID: 39715963](https://pubmed.ncbi.nlm.nih.gov/39715963/)). Early seizure management and developmental support constitute tertiary prevention.

**Counseling.** Autosomal-recessive recurrence risk is 25% per pregnancy for carrier couples; genetic counseling is central.

**Immunization / public health / environmental interventions.** Not applicable to disease causation (standard childhood immunization and infection-avoidance are prudent given decompensation risk).

---

## 14. Other Species / Natural Disease

**Taxonomy / orthologs.** QARS1 is evolutionarily conserved; orthologs exist across eukaryotes (human *QARS1*; mouse *Qars1*). Mechanistic enzymology derives substantially from bacterial/archaeal and fungal GlnRS systems (*E. coli*, *Thermus thermophilus*, *Pseudomonas aeruginosa*, *Candida albicans* Gln4) ([PMID: 16734422](https://pubmed.ncbi.nlm.nih.gov/16734422/); [PMID: 30248426](https://pubmed.ncbi.nlm.nih.gov/30248426/); [PMID: 31833153](https://pubmed.ncbi.nlm.nih.gov/31833153/); [PMID: 38402621](https://pubmed.ncbi.nlm.nih.gov/38402621/)).

**Natural disease in other species.** No naturally occurring QARS1-equivalent disease is well documented in companion animals or wildlife (no established OMIA counterpart). **Comparative biology:** the aminoacylation mechanism is deeply conserved, making bacterial/fungal GlnRS structures directly informative about human pathogenic residues. **Zoonotic/transmission:** not applicable.

**Note:** Fungal GlnRS (Gln4) is pursued as an *antifungal drug target* — a translational-biology counterpoint, not a disease model ([PMID: 38402621](https://pubmed.ncbi.nlm.nih.gov/38402621/)).

---

## 15. Model Organisms

**Direct QARS1 disease models are limited.** No well-characterized mouse knock-in model recapitulating MSCCA is reported in this knowledge base. **In vitro / cellular models** have been central:
- **Patient-derived cell lines / transfected cells:** aminoacylation and stability assays demonstrating reduced catalytic activity and misfolding ([PMID: 24656866](https://pubmed.ncbi.nlm.nih.gov/24656866/)).
- **Neuroblastoma 2A (N2a) cells:** transient expression of p.Lys496* showed diminished, aggregated protein ([PMID: 25471517](https://pubmed.ncbi.nlm.nih.gov/25471517/)).
- **Recombinant human GlnRS crystallography:** structural basis of NTD vs catalytic-domain mutation effects ([PMID: 26869582](https://pubmed.ncbi.nlm.nih.gov/26869582/)).

**Analogous ARS models (supporting the mechanistic framework, not QARS1-specific).**
- ***Drosophila* PARS2 (mitochondrial prolyl-tRNA synthetase) model:** "Inactivation of dPARS2 in Drosophila causes developmental delay and seizure, two main clinical features in human PARS2 deficiency-associated patients," via ISR activation ([PMID: 41380592](https://pubmed.ncbi.nlm.nih.gov/41380592/)).
- **Neuronal *Dars2* knockout mice:** progressive cortical atrophy, behavioral disruption, and early immune/stress-pathway activation ([PMID: 31887305](https://pubmed.ncbi.nlm.nih.gov/31887305/)).

**Model limitations.** Bacterial/fungal and in-vitro systems capture enzymology but not CNS-selective neurodegeneration; cross-ARS animal models demonstrate ISR-linked seizures/delay but are not QARS1. A faithful QARS1 hypomorphic mammalian model remains a gap.

---

## Key Findings (expanded)

### F001 — Biallelic QARS1 loss-of-function variants cause MSCCA
Whole-exome sequencing identified compound-heterozygous *QARS1* mutations as the only candidate causative variants in two unrelated families with progressive microcephaly, infantile seizures, and cerebral–cerebellar atrophy. "we report the identification of mutations in QARS (encoding glutaminyl-tRNA synthetase [QARS]) as the causative variants in two unrelated families affected by progressive microcephaly, severe seizures in infancy, atrophy of the cerebral cortex and cerebellar vermis, and mild atrophy of the cerebellar hemispheres" ([PMID: 24656866](https://pubmed.ncbi.nlm.nih.gov/24656866/)). Four variants (NTD: p.Gly45Val, p.Tyr57His; catalytic core: p.Arg403Trp, p.Arg515Trp) altered conserved residues and impaired aminoacylation — NTD variants >10-fold, catalytic-core variants completely — establishing loss of function.

### F002 — Dual mechanism: reduced catalytic efficiency plus misfolding
Human GlnRS crystal structures revealed two mechanistic classes: "Pathological mutations mapping in the NTD alter the domain structure, and decrease catalytic activity and stability of GlnRS, whereas missense mutations in the catalytic domain induce misfolding of the enzyme" ([PMID: 26869582](https://pubmed.ncbi.nlm.nih.gov/26869582/)). A truncating allele behaves as a protein-destabilizing LoF: p.Lys496* produced "diminished and aberrantly aggregated expression" in N2a cells ([PMID: 25471517](https://pubmed.ncbi.nlm.nih.gov/25471517/)).

### F003 — Broad phenotypic spectrum from severe DEE to non-epileptic microcephaly
Severity tracks residual enzyme function. Severe neonatal epileptic encephalopathy anchors one end ([PMID: 24656866](https://pubmed.ncbi.nlm.nih.gov/24656866/)); a consanguineous family of seven with homozygous p.(Arg378His) had "microcephaly, severe intellectual and developmental disability, but no epilepsy" ([PMID: 40448856](https://pubmed.ncbi.nlm.nih.gov/40448856/)); and a homozygous p.Val476Ile presentation showed "severe postnatal growth failure, absence of epilepsy, and minor MRI findings, thus further expanding the phenotypic spectrum" ([PMID: 28620870](https://pubmed.ncbi.nlm.nih.gov/28620870/)). Milder compound-heterozygous cases achieve seizure control ([PMID: 34774383](https://pubmed.ncbi.nlm.nih.gov/34774383/); [PMID: 39715963](https://pubmed.ncbi.nlm.nih.gov/39715963/)).

### F004 — Integrated stress response as a plausible shared effector (inferred)
Across ARS disorders, reduced aminoacylation activates the ISR, which causally contributes to pathology. In a Drosophila PARS2 model, "Inactivation of dPARS2 in Drosophila causes developmental delay and seizure, two main clinical features in human PARS2 deficiency-associated patients" via ISR ([PMID: 41380592](https://pubmed.ncbi.nlm.nih.gov/41380592/)); ISR also drives ARS-associated peripheral neuropathy ([PMID: 34516839](https://pubmed.ncbi.nlm.nih.gov/34516839/)). No QARS1-specific ISR demonstration exists — this remains inferred.

### F005 — GlnRS is a class I synthetase with unusual tRNA-dependent glutamine activation
GlnRS uniquely requires prior tRNA binding to activate glutamine: it "generates Gln-tRNA(Gln) 10(7)-fold more efficiently than Glu-tRNA(Gln) and requires tRNA to synthesize the activated aminoacyl adenylate in the first step of the reaction" ([PMID: 15845536](https://pubmed.ncbi.nlm.nih.gov/15845536/)). Cognate selection uses "Arg30 ... as a negative determinant to drive binding of non-cognate glutamate into a non-productive orientation" ([PMID: 12691748](https://pubmed.ncbi.nlm.nih.gov/12691748/)) and Tyr211 hydrogen bonding ([PMID: 9562563](https://pubmed.ncbi.nlm.nih.gov/9562563/)). This explains why catalytic-core substitutions abolish activity.

---

## Mechanistic Model / Interpretation (synthesis)

MSCCA is best understood as a **translational-insufficiency disorder of the developing brain.** Two mutation classes converge on loss of GlnRS function: (i) NTD missense variants that modestly reduce catalysis and destabilize the enzyme, and (ii) catalytic-core missense/truncating variants that abolish activity or cause aggregation. The shared endpoint is **insufficient glutaminyl-tRNA^Gln**, which throttles protein synthesis when the brain's biosynthetic demand peaks. This produces the triad of progressive microcephaly, cerebral/cerebellar atrophy, and intractable seizures. The **severity continuum maps onto residual activity/solubility**, explaining why some biallelic patients have neonatal epileptic encephalopathy while others have non-epileptic microcephaly or well-controlled focal epilepsy. A biologically compelling but **QARS1-unproven amplifier** is the **integrated stress response**, which in other ARS disorders is sufficient to generate seizures and developmental delay in vivo.

| Mutation class | Example | Catalysis | Stability/solubility | Typical severity |
|---|---|---|---|---|
| NTD missense | p.Gly45Val, p.Tyr57His | ↓ >10-fold | ↓ | Severe |
| Catalytic-core missense | p.Arg403Trp, p.Arg515Trp | Abolished | — | Severe |
| Truncating | p.Lys496* | Lost | Aggregated | Severe |
| Solubility-predominant | p.Arg378Cys/p.Arg525Gln | ~2-fold ↓ | ↓↓ solubility | Mild |

---

## Evidence Base

| PMID | Role | Key support |
|---|---|---|
| [24656866](https://pubmed.ncbi.nlm.nih.gov/24656866/) | Landmark | Establishes QARS1 as causal; defines NTD vs catalytic-core variant effects |
| [26869582](https://pubmed.ncbi.nlm.nih.gov/26869582/) | Mechanism | Human GlnRS structures: NTD → ↓activity/stability; catalytic domain → misfolding |
| [25471517](https://pubmed.ncbi.nlm.nih.gov/25471517/) | Mechanism | p.Lys496* truncation → aggregated, diminished protein (LoF) |
| [40448856](https://pubmed.ncbi.nlm.nih.gov/40448856/) | Spectrum | Non-epileptic phenotype; 26-patient review |
| [28620870](https://pubmed.ncbi.nlm.nih.gov/28620870/) | Spectrum | Growth failure/microcephaly without epilepsy; phenotypic expansion |
| [34774383](https://pubmed.ncbi.nlm.nih.gov/34774383/) | Spectrum/therapy | Mild phenotype from solubility-reducing variants; 86% epilepsy/79% drug-resistant; carbamazepine control |
| [39715963](https://pubmed.ncbi.nlm.nih.gov/39715963/) | Spectrum/therapy | Childhood focal epilepsy; levetiracetam control; steroid-responsive para-infectious encephalopathy |
| [15845536](https://pubmed.ncbi.nlm.nih.gov/15845536/) | Enzymology | tRNA-dependent amino-acid activation; 10⁷-fold Gln selectivity |
| [16734422](https://pubmed.ncbi.nlm.nih.gov/16734422/) | Enzymology | tRNA-mediated induced-fit active-site assembly |
| [12691748](https://pubmed.ncbi.nlm.nih.gov/12691748/) | Enzymology | Arg30 negative determinant for amino-acid discrimination |
| [9562563](https://pubmed.ncbi.nlm.nih.gov/9562563/) | Enzymology | Tyr211 hydrogen-bond recognition of glutamine |
| [41380592](https://pubmed.ncbi.nlm.nih.gov/41380592/) | Inferred mechanism | PARS2 ISR model reproduces delay + seizures |
| [34516839](https://pubmed.ncbi.nlm.nih.gov/34516839/) | Inferred mechanism | ISR contributes to ARS-associated neuropathy |
| [31887305](https://pubmed.ncbi.nlm.nih.gov/31887305/) | Analogous model | DARS2 neuronal KO: progressive atrophy + early immune/stress activation |
| [39542129](https://pubmed.ncbi.nlm.nih.gov/39542129/) | Context | QARS1 within multi-tRNA synthetase complex |
| [37776328](https://pubmed.ncbi.nlm.nih.gov/37776328/) | Context | ARS moonlighting functions (apoptosis, transcription) |
| [34774383](https://pubmed.ncbi.nlm.nih.gov/34774383/) | Epidemiology | 86% of prior QARS1 patients had epilepsy; 79% pharmaco-resistant |

---

## Limitations and Knowledge Gaps

- **Small evidence base:** ~26 published patients; frequencies and prognosis are approximate, and no registry/natural-history study exists.
- **ISR step is inferred, not demonstrated for QARS1:** the integrated stress-response link rests on analogy to PARS2/MARS1/other ARS disorders, not direct QARS1 experiments.
- **No faithful mammalian QARS1 disease model** to establish the causal chain in vivo or test therapies.
- **Genotype–phenotype correlation is qualitative:** residual-activity thresholds that separate epileptic from non-epileptic phenotypes are not quantitatively defined.
- **No biomarkers, no disease-modifying therapy, no clinical trials.**
- **Moonlighting/apoptosis contribution unquantified** for QARS1 specifically.

## Proposed Follow-up Experiments / Actions

1. **Generate a Qars1 hypomorphic mouse** (knock-in of p.Arg403Trp or an NTD variant) to test whether reduced aminoacylation produces progressive microcephaly, cerebellar atrophy, and seizures, and to map the causal chain in vivo.
2. **Directly assay ISR activation** (eIF2α-P, ATF4, CHOP) in QARS1-mutant patient iPSC-derived neurons/organoids, and test whether ISR inhibitors (e.g., ISRIB) rescue translational and survival phenotypes — converting the inferred Branch B into a tested step.
3. **Quantitative genotype–function–phenotype mapping:** systematically measure aminoacylation kinetics and solubility for all reported variants and correlate with clinical severity to define a predictive threshold for epilepsy risk.
4. **Cerebral organoid modeling** to capture CNS-selective vulnerability and screen mechanism-based therapeutics (ISR modulation, chemical chaperones for misfolding alleles).
5. **Establish an international patient registry** for reliable natural-history, survival, seizure-response, and QoL data, with standardized MRI/EEG phenotyping.
6. **Prospectively evaluate corticosteroid protocols** for para-infectious encephalopathic decompensations, given anecdotal benefit.

---

*Evidence source legend: human clinical (case reports/series), in vitro (aminoacylation/solubility/structural), model organism (Drosophila/mouse for analogous ARS genes), computational/structural (crystallography, docking).*


## Artifacts

- [OpenScientist final report](Diffuse_Cerebral_and_Cerebellar_Atrophy-Intractable_Seizures-Progressive_Microcephaly_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Diffuse_Cerebral_and_Cerebellar_Atrophy-Intractable_Seizures-Progressive_Microcephaly_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 14 |
| Quoted claims found in source | 13 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 19 |
| On topic | 7 |
| Off topic | 5 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:24656866` *(abstract only)*: "we report the identification of mutations in QARS (encoding glutaminyl-tRNA synthetase [QARS]) as the causative variants in two unrelated families affected by progressive microcephaly, severe seizures in infancy, atrophy of the cerebral cortex and cerebellar vermis, and mild atrophy of the cerebellar hemispheres"
  - closest text in source: "we report the identification of mutations in QARS (encoding glutaminyl-tRNA synthetase [QARS]) as the causative variants in two unrelated families affected by progressive microcephaly, severe seizures in infancy, atrophy of the cerebral cortex and cerebellar vermis, and mild atrophy of the cerebellar hemispheres"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:15845536` (6 mentions) - tRNA-dependent aminoacyl-adenylate hydrolysis by a nonediting class I aminoacyl-tRNA synthetase.
  - shared terms: aminoacylation
- `PMID:12691748` (6 mentions) - Amino acid discrimination by a class I aminoacyl-tRNA synthetase specified by negative determinants.
  - shared terms: enzyme
- `PMID:9562563` (6 mentions) - How glutaminyl-tRNA synthetase selects glutamine.
  - shared terms: enzyme
- `PMID:30248426` (3 mentions) - Structural and functional analysis of Glutaminyl-tRNA synthetase (TtGlnRS) from Thermus thermophilus HB8 and its complexes.
  - shared terms: enzyme
- `PMID:38402621` (5 mentions) - Allosteric inhibition of tRNA synthetase Gln4 by N-pyrimidinyl-β-thiophenylacrylamides exerts highly selective antifungal activity.
  - shared terms: activity

Weighed against this report's own most characteristic terms: `qars1`, `seizure`, `disorder`, `atrophy`, `microcephaly`, `patient`, `variant`, `progressive`, `activity`, `developmental`, `disease`, `cerebellar`, `aminoacylation`, `cerebral`, `severe`, `milder`, `epilepsy`, `enzyme`, `phenotype`, `reduced`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 21 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 12 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014335` (3 mentions) - the report calls it "MONDO"; MONDO calls it **diffuse cerebral and cerebellar atrophy - intractable seizures - progressive microcephaly syndrome**
- `HP:0000253` (1 mention) - the report calls it "Physical/sign"; HP calls it **Progressive microcephaly**
- `HP:0001250` (1 mention) - the report calls it "Sign"; HP calls it **Seizure**
- `HP:0200134` (1 mention) - the report calls it "Clinical syndrome"; HP calls it **Epileptic encephalopathy**
- `HP:0002120` (2 mentions) - the report calls it "Imaging/sign"; HP calls it **Cerebral cortical atrophy**
- `HP:0001272` (1 mention) - the report calls it "Imaging/sign"; HP calls it **Cerebellar atrophy**
- `HP:0010864` (1 mention) - the report calls it "Cognitive"; HP calls it **Severe intellectual disability**
- `HP:0001263` (1 mention) - the report calls it "Behavioral"; HP calls it **Global developmental delay**
- `HP:0001257` (1 mention) - the report calls it "Sign"; HP calls it **Spasticity**
- `HP:0001252` (1 mention) - the report calls it "Sign"; HP calls it **Hypotonia**
- `HP:0004322` (1 mention) - the report calls it "Sign"; HP calls it **Short stature**
- `HP:0002072` (1 mention) - the report calls it "Sign"; HP calls it **Chorea**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005829` (1 mention) - the report calls it "Cytoplasm / cytosol"; GO calls it **cytosol**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000540` - called "neuron", "neurons"
- `CL:0000121` - called "Purkinje cell", "Purkinje cells"