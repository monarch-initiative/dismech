---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-27T17:59:10.084772'
end_time: '2026-10-27T18:34:22.190413'
duration_seconds: 2112.11
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Combined Oxidative Phosphorylation Deficiency 52
  mondo_id: MONDO:0030311
  category: Mendelian
  causal_genes: NFS1
  omim_id: OMIM:619386
  synonyms: COXPD52
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
citation_count: 10
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 10
  quotes_valid: 10
  relevance_assessed: 11
  on_topic: 8
  validator_version: 0.4.0
term_validation:
  total_terms: 33
  verified: 31
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 11
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0030311
    reported_labels:
    - MONDO
    ontology_label: combined oxidative phosphorylation deficiency 52
  - term_id: HP:0003128
    reported_labels:
    - Lactic acidosis
    - Lab abnormality
    ontology_label: Lactic acidosis
  - term_id: HP:0001252
    reported_labels:
    - Hypotonia
    - Clinical sign
    ontology_label: Hypotonia
  - term_id: HP:0012378
    reported_labels:
    - Fatigue
    - Symptom
    ontology_label: Fatigue
  - term_id: HP:0003542
    reported_labels:
    - Increased muscle lactate
    - Lab abnormality
    ontology_label: Increased circulating pyruvate concentration
  - term_id: NCIT:C15417
    reported_labels:
    - Genetic counseling
    ontology_label: Randomized Clinical Trial
  - term_id: HP:0011024
    reported_labels:
    - Symptom
    ontology_label: Abnormality of the gastrointestinal tract
  labels_variant: 4
  obsolete_terms:
  - term_id: GO:0097428
    ontology_label: obsolete protein maturation by iron-sulfur cluster transfer
    replaced_by: GO:0051604
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Combined_Oxidative_Phosphorylation_Deficiency_52-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Combined_Oxidative_Phosphorylation_Deficiency_52-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Oxidative Phosphorylation Deficiency 52
- **MONDO ID:** MONDO:0030311 (if available)
- **Causal gene(s):** NFS1
- **OMIM:** OMIM:619386
- **Synonyms:** COXPD52
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Combined Oxidative Phosphorylation Deficiency 52** covering all of the
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

# Combined Oxidative Phosphorylation Deficiency 52 (COXPD52): A Comprehensive Disease Characteristics Report

**Disease:** Combined Oxidative Phosphorylation Deficiency 52 (COXPD52)
**Causal gene:** **NFS1** (cysteine desulfurase, 20q11.22; UniProt Q9Y697; NCBI Gene 9054; HGNC:7808)
**MONDO ID:** MONDO:0030311 · **OMIM:** #619386 · **Synonym:** COXPD52
**Inheritance:** Autosomal recessive · **Category:** Mendelian, ultra-rare mitochondrial disease

---

## Summary

**Combined Oxidative Phosphorylation Deficiency 52 (COXPD52) is an ultra-rare autosomal recessive mitochondrial disease caused by biallelic hypomorphic variants in *NFS1***, the nuclear gene encoding the sole mitochondrial **cysteine desulfurase**—the enzyme that initiates iron–sulfur (Fe–S) cluster biogenesis. Because NFS1 mobilizes sulfur from L-cysteine to build the [2Fe–2S] clusters that mature downstream Fe–S enzymes, reduction of its activity produces a *combined* deficiency affecting multiple mitochondrial and extra-mitochondrial Fe–S-dependent processes simultaneously. The disease was first defined in 2014 under the descriptive name "infantile mitochondrial complex II/III deficiency," and later subsumed under the OMIM COXPD series as entry #619386.

The clinical spectrum is **genotype-correlated and strikingly variable**. At the severe end, infants homozygous for the recurrent missense variant **c.215G>A (p.Arg72Gln)** present in the neonatal/infantile period with lactic acidemia, hypotonia, muscle weakness, abnormal mitochondrial morphology on muscle biopsy, combined respiratory-chain complex II+III (variably I) deficiency, and multisystem organ failure that is frequently fatal. At the mild end, a compound heterozygous patient (p.Arg72Gln / p.Arg412His) survived to present as a young adult with gastrointestinal symptoms and fatigue. This phenotypic breadth reflects NFS1's position as the **rate-limiting, upstream node** of the entire cellular Fe–S supply chain: its sulfur output feeds the respiratory chain, the TCA-cycle aconitases, lipoic acid synthesis, the cytosolic iron–sulfur assembly (CIA) pathway (including DNA replication/repair enzymes), and tRNA thiolation.

There is **no disease-specific or approved therapy**; management is supportive mitochondrial care (treatment of lactic acidosis, nutritional support, cofactor/"mitochondrial cocktail" supplementation, and avoidance of metabolic decompensation). Diagnosis rests on **exome or genome sequencing** demonstrating biallelic *NFS1* variants, supported by a characteristic biochemical signature: elevated blood/CSF lactate, abnormal mitochondria on muscle biopsy, combined complex II/III (±I) deficiency, and—distinctively—reduced activity of **both mitochondrial and cytosolic aconitases**, which separates COXPD52 from mtDNA-encoded respiratory defects. This report synthesizes eight confirmed findings across 35 reviewed papers, organized against the 15-section disease-characteristics template.

---

## Key Findings

### Finding 1 — COXPD52 is an autosomal recessive mitochondrial disease caused by biallelic *NFS1* variants

