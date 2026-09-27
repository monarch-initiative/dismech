---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-22T13:15:58.053813'
end_time: '2026-09-22T13:31:46.051875'
duration_seconds: 948.0
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Periventricular Nodular Heterotopia 9
  mondo_id: MONDO:0030061
  category: Disease
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
  quotes_checked: 17
  quotes_valid: 17
  relevance_assessed: 25
  on_topic: 11
  validator_version: 0.2.1
term_validation:
  total_terms: 28
  verified: 27
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 2
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: HP:0001263
    reported_labels:
    - Clinical sign
    ontology_label: Global developmental delay
  - term_id: HP:0001249
    reported_labels:
    - Clinical sign
    ontology_label: Intellectual disability
  - term_id: HP:0002126
    reported_labels:
    - Imaging/structural
    ontology_label: Polymicrogyria
  - term_id: HP:0000252
    reported_labels:
    - Physical
    ontology_label: Microcephaly
  - term_id: HP:0004322
    reported_labels:
    - Physical
    ontology_label: Short stature
  - term_id: HP:0001999
    reported_labels:
    - Physical
    ontology_label: Abnormal facial shape
  - term_id: HP:0000407
    reported_labels:
    - Clinical sign
    ontology_label: Sensorineural hearing impairment
  - term_id: GO:0005874
    reported_labels:
    - microtubules
    - "Subcellular level:** cytoskeleton \u2014 **microtubules"
    ontology_label: microtubule
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Periventricular_Nodular_Heterotopia_9-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Periventricular_Nodular_Heterotopia_9-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Periventricular Nodular Heterotopia 9
- **MONDO ID:** MONDO:0030061 (if available)
- **Category:** Disease

## Research Objectives

Please provide a comprehensive research report on **Periventricular Nodular Heterotopia 9** covering all of the
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

# Periventricular Nodular Heterotopia 9 (PVNH9): A Comprehensive Disease Characterization Report

**Target disease:** Periventricular Nodular Heterotopia 9 (PVNH9)
**MONDO ID:** MONDO:0030061 · **OMIM:** #618918 · **Causal gene:** *MAP1B* (HGNC:6836; 5q13.2)
**Report type:** Disease knowledge-base entry compiled from primary literature (41 papers reviewed, 8 findings confirmed)

---

## Summary

**Periventricular Nodular Heterotopia 9 (PVNH9) is a rare, autosomal dominant malformation of cortical development caused by heterozygous loss-of-function (LoF) variants in *MAP1B*, the gene encoding the neuron-specific microtubule-associated protein 1B.** PVNH is defined by nodular masses of neurons and glia ectopically retained along the walls of the lateral ventricles because they fail to complete radial migration to the cortex. In PVNH9 the nodules are characteristically **frontally (anteriorly) predominant** and are frequently accompanied by **perisylvian polymicrogyria** and **corpus callosum abnormalities**. The clinical presentation typically emerges in childhood and includes **global developmental delay, intellectual disability, focal epilepsy, and behavioural dysregulation**, with variable dysmorphism, microcephaly and short stature reported in some individuals.

The mechanistic basis is well supported across human genetics, mouse genetics, and cell biology. MAP1B crosslinks and stabilizes microtubules, couples microtubules to the actin cytoskeleton, and regulates growth-cone dynamics and axon elongation; it is a downstream effector of Netrin-1 signalling and its translation is repressed by the fragile-X protein FMRP. Heterozygous LoF variants reduce MAP1B mRNA and protein (haploinsufficiency), impairing microtubule stabilization and radial neuronal migration and leaving neurons stranded in periventricular nodules. The founding genome-wide collapsing analysis (Heinzen et al., 2018) implicated *MAP1B* through four ultra-rare LoF variants, and independent families have since confirmed the association, demonstrating **autosomal dominant inheritance with incomplete penetrance and variable expressivity** (one variant was inherited from a parent with previously undiagnosed PVNH).

A striking **allelic dichotomy** distinguishes PVNH9 from another *MAP1B* phenotype: LoF variants cause PVNH-related neurological disease, whereas **missense** variants cause **autosomal dominant nonsyndromic sensorineural hearing loss** (SNHL) without brain malformation, reflecting MAP1B's high expression in cochlear spiral ganglion neurons. There is **no disease-modifying therapy**; management is symptomatic — antiseizure medication for epilepsy (often drug-resistant) and, for refractory focal epilepsy, ablative surgery such as MR-guided laser interstitial thermal therapy (MRgLITT) targeting epileptogenic nodules — alongside developmental, educational and rehabilitative support and genetic counselling.

---

## Key Findings

### Finding 1 — PVNH9 is caused by heterozygous loss-of-function variants in *MAP1B*

