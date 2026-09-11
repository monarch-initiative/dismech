---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-06T05:46:32.422403'
end_time: '2026-09-06T06:04:54.801967'
duration_seconds: 1102.38
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hypertrophic Cardiomyopathy 1
  mondo_id: MONDO:0008647
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 47
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 20
  on_topic: 13
  validator_version: 0.2.1
term_validation:
  total_terms: 54
  verified: 49
  not_found: 2
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.039
  labels_checked: 13
  labels_matching: 0
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: MONDO:0008647
    reported_labels:
    - if available
    ontology_label: hypertrophic cardiomyopathy 1
  - term_id: HP:0031797
    reported_labels:
    - Incomplete penetrance
    ontology_label: Clinical course
  - term_id: HP:0001639
    reported_labels:
    - Sign; age-dependent, variable; defining overt phenotype
    ontology_label: Hypertrophic cardiomyopathy
  - term_id: HP:0001645
    reported_labels:
    - Severe outcome, uncommon with modern management
    ontology_label: Sudden cardiac death
  - term_id: NCIT:C139785
    reported_labels:
    - Gene Editing
    ontology_label: Uterine Corpus Carcinoma and Carcinosarcoma pN2a TNM Finding v8
  - term_id: HP:0005117
    reported_labels:
    - Functional sign; commonly progressive with remodeling
    ontology_label: Elevated diastolic blood pressure
  - term_id: HP:0001681
    reported_labels:
    - Symptom, often exertional/microvascular
    ontology_label: Angina pectoris
  - term_id: HP:0001279
    reported_labels:
    - Episodic symptom
    ontology_label: Syncope
  - term_id: HP:0031604
    reported_labels:
    - Imaging/pathology sign; variable and progressive
    ontology_label: Agenesis of the carotid canal
  - term_id: HP:0001644
    reported_labels:
    - Late complication in a minority
    ontology_label: Dilated cardiomyopathy
  labels_variant: 3
  unresolved_terms:
  - NCIT:C29622
  - NCIT:C151608
  unresolvable_prefixes:
  - OMIM
  - LOINC
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Hypertrophic_Cardiomyopathy_1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypertrophic Cardiomyopathy 1
- **MONDO ID:** MONDO:0008647 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hypertrophic Cardiomyopathy 1** covering all of the
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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypertrophic Cardiomyopathy 1
- **MONDO ID:** MONDO:0008647 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hypertrophic Cardiomyopathy 1** covering all of the
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


# Hypertrophic Cardiomyopathy 1 (MYH7-related): comprehensive disease-characteristics report

## Executive summary and scope

**Hypertrophic cardiomyopathy 1 (HCM1)** is the historical locus-specific form of familial hypertrophic cardiomyopathy caused by heterozygous pathogenic variants in **MYH7**, which encodes β-cardiac myosin heavy chain. It should not be conflated with all hypertrophic cardiomyopathy (HCM), a genetically heterogeneous phenotype involving multiple sarcomeric genes and phenocopies. Open Targets identifies MYH7 as the strongest-scoring target associated with broad HCM, but also associates MYBPC3 and other genes with the general phenotype. Unless explicitly marked “MYH7-specific,” clinical recommendations below derive from broad-HCM cohorts and guidelines and are extrapolated to HCM1 (OpenTargets Search: hypertrophic cardiomyopathy-MYH7).

The following table summarizes ontology-ready findings.

| Domain | Ontology/Identifiers | High-Confidence Finding | Evidence & Quantitative Value | Caveat (Broad vs MYH7) |
|---|---|---|---|---|
| Disease Scope | MONDO:0005045 (HCM), OMIM:192600 (HCM1) | Hypertrophic cardiomyopathy 1 represents locus-specific MYH7-related familial HCM, a subset of the broader HCM phenotype. | OpenTargets maps MYH7 strongly to broad HCM; MYH7 variants account for ~15% of all clinical HCM cases and ~30-40% of sarcomere-positive cases (OpenTargets Search: hypertrophic cardiomyopathy-MYH7, hao2026hypertrophiccardiomyopathycomprehensive pages 1-2, pietsch2024investigationofmicrotubule pages 32-35). | MYH7-specific finding. Broad HCM includes multiple other genes (e.g., MYBPC3). |
| Etiology / Genetics | HGNC:7577 (MYH7), NCIT:C25742 (Autosomal Dominant) | Pathogenic variants are primarily missense mutations clustered in the beta-myosin heavy chain (β-MHC) head domain (aa 167-931) altering contractile function. | Molecular mapping/sequencing: Missense clustering in motor/actin-binding domains correlates with disease (pires2025exploringmyh7in pages 1-1). | MYH7-specific. Loss-of-function/null variants lack sufficient evidence for pathogenicity (pires2025exploringmyh7in pages 1-1). |
| Penetrance | HP:0031797 (Incomplete penetrance) | Incomplete, age-dependent autosomal dominant penetrance. Penetrance is higher in clinical/family contexts than in incidental populations. | Meta-analysis: ~65% penetrance in nonproband relatives (highest among sarcomere genes); ~11% in incidental population carriers; 23% short-term conversion (topriceanu2024metaanalysisofpenetrance pages 1-2). | MYH7-specific. Modifiers (genetic/environmental) heavily influence transition to overt disease. |
| Molecular Pathophysiology | GO:0006936 (Muscle contraction), GO:0005739 (Mitochondrion), CL:0000746 (Cardiac muscle cell) | MYH7 mutations induce hypercontractility, increased mitochondrial respiration, and stromal activation via EGFR-mediated paracrine signaling leading to fibrosis. | In vitro/iPSC models: MYH7 G256E disrupts folded-back state, increasing active heads by 33%; MYH7 R403Q increases collagen I by 40% and tissue stiffness (ewoldt2024hypertrophiccardiomyopathy–associatedmutations pages 1-2, lee2024incompletepenetranthypertrophiccardiomyopathy pages 1-2). | MYH7-specific mechanistic pathway demonstrated in engineered tissues. |
| Phenotypes / Natural History | HP:0001639 (HCM), HP:0001645 (SCD), HP:0001714 (Ventricular tachycardia) | Asymmetric septal hypertrophy, earlier onset, and higher severity/SCD risk compared to other sarcomere genes. | Registry/cohort data: MYH7 carriers have ~2x SCD incidence vs genotype-negative, median onset ~35 years, increased atrial fibrillation (santos2025geneticclinicaland pages 9-10, hao2026hypertrophiccardiomyopathycomprehensive pages 2-4). | MYH7-specific relative severity. LVOT obstruction and HF occur in broad HCM. |
| Diagnostics | NCIT:C116499 (Echocardiography), NCIT:C116496 (CMR), LOINC:34532-2 (ECG) | Diagnosis via LV wall thickness ≥15mm; CMR assesses LGE/fibrosis for sudden death risk. Cascade screening requires regular echo surveillance if genetics uncertain. | Clinical guidelines: Dynamic LVOT obstruction provocation; 48h Holter for NSVT (mobiuswinkler2024thediagnosisand pages 2-3, fernandes2024guidelinesonthe pages 24-26). | Broad HCM evidence. Applicable to MYH7, but not locus-exclusive. |
| Pharmacotherapy | NCIT:C66946 (Mavacamten), NCIT:C29622 (Beta Blocker) | Cardiac myosin inhibitors (mavacamten, aficamten) target hypercontractility, improving LVOT gradients and NYHA class; LVEF monitoring required. | SEQUOIA-HCM (aficamten): >80% on high dose, 4.9% required dose reduction for LVEF <50%. VALOR-HCM (mavacamten): sustained SRT freedom (coats2024dosingandsafety pages 1-2, desai2025mavacamteninpatients pages 10-11, coats2024dosingandsafety pages 2-4). | Broad HCM evidence. Myosin inhibitors specifically target sarcomeric hypercontractility. |
| Interventional Therapies | NCIT:C151608 (ICD), NCIT:C177729 (Septal Reduction Therapy) | Septal reduction (myectomy/ablation) for refractory obstructive HCM. Primary prevention ICD based on personalized SCD risk stratification. | Clinical guidelines: Shared decision-making for ICD; septal reduction reserved for severe drug-refractory obstruction (bertero2025hypertrophiccardiomyopathyevolving pages 3-3, mcbenedict2024impactofgenetic pages 10-11). | Broad HCM evidence. MYH7 patients may require these earlier due to phenotype severity. |
| Emerging Gene Therapies | NCIT:C139785 (Gene Editing) | Adenine base editing (ABE8e) and RNA nucleases (hpCas13d) can precisely correct or silence specific MYH7 SNVs to prevent hypertrophy. | In vivo mouse/iPSC models: ABE8e corrected MYH7 R403Q in ≥70% of ventricular cardiomyocytes; hpCas13d selectively suppressed mutant alleles (yang2024allelespecificsuppressionof pages 1-2, reichart2023efficientinvivo pages 1-2, chai2023baseeditingcorrection pages 1-3). | MYH7-specific. Preclinical stage; demonstrates feasibility of single-dose genetic correction. |
| Animal / in vitro Models | NCIT:C14272 (Mouse Model), NCIT:C14283 (Porcine Model) | Large and small animal models (spontaneous and engineered) recapitulate hypertrophy, metabolic defects, and early perinatal manifestations. | Swine (MYH7 R723G, R403Q) show early disease onset, mitochondrial defect; feline models (MYH7 E1883K) show spontaneous analogous HCM (joshua2023felinemyocardialtranscriptome pages 1-2, stern2023hypertrophiccardiomyopathyin pages 1-3, montag2018successfulknockinof pages 1-2). | Broad HCM (some MYBPC3 models) and MYH7-specific (e.g., swine knock-ins, feline orthologs). |


