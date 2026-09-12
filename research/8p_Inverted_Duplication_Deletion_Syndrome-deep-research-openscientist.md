---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-03T18:52:51.401677'
end_time: '2026-09-03T19:37:42.824001'
duration_seconds: 2691.42
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: 8p inverted duplication/deletion syndrome
  mondo_id: MONDO:0019876
  category: Chromosomal Disorder
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
citation_count: 20
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 20
  quotes_valid: 20
  relevance_assessed: 22
  on_topic: 16
  validator_version: 0.2.1
term_validation:
  total_terms: 47
  verified: 44
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 11
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: HP:0001252
    reported_labels:
    - Neonatal
    ontology_label: Hypotonia
  - term_id: HP:0001999
    reported_labels:
    - Congenital
    ontology_label: Abnormal facial shape
  - term_id: HP:0001250
    reported_labels:
    - "Mean 3.9 y (2 mo\u20139 y)"
    ontology_label: Seizure
  - term_id: HP:0000252
    reported_labels:
    - Congenital
    ontology_label: Microcephaly
  - term_id: HP:0000708
    reported_labels:
    - Childhood
    ontology_label: Atypical behavior
  - term_id: NCIT:C157664
    reported_labels:
    - Cardiac Surgery
    ontology_label: Poorly Marginated Nodule
  - term_id: NCIT:C15311
    reported_labels:
    - Nutritional Support
    ontology_label: Quality Control
  - term_id: NCIT:C15277
    reported_labels:
    - Supportive Care
    ontology_label: Mastectomy
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
  path: 8p_Inverted_Duplication_Deletion_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: 8p_Inverted_Duplication_Deletion_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** 8p inverted duplication/deletion syndrome
- **MONDO ID:** MONDO:0019876 (if available)
- **Category:** Chromosomal Disorder

## Research Objectives

Please provide a comprehensive research report on **8p inverted duplication/deletion syndrome** covering all of the
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

# 8p Inverted Duplication/Deletion Syndrome (inv dup del(8p)) — Comprehensive Disease Characterization Report

**Disease:** 8p inverted duplication/deletion syndrome
**MONDO ID:** MONDO:0019876
**Orphanet:** ORPHA:96092 ("Chromosome 8p inverted duplication/deletion")
**Category:** Chromosomal (contiguous-gene) disorder
**Report basis:** 5 autonomous investigation iterations, 11 confirmed findings, 53 primary papers reviewed

---

## Summary

8p inverted duplication/deletion syndrome (**inv dup del(8p)**) is a rare, almost invariably sporadic (de novo) contiguous-gene chromosomal disorder. It is defined by a single rearranged chromosome 8 that simultaneously carries a **terminal 8p deletion** (~6.7–11.4 Mb, 8p23.3→8p23.1) and an **inverted interstitial duplication** (~30–32 Mb, 8p23.1→8p11.1), the two imbalances being separated by a preserved single-copy (disomic) region delimited by the olfactory-receptor (OR) low-copy-repeat clusters (REPD/REPP). The rearrangement arises predominantly by **non-allelic homologous recombination (NAHR)** during **maternal meiosis** between these OR repeats, an event strongly predisposed by a common **paracentric 8p23.1 inversion polymorphism** carried in the heterozygous state by ~26% of individuals of European descent. Because the operative risk factor is the mother's benign inversion-carrier status rather than maternal age, and because the event is de novo, recurrence risk in a family is low.

The dual dosage imbalance drives a highly penetrant, multisystem phenotype. Terminal haploinsufficiency of dosage-sensitive transcription factors — most importantly **GATA4** and **SOX7** at 8p23.1 — together with triplosensitivity of the large interstitial duplication produces a recognizable clinical picture: developmental delay / intellectual disability in ~97% of patients, anomalies of the corpus callosum (agenesis/hypoplasia) in ~60–65%, infantile hypotonia, characteristic facial dysmorphism, congenital heart defects (notably atrioventricular/atrial septal defects), and seizures in ~30–35% (mean onset ~3.9 years). Severity is graded by the size and breakpoints of the imbalance and is attenuated by somatic mosaicism. Model organisms (mouse *Gata4*, zebrafish *sox7*) recapitulate the cardiac and vascular components, validating the dosage mechanism for the heart phenotype, though no model reproduces the whole contiguous imbalance.

Diagnosis is molecular-cytogenetic: **chromosomal microarray (CMA/aCGH/SNP-array)** defines the deletion+duplication pattern with precise breakpoints, with **karyotype** (typically add(8)(p23)/der(8)) and **FISH** confirmation and parental karyotyping to document de novo origin. Prenatally, diagnosis is triggered by ultrasound anomalies (increased nuchal translucency, ventriculomegaly, cardiac and renal defects) that can mimic trisomy 18. There is **no curative or disease-specific therapy**; management is symptomatic and multidisciplinary, and prevention is limited to genetic counseling and prenatal/preimplantation diagnosis.

---

## Section 1 — Disease Information

**Overview.** inv dup del(8p) is a recurrent structural chromosomal rearrangement of the short arm of chromosome 8, producing a contiguous-gene syndrome from combined deletion (dosage loss) and inverted duplication (dosage gain). The clinical entity is dominated by neurodevelopmental impairment, brain (corpus callosum) malformation, hypotonia, dysmorphism, and congenital heart disease.

