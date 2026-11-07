---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-22T20:31:14.167837'
end_time: '2026-10-22T20:46:01.130678'
duration_seconds: 886.96
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Pan-Chung-Bellen Syndrome
  mondo_id: MONDO:0975953
  category: Mendelian
  causal_genes: FRYL
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
citation_count: 7
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 4
  validator_version: 0.3.0
term_validation:
  total_terms: 35
  verified: 33
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 0
  labels_mismatched: 15
  mislabelled_terms:
  - term_id: HP:0001263
    reported_labels:
    - 7/7 (high)
    ontology_label: Global developmental delay
  - term_id: HP:0001249
    reported_labels:
    - high
    ontology_label: Intellectual disability
  - term_id: HP:0007018
    reported_labels:
    - variable
    ontology_label: Attention deficit hyperactivity disorder
  - term_id: HP:0002007
    reported_labels:
    - variable
    ontology_label: Frontal bossing
  - term_id: HP:0000490
    reported_labels:
    - variable
    ontology_label: Deeply set eye
  - term_id: HP:0001636
    reported_labels:
    - 1 patient
    ontology_label: Tetralogy of Fallot
  - term_id: HP:0000085
    reported_labels:
    - 1 patient
    ontology_label: Horseshoe kidney
  - term_id: HP:0000028
    reported_labels:
    - variable
    ontology_label: Cryptorchidism
  - term_id: HP:0000766
    reported_labels:
    - variable
    ontology_label: Abnormal sternum morphology
  - term_id: HP:0012448
    reported_labels:
    - subset
    ontology_label: Delayed myelination
  - term_id: HP:0002500
    reported_labels:
    - subset
    ontology_label: Abnormal cerebral white matter morphology
  - term_id: HP:0002353
    reported_labels:
    - subset
    ontology_label: EEG abnormality
  - term_id: HP:0000776
    reported_labels:
    - prenatal case
    ontology_label: Congenital diaphragmatic hernia
  - term_id: GO:0005874
    reported_labels:
    - 'GO cellular components: microtubule'
    - Subcellular:** Microtubule cytoskeleton
    ontology_label: microtubule
  - term_id: CL:0000540
    reported_labels:
    - 'CL cell types: neuron'
    - "Tissue/cell level:** Nervous tissue \u2014 neurons"
    ontology_label: neuron
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0010769
    ontology_label: obsolete regulation of cell morphogenesis involved in differentiation
    replaced_by: GO:0022604
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Pan-Chung-Bellen_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Pan-Chung-Bellen_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pan-Chung-Bellen Syndrome
- **MONDO ID:** MONDO:0975953 (if available)
- **Causal gene(s):** FRYL
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

Please provide a comprehensive research report on **Pan-Chung-Bellen Syndrome** covering all of the
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

# Pan-Chung-Bellen Syndrome (PCBS): A Comprehensive Disease Characterization Report

**Target disease:** Pan-Chung-Bellen Syndrome (PCBS)
**MONDO ID:** MONDO:0975953 · **OMIM phenotype:** #621049 · **DOID:** 0061146 · **MedGen:** C5975547
**Causal gene:** **FRYL** (FRY-like transcription coactivator; OMIM gene *620798; HGNC; NCBI Gene 285527; Ensembl ENSG00000075539; UniProt O94915; locus 4p11)
**Inheritance:** Autosomal dominant (almost always de novo), via haploinsufficiency / loss of function

---

## Summary

