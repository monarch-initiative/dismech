---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T18:54:55.047004'
end_time: '2026-10-31T19:10:14.057648'
duration_seconds: 919.01
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: '"ETV6-Related Thrombocytopenia"'
  mondo_id: MONDO:0014536
  category: Mendelian
  causal_genes: ETV6
  omim_id: OMIM:616216
  synonyms: ETV6 thrombocytopenia; ETV6-related thrombocytopenia with or without myeloid
    malignancy; thrombocytopenia caused by mutation in ETV6
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
citation_count: 16
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 15
  validator_version: 0.4.0
term_validation:
  total_terms: 24
  verified: 22
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 2
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: MONDO:0014536
    reported_labels:
    - MONDO
    ontology_label: thrombocytopenia 5
  - term_id: HP:0001873
    reported_labels:
    - Laboratory abnormality / clinical sign
    ontology_label: Thrombocytopenia
  - term_id: HP:0001972
    reported_labels:
    - Laboratory abnormality
    ontology_label: Macrocytic anemia
  - term_id: HP:0003540
    reported_labels:
    - Laboratory abnormality
    ontology_label: Impaired platelet aggregation
  - term_id: HP:0001892
    reported_labels:
    - Symptom / clinical sign
    ontology_label: Abnormal bleeding
  - term_id: HP:0006721
    reported_labels:
    - Neoplasm
    ontology_label: Acute lymphoblastic leukemia
  - term_id: HP:0004808
    reported_labels:
    - Neoplasm
    ontology_label: Acute myeloid leukemia
  - term_id: GO:0005737
    reported_labels:
    - "cytoplasm \u2014 aberrant localization"
    - cytoplasm
    ontology_label: cytoplasm
  labels_variant: 5
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ETV6-Related_Thrombocytopenia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ETV6-Related_Thrombocytopenia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** "ETV6-Related Thrombocytopenia"
- **MONDO ID:** MONDO:0014536 (if available)
- **Causal gene(s):** ETV6
- **OMIM:** OMIM:616216
- **Synonyms:** ETV6 thrombocytopenia; ETV6-related thrombocytopenia with or without myeloid malignancy; thrombocytopenia caused by mutation in ETV6
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **"ETV6-Related Thrombocytopenia"** covering all of the
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

# ETV6-Related Thrombocytopenia (Thrombocytopenia 5): Comprehensive Disease Characterization Report

**Disease:** ETV6-Related Thrombocytopenia (Thrombocytopenia 5, THC5)
**Causal gene:** **ETV6** (ETS variant transcription factor 6; formerly *TEL*), HGNC:3495, chromosome 12p13.2, NCBI Gene 2120
**Key identifiers:** OMIM:616216 (Thrombocytopenia 5, THC5) · MONDO:0014536 · Orphanet (ETV6-related thrombocytopenia with predisposition to leukemia) · Inheritance: Autosomal dominant · Category: Mendelian

> This report concerns the Mendelian disorder caused by germline variants in **ETV6**. It must not be confused with similarly numbered inherited thrombocytopenias caused by other genes (e.g., *ANKRD26*-related THC2, *RUNX1*-related familial platelet disorder/THC-FPD); the defining gene here is **ETV6**.

---

## Summary