COXPD52 (OMIM #619386; MONDO:0030311) is caused by biallelic pathogenic variants in **NFS1** (cysteine desulfurase, chromosome 20q11.22). The founding report by Farhan et al. (2014) used autozygosity mapping combined with exome sequencing in a consanguineous family to identify the homozygous variant **c.215G>A, p.Arg72Gln** in an infant with what the authors termed "infantile mitochondrial complex II/III deficiency, a novel autosomal recessive mitochondrial disease characterized by lactic acidemia, hypotonia, respiratory chain complex II and III deficiency, multisystem organ failure and abnormal mitochondria" [PMID: 24498631]. The same study reported that "we identified c.215G>A, p.Arg72Gln in NFS1 as the likely causative mutation."

The disease entity and its causal gene were corroborated and expanded by Yang et al. (2022), who reported three additional unrelated patients: "The c.215G>A p.(Arg72Gln) variant in NFS1 has been previously reported to cause infantile mitochondrial complex II and III deficiency. We describe three additional unrelated patients with the same missense variant" [PMID: 35026043]. The recurrence of the *same* missense allele across unrelated families, together with autosomal recessive segregation, firmly establishes *NFS1* as the single causal gene for this Mendelian disorder.

> **Evidence type:** Human clinical / genetic. **Key PMIDs:** [24498631](https://pubmed.ncbi.nlm.nih.gov/24498631/), [35026043](https://pubmed.ncbi.nlm.nih.gov/35026043/).

### Finding 2 — NFS1 is the catalytic core of the mitochondrial Fe–S assembly complex; p.Arg72Gln impairs cysteine desulfurase activity

NFS1 is the catalytic cysteine desulfurase at the heart of the mitochondrial **iron–sulfur cluster (ISC) assembly complex**. It functions in a multi-subunit core together with ISD11 (LYRM4), mitochondrial acyl carrier protein (ACP), and the scaffold protein ISCU2, and is allosterically activated by frataxin (FXN), with electrons supplied by ferredoxin-2 (FDX2). Maio et al. (2020) describe how structural work on "the human cysteine desulfurase NFS1, in complex with the LYR protein ISD11, the acyl carrier protein ACP, and the main scaffold ISCU, have shed light on the molecular interactions that govern initial cluster assembly on ISCU" [PMID: 31918395]. NFS1 abstracts sulfur from L-cysteine to build [2Fe–2S] clusters on ISCU2.

In patients, the functional consequences of reduced NFS1 activity are broad. Yang et al. (2022) found that "functional analyses demonstrated decreased activity in respiratory chain complex II and variably in complexes I and III. We found decreased mitochondrial and cytosolic aconitase activities but only mildly affected lipoylation" of PDH/2-OGDH [PMID: 35026043]. The p.Arg72Gln residue lies adjacent to the catalytic machinery; its substitution reduces—but does not abolish—desulfurase output, consistent with a **hypomorphic** rather than null mechanism, and the deficit propagates to multiple Fe–S-dependent enzymes in both mitochondrial and cytosolic compartments.

> **Evidence type:** Human clinical + structural/in vitro. **Key PMIDs:** [31918395](https://pubmed.ncbi.nlm.nih.gov/31918395/), [35026043](https://pubmed.ncbi.nlm.nih.gov/35026043/).

### Finding 3 — The phenotypic spectrum ranges from fatal infantile multisystem disease to milder adult-onset fatigue/GI disease

COXPD52 phenotype is variable and correlates with genotype. At the **severe infantile end** (homozygous p.Arg72Gln), patients present with neonatal/infantile-onset lactic acidemia, hypotonia, weakness, combined respiratory-chain complex II+III deficiency, abnormal mitochondrial morphology, and multisystem organ failure [PMID: 24498631]. Yang et al. (2022) reported that "Two infants with the same homozygous variant presented with hypotonia, weakness and lactic acidosis," with abnormal mitochondrial morphology on muscle biopsy and decreased complex II (variably I/III) activity. At the **mild end**, the same study noted that "one patient with compound heterozygous p.(Arg72Gln) and p.(Arg412His) variants presented as a young adult with gastrointestinal symptoms and fatigue" [PMID: 35026043].

**Suggested HPO terms:** HP:0001942 (Metabolic acidosis) / HP:0003128 (Lactic acidosis); HP:0001252 (Hypotonia); HP:0003198 (Myopathy) / HP:0001324 (Muscle weakness); HP:0003200 (Ragged-red muscle fibers / abnormal mitochondria); HP:0011968 (Feeding difficulties); HP:0002024 (Malabsorption); HP:0012378 (Fatigue); HP:0003542 (Increased muscle lactate).

> **Evidence type:** Human clinical. **Key PMIDs:** [24498631](https://pubmed.ncbi.nlm.nih.gov/24498631/), [35026043](https://pubmed.ncbi.nlm.nih.gov/35026043/).

### Finding 4 — NFS1 supplies sulfur for mitochondrial AND cytosolic Fe–S enzymes, tRNA thiolation, and genome maintenance; broad loss explains multisystem disease

NFS1 is the **sole mitochondrial cysteine desulfurase** and the rate-limiting enzyme of Fe–S cluster biogenesis. Its sulfur output feeds three major branches: (i) **mitochondrial Fe–S enzymes**—respiratory complexes I/II/III, mitochondrial aconitase (ACO2), and lipoic acid synthase; (ii) the **cytosolic iron–sulfur assembly (CIA) pathway**, which matures cytosolic and nuclear Fe–S proteins including cytosolic aconitase/IRP1 (ACO1) and multiple DNA replication/repair enzymes; and (iii) **tRNA thiolation**. Zhu et al. (2025) note that NFS1 "participates in numerous critical cellular processes, including iron-sulfur (Fe-S) cluster biosynthesis and tRNA thiolation" [PMID: 40141425].

The breadth of this dependency directly explains the multisystem clinical picture. Zangari et al. (2025) demonstrate that "NFS1 inhibition by D-Cys affects all cellular iron-sulfur cluster-dependent functions, including mitochondrial respiration, nucleotide metabolism and maintenance of genome integrity, leading to decreased oxygen consumption, DNA damage and cell cycle arrest" [PMID: 40797101]. Patient biochemistry confirms the combined mitochondrial + cytosolic aconitase deficiency predicted by this model [PMID: 35026043].

**Suggested GO terms:** GO:0016226 (iron-sulfur cluster assembly); GO:0031071 (cysteine desulfurase activity); GO:0097428 (protein maturation by iron-sulfur cluster transfer); GO:0002143 (tRNA wobble position thiouridine biosynthesis). **Cellular component:** GO:0005759 (mitochondrial matrix), GO:0005829 (cytosol). **CHEBI:** L-cysteine (CHEBI:17561), iron-sulfur cluster (CHEBI:30408).

> **Evidence type:** In vitro / cell biology + human clinical. **Key PMIDs:** [40797101](https://pubmed.ncbi.nlm.nih.gov/40797101/), [40141425](https://pubmed.ncbi.nlm.nih.gov/40141425/), [35026043](https://pubmed.ncbi.nlm.nih.gov/35026043/).

### Finding 5 — NFS1 is a PLP (vitamin B6)-dependent, intrinsically low-activity desulfurase requiring frataxin activation

NFS1 is a **pyridoxal 5′-phosphate (PLP, vitamin B6)-dependent** enzyme. Patra & Barondeau (2019) describe the core assembly machine as "a low-activity pyridoxal 5'-phosphate (PLP)-dependent cysteine desulfurase enzyme that consists of catalytic (NFS1), LYRM protein (ISD11), and acyl carrier protein (ACP) subunits" [PMID: 31511419]. The intrinsically low basal activity means the enzyme is critically dependent on accessory subunits and allosteric activators for physiological output.

Frataxin (FXN) is the key allosteric activator. Cory et al. (2025) describe how "Iron-sulfur clusters are essential protein cofactors synthesized in human mitochondria by an NFS1-ISD11-ACP-ISCU2-FXN assembly complex," with frataxin acting as a "molecular lock" that shifts the complex toward an active quaternary structure, accelerating substrate binding, persulfide formation, and sulfur delivery to ISCU2 [PMID: 39909887]. The functional interdependence of NFS1 with FXN is mechanistically important: it links COXPD52 biology to Friedreich ataxia (a frataxin-deficiency disease) and underscores why partial loss of NFS1 catalytic efficiency has outsized downstream consequences.

**Protein annotations:** UniProt Q9Y697 (NFS1_HUMAN); Pfam Aminotran_5 / class-V aminotransferase fold; InterPro cysteine desulfurase.

> **Evidence type:** Structural / biochemical. **Key PMIDs:** [31511419](https://pubmed.ncbi.nlm.nih.gov/31511419/), [39909887](https://pubmed.ncbi.nlm.nih.gov/39909887/).

### Finding 6 — Ultra-rare, autosomal recessive, complete penetrance; p.Arg72Gln recurs via consanguinity/shared haplotype

Inheritance is **autosomal recessive**: two defective alleles are required, and heterozygous carriers are unaffected because a single functional allele provides sufficient desulfurase activity. The disease is **ultra-rare**, with only a handful of families reported since 2014—one consanguineous family identified through autozygosity mapping [PMID: 24498631] and three additional unrelated patients [PMID: 35026043]. The recurrent allele c.215G>A (p.Arg72Gln) appears in the homozygous state in consanguineous/isolated-population backgrounds ("we identified c.215G>A, p.Arg72Gln in NFS1 as the likely causative mutation" via "autozygosity mapping, exome sequencing...") [PMID: 24498631], and as a compound heterozygous allele paired with c.1235G>A (p.Arg412His): "one patient with compound heterozygous p.(Arg72Gln) and p.(Arg412His) variants" [PMID: 35026043].

Notably, biallelic truncating/complete loss-of-function alleles have **not** been reported, consistent with *NFS1* being an essential gene—hypomorphic missense variants are tolerated (in the homozygous or compound-heterozygous state), whereas a complete null is predicted to be embryonic-lethal. ClinVar lists *NFS1* c.215G>A as pathogenic/likely pathogenic for this condition. No formal Orphanet prevalence, incidence, founder-population frequency, or carrier-frequency estimate has been published.

> **Evidence type:** Human genetic / population. **Key PMIDs:** [24498631](https://pubmed.ncbi.nlm.nih.gov/24498631/), [35026043](https://pubmed.ncbi.nlm.nih.gov/35026043/).

### Finding 7 — NFS1/cysteine desulfurase is deeply conserved; orthologs are essential across species

Fe–S clusters and the cysteine desulfurase that builds them are, in the words of Farhan et al. (2014), "a class of highly conserved and ubiquitous prosthetic groups" [PMID: 24498631]. NFS1 orthologs span the tree of life: *S. cerevisiae* NFS1 (essential for viability; mitochondrial), *E. coli* IscS/NifS (bacterial cysteine desulfurases that are the structural and functional prototypes), *Drosophila melanogaster* Nfs1, and mouse *Nfs1* (NCBI Gene 18041). The machinery's functional interdependence with conserved partners frataxin (FXN/Yfh1), ISCU (Isu1/2), ISD11/LYRM4, and HSPA9/Mortalin has been demonstrated in yeast and zebrafish ISC-biogenesis models. Shan & Cortopassi (2016) showed that "HSPA9 interacts with and stabilizes the mitochondrial ISC biogenesis proteins frataxin, Nfs1, ISCU, and Nfu," linking Nfs1 to aconitase activity and erythroid differentiation [PMID: 26702583].

**NCBI Taxa:** human (9606), mouse (10090), zebrafish (7955), *Drosophila* (7227), *S. cerevisiae* (4932), *E. coli* (562). The essentiality of NFS1 orthologs means complete-knockout model organisms are typically inviable; disease-relevant models require hypomorphic, conditional, or knock-in (patient-variant) approaches.

> **Evidence type:** Comparative / model organism. **Key PMIDs:** [24498631](https://pubmed.ncbi.nlm.nih.gov/24498631/), [26702583](https://pubmed.ncbi.nlm.nih.gov/26702583/).

### Finding 8 — Diagnosis rests on exome/genome sequencing plus biochemical Fe–S enzyme deficiency; treatment is supportive with poor infantile prognosis

**Diagnosis** is established by whole-exome or whole-genome sequencing confirming biallelic *NFS1* variants (NFS1 is not included on all targeted mitochondrial gene panels), supported by a distinctive biochemical signature: elevated blood/CSF lactate (and lactate:pyruvate ratio), muscle biopsy showing abnormal mitochondrial morphology, and respiratory-chain enzyme assays revealing combined complex II+III (±I) deficiency **plus** reduced activity of both mitochondrial and cytosolic aconitase. Yang et al. (2022) summarize the signature: "Skeletal muscle biopsy from patients 1 and 3 showed abnormal mitochondrial morphology, and functional analyses demonstrated decreased activity in respiratory chain complex II and variably in complexes I and III. We found decreased mitochondrial and cytosolic aconitase activities" [PMID: 35026043]. Because the defect spans complexes II/III and *extra*-mitochondrial Fe–S enzymes, the biochemical pattern distinguishes COXPD52 from mtDNA-encoded complex defects, which do not impair cytosolic aconitase.

**Differential diagnosis** includes other Fe–S biogenesis disorders: ISCU myopathy, Friedreich ataxia (FXN), LYRM4/ISD11 deficiency (COXPD19), the multiple-mitochondrial-dysfunction syndromes (BOLA3, NFU1, IBA57, ISCA2), and FDX2/FDXR disorders.

**Treatment:** there is no disease-specific or approved therapy. Management is supportive mitochondrial care—treating lactic acidosis, providing nutritional support, administering a "mitochondrial cocktail" of vitamins/cofactors, and avoiding metabolic decompensation. **Prognosis:** severe infantile homozygous p.Arg72Gln cases have high early mortality from multisystem organ failure [PMID: 24498631], whereas the milder compound-heterozygous genotype survived to adulthood [PMID: 35026043].

**Suggested NCIT concepts:** Supportive Care (NCIT:C15277), Genetic Counseling (NCIT:C15417).

> **Evidence type:** Human clinical. **Key PMIDs:** [35026043](https://pubmed.ncbi.nlm.nih.gov/35026043/), [24498631](https://pubmed.ncbi.nlm.nih.gov/24498631/).

---

## Section-by-Section Disease Characteristics

### 1. Disease Information

COXPD52 is a **nuclear-gene mitochondrial disease** of iron–sulfur cluster biogenesis. It was originally described (2014) as "infantile mitochondrial complex II/III deficiency" and is now cataloged in the OMIM "combined oxidative phosphorylation deficiency" series as entry **#619386**.

| Identifier | Value |
|---|---|
| OMIM | #619386 |
| MONDO | MONDO:0030311 |
| Gene | NFS1 (HGNC:7808; NCBI Gene 9054; UniProt Q9Y697) |
| Locus | 20q11.22 |
| Synonym | COXPD52; infantile mitochondrial complex II/III deficiency |
| Orphanet / ICD-10 / ICD-11 / MeSH | No dedicated code identified (subsumed under mitochondrial/OXPHOS disorders) |

**Information source:** derived almost entirely from **individual-patient case reports** (two primary publications describing a total of four patients) rather than aggregated disease-level registries—reflecting the disorder's ultra-rarity.

### 2. Etiology

**Causal factor:** purely **genetic**—biallelic hypomorphic variants in *NFS1*. **Genetic risk factors:** the recurrent c.215G>A (p.Arg72Gln) allele and the c.1235G>A (p.Arg412His) allele; consanguinity is a major contributor by increasing homozygosity for the recurrent variant [PMID: 24498631]. No environmental, infectious, lifestyle, or occupational risk factors are established. No protective variants or modifier alleles are documented. **Gene–environment interactions:** none established; however, intercurrent catabolic stress (infection, fasting) may precipitate metabolic decompensation in a vulnerable Fe–S-deficient background (mechanistically inferred, not formally demonstrated).

### 3. Phenotypes

| Phenotype | Type | HPO | Onset | Severity | Frequency |
|---|---|---|---|---|---|
| Lactic acidosis | Lab abnormality | HP:0003128 | Neonatal/infantile | Severe (infantile) | Core feature |
| Hypotonia | Clinical sign | HP:0001252 | Infantile | Moderate–severe | Core feature |
| Muscle weakness / myopathy | Clinical sign | HP:0001324 / HP:0003198 | Infantile | Variable | Common |
| Abnormal mitochondrial morphology | Pathology/biopsy | HP:0003200 (ragged-red) | Infantile | — | Reported in biopsied patients |
| Multisystem organ failure | Clinical | — | Infantile | Severe/fatal | Severe genotype |
| Gastrointestinal symptoms | Symptom | HP:0011024 | Young adult | Mild | Mild genotype |
| Fatigue | Symptom | HP:0012378 | Young adult | Mild | Mild genotype |
| Increased muscle lactate | Lab abnormality | HP:0003542 | Infantile | — | Reported |

**Quality-of-life impact:** severe infantile disease is devastating with high early mortality; the milder adult phenotype (chronic GI symptoms, fatigue) impairs daily functioning but is compatible with survival. Formal EQ-5D/SF-36 data are unavailable given rarity.

### 4. Genetic / Molecular Information

**Causal gene:** *NFS1* (disease OMIM #619386). **Pathogenic variants** reported: c.215G>A (p.Arg72Gln)—recurrent, missense, pathogenic/likely pathogenic in ClinVar; and c.1235G>A (p.Arg412His)—missense, in trans with p.Arg72Gln in the adult patient. **Variant class:** missense (hypomorphic). **Functional consequence:** partial **loss of function** (reduced cysteine desulfurase activity); no gain-of-function or dominant-negative mechanism. **Somatic vs germline:** germline. **Allele frequency:** p.Arg72Gln is rare in gnomAD, consistent with a pathogenic recessive allele. **Modifier genes:** none established, though genes of the ISC/CIA machinery (FXN, ISCU, LYRM4, FDX2, HSPA9) are plausible candidates. **Epigenetic changes / chromosomal abnormalities:** none reported or expected for this single-gene point-mutation disorder.

### 5. Environmental Information

**Not applicable.** No environmental toxins, radiation, pollution, occupational exposures, lifestyle factors, or infectious agents are implicated in causing COXPD52. The disease is monogenic and recessive.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic hypomorphic *NFS1* variants** (e.g., p.Arg72Gln) **result in** a structurally intact but catalytically impaired cysteine desulfurase within the core ISC complex (NFS1–ISD11–ACP–ISCU2, activated by FXN; electrons from FDX2) [PMID: 31511419, 39909887].
2. Reduced NFS1 activity **leads to** diminished mobilization of sulfur from L-cysteine and **decreased de novo assembly of [2Fe–2S] clusters** on the ISCU2 scaffold [PMID: 31918395].
3. The resulting Fe–S cofactor shortfall **branches** into multiple downstream failures:
   - **Branch A (mitochondrial respiration):** failure to mature Fe–S subunits of respiratory complexes I, II, and III **results in** combined OXPHOS deficiency and impaired electron transport [PMID: 24498631, 35026043].
   - **Branch B (TCA cycle / metabolism):** loss of Fe–S in mitochondrial aconitase (ACO2) and reduced lipoic acid synthesis **impair** the TCA cycle and oxidative decarboxylation (lipoylation only mildly affected in patients) [PMID: 35026043].
   - **Branch C (cytosolic/nuclear):** reduced sulfur supply to the CIA pathway **leads to** decreased cytosolic aconitase (ACO1/IRP1) activity and impaired maturation of DNA replication/repair Fe–S enzymes, causing DNA damage and cell-cycle arrest (demonstrated for NFS1 inhibition) [PMID: 40797101].
   - **Branch D (translation):** impaired tRNA thiolation **compromises** accurate mitochondrial/cytosolic translation (inferred for patients; demonstrated as an NFS1 function) [PMID: 40141425].
4. Impaired OXPHOS and TCA flux **cause** a shift to anaerobic glycolysis, **producing lactic acidemia** and energy deficit [PMID: 24498631].
5. Energy failure in high-demand tissues (skeletal/cardiac muscle, CNS, liver) **results in** hypotonia, weakness, abnormal mitochondrial morphology, and—at the severe end—**multisystem organ failure** [PMID: 24498631, 35026043].

**Upstream vs downstream:** the *NFS1* catalytic defect is the single upstream lesion; all respiratory, metabolic, genome-maintenance, and translational phenotypes are downstream consequences of a shared Fe–S supply bottleneck. **Cell types / processes:** high-oxidative-demand cells (skeletal myocytes CL:0000188, cardiomyocytes CL:0000746, hepatocytes CL:0000182, neurons CL:0000540). **GO processes:** GO:0016226 (iron-sulfur cluster assembly), GO:0006099 (TCA cycle), GO:0045333 (cellular respiration), GO:0006281 (DNA repair). **Subcellular compartments:** mitochondrial matrix (GO:0005759), cytosol (GO:0005829).

### 7. Anatomical Structures Affected

**Primary organs:** skeletal muscle (UBERON:0001134), and—via systemic energy failure—heart, liver, and central nervous system. **Body systems:** musculoskeletal, nervous, metabolic/endocrine, gastrointestinal. **Tissue level:** striated muscle tissue; the adult phenotype implicates the GI tract (UBERON:0001555). **Cell level:** skeletal myocytes (CL:0000188), neurons (CL:0000540), hepatocytes (CL:0000182). **Subcellular:** mitochondria (GO:0005739) are the principal affected compartment, with secondary cytosolic/nuclear involvement via the CIA pathway. **Lateralization:** systemic/bilateral (not a lateralized disorder).

### 8. Temporal Development

**Onset:** bimodal and genotype-dependent—**neonatal/infantile** (severe homozygous p.Arg72Gln) vs **young adult** (compound heterozygous p.Arg72Gln/p.Arg412His) [PMID: 24498631, 35026043]. **Onset pattern:** acute/subacute metabolic crisis in infants; insidious chronic course in the adult. **Progression:** rapidly progressive to multisystem organ failure in the infantile form; chronic and comparatively stable in the mild form. **Disease course:** progressive (infantile) vs chronic (adult). **Critical period:** the neonatal/early-infantile window is the period of greatest vulnerability and the key opportunity for supportive intervention.

### 9. Inheritance and Population

**Inheritance:** autosomal recessive, **complete penetrance** in biallelic individuals, with **variable expressivity** driven by genotype (homozygous vs compound-heterozygous). **Epidemiology:** ultra-rare—only four patients in two publications; no published prevalence or incidence. **Carrier frequency:** not formally estimated; p.Arg72Gln is rare in gnomAD. **Consanguinity:** a documented contributor (founding family identified by autozygosity mapping) [PMID: 24498631]. **Founder effect:** the recurrence of p.Arg72Gln across unrelated families suggests a possible shared ancestral haplotype, though this has not been formally proven. **Anticipation / germline mosaicism:** not applicable (non-repeat, point-mutation disorder). **Sex ratio:** no sex bias reported (autosomal). Note that biallelic null genotypes are absent, consistent with *NFS1* essentiality.

### 10. Diagnostics

**Genetic testing (definitive):** WES or WGS to identify biallelic *NFS1* variants; single-gene/targeted testing once *NFS1* is suspected. NFS1 is not on all mitochondrial panels, so broad sequencing is preferred. **Biochemical/laboratory:** elevated blood and CSF lactate with increased lactate:pyruvate ratio; muscle respiratory-chain enzyme assays showing combined complex II+III (±I) deficiency; and the discriminating finding of **reduced mitochondrial *and* cytosolic aconitase activity** [PMID: 35026043]. **Histopathology:** muscle biopsy showing abnormal mitochondrial morphology [PMID: 35026043, 24498631]. **Differential diagnosis:** ISCU myopathy, Friedreich ataxia (FXN), COXPD19 (LYRM4/ISD11), multiple mitochondrial dysfunction syndromes (NFU1, BOLA3, IBA57, ISCA2), FDX2/FDXR disorders—distinguished by gene and by the characteristic combined mito+cytosolic Fe–S enzyme pattern. **Screening:** no newborn or population carrier-screening program exists; cascade testing of relatives and prenatal/preimplantation testing are options once a familial genotype is known.

### 11. Outcome / Prognosis

**Survival/mortality:** the severe infantile homozygous form carries **high early mortality** from multisystem organ failure [PMID: 24498631]. The milder compound-heterozygous genotype is compatible with **survival to adulthood** [PMID: 35026043]. **Morbidity:** infantile survivors face profound disability from energy-failure myopathy/encephalopathy; the adult form causes chronic GI symptoms and fatigue. **Prognostic factors:** genotype is the dominant prognostic determinant (homozygous p.Arg72Gln = severe; compound heterozygous with p.Arg412His = mild), alongside age of onset and the severity of lactic acidosis. No validated prognostic biomarkers beyond lactate and enzyme-activity measures are established.

### 12. Treatment

**No disease-specific or approved therapy exists.** Management is **supportive mitochondrial care** (NCIT:C15277, Supportive Care):

- **Pharmacotherapy/supportive:** correction of lactic acidosis; "mitochondrial cocktail" cofactors/vitamins (e.g., riboflavin, thiamine, coenzyme Q10, L-carnitine)—empiric, not disease-validated.
- **Pharmacogenomics / gene therapy / cell therapy / RNA therapy / targeted or immunotherapy:** none established or in trials for COXPD52.
- **Nutritional/metabolic:** avoidance of catabolic stress and fasting; nutritional support for feeding difficulties.
- **Genetic counseling** (NCIT:C15417) for families.

*Mechanistic note:* Because NFS1 is a **PLP (vitamin B6)-dependent** enzyme [PMID: 31511419] and depends on cysteine as substrate, cofactor/substrate-oriented strategies (e.g., vitamin B6, cysteine/N-acetylcysteine supplementation) are biologically rational hypotheses worth formal study—analogous to the reported benefit of L-cysteine/NAC in the related Fe–S/tRNA disorder COXPD10 [PMID: 42753170]—but they remain **unproven for COXPD52**.

### 13. Prevention

**Primary prevention** is limited to reproductive genetic strategies: **genetic counseling**, carrier/cascade testing in affected families, and **prenatal or preimplantation genetic diagnosis** once the familial variants are known. **Secondary/tertiary prevention** centers on early recognition of metabolic decompensation and proactive supportive management to prevent complications. No vaccine, environmental, or public-health intervention is applicable (non-infectious, non-environmental monogenic disease).

### 14. Other Species / Natural Disease

NFS1/cysteine desulfurase is **deeply conserved and essential** across eukaryotes and bacteria [PMID: 24498631]. Orthologs: *S. cerevisiae* NFS1, *E. coli* IscS/NifS, *Drosophila* Nfs1, mouse *Nfs1* (NCBI Gene 18041; Taxon 10090), zebrafish (Taxon 7955). **NCBI Taxa:** human 9606, mouse 10090, zebrafish 7955, *Drosophila* 7227, *S. cerevisiae* 4932, *E. coli* 562. No naturally occurring companion-animal or wildlife disease equivalent to COXPD52 is cataloged (e.g., in OMIA). There is no zoonotic or cross-species transmission dimension. Evolutionary conservation of the ISC machinery (NFS1 with FXN/Yfh1, ISCU/Isu1-2, ISD11/LYRM4, HSPA9) makes model organisms highly informative for mechanism [PMID: 26702583].

### 15. Model Organisms

**Model types:** because NFS1 orthologs are essential, complete knockouts are inviable; disease-relevant modeling uses **hypomorphic, conditional, or patient-variant knock-in** approaches, plus **cellular/in vitro** systems. Established systems informing COXPD52 biology include:
- **Yeast (*S. cerevisiae*):** NFS1/Yfh1 ISC-biogenesis genetics; frataxin-bypass and complementation studies [PMID: 40563426].
- **Zebrafish / erythroid models:** Nfs1 within the HSPA9-stabilized ISC machinery; required for aconitase activity and erythroid differentiation [PMID: 26702583].
- **Mammalian cell lines:** NFS1 knockdown/inhibition (e.g., D-cysteine) recapitulates loss of Fe–S-dependent respiration, nucleotide metabolism, and genome integrity [PMID: 40797101]; in vitro reconstitution of the NFS1–ISD11–ACP–ISCU2–FXN complex enables direct enzymatic study of patient variants [PMID: 31511419, 39909887].

**Phenotype recapitulation:** cellular and lower-organism models faithfully reproduce the **biochemical** core (loss of Fe–S enzyme activities, respiratory deficiency, aconitase loss), supporting mechanism. **Limitations:** no published rodent model carries the patient p.Arg72Gln allele to recapitulate the full infantile multisystem syndrome; the organismal phenotype and genotype–phenotype gradient remain incompletely modeled. **Resources:** MGI (mouse *Nfs1*), SGD (yeast NFS1), ZFIN (zebrafish), Cellosaurus (cell lines).

---

## Mechanistic Model / Interpretation

```
        Biallelic hypomorphic NFS1 variants (p.Arg72Gln ± p.Arg412His)
                              │
                              ▼
     Catalytically impaired cysteine desulfurase in core ISC complex
          (NFS1–ISD11/LYRM4–ACP–ISCU2, activated by FXN; e- from FDX2)
                              │
          ↓ reduced L-cysteine → sulfur mobilization
          ↓ reduced [2Fe–2S] assembly on ISCU2 scaffold
                              │
        ┌─────────────┬───────────────┬────────────────┬─────────────────┐
        ▼             ▼               ▼                ▼                 ▼
  Resp. complexes  Mito aconitase  CIA pathway →   tRNA thiolation   Lipoic acid
   I / II / III      (ACO2)        cytosolic ACO1   (translation      synthesis
   Fe–S subunits    + TCA cycle     + nuclear DNA    fidelity)        (mild in pts)
        │             │             repair enzymes       │                │
        ▼             ▼               ▼                   ▼                ▼
  Combined OXPHOS  TCA flux loss  DNA damage,        impaired         (partial)
   deficiency      ↓ ATP          cell-cycle arrest  translation
        │             │               │
        └──────┬──────┘               │ (NFS1-inhibition data; inferred in patients)
               ▼
   Energy failure + lactic acidemia (anaerobic glycolysis shift)
               │
               ▼
  High-demand tissues: muscle (hypotonia/weakness, abnormal mitochondria),
  CNS, heart, liver  →  MULTISYSTEM ORGAN FAILURE (severe genotype)
  OR  chronic GI symptoms + fatigue (mild genotype)
```

The unifying interpretation is that COXPD52 is a **single upstream catalytic bottleneck disease**: one partially-active enzyme (NFS1) sits at the head of the entire cellular Fe–S supply chain, so a modest reduction in its activity produces a *combined, multi-pathway, multi-organ* deficiency. The biochemical fingerprint that distinguishes it from mtDNA-encoded respiratory diseases—**simultaneous mitochondrial and cytosolic aconitase loss**—is the direct readout of this upstream-bottleneck architecture. Genotype tunes severity: the more residual desulfurase activity the alleles preserve, the milder and later the disease.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [24498631](https://pubmed.ncbi.nlm.nih.gov/24498631/) | *Exome sequencing identifies NFS1 deficiency in infantile complex II/III deficiency* | Human genetic/clinical | F1, F2 (disease def.), F3 (severe phenotype), F6 (AR, consanguinity), F7 (conservation), F8 (Dx/prognosis) |
| [35026043](https://pubmed.ncbi.nlm.nih.gov/35026043/) | *Expanding the phenotypic and molecular spectrum of NFS1-related disorders* | Human clinical | F1 (recurrence), F2 (biochemistry), F3 (spectrum), F4 (mito+cyto aconitase), F6 (compound het), F8 (Dx signature) |
| [31918395](https://pubmed.ncbi.nlm.nih.gov/31918395/) | *Mammalian Fe-S cluster biogenesis: frataxin, ACP, ATPase transfer* | Review/structural | F2 (core complex, cluster assembly on ISCU) |
| [40797101](https://pubmed.ncbi.nlm.nih.gov/40797101/) | *D-cysteine impairs tumour growth by inhibiting NFS1* | In vitro | F4 (breadth: respiration, nucleotide metabolism, genome integrity) |
| [40141425](https://pubmed.ncbi.nlm.nih.gov/40141425/) | *Selective inhibitor of human NFS1 via virtual screening* | In vitro | F4 (Fe-S biosynthesis + tRNA thiolation) |
| [31511419](https://pubmed.ncbi.nlm.nih.gov/31511419/) | *Mechanism of activation of human cysteine desulfurase by frataxin* | Biochemical | F5 (PLP-dependent, low-activity; subunits) |
| [39909887](https://pubmed.ncbi.nlm.nih.gov/39909887/) | *Frataxin traps low-abundance quaternary structure* | Structural | F5 (NFS1-ISD11-ACP-ISCU2-FXN complex) |
| [26702583](https://pubmed.ncbi.nlm.nih.gov/26702583/) | *Mitochondrial Hspa9/Mortalin regulates erythroid differentiation via ISC assembly* | Model organism | F7 (conserved ISC machinery incl. Nfs1) |
| [23814038](https://pubmed.ncbi.nlm.nih.gov/23814038/) | *Mutations in LYRM4/ISD11 cause combined OXPHOS deficiency* | Human clinical | Differential Dx (COXPD19); NFS1 stabilization context |
| [42753170](https://pubmed.ncbi.nlm.nih.gov/42753170/) | *L-Cysteine/NAC improves outcome in COXPD10* | Human case | Rational (unproven) cofactor-therapy analogy |

**Challenges / cautionary context:** The large body of **NFS1 cancer literature** (osteosarcoma, colorectal, lung, AML, DLBCL, OSCC—PMIDs 42704489, 42069097, 41005206, 42878337, 35221331, 42068882, 42034254) studies NFS1 as an *overexpressed, pro-survival, anti-ferroptosis* oncogenic dependency. This is biologically consistent with (but opposite in direction to) COXPD52: in cancer, NFS1 is *up*regulated to protect against ferroptosis and support proliferation, whereas in COXPD52 NFS1 is *hypo*functional. These papers reinforce the enzyme's central Fe–S role but do not directly describe the recessive disease.

---

## Limitations and Knowledge Gaps

1. **Very small evidence base.** The entire clinical literature on COXPD52 comprises two publications and four patients. Genotype–phenotype correlation, penetrance nuances, and natural history are therefore based on minimal data.
2. **No epidemiology.** No published prevalence, incidence, carrier frequency, founder-haplotype confirmation, or geographic distribution exists.
3. **Narrow variant spectrum.** Only two missense variants (p.Arg72Gln, p.Arg412His) are reported; the full allelic and phenotypic spectrum (including whether any hypomorphic truncating combinations are viable) is unknown. Absence of biallelic null genotypes is inferred to reflect essentiality but is not formally proven in humans.
4. **No disease-specific therapy or trials.** Cofactor/substrate strategies (vitamin B6, cysteine/NAC) are mechanistically plausible but untested in COXPD52.
5. **No dedicated animal model of the human disease.** Existing models are essential-gene knockouts (inviable) or knockdowns; no published rodent carries the patient p.Arg72Gln allele to recapitulate the multisystem syndrome.
6. **Mechanistic steps partly inferred.** The contributions of tRNA-thiolation and genome-maintenance branches to patient phenotype are extrapolated from NFS1-inhibition/cancer studies rather than demonstrated in patient tissue.

---

## Proposed Follow-up Experiments / Actions

1. **Build a patient-variant knock-in model.** Generate a *Nfs1* p.Arg72Gln (and compound-heterozygous) mouse or zebrafish, or patient iPSC-derived cardiomyocytes/myotubes, to recapitulate the organismal phenotype and enable natural-history and therapeutic studies.
2. **Quantitative enzymology of patient variants.** Reconstitute NFS1–ISD11–ACP–ISCU2–FXN with p.Arg72Gln and p.Arg412His to measure residual desulfurase activity, cluster-transfer rate, and FXN-responsiveness—directly testing the genotype–severity gradient.
3. **Test cofactor/substrate therapies.** In patient cells and models, evaluate high-dose vitamin B6 (PLP), L-cysteine/N-acetylcysteine, and iron-handling modulators, mirroring the COXPD10 cysteine/NAC precedent [PMID: 42753170].
4. **Establish a patient registry / GeneMatcher outreach.** Aggregate additional cases to define prevalence, allelic spectrum, penetrance, and genotype–phenotype correlation.
5. **Validate the diagnostic biochemical signature.** Prospectively test whether combined mitochondrial + cytosolic aconitase deficiency reliably discriminates COXPD52 (and other ISC/CIA disorders) from mtDNA-encoded OXPHOS defects in diagnostic cohorts.
6. **Confirm or refute a founder haplotype.** Haplotype-phase the recurrent c.215G>A allele across reported families to establish whether it reflects a shared ancestral origin or recurrent mutation.

---

*Report compiled from 8 confirmed findings across 35 reviewed papers over 5 investigation iterations. Evidence types are labeled per claim (human clinical, model organism, in vitro/biochemical, structural, computational). Primary clinical evidence derives from two publications (PMID 24498631, PMID 35026043); mechanistic evidence from Fe–S biogenesis structural/biochemical and NFS1-function studies.*


## Artifacts

- [OpenScientist final report](Combined_Oxidative_Phosphorylation_Deficiency_52-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Combined_Oxidative_Phosphorylation_Deficiency_52-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 10 |
| Quoted claims found in source | 10 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 11 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 22 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030311` (3 mentions) - the report calls it "MONDO"; MONDO calls it **combined oxidative phosphorylation deficiency 52**
- `HP:0003128` (2 mentions) - the report calls it "Lactic acidosis", "Lab abnormality"; HP calls it **Lactic acidosis**
- `HP:0001252` (2 mentions) - the report calls it "Hypotonia", "Clinical sign"; HP calls it **Hypotonia**
- `HP:0012378` (2 mentions) - the report calls it "Fatigue", "Symptom"; HP calls it **Fatigue**
- `HP:0003542` (2 mentions) - the report calls it "Increased muscle lactate", "Lab abnormality"; HP calls it **Increased circulating pyruvate concentration**
- `NCIT:C15417` (2 mentions) - the report calls it "Genetic counseling"; NCIT calls it **Randomized Clinical Trial**
- `HP:0011024` (1 mention) - the report calls it "Symptom"; HP calls it **Abnormality of the gastrointestinal tract**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0097428` (obsolete protein maturation by iron-sulfur cluster transfer) (1 mention) - replaced by `GO:0051604`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003200` (2 mentions) - the report calls it "Ragged-red muscle fibers / abnormal mitochondria", "ragged-red"; HP calls it **Ragged-red muscle fibers**
- `GO:0097428` (1 mention) - the report calls it "protein maturation by iron-sulfur cluster transfer"; GO calls it **obsolete protein maturation by iron-sulfur cluster transfer**
- `GO:0002143` (1 mention) - the report calls it "tRNA wobble position thiouridine biosynthesis"; GO calls it **tRNA wobble position uridine thiolation**, and lists "wobble position s2U biosynthesis" among its other names
- `GO:0006099` (1 mention) - the report calls it "TCA cycle"; GO calls it **tricarboxylic acid cycle**, and lists "TCA cycle" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0003128` - called "Lactic acidosis", "Lab abnormality"
- `HP:0001252` - called "Hypotonia", "Clinical sign"
- `HP:0003200` - called "Ragged-red muscle fibers / abnormal mitochondria", "ragged-red"
- `HP:0012378` - called "Fatigue", "Symptom"
- `HP:0003542` - called "Increased muscle lactate", "Lab abnormality"