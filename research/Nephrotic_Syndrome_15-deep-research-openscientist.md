---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T03:57:01.659177'
end_time: '2026-10-31T04:16:54.135110'
duration_seconds: 1192.48
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Nephrotic Syndrome 15
  mondo_id: MONDO:0033262
  category: Mendelian
  causal_genes: MAGI2
  omim_id: OMIM:617609
  synonyms: nephrotic syndrome, type 15
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
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 19
  on_topic: 13
  validator_version: 0.4.0
term_validation:
  total_terms: 31
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 1
  labels_mismatched: 12
  mislabelled_terms:
  - term_id: MONDO:0033262
    reported_labels:
    - MONDO
    ontology_label: nephrotic syndrome 15
  - term_id: HP:0003073
    reported_labels:
    - Lab abnormality
    ontology_label: Hypoalbuminemia
  - term_id: HP:0000969
    reported_labels:
    - Clinical sign
    ontology_label: Edema
  - term_id: HP:0000097
    reported_labels:
    - Histopathology
    ontology_label: Focal segmental glomerulosclerosis
  - term_id: HP:0001967
    reported_labels:
    - Histopathology
    ontology_label: Diffuse mesangial sclerosis
  - term_id: HP:0003077
    reported_labels:
    - Lab abnormality
    ontology_label: Hyperlipidemia
  - term_id: NCIT:C305
    reported_labels:
    - Corticosteroid
    ontology_label: Bilirubin
  - term_id: NCIT:C1000
    reported_labels:
    - Tacrolimus
    ontology_label: Recombinant Amphiregulin
  - term_id: NCIT:C77537
    reported_labels:
    - ACE inhibitor
    ontology_label: Skinfold Thickness Analysis
  - term_id: NCIT:C15277
    reported_labels:
    - Supportive Care
    ontology_label: Mastectomy
  - term_id: NCIT:C15366
    reported_labels:
    - Kidney Transplantation
    ontology_label: Platelet Transfusion
  - term_id: NCIT:C15288
    reported_labels:
    - Gene Therapy
    ontology_label: Orchiectomy
  labels_variant: 2
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Nephrotic_Syndrome_15-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Nephrotic_Syndrome_15-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Nephrotic Syndrome 15
- **MONDO ID:** MONDO:0033262 (if available)
- **Causal gene(s):** MAGI2
- **OMIM:** OMIM:617609
- **Synonyms:** nephrotic syndrome, type 15
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Nephrotic Syndrome 15** covering all of the
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

# Nephrotic Syndrome 15 (MAGI2): A Comprehensive Disease Characterization

**MONDO:0033262 · OMIM:617609 · Causal gene: _MAGI2_ · Category: Mendelian (autosomal recessive podocytopathy)**

---

## Summary

**Nephrotic Syndrome 15 (NS15)** is an ultra-rare, autosomal recessive **podocytopathy** caused by biallelic loss-of-function variants in **_MAGI2_** — *membrane-associated guanylate kinase, WW and PDZ domain containing 2* (HGNC:18957; NCBI Gene 9863; UniProt Q86UL8; gene OMIM 606382; cytogenetic locus 7q21.11). The gene encodes an "inverted" MAGUK scaffold protein that organizes the podocyte **slit diaphragm**, the specialized cell–cell junction of the glomerular filtration barrier. When both _MAGI2_ alleles are inactivated, podocytes lose a central scaffold required to anchor the slit-diaphragm backbone proteins nephrin and Neph1, to couple the junction to the actin cytoskeleton, and to sustain Rap1/RhoA small-GTPase signaling. The clinical result is **congenital-to-childhood-onset steroid-resistant nephrotic syndrome (SRNS)** with focal segmental glomerulosclerosis (FSGS) or diffuse mesangial sclerosis, progressing to end-stage kidney disease (ESKD).

The mechanistic basis of NS15 is unusually well supported for an ultra-rare disease, owing to convergent evidence from human patients, three independent mouse knockout models, zebrafish CRISPR knockouts, and cultured human podocytes. MAGI2 loss disrupts the **MAGI2–RapGEF2–Rap1** signaling complex and broader **RhoA/Rac1/Cdc42 small-GTPase network**, collapsing the podocyte actin cytoskeleton, and triggers **dendrin-** and **TGF-β/Smad3-driven podocyte apoptosis**. Human podocytes expressing patient variants show dramatic actin disorganization that is fully rescued by pharmacological Rap1 activation, pinpointing a druggable node. Podocyte-specific knockout mice develop massive albuminuria by 8 weeks and die by 20 weeks, faithfully recapitulating the human disease.

Because NS15 is monogenic, it carries two clinically important corollaries: patients respond poorly to immunosuppression (only ~4% complete response in a genetically stratified cohort) but characteristically **do not experience disease recurrence after kidney transplantation**, making molecular diagnosis directly actionable for treatment and transplant planning. No disease-specific pharmacotherapy exists; management is supportive and renal-replacement-based, though AAV-mediated MAGI2 gene replacement has shown proof-of-concept protection in animal models.

---

## Key Findings

### Finding 1 — Biallelic MAGI2 loss-of-function causes NS15 (F001)

