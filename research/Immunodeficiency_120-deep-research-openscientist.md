---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-22T16:58:06.046068'
end_time: '2026-09-22T17:37:52.110081'
duration_seconds: 2386.06
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Immunodeficiency 120
  mondo_id: MONDO:0970994
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
citation_count: 3
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 51
  verified: 48
  not_found: 1
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.02
  labels_checked: 29
  labels_matching: 10
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: MONDO:0970994
    reported_labels:
    - MONDO
    ontology_label: immunodeficiency 120
  - term_id: HP:0002326
    reported_labels:
    - Herpes simplex disease
    ontology_label: Transient ischemic attack
  - term_id: HP:0200042
    reported_labels:
    - Clinical sign
    ontology_label: Skin ulcer
  - term_id: HP:0031521
    reported_labels:
    - Clinical sign
    ontology_label: Vaginal clear cell adenocarcinoma
  - term_id: HP:0005387
    reported_labels:
    - Decreased antibody level in blood
    ontology_label: Combined immunodeficiency
  - term_id: HP:0004322
    reported_labels:
    - Physical manifestation
    ontology_label: Short stature
  - term_id: HP:0007018
    reported_labels:
    - Behavioral
    ontology_label: Attention deficit hyperactivity disorder
  - term_id: HP:0000407
    reported_labels:
    - Physical manifestation
    ontology_label: Sensorineural hearing impairment
  - term_id: UBERON:0002048
    reported_labels:
    - Respiratory tract / lungs
    - lung
    ontology_label: lung
  labels_variant: 10
  unresolved_terms:
  - HP:0410413
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Immunodeficiency_120-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Immunodeficiency_120-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 120
- **MONDO ID:** MONDO:0970994 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 120** covering all of the
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

# Immunodeficiency 120 (IMD120): A Comprehensive Disease Characterization

**Disease:** Immunodeficiency 120 (IMD120)
**MONDO ID:** MONDO:0970994 · **OMIM:** #620836 · **Causal gene:** *POLD1* (HGNC:9175, OMIM 174761), chromosome 19q13.33
**Category:** Mendelian, autosomal recessive combined immunodeficiency
**Report date:** 2026-09-22

---

## Summary

**Immunodeficiency 120 (IMD120) is an ultra-rare autosomal recessive combined immunodeficiency caused by biallelic hypomorphic (partial loss-of-function) variants in *POLD1*, the gene encoding the p125 catalytic and proofreading subunit of DNA polymerase delta (Polδ), the principal lagging-strand replicase of the eukaryotic genome.** Because complete loss of *POLD1* is incompatible with cellular viability, the disease arises only from partial (hypomorphic) alleles that leave residual Polδ function. The consequence is a state of chronic **replicative stress** that selectively impairs the proliferation of highly dividing lymphocytes — most conspicuously T cells — producing T-cell lymphopenia, impaired T-cell (but not B-cell) proliferation, hypogammaglobulinemia, and recurrent infections with a striking susceptibility to herpesviruses. A subset of patients also display syndromic features (short stature, intellectual disability, hearing loss), reflecting the housekeeping role of Polδ in all replicating tissues.

