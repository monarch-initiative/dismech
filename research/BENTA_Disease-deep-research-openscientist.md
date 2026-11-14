---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-13T08:50:19.212900'
end_time: '2026-11-13T09:06:06.958881'
duration_seconds: 947.75
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: BENTA Disease
  mondo_id: MONDO:0014645
  category: Mendelian
  causal_genes: CARD11
  omim_id: OMIM:616452
  synonyms: B-cell expansion with NF-kB and T-cell anergy disease
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    save_artifacts: true
    artifact_max_bytes: 5242880
    artifact_keep_runtime: false
    artifact_extra_extensions: []
    artifact_include_globs: []
    artifact_exclude_globs: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
run_metadata:
  job_id: 5595e380-00d0-421b-993f-000040c5e1d2
citation_count: 15
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 14
  off_topic: 1
  off_topic_references:
  - PMID:37126937
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 38
  verified: 35
  not_found: 0
  obsolete: 2
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 7
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: MONDO:0014645
    reported_labels:
    - MONDO
    ontology_label: BENTA disease
  - term_id: HP:0001744
    reported_labels:
    - Common
    ontology_label: Splenomegaly
  - term_id: HP:0002716
    reported_labels:
    - Common
    ontology_label: Lymphadenopathy
  - term_id: HP:0002719
    reported_labels:
    - Common
    ontology_label: Recurrent infections
  - term_id: GO:0005737
    reported_labels:
    - cytoplasm / aggregate localization
    ontology_label: cytoplasm
  - term_id: NCIT:C312
    reported_labels:
    - Prednisolone
    ontology_label: Bleomycin Sulfate
  - term_id: NCIT:C1133
    reported_labels:
    - Tacrolimus
    ontology_label: ImuVert
  - term_id: NCIT:C157808
    reported_labels:
    - Relief of airway obstruction from lymphoid hyperplasia
    ontology_label: Casts and Splints
  - term_id: NCIT:C15431
    reported_labels:
    - Considered for severe/refractory cases (not established)
    ontology_label: Hematopoietic Cell Transplantation
  labels_variant: 4
  obsolete_terms:
  - term_id: HP:0005435
    ontology_label: obsolete Impaired T cell function
    replaced_by: HP:0011840
  - term_id: GO:0051092
    ontology_label: obsolete positive regulation of NF-kappaB transcription factor
      activity
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: BENTA_Disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: BENTA_Disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** BENTA Disease
- **MONDO ID:** MONDO:0014645 (if available)
- **Causal gene(s):** CARD11
- **OMIM:** OMIM:616452
- **Synonyms:** B-cell expansion with NF-kB and T-cell anergy disease
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **BENTA Disease** covering all of the
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

# BENTA Disease (B-cell Expansion with NF-κB and T-cell Anergy): A Comprehensive Disease Characterization Report

**Target disease:** BENTA Disease — *B-cell Expansion with NF-κB and T-cell Anergy*
**Causal gene:** **CARD11** (CARMA1; HGNC:16393, NCBI Gene 84433, UniProt Q9BXL7, chromosome 7p22.2)
**Identifiers:** OMIM 616452 · MONDO:0014645
**Inheritance:** Autosomal dominant (germline gain-of-function); one biallelic case reported
**Category:** Mendelian inborn error of immunity

---

## Summary

**BENTA disease is a rare, autosomal-dominant inborn error of immunity caused by germline gain-of-function (GOF) missense (and rare in-frame deletion) variants in *CARD11*** — the gene encoding the lymphocyte scaffold protein CARMA1. CARD11 normally transmits antigen-receptor signals from the B-cell and T-cell receptors to the transcription factor NF-κB via the CARD11–BCL10–MALT1 (CBM) signalosome. In BENTA, the mutant CARD11 protein self-aggregates and nucleates a constitutively active CBM signalosome, driving **antigen-independent NF-κB activation**. The clinical consequence is a congenital, polyclonal, naïve-predominant **B-cell lymphocytosis** accompanied by **splenomegaly, lymphadenopathy, and recurrent infections**, with paradoxical **T-cell anergy** (functional hyporesponsiveness) despite the activating lesion.

The natural history is strikingly variable. Many patients are asymptomatic or improve without targeted therapy, while a subset suffers early-childhood fatal complications — in a 2025 systematic review of 34 cases, all six deaths occurred before age three, attributable to refractory hemophagocytic lymphohistiocytosis (HLH) or opportunistic infection. Across the reported literature (fewer than ~40 patients worldwide), HLH emerged in roughly 19% of cases, and B-lymphocytosis — though characteristic — was not universal. BENTA patients carry an **elevated lifetime risk of lymphoid malignancy**, spanning both B-cell lymphoma (the same GOF lesions occur somatically in activated B-cell diffuse large B-cell lymphoma, ABC-DLBCL) and, unexpectedly, T-cell lymphoma (subcutaneous panniculitis-like T-cell lymphoma, SPTCL, in two unrelated patients).

There is **no established curative therapy**. Management is supportive and immunomodulatory — corticosteroids, the mTOR inhibitor sirolimus, and the calcineurin inhibitor tacrolimus have been used with clinical benefit; splenectomy paradoxically worsens lymphocytosis and is avoided. Mechanism-based agents targeting the downstream CBM–NF-κB axis (MALT1 paracaspase inhibitors, BTK inhibitors), developed for ABC-DLBCL, represent rational investigational options. This report synthesizes eight confirmed findings from 21 primary papers across all 15 requested disease-characterization domains, distinguishing human clinical, model-organism, and in-vitro evidence throughout.

---

## 1. Disease Information

**Overview.** BENTA (*B-cell Expansion with NF-κB and T-cell Anergy*) is a rare primary immunodeficiency / lymphoproliferative disorder — more precisely an inborn error of immunity with immune dysregulation — caused by germline gain-of-function mutations in **CARD11**. The hallmark is a congenital or early-childhood polyclonal expansion of B lymphocytes driven by constitutive NF-κB signaling, coupled with functional T-cell anergy. It was first defined molecularly by Snow et al. in 2012 ([PMID: 23129749](https://pubmed.ncbi.nlm.nih.gov/23129749/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | 616452 |
| MONDO | MONDO:0014645 |
| Gene (HGNC) | CARD11, HGNC:16393 |
| NCBI Gene | 84433 |
| UniProt | Q9BXL7 |
| Cytogenetic locus | 7p22.2 |
| MeSH | No dedicated BENTA term; indexed under Primary Immunodeficiency Diseases / Lymphocytosis |
| ICD-10/ICD-11 | No specific code; grouped with primary immunodeficiencies |
| Orphanet | Rare immune dysregulation / lymphoproliferation (no large registry entry) |

**Synonyms / alternative names.** B-cell Expansion with NF-kB and T-cell Anergy; CARD11 gain-of-function disorder; CARD11 GOF; congenital B-cell lymphocytosis due to CARD11.

**Source of information.** The information base is a mix of **individual patient case reports and small case series** (the large majority of the literature) aggregated into two systematic reviews (Nishinosono et al. 2025, [PMID: 39998705](https://pubmed.ncbi.nlm.nih.gov/39998705/); Baldini-type review 2025, [PMID: 40157432](https://pubmed.ncbi.nlm.nih.gov/40157432/)). There are no EHR-scale or population-registry datasets given the disease's rarity.

---

## 2. Etiology

**Primary cause — genetic.** BENTA is a **monogenic** disease caused by germline heterozygous (rarely biallelic) **gain-of-function variants in CARD11**. Snow et al. identified a germline heterozygous missense mutation **E127G** in an affected family and an independent **G116S** in an unrelated, phenotypically similar patient; both map to the CARD11 coiled-coil domain and drive constitutive NF-κB activation ([PMID: 23129749](https://pubmed.ncbi.nlm.nih.gov/23129749/)):

> *"We found a novel germline heterozygous missense mutation (E127G) in affected patients in the gene encoding CARD11... We subsequently identified a second germline mutation (G116S) in an unrelated, phenotypically similar patient, confirming mutations in CARD11 drive disease."*

**Genetic risk factors.** The causal variants *are* the risk factors — this is a highly penetrant Mendelian disorder, not a polygenic/susceptibility trait. No separate GWAS susceptibility loci apply.

**Environmental risk / trigger factors.** Environmental exposures do not *cause* BENTA, but they **modulate severity and precipitate complications**. The most important is **Epstein–Barr virus (EBV) infection**, which markedly exacerbates B lymphocytosis; **splenectomy** similarly worsens the lymphocyte count and is therefore contraindicated ([PMID: 25352053](https://pubmed.ncbi.nlm.nih.gov/25352053/)). Infections (including opportunistic) are major triggers of fatal outcomes in infancy.

**Protective factors.** No genetic or environmental protective alleles are established. Milder phenotypes track with specific hypomorphic GOF alleles (e.g., C49Y, K215del) rather than with modifier genes.

**Gene–environment interactions.** The clearest interaction is **CARD11-GOF × EBV**: the expanded, NF-κB-primed B-cell compartment responds to EBV with dramatic further expansion and heightened HLH risk. This is a mechanistic inference supported by longitudinal observation rather than controlled study.

---

## 3. Phenotypes

BENTA phenotypes span clinical signs, physical manifestations, laboratory abnormalities, and malignancy predisposition. Core features and suggested HPO terms:

| Phenotype | Type | Characteristics | Frequency | HPO suggestion |
|---|---|---|---|---|
| Polyclonal B-cell lymphocytosis | Lab abnormality | Congenital/early onset; counts 20,000–90,000/mm³ in severe cases; persistent | Characteristic but **not universal** | HP:0012132 (B lymphocytosis) / HP:0001974 (Leukocytosis) |
| Splenomegaly | Clinical sign | Early childhood; variable | Common | HP:0001744 |
| Lymphadenopathy | Clinical sign | Early childhood | Common | HP:0002716 |
| Recurrent infections | Clinical | Esp. respiratory; opportunistic in severe cases | Common | HP:0002719 |
| T-cell anergy / hyporesponsiveness | Lab/functional | Reduced antigen-receptor responsiveness; near-normal counts & Vβ diversity | Characteristic | HP:0005435 (Impaired T-cell function) |
| Hemophagocytic lymphohistiocytosis (HLH) | Clinical | Fever, splenomegaly, hypercytokinemia; can be fatal | ~18.8% | HP:0003261-adjacent; HP:0012047 (Histiocytosis) |
| B-cell / T-cell lymphoma | Malignancy | B-cell lymphoproliferation; SPTCL in 2 patients | Elevated lifetime risk | HP:0012191 (B-cell lymphoma) |
| Autoimmune-like manifestations | Clinical | Polyarthritis, encephalitis (one maternal case) | Rare | HP:0001369 (Arthritis) / HP:0002383 (Encephalitis) |
| Adenotonsillar/lymphoid hyperplasia | Physical | Airway obstruction in one patient | Rare | HP:0040286 (Abnormal tonsil morphology) |

The core clinical presentation is summarized by the 2025 review ([PMID: 40157432](https://pubmed.ncbi.nlm.nih.gov/40157432/)):

> *"typically presenting with early-onset polyclonal B-cell lymphocytosis, splenomegaly, lymphadenopathy, and recurrent infections"*

**Severity and progression.** Highly **variable expressivity**: mild alleles (C49Y, K215del) retain near-normal counts and vaccine responses, while severe cases (e.g., G123D, M365K, biallelic R331P) show massive lymphocytosis and life-threatening complications. The disease is generally chronic/lifelong; lymphocytosis is persistent rather than remitting.

**Quality of life.** No formal EQ-5D/SF-36/PROMIS data exist. Impact ranges from negligible (asymptomatic carriers) to severe (infants with HLH, airway-obstructing lymphoid hyperplasia, malignancy). Chronic infection susceptibility and surveillance burden affect daily functioning in symptomatic patients.

---

## 4. Genetic / Molecular Information

**Causal gene.** *CARD11* (Caspase Recruitment Domain family member 11), a multidomain cytoplasmic scaffold expressed predominantly in hematopoietic/lymphoid tissue. Disease OMIM 616452.

**CARD11 allelic series — three distinct Mendelian diseases from one gene:**

| Mechanism | Disease | OMIM | Direction |
|---|---|---|---|
| Biallelic loss-of-function | CARD11-deficiency combined immunodeficiency (CID with atopy) | 615206 | LOF |
| Heterozygous dominant-negative LOF | CADINS / CARD11-associated atopy (severe atopic dermatitis, infections) | 617638 | DN-LOF |
| **Heterozygous gain-of-function** | **BENTA** | **616452** | **GOF** |

CARD11 is required for normal activation of NF-κB, JNK, and mTOR during antigen-receptor signaling ([PMID: 34341167](https://pubmed.ncbi.nlm.nih.gov/34341167/)).

**Reported pathogenic BENTA variants (allelic series):**

| Variant | Zygosity | Domain | Notes | PMID |
|---|---|---|---|---|
| E127G | Het | Coiled-coil | Founding variant, familial | 23129749 |
| G116S | Het | Coiled-coil | Founding variant, unrelated | 23129749 |
| G123D | Het (de novo & inherited) | Coiled-coil | Familial (mother→son); maternal autoimmune features | 25352053 / 36129242 |
| G123S | Het | Coiled-coil | — | reviews |
| C49Y | Het | CARD | Mild phenotype, 3 patients | 25930198 |
| M365K | Het | — | Mouse knock-in model | 36960072 |
| D357E | Het | — | — | 40157432 |
| K215del (in-frame 3-bp del) | Het | Coiled-coil | Mild, subtle NF-κB increase | 31897776 |
| R331P | **Homozygous (biallelic)** | — | B-cell reprogramming | 41456721 |

**Variant classification.** Pathogenic / likely pathogenic per ACMG/AMP, supported by functional NF-κB assays. All are **missense or in-frame deletion** (no truncating variants cause GOF).

**Allele frequency.** Germline GOF variants are **absent or vanishingly rare in gnomAD**, consistent with pathogenicity and strong purifying selection.

**Somatic vs germline.** BENTA is defined by **germline** variants. Notably, the **same lesion class occurs somatically** in ABC-DLBCL — a key link between the Mendelian disease and lymphomagenesis.

**Functional consequence.** **Gain of function** — constitutive, antigen-independent NF-κB activation. The variants promote self-aggregation of CARD11 and spontaneous CBM signalosome assembly.

**Modifier genes / epigenetics / chromosomal abnormalities.** No specific modifier genes, epigenetic signatures, or large-scale chromosomal abnormalities have been established for BENTA. B cells show an aberrant transcriptional program (see §6), but no disease-specific methylation studies exist.

---

## 5. Environmental Information

- **Environmental / toxic factors:** None causative. No occupational, radiation, or pollution associations.
- **Lifestyle factors:** None established.
- **Infectious agents:** **EBV is a key disease modifier/trigger**, markedly exacerbating B lymphocytosis and predisposing to HLH ([PMID: 25352053](https://pubmed.ncbi.nlm.nih.gov/25352053/)). Opportunistic infections are major causes of early-childhood mortality. Infections do not *cause* BENTA but act on the genetically primed immune compartment.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A **germline GOF variant in CARD11** (e.g., E127G, G116S, G123D, M365K, biallelic R331P), most often in the coiled-coil/CARD region, **alters the autoinhibited conformation** of the CARD11 scaffold.
2. This **leads to spontaneous self-aggregation** of mutant CARD11 into large cytosolic structures ("mCADS" — mutant CARD11-dependent shells) *[in-vitro demonstrated]*.
3. The aggregates **nucleate assembly of the CARD11–BCL10–MALT1 (CBM) signalosome** and **recruit phospho-IKK and MALT1**, i.e., an active signaling platform — **without antigen-receptor engagement**.
4. Constitutive CBM/IKK activity **results in antigen-independent, constitutive NF-κB activation** (with parallel JNK and mTOR signaling) *[demonstrated in reporter and primary-cell assays]*.
5. In **B cells**, constitutive NF-κB **drives upregulation of cell-cycle progression and survival genes**, **leading to enhanced proliferation and survival** and a **polyclonal, naïve-predominant B-cell expansion** (lymphocytosis, splenomegaly, lymphadenopathy).
6. In **T cells**, the same lesion **results paradoxically in functional anergy/hyporesponsiveness** (reduced IFN-γ-producing CD3⁺ cells), while counts and Vβ diversity remain near normal *[mechanism partly inferred — likely chronic-signaling-induced desensitization]*.
7. The expanded, NF-κB-primed compartment, further **triggered by EBV infection**, **branches toward HLH** (hypercytokinemia, impaired NK degranulation) and/or **toward lymphoid malignancy** (B-cell lymphoma; rarely SPTCL T-cell lymphoma), the leading causes of severe morbidity/mortality.

```
 CARD11 GOF variant (germline)
          │ alters autoinhibition
          ▼
 Self-aggregation → mCADS
          │ recruits BCL10, MALT1, pIKK
          ▼
 Constitutive CBM signalosome
          │ antigen-INDEPENDENT
          ▼
 Constitutive NF-κB (+ JNK, mTOR)
        ┌─────────────┴─────────────┐
        ▼                           ▼
  B CELL: proliferation,      T CELL: anergy /
  survival, naïve expansion   hyporesponsiveness
        │
        ▼  (+EBV trigger)
   ┌────┴─────┐
   ▼          ▼
 HLH     Lymphoma (B-cell;
         rarely SPTCL T-cell)
```

### Mechanistic detail

**Molecular pathways.** Canonical **NF-κB** is the central effector (CBM → IKK → IκB degradation → NF-κB nuclear translocation). JNK/AP-1 and mTOR are co-activated. Suggested pathway references: KEGG NF-κB signaling; Reactome CBM-mediated NF-κB activation.

**Protein dysfunction — gain of function via aggregation.** Stinson et al. showed GOF CARD11 mutants form cytosolic aggregates that colocalize with the signaling machinery ([PMID: 32473470](https://pubmed.ncbi.nlm.nih.gov/32473470/)):

> *"GOF CARD11 mutants can form large, peculiar cytosolic protein aggregates we term mCADS (mutant CARD11 dependent shells). MALT1 and phospho-IKK are reliably colocalized with mCADS, indicative of active signaling."*

and that these mutants *"drive constitutive NF-κB activity without AgR stimulation."* The CBM complex is the essential molecular hub ([PMID: 25087226](https://pubmed.ncbi.nlm.nih.gov/25087226/)):

> *"The CBM complex forms an essential molecular link between the triggering of cell-surface antigen receptors and nuclear factor κB activation."*

**Cellular processes.** Dysregulated cell-cycle progression, enhanced survival/anti-apoptosis, and lymphoproliferation in B cells; T-cell anergy. Brohl et al. documented the B-cell program ([PMID: 25352053](https://pubmed.ncbi.nlm.nih.gov/25352053/)):

> *"this patient's B cells exhibited higher expression of several cell cycle progression genes, as well as enhanced proliferation and improved survival following B cell receptor stimulation."*

**Immune system involvement.** A hybrid of **immune dysregulation (B-cell overgrowth), partial immunodeficiency (infection susceptibility, T-cell anergy), and hyperinflammation (HLH)**.

**Transcriptomic / single-cell profiling.** Bhattad et al. profiled a biallelic R331P patient ([PMID: 41456721](https://pubmed.ncbi.nlm.nih.gov/41456721/)):

> *"massive expansion of B cells with a naive surface phenotype and aberrant transcriptional program."*

**Suggested ontology terms.** GO:0051092 (positive regulation of NF-κB transcription factor activity); GO:0038095 (BCR signaling pathway); GO:0002376 (immune system process); CL:0000236 (B cell); CL:0000788 (naive B cell); CL:0000084 (T cell); GO:0005737 (cytoplasm / aggregate localization).

---

## 7. Anatomical Structures Affected

**Organ level.** Primary: **spleen (splenomegaly; UBERON:0002106), lymph nodes (lymphadenopathy; UBERON:0000029), peripheral blood (UBERON:0000178), bone marrow (UBERON:0002371)**. Secondary: **liver (hepatomegaly in HLH; UBERON:0002107)**, **tonsils/adenoids (lymphoid hyperplasia; UBERON:0002372)**, skin (SPTCL; UBERON:0002097). Body system: **hematopoietic / immune system (UBERON:0002405 immune system; UBERON:0002390 hematopoietic system)**.

**Tissue / cell level.** Lymphoid tissue; the expanded population is **naïve B cells (CL:0000788 naive B cell / CL:0000236 B cell)**; T cells (CL:0000084) are functionally impaired; NK cells (CL:0000623) show impaired degranulation during HLH.

**Subcellular level.** The pathology is centered in the **cytoplasm (GO:0005737)**, where mutant CARD11 forms aggregates (mCADS) and assembles the CBM signalosome; signaling culminates in the **nucleus (GO:0005634)** via NF-κB translocation.

**Localization / lateralization.** Systemic and **bilateral** (generalized lymphoproliferation, splenomegaly). SPTCL presents as subcutaneous skin lesions.

---

## 8. Temporal Development

- **Onset.** **Congenital / early childhood** — lymphocytosis is frequently detectable from infancy; "congenital B-cell lymphocytosis" is a descriptive term for the disease. Onset pattern is **chronic/insidious**.
- **Progression.** **Variable**: often stable and indolent over years; a subset progresses rapidly in infancy to HLH/fatal infection. Not relapsing-remitting in the classic sense, though EBV and infections cause episodic exacerbations.
- **Duration.** **Chronic, lifelong** (persistent lymphocytosis).
- **Remission.** No spontaneous resolution of the genetic lesion; symptoms can improve with immunomodulation (treatment-induced improvement).
- **Critical period.** The **first ~3 years of life** are the window of highest mortality — all six deaths in the 34-case review occurred before age 3 ([PMID: 39998705](https://pubmed.ncbi.nlm.nih.gov/39998705/)), making early diagnosis and vigilance against HLH/infection the key intervention window.

---

## 9. Inheritance and Population

**Epidemiology.** **Ultra-rare: fewer than ~40 patients reported worldwide as of 2025** (34 cases in Nishinosono review [PMID: 39998705](https://pubmed.ncbi.nlm.nih.gov/39998705/); 29 in the Baldini-type review [PMID: 40157432](https://pubmed.ncbi.nlm.nih.gov/40157432/)). **No formal prevalence or incidence estimate exists.**

**Inheritance.** **Autosomal dominant**, with both **de novo** and **inherited (mother→child)** cases documented. **One biallelic (homozygous R331P)** case is reported. Stated plainly ([PMID: 40157432](https://pubmed.ncbi.nlm.nih.gov/40157432/)):

> *"Gain-of-function (GOF) mutations in CARD11 cause BENTA disease (B cell Expansion with NF-κB and T cell Anergy), an autosomal dominant disorder."*

- **Penetrance:** High but with **variable expressivity** — B-lymphocytosis is frequent but "not universally present."
- **Expressivity:** Highly variable (mild C49Y/K215del vs severe G123D/M365K/R331P).
- **Anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism / founder effects / consanguinity:** No founder effect established; biallelic R331P implies possible consanguinity in that pedigree. No documented germline mosaicism.
- **Carrier frequency:** Vanishingly low (GOF variants near-absent in gnomAD).

**Population demographics.** Reported cases span **multiple ethnicities — USA, Europe, India, China, Japan** — with no geographic clustering. **Both sexes affected**; no strong sex bias documented. Age distribution skews to congenital/pediatric diagnosis.

---

## 10. Diagnostics

**Laboratory tests.** CBC with differential showing **persistent polyclonal B lymphocytosis** (20,000–90,000/mm³ in severe cases); flow cytometry demonstrating **polyclonal, naïve-predominant (CD19⁺) B-cell expansion** — distinguishing BENTA from monoclonal leukemias (e.g., CLL). Immunoglobulin levels variable; vaccine responses often preserved in mild cases.

**Biomarkers.** No validated circulating biomarker beyond the lymphocyte phenotype; HLH work-up (ferritin, soluble IL-2R, triglycerides, fibrinogen, NK-cell degranulation) when hyperinflammation is suspected.

**Functional / immunologic assays.** In-vitro NF-κB reporter assays and lymphocyte proliferation studies (reduced proliferation to TCR/mitogen stimulation = T-cell anergy); **mCADS aggregation assays** in research settings.

**Genetic testing — definitive.** Diagnosis is confirmed by **identification of a germline GOF CARD11 variant**. Recommended approach: **single-gene testing, targeted primary-immunodeficiency/inborn-errors-of-immunity gene panels, or WES/WGS**. Functional confirmation (NF-κB activation assay) supports VUS reclassification. Chromosomal microarray, karyotyping, FISH, mtDNA, and repeat-expansion testing are **not applicable**.

**Clinical criteria / differential diagnosis.** No formal consensus criteria. Differential includes: **monoclonal B-cell lymphocytosis / CLL** (BENTA is polyclonal, congenital), **other congenital lymphocytoses**, **ALPS**, **primary HLH**, and reactive EBV lymphocytosis. BENTA-HLH overlap is an important diagnostic pitfall ([PMID: 37401643](https://pubmed.ncbi.nlm.nih.gov/37401643/)).

**Screening.** No newborn or population screening exists. **Cascade genetic testing** of relatives is appropriate once a familial variant is identified.

---

## 11. Outcome / Prognosis

**Prognosis is bimodal.** Many patients are indolent; a minority die young. In the 34-case systematic review ([PMID: 39998705](https://pubmed.ncbi.nlm.nih.gov/39998705/)):

> *"Among these cases, 15 were either asymptomatic or showed improvement without requiring any specific treatment. However, all six reported deaths were diagnosed before the age of 3 years, with two attributed to refractory hemophagocytic syndrome and four caused by opportunistic infections."*

| Outcome metric | Finding |
|---|---|
| Asymptomatic / improved without treatment | 15 / 34 (~44%) |
| Deaths | 6 / 34 (~18%), **all before age 3** |
| Cause of death | HLH (2), opportunistic infection (4) |
| HLH complication rate | ~18.8% |
| Malignancy | Elevated lifetime risk (B-cell lymphoma; SPTCL in 2) |

**Morbidity.** Recurrent infections, splenomegaly-related issues, lymphoid hyperplasia (airway obstruction), HLH, and malignancy surveillance burden.

**Prognostic factors.** Severity correlates with the **specific allele** (mild C49Y/K215del vs severe G123D/M365K/R331P), **EBV exposure**, and **early HLH**. No validated prognostic biomarker panel exists. No formal 5-/10-year survival statistics are published given rarity.

---

## 12. Treatment

**No curative or disease-specific approved therapy exists.** Management is **supportive and immunomodulatory**, guided by severity.

| Intervention | Role | NCIT suggestion | Evidence |
|---|---|---|---|
| Corticosteroids (prednisolone, dexamethasone) | First-line for symptomatic lymphoproliferation / HLH | NCIT:C312 (Prednisolone) | 39998705, 36129242 |
| Sirolimus (rapamycin, mTOR inhibitor) | Successful control of lymphoproliferation | NCIT:C1212 (Sirolimus) | 39998705 |
| Tacrolimus (calcineurin inhibitor) | Used with prednisolone in familial G123D case | NCIT:C1133 (Tacrolimus) | 36129242 |
| Etoposide (+ dexamethasone, HLH protocol) | For HLH episodes | NCIT:C491 (Etoposide) | 37401643 |
| Antibiotics / anti-infectives | Control of infections precipitating HLH | — | 37401643 |
| Adenoidectomy / tonsillectomy | Relief of airway obstruction from lymphoid hyperplasia | NCIT:C157808 | reviews |
| HSCT | Considered for severe/refractory cases (not established) | NCIT:C15431 | reviews |
| **Splenectomy — AVOID** | **Worsens lymphocytosis** | — | 25352053 |

**Sirolimus success** is explicitly documented ([PMID: 39998705](https://pubmed.ncbi.nlm.nih.gov/39998705/)): *"Her symptoms improved with prednisolone and sirolimus."*

**Mechanism-based / investigational.** Because BENTA is driven by constitutive CBM→NF-κB signaling, **downstream-targeted agents are rational**:
- **MALT1 paracaspase inhibitors** — developed for ABC-DLBCL, where *"B cell receptor-addicted lymphomas rely strongly on this cancer cell-intrinsic MALT1 protease function"* ([PMID: 37126937](https://pubmed.ncbi.nlm.nih.gov/37126937/); see also [PMID: 34783281](https://pubmed.ncbi.nlm.nih.gov/34783281/), [PMID: 19897720](https://pubmed.ncbi.nlm.nih.gov/19897720/)).
- **BTK inhibitors** (upstream of CBM in BCR signaling).
- **SMAC mimetics** targeting cIAP1/2 in the CBM complex ([PMID: 27070702](https://pubmed.ncbi.nlm.nih.gov/27070702/)).

None are yet standard for BENTA. No specific NCT-registered BENTA trials are established.

**Pharmacogenomics.** Not specifically characterized for BENTA.

---

## 13. Prevention

- **Primary prevention:** Not possible (germline genetic disease). **Genetic counseling** for affected families (autosomal dominant; 50% transmission risk from an affected heterozygous parent) is the main preventive tool, with optional **prenatal / preimplantation genetic testing** once a familial variant is known.
- **Secondary prevention:** Early molecular diagnosis and **cascade testing** of relatives; close surveillance in infancy for HLH and infection (the critical <3-year window).
- **Tertiary prevention:** Aggressive infection control, **avoidance of splenectomy**, EBV monitoring, and malignancy surveillance to prevent complications.
- **Immunization / prophylaxis:** Standard vaccination (many patients respond to conjugate vaccines); infection prophylaxis as clinically indicated. No disease-specific vaccine.
- **Public health / environmental:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / ortholog:** Human *CARD11* (NCBI Gene 84433); mouse *Card11* ortholog (**NCBI Gene 108723**). Highly conserved across mammals.
- **Natural disease in other species:** No naturally occurring BENTA-equivalent disease is documented in companion animals or wildlife (no OMIA entry for a CARD11-GOF animal disease). The disease is known only from humans and engineered models.
- **Comparative biology:** The CBM→NF-κB axis is evolutionarily conserved; mouse *Card11* alleles recapitulate both GOF (activation) and LOF (immunodeficiency) ends of the human allelic series, confirming conserved mechanism.
- **Zoonotic / transmission:** Not applicable (non-infectious genetic disease).

---

## 15. Model Organisms

**Mouse models (primary):**

| Model | Type | Phenotype | PMID |
|---|---|---|---|
| **Card11 M365K knock-in** | Germline GOF knock-in | Increased B- and T-lymphocyte activation and proliferation after antigen-receptor stimulation; models BENTA/DLBCL GOF spectrum | 36960072 |
| Card11 R30W | Point mutant (allele study) | Demonstrates CARD11 role in NF-κB, JNK, mTOR activation | 34341167 |
| **Card11 knockout / "unmodulated" (LOF)** | Null / LOF | Combined immunodeficiency; impaired B/T antigen-receptor-induced NF-κB — the **opposite** pole of the allelic series | — |

**In-vitro / cellular models (heavily used):**
- **HEK293T transfection** NF-κB reporter assays to quantify constitutive activation.
- **Patient-derived primary lymphocytes** and lymphocyte cell lines (e.g., **Jurkat**) for signaling and mCADS aggregation studies ([PMID: 32473470](https://pubmed.ncbi.nlm.nih.gov/32473470/), [PMID: 23129749](https://pubmed.ncbi.nlm.nih.gov/23129749/), [PMID: 40157432](https://pubmed.ncbi.nlm.nih.gov/40157432/)).
- ABC-DLBCL cell lines carrying analogous somatic CARD11 mutations as a disease-adjacent model.

**Phenotype recapitulation.** The M365K knock-in reproduces the **lymphocyte hyperactivation/proliferation** core of BENTA. **Limitations:** mouse models do not fully capture human T-cell anergy, the HLH/EBV-driven mortality, or the human malignancy spectrum (EBV does not infect mice); the biallelic R331P human phenotype has no mouse equivalent.

**Resources:** MGI (mouse *Card11*), IMPC/IMSR for knockout lines; Cellosaurus/ATCC for cell lines.

---

## Key Findings (Consolidated)

### Finding 1 — BENTA is caused by germline gain-of-function *CARD11* mutations (autosomal dominant)
Snow et al. (2012) identified germline heterozygous **E127G** (familial) and **G116S** (unrelated) in the CARD11 coiled-coil domain, both driving constitutive NF-κB activation ([PMID: 23129749](https://pubmed.ncbi.nlm.nih.gov/23129749/)). An expanding allelic series now includes G123D, C49Y, M365K, D357E, K215del, G123S, and the homozygous R331P. Inheritance is autosomal dominant (de novo and inherited), with one biallelic case ([PMID: 40157432](https://pubmed.ncbi.nlm.nih.gov/40157432/)).

### Finding 2 — Mechanism: GOF CARD11 self-aggregates to nucleate a constitutive CBM signalosome
Mutant CARD11 forms cytosolic aggregates (mCADS) colocalizing with MALT1 and phospho-IKK, driving antigen-independent NF-κB activity ([PMID: 32473470](https://pubmed.ncbi.nlm.nih.gov/32473470/)). The CBM complex is the essential link between antigen receptors and NF-κB ([PMID: 25087226](https://pubmed.ncbi.nlm.nih.gov/25087226/)).

### Finding 3 — Clinical phenotype: early-onset polyclonal B-cell lymphocytosis with HLH and lymphoma risk
Core presentation: polyclonal B lymphocytosis, splenomegaly, lymphadenopathy, recurrent infections ([PMID: 40157432](https://pubmed.ncbi.nlm.nih.gov/40157432/)). HLH in ~18.8%; lymphocytosis not universal. Severe cases reach 20,000–90,000/mm³, exacerbated by EBV and splenectomy ([PMID: 25352053](https://pubmed.ncbi.nlm.nih.gov/25352053/)).

### Finding 4 — Treatment/prognosis: often indolent but early-childhood fatal complications
15/34 asymptomatic or improved without treatment; all 6 deaths before age 3 (2 HLH, 4 opportunistic infection) ([PMID: 39998705](https://pubmed.ncbi.nlm.nih.gov/39998705/)). Corticosteroids, sirolimus, tacrolimus used; MALT1/BTK inhibition investigational.

### Finding 5 — Model organisms: Card11 M365K knock-in mouse recapitulates GOF; Card11-null is immunodeficient
The M365K knock-in increases lymphocyte activation/proliferation ([PMID: 36960072](https://pubmed.ncbi.nlm.nih.gov/36960072/)); Card11 KO causes combined immunodeficiency (opposite pole). In-vitro HEK293T and patient-cell assays are mainstays.

### Finding 6 — CARD11 allelic series, epidemiology, identifiers
Three diseases from one gene (CID 615206 LOF; CADINS 617638 DN-LOF; BENTA 616452 GOF). Ultra-rare (<~40 patients). GOF variants near-absent in gnomAD.

### Finding 7 — B-cell immunophenotype: polyclonal, naïve-surface, aberrant transcriptional program
Biallelic R331P patient showed massive naïve B-cell expansion with aberrant transcription ([PMID: 41456721](https://pubmed.ncbi.nlm.nih.gov/41456721/)); B cells show upregulated cell-cycle genes and enhanced proliferation/survival ([PMID: 25352053](https://pubmed.ncbi.nlm.nih.gov/25352053/)). T cells retain Vβ diversity but are hyporesponsive ([PMID: 37401643](https://pubmed.ncbi.nlm.nih.gov/37401643/)).

### Finding 8 — Predisposition to lymphoid malignancy (B-cell and T-cell)
The BENTA lesion class occurs somatically in ABC-DLBCL ([PMID: 32473470](https://pubmed.ncbi.nlm.nih.gov/32473470/)); activating CARD11 mutations predispose to B-cell malignancy ([PMID: 23129749](https://pubmed.ncbi.nlm.nih.gov/23129749/)); two unrelated patients developed SPTCL T-cell lymphoma ([PMID: 37562721](https://pubmed.ncbi.nlm.nih.gov/37562721/)).

---

## Mechanistic Model / Interpretation

BENTA is best understood as the **germline, whole-organism manifestation of the same oncogenic lesion that, acquired somatically, produces ABC-DLBCL**. A single structural change in CARD11 relieves its autoinhibition, allowing it to aggregate and self-assemble the CBM signalosome in the absence of antigen. The downstream NF-κB output is cell-type-divergent: B cells interpret constitutive NF-κB as a proliferation/survival signal and expand polyclonally, whereas T cells become anergic — a paradox likely reflecting chronic-signaling-induced desensitization and lineage-specific wiring. This divergence is the disease's defining signature ("B-cell Expansion" + "T-cell Anergy").

The **bimodal prognosis** maps onto allele strength and environmental triggers. Strong alleles plus EBV plus the vulnerable infant immune system can tip the system from indolent lymphoproliferation into HLH or fatal opportunistic infection; weak alleles produce lifelong but benign lymphocytosis. This model explains why **splenectomy worsens disease** (removing a filter redistributes/boosts the expansion), why **sirolimus/mTOR and calcineurin inhibition help** (dampening the proliferative arm), and why **downstream MALT1/BTK inhibitors are the most rational targeted strategy** — they attack the single constitutively active node common to all BENTA alleles.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports |
|---|---|---|
| [23129749](https://pubmed.ncbi.nlm.nih.gov/23129749/) | *Congenital B-cell lymphocytosis explained by novel germline CARD11 mutations* | Causal gene, E127G/G116S, B-malignancy predisposition |
| [32473470](https://pubmed.ncbi.nlm.nih.gov/32473470/) | *GOF mutations in CARD11 promote enhanced aggregation...* | mCADS aggregation mechanism, DLBCL link |
| [25087226](https://pubmed.ncbi.nlm.nih.gov/25087226/) | *The CBM signalosome complex...* | CBM as antigen-receptor→NF-κB link |
| [40157432](https://pubmed.ncbi.nlm.nih.gov/40157432/) | *BENTA disease or CARD11 GOF?* | AD inheritance, core phenotype, HLH 18.8% |
| [25352053](https://pubmed.ncbi.nlm.nih.gov/25352053/) | *Germline CARD11 mutation... severe congenital B-cell lymphocytosis* | Severity, EBV/splenectomy, B-cell program |
| [39998705](https://pubmed.ncbi.nlm.nih.gov/39998705/) | *Successful treatment with sirolimus...* | Outcomes (6 deaths <3y), sirolimus/prednisolone |
| [41456721](https://pubmed.ncbi.nlm.nih.gov/41456721/) | *B-cell lymphocytosis... biallelic CARD11* | Naïve B-cell expansion, transcriptional reprogramming, biallelic R331P |
| [37401643](https://pubmed.ncbi.nlm.nih.gov/37401643/) | *BENTA overlapping with HLH* | T-cell hyporesponsiveness, HLH overlap |
| [37562721](https://pubmed.ncbi.nlm.nih.gov/37562721/) | *SPTCL in two BENTA individuals* | T-cell lymphoma predisposition |
| [36129242](https://pubmed.ncbi.nlm.nih.gov/36129242/) | *Familial G123D...* | Inheritance, autoimmune features, tacrolimus |
| [31897776](https://pubmed.ncbi.nlm.nih.gov/31897776/) | *K215del deletion...* | Mild allele, subtle NF-κB increase |
| [25930198](https://pubmed.ncbi.nlm.nih.gov/25930198/) | *Mild lymphocytosis with C49Y* | Mild allele, variable expressivity |
| [37126937](https://pubmed.ncbi.nlm.nih.gov/37126937/) / [34783281](https://pubmed.ncbi.nlm.nih.gov/34783281/) / [19897720](https://pubmed.ncbi.nlm.nih.gov/19897720/) / [27070702](https://pubmed.ncbi.nlm.nih.gov/27070702/) | MALT1/CBM targeting in DLBCL | Investigational therapeutic rationale |
| [34341167](https://pubmed.ncbi.nlm.nih.gov/34341167/) | Mouse Card11 R30W allele | CARD11 → NF-κB/JNK/mTOR; allelic series |

All eight findings are **human-clinical** at their core, reinforced by **in-vitro functional** assays (NF-κB reporters, mCADS) and **mouse-model** corroboration (M365K GOF, Card11-null LOF).

---

## Limitations and Knowledge Gaps

1. **Rarity limits epidemiology.** With <40 patients, there is no prevalence/incidence, no formal survival statistics, and selection/publication bias toward severe cases.
2. **Mechanism of T-cell anergy is incompletely resolved** — the paradox of an activating lesion causing T-cell hyporesponsiveness is inferred, not fully demonstrated.
3. **No genotype–phenotype rule is validated.** Allele-severity correlations are observational; the same variant can give variable expressivity.
4. **No disease-specific clinical trials or approved targeted therapy.** MALT1/BTK inhibition is extrapolated from DLBCL, not tested in BENTA.
5. **Model limitations.** Mice don't capture EBV-driven exacerbation, HLH mortality, or human malignancy spectrum; no model of biallelic R331P.
6. **No epigenetic or multi-omic disease-wide datasets**, and no QoL instruments applied.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international BENTA registry** to capture natural history, genotype–phenotype correlations, and outcomes prospectively.
2. **Allele-resolved functional screen** of all reported CARD11 variants in a uniform NF-κB/mCADS assay to build a quantitative severity ladder.
3. **Preclinical test of MALT1 paracaspase inhibitors and BTK inhibitors** in the Card11 M365K knock-in mouse and patient-derived B cells, measuring lymphocytosis, NF-κB output, and HLH susceptibility.
4. **Single-cell multi-omics (scRNA-seq + CITE-seq) of paired B and T compartments** across mild vs severe patients to dissect the proliferation-vs-anergy divergence.
5. **Define EBV interaction mechanistically** — controlled infection of patient B cells / humanized models to clarify the EBV × CARD11-GOF HLH/lymphoma axis.
6. **Develop consensus diagnostic and surveillance guidelines**, emphasizing the <3-year critical window, splenectomy avoidance, and malignancy monitoring.
7. **Pilot sirolimus/mTOR vs calcineurin-inhibitor comparison** in symptomatic patients within a registry-embedded study.

---

*Report compiled from 21 primary papers across a 5-iteration autonomous investigation. Evidence types are distinguished as human-clinical, in-vitro functional, and model-organism throughout. All quoted abstract excerpts are verbatim from the cited PMIDs.*


## Artifacts

- [OpenScientist final report](BENTA_Disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](BENTA_Disease-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 14 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:37126937` (4 mentions) - Function and targeting of MALT1 paracaspase in cancer.
  - shared terms: cell, cbm

Weighed against this report's own most characteristic terms: `card11`, `hlh`, `benta`, `b-cell`, `infection`, `disease`, `patient`, `gof`, `lymphocytosis`, `germline`, `t-cell`, `gene`, `biallelic`, `ebv`, `cell`, `anergy`, `severe`, `r331p`, `cbm`, `variant`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 1 |
| Terms whose name was checked | 20 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014645` (2 mentions) - the report calls it "MONDO"; MONDO calls it **BENTA disease**
- `HP:0001744` (1 mention) - the report calls it "Common"; HP calls it **Splenomegaly**
- `HP:0002716` (1 mention) - the report calls it "Common"; HP calls it **Lymphadenopathy**
- `HP:0002719` (1 mention) - the report calls it "Common"; HP calls it **Recurrent infections**
- `GO:0005737` (2 mentions) - the report calls it "cytoplasm / aggregate localization"; GO calls it **cytoplasm**
- `NCIT:C312` (1 mention) - the report calls it "Prednisolone"; NCIT calls it **Bleomycin Sulfate**
- `NCIT:C1133` (1 mention) - the report calls it "Tacrolimus"; NCIT calls it **ImuVert**
- `NCIT:C157808` (1 mention) - the report calls it "Relief of airway obstruction from lymphoid hyperplasia"; NCIT calls it **Casts and Splints**
- `NCIT:C15431` (1 mention) - the report calls it "Considered for severe/refractory cases (not established)"; NCIT calls it **Hematopoietic Cell Transplantation**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0005435` (obsolete Impaired T cell function) (1 mention) - replaced by `HP:0011840`
- `GO:0051092` (obsolete positive regulation of NF-kappaB transcription factor activity) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0005435` (1 mention) - the report calls it "Impaired T-cell function"; HP calls it **obsolete Impaired T cell function**
- `HP:0040286` (1 mention) - the report calls it "Abnormal tonsil morphology"; HP calls it **Abnormal axial muscle morphology**
- `GO:0051092` (1 mention) - the report calls it "positive regulation of NF-κB transcription factor activity"; GO calls it **obsolete positive regulation of NF-kappaB transcription factor activity**
- `GO:0038095` (1 mention) - the report calls it "BCR signaling pathway"; GO calls it **Fc-epsilon receptor signaling pathway**