**Key identifiers.**
- **MONDO:** MONDO:0019876
- **Orphanet:** ORPHA:96092 ("Chromosome 8p inverted duplication/deletion")
- **MeSH:** concept mapped to *Chromosomes, Human, Pair 8*
- **OMIM:** No single dedicated phenotype MIM number; covered under the contiguous-gene 8p23.1 deletion/duplication entries and **GATA4** (%607941)
- **ICD-10:** Q99.9 / Q93–Q95 range (chromosomal abnormalities); ICD-11: LD44 (chromosomal anomalies)

**Synonyms / alternative names:** inv dup del(8p); invdupdel(8p); inverted duplication deletion 8p syndrome; inverted duplication of 8p with terminal deletion; der(8) inverted duplication deletion syndrome; recombinant chromosome 8 (partial).

**Information source.** The knowledge base for this disorder is derived from **aggregated individual case reports and small cohort/case series** (the largest being 36 new patients plus a literature review), supplemented by prenatal diagnostic series and disease-level cytogenetic resources (Orphanet, DECIPHER, ClinVar). There is no large population-level EHR dataset.

---

## Section 2 — Etiology

**Primary cause (genetic, structural).** The disorder is caused by a de novo structural chromosomal rearrangement, not by environmental or infectious factors. The recurrent rearrangement combines a distal terminal deletion (8p23.3→8p23.1) with an inverted interstitial duplication (8p23.1→8p11.1) separated by a disomic region delimited by the OR gene clusters.

**Mechanism.** The rearrangement arises by **NAHR during maternal meiosis** between segmental duplications made up of OR gene clusters (REPD/REPP), facilitated by a paracentric **8p23.1 inversion polymorphism** present in ~26% of Europeans. A dicentric chromosome intermediate forms, breaks, and the resulting terminal deletion is stabilized by **telomere healing** (direct addition of telomeric repeats), or rarely by **telomere capture from 8q**.

