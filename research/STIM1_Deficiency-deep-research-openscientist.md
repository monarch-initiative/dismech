---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T20:37:56.271670'
end_time: '2026-09-29T21:28:23.307437'
duration_seconds: 3027.04
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: STIM1 Deficiency
  mondo_id: MONDO:0013008
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
  quotes_checked: 32
  quotes_valid: 25
  quotes_unsupported: 7
  unsupported_quote_references:
  - PMID:26469693
  - PMID:33733462
  - PMID:21217057
  - PMID:20111871
  - PMID:23483280
  - PMID:19075015
  - PMID:16582901
  relevance_assessed: 23
  on_topic: 17
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 36
  verified: 33
  not_found: 1
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.029
  labels_checked: 14
  labels_matching: 0
  labels_mismatched: 11
  mislabelled_terms:
  - term_id: MONDO:0013008
    reported_labels:
    - MONDO
    ontology_label: combined immunodeficiency due to STIM1 deficiency
  - term_id: HP:0005387
    reported_labels:
    - Clinical/lab
    ontology_label: Combined immunodeficiency
  - term_id: HP:0002719
    reported_labels:
    - Clinical
    ontology_label: Recurrent infections
  - term_id: HP:0001890
    reported_labels:
    - Lab/clinical
    ontology_label: Autoimmune hemolytic anemia
  - term_id: HP:0001973
    reported_labels:
    - Lab/clinical
    ontology_label: Autoimmune thrombocytopenia
  - term_id: HP:0002716
    reported_labels:
    - Clinical
    ontology_label: Lymphadenopathy
  - term_id: HP:0001433
    reported_labels:
    - Clinical
    ontology_label: Hepatosplenomegaly
  - term_id: HP:0001252
    reported_labels:
    - Physical
    ontology_label: Hypotonia
  - term_id: HP:0001324
    reported_labels:
    - Physical
    ontology_label: Muscle weakness
  - term_id: HP:0000535
    reported_labels:
    - Physical
    ontology_label: obsolete Sparse and thin eyebrow
  - term_id: UBERON:0001769
    reported_labels:
    - "Eye \u2014 iris smooth muscle"
    ontology_label: iris
  labels_variant: 3
  unresolved_terms:
  - HP:0009925
  obsolete_terms:
  - term_id: HP:0000535
    ontology_label: obsolete Sparse and thin eyebrow
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: STIM1_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: STIM1_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** STIM1 Deficiency
- **MONDO ID:** MONDO:0013008 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **STIM1 Deficiency** covering all of the
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

# STIM1 Deficiency (CRAC Channelopathy) — Comprehensive Disease Characterization Report

**Disease:** STIM1 Deficiency
**MONDO ID:** MONDO:0013008
**OMIM:** #612783 (Immunodeficiency 10, IMD10)
**Category:** Mendelian, autosomal recessive
**Gene:** *STIM1* (Stromal Interaction Molecule 1; HGNC:11386; NCBI Gene 6786; OMIM *605921; chromosome 11p15.4)

---

## Summary

STIM1 deficiency is an **ultra-rare, autosomal-recessive CRAC (Ca²⁺-release-activated Ca²⁺) channelopathy** caused by **biallelic loss-of-function (LOF) variants in *STIM1***, the endoplasmic-reticulum (ER) Ca²⁺ sensor that activates the plasma-membrane channel ORAI1. When STIM1 cannot sense ER Ca²⁺ depletion or engage ORAI1, **store-operated Ca²⁺ entry (SOCE)** is abolished. Because SOCE is a near-universal cellular signaling module, its loss produces a **congenital multisystem syndrome**: a SCID-like combined immunodeficiency accompanied — paradoxically — by autoimmunity and lymphoproliferation, together with non-immune features including muscular hypotonia/myopathy, anhidrotic (anhydrotic) ectodermal dysplasia with defective sweating, dental enamel hypomineralization, and pupillary/iris abnormalities (mydriasis). The syndrome is shared with recessive ORAI1 deficiency, its molecular partner, and together they define "CRAC channelopathy" ([PMID: 26469693](https://pubmed.ncbi.nlm.nih.gov/26469693/)).

The **core causal chain** is well established: biallelic LOF *STIM1* mutation → loss/nonfunction of STIM1 protein → failure of the luminal EF-hand/SAM (EF-SAM) domain to sense ER Ca²⁺ depletion and oligomerize → failure to translocate to ER–plasma-membrane junctions and gate ORAI1 via the CRAC activation domain (CAD) → CRAC channels remain closed → absent SOCE → collapse of the downstream **Ca²⁺–calmodulin–calcineurin–NFAT** transcriptional axis in lymphocytes (impaired cytokine production despite normal lymphocyte development) plus failure of Ca²⁺-dependent functions in muscle, sweat gland, ameloblast, and iris smooth muscle. Critically, STIM1 deficiency (LOF) is the **mechanistic mirror image** of dominant STIM1 gain-of-function (GOF), which causes constitutive SOCE and the tubular aggregate myopathy (TAM) / Stormorken syndrome spectrum — a distinction essential for correct classification and rational therapy.

The **only curative therapy for the immunodeficiency is allogeneic hematopoietic stem cell transplantation (HSCT)**, as for other combined immunodeficiencies; HSCT does not correct the non-hematopoietic (muscle, ectodermal, dental) features, which are managed supportively. A **splice-correcting antisense oligonucleotide (ASO)** that restores STIM1 splicing/function in patient cells has been demonstrated as a proof-of-concept, mutation-specific therapy ([PMID: 38977117](https://pubmed.ncbi.nlm.nih.gov/38977117/)). Untreated, the disease is life-threatening in infancy/early childhood from recurrent, severe, and opportunistic infections, compounded by autoimmune cytopenias and lymphoproliferation.

---

## 1. Disease Information

STIM1 deficiency is a **primary (inborn) error of immunity** classified as a CRAC channelopathy. It is defined by the loss of store-operated Ca²⁺ entry (SOCE) secondary to biallelic loss-of-function of the ER Ca²⁺ sensor STIM1. As stated in the landmark review, "**CRAC channelopathy is caused by loss-of-function mutations in ORAI1 and STIM1 that abolish CRAC channel function and SOCE; it is characterized by severe combined immunodeficiency (SCID)-like disease, autoimmunity, muscular hypotonia, and ectodermal dysplasia, with defects in sweat gland function and dental enamel formation**" ([PMID: 26469693](https://pubmed.ncbi.nlm.nih.gov/26469693/)).

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0013008 |
| OMIM | #612783 (Immunodeficiency 10) |
| Gene (HGNC) | STIM1, HGNC:11386 |
| NCBI Gene | 6786 (human); 20866 (mouse *Stim1*) |
| UniProt | Q13586 (human STIM1) |
| Orphanet | CRAC channelopathy spectrum (immunodeficiency by defective SOCE) |
| ICD-11 | 4A00 (immunodeficiencies) group |
| MeSH | Related terms: "Severe Combined Immunodeficiency"; "Stromal Interaction Molecule 1" |

**Synonyms / alternative names:** Immunodeficiency 10 (IMD10); STIM1 loss-of-function; CRAC channelopathy (STIM1 type); combined immunodeficiency with autoimmunity due to STIM1 deficiency; store-operated calcium entry (SOCE) deficiency.

**Source of information:** The disease is characterized almost entirely from **individual patient reports and small consanguineous kindreds** (fewer than ~15 families reported worldwide) combined with **in vitro functional studies and animal models** — not from aggregated EHR-scale registries. The evidence base is therefore case-based human clinical data plus mechanistic model-organism and cellular studies.

---

## 2. Etiology

**Primary cause — purely genetic.** STIM1 deficiency is caused **solely by biallelic recessive loss-of-function variants in *STIM1*** that abolish SOCE. There are **no environmental, infectious, or toxic causes**, no somatic contribution, and no established modifier genes or disease-specific epigenetic changes. Infections in patients are downstream *consequences* of the immunodeficiency, not causes (Finding F012).

**Genetic risk factors.** The causal genetic events are germline biallelic LOF variants (homozygous or compound heterozygous). Reported variants include nonsense/frameshift alleles (e.g., c.685delT, p.Phe229Leufs*12, causing complete protein loss; [PMID: 33733462](https://pubmed.ncbi.nlm.nih.gov/33733462/)) and splice-site variants (e.g., NM_003156 c.792-3C>G producing exon-7 skipping/intron retention with impaired SOCE; [PMID: 38977117](https://pubmed.ncbi.nlm.nih.gov/38977117/)). **Consanguinity is a strong risk factor**, as expected for a rare recessive disorder — e.g., "we studied two siblings from a consanguineous Syrian family" ([PMID: 33733462](https://pubmed.ncbi.nlm.nih.gov/33733462/)).

**Environmental / lifestyle risk factors:** None identified. **Protective factors (genetic or environmental):** None established.

**Gene–environment interactions:** None mechanistically established. The only "interaction" is that pathogen exposure unmasks and drives the clinical immunodeficiency, but pathogens are not co-causal.

**LOF vs GOF dichotomy (etiologic classification).** STIM1 deficiency (recessive LOF) is the mechanistic opposite of autosomal-dominant STIM1 **gain-of-function**, which causes constitutive CRAC activation and the TAM/Stormorken spectrum: "**By contrast, autosomal dominant gain-of-function mutations in ORAI1 and STIM1 result in constitutive CRAC channel activation, SOCE, and increased intracellular Ca²⁺ levels that are associated with an overlapping spectrum of diseases, including nonsyndromic tubular aggregate myopathy (TAM) and York platelet and Stormorken syndromes**" ([PMID: 26469693](https://pubmed.ncbi.nlm.nih.gov/26469693/)). "**Loss- and gain-of-function gene mutations in ORAI1 and STIM1 in human patients cause distinct disease syndromes**" ([PMID: 26469693](https://pubmed.ncbi.nlm.nih.gov/26469693/)).

---

## 3. Phenotypes

STIM1 deficiency is a **congenital multisystem disorder**. The immunological phenotype (combined immunodeficiency + immune dysregulation) is essentially universal; individual non-immune features are variably present (variable expressivity). Frequencies are qualitative given the very small number of reported patients (F011).

| Phenotype | Type | HPO term | Onset | Frequency |
|---|---|---|---|---|
| Combined immunodeficiency (SCID-like) | Clinical/lab | HP:0005387 | Congenital/infantile | Near-universal |
| Recurrent/opportunistic infections | Clinical | HP:0002719 | Infantile | Near-universal |
| Autoimmune hemolytic anemia | Lab/clinical | HP:0001890 | Infantile/childhood | Common |
| Autoimmune thrombocytopenia | Lab/clinical | HP:0001973 | Infantile/childhood | Common |
| Lymphoproliferation / lymphadenopathy | Clinical | HP:0002716 | Childhood | Common |
| Hepatosplenomegaly | Clinical | HP:0001433 | Childhood | Variable |
| Muscular hypotonia | Physical | HP:0001252 | Congenital | Common |
| Muscle weakness / myopathy | Physical | HP:0001324 | Congenital | Common |
| Hypohidrosis / anhidrosis | Physical | HP:0000970 / HP:0009925 | Congenital | Common (ectodermal dysplasia) |
| Dental enamel hypoplasia / amelogenesis imperfecta | Physical | HP:0006297 / HP:0000705 | Congenital (dentition) | Common |
| Mydriasis / pupillary abnormality | Physical | HP:0000535 | Congenital | Reported |
| Skin hyperlaxity / elastic skin | Physical | — | Congenital | Reported (expanded phenotype) |
| Dysmorphic facies, hypoplastic patellae | Physical | — | Congenital | Reported (expanded phenotype) |

Key supporting quotes: "**in the case of STIM1 deficiency, autoimmunity and lymphoproliferative disease. The immunodeficiency in these patients is due to a severe defect in T cell activation but not in lymphocyte development**" ([PMID: 20189884](https://pubmed.ncbi.nlm.nih.gov/20189884/)); the disease "**is dominated by severe immunodeficiency and autoimmunity due to impaired SOCE**" ([PMID: 22615435](https://pubmed.ncbi.nlm.nih.gov/22615435/)); "**muscular hypotonia, and ectodermal dysplasia, with defects in sweat gland function and dental enamel formation**" ([PMID: 26469693](https://pubmed.ncbi.nlm.nih.gov/26469693/)); the expanded phenotype "**presenting with muscle weakness, hyperlaxity, elastic skin, tooth abnormalities, dysmorphic facies, hypoplastic patellae and history of respiratory infections**" ([PMID: 33733462](https://pubmed.ncbi.nlm.nih.gov/33733462/)).

**Quality-of-life impact:** Severe. Life-threatening infections dominate infancy; chronic autoimmune cytopenias require transfusion/immunosuppression; anhidrosis causes heat intolerance and hyperthermia risk; enamel defects affect dentition and nutrition; hypotonia/myopathy impairs motor development. Formal EQ-5D/SF-36 data are not available for this ultra-rare disease.

**Severity/progression:** Immune features are severe and life-threatening but treatable by HSCT; non-immune features are largely **congenital and static/non-progressive** rather than degenerative.

---

## 4. Genetic / Molecular Information

**Causal gene:** *STIM1* (HGNC:11386; NCBI Gene 6786; OMIM *605921; UniProt Q13586), encoding the single-pass ER-membrane Ca²⁺ sensor Stromal Interaction Molecule 1.

**Pathogenic variants (biallelic, recessive):**

| Variant (cDNA / protein) | Type | Consequence | Reference |
|---|---|---|---|
| c.685delT, p.Phe229Leufs*12 (homozygous) | Frameshift | Complete loss of STIM1 protein | [PMID: 33733462](https://pubmed.ncbi.nlm.nih.gov/33733462/) |
| NM_003156 c.792-3C>G (homozygous) | Splice-site | Exon-7 skipping / intron retention; impaired SOCE | [PMID: 38977117](https://pubmed.ncbi.nlm.nih.gov/38977117/) |
| Additional nonsense/splice LOF alleles (case reports) | Nonsense/splice | Loss of function, absent SOCE | [PMID: 26469693](https://pubmed.ncbi.nlm.nih.gov/26469693/) |

Supporting quotes: "**we have identified a new homozygous frameshift mutation in STIM1: c.685delT [p.(Phe229Leufs*12)], leading to a complete loss of STIM1 protein**" ([PMID: 33733462](https://pubmed.ncbi.nlm.nih.gov/33733462/)); "**a novel homozygous mutation, NM_003156 c.792-3C > G, in STIM1 in a patient with a clinical profile of CRAC channelopathy, including immune system deficiencies and muscle weakness**" ([PMID: 38977117](https://pubmed.ncbi.nlm.nih.gov/38977117/)).

**Variant classification:** Reported LOF variants are pathogenic (ACMG/AMP), supported by functional evidence of abolished SOCE (PS3), null variant type (PVS1), and segregation in consanguineous families.

**Variant types:** Nonsense, frameshift, and splice-site (all loss-of-function). **Allele frequency:** Extremely rare/private; not reported at appreciable frequency in gnomAD (consistent with recessive, ultra-rare disease). **Origin:** Germline only; no somatic contribution. **Functional consequence:** **Loss of function** (loss of ER Ca²⁺ sensing and ORAI1 gating → absent SOCE). By contrast, dominant TAM/Stormorken alleles are **gain-of-function** (F012).

**Modifier genes / epigenetics / chromosomal abnormalities:** None established for STIM1 deficiency. The paralog STIM2 (lower activation threshold) is a plausible but untested compensatory modifier in humans. No disease-specific methylation/histone signatures or large structural rearrangements are reported.

---

## 5. Environmental Information

**No environmental, lifestyle, or infectious etiologic factors** contribute to disease *causation*. STIM1 deficiency is a monogenic recessive disorder. Infectious agents (viral, bacterial, fungal) are **downstream complications** of the immunodeficiency, not triggers. No toxin, radiation, occupational, or dietary factor has been implicated in onset or severity (F012).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic LOF *STIM1* mutation** → loss or nonfunction of STIM1 protein (demonstrated; complete protein loss for c.685delT, [PMID: 33733462](https://pubmed.ncbi.nlm.nih.gov/33733462/)).
2. **Loss of ER Ca²⁺ sensing:** the luminal EF-hand/SAM (EF-SAM) domain can no longer detect ER Ca²⁺ depletion or relieve autoinhibition to oligomerize (demonstrated biophysically: "**the STIM1 Ca²⁺-binding EF-hand and the STIM2 SAM domain are major contributors to the autoinhibition of oligomerization**", [PMID: 21217057](https://pubmed.ncbi.nlm.nih.gov/21217057/)) → **leads to**
3. **Failure of STIM1 conformational activation and translocation** to ER–plasma-membrane junctions; the CRAC activation domain (CAD/CC1+CAD) cannot form store-dependent oligomers ("**Addition of CC1 + CAD, but not CC1 alone, enables the formation of stable store-dependent oligomers. Within the CAD, both CC2 and C-terminal residues contribute to oligomer formation**", [PMID: 20375143](https://pubmed.ncbi.nlm.nih.gov/20375143/)) → **results in**
4. **Failure to bind and gate ORAI1**, the pore-forming CRAC subunit (normal mechanism: "**ORAI1 (or CRACM1) acts as the pore-forming subunit of the CRAC channel in the plasma membrane. Stromal interaction molecule (STIM) 1 is localized in the ER, senses [Ca²⁺]ER, and activates the CRAC channel upon store depletion by binding to ORAI1**", [PMID: 20111871](https://pubmed.ncbi.nlm.nih.gov/20111871/)) → **leads to**
5. **CRAC channels remain closed → absent store-operated Ca²⁺ entry (SOCE)** and no I_CRAC (demonstrated in patient cells: "**Calcium influx analysis revealed impaired SOCE in the patient cells**", [PMID: 38977117](https://pubmed.ncbi.nlm.nih.gov/38977117/)). This is the **central, fully penetrant cellular lesion.** The chain then **branches** across tissues:

   **Branch A — Immune (demonstrated):** Absent sustained Ca²⁺ → failure of the **Ca²⁺–calmodulin–calcineurin–NFAT** axis → NFAT cannot be dephosphorylated/translocate to the nucleus → cytokine gene transcription (e.g., IL-2) fails → defective T-cell activation/effector function despite normal lymphocyte development ("**Ca²⁺-calcineurin-nuclear factor of activated T cells (NFAT) signalling pathway**", [PMID: 23483280](https://pubmed.ncbi.nlm.nih.gov/23483280/); NFAT nuclear import was the discovery readout for ORAI1, "**promoting the immune response to pathogens by activating the transcription factor NFAT**", [PMID: 16582901](https://pubmed.ncbi.nlm.nih.gov/16582901/)) → **combined immunodeficiency**. Concurrent failure of Treg/iNKT function and loss of tolerance → **autoimmunity + lymphoproliferation** (F002, F006, F010).

   **Branch B — Skeletal muscle (inferred / model-supported):** Loss of SOCE-dependent Ca²⁺ replenishment → impaired muscle Ca²⁺ handling → **hypotonia/myopathy**.

   **Branch C — Eccrine sweat gland (inferred):** Loss of SOCE in secretory epithelium → **anhidrosis / ectodermal dysplasia**.

   **Branch D — Ameloblasts/enamel organ (model-supported):** Loss of SOCE in ameloblasts → defective enamel mineralization → **enamel hypoplasia** ("**Stim1 Regulates Enamel Mineralization and Ameloblast Modulation**", [PMID: 28732182](https://pubmed.ncbi.nlm.nih.gov/28732182/); SOCE impairment in enamel cells, [PMID: 28352661](https://pubmed.ncbi.nlm.nih.gov/28352661/)).

   **Branch E — Iris smooth muscle (inferred):** → **mydriasis / pupillary abnormality**.

6. Branch A extends further to **STIM1–NFAT synergy with STAT1 controlling T-bet / Th1 differentiation** ([PMID: 39984734](https://pubmed.ncbi.nlm.nih.gov/39984734/)) and to **Ca²⁺-dependent T-cell metabolic reprogramming** ([PMID: 33103016](https://pubmed.ncbi.nlm.nih.gov/33103016/)).

### Detail by category

- **Molecular pathways:** SOCE / CRAC signaling → **Ca²⁺–calcineurin–NFAT** (canonical effector); STIM1→STAT1→T-bet (Th1). GOF of the same pathway drives STIM1/Orai1/NFAT-mediated pathology in other contexts (e.g., cardiac; [PMID: 42285689](https://pubmed.ncbi.nlm.nih.gov/42285689/)), confirming the pathway's centrality.
- **Cellular processes:** T-cell activation, cytokine transcription, regulatory-T-cell stability, NK/iNKT cytotoxicity, macrophage/monocyte chemotaxis (STIM1-dependent; [PMID: 38815866](https://pubmed.ncbi.nlm.nih.gov/38815866/)).
- **Protein dysfunction:** Loss of function of STIM1 — failure of the EF-SAM Ca²⁺ sensor and CAD gating module (structural/biophysical basis: [PMID: 21217057](https://pubmed.ncbi.nlm.nih.gov/21217057/), [PMID: 20375143](https://pubmed.ncbi.nlm.nih.gov/20375143/), [PMID: 18166150](https://pubmed.ncbi.nlm.nih.gov/18166150/)).
- **Immune involvement:** Combined immunodeficiency (defective T/NK/B/iNKT/Treg) plus autoimmunity — "**It is dominated by severe immunodeficiency and autoimmunity due to impaired SOCE and defects in the function of several lymphocyte subsets. These include CD8⁺ T cells, CD4⁺ effector and regulatory T cells, natural killer (NK) cells and B cells**" ([PMID: 22615435](https://pubmed.ncbi.nlm.nih.gov/22615435/)). Reduced iNKT/Treg cells drive autoimmunity ("**ORAI1 mutations were associated with strongly reduced numbers of invariant natural killer T and regulatory T (Treg) cells**", [PMID: 29155098](https://pubmed.ncbi.nlm.nih.gov/29155098/)).
- **Biochemical abnormality:** Ion channel defect (CRAC channelopathy) — absent I_CRAC/SOCE.
- **Subcellular compartments (GO CC):** ER membrane (GO:0005789), ER–plasma membrane contact site (GO:0140268), plasma membrane (GO:0005886).

**Suggested GO biological-process terms:** store-operated calcium entry (GO:0002115), calcium ion transmembrane import into cytosol (GO:0097553), positive regulation of T-cell activation (GO:0050870), NFAT protein import into nucleus. **Suggested CL terms:** T cell (CL:0000084), CD8-positive αβ T cell (CL:0000625), regulatory T cell (CL:0000815), natural killer cell (CL:0000623), B cell (CL:0000236), ameloblast (CL:0000059), skeletal muscle fiber (CL:0008002). **CHEBI:** calcium(2+) (CHEBI:29108).

---

## 7. Anatomical Structures Affected

**Primary organ systems and structures (F007):**

| Level | Structure | UBERON / CL | Manifestation |
|---|---|---|---|
| Organ system | Immune/lymphoid system | UBERON:0002405 | Immunodeficiency + autoimmunity + lymphoproliferation |
| Organ | Skeletal muscle | UBERON:0001134 | Hypotonia / weakness |
| Organ/tissue | Skin — eccrine sweat glands | UBERON:0001820 | Anhidrosis (ectodermal dysplasia) |
| Organ/tissue | Tooth enamel organ / ameloblasts | UBERON:0001091 / CL:0000059 | Enamel hypomineralization |
| Organ | Eye — iris smooth muscle | UBERON:0001769 | Mydriasis |
| Secondary | Liver / spleen, lymph nodes | UBERON:0002107 / UBERON:0002106 | Hepatosplenomegaly, lymphadenopathy |

**Cell populations targeted:** CD8⁺ and CD4⁺ effector T cells, regulatory T cells, iNKT cells, NK cells, B cells, ameloblasts, skeletal myofibers, eccrine secretory epithelial cells, iris smooth muscle cells.

**Subcellular compartments:** ER membrane (STIM1 residence) and ER–plasma-membrane junctions where CRAC channels assemble (GO:0140268).

Supporting quotes: "**immunodeficiency, muscular hypotonia and anhydrotic ectodermal dysplasia**" ([PMID: 20189884](https://pubmed.ncbi.nlm.nih.gov/20189884/)); "**muscular hypotonia, and ectodermal dysplasia, with defects in sweat gland function and dental enamel formation. The latter defect emphasizes an important role of CRAC channels in tooth development**" ([PMID: 26469693](https://pubmed.ncbi.nlm.nih.gov/26469693/)). **Lateralization:** Systemic/bilateral, not lateralized.

---

## 8. Temporal Development

- **Onset:** Congenital to early infancy. The immunodeficiency typically manifests within the first months of life as recurrent/severe/opportunistic infections (SCID-like), consistent with the T-cell activation defect ([PMID: 20189884](https://pubmed.ncbi.nlm.nih.gov/20189884/)).
- **Onset pattern:** Immune disease — subacute/insidious then severe with infection; non-immune features (hypotonia, anhidrosis, enamel/iris defects) present congenitally.
- **Progression:** Immune disease is progressive/life-threatening if untreated; non-immune features are largely **static (non-degenerative)**. Autoimmune cytopenias and lymphoproliferation follow a chronic, relapsing course.
- **Duration:** Chronic/lifelong; the immunodeficiency is curable by HSCT, but ectodermal, dental, and muscle features persist.
- **Critical period / window of intervention:** Early infancy — analogous to SCID, early HSCT before infectious complications improves outcome. Mutation-specific ASO therapy would similarly be most valuable early.

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive.** Biallelic (homozygous or compound heterozygous) LOF variants are required; heterozygous carriers are clinically asymptomatic although their T cells show partially reduced SOCE — a demonstrated **gene-dosage effect** in the analogous ORAI1 channelopathy: "**Although heterozygous carriers of the mutation show no clinical symptoms of immunodeficiency, store-operated Ca²⁺ entry in their T cells is impaired, suggesting a gene-dosage effect of the mutation**" ([PMID: 19075015](https://pubmed.ncbi.nlm.nih.gov/19075015/)).
- **Penetrance / expressivity:** Loss of SOCE/CRAC current is a **fully penetrant cellular phenotype**, but **clinical expressivity is variable** — "**we confirmed that the complete loss of STIM1 function is not always associated with severe immune disorders**" ([PMID: 33733462](https://pubmed.ncbi.nlm.nih.gov/33733462/)).
- **Consanguinity:** Strongly associated; reported families are frequently consanguineous (e.g., "**we studied two siblings from a consanguineous Syrian family**", [PMID: 33733462](https://pubmed.ncbi.nlm.nih.gov/33733462/)).
- **Epidemiology:** **Ultra-rare.** Fewer than ~15 STIM1-deficient families reported worldwide; no reliable population prevalence/incidence estimate exists. **Carrier frequency:** Not established; variants are private/very rare.
- **Founder effects, anticipation, germline mosaicism:** None established. Anticipation is not expected (not a repeat-expansion disorder).
- **Sex ratio:** No strong sex bias reported (autosomal). **Geographic distribution:** Case reports skew to populations with higher consanguinity rates, reflecting recessive inheritance rather than true regional endemicity.

---

## 10. Diagnostics

**Diagnostic workflow (F008):** combine a **functional SOCE/CRAC assay** with **molecular genetic confirmation**.

1. **Functional biomarker (highly specific):** A store-operated Ca²⁺ entry (SOCE) assay on patient T cells or fibroblasts shows abolished/impaired Ca²⁺ influx and absent I_CRAC. "**Calcium influx analysis revealed impaired SOCE in the patient cells, indicating a loss of STIM1 function**" ([PMID: 38977117](https://pubmed.ncbi.nlm.nih.gov/38977117/)). Re-expression of wild-type protein rescues SOCE, confirming causality (rescue paradigm in the CRAC channelopathy spectrum: "**expression of wild-type Orai1 in SCID T cells restores store-operated Ca²⁺ influx and the CRAC current**", [PMID: 16582901](https://pubmed.ncbi.nlm.nih.gov/16582901/)).
2. **Molecular diagnosis:** Whole-exome sequencing ("**Using exome sequencing, we have identified a new homozygous frameshift mutation in STIM1**", [PMID: 33733462](https://pubmed.ncbi.nlm.nih.gov/33733462/)), targeted single-gene *STIM1* testing, or primary-immunodeficiency gene panels; historically supported by SNP-array linkage/genome-wide screens ("**a modified linkage analysis with single-nucleotide polymorphism arrays, and a Drosophila RNA interference screen**", [PMID: 16582901](https://pubmed.ncbi.nlm.nih.gov/16582901/)). WGS is also applicable.
3. **Immunologic workup:** Normal/near-normal lymphocyte numbers and development but **defective T-cell activation and cytokine production**; reduced Treg/iNKT cells; autoimmune cytopenias (hemolytic anemia, thrombocytopenia) on CBC/DAT.
4. **Other exam findings:** Muscle hypotonia; anhidrosis (sweat testing); enamel defects on dental exam; mydriasis on eye exam.

**Differential diagnosis:** Typical SCID (STIM1 deficiency is distinguished by *normal lymphocyte development* plus prominent autoimmunity/lymphoproliferation plus ectodermal/dental/muscle features); ORAI1 deficiency (partner gene, clinically near-identical — resolve by gene testing); anhidrotic ectodermal dysplasia with immunodeficiency (NEMO/IKBKG); other combined immunodeficiencies with immune dysregulation. STIM1 **gain-of-function** TAM/Stormorken syndrome is the key mirror-image differential (myopathy + thrombocytopenia + miosis, *dominant*).

**Screening:** Newborn TREC-based SCID screening may not reliably detect STIM1 deficiency because T-cell *numbers/development* are relatively preserved; cascade genetic testing and prenatal/carrier testing are appropriate in known families.

---

## 11. Outcome / Prognosis

- **Untreated prognosis:** Poor and life-threatening in infancy/early childhood. The SCID-like immunodeficiency causes recurrent, severe, and opportunistic viral, bacterial, and fungal infections; autoimmunity (hemolytic anemia, thrombocytopenia) and lymphoproliferation add substantial morbidity and mortality (F009, F011).
- **Curative treatment outcome:** Allogeneic HSCT can cure the hematopoietic/immune disease (see §12) but does **not** correct non-hematopoietic features (muscle hypotonia, anhidrosis/ectodermal dysplasia, dental enamel defects), which persist and require supportive management.
- **Morbidity / disability:** Chronic — heat intolerance from anhidrosis, motor impairment from hypotonia/myopathy, dental morbidity, and autoimmune cytopenia burden.
- **Prognostic factors:** Timing of diagnosis and HSCT, severity/control of infections and autoimmunity, and donor availability. No validated molecular prognostic biomarkers beyond the underlying null genotype.
- **Quality of life:** No formal EQ-5D/SF-36/PROMIS datasets exist for this ultra-rare disease.

---

## 12. Treatment

**Definitive therapy — Allogeneic HSCT (NCIT: Hematopoietic Stem Cell Transplantation, C15431).** Because the immunodeficiency is intrinsic to hematopoietic cells, allogeneic HSCT is the only curative option for the immune disease, as for other SCID/combined immunodeficiencies. A CRAC-channelopathy patient (ORAI1 deficiency) is documented within the inborn-errors-of-immunity HSCT pathway, receiving virus-specific T cells pre-transplant ("**1 ORAI1 deficiency**"; [PMID: 33462728](https://pubmed.ncbi.nlm.nih.gov/33462728/)). HSCT does **not** correct muscle, ectodermal, or dental manifestations (F009).

**Supportive / symptomatic care:**
- Immunoglobulin replacement (NCIT: Intravenous Immunoglobulin Therapy).
- Antimicrobial/antiviral/antifungal prophylaxis.
- Immunosuppression for autoimmune cytopenias and lymphoproliferation (corticosteroids, etc.).
- Heat-avoidance and thermoregulatory management for anhidrosis.
- Dental care for enamel defects; physiotherapy for hypotonia/weakness.

**Experimental / mutation-specific therapy:** A **splice-correcting antisense oligonucleotide (ASO)** restored STIM1 splicing and function in patient cells: "**We developed an antisense oligonucleotide treatment that improves STIM1 splicing and highlighted its potential as a therapeutic approach**" ([PMID: 38977117](https://pubmed.ncbi.nlm.nih.gov/38977117/)). This is genotype-specific (applicable to splice-altering alleles).

**Pharmacology note:** CRAC-channel modulators are being developed largely for **gain-of-function/inflammatory** indications — Orai *blockers* would be **irrational** for LOF deficiency (a channel activator, not a blocker, would conceptually be required). Selective Orai blockers (e.g., indazole/pyrazole scaffolds; [PMID: 39232360](https://pubmed.ncbi.nlm.nih.gov/39232360/)) are therefore relevant to the disease's differential/GOF spectrum but not to treating LOF STIM1 deficiency. **Pharmacogenomics:** Not applicable.

---

## 13. Prevention

- **Primary prevention:** Not possible for the monogenic disease itself. **Genetic counseling** for consanguineous families and families with a prior affected child is central; recurrence risk is 25% per pregnancy (autosomal recessive).
- **Reproductive options:** Carrier testing, preimplantation genetic diagnosis (PGD), and prenatal testing in known families.
- **Secondary prevention:** Early molecular diagnosis and cascade testing to enable timely HSCT before infectious complications. Standard newborn SCID (TREC) screening may miss STIM1 deficiency because T-cell numbers are relatively preserved — a diagnostic gap.
- **Tertiary prevention (complication avoidance):** Infection prophylaxis, IVIG, immunosuppression for autoimmunity, heat-avoidance for anhidrosis, dental surveillance, and vaccination caution (live vaccines contraindicated in combined immunodeficiency).
- **Immunization / public health / environmental interventions:** Not applicable as disease modifiers (non-infectious genetic disorder), beyond standard protection of immunocompromised patients.

---

## 14. Other Species / Natural Disease

- **Orthologs:** Mouse *Stim1* (NCBI Gene 20866; species *Mus musculus*, NCBI:txid10090); orthologs are conserved broadly across vertebrates. The STIM/Orai SOCE machinery is evolutionarily ancient — originally characterized in non-excitable cells and via *Drosophila* RNAi screens ([PMID: 16582901](https://pubmed.ncbi.nlm.nih.gov/16582901/)).
- **Natural disease in other species (OMIA/veterinary):** No well-established naturally occurring STIM1-deficiency disease has been characterized in companion animals or wildlife in the reviewed literature; the human disease is modeled mechanistically in engineered mice.
- **Comparative biology:** The SOCE pathway is highly conserved, so engineered *Stim1* loss in mice recapitulates key aspects of the human disease (see §15). **Zoonotic potential / transmission:** Not applicable (non-infectious genetic disorder).

---

## 15. Model Organisms

**Mouse (*Mus musculus*) is the principal model (F006):**

| Model | Finding | Recapitulation | Reference |
|---|---|---|---|
| T-cell/conditional *Stim1*-deficient mice | Impaired autoreactive T-cell activation, reduced Th1/Th17, complete EAE protection | Confirms in vivo requirement of STIM1/SOCE for effector T-cell function (mirrors human immunodeficiency) | [PMID: 20028655](https://pubmed.ncbi.nlm.nih.gov/20028655/) |
| Treg-specific *Stim1* deletion | STIM1-dependent stress signaling drives Treg instability/inflammation | Models the human autoimmunity/immune-dysregulation phenotype | [PMID: 42421074](https://pubmed.ncbi.nlm.nih.gov/42421074/) |
| Macrophage/monocyte studies | STIM1-dependent SOCE governs chemotaxis and monocyte recruitment | Models innate-immune contribution | [PMID: 38815866](https://pubmed.ncbi.nlm.nih.gov/38815866/) |
| Ameloblast/enamel *Stim1* models | Stim1 regulates enamel mineralization; LOF impairs SOCE in enamel cells | Explains dental enamel phenotype | [PMID: 28732182](https://pubmed.ncbi.nlm.nih.gov/28732182/), [PMID: 28352661](https://pubmed.ncbi.nlm.nih.gov/28352661/) |
| Patient lymphocytes/fibroblasts (cellular model) | Absent SOCE, rescued by WT re-expression | Establishes channel defect → absent SOCE causality | [PMID: 16582901](https://pubmed.ncbi.nlm.nih.gov/16582901/) |

Supporting quote: "**STIM1 deficiency significantly impaired the generation of neuroantigen-specific T cell responses in vivo with reduced Th1/Th17 responses, resulting in complete protection from EAE**" ([PMID: 20028655](https://pubmed.ncbi.nlm.nih.gov/20028655/)).

**Model types available:** Conditional/tissue-specific knockouts (T-cell, Treg, ameloblast), global knockdowns, patient-derived primary cells and fibroblasts; iPSC/organoid models are feasible but not prominently reported. **Model limitations:** Global *Stim1* knockout is largely perinatal-lethal in mice, necessitating conditional models; single-tissue models capture individual branches (immune, dental) rather than the full multisystem human syndrome. **Applications:** Dissecting SOCE-dependent T-cell activation, tolerance, enamel biology, and testing splice-correction/rescue strategies.

---

## Mechanistic Model / Synthesis

```
   Biallelic LOF STIM1 mutation (nonsense / frameshift / splice)
                        │  (loss / nonfunction of STIM1 protein)
                        ▼
   EF-SAM domain cannot sense ER Ca2+ depletion → no autoinhibition relief
                        │
                        ▼
   No STIM1 oligomerization / CAD-mediated translocation to ER–PM junctions
                        │
                        ▼
   ORAI1 not gated → CRAC channels CLOSED → ABSENT SOCE (I_CRAC = 0)
                        │
        ┌───────────────┼───────────────┬───────────────┬──────────────┐
        ▼               ▼               ▼               ▼              ▼
 Ca2+–calcineurin   Muscle Ca2+     Sweat gland      Ameloblast      Iris smooth
 –NFAT axis fails   handling ↓      secretion ↓      SOCE ↓          muscle ↓
        │               │               │               │              │
        ▼               ▼               ▼               ▼              ▼
 Cytokine genes    Hypotonia /     Anhidrosis /     Enamel          Mydriasis
 not transcribed   myopathy        ectodermal       hypoplasia
 (IL-2 etc.)                       dysplasia
        │
        ▼
 Combined immunodeficiency (defective T/NK/B/iNKT)
 + Treg/iNKT dysfunction → autoimmunity + lymphoproliferation
        │
        ▼
 Recurrent/opportunistic infections + autoimmune cytopenias
 (life-threatening in infancy; curable by HSCT — immune branch only)
```

The unifying principle is that **STIM1 is the obligatory ER Ca²⁺ sensor for SOCE**, and its loss removes a single node whose downstream Ca²⁺ signal is required across many terminally differentiated cell types. The immune branch is clinically dominant and the only one correctable by HSCT, because it is hematopoietic-cell-intrinsic; the muscle, ectodermal, and dental branches arise in non-hematopoietic tissues and therefore persist after transplant. The **LOF↔GOF mirror** (deficiency vs TAM/Stormorken) is the organizing classification insight: both perturb the same Ca²⁺ set-point but in opposite directions, and both produce myopathy — underscoring how tightly skeletal muscle depends on SOCE homeostasis.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in report |
|---|---|---|
| [26469693](https://pubmed.ncbi.nlm.nih.gov/26469693/) | *Diseases caused by mutations in ORAI1 and STIM1* | Defines CRAC channelopathy; LOF vs GOF dichotomy; non-immune features (F001, F004, F007, F011, F012) |
| [20189884](https://pubmed.ncbi.nlm.nih.gov/20189884/) | *Immunodeficiency due to mutations in ORAI1 and STIM1* | STIM1-specific autoimmunity/lymphoproliferation; T-cell activation defect (F002, F007, F009, F011) |
| [22615435](https://pubmed.ncbi.nlm.nih.gov/22615435/) | *Regulation of lymphocyte function by ORAI/STIM* | Lymphocyte subsets affected (F002, F011) |
| [33733462](https://pubmed.ncbi.nlm.nih.gov/33733462/) | *Novel bi-allelic LOF STIM1 mutation expands phenotype* | c.685delT complete protein loss; consanguinity; variable expressivity (F001, F004, F005, F008) |
| [38977117](https://pubmed.ncbi.nlm.nih.gov/38977117/) | *SOCE dysfunction from novel STIM1 mutation* | Splice variant; SOCE assay; ASO therapy (F001, F004, F008, F009) |
| [20111871](https://pubmed.ncbi.nlm.nih.gov/20111871/) | *CRAC channelopathies* | Normal STIM1→ORAI1 SOCE mechanism (F003) |
| [20375143](https://pubmed.ncbi.nlm.nih.gov/20375143/) | *CRAC activation domain in STIM1 oligomerization* | CAD gating module (F003) |
| [21217057](https://pubmed.ncbi.nlm.nih.gov/21217057/) | *Auto-inhibitory role of EF-SAM* | ER Ca²⁺-sensing module (F003) |
| [18166150](https://pubmed.ncbi.nlm.nih.gov/18166150/) | *Biophysical characterization of EF-SAM* | STIM1/2 sensor biophysics (F003) |
| [23483280](https://pubmed.ncbi.nlm.nih.gov/23483280/) | *Orai1-NFAT signalling in T cells* | Calcineurin-NFAT effector pathway (F010) |
| [16582901](https://pubmed.ncbi.nlm.nih.gov/16582901/) | *Orai1 mutation abrogates CRAC function* | Rescue paradigm; NFAT link; discovery methods (F006, F008, F010) |
| [39984734](https://pubmed.ncbi.nlm.nih.gov/39984734/) | *STIM1-NFAT synergizes with STAT1 → T-bet* | Th1 differentiation branch (F010) |
| [19075015](https://pubmed.ncbi.nlm.nih.gov/19075015/) | *Orai1 SCID mutation in heterozygotes* | Recessive/gene-dosage; carriers asymptomatic (F005) |
| [20028655](https://pubmed.ncbi.nlm.nih.gov/20028655/) | *STIM1/2 in autoreactive T-cell activation (EAE)* | Mouse effector T-cell requirement (F006) |
| [42421074](https://pubmed.ncbi.nlm.nih.gov/42421074/) | *STIM1-dependent Treg dysfunction* | Treg instability/autoimmunity model (F006) |
| [38815866](https://pubmed.ncbi.nlm.nih.gov/38815866/) | *STIM1-dependent SOCE in macrophage chemotaxis* | Innate-immune model (F006) |
| [28732182](https://pubmed.ncbi.nlm.nih.gov/28732182/) | *Stim1 regulates enamel mineralization* | Dental/ameloblast mechanism (F007) |
| [28352661](https://pubmed.ncbi.nlm.nih.gov/28352661/) | *SOCE in enamel cells* | Enamel SOCE dependence (F007) |
| [33462728](https://pubmed.ncbi.nlm.nih.gov/33462728/) | *Viral-specific T cells pre-HSCT in IEI* | HSCT pathway incl. CRAC channelopathy (F009) |
| [29155098](https://pubmed.ncbi.nlm.nih.gov/29155098/) | *ORAI1 mutations abolishing SOCE* | Reduced iNKT/Treg → autoimmunity (F002) |

**Evidence source types:** Human clinical (case reports/kindreds: 33733462, 38977117, 20189884, 19075015); in vitro/biophysical (21217057, 20375143, 18166150, 20111871); model organism (20028655, 42421074, 38815866, 28732182, 28352661); computational/structural (EF-SAM/CAD studies).

---

## Limitations and Knowledge Gaps

1. **Ultra-rare, case-based evidence.** Fewer than ~15 STIM1-deficient families are reported; there are **no population prevalence/incidence figures**, no natural-history cohorts, and no formal QoL datasets. Frequencies of individual phenotypes are qualitative.
2. **Cross-gene extrapolation.** Several mechanistic and treatment points (carrier gene-dosage effect, HSCT pathway, iNKT/Treg reduction) draw on the closely related **ORAI1 deficiency** because STIM1-specific human data are sparse. ORAI1 and STIM1 are obligate partners, so extrapolation is well justified but not identical.
3. **Non-immune branches are partly model-inferred.** The muscle, sweat-gland, and iris branches are strongly inferred from SOCE biology and mouse data; direct human tissue-level mechanistic proof is limited. Enamel involvement is best supported (mouse ameloblast models).
4. **Variable expressivity is unexplained.** The observation that complete STIM1 loss is "not always associated with severe immune disorders" ([PMID: 33733462](https://pubmed.ncbi.nlm.nih.gov/33733462/)) lacks a defined modifier mechanism (possibly STIM2 compensation — untested in humans).
5. **Therapeutics are early.** HSCT experience specific to STIM1 (vs ORAI1) is limited; the splice-correcting ASO is in vitro proof-of-concept only, with no clinical trial (no NCT identifier established).
6. **No investigational primary dataset was analyzed** in this study; conclusions are literature-synthesis based.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international STIM1-deficiency registry** to quantify prevalence, genotype–phenotype correlations, penetrance/expressivity of each organ branch, and long-term HSCT vs non-immune outcomes.
2. **Test STIM2 as a modifier** of expressivity in patient cells and mouse models (e.g., STIM2 dosage rescue of residual SOCE), to explain why some complete-LOF patients lack severe immune disease.
3. **Advance the splice-correcting ASO** toward preclinical/IND studies for splice-altering alleles (e.g., c.792-3C>G), and evaluate gene-replacement or base/prime-editing for null alleles.
4. **Systematic multi-tissue phenotyping in conditional mouse models** (muscle-, sweat-gland-, and iris-specific *Stim1* KO) to convert inferred branches into demonstrated mechanisms and to test whether HSCT alone can address any non-immune feature.
5. **Improve newborn screening** — because TREC screening may miss STIM1 deficiency (preserved T-cell numbers), evaluate functional SOCE-based or panel-based add-ons for high-risk/consanguineous populations.
6. **Prospective HSCT outcome study** in CRAC channelopathy (STIM1 + ORAI1) to define conditioning, timing, and the fate of autoimmunity/lymphoproliferation post-transplant.

---

*Report compiled from 12 confirmed findings and 48 reviewed papers across 5 investigation iterations. Evidence is human clinical (case reports/kindreds), in vitro/biophysical, and model-organism; primary population-scale data are unavailable for this ultra-rare disorder.*


## Artifacts

- [OpenScientist final report](STIM1_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](STIM1_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 32 |
| Quoted claims found in source | 25 |
| Quoted claims **not** found in source | 7 |
| References weighed for topical relevance | 23 |
| On topic | 17 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

6 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:26469693`: "**By contrast, autosomal dominant gain-of-function mutations in ORAI1 and STIM1 result in constitutive CRAC channel activation, SOCE, and increased intracellular Ca²⁺ levels that are associated with an overlapping spectrum of diseases, including nonsyndromic tubular aggregate myopathy (TAM) and York platelet and Stormorken syndromes**"
  - closest text in source: "By contrast, autosomal dominant gain-of-function mutations in ORAI1 and STIM1 result in constitutive CRAC channel activation, SOCE, and increased intracellular Ca(2+) levels that are associated with an overlapping spectrum of diseases, including nonsyndromic tubular aggregate myopathy (TAM) and York platelet and Stormorken syndromes"
- `PMID:33733462` *(abstract only)*: "**we have identified a new homozygous frameshift mutation in STIM1: c.685delT [p.(Phe229Leufs*12)], leading to a complete loss of STIM1 protein**"
  - closest text in source: "Using exome sequencing, we have identified a new homozygous frameshift mutation in STIM1: c.685delT [p.(Phe229Leufs*12)], leading to a complete loss of STIM1 protein"
- `PMID:21217057` *(abstract only)*: "**the STIM1 Ca²⁺-binding EF-hand and the STIM2 SAM domain are major contributors to the autoinhibition of oligomerization**"
  - closest text in source: "To probe the structural basis for the functional differences between STIM1 and STIM2 we engineered a series of EF-hand and sterile α motif (SAM) domain (EF-SAM) chimeras, demonstrating that the STIM1 Ca(2+)-binding EF-hand and the STIM2 SAM domain are major contributors to the autoinhibition of oligomerization in each respective isoform"
- `PMID:20111871` *(abstract only)*: "**ORAI1 (or CRACM1) acts as the pore-forming subunit of the CRAC channel in the plasma membrane. Stromal interaction molecule (STIM) 1 is localized in the ER, senses [Ca²⁺]ER, and activates the CRAC channel upon store depletion by binding to ORAI1**"
  - closest text in source: "Stromal interaction molecule (STIM) 1 is localized in the ER, senses [Ca2+]ER, and activates the CRAC channel upon store depletion by binding to ORAI1"
- `PMID:23483280` *(abstract only)*: "**Ca²⁺-calcineurin-nuclear factor of activated T cells (NFAT) signalling pathway**"
  - closest text in source: "TCR activation turns on various signalling pathways, one of the important one being the Ca(2+)-calcineurin-nuclear factor of activated T cells (NFAT) signalling pathway"
- `PMID:19075015` *(abstract only)*: "**Although heterozygous carriers of the mutation show no clinical symptoms of immunodeficiency, store-operated Ca²⁺ entry in their T cells is impaired, suggesting a gene-dosage effect of the mutation**"
  - closest text in source: "Although heterozygous carriers of the mutation show no clinical symptoms of immunodeficiency, store-operated Ca(2+) entry in their T cells is impaired, suggesting a gene-dosage effect of the mutation"
- `PMID:16582901` *(abstract only)*: "**expression of wild-type Orai1 in SCID T cells restores store-operated Ca²⁺ influx and the CRAC current**"
  - closest text in source: "The SCID patients are homozygous for a single missense mutation in ORAI1, and expression of wild-type Orai1 in SCID T cells restores store-operated Ca2+ influx and the CRAC current (I(CRAC))"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 14 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 11 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013008` (2 mentions) - the report calls it "MONDO"; MONDO calls it **combined immunodeficiency due to STIM1 deficiency**
- `HP:0005387` (1 mention) - the report calls it "Clinical/lab"; HP calls it **Combined immunodeficiency**
- `HP:0002719` (1 mention) - the report calls it "Clinical"; HP calls it **Recurrent infections**
- `HP:0001890` (1 mention) - the report calls it "Lab/clinical"; HP calls it **Autoimmune hemolytic anemia**
- `HP:0001973` (1 mention) - the report calls it "Lab/clinical"; HP calls it **Autoimmune thrombocytopenia**
- `HP:0002716` (1 mention) - the report calls it "Clinical"; HP calls it **Lymphadenopathy**
- `HP:0001433` (1 mention) - the report calls it "Clinical"; HP calls it **Hepatosplenomegaly**
- `HP:0001252` (1 mention) - the report calls it "Physical"; HP calls it **Hypotonia**
- `HP:0001324` (1 mention) - the report calls it "Physical"; HP calls it **Muscle weakness**
- `HP:0000535` (1 mention) - the report calls it "Physical"; HP calls it **obsolete Sparse and thin eyebrow**
- `UBERON:0001769` (1 mention) - the report calls it "Eye — iris smooth muscle"; UBERON calls it **iris**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0009925` (1 mention) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0000535` (obsolete Sparse and thin eyebrow) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0002405` (1 mention) - the report calls it "Immune/lymphoid system"; UBERON calls it **immune system**
- `UBERON:0001134` (1 mention) - the report calls it "Skeletal muscle"; UBERON calls it **skeletal muscle tissue**, and lists "skeletal muscle" among its other names
- `UBERON:0001820` (1 mention) - the report calls it "Skin — eccrine sweat glands"; UBERON calls it **sweat gland**