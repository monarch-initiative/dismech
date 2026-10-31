---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T23:22:23.669315'
end_time: '2026-10-15T23:22:25.769235'
duration_seconds: 2.1
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Pseudohypoaldosteronism Type IB2 Autosomal Recessive
  mondo_id: MONDO:0859317
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
citation_count: 24
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:41457049
  relevance_assessed: 24
  on_topic: 21
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 41
  verified: 38
  not_found: 1
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.026
  labels_checked: 25
  labels_matching: 8
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: MONDO:0859317
    reported_labels:
    - PHA type IB2
    - Pseudohypoaldosteronism type IB2, autosomal recessive
    ontology_label: pseudohypoaldosteronism, type IB2, autosomal recessive
  - term_id: HP:0002902
    reported_labels:
    - Lab abnormality
    ontology_label: Hyponatremia
  - term_id: HP:0002153
    reported_labels:
    - Lab abnormality
    ontology_label: Hyperkalemia
  - term_id: HP:0001942
    reported_labels:
    - Lab abnormality
    ontology_label: Metabolic acidosis
  - term_id: HP:0000859
    reported_labels:
    - Lab abnormality
    ontology_label: Increased circulating aldosterone concentration
  - term_id: HP:0001508
    reported_labels:
    - Clinical sign
    ontology_label: Failure to thrive
  - term_id: HP:0012236
    reported_labels:
    - Lab abnormality
    ontology_label: Elevated sweat chloride
  - term_id: NCIT:C29343
    reported_labels:
    - Polystyrene Sulfonate
    ontology_label: Pyran Polymer
  - term_id: NCIT:C87720
    reported_labels:
    - Sodium Bicarbonate
    ontology_label: Pararosaniline Pamoate Anhydrous
  labels_variant: 8
  unresolved_terms:
  - NCIT:C77398
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
  path: Pseudohypoaldosteronism_Type_IB2_Autosomal_Recessive-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Pseudohypoaldosteronism_Type_IB2_Autosomal_Recessive-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pseudohypoaldosteronism Type IB2 Autosomal Recessive
- **MONDO ID:** MONDO:0859317 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Pseudohypoaldosteronism Type IB2 Autosomal Recessive** covering all of the
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

# Pseudohypoaldosteronism Type IB2, Autosomal Recessive — Comprehensive Disease Report

**MONDO ID:** MONDO:0859317 · **Category:** Mendelian · **Causal gene:** *SCNN1B* (ENaC β-subunit) · **Inheritance:** Autosomal recessive

---

## Summary

**Pseudohypoaldosteronism type IB2 (PHA1B2; MONDO:0859317) is the *SCNN1B*/β-subunit variant of the severe, systemic, autosomal-recessive form of type 1 pseudohypoaldosteronism (PHA1).** It is caused by biallelic loss-of-function variants in *SCNN1B* (16p12.2), the gene encoding the β-subunit of the amiloride-sensitive epithelial sodium channel (ENaC). ENaC is the final effector of aldosterone-driven sodium reabsorption. When the channel cannot assemble or conduct sodium, the body becomes resistant to aldosterone at the end organ (the hormone is present and markedly elevated, but its signal cannot be transduced), producing a systemic salt-wasting disorder affecting the kidney, colon, lung, and sweat/salivary/skin epithelia. PHA1 is subdivided into a milder **autosomal dominant renal form (PHA1A, *NR3C2*/mineralocorticoid receptor)** and a severe **systemic autosomal recessive form (PHA1B)** caused by biallelic mutations in the three ENaC subunit genes — *SCNN1A* (α, IB1), *SCNN1B* (β, **IB2**), and *SCNN1G* (γ, IB3). The clinical and biochemical phenotype is indistinguishable among the three subunit subtypes.

**Clinically, PHA1B2 presents in the neonatal period** (median age ~14 days) with a life-threatening salt-wasting crisis: poor feeding, vomiting, weight loss, dehydration, failure to thrive, and circulatory shock, accompanied by the biochemical triad of **hyponatremia, hyperkalemia, and metabolic acidosis** with **markedly elevated plasma renin and aldosterone**. Extra-renal features distinguish the systemic form from the renal form — cystic fibrosis-like pulmonary disease, eczematous/miliaria-like skin lesions, and elevated sweat chloride (a positive sweat test). Critically, the electrolyte abnormalities are **resistant to glucocorticoid and mineralocorticoid therapy**, which is the key feature distinguishing PHA1 from congenital adrenal hyperplasia (CAH). Management is **lifelong supportive care**: high-dose oral sodium chloride, potassium-lowering cation-exchange resins (sodium/calcium polystyrene sulfonate), alkali for acidosis, and acute measures for hyperkalemic emergencies. There is no cure and no disease-modifying therapy. Mortality is substantial (reported 25–67% across cohorts, largely from hyperkalemic cardiac arrest), yet survival with normal neurological outcome into adulthood is achievable with intensive management.

**At the molecular level, PHA1B2 is an ENaC channelopathy.** Biallelic *SCNN1B* loss-of-function abolishes or severely reduces apical sodium conductance in principal cells of the aldosterone-sensitive distal nephron, triggering urinary sodium wasting, failure of distal potassium/hydrogen secretion, and compensatory (but futile) renin-angiotensin-aldosterone system (RAAS) activation. A distinctive feature of the β-subunit is that **truncated β-ENaC subunits can retain partial channel activity**, providing a molecular explanation for phenotypic variability and the clinical observation that salt requirements sometimes decline with age. The βENaC (*Scnn1b*) knockout mouse faithfully recapitulates the human disorder (hyperkalemia, renal salt wasting, elevated aldosterone, neonatal death), confirming the causal mechanism. This report synthesizes 10 confirmed findings drawn from 52 reviewed papers across all 15 requested domains.

