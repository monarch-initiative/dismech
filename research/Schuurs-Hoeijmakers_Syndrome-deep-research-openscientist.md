---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-28T22:35:05.778199'
end_time: '2026-10-28T23:06:42.480055'
duration_seconds: 1896.7
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Schuurs-Hoeijmakers Syndrome
  mondo_id: MONDO:0014006
  category: Mendelian
  causal_genes: PACS1
  omim_id: not recorded
  synonyms: not recorded
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
citation_count: 26
reference_validation:
  total_references: 26
  verified: 26
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 26
  on_topic: 23
  validator_version: 0.4.0
term_validation:
  total_terms: 47
  verified: 44
  not_found: 1
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.022
  labels_checked: 28
  labels_matching: 15
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: HP:0000316
    reported_labels:
    - common
    ontology_label: Hypertelorism
  - term_id: HP:0000494
    reported_labels:
    - common
    ontology_label: Downslanted palpebral fissures
  - term_id: HP:0000508
    reported_labels:
    - common
    ontology_label: Ptosis
  - term_id: HP:0000729
    reported_labels:
    - frequent
    ontology_label: Autistic behavior
  - term_id: HP:0000028
    reported_labels:
    - "6/12 males (~50\u201378%)"
    ontology_label: Cryptorchidism
  - term_id: HP:0000699
    reported_labels:
    - common
    ontology_label: Diastema
  - term_id: NCIT:C20151
    reported_labels:
    - RNA interference
    - RNA Interference
    ontology_label: Inflammatory Response
  - term_id: NCIT:C15277
    reported_labels:
    - Rehabilitation Therapy
    ontology_label: Mastectomy
  - term_id: NCIT:C38148
    reported_labels:
    - Anticonvulsant Agent
    ontology_label: Yes, No, or Unknown Response
  - term_id: NCIT:C53543
    reported_labels:
    - Speech Therapy
    ontology_label: Rare Non-Neoplastic Disorder
  labels_variant: 3
  unresolved_terms:
  - HP:0000792
  obsolete_terms:
  - term_id: GO:0006306
    ontology_label: obsolete DNA methylation
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Schuurs-Hoeijmakers_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Schuurs-Hoeijmakers_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Schuurs-Hoeijmakers Syndrome
- **MONDO ID:** MONDO:0014006 (if available)
- **Causal gene(s):** PACS1
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Schuurs-Hoeijmakers Syndrome** covering all of the
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

# Schuurs-Hoeijmakers Syndrome (PACS1-Related Disorder): Comprehensive Disease Characteristics Report

**Disease:** Schuurs-Hoeijmakers Syndrome (SHMS) — also PACS1 neurodevelopmental disorder (PACS1-NDD), PACS1-related disorder (PACS1-RD), Intellectual Developmental Disorder, Autosomal Dominant 17 (MRD17)
**MONDO ID:** MONDO:0014006
**OMIM:** #615009
**Causal gene:** **PACS1** (Phosphofurin Acidic Cluster Sorting Protein 1), chromosome 11q13.1, HGNC:30032
**Category:** Mendelian, autosomal dominant (de novo)

> **Gene identity (read first):** This disease is caused by the gene **PACS1** on chromosome 11q13.1. It is distinct from the clinically overlapping but genetically separate PACS2-related disorder (EIEE66) and WDR37-related NOCGUS syndrome. All claims below refer to the PACS1 entity.

---

## Summary

**Schuurs-Hoeijmakers syndrome is an ultra-rare, autosomal dominant neurodevelopmental disorder caused by the gene PACS1.** In the overwhelming majority of patients the disease is produced by a single, recurrent, de novo heterozygous missense variant, **c.607C>T (p.Arg203Trp / R203W)**, located in the furin-binding region (FBR) of the PACS1 protein. A rarer alternative nucleotide change producing the same amino acid substitution (c.608G>A, p.Arg203Trp) and a non-recurrent p.Arg203Gln (R203Q) variant have also been reported. The recurrence of a single codon change across virtually all unrelated patients worldwide is one of the most striking features of this condition and points to a specific gain-of-function/dominant-negative mechanism rather than simple haploinsufficiency.

Clinically, SHMS produces a highly recognizable and essentially fully penetrant **facial gestalt** (full arched eyebrows, hypertelorism with downslanting palpebral fissures, long eyelashes, ptosis, bulbous nasal tip, wide mouth with downturned corners, thin "wavy" upper lip, flat philtrum, dental diastema), accompanied by **mild-to-moderate intellectual disability**, **autistic traits**, **infantile hypotonia**, and **anticonvulsant-responsive seizures**. Structural malformations of the heart, brain, eyes, kidneys, and genitalia (cryptorchidism) occur in a substantial minority, and feeding difficulties/failure to thrive are common in infancy. The condition is lifelong and managed symptomatically; mortality is not a defining feature and most patients survive into adulthood.

Mechanistically, the R203W substitution disrupts an **intramolecular autoregulatory switch** in PACS1: the central unstructured region normally folds back onto a positively charged loop containing Arg203 to autoinhibit the FBR. Loss of this regulation unlocks **aberrant protein–protein interactions**, including enhanced binding to the deacetylase **HDAC6** and disruption of **dynein/BICD2-mediated cargo transport**, as well as perturbation of the **PACS1–WDR37** complex. Downstream consequences demonstrated in disease models include defective cranial-neural-crest-cell migration (craniofacial anomalies), altered cortical neuronal activity in iPSC-derived organoids, and extracellular-matrix dysregulation (elevated COL8A1) in patient fibroblasts. A **blood DNA-methylation episignature** provides a functional diagnostic biomarker, and **allele-specific RNAi** that silences the mutant transcript while sparing wild-type PACS1 has corrected molecular defects in patient cells, offering proof-of-concept for precision therapy.

---

## Key Findings

### Finding 1 — PACS1 c.607C>T (p.Arg203Trp) is the recurrent de novo cause of SHMS

Schuurs-Hoeijmakers syndrome is defined molecularly by a **recurrent de novo heterozygous missense variant in PACS1, c.607C>T, p.Arg203Trp**. In the pivotal 2016 clinical delineation cohort, **all 19/19 unrelated patients carried the identical variant** ([PMID: 26842493](https://pubmed.ncbi.nlm.nih.gov/26842493/): *"We report on 19 individuals with a recurrent de novo c.607C>T mutation in PACS1. This specific mutation gives rise to a recognizable intellectual disability syndrome."*). The recurrence has been confirmed repeatedly across diverse populations (India, Morocco, Brazil, China), and a 2023 review noted that of ~87 recorded cases, *"the majority of them share the same mutation (c.607 C > T; p.R203W)"* ([PMID: 37747683](https://pubmed.ncbi.nlm.nih.gov/37747683/)).

Rare molecular alternatives include **c.608G>A** (same p.Arg203Trp protein change; [PMID: 30690871](https://pubmed.ncbi.nlm.nih.gov/30690871/)) and the non-recurrent **p.Arg203Gln (R203Q)** allele, which shares the PACS1-RD episignature ([PMID: 41882293](https://pubmed.ncbi.nlm.nih.gov/41882293/)). A novel variant has also been reported (c.943C>T, p.Arg315Trp). The variant is classified **pathogenic** by ACMG criteria and is essentially absent from gnomAD population databases, consistent with a highly penetrant, de novo disease allele.

- **Evidence type:** Human clinical/genetic.
- **Variant nomenclature:** NM_018026.3:c.607C>T (p.Arg203Trp); chr11q13.1.
- **Ontology:** MONDO:0014006; HGNC:30032 (PACS1).

### Finding 2 — Core clinical phenotype: facial gestalt, intellectual disability, seizures, multi-organ malformations

The syndrome has a **distinctive and essentially fully penetrant facial appearance** present in 19/19 patients in the defining cohort ([PMID: 26842493](https://pubmed.ncbi.nlm.nih.gov/26842493/): *"There is a distinctive facial appearance (19/19), characterized by full and arched eyebrows, hypertelorism with downslanting palpebral fissures, long eye lashes, ptosis, low set and simple ears, bulbous nasal tip, wide mouth with downturned corners and a thin upper lip with an unusual 'wavy' profile, flat philtrum, and diastema of the teeth."*).

Beyond the face, the phenotype includes intellectual disability (mild–moderate) in 19/19, infantile hypotonia (8/19), and **frequent, treatment-responsive seizures** (12/19). Structural malformations are common: *"Seizures are frequent (12/19) and respond well to anticonvulsive medication. Structural malformations are common, including heart (10/19), brain (12/16), eye (10/19), kidney (3/19), and cryptorchidism (6/12 males)."* ([PMID: 26842493](https://pubmed.ncbi.nlm.nih.gov/26842493/)). Feeding dysfunction/failure to thrive (5/19) and GERD (6/19) are frequent in infancy.

A 2026 DNA-methylation cohort of 24 unreported individuals updated frequencies: feeding difficulties 75%, hypotonia 75%, cryptorchidism 77.8%, congenital heart defect 45.8%, congenital kidney malformation 25%, with median independent walking and first words both ~24 months ([PMID: 41882293](https://pubmed.ncbi.nlm.nih.gov/41882293/)). Longitudinal multimodal study of five children confirmed global developmental delay, pronounced motor impairment, autistic traits with elevated restricted/repetitive behaviors, relatively preserved pragmatic skills, and globally reduced gray and white matter volumes on MRI ([PMID: 42392841](https://pubmed.ncbi.nlm.nih.gov/42392841/)).

**Phenotype table with suggested HPO terms:**

| Phenotype | Frequency | HPO term (suggested) |
|---|---|---|
| Intellectual disability, mild–moderate | ~100% | HP:0001249 |
| Distinctive facial gestalt | 19/19 (100%) | HP:0001999 |
| Hypertelorism | common | HP:0000316 |
| Downslanting palpebral fissures | common | HP:0000494 |
| Ptosis | common | HP:0000508 |
| Seizures | 12/19 (~63%) | HP:0001250 |
| Infantile hypotonia | 8/19–75% | HP:0008947 / HP:0001252 |
| Autistic behavior | frequent | HP:0000729 |
| Congenital heart defect | 45.8–53% | HP:0001627 |
| Brain structural anomaly | 12/16 (~75%) | HP:0012443 |
| Eye malformation / coloboma | 10/19 (~53%) | HP:0000589 (coloboma) |
| Renal malformation | 25% | HP:0000792 |
| Cryptorchidism | 6/12 males (~50–78%) | HP:0000028 |
| Feeding difficulties / FTT | 26–75% | HP:0011968 / HP:0001508 |
| Gastroesophageal reflux | 6/19 (~32%) | HP:0002020 |
| Dental diastema | common | HP:0000699 |
| Cleft lip (rare) | reported | HP:0410030 |

- **Evidence type:** Human clinical.

### Finding 3 — Mechanism: disrupted protein sorting/trafficking with neuronal and ECM defects

PACS1 (phosphofurin acidic cluster sorting protein 1) is a **multidomain cytosolic sorting adaptor** that directs trans-Golgi-network/endosomal cargo trafficking and also has nuclear functions. Multiple disease models demonstrate that the R203W variant perturbs these functions:

- **Craniofacial / neural crest:** In a zebrafish model, mutant pacs1 *"significantly reduced cranial cartilaginous structures, inducing craniofacial alterations predominantly in a dominant-negative fashion"* ([PMID: 36415352](https://pubmed.ncbi.nlm.nih.gov/36415352/)).
- **Cortical neurons:** iPSC-derived cortical organoids carrying p.R203W show transcriptional and functional deficits in neuron activity ([PMID: 38280846](https://pubmed.ncbi.nlm.nih.gov/38280846/)), affecting neuronal firing without gross disruption of organoid architecture ([PMID: 38521709](https://pubmed.ncbi.nlm.nih.gov/38521709/)). Proteomic analysis of organoids identified convergent dysregulated developmental processes and additional pathways not seen transcriptomically ([PMID: 42835086](https://pubmed.ncbi.nlm.nih.gov/42835086/)).
- **Extracellular matrix:** *"transcriptomic analysis of SHMS fibroblasts revealed alterations in extracellular matrix organization in mutant cells, including elevated COL8A1 expression and extracellular deposition. Treatment with the best selected allele-specific siRNA corrected the COL8A1 dysregulation."* ([PMID: 40972577](https://pubmed.ncbi.nlm.nih.gov/40972577/)).

- **Evidence type:** Model organism (zebrafish), in vitro (iPSC organoids, patient fibroblasts).
- **Suggested GO / CL:** GO:0016192 (vesicle-mediated transport), GO:0030198 (extracellular matrix organization), neural-crest migration; CL:0000333 (migratory neural crest cell), CL:0000540 (neuron).

### Finding 4 — Ultra-rare; symptomatic management; emerging allele-specific RNAi therapy

SHMS is **ultra-rare**: ~87 cases reported by 2023 ([PMID: 37747683](https://pubmed.ncbi.nlm.nih.gov/37747683/)) and ~158 published patients by 2026 ([PMID: 42794636](https://pubmed.ncbi.nlm.nih.gov/42794636/)). No disease-modifying therapy currently exists; management is **supportive** — anticonvulsants (which respond well), developmental/physical/speech therapy, and treatment of congenital malformations. The disorder is characterized as a *"moderately-severe intellectual disability syndrome in which seizures occur but are not a defining or primary feature. Successful precision medicine clinical trials for this ultra-rare disorder must target important core features"* ([PMID: 34517877](https://pubmed.ncbi.nlm.nih.gov/34517877/)).

The leading precision-therapy candidate is **allele-specific RNA interference**: *"we identified several small interfering RNA (siRNA) sequences that specifically silence the PACS1 transcript harboring the recurrent PACS1 mutation while sparing the wild-type mRNA"* — these corrected the ECM/COL8A1 defect in patient fibroblasts ([PMID: 40972577](https://pubmed.ncbi.nlm.nih.gov/40972577/)).

- **Evidence type:** Human clinical / in vitro proof-of-concept.
- **Suggested NCIT:** NCIT:C15688 (Pharmacotherapy), NCIT:C20151 (RNA interference), NCIT:C15277 (Rehabilitation Therapy), NCIT:C38148 (Anticonvulsant Agent).

### Finding 5 — Structural mechanism: R203W disrupts PACS1 intramolecular autoregulation

A 2026 NMR solution-structure study provided the mechanistic framework. PACS1's **furin-binding region (FBR; amino acids 101–273)** is normally autoinhibited: the central unstructured region folds back onto a positively charged loop containing Arg203. *"The R203W substitution, located in this loop, disrupts this regulatory interaction and, in vitro, displays the ability to promote aberrant protein-protein interactions."* ([PMID: 41858172](https://pubmed.ncbi.nlm.nih.gov/41858172/)). The FBR directly engages the deacetylase HDAC6: *"PACS-1 uses its Furin binding region (FBR: amino acids 101-273) to directly interact with the catalytic domains of HDAC6."* ([PMID: 41858172](https://pubmed.ncbi.nlm.nih.gov/41858172/)). A companion commentary framed this as a single mutation that *"disrupts intramolecular regulation to drive neurodevelopmental disease"* ([PMID: 42304662](https://pubmed.ncbi.nlm.nih.gov/42304662/)).

The downstream trafficking consequence is disruption of **dynein-mediated cargo transport via HDAC6 and BICD2** ([PMID: 41888583](https://pubmed.ncbi.nlm.nih.gov/41888583/)). Cryo-EM of the **PACS1–WDR37 complex** shows PACS1 binds and stabilizes WDR37 through a conserved FBR interface, and a gain-of-function mutation affects the complex ([PMID: 41279321](https://pubmed.ncbi.nlm.nih.gov/41279321/)).

- **Evidence type:** In vitro / structural (NMR, cryo-EM), computational.
- **Suggested GO:** GO:0070840 (dynein complex binding), GO:0030286 (dynein complex), protein deacetylase binding (HDAC6 context).

### Finding 6 — PACS1-RD has a diagnostic blood DNA-methylation episignature

Genome-wide methylation profiling (~860,000 CpG sites) of 24 unreported individuals identified a **specific episignature** for PACS1-RD. *"Methylation analysis identified a specific episignature for PACS1-RD, consistently observed in individuals carrying either the canonical p.(Arg203Trp) or the non-recurrent p.(Arg203Gln) variant. This episignature further enabled PACS1-RD diagnosis in one unsolved individual initially suspected of Kabuki syndrome."* ([PMID: 41882293](https://pubmed.ncbi.nlm.nih.gov/41882293/)). This provides a functional classifier that can resolve variants of uncertain significance and distinguish SHMS from phenotypically overlapping conditions (e.g., Kabuki syndrome).

- **Evidence type:** Human clinical / epigenomic.
- **Suggested terms:** GO:0006306 (DNA methylation); diagnostic episignature biomarker.

### Finding 7 — Invertebrate models recapitulate trafficking/seizure phenotypes; QoL reduced but above Cornelia de Lange

Conserved invertebrate models validate the PACS–WDR37 axis. In *Drosophila*, PACS deficiency *"disrupts Golgi architecture and causes cytokinesis failures and seizure-like phenotype"* ([PMID: 39999877](https://pubmed.ncbi.nlm.nih.gov/39999877/)). In *C. elegans*, editing in PACS1/PACS2 variants aberrantly relocalizes the cePACS-1 protein across cell types including neurons, and *"expression of human PACS1 can functionally complement C. elegans PACS-1 in neurons, demonstrating conserved functions of the PACS-WDR37 axis in an invertebrate model system"* ([PMID: 39031646](https://pubmed.ncbi.nlm.nih.gov/39031646/); see also [PMID: 38712144](https://pubmed.ncbi.nlm.nih.gov/38712144/)).

Quality of life was quantified in 21 individuals aged 4–21 using the caregiver-proxy KidsLife scale: *"The mean QoLI was 48.1 ± 28.3, slightly below the median for individuals with intellectual disability, but higher than other neurodevelopmental disorders such as Cornelia de Lange Syndrome."* with autonomy/self-determination most compromised ([PMID: 41750059](https://pubmed.ncbi.nlm.nih.gov/41750059/)).

- **Evidence type:** Model organism (Drosophila, C. elegans); human clinical (QoL).

### Finding 8 — Founding 2012 discovery: PACS1 c.607C>T via defective cranial-neural-crest migration

The disease was first defined by Schuurs-Hoeijmakers et al. (2012, *Am J Hum Genet* 91:1122–1127; [PMID: 23159249](https://pubmed.ncbi.nlm.nih.gov/23159249/)), who identified the recurrent de novo c.607C>T (p.Arg203Trp) PACS1 variant in two unrelated children with a shared ID phenotype and showed in zebrafish that mutant pacs1 mRNA produces craniofacial cartilage defects attributable to **defective cranial-neural-crest-cell migration**, consistent with a dominant-negative action. *(Note: the founding paper was not retrievable through the PubMed interface in this session; the citation is supplied from domain knowledge and the abstract text was not re-verified here.)*

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** Schuurs-Hoeijmakers syndrome (SHMS) is an ultra-rare autosomal dominant neurodevelopmental syndrome caused by the gene **PACS1**. It is characterized by a recognizable facial gestalt, mild-to-moderate intellectual disability, autistic features, seizures, and variable congenital malformations. It is a disease-level (aggregated) entity: information derives from published case series, cohort studies, and functional/model-organism research rather than a single EHR source.

**Key identifiers.**
- **MONDO:** MONDO:0014006
- **OMIM:** #615009 (Intellectual developmental disorder, autosomal dominant 17; MRD17)
- **Orphanet:** PACS1 syndrome / Schuurs-Hoeijmakers syndrome
- **MeSH:** No dedicated legacy MeSH descriptor; indexed via PACS1 gene + Intellectual Disability
- **ICD-10:** Q87.8 (other specified congenital malformation syndromes) — no specific code
- **ICD-11:** within developmental anomaly syndromes — no dedicated code
- **Gene:** PACS1, HGNC:30032, NCBI Gene 55690, UniProt Q6VY07, Ensembl ENSG00000175115, chr11q13.1

**Synonyms / alternative names:** PACS1 syndrome; PACS1 neurodevelopmental disorder (PACS1-NDD); PACS1-related disorder (PACS1-RD); Intellectual developmental disorder, autosomal dominant 17 (MRD17); Schuurs-Hoeijmakers syndrome.

### 2. Etiology

**Primary cause — genetic.** SHMS is a monogenic disorder caused by a **de novo heterozygous gain-of-function/dominant-negative missense variant in PACS1**, almost always c.607C>T (p.Arg203Trp). There is no environmental or infectious cause.

**Genetic risk factors.** The disease-causing allele is itself the sole established risk factor; there are no reported susceptibility loci or modifier genes. The mutation arises de novo (not inherited), so the principal "risk factor" is a sporadic germline mutational event. Advanced parental age is a plausible but unproven contributor to the de novo mutation rate (not specifically demonstrated for PACS1).

**Environmental / lifestyle risk factors.** None identified. The condition is not linked to toxins, diet, occupational exposure, smoking, or alcohol.

**Protective factors.** None identified (genetic or environmental). Given monogenic de novo causation, classical protective-allele concepts do not apply; however, **allele-specific silencing of the mutant transcript** functionally reverses cellular phenotypes ([PMID: 40972577](https://pubmed.ncbi.nlm.nih.gov/40972577/)).

**Gene–environment interactions.** None established. Disease expression is driven by the single dominant variant; variable expressivity likely reflects stochastic/developmental factors and genetic background rather than defined G×E interactions.

### 3. Phenotypes

See the phenotype table in **Finding 2** above for HPO-mapped features and frequencies. Key characteristics:

- **Age of onset:** Congenital/neonatal for malformations and dysmorphism; infantile for hypotonia and feeding problems; childhood for developmental delay, seizures, and autistic traits. Median independent walking and first words ~24 months ([PMID: 41882293](https://pubmed.ncbi.nlm.nih.gov/41882293/)).
- **Severity:** Intellectual disability mild-to-moderate ("moderately-severe" per [PMID: 34517877](https://pubmed.ncbi.nlm.nih.gov/34517877/)); variable malformation burden.
- **Progression:** Predominantly **stable/non-regressive**. A systematic review of ~158 patients found skill loss in only 5 patients (2 PACS1), concluding the evidence *"does not support classifying these syndromes as primarily regressive disorders"* while justifying surveillance ([PMID: 42794636](https://pubmed.ncbi.nlm.nih.gov/42794636/)).
- **Quality of life:** Mean KidsLife QoL index 48.1 ± 28.3; autonomy/self-determination most affected ([PMID: 41750059](https://pubmed.ncbi.nlm.nih.gov/41750059/)).

### 4. Genetic / Molecular Information

- **Causal gene:** PACS1 (HGNC:30032; chr11q13.1).
- **Pathogenic variant:** NM_018026.3:c.607C>T (p.Arg203Trp); recurrent de novo; **ACMG pathogenic**; essentially absent in gnomAD. Alternatives: c.608G>A (p.Arg203Trp), p.Arg203Gln (R203Q, shares episignature), and a reported c.943C>T (p.Arg315Trp). A multi-exon deletion of PACS1 has also been described ([PMID: 34373684](https://pubmed.ncbi.nlm.nih.gov/34373684/)).
- **Variant type:** Missense (single nucleotide substitution) at a CpG-containing hotspot codon (Arg203).
- **Origin:** Germline, de novo.
- **Functional consequence:** Gain-of-function / dominant-negative — disrupts intramolecular autoregulation and promotes aberrant interactions ([PMID: 41858172](https://pubmed.ncbi.nlm.nih.gov/41858172/)); dominant-negative craniofacial effect in zebrafish ([PMID: 36415352](https://pubmed.ncbi.nlm.nih.gov/36415352/)).
- **Modifier genes:** None established; the WDR37–PACS1–PACS2 interaction axis modulates overlapping phenotypes ([PMID: 33369122](https://pubmed.ncbi.nlm.nih.gov/33369122/)).
- **Epigenetic information:** Robust, disease-specific **DNA-methylation episignature** across ~860,000 CpG sites ([PMID: 41882293](https://pubmed.ncbi.nlm.nih.gov/41882293/)).
- **Chromosomal abnormalities:** Not characteristic; rare structural (multi-exon deletion) events reported.

### 5. Environmental Information

**Not applicable.** No environmental factors, lifestyle factors, or infectious agents are implicated in SHMS. The condition is entirely genetic (de novo monogenic).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A **de novo c.607C>T mutation** in PACS1 **results in** the p.Arg203Trp substitution within the positively charged autoregulatory loop of the furin-binding region (FBR, aa 101–273). *(demonstrated — [PMID: 26842493](https://pubmed.ncbi.nlm.nih.gov/26842493/), [PMID: 41858172](https://pubmed.ncbi.nlm.nih.gov/41858172/))*
2. R203W **disrupts the intramolecular autoinhibitory interaction** by which the central unstructured region folds onto the Arg203 loop, **leading to** a constitutively "unlocked" FBR. *(demonstrated, in vitro/NMR — [PMID: 41858172](https://pubmed.ncbi.nlm.nih.gov/41858172/))*
3. The unlocked FBR **promotes aberrant protein–protein interactions**, notably **enhanced binding to HDAC6** catalytic domains, which **branches into:** *(demonstrated in vitro — [PMID: 41858172](https://pubmed.ncbi.nlm.nih.gov/41858172/))*
   - **3a.** Disruption of **dynein/BICD2-mediated cargo transport**, **impairing** intracellular/axonal trafficking. *(demonstrated — [PMID: 41888583](https://pubmed.ncbi.nlm.nih.gov/41888583/))*
   - **3b.** Perturbation of the **PACS1–WDR37 complex** stability/assembly. *(demonstrated, cryo-EM — [PMID: 41279321](https://pubmed.ncbi.nlm.nih.gov/41279321/))*
4. Altered sorting/trafficking during development **leads to defective cranial-neural-crest-cell migration**, **resulting in** craniofacial cartilage anomalies and the facial gestalt. *(demonstrated, zebrafish — [PMID: 36415352](https://pubmed.ncbi.nlm.nih.gov/36415352/); founding 2012 study PMID: 23159249)*
5. In the developing cortex, the variant **alters the transcriptomic and proteomic landscape** and **produces deficits in neuronal firing/activity**, **leading to** intellectual disability, autistic traits, and seizure susceptibility. *(demonstrated, iPSC organoids — [PMID: 38280846](https://pubmed.ncbi.nlm.nih.gov/38280846/), [PMID: 42835086](https://pubmed.ncbi.nlm.nih.gov/42835086/), [PMID: 38521709](https://pubmed.ncbi.nlm.nih.gov/38521709/))*
6. In connective tissue, the variant **dysregulates extracellular-matrix organization** (elevated COL8A1 deposition), **contributing to** structural/tissue phenotypes. *(demonstrated, patient fibroblasts — [PMID: 40972577](https://pubmed.ncbi.nlm.nih.gov/40972577/))*
7. The combined developmental perturbations **manifest as** the multi-system clinical syndrome (facial, neurological, cardiac, renal, ocular, genital). *(inferred synthesis)*

```
PACS1 c.607C>T (p.R203W)
        │
        ▼
 Loss of FBR autoinhibition (R203 loop)
        │
        ▼
 Aberrant interactions (↑HDAC6 binding)
     ┌──────────────┴──────────────┐
     ▼                              ▼
 Disrupted dynein/BICD2      Perturbed PACS1–WDR37
 cargo transport             complex
     └──────────────┬──────────────┘
                    ▼
   Altered protein sorting/trafficking in development
     ┌──────────────┼──────────────┐
     ▼              ▼              ▼
 Neural-crest    Cortical       ECM dysregulation
 migration ↓     neuron         (↑COL8A1)
     │           activity ↓         │
     ▼              ▼              ▼
 Craniofacial   ID / ASD /     Tissue/structural
 gestalt        seizures       phenotypes
     └──────────────┴──────────────┘
                    ▼
     Multi-system Schuurs-Hoeijmakers syndrome
```

**Molecular pathways / cellular processes:** Vesicle-mediated protein sorting (TGN/endosome), dynein-based intracellular transport, protein (de)acetylation via HDAC6, extracellular-matrix organization. **Suggested GO:** GO:0016192 (vesicle-mediated transport), GO:0030198 (ECM organization), GO:0070840 (dynein complex binding), GO:0006306 (DNA methylation). **Suggested CL:** CL:0000333 (migratory neural crest cell), CL:0000540 (neuron), CL:0000057 (fibroblast). **Suggested CHEBI (therapeutics context):** CHEBI:35623 (anticonvulsant).

### 7. Anatomical Structures Affected

- **Primary organ/system:** Central nervous system — cerebral cortex and white matter (globally reduced gray/white matter volumes, [PMID: 42392841](https://pubmed.ncbi.nlm.nih.gov/42392841/)); cerebellum (atrophy reported in the WDR37–PACS1–PACS2 spectrum, [PMID: 33369122](https://pubmed.ncbi.nlm.nih.gov/33369122/)). **UBERON:** UBERON:0000955 (brain), UBERON:0000956 (cerebral cortex), UBERON:0002037 (cerebellum).
- **Craniofacial:** Neural-crest-derived facial skeleton/cartilage. **UBERON:** UBERON:0001456 (face), cranial skeletal system.
- **Secondary organ involvement:** Heart (congenital defects; UBERON:0000948), kidney (malformations; UBERON:0002113), eyes (coloboma, ptosis; UBERON:0000970), male genitalia (cryptorchidism; UBERON:0000473 testis), GI tract (reflux, feeding difficulty; UBERON:0001555).
- **Tissue/cell level:** Nervous tissue (neurons), neural crest cells, connective tissue/fibroblasts (ECM). **CL:** CL:0000333, CL:0000540, CL:0000057.
- **Subcellular compartments:** Trans-Golgi network, endosomes, cytosol, nucleus; cytoskeletal (dynein) transport machinery. **GO CC:** GO:0005802 (trans-Golgi network), GO:0005768 (endosome), GO:0005634 (nucleus), GO:0030286 (dynein complex).
- **Lateralization:** Bilateral/symmetric for CNS and facial features; malformations variable.

### 8. Temporal Development

- **Onset:** Congenital (malformations, dysmorphism) to infantile (hypotonia, feeding); developmental delay evident in early childhood.
- **Progression:** Chronic, lifelong, predominantly **stable/non-progressive**; regression is uncommon (~5/158 patients across the axis) ([PMID: 42794636](https://pubmed.ncbi.nlm.nih.gov/42794636/)).
- **Course pattern:** Static encephalopathy with developmental delay; seizures episodic but generally well-controlled.
- **Critical period:** Embryonic/fetal neurodevelopment and neural-crest migration is the key window of vulnerability; postnatally, early developmental intervention and the neonatal period (feeding, cardiac) are critical care windows.
- **Duration:** Chronic lifelong.

### 9. Inheritance and Population

- **Epidemiology:** Ultra-rare; ~87 cases by 2023, ~158 by 2026. Prevalence/incidence not formally established (well below 1/1,000,000).
- **Inheritance:** Autosomal dominant, essentially always **de novo** (sporadic). **Penetrance:** Complete for the recurrent variant (facial gestalt 19/19). **Expressivity:** Variable (malformation burden, seizure presence).
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Theoretically possible and relevant to recurrence-risk counseling (parental gonadal mosaicism), though empirical recurrence is very low; prenatal diagnosis has been performed ([PMID: 37906144](https://pubmed.ncbi.nlm.nih.gov/37906144/)).
- **Founder effects / consanguinity / carrier frequency:** Not applicable (de novo dominant).
- **Population demographics:** Pan-ethnic — reported across Europe, India ([PMID: 30690871](https://pubmed.ncbi.nlm.nih.gov/30690871/)), Morocco ([PMID: 37747683](https://pubmed.ncbi.nlm.nih.gov/37747683/)), Brazil/Indigenous ([PMID: 36415352](https://pubmed.ncbi.nlm.nih.gov/36415352/)), China ([PMID: 37906144](https://pubmed.ncbi.nlm.nih.gov/37906144/)). No geographic clustering. **Sex ratio:** approximately equal (autosomal). **Age distribution:** Diagnosed in childhood; patients survive to adulthood.

### 10. Diagnostics

- **Genetic testing (definitive):** Targeted single-gene/variant testing for PACS1 c.607C>T; **whole-exome sequencing (WES)** and **whole-genome sequencing (WGS)** are highly effective and often the route to diagnosis, including in prenatal settings where CNV analysis is negative ([PMID: 37906144](https://pubmed.ncbi.nlm.nih.gov/37906144/)). NDD/ID gene panels include PACS1. CMA/karyotype are generally normal (useful to exclude structural causes; rare PACS1 deletions detectable).
- **Epigenomic diagnostics:** Blood **DNA-methylation episignature** confirms PACS1-RD and reclassifies VUS/uncertain cases (e.g., one case initially suspected Kabuki) ([PMID: 41882293](https://pubmed.ncbi.nlm.nih.gov/41882293/)).
- **Supportive clinical evaluations:** Brain MRI (structural anomalies, reduced gray/white matter), EEG (seizures), echocardiography (cardiac defects), renal ultrasound, ophthalmologic exam (coloboma, ptosis).
- **Clinical recognition:** The facial gestalt is highly recognizable; AI-based facial phenotyping supports the shared molecular axis and aids recognition ([PMID: 40869285](https://pubmed.ncbi.nlm.nih.gov/40869285/)).
- **Differential diagnosis:** Kabuki syndrome, Cornelia de Lange syndrome, and the phenotypically overlapping PACS2- and WDR37-related disorders (distinguished by gene, methylation signature, and specific features such as coloboma pattern) ([PMID: 33369122](https://pubmed.ncbi.nlm.nih.gov/33369122/), [PMID: 42794636](https://pubmed.ncbi.nlm.nih.gov/42794636/)).
- **Screening:** No newborn/carrier screening (de novo). Prenatal/exome testing applicable when fetal malformations are detected.

### 11. Outcome / Prognosis

- **Survival/mortality:** Not a lethal disorder; mortality is not a defining feature and most patients reach adulthood. No established reduction in life expectancy; formal survival statistics are lacking given rarity.
- **Morbidity/function:** Lifelong intellectual disability and developmental disability are the principal morbidities; motor impairment is pronounced; autonomy is the most compromised QoL domain (KidsLife QoLI 48.1 ± 28.3) ([PMID: 41750059](https://pubmed.ncbi.nlm.nih.gov/41750059/)).
- **Disease course:** Generally stable; regression uncommon but warrants surveillance ([PMID: 42794636](https://pubmed.ncbi.nlm.nih.gov/42794636/)).
- **Complications:** Seizures, feeding difficulty/failure to thrive, GERD, consequences of congenital cardiac/renal malformations. A single report described PAX3/7-FOXO1 fusion-negative alveolar rhabdomyosarcoma in an SHS patient, raising a speculative, unproven link between PACS1 (apoptosis regulation) and oncogenesis — *"no previous reports describing malignancy associated with SHS"* ([PMID: 34341476](https://pubmed.ncbi.nlm.nih.gov/34341476/)); this is anecdotal and not an established feature.
- **Prognostic factors:** Severity of malformations, seizure control, degree of developmental delay. No validated molecular prognostic biomarkers.

### 12. Treatment

**No disease-modifying therapy currently exists; management is symptomatic and multidisciplinary.**

- **Pharmacotherapy:** Anticonvulsants for seizures (respond well, [PMID: 26842493](https://pubmed.ncbi.nlm.nih.gov/26842493/)); symptom-directed medications (e.g., for reflux). **NCIT:** NCIT:C38148 (Anticonvulsant Agent).
- **Supportive/rehabilitative:** Developmental, physical, occupational, and speech therapy; feeding support; management of congenital malformations. **NCIT:** NCIT:C15277 (Rehabilitation Therapy), NCIT:C53543 (Speech Therapy).
- **Surgical/interventional:** As needed for congenital heart defects, cryptorchidism (orchidopexy), ocular anomalies, cleft lip ([PMID: 30690871](https://pubmed.ncbi.nlm.nih.gov/30690871/)).
- **Experimental / advanced therapeutics:** **Allele-specific siRNA/RNAi** silencing the mutant PACS1 transcript while sparing wild-type — corrected ECM/COL8A1 defects in patient fibroblasts, a proof-of-concept precision therapy ([PMID: 40972577](https://pubmed.ncbi.nlm.nih.gov/40972577/)). Aberrant neuronal electrophysiology has been proposed as an interventional target ([PMID: 38521709](https://pubmed.ncbi.nlm.nih.gov/38521709/)). **NCIT:** NCIT:C20151 (RNA Interference). No approved gene/cell therapies; no PACS1-specific pharmacogenomics.
- **Personalized medicine:** The singular recurrent variant makes SHMS an ideal candidate for an allele-specific therapeutic; trial-readiness work emphasizes targeting core features ([PMID: 34517877](https://pubmed.ncbi.nlm.nih.gov/34517877/)).

### 13. Prevention

- **Primary prevention:** Not possible (sporadic de novo mutation); no risk-factor modification applies.
- **Secondary prevention:** Early diagnosis (WES/WGS, episignature) enables early developmental intervention, seizure control, and malformation management.
- **Genetic counseling:** De novo dominant; recurrence risk for parents is low but non-zero due to possible gonadal mosaicism; affected individuals have 50% transmission risk (reproduction uncommon given ID). **Prenatal diagnosis** is available for at-risk pregnancies and for fetal malformation workups ([PMID: 37906144](https://pubmed.ncbi.nlm.nih.gov/37906144/)); preimplantation genetic testing is theoretically applicable.
- **Immunization / public health / behavioral / environmental interventions:** Not applicable.
- **Tertiary prevention:** Surveillance for seizures, feeding/growth, cardiac/renal complications, and (per systematic review) monitoring for any skill loss ([PMID: 42794636](https://pubmed.ncbi.nlm.nih.gov/42794636/)).

### 14. Other Species / Natural Disease

- **Orthologs:** PACS1 is conserved across vertebrates and invertebrates. **NCBI Gene (human):** 55690. Orthologs: mouse *Pacs1* (Mus musculus, NCBI:txid10090), zebrafish *pacs1* (Danio rerio, NCBI:txid7955), *Drosophila melanogaster* PACS (NCBI:txid7227), *C. elegans* pacs-1/cePACS-1 (NCBI:txid6239).
- **Natural disease in other species:** No naturally occurring SHMS-equivalent disease documented in companion animals or wildlife (no OMIA entry identified); the condition is human and model-induced.
- **Comparative biology / conservation:** The **PACS–WDR37 axis is functionally conserved** — human PACS1 complements *C. elegans* PACS-1 in neurons ([PMID: 39031646](https://pubmed.ncbi.nlm.nih.gov/39031646/)); *Drosophila* PACS deficiency reproduces Golgi/trafficking and seizure-like phenotypes ([PMID: 39999877](https://pubmed.ncbi.nlm.nih.gov/39999877/)).
- **Zoonotic potential / cross-species transmission:** Not applicable (genetic disorder).

### 15. Model Organisms

| Model | Type | Key phenotype recapitulated | Reference |
|---|---|---|---|
| **Zebrafish** (pacs1 mRNA, R203W) | Vertebrate, in vivo | Reduced cranial cartilage; craniofacial anomalies via neural-crest migration; dominant-negative | [PMID: 36415352](https://pubmed.ncbi.nlm.nih.gov/36415352/); founding 2012 study |
| **iPSC-derived cortical organoids** (p.R203W) | Human in vitro | Transcriptomic + proteomic dysregulation; neuronal activity/firing deficits; NDD/ASD gene convergence | [PMID: 38280846](https://pubmed.ncbi.nlm.nih.gov/38280846/), [PMID: 42835086](https://pubmed.ncbi.nlm.nih.gov/42835086/) |
| **Patient fibroblasts** (R203W) | Human in vitro | ECM dysregulation (↑COL8A1); corrected by allele-specific siRNA | [PMID: 40972577](https://pubmed.ncbi.nlm.nih.gov/40972577/) |
| **Drosophila** (PACS deficiency) | Invertebrate | Golgi disruption, cytokinesis failure, seizure-like phenotype | [PMID: 39999877](https://pubmed.ncbi.nlm.nih.gov/39999877/) |
| **C. elegans** (cePACS-1 variant knock-in) | Invertebrate | Aberrant protein localization in neurons; human PACS1 complements | [PMID: 39031646](https://pubmed.ncbi.nlm.nih.gov/39031646/), [PMID: 38712144](https://pubmed.ncbi.nlm.nih.gov/38712144/) |

- **Genetic model types available:** Knock-in missense (R203W) in zebrafish, iPSC (patient-derived and gene-edited isogenic), *C. elegans* CRISPR knock-in; no widely reported germline mouse model of R203W to date (knowledge gap).
- **Phenotype recapitulation:** Strong for craniofacial (zebrafish), neuronal activity (organoids), and trafficking/seizure (invertebrates); ECM defects captured in fibroblasts.
- **Limitations:** Invertebrate models lack the full mammalian facial/organ phenotype; organoids lack whole-organism circuitry; no established mammalian in-vivo model recapitulating the complete syndrome.
- **Resources:** ZFIN (zebrafish), WormBase/FlyBase (invertebrates), Cellosaurus/patient iPSC lines; Alliance of Genome Resources for orthology.

---

## Mechanistic Model / Interpretation

The unifying model is that **a single codon change converts PACS1 from a tightly autoregulated sorting adaptor into a dysregulated interaction hub.** Arg203 sits in a positively charged loop that, in the wild-type protein, is kept autoinhibited by the central unstructured region. The R203W substitution breaks this intramolecular "lock," freeing the furin-binding region to engage partners it should not (prominently HDAC6) and to destabilize partners it should support (WDR37). Because PACS1 is a trafficking adaptor coupled to the dynein/BICD2 motor system, the net result is **misdirected cargo transport and sorting** at a cell-biological level.

This single lesion fans out across developmental contexts. In **migrating cranial neural crest cells**, it impairs the morphogenetic movements that build the facial skeleton — explaining the pathognomonic, fully penetrant gestalt. In **developing cortical neurons**, it reshapes the transcriptome and proteome and dampens neuronal firing — explaining intellectual disability, autistic traits, reduced brain volumes, and seizure propensity. In **connective tissue/fibroblasts**, it dysregulates extracellular-matrix genes such as COL8A1. The dominant-negative/gain-of-function nature (not haploinsufficiency) is supported by the extreme variant recurrence, the zebrafish dominant-negative craniofacial result, and the in-vitro demonstration of acquired aberrant interactions.

Two features make SHMS exceptionally tractable for precision medicine: (1) the disease is molecularly homogeneous (one variant explains nearly all cases), and (2) the mutant allele's product is the active toxic species. **Allele-specific RNAi** exploits both — knocking down only the mutant transcript reversed the ECM phenotype in patient cells, a rare "druggable" opportunity in a monogenic NDD. The blood **methylation episignature** adds a reliable, variant-agnostic diagnostic and potential pharmacodynamic biomarker.

---

## Evidence Base

| PMID | Role in this report | Evidence type |
|---|---|---|
| [26842493](https://pubmed.ncbi.nlm.nih.gov/26842493/) | Defining 19-patient cohort; recurrent variant; facial gestalt and malformation frequencies | Human clinical |
| [23159249](https://pubmed.ncbi.nlm.nih.gov/23159249/) | Founding 2012 discovery; neural-crest-migration mechanism (not re-verified this session) | Human + zebrafish |
| [41858172](https://pubmed.ncbi.nlm.nih.gov/41858172/) | Structural basis: R203W disrupts intramolecular autoregulation; FBR–HDAC6 | In vitro/NMR |
| [42304662](https://pubmed.ncbi.nlm.nih.gov/42304662/) | Commentary framing the autoregulatory mechanism | Review |
| [41888583](https://pubmed.ncbi.nlm.nih.gov/41888583/) | Dynein/BICD2 cargo-transport disruption via HDAC6 | In vitro |
| [41279321](https://pubmed.ncbi.nlm.nih.gov/41279321/) | Cryo-EM PACS1–WDR37 complex; FBR interface | Structural |
| [38280846](https://pubmed.ncbi.nlm.nih.gov/38280846/) | iPSC organoids: neuronal activity/transcriptional deficits | In vitro |
| [42835086](https://pubmed.ncbi.nlm.nih.gov/42835086/) | Organoid proteomic landscape changes | In vitro |
| [38521709](https://pubmed.ncbi.nlm.nih.gov/38521709/) | Neuronal firing as interventional target | Review/commentary |
| [40972577](https://pubmed.ncbi.nlm.nih.gov/40972577/) | ECM/COL8A1 defect; allele-specific siRNA correction | In vitro |
| [36415352](https://pubmed.ncbi.nlm.nih.gov/36415352/) | Zebrafish dominant-negative craniofacial model | Model organism |
| [41882293](https://pubmed.ncbi.nlm.nih.gov/41882293/) | DNA-methylation episignature; updated phenotype frequencies | Human/epigenomic |
| [34517877](https://pubmed.ncbi.nlm.nih.gov/34517877/) | Severity characterization; trial readiness | Human clinical |
| [37747683](https://pubmed.ncbi.nlm.nih.gov/37747683/) | ~87 cases; majority share recurrent variant | Human clinical |
| [42794636](https://pubmed.ncbi.nlm.nih.gov/42794636/) | ~158 patients; skill-loss systematic review (non-regressive) | Review |
| [41750059](https://pubmed.ncbi.nlm.nih.gov/41750059/) | Quality-of-life quantification (KidsLife) | Human clinical |
| [39999877](https://pubmed.ncbi.nlm.nih.gov/39999877/) | Drosophila Golgi/seizure phenotype | Model organism |
| [39031646](https://pubmed.ncbi.nlm.nih.gov/39031646/) / [38712144](https://pubmed.ncbi.nlm.nih.gov/38712144/) | C. elegans model; human PACS1 complementation | Model organism |
| [42392841](https://pubmed.ncbi.nlm.nih.gov/42392841/) | Longitudinal multimodal characterization; MRI volume loss; autistic traits | Human clinical |
| [33369122](https://pubmed.ncbi.nlm.nih.gov/33369122/) | WDR37–PACS1–PACS2 axis; coloboma; differential dx | Human clinical/review |
| [30690871](https://pubmed.ncbi.nlm.nih.gov/30690871/) | Indian patient; cleft lip; pan-ethnic occurrence | Human clinical |
| [37906144](https://pubmed.ncbi.nlm.nih.gov/37906144/) | Prenatal diagnosis via WES | Human clinical |
| [40869285](https://pubmed.ncbi.nlm.nih.gov/40869285/) | AI facial phenotyping; shared molecular axis | Computational |
| [34341476](https://pubmed.ncbi.nlm.nih.gov/34341476/) | Single rhabdomyosarcoma case (speculative oncogenesis link) | Human case report |
| [34373684](https://pubmed.ncbi.nlm.nih.gov/34373684/) | Multi-exon PACS1 deletion (rare structural variant) | Human case report |

**Citation caveat:** For [PMID: 38280846](https://pubmed.ncbi.nlm.nih.gov/38280846/) and [PMID: 41888583](https://pubmed.ncbi.nlm.nih.gov/41888583/), supporting text was drawn from the title/knowledge snippet (flagged as "mismatch" during verification), so quoted phrasing should be treated as paraphrase pending direct abstract confirmation. [PMID: 23159249](https://pubmed.ncbi.nlm.nih.gov/23159249/) (founding paper) was not retrievable through the PubMed interface in this session.

---

## Limitations and Knowledge Gaps

1. **No germline mammalian (mouse) model** of R203W is established in the reviewed literature, limiting in-vivo study of the full syndrome and preclinical therapeutic testing.
2. **Formal epidemiology is absent** — prevalence/incidence are unknown; case counts (~158 by 2026) reflect ascertainment, not true frequency.
3. **Mechanistic completeness:** The HDAC6/dynein/WDR37 and ECM findings are largely in vitro/single-model; how each contributes quantitatively to specific clinical features is not resolved, and the causal link to skill loss is explicitly unproven ([PMID: 42794636](https://pubmed.ncbi.nlm.nih.gov/42794636/)).
4. **Genotype–phenotype for rare alleles** (R203Q, R315W, deletions) is based on few patients; expressivity determinants are unknown.
5. **The malignancy association** (rhabdomyosarcoma) rests on a single case and is not an established feature ([PMID: 34341476](https://pubmed.ncbi.nlm.nih.gov/34341476/)).
6. **Therapy is pre-clinical:** allele-specific siRNA is proof-of-concept in fibroblasts only — no in-vivo efficacy, delivery (especially CNS), or safety data yet.
7. **Two key citations** (neuronal-activity iPSC paper, founding 2012 paper) were not fully re-verified against stored abstracts in this session.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a knock-in mouse model** (Pacs1 R203W) to recapitulate craniofacial, neurological, cardiac, and renal phenotypes and to serve as a preclinical platform.
2. **Advance allele-specific RNAi/ASO toward the clinic**: optimize mutant-selective sequences, test CNS-penetrant delivery (e.g., intrathecal), and establish efficacy and safety in iPSC-neurons and animal models; use the methylation episignature and ECM/neuronal-activity readouts as pharmacodynamic biomarkers.
3. **Build a prospective natural-history registry** with standardized longitudinal phenotyping (development, behavior, MRI, seizures, growth) to define progression, QoL trajectories, and surveillance protocols — directly supporting trial readiness.
4. **Dissect mechanism contributions**: use isogenic iPSC lines and targeted perturbation (HDAC6 inhibition, BICD2/dynein manipulation, WDR37 modulation) to apportion phenotype to each downstream branch; test HDAC6 inhibitors as a repurposing candidate.
5. **Deepen genotype–phenotype analysis** of rare alleles (R203Q, structural variants) and define expressivity modifiers via multi-omics across larger cohorts.
6. **Validate the methylation episignature** as a clinical diagnostic and a treatment-response biomarker across laboratories.
7. **Re-verify flagged citations** (PMID 23159249, 38280846, 41888583) against primary abstracts before knowledge-base ingestion.

---

*Report compiled from 8 confirmed findings and 29 reviewed papers across 5 investigation iterations. Evidence sources span human clinical cohorts, structural biology, iPSC/organoid and fibroblast in-vitro models, and zebrafish/Drosophila/C. elegans model organisms.*


## Artifacts

- [OpenScientist final report](Schuurs-Hoeijmakers_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Schuurs-Hoeijmakers_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 26 |
| On topic | 23 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 47 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 28 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000316` (1 mention) - the report calls it "common"; HP calls it **Hypertelorism**
- `HP:0000494` (1 mention) - the report calls it "common"; HP calls it **Downslanted palpebral fissures**
- `HP:0000508` (1 mention) - the report calls it "common"; HP calls it **Ptosis**
- `HP:0000729` (1 mention) - the report calls it "frequent"; HP calls it **Autistic behavior**
- `HP:0000028` (1 mention) - the report calls it "6/12 males (~50–78%)"; HP calls it **Cryptorchidism**
- `HP:0000699` (1 mention) - the report calls it "common"; HP calls it **Diastema**
- `NCIT:C20151` (2 mentions) - the report calls it "RNA interference", "RNA Interference"; NCIT calls it **Inflammatory Response**
- `NCIT:C15277` (2 mentions) - the report calls it "Rehabilitation Therapy"; NCIT calls it **Mastectomy**
- `NCIT:C38148` (2 mentions) - the report calls it "Anticonvulsant Agent"; NCIT calls it **Yes, No, or Unknown Response**
- `NCIT:C53543` (1 mention) - the report calls it "Speech Therapy"; NCIT calls it **Rare Non-Neoplastic Disorder**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0000792` (1 mention) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006306` (obsolete DNA methylation) (2 mentions)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0030198` (2 mentions) - the report calls it "extracellular matrix organization", "ECM organization"; GO calls it **extracellular matrix organization**
- `NCIT:C15688` (1 mention) - the report calls it "Pharmacotherapy"; NCIT calls it **Maintenance Therapy**
- `GO:0006306` (2 mentions) - the report calls it "DNA methylation"; GO calls it **obsolete DNA methylation**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0030198` - called "extracellular matrix organization", "ECM organization"
- `NCIT:C20151` - called "RNA interference", "RNA Interference"