The disorder was delineated from just **two unrelated families** in the founding literature: Cui et al. 2020 ([PMID: 31629014](https://pubmed.ncbi.nlm.nih.gov/31629014/)), who described a consanguineous Turkish kindred homozygous for *POLD1* p.R1060C, and Conde et al. 2019 ([PMID: 31449058](https://pubmed.ncbi.nlm.nih.gov/31449058/)), who described a family with compound-heterozygous *POLD1* variants and a related *POLD2*-deficient patient. A central mechanistic insight from this investigation is that pathogenic genotypes converge on reduced functional Polδ output through **two distinct biochemical routes**: (1) destabilization of the Polδ holoenzyme complex with impaired recruitment of Replication Factor C (RFC) — the mechanism of p.R1060C in the C-terminal CysB metal-binding motif; and (2) reduced intrinsic polymerase catalytic activity with preserved complex assembly — the mechanism of the p.Q684H+p.S939W in-cis alleles near the polymerase active site.

Clinically, IMD120 is managed with **immunoglobulin replacement therapy (IgRT)** plus **antiviral (acyclovir) prophylaxis**, which effectively controls infections. **Reduced-intensity-conditioning hematopoietic stem cell transplantation (HSCT)** has been reported as a feasible curative option (Keles et al. 2026, PMID 42104577), though the DNA-repair/replication defect raises theoretical concerns about conditioning toxicity and long-term genome-instability risk. No dedicated immunodeficiency animal model exists; existing *Pold1* mouse models are either embryonic-lethal (null) or cancer-prone proofreading mutants, neither of which recapitulates the human immune phenotype. Notably, *POLD1* is a strikingly pleiotropic locus: different allele classes produce autosomal dominant MDPL progeroid syndrome, autosomal recessive nonsyndromic hearing loss, and colorectal cancer predisposition — placing IMD120 within a broader *POLD1* allelic series.

---

## Section 1 — Disease Information

**Overview.** Immunodeficiency 120 (IMD120) is a Mendelian, autosomal recessive **combined immunodeficiency** (affecting both cellular/T-cell and, secondarily, humoral/antibody immunity) resulting from biallelic mutations in *POLD1*. The disease is best understood as a **replicative-stress T-cell immunodeficiency**: partial impairment of DNA polymerase delta compromises the DNA replication that lymphocytes require for clonal proliferation upon antigen encounter, so patients present with recurrent infections (especially herpetic/viral), T-cell lymphopenia, and impaired T-cell proliferation.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | #620836 (Immunodeficiency 120) |
| MONDO | MONDO:0970994 |
| Causal gene | *POLD1* — OMIM 174761, HGNC:9175 |
| OMIM Phenotypic Series | PS300755 (combined immunodeficiency) |
| Cytogenetic location | 19q13.33 |
| Orphanet / ICD-10 / ICD-11 / MeSH | No dedicated code identified (ultra-rare; typically coded under generic combined immunodeficiency / D81 categories) |

**Synonyms / alternative names.** "POLD1 deficiency," "POLD1-associated combined immunodeficiency," "combined immunodeficiency due to POLD1 mutation," and (descriptively) "syndromic immunodeficiency with replicative stress" (Conde et al. 2019).

**Information source.** The disease-level entry is derived from **aggregated resources** (OMIM, MONDO) that in turn summarize a small number of **individual patient reports** (case series from two families). All clinical data are individual-patient in origin; there are no EHR-scale or registry datasets for this ultra-rare condition.

---

## Section 2 — Etiology

**Primary cause — genetic.** IMD120 is a monogenic disorder caused by **biallelic (homozygous or compound heterozygous) hypomorphic mutations in *POLD1***. There is no environmental or infectious cause of the underlying disease, although infectious exposures determine the clinical manifestations (the immune defect is unmasked by pathogen encounter). The recurrent, especially herpetic, infections are a *consequence* of the genetic defect rather than a cause.

**Genetic risk factors.**
- **Causal variants:** p.R1060C (c.3178C>T; homozygous; Cui 2020); compound-heterozygous variants including p.Q684H + p.S939W in cis (Conde 2019).
- **Consanguinity** is a major contributor: the index kindred was a consanguineous Turkish family, and the related *POLD2* patient was also from a consanguineous union. Consanguinity greatly elevates the chance of homozygosity for rare recessive hypomorphic alleles.
- **Modifier genes:** none formally established for IMD120. Given the shared holoenzyme, *POLD2*, *POLD3*, and *POLD4* subunit dosage are biologically plausible modifiers, but no human data exist.

**Environmental / lifestyle risk factors.** None identified as disease-causing. As with any T-cell immunodeficiency, exposure to herpesviruses and respiratory pathogens drives morbidity.

**Protective factors.** No genetic or environmental protective factors have been characterized. Conceptually, the only "protective" allele state is retention of at least one functional *POLD1* allele (heterozygous carriers are asymptomatic for IMD120).

**Gene–environment interactions.** The core interaction is **genotype × pathogen exposure**: the hypomorphic Polδ genotype produces a proliferation-limited T-cell compartment that fails to mount adequate clonal responses, so environmental pathogen load (herpesviruses, respiratory bacteria/viruses) determines the frequency and severity of clinical episodes.

---

## Section 3 — Phenotypes

IMD120 phenotypes fall into three groups: (a) **infection susceptibility**, (b) **immunologic/laboratory abnormalities**, and (c) **syndromic/developmental features**. Onset is in **early childhood/infancy**, and the course is chronic.

| Phenotype | Type | HPO suggestion | Onset / severity / frequency |
|---|---|---|---|
| Recurrent infections (esp. herpetic/viral) | Clinical sign | HP:0002719 (Recurrent infections); HP:0004429 (Recurrent viral infections) | Early childhood; moderate–severe; core feature in both families |
| Recurrent herpes (oral herpes, herpes zoster) | Clinical sign | HP:0002326 (Herpes simplex disease) | Recurrent episodes every 1–2 months in index patient |
| Recurrent respiratory tract infections → bronchiectasis | Clinical sign | HP:0002205; HP:0002110 (Bronchiectasis) | From infancy; bronchiectasis by age 6 months (Conde 2019); severe |
| Molluscum contagiosum (chronic facial) | Clinical sign | HP:0200042 | Chronic; viral susceptibility marker |
| Recurrent skin abscesses | Clinical sign | HP:0031521 | Recurrent |
| T-cell lymphopenia (↓CD4, esp. ↓CD8; naive-cell loss) | Laboratory abnormality | HP:0005403 (T lymphocytopenia); HP:0410413 | Congenital/early; core feature |
| Impaired T-cell (not B-cell) proliferation | Laboratory abnormality | HP:0031381 (Decreased proliferation of T cells) | Diagnostic hallmark |
| Hypogammaglobulinemia (↓IgG, low IgA/IgM) | Laboratory abnormality | HP:0004313 / HP:0002850 | Mild–moderate; IgRT-responsive |
| Impaired vaccine (tetanus) antibody response | Laboratory abnormality | HP:0005387 (Decreased antibody level in blood) | Present despite full vaccination |
| B-cell and NK-cell reduction | Laboratory abnormality | HP:0010976 (B lymphocytopenia); HP:0040218 (Reduced NK cell count) | Reported in Conde 2019 family |
| Short stature | Physical manifestation | HP:0004322 | Childhood; syndromic subset |
| Intellectual disability / speech delay | Behavioral/developmental | HP:0001249; HP:0000750 | Severe impairment with poor speech (Conde 2019); mild in OMIM |
| Attention deficits / hyperactivity | Behavioral | HP:0007018 | Reported subset |
| Sensorineural hearing loss | Physical manifestation | HP:0000407 | OMIM-listed feature |

**Immunophenotypic signature (from Cui 2020, verified quote):** *"The patients exhibited decreased numbers of naive CD4 and especially CD8 T cells in favor of effector memory subpopulations."* The T-cell compartment additionally showed **oligoclonality and restricted TCR-β V-J pairing** — hallmarks of a proliferation-restricted, contracted T-cell repertoire.

**Quality-of-life impact.** No formal EQ-5D/SF-36/PROMIS data exist for this ultra-rare disease. Qualitatively, recurrent infections, bronchiectasis (irreversible structural lung damage), lifelong IgRT dependence, and — in syndromic patients — intellectual disability and hearing loss produce substantial cumulative disability and care burden.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *POLD1* (DNA polymerase delta 1, catalytic subunit; p125), OMIM 174761, HGNC:9175, at 19q13.33. POLD1 provides both the **5′→3′ polymerase** and the **3′→5′ exonuclease (proofreading)** activities of Polδ and anchors the four-subunit holoenzyme (POLD1/POLD2/POLD3/POLD4).

**Pathogenic variants (IMD120-causing, biallelic).**

| Variant | Family | Zygosity | Location | Functional consequence |
|---|---|---|---|---|
| p.R1060C (c.3178C>T; exon 26; NM_001256849.1; rs777018011; OMIM 174761.0007) | Cui 2020 (Turkish, consanguineous) | Homozygous | C-terminal **CysB metal-binding motif** | **Destabilizes** Polδ complex → ↓POLD1/POLD2/POLD3 levels; impaired RFC recruitment |
| p.Q684H + p.S939W (in cis; NM_002691) | Conde 2019 (patient 2) | Compound het | Near **polymerase active site** | **Reduces intrinsic catalytic activity** without affecting complex stability |

- **Variant classification (ACMG/AMP):** pathogenic/likely pathogenic on the basis of segregation, absence from population databases, and functional validation.
- **Variant type/class:** missense (both established genotypes). p.R1060C is absent from gnomAD/ExAC/dbSNP/1000 Genomes — consistent with an ultra-rare recessive allele.
- **Somatic vs germline:** **germline** (inherited, biallelic).
- **Functional consequence:** **partial loss of function (hypomorphic)**. Complete loss of function is not viable (see Section 15). The two genotypes represent convergent hypofunction via different biochemical mechanisms (Finding F007).

**Allelic series at *POLD1* (important for interpretation).** *POLD1* is highly pleiotropic; the allele class determines the phenotype:

| Phenotype | OMIM | Inheritance | Representative allele(s) |
|---|---|---|---|
| **IMD120** (combined immunodeficiency) | #620836 | AR | biallelic hypomorphic missense (p.R1060C; p.Q684H+p.S939W) |
| **MDPL syndrome** (mandibular hypoplasia, deafness, progeroid, lipodystrophy) | #615381 | **AD** | recurrent heterozygous **p.Ser605del** (polymerase active site) |
| Nonsyndromic sensorineural hearing loss | — | AR | p.Gly1100Arg + null p.Ser197Hisfs*54 (~33% residual polymerase activity; Oh 2020, PMID 31944473) |
| Colorectal cancer susceptibility 12 (CRCS12) | — | AD | **exonuclease-domain (proofreading)** variants |

**Modifier genes / epigenetics / chromosomal abnormalities.** No modifier genes, epigenetic mechanisms, or chromosomal abnormalities are established for IMD120 specifically. (In cancer contexts, *POLD1* expression is modulated by copy-number gain, promoter methylation, and miR-139-3p — PMID 35189839 — but these are tumor-biology findings, not IMD120 mechanisms.)

---

## Section 5 — Environmental Information

- **Environmental factors:** No toxin, radiation, pollution, or occupational exposure causes IMD120. It is a monogenic disorder.
- **Lifestyle factors:** Not applicable to disease causation.
- **Infectious agents:** Pathogens are **triggers/manifesting agents, not causes**. The characteristic organisms are **herpesviruses** (HSV — recurrent oral herpes; VZV — recurrent herpes zoster; molluscum contagiosum poxvirus) and **respiratory bacteria/viruses** driving recurrent pneumonia and bronchiectasis. The viral-susceptibility bias reflects the dependence of antiviral defense on robust T-cell clonal expansion.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **biallelic hypomorphic missense mutation in *POLD1*** (e.g., p.R1060C, or p.Q684H+p.S939W in cis) alters the p125 catalytic subunit of DNA polymerase delta. *(demonstrated)*
2. This **leads to** one of two biochemical lesions:
   - **Branch A (destabilization):** p.R1060C disrupts the intramolecular interaction between the POLD1 **CysB motif** and the catalytic domain, and between POLD1 and POLD2, **destabilizing the Polδ holoenzyme** and lowering steady-state levels of POLD1/POLD2/POLD3. *(demonstrated by molecular dynamics + cellular assays)*
   - **Branch B (catalytic reduction):** p.Q684H+p.S939W near the active site **reduces intrinsic polymerase catalytic activity** while leaving complex assembly intact. *(demonstrated; rescued by WT subunit overexpression)*
3. Both branches **result in** reduced functional Polδ output → **ineffective recruitment of Replication Factor C (RFC)** to initiate DNA replication and **reduced enzymatic polymerase activity**. *(demonstrated)*
4. This **leads to** a **decreased fraction of cells entering/progressing through the cell cycle** (S-phase DNA synthesis defect) — i.e., **replicative stress**. *(demonstrated; DNA repair after genotoxic stress was normal, indicating a specific mitotic/S-phase synthesis defect)*
5. Replicative stress **selectively impairs the proliferation of rapidly dividing lymphocytes**. Upon TCR activation, patient T cells show **reduced proliferative responses** coupled to **decreased cell-cycle progression**. *(demonstrated)*
6. Impaired clonal expansion **results in** **T-cell lymphopenia**, loss of naive CD4/CD8 T cells, skewing toward effector-memory subsets, **oligoclonality**, and **restricted TCR-β V-J pairing** (a contracted repertoire). *(demonstrated)*
7. The compromised T-cell compartment **leads to** impaired T-cell help and antiviral immunity → **recurrent, especially herpetic/viral, infections**, and, via defective T-dependent B-cell help, **hypogammaglobulinemia and impaired vaccine antibody responses** (B-cell intrinsic proliferation is comparatively spared). *(demonstrated)*
8. In parallel (branch), the housekeeping requirement for Polδ in all dividing tissues **contributes to** **syndromic features** — short stature, intellectual disability/developmental delay, hearing loss — reflecting replicative stress beyond the immune system. *(inferred from phenotype; tissue-level mechanism not directly demonstrated)*

```
POLD1 biallelic hypomorphic missense
        │
        ├── Branch A: CysB/POLD2 interface disruption ─► holoenzyme destabilized (↓POLD1/2/3)
        │                                                        │
        └── Branch B: active-site substitution ─► ↓ catalytic activity (complex intact)
                                                                 │
                                        ▼  (convergence)  ▼
                              Reduced functional Polδ output
                                          │
                              Ineffective RFC recruitment / ↓ replication initiation
                                          │
                              S-phase DNA-synthesis defect  →  REPLICATIVE STRESS
                                          │
                   ┌──────────────────────┴───────────────────────┐
                   ▼                                               ▼
        Impaired T-cell clonal proliferation           Replicative stress in other
        (↓cell-cycle progression on TCR activation)     dividing tissues (inferred)
                   │                                               │
        T-cell lymphopenia; naive→EM skewing;            Short stature, ID/dev delay,
        oligoclonality; restricted TCR-β repertoire      hearing loss (syndromic subset)
                   │
        Impaired antiviral immunity + defective T-help
                   │
        Recurrent herpetic/viral & respiratory infections;
        hypogammaglobulinemia; poor vaccine responses
```

### Checklist of mechanistic categories

- **Molecular pathways:** DNA replication (leading/lagging-strand synthesis by Polδ), replication-initiation licensing via RFC/PCNA clamp loading, cell-cycle (G1→S→M) progression, DNA-damage/replication-stress response.
- **Cellular processes:** Cell-cycle progression and clonal proliferation (GO:0007049 cell cycle; GO:0006260 DNA replication; GO:0042098 T cell proliferation). The primary defect is proliferation, not apoptosis or repair per se (DNA repair after genotoxic stress was normal).
- **Protein dysfunction:** Holoenzyme destabilization (branch A) vs. reduced catalytic turnover (branch B) — both **partial loss of function** of Polδ.
- **Metabolic changes:** None specific; the lesion is in nucleic-acid synthesis machinery, not intermediary metabolism.
- **Immune system involvement:** Combined immunodeficiency — cell-intrinsic T-cell proliferation defect with secondary humoral impairment (GO:0002250 adaptive immune response; GO:0046631 alpha-beta T cell activation).
- **Tissue damage mechanisms:** Structural lung damage (bronchiectasis) is infection-driven, not a primary Polδ lesion.
- **Biochemical abnormalities:** Reduced DNA polymerase δ enzymatic activity; impaired RFC clamp-loader recruitment.
- **Molecular profiling:** Patient PBMCs/HEK293 cells showed reduced POLD-subunit expression, impaired complex stability, reduced cell-cycle fraction, and reduced polymerase activity (Cui 2020). No dedicated transcriptomic/proteomic/metabolomic IMD120 datasets exist.

**Upstream vs downstream.** *Upstream:* the *POLD1* mutation and Polδ hypofunction (initiating lesion). *Midstream:* impaired replication initiation and replicative stress. *Downstream:* the T-cell proliferation defect and its immunologic/clinical sequelae.

**Cell types (CL) and processes (GO):** CL:0000084 (T cell), CL:0000624 (CD4+ T cell), CL:0000625 (CD8+ T cell), CL:0000898 (naive T cell), CL:0000909 (effector memory T cell), CL:0000236 (B cell), CL:0000623 (NK cell). GO:0006260 (DNA replication), GO:0007049 (cell cycle), GO:0042098 (T cell proliferation), GO:0000731 (DNA synthesis involved in DNA repair — spared).

---

## Section 7 — Anatomical Structures Affected

- **Primary system:** **Immune / hematolymphoid system** (UBERON:0002405 immune system; UBERON:0000178 blood). The functional lesion is in the **T-lymphocyte compartment**, with secondary humoral (B-cell/immunoglobulin) impairment.
- **Primary lymphoid organs:** thymus (UBERON:0002370) and bone marrow (UBERON:0002371) as sites of lymphocyte production; peripheral lymphoid tissue (lymph nodes UBERON:0000029, spleen UBERON:0002106).
- **Secondary organ involvement (complications):**
  - **Respiratory tract / lungs** (UBERON:0002048) — recurrent infections leading to **bronchiectasis** (irreversible airway dilation).
  - **Skin** (UBERON:0002097) — molluscum contagiosum, recurrent abscesses, herpetic lesions.
  - **Ear / cochlea** (UBERON:0001690 / UBERON:0001844) — sensorineural hearing loss (syndromic subset).
  - **Central nervous system / brain** (UBERON:0000955) — intellectual disability, speech delay (syndromic subset).
  - **Skeletal/growth axis** — short stature.
- **Tissue/cell level:** hematopoietic/lymphoid cells; epithelial injury (airway) is secondary to infection. Targeted cell populations: naive CD4+/CD8+ T cells (depleted), effector-memory T cells (relatively expanded), B cells and NK cells (reduced in the Conde family).
- **Subcellular level:** **Nucleus** (GO:0005634) — site of DNA replication; specifically the **DNA polymerase delta complex** (GO:0043625) and replication fork machinery (GO:0005657 replication fork).
- **Lateralization:** Not applicable — systemic/bilateral immune and developmental involvement.

---

## Section 8 — Temporal Development

- **Onset:** **Early childhood / infancy.** Respiratory infections began in infancy in the Conde family (bronchiectasis by 6 months); recurrent herpetic infections and T-cell lymphopenia manifest in childhood.
- **Onset pattern:** Insidious/chronic — recurrent infections accumulating over time, punctuated by acute infectious episodes.
- **Progression:** Chronic and **lifelong**. Without treatment, recurrent infections drive **progressive, cumulative organ damage** (notably bronchiectasis, which is irreversible). Syndromic/developmental features (short stature, intellectual disability, hearing loss) are static-to-slowly-evolving developmental deficits.
- **Disease course:** Persistent immunodeficiency with **episodic** infectious exacerbations (e.g., oral herpes every 1–2 months in the index patient) superimposed on a chronic baseline.
- **Remission:** No spontaneous remission. **Treatment-induced control** is achievable — IgRT resolves lower respiratory tract infections and markedly reduces herpetic episodes; HSCT can be **curative** for the immune defect.
- **Critical periods:** Early diagnosis (before irreversible bronchiectasis and before severe infections) is the key window for intervention — paralleling the rationale for early treatment in other T-cell immunodeficiencies/SCID.

---

## Section 9 — Inheritance and Population

- **Inheritance:** **Autosomal recessive** (biallelic — homozygous or compound heterozygous). Heterozygous carriers are unaffected for IMD120.
- **Epidemiology:** **Ultra-rare.** Only **two unrelated *POLD1* families** are reported to date (Cui 2020; Conde 2019). No prevalence or incidence estimates exist; the true frequency is likely **<1 per 1,000,000**.
- **Penetrance / expressivity:** Presumed high penetrance for the immunodeficiency in biallelic carriers, but with **variable expressivity** — the two reported families differ in the prominence of syndromic features (the Conde family had prominent developmental impairment; the Cui family emphasized the immune/herpetic phenotype). With only two families, penetrance/expressivity cannot be precisely quantified.
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not reported.
- **Consanguinity:** **Major role.** The index kindred was consanguineous Turkish; the related *POLD2* patient was also consanguineous. Consanguinity is the principal route to homozygosity for rare hypomorphic recessive alleles.
- **Founder effects / carrier frequency:** None established; p.R1060C is absent from population databases, arguing against a common founder allele.
- **Population demographics:** Reported patients are of Turkish and (Conde family) unspecified ancestry. No sex bias expected (autosomal). Age distribution: pediatric onset.
- **Geographic distribution:** No endemic pattern; cases are sporadic and consanguinity-associated.

---

## Section 10 — Diagnostics

**Laboratory / immunologic tests (diagnostic hallmarks):**
- **Lymphocyte subset enumeration (flow cytometry):** T-cell lymphopenia with **decreased naive CD4+ and especially CD8+ T cells**, effector-memory skewing; reduced B and NK cells in some patients. (LOINC/flow-cytometry immunophenotyping.)
- **T-cell proliferation assay:** **Impaired T-cell (not B-cell) proliferation** to TCR/mitogen stimulation — the single most discriminating functional test.
- **Immunoglobulins:** low IgG, low IgA/IgM (hypogammaglobulinemia).
- **Vaccine response:** absent/poor tetanus antibody response despite full vaccination.
- **TCR repertoire analysis:** oligoclonality and restricted TCR-β V-J pairing (spectratyping/TCR-seq).
- **Cell-cycle / replicative-stress assays (research):** decreased S-phase fraction; reduced Polδ complex levels and polymerase activity.

**Genetic testing (definitive):**
- **Whole exome sequencing (WES) / whole genome sequencing (WGS):** the primary route to diagnosis — both families were identified by exome-scale sequencing. Given phenotypic overlap with many inborn errors of immunity, broad sequencing (WES/WGS) or a **combined immunodeficiency / IEI gene panel including *POLD1*** is the recommended approach.
- **Targeted *POLD1* sequencing / segregation analysis** to confirm biallelic status and phase (important for compound heterozygotes; note the in-cis p.Q684H+p.S939W configuration in Conde patient 2).
- **Functional confirmation** (polymerase activity, complex stability) supports variant interpretation, especially for VUS. The **PolED database** (PMID 41263451) curates functional evidence for *POLD1* variants and is a useful clinical resource.

**Imaging:** High-resolution chest CT to detect/monitor **bronchiectasis** and pulmonary sequelae; audiometry for hearing loss.

**Newborn screening:** Standard TREC-based SCID newborn screening detects severe T-cell lymphopenia and **may flag** IMD120 as a non-SCID T-cell-lymphopenia condition (analogous to syndromic T-cell lymphopenias identified through SCID NBS programs), but IMD120 is not a specific NBS target.

**Differential diagnosis:** SCID and leaky-SCID, other combined immunodeficiencies (e.g., MHC class II deficiency, FADD deficiency), DNA-repair/replication syndromes, and — for the syndromic features — other progeroid/short-stature syndromes. The distinguishing features of IMD120 are the **isolated T-cell proliferation defect with preserved B-cell proliferation**, the herpesvirus susceptibility, and biallelic *POLD1* variants. Because *POLD1* also causes MDPL (AD progeroid) and hearing loss, allele class and zygosity distinguish these entities.

---

## Section 11 — Outcome / Prognosis

- **Survival / mortality:** No formal survival statistics exist (only two families). Prognosis is dominated by **infection control** and **cumulative organ damage** (bronchiectasis). With effective IgRT and antiviral prophylaxis, patients can be stabilized; HSCT offers potential cure.
- **Morbidity / disability:** Significant — recurrent infections, irreversible bronchiectasis, lifelong treatment dependence, and (syndromic subset) intellectual disability, hearing loss, and short stature.
- **Complications:** Bronchiectasis and chronic lung disease; recurrent/severe herpetic disease; chronic viral skin lesions (molluscum); potential end-organ damage from recurrent infection.
- **Recovery potential:** The immune defect is not self-correcting; **HSCT can restore T-cell numbers and function** (Keles 2026). Established structural damage (e.g., bronchiectasis) and developmental deficits are not reversible.
- **Prognostic factors:** Timing of diagnosis and treatment initiation, degree of pre-existing organ damage, infection burden, and access to HSCT are the key determinants. There are no validated molecular prognostic biomarkers.
- **Theoretical long-term concern:** Because Polδ participates in genome maintenance, a **long-term genome-instability/malignancy risk** is biologically plausible; however, unlike the *POLD1* exonuclease (proofreading) variants that cause cancer predisposition, IMD120 variants primarily reduce polymerase output rather than abolish proofreading, and no cancer excess has been reported in the two families. This remains an open question requiring long-term follow-up.

---

## Section 12 — Treatment

**Established/effective management (from Cui 2020, verified):**
- **Immunoglobulin replacement therapy (IgRT)** (NCIT: Immunoglobulin Therapy) — the index patient started IgRT with **resolution of lower respiratory tract infections and markedly decreased herpetic infections**. Standard of care for the antibody deficiency.
- **Antiviral prophylaxis with acyclovir** (NCIT: Acyclovir) — used for recurrent oral herpes and herpes zoster; addresses the characteristic herpesvirus susceptibility.
- **Antimicrobial prophylaxis / prompt treatment of infections** and airway clearance/management for bronchiectasis (supportive).

**Curative therapy:**
- **Hematopoietic stem cell transplantation (HSCT)** (NCIT: Hematopoietic Stem Cell Transplantation). Keles et al. 2026 ([PMID: 42104577](https://pubmed.ncbi.nlm.nih.gov/42104577/)) reported the **first successful HSCT** in an 18-year-old IgRT-dependent woman with POLD1 deficiency: matched related donor, **reduced-intensity conditioning** (cyclophosphamide, fludarabine, ATG), tacrolimus + low-dose methotrexate GVHD prophylaxis; **prompt engraftment without major complications, improved T-cell counts/function, and she remained well off IgRT**. Reduced-intensity conditioning is a rational choice given theoretical DNA-replication/repair toxicity concerns in a Polδ-deficient host.

**Advanced / experimental therapeutics:** No gene therapy, RNA-based therapy, or *POLD1*-targeted therapy exists for IMD120. No IMD120-specific clinical trials (NCT) were identified. Gene therapy is conceptually challenging because *POLD1* is a tightly dosage-controlled housekeeping gene.

**Pharmacogenomics:** No IMD120-specific pharmacogenomic guidance. General caution is warranted with genotoxic/antimetabolite chemotherapeutics and conditioning agents given the underlying replication defect.

**Treatment strategy summary:**

| Line | Intervention | Goal | Evidence |
|---|---|---|---|
| Supportive/first-line | IgRT + acyclovir prophylaxis; treat infections; airway care | Control infections, prevent organ damage | Cui 2020 (PMID 31629014) |
| Definitive/curative | Reduced-intensity-conditioning HSCT | Restore T-cell immunity, off IgRT | Keles 2026 (PMID 42104577) |

---

## Section 13 — Prevention

- **Primary prevention:** Not preventable at the individual level (monogenic). **Genetic counseling** and, in consanguineous families, **carrier/cascade testing** and reproductive options (prenatal diagnosis, preimplantation genetic testing) are the principal preventive tools once a familial *POLD1* genotype is known.
- **Secondary prevention (early detection):** Early recognition via IEI evaluation and genetic testing; TREC-based SCID newborn screening may incidentally flag T-cell lymphopenia. Early diagnosis enables IgRT/antiviral prophylaxis before irreversible lung damage.
- **Tertiary prevention (complication prevention):** IgRT and antiviral/antimicrobial prophylaxis to prevent recurrent infection and bronchiectasis progression; audiologic and developmental support in syndromic patients; consideration of HSCT before accumulation of end-organ damage.
- **Immunization:** Routine inactivated vaccines are appropriate, but **antibody responses are impaired** (poor tetanus response reported); **live vaccines are contraindicated** in significant T-cell immunodeficiency. IgRT provides passive protection.
- **Counseling:** Autosomal recessive counseling — 25% recurrence risk for unaffected carrier couples; emphasize consanguinity risk.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy / orthologs:** *POLD1* is deeply evolutionarily conserved. Orthologs: mouse *Pold1* (NCBI Gene 18971), and homologs across vertebrates and yeast (*S. cerevisiae POL3/CDC2*). The catalytic and proofreading functions are conserved from yeast to human.
- **Natural disease in other species:** No naturally occurring *POLD1*-associated combined immunodeficiency has been reported in companion animals or wildlife (no OMIA entry identified for an equivalent immune phenotype).
- **Comparative biology:** The essentiality of Polδ for replication is conserved across all eukaryotes; the disease mechanism (replicative stress from Polδ hypofunction) is expected to be conserved, but the specific immune phenotype has only been characterized in humans.
- **Transmission / zoonosis:** Not applicable — genetic, non-transmissible disorder.

---

## Section 15 — Model Organisms

**No dedicated immunodeficiency model of IMD120 exists.** Existing *Pold1* mouse models bracket the disease but do not reproduce it:

| Model | Genotype | Phenotype | Relevance to IMD120 |
|---|---|---|---|
| *Pold1* null | *Pold1⁻/⁻* | **Peri-implantation embryonic lethality**; defective inner-cell-mass proliferation, impaired DNA synthesis, spontaneous apoptosis (Uchimura PLoS ONE 2009; MGI:3833589) | Confirms *POLD1* is **essential** — explains why only hypomorphic alleles cause human disease |
| Proofreading-dead | *Pold1^D400A/D400A* | Viable, fertile; **~15× higher mutation rate**, **~94% cancer incidence by 18 mo** (median survival ~10 mo), mostly epithelial carcinomas incl. skin SCC (Goldsby 2001/2002; Venkatesan PNAS 2007) | Models the **cancer** (exonuclease/CRCS12) phenotype, **not** IMD120 |
| Polymerase-domain point mutants | *Pold1^L604K/L604G* | **Embryonic lethal** | Illustrates lethality of strong polymerase-domain lesions |
| Hypomorphic allele | *Pold1* hypomorph | Disrupted gastrulation embryo-size/morphogenesis coordination (Biology Open 2022) | Demonstrates dosage-sensitive developmental effects; closest to "partial LOF" but not immune-focused |

**Implications / limitations.** The essentiality of *Pold1* (null = embryonic lethal) means an IMD120 model must use a **precisely hypomorphic allele** (e.g., a knock-in of the human p.R1060C-equivalent residue) to survive to immune-competence and reveal the T-cell phenotype. No such immune-focused model has been generated. Available models capture either **lethality** (null/strong point mutants) or **cancer** (proofreading-dead), leaving the **replicative-stress T-cell defect** experimentally uncharacterized in vivo. **iPSC-derived and CRISPR-edited cellular models** (as used for other immuno-actinopathies) plus patient PBMCs/HEK293 systems (Cui 2020) currently carry the mechanistic evidence.

**Recommended model resources:** MGI (mouse *Pold1*), IMPC/IMSR for allele availability; patient-derived iPSC → T-cell differentiation and CRISPR knock-in of hypomorphic alleles for immune-phenotype modeling.

---

## Key Findings (with statistical/experimental evidence)

### Finding 1 — POLD1 is the causal gene; IMD120 is an autosomal recessive combined immunodeficiency
Biallelic (homozygous or compound heterozygous) *POLD1* mutations cause IMD120 (OMIM #620836; MONDO:0970994). Cui et al. 2020 identified homozygous c.3178C>T (p.R1060C) in **3 related subjects** from a consanguineous Turkish kindred; Conde et al. 2019 identified compound-heterozygous *POLD1* variants. Verified quotes ([PMID: 31629014](https://pubmed.ncbi.nlm.nih.gov/31629014/)): *"We identified a missense mutation (c.3178C>T; p.R1060C) in POLD1 in 3 related subjects who presented with recurrent, especially herpetic, infections and T-cell lymphopenia with impaired T-cell but not B-cell proliferation,"* and *"These results identify gene defects in POLD1 as a novel cause of T-cell immunodeficiency."*

### Finding 2 — Clinical spectrum: infections + T-cell lymphopenia + syndromic features
Early-onset recurrent (especially herpetic/viral) infections, T-cell lymphopenia (↓naive CD4/CD8, effector-memory skewing, oligoclonality, restricted TCR-β repertoire), hypogammaglobulinemia, recurrent respiratory infections → bronchiectasis (by 6 months in Conde family), chronic molluscum, skin abscesses, and syndromic features (short stature, intellectual disability/speech delay, hearing loss). Verified quote ([PMID: 31629014](https://pubmed.ncbi.nlm.nih.gov/31629014/)): *"The patients exhibited decreased numbers of naive CD4 and especially CD8 T cells in favor of effector memory subpopulations."*

### Finding 3 — Mechanism: Polδ hypofunction → replicative stress → T-cell proliferation defect
Hypomorphic *POLD1* variants destabilize the Polδ complex, impair RFC recruitment and cell-cycle progression, causing replicative stress and defective T-cell proliferation. Verified quotes ([PMID: 31629014](https://pubmed.ncbi.nlm.nih.gov/31629014/)): *"The mutation destabilizes the Polδ complex, leading to ineffective recruitment of replication factor C to initiate DNA replication,"* and *"Molecular dynamics simulation revealed that the R1060C mutation disrupts the intramolecular interaction between the POLD1 CysB motif and the catalytic domain and also between POLD1 and the Polδ subunit POLD2."* Conde 2019 termed it a *"syndromic immunodeficiency with replicative stress"* with normal post-genotoxic DNA repair — i.e., a specific S-phase synthesis defect.

### Finding 4 — Two convergent molecular routes to Polδ hypofunction
(a) **Destabilization** — p.R1060C in the CysB motif lowers POLD1/POLD2/POLD3 levels (complex instability). (b) **Reduced catalytic activity with intact assembly** — p.Q684H+p.S939W (in cis, near the active site) reduce intrinsic polymerase activity without destabilizing the complex. Both are biallelic and converge on reduced functional Polδ output.

### Finding 5 — Model organisms: no immune model; null lethal, proofreading-dead cancer-prone
*Pold1⁻/⁻* mice are peri-implantation lethal (essential gene); *Pold1^D400A^* proofreading-dead mice are viable but ~94% cancer-prone. Neither models the IMD120 immune phenotype.

### Finding 6 — Management: IgRT + acyclovir effective; RIC-HSCT feasible/curative
IgRT resolved lower respiratory infections and markedly reduced herpetic episodes; acyclovir controlled recurrent herpes (Cui 2020). Keles 2026 (PMID 42104577) reported the first successful reduced-intensity-conditioning HSCT with engraftment, restored T-cell function, and independence from IgRT.

### Finding 7 — Inheritance/epidemiology and the POLD1 allelic series
Ultra-rare AR disorder, consanguinity-associated, ~2 families reported; allelic to AD MDPL syndrome (p.Ser605del), AR nonsyndromic hearing loss (p.Gly1100Arg + null; ~33% residual activity, PMID 31944473), and colorectal cancer susceptibility 12 (exonuclease-domain variants).

---

## Mechanistic Model / Interpretation

IMD120 is best understood as a **dosage disease of a housekeeping replicase**. *POLD1* is essential and dosage-sensitive: null alleles are lethal, so only **partial loss-of-function** genotypes produce viable, disease-manifesting individuals. The unifying pathophysiology is **replicative stress** — a quantitative shortfall in DNA-synthesis capacity that becomes limiting precisely in the cells that must proliferate fastest and most explosively: **antigen-activated T lymphocytes**. This explains the otherwise puzzling selectivity of the phenotype (T-cell proliferation impaired, B-cell proliferation relatively spared; antiviral immunity most affected) and the herpesvirus susceptibility (control of herpesviruses is exquisitely T-cell dependent).

The convergence of two biochemically distinct genotypes (complex destabilization vs. reduced catalytic activity) on the **same functional endpoint** (reduced Polδ output → replicative stress) is a strong argument that **quantitative Polδ activity, not any single structural interaction, is the disease-relevant variable**. It also predicts a **genotype–severity gradient**: the more residual Polδ activity an allele combination retains, the milder (or more tissue-restricted) the phenotype — a prediction consistent with the broader *POLD1* allelic series, where different residual-activity/allele-class combinations yield hearing loss, progeroid MDPL, cancer predisposition, or combined immunodeficiency.

---

## Evidence Base

| PMID | Title (abbrev.) | Role |
|---|---|---|
| [31629014](https://pubmed.ncbi.nlm.nih.gov/31629014/) | *Combined immunodeficiency caused by a loss-of-function mutation in DNA polymerase delta 1* (Cui 2020) | **Founding paper**: identifies POLD1, p.R1060C, clinical/immune phenotype, and the destabilization/RFC mechanism |
| 31449058 | Conde et al. 2019 (POLD1/POLD2 replicative-stress immunodeficiency) | Second family; compound-het POLD1 (p.Q684H+p.S939W) and POLD2 patient; defines "replicative stress," branch B mechanism |
| [42104577](https://pubmed.ncbi.nlm.nih.gov/42104577/) | Keles et al. 2026 (Pediatric Transplantation) | First successful RIC-HSCT in POLD1 deficiency; curative option |
| [31944473](https://pubmed.ncbi.nlm.nih.gov/31944473/) | Oh et al. 2020 | AR nonsyndromic hearing loss from POLD1; ~33% residual activity — supports dosage/allelic-series model |
| [41263451](https://pubmed.ncbi.nlm.nih.gov/41263451/) | *PolED database* | Curated functional-variant resource for POLD1/POLE interpretation |
| [34594041](https://pubmed.ncbi.nlm.nih.gov/34594041/) | Robinson et al. 2021 | Germline POLE/POLD1 (proofreading) mutations: mutation burden, cancer — contrasts IMD120 (non-proofreading, no premature aging) |
| Mouse models | Uchimura 2009 (MGI:3833589); Goldsby 2001/2002; Venkatesan 2007 (PNAS); Biology Open 2022 | Establish Pold1 essentiality (null lethal) and proofreading-dead cancer phenotype; absence of an immune model |

Additional MDPL papers (PMIDs 41219970, 41083899, 39611849, 41742372, 42488286) establish that the **p.Ser605del active-site allele** causes the *dominant* progeroid MDPL phenotype via gain-of-abnormal-interaction (e.g., aberrant TRF1 binding) and telomere/PARP1 dysregulation — mechanistically and inheritance-wise distinct from the *recessive hypomorphic* IMD120 alleles, reinforcing that **allele class dictates phenotype** at this locus.

---

## Limitations and Knowledge Gaps

1. **Extremely small sample:** Only **two unrelated families** define IMD120. Penetrance, expressivity, full phenotypic spectrum, natural history, prognosis, and genotype–phenotype correlations are all under-determined.
2. **No epidemiologic data:** No prevalence/incidence estimates; no registry; no defined Orphanet/ICD code.
3. **No in vivo immune model:** The T-cell replicative-stress mechanism has not been reproduced in an animal model; a hypomorphic knock-in mouse is needed.
4. **Syndromic-feature mechanism inferred, not demonstrated:** The link from Polδ hypofunction to short stature/ID/hearing loss is a plausible housekeeping-replicative-stress inference but is not experimentally dissected.
5. **Long-term cancer/genome-instability risk unknown:** Whether IMD120 patients carry elevated malignancy risk (as proofreading-defective *POLD1* carriers do) is unresolved; the mechanism differs (reduced synthesis vs. lost proofreading), but long-term follow-up is lacking.
6. **HSCT evidence is a single case:** Curative HSCT is supported by one patient; optimal conditioning intensity and long-term outcomes (including any excess conditioning toxicity from the replication defect) are unknown.
7. **B-cell/NK involvement variability:** B-cell and NK reductions were prominent in one family but the "T-cell selective" framing derives largely from the other — the true combined-immunodeficiency breadth needs more cases.

---

## Proposed Follow-up Experiments / Actions

1. **Build a hypomorphic *Pold1* knock-in mouse** (e.g., p.R1060C-equivalent) to test whether it recapitulates T-cell lymphopenia, proliferation defect, and infection susceptibility — the missing in vivo model.
2. **Patient/CRISPR iPSC → T-cell differentiation** to quantify replicative stress, cell-cycle kinetics, and repertoire contraction cell-autonomously, and to test allele-specific severity (branch A vs. branch B).
3. **Genotype–activity–phenotype mapping** across the *POLD1* allelic series: measure residual polymerase activity for IMD120 vs. hearing-loss vs. MDPL vs. cancer alleles and correlate with tissue-specific phenotype to formalize the dosage model (leverage the PolED database, PMID 41263451).
4. **International case-finding/registry:** Systematically re-examine unexplained combined immunodeficiency and SCID-NBS-positive T-cell-lymphopenia cohorts for biallelic *POLD1* variants to expand the phenotypic spectrum and estimate frequency.
5. **Long-term surveillance protocol:** Prospectively monitor IMD120 patients for malignancy, somatic mutation burden, and organ damage to resolve the genome-instability question.
6. **HSCT outcome collation:** Aggregate additional transplant cases to define optimal (reduced-intensity) conditioning and long-term efficacy/safety.
7. **Deep immunophenotyping + TCR-seq** on any newly identified patients to precisely quantify the naive-cell loss, effector-memory skewing, and repertoire restriction, and to test whether B-cell/NK involvement is consistent.

---

## Ontology Term Appendix

- **Disease:** MONDO:0970994; OMIM #620836
- **Gene/protein:** *POLD1* (HGNC:9175); GO:0043625 (delta DNA polymerase complex); GO:0006260 (DNA replication); GO:0007049 (cell cycle); GO:0042098 (T cell proliferation); GO:0005634 (nucleus)
- **Cells (CL):** CL:0000084 (T cell), CL:0000624 (CD4+ T cell), CL:0000625 (CD8+ T cell), CL:0000898 (naive T cell), CL:0000909 (effector memory T cell), CL:0000236 (B cell), CL:0000623 (NK cell)
- **Anatomy (UBERON):** UBERON:0002405 (immune system), UBERON:0002370 (thymus), UBERON:0002371 (bone marrow), UBERON:0002048 (lung), UBERON:0002097 (skin), UBERON:0001690 (ear)
- **Phenotypes (HPO):** HP:0002719, HP:0004429, HP:0002326, HP:0005403, HP:0031381, HP:0004313, HP:0002110, HP:0004322, HP:0001249, HP:0000407
- **Treatments (NCIT):** Immunoglobulin therapy; Acyclovir; Hematopoietic Stem Cell Transplantation
- **Chemicals (CHEBI):** acyclovir (CHEBI:2453)

---

*Evidence source types: human clinical (case series — Cui 2020, Conde 2019; case report — Keles 2026); in vitro/cellular and in silico (patient PBMCs, HEK293, molecular dynamics — Cui 2020); model organism (mouse Pold1 — Uchimura 2009, Goldsby 2001/2002, Venkatesan 2007). All mechanistic and clinical claims are cited to primary literature by PMID.*


## Artifacts

- [OpenScientist final report](Immunodeficiency_120-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Immunodeficiency_120-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 51 |
| Resolved | 48 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 29 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 10 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0970994` (4 mentions) - the report calls it "MONDO"; MONDO calls it **immunodeficiency 120**
- `HP:0002326` (2 mentions) - the report calls it "Herpes simplex disease"; HP calls it **Transient ischemic attack**
- `HP:0200042` (1 mention) - the report calls it "Clinical sign"; HP calls it **Skin ulcer**
- `HP:0031521` (1 mention) - the report calls it "Clinical sign"; HP calls it **Vaginal clear cell adenocarcinoma**
- `HP:0005387` (1 mention) - the report calls it "Decreased antibody level in blood"; HP calls it **Combined immunodeficiency**
- `HP:0004322` (2 mentions) - the report calls it "Physical manifestation"; HP calls it **Short stature**
- `HP:0007018` (1 mention) - the report calls it "Behavioral"; HP calls it **Attention deficit hyperactivity disorder**
- `HP:0000407` (2 mentions) - the report calls it "Physical manifestation"; HP calls it **Sensorineural hearing impairment**
- `UBERON:0002048` (2 mentions) - the report calls it "Respiratory tract / lungs", "lung"; UBERON calls it **lung**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0410413` (1 mention) - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0031381` (2 mentions) - the report calls it "Decreased proliferation of T cells"; HP calls it **Decreased mitogen-induced T-cell proliferation**, and lists "Decreased lymphocyte proliferation in response to mitogen" among its other names
- `CL:0000624` (2 mentions) - the report calls it "CD4+ T cell"; CL calls it **CD4-positive, alpha-beta T cell**
- `CL:0000625` (2 mentions) - the report calls it "CD8+ T cell"; CL calls it **CD8-positive, alpha-beta T cell**
- `CL:0000909` (2 mentions) - the report calls it "effector memory T cell"; CL calls it **CD8-positive, alpha-beta memory T cell**
- `CL:0000623` (2 mentions) - the report calls it "NK cell"; CL calls it **natural killer cell**, and lists "NK cell" among its other names
- `GO:0000731` (1 mention) - the report calls it "DNA synthesis involved in DNA repair — spared"; GO calls it **DNA synthesis involved in DNA repair**
- `UBERON:0002370` (2 mentions) - the report calls it "Primary lymphoid organs:** thymus", "thymus"; UBERON calls it **thymus**, and lists "thymus organ" among its other names
- `UBERON:0002097` (2 mentions) - the report calls it "Skin", "skin"; UBERON calls it **skin of body**, and lists "skin" among its other names
- `UBERON:0000955` (1 mention) - the report calls it "Central nervous system / brain"; UBERON calls it **brain**, and lists "suprasegmental levels of nervous system" among its other names
- `GO:0005634` (2 mentions) - the report calls it "Nucleus", "Subcellular level:** **Nucleus", "nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HGNC:9175` - called "POLD1", "Gene/protein:** *POLD1"
- `UBERON:0002370` - called "Primary lymphoid organs:** thymus", "thymus"
- `UBERON:0002048` - called "Respiratory tract / lungs", "lung"
- `UBERON:0002097` - called "Skin", "skin"
- `GO:0005634` - called "Nucleus", "Subcellular level:** **Nucleus", "nucleus"
- `GO:0043625` - called "DNA polymerase delta complex", "delta DNA polymerase complex"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.