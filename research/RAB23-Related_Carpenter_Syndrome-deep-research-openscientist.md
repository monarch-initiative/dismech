---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T16:14:34.984698'
end_time: '2026-09-01T16:42:44.973147'
duration_seconds: 1689.99
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: RAB23-related Carpenter Syndrome
  mondo_id: ''
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
citation_count: 23
reference_validation:
  total_references: 23
  verified: 23
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 23
  on_topic: 17
  validator_version: 0.2.1
term_validation:
  total_terms: 53
  verified: 51
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 27
  labels_matching: 15
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: MONDO:0008544
    reported_labels:
    - MONDO
    ontology_label: tetramelic monodactyly
  - term_id: HP:0001513
    reported_labels:
    - Obesity
    - Frequent
    ontology_label: Obesity
  - term_id: HP:0001627
    reported_labels:
    - Abnormal heart morphology
    - "Frequent (~30\u201350%)"
    ontology_label: Abnormal heart morphology
  - term_id: HP:0000028
    reported_labels:
    - Cryptorchidism
    - Universal in boys
    ontology_label: Cryptorchidism
  - term_id: HP:0001537
    reported_labels:
    - Umbilical hernia
    - Frequent
    ontology_label: Umbilical hernia
  - term_id: HP:0001249
    reported_labels:
    - Intellectual disability
    - ~75% (variable)
    ontology_label: Intellectual disability
  - term_id: HP:0007957
    reported_labels:
    - Occasional
    ontology_label: Corneal opacity
  - term_id: UBERON:0000955
    reported_labels:
    - anterior cranial fossa hypoplasia, bulging middle fossa, hydrocephalus
    ontology_label: brain
  - term_id: UBERON:0001474
    reported_labels:
    - Tissue level:** bone
    ontology_label: bone element
  labels_variant: 3
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
  path: RAB23-Related_Carpenter_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: RAB23-Related_Carpenter_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** RAB23-related Carpenter Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **RAB23-related Carpenter Syndrome** covering all of the
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

# RAB23-related Carpenter Syndrome (CRPT1): Comprehensive Disease Characterization Report

## Summary

