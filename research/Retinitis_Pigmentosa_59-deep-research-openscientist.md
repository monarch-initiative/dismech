---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-30T19:29:59.765584'
end_time: '2026-09-30T20:17:24.286990'
duration_seconds: 2844.52
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Retinitis Pigmentosa 59
  mondo_id: MONDO:0013468
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
citation_count: 17
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 13
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 28
  verified: 26
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 1
  labels_mismatched: 12
  mislabelled_terms:
  - term_id: MONDO:0013468
    reported_labels:
    - MONDO
    ontology_label: retinitis pigmentosa 59
  - term_id: HP:0000662
    reported_labels:
    - Symptom
    ontology_label: Nyctalopia
  - term_id: HP:0000510
    reported_labels:
    - Clinical sign
    ontology_label: Rod-cone dystrophy
  - term_id: HP:0001133
    reported_labels:
    - Clinical sign
    ontology_label: Constriction of peripheral visual field
  - term_id: HP:0007737
    reported_labels:
    - Physical manifestation
    ontology_label: Spicular pigmentation of the retina
  - term_id: HP:0000512
    reported_labels:
    - Lab/functional
    ontology_label: Abnormal electroretinogram
  - term_id: HP:0007663
    reported_labels:
    - Symptom/sign
    ontology_label: Reduced visual acuity
  - term_id: HP:0000608
    reported_labels:
    - Clinical sign
    ontology_label: Macular degeneration
  - term_id: HP:0007894
    reported_labels:
    - Clinical sign
    ontology_label: Fundus hypopigmentation
  - term_id: UBERON:0000966
    reported_labels:
    - retina
    - "Organ level:** Eye \u2014 specifically the **retina"
    ontology_label: retina
  - term_id: NCIT:C233
    reported_labels:
    - Acetazolamide
    ontology_label: Aminoglutethimide
  - term_id: NCIT:C61796
    reported_labels:
    - N-Acetylcysteine
    ontology_label: Ivermectin
  labels_variant: 2
  obsolete_terms:
  - term_id: GO:0019408
    ontology_label: obsolete dolichol biosynthetic process
    replaced_by: GO:0043048
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Retinitis_Pigmentosa_59-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Retinitis_Pigmentosa_59-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Retinitis Pigmentosa 59
- **MONDO ID:** MONDO:0013468 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Retinitis Pigmentosa 59** covering all of the
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

# Retinitis Pigmentosa 59 (RP59): A Comprehensive Disease Characteristics Report

**Disease:** Retinitis Pigmentosa 59 | **OMIM:** #613861 | **MONDO:** MONDO:0013468 | **Gene:** *DHDDS* (OMIM \*608172) | **Category:** Mendelian (autosomal recessive)

---

## Summary

Retinitis Pigmentosa 59 (RP59) is a rare, non-syndromic, autosomal recessive rod–cone dystrophy caused by biallelic missense variants in **DHDDS** (dehydrodolichyl diphosphate synthase), the catalytic subunit of the endoplasmic-reticulum **cis-prenyltransferase (cis-PT)** complex that synthesizes dolichol — the obligate lipid carrier for protein N-glycosylation. The disease is defined biochemically by a hypomorphic enzymatic defect: the recurrent **K42E (c.124A>G, p.Lys42Glu)** allele lowers catalytic efficiency and shortens dolichol chains (yielding a diagnostic elevation of the dolichol-18/dolichol-19 ratio) **without** producing a gross serum hypoglycosylation defect. K42E is an **Ashkenazi Jewish (AJ) founder mutation**, accounting for ~33% of genetically solved AJ retinitis pigmentosa families and carried by roughly **1 in 91 people of AJ ancestry** (gnomAD v4 ASJ allele frequency 0.55%).

Clinically, RP59 presents as a classic rod-cone dystrophy — night blindness, progressive peripheral-then-central visual-field loss, bone-spicule retinal pigmentation, and an attenuated or extinguished electroretinogram (ERG) — but with **unusually prominent macular and retinal-pigment-epithelium (RPE) involvement** that gives a distinctive fundus autofluorescence signature. This distinguishes DHDDS-RP from other genetic RP subtypes and hints at a mechanism extending beyond pure photoreceptor loss. Multiple knock-in and conditional mouse models (K42E, T206A, RPE-specific *Dhdds* ablation) localize early pathology to the **inner retina** — thinning of the inner nuclear layer, reduced bipolar/amacrine cell densities, and defective photoreceptor-to-bipolar synaptic transmission — as well as to the RPE, rather than to primary outer-segment degeneration.

There is currently **no gene-specific cure**. Management is supportive: carbonic-anhydrase inhibitors for cystoid macular edema, cataract surgery, low-vision rehabilitation, and genetic counseling with founder-variant carrier screening in Ashkenazi Jews. Antioxidant (N-acetylcysteine) and broad gene-based therapies for RP are in development. Importantly, *DHDDS* is an allelic locus for a **separate, dominant, de novo neurodevelopmental/neurodegenerative disorder (DEDSM)** — developmental delay, epilepsy, myoclonus, and movement disorder — which is mechanistically and genetically distinct from recessive RP59.

---

## Section 1 — Disease Information

