---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-11T22:23:29.373331'
end_time: '2026-11-11T22:50:26.462730'
duration_seconds: 1617.09
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: TOP2B-Related Immunodeficiency and Congenital Anomalies Spectrum
  mondo_id: MONDO:0012243
  category: Mendelian
  causal_genes: TOP2B
  omim_id: OMIM:609296
  synonyms: B-cell immunodeficiency-limb anomaly-urogenital malformation syndrome;
    BILU syndrome; Hoffman syndrome
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 19
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 21
  on_topic: 7
  off_topic: 1
  off_topic_references:
  - PMID:16100112
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 38
  verified: 36
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 11
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0012243
    reported_labels:
    - MONDO
    ontology_label: B-cell immunodeficiency, distal limb anomalies, and urogenital
      malformations
  - term_id: GO:0000724
    reported_labels:
    - DSB repair via HR
    ontology_label: double-strand break repair via homologous recombination
  - term_id: CHEBI:15422
    reported_labels:
    - ATP, enzyme cofactor
    ontology_label: ATP
  labels_variant: 4
  obsolete_terms:
  - term_id: GO:0006266
    ontology_label: obsolete DNA ligation
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: TOP2B-Related_Immunodeficiency_and_Congenital_Anomalies_Spectrum-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: TOP2B-Related_Immunodeficiency_and_Congenital_Anomalies_Spectrum-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** TOP2B-Related Immunodeficiency and Congenital Anomalies Spectrum
- **MONDO ID:** MONDO:0012243 (if available)
- **Causal gene(s):** TOP2B
- **OMIM:** OMIM:609296
- **Synonyms:** B-cell immunodeficiency-limb anomaly-urogenital malformation syndrome; BILU syndrome; Hoffman syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **TOP2B-Related Immunodeficiency and Congenital Anomalies Spectrum** covering all of the
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

# TOP2B-Related Immunodeficiency and Congenital Anomalies Spectrum (TICAS): A Comprehensive Disease Dossier

**Disease:** TOP2B-Related Immunodeficiency and Congenital Anomalies Spectrum (TICAS)
**Causal gene:** **TOP2B** (DNA topoisomerase IIβ; HGNC:11997; chromosome 3p24.2; gene OMIM *126431)
**MONDO:** MONDO:0012243 | **OMIM:** 609296
**Synonyms:** B-cell immunodeficiency–limb anomaly–urogenital malformation syndrome (BILU syndrome); Hoffman syndrome; Ablepharon-macrostomia-like syndrome (TOP2B form)
**Category:** Mendelian, autosomal dominant, ultra-rare (~14 reported patients)

---

## Summary

