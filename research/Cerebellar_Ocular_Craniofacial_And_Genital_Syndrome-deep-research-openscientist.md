---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-05T00:58:31.140195'
end_time: '2026-11-05T01:13:19.785350'
duration_seconds: 888.65
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Cerebellar, Ocular, Craniofacial, and Genital Syndrome
  mondo_id: MONDO:0032774
  category: Mendelian
  causal_genes: MAB21L1
  omim_id: OMIM:618479
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
citation_count: 11
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 10
  quotes_valid: 10
  relevance_assessed: 11
  on_topic: 7
  validator_version: 0.5.1
term_validation:
  total_terms: 28
  verified: 26
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 5
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: HP:0001321
    reported_labels:
    - Clinical sign (imaging)
    ontology_label: Cerebellar hypoplasia
  - term_id: HP:0001251
    reported_labels:
    - Clinical sign
    ontology_label: Ataxia
  - term_id: HP:0001249
    reported_labels:
    - Behavioral/cognitive
    ontology_label: Intellectual disability
  - term_id: HP:0000568
    reported_labels:
    - Physical manifestation
    ontology_label: Microphthalmia
  - term_id: HP:0001131
    reported_labels:
    - Clinical sign
    ontology_label: Corneal dystrophy
  - term_id: HP:0001999
    reported_labels:
    - Physical manifestation
    ontology_label: Abnormal facial shape
  - term_id: HP:0000252
    reported_labels:
    - Physical manifestation
    ontology_label: Microcephaly
  - term_id: HP:0100783
    reported_labels:
    - abnormal nipple
    ontology_label: Breast aplasia
  - term_id: UBERON:0000970
    reported_labels:
    - Primary organs:** Eye
    ontology_label: eye
  labels_variant: 2
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
  path: Cerebellar_Ocular_Craniofacial_And_Genital_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Cerebellar_Ocular_Craniofacial_And_Genital_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cerebellar, Ocular, Craniofacial, and Genital Syndrome
- **MONDO ID:** MONDO:0032774 (if available)
- **Causal gene(s):** MAB21L1
- **OMIM:** OMIM:618479
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Cerebellar, Ocular, Craniofacial, and Genital Syndrome** covering all of the
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

# Cerebellar, Ocular, Craniofacial, and Genital (COFG) Syndrome — Comprehensive Disease Report

**Disease:** Cerebellar, Ocular, Craniofacial, and Genital Syndrome (COFG; also "Cerebello-Oculo-Facio-Genital syndrome")
**MONDO ID:** MONDO:0032774 · **OMIM:** 618479
**Causal gene:** **MAB21L1** (mab-21 like 1; HGNC:6757; NCBI Gene 4081; Ensembl ENSG00000180660; UniProt Q13394; locus 13q13.3)
**Category:** Mendelian, autosomal recessive

---

## Summary

Cerebellar, Ocular, Craniofacial, and Genital (COFG) syndrome is an **ultra-rare autosomal-recessive congenital malformation syndrome caused by biallelic loss-of-function variants in the gene MAB21L1** (male abnormal 21-like 1). MAB21L1 encodes a putative, but catalytically unproven, nucleotidyltransferase that belongs to the evolutionarily conserved cGAS/MAB21 (CD-NTase) structural family and functions as a developmental cell-fate determinant. The disorder was defined by Rad et al. (2019) in 10 affected individuals from 5 consanguineous families and is clinically recognisable by a constellation of features giving the syndrome its name: cerebellar hypoplasia with ataxia, ocular anomalies (corneal dystrophy, microphthalmia), a distinctive craniofacial gestalt with variable microcephaly, and genital malformation (underdeveloped labioscrotal folds / scrotal agenesis), together with hairy nipples and intellectual disability.

A central genetic insight of this entry is the **allelic series** at the MAB21L1 locus. **Biallelic (homozygous/compound heterozygous) loss-of-function** variants produce the full multisystem recessive COFG syndrome. In sharp contrast, **monoallelic (heterozygous) missense variants clustered at the Arg51 codon** cause a distinct **autosomal-dominant, eye-restricted disorder** — microphthalmia/aniridia, also termed BAMD (blepharophimosis with anterior segment and macular dysgenesis) — without the cerebellar, craniofacial, or genital features of COFG. These are two different diseases that happen to share a gene, and it is essential not to conflate them.

Mechanistically, MAB21L1 adopts the cGAS nucleotidyltransferase fold but in an apparently inactive conformation, and purified protein has not shown nucleotidyltransferase catalysis. Instead, functional data point to a **non-catalytic role in transcriptional regulation of developmental programs**: in the mouse lens placode, loss of Mab21l1 downregulates lens-fate genes (Pitx3, Maf, Sfrp2), perturbs DNA/nucleotide-metabolism gene expression, and triggers endoplasmic reticulum (ER) stress followed by cell death. A Mab21l1-null mouse recapitulates core human features — microphthalmia, fontanelle/craniofacial dysosteogenesis, and genital (preputial gland) hypoplasia — establishing a faithful model organism. The disease is congenital and static (non-degenerative). There is no disease-modifying or targeted therapy; management is supportive and multidisciplinary, with genetic counseling and prenatal/preimplantation testing offered for prevention given the ~25% sibling recurrence risk.

---

## Key Findings

### Finding 1 — Biallelic MAB21L1 loss of function causes autosomal-recessive COFG syndrome

