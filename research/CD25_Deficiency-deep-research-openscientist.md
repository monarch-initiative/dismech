---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-24T19:27:21.818706'
end_time: '2026-09-24T19:40:38.276248'
duration_seconds: 796.46
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: CD25 Deficiency
  mondo_id: MONDO:0011664
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
citation_count: 16
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 17
  quotes_valid: 13
  quotes_unsupported: 4
  unsupported_quote_references:
  - PMID:9096364
  - PMID:17196245
  - PMID:30742970
  relevance_assessed: 16
  on_topic: 9
  needs_review: true
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 47
  verified: 45
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 7
  labels_mismatched: 13
  mislabelled_terms:
  - term_id: MONDO:0011664
    reported_labels:
    - MONDO
    ontology_label: immunodeficiency due to CD25 deficiency
  - term_id: HP:0001508
    reported_labels:
    - Physical
    ontology_label: Failure to thrive
  - term_id: HP:0002205
    reported_labels:
    - Sign
    ontology_label: Recurrent respiratory infections
  - term_id: HP:0000964
    reported_labels:
    - Physical
    ontology_label: Eczematoid dermatitis
  - term_id: HP:0002608
    reported_labels:
    - Lab/clinical
    ontology_label: Celiac disease
  - term_id: HP:0100646
    reported_labels:
    - Lab/clinical
    ontology_label: Thyroiditis
  - term_id: HP:0001890
    reported_labels:
    - Lab
    ontology_label: Autoimmune hemolytic anemia
  - term_id: HP:0002716
    reported_labels:
    - Sign
    ontology_label: Lymphadenopathy
  - term_id: HP:0001433
    reported_labels:
    - Sign
    ontology_label: Hepatosplenomegaly
  - term_id: HP:0006538
    reported_labels:
    - Clinical
    ontology_label: Recurrent bronchopulmonary infections
  - term_id: HP:0002850
    reported_labels:
    - Lab
    ontology_label: Decreased circulating IgM concentration
  - term_id: HP:0010702
    reported_labels:
    - Lab
    ontology_label: Increased circulating immunoglobulin concentration
  - term_id: UBERON:0000964
    reported_labels:
    - Lacrimal/ocular surface & cornea
    ontology_label: cornea
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
  path: CD25_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: CD25_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CD25 Deficiency
- **MONDO ID:** MONDO:0011664 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CD25 Deficiency** covering all of the
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

# CD25 Deficiency (IL2RA Deficiency): A Comprehensive Disease Characteristics Report

**Disease Name:** CD25 Deficiency (Immunodeficiency 41 with lymphoproliferation and autoimmunity, IMD41)
**MONDO ID:** MONDO:0011664
**Category:** Mendelian (monogenic inborn error of immunity)

---

## Summary

CD25 deficiency is an **ultra-rare autosomal recessive inborn error of immunity** caused by biallelic loss-of-function variants in **IL2RA** (chromosome 10p15.1), the gene encoding CD25, the alpha chain of the high-affinity interleukin-2 (IL-2) receptor. CD25, in complex with CD122 (IL-2Rβ) and the common gamma chain (γc), confers high-affinity IL-2 binding. Loss of this chain abolishes high-affinity IL-2/JAK1-JAK3/STAT5 signaling, which is indispensable for the development, survival, stability, and suppressive function of FOXP3⁺ regulatory T cells (Tregs) and for normal IL-10 production. The resulting failure of peripheral immune tolerance produces an **IPEX-like syndrome** that paradoxically combines features of immunodeficiency (recurrent viral, bacterial, and fungal infections) with early-childhood **autoimmunity and lymphoproliferation** (autoimmune enteropathy, hepatitis, thyroiditis, cytopenias, eczema, multi-organ lymphocytic infiltration, and severe failure to thrive).

The disorder was first described by Sharfe et al. in 1997 as a truncation mutation of the IL-2 receptor alpha chain producing profound cellular immunodeficiency with extensive lymphocytic tissue infiltration. Fewer than ~15 molecularly confirmed cases have been reported worldwide as of 2026, so essentially all knowledge derives from **individual patient case reports** rather than aggregated registries; no population prevalence or incidence estimate is established. Diagnosis rests on demonstrating **absent surface CD25** on T cells by flow cytometry, followed by **IL2RA sequencing** for molecular confirmation. The differential diagnosis centers on IPEX (FOXP3) and other IPEX-like Tregopathies.

Without definitive treatment the disease is severe and often fatal in early childhood from overwhelming infection or autoimmune organ damage. **Allogeneic hematopoietic stem cell transplantation (HSCT)** is the only curative therapy, restoring functional Tregs, and can produce complete resolution of symptoms. **Rapamycin (sirolimus)**, an mTOR inhibitor that favors Tregs, has been used as effective and safe bridging immunomodulation. Because the disorder is Mendelian, prevention is limited to genetic counseling, cascade carrier testing (especially in consanguineous families), and prenatal/preimplantation genetic testing once the familial variant is known. Mouse models (Il2⁻/⁻ and Il2ra/CD25 knockout) recapitulate the human phenotype and demonstrate genetic-background-dependent modifier effects.

---

## 1. Disease Information