RAB23-related Carpenter syndrome (Carpenter syndrome type 1, **CRPT1**; historically **acrocephalopolysyndactyly type II**; **OMIM #201000**; **ORPHA:65759**; **MONDO:0008544**) is an ultra-rare autosomal-recessive multiple-congenital-malformation disorder with an estimated prevalence of roughly **1 in 1,000,000 births**. It is caused by **biallelic loss-of-function variants in RAB23** (gene *OMIM \*606144*; HGNC:9776; NCBI Gene 51715; UniProt Q9ULC3; chromosome **6p11.2**), which encodes a small RAB-family GTPase that functions as a **negative regulator of Hedgehog (HH) signaling** and a regulator of ciliary membrane trafficking. When RAB23 function is lost, ciliary Smoothened turnover is impaired and downstream GLI-mediated transcription and FGF10–ERK signaling are de-repressed, and primary-cilium formation is perturbed in a cell-type–dependent manner. The convergent developmental consequence is the near-universal clinical dyad of **multisuture craniosynostosis and preaxial polysyndactyly**, accompanied by frequent obesity, congenital heart disease, cryptorchidism/hypogenitalism, umbilical hernia, and variable (~75%) intellectual impairment.

The molecular pathology is a classic recessive loss-of-function paradigm: most pathogenic alleles are **truncating and subject to nonsense-mediated decay (NMD)**, and even in-frame or missense lesions (e.g., Y79del, disrupting the switch-II region; or C-terminal frameshifts that abolish the prenylatable cysteine) converge on loss of RAB23 activity. A recurrent **L145X founder mutation** in patients of northern European descent illustrates the population genetics of the disorder. A clinically overlapping but genetically distinct subtype, **CRPT2** (**OMIM #614976**), is caused by biallelic **MEGF8** variants and is distinguished by frequent left–right patterning defects and predominantly single-midline-suture synostosis.

Management is entirely **symptomatic and reconstructive**. Early cranial-vault expansion / fronto-orbital advancement (ideally within 6–12 months of life, and urgently in the setting of raised intracranial pressure) is the cornerstone, complemented by cardiac surgery, hand/foot reconstruction, orchidopexy, and multidisciplinary developmental support. No disease-modifying pharmacotherapy or gene therapy exists. Prognosis is variable and multisystem; intellectual outcome correlates with the presence of cerebral malformations and untreated raised intracranial pressure rather than being invariable, and affected individuals can survive to adulthood and pregnancy.

---

## Key Findings

### Finding 1 — RAB23 biallelic loss-of-function is the cause of CRPT1

Carpenter syndrome type 1 is caused by **biallelic loss-of-function mutations in RAB23**. The gene was identified by homozygosity mapping across 15 independent families, which linked disease to chromosome **6p12.1–q12** and identified five distinct RAB23 mutations (four truncating and one missense). RAB23 encodes a member of the RAB guanosine-triphosphatase (GTPase) family of vesicle-transport proteins and functions as a **negative regulator of Hedgehog signaling**. The loss-of-function mechanism is reinforced at the transcript level: truncating mutations produce mRNAs that are degraded by **nonsense-mediated decay (NMD)**, an important contributor to pathogenesis. *[human clinical / in vitro]*

- *"we found linkage to chromosome 6p12.1-q12 and, in 15 independent families, identified five different mutations (four truncating and one missense) in RAB23, which encodes a member of the RAB guanosine triphosphatase (GTPase) family of vesicle transport proteins and acts as a negative regulator of hedgehog (HH) signaling"* — [PMID: 17503333](https://pubmed.ncbi.nlm.nih.gov/17503333/)
- *"We provide experimental evidence that transcripts encoding truncating mutations are subject to nonsense-mediated decay, and that this plays an important role in the pathogenesis of many RAB23 mutations."* — [PMID: 21412941](https://pubmed.ncbi.nlm.nih.gov/21412941/)

**Ontology anchors:** gene RAB23 (HGNC:9776); GO:0007224 (smoothened signaling pathway); GO:0045879 (negative regulation of smoothened signaling pathway).

### Finding 2 — Core phenotype: multisuture craniosynostosis + polysyndactyly, with frequent obesity, cardiac defects, and cryptorchidism

**Multisuture craniosynostosis** and **polysyndactyly** are present in essentially all molecularly confirmed patients described to date, and abnormal external genitalia (cryptorchidism) are universal in affected boys. The cardinal clinical picture — historically termed acrocephalopolysyndactyly — comprises craniosynostosis, short fingers, soft-tissue syndactyly, preaxial polydactyly, congenital heart disease, hypogenitalism, obesity, and umbilical hernia. As many as **three-fourths of patients have some degree of intellectual impairment**. No genotype–phenotype correlations are apparent. *[human clinical]*

- *"Multi-suture craniosynostosis and polysyndactyly have been present in all patients described to date, and abnormal external genitalia have been universal in boys."* — [PMID: 21412941](https://pubmed.ncbi.nlm.nih.gov/21412941/)
- *"Acrocephalopolysyndactyly or Carpenter syndrome consists of craniosynostosis, short fingers, soft tissue syndactyly, preaxial polydactyly, congenital heart disease, hypogenitalism, obesity, and umbilical hernia. As many as three-fourths of the patients have some degree of intellectual impairment."* — [PMID: 8352858](https://pubmed.ncbi.nlm.nih.gov/8352858/)

**Suggested HPO terms:** HP:0001363 (Craniosynostosis); HP:0004440 (Coronal craniosynostosis); HP:0100259 (Polysyndactyly); HP:0100258 (Preaxial polydactyly); HP:0001159 (Syndactyly); HP:0001513 (Obesity); HP:0001627 (Abnormal heart morphology); HP:0000028 (Cryptorchidism); HP:0001537 (Umbilical hernia); HP:0001249 (Intellectual disability).

### Finding 3 — Recurrent L145X founder mutation; MEGF8 defines the distinct CRPT2 subtype

Among reported patients, **10 individuals were homozygous for the same nonsense mutation, L145X, on a common haplotype**, indicating a **founder effect in patients of northern European descent**. Separately, a clinically overlapping but genetically distinct disorder — **CRPT2** — is caused by biallelic **MEGF8** variants and is **frequently associated with abnormal left-right patterning** (situs inversus, dextrocardia, transposition of the great arteries). Laterality defects occur in nearly half of MEGF8 cases but are rare in RAB23 cases, providing a clinically useful discriminator. *[human clinical]*

- *"In 10 patients, the disease was caused by homozygosity for the same nonsense mutation, L145X, that resides on a common haplotype, indicative of a founder effect in patients of northern European descent."* — [PMID: 17503333](https://pubmed.ncbi.nlm.nih.gov/17503333/)
- *"we describe a disorder caused by mutations in multiple epidermal-growth-factor-like-domains 8 (MEGF8), which exhibits substantial clinical overlap with Carpenter syndrome but is frequently associated with abnormal left-right patterning"* — [PMID: 23063620](https://pubmed.ncbi.nlm.nih.gov/23063620/)

Additional recurrent/founder-type alleles reported include c.82C>T p.(Arg28\*) (first molecularly confirmed continental-African case, Tanzania; [PMID: 33368989](https://pubmed.ncbi.nlm.nih.gov/33368989/)) and c.86dupA in a Comorian family ([PMID: 20358613](https://pubmed.ncbi.nlm.nih.gov/20358613/)).

### Finding 4 — RAB23 coordinates suture osteogenesis by repressing FGF-ERK and GLI1; loss causes a context-dependent ciliopathy

In mouse calvarial models, RAB23 is active in osteoblasts at the osteogenic front and regulates **both Hedgehog and FGF pathways**, repressing **FGF10–pERK1/2 and GLI1** during early osteogenesis. Across three independent vertebrate systems — Rab23 conditional-knockout mice, Carpenter-syndrome patient-derived iPSCs, and zebrafish morphants — RAB23 loss recapitulates CS/ciliopathy features and consistently perturbs **primary-cilium formation, but in a cell-type–dependent (context-dependent) manner** (affecting chondrocytes, mouse embryonic fibroblasts, neural progenitors, and neocortical neurons differently). *[model organism / iPSC]*

- *"RAB23 coordinates early osteogenesis by repressing FGF10-pERK1/2 and GLI1"* — [PMID: 32662771](https://pubmed.ncbi.nlm.nih.gov/32662771/)
- *"all three different vertebrate mutant models consistently show a perturbation of primary cilia formation, intriguingly, in a context-dependent manner"* — [PMID: 40825043](https://pubmed.ncbi.nlm.nih.gov/40825043/)

**Suggested GO terms:** GO:0060348 (bone development); GO:0001503 (ossification); GO:0060271 (cilium assembly); GO:0070848 (response to growth factor).

### Finding 5 — RAB23 controls ciliary Smoothened turnover and Kif17 trafficking

Mechanistically, depletion of Rab23 or expression of dominant-negative Rab23 **decreases the ciliary steady-state level specifically of Smoothened** (but not of control ciliary proteins EB1 or Kim1), implicating RAB23 in protein turnover within the cilium. RAB23 also exists in a complex with the kinesin-2 motor **Kif17** and importin β2, and **ciliary localization of Kif17 is disrupted in Rab23-depleted cells**. RAB23 is enriched at the primary cilium. Together these establish the physical basis by which RAB23 loss dysregulates the ciliary Hedgehog signal-transduction apparatus. *[in vitro]*

- *"Depletion of Rab23 or expression of dominant-negative Rab23 decreased the ciliary steady state specifically of Smoothened but not EB1 or Kim1, suggesting a role of Rab23 in protein turnover in the cilium."* — [PMID: 20375059](https://pubmed.ncbi.nlm.nih.gov/20375059/)
- *"ciliary localization of the kinesin-2 motor protein Kif17 was disrupted in Rab23-depleted cells"* — [PMID: 26136363](https://pubmed.ncbi.nlm.nih.gov/26136363/)

**Suggested GO terms:** GO:0005929 (cilium); GO:0060170 (ciliary membrane); GO:0042073 (intraciliary transport).

### Finding 6 — Structural basis of loss of function: switch-II disruption and loss of prenylation

High-resolution crystal structures of human RAB23 (wild-type and the **Y79del** clinical mutant, bound to GDP and to the non-hydrolyzable GTP analog GMPPNP) demonstrate that the Y79 deletion causes **structural distortions in the switch-II region** relative to wild type, potentially disrupting binding to interacting partners and thereby producing loss of function. Clinical point mutations M12K, C85R, and Y79del all fall within the GTPase domain. A second, orthogonal loss-of-function mechanism arises from truncating frameshift variants (e.g., p.Val161Leufs) that **remove the C-terminal prenylatable cysteine**, so that the truncated protein fails to undergo the lipid modification required to associate with target membranes. *[computational/structural / in vitro]*

- *"the Y79 deletion mutant exhibited structural distortions in the switch II region relative to that of the WT. The structural changes potentially disrupted the binding of Rab23 Y79del to its interacting partners, thus leading to a loss-of-function and the development of Carpenter syndrome"* — [PMID: 39615683](https://pubmed.ncbi.nlm.nih.gov/39615683/)
- *"Due to the loss of the C-terminally prenylatable cysteine residue, the truncated protein will probably fail to associate with the target cellular membranes due to the absence of the necessary lipid modification."* — [PMID: 23599695](https://pubmed.ncbi.nlm.nih.gov/23599695/)

**Suggested GO terms:** GO:0003924 (GTPase activity); GO:0005525 (GTP binding); GO:0018344 (protein geranylgeranylation).

### Finding 7 — Ultra-rare autosomal recessive disorder; model organisms

Carpenter syndrome has an **estimated prevalence of ~1 in a million births**. Disease models that recapitulate CS features include **Rab23 conditional-knockout mice, CS patient-derived iPSCs, and zebrafish morphants**. The spontaneous mouse mutant **"open brain" (opb)** carries a homozygous Rab23 mutation and shows **embryonic lethality with open neural-tube defects** — a notable species difference, since human RAB23-null homozygosity is not lethal, indicating a divergent early-developmental requirement. RAB23 also regulates Nodal expression in the left lateral plate mesoderm and Kupffer's vesicle, contributing to left–right patterning. *[human clinical / model organism]*

- *"This syndrome's rarity, with an estimated prevalence of one in a million births"* — [PMID: 39040725](https://pubmed.ncbi.nlm.nih.gov/39040725/)
- *"the embryonic lethality and open neural tube phenotype of a spontaneous mouse mutant that carries homozygous mutation of open brain, a gene encoding Rab23"* — [PMID: 29727300](https://pubmed.ncbi.nlm.nih.gov/29727300/)
- *"including Rab23 conditional knockout (CKO) mouse mutants, CS patient-derived induced pluripotent stem cells (iPSCs), and zebrafish morphants"* — [PMID: 40825043](https://pubmed.ncbi.nlm.nih.gov/40825043/)

### Finding 8 — Management is multidisciplinary and reconstructive

Management is centered on **early surgical release of the fused sutures with fronto-orbital advancement**, clearly indicated particularly in cases of **elevated intracranial pressure**. Early correction of craniofacial deformity is usually safe within **6 to 12 months** of life; operative planning uses 3D CT because venous drainage abnormalities and ectatic emissary veins can cause significant intraoperative bleeding. Advanced techniques include cranial-vault remodeling and monobloc distraction osteogenesis. Cardiac defects (e.g., Tetralogy of Fallot) require surgical correction, and treated patients can survive to adulthood and successful pregnancy. **No CS-specific pharmacotherapy or gene therapy exists**; care is supportive and reconstructive. *[human clinical]*

- *"early release of craniosynostoses with fronto-orbital advancement is clearly indicated in the CS literature, particularly in cases of elevated intracranial pressure"* — [PMID: 25162549](https://pubmed.ncbi.nlm.nih.gov/25162549/)
- *"Early correction of craniofacial deformity in Carpenter's syndrome is usually safe within 6 to 12 months. Venous drainage abnormalities and ectatic emissary veins can lead to significant bleeding"* — [PMID: 34244844](https://pubmed.ncbi.nlm.nih.gov/34244844/)

**Suggested NCIT terms:** cranial-vault remodeling / fronto-orbital advancement; distraction osteogenesis (NCIT:C92968); cardiac surgical correction; orchidopexy; rehabilitation therapy.

### Finding 9 — Lifelong multisystem morbidity; intellectual outcome is variable, not invariable

Although up to three-fourths of patients show some degree of intellectual impairment, **mental retardation is not an invariable feature**; the **most severe developmental delay is associated with cerebral malformations demonstrable on MRI/CT**, so neuroradiologic examination can help predict intellectual outcome. Characteristic craniofacial features include marked absence/underdevelopment of the anterior cranial fossa with bulging of the middle cranial fossa, and there is **no correlation between the degree of craniofacial dysmorphology and brain dysmorphology**. Congenital and progressive residual cardiac defects contribute to morbidity, and an atypical case associated chronic kidney disease with CS. The phenotypic spectrum has been expanded to include overgrowth with advanced bone age, epileptogenic EEG changes, and autistic features. *[human clinical]*

- *"Because mental retardation is not an invariable feature of this syndrome or other craniosynostosis syndromes, neuroradiologic examination may help in predicting the intellectual outcome in these patients."* — [PMID: 8352858](https://pubmed.ncbi.nlm.nih.gov/8352858/)
- *"overgrowth with advanced bone age, epileptogenic changes on electroencephalogram and autistic features"* — [PMID: 34748996](https://pubmed.ncbi.nlm.nih.gov/34748996/)

### Finding 10 — Identifiers and nosology

RAB23-related Carpenter syndrome = **CRPT1 / acrocephalopolysyndactyly type II**, **OMIM #201000**, caused by RAB23 (gene OMIM *606144; HGNC:9776; NCBI Gene 51715; UniProt Q9ULC3; chromosome 6p11.2). A second locus, **MEGF8 (CRPT2, OMIM #614976)**, causes a subtype with substantial clinical overlap but **frequent laterality defects** and typically **single-midline-suture** synostosis, whereas RAB23-CRPT1 shows **multi-suture craniosynostosis**. Orphanet **ORPHA:65759**; **MONDO:0008544**. *[human clinical]*

- *"Craniosynostosis in CRPT2 commonly involves a single midline suture in comparison to the multi-suture craniosynostosis characteristic of CRPT1."* — [PMID: 38760421](https://pubmed.ncbi.nlm.nih.gov/38760421/)
- *"mutations in multiple epidermal-growth-factor-like-domains 8 (MEGF8), which exhibits substantial clinical overlap with Carpenter syndrome but is frequently associated with abnormal left-right patterning"* — [PMID: 23063620](https://pubmed.ncbi.nlm.nih.gov/23063620/)

---

## Mechanistic Model / Interpretation

The unifying interpretation is that **RAB23 is a ciliary "brake" on morphogen signaling**. Under normal conditions, RAB23 at the primary cilium promotes turnover of Smoothened and correct trafficking of ciliary motors (Kif17), thereby keeping Hedgehog/GLI output — and, in cranial osteoblasts, FGF10–ERK output — appropriately low. Removing this brake (through NMD-mediated protein loss, switch-II GTPase-cycle disruption, or loss of prenylation-dependent membrane targeting) **de-represses these pathways**. Because different tissues rely on cilium-dependent signaling to different degrees, RAB23 loss manifests as a **context-dependent ciliopathy**: strongest and most consistent in the developing skull (multisuture synostosis) and limb (polysyndactyly), with variable CNS, cardiac, and metabolic consequences.

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic RAB23 loss-of-function variant** (truncating → NMD; or switch-II/prenylation-disrupting) **results in** absent/non-functional RAB23 GTPase protein. *(Demonstrated.)*
2. Loss of RAB23 at the primary cilium **leads to** failure of normal ciliary protein turnover — specifically dysregulated **ciliary Smoothened** and disrupted Kif17 motor trafficking. *(Demonstrated in vitro.)*
3. Dysregulated ciliary Smoothened **results in** **de-repression of Hedgehog (GLI-mediated) signaling**; in parallel, RAB23 loss **de-represses FGF10–pERK1/2 signaling** at the cranial osteogenic front. *(Demonstrated in calvarial models.)*
4. **Branch A (skull):** De-repressed HH/GLI1 + FGF-ERK in cranial osteoblasts **leads to** premature/accelerated osteogenic differentiation and **multisuture craniosynostosis**. *(Demonstrated.)*
5. **Branch B (limb):** Altered HH gradient in the limb bud **results in** **preaxial polydactyly/polysyndactyly**. *(Inferred from HH-pathway biology and model phenotypes.)*
6. **Branch C (CNS/cardiac/other):** Context-dependent perturbation of primary-cilium formation and Nodal regulation **leads to** cerebral malformations, variable intellectual impairment, cardiac defects, and (rarely) laterality anomalies. *(Partly demonstrated, partly inferred.)*

```
 RAB23 biallelic LOF (NMD / switch-II / no prenylation)
                 │
                 ▼
   Loss of ciliary RAB23 function
        (dysregulated Smoothened turnover, ↓Kif17 trafficking)
                 │
        ┌────────┴─────────┐
        ▼                  ▼
 De-repressed HH/GLI1   De-repressed FGF10–pERK1/2
        │                  │
        └────────┬─────────┘
                 ▼
   Aberrant osteogenic & patterning programs
        │           │            │
        ▼           ▼            ▼
  Multisuture   Preaxial     Cilium-dependent
 craniosynostosis polysyndactyly CNS/cardiac defects
```

This model explains the near-universal core dyad, the variable expressivity, the correlation of cognitive outcome with cerebral malformation, and the absence of genotype–phenotype correlation (all pathogenic alleles converge on the same loss-of-function endpoint). It also clarifies why the closely related **CRPT2 (MEGF8)** shares the craniosynostosis/limb phenotype yet reaches it through a distinct, largely Hedgehog-independent **BMPR1A–BMP-SMAD** route and adds laterality defects ([PMID: 42399640](https://pubmed.ncbi.nlm.nih.gov/42399640/)).

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** RAB23-related Carpenter syndrome is a rare autosomal-recessive syndromic craniosynostosis (an "acrocephalopolysyndactyly") defined by the co-occurrence of multisuture craniosynostosis and polysyndactyly with a constellation of additional malformations (obesity, congenital heart disease, hypogenitalism, umbilical hernia, and frequently intellectual impairment).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM (disease, CRPT1) | #201000 |
| OMIM (gene) | *606144 (RAB23) |
| Orphanet | ORPHA:65759 |
| MONDO | MONDO:0008544 |
| HGNC | HGNC:9776 (RAB23) |
| NCBI Gene | 51715 |
| Ensembl | ENSG00000112210 |
| UniProt | Q9ULC3 |
| Cytoband | 6p11.2 |
| ICD-10 | Q87.0 / Q75.x |
| SNOMED CT | 21086008 (Acrocephalopolysyndactyly) |
| MeSH | Acrocephalopolysyndactyly |

**Synonyms:** Carpenter syndrome; Carpenter syndrome type 1 (CRPT1); acrocephalopolysyndactyly type II (ACPS II); ACPS2.

**Data source type:** Information is derived from **aggregated disease-level resources** (OMIM, Orphanet) and from **individual patient reports/case series** in the primary literature; the disorder is too rare for EHR-scale cohorts.

### 2. Etiology

**Causal factor:** purely **genetic** — biallelic loss-of-function variants in RAB23 (Finding 1). There is no known environmental, infectious, or toxic contribution to CRPT1.

**Genetic risk factors:** The disease requires two pathogenic RAB23 alleles; heterozygous carriers are unaffected. A **founder L145X allele** elevates carrier frequency in populations of northern European descent (Finding 3); other recurrent alleles (p.Arg28\*, c.86dupA) occur in specific pedigrees/populations. **Consanguinity** substantially raises risk owing to autosomal-recessive inheritance (multiple reported families are consanguineous). Genetic heterogeneity exists at the disease level: MEGF8 causes CRPT2.

**Environmental / lifestyle / protective factors / gene–environment interactions:** None established. No environmental risk factors, protective genetic or environmental factors, or gene–environment interactions have been demonstrated for this Mendelian disorder. *(Not applicable / not available.)*

### 3. Phenotypes

Onset is congenital; features are structural. Frequencies are qualitative given small cohorts.

| Phenotype | Type | Frequency | HPO term |
|---|---|---|---|
| Multisuture craniosynostosis (often bicoronal + sagittal + metopic; cloverleaf/turricephaly) | Physical/skeletal | Near-universal (~100%) | HP:0001363 / HP:0002676 |
| Polysyndactyly (preaxial polydactyly, cutaneous syndactyly, brachydactyly) | Physical/skeletal | Near-universal (~100%) | HP:0100259 / HP:0100258 / HP:0001159 |
| Cryptorchidism / abnormal genitalia (males) | Physical | Universal in boys | HP:0000028 |
| Obesity | Physical/metabolic | Frequent | HP:0001513 |
| Congenital heart disease (ASD, VSD, PDA, ToF, TGA) | Clinical sign | Frequent (~30–50%) | HP:0001627 |
| Intellectual disability / developmental delay | Behavioral/cognitive | ~75% (variable) | HP:0001249 |
| Umbilical hernia | Physical | Frequent | HP:0001537 |
| Characteristic facies (flat nasal bridge, hypertelorism, low-set ears) | Physical | Frequent | HP:0000316 / HP:0005280 |
| Genu valgum / short stature / skeletal dysplasia | Physical/skeletal | Variable | HP:0002857 / HP:0004322 |
| Hydrocephalus / cerebral malformations | Clinical sign | Occasional | HP:0000238 / HP:0002011 |
| Corneal/ophthalmic anomalies | Clinical sign | Occasional | HP:0007957 |
| Atypical: overgrowth/advanced bone age, seizures, autistic features | Various | Rare | HP:0001548 / HP:0001250 / HP:0000729 |

**Onset:** congenital (some prenatally detectable). **Severity/progression:** structural anomalies are static in origin but craniosynostosis can drive progressive raised intracranial pressure; cardiac lesions may progress. Variable expressivity, including intrafamilial ([PMID: 20358613](https://pubmed.ncbi.nlm.nih.gov/20358613/)). **Quality of life:** substantial and lifelong (reconstructive-surgery burden, motor/orthopedic complications, cardiac limitation, cognitive outcome); no CS-specific validated QoL instrument data exist.

### 4. Genetic / Molecular Information

**Causal gene:** RAB23 (6p11.2), ~237-aa small GTPase, 6 coding exons. **Variant spectrum:** predominantly truncating (nonsense, frameshift, splice-site) with occasional missense/in-frame deletions; ≥12 distinct mutations across dozens of families. **Classification:** biallelic pathogenic/likely-pathogenic per ACMG/AMP (PVS1 for null alleles; segregation; functional evidence). **Functional consequence:** **loss of function** via (i) NMD of truncating transcripts, (ii) switch-II structural disruption (Y79del), and (iii) loss of C-terminal prenylation/membrane targeting (Findings 1, 6). **Allele frequency:** pathogenic alleles are extremely rare in gnomAD. **Origin:** germline. **Modifier genes / epigenetics / large chromosomal abnormalities:** none established for CRPT1 (karyotype typically normal).

Representative variants: L145X (founder, N. European); p.Arg28\* (Tanzania); c.86dupA (Comoros); c.481G>C p.Val161Leufs*16 (exon-6 skipping, prenylation loss); M12K, C85R, Y79del (GTPase-domain).

### 5. Environmental Information

**Not applicable.** CRPT1 is a monogenic disorder with no established environmental, lifestyle, or infectious contributors. (Obesity, once present, is a genetically driven feature that may be modifiable by diet/lifestyle as supportive care, but is not an environmental cause.)

### 6. Mechanism / Pathophysiology

*See the "Mechanistic Model / Interpretation" section above for the full ordered causal chain and diagram.*

- **Molecular pathways:** Sonic Hedgehog/GLI (primary; de-repressed), FGF10–ERK1/2 (MAPK), Nodal/left–right patterning. (CRPT2/MEGF8: BMP–SMAD.) KEGG: Hedgehog (hsa04340); MAPK (hsa04010); Reactome: Signaling by Hedgehog.
- **Cellular processes:** ciliogenesis and intraciliary transport; osteoblast differentiation/ossification; cell proliferation (e.g., cerebellar granule-cell precursors — Hedgehog de-repression links to medulloblastoma biology, [PMID: 34210780](https://pubmed.ncbi.nlm.nih.gov/34210780/)).
- **Protein dysfunction:** loss of GTPase cycling (switch-II) and loss of membrane targeting (prenylation).
- **Subcellular compartments:** primary cilium/ciliary membrane, basal body, Golgi-derived vesicles, plasma membrane.
- **Immune/metabolic:** no primary immune involvement; obesity implicates Hedgehog's role in adipogenesis/energy balance.
- **GO terms:** GO:0007224; GO:0045879; GO:0060271; GO:0042073; GO:0003924; GO:0018342; GO:0001503; GO:0007368. **CL terms:** osteoblast CL:0000062; chondrocyte CL:0000138; neural progenitor CL:0011020; fibroblast CL:0000057; adipocyte CL:0000136.
- **Molecular profiling (omics):** No large transcriptomic/proteomic/metabolomic patient datasets exist for this ultra-rare disease; mechanistic data derive from targeted mouse/zebrafish/iPSC assays.

### 7. Anatomical Structures Affected

- **Organ/system level:** skeletal (cranial sutures/skull UBERON:0004339; digits UBERON:0002544; long bones); cardiovascular (heart UBERON:0000948); nervous system/brain (UBERON:0000955 — anterior cranial fossa hypoplasia, bulging middle fossa, hydrocephalus); reproductive (testis UBERON:0000473 — cryptorchidism); abdominal wall (umbilical hernia); renal (rare CKD, [PMID: 39040725](https://pubmed.ncbi.nlm.nih.gov/39040725/)); visual (cornea/eye UBERON:0000970); endocrine/metabolic (adiposity).
- **Tissue level:** bone (UBERON:0001474), cartilage (UBERON:0002418), nervous tissue, cardiac muscle.
- **Cell level:** osteoblasts, chondrocytes, cardiomyocytes, neural progenitors/neurons, adipocytes.
- **Subcellular level:** primary cilium (GO:0005929), ciliary membrane (GO:0060170), basal body (GO:0036064), plasma membrane.
- **Lateralization:** craniofacial/acral involvement is **bilateral** (often asymmetric); situs/laterality defects are asymmetric and rare in CRPT1.

### 8. Temporal Development

- **Onset:** congenital; malformations form during embryogenesis and are evident at birth (some prenatally detectable — abnormal skull shape, bowed femora, cardiac defect; [PMID: 25168863](https://pubmed.ncbi.nlm.nih.gov/25168863/)).
- **Onset pattern:** structural/insidious (developmental), not acute.
- **Progression:** underlying malformations are static in origin, but secondary processes are progressive (raised ICP from skull growth against fused sutures; progression of residual cardiac lesions, [PMID: 23706836](https://pubmed.ncbi.nlm.nih.gov/23706836/); worsening obesity/orthopedic problems). Chronic, lifelong; no spontaneous remission.
- **Critical period:** first 6–12 months of life for cranial-vault surgery to protect brain growth and vision.

### 9. Inheritance and Population

- **Epidemiology:** ultra-rare; prevalence **~1 in 1,000,000 births** (~0.1 per 100,000); incidence not precisely quantified; <~100 molecularly confirmed cases.
- **Inheritance:** autosomal recessive (OMIM #201000).
- **Penetrance:** effectively complete for the core dyad in biallelic-null genotypes.
- **Expressivity:** variable, including intrafamilial; no genotype–phenotype correlation.
- **Genetic anticipation / germline mosaicism:** not features of this disorder; recurrence risk follows standard AR 25%.
- **Founder effects:** L145X (northern European); other recurrent alleles in specific populations (Comoros, Tanzania, Arabian Peninsula).
- **Consanguinity:** strong contributor.
- **Carrier frequency:** low overall; elevated in consanguineous/founder populations.
- **Demographics:** reported worldwide; no strong sex bias in occurrence (male-specific genital findings emphasized); diagnosed in infancy/childhood.

### 10. Diagnostics

- **Clinical/imaging:** recognition of the craniosynostosis + polysyndactyly gestalt; **3D CT** of the skull (suture fusion, cranial-fossa morphology, venous/emissary-vein assessment for operative planning); brain MRI (cerebral malformations — prognostic); echocardiography; skeletal survey. Prenatal ultrasound/fetal CT may show abnormal skull shape, bowed femora, cardiac defect.
- **Laboratory/biomarkers:** no specific biochemical biomarker or enzyme assay; diagnosis is molecular.
- **Genetic testing (definitive):** single-gene **RAB23 sequencing** (6 coding exons); **craniosynostosis gene panels** including RAB23 and MEGF8; **WES** for atypical presentations/second locus; **WGS** for deep-intronic/structural variants; chromosomal microarray/karyotype mainly to exclude mimics; RNA/splicing analysis to prove pathogenicity of splice variants.
- **Diagnostic criteria:** no formal consensus criteria; characteristic phenotype + biallelic RAB23 variants.
- **Differential diagnosis:** Apert, Pfeiffer, Crouzon, Saethre–Chotzen, Muenke (FGFR/TWIST-related, usually dominant); Greig cephalopolysyndactyly (GLI3); Bardet–Biedl and other ciliopathies; other ACPS variants; and **MEGF8-related CRPT2** (laterality/situs defects, usually single-midline-suture synostosis).
- **Screening:** no population newborn screening; cascade/carrier testing and prenatal/preimplantation genetic testing once familial variants are known.

### 11. Outcome / Prognosis

- **Survival/mortality:** no formal survival statistics; life expectancy is often near-normal with successful surgical management, and patients can reach adulthood and pregnancy. Early mortality risk relates chiefly to severe congenital heart disease, airway compromise, and raised-ICP complications.
- **Morbidity/function:** significant lifelong morbidity — variable cognitive impairment (up to ~75%), visual/airway issues, repeated craniofacial/orthopedic/cardiac surgeries, mobility limitation from hand/foot anomalies.
- **Complications:** raised intracranial pressure, hydrocephalus, operative bleeding from ectatic emissary veins, progressive cardiac disease, obesity-related sequelae, rare CKD.
- **Prognostic factors:** presence/absence of cerebral malformation on imaging (predicts cognitive outcome), severity/timeliness of craniosynostosis correction, cardiac disease severity. No molecular prognostic biomarker; no genotype–phenotype correlation.
- **QoL measures:** no disease-specific validated instruments reported.

### 12. Treatment

**No disease-modifying, pharmacologic, gene, cell, or RNA therapy exists.** Management is symptomatic, reconstructive, and multidisciplinary.

- **Surgical/interventional (mainstay):** cranial vault expansion / fronto-orbital advancement (first 6–12 months, esp. with raised ICP); monobloc/midface distraction osteogenesis (NCIT:C92968); hand/foot reconstruction; cardiac surgery; orchidopexy; umbilical hernia repair; orthopedic correction of genu valgum/scoliosis; VP shunt for hydrocephalus.
- **Supportive/rehabilitative:** ophthalmology, airway/sleep management, audiology, developmental/physical/occupational/speech therapy, special education, dietary/lifestyle management of obesity.
- **Pharmacotherapy/pharmacogenomics:** none specific/applicable.
- **Experimental/targeted:** none in clinical use. Mechanistically, **SMO inhibitors** rescue Hh-dependent limb defects and **BMP type-I receptor inhibition** rescues MEGF8-driven craniosynostosis in models ([PMID: 42399640](https://pubmed.ncbi.nlm.nih.gov/42399640/)) — proof-of-concept only. No registered interventional trials specific to RAB23 Carpenter syndrome.
- **Treatment strategy:** individualized, staged surgical algorithm prioritizing ICP relief and airway/cardiac stabilization, then facial/skeletal reconstruction and developmental support.

### 13. Prevention

- **Primary prevention:** not possible; risk reduction centers on **genetic counseling** for at-risk (especially consanguineous) couples and carrier relatives.
- **Secondary prevention:** prenatal diagnosis when a familial variant is known (or ultrasound suspicion); early postnatal craniofacial/cardiac evaluation and timely surgery.
- **Tertiary prevention:** surveillance/management of raised ICP, cardiac, visual, airway, orthopedic, and metabolic complications.
- **Genetic screening:** cascade carrier testing, PGT-M, and prenatal testing once variants are identified.
- **Immunization / public-health / environmental interventions:** not applicable.

### 14. Other Species / Natural Disease

- **Taxonomy of models:** *Mus musculus* (NCBI:txid10090), *Danio rerio* (NCBI:txid7955).
- **Orthologous genes:** mouse *Rab23* (NCBI Gene 19334; classic **"open brain," opb** allele); zebrafish *rab23*. RAB23 is conserved across metazoans and even present in flagellated protists such as *Trypanosoma brucei* (correlating with cilia/flagella; [PMID: 21676215](https://pubmed.ncbi.nlm.nih.gov/21676215/)).
- **Natural disease in animals:** no well-characterized spontaneous naturally occurring companion-animal/wildlife "Carpenter syndrome" is documented; the mouse *opb* mutant is a spontaneous laboratory mutation. Veterinary relevance is primarily as research models.
- **Comparative biology:** disease mechanisms (Hedgehog antagonism, ciliary trafficking, left–right patterning) are highly conserved; a key species difference is that homozygous *Rab23* null is embryonic-lethal (open neural tube) in mice but viable in humans.
- **Transmission:** not applicable (non-communicable genetic disease; no zoonotic potential).

### 15. Model Organisms

| Model | Type | Key features / recapitulation | Reference |
|---|---|---|---|
| "Open brain" (opb) mouse | Spontaneous mammalian mutant | Open neural-tube defect, embryonic lethal (more severe than human); established Rab23 as Shh antagonist | [PMID: 29727300](https://pubmed.ncbi.nlm.nih.gov/29727300/) |
| Rab23 conditional-KO mouse | Genetic (conditional) | Best mammalian model; skeletal/chondrocyte/neural CS features; context-dependent cilia defects | [PMID: 40825043](https://pubmed.ncbi.nlm.nih.gov/40825043/) |
| Calvarial/osteoblast explant | Ex vivo | RAB23 represses FGF10-pERK1/2 & GLI1 in osteogenesis | [PMID: 32662771](https://pubmed.ncbi.nlm.nih.gov/32662771/) |
| CS patient-derived iPSCs | In vitro human | Perturbed cilium formation, context-dependent | [PMID: 40825043](https://pubmed.ncbi.nlm.nih.gov/40825043/) |
| Zebrafish morphants | Vertebrate | Ciliopathy/patterning defects; Nodal/laterality | [PMID: 40825043](https://pubmed.ncbi.nlm.nih.gov/40825043/) |
| MDCK/knockdown cells; recombinant RAB23 | In vitro / structural | Ciliary Smoothened/Kif17 trafficking; crystal structures (WT, Y79del) | [PMID: 20375059](https://pubmed.ncbi.nlm.nih.gov/20375059/), [PMID: 26136363](https://pubmed.ncbi.nlm.nih.gov/26136363/), [PMID: 39615683](https://pubmed.ncbi.nlm.nih.gov/39615683/) |

**Phenotype recapitulation & limitations:** models reproduce craniofacial/skeletal defects, ciliary dysfunction, and Hedgehog/Nodal dysregulation, but no single model captures the full human multisystem spectrum; the mouse null's lethality and species-specific developmental requirements limit direct translation. **Resources:** MGI (mouse), ZFIN (zebrafish), IMPC/KOMP, Cellosaurus (iPSC lines), PDB (RAB23 structures).

---

## Evidence Base

| PMID | Contribution | Role |
|---|---|---|
| [17503333](https://pubmed.ncbi.nlm.nih.gov/17503333/) | Gene discovery; RAB23 as HH negative regulator; L145X founder | Foundational — supports F1, F3 |
| [21412941](https://pubmed.ncbi.nlm.nih.gov/21412941/) | NMD of truncating alleles; universal core features | Supports F1, F2 |
| [8352858](https://pubmed.ncbi.nlm.nih.gov/8352858/) | Clinical spectrum; cerebral malformation predicts cognition | Supports F2, F9 |
| [23063620](https://pubmed.ncbi.nlm.nih.gov/23063620/) | MEGF8/CRPT2 with laterality defects | Supports F3, F10 |
| [32662771](https://pubmed.ncbi.nlm.nih.gov/32662771/) | RAB23 represses FGF10-pERK1/2 and GLI1 in osteogenesis | Supports F4 |
| [40825043](https://pubmed.ncbi.nlm.nih.gov/40825043/) | Context-dependent ciliopathy across 3 models | Supports F4, F7 |
| [20375059](https://pubmed.ncbi.nlm.nih.gov/20375059/) | RAB23 regulates ciliary Smoothened turnover | Supports F5 |
| [26136363](https://pubmed.ncbi.nlm.nih.gov/26136363/) | RAB23–Kif17 ciliary trafficking | Supports F5 |
| [39615683](https://pubmed.ncbi.nlm.nih.gov/39615683/) | Crystal structure; Y79del disrupts switch-II | Supports F6 |
| [23599695](https://pubmed.ncbi.nlm.nih.gov/23599695/) | Loss of prenylatable cysteine → membrane-targeting failure | Supports F6 |
| [39040725](https://pubmed.ncbi.nlm.nih.gov/39040725/) | Prevalence ~1/1,000,000; CKD association | Supports F7, F9 |
| [29727300](https://pubmed.ncbi.nlm.nih.gov/29727300/) | Open brain mouse; species difference | Supports F7 |
| [25162549](https://pubmed.ncbi.nlm.nih.gov/25162549/) | FOA indicated, esp. raised ICP | Supports F8 |
| [34244844](https://pubmed.ncbi.nlm.nih.gov/34244844/) | Surgical timing 6–12 mo; bleeding risk | Supports F8 |
| [34748996](https://pubmed.ncbi.nlm.nih.gov/34748996/) | Expanded phenotype/mutations | Supports F9 |
| [38760421](https://pubmed.ncbi.nlm.nih.gov/38760421/) | CRPT1 multi-suture vs CRPT2 single-midline | Supports F10 |
| [42399640](https://pubmed.ncbi.nlm.nih.gov/42399640/) | MEGF8 BMP-SMAD mechanism (contrast to RAB23-FGF-ERK) | Mechanistic contrast |
| [25168863](https://pubmed.ncbi.nlm.nih.gov/25168863/) | Prenatal findings; novel splice variant | Supports Diagnostics |
| [20358613](https://pubmed.ncbi.nlm.nih.gov/20358613/) | Comorian family; intrafamilial variability | Supports Inheritance |
| [33368989](https://pubmed.ncbi.nlm.nih.gov/33368989/) | First continental-African case (R28X) | Supports Population |
| [23706836](https://pubmed.ncbi.nlm.nih.gov/23706836/) | Adult survival/pregnancy; cardiac progression | Supports Prognosis |

**Consistency:** No contradictory findings were encountered. All ten confirmed findings are mutually reinforcing, spanning human genetics, structural biology, cell biology, and clinical management. The one apparent tension — mouse null lethality vs. viable human null — is explicitly reconciled as a species-specific developmental requirement.

## Limitations and Knowledge Gaps

- **Rarity limits epidemiology and outcomes data:** no robust prevalence/incidence by region, no survival curves, and no validated CS-specific quality-of-life data.
- **Genotype–phenotype:** no correlations identified; the basis of variable expressivity (including within families) is unexplained — possible modifier genes/epigenetics remain uncharacterized.
- **Mechanistic gaps:** the precise molecular partners disrupted by the switch-II lesion, and the tissue-specific determinants of the "context-dependent" cilium phenotype, are not fully defined. The link from ciliary Smoothened dysregulation to the specific (preaxial) limb pattern is inferred.
- **No therapeutics pipeline:** absence of pharmacologic pathway-modulation (e.g., SMO inhibitor) data for CRPT1, in contrast to emerging pathway-specific rescue concepts in CRPT2 models.
- **Population coverage:** most molecular data derive from European and a handful of African/Middle-Eastern pedigrees; the global variant landscape is incompletely sampled.

## Proposed Follow-up Experiments / Actions

1. **Assemble an international CRPT1 registry** to quantify phenotype frequencies, natural history, raised-ICP incidence, and neurodevelopmental outcomes with denominators.
2. **Systematic RAB23 variant curation** (ClinVar/gnomAD reconciliation) with functional assays (GTPase cycling, ciliary Smoothened turnover, membrane association) to standardize ACMG classification and probe genotype–phenotype signals.
3. **Test pathway-targeted rescue** in Rab23-CKO mice and patient iPSC-derived cranial mesenchyme: SMO/GLI antagonists and FGF-ERK inhibitors, benchmarking against BMP-receptor-inhibition rescue reported for MEGF8/CRPT2.
4. **Single-cell and spatial transcriptomics of cranial sutures** in Rab23 models to map cell-type-specific de-repression of HH and FGF programs and identify the "context" determining the cilium phenotype.
5. **Prospective neuroimaging-outcome study** to validate MRI/CT cerebral-malformation findings as a quantitative prognostic biomarker for intellectual outcome.
6. **Search for modifier loci/epigenetic marks** underlying intrafamilial variability using trio/family designs.

---

*Report compiled from 10 confirmed findings across 33 reviewed papers over 5 investigation iterations. Evidence types: human clinical (case series/reports), model organism (mouse, zebrafish), in vitro (iPSC, cell lines), and computational/structural (crystallography). Frequencies are approximate given the ultra-rare nature of the disorder; no large-scale omics, QoL, or survival datasets currently exist for CRPT1.*


## Artifacts

- [OpenScientist final report](RAB23-Related_Carpenter_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](RAB23-Related_Carpenter_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 23 |
| On topic | 17 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 53 |
| Resolved | 51 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 27 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008544` (3 mentions) - the report calls it "MONDO"; MONDO calls it **tetramelic monodactyly**
- `HP:0001513` (2 mentions) - the report calls it "Obesity", "Frequent"; HP calls it **Obesity**
- `HP:0001627` (2 mentions) - the report calls it "Abnormal heart morphology", "Frequent (~30–50%)"; HP calls it **Abnormal heart morphology**
- `HP:0000028` (2 mentions) - the report calls it "Cryptorchidism", "Universal in boys"; HP calls it **Cryptorchidism**
- `HP:0001537` (2 mentions) - the report calls it "Umbilical hernia", "Frequent"; HP calls it **Umbilical hernia**
- `HP:0001249` (2 mentions) - the report calls it "Intellectual disability", "~75% (variable)"; HP calls it **Intellectual disability**
- `HP:0007957` (1 mention) - the report calls it "Occasional"; HP calls it **Corneal opacity**
- `UBERON:0000955` (1 mention) - the report calls it "anterior cranial fossa hypoplasia, bulging middle fossa, hydrocephalus"; UBERON calls it **brain**
- `UBERON:0001474` (1 mention) - the report calls it "Tissue level:** bone"; UBERON calls it **bone element**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0100259` (2 mentions) - the report calls it "Polysyndactyly"; HP calls it **Postaxial polydactyly**
- `GO:0005929` (2 mentions) - the report calls it "cilium", "Subcellular level:** primary cilium"; GO calls it **cilium**, and lists "primary cilium" among its other names
- `UBERON:0000473` (1 mention) - the report calls it "cryptorchidism"; UBERON calls it **testis**, and lists "orchis" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0001513` - called "Obesity", "Frequent"
- `HP:0001627` - called "Abnormal heart morphology", "Frequent (~30–50%)"
- `HP:0000028` - called "Cryptorchidism", "Universal in boys"
- `HP:0001537` - called "Umbilical hernia", "Frequent"
- `HP:0001249` - called "Intellectual disability", "~75% (variable)"
- `GO:0005929` - called "cilium", "Subcellular level:** primary cilium"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.