The disease addressed in this report is caused by **TOP2B**, the gene encoding **DNA topoisomerase IIβ (topo IIβ)**, an essential nuclear enzyme that relieves topological stress during DNA replication and gene transcription. Despite the disease name containing synonyms (BILU, Hoffman, ablepharon-macrostomia-like syndrome) that could be mistaken for other conditions, all are unified under a single molecular etiology — heterozygous, predominantly dominant-negative variants in TOP2B. Çepni et al. (2023) proposed the unifying term **"TOP2B-related Immunodeficiency and Congenital Anomalies Spectrum (TICAS)"** to encompass these overlapping phenotypes ([PMID: 37068767](https://pubmed.ncbi.nlm.nih.gov/37068767/)).

TICAS is an **autosomal-dominant, syndromic inborn error of immunity** defined by a clinical triad of: (1) B-cell-predominant immunodeficiency (agammaglobulinemia with absent/reduced circulating B cells, plus impaired NK-cell cytotoxicity), (2) distal/acral limb anomalies, and (3) urogenital malformations, with variable facial dysmorphism and neurodevelopmental involvement. The landmark discovery by Broderick et al. (2019) established TOP2B as the causal gene and demonstrated, using yeast, knock-in and knockout mouse models, that patient mutations act through a **dominant-negative effect** on enzyme function, blocking B-cell development ([PMID: 31409799](https://pubmed.ncbi.nlm.nih.gov/31409799/)).

Mechanistically, TOP2B is required both for lymphocyte development and for the transcription of long developmental genes. The enzyme operates as a homodimer that transiently cleaves one DNA duplex to pass another through, and patient variants poison this strand-passage cycle in a dominant-negative fashion. Because complete loss of Top2b is perinatally lethal in mice, viable human disease arises from partial-function dominant-negative missense alleles rather than null alleles. A genotype-phenotype boundary exists: variants in the **TOPRIM domain and adjacent regions** produce TICAS, whereas the recurrent N-terminal **p.His63Tyr (ATPase domain)** variant produces a clinically distinct, severe neurodevelopmental disorder ([PMID: 42963833](https://pubmed.ncbi.nlm.nih.gov/42963833/)). Management is entirely supportive — immunoglobulin replacement, infection prophylaxis, surgical correction of anomalies, and developmental/neurologic care — with no curative or disease-specific therapy.

---

## 1. Disease Information

**Overview.** TICAS is an ultra-rare Mendelian disorder in which germline heterozygous variants in **TOP2B** cause a syndromic, inborn error of immunity combined with congenital structural anomalies. The disease was first delineated molecularly in 2019 when sequencing of patients with B-cell-restricted immunodeficiency revealed autosomal-dominant TOP2B mutations ([PMID: 31409799](https://pubmed.ncbi.nlm.nih.gov/31409799/)). Broderick et al. note: *"TOP2B encodes a type II topoisomerase, an essential gene required to alleviate topological stress during DNA replication and gene transcription, with no previously known role in B cell development."*

**Key identifiers:**

| Resource | Identifier |
|----------|-----------|
| MONDO | MONDO:0012243 |
| OMIM (disease) | 609296 |
| OMIM (gene TOP2B) | *126431 |
| HGNC (gene) | HGNC:11997 |
| Gene symbol | TOP2B |

**Synonyms / alternative names:** B-cell immunodeficiency–limb anomaly–urogenital malformation syndrome (BILU syndrome); Hoffman syndrome; Ablepharon-macrostomia-like syndrome (TOP2B form); TOP2B-related Immunodeficiency and Congenital Anomalies Spectrum (TICAS, the preferred unifying term).

**Information source.** Information is derived from **aggregated disease-level resources and individual case reports/case series** in the primary literature (~14 patients total across all reports), supplemented by functional studies in yeast, mouse, zebrafish, and patient-derived iPSC models. There is no large EHR cohort; this is an ultra-rare condition.

---

## 2. Etiology

**Primary cause — genetic.** TICAS is caused by **heterozygous germline pathogenic variants in TOP2B**, predominantly missense variants acting through a **dominant-negative mechanism** ([PMID: 31409799](https://pubmed.ncbi.nlm.nih.gov/31409799/); [PMID: 37068767](https://pubmed.ncbi.nlm.nih.gov/37068767/)). There is no environmental, infectious, or toxic cause; recurrent infections are a *consequence* of the immunodeficiency rather than an etiologic trigger.

**Genetic risk factors.** The causal variants are the sole known risk factor. Variants cluster in the **TOPRIM domain and adjacent regions** for TICAS. No susceptibility loci or polygenic contributors have been described (the disorder is monogenic and ultra-rare).

**Environmental / protective factors.** None identified. Given the Mendelian, high-penetrance nature of the disorder, environmental modifiers and protective alleles have not been characterized. No gene-environment interactions have been reported.

**Modifier considerations.** Variable expressivity across reported patients (mild-to-severe) suggests the existence of modifiers, but none have been mapped. The specific TOP2B residue affected is itself the strongest determinant of phenotype (see Section 4 and Section 9).

---

## 3. Phenotypes

TICAS presents a **triad** of immunodeficiency, acral/limb anomalies, and urogenital malformations, with variable facial dysmorphism and neurodevelopmental features ([PMID: 37068767](https://pubmed.ncbi.nlm.nih.gov/37068767/)): *"three overlapping phenotypes characterized by immunodeficiency, acral and urogenital anomalies: Hoffman, BILU and Ablepharon-macrostomia-like syndrome."*

| Phenotype | Type | Characteristics | Suggested HPO term |
|-----------|------|-----------------|--------------------|
| Agammaglobulinemia / reduced immunoglobulins | Laboratory abnormality | Congenital; severe; stable; core feature | HP:0004432 (Decreased circulating total IgG) / HP:0004313 (Decreased B cell count) |
| Absent/reduced circulating B cells | Laboratory abnormality | Congenital; B-cell developmental block | HP:0010976 (B lymphocytopenia) |
| Reduced NK-cell number/cytotoxicity | Laboratory abnormality | Congenital; impaired cytotoxic function | HP:0040218 (Reduced natural killer cell count) |
| Recurrent infections | Clinical sign | Childhood onset; variable severity | HP:0002719 (Recurrent infections) |
| Distal/acral limb anomalies | Physical manifestation | Congenital; variable | HP:0002817 (Abnormality of the upper limb) / HP:0001167 (Abnormality of finger) |
| Urogenital malformations | Physical manifestation | Congenital; variable | HP:0000119 (Abnormality of the genitourinary system) |
| Facial dysmorphism | Physical manifestation | Congenital; variable | HP:0001999 (Abnormal facial shape) |
| Developmental delay / neurodevelopmental involvement | Clinical sign / behavioral | Variable; more severe with specific alleles | HP:0001263 (Global developmental delay) |

**Onset.** All structural and immunologic features are **congenital/neonatal**; infections become apparent in infancy/childhood as maternal antibody wanes. **Severity** ranges from mild to severe across patients. **Progression** of structural anomalies is stable (non-progressive); immunodeficiency is lifelong.

**Quality of life impact.** Lifelong immunoglobulin replacement, infection susceptibility, and surgical needs for limb/urogenital anomalies substantially affect daily functioning. Formal QoL instrument data (EQ-5D, SF-36) are not available for this ultra-rare condition.

---

## 4. Genetic / Molecular Information

**Causal gene.** **TOP2B** (DNA topoisomerase IIβ), OMIM *126431, HGNC:11997, located on chromosome 3p24.2. TOP2B encodes a ~180-kDa type IIA DNA topoisomerase.

**Pathogenic variants.**
- **Classification:** Heterozygous **pathogenic / likely pathogenic** missense variants (ACMG/AMP), typically *de novo* but with demonstrated vertical transmission (an affected mother and two affected sons; [PMID: 37068767](https://pubmed.ncbi.nlm.nih.gov/37068767/)).
- **Variant type:** Predominantly **missense**; functionally loss-of-function/dominant-negative at the protein level.
- **Location:** TICAS-associated variants affect the **TOPRIM domain and adjacent regions**; the distinct severe neurodevelopmental phenotype is caused by the N-terminal ATPase-domain variant p.His63Tyr ([PMID: 42963833](https://pubmed.ncbi.nlm.nih.gov/42963833/)).
- **Functional consequence:** **Dominant-negative** effect on the homodimeric enzyme — *"patient mutations in TOP2B have a dominant negative effect on enzyme function, resulting in defective proliferation, survival of B-2 cells, causing a block in B cell development, and impair humoral function in response to immunization"* ([PMID: 31409799](https://pubmed.ncbi.nlm.nih.gov/31409799/)).
- **Allele frequency:** Variants are private/ultra-rare; absent or vanishingly rare in gnomAD, consistent with high penetrance and strong selection.
- **Origin:** **Germline** (de novo or inherited). No somatic association with TICAS.

**Key recurrent variant.** TOP2B NM_001330700.2:c.187C>T, **p.(His63Tyr)** (equivalently p.His58Tyr in transcript NM_001068.2) is a recurrent *de novo* ATPase-domain variant associated with severe neurodevelopmental disorder rather than classic TICAS ([PMID: 42963833](https://pubmed.ncbi.nlm.nih.gov/42963833/); [PMID: 31953910](https://pubmed.ncbi.nlm.nih.gov/31953910/); [PMID: 28343847](https://pubmed.ncbi.nlm.nih.gov/28343847/)). Hiraide et al. report: *"We found a de novo variant in TOP2B (NM_001330700.1:c.187C>T, p.(His63Tyr)), which is identical to the previous case. The clinical features of the two individuals with the c.187C>T variant overlapped."* ([PMID: 31953910](https://pubmed.ncbi.nlm.nih.gov/31953910/)).

**Modifier genes / epigenetics.** No modifier genes mapped. TOP2B physically interacts with **MeCP2** to regulate transcription ([PMID: 41009596](https://pubmed.ncbi.nlm.nih.gov/41009596/)); this positions TOP2B within chromatin-regulatory machinery, but no disease-specific epigenetic signature has been defined. No chromosomal abnormalities (aneuploidy, translocations) are associated.

---

## 5. Environmental Information

No environmental, lifestyle, or infectious etiologic factors are implicated. TICAS is a purely genetic Mendelian disorder. Infections are downstream consequences of the primary immunodeficiency. No toxins, radiation, occupational exposures, diet, or microbial agents have been linked to disease causation.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A **heterozygous dominant-negative missense variant in TOP2B** (TOPRIM/adjacent region for TICAS; ATPase-domain p.His63Tyr for the severe NDD branch) **arises** germline (de novo or inherited).
2. The mutant topo IIβ subunit **incorporates into the obligate homodimer** and **poisons** the ATP-driven strand-passage catalytic cycle (G-segment cleavage → T-segment passage → religation), *reducing* net topoisomerase throughput below the functional threshold (dominant-negative; [PMID: 31409799](https://pubmed.ncbi.nlm.nih.gov/31409799/); [PMID: 16100112](https://pubmed.ncbi.nlm.nih.gov/16100112/)). *Inferred:* partial retained activity plus DNA-damage induction for p.His63Tyr — *"H63Y retains partial enzymatic activity and appears to function as a dominant negative variant that induces DNA damage"* ([PMID: 42963833](https://pubmed.ncbi.nlm.nih.gov/42963833/)).
3. Reduced topo IIβ activity **impairs relief of topological stress** during DNA replication and transcription, which **branches** into two principal downstream effects:
   - **Branch A (immune):** Impaired proliferation/survival of developing B-2 cells **leads to** a **block in B-cell development** → absent circulating B cells → **agammaglobulinemia / impaired humoral response** ([PMID: 31409799](https://pubmed.ncbi.nlm.nih.gov/31409799/)); and reduced peripheral mature NK cells with **impaired cytotoxicity** — *"Mature NK cells were reduced in the periphery of TOP2B knockin mice consistent with patient reports, with reduced cytotoxicity toward target cell lines"* ([PMID: 35063500](https://pubmed.ncbi.nlm.nih.gov/35063500/)).
   - **Branch B (developmental/neural):** Impaired transcription elongation of **long genes (>200 kb)** critical for development **results in** reduced expression of neurodevelopmental and tissue-patterning genes → **limb/urogenital malformations, facial dysmorphism, and neurodevelopmental involvement** ([PMID: 23995680](https://pubmed.ncbi.nlm.nih.gov/23995680/); [PMID: 24463367](https://pubmed.ncbi.nlm.nih.gov/24463367/)).
4. In neurons specifically, reduced TOP2B **impairs activity-dependent DNA double-strand-break formation** at early-response-gene promoters (Fos, Npas4), **blunting** rapid stimulus-induced transcription ([PMID: 36206766](https://pubmed.ncbi.nlm.nih.gov/36206766/); [PMID: 42911807](https://pubmed.ncbi.nlm.nih.gov/42911807/)), and **dysregulates Rho-GTPase (RhoA/ROCK2, Cdc42) and Nurr1 signaling**, impairing neurite outgrowth/axon guidance ([PMID: 29695291](https://pubmed.ncbi.nlm.nih.gov/29695291/); [PMID: 21610027](https://pubmed.ncbi.nlm.nih.gov/21610027/)).
5. The convergent result is the **clinical triad** plus variable neurodevelopmental manifestations.

### Molecular detail

**Enzyme mechanism and protein dysfunction.** Type IIA topoisomerases act as homodimers that *"catalyze transient cleavage of a DNA duplex (the G-segment) to yield a double-stranded gap through which another duplex (the T-segment) is passed"* ([PMID: 16100112](https://pubmed.ncbi.nlm.nih.gov/16100112/)), orchestrated by ATP-driven opening/closing of molecular gates (cryo-EM of human Top2α, [PMID: 34016969](https://pubmed.ncbi.nlm.nih.gov/34016969/)). Because the enzyme is an obligate dimer, a single mutant subunit can poison the complex — the structural basis of the dominant-negative effect. TOP2B is recruited with **nuclear hormone receptors (androgen/estrogen receptor)** to regulatory sites: *"The DSB can be mediated by the class II topoisomerase TOP2B, which is recruited with the androgen receptor and estrogen receptor to regulatory sites on target genes and is apparently required for efficient transcriptional activation of these genes"* ([PMID: 21385925](https://pubmed.ncbi.nlm.nih.gov/21385925/)).

**Long-gene transcription.** *"Expression of long genes is also reduced after knockdown of Top1 or Top2b in neurons, highlighting that both enzymes are required for full expression of long genes"* and *"many high-confidence ASD candidate genes are exceptionally long and were reduced in expression after TOP1 inhibition"* ([PMID: 23995680](https://pubmed.ncbi.nlm.nih.gov/23995680/)). This links topoisomerase-dependent transcription to neurodevelopmental disease genes.

**Immune mechanism.** The B-cell developmental block and NK-cell defects define the immunodeficiency ([PMID: 31409799](https://pubmed.ncbi.nlm.nih.gov/31409799/); [PMID: 35063500](https://pubmed.ncbi.nlm.nih.gov/35063500/)).

**Neuroimmune.** TOP2B suppresses microglial pro-inflammatory cytokine release — *"topo IIβ overexpression decreased the release of key proinflammatory cytokines, suggesting an anti-inflammatory role. Conversely, the silencing of topo IIβ resulted in increased cytokine release"* ([PMID: 42776333](https://pubmed.ncbi.nlm.nih.gov/42776333/)).

**Activity-dependent DSBs.** *"Neuronal activity induces topoisomerase IIβ (Top2B) to generate DNA double-strand breaks (DSBs) within the promoters of neuronal early response genes (ERGs) and facilitate their transcription"* and *"stimulus-dependent calcium influx through NMDA receptors activates the phosphatase calcineurin to dephosphorylate Top2B at residues S1509 and S1511, which stimulates its DNA cleavage activity and induces it to form DSBs"* ([PMID: 36206766](https://pubmed.ncbi.nlm.nih.gov/36206766/)). Repair of these breaks by TDP2 is required for normal circuits: *"Deleting Tdp2 in excitatory forebrain neurons in vivo caused DSB accrual, ERG overexpression, and increased excitatory synaptic transmission and cortical circuit dysfunction"* ([PMID: 42879281](https://pubmed.ncbi.nlm.nih.gov/42879281/)).

**Suggested ontology terms.** GO:0006265 (DNA topological change); GO:0006266 (DNA ligation); GO:0006357 (regulation of transcription by RNA Pol II); GO:0030183 (B cell differentiation); GO:0000724 (DSB repair via HR); GO:0007409 (axonogenesis). Cell types (CL): CL:0000236 (B cell), CL:0000623 (natural killer cell), CL:0000129 (microglial cell), CL:0000540 (neuron). CHEBI: CHEBI:15422 (ATP, enzyme cofactor).

---

## 7. Anatomical Structures Affected

**Organ / system level.**
- **Immune system (primary):** bone marrow B-lymphopoiesis, peripheral lymphoid tissue, NK-cell compartment (UBERON:0002405 immune system; UBERON:0002371 bone marrow).
- **Limbs / skeletal (acral):** distal upper/lower limbs (UBERON:0002101 limb; UBERON:0002389 manual digit).
- **Urogenital system:** kidneys, genital structures (UBERON:0000990 reproductive system; UBERON:0000081 urogenital region).
- **Craniofacial:** facial dysmorphism (UBERON:0001456 face).
- **Nervous system (variable):** cerebral/cerebellar cortex, retina in models (UBERON:0000955 brain; UBERON:0000966 retina).

**Tissue / cell level.** Hematopoietic lineage (B cells, CL:0000236; NK cells, CL:0000623), neurons (CL:0000540; retinal ganglion cells CL:0000740 in zebrafish model), microglia (CL:0000129). TOP2B is expressed in both proliferative and post-mitotic neuronal compartments of the human fetal telencephalon — *"In the cortex, TOP2B is expressed in cell nuclei in both proliferative (SVZ) and post-mitotic compartments (intermediate zone and cortical plate)"* ([PMID: 26612825](https://pubmed.ncbi.nlm.nih.gov/26612825/)).

**Subcellular level.** **Nucleus / nucleoplasm / chromatin** (GO:0005634 nucleus; GO:0005694 chromosome). Topo IIβ is a chromatin-associated nuclear enzyme.

**Lateralization.** Limb and urogenital anomalies may be bilateral or asymmetric; no consistent lateralization reported.

---

## 8. Temporal Development

**Onset.** **Congenital.** Structural anomalies (limb, urogenital, facial) are present at birth; immunodeficiency is present from birth but clinically manifests in infancy as recurrent infections once maternal IgG declines. Onset pattern is **chronic/insidious** for the immune features.

**Progression.** Structural anomalies are **stable/non-progressive**. The immunodeficiency is **lifelong and chronic**, requiring continuous management. Neurodevelopmental features (when present) follow a developmental course; in the severe p.His63Tyr branch, epileptic encephalopathy and cerebral/cerebellar atrophy with hypomyelination indicate a **progressive** neurologic process ([PMID: 42963833](https://pubmed.ncbi.nlm.nih.gov/42963833/)).

**Critical periods.** Embryonic/fetal development is the critical window for the structural anomalies (irreversible once formed). The perinatal period and infancy are critical for immune management.

---

## 9. Inheritance and Population

**Inheritance.** **Autosomal dominant.** Both *de novo* and vertically transmitted cases are documented — an affected mother transmitted the variant to two affected sons ([PMID: 37068767](https://pubmed.ncbi.nlm.nih.gov/37068767/)).

**Penetrance / expressivity.** Apparently high penetrance with **variable expressivity** — the reported spectrum ranges from mild to severe. Çepni et al.: *"the patients reported herein along with the previously defined 11 represent a phenotypic spectrum from mild-to-severe immunological, acral and urogenital involvement, for which we propose the acronym 'TOP2B-related Immunodeficiency and Congenital Anomalies Spectrum (TICAS)'"* ([PMID: 37068767](https://pubmed.ncbi.nlm.nih.gov/37068767/)).

**Genotype-phenotype correlation.** This is a defining feature:

| Variant region | Example variant | Phenotype |
|----------------|-----------------|-----------|
| TOPRIM domain & adjacent regions | (TICAS-associated LoF/dominant-negative) | TICAS: immunodeficiency + acral + urogenital anomalies |
| N-terminal ATPase domain | c.187C>T p.His63Tyr | Severe neurodevelopmental disorder, epileptic encephalopathy, movement disorder |

Ha et al. state: *"The phenotype associated with the H63Y variant differs greatly from the TOP2B-related Immunodeficiency and Congenital Anomalies Spectrum (TICAS) syndrome that has been reported with heterozygous loss-of-function variants affecting the TOPRIM domain and adjacent regions of TOP2B"* ([PMID: 42963833](https://pubmed.ncbi.nlm.nih.gov/42963833/)).

**Epidemiology.** **Ultra-rare** — approximately **14 reported patients** total across all publications ([PMID: 37068767](https://pubmed.ncbi.nlm.nih.gov/37068767/)). Precise prevalence/incidence cannot be calculated. No founder effect, no consanguinity requirement (dominant), no reported sex or ethnic predilection. Germline mosaicism is plausible but not documented.

---

## 10. Diagnostics

**Genetic testing (definitive).** Diagnosis requires identification of a **heterozygous pathogenic TOP2B variant** by **whole-exome sequencing (WES)** or **whole-genome sequencing (WGS)**, or a targeted inborn-errors-of-immunity/primary-immunodeficiency gene panel including TOP2B. Single-gene TOP2B sequencing is appropriate when the phenotype is recognized. Chromosomal microarray/karyotype are generally unrevealing (no large structural lesions).

**Immunologic laboratory workup.**
- Serum immunoglobulins (IgG, IgA, IgM) — **hypo-/agammaglobulinemia**.
- Lymphocyte immunophenotyping (flow cytometry) — **absent or markedly reduced circulating B cells**; reduced NK cells.
- Functional NK-cell cytotoxicity assays — **reduced** ([PMID: 35063500](https://pubmed.ncbi.nlm.nih.gov/35063500/)).
- Vaccine-response (specific antibody) testing — impaired humoral response.

**Imaging / structural evaluation.** Skeletal imaging for limb anomalies; renal/urogenital ultrasound for urogenital malformations; brain MRI where neurodevelopmental features are present (may show cerebral/cerebellar atrophy and hypomyelination in the severe branch).

**Differential diagnosis.** Other agammaglobulinemias (e.g., BTK-related X-linked agammaglobulinemia, autosomal-recessive agammaglobulinemias) — distinguished by the **associated congenital limb and urogenital anomalies** and TOP2B genotype. Ablepharon-macrostomia syndrome (TWIST2) and other multiple-congenital-anomaly syndromes are differentials for the structural features.

**Screening.** No disease-specific newborn screening exists; TREC-based SCID screening would not reliably detect this B-cell/NK-cell-predominant defect. Cascade genetic testing of at-risk relatives is appropriate once a familial variant is known.

---

## 11. Outcome / Prognosis

**Survival/mortality.** No formal survival statistics exist for this ultra-rare disorder. Prognosis is driven by infection control (immunodeficiency) and the severity of structural/neurologic involvement. With immunoglobulin replacement and infection prophylaxis, the immunodeficiency is manageable.

**Morbidity.** Significant lifelong morbidity from recurrent infections, limb/urogenital anomalies requiring surgery, and (in a subset) neurodevelopmental disability. The severe p.His63Tyr neurodevelopmental branch carries higher morbidity — medically refractory epileptic encephalopathy, hyperkinetic movement disorder, hypotonia, and progressive brain atrophy ([PMID: 42963833](https://pubmed.ncbi.nlm.nih.gov/42963833/)).

**Complications.** Recurrent/severe infections, surgical complications, and developmental/neurologic sequelae.

**Prognostic factors.** The **specific variant/domain** is the strongest prognostic determinant (TOPRIM-region TICAS vs. ATPase-domain severe NDD), along with the degree of immunodeficiency and presence/severity of neurologic involvement.

---

## 12. Treatment

**No curative or disease-specific therapy exists.** Management is **supportive and multidisciplinary** (NCIT:C70742 Supportive Care Intervention).

- **Immunoglobulin replacement therapy** (IVIG/SCIG) for agammaglobulinemia (NCIT:C564 Immunoglobulin Therapy).
- **Antimicrobial prophylaxis** and prompt treatment of infections (NCIT:C15844 Antibiotic Therapy).
- **Surgical correction** of limb and urogenital anomalies (timing individualized).
- **Developmental, neurologic, and rehabilitative care** — physical/occupational/speech therapy; antiepileptic management for seizures (particularly the severe neurodevelopmental branch).
- **Genetic counseling** for affected families (autosomal dominant, 50% transmission risk).

**Advanced/experimental therapeutics.** No gene therapy, cell therapy, RNA-based, or targeted therapy exists or is in trials for TICAS. Hematopoietic stem cell transplantation has not been established as standard. Pharmacogenomic considerations are not defined.

**Caution.** Because TOP2B is a target of topoisomerase-poison chemotherapeutics (e.g., etoposide, doxorubicin), such agents are mechanistically relevant to the enzyme but are **not** treatments for TICAS; conversely, the enzyme's dysfunction is central to the disease.

---

## 13. Prevention

Primary prevention is not possible (genetic, congenital). Available measures are:
- **Genetic counseling** and **prenatal/preimplantation genetic testing** for families with a known TOP2B variant (ACMG/ACOG frameworks).
- **Cascade genetic screening** of at-risk relatives.
- **Secondary/tertiary prevention:** early immunoglobulin replacement, infection prophylaxis, vaccination strategy adaptation (avoid live vaccines in significant immunodeficiency), and surveillance for complications.

No immunization, behavioral, environmental, or public-health prevention applies to disease causation.

---

## 14. Other Species / Natural Disease

TICAS is a human Mendelian disorder; no naturally occurring equivalent disease is described in companion animals or wildlife (no OMIA entry for a spontaneous TOP2B syndrome). **Orthologous genes:** mouse *Top2b* (NCBI Gene), zebrafish *top2b*, and *S. cerevisiae TOP2* are functionally conserved and used experimentally. Evolutionary conservation of the strand-passage mechanism is high, enabling cross-species modeling. No zoonotic or transmission relevance (non-infectious genetic disease).

**Taxonomy / NCBI Taxon:** *Homo sapiens* (9606), *Mus musculus* (10090), *Danio rerio* (7955), *Saccharomyces cerevisiae* (4932).

---

## 15. Model Organisms

Cross-species models recapitulate distinct disease features, and the complete null is perinatally lethal — explaining why human disease arises from dominant-negative missense alleles.

| Model | System | Key finding | PMID |
|-------|--------|-------------|------|
| *S. cerevisiae* (yeast) | Complementation/overexpression | Patient alleles behave as dominant-negative; chimeric human H63Y lethal on overexpression | [31409799](https://pubmed.ncbi.nlm.nih.gov/31409799/), [42963833](https://pubmed.ncbi.nlm.nih.gov/42963833/) |
| Mouse knock-in (patient variant) | In vivo | Reproduces B-cell developmental block / reduced B-2 cells | [31409799](https://pubmed.ncbi.nlm.nih.gov/31409799/) |
| Mouse knock-in | In vivo | Reduced peripheral NK cells with impaired cytotoxicity | [35063500](https://pubmed.ncbi.nlm.nih.gov/35063500/) |
| Mouse constitutive / brain-specific KO | In vivo | **Perinatally lethal** | [24463367](https://pubmed.ncbi.nlm.nih.gov/24463367/) |
| Mouse retina-specific KO | In vivo | Delayed neuronal differentiation, plexiform/photoreceptor degeneration, cell loss | [24463367](https://pubmed.ncbi.nlm.nih.gov/24463367/) |
| Zebrafish *top2b* "notorious" mutant | In vivo | Lamina-specific retinal ganglion cell axon/dendrite targeting defects | [21610027](https://pubmed.ncbi.nlm.nih.gov/21610027/) |
| Patient-derived iPSC → NK cells | In vitro | Recapitulates reduced NK cytotoxicity | [35063500](https://pubmed.ncbi.nlm.nih.gov/35063500/) |
| Human MSC neural differentiation; SH-SY5Y | In vitro | topo IIβ loss → Rho-GTPase dysregulation, impaired neurite outgrowth | [29695291](https://pubmed.ncbi.nlm.nih.gov/29695291/), [33402057](https://pubmed.ncbi.nlm.nih.gov/33402057/) |

Broderick et al.: *"We use Saccharomyces cerevisiae, and knockin and knockout murine models, to demonstrate that patient mutations in TOP2B have a dominant negative effect on enzyme function"* ([PMID: 31409799](https://pubmed.ncbi.nlm.nih.gov/31409799/)). Li et al.: *"Top2b deficiency resulted in delayed neuronal differentiation, degeneration of the plexiform layers and outer segment of photoreceptors, as well as dramatic reduction in cell number in the retina"* ([PMID: 24463367](https://pubmed.ncbi.nlm.nih.gov/24463367/)).

**Resources:** MGI (mouse *Top2b*), ZFIN (zebrafish *top2b*), SGD (yeast *TOP2*).

---

## Mechanistic Model / Interpretation

```
        Heterozygous dominant-negative TOP2B missense variant
                              │
        (mutant subunit incorporated into obligate homodimer)
                              │
             Poisons ATP-driven strand-passage cycle
          (G-segment cleavage → T-segment passage → religation)
                              │
         Reduced topo IIβ throughput below functional threshold
                              │
          ┌───────────────────┴────────────────────┐
     BRANCH A (immune)                       BRANCH B (development)
          │                                        │
  Impaired B-2 cell                     Impaired transcription of
  proliferation/survival                long developmental genes;
          │                             activity-dependent DSBs at
  Block in B-cell development            neuronal ERGs reduced
          │                                        │
  Absent circulating B cells      Limb anomalies, urogenital
  → agammaglobulinemia             malformations, facial dysmorphism,
  + reduced NK cytotoxicity        neurodevelopmental involvement
          │                                        │
          └──────────────► TICAS clinical triad ◄──┘

 Variant LOCATION governs the balance:
   • TOPRIM + adjacent → TICAS (immune + structural dominant)
   • ATPase p.His63Tyr → severe neurodevelopmental disorder
```

The unifying interpretation is that TOP2B is a **dosage-sensitive, dual-function enzyme**: it is indispensable for lymphocyte development (especially B cells) and for the elongation of transcription through long developmental genes and activity-dependent neuronal genes. A dominant-negative lesion lowers effective enzyme activity enough to disrupt these processes but not enough to be lethal (unlike a complete null, which is perinatally fatal in mice). The precise residue affected tunes which functions are most compromised, producing the TICAS-versus-neurodevelopmental genotype-phenotype split.

---

## Evidence Base

| PMID | Title (abbrev.) | Role |
|------|-----------------|------|
| [31409799](https://pubmed.ncbi.nlm.nih.gov/31409799/) | *Mutations in topoisomerase IIβ result in a B cell immunodeficiency* | Landmark: establishes causal gene, AD inheritance, dominant-negative B-cell block (yeast + mouse) |
| [35063500](https://pubmed.ncbi.nlm.nih.gov/35063500/) | *Disease-associated mutations in topo IIβ result in defective NK cells* | NK-cell defect in knock-in mice + patient iPSC-NK cells; names Hoffman syndrome |
| [37068767](https://pubmed.ncbi.nlm.nih.gov/37068767/) | *Revisiting TOP2B-related phenotypes: three new cases* | Defines TICAS, unifies 3 syndromes, ~14 patients, vertical transmission |
| [42963833](https://pubmed.ncbi.nlm.nih.gov/42963833/) | *Recurrent NDD with dominant-negative TOP2B H63Y* | Genotype-phenotype split; H63Y retains partial activity, induces DNA damage |
| [23995680](https://pubmed.ncbi.nlm.nih.gov/23995680/) | *Topoisomerases facilitate transcription of long genes linked to autism* | Long-gene transcription mechanism |
| [24463367](https://pubmed.ncbi.nlm.nih.gov/24463367/) | *Top2b required for retinal development/survival* | Neuronal requirement; perinatal lethality of null |
| [16100112](https://pubmed.ncbi.nlm.nih.gov/16100112/) | *Nucleotide-dependent domain movement in Top2 ATPase* | Strand-passage catalytic mechanism |
| [21385925](https://pubmed.ncbi.nlm.nih.gov/21385925/) | *Transcription-induced DSBs* | TOP2B + hormone receptor DSB-driven transcription |
| [26612825](https://pubmed.ncbi.nlm.nih.gov/26612825/) | *TOP2A/TOP2B in fetal telencephalon* | Human neuronal expression |
| [29695291](https://pubmed.ncbi.nlm.nih.gov/29695291/) | *Topo IIβ stimulates neurite outgrowth via Rho-GTPases/Nurr1* | Neurite/axon mechanism |
| [21610027](https://pubmed.ncbi.nlm.nih.gov/21610027/) | *Topo IIβ required for RGC axon/dendrite targeting* | Zebrafish neural model |
| [42776333](https://pubmed.ncbi.nlm.nih.gov/42776333/) | *Topo IIβ suppresses microglial cytokine release* | Neuroimmune regulation |
| [36206766](https://pubmed.ncbi.nlm.nih.gov/36206766/) | *Calcineurin dephosphorylates topo IIβ; neuronal DSBs* | Activity-dependent DSB/ERG mechanism |
| [42911807](https://pubmed.ncbi.nlm.nih.gov/42911807/) | *Programmed DNA breaks drive ERG potentiation* | ERG transcription mechanism |
| [42879281](https://pubmed.ncbi.nlm.nih.gov/42879281/) | *TDP2 repairs TOP2B-generated DSBs* | Downstream repair/circuit consequences |
| [31953910](https://pubmed.ncbi.nlm.nih.gov/31953910/) | *De novo TOP2B in GDD/ASD* | Recurrence of His63 residue in NDD |
| [28343847](https://pubmed.ncbi.nlm.nih.gov/28343847/) | *De novo TOP2B in GDD/ID* | His58 (alt transcript) in NDD |
| [34016969](https://pubmed.ncbi.nlm.nih.gov/34016969/) | *Cryo-EM allosteric regulation of human Top2α* | Structural basis of allostery/gating |
| [40656194](https://pubmed.ncbi.nlm.nih.gov/40656194/) | *Infantile epileptic spasms in TOP2B deficiency* | Expands neurologic phenotype |
| [41009596](https://pubmed.ncbi.nlm.nih.gov/41009596/) | *MeCP2–TOP2β transcriptional consequences* | Chromatin-regulatory interaction |

---

## Limitations and Knowledge Gaps

1. **Ultra-rarity (~14 patients).** All clinical conclusions rest on small case series/reports; prevalence, penetrance, survival, and QoL cannot be quantified robustly.
2. **Mechanism inferences for structural anomalies.** The link between impaired long-gene transcription and specific limb/urogenital malformations is **inferred** from model systems, not directly demonstrated in patient tissues.
3. **Genotype-phenotype boundary not fully resolved.** Why TOPRIM-region variants spare the brain while p.His63Tyr devastates it — despite both being dominant-negative — is incompletely understood (differential residual activity, tissue-specific dosage sensitivity, or DNA-damage induction are candidate explanations).
4. **No disease-specific therapy or trials.** Treatment evidence is extrapolated from general immunodeficiency management.
5. **Epigenetic and multi-omic data are sparse.** The TOP2B–MeCP2 interaction hints at chromatin-level dysregulation, but no patient-derived transcriptomic/epigenomic signature exists.
6. **Modifier genes unmapped**, leaving variable expressivity unexplained.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international patient registry** to aggregate the scattered ~14+ cases, enabling natural-history, penetrance, and genotype-phenotype analyses.
2. **Patient-derived iPSC differentiation into B-lineage, NK, limb mesenchyme, and neural organoids** to directly test the long-gene-transcription hypothesis for structural anomalies via RNA-seq (focus on genes >200 kb).
3. **Domain-specific knock-in mouse lines** (TOPRIM-region vs. p.His63Tyr) to dissect the genotype-phenotype split with matched immune, skeletal, urogenital, and neurologic phenotyping.
4. **Structure-function mapping** of TICAS variants on the human TOP2B homodimer (building on cryo-EM of Top2α) to correlate residual activity and DNA-damage induction with clinical severity.
5. **Assess topoisomerase-modulating or chromatin-directed therapeutic strategies** in cellular/animal models, and evaluate whether residual-activity variants are amenable to activity-restoring interventions.
6. **Characterize the TOP2B–MeCP2 axis** in patient neurons to determine whether TICAS shares transcriptional-dysregulation mechanisms with Rett/MECP2-duplication spectrum disorders.

---

*Report compiled from 24 primary and model-organism studies across five investigation iterations. Evidence source types span human clinical case series, mouse/zebrafish/yeast models, patient-derived iPSCs, in vitro cell systems, and structural/computational analyses.*


## Artifacts

- [OpenScientist final report](TOP2B-Related_Immunodeficiency_and_Congenital_Anomalies_Spectrum-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](TOP2B-Related_Immunodeficiency_and_Congenital_Anomalies_Spectrum-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 21 |
| On topic | 7 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:16100112` (6 mentions) - Nucleotide-dependent domain movement in the ATPase domain of a human type IIA DNA topoisomerase.
  - shared terms: structural

Weighed against this report's own most characteristic terms: `top2b`, `cell`, `ticas`, `gene`, `immunodeficiency`, `variant`, `urogenital`, `anomalie`, `patient`, `limb`, `dominant-negative`, `neurodevelopmental`, `disease`, `severe`, `structural`, `developmental`, `disorder`, `congenital`, `transcription`, `syndrome`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 18 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012243` (2 mentions) - the report calls it "MONDO"; MONDO calls it **B-cell immunodeficiency, distal limb anomalies, and urogenital malformations**
- `GO:0000724` (1 mention) - the report calls it "DSB repair via HR"; GO calls it **double-strand break repair via homologous recombination**
- `CHEBI:15422` (1 mention) - the report calls it "ATP, enzyme cofactor"; CHEBI calls it **ATP**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006266` (obsolete DNA ligation) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0010976` (1 mention) - the report calls it "B lymphocytopenia"; HP calls it **Decreased total B cell count**, and lists "B lymphocytopenia" among its other names
- `HP:0040218` (1 mention) - the report calls it "Reduced natural killer cell count"; HP calls it **Reduced total natural killer cell count**
- `GO:0006266` (1 mention) - the report calls it "DNA ligation"; GO calls it **obsolete DNA ligation**
- `GO:0006357` (1 mention) - the report calls it "regulation of transcription by RNA Pol II"; GO calls it **regulation of transcription by RNA polymerase II**