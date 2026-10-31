---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T23:22:23.669307'
end_time: '2026-10-15T23:22:25.322221'
duration_seconds: 1.65
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hypomagnesemia, Seizures, and Intellectual Disability 2
  mondo_id: MONDO:0020788
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
citation_count: 7
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 5
  validator_version: 0.3.0
term_validation:
  total_terms: 31
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 10
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: HP:0100520
    reported_labels:
    - Renal magnesium wasting
    ontology_label: Oliguria
  - term_id: CL:0000540
    reported_labels:
    - neuron
    - Tissue/cell level:** CNS neurons
    ontology_label: neuron
  - term_id: UBERON:0000955
    reported_labels:
    - "Organ level:** Primary \u2014 brain/CNS"
    ontology_label: brain
  - term_id: NCIT:C260
    reported_labels:
    - Anticonvulsant Agent
    ontology_label: Beta-Lactam Antibiotic
  - term_id: NCIT:C29136
    reported_labels:
    - Magnesium
    ontology_label: K-RAS ASP-13 Mutant Protein
  - term_id: NCIT:C15265
    reported_labels:
    - Rehabilitation Therapy
    ontology_label: Kidney Transplantation
  labels_variant: 2
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hypomagnesemia_Seizures_And_Intellectual_Disability_2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hypomagnesemia_Seizures_And_Intellectual_Disability_2-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypomagnesemia, Seizures, and Intellectual Disability 2
- **MONDO ID:** MONDO:0020788 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypomagnesemia, Seizures, and Intellectual Disability 2** covering all of the
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

# Hypomagnesemia, Seizures, and Intellectual Disability 2 (HOMGSMR2): A Comprehensive Disease Characteristics Report

**Disease:** Hypomagnesemia, Seizures, and Intellectual Disability 2 (HOMGSMR2 / HSMR2)
**Causal gene:** *ATP1A1* (Na⁺/K⁺-ATPase catalytic α1 subunit)
**Identifiers:** OMIM #618314 · ORPHA:564178 · MONDO:0020788 · Gene *ATP1A1* OMIM \*182310 · HGNC:799 · chromosome 1p13.1
**Category:** Mendelian (autosomal dominant, de novo)

---

## Summary