*Table: A structured summary of clinical, genetic, molecular, and therapeutic findings for MYH7-related hypertrophic cardiomyopathy, distinguishing gene-specific mechanisms from broad HCM guidelines.*

## 1. Disease information

### Definition

HCM is unexplained left-ventricular (LV) wall thickening that is not solely explained by loading conditions such as hypertension, valvular disease, or athletic remodeling. HCM1 is the **MYH7-related autosomal-dominant subset**. Its cardinal pathology comprises cardiomyocyte hypertrophy and disarray, interstitial fibrosis, diastolic dysfunction, and—variably—dynamic LV outflow-tract obstruction (LVOTO). Clinical expression ranges from lifelong subclinical disease to dyspnea, angina, syncope, atrial or ventricular arrhythmia, heart failure, stroke, and sudden cardiac death (SCD) (mobiuswinkler2024thediagnosisand pages 2-3, lee2024incompletepenetranthypertrophiccardiomyopathy pages 1-2).

### Identifiers and synonyms

- **MONDO:** MONDO:0008647, as supplied for HCM1; broad HCM is separately represented as **MONDO:0005045**. Database releases should be checked before ingestion because locus-specific mappings can change.
- **OMIM:** **192600**, cardiomyopathy, familial hypertrophic, 1.
- **Gene:** MYH7; **HGNC:7577**; chromosome **14q12**; Ensembl ENSG00000092054.
- **MeSH:** *Cardiomyopathy, Hypertrophic* (D002312; broad phenotype).
- **ICD-10-CM:** I42.1, obstructive hypertrophic cardiomyopathy; I42.2, other hypertrophic cardiomyopathy.
- **ICD-11:** BC43.0, hypertrophic cardiomyopathy; local extension codes may distinguish obstruction.
- **Orphanet:** familial hypertrophic cardiomyopathy is represented at disease-family level; verify the current ORPHA record rather than assuming a MYH7-exclusive mapping.
- **Synonyms:** familial hypertrophic cardiomyopathy 1; HCM1; MYH7-related hypertrophic cardiomyopathy; β-myosin-heavy-chain cardiomyopathy; familial hypertrophic obstructive cardiomyopathy when LVOTO is present. “IHSS” and “hypertrophic subaortic stenosis” are historical, anatomically incomplete terms.

This report synthesizes **aggregated disease-level resources, cohorts, trials, and experimental studies**, not individual EHR data. Some cited real-world studies use coded administrative records, but no patient-level EHR is reproduced here.

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factor

HCM1 is caused by a **germline heterozygous pathogenic/likely pathogenic MYH7 variant**. MYH7 encodes the 1,935-amino-acid β-myosin heavy chain, the major adult human ventricular thick-filament motor. Pathogenic HCM variants are predominantly missense substitutions, enriched in approximately residues 167–931 encompassing the myosin motor/head and actin/ATP-interacting regions. Predicted loss-of-function variants should not automatically receive full PVS1 weight because MYH7 haploinsufficiency is not the established HCM1 mechanism; most HCM variants act through altered-function or “poison-peptide” effects (pires2025exploringmyh7in pages 1-2, pires2025exploringmyh7in pages 1-1).

### Genetic risk and modifiers

- A P/LP MYH7 allele is the primary risk factor; multiple sarcomeric variants can worsen expression, although variant-level prediction remains imperfect.
- Family history of early HCM, heart failure, ventricular arrhythmia, or SCD increases concern.
- Penetrance is modified by age, sex, polygenic background, allelic expression, and probably epigenetic and environmental factors. The best 2024 meta-analysis concluded that penetrance is “highly variable” and influenced by “context-dependent genetic and environmental factors” (topriceanu2024metaanalysisofpenetrance pages 1-2).
- MYH7 variants may also produce dilated, restrictive, or noncompaction cardiomyopathy and skeletal myopathy, so genotype must be interpreted with the phenotype and family segregation (pires2025exploringmyh7in pages 5-6).

### Environmental/lifestyle factors

Hypertension, obesity, diabetes, sleep-disordered breathing, and sustained hemodynamic load do not cause monogenic HCM1 but can increase LV mass, symptoms, atrial remodeling, and heart-failure burden. Dehydration, vasodilation, fever, heavy alcohol exposure, and abrupt high-intensity exertion can worsen dynamic obstruction or precipitate symptoms. Smoking and pollution are general cardiovascular hazards but are not established HCM1-specific causes. No infectious agent causes HCM1.

### Protective factors

No validated protective MYH7 allele or diet prevents HCM1. Clinically useful protection is secondary/tertiary: blood-pressure and weight control, avoidance of volume depletion and stimulant misuse, individualized exercise, surveillance, anticoagulation for atrial fibrillation, and ICD placement when SCD risk justifies it. Low- and moderate-intensity exercise is now considered beneficial for most patients rather than universally prohibited (bertero2025hypertrophiccardiomyopathyevolving pages 3-3).

## 3. Phenotypes

| Phenotype | Type/course and approximate frequency | Suggested HPO term | Functional/QOL effect |
|---|---|---|---|
| LV hypertrophy, often asymmetric septal | Sign; age-dependent, variable; defining overt phenotype | HP:0001639 | May be asymptomatic or impair filling/exercise capacity |
| Dynamic LVOTO/SAM | Sign; resting or provocable; broad-HCM rather than MYH7-specific | HP:0001727; HP:0001654 | Exertional dyspnea, chest pain, presyncope |
| Diastolic dysfunction | Functional sign; commonly progressive with remodeling | HP:0005117 | Exercise intolerance and congestion |
| Dyspnea/fatigue | Symptoms; episodic or progressive | HP:0002094; HP:0012378 | Reduced activity and KCCQ/SF-36 domains |
| Chest pain | Symptom, often exertional/microvascular | HP:0001681 | Activity limitation and anxiety |
| Palpitations/AF | Symptom/sign; risk rises with age and LA enlargement | HP:0001962; HP:0005110 | Stroke risk, impaired capacity, hospitalization |
| NSVT/VT/VF | Electrophysiologic sign; minority but prognostically important | HP:0004756; HP:0001663 | Syncope, ICD therapy, SCD risk |
| Syncope | Episodic symptom | HP:0001279 | Injury risk and major SCD-risk evaluation trigger |
| Myocardial fibrosis/LGE | Imaging/pathology sign; variable and progressive | HP:0031604 | Arrhythmic and HF risk; no direct symptom necessarily |
| Systolic dysfunction/end-stage HCM | Late complication in a minority | HP:0001644 | Advanced HF, transplantation risk |
| SCD | Severe outcome, uncommon with modern management | HP:0001645 | Premature mortality and major family impact |