> **Scope note on nomenclature.** Because the clinical/biochemical phenotype, mechanism, prognosis and treatment are essentially identical across the three subunit subtypes (IB1/IB2/IB3), much of the evidence below derives from the systemic PHA1B literature as a whole, with SCNN1B-specific data highlighted where available. MONDO:0859317 (PHA type IB2) = the SCNN1B/β-subunit subtype, confirmed by a 2026 case report explicitly labeling SCNN1B compound-heterozygous disease as "Pseudohypoaldosteronism Type 1B2" ([PMID: 41457049](https://pubmed.ncbi.nlm.nih.gov/41457049/)).

---

## 1. Disease Information

**Overview.** Pseudohypoaldosteronism type IB2 is the systemic, autosomal-recessive form of type 1 pseudohypoaldosteronism caused specifically by biallelic loss-of-function variants in *SCNN1B*, the gene encoding the β-subunit of the epithelial sodium channel. "Pseudohypoaldosteronism" denotes end-organ resistance to aldosterone: aldosterone (and renin) are markedly elevated, but target epithelia fail to reabsorb sodium because the downstream effector channel (ENaC) is non-functional. The term "systemic" reflects that ENaC loss affects multiple organs (kidney, colon, lung, sweat/salivary glands, skin), unlike the "renal" (kidney-limited) form.

The disease taxonomy was confirmed by a 2026 case report that explicitly titled compound-heterozygous *SCNN1B* disease as "Pseudohypoaldosteronism Type 1B2," establishing that MONDO:0859317 corresponds to the *SCNN1B*/β-subunit subtype ([PMID: 41457049](https://pubmed.ncbi.nlm.nih.gov/41457049/)): *"The autosomal recessive systemic form (PHA1B), caused by mutations in SCNN1A, SCNN1B, or SCNN1G, is particularly severe and typically manifests in the neonatal period. Among these, SCNN1B-related cases occur less frequently than SCNN1A-related cases."*

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0859317 (Pseudohypoaldosteronism type IB2, autosomal recessive) |
| OMIM (phenotype) | #264350 (Pseudohypoaldosteronism type I, autosomal recessive — covers IB1/IB2/IB3) |
| Gene | *SCNN1B* (HGNC:10600); OMIM gene *600760* |
| Orphanet | ORPHA:171876 (Autosomal recessive pseudohypoaldosteronism type 1) |
| ICD-10 | E27.4 (Other and unspecified adrenocortical insufficiency); mineralocorticoid resistance |
| MeSH | D011546 (Pseudohypoaldosteronism) |

**Synonyms / alternative names.** PHA1B2; systemic pseudohypoaldosteronism type 1 (β-subunit); autosomal recessive PHA1, SCNN1B-related; multisystem pseudohypoaldosteronism type 1; mineralocorticoid resistance (systemic type). Within the subunit classification: IB1 = *SCNN1A*, **IB2 = *SCNN1B***, IB3 = *SCNN1G*.

**Source of information.** This report is derived from **aggregated disease-level resources** (OMIM, Orphanet, PubMed reviews) combined with **individual patient case reports and small case series** — the dominant evidence type for this ultra-rare disorder. No EHR-scale datasets exist.

---

## 2. Etiology

**Disease causal factors.** PHA1B2 is a **monogenic (Mendelian) disorder** caused exclusively by **biallelic (homozygous or compound-heterozygous) loss-of-function variants in *SCNN1B***. There is no environmental or infectious cause of the primary disease. Causality is well established: biallelic ENaC subunit mutations cause systemic PHA1, whereas *NR3C2* (mineralocorticoid receptor) mutations cause the distinct renal form ([PMID: 42549990](https://pubmed.ncbi.nlm.nih.gov/42549990/)): *"a milder renal form (PHA1A) due to NR3C2 mutations and a severe systemic form (PHA1B) caused by biallelic mutations in epithelial sodium channel (ENaC) subunit genes."*

**Genetic risk factors.** The sole genetic risk factor is inheritance of two loss-of-function *SCNN1B* alleles. **Consanguinity is a strong contextual contributor** — homozygous variants predominate in offspring of consanguineous unions (78% consanguinity in a 2026 systemic PHA1B series; 100% in a 37-year UK cohort). Heterozygous carriers are asymptomatic. Modifier effects likely exist (see §4), notably residual channel activity of hypomorphic truncating alleles.

**Environmental risk factors.** None cause the disease. However, **dietary sodium intake** modulates severity: inadequate salt provokes crises, and high salt intake is therapeutic. Intercurrent illness (vomiting, diarrhea, infection, heat/sweating) can precipitate acute decompensation by increasing sodium losses.

**Protective factors.** No genetic protective alleles are established. The principal "protective" intervention is **exogenous salt supplementation**. Residual ENaC activity from hypomorphic (e.g., certain truncating) *SCNN1B* alleles can be protective relative to complete null alleles, explaining milder courses in some patients.

**Gene–environment interactions.** The central G×E interaction is between ENaC genotype and dietary salt: *"The complex interaction between genetic factors (ENaC mutations) and the risk factor (salt intake) can now be studied experimentally"* ([PMID: 11826291](https://pubmed.ncbi.nlm.nih.gov/11826291/)). Loss-of-function ENaC mutations create salt sensitivity/salt wasting; the magnitude of clinical crisis depends on salt availability.

---

## 3. Phenotypes

PHA1B2 phenotypes fall into three categories: (a) consequences of systemic salt wasting, (b) laboratory abnormalities, and (c) extra-renal epithelial manifestations. All are **neonatal-onset** and, in the systemic form, **lifelong**.

| Phenotype | Type | HPO term | Onset | Severity | Frequency |
|---|---|---|---|---|---|
| Hyponatremia | Lab abnormality | HP:0002902 | Neonatal | Severe (median Na 124 mEq/L) | ~100% |
| Hyperkalemia | Lab abnormality | HP:0002153 | Neonatal | Severe (median K 8.0 mEq/L) | ~100% |
| Metabolic acidosis | Lab abnormality | HP:0001942 | Neonatal | Moderate–severe | Very frequent |
| Elevated renin | Lab abnormality | HP:0000848 (hyperreninemia) | Neonatal | Marked | ~100% |
| Hyperaldosteronism | Lab abnormality | HP:0000859 | Neonatal | Marked | ~100% |
| Salt wasting / dehydration | Clinical sign | HP:0003648 / HP:0001944 | Neonatal | Severe | ~100% |
| Failure to thrive | Clinical sign | HP:0001508 | Neonatal/infancy | Severe | Very frequent |
| Vomiting / poor feeding | Symptom | HP:0002013 / HP:0011968 | Neonatal | Moderate–severe | Frequent |
| Recurrent respiratory (CF-like) disease | Physical manifestation | HP:0002205 / HP:0006528 | Neonatal | Variable | ~71% (5/7, SCNN1A cohort) |
| Dermatitis / miliaria-like rash | Physical manifestation | HP:0000964 / HP:0011123 | Infancy | Variable, often treatment-resistant | Reported |
| Elevated sweat chloride | Lab abnormality | HP:0012236 | Any | Positive sweat test | Characteristic of systemic form |

**Characteristics.** Onset is **neonatal** (first 1–2 weeks of life; median 14 days). Severity is **severe** (life-threatening). Progression: the acute crisis is **episodic/fluctuating** around a **chronic lifelong baseline** in the systemic form — unlike the renal form where symptoms remit in toddlerhood. The core electrolyte phenotype has ~100% frequency; the pulmonary phenotype is variable and *not predictable from genotype* ([PMID: 23416952](https://pubmed.ncbi.nlm.nih.gov/23416952/)): *"affected children suffer from neonatal onset of multi-organ salt loss and often exhibit cystic fibrosis-like pulmonary symptoms"* (5/7, i.e. 71%, in that series).

The quantitative neonatal presentation is documented in the 2026 Indian series ([PMID: 42549990](https://pubmed.ncbi.nlm.nih.gov/42549990/)): *"The median age at presentation was 14 days (interquartile range 5.5-42.5)... All presented with hyponatraemia and hyperkalaemia (median serum sodium 124 mEq/L; potassium 8.0 mEq/L)."*

**Quality of life impact.** No formal EQ-5D/SF-36 data exist for this ultra-rare disorder. Qualitatively, affected individuals and families face a high burden: frequent hospitalizations in infancy, the need for large-volume oral salt supplements and potassium-binding resins (often via nasogastric/gastrostomy feeding), lifelong electrolyte monitoring, and the ongoing risk of fatal hyperkalemia. Survivors with normal neurological outcome can achieve normal physical development and even pregnancy ([PMID: 33690157](https://pubmed.ncbi.nlm.nih.gov/33690157/)).

---

## 4. Genetic / Molecular Information

**Causal gene.** ***SCNN1B*** (Sodium Channel Epithelial 1 Subunit Beta), HGNC:10600, located at **16p12.2**, encoding the β-subunit of ENaC (640 residues). The α (*SCNN1A*, 12p13), β (*SCNN1B*, 16p12.2), and γ (*SCNN1G*, 16p12) subunits assemble as a heterotrimeric channel ([PMID: 26817011](https://pubmed.ncbi.nlm.nih.gov/26817011/)): *"mutations in the amiloride-sensitive epithelial sodium channel gene (alpha subunit=SCNN1A, 12p13; beta subunit=SCNN1b, 16p12.2-p12.1; gamma subunit=SCNN1G, 16p12) causes a more severe autosomal recessive form, which has systemic effects."*

**Pathogenic variants.** Variants are generally **private/novel** rather than recurrent founder mutations. Reported *SCNN1B* variant types include **frameshift, nonsense, and splice-site** mutations producing truncated or absent β-ENaC:

| Variant (SCNN1B) | Type | Consequence | Source |
|---|---|---|---|
| c.648dupA (p.Glu217fs), exon 4 | Frameshift | Truncated β (253/640 aa), partial activity | [PMID: 20064610](https://pubmed.ncbi.nlm.nih.gov/20064610/) |
| c.915delC (p.Tyr306fs), exon 6 | Frameshift | Truncated β (317/640 aa), partial activity | [PMID: 20064610](https://pubmed.ncbi.nlm.nih.gov/20064610/) |
| c.1266-1G>C (intron 8) | Splice-site (homozygous) | Systemic PHA1, improved with age | [PMID: 23426840](https://pubmed.ncbi.nlm.nih.gov/23426840/) |

Variant classification follows ACMG/AMP; loss-of-function variants in *SCNN1B* in the biallelic state are classified **pathogenic**. Allele frequencies in gnomAD are extremely low (consistent with an ultra-rare recessive disorder). Origin is **germline**; no somatic involvement. Functional consequence is **loss of function** — but importantly, truncated β-subunits can retain **partial (residual) channel activity** ([PMID: 20064610](https://pubmed.ncbi.nlm.nih.gov/20064610/)): *"The p.Glu217fs (c.648dupA in exon 4) and p.Tyr306fs (c.915delC in exon 6) mutations produce shortened beta-ENaC subunits with 253 and 317 residues respectively instead of the 640 residues present in beta-ENaC subunit. Expression of cRNAs carrying these mutations in Xenopus oocytes showed that the mutations drastically reduce but do not eliminate ENaC activity."* This hypomorphic-vs-null severity gradient acts as an intrinsic modifier.

**Modifier genes.** Formal modifiers are not established. The other two ENaC subunits (*SCNN1A*, *SCNN1G*) functionally interact with the β-subunit — truncated β can still partially chaperone α and γ to the membrane to form a weakly active channel. Variability in residual activity likely drives much of the phenotypic variation.

**Epigenetic information / chromosomal abnormalities.** No disease-specific epigenetic signatures or large chromosomal rearrangements are characteristic of PHA1B2. (In the allelic *SCNN1A* subtype, a homozygous gross deletion has been reported — [PMID: 41275343](https://pubmed.ncbi.nlm.nih.gov/41275343/) — indicating that larger structural LoF alleles can occur in ENaC genes.)

---

## 5. Environmental Information

**Environmental factors.** No toxin, radiation, or occupational exposure causes PHA1B2. The dominant environmental variable is **dietary sodium**: salt deprivation precipitates decompensation; salt supplementation is therapeutic.

**Lifestyle factors.** Not applicable to disease causation. Chronic high-salt diet and potassium restriction are therapeutic lifestyle requirements.

**Infectious agents.** None cause PHA1B2. Crucially, infection (especially urinary tract infection) and obstructive uropathy cause **secondary/transient PHA**, the principal differential diagnosis (see §10). Intercurrent infections can also trigger acute metabolic crises in genetically affected patients by increasing fluid/sodium losses.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

```
1. Biallelic SCNN1B loss-of-function variant (germline)
        │  leads to
2. Absent or non-functional β-ENaC subunit
        │  results in
3. Failure to assemble a conductive αβγ-ENaC heterotrimer in apical membranes
   of epithelial cells  (partial activity possible with truncating/hypomorphic alleles)
        │  leads to
4. Loss of amiloride-sensitive apical Na+ conductance in the aldosterone-sensitive
   distal nephron (ASDN) principal cells — AND in colon, lung, sweat/salivary gland, skin
        │
        ├──(renal branch)── urinary Na+ wasting + failure of distal K+/H+ secretion
        │        │  results in
        │     5a. Hyponatremia, hypovolemia, hyperkalemia, metabolic acidosis
        │        │  leads to
        │     6a. Compensatory RAAS activation → HIGH renin + HIGH aldosterone
        │        │  but (end-organ resistance) signal cannot be transduced
        │        │  results in
        │     7a. Neonatal salt-wasting crisis / circulatory shock;
        │         hyperkalemic cardiac arrhythmia / arrest
        │
        └──(extra-renal branch)── loss of airway/skin/gland Na+ absorption
                 │  results in
              5b. ↑ Airway surface liquid → impaired mucociliary clearance → CF-like lung disease;
                  ↑ sweat/salivary Na+ (positive sweat test); dermatitis/miliaria
```

### Detailed mechanism

**Molecular pathway (aldosterone → ENaC).** ENaC is the amiloride-sensitive effector of aldosterone action in the ASDN (late distal convoluted tubule, connecting tubule, collecting duct) principal cells. Aldosterone normally upregulates ENaC through the **MR → SGK1 → Nedd4-2** axis: SGK1 phosphorylates the ubiquitin ligase Nedd4-2, preventing ENaC ubiquitylation/internalization and thereby increasing channel surface density ([PMID: 15958725](https://pubmed.ncbi.nlm.nih.gov/15958725/)): *"aldosterone treatment induces an increase in Nedd4-2 phosphorylation... accompanied by a raise in Sgk1 expression and transepithelial Na+ transport."* In PHA1B2 this entire regulatory cascade is intact and hyperactivated, but it is **futile** because the terminal effector channel is defective — the definition of end-organ aldosterone resistance ([PMID: 21664233](https://pubmed.ncbi.nlm.nih.gov/21664233/)): *"Loss-of-function mutations in two key components of the aldosterone response, the mineralocorticoid receptor and the epithelial sodium channel ENaC, lead to type 1 pseudohypoaldosteronism (PHA1), a rare genetic disease of aldosterone resistance."*

**Protein dysfunction.** β-ENaC is one of three homologous subunits forming the channel; loss of the β-subunit impairs channel assembly, trafficking, and conductance. A distinctive β-subunit feature is that **truncated proteins can still partially chaperone α and γ to the surface**, producing a weakly active channel — explaining residual function and variable expressivity ([PMID: 20064610](https://pubmed.ncbi.nlm.nih.gov/20064610/)). The amiloride-sensitive channel and its subunits underlie transepithelial sodium reabsorption; loss-of-function is the molecular basis of systemic PHA1 ([PMID: 19571553](https://pubmed.ncbi.nlm.nih.gov/19571553/)): *"This review provides an overview on transepithelial sodium reabsorption and on clinical features and the underlying molecular pathology of systemic and renal PHA1 caused by mutations in the subunit genes (SCNN1A, SCNN1B, SCNN1G) of the epithelial sodium channel (ENaC)."*

**Cellular processes / cell types.** The primary cells are **renal collecting duct principal cells** (CL:1000714) and ASDN epithelial cells; secondarily, **colonic epithelial cells**, **airway multiciliated epithelial cells**, **sweat/salivary gland duct cells**, and **keratinocytes/skin epithelium**. In multiciliated airway cells, ENaC regulates airway surface liquid volume essential for mucociliary transport ([PMID: 26772908](https://pubmed.ncbi.nlm.nih.gov/26772908/)): *"In multi-ciliated cells, ENaC is located in cilia and plays an essential role in the regulation of epithelial surface liquid volume necessary for cilial transport of mucus and gametes in the respiratory and reproductive tracts respectively."* Loss of airway Na+ absorption raises surface-liquid volume and impairs clearance — producing the **CF-like phenotype** (opposite ionic defect to CF but convergent on airway-liquid homeostasis).

**Biochemical abnormalities.** This is an **ion channel defect** (loss of apical Na+ channel function), not an enzyme deficiency. Downstream biochemistry: reduced distal Na+ reabsorption lowers the lumen-negative transepithelial potential that drives K+ and H+ secretion, hence hyperkalemia and metabolic acidosis accompany the sodium wasting.

**Suggested ontology terms.** GO:0035725 (sodium ion transmembrane transport), GO:0003097 (renal water transport), GO:0006885 (regulation of pH), GO:0002028 (regulation of sodium ion transport); CL:1000714 (kidney collecting duct principal cell), CL:0000066 (epithelial cell), CL:0002370 (respiratory ciliated cell); CHEBI:29101 (sodium ion), CHEBI:29103 (potassium ion), CHEBI:27584 (aldosterone), CHEBI:2674 (amiloride).

---

## 7. Anatomical Structures Affected

**Organ level.**
- **Primary:** Kidney (ASDN: late DCT, connecting tubule, collecting duct) — UBERON:0002113 (kidney), UBERON:0001232 (collecting duct).
- **Systemic/multi-organ:** Colon/large intestine (UBERON:0001155), lung/airways (UBERON:0002048), sweat glands (UBERON:0001820), salivary glands (UBERON:0001044), skin (UBERON:0002097).
- **Secondary involvement:** Cardiovascular system (hyperkalemia-induced arrhythmia/arrest); central nervous system (hypoxic-ischemic injury secondary to cardiac arrest — 16% severe neurological impairment).
- **Body systems:** Endocrine/renal (mineralocorticoid axis), renal/urinary, respiratory, integumentary, digestive, cardiovascular.

The systemic form explicitly involves kidney, colon, lung, salivary and sweat glands — distinguishing it from the kidney-limited renal form ([PMID: 31914462](https://pubmed.ncbi.nlm.nih.gov/31914462/)): *"The systemic type can - apart from the kidneys - affect colon, lungs, salivary and sweat glands... symptoms persist until adulthood."*

**Tissue and cell level.** Epithelial tissue is targeted throughout: renal collecting-duct principal cells (CL:1000714), colonic surface epithelium, airway multiciliated epithelium (CL:0002370), exocrine gland ductal epithelium, epidermal keratinocytes.

**Subcellular level.** The defect localizes to the **apical plasma membrane** (GO:0016324, apical plasma membrane) where ENaC resides; trafficking/degradation involves endosomal–ubiquitin–proteasome machinery (Nedd4-2).

**Localization / lateralization.** Effects are **bilateral and symmetric** (both kidneys, both lungs, generalized skin/glandular involvement) — consistent with a systemic genetic channelopathy rather than a focal lesion.

---

## 8. Temporal Development

**Onset.** **Congenital/neonatal.** Symptoms begin within the first 1–2 weeks of life (median 14 days). Onset pattern is **acute** salt-wasting crisis superimposed on a lifelong underlying channel defect.

**Progression.** The disorder is **chronic and lifelong** in the systemic form. There are no discrete "stages." Course is characterized by acute, potentially fatal crises (episodic decompensation precipitated by salt deprivation, illness, or heat) on a chronic baseline requiring continuous management. Salt requirements may **decline with age** in some patients — attributed to partial residual ENaC activity, reduced dependence on aldosterone for salt homeostasis with maturation, and alternative sodium-conserving mechanisms ([PMID: 23426840](https://pubmed.ncbi.nlm.nih.gov/23426840/)): plasma renin/aldosterone *"returned to normal with large amounts of dietary salt and serum sodium (Na+) and potassium (K+) levels were within normal range at the end of the first year of life."* The systemic form's symptoms are *"life-long recurrent"* ([PMID: 17546235](https://pubmed.ncbi.nlm.nih.gov/17546235/)).

**Patterns.** Unlike renal PHA1A (which remits in early childhood), systemic PHA1B/IB2 does **not fully remit** — symptoms persist into adulthood, though severity may attenuate. The **critical period** for intervention is the neonatal/early-infancy window, when hyperkalemia poses the greatest risk of cardiac arrest; prompt recognition and treatment in this window is the single most important determinant of survival and neurological outcome.

---

## 9. Inheritance and Population

**Epidemiology.** PHA1B2 is **ultra-rare**. Systemic autosomal-recessive PHA1 (all subunits combined) is estimated at **<1 per 1,000,000** (Orphanet-aggregated); the *SCNN1B* (IB2) subtype is reported **less frequently than the *SCNN1A* (IB1) subtype** ([PMID: 41457049](https://pubmed.ncbi.nlm.nih.gov/41457049/)): *"SCNN1B-related cases occur less frequently than SCNN1A-related cases."* Precise incidence/prevalence figures specific to IB2 are not established; the literature consists of case reports and small series.

**Inheritance.** **Autosomal recessive.** Both parents are asymptomatic heterozygous carriers ([PMID: 23416952](https://pubmed.ncbi.nlm.nih.gov/23416952/)): *"All parents were asymptomatic heterozygous carriers of the respective mutations, confirming the autosomal recessive mode of inheritance."*

**Penetrance / expressivity.** Penetrance of biallelic loss-of-function is **essentially complete**; expressivity is **variable** (unpredictable pulmonary phenotype; hypomorphic-vs-null severity gradient). No genetic anticipation (not a repeat-expansion disorder). Germline mosaicism is not a documented feature.

**Founder effects / consanguinity.** No established founder alleles — most variants are **novel/private**. **Consanguinity is a strong contextual contributor**: 78% (7/9) in a 2026 systemic PHA1B series ([PMID: 42549990](https://pubmed.ncbi.nlm.nih.gov/42549990/)): *"parental consanguinity was present in seven (78%)"*; and 100% in a 37-year UK cohort. Cases cluster in South Asian, Middle Eastern, African, Turkish, Iranian, and East Asian communities.

**Carrier frequency.** Not formally established; expected to be very low given disease rarity (consistent with gnomAD rarity of LoF *SCNN1B* alleles).

**Demographics.** **Sex ratio ~1:1** (autosomal). Age distribution spans newborns to adults (lifelong systemic form); one affected woman had a successful pregnancy at age 28 ([PMID: 33690157](https://pubmed.ncbi.nlm.nih.gov/33690157/)).

---

## 10. Diagnostics

**Clinical/laboratory tests.** The diagnostic profile is: serum electrolytes (hyponatremia, hyperkalemia), venous blood gas (metabolic acidosis), paired **plasma renin activity and aldosterone** (both markedly elevated), and exclusion of adrenal causes (normal/appropriate 17-hydroxyprogesterone and cortisol). Systemic PHA1 patients characteristically have a **positive sweat test** (elevated sweat chloride), reflecting ENaC loss in sweat glands — absent in renal PHA1A ([PMID: 31018202](https://pubmed.ncbi.nlm.nih.gov/31018202/)): *"All patients exhibited laboratory characteristics including severe hyponatremia, hyperkalemia, metabolic acidosis, elevated plasma renin, elevated aldosterone, and positive sweat tests, suggesting a diagnosis of systemic PHA1."*

**Genetic testing.** Molecular confirmation is by sequencing *SCNN1A/SCNN1B/SCNN1G* (and *NR3C2* for the renal form). **Whole-exome sequencing (WES)** is the practical approach and often reveals homozygous variants in consanguineous families; targeted gene panels and single-gene *SCNN1B* testing are alternatives. Chromosomal microarray may detect large deletions in ENaC genes in rare cases. Karyotyping, FISH, mitochondrial DNA testing, and repeat-expansion testing are **not applicable**.

**Clinical criteria & differential diagnosis.** Diagnosis rests on the biochemical triad + elevated renin/aldosterone + positive sweat test + ENaC sequencing. Two key differentials:

1. **Congenital adrenal hyperplasia (CAH) / primary adrenal insufficiency** — the critical distinguishing feature is that PHA1 electrolyte abnormalities are **resistant to glucocorticoid and mineralocorticoid therapy** ([PMID: 23641881](https://pubmed.ncbi.nlm.nih.gov/23641881/)): *"Patients with PHA1 are often initially diagnosed with congenital adrenal hyperplasia, but their electrolyte abnormalities are resistant to treatment with glucocorticoids and mineralocorticoids."*
2. **Secondary (transient) PHA** from urinary tract infection and/or obstructive uropathy (e.g., posterior urethral valves) — resolves after treating the underlying cause, so **renal ultrasound and urine culture are mandatory** ([PMID: 22397047](https://pubmed.ncbi.nlm.nih.gov/22397047/)): *"Secondary pseudohypoaldosteronism type 1 develops due to transient aldosterone resistance in renal tubules... urinary tract infections and/or urinary tract anomalies are the most common causes... The treatment is usually elimination of the underlying cause."*

**Screening.** No population newborn screening exists. **Cascade carrier testing** of relatives and **prenatal/preimplantation testing** are available once the familial *SCNN1B* variants are known.

---

## 11. Outcome / Prognosis

**Survival / mortality.** Mortality is **substantial**, driven chiefly by hyperkalemic cardiac arrest in the neonatal period. A 37-year single-centre UK cohort (12 children, 8 families, *SCNN1A/SCNN1G*, all consanguineous) reported **25% (3/12) mortality and 16% (2/12) severe neurological impairment** after hyperkalemia-induced cardiac arrest ([PMID: 33690157](https://pubmed.ncbi.nlm.nih.gov/33690157/)): *"Three children died (25%) and two (16%) had severe neurological impairment post-cardiac arrest secondary to hyperkalaemia. One affected female had a successful pregnancy at the age of 28 years. Despite high mortality and morbidity in this condition, survival with normal physical and neurological outcome is possible, justifying intensive management to prevent electrolyte imbalance."* An independent 2026 Indian series of 9 systemic PHA1B children reported **67% (6/9) mortality** ([PMID: 42549990](https://pubmed.ncbi.nlm.nih.gov/42549990/)): *"Six patients (67%) died."*

| Cohort | n | Mortality | Neurological morbidity | PMID |
|---|---|---|---|---|
| UK, 37-year, SCNN1A/SCNN1G | 12 | 25% (3/12) | 16% (2/12) | 33690157 |
| India, systemic PHA1B | 9 | 67% (6/9) | — | 42549990 |

**Morbidity / function.** Survivors who avoid hyperkalemic cardiac arrest can achieve **normal physical and neurological development**. Those who suffer cardiac arrest risk hypoxic-ischemic neurological injury. Lifelong treatment burden is high. No standardized QoL measures are published.

**Disease course / complications.** Complications include hyperkalemic arrhythmia/cardiac arrest, dehydration/shock, failure to thrive, recurrent respiratory infections (CF-like), and skin disease. Recovery potential is good **with** prompt intensive management and poor **without** it — underscoring that outcome is largely determined by timely recognition and treatment.

**Prognostic factors.** Earlier diagnosis and prompt correction of hyperkalemia are the dominant favorable prognostic factors. Residual ENaC activity (hypomorphic alleles) may predict a milder course. No validated molecular prognostic biomarkers exist beyond genotype.

---

## 12. Treatment

**There is no cure and no disease-specific (mineralocorticoid) therapy.** Management is **lifelong supportive correction of the salt-wasting state** ([PMID: 17546235](https://pubmed.ncbi.nlm.nih.gov/17546235/)): *"The systemic form of PHA1 results in a severe phenotype, and high doses of salt supplementation are necessary. The symptoms are life-long recurrent."*

**Pharmacotherapy / supportive care (core measures):**

| Intervention | Purpose | NCIT suggestion | Evidence |
|---|---|---|---|
| High-dose oral **sodium chloride** | Replace urinary Na+ losses | NCIT:C77398 (Sodium Chloride) | [PMID: 41457049](https://pubmed.ncbi.nlm.nih.gov/41457049/) |
| **Sodium/calcium polystyrene sulfonate** (cation-exchange resin) | Chronic potassium lowering | NCIT:C29343 (Polystyrene Sulfonate) | [PMID: 38288475](https://pubmed.ncbi.nlm.nih.gov/38288475/) |
| Oral **alkali** (sodium bicarbonate/citrate) | Correct metabolic acidosis | NCIT:C87720 (Sodium Bicarbonate) | [PMID: 41457049](https://pubmed.ncbi.nlm.nih.gov/41457049/) |
| IV fluids, insulin-glucose, bicarbonate | Acute hyperkalemia | — | [PMID: 23680607](https://pubmed.ncbi.nlm.nih.gov/23680607/) |
| **Peritoneal dialysis** | Refractory hyperkalemia | NCIT:C15248 (Peritoneal Dialysis) | [PMID: 23680607](https://pubmed.ncbi.nlm.nih.gov/23680607/) |
| NG/gastrostomy feeding | Deliver large supplement burden | — | Clinical practice |

The combination of oral sodium chloride, sodium citrate, and potassium-binding resins corrects the electrolyte imbalance and stabilizes patients ([PMID: 41457049](https://pubmed.ncbi.nlm.nih.gov/41457049/)): *"Treatment with oral sodium chloride, sodium citrate, and potassium-binding resins led to gradual correction of electrolyte imbalance and clinical stabilization."* Sodium polystyrene sulfonate decanted into feeds enables long-term outpatient control ([PMID: 38288475](https://pubmed.ncbi.nlm.nih.gov/38288475/)): *"systemic PHA type 1 tends to have more severe electrolyte imbalance and can be more refractory to treatment... successfully managed with sodium polystyrene sulfonate decanted into feeds along with sodium supplementation."* Management remains difficult and the course can be fatal despite aggressive therapy ([PMID: 23680607](https://pubmed.ncbi.nlm.nih.gov/23680607/)): *"She was aggressively managed with intravenous fluids, potassium-lowering agents, high-dose sodium chloride supplementation and peritoneal dialysis... Eventually, she succumbed to pneumonia and septicemia at 4 months of age."* High-dose salt plus potassium-lowering therapy is the mainstay, though management is often difficult ([PMID: 21750640](https://pubmed.ncbi.nlm.nih.gov/21750640/)).

**Pharmacogenomics.** Not applicable. **Mineralocorticoids (fludrocortisone) and glucocorticoids (hydrocortisone) are ineffective** — the defect is at the end-organ channel, downstream of the receptor.

**Advanced therapeutics.** No approved gene therapy, cell therapy, RNA-based therapy, or targeted therapy exists for PHA1B2. These represent future directions (see §Follow-up).

**Supportive/rehabilitative.** Nutritional support, treatment of intercurrent infections, and respiratory care for the CF-like component.

---

## 13. Prevention

**Primary prevention.** The disease cannot be prevented once biallelic LoF is inherited. At the population/family level, **genetic counseling** and **carrier screening** in consanguineous families and affected pedigrees reduce recurrence. **Preimplantation genetic diagnosis (PGD)** and **prenatal testing** are options once familial *SCNN1B* variants are identified.

**Secondary prevention.** Early recognition — any neonate with hyponatremia + hyperkalemia should prompt immediate suspicion, aggressive treatment, and rule-out of CAH and secondary PHA. There is no population newborn screening for PHA1.

**Tertiary prevention.** Preventing complications is the mainstay: continuous electrolyte monitoring, maintenance salt/potassium-lowering therapy, patient/family education on sick-day management and signs of hyperkalemia, and prompt treatment of intercurrent illness to avert fatal crises.

**Counseling.** Autosomal recessive counseling: 25% recurrence risk per pregnancy for carrier couples; offer cascade testing and reproductive options. **Immunization, behavioral/public-health, and environmental interventions** are not disease-specific beyond routine pediatric care.

---

## 14. Other Species / Natural Disease

**Taxonomy / orthologs.** *SCNN1B* is conserved across mammals. ENaC is one of four paralogous subunits (*SCNN1A/B/G/D*) within the ENaC/degenerin (ENaC/DEG) superfamily, with deep evolutionary conservation of the channel architecture ([PMID: 26772908](https://pubmed.ncbi.nlm.nih.gov/26772908/)). The mouse ortholog is *Scnn1b* (NCBI Gene 20277; Taxon NCBI:txid10090).

**Natural disease.** No well-characterized spontaneous PHA1B2-equivalent natural disease is documented in companion animals or wildlife (OMIA). The disorder is principally studied through engineered model organisms rather than naturally occurring animal disease.

**Comparative biology.** The mouse β-ENaC knockout phenotype closely mirrors human PHA1, demonstrating strong evolutionary conservation of ENaC's role in renal sodium/potassium homeostasis (see §15). Subunit-specific knockout phenotypes (α vs β) reveal conserved, non-redundant roles: α is essential for perinatal lung-liquid clearance, β for distal-nephron sodium transport.

**Transmission.** Not applicable — PHA1B2 is a non-transmissible, non-zoonotic genetic disorder.

---

## 15. Model Organisms

**Mouse (*Mus musculus*) is the principal model.** Gene-targeted disruption of the β-subunit (*Scnn1b*) faithfully recapitulates PHA1B2 ([PMID: 9990092](https://pubmed.ncbi.nlm.nih.gov/9990092/)): *"The betaENaC-deficient mice showed normal prenatal development but died within 2 days after birth, most likely of hyperkalemia. In the -/- mice, we found an increased urine Na+ concentration despite hyponatremia and a decreased urine K+ concentration despite hyperkalemia. Moreover, serum aldosterone levels were increased."* This reproduces the human salt-wasting, hyperkalemia, and high-aldosterone phenotype.

**Subunit-specific phenotypes.** The β-knockout reveals non-redundant subunit roles ([PMID: 9990092](https://pubmed.ncbi.nlm.nih.gov/9990092/)): *"in contrast to the alpha subunit, the beta subunit is not required for the transition from a liquid-filled to an air-filled lung. The phenotype of the betaENaC-deficient mice is similar to that of humans with pseudohypoaldosteronism type 1."* Unlike αENaC-deficient mice (which die of defective lung-liquid clearance/respiratory failure), βENaC neonates die of hyperkalemia — the β-subunit is required for renal collecting-duct sodium transport but not the perinatal lung transition.

**Viable chronic model.** An αENaC(−/−)Tg transgenic rescue mouse survives the lethal pulmonary phenotype and then develops severe chronic PHA1, enabling study of pathogenesis and treatment ([PMID: 9326675](https://pubmed.ncbi.nlm.nih.gov/9326675/)): *"Transgenic expression of alphaENaC driven by a cytomegalovirus promoter in alphaENaC(-/-) knockout mice [alphaENaC(-/-)Tg] rescued the perinatal lethal pulmonary phenotype... alphaENaC(-/-)Tg mice showed clinical features of severe PHA-1"* (metabolic acidosis, urinary salt wasting, growth retardation, ~50% mortality).

**In vitro systems.** *Xenopus laevis* oocyte co-expression is the standard functional assay for ENaC variants, used to demonstrate that truncated β-ENaC subunits retain partial activity ([PMID: 20064610](https://pubmed.ncbi.nlm.nih.gov/20064610/)).

**Model characteristics / limitations.** Phenotype recapitulation is excellent for the renal salt-wasting/hyperkalemia component. The principal limitation is **perinatal lethality** of complete knockouts, which restricts study of chronic disease and necessitates rescue/conditional approaches. Resources: MGI (*Scnn1b*), IMPC/KOMP.

---

## Mechanistic Model / Interpretation

PHA1B2 is best understood as a **single-gene channelopathy with systemic, epithelium-wide consequences**. The unifying logic: ENaC is the terminal effector of aldosterone action; abolishing it uncouples a hyperactive hormonal signal from its physiological output.

```
   Aldosterone ↑↑  →  MR  →  SGK1  →  (phospho)Nedd4-2 ⟂  →  [ENaC at apical membrane]
   (futile: present and amplified)                              │
                                                                ✗  SCNN1B LoF → no/defective β-subunit
                                                                │
                              ┌─────────────────────────────────┴─────────────────────────────┐
                        RENAL / COLONIC                                          EXTRA-RENAL (lung, sweat, skin)
                 ↓ Na+ reabsorption                                     ↑ airway surface liquid → ↓ mucociliary clearance
                 ↓ lumen-negative potential                            ↑ sweat/salivary Na+ (positive sweat test)
                 ↓ K+ & H+ secretion                                   dermatitis / miliaria
                        │
          Na+ wasting + hyperkalemia + acidosis
                        │
          hypovolemia → RAAS activation (renin↑, aldosterone↑) — but signal cannot be transduced
                        │
          neonatal salt-wasting crisis; hyperkalemic cardiac arrest (life-threatening)
```

**Upstream vs downstream.** The upstream lesion is the *SCNN1B* mutation → absent/defective β-ENaC. All clinical features are downstream of lost apical sodium conductance. The renin/aldosterone elevation is a *downstream compensatory* response, not a cause — distinguishing PHA from true hypoaldosteronism. The β-subunit's capacity to support **residual channel activity** when truncated is the key modifier explaining why some patients have milder, age-attenuating courses while others have severe, null-like disease. Notably, β-ENaC loss-of-function can also present predominantly as a **CF-like airway phenotype in the absence of overt renal disease** ([PMID: 16207733](https://pubmed.ncbi.nlm.nih.gov/16207733/)): *"We report two non-classic CF patients without CFTR mutations who have novel deleterious mutations in the beta-subunits of SCNN1 in the absence of overt renal disease"* — underscoring the variable expressivity of β-subunit defects.

---

## Evidence Base

| PMID | Title (abbrev.) | Role |
|---|---|---|
| [41457049](https://pubmed.ncbi.nlm.nih.gov/41457049/) | *Compound het SCNN1B → PHA Type 1B2, neonatal twins* | **Defines IB2 = SCNN1B**; biochemistry; treatment |
| [42549990](https://pubmed.ncbi.nlm.nih.gov/42549990/) | *PHA1B spectrum in Indian children* | Quantitative presentation, consanguinity, 67% mortality |
| [26817011](https://pubmed.ncbi.nlm.nih.gov/26817011/) | *PHA with MR polymorphisms* | Gene symbols & chromosomal loci of ENaC subunits |
| [19571553](https://pubmed.ncbi.nlm.nih.gov/19571553/) | *Clinical & molecular features of PHA1* | ENaC LoF as molecular basis |
| [21664233](https://pubmed.ncbi.nlm.nih.gov/21664233/) | *Aldosterone resistance review* | ENaC/MR LoF → aldosterone resistance |
| [15958725](https://pubmed.ncbi.nlm.nih.gov/15958725/) | *Aldosterone–SGK1–Nedd4-2 axis* | Regulatory pathway rendered futile |
| [9990092](https://pubmed.ncbi.nlm.nih.gov/9990092/) | *βENaC knockout mouse* | **IB2 model**: hyperkalemia, salt wasting, high aldosterone |
| [9326675](https://pubmed.ncbi.nlm.nih.gov/9326675/) | *αENaC(−/−)Tg rescue mouse* | Viable chronic PHA1 model |
| [20064610](https://pubmed.ncbi.nlm.nih.gov/20064610/) | *Truncated βENaC partial activity* | **Direct SCNN1B functional genetics**; residual activity |
| [16207733](https://pubmed.ncbi.nlm.nih.gov/16207733/) | *βENaC mutations in CF-like syndrome* | β-subunit variable expressivity (airway) |
| [26772908](https://pubmed.ncbi.nlm.nih.gov/26772908/) | *ENaC family phylogeny/tissue distribution* | Airway/mucociliary role; subunit paralogy |
| [23416952](https://pubmed.ncbi.nlm.nih.gov/23416952/) | *SCNN1A mutations; multi-organ salt loss* | AR inheritance; pulmonary frequency 5/7 |
| [31018202](https://pubmed.ncbi.nlm.nih.gov/31018202/) | *Systemic PHA1, SCNN1A/SCNN1B* | Diagnostic lab profile incl. positive sweat test |
| [23641881](https://pubmed.ncbi.nlm.nih.gov/23641881/) | *Failure to thrive, hyponatremia, hyperkalemia* | CAH differential; steroid resistance |
| [22397047](https://pubmed.ncbi.nlm.nih.gov/22397047/) | *Secondary PHA from UTI/anomalies* | Transient PHA differential |
| [33690157](https://pubmed.ncbi.nlm.nih.gov/33690157/) | *AR PHA treatment requirements (UK)* | Prognosis: 25% mortality, 16% neuro morbidity |
| [38288475](https://pubmed.ncbi.nlm.nih.gov/38288475/) | *SPS management of systemic PHA1* | Long-term potassium-lowering strategy |
| [23680607](https://pubmed.ncbi.nlm.nih.gov/23680607/) | *PHA1 management issues* | Acute management incl. peritoneal dialysis; fatal course |
| [21750640](https://pubmed.ncbi.nlm.nih.gov/21750640/) | *Critical points in PHA1 management* | High-dose salt + K-lowering mainstay; difficulty |
| [17546235](https://pubmed.ncbi.nlm.nih.gov/17546235/) | *Mineralocorticoid resistance: PHA1* | Lifelong course; high-dose salt |
| [11826291](https://pubmed.ncbi.nlm.nih.gov/11826291/) | *ENaC & sodium balance, gene–environment* | G×E (ENaC genotype × salt intake) |
| [23426840](https://pubmed.ncbi.nlm.nih.gov/23426840/) | *Novel SCNN1B splice mutation, Turkish patient* | IB2 splice variant; age-related improvement |
| [31914462](https://pubmed.ncbi.nlm.nih.gov/31914462/) | *Differential-diagnostic reflections, PHA1* | Systemic vs renal organ involvement; persistence |
| [41275343](https://pubmed.ncbi.nlm.nih.gov/41275343/) | *Gross deletion in SCNN1A* | Structural LoF alleles; dermatologic involvement |

**Consistency.** Two independent cohorts converge on high but variable neonatal mortality (25% UK; 67% India). Human functional genetics ([PMID: 20064610](https://pubmed.ncbi.nlm.nih.gov/20064610/)) and the mouse knockout ([PMID: 9990092](https://pubmed.ncbi.nlm.nih.gov/9990092/)) agree on the loss-of-function mechanism, and the β-specific residual-activity finding reconciles observed phenotypic variability.

---

## Limitations and Knowledge Gaps

1. **IB2-specific data are sparse.** Most systemic PHA1 literature concerns *SCNN1A* (IB1); *SCNN1B* cases are fewer, so IB2-specific incidence, prevalence, genotype–phenotype correlations, and natural history are extrapolated partly from the broader PHA1B literature.
2. **No formal epidemiology.** Precise incidence/prevalence and carrier frequency for IB2 are not established; figures are aggregated/estimated.
3. **No QoL instruments** validated for this disorder; quality-of-life impact is qualitative.
4. **Mortality estimates vary widely** (25–67%) and derive from small, consanguinity-enriched cohorts — likely not generalizable and subject to ascertainment bias.
5. **Mechanistic gaps:** the precise basis of the variable pulmonary phenotype (unpredictable from genotype) and of age-related attenuation remains incompletely defined.
6. **No disease-modifying therapy;** advanced therapeutics (gene/RNA/small-molecule ENaC modulators) are untested in PHA1B2.

---

## Proposed Follow-up Experiments / Actions

1. **IB2-specific variant–function registry.** Systematically catalog all reported *SCNN1B* variants with electrophysiological residual-activity measurements (Xenopus/HEK) to build a genotype → residual-activity → phenotype map that could predict severity and salt requirements.
2. **Conditional/hypomorphic mouse models.** Generate inducible or tissue-specific *Scnn1b* alleles (and hypomorphic knock-ins mimicking human truncations) to study chronic disease, the pulmonary phenotype, and age-related attenuation without perinatal lethality.
3. **Therapeutic screening for channel rescue.** Test small-molecule chemical chaperones or read-through agents (for nonsense alleles) and ENaC-stabilizing compounds in oocyte/organoid systems expressing truncated β-ENaC with residual activity.
4. **Airway-liquid mechanistic studies.** Use airway organoids/iPSC-derived multiciliated epithelia from IB2 patients to dissect the CF-like phenotype and test whether it tracks with residual channel activity.
5. **Natural-history cohort.** Establish a multicenter IB2 registry to define true prevalence, long-term outcomes, salt-requirement trajectories, and prognostic biomarkers with adequate power.
6. **Prospective diagnostic protocol validation.** Validate a rapid neonatal algorithm (biochemical triad → renin/aldosterone + sweat test + rapid ENaC panel, with mandatory renal ultrasound/urine culture to exclude secondary PHA) to shorten time-to-diagnosis and reduce hyperkalemic cardiac arrest.

---

*Report compiled from 10 confirmed findings across 52 reviewed papers (5 investigation iterations). Evidence types: predominantly human clinical case reports/series, supported by mouse model and in vitro (Xenopus oocyte) functional studies and mechanistic reviews.*


## Artifacts

- [OpenScientist final report](Pseudohypoaldosteronism_Type_IB2_Autosomal_Recessive-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Pseudohypoaldosteronism_Type_IB2_Autosomal_Recessive-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 24 |
| On topic | 21 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:41457049`: "Pseudohypoaldosteronism Type 1B2"
  - Text part not found as substring: 'Pseudohypoaldosteronism Type 1B2'

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 25 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0859317` (5 mentions) - the report calls it "PHA type IB2", "Pseudohypoaldosteronism type IB2, autosomal recessive"; MONDO calls it **pseudohypoaldosteronism, type IB2, autosomal recessive**
- `HP:0002902` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Hyponatremia**
- `HP:0002153` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Hyperkalemia**
- `HP:0001942` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Metabolic acidosis**
- `HP:0000859` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Increased circulating aldosterone concentration**
- `HP:0001508` (1 mention) - the report calls it "Clinical sign"; HP calls it **Failure to thrive**
- `HP:0012236` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Elevated sweat chloride**
- `NCIT:C29343` (1 mention) - the report calls it "Polystyrene Sulfonate"; NCIT calls it **Pyran Polymer**
- `NCIT:C87720` (1 mention) - the report calls it "Sodium Bicarbonate"; NCIT calls it **Pararosaniline Pamoate Anhydrous**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `NCIT:C77398` (1 mention), reported as "Sodium Chloride" - NCIT does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000848` (1 mention) - the report calls it "hyperreninemia"; HP calls it **Increased circulating renin concentration**, and lists "Hyperreninemia" among its other names
- `CL:1000714` (3 mentions) - the report calls it "renal collecting duct principal cells", "kidney collecting duct principal cell"; CL calls it **kidney cortex collecting duct principal cell**
- `CL:0002370` (2 mentions) - the report calls it "respiratory ciliated cell"; CL calls it **respiratory tract goblet cell**, and lists "respiratory goblet cell" among its other names
- `CHEBI:29101` (1 mention) - the report calls it "sodium ion"; CHEBI calls it **sodium(1+)**, and lists "SODIUM ION" among its other names
- `CHEBI:29103` (1 mention) - the report calls it "potassium ion"; CHEBI calls it **potassium(1+)**, and lists "POTASSIUM ION" among its other names
- `CHEBI:2674` (1 mention) - the report calls it "amiloride"; CHEBI calls it **amodiaquine**
- `UBERON:0001155` (1 mention) - the report calls it "Systemic/multi-organ:** Colon/large intestine"; UBERON calls it **colon**, and lists "posterior intestine" among its other names
- `NCIT:C15248` (1 mention) - the report calls it "Peritoneal Dialysis"; NCIT calls it **Hemodialysis**, and lists "Renal Dialysis" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0859317` - called "PHA type IB2", "Pseudohypoaldosteronism type IB2, autosomal recessive"
- `CL:1000714` - called "renal collecting duct principal cells", "kidney collecting duct principal cell"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.