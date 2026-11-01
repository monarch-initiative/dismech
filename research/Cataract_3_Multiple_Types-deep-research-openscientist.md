---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T08:57:47.404090'
end_time: '2026-10-31T09:12:02.431833'
duration_seconds: 855.03
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Cataract 3, Multiple Types
  mondo_id: MONDO:0011104
  category: Mendelian
  causal_genes: CRYBB2
  omim_id: OMIM:601547
  synonyms: cataract (disease) caused by mutation in CRYBB2; CRYBB2 cataract (disease);
    CTRCT3
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
citation_count: 30
reference_validation:
  total_references: 31
  verified: 31
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 31
  on_topic: 21
  validator_version: 0.4.0
term_validation:
  total_terms: 22
  verified: 21
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 3
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0011104
    reported_labels:
    - MONDO
    ontology_label: cataract 3 multiple types
  - term_id: HP:0000519
    reported_labels:
    - Congenital cataract
    - Localization & lateralization:** **bilateral** in the great majority
    ontology_label: Developmental cataract
  - term_id: HP:0000589
    reported_labels:
    - related
    ontology_label: Coloboma
  - term_id: GO:0005737
    reported_labels:
    - Subcellular level:** cytoplasm of fiber cells
    ontology_label: cytoplasm
  - term_id: CL:0000199
    reported_labels:
    - Tissue/cell level:** lens fiber cells
    ontology_label: mechanoreceptor cell
  labels_variant: 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Cataract_3_Multiple_Types-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Cataract_3_Multiple_Types-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cataract 3, Multiple Types
- **MONDO ID:** MONDO:0011104 (if available)
- **Causal gene(s):** CRYBB2
- **OMIM:** OMIM:601547
- **Synonyms:** cataract (disease) caused by mutation in CRYBB2; CRYBB2 cataract (disease); CTRCT3
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Cataract 3, Multiple Types** covering all of the
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

# Cataract 3, Multiple Types (CTRCT3) — Comprehensive Disease Characteristics Report

**Disease:** Cataract 3, Multiple Types (CTRCT3)
**Causal gene:** **CRYBB2** (β-B2-crystallin)
**MONDO:** MONDO:0011104 · **OMIM:** 601547 · **Gene MIM:** 123620 · **HGNC:** 2398 · **Chromosome:** 22q11.2–q12.1
**Category:** Mendelian, predominantly autosomal dominant

---

## Summary

**Cataract 3, Multiple Types (CTRCT3; OMIM 601547; MONDO:0011104) is a Mendelian, predominantly autosomal-dominant congenital/early-childhood cataract caused by mutations in CRYBB2, the gene encoding β-B2-crystallin — the most abundant β-crystallin of the ocular lens.** Although the serial disease name ("Cataract 3") does not itself name a gene, the MONDO ID and OMIM entry map unambiguously to CRYBB2 on chromosome 22q11.2–q12.1. A recurrent nonsense "hotspot" mutation, c.463C>T (p.Gln155*, also written Q155X; rs74315489) in exon 6, has been found independently in ethnically distinct families (American, Swiss, Chinese, Taiwanese, Mexican), most plausibly arising repeatedly through gene conversion with the adjacent CRYBB2P1 pseudogene. Strikingly, this single genotype produces several distinct lens-opacity morphologies — cerulean (blue-dot), Coppock-like, pulverulent, sutural, perinuclear and total cataract — which is the origin of the "multiple types" designation.

Mechanistically, the pathway runs from a destabilizing mutation in a Greek-key motif or the C-terminal domain of βB2-crystallin, through reduced conformational and thermodynamic stability and impaired crystallin–crystallin interactions, to loss of the short-range-ordered protein packing that the lens requires for transparency, culminating in protein aggregation and light scattering within lens fiber cells. The lens is the only organ affected in humans, though mouse models reveal that βB2-crystallin is also expressed in brain and retina and is linked to schizophrenia-like endophenotypes. Inheritance is high-penetrance autosomal dominant with marked variable expressivity; a rare recessive form exists via a homozygous CRYBB2–CRYBB2P1 fusion deletion.

Diagnosis combines slit-lamp/red-reflex examination with molecular genetic testing (whole-exome sequencing or targeted congenital-cataract gene panels confirmed by Sanger sequencing). The only effective, definitive treatment is **cataract surgery** (lensectomy ± intraocular lens) followed by optical correction and amblyopia management, ideally performed in early infancy to prevent irreversible deprivation amblyopia. Pharmacological "anti-aggregation" therapies (lanosterol, 25-hydroxycholesterol/VP1-001, N-acetylcarnosine) remain experimental and unproven; no gene-specific therapy exists.

---

## 1. Disease Information

**Overview.** CTRCT3 is an inherited (congenital/developmental) cataract — an opacification of the crystalline lens present at birth or developing in early childhood — caused by pathogenic variants in **CRYBB2**. It is typically **bilateral** and is a classic example of a single gene producing multiple cataract morphologies within and across families.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | 601547 (Cataract 3, Multiple Types; CTRCT3) |
| OMIM (gene) | 123620 (CRYBB2) |
| MONDO | MONDO:0011104 |
| Gene (HGNC) | CRYBB2 (HGNC:2398) |
| Cytoband | 22q11.2–q12.1 |
| mRNA reference | NM_000496.2 |
| UniProt | P43320 (CRBB2_HUMAN) |
| Recurrent variant | c.463C>T (p.Gln155*), rs74315489 |
| Orphanet | Rare early-onset non-syndromic cataract group |
| ICD-10 | Q12.0 (Congenital cataract) |
| MeSH | Cataract (D002386) |