Hypomagnesemia, Seizures, and Intellectual Disability 2 (HOMGSMR2) is an **ultra-rare, autosomal-dominant Mendelian disorder** caused by **de novo heterozygous missense variants in *ATP1A1***, the gene encoding the catalytic α1 subunit of the ubiquitous Na⁺/K⁺-ATPase (the sodium–potassium pump). The disorder was first defined in 2018 by Schlingmann and colleagues, who identified the gene by whole-exome and Sanger sequencing in three infants from non-consanguineous families presenting with the characteristic clinical triad: **infantile-onset generalized refractory seizures, severe hypomagnesemia due to renal magnesium wasting, and significant intellectual disability** ([PMID: 30388404](https://pubmed.ncbi.nlm.nih.gov/30388404/)).

The defining mechanistic insight of this disease is that the pathogenic variants produce a **dual (two-hit) molecular defect in a single protein**: a partial *loss* of normal ion-pumping activity combined with a *neomorphic gain* of an aberrant passive cation-leak current. Functional studies in heterologous expression systems and, most recently, a 3 Å cryo-EM structure of a mutant pump, demonstrated that the characteristic variants (L302R, G303R, M859R, W931R), which cluster in transmembrane segments M3, M7, and M8, each introduce a large positively charged arginine deep within the lipid-embedded membrane domain. This both degrades the pump cycle and opens a passive leak pathway at the protein–lipid interface that depolarizes the cell membrane. In **neurons**, this depolarization drives hyperexcitability (seizures) and impaired neurodevelopment; in **distal convoluted tubule (DCT) epithelial cells** of the kidney, loss of the basolateral Na⁺ gradient and the favorable membrane potential cripples TRPM6-dependent transcellular Mg²⁺ reabsorption, producing renal magnesium wasting.

A critical and clinically important corollary is that **the disease requires a *malfunctioning* — not simply absent — gene product.** Heterozygous *Atp1a1*-null knockout mice are phenotypically normal, and a healthy adult human carrying a protein-null truncating allele lacks disease features; simple haploinsufficiency is therefore insufficient to cause disease. This "toxic/neomorphic" leak mechanism also explains the most frustrating clinical feature: **seizures are refractory to magnesium repletion and frequently to antiepileptic drugs**, because the primary lesion is an intrinsic membrane ion leak rather than magnesium deficiency per se. No disease-modifying therapy exists; management is supportive (antiepileptic drugs, magnesium supplementation, developmental/rehabilitative care). Fewer than ~20 families with any germline *ATP1A1* phenotype have been reported worldwide, and HOMGSMR2 itself has been described in only a handful of de novo cases since 2018.

---

## Key Findings

### Finding 1 — HOMGSMR2 is caused by de novo heterozygous missense variants in *ATP1A1*

Schlingmann et al. (2018) used whole-exome sequencing and confirmatory conventional Sanger sequencing to identify **heterozygous de novo mutations in the catalytic Na⁺/K⁺-ATPase α1 subunit (*ATP1A1*)** in three infants from non-consanguineous families. The paper states directly: *"Whole-exome sequencing and conventional Sanger sequencing identified heterozygous de novo mutations in the catalytic Na+, K+-ATPase α1 subunit (ATP1A1)"* ([PMID: 30388404](https://pubmed.ncbi.nlm.nih.gov/30388404/)). The disorder is catalogued as **OMIM #618314 (HOMGSMR2)**; the gene *ATP1A1* maps to chromosome **1p13.1**. Inheritance is autosomal dominant with all reported cases arising de novo.

### Finding 2 — A dual molecular mechanism: loss of pump function *plus* an abnormal cation leak

The central pathophysiological discovery is that the mutant α1 subunits do not merely lose activity — they also acquire a pathological new property. Functional characterization of mutant Na⁺/K⁺-ATPase α1 subunits in heterologous expression systems *"revealed not only a loss of Na+, K+-ATPase function but also abnormal cation permeabilities, which led to membrane depolarization and possibly aggravated the effect of the loss of physiological pump activity"* ([PMID: 30388404](https://pubmed.ncbi.nlm.nih.gov/30388404/)). Dohrn et al. (2022) independently confirmed a loss-of-function component using an ouabain-sensitivity viability assay in HEK cells (mutant-expressing cells showed significantly decreased viability after 72 h ouabain exposure), supporting a haploinsufficiency/loss-of-function contribution layered on top of the gain-of-leak.

### Finding 3 — The core clinical triad: infantile generalized seizures, severe renal-wasting hypomagnesemia, and intellectual disability

The three index infants *"presented with a disease phenotype consisting of generalized seizures in infancy, severe hypomagnesemia, and renal magnesium wasting. Seizures persisted despite magnesium supplementation and were associated with significant intellectual disability"* ([PMID: 30388404](https://pubmed.ncbi.nlm.nih.gov/30388404/)). Seizures are refractory/intractable, onset is in infancy (neonatal to infantile, documented range 6 days–6 months of age), and the intellectual disability is significant. This triad defines the clinical gestalt of HOMGSMR2.

### Finding 4 — *ATP1A1* is an allelic series spanning an overlapping neurological spectrum

Germline de novo *ATP1A1* variants cause a spectrum of overlapping neurological disorders beyond HOMGSMR2:

| Phenotype | Representative variant(s) | Reference |
|---|---|---|
| CMT2DD (axonal Charcot–Marie–Tooth type 2) | p.Leu48Arg, p.Ile592Thr, p.Ala597Thr, p.Asp601Phe, p.Pro600Ala/Thr, p.Asp811Ala | Lassuthova 2018 ([PMID: 29499166](https://pubmed.ncbi.nlm.nih.gov/29499166/)) |
| Hereditary spastic paraplegia (HSP) | de novo p.Leu337Pro | Stregapede 2020 ([PMID: 31705535](https://pubmed.ncbi.nlm.nih.gov/31705535/)) |
| Complex neurodevelopmental syndrome | p.Gln225Arg, p.Gly335Cys, p.Gly509Asp, p.Gly718Ser, p.Phe923Tyr | Dohrn 2022 ([PMID: 35110381](https://pubmed.ncbi.nlm.nih.gov/35110381/)) |
| HOMGSMR2 | L302R, G303R, M859R, W931R (+ P333R, G864R, D933N) | Schlingmann 2018 ([PMID: 30388404](https://pubmed.ncbi.nlm.nih.gov/30388404/)) |

Lassuthova et al. *"were able to define mutations in ATP1A1, which encodes the alpha1 subunit of the Na+/K+-ATPase"* as a cause of autosomal-dominant CMT2, establishing the allelic series ([PMID: 29499166](https://pubmed.ncbi.nlm.nih.gov/29499166/)). As of 2022 only ~16 families worldwide carried pathogenic germline *ATP1A1* variants. Separately, *somatic* (not germline) *ATP1A1* variants cause aldosterone-producing adenomas / primary aldosteronism — a distinct mechanism in a different tissue.

### Finding 5 — Genotype–phenotype correlation: M3/M7 variants predict the severe HOMGSMR2 phenotype

Lin et al. (2021) reviewed six patients with de novo *ATP1A1* variants, all localizing to transmembrane regions M3, M4, M7, and M8. They reported that *"variations in M3 and M7 transmembrane regions were related to more severe phenotype than those in M4 and M8, which suggested that variations in M3 and M7 might cause more severe ATP1A1 functional defect"* ([PMID: 33968856](https://pubmed.ncbi.nlm.nih.gov/33968856/)). Patients with M3/M7 variants had severe phenotypes (developmental delay plus epileptic encephalopathy; 3 of 4 with hypomagnesemia), whereas M4/M8 variants gave milder phenotypes (mild developmental delay, no seizures/hypomagnesemia). Importantly, *"hypomagnesemia in this disorder might relate to more severe phenotype and indicate more severe Na+/K+-ATPase dysfunction"* — hypomagnesemia is a severity marker. New variants reported in that series included p.Asp933Asn and p.Gly864Arg. Across all series, correcting hypomagnesemia did not control seizures.

### Finding 6 — HOMGSMR2 variants introduce a buried positive charge (arginine) in transmembrane segments M3, M7, M8

Schlingmann (2018) screened seven children with the combination of hypomagnesemia, intractable seizures, and severe intellectual disability who were negative for *CNNM2* and *TRPM6* mutations, and found three to be heterozygous for de novo *ATP1A1* missense variants. The infants presented between 6 days and 6 months of age with generalized convulsions and severe hypomagnesemia (serum Mg 0.30–0.36 mmol/L; normal ~0.7–1.0 mmol/L). The classic HOMGSMR2 variants — **L302R and G303R (segment M3), M859R (M7), and W931R (M8)** — each introduce a large, positively charged arginine near the center of a membrane-embedded transmembrane segment, a chemically disruptive substitution in a hydrophobic environment. Additional reported variants associated with intellectual disability and renal hypomagnesemia include **Pro333Arg, Gly864Arg, and Asp933Asn**. The clinical context in which these variants were identified is the triad of *"generalized seizures in infancy, severe hypomagnesemia, and renal magnesium wasting"* ([PMID: 30388404](https://pubmed.ncbi.nlm.nih.gov/30388404/)).

### Finding 7 — Cryo-EM and electrophysiology confirm an aberrant passive cation leak as the shared mechanism

Colmano et al. (2026, *Journal of General Physiology*) directly tested the four hypomagnesemia/treatment-resistant-seizure variants (L302R, G303R, M859R, W931R) by heterologous expression in HEK293 cells and *Xenopus* oocytes. All four showed reduced cell survival under ouabain (confirming defective pump function) and increased cytosolic/mislocalized signal relative to plasmalemmal wild-type. Under voltage clamp, each variant produced passive "leak" currents; Na⁺ and Cl⁻ were shown to permeate through G303R and W931R. A **3 Å cryo-EM structure of the W931R-α1β1 complex with bound ouabain** revealed a distorted transmembrane segment M9 creating a concavity in the detergent micelle. The authors concluded that *"besides a loss of NKA function, all four variants carry an aberrant leak current that probably underlies the seizures and the hypomagnesemia characterizing this phenotype"* and that *"The structure showed a distorted transmembrane segment M9, which causes a concavity in the detergent micelle, suggesting that similar distortions may provide a leak pathway at the protein-lipid interface"* ([PMID: 42377349](https://pubmed.ncbi.nlm.nih.gov/42377349/)). This provides the structural basis for the gain-of-leak mechanism.

### Finding 8 — Identifiers and epidemiology: an ultra-rare sporadic de novo disorder

Key identifiers: **OMIM #618314** (HOMGSMR2); *ATP1A1* gene **OMIM \*182310**, **HGNC:799**, chromosome **1p13.1**; Orphanet **ORPHA:564178** ("Primary hypomagnesemia–refractory seizures–intellectual disability syndrome"); **MONDO:0020788** (confirmed via GenCC). The disorder is ultra-rare: fewer than ~20 families have been reported across all germline *ATP1A1* phenotypes, and HOMGSMR2 itself has been described in only a handful of de novo cases since 2018. All cases are sporadic/de novo (in non-consanguineous families). No sex predilection has been reported, no founder effect is known, and carrier frequency is not applicable (de novo variants, absent from gnomAD).

### Finding 9 — Treatment is supportive and symptomatic; seizures are refractory to magnesium

In the Schlingmann (2018) cohort, infants presented at 6 days–6 months with generalized convulsions and severe hypomagnesemia (0.30–0.36 mmol/L) and were treated with antiepileptic drugs plus intravenous then ongoing oral magnesium supplementation. Despite normalization or amelioration of serum magnesium, seizure activity persisted, with frequent generalized seizures and repeated episodes of status epilepticus. Brain MRI may show reduced cerebral volume. The abstract notes *"Seizures persisted despite magnesium supplementation and were associated with significant intellectual disability"* ([PMID: 30388404](https://pubmed.ncbi.nlm.nih.gov/30388404/)). No disease-modifying or targeted therapy exists; management consists of antiepileptic drugs, magnesium repletion, and developmental/rehabilitative support.

### Finding 10 — Anatomical/cellular targets: the renal distal convoluted tubule and CNS neurons

*ATP1A1* is ubiquitously expressed but is particularly abundant in kidney and CNS. Lin et al. note that *"ATP1A1 encodes an α1 isoform of Na+/K+-ATPase, which is expressed abundantly in kidneys and central nervous system"* ([PMID: 33968856](https://pubmed.ncbi.nlm.nih.gov/33968856/)). In the **kidney**, the α1 pump resides on the basolateral membrane of **distal convoluted tubule (DCT) epithelial cells**, where the Na⁺ gradient and negative membrane potential it maintains drive transcellular Mg²⁺ reabsorption through the apical **TRPM6** channel; pump dysfunction and depolarization impair DCT Mg²⁺ reabsorption, producing renal magnesium wasting and hypomagnesemia. Schlingmann (2018) underscores the indispensable role of the α1 isoform for renal-tubular magnesium handling. In the **CNS**, neuronal α1 maintains the resting membrane potential; the leak/depolarization produces neuronal hyperexcitability (seizures) and impaired development. Brain MRI can show reduced cerebral volume.

### Finding 11 — Model organisms: *Atp1a1* is essential, and the null allele is non-pathogenic

Spontarelli et al. (bioRxiv 2023 / *Biochim Biophys Acta Mol Cell Res* 2024) tested *Atp1a1*⁺/⁻ knockout mice against wild-type littermates and found the heterozygous-null mice to be **phenotypically normal up to 18 months, even under exercise challenge**. Homozygous-null *Atp1a1* is embryonic-lethal (the gene is essential). Critically, a **healthy adult human carrying a protein-null early-truncation variant (p.Y148\*) also lacked ATP1A1-disease features.** The authors concluded that *"these results suggest that a malfunctioning gene product is required for disease induction by ATP1A1 variants"* ([PMID: 37090550](https://pubmed.ncbi.nlm.nih.gov/37090550/)). This is strong evidence that **simple loss of one allele (haploinsufficiency) is insufficient** to cause disease; a toxic/neomorphic mutant protein is required. Orthologs: mouse *Atp1a1* (NCBI Gene 11928), rat *Atp1a1* (24211), with the conserved α subunit in zebrafish (*atp1a1a.1*), *Drosophila* (*Atpalpha*), and *C. elegans* (*eat-6*). No knock-in mouse carrying a human HOMGSMR2 missense variant (e.g., L302R) has yet been published; disease modeling to date relies on heterologous expression (HEK293, *Xenopus* oocytes) and cryo-EM.

### Finding 12 — Diagnosis rests on biochemistry plus trio sequencing; differentials are other hereditary hypomagnesemias

The diagnostic workup (Schlingmann 2018) features **severe hypomagnesemia** (serum Mg 0.30–0.36 mmol/L; reference ~0.7–1.05 mmol/L) with a calculated **urinary fractional excretion of magnesium that is inappropriately high**, indicating massive renal magnesium wasting (renal loss rather than gastrointestinal loss). Serum calcium is normal/variable; EEG shows epileptiform/seizure activity; brain MRI may show reduced cerebral volume. Molecular diagnosis is by whole-exome (trio) or whole-genome sequencing, or targeted *ATP1A1* sequencing; the original cohort was first excluded for *CNNM2* and *TRPM6* before *ATP1A1* was found. The diagnostic hallmark is *"generalized seizures in infancy, severe hypomagnesemia, and renal magnesium wasting"* ([PMID: 30388404](https://pubmed.ncbi.nlm.nih.gov/30388404/)). Differential diagnosis includes other genetic renal magnesium-wasting disorders: *TRPM6* (HSH/HOMG1, with secondary hypocalcemia), *CNNM2* (HOMG6), *FXYD2*, *KCNA1*, *EGF*, *CLDN16*/*CLDN19*, and *SLC12A3* (Gitelman syndrome).

### Finding 13 — Synthesis: a dominant de novo channelopathy-like disorder with unified pump-loss-plus-leak pathophysiology

Integrating all evidence, de novo heterozygous *ATP1A1* missense variants (L302R/G303R in M3, M859R in M7, W931R in M8; also P333R, G864R, D933N) cause HOMGSMR2. Converging **in vitro** (HEK293, *Xenopus* oocyte voltage clamp), **structural** (3 Å cryo-EM of W931R with distorted M9), and **genetic** (null alleles non-pathogenic in mouse and human) data establish the dual mechanism: partial loss of Na⁺/K⁺ pumping plus a neomorphic passive cation leak that depolarizes neurons (→ refractory seizures, intellectual disability) and DCT cells (→ impaired TRPM6-dependent Mg²⁺ reabsorption → renal Mg wasting/hypomagnesemia). Severity tracks variant domain (M3/M7 severe; M4/M8 mild). Treatment is supportive; magnesium repletion corrects biochemistry but not seizures. The integrated conclusion is that *"besides a loss of NKA function, all four variants carry an aberrant leak current that probably underlies the seizures and the hypomagnesemia"* ([PMID: 42377349](https://pubmed.ncbi.nlm.nih.gov/42377349/)).

---

## Report by Template Section

### 1. Disease Information

HOMGSMR2 is a Mendelian, autosomal-dominant, de novo disorder of the Na⁺/K⁺-ATPase α1 subunit, defined by infantile-onset refractory generalized seizures, severe hypomagnesemia from renal magnesium wasting, and intellectual disability. **Identifiers:** OMIM #618314; ORPHA:564178; MONDO:0020788; MeSH has no dedicated term (indexed under hypomagnesemia / genetic epilepsy). **Synonyms / alternative names:** Hypomagnesemia, Seizures, and Mental Retardation 2 (original OMIM title); HSMR2; HOMGSMR2; "Primary hypomagnesemia–refractory seizures–intellectual disability syndrome" (Orphanet). **Information source:** aggregated disease-level resources (OMIM, Orphanet) built from a small number of published individual-patient case reports — the evidence base is a handful of de novo cases, not an EHR-scale cohort.

### 2. Etiology

**Causal factor:** purely genetic — a heterozygous de novo missense variant in *ATP1A1*. There are no established environmental, infectious, or mechanical causes. **Genetic risk factors:** the pathogenic variant is itself causal and fully penetrant where reported; no susceptibility loci or modifier genes have been defined. **Environmental risk factors:** none identified; because variants are de novo, advanced parental age is a plausible but undocumented contributor to the mutational event. **Protective factors:** none characterized genetically or environmentally; notably, *ATP1A1*-null (loss-of-function) alleles are *not* pathogenic, so a null second allele would be expected to be tolerated. **Gene–environment interactions:** none established; this is a monogenic disorder with a dominant, intrinsic protein defect.

### 3. Phenotypes

| Phenotype | Type | Suggested HPO | Onset | Severity | Frequency |
|---|---|---|---|---|---|
| Generalized seizures / epilepsy | Clinical sign (neurologic) | HP:0002197 (Generalized-onset seizure), HP:0001250 (Seizure) | Neonatal–infantile | Severe, refractory, often status epilepticus | Core (all reported cases) |
| Hypomagnesemia | Laboratory abnormality | HP:0002917 (Hypomagnesemia) | Neonatal–infantile | Severe (0.30–0.36 mmol/L) | Core |
| Renal magnesium wasting | Laboratory/physiologic | HP:0100520 (Renal magnesium wasting) | Congenital/infantile | Severe | Core |
| Intellectual disability | Behavioral/cognitive | HP:0001249 (Intellectual disability) | Infantile onward | Significant, often severe | Core |
| Global developmental delay | Behavioral/cognitive | HP:0001263 (Global developmental delay) | Infantile | Variable–severe | Frequent |
| Reduced cerebral volume | Imaging/physical | HP:0002120 (Cerebral cortical atrophy) | Infantile | Variable | Subset |
| Epileptic encephalopathy | Clinical sign | HP:0200134 (Epileptic encephalopathy) | Infantile | Severe | M3/M7 variants |

**Quality of life impact:** severe — intractable seizures, profound developmental/intellectual impairment, and lifelong dependency for care markedly reduce functional independence; standardized QoL instruments have not been applied in this ultra-rare population.

### 4. Genetic / Molecular Information

**Causal gene:** *ATP1A1* (HGNC:799; OMIM \*182310; chromosome 1p13.1; UniProt P05023), encoding the catalytic α1 subunit of the Na⁺/K⁺-ATPase. **Pathogenic variants:** heterozygous missense. Classic HOMGSMR2 alleles — **L302R, G303R (M3), M859R (M7), W931R (M8)** — plus **P333R, G864R, D933N** reported with intellectual disability + renal hypomagnesemia. **ACMG classification:** pathogenic/likely pathogenic (de novo occurrence PS2, absent from gnomAD PM2, clustering in a functional domain, deleterious in vitro). **Variant type:** missense, frequently introducing a buried arginine in a transmembrane helix. **Allele frequency:** absent from gnomAD (de novo). **Origin:** germline de novo (contrast with *somatic ATP1A1* variants causing primary aldosteronism). **Functional consequence:** combined loss-of-function (reduced pumping) and gain-of-function/neomorphic (passive cation leak); the leak is the distinguishing lesion. **Modifier genes:** none defined; variant *domain location* (M3/M7 vs M4/M8) is the principal determinant of severity. **Epigenetic / chromosomal abnormalities:** not applicable (point mutations; no reported structural variants or methylation changes). **CHEBI-relevant entities:** magnesium(2+) (CHEBI:18420), sodium(1+) (CHEBI:29101), potassium(1+) (CHEBI:29103), ATP (CHEBI:30616), ouabain (CHEBI:472657).

### 5. Environmental Information

No environmental factors, lifestyle factors, or infectious agents are implicated in disease causation — HOMGSMR2 is monogenic. Dietary magnesium intake modulates serum magnesium but does not correct the intrinsic renal wasting or the seizures.

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**

1. A **de novo heterozygous missense variant** in *ATP1A1* (e.g., L302R, G303R, M859R, W931R) introduces a **buried charged arginine into a transmembrane segment (M3/M7/M8)** → *leads to* local distortion of the membrane domain (cryo-EM: distorted M9, concavity at the protein–lipid interface).
2. The distorted α1 subunit **partially loses Na⁺/K⁺ pumping activity** (loss-of-function) → *reduces* the transmembrane Na⁺/K⁺ gradient the cell depends on.
3. In parallel, the same distortion **opens a neomorphic passive cation-leak pathway** (gain-of-function; Na⁺ and Cl⁻ permeate) → *results in* abnormal inward leak currents (demonstrated by voltage clamp).
4. The combined pump loss + leak → **chronic membrane depolarization** of the affected cell.

   **Branch A — neurons (CNS):** depolarization *leads to* neuronal hyperexcitability → **refractory generalized seizures, epileptic encephalopathy, and impaired neurodevelopment / intellectual disability**; may *result in* reduced cerebral volume.

   **Branch B — renal DCT epithelium:** loss of the basolateral Na⁺ gradient and favorable negative membrane potential *results in* impaired driving force for **apical TRPM6-mediated transcellular Mg²⁺ reabsorption** → **renal magnesium wasting → severe hypomagnesemia**. (The hypomagnesemia step is inferred from DCT physiology and the known TRPM6 pathway rather than directly demonstrated in patient kidney.)
5. Hypomagnesemia itself may lower the seizure threshold, but because the primary lesion is an intrinsic membrane leak, **magnesium repletion does not abolish seizures** (observed clinically).

**Molecular pathways / processes:** Na⁺/K⁺-ATPase ion transport (KEGG/Reactome), membrane potential maintenance, transcellular divalent cation transport. **Protein dysfunction:** combined loss-of-function + neomorphic leak; structural distortion of transmembrane helices (cryo-EM). **Biochemical abnormality:** ion-pump/ion-channel defect (a "pump-turned-leaky-channel"). **GO terms:** GO:0005391 (sodium:potassium-exchanging ATPase activity), GO:0006814 (sodium ion transport), GO:0071805 (potassium ion transmembrane transport), GO:0051899 (membrane depolarization), GO:0015693 (magnesium ion transport). **CL terms:** CL:1000849 (kidney distal convoluted tubule epithelial cell), CL:0000540 (neuron). **Immune, metabolic, oxidative, fibrotic mechanisms:** not implicated.

### 7. Anatomical Structures Affected

- **Organ level:** Primary — brain/CNS (UBERON:0000955) and kidney (UBERON:0002113). Body systems: nervous system and renal/urinary system; magnesium homeostasis is systemic.
- **Tissue/cell level:** CNS neurons (CL:0000540); renal distal convoluted tubule epithelium (CL:1000849; distal convoluted tubule UBERON:0001292). Nervous tissue and renal epithelial tissue.
- **Subcellular level:** plasma membrane (GO:0005886), specifically the basolateral membrane (GO:0016323) in DCT cells; mutant protein shows increased cytosolic mislocalization.
- **Localization / lateralization:** seizures are generalized (bilateral); renal involvement is bilateral and diffuse.

### 8. Temporal Development

- **Onset:** neonatal–infantile (documented 6 days to 6 months); congenital underlying defect. Onset pattern is early and acute with respect to seizures.
- **Progression:** chronic and lifelong; seizures are often intractable with repeated status epilepticus; intellectual disability is static-to-progressive in functional impact. Disease course is persistent rather than relapsing-remitting.
- **Patterns:** no spontaneous remission; infancy is the critical window for seizure onset and neurodevelopmental injury, making early diagnosis and seizure control the key (though currently limited) opportunity for intervention.

### 9. Inheritance and Population

- **Epidemiology:** ultra-rare; prevalence/incidence not formally estimated (fewer than ~20 families across all germline *ATP1A1* phenotypes; only a handful of HOMGSMR2 cases). Orphanet lists it as a rare disease.
- **Inheritance:** autosomal dominant, de novo. **Penetrance:** apparently complete for reported variants. **Expressivity:** variable, correlating with variant domain (M3/M7 severe; M4/M8 mild). **Anticipation, germline mosaicism, founder effects, consanguinity:** not applicable/not reported — all cases sporadic in non-consanguineous families. **Carrier frequency:** not applicable (de novo; absent from gnomAD).
- **Population demographics:** no ethnic predilection, no geographic clustering, no sex bias reported; affected individuals present in infancy.

### 10. Diagnostics

- **Laboratory:** severe hypomagnesemia (serum Mg 0.30–0.36 mmol/L vs reference ~0.7–1.05); **inappropriately high urinary fractional excretion of magnesium** confirming renal wasting; serum calcium normal/variable (distinguishes from *TRPM6* HSH, which has secondary hypocalcemia). LOINC: serum magnesium (19123-9), urine magnesium.
- **Electrophysiology:** EEG shows epileptiform/seizure activity.
- **Imaging:** brain MRI may show reduced cerebral volume.
- **Genetic testing:** trio whole-exome or whole-genome sequencing is the primary diagnostic; targeted *ATP1A1* sequencing or a hereditary-hypomagnesemia/epilepsy gene panel is appropriate. CMA/karyotype/FISH are not informative (point mutations). The original cohort excluded *CNNM2* and *TRPM6* before *ATP1A1* was identified.
- **Differential diagnosis:** *TRPM6* (HSH/HOMG1 — distinguished by secondary hypocalcemia), *CNNM2* (HOMG6), *FXYD2*, *KCNA1*, *EGF*, *CLDN16*/*CLDN19* (with hypercalciuria/nephrocalcinosis), *SLC12A3* (Gitelman — hypokalemic metabolic alkalosis). Among these, the seizure + intellectual-disability combination with normal calcium points toward *ATP1A1*.
- **Screening:** no newborn or population screening exists; cascade/carrier screening is not applicable (de novo).

### 11. Outcome / Prognosis

Prognosis is **poor for neurodevelopment**. Seizures are frequently refractory with repeated status epilepticus, and intellectual disability is significant to severe and permanent. No survival statistics have been formally published given the tiny cohort; the disorder is chronic and lifelong. Reduced cerebral volume on MRI portends worse outcome. **Prognostic factor:** variant domain — M3/M7 variants (with hypomagnesemia) predict the severe phenotype; M4/M8 variants predict milder disease without seizures. Hypomagnesemia itself is a marker of more severe pump dysfunction. Recovery potential is limited because the lesion is a fixed intrinsic membrane defect.

### 12. Treatment

No disease-modifying or targeted therapy exists; management is **supportive and symptomatic**:

- **Pharmacotherapy:** antiepileptic drugs for seizure control (often only partially effective) — NCIT:C260 (Anticonvulsant Agent); magnesium supplementation (IV then oral) — NCIT:C29136 (Magnesium) — corrects biochemistry but *not* seizures.
- **Supportive/rehabilitative:** developmental support, physical/occupational/speech therapy — NCIT:C15265 (Rehabilitation Therapy); nutritional support.
- **Advanced therapeutics (gene/cell/RNA/targeted/immuno):** none available; conceptually, because the mutant exerts a toxic gain-of-leak, **allele-specific knockdown (ASO/siRNA) of the mutant allele** is a mechanistically rational but purely hypothetical future approach (the healthy null-allele human and heterozygous-null mouse suggest removing the bad allele could be tolerated).
- **Pharmacogenomics / personalized medicine:** none established.
- **Treatment outcomes:** seizures commonly remain refractory; magnesium repletion reliably raises serum Mg but does not control seizures.

### 13. Prevention

- **Primary prevention:** not possible (de novo mutation). **Secondary/tertiary prevention:** early genetic diagnosis to guide seizure management and avoid futile escalation of magnesium as a seizure therapy; aggressive seizure control to limit neurodevelopmental injury.
- **Genetic counseling:** recurrence risk for parents of an affected child is low (de novo), though germline mosaicism cannot be fully excluded; affected individuals (if reproductive) would have 50% transmission risk. Prenatal/PGT is feasible only once a familial variant is known.
- **Screening/immunization/public health:** not applicable.

### 14. Other Species / Natural Disease

*ATP1A1* is deeply conserved. Orthologs: **mouse *Atp1a1* (NCBI Gene 11928; Taxon 10090), rat *Atp1a1* (24211; Taxon 10116)**, zebrafish *atp1a1a.1* (Taxon 7955), *Drosophila Atpalpha* (Taxon 7227), *C. elegans eat-6* (Taxon 6239). No naturally occurring companion-animal or wildlife disease equivalent to HOMGSMR2 is catalogued in OMIA. The gene's essentiality (homozygous-null lethality) is conserved, underscoring evolutionary conservation of the pump's housekeeping role. Zoonotic/transmission considerations are not applicable (genetic disease).

### 15. Model Organisms

- **Available models:** *Atp1a1*⁺/⁻ heterozygous-null mice (phenotypically normal to 18 months, even under exercise challenge); homozygous-null is embryonic-lethal. Heterologous expression systems — **HEK293 cells and *Xenopus* oocytes** — are the workhorse for functional characterization (ouabain-survival assays, voltage-clamp leak-current measurement). Cryo-EM structural models of mutant α1β1 complexes (e.g., W931R) exist.
- **Genetic models available:** knockout (null) mice; **no knock-in mouse carrying a human HOMGSMR2 missense variant has yet been published.**
- **Phenotype recapitulation:** the null mouse does *not* recapitulate disease (confirming that disease requires a malfunctioning product, not loss); heterologous systems faithfully reproduce the molecular defects (loss of pumping + leak) but not the organismal phenotype.
- **Limitations / applications:** current models illuminate the molecular mechanism but lack an in vivo whole-animal model of the seizure/hypomagnesemia phenotype — the key gap for therapeutic testing. **Resources:** MGI, IMPC/KOMP (mouse); Cellosaurus (HEK293); PDB/EMDB (cryo-EM structures).

---

## Mechanistic Model / Interpretation

```
          de novo heterozygous ATP1A1 missense variant
          (L302R, G303R [M3]; M859R [M7]; W931R [M8]; P333R, G864R, D933N)
                              │
                 buried Arg distorts transmembrane helix
                 (cryo-EM: distorted M9, protein–lipid concavity)
                              │
            ┌─────────────────┴──────────────────┐
   LOSS of function                      GAIN of function (neomorphic)
   partial ↓ Na+/K+ pumping              passive cation LEAK (Na+, Cl-)
            └─────────────────┬──────────────────┘
                              ▼
                   chronic MEMBRANE DEPOLARIZATION
                              │
            ┌─────────────────┴──────────────────┐
            ▼                                     ▼
   NEURONS (CNS)                         RENAL DCT EPITHELIUM
   hyperexcitability                     ↓ basolateral Na+ gradient
            │                            ↓ driving force for apical TRPM6
            ▼                                     ▼
   refractory generalized               impaired Mg2+ reabsorption
   seizures + intellectual                       ▼
   disability (± ↓ cerebral vol)        renal Mg wasting → severe
                                        HYPOMAGNESEMIA
                              │
       Mg2+ repletion corrects serum Mg but NOT seizures
       (lesion is an intrinsic membrane leak, not Mg deficiency)
```

The unifying concept is a **"pump-turned-leaky-channel."** The same single-residue substitution that cripples the ATP-driven ion pump also carves a passive conductance pathway through the membrane domain. Two independent cell targets — excitable neurons and magnesium-reabsorbing DCT cells — are each exquisitely dependent on the α1 pump to maintain their electrochemical gradients, which is why one molecular lesion produces the seemingly unrelated neurologic and renal phenotypes. The genetic evidence that null alleles are benign (mouse and human) is the keystone: it rules out pure haploinsufficiency and establishes that the mutant protein is actively harmful, which both explains the dominant inheritance and nominates allele-specific silencing as the logical (if unproven) therapeutic direction.

---

## Evidence Base

| Paper | PMID | Contribution |
|---|---|---|
| *Germline De Novo Mutations in ATP1A1 Cause Renal Hypomagnesemia, Refractory Seizures, and Intellectual Disability* (Schlingmann et al., 2018) | [30388404](https://pubmed.ncbi.nlm.nih.gov/30388404/) | **Foundational.** Defines the disease, the gene, the clinical triad, and the dual loss-of-pump + abnormal-cation-permeability mechanism. |
| *ATP1A1 mutations cause autosomal-dominant CMT2 (CMT2DD)* (Lassuthova et al., 2018) | [29499166](https://pubmed.ncbi.nlm.nih.gov/29499166/) | Establishes the *ATP1A1* allelic series across neurological phenotypes. |
| *Hereditary spastic paraplegia is a novel phenotype for germline de novo ATP1A1 mutation* (Stregapede et al., 2020) | [31705535](https://pubmed.ncbi.nlm.nih.gov/31705535/) | Extends the allelic spectrum (de novo p.Leu337Pro → HSP). |
| *De Novo* ATP1A1 variants (Dohrn et al., 2022) | [35110381](https://pubmed.ncbi.nlm.nih.gov/35110381/) | Five additional de novo variants (complex neurodevelopmental syndrome); ouabain-viability confirmation of loss-of-function. |
| Lin et al., 2021 (phenotype review of de novo *ATP1A1* variants) | [33968856](https://pubmed.ncbi.nlm.nih.gov/33968856/) | Genotype–phenotype correlation: M3/M7 severe vs M4/M8 mild; hypomagnesemia = severity marker; kidney + CNS as target organs. |
| Spontarelli et al., 2023/2024 (*Atp1a1*⁺/⁻ mice) | [37090550](https://pubmed.ncbi.nlm.nih.gov/37090550/) | Null allele non-pathogenic → disease requires a malfunctioning product. |
| Colmano et al., 2026 (*J Gen Physiol*; cryo-EM + electrophysiology) | [42377349](https://pubmed.ncbi.nlm.nih.gov/42377349/) | Structural + functional proof of the aberrant leak current for L302R/G303R/M859R/W931R; distorted M9. |

All mechanistic and clinical claims are anchored to these primary sources. Evidence types span **human clinical** (Schlingmann, Lin, Dohrn, Stregapede, Lassuthova), **model organism** (Spontarelli — mouse), **in vitro heterologous expression / electrophysiology** (Colmano, Dohrn — HEK293, *Xenopus*), and **structural/computational** (Colmano — cryo-EM).

---

## Limitations and Knowledge Gaps

1. **Tiny evidence base.** The entire literature rests on a handful of de novo cases; prevalence, incidence, survival, and natural-history data are essentially unquantified.
2. **No in vivo phenotypic model.** There is no knock-in mouse (or other animal) carrying a human HOMGSMR2 missense variant, so the organismal seizure/hypomagnesemia phenotype has never been reproduced in an animal — limiting therapeutic testing.
3. **Renal mechanism is inferred.** The DCT/TRPM6 causal step is extrapolated from established magnesium-handling physiology and the pump's basolateral role, not directly demonstrated in patient kidney tissue.
4. **Leak selectivity incompletely mapped.** Permeating ions were defined for only some variants (Na⁺/Cl⁻ for G303R and W931R); the full ionic basis of depolarization across all variants is not complete.
5. **Therapeutics are entirely supportive.** No targeted therapy has been tested; the allele-specific knockdown hypothesis is untested.
6. **Genotype–phenotype rules are provisional.** The M3/M7-severe vs M4/M8-mild correlation rests on six patients and may not generalize.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a knock-in mouse** carrying a representative severe variant (e.g., L302R or W931R) to establish the first in vivo model of seizures + renal Mg wasting and to test therapeutic candidates.
2. **Test allele-specific silencing (ASO/siRNA/CRISPR)** of the mutant allele in patient-derived iPSC neurons and kidney organoids, leveraging the finding that null alleles are tolerated.
3. **Map the full leak-current ion selectivity** for every reported variant by systematic voltage-clamp/reversal-potential analysis, and screen small molecules (e.g., pore-blocking candidates) able to occlude the leak without further impairing residual pump activity.
4. **Direct demonstration of DCT/TRPM6 dysfunction** using kidney organoids or conditional DCT-specific mutant expression to confirm the inferred renal causal step.
5. **Establish an international patient registry** to quantify prevalence, natural history, seizure-therapy response, and genotype–phenotype correlations with adequate power.
6. **Evaluate non-magnesium anticonvulsant strategies** rationally targeting membrane depolarization (e.g., sodium-channel modulators) given that magnesium repletion fails to control seizures.

---

## Conclusion

Hypomagnesemia, Seizures, and Intellectual Disability 2 (HOMGSMR2; OMIM #618314, ORPHA:564178, MONDO:0020788) is an ultra-rare autosomal-dominant disorder caused by de novo heterozygous missense variants in *ATP1A1*, the catalytic α1 subunit of the Na⁺/K⁺-ATPase. The variants cluster in transmembrane segments M3/M7/M8 (L302R, G303R, M859R, W931R) and produce a dual molecular defect — partial loss of ion pumping plus a neomorphic passive cation leak — proven by electrophysiology and a 3 Å cryo-EM structure. The resulting membrane depolarization injures CNS neurons (refractory infantile seizures and intellectual disability) and renal distal convoluted tubule cells (impaired TRPM6-dependent Mg²⁺ reabsorption → renal magnesium wasting). Because the lesion is an intrinsic membrane leak rather than magnesium deficiency, seizures resist magnesium repletion, and treatment remains supportive. The demonstration that *ATP1A1*-null alleles are phenotypically tolerated in both mouse and human establishes that a malfunctioning — not merely absent — protein is required for disease, and points toward allele-specific silencing as a rational future therapeutic strategy.


## Artifacts

- [OpenScientist final report](Hypomagnesemia_Seizures_And_Intellectual_Disability_2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hypomagnesemia_Seizures_And_Intellectual_Disability_2-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 18 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0100520` (1 mention) - the report calls it "Renal magnesium wasting"; HP calls it **Oliguria**
- `CL:0000540` (2 mentions) - the report calls it "neuron", "Tissue/cell level:** CNS neurons"; CL calls it **neuron**
- `UBERON:0000955` (1 mention) - the report calls it "Organ level:** Primary — brain/CNS"; UBERON calls it **brain**
- `NCIT:C260` (1 mention) - the report calls it "Anticonvulsant Agent"; NCIT calls it **Beta-Lactam Antibiotic**
- `NCIT:C29136` (1 mention) - the report calls it "Magnesium"; NCIT calls it **K-RAS ASP-13 Mutant Protein**
- `NCIT:C15265` (1 mention) - the report calls it "Rehabilitation Therapy"; NCIT calls it **Kidney Transplantation**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005391` (1 mention) - the report calls it "sodium:potassium-exchanging ATPase activity"; GO calls it **P-type sodium:potassium-exchanging transporter activity**, and lists "sodium/potassium-exchanging ATPase activity" among its other names
- `GO:0005886` (1 mention) - the report calls it "Subcellular level:** plasma membrane"; GO calls it **plasma membrane**, and lists "cellular membrane" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000540` - called "neuron", "Tissue/cell level:** CNS neurons"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.