> "Inverted 8p duplication deletions are recurrent chromosomal rearrangements that most often arise through non-allelic homologous recombination (NAHR) during maternal meiosis between segmental duplications made up of the olfactory receptor (OR) gene clusters. The presence of a paracentric inversion polymorphism in 8p23.1, found in approximately 26% of European population, may trigger meiotic misalignment and NAHR between the OR gene repeats." — [PMID: 24502041](https://pubmed.ncbi.nlm.nih.gov/24502041/)

> "The terminal deletions are stabilized by direct addition of telomeric repeats, so called telomere healing." — [PMID: 19041960](https://pubmed.ncbi.nlm.nih.gov/19041960/)

**Genetic risk factor.** The single established predisposing factor is **maternal heterozygosity for the 8p23.1 inversion polymorphism**, a benign structural variant that itself causes no phenotype but confers susceptibility to meiotic malsegregation. In the landmark study all 8 mothers of inv dup(8p) probands were inversion carriers ([PMID: 11231899](https://pubmed.ncbi.nlm.nih.gov/11231899/)).

**Environmental risk factors / protective factors / gene-environment interactions.** None are established. Because the event is a meiotic recombination error, there are no known environmental risk factors, protective exposures, or gene–environment interactions. Unlike aneuploidies, **maternal age is not the operative factor**; maternal inversion-carrier status is.

---

## Section 3 — Phenotypes

The phenotype is multisystem and highly penetrant. Frequencies below are drawn primarily from the largest cohort (36 new patients + literature review; [PMID: 34866188](https://pubmed.ncbi.nlm.nih.gov/34866188/)) and independent case series ([PMID: 35327368](https://pubmed.ncbi.nlm.nih.gov/35327368/)).

| Phenotype | Type | Frequency | Onset | HPO suggestion |
|---|---|---|---|---|
| Developmental delay / intellectual disability | Neurodevelopmental | ~97% (32/33) | Neonatal–infancy | HP:0001263 / HP:0001249 |
| Anomalies of the corpus callosum (agenesis/hypoplasia) | Structural CNS | ~63% (17/27 imaged) | Congenital | HP:0001274 / HP:0001338 |
| Muscular hypotonia | Neuromuscular | Very frequent (near-universal in series) | Neonatal | HP:0001252 |
| Dysmorphic facial features | Physical | Present in all cases of one series | Congenital | HP:0001999 |
| Seizures / epilepsy | Neurological | ~34% | Mean 3.9 y (2 mo–9 y) | HP:0001250 |
| Congenital heart defects (ASD/AVSD, others) | Cardiovascular | Frequent | Congenital | HP:0001627 / HP:0001671 |
| Psychomotor and language delay | Neurodevelopmental | Very frequent | Infancy | HP:0011342 / HP:0000750 |
| Orthopedic/skeletal anomalies (scoliosis, limb/joint) | Musculoskeletal | Frequent | Childhood | HP:0002751 / HP:0002650 |
| Microcephaly | Physical/CNS | Variable (deletion component) | Congenital | HP:0000252 |
| Behavioral problems | Behavioral | Variable | Childhood | HP:0000708 |

**Prenatal presentation.** Can mimic trisomy 18: increased nuchal translucency, ventriculomegaly, cardiac defects (including hypoplastic left heart), renal anomalies, and craniofacial dysmorphism.

**Characteristics.** Onset is congenital/neonatal; severity is variable (mild to severe); course is generally **stable/non-progressive** structurally but with lifelong disability; seizures may be episodic. Quality-of-life impact is substantial and lifelong: most survivors have persistent intellectual disability, hypotonia, and require ongoing developmental support, affecting mobility, communication, self-care, and independent living.

> "97% (n = 32/33) of patients presented with mild to severe developmental delay/ID and 34% had seizures with mean age of onset of 3.9 years (2 months-9 years). Moreover, out of the 24 patients with brain MRI and 3 fetuses with neuropathology analysis, 63% (n = 17/27) had AnCC." — [PMID: 34866188](https://pubmed.ncbi.nlm.nih.gov/34866188/)

> "The main clinical manifestations in all cases are psychomotor and language delay, muscle hypotonia, and dysmorphic facial features. Malformations of the central nervous system, such as corpus callosum agenesis, were found in five cases." — [PMID: 35327368](https://pubmed.ncbi.nlm.nih.gov/35327368/)

---

## Section 4 — Genetic / Molecular Information

**Causal lesion.** A single derivative chromosome 8 carrying a terminal deletion (8p23.3→8p23.1) + an inverted interstitial duplication (8p23.1→8p11.1), separated by a disomic segment bounded by OR clusters. This is a **structural (copy-number) variant**, classified **pathogenic** per ACMG/AMP CNV guidelines given established dosage-sensitive gene content.

**Key dosage-sensitive genes.**
- **GATA4** (8p23.1; HGNC:4173; OMIM %607941) — cardiac transcription factor; haploinsufficiency in the deletion drives congenital heart defects and contributes to diaphragmatic hernia.
- **SOX7** (8p23.1; HGNC:18196) — SoxF transcription factor; deletion contributes to cardiac/vascular defects.
- **NEIL2** (8p23.1) — implicated with GATA4/SOX7 in diaphragmatic defects by protein-interaction network analysis.
- **Defensin (DEFA/DEFB) cluster** (8p23.1) — deletion associated with reduced NK-cell activity and low α-defensin, contributing to infectious vulnerability.
- Candidate genes **XKR6** and **MIR597** proposed for absence seizures within the 8p23.1 interval.

> "implicated GATA4, NEIL2, and SOX7 in diaphragmatic defects. Sequence analysis of these genes in 226 chromosomally normal CDH patients, as well as in a small number of deletion 8p23.1 patients, showed rare unreported variants in the coding region" — [PMID: 23165946](https://pubmed.ncbi.nlm.nih.gov/23165946/)

> "This patient showed lower NK cell activity and α-defensin level compared with healthy controls. These results suggest that decreased NK cell activity can result from DEF haploinsufficiency." — [PMID: 35768224](https://pubmed.ncbi.nlm.nih.gov/35768224/)

**Reciprocal / related conditions.** The same NAHR mechanism generates reciprocal products: the supernumerary +der(8)(8p23.1pter) marker, the recurrent 8p23.1 interstitial deletion syndrome, and isolated 8p23.1 duplication syndrome (prevalence ~1/58,000), which produces a milder overlapping phenotype with GATA4 gain also linked to CHD.

> "The 8p23.1 duplication syndrome (8p23.1 DS) is a recurrent genomic condition with an estimated prevalence of 1 in 58,000." — [PMID: 26097203](https://pubmed.ncbi.nlm.nih.gov/26097203/)

**Modifier genes / epigenetics.** No specific trans-acting modifier genes are established for inv dup del(8p); phenotype modulation is driven mainly by rearrangement size/breakpoints and mosaicism (Section 9). No disease-specific epigenetic signature is documented.

**Chromosomal abnormality classification.** Complex intrachromosomal rearrangement (terminal deletion + inverted interstitial duplication) — cytogenetically add(8)(p23)/der(8). Allele frequencies are not applicable (recurrent de novo structural event, not an SNV). Origin is **germline** (maternal meiosis); somatic (postzygotic) mosaic forms occur.

---

## Section 5 — Environmental Information

**Not applicable.** No environmental factors, lifestyle factors, or infectious agents are implicated in causing inv dup del(8p). The disorder is a de novo meiotic recombination error. (Affected individuals have increased vulnerability to infections as a downstream *consequence* of DEF-cluster haploinsufficiency — see Sections 8 and 11 — but infections do not cause the syndrome.)

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. A mother carries the **8p23.1 paracentric inversion polymorphism** in the heterozygous state (present in ~26% of Europeans) → predisposes to meiotic misalignment.
2. During **maternal meiosis**, the OR gene clusters (REPD/REPP) flanking 8p23.1 misalign → **NAHR** between the repeats.
3. NAHR **results in** a **dicentric chromosome intermediate** (and a reciprocal acentric fragment).
4. The dicentric **breaks** asymmetrically → **leads to** a chromosome bearing a terminal 8p deletion + an inverted interstitial 8p duplication.
5. The broken terminal end is **stabilized by telomere healing** (direct telomeric-repeat addition) or, rarely, telomere capture from 8q → yields a stable derivative chromosome 8.
6. Fertilization transmits the derivative chromosome → the zygote has **terminal 8p23 haploinsufficiency + interstitial 8p triplosensitivity**.
7. **Haploinsufficiency of GATA4/SOX7/NEIL2** (deletion) → impaired cardiac transcription-factor dosage → **results in** congenital heart defects and (with diaphragm-expressed genes) diaphragmatic hernia. *(Demonstrated in model organisms.)*
8. **Haploinsufficiency of the DEF cluster** (deletion) → reduced NK-cell activity and α-defensin → **leads to** immune vulnerability and severe respiratory infections. *(Demonstrated in one patient.)*
9. **Combined dosage imbalance of many 8p genes** (deletion and duplication) → disrupted neurodevelopment → **results in** corpus callosum anomalies, intellectual disability, hypotonia, and seizures. *(Gene-specific causality largely inferred; corpus-callosum-anomaly risk region mapped.)*
10. Structural malformations + neurodevelopmental impairment → **lead to** the lifelong multisystem clinical phenotype.

### Detail by category

- **Molecular pathways / cellular processes.** The cardiac branch converges on **cardiac transcription-factor networks** (GATA4–TBX5–NKX2-5–HAND2; GATA4–GATA5–GATA6 combinatorial regulation) governing cardiomyocyte proliferation and septation. In mouse models, reduced Gata4 dosage lowers cardiomyocyte proliferation (Cdk4/Cdk2 downregulation; p21/Cdkn1a de-repression via FOG-2/NuRD). The vascular branch involves **SoxF–Notch** signaling (Sox7 upstream of hey2, efnb2, Dll4/Notch1) in arterial specification.
  - GO suggestions: heart development (GO:0007507), cardiac septum morphogenesis (GO:0003279), regulation of cardiomyocyte proliferation, arterial endothelial cell differentiation (GO:0060842), corpus callosum morphogenesis / axon guidance, forebrain development.
- **Protein dysfunction.** Loss-of-dosage (haploinsufficiency) of GATA4/SOX7 and gain-of-dosage of interstitial genes; the mechanism is quantitative (gene dosage), not a mutant-protein misfolding mechanism.
- **Immune involvement.** DEF-cluster haploinsufficiency → reduced NK activity/α-defensin → impaired innate antiviral defense.
- **Cell types (CL suggestions):** cardiomyocyte (CL:0000746), endocardial/endothelial cell (CL:0002350/CL:0000115), arterial endothelial cell (CL:1000413), neuron (CL:0000540), natural killer cell (CL:0000623), skeletal muscle myocyte (hypotonia; CL:0000188).

Upstream mechanisms are the meiotic NAHR event and the resulting dosage imbalance; downstream are the organ-specific developmental failures (heart, brain commissures, diaphragm, immune cells).

---

## Section 7 — Anatomical Structures Affected

**Organ / body-system level.**
- **Central nervous system** (primary): corpus callosum (agenesis/hypoplasia), cerebral ventricles (ventriculomegaly), brain generally — UBERON:0002336 (corpus callosum), UBERON:0000955 (brain), UBERON:0002285 (lateral ventricle).
- **Cardiovascular system** (primary): heart septa and valves, outflow tract, great vessels — UBERON:0000948 (heart), UBERON:0002099 (cardiac septum).
- **Musculoskeletal system:** skeletal muscle (hypotonia), spine (scoliosis), limbs/joints — UBERON:0001134 (skeletal muscle), UBERON:0001130 (vertebral column).
- **Craniofacial:** dysmorphic facial structures — UBERON:0001456 (face).
- **Diaphragm** (secondary, subset): congenital diaphragmatic hernia — UBERON:0001103 (diaphragm).
- **Renal** (secondary, prenatal): kidney anomalies — UBERON:0002113 (kidney).
- **Immune system** (secondary): NK-cell function — UBERON:0002405.

**Tissue / cell level.** Nervous tissue (callosal projection neurons, glia), cardiac muscle (cardiomyocytes) and endocardium/endothelium, skeletal muscle, NK cells.

**Subcellular level (GO CC).** Nucleus (transcription-factor localization; GO:0005634) is central given the dosage effect on nuclear transcription factors (GATA4, SOX7). No specific mitochondrial/ER/lysosomal defect is established.

**Localization / lateralization.** CNS and cardiac malformations are typically **midline/bilateral** (the corpus callosum is a midline commissure; septal defects are central). Rare **laterality defects** (dextrocardia with corpus callosum agenesis) are reported ([PMID: 20880309](https://pubmed.ncbi.nlm.nih.gov/20880309/)).

---

## Section 8 — Temporal Development

- **Onset:** Congenital — the chromosomal imbalance is present from conception; malformations are prenatal/neonatal. Prenatal detection is possible via ultrasound anomalies.
- **Onset pattern:** Chronic/congenital (structural anomalies fixed at birth); seizures have a later, childhood onset (mean 3.9 y, range 2 months–9 years).
- **Progression:** Structural anomalies are **stable/non-progressive**; the disorder is a **chronic, lifelong** condition. Developmental delay is persistent; seizures may be episodic and require ongoing management.
- **Disease course:** Non-remitting congenital disorder; no spontaneous remission of core features. Severity is set largely at conception by rearrangement extent (and any mosaicism).
- **Critical periods:** Embryonic organogenesis (cardiac septation, diaphragm formation ~E11.5–12.5 equivalent, commissural/corpus-callosum development) is the window in which the dosage imbalance produces malformations; the principal postnatal intervention window is **early developmental intervention** and surgical correction of malformations.

---

## Section 9 — Inheritance and Population

**Epidemiology.** inv dup del(8p) is **rare with no established population prevalence** (Orphanet lists it among rare chromosomal anomalies). For scale, the reciprocal isolated 8p23.1 duplication syndrome has an estimated prevalence of ~1/58,000. In an unselected pediatric developmental-disorder cohort, pathogenic 8p CNVs occurred in ~1% (10/966), of which inv dup del(8p) is a subset.

> "found 10 individuals with pathogenic copy number variants (CNVs) on the short arm of chromosome 8 (8p), representing approximately 1% of the patients analyzed" — [PMID: 20461109](https://pubmed.ncbi.nlm.nih.gov/20461109/)

**Inheritance.** **De novo, sporadic**, arising in **maternal meiosis**. Parental karyotypes are typically normal. The predisposing factor is maternal heterozygosity for the benign 8p23.1 inversion (~26% of Europeans). Recurrence risk is low. Rare somatic-mosaic forms occur postzygotically.

> "Since inv dup(8p)s originate consistently in maternal meiosis, we investigated the maternal chromosomes 8 in eight mothers of subjects with inv dup(8p) ... All the mothers were heterozygous for an 8p submicroscopic inversion that was delimited by the 8p-OR gene clusters and was present, in heterozygous state, in 26% of a population of European descent." — [PMID: 11231899](https://pubmed.ncbi.nlm.nih.gov/11231899/)

**Penetrance / expressivity.** Penetrance is high for the classic rearrangement; **expressivity is highly variable**, scaling with imbalance size/breakpoints and attenuated by mosaicism (below). No genetic anticipation (not a repeat-expansion disorder). Founder effects and consanguinity are not relevant. "Carrier frequency" in the classic sense does not apply; the relevant population parameter is the ~26% maternal inversion-polymorphism frequency (a susceptibility, not a disease-carrier state).

**Demographics.** Both sexes affected (autosomal; no strong sex bias reported). The inversion polymorphism is documented at ~26% in European-descent populations; the operative maternal factor is inversion-carrier status, not maternal age. The 8p23.1 segmental-duplication architecture is also a general genomic-instability hotspot (e.g., somatic 8p loss in ~31% of multiple myeloma).

---

## Section 10 — Diagnostics

**Definitive diagnosis is molecular-cytogenetic.**
- **Chromosomal microarray (CMA; aCGH or SNP-array):** first-line; defines precise breakpoints and the characteristic pattern — terminal 8p deletion + interstitial inverted duplication separated by a single-copy disomic region.
- **G-banded karyotype:** typically shows add(8)(p23) or der(8).
- **Metaphase FISH:** confirms the inverted duplication and 8p subtelomere deletion; subtelomeric/centromeric/whole-chromosome painting probes.
- **Parental karyotyping:** documents de novo origin and can reveal the maternal 8p23.1 inversion.

> "aCGH detected an 11.35 Mb deletion in 8p23.3-p23.1 encompassing SOX7 and GATA4, and a 31.99 Mb duplication in 8p23.1-p11.1 in the fetus. Metaphase FISH confirmed inv dup del(8p)." — [PMID: 27343326](https://pubmed.ncbi.nlm.nih.gov/27343326/)

**Prenatal diagnosis.** Invasive testing (CVS/amniocentesis) with CMA is prompted by ultrasound findings — increased NT, ventriculomegaly, cardiac defects, renal/craniofacial anomalies — that can mimic trisomy 18. In prenatal SNP-array cohorts, multisystem ultrasound anomalies confer the highest CMA yield (~27%) and increased NT is the strongest soft-marker predictor of chromosomal pathology.

> "multisystem anomalies conferred the highest risk (27.3%), driven predominantly by aneuploidies; among soft markers, increased nuchal translucency (NT) emerged as the strongest predictor of chromosomal pathology" — [PMID: 42067806](https://pubmed.ncbi.nlm.nih.gov/42067806/)

**Supporting clinical work-up.** Brain **MRI** (corpus callosum anomalies, ventriculomegaly); **echocardiography** (septal/valve defects); orthopedic/skeletal evaluation; immune work-up (NK-cell activity, α-defensin) where infections recur. **Prenatal WGS** and low-coverage WGS can also detect the large CNVs with performance comparable to CMA.

**Differential diagnosis.** Trisomy 18 (prenatal overlap), isolated 8p23.1 deletion or duplication syndromes, other contiguous-gene syndromes with corpus callosum agenesis and CHD, Kabuki-like phenotypes; distinguished by the characteristic dual deletion+duplication CMA signature.

**Screening.** No population/newborn screening exists for inv dup del(8p); detection is via diagnostic (not screening) CMA prompted by phenotype, or prenatally by ultrasound-triggered testing.

---

## Section 11 — Outcome / Prognosis

**Nature.** Chronic, lifelong congenital disorder; **no cure**; management supportive.

**Mortality.** Prognosis is dominated by malformation severity. **Congenital heart defects** (including hypoplastic left heart) and **congenital diaphragmatic hernia** are the principal life-threatening complications; neonatal death occurs with severe cardiac malformation (e.g., severe polyvalvular dysplasia, death at day 12).

> "the present case had severe polyvalvular dysplasia and the infant deceased at day 12 of life" — [PMID: 28211984](https://pubmed.ncbi.nlm.nih.gov/28211984/)

> "Recurrent interstitial deletion of a region of 8p23.1 flanked by the low copy repeats 8p-OR-REPD and 8p-OR-REPP is associated with a spectrum of anomalies that can include congenital heart malformations and congenital diaphragmatic hernia (CDH). Haploinsufficiency of GATA4 is thought to play a critical role in the development of these birth defects." — [PMID: 19606479](https://pubmed.ncbi.nlm.nih.gov/19606479/)

**Morbidity.** Survivors have persistent intellectual disability, hypotonia, orthopedic problems (scoliosis, joint/limb anomalies), and require lifelong developmental support. **Immune vulnerability** (DEF haploinsufficiency) predisposes to severe respiratory infections (severe RSV bronchiolitis; a severe COVID-19 case requiring 26-day hospitalization with 9 days in PICU and mechanical ventilation).

> "This patient showed lower NK cell activity and α-defensin level compared with healthy controls." — [PMID: 35768224](https://pubmed.ncbi.nlm.nih.gov/35768224/)

**Prognostic factors.** Rearrangement size/breakpoints, presence and severity of CHD/CDH, and mosaicism. **Milder outcomes** occur with smaller duplications, isolated terminal deletions distal to GATA4, or somatic mosaicism.

> "This female has developmental delay, but lacks congenital anomalies that are associated with either 8p abnormality in non-mosaic form. The attenuated phenotype in this individual may be due to compensation of one cell line for imbalances in the other cell line." — [PMID: 20830805](https://pubmed.ncbi.nlm.nih.gov/20830805/)

> "unlike the inv dup del(8p), the phenotype in our case is milder with no central nervous system malformations or cardiac defects" — [PMID: 18302246](https://pubmed.ncbi.nlm.nih.gov/18302246/)

---

## Section 12 — Treatment

**No disease-specific or curative therapy exists.** There are no pharmacological, gene, or cell therapies targeting the rearrangement, and no registered disease-specific clinical trials. Management is **supportive and multidisciplinary**:

| Domain | Intervention | NCIT suggestion |
|---|---|---|
| Development | Early developmental intervention; physical, occupational, speech therapy | Rehabilitation Therapy (NCIT:C15917) |
| Cardiac | Surgical repair of congenital heart defects | Cardiac Surgery (NCIT:C157664) |
| Diaphragm | Surgical repair of diaphragmatic hernia | Surgical Procedure (NCIT:C15329) |
| Epilepsy (~34%) | Anti-seizure medication | Anticonvulsant Agent (NCIT:C264) |
| Orthopedic | Management of scoliosis/limb/joint anomalies | Orthopedic Procedure |
| Nutrition/feeding | Feeding support | Nutritional Support (NCIT:C15311) |
| Infections | Intensive/critical care (mechanical ventilation, dexamethasone, remdesivir in severe COVID-19) | Supportive Care (NCIT:C15277) |

> "There, she was mechanically ventilated, received dexamethasone and remdesivir, and was hospitalized for 26 days, nine of which were in the pediatric intensive care unit." — [PMID: 37829974](https://pubmed.ncbi.nlm.nih.gov/37829974/)

**Pharmacogenomics, advanced therapeutics, targeted/immunotherapy, personalized medicine:** none applicable/available for this disorder.

---

## Section 13 — Prevention

- **Primary prevention:** Not possible (de novo meiotic event). No vaccination or risk-factor modification prevents the rearrangement.
- **Secondary prevention:** **Prenatal diagnosis** by CMA (prompted by ultrasound anomalies/increased NT) enables informed reproductive decisions and delivery planning. Preimplantation genetic testing is an option for known inversion carriers.
- **Tertiary prevention:** Prevent complications — surgical correction of malformations, seizure control, and **infection prophylaxis** (COVID-19 vaccination and RSV prophylaxis are advised given the DEF-related immune vulnerability).
- **Genetic counseling:** Central preventive measure. Because the event arises de novo from a common benign maternal inversion polymorphism, recurrence risk is low, but the same NAHR mechanism can generate reciprocal deletion/duplication products, so prenatal monitoring is recommended.

> "Prenatal diagnosis should be performed to monitor the recurrent risk of inv dup del(8p), as well as the other three harmful consequences resulted from the same NAHR mechanism." — [PMID: 20677137](https://pubmed.ncbi.nlm.nih.gov/20677137/)

---

## Section 14 — Other Species / Natural Disease

There is **no naturally occurring animal disease** equivalent to inv dup del(8p) — the specific human 8p23.1 OR-cluster/inversion architecture and NAHR-driven rearrangement are human-specific. However, the **individual dosage-sensitive genes are evolutionarily conserved** and modeled experimentally (Section 15):
- **Mouse *Gata4*** (NCBI Gene 14463) — ortholog of human GATA4.
- **Zebrafish *sox7*, *sox18*** — orthologs of the human SOXF family.
- Taxonomy: *Mus musculus* (NCBI:txid10090), *Danio rerio* (NCBI:txid7955).

No zoonotic potential or cross-species transmission (non-infectious genetic disorder). No breed-specific (VBO) associations.

---

## Section 15 — Model Organisms

No single model reproduces the entire inv dup del(8p) contiguous imbalance, but **gene-specific models recapitulate the cardiac and vascular components**, validating the dosage mechanism.

**Mouse (mammalian):**
- *Gata4* is a core cardiac transcription factor; disruption causes congenital heart defects. **Gata4(+/-);Tbx5(+/-)** embryos show decreased atrial/ventricular myocardial thickness and atrioventricular septation defects with reduced cardiomyocyte proliferation (Cdk4/Cdk2 downregulation).
- **Gata4/Gata5** compound heterozygotes develop double-outlet right ventricle, VSDs, and valve defects.

> "Gata4(+/-);Tbx5(+/-) mouse embryos display decreased atrial and ventricular myocardial thickness at E11.5, prior to cardiac septation." — [PMID: 24858909](https://pubmed.ncbi.nlm.nih.gov/24858909/)

**Zebrafish:**
- *sox7* mutants show a "short circulatory loop" from aberrant artery–vein connections; Sox7 acts upstream of Notch (hey2, efnb2) in arterial specification. Combined Sox7/Sox18 loss ablates the dorsal aorta.

> "sox7 mutants display a short circulatory loop around the heart as a result of aberrant connections between the lateral dorsal aorta (LDA) and either the venous primary head sinus (PHS) or the common cardinal vein (CCV)" — [PMID: 25834021](https://pubmed.ncbi.nlm.nih.gov/25834021/)

**Model characteristics.** These models faithfully reproduce the **cardiac septal/outflow and vascular defects** of the 8p23.1-deletion component. **Limitations:** they capture only single-gene dosage effects, not the combined deletion+duplication imbalance, the neurodevelopmental/corpus-callosum phenotype, or the immune (defensin) component. **Resources:** MGI (mouse *Gata4*), ZFIN (zebrafish *sox7*/*sox18*).

---

## Mechanistic Model (Synthesis)

```
Maternal 8p23.1 inversion polymorphism (heterozygous, ~26% Europeans)
                    │  predisposes to
                    ▼
   Meiotic misalignment of OR repeats (REPD/REPP) at 8p23.1
                    │  NAHR
                    ▼
        Dicentric chromosome 8 intermediate
                    │  asymmetric breakage
                    ▼
  der(8): TERMINAL 8p DELETION  +  INVERTED INTERSTITIAL 8p DUPLICATION
                    │  stabilized by telomere healing / (rare) 8q capture
                    ▼
     ┌──────────────┴───────────────┬──────────────────────┐
     ▼                              ▼                      ▼
 GATA4/SOX7/NEIL2 loss        DEF cluster loss      Global 8p dosage imbalance
 (deletion, dosage↓)          (deletion)            (deletion + duplication)
     │                              │                      │
     ▼                              ▼                      ▼
 Congenital heart defects     ↓NK activity,         Corpus callosum anomalies,
 ± diaphragmatic hernia       ↓α-defensin           ID, hypotonia, seizures,
 [model-validated]            → severe infections    dysmorphism [largely inferred]
     └──────────────┬───────────────┴──────────────────────┘
                    ▼
        Lifelong multisystem clinical phenotype
```

**Upstream** = the maternal inversion + NAHR + dosage imbalance. **Downstream** = organ-specific developmental failures. The cardiac and vascular branches are experimentally demonstrated (mouse/zebrafish); the neurodevelopmental branch is well correlated but gene-level causality remains largely inferred.

---

## Evidence Base — Key Literature

| PMID | Contribution | Evidence type |
|---|---|---|
| [24502041](https://pubmed.ncbi.nlm.nih.gov/24502041/) | NAHR/maternal-meiosis/OR-cluster mechanism; 26% inversion frequency | Human, cytogenetic |
| [11231899](https://pubmed.ncbi.nlm.nih.gov/11231899/) | Landmark: maternal meiotic origin; all mothers inversion carriers | Human, cytogenetic |
| [19041960](https://pubmed.ncbi.nlm.nih.gov/19041960/) | Telomere healing stabilizes terminal deletion; 8q telomere capture | Human, case |
| [34866188](https://pubmed.ncbi.nlm.nih.gov/34866188/) | Largest cohort (36 pts): ID 97%, seizures 34%, AnCC 63% | Human, cohort |
| [35327368](https://pubmed.ncbi.nlm.nih.gov/35327368/) | 8-case series: psychomotor/language delay, hypotonia, dysmorphism, CC agenesis | Human, series |
| [23165946](https://pubmed.ncbi.nlm.nih.gov/23165946/) | GATA4/NEIL2/SOX7 → diaphragmatic (and cardiac) defects | Human + network |
| [35768224](https://pubmed.ncbi.nlm.nih.gov/35768224/) | DEF haploinsufficiency → low NK activity/α-defensin → severe RSV | Human, case |
| [26097203](https://pubmed.ncbi.nlm.nih.gov/26097203/) | Reciprocal 8p23.1 duplication prevalence ~1/58,000 | Human, cohort |
| [28533195](https://pubmed.ncbi.nlm.nih.gov/28533195/) | 8p23.1 deletion syndrome spectrum (CHD, ID, behavior, microcephaly, epilepsy) | Human, review/case |
| [18393291](https://pubmed.ncbi.nlm.nih.gov/18393291/) | GATA4 as causal gene for cardiac phenotype | Human, mapping |
| [24858909](https://pubmed.ncbi.nlm.nih.gov/24858909/) | Mouse Gata4/Tbx5: myocardial/septation defects | Mouse model |
| [25834021](https://pubmed.ncbi.nlm.nih.gov/25834021/) | Zebrafish sox7: cardiovascular defects, Sox7 upstream of Notch | Zebrafish model |
| [27343326](https://pubmed.ncbi.nlm.nih.gov/27343326/) | aCGH + FISH diagnostic workflow (SOX7/GATA4 deletion) | Human, prenatal |
| [42067806](https://pubmed.ncbi.nlm.nih.gov/42067806/) | Prenatal CMA yield; NT strongest predictor | Human, cohort |
| [28211984](https://pubmed.ncbi.nlm.nih.gov/28211984/) | Neonatal mortality from severe polyvalvular dysplasia | Human, case |
| [19606479](https://pubmed.ncbi.nlm.nih.gov/19606479/) | 8p23.1 deletion → CHD + CDH; GATA4 haploinsufficiency critical | Human, series |
| [37829974](https://pubmed.ncbi.nlm.nih.gov/37829974/) | Severe COVID-19 in affected infant; intensive care | Human, case |
| [20677137](https://pubmed.ncbi.nlm.nih.gov/20677137/) | Prenatal diagnosis/counseling as prevention | Human, case |
| [20830805](https://pubmed.ncbi.nlm.nih.gov/20830805/) | Mosaicism attenuates phenotype | Human, case |
| [18302246](https://pubmed.ncbi.nlm.nih.gov/18302246/) | Tandem vs inverted duplication modulates severity | Human, case |
| [20461109](https://pubmed.ncbi.nlm.nih.gov/20461109/) | Pathogenic 8p CNVs ~1% of developmental-disorder cohort | Human, cohort |
| [20880309](https://pubmed.ncbi.nlm.nih.gov/20880309/) | Dextrocardia + corpus callosum agenesis (laterality) | Human, case |

---

## Limitations and Knowledge Gaps

1. **No prevalence estimate.** The disorder's true incidence/prevalence is unknown; evidence is from case reports and small series, biasing toward severe/recognizable cases.
2. **Neurodevelopmental gene-level causality is inferred, not demonstrated.** While the cardiac (GATA4/SOX7) and immune (DEF) branches are mechanistically supported by models/patient data, the specific genes responsible for corpus callosum anomalies, intellectual disability, and seizures within the large duplication/deletion intervals are not individually proven.
3. **No whole-syndrome animal model.** Existing models capture single-gene dosage effects only; the combined deletion+duplication imbalance and the neurodevelopmental phenotype are not modeled.
4. **Genotype–phenotype correlation is incomplete.** One 8-case series found no clear correlation between molecular-cytogenetic variants and clinical severity, though a corpus-callosum-anomaly risk region has been mapped.
5. **No natural-history/QoL data.** Longitudinal outcome, life-expectancy, and standardized quality-of-life data are lacking.
6. **Epigenetic and multi-omic characterization absent.** No transcriptomic, proteomic, metabolomic, or methylation profiling specific to inv dup del(8p) is available.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international registry** to define prevalence, natural history, mortality, and QoL with standardized instruments.
2. **Breakpoint–phenotype mapping** across large CMA cohorts to refine the corpus-callosum, seizure, and ID critical regions and to test dosage of specific candidate genes (XKR6, MIR597, and duplication-interval genes).
3. **Neurodevelopmental modeling:** generate patient-derived iPSCs / cerebral organoids carrying the rearrangement (or engineered 8p dosage changes) to test corpus-callosum/neuronal phenotypes and identify driver genes.
4. **Systematic immune phenotyping** (NK activity, α-defensin, infection history) across a patient cohort to determine how consistently DEF haploinsufficiency causes clinically relevant immunodeficiency and to guide prophylaxis (RSV, COVID-19 vaccination).
5. **Prospective cardiac outcome study** correlating GATA4/SOX7 deletion status with CHD type/severity and surgical outcomes.
6. **Transcriptomic/methylation profiling** of patient tissues (or organoids) to search for a diagnostic episignature and downstream dysregulated pathways.

---

*Report compiled from 5 investigation iterations, 11 confirmed findings, and 53 primary papers. Evidence types are distinguished throughout as human clinical, model organism, in vitro, or computational.*


## Artifacts

- [OpenScientist final report](8p_Inverted_Duplication_Deletion_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](8p_Inverted_Duplication_Deletion_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 20 |
| Quoted claims found in source | 20 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 22 |
| On topic | 16 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 47 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 22 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001252` (1 mention) - the report calls it "Neonatal"; HP calls it **Hypotonia**
- `HP:0001999` (1 mention) - the report calls it "Congenital"; HP calls it **Abnormal facial shape**
- `HP:0001250` (1 mention) - the report calls it "Mean 3.9 y (2 mo–9 y)"; HP calls it **Seizure**
- `HP:0000252` (1 mention) - the report calls it "Congenital"; HP calls it **Microcephaly**
- `HP:0000708` (1 mention) - the report calls it "Childhood"; HP calls it **Atypical behavior**
- `NCIT:C157664` (1 mention) - the report calls it "Cardiac Surgery"; NCIT calls it **Poorly Marginated Nodule**
- `NCIT:C15311` (1 mention) - the report calls it "Nutritional Support"; NCIT calls it **Quality Control**
- `NCIT:C15277` (1 mention) - the report calls it "Supportive Care"; NCIT calls it **Mastectomy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0007507` (1 mention) - the report calls it "GO suggestions: heart development"; GO calls it **heart development**
- `UBERON:0001134` (1 mention) - the report calls it "skeletal muscle"; UBERON calls it **skeletal muscle tissue**, and lists "skeletal muscle" among its other names
- `NCIT:C15917` (1 mention) - the report calls it "Rehabilitation Therapy"; NCIT calls it **Arterial Embolization**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.