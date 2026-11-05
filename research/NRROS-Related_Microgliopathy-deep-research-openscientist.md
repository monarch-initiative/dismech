---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-04T18:53:27.189089'
end_time: '2026-11-04T19:10:27.491994'
duration_seconds: 1020.3
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: NRROS-Related Microgliopathy
  mondo_id: MONDO:0030033
  category: Mendelian
  causal_genes: NRROS
  omim_id: OMIM:618875
  synonyms: seizures, early-onset, with neurodegeneration and brain calcification;
    SENEBAC
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
citation_count: 11
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 4
  validator_version: 0.5.1
term_validation:
  total_terms: 26
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 2
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0030033
    reported_labels:
    - MONDO
    ontology_label: seizures, early-onset, with neurodegeneration and brain calcifications
  - term_id: HP:0002376
    reported_labels:
    - Median ~12 mo
    ontology_label: Developmental regression
  - term_id: HP:0002059
    reported_labels:
    - Progressive
    ontology_label: Cerebral atrophy
  labels_variant: 4
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
  path: NRROS-Related_Microgliopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: NRROS-Related_Microgliopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** NRROS-Related Microgliopathy
- **MONDO ID:** MONDO:0030033 (if available)
- **Causal gene(s):** NRROS
- **OMIM:** OMIM:618875
- **Synonyms:** seizures, early-onset, with neurodegeneration and brain calcification; SENEBAC
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **NRROS-Related Microgliopathy** covering all of the
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

# NRROS-Related Microgliopathy (SENEBAC): Comprehensive Disease Characterization

**Disease:** NRROS-Related Microgliopathy — *Seizures, Early-onset, with Neurodegeneration And Brain Calcification* (SENEBAC)
**Causal gene:** **NRROS** (Negative Regulator of Reactive Oxygen Species; also known as *LRRC33*; HGNC:25124; NCBI Gene 375387; UniProt Q86YC3; cytoband 3q29)
**Identifiers:** MONDO:0030033 · OMIM:618875
**Category:** Mendelian, autosomal recessive, ultra-rare

> **Causal gene stated up front:** This disorder is caused by **biallelic loss-of-function variants in the NRROS gene** (also called **LRRC33**). The OMIM phenotype title ("Seizures, early-onset, with neurodegeneration and brain calcification"; SENEBAC) is descriptive and does not name a gene, but all identifiers above (MONDO:0030033, OMIM:618875) point to the same NRROS-related entity.

---

## Summary

NRROS-Related Microgliopathy is an ultra-rare, autosomal-recessive, infantile-onset, progressive and usually lethal neurodegenerative disorder caused by **biallelic loss-of-function (LoF) variants in the NRROS gene** (also called *LRRC33*). NRROS is a microglial/macrophage transmembrane "milieu" protein whose principal function is to anchor latent transforming growth factor-β1 (TGF-β1) at the cell surface, where it enables highly localized, integrin-αVβ8-dependent activation of the cytokine. A second, distinct function of NRROS is to serve as an endoplasmic-reticulum-based negative regulator of the NADPH oxidase subunit NOX2, restraining reactive oxygen species (ROS) production.

The disease mechanism follows a coherent causal chain: biallelic NRROS LoF variants produce absent or non-functional protein that fails to anchor latent TGF-β1 at the microglial surface; this abolishes local integrin-αVβ8-dependent TGF-β1 activation, depriving microglia of the autocrine/paracrine TGF-β1 signal required for their homeostatic maturation program. The resulting microglial dysfunction — compounded by a loss of NOX2 restraint that permits excess oxidative damage — produces a calcifying leukoencephalopathy with combined grey- and white-matter degeneration, foamy macrophage infiltration, and dystrophic intracranial calcification. Clinically, affected children typically develop normally for several months, then present with drug-resistant epilepsy, developmental regression, acquired microcephaly, and relentless neurodegeneration, with a median age at death of approximately 3 years.

Fewer than ~15 individuals have been reported worldwide. Diagnosis is molecular (exome or genome sequencing) supported by a characteristic neuroimaging signature of progressive cerebral atrophy, white-matter volume loss/delayed myelination, and punctate or serpiginous calcifications at the grey-white matter junction. There is no disease-modifying therapy; management is entirely supportive and palliative, with genetic counseling as the only means of prevention. The Nrros-knockout mouse and the Lrrc33-deficient mouse faithfully recapitulate key features, and human biallelic TGFB1 deficiency causes a convergent encephalopathy, together validating the mechanistic model.