ECG abnormalities occur in approximately **75–95%** of broad-HCM patients, but a normal ECG does not exclude disease. MYH7 disease tends toward earlier presentation and more severe hypertrophy/arrhythmia than genotype-negative HCM, although expressivity remains wide (hao2026hypertrophiccardiomyopathycomprehensive pages 2-4, mobiuswinkler2024thediagnosisand pages 2-3). Symptoms can begin in childhood, adolescence, adulthood, or rarely prenatally; a 2024 family meta-analysis found mean overt-HCM diagnosis at **38 years** across sarcomeric genes (topriceanu2024metaanalysisofpenetrance pages 1-2).

## 4. Genetic and molecular information

### Gene and variants

- **MYH7/HGNC:7577**, β-cardiac myosin heavy chain; 41 exons over approximately 22.9 kb at 14q12 (pires2025exploringmyh7in pages 1-2).
- Variant class: predominantly heterozygous **missense**; examples with extensive experimental evidence include **p.Arg403Gln (R403Q)**, **p.Gly256Glu (G256E)**, and **p.Arg723Gly (R723G)**.
- Origin: constitutional/germline; de novo variants occur, but inherited autosomal-dominant disease is typical. Somatic MYH7 mutation is not the usual mechanism.
- Population frequency: a credible HCM-causing variant should be rare enough for disease prevalence/penetrance; exact gnomAD frequency must be recorded per variant and ancestry. Do not assign pathogenicity from rarity alone.
- Classification: use ACMG/AMP plus MYH7/sarcomere-specific ClinGen guidance, segregation, phenotype, functional evidence, and periodic reanalysis. A VUS is **not** actionable for predictive cascade testing (abbas2024roleofgenetics pages 9-11).

### Functional effect

Variant effects are mutation-specific. G256E reduced the folded-back myosin fraction by **33%**, increasing contraction-available heads and producing faster/greater tension from myofibrils through single cells and engineered tissues. Single-cell profiling showed increased mitochondrial-gene expression and respiration (lee2024incompletepenetranthypertrophiccardiomyopathy pages 1-2). R403Q has shown context-dependent gain/loss measurements, illustrating why single-assay evidence is insufficient.

### Modifiers and epigenetics

Robust, routinely actionable modifier genes are not established. Polygenic LV-wall-thickness background, sex, ancestry, hypertension, obesity, and allelic imbalance probably modify penetrance. DNA methylation, chromatin remodeling, microRNAs, and histone signaling are research findings, not diagnostic biomarkers. Large chromosomal abnormalities, aneuploidy, repeat expansions, and mitochondrial DNA variants are not typical causes of HCM1.

## 5. Environmental information

HCM1 is not infectious, toxic, occupational, or radiation-induced. Environmental factors primarily alter **expression and complications**, not the initiating lesion. Clinical management should address hypertension, obesity, inactivity, smoking, excess alcohol, sleep apnea, and dehydration. Competitive or vigorous exercise is no longer automatically forbidden; decisions require phenotype, rhythm history, LVOTO, blood-pressure response, fibrosis, family history, and shared decision-making (bertero2025hypertrophiccardiomyopathyevolving pages 3-3).

## 6. Mechanism/pathophysiology

### Ordered causal chain

1. A heterozygous MYH7 missense variant **leads to** incorporation of altered β-myosin into ventricular sarcomeres.
2. Altered motor-domain kinetics and/or destabilization of the folded-back super-relaxed state **results in** more contraction-competent myosin heads; the magnitude and direction are variant-specific.
3. Excess actin–myosin engagement **leads to** hypercontractility, higher ATP demand, impaired relaxation, and abnormal mechanosensing.
4. Energetic stress and altered calcium handling **result in** mitochondrial/metabolic adaptation; in G256E cells, increased mitochondrial respiration is demonstrated, while later energetic failure is partly inferred from broader HCM studies (lee2024incompletepenetranthypertrophiccardiomyopathy pages 1-2).
5. Cardiomyocyte stress signaling **leads to** hypertrophic transcription and cellular enlargement; implicated pathways include CaMKII–HDAC, MAPK, PI3K–AKT–mTOR, calcineurin–NFAT, and mechanotransduction, but their causal importance varies by model (pietsch2024investigationofmicrotubule pages 32-35).
6. **Branch A:** cardiomyocyte hypertrophy/disarray **results in** increased LV wall thickness, reduced compliance, diastolic dysfunction, and—when septal geometry and mitral SAM coexist—dynamic LVOTO.
7. **Branch B:** mutant cardiomyocyte paracrine signaling **leads to** fibroblast proliferation and extracellular-matrix deposition. In MYH7-R403Q microtissues, collagen-I content rose **40%**, and EGFR inhibition attenuated stromal activation (ewoldt2024hypertrophiccardiomyopathy–associatedmutations pages 1-2).
8. Hypertrophy, microvascular supply–demand mismatch, and fibrosis **result in** ischemia, heterogeneous conduction, and repolarization abnormalities.
9. These changes **lead to** dyspnea, angina, AF, ventricular arrhythmias, syncope, heart failure, stroke, and SCD.

### Cell, process, and compartment annotations

- **Cells:** ventricular cardiomyocyte (CL:0000746), cardiac fibroblast (CL:0002548), vascular endothelial cell (CL:0000115), vascular smooth-muscle cell (CL:0000359), macrophage (CL:0000235).
- **Processes:** muscle contraction (GO:0006936), actin–myosin filament sliding (GO:0033275), cardiac-muscle hypertrophy (GO:0003300), mitochondrial ATP synthesis (GO:0042775), extracellular-matrix organization (GO:0030198), fibroblast proliferation (GO:0048144), calcium-ion homeostasis (GO:0055074), cardiac conduction (GO:0061337).
- **Compartments:** sarcomere (GO:0030017), myosin complex (GO:0016459), thick filament (GO:0032982), mitochondrion (GO:0005739), extracellular matrix (GO:0031012).

### Molecular profiling and advanced technologies

The strongest recent MYH7-specific evidence integrates molecular biophysics, gene-edited hiPSC cardiomyocytes, engineered heart tissue, single-cell transcriptomics, and metabolic profiling (lee2024incompletepenetranthypertrophiccardiomyopathy pages 1-2). Single-nucleus RNA sequencing of MYH7-variant engineered tissues supports cardiomyocyte-to-fibroblast EGFR-mediated signaling (ewoldt2024hypertrophiccardiomyopathy–associatedmutations pages 1-2). Feline HCM RNA-seq identified chamber-specific remodeling, fibrosis, inflammation, calcium, microvascular, and metabolic signatures, including RhoGDI/Rho-GTPase, integrin/ILK, PPARα/RXRα, HIF1α, and CXCR4 pathways; this is comparative, not MYH7-exclusive human evidence (joshua2023felinemyocardialtranscriptome pages 1-2).

## 7. Anatomy

- **Primary organ/system:** heart/cardiovascular system; UBERON:0000948.
- **Primary site:** LV myocardium, UBERON:0002084; interventricular septum, UBERON:0002094; papillary muscles and mitral apparatus may contribute to obstruction.
- **Secondary sites:** left atrium enlarges with diastolic burden/AF; coronary microvasculature contributes to ischemia; lungs are secondarily affected by congestion; brain may be affected by embolic stroke.
- **Tissue:** cardiac muscle tissue, UBERON:0001133.
- **Subcellular focus:** sarcomere, thick filament, myosin head/S1 motor, mitochondria, and extracellular matrix.
- **Localization:** usually diffuse/asymmetric rather than unilateral; septal, reverse-curvature, apical, midventricular, or concentric patterns can occur.

## 8. Temporal development

HCM1 is a chronic lifelong predisposition with **age-dependent penetrance**. In family studies, MYH7 penetrance was approximately **65%**; short-term phenotypic conversion among genotype-positive/phenotype-negative relatives was approximately **23%**, compared with 12% for MYBPC3. Across genes, 15% converted over about eight years from a mean starting age near 16 years (topriceanu2024metaanalysisofpenetrance pages 1-2).

A useful staging model is: genotype-positive/phenotype-negative → subclinical electrical/imaging abnormalities → overt hypertrophy, with or without obstruction → complications (AF, fibrosis, HF, arrhythmia) → minority end-stage systolic dysfunction. Progression may be slow, stable for decades, or accelerated. True spontaneous genetic remission is not expected, although gradients and symptoms can improve with treatment.