PVNH9 (OMIM #618918) is caused by heterozygous mutations in *MAP1B* (microtubule-associated protein 1B; HGNC:6836; chromosome 5q13.2). Multiple independent families with de novo or inherited LoF variants — nonsense, frameshift and splice-site — have been reported. Documented alleles include c.7091dup and c.2035G>T (p.Glu679*). The mechanism is **haploinsufficiency / loss of function**: functional assays demonstrate significantly reduced *MAP1B* mRNA and protein in mutant versus wild-type.

A 2025 report describing a novel *MAP1B* LoF variant states plainly that "*PVNH9 is caused by a heterozygous mutation in the microtubule-associated protein 1B (MAP1B) gene*" and that "*the qPCR and western blot analyses demonstrated significantly reduced mRNA and protein expression, respectively, in the mutant compared with that in the wild-type*" [PMID: 40802165](https://pubmed.ncbi.nlm.nih.gov/40802165/). A de novo nonsense variant, "*a de novo nonsense MAP1B mutation (c.2035G>T, p.Glu679X) detected on whole exome sequencing*," anchors the LoF class [PMID: 31317654](https://pubmed.ncbi.nlm.nih.gov/31317654/). *Evidence source: human clinical + in vitro functional.*

### Finding 2 — Genotype–phenotype correlation: LoF → PVNH; missense → isolated deafness

A review of *MAP1B* genotype–phenotype associations found that **LoF variants** (nonsense, frameshift, splice) predominantly cause **PVNH-related neurological disease** (intellectual disability, epilepsy, developmental delay, dysmorphism), whereas **missense variants** may present with **only deafness** (nonsyndromic SNHL). As stated: "*loss-of-function (LOF) variants in MAP1B mainly lead to PVNH-related neurological symptoms, while patients with missense variants may only present with deafness*" [PMID: 40802165](https://pubmed.ncbi.nlm.nih.gov/40802165/). This dichotomy is mechanistically important: it suggests the two allele classes exert distinct molecular consequences (haploinsufficiency versus a tissue-restricted or altered-function effect). *Evidence source: human clinical review.*

### Finding 3 — Clinical spectrum: anteriorly-predominant PVNH, developmental delay, intellectual disability, epilepsy

In a case series of **7 affected individuals from 3 unrelated families** carrying pathogenic *MAP1B* variants (all LoF), features included global developmental delay, intellectual disability, behavioural dysregulation and focal epilepsy. Neuroimaging revealed **anteriorly (frontally) predominant PVNH in 4 of 5 cases** with imaging available; some patients additionally showed polymicrogyria (PMG) and dysgenesis/agenesis of the corpus callosum. Additional reported features include microcephaly, short stature and dysmorphic facial features.

The primary description reports: "*Clinical features included global developmental delay, intellectual disability, behavioural dysregulation, and focal epilepsy. Neuroimaging revealed anteriorly predominant PVNH in four of five cases*" [PMID: 40874586](https://pubmed.ncbi.nlm.nih.gov/40874586/). An earlier review summarizes the recurrent presentation as "*a phenotype including periventricular nodular heterotopia (PVNH), intellectual disability (ID), seizures, and dysmorphic features*" [PMID: 31317654](https://pubmed.ncbi.nlm.nih.gov/31317654/). *Evidence source: human clinical.*

### Finding 4 — Mechanism: MAP1B is a microtubule stabilizer essential for neuronal migration and axon growth, and is FMRP-regulated

MAP1B is a neuron-specific microtubule-associated protein that crosslinks microtubules and actin filaments, stabilizes microtubules, and controls growth-cone dynamics and axon branching/elongation. It is a **downstream effector of Netrin-1 signalling** (via GSK3/CDK5-dependent phosphorylation); MAP1B-deficient neurons show reduced chemoattractant responses to Netrin-1, and mice show axon-tract and pontine-nuclei defects. **MAP1B translation is repressed by FMRP**, and FMRP regulates postnatal neuronal migration via MAP1B. MAP1B acts **synergistically with MAP2 and tau** — double-knockout mice show delayed neuronal migration and disorganized cortical layering. A newly described **nuclear pool of MAP1B** interacts with the BRG1 chromatin-remodelling complex; increasing the nuclear/cytosol ratio disrupts neuronal positioning, reminiscent of MAP1B patients, and mutant human brain organoids show neuronal ectopia.

Supporting quotes: "*Functional data from animal and cell models support a mechanism involving impaired microtubule stabilization, altered growth cone dynamics, and dysregulated axon branching*" [PMID: 40874586](https://pubmed.ncbi.nlm.nih.gov/40874586/); "*map1B-deficient neurons from the lower rhombic lip and other brain regions have reduced chemoattractive responses to Netrin 1 in vitro*" [PMID: 15186740](https://pubmed.ncbi.nlm.nih.gov/15186740/); "*FMRP regulates postnatal neuronal migration via MAP1B*" [PMID: 38757694](https://pubmed.ncbi.nlm.nih.gov/38757694/); "*increasing the nuclear/cytosol ratio disrupts neuronal positioning, reminiscent of patients with MAP1B mutations*" [PMID: 42276043](https://pubmed.ncbi.nlm.nih.gov/42276043/); and "*disrupted cortical patterning caused by retarded neuronal migration*" [PMID: 11581286](https://pubmed.ncbi.nlm.nih.gov/11581286/). *Evidence source: model organism + in vitro + computational.*

### Finding 5 — Map1b-deficient mice recapitulate neuronal migration and axon defects

Map1b-deficient mice (gene-trap/knockout; *Mus musculus*; ortholog *Map1b*, NCBI Gene 17755) show severe abnormal nervous-system development. Homozygous mutants **die on the first postnatal day** with altered structure of several brain regions, and analyses "*suggest the participation of MAP1B in neuronal migration*." Cultured DRG neurons from MAP1B-deficient mice show reduced axon elongation (~half the elongation speed of controls) and increased growth-cone area. Map2/Map1b and tau/Map1b double-knockouts show delayed neuronal migration and disorganized cortical layering, indicating partial redundancy with other MAPs.

Quotes: "*Homozygous mice die on the first day after birth, probably due to a severe abnormal development of the nervous system*" and "*Analyses of these mice indicate the presence of several neural defects and suggest the participation of MAP1B in neuronal migration*" [PMID: 11085878](https://pubmed.ncbi.nlm.nih.gov/11085878/); "*Cultured DRG neurons from MAP1B deficient mice show a reduction in axon elongation and an increase in growth cone area*" [PMID: 12088839](https://pubmed.ncbi.nlm.nih.gov/12088839/). *Evidence source: model organism.*

### Finding 6 — PVNH9 within the PVNH spectrum: genetic heterogeneity and epilepsy burden

PVNH is a malformation of cortical development caused by impaired neuronal migration producing nodular masses of neurons/glia along the lateral ventricle walls. It is **genetically heterogeneous**: the most common single-gene cause is X-linked *FLNA* (PVNH1, predominantly females, male prenatal lethality); other loci include *ARFGEF2* (PVNH2, autosomal recessive) and *MAP1B* (PVNH9, autosomal dominant). In FLNA-negative bilateral PVNH cohorts (n = 71), focal-onset seizures were most common (79.3%), developmental delay was present in 21.8%, family history of epilepsy in 36.9%, and febrile seizures in 16.6%. Epilepsy is frequently drug-resistant; surgical options include stereotactic MRgLITT targeting epileptogenic nodules.

Quotes: "*Periventricular nodular heterotopia (PVNH) is a malformation of cortical development due to impaired neuronal migration resulting in the formation of nodular masses of neurons and glial cells in close proximity to the ventricular walls*" and "*Focal onset seizures were the most common type of seizure presentation (79.3%)*" [PMID: 26340046](https://pubmed.ncbi.nlm.nih.gov/26340046/); "*Stereotactic MR guided laser interstitial thermal therapy (MRgLITT) has recently become available for controlled focal ablation, enabling us to target these lesions*" [PMID: 24518890](https://pubmed.ncbi.nlm.nih.gov/24518890/). *Evidence source: human clinical.*

### Finding 7 — *MAP1B* implicated by genome-wide significant collapsing analysis, with incomplete penetrance

The founding study exome-sequenced **202 individuals with sporadic PVNH**. A gene-level collapsing analysis identified a **genome-wide significant signal** driven by four ultra-rare LoF heterozygous variants in *MAP1B* (including one de novo). PVNH cases overall showed a significant excess of nonsynonymous de novo variants in intolerant genes (p = 3.27×10⁻⁷). The PVNH was frontally predominant and associated with perisylvian polymicrogyria. In at least one instance the variant was inherited from a parent with previously undiagnosed PVNH, demonstrating **incomplete penetrance/variable expressivity**. A subsequent family (Arya et al., 2021) with a novel heterozygous frameshift variant showed seizures (febrile, fever-triggered, afebrile), photosensitivity, mild developmental delay, obsessive-compulsive behaviours and poor attention, with periventricular heterotopia, corpus callosum abnormalities and perisylvian polymicrogyria.

Quotes: "*we identified a genome-wide significant signal driven by four ultra-rare loss-of-function heterozygous variants in MAP1B, including one de novo variant*"; "*In at least one instance, the MAP1B variant was inherited from a parent with previously undiagnosed PVNH*"; "*The PVNH was frontally predominant and associated with perisylvian polymicrogyria*" [PMID: 29738522](https://pubmed.ncbi.nlm.nih.gov/29738522/). Confirmatory imaging: "*Neuroimaging showed PVH, corpus callosum abnormalities, and perisylvian polymicrogyria*" [PMID: 33772511](https://pubmed.ncbi.nlm.nih.gov/33772511/). *Evidence source: human genetics (statistical).*

### Finding 8 — *MAP1B* missense variants cause autosomal dominant nonsyndromic sensorineural hearing loss (distinct allelic phenotype)

Three novel heterozygous *MAP1B* missense mutations (c.4198A>G p.Ser1400Gly; c.2768T>C p.Ile923Thr; c.5512T>C p.Phe1838Leu) cosegregated with **autosomal dominant nonsyndromic SNHL** in three unrelated Chinese families. MAP1B is highly expressed in cochlear spiral ganglion neurons. Patient iPSC-derived otic sensory neuron-like cells carrying p.Ser1400Gly showed reduced MAP1B levels/phosphorylation, disturbed microtubule dynamics, impaired axonal elongation and electrophysiological defects — rescued by CRISPR/Cas9 correction. Map1b heterozygous knockout mice displayed late-onset progressive SNHL, more pronounced at high frequencies.

Quotes: "*Three novel heterozygous MAP1B mutations (c.4198A>G, p.1400S>G; c.2768T>C, p.923I>T; c.5512T>C, p.1838F>L) were cosegregated with autosomal dominant inheritance of nonsyndromic sensorineural hearing loss in 3 unrelated Chinese families*"; "*Map1b heterozygous KO mice displayed late-onset progressive sensorineural hearing loss that was more pronounced in the high frequencies*"; "*MAP1B is highly expressed in the spiral ganglion neurons in the mouse cochlea*" [PMID: 33268592](https://pubmed.ncbi.nlm.nih.gov/33268592/). *Evidence source: human genetics + iPSC + mouse.*

---

## Report by Requested Section

### 1. Disease Information

PVNH9 is a rare, genetically-defined subtype of **periventricular nodular heterotopia** — a malformation of cortical development in which nodules of neurons and glia are ectopically retained along the lateral ventricular walls due to failed radial neuronal migration [PMID: 26340046](https://pubmed.ncbi.nlm.nih.gov/26340046/). It is defined at the molecular level by heterozygous LoF variants in *MAP1B* [PMID: 40802165](https://pubmed.ncbi.nlm.nih.gov/40802165/).

**Key identifiers:** OMIM #618918; MONDO:0030061; causal gene *MAP1B* (HGNC:6836; OMIM *157129; NCBI Gene 4131; chromosome 5q13.2). Orphanet groups the disorder under periventricular nodular heterotopia; a dedicated ICD-11 code is not established, but the broad category is congenital malformation of the brain (ICD-11 LA05; ICD-10 Q04.8, "other specified congenital malformations of brain"). MeSH: "Periventricular Nodular Heterotopia." **Synonyms/alternative names:** PVNH9; PNH9; MAP1B-related periventricular nodular heterotopia; MAP1B-related brain malformation/syndrome.

**Information source:** The evidence is derived from **aggregated disease-level resources and small case series/cohorts** (OMIM, published families, exome/genome cohorts), not large EHR datasets.

### 2. Etiology

**Causal factors — genetic.** The primary cause is a heterozygous germline LoF variant in *MAP1B* (nonsense, frameshift, splice-site) acting through haploinsufficiency [PMID: 40802165](https://pubmed.ncbi.nlm.nih.gov/40802165/); [PMID: 29738522](https://pubmed.ncbi.nlm.nih.gov/29738522/). No environmental or infectious cause is implicated; PVNH9 is a monogenic neurodevelopmental malformation.

**Genetic risk factors.** The causal variant is itself the risk determinant. Broader PVNH is genetically heterogeneous (see §4/§9), and rare genomic copy-number variants contribute to the wider PVNH population — array-CGH shows an enrichment of pathogenic CNVs in PVNH versus polymicrogyria (35.7% vs 9.1%) [PMID: 30683929](https://pubmed.ncbi.nlm.nih.gov/30683929/).

**Environmental / lifestyle risk factors.** None established for PVNH9 specifically. As a de novo or inherited monogenic malformation, it is not attributable to toxins, occupational exposure, diet, smoking or alcohol.

**Protective factors.** None identified (genetic or environmental). *Not available for this disease.*

**Gene–environment interactions.** No documented GxE interactions. Phenotypic variability appears driven by genetic/modifier and stochastic developmental factors rather than environment; note fever-triggered seizures in one family [PMID: 33772511](https://pubmed.ncbi.nlm.nih.gov/33772511/) as a possible symptomatic trigger rather than a disease-causing interaction.

### 3. Phenotypes

| Phenotype | Type | Suggested HPO | Onset | Severity | Frequency |
|---|---|---|---|---|---|
| Periventricular nodular heterotopia (frontally predominant) | Imaging/structural | HP:0032388 (periventricular nodular heterotopia) | Congenital | — | ~core (4/5 imaged) |
| Global developmental delay | Clinical sign | HP:0001263 | Infancy/childhood | Mild–moderate | Common |
| Intellectual disability | Clinical sign | HP:0001249 | Childhood | Mild–moderate | Common |
| Focal epilepsy / seizures | Clinical sign | HP:0007359 / HP:0001250 | Childhood | Variable, often drug-resistant | Common |
| Behavioural dysregulation / OCD features / poor attention | Behavioural | HP:0000708 / HP:0000722 / HP:0000736 | Childhood | Variable | Subset |
| Polymicrogyria (perisylvian) | Imaging/structural | HP:0002126 | Congenital | — | Subset |
| Corpus callosum dysgenesis/agenesis | Imaging/structural | HP:0001274 / HP:0001273 | Congenital | — | Subset |
| Microcephaly | Physical | HP:0000252 | Congenital/childhood | Variable | Subset |
| Short stature | Physical | HP:0004322 | Childhood | Variable | Subset |
| Dysmorphic facial features | Physical | HP:0001999 | Congenital | Variable | Subset |
| Sensorineural hearing loss (missense alleles only) | Clinical sign | HP:0000407 | Late-onset, progressive | High-frequency predominant | Missense subgroup |

Core features are supported by [PMID: 40874586](https://pubmed.ncbi.nlm.nih.gov/40874586/) and [PMID: 31317654](https://pubmed.ncbi.nlm.nih.gov/31317654/); the missense/deafness phenotype by [PMID: 33268592](https://pubmed.ncbi.nlm.nih.gov/33268592/). **Progression:** the structural malformation is static (congenital), while epilepsy and cognitive/behavioural features constitute the chronic clinical burden. **Quality-of-life impact:** driven principally by epilepsy (often drug-resistant), intellectual disability and behavioural dysregulation, which affect education, independence and daily functioning; disease-specific QoL instruments have not been applied. Bilateral frontal PVNH generally carries "*milder sequelae than other forms of bilateral PVNH*" [PMID: 41468712](https://pubmed.ncbi.nlm.nih.gov/41468712/).

### 4. Genetic / Molecular Information

- **Causal gene:** *MAP1B* (HGNC:6836; OMIM *157129; NCBI Gene 4131; UniProt P46821; 5q13.2).
- **Pathogenic variants:** Nonsense (e.g., c.2035G>T p.Glu679* [PMID: 31317654](https://pubmed.ncbi.nlm.nih.gov/31317654/)), frameshift/duplication (e.g., c.7091dup), and splice variants; classified pathogenic/likely pathogenic per ACMG (de novo occurrence, LoF in a constrained gene, segregation). Four ultra-rare heterozygous LoF variants underpinned the founding genome-wide signal [PMID: 29738522](https://pubmed.ncbi.nlm.nih.gov/29738522/).
- **Variant class / functional consequence:** LoF → **haploinsufficiency** (reduced mRNA and protein) [PMID: 40802165](https://pubmed.ncbi.nlm.nih.gov/40802165/). By contrast, **missense** variants (p.Ser1400Gly, p.Ile923Thr, p.Phe1838Leu) cause SNHL and behave as a distinct allelic series [PMID: 33268592](https://pubmed.ncbi.nlm.nih.gov/33268592/).
- **Allele frequency:** Pathogenic variants are ultra-rare/private in population databases (gnomAD); *MAP1B* is a highly constrained gene, consistent with LoF intolerance.
- **Somatic vs germline:** Germline (de novo or inherited).
- **Modifier genes:** Functional redundancy with *MAP2* and *MAPT* (tau) [PMID: 11581286](https://pubmed.ncbi.nlm.nih.gov/11581286/); EB1/*MAPRE1* can partially complement MAP1B loss [PMID: 15789376](https://pubmed.ncbi.nlm.nih.gov/15789376/) — candidate genetic modifiers of expressivity, though not clinically validated.
- **Epigenetic information:** No disease-specific methylation/histone signature reported. *Not available.*
- **Chromosomal abnormalities:** PVNH broadly is associated with recurrent CNVs (e.g., 7q11.23, 7p22.1) and extreme genetic heterogeneity [PMID: 30683929](https://pubmed.ncbi.nlm.nih.gov/30683929/); [PMID: 41468712](https://pubmed.ncbi.nlm.nih.gov/41468712/), but PVNH9 itself is defined by intragenic *MAP1B* LoF.

### 5. Environmental Information

No environmental factors, lifestyle factors, or infectious agents are implicated in PVNH9. It is a monogenic developmental disorder. *Not applicable.*

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A **heterozygous LoF variant in *MAP1B*** (nonsense/frameshift/splice) **results in** reduced *MAP1B* mRNA and protein — **haploinsufficiency** [PMID: 40802165](https://pubmed.ncbi.nlm.nih.gov/40802165/).
2. Reduced MAP1B **leads to** impaired microtubule stabilization and impaired crosslinking of microtubules to actin, **disrupting growth-cone dynamics and axon branching/elongation** [PMID: 40874586](https://pubmed.ncbi.nlm.nih.gov/40874586/); [PMID: 12088839](https://pubmed.ncbi.nlm.nih.gov/12088839/).
3. Because MAP1B is a **downstream effector of Netrin-1 signalling** (GSK3/CDK5-phosphorylation), reduced MAP1B **blunts chemoattractant responses** guiding migrating neurons and axons [PMID: 15186740](https://pubmed.ncbi.nlm.nih.gov/15186740/). *(Upstream regulation: FMRP normally represses MAP1B translation and regulates migration via MAP1B [PMID: 38757694](https://pubmed.ncbi.nlm.nih.gov/38757694/); a nuclear MAP1B pool interacting with BRG1 chromatin remodelling also influences positioning [PMID: 42276043](https://pubmed.ncbi.nlm.nih.gov/42276043/).)*
4. Impaired cytoskeletal dynamics **cause retarded radial neuronal migration** during corticogenesis (demonstrated in mouse; partially buffered by MAP2/tau redundancy) [PMID: 11581286](https://pubmed.ncbi.nlm.nih.gov/11581286/); [PMID: 11085878](https://pubmed.ncbi.nlm.nih.gov/11085878/).
5. Neurons that fail to migrate **are retained as ectopic nodules along the lateral ventricle walls** — periventricular nodular heterotopia, frontally predominant [PMID: 26340046](https://pubmed.ncbi.nlm.nih.gov/26340046/); [PMID: 29738522](https://pubmed.ncbi.nlm.nih.gov/29738522/).
   - **Branch A:** Cortical dysgenesis co-occurs as **perisylvian polymicrogyria** and **corpus callosum abnormalities** (axon-guidance component) [PMID: 29738522](https://pubmed.ncbi.nlm.nih.gov/29738522/); [PMID: 33772511](https://pubmed.ncbi.nlm.nih.gov/33772511/).
   - **Branch B (missense alleles):** in cochlear **spiral ganglion neurons**, altered MAP1B **causes sensorineural hearing loss** rather than migration failure [PMID: 33268592](https://pubmed.ncbi.nlm.nih.gov/33268592/).
6. Ectopic nodules and abnormal cortical circuitry **produce an epileptogenic substrate and disordered network function**, which **results in** focal epilepsy, developmental delay, intellectual disability and behavioural dysregulation [PMID: 40874586](https://pubmed.ncbi.nlm.nih.gov/40874586/); [PMID: 26340046](https://pubmed.ncbi.nlm.nih.gov/26340046/).

```
MAP1B LoF variant
      │ (haploinsufficiency: down mRNA / down protein)
      ▼
down microtubule stabilization / MT-actin crosslinking
      │  (blunted Netrin-1 response; FMRP / nuclear-BRG1 regulation upstream)
      ▼
impaired growth-cone dynamics & axon elongation
      ▼
retarded radial neuronal migration ──► Branch A: perisylvian polymicrogyria + corpus callosum anomalies
      ▼                                 Branch B (missense): spiral ganglion neurons → SNHL
ectopic periventricular nodules (frontal-predominant PVNH)
      ▼
epileptogenic cortical network
      ▼
epilepsy · developmental delay · intellectual disability · behaviour
```

**Molecular pathways:** microtubule/cytoskeletal regulation; Netrin-1/DCC guidance; JNK-MAPK signalling phosphorylates MAP1B (MKK4/MKK7→JNK), linking stress-kinase pathways to migration/axon elongation [PMID: 22090513](https://pubmed.ncbi.nlm.nih.gov/22090513/); [PMID: 40594443](https://pubmed.ncbi.nlm.nih.gov/40594443/). **Cellular processes:** neuronal migration (GO:0001764), axon guidance (GO:0007411), microtubule cytoskeleton organization (GO:0000226), growth-cone dynamics. **Protein dysfunction:** loss of function/haploinsufficiency of a microtubule-stabilizing MAP. **Immune/metabolic involvement:** not implicated. **Cell types:** migrating cortical projection neurons (CL:0000679 glutamatergic neuron; migrating post-mitotic neurons), and — for the missense branch — cochlear spiral ganglion neurons (CL:0000100).

### 7. Anatomical Structures Affected

- **Organ/system:** central nervous system — cerebral cortex and periventricular white matter (UBERON:0000956 cerebral cortex; UBERON:0002285 periventricular region; UBERON:0002436 lateral ventricle). Body system: nervous system.
- **Localization:** heterotopic nodules along the **lateral ventricle walls**, **frontally (anteriorly) predominant**, typically **bilateral** [PMID: 29738522](https://pubmed.ncbi.nlm.nih.gov/29738522/); [PMID: 41468712](https://pubmed.ncbi.nlm.nih.gov/41468712/). Associated: **perisylvian cortex** (polymicrogyria) and **corpus callosum** (UBERON:0002336).
- **Tissue/cell level:** nervous tissue; ectopic post-mitotic neurons and glia forming nodules. For the missense/deafness branch: cochlear spiral ganglion neurons.
- **Subcellular level:** cytoskeleton — **microtubules** (GO:0005874) and the microtubule–actin interface; a **nuclear** MAP1B pool is also implicated (GO:0005634) [PMID: 42276043](https://pubmed.ncbi.nlm.nih.gov/42276043/); presynaptic terminals in mature neurons [PMID: 27425640](https://pubmed.ncbi.nlm.nih.gov/27425640/).

### 8. Temporal Development

- **Onset:** the malformation is **congenital** (arises during fetal corticogenesis); clinical features (seizures, developmental delay) manifest in **infancy/childhood** [PMID: 40874586](https://pubmed.ncbi.nlm.nih.gov/40874586/).
- **Progression:** the structural lesion is **static/stable**; epilepsy and neurodevelopmental features follow a **chronic, lifelong** course. Missense-associated SNHL is **late-onset and progressive** [PMID: 33268592](https://pubmed.ncbi.nlm.nih.gov/33268592/).
- **Critical period:** the window of vulnerability is **prenatal neuronal migration** (~weeks 8–24 of gestation); there is no postnatal window to reverse the malformation, so intervention is symptomatic.

### 9. Inheritance and Population

- **Inheritance:** **Autosomal dominant**, de novo or inherited [PMID: 29738522](https://pubmed.ncbi.nlm.nih.gov/29738522/).
- **Penetrance/expressivity:** **incomplete penetrance and variable expressivity** — a variant was inherited from a parent with previously undiagnosed PVNH [PMID: 29738522](https://pubmed.ncbi.nlm.nih.gov/29738522/).
- **Epidemiology:** PVNH9 is ultra-rare with no formal prevalence/incidence estimate; it represents a small fraction of overall PVNH (itself dominated by *FLNA*). Bilateral frontal PVNH — the pattern within which *MAP1B* falls — accounts for **~10% of all PVNH** [PMID: 41468712](https://pubmed.ncbi.nlm.nih.gov/41468712/). *Precise PVNH9 prevalence: not available.*
- **Sex ratio:** No strong sex bias reported for PVNH9 (unlike X-linked *FLNA* PVNH1, which predominates in females with male prenatal lethality) [PMID: 23622213](https://pubmed.ncbi.nlm.nih.gov/23622213/).
- **Founder effects / consanguinity / anticipation / mosaicism:** none established; not a repeat-expansion disorder. *Not applicable/not available.*

### 10. Diagnostics

- **Imaging (primary diagnostic modality):** brain **MRI** shows bilateral frontally-predominant periventricular nodules isointense to grey matter, often with perisylvian polymicrogyria and corpus callosum anomalies [PMID: 29738522](https://pubmed.ncbi.nlm.nih.gov/29738522/); [PMID: 41468712](https://pubmed.ncbi.nlm.nih.gov/41468712/).
- **Genetic testing:** **exome or genome sequencing** is the diagnostic mainstay (variant detected on WES [PMID: 31317654](https://pubmed.ncbi.nlm.nih.gov/31317654/)); PVNH gene panels including *MAP1B*, *FLNA*, *ARFGEF2* and others; **chromosomal microarray (CMA)** for CNVs given genetic heterogeneity — CMA yields a diagnosis in ~13% and exome/genome in ~38% of bilateral frontal PVNH where tested [PMID: 41468712](https://pubmed.ncbi.nlm.nih.gov/41468712/).
- **Electrophysiology:** EEG for seizure characterization (focal-onset predominant [PMID: 26340046](https://pubmed.ncbi.nlm.nih.gov/26340046/)).
- **Differential diagnosis:** other PVNH genetic subtypes (notably *FLNA* PVNH1 — classic bilateral frontocentral, female-predominant; *ARFGEF2* PVNH2), and other malformations of cortical development (lissencephaly/SBH from *LIS1*/*DCX*, polymicrogyria syndromes) [PMID: 23622213](https://pubmed.ncbi.nlm.nih.gov/23622213/); [PMID: 28411558](https://pubmed.ncbi.nlm.nih.gov/28411558/).
- **Biomarkers / omics / newborn screening:** no molecular biomarker or newborn-screening test exists; diagnosis is imaging + sequencing.

### 11. Outcome / Prognosis

PVNH9 is a **chronic, non-progressive** structural disorder; **life expectancy is generally not shortened** in humans (in contrast to the perinatal lethality of homozygous mouse knockouts, which reflects biallelic loss not seen in patients [PMID: 11085878](https://pubmed.ncbi.nlm.nih.gov/11085878/)). Morbidity is driven by **epilepsy** (frequently drug-resistant [PMID: 30819503](https://pubmed.ncbi.nlm.nih.gov/30819503/)), **intellectual disability**, and **behavioural dysregulation**. Bilateral frontal PVNH tends to have **milder sequelae** than other bilateral PVNH forms [PMID: 41468712](https://pubmed.ncbi.nlm.nih.gov/41468712/). **Prognostic factors:** seizure control, severity of associated malformations (polymicrogyria, corpus callosum agenesis) and degree of cognitive impairment. No validated prognostic biomarkers. Quality-of-life instruments have not been formally applied.

### 12. Treatment

There is **no disease-modifying/curative therapy**; management is symptomatic and multidisciplinary.

- **Pharmacotherapy:** **antiseizure medications** for epilepsy (NCIT: Anticonvulsant Agent). Choice follows focal-epilepsy guidelines; drug resistance is common [PMID: 30819503](https://pubmed.ncbi.nlm.nih.gov/30819503/).
- **Surgical/interventional:** for refractory focal epilepsy arising from epileptogenic nodules, **stereotactic MR-guided laser interstitial thermal therapy (MRgLITT)** enables focal ablation of nodules [PMID: 24518890](https://pubmed.ncbi.nlm.nih.gov/24518890/); [PMID: 28370739](https://pubmed.ncbi.nlm.nih.gov/28370739/); resective/stereotactic epilepsy surgery is an option in selected cases [PMID: 30819503](https://pubmed.ncbi.nlm.nih.gov/30819503/).
- **Supportive/rehabilitative:** developmental and educational support, physical/occupational/speech therapy, and behavioural/psychiatric management (NCIT: Rehabilitation Therapy; Supportive Care).
- **Advanced/experimental therapeutics (gene, cell, RNA, targeted, immuno):** none reported for PVNH9. *Not available.*
- **Pharmacogenomics / personalized medicine:** none specific to PVNH9. *Not available.*
- **For the missense/deafness allelic phenotype:** management is hearing rehabilitation (amplification/cochlear implantation as indicated) — outside the PVNH9 malformation itself [PMID: 33268592](https://pubmed.ncbi.nlm.nih.gov/33268592/).

### 13. Prevention

Because PVNH9 is a monogenic developmental malformation, prevention is limited to **reproductive/genetic strategies**: **genetic counselling** for autosomal dominant transmission with incomplete penetrance, **cascade testing** of at-risk relatives, and options for **prenatal diagnosis or preimplantation genetic testing** when a familial variant is known. **Tertiary prevention** — preventing complications — centres on optimizing seizure control and developmental support. There is no primary prevention (no modifiable environmental risk), no immunization, and no population screening. *Primary/behavioural/public-health prevention: not applicable.*

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *Mus musculus* *Map1b* (NCBI Gene 17755; NCBI Taxon 10090) is the principal experimental ortholog; a *Drosophila* ortholog **Futsch** exists (relevant to fragile-X/MAP1B biology) [PMID: 15498496](https://pubmed.ncbi.nlm.nih.gov/15498496/).
- **Natural disease in other species:** no naturally-occurring companion-animal or wildlife PVNH9 equivalent is documented in OMIA. *Not available.* Disease knowledge derives from engineered models, not natural animal disease.
- **Comparative biology:** MAP1B's role in neuronal migration and axon growth is **evolutionarily conserved** from Drosophila (Futsch) to mouse to human, supporting cross-species mechanistic inference [PMID: 15498496](https://pubmed.ncbi.nlm.nih.gov/15498496/); [PMID: 11085878](https://pubmed.ncbi.nlm.nih.gov/11085878/).
- **Zoonotic potential:** none (genetic disorder). *Not applicable.*

### 15. Model Organisms

| Model | Type | Key phenotype | Recapitulation | Reference |
|---|---|---|---|---|
| *Map1b* KO / gene-trap mouse (homozygous) | Mammalian, germline KO | Perinatal (P1) lethality; severe abnormal CNS development; neuronal migration defects | Confirms migration mechanism; homozygous lethality exceeds heterozygous human phenotype | [PMID: 11085878](https://pubmed.ncbi.nlm.nih.gov/11085878/) |
| *Map1b* heterozygous KO mouse | Mammalian | Late-onset progressive high-frequency SNHL | Models the missense/deafness allelic branch | [PMID: 33268592](https://pubmed.ncbi.nlm.nih.gov/33268592/) |
| *Map1b* / *Map2* and *Map1b* / *Mapt*(tau) double KO | Mammalian | Delayed neuronal migration, disorganized cortical layering | Reveals MAP redundancy; unmasks migration role | [PMID: 11581286](https://pubmed.ncbi.nlm.nih.gov/11581286/) |
| MAP1B-deficient DRG/hippocampal neurons | In vitro (mouse) | Reduced axon elongation, increased growth-cone area, presynaptic deficits | Cellular mechanism of axon growth defect | [PMID: 12088839](https://pubmed.ncbi.nlm.nih.gov/12088839/); [PMID: 27425640](https://pubmed.ncbi.nlm.nih.gov/27425640/) |
| Patient iPSC-derived otic sensory neuron-like cells | In vitro (human) | Reduced MAP1B/phospho-MAP1B, disturbed microtubule dynamics, impaired axon elongation; rescued by CRISPR correction | Directly models human missense allele | [PMID: 33268592](https://pubmed.ncbi.nlm.nih.gov/33268592/) |
| Human brain organoids (MAP1B mutant / nuclear ratio) | In vitro (human) | Neuronal ectopia; disrupted positioning | Models cortical mispositioning | [PMID: 42276043](https://pubmed.ncbi.nlm.nih.gov/42276043/) |
| *Drosophila* (Futsch; *fmr1* context) | Invertebrate | Altered synaptic/neuronal elaboration | Conserved MAP1B/FMRP axis | [PMID: 15498496](https://pubmed.ncbi.nlm.nih.gov/15498496/) |

**Model resources:** MGI (mouse *Map1b*), IMPC/IMSR (KO alleles), Cellosaurus (iPSC lines), FlyBase (*futsch*). **Limitation:** homozygous mouse lethality and the SNHL-focused heterozygous phenotype mean no single model fully recapitulates human heterozygous LoF PVNH9 cortical heterotopia; organoids are the most direct human-relevant system.

---

## Mechanistic Model / Interpretation

The findings converge into a single coherent model: **PVNH9 is a microtubule-cytoskeletal disorder of neuronal migration caused by MAP1B haploinsufficiency.** MAP1B is expressed early in nervous-system development where it stabilizes microtubules and links them to actin, powering the growth-cone motility and axon elongation that migrating neurons and their processes require. When one *MAP1B* allele is lost, protein dosage falls below the threshold needed for timely radial migration (a threshold partly buffered by the redundant MAPs MAP2 and tau, and by EB1). Neurons that fail to reach the cortical plate remain as **frontally-predominant periventricular nodules**, while accompanying axon-guidance failures manifest as perisylvian polymicrogyria and corpus callosum anomalies. The resulting aberrant cortical circuitry is epileptogenic and cognitively/behaviourally disruptive.

The model is unusually well-triangulated: **statistical human genetics** (genome-wide significant collapsing signal), **independent case series**, **functional demonstration of reduced expression**, **mouse genetics** (migration defect, redundancy), and **cellular/organoid biology** all point the same way. The **allelic dichotomy** — LoF causing brain malformation versus missense causing isolated deafness — is the most intriguing feature and implies that missense alleles do not simply reduce dosage but exert a tissue-restricted or altered-function effect to which cochlear spiral ganglion neurons are selectively vulnerable, while LoF's dosage reduction preferentially derails cortical migration.

---

## Evidence Base

| PMID | Contribution | Evidence type |
|---|---|---|
| [40802165](https://pubmed.ncbi.nlm.nih.gov/40802165/) | Causal gene + LoF/haploinsufficiency; genotype–phenotype dichotomy | Human clinical + in vitro |
| [40874586](https://pubmed.ncbi.nlm.nih.gov/40874586/) | Core clinical spectrum; anteriorly predominant PVNH; mechanism synthesis | Human clinical |
| [31317654](https://pubmed.ncbi.nlm.nih.gov/31317654/) | De novo nonsense variant; recurrent phenotype triad | Human clinical |
| [29738522](https://pubmed.ncbi.nlm.nih.gov/29738522/) | Founding genome-wide collapsing signal; incomplete penetrance; imaging | Human genetics (statistical) |
| [33772511](https://pubmed.ncbi.nlm.nih.gov/33772511/) | Confirmatory family; epilepsy + imaging triad | Human clinical |
| [15186740](https://pubmed.ncbi.nlm.nih.gov/15186740/) | MAP1B downstream of Netrin-1 in migration/guidance | Model organism/in vitro |
| [38757694](https://pubmed.ncbi.nlm.nih.gov/38757694/) | FMRP regulates migration via MAP1B (upstream) | Model organism |
| [42276043](https://pubmed.ncbi.nlm.nih.gov/42276043/) | Nuclear MAP1B/BRG1; organoid ectopia | In vitro/human organoid |
| [11581286](https://pubmed.ncbi.nlm.nih.gov/11581286/) | MAP1B/MAP2 redundancy; retarded migration | Model organism |
| [11085878](https://pubmed.ncbi.nlm.nih.gov/11085878/) | KO mouse lethality + migration defect | Model organism |
| [12088839](https://pubmed.ncbi.nlm.nih.gov/12088839/) | Axon elongation/growth-cone cellular phenotype | In vitro |
| [26340046](https://pubmed.ncbi.nlm.nih.gov/26340046/) | PVNH definition; epilepsy burden quantification | Human clinical |
| [24518890](https://pubmed.ncbi.nlm.nih.gov/24518890/) | MRgLITT surgical option | Human clinical |
| [33268592](https://pubmed.ncbi.nlm.nih.gov/33268592/) | Missense → SNHL allelic branch; iPSC + mouse | Human genetics + iPSC + mouse |
| [41468712](https://pubmed.ncbi.nlm.nih.gov/41468712/) | Bilateral frontal PVNH as ~10% of PVNH; milder sequelae | Human clinical |
| [30683929](https://pubmed.ncbi.nlm.nih.gov/30683929/) | Genetic heterogeneity/CNVs in PVNH | Human genetics |

---

## Limitations and Knowledge Gaps

- **Small evidence base:** PVNH9 is defined by a handful of families and cohort variants; precise **prevalence, penetrance quantification, sex ratio, and natural-history data are unavailable**.
- **Mechanism of the allelic dichotomy** (LoF→PVNH vs missense→deafness) is not fully resolved — whether missense alleles are hypomorphic, dominant-negative or gain-of-function in the cochlea remains to be tested directly.
- **Model mismatch:** no mouse model reproduces human heterozygous-LoF cortical heterotopia (homozygotes are perinatally lethal; heterozygotes model deafness). Human organoids are the most promising but early-stage system.
- **No genotype–phenotype granularity** linking specific LoF variant position to severity of epilepsy or cognition; **modifier genes** (MAP2, tau, EB1) are hypothesized but not clinically validated.
- **No omics profiling** (transcriptomic/proteomic/metabolomic/epigenomic) specific to PVNH9 patient tissue; no biomarkers.
- **Treatment evidence is generic** (focal-epilepsy management); no PVNH9-specific therapeutic trials.

## Proposed Follow-up Experiments / Actions

1. **Establish an international PVNH9 registry** to quantify penetrance, expressivity, sex ratio, epilepsy trajectory and cognitive outcomes.
2. **Isogenic human cortical organoids/assembloids** carrying patient LoF versus missense variants (with CRISPR-corrected controls) to directly test migration failure, quantify dosage thresholds, and dissect the allelic dichotomy.
3. **Conditional / heterozygous cortical *Map1b* models** (or humanized alleles) to bypass homozygous lethality and reproduce the heterotopia phenotype in vivo.
4. **Functional characterization of missense alleles** in cochlear versus cortical neuronal contexts to determine hypomorphic vs dominant-negative behaviour.
5. **Modifier screens** for MAP2/tau/EB1 dosage effects on migration rescue, to explain variable expressivity and identify candidate therapeutic targets.
6. **Standardized deep phenotyping** (MRI subtyping, EEG, neuropsychology, QoL instruments) to build prognostic models and refine surgical (MRgLITT) candidate selection.

---

*Evidence source key: human clinical = patient case series/cohorts; human genetics = statistical/variant studies; model organism = mouse/Drosophila; in vitro = cultured neurons/iPSC/organoids; computational = in silico. This report was compiled from 41 reviewed publications and 8 confirmed findings.*


## Artifacts

- [OpenScientist final report](Periventricular_Nodular_Heterotopia_9-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Periventricular_Nodular_Heterotopia_9-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 17 |
| Quoted claims found in source | 17 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 25 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 10 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001263` (1 mention) - the report calls it "Clinical sign"; HP calls it **Global developmental delay**
- `HP:0001249` (1 mention) - the report calls it "Clinical sign"; HP calls it **Intellectual disability**
- `HP:0002126` (1 mention) - the report calls it "Imaging/structural"; HP calls it **Polymicrogyria**
- `HP:0000252` (1 mention) - the report calls it "Physical"; HP calls it **Microcephaly**
- `HP:0004322` (1 mention) - the report calls it "Physical"; HP calls it **Short stature**
- `HP:0001999` (1 mention) - the report calls it "Physical"; HP calls it **Abnormal facial shape**
- `HP:0000407` (1 mention) - the report calls it "Clinical sign"; HP calls it **Sensorineural hearing impairment**
- `GO:0005874` (1 mention) - the report calls it "microtubules", "Subcellular level:** cytoskeleton — **microtubules"; GO calls it **microtubule**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005874` - called "microtubules", "Subcellular level:** cytoskeleton — **microtubules"