**ETV6-Related Thrombocytopenia is an autosomal dominant Mendelian bleeding/cancer-predisposition syndrome caused by germline heterozygous variants in *ETV6*, the gene encoding the master hematopoietic transcriptional repressor ETV6 (TEL).** The disease was defined in 2015 when whole-exome sequencing of a family with dominantly inherited thrombocytopenia, elevated erythrocyte mean corpuscular volume (MCV), and two cases of B-cell precursor acute lymphoblastic leukemia (ALL) identified a heterozygous *ETV6* c.641C>T (p.Pro214Leu) variant segregating with disease ([PMID: 25807284](https://pubmed.ncbi.nlm.nih.gov/25807284/)). The clinical phenotype is a lifelong, mild-to-moderate thrombocytopenia with red-cell macrocytosis and generally mild bleeding, but its defining and most consequential feature is a high, age-dependent, incompletely penetrant predisposition to hematological malignancy — principally childhood B-ALL, plus adult myelodysplastic syndrome (MDS) and acute myeloid leukemia (AML).

Mechanistically, pathogenic *ETV6* variants act as **dominant-negative loss-of-function alleles**. Variants cluster in the ETS (DNA-binding) and central/linker domains. The mutant protein is mislocalized from the nucleus to the cytoplasm and physically co-sequesters wild-type ETV6, abolishing nuclear transcriptional repression of ETV6 target genes. This produces two main phenotypic branches: (1) dysregulated megakaryopoiesis — an expanded but immature megakaryocyte pool with abnormal cytoskeletal organization and impaired proplatelet formation, yielding thrombocytopenia with largely preserved platelet size; and (2) a predisposed hematopoietic stem/progenitor compartment that, upon acquiring a somatic "second hit" (frequently deletion of the remaining wild-type *ETV6* allele plus cooperating mutations), transforms to leukemia. A CRISPR knock-in mouse of the recurrent human mutation adds a third, inflammation-driven branch: elevated IL-18 and IL-13 impair B-lymphoid development of multipotent progenitors, linking ETV6 dysfunction to both defective thrombopoiesis and leukemogenesis.

There is **no disease-specific drug**. Management is surveillance-based: lifelong hematologic monitoring for malignant transformation, genetic counseling and cascade testing, avoidance of immune-thrombocytopenia (ITP)-type therapies (splenectomy, immunosuppression) that are inappropriate for this inherited disorder, and — critically — carrier-aware selection of related donors for allogeneic hematopoietic stem cell transplantation (HSCT) to prevent donor-derived leukemia. The disorder is ultra-rare (only ~18 families reported by 2017), and no population prevalence figures are firmly established. Knowledge derives almost entirely from aggregated disease-level resources — pedigree case reports/series (human clinical), in vitro functional assays, patient iPSC models, and genetically engineered mouse models — rather than individual-level EHR data.

---

## 1. Disease Information

**Overview.** ETV6-Related Thrombocytopenia (Thrombocytopenia 5; THC5) is an autosomal dominant inherited platelet disorder with predisposition to hematological malignancy. Patients present, usually in childhood, with decreased platelet number and a tendency to bleed, and carry germline mutations in *ETV6*, a master hematopoietic transcription factor ([PMID: 28555414](https://pubmed.ncbi.nlm.nih.gov/28555414/)): *"Patients with thrombocytopenia 5 have an autosomal dominant disorder of decreased platelet number with tendency to bleed, usually presenting in childhood, and have been found to have germline mutations in ETV6, which encodes a master hematopoietic transcription factor."*

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | 616216 (Thrombocytopenia 5, THC5) |
| MONDO | MONDO:0014536 |
| Gene (HGNC) | ETV6, HGNC:3495 |
| NCBI Gene | 2120 |
| Chromosome | 12p13.2 |
| Orphanet | ETV6-related thrombocytopenia with predisposition to acute lymphoblastic leukemia |

**Synonyms / alternative names:** ETV6 thrombocytopenia; ETV6-related thrombocytopenia with or without myeloid malignancy; thrombocytopenia caused by mutation in ETV6; ETV6-related thrombocytopenia and leukemia predisposition; THC5. The gene was historically called *TEL* (translocation-ETS-leukemia).

**Information source type.** Disease-level aggregated resources (OMIM, Orphanet) and individual-patient/family-level primary literature (pedigree studies, functional characterizations). Not EHR-population-derived; a rare Mendelian disorder characterized through family-based gene discovery and functional studies.

---

## 2. Etiology

**Primary cause — genetic.** The disease is monogenic: a germline heterozygous pathogenic variant in *ETV6* is the necessary cause. The original gene-discovery study identified *ETV6* c.641C>T (p.Pro214Leu) by whole-exome sequencing and found two additional *ETV6*-mutant families among 23 screened ([PMID: 25807284](https://pubmed.ncbi.nlm.nih.gov/25807284/)): *"Whole-exome sequencing identified a heterozygous single-nucleotide change in ETV6 (ets variant 6), c.641C>T, encoding a p.Pro214Leu substitution in the central domain, segregating with thrombocytopenia and elevated MCV."*

**Genetic risk factors.** The causal variants themselves (Section 4) are the risk factors for thrombocytopenia. For the *malignancy* phenotype, the germline variant establishes a predisposed clone that requires a somatic second hit — the strongest driver of progression is acquisition of additional somatic lesions, most characteristically loss of the wild-type *ETV6* allele ([PMID: 26102509](https://pubmed.ncbi.nlm.nih.gov/26102509/)). Modifier genes are not firmly established.

**Environmental, lifestyle, and infectious factors.** No specific environmental toxin, radiation, occupational exposure, lifestyle factor (smoking, diet, alcohol), or infectious agent has been identified as causing or triggering ETV6-related thrombocytopenia. This is a germline Mendelian disorder; environmental contributions are not applicable to onset. As a non-specific consideration, prior cytotoxic chemotherapy may contribute to therapy-related MDS in predisposed carriers — one reported sibling developed therapy-related MDS after childhood ALL ([PMID: 40858768](https://pubmed.ncbi.nlm.nih.gov/40858768/)).

**Protective factors.** No genetic or environmental protective factors are established.

**Gene–environment interactions.** No specific gene–environment interaction is characterized. The dominant interaction is gene–somatic-mutation (two-hit): germline ETV6 loss predisposes; a stochastic/acquired somatic event completes transformation.

---

## 3. Phenotypes

The core phenotype is **mild-to-moderate thrombocytopenia with a tendency to bleed, red-cell macrocytosis, impaired platelet function, and predisposition to hematological malignancy** ([PMID: 28555414](https://pubmed.ncbi.nlm.nih.gov/28555414/); [PMID: 25807284](https://pubmed.ncbi.nlm.nih.gov/25807284/)).

| Phenotype | Type | HPO suggestion | Onset | Severity / frequency | Progression |
|---|---|---|---|---|---|
| Thrombocytopenia | Laboratory abnormality / clinical sign | HP:0001873 | Childhood (often congenital/early) | Mild–moderate; high penetrance | Stable, lifelong |
| Red-cell macrocytosis (high MCV) | Laboratory abnormality | HP:0001972 | Childhood | Co-segregates with thrombocytopenia | Stable |
| Abnormal platelet aggregation / dysfunction | Laboratory abnormality | HP:0003540 | Lifelong | Impaired aggregation in ~90% of IT patients tested | Stable |
| Bleeding tendency (bruising, epistaxis, mucosal) | Symptom / clinical sign | HP:0001892 | Childhood | Generally mild; often not main issue | Episodic with hemostatic challenge |
| B-cell acute lymphoblastic leukemia | Neoplasm | HP:0006721 | Childhood | Subset; part of ~10–45% HM risk | Progressive if untreated |
| Myelodysplastic syndrome | Neoplasm | HP:0002863 | Adult | Subset | Progressive |
| Acute myeloid leukemia | Neoplasm | HP:0004808 | Adult | Subset | Progressive |
| Normal/near-normal platelet size | Laboratory feature | — | — | Distinguishes from macrothrombocytopenias | Stable |

**Key quantitative/clinical details.** In a cohort of inherited thrombocytopenia with malignancy risk, *"Platelet aggregation was impaired in 90% of all patients, while reduced activation and granule secretion were heterogeneous"* ([PMID: 40670159](https://pubmed.ncbi.nlm.nih.gov/40670159/)); genetic diagnosis was delayed ~20 years from first thrombocytopenia detection. The original family displayed the characteristic triad: *"autosomal dominant thrombocytopenia, high erythrocyte mean corpuscular volume (MCV) and two occurrences of B cell-precursor acute lymphoblastic leukemia (ALL)"* ([PMID: 25807284](https://pubmed.ncbi.nlm.nih.gov/25807284/)).

**Quality-of-life impact.** Bleeding is frequently NOT the dominant clinical problem; it is usually mild. The principal burden on quality of life and prognosis is the lifelong cancer risk and surveillance need ([PMID: 28594466](https://pubmed.ncbi.nlm.nih.gov/28594466/): *"mutations in RUNX1, ANKRD26 and ETV6 cause congenital thrombocytopaenia, but we now know that they also predispose to haematological malignancies"*). Formal EQ-5D/SF-36 data specific to this ultra-rare disorder are not available.

---

## 4. Genetic / Molecular Information

**Causal gene.** *ETV6* (ETS variant transcription factor 6; TEL), HGNC:3495, chromosome 12p13.2, NCBI Gene 2120. ETV6 is an ETS-family transcriptional repressor and master hematopoietic regulator ([PMID: 28555414](https://pubmed.ncbi.nlm.nih.gov/28555414/)).

**Pathogenic variants.** Reported germline pathogenic/likely-pathogenic variants cluster in the **ETS (DNA-binding) domain** and the **central/linker domain**, predominantly **missense** with occasional **frameshift** ([PMID: 25807284](https://pubmed.ncbi.nlm.nih.gov/25807284/); [PMID: 26102509](https://pubmed.ncbi.nlm.nih.gov/26102509/); [PMID: 27663637](https://pubmed.ncbi.nlm.nih.gov/27663637/); [PMID: 40858768](https://pubmed.ncbi.nlm.nih.gov/40858768/)):

| Variant (protein) | cDNA | Domain | Type | Note |
|---|---|---|---|---|
| p.Pro214Leu | c.641C>T | Central/linker | Missense | Recurrent "founder-like" hotspot; LOF control in assays; predicted extra nuclear export signal |
| p.Arg418Gly | c.1252A>G | ETS DNA-binding | Missense | Associated with alternative splicing / exon skipping |
| p.Leu349Pro | — | Central | Missense | Thrombocytopenia + ALL kindred |
| p.Asn385fs | — | — | Frameshift | WT-ETV6 allele deleted in leukemic cells |
| p.Ala377Thr | — | ETS | Missense | Reduced corepressor binding |
| p.Tyr401Asn | — | ETS | Missense | Reduced corepressor binding |
| p.Leu376Gln | — | — | Missense | Hematological + solid-tumor pedigree; absent from gnomAD |
| p.Arg202Gly | c.604C>G | Central | Missense | **WT-like in functional assays — NOT loss-of-function** (cautionary VUS) |

**Variant classification (ACMG/AMP).** Pathogenicity is variant-specific and requires functional evaluation. A key cautionary example: p.Arg202Gly, found in monozygotic twins with ETV6::RUNX1-positive B-ALL, behaved WT-like in localization and reporter assays and does **not** support a loss-of-function effect, whereas p.Pro214Leu failed to repress target promoters ([PMID: 42479114](https://pubmed.ncbi.nlm.nih.gov/42479114/)). Rare *ETV6* variants should not be over-called as pathogenic without functional data.

**Allele frequency.** Pathogenic variants are essentially absent from large population databases (e.g., p.Leu376Gln not in gnomAD), consistent with pathogenic rarity ([PMID: 40858768](https://pubmed.ncbi.nlm.nih.gov/40858768/)).

**Somatic vs germline.** The disease-defining variant is **germline heterozygous**. A somatic second hit — frequently deletion/loss of the remaining wild-type *ETV6* allele — occurs in leukemic cells: *"Leukemic cells from the proband in the second kindred showed deletion of wild type ETV6 with retention of the ETV6 p.N385fs"* ([PMID: 26102509](https://pubmed.ncbi.nlm.nih.gov/26102509/)). Germline status must be confirmed in non-hematopoietic tissue (skin fibroblasts) to avoid mistaking a germline allele for somatic clonal hematopoiesis ([PMID: 40858768](https://pubmed.ncbi.nlm.nih.gov/40858768/)).

**Functional consequence.** Dominant-negative loss of function. Mutant ETV6 is mislocalized to the cytoplasm and co-sequesters wild-type ETV6, reducing transcriptional repression ([PMID: 25807284](https://pubmed.ncbi.nlm.nih.gov/25807284/); [PMID: 26102509](https://pubmed.ncbi.nlm.nih.gov/26102509/)). ETS-domain variants additionally reduce corepressor binding ([PMID: 27663637](https://pubmed.ncbi.nlm.nih.gov/27663637/)).

**Modifier genes, epigenetics, chromosomal abnormalities.** No specific modifier genes or disease-specific epigenetic signatures are established for the germline disorder. Large-scale chromosomal abnormalities are not the primary germline lesion; however, somatic loss of 12p / the wild-type *ETV6* allele participates in transformation.

---

## 5. Environmental Information

No environmental, lifestyle, or infectious factors are established as causes or triggers — it is a germline Mendelian disorder. As a non-specific consideration, prior cytotoxic therapy for a first malignancy may contribute to therapy-related MDS in predisposed carriers ([PMID: 40858768](https://pubmed.ncbi.nlm.nih.gov/40858768/)), but no primary environmental etiology applies. **Not applicable / not available.**

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A **germline heterozygous *ETV6* variant** in the ETS or central/linker domain **leads to** production of a structurally altered ETV6 protein (normal transcript/protein levels in several variants) ([PMID: 25807284](https://pubmed.ncbi.nlm.nih.gov/25807284/); [PMID: 26102509](https://pubmed.ncbi.nlm.nih.gov/26102509/)).
2. The mutant protein **results in** impaired nuclear localization — ETV6 is mislocalized to the **cytoplasm**, and (dominant-negative) co-sequesters endogenous wild-type ETV6 (*inferred* to involve an exposed/created nuclear export signal, predicted in silico for p.Pro214Leu) ([PMID: 25807284](https://pubmed.ncbi.nlm.nih.gov/25807284/); [PMID: 42479114](https://pubmed.ncbi.nlm.nih.gov/42479114/)).
3. Cytoplasmic mislocalization **leads to** loss of nuclear ETV6-mediated transcriptional repression; ETS-domain variants additionally **result in** reduced corepressor binding ([PMID: 26102509](https://pubmed.ncbi.nlm.nih.gov/26102509/); [PMID: 27663637](https://pubmed.ncbi.nlm.nih.gov/27663637/)).
4. Loss of repression **branches** into three downstream effects:
   - **4a (thrombocytopenia branch):** Dysregulated megakaryopoiesis — expansion of megakaryocyte colony-forming units but production of **immature megakaryocytes** with abnormal cytoskeletal organization **leads to** defective **proplatelet formation** → reduced platelet release → thrombocytopenia (largely preserved platelet size) → mild bleeding ([PMID: 27663637](https://pubmed.ncbi.nlm.nih.gov/27663637/); [PMID: 34019812](https://pubmed.ncbi.nlm.nih.gov/34019812/)).
   - **4b (erythroid branch):** Altered erythropoiesis **results in** red-cell macrocytosis (elevated MCV) ([PMID: 25807284](https://pubmed.ncbi.nlm.nih.gov/25807284/)).
   - **4c (inflammation/lymphoid branch):** ETV6 dysfunction **promotes** sterile inflammation; elevated **IL-18 and IL-13** **abrogate** B-cell development of multipotent progenitor (MPP4) cells (*demonstrated in mouse knock-in; mechanistic inference for human leukemogenesis*) ([PMID: 35803545](https://pubmed.ncbi.nlm.nih.gov/35803545/)).
5. Over years, a predisposed clone **acquires a somatic second hit** — frequently **deletion/loss of the remaining wild-type *ETV6* allele** plus cooperating mutations ([PMID: 26102509](https://pubmed.ncbi.nlm.nih.gov/26102509/)).
6. The second hit **leads to** clonal expansion → hematological malignancy (childhood B-ALL; adult MDS/AML) ([PMID: 28555414](https://pubmed.ncbi.nlm.nih.gov/28555414/); [PMID: 26102509](https://pubmed.ncbi.nlm.nih.gov/26102509/)).

### Mechanistic detail

- **Molecular pathways / cellular processes:** ETV6 performs sequence-specific **DNA-binding transcriptional repression** (GO:0000122) and regulates **hematopoietic/megakaryocyte differentiation**. Disease is driven by loss of this repressive function. Suggested GO terms: GO:0030219 (megakaryocyte differentiation), GO:0030220 (platelet formation), GO:0006357 (regulation of transcription by RNA Pol II), GO:0050729 (positive regulation of inflammatory response — IL-18/IL-13 branch).
- **Protein dysfunction:** Dominant-negative loss of function via subcellular mislocalization (nucleus → cytoplasm) and co-sequestration of wild-type protein; ETS-domain variants impair corepressor recruitment. Suggested GO cellular components: GO:0005634 (nucleus — normal site), GO:0005737 (cytoplasm — aberrant localization).
- **Immune/inflammatory involvement:** The CRISPR knock-in mouse revealed sterile inflammation with IL-18 and IL-13 impairing lymphoid development — *"a model in which ETV6 dysfunction promotes inflammation, which adversely affects thrombopoiesis and promotes leukemogenesis"* ([PMID: 35803545](https://pubmed.ncbi.nlm.nih.gov/35803545/)).
- **Cell types (CL terms):** megakaryocyte (CL:0000556), platelet (CL:0000233), erythroid lineage (CL:0000764), hematopoietic multipotent progenitor (CL:0000837), common lymphoid progenitor (CL:0000051).
- **Upstream vs downstream:** Upstream = germline variant → cytoplasmic mislocalization → loss of repression. Downstream = megakaryocyte maturation defect/thrombocytopenia, macrocytosis, inflammation-impaired lymphopoiesis, and (after second hit) leukemia.

### Schematic

```
 Germline ETV6 variant (ETS / central domain; missense > frameshift)
              │
              ▼
 Cytoplasmic mislocalization of mutant ETV6
 (+ co-sequestration of WT ETV6 = DOMINANT-NEGATIVE)
              │
              ▼
 Loss of nuclear transcriptional repression
 (ETS-domain variants: ↓ corepressor binding)
     ┌────────────┼─────────────────────────┐
     ▼            ▼                          ▼
 4a Megakaryo-  4b Erythroid            4c Sterile inflammation
 poiesis:       alteration:            (IL-18, IL-13)
 ↑ immature MKs  ↑ MCV                 impairs MPP4→B-cell
 abnormal        (macrocytosis)        development
 cytoskeleton
     │                                        │
     ▼                                        │
 ↓ proplatelet formation                      │
     │                                        │
     ▼                                        ▼
 THROMBOCYTOPENIA  ───────────►  SOMATIC 2nd HIT (loss of WT ETV6 allele)
 (mild bleeding)                              │
                                             ▼
                                   B-ALL (childhood) / MDS-AML (adult)
```

---

## 7. Anatomical Structures Affected

- **Organ/system level:** The **hematopoietic system** and **bone marrow** (UBERON:0002371, bone marrow; UBERON:0002390, hematopoietic system) are the primary sites. ETV6 is required specifically for bone-marrow hematopoiesis ([PMID: 9694803](https://pubmed.ncbi.nlm.nih.gov/9694803/)). Secondary involvement: peripheral blood and, in leukemia, extramedullary sites.
- **Tissue/cell level:** Affected cells are **megakaryocytes** (CL:0000556; overproduced but immature with defective proplatelet formation — [PMID: 34019812](https://pubmed.ncbi.nlm.nih.gov/34019812/), [PMID: 27663637](https://pubmed.ncbi.nlm.nih.gov/27663637/)), the **erythroid lineage** (CL:0000764; macrocytosis — [PMID: 25807284](https://pubmed.ncbi.nlm.nih.gov/25807284/)), and **multipotent/lymphoid progenitors** (MPP4; CL:0000837 — [PMID: 35803545](https://pubmed.ncbi.nlm.nih.gov/35803545/)). Carriers show increased circulating **CD34+ progenitors** ([PMID: 27663637](https://pubmed.ncbi.nlm.nih.gov/27663637/)).
- **Subcellular level:** The core defect is subcellular localization — mutant ETV6 is displaced from the **nucleus** (GO:0005634) to the **cytoplasm** (GO:0005737) ([PMID: 25807284](https://pubmed.ncbi.nlm.nih.gov/25807284/); [PMID: 26102509](https://pubmed.ncbi.nlm.nih.gov/26102509/)).
- **Localization/lateralization:** Systemic hematologic disorder; lateralization not applicable.

---

## 8. Temporal Development

- **Onset:** Thrombocytopenia typically presents in **childhood** (often congenital/early-life) and is chronic/lifelong ([PMID: 28555414](https://pubmed.ncbi.nlm.nih.gov/28555414/)); onset pattern **chronic/insidious**.
- **Progression:** The thrombocytopenia itself is **stable** over the lifespan. Malignancy risk is **age-dependent**: B-ALL characteristically presents in childhood, MDS/AML in adulthood — within a single pedigree one sibling had childhood ALL and adult therapy-related MDS while another had only chronic isolated thrombocytopenia ([PMID: 40858768](https://pubmed.ncbi.nlm.nih.gov/40858768/)).
- **Disease course:** Lifelong (chronic) for thrombocytopenia; the leukemic branch, when it occurs, is a discrete transformative event requiring intensive therapy.
- **Critical periods / intervention windows:** Continuous lifelong hematologic surveillance is the practical intervention window; no defined molecular "critical period" for prevention is established.

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal dominant** ([PMID: 25807284](https://pubmed.ncbi.nlm.nih.gov/25807284/); [PMID: 28555414](https://pubmed.ncbi.nlm.nih.gov/28555414/)).
- **Penetrance:** **High (near-complete) for thrombocytopenia/macrocytosis**, which co-segregate with the variant; **incomplete, age-dependent for hematological malignancy** — ~10–45% across the ETV6/RUNX1/ANKRD26 group ([PMID: 40670159](https://pubmed.ncbi.nlm.nih.gov/40670159/): *"Inherited thrombocytopenia (IT) with germline variants in RUNX1, ETV6 or ANKRD26 carries a high risk (10%-45%) of developing haematological malignancy."*).
- **Expressivity:** **Variable**, even within a single family ([PMID: 40858768](https://pubmed.ncbi.nlm.nih.gov/40858768/)).
- **Epidemiology:** **Ultra-rare** — only **18 families** had been reported by 2017 ([PMID: 28555414](https://pubmed.ncbi.nlm.nih.gov/28555414/): *"Since the first description of germline ETV6 mutations, 18 families have been reported."*). No established population prevalence/incidence; no formal Orphanet prevalence class.
- **Founder effects / anticipation / mosaicism / consanguinity / carrier frequency:** No firmly established founder population, though **p.Pro214Leu recurs** across unrelated families (recurrent hotspot/founder-like allele). Genetic anticipation and germline mosaicism not established. Carrier frequency unknown (variants absent from gnomAD).
- **Demographics:** No firmly established ethnic predilection, sex bias, or geographic clustering. Age distribution: thrombocytopenia from childhood; B-ALL in children, MDS/AML in adults.

---

## 10. Diagnostics

- **Clinical/laboratory tests:** CBC shows **isolated mild-to-moderate thrombocytopenia** with **elevated MCV (macrocytosis)** and **near-normal platelet size**; platelet aggregation studies are typically **impaired** ([PMID: 25807284](https://pubmed.ncbi.nlm.nih.gov/25807284/); [PMID: 40670159](https://pubmed.ncbi.nlm.nih.gov/40670159/)). LOINC: platelet count (26515-7), MCV (30428-7).
- **Genetic testing (definitive):** Diagnosis is molecular. **Targeted panel-based NGS** covering inherited platelet-disorder genes (e.g., 59-gene panels including ETV6, RUNX1, ANKRD26) is standard ([PMID: 31249973](https://pubmed.ncbi.nlm.nih.gov/31249973/): *"we developed, verified, and evaluated a targeted, panel-based next-generation sequencing approach comprising 59 genes associated with IPD"*). WES/WGS aid gene discovery and atypical cases. **Germline confirmation on non-hematopoietic tissue** (cultured skin fibroblasts) is required to distinguish germline from somatic/clonal variants ([PMID: 40858768](https://pubmed.ncbi.nlm.nih.gov/40858768/): *"Germline testing on skin fibroblasts confirmed the presence of the same ETV6 variant in the proband and two of his siblings"*).
- **Variant interpretation caveat:** Rare *ETV6* variants require **functional assessment** (subcellular localization + transcriptional reporter assays) before being called pathogenic; p.Arg202Gly is WT-like despite occurring in leukemia twins ([PMID: 42479114](https://pubmed.ncbi.nlm.nih.gov/42479114/)).
- **Diagnostic delay:** Frequently ~20 years from first thrombocytopenia detection to genetic diagnosis ([PMID: 40670159](https://pubmed.ncbi.nlm.nih.gov/40670159/)).
- **Differential diagnosis:** Other inherited thrombocytopenias with malignancy predisposition (RUNX1-RT/FPDMM, ANKRD26-RT), immune thrombocytopenia (ITP), Bernard-Soulier syndrome, other inherited platelet disorders. Distinguishing features: ETV6 shows macrocytosis, near-normal platelet size, and a distinctive molecular signature (overproduced immature megakaryocytes vs. RUNX1's reduced, more agonist-responsive megakaryocytes — [PMID: 34019812](https://pubmed.ncbi.nlm.nih.gov/34019812/)).
- **Screening:** Cascade testing of at-risk relatives; no population newborn screening exists.

---

## 11. Outcome / Prognosis

- **Thrombocytopenia prognosis:** Generally benign; bleeding is usually mild and *"not the main clinical issue"* ([PMID: 28594466](https://pubmed.ncbi.nlm.nih.gov/28594466/)).
- **Malignancy dominates prognosis:** The ~10–45% lifetime hematological-malignancy risk (childhood B-ALL; adult MDS/AML) is the principal determinant of outcome ([PMID: 40670159](https://pubmed.ncbi.nlm.nih.gov/40670159/); [PMID: 28555414](https://pubmed.ncbi.nlm.nih.gov/28555414/)). Some pedigrees also show solid-tumor predisposition ([PMID: 40858768](https://pubmed.ncbi.nlm.nih.gov/40858768/)).
- **Survival/mortality:** No disorder-specific survival statistics are established given rarity; outcomes depend on the specific malignancy that develops and its treatment.
- **Prognostic factors:** Development of malignancy; acquisition of a somatic second hit (loss of wild-type *ETV6*); need for HSCT. No validated prognostic biomarker panel beyond genotype and clinical/molecular surveillance.

---

## 12. Treatment

**There is no disease-specific or disease-modifying drug for the germline ETV6 defect; management is supportive and surveillance-based** ([PMID: 28555414](https://pubmed.ncbi.nlm.nih.gov/28555414/)).

- **Supportive care for bleeding:** Platelet transfusion and antifibrinolytics as needed for significant bleeding or hemostatic challenges. **ITP-directed therapies (splenectomy, immunosuppression) are inappropriate** and should be avoided — this is not immune-mediated.
- **Surveillance:** Lifelong hematologic monitoring for malignant transformation, with recommendations for patient screening and follow-up ([PMID: 28555414](https://pubmed.ncbi.nlm.nih.gov/28555414/)).
- **Treatment of malignancy:** Standard protocols for the specific leukemia/MDS, potentially including **allogeneic HSCT** (NCIT: Hematopoietic Cell Transplantation).
- **Carrier-aware donor selection (critical):** For allogeneic HSCT, **related donors must be screened** to avoid using a donor carrying the same germline variant, which risks **donor-derived leukemia** and graft failure ([PMID: 36279069](https://pubmed.ncbi.nlm.nih.gov/36279069/): *"Prompt recognition of affected patients is imperative not only for personalized surveillance strategies but also for proper donor selection for those undergoing stem cell transplantation to avoid familial donors who also may share the same germline mutation"*; [PMID: 37913908](https://pubmed.ncbi.nlm.nih.gov/37913908/)). Empirical risk: of 5 patients transplanted from a predisposition-variant-positive relative donor, **1 developed donor-derived leukemia** ([PMID: 42418371](https://pubmed.ncbi.nlm.nih.gov/42418371/)).
- **Genetic counseling:** Integral to management (risk assessment, cascade testing, family planning).
- **Experimental/targeted therapies:** None approved or in trials specifically for the germline ETV6 defect. The **IL-18/IL-13 sterile-inflammation axis** identified in the mouse knock-in is a mechanistic (not yet clinical) therapeutic candidate ([PMID: 35803545](https://pubmed.ncbi.nlm.nih.gov/35803545/)).
- **Pharmacogenomics:** Not specifically established for this disorder.

NCIT suggestions: Hematopoietic Cell Transplantation, Platelet Transfusion, Supportive Care, Genetic Counseling.

---

## 13. Prevention

- **Primary prevention:** Not possible for a germline disorder. Reproductive options (genetic counseling, preimplantation genetic diagnosis, prenatal testing) can prevent transmission to offspring.
- **Secondary prevention (most important):** **Surveillance and cascade genetic testing** to detect malignant transformation early and identify at-risk relatives ([PMID: 28555414](https://pubmed.ncbi.nlm.nih.gov/28555414/); [PMID: 36279069](https://pubmed.ncbi.nlm.nih.gov/36279069/)).
- **Tertiary prevention:** Avoid inappropriate ITP therapies; carrier-aware donor selection for HSCT to prevent donor-derived malignancy ([PMID: 42418371](https://pubmed.ncbi.nlm.nih.gov/42418371/)); appropriate peri-procedural hemostatic management.
- **Genetic counseling:** Central to prevention (autosomal dominant, 50% transmission risk).
- **Immunization / public health / environmental interventions:** Not applicable (no infectious or environmental etiology).

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** Human *ETV6* (NCBI Gene 2120) has a mouse ortholog *Etv6* (NCBI Gene 14011; NCBI Taxon 10090, *Mus musculus*). ETV6 is evolutionarily conserved as a hematopoietic regulator.
- **Natural disease in other species:** No well-characterized naturally occurring ETV6-related thrombocytopenia syndrome in companion animals or wildlife is documented (no established OMIA entry for this specific germline syndrome). **Not available.**
- **Comparative biology:** The essential role of ETV6 in bone-marrow hematopoiesis is conserved — mouse knockouts demonstrate conserved requirement (Section 15), providing a strong comparative basis even though a spontaneous human-equivalent disease is not reported in other species.
- **Transmission / zoonosis:** Not applicable (germline genetic disorder).

---

## 15. Model Organisms

- **Mouse knockout (constitutive):** *Etv6/Tel*-null mice are **embryonic lethal** due to a yolk-sac angiogenic defect; chimera studies show ETV6 is **essential for bone-marrow hematopoiesis of all lineages**, manifesting within the first postnatal week ([PMID: 9694803](https://pubmed.ncbi.nlm.nih.gov/9694803/)): *"TEL function is essential for the establishment of hematopoiesis of all lineages in the bone marrow. This defect is manifest within the first week of postnatal life."* and *"TEL-/- mice are embryonic lethal because of a yolk sac angiogenic defect."*
- **CRISPR/Cas9 knock-in mouse (disease allele):** A knock-in of the most common recurrent germline *ETV6* mutation is viable and recapitulates key features — **hematopoietic defects centered on the MPP4 progenitor subset and sterile inflammation** ([PMID: 35803545](https://pubmed.ncbi.nlm.nih.gov/35803545/)): *"we developed a mouse model of the most common recurrent, disease-causing germline mutation in ETV6. We found defects in hematopoiesis related primarily to abnormalities of the multipotent progenitor population 4 (MPP4) subset ... and evidence of sterile inflammation."* It links **IL-18/IL-13** to impaired B-cell development.
- **Patient-derived iPSC models:** CRISPR-Cas9-engineered and patient-derived iPSC lines recapitulate the megakaryocyte phenotype and distinguish ETV6 from RUNX1 disease ([PMID: 34019812](https://pubmed.ncbi.nlm.nih.gov/34019812/)): *"The ETV6-mutant iPSCs yield more hematopoietic progenitor cells and megakaryocytes, but the megakaryocytes are immature and less responsive to agonist stimulation"*, and *"both mutant iPSC lines display defects in proplatelet formation ... the molecular mechanisms may be distinct."* A new patient iPSC line, MULi001-A, carries germline p.Pro214Leu ([PMID: 42296844](https://pubmed.ncbi.nlm.nih.gov/42296844/)).
- **In vitro cell systems:** HeLa and Ba/F3 cells expressing wild-type vs. mutant ETV6 are used for localization and transcriptional-reporter assays (e.g., MMP3, PF4 promoters) to classify variant function ([PMID: 42479114](https://pubmed.ncbi.nlm.nih.gov/42479114/); [PMID: 35803545](https://pubmed.ncbi.nlm.nih.gov/35803545/)).
- **Phenotype recapitulation & limitations:** The knock-in mouse captures progenitor defects and inflammation but is viable (unlike the embryonic-lethal null) and does not fully model human B-ALL incidence; iPSC models capture megakaryocyte maturation/proplatelet defects but lack the in vivo marrow niche and long-term leukemogenesis. Resources: MGI (mouse *Etv6*), Cellosaurus (iPSC lines).

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [25807284](https://pubmed.ncbi.nlm.nih.gov/25807284/) | *Germline mutations in ETV6 … thrombocytopenia, red cell macrocytosis, predisposition to ALL* | Founding gene-discovery paper; triad; p.Pro214Leu/p.Arg418Gly; cytoplasmic mislocalization; dominant-negative mechanism |
| [26102509](https://pubmed.ncbi.nlm.nih.gov/26102509/) | *Germline ETV6 mutations confer susceptibility to ALL and thrombocytopenia* | Independent confirmation; impaired nuclear localization; somatic loss of WT allele |
| [27663637](https://pubmed.ncbi.nlm.nih.gov/27663637/) | *Germline ETV6 variants … reduced platelet formation, dysfunction, ↑CD34+* | Loss of repressor activity; ETS variants ↓corepressor binding; expanded MK-CFU, defective proplatelet formation |
| [28555414](https://pubmed.ncbi.nlm.nih.gov/28555414/) | *Germline ETV6 mutations and predisposition to hematological malignancies* | Clinical overview; THC5; 18 families; malignancy spectrum; surveillance |
| [34019812](https://pubmed.ncbi.nlm.nih.gov/34019812/) | *iPSC model of ETV6 vs RUNX1 thrombocytopenia* | ETV6 MKs overproduced-but-immature; shared proplatelet defect; distinct mechanisms |
| [35803545](https://pubmed.ncbi.nlm.nih.gov/35803545/) | *Germline ETV6 mutation promotes inflammation …* | CRISPR knock-in mouse; MPP4 defect; IL-18/IL-13; leukemogenesis model |
| [9694803](https://pubmed.ncbi.nlm.nih.gov/9694803/) | *TEL/ETV6 required specifically for bone-marrow hematopoiesis* | Normal ETV6 role; KO embryonic lethality |
| [40670159](https://pubmed.ncbi.nlm.nih.gov/40670159/) | *Inherited thrombocytopenia with malignancy risk* | 10–45% HM risk; impaired aggregation in 90%; ~20-yr diagnostic delay |
| [40858768](https://pubmed.ncbi.nlm.nih.gov/40858768/) | *Rare germline ETV6 variant … thrombocytopenia and acute leukemia* | p.Leu376Gln; fibroblast germline confirmation; variable expressivity; solid tumors |
| [36279069](https://pubmed.ncbi.nlm.nih.gov/36279069/) | *Germline predisposition syndromes in hematologic malignancies* | Surveillance + carrier-aware donor selection |
| [37913908](https://pubmed.ncbi.nlm.nih.gov/37913908/) | *Donor-derived malignancy risks in allo-HSCT* | Screening related donors |
| [42418371](https://pubmed.ncbi.nlm.nih.gov/42418371/) | *Germline testing for children undergoing HCT* | 1/5 recipients of variant-positive relative donor developed donor-derived leukemia |
| [31249973](https://pubmed.ncbi.nlm.nih.gov/31249973/) | *Targeted NGS for platelet disorders* | 59-gene panel diagnostic modality |
| [42479114](https://pubmed.ncbi.nlm.nih.gov/42479114/) | *Functional analysis of rare ETV6 germline variants* | Variant-level functional assays; p.Arg202Gly WT-like vs p.Pro214Leu LOF |
| [28594466](https://pubmed.ncbi.nlm.nih.gov/28594466/) | *Bleeding is not the main issue in inherited thrombocytopenias* | Malignancy, not bleeding, dominates concern |
| [42296844](https://pubmed.ncbi.nlm.nih.gov/42296844/) | *MULi001-A iPSC line, ETV6 p.Pro214Leu* | Patient iPSC resource |

**Evidence-type summary:** Human clinical/family studies ([25807284](https://pubmed.ncbi.nlm.nih.gov/25807284/), [26102509](https://pubmed.ncbi.nlm.nih.gov/26102509/), [27663637](https://pubmed.ncbi.nlm.nih.gov/27663637/), [40670159](https://pubmed.ncbi.nlm.nih.gov/40670159/), [40858768](https://pubmed.ncbi.nlm.nih.gov/40858768/)); model organism ([9694803](https://pubmed.ncbi.nlm.nih.gov/9694803/), [35803545](https://pubmed.ncbi.nlm.nih.gov/35803545/)); in vitro/iPSC ([34019812](https://pubmed.ncbi.nlm.nih.gov/34019812/), [42479114](https://pubmed.ncbi.nlm.nih.gov/42479114/), [42296844](https://pubmed.ncbi.nlm.nih.gov/42296844/)); clinical-practice/transplant ([28555414](https://pubmed.ncbi.nlm.nih.gov/28555414/), [36279069](https://pubmed.ncbi.nlm.nih.gov/36279069/), [37913908](https://pubmed.ncbi.nlm.nih.gov/37913908/), [42418371](https://pubmed.ncbi.nlm.nih.gov/42418371/)).

---

## Limitations and Knowledge Gaps

1. **Epidemiology is unquantified.** Only ~18 families were reported by 2017; no reliable prevalence/incidence estimates, no established founder populations, no sex/ethnic distribution data. Carrier frequency unknown (variants absent from gnomAD).
2. **Penetrance estimates are borrowed.** The quoted 10–45% malignancy risk is for the combined ETV6/RUNX1/ANKRD26 group; ETV6-specific, age-stratified penetrance is not precisely defined given small cohorts.
3. **Variant interpretation is difficult.** Rare *ETV6* variants require functional assays; some (p.Arg202Gly) are WT-like despite leukemia co-occurrence, risking over-call of pathogenicity.
4. **The inflammation branch is model-derived.** The IL-18/IL-13 mechanism is demonstrated in the mouse knock-in; its contribution to human thrombocytopenia and leukemogenesis is inferred, not clinically proven.
5. **No therapeutics target the germline defect.** Management is entirely supportive/surveillance-based; no validated prognostic biomarker predicts which carriers will transform.
6. **Modifier genes and epigenetics are unexplored** for this disorder.

---

## Proposed Follow-up Experiments / Actions

1. **Build an international ETV6-RT registry** to generate gene-specific, age-stratified penetrance for B-ALL vs MDS/AML and genotype–phenotype correlations (central-domain vs ETS-domain variants).
2. **Systematic functional classification** of all reported *ETV6* variants using standardized localization + reporter assays (MMP3/PF4 promoters), building an evidence-based pathogenicity framework to reduce VUS and over-calling ([PMID: 42479114](https://pubmed.ncbi.nlm.nih.gov/42479114/)).
3. **Test the IL-18/IL-13 axis as a therapeutic target** in the knock-in mouse and patient iPSC systems — e.g., IL-18/IL-13 blockade to assess rescue of lymphoid development and thrombopoiesis ([PMID: 35803545](https://pubmed.ncbi.nlm.nih.gov/35803545/)).
4. **Single-cell and longitudinal clonal tracking** of carrier bone marrow to detect pre-leukemic second hits (wild-type *ETV6* loss) early, enabling risk-adapted surveillance.
5. **Formalize carrier-aware HSCT donor screening** into guidelines and prospectively quantify donor-derived leukemia risk, building on the 1/5 signal ([PMID: 42418371](https://pubmed.ncbi.nlm.nih.gov/42418371/)).
6. **Define optimal surveillance intervals** (CBC, marrow evaluation) through natural-history study, since no evidence-based schedule currently exists.

---

*Report compiled from 14 confirmed findings and 30 reviewed papers over 5 investigation iterations. All mechanistic and clinical claims are attributed to primary literature with verified PMID citations.*


## Artifacts

- [OpenScientist final report](ETV6-Related_Thrombocytopenia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ETV6-Related_Thrombocytopenia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 15 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014536` (2 mentions) - the report calls it "MONDO"; MONDO calls it **thrombocytopenia 5**
- `HP:0001873` (1 mention) - the report calls it "Laboratory abnormality / clinical sign"; HP calls it **Thrombocytopenia**
- `HP:0001972` (1 mention) - the report calls it "Laboratory abnormality"; HP calls it **Macrocytic anemia**
- `HP:0003540` (1 mention) - the report calls it "Laboratory abnormality"; HP calls it **Impaired platelet aggregation**
- `HP:0001892` (1 mention) - the report calls it "Symptom / clinical sign"; HP calls it **Abnormal bleeding**
- `HP:0006721` (1 mention) - the report calls it "Neoplasm"; HP calls it **Acute lymphoblastic leukemia**
- `HP:0004808` (1 mention) - the report calls it "Neoplasm"; HP calls it **Acute myeloid leukemia**
- `GO:0005737` (2 mentions) - the report calls it "cytoplasm — aberrant localization", "cytoplasm"; GO calls it **cytoplasm**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002863` (1 mention) - the report calls it "Neoplasm"; HP calls it **Myelodysplasia**
- `GO:0000122` (1 mention) - the report calls it "DNA-binding transcriptional repression"; GO calls it **negative regulation of transcription by RNA polymerase II**
- `GO:0006357` (1 mention) - the report calls it "regulation of transcription by RNA Pol II"; GO calls it **regulation of transcription by RNA polymerase II**
- `GO:0050729` (1 mention) - the report calls it "positive regulation of inflammatory response — IL-18/IL-13 branch"; GO calls it **positive regulation of inflammatory response**
- `GO:0005634` (2 mentions) - the report calls it "nucleus — normal site", "nucleus"; GO calls it **nucleus**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005634` - called "nucleus — normal site", "nucleus"
- `GO:0005737` - called "cytoplasm — aberrant localization", "cytoplasm"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.