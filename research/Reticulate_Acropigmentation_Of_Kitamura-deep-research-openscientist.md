---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-27T18:49:07.915683'
end_time: '2026-10-27T19:03:05.964216'
duration_seconds: 838.05
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Reticulate Acropigmentation Of Kitamura
  mondo_id: MONDO:0014234
  category: Mendelian
  causal_genes: ADAM10
  omim_id: OMIM:615537
  synonyms: RAK; RAPK; Kitamura reticulate acropigmentation; Kitamura disease
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
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 28
reference_validation:
  total_references: 28
  verified: 28
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 28
  on_topic: 13
  validator_version: 0.4.0
term_validation:
  total_terms: 22
  verified: 19
  not_found: 2
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.095
  labels_checked: 11
  labels_matching: 7
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0014234
    reported_labels:
    - MONDO
    ontology_label: reticulate acropigmentation of Kitamura
  - term_id: HP:0007441
    reported_labels:
    - Reticulated skin pigmentation
    ontology_label: Hyperpigmented/hypopigmented macules
  - term_id: HP:0000212
    reported_labels:
    - Rare (single report)
    ontology_label: Gingival overgrowth
  labels_variant: 1
  unresolved_terms:
  - UBERON:0003401
  - UBERON:0003402
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Reticulate_Acropigmentation_Of_Kitamura-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Reticulate_Acropigmentation_Of_Kitamura-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Reticulate Acropigmentation Of Kitamura
- **MONDO ID:** MONDO:0014234 (if available)
- **Causal gene(s):** ADAM10
- **OMIM:** OMIM:615537
- **Synonyms:** RAK; RAPK; Kitamura reticulate acropigmentation; Kitamura disease
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Reticulate Acropigmentation Of Kitamura** covering all of the
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

# Reticulate Acropigmentation of Kitamura (RAK): A Comprehensive Disease Characterization Report

**Disease:** Reticulate Acropigmentation of Kitamura (RAK; RAPK; Kitamura disease)
**MONDO ID:** MONDO:0014234 · **OMIM:** #615537 · **Causal gene:** **ADAM10** (HGNC:188; NCBI Gene 102; UniProt O14672; a disintegrin and metalloproteinase domain-containing protein 10)
**Category:** Mendelian, autosomal dominant

> **Note on disease identity:** The name "Reticulate Acropigmentation of Kitamura" is correctly matched to **ADAM10**. It should not be confused with the clinically similar **Dowling-Degos disease** (KRT5/POFUT1/POGLUT1/PSENEN/GLMN) or **dyschromatosis symmetrica hereditaria** (ADAR1), which are distinct genetic entities within the overlapping reticulate-pigmentary-disorder spectrum.

---

## Summary

Reticulate Acropigmentation of Kitamura (RAK) is a rare, autosomal-dominant pigmentary genodermatosis caused by **heterozygous loss-of-function variants in ADAM10**, the gene encoding the zinc-metalloprotease and ectodomain sheddase ADAM10. First described by Kitamura in Japan in 1943, the disorder manifests before puberty as reticulate (net-like), slightly depressed, brown pigmented macules concentrated on the dorsa of the hands and feet. Over years the pigmentation extends proximally to the limbs and trunk, and characteristic palmar pits and breaks in the epidermal ridge pattern (dermatoglyphic interruptions) develop. It is a benign, lifelong, cosmetically significant condition with a normal life expectancy and no systemic organ failure in the great majority of patients.

The central molecular insight, established by whole-exome sequencing of a RAK pedigree in 2013, is that RAK results from ADAM10 haploinsufficiency. ADAM10 is the principal **Site-2 (S2) sheddase that activates Notch signaling in the epidermis**. Reduced ADAM10 activity is inferred to lower keratinocyte and melanocyte Notch signaling, dysregulating epidermal differentiation and melanocyte homeostasis. Histopathology shows epidermal atrophy, elongated rete ridges laden with melanin, an increased number of active (dopa-positive) basal melanocytes, and enhanced melanosome transfer to keratinocytes — together producing the reticulate hyperpigmentation. This Notch-centric mechanism places RAK within a larger spectrum of **reticulate pigmentary disorders** that share disruption of Notch processing/glycosylation genes, most notably Dowling-Degos disease (DDD; KRT5, POFUT1, POGLUT1, PSENEN, GLMN).

RAK predominantly affects East Asian (Japanese, Chinese) populations, though cases occur worldwide. Diagnosis rests on clinical and histopathologic recognition supported by ADAM10 genetic testing, which is the most reliable way to distinguish RAK from clinically overlapping reticulate disorders. No curative or disease-modifying therapy exists; treatment is limited to inconsistently effective cosmetic measures (topical/oral retinoids, laser). The principal disease model is the mouse epidermal (K14-Cre) *Adam10* conditional knockout, which recapitulates epidermal Notch loss-of-function; global *Adam10* knockout is embryonic lethal owing to Notch failure. No naturally occurring animal counterpart of RAK has been described.

