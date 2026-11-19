---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-05T00:58:31.144245'
end_time: '2026-11-05T01:22:59.306506'
duration_seconds: 1468.16
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Tessadori-Van Haaften Neurodevelopmental Syndrome 3
  mondo_id: MONDO:0030993
  category: Mendelian
  causal_genes: H4C5
  omim_id: OMIM:619950
  synonyms: TEVANED3
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
citation_count: 11
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 12
  validator_version: 0.5.1
term_validation:
  total_terms: 27
  verified: 26
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 1
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: HP:0001249
    reported_labels:
    - Cognitive/behavioral
    ontology_label: Intellectual disability
  - term_id: HP:0000252
    reported_labels:
    - Physical/clinical sign
    ontology_label: Microcephaly
  - term_id: HP:0004322
    reported_labels:
    - Physical
    ontology_label: Short stature
  - term_id: HP:0001999
    reported_labels:
    - Physical
    ontology_label: Abnormal facial shape
  - term_id: HP:0001250
    reported_labels:
    - Clinical sign
    ontology_label: Seizure
  - term_id: CL:0000540
    reported_labels:
    - Suggested CL terms:** neuron
    ontology_label: neuron
  - term_id: NCIT:C19236
    reported_labels:
    - Suggested NCIT terms:** Supportive Care
    ontology_label: Physical Chemical Technique
  labels_variant: 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Tessadori-Van_Haaften_Neurodevelopmental_Syndrome_3-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Tessadori-Van_Haaften_Neurodevelopmental_Syndrome_3-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Tessadori-Van Haaften Neurodevelopmental Syndrome 3
- **MONDO ID:** MONDO:0030993 (if available)
- **Causal gene(s):** H4C5
- **OMIM:** OMIM:619950
- **Synonyms:** TEVANED3
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Tessadori-Van Haaften Neurodevelopmental Syndrome 3** covering all of the
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

# Tessadori–Van Haaften Neurodevelopmental Syndrome 3 (TEVANED3): Comprehensive Disease Characteristics Report

**Disease:** Tessadori–Van Haaften Neurodevelopmental Syndrome 3 (TEVANED3)
**MONDO:** MONDO:0030993 · **OMIM:** 619950 · **Causal gene:** **H4C5** (formerly *HIST1H4E*; HGNC:4790; NCBI Gene 8367; Ensembl ENSG00000276966; locus 6p22.2)
**Category:** Mendelian, autosomal dominant (de novo)

---

## Summary

