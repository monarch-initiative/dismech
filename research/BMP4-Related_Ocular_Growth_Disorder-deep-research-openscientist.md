---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-09T16:55:47.906260'
end_time: '2026-11-09T17:25:52.117742'
duration_seconds: 1804.21
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: BMP4-Related Ocular Growth Disorder
  mondo_id: MONDO:0100613
  category: Mendelian
  causal_genes: BMP4
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
citation_count: 22
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 22
  on_topic: 15
  validator_version: 0.5.1
term_validation:
  total_terms: 35
  verified: 33
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 0
  labels_mismatched: 15
  mislabelled_terms:
  - term_id: HP:0000568
    reported_labels:
    - Structural
    ontology_label: Microphthalmia
  - term_id: HP:0000528
    reported_labels:
    - Structural
    ontology_label: Anophthalmia
  - term_id: HP:0000589
    reported_labels:
    - Structural
    ontology_label: Coloboma
  - term_id: HP:0000483
    reported_labels:
    - Structural
    ontology_label: Astigmatism
  - term_id: HP:0000556
    reported_labels:
    - Clinical sign
    ontology_label: Retinal dystrophy
  - term_id: HP:0011003
    reported_labels:
    - Clinical sign
    ontology_label: High myopia
  - term_id: HP:0012443
    reported_labels:
    - Structural
    ontology_label: Abnormal brain morphology
  - term_id: HP:0012503
    reported_labels:
    - Endocrine/structural
    ontology_label: Abnormal pituitary gland morphology
  - term_id: HP:0000776
    reported_labels:
    - Structural
    ontology_label: Congenital diaphragmatic hernia
  - term_id: HP:0001510
    reported_labels:
    - Clinical sign
    ontology_label: Growth delay
  - term_id: HP:0001263
    reported_labels:
    - Neuro/behavioral
    ontology_label: Global developmental delay
  - term_id: HP:0000110
    reported_labels:
    - Structural
    ontology_label: Renal dysplasia
  - term_id: HP:0000347
    reported_labels:
    - Structural
    ontology_label: Micrognathia
  - term_id: UBERON:0000970
    reported_labels:
    - Primary organ:** Eye/globe
    ontology_label: eye
  - term_id: UBERON:0000955
    reported_labels:
    - Secondary involvement:** Brain
    ontology_label: brain
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: BMP4-Related_Ocular_Growth_Disorder-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: BMP4-Related_Ocular_Growth_Disorder-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** BMP4-Related Ocular Growth Disorder
- **MONDO ID:** MONDO:0100613 (if available)
- **Causal gene(s):** BMP4
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

Please provide a comprehensive research report on **BMP4-Related Ocular Growth Disorder** covering all of the
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

# BMP4-Related Ocular Growth Disorder (MONDO:0100613) — Comprehensive Disease Characterization

**MONDO:** MONDO:0100613 · **Causal gene:** **BMP4** (Bone Morphogenetic Protein 4; HGNC:1071; NCBI Gene 652; chromosome 14q22.2) · **OMIM:** 607932 (Microphthalmia, syndromic 6) · **Category:** Mendelian (autosomal dominant)

## Summary

**BMP4-Related Ocular Growth Disorder** (MONDO:0100613; corresponding to OMIM 607932, *Microphthalmia, syndromic 6* [MCOPS6]) is a rare, congenital, autosomal-dominant developmental eye malformation caused by **heterozygous loss-of-function (LOF) variants** in, and **14q22.2 contiguous-gene deletions** of, the gene **BMP4** — which encodes **Bone Morphogenetic Protein 4**, a secreted morphogen of the TGF-β/BMP superfamily. The disease name is a serial descriptor; its causal gene is unambiguously **BMP4**, not any of the many other anophthalmia/microphthalmia genes (e.g., *OTX2*, *SOX2*, *STRA6*, *SALL4*, *NAA10*), which cause clinically overlapping but genetically distinct conditions.

The mechanistic core of the disorder is **morphogen dosage sensitivity**. BMP4 is the **dorsal morphogen of the optic cup**: the *level* of BMP4 signaling sets dorso-ventral patterning through a Tbx2/Tbx3/Tbx5-versus-Vax1/Vax2 gene expression system, operating within an integrated BMP4–Sonic hedgehog (Shh)–FGF8 signaling network and antagonized by Shh ventrally. When one BMP4 allele is lost, this dosage-dependent patterning and the growth of the eye are disrupted, producing **microphthalmia/anophthalmia with coloboma**, anterior-segment anomalies (sclerocornea, Axenfeld-Rieger-type malformation), retinal dystrophy, and high myopia. Because BMP4 is expressed in the optic vesicle, retina, lens, pituitary region, and developing digits, the disorder is **pleiotropic**, frequently accompanied by brain malformation, pituitary/hypopituitary anomalies, polydactyly/syndactyly, growth delay, skeletal defects, and — across the allelic spectrum — Stickler-syndrome-like and renal (CAKUT) features.

Clinically, the condition shows **incomplete penetrance and highly variable expressivity**, modified in part by the **Hedgehog pathway** (digenic "low-penetrance" BMP4 + HH-pathway cases are documented). There is **no gene-specific or disease-modifying therapy**; care is supportive, reconstructive (socket/orbital expansion, prosthetics, with good cosmetic outcomes), and multidisciplinary, anchored by genetic counseling. This report consolidates nine confirmed findings drawn from human clinical genetics, mouse/zebrafish/chick developmental models, and in vitro studies across 27 reviewed papers.

---

## Key Findings

### Finding 1 — BMP4 loss-of-function causes a syndromic microphthalmia/anophthalmia spectrum (MCOPS6)

The foundational human-genetic evidence comes from Reis et al. 2011 ([PMID: 21340693](https://pubmed.ncbi.nlm.nih.gov/21340693/)), who screened **133 patients** with ocular developmental disorders and identified disease-causing *BMP4* lesions in several. These included **2 patients with BMP4 deletions** (presenting with SHORT syndrome and anterior-segment anomalies) and **3 intragenic mutations**:

- a nonsense variant **c.592C>T (p.R198X)** in a patient with anophthalmia/microphthalmia with sclerocornea, right-sided diaphragmatic hernia, and hydrocephalus;
- a frameshift **c.171dupC (p.E58RfsX17)** in half-siblings with anophthalmia/microphthalmia, polydactyly, and poor growth;
- a missense **c.362A>G (p.H121R)**.

The authors documented **variable expressivity and non-penetrance** — one variant was carried by an unaffected mother. In their words: *"A patient with anophthalmia, microphthalmia with sclerocornea, right-sided diaphragmatic hernia, and hydrocephalus was found to have a c.592C >T (p.R198X) nonsense mutation in BMP4,"* and these results *"significantly expand the number of reported loss-of-function mutations, further support the critical role of BMP4 in ocular development, and provide additional evidence of variable expression/non-penetrance of BMP4"* ([PMID: 21340693](https://pubmed.ncbi.nlm.nih.gov/21340693/)). This establishes the **loss-of-function/haploinsufficiency** mechanism that defines the disorder.

### Finding 2 — BMP4 acts within an Lhx2-regulated network driving optic cup formation and lens induction

Yun et al. 2009 ([PMID: 19906857](https://pubmed.ncbi.nlm.nih.gov/19906857/)) showed that in *Lhx2*-null mouse embryos, eye development arrests **before optic cup formation**. Of the signaling pathways examined, *"only BMP signaling is noticeably altered and Bmp4 and Bmp7 mRNAs are undetectable."* Supplying exogenous BMP to *Lhx2*-null optic vesicle/lens ectoderm restored expression of lens-inducing determinants (Pax2, Fgf15, Sox2). This places **BMP4 downstream of Lhx2 and upstream of lens induction**, mechanistically linking BMP4 loss to failed eye morphogenesis and explaining why *BMP4* haploinsufficiency can produce an absent or severely reduced eye.

### Finding 3 — BMP4 mutations cause overlapping eye–brain–digit anomalies, with a BMP4–Hedgehog interaction

The landmark gene-identification study, Bakrania et al. 2008 ([PMID: 18252212](https://pubmed.ncbi.nlm.nih.gov/18252212/)), identified a frameshift **c.226del2 (p.S76fs104X)** segregating with anophthalmia-microphthalmia (AM), retinal dystrophy, myopia, brain anomalies, and polydactyly in a family, plus a non-conservative missense **c.278A>G (p.E93G)** in another. The authors reported that they *"analyzed the BMP4 (Bone Morphogenetic Protein-4) gene and identified a frameshift mutation (c.226del2, p.S76fs104X) that segregated with AM, retinal dystrophy, myopia, brain anomalies, and polydactyly in a family and a nonconservative missense mutation (c.278A-->G, p.E93G)."* In human embryos, they *"demonstrate expression of BMP4 in optic vesicle, developing retina and lens, pituitary region, and digits strongly supporting BMP4 as a causative gene for AM, pituitary, and poly/syndactyly,"* providing the spatial basis for the disorder's pleiotropy. Critically, they also *"identified four cases, some of whom had retinal dystrophy, with 'low-penetrant' mutations in both BMP4 and HH,"* supporting a **digenic / modifier model** in which the Hedgehog pathway tunes BMP4 penetrance. They also reported two new 14q22-q23 deletion AM cases (one with pituitary anomalies).

### Finding 4 — 14q22 contiguous deletions and mouse Bmp4+/− recapitulate the eye + digit phenotype

Hayashi et al. 2008 ([PMID: 18925664](https://pubmed.ncbi.nlm.nih.gov/18925664/)) reported *"a 2.7-Mb heterozygous deletion at 14q22.1-q22.3 harboring 18 protein-coding genes. Among the genes, BMP4 was a candidate for the gene causing the abnormalities of both the eye and digits"* in a girl with psychomotor retardation, bilateral congenital corneal opacity, and bilateral postaxial polysyndactyly of the feet. They noted that *"Bmp4 heterozygous null mice revealed skeletal abnormalities including polydactyly and ocular anterior segment abnormalities."* This provides two convergent lines of support: a **contiguous-gene deletion** mechanism in humans and a **mouse haploinsufficiency model** that recapitulates the core phenotypes. (GMFB within the deleted interval is a candidate for the psychomotor retardation, illustrating that deletion cases carry additional contiguous-gene contributions.)

### Finding 5 — BMP4 is the dosage-sensitive dorsal morphogen of the optic cup

Behesti et al. 2006 ([PMID: 17173667](https://pubmed.ncbi.nlm.nih.gov/17173667/)) demonstrated in mouse whole-embryo culture that *"the level of BMP4 signaling is critical for the regulation of distinct Tbx2, Tbx3, Tbx5 and Vax2 gene expression domains along the dorso-ventral axis of the mouse optic cup."* BMP4/Noggin beads shifted these domains and altered growth. This **dosage-sensitivity is the direct mechanistic basis for haploinsufficiency**: a 50% reduction in BMP4 is sufficient to mis-pattern and under-grow the eye.

This dorsal role is embedded in an integrated signaling system. Kobayashi et al. 2010 ([PMID: 20298259](https://pubmed.ncbi.nlm.nih.gov/20298259/)) showed that *"bone morphogenetic protein 4 (BMP4) and Sonic hedgehog (Shh) constitute a dorsal-ventral signaling system together with fibroblast growth factor 8 (FGF8),"* specifying optic-vesicle polarity and governing ocular morphogenesis. Zhao et al. 2010 ([PMID: 19854269](https://pubmed.ncbi.nlm.nih.gov/19854269/)) showed that *"In the dorsal part of the developing retina, Bmp4 is expressed and antagonizes the ventralizing effects of Shh signaling through the activation of Tbx5 expression."* In zebrafish, Gosse & Baier 2009 ([PMID: 19164594](https://pubmed.ncbi.nlm.nih.gov/19164594/)) found Gdf6a(Radar) induces *Bmp4/Tbx5/Tbx2b* and suppresses *Vax2* to establish dorsal retinal identity — demonstrating **evolutionary conservation** of the BMP4-driven dorsalization cascade. Pax6 also regulates the FGF8/BMP4 balance during optic-cup patterning (Kim & Lauderdale 2007, [PMID: 17381541](https://pubmed.ncbi.nlm.nih.gov/17381541/)).

### Finding 6 — BMP4 is pleiotropic across an allelic spectrum; the disorder is genetic/developmental with no major environmental trigger

BMP4 LOF produces phenotypes beyond the eye. Nixon et al. 2019 ([PMID: 30568244](https://pubmed.ncbi.nlm.nih.gov/30568244/)) identified *"A novel heterozygous BMP4 variant causing a premature stop codon, c.130G>T, p.(Gly44Ter), which segregated with clinical features of Stickler syndrome in multiple family members"* — with associated **renal dysplasia**. Reis et al. 2011 ([PMID: 21340693](https://pubmed.ncbi.nlm.nih.gov/21340693/)) reported this was *"the first report indicating a role for BMP4 in SHORT syndrome, Axenfeld-Rieger malformation, growth delay, macrocephaly, and diaphragmatic hernia."* BMP4 is also implicated in congenital anomalies of the kidney and urinary tract (CAKUT) via BMP/SMAD signaling ([PMID: 29197384](https://pubmed.ncbi.nlm.nih.gov/29197384/)) and has been examined as a candidate (and excluded) in a syndromic cleft lip/oculodentodigital case ([PMID: 22699666](https://pubmed.ncbi.nlm.nih.gov/22699666/)), reflecting its craniofacial/tooth roles. This is a **Mendelian developmental disorder**: no infectious agent and no established specific teratogen act on the BMP4 genotype itself. A EUROCAT study of Chernobyl radiological contamination ([PMID: 3148908](https://pubmed.ncbi.nlm.nih.gov/3148908/)) found no general increase in anophthalmos/microphthalmos frequency, arguing against a broad environmental driver for the phenotype.

### Finding 7 — Diagnosis relies on clinical/imaging identification plus genomic testing

Diagnosis combines **clinical examination**, **ocular ultrasound/MRI** (globe size, optic nerve, orbital cysts), and **brain/pituitary MRI**, followed by **molecular confirmation**. The Oculome 429-gene NGS panel (Patel et al. 2019, [PMID: 30653986](https://pubmed.ncbi.nlm.nih.gov/30653986/)) includes a dedicated *"microphthalmia-anophthalmia-coloboma (MAC; 86 genes)"* subpanel covering BMP4. **Chromosomal microarray (CMA)** detects 14q22-q23 contiguous-gene deletions. **Whole-genome sequencing adds yield**: in 100 previously undiagnosed families with eye developmental disorders, WGS found (likely) pathogenic variants in 18 patients, and *"fourteen of these variants would have been missed by conventional genes panels or CGH-array, underscoring the broader diagnostic scope of WGS"* ([PMID: 42448966](https://pubmed.ncbi.nlm.nih.gov/42448966/)). Even so, fewer than half of congenital eye-malformation patients receive a definitive molecular diagnosis.

### Finding 8 — Management is supportive, reconstructive, and multidisciplinary

No disease-modifying therapy exists. McLean et al. 2003 ([PMID: 12812886](https://pubmed.ncbi.nlm.nih.gov/12812886/)) studied 34 patients (40 orbits) with microphthalmos/anophthalmos and orbital cysts, using surgical cyst removal (42.5%), cyst retention with conformers (42.5%), silicone expanders, and staged approaches. They reported that *"33 out of 34 patients had a good cosmetic result which illustrates that the orbital cyst in microphthalmos or anophthalmos performs a useful role in socket expansion and that the majority of patients with this condition can expect a good cosmetic outcome."* Management of the newborn is a shared neonatologist–ophthalmologist responsibility ([PMID: 40038803](https://pubmed.ncbi.nlm.nih.gov/40038803/)).

### Finding 9 — Inheritance, epidemiology, and prognosis (consolidated)

The disorder is **autosomal dominant**, caused by heterozygous BMP4 LOF variants or 14q22.2 deletions, frequently **de novo** but transmitted in families, with **incomplete penetrance** (an unaffected obligate carrier is documented, [PMID: 21340693](https://pubmed.ncbi.nlm.nih.gov/21340693/)) and **highly variable expressivity**, modified by the Hedgehog pathway ([PMID: 18252212](https://pubmed.ncbi.nlm.nih.gov/18252212/)). BMP4 is a **rare cause** within the anophthalmia-microphthalmia (A/M) spectrum. Phenotype-level birth prevalence is *"anophthalmia at 0.6-4.2 per 100,000 births and microphthalmia at 2-17 per 100,000 births, with a combined prevalence of up to 30 per 100,000"* ([PMID: 40038803](https://pubmed.ncbi.nlm.nih.gov/40038803/)), and *"around 25% of patients have an underlying genetic syndrome that is diagnosable"* ([PMID: 22005280](https://pubmed.ncbi.nlm.nih.gov/22005280/)). Structural defects are **congenital and non-progressive**; life expectancy is usually normal unless severe syndromic complications (diaphragmatic hernia, major brain malformation, hypopituitarism) occur. The principal lifelong morbidity is **congenital visual impairment/blindness**, with good cosmetic outcomes from socket/orbital rehabilitation. No sex or ethnic predilection is established; pathogenic alleles are ultra-rare in gnomAD.

---

## Report by Template Section

### 1. Disease Information

**Overview.** BMP4-Related Ocular Growth Disorder is a rare congenital developmental disorder of eye growth and patterning caused by reduced dosage of the BMP4 morphogen. It presents within the anophthalmia–microphthalmia–coloboma (A/M/C) spectrum, often syndromic with brain, pituitary, digit, growth, skeletal, and renal involvement.

**Key identifiers.**
- **MONDO:** MONDO:0100613
- **OMIM:** 607932 (Microphthalmia, syndromic 6 / MCOPS6); BMP4 gene OMIM 112262
- **Gene:** BMP4 (HGNC:1071; NCBI Gene 652; chromosome 14q22.2)
- **Orphanet / ICD / MeSH:** Indexed under A/M categories (ICD-10 Q11.x for anophthalmos/microphthalmos; MeSH "Microphthalmos," "Anophthalmos"). A BMP4-specific Orphanet code is not clearly recorded; best indexed via MONDO:0100613 / OMIM 607932.
- **Synonyms:** Microphthalmia syndromic 6 (MCOPS6); BMP4-related microphthalmia/anophthalmia with extraocular anomalies.

**Source of information.** Derived from **aggregated disease-level resources** (OMIM, published case series, model-organism studies) rather than individual EHR data.

### 2. Etiology

- **Primary cause:** Genetic — heterozygous BMP4 loss-of-function (nonsense, frameshift, splice, deleterious missense) variants and 14q22.2 contiguous-gene deletions ([PMID: 21340693](https://pubmed.ncbi.nlm.nih.gov/21340693/), [PMID: 18252212](https://pubmed.ncbi.nlm.nih.gov/18252212/), [PMID: 18925664](https://pubmed.ncbi.nlm.nih.gov/18925664/)).
- **Genetic risk/modifier factors:** Hedgehog-pathway variants act as **digenic modifiers** producing "low-penetrant" phenotypes ([PMID: 18252212](https://pubmed.ncbi.nlm.nih.gov/18252212/)).
- **Environmental risk factors:** None specifically established for the BMP4 genotype. Chernobyl radiological contamination did not raise A/M frequency ([PMID: 3148908](https://pubmed.ncbi.nlm.nih.gov/3148908/)).
- **Protective factors:** None established.
- **Gene–environment interactions:** Not specifically characterized for BMP4; the dominant interaction is **gene–gene** (BMP4 × HH pathway).

### 3. Phenotypes

| Phenotype | Type | HPO suggestion | Onset | Notes / PMID |
|---|---|---|---|---|
| Microphthalmia | Structural | HP:0000568 | Congenital | Core feature |
| Anophthalmia | Structural | HP:0000528 | Congenital | Core feature |
| Coloboma | Structural | HP:0000589 | Congenital | Common |
| Sclerocornea / corneal opacity | Clinical sign | HP:0000647 / HP:0007957 | Congenital | [21340693](https://pubmed.ncbi.nlm.nih.gov/21340693/), [18925664](https://pubmed.ncbi.nlm.nih.gov/18925664/) |
| Anterior-segment dysgenesis / Axenfeld-Rieger | Structural | HP:0000483 | Congenital | [21340693](https://pubmed.ncbi.nlm.nih.gov/21340693/) |
| Retinal dystrophy | Clinical sign | HP:0000556 | Congenital/childhood | [18252212](https://pubmed.ncbi.nlm.nih.gov/18252212/) |
| High myopia | Clinical sign | HP:0011003 | Childhood | [18252212](https://pubmed.ncbi.nlm.nih.gov/18252212/) |
| Polydactyly / polysyndactyly | Physical | HP:0100259 / HP:0001159 | Congenital | [18252212](https://pubmed.ncbi.nlm.nih.gov/18252212/), [18925664](https://pubmed.ncbi.nlm.nih.gov/18925664/) |
| Brain malformation | Structural | HP:0012443 | Congenital | [18252212](https://pubmed.ncbi.nlm.nih.gov/18252212/) |
| Pituitary anomaly / hypopituitarism | Endocrine/structural | HP:0012503 | Congenital | [18252212](https://pubmed.ncbi.nlm.nih.gov/18252212/) |
| Congenital diaphragmatic hernia | Structural | HP:0000776 | Congenital | [21340693](https://pubmed.ncbi.nlm.nih.gov/21340693/) |
| Growth delay / short stature | Clinical sign | HP:0001510 | Childhood | [21340693](https://pubmed.ncbi.nlm.nih.gov/21340693/) |
| Psychomotor/developmental delay | Neuro/behavioral | HP:0001263 | Childhood | Especially deletion cases [18925664](https://pubmed.ncbi.nlm.nih.gov/18925664/) |
| Renal dysplasia (CAKUT) | Structural | HP:0000110 | Congenital | [30568244](https://pubmed.ncbi.nlm.nih.gov/30568244/) |
| Stickler-like / skeletal features | Structural | HP:0000347 | Congenital | [30568244](https://pubmed.ncbi.nlm.nih.gov/30568244/) |

**Characteristics.** Onset is **congenital**; severity is **variable** (from isolated microphthalmia to bilateral anophthalmia with multisystem involvement); structural defects are **stable/non-progressive**; penetrance is **incomplete**. **Quality of life** is dominated by congenital visual impairment/blindness and, where present, neurodevelopmental and endocrine morbidity.

### 4. Genetic / Molecular Information

- **Causal gene:** BMP4 (OMIM 112262; HGNC:1071; 14q22.2).
- **Variant types:** Nonsense (c.592C>T p.R198X; c.130G>T p.Gly44Ter), frameshift (c.171dupC p.E58RfsX17; c.226del2 p.S76fs104X), missense (c.362A>G p.H121R; c.278A>G p.E93G), and whole-gene/contiguous deletions (14q22.1–q22.3, ~2.7 Mb).
- **Classification:** Truncating variants are pathogenic/likely pathogenic by ACMG criteria (PVS1-type for a haploinsufficient gene); missense variants require functional/segregation support.
- **Allele frequency:** Pathogenic alleles are ultra-rare/absent in gnomAD.
- **Origin:** Germline; both de novo and inherited.
- **Functional consequence:** **Loss of function / haploinsufficiency** of a dosage-sensitive morphogen.
- **Modifier genes:** Hedgehog-pathway genes ([PMID: 18252212](https://pubmed.ncbi.nlm.nih.gov/18252212/)).
- **Epigenetics:** Not specifically characterized for this disease.
- **Chromosomal abnormalities:** 14q22.2/14q22-q23 deletions (detectable by CMA).

### 5. Environmental Information

No specific toxins, infectious agents, or lifestyle factors are established as causes of the BMP4 genotype or its penetrance. The condition is genetically determined. Population-level A/M surveillance did not detect an environmental (radiological) signal ([PMID: 3148908](https://pubmed.ncbi.nlm.nih.gov/3148908/)).

### 6. Mechanism / Pathophysiology

**Causal chain (initiating lesion → clinical manifestation):**

1. A **heterozygous BMP4 LOF variant or 14q22.2 deletion** *results in* ~50% reduction of functional BMP4 morphogen (haploinsufficiency). [demonstrated — human genetics]
2. Reduced BMP4 *leads to* loss of the normal **dorsal-high BMP4 signaling gradient** across the optic vesicle/cup. [inferred from dosage experiments]
3. Reduced dorsal BMP4 *results in* **mis-patterning of dorso-ventral gene domains** — downregulation of Tbx2/Tbx3/Tbx5 and failure to restrict Vax1/Vax2 — within the BMP4–Shh–FGF8 system. [demonstrated — mouse/zebrafish]
4. Because BMP4 normally **antagonizes ventralizing Shh** via Tbx5 activation, its loss *leads to* ventralization and disturbed optic-cup polarity. [demonstrated — [PMID: 19854269](https://pubmed.ncbi.nlm.nih.gov/19854269/)]
5. Disrupted patterning, acting downstream of Lhx2, *results in* **impaired optic-cup morphogenesis and defective lens induction** (BMP4 required for Pax2/Fgf15/Sox2 induction). [demonstrated — [PMID: 19906857](https://pubmed.ncbi.nlm.nih.gov/19906857/)]
6. These failures *lead to* **reduced eye growth and structural malformation** → microphthalmia/anophthalmia, coloboma, anterior-segment and retinal anomalies. [clinical correlate]
7. In parallel, loss of BMP4 in its other expression domains (pituitary region, digits, kidney, craniofacial/skeleton) *results in* **extraocular anomalies** — the branch producing brain/pituitary, polydactyly, renal (CAKUT), growth, and Stickler-like features. [demonstrated — expression + clinical]
8. **Hedgehog-pathway genetic background** modulates steps 3–6, *tuning penetrance/expressivity* (digenic low-penetrant cases). [demonstrated — [PMID: 18252212](https://pubmed.ncbi.nlm.nih.gov/18252212/)]

**Pathway/process detail:**
- **Molecular pathway:** TGF-β/BMP–SMAD1/5/8 signaling; integrated with Shh and FGF8; upstream regulators Lhx2, Pax6, Gdf6a(Radar).
- **GO biological processes:** eye development (GO:0001654), optic cup formation involved in camera-type eye development (GO:0003409), dorsal/ventral pattern formation (GO:0009953), BMP signaling pathway (GO:0030509), lens development in camera-type eye (GO:0002088).
- **Cell types (CL):** retinal pigment epithelial cell (CL:0002586), neural retina progenitor cell, lens fiber/epithelial cells, optic-vesicle neuroepithelium.
- **Protein dysfunction:** Haploinsufficiency (reduced secreted ligand), not aggregation or dominant-negative (though some missense alleles may act as hypomorphs).

### 7. Anatomical Structures Affected

- **Primary organ:** Eye/globe (UBERON:0000970) — retina (UBERON:0000966), lens (UBERON:0000965), cornea (UBERON:0000964), anterior segment, optic nerve.
- **Secondary involvement:** Brain (UBERON:0000955), pituitary gland (UBERON:0000007), autopod/digits (UBERON:0002544), kidney/urinary tract (UBERON:0002113), diaphragm (UBERON:0001103), skeleton.
- **Body systems:** Visual, nervous, endocrine, musculoskeletal, renal/urinary.
- **Subcellular (GO CC):** extracellular space/region (GO:0005615) for the secreted ligand; nucleus for downstream SMAD-mediated transcription.
- **Lateralization:** Frequently **bilateral**, but can be unilateral/asymmetric.

### 8. Temporal Development

- **Onset:** Congenital (prenatal, during optic-cup/lens morphogenesis in weeks 3–10 of human gestation).
- **Progression:** Structural malformations are **non-progressive/stable** after birth; secondary complications (e.g., glaucoma, retinal detachment, amblyopia) can evolve.
- **Critical period:** Early optic-vesicle/optic-cup stage — the window in which BMP4 dosage is decisive; there is no post-natal window to correct the primary malformation.
- **Duration:** Lifelong.

### 9. Inheritance and Population

- **Inheritance:** Autosomal dominant; de novo and familial; incomplete penetrance; variable expressivity.
- **Epidemiology:** BMP4 is a rare cause within A/M; phenotype birth prevalence up to ~30/100,000 combined ([PMID: 40038803](https://pubmed.ncbi.nlm.nih.gov/40038803/)); ~25% of A/M is syndromic/diagnosable ([PMID: 22005280](https://pubmed.ncbi.nlm.nih.gov/22005280/)).
- **Penetrance/expressivity:** Incomplete penetrance (unaffected obligate carrier reported); highly variable expressivity, modified by HH pathway.
- **Mosaicism/founder effects/consanguinity:** Not specifically established; dominant mechanism makes consanguinity non-contributory.
- **Sex ratio / ethnicity:** No established predilection.

### 10. Diagnostics

- **Clinical/imaging:** Ophthalmologic exam; ocular ultrasound/MRI (globe size, optic nerve, orbital cysts); brain and pituitary MRI; renal ultrasound when indicated.
- **Genetic testing:** MAC-focused NGS gene panels (e.g., Oculome 86-gene MAC subpanel, [PMID: 30653986](https://pubmed.ncbi.nlm.nih.gov/30653986/)); single-gene BMP4 testing; chromosomal microarray for 14q22 deletions; WES/WGS, with WGS adding substantial yield for variants missed by panels/CGH-array ([PMID: 42448966](https://pubmed.ncbi.nlm.nih.gov/42448966/)).
- **Differential diagnosis:** Other A/M genes — *OTX2* (note: an OTX2 microdeletion not involving BMP4 can mimic the syndrome, [PMID: 30268123](https://pubmed.ncbi.nlm.nih.gov/30268123/)), *SOX2*, *STRA6*, *SALL4* (acro-renal-ocular, [PMID: 27661448](https://pubmed.ncbi.nlm.nih.gov/27661448/)), *NAA10* (Lenz microphthalmia, [PMID: 24431331](https://pubmed.ncbi.nlm.nih.gov/24431331/)), *RAX*, *VSX2*, *MAB21L2* ([PMID: 15385160](https://pubmed.ncbi.nlm.nih.gov/15385160/)).
- **Screening:** Cascade testing of at-risk relatives; prenatal ultrasound can detect severe microphthalmia/anophthalmia.

### 11. Outcome / Prognosis

- **Survival/mortality:** Generally normal life expectancy; mortality is driven by severe syndromic complications (diaphragmatic hernia, major brain malformation, hypopituitarism).
- **Morbidity/function:** Principal lifelong burden is **congenital visual impairment/blindness**; additional neurodevelopmental, endocrine, renal morbidity in syndromic cases.
- **Recovery:** Primary malformation is irreversible; reconstructive socket/orbital rehabilitation yields good cosmetic outcomes (33/34 patients, [PMID: 12812886](https://pubmed.ncbi.nlm.nih.gov/12812886/)).
- **Prognostic factors:** Laterality and severity of ocular defect; presence/severity of extraocular (brain, pituitary, diaphragmatic) involvement.

### 12. Treatment

No disease-modifying or gene-specific therapy exists. Management is supportive/reconstructive and multidisciplinary:
- **Surgical/interventional (NCIT ~ ocular prosthesis, orbital reconstruction):** staged socket/orbital expansion with conformers, silicone expanders, and self-inflating expanders; orbital cyst management (removal vs retention), which can aid socket expansion ([PMID: 12812886](https://pubmed.ncbi.nlm.nih.gov/12812886/)).
- **Supportive/rehabilitative:** low-vision services, amblyopia management for the better eye, prosthetic fitting, endocrine replacement if hypopituitary, and management of renal/respiratory/neurodevelopmental complications.
- **Advanced/experimental therapeutics:** None established; no gene, cell, RNA, or targeted therapy in clinical use for this gene.
- **Pharmacogenomics:** Not applicable.

### 13. Prevention

- **Primary prevention:** Not applicable (genetic/developmental).
- **Genetic counseling:** Central — AD inheritance with incomplete penetrance and variable expressivity complicates recurrence-risk estimation; options include prenatal diagnosis and preimplantation genetic testing for known familial variants.
- **Secondary/tertiary prevention:** Early multidisciplinary surveillance (ophthalmology, endocrinology, nephrology, developmental pediatrics) to manage complications and optimize visual/developmental outcomes.

### 14. Other Species / Natural Disease

- **Orthologs:** Mouse *Bmp4* (NCBI Gene 12159), zebrafish *bmp4*, chick *BMP4*.
- **Model phenotypes recapitulate human disease:** *Bmp4+/−* mice show polydactyly and ocular anterior-segment abnormalities ([PMID: 18925664](https://pubmed.ncbi.nlm.nih.gov/18925664/)). Conservation of the BMP4-dorsalization cascade is demonstrated across mouse, chick, and zebrafish.
- **Natural disease in companion animals/wildlife:** Not specifically recorded for BMP4; no established zoonotic relevance (non-transmissible genetic disorder).

### 15. Model Organisms

| Model | System | Key finding | PMID |
|---|---|---|---|
| Mouse *Bmp4+/−* | Mammalian knockout (het) | Polydactyly + ocular anterior-segment defects (recapitulates human) | [18925664](https://pubmed.ncbi.nlm.nih.gov/18925664/) |
| Mouse *Lhx2−/−* | Knockout | Bmp4/Bmp7 undetectable; eye arrests pre-optic-cup; BMP restores lens determinants | [19906857](https://pubmed.ncbi.nlm.nih.gov/19906857/) |
| Mouse whole-embryo culture (BMP4/Noggin beads) | Ex vivo | BMP4 *level* sets Tbx2/3/5 & Vax2 domains and DV growth | [17173667](https://pubmed.ncbi.nlm.nih.gov/17173667/) |
| Mouse optic-vesicle signaling | In vivo/ex vivo | BMP4–Shh–FGF8 DV system; FGF8 upregulation | [20298259](https://pubmed.ncbi.nlm.nih.gov/20298259/) |
| Zebrafish *gdf6a*(Radar) | Mutant/overexpression | Induces Bmp4/Tbx5/Tbx2b, suppresses Vax2 → dorsal retinal identity | [19164594](https://pubmed.ncbi.nlm.nih.gov/19164594/) |
| Chick optic cup (Pax6 electroporation) | In ovo | Pax6 balances FGF8/BMP4 during patterning | [17381541](https://pubmed.ncbi.nlm.nih.gov/17381541/) |

**Recapitulation/limitations:** Mouse haploinsufficiency reproduces eye + digit phenotypes but with its own variable expressivity; models best capture developmental patterning, less so the full human syndromic range (pituitary, renal, Stickler-like features).

---

## Mechanistic Model / Interpretation

```
 BMP4 LOF variant / 14q22.2 deletion
            │ (50% dosage loss — haploinsufficiency)
            ▼
 Loss of dorsal-high BMP4 gradient in optic vesicle/cup
            │
            ▼
 Mis-set DV gene domains:  Tbx2/Tbx3/Tbx5 ↓   Vax1/Vax2 ↑ (de-restricted)
   (within BMP4 ─┤ Shh  and  BMP4 → FGF8 network; downstream of Lhx2, Pax6)
            │
            ├─────────────► Impaired optic-cup morphogenesis + failed lens induction
            │                       │
            │                       ▼
            │               Microphthalmia / Anophthalmia / Coloboma,
            │               anterior-segment dysgenesis, retinal dystrophy, myopia
            │
            └─(other BMP4 domains: pituitary, digits, kidney, craniofacial/skeleton)
                        │
                        ▼
              Brain/pituitary anomalies, polydactyly/syndactyly,
              CAKUT/renal dysplasia, growth delay, Stickler-like/skeletal features

   MODIFIER:  Hedgehog-pathway genotype  ──►  tunes penetrance & expressivity
                                               (digenic "low-penetrant" cases)
```

The unifying principle is **morphogen dosage sensitivity**: BMP4 must be present at the correct level, in the correct dorsal domain, at the correct developmental time. A single functional allele is insufficient to maintain the gradient that patterns and grows the eye, which is why **haploinsufficiency** (rather than dominant-negative misfolding) is the operative mechanism. The same dosage logic, applied across BMP4's multiple expression territories, explains the pleiotropy, and the modifier logic of the co-active Hedgehog pathway explains the incomplete penetrance and variable expressivity that make genetic counseling challenging.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [21340693](https://pubmed.ncbi.nlm.nih.gov/21340693/) | BMP4 LOF in eye disorders incl. SHORT syndrome | Human clinical genetics | LOF mechanism; allelic spectrum; non-penetrance (F1, F6, F9) |
| [18252212](https://pubmed.ncbi.nlm.nih.gov/18252212/) | BMP4 eye–brain–digit anomalies; BMP4–HH overlap | Human genetics + embryo expression | Gene identification; pleiotropy; HH modifier (F3, F9) |
| [18925664](https://pubmed.ncbi.nlm.nih.gov/18925664/) | 14q22.1–q22.3 deletion incl. BMP4 | Human + mouse | Contiguous deletion; Bmp4+/− model (F4) |
| [19906857](https://pubmed.ncbi.nlm.nih.gov/19906857/) | Lhx2 links intrinsic/extrinsic optic-cup factors | Mouse model | BMP4 downstream of Lhx2; lens induction (F2) |
| [17173667](https://pubmed.ncbi.nlm.nih.gov/17173667/) | Level of BMP4 sets Tbx/Vax domains | Mouse ex vivo | Dosage sensitivity (F5) |
| [20298259](https://pubmed.ncbi.nlm.nih.gov/20298259/) | BMP4–Shh–FGF8 DV system | Model organism | DV signaling network (F5) |
| [19854269](https://pubmed.ncbi.nlm.nih.gov/19854269/) | Shh limits Bmp4 to dorsal domain | Model organism | BMP4–Shh antagonism; Tbx5 effector (F5) |
| [19164594](https://pubmed.ncbi.nlm.nih.gov/19164594/) | Gdf6a(Radar) dorsalizes zebrafish retina | Zebrafish | Conservation of BMP4 dorsalization (F5) |
| [17381541](https://pubmed.ncbi.nlm.nih.gov/17381541/) | Pax6 balances FGF8/BMP4 | Chick | Upstream regulation of BMP4 (F5) |
| [30568244](https://pubmed.ncbi.nlm.nih.gov/30568244/) | BMP4 LOF in Stickler + renal dysplasia | Human genetics | Allelic pleiotropy (F6) |
| [12812886](https://pubmed.ncbi.nlm.nih.gov/12812886/) | Management of orbital cysts in A/M | Human clinical series | Reconstructive management (F8) |
| [30653986](https://pubmed.ncbi.nlm.nih.gov/30653986/) | Oculome NGS panel | Human diagnostic | Panel diagnostics (F7) |
| [42448966](https://pubmed.ncbi.nlm.nih.gov/42448966/) | WGS in ocular developmental disorders | Human diagnostic | WGS yield (F7) |
| [40038803](https://pubmed.ncbi.nlm.nih.gov/40038803/) | Management of A/M/coloboma in the newborn | Review | Epidemiology; management (F9) |
| [22005280](https://pubmed.ncbi.nlm.nih.gov/22005280/) | Eye development genes and syndromes | Review | ~25% syndromic A/M (F9) |
| [3148908](https://pubmed.ncbi.nlm.nih.gov/3148908/) | Chernobyl & CNS/eye malformations (EUROCAT) | Epidemiology | No environmental A/M signal (F6) |

**Challenging / nuancing evidence:** [PMID: 30268123](https://pubmed.ncbi.nlm.nih.gov/30268123/) shows that a neighboring OTX2 deletion *not* involving BMP4 can produce a nearly identical syndromic anophthalmia — underscoring the need to confirm BMP4 involvement rather than assuming it from phenotype or locus. [PMID: 27661448](https://pubmed.ncbi.nlm.nih.gov/27661448/) (SALL4, which regulates BMP4) and [PMID: 24431331](https://pubmed.ncbi.nlm.nih.gov/24431331/) (NAA10, dysregulating BMP4/STRA6) show other genes converge on BMP4/retinoic-acid signaling, reinforcing BMP4's network centrality while also representing diagnostic mimics.

---

## Limitations and Knowledge Gaps

1. **No formal penetrance/expressivity estimates.** Penetrance is "incomplete" based on anecdotal unaffected carriers; no cohort-based penetrance figure exists.
2. **BMP4-specific prevalence unknown.** Only phenotype-level (A/M) prevalence is available; the fraction attributable to BMP4 is not quantified.
3. **Genotype–phenotype correlation is weak.** It is unclear why some variants give isolated ocular disease and others severe multisystem syndromes; the relative contribution of HH-pathway modifiers versus stochastic developmental noise is unresolved.
4. **Missense variant interpretation.** Functional assays distinguishing hypomorphic missense alleles from benign variants are limited; most confident calls are for truncating variants and deletions.
5. **No epigenetic or omics profiling** specific to BMP4-related disease in patient tissue (eye tissue is rarely accessible).
6. **No therapeutic pipeline.** No gene/cell/RNA therapy programs target this disorder; all management is downstream and supportive.
7. **Contiguous-deletion confounding.** 14q22 deletion phenotypes reflect multiple genes (e.g., GMFB, OTX2), complicating attribution of specific features to BMP4.

---

## Proposed Follow-up Experiments / Actions

1. **Build a BMP4 variant registry** linking genotype (truncating vs missense vs deletion), penetrance, and syndromic features to derive quantitative penetrance/expressivity estimates and genotype–phenotype rules.
2. **Functional assays for missense/VUS:** BMP–SMAD luciferase reporter and in vitro secretion/activity assays to reclassify VUS per ACMG PS3/BS3.
3. **Test the HH-modifier hypothesis systematically** by sequencing HH-pathway genes in BMP4 carriers to confirm digenic penetrance modulation and quantify its effect size.
4. **Patient-derived iPSC → optic organoids** to model BMP4 haploinsufficiency, measure dorso-ventral marker (TBX5/VAX2) dysregulation, and test whether exogenous BMP4/agonists rescue patterning — a possible proof-of-concept for dosage restoration.
5. **Refine the diagnostic algorithm:** position WGS/CMA earlier for suspected A/M given the demonstrated yield over panels, ensuring BMP4 and the 14q22 region are covered for CNV calling.
6. **Prospective natural-history study** capturing ocular, endocrine, renal, neurodevelopmental, and skeletal outcomes to inform counseling and surveillance schedules.

---

*Evidence source legend:* Human clinical genetics ([21340693](https://pubmed.ncbi.nlm.nih.gov/21340693/), [18252212](https://pubmed.ncbi.nlm.nih.gov/18252212/), [18925664](https://pubmed.ncbi.nlm.nih.gov/18925664/), [30568244](https://pubmed.ncbi.nlm.nih.gov/30568244/)); model organism (mouse/zebrafish/chick: [19906857](https://pubmed.ncbi.nlm.nih.gov/19906857/), [17173667](https://pubmed.ncbi.nlm.nih.gov/17173667/), [20298259](https://pubmed.ncbi.nlm.nih.gov/20298259/), [19854269](https://pubmed.ncbi.nlm.nih.gov/19854269/), [19164594](https://pubmed.ncbi.nlm.nih.gov/19164594/), [17381541](https://pubmed.ncbi.nlm.nih.gov/17381541/)); clinical management/diagnostics ([12812886](https://pubmed.ncbi.nlm.nih.gov/12812886/), [30653986](https://pubmed.ncbi.nlm.nih.gov/30653986/), [42448966](https://pubmed.ncbi.nlm.nih.gov/42448966/)); epidemiology/review ([40038803](https://pubmed.ncbi.nlm.nih.gov/40038803/), [22005280](https://pubmed.ncbi.nlm.nih.gov/22005280/), [3148908](https://pubmed.ncbi.nlm.nih.gov/3148908/)).


## Artifacts

- [OpenScientist final report](BMP4-Related_Ocular_Growth_Disorder-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](BMP4-Related_Ocular_Growth_Disorder-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 22 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 16 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 15 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000568` (1 mention) - the report calls it "Structural"; HP calls it **Microphthalmia**
- `HP:0000528` (1 mention) - the report calls it "Structural"; HP calls it **Anophthalmia**
- `HP:0000589` (1 mention) - the report calls it "Structural"; HP calls it **Coloboma**
- `HP:0000483` (1 mention) - the report calls it "Structural"; HP calls it **Astigmatism**
- `HP:0000556` (1 mention) - the report calls it "Clinical sign"; HP calls it **Retinal dystrophy**
- `HP:0011003` (1 mention) - the report calls it "Clinical sign"; HP calls it **High myopia**
- `HP:0012443` (1 mention) - the report calls it "Structural"; HP calls it **Abnormal brain morphology**
- `HP:0012503` (1 mention) - the report calls it "Endocrine/structural"; HP calls it **Abnormal pituitary gland morphology**
- `HP:0000776` (1 mention) - the report calls it "Structural"; HP calls it **Congenital diaphragmatic hernia**
- `HP:0001510` (1 mention) - the report calls it "Clinical sign"; HP calls it **Growth delay**
- `HP:0001263` (1 mention) - the report calls it "Neuro/behavioral"; HP calls it **Global developmental delay**
- `HP:0000110` (1 mention) - the report calls it "Structural"; HP calls it **Renal dysplasia**
- `HP:0000347` (1 mention) - the report calls it "Structural"; HP calls it **Micrognathia**
- `UBERON:0000970` (1 mention) - the report calls it "Primary organ:** Eye/globe"; UBERON calls it **eye**
- `UBERON:0000955` (1 mention) - the report calls it "Secondary involvement:** Brain"; UBERON calls it **brain**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0001654` (1 mention) - the report calls it "GO biological processes:** eye development"; GO calls it **eye development**