---

## Section 1 — Disease Information

**Overview.** NRROS-Related Microgliopathy (SENEBAC) is a Mendelian, infantile-onset neurodegenerative disease characterized by the triad of early-onset drug-resistant seizures, progressive neurodegeneration with developmental regression, and intracranial (brain) calcification. It is a disorder of microglial dysfunction (a "microgliopathy") driven by failure of localized TGF-β1 activation in the central nervous system.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0030033 |
| OMIM (phenotype) | 618875 (SENEBAC) |
| Gene | NRROS / LRRC33 — HGNC:25124; NCBI Gene 375387; Ensembl ENSG00000174004; UniProt Q86YC3 |
| Cytoband | 3q29 |
| ICD-10 / ICD-11 / MeSH / Orphanet | No NRROS-specific code (ultra-rare; not separately coded) |

**Synonyms / alternative names.** Seizures, early-onset, with neurodegeneration and brain calcification; SENEBAC; NRROS-related microgliopathy; NRROS-related lethal microgliopathy.

**Information source.** The knowledge base for this disease is derived from aggregated, disease-level primary literature — small case series and systematic case-based reviews of individual patients identified via research exome/genome sequencing — rather than from large EHR-based or registry cohorts. This reflects the extreme rarity of the condition.

---

## Section 2 — Etiology

**Primary cause (genetic).** The disease is caused exclusively by **biallelic (autosomal-recessive) loss-of-function variants in NRROS**. Dong et al. (2020) reported six individuals from four families with bi-allelic NRROS variants ([PMID: 32197075](https://pubmed.ncbi.nlm.nih.gov/32197075/)): *"We report six individuals from four families with bi-allelic variants in NRROS."* Subsequent reports (Macintosh 2022; Madaan 2022) expanded the cohort to ~15 individuals.

**Genetic risk factors.** The only established risk factor is inheritance of two LoF NRROS alleles. Variant classes include nonsense, frameshift, splice-site, and damaging missense variants affecting two functional NRROS domains. A **recurrent c.1981delC (p.Leu661Serfs*97)** frameshift was observed in two families, attributed to a likely founder effect ([PMID: 35716448](https://pubmed.ncbi.nlm.nih.gov/35716448/)): *"The most common reported genetic variation was c.1981delC; (p.Leu661Serfs*97) observed in two families (likely due to a founder effect)."* Other reported variants include c.185T>C (p.Leu62Pro), c.310C>T (p.Gln104Ter), and c.1359del (p.Ser454Alafs*11). Consanguinity contributes to recessive inheritance in some families.

**Environmental risk factors.** None identified. This is a monogenic disorder; no toxic, infectious, lifestyle, or occupational contributor has been described.

**Protective factors.** None identified (genetic or environmental). No protective modifier alleles have been reported.

**Gene–environment interactions.** None established. Given the fully penetrant monogenic etiology, the disease is not known to depend on environmental modifiers.

---

## Section 3 — Phenotypes

Phenotypes derive principally from the Madaan 2022 systematic review (n=11 children, 6 girls), Dong 2020, and Macintosh 2022.

| Phenotype | Type | Frequency | Onset / course | HPO term |
|---|---|---|---|---|
| Drug-resistant epilepsy | Clinical sign | 11/11 (100%) | Median onset ~12 mo; refractory, progressive | HP:0032794 (and HP:0001250 Seizure) |
| Epileptic/infantile spasms | Clinical sign | 3/11 | Infantile | HP:0012469 |
| Developmental regression | Symptom | Majority (normal early development in 7/11, then regression) | Median ~12 mo | HP:0002376 |
| Progressive cerebral atrophy | Imaging/structural | All | Progressive | HP:0002059 |
| Cerebral white-matter abnormality / loss | Imaging/structural | All | Progressive; delayed myelination | HP:0002500; HP:0012448 (Delayed CNS myelination) |
| Intracranial calcification | Imaging/structural | 8/11 | Punctate/serpiginous at grey-white junction | HP:0002514 (Cerebral calcification) |
| Acquired (secondary) microcephaly | Physical sign | Reported | Acquired, progressive | HP:0005484 |

**Phenotype characteristics.** Onset is typically **infantile** (early development normal in 7/11 before seizure onset and regression at a median of 12 months). Severity is **severe**; course is **progressive** and usually fatal. Madaan 2022 quantified the natural history ([PMID: 35716448](https://pubmed.ncbi.nlm.nih.gov/35716448/)): *"The median age at seizure onset and developmental regression was 12 months, and the median age at death was 36 months. Intracranial calcifications were described in eight of eleven children."*

Macintosh 2022 documented the neuropathology ([PMID: 35099671](https://pubmed.ncbi.nlm.nih.gov/35099671/)): *"Pathological examination revealed both extensive grey and white matter involvement, dystrophic calcifications, and infiltration of foamy macrophages."*

**Quality-of-life impact.** Profound. Affected children experience refractory seizures, loss of acquired motor and cognitive milestones, acquired microcephaly, and progressive neurological disability leading to early death; impact on daily functioning is total, requiring full caregiving support. No formal EQ-5D/SF-36 QoL instrument data exist for this ultra-rare disease.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** NRROS / LRRC33 (HGNC:25124; NCBI Gene 375387; Ensembl ENSG00000174004; UniProt Q86YC3), on chromosome 3q29. Associated OMIM phenotype 618875.

**Pathogenic variants.**
- **Classification:** Reported variants are pathogenic/likely pathogenic LoF (ACMG/AMP); some damaging missense variants affect conserved functional domains.
- **Variant types:** Nonsense (e.g., c.310C>T, p.Gln104Ter), frameshift (c.1981delC p.Leu661Serfs*97; c.1359del p.Ser454Alafs*11), splice-site, and missense (c.185T>C, p.Leu62Pro).
- **Allele frequency:** All reported pathogenic variants are extremely rare/absent in population databases (gnomAD), consistent with a severe recessive phenotype.
- **Origin:** Germline, biallelic (autosomal recessive).
- **Functional consequence:** Loss of function. Functional studies showed mutant NRROS proteins co-localize intracellularly with latent TGF-β1 but fail to anchor it at the cell surface ([PMID: 32197075](https://pubmed.ncbi.nlm.nih.gov/32197075/)): *"these variants result in aberrant NRROS proteins with impaired ability to anchor latent TGF-β1 on the cell surface."*

**Modifier genes.** None established. The recurrent founder variant suggests population-specific recurrence rather than modifier effects.

**Epigenetic information (gene regulation).** NRROS/LRRC33 expression is epigenetically modulated: TLR ligands down-regulate LRRC33 via H3K4me3 and H3K27me3 chromatin modifications ([PMID: 24550525](https://pubmed.ncbi.nlm.nih.gov/24550525/)). This pertains to normal gene regulation rather than a disease-specific epimutation.

**Chromosomal abnormalities.** None reported; the disease results from point/small indel variants, not large structural rearrangements.

---

## Section 5 — Environmental Information

No environmental, lifestyle, or infectious contributors are implicated in NRROS-Related Microgliopathy. The disease is monogenic and recessive. Of mechanistic note, NRROS's normal physiology intersects with host defense — NRROS-deficient phagocytes show enhanced bactericidal activity against *E. coli* and *Listeria* due to increased ROS ([PMID: 24739962](https://pubmed.ncbi.nlm.nih.gov/24739962/)) — but no infectious trigger is required for or associated with the human neurodegenerative disease.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic NRROS LoF variants** → absent or non-functional NRROS/LRRC33 protein (*loss of function; demonstrated*).
2. → **Failure to anchor latent proTGF-β1 at the microglial/macrophage cell surface** (*demonstrated by flow cytometry; Dong 2020*). Mutant protein co-localizes with latent TGF-β1 intracellularly but is not displayed at the surface.
3. → **Loss of integrin-αVβ8-dependent local activation of TGF-β1** (*demonstrated in Lrrc33/NRROS biology; Qin 2018*).
4. → **Deficient autocrine/paracrine TGF-β1 signaling** that normally maintains the microglial homeostatic/maturation program → **microglial dysmaturation and dysfunction** (*inferred from mouse convergence with TGF-β1 deficiency*).
5. → **(Branch) Loss of NOX2 restraint** permits excess phagocyte ROS and oxidative CNS tissue damage (*inferred contribution from Noubade 2014 NRROS-NOX2 biology*).
6. → **Neuroinflammation, foamy macrophage infiltration, dysmyelination / white-matter loss, grey-matter degeneration, and dystrophic calcification** (*demonstrated neuropathology; Macintosh 2022*).
7. → **Clinical disease:** infantile drug-resistant epilepsy, developmental regression, acquired microcephaly, progressive neurodegeneration, and early death (median ~36 months).

```
NRROS biallelic LoF
        │
        ▼
No surface anchoring of latent TGF-β1 ───────────┐
        │                                         │ (branch)
        ▼                                         ▼
Loss of integrin-αVβ8 activation of TGF-β1   Loss of NOX2 restraint
        │                                         │
        ▼                                         ▼
Deficient microglial TGF-β1 signaling      Excess phagocyte ROS
        │                                         │
        └──────────────┬──────────────────────────┘
                       ▼
     Microglial dysfunction + oxidative CNS damage
                       ▼
 Leukoencephalopathy: dysmyelination, grey+white matter
 degeneration, foamy macrophages, dystrophic calcification
                       ▼
 Drug-resistant epilepsy, regression, microcephaly,
 progressive neurodegeneration, early death (~3 yr)
```

### Mechanistic detail

**Molecular pathway — TGF-β1 activation.** NRROS/LRRC33 is a transmembrane leucine-rich-repeat "milieu molecule" that covalently links proTGF-β1 and presents it on the microglial surface for localized, integrin-αVβ8-dependent activation ([PMID: 29909984](https://pubmed.ncbi.nlm.nih.gov/29909984/)): *"LRRC33 on the surface of microglia functions as a milieu molecule and enables highly localized, integrin-αVβ8-dependent TGF-β activation."* The structural basis for LRRC33's specificity for TGF-β1 and its integrin recognition was resolved by Duan et al. 2022 ([PMID: 36008481](https://pubmed.ncbi.nlm.nih.gov/36008481/)). GO term: **GO:0007179** (TGF-β receptor signaling pathway).

**Second function — NOX2 / ROS regulation.** NRROS was originally defined (Noubade et al. 2014, *Nature*) as an ER-resident negative regulator of NOX2 ([PMID: 24739962](https://pubmed.ncbi.nlm.nih.gov/24739962/)): *"NRROS is localized to the endoplasmic reticulum, where it directly interacts with nascent NOX2 (also known as gp91(phox) and encoded by Cybb) monomer ... and facilitates the degradation of NOX2 through the endoplasmic-reticulum-associated degradation pathway."* NRROS-deficient phagocytes produce increased ROS and NRROS-deficient mice develop severe EAE from CNS oxidative damage, supporting an oxidative-injury branch (GO:2000377, regulation of ROS metabolic process; CHEBI:26523, reactive oxygen species).

**Cellular processes.** Microglial cell activation/maturation (GO:0001774), myelination (GO:0042552), neuroinflammation, and dystrophic calcification. **Cell types:** microglia (CL:0000129) and CNS/perivascular macrophages (CL:0000881).

**Protein dysfunction.** Loss of function via truncation or destabilizing missense; retained intracellular latent-TGF-β1 binding but lost surface display and activation.

**Immune system involvement.** NRROS/LRRC33 is also a negative regulator of multiple Toll-like receptors and NF-κB signaling ([PMID: 23545260](https://pubmed.ncbi.nlm.nih.gov/23545260/); [PMID: 24550525](https://pubmed.ncbi.nlm.nih.gov/24550525/)). Dysregulated innate-immune/microglial homeostasis is central to the CNS pathology.

**Subcellular components.** Plasma membrane (GO:0005886, TGF-β1 presentation), ER (GO:0005783, NOX2 regulation), and mitochondrion (GO:0005739; mitochondrial ultrastructural abnormalities seen on EM, Macintosh 2022).

---

## Section 7 — Anatomical Structures Affected

- **Organ / system:** Central nervous system (brain) — the nervous system is the primary and essentially exclusive system affected. UBERON:0000955 (brain).
- **Tissue level:** Both grey matter (UBERON:0000956, cerebral cortex) and white matter (UBERON:0003544, cerebral white matter) are affected — "extensive grey and white matter involvement" (Macintosh 2022).
- **Cell populations:** Microglia (CL:0000129) and infiltrating foamy macrophages (CL:0000881) are the key cellular players.
- **Subcellular:** Plasma membrane (GO:0005886), endoplasmic reticulum (GO:0005783), mitochondria (GO:0005739).
- **Localization / lateralization:** Diffuse and bilateral; calcifications are typically located at the grey-white matter junction (punctate/serpiginous).

---

## Section 8 — Temporal Development

- **Onset:** Infantile. Early development is often normal (7/11 children), followed by seizure onset and developmental regression at a **median of ~12 months**. Onset pattern is subacute-to-chronic with regression.
- **Progression:** Relentlessly progressive — progressive cerebral atrophy, white-matter loss, and acquired microcephaly. No remission.
- **Disease course:** Progressive neurodegenerative; **median age at death ~36 months** (Madaan 2022).
- **Critical period:** The first 1–3 years of life represent the window of clinical manifestation; by extension, any disease-modifying intervention (hypothetical) would need to act very early, likely before irreversible neurodegeneration.

---

## Section 9 — Inheritance and Population

- **Inheritance:** Autosomal recessive (biallelic NRROS LoF). Consanguinity reported; recurrent founder variant c.1981delC in two families.
- **Penetrance / expressivity:** Apparently complete penetrance in reported biallelic LoF individuals; the phenotype is consistently severe, though age at death varies.
- **Epidemiology:** Ultra-rare. Fewer than ~15 individuals reported worldwide; no formal prevalence/incidence estimate exists (Orphanet-level ultra-rare, <1/1,000,000).
- **Founder effect:** Yes — the recurrent c.1981delC (p.Leu661Serfs*97) frameshift.
- **Carrier frequency:** Not established; pathogenic alleles are extremely rare in gnomAD.
- **Sex ratio:** No strong skew reported (6 girls among 11 in Madaan 2022); consistent with autosomal-recessive inheritance.
- **Geographic distribution:** Scattered case reports; no defined endemic region.

---

## Section 10 — Diagnostics

**Primary diagnostic route — molecular.** Diagnosis is established by identifying biallelic NRROS variants via **whole-exome sequencing (WES)** or **whole-genome sequencing (WGS)**; all reported families were ascertained by exome sequencing ([PMID: 32197075](https://pubmed.ncbi.nlm.nih.gov/32197075/)). Single-gene NRROS testing and epilepsy/leukodystrophy/neurodegeneration gene panels are appropriate when the phenotype is recognized. Chromosomal microarray and karyotyping are not informative (no structural abnormality).

**Neuroimaging.** Characteristic and diagnostically useful:
- Progressive cerebral atrophy and cerebral white-matter volume loss / delayed myelination.
- **Punctate or serpiginous calcifications at the grey-white matter junction** (CT is most sensitive for calcification). Madaan 2022: *"Punctate or serpiginous calcifications at the grey-white matter junction and acquired microcephaly are further c[haracteristic features]"* ([PMID: 35716448](https://pubmed.ncbi.nlm.nih.gov/35716448/)).

**Neuropathology (where available).** Extensive grey + white matter degeneration, dystrophic calcification, foamy macrophage infiltration, and mitochondrial ultrastructural abnormalities on EM (Macintosh 2022).

**Electrophysiology.** EEG demonstrates epileptiform/epileptic-encephalopathy patterns consistent with drug-resistant epilepsy and infantile/epileptic spasms.

**Biomarkers.** No disease-specific blood or CSF biomarker is established; diagnosis is molecular.

**Differential diagnosis.** Other infantile leukoencephalopathies with intracranial calcification — notably Aicardi-Goutières syndrome, cerebroretinal microangiopathy with calcifications and cysts (CRMCC/CTC1-related; [PMID: 28072696](https://pubmed.ncbi.nlm.nih.gov/28072696/)), congenital (TORCH) infections, Coats plus, and other microgliopathies/leukodystrophies. NRROS testing distinguishes this entity.

**Screening.** Carrier screening and cascade testing of at-risk relatives once a familial variant is known; prenatal/preimplantation testing is feasible for known biallelic variants.

---

## Section 11 — Outcome / Prognosis

- **Survival / life expectancy:** Poor. Median age at death ~36 months (Madaan 2022). The disease is usually lethal in early childhood.
- **Mortality:** Disease-specific; death results from progressive neurodegeneration and its complications (refractory seizures, respiratory/nutritional failure).
- **Morbidity / disability:** Profound and universal — loss of developmental milestones, refractory epilepsy, acquired microcephaly, and severe neurological disability.
- **Disease course / complications:** Relentlessly progressive; complications include status epilepticus, aspiration, feeding difficulty, and respiratory compromise.
- **Recovery potential:** None; no recovery or remission reported.
- **Prognostic factors:** Biallelic LoF genotype predicts the severe phenotype; no validated molecular prognostic biomarker beyond genotype.

---

## Section 12 — Treatment

**No disease-modifying or curative therapy exists.** Management is entirely **symptomatic, supportive, and palliative**:

| Intervention | Role | NCIT suggestion |
|---|---|---|
| Antiseizure/anticonvulsant medications | Seizure control (often refractory) | C264 (Anticonvulsant Agent) |
| Rehabilitation (PT/OT/speech) | Function/comfort | C15917 (Rehabilitation Therapy) |
| Nutritional & respiratory support | Supportive care | C15277 (Supportive Care) |
| Palliative / end-of-life care | Comfort | C15284 (Palliative Care) |
| Genetic counseling | Family guidance/prevention | C15516 (Genetic Counseling) |

**Advanced therapeutics.** No gene therapy, cell therapy, RNA-based therapy, or TGF-β1-replacement trials have been reported for this indication. Conceptually, because the downstream effector is localized TGF-β1 activation, strategies restoring microglial TGF-β1 signaling or NRROS function are of theoretical interest but remain unexplored clinically.

**Pharmacogenomics / personalized medicine.** None established.

---

## Section 13 — Prevention

- **Primary prevention:** Not applicable in the conventional sense (monogenic). Prevention is through **genetic counseling** and reproductive options for carrier couples (prenatal diagnosis, preimplantation genetic testing) once a familial biallelic NRROS genotype is known.
- **Secondary prevention / screening:** Cascade carrier testing of relatives; no population newborn screen exists given rarity.
- **Tertiary prevention:** Supportive management to limit complications (aspiration, status epilepticus).
- **Counseling:** Autosomal-recessive recurrence risk is 25% for carrier couples; genetic counseling is central.
- **Immunization / public health / environmental interventions:** Not applicable.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy / orthologs:** Mouse ortholog *Nrros* (NCBI Gene 70571; NCBITaxon:10090). The gene and its TGF-β1/NOX2 functions are evolutionarily conserved in mammals.
- **Natural disease in other species:** No naturally occurring companion-animal or wildlife disease specifically attributed to NRROS has been reported (no OMIA entry noted).
- **Comparative biology:** The mouse recapitulates the human phenotype (see Section 15), supporting conservation of the disease mechanism. The TGF-β1/LRRC33 axis is also studied extensively in mouse tumor immunology.
- **Zoonotic potential:** Not applicable (non-infectious genetic disease).

---

## Section 15 — Model Organisms

- **Mouse (primary mammalian model).** The **Nrros-knockout mouse** and the **Lrrc33-deficient mouse** are the principal models.
  - *Phenotype recapitulation:* Strong. Dong 2020 states ([PMID: 32197075](https://pubmed.ncbi.nlm.nih.gov/32197075/)): *"The phenotypic features in affected individuals are consistent with those observed in the Nrros knockout mouse, and they overlap with those seen in the human condition associated with TGF-β1 deficiency."* Qin 2018 showed Lrrc33⁻/⁻ mice have microglial dysfunction from loss of localized TGF-β1 activation. Noubade 2014 showed Nrros-deficient mice develop severe EAE from CNS oxidative damage (ROS branch).
  - *Model types available:* Constitutive knockout; the NOX2-interaction and TGF-β1-presentation functions have both been dissected in mouse.
  - *Limitations:* Mouse models may not fully capture the human calcification phenotype or exact clinical course; the two NRROS functions (TGF-β1 vs NOX2) are partly separable in different mouse studies.
- **Convergent human genetic model — TGFB1 deficiency.** Biallelic human TGFB1 LoF causes severe infantile inflammatory bowel disease and encephalopathy ([PMID: 29483653](https://pubmed.ncbi.nlm.nih.gov/29483653/)). This confirms CNS dependence on TGF-β1 — the downstream effector of NRROS — and supports the mechanistic model.
- **In vitro / cellular.** Flow-cytometry assays of surface vs intracellular latent TGF-β1 anchoring in cells expressing wild-type vs mutant NRROS (Dong 2020) provided the functional proof of the anchoring defect. Structural studies (Duan 2022) defined LRRC33–TGF-β1–integrin specificity.

---

## Mechanistic Model / Interpretation

NRROS-Related Microgliopathy is best understood as a **microglial TGF-β1-activation deficiency with a superimposed oxidative-damage component**. The unifying insight is that NRROS/LRRC33 has two conserved jobs in myeloid/microglial cells: (1) at the **plasma membrane**, it anchors and presents latent TGF-β1 for integrin-αVβ8-dependent local activation; and (2) in the **ER**, it degrades nascent NOX2 to restrain ROS. Biallelic LoF simultaneously removes a pro-homeostatic signal (TGF-β1) and a brake on oxidative stress (NOX2). In the CNS, microglia critically depend on autocrine/paracrine TGF-β1 to adopt and maintain their homeostatic identity; losing this signal yields dysfunctional microglia, while unrestrained ROS adds oxidative tissue injury. The combined insult produces a calcifying leukoencephalopathy with grey- and white-matter degeneration and foamy macrophage infiltration, which clinically manifests as early-onset refractory epilepsy, regression, microcephaly, and progressive, usually fatal neurodegeneration.

The model is strongly triangulated: (i) patient variants functionally fail to anchor TGF-β1 (in vitro), (ii) the Nrros/Lrrc33 mouse phenocopies the disease, and (iii) human TGFB1 deficiency — the downstream effector — independently causes encephalopathy. The relative contributions of the TGF-β1 (upstream, best-supported) versus NOX2/ROS (branch, inferred) arms to the human calcification phenotype remain to be fully quantified.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [32197075](https://pubmed.ncbi.nlm.nih.gov/32197075/) | Bi-allelic LoF NRROS variants impairing active TGF-β1 delivery cause severe infantile neurodegeneration | Establishes causality (6 individuals/4 families), anchoring defect, mouse/TGF-β1 convergence |
| [35716448](https://pubmed.ncbi.nlm.nih.gov/35716448/) | Delineating the epilepsy phenotype of NRROS-related microgliopathy | Natural history (n=11): onset ~12 mo, death ~36 mo, calcification 8/11, founder variant |
| [35099671](https://pubmed.ncbi.nlm.nih.gov/35099671/) | Novel biallelic NRROS variants; lethal microgliopathy | Neuropathology: grey+white matter, dystrophic calcification, foamy macrophages, mitochondrial EM |
| [29909984](https://pubmed.ncbi.nlm.nih.gov/29909984/) | A milieu molecule for TGF-β required for microglia function | Defines NRROS/LRRC33 microglial TGF-β1 activation (integrin-αVβ8) |
| [24739962](https://pubmed.ncbi.nlm.nih.gov/24739962/) | NRROS negatively regulates ROS during host defence and autoimmunity | ER/NOX2 function; ROS branch; EAE |
| [29483653](https://pubmed.ncbi.nlm.nih.gov/29483653/) | Human TGF-β1 deficiency causes IBD and encephalopathy | Confirms CNS dependence on downstream TGF-β1 |
| [36008481](https://pubmed.ncbi.nlm.nih.gov/36008481/) | Specificity of TGF-β1 signal by LRRC33 and integrin | Structural basis of LRRC33–TGF-β1–integrin |
| [23545260](https://pubmed.ncbi.nlm.nih.gov/23545260/) / [24550525](https://pubmed.ncbi.nlm.nih.gov/24550525/) | LRRC33 inhibits TLR/NF-κB; epigenetically modulated | Immune-regulatory role; H3K4me3/H3K27me3 regulation |
| [28072696](https://pubmed.ncbi.nlm.nih.gov/28072696/) | CRMCC case report | Differential diagnosis (calcifying leukoencephalopathy, CTC1) |

Supporting tumor-immunology literature ([PMID: 35181792](https://pubmed.ncbi.nlm.nih.gov/35181792/), [40992270](https://pubmed.ncbi.nlm.nih.gov/40992270/), [31600200](https://pubmed.ncbi.nlm.nih.gov/31600200/)) corroborates the LRRC33/TGF-β1 axis in myeloid cells, reinforcing the mechanistic foundation.

---

## Limitations and Knowledge Gaps

- **Very small N (<~15 patients).** All epidemiology, natural-history, and genotype-phenotype statements rest on small case series; prevalence/incidence are unquantified.
- **TGF-β1 vs NOX2 contribution.** The relative weight of lost TGF-β1 signaling (best-supported) versus the NOX2/ROS oxidative branch (inferred) in producing human calcification and neurodegeneration is not quantitatively resolved.
- **No validated biomarker.** No blood/CSF biomarker exists for diagnosis or disease monitoring.
- **No therapeutic data.** No trials of any disease-modifying approach; all treatment is supportive.
- **Mechanism-to-calcification link.** The precise mechanism linking microglial dysfunction/ROS to dystrophic grey-white junction calcification is not fully elucidated.
- **Citation caveat.** One cited abstract snippet (PMID:29483653) was logged as a title-derived paraphrase in the knowledge state; the underlying claim (human TGF-β1 deficiency → encephalopathy) is correct and consistent with the paper's subject.

---

## Proposed Follow-up Experiments / Actions

1. **International patient registry & natural-history study** to refine prevalence, genotype-phenotype correlations, and survival with larger N.
2. **Dissect the TGF-β1 vs NOX2 contributions** using conditional/separation-of-function Nrros mouse alleles (TGF-β1-presentation-dead vs NOX2-binding-dead) to attribute calcification and neurodegeneration to each arm.
3. **Microglial single-cell/spatial transcriptomics** from patient-derived iPSC microglia or mouse models to map the dysmaturation signature and identify druggable nodes.
4. **Biomarker discovery** (CSF/plasma neurofilament, TGF-β pathway readouts, ROS markers) for diagnosis and potential trial endpoints.
5. **Preclinical therapeutic exploration:** test whether restoring TGF-β1 signaling (e.g., engineered/targeted TGF-β1 delivery to microglia) or antioxidant/NOX2 modulation mitigates phenotype in Nrros mouse models; evaluate gene-replacement feasibility given the early critical window.
6. **Standardized imaging protocol** (CT for calcification + MRI for white matter) to enable earlier recognition and differential diagnosis from Aicardi-Goutières/CRMCC.

---

*Report compiled from an autonomous multi-iteration investigation (8 confirmed findings; 18 papers reviewed). Evidence sources span human clinical case series, mouse models, in vitro functional assays, and structural/computational studies.*


## Artifacts

- [OpenScientist final report](NRROS-Related_Microgliopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](NRROS-Related_Microgliopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 9 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030033` (3 mentions) - the report calls it "MONDO"; MONDO calls it **seizures, early-onset, with neurodegeneration and brain calcifications**
- `HP:0002376` (1 mention) - the report calls it "Median ~12 mo"; HP calls it **Developmental regression**
- `HP:0002059` (1 mention) - the report calls it "Progressive"; HP calls it **Cerebral atrophy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0012469` (1 mention) - the report calls it "Infantile"; HP calls it **Infantile spasms**
- `HP:0005484` (1 mention) - the report calls it "Acquired, progressive"; HP calls it **Secondary microcephaly**, and lists "Acquired microcephaly" among its other names
- `CL:0000129` (2 mentions) - the report calls it "Cell populations:** Microglia"; CL calls it **microglial cell**, and lists "microglia" among its other names
- `GO:0005886` (2 mentions) - the report calls it "Subcellular:** Plasma membrane"; GO calls it **plasma membrane**, and lists "cellular membrane" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.