---

## 1. Disease Information

RAK is a hereditary reticulate pigmentary disorder (RPD) of the acral skin. The causal gene is **ADAM10**. Key identifiers:

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0014234 |
| OMIM | #615537 |
| Gene (OMIM) | ADAM10, *602192* |
| HGNC | HGNC:188 (ADAM10) |
| Orphanet | Listed under reticulate pigmentary disorders / acropigmentation of Kitamura |
| Synonyms | RAK; RAPK; Kitamura reticulate acropigmentation; Kitamura disease; reticulate acropigmentation |

The disease-level information in this report derives from **aggregated disease-level resources and primary case reports / case series**, not from individual EHR datasets. RAK was first described by Kitamura et al. in 1943 ([PMID: 40950988](https://pubmed.ncbi.nlm.nih.gov/40950988/)).

---

## 2. Etiology

**Primary cause — genetic.** RAK is a monogenic Mendelian disorder caused by heterozygous loss-of-function variants in **ADAM10**. Whole-exome sequencing of a RAK family, followed by Sanger sequencing of four additional unrelated patients, identified five heterozygous ADAM10 mutations — three truncating, one splice-site, and one missense — with no mutations in KRT5 (the Dowling-Degos gene), establishing RAK as a genetically distinct entity ([PMID: 23666529](https://pubmed.ncbi.nlm.nih.gov/23666529/)). *"A mutation in ADAM10 encoding a zinc metalloprotease… was identified in the RAK family."*

**Genetic risk factors.** The causal variants themselves are the risk factor; inheritance is autosomal dominant with high penetrance. No additional susceptibility loci or validated modifier genes have been defined.

**Environmental / lifestyle risk factors.** None established. RAK is a constitutive genetic disorder; no toxin, infection, diet, or occupational exposure is known to cause or trigger it. Pigmentation is lifelong and not clearly photo-driven, though sun-exposed acral sites are prominently involved.

**Protective factors.** No genetic or environmental protective factors are known.

**Gene–environment interactions.** None demonstrated.

---

## 3. Phenotypes

RAK phenotypes are primarily **physical manifestations / clinical signs** of the skin.

| Phenotype | Type | Onset | Frequency | Suggested HPO |
|---|---|---|---|---|
| Reticulate hyperpigmentation of dorsal hands/feet | Physical sign | Before puberty (childhood) | Hallmark / near-universal | HP:0007441 (Reticulated skin pigmentation) |
| Slightly depressed pigmented macules | Physical sign | Childhood | Characteristic | HP:0001000 (Abnormality of skin pigmentation) |
| Palmar pits | Physical sign | Childhood–adolescence | Common | HP:0010610 (Palmar pits) |
| Breaks/interruption of dermatoglyphics (epidermal ridges) | Physical sign | Childhood | Common | HP:0007477 (Abnormal dermatoglyphics) |
| Proximal extension to limbs/trunk | Progression feature | Later (years) | Variable | — |
| Skeletal anomalies (absent terminal phalanges of toes; clinodactyly) | Rare associated | Variable | Rare (isolated reports) | HP:0030084 (Clinodactyly) |
| Gingival hyperplasia | Rare associated | Variable | Rare (single report) | HP:0000212 |

**Characteristics.** Onset is pre-pubertal/childhood. Severity is mild–moderate and cosmetic; the course is **chronic, slowly progressive, and non-remitting**, with proximal spread over years. The acral reticulate pigmentation, palmar pits, and dermatoglyphic breaks are the core, highly frequent features; skeletal and gingival anomalies are exceptional.

Key quotations: *"The characteristic skin lesions are reticulate, slightly depressed pigmented macules mainly affecting the dorsa of the hands and feet, which first appear before puberty and subsequently expand to the proximal limb and the trunk"* ([PMID: 23666529](https://pubmed.ncbi.nlm.nih.gov/23666529/)); *"hyperpigmented macules or papules that may interrupt the dermatoglyphics with extra-dermatological manifestations"* ([PMID: 35978738](https://pubmed.ncbi.nlm.nih.gov/35978738/)). Bony anomalies (absent terminal phalanges of the 2nd–4th toes) were reported in a single case ([PMID: 8973039](https://pubmed.ncbi.nlm.nih.gov/8973039/)).

**Quality of life.** Impact is cosmetic/psychosocial rather than functional or life-threatening; no disease-specific QoL instrument data exist.

---

## 4. Genetic / Molecular Information

**Causal gene:** ADAM10 (chromosome 15q21.3), encoding a zinc-dependent transmembrane metalloprotease ("a disintegrin and metalloproteinase domain-containing protein 10").

**Pathogenic variants.** Reported RAK variants are predominantly **loss-of-function**: truncating (nonsense/frameshift), splice-site, and missense. In the defining study: *"We identified a total of three truncating mutations, a splice site mutation and a missense mutation in ADAM10"* ([PMID: 23666529](https://pubmed.ncbi.nlm.nih.gov/23666529/)). Additional novel ADAM10 mutations have since been reported in individual RAK cases, including functional-implication studies ([PMID: 29192958](https://pubmed.ncbi.nlm.nih.gov/29192958/); [PMID: 26892935](https://pubmed.ncbi.nlm.nih.gov/26892935/); [PMID: 30488468](https://pubmed.ncbi.nlm.nih.gov/30488468/)).

- **Variant classification:** pathogenic / likely pathogenic (ACMG), consistent with haploinsufficiency.
- **Variant type/class:** nonsense, frameshift (truncating), splice-site, missense.
- **Allele frequency:** private/family-specific; not common polymorphisms (ultra-rare).
- **Origin:** germline, autosomal dominant.
- **Functional consequence:** **loss of function / haploinsufficiency** (reduced functional ADAM10).

**Modifier genes / epigenetics / chromosomal abnormalities.** No validated modifiers, epigenetic marks, or chromosomal rearrangements are described for RAK.

**Spectrum context.** RAK is genetically distinct from Dowling-Degos disease, whose causal genes are KRT5, POFUT1, POGLUT1, PSENEN, and GLMN ([PMID: 40674458](https://pubmed.ncbi.nlm.nih.gov/40674458/)). POFUT1 and POGLUT1 glycosylate Notch, and PSENEN/NCSTN are γ-secretase subunits — all converging on Notch, as does ADAM10 ([PMID: 24387993](https://pubmed.ncbi.nlm.nih.gov/24387993/); [PMID: 37665193](https://pubmed.ncbi.nlm.nih.gov/37665193/)).

---

## 5. Environmental Information

No environmental factors, lifestyle factors, or infectious agents are implicated in RAK. It is a constitutive monogenic disorder. (ADAM10 is notably the cellular receptor exploited by *Staphylococcus aureus* α-toxin and participates in skin-microbiome regulation, but these are ADAM10 biology findings, not RAK triggers — [PMID: 30324336](https://pubmed.ncbi.nlm.nih.gov/30324336/); [PMID: 34582748](https://pubmed.ncbi.nlm.nih.gov/34582748/).)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A **heterozygous loss-of-function ADAM10 variant** (truncating, splice-site, or missense) **results in** reduced functional ADAM10 protein (haploinsufficiency). *[Demonstrated — human genetics, PMID 23666529]*
2. Reduced ADAM10 **leads to** decreased Site-2 ectodomain shedding of the Notch receptor in epidermal keratinocytes and melanocytes. *[Demonstrated in mouse epidermis; inferred for human RAK — PMID 21205794]*
3. Decreased Notch shedding **results in** less generation of the Notch intracellular domain (NICD) and **reduced Notch signaling**. *[Demonstrated — PMID 21205794]*
4. Reduced epidermal Notch signaling **leads to** dysregulated keratinocyte differentiation (epidermal atrophy, elongated rete ridges) **and, in parallel,** altered melanocyte/melanocyte-precursor homeostasis. *[Branch — keratinocyte arm demonstrated in mouse; melanocyte arm inferred — PMID 21205794, PMID 25705850]*
5. Melanocyte dysregulation **results in** an increased number of active (dopa-positive) basal melanocytes and **enhanced transfer of melanosomes** to surrounding keratinocytes. *[Demonstrated — human histology/ultrastructure, PMID 3994414]*
6. These cellular changes **manifest as** pre-pubertal, slowly progressive, bilateral acral **reticulate hyperpigmentation** with palmar pits and dermatoglyphic breaks. *[Demonstrated — clinical, PMID 23666529]*

```
ADAM10 LoF variant (germline, heterozygous)
        │  haploinsufficiency
        ▼
Reduced ADAM10 Site-2 sheddase activity
        │
        ▼
↓ Notch shedding → ↓ NICD → ↓ epidermal Notch signaling
        │
        ├──────────────┬───────────────────────────┐
        ▼              ▼                           ▼
Keratinocyte      Melanocyte / MC-precursor    Epidermal barrier/
differentiation   homeostasis dysregulated     adnexal changes
dysregulated      (↑ active basal              (modeled in mouse cKO)
(atrophy, long    melanocytes, ↑ melanosome
rete ridges)      transfer to keratinocytes)
        │              │
        └──────┬───────┘
               ▼
   Acral reticulate hyperpigmentation + palmar pits + dermatoglyphic breaks
```

### Supporting detail

- **Molecular pathway:** **Notch signaling** is the central axis. ADAM10 is *"the major Site-2 processing enzyme for Notch in the epidermis in vivo, and thus… a central regulator of skin development and maintenance,"* and in its absence *"Notch processing is indeed strongly reduced resulting in decreased levels of Notch intracellular domain fragment and functional Notch signaling"* ([PMID: 21205794](https://pubmed.ncbi.nlm.nih.gov/21205794/)). Suggested GO terms: **GO:0007219 (Notch signaling pathway)**, **GO:0006509 (membrane protein ectodomain proteolysis)**, **GO:0004222 (metalloendopeptidase activity)**.
- **Protein dysfunction:** ADAM10 is a promiscuous α-secretase/sheddase; *"ADAM10 was found to exert many additional functions, cleaving about 100 different membrane proteins"* ([PMID: 37218105](https://pubmed.ncbi.nlm.nih.gov/37218105/)). Among its ~100 substrates (Notch, E-/N-cadherin, APP, ephrins, cytokine receptors), Notch is the essential one whose loss is lethal: *"the even earlier fatal effects of ADAM10 deficiency exhibit key features of disabled Notch signalling and possibly also cadherin processing defects"* ([PMID: 18393804](https://pubmed.ncbi.nlm.nih.gov/18393804/)).
- **Cellular processes:** melanocyte survival/proliferation and melanosome transfer. *"Inhibition of Notch signaling reduced the proliferation of NCSC-like cells, induced cell death"* ([PMID: 25705850](https://pubmed.ncbi.nlm.nih.gov/25705850/)). The pigment mechanism is cell-biological: *"the hyperpigmentation of RAPK is due to increased number of active melanocytes and to increased transfer of melanosomes to surrounding keratinocytes"* ([PMID: 3994414](https://pubmed.ncbi.nlm.nih.gov/3994414/)).
- **Cell types (CL):** keratinocyte (**CL:0000312**), melanocyte (**CL:0000148**), epidermal/melanocyte stem cells.
- **Subcellular (GO cellular component):** melanosome (**GO:0042470**), plasma membrane (**GO:0005886**).

---

## 7. Anatomical Structures Affected

- **Organ:** skin (**UBERON:0002097**), the sole primary organ affected. No secondary systemic organ involvement in typical disease.
- **Body system:** integumentary system (**UBERON:0002416**).
- **Regional sites:** dorsum of hand (**UBERON:0003401**) and dorsum of foot (**UBERON:0003402**); palms and soles (palmar pits); later proximal limbs and trunk.
- **Tissue/cell:** epidermis (**UBERON:0001003**) — epithelial tissue; affected cells are **keratinocytes (CL:0000312)** and **melanocytes (CL:0000148)** at the basal layer; adnexal structures (hair follicles, sebaceous glands) are affected in the mouse model but not clinically prominent in human RAK.
- **Subcellular:** melanosome (GO:0042470).
- **Lateralization:** **bilateral and symmetric**, acrally accentuated.

Histology: *"epidermal atrophy, elongation of the rete ridges with large amounts of melanin, and an increased number of dopa-positive basal melanocytes"* ([PMID: 3994414](https://pubmed.ncbi.nlm.nih.gov/3994414/)).

---

## 8. Temporal Development

- **Onset:** pediatric, **before puberty**; insidious/chronic onset.
- **Progression:** slowly progressive — lesions begin acrally and extend proximally to limbs and trunk over years. No staging system; the disease is **chronic and lifelong**.
- **Course pattern:** progressive-then-stable hyperpigmentation; **no spontaneous remission**.
- **Critical period:** childhood/adolescence, when lesions emerge and spread.

*"…first appear before puberty and subsequently expand to the proximal limb and the trunk"* ([PMID: 23666529](https://pubmed.ncbi.nlm.nih.gov/23666529/)).

---

## 9. Inheritance and Population

- **Inheritance:** autosomal dominant, high penetrance; the RAK/DDD spectrum shows *"rare genodermatoses inherited as an autosomal dominant trait with variable penetrance"* ([PMID: 26955585](https://pubmed.ncbi.nlm.nih.gov/26955585/)).
- **Penetrance/expressivity:** high penetrance with variable expressivity (age of onset, extent of spread, rare skeletal associations).
- **Epidemiology:** extremely rare; **no formal prevalence/incidence figures** are established (ultra-rare). East Asian (Japanese, Chinese) predominance: *"Reticulate acropigmentation of Kitamura (RAK) predominantly affects East Asian populations, though isolated cases and familial occurrences have been reported globally"* ([PMID: 40950988](https://pubmed.ncbi.nlm.nih.gov/40950988/)); *"Japanese researchers Kitamura et al. first described this condition in 1943"* ([PMID: 40950988](https://pubmed.ncbi.nlm.nih.gov/40950988/)).
- **Anticipation, germline mosaicism, founder effects, consanguinity, carrier frequency:** not established/not applicable (dominant disorder; variants are private).
- **Sex ratio / age distribution:** no strong sex predilection reported; onset in childhood.

---

## 10. Diagnostics

**Clinical/histopathologic diagnosis + genetic confirmation.**

- **Dermoscopy & clinical signs:** reticulate, slightly depressed brown macules on dorsal hands/feet; pigmented palmar pits; dermatoglyphic breaks aid recognition ([PMID: 32055533](https://pubmed.ncbi.nlm.nih.gov/32055533/); [PMID: 32055524](https://pubmed.ncbi.nlm.nih.gov/32055524/); [PMID: 23746125](https://pubmed.ncbi.nlm.nih.gov/23746125/)).
- **Histopathology/IHC:** epidermal atrophy, elongated melanin-laden rete ridges, increased dopa-positive basal melanocytes; EM shows melanosome complexes in keratinocytes and melanosome-filled dendrites ([PMID: 3994414](https://pubmed.ncbi.nlm.nih.gov/3994414/)).
- **Genetic testing (definitive):** single-gene **ADAM10** sequencing or exome/panel testing. Because features overlap heavily across RPDs, *"each of these hereditary conditions possesses a unique genetic mutation, and genetic analysis is thus more useful in the diagnosis of these conditions"* ([PMID: 29201043](https://pubmed.ncbi.nlm.nih.gov/29201043/)); *"The overlapping features often add confusion and cause delay in diagnosis"* ([PMID: 39139099](https://pubmed.ncbi.nlm.nih.gov/39139099/)).

**Differential diagnosis (reticulate pigmentary disorders) with distinguishing genes:**

| Disorder | Gene | Distinguishing feature |
|---|---|---|
| Dowling-Degos disease | KRT5, POFUT1, POGLUT1, PSENEN, GLMN | Flexural distribution, comedo-like lesions |
| Dyschromatosis symmetrica hereditaria (DSH) | ADAR1 | Mixed hyper-/hypopigmented acral macules |
| Dyschromatosis universalis hereditaria (DUH) | ABCB6 | Generalized dyschromia |
| Naegeli-Franceschetti-Jadassohn / DPR | KRT14 | Absent dermatoglyphics, hypohidrosis |
| Dyskeratosis congenita | Telomere genes | Nail dystrophy, leukoplakia, BM failure |
| X-linked reticulate pigmentary disorder | POLA1 | X-linked, systemic |

(References: [PMID: 29201043](https://pubmed.ncbi.nlm.nih.gov/29201043/); [PMID: 37372478](https://pubmed.ncbi.nlm.nih.gov/37372478/); [PMID: 39139099](https://pubmed.ncbi.nlm.nih.gov/39139099/); [PMID: 30692041](https://pubmed.ncbi.nlm.nih.gov/30692041/).)

**Screening:** no newborn/population screening; cascade genetic testing within families is possible once a pathogenic ADAM10 variant is known.

---

## 11. Outcome / Prognosis

RAK is **benign** with a **normal life expectancy** and no disease-specific mortality. Morbidity is **cosmetic/psychosocial** only. The hyperpigmentation is chronic, lifelong, and slowly progressive without spontaneous remission. No validated prognostic biomarkers are needed, as the disease does not threaten survival or organ function. *"all three having limited treatment options"* characterizes the therapeutic outlook for RAK and overlapping RPDs ([PMID: 38646262](https://pubmed.ncbi.nlm.nih.gov/38646262/)).

---

## 12. Treatment

**No curative or disease-modifying therapy exists.** Management is cosmetic and often disappointing:

- **Topical:** retinoids (adapalene), hydroquinone — inconsistent results. In clinically overlapping DDD, *"The patient was unsuccessfully treated with adapalene gel and refused the recommended oral retinoid therapy, as well as laser therapy"* ([PMID: 36919394](https://pubmed.ncbi.nlm.nih.gov/36919394/)).
- **Systemic:** oral retinoids — generally unsuccessful.
- **Device:** laser (e.g., Er:YAG, Q-switched) — reported effective only in isolated cases.
- **Supportive:** photoprotection, cosmetic camouflage, psychosocial support.

No pharmacogenomic, gene, cell, RNA, or targeted therapies are approved or in trials for RAK. Suggested NCIT concepts: retinoid therapy (NCIT:C1909 class), laser therapy (NCIT:C15193). *"all three having limited treatment options"* is explicitly documented ([PMID: 38646262](https://pubmed.ncbi.nlm.nih.gov/38646262/)).

---

## 13. Prevention

No primary prevention is possible for a constitutive genetic disorder. **Genetic counseling** is the principal preventive tool: autosomal dominant inheritance implies a 50% transmission risk to offspring. Once a family's pathogenic ADAM10 variant is identified, **cascade testing, prenatal testing, or preimplantation genetic diagnosis** are theoretically available but rarely pursued given the benign nature of the disease. No immunization, behavioral, or public-health interventions apply.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** ADAM10 is highly evolutionarily conserved — mouse *Adam10* (NCBI Gene 11487), zebrafish *adam10a/adam10b*. Human ADAM10 is NCBI Gene 102.
- **Natural disease:** **No naturally occurring reticulate acropigmentation has been reported in companion animals or wildlife** (OMIA lists no RAK entry).
- **Comparative biology:** The ADAM10→Notch axis is deeply conserved, so mechanistic conclusions from mouse apply broadly; however, the specific human pigmentary phenotype has no documented animal counterpart.
- **Transmission:** not applicable (non-infectious, non-zoonotic).

---

## 15. Model Organisms

| Model | Type | Phenotype | Relevance |
|---|---|---|---|
| Epidermal (K14-Cre) *Adam10* cKO mouse | Conditional knockout | Perinatal lethality, barrier impairment, absent sebaceous glands, reduced spinous layer, hair loss, cysts, reduced Notch processing | Key model; recapitulates epidermal Notch LoF ([PMID: 21205794](https://pubmed.ncbi.nlm.nih.gov/21205794/)) |
| Global *Adam10* KO mouse | Constitutive knockout | Embryonic lethal (Notch failure, cadherin defects) | Demonstrates Notch as essential substrate ([PMID: 26522965](https://pubmed.ncbi.nlm.nih.gov/26522965/); [PMID: 18393804](https://pubmed.ncbi.nlm.nih.gov/18393804/)) |
| dsRNA-induced *Adam10* ablation (upper HF) | Induced | Skin dysbiosis, ILC2-mediated hair-follicle destruction | Models ADAM10-Notch–microbiome axis ([PMID: 34582748](https://pubmed.ncbi.nlm.nih.gov/34582748/)) |

*"K14-Cre driven epidermal Adam10 deletion leads to perinatal lethality, barrier impairment and absence of sebaceous glands"* ([PMID: 21205794](https://pubmed.ncbi.nlm.nih.gov/21205794/)).

**Limitations of models:** mouse epidermal knockouts are far more severe (lethal, barrier failure) than the mild human haploinsufficiency; crucially, **no model reproduces the specific human acral reticulate hyperpigmentation**, so models inform the ADAM10→Notch mechanism but not the pigmentary phenotype directly. No zebrafish/Drosophila/iPSC/organoid RAK-specific model is established.

---

## Key Findings (with evidence)

1. **ADAM10 loss-of-function causes RAK.** WES of a RAK pedigree + Sanger of 4 unrelated patients found 5 heterozygous ADAM10 mutations (3 truncating, 1 splice, 1 missense); no KRT5 mutations — RAK is distinct from DDD ([PMID: 23666529](https://pubmed.ncbi.nlm.nih.gov/23666529/)).
2. **ADAM10 is the principal epidermal Site-2 Notch sheddase;** its loss reduces NICD and Notch signaling and reproduces Notch-LoF skin phenotypes in mice ([PMID: 21205794](https://pubmed.ncbi.nlm.nih.gov/21205794/)).
3. **RAK belongs to a Notch-pathway reticulate pigmentary spectrum** overlapping DDD (KRT5, POFUT1, POGLUT1, PSENEN, GLMN) — all Notch processing/glycosylation genes ([PMID: 40674458](https://pubmed.ncbi.nlm.nih.gov/40674458/); [PMID: 24387993](https://pubmed.ncbi.nlm.nih.gov/24387993/); [PMID: 37665193](https://pubmed.ncbi.nlm.nih.gov/37665193/)).
4. **Histopathology:** epidermal atrophy, elongated melanin-laden rete ridges, increased active basal melanocytes, enhanced melanosome transfer ([PMID: 3994414](https://pubmed.ncbi.nlm.nih.gov/3994414/)).
5. **Clinical phenotype:** pre-pubertal acral reticulate hyperpigmentation with dermatoglyphic breaks, palmar pits, rare skeletal anomalies ([PMID: 23666529](https://pubmed.ncbi.nlm.nih.gov/23666529/); [PMID: 35978738](https://pubmed.ncbi.nlm.nih.gov/35978738/); [PMID: 8973039](https://pubmed.ncbi.nlm.nih.gov/8973039/)).
6. **ADAM10 is a promiscuous sheddase (~100 substrates);** Notch is the essential one whose loss is embryonic-lethal ([PMID: 37218105](https://pubmed.ncbi.nlm.nih.gov/37218105/); [PMID: 18393804](https://pubmed.ncbi.nlm.nih.gov/18393804/)).
7. **Epidemiology:** extremely rare, East-Asian predominant, AD with variable penetrance/expressivity ([PMID: 40950988](https://pubmed.ncbi.nlm.nih.gov/40950988/); [PMID: 26955585](https://pubmed.ncbi.nlm.nih.gov/26955585/)).
8. **Diagnosis** rests on clinical-dermoscopic-histologic correlation + ADAM10 genetic confirmation ([PMID: 29201043](https://pubmed.ncbi.nlm.nih.gov/29201043/); [PMID: 39139099](https://pubmed.ncbi.nlm.nih.gov/39139099/)).
9. **Notch regulates melanocyte/MC-stem-cell homeostasis,** linking ADAM10 loss to altered pigmentation ([PMID: 25705850](https://pubmed.ncbi.nlm.nih.gov/25705850/)).
10. **Benign, chronic, limited-therapy disorder** ([PMID: 38646262](https://pubmed.ncbi.nlm.nih.gov/38646262/); [PMID: 36919394](https://pubmed.ncbi.nlm.nih.gov/36919394/)).
11. **Mouse epidermal *Adam10* cKO is the key model;** no natural animal RAK ([PMID: 21205794](https://pubmed.ncbi.nlm.nih.gov/21205794/); [PMID: 26522965](https://pubmed.ncbi.nlm.nih.gov/26522965/)).
12. **Integrated causal model:** ADAM10 haploinsufficiency → ↓ epidermal Notch → keratinocyte/melanocyte dysregulation → acral reticulate hyperpigmentation ([PMID: 23666529](https://pubmed.ncbi.nlm.nih.gov/23666529/); [PMID: 21205794](https://pubmed.ncbi.nlm.nih.gov/21205794/); [PMID: 3994414](https://pubmed.ncbi.nlm.nih.gov/3994414/)).

---

## Mechanistic Model / Interpretation

The twelve findings converge on a single, coherent causal narrative. RAK begins with a germline heterozygous ADAM10 loss-of-function allele. Because ADAM10 is the dominant Site-2 sheddase that activates Notch in the epidermis, halving its dose is sufficient to reduce Notch intracellular-domain generation and downstream Notch signaling. Notch is a master regulator of both keratinocyte differentiation and melanocyte homeostasis, so its attenuation branches into two coupled effects: aberrant keratinocyte differentiation (seen histologically as epidermal atrophy and elongated, melanin-laden rete ridges) and increased activity of basal melanocytes with enhanced melanosome transfer to keratinocytes. The net clinical readout is the slightly depressed, reticulate, acral hyperpigmentation with palmar pits and dermatoglyphic breaks. Critically, the same Notch axis — accessed through glycosylation (POFUT1, POGLUT1) or γ-secretase (PSENEN, NCSTN) — unifies the clinically overlapping Dowling-Degos spectrum, explaining why these disorders share reticulate pigmentation yet are genetically distinct.

The chain is firmly anchored at its endpoints (human genetics at the top; human histology and clinical phenotype at the bottom) but relies on mouse/in-vitro evidence for its middle steps (the quantitative reduction in Notch signaling and the keratinocyte/melanocyte response). This is the principal interpretive caveat: the Notch-reduction step is demonstrated in mouse epidermis and inferred, not directly measured, in human RAK skin.

---

## Evidence Base

| PMID | Role |
|---|---|
| [23666529](https://pubmed.ncbi.nlm.nih.gov/23666529/) | Defining genetics — ADAM10 mutations cause RAK; distinct from DDD |
| [21205794](https://pubmed.ncbi.nlm.nih.gov/21205794/) | Mechanism — ADAM10 is epidermal Site-2 Notch sheddase; mouse cKO |
| [3994414](https://pubmed.ncbi.nlm.nih.gov/3994414/) | Histology/ultrastructure — melanocyte behavior in RAK |
| [37218105](https://pubmed.ncbi.nlm.nih.gov/37218105/) | ADAM10 substrate breadth (~100) and pathophysiology |
| [18393804](https://pubmed.ncbi.nlm.nih.gov/18393804/) | Notch as essential ADAM10 substrate (lethality) |
| [25705850](https://pubmed.ncbi.nlm.nih.gov/25705850/) | Notch controls melanocyte-precursor fate/survival |
| [40674458](https://pubmed.ncbi.nlm.nih.gov/40674458/) | DDD spectrum genes (Notch pathway) |
| [24387993](https://pubmed.ncbi.nlm.nih.gov/24387993/) | POGLUT1/POFUT1 — Notch glycosylation in DDD |
| [37665193](https://pubmed.ncbi.nlm.nih.gov/37665193/) | NCSTN/PSENEN — γ-secretase in DDD spectrum |
| [30692041](https://pubmed.ncbi.nlm.nih.gov/30692041/) | Review of DSH and RAK, Notch hypothesis |
| [37372478](https://pubmed.ncbi.nlm.nih.gov/37372478/) | Inherited RPD review, East-Asian predominance |
| [29201043](https://pubmed.ncbi.nlm.nih.gov/29201043/) | Genetic testing as definitive diagnostic |
| [39139099](https://pubmed.ncbi.nlm.nih.gov/39139099/) | Algorithmic diagnostic approach |
| [40950988](https://pubmed.ncbi.nlm.nih.gov/40950988/) | Epidemiology, 1943 first description |
| [38646262](https://pubmed.ncbi.nlm.nih.gov/38646262/) | Limited treatment options |
| [34582748](https://pubmed.ncbi.nlm.nih.gov/34582748/) | ADAM10-Notch–microbiome axis (hair follicle) |
| [26522965](https://pubmed.ncbi.nlm.nih.gov/26522965/) | ADAM10 biology; global KO embryonic lethal |
| [36919394](https://pubmed.ncbi.nlm.nih.gov/36919394/) | DDD treatment refractoriness (overlapping disorder) |
| [35978738](https://pubmed.ncbi.nlm.nih.gov/35978738/) / [8973039](https://pubmed.ncbi.nlm.nih.gov/8973039/) | Rare extradermatological (skeletal) associations |

**Evidence source types:** human clinical genetics and histopathology (23666529, 3994414, 35978738, 8973039); mouse model (21205794, 34582748, 26522965); in vitro / mechanistic (25705850, 37218105, 18393804); reviews (30692041, 37372478, 40674458).

---

## Limitations and Knowledge Gaps

- **No direct human tissue proof** that NICD/Notch signaling is reduced in RAK epidermis — the Notch-reduction step is inferred from the mouse model, not demonstrated in patient skin.
- **Genotype–phenotype correlation is unknown:** why haploinsufficiency produces a *pigmentary, acral* phenotype in humans while the mouse epidermal null is lethal and barrier-focused is unexplained. The mild human phenotype vs. severe mouse phenotype gap limits model translation.
- **No formal epidemiology** (prevalence/incidence) exists; estimates are impressionistic.
- **Melanocyte-arm mechanism is partly inferred:** the link from reduced keratinocyte/melanocyte Notch to "increased active melanocytes + melanosome transfer" is supported by histology (3994414) and Notch-melanocyte biology (25705850) but not by a RAK-specific functional melanocyte study.
- **No modifier genes, epigenetic data, or therapeutics** have been systematically investigated.

---

## Proposed Follow-up Experiments / Actions

1. **Patient-skin Notch readout:** quantify NICD, HES1/HEY1, and ADAM10 protein in RAK lesional vs. non-lesional epidermis to directly test steps 2–3 of the causal chain.
2. **RAK-relevant model:** generate a *melanocyte-specific or inducible heterozygous* Adam10 mouse (or a human iPSC-derived keratinocyte–melanocyte co-culture / skin organoid carrying a patient ADAM10 LoF variant) to reproduce the pigmentary phenotype at physiologic haploinsufficiency.
3. **Melanocyte functional assays:** measure melanocyte activation (dopa positivity, tyrosinase), dendricity, and melanosome transfer under ADAM10 knockdown/Notch inhibition.
4. **Genotype–phenotype registry:** aggregate ADAM10 variants with age of onset, extent of spread, and rare skeletal/gingival features to define expressivity drivers.
5. **Therapeutic exploration:** test whether topical Notch-pathway modulators or targeted melanogenesis inhibitors improve pigmentation in controlled series, given the current therapeutic void.

---

*Report compiled from a 5-iteration autonomous investigation; 12 confirmed findings; 44 papers reviewed.*


## Artifacts

- [OpenScientist final report](Reticulate_Acropigmentation_Of_Kitamura-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Reticulate_Acropigmentation_Of_Kitamura-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 28 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 22 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 11 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014234` (2 mentions) - the report calls it "MONDO"; MONDO calls it **reticulate acropigmentation of Kitamura**
- `HP:0007441` (1 mention) - the report calls it "Reticulated skin pigmentation"; HP calls it **Hyperpigmented/hypopigmented macules**
- `HP:0000212` (1 mention) - the report calls it "Rare (single report)"; HP calls it **Gingival overgrowth**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `UBERON:0003401` (1 mention) - UBERON does not contain this term
- `UBERON:0003402` (1 mention) - UBERON does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0042470` (2 mentions) - the report calls it "Subcellular:** melanosome"; GO calls it **melanosome**