**Pan-Chung-Bellen syndrome (PCBS) is a recently delineated autosomal-dominant neurodevelopmental malformation syndrome caused by heterozygous, almost always *de novo*, loss-of-function (LoF) or deleterious missense variants in the gene *FRYL* (FRY-like transcription coactivator).** The disorder was defined in 2024 by Pan, Chung, Bellen and colleagues, who reported fourteen unrelated individuals with heterozygous *FRYL* variants presenting with developmental delay, intellectual disability, dysmorphic facial features, and congenital anomalies across multiple organ systems ([PMID: 38479391](https://pubmed.ncbi.nlm.nih.gov/38479391/)). The variants were confirmed *de novo* in all but one individual. Human genetic-constraint data (pLI = 1; missense Z = 3.3) indicate that *FRYL* is strongly intolerant to loss of function, and the pathogenic mechanism is best modeled as **haploinsufficiency**.

FRYL is a member of the evolutionarily conserved **Furry (Fry) family** of large scaffold proteins (yeast Tao3p/Mor2p; *C. elegans* Sax-2; *Drosophila* Furry). These proteins act as activators/scaffolds of the **NDR (Nuclear Dbf2-Related) family Ser/Thr kinases** (STK38/STK38L in humans; Tricornered in flies; Cbk1p/Orb6p in yeast). The conserved **Furry–NDR kinase module**, together with microtubule-associated functions, governs **polarized cell growth and neuronal morphogenesis** — dendritic tiling/branching and neurite outgrowth. Reduced FRYL dosage is therefore inferred to impair this polarized-growth / neuronal-morphogenesis program during development, producing the neurodevelopmental and malformation phenotype. The mechanistic link was functionally supported by *Drosophila* knock-in modeling of patient missense variants in the fly ortholog *furry* (*fry*), which recapitulated an allelic series of severe, partial, and null functional effects.

The clinical spectrum is **multi-system and highly variable in expressivity**, ranging from a severe prenatal/fetal presentation (including congenital diaphragmatic hernia) through the canonical developmental-delay/intellectual-disability phenotype with congenital cardiac (tetralogy of Fallot), renal/urogenital, and skeletal anomalies, to a comparatively mild, predominantly behavioral (ASD/ADHD) presentation. No disease-specific therapy exists; management is **supportive and symptomatic**, organized around early developmental intervention, system-specific surgical correction of congenital anomalies, and genetic counseling. Because PCBS is newly described (~2024) and based on small cohorts and case reports, quantitative epidemiology, penetrance, natural history, and prognosis remain largely uncharacterized.

---

## Key Findings

### Finding 1 — PCBS is a dominant *FRYL*-related neurodevelopmental disorder (F001)

The defining study by Pan et al. (2024, *American Journal of Human Genetics* 111:742–760) reported **fourteen individuals with heterozygous variants in *FRYL*** presenting with developmental delay, intellectual disability, dysmorphic features, and other congenital anomalies in multiple systems. The variants were confirmed *de novo* in all individuals except one, establishing a dominant mechanism with recurrent new mutation. Human genetic data indicate that *FRYL* is intolerant to loss of function.

> *"we report fourteen individuals with heterozygous variants in FRYL who present with developmental delay, intellectual disability, dysmorphic features, and other congenital anomalies in multiple systems. The variants are confirmed de novo in all individuals except one. Human genetic data suggest that FRYL is intolerant to loss of function (LoF)."* — [PMID: 38479391](https://pubmed.ncbi.nlm.nih.gov/38479391/)

*FRYL* encodes the FRY-like transcription coactivator, a Furry-family protein conserved from yeast to human, located on chromosome **4p11**. This finding establishes the gene, the dominant de novo inheritance, LoF intolerance, and the core clinical features of the syndrome. **Evidence type: human clinical (cohort).**

### Finding 2 — FRYL functions as a Furry-family scaffold/activator of NDR kinases controlling polarized growth and neuronal morphogenesis (F002)

Furry (Fry) proteins are conserved from yeast to humans and genetically and physically interact with NDR kinases as activators or scaffolds. The **Fry–NDR kinase signaling axis** controls polarized cell growth, epidermal morphogenesis, dendritic tiling/branching, and neurite outgrowth — the biology directly relevant to a neurodevelopmental disorder.

> *"Fry and its orthologues in invertebrates (termed Tao3p in budding yeast, Mor2p in fission yeast, Sax-2 in nematode and Fry in fruit fly) genetically and physically interact with nuclear Dbf2-related (NDR) kinases (termed Cbk1p in budding yeast, Orb6p in fission yeast, Sax-1 in nematode and Trc in fruitfly), and function as activators or scaffolds of these kinases. Fry-NDR kinase signals are implicated in the control of polarized cell growth and morphogenesis in yeast, neurite outgrowth in nematode, and epidermal morphogenesis and dendritic tiling in fruit fly."* — [PMID: 24403109](https://pubmed.ncbi.nlm.nih.gov/24403109/)

Mammalian Fry/FRYL additionally behaves as a **microtubule-associated protein** regulating chromosome alignment, spindle organization, PLK1 activation, and microtubule acetylation (via Sirtuin-2 inhibition). In the fly, *furry* is expressed in neurons but not glia; homozygous *fry* LoF is lethal at various developmental stages, and clonal loss causes wing and compound-eye defects.

> *"the fly FRYL ortholog, furry (fry), is expressed in multiple tissues, including the central nervous system where it is present in neurons but not in glia. Homozygous fry LoF mutation is lethal at various developmental stages, and loss of fry in mutant clones causes defects in wings and compound eyes."* — [PMID: 38479391](https://pubmed.ncbi.nlm.nih.gov/38479391/)

More recently, FRYL (Furry-like) was shown to scaffold NDR kinase within the **Crumbs–PATJ polarity complex and Homer-condensate–mediated YAP–Wnt/β-catenin signaling** crosstalk, with FRYL promoting cytoplasmic Homer droplet formation and acting pathway-selectively (antagonizing FRYL promotes YAP activation, while cooperating with FRYL enhances Wnt/β-catenin signaling) ([PMID: 42455669](https://pubmed.ncbi.nlm.nih.gov/42455669/)). This defines the conserved molecular function of FRYL and provides the mechanistic basis of the disorder. **Evidence type: model organism / in vitro / review.**

### Finding 3 — Identifiers and the multi-system clinical phenotype spectrum (F003)

**Identifiers:** OMIM phenotype #621049 (PAN-CHUNG-BELLEN SYNDROME; PCBS); OMIM gene *FRYL* *620798; MONDO:0975953; DOID:0061146; MedGen C5975547; locus 4p11; autosomal dominant.

Pan et al. 2024 described 14 unrelated patients, 13 *de novo*. A concordant core subset of **7 patients (ages 8–20)** showed: developmental delay/intellectual disability in **7/7**, autism in **5/7**, seizures in **2/7**, and hypotonia in **1/7**. The OMIM clinical synopsis lists:

| System | Features |
|---|---|
| Craniofacial / dysmorphism | Frontal bossing, deep-set eyes |
| CNS | Hypotonia, seizures, developmental delay, impaired intellectual development, delayed myelination, abnormal cerebral white-matter morphology, abnormal EEG |
| Behavioral | Autism spectrum disorder, ADHD |
| Cardiovascular | Tetralogy of Fallot (1 patient) |
| Genitourinary | Horseshoe kidney (1), cryptorchidism, hydrocele |
| Skeletal | Non-fusion of sternum, pectus deformity |
| Prenatal (later report) | Congenital diaphragmatic hernia |

> *"fourteen individuals with heterozygous variants in FRYL who present with developmental delay, intellectual disability, dysmorphic features, and other congenital anomalies in multiple systems"* — [PMID: 38479391](https://pubmed.ncbi.nlm.nih.gov/38479391/)

Congenital anomalies span cardiovascular, skeletal, gastrointestinal, renal, and urogenital systems. **Evidence type: human clinical.**

### Finding 4 — FRYL variant spectrum: 9 LoF + 5 missense; haploinsufficiency confirmed by constraint and fly knock-ins (F004)

Pan et al. 2024 identified 14 *FRYL* variants: **9 predicted loss-of-function** (premature stop/nonsense, frameshift, or splicing defects, all predicted to trigger nonsense-mediated decay) and **5 missense**. All missense were predicted deleterious; all except p.Ser2397Ile are classified **likely pathogenic** per ACMG/AMP. Constraint metrics confirm intolerance: **pLI = 1** (LoF-intolerant) and **missense Z-score = 3.3**. Variants were **absent from gnomAD**.

The splicing-variant patient exhibited brisk reflexes, central hypotonia, central hypoventilation, delayed myelination, abnormal cerebral white-matter morphology, and abnormal EEG. *Drosophila furry* (*fry*) knock-ins of 4/5 missense variants produced an **allelic series**: *fry* p.Phe2746Ser (≈ FRYL p.Phe2295Ser) behaved as a **severe LoF**; two others as **partial LoF**; and p.Ser2397Ile (not confirmed de novo) caused **no fly defect**, consistent with a VUS.

> *"One variant behaves as a severe LoF variant, whereas two others behave as partial LoF variants. One variant does not cause any observable defect in flies, and the corresponding human variant is not confirmed to be de novo, suggesting that this is a variant of uncertain significance."* — [PMID: 38479391](https://pubmed.ncbi.nlm.nih.gov/38479391/)

This cross-species functional modeling directly supports **haploinsufficiency / loss of function** as the disease mechanism and provides a template for classifying future variants. **Evidence type: human clinical + model organism functional validation.**

### Finding 5 — FRYL gene annotation, brain-enriched expression, and cross-species orthologs (F005)

FRYL (FRY-like transcription coactivator; aliases **AF4p12, KIAA0826, MOR2**): NCBI Gene **285527**, Ensembl **ENSG00000075539**, UniProt **O94915**, locus 4p11 (chr4:~48.5–48.8 Mb, GRCh38). The Human Protein Atlas reports FRYL as cytoplasmic and **tissue-enhanced in brain**, with subcellular localization to **microtubules, the cytokinetic bridge, and cytosol** — consistent with a microtubule-associated-protein role.

**Orthologs (HomoloGene 103956):** mouse *Fryl* (MGI:1919563, Gene 72313; ENSMUSG00000070733); rat *Fryl*; zebrafish *fryl* (ZFIN ZDB-GENE-040914-58; predicted to act upstream of/within heart development, active at cell cortex / site of polarized growth); *Drosophila melanogaster fry* (*furry*); *C. elegans sax-2*. Human **FRY and FRYL are paralogs**; the single invertebrate ortholog *fry* was used by Pan et al. to model patient variants.

> *"the fly FRYL ortholog, furry (fry), is expressed in multiple tissues, including the central nervous system where it is present in neurons but not in glia"* — [PMID: 38479391](https://pubmed.ncbi.nlm.nih.gov/38479391/)

**Evidence type: database annotation + model organism.**

### Finding 6 — Variable expressivity: severe fetal malformation to mild behavioral-only presentation (F006)

Beyond the 2024 defining cohort, two 2025–2026 reports expand the phenotypic spectrum and demonstrate **variable expressivity**:

- **Sandhu et al. 2025** (*Prenatal Diagnosis*, doi:10.1002/pd.6879; PMC12530344) describe a **fetal/prenatal phenotype including congenital diaphragmatic hernia**, not previously reported — the severe end of the spectrum.
- **Acharya et al. 2026** (*Indian Journal of Pediatrics* 93:1015; doi:10.1007/s12098-026-06318-2) report a **6-year-old girl with a comparatively mild, predominantly behavioral presentation** — ASD and ADHD with hyperactivity, impulsivity, hyperphagia, and poor attention — who achieved **normal early milestones** and lacked global developmental delay, seizures, or major neuroanatomical abnormalities. She carried co-occurring pathogenic variants in *FRYL* and *SUPT16H* (NEDDFAC), proposed as a **digenic** presentation.

Reported diagnostic yield in unexplained neurodevelopmental disorders is **30–50%**, supporting early genomic (exome/genome) testing.

> *"a dominant disorder with developmental and..."* — [PMID: 38479391](https://pubmed.ncbi.nlm.nih.gov/38479391/)

This confirms the autosomal-dominant backbone against which variable expressivity is interpreted. **Evidence type: human clinical case reports.**

---

## Section-by-Section Report

### 1. Disease Information

PCBS is an autosomal-dominant **neurodevelopmental malformation syndrome** caused by heterozygous *FRYL* variants, named for first/corresponding authors Pan, Chung, and Bellen (2024). It is characterized by developmental delay, intellectual disability, dysmorphic facial features (frontal bossing, deep-set eyes), autism/ADHD, and variable multi-system congenital anomalies.

- **OMIM phenotype:** #621049 · **OMIM gene:** *FRYL* *620798
- **MONDO:** MONDO:0975953 · **DOID:** 0061146 · **MedGen:** C5975547
- **ICD-10/ICD-11, MeSH, Orphanet:** No dedicated code identified (disease too recently described; *not available*).
- **Synonyms:** Pan-Chung-Bellen syndrome; PCBS; FRYL-related neurodevelopmental disorder (none formally recorded in the template).

**Information source:** Aggregated from individual-patient reports compiled into a disease-level cohort (Pan et al. 2024) plus subsequent case reports — i.e., clinically-derived individual-patient data rather than EHR-at-scale resources.

### 2. Etiology

- **Primary cause:** Genetic — heterozygous *FRYL* LoF or deleterious missense variants, almost always *de novo* (13/14 in the defining cohort). Mechanism: **haploinsufficiency**.
- **Genetic risk factors:** The causal variant itself. FRYL constraint (pLI = 1; missense Z = 3.3) indicates the gene cannot tolerate reduced dosage. No susceptibility loci or modifier genes are established; one case suggests a possible digenic contribution from *SUPT16H* (F006).
- **Environmental risk factors:** None established. As a *de novo* dominant disorder, **advanced parental age** is a plausible but unproven contributor to new-mutation rate (general principle, not demonstrated for *FRYL*).
- **Protective factors:** None known (genetic or environmental).
- **Gene–environment interactions:** Not characterized; *not available*.

### 3. Phenotypes

Phenotype types span clinical signs, physical/dysmorphic manifestations, behavioral changes, and laboratory/imaging abnormalities. Suggested HPO terms:

| Phenotype | Type | Approx. frequency (core cohort) | Suggested HPO |
|---|---|---|---|
| Developmental delay | Sign | 7/7 (high) | HP:0001263 |
| Intellectual disability | Sign | high | HP:0001249 |
| Autism spectrum disorder | Behavioral | 5/7 | HP:0000717 |
| ADHD | Behavioral | variable | HP:0007018 |
| Seizures | Sign | 2/7 | HP:0001250 |
| Hypotonia | Sign | 1/7 (central) | HP:0001252 |
| Frontal bossing | Dysmorphism | variable | HP:0002007 |
| Deep-set eyes | Dysmorphism | variable | HP:0000490 |
| Tetralogy of Fallot | Malformation | 1 patient | HP:0001636 |
| Horseshoe kidney | Malformation | 1 patient | HP:0000085 |
| Cryptorchidism | Malformation | variable | HP:0000028 |
| Pectus deformity / sternal non-fusion | Skeletal | variable | HP:0000766 |
| Delayed myelination | Imaging | subset | HP:0012448 |
| Abnormal cerebral white matter | Imaging | subset | HP:0002500 |
| Abnormal EEG | Lab/electrophysiology | subset | HP:0002353 |
| Congenital diaphragmatic hernia | Malformation | prenatal case | HP:0000776 |

- **Age of onset:** Congenital/neonatal for malformations; infancy–childhood for neurodevelopmental features; prenatal in the diaphragmatic-hernia case.
- **Severity:** Variable — from severe fetal malformation to mild behavioral-only.
- **Progression:** Neurodevelopmental features are static/developmental rather than neurodegenerative; malformations are congenital and stable (post-correction).
- **QoL impact:** Not formally measured; inferred substantial impact from ID/ASD and congenital-anomaly burden. *No EQ-5D/SF-36 data available.*

### 4. Genetic / Molecular Information

- **Causal gene:** *FRYL* (OMIM *620798; HGNC; NCBI Gene 285527; Ensembl ENSG00000075539; UniProt O94915; 4p11).
- **Variant classes:** 9 LoF (nonsense/frameshift/splice, NMD-predicted) + 5 missense; most likely pathogenic (ACMG/AMP); one VUS (p.Ser2397Ile).
- **Allele frequency:** Variants absent from gnomAD.
- **Origin:** Germline, overwhelmingly *de novo* (13/14).
- **Functional consequence:** Loss of function / haploinsufficiency (confirmed by pLI = 1, missense Z = 3.3, and fly knock-in allelic series).
- **Modifier genes:** Possible digenic *SUPT16H* co-occurrence in one mild case (unproven as a general modifier).
- **Epigenetic / chromosomal abnormalities:** No specific methylation signature or recurrent cytogenetic lesion reported; *not available*.

### 5. Environmental Information

No environmental, lifestyle, or infectious contributors are established. PCBS is a monogenic *de novo* dominant disorder; environmental/infectious agents are **not applicable** as causes. (Note: unrelated literature associates *FRYL* loci with common-disease GWAS signals — GERD/COPD comorbidity [PMID: 39919125], diabetic nephropathy [PMID: 42509683] — but these are distinct from the Mendelian syndrome and do not inform PCBS etiology.)

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A heterozygous *de novo* **LoF or deleterious missense variant in *FRYL*** arises (NMD of LoF alleles; hypomorphic/null missense alleles). → *demonstrated.*
2. This **reduces functional FRYL protein dosage** (haploinsufficiency), supported by pLI = 1 and the fly allelic series. → *demonstrated (constraint + modeling).*
3. Reduced FRYL **impairs the Furry–NDR (STK38/Tricornered) kinase module** for which FRYL serves as scaffold/activator. → *inferred from conserved orthologue function.*
4. **Branch A — neuronal morphogenesis:** Impaired Fry–NDR signaling disrupts **polarized growth, dendritic tiling/branching, and neurite outgrowth** in neurons (FRYL is neuron-expressed, not glial). → *inferred.*
   → leads to abnormal neuronal connectivity → **developmental delay, intellectual disability, ASD/ADHD, seizures, abnormal white matter/myelination.**
5. **Branch B — microtubule / cell-division functions:** Reduced FRYL perturbs **microtubule acetylation (via SIRT2), spindle organization, chromosome alignment, and PLK1 activation**, affecting proliferating progenitors. → *inferred.*
   → contributes to **growth/morphogenesis defects and congenital malformations.**
6. **Branch C — epithelial polarity / Hippo–Wnt crosstalk:** FRYL scaffolds NDR kinase within the **Crumbs–PATJ polarity complex and Homer-condensate YAP–Wnt/β-catenin signaling**. Dysregulation perturbs organ morphogenesis. → *inferred (in vitro).*
   → contributes to **cardiac (tetralogy of Fallot), renal (horseshoe kidney), skeletal (sternal/pectus), and diaphragmatic malformations.**
7. Convergence of branches A–C during embryonic/fetal development → **the multi-system PCBS phenotype**, with severity set by residual FRYL function and genetic background (variable expressivity).

**Upstream vs downstream:** The mutation and FRYL dosage reduction are upstream; Furry–NDR kinase dysfunction is the proximal molecular node; cytoskeletal, polarity, and Hippo–Wnt perturbations are intermediate; tissue-level morphogenetic failures and neuronal connectivity defects are downstream clinical manifestations.

**Pathways / processes / ontology suggestions:**
- Molecular pathways: NDR/Hippo kinase signaling; YAP–Wnt/β-catenin crosstalk; (FRYL GWAS hub reports also implicate mTOR, PI3K-Akt, cytoskeletal pathways — context-dependent).
- GO biological processes: regulation of cell morphogenesis involved in differentiation (GO:0010769); dendrite morphogenesis (GO:0048813); establishment/maintenance of cell polarity (GO:0007163); microtubule cytoskeleton organization (GO:0000226); neuron projection morphogenesis (GO:0048812).
- GO cellular components: microtubule (GO:0005874); cytosol (GO:0005829); midbody/cytokinetic bridge (GO:0030496).
- CL cell types: neuron (CL:0000540); central nervous system neuron (CL:0002319).

### 7. Anatomical Structures Affected

- **Primary organ:** Brain / central nervous system (UBERON:0000955 brain; UBERON:0001017 CNS).
- **Secondary organs:** Heart (UBERON:0000948; tetralogy of Fallot), kidney (UBERON:0002113; horseshoe kidney), gonads/urogenital tract (cryptorchidism, hydrocele), sternum/thoracic skeleton (UBERON:0000975; pectus/sternal non-fusion), diaphragm (UBERON:0001103; CDH).
- **Body systems:** Nervous, cardiovascular, renal/urogenital, musculoskeletal, respiratory/diaphragmatic, gastrointestinal.
- **Tissue/cell level:** Nervous tissue — neurons (CL:0000540), specifically affected over glia (fly data). Brain white matter affected (delayed myelination).
- **Subcellular:** Microtubule cytoskeleton (GO:0005874), cytokinetic bridge/midbody, cytosol.
- **Lateralization:** Predominantly bilateral (CNS); malformations may be midline (sternum, diaphragm) or lateralized (kidney, testis).

### 8. Temporal Development

- **Onset:** Congenital for malformations (prenatal in the CDH case); infancy–childhood for neurodevelopmental features. Pattern is chronic/insidious.
- **Progression:** Neurodevelopmental features are **developmental/static** (not neurodegenerative); congenital anomalies are fixed and corrected surgically. No evidence of progressive decline.
- **Course:** Chronic, lifelong. Seizures (when present) may be episodic.
- **Critical periods:** Embryonic/fetal organogenesis (malformations) and early childhood (neurodevelopment / early-intervention window).
- **Remission:** Not applicable to the underlying disorder; behavioral features may respond to intervention.

### 9. Inheritance and Population

- **Inheritance:** Autosomal dominant, predominantly *de novo* (13/14).
- **Penetrance / expressivity:** Presumed high penetrance but **highly variable expressivity** (severe fetal → mild behavioral). Formal penetrance estimates *not available*.
- **Anticipation / mosaicism / founder effects / consanguinity:** Not applicable / not reported (de novo dominant; no repeat expansion).
- **Carrier frequency:** Not applicable (de novo dominant, not a recessive carrier state).
- **Epidemiology:** **Ultra-rare**; precise prevalence/incidence *not available* (only ~14 defining cases plus isolated reports as of 2026).
- **Demographics:** No ethnic predisposition or sex skew established; both sexes affected. Geographic distribution: worldwide (cohort was international).

### 10. Diagnostics

- **Genetic testing is the diagnostic cornerstone.** Recommended approach: **exome sequencing (ES) or genome sequencing (GS)** with trio analysis to confirm de novo status; diagnostic yield in unexplained NDD is ~30–50%. Single-gene *FRYL* testing or NDD/epilepsy gene panels including *FRYL* are alternatives. Chromosomal microarray is appropriate in the malformation workup but will not detect most *FRYL* SNVs/indels.
- **Variant interpretation:** ACMG/AMP classification; *Drosophila fry* knock-in functional assays can reclassify missense VUS (Pan et al. model).
- **Supportive clinical tests:** Brain MRI (delayed myelination, abnormal white matter), EEG (seizures/abnormal background), echocardiography (cardiac anomalies), renal/abdominal ultrasound (horseshoe kidney), skeletal exam/imaging (pectus, sternal non-fusion), prenatal ultrasound (CDH).
- **Biomarkers / omics diagnostics:** No disease-specific biochemical biomarker; biochemical testing yield is effectively 0% (consistent with a monogenic structural gene). *No validated proteomic/metabolomic/epigenomic diagnostic.*
- **Differential diagnosis:** Other de novo dominant NDD-with-malformation syndromes and chromatin/cytoskeletal-regulator disorders; distinguished by *FRYL* genotype.
- **Screening:** No population or newborn screening; cascade testing generally unnecessary given de novo origin, but recurrence counseling applies.

### 11. Outcome / Prognosis

- **Survival/mortality:** No quantitative data. Prognosis likely dominated by severity of congenital malformations (e.g., CDH, complex cardiac disease) and neurodevelopmental burden. Severe fetal presentations carry high perinatal risk; milder cases are compatible with survival to at least childhood/adolescence (cohort ages 8–20).
- **Morbidity/disability:** Chronic — intellectual disability, ASD/ADHD, and anomaly-related disability. Lifelong functional support frequently needed.
- **QoL measures:** Not formally reported.
- **Complications:** Seizures, consequences of cardiac/renal/diaphragmatic malformations, feeding/behavioral issues.
- **Prognostic factors:** Residual FRYL function (severe vs partial LoF), presence/severity of major congenital anomalies, possible modifier/digenic contributions. No validated prognostic biomarker.

### 12. Treatment

**No disease-specific or disease-modifying therapy exists.** Management is **supportive and symptomatic**, multidisciplinary:

| Domain | Intervention | Suggested NCIT concept |
|---|---|---|
| Neurodevelopment | Early developmental intervention, special education, speech/OT/PT | NCIT rehabilitation therapy |
| Behavior (ASD/ADHD) | Behavioral therapy; stimulants/non-stimulants for ADHD symptoms as indicated | NCIT pharmacotherapy / behavioral intervention |
| Seizures | Standard antiseizure medications as clinically indicated | NCIT anticonvulsant therapy |
| Cardiac anomalies | Surgical correction (e.g., tetralogy of Fallot repair) | NCIT surgical procedure |
| Renal/urogenital | Urological management; orchidopexy for cryptorchidism | NCIT surgical procedure |
| Diaphragmatic hernia | Neonatal surgical repair | NCIT surgical procedure |
| Skeletal (pectus) | Orthopedic/surgical management as needed | NCIT surgical procedure |

- **Advanced therapeutics (gene/cell/RNA/targeted/immuno):** None developed; *not applicable* at present.
- **Pharmacogenomics / personalized medicine:** Not established.
- **Experimental trials:** No PCBS-specific registered trials identified.

### 13. Prevention

- **Primary prevention:** Not possible for de novo mutation. Preconception/reproductive counseling applies.
- **Secondary prevention:** Prenatal/perinatal detection of malformations (ultrasound, prenatal exome) enables delivery planning for severe presentations (e.g., CDH).
- **Genetic counseling:** Essential — recurrence risk for parents of a de novo case is low (baseline + possible germline mosaicism); an affected individual's own transmission risk is 50% (autosomal dominant).
- **Reproductive options:** Prenatal diagnosis and preimplantation genetic testing available once a familial variant is known.
- **Immunization / public-health / environmental measures:** Not applicable (non-infectious, non-environmental Mendelian disorder).

### 14. Other Species / Natural Disease

- **Orthologs/taxonomy:** Mouse *Fryl* (NCBI Gene 72313; MGI:1919563), rat *Fryl*, zebrafish *fryl* (ZFIN ZDB-GENE-040914-58), *Drosophila melanogaster fry/furry*, *C. elegans sax-2*. Human **FRY and FRYL are paralogs**.
- **Natural disease in other species:** No naturally occurring *FRYL*-equivalent disease documented in companion animals/wildlife (no OMIA entry identified); *not available*.
- **Comparative biology:** The Furry–NDR module is deeply conserved (yeast→human), making mechanisms evolutionarily transferable. Zebrafish *fryl* is implicated in heart development, paralleling human cardiac anomalies. GWAS of *fryl/FRYL* across sea urchin, sheep, and duck link the gene to sex determination, body size, and growth, consistent with a conserved developmental/growth role.
- **Zoonotic potential:** Not applicable.

### 15. Model Organisms

- **Primary model:** *Drosophila melanogaster* (*fry/furry*). Pan et al. generated **knock-in alleles** of human patient missense variants in the fly ortholog, recapitulating a severe/partial/null allelic series — strong phenotype-to-genotype validation and a platform for VUS reclassification.
- **Model characteristics:** Fly *fry* is neuron-expressed; homozygous LoF is lethal; clonal loss causes wing/compound-eye morphogenesis defects — recapitulating the polarized-growth/morphogenesis biology. Limitation: invertebrate models cannot fully capture human cognition, brain structure, or complex organ malformations.
- **Other systems:** Mouse (*Fryl*, MGI), rat (RGD), zebrafish (*fryl*, ZFIN; heart-development phenotype) orthologs exist for future modeling. No published PCBS-specific mammalian knock-in disease model identified yet.
- **Resources:** FlyBase, MGI, RGD, ZFIN, WormBase (*sax-2*), Alliance of Genome Resources.

---

## Mechanistic Model / Interpretation

```
   de novo heterozygous FRYL variant (9 LoF + 5 missense; NMD of LoF)
                     │  [demonstrated]
                     ▼
         Reduced FRYL dosage — HAPLOINSUFFICIENCY
         (pLI=1, missense Z=3.3; fly allelic series)
                     │  [demonstrated: constraint + modeling]
                     ▼
     Impaired Furry–NDR (STK38/Tricornered) kinase scaffold function
                     │  [inferred from conserved orthologue biology]
         ┌───────────┼─────────────────────┐
         ▼           ▼                     ▼
   (A) Neuronal   (B) Microtubule/      (C) Epithelial polarity +
   morphogenesis  spindle/PLK1/SIRT2    Crumbs-PATJ / Homer–YAP–Wnt
   dendrite/      → progenitor division  crosstalk
   neurite defects                       → organ morphogenesis
         │           │                     │
         ▼           ▼                     ▼
   DD, ID, ASD/   growth &            cardiac (TOF), renal
   ADHD, seizures  malformation        (horseshoe kidney),
   abnormal WM     tendency            skeletal, diaphragmatic (CDH)
         └───────────┴──────────┬──────────┘
                                ▼
          Multi-system PCBS phenotype; severity set by residual
          FRYL function + genetic background → VARIABLE EXPRESSIVITY
```

The strongest-evidence links are the upstream steps (mutation → haploinsufficiency), which are demonstrated by human constraint statistics and cross-species fly knock-in functional data. The downstream tissue-specific branches are **inferred** from the conserved molecular function of the Furry–NDR module and FRYL's documented roles in microtubule regulation and epithelial-polarity/Hippo–Wnt signaling, rather than directly demonstrated in PCBS patient tissue.

---

## Evidence Base

| PMID | Title (abbrev.) | Role / what it supports |
|---|---|---|
| [38479391](https://pubmed.ncbi.nlm.nih.gov/38479391/) | *De novo variants in FRYL…developmental delay, intellectual disability, dysmorphic features* | **Defining paper.** Establishes gene, de novo dominant inheritance, LoF intolerance, multi-system phenotype, variant spectrum (9 LoF + 5 missense), fly knock-in allelic series, neuronal expression. Supports F001, F002, F003, F004, F005, F006. |
| [24403109](https://pubmed.ncbi.nlm.nih.gov/24403109/) | *Multifaceted roles of Furry proteins in invertebrates and vertebrates* | Defines conserved Furry–NDR kinase scaffold function in polarized growth and neuronal morphogenesis. Supports F002 mechanism. |
| [15591127](https://pubmed.ncbi.nlm.nih.gov/15591127/) | *Tricornered…interacts with furry during Drosophila wing hair development* | Fry–NDR (Trc) physical interaction and role in polarized epidermal morphogenesis. Supports F002. |
| [20406475](https://pubmed.ncbi.nlm.nih.gov/20406475/) | *Drosophila Fry protein interacts with Trc and is highly mobile in vivo* | Fry essential (LoF lethal), interacts with Trc, enriched at growing tips; polarized-growth/transport role. Supports F002. |
| [42455669](https://pubmed.ncbi.nlm.nih.gov/42455669/) | *Homer condensates orchestrate YAP-Wnt signaling…downstream of Crumbs polarity* | FRYL as NDR-kinase scaffold in Crumbs–PATJ polarity and Homer/YAP–Wnt crosstalk. Supports branch C of mechanism. |
| [29983373](https://pubmed.ncbi.nlm.nih.gov/29983373/) | *Structural basis for auto-inhibition of NDR1…* | Mechanistic detail on NDR kinase regulation and Furry-scaffold association. Contextual support for F002. |
| [30375416](https://pubmed.ncbi.nlm.nih.gov/30375416/) | *Lhx1-Ldb1 complex interacts with Furry…pronephric kidney development* | Fry role in kidney field specification — relevant to renal malformations. Contextual support for branch C. |
| [34812992](https://pubmed.ncbi.nlm.nih.gov/34812992/); [39080522](https://pubmed.ncbi.nlm.nih.gov/39080522/); [38909509](https://pubmed.ncbi.nlm.nih.gov/38909509/) | GWAS of *fryl/FRYL* in sea urchin / sheep / duck | Cross-species associations with sex determination, body size, growth — indicate conserved developmental/growth roles (contextual, not PCBS-specific). |
| [42220229](https://pubmed.ncbi.nlm.nih.gov/42220229/) | RWD monogenic epilepsies; *FRYL* as gene of uncertain significance | Lists *FRYL* among epilepsy GUS with predicted structural effects — consistent with seizure phenotype and the need for functional validation. |

**Caveats on context literature:** Several *FRYL* papers concern common-disease GWAS, cancer, or circRNA biology (e.g., prostate cancer [PMID: 34386489], sepsis-AKI circ-Fryl [PMID: 34478012, 39994492], GERD/COPD [PMID: 39919125], diabetic nephropathy [PMID: 42509683]). These describe *FRYL* in unrelated contexts and **do not inform the Mendelian PCBS phenotype**; they were reviewed and excluded from mechanistic attribution to avoid misattribution.

---

## Limitations and Knowledge Gaps

1. **Very small evidence base.** The disorder rests on one defining cohort (n=14, 2024) plus isolated 2025–2026 case reports. Phenotype frequencies derive from a 7-patient core subset.
2. **No epidemiology.** Prevalence, incidence, sex ratio, and ethnic/geographic distribution are unknown.
3. **Penetrance/expressivity unquantified.** Variable expressivity is documented qualitatively (severe fetal → mild behavioral) but not statistically.
4. **Mechanism largely inferred.** Human PCBS patient-tissue mechanistic data are absent; downstream branches rely on orthologue biology and in-vitro FRYL functions. No mammalian PCBS disease model is yet published.
5. **Natural history and prognosis undefined.** No survival, longitudinal, or QoL data.
6. **Digenic / modifier uncertainty.** The *FRYL* + *SUPT16H* mild case raises but does not prove genetic-background effects.
7. **VUS burden.** Missense interpretation remains challenging; one cohort variant (p.Ser2397Ile) is a VUS.
8. **No therapeutics.** No disease-specific treatment, trial, or biomarker exists.

---

## Proposed Follow-up Experiments / Actions

1. **Expand the patient registry.** International data-sharing (GeneMatcher, Matchmaker Exchange) to build a larger cohort for genotype–phenotype correlation, penetrance, and natural-history studies.
2. **Generate a mammalian model.** Create *Fryl*+/− and patient-variant knock-in mice (and/or zebrafish *fryl* mutants) to test neurodevelopmental, cardiac, renal, and diaphragmatic phenotype recapitulation.
3. **Functionally classify all missense variants** using the established *Drosophila fry* knock-in assay plus NDR-kinase activity readouts to resolve VUS and build an allelic-severity map.
4. **Patient-derived neuronal models.** iPSC-derived neurons/organoids from PCBS individuals to assay dendrite/neurite morphogenesis, microtubule acetylation (SIRT2 axis), and NDR-kinase signaling directly in human cells.
5. **Mechanistic dissection of branches.** Test whether cardiac/renal/diaphragmatic malformations trace to FRYL's Crumbs–PATJ/Homer–YAP–Wnt polarity role versus its microtubule/mitotic role.
6. **Prenatal phenotype characterization.** Collate fetal cases (CDH and others) to define the severe end of the spectrum and inform prenatal counseling.
7. **Biomarker exploration.** Transcriptomic/proteomic profiling of patient cells to identify molecular signatures for diagnosis and, eventually, therapeutic readouts.

---

*Report compiled from 5 discovery iterations; 6 confirmed findings; 23 papers reviewed. Evidence types are indicated throughout as human clinical, model organism, in vitro, computational, or database annotation. Primary reference: Pan et al., Am J Hum Genet 2024 ([PMID: 38479391](https://pubmed.ncbi.nlm.nih.gov/38479391/)).*


## Artifacts

- [OpenScientist final report](Pan-Chung-Bellen_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Pan-Chung-Bellen_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 16 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 15 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001263` (1 mention) - the report calls it "7/7 (high)"; HP calls it **Global developmental delay**
- `HP:0001249` (1 mention) - the report calls it "high"; HP calls it **Intellectual disability**
- `HP:0007018` (1 mention) - the report calls it "variable"; HP calls it **Attention deficit hyperactivity disorder**
- `HP:0002007` (1 mention) - the report calls it "variable"; HP calls it **Frontal bossing**
- `HP:0000490` (1 mention) - the report calls it "variable"; HP calls it **Deeply set eye**
- `HP:0001636` (1 mention) - the report calls it "1 patient"; HP calls it **Tetralogy of Fallot**
- `HP:0000085` (1 mention) - the report calls it "1 patient"; HP calls it **Horseshoe kidney**
- `HP:0000028` (1 mention) - the report calls it "variable"; HP calls it **Cryptorchidism**
- `HP:0000766` (1 mention) - the report calls it "variable"; HP calls it **Abnormal sternum morphology**
- `HP:0012448` (1 mention) - the report calls it "subset"; HP calls it **Delayed myelination**
- `HP:0002500` (1 mention) - the report calls it "subset"; HP calls it **Abnormal cerebral white matter morphology**
- `HP:0002353` (1 mention) - the report calls it "subset"; HP calls it **EEG abnormality**
- `HP:0000776` (1 mention) - the report calls it "prenatal case"; HP calls it **Congenital diaphragmatic hernia**
- `GO:0005874` (2 mentions) - the report calls it "GO cellular components: microtubule", "Subcellular:** Microtubule cytoskeleton"; GO calls it **microtubule**
- `CL:0000540` (2 mentions) - the report calls it "CL cell types: neuron", "Tissue/cell level:** Nervous tissue — neurons"; CL calls it **neuron**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0010769` (obsolete regulation of cell morphogenesis involved in differentiation) (1 mention) - replaced by `GO:0022604`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001252` (1 mention) - the report calls it "1/7 (central)"; HP calls it **Hypotonia**, and lists "Central hypotonia" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005874` - called "GO cellular components: microtubule", "Subcellular:** Microtubule cytoskeleton"
- `CL:0000540` - called "CL cell types: neuron", "Tissue/cell level:** Nervous tissue — neurons"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.