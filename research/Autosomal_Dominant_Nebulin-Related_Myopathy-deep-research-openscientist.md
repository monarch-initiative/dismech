---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-09T16:55:47.907778'
end_time: '2026-11-09T17:14:41.636749'
duration_seconds: 1133.73
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Autosomal Dominant Nebulin-Related Myopathy
  mondo_id: MONDO:1010152
  category: Mendelian
  causal_genes: NEB
  omim_id: not recorded
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
citation_count: 22
reference_validation:
  total_references: 26
  verified: 26
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 26
  on_topic: 21
  validator_version: 0.5.1
term_validation:
  total_terms: 34
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 1
  labels_mismatched: 14
  mislabelled_terms:
  - term_id: HP:0002460
    reported_labels:
    - Clinical sign
    ontology_label: Distal muscle weakness
  - term_id: HP:0009027
    reported_labels:
    - Clinical sign
    ontology_label: Foot dorsiflexor weakness
  - term_id: HP:0009130
    reported_labels:
    - Pathology
    ontology_label: Hand muscle atrophy
  - term_id: HP:0001252
    reported_labels:
    - Clinical sign
    ontology_label: Hypotonia
  - term_id: HP:0000218
    reported_labels:
    - Physical
    ontology_label: High palate
  - term_id: HP:0011968
    reported_labels:
    - Symptom
    ontology_label: Feeding difficulties
  - term_id: HP:0003803
    reported_labels:
    - Lab/pathology
    ontology_label: Type 1 muscle fiber predominance
  - term_id: HP:0002093
    reported_labels:
    - Clinical sign
    ontology_label: Respiratory insufficiency
  - term_id: HP:0001283
    reported_labels:
    - Clinical sign
    ontology_label: Bulbar palsy
  - term_id: HP:0003798
    reported_labels:
    - Lab/pathology
    ontology_label: Nemaline bodies
  - term_id: NCIT:C116838
    reported_labels:
    - respiratory support
    ontology_label: CNS 2c
  - term_id: NCIT:C15719
    reported_labels:
    - physical therapy
    ontology_label: Surveillance
  - term_id: NCIT:C15285
    reported_labels:
    - nutritional support
    ontology_label: Nursing Research
  - term_id: NCIT:C51696
    reported_labels:
    - orthopedic procedure
    ontology_label: Orthotopic Liver Transplantation
  labels_variant: 3
  unresolvable_prefixes:
  - GARD
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Autosomal_Dominant_Nebulin-Related_Myopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Autosomal_Dominant_Nebulin-Related_Myopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Nebulin-Related Myopathy
- **MONDO ID:** MONDO:1010152 (if available)
- **Causal gene(s):** NEB
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Nebulin-Related Myopathy** covering all of the
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

# Autosomal Dominant Nebulin-Related Myopathy (MONDO:1010152): A Comprehensive Disease Characterization

## Summary

**Autosomal Dominant Nebulin-Related Myopathy (MONDO:1010152)** is a rare, mild, slowly progressive, predominantly **distal** skeletal muscle myopathy caused by heterozygous pathogenic variation in **NEB**, the gene on chromosome 2q23.3 encoding **nebulin** — a giant (~700–800 kDa) filamentous sarcomeric thin-filament protein that acts as a "molecular ruler" to specify and stabilize actin thin-filament length. The dominant distal form is specifically caused by **single large heterozygous (sometimes mosaic) multi-exon deletions spanning ~52–97 exons of NEB**. This contrasts sharply with the far more common autosomal **recessive** nemaline myopathy type 2 (NEM2; OMIM 256030), which arises from biallelic (compound heterozygous or homozygous) NEB variants and produces a more severe, proximal-predominant congenital phenotype.

The mechanistic chain is well established at the molecular level: loss/dysfunction of nebulin leads to **shortened and non-uniform actin thin filaments**, **reduced myofilament calcium sensitivity**, **altered crossbridge cycling kinetics**, and a **destabilized myosin super-relaxed (SRX) state** that raises resting ATP consumption. Together these produce a ~60% loss of force-generating capacity and the characteristic muscle weakness. A key unresolved question is whether the dominant large deletions act via **haploinsufficiency** or a **dominant-negative** mechanism — the curated MONDO definition asserts a dominant-negative mechanism, but direct experimental proof for the dominant distal form specifically is still lacking.

There is **no curative therapy**. Management is supportive (respiratory support, physiotherapy/orthotics for foot drop, feeding and bulbar support, orthopedic care). The most mechanistically rational investigational approaches are **fast skeletal troponin activators** (e.g., CK-2066260, which restores calcium sensitivity of force in patient fibers) and **myosin modulators** (e.g., Mavacamten, which reverses ATP overconsumption in vitro). This report synthesizes 10 confirmed findings from 48 reviewed papers into a complete disease-knowledge-base entry across all 15 requested domains.

---

## Key Findings

### Finding 1 — Large heterozygous NEB deletions cause a mild dominant distal phenotype