COFG syndrome is caused by **biallelic (homozygous or compound heterozygous) loss-of-function variants in MAB21L1**. The defining study, Rad et al. (2019, *J Med Genet*), identified homozygous MAB21L1 variants in affected individuals from consanguineous families and named the "Cerebello-Oculo-Facio-Genital" (COFG) syndrome, mapping it to MONDO:0032774 / OMIM 618479. MAB21L1 is a putative nucleotidyltransferase of the MAB21/cGAS family. The paper states that MAB21L1 "*is a member of an evolutionarily well-conserved family of the male abnormal 21 (MAB21)-like proteins*" and that the report "*defines an ultrarare but clinically recognisable Cerebello-Oculo-Facio-Genital syndrome associated with recessive*" variants ([PMID: 30487245](https://pubmed.ncbi.nlm.nih.gov/30487245/)).

This establishes the core gene–disease relationship: the disease is Mendelian, recessive, and arises from loss of MAB21L1 function. Evidence source: human clinical genetics (consanguineous family cohort).

### Finding 2 — Allelic series: biallelic LoF → multisystem COFG; monoallelic Arg51 missense → dominant isolated ocular disease

The MAB21L1 locus produces **two genetically and clinically distinct disorders**. Biallelic loss of function gives the multisystem recessive COFG syndrome. By contrast, **heterozygous missense variants clustered at the Arg51 codon** (c.152G>T p.Arg51Leu, c.152G>A, c.155T>G) cause an **autosomal-dominant, eye-only disorder** — severe aniridia and/or microphthalmia (BAMD: blepharophimosis + anterior segment and macular dysgenesis) — *without* the cerebellar or genital features of COFG. Several of these variants are de novo and absent from gnomAD.

Wang et al. (2023, describing the dominant BAMD syndrome) summarize the distinction: "*Biallelic MAB21L1 variants have been reported to cause autosomal recessive cerebellar, ocular, craniofacial, and genital syndrome (COFG), whereas only five heterozygous pathogenic variants have been suspected to cause autosomal dominant (AD) microphthalmia and aniridia in eight families*" ([PMID: 36892533](https://pubmed.ncbi.nlm.nih.gov/36892533/)). Hall et al. (2022) documented the Arg51 clustering: "*We report nine individuals from five families with severe aniridia and/or microphthalmia (with no detectable PAX6 mutation) with ultrarare monoallelic missense variants altering the Arg51 codon of MAB21L1*" ([PMID: 36413568](https://pubmed.ncbi.nlm.nih.gov/36413568/)).

This dual architecture — recessive LoF multisystem syndrome vs. dominant Arg51 ocular disease — is the single most important nuance for a knowledge-base curator, because the disease name ("ocular" is shared) can easily mislead toward the dominant entity. Evidence source: human clinical genetics.

### Finding 3 — Cardinal COFG phenotypes and the exact biallelic variant set

The defining cohort (Rad et al. 2019) comprised **10 affected individuals from 5 consanguineous families**. The **cardinal features** are: a characteristic facial gestalt, corneal dystrophy, hairy nipples, underdeveloped labioscrotal folds and scrotum / scrotal agenesis, cerebellar hypoplasia with ataxia, and variable microcephaly, together with intellectual disability and additional ophthalmological anomalies. The abstract states the cardinal features "*include a characteristic facial gestalt, corneal dystrophy, hairy nipples, underdeveloped labioscrotal folds and scrotum/scrotal agenesis as well as cerebellar hypoplasia with ataxia and variable microcephaly*" ([PMID: 30487245](https://pubmed.ncbi.nlm.nih.gov/30487245/)).

The **causal variants** were four loss-of-function (p.Glu281fs*20, p.Arg287Glufs*14, p.Tyr280*, p.Ser93Serfs*48) and one missense (p.Gln233Pro), all biallelic (homozygous): "*We identified four homozygous MAB21L1 loss of function variants (p.Glu281fs*20, p.Arg287Glufs*14 p.Tyr280* and p.Ser93Serfs*48) and one missense variant (p.Gln233Pro) in 10 affected individuals from 5 consanguineous families*" ([PMID: 30487245](https://pubmed.ncbi.nlm.nih.gov/30487245/)). Evidence source: human clinical genetics.

### Finding 4 — MAB21L1 is a cGAS structural homolog; mechanism is transcriptional regulation and ER stress, not demonstrated catalysis

MAB21L1 is a **structural homolog of cGAS** (cyclic GMP-AMP synthase). The crystal structure (de Oliveira Mann et al. 2016) shows human MAB21L1 adopts the cGAS nucleotidyltransferase fold in an inactive conformation, with a putative NTP-binding site corresponding to the DNA-binding site of cGAS. The authors report "*high structural conservation between MAB21L1 and cGAS but also uncovers important differences*" ([PMID: 27271801](https://pubmed.ncbi.nlm.nih.gov/27271801/)). Despite the fold, Hall et al. (2022) could **not demonstrate nucleotidyltransferase activity**: "*The predicted nucleotidyltransferase function of MAB21L1 could not be demonstrated using purified protein with a variety of nucleotide substrates and oligonucleotide activators*" ([PMID: 36413568](https://pubmed.ncbi.nlm.nih.gov/36413568/)). They instead found MAB21L1 associates with PAX6 regulators MEIS1/MEIS2/PBX1 and the NCoR component TBL1XR1, implicating a **transcriptional/co-regulatory role**.

Functional genomics in the mouse supports this. Single-cell RNA-seq of the Mab21l1-null lens placode (Yamada et al. 2021) revealed 279 differentially expressed genes (131 down, 148 up), including downregulation of lens-fate genes and enrichment of DNA/nucleotide-metabolism genes. The authors "*identified 21 lens-specific genes that were downregulated in Mab21l1-null cells, including three key genes involved in lens formation: Pitx3, Maf and Sfrp2*," and immunohistochemistry "*indicated endoplasmic reticulum stress at the 24- to 26-somite stage in Mab21l1-null lens placodes*" ([PMID: 34779479](https://pubmed.ncbi.nlm.nih.gov/34779479/)), preceding cell death. Evidence sources: structural biology / in vitro biochemistry; mouse model single-cell transcriptomics.

### Finding 5 — The Mab21l1-null mouse recapitulates core COFG features across all three affected systems

Promsut et al. (2024) report that the **Mab21l1-null mouse model recapitulates core human COFG features**: severe microphthalmia and fontanelle dysosteogenesis mirroring human patients, and — in males — hypoplastic preputial glands (the rodent-specific derivative of the cranial scrotal fold), paralleling scrotal agenesis in male human patients. The abstract states: "*A COFG mouse model with Mab21l1-null mutation causes severe microphthalmia and fontanelle dysosteogenesis, similar to the symptoms in human patients*," and "*One of the typical symptoms is scrotal agenesis in male infants, while male Mab21l1-null mice show hypoplastic preputial glands, a rodent-specific derivative of the cranial scrotal fold*" ([PMID: 37750449](https://pubmed.ncbi.nlm.nih.gov/37750449/)). Neonatal MAB21L1 expression localizes to two mesenchymal cell populations in the external genitalia (beneath scrotal/labial skin and around preputial/clitoral glands). This model spans eye, craniofacial, and genital systems, making it a strong platform for mechanistic study. Evidence source: mouse model.

### Finding 6 — Monoallelic vs biallelic confirmed as two distinct disorders; dominant microphthalmia has "moderate" clinical validity

Li et al. (2024, *Ophthalmic Genet*) reported a rare Arg51 monoallelic missense in 4 individuals of one family with microphthalmia and reviewed 13 further autosomal-dominant families. Genotype–phenotype analysis confirmed that **monoallelic carriers show solely eye abnormalities**, diverging sharply from biallelic COFG (ocular + extraocular). A ClinGen-style assessment judged the clinical validity of MAB21L1 for AD microphthalmia as **"moderate."** The abstract notes "*patients with a single allele missense variant in MAB21L1 exhibited solely eye abnormalities*" and that "*the clinical validity of MAB21L1 and the emerging autosomal dominant microphthalmia can be regarded as moderate*" ([PMID: 39016008](https://pubmed.ncbi.nlm.nih.gov/39016008/)). Evidence source: human clinical genetics / gene-disease validity curation.

### Finding 7 — Gene identifiers and genomic context

MAB21L1 ("mab-21 like 1") maps to **chromosome 13q13.3** (GRCh38 chr13:35,473,419–35,478,764, minus strand). Identifiers: **HGNC:6757, NCBI Gene 4081, Ensembl ENSG00000180660, UniProt Q13394.** The coding sequence is **intronless (single-exon)**. The NCBI RefSeq summary states: "This gene is similar to the MAB-21 cell fate-determining gene found in C. elegans. It may be involved in eye and cerebellum development." All reported COFG LoF variants and the dominant Arg51 missense fall within this single coding exon — a feature that simplifies single-gene and panel sequencing.

### Finding 8 — Evolutionarily conserved cell-fate determinant expressed in developing eye and cerebellum

MAB21L1 is the vertebrate ortholog of *C. elegans* **mab-21**, the founding family member. mab-21 encodes a 386-aa protein required for the choice of alternate cell fates in the male tail and acts as a genetic modifier of Hox (HOM-C) gene function in sensory ray identity (Chow et al. 1995): "*The gene mab-21, which encodes a novel protein of 386 amino acids, is required for the choice of alternate cell fates by several cells in the C. elegans male tail*" ([PMID: 8582275](https://pubmed.ncbi.nlm.nih.gov/8582275/)). In the mouse, Mab21l1 and the paralog Mab21l2 transcripts are "*predominantly detected in the eye and cerebellum*" with partially overlapping embryonic expression (Wong & Chow 1999) ([PMID: 10495284](https://pubmed.ncbi.nlm.nih.gov/10495284/)). This expression pattern maps directly onto the eye and cerebellar target organs of COFG. Evidence sources: invertebrate model (C. elegans); mouse developmental expression.

### Finding 9 — Epidemiology, course, and management

COFG is **ultra-rare** (fewer than ~20 reported individuals; the defining cohort is 10 individuals from 5 consanguineous Middle Eastern families). Inheritance is **autosomal recessive**, with ~25% sibling recurrence risk; **consanguinity / homozygosity-by-descent is the dominant risk factor**. Malformations are **congenital** and the course is **static (non-degenerative)**. There is **no disease-modifying or targeted therapy, gene therapy, or interventional clinical trial**; management is **supportive and multidisciplinary** (ophthalmologic surgery, physiotherapy/occupational therapy for ataxia, developmental/educational support, reconstructive genital surgery) plus genetic counseling and prenatal/preimplantation testing for prevention. The defining paper confirms the "*ultrarare but clinically recognisable*" recessive nature of the disorder ([PMID: 30487245](https://pubmed.ncbi.nlm.nih.gov/30487245/)). Evidence source: human clinical genetics.

---

## Full Report by Section

### 1. Disease Information

COFG syndrome is a congenital, multisystem, autosomal-recessive malformation syndrome. Its name is an acronym of its four cardinal domains: **C**erebellar (hypoplasia, ataxia), **O**cular (corneal dystrophy, microphthalmia, other anterior-segment anomalies), **C**raniofacial (distinctive gestalt, variable microcephaly), and **G**enital (underdeveloped labioscrotal folds, scrotal agenesis). Intellectual disability and hairy nipples are additional recognizable features.

**Key identifiers:** MONDO:0032774 · OMIM:618479 · Orphanet: listed under rare developmental-defect syndromes (MAB21L1-related syndrome). ICD-10/ICD-11 have no specific code (coded under congenital malformation syndromes, e.g., ICD-11 LD2F). MeSH: no dedicated descriptor. Gene: MAB21L1 (HGNC:6757).

**Synonyms / alternative names:** Cerebello-Oculo-Facio-Genital syndrome; COFG syndrome; MAB21L1-related syndrome (recessive). *Note:* the dominant Arg51 ocular disorder is a separate entity (microphthalmia/aniridia; "BAMD") and should not be listed as a synonym.

**Information source:** Aggregated disease-level resources (OMIM, MONDO) built from individual-patient case series; the primary data derive from individual patients in consanguineous families, not EHR-scale cohorts.

### 2. Etiology

**Primary cause:** Genetic — **biallelic loss-of-function variants in MAB21L1**. No environmental, infectious, or multifactorial contribution is established.

**Genetic risk factors:** The causal variants are the two pathogenic MAB21L1 alleles. The single dominant risk factor for occurrence is **consanguinity / homozygosity-by-descent**, which raises the probability of inheriting two null alleles. No modifier genes or susceptibility loci are defined.

**Environmental risk / protective factors:** None identified. No lifestyle, occupational, toxic, dietary, or infectious factors are implicated — consistent with a fully penetrant Mendelian malformation syndrome.

**Protective factors:** None genetic or environmental identified. (The only "protective" consideration is non-consanguineous mating, which lowers recurrence probability in at-risk families.)

**Gene–environment interactions:** None known or expected for this monogenic, highly penetrant disorder.

### 3. Phenotypes

| Phenotype | Type | HPO suggestion | Onset | Course | Frequency (defining cohort) |
|---|---|---|---|---|---|
| Cerebellar hypoplasia | Clinical sign (imaging) | HP:0001321 | Congenital | Static | Core feature |
| Ataxia | Clinical sign | HP:0001251 | Infancy | Static | Core feature |
| Intellectual disability | Behavioral/cognitive | HP:0001249 | Childhood | Static | Common |
| Microphthalmia | Physical manifestation | HP:0000568 | Congenital | Static | Common |
| Corneal dystrophy | Clinical sign | HP:0001131 | Congenital/early | Variable | Core feature |
| Distinctive facial gestalt | Physical manifestation | HP:0001999 | Congenital | Static | Core feature |
| Microcephaly (variable) | Physical manifestation | HP:0000252 | Congenital | Static | Variable |
| Hairy nipples | Physical manifestation | HP:0100783 (abnormal nipple) | Congenital | Static | Distinctive |
| Scrotal agenesis / underdeveloped labioscrotal folds | Physical manifestation | HP:0000050 / HP:0000054 | Congenital | Static | Core (males) |

**Severity/progression:** Features are congenital and non-progressive (static). Severity is moderate-to-severe for the structural malformations; expressivity is somewhat variable (e.g., microcephaly present in some, absent in others).

**Quality-of-life impact:** Combined visual impairment (corneal/ocular disease), motor disability (cerebellar ataxia), and intellectual disability substantially affect daily functioning, education, and independence. Disease-specific QoL instruments (EQ-5D, SF-36) have not been applied to this ultra-rare disorder.

### 4. Genetic / Molecular Information

**Causal gene:** MAB21L1 (HGNC:6757; NCBI Gene 4081; Ensembl ENSG00000180660; UniProt Q13394), chromosome 13q13.3, single coding exon (intronless).

**Pathogenic variants (recessive COFG):** Four LoF — p.Glu281fs*20, p.Arg287Glufs*14, p.Tyr280* (nonsense), p.Ser93Serfs*48 (frameshift) — plus one missense p.Gln233Pro, all biallelic/homozygous ([PMID: 30487245](https://pubmed.ncbi.nlm.nih.gov/30487245/)). Variant classes: frameshift, nonsense, missense. Functional consequence: **loss of function.**

**Dominant ocular variants (separate disorder):** Monoallelic missense at the **Arg51 codon** — c.152G>T p.Arg51Leu, c.152G>A, c.155T>G ([PMID: 36413568](https://pubmed.ncbi.nlm.nih.gov/36413568/); [PMID: 33973683](https://pubmed.ncbi.nlm.nih.gov/33973683/)). These are de novo in several families, absent from gnomAD, and act via a dominant (likely gain-of-function or dominant-negative) mechanism distinct from the recessive LoF.

**Allele frequency:** Pathogenic variants are ultra-rare/absent in gnomAD, consistent with severe recessive disease and de novo dominant alleles.

**Somatic vs germline:** Germline. No somatic or cancer association.

**Modifier genes:** None established.

**Epigenetic information:** No disease-specific DNA-methylation or histone-modification signature reported.

**Chromosomal abnormalities:** None; disease is caused by point/indel variants within the single MAB21L1 exon, not by large structural rearrangements.

### 5. Environmental Information

Not applicable. COFG is a purely monogenic congenital disorder with no reported environmental, lifestyle, toxic, or infectious contributors.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic loss-of-function variants in MAB21L1** (frameshift/nonsense/deleterious missense) **lead to** absence or non-function of the MAB21L1 protein in developing tissues.
2. Loss of MAB21L1 **results in** failure of its non-catalytic regulatory function — MAB21L1 normally associates with PAX6-pathway regulators (MEIS1/MEIS2/PBX1) and the NCoR co-repressor component TBL1XR1 (inferred co-regulatory role; catalysis not demonstrated) ([PMID: 36413568](https://pubmed.ncbi.nlm.nih.gov/36413568/)).
3. This **leads to** dysregulated transcription of developmental cell-fate programs. In the lens placode this is demonstrated: downregulation of lens-fate genes **Pitx3, Maf, Sfrp2** and perturbed DNA/nucleotide-metabolism genes ([PMID: 34779479](https://pubmed.ncbi.nlm.nih.gov/34779479/)).
4. Transcriptional dysregulation **results in** cellular stress — specifically **endoplasmic reticulum (ER) stress** at the 24–26 somite stage in Mab21l1-null lens placodes ([PMID: 34779479](https://pubmed.ncbi.nlm.nih.gov/34779479/)).
5. ER stress **leads to** **cell death / apoptosis** of affected progenitor populations (inferred to follow the demonstrated stress).
6. Loss of the correct cell-fate program and progenitor depletion **results in** failed/aberrant organogenesis in MAB21L1-expressing tissues — the developing **eye** and **cerebellum** (Finding 8) — and, via mesenchymal expression, the **craniofacial skeleton** and **external genitalia**.
7. This **manifests clinically as** the COFG tetrad: microphthalmia/corneal dystrophy (eye), cerebellar hypoplasia with ataxia (cerebellum), distinctive facial gestalt with variable microcephaly (craniofacial), and scrotal agenesis (genital).

**Branch (dominant disease):** A *monoallelic* Arg51 missense does not cause loss of function but a dominant allele that **leads to** an eye-restricted developmental defect (microphthalmia/aniridia) without the extraocular branches above.

**Pathways / processes:** PAX6 developmental gene-regulatory network; eye and cerebellar morphogenesis; lens-fiber cell-fate specification. GO suggestions: GO:0001654 (eye development), GO:0021549 (cerebellum development), GO:0030154 (cell differentiation), GO:0034976 (response to ER stress), GO:0006915 (apoptotic process), GO:0048593 (camera-type eye morphogenesis). Cell types (CL): lens placode/fiber cells (lens fiber cell CL:0011004), cerebellar neurons, cranial/genital mesenchymal cells (mesenchymal cell CL:0000134).

**Protein dysfunction:** MAB21L1 folds like cGAS but is catalytically inactive in vitro; the recessive variants cause loss of a structural/scaffolding/transcriptional-regulatory function rather than loss of an enzyme activity ([PMID: 27271801](https://pubmed.ncbi.nlm.nih.gov/27271801/); [PMID: 36413568](https://pubmed.ncbi.nlm.nih.gov/36413568/)). The broader CD-NTase family context is reviewed in [PMID: 31593902](https://pubmed.ncbi.nlm.nih.gov/31593902/), which notes "*The CD-NTase family also includes uncharacterized human genes like MB21D2 and Mab21L1, highlighting emerging functions of cGAS-like signaling beyond innate immunity.*"

**Molecular profiling:** scRNA-seq of Mab21l1-null lens placode — 279 DEGs (131 down / 148 up); lens-fate downregulation and ER stress ([PMID: 34779479](https://pubmed.ncbi.nlm.nih.gov/34779479/)). No human proteomic/metabolomic/lipidomic signature available.

### 7. Anatomical Structures Affected

- **Primary organs:** Eye (UBERON:0000970) — cornea (UBERON:0000964), lens (UBERON:0000965); Cerebellum (UBERON:0002037); Craniofacial skeleton / cranial sutures and fontanelles (UBERON:0003129 skull); External genitalia — scrotum (UBERON:0001300).
- **Body systems:** Nervous (cerebellum, cognition), visual/ocular, musculoskeletal/craniofacial, reproductive/genital.
- **Secondary involvement:** Skin adnexa (nipple hair). No cardiovascular, respiratory, renal, or hepatic primary involvement reported.
- **Tissue/cell level:** Neuroectoderm-derived ocular tissues (lens placode, cornea), cerebellar neuroepithelium, and cranial/genital mesenchyme (two mesenchymal populations in neonatal external genitalia express MAB21L1) ([PMID: 37750449](https://pubmed.ncbi.nlm.nih.gov/37750449/)).
- **Subcellular:** Endoplasmic reticulum (GO:0005783) implicated via ER stress; MAB21L1 protein is cytoplasmic/nuclear-associated.
- **Localization / lateralization:** Bilateral and generally symmetric congenital malformations.

### 8. Temporal Development

- **Onset:** Congenital / prenatal (malformations established during embryogenesis).
- **Onset pattern:** Chronic/congenital (structural, present at birth).
- **Progression:** Static, non-degenerative. No defined stages; features are stable over the lifespan.
- **Course pattern:** Stable lifelong.
- **Critical period:** Embryonic organogenesis of eye and cerebellum (mouse ER stress/cell death window at the 24–26 somite stage marks a vulnerable developmental interval) — the relevant window is prenatal, so there is no postnatal intervention window to reverse the malformations.

### 9. Inheritance and Population

- **Epidemiology:** Ultra-rare; <~20 reported individuals worldwide. No reliable prevalence/incidence estimate (likely <1 per 1,000,000). Defining cohort: 10 individuals / 5 families ([PMID: 30487245](https://pubmed.ncbi.nlm.nih.gov/30487245/)).
- **Inheritance:** Autosomal recessive (biallelic LoF). Sibling recurrence risk ~25%.
- **Penetrance:** Complete for biallelic LoF (fully penetrant in reported families).
- **Expressivity:** Variable (e.g., microcephaly variable).
- **Anticipation / mosaicism:** Not applicable / not reported.
- **Founder effects / consanguinity:** No specific founder haplotype; **consanguinity is the dominant driver** — reported families are consanguineous, predominantly Middle Eastern.
- **Carrier frequency:** Not established; heterozygous carriers are asymptomatic.
- **Sex ratio:** Both sexes affected; genital phenotype is most conspicuous in males (scrotal agenesis). No sex bias in occurrence.

### 10. Diagnostics

- **Primary diagnostic:** Molecular genetic testing identifying **biallelic pathogenic MAB21L1 variants**. Because MAB21L1 is a single intronless coding exon, **single-gene sequencing** is efficient; in practice diagnosis is usually made by **whole-exome (WES)** or **whole-genome (WGS)** sequencing or a developmental-disorder/microphthalmia gene panel, confirmed by Sanger and segregation.
- **Clinical/imaging:** Brain MRI (cerebellar hypoplasia); ophthalmologic examination (microphthalmia, corneal dystrophy, anterior-segment assessment); dysmorphology exam (facial gestalt, microcephaly, nipple hair); genital examination.
- **Chromosomal microarray / karyotype / FISH:** Normal — not diagnostic (no structural/CNV basis).
- **Biomarkers / metabolic / enzyme assays:** None; no biochemical biomarker exists.
- **Differential diagnosis:** Other cerebellar hypoplasia syndromes; other microphthalmia/anophthalmia-coloboma disorders (notably **PAX6-related aniridia** — note the dominant Arg51 MAB21L1 phenotype specifically occurs **without detectable PAX6 mutation**); Gómez-López-Hernández and related cerebello-facial syndromes. The combination of cerebellar + ocular + craniofacial + genital features with recessive inheritance is distinctive.
- **Screening:** Cascade carrier testing within affected families; prenatal/preimplantation genetic testing where the familial variants are known. No population newborn screening.

### 11. Outcome / Prognosis

- **Survival / mortality:** No evidence of reduced life expectancy; the malformations are structural and non-lethal. No disease-specific mortality data (cohort too small).
- **Morbidity / disability:** Significant lifelong disability from combined visual impairment, cerebellar ataxia, and intellectual disability.
- **Disease course:** Static; complications are those of the fixed malformations (visual limitation, motor/coordination difficulties, learning disability, genital anomaly). No progressive organ failure.
- **Recovery potential:** Congenital structural defects are not recoverable; rehabilitation and surgery mitigate function.
- **Prognostic factors / biomarkers:** None validated; severity tracks with the extent of structural malformation.

### 12. Treatment

**No disease-modifying, gene, RNA, cell, or targeted therapy exists.** Management is **supportive and multidisciplinary** (NCIT: Supportive Care, C15277):

- **Ophthalmologic care / surgery** (NCIT: Ophthalmologic Surgical Procedure) for corneal and anterior-segment disease; visual aids.
- **Physical and occupational therapy** (NCIT: Physical Therapy C15415; Occupational Therapy) for cerebellar ataxia and motor function.
- **Developmental, educational, and speech support** for intellectual disability.
- **Reconstructive genital/urologic surgery** as indicated for genital malformation.
- **Genetic counseling** for the family (recurrence risk, reproductive options).

No pharmacotherapy, pharmacogenomics, immunotherapy, or interventional clinical trial (no NCT identifiers) is available for COFG.

### 13. Prevention

- **Primary prevention:** Genetic counseling for consanguineous and at-risk couples; where familial variants are known, **prenatal diagnosis** or **preimplantation genetic testing (PGT-M)** can prevent recurrence.
- **Secondary prevention:** Cascade testing of relatives; early multidisciplinary intervention (vision, developmental, motor) to optimize function.
- **Tertiary prevention:** Rehabilitation and corrective surgery to limit disability from the fixed malformations.
- **Immunization / public-health / environmental measures:** Not applicable (non-infectious, non-environmental).
- **Counseling:** Central to management given ~25% sibling recurrence risk.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** Human MAB21L1 (NCBI Gene 4081); mouse *Mab21l1* (NCBI Gene 17127; *Mus musculus*, NCBI:txid10090); and the founding invertebrate ortholog *C. elegans* **mab-21** (*Caenorhabditis elegans*, NCBI:txid6239). A paralog, MAB21L2, shares eye/cerebellum expression.
- **Natural disease in other species:** No naturally occurring COFG-equivalent disease is catalogued in companion animals or wildlife (no OMIA entry noted). Disease knowledge comes from engineered models, not spontaneous animal disease.
- **Comparative / evolutionary biology:** The mab-21 family is deeply conserved as a **cell-fate determinant** — *C. elegans* mab-21 governs male-tail cell-fate choice and modifies Hox function ([PMID: 8582275](https://pubmed.ncbi.nlm.nih.gov/8582275/)) — and vertebrate orthologs retain eye/cerebellum developmental roles ([PMID: 10495284](https://pubmed.ncbi.nlm.nih.gov/10495284/)), demonstrating conserved mechanism.
- **Transmission / zoonosis:** Not applicable.

### 15. Model Organisms

- **Mouse (primary model):** The **Mab21l1-null mouse** recapitulates core COFG features — severe microphthalmia, fontanelle/craniofacial dysosteogenesis, and (in males) hypoplastic preputial glands modeling scrotal agenesis ([PMID: 37750449](https://pubmed.ncbi.nlm.nih.gov/37750449/)). Used for single-cell transcriptomics of the lens placode, revealing the Pitx3/Maf/Sfrp2 program and ER stress ([PMID: 34779479](https://pubmed.ncbi.nlm.nih.gov/34779479/)). Model type: mammalian knockout. Strong eye/craniofacial/genital recapitulation; cerebellar and cognitive phenotypes less characterized (limitation).
- **Zebrafish:** The paralog *mab21l2* complementation assay has been used to test human MAB21L1 variant function in vivo ([PMID: 33973683](https://pubmed.ncbi.nlm.nih.gov/33973683/)).
- **C. elegans:** mab-21 is the ancestral functional model for cell-fate determination ([PMID: 8582275](https://pubmed.ncbi.nlm.nih.gov/8582275/)).
- **In vitro:** Purified recombinant MAB21L1 for structural/biochemical assays ([PMID: 27271801](https://pubmed.ncbi.nlm.nih.gov/27271801/); [PMID: 36413568](https://pubmed.ncbi.nlm.nih.gov/36413568/)).
- **Resources:** MGI (mouse), ZFIN (zebrafish), WormBase (C. elegans).

---

## Mechanistic Model / Interpretation

```
 Biallelic LoF in MAB21L1 (frameshift / nonsense / deleterious missense)
                 │  (loss of function)
                 ▼
 Absent/non-functional MAB21L1 protein in developing eye, cerebellum,
 craniofacial & genital mesenchyme
                 │  (loss of non-catalytic co-regulatory role;
                 │   assoc. with MEIS1/2, PBX1, TBL1XR1 — inferred)
                 ▼
 Dysregulated developmental transcription
 (lens placode: down Pitx3, down Maf, down Sfrp2; perturbed DNA/nucleotide metab.)
                 │  (demonstrated in mouse scRNA-seq)
                 ▼
 Endoplasmic reticulum (ER) stress  --->  Cell death / apoptosis
 (24-26 somite stage)                     of progenitor populations
                 │
                 ▼
 Failed / aberrant organogenesis in MAB21L1-expressing tissues
                 │
   ┌─────────────┼───────────────┬────────────────┐
   ▼             ▼               ▼                ▼
 Eye          Cerebellum     Craniofacial      Genital
 (micro-      (hypoplasia,   (facial gestalt,  (scrotal
 phthalmia,   ataxia)        microcephaly,     agenesis,
 corneal                     fontanelle        labioscrotal
 dystrophy)                  dysosteogenesis)  hypoplasia)

 -- BRANCH (different disease) --
 Monoallelic Arg51 missense (de novo, dominant) ---> isolated
 microphthalmia / aniridia (BAMD), NO extraocular features
```

The key interpretive point is that MAB21L1 is **not acting as an enzyme** in this disease: despite its cGAS-like nucleotidyltransferase fold, catalytic activity has not been demonstrated, and the recessive phenotype is best explained by loss of a **developmental transcriptional/co-regulatory function** in PAX6-network-associated cell-fate determination. The spatial logic of the syndrome — eye, cerebellum, craniofacial, genital — matches the tissues where MAB21L1 (and its orthologs) are expressed and where it governs cell fate. The dominant Arg51 ocular disorder is mechanistically separate (a dominant missense effect confined to ocular development), and keeping these two entities distinct is essential for accurate curation.

| Feature | Recessive COFG | Dominant Arg51 ocular disease |
|---|---|---|
| Inheritance | Autosomal recessive | Autosomal dominant (often de novo) |
| Zygosity | Biallelic | Monoallelic |
| Variant type | LoF (frameshift/nonsense) + rare missense | Missense at Arg51 codon |
| Organ involvement | Cerebellum, eye, craniofacial, genital | Eye only (microphthalmia/aniridia/BAMD) |
| Mechanism | Loss of function | Dominant (gain-of-function / dominant-negative) |
| Gene-disease validity | Established | Moderate (ClinGen-style) |
| Key refs | PMID 30487245 | PMID 36892533, 36413568, 33973683, 39016008 |

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report | Evidence type |
|---|---|---|---|
| [30487245](https://pubmed.ncbi.nlm.nih.gov/30487245/) | *MAB21L1 loss of function causes a syndromic neurodevelopmental disorder…* | **Defining paper** — recessive COFG, cardinal features, biallelic variants | Human clinical genetics |
| [36892533](https://pubmed.ncbi.nlm.nih.gov/36892533/) | *Missense Mutations in MAB21L1: … Autosomal Dominant Ocular BAMD Syndrome* | Distinguishes recessive COFG from dominant ocular disease | Human clinical genetics |
| [36413568](https://pubmed.ncbi.nlm.nih.gov/36413568/) | *Monoallelic variants … MAB21L1 Arg51 Cause Aniridia and microphthalmia* | Arg51 dominant disorder; no NTase activity; MEIS/PBX/TBL1XR1 interactions | Human genetics + in vitro |
| [39016008](https://pubmed.ncbi.nlm.nih.gov/39016008/) | *Monoallelic missense variants in MAB21L1* | Confirms eye-only dominant phenotype; "moderate" gene-disease validity | Human genetics / curation |
| [34779479](https://pubmed.ncbi.nlm.nih.gov/34779479/) | *MAB21L1 modulates gene expression … in the lens placode* | Mechanism: lens-fate genes, DNA metabolism, ER stress | Mouse scRNA-seq |
| [37750449](https://pubmed.ncbi.nlm.nih.gov/37750449/) | *External genitalia phenotypes of a Mab21l1-null mouse model* | Model recapitulation (eye, craniofacial, genital) | Mouse model |
| [27271801](https://pubmed.ncbi.nlm.nih.gov/27271801/) | *Structural … characterization of MAB21L1* | cGAS structural homology; inactive conformation | Structural biology |
| [31593902](https://pubmed.ncbi.nlm.nih.gov/31593902/) | *cGAS and CD-NTase enzymes: structure, mechanism, evolution* | Places MAB21L1 in CD-NTase family | Review |
| [33973683](https://pubmed.ncbi.nlm.nih.gov/33973683/) | *Identification of missense MAB21L1 variants in microphthalmia and aniridia* | Arg51Leu + zebrafish complementation | Human genetics + zebrafish |
| [10495284](https://pubmed.ncbi.nlm.nih.gov/10495284/) | *Developmental expression of Mab21l2…* | Eye/cerebellum expression of Mab21 family | Mouse developmental |
| [8582275](https://pubmed.ncbi.nlm.nih.gov/8582275/) | *The mab-21 gene of C. elegans…* | Ancestral cell-fate function, Hox modifier | C. elegans |

---

## Limitations and Knowledge Gaps

1. **Very small cohort.** The entire human evidence base for recessive COFG rests on ~10–20 individuals, almost all from consanguineous Middle Eastern families. Prevalence, full phenotypic range, penetrance details, and natural history are therefore imprecise.
2. **Mechanism partially inferred.** ER stress and transcriptional dysregulation are demonstrated in the mouse lens placode, but the apoptotic step and the extension of the lens mechanism to cerebellum, craniofacial skeleton, and genitalia are inferred by analogy rather than directly shown. The precise molecular function of MAB21L1 (scaffold? transcriptional co-regulator? cryptic enzyme?) remains unresolved — notably, no nucleotidyltransferase activity has been demonstrated.
3. **Genotype–phenotype for the recessive missense variant.** The recessive missense p.Gln233Pro is grouped with LoF alleles, but its mechanistic equivalence to true nulls is assumed, not proven.
4. **Dominant vs recessive boundary.** How a monoallelic Arg51 missense produces a dominant, eye-restricted disease while complete biallelic loss produces a multisystem syndrome is not mechanistically explained (possible gain-of-function/dominant-negative vs loss-of-function dichotomy).
5. **Model gaps.** The Mab21l1-null mouse models eye/craniofacial/genital features well but the cerebellar and cognitive phenotypes are less characterized.
6. **No biomarkers, no therapy, no trials.** There is no biochemical biomarker, no disease-modifying therapy, and no interventional trial.

---

## Proposed Follow-up Experiments / Actions

1. **Tissue-resolved mechanism:** Perform conditional/whole-animal single-cell and spatial transcriptomics of Mab21l1-null **cerebellum, cranial sutures, and external genital mesenchyme** to test whether the lens-placode mechanism (cell-fate gene loss → ER stress → apoptosis) generalizes across all four affected systems.
2. **Define molecular function:** Use proximity labeling (BioID/TurboID) and ChIP/CUT&RUN in relevant progenitors to map the MAB21L1 interactome and genomic occupancy, directly testing the proposed PAX6-network co-regulatory role (MEIS1/2, PBX1, TBL1XR1).
3. **Variant functional assays:** Establish a standardized in vivo (zebrafish *mab21l2* complementation) and in vitro assay to classify recessive missense (e.g., p.Gln233Pro) as hypomorph vs null, and to contrast with the dominant Arg51 alleles — clarifying the LoF vs dominant mechanism split.
4. **Recessive vs dominant modeling:** Generate knock-in mice carrying the human Arg51 missense (heterozygous) to test whether it reproduces isolated ocular disease, formally separating the two disorders in vivo.
5. **Clinical consolidation:** Build an international registry / GeneMatcher-based case series to refine the phenotypic spectrum, penetrance, and natural history, and to support ClinGen gene–disease validity re-curation for both the recessive and dominant entities.
6. **Curation action:** In the knowledge base, encode COFG (recessive, MONDO:0032774) and the dominant Arg51 microphthalmia/aniridia as **separate disease entries sharing MAB21L1**, with explicit cross-references to prevent conflation.

---

*Report compiled from a 5-iteration autonomous investigation; 9 confirmed findings; 11 primary papers reviewed. All mechanistic and clinical claims are attributed to the cited PMIDs above.*


## Artifacts

- [OpenScientist final report](Cerebellar_Ocular_Craniofacial_And_Genital_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Cerebellar_Ocular_Craniofacial_And_Genital_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 10 |
| Quoted claims found in source | 10 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 11 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 16 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001321` (1 mention) - the report calls it "Clinical sign (imaging)"; HP calls it **Cerebellar hypoplasia**
- `HP:0001251` (1 mention) - the report calls it "Clinical sign"; HP calls it **Ataxia**
- `HP:0001249` (1 mention) - the report calls it "Behavioral/cognitive"; HP calls it **Intellectual disability**
- `HP:0000568` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Microphthalmia**
- `HP:0001131` (1 mention) - the report calls it "Clinical sign"; HP calls it **Corneal dystrophy**
- `HP:0001999` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Abnormal facial shape**
- `HP:0000252` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Microcephaly**
- `HP:0100783` (1 mention) - the report calls it "abnormal nipple"; HP calls it **Breast aplasia**
- `UBERON:0000970` (1 mention) - the report calls it "Primary organs:** Eye"; UBERON calls it **eye**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0034976` (1 mention) - the report calls it "response to ER stress"; GO calls it **response to endoplasmic reticulum stress**, and lists "response to ER stress" among its other names
- `GO:0005783` (1 mention) - the report calls it "Subcellular:** Endoplasmic reticulum"; GO calls it **endoplasmic reticulum**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.