**Synonyms / alternative names:** cataract (disease) caused by mutation in CRYBB2; CRYBB2 cataract (disease); CTRCT3; cerulean cataract (CRYBB2-related); Coppock-like cataract (CRYBB2-related).

**Source of information.** The knowledge in this report derives from **aggregated disease-level resources** (OMIM, ClinVar, HGNC) and **primary pedigree/family-based literature** (linkage and exome sequencing of cataract families), plus in-vitro biophysics and animal models — not from EHR/individual-patient registries.

---

## 2. Etiology

**Disease causal factors.** CTRCT3 is a **monogenic (Mendelian) disorder**: heterozygous pathogenic variants in CRYBB2 are sufficient to cause disease in most families. The best-characterized cause is the recurrent chain-termination mutation **p.Gln155\*** (Q155X), first reported in an autosomal dominant cerulean cataract family ([PMID: 9158139](https://pubmed.ncbi.nlm.nih.gov/9158139/): *"a chain-termination mutation in CRYBB2 is associated with ADCC in this family"*) and subsequently in Coppock-like, Chinese, Taiwanese and Mexican pulverulent families. Additional missense variants (e.g., p.Val146Met, p.Arg160Pro, p.Ile109Phe) extend the allelic spectrum.

**Genetic risk factors.** The causal variants themselves are the dominant determinants. The recurrent Q155* allele is believed to arise repeatedly by **gene conversion** with the adjacent CRYBB2P1 pseudogene, explaining its independent recurrence in unrelated populations ([PMID: 19321936](https://pubmed.ncbi.nlm.nih.gov/19321936/): *"Two transitions, NM_000496.2:c.463C>T and NM_000496.2:c.471C>T, in CRYBB2 are identical to the sequence of CRYBB2P"*).

**Environmental risk factors.** For the Mendelian form, environmental exposure is not required. However, environmental stresses — UV irradiation, oxidative stress, heat — can **accelerate** aggregation of already-destabilized crystallins ([PMID: 34896472](https://pubmed.ncbi.nlm.nih.gov/34896472/); [PMID: 41679456](https://pubmed.ncbi.nlm.nih.gov/41679456/)). Age, smoking and UV are established risk factors for age-related cataract generally, relevant to gene-environment interplay but not the primary cause here.

**Protective factors.** No specific protective alleles or dietary/lifestyle protective factors for CRYBB2 cataract have been established. By analogy to age-related cataract, redox buffering (glutathione) and avoidance of UV/oxidative stress are plausibly protective but unproven for this Mendelian entity.

**Gene–environment interactions.** The central interaction: a destabilizing CRYBB2 mutation lowers the threshold at which environmental/oxidative stress triggers crystallin aggregation — a "two-hit" conceptual model in which the genetic lesion sets a reduced stability baseline and environmental stress precipitates or worsens opacity.

---

## 3. Phenotypes

**Core phenotype:** bilateral congenital or early-childhood cataract (lens opacity) of **variable morphology**. The same genotype can present as different opacity patterns, a hallmark of CTRCT3.

| Phenotype | Type | HPO suggestion | Onset | Frequency/notes |
|---|---|---|---|---|
| Congenital cataract (bilateral) | Clinical sign | HP:0000519 (Congenital cataract) | Congenital / early childhood | Core feature, essentially all patients |
| Cerulean (blue-dot) cataract | Clinical sign | HP:0010924 (Cerulean cataract) | Congenital | Classic morphology |
| Coppock-like cataract | Clinical sign | HP:0007971 (Nuclear cataract, related) | Congenital | Distinct entity, same Q155* allele |
| Pulverulent cataract | Clinical sign | HP:0010696 (Pulverulent cataract) | Congenital | Mexican ADPC family |
| Sutural / perinuclear / total cataract | Clinical sign | HP:0100018 (Sutural cataract) | Congenital | Part of "multiple types" |
| Microphthalmia | Physical malformation | HP:0000568 (Microphthalmia) | Congenital | Minority of patients |
| Microcornea | Physical malformation | HP:0000482 (Microcornea) | Congenital | Minority of patients |
| Posterior capsule coloboma | Physical malformation | HP:0000589 (related) | Congenital | Rare |
| Reduced visual acuity | Symptom/sign | HP:0000505 (Visual impairment) | Variable | Often mild until adulthood in cerulean |

**Phenotype characteristics.** Onset is **congenital to early childhood**; severity is **variable** (mild, slowly progressive cerulean opacities through dense total cataract). In cerulean cataract, *"usually visual acuity is only mildly reduced until adulthood, when lens extraction is generally necessary"* ([PMID: 9158139](https://pubmed.ncbi.nlm.nih.gov/9158139/)). A minority show additional ocular anomalies ([PMID: 42919179](https://pubmed.ncbi.nlm.nih.gov/42919179/): *"two patients presented with both microphthalmia and microcornea"*; *"The associated cataract phenotypes included total cataract, cerulean cataract, and perinuclear cataract"*).

**Quality of life.** Untreated bilateral congenital cataract causes deprivation amblyopia and potentially lifelong visual impairment/blindness; with timely surgery and amblyopia therapy, outcomes can be good. Secondary strabismus and nystagmus occur in a substantial minority of congenital cataract patients overall.

---

## 4. Genetic/Molecular Information

**Causal gene.** **CRYBB2** (β-B2-crystallin), HGNC:2398, OMIM 123620, at chromosome **22q11.2–q12.1**. βB2-crystallin is the most abundant β-crystallin in the human lens and forms a **domain-swapped homodimer** built from four Greek-key motifs ([PMID: 17327390](https://pubmed.ncbi.nlm.nih.gov/17327390/)).

**Pathogenic variants (selected):**

| Variant (cDNA) | Protein | Type | Phenotype | Evidence (PMID) |
|---|---|---|---|---|
| c.463C>T (rs74315489) | p.Gln155* (Q155X) | Nonsense | Cerulean / Coppock-like / pulverulent | 9158139, 10634616, 27385965, 29395391 |
| c.436G>A | p.Val146Met | Missense | ADCC (Chinese) | 38869770 |
| c.479G>C | p.Arg160Pro | Missense (de novo) | Complex ocular phenotype (with BEST1) | 37076855 |
| c.325A>T | p.Ile109Phe | Missense (de novo) | Congenital cataract | 42827312 |
| genomic deletion | CRYBB2–CRYBB2P1 fusion | Structural (recessive) | AR congenital cataract | 36075891 |

**Variant classification.** The recurrent Q155* is classified **pathogenic** (strong cosegregation; LOD up to 5.5 in the Mexican ADPC family; absent from controls) ([PMID: 27385965](https://pubmed.ncbi.nlm.nih.gov/27385965/): *"a nonsense mutation c.475C>T (p.Q155*) in exon 6 of the CRYBB2 gene with ADPC"*). Missense variants are typically classified pathogenic/likely pathogenic based on cosegregation, conservation, absence in controls, and structural modeling.

**Allele frequency.** Pathogenic CRYBB2 cataract alleles are extremely rare/absent in gnomAD; each is essentially private to affected families. Q155* is notable for recurrent de novo-like origin via gene conversion, not population frequency.

**Somatic vs germline.** All disease variants are **germline** (some de novo, e.g., p.Ile109Phe, p.Arg160Pro). No somatic/oncogenic involvement.

**Functional consequences.** The dominant mechanism is best described as a **destabilizing / dominant-negative** effect: truncated or destabilized βB2-crystallin disrupts crystallin packing and interactions rather than a simple loss of function. In vitro, the Q155* mutant shows *"decreased ordered structure and stability"* and *"a decrease in protein–protein interactions"* ([PMID: 15889016](https://pubmed.ncbi.nlm.nih.gov/15889016/)).

**Modifier genes / epigenetics / chromosomal abnormalities.** Variable expressivity (same allele → different morphologies) implies modifiers, but no specific modifier gene has been mapped for CTRCT3. No disease-specific epigenetic mechanism is established. No recurrent large rearrangement is characteristic beyond the rare recessive CRYBB2–CRYBB2P1 deletion.

---

## 5. Environmental Information

CTRCT3 is fundamentally **genetic**; environmental factors are secondary. **Environmental/oxidative stress** (UV radiation, heat, oxidative stress) can accelerate aggregation of destabilized β-crystallins in experimental systems ([PMID: 34896472](https://pubmed.ncbi.nlm.nih.gov/34896472/): *"the L116P mutation increased susceptibility of βB1-crystallin against UV radiation"*). **Lifestyle factors** (smoking, UV exposure) are established contributors to age-related cataract but have no established causal role in CRYBB2-driven congenital cataract. **Infectious agents** are not applicable to this Mendelian disease (in contrast to congenital rubella cataract, a separate entity).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (mutation → opacity)

1. A **CRYBB2 pathogenic variant** (e.g., Q155* truncation, or missense V146M/R160P/I109F) disrupts a **Greek-key motif or the C-terminal domain** of βB2-crystallin. *(Demonstrated structurally/biophysically.)*
2. **Leads to** reduced conformational and thermodynamic stability and increased hydrophobic exposure. *(Demonstrated — [PMID: 15889016](https://pubmed.ncbi.nlm.nih.gov/15889016/).)*
3. **Results in** impaired crystallin–crystallin interactions and loss of the short-range-ordered packing required for lens transparency, with decreased solubility. *(Demonstrated for Q155*; inferred for the in-vivo lens milieu.)*
4. **Results in** misfolding and protein aggregation. *(Inferred by direct analogy to homologous βB1 mutants Q70P/S93R/L116P and γD S78 mutants, which show decreased solubility, aggresome/amyloid formation and reduced cell viability — [PMID: 37148932](https://pubmed.ncbi.nlm.nih.gov/37148932/), [PMID: 35359596](https://pubmed.ncbi.nlm.nih.gov/35359596/), [PMID: 34896472](https://pubmed.ncbi.nlm.nih.gov/34896472/), [PMID: 37739288](https://pubmed.ncbi.nlm.nih.gov/37739288/).)*
5. **Light scattering** by aggregates in **lens fiber cells** → **lens opacity (cataract)** → **visual impairment**. *(Demonstrated clinically.)*

**Branches:**
- **Environmental branch:** UV/oxidative/heat stress accelerates aggregation (step 4 reached sooner).
- **Developmental branch:** A CRYBB2 splice variant in zebrafish causes **lens fiber cell differentiation defects**, ECM (collagen IV/laminin) remodeling and hyaloid vascular abnormalities ([PMID: 41989229](https://pubmed.ncbi.nlm.nih.gov/41989229/): *"crybb2 disruption caused lens fiber cell differentiation defects and was accompanied by abnormal hyaloid vascular patterning"*).

```
CRYBB2 mutation (Q155*/missense)
        │  disrupts Greek-key / C-terminal domain
        ▼
Reduced thermodynamic stability + hydrophobic exposure
        │
        ├─────────────► Impaired crystallin–crystallin interactions
        │                        │  loss of short-range order, ↓ solubility
        │                        ▼
   [UV/oxidative/heat] ──► Misfolding & aggregation ──► Light scattering in fiber cells ──► CATARACT
        │                                                        ▲
        └── Developmental branch:                                │
            fiber differentiation defect + ECM/vascular ─────────┘
```

**Molecular pathways / cellular processes.** Core process = proteostasis failure of structural crystallins. GO suggestions: **GO:0002088** (lens development in camera-type eye), **GO:0043010** (camera-type eye development), **GO:0007601** (visual perception), **GO:0006457** (protein folding), **GO:0050896** (response to stimulus/oxidative stress). Cellular compartment: **GO:0005737** (cytoplasm) — crystallins are densely packed cytoplasmic proteins.

**Protein dysfunction.** Misfolding, destabilization, impaired domain-swapped dimer formation, aggregation (UniProt P43320). Interface deamidation likewise destabilizes the dimer ([PMID: 16519509](https://pubmed.ncbi.nlm.nih.gov/16519509/): *"deamidation at critical sites destabilizes betaB2 and may disrupt the function of betaB2 in the lens"*).

**Immune/metabolic involvement.** Not central. Age-related cataract literature implicates oxidative stress, glutathione decline and ferroptosis in lens epithelial cells ([PMID: 41679456](https://pubmed.ncbi.nlm.nih.gov/41679456/)), relevant to the stress-acceleration branch but not the primary Mendelian mechanism.

**Cell types (CL):** lens fiber cell (**CL:0000199**), lens epithelial cell (**CL:0002224**).

---

## 7. Anatomical Structures Affected

- **Primary organ:** the **ocular lens** (crystalline lens) — **UBERON:0000965** (lens of camera-type eye), within the eye (UBERON:0000970).
- **Secondary involvement:** retina/visual pathway secondarily via deprivation amblyopia; associated anterior-segment anomalies (microcornea — cornea UBERON:0000964; microphthalmia — whole eye). Secondary surgical complication: glaucoma.
- **Body system:** visual/sensory system only (non-syndromic in humans).
- **Tissue/cell level:** lens fiber cells (CL:0000199) and lens epithelial cells (CL:0002224); opacity concentrates in nucleus/cortex by morphology.
- **Subcellular level:** cytoplasm of fiber cells (GO:0005737), where crystallins are packed; aggregates form in the cytosol.
- **Localization & lateralization:** **bilateral** in the great majority (HP:0000519), with possible asymmetry between eyes.

---

## 8. Temporal Development

- **Onset:** congenital or early childhood; opacities frequently present at birth. Pattern typically **chronic/insidious** for cerulean types, **congenital/overt** for total cataract.
- **Progression:** variable. Cerulean opacities progress slowly, with vision *"only mildly reduced until adulthood"* ([PMID: 9158139](https://pubmed.ncbi.nlm.nih.gov/9158139/)); dense/total cataract requires early intervention.
- **Course / duration:** chronic and lifelong unless the lens is removed. Opacity does not spontaneously remit; "remission" is surgically induced by lensectomy.
- **Critical periods:** the **first weeks–months of life** are critical — delayed surgery allows irreversible deprivation amblyopia. Recommended timing: within ~6 weeks for unilateral and by ~4 months (6–10 weeks) for bilateral cataract ([PMID: 31317088](https://pubmed.ncbi.nlm.nih.gov/31317088/); [PMID: 40193670](https://pubmed.ncbi.nlm.nih.gov/40193670/)).

---

## 9. Inheritance and Population

**Inheritance.** Predominantly **autosomal dominant** with **high/near-complete penetrance** and **variable expressivity**. The Coppock-like family was *"autosomal dominant and appeared to be fully penetrant"* ([PMID: 10634616](https://pubmed.ncbi.nlm.nih.gov/10634616/)); the Mexican ADPC family showed cosegregation with LOD 5.5 ([PMID: 27385965](https://pubmed.ncbi.nlm.nih.gov/27385965/)). A rare **autosomal recessive** form is caused by a homozygous CRYBB2–CRYBB2P1 fusion deletion ([PMID: 36075891](https://pubmed.ncbi.nlm.nih.gov/36075891/): *"is responsible for autosomal recessive congenital cataracts"*).

**Expressivity / phenotypic heterogeneity.** The same Q155* allele produces cerulean, Coppock-like and pulverulent cataract — *"The CCL and the cerulean cataract are two distinct clinical entities associated with the same genetic defect"* ([PMID: 10634616](https://pubmed.ncbi.nlm.nih.gov/10634616/)).

**Epidemiology.** CTRCT3 is a rare Mendelian subset of congenital cataract. Congenital cataract overall affects **~0.63–9.74 per 10,000 births** (highest in Asia; ~7.4 per 10,000 children) ([PMID: 38869770](https://pubmed.ncbi.nlm.nih.gov/38869770/)), is **bilateral in ~56%** of cases ([PMID: 28652574](https://pubmed.ncbi.nlm.nih.gov/28652574/)), and **~25–50%** are genetic, with crystallin genes (including CRYBB2) the most common cause. 38 genes are associated with isolated cataract ([PMID: 32217542](https://pubmed.ncbi.nlm.nih.gov/32217542/): *"38 disease-causing genes have been identified to date to be associated with isolated cataract"*).

**Founder effects / recurrence.** No classic founder effect; instead Q155* **recurs** across populations, plausibly via gene conversion with CRYBB2P1 ([PMID: 19321936](https://pubmed.ncbi.nlm.nih.gov/19321936/)).

**Consanguinity.** Contributes to the rare recessive deletion form; not relevant to the dominant form.

**Sex ratio / demographics.** No established sex bias for the Mendelian form. Reported families span American, Swiss, Chinese, Taiwanese, Mexican, Pakistani and other ancestries — broad geographic distribution.

---

## 10. Diagnostics

**Clinical tests.** Diagnosis rests on **slit-lamp biomicroscopy** and **red-reflex testing** documenting bilateral lens opacity, with **B-scan ultrasound** where media opacity limits fundus view. Opacity morphology is documented by slit-lamp photography.

**Genetic testing.** **Whole-exome sequencing (WES)** and **targeted congenital-cataract gene panels** (e.g., 153-gene panels covering crystallins, connexins, MIP, PAX6) confirmed by **Sanger sequencing** are standard. Diagnostic yields in pediatric cataract cohorts range **~45–82%**:

| Study | Population | Yield | PMID |
|---|---|---|---|
| Myanmar paediatric cataract (WES) | 20 probands | 45% (9/20); genes incl. CRYBB2 | [40229141](https://pubmed.ncbi.nlm.nih.gov/40229141/) |
| Israeli/Palestinian bilateral pediatric cataract | 22 families | 81.8% (18/22) | [38874774](https://pubmed.ncbi.nlm.nih.gov/38874774/) |
| Panel-based exome (153-gene panel) | congenital cataract | panel described | [34840822](https://pubmed.ncbi.nlm.nih.gov/34840822/) |

([PMID: 40229141](https://pubmed.ncbi.nlm.nih.gov/40229141/): *"Pathogenic or likely pathogenic variants were identified in 45% (9/20) of probands in genes MIP, COL2A1, NHS, GJA8, GJA3, CRYGC, CRYBB2, PAX6 and SLC7A8."*)

**Differential diagnosis.** Other crystallin cataracts (CRYAA, CRYGC/D, CRYBA1, CRYBB1), connexin cataracts (GJA3/Cx46, GJA8/Cx50), MIP/AQP0, beaded-filament (BFSP1/2), and transcription-factor cataracts (PAX6, MAF, PITX3), plus syndromic causes. Complex phenotypes can require **digenic/combined interpretation** (e.g., BEST1 + CRYBB2 producing microphthalmia/microcornea/cataract/vitelliform dystrophy — [PMID: 37076855](https://pubmed.ncbi.nlm.nih.gov/37076855/)).

**Screening.** Newborn red-reflex screening detects congenital cataract; **cascade genetic testing** of at-risk relatives is appropriate once a familial variant is identified. No omics-based or liquid-biopsy diagnostic is used.

---

## 11. Outcome / Prognosis

**Survival/mortality.** CTRCT3 is **not life-threatening**; life expectancy is normal; no disease-specific mortality.

**Morbidity/function.** The principal morbidity is **visual** — untreated bilateral congenital cataract causes deprivation amblyopia and potential lifelong blindness, a major cause of childhood visual impairment worldwide. With timely surgery and diligent amblyopia therapy, outcomes are often good, but results are threatened by late presentation and poor adherence to post-operative refractive/amblyopia care ([PMID: 37931121](https://pubmed.ncbi.nlm.nih.gov/37931121/)).

**Complications.** Post-surgical complications include **visual axis opacification (posterior capsule opacification)**, **aphakic/pseudophakic glaucoma** (more common with microphthalmia and very early surgery), nystagmus and strabismus, and refractive error from axial growth/myopic shift.

**Prognostic factors.** Earlier surgery within the critical window, symmetric bilateral management, absence of microphthalmia, and strong adherence to amblyopia therapy predict better visual outcomes.

---

## 12. Treatment

**Definitive treatment is surgical.** There is **no approved pharmacologic or gene-specific therapy** for CRYBB2 cataract. Management is **lensectomy** with **primary posterior capsulotomy ± anterior vitrectomy**, followed by optical correction (intraocular lens, contact lenses, or aphakic glasses) and **amblyopia therapy**. NCIT: *Cataract Surgery*, *Lensectomy*, *Intraocular Lens Implantation*.

**Surgical timing.** *"Cataract surgery is recommended at 6 weeks of age for unilateral cataract and between 6 and 8 weeks of age for bilateral cases"* ([PMID: 31317088](https://pubmed.ncbi.nlm.nih.gov/31317088/)); bilateral cases by ~4 months ([PMID: 40193670](https://pubmed.ncbi.nlm.nih.gov/40193670/)). IOL power selection is complicated by ongoing axial growth and myopic shift.

**IOL vs aphakia.** A Cochrane review of RCTs found no high-level evidence favoring one surgical approach over another; in children under 2 there may be little or no difference in visual acuity between pseudophakia and aphakia (very low-certainty evidence) ([PMID: 36107778](https://pubmed.ncbi.nlm.nih.gov/36107778/)).

**Experimental pharmacotherapy.** Anti-aggregation small molecules — **lanosterol**, **25-hydroxycholesterol (VP1-001)**, **N-acetylcarnosine**, **N-acetylcysteine amide** — show promise in some cataract models ([PMID: 36484206](https://pubmed.ncbi.nlm.nih.gov/36484206/)) but remain unproven; at least one rigorous study reported **failure of lanosterol/oxysterols to restore lens clarity** ([PMID: 31186457](https://pubmed.ncbi.nlm.nih.gov/31186457/): *"lanosterol liposomes failed to either reverse these lens opacities or prevent the further progression of cataracts"*). No gene therapy, RNA therapy, or immunotherapy exists for this indication.

**Pharmacogenomics / personalized medicine.** Not applicable beyond genotype-informed counseling.

---

## 13. Prevention

- **Primary prevention:** not possible for a germline Mendelian disorder; genetic counseling and reproductive options (preimplantation genetic testing, prenatal diagnosis) can prevent transmission.
- **Secondary prevention:** **universal newborn red-reflex screening** enables early detection and timely surgery — the single most important factor preventing irreversible amblyopia.
- **Tertiary prevention:** meticulous post-operative care (amblyopia therapy, refractive correction, glaucoma surveillance) prevents complications and visual loss.
- **Genetic counseling:** autosomal dominant inheritance implies ~50% transmission risk from an affected parent; variable expressivity means affected offspring may show different morphology/severity. Cascade testing of relatives is recommended once the family variant is known.
- **Immunization / public health / environmental interventions:** not applicable (non-infectious, non-environmental cause).

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** CRYBB2 is highly conserved; the Q155 residue is **100% conserved across 56 orthologs spanning fish to primates** ([PMID: 29395391](https://pubmed.ncbi.nlm.nih.gov/29395391/)). Mouse ortholog **Crybb2** (MGI); zebrafish *crybb2*.
- **Natural/veterinary disease:** The **Philly mouse** carries an in-frame 12-nt (4-amino-acid) C-terminal deletion in βB2-crystallin causing inherited cataract — a long-standing natural/mutant model ([PMID: 1707874](https://pubmed.ncbi.nlm.nih.gov/1707874/): *"The Philly mouse, a strain with an inherited cataract, has an abnormal beta B2-crystallin, the principal beta-crystallin in the mouse"*; *"This abnormal beta B2-crystallin may be the cause of the cataract in this animal"*).
- **Comparative biology:** The aggregation/destabilization mechanism is evolutionarily conserved across β/γ-crystallins and across species, making rodent and zebrafish systems valid models.
- **Zoonotic potential:** none (non-infectious genetic disease).

---

## 15. Model Organisms

| Model | Type | Allele | Phenotype recapitulation | PMID |
|---|---|---|---|---|
| Philly mouse | Mammalian (spontaneous) | In-frame 12-nt / 4-aa C-terminal Crybb2 deletion | Inherited cataract via destabilized βB2 | [1707874](https://pubmed.ncbi.nlm.nih.gov/1707874/) |
| ENU C-terminal Crybb2 missense series | Mammalian (induced) | C-terminal missense alleles | Cataract + brain/behavioral (schizophrenia) endophenotypes | [30291584](https://pubmed.ncbi.nlm.nih.gov/30291584/) |
| Zebrafish *crybb2* splice/disruption | Vertebrate (induced) | Splice variant / crybb2 disruption | Lens fiber differentiation defects, ECM remodeling, hyaloid vascular anomalies | [41989229](https://pubmed.ncbi.nlm.nih.gov/41989229/) |
| Recombinant Q155* βB2 (in vitro) | Biophysical/in vitro | p.Gln155* | Decreased stability, reduced protein–protein interactions | [15889016](https://pubmed.ncbi.nlm.nih.gov/15889016/) |

**Non-lens biology.** βB2-crystallin is expressed in adult mouse brain and retina; a comprehensive study found *"Crybb2 Mutations Consistently Affect Schizophrenia Endophenotypes in Mice"* and that *"CRYBB2 also is expressed in non-lens tissue such as the adult mouse brain and is associated with neuropsychiatric disorders such as schizophrenia"* ([PMID: 30291584](https://pubmed.ncbi.nlm.nih.gov/30291584/)). βB2-crystallin has also been implicated in retinal ganglion cell axon growth/regeneration. These are not features of the human Mendelian CTRCT3 phenotype but are important biology.

**Model limitations.** Mouse βB2 is the principal β-crystallin (as in humans), so lens phenotypes translate well; however, species differences in lens optics and the murine neuropsychiatric associations do not map onto human non-syndromic cataract. In-vitro recombinant studies capture destabilization but not the in-vivo developmental/ECM branch seen in zebrafish.

---

## Key Findings (Consolidated)

### F001 — CRYBB2 is the cause; Q155* is a recurrent hotspot
CTRCT3 (OMIM 601547; MONDO:0011104) maps to 22q11.2–q12.1 and is caused by **CRYBB2** (β-B2-crystallin). The recurrent c.463C>T (p.Gln155*/Q155X; rs74315489) in exon 6 appears in ethnically distinct families with LOD scores up to 5.5, producing cerulean, Coppock-like, pulverulent, sutural and total cataract — hence "multiple types." The allele likely arises by gene conversion with CRYBB2P1. **Evidence:** [PMID: 9158139](https://pubmed.ncbi.nlm.nih.gov/9158139/), [PMID: 10634616](https://pubmed.ncbi.nlm.nih.gov/10634616/), [PMID: 27385965](https://pubmed.ncbi.nlm.nih.gov/27385965/), [PMID: 19321936](https://pubmed.ncbi.nlm.nih.gov/19321936/).

### F002 — Mechanism: destabilization impairs crystallin interactions
In vitro, recombinant Q155* βB2-crystallin shows **decreased protein–protein interactions, decreased ordered secondary structure, and reduced thermodynamic stability**, retaining some dimer structure. βB2 forms a domain-swapped Greek-key homodimer; destabilizing substitutions/deamidations at the interface destabilize the dimer. **Evidence:** [PMID: 15889016](https://pubmed.ncbi.nlm.nih.gov/15889016/), [PMID: 17327390](https://pubmed.ncbi.nlm.nih.gov/17327390/), [PMID: 16519509](https://pubmed.ncbi.nlm.nih.gov/16519509/), [PMID: 1707874](https://pubmed.ncbi.nlm.nih.gov/1707874/).

### F003 — Phenotype & treatment
Bilateral congenital/early-childhood cataract of variable morphology, sometimes with microphthalmia/microcornea; cerulean cataract often only mildly reduces acuity until adulthood. Management is surgical, timed to prevent amblyopia. **Evidence:** [PMID: 42919179](https://pubmed.ncbi.nlm.nih.gov/42919179/), [PMID: 9158139](https://pubmed.ncbi.nlm.nih.gov/9158139/), [PMID: 31317088](https://pubmed.ncbi.nlm.nih.gov/31317088/), [PMID: 40193670](https://pubmed.ncbi.nlm.nih.gov/40193670/).

### F004 — Mouse models and non-lens role
Multiple Crybb2 alleles (Philly mouse; ENU missense series) model the disease; βB2 is expressed in brain/retina and linked to schizophrenia endophenotypes in mice. **Evidence:** [PMID: 30291584](https://pubmed.ncbi.nlm.nih.gov/30291584/), [PMID: 1707874](https://pubmed.ncbi.nlm.nih.gov/1707874/).

### F005 — Inheritance and epidemiology
Predominantly autosomal dominant, high/near-complete penetrance, variable expressivity; rare recessive CRYBB2–CRYBB2P1 deletion form. CTRCT3 is a rare Mendelian subset of congenital cataract (overall ~0.63–9.74/10,000 births; ~56% bilateral; ~25–50% genetic). **Evidence:** [PMID: 10634616](https://pubmed.ncbi.nlm.nih.gov/10634616/), [PMID: 36075891](https://pubmed.ncbi.nlm.nih.gov/36075891/), [PMID: 38869770](https://pubmed.ncbi.nlm.nih.gov/38869770/), [PMID: 28652574](https://pubmed.ncbi.nlm.nih.gov/28652574/), [PMID: 32217542](https://pubmed.ncbi.nlm.nih.gov/32217542/).

### F006 — Diagnostics and emerging therapy
Slit-lamp exam + WES/gene-panel genetic testing (yields ~45–82%); surgery definitive; pharmacologic anti-aggregation therapy experimental and unproven. **Evidence:** [PMID: 40229141](https://pubmed.ncbi.nlm.nih.gov/40229141/), [PMID: 34840822](https://pubmed.ncbi.nlm.nih.gov/34840822/), [PMID: 31186457](https://pubmed.ncbi.nlm.nih.gov/31186457/).

### F007 — Consolidated causal chain + gene-environment interaction
Destabilized βB2-crystallin (aggregation accelerated by UV/oxidative/heat stress) scatters light in lens fiber cells; a developmental branch (fiber differentiation/ECM/vascular changes) is supported in zebrafish. **Evidence:** [PMID: 34896472](https://pubmed.ncbi.nlm.nih.gov/34896472/), [PMID: 37148932](https://pubmed.ncbi.nlm.nih.gov/37148932/), [PMID: 41989229](https://pubmed.ncbi.nlm.nih.gov/41989229/).

---

## Mechanistic Model / Interpretation

The unifying model is **proteostatic failure of a structural lens protein**. βB2-crystallin's job is purely structural: at enormous concentration in long-lived, non-dividing fiber cells, it must remain soluble and participate in ordered short-range packing to keep the lens transparent. CTRCT3 mutations are not enzymatic "loss of catalysis" lesions; they are **stability lesions**. Whether the mutation truncates the C-terminus (Q155*) or substitutes a core Greek-key residue (missense), the common downstream consequence is lowered thermodynamic stability, exposure of hydrophobic surface, impaired dimer/higher-order interactions, decreased solubility, and ultimately aggregation. Because the aggregates scatter light, the macroscopic result is opacity. The **dominant** inheritance fits a dominant-negative/aggregation-seeding mechanism in which mutant protein corrupts the packing of its wild-type partners.

Two features make CTRCT3 instructive. First, **one genotype, many phenotypes** (cerulean vs Coppock-like vs pulverulent from the same Q155* allele) implies stochastic and modifier-dependent control over *where* and *when* aggregation nucleates during lens development — not a simple dose-response. Second, **environmental stress lowers the aggregation threshold**, tying this Mendelian disease conceptually to age-related cataract, where the same crystallins aggregate after a lifetime of oxidative/UV insult.

---

## Evidence Base

| PMID | Role | How it supports/challenges findings |
|---|---|---|
| [9158139](https://pubmed.ncbi.nlm.nih.gov/9158139/) | Landmark | First links a CRYBB2 chain-termination mutation to ADCC; natural history |
| [10634616](https://pubmed.ncbi.nlm.nih.gov/10634616/) | Key | Same Q155* → distinct Coppock-like vs cerulean; full penetrance, AD |
| [27385965](https://pubmed.ncbi.nlm.nih.gov/27385965/) | Key | Q155* in Mexican ADPC family, LOD 5.5 |
| [19321936](https://pubmed.ncbi.nlm.nih.gov/19321936/) | Mechanistic | Gene-conversion origin from CRYBB2P1 pseudogene |
| [15889016](https://pubmed.ncbi.nlm.nih.gov/15889016/) | Biophysics | Q155* destabilizes βB2, reduces protein interactions |
| [17327390](https://pubmed.ncbi.nlm.nih.gov/17327390/) | Structure | Domain-swapped Greek-key βB2 dimer |
| [16519509](https://pubmed.ncbi.nlm.nih.gov/16519509/) | Biophysics | Interface deamidation destabilizes dimer |
| [1707874](https://pubmed.ncbi.nlm.nih.gov/1707874/) | Model | Philly mouse — natural Crybb2 cataract model |
| [30291584](https://pubmed.ncbi.nlm.nih.gov/30291584/) | Model | Non-lens brain expression; schizophrenia endophenotypes |
| [41989229](https://pubmed.ncbi.nlm.nih.gov/41989229/) | Model | Zebrafish developmental/ECM/vascular branch |
| [42919179](https://pubmed.ncbi.nlm.nih.gov/42919179/) | Clinical | Phenotype spectrum incl. microphthalmia/microcornea |
| [31317088](https://pubmed.ncbi.nlm.nih.gov/31317088/), [40193670](https://pubmed.ncbi.nlm.nih.gov/40193670/) | Clinical | Surgical timing to prevent amblyopia |
| [36075891](https://pubmed.ncbi.nlm.nih.gov/36075891/) | Clinical | Rare recessive CRYBB2–CRYBB2P1 deletion form |
| [38869770](https://pubmed.ncbi.nlm.nih.gov/38869770/), [28652574](https://pubmed.ncbi.nlm.nih.gov/28652574/), [32217542](https://pubmed.ncbi.nlm.nih.gov/32217542/) | Epidemiology | Congenital cataract burden, genetic fraction, gene count |
| [40229141](https://pubmed.ncbi.nlm.nih.gov/40229141/), [34840822](https://pubmed.ncbi.nlm.nih.gov/34840822/), [38874774](https://pubmed.ncbi.nlm.nih.gov/38874774/) | Diagnostics | WES/panel yields incl. CRYBB2 |
| [31186457](https://pubmed.ncbi.nlm.nih.gov/31186457/), [36484206](https://pubmed.ncbi.nlm.nih.gov/36484206/) | Therapy | Experimental anti-aggregation drugs; lanosterol failure |
| [34896472](https://pubmed.ncbi.nlm.nih.gov/34896472/), [37148932](https://pubmed.ncbi.nlm.nih.gov/37148932/), [35359596](https://pubmed.ncbi.nlm.nih.gov/35359596/), [37739288](https://pubmed.ncbi.nlm.nih.gov/37739288/) | Mechanistic analogy | βB1/γD mutants: Greek-key disruption, aggregation, UV susceptibility |
| [41679456](https://pubmed.ncbi.nlm.nih.gov/41679456/) | Context | Lens aging, oxidative stress, gene-environment interaction |

---

## Limitations and Knowledge Gaps

1. **Direct in-vivo aggregation data for human CRYBB2 mutants are limited.** Much of the aggregation mechanism (step 4) is **inferred by analogy** to homologous βB1/γD mutants rather than demonstrated directly for CRYBB2 in human lens.
2. **No molecular explanation for variable expressivity.** Why the same Q155* allele yields cerulean vs Coppock-like vs pulverulent cataract is unknown; specific modifier genes have not been mapped.
3. **Epidemiology is indirect.** No CTRCT3-specific prevalence/incidence figures exist; numbers are for congenital cataract as a whole. Penetrance/expressivity estimates come from small pedigrees.
4. **No disease-specific natural history study** quantifies progression rate by morphology.
5. **Therapeutics gap.** No approved pharmacologic or gene-specific therapy; anti-aggregation drug data are conflicting (lanosterol failure vs promising oxysterol reports).
6. **Human relevance of murine neuropsychiatric findings is unresolved** — CRYBB2 schizophrenia endophenotypes are murine and not part of the human non-syndromic phenotype.

---

## Proposed Follow-up Experiments / Actions

1. **Direct biophysical/cellular characterization of common CRYBB2 missense alleles** (V146M, I109F, R160P) in human lens epithelial cells and recombinant systems: solubility, aggregation kinetics, aggresome formation, and chaperone (α-crystallin) rescue — to confirm step 4 for CRYBB2 specifically.
2. **Modifier mapping / genotype–phenotype study** across large multi-family CRYBB2 cohorts to explain variable morphology (candidate modifiers: α-crystallin chaperone capacity, redox genes).
3. **Patient-derived iPSC → lens organoid models** carrying Q155* and missense alleles to study the developmental (fiber differentiation/ECM) branch identified in zebrafish and to serve as an anti-aggregation drug-screening platform.
4. **Controlled test of anti-aggregation compounds** (25-hydroxycholesterol/VP1-001, N-acetylcarnosine) on CRYBB2-mutant lens organoids to resolve the lanosterol controversy for this gene.
5. **Registry development** to capture CTRCT3-specific prevalence, penetrance, progression, and visual outcomes.
6. **gnomAD/ClinVar reanalysis** of the CRYBB2–CRYBB2P1 locus to quantify gene-conversion recurrence rate and refine counseling on recurrence risk.

---

*Report compiled from 7 confirmed findings and 50 reviewed papers over 5 investigation iterations. Evidence types span human clinical/pedigree studies, in-vitro biophysics, and model organisms (mouse, zebrafish). All mechanistic steps are flagged as demonstrated or inferred in Section 6.*


## Artifacts

- [OpenScientist final report](Cataract_3_Multiple_Types-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Cataract_3_Multiple_Types-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 31 |
| On topic | 21 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 22 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 12 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0011104` (4 mentions) - the report calls it "MONDO"; MONDO calls it **cataract 3 multiple types**
- `HP:0000519` (2 mentions) - the report calls it "Congenital cataract", "Localization & lateralization:** **bilateral** in the great majority"; HP calls it **Developmental cataract**
- `HP:0000589` (1 mention) - the report calls it "related"; HP calls it **Coloboma**
- `GO:0005737` (2 mentions) - the report calls it "Subcellular level:** cytoplasm of fiber cells"; GO calls it **cytoplasm**
- `CL:0000199` (2 mentions) - the report calls it "Tissue/cell level:** lens fiber cells"; CL calls it **mechanoreceptor cell**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0010924` (1 mention) - the report calls it "Cerulean cataract"; HP calls it **Posterior cortical cataract**
- `HP:0007971` (1 mention) - the report calls it "Nuclear cataract, related"; HP calls it **Lamellar cataract**
- `HP:0010696` (1 mention) - the report calls it "Pulverulent cataract"; HP calls it **Polar cataract**
- `HP:0100018` (1 mention) - the report calls it "Sutural cataract"; HP calls it **Nuclear cataract**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000519` - called "Congenital cataract", "Localization & lateralization:** **bilateral** in the great majority"