The defining molecular lesion of this disease is a **single large heterozygous deletion of NEB**. In the landmark cohort of Sagath et al. (2025), 35 families with NEB structural variants were studied; among them, **12 families with a distal myopathy phenotype** (10 previously unpublished) carried **8 unique large deletions encompassing 52–97 exons**, present in either heterozygous (n=10) or mosaic (n=2) state. Critically, *"all patients with large dominant deletions in NEB had milder, predominantly distal muscle weakness,"* and the authors state that *"large deletions have been shown to cause dominantly inherited distal myopathies"* [PMID: 40517164](https://pubmed.ncbi.nlm.nih.gov/40517164/). This established, for the first time, a statistically significant association between large heterozygous NEB deletions and a dominant distal phenotype, cleanly separating this entity from recessive NEM2.

### Finding 2 — NEB encodes nebulin, a giant thin-filament molecular ruler

Nebulin (~700–800 kDa) is a giant filamentous protein that spans nearly the entire length of the actin thin filament in skeletal muscle sarcomeres. Cryo-EM/tomography of intact myofibrils demonstrated that *"in skeletal muscle, nebulin stabilizes and regulates the length of thin filaments"* and that the structures *"support the role of nebulin as a thin filament 'molecular ruler' and provide a molecular basis for studying nemaline myopathies"* [PMID: 35175800](https://pubmed.ncbi.nlm.nih.gov/35175800/). Nebulin interacts with actin and a troponin-T linker (not directly with myosin or tropomyosin), binds CapZ at the Z-disc to anchor thin-filament barbed ends [PMID: 18272787](https://pubmed.ncbi.nlm.nih.gov/18272787/), and regulates muscle contraction, Z-disc formation, and myofibril assembly [PMID: 26792324](https://pubmed.ncbi.nlm.nih.gov/26792324/).

### Finding 3 — Nebulin deficiency weakens muscle via shortened filaments, reduced Ca²⁺ sensitivity, and altered crossbridge cycling

In NEB-mutant patient muscle, nebulin is severely reduced (especially its N-terminus), force-generating capacity falls by ~60%, and the force–sarcomere length relationship is left-shifted. Average thin-filament length is *"reduced from approximately 1.3 microm in control muscle to approximately 0.75 microm in NM-NEB muscle"* [PMID: 19346529](https://pubmed.ncbi.nlm.nih.gov/19346529/). Beyond filament length, nebulin-deficient fibers *"develop less force due to reduced myofilament calcium sensitivity and altered crossbridge cycling kinetics"* [PMID: 21115852](https://pubmed.ncbi.nlm.nih.gov/21115852/). Conditional Neb-knockout mice recapitulate reduced specific force from fewer force-generating crossbridges and shorter thin filaments, with muscle-type-dependent atrophy via MuRF-1/MUSA1/Gadd45a proteolysis [PMID: 26123491](https://pubmed.ncbi.nlm.nih.gov/26123491/). A fast skeletal troponin activator, CK-2066260, *"greatly increased the calcium-sensitivity of force generation"* in patient fibers [PMID: 23572184](https://pubmed.ncbi.nlm.nih.gov/23572184/).

### Finding 4 — NEB gene architecture and the recessive-vs-dominant divide

NEB (HGNC-approved symbol **NEB**; chromosome **2q23.3**) is one of the largest human genes with ~183 exons, including an 8-exon triplicate region (exons 82–105) and alternatively spliced exons. **Recessive NEM2 (OMIM 256030)** results from biallelic variants — point mutations, small indels, splice variants, and intragenic copy-number changes. The in-frame deletion of **exon 55 (NEB ΔExon55)** is the single most common disease-causing variant and a **founder mutation in Ashkenazi Jewish patients** — a model was designed to *"replicate a founder mutation seen frequently in patients with nemaline myopathy with Ashkenazi Jewish heritage"* [PMID: 23715096](https://pubmed.ncbi.nlm.nih.gov/23715096/). By contrast, single large heterozygous deletions spanning 52–97 exons cause the autosomal dominant distal myopathy: *"eight unique, large deletions encompassing 52-97 exons in either heterozygous (n = 10) or mosaic (n = 2) state were identified"* [PMID: 40517164](https://pubmed.ncbi.nlm.nih.gov/40517164/).

### Finding 5 — Epidemiology, clinical, and diagnostic profile

Nemaline myopathy overall affects **~1 in 50,000 live births**, with prevalence up to ~1 in 20,000 in certain populations; NEB is the most common causative gene (>50% of cases) [PMID: 31530540](https://pubmed.ncbi.nlm.nih.gov/31530540/). NEB-associated phenotypes span classic nemaline myopathy, core-rod myopathy, and distal myopathies — *"pathogenic NEB variants have been identified in core-rod myopathy and in distal myopathies"* [PMID: 25205138](https://pubmed.ncbi.nlm.nih.gov/25205138/). Diagnosis rests on muscle biopsy (nemaline rods — Z-disc-derived electron-dense bodies), genetic testing, EMG (myogenic pattern), and muscle MRI. In NEB-related NM, *"most patients (18/21) presented with lower limb muscle weakness, with a distal predominance,"* and MRI shows greatest fatty infiltration in soleus, gastrocnemius, and gluteus maximus [PMID: 40583855](https://pubmed.ncbi.nlm.nih.gov/40583855/). Natural history is relatively stable; in a cross-sectional cohort, 58% needed mechanical support and 65% had abnormal pulmonary function [PMID: 33397769](https://pubmed.ncbi.nlm.nih.gov/33397769/).

### Finding 6 — Animal and cellular models recapitulate the disease

Multiple models reproduce NEB myopathy: conditional Neb-KO mice develop nemaline rods, <5% nebulin, shortened thin filaments, reduced specific force, and fiber-type switching [PMID: 26123491](https://pubmed.ncbi.nlm.nih.gov/26123491/); Neb ΔExon55 mice replicate the Ashkenazi founder mutation, producing *"nemaline bodies—a hallmark feature of nemaline myopathy—in muscle fibres from Neb(ΔExon55) mice"* [PMID: 23715096](https://pubmed.ncbi.nlm.nih.gov/23715096/); and an allelic series of zebrafish neb mutants *"recapitulate most aspects of NEB-based NM, showing drastically reduced survival, defective muscle structure, reduced contraction force, shorter thin filaments"* [PMID: 38493359](https://pubmed.ncbi.nlm.nih.gov/38493359/).

### Finding 7 — No curative therapy; supportive management with mechanism-based leads

Management is primarily supportive: respiratory support (NIV/ventilation), physiotherapy/orthotics for distal weakness and foot drop, feeding/bulbar support, and orthopedic care — *"management remains mainly supportive, and currently, there is no available curative treatment"* [PMID: 38866581](https://pubmed.ncbi.nlm.nih.gov/38866581/). Controlled model studies of nutritional supplements (L-tyrosine, L-carnitine, taurine, creatine) *"revealed no significant improvement in skeletal muscle function emphasizing the urgency to develop effective therapies for nemaline myopathy"* [PMID: 29848386](https://pubmed.ncbi.nlm.nih.gov/29848386/). Mechanism-based leads include fast skeletal troponin activators and myosin modulators.

### Finding 8 — Variant architecture determines inheritance and severity

In the 35-family cohort, recessive disease arose from compound-heterozygous intragenic deletions/duplications or triplicate-region gains plus a small trans variant (23 families; 2 homozygous), and *"in the families where inheritance was recessive, no correlation could be made between the types of variants and the severity of the disease."* In contrast, the 12 distal-myopathy families each carried a single large heterozygous deletion, and the authors *"establish a clear and statistically significant association"* between large dominant NEB deletions and the distal phenotype [PMID: 40517164](https://pubmed.ncbi.nlm.nih.gov/40517164/). Independent large cohorts (de Feraudy et al., 49 nebulin-related congenital myopathy patients) confirm the histological spectrum of rods ± cores [PMID: 42609597](https://pubmed.ncbi.nlm.nih.gov/42609597/).

### Finding 9 — NEB mutations destabilize the myosin super-relaxed state and remodel the energy proteome

In muscle fibers from NEB-NM patients and nebulin-deficient mice, *"the myosin stabilizing conformational state, known as super-relaxed state, was significantly impaired, inducing an increase in the energy (ATP) consumption of resting muscle fibres from NEB-NM patients,"* which helps explain why *"histological analyses of patients' muscle biopsies often reveal unexplained accumulation of glycogen and abnormally shaped mitochondria"* [PMID: 36528760](https://pubmed.ncbi.nlm.nih.gov/36528760/). The myosin modulator Mavacamten (promotes SRX) reversed myosin ATP overconsumption in vitro in patient fibers, but 4-week in vivo treatment of conditional Neb-KO mice did not correct the dysregulated energy proteome [PMID: 39216086](https://pubmed.ncbi.nlm.nih.gov/39216086/).

### Finding 10 — MONDO curation confirms gene, phenotype, and asserted mechanism

The MONDO ontology entry **MONDO:1010152** (label "autosomal dominant nebulin-related myopathy"; cross-reference GARD:0028130) defines the disease as *"any myopathy in which an autosomal dominantly inherited genetic variation in the NEB gene causes disease via a dominant-negative mechanism,"* with symptoms including *"distal muscle weakness, hypotonia, muscle fiber atrophy, foot drop, high arched palate, feeding difficulties, and type 1 fiber predominance."* This confirms NEB causation and the dominant, distal-predominant phenotype.

---

## Full Section-by-Section Report

### 1. Disease Information

**Overview.** Autosomal dominant nebulin-related myopathy is a rare inherited skeletal muscle disease caused by **heterozygous large multi-exon deletions of the NEB gene**. It presents as a **mild, slowly progressive distal myopathy** — distinct from the severe, proximal, congenital recessive nemaline myopathy type 2 (NEM2) caused by biallelic NEB variants.

**Key identifiers.**
- **Mondo:** MONDO:1010152 (autosomal dominant nebulin-related myopathy)
- **Causal gene:** NEB (HGNC:7720), chromosome 2q23.3
- **GARD:** 0028130 (cross-reference in MONDO)
- **Related OMIM:** NEM2 / 256030 (recessive nebulin nemaline myopathy); NEB gene OMIM 161650
- **ICD-11:** 8C70 (Primary disorders of muscles) / congenital myopathy category; **ICD-10:** G71.2 (congenital myopathies)
- **MeSH:** Myopathies, Nemaline (D017696)
- **Orphanet:** Nemaline myopathy (ORPHA:607) and distal myopathy subtypes

**Synonyms / alternative names:** NEB-related dominant distal myopathy; nebulin-related distal myopathy; distal nemaline/nebulin myopathy. (Formal synonyms "not recorded" per the template.)

**Information source:** Aggregated disease-level resources (OMIM, Orphanet, MONDO, HPO) combined with primary cohort and case-level literature (not EHR-derived).

### 2. Etiology

**Disease causal factors.** Purely **genetic** — heterozygous large multi-exon deletions (~52–97 exons) of NEB. No environmental, infectious, or acquired cause. (Note: an acquired, non-genetic mimic, sporadic late-onset nemaline myopathy [SLONM], is a separate entity frequently associated with monoclonal gammopathy — PMID 41270914 — and must not be confused with this inherited disease.)

**Genetic risk factors.** The causal variant class is the large heterozygous NEB deletion. Mosaicism (n=2/12 families) can also cause disease [PMID: 40517164](https://pubmed.ncbi.nlm.nih.gov/40517164/). No susceptibility loci or validated modifier genes are established for the dominant form; a modifier screen in recessive models failed to identify modifiers [PMID: 31530540](https://pubmed.ncbi.nlm.nih.gov/31530540/).

**Environmental / lifestyle risk and protective factors:** None established. No protective variants or alleles identified.

**Gene–environment interactions:** None documented.

### 3. Phenotypes

| Phenotype | Type | HPO term | Onset / severity / frequency |
|---|---|---|---|
| Distal muscle weakness (predominant) | Clinical sign | HP:0002460 | Childhood–adult; mild; distal predominance (~18/21 NEB-NM lower-limb cases) |
| Foot drop | Clinical sign | HP:0009027 | Chronic, slowly progressive |
| Muscle fiber atrophy | Pathology | HP:0009130 | Variable |
| Hypotonia | Clinical sign | HP:0001252 | Neonatal/childhood in congenital forms |
| High-arched palate | Physical | HP:0000218 | Congenital |
| Feeding difficulties | Symptom | HP:0011968 | Infancy (more severe forms) |
| Type 1 fiber predominance | Lab/pathology | HP:0003803 | Biopsy finding |
| Respiratory insufficiency | Clinical sign | HP:0002093 | Variable; 65% abnormal PFTs across NM cohort |
| Bulbar dysfunction | Clinical sign | HP:0001283 | Variable |
| Nemaline rods on biopsy | Lab/pathology | HP:0003798 | Diagnostic hallmark |

**Characteristics:** In the dominant distal form specifically, onset is typically childhood–adult, severity is **mild**, and progression is **slow/relatively stable** [PMID: 40517164](https://pubmed.ncbi.nlm.nih.gov/40517164/); [PMID: 33397769](https://pubmed.ncbi.nlm.nih.gov/33397769/). Distal lower-limb weakness with foot drop dominates. **Quality-of-life impact:** foot drop and distal weakness impair gait and daily mobility; respiratory and bulbar involvement, when present, drive the greatest QoL burden. Formal EQ-5D/SF-36 data for the dominant subtype are not available.

### 4. Genetic / Molecular Information

**Causal gene:** NEB (HGNC:7720; OMIM 161650), 2q23.3, ~183 exons, one of the largest human genes. Contains an 8-exon triplicate region (exons 82–105) and alternatively spliced exons.

**Pathogenic variants (dominant form):** Single **large heterozygous deletions** spanning **52–97 exons** (structural variants / large copy-number losses), classified pathogenic; 10/12 heterozygous, 2/12 mosaic [PMID: 40517164](https://pubmed.ncbi.nlm.nih.gov/40517164/). **Variant class:** multi-exon structural deletion (CNV). **Functional consequence:** loss of a large internal nebulin segment; mechanism debated between **haploinsufficiency** and **dominant-negative** (MONDO asserts dominant-negative).

**Recessive contrast (NEM2):** biallelic point mutations, small indels, splice variants, intragenic deletions/duplications, and triplicate-region gains; pathogenic variants represent only ~7% of NEB coding variants [PMID: 25205138](https://pubmed.ncbi.nlm.nih.gov/25205138/). The **exon 55 in-frame deletion** is the most common single disease variant and an Ashkenazi Jewish founder mutation [PMID: 23715096](https://pubmed.ncbi.nlm.nih.gov/23715096/).

**Allele frequency:** Large pathogenic NEB deletions are extremely rare/absent in gnomAD. **Origin:** germline (with documented mosaicism). **Modifier genes / epigenetics / chromosomal abnormalities:** none established for the dominant form.

### 5. Environmental Information

Not applicable — this is a monogenic disorder with no established environmental, lifestyle, or infectious contributors. (Acquired nemaline rod pathology exists as separate entities: SLONM/MGUS-associated and inflammatory "myositis with nemaline rods," PMID 42700620 — not relevant to the inherited NEB disease.)

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**

1. A **large heterozygous (or mosaic) deletion of 52–97 NEB exons** *leads to* loss of a substantial internal segment of nebulin and reduced/dysfunctional nebulin protein in the sarcomere. *(demonstrated: PMID 40517164)*
2. Reduced functional nebulin *results in* **failure of thin-filament length specification/stabilization** (loss of molecular-ruler and CapZ-anchoring function). *(demonstrated: PMID 35175800, 18272787)*
3. This *leads to* **shortened, non-uniform actin thin filaments** (~1.3 µm → ~0.75 µm in nebulin-deficient muscle). *(demonstrated: PMID 19346529)*
4. Shorter/non-uniform filaments *result in* **reduced thin–thick filament overlap and fewer force-generating crossbridges**, plus **reduced myofilament calcium sensitivity and altered crossbridge cycling kinetics**. *(demonstrated: PMID 21115852, 26123491)*
5. In parallel (branch), reduced nebulin *leads to* **destabilization of the myosin super-relaxed (SRX) state**, *resulting in* **increased resting ATP consumption and remodeling of the energy proteome** (glycogen accumulation, abnormal mitochondria). *(demonstrated: PMID 36528760)*
6. In another branch, muscle-type-dependent **upregulation of proteolysis (MuRF-1/MUSA1/Gadd45a)** *results in* atrophy of glycolytic-fiber-rich muscles. *(demonstrated in mouse: PMID 26123491)*
7. Steps 4–6 converge to *cause* a **~60% reduction in force-generating capacity** and the **clinical phenotype of mild, distal-predominant muscle weakness** with nemaline rods, type 1 fiber predominance, and atrophy. *(demonstrated: PMID 19346529, 40517164)*

Whether step 1→2 proceeds via haploinsufficiency or a dominant-negative poison effect of a truncated/internally-deleted nebulin is **inferred, not demonstrated**, for the dominant distal form.

**Molecular/cellular detail:** sarcomere thin-filament assembly and length regulation (GO:0030239 myofibril assembly; GO:0030240 skeletal muscle thin filament assembly; GO:0003009 skeletal muscle contraction); actin binding (GO:0003779); crossbridge cycling and ATP hydrolysis (GO:0030049 muscle filament sliding). **Cell type:** skeletal muscle fiber (CL:0000188 cell of skeletal muscle; CL:0008002 skeletal muscle fiber), with type 1 (slow oxidative) predominance. **Subcellular:** sarcomere / myofibril / Z-disc (GO:0030017 sarcomere; GO:0031674 I band; GO:0030018 Z disc; GO:0005865 striated muscle thin filament); mitochondria secondarily abnormal. **Metabolic:** elevated resting ATP turnover from SRX loss; glycogen accumulation (CHEBI:28087). No primary immune involvement.

### 7. Anatomical Structures Affected

- **Organ/system:** skeletal muscle / musculoskeletal system (UBERON:0001134 skeletal muscle tissue; UBERON:0002385 muscle tissue). **Body systems:** musculoskeletal (primary); respiratory (secondary — respiratory muscles); bulbar/oropharyngeal (secondary).
- **Primary muscles:** distal lower-limb muscles — **soleus, gastrocnemius** (greatest fatty infiltration on MRI), tibialis; gluteus maximus also involved [PMID: 40583855](https://pubmed.ncbi.nlm.nih.gov/40583855/). UBERON:0011907 (gastrocnemius), UBERON:0001388 (soleus).
- **Tissue/cell:** striated skeletal muscle fiber (CL:0000188); type 1 fiber predominance.
- **Subcellular:** sarcomere thin filament, Z-disc (GO:0030017; GO:0030018).
- **Lateralization:** bilateral, broadly symmetric.

### 8. Temporal Development

- **Onset:** childhood to adult for the dominant distal form; **insidious/chronic**. (Congenital/neonatal onset characterizes severe recessive NEM2, not the dominant distal form.)
- **Progression:** **slow**, relatively **stable** course; distal-predominant; disease duration is chronic/lifelong [PMID: 33397769](https://pubmed.ncbi.nlm.nih.gov/33397769/); [PMID: 40517164](https://pubmed.ncbi.nlm.nih.gov/40517164/). MRI fatty infiltration correlates with disease duration (r ≈ 0.57–0.60) [PMID: 40583855](https://pubmed.ncbi.nlm.nih.gov/40583855/).
- **Patterns:** progressive but non-episodic; no remission; critical intervention windows not defined.

### 9. Inheritance and Population

- **Inheritance:** **autosomal dominant** (single large heterozygous NEB deletion); mosaicism documented.
- **Epidemiology:** Nemaline myopathy overall ~**1 in 50,000 live births** (up to ~1 in 20,000 in some populations); NEB is the most common gene (>50%) [PMID: 31530540](https://pubmed.ncbi.nlm.nih.gov/31530540/). The dominant distal subtype is rarer; exact prevalence unknown (12 families in the defining study).
- **Penetrance/expressivity:** appears penetrant within affected families; expressivity variable (mild distal weakness).
- **Founder effects:** the exon-55 deletion is an Ashkenazi Jewish founder allele — but that is a **recessive** NEM2 allele, not the dominant deletion.
- **Carrier frequency/consanguinity:** relevant to recessive NEM2, not the dominant form. **Sex ratio:** no sex predilection expected for autosomal dominant inheritance.

### 10. Diagnostics

- **Muscle biopsy:** nemaline rods (Z-disc-derived electron-dense bodies) on light and electron microscopy; type 1 fiber predominance; ± cores (rod-core) [PMID: 25205138](https://pubmed.ncbi.nlm.nih.gov/25205138/); [PMID: 42609597](https://pubmed.ncbi.nlm.nih.gov/42609597/).
- **EMG:** myogenic (myopathic) pattern.
- **Muscle MRI:** distal-predominant fatty infiltration (soleus > gastrocnemius > gluteus maximus) [PMID: 40583855](https://pubmed.ncbi.nlm.nih.gov/40583855/).
- **Genetic testing:** NEB is very large and GC/repeat-rich, so **structural-variant-aware** approaches are essential — custom CGH arrays, short-read genome sequencing, droplet digital PCR, exome with CNV calling, and Sanger confirmation were all used to detect the large deletions [PMID: 40517164](https://pubmed.ncbi.nlm.nih.gov/40517164/). Standard exome panels can **miss** large NEB deletions; WGS/CMA/ddPCR improve detection.
- **Laboratory:** creatine kinase often normal or mildly elevated (nonspecific).
- **Differential diagnosis:** recessive NEM2; other thin-filament myopathies (ACTA1, TPM2, TPM3, TNNT1, KBTBD13, KLHL40/41); acquired SLONM (adult, monoclonal gammopathy); inflammatory myositis with rods. Distinguishing features: inheritance pattern, variant architecture, age/distribution of weakness, presence of monoclonal protein/inflammation.

### 11. Outcome / Prognosis

- The dominant distal form has a **favorable prognosis**: mild weakness, slow progression, generally preserved ambulation and life expectancy [PMID: 40517164](https://pubmed.ncbi.nlm.nih.gov/40517164/). This contrasts with severe recessive NEM2, which can cause neonatal respiratory failure and early death.
- Across the broader NM spectrum, morbidity includes mechanical support needs (58%), abnormal pulmonary function (65%), and bulbar dysfunction, but the course is *"relatively stable"* [PMID: 33397769](https://pubmed.ncbi.nlm.nih.gov/33397769/).
- **Prognostic factors:** variant architecture is the dominant determinant — large heterozygous deletions predict the mild distal phenotype [PMID: 40517164](https://pubmed.ncbi.nlm.nih.gov/40517164/). MRI fatty infiltration tracks disease duration.

### 12. Treatment

**No curative therapy exists; management is supportive** [PMID: 38866581](https://pubmed.ncbi.nlm.nih.gov/38866581/).

| Modality | Intervention | NCIT suggestion |
|---|---|---|
| Respiratory | Non-invasive ventilation, pulmonary monitoring | NCIT:C116838 (respiratory support) |
| Physical/orthotic | Physiotherapy, ankle-foot orthoses for foot drop | NCIT:C15719 (physical therapy) |
| Nutritional/bulbar | Feeding support, swallowing management | NCIT:C15285 (nutritional support) |
| Orthopedic | Scoliosis/contracture management | NCIT:C51696 (orthopedic procedure) |
| Investigational (Ca²⁺ sensitizer) | Fast skeletal troponin activator (CK-2066260) — restores Ca²⁺ sensitivity in patient fibers [PMID: 23572184] | — |
| Investigational (myosin modulator) | Mavacamten — reverses ATP overconsumption in vitro [PMID: 39216086] | — |

**Ineffective/unproven:** nutritional supplements — controlled model studies of L-tyrosine, L-carnitine, taurine, and creatine showed no significant functional benefit [PMID: 29848386](https://pubmed.ncbi.nlm.nih.gov/29848386/); [PMID: 30065346](https://pubmed.ncbi.nlm.nih.gov/30065346/). MuRF1 knockout increased muscle mass but not force [PMID: 35897687](https://pubmed.ncbi.nlm.nih.gov/35897687/). **Pharmacogenomics, gene/cell/RNA therapy, immunotherapy:** none established; gene replacement is impractical given nebulin's enormous size.

### 13. Prevention

- **Primary prevention:** not applicable (monogenic). **Genetic counseling** is the principal preventive tool — autosomal dominant transmission implies 50% offspring risk; mosaicism complicates recurrence-risk estimates [PMID: 40517164](https://pubmed.ncbi.nlm.nih.gov/40517164/).
- **Reproductive options:** prenatal testing and preimplantation genetic diagnosis are feasible once the familial deletion is defined.
- **Secondary/tertiary prevention:** surveillance of respiratory/bulbar function; orthotic and rehabilitation measures to prevent contractures and falls.
- **Immunization/public health:** not applicable.

### 14. Other Species / Natural Disease

- **Model species with NEB orthologs:** *Mus musculus* (Neb), *Danio rerio* (neb), *Gallus gallus* (chicken nebulin, sequenced and conserved — 74–91% identity in the C-terminal region) [PMID: 18522464](https://pubmed.ncbi.nlm.nih.gov/18522464/).
- **Natural disease in companion animals/wildlife:** no well-documented naturally occurring NEB nemaline myopathy reported in OMIA for this specific entity.
- **Evolutionary conservation:** nebulin's modular repeat structure, Z-line binding, and actin-binding regions are conserved across vertebrates, supporting cross-species mechanistic validity.
- **Zoonotic potential:** not applicable (genetic disease).

### 15. Model Organisms

| Model | Type | Key features / recapitulation | PMID |
|---|---|---|---|
| Conditional Neb-KO mouse (MCK-Cre) | Mammalian, conditional KO | <5% nebulin, nemaline rods, shortened thin filaments, reduced specific force, fiber-type switch, muscle-type-dependent atrophy | [26123491](https://pubmed.ncbi.nlm.nih.gov/26123491/) |
| Neb ΔExon55 mouse | Knock-in (founder mutation) | Growth retardation, nemaline bodies, reduced thin-filament length and force | [23715096](https://pubmed.ncbi.nlm.nih.gov/23715096/) |
| Novel Neb exon-55 deletion mouse | Knock-in | Recapitulates recurrent human variant | [40108735](https://pubmed.ncbi.nlm.nih.gov/40108735/) |
| Zebrafish neb allelic series | Vertebrate | Reduced survival, defective muscle structure, reduced force, shorter thin filaments, Z-disc thickening | [38493359](https://pubmed.ncbi.nlm.nih.gov/38493359/) |
| Patient-derived single myofibers | In vitro human | Force deficit, reduced Ca²⁺ sensitivity, SRX destabilization; used to test CK-2066260 and Mavacamten | [23572184](https://pubmed.ncbi.nlm.nih.gov/23572184/), [36528760](https://pubmed.ncbi.nlm.nih.gov/36528760/) |

**Limitations of models:** most model the **recessive/loss-of-function** biology; a model specifically reproducing the **dominant large heterozygous deletion** (to test haploinsufficiency vs dominant-negative) is a key gap. **Resources:** MGI (mouse), ZFIN (zebrafish), Alliance of Genome Resources.

---

## Mechanistic Model / Interpretation

```
  NEB large heterozygous deletion (52–97 exons; germline or mosaic)
                    │
                    ▼
      Reduced / internally-deleted nebulin in sarcomere
          (haploinsufficiency vs dominant-negative — UNRESOLVED)
                    │
        ┌───────────┼───────────────────────────────┐
        ▼           ▼                                ▼
  Loss of thin-   Destabilized myosin         Muscle-type-dependent
  filament ruler  super-relaxed (SRX) state   proteolysis (MuRF-1/
  & CapZ anchor        │                       MUSA1/Gadd45a)
        │              ▼                                │
        ▼        ↑ resting ATP use,                     ▼
  Short, non-    glycogen accumulation,           Fiber atrophy
  uniform thin   abnormal mitochondria       (glycolytic-rich muscles)
  filaments           │                                │
  (1.3→0.75 µm)       │                                │
        │             │                                │
        ▼             │                                │
  ↓ crossbridge       │                                │
  number, ↓ Ca²⁺      │                                │
  sensitivity,        │                                │
  altered kinetics    │                                │
        └─────────────┴────────────────────────────────┘
                    │
                    ▼
      ~60% loss of force-generating capacity
                    │
                    ▼
   MILD, DISTAL-PREDOMINANT, SLOWLY PROGRESSIVE MYOPATHY
   (foot drop, type 1 fiber predominance, nemaline rods)
```

The unifying interpretation is that **nebulin loss simultaneously corrupts thin-filament architecture and energetic homeostasis**. The thin-filament branch (shortening, reduced overlap, reduced Ca²⁺ sensitivity) is the primary driver of weakness; the SRX/energetic branch explains the otherwise puzzling metabolic histology; and the proteolytic branch explains muscle-type-dependent atrophy. The dominant distal phenotype's **mildness** likely reflects the **heterozygous dosage** (residual nebulin from the intact allele) compared with the near-complete loss in biallelic recessive disease — a model consistent with haploinsufficiency, though the MONDO curation's assertion of a dominant-negative mechanism remains to be directly tested.

---

## Evidence Base

| PMID | Title (abbrev.) | Role |
|---|---|---|
| [40517164](https://pubmed.ncbi.nlm.nih.gov/40517164/) | *Structural variation in nebulin... dominant distal phenotype* | **Defining study** — establishes dominant distal form from large heterozygous deletions |
| [39802796](https://pubmed.ncbi.nlm.nih.gov/39802796/) | *(preprint of above)* | Preprint corroboration |
| [35175800](https://pubmed.ncbi.nlm.nih.gov/35175800/) | *Structures from intact myofibrils... nebulin* | Molecular-ruler structural basis |
| [19346529](https://pubmed.ncbi.nlm.nih.gov/19346529/) | *Thin filament length dysregulation...* | Quantifies thin-filament shortening (1.3→0.75 µm) |
| [21115852](https://pubmed.ncbi.nlm.nih.gov/21115852/) | *Nebulin, a major player...* | Ca²⁺ sensitivity + crossbridge kinetics |
| [26123491](https://pubmed.ncbi.nlm.nih.gov/26123491/) | *Nebulin deficiency in adult muscle...* | Conditional KO; force deficit + proteolysis |
| [36528760](https://pubmed.ncbi.nlm.nih.gov/36528760/) | *NEB mutations disrupt super-relaxed state...* | Energetic/SRX branch |
| [23572184](https://pubmed.ncbi.nlm.nih.gov/23572184/) | *Troponin activator augments force...* | CK-2066260 restores Ca²⁺ sensitivity |
| [39216086](https://pubmed.ncbi.nlm.nih.gov/39216086/) | *Myosin ATPase inhibition fails to rescue...* | Mavacamten in vitro success / in vivo limit |
| [23715096](https://pubmed.ncbi.nlm.nih.gov/23715096/) | *Deleting exon 55...* | ΔExon55 mouse; Ashkenazi founder |
| [38493359](https://pubmed.ncbi.nlm.nih.gov/38493359/) | *Zebrafish allelic series...* | Vertebrate model recapitulation |
| [25205138](https://pubmed.ncbi.nlm.nih.gov/25205138/) | *Mutation update: spectra of nebulin variants* | Phenotypic spectrum incl. distal |
| [40583855](https://pubmed.ncbi.nlm.nih.gov/40583855/) | *Muscle MRI changes in NEB NM* | Distal MRI pattern |
| [33397769](https://pubmed.ncbi.nlm.nih.gov/33397769/) | *Cross-sectional study of NM* | Natural history, stability |
| [31530540](https://pubmed.ncbi.nlm.nih.gov/31530540/) | *Failure to identify modifiers...* | Epidemiology (1/50,000) |
| [38866581](https://pubmed.ncbi.nlm.nih.gov/38866581/) | *L-tyrosine for infant with NM* | Supportive-only management |
| [29848386](https://pubmed.ncbi.nlm.nih.gov/29848386/) | *Testing of therapies... lack of efficacy* | Supplements ineffective |
| [42609597](https://pubmed.ncbi.nlm.nih.gov/42609597/) | *Cohort of 49 nebulin-related CM* | Histological spectrum confirmation |
| [18272787](https://pubmed.ncbi.nlm.nih.gov/18272787/) | *Nebulin interacts with CapZ* | Z-disc anchoring |
| [26792324](https://pubmed.ncbi.nlm.nih.gov/26792324/) | *Nebulin, a multi-functional giant* | Multiple cellular roles |

**Evidence source types:** human clinical/genetic cohorts (40517164, 40583855, 33397769, 42609597, 25205138); human in vitro single-fiber mechanics (19346529, 23572184, 36528760); model organism (26123491, 23715096, 40108735, 38493359, 39216086); structural/computational (35175800, 18272787).

---

## Limitations and Knowledge Gaps

1. **Mechanism of dominance unresolved.** Whether large heterozygous NEB deletions cause disease by **haploinsufficiency** or a **dominant-negative** effect is not experimentally established for the dominant distal form. MONDO asserts dominant-negative, but no model specifically reproduces the heterozygous large deletion to test this.
2. **Small defining cohort.** The dominant distal entity is based on 12 families [PMID: 40517164]; precise prevalence, penetrance, expressivity, sex ratio, and long-term natural history are not yet quantified for this subtype specifically.
3. **Most functional/mechanistic data derive from recessive/KO models**, which may not fully capture the milder heterozygous biology.
4. **Detection challenges.** Large NEB deletions are easily missed by standard exome panels; the true frequency may be underestimated until SV-aware sequencing is routine.
5. **No disease-specific QoL or mortality datasets** for the dominant distal form.
6. **Therapeutics are preclinical.** Troponin activators and myosin modulators show in vitro promise but lack in vivo efficacy or clinical trial data for NEB disease.

---

## Proposed Follow-up Experiments / Actions

1. **Build a heterozygous large-deletion model** (mouse or patient iPSC-derived myotubes) replicating a representative 52–97-exon deletion to directly test **haploinsufficiency vs dominant-negative** — the single highest-priority mechanistic question.
2. **Quantify nebulin protein and isoform composition** from the intact allele in patient muscle (Western/mass spec) to assess residual function and dosage effects.
3. **Establish a dominant-distal NEB natural-history registry** capturing onset, progression (serial MRI, MFM), respiratory/bulbar outcomes, penetrance, and QoL (PROMIS/SF-36).
4. **Advance fast skeletal troponin activators** toward trial-readiness in NEB-specific models, given their mechanistic fit (restore Ca²⁺ sensitivity in patient fibers).
5. **Test longer-duration / combination myosin modulation** (Mavacamten ± metabolic support) since 4-week in vivo treatment failed to correct the energy proteome [PMID: 39216086].
6. **Standardize SV-aware diagnostic pipelines** (WGS/ddPCR/CGH) for NEB to improve detection of large dominant deletions and refine epidemiology.
7. **Genetic counseling protocols** addressing mosaicism-adjusted recurrence risk for families with large NEB deletions.

---

*Report compiled from 10 confirmed findings and 48 reviewed papers across 5 investigation iterations. Causal gene: **NEB** (nebulin), chromosome 2q23.3. Disease: **MONDO:1010152**, autosomal dominant nebulin-related myopathy.*


## Artifacts

- [OpenScientist final report](Autosomal_Dominant_Nebulin-Related_Myopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Autosomal_Dominant_Nebulin-Related_Myopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 26 |
| On topic | 21 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 18 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 14 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002460` (1 mention) - the report calls it "Clinical sign"; HP calls it **Distal muscle weakness**
- `HP:0009027` (1 mention) - the report calls it "Clinical sign"; HP calls it **Foot dorsiflexor weakness**
- `HP:0009130` (1 mention) - the report calls it "Pathology"; HP calls it **Hand muscle atrophy**
- `HP:0001252` (1 mention) - the report calls it "Clinical sign"; HP calls it **Hypotonia**
- `HP:0000218` (1 mention) - the report calls it "Physical"; HP calls it **High palate**
- `HP:0011968` (1 mention) - the report calls it "Symptom"; HP calls it **Feeding difficulties**
- `HP:0003803` (1 mention) - the report calls it "Lab/pathology"; HP calls it **Type 1 muscle fiber predominance**
- `HP:0002093` (1 mention) - the report calls it "Clinical sign"; HP calls it **Respiratory insufficiency**
- `HP:0001283` (1 mention) - the report calls it "Clinical sign"; HP calls it **Bulbar palsy**
- `HP:0003798` (1 mention) - the report calls it "Lab/pathology"; HP calls it **Nemaline bodies**
- `NCIT:C116838` (1 mention) - the report calls it "respiratory support"; NCIT calls it **CNS 2c**
- `NCIT:C15719` (1 mention) - the report calls it "physical therapy"; NCIT calls it **Surveillance**
- `NCIT:C15285` (1 mention) - the report calls it "nutritional support"; NCIT calls it **Nursing Research**
- `NCIT:C51696` (1 mention) - the report calls it "orthopedic procedure"; NCIT calls it **Orthotopic Liver Transplantation**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000188` (2 mentions) - the report calls it "Tissue/cell:** striated skeletal muscle fiber"; CL calls it **cell of skeletal muscle**
- `UBERON:0011907` (1 mention) - the report calls it "gastrocnemius"; UBERON calls it **gastrocnemius medialis**
- `UBERON:0001388` (1 mention) - the report calls it "soleus"; UBERON calls it **gastrocnemius**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `GARD`, `ORPHA`.