## 9. Inheritance and population

### Inheritance

- Autosomal dominant, with a **50% transmission probability per pregnancy** from a heterozygous parent.
- Incomplete, age-dependent penetrance and markedly variable expressivity.
- No established anticipation mechanism; apparent earlier disease in successive generations can reflect ascertainment or modifiers.
- Germline mosaicism is possible but uncommon; consanguinity is not central to dominant HCM1.
- Founder variants occur in particular populations, but HCM1 is worldwide and not restricted to an ancestry.

### Penetrance context

In clinically ascertained nonproband relatives, pooled MYH7 penetrance was approximately **65%**. Incidentally identified sarcomeric P/LP carriers in population cohorts had only about **11%** overt HCM penetrance, showing strong ascertainment and modifier effects (topriceanu2024metaanalysisofpenetrance pages 1-2).

### Epidemiology

Broad phenotypic HCM prevalence is conventionally about **1:500** and may approach **1:250** when genetics and family screening are included. MYH7 accounts for roughly **15% of clinically diagnosed HCM**, but this is not the population prevalence of HCM1 (hao2026hypertrophiccardiomyopathycomprehensive pages 1-2). HCM is diagnosed more often in men in clinical cohorts, despite autosomal inheritance; delayed recognition and sex-related expression likely contribute. Reliable MYH7-specific incidence, carrier frequency, and sex ratio are not established.

## 10. Diagnostics

### Clinical diagnostic pathway

1. Three-generation pedigree, symptoms, examination, blood pressure, and exclusion of loading/systemic causes.
2. Twelve-lead ECG; abnormalities are frequent but nonspecific.
3. Transthoracic echocardiography to measure maximum wall thickness, diastolic function, SAM, mitral regurgitation, and resting/provoked LVOT gradient.
4. Valsalva/standing or exercise echocardiography when resting obstruction is absent; approximately half of obstructive cases may require provocation (mobiuswinkler2024thediagnosisand pages 1-2).
5. CMR when echo is incomplete, morphology is atypical, phenocopy is possible, or fibrosis/apical aneurysm/thickness must be characterized. LGE contributes to risk assessment (fernandes2024guidelinesonthe pages 24-26).
6. Ambulatory ECG—often 24–48 hours and repeated according to phenotype—to detect AF and NSVT; 48-hour monitoring is emphasized for risk stratification (mobiuswinkler2024thediagnosisand pages 2-3).
7. Exercise testing/CPET for symptoms, blood-pressure response, functional capacity, and provoked obstruction.

In adults, maximum end-diastolic LV wall thickness **≥15 mm** unexplained by loading is the usual threshold; **13–14 mm** can support diagnosis in a first-degree relative or genotype-positive person. Pediatric diagnosis uses body-size-adjusted z-scores. LV wall thickness **≥30 mm** is a major SCD-risk marker, not merely a diagnostic threshold (mobiuswinkler2024thediagnosisand pages 2-3).

### Biomarkers and pathology

NT-proBNP reflects wall stress/HF burden; high-sensitivity troponin may reflect injury. Neither is diagnostic for HCM1. Histology—myocyte hypertrophy/disarray, fibrosis, and small-vessel disease—is supportive but biopsy is unnecessary in routine sarcomeric HCM. Low ECG voltage despite marked hypertrophy raises amyloidosis/storage disease concern (mobiuswinkler2024thediagnosisand pages 2-3).

### Genetic testing

Use a phenotype-anchored NGS panel containing definitive sarcomere genes—at minimum MYH7, MYBPC3, TNNT2, TNNI3, TPM1, ACTC1, MYL2, and MYL3—plus genes for clinically plausible phenocopies. Testing yield is approximately **30% in sporadic** and up to **60% in familial/young typical HCM** (abbas2024roleofgenetics pages 9-11, fernandes2024guidelinesonthe pages 24-26).

- **Single-gene MYH7 testing:** appropriate when a known familial variant exists; otherwise a curated panel is preferable.
- **WES/WGS:** useful after a negative panel in strongly familial disease, atypical disease, or research; WGS can identify structural/deep intronic variants. Interpretation, not sequencing, is the main limitation.
- **CMA, karyotype, FISH, repeat-expansion, and mtDNA testing:** not routine for isolated HCM1; use only when syndromic features indicate them.
- **RNA-seq:** may resolve splice variants in selected cases; not routine.
- **Cascade testing:** offer targeted testing to first-degree relatives when the proband has a P/LP variant. A relative who tests negative for the familial variant can usually leave serial HCM surveillance, subject to family-specific considerations. Do not use a VUS for predictive exclusion; relatives instead receive longitudinal ECG/echo surveillance (abbas2024roleofgenetics pages 9-11).

### Differential diagnosis

Exclude hypertensive/valvular remodeling, athlete’s heart, amyloidosis, Fabry disease, Danon disease, PRKAG2 glycogenosis, Pompe disease, Friedreich ataxia, mitochondrial disease, RASopathies, and other cardiomyopathies. CMR, extracardiac features, enzyme/protein studies, scintigraphy for transthyretin amyloid, and genetic testing are selected by phenotype (fernandes2024guidelinesonthe pages 24-26).

## 11. Outcome and prognosis

Modern specialist care yields near-normal life expectancy for many patients, with broad-HCM mortality generally **<1% per year** under optimal management. Prognosis is nevertheless heterogeneous (mobiuswinkler2024thediagnosisand pages 2-3).

Major complications are AF and thromboembolic stroke, ventricular arrhythmia/SCD, progressive HF, mitral regurgitation, apical aneurysm, and a minority with end-stage systolic dysfunction/transplantation. MYH7-positive disease tends toward earlier diagnosis and increased AF, ventricular arrhythmia, HF, and transplantation risk, but genotype alone does not determine ICD placement (santos2025geneticclinicaland pages 9-10, hao2026hypertrophiccardiomyopathycomprehensive pages 2-4).

Risk assessment integrates prior cardiac arrest/VT, unexplained syncope, family SCD, maximum wall thickness, apical aneurysm, LVEF, NSVT, LVOTO, LA size, age, and CMR fibrosis. ECG imaging research found delayed/dispersed activation in HCM; arrhythmic survivors had mean activation time **63.2 versus 57.4 ms** and activation-recovery interval **234.0 versus 221.4 ms**, but this remains investigational (not standard risk scoring) (mobiuswinkler2024thediagnosisand pages 2-3).

## 12. Treatment

### General strategy

Treatment is phenotype-driven, not currently MYH7-variant-specific: manage obstruction/symptoms, AF/stroke, HF, and SCD risk; refer complex cases to an HCM center.

- **Nonvasodilating β-blocker** first line for symptomatic obstructive HCM; NCIT concept: Beta Adrenergic Blocking Agent.
- **Verapamil or diltiazem** if β-blockers are ineffective/not tolerated; avoid in severe hypotension or extreme gradients.
- **Disopyramide** may be added for persistent obstruction, with QT/anticholinergic monitoring.
- **Mavacamten**, a reversible cardiac-myosin inhibitor, directly reduces excessive cross-bridge formation. It improves gradients, symptoms, and exercise capacity in symptomatic obstructive HCM but can reduce LVEF and requires interaction review and serial echocardiography under applicable regulatory requirements. NCIT: cardiac myosin inhibitor/antineoplastic-thesaurus drug concept as locally mapped.
- **Aficamten** is a next-generation myosin inhibitor. In the 282-patient phase III SEQUOIA-HCM program, **4.9%** required dose reduction for LVEF <50%; no associated treatment interruption or worsening HF occurred, and adverse events were similar to placebo. These results are broad obstructive-HCM data, not MYH7-only outcomes (coats2024dosingandsafety pages 1-2, coats2024dosingandsafety pages 2-4).

### Complication-directed treatment

