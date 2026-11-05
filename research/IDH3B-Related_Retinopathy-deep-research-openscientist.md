---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-04T18:28:52.415701'
end_time: '2026-11-04T19:29:32.168417'
duration_seconds: 3639.75
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: IDH3B-Related Retinopathy
  mondo_id: MONDO:0800393
  category: Mendelian
  causal_genes: IDH3B
  omim_id: not recorded
  synonyms: retinitis pigmentosa 46; RP46
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
citation_count: 9
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 6
  validator_version: 0.5.1
term_validation:
  total_terms: 30
  verified: 27
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 2
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: HP:0000662
    reported_labels:
    - Symptom
    ontology_label: Nyctalopia
  - term_id: HP:0001133
    reported_labels:
    - Clinical sign
    ontology_label: Constriction of peripheral visual field
  - term_id: HP:0007769
    reported_labels:
    - Clinical sign
    ontology_label: Peripheral retinal degeneration
  - term_id: HP:0007843
    reported_labels:
    - Clinical sign
    ontology_label: Attenuation of retinal blood vessels
  - term_id: HP:0001104
    reported_labels:
    - Clinical sign
    ontology_label: Macular hypoplasia
  - term_id: HP:0000512
    reported_labels:
    - Electrophysiology
    ontology_label: Abnormal electroretinogram
  - term_id: HP:0000572
    reported_labels:
    - Symptom
    ontology_label: Visual loss
  - term_id: HP:0000608
    reported_labels:
    - Functional/lab
    ontology_label: Macular degeneration
  - term_id: UBERON:0000966
    reported_labels:
    - retina
    - Organ level:** The **eye**, specifically the **retina
    ontology_label: retina
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
  path: IDH3B-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: IDH3B-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** IDH3B-Related Retinopathy
- **MONDO ID:** MONDO:0800393 (if available)
- **Causal gene(s):** IDH3B
- **OMIM:** not recorded
- **Synonyms:** retinitis pigmentosa 46; RP46
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **IDH3B-Related Retinopathy** covering all of the
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

# IDH3B-Related Retinopathy (Retinitis Pigmentosa 46, RP46): Comprehensive Disease Report

**Disease:** IDH3B-Related Retinopathy · **Causal gene:** *IDH3B* · **MONDO:** MONDO:0800393 · **OMIM:** #612572 (phenotype); *604526 (gene) · **Category:** Mendelian (autosomal recessive)

---

## Summary

**IDH3B-related retinopathy is a rare, autosomal-recessive, nonsyndromic rod–cone dystrophy (retinitis pigmentosa) caused by biallelic loss-of-function variants in *IDH3B***, the gene encoding the β (structural/regulatory) subunit of mitochondrial NAD⁺-specific isocitrate dehydrogenase (NAD-IDH, also called IDH3). The disease is catalogued as **Retinitis Pigmentosa 46 (RP46)**. Although the enzyme IDH3 is a housekeeping component of the tricarboxylic acid (TCA / Krebs) cycle present in every mitochondrion, its loss produces disease confined to the retina. This paradox is the central mechanistic story of the condition: in most tissues the NADP-dependent isocitrate dehydrogenase (IDH2) can substitute for the oxidative decarboxylation of isocitrate, but the metabolically extreme, mitochondria-rich photoreceptors of the retina have a particular requirement for NAD-IDH, so they alone degenerate when it fails.

The disease was discovered by **Hartong et al. (2008, *Nature Genetics*)** in two consanguineous families, in whom affected individuals were homozygous for loss-of-function *IDH3B* mutations ([PMID: 18806796](https://pubmed.ncbi.nlm.nih.gov/18806796/)). Patient-derived cells showed NAD-IDH activity reduced to roughly 5% of normal, with an approximately **300-fold increase in the Km for NAD**, while NADP-IDH (IDH2) activity was preserved and patients had no extra-ocular disease. *IDH3B* is one of three subunit genes of the IDH3 heterotetramer, and strikingly **all three — *IDH3A*, *IDH3B*, and *IDH3G* — cause inherited retinal degeneration**, defining a convergent "IDH3-opathy." Within this family, *IDH3B* disease tends to be **milder and later-onset (≈30–50 years)** than *IDH3A* disease (childhood onset), a difference traced to the biochemistry of subunit assembly: αγ-dimers that survive loss of the β-subunit retain more catalytic activity than αβ-dimers.

This condition is extremely rare. Across ~546 RP probands screened in the original study, only two families carried *IDH3B* variants (~0.4%), and only a handful of pathogenic alleles have ever been reported worldwide: a frameshift **c.589delA (p.Ile197fs)**, a missense **p.Leu98Pro**, and a later missense **p.Gly286Glu**. There is no disease-specific treatment; management is supportive and follows general RP care (low-vision support, vitamin A considerations, surveillance for cataract and cystoid macular edema), with genetic counseling for families. No mouse model yet reproduces the retinopathy — *Idh3b*-null mice instead develop male infertility — which is itself informative about the residual-activity buffering that makes β-subunit loss comparatively mild.

---

## Key Findings

### Finding 1 — Biallelic *IDH3B* loss-of-function mutations cause autosomal-recessive RP (RP46)

The foundational observation, from **Hartong et al. 2008** ([PMID: 18806796](https://pubmed.ncbi.nlm.nih.gov/18806796/)), identified two families with retinitis pigmentosa in which affected members were homozygous for loss-of-function mutations in *IDH3B*. The abstract states directly: *"Affected family members were homozygous for loss-of-function mutations in IDH3B, encoding the beta-subunit of NAD-specific isocitrate dehydrogenase (NAD-IDH, or IDH3), which is believed to catalyze the oxidation of isocitrate to alpha-ketoglutarate in the citric acid cycle."* The inheritance is autosomal recessive, and the disease is confined to the eye (nonsyndromic RP). This finding established *IDH3B* as a retinal disease gene and the TCA cycle as an unexpected locus of photoreceptor vulnerability. The condition is indexed as MONDO:0800393 and OMIM #612572, with the synonyms RP46 and retinitis pigmentosa 46. Evidence type: **human clinical / genetic**.

### Finding 2 — Mechanism: *IDH3B* deficiency cripples NAD-IDH activity while NADP-IDH is spared

In patient-derived cells, NAD-IDH enzymatic activity was substantially reduced, with *"about a 300-fold increase in the K(m) for NAD"* ([PMID: 18806796](https://pubmed.ncbi.nlm.nih.gov/18806796/)). Critically, NADP-specific IDH (IDH2) activity was normal, and the patients had no health problems outside the eye. The authors concluded that *"the retina has a particular requirement for NAD-IDH."* This dissociation — a systemic TCA-cycle enzyme defect that manifests only in the retina — is the keystone of the pathophysiology. The interpretation is that, in most tissues, NADP-IDH (IDH2) can take over the oxidative decarboxylation of isocitrate to α-ketoglutarate, but photoreceptors, with their extraordinary and continuous energy demand, cannot tolerate the loss of the NAD-dependent isoform. The residual NAD-IDH activity in homozygous patient lysates was approximately **4.8% of normal** (heterozygotes ~24%), quantifying the severity of the enzymatic lesion. Evidence type: **in vitro biochemistry on patient cells**.

### Finding 3 — IDH3 is a heterotetramer; all three subunit genes cause inherited retinal degeneration ("IDH3-opathy")

IDH3 functions as an **(αβαγ)₂ heterotetramer** — two catalytic α-subunits (IDH3A) paired respectively with one regulatory β-subunit (IDH3B) and one regulatory γ-subunit (IDH3G) per half-enzyme. Remarkably, pathogenic variants in each of the three subunit genes cause inherited retinal degeneration:

- **IDH3A** — biallelic variants cause autosomal-recessive RP with or without macular pseudocoloboma. The discovery study reported that *"IDH3A variants were identified as a novel cause of typical arRP"* ([PMID: 28412069](https://pubmed.ncbi.nlm.nih.gov/28412069/)).
- **IDH3B** — biallelic variants cause arRP/RP46 (Hartong 2008).
- **IDH3G** — located at the RP34 locus on the X chromosome, causes X-linked RP. Bianco et al. 2025 reported *"4 rare single-nucleotide variants in IDH3G (HGNC:5386), located at the RP34 locus on the X chromosome, and a complete gene deletion, in 5 unrelated male individuals affected with nonsyndromic RP"* ([PMID: 40119724](https://pubmed.ncbi.nlm.nih.gov/40119724/)).

This convergence across all three structural components of a single mitochondrial enzyme is powerful genetic evidence that **loss of IDH3 holoenzyme function — not a subunit-specific moonlighting role — is the shared disease mechanism**. Evidence type: **human genetics across multiple cohorts**.

### Finding 4 — Mouse models do not recapitulate the retinopathy; *Idh3b*-null mice develop infertility, explained by residual αγ-dimer activity

Two mouse studies clarify why *IDH3B* loss is milder than *IDH3A* loss and why modeling has been difficult:

1. **Findlay et al. 2018 (*Disease Models & Mechanisms*)** ([PMID: 30478029](https://pubmed.ncbi.nlm.nih.gov/30478029/)) showed that an *Idh3a* E229K missense mutation causes age-dependent retinal degeneration with reduced mitochondrial maximal respiration and reserve capacity, whereas loss-of-function *Idh3b* mutants show **no retinal degeneration, no retinal stress (no GFAP upregulation), and no respiration defect**. Biochemically, IDH3α alone is inactive; **αγ-dimers retain ~36% of heterotetramer specific activity while αβ-dimers retain only ~16%.** Thus, when IDH3B is lost, catalytically competent αγ-dimers persist and buffer the enzymatic deficit. The abstract notes: *"Isocitrate dehydrogenase (IDH) is an enzyme required for the production of α-ketoglutarate from isocitrate."*

2. **Yang/Chen et al. 2022 (*J Biol Chem*)** ([PMID: 35985423](https://pubmed.ncbi.nlm.nih.gov/35985423/)) generated global *Idh3b*-knockout mice, which are IDH3-activity deficient and accumulate isocitrate (especially in testis). These mice show **male infertility from spermiogenesis arrest** (defective acrosome and flagellum biogenesis) but **not retinal degeneration**. The paper is titled *"Isocitrate dehydrogenase 3b is required for spermiogenesis but dispensable for retinal viability."*

The species difference (mouse retina tolerant, human retina vulnerable) is an important caveat for preclinical work, but the biochemical explanation — αγ-dimer buffering — is consistent across both studies and directly rationalizes the genotype–phenotype gradient seen in patients. Evidence type: **model organism + in vitro enzymology**.

### Finding 5 — Specific pathogenic variants and extreme rarity

Hartong et al. 2008 identified two homozygous *IDH3B* variants in two consanguineous (first-cousin) families:

| Family | Variant (cDNA) | Protein | Type | OMIM allele |
|--------|---------------|---------|------|-------------|
| 6897 | c.589delA | p.Ile197fs | Frameshift (null, triggers NMD) | 604526.0001 |
| E067 | — | p.Leu98Pro (L98P) | Missense | 604526.0002 |

Screening **261 recessive-RP and 285 simplex-RP probands (~546 total)** yielded only these two families; the variants were absent from 95 controls. This places the contribution of *IDH3B* at roughly **0.4% of screened RP**, making it one of the rarest known RP genes. The abstract confirms: *"Affected family members were homozygous for loss-of-function mutations in IDH3B."* A later report (Zenteno et al. 2020) identified a third pathogenic allele. Evidence type: **human genetics / cohort screening**.

### Finding 6 — Late-onset phenotype with ~4.8% residual activity, and a third variant (p.Gly286Glu)

Genotype–phenotype comparison across the IDH3-opathy spectrum shows that **IDH3A-mutation patients present with early-onset retinal degeneration (ages ~1–11 years)**, whereas **IDH3B-mutation patients present late (~30–50 years)** — consistent with the milder biochemical consequence of β-subunit loss and the αγ-dimer buffering described above. In Hartong 2008, homozygous patient cell lysates retained only ~4.8% of normal NAD-IDH activity (heterozygotes ~24%); the c.589delA frameshift triggers nonsense-mediated decay and is functionally null. A third pathogenic variant, **c.857G>A / p.Gly286Glu (G286E)**, was found homozygous in a Mexican RP proband (patient 3868) by **Zenteno et al. 2020** ([PMID: 31736247](https://pubmed.ncbi.nlm.nih.gov/31736247/)), whose abstract states: *"Novel deleterious variants in IDH3B and ARL6 were identified, supporting their involvement in RD."* Evidence type: **human clinical + biochemistry**.

---

## Section-by-Section Report

### 1. Disease Information

IDH3B-related retinopathy is a **rare, nonsyndromic, autosomal-recessive retinitis pigmentosa** — a progressive rod–cone dystrophy — caused by biallelic loss-of-function variants in *IDH3B*. Rods (night and peripheral vision) degenerate before cones (central and color vision), producing the classic RP course of nyctalopia → peripheral/midperipheral field loss → eventual central involvement.

**Key identifiers:**
- **MONDO:** MONDO:0800393
- **OMIM phenotype:** #612572 (Retinitis pigmentosa 46, RP46)
- **OMIM gene:** *604526 (*IDH3B*)
- **Gene / HGNC:** *IDH3B*, HGNC:4521; chromosome 20p13
- **ICD-11:** 9B70.0 (Retinitis pigmentosa) — not disease-gene-specific
- **ICD-10:** H35.52 (Pigmentary retinal dystrophy)
- **MeSH:** D012174 (Retinitis Pigmentosa) — no gene-specific descriptor
- **Orphanet:** subsumed under non-syndromic RP (ORPHA:791); no RP46-specific code

**Synonyms:** Retinitis pigmentosa 46; RP46; IDH3B-related retinitis pigmentosa.

**Source of information:** Derived from **aggregated disease-level resources** (OMIM, published case reports/cohort genetic studies) rather than large EHR datasets — reflecting the disease's extreme rarity (a handful of reported families worldwide).

### 2. Etiology

**Primary cause — genetic.** The disease is monogenic and Mendelian: biallelic (homozygous or compound-heterozygous) loss-of-function variants in *IDH3B*. There is no known environmental, infectious, or multifactorial cause.

**Genetic risk factors:** The causal variants are the risk factors themselves — loss-of-function *IDH3B* alleles (frameshift p.Ile197fs; missense p.Leu98Pro, p.Gly286Glu). **Consanguinity** is a strong contributing factor: both original families were first-cousin unions, and homozygosity by descent is the predominant route to disease given the rarity of each allele. No modifier genes are established in humans, though the *IDH3A*/*IDH3G* paralogs and residual αγ-dimer activity biologically modulate severity.

**Environmental risk factors:** None established specific to this disease. General RP aggravators (e.g., high-dose vitamin A considerations, light exposure) are discussed in RP broadly but not validated for *IDH3B*.

**Protective factors:** No genetic or environmental protective factors are documented. Biologically, **residual NAD-IDH activity from αγ-dimers and from NADP-IDH (IDH2) compensation in non-retinal tissues** acts as an intrinsic "protective" buffer that confines disease to the retina and delays onset — but this is a mechanistic feature, not a modifiable protective exposure.

**Gene–environment interactions:** None documented.

### 3. Phenotypes

The phenotype is that of **typical, nonsyndromic retinitis pigmentosa**, with notably **late/adult onset** in the IDH3B form.

| Phenotype | Type | HPO term | Onset / severity / course | Frequency |
|-----------|------|----------|---------------------------|-----------|
| Night blindness (nyctalopia) | Symptom | HP:0000662 | Typically earliest symptom; adult-onset in IDH3B; progressive | Characteristic / near-universal in RP |
| Constricted visual fields | Clinical sign | HP:0001133 | Midperipheral loss → tunnel vision; progressive | Characteristic |
| Progressive rod–cone dystrophy | Clinical sign | HP:0007769 | Rods before cones; slowly progressive | Defining feature |
| Bone-spicule retinal pigmentation | Fundus manifestation | HP:0007737 | Mid-to-late disease; progressive | Characteristic |
| Retinal arteriolar attenuation | Clinical sign | HP:0007843 | Progressive | Common in RP |
| Waxy optic disc pallor | Clinical sign | HP:0001104 | Later disease | Common in RP |
| Reduced/extinguished ERG (rod > cone) | Electrophysiology | HP:0000512 | Early, often precedes symptoms | Characteristic |
| Reduced visual acuity | Symptom | HP:0000572 | Later, when macula/cones involved | Variable |
| Abnormal dark adaptation | Functional/lab | HP:0000608 | Early | Characteristic |

**Phenotype characteristics:** Age of onset is **adult (~30–50 years)**, distinctly later than IDH3A-RP (childhood, 1–11 yr). Severity is **moderate** and the course is **slowly progressive**. Because reported cases are few, exact frequencies per phenotype are not quantified for IDH3B specifically; the features listed are those of the RP syndrome with which patients presented.

**Quality-of-life impact:** Progressive peripheral then central visual loss impairs mobility, night-time function, driving, reading, and can cause legal blindness in later decades — but the late onset relative to IDH3A disease means useful central vision is often retained into mid-adult life. No IDH3B-specific QoL instrument data (EQ-5D/SF-36/PROMIS) exist; impact is inferred from the general RP literature.

### 4. Genetic / Molecular Information

**Causal gene:** *IDH3B* (HGNC:4521; OMIM *604526; NCBI Gene 3420; Ensembl ENSG00000101365), chromosome 20p13. It encodes the **β-subunit** of mitochondrial NAD⁺-specific isocitrate dehydrogenase (IDH3). UniProt: O43837 (IDH3B_HUMAN).

**Pathogenic variants (all reported alleles):**

| Variant | Protein | Class | Consequence | Classification |
|---------|---------|-------|-------------|----------------|
| c.589delA | p.Ile197fs | Frameshift | Null; NMD of transcript | Pathogenic |
| c.293T>C (approx.) | p.Leu98Pro | Missense | Loss of function | Pathogenic/Likely pathogenic |
| c.857G>A | p.Gly286Glu | Missense | Loss of function | Pathogenic/Likely pathogenic |

**Variant classification:** All reported alleles act by **loss of function** (not gain-of-function; contrast with somatic neomorphic *IDH1/IDH2* R132/R172 mutations in cancer, which are mechanistically unrelated). Per ACMG/AMP framing, the frameshift is a null (PVS1-type); the missense alleles are supported by segregation in consanguineous families, absence in controls, and functional enzymatic data.

**Allele frequency:** Extremely rare; the alleles were absent from 95 controls in the discovery study and are not appreciable in gnomAD. Each is essentially private to the reported families/populations.

**Somatic vs germline:** **Germline** in all cases. *IDH3B* is not an oncogene and has no role in somatic/oncogenic processes.

**Functional consequence:** Loss of the β-subunit impairs assembly and catalytic output of the IDH3 holoenzyme, reducing NAD-IDH activity to ~5% of normal with a ~300-fold increase in Km for NAD.

**Modifier genes:** None proven in humans. The paralogous subunit genes *IDH3A* and *IDH3G*, and the compensating enzyme *IDH2* (NADP-IDH), are biological modulators of the phenotype's tissue specificity and severity.

**Epigenetic information / chromosomal abnormalities:** None reported or implicated.

### 5. Environmental Information

No environmental, lifestyle, or infectious factors are known to cause or trigger IDH3B-related retinopathy. It is a purely Mendelian, monogenic disorder. General RP considerations (light exposure, vitamin A/DHA supplementation debates) are not validated for this specific genotype.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic loss-of-function variants in *IDH3B*** (frameshift p.Ile197fs or missense p.Leu98Pro/p.Gly286Glu) **lead to** absence or dysfunction of the IDH3 β-subunit protein (frameshift transcript degraded by NMD). *[demonstrated — human genetics]*
2. Loss of the β-subunit **results in** impaired assembly/catalysis of the IDH3 (αβαγ)₂ heterotetramer; some catalytically competent **αγ-dimers persist** (branch: residual activity). *[demonstrated in vitro — αγ retains ~36%, αβ ~16% of holoenzyme activity]*
3. Impaired holoenzyme **leads to** a severe reduction of **NAD⁺-specific isocitrate dehydrogenase activity (~5% residual; ~300-fold ↑ Km for NAD)**, while NADP-IDH/IDH2 activity is preserved. *[demonstrated — patient-cell biochemistry]*
4. In most tissues, **NADP-IDH (IDH2) compensates** for the oxidative decarboxylation of isocitrate → α-ketoglutarate, so no systemic disease occurs (branch explains tissue specificity and the infertility-only mouse phenotype). *[inferred from normal IDH2 activity + absence of extra-ocular disease]*
5. In the **retina**, which has a particular requirement for NAD-IDH, the deficit **results in** a TCA-cycle/α-ketoglutarate and mitochondrial-energy shortfall that compensation cannot cover. *[demonstrated requirement; exact flux consequence inferred]*
6. The energy/metabolic shortfall **leads to** chronic bioenergetic stress in the extraordinarily energy-demanding, mitochondria-rich **photoreceptors** (especially the inner segment). *[inferred — supported by photoreceptor-metabolism literature and the Idh3a mouse respiration defect]*
7. Chronic stress **results in** progressive **photoreceptor cell death (rods before cones)**. *[inferred from RP pathology]*
8. Photoreceptor loss **leads to** the clinical phenotype: nyctalopia → peripheral field constriction → bone-spicule pigmentation, attenuated vessels, reduced ERG → eventual central vision loss. *[demonstrated — clinical]*

**Molecular pathways:** TCA / Krebs cycle (KEGG hsa00020); oxidative decarboxylation of isocitrate to α-ketoglutarate; mitochondrial oxidative phosphorylation downstream. **CHEBI:** isocitrate (CHEBI:16087), α-ketoglutarate/2-oxoglutarate (CHEBI:16810), NAD⁺ (CHEBI:15846).

**Cellular processes / GO terms:** isocitrate metabolic process (GO:0006102); tricarboxylic acid cycle (GO:0006099); NAD metabolism; generation of precursor metabolites and energy (GO:0006091); neuron/photoreceptor apoptotic process (GO:0043524) downstream.

**Protein dysfunction:** Loss of a structural/regulatory subunit → failure of heterotetramer assembly and allosteric activation → catalytic insufficiency (loss of function). Structural studies of human IDH3 clarify the (αβαγ)₂ architecture and allosteric activation mechanism ([PMID: 36375638](https://pubmed.ncbi.nlm.nih.gov/36375638/); [PMID: 37542909](https://pubmed.ncbi.nlm.nih.gov/37542909/)).

**Metabolic changes:** Reduced NAD-IDH flux; isocitrate accumulation (demonstrated in *Idh3b*-KO mouse tissues); diminished α-ketoglutarate production. Photoreceptors rely heavily on aerobic glycolysis but also on mitochondrial OXPHOS of pyruvate and fatty acids; disruption of TCA-cycle enzymes reprograms retinal metabolism and causes degeneration, as shown for the related enzyme PDHA1 ([PMID: 41780638](https://pubmed.ncbi.nlm.nih.gov/41780638/)).

**Immune involvement / epigenetics:** None implicated — this is a primary metabolic/energetic degeneration, not inflammatory or autoimmune, though reactive gliosis accompanies photoreceptor loss as in all RP.

**Tissue damage mechanism:** Chronic mitochondrial bioenergetic insufficiency / metabolic stress in photoreceptors → progressive apoptotic degeneration.

**Upstream vs downstream:** Upstream = *IDH3B* mutation → enzyme deficiency (cause). Downstream = retinal energy shortfall → photoreceptor death → vision loss (effect). The tissue-specificity branch (IDH2 compensation) is the key explanatory node.

**Cell types (CL):** photoreceptor cell (CL:0000210); rod cell (CL:0000604); cone cell (CL:0000573).

### 7. Anatomical Structures Affected

- **Organ level:** The **eye**, specifically the **retina** (UBERON:0000966); within it the **neural retina** (UBERON:0003902) and the photoreceptor layer. No secondary organ involvement — the disease is nonsyndromic. Body system: **sensory / visual system** (nervous system).
- **Tissue/cell level:** Neural (photoreceptor) tissue; the **retinal photoreceptor layer** (UBERON:0001789). Target cells: **rod photoreceptors (CL:0000604)** earliest, then **cone photoreceptors (CL:0000573)**; retinal pigment epithelium secondarily involved in the degenerative cascade.
- **Subcellular level:** **Mitochondrion** (GO:0005739), **mitochondrial matrix** (GO:0005759) — the location of the IDH3 holoenzyme; photoreceptor inner segments are mitochondria-dense.
- **Localization / lateralization:** **Bilateral and largely symmetric**, as is typical for inherited retinal dystrophies.

### 8. Temporal Development

- **Onset:** **Adult-onset, ~30–50 years** — a defining distinction from IDH3A-RP (childhood, 1–11 yr). Onset pattern is **insidious/chronic**, usually beginning with night blindness.
- **Progression:** Slow and **progressive**, moving from peripheral to central vision over years to decades. Stages parallel generic RP: early (nyctalopia, ERG changes) → intermediate (field constriction, pigmentary changes) → advanced (central/acuity loss, possible legal blindness in later life).
- **Course pattern:** Chronic, lifelong, progressive (not episodic or relapsing-remitting). No spontaneous remission.
- **Critical periods:** Any future gene- or metabolism-targeted therapy would be most effective while viable photoreceptors remain — i.e., a therapeutic window before advanced degeneration. The comparatively late onset may widen this window relative to IDH3A disease.

### 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive.** Both discovery families were consanguineous (first-cousin), with affected members homozygous by descent.
- **Penetrance:** Presumed high/complete in biallelic individuals, though exact figures are unavailable given tiny case numbers. **Expressivity** appears variable with respect to age of onset.
- **Epidemiology:** **Ultra-rare.** Only ~0.4% of ~546 screened RP probands carried *IDH3B* variants (2 families); a handful of additional families reported since. No reliable prevalence/incidence estimates exist; it is among the rarest RP genes. RP overall affects ~1 in 3,500–4,000 people, so *IDH3B* accounts for a very small fraction of that.
- **Founder effects / geographic distribution:** No established founder allele; reported families are geographically scattered (original families plus a Mexican proband with p.Gly286Glu). Consanguineous populations are over-represented, as expected for a rare recessive disorder.
- **Carrier frequency:** Not reliably estimable; heterozygous carriers are asymptomatic (retain ~24% NAD-IDH activity).
- **Sex ratio:** ~1:1 (autosomal recessive; no sex bias). *Note:* the related X-linked **IDH3G** form (RP34) affects males — a different gene, not to be conflated with IDH3B.
- **Genetic anticipation / germline mosaicism:** Not applicable / not reported.

### 10. Diagnostics

- **Clinical/ophthalmic workup:** Dilated fundus exam (bone-spicule pigmentation, vessel attenuation, waxy disc pallor); **full-field ERG** (reduced/extinguished rod-predominant responses — the key functional test); visual-field perimetry (peripheral constriction); **OCT** (outer retinal/photoreceptor thinning); fundus autofluorescence; dark-adaptometry.
- **Biomarkers/laboratory:** No circulating biomarker. In research settings, reduced NAD-IDH enzymatic activity in patient cells is demonstrable but is not a routine clinical assay.
- **Genetic testing (definitive):** Diagnosis is confirmed by identifying biallelic *IDH3B* variants. Recommended approaches: **retinal dystrophy / RP gene panels** (which include *IDH3A*, *IDH3B*, *IDH3G*), **whole-exome sequencing (WES)**, or **whole-genome sequencing (WGS)**. Because *IDH3B* RP is so rare, panel/WES is preferred over single-gene testing; segregation analysis in consanguineous families and homozygosity mapping aided the original discovery.
- **Clinical criteria / differential diagnosis:** Clinical RP criteria (nyctalopia + characteristic fundus + reduced ERG + progressive field loss). Differentials include the many other nonsyndromic arRP genes (e.g., *EYS*, nonsyndromic *USH2A*) and — importantly for molecular diagnosis — the other IDH3-opathy genes *IDH3A* (childhood onset ± macular pseudocoloboma) and *IDH3G* (X-linked). Syndromic RP mimics (Usher, Bardet–Biedl) are excluded by the absence of extra-ocular features.
- **Screening:** Cascade genetic testing of at-risk relatives once familial variants are known; carrier testing for reproductive planning in consanguineous families.

### 11. Outcome / Prognosis

- **Survival/mortality:** **Normal life expectancy; no mortality.** The disease is confined to the eye with no systemic involvement.
- **Morbidity/function:** The principal burden is **progressive visual disability** — night blindness, field constriction, and potential legal blindness in later decades. Because onset is late relative to IDH3A disease, useful vision is often retained well into adulthood.
- **Complications:** As in general RP — **posterior subcapsular cataract** and **cystoid macular edema** can occur and are treatable; these warrant surveillance.
- **Prognostic factors:** Later onset and higher residual enzyme activity predict milder/slower disease; genotype (missense with residual function vs null frameshift) and the compensatory αγ-dimer activity are the main biological prognostic modifiers.

### 12. Treatment

**There is no disease-specific or curative therapy.** Management mirrors general RP care:

- **Supportive/rehabilitative:** Low-vision aids, orientation and mobility training, occupational support, protective tinted lenses; regular ophthalmic surveillance. **NCIT:** Supportive Care (NCIT:C19236).
- **Complication management:** Cataract surgery when indicated; **carbonic anhydrase inhibitors** (e.g., topical dorzolamide or oral acetazolamide) for cystoid macular edema.
- **Nutritional:** Vitamin A palmitate and DHA have been studied in RP broadly but are not validated for *IDH3B* and carry risks; use is individualized and controversial.
- **Advanced/experimental:** No *IDH3B*-specific gene therapy, RNA therapy, or small molecule exists. Because the disease is a recessive loss-of-function condition affecting a defined gene, it is **conceptually amenable to AAV-mediated gene augmentation** (as pursued for other recessive RP genes), but no program is reported. There are no registered clinical trials specific to IDH3B-RP. General RP interventions under investigation (retinal prosthesis, optogenetics, stem-cell approaches) could in principle apply at end-stage. **NCIT:** Gene Therapy (NCIT:C15262).
- **Pharmacogenomics:** Not applicable.

### 13. Prevention

- **Primary prevention:** Not possible for a Mendelian disorder. **Genetic counseling** for consanguineous families and carrier couples is the principal preventive tool, with options including prenatal diagnosis and **preimplantation genetic testing (PGT)** once familial variants are known.
- **Secondary prevention:** Early molecular diagnosis enables monitoring and timely management of treatable complications (cataract, macular edema) and would enable early enrollment in any future gene therapy.
- **Tertiary prevention:** Low-vision rehabilitation and complication surveillance to preserve function.
- **Counseling:** Autosomal-recessive recurrence risk is 25% for offspring of two carriers; cascade testing of relatives is advised. **NSGC/ACMG** genetic-counseling frameworks apply.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *IDH3B* is conserved across vertebrates. Mouse ortholog *Idh3b* (NCBI Gene 170718); the enzyme IDH3 is deeply conserved.
- **Natural disease:** No naturally occurring *IDH3B* retinopathy is documented in companion animals or wildlife (no OMIA entry for IDH3B retinal disease at time of writing).
- **Comparative biology:** Importantly, **engineered mouse models do NOT recapitulate the human retinopathy.** *Idh3b*-null mice develop **male infertility (spermiogenesis arrest)** rather than retinal degeneration ([PMID: 35985423](https://pubmed.ncbi.nlm.nih.gov/35985423/)), while *Idh3a* mutant mice do degenerate ([PMID: 30478029](https://pubmed.ncbi.nlm.nih.gov/30478029/)). This species/subunit discrepancy is explained by αγ-dimer residual activity and highlights a comparative-pathology divergence between mouse and human retina.
- **Zoonosis / transmission:** Not applicable (non-infectious genetic disease).

### 15. Model Organisms

| Model | Genotype | Phenotype | Recapitulates human RP? | Reference |
|-------|----------|-----------|-------------------------|-----------|
| Mouse (*Idh3a* E229K) | Missense, α-subunit | Age-dependent retinal degeneration; ↓ mitochondrial respiration/reserve | Yes (models IDH3A-RP) | [PMID: 30478029](https://pubmed.ncbi.nlm.nih.gov/30478029/) |
| Mouse (*Idh3b* LOF, Findlay) | β-subunit loss | No retinal degeneration; no GFAP stress; no respiration defect | **No** | [PMID: 30478029](https://pubmed.ncbi.nlm.nih.gov/30478029/) |
| Mouse (*Idh3b* global KO, Yang/Chen) | β-subunit null | Isocitrate accumulation; **male infertility** (spermiogenesis arrest); retina spared | **No** | [PMID: 35985423](https://pubmed.ncbi.nlm.nih.gov/35985423/) |

- **Model types available:** Mouse knockout/knock-in (above). No published zebrafish, *Drosophila*, organoid, or patient-iPSC retinal model specific to *IDH3B* RP is reported, though patient fibroblasts/lymphoblasts were used for the original enzymatic studies (in vitro).
- **Limitations:** The central limitation is that **no existing animal model reproduces the IDH3B retinal phenotype**, because residual αγ-dimer activity buffers the mouse retina. This impedes preclinical therapy testing and means mechanistic inference rests on human genetics/biochemistry plus the *Idh3a* model as a pathway proxy.
- **Applications:** The *Idh3a* model is useful for studying the downstream pathway (mitochondrial respiration, α-ketoglutarate supply, photoreceptor energetics); the *Idh3b* models illuminate subunit-specific biochemistry and the compensation that defines the human disease's mildness.

---

## Mechanistic Model (Synthesis)

```
  IDH3B biallelic LOF variants
  (p.Ile197fs null / p.Leu98Pro / p.Gly286Glu)
            │  demonstrated (human genetics)
            ▼
  Loss of IDH3 β-subunit
  (frameshift mRNA → NMD)
            │
            ▼
  Impaired IDH3 (αβαγ)₂ assembly/catalysis ───► αγ-dimers persist
            │  in vitro                          (~36% activity; buffer)
            ▼
  NAD-IDH activity ↓ to ~5%        NADP-IDH / IDH2 activity PRESERVED
  (~300-fold ↑ Km for NAD)                       │
            │                                     ▼
            │                        Non-retinal tissues compensate
            │                        → NO systemic disease
            ▼                        (mouse: infertility, not retina)
  RETINA: particular requirement for NAD-IDH
  → TCA / α-ketoglutarate & mitochondrial energy shortfall
            │  inferred
            ▼
  Chronic bioenergetic stress in photoreceptors
  (mitochondria-rich inner segments)
            │  inferred
            ▼
  Progressive photoreceptor death (RODS before CONES)
            │
            ▼
  CLINICAL RP46: nyctalopia → field constriction → bone spicules,
  vessel attenuation, ↓ERG → late central vision loss (onset ~30–50 yr)
```

The single most important and best-supported node is the **branch at steps 3–4**: NAD-IDH is crippled but NADP-IDH (IDH2) is spared, so compensation occurs everywhere except the retina. This explains (a) why a ubiquitous TCA enzyme causes eye-only disease, (b) why mice develop infertility rather than retinopathy, and (c) why IDH3B disease is milder/later than IDH3A disease (more residual activity via αγ-dimers).

---

## Evidence Base

| PMID | Title (abbrev.) | Role | Evidence type |
|------|-----------------|------|---------------|
| [18806796](https://pubmed.ncbi.nlm.nih.gov/18806796/) | *Insights from RP into roles of IDH in the Krebs cycle* (Hartong 2008) | **Foundational** — biallelic IDH3B LOF causes RP; 300-fold ↑ Km; retina-specific NAD-IDH requirement; discovery alleles | Human genetics + in vitro biochemistry |
| [28412069](https://pubmed.ncbi.nlm.nih.gov/28412069/) | *Biallelic IDH3A variants cause RP with pseudocoloboma* | Partner subunit IDH3A causes same recessive RP → IDH3-opathy | Human genetics (WES) |
| [40119724](https://pubmed.ncbi.nlm.nih.gov/40119724/) | *IDH3G as candidate for X-linked RP* (2025) | Third subunit IDH3G causes X-linked RP (RP34) → completes IDH3-opathy | Human genetics |
| [30478029](https://pubmed.ncbi.nlm.nih.gov/30478029/) | *Mouse Idh3a vs Idh3b retinal study* (Findlay 2018) | Idh3a mutants degenerate; Idh3b mutants do not; αγ vs αβ dimer activity | Model organism + enzymology |
| [35985423](https://pubmed.ncbi.nlm.nih.gov/35985423/) | *IDH3B required for spermiogenesis, dispensable for retinal viability* | Idh3b-KO mice: infertility, not retinopathy; isocitrate accumulation | Model organism |
| [31736247](https://pubmed.ncbi.nlm.nih.gov/31736247/) | *Genetic heterogeneity of IRD in Mexican patients* (Zenteno 2020) | Third IDH3B variant p.Gly286Glu in a Mexican proband | Human genetics (NGS) |
| [36375638](https://pubmed.ncbi.nlm.nih.gov/36375638/) | *Structures of constitutively active IDH3 mutant* | IDH3 (αβαγ)₂ architecture, allosteric activation, catalysis | Structural biology |
| [37542909](https://pubmed.ncbi.nlm.nih.gov/37542909/) | *Catalysis and regulation of mammalian NAD-IDH* | Confirms subunit composition and mechanism | Review / structural |
| [41780638](https://pubmed.ncbi.nlm.nih.gov/41780638/) | *Photoreceptor Pdha1 deletion induces degeneration* | Supports that mitochondrial TCA/pyruvate metabolism is essential for photoreceptors | Model organism (context) |
| [32094231](https://pubmed.ncbi.nlm.nih.gov/32094231/) · [42263749](https://pubmed.ncbi.nlm.nih.gov/42263749/) | *Photoreceptor metabolism reviews/models* | Context for extreme photoreceptor energy demand underlying retinal vulnerability | Review / computational |

**How the evidence converges:** Human genetics (18806796, 28412069, 40119724, 31736247) establishes that all three IDH3 subunit genes cause RP and identifies the IDH3B alleles. In vitro biochemistry (18806796) quantifies the enzymatic lesion and demonstrates the IDH2-sparing that explains tissue specificity. Mouse models (30478029, 35985423) both refine the mechanism (αγ-dimer buffering) and flag a translational gap (no retinopathy model). Structural work (36375638, 37542909) grounds the loss-of-function interpretation in holoenzyme architecture. Photoreceptor-metabolism literature (41780638, 32094231, 42263749) provides the physiological rationale for why the retina is uniquely vulnerable to a TCA-cycle enzyme deficiency.

---

## Limitations and Knowledge Gaps

1. **Extreme rarity → thin clinical dataset.** Only a few families/probands are reported, so phenotype frequencies, penetrance, expressivity, natural-history curves, and QoL metrics specific to IDH3B are poorly quantified; much is extrapolated from generic RP.
2. **No faithful animal model.** The mouse retina tolerates *Idh3b* loss (developing infertility instead), leaving the downstream retinal cascade (steps 5–7) mechanistically **inferred** rather than directly demonstrated in an IDH3B-specific system.
3. **Downstream mechanism unproven in retina.** The link from α-ketoglutarate/energy shortfall to photoreceptor apoptosis is plausible and consistent with the IDH3A model and broader photoreceptor-metabolism data, but not directly shown for IDH3B human retina.
4. **Allelic series is tiny.** With only three reported pathogenic variants, genotype–phenotype correlation is limited; residual-activity predictions rest largely on in vitro dimer assays.
5. **No therapeutics.** No gene therapy, trial, or biomarker specific to IDH3B exists.
6. **Ontology/identifier sparseness.** The disease lacks dedicated Orphanet/ICD/MeSH codes, folding into generic RP categories, which complicates knowledge-base curation.

---

## Proposed Follow-up Experiments / Actions

1. **Patient-iPSC retinal organoids** carrying IDH3B null and missense alleles — the most promising route to a *human* model that captures the retina-specific vulnerability the mouse lacks; assay NAD-IDH activity, α-ketoglutarate flux, mitochondrial respiration, and photoreceptor survival.
2. **Humanized / retina-sensitized mouse models** — e.g., combine *Idh3b* loss with partial *Idh3g*/αγ-activity reduction or metabolic stress to unmask a retinal phenotype, directly testing the αγ-dimer buffering hypothesis in vivo.
3. **Deep-phenotyping registry** — pool the worldwide IDH3B families (standardized ERG, OCT, perimetry, longitudinal follow-up) to define natural history, onset range, and progression rate precisely.
4. **Metabolomic profiling** of patient cells/organoids (isocitrate, α-ketoglutarate, TCA intermediates) to validate and biomarker-ize the predicted metabolic shortfall.
5. **AAV gene-augmentation proof-of-concept** — because this is a recessive LOF disorder with a small gene, test *IDH3B* replacement in the organoid/sensitized-mouse systems as a preclinical therapy step.
6. **Variant functional calibration** — systematically express reported and hypothetical IDH3B missense variants, measure residual holoenzyme activity, and correlate with onset age to build a predictive ACMG functional assay.
7. **Targeted screening of consanguineous RP cohorts** — to expand the allelic series and clarify population distribution and any founder effects.

---

*Report compiled from autonomous iterative investigation (5 iterations; 6 confirmed findings; 18 papers reviewed). Evidence types are labeled throughout as human clinical/genetic, in vitro biochemistry, model organism, structural, or computational.*


## Artifacts

- [OpenScientist final report](IDH3B-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](IDH3B-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 14 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000662` (1 mention) - the report calls it "Symptom"; HP calls it **Nyctalopia**
- `HP:0001133` (1 mention) - the report calls it "Clinical sign"; HP calls it **Constriction of peripheral visual field**
- `HP:0007769` (1 mention) - the report calls it "Clinical sign"; HP calls it **Peripheral retinal degeneration**
- `HP:0007843` (1 mention) - the report calls it "Clinical sign"; HP calls it **Attenuation of retinal blood vessels**
- `HP:0001104` (1 mention) - the report calls it "Clinical sign"; HP calls it **Macular hypoplasia**
- `HP:0000512` (1 mention) - the report calls it "Electrophysiology"; HP calls it **Abnormal electroretinogram**
- `HP:0000572` (1 mention) - the report calls it "Symptom"; HP calls it **Visual loss**
- `HP:0000608` (1 mention) - the report calls it "Functional/lab"; HP calls it **Macular degeneration**
- `UBERON:0000966` (1 mention) - the report calls it "retina", "Organ level:** The **eye**, specifically the **retina"; UBERON calls it **retina**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0007737` (1 mention) - the report calls it "Fundus manifestation"; HP calls it **Spicular pigmentation of the retina**, and lists "Bone corpuscle fundus pigmentation" among its other names
- `UBERON:0001789` (1 mention) - the report calls it "retinal photoreceptor layer"; UBERON calls it **outer nuclear layer of retina**, and lists "retinal outer nuclear layer" among its other names
- `GO:0005739` (1 mention) - the report calls it "Mitochondrion", "Subcellular level:** **Mitochondrion"; GO calls it **mitochondrion**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0000966` - called "retina", "Organ level:** The **eye**, specifically the **retina"
- `GO:0005739` - called "Mitochondrion", "Subcellular level:** **Mitochondrion"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.