**Overview.** CD25 deficiency is a monogenic, autosomal recessive inborn error of immunity in which loss of the IL-2 receptor alpha chain (CD25) disables high-affinity IL-2 signaling and thereby cripples regulatory T-cell function. The clinical picture is described as "IPEX-like" because it phenocopies IPEX (Immune dysregulation, Polyendocrinopathy, Enteropathy, X-linked syndrome) caused by FOXP3 mutations, but with a normal FOXP3 gene. Sharfe et al. (1997) described "a novel human immune aberration arising from a truncation mutation of the interleukin-2 receptor alpha chain (CD25)… characterized by decreased numbers of peripheral T cells displaying abnormal proliferation but normal B cell development. Extensive lymphocytic infiltration of tissues, including lung, liver, gut, and bone, is observed, accompanied by tissue atrophy and inflammation" ([PMID: 9096364](https://pubmed.ncbi.nlm.nih.gov/9096364/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0011664 |
| OMIM (phenotype) | #606367 — IMMUNODEFICIENCY 41 WITH LYMPHOPROLIFERATION AND AUTOIMMUNITY (IMD41) |
| OMIM (gene) | *147730 (IL2RA) |
| Orphanet | ORPHA:169153 — Immunodeficiency due to a defect in CD25 |
| HGNC (gene) | HGNC:6008 (IL2RA) |
| NCBI Gene | 3559 |
| UniProt | P01589 |
| Chromosome | 10p15.1 |
| ICD-10 | D81.8 / D84.9 (immunodeficiency range) |
| MeSH | via "Interleukin-2 Receptor alpha Subunit" |

**Synonyms / alternative names.** IL2RA deficiency; interleukin-2 receptor alpha chain deficiency; CD25 deficiency syndrome; Immunodeficiency 41 with lymphoproliferation and autoimmunity (IMD41); IPEX-like syndrome due to CD25 deficiency.

**Data provenance.** Because only ~13 molecularly confirmed cases had been reported worldwide as of 2026 ([PMID: 41659858](https://pubmed.ncbi.nlm.nih.gov/41659858/)), disease-level knowledge derives almost entirely from **individual patient case reports and small case series**, not from aggregated EHR/registry resources.

---

## 2. Etiology

**Causal factors.** CD25 deficiency is **purely genetic** — caused by biallelic (homozygous or compound heterozygous) germline loss-of-function variants in *IL2RA*. There is no environmental, toxic, occupational, or lifestyle cause. Loss-of-function IL2RA variants "cause a very rare autosomal recessive disorder marked by early-onset autoimmunity and recurrent infections with an IPEX-like presentation" ([PMID: 41694357](https://pubmed.ncbi.nlm.nih.gov/41694357/)).

**Genetic risk factors.** The only causal risk factor is inheriting two defective *IL2RA* alleles. The principal **population risk factor is parental consanguinity** — reported patients are frequently born to first-cousin parents ("Both patients were born to first-cousin parents," [PMID: 41694357](https://pubmed.ncbi.nlm.nih.gov/41694357/)), consistent with a recessive disorder concentrated in inbred pedigrees.

**Environmental / lifestyle risk factors.** None are causal. Infections act as **triggers and complications** of the underlying immunodeficiency rather than as causes.

**Protective factors.** No genetic or environmental protective factors are established. Because the disease is Mendelian and fully penetrant when biallelic LOF variants are present, "protection" is effectively the absence of a second pathogenic allele (carriers are healthy).

**Gene–environment interactions.** In humans these are not well characterized owing to case rarity. However, mouse models demonstrate a clear **modifier / gene–environment interaction**: Il2⁻/⁻ mice develop ulcerative-colitis-like disease on a mixed 129/Ola × C57BL/6 background but generalized systemic autoimmunity when backcrossed to BALB/c, showing that genetic background dictates the phenotype ([PMID: 9065030](https://pubmed.ncbi.nlm.nih.gov/9065030/)). Gut microbial antigens are inferred to drive the autoimmune enteropathy.

**Important distinction — Mendelian LOF disease vs. common autoimmune-susceptibility polymorphisms.** The rare Mendelian CD25 deficiency is mechanistically distinct from the well-established role of **common non-coding IL2RA regulatory polymorphisms** (e.g., rs2104286, rs12722495/rs12722496, rs41295061, rs7093069) as **polygenic susceptibility loci** for type 1 diabetes, multiple sclerosis, and autoimmune thyroid disease. Fine-mapping identified multiple independent T1D and MS association signals in the IL2RA/CD25 region ([PMID: 26106896](https://pubmed.ncbi.nlm.nih.gov/26106896/)); IL2RA-rs41295061 (10p15) association was replicated in T1D ([PMID: 21875375](https://pubmed.ncbi.nlm.nih.gov/21875375/)); and IL-2RA rs7093069 (TT genotype) was associated with pediatric autoimmune thyroid disease ([PMID: 33193078](https://pubmed.ncbi.nlm.nih.gov/33193078/)). These common variants subtly tune CD25 expression and confer complex-trait autoimmune risk, whereas the rare biallelic LOF variants abolish CD25 entirely and cause the monogenic syndrome.

---

## 3. Phenotypes

Phenotypes are curated from reported cases ([PMID: 9096364](https://pubmed.ncbi.nlm.nih.gov/9096364/), [17196245](https://pubmed.ncbi.nlm.nih.gov/17196245/), [23416241](https://pubmed.ncbi.nlm.nih.gov/23416241/), [24116927](https://pubmed.ncbi.nlm.nih.gov/24116927/), [29252577](https://pubmed.ncbi.nlm.nih.gov/29252577/), [30742970](https://pubmed.ncbi.nlm.nih.gov/30742970/), [41694357](https://pubmed.ncbi.nlm.nih.gov/41694357/), [41659858](https://pubmed.ncbi.nlm.nih.gov/41659858/)). Because fewer than ~15 cases exist, frequencies are **qualitative** (most/common) rather than precise percentages. Onset is typically **neonatal to early childhood** (congenital/pediatric); severity is **severe**; the course is **chronic and progressive** without treatment.

| Phenotype | Type | Suggested HPO term | Frequency (qualitative) |
|---|---|---|---|
| Chronic diarrhea / autoimmune (celiac-like) enteropathy | Sign / GI | HP:0002028; HP:0002590 | Majority |
| Failure to thrive / growth failure | Physical | HP:0001508 | Majority |
| Recurrent respiratory infections | Sign | HP:0002205 | Majority |
| Recurrent bacterial/viral/fungal infections | Sign | HP:0002719; HP:0002841 | Majority |
| Eczema / dermatitis | Physical | HP:0000964 | Common |
| Autoimmune hepatitis | Lab/clinical | HP:0002608 | Common |
| Autoimmune thyroiditis | Lab/clinical | HP:0100646 | Reported (≥1 case) |
| Autoimmune hemolytic anemia / cytopenias | Lab | HP:0001890 | Reported |
| Lymphadenopathy / lymphoproliferation | Sign | HP:0002716 | Common |
| Hepatosplenomegaly | Sign | HP:0001433 | Common |
| Chronic inflammatory lung disease / follicular bronchiolitis | Clinical | HP:0006538 | Reported |
| Keratitis / severe dry eye (ocular surface disease) | Clinical | HP:0000491; HP:0000492 | Reported |
| Impaired T-cell proliferation | Lab | HP:0002850 | Majority |
| Hypergammaglobulinemia | Lab | HP:0010702 | Common |
| Absent CD25 surface expression | Lab | (diagnostic) | Universal |

Key supporting quotes: patients "presented in early childhood with recurrent respiratory and gastrointestinal infections, severe failure to thrive, chronic diarrhea with celiac-like enteropathy, and autoimmune manifestations including autoimmune hepatitis, dermatitis, and, in one case, autoimmune thyroiditis" ([PMID: 41694357](https://pubmed.ncbi.nlm.nih.gov/41694357/)); "Recurrent infections and lymphocyte infiltration of multiple tissues are the main clinical presentations" ([PMID: 29252577](https://pubmed.ncbi.nlm.nih.gov/29252577/)). Primary biliary cirrhosis has also been reported, notably as a rare pediatric occurrence ([PMID: 24116927](https://pubmed.ncbi.nlm.nih.gov/24116927/), [PMID: 20650610](https://pubmed.ncbi.nlm.nih.gov/20650610/)).

**Quality of life.** No formal EQ-5D/SF-36/PROMIS data exist for this ultra-rare disease. Qualitatively, untreated disease imposes profound impairment: chronic diarrhea and malabsorption, failure to thrive, repeated hospitalizations for infection, autoimmune organ damage, and severe dry-eye discomfort all severely reduce daily functioning. Successful HSCT can restore near-normal functioning.

---

## 4. Genetic / Molecular Information

**Causal gene.** *IL2RA* (HGNC:6008; OMIM *147730; NCBI Gene 3559; UniProt P01589), located on chromosome **10p15.1**, encoding CD25, the 55-kDa alpha chain of the IL-2 receptor.

**Pathogenic variants.** Reported disease-causing variants are biallelic and loss-of-function, spanning:
- **Nonsense/truncation** variants (the original Sharfe et al. 1997 case, [PMID: 9096364](https://pubmed.ncbi.nlm.nih.gov/9096364/)).
- **Missense** variants causing conformational loss of surface expression — e.g., c.122A>C, p.Tyr41Ser (Y41S), a homozygous missense mutation with no CD25 on CD4⁺ T cells and extremely low Tregs ([PMID: 24116927](https://pubmed.ncbi.nlm.nih.gov/24116927/)); and a conformational mutation described as "a severe protein conformational alteration that abrogates its cell surface expression" ([PMID: 30742970](https://pubmed.ncbi.nlm.nih.gov/30742970/)).

**Variant classification.** Reported variants are classified **pathogenic/likely pathogenic** per ACMG/AMP criteria (functional evidence of absent surface expression, segregation in consanguineous families, absence/rarity in population databases).

**Allele frequency.** Causal LOF variants are private/ultra-rare and essentially absent from gnomAD at appreciable frequency. By contrast, common regulatory SNPs in the locus are polymorphic (see Section 2).

**Origin.** **Germline**, biallelic. No somatic mechanism.

**Functional consequence.** **Loss of function** — loss of high-affinity IL-2 binding. CD25 "contributes only to IL-2 binding affinity but not to the recruitment of signalling molecules" ([PMID: 24116927](https://pubmed.ncbi.nlm.nih.gov/24116927/)), so its loss reduces IL-2 receptor affinity rather than eliminating all IL-2 signaling capacity, but this is sufficient to cripple Treg biology.

**Modifier genes.** Not defined in humans. Mouse background effects (129 vs BALB/c) demonstrate strong modifier influence ([PMID: 9065030](https://pubmed.ncbi.nlm.nih.gov/9065030/)). Related Treg biology implicates FOXP1/FOXP4, which bind Il2ra promoter regions to regulate CD25 expression ([PMID: 40794436](https://pubmed.ncbi.nlm.nih.gov/40794436/)).

**Epigenetic information.** No disease-specific methylation/histone data. FOXP1/FOXP4 transcriptional control of the Il2ra promoter is the most relevant regulatory layer ([PMID: 40794436](https://pubmed.ncbi.nlm.nih.gov/40794436/)).

**Chromosomal abnormalities.** None — this is a single-gene disorder, not a structural/aneuploidy syndrome.

---

## 5. Environmental Information

- **Environmental factors:** None causal. No toxin, radiation, pollution, or occupational exposure contributes to disease onset.
- **Lifestyle factors:** Not applicable (disease presents in infancy).
- **Infectious agents:** Pathogens act as **triggers/complications**, not causes. Patients suffer recurrent **viral (including CMV/herpesviruses), bacterial, and fungal (Candida)** infections due to the immunodeficiency. Gut microbial antigens are inferred to drive autoimmune enteropathy (by analogy to IL-2-pathway mouse colitis, [PMID: 9065030](https://pubmed.ncbi.nlm.nih.gov/9065030/)).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function variants in *IL2RA*** (nonsense/truncation or conformational missense) **lead to** absent or non-functional CD25 protein at the T-cell plasma membrane ([PMID: 9096364](https://pubmed.ncbi.nlm.nih.gov/9096364/), [30742970](https://pubmed.ncbi.nlm.nih.gov/30742970/)).
2. Loss of CD25 **results in** failure to assemble the high-affinity IL-2 receptor (CD25 + CD122 + γc), abolishing high-affinity IL-2 binding ([PMID: 19348914](https://pubmed.ncbi.nlm.nih.gov/19348914/)).
3. Loss of high-affinity IL-2 binding **leads to** deficient JAK1/JAK3 → STAT5 phosphorylation in T cells (*inferred from IL-2 receptor signaling biology*; reduced pSTAT5 is used functionally in diagnosis).
4. Deficient STAT5 signaling **results in** impaired FOXP3⁺ regulatory T-cell development, survival, stability, and suppressive function, and **impaired IL-10 production** by CD4 lymphocytes ([PMID: 17196245](https://pubmed.ncbi.nlm.nih.gov/17196245/), [19348914](https://pubmed.ncbi.nlm.nih.gov/19348914/)).
5. Treg failure **leads to** loss of peripheral immune tolerance, which **branches** into two co-existing outcomes:
   - **Branch A — Autoimmunity/lymphoproliferation:** uncontrolled activation and expansion of autoreactive effector T cells (notably CD8⁺STAT5⁺ cytotoxic T cells) **results in** multi-organ lymphocytic infiltration, autoimmune enteropathy, hepatitis, thyroiditis, cytopenias, and lymphadenopathy ([PMID: 23416241](https://pubmed.ncbi.nlm.nih.gov/23416241/), [9096364](https://pubmed.ncbi.nlm.nih.gov/9096364/)).
   - **Branch B — Immunodeficiency:** impaired antigen-specific T-cell responses **result in** susceptibility to recurrent viral, bacterial, and fungal infections ([PMID: 23416241](https://pubmed.ncbi.nlm.nih.gov/23416241/)).
6. Combined tissue infiltration, autoimmune organ damage, malabsorptive enteropathy, and recurrent infection **lead to** failure to thrive and, untreated, early-childhood morbidity and mortality.

```
IL2RA biallelic LOF
        │
        ▼
No functional CD25 at plasma membrane
        │
        ▼
No high-affinity IL-2 receptor (CD25+CD122+γc)
        │
        ▼
↓ JAK1/JAK3 → STAT5 signaling
        │
        ▼
FOXP3+ Treg failure  +  ↓ IL-10
        │
        ▼
Loss of peripheral tolerance
     ┌──────────────┴───────────────┐
     ▼                              ▼
Branch A: AUTOIMMUNITY          Branch B: IMMUNODEFICIENCY
(CD8+ lymphoproliferation,      (impaired antigen-specific
 enteropathy, hepatitis,         responses → recurrent viral,
 thyroiditis, cytopenias,        bacterial, fungal infections)
 multi-organ infiltration)
     └──────────────┬───────────────┘
                    ▼
     Failure to thrive; early-childhood
     morbidity/mortality if untreated
```

### Mechanistic detail

- **Molecular pathways:** Interleukin-2 signaling via **JAK-STAT5** (Reactome R-HSA-451927 "Interleukin-2 signaling"; KEGG hsa04630 JAK-STAT; hsa04060 cytokine–cytokine receptor interaction). "Of crucial importance for the delivery of IL-2 signals to Treg cells is the expression of CD25, which, along with CD122 and gammac, confers high affinity binding to IL-2" ([PMID: 19348914](https://pubmed.ncbi.nlm.nih.gov/19348914/)).
- **Cellular processes:** Failure of regulatory T-cell differentiation and suppression; unrestrained effector T-cell proliferation and inflammation.
- **Protein dysfunction:** Loss of function via truncation or conformational abrogation of surface expression ([PMID: 30742970](https://pubmed.ncbi.nlm.nih.gov/30742970/)).
- **Immune involvement:** Simultaneous immunodeficiency and autoimmunity — a "Tregopathy." Caudy et al. showed a CD25-deficient patient had "defective IL-10 expression from CD4 lymphocytes, whereas a Foxp3-deficient patient expressed normal levels of IL-10… although Foxp3 is not required for normal IL-10 expression by human CD4 lymphocytes, CD25 expression is important" ([PMID: 17196245](https://pubmed.ncbi.nlm.nih.gov/17196245/)).
- **Tissue damage:** Direct cytotoxic and inflammatory injury — "Activated CD8(+)STAT5(+) T cells with lytic potential infiltrated the skin, even though FOXP3(+) Tregs were present" ([PMID: 23416241](https://pubmed.ncbi.nlm.nih.gov/23416241/)).

**Suggested GO / CL terms.** Biological processes: interleukin-2-mediated signaling pathway (GO:0038110); regulatory T cell differentiation (GO:0045066); positive regulation of T cell proliferation (GO:0042102); JAK-STAT cascade (GO:0007259); tolerance induction (GO:0002507); negative regulation of immune response (GO:0050777). Cell types: regulatory T cell (CL:0000792); CD8-positive, alpha-beta T cell (CL:0000625); CD4-positive, alpha-beta T cell (CL:0000624); thymocyte (CL:0000893); B cell (CL:0000236).

---

## 7. Anatomical Structures Affected

**Organ / body-system level.** Immune/hematologic (primary), digestive, respiratory, integumentary, hepatobiliary, and endocrine systems. Sharfe et al. documented "extensive lymphocytic infiltration of tissues, including lung, liver, gut, and bone… accompanied by tissue atrophy and inflammation" ([PMID: 9096364](https://pubmed.ncbi.nlm.nih.gov/9096364/)).

| Structure | UBERON term |
|---|---|
| Intestine / gut | UBERON:0000160 |
| Liver | UBERON:0002107 |
| Lung | UBERON:0002048 |
| Skin | UBERON:0002097 |
| Bone / bone marrow | UBERON:0002371 |
| Thymus | UBERON:0002370 |
| Lymph node | UBERON:0000029 |
| Spleen | UBERON:0002106 |
| Thyroid gland | UBERON:0002046 |
| Lacrimal/ocular surface & cornea | UBERON:0000964 |

**Tissue / cell level.** Primarily lymphoid tissue and infiltrated epithelial organs. Key cell types: FOXP3⁺ regulatory T cells (CL:0000792), CD8⁺ and CD4⁺ αβ T cells (CL:0000625, CL:0000624), thymocytes (CL:0000893), B cells (CL:0000236).

**Subcellular level.** Plasma membrane (GO:0005886) — site of the CD25 receptor; LOF variants prevent surface localization ([PMID: 30742970](https://pubmed.ncbi.nlm.nih.gov/30742970/)). Also external side of plasma membrane (GO:0009897) and receptor complex (GO:0043235).

**Localization / lateralization.** Multi-organ and **bilateral/systemic** (e.g., bilateral ocular surface disease, generalized lymphoproliferation), not focal or unilateral.

---

## 8. Temporal Development

- **Onset:** **Congenital/neonatal to early childhood**, typically **insidious-to-subacute** with recurrent infections and chronic diarrhea in infancy.
- **Progression:** Chronic and **progressive** without treatment, with accumulating autoimmune organ damage and lymphoproliferation. Episodic autoimmune flares are superimposed.
- **Duration:** Chronic, lifelong; untreated cases carry high early-childhood mortality.
- **Remission:** No spontaneous remission. Durable remission/cure is **treatment-induced** by HSCT; sirolimus induces medical control.
- **Critical period:** Early **molecular diagnosis and timely HSCT** represent the key window of therapeutic opportunity — "early clinical and molecular diagnosis… promptly led to HSCT, allowing complete resolution of the symptoms and definitive cure" ([PMID: 30742970](https://pubmed.ncbi.nlm.nih.gov/30742970/)).

---

## 9. Inheritance and Population

**Epidemiology.** Ultra-rare; ~13 molecularly confirmed cases reported worldwide as of 2026 ([PMID: 41659858](https://pubmed.ncbi.nlm.nih.gov/41659858/)). **No population prevalence or incidence estimate is established** (data-level rarity).

**Inheritance.** **Autosomal recessive**, biallelic germline LOF variants — "a rare autosomal recessive inborn error of immunity" ([PMID: 41659858](https://pubmed.ncbi.nlm.nih.gov/41659858/)). Both sexes affected (autosomal). Penetrance appears **complete** with biallelic LOF; expressivity is **variable** (spectrum from predominant enteropathy to lung, ocular, or hepatic involvement).

**Consanguinity / founder effects.** **Consanguinity is the principal population risk factor** — first-cousin unions are frequently reported ([PMID: 41694357](https://pubmed.ncbi.nlm.nih.gov/41694357/)). No broad founder mutation established; variants are largely private.

**Carrier frequency.** Not established given rarity; heterozygous carriers are clinically unaffected.

**Population demographics.** Reported across multiple populations (Canada, Argentina, Italy, Morocco, others), with clustering in consanguineous families. No sex predilection. Age distribution is pediatric (presentation in infancy/early childhood). Data derive from **individual case reports**, not registries.

---

## 10. Diagnostics

**Frontline immunophenotyping.** **Flow cytometry** demonstrating absent/reduced surface CD25 on CD4⁺/activated T cells is the key rapid test: "Cytofluorimetric analysis revealed the total absence of CD25 cell surface expression and addressed IL2Rα molecular investigation" ([PMID: 30742970](https://pubmed.ncbi.nlm.nih.gov/30742970/)); "flow cytometry showed a complete absence of CD25 expression" ([PMID: 41694357](https://pubmed.ncbi.nlm.nih.gov/41694357/)).

**Molecular confirmation.** Sequencing of *IL2RA* — single-gene testing, IEI/immune-dysregulation gene panels, or **whole-exome/whole-genome sequencing**. Genetic distinction from IPEX is essential: "Any patient with features of IPEX but with a normal Foxp3 gene should be screened for mutations in the IL-2 receptor subunit CD25" ([PMID: 17196245](https://pubmed.ncbi.nlm.nih.gov/17196245/)).

**Supporting laboratory tests.** Lymphocyte subsets (variable; often normal-to-low T cells with expanded activated CD8⁺); immunoglobulins (often normal-to-high, hypergammaglobulinemia); autoantibodies (broad spectrum, including anti-mitochondrial antibodies; [PMID: 20650610](https://pubmed.ncbi.nlm.nih.gov/20650610/)); impaired in-vitro T-cell proliferation to mitogens ([PMID: 9096364](https://pubmed.ncbi.nlm.nih.gov/9096364/), [23416241](https://pubmed.ncbi.nlm.nih.gov/23416241/)).

**Functional test.** Reduced IL-2-induced STAT5 phosphorylation in responder cells.

**Biopsy/pathology.** Affected-organ biopsy shows lymphocytic infiltration and tissue inflammation (e.g., follicular bronchiolitis with lymphocyte hyperplasia in lung).

**Differential diagnosis.** IPEX (FOXP3); CD122/IL2RB deficiency; STAT5b deficiency; LRBA deficiency; CTLA4 haploinsufficiency; other IPEX-like Tregopathies; and severe combined immunodeficiency (SCID). CD25 deficiency is distinguished from SCID by lymphoproliferation, autoimmunity, and preserved B-cell development ([PMID: 24116927](https://pubmed.ncbi.nlm.nih.gov/24116927/)).

**Screening.** Not part of standard newborn screening. Cascade carrier and prenatal/preimplantation testing available once the familial variant is known.

---

## 11. Outcome / Prognosis

**Untreated course.** Severe and progressive, with high risk of death in early childhood from overwhelming infection and/or autoimmune organ damage — analogous to the lethal Il2/Il2ra-null mouse phenotype (death within ~5 weeks on the BALB/c background, [PMID: 9065030](https://pubmed.ncbi.nlm.nih.gov/9065030/)) and severe multi-organ infiltration in humans ([PMID: 9096364](https://pubmed.ncbi.nlm.nih.gov/9096364/)).

**Treated course.** **HSCT is potentially curative** — "complete resolution of the symptoms and definitive cure of the disease" after early transplantation ([PMID: 30742970](https://pubmed.ncbi.nlm.nih.gov/30742970/)); long-term HSCT outcomes are reviewed in two additional novel cases ([PMID: 41659858](https://pubmed.ncbi.nlm.nih.gov/41659858/)).

**Morbidity / QoL.** Substantial untreated morbidity (malnutrition, autoimmune organ damage, recurrent infection, dry-eye disease). Formal disability/QoL metrics are not available.

**Prognostic factors.** Timely molecular diagnosis and access to HSCT are the dominant prognostic determinants; extent of established autoimmune organ damage at transplant influences outcome. No validated prognostic biomarkers beyond the diagnostic markers.

---

## 12. Treatment

**Definitive / curative therapy.** **Allogeneic hematopoietic stem cell transplantation (HSCT)** replaces the defective hematopoietic compartment and restores functional Tregs — the only curative option (NCIT:C15431 Hematopoietic Stem Cell Transplantation) ([PMID: 30742970](https://pubmed.ncbi.nlm.nih.gov/30742970/), [41659858](https://pubmed.ncbi.nlm.nih.gov/41659858/)).

**Bridging / medical immunomodulation.**
- **Rapamycin (sirolimus)** — mTOR inhibitor that spares/favors Tregs; reported as an "effective and safe treatment of a novel IL2RA deficiency" ([PMID: 31605764](https://pubmed.ncbi.nlm.nih.gov/31605764/)) (NCIT:C1212 Sirolimus; CHEBI:9168).
- **Corticosteroids and other immunosuppressants** for autoimmune flares.
- **Immunoglobulin replacement and antimicrobial prophylaxis** for infection control.
- **Nutritional support** for enteropathy and failure to thrive.

**Pharmacogenomics.** Not specifically defined for this disease.

**Personalized / genotype-guided approach.** Diagnosis-driven: confirmation of IL2RA LOF directs the patient toward definitive HSCT with sirolimus bridging, and enables family cascade testing.

**Treatment strategy (algorithm).** (1) Recognize IPEX-like phenotype → (2) flow cytometry for surface CD25 → (3) IL2RA sequencing → (4) initiate sirolimus/immunosuppression + supportive care to control autoimmunity and infection → (5) proceed to allogeneic HSCT as definitive cure.

---

## 13. Prevention

- **Primary prevention:** None possible for a Mendelian disorder (no modifiable exposure).
- **Secondary/tertiary prevention:** Early molecular diagnosis, infection prophylaxis, immunosuppressive control of autoimmunity, and **timely HSCT** to prevent irreversible organ damage.
- **Reproductive prevention / counseling:** Genetic counseling for autosomal recessive recurrence risk (**25% per pregnancy** for carrier couples); **cascade carrier testing** in consanguineous families; and **prenatal or preimplantation genetic testing** once the familial *IL2RA* variant is identified.
- **Immunization / public-health interventions:** Not disease-specific, though routine infection prevention and prophylaxis are important for affected children.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** *Mus musculus* (NCBI Taxon 10090) is the principal model species. No described spontaneous natural companion-animal disease equivalent.
- **Orthologous gene:** *Il2ra* (mouse ortholog of human *IL2RA*; MGI).
- **Comparative biology:** Mouse Il2ra/Il2 knockouts recapitulate lymphoproliferation, autoimmune hemolytic anemia, and inflammatory bowel disease due to defective Treg-mediated peripheral tolerance, confirming evolutionary conservation of the IL-2/CD25 tolerance mechanism ([PMID: 9065030](https://pubmed.ncbi.nlm.nih.gov/9065030/)).
- **Transmission / zoonotic potential:** None (genetic disorder).

---

## 15. Model Organisms

**Mammalian genetic models (mouse; NCBI Taxon 10090).**
- **Il2⁻/⁻ knockout mice:** On a mixed 129/Ola × C57BL/6 background, predominantly develop **ulcerative-colitis-like disease**; when backcrossed to **BALB/c** they develop **generalized autoimmune disease** — hemolytic anemia, follicular hyperplasia of lymphoid organs, and inflammation of pancreas, liver, heart, lungs, and thoracic vessels — dying within ~5 weeks, with uncontrolled polyclonal T- and B-cell activation and increased autoantibodies ([PMID: 9065030](https://pubmed.ncbi.nlm.nih.gov/9065030/)). This demonstrates both phenotype recapitulation and **genetic-background modifier effects**.
- **Il2ra (CD25) knockout mice** (Willerford et al., *Immunity* 1995): massive lymphoproliferation, autoimmune hemolytic anemia, and inflammatory bowel disease from defective Treg-mediated tolerance — a direct genetic model of the human disorder.
- **Foxp1/Foxp4 Treg-conditional knockouts:** combined deletion causes lymphoproliferation, inflammation, autoimmunity, and early lethality with reduced CD25 expression, mechanistically linking FOXP1/FOXP4 → Il2ra promoter → CD25 → Treg function ([PMID: 40794436](https://pubmed.ncbi.nlm.nih.gov/40794436/)).

**Model characteristics.** Recapitulation is strong for **autoimmunity, lymphoproliferation, and colitis**; the immunodeficiency/infection-susceptibility axis is less emphasized in murine models. Genetic-background dependence is a key limitation for translating a single model to the full human phenotype spectrum.

**Resources.** MGI, IMPC/KOMP, IMSR (for Il2ra/Il2 alleles).

---

## Evidence Base

| PMID | Title (abbrev.) | Role / how it supports findings |
|---|---|---|
| [9096364](https://pubmed.ncbi.nlm.nih.gov/9096364/) | Human immune disorder from IL-2Rα mutation (Sharfe 1997) | Original description; truncation of CD25, tissue lymphocytic infiltration (lung, liver, gut, bone) |
| [17196245](https://pubmed.ncbi.nlm.nih.gov/17196245/) | CD25 deficiency causes IPEX-like syndrome, defective IL-10 | Establishes IPEX-like designation, CD25-dependent IL-10; IL2RA screening if FOXP3 normal |
| [23416241](https://pubmed.ncbi.nlm.nih.gov/23416241/) | Human IL2RA null mutation | CD8⁺ lymphoproliferation, impaired antigen responses, tissue infiltration despite FOXP3⁺ Tregs |
| [19348914](https://pubmed.ncbi.nlm.nih.gov/19348914/) | IL-2/CD25 immunoregulatory mechanisms | CD25 + CD122 + γc confer high-affinity IL-2 binding to Tregs |
| [30742970](https://pubmed.ncbi.nlm.nih.gov/30742970/) | New conformational mutation; HSCT cure | Conformational missense abrogates surface CD25; flow-cytometry diagnosis; HSCT cure |
| [41694357](https://pubmed.ncbi.nlm.nih.gov/41694357/) | First Moroccan cases | AR inheritance, consanguinity, core phenotype, absent CD25 on flow |
| [41659858](https://pubmed.ncbi.nlm.nih.gov/41659858/) | Two novel cases + review (long-term HSCT) | Confirms rarity (~13 cases), AR IEI definition, HSCT outcomes |
| [24116927](https://pubmed.ncbi.nlm.nih.gov/24116927/) | Follicular bronchiolitis phenotype | Y41S missense; absent CD25/very low Tregs; lung disease; distinction from SCID |
| [29252577](https://pubmed.ncbi.nlm.nih.gov/29252577/) | Severe dry eye in CD25 deficiency | Ocular surface disease; multi-tissue lymphocytic infiltration |
| [31605764](https://pubmed.ncbi.nlm.nih.gov/31605764/) | Rapamycin treatment | Sirolimus as effective/safe bridging therapy |
| [9065030](https://pubmed.ncbi.nlm.nih.gov/9065030/) | Il2⁻/⁻ BALB/c autoimmune mice | Mouse model; genetic-background modifier effect |
| [40794436](https://pubmed.ncbi.nlm.nih.gov/40794436/) | FOXP1/FOXP4 in Tregs | FOXP1/4 bind Il2ra promoter, regulate CD25; modifier biology |
| [20650610](https://pubmed.ncbi.nlm.nih.gov/20650610/) | Autoantibody spectrum in IPEX | Broad autoantibodies; pediatric PBC linked to CD25 deficiency |
| [26106896](https://pubmed.ncbi.nlm.nih.gov/26106896/) | Fine-mapping IL2RA region | Common IL2RA variants as MS/T1D susceptibility (distinct from LOF disease) |
| [21875375](https://pubmed.ncbi.nlm.nih.gov/21875375/) | 10p15 IL2RA in T1D | rs41295061 association replicated in T1D |
| [33193078](https://pubmed.ncbi.nlm.nih.gov/33193078/) | IL2RA in autoimmune thyroid disease | rs7093069 TT genotype increases AITD risk |

---

## Limitations and Knowledge Gaps

1. **Extreme rarity.** With only ~13–15 molecularly confirmed cases, all epidemiologic parameters (prevalence, incidence, carrier frequency, sex ratio, precise phenotype frequencies) are unquantified; phenotype frequencies remain qualitative.
2. **Case-report evidence base.** Nearly all human data come from single cases/small series with inherent selection and publication bias. No natural-history cohort or registry exists.
3. **Genotype–phenotype correlation** is undefined given so few variants.
4. **Mechanistic steps partly inferred.** The STAT5-phosphorylation step and gut-microbial drive of enteropathy are inferred from IL-2 biology and mouse data rather than directly demonstrated in every patient.
5. **Modifier genes in humans** are unknown; mouse background effects suggest they exist.
6. **No formal QoL/disability metrics** or standardized outcome measures are available.
7. **Long-term HSCT outcomes** are based on very few transplanted patients.

## Proposed Follow-up Experiments / Actions

1. **Establish an international IL2RA-deficiency patient registry** (via IEI consortia such as ESID/USIDNET) to aggregate genotype, phenotype, treatment, and outcome data.
2. **Systematic functional characterization** of each reported IL2RA variant (surface expression, IL-2 binding, pSTAT5 response) to build a variant-effect map.
3. **Single-cell / immune profiling** of patient PBMCs and affected tissues to resolve Treg vs. effector-cell dynamics and IL-10 deficits at cellular resolution.
4. **Standardized HSCT outcome tracking** (conditioning regimen, chimerism, autoimmunity resolution, long-term immune reconstitution).
5. **Evaluate low-dose IL-2 and sirolimus** as bridging therapies in a prospective, protocolized fashion (noting that high-affinity receptor loss may blunt low-dose IL-2 efficacy — a hypothesis worth testing).
6. **Explore gene-correction / gene-editing** (e.g., autologous HSC IL2RA correction) as a future curative alternative to allogeneic HSCT.
7. **Carrier screening in consanguineous populations** where cases have clustered, to enable earlier diagnosis and reproductive counseling.

---

*Evidence source types are indicated throughout: human clinical (case reports/series), model organism (mouse knockouts), and in vitro/functional (flow cytometry, STAT5 assays). Ontology suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) are provided inline for knowledge-base ingestion.*


## Artifacts

- [OpenScientist final report](CD25_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](CD25_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 17 |
| Quoted claims found in source | 13 |
| Quoted claims **not** found in source | 4 |
| References weighed for topical relevance | 16 |
| On topic | 9 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:9096364` *(abstract only)*: "a novel human immune aberration arising from a truncation mutation of the interleukin-2 receptor alpha chain (CD25)… characterized by decreased numbers of peripheral T cells displaying abnormal proliferation but normal B cell development. Extensive lymphocytic infiltration of tissues, including lung, liver, gut, and bone, is observed, accompanied by tissue atrophy and inflammation"
  - closest text in source: "Extensive lymphocytic infiltration of tissues, including lung, liver, gut, and bone, is observed, accompanied by tissue atrophy and inflammation"
- `PMID:17196245` *(abstract only)*: "defective IL-10 expression from CD4 lymphocytes, whereas a Foxp3-deficient patient expressed normal levels of IL-10… although Foxp3 is not required for normal IL-10 expression by human CD4 lymphocytes, CD25 expression is important"
  - closest text in source: "This patient exhibited defective IL-10 expression from CD4 lymphocytes, whereas a Foxp3-deficient patient expressed normal levels of IL-10"
- `PMID:9096364` *(abstract only)*: "extensive lymphocytic infiltration of tissues, including lung, liver, gut, and bone… accompanied by tissue atrophy and inflammation"
  - closest text in source: "Extensive lymphocytic infiltration of tissues, including lung, liver, gut, and bone, is observed, accompanied by tissue atrophy and inflammation"
- `PMID:30742970` *(abstract only)*: "early clinical and molecular diagnosis… promptly led to HSCT, allowing complete resolution of the symptoms and definitive cure"
  - closest text in source: "The early clinical and molecular diagnosis of CD25 deficiency in this patient promptly led to hematopoietic stem cell transplantation (HSCT), allowing complete resolution of the symptoms and definitive cure of the disease."

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 47 |
| Resolved | 45 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 22 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 13 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0011664` (2 mentions) - the report calls it "MONDO"; MONDO calls it **immunodeficiency due to CD25 deficiency**
- `HP:0001508` (1 mention) - the report calls it "Physical"; HP calls it **Failure to thrive**
- `HP:0002205` (1 mention) - the report calls it "Sign"; HP calls it **Recurrent respiratory infections**
- `HP:0000964` (1 mention) - the report calls it "Physical"; HP calls it **Eczematoid dermatitis**
- `HP:0002608` (1 mention) - the report calls it "Lab/clinical"; HP calls it **Celiac disease**
- `HP:0100646` (1 mention) - the report calls it "Lab/clinical"; HP calls it **Thyroiditis**
- `HP:0001890` (1 mention) - the report calls it "Lab"; HP calls it **Autoimmune hemolytic anemia**
- `HP:0002716` (1 mention) - the report calls it "Sign"; HP calls it **Lymphadenopathy**
- `HP:0001433` (1 mention) - the report calls it "Sign"; HP calls it **Hepatosplenomegaly**
- `HP:0006538` (1 mention) - the report calls it "Clinical"; HP calls it **Recurrent bronchopulmonary infections**
- `HP:0002850` (1 mention) - the report calls it "Lab"; HP calls it **Decreased circulating IgM concentration**
- `HP:0010702` (1 mention) - the report calls it "Lab"; HP calls it **Increased circulating immunoglobulin concentration**
- `UBERON:0000964` (1 mention) - the report calls it "Lacrimal/ocular surface & cornea"; UBERON calls it **cornea**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0000160` (1 mention) - the report calls it "Intestine / gut"; UBERON calls it **intestine**
- `UBERON:0002097` (1 mention) - the report calls it "Skin"; UBERON calls it **skin of body**, and lists "skin" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.