- AF: rhythm/rate control as appropriate and oral anticoagulation because HCM-associated AF carries substantial stroke risk; standard CHA₂DS₂-VASc thresholds should not be the sole gatekeeper.
- HF/congestion: cautious diuretics; standard guideline-directed therapy when LVEF becomes reduced.
- ICD: secondary prevention after arrest/sustained VT and individualized primary prevention for high-risk patients. Shared decision-making must include device complications (bertero2025hypertrophiccardiomyopathyevolving pages 3-3).
- **Septal myectomy** or **alcohol septal ablation**: for severe, drug-refractory symptomatic LVOTO at experienced centers; myectomy is preferred when concomitant mitral/subvalvular abnormalities require correction. NCIT suggestions: Surgical Procedure; Cardiac Septal Ablation; Implantable Cardioverter Defibrillator.
- Transplantation: advanced refractory HF/end-stage disease.

### Experimental precision therapies

- Chai et al. corrected dominant-negative **MYH7 c.1208G>A (p.R403Q)** in patient-derived cardiomyocytes and prevented disease in humanized mice using adenine base editing—preclinical, not human therapy (Nature Medicine, February 2023; DOI: https://doi.org/10.1038/s41591-022-02176-5) (chai2023baseeditingcorrection pages 1-3).
- Reichart et al. achieved correction in **≥70% of ventricular cardiomyocytes** with dual-AAV9 ABE8e and maintained normal mouse cardiac structure/function; Cas9 allele inactivation had dose-dependent toxicity (Nature Medicine, 16 February 2023; DOI: https://doi.org/10.1038/s41591-022-02190-7) (reichart2023efficientinvivo pages 1-2).
- High-precision Cas13d selectively suppressed mutant MYH7 RNA in two mouse models and screened applicability across **45 human pathogenic MYH7 SNVs** (Circulation, 23 July 2024; DOI: https://doi.org/10.1161/CIRCULATIONAHA.123.067890) (yang2024allelespecificsuppressionof pages 1-2).

These approaches face delivery, immunity, off-target/bystander editing, durability, dose, and germline-exposure issues. No gene, RNA, or cell therapy is approved for HCM1. TN-201 (NCT05836259) is an early clinical gene-replacement program for **MYBPC3**, not MYH7, and therefore should not be annotated as HCM1-specific therapy (sanghvi2025hypertrophiccardiomyopathymanagement pages 14-15).

## 13. Prevention

**Primary prevention of the inherited allele** is unavailable after conception. Reproductive options include genetic counseling, natural conception with prenatal diagnosis, or IVF with preimplantation genetic testing when a familial P/LP variant is known. Counseling must address incomplete penetrance and variable severity (abbas2024roleofgenetics pages 9-11).

**Secondary prevention** comprises cascade genetic testing, serial ECG/echo for genotype-positive or untested relatives, early CMR/Holter when indicated, and molecular autopsy after unexplained HCM-related SCD. Population-wide newborn or adult genetic screening is not standard.

**Tertiary prevention** includes AF detection/anticoagulation, individualized exercise, control of blood pressure and weight, avoidance of dehydration and unsafe drug interactions, myosin-inhibitor monitoring, and ICD placement for justified risk. Vaccination follows routine public-health schedules; there is no HCM1 vaccine or antimicrobial prophylaxis.

## 14. Other species and natural disease

- **Domestic cat, Felis catus (NCBI Taxon 9685):** spontaneous HCM affects approximately 15% of cats and resembles human HCM in LV hypertrophy, diastolic dysfunction, fibrosis, disarray, and variable progression. A feline orthologue of human MYH7 p.Glu1883Lys has been reported, although established breed-associated variants are more often MYBPC3 p.A31P in Maine Coon and p.R820W in Ragdoll cats (joshua2023felinemyocardialtranscriptome pages 1-2, stern2023hypertrophiccardiomyopathyin pages 1-3).
- Feline RNA-seq of five HCM and five control cats in LV and LA tissue identified chamber-specific remodeling, fibrosis, inflammation, calcium, microvascular, and metabolic pathways (PLOS ONE, 16 March 2023; DOI: https://doi.org/10.1371/journal.pone.0283244) (joshua2023felinemyocardialtranscriptome pages 1-2).
- There is no transmission or zoonotic risk; these are homologous genetic/phenotypic diseases, not infections.

## 15. Model organisms and experimental systems

- **hiPSC cardiomyocytes and engineered heart tissues:** best for variant-specific human β-myosin mechanics, isogenic correction, calcium/energetic phenotyping, and drug testing. Limitations include cellular immaturity and absent systemic physiology. The 2024 G256E study explicitly demonstrated hypercontractility “across scales” with increased mitochondrial respiration (PNAS, 29 April 2024; DOI: https://doi.org/10.1073/pnas.2318413121) (lee2024incompletepenetranthypertrophiccardiomyopathy pages 1-2).
- **Multicellular cardiac microtissues:** MYH7-R403Q cardiomyocytes plus wild-type fibroblasts reproduce paracrine fibrosis and allow EGFR-pathway interrogation; they still simplify immune, vascular, and loading environments (ewoldt2024hypertrophiccardiomyopathy–associatedmutations pages 1-2).
- **Mouse:** rapid genetics and in-vivo editing, but adult mouse ventricle predominantly expresses α-myosin rather than human-like β-myosin, limiting direct MYH7 translation (montag2018successfulknockinof pages 1-2).
- **Rabbit/pig:** more human-like myosin and cardiac physiology. TALEN knock-in MYH7 R723G pigs displayed neonatal disarray, malformed nuclei, MYH7 overexpression, and death within 24 hours—useful for early pathology but too severe for ordinary adult natural history (Scientific Reports 2018; DOI: https://doi.org/10.1038/s41598-018-22936-z) (montag2018successfulknockinof pages 1-2).
- **Cat:** valuable spontaneous large-animal HCM model, but many feline cases are genetically unresolved or MYBPC3-related rather than MYH7-specific (joshua2023felinemyocardialtranscriptome pages 1-2, stern2023hypertrophiccardiomyopathyin pages 1-3).

## Recent research priorities and expert interpretation

The principal 2023–2024 advances were: (1) quantitative, context-aware penetrance estimates; (2) multiscale demonstration that an incompletely penetrant MYH7 variant can directly increase available myosin heads, force, and mitochondrial respiration; (3) identification of cardiomyocyte–fibroblast EGFR signaling as a fibrosis mechanism; (4) phase III validation of myosin inhibition for obstructive HCM; and (5) proof-of-concept correction or selective silencing of MYH7 variants in human cells and mice (topriceanu2024metaanalysisofpenetrance pages 1-2, ewoldt2024hypertrophiccardiomyopathy–associatedmutations pages 1-2, yang2024allelespecificsuppressionof pages 1-2, reichart2023efficientinvivo pages 1-2, chai2023baseeditingcorrection pages 1-3, coats2024dosingandsafety pages 1-2, lee2024incompletepenetranthypertrophiccardiomyopathy pages 1-2).

The authoritative interpretation is that genetic testing is already clinically valuable for **etiologic diagnosis and cascade screening**, but individual prognosis and treatment selection remain predominantly phenotype-led. Variant-specific functional data are increasingly informative, yet they are not interchangeable across MYH7 substitutions. Myosin inhibitors are the first widely implemented mechanism-directed drugs, whereas gene editing remains preclinical.

## Evidence limitations

PMIDs were requested, but the retrieved full texts and metadata did not consistently expose PMID fields; DOI URLs and publication dates are therefore supplied where verified rather than inventing identifiers. Exact phenotype frequencies, incidence, carrier frequency, environmental effect sizes, protective alleles, and quality-of-life values are generally unavailable specifically for MYH7-HCM1. Administrative-code and broad-HCM estimates should not be represented as locus-specific statistics. Direct abstract wording supported by retrieved texts includes: G256E produced “hypercontractile force generation across scales, accompanied by increased mitochondrial respiration,” and the 2024 penetrance meta-analysis concluded that penetrance is “highly variable” and context dependent (topriceanu2024metaanalysisofpenetrance pages 1-2, lee2024incompletepenetranthypertrophiccardiomyopathy pages 1-2).

References

1. (OpenTargets Search: hypertrophic cardiomyopathy-MYH7): Open Targets Query (hypertrophic cardiomyopathy-MYH7, 24 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (hao2026hypertrophiccardiomyopathycomprehensive pages 1-2): Luwen Hao, Xin Chen, and Bo Qin. Hypertrophic cardiomyopathy: comprehensive insights into pathogenic genes and genotype-phenotype associations. Frontiers in Cell and Developmental Biology, Jan 2026. URL: https://doi.org/10.3389/fcell.2026.1741252, doi:10.3389/fcell.2026.1741252. This article has 1 citations.

3. (pietsch2024investigationofmicrotubule pages 32-35): NJ Pietsch. Investigation of microtubule detyrosination modulation in human ipsc-cardiomyocytes and hcm mice. Unknown journal, 2024.

4. (pires2025exploringmyh7in pages 1-1): Lucas Vieira Lacerda Pires, Vinícius Machado Correia, Layara Fernanda Vicente Pereira Lipari, Fernanda Almeida Andrade, Fábio Fernandes, Vagner Madrini, Mariana Lombardi Peres de Carvalho, Giovanna Napolitano, Elisangela Aparecida da Silva, Kelvin Henrique Vilalva, Vitória Pelegrino do Val, and José Eduardo Krieger. Exploring myh7 in cardiomyopathies: genetic drivers and clinical outcomes. ABC Heart Fail Cardiomyop, Apr 2025. URL: https://doi.org/10.36660/abchf.20240054i, doi:10.36660/abchf.20240054i. This article has 1 citations.

5. (topriceanu2024metaanalysisofpenetrance pages 1-2): Constantin-Cristian Topriceanu, Alexandre C. Pereira, James C. Moon, Gabriella Captur, and Carolyn Y. Ho. Meta-analysis of penetrance and systematic review on transition to disease in genetic hypertrophic cardiomyopathy. Jan 2024. URL: https://doi.org/10.1161/circulationaha.123.065987, doi:10.1161/circulationaha.123.065987. This article has 110 citations and is from a highest quality peer-reviewed journal.

6. (ewoldt2024hypertrophiccardiomyopathy–associatedmutations pages 1-2): Jourdan K. Ewoldt, Miranda C. Wang, Micheal A. McLellan, Paige E. Cloonan, Anant Chopra, Joshua Gorham, Linqing Li, Daniel M. DeLaughter, Xining Gao, Joshua H. Lee, Jon A. L. Willcox, Olivia Layton, Rebeccah J. Luu, Christopher N. Toepfer, Jeroen Eyckmans, Christine E. Seidman, Jonathan G. Seidman, and Christopher S. Chen. Hypertrophic cardiomyopathy–associated mutations drive stromal activation via egfr-mediated paracrine signaling. Oct 2024. URL: https://doi.org/10.1126/sciadv.adi6927, doi:10.1126/sciadv.adi6927. This article has 18 citations and is from a highest quality peer-reviewed journal.

7. (lee2024incompletepenetranthypertrophiccardiomyopathy pages 1-2): Soah Lee, Alison S. Vander Roest, Cheavar A. Blair, Kerry Kao, Samantha B. Bremner, Matthew C. Childers, Divya Pathak, Paul Heinrich, Daniel Lee, Orlando Chirikian, Saffie E. Mohran, Brock Roberts, Jacqueline E. Smith, James W. Jahng, David T. Paik, Joseph C. Wu, Ruwanthi N. Gunawardane, Kathleen M. Ruppel, David L. Mack, Beth L. Pruitt, Michael Regnier, Sean M. Wu, James A. Spudich, and Daniel Bernstein. Incomplete-penetrant hypertrophic cardiomyopathy myh7 g256e mutation causes hypercontractility and elevated mitochondrial respiration. Proceedings of the National Academy of Sciences of the United States of America, Apr 2024. URL: https://doi.org/10.1073/pnas.2318413121, doi:10.1073/pnas.2318413121. This article has 28 citations and is from a highest quality peer-reviewed journal.

8. (santos2025geneticclinicaland pages 9-10): Emerson de Santana Santos, Gabriel da Costa Kuhn, Antônio Guilherme Cunha de Almeida, João Victor Andrade Pimentel, Newton Vital Figueiredo Neto, Larissa Rebeca da Silva Tavares, Bárbara Letícia Lima dos Santos, Ana Beatriz Leite Aragão, Beatriz Carolina de Araujo Pereira, Caio da Silva Ferreira, Willian Moreira Leão e Silva, Enaldo Vieira de Melo, Irlaneide da Silva Tavares, Antônio Carlos Sobral Sousa, and Joselina Luzia Menezes Oliveira. Genetic, clinical, and sociodemographic profile of individuals with diagnosis or family history of hypertrophic cardiomyopathy: insights from a prospective cohort. Sep 2025. URL: https://doi.org/10.3390/genes16091100, doi:10.3390/genes16091100. This article has 3 citations.

9. (hao2026hypertrophiccardiomyopathycomprehensive pages 2-4): Luwen Hao, Xin Chen, and Bo Qin. Hypertrophic cardiomyopathy: comprehensive insights into pathogenic genes and genotype-phenotype associations. Frontiers in Cell and Developmental Biology, Jan 2026. URL: https://doi.org/10.3389/fcell.2026.1741252, doi:10.3389/fcell.2026.1741252. This article has 1 citations.

10. (mobiuswinkler2024thediagnosisand pages 2-3): Maximilian N. Möbius-Winkler, Ulrich Laufs, and Karsten Lenk. The diagnosis and treatment of hypertrophic cardiomyopathy. Deutsches Arzteblatt international, Nov 2024. URL: https://doi.org/10.3238/arztebl.m2024.0196, doi:10.3238/arztebl.m2024.0196. This article has 14 citations and is from a peer-reviewed journal.

11. (fernandes2024guidelinesonthe pages 24-26): F Fernandes, MV Simões, and EB Correia. Guidelines on the diagnosis and treatment of hypertrophic cardiomyopathy-2024. Unknown journal, 2024.

12. (coats2024dosingandsafety pages 1-2): Caroline J. Coats, Ahmad Masri, Michael E. Nassif, Roberto Barriales‐Villa, Michael Arad, Nuno Cardim, Lubna Choudhury, Brian Claggett, Hans‐Dirk Düngen, Pablo Garcia‐Pavia, Albert A. Hagège, James L. Januzzi, Matthew M. Y. Lee, Gregory D. Lewis, Chang‐Sheng Ma, Martin S. Maron, Zi Michael Miao, Michelle Michels, Iacopo Olivotto, Artur Oreziak, Anjali T. Owens, John A. Spertus, Scott D. Solomon, Jacob Tfelt‐Hansen, Marion van Sinttruije, Josef Veselka, Hugh Watkins, Daniel L. Jacoby, Polina German, Stephen B. Heitner, Stuart Kupfer, Justin D. Lutz, Fady I. Malik, Lisa Meng, Amy Wohltman, Theodore P. Abraham, Yuhui Zhang, Haibo Yang, Chunli Shao, Zuyi Yuan, Qingchun Zeng, Xiaodong Li, Yushi Wang, Yan Shu, Mulei Chen, Ling Tao, Xinli Li, Jingfeng Wang, Zaixin Yu, Xiang Cheng, Kui Hong, David Zemanek, Henning Bundgaard, Jens Thune, Morten Jensen, Jens Mogensen, Gilbert Habib, Philippe Charron, Thibault Lhermusier, Jean‐Noël Trochu, Patricia Reant, Damien Logeart, Veselin Mitrovic, Tarek Bekfani, Frank Edelmann, Tim Seidler, Benjamin Meder, Paul Christian Schulze, Stephan Stoerk, Tienush Rassaf, Bela Merkely, Donna Zfat‐Zwas, Majdi Halabi, Offir Paz, Xavier Piltz, Marco Metra, Marco Canepa, Beatrice Musumeci, Michele Emdin, Ahmad Amin, Christian Knackstedt, Wojciech Wojakowski, Dariusz Dudek, Alexandra Toste, José Mesquita Bastos, Juan Ramón Gimeno Blanes, Rafael Jesus Hidalgo Urbano, Ana Garcia Alvarez, Luis Miguel Rincón Diaz, Tomas Vicente Ripoll Vera, Perry Elliott, NHS Greater Glasgow, Rob Cooper, Liverpool Heart, Masliza Mahmod, Antonis Pantazis, Maria Teresa Tome Esteban, Oregon Health, Ali Marian, David Owens, Frank McGrew, Richard Bach, Omar Wever‐Pinzon, Elias Collado, Aslan Turer, Bashar Hannawi, Jeffrey Geske, Penn Heart, John Symanski, Sanger Heart, Christopher Kramer, Nitasha Sarswat, Ferhaan Ahmad, Jeremy Markowitz, Neal Lakdawala, Sandeep Jani, Marshall Brinkley, Ozlem Bilen, Craig Asher, Sitaramesh Emani, Abhinav Sharma, David Fermin, Melissa Lyle, David Raymer, Andrew Darlington, Christopher Nielsen, Andrew Wang, Sherif Nagueh, Matthew Martinez, Milind Desai, Albree Tower‐Rader, Jacob Kelly, Alaska Heart, Florian Rader, Sounok Sen, Patrick Bering, Mathew Maurer, Sumeet Mitter, Mark Sherrid, Timothy Wong, Zainal Hussain, Sara Saberi, Srihari Naidu, and Jorge Silva Enciso. Dosing and safety profile of aficamten in symptomatic obstructive hypertrophic cardiomyopathy: results from sequoia‐hcm. Aug 2024. URL: https://doi.org/10.1161/jaha.124.035993, doi:10.1161/jaha.124.035993. This article has 28 citations.

13. (desai2025mavacamteninpatients pages 10-11): Milind Y. Desai, Kathy Wolski, Anjali Owens, Jeffrey B. Geske, Sara Saberi, Andrew Wang, Mark Sherrid, Paul C. Cremer, Neal K. Lakdawala, Albree Tower-Rader, David Fermin, Srihari S. Naidu, Nicholas G. Smedira, Hartzell Schaff, Zhiqun Gong, Lana Mudarris, Kathy Lampl, Amy J. Sehnert, and Steven E. Nissen. Mavacamten in patients with hypertrophic cardiomyopathy referred for septal reduction: week 128 results from valor-hcm. Circulation, 151:1378-1390, Nov 2025. URL: https://doi.org/10.1161/circulationaha.124.072445, doi:10.1161/circulationaha.124.072445. This article has 84 citations and is from a highest quality peer-reviewed journal.

14. (coats2024dosingandsafety pages 2-4): Caroline J. Coats, Ahmad Masri, Michael E. Nassif, Roberto Barriales‐Villa, Michael Arad, Nuno Cardim, Lubna Choudhury, Brian Claggett, Hans‐Dirk Düngen, Pablo Garcia‐Pavia, Albert A. Hagège, James L. Januzzi, Matthew M. Y. Lee, Gregory D. Lewis, Chang‐Sheng Ma, Martin S. Maron, Zi Michael Miao, Michelle Michels, Iacopo Olivotto, Artur Oreziak, Anjali T. Owens, John A. Spertus, Scott D. Solomon, Jacob Tfelt‐Hansen, Marion van Sinttruije, Josef Veselka, Hugh Watkins, Daniel L. Jacoby, Polina German, Stephen B. Heitner, Stuart Kupfer, Justin D. Lutz, Fady I. Malik, Lisa Meng, Amy Wohltman, Theodore P. Abraham, Yuhui Zhang, Haibo Yang, Chunli Shao, Zuyi Yuan, Qingchun Zeng, Xiaodong Li, Yushi Wang, Yan Shu, Mulei Chen, Ling Tao, Xinli Li, Jingfeng Wang, Zaixin Yu, Xiang Cheng, Kui Hong, David Zemanek, Henning Bundgaard, Jens Thune, Morten Jensen, Jens Mogensen, Gilbert Habib, Philippe Charron, Thibault Lhermusier, Jean‐Noël Trochu, Patricia Reant, Damien Logeart, Veselin Mitrovic, Tarek Bekfani, Frank Edelmann, Tim Seidler, Benjamin Meder, Paul Christian Schulze, Stephan Stoerk, Tienush Rassaf, Bela Merkely, Donna Zfat‐Zwas, Majdi Halabi, Offir Paz, Xavier Piltz, Marco Metra, Marco Canepa, Beatrice Musumeci, Michele Emdin, Ahmad Amin, Christian Knackstedt, Wojciech Wojakowski, Dariusz Dudek, Alexandra Toste, José Mesquita Bastos, Juan Ramón Gimeno Blanes, Rafael Jesus Hidalgo Urbano, Ana Garcia Alvarez, Luis Miguel Rincón Diaz, Tomas Vicente Ripoll Vera, Perry Elliott, NHS Greater Glasgow, Rob Cooper, Liverpool Heart, Masliza Mahmod, Antonis Pantazis, Maria Teresa Tome Esteban, Oregon Health, Ali Marian, David Owens, Frank McGrew, Richard Bach, Omar Wever‐Pinzon, Elias Collado, Aslan Turer, Bashar Hannawi, Jeffrey Geske, Penn Heart, John Symanski, Sanger Heart, Christopher Kramer, Nitasha Sarswat, Ferhaan Ahmad, Jeremy Markowitz, Neal Lakdawala, Sandeep Jani, Marshall Brinkley, Ozlem Bilen, Craig Asher, Sitaramesh Emani, Abhinav Sharma, David Fermin, Melissa Lyle, David Raymer, Andrew Darlington, Christopher Nielsen, Andrew Wang, Sherif Nagueh, Matthew Martinez, Milind Desai, Albree Tower‐Rader, Jacob Kelly, Alaska Heart, Florian Rader, Sounok Sen, Patrick Bering, Mathew Maurer, Sumeet Mitter, Mark Sherrid, Timothy Wong, Zainal Hussain, Sara Saberi, Srihari Naidu, and Jorge Silva Enciso. Dosing and safety profile of aficamten in symptomatic obstructive hypertrophic cardiomyopathy: results from sequoia‐hcm. Aug 2024. URL: https://doi.org/10.1161/jaha.124.035993, doi:10.1161/jaha.124.035993. This article has 28 citations.

15. (bertero2025hypertrophiccardiomyopathyevolving pages 3-3): Edoardo Bertero, Marco Canepa, and Iacopo Olivotto. Hypertrophic cardiomyopathy evolving management: american heart association/american college of cardiology vs. european society of cardiology guidelines. European heart journal, 46:359-361, Nov 2025. URL: https://doi.org/10.1093/eurheartj/ehae507, doi:10.1093/eurheartj/ehae507. This article has 11 citations and is from a highest quality peer-reviewed journal.

16. (mcbenedict2024impactofgenetic pages 10-11): Billy McBenedict, Wilhelmina N Hauwanga, Emmanuel S Amadi, Aaron A Abraham, Rithika Sivakumar, Madeleine O Okere, Melvin Chun Yang Yau, Nematalla Balla, Thasneem Rahumathulla, Berley Alphonse, and Bruno Lima Pessôa. Impact of genetic testing on the diagnosis, management, and prognosis of hypertrophic cardiomyopathy: a systematic review. Oct 2024. URL: https://doi.org/10.7759/cureus.70993, doi:10.7759/cureus.70993. This article has 2 citations.

17. (yang2024allelespecificsuppressionof pages 1-2): Ping Yang, Yingmei Lou, Zilong Geng, Zhizhao Guo, Shuo Wu, Yige Li, Kaiyuan Song, Ting Shi, Shasha Zhang, Junhao Xiong, Alex F. Chen, Dali Li, William T. Pu, Lintai Da, Yan Zhang, Kun Sun, and Bing Zhang. Allele-specific suppression of variant mhc with high-precision rna nuclease crispr-cas13d prevents hypertrophic cardiomyopathy. Jul 2024. URL: https://doi.org/10.1161/circulationaha.123.067890, doi:10.1161/circulationaha.123.067890. This article has 41 citations and is from a highest quality peer-reviewed journal.

18. (reichart2023efficientinvivo pages 1-2): Daniel Reichart, Gregory A. Newby, Hiroko Wakimoto, Mingyue Lun, Joshua M. Gorham, Justin J. Curran, Aditya Raguram, Daniel M. DeLaughter, David A. Conner, Júlia D. C. Marsiglia, Sajeev Kohli, Lukas Chmatal, David C. Page, Nerea Zabaleta, Luk Vandenberghe, David R. Liu, Jonathan G. Seidman, and Christine Seidman. Efficient in vivo genome editing prevents hypertrophic cardiomyopathy in mice. Nature Medicine, 29:412-421, Feb 2023. URL: https://doi.org/10.1038/s41591-022-02190-7, doi:10.1038/s41591-022-02190-7. This article has 225 citations and is from a highest quality peer-reviewed journal.

19. (chai2023baseeditingcorrection pages 1-3): Andreas C. Chai, Miao Cui, Francesco Chemello, Hui Li, Kenian Chen, Wei Tan, Ayhan Atmanli, John R. McAnally, Yu Zhang, Lin Xu, Ning Liu, Rhonda Bassel-Duby, and Eric N. Olson. Base editing correction of hypertrophic cardiomyopathy in human cardiomyocytes and humanized mice. Nature Medicine, 29:401-411, Feb 2023. URL: https://doi.org/10.1038/s41591-022-02176-5, doi:10.1038/s41591-022-02176-5. This article has 193 citations and is from a highest quality peer-reviewed journal.

20. (joshua2023felinemyocardialtranscriptome pages 1-2): Jessica Joshua, Jeff Caswell, M. Lynne O’Sullivan, Geoffrey Wood, and Sonja Fonfara. Feline myocardial transcriptome in health and in hypertrophic cardiomyopathy—a translational animal model for human disease. PLOS ONE, 18:e0283244, Mar 2023. URL: https://doi.org/10.1371/journal.pone.0283244, doi:10.1371/journal.pone.0283244. This article has 19 citations and is from a peer-reviewed journal.

21. (stern2023hypertrophiccardiomyopathyin pages 1-3): Joshua A. Stern, Victor N. Rivas, Joanna L. Kaplan, Yu Ueda, Maureen S. Oldach, Eric S. Ontiveros, Kristina B. Kooiker, Sabine J. van Dijk, and Samantha P. Harris. Hypertrophic cardiomyopathy in purpose-bred cats with the a31p mutation in cardiac myosin binding protein-c. Scientific Reports, Jun 2023. URL: https://doi.org/10.1038/s41598-023-36932-5, doi:10.1038/s41598-023-36932-5. This article has 25 citations and is from a peer-reviewed journal.

22. (montag2018successfulknockinof pages 1-2): J. Montag, B. Petersen, A. K. Flögel, E. Becker, A. Lucas-Hahn, G. J. Cost, C. Mühlfeld, T. Kraft, H. Niemann, and B. Brenner. Successful knock-in of hypertrophic cardiomyopathy-mutation r723g into the myh7 gene mimics hcm pathology in pigs. Scientific Reports, Mar 2018. URL: https://doi.org/10.1038/s41598-018-22936-z, doi:10.1038/s41598-018-22936-z. This article has 57 citations and is from a peer-reviewed journal.

23. (pires2025exploringmyh7in pages 1-2): Lucas Vieira Lacerda Pires, Vinícius Machado Correia, Layara Fernanda Vicente Pereira Lipari, Fernanda Almeida Andrade, Fábio Fernandes, Vagner Madrini, Mariana Lombardi Peres de Carvalho, Giovanna Napolitano, Elisangela Aparecida da Silva, Kelvin Henrique Vilalva, Vitória Pelegrino do Val, and José Eduardo Krieger. Exploring myh7 in cardiomyopathies: genetic drivers and clinical outcomes. ABC Heart Fail Cardiomyop, Apr 2025. URL: https://doi.org/10.36660/abchf.20240054i, doi:10.36660/abchf.20240054i. This article has 1 citations.

24. (pires2025exploringmyh7in pages 5-6): Lucas Vieira Lacerda Pires, Vinícius Machado Correia, Layara Fernanda Vicente Pereira Lipari, Fernanda Almeida Andrade, Fábio Fernandes, Vagner Madrini, Mariana Lombardi Peres de Carvalho, Giovanna Napolitano, Elisangela Aparecida da Silva, Kelvin Henrique Vilalva, Vitória Pelegrino do Val, and José Eduardo Krieger. Exploring myh7 in cardiomyopathies: genetic drivers and clinical outcomes. ABC Heart Fail Cardiomyop, Apr 2025. URL: https://doi.org/10.36660/abchf.20240054i, doi:10.36660/abchf.20240054i. This article has 1 citations.

25. (abbas2024roleofgenetics pages 9-11): Mohammed Tiseer Abbas, Nima Baba Ali, Juan M. Farina, Ahmed K. Mahmoud, Milagros Pereyra, Isabel G. Scalia, Moaz A. Kamel, Timothy Barry, Steven J. Lester, Charles R. Cannan, Rohit Mital, Susan Wilansky, William K. Freeman, Chieh-Ju Chao, Said Alsidawi, Chadi Ayoub, and Reza Arsanjani. Role of genetics in diagnosis and management of hypertrophic cardiomyopathy: a glimpse into the future. Mar 2024. URL: https://doi.org/10.3390/biomedicines12030682, doi:10.3390/biomedicines12030682. This article has 29 citations.

26. (mobiuswinkler2024thediagnosisand pages 1-2): Maximilian N. Möbius-Winkler, Ulrich Laufs, and Karsten Lenk. The diagnosis and treatment of hypertrophic cardiomyopathy. Deutsches Arzteblatt international, Nov 2024. URL: https://doi.org/10.3238/arztebl.m2024.0196, doi:10.3238/arztebl.m2024.0196. This article has 14 citations and is from a peer-reviewed journal.

27. (sanghvi2025hypertrophiccardiomyopathymanagement pages 14-15): Mihir M Sanghvi, Eamon Dhall, C Anwar A. Chahal, Constantinos O'Mahony, Saidi A Mohiddin, Konstantinos Savvatis, Fabrizio Ricci, Patricia B Munroe, Steffen E Petersen, Nay Aung, and Mohammed Y Khanji. Hypertrophic cardiomyopathy management: a systematic review of the clinical practice guidelines and recommendations. European heart journal. Quality of care & clinical outcomes, Jan 2025. URL: https://doi.org/10.1093/ehjqcco/qcae117, doi:10.1093/ehjqcco/qcae117. This article has 16 citations.

## Artifacts

- [Edison artifact artifact-00](Hypertrophic_Cardiomyopathy_1-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 20 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 54 |
| Resolved | 49 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 13 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008647` (2 mentions) - the report calls it "if available"; MONDO calls it **hypertrophic cardiomyopathy 1**
- `HP:0031797` (1 mention) - the report calls it "Incomplete penetrance"; HP calls it **Clinical course**
- `HP:0001639` (2 mentions) - the report calls it "Sign; age-dependent, variable; defining overt phenotype"; HP calls it **Hypertrophic cardiomyopathy**
- `HP:0001645` (2 mentions) - the report calls it "Severe outcome, uncommon with modern management"; HP calls it **Sudden cardiac death**
- `NCIT:C139785` (1 mention) - the report calls it "Gene Editing"; NCIT calls it **Uterine Corpus Carcinoma and Carcinosarcoma pN2a TNM Finding v8**
- `HP:0005117` (1 mention) - the report calls it "Functional sign; commonly progressive with remodeling"; HP calls it **Elevated diastolic blood pressure**
- `HP:0001681` (1 mention) - the report calls it "Symptom, often exertional/microvascular"; HP calls it **Angina pectoris**
- `HP:0001279` (1 mention) - the report calls it "Episodic symptom"; HP calls it **Syncope**
- `HP:0031604` (1 mention) - the report calls it "Imaging/pathology sign; variable and progressive"; HP calls it **Agenesis of the carotid canal**
- `HP:0001644` (1 mention) - the report calls it "Late complication in a minority"; HP calls it **Dilated cardiomyopathy**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `NCIT:C29622` (1 mention) - NCIT does not contain this term
- `NCIT:C151608` (1 mention) - NCIT does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006936` (2 mentions) - the report calls it "Processes:** muscle contraction"; GO calls it **muscle contraction**
- `CL:0000746` (2 mentions) - the report calls it "Cells:** ventricular cardiomyocyte"; CL calls it **cardiac muscle cell**, and lists "cardiomyocyte" among its other names
- `GO:0030017` (1 mention) - the report calls it "Compartments:** sarcomere"; GO calls it **sarcomere**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `LOINC`.