**Tessadori–Van Haaften Neurodevelopmental Syndrome 3 (TEVANED3) is an ultra-rare autosomal-dominant neurodevelopmental disorder caused by heterozygous *de novo* missense variants in the canonical histone H4 gene H4C5** (formerly *HIST1H4E*). H4C5 is one of 14 human genes that each encode the identical histone H4 protein. Because the protein is invariant, pathology does not arise from simple haploinsufficiency but from a *dominant* effect of the mutant histone, which is still produced and incorporated into chromatin. TEVANED3 is one member of an allelic series of "H4 histonopathies" first delineated by Tessadori and colleagues in 2022, in which recurrent de novo missense variants spread across at least six H4 genes (H4C3, H4C4, **H4C5**, H4C6, H4C9, H4C11) produce an overlapping syndrome ([PMID: 35202563](https://pubmed.ncbi.nlm.nih.gov/35202563/)).

The core clinical phenotype is **intellectual disability with motor and/or global developmental delay in essentially all affected individuals**, accompanied by a variable constellation of non-neurological features including microcephaly, short stature, facial dysmorphism, and structural anomalies. At least one well-documented H4C5 case (p.Tyr99His) presented with autism, developmental delay, microcephaly, and a "happy demeanor" that clinically mimicked Angelman syndrome, underscoring an important differential diagnosis ([PMID: 36987712](https://pubmed.ncbi.nlm.nih.gov/36987712/)).

Mechanistically, the disease-causing variants cluster in the globular core of histone H4 at surfaces that mediate histone–histone and histone–chaperone contacts. Incorporation of the altered H4 **destabilizes the nucleosome** and perturbs chromatin assembly, dysregulating chromatin-templated transcription, replication, cell-cycle progression, and DNA-damage repair during development. In zebrafish, H4 disease variants reproduce abnormal development, defective head structures, and shortened body axis. TEVANED3 is a **static (non-progressive)** developmental disorder; diagnosis rests on **trio exome/genome sequencing**; and management is entirely **supportive and multidisciplinary** with no disease-specific therapy. Because the germline histonopathy cancer incidence is ~1% (below the 5% threshold), routine tumor surveillance is not currently recommended.

---

## Key Findings

### Finding 1 — TEVANED3 is caused by de novo missense variants in H4C5, one of 14 canonical histone H4 genes

Tessadori et al. (2022) identified a cohort of **29 subjects with de novo missense variants across six histone H4 genes** (H4C3, H4C4, **H4C5**, H4C6, H4C9, H4C11), defining a new neurodevelopmental syndrome family. H4C5 — with prior symbol *HIST1H4E*, reference transcript NM_003545.4 — is the specific gene assigned to **OMIM 619950 / MONDO:0030993 (TEVANED3)**. All H4 genes encode an identical protein, so the disorder arises not from loss of one gene copy but from a heterozygous *de novo* missense change that produces an altered histone which is still deposited into chromatin — a dominant, likely dominant-negative/gain-of-function mechanism. A specific example pathogenic H4C5 variant is c.295T>C p.(Tyr99His), confirmed de novo and classified likely pathogenic ([PMID: 36987712](https://pubmed.ncbi.nlm.nih.gov/36987712/)).

> *"All individuals present with neurodevelopmental features of intellectual disability and motor and/or gross developmental delay, while non-neurological features are more variable."* — [PMID: 35202563](https://pubmed.ncbi.nlm.nih.gov/35202563/)

> *"Genome sequencing identified the H4 histone gene variant H4C5 NM_003545.4: c.295T>C, p.Tyr99His, which parental testing confirmed to be de novo."* — [PMID: 36987712](https://pubmed.ncbi.nlm.nih.gov/36987712/)

Gene identifiers were independently verified via mygene.info/NCBI: **H4C5** ("H4 clustered histone 5"); prior symbol *HIST1H4E*; **HGNC:4790**; **NCBI Gene 8367**; **Ensembl ENSG00000276966**; locus **6p22.2** (GRCh38 chr6:26,204,610–26,205,021, + strand). Notably, the gene's own NCBI alias list includes "TEVANED3" and "TEBIVANED3", directly confirming the gene–disease link.

### Finding 2 — Core clinical phenotype: intellectual disability and developmental/motor delay, with variable microcephaly, short stature, and dysmorphism

Across the 29-subject H4 cohort, **all** individuals had neurodevelopmental features (intellectual disability and motor and/or gross developmental delay), while non-neurological features — short stature, microcephaly, facial dysmorphisms, and structural anomalies — were **more variable** ([PMID: 35202563](https://pubmed.ncbi.nlm.nih.gov/35202563/)). An independent H4C5 case presented with autism, developmental delay, microcephaly, and a "happy demeanor" clinically suspected to be Angelman syndrome (Angelman molecular testing negative) ([PMID: 36987712](https://pubmed.ncbi.nlm.nih.gov/36987712/)). Analogous H4 syndromes caused by variants in other H4 genes (e.g., *HIST1H4J*/H4C11, and *HIST1H4C* p.K91 substitutions) show growth delay, microcephaly, profound intellectual disability, and dysmorphic facies ([PMID: 31804630](https://pubmed.ncbi.nlm.nih.gov/31804630/)).

> *"A 4-year-old male with autism, developmental delay, microcephaly, and a happy demeanor underwent evaluation through the Undiagnosed Disease Network. He was clinically suspected to have Angelman syndrome; however, molecular testing was negative."* — [PMID: 36987712](https://pubmed.ncbi.nlm.nih.gov/36987712/)

> *"We report here a de novo missense variant in HIST1H4J resulting in a complex syndrome combining growth delay, microcephaly and intellectual disability."* — [PMID: 31804630](https://pubmed.ncbi.nlm.nih.gov/31804630/)

**Suggested HPO terms:** Intellectual disability (HP:0001249); Global developmental delay (HP:0001263); Motor delay (HP:0001270); Microcephaly (HP:0000252); Short stature (HP:0004322); Autistic behavior (HP:0000729); Abnormal facial shape (HP:0001999); Seizure (HP:0001250, where present); Muscular hypotonia (HP:0001252, by analogy with related histonopathies).

### Finding 3 — Mechanism: H4 missense variants destabilize the nucleosome and disrupt histone–chaperone interactions, impairing chromatin-dependent development

The disease variants **cluster to specific regions of the H4 core globular domain** where protein–protein interactions occur with other histone subunits or histone chaperones ([PMID: 35202563](https://pubmed.ncbi.nlm.nih.gov/35202563/)). The recurrently affected residue **H4K91** lies at the (H3–H4)₂ tetramer / H2A–H2B dimer interface; biochemical work shows that modification or substitution at H4K91 **destabilizes the nucleosome in vitro** and perturbs chromatin structure, transcription, cell-cycle progression, DNA-damage repair, and telomere silencing ([PMID: 31542297](https://pubmed.ncbi.nlm.nih.gov/31542297/)). In zebrafish embryos, H4 disease variants caused abnormal general development, defective head organs, and reduced body-axis length ([PMID: 35202563](https://pubmed.ncbi.nlm.nih.gov/35202563/); [PMID: 31804630](https://pubmed.ncbi.nlm.nih.gov/31804630/)).

> *"These variants cluster to specific regions of the core H4 globular domain, where protein-protein interactions occur with either other histone subunits or histone chaperones."* — [PMID: 35202563](https://pubmed.ncbi.nlm.nih.gov/35202563/)

> *"an evolutionarily conserved Kglu at histone H4K91 destabilizes nucleosome in vitro"* and *"results in a global upregulation of transcription and defects in cell-cycle progression, DNA damage repair, and telomere silencing"* — [PMID: 31542297](https://pubmed.ncbi.nlm.nih.gov/31542297/)

### Finding 4 — H4C5 syndrome belongs to the emerging class of germline "histonopathies" with shared NDD features and episignature potential

A pan-histonopathy study of **192 individuals** analyzed germline histone-variant disorders including Tessadori–Bicknell–van Haaften NDD, *HIST1H1E* (Rahman) syndrome, and Bryant–Li–Bhoj syndrome (histone H3.3) ([PMID: 40241305](https://pubmed.ncbi.nlm.nih.gov/40241305/)). Across this community, the cancer incidence is ~1%, below the 5% surveillance threshold. Related chromatin-regulator NDDs (MSL2, SET, KMT2B, DMAP1, and others) have established DNA-methylation **episignatures** used to classify variants of uncertain significance ([PMID: 38815585](https://pubmed.ncbi.nlm.nih.gov/38815585/); [PMID: 42322191](https://pubmed.ncbi.nlm.nih.gov/42322191/); [PMID: 39933316](https://pubmed.ncbi.nlm.nih.gov/39933316/); [PMID: 42275155](https://pubmed.ncbi.nlm.nih.gov/42275155/)), indicating that episignature approaches are being extended across chromatin/histone disorders.

> *"Mendelian histonopathies are rare neurodevelopmental disorders (NDDs) caused by germline variants in histone-encoding genes."* and *"the community-wide cancer incidence is currently 1%, which falls below the recommended 5% cut off for routine surveillance"* — [PMID: 40241305](https://pubmed.ncbi.nlm.nih.gov/40241305/)

### Finding 5 — TEVANED3 is static, diagnosed by trio WES/WGS, managed supportively, with no cancer surveillance indicated

Diagnosis relies on **trio whole-exome/whole-genome sequencing** demonstrating a de novo H4C5 missense variant; targeted single-gene, karyotype, microarray, and repeat-expansion tests are non-diagnostic and serve mainly to exclude mimics. The condition is a **static developmental disorder** with no reported neurodegeneration — contrasting with the H3.3 Bryant–Li–Bhoj syndrome, which was initially characterized as progressive ([PMID: 38678163](https://pubmed.ncbi.nlm.nih.gov/38678163/)). No disease-modifying therapy exists; care is supportive/multidisciplinary (physical, occupational, and speech therapy; special education; anti-seizure medication as needed). Routine tumor surveillance is not recommended ([PMID: 40241305](https://pubmed.ncbi.nlm.nih.gov/40241305/)). Angelman syndrome is the key differential ([PMID: 36987712](https://pubmed.ncbi.nlm.nih.gov/36987712/)).

> *"cases of clinically suspected Angelman syndrome without molecular confirmation should undergo exome or genome sequencing"* — [PMID: 36987712](https://pubmed.ncbi.nlm.nih.gov/36987712/)

### Finding 6 — Verified H4C5 gene identifiers and ClinVar variant landscape

ClinVar contains **~75 H4C5 variants** on transcript NM_003545.4. Only a few are classified **Pathogenic** (c.113T>C p.Leu38Pro; c.121C>T p.Arg41Cys) or **Likely pathogenic** (c.81C>G p.Ile27Met), with the majority classified **Variant of Uncertain Significance** and some synonymous **Benign/Likely benign**. The published case variant c.295T>C p.(Tyr99His) was classified likely pathogenic ([PMID: 36987712](https://pubmed.ncbi.nlm.nih.gov/36987712/)).

---

## Section-by-Section Report

### 1. Disease Information

TEVANED3 is an ultra-rare Mendelian neurodevelopmental syndrome defined by intellectual disability and developmental delay arising from a de novo missense variant in the histone H4 gene **H4C5**. **Key identifiers:** OMIM 619950; MONDO:0030993; synonym **TEVANED3** (and the variant abbreviation TEBIVANED3); gene alias *HIST1H4E* (prior symbol). An explicit Orphanet code, ICD-10/ICD-11, and MeSH term were not established for this specific serial-numbered subtype in the materials reviewed; it falls under the broad umbrella of "histone H4–related neurodevelopmental disorders." Information is derived from **aggregated disease-level resources** (OMIM, ClinVar) plus **individual published patient reports** (notably the 29-subject cohort of [PMID: 35202563](https://pubmed.ncbi.nlm.nih.gov/35202563/) and the single H4C5 case of [PMID: 36987712](https://pubmed.ncbi.nlm.nih.gov/36987712/)), not from EHR-scale data.

**Synonyms/related terms:** TEVANED3; TEBIVANED3; Tessadori–Bicknell–van Haaften neurodevelopmental syndrome (series); H4C5-related / histone H4–related neurodevelopmental disorder.

### 2. Etiology

**Disease causal factor:** purely genetic — a heterozygous *de novo* missense variant in H4C5. There is no known environmental, infectious, or multifactorial contribution to disease causation.

**Genetic risk factors:** the causal variant itself; because events are de novo, there is no inherited susceptibility locus or modifier gene established for TEVANED3. Advanced parental age is a general risk factor for de novo mutations but has not been specifically quantified here.

**Protective factors:** none identified (genetic or environmental).

**Gene–environment interactions:** none established. A broader observation across histonopathies is that histones sit "at the interface of genetics and epigenetics," raising the theoretical possibility of gene–environment modulation of phenotype, but this remains speculative ([PMID: 38678163](https://pubmed.ncbi.nlm.nih.gov/38678163/)).

### 3. Phenotypes

| Phenotype | Type | HPO term | Frequency | Onset | Severity/Course |
|---|---|---|---|---|---|
| Intellectual disability | Cognitive/behavioral | HP:0001249 | Essentially all (core) | Childhood | Variable; static |
| Global/motor developmental delay | Developmental | HP:0001263 / HP:0001270 | Essentially all (core) | Infancy–childhood | Variable; static |
| Microcephaly | Physical/clinical sign | HP:0000252 | Variable | Congenital/early | Non-progressive |
| Short stature | Physical | HP:0004322 | Variable | Childhood | Stable |
| Facial dysmorphism | Physical | HP:0001999 | Variable | Congenital | Stable |
| Autistic behavior | Behavioral | HP:0000729 | Subset (e.g., p.Tyr99His case) | Childhood | Stable |
| Seizures | Clinical sign | HP:0001250 | Subset | Variable | Episodic |
| "Happy demeanor" (Angelman-like) | Behavioral | — | Reported in H4C5 case | Childhood | Stable |

Neurodevelopmental features are the **penetrant core**; non-neurological features are variably expressed. All features are consistent with a **static (non-progressive)** course. **Quality-of-life impact:** substantial and lifelong, driven by intellectual disability and motor impairment affecting independence, communication, and education; formal QoL instruments (EQ-5D, SF-36, PROMIS) have not been applied in this ultra-rare condition.

### 4. Genetic/Molecular Information

- **Causal gene:** H4C5 (HGNC:4790; NCBI Gene 8367), locus 6p22.2, transcript NM_003545.4; protein product histone H4 (UniProt P62805), identical across all 14 H4 genes.
- **Variant class:** heterozygous **missense**, **de novo**, germline. Because all H4 genes encode an identical protein, the pathogenic effect is a **dominant** consequence of the altered histone (dominant-negative / gain-of-function rather than haploinsufficiency).
- **Representative pathogenic/likely-pathogenic variants:** c.295T>C p.(Tyr99His) (likely pathogenic, de novo; [PMID: 36987712](https://pubmed.ncbi.nlm.nih.gov/36987712/)); c.113T>C p.(Leu38Pro) and c.121C>T p.(Arg41Cys) (Pathogenic, ClinVar); c.81C>G p.(Ile27Met) (Likely pathogenic, ClinVar).
- **ClinVar landscape:** ~75 H4C5 variants; a minority pathogenic/likely pathogenic, the majority VUS, plus benign synonymous variants.
- **Allele frequency:** pathogenic variants are absent from population databases (de novo, under strong negative selection); H4 genes are highly constrained in gnomAD.
- **Functional consequence:** nucleosome destabilization / impaired chromatin assembly (see Mechanism).
- **Modifier genes / epigenetics / chromosomal abnormalities:** none specifically established for TEVANED3. By analogy with related chromatin disorders, a disease-specific **DNA-methylation episignature** is plausible but has not yet been formally validated for H4C5.

### 5. Environmental Information

Not applicable. TEVANED3 is a monogenic de novo disorder with **no environmental, lifestyle, or infectious contributors** to causation. (For context only, valproic acid is a histone-pathway-modulating teratogen in pregnancy, but it is unrelated to the causation of TEVANED3 — [PMID: 38203562](https://pubmed.ncbi.nlm.nih.gov/38203562/).)

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**

1. A **de novo missense variant in H4C5** arises in the germline → produces an **altered but still-expressed histone H4 protein**.
2. The altered H4, **identical in sequence to that from 13 other H4 genes except at the mutated residue**, is **incorporated into nucleosomes** during chromatin assembly (dominant mechanism; the wild-type copies cannot prevent incorporation of mutant protein).
3. Because the variants sit at **core globular-domain surfaces that contact other histone subunits or histone chaperones** (demonstrated clustering; [PMID: 35202563](https://pubmed.ncbi.nlm.nih.gov/35202563/)) → **histone–histone and histone–chaperone interactions are disrupted** and the **nucleosome is destabilized** (demonstrated biochemically for the recurrently affected H4K91 interface residue; [PMID: 31542297](https://pubmed.ncbi.nlm.nih.gov/31542297/)).
4. Nucleosome/chromatin destabilization → **dysregulated chromatin-templated processes**: global transcriptional changes, impaired cell-cycle progression, defective DNA-damage repair, and altered telomere silencing (demonstrated in model systems; [PMID: 31542297](https://pubmed.ncbi.nlm.nih.gov/31542297/)).
5. During embryogenesis, disrupted chromatin regulation → **abnormal developmental gene-expression programs** → (demonstrated in zebrafish) abnormal general development, defective head organs, and shortened body axis ([PMID: 35202563](https://pubmed.ncbi.nlm.nih.gov/35202563/); [PMID: 31804630](https://pubmed.ncbi.nlm.nih.gov/31804630/)).
6. In humans, this *leads to* the clinical manifestation: **intellectual disability and developmental/motor delay (penetrant), with variable microcephaly, short stature, dysmorphism, and autism** (*inferred* from the model-organism mechanism plus the human phenotype correlation).

```
 H4C5 de novo missense
          │
          ▼
 altered H4 protein (still expressed)
          │  incorporated into nucleosome (dominant)
          ▼
 disrupted histone–histone / histone–chaperone contacts
          │
          ▼
 NUCLEOSOME DESTABILIZATION  ← biochemically shown (H4K91) [31542297]
          │
   ┌──────┴───────────────────────────┐
   ▼                                   ▼
 transcriptional dysregulation   defective cell cycle / DNA repair / telomere silencing
   │                                   │
   └──────────────┬────────────────────┘
                  ▼
 aberrant developmental gene expression
                  ▼
 abnormal neurodevelopment (zebrafish: head/axis defects) → human NDD phenotype
```

- **Molecular pathways:** chromatin assembly and nucleosome organization; chromatin-templated transcription, replication, repair. No classical signaling cascade (Wnt/MAPK/mTOR) is implicated as primary.
- **Cellular processes:** cell-cycle regulation, DNA-damage repair, transcriptional regulation.
- **Protein dysfunction:** altered histone surface → loss of normal histone–histone/chaperone binding → nucleosome instability (gain-of-function/dominant-negative, not loss of expression).
- **Upstream vs downstream:** the mutation and nucleosome destabilization are **upstream**; transcriptional and cell-cycle/repair defects are **downstream**; the clinical phenotype is the most downstream manifestation.
- **Suggested GO terms:** nucleosome assembly (GO:0006334); chromatin organization (GO:0006325); regulation of transcription by RNA polymerase II (GO:0006357); DNA repair (GO:0006281); cell cycle (GO:0007049); nucleosome (GO:0000786, cellular component).
- **Suggested CL terms:** neuron (CL:0000540); neural progenitor/stem cell (CL:0000047) — affected cell populations during neurodevelopment (inferred).

### 7. Anatomical Structures Affected

- **Organ/system level:** primarily the **central nervous system / brain** (UBERON:0000955), manifesting as intellectual disability and developmental delay. Secondary involvement is variable: **skeletal/growth** (short stature), **craniofacial** (microcephaly, dysmorphism), and occasional structural anomalies.
- **Tissue/cell level:** nervous tissue; neurons and neural progenitors are the inferred principal affected populations, though the molecular lesion is **ubiquitous** (histones are universal), so chromatin dysfunction is cell-non-specific at the molecular level even if the clinical readout is brain-dominant.
- **Subcellular level:** the **nucleus** (GO:0005634) and specifically **chromatin/nucleosome** (GO:0000785/GO:0000786) are the compartments involved.
- **Localization/lateralization:** brain involvement is **bilateral/global**; no lateralized or focal lesion is characteristic.

### 8. Temporal Development

- **Onset:** congenital/early childhood; developmental delay and microcephaly are apparent in infancy to early childhood.
- **Onset pattern:** **insidious/chronic** developmental, not acute.
- **Progression:** **static (non-progressive)** — no neurodegeneration reported, distinguishing it from progressive histonopathies such as H3.3 Bryant–Li–Bhoj syndrome ([PMID: 38678163](https://pubmed.ncbi.nlm.nih.gov/38678163/)).
- **Course/duration:** lifelong, stable.
- **Critical period:** embryonic/early neurodevelopment is the window of vulnerability (chromatin-dependent developmental programming); no therapeutic window has been defined.

### 9. Inheritance and Population

- **Inheritance:** autosomal dominant, essentially always **de novo** (sporadic).
- **Epidemiology:** ultra-rare; precise prevalence/incidence are not established. The defining cohort described 29 subjects across six H4 genes, so H4C5-specific counts are small (a handful of published cases).
- **Penetrance:** the neurodevelopmental core appears highly penetrant; non-neurological features show **variable expressivity**.
- **Anticipation / germline mosaicism / founder effects / consanguinity / carrier frequency:** not applicable or not reported — de novo dominant disorders have no carrier frequency and no consanguinity contribution; recurrence risk to siblings is low but not zero owing to possible parental germline mosaicism (general principle; not specifically documented for H4C5).
- **Population demographics:** no ethnic predilection, geographic clustering, or sex bias established; age distribution reflects a pediatric-diagnosed, lifelong condition.

### 10. Diagnostics

- **Primary diagnostic test:** **trio whole-exome sequencing (WES) or whole-genome sequencing (WGS)** demonstrating a de novo H4C5 missense variant ([PMID: 35202563](https://pubmed.ncbi.nlm.nih.gov/35202563/); [PMID: 36987712](https://pubmed.ncbi.nlm.nih.gov/36987712/)). Trio testing is essential to establish de novo status and classify pathogenicity (ACMG criterion PS2).
- **Non-diagnostic / exclusionary tests:** single-gene testing is impractical given 14 identical H4 genes; **karyotype, chromosomal microarray, and repeat-expansion testing are non-diagnostic** and serve mainly to exclude mimics (e.g., Angelman syndrome via methylation/UBE3A testing).
- **Biomarkers/imaging/labs:** no specific biomarker, laboratory abnormality, or pathognomonic imaging finding; MRI may show non-specific changes or microcephaly.
- **Emerging:** DNA-methylation **episignature** classification is plausible (proven for several related chromatin disorders — [PMID: 38815585](https://pubmed.ncbi.nlm.nih.gov/38815585/); [PMID: 42322191](https://pubmed.ncbi.nlm.nih.gov/42322191/)) but not yet validated specifically for H4C5.
- **Differential diagnosis:** **Angelman syndrome** is the key mimic — exome/genome sequencing is recommended for Angelman-like presentations without molecular confirmation ([PMID: 36987712](https://pubmed.ncbi.nlm.nih.gov/36987712/)); other chromatin-regulator NDDs overlap clinically.

### 11. Outcome / Prognosis

- **Survival/mortality:** no evidence of reduced life expectancy or disease-specific mortality; it is a non-lethal, non-progressive developmental disorder.
- **Morbidity/function:** principal burden is lifelong intellectual disability and motor impairment with associated disability; variable additional morbidity from seizures, growth, and dysmorphic features.
- **Course:** static; recovery is not expected but neither is deterioration. Supportive therapy can improve functional outcomes.
- **Prognostic factors:** likely related to variant location/severity and degree of intellectual disability; no validated prognostic biomarker. Cancer risk is not elevated to a surveillance-warranting degree (~1% community-wide; [PMID: 40241305](https://pubmed.ncbi.nlm.nih.gov/40241305/)).

### 12. Treatment

- **No disease-specific or disease-modifying therapy exists.** Management is **supportive and multidisciplinary**: physical therapy, occupational therapy, speech/language therapy, special education, and developmental support; anti-seizure medication where epilepsy is present; management of growth, feeding, orthopedic, and ophthalmologic issues as they arise.
- **Pharmacogenomics / gene therapy / cell therapy / RNA therapy / targeted therapy / immunotherapy:** none applicable or available.
- **Experimental:** no registered disease-specific clinical trials identified.
- **Suggested NCIT terms:** Supportive Care (NCIT:C19236); Physical Therapy (NCIT:C15917); Occupational Therapy (NCIT:C15214); Speech Therapy (NCIT:C15192); Anticonvulsant Agent (NCIT:C264).

### 13. Prevention

- **Primary prevention:** none possible for de novo mutations.
- **Secondary prevention:** early developmental intervention to optimize functional outcomes.
- **Genetic counseling:** recurrence risk to future siblings is low (de novo) but not zero due to possible parental germline mosaicism; prenatal or preimplantation testing is feasible for a known familial variant. No population carrier screening is relevant.
- **Cancer surveillance:** not currently recommended (histonopathy cancer incidence ~1%, below the 5% threshold; [PMID: 40241305](https://pubmed.ncbi.nlm.nih.gov/40241305/)).

### 14. Other Species / Natural Disease

- **Orthology/conservation:** histone H4 is among the **most evolutionarily conserved proteins** known; H4 genes and the H4K91 interface are conserved from yeast to human, which is why yeast and zebrafish are informative mechanistic models ([PMID: 31542297](https://pubmed.ncbi.nlm.nih.gov/31542297/); [PMID: 35202563](https://pubmed.ncbi.nlm.nih.gov/35202563/)).
- **Natural disease / veterinary relevance:** no naturally occurring H4C5-equivalent disease is documented in companion animals or wildlife (OMIA search not productive for this specific gene). No zoonotic or cross-species transmission is applicable (monogenic disorder).

### 15. Model Organisms

- **Zebrafish (*Danio rerio*):** embryos expressing H4 disease variants recapitulate abnormal general development, defective head organs, and reduced body-axis length — the principal in vivo disease model demonstrating causality ([PMID: 35202563](https://pubmed.ncbi.nlm.nih.gov/35202563/); [PMID: 31804630](https://pubmed.ncbi.nlm.nih.gov/31804630/)).
- **Yeast / in vitro biochemistry:** nucleosome-reconstitution assays and yeast genetics established that perturbation of H4K91 destabilizes the nucleosome and disrupts transcription, cell cycle, DNA repair, and telomere silencing ([PMID: 31542297](https://pubmed.ncbi.nlm.nih.gov/31542297/)).
- **Model characteristics:** zebrafish capture gross developmental and craniofacial/CNS phenotypes but do not model higher cognitive deficits; mammalian (mouse) and iPSC/organoid models specific to H4C5 are not yet reported and represent a clear gap.

---

## Mechanistic Model / Interpretation

TEVANED3 is best understood as a **dominant "poison-histone" chromatin disorder**. Unlike loss-of-function NDDs, the pathogenic allele is expressed and its altered protein product is deposited into chromatin, where it corrupts nucleosome architecture from within. Because the mutated residues sit precisely at histone–histone and histone–chaperone interfaces (a statistically notable clustering rather than random distribution), the consequence is **nucleosome destabilization** — directly demonstrated for the recurrent H4K91 interface residue. The downstream ripple effects (transcriptional dysregulation; impaired cell-cycle, DNA-repair, and telomere control) are generic to chromatin instability but become developmentally catastrophic in the tightly timed, chromatin-dependent programs of neurodevelopment, yielding a penetrant intellectual-disability/developmental-delay core with a variably expressed somatic/craniofacial periphery. The disorder's **static** nature (no neurodegeneration) fits a developmental-programming lesion rather than an ongoing toxic process, and distinguishes it from progressive histonopathies like the H3.3-related Bryant–Li–Bhoj syndrome.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [35202563](https://pubmed.ncbi.nlm.nih.gov/35202563/) | *Recurrent de novo missense variants across multiple histone H4 genes underlie a neurodevelopmental syndrome* | Defining cohort (n=29); core phenotype; variant clustering at functional interfaces; zebrafish model |
| [36987712](https://pubmed.ncbi.nlm.nih.gov/36987712/) | *H4C5 missense variant leads to a neurodevelopmental phenotype overlapping with Angelman syndrome* | Specific H4C5 case (p.Tyr99His, de novo, likely pathogenic); Angelman differential; WES/WGS route |
| [31542297](https://pubmed.ncbi.nlm.nih.gov/31542297/) | *Glutarylation of Histone H4 Lysine 91 Regulates Chromatin Dynamics* | Biochemical proof that H4K91 perturbation destabilizes nucleosome and dysregulates transcription/cell cycle/repair |
| [31804630](https://pubmed.ncbi.nlm.nih.gov/31804630/) | *A de novo variant in HIST1H4J causes a syndrome analogous to HIST1H4C NDD* | Allelic-series phenotype (growth delay, microcephaly, ID); shared H4 spectrum |
| [40241305](https://pubmed.ncbi.nlm.nih.gov/40241305/) | *Deep phenotyping of 192 individuals with germline histonopathies* | Classifies H4 disorders as histonopathies; ~1% cancer incidence → no surveillance |
| [38678163](https://pubmed.ncbi.nlm.nih.gov/38678163/) | *Expanded spectrum of Bryant–Li–Bhoj syndrome (H3.3)* | Contrast: H3.3 disorder; supports static vs progressive distinction |
| [38815585](https://pubmed.ncbi.nlm.nih.gov/38815585/); [42322191](https://pubmed.ncbi.nlm.nih.gov/42322191/); [39933316](https://pubmed.ncbi.nlm.nih.gov/39933316/); [42275155](https://pubmed.ncbi.nlm.nih.gov/42275155/) | MSL2, SET, KMT2B, DMAP1 NDDs with episignatures | Precedent for episignature diagnostics extendable to H4 disorders |
| [37605493](https://pubmed.ncbi.nlm.nih.gov/37605493/); [34788807](https://pubmed.ncbi.nlm.nih.gov/34788807/) | HIST1H1E (Rahman) syndrome | Related linker-histone histonopathy; shared NDD features |

---

## Limitations and Knowledge Gaps

1. **Small H4C5-specific sample.** Published H4C5 cases number only a handful; most phenotype data come from the mixed six-gene H4 cohort, so H4C5-specific frequencies, penetrance, and expressivity are imprecise.
2. **No validated episignature** specifically confirmed for H4C5, though strong precedent exists across related chromatin disorders.
3. **No mammalian or iPSC/organoid H4C5 model;** mechanistic inferences for cognition rest on zebrafish, yeast, and biochemistry rather than brain-specific mammalian systems.
4. **Mechanism partly inferred.** Nucleosome destabilization is directly shown for the H4K91 interface; extrapolation to every H4C5 variant (e.g., p.Tyr99His, p.Leu38Pro) is reasonable but not individually demonstrated.
5. **Epidemiology unquantified** (no prevalence/incidence); no formal natural-history or quality-of-life studies.
6. **Ontology gaps:** no dedicated Orphanet/ICD/MeSH codes identified for this serial-numbered subtype in the materials reviewed.

## Proposed Follow-up Experiments / Actions

1. **Aggregate an H4C5-specific case series** (GeneMatcher/Matchmaker Exchange) to quantify penetrance, expressivity, and variant-specific phenotype correlations.
2. **Develop and validate a blood DNA-methylation episignature** for H4C5 to reclassify the many VUS in ClinVar.
3. **Functional characterization of individual H4C5 variants** (p.Tyr99His, p.Leu38Pro, p.Arg41Cys) in nucleosome-stability, chromatin-accessibility (ATAC-seq), and transcriptomic assays.
4. **Generate iPSC-derived neurons/organoids and/or a mouse knock-in** to model neurodevelopmental consequences in a mammalian/human context.
5. **Natural-history and quality-of-life study** across histonopathies to define prognosis and care standards.
6. **Confirm/complete cross-ontology mapping** (Orphanet, ICD-11, MeSH) and formalize HPO annotations with frequencies.


## Artifacts

- [OpenScientist final report](Tessadori-Van_Haaften_Neurodevelopmental_Syndrome_3-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Tessadori-Van_Haaften_Neurodevelopmental_Syndrome_3-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 12 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001249` (2 mentions) - the report calls it "Cognitive/behavioral"; HP calls it **Intellectual disability**
- `HP:0000252` (2 mentions) - the report calls it "Physical/clinical sign"; HP calls it **Microcephaly**
- `HP:0004322` (2 mentions) - the report calls it "Physical"; HP calls it **Short stature**
- `HP:0001999` (2 mentions) - the report calls it "Physical"; HP calls it **Abnormal facial shape**
- `HP:0001250` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Seizure**
- `CL:0000540` (1 mention) - the report calls it "Suggested CL terms:** neuron"; CL calls it **neuron**
- `NCIT:C19236` (1 mention) - the report calls it "Suggested NCIT terms:** Supportive Care"; NCIT calls it **Physical Chemical Technique**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000729` (2 mentions) - the report calls it "Behavioral"; HP calls it **Autistic behavior**
- `GO:0006334` (1 mention) - the report calls it "Suggested GO terms:** nucleosome assembly"; GO calls it **nucleosome assembly**
- `UBERON:0000955` (1 mention) - the report calls it "central nervous system / brain"; UBERON calls it **brain**, and lists "suprasegmental levels of nervous system" among its other names
- `GO:0005634` (1 mention) - the report calls it "nucleus", "Subcellular level:** the **nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005634` - called "nucleus", "Subcellular level:** the **nucleus"