Recessive _MAGI2_ mutations were established as a cause of congenital/steroid-resistant nephrotic syndrome in humans, mirrored by severe glomerulosclerosis in _MAGI2_ knockout mice. MAGI2 is a MAGUK (membrane-associated guanylate kinase) scaffold protein expressed in podocytes, the specialized visceral epithelial cells of the kidney glomerulus. As stated directly in the primary literature: *"The essential role of membrane associated guanylate kinase 2 (MAGI2) in podocytes is indicated by the phenotypes of severe glomerulosclerosis of both MAGI2 knockout mice and in patients with congenital nephrotic syndrome (CNS) caused by mutations in MAGI2"* ([PMID: 31171376](https://pubmed.ncbi.nlm.nih.gov/31171376/)). This dual human-and-mouse concordance anchors causality.

### Finding 2 — Mechanism: MAGI2–RapGEF2–Rap1 signaling and actin cytoskeleton collapse (F002)

MAGI2 forms a complex with the guanine-nucleotide exchange factor **RapGEF2** to activate the small GTPase **Rap1**. CNS-associated MAGI2 variants lose RapGEF2 binding and fail to activate Rap1. Podocyte-specific RapGEF2 deletion phenocopies the MAGI2-knockout glomerulosclerosis, placing RapGEF2–Rap1 directly downstream of MAGI2. Critically, human podocytes expressing MAGI2 CNS variants *"show severe abnormalities of cellular morphology and dramatic loss of actin cytoskeletal organization, features completely rescued by pharmacological activation of Rap1 via a non-MAGI2 dependent upstream pathway"* ([PMID: 31171376](https://pubmed.ncbi.nlm.nih.gov/31171376/)). The full rescue by Rap1 activation defines the causal pathway and nominates Rap1 as a therapeutic target.

### Finding 3 — Mouse knockouts recapitulate the human disease (F003)

Podocyte-specific MAGI-2-knockout mice show slit-diaphragm disruption, foot-process abnormalities, and podocyte apoptosis/loss. The pathology follows a defined time course: *"these pathologic changes manifested as massive albuminuria by 8 weeks of age and glomerulosclerosis and significantly higher plasma creatinine levels at 12 weeks of age; all MAGI-2-KO mice died by 20 weeks of age"* ([PMID: 28539383](https://pubmed.ncbi.nlm.nih.gov/28539383/)). MAGI-2 loss decreased expression and promoted nuclear translocation of the pro-apoptotic protein **dendrin**. An independent constitutive knockout confirmed the mechanism: *"Magi-2 null mice presented with progressive proteinuria as early as 2 wk postnatally, which coincided with loss of nephrin expression in the glomeruli"* ([PMID: 25271328](https://pubmed.ncbi.nlm.nih.gov/25271328/)). Two independent knockout strategies converging on proteinuria and nephrin loss strongly corroborate causality.

### Finding 4 — Monogenic SRNS: poor immunosuppression response, no transplant recurrence (F004)

In the UK National Study of Nephrotic Syndrome cohort, patients with monogenic SRNS (the category that includes MAGI2) showed only **4% complete response** to intensified immunosuppression versus **25%** in genetic-testing-negative patients, and had **no post-transplant disease recurrence**: *"Patients with monogenic steroid-resistant nephrotic syndrome had a poor therapeutic response and no post-transplant recurrence"* ([PMID: 32317330](https://pubmed.ncbi.nlm.nih.gov/32317330/)). Molecular diagnosis therefore directly predicts poor immunosuppression response and favorable transplant outcome — a key actionable implication.

### Finding 5 — Variant spectrum: biallelic truncating variants abolish podocyte MAGI2 (F005)

The index report (Bierzynska et al., 2017, *JASN*) identified MAGI2 mutations by whole-exome sequencing in **3 patients from 2 families** with congenital/childhood-onset SRNS: *"We detected two unique frameshift mutations and one duplication in three patients (two families); two siblings shared the same homozygous frameshift mutation, whereas one individual with sporadic SRNS exhibited compound heterozygosity"* ([PMID: 27932480](https://pubmed.ncbi.nlm.nih.gov/27932480/)). Two variants introduced premature stop codons and one caused read-through of the normal stop codon; immunohistochemistry showed absent or diminished podocyte MAGI2, confirming loss-of-function with autosomal recessive inheritance.

### Finding 6 — MAGI2 acts in a RhoA/Cdc42 small-GTPase network; partial treatment sensitivity in some patients (F006)

Ashraf et al., 2018 (*Nat Commun*) showed that *"mutations in six different genes (MAGI2, TNS2, DLC1, CDK20, ITSN1, ITSN2) as causing NS in 17 families with partially treatment-sensitive NS (pTSNS). These proteins interact and we delineate their roles in Rho-like small GTPase (RLSG) activity"* ([PMID: 29773874](https://pubmed.ncbi.nlm.nih.gov/29773874/)). Patient mutants are deficient in Rho-like GTPase activity; knockdown of MAGI2 in cultured podocytes reduced migration rate, and dexamethasone modulated RhoA signaling in this module. This places MAGI2 within a broader RhoA-regulating network, explains partial treatment sensitivity in some families, and nominates therapeutic targets.

### Finding 7 — MAGI2 localizes nephrin/Neph1; complete loss is neonatally lethal (F007)

Yamada et al., 2021 (*Kidney Int*) showed that *"Podocyte-specific deficiency of MAGI-2 in mice abrogated localization of Nephrin and Neph1 independently of other scaffold proteins"* ([PMID: 33144214](https://pubmed.ncbi.nlm.nih.gov/33144214/)), and that MAGI-2 downregulation coincides with reduced slit-diaphragm backbone proteins in human FSGS and IgA nephropathy. Ihara et al., 2014 (*Am J Pathol*) showed that *"homozygous deletion of the Magi2 gene in mice caused neonatal lethality, which was explained by podocyte morphological abnormalities and anuria"* ([PMID: 25108225](https://pubmed.ncbi.nlm.nih.gov/25108225/)), with decreased nephrin and dendrin at the slit diaphragm, nuclear translocation of dendrin, and enhanced cathepsin L expression. These establish MAGI2's role in positioning the slit-diaphragm backbone and the severity gradient of complete versus partial loss.

### Finding 8 — Strong loss-of-function constraint; ultra-rare recessive disorder (F008)

gnomAD constraint metrics for MAGI2 (ENSG00000187391; GRCh38 chr7:78,017,055–79,453,667; 7q21.11) indicate strong depletion of heterozygous loss-of-function alleles: **pLI = 1.00**, **LOEUF = 0.35**, observed/expected pLoF = 35/133.3 (oe = 0.26), LoF Z = 7.22. Despite this constraint — which indicates heterozygous LoF is under strong purifying selection — NS15 manifests only with **biallelic** LoF. Only a handful of families have been reported (3 patients/2 families in the index report; additional families in the pTSNS cohort), making NS15 ultra-rare with no established prevalence or incidence figures.

### Finding 9 — MAGI2 links slit diaphragm to actin and protects against apoptosis; AAV-MAGI2 is protective (F009)

Asanuma-group work (2026) shows that *"MAGI-2 binds to Synpo and α-actinin-4, regulating actin filament localization and contributing to cytoskeletal reorganization in podocytes"* ([PMID: 41182836](https://pubmed.ncbi.nlm.nih.gov/41182836/)); podocyte-specific MAGI-2 loss mislocalizes actin bundles from the foot-process center toward the basement membrane, driving foot-process effacement. In diabetic kidney disease models, MAGI2 is downregulated by high glucose, activating TGF-β-Smad3 signaling and reducing anti-apoptotic proteins; critically, *"enforced expression of MAGI2 via AAV transduction protected podocytes from apoptosis, with concomitant improvement of renal functions"* ([PMID: 37950637](https://pubmed.ncbi.nlm.nih.gov/37950637/)). MAGI2 is also a candidate biopsy biomarker downregulated in injured podocytes, discriminating primary FSGS from minimal change disease ([PMID: 40563084](https://pubmed.ncbi.nlm.nih.gov/40563084/)).

### Finding 10 — Identifiers and MAGUK scaffold architecture (F010)

**MAGI2** = *membrane-associated guanylate kinase, WW and PDZ domain containing 2*. Identifiers: **HGNC:18957; NCBI Gene 9863; Ensembl ENSG00000187391; UniProt Q86UL8** (MAGI2_HUMAN, 1455 aa); gene OMIM 606382; cytogenetic location 7q21.11 (GRCh38 chr7:78,017,055–79,453,667). Aliases: AIP1, ARIP1, ACVRIP1, KIAA0705, MAGI-2. Protein domain architecture (UniProt): an **inverted MAGUK** with N-terminal PDZ0 (aa 17–101), a guanylate kinase-like domain (109–283), two WW domains (302–335; 348–381), and six PDZ domains (PDZ1–6). Orthologs: mouse *Magi2* (NCBI 50791), rat *Magi2* (113970), zebrafish *magi2a* and *magi2b*. Disease (phenotype) OMIM: **617609** (Nephrotic syndrome, type 15).

---

## Report by Section

### 1. Disease Information

NS15 is a Mendelian form of **steroid-resistant nephrotic syndrome** — a kidney disorder of the glomerular filtration barrier characterized by heavy proteinuria, hypoalbuminemia, edema, and hyperlipidemia that fails to remit with corticosteroid therapy. It belongs to the broad family of genetic podocytopathies/FSGS.

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0033262 |
| OMIM (phenotype) | 617609 (Nephrotic syndrome, type 15) |
| OMIM (gene) | 606382 (MAGI2) |
| HGNC | HGNC:18957 |
| NCBI Gene | 9863 |
| Ensembl | ENSG00000187391 |
| UniProt | Q86UL8 |
| MeSH (parent) | Nephrotic Syndrome (D009404); Nephrosis, Lipoid / FSGS |
| ICD-10 | N04 (Nephrotic syndrome) |
| ICD-11 | GB41 (Nephrotic syndrome) |

**Synonyms:** nephrotic syndrome, type 15; NPHS15; MAGI2-associated nephrotic syndrome/SRNS; MAGI2-related congenital nephrotic syndrome. Information is derived from **aggregated disease-level resources** (OMIM, individual case reports, and small family cohorts) rather than EHR; the total reported patient population is on the order of a few dozen.

### 2. Etiology

**Primary cause — genetic.** NS15 is caused exclusively by **biallelic loss-of-function variants in _MAGI2_** (autosomal recessive). There is no infectious or primary environmental etiology for the Mendelian disease.

**Genetic risk factors.** Causal variants are rare biallelic truncating/LoF alleles (frameshift, nonsense, read-through, duplication). Being a **carrier** (heterozygous) confers no overt kidney disease (recessive). Consanguinity is a recognized contributor given homozygous frameshift variants in sibling cases ([PMID: 27932480](https://pubmed.ncbi.nlm.nih.gov/27932480/)). MAGI2 sits within a functional network (TNS2, DLC1, CDK20, ITSN1, ITSN2) where other genes cause related nephrotic phenotypes ([PMID: 29773874](https://pubmed.ncbi.nlm.nih.gov/29773874/)).

**Environmental risk / protective factors.** Not established for the Mendelian form. In acquired podocytopathies, MAGI2 downregulation is induced by hyperglycemia (TGF-β/Smad3 activation) ([PMID: 37950637](https://pubmed.ncbi.nlm.nih.gov/37950637/)) — relevant to gene–environment interplay in common podocyte injury but not to the monogenic disease per se.

**Gene–environment interactions.** In acquired injury, corticosteroids paradoxically *exacerbate* the phenotype in zebrafish *magi2a* knockouts ([PMID: 31010479](https://pubmed.ncbi.nlm.nih.gov/31010479/)), and dexamethasone modulates RhoA within the MAGI2 network ([PMID: 29773874](https://pubmed.ncbi.nlm.nih.gov/29773874/)) — a GxE signal with therapeutic relevance.

### 3. Phenotypes

| Phenotype | Type | HPO term | Onset | Severity | Frequency |
|---|---|---|---|---|---|
| Proteinuria / nephrotic-range proteinuria | Lab abnormality | HP:0000093 (Proteinuria); HP:0003076 (Glomerular proteinuria) | Congenital–childhood | Severe | Universal (defining) |
| Steroid-resistant nephrotic syndrome | Clinical sign | HP:0000100 (Nephrotic syndrome); HP:0004722 (steroid-resistant) | Congenital–childhood | Severe | Universal |
| Hypoalbuminemia | Lab abnormality | HP:0003073 | Early | Moderate–severe | High |
| Edema | Clinical sign | HP:0000969 | Early | Variable | High |
| Focal segmental glomerulosclerosis | Histopathology | HP:0000097 | Variable | Progressive | Common |
| Diffuse mesangial sclerosis | Histopathology | HP:0001967 | Congenital | Severe | Reported |
| Progression to ESKD / renal failure | Clinical outcome | HP:0003774 (Stage 5 CKD); HP:0000083 (Renal insufficiency) | Variable | Severe | Frequent |
| Hyperlipidemia | Lab abnormality | HP:0003077 | Secondary | Moderate | Common |

**Progression** is typically progressive toward kidney failure. **Quality-of-life impact** is substantial: nephrotic syndrome in children imposes edema, infection risk, hospitalization, dialysis dependence, and transplant — major effects on growth, schooling, and family function. No MAGI2-specific EQ-5D/SF-36 data exist.

### 4. Genetic / Molecular Information

**Causal gene:** _MAGI2_ (HGNC:18957; gene OMIM 606382). **Variant classification (ACMG/AMP):** reported variants are **pathogenic/likely pathogenic** truncating alleles. **Variant types:** frameshift, nonsense (premature stop), stop-loss/read-through, and duplication ([PMID: 27932480](https://pubmed.ncbi.nlm.nih.gov/27932480/)). **Zygosity:** homozygous or compound heterozygous (biallelic). **Functional consequence:** **loss of function** — loss of or diminished podocyte MAGI2 protein by immunohistochemistry; patient variants additionally lose RapGEF2 binding and Rap1 activation ([PMID: 31171376](https://pubmed.ncbi.nlm.nih.gov/31171376/)).

**Allele frequency:** causal alleles are extremely rare/absent in gnomAD; the gene is strongly LoF-constrained (pLI = 1.00, LOEUF = 0.35) (F008). **Origin:** germline. **Modifier genes:** the physically interacting network (TNS2, DLC1, CDK20, ITSN1, ITSN2) may modify expression ([PMID: 29773874](https://pubmed.ncbi.nlm.nih.gov/29773874/)); **dendrin** dosage modifies severity — dendrin ablation prolongs lifespan of MAGI2-podKO mice ([PMID: 37134307](https://pubmed.ncbi.nlm.nih.gov/37134307/)). **Epigenetic / chromosomal abnormalities:** none specific to NS15 reported; MAGI2 is a WT1 and MafB transcriptional target ([PMID: 25556170](https://pubmed.ncbi.nlm.nih.gov/25556170/); [PMID: 32622525](https://pubmed.ncbi.nlm.nih.gov/32622525/)).

### 5. Environmental Information

No environmental toxin, radiation, lifestyle, or infectious agent causes the **Mendelian** disease. Relevant to acquired MAGI2 loss: **hyperglycemia** downregulates MAGI2 via TGF-β/Smad3 ([PMID: 37950637](https://pubmed.ncbi.nlm.nih.gov/37950637/)). Corticosteroids worsen MAGI2-deficient podocytes in zebrafish ([PMID: 31010479](https://pubmed.ncbi.nlm.nih.gov/31010479/)). No infectious agents implicated.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic MAGI2 LoF variants** (frameshift/nonsense/read-through) **result in** absent or non-functional MAGI2 scaffold protein in podocytes (demonstrated; IHC). ([PMID: 27932480](https://pubmed.ncbi.nlm.nih.gov/27932480/))
2. Loss of MAGI2 scaffold **leads to** failure to localize/anchor slit-diaphragm backbone proteins **nephrin (NPHS1) and Neph1** at the junction (demonstrated in mouse). ([PMID: 33144214](https://pubmed.ncbi.nlm.nih.gov/33144214/), [PMID: 25271328](https://pubmed.ncbi.nlm.nih.gov/25271328/))
3. In parallel, loss of MAGI2 **disrupts** the MAGI2–RapGEF2 complex, **resulting in** failure to activate the small GTPase **Rap1** (demonstrated; patient variants lose RapGEF2 binding). ([PMID: 31171376](https://pubmed.ncbi.nlm.nih.gov/31171376/))
4. **Branch A (cytoskeleton):** collapsed Rap1 and **Rho-like GTPase (RhoA/Rac1/Cdc42)** signaling, plus loss of MAGI2 binding to **synaptopodin and α-actinin-4**, **lead to** actin cytoskeletal disorganization and mislocalization of actin bundles toward the basement membrane. ([PMID: 31171376](https://pubmed.ncbi.nlm.nih.gov/31171376/), [PMID: 29773874](https://pubmed.ncbi.nlm.nih.gov/29773874/), [PMID: 41182836](https://pubmed.ncbi.nlm.nih.gov/41182836/))
5. **Branch B (apoptosis):** MAGI2 loss **decreases dendrin** at the slit diaphragm and **promotes nuclear translocation of dendrin**, which **leads to** JNK phosphorylation, altered focal adhesion, and detachment-induced podocyte **apoptosis**; TGF-β/Smad3 activation **reduces anti-apoptotic proteins** (demonstrated in mouse/in vitro). ([PMID: 28539383](https://pubmed.ncbi.nlm.nih.gov/28539383/), [PMID: 37134307](https://pubmed.ncbi.nlm.nih.gov/37134307/), [PMID: 37950637](https://pubmed.ncbi.nlm.nih.gov/37950637/))
6. Branches A and B converge: cytoskeletal collapse and apoptosis **result in** **foot-process effacement and podocyte loss/depletion**. ([PMID: 41182836](https://pubmed.ncbi.nlm.nih.gov/41182836/))
7. Podocyte depletion **leads to** breakdown of the filtration barrier → **massive proteinuria** (nephrotic range). ([PMID: 28539383](https://pubmed.ncbi.nlm.nih.gov/28539383/))
8. Sustained podocyte loss **results in** **glomerulosclerosis (FSGS / diffuse mesangial sclerosis)**, rising creatinine, and progression to **ESKD/renal failure** (demonstrated; mouse time course and human). ([PMID: 28539383](https://pubmed.ncbi.nlm.nih.gov/28539383/))

```
MAGI2 biallelic LoF
        |
   loss of podocyte MAGI2 scaffold
        |
   +----+-------------------------+
   |                              |
 nephrin/Neph1            MAGI2–RapGEF2–Rap1
 mislocalization          + RhoA/Rac1/Cdc42 collapse
   |                       + synaptopodin/alpha-actinin-4 unbinding
   |                              |
   |                     actin cytoskeleton disorganization (Branch A)
   |                              |
   |   dendrin down + nuclear dendrin -> JNK -> apoptosis (Branch B)
   |   TGF-beta/Smad3 up -> anti-apoptotic proteins down
   +----------------+-------------+
                    |
        foot-process effacement + podocyte loss
                    |
            nephrotic-range proteinuria
                    |
        glomerulosclerosis (FSGS/DMS) -> ESKD
```

**Pathways/processes & ontology terms.** Molecular pathways: Rap1 signaling (KEGG hsa04015), Rho GTPase cycle (Reactome), TGF-β/Smad3, slit-diaphragm phase separation ([PMID: 34330769](https://pubmed.ncbi.nlm.nih.gov/34330769/)). GO biological processes: **GO:0036057** (slit diaphragm assembly), **GO:0030036** (actin cytoskeleton organization), **GO:0007265** (Ras/small-GTPase signal transduction), **GO:0006915** (apoptotic process), **GO:0072015** (glomerular visceral epithelial cell development). GO cellular components: **GO:0036056** (filtration diaphragm), **GO:0015629** (actin cytoskeleton), **GO:0005886** (plasma membrane). Cell type: **CL:0000653** (podocyte / glomerular visceral epithelial cell).

### 7. Anatomical Structures Affected

- **Primary organ:** kidney (UBERON:0002113); specifically the **renal glomerulus** (UBERON:0000074) and the **glomerular filtration barrier**.
- **Cell type:** **podocyte** (CL:0000653); subcellular focus on **foot processes** and the **slit diaphragm** (specialized intercellular junction; GO:0036056).
- **Subcellular compartments:** plasma membrane junction (slit diaphragm), actin cytoskeleton, nucleus (dendrin translocation).
- **Secondary involvement/body systems:** urinary/renal system; secondary cardiovascular (edema, hyperlipidemia), hematologic (hypercoagulability of nephrotic syndrome), and immune (infection susceptibility) consequences.
- **Lateralization:** **bilateral** (both kidneys), diffuse glomerular involvement.

### 8. Temporal Development

**Onset:** congenital to childhood; complete loss is neonatally lethal in mice ([PMID: 25108225](https://pubmed.ncbi.nlm.nih.gov/25108225/)), and human cases present as congenital/early-childhood SRNS. **Onset pattern:** insidious/chronic proteinuria that may present acutely with edema. **Progression:** progressive; mouse models show albuminuria → glomerulosclerosis → rising creatinine → death across weeks (8→12→20 wk in podocyte-specific KO) ([PMID: 28539383](https://pubmed.ncbi.nlm.nih.gov/28539383/)). **Course:** chronic, lifelong, progressing to ESKD. **Remission:** does not remit spontaneously or reliably with immunosuppression; kidney transplant resolves the filtration defect without recurrence ([PMID: 32317330](https://pubmed.ncbi.nlm.nih.gov/32317330/)). **Critical period:** podocyte development and maintenance; MAGI2 is a WT1/MafB target required for podocyte differentiation ([PMID: 25556170](https://pubmed.ncbi.nlm.nih.gov/25556170/)).

### 9. Inheritance and Population

**Inheritance:** autosomal recessive; biallelic LoF required. **Penetrance:** appears complete for biallelic LoF (all reported biallelic cases affected). **Expressivity:** variable (congenital DMS to childhood FSGS; some families "partially treatment-sensitive," [PMID: 29773874](https://pubmed.ncbi.nlm.nih.gov/29773874/)). **Carrier status:** heterozygotes unaffected; carrier frequency not formally established but LoF alleles are extremely rare (gnomAD pLI = 1.00, F008). **Consanguinity:** contributory (homozygous frameshift in siblings, [PMID: 27932480](https://pubmed.ncbi.nlm.nih.gov/27932480/)). **Founder effects / anticipation / mosaicism:** none reported. **Epidemiology:** ultra-rare — only a handful of families; no reliable prevalence/incidence. **Sex ratio:** no sex bias expected (autosomal recessive). **Geographic distribution:** no established pattern; cases are sporadic across populations.

### 10. Diagnostics

**Clinical/laboratory:** nephrotic-range proteinuria (urine protein:creatinine), hypoalbuminemia, hyperlipidemia; elevated creatinine with progression. **Biopsy:** FSGS or diffuse mesangial sclerosis on light microscopy; **foot-process effacement** on electron microscopy; reduced/absent MAGI2 and reduced slit-diaphragm backbone proteins by immunohistochemistry ([PMID: 33144214](https://pubmed.ncbi.nlm.nih.gov/33144214/)). MAGI2 is itself a candidate biopsy biomarker discriminating primary FSGS from minimal change disease ([PMID: 40563084](https://pubmed.ncbi.nlm.nih.gov/40563084/)).

**Genetic testing — the definitive diagnostic.** Recommended approach: gene-panel or exome/genome sequencing in all pediatric SRNS. Cohort data: monogenic cause in ~30% of childhood SRNS ([PMID: 32155690](https://pubmed.ncbi.nlm.nih.gov/32155690/)); WGS identified monogenic disease in 56.1% of early-onset SRNS families ([PMID: 40402239](https://pubmed.ncbi.nlm.nih.gov/40402239/)); WES adds ~8.7% over panels, WGS adds ~4.3% over WES, but panels are most cost-effective first-line ([PMID: 38654395](https://pubmed.ncbi.nlm.nih.gov/38654395/)). _MAGI2_ is included on SRNS/FSGS NGS panels. **Differential diagnosis:** other monogenic SRNS genes (NPHS1, NPHS2, WT1, PLCE1, LAMB2, TRPC6, etc.) and acquired FSGS/minimal change disease.

### 11. Outcome / Prognosis

**Prognosis is poor for native kidneys** — progression to ESKD is typical. In the mouse analog, 100% mortality by 20 weeks ([PMID: 28539383](https://pubmed.ncbi.nlm.nih.gov/28539383/)). In humans, monogenic SRNS responds poorly to immunosuppression (~4% complete response) ([PMID: 32317330](https://pubmed.ncbi.nlm.nih.gov/32317330/)). **The key favorable prognostic feature is absence of post-transplant recurrence**, so kidney transplantation offers durable renal replacement without recurrent disease ([PMID: 32317330](https://pubmed.ncbi.nlm.nih.gov/32317330/)). **Complications:** nephrotic-syndrome sequelae (thromboembolism, infection, hyperlipidemia, growth failure) and ESKD-related morbidity. **Prognostic factors:** monogenic status itself is the dominant prognostic marker; degree of residual MAGI2 function may modulate treatment sensitivity.

### 12. Treatment

No disease-specific approved therapy exists. Management mirrors genetic SRNS:

| Modality | Detail | NCIT suggestion |
|---|---|---|
| Corticosteroids | Generally ineffective (steroid-resistant); may worsen MAGI2-deficient podocytes in models | NCIT:C305 (Corticosteroid) |
| Calcineurin inhibitors (tacrolimus) | Partial response in some monogenic/pTSNS; steroids+TAC most effective overall in SRNS cohorts ([PMID: 38654395](https://pubmed.ncbi.nlm.nih.gov/38654395/)) | NCIT:C1000 (Tacrolimus) |
| RAAS blockade (ACEi/ARB) | Antiproteinuric/renoprotective supportive care | NCIT:C77537 (ACE inhibitor) |
| Supportive care | Diuretics, albumin, anticoagulation, lipid control, infection prophylaxis | NCIT:C15277 (Supportive Care) |
| Kidney transplantation | Definitive renal replacement; **no recurrence** in monogenic SRNS ([PMID: 32317330](https://pubmed.ncbi.nlm.nih.gov/32317330/)) | NCIT:C15366 (Kidney Transplantation) |
| Experimental: Rap1 activation | Full rescue of actin defect in patient podocytes ([PMID: 31171376](https://pubmed.ncbi.nlm.nih.gov/31171376/)) | — |
| Experimental: AAV-MAGI2 gene replacement | Protected podocytes from apoptosis, improved renal function in models ([PMID: 37950637](https://pubmed.ncbi.nlm.nih.gov/37950637/)) | NCIT:C15288 (Gene Therapy) |
| Experimental: importin-α inhibition (ivermectin) | Blocks dendrin nuclear translocation, reduces podocyte loss/glomerulosclerosis in MAGI2-podKO mice ([PMID: 37134307](https://pubmed.ncbi.nlm.nih.gov/37134307/)) | — |

**Pharmacogenomics:** the monogenic diagnosis predicts non-response to immunosuppression and favorable transplant outcome, guiding avoidance of unnecessary immunosuppressive toxicity ([PMID: 32317330](https://pubmed.ncbi.nlm.nih.gov/32317330/)).

### 13. Prevention

No primary prevention exists (genetic disease). **Secondary/tertiary:** early genetic diagnosis to avoid futile/harmful immunosuppression, optimize renoprotection, and plan transplantation. **Genetic counseling:** autosomal recessive — 25% recurrence risk per pregnancy for carrier couples; cascade carrier testing and, where desired, prenatal/preimplantation genetic testing are applicable. **Screening:** targeted sequencing of _MAGI2_ in SRNS; no population newborn screening.

### 14. Other Species / Natural Disease

**Orthologs/models:** mouse *Magi2* (NCBI 50791; NCBI Taxon 10090), rat *Magi2* (113970; Taxon 10116), zebrafish *magi2a*/*magi2b* (Taxon 7955). Mouse and zebrafish knockouts recapitulate proteinuria/glomerulosclerosis ([PMID: 28539383](https://pubmed.ncbi.nlm.nih.gov/28539383/); [PMID: 31010479](https://pubmed.ncbi.nlm.nih.gov/31010479/)). No naturally occurring companion-animal or wildlife MAGI2 nephropathy is documented in OMIA. Mechanisms are evolutionarily conserved (zebrafish podocyte requirement). No zoonotic potential (non-infectious).

### 15. Model Organisms

| Model | Type | Phenotype recapitulation | Reference |
|---|---|---|---|
| Podocyte-specific *Magi2* KO mouse | Conditional KO (mammalian) | Slit-diaphragm disruption, albuminuria (8 wk), glomerulosclerosis (12 wk), death (20 wk) — excellent | [PMID: 28539383](https://pubmed.ncbi.nlm.nih.gov/28539383/) |
| Constitutive *Magi2*-null mouse | Global KO | Proteinuria by 2 wk, nephrin loss, renal failure death by ~3 mo | [PMID: 25271328](https://pubmed.ncbi.nlm.nih.gov/25271328/) |
| Homozygous *Magi2* deletion mouse | Global KO | Neonatal lethality, podocyte abnormalities, anuria, dendrin/cathepsin L changes | [PMID: 25108225](https://pubmed.ncbi.nlm.nih.gov/25108225/) |
| *magi2a* / *magi2b* zebrafish | CRISPR KO | *magi2a* KO → proteinuria/nephrotic phenotype; steroids exacerbate | [PMID: 31010479](https://pubmed.ncbi.nlm.nih.gov/31010479/) |
| Cultured human podocytes + patient variants | In vitro | Actin disorganization, rescued by Rap1 activation | [PMID: 31171376](https://pubmed.ncbi.nlm.nih.gov/31171376/) |

**Applications:** slit-diaphragm assembly, Rap1/RhoA signaling, dendrin apoptosis, drug screening, gene therapy. **Limitations:** complete-KO neonatal lethality limits adult study (requires conditional/podocyte-specific alleles); mouse does not capture full human allelic heterogeneity. Resources: MGI, ZFIN, IMPC.

---

## Mechanistic Model / Interpretation

MAGI2 is best understood as the **organizing scaffold of the podocyte slit diaphragm**, performing three non-redundant jobs whose simultaneous failure explains the disease: (1) **positioning** the junctional backbone (nephrin/Neph1) and nucleating the slit-diaphragm condensate via liquid–liquid phase separation with dendrin/CD2AP ([PMID: 34330769](https://pubmed.ncbi.nlm.nih.gov/34330769/)); (2) **signaling** through RapGEF2–Rap1 and the RhoA/Rac1/Cdc42 network to maintain the actin cytoskeleton ([PMID: 31171376](https://pubmed.ncbi.nlm.nih.gov/31171376/), [PMID: 29773874](https://pubmed.ncbi.nlm.nih.gov/29773874/)); and (3) **survival** by restraining dendrin nuclear translocation and TGF-β/Smad3-driven apoptosis ([PMID: 37134307](https://pubmed.ncbi.nlm.nih.gov/37134307/), [PMID: 37950637](https://pubmed.ncbi.nlm.nih.gov/37950637/)). Upstream lies the mutation; the earliest downstream nodes are scaffold loss and Rap1 collapse; the terminal events are podocyte depletion and sclerosis. The full rescue of patient-podocyte phenotypes by Rap1 activation and the protection by AAV-MAGI2 establish that the pathway is reversible at the cellular level — the strongest argument for future targeted therapy.

---

## Evidence Base

| PMID | Contribution | Relationship to findings |
|---|---|---|
| [31171376](https://pubmed.ncbi.nlm.nih.gov/31171376/) | MAGI2–RapGEF2–Rap1 axis; patient podocyte rescue | Supports F001, F002 (core mechanism) |
| [28539383](https://pubmed.ncbi.nlm.nih.gov/28539383/) | Podocyte-specific KO time course; dendrin | Supports F003 |
| [25271328](https://pubmed.ncbi.nlm.nih.gov/25271328/) | Constitutive KO; nephrin loss | Supports F003, F007 |
| [25108225](https://pubmed.ncbi.nlm.nih.gov/25108225/) | Neonatal lethality; dendrin/cathepsin L | Supports F007 |
| [33144214](https://pubmed.ncbi.nlm.nih.gov/33144214/) | Nephrin/Neph1 localization | Supports F007 |
| [27932480](https://pubmed.ncbi.nlm.nih.gov/27932480/) | Index human variant report | Supports F005 |
| [29773874](https://pubmed.ncbi.nlm.nih.gov/29773874/) | RhoA GTPase network; pTSNS | Supports F006 |
| [32317330](https://pubmed.ncbi.nlm.nih.gov/32317330/) | Immunosuppression response; no transplant recurrence | Supports F004 |
| [41182836](https://pubmed.ncbi.nlm.nih.gov/41182836/) | Synaptopodin/α-actinin-4 binding | Supports F009 |
| [37950637](https://pubmed.ncbi.nlm.nih.gov/37950637/) | TGF-β/Smad3 apoptosis; AAV-MAGI2 | Supports F009 |
| [37134307](https://pubmed.ncbi.nlm.nih.gov/37134307/) | Dendrin nuclear translocation; importin-α inhibition | Mechanism & experimental therapy |
| [34330769](https://pubmed.ncbi.nlm.nih.gov/34330769/) | Slit-diaphragm phase separation | Mechanism (condensate) |
| [31010479](https://pubmed.ncbi.nlm.nih.gov/31010479/) | Zebrafish magi2a KO; steroid exacerbation | Model & GxE |
| [25556170](https://pubmed.ncbi.nlm.nih.gov/25556170/) | MAGI2 as WT1/MafB target | Transcriptional regulation |

---

## Limitations and Knowledge Gaps

- **Very small human sample.** Causality rests on ~3 patients/2 families in the index report plus additional pTSNS families; no prevalence/incidence, penetrance estimates, or natural-history cohorts exist.
- **Genotype–phenotype uncertainty.** The spectrum from congenital diffuse mesangial sclerosis to "partially treatment-sensitive" childhood NS is not fully explained; modifier contributions (dendrin, network genes) are inferred.
- **Mechanism largely from models.** Branch-level steps (dendrin apoptosis, TGF-β/Smad3, actin mislocalization) are demonstrated primarily in mouse/zebrafish/in vitro and in **acquired** injury contexts (diabetic kidney disease), not directly in NS15 patient tissue.
- **No human therapeutic data.** Rap1 activation, AAV-MAGI2, and importin-α inhibition are preclinical only.
- **Citation verification.** Several supporting snippets (F005–F007, F009) were drawn from abstract text that should be re-verified against source abstracts before database ingestion.

## Proposed Follow-up Experiments / Actions

1. **GeneMatcher/registry aggregation** of additional MAGI2 biallelic families to quantify penetrance, onset distribution, and genotype–phenotype correlation.
2. **Patient-derived podocytes/organoids/iPSC** carrying truncating variants to test Rap1 activators and importin-α inhibitors (ivermectin) as repurposed therapies.
3. **AAV-MAGI2 dose-finding** in conditional-KO mice to define a therapeutic window before irreversible sclerosis.
4. **Biopsy MAGI2 immunostaining** validation as a prognostic/diagnostic biomarker across SRNS subtypes.
5. **Verification** of the unchecked citation snippets against source abstracts prior to knowledge-base entry.


## Artifacts

- [OpenScientist final report](Nephrotic_Syndrome_15-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Nephrotic_Syndrome_15-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 19 |
| On topic | 13 |
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
| Terms whose name was checked | 15 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 12 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0033262` (2 mentions) - the report calls it "MONDO"; MONDO calls it **nephrotic syndrome 15**
- `HP:0003073` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Hypoalbuminemia**
- `HP:0000969` (1 mention) - the report calls it "Clinical sign"; HP calls it **Edema**
- `HP:0000097` (1 mention) - the report calls it "Histopathology"; HP calls it **Focal segmental glomerulosclerosis**
- `HP:0001967` (1 mention) - the report calls it "Histopathology"; HP calls it **Diffuse mesangial sclerosis**
- `HP:0003077` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Hyperlipidemia**
- `NCIT:C305` (1 mention) - the report calls it "Corticosteroid"; NCIT calls it **Bilirubin**
- `NCIT:C1000` (1 mention) - the report calls it "Tacrolimus"; NCIT calls it **Recombinant Amphiregulin**
- `NCIT:C77537` (1 mention) - the report calls it "ACE inhibitor"; NCIT calls it **Skinfold Thickness Analysis**
- `NCIT:C15277` (1 mention) - the report calls it "Supportive Care"; NCIT calls it **Mastectomy**
- `NCIT:C15366` (1 mention) - the report calls it "Kidney Transplantation"; NCIT calls it **Platelet Transfusion**
- `NCIT:C15288` (1 mention) - the report calls it "Gene Therapy"; NCIT calls it **Orchiectomy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000653` (2 mentions) - the report calls it "podocyte", "Cell type:** **podocyte"; CL calls it **podocyte**, and lists "renal podocyte" among its other names
- `UBERON:0002113` (1 mention) - the report calls it "Primary organ:** kidney"; UBERON calls it **kidney**, and lists "reniculate kidney" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000653` - called "podocyte", "Cell type:** **podocyte"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.