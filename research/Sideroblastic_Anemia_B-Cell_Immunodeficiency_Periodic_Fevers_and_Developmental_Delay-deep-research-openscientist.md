---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-06T19:40:51.645652'
end_time: '2026-11-06T20:24:38.348409'
duration_seconds: 2626.7
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Sideroblastic Anemia with B-Cell Immunodeficiency, Periodic Fevers,
    and Developmental Delay
  mondo_id: MONDO:0014487
  category: Mendelian
  causal_genes: TRNT1
  omim_id: OMIM:616084
  synonyms: SIFD syndrome; SIFD
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
citation_count: 19
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 21
  on_topic: 21
  validator_version: 0.5.1
term_validation:
  total_terms: 44
  verified: 42
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 7
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0014487
    reported_labels:
    - MONDO
    ontology_label: congenital sideroblastic anemia-B-cell immunodeficiency-periodic
      fever-developmental delay syndrome
  - term_id: HP:0011368
    reported_labels:
    - dermatological manifestation
    ontology_label: Epidermal thickening
  - term_id: GO:0006914
    reported_labels:
    - Cellular processes:** impaired autophagy
    ontology_label: autophagy
  - term_id: GO:0005739
    reported_labels:
    - mitochondria
    - Subcellular localization:** **mitochondria
    ontology_label: mitochondrion
  - term_id: UBERON:0000955
    reported_labels:
    - "Nervous system** \u2014 brain"
    ontology_label: brain
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
  path: Sideroblastic_Anemia_B-Cell_Immunodeficiency_Periodic_Fevers_and_Developmental_Delay-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Sideroblastic_Anemia_B-Cell_Immunodeficiency_Periodic_Fevers_and_Developmental_Delay-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sideroblastic Anemia with B-Cell Immunodeficiency, Periodic Fevers, and Developmental Delay
- **MONDO ID:** MONDO:0014487 (if available)
- **Causal gene(s):** TRNT1
- **OMIM:** OMIM:616084
- **Synonyms:** SIFD syndrome; SIFD
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Sideroblastic Anemia with B-Cell Immunodeficiency, Periodic Fevers, and Developmental Delay** covering all of the
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

# Sideroblastic Anemia with B-Cell Immunodeficiency, Periodic Fevers, and Developmental Delay (SIFD) — Comprehensive Disease Report

**Disease:** Sideroblastic Anemia with B-Cell Immunodeficiency, Periodic Fevers, and Developmental Delay (SIFD)
**Causal gene:** **TRNT1** (tRNA nucleotidyltransferase 1; CCA-adding enzyme; HGNC:17341; gene OMIM 612907)
**Disease identifiers:** MONDO:0014487 · OMIM 616084 · Orphanet ORPHA:457395 · Synonyms: SIFD syndrome, SIFD, TRNT1 deficiency
**Category:** Mendelian, autosomal recessive

> This report concerns **SIFD syndrome**, caused by **biallelic partial loss-of-function variants in _TRNT1_**, the gene encoding the **CCA-adding tRNA nucleotidyltransferase** that matures the 3′ end of all cytosolic and mitochondrial transfer RNAs. All identifiers above point to the same TRNT1-related entity; the disease name is descriptive (not a serial number).

---

## Summary