**Overview.** RP59 is a specific, rare, autosomal recessive, non-syndromic subtype of retinitis pigmentosa. Retinitis pigmentosa as a whole is a leading cause of inherited visual disability with a worldwide prevalence of approximately **1:4000** ([PMID: 29597005](https://pubmed.ncbi.nlm.nih.gov/29597005/); *"RP is a leading cause of visual disability, with a worldwide prevalence of 1:4000."*). RP59 is defined by biallelic pathogenic variants in *DHDDS*.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM (disease) | #613861 (Retinitis pigmentosa 59) |
| OMIM (gene) | \*608172 (*DHDDS*) |
| MONDO | MONDO:0013468 |
| HGNC | HGNC:20603 (*DHDDS*) |
| UniProt | Q86SQ9 (DHDDS protein) |
| Gene locus | Chromosome 1p36.11 |
| dbSNP (K42E) | rs147394623 |

**Synonyms / alternative names.** RP59; DHDDS-related retinitis pigmentosa; DHDDS-associated inherited retinal degeneration (IRD). The broader *DHDDS* disease spectrum also includes DHDDS-congenital disorder of glycosylation (DHDDS-CDG) and DEDSM (developmental delay and seizures with or without movement abnormalities).

**Source of information.** The knowledge here is derived from aggregated disease-level resources (OMIM, Orphanet, gnomAD) and primary literature (case series, family-based whole-exome studies, biochemical and animal-model work), not from individual EHR records.

---

## Section 2 — Etiology

**Disease causal factors.** RP59 is a **monogenic Mendelian disorder** caused by biallelic (homozygous or compound heterozygous) pathogenic missense variants in *DHDDS*. Whole-exome sequencing of an Ashkenazi Jewish family with 3 of 4 affected siblings identified a homozygous **c.124A>G (p.Lys42Glu, K42E)** variant as causal ([PMID: 24664694](https://pubmed.ncbi.nlm.nih.gov/24664694/); *"A single-nucleotide mutation in the gene that encodes DHDDS has been identified by whole exome sequencing as the cause of the non-syndromic recessive retinitis pigmentosa (RP) in a family of Ashkenazi Jewish origin..."*). Reported RP59-causing genotypes include **K42E/K42E, T206A/K42E, and R98W/K42E** ([PMID: 40574710](https://pubmed.ncbi.nlm.nih.gov/40574710/); *"three variant alleles (K42E/K42E, T206A/K42E and R98W/K42E) have been reported to cause retinitis pigmentosa 59 (RP59)"*).

**Genetic risk factors.** The single dominant genetic risk factor is inheritance of two pathogenic *DHDDS* alleles. The **K42E founder allele** dramatically elevates carrier risk in individuals of Ashkenazi Jewish ancestry (see Sections 4 and 9). Modifier genes in the glycosylation pathway (notably *ALG6*) influence expressivity (Section 4).

**Environmental risk factors.** No established environmental risk factors initiate RP59; the disease is fully genetically determined. General retinal-health factors (e.g., light exposure, oxidative stress) may modulate progression but are not documented as specific RP59 risk factors.

**Protective factors.** No validated genetic or environmental protective alleles specific to RP59 are documented. Modifier alleles can shift severity in either direction (e.g., *ALG6* F304S was associated with **less** peripheral rod disease even while worsening macular cone disease; [PMID: 38256083](https://pubmed.ncbi.nlm.nih.gov/38256083/)).

**Gene–environment interactions.** No specific gene-environment interaction has been established for RP59. The dominant modulatory interactions are **gene–gene** (glycosylation-pathway modifiers).

---

## Section 3 — Phenotypes

RP59 manifests as a progressive rod-cone dystrophy with added macular/RPE features. Key phenotypes, with suggested HPO terms:

| Phenotype | Type | HPO term | Onset / progression | Frequency |
|---|---|---|---|---|
| Night blindness (nyctalopia) | Symptom | HP:0000662 | Early, progressive | Characteristic/typical |
| Rod-cone dystrophy | Clinical sign | HP:0000510 | Early-onset, progressive | Defining feature |
| Constriction of visual field | Clinical sign | HP:0001133 | Peripheral→central, progressive | Typical |
| Bone-spicule retinal pigmentation | Physical manifestation | HP:0007737 | Progressive | Typical |
| Abnormal/attenuated or absent ERG | Lab/functional | HP:0000512 | Early, progressive | Typical/severe |
| Reduced visual acuity | Symptom/sign | HP:0007663 | Progressive, worse & earlier than MAK-RP | Common |
| Macular degeneration / maculopathy | Clinical sign | HP:0000608 | Prominent in DHDDS-RP | Characteristic |
| Retinal pigment epithelial atrophy | Clinical sign | HP:0007894 | Progressive | Common |

**Characteristics.** DHDDS-RP59 patients exhibit **classic RP symptoms** (night blindness, progressive peripheral then central visual field loss, bone-spicule pigmentation, attenuated ERG) **plus macular changes suggestive of RPE involvement** ([PMID: 32245241](https://pubmed.ncbi.nlm.nih.gov/32245241/); *"Patients with certain defects in the dehydrodolichyl diphosphate synthase (DHDDS) gene (RP59; OMIM #613861) exhibit classic symptoms of retinitis pigmentosa, as well as macular changes, suggestive of retinal pigment epithelium (RPE) involvement."*). On ultra-widefield fundus autofluorescence (FAF), DHDDS patients (n=12) had a **significantly more abnormal macular FAF pattern and more widespread decreased peripheral autofluorescence** than MAK or FAM161A RP patients (macular abnormality p=0.001) ([PMID: 35501492](https://pubmed.ncbi.nlm.nih.gov/35501492/); *"DHDDS patients had a more abnormal macular FAF pattern and more widespread decrease in peripheral autofluorescence."*). DHDDS patients tend to have **worse visual acuity and visual fields at younger ages than MAK patients** ([PMID: 29276052](https://pubmed.ncbi.nlm.nih.gov/29276052/)), indicating relatively severe, earlier expressivity.

**Severity / progression.** Severity is **moderate-to-severe and progressive**, with variable expressivity influenced by modifier genes. Onset is early (see Section 8).

**Quality-of-life impact.** Progressive constriction of the visual field and central vision loss lead to loss of independent mobility, driving cessation, reading difficulty, and eventual legal blindness — substantial impacts on daily functioning. Disease-specific QoL instrument data for RP59 specifically were not identified; general RP QoL burden applies.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *DHDDS* (dehydrodolichyl diphosphate synthase), chromosome 1p36.11, OMIM \*608172, HGNC:20603, UniProt Q86SQ9.

**Pathogenic variants.**

| Variant | HGVS (NM_024887.4) | Protein | Type | Role |
|---|---|---|---|---|
| K42E | c.124A>G | p.Lys42Glu | Missense | Founder hypomorph; most common RP59 allele |
| T206A | c.616A>G | p.Thr206Ala | Missense | RP59 in trans with K42E or homozygous |
| R98W | — | p.Arg98Trp | Missense | RP59 in trans with K42E |

The K42E variant changes the **highly conserved residue Lys42 to Glu, resulting in lower catalytic efficiency** ([PMID: 24664694](https://pubmed.ncbi.nlm.nih.gov/24664694/)) — i.e., a **hypomorphic, partial loss-of-function** allele rather than a null. Biallelic null/severe-hypomorphic combinations (e.g., nonsense + splice) instead cause fatal infantile DHDDS-CDG, indicating an allelic dosage/severity spectrum.

**Variant classification (ACMG/AMP).** K42E is classified **pathogenic** for RP59 given segregation, functional enzyme data, and biochemical biomarker evidence. T206A and R98W are pathogenic/likely-pathogenic in the recessive RP context.

**Allele frequency (gnomAD v4; computational/database evidence — Finding F012).** Direct query of gnomAD v4 for variant 1-26438228-A-G (rs147394623) returns:

| Population | Allele frequency | Allele count |
|---|---|---|
| Global (exomes) | 1.29×10⁻⁴ | 188 / 1,461,728 |
| **Ashkenazi Jewish (ASJ)** | **0.555%** | 145 / 26,132 |
| Non-Finnish European | 2.2×10⁻⁵ | 24 / 1,111,908 |
| African / East Asian / South Asian / Finnish / Mid-Eastern | ~absent | — |

This is a **~257-fold ASJ-vs-NFE enrichment**. Predicted ASJ carrier frequency ≈ 2pq ≈ **1.1% (~1 in 91)**; predicted ASJ homozygote (affected) frequency q² ≈ **1 in ~32,000** before accounting for compound heterozygosity with T206A/R98W.

**Functional consequence.** Partial **loss of function** (reduced catalytic efficiency of cis-PT), not gain-of-function or dominant-negative, in the recessive RP context.

**Modifier genes.** In 11 K42E-IRD patients, an **ALG6 modifier variant (F304S)** correlated with **greater macular cone disease severity but less peripheral rod disease severity**, showing that glycosylation-pathway modifier genes influence RP59 expressivity ([PMID: 38256083](https://pubmed.ncbi.nlm.nih.gov/38256083/)). Additional candidate modifiers tested include *ALG8, DDOST, MPDU1, TNKS*.

**Epigenetic information / chromosomal abnormalities.** No disease-specific DNA-methylation, histone, or large-scale chromosomal abnormality is documented for RP59; it is a point-mutation monogenic disorder.

---

## Section 5 — Environmental Information

No environmental toxins, radiation, pollution, occupational exposures, lifestyle factors, or infectious agents are established as causes or triggers of RP59. The disease is entirely genetically determined by biallelic *DHDDS* variants. (This section is **not applicable** beyond general retinal-health considerations.)

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic hypomorphic *DHDDS* variants (e.g., K42E)** → reduce the **catalytic efficiency** of the DHDDS subunit of cis-prenyltransferase (*demonstrated* — enzyme assays, [PMID: 24664694]).
2. Reduced cis-PT activity → **impaired synthesis of dehydrodolichyl diphosphate**, the precursor of dolichol (*demonstrated* — enzymology/structure, [PMID: 33077723]).
3. Impaired dolichol synthesis → **characteristic shortening of dolichol chains**, with dolichol-18 replacing normal dolichol-19 (elevated D18/D19 ratio) in plasma/urine/retina (*demonstrated* — LC-MS in patients and mice, [PMID: 24078709]; [PMID: 37443173]).
4. Branch A — **N-glycosylation**: In RP59, dolichol shortening does **NOT** cause gross serum hypoglycosylation (transferrin isoelectric focusing normal; [PMID: 24664694]). This distinguishes RP59 from severe DHDDS-CDG.
5. Branch B — **Retinal/RPE pathology** (the clinically relevant path): altered dolichol metabolism → **inner-retinal dysfunction** with defective photoreceptor-to-bipolar synaptic transmission, inner nuclear layer thinning, and bipolar/amacrine cell loss (*demonstrated in mouse models*, inferred for humans; [PMID: 37443173]; [PMID: 40574710]) **and** RPE atrophy/dysfunction (*demonstrated* in RPE-specific ablation mice; [PMID: 32245241]).
6. Inner-retinal + RPE dysfunction → **progressive rod-cone degeneration, macular/RPE involvement, and abnormal ERG/FAF** → clinical **night blindness, field constriction, central vision loss** (*clinical manifestation*).

### Detail by category

**Molecular pathways / biochemistry.** DHDDS is the catalytic subunit of the human cis-prenyltransferase (with NgBR/NUS1), synthesizing **dehydrodolichyl diphosphate**, the precursor of **dolichol**, the obligate lipid carrier for N-glycosylation ([PMID: 33077723](https://pubmed.ncbi.nlm.nih.gov/33077723/); *"The human cis-prenyltransferase (hcis-PT) is an enzymatic complex essential for protein N-glycosylation. Synthesizing the precursor of the glycosyl carrier dolichol-phosphate, mutations in hcis-PT cause severe human diseases."*). The enzyme operates in the isoprenoid/dolichol arm of the mevalonate pathway. GO terms: **di-trans,poly-cis-decaprenylcistransferase activity (GO:0045547)**, **dolichol biosynthetic process (GO:0019408)**, **ER membrane (GO:0005789)**.

**Protein dysfunction / structure.** The human cis-PT is a **heterotetramer** of two catalytic DHDDS subunits and two inactive **Nogo-B receptor (NgBR, gene NUS1)** subunits, assembling via DHDDS C-termini as a **dimer-of-heterodimers**; the NgBR distal C-terminus crosses the interface to help form the DHDDS active site (2.3 Å crystal structure; [PMID: 33077723](https://pubmed.ncbi.nlm.nih.gov/33077723/); *"the 2.3 Å crystal structure reveals that the tetramer assembles via the DHDDS C-termini as a dimer-of-heterodimers"*). **Disease mutations cluster around the active site**, and molecular-dynamics simulations propose a mechanism for hcis-PT dysfunction in RP ([PMID: 33077723](https://pubmed.ncbi.nlm.nih.gov/33077723/); *"we explored the functional consequences of disease mutations clustered around the active-site... we propose a mechanism for hcis-PT dysfunction in retinitis pigmentosa"*). K42 is a highly conserved residue; K42E is a hypomorphic partial loss-of-function change.

**Cellular processes / tissue damage.** Mouse models show **elevated expression of synaptogenesis/synaptic genes**, progressive reduction of inner nuclear layer (INL) and total retinal thickness from ~postnatal 2 months, and INL/outer plexiform layer cell loss — **without profound photoreceptor outer-segment degeneration or N-glycosylation defect** ([PMID: 37443173](https://pubmed.ncbi.nlm.nih.gov/37443173/); *"Quantitative retinal cell layer thickness measurements demonstrated a significant reduction in the inner nuclear layer (INL) and total retinal thickness (TRT) beginning at postnatal (PN) ∼2 months"*). T206A/T206A, T206A/K42E and K42E/K42E mice show reduced INL thickness, reduced ERG b-waves with relatively spared a-waves, attenuated c- and d-waves, and reduced bipolar/amacrine densities. The authors **propose that RP59 dysfunction involves defective photoreceptor-to-bipolar synaptic transmission with concomitant bipolar/amacrine cell degeneration** ([PMID: 40574710](https://pubmed.ncbi.nlm.nih.gov/40574710/); *"We propose that the physiological basis of retinal dysfunction in RP59 involves defective photoreceptor to bipolar cell synaptic transmission with concomitant bipolar/amacrine cell degeneration."*).

**RPE contribution.** Selective *Dhdds* ablation in mouse RPE causes **RPE atrophy, hyper-reflectivity, transmigration into the photoreceptor layer, and scotopic a-/b-wave reductions of 83%/77% at 3 months** ([PMID: 32245241](https://pubmed.ncbi.nlm.nih.gov/32245241/)), directly demonstrating an RPE-autonomous component consistent with the macular/RPE phenotype seen in patients.

**Cell types (CL) and biological processes (GO).** Cell types: photoreceptor (CL:0000210), rod (CL:0000604), cone (CL:0000573), retinal bipolar neuron (CL:0000748), amacrine cell (CL:0000561), retinal pigment epithelial cell (CL:0002586). Biological processes: dolichol biosynthetic process (GO:0019408), protein N-linked glycosylation (GO:0006487), synaptic transmission / photoreceptor cell maintenance.

**Immune / metabolic / epigenetic.** No autoimmune or infectious mechanism. The core metabolic defect is in **isoprenoid/dolichol lipid metabolism**. No RP59-specific epigenetic mechanism is documented.

---

## Section 7 — Anatomical Structures Affected

- **Organ level:** Eye — specifically the **retina** (UBERON:0000966) and **retinal pigment epithelium** (UBERON:0001782). Body system: **visual/nervous system**. RP59 is non-syndromic — no secondary organ involvement in the classic recessive form (contrast: DHDDS-CDG and DEDSM involve the CNS).
- **Tissue/cell level:** Neural retina (nervous tissue) and RPE (epithelial tissue). Affected cell populations: rods, cones, **retinal bipolar neurons (CL:0000748)** and **amacrine cells (CL:0000561)** (inner retina), and **RPE cells (CL:0002586)**. The inner-nuclear-layer emphasis is a distinctive feature relative to classic outer-retinal RP.
- **Subcellular level:** **Endoplasmic reticulum membrane (GO:0005789)**, where cis-PT resides and dolichol is synthesized; photoreceptor outer segments and synaptic terminals (outer plexiform layer) are functionally implicated.
- **Localization:** **Bilateral**, roughly symmetric retinal involvement, with prominent **macular** (central) plus peripheral involvement. UBERON: retina (UBERON:0000966), macula lutea (UBERON:0005388), RPE (UBERON:0001782).

---

## Section 8 — Temporal Development

- **Onset:** Early-onset retinal degeneration; the index AJ family had **early-onset** disease in 3 of 4 affected siblings ([PMID: 24664694]). RP typically manifests with **night blindness in adolescence**, followed by concentric visual field loss ([PMID: 29597005](https://pubmed.ncbi.nlm.nih.gov/29597005/)). DHDDS patients tend to have worse acuity/fields at **younger ages** than MAK patients ([PMID: 29276052]).
- **Onset pattern:** Insidious, chronic.
- **Progression:** Progressive and centripetal — *"RP typically manifests with night blindness in adolescence, followed by concentric visual field loss, reflecting the principal dysfunction of rod photoreceptors; central vision loss occurs later in life due to cone dysfunction"* ([PMID: 29597005](https://pubmed.ncbi.nlm.nih.gov/29597005/)). Stages: early (nyctalopia, mid-peripheral field loss) → intermediate (ring scotoma, tunnel vision) → advanced (central vision loss, near-extinguished ERG) → end-stage (legal blindness).
- **Course / duration:** Chronic, lifelong, progressive.
- **Remission / critical periods:** No spontaneous remission. Early intervention (before substantial cell loss) is the theoretical window for future gene/cell therapies; mouse INL thinning begins ~PN 2 months, defining an early structural window.

---

## Section 9 — Inheritance and Population

- **Epidemiology:** RP overall prevalence ~**1:4000** ([PMID: 29597005]). RP59 is a specific **rare** autosomal recessive subtype; precise population incidence/prevalence of RP59 is not separately established, but it is enriched in Ashkenazi Jews. Among 230 AJ RP families, a cause was found in **37%**, and K42E was present in **33%** of solved families (second only to the MAK Alu insertion at 39%) ([PMID: 29276052](https://pubmed.ncbi.nlm.nih.gov/29276052/); *"...c.124A>G, p.K42E in dehydrodolichol diphosphate synthase (DHDDS) (33%)."*).
- **Inheritance:** **Autosomal recessive** with essentially complete penetrance in biallelic carriers.
- **Penetrance / expressivity:** High/complete penetrance; **variable expressivity** modulated by modifiers (e.g., *ALG6*; [PMID: 38256083]).
- **Founder effect:** K42E is an **Ashkenazi Jewish founder allele** (gnomAD ASJ AF 0.555%; ~257-fold over NFE; Finding F012). Carrier frequency ~**1 in 91** in AJ ancestry.
- **Consanguinity:** Founder homozygosity (rather than classical consanguinity) underlies most AJ cases; consanguinity contributes in recessive RP broadly.
- **Sex ratio:** No sex predilection (autosomal).
- **Geographic/ethnic distribution:** Concentrated in Ashkenazi Jewish populations; the variant is essentially absent in African, East Asian, South Asian, Finnish, and Mid-Eastern subsets (gnomAD v4).

---

## Section 10 — Diagnostics

Diagnosis rests on **three complementary pillars** (Finding F011):

1. **Clinical RP evaluation** — fundus exam (bone-spicule pigment, attenuated vessels, waxy disc pallor); **full-field ERG** (reduced/absent scotopic and photopic responses); visual fields; **OCT** (outer retinal layer loss, macular changes); and **fundus autofluorescence** showing a **distinctive abnormal macular pattern and widespread peripheral decreased autofluorescence** ([PMID: 35501492](https://pubmed.ncbi.nlm.nih.gov/35501492/)).
2. **Biochemical biomarker — dolichol profiling.** LC-MS of plasma/urine shows a **characteristic shortening of dolichols** with an elevated **D18/D19 ratio** that discriminates patients > carriers > normals by ROC analysis ([PMID: 24078709](https://pubmed.ncbi.nlm.nih.gov/24078709/); *"We observed a characteristic shortening of plasma and urinary dolichols in retinitis pigmentosa (RP) patients carrying K42E and T206A mutations..."*). Crucially, *"Dolichol profiling, complementary to genotyping, can be readily adapted as a test in the clinic not only for the diagnosis of patients but also for identification of carriers with DHDDS or other genetic mutations that may impair dolichol biosynthesis."* ([PMID: 24078709]).
3. **Molecular genetic testing** — targeted single-variant testing for the AJ founder **K42E**, RP/IRD gene panels, or whole-exome/genome sequencing ([PMID: 24664694]).

**Important negative test:** Standard serum **transferrin isoelectric focusing is typically normal** in RP59 — *"Patterns of plasma transferrin isoelectric focusing gel were normal in all family members, indicating no significant abnormality in protein glycosylation"* ([PMID: 24664694](https://pubmed.ncbi.nlm.nih.gov/24664694/)) — so routine CDG screening will miss RP59; dolichol profiling and/or genetics are required.

**Differential diagnosis:** other genetic RP subtypes (MAK, FAM161A, USH2A, RPGR), Leber congenital amaurosis, and acquired outer retinopathies (e.g., AZOOR) — distinguished by genotype and the distinctive DHDDS FAF/macular pattern.

**Screening:** Ashkenazi Jewish **carrier screening** for K42E (and cascade family testing) is the key preventive-diagnostic measure.

CHEBI terms: dolichol (CHEBI:16091), dolichyl phosphate (CHEBI:57683).

---

## Section 11 — Outcome / Prognosis

- **Survival/mortality:** RP59 is **not life-limiting** in its non-syndromic recessive form; no excess mortality. (Contrast: severe biallelic DHDDS-CDG can be fatal in infancy.)
- **Morbidity/function:** Progressive, potentially severe **visual disability** culminating in legal blindness; DHDDS patients trend toward worse acuity/fields at younger ages than MAK-RP ([PMID: 29276052]).
- **Disease course/complications:** Cystoid macular edema, cataract, and posterior subcapsular lens changes are common RP complications affecting central vision.
- **Prognostic factors:** Genotype (K42E/K42E vs compound heterozygous), modifier alleles (*ALG6* F304S shifts macular vs peripheral severity; [PMID: 38256083]), and age at presentation.
- **Prognostic biomarker:** Dolichol D18/D19 ratio tracks the biochemical defect and could serve as a monitoring/prognostic marker (research use).

---

## Section 12 — Treatment

**There is no approved gene-specific therapy for DHDDS-RP59** (Finding F009). Management is supportive and symptomatic.

| Intervention | Evidence / role | NCIT (suggested) |
|---|---|---|
| Carbonic-anhydrase inhibitors (oral acetazolamide, methazolamide; topical dorzolamide) | **First-line for RP-associated cystoid macular edema.** Network meta-analysis (12 studies) found these reduced central macular thickness and improved BCVA at 3–4 months, outperforming anti-VEGF/steroids ([PMID: 42493417](https://pubmed.ncbi.nlm.nih.gov/42493417/); *"At 3-4 months, DEXi, acetazolamide, methazolamide and dorzolamide demonstrated comparable CMT reduction and outperformed anti-VEGF therapies"*) | Acetazolamide (NCIT:C233); Dorzolamide |
| N-acetylcysteine (NAC) | Antioxidant; Phase III **"NAC Attack"** trial ongoing for RP, targeting oxidative-stress-driven photoreceptor loss ([PMID: 39864434](https://pubmed.ncbi.nlm.nih.gov/39864434/); *"The ongoing multicentre Phase III trial 'NAC Attack' aims to evaluate the long-term efficacy and safety of NAC in RP."*) | N-Acetylcysteine (NCIT:C61796) |
| Low-vision rehabilitation, cataract surgery | Standard supportive care | Low Vision Aid |
| Gene / cell-based therapy | Investigational for RP broadly; none DHDDS-specific yet | Gene Therapy (NCIT:C15262) |
| Vitamin A palmitate | Debated in RP generally; **contraindicated in some genotypes** — use with caution | — |

Of note, acetazolamide improved systemic symptoms in a K42E DHDDS-CDG patient ([PMID: 36046393](https://pubmed.ncbi.nlm.nih.gov/36046393/)). **Personalized approach:** genotype-guided counseling and modifier-aware prognostication (*ALG6*) are emerging.

---

## Section 13 — Prevention

- **Primary prevention:** Not applicable to a Mendelian disorder in a born individual; **genetic counseling and Ashkenazi Jewish carrier screening** for K42E enable informed reproductive decisions (prenatal testing, preimplantation genetic diagnosis). Given ~1-in-91 AJ carrier frequency, population carrier screening is impactful.
- **Secondary prevention:** Early diagnosis (genetics + dolichol profiling + imaging) to monitor and treat complications (macular edema, cataract) before irreversible central vision loss.
- **Tertiary prevention:** Management of complications and low-vision rehabilitation to preserve function.
- **Counseling:** Autosomal-recessive risk counseling; cascade testing of relatives of probands.
- **Immunization / public health / environmental:** Not applicable.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy/orthologs:** *DHDDS* is highly conserved across eukaryotes; the enzyme's homology across species enables cross-species mechanistic study ([PMID: 28809830](https://pubmed.ncbi.nlm.nih.gov/28809830/)). Mouse *Dhdds* is the principal ortholog used for modeling.
- **Natural disease in other species:** No well-characterized spontaneous RP59-equivalent natural disease is documented in companion animals or wildlife; vertebrate models are engineered (see Section 15; reviewed in [PMID: 36362109](https://pubmed.ncbi.nlm.nih.gov/36362109/)).
- **Comparative biology:** The cis-PT/dolichol pathway is evolutionarily conserved from bacteria/yeast (rubber/undecaprenyl synthases) to humans, supporting strong conservation of disease mechanism.
- **Transmission / zoonosis:** Not applicable (genetic disease).

---

## Section 15 — Model Organisms

RP59 has a rich set of engineered models (reviewed in *Vertebrate Animal Models of RP59*, [PMID: 36362109](https://pubmed.ncbi.nlm.nih.gov/36362109/)).

| Model | Type | Key phenotype | Reference |
|---|---|---|---|
| **Dhdds K42E knock-in mouse** | Mammalian, knock-in | Shortened retina/liver/brain dolichols; INL & total retinal thinning from ~PN 2 mo; INL/OPL cell loss; **no** profound outer-segment degeneration or N-glycosylation defect; defective synaptic transmission | [PMID: 37443173](https://pubmed.ncbi.nlm.nih.gov/37443173/) |
| **Dhdds T206A & K42E knock-in mice (T206A/T206A, T206A/K42E, K42E/K42E)** | Mammalian, knock-in | Reduced INL thickness; reduced ERG b-waves with relatively spared a-waves; attenuated c-/d-waves; reduced bipolar/amacrine densities; **phenotypically similar** across genotypes | [PMID: 40574710](https://pubmed.ncbi.nlm.nih.gov/40574710/) |
| **RPE-specific Dhdds ablation mouse** | Mammalian, conditional KO | RPE atrophy, hyper-reflectivity, transmigration into photoreceptor layer; scotopic a-/b-wave reductions 83%/77% at 3 mo | [PMID: 32245241](https://pubmed.ncbi.nlm.nih.gov/32245241/) |
| **Patient-derived cells** | In vitro | Niemann-Pick C-like endolysosomal dysfunction; correctable by miglustat (in DHDDS-CDG context) | [PMID: 40003936](https://pubmed.ncbi.nlm.nih.gov/40003936/) |

**Phenotype recapitulation:** The knock-in models reproduce the **inner-retinal** and RPE features but, notably, do **not** show the profound photoreceptor degeneration classically expected of RP — a key insight redirecting the mechanistic focus to bipolar/amacrine synaptic pathology. **Limitations:** species differences in dolichol chain length and retinal architecture; incomplete modeling of human macular involvement (mice lack a macula).

---

## Mechanistic Model / Interpretation

```
Biallelic DHDDS hypomorph (K42E)
        │  (reduced catalytic efficiency — demonstrated)
        ▼
cis-PT (DHDDS2·NgBR2 heterotetramer) makes less
dehydrodolichyl-PP → less / shorter dolichol
        │  (elevated D18/D19 ratio — biomarker)
        ├──────────────► N-glycosylation LARGELY PRESERVED
        │                (normal transferrin IEF; no gross CDG)
        │
        └──────────────► RETINAL / RPE DYSFUNCTION
                          ├─ Inner retina: defective photoreceptor→bipolar
                          │   synaptic transmission; INL thinning;
                          │   bipolar/amacrine loss  (mouse-demonstrated)
                          └─ RPE: atrophy, transmigration  (mouse-demonstrated)
                                    │
                                    ▼
                    Progressive rod-cone dystrophy + macular/RPE disease
                    → nyctalopia, field constriction, central vision loss,
                      abnormal ERG/FAF  (human clinical)
```

The central, somewhat counterintuitive insight of RP59 biology is a **tissue-specific vulnerability paradox**: DHDDS is essential for N-glycosylation in *all* cells, yet the recessive hypomorphic K42E allele produces an **eye-restricted phenotype without gross systemic hypoglycosylation**. The retina — and specifically the inner-retinal synaptic circuitry and RPE — appears exquisitely sensitive to the partial reduction in dolichol supply. This contrasts with the **allelic dominant DEDSM** disorder (de novo *DHDDS* variants such as R211Q, R37H) that causes a neurodevelopmental/neurodegenerative syndrome with epilepsy, myoclonus, and movement disorder ([PMID: 34382076](https://pubmed.ncbi.nlm.nih.gov/34382076/); *"Patients presented during infancy or childhood with a variable association of neurodevelopmental disorder, generalized epilepsy, action myoclonus/cortical tremor and ataxia."*), and with severe biallelic null combinations that cause fatal infantile CDG. RP59 thus sits at the mild end of a *DHDDS* allelic dosage spectrum.

---

## Evidence Base

| PMID | Contribution | Supports |
|---|---|---|
| [24664694](https://pubmed.ncbi.nlm.nih.gov/24664694/) | WES identifies K42E as cause of recessive RP; reduced catalytic efficiency; normal transferrin IEF | F001, F003, F007, F011 |
| [40574710](https://pubmed.ncbi.nlm.nih.gov/40574710/) | RP59-causing genotypes; knock-in mice; inner-retinal synaptic mechanism | F001, F004 |
| [24078709](https://pubmed.ncbi.nlm.nih.gov/24078709/) | Dolichol chain shortening (D18/D19) as biomarker & carrier test | F003, F011 |
| [33077723](https://pubmed.ncbi.nlm.nih.gov/33077723/) | 2.3 Å cis-PT heterotetramer structure; mutations at active site | F003, F007 |
| [29276052](https://pubmed.ncbi.nlm.nih.gov/29276052/) | K42E = 33% of solved AJ RP; worse phenotype than MAK | F002, F006, F010 |
| [32245241](https://pubmed.ncbi.nlm.nih.gov/32245241/) | Macular/RPE involvement; RPE-ablation model (83%/77% ERG loss) | F006 |
| [35501492](https://pubmed.ncbi.nlm.nih.gov/35501492/) | Distinctive DHDDS FAF/macular signature | F006, F011 |
| [37443173](https://pubmed.ncbi.nlm.nih.gov/37443173/) | K42E knock-in: INL thinning, synaptic defect, no CDG | F003, F004 |
| [38256083](https://pubmed.ncbi.nlm.nih.gov/38256083/) | ALG6 F304S modifier of retinal severity | F008 |
| [34382076](https://pubmed.ncbi.nlm.nih.gov/34382076/) | De novo dominant DHDDS neurodevelopmental disorder (DEDSM) | F005, F008 |
| [40003936](https://pubmed.ncbi.nlm.nih.gov/40003936/) | DHDDS-NgBR dolichol role; endolysosomal dysfunction; miglustat | F005 |
| [36046393](https://pubmed.ncbi.nlm.nih.gov/36046393/) | Late-onset CDG from homozygous K42E; acetazolamide benefit | F008, F009 |
| [42493417](https://pubmed.ncbi.nlm.nih.gov/42493417/) | Carbonic-anhydrase inhibitors first-line for RP macular edema | F009 |
| [39864434](https://pubmed.ncbi.nlm.nih.gov/39864434/) | NAC Phase III "NAC Attack" antioxidant trial for RP | F009 |
| [29597005](https://pubmed.ncbi.nlm.nih.gov/29597005/) | RP prevalence 1:4000; natural history | F010 |
| [36362109](https://pubmed.ncbi.nlm.nih.gov/36362109/) | Review of RP59 vertebrate animal models | Section 15 |
| gnomAD v4 (computational) | K42E ASJ AF 0.555%; ~1 in 91 carriers; 257-fold enrichment | F012 |

---

## Limitations and Knowledge Gaps

1. **Tissue-specificity mechanism unresolved.** Why a ubiquitously required glycosylation enzyme causes an *eye-restricted*, largely non-glycosylation phenotype in RP59 is not mechanistically explained at the molecular level.
2. **Human inner-retinal pathology is inferred from mouse models.** The bipolar/amacrine synaptic mechanism ([PMID: 37443173]; [PMID: 40574710]) is demonstrated in mice; direct human histopathology confirmation is limited, and mice lack a macula (the very region most distinctively affected in patients).
3. **No RP59-specific prevalence/incidence figures.** Epidemiology is extrapolated from AJ RP cohorts and gnomAD carrier frequencies; true population penetrance and prevalence (including compound heterozygotes) are estimates.
4. **Limited genotype–phenotype data for non-K42E genotypes** (T206A, R98W) in humans.
5. **No dedicated QoL/natural-history longitudinal data** for RP59 specifically.
6. **Modifier landscape incomplete.** Only *ALG6* is validated; *ALG8, DDOST, MPDU1, TNKS* remain candidate modifiers.
7. **No disease-specific therapy** exists; the therapeutic pipeline (gene therapy, antioxidants) is generic to RP, not DHDDS-targeted.

---

## Proposed Follow-up Experiments / Actions

1. **Human retinal validation:** Use patient-derived retinal organoids/iPSC-RPE and, where available, donor retinal histopathology to confirm the inner-retinal/bipolar-synaptic mechanism and the RPE contribution in human tissue.
2. **Dolichol-supplementation / substrate-rescue trials:** Test whether dolichol or dolichyl-phosphate supplementation, or isoprenoid-pathway modulation, rescues the biochemical and functional phenotype in K42E knock-in mice and organoids.
3. **Gene-replacement therapy development:** AAV-*DHDDS* gene augmentation (targeting photoreceptors/bipolar cells and RPE) given the recessive loss-of-function mechanism and early therapeutic window (pre-PN-2-month structural change in mice).
4. **Prospective natural-history study** of genotyped RP59 patients with standardized OCT, FAF, ERG, visual fields, and QoL instruments, stratified by genotype and *ALG6* modifier status.
5. **Systematic modifier screen** (*ALG6, ALG8, DDOST, MPDU1, TNKS* and genome-wide) in larger K42E cohorts to build a severity-prediction model.
6. **Biomarker qualification:** Validate plasma/urinary D18/D19 dolichol ratio as a surrogate endpoint for therapeutic trials and as a clinical carrier-screening adjunct.
7. **Expand Ashkenazi Jewish carrier screening panels** to include DHDDS K42E (carrier ~1 in 91) alongside other AJ founder mutations, with cascade testing.


## Artifacts

- [OpenScientist final report](Retinitis_Pigmentosa_59-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Retinitis_Pigmentosa_59-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 15 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 12 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013468` (2 mentions) - the report calls it "MONDO"; MONDO calls it **retinitis pigmentosa 59**
- `HP:0000662` (1 mention) - the report calls it "Symptom"; HP calls it **Nyctalopia**
- `HP:0000510` (1 mention) - the report calls it "Clinical sign"; HP calls it **Rod-cone dystrophy**
- `HP:0001133` (1 mention) - the report calls it "Clinical sign"; HP calls it **Constriction of peripheral visual field**
- `HP:0007737` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Spicular pigmentation of the retina**
- `HP:0000512` (1 mention) - the report calls it "Lab/functional"; HP calls it **Abnormal electroretinogram**
- `HP:0007663` (1 mention) - the report calls it "Symptom/sign"; HP calls it **Reduced visual acuity**
- `HP:0000608` (1 mention) - the report calls it "Clinical sign"; HP calls it **Macular degeneration**
- `HP:0007894` (1 mention) - the report calls it "Clinical sign"; HP calls it **Fundus hypopigmentation**
- `UBERON:0000966` (2 mentions) - the report calls it "retina", "Organ level:** Eye — specifically the **retina"; UBERON calls it **retina**
- `NCIT:C233` (1 mention) - the report calls it "Acetazolamide"; NCIT calls it **Aminoglutethimide**
- `NCIT:C61796` (1 mention) - the report calls it "N-Acetylcysteine"; NCIT calls it **Ivermectin**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0019408` (obsolete dolichol biosynthetic process) (2 mentions) - replaced by `GO:0043048`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005789` (2 mentions) - the report calls it "Subcellular level:** **Endoplasmic reticulum membrane"; GO calls it **endoplasmic reticulum membrane**
- `NCIT:C15262` (1 mention) - the report calls it "Gene Therapy"; NCIT calls it **Immunotherapy**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0000966` - called "retina", "Organ level:** Eye — specifically the **retina"