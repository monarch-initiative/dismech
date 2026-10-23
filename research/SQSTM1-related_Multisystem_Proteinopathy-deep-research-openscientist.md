---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-12T14:48:28.892515'
end_time: '2026-10-12T15:17:59.747794'
duration_seconds: 1770.86
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: SQSTM1-related Multisystem Proteinopathy
  mondo_id: MONDO:0800464
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
citation_count: 25
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 25
  on_topic: 16
  validator_version: 0.3.0
term_validation:
  total_terms: 33
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 28
  labels_matching: 19
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0800464
    reported_labels:
    - disease
    ontology_label: SQSTM1-related multisystem proteinopathy
  - term_id: HP:0002661
    reported_labels:
    - Paget disease of bone
    ontology_label: Painless fractures due to injury
  - term_id: HP:0031605
    reported_labels:
    - Vertical gaze palsy
    ontology_label: Abnormal fundus pigmentation
  - term_id: NCIT:C1455
    reported_labels:
    - Bisphosphonate
    ontology_label: Conjugate Vaccine
  - term_id: NCIT:C575
    reported_labels:
    - Dexamethasone
    ontology_label: Immunotoxin
  - term_id: NCIT:C17007
    reported_labels:
    - genetic testing
    ontology_label: Positron Emission Tomography
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: SQSTM1-related_Multisystem_Proteinopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: SQSTM1-related_Multisystem_Proteinopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SQSTM1-related Multisystem Proteinopathy
- **MONDO ID:** MONDO:0800464 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SQSTM1-related Multisystem Proteinopathy** covering all of the
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

# SQSTM1-related Multisystem Proteinopathy (MSP3): A Comprehensive Disease Characterization

**MONDO ID:** MONDO:0800464 · **OMIM:** 616887 (MSP3) · **Gene:** *SQSTM1*/p62 (HGNC:11280; NCBI Gene 8878; UniProt Q13501; chr5q35) · **Category:** Mendelian
**Report type:** Disease knowledge-base characterization · **Evidence base:** 10 confirmed findings, 60 papers reviewed

---

## Summary

**SQSTM1-related multisystem proteinopathy (MSP3)** is a dominantly inherited, adult-onset, pleiotropic disorder caused by germline variants in *SQSTM1*, the gene encoding the autophagy receptor/signaling scaffold **p62/sequestosome-1**. A single genetic lesion produces a remarkably variable clinical spectrum: **inclusion body/distal myopathy (IBM/MRV)**, **amyotrophic lateral sclerosis (ALS)**, **frontotemporal dementia (FTD)**, and **Paget disease of bone (PDB)**, unified pathologically by p62- and TDP-43–positive protein aggregates and rimmed vacuoles. Most pathogenic variants cluster in the **ubiquitin-associated (UBA) domain**, with **p.P392L (c.1175C>T)** the single most common allele across populations ([PMID: 17229007](https://pubmed.ncbi.nlm.nih.gov/17229007/)).

Mechanistically, the disease **branches from one p62 lesion into two arms**. A **gain-of-function bone arm** operates through enhanced RANK→NF-κB signaling that drives osteoclast overactivity and pagetic bone remodeling — but this arm is **incompletely penetrant and requires an environmental "second hit"** (paramyxoviral measles nucleocapsid protein acting via IL-6), as demonstrated in knock-in mice ([PMID: 24339057](https://pubmed.ncbi.nlm.nih.gov/24339057/)). A **loss-of-function neuromuscular arm** reflects impaired selective autophagy and mitophagy, causing TDP-43 aggregation and degeneration of muscle and motor/cortical neurons. Strikingly, **biallelic loss-of-function** of the *same* gene produces a completely distinct **recessive childhood-onset neurodegeneration** with ataxia, dystonia, and vertical gaze palsy (DNECAS) ([PMID: 27545679](https://pubmed.ncbi.nlm.nih.gov/27545679/)).

The clinical and prognostic bottom line is **organ-dependent**: the bone arm is largely **benign and highly treatable/preventable** with zoledronic acid — including genotype-guided prophylaxis that prevented new lesions in a randomized trial of *SQSTM1* carriers ([PMID: 38123339](https://pubmed.ncbi.nlm.nih.gov/38123339/)) — whereas the neuromuscular arms (ALS/FTD, distal myopathy, childhood neurodegeneration) are **progressive, life-limiting, and lack disease-modifying therapy**. A rare but grave complication of the bone arm is malignant (osteosarcoma/giant-cell) transformation in <1% of polyostotic PDB, often associated with a *ZNF687* second-hit genotype ([PMID: 32106343](https://pubmed.ncbi.nlm.nih.gov/32106343/)).

---

## Key Findings

### Finding 1 — SQSTM1 causes a pleiotropic multisystem proteinopathy spanning IBM, ALS, FTD, and Paget disease of bone

Heterozygous *SQSTM1* variants produce a clinical spectrum encompassing **inclusion body myopathy (IBM), motor neuron disease/ALS, frontotemporal dementia (FTD), and Paget disease of bone (PDB)**, unified by shared **TDP-43– and p62-positive aggregate pathology** and **rimmed vacuoles**. *SQSTM1* is formally designated **MSP3 (OMIM 616887)**, one of a family of MSP genes that also includes *VCP*, *HNRNPA2B1*, and *HNRNPA1*.

As the landmark MSP review states: *"Mutations in VCP, HNRNPA2B1, HNRNPA1, and SQSTM1, encoding RNA-binding proteins or proteins in quality-control pathways, cause multisystem proteinopathies (MSP). They share pathological findings of protein aggregation and clinical combinations of inclusion body myopathy (IBM), neurodegeneration [motor neuron disorder (MND)/frontotemporal dementia (FTD)], and Paget disease of bone (PDB)"* ([PMID: 36861178](https://pubmed.ncbi.nlm.nih.gov/36861178/)). In the Mayo Clinic MSP cohort, *SQSTM1*+*TIA1* accounted for 5 of 31 MSP individuals.

Demographically, a Chinese MSP cohort of 953 ALS/IBM/dementia patients identified 29 carriers of MSP-gene variants, with onset predominantly in the 3rd–5th decade and strong male predominance: *"Most patients were male (72.4%), with disease onset predominantly in the third to fifth decades of life. The majority of patients (21/29) presented with a single clinical phenotype"* ([PMID: 41737544](https://pubmed.ncbi.nlm.nih.gov/41737544/)). The fact that **most patients present with a single phenotype** is central to the disease's clinical reality — full multisystem co-occurrence in one individual is the exception, not the rule.

**Ontology anchors:** MONDO:0800464 (disease); HP:0003198 (Myopathy); HP:0007354 (Amyotrophic lateral sclerosis); HP:0002145 (Frontotemporal dementia); HP:0002661 (Paget disease of bone).

### Finding 2 — Pathogenic SQSTM1 variants cluster in the UBA domain and impair selective autophagy with NF-κB activation

In familial PDB, **all 14 initially reported *SQSTM1* mutations affect the ubiquitin-associated (UBA) domain**, with **P392L** the most prevalent, present in both familial and sporadic cases across populations: *"The 14 mutations reported in SQSTM1/p62 all affect the ubiquitin-associated domain of the protein. The P392L mutation is the most commonly observed mutation in PDB patients"* ([PMID: 17229007](https://pubmed.ncbi.nlm.nih.gov/17229007/)).

Functionally, the p62 protein is a multidomain scaffold: it binds ubiquitinated cargo via the UBA domain, LC3 via its LIR motif (acting as a selective autophagy receptor), and sequesters KEAP1 to activate the NFE2L2/Nrf2 antioxidant response. Pathogenic variants disrupt this machinery. Studies of the **p.R321C** variant demonstrate the dual mechanism: *"In vitro studies associated the p62-321C variant with a blockade of autophagy and with the activation of the NF-kB pathway"* ([PMID: 40374720](https://pubmed.ncbi.nlm.nih.gov/40374720/)). A humanized p62-321C mouse developed stimulus-induced seizures, CNS p62/cFos changes, and degenerating spinal motor neurons.

**Ontology anchors:** GO:0005515 (protein binding); GO:0061136 (regulation of proteasomal protein catabolic process); GO:0000421 (autophagosome membrane); GO:0038061 (NIK/NF-κB signaling). Protein: UniProt Q13501, UBA domain residues ~389–434.

### Finding 3 — Biallelic SQSTM1 loss-of-function causes a distinct recessive childhood-onset neurodegeneration (DNECAS)

In sharp mechanistic contrast to the dominant adult disease, **biallelic (recessive) loss of p62** produces a childhood/adolescence-onset neurodegenerative disorder. Haack et al. *"identified three different biallelic loss-of-function variants in SQSTM1 in nine affected individuals from four families with a childhood- or adolescence-onset neurodegenerative disorder characterized by gait abnormalities, ataxia, dysarthria, dystonia, vertical gaze palsy, and cognitive decline"* ([PMID: 27545679](https://pubmed.ncbi.nlm.nih.gov/27545679/)).

Affected fibroblasts showed **complete absence of p62 protein** and investigators *"found evidence of a defect in the early response to mitochondrial depolarization and autophagosome formation"* ([PMID: 27545679](https://pubmed.ncbi.nlm.nih.gov/27545679/)) — directly implicating a **mitophagy/autophagy-initiation defect**. A novel homozygous frameshift (c.790del) was subsequently reported in childhood-onset progressive neurodegeneration with ataxia and gaze palsy ([PMID: 35957775](https://pubmed.ncbi.nlm.nih.gov/35957775/)).

**Ontology anchors:** HP:0001251 (Ataxia); HP:0001332 (Dystonia); HP:0031605 (Vertical gaze palsy); HP:0100543 (Cognitive impairment); GO:0000423 (mitophagy).

### Finding 4 — Epidemiology: SQSTM1 is the most common PDB gene; PDB prevalence ~1–2% in older adults but declining, male-predominant, with strong geographic variation

Paget disease of bone, the most frequent *SQSTM1*-associated phenotype, affects **~1–2% of adults over 55** in high-prevalence regions (UK, Western Europe), with marked geographic clustering (highest in NW England) and a **continuing secular decline**. In the UK, *"the overall standardized incidence decreased from 0.75/10,000 person-years in 1999 to 0.20/10,000 person-years in 2015"* ([PMID: 33742666](https://pubmed.ncbi.nlm.nih.gov/33742666/)).

Prevalence is far lower in Asian populations. In South Korea, researchers reported *"a mean prevalence of 1.20 per 100,000 and an age-adjusted incidence ranging from 0.38 to 1.26 per 100,000 person-years"* ([PMID: 39906256](https://pubmed.ncbi.nlm.nih.gov/39906256/)). PDB is **male-predominant and strongly age-dependent**, with crude incidence rising from ~0.04–0.07/10,000/yr at age 45–49 to 3.7–6.3/10,000/yr at ≥85.

The **full SQSTM1-MSP syndrome** (neuromuscular + bone) is much rarer than isolated PDB: MSP overall was found in only 3.0% (29/953) of a Chinese ALS/IBM/dementia cohort, and a Japanese nationwide survey ascertained only 47 MSP patients ([PMID: 38287512](https://pubmed.ncbi.nlm.nih.gov/38287512/)). The secular decline and a **rural/livestock (cattle density)** association point to an environmental contribution: *"A moderately positive correlation (R2 = 0.236) was identified between PDB incidence and the density of female breeding cattle"* ([PMID: 40408225](https://pubmed.ncbi.nlm.nih.gov/40408225/)).

| Population / Region | Metric | Value | Source |
|---|---|---|---|
| UK (1999) | Standardized incidence | 0.75 / 10,000 PY | [PMID: 33742666](https://pubmed.ncbi.nlm.nih.gov/33742666/) |
| UK (2015) | Standardized incidence | 0.20 / 10,000 PY | [PMID: 33742666](https://pubmed.ncbi.nlm.nih.gov/33742666/) |
| South Korea | Mean prevalence | 1.20 / 100,000 | [PMID: 39906256](https://pubmed.ncbi.nlm.nih.gov/39906256/) |
| South Korea | Age-adjusted incidence | 0.38–1.26 / 100,000 PY | [PMID: 39906256](https://pubmed.ncbi.nlm.nih.gov/39906256/) |
| China (MSP cohort) | MSP among ALS/IBM/dementia | 29/953 (3.0%) | [PMID: 41737544](https://pubmed.ncbi.nlm.nih.gov/41737544/) |
| Japan | Nationwide MSP patients | 47 | [PMID: 38287512](https://pubmed.ncbi.nlm.nih.gov/38287512/) |

### Finding 5 — Treatment: Zoledronic acid durably controls SQSTM1-associated PDB, and genetic-test-guided prophylaxis can prevent bone lesions

Intravenous **zoledronic acid** (an aminobisphosphonate; NCIT:C1699) is the mainstay for the bone component. In a long-term retrospective cohort, biochemical response favored treatment strongly: *"Primary outcome was more prevalent in the ZOL compared to the NZOL group [42 patients (88%) VS 11 patients (52%) respectively, P = 0.004]"* ([PMID: 38555314](https://pubmed.ncbi.nlm.nih.gov/38555314/)), with sustained normalization of alkaline phosphatase.

Most importantly, the **ZiPP/PREVENT-PDB randomized trial** of 222 *SQSTM1*-pathogenic-variant carriers showed that **prophylactic zoledronic acid prevented new bone lesions**: *"Eight of the placebo group had a poor outcome (lesions which were new, unchanged or progressing) compared with none of the ZA group (OR 0.08, 95% CI 0.00 to 0.42, p=0.003)"* over a median 84 months ([PMID: 38123339](https://pubmed.ncbi.nlm.nih.gov/38123339/)). This is a rare example of **genotype-guided precision prevention** in a Mendelian disease.

The acute phase response (fever, myalgia) after zoledronate can be attenuated by a short course of dexamethasone ([PMID: 36970850](https://pubmed.ncbi.nlm.nih.gov/36970850/)). By contrast, **no disease-modifying therapy exists** for the myopathy/ALS/FTD components, which are managed supportively (physiotherapy, occupational therapy, respiratory care).

**Ontology anchors:** NCIT:C1699 (Zoledronic Acid); NCIT:C1455 (Bisphosphonate); NCIT:C575 (Dexamethasone); CHEBI:46557 (zoledronic acid).

### Finding 6 — TIA1/SQSTM1 digenic late-onset distal myopathy defines a homogeneous SQSTM1 muscle phenotype, with SQSTM1 acting as a modifier

The muscle arm of *SQSTM1* disease is frequently **digenic**. Co-inheritance of **TIA1 p.Asn357Ser** and **SQSTM1 p.Pro392Leu** produces a strikingly homogeneous phenotype: *"These twenty-four patients (75% males) had late-onset (52,6 ± 10,1 years), mainly asymmetric, distal ankle and hand finger extension weakness (75%), mild CK elevation (82.4%) and myopathic EMG"* ([PMID: 39142003](https://pubmed.ncbi.nlm.nih.gov/39142003/)).

The TIA1 allele is enriched in distal myopathy panels and is proposed as a genetic modifier: *"We confirm an increased burden of the TIA1 p.Asn357Ser variant in distal myopathy patients which could act as a genetic modifier"* ([PMID: 39142003](https://pubmed.ncbi.nlm.nih.gov/39142003/)). An independent Spanish report confirmed that *"a similar phenotype has been attributed to the digenic inheritance of TIA1 c.1070A>G (p.Asn357Ser) and SQSTM1 c.1175C>T (p.Pro392Leu) variants"* ([PMID: 38016875](https://pubmed.ncbi.nlm.nih.gov/38016875/)). Muscle biopsy shows rimmed vacuoles (combined 44–83%) with p62/TDP-43 aggregates. Notably, *SQSTM1* can also cause **proximal** myopathy with rimmed vacuoles via a frameshift variant, broadening the muscle phenotype ([PMID: 36998782](https://pubmed.ncbi.nlm.nih.gov/36998782/)).

**Ontology anchors:** HP:0003693 (Distal amyotrophy); HP:0003805 (Rimmed vacuoles); HP:0003236 (Elevated circulating creatine kinase); HP:0003458 (EMG: myopathic abnormalities); HP:0030319 (Finger extensor weakness).

### Finding 7 — Mutant p62 potentiates RANK-induced NF-κB activation and osteoclastogenesis (bone arm) and accelerates ALS progression (neuro arm)

On the **bone side**, PDB-associated p62 mutants act by **gain-of-function on NF-κB**: *"p62 mutants increased NF-kappaB activation and significantly potentiated osteoclast formation and bone resorption in human primary cell cultures"* ([PMID: 16813535](https://pubmed.ncbi.nlm.nih.gov/16813535/)). This study described a novel **K378X** truncation causing a severe polyostotic phenotype alongside P392L and E396X.

On the **neurodegeneration side**, *SQSTM1* missense variants span the PB1, TRAF6-binding, PEST, and UBA domains and **worsen prognosis**. In a Chinese ALS cohort, *"the ΔFS analysis revealed that the risk of death or tracheostomy was significantly increased in SQSTM1 mutation carriers (p < 0.05)"* ([PMID: 25708934](https://pubmed.ncbi.nlm.nih.gov/25708934/)). Neuropathologically, p62 immunohistochemistry reliably labels TDP-43–positive and C9RANT-positive neuronal cytoplasmic inclusions in FTLD/ALS tissue.

**Ontology anchors:** GO:0038061 (NIK/NF-κB signaling); GO:0045670 (regulation of osteoclast differentiation); CL:0000092 (osteoclast); CL:0000100 (motor neuron).

### Finding 8 — Diagnostic workup is organ-specific

Diagnosis depends on which arm is manifest:

- **Bone arm (PDB):** Usually detected incidentally via isolated **elevated serum total/bone alkaline phosphatase** (elevated in ~90% of PDB; LOINC 6768-6) or on radiographs. *"Most cases of PDB are diagnosed incidentally on radiographs or as an isolated elevation of serum alkaline phosphatase... Diagnosis is made on the basis of typical radiological features on plain films, while a radionuclide bone scan may be used to assess the extent of disease"* ([PMID: 33543158](https://pubmed.ncbi.nlm.nih.gov/33543158/)). Pathognomonic radiographic features include cortical thickening, medullary expansion, osteolytic "blade of grass" fronts, and mixed lytic-sclerotic skull; histology shows mosaic cement lines. Bone-turnover markers (CTX, P1NP) are elevated.
- **Neuromuscular arm:** Requires **needle EMG** (myopathic ± neurogenic), **muscle MRI** (distal fatty replacement, e.g., medial gastrocnemius), and **muscle biopsy**: *"Muscle biopsy showed rimmed vacuoles (44.4%), myofibrillar disorganization (16.7%) or both (38.9%), with P62/TDP43 aggregates"* ([PMID: 39142003](https://pubmed.ncbi.nlm.nih.gov/39142003/)).
- **Definitive diagnosis is molecular:** Targeted *SQSTM1* sequencing or multigene MSP/ALS/distal-myopathy NGS panels (including *TIA1*), with WES/WGS for atypical cases.

**Ontology anchors:** LOINC 6768-6 (Alkaline phosphatase); NCIT:C17007 (genetic testing); HP:0003236 (elevated CK).

### Finding 9 — Mouse models show p62 P394L (= human P392L) causes osteoclast RANKL-hyperresponsiveness but requires a second hit for full Paget lesions

The gene-environment nature of the bone arm is directly demonstrated in mice. *"We generated p62(P394L) knock-in mice (p62KI) and found that although OCL numbers were increased, the mice did not develop pagetic lesions. However, mice expressing both MVNP and p62KI developed more exuberant pagetic lesions than mice expressing MVNP alone"* ([PMID: 24339057](https://pubmed.ncbi.nlm.nih.gov/24339057/)). The downstream mediator is IL-6: *"Interleukin-6 (IL-6) production is essential for the pagetic phenotype, because transgenic mice with MVNP targeted to OCLs develop pagetic OCLs and lesions, but this phenotype is absent when MVNP mice are bred to IL-6(-/-) mice"* ([PMID: 24339057](https://pubmed.ncbi.nlm.nih.gov/24339057/)).

This explains **incomplete, age-dependent penetrance** of PDB: the p62 UBA mutation primes osteoclasts to RANKL but, alone, is insufficient; a paramyxoviral/inflammatory "second hit" acting through IL-6 is needed for full lesions. Available model systems therefore include: **p62(P394L) knock-in mice** (bone), the **humanized p62-R321C mouse** (CNS: seizures, motor-neuron degeneration; [PMID: 40374720](https://pubmed.ncbi.nlm.nih.gov/40374720/)), **Sqstm1/p62-null mice** (mitophagy defect; models the biallelic human phenotype), and **patient fibroblasts/iPSC** and **RAW264.7 osteoclast cultures**.

**Ontology anchors:** NCBI Taxon 10090 (*Mus musculus*); MGI *Sqstm1*; CL:0000092 (osteoclast); GO:0032635 (interleukin-6 production).

### Finding 10 — Prognosis is organ-specific: PDB arm usually benign/treatable but <1% undergo osteosarcoma transformation; neuro arm is progressive and life-limiting

Most *SQSTM1*-associated PDB is **mild and monostotic** (77% monostotic; only 3% fracture in one cohort) and controllable with bisphosphonates. Complications include bone pain, deformity, fractures, deafness (skull involvement), compression neuropathy/spinal cord compromise, secondary osteoarthritis, and high-output cardiac states.

The gravest bone complication is **malignant transformation**: *"Neoplastic transformation is a rare but serious complication of Paget's disease of bone (PDB), occurring in fewer than 1% of individuals with polyostotic disease. Their prognosis is poor, with less than 50% surviving 5 years"* ([PMID: 32106343](https://pubmed.ncbi.nlm.nih.gov/32106343/)). Spinal pagetic osteosarcoma has a 5-year survival as low as 10% ([PMID: 42359209](https://pubmed.ncbi.nlm.nih.gov/42359209/)). Transformation is associated with a **germline ZNF687 P937R founder mutation** and **dual SQSTM1+ZNF687 genotypes** — a case report documented *"genetic testing confirming dual SQSTM1 and ZNF687 mutations"* ([PMID: 41630218](https://pubmed.ncbi.nlm.nih.gov/41630218/)).

In contrast, the **neuromuscular components are relentlessly progressive**: distal myopathy causes slowly progressive disability over 10+ years; SQSTM1-ALS carriers have accelerated decline and shortened survival ([PMID: 25708934](https://pubmed.ncbi.nlm.nih.gov/25708934/)); FTD and the biallelic childhood neurodegeneration are progressive and fatal.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

**Shared initiating lesion:**
1. A germline *SQSTM1* variant (most commonly a **UBA-domain missense, e.g., p.P392L**) **alters p62 function** → impairs ubiquitin-cargo binding and p62's dual role as autophagy receptor and signaling scaffold ([PMID: 17229007](https://pubmed.ncbi.nlm.nih.gov/17229007/)).

The pathway then **branches** according to cell type, gene dose (mono- vs biallelic), and environment:

**BRANCH A — Bone (gain-of-function, environment-gated):**
2A. Mutant p62 **potentiates RANK→NF-κB signaling** in osteoclast precursors ([PMID: 16813535](https://pubmed.ncbi.nlm.nih.gov/16813535/)) → **leads to** osteoclast RANKL-hyperresponsiveness and increased osteoclast number.
3A. Alone this is **insufficient** (p62KI mice do not develop lesions) → a **second hit** (paramyxoviral MVNP; inferred from epidemiologic measles/livestock associations) **acts via IL-6** ([PMID: 24339057](https://pubmed.ncbi.nlm.nih.gov/24339057/)) → **results in** exuberant, disorganized bone remodeling.
4A. **Leads to** focal accelerated bone turnover → cortical thickening, medullary expansion, deformity, fractures, deafness → clinical **Paget disease of bone**.
5A. Rarely (<1%, often with a *ZNF687* second hit) → **malignant transformation to osteosarcoma** ([PMID: 32106343](https://pubmed.ncbi.nlm.nih.gov/32106343/)).

**BRANCH B — Neuromuscular (loss-of-function / impaired autophagy):**
2B. Mutant p62 **blocks selective autophagy and impairs mitophagy** ([PMID: 40374720](https://pubmed.ncbi.nlm.nih.gov/40374720/)) → **leads to** accumulation of ubiquitinated cargo and damaged mitochondria.
3B. **Results in** cytoplasmic **TDP-43 and p62 aggregation** with rimmed vacuoles in myofibers and neurons ([PMID: 39142003](https://pubmed.ncbi.nlm.nih.gov/39142003/)).
4B. Co-modifier alleles (e.g., **TIA1 p.N357Ser**) lower the threshold → **digenic distal myopathy** ([PMID: 39142003](https://pubmed.ncbi.nlm.nih.gov/39142003/)); in motor/cortical neurons → **ALS/FTD** with accelerated progression ([PMID: 25708934](https://pubmed.ncbi.nlm.nih.gov/25708934/)).

**BRANCH C — Recessive childhood neurodegeneration (complete loss-of-function):**
2C. **Biallelic** LoF → **complete absence of p62 protein** → defective early mitophagy response ([PMID: 27545679](https://pubmed.ncbi.nlm.nih.gov/27545679/)) → **leads to** childhood-onset neurodegeneration with ataxia, dystonia, gaze palsy (DNECAS).

### Branch comparison table

| Feature | Bone arm (PDB) | Neuromuscular arm (IBM/ALS/FTD) | Recessive childhood (DNECAS) |
|---|---|---|---|
| Inheritance | Autosomal dominant | Autosomal dominant (± digenic) | Autosomal recessive |
| Dominant mechanism | Gain-of-function (NF-κB↑) | Loss-of-function (autophagy↓) | Complete LoF (no p62) |
| Variant type | UBA missense (P392L) | Missense across domains; truncating | Biallelic truncating/frameshift |
| Second hit needed | Yes (MVNP/IL-6) | Modifier alleles (TIA1) | No |
| Onset | Older adult (>55) | 3rd–5th decade | Childhood/adolescence |
| Penetrance | Incomplete, age-dependent | Incomplete, variable | High (recessive) |
| Pathology | Mosaic cement lines, osteoclast↑ | p62/TDP-43 aggregates, rimmed vacuoles | Mitophagy defect |
| Prognosis | Benign, treatable | Progressive, life-limiting | Progressive, fatal |
| Therapy | Zoledronic acid (preventable!) | Supportive only | Supportive only |

### ASCII schematic

```
                 SQSTM1 / p62 germline variant
                 (UBA domain, e.g. P392L)
                            |
        +-------------------+--------------------+
        |                                        |
  GAIN-OF-FUNCTION                        LOSS-OF-FUNCTION
  (RANK -> NF-kB up)                      (autophagy/mitophagy down)
        |                                        |
  osteoclast hyper-                      ubiquitin + damaged
  responsiveness                         mitochondria accumulate
        |                                        |
  + MVNP / IL-6  <-- environmental        p62/TDP-43 aggregation
    SECOND HIT        trigger                    |
        |                             +----------+-----------+
  Paget disease of bone               |                      |
        |                        +TIA1 modifier         biallelic LoF
  <1% osteosarcoma               (digenic)                   |
  (+ZNF687)                           |                 childhood
                              distal myopathy /          neurodegeneration
                              IBM / ALS / FTD            (ataxia, gaze palsy)
```

---

## Evidence Base

| PMID | Title (abbreviated) | Supports finding(s) | Evidence type |
|---|---|---|---|
| [36861178](https://pubmed.ncbi.nlm.nih.gov/36861178/) | MSPs and MSP-like disorders: spectrum | F1 (disease definition) | Human clinical / review |
| [41737544](https://pubmed.ncbi.nlm.nih.gov/41737544/) | Chinese MSP genetic spectrum | F1, F4 (demographics) | Human clinical cohort |
| [17229007](https://pubmed.ncbi.nlm.nih.gov/17229007/) | SQSTM1 mutation frequencies/haplotypes | F2 (UBA clustering, P392L) | Human genetics |
| [40374720](https://pubmed.ncbi.nlm.nih.gov/40374720/) | p.R321C CNS abnormalities | F2 (autophagy/NF-κB), F9 (mouse) | In vitro + mouse |
| [27545679](https://pubmed.ncbi.nlm.nih.gov/27545679/) | Biallelic SQSTM1 childhood neurodegeneration | F3 (DNECAS) | Human genetics + fibroblasts |
| [35957775](https://pubmed.ncbi.nlm.nih.gov/35957775/) | Novel c.790del recessive case | F3 | Human case |
| [33742666](https://pubmed.ncbi.nlm.nih.gov/33742666/) | UK PDB declining incidence | F4 (epidemiology) | Epidemiology |
| [39906256](https://pubmed.ncbi.nlm.nih.gov/39906256/) | South Korea PDB epidemiology | F4 | Epidemiology |
| [40408225](https://pubmed.ncbi.nlm.nih.gov/40408225/) | PDB decline & livestock association | F4 (environment) | Epidemiology |
| [38287512](https://pubmed.ncbi.nlm.nih.gov/38287512/) | Japan nationwide MSP survey | F4 | Epidemiology |
| [38555314](https://pubmed.ncbi.nlm.nih.gov/38555314/) | Zoledronic acid long-term effectiveness | F5 (treatment) | Clinical cohort |
| [38123339](https://pubmed.ncbi.nlm.nih.gov/38123339/) | ZiPP/PREVENT-PDB RCT (genotype-guided) | F5 (prevention) | Randomized trial |
| [36970850](https://pubmed.ncbi.nlm.nih.gov/36970850/) | Dexamethasone for zoledronate APR | F5 (adverse-event mgmt) | Randomized trial |
| [39142003](https://pubmed.ncbi.nlm.nih.gov/39142003/) | TIA1/SQSTM1 digenic myopathy landscape | F6, F8 (diagnosis) | Human clinical cohort |
| [38016875](https://pubmed.ncbi.nlm.nih.gov/38016875/) | Digenic TIA1/SQSTM1 Spanish patients | F6 | Human case series |
| [36998782](https://pubmed.ncbi.nlm.nih.gov/36998782/) | Frameshift SQSTM1 proximal MRV | F6 | Human case |
| [16813535](https://pubmed.ncbi.nlm.nih.gov/16813535/) | K378X, NF-κB, osteoclastogenesis | F7 (bone mechanism) | In vitro functional |
| [25708934](https://pubmed.ncbi.nlm.nih.gov/25708934/) | Six SQSTM1 mutations in Chinese ALS | F7, F10 (prognosis) | Human genetics |
| [33543158](https://pubmed.ncbi.nlm.nih.gov/33543158/) | Paget's disease clinical update | F8 (diagnosis) | Clinical review |
| [24339057](https://pubmed.ncbi.nlm.nih.gov/24339057/) | IL-6/MVNP + p62 P394L knock-in mice | F9 (GxE, model) | Mouse model |
| [32106343](https://pubmed.ncbi.nlm.nih.gov/32106343/) | ZNF687 in neoplastic PDB transformation | F10 (prognosis) | Human genetics |
| [41630218](https://pubmed.ncbi.nlm.nih.gov/41630218/) | Spinal PDB malignant transformation | F10 | Human case |
| [42359209](https://pubmed.ncbi.nlm.nih.gov/42359209/) | Pagetic spinal osteosarcoma review | F10 | Clinical review |

**Challenges / nuances:** The *VCP*-focused MSP therapeutic literature (rapamycin/chloroquine, exercise training; e.g. [PMID: 24130765](https://pubmed.ncbi.nlm.nih.gov/24130765/)) is encouraging for the autophagy-targeting concept but is **not SQSTM1-specific**, and one key paper was retracted ([PMID: 25884947](https://pubmed.ncbi.nlm.nih.gov/25884947/)) — it should not be over-extrapolated to *SQSTM1*. The livestock/measles environmental link is **correlational** (R²=0.236) and mechanistically supported only in mice, not proven in human *SQSTM1* carriers.

---

## Section-by-Section Knowledge-Base Content

**1. Disease Information.** Adult-onset dominant multisystem proteinopathy (MSP3, OMIM 616887, MONDO:0800464) plus a distinct recessive pediatric neurodegeneration (DNECAS). Synonyms: *SQSTM1-related MSP*; p62-related myopathy/ALS/FTD/PDB. Information is aggregated from case series, cohorts, and registries (disease-level), not single-patient EHR.

**2. Etiology.** Primary cause: germline *SQSTM1* variants. Genetic risk: UBA-domain missense (P392L most common); modifier *TIA1* p.N357Ser (muscle), *ZNF687* P937R (malignant transformation). Environmental: paramyxovirus (measles/MVNP), rural/cattle exposure, age, male sex. Gene-environment interaction is proven in mice (p62KI requires MVNP/IL-6; [PMID: 24339057](https://pubmed.ncbi.nlm.nih.gov/24339057/)).

**3. Phenotypes.** PDB (HP:0002661), distal amyotrophy (HP:0003693), rimmed vacuoles (HP:0003805), elevated CK (HP:0003236), ALS (HP:0007354), FTD (HP:0002145), ataxia (HP:0001251), dystonia (HP:0001332), gaze palsy (HP:0031605), hearing loss (HP:0000365), cognitive decline (HP:0100543). Onset mostly 3rd–5th decade (neuromuscular) or >55 (bone); childhood for recessive form. Progressive for neuro arm; treatable/stable for bone.

**4. Genetic/Molecular.** *SQSTM1* (HGNC:11280, chr5q35, UniProt Q13501). Variants: missense, nonsense (K378X, E396X), frameshift. Classification per ACMG; P392L pathogenic. Modifier genes: *TIA1*, *ZNF687*. Rare in gnomAD. Germline origin. Functional consequence: gain-of-function (NF-κB/bone) and loss-of-function (autophagy/neuro).

**5. Environmental.** Paramyxovirus/measles nucleocapsid (via IL-6), livestock/rural exposure; secular decline implies modifiable environmental component.

**6. Mechanism.** See causal chain above. Pathways: RANK–NF-κB (KEGG), selective autophagy/mitophagy (GO:0000423), KEAP1-NFE2L2. Cell types: osteoclast (CL:0000092), motor neuron (CL:0000100), skeletal myofiber.

**7. Anatomy.** Bone (UBERON:0001474; skull, spine, pelvis, long bones), skeletal muscle (UBERON:0001134; distal > proximal), spinal cord/motor neurons, frontotemporal cortex, cerebellum. Subcellular: autophagosome (GO:0005776), lysosome, mitochondrion.

**8. Temporal.** Adult/late onset (bone, >55; neuromuscular, 3rd–5th decade), childhood for recessive. Insidious, chronic, progressive (neuro) vs. focal/stable (bone).

**9. Inheritance/Population.** AD (dominant arms), AR (DNECAS), often digenic. Incomplete, age-dependent penetrance. Variable expressivity. PDB ~1–2% in high-prevalence regions, declining; male-predominant; NW England clustering.

**10. Diagnostics.** ALP + bone-turnover markers + radiography/bone scan (bone); EMG + muscle MRI + biopsy with p62/TDP-43 (muscle); molecular *SQSTM1* sequencing / NGS panels (definitive).

**11. Prognosis.** Bone arm benign/treatable, <1% osteosarcoma (poor, <50% 5-yr survival). Neuro arm progressive, life-limiting; ALS carriers have shortened survival.

**12. Treatment.** Zoledronic acid (NCIT:C1699) for PDB — including genotype-guided prophylaxis; dexamethasone for APR; supportive care (PT/OT, respiratory) for neuromuscular arms. No disease-modifying neuro therapy.

**13. Prevention.** Primary/secondary: genetic testing + prophylactic zoledronic acid in *SQSTM1* carriers (proven in ZiPP RCT); genetic counseling; cascade testing. Tertiary: bisphosphonates to prevent deformity/complications.

**14. Other species.** Mouse (NCBI Taxon 10090) ortholog *Sqstm1*; p62(P394L) knock-in and p62-null models. No major naturally occurring animal disease documented.

**15. Model organisms.** p62(P394L) knock-in (bone), humanized p62-R321C (CNS), Sqstm1-null (mitophagy/recessive), patient fibroblasts/iPSC, RAW264.7 osteoclast cultures.

---

## Limitations and Knowledge Gaps

1. **No dedicated SQSTM1-MSP primary dataset was analyzed** — this report synthesizes published literature; all statistics are extracted from cited studies.
2. **Penetrance and genotype-phenotype rules are imprecise.** Why one carrier develops PDB, another ALS, and another nothing is unexplained beyond modifier alleles and environmental hits.
3. **The environmental "second hit" is proven only in mice.** The measles/MVNP-IL-6 axis and livestock correlation (R²=0.236) are not mechanistically confirmed in human *SQSTM1* carriers.
4. **No disease-modifying therapy for the neuromuscular arms.** Autophagy-modulating strategies remain extrapolations from *VCP* models (one key paper retracted).
5. **Cohorts are small and geographically skewed** (Europe, East Asia); carrier frequency, incidence of the full MSP syndrome, and sex ratios for the neuromuscular arms are poorly quantified.
6. **Prognostic biomarkers are lacking** for predicting which carriers will convert to neurodegeneration.

---

## Proposed Follow-up Experiments / Actions

1. **Genotype-phenotype registry:** Pool international *SQSTM1* carriers to estimate arm-specific penetrance, modifier burden (*TIA1*, *ZNF687*), and environmental covariates.
2. **Test the viral second-hit hypothesis in humans:** Serological/PCR studies for paramyxovirus exposure stratified by *SQSTM1* genotype and PDB status.
3. **iPSC-derived osteoclast + motor-neuron isogenic panels** carrying P392L, R321C, and biallelic LoF to dissect the gain- vs loss-of-function branch point quantitatively.
4. **Biomarker discovery:** Longitudinal serum/CSF neurofilament, TDP-43, and bone-turnover markers to predict neuromuscular conversion in asymptomatic carriers.
5. **Therapeutic trials of autophagy enhancers** specifically in *SQSTM1* muscle/neuron models before clinical translation.
6. **Extend prophylaxis evidence:** Longer-term ZiPP follow-up and health-economic analysis to inform guidelines on genotype-guided zoledronic acid.
7. **Screen for ZNF687 co-mutation** in polyostotic *SQSTM1*-PDB patients as a malignant-transformation risk stratifier.

---

*Report compiled from 10 confirmed findings across 5 investigation iterations and 60 reviewed papers. Evidence types span human clinical cohorts, human genetics, in vitro functional assays, mouse models, and epidemiology.*


## Artifacts

- [OpenScientist final report](SQSTM1-related_Multisystem_Proteinopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](SQSTM1-related_Multisystem_Proteinopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 25 |
| On topic | 16 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 28 |
| Terms named correctly | 19 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0800464` (3 mentions) - the report calls it "disease"; MONDO calls it **SQSTM1-related multisystem proteinopathy**
- `HP:0002661` (2 mentions) - the report calls it "Paget disease of bone"; HP calls it **Painless fractures due to injury**
- `HP:0031605` (2 mentions) - the report calls it "Vertical gaze palsy"; HP calls it **Abnormal fundus pigmentation**
- `NCIT:C1455` (1 mention) - the report calls it "Bisphosphonate"; NCIT calls it **Conjugate Vaccine**
- `NCIT:C575` (1 mention) - the report calls it "Dexamethasone"; NCIT calls it **Immunotoxin**
- `NCIT:C17007` (1 mention) - the report calls it "genetic testing"; NCIT calls it **Positron Emission Tomography**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0038061` (2 mentions) - the report calls it "NIK/NF-κB signaling"; GO calls it **non-canonical NF-kappaB signal transduction**, and lists "NIK/NF-kappaB signaling" among its other names
- `HP:0003236` (3 mentions) - the report calls it "Elevated circulating creatine kinase", "elevated CK"; HP calls it **Elevated circulating creatine kinase activity**, and lists "Elevated serum CPK" among its other names
- `HP:0030319` (1 mention) - the report calls it "Finger extensor weakness"; HP calls it **Weakness of facial musculature**, and lists "Face weakness" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0003236` - called "Elevated circulating creatine kinase", "elevated CK"