SIFD is a rare, autosomal-recessive, infantile-onset multisystem disorder caused by **biallelic partial loss-of-function variants in TRNT1**, the gene encoding the essential **CCA-adding tRNA nucleotidyltransferase**. TRNT1 catalyzes the template-independent addition of the 3′-terminal cytosine–cytosine–adenosine (CCA) trinucleotide to all mature cytosolic and mitochondrial tRNAs, a modification obligatory for aminoacylation and therefore for protein synthesis in both compartments. Because complete loss of TRNT1 is incompatible with life, SIFD arises only from hypomorphic allele combinations that reduce — but do not abolish — enzymatic activity ([PMID: 25193871](https://pubmed.ncbi.nlm.nih.gov/25193871/); [PMID: 32471101](https://pubmed.ncbi.nlm.nih.gov/32471101/)).

The clinical syndrome was first delineated by Wiseman and colleagues in 2013 across 12 cases, one year before TRNT1 was identified as the cause ([PMID: 23553769](https://pubmed.ncbi.nlm.nih.gov/23553769/); [PMID: 25193871](https://pubmed.ncbi.nlm.nih.gov/25193871/)). The cardinal tetrad — sideroblastic/microcytic anemia, B-cell immunodeficiency with hypogammaglobulinemia, periodic fevers, and developmental delay — is accompanied by a broad spectrum of secondary features including retinitis pigmentosa, cataract, sensorineural deafness, cardiomyopathy, renal tubulopathy, gastrointestinal disease, and neutrophilic dermatosis. Mechanistically, reduced CCA addition depletes mature tRNAs, impairing cytosolic and mitochondrial translation; this produces mitochondrial dysfunction, oxidative stress, impaired autophagy/proteostasis, and a **TNF-driven autoinflammatory state** ([PMID: 29358286](https://pubmed.ncbi.nlm.nih.gov/29358286/); [PMID: 28390992](https://pubmed.ncbi.nlm.nih.gov/28390992/)).

Prognosis is guarded: pooled survival is roughly 69% at 10 years, with early onset (≤3 months), seizures, and low B-cell counts predicting worse outcomes, and the recurrent hot-spot allele **c.668T>C (p.Ile223Thr)** over-represented among fatal cases ([PMID: 41795040](https://pubmed.ncbi.nlm.nih.gov/41795040/); [PMID: 34310935](https://pubmed.ncbi.nlm.nih.gov/34310935/)). Two therapeutic pillars have emerged: **TNF-α inhibitors** (etanercept, adalimumab; thalidomide as alternative) control the autoinflammatory component, and **allogeneic hematopoietic stem cell transplantation (HSCT)** can correct the hematologic and immunologic disease ([PMID: 29358286](https://pubmed.ncbi.nlm.nih.gov/29358286/); [PMID: 23553769](https://pubmed.ncbi.nlm.nih.gov/23553769/)).

---

## 1. Disease Information

SIFD is a syndromic congenital sideroblastic anemia in which hematologic disease co-occurs with humoral immunodeficiency, recurrent/periodic febrile episodes without an infective cause, and neurodevelopmental impairment. It was originally described as "a novel syndrome of congenital sideroblastic anemia, B-cell immunodeficiency, periodic fevers, and developmental delay" ([PMID: 23553769](https://pubmed.ncbi.nlm.nih.gov/23553769/)).

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0014487 |
| OMIM (disease) | 616084 |
| OMIM (gene TRNT1) | 612907 |
| Orphanet | ORPHA:457395 |
| HGNC | 17341 (TRNT1) |
| MeSH | indexed under sideroblastic anemia / immunologic deficiency syndromes |
| ICD-10 | D64.0 (hereditary sideroblastic anemia), approximate |

**Synonyms / alternative names:** SIFD; SIFD syndrome; TRNT1 deficiency; congenital sideroblastic anemia with immunodeficiency, fevers and developmental delay.

**Source of information:** The knowledge in this report is derived from **aggregated disease-level resources** — systematic reviews and case series pooling individually-reported patients from the world literature — rather than from a single EHR cohort. The largest aggregations comprise roughly 58–75+ unique patients ([PMID: 35984545](https://pubmed.ncbi.nlm.nih.gov/35984545/); [PMID: 41795040](https://pubmed.ncbi.nlm.nih.gov/41795040/)).

---

## 2. Etiology

**Primary cause — genetic:** SIFD is caused by **biallelic (homozygous or compound heterozygous) partial loss-of-function variants in TRNT1** ([PMID: 25193871](https://pubmed.ncbi.nlm.nih.gov/25193871/); [PMID: 32471101](https://pubmed.ncbi.nlm.nih.gov/32471101/)). As stated in the landmark gene discovery, *"SIFD is caused by biallelic mutations in TRNT1, the gene encoding the CCA-adding enzyme essential for maturation of both nuclear and mitochondrial transfer RNAs"* ([PMID: 25193871](https://pubmed.ncbi.nlm.nih.gov/25193871/)).

**Genetic risk architecture:** The disease is fully penetrant Mendelian; two hypomorphic alleles are required. Complete loss of function is lethal, so all disease-causing genotypes retain residual enzyme activity ([PMID: 25193871](https://pubmed.ncbi.nlm.nih.gov/25193871/)). The nature of the allele combination is the principal determinant of severity — milder/more hypomorphic combinations produce the attenuated **retinitis pigmentosa with erythrocyte microcytosis** phenotype, while more severe combinations produce full SIFD, illustrating a genotype–phenotype gradient along a single allelic series: partial LOF *"are associated with various, seemingly unrelated human diseases including sideroblastic anemia with B-cell immunodeficiency, periodic fevers and developmental delay (SIFD), retinitis pigmentosa with erythrocyte microcytosis, and progressive B-cell immunodeficiency"* ([PMID: 32471101](https://pubmed.ncbi.nlm.nih.gov/32471101/); [PMID: 42830586](https://pubmed.ncbi.nlm.nih.gov/42830586/)).

**Environmental risk, protective factors, and gene–environment interaction:** No established environmental risk factors, protective dietary/lifestyle factors, or gene–environment interactions have been identified for this monogenic disorder. **Consanguinity** increases the likelihood of homozygous genotypes in affected families (see §9). Febrile/inflammatory episodes may be clinically triggered by intercurrent infection, but the disease itself is genetically determined. *This information is not available / not applicable beyond the genetic etiology.*

---

## 3. Phenotypes

Phenotype frequencies are best quantified by the systematic review of 58 unique patients ([PMID: 35984545](https://pubmed.ncbi.nlm.nih.gov/35984545/)), which reported: *"The most frequent manifestations are haematologic such as microcytic anaemia or sideroblastic anaemia (55/58), recurrent fever (52/58), neurologic abnormalities (48/58), immunologic abnormalities in particular a humoral immunodeficiency (48/58), gastrointestinal signs and symptoms (38/58), eye diseases as cataract and retinitis pigmentosa (27/58), failure to thrive (26/58), mucocutaneous involvement (29/58), sensorineural deafness (19/58)."*

| Phenotype | Type | Frequency | HPO suggestion |
|---|---|---|---|
| Microcytic / sideroblastic anemia | Lab abnormality / hematologic | 55/58 (~95%) | HP:0001877 (microcytic anemia); HP:0001924 (sideroblastic anemia) |
| Recurrent / periodic fever | Clinical sign | 52/58 (~90%) | HP:0001954 (recurrent fever); HP:0025142 (periodic fever) |
| Neurologic abnormality / developmental delay | Clinical sign | 48/58 (~83%) | HP:0001263 (global developmental delay) |
| Humoral immunodeficiency / hypogammaglobulinemia | Lab abnormality / immunologic | 48/58 (~83%) | HP:0004313 (decreased antibody level); HP:0005404 (B-cell lymphopenia) |
| Gastrointestinal signs | Clinical sign | 38/58 (~66%) | HP:0011024 (GI tract abnormality) |
| Mucocutaneous involvement | Physical manifestation | 29/58 (~50%) | HP:0011368 (dermatological manifestation) |
| Eye disease (cataract, retinitis pigmentosa) | Clinical sign | 27/58 (~47%) | HP:0000518 (cataract); HP:0000510 (retinitis pigmentosa) |
| Failure to thrive | Clinical sign | 26/58 (~45%) | HP:0001508 (failure to thrive) |
| Sensorineural deafness | Clinical sign | 19/58 (~33%) | HP:0000407 (sensorineural hearing impairment) |

**Additional reported features:** cardiomyopathy (HP:0001638), renal tubulopathy/nephrocalcinosis (HP:0000121), hepatosplenomegaly (HP:0001433), exocrine pancreatic insufficiency (HP:0001738), cerebellar atrophy (HP:0001272), seizures (HP:0001250), brittle hair (HP:0002299), and neutrophilic dermatosis ([PMID: 27370603](https://pubmed.ncbi.nlm.nih.gov/27370603/); [PMID: 29055896](https://pubmed.ncbi.nlm.nih.gov/29055896/); [PMID: 33332575](https://pubmed.ncbi.nlm.nih.gov/33332575/)).

**Characteristics:** Age of onset is **neonatal/early-infantile** — *"Onset of disease is very early with a median age of 4 months (range 0-252 months)"* across 58 patients ([PMID: 35984545](https://pubmed.ncbi.nlm.nih.gov/35984545/)) and mean ~3.0 months in another series ([PMID: 36729249](https://pubmed.ncbi.nlm.nih.gov/36729249/)). Severity is **variable** but often severe; fevers follow an **episodic/periodic** course while anemia and developmental features are typically **progressive/chronic**. The disease can be exceptionally severe antenatally, presenting as fetal hydrops and neonatal death with prominent extramedullary erythropoiesis ([PMID: 29055896](https://pubmed.ncbi.nlm.nih.gov/29055896/)).

**Quality-of-life impact:** Transfusion dependence, recurrent fevers, developmental delay, visual/hearing loss, and immunodeficiency collectively impose a very high burden on affected children and caregivers. Formal EQ-5D/SF-36/PROMIS data are *not available* for this ultra-rare disease.

---

## 4. Genetic / Molecular Information

**Causal gene:** **TRNT1** (tRNA nucleotidyltransferase 1), chromosome 3p; gene OMIM 612907; HGNC:17341. The enzyme adds the 3′-terminal CCA trinucleotide to all mature cytosolic and mitochondrial tRNAs: *"tRNA nucleotidyl transferase 1 (TRNT1) is an essential enzyme catalyzing the addition of terminal cytosine-cytosine-adenosine (CCA) trinucleotides to all mature tRNAs, which is necessary for aminoacylation"* ([PMID: 32471101](https://pubmed.ncbi.nlm.nih.gov/32471101/)).

**Pathogenic variant spectrum:** Across ~41–46 reported mutations in 58–75 patients, variants are **predominantly missense**, with additional nonsense, frameshift, and splice-site alleles; non-coding/promoter variants are over-represented among fatal cases ([PMID: 35984545](https://pubmed.ncbi.nlm.nih.gov/35984545/); [PMID: 36729249](https://pubmed.ncbi.nlm.nih.gov/36729249/); [PMID: 34310935](https://pubmed.ncbi.nlm.nih.gov/34310935/)). Representative variants include:

| Variant (cDNA) | Protein | Notes |
|---|---|---|
| c.668T>C | p.Ile223Thr | Recurrent **hot-spot**; severe/lethal association |
| c.88A>G | p.Met30Val | Compound-het, uncertain significance ([PMID: 34625936](https://pubmed.ncbi.nlm.nih.gov/34625936/)) |
| c.363G>T | p.Glu121Asp | Compound-het, likely pathogenic ([PMID: 34625936](https://pubmed.ncbi.nlm.nih.gov/34625936/)) |
| c.193G>C | p.Ala65Pro | Hypomorphic, RP phenotype ([PMID: 42830586](https://pubmed.ncbi.nlm.nih.gov/42830586/)) |
| c.1252dup | p.Ser418fs | Truncating, in trans with hypomorph ([PMID: 42830586](https://pubmed.ncbi.nlm.nih.gov/42830586/)) |
| c.495_498del | p.Phe167Tfs*9 | Neutrophilic dermatosis case ([PMID: 33332575](https://pubmed.ncbi.nlm.nih.gov/33332575/)) |
| c.1246A>G | p.Lys416Glu | Same case ([PMID: 33332575](https://pubmed.ncbi.nlm.nih.gov/33332575/)) |

**Variant classification (ACMG/AMP):** Most established alleles are pathogenic/likely pathogenic; novel variants are often classified by combinations of PM1/PM2/PP3/PP4 and functional evidence ([PMID: 34625936](https://pubmed.ncbi.nlm.nih.gov/34625936/)). **Allele frequency:** Pathogenic alleles are rare in gnomAD, consistent with ultra-rare recessive disease (carrier frequency undefined).

**Functional consequences — loss of function (hypomorphic):** In vitro characterization shows disease-linked missense substitutions reduce protein thermal stability and/or catalytic efficiency: *"the SIFD phenotype is linked to poor stability of the T154I and L166S variant proteins, and to a combination of reduced stability and altered catalytic efficiency in the M158V, R190I and I223T variants"* ([PMID: 29454993](https://pubmed.ncbi.nlm.nih.gov/29454993/)). The mechanism is **partial loss of function**, not gain of function or dominant-negative action: *"the patient-associated TRNT1 mutations result in partial loss of function of TRNT1 and lead to metabolic defects in both the mitochondria and cytosol, which can account for the phenotypic pleiotropy"* ([PMID: 25193871](https://pubmed.ncbi.nlm.nih.gov/25193871/)).

**Modifier genes, epigenetics, chromosomal abnormalities:** No established modifier genes, disease-specific epigenetic signatures, or chromosomal abnormalities have been reported. *Not available / not applicable.* **Somatic vs germline:** All pathogenic variants are **germline**.

---

## 5. Environmental Information

SIFD is a monogenic disorder with **no established environmental, lifestyle, or infectious causal agents**. Intercurrent infections may precipitate febrile/inflammatory flares and, given the humoral immunodeficiency, patients are susceptible to bacterial and viral infections (e.g., herpetic stomatitis, pneumonia, Metapneumovirus tracheitis reported in one case; [PMID: 33332575](https://pubmed.ncbi.nlm.nih.gov/33332575/)), but these are complications rather than causes. *Environmental and lifestyle sections are not applicable to disease causation.*

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic hypomorphic TRNT1 variants** reduce the abundance/stability/catalytic efficiency of the CCA-adding enzyme (demonstrated in vitro) → **leads to** partial loss of 3′-CCA-addition capacity. ([PMID: 25193871](https://pubmed.ncbi.nlm.nih.gov/25193871/); [PMID: 29454993](https://pubmed.ncbi.nlm.nih.gov/29454993/))
2. Reduced CCA addition → **results in** failure to mature a fraction of **mitochondrial tRNAs** (tRNA-Cys, tRNA-LeuUUR, tRNA-His demonstrated in patient fibroblasts) **and cytosolic tRNAs** (deep tRNA-seq shows significant deficiency of mature cytosolic tRNAs). ([PMID: 27370603](https://pubmed.ncbi.nlm.nih.gov/27370603/); [PMID: 29358286](https://pubmed.ncbi.nlm.nih.gov/29358286/))
3. tRNA pool depletion → **impairs aminoacylation and translation** in both compartments → loss of tRNA integrity and imbalance of distinct proteins (proteostasis defect). ([PMID: 37239403](https://pubmed.ncbi.nlm.nih.gov/37239403/))
   - **Branch A (mitochondrial):** Impaired mitochondrial translation → **leads to** mitochondrial dysfunction and **oxidative stress**, with impaired **autophagy**: *"Patient-specific iPSCs and iPSC-derived retinal organoids exhibited a deficit in autophagy, as evidenced by aberrant accumulation of LC3-II and elevated levels of oxidative stress"* ([PMID: 28390992](https://pubmed.ncbi.nlm.nih.gov/28390992/)).
   - **Branch B (cytosolic/immune):** Cytosolic tRNA deficiency and proteostasis stress → **drives** a TNF-dependent autoinflammatory program (elevated serum IL-6, IFN-γ and IFN-induced cytokines; tissue TNF and IL-1β), *inferred* to arise from stress-sensing of aberrant translation. ([PMID: 29358286](https://pubmed.ncbi.nlm.nih.gov/29358286/))
4. In macrophages, TRNT1 function supports **mitochondrial reprogramming** via the translocator protein **TSPO**, required for antibacterial/antiviral cytokine responses — linking the translational defect to innate-immune dysfunction. ([PMID: 41019077](https://pubmed.ncbi.nlm.nih.gov/41019077/))
5. Compartment-specific consequences → **produce** the clinical manifestations:
   - Erythroid precursor dysfunction → **sideroblastic/microcytic anemia**
   - B-cell maturation arrest at the pro-B/CD19+ stage → **hypogammaglobulinemia / B-cell immunodeficiency** ([PMID: 30758723](https://pubmed.ncbi.nlm.nih.gov/30758723/))
   - TNF-driven inflammation → **periodic fevers**, neutrophilic dermatosis
   - Neuronal/retinal/cochlear vulnerability to oxidative/translational stress → **developmental delay, retinitis pigmentosa, deafness**

### Detail by category

- **Molecular pathways:** tRNA 3′-end maturation (CCA addition) feeding cytosolic and mitochondrial translation; downstream TNF signaling and IFN pathways. GO terms: GO:0001680 (tRNA 3′-terminal CCA addition), GO:0006412 (translation), GO:0032543 (mitochondrial translation).
- **Cellular processes:** impaired autophagy (GO:0006914), oxidative stress response (GO:0006979), inflammatory response (GO:0006954), apoptosis/necrosis of marrow and skin cells seen on EM ([PMID: 29358286](https://pubmed.ncbi.nlm.nih.gov/29358286/)).
- **Protein dysfunction:** reduced thermal stability and catalytic efficiency of mutant TRNT1 (loss of function) ([PMID: 29454993](https://pubmed.ncbi.nlm.nih.gov/29454993/)).
- **Immune involvement:** combined humoral immunodeficiency (B-cell arrest) and autoinflammation. *"Inflammatory cytokines, mainly interleukin (IL)-6, interferon gamma (IFN-γ) and IFN-induced cytokines were elevated in the serum, whereas tumour necrosis factor (TNF) and IL-1β were present in tissue biopsies of patients with active inflammatory disease"* ([PMID: 29358286](https://pubmed.ncbi.nlm.nih.gov/29358286/); [PMID: 30758723](https://pubmed.ncbi.nlm.nih.gov/30758723/)).
- **Subcellular localization:** **mitochondria** (GO:0005739) and **cytosol** (GO:0005829) — dual-compartment defect explains pleiotropy ([PMID: 25193871](https://pubmed.ncbi.nlm.nih.gov/25193871/)).

### Schematic

```
Biallelic hypomorphic TRNT1
        │ (reduced stability/catalysis)
        ▼
 ↓ 3'-CCA addition to tRNAs
        │
   ┌────┴─────────────────────────┐
   ▼                              ▼
Mitochondrial tRNA deficit    Cytosolic tRNA deficit
   │                              │
   ▼                              ▼
Mito dysfunction,            Impaired translation,
oxidative stress,            proteostasis imbalance
impaired autophagy                │
   │                              ▼
   │                      TNF-driven autoinflammation
   │                      (serum IL-6/IFN-γ; tissue TNF/IL-1β)
   └──────────────┬───────────────┘
                  ▼
 Sideroblastic anemia · B-cell immunodeficiency ·
 periodic fevers · developmental delay · RP/cataract ·
 deafness · cardiomyopathy · renal/GI disease
```

---

## 7. Anatomical Structures Affected

**Primary organs / systems:**
- **Hematopoietic/bone marrow** (UBERON:0002371) — erythroid precursors (CL:0000038) → sideroblastic/microcytic anemia with ring sideroblasts.
- **Immune system** — B lymphocytes (CL:0000236), maturation arrest at pro-B/CD19+ stage → hypogammaglobulinemia ([PMID: 30758723](https://pubmed.ncbi.nlm.nih.gov/30758723/)).
- **Nervous system** — brain (UBERON:0000955) and cerebellum (UBERON:0002037) → developmental delay, seizures, cerebellar atrophy.
- **Eye** — retina/photoreceptors (CL:0000210; UBERON:0000966) and lens (UBERON:0000965) → retinitis pigmentosa, cataract.

**Secondary involvement:** gastrointestinal tract (UBERON:0001555) and exocrine pancreas (UBERON:0001263); kidney/renal tubules (UBERON:0001231) → tubulopathy, nephrocalcinosis; heart (UBERON:0000948) → cardiomyopathy; liver/spleen → hepatosplenomegaly; skin (UBERON:0002097) → neutrophilic dermatosis; inner ear/cochlea → sensorineural deafness ([PMID: 27370603](https://pubmed.ncbi.nlm.nih.gov/27370603/); [PMID: 29055896](https://pubmed.ncbi.nlm.nih.gov/29055896/); [PMID: 33332575](https://pubmed.ncbi.nlm.nih.gov/33332575/)).

**Subcellular level:** mitochondria (GO:0005739) and cytosol (GO:0005829), reflecting the tRNA pool in both compartments. **Lateralization:** manifestations (anemia, fevers, developmental delay) are systemic/bilateral.

---

## 8. Temporal Development

**Onset:** Congenital to early-infantile; median age of onset 4 months (range 0–252 months) ([PMID: 35984545](https://pubmed.ncbi.nlm.nih.gov/35984545/)); median age at presentation 2 months in the original cohort ([PMID: 23553769](https://pubmed.ncbi.nlm.nih.gov/23553769/)); mean ~3.0 months ([PMID: 36729249](https://pubmed.ncbi.nlm.nih.gov/36729249/)). Onset pattern is typically **subacute to chronic**, with superimposed **episodic** febrile flares. Severe cases present antenatally as fetal hydrops ([PMID: 29055896](https://pubmed.ncbi.nlm.nih.gov/29055896/)).

**Progression:** Chronic, lifelong, multisystem. Anemia and neurodevelopmental features are **progressive**; fevers are **periodic/relapsing**. Natural history in the original series showed median survival of 48 months with deaths from cardiac or multiorgan failure ([PMID: 23553769](https://pubmed.ncbi.nlm.nih.gov/23553769/)).

**Remission / critical periods:** Spontaneous remission is not characteristic. Treatment-induced control of inflammation (TNF inhibition) and definitive correction of hematologic/immune disease (HSCT) are achievable. Early childhood is the critical window for intervention, given high early mortality in severe genotypes ([PMID: 41795040](https://pubmed.ncbi.nlm.nih.gov/41795040/); [PMID: 23553769](https://pubmed.ncbi.nlm.nih.gov/23553769/)).

---

## 9. Inheritance and Population

**Inheritance:** **Autosomal recessive**; both homozygous (consanguineous families) and compound heterozygous (non-consanguineous) genotypes are reported ([PMID: 25193871](https://pubmed.ncbi.nlm.nih.gov/25193871/); [PMID: 36729249](https://pubmed.ncbi.nlm.nih.gov/36729249/)). **Penetrance** is effectively complete for biallelic hypomorphic genotypes; **expressivity is variable**, graded by residual enzyme activity (full SIFD ↔ isolated RP with microcytosis). No genetic anticipation (not a repeat-expansion disorder); germline mosaicism and founder effects are not established.

**Epidemiology:** Ultra-rare — the entire world literature comprises roughly **58–75+ described patients**; one systematic review noted *"The search identified 29 publications describing 58 unique patients"* ([PMID: 35984545](https://pubmed.ncbi.nlm.nih.gov/35984545/); [PMID: 41795040](https://pubmed.ncbi.nlm.nih.gov/41795040/)). Population prevalence/incidence estimates are not formally established. The disorder is **pan-ethnic** (European, Chinese, Japanese, Middle Eastern populations all reported). **Sex ratio** is ~1:1: *"The male: female ratio was 1: 1, and the mean age of onset was 3.0 months"* ([PMID: 36729249](https://pubmed.ncbi.nlm.nih.gov/36729249/)). **Consanguinity** contributes to homozygous cases. **Carrier frequency** is undefined but presumed very low.

---

## 10. Diagnostics

**Genetic testing (definitive):** Diagnosis is established by **whole-exome or whole-genome sequencing** identifying biallelic TRNT1 variants, confirmed by Sanger segregation ([PMID: 25193871](https://pubmed.ncbi.nlm.nih.gov/25193871/); [PMID: 34625936](https://pubmed.ncbi.nlm.nih.gov/34625936/); [PMID: 42830586](https://pubmed.ncbi.nlm.nih.gov/42830586/)). Single-gene testing and sideroblastic-anemia/immunodeficiency gene panels including TRNT1 are also used. The recurrent hot-spot **c.668T>C (p.Ile223Thr)** should be specifically sought given its prognostic weight.

**Supportive laboratory findings:**
- Microcytic/sideroblastic anemia with **ring sideroblasts** on bone-marrow iron (Prussian blue) staining; low hemoglobin (median 7.1 g/dL) and low MCV (median 62.0 fL) in the original cohort ([PMID: 23553769](https://pubmed.ncbi.nlm.nih.gov/23553769/)).
- **B lymphopenia** (CD19+ 0.016–0.22 ×10⁹/L) and **panhypogammaglobulinemia** ([PMID: 23553769](https://pubmed.ncbi.nlm.nih.gov/23553769/); [PMID: 30758723](https://pubmed.ncbi.nlm.nih.gov/30758723/)).
- Elevated inflammatory markers (CRP, ferritin, IL-6) during febrile episodes; electrolyte imbalance during crises ([PMID: 27370603](https://pubmed.ncbi.nlm.nih.gov/27370603/); [PMID: 29358286](https://pubmed.ncbi.nlm.nih.gov/29358286/)).

**Functional/research assays:** CCA-addition assays and deep tRNA sequencing in patient fibroblasts demonstrate the molecular defect — *"Deep tRNA sequencing of patients' fibroblasts showed significant deficiency of mature cytosolic tRNAs"* ([PMID: 29358286](https://pubmed.ncbi.nlm.nih.gov/29358286/)); and *"functional perturbation of 3' CCA addition to mitochondrial tRNAs (tRNA(Cys), tRNA(LeuUUR) and tRNA(His)) in fibroblasts"* ([PMID: 27370603](https://pubmed.ncbi.nlm.nih.gov/27370603/)).

**Differential diagnosis:** Other congenital sideroblastic anemias (e.g., ALAS2/X-linked, SLC25A38, mitochondrial/Pearson syndrome), other autoinflammatory periodic fever syndromes, and primary humoral immunodeficiencies — distinguished by the characteristic SIFD tetrad and biallelic TRNT1 genotype ([PMID: 25193871](https://pubmed.ncbi.nlm.nih.gov/25193871/)).

**Screening:** Cascade genetic testing of at-risk relatives and prenatal/preimplantation genetic testing are available once the familial variants are known. No population newborn screening exists.

---

## 11. Outcome / Prognosis

**Survival:** The largest systematic review (75 patients) reported *"The estimated 2-, 5-, and 10-year Kaplan–Meier survival probabilities for all patients were 88.45%, 76.67%, 68.84% for all patients"* ([PMID: 41795040](https://pubmed.ncbi.nlm.nih.gov/41795040/)). Survival was markedly worse for onset ≤3 months (82.40% / 58.86% / 44.85%) and for patients with seizures (70% / 40% / 26.68%; log-rank P<0.05). An earlier review estimated *"the mortality in cases of SIFD was approximately 44% (14/32)"* ([PMID: 34310935](https://pubmed.ncbi.nlm.nih.gov/34310935/)), and the original cohort had a median survival of 48 months ([PMID: 23553769](https://pubmed.ncbi.nlm.nih.gov/23553769/)).

**Adverse prognostic factors:** *"younger age of onset of ≤ 3 months, seizures, and decreased B-cell count"* ([PMID: 41795040](https://pubmed.ncbi.nlm.nih.gov/41795040/)). The hot-spot genotype is lethality-associated: *"about 79% of individuals who died carried the hot-spot mutation c.668 T > C"* ([PMID: 34310935](https://pubmed.ncbi.nlm.nih.gov/34310935/)).

**Causes of death:** *"Median survival was 48 months, with 7 deaths caused by cardiac or multiorgan failure"* ([PMID: 23553769](https://pubmed.ncbi.nlm.nih.gov/23553769/)).

**Morbidity:** Transfusion dependence with iron overload, developmental disability, visual and hearing loss, and recurrent infection contribute to high morbidity. Definitive HSCT can cure the hematologic/immune disease but does not reverse established neurologic/sensory deficits.

---

## 12. Treatment

**Supportive care (foundational):** *"Acute management of these patients included transfusion for anaemia, fluid and electrolyte replacement and immunoglobulin therapy"* ([PMID: 27370603](https://pubmed.ncbi.nlm.nih.gov/27370603/)). Iron chelation is required for transfusional iron overload; immunoglobulin (IVIG/SCIG) replacement treats hypogammaglobulinemia ([PMID: 23553769](https://pubmed.ncbi.nlm.nih.gov/23553769/)). NCIT: Blood Transfusion; Intravenous Immunoglobulin Therapy; Iron Chelation Therapy.

**Anti-inflammatory / targeted (TNF inhibition — NCIT: Tumor Necrosis Factor Inhibitor):** TNF-α inhibitors control the autoinflammatory component where IVIG fails. In the mechanistic study, *"In 4/4 patients, treatment with a TNF inhibitor suppressed inflammation, reduced the need for blood transfusions and improved growth"* ([PMID: 29358286](https://pubmed.ncbi.nlm.nih.gov/29358286/)). Case reports confirm **etanercept**: *"her condition stabilized with etanercept (a tumor necrosis factor [TNF] inhibitor) and corticosteroids therapy"* ([PMID: 41795040](https://pubmed.ncbi.nlm.nih.gov/41795040/); [PMID: 36121781](https://pubmed.ncbi.nlm.nih.gov/36121781/)). **Thalidomide** is an effective alternative: *"Adalimumab was discontinued and replaced with thalidomide, which controlled the periodic fever and normalized inflammatory markers effectively"* ([PMID: 36729249](https://pubmed.ncbi.nlm.nih.gov/36729249/)).

**Curative therapy (NCIT: Allogeneic Hematopoietic Stem Cell Transplantation):** Allogeneic HSCT can correct the hematologic and immunologic disease. In the original series, *"One child underwent bone marrow transplantation aged 9 months, with apparent cure of the hematologic and immunologic manifestations"* ([PMID: 23553769](https://pubmed.ncbi.nlm.nih.gov/23553769/)); HSCT has since been applied for severe disease ([PMID: 41795040](https://pubmed.ncbi.nlm.nih.gov/41795040/)).

**Treatment strategy:** A rational algorithm is (1) supportive care (transfusion, chelation, IVIG) + (2) TNF inhibition for autoinflammation + (3) consideration of allogeneic HSCT for severe hematologic/immune disease, ideally before irreversible organ damage. No approved gene therapy, RNA-based therapy, or pharmacogenomic guidance currently exists; treatment is not genotype-tailored beyond prognostic risk stratification.

---

## 13. Prevention

Because SIFD is monogenic, prevention is **genetic rather than public-health**:
- **Genetic counseling** for autosomal-recessive 25% recurrence risk in carrier couples.
- **Carrier testing** of relatives and **prenatal / preimplantation genetic testing** once familial TRNT1 variants are known.
- **Secondary prevention** within affected individuals: early TNF inhibition and IVIG to prevent inflammatory and infectious complications; chelation to prevent iron-overload organ damage; audiology/ophthalmology surveillance for early detection of sensory loss.

No primary prevention (vaccination, lifestyle) applies to disease occurrence; standard childhood immunization and infection prophylaxis are advisable given immunodeficiency. *Population screening and environmental interventions are not applicable.*

---

## 14. Other Species / Natural Disease

TRNT1 is evolutionarily conserved; the CCA-adding enzyme has orthologs across eukaryotes, including the budding-yeast gene **CCA1** (*Saccharomyces cerevisiae*, NCBI:txid4932), which functionally complements human TRNT1 and was used to validate pathogenic variants ([PMID: 25193871](https://pubmed.ncbi.nlm.nih.gov/25193871/)). A mouse ortholog (*Trnt1*) exists. **No naturally occurring SIFD-equivalent disease** in companion animals or wildlife has been documented in OMIA, and there is no zoonotic or cross-species transmission (genetic disorder). Comparative value lies in the deep conservation of tRNA CCA-addition machinery, which underpins model-organism complementation studies.

---

## 15. Model Organisms

| Model | System | Key findings | PMID |
|---|---|---|---|
| **Budding yeast** (CCA1-null complementation) | *S. cerevisiae* (NCBI:txid4932) | Confirmed patient variants cause **partial LOF** and dual mito/cytosolic metabolic defects | [25193871](https://pubmed.ncbi.nlm.nih.gov/25193871/) |
| **Patient iPSC-derived retinal organoids** | In vitro human | Reduced full-length TRNT1, autophagy deficit (LC3-II accumulation), elevated oxidative stress | [28390992](https://pubmed.ncbi.nlm.nih.gov/28390992/) |
| **Patient-derived intestinal epithelial organoids** | In vitro human (monogenic IBD panel) | TRNT1 included among early-onset IBD drivers; epithelial phenotyping | [41273131](https://pubmed.ncbi.nlm.nih.gov/41273131/); [40666956](https://pubmed.ncbi.nlm.nih.gov/40666956/) |
| **RAW264.7 macrophages (siRNA knockdown)** | Murine cell line | TRNT1 knockdown impairs LPS/Poly(I:C) cytokine responses via TSPO-dependent mitochondrial reprogramming | [41019077](https://pubmed.ncbi.nlm.nih.gov/41019077/) |
| **Patient fibroblasts** | In vitro human | Deep tRNA-seq (cytosolic tRNA deficiency); CCA-addition assays (mt-tRNA defect) | [29358286](https://pubmed.ncbi.nlm.nih.gov/29358286/); [27370603](https://pubmed.ncbi.nlm.nih.gov/27370603/); [37239403](https://pubmed.ncbi.nlm.nih.gov/37239403/) |

**Phenotype recapitulation & limitations:** The yeast model captures the enzymatic/metabolic defect but not the multisystem phenotype — *"Using budding yeast lacking the TRNT1 homolog, CCA1, we confirm that the patient-associated TRNT1 mutations result in partial loss of function"* ([PMID: 25193871](https://pubmed.ncbi.nlm.nih.gov/25193871/)). iPSC-retinal organoids reproduce retinal/autophagy/oxidative pathology ([PMID: 28390992](https://pubmed.ncbi.nlm.nih.gov/28390992/)); macrophage knockdown models the innate-immune defect ([PMID: 41019077](https://pubmed.ncbi.nlm.nih.gov/41019077/)). **No complete-knockout mammalian model exists because complete loss of TRNT1 is lethal** — a hypomorphic/conditional mouse would be needed to model the systemic disease. These complementary systems together illuminate distinct facets of the pathophysiology.

---

## Evidence Base

| PMID | Study | Contribution |
|---|---|---|
| [23553769](https://pubmed.ncbi.nlm.nih.gov/23553769/) | Wiseman 2013, *J Exp Med* | Original clinical delineation (12 cases); natural history, 48-mo median survival, BMT curative for hematologic/immune disease |
| [25193871](https://pubmed.ncbi.nlm.nih.gov/25193871/) | Chakraborty 2014, *Blood* | Landmark gene discovery; biallelic TRNT1, partial LOF, yeast complementation, dual-compartment defect |
| [29358286](https://pubmed.ncbi.nlm.nih.gov/29358286/) | Giannelou 2018 | TNF-driven autoinflammation; cytosolic tRNA deficiency; TNF inhibitor efficacy (4/4) |
| [28390992](https://pubmed.ncbi.nlm.nih.gov/28390992/) | iPSC retinal organoids | Autophagy deficit + oxidative stress downstream of TRNT1 deficiency |
| [27370603](https://pubmed.ncbi.nlm.nih.gov/27370603/) | TRNT1 deficiency clinical/biochemical | mt-tRNA CCA-addition defect in patient fibroblasts; supportive-care measures |
| [29454993](https://pubmed.ncbi.nlm.nih.gov/29454993/) | In vitro variant study | Mutant protein instability/altered catalysis (T154I, M158V, L166S, R190I, I223T) |
| [35984545](https://pubmed.ncbi.nlm.nih.gov/35984545/) | Systematic review (58 patients) | Phenotype frequencies; median onset 4 months |
| [41795040](https://pubmed.ncbi.nlm.nih.gov/41795040/) | Systematic review (75 patients) | Survival statistics; adverse prognostic factors; TNF inhibitor/HSCT |
| [34310935](https://pubmed.ncbi.nlm.nih.gov/34310935/) | Chinese case report/review | Mortality ~44%; c.668T>C lethality association |
| [36729249](https://pubmed.ncbi.nlm.nih.gov/36729249/) | Thalidomide case | Thalidomide efficacy; 1:1 sex ratio; mean onset 3.0 months |
| [30758723](https://pubmed.ncbi.nlm.nih.gov/30758723/) | Atypical SIFD | B-cell maturation arrest at pro-B/CD19+ stage |
| [41019077](https://pubmed.ncbi.nlm.nih.gov/41019077/) | Macrophage/TSPO study | Innate-immune mechanism via TSPO-dependent mitochondrial reprogramming |
| [37239403](https://pubmed.ncbi.nlm.nih.gov/37239403/) | TRNT1 proteostasis | Loss of tRNA integrity and protein imbalance |
| [32471101](https://pubmed.ncbi.nlm.nih.gov/32471101/) | Review of CCA-addition defects | Essential enzyme function; allelic phenotypic spectrum |
| [29055896](https://pubmed.ncbi.nlm.nih.gov/29055896/) | Fetal hydrops report | Expands phenotype to antenatal severe presentation |
| [33332575](https://pubmed.ncbi.nlm.nih.gov/33332575/) | Neutrophilic dermatosis | New skin manifestation; novel variant |
| [42830586](https://pubmed.ncbi.nlm.nih.gov/42830586/) | RP + microcytosis | Milder hypomorphic-allele phenotype end of spectrum |
| [34625936](https://pubmed.ncbi.nlm.nih.gov/34625936/) | Novel compound-het case | ACMG variant classification example |

---

## Limitations and Knowledge Gaps

1. **Ultra-rare disease / small-N evidence.** All epidemiologic and prognostic estimates derive from pooled case reports and systematic reviews (≤75 patients), introducing ascertainment and publication bias toward severe cases; true prevalence, incidence, and carrier frequency are unknown.
2. **No whole-organism mammalian disease model.** Because complete TRNT1 loss is lethal, there is no knockout mouse recapitulating systemic SIFD; a hypomorphic/conditional model is lacking, limiting in vivo mechanistic and therapeutic testing.
3. **Incomplete genotype–phenotype map.** While c.668T>C is clearly severe, residual-activity thresholds that separate full SIFD from isolated RP/microcytosis are not quantitatively defined for most allele pairs.
4. **Mechanism of tissue specificity is unresolved.** Why a ubiquitous tRNA-maturation defect preferentially injures erythroid precursors, B cells, neurons, and photoreceptors remains inferential.
5. **Limited long-term outcome and QoL data.** No standardized QoL instruments, and long-term post-HSCT neurologic/sensory outcomes are sparsely reported.
6. **No disease-specific pharmacogenomics or gene therapy** is yet available.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international SIFD/TRNT1 registry** with standardized genotype, phenotype, treatment, and survival data to replace pooled case-report inference with prospective natural-history analysis.
2. **Generate a hypomorphic or conditional Trnt1 mouse** to model systemic disease, test TNF-inhibition timing, and evaluate gene/RNA-based therapies in vivo.
3. **Quantitative enzyme–phenotype correlation:** systematically measure residual CCA-adding activity and thermal stability for all reported variants in vitro to build a predictive severity model useful for counseling.
4. **Dissect tissue-selective vulnerability** using patient iPSC-derived erythroid, B-lymphoid, and neuronal lineages to define which cell types depend most on TRNT1 and why.
5. **Prospective trial of TNF inhibitors ± HSCT** with predefined response/survival endpoints, and biomarker monitoring (IL-6, IFN-γ, tissue TNF/IL-1β) to formalize the empirically effective regimen.
6. **Explore TSPO-targeted or mitochondrial/antioxidant adjuncts** suggested by the macrophage and retinal-organoid mechanistic work ([PMID: 41019077](https://pubmed.ncbi.nlm.nih.gov/41019077/); [PMID: 28390992](https://pubmed.ncbi.nlm.nih.gov/28390992/)).

---

*Report compiled from 26 reviewed publications and 11 confirmed findings. Evidence source types span human clinical (case series/systematic reviews), in vitro (patient fibroblasts, iPSC organoids, enzymology), and model-organism (yeast complementation, murine macrophage knockdown) studies.*


## Artifacts

- [OpenScientist final report](Sideroblastic_Anemia_B-Cell_Immunodeficiency_Periodic_Fevers_and_Developmental_Delay-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Sideroblastic_Anemia_B-Cell_Immunodeficiency_Periodic_Fevers_and_Developmental_Delay-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 21 |
| On topic | 21 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 44 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 15 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014487` (2 mentions) - the report calls it "MONDO"; MONDO calls it **congenital sideroblastic anemia-B-cell immunodeficiency-periodic fever-developmental delay syndrome**
- `HP:0011368` (1 mention) - the report calls it "dermatological manifestation"; HP calls it **Epidermal thickening**
- `GO:0006914` (1 mention) - the report calls it "Cellular processes:** impaired autophagy"; GO calls it **autophagy**
- `GO:0005739` (2 mentions) - the report calls it "mitochondria", "Subcellular localization:** **mitochondria"; GO calls it **mitochondrion**
- `UBERON:0000955` (1 mention) - the report calls it "Nervous system** — brain"; UBERON calls it **brain**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0011024` (1 mention) - the report calls it "GI tract abnormality"; HP calls it **Abnormality of the gastrointestinal tract**, and lists "Abnormality of the GI tract" among its other names
- `UBERON:0002371` (1 mention) - the report calls it "Hematopoietic/bone marrow"; UBERON calls it **bone marrow**
- `CL:0000236` (1 mention) - the report calls it "Immune system** — B lymphocytes"; CL calls it **B cell**, and lists "B lymphocyte" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005739` - called "mitochondria", "Subcellular localization:** **mitochondria"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.