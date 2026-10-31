---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T15:27:58.213639'
end_time: '2026-09-29T15:41:47.026294'
duration_seconds: 828.81
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: External Hordeolum
  mondo_id: MONDO:0001642
  category: Infectious Disease
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
citation_count: 31
reference_validation:
  total_references: 31
  verified: 31
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 31
  on_topic: 20
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 7
  verified: 7
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 1
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0025421
    reported_labels:
    - Eyelid pain, approximate
    ontology_label: Pneumomediastinum
  - term_id: HP:0000198
    reported_labels:
    - Abnormal eyelid morphology
    ontology_label: Absence of Stensen duct
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: External_Hordeolum-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: External_Hordeolum-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** External Hordeolum
- **MONDO ID:** MONDO:0001642 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **External Hordeolum** covering all of the
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

# External Hordeolum (Stye): A Comprehensive Disease Characterization Report

**Disease:** External Hordeolum | **MONDO ID:** MONDO:0001642 | **Category:** Infectious Disease
**Report basis:** 5 iterations, 10 confirmed findings, 40 papers reviewed

---

## Summary

**External hordeolum (a "stye") is a common, acute, painful, usually self-limited suppurative (abscess-forming) infection of the superficial eyelash-line glands of Zeis (sebaceous) and Moll (apocrine), most often caused by *Staphylococcus aureus*.** It is distinguished from internal hordeolum, which involves the meibomian glands within the tarsal plate. The disease is an **acquired, non-genetic, multifactorial condition**: exhaustive review found no OMIM phenotype entry, no ClinVar/HGMD pathogenic variants, no susceptibility loci, and no dedicated animal or organoid model. Its causal chain runs from **gland-orifice obstruction → bacterial proliferation → neutrophilic abscess formation → pointing and spontaneous drainage at the anterior lid margin**.

The clinical picture is dominated by an excellent prognosis — most lesions resolve spontaneously in about one week — set against a background of frequent recurrence and a small but important set of severe complications when lesions are neglected (preseptal cellulitis, eyelid necrosis, and rarely periorbital necrotizing fasciitis). Predisposition is driven by chronic **blepharitis and meibomian gland dysfunction (MGD)**, **Demodex mite infestation** (strongly associated with recurrent external hordeola), and emerging **iatrogenic causes** (CFTR modulators such as elexacaftor/tezacaftor/ivacaftor, and GLP-1/GIP agonists such as tirzepatide) that induce sterile gland obstruction.

Management is **conservative-first**: warm compresses, lid hygiene, and topical antibiotics for 5–14 days, with incision and curettage reserved for non-resolving lesions. Diagnosis is clinical, but persistent, recurrent, or clinically atypical lesions must be biopsied to exclude **sebaceous cell carcinoma**, the most commonly missed malignancy masquerading as benign eyelid lesions. Because there is no genetic or molecular disease architecture, sections of the research template concerning causal genes, variants, inheritance, omics diagnostics, and model organisms are legitimately **"not applicable"** for this disease — a finding that is itself informative for a knowledge-base entry.

---

## Key Findings

### F001 — External hordeolum is an acute suppurative infection of the eyelash-line glands of Zeis/Moll

External hordeolum is defined anatomically by the specific glands it affects. A Cochrane review ([PMID: 28181687](https://pubmed.ncbi.nlm.nih.gov/28181687/)) states: *"When the meibomian gland in the tarsal plate is affected, internal hordeolum occurs, while when the glands of Zeis or Moll associated with eyelash follicles are affected, external hordeolum, or stye occurs."* This distinction is the defining feature separating external from internal hordeolum and localizes the disease to the **anterior lid margin at the lash line** (glands of Zeis = sebaceous glands of the follicle; glands of Moll = modified apocrine sweat glands). The natural history is benign and time-limited: *"The onset of hordeolum is usually self limited, and may resolve in about a week with spontaneous drainage of the abscess."* Recurrences are very common, and unresolved lesions can progress to a chalazion (a chronic lipogranuloma) or to eyelid cellulitis.

### F002 — The disease is usually caused by bacterial infection, predominantly *Staphylococcus aureus*

Hordeolum is a bacterial infection of eyelid oil glands. A Cochrane review ([PMID: 28068454](https://pubmed.ncbi.nlm.nih.gov/28068454/)) states: *"A hordeolum is a common, painful inflammation of the eyelid margin that is usually caused by a bacterial infection."* The specific pathogen is most often *S. aureus*. A case report of a rare, severe complication ([PMID: 41787906](https://pubmed.ncbi.nlm.nih.gov/41787906/)) documents *"periorbital NF [necrotizing fasciitis] caused by methicillin-sensitive Staphylococcus aureus (MSSA) in a previously healthy 48-year-old woman, originating from a neglected, recurrent hordeolum,"* confirming both the staphylococcal etiology and the potential for the infection to spread destructively when neglected. **Pathogen note:** causative organism *Staphylococcus aureus* (NCBI Taxon 1280).

### F003 — Demodex mite infestation is strongly associated with recurrent hordeola, especially external hordeola

An observational comparative study of 250 patients ([PMID: 34725365](https://pubmed.ncbi.nlm.nih.gov/34725365/)) found *"Demodex was detected in 91 (59.5%) and 17 (17.5%) patients in the recurrent hordeolum and control groups (p < 0.001), respectively"* — a roughly 3.4-fold higher detection rate in recurrent cases. Critically for this disease, external hordeola predominated among Demodex-associated lesions: *"The most common presentation of Demodex-associated recurrent lesions was external hordeola (67%) (p = 0.002)."* Demodex-infested patients also recurred sooner after incision and curettage, and the association was strongest in patients in their 20s. This positions **Demodex folliculorum/brevis infestation** as a leading modifiable driver of recurrence.

| Group | n | Demodex detected | Rate |
|---|---|---|---|
| Recurrent hordeolum | 153 | 91 | **59.5%** |
| Controls | 97 | 17 | 17.5% |
| Statistical test | — | — | p < 0.001 |

### F004 — Hordeolum is common, with bimodal age peaks and a slight youth female predominance

A Japanese nationwide claims study (2014–2022) recording 1,104,078 procedures ([PMID: 41675090](https://pubmed.ncbi.nlm.nih.gov/41675090/)) reported: *"The annual average rates were 40.9 for ITC [invasive treatment for chalazion] and 56.2 for ITH [invasive treatment for hordeolum] per 100 000 person-years."* Invasive treatment for hordeolum showed **bimodal age peaks** (males 10–14 y: 82.9; 35–39 y: 72.1 per 100,000; females 10–14 y: 102.4; 30–34 y: 78.3 per 100,000), with a youth female predominance (F:M ≈ 1.7 at ages 20–24) but an overall sex ratio near 1.0. In a Korean military teleophthalmology cohort ([PMID: 42299138](https://pubmed.ncbi.nlm.nih.gov/42299138/)), *"The most common diagnoses were hordeolum/chalazion (39.3%) and viral conjunctivitis (20.3%),"* underscoring that hordeolum/chalazion is among the most frequent ophthalmic diagnoses seen in general practice.

### F005 — Systemic drugs (CFTR modulators, GLP-1/GIP agonists) are emerging iatrogenic risk factors

Two distinct drug classes have recently been linked to hordeolum through gland dysfunction. A pediatric cystic fibrosis case series ([PMID: 41298194](https://pubmed.ncbi.nlm.nih.gov/41298194/)) reported: *"This report highlights a 5.5-fold increased incidence of chalazion/hordeolum in pwCF [people with cystic fibrosis]"* on elexacaftor/tezacaftor/ivacaftor (ETI), with one-third of affected patients needing therapy interruption to resolve. Separately, a case series of tirzepatide (a dual GLP-1/GIP agonist) ([PMID: 42756500](https://pubmed.ncbi.nlm.nih.gov/42756500/)) documented multiple simultaneous hordeola with positive dechallenge/rechallenge, *"supporting a sterile, obstructive meibomian gland process rather than infection."* These observations reinforce **gland obstruction** as the upstream mechanistic event that precedes (and enables) secondary infection.

### F006 — First-line management is conservative; incision/curettage is reserved for non-resolving lesions

A practice survey of the Korean Society of Ophthalmic Plastic and Reconstructive Surgery ([PMID: 40267992](https://pubmed.ncbi.nlm.nih.gov/40267992/)) established the real-world algorithm: *"For hordeolum, topical antibiotics are preferred by 59 respondents (73.8%), with 49 (83.7%) considering them effective,"* and *"Most (62 respondents, 77.6%) pursue nonsurgical treatment for 5 to 14 days before considering incision and curettage."* Importantly, formal evidence is thin: Cochrane reviews of non-surgical interventions for acute internal hordeolum ([PMID: 28068454](https://pubmed.ncbi.nlm.nih.gov/28068454/), [PMID: 23633345](https://pubmed.ncbi.nlm.nih.gov/23633345/), [PMID: 20824865](https://pubmed.ncbi.nlm.nih.gov/20824865/)) and a Cochrane review of acupuncture ([PMID: 28181687](https://pubmed.ncbi.nlm.nih.gov/28181687/)) all found insufficient randomized evidence to draw firm conclusions. Emerging options include **intense pulsed light** (IPL), which produced significant OSDI reduction and faster recovery versus medication ([PMID: 41731784](https://pubmed.ncbi.nlm.nih.gov/41731784/)), and **intralesional diluted 5-fluorouracil** for persistent nodules ([PMID: 42367702](https://pubmed.ncbi.nlm.nih.gov/42367702/)).

### F007 — Prognosis is excellent, but rare severe complications occur if neglected

Reviews confirm the benign baseline: *"The majority of these lesions resolve spontaneously over time"* ([PMID: 34379160](https://pubmed.ncbi.nlm.nih.gov/34379160/)). However, neglected or severe external hordeola can progress to serious complications, including preseptal cellulitis, upper eyelid necrosis with anterior-lamella damage — *"upper eyelid necrosis initially misdiagnosed as a preseptal cellulitis following a hordeolum externum resulting in great damage to the upper eyelid (anterior lamella)"* ([PMID: 34054469](https://pubmed.ncbi.nlm.nih.gov/34054469/)) — and life-threatening periorbital necrotizing fasciitis ([PMID: 41787906](https://pubmed.ncbi.nlm.nih.gov/41787906/)). A primary-care review ([PMID: 32622681](https://pubmed.ncbi.nlm.nih.gov/32622681/)) situates hordeolum among common eyelid infections presenting with redness, swelling, and tearing.

### F008 — Diagnosis is clinical; atypical/recurrent lesions require biopsy to exclude sebaceous carcinoma

Hordeolum is diagnosed clinically from its typical morphology and course. The key danger is malignancy masquerading as a benign lesion. A histopathology series of 1,060 clinically diagnosed chalazia ([PMID: 14762403](https://pubmed.ncbi.nlm.nih.gov/14762403/)) found: *"Sebaceous cell carcinoma was the most commonly missed malignancy (12 cases, 1.1%) followed by basal cell carcinoma (three cases, 0.3%),"* — a ~1.4% overall malignancy rate. Multiple case reports document sebaceous gland carcinoma masquerading as chalazion/hordeolum ([PMID: 32788569](https://pubmed.ncbi.nlm.nih.gov/32788569/), [PMID: 25258508](https://pubmed.ncbi.nlm.nih.gov/25258508/), [PMID: 11417345](https://pubmed.ncbi.nlm.nih.gov/11417345/)), and even orbital metastasis from breast carcinoma has mimicked a hordeolum ([PMID: 42552075](https://pubmed.ncbi.nlm.nih.gov/42552075/)). The clinical rule ([PMID: 34379160](https://pubmed.ncbi.nlm.nih.gov/34379160/)): *"In persistent, recurrent or clinically atypical cases malignant tumors must be excluded as a differential diagnosis by excisional biopsy and histopathological assessment."*

### F009 — Chronic blepharitis/MGD predisposes to hordeolum; lid hygiene is the mainstay of prevention

Hordeola arise on a background of underlying gland disease: *"They can occur in association with underlying diseases causing Meibomian gland dysfunction and/or chronic blepharitis"* ([PMID: 34379160](https://pubmed.ncbi.nlm.nih.gov/34379160/)). Blepharitis itself is a chronic multifactorial eyelid-margin inflammation whose suspected drivers include chronic low-grade bacterial infection, Demodex infestation, and seborrhea ([PMID: 22592706](https://pubmed.ncbi.nlm.nih.gov/22592706/)), and whose treatment goals explicitly include recurrence prevention via lid hygiene, topical/systemic antibiotics, and omega-3 supplements ([PMID: 38337403](https://pubmed.ncbi.nlm.nih.gov/38337403/)). Lid-margin cleansing has direct preventive value: a novel detergent *"successfully eliminated Demodex mites, a common pathogen of refractory obstructive meibomian gland dysfunction"* ([PMID: 33967173](https://pubmed.ncbi.nlm.nih.gov/33967173/)).

### F010 — External hordeolum is a non-genetic acquired disease with no causal genes, animal models, or omics diagnostics

A comprehensive review across Cochrane systematic reviews, national claims registries, clinical reviews, and case series identified **no OMIM phenotype entry, no ClinVar/HGMD pathogenic variants, no susceptibility loci, no dedicated animal/organoid model, and no omics-based diagnostic** for external hordeolum. Etiology is uniformly described as acquired bacterial infection (predominantly *S. aureus*) of obstructed lash-line glands ([PMID: 28181687](https://pubmed.ncbi.nlm.nih.gov/28181687/), [PMID: 28068454](https://pubmed.ncbi.nlm.nih.gov/28068454/)), with acquired risk factors rather than heredity.

---

## Full Section-by-Section Report

### 1. Disease Information

**Overview.** External hordeolum ("stye") is an acute, localized, painful, suppurative bacterial infection of the superficial glands at the eyelash line — the sebaceous **glands of Zeis** and the apocrine **glands of Moll** — presenting as a tender erythematous nodule or pustule pointing anteriorly at the lid margin near an eyelash follicle. It is contrasted with **internal hordeolum**, an infection of the deeper meibomian glands within the tarsal plate ([PMID: 28181687](https://pubmed.ncbi.nlm.nih.gov/28181687/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0001642 (external hordeolum) |
| ICD-10 | H00.0 (Hordeolum externum, within Hordeolum and other deep inflammation of eyelid) |
| ICD-11 | 9A01.0 (Hordeolum) |
| MeSH | D006726 (Hordeolum) |
| SNOMED CT | Hordeolum externum / stye |
| OMIM | **Not applicable** — no Mendelian phenotype entry |
| Orphanet | **Not applicable** — not a rare disease |

**Synonyms / alternative names.** Stye (sty); hordeolum externum; external stye; acute superficial eyelid abscess of the lash line.

**Source of information.** This report is derived overwhelmingly from **aggregated disease-level resources** — Cochrane systematic reviews, national health-insurance claims registries (Japan, Korea), clinical review articles, and case series — rather than individual EHR-level patient records.

### 2. Etiology

**Causal factors.** The primary cause is **infectious**: acute bacterial infection, predominantly *Staphylococcus aureus* (including MSSA), of the Zeis/Moll glands ([PMID: 28068454](https://pubmed.ncbi.nlm.nih.gov/28068454/), [PMID: 41787906](https://pubmed.ncbi.nlm.nih.gov/41787906/)). Mechanistically, infection is typically enabled by **gland-orifice obstruction** ([PMID: 42756500](https://pubmed.ncbi.nlm.nih.gov/42756500/)).

**Genetic risk factors.** None identified. No causal variants, susceptibility loci, or modifier genes are documented (F010). This is a non-Mendelian, non-heritable acquired infection.

**Environmental / acquired risk factors.**
- Chronic **blepharitis** and **meibomian gland dysfunction (MGD)** ([PMID: 34379160](https://pubmed.ncbi.nlm.nih.gov/34379160/))
- **Demodex** mite infestation (recurrent external hordeola: 59.5% vs 17.5%, p<0.001) ([PMID: 34725365](https://pubmed.ncbi.nlm.nih.gov/34725365/))
- Seborrhea and inflammatory skin conditions ([PMID: 22592706](https://pubmed.ncbi.nlm.nih.gov/22592706/))
- **Age** (bimodal peaks in youth and 30s), **youth female sex** ([PMID: 41675090](https://pubmed.ncbi.nlm.nih.gov/41675090/))
- **Iatrogenic/drug-induced**: CFTR modulators (elexacaftor/tezacaftor/ivacaftor, 5.5× incidence) ([PMID: 41298194](https://pubmed.ncbi.nlm.nih.gov/41298194/)); GLP-1/GIP agonists (tirzepatide) ([PMID: 42756500](https://pubmed.ncbi.nlm.nih.gov/42756500/)); systemic therapies causing blepharitis (chemotherapy, bortezomib, cetuximab, TNFα inhibitors, dupilumab) ([PMID: 38337403](https://pubmed.ncbi.nlm.nih.gov/38337403/))

**Protective factors.** No genetic protective variants exist. The principal protective/preventive factor is **lid hygiene** (warm compresses, lid-margin cleansing), which reduces gland obstruction and eradicates Demodex ([PMID: 33967173](https://pubmed.ncbi.nlm.nih.gov/33967173/)).

**Gene–environment interactions.** Not applicable — no genetic component is documented. The relevant interactions are purely **environment–environment** (e.g., MGD + Demodex + bacterial colonization synergizing to promote recurrence).

### 3. Phenotypes

| Phenotype | Type | Suggested HPO | Onset / severity / frequency |
|---|---|---|---|
| Eyelid pain / tenderness | Symptom | HP:0025421 (Eyelid pain, approximate) | Acute; mild–moderate; near-universal |
| Localized eyelid swelling | Clinical sign | HP:0000198 (Abnormal eyelid morphology) | Acute; variable |
| Eyelid erythema / redness | Clinical sign | inflammation of eyelid | Acute; common |
| Lash-line pustule/abscess pointing anteriorly | Physical manifestation | HP:0025615 (Abscess) | Acute; defining feature |
| Foreign-body sensation, tearing, itchiness | Symptom | ocular surface irritation | Acute; common ([PMID: 32622681](https://pubmed.ncbi.nlm.nih.gov/32622681/)) |

**Phenotype characteristics.** Onset is **acute** (over 1–3 days); severity is usually **mild to moderate**; course is **self-limited and episodic** (resolving in ~1 week, but frequently recurring) ([PMID: 28181687](https://pubmed.ncbi.nlm.nih.gov/28181687/)). Age of onset spans childhood through adulthood with **bimodal peaks** ([PMID: 41675090](https://pubmed.ncbi.nlm.nih.gov/41675090/)).

**Quality-of-life impact.** Generally modest and transient given the self-limited course, though pain, cosmetic concern, and recurrence can be bothersome. IPL treatment produced statistically significant reductions in Ocular Surface Disease Index (OSDI) scores, indicating measurable symptom burden that is treatment-responsive ([PMID: 41731784](https://pubmed.ncbi.nlm.nih.gov/41731784/)).

### 4. Genetic / Molecular Information

**Not applicable.** External hordeolum has **no causal genes, no pathogenic variants (ClinVar/HGMD), no modifier genes, no disease-specific epigenetic signatures, and no chromosomal abnormalities** (F010). It is not a genetic disease. The only relevant molecular actor is the pathogen genome (*S. aureus*), not the host germline.

### 5. Environmental Information

- **Infectious agents:** *Staphylococcus aureus* (NCBI Taxon 1280), the predominant cause ([PMID: 28068454](https://pubmed.ncbi.nlm.nih.gov/28068454/), [PMID: 41787906](https://pubmed.ncbi.nlm.nih.gov/41787906/)); *Demodex folliculorum/brevis* mites as recurrence drivers ([PMID: 34725365](https://pubmed.ncbi.nlm.nih.gov/34725365/)).
- **Lifestyle / hygiene factors:** poor lid hygiene, eye rubbing, and contact-lens or cosmetics-related contamination facilitate bacterial gland colonization (inferred from blepharitis/MGD literature, [PMID: 22592706](https://pubmed.ncbi.nlm.nih.gov/22592706/)).
- **Iatrogenic environmental exposures:** systemic drugs inducing gland obstruction/blepharitis (F005; [PMID: 41298194](https://pubmed.ncbi.nlm.nih.gov/41298194/), [PMID: 42756500](https://pubmed.ncbi.nlm.nih.gov/42756500/), [PMID: 38337403](https://pubmed.ncbi.nlm.nih.gov/38337403/)).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A predisposing condition (**chronic blepharitis, MGD, Demodex infestation, seborrhea, or drug-induced gland dysfunction**) **leads to** obstruction/dysfunction of a gland of Zeis or Moll at the lash line. *[Predisposition demonstrated ([PMID: 34379160](https://pubmed.ncbi.nlm.nih.gov/34379160/)); obstruction step partly inferred, but directly supported for drug-induced cases ([PMID: 42756500](https://pubmed.ncbi.nlm.nih.gov/42756500/)).]*
2. Gland-orifice obstruction and stasis of sebaceous/apocrine secretion **result in** a favorable niche for bacterial proliferation, chiefly *Staphylococcus aureus*. *[Inferred from combined infection + obstruction evidence.]*
3. Bacterial proliferation **leads to** acute suppurative inflammation with **neutrophil recruitment** and localized **abscess** formation within/around the follicle. *[Demonstrated: bacterial etiology ([PMID: 28068454](https://pubmed.ncbi.nlm.nih.gov/28068454/)); abscess is the defining lesion ([PMID: 28181687](https://pubmed.ncbi.nlm.nih.gov/28181687/)).]*
4. The abscess **causes** the clinical manifestation: a painful, erythematous, tender nodule/pustule pointing at the anterior lid margin.
5. The abscess typically **points and drains spontaneously**, **resulting in** resolution in ~1 week (self-limited course) ([PMID: 28181687](https://pubmed.ncbi.nlm.nih.gov/28181687/)).

**Branch A — recurrence/chronicity:** Persistent gland obstruction or residual granulomatous material **leads to** a chalazion (chronic lipogranuloma) or recurrent hordeola ([PMID: 28181687](https://pubmed.ncbi.nlm.nih.gov/28181687/)); Demodex persistence accelerates recurrence ([PMID: 34725365](https://pubmed.ncbi.nlm.nih.gov/34725365/)).

**Branch B — complication:** If neglected, the infection **spreads** contiguously to **result in** preseptal cellulitis, eyelid necrosis ([PMID: 34054469](https://pubmed.ncbi.nlm.nih.gov/34054469/)), or, rarely, fulminant **periorbital necrotizing fasciitis** ([PMID: 41787906](https://pubmed.ncbi.nlm.nih.gov/41787906/)).

```
Predisposition (blepharitis / MGD / Demodex / drug)
        │  obstruction of Zeis/Moll gland
        ▼
Secretion stasis ──► bacterial (S. aureus) proliferation
        │
        ▼
Neutrophilic suppuration ──► ABSCESS at lash line
        │
   ┌────┴──────────────┬───────────────────┐
   ▼                   ▼                   ▼
Spontaneous       Recurrence /         Contiguous spread
drainage (~1 wk)  chalazion           → cellulitis / necrosis
= RESOLUTION                          → necrotizing fasciitis (rare)
```

**Molecular / cellular processes:** acute inflammation (GO:0006954, inflammatory response), neutrophil-mediated antibacterial response and abscess formation, innate immune defense. **Cell types (CL):** neutrophil (CL:0000775), sebaceous gland cell (glands of Zeis), apocrine/sweat gland cell (glands of Moll), eyelid keratinocytes. **No autoimmune, metabolic-enzyme, protein-misfolding, or channelopathy mechanism** applies. There are no disease-specific transcriptomic, proteomic, metabolomic, or single-cell profiling datasets (F010).

### 7. Anatomical Structures Affected

- **Organ level (primary):** eyelid (UBERON:0000160), specifically the anterior lid margin at the eyelash line. **Secondary/complications:** orbital soft tissue/periorbita (preseptal cellulitis, necrotizing fasciitis), eyelid skin/anterior lamella (necrosis).
- **Body system:** integumentary/visual accessory (ocular adnexa).
- **Tissue/cell level:** glands of Zeis (sebaceous glands of the follicle), glands of Moll (modified apocrine sweat glands), eyelash follicle epithelium. **Cell Ontology:** sebaceous gland cell, apocrine gland cell, neutrophil (CL:0000775).
- **Subcellular level:** not specifically implicated (no organelle-level pathology).
- **Localization:** eyelash-line glands (UBERON:0000160 eyelid; follicle-associated glands). **Lateralization:** typically **unilateral**; can be bilateral or multiple, notably in drug-induced (tirzepatide) cases with simultaneous lesions ([PMID: 42756500](https://pubmed.ncbi.nlm.nih.gov/42756500/)).

### 8. Temporal Development

- **Onset:** **acute** (days). Occurs across the lifespan with bimodal age peaks in youth (10–14 y) and adults in their 30s ([PMID: 41675090](https://pubmed.ncbi.nlm.nih.gov/41675090/)).
- **Progression:** rapid onset, then **self-limited**; usual resolution ~1 week by spontaneous drainage ([PMID: 28181687](https://pubmed.ncbi.nlm.nih.gov/28181687/)).
- **Course pattern:** **episodic/recurrent**; unresolved lesions may become chronic (chalazion).
- **Duration:** **self-limited** (short-lived per episode); recurrences common.
- **Remission:** predominantly **spontaneous**; treatment (compresses, antibiotics, I&C) can accelerate resolution.
- **Critical window:** early recognition and conservative treatment (5–14 days) before considering procedural intervention; neglect is the key driver of complications ([PMID: 40267992](https://pubmed.ncbi.nlm.nih.gov/40267992/), [PMID: 41787906](https://pubmed.ncbi.nlm.nih.gov/41787906/)).

### 9. Inheritance and Population

- **Epidemiology:** Population-based invasive-treatment rate ≈ **56.2 per 100,000 person-years** in Japan (procedures — a lower bound on true incidence, since most cases are treated non-invasively) ([PMID: 41675090](https://pubmed.ncbi.nlm.nih.gov/41675090/)). Hordeolum/chalazion was the single most common ophthalmic diagnosis (39.3%) in a Korean cohort ([PMID: 42299138](https://pubmed.ncbi.nlm.nih.gov/42299138/)). Public awareness is high (73.8% of Polish adults had heard of hordeolum, [PMID: 36834287](https://pubmed.ncbi.nlm.nih.gov/36834287/)).
- **Inheritance:** **None** — non-genetic, acquired; no inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity role, or carrier frequency applies (F010).
- **Sex ratio:** overall ≈ 1.0; **youth female predominance** (F:M ≈ 1.7 at 20–24 y) ([PMID: 41675090](https://pubmed.ncbi.nlm.nih.gov/41675090/)).
- **Age distribution:** bimodal (adolescents and adults in their 30s).
- **Geographic distribution:** worldwide; no endemic clustering (contrast with vector-borne eyelid disease such as cutaneous leishmaniasis, [PMID: 28095664](https://pubmed.ncbi.nlm.nih.gov/28095664/)).

### 10. Diagnostics

- **Clinical diagnosis** is the standard: typical acute tender lash-line pustule with characteristic course ([PMID: 34379160](https://pubmed.ncbi.nlm.nih.gov/34379160/), [PMID: 32622681](https://pubmed.ncbi.nlm.nih.gov/32622681/)). No routine laboratory test, biomarker, or imaging study is required.
- **Microbiology:** culture (e.g., of drainage) may identify *S. aureus* in complicated/atypical cases ([PMID: 41787906](https://pubmed.ncbi.nlm.nih.gov/41787906/)).
- **Demodex evaluation:** lash sampling/microscopy in recurrent cases ([PMID: 34725365](https://pubmed.ncbi.nlm.nih.gov/34725365/)).
- **Imaging:** noninvasive **meibography** can help distinguish sebaceous carcinoma (high reflectivity, poorly marginated) from benign chalazion ([PMID: 25258508](https://pubmed.ncbi.nlm.nih.gov/25258508/)); orbital MRI may be needed if malignancy/metastasis is suspected ([PMID: 42552075](https://pubmed.ncbi.nlm.nih.gov/42552075/)).
- **Histopathology/biopsy:** the critical test for **persistent, recurrent, or atypical** lesions to exclude sebaceous cell carcinoma and other malignancies ([PMID: 14762403](https://pubmed.ncbi.nlm.nih.gov/14762403/), [PMID: 34379160](https://pubmed.ncbi.nlm.nih.gov/34379160/), [PMID: 16008694](https://pubmed.ncbi.nlm.nih.gov/16008694/)).
- **Genetic / omics testing:** **not applicable** — no genetic test, gene panel, or omics-based diagnostic exists (F010).
- **Differential diagnosis:** internal hordeolum, chalazion, preseptal cellulitis, sebaceous cell carcinoma, basal/squamous cell carcinoma, tarsal epithelial cyst ([PMID: 32826823](https://pubmed.ncbi.nlm.nih.gov/32826823/)), pyogenic granuloma, eyelid cutaneous horn ([PMID: 39393420](https://pubmed.ncbi.nlm.nih.gov/39393420/)), and rarely orbital metastasis ([PMID: 42552075](https://pubmed.ncbi.nlm.nih.gov/42552075/)) or systemic disease (granulomatosis with polyangiitis, [PMID: 39336596](https://pubmed.ncbi.nlm.nih.gov/39336596/)).

### 11. Outcome / Prognosis

- **Survival/mortality:** essentially **no disease-specific mortality**; excellent prognosis with spontaneous resolution ([PMID: 34379160](https://pubmed.ncbi.nlm.nih.gov/34379160/)). Fatal outcomes are exceptional and confined to neglected complications like necrotizing fasciitis ([PMID: 41787906](https://pubmed.ncbi.nlm.nih.gov/41787906/)).
- **Morbidity:** low; transient pain/swelling, cosmetic concern, recurrence. Long-term disability is rare.
- **Complications:** chalazion, preseptal cellulitis, eyelid (anterior-lamella) necrosis ([PMID: 34054469](https://pubmed.ncbi.nlm.nih.gov/34054469/)), periorbital necrotizing fasciitis ([PMID: 41787906](https://pubmed.ncbi.nlm.nih.gov/41787906/)).
- **Recovery:** near-complete recovery expected with or without treatment; treatment shortens the course.
- **Prognostic factors:** neglect/delay and comorbid immune status raise complication risk; Demodex infestation predicts earlier recurrence ([PMID: 34725365](https://pubmed.ncbi.nlm.nih.gov/34725365/)).

### 12. Treatment

| Modality | Details | Evidence | NCIT (suggested) |
|---|---|---|---|
| Warm compresses | First-line; promote drainage | [PMID: 40267992](https://pubmed.ncbi.nlm.nih.gov/40267992/), [PMID: 42361717](https://pubmed.ncbi.nlm.nih.gov/42361717/) | Warm Compress Therapy |
| Lid hygiene | Lid-margin cleansing; targets Demodex/MGD | [PMID: 33967173](https://pubmed.ncbi.nlm.nih.gov/33967173/) | Hygiene |
| Topical antibiotics | Preferred by 73.8% of surgeons; effective per 83.7% | [PMID: 40267992](https://pubmed.ncbi.nlm.nih.gov/40267992/) | Topical Antibiotic Therapy |
| Incision & curettage | For non-resolving lesions after 5–14 days | [PMID: 40267992](https://pubmed.ncbi.nlm.nih.gov/40267992/) | Incision and Drainage |
| Intense pulsed light (IPL) | Faster recovery, lower OSDI, fewer surgeries vs meds | [PMID: 41731784](https://pubmed.ncbi.nlm.nih.gov/41731784/) | Phototherapy |
| Intralesional 5-FU (diluted) | For persistent inflammatory nodules | [PMID: 42367702](https://pubmed.ncbi.nlm.nih.gov/42367702/) | Fluorouracil |
| Systemic antibiotics | For cellulitis/complicated cases | [PMID: 41787906](https://pubmed.ncbi.nlm.nih.gov/41787906/) | Systemic Antibiotic Therapy |

**Evidence caveat:** Cochrane reviews found **insufficient RCT evidence** for or against non-surgical interventions ([PMID: 28068454](https://pubmed.ncbi.nlm.nih.gov/28068454/), [PMID: 23633345](https://pubmed.ncbi.nlm.nih.gov/23633345/), [PMID: 20824865](https://pubmed.ncbi.nlm.nih.gov/20824865/)) and for acupuncture ([PMID: 28181687](https://pubmed.ncbi.nlm.nih.gov/28181687/)). **Pharmacogenomics, gene therapy, cell therapy, RNA therapy, targeted therapy, and immunotherapy are not applicable.** For iatrogenic cases, **dechallenge** (drug interruption) can resolve lesions ([PMID: 41298194](https://pubmed.ncbi.nlm.nih.gov/41298194/), [PMID: 42756500](https://pubmed.ncbi.nlm.nih.gov/42756500/)).

### 13. Prevention

- **Primary prevention:** **lid hygiene** and warm compresses to prevent gland obstruction; management of underlying blepharitis/MGD ([PMID: 34379160](https://pubmed.ncbi.nlm.nih.gov/34379160/), [PMID: 38337403](https://pubmed.ncbi.nlm.nih.gov/38337403/)); Demodex eradication via lid-margin cleansing ([PMID: 33967173](https://pubmed.ncbi.nlm.nih.gov/33967173/)).
- **Secondary prevention:** early recognition and conservative treatment to prevent progression to cellulitis/necrosis ([PMID: 40267992](https://pubmed.ncbi.nlm.nih.gov/40267992/)).
- **Tertiary prevention:** biopsy of atypical/recurrent lesions to avoid missing malignancy ([PMID: 14762403](https://pubmed.ncbi.nlm.nih.gov/14762403/)); prompt antibiotic/surgical care for spreading infection.
- **Immunization / genetic screening / counseling:** **not applicable** (no vaccine, no genetic basis).
- **Iatrogenic prevention:** monitor patients on CFTR modulators, GLP-1/GIP agonists, and blepharitis-inducing systemic therapies ([PMID: 41298194](https://pubmed.ncbi.nlm.nih.gov/41298194/), [PMID: 42756500](https://pubmed.ncbi.nlm.nih.gov/42756500/), [PMID: 38337403](https://pubmed.ncbi.nlm.nih.gov/38337403/)).

### 14. Other Species / Natural Disease

Explicit veterinary literature on external hordeolum was not identified in this investigation. Because the causative organism (*S. aureus*, NCBI Taxon 1280) and the anatomical substrate (eyelash-associated sebaceous/apocrine glands) are broadly conserved in mammals, an analogous stye-like eyelid gland abscess is biologically plausible in companion animals, but no OMIA entry or specific breed/taxon/orthologous-gene association is applicable (this is not a genetic disease). **Zoonotic transmission:** not applicable.

### 15. Model Organisms

**Not applicable.** No dedicated animal, invertebrate, cellular, organoid, or iPSC model of external hordeolum exists (F010). Because the disease is an acquired, self-limited, localized bacterial gland infection without a genetic basis, there is no knockout/knock-in/transgenic/humanized model and no model-organism database entry (MGI, RGD, ZFIN, etc.). Mechanistic understanding derives from human clinical observation and the broader blepharitis/MGD/Demodex literature.

---

## Mechanistic Model / Interpretation

The unifying model is a **two-hit process**: (1) an **obstruction hit** to a lash-line gland (from blepharitis, MGD, Demodex, seborrhea, or drug effect) that impairs secretion outflow, followed by (2) an **infection hit** from *S. aureus* proliferating in the stagnant gland, producing a neutrophilic abscess. The drug-induced cases (tirzepatide, CFTR modulators) are especially instructive: they demonstrate that **gland obstruction alone** can generate the clinical picture (a "sterile, obstructive" process, [PMID: 42756500](https://pubmed.ncbi.nlm.nih.gov/42756500/)), positioning obstruction firmly **upstream** of infection in the causal chain. Recurrence is best explained by persistence of the upstream driver (untreated MGD/blepharitis or Demodex), which is why **lid hygiene** — an intervention aimed at the upstream obstruction/infestation rather than the downstream abscess — is the most rational preventive lever.

| Axis | External hordeolum | Contrast |
|---|---|---|
| Affected gland | Zeis (sebaceous) + Moll (apocrine), lash line | Internal hordeolum: meibomian (tarsal plate) |
| Nature | Acute suppurative abscess | Chalazion: chronic lipogranuloma |
| Genetic basis | None | — |
| Prognosis | Excellent, self-limited | Malignant masquerade (sebaceous carcinoma): poor if missed |

---

## Evidence Base

| PMID | Type | Supports |
|---|---|---|
| [28181687](https://pubmed.ncbi.nlm.nih.gov/28181687/) | Cochrane review | Definition (Zeis/Moll), self-limited course (F001, F006) |
| [28068454](https://pubmed.ncbi.nlm.nih.gov/28068454/) | Cochrane review | Bacterial etiology; evidence gap (F002, F006) |
| [41787906](https://pubmed.ncbi.nlm.nih.gov/41787906/) | Case report | MSSA etiology; necrotizing fasciitis complication (F002, F007) |
| [34725365](https://pubmed.ncbi.nlm.nih.gov/34725365/) | Comparative study (n=250) | Demodex–recurrent external hordeola association (F003) |
| [41675090](https://pubmed.ncbi.nlm.nih.gov/41675090/) | Nationwide claims (Japan) | Incidence, bimodal age, sex ratio (F004) |
| [42299138](https://pubmed.ncbi.nlm.nih.gov/42299138/) | Cohort (Korea) | Hordeolum/chalazion most common diagnosis (F004) |
| [41298194](https://pubmed.ncbi.nlm.nih.gov/41298194/) | Case series | CFTR modulator 5.5× risk (F005) |
| [42756500](https://pubmed.ncbi.nlm.nih.gov/42756500/) | Case series | Tirzepatide; obstructive mechanism (F005) |
| [40267992](https://pubmed.ncbi.nlm.nih.gov/40267992/) | Practice survey | Conservative-first management algorithm (F006) |
| [41731784](https://pubmed.ncbi.nlm.nih.gov/41731784/) | Prospective cohort | IPL efficacy (F006) |
| [42367702](https://pubmed.ncbi.nlm.nih.gov/42367702/) | Case series | Intralesional 5-FU (F006) |
| [34379160](https://pubmed.ncbi.nlm.nih.gov/34379160/) | Review | Prognosis, MGD link, biopsy rule (F007, F008, F009) |
| [34054469](https://pubmed.ncbi.nlm.nih.gov/34054469/) | Case report | Eyelid necrosis complication (F007) |
| [14762403](https://pubmed.ncbi.nlm.nih.gov/14762403/) | Histopath series (n=1060) | Malignancy masquerade rate 1.4% (F008) |
| [32788569](https://pubmed.ncbi.nlm.nih.gov/32788569/), [25258508](https://pubmed.ncbi.nlm.nih.gov/25258508/), [11417345](https://pubmed.ncbi.nlm.nih.gov/11417345/), [16008694](https://pubmed.ncbi.nlm.nih.gov/16008694/) | Case reports/series | Sebaceous carcinoma masquerade (F008) |
| [22592706](https://pubmed.ncbi.nlm.nih.gov/22592706/), [38337403](https://pubmed.ncbi.nlm.nih.gov/38337403/), [33967173](https://pubmed.ncbi.nlm.nih.gov/33967173/) | Reviews/study | Blepharitis/MGD predisposition; lid hygiene (F009) |
| [32622681](https://pubmed.ncbi.nlm.nih.gov/32622681/) | Primary-care review | Clinical presentation/management (F007) |

---

## Limitations and Knowledge Gaps

1. **Weak trial evidence.** The strongest sources are Cochrane reviews that repeatedly conclude there is **insufficient RCT evidence** for or against standard treatments; much guidance rests on expert opinion, case series, and observational data.
2. **External hordeolum specifically excluded from key reviews.** The Cochrane hordeolum reviews restricted themselves to *internal* hordeolum and **explicitly excluded external hordeola** — so the highest-quality synthesis does not directly cover the target disease. Much of the actionable evidence is extrapolated.
3. **Incidence is a lower bound.** The Japanese figure (56.2/100,000) counts *invasive treatments*, not all cases; true community incidence is far higher since most styes are self-treated.
4. **No molecular architecture.** No genetic, transcriptomic, proteomic, metabolomic, epigenomic, single-cell, or model-organism data exist — sections 4, 14, and 15 are legitimately "not applicable," but this reflects absence of study rather than proven absence of biology.
5. **Emerging iatrogenic signals are new and small.** The CFTR-modulator and tirzepatide associations rest on case series and warrant confirmation.

## Proposed Follow-up Experiments / Actions

1. **Dedicated external-hordeolum RCT** comparing warm compresses ± topical antibiotics vs lid hygiene vs early IPL, with standardized OSDI and recurrence endpoints — directly addressing the Cochrane evidence gap.
2. **Prospective Demodex-stratified cohort** to test whether anti-Demodex lid hygiene (e.g., tea-tree/terpinen-4-ol regimens) reduces recurrent external-hordeola incidence.
3. **Pharmacovigilance analysis** (FAERS/national registries) to quantify the hordeolum signal for CFTR modulators and GLP-1/GIP agonists and define dose/duration relationships.
4. **Microbiome/culture study** of external-hordeolum drainage to confirm *S. aureus* dominance, MSSA/MRSA proportions, and any role for the lid-margin microbiome in recurrence.
5. **Diagnostic-accuracy study of noninvasive meibography** as a triage tool to flag atypical lesions needing biopsy, aiming to reduce missed sebaceous carcinoma.
6. **Knowledge-base curation:** explicitly record "not applicable" for genetic/omics/model-organism fields with F010 as the supporting evidence item, to prevent spurious downstream inference.

---

*Report compiled from 10 confirmed findings and 40 reviewed papers across 5 investigation iterations. Evidence source types span human clinical (systematic reviews, registries, cohorts, case series/reports); no model-organism, in vitro, or computational disease models exist for this acquired infectious condition.*


## Artifacts

- [OpenScientist final report](External_Hordeolum-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](External_Hordeolum-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 31 |
| On topic | 20 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 4 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0025421` (1 mention) - the report calls it "Eyelid pain, approximate"; HP calls it **Pneumomediastinum**
- `HP:0000198` (1 mention) - the report calls it "Abnormal eyelid morphology"; HP calls it **Absence of Stensen duct**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0001642` (2 mentions) - the report calls it "external hordeolum"; MONDO calls it **hordeolum externum**