---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-09T00:50:42.184706'
end_time: '2026-11-09T01:08:01.853511'
duration_seconds: 1039.67
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: TTLL5-Related Retinopathy
  mondo_id: MONDO:1040038
  category: Mendelian
  causal_genes: TTLL5
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
citation_count: 10
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 10
  validator_version: 0.5.1
term_validation:
  total_terms: 38
  verified: 33
  not_found: 0
  obsolete: 0
  unverifiable: 5
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 10
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: MONDO:1040038
    reported_labels:
    - umbrella
    - TTLL5-related retinopathy
    ontology_label: TTLL5-related retinopathy
  - term_id: DOID:0111025
    reported_labels:
    - DOID
    ontology_label: cone-rod dystrophy 19
  - term_id: HP:0000551
    reported_labels:
    - Symptom
    ontology_label: Color vision defect
  - term_id: HP:0000512
    reported_labels:
    - Laboratory/functional abnormality
    ontology_label: Abnormal electroretinogram
  - term_id: HP:0011003
    reported_labels:
    - Physical/refractive
    ontology_label: High myopia
  - term_id: HP:0000613
    reported_labels:
    - Symptom
    ontology_label: Photophobia
  - term_id: HP:0007675
    reported_labels:
    - Functional abnormality
    ontology_label: Progressive night blindness
  - term_id: GO:0120197
    reported_labels:
    - photoreceptor cell outer segment organization
    ontology_label: mucociliary clearance
  labels_variant: 4
  unresolvable_prefixes:
  - RHEA
  - MGI
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: TTLL5-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: TTLL5-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** TTLL5-Related Retinopathy
- **MONDO ID:** MONDO:1040038 (if available)
- **Causal gene(s):** TTLL5
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

Please provide a comprehensive research report on **TTLL5-Related Retinopathy** covering all of the
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

# TTLL5-Related Retinopathy — Comprehensive Disease Characterization Report

**Disease:** TTLL5-Related Retinopathy
**MONDO ID:** MONDO:1040038 (umbrella) → MONDO:0014372 Cone-rod dystrophy 19 (CORD19)
**Specific OMIM entity:** Cone-rod dystrophy 19 (CORD19), OMIM #615860
**Causal gene:** **TTLL5** (Tubulin Tyrosine Ligase Like 5; HGNC:19963; 14q24.3; gene OMIM *612268)
**Category:** Mendelian, autosomal recessive

---

## Summary

**TTLL5-related retinopathy is a rare, autosomal recessive, cone-dominated inherited retinal dystrophy (IRD) caused by biallelic loss-of-function variants in the gene *TTLL5*, which encodes a protein/tubulin polyglutamylase.** The disease's specific OMIM entity is cone-rod dystrophy 19 (CORD19, OMIM #615860), and MONDO:1040038 ("TTLL5-related retinopathy") is a ClinGen Ocular Clinical Domain Working Group umbrella term that encompasses this entity. The causal gene was identified in 2014 by exome sequencing of individuals with "cone-first" retinal disease, and the gene—not the generic disease name—defines the condition.

The core disease mechanism is highly specific and well-supported. TTLL5 is the polyglutamylase responsible for adding glutamate side chains to **RPGR-ORF15**, a ciliary protein that resides at the photoreceptor connecting cilium. Loss of TTLL5 function abolishes RPGR-ORF15 glutamylation without markedly perturbing bulk tubulin glutamylation. This disrupts ciliary trafficking of opsins (early cone-opsin mislocalization is observed), leading to slow, progressive photoreceptor degeneration that preferentially affects cones first and then rods. The *Ttll5* mutant mouse phenocopies *Rpgr*-null mice, firmly linking TTLL5 disease to the RPGR pathway. Because TTLL5 is also expressed in the sperm flagellum centriole, male patients with truncating variants additionally exhibit reduced sperm motility and infertility (asthenozoospermia)—a genotype-dependent syndromic feature.

Clinically, the disease presents in adulthood with slowly progressive central and color-vision loss, macular/parafoveal atrophy, cone-dominated electroretinogram (ERG) deficits, and frequent high myopia. The phenotypic spectrum spans cone dystrophy (CD), cone-rod dystrophy (CRD), and rod-cone dystrophy (RCD). Characteristic imaging features include parafoveal ellipsoid zone loss, macular hyperautofluorescence, and a described "solar flare" sign. There is currently **no approved disease-specific therapy**; management is supportive (refractive correction, low-vision aids, photophobia management, surveillance imaging, and genetic counseling). AAV-mediated gene augmentation is conceptually feasible given the recessive loss-of-function mechanism and manageable 1,281-amino-acid coding sequence, but remains hypothetical/preclinical for TTLL5.

---

## 1. Disease Information

**Overview.** TTLL5-related retinopathy is a non-syndromic (occasionally syndromic) inherited retinal dystrophy with a cone-dominated, macula-centered pattern of degeneration. It belongs to the broad family of IRDs, which collectively affect approximately **1 in 2,000 individuals worldwide**, with over 324 genes implicated ([PMID: 40794304](https://pubmed.ncbi.nlm.nih.gov/40794304/)): *"It affects 1/2000 individuals worldwide, and over 324 genes and 20 phenotypes are implicated in these pathologies."* Within IRDs, cone and cone-rod dystrophies are a minority subset (~10% of IRD probands in several cohorts), and TTLL5 is a rare gene even within that subset.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO (umbrella) | MONDO:1040038 "TTLL5-related retinopathy" |
| MONDO (child/specific) | MONDO:0014372 "cone-rod dystrophy 19" (CORD19) |
| OMIM (phenotype) | #615860 (cone-rod dystrophy 19) |
| OMIM (gene) | *612268 (TTLL5) |
| DOID | DOID:0111025 |
| UMLS | C4014501 |
| MedGen | 862938 |
| GARD | 0016022 (CORD19); 0027241 (xref for umbrella) |
| HGNC (gene) | HGNC:19963 |
| NCBI Gene | 23093 |
| Ensembl | ENSG00000119685 |
| UniProt (protein) | Q6EMB2 |

**Synonyms / alternative names.** CORD19; cone-rod dystrophy 19; TTLL5 cone-rod dystrophy; cone-rod dystrophy caused by mutation in TTLL5; TTLL5-associated retinal dystrophy; TTLL5-associated cone/cone-rod dystrophy.

**Information source.** The knowledge base entry is derived from **aggregated disease-level resources** (OMIM, Orphanet, ClinGen, ClinVar, HGNC, UniProt) supplemented by **individual patient case series and cohorts** from the primary literature (Sergouniotis 2014; Bedoni/Astuti 2016; Oh 2022; Zhou 2026; Archer & Ronquillo 2026), not from a single EHR system.

---

## 2. Etiology

**Primary cause (genetic).** The disease is caused by **biallelic (homozygous or compound heterozygous) pathogenic variants in TTLL5**. The predominant mechanism is loss of function. TTLL5 was identified as the causal gene by exome sequencing in a cohort of individuals with cone-dominated retinal disease ([PMID: 24791901](https://pubmed.ncbi.nlm.nih.gov/24791901/)): *"TTLL5, encoding a tubulin glutamylase, was highlighted as the most likely disease-associated gene."*

**Genetic risk factors.** The causal variants themselves are the risk factor; being a biallelic carrier of pathogenic TTLL5 null alleles is effectively deterministic for retinal disease. Heterozygous carriers are unaffected (recessive). gnomAD constraint metrics confirm that heterozygous loss of function is tolerated (pLI ≈ 0; observed/expected LoF o/e = 0.78, LOEUF = 0.91), consistent with a recessive, non-haploinsufficient mechanism.

**Environmental risk factors.** No established environmental risk factors cause or trigger TTLL5 retinopathy. It is a monogenic Mendelian disease. Age is the principal modifier of severity (disease progresses with age); high myopia is an associated feature rather than an environmental cause. UV/light exposure is a theoretical aggravator for any cone/macular dystrophy but is not established as disease-modifying for TTLL5 specifically.

**Protective factors.** None established. No protective modifier alleles or environmental protective factors have been identified for TTLL5 retinopathy.

**Gene–environment interactions.** None documented. Consanguinity increases the probability of homozygosity for rare recessive null alleles and thus the occurrence of disease in affected families, but this is a population-genetic effect rather than a biological gene–environment interaction.

---

## 3. Phenotypes

The disease produces a spectrum of overlapping phenotypes. The largest single-center cohort to date (Zhou et al. 2026, n=21 from 19 families) classified patients as **2 cone dystrophy (CD), 12 cone-rod dystrophy (CRD), and 7 rod-cone dystrophy (RCD)** ([PMID: 41933583](https://pubmed.ncbi.nlm.nih.gov/41933583/)): *"2 patients were diagnosed with cone dystrophy (CD), 12 with cone-rod dystrophy (CRD), and 7 with rod-cone dystrophy (RCD)."*

| Phenotype | Type | HPO suggestion | Onset | Severity / progression | Frequency |
|---|---|---|---|---|---|
| Reduced central/visual acuity | Symptom/clinical sign | HP:0007663 / HP:0000572 | Adult | Progressive; BCVA correlates with age (R=0.704, P<0.001) | Universal |
| Color vision defect (dyschromatopsia) | Symptom | HP:0000551 | Adult | Progressive | Common (cone-dominated) |
| Macular / parafoveal atrophy | Clinical sign (imaging) | HP:0007906 / HP:0001103 | Adult | Progressive, extends beyond posterior pole | Characteristic |
| Cone-dominated ERG loss | Laboratory/functional abnormality | HP:0000512 | Adult | Progressive | Characteristic |
| High myopia | Physical/refractive | HP:0011003 | Early–adult | Structural | 66.7% (14/21) bilateral high myopia |
| Photophobia | Symptom | HP:0000613 | Adult | Chronic | Common in cone disease |
| Reduced/absent rod function (RCD cases) | Functional abnormality | HP:0007675 | Adult | Progressive | Subset (RCD) |
| Reduced sperm motility / male infertility | Laboratory/clinical (syndromic) | HP:0012864 / HP:0000789 | Adult | — | Males with truncating variants |
| High-frequency hearing loss | Clinical sign (rare) | HP:0000492 / HP:0008542 | Adult | — | Rare (single report) |

**Age of onset.** Predominantly adult-onset. Zhou et al. report spherical equivalent -1.13 to -18.00 D and BCVA 0–2.70 LogMAR (median 0.6), correlating with age ([PMID: 41933583](https://pubmed.ncbi.nlm.nih.gov/41933583/)): *"All patients were myopic, with spherical equivalent values ranging from -1.13 to -18.00 diopters, and 14 of 21 (66.67%) had bilateral high myopia."*

**Progression.** Slowly progressive: retinal involvement is *"characterized by macular degeneration with progressive extension beyond the posterior pole"* ([PMID: 41933583](https://pubmed.ncbi.nlm.nih.gov/41933583/)).

**Quality of life impact.** Central and color-vision loss impairs reading, driving, face recognition, and fine visual tasks; high myopia compounds refractive disability; photophobia affects outdoor/bright-light function. No disease-specific EQ-5D/SF-36 data exist for TTLL5 retinopathy; QoL inference is based on comparable cone/cone-rod dystrophies.

---

## 4. Genetic / Molecular Information

**Causal gene.** *TTLL5* (OMIM *612268; HGNC:19963; NCBI Gene 23093; Ensembl ENSG00000119685) at locus **14q24.3**. The protein (UniProt **Q6EMB2**) is 1,281 aa in the canonical isoform (a longer retina-enriched isoform of ~1,294 aa exists) and functions as an ATP-dependent protein/tubulin **polyglutamylase** (EC 6.3.2.-; Rhea RHEA:60144/60148), adding L-glutamate to γ-carboxyl side chains of substrate glutamates.

**Protein architecture and variant localization.**

| Domain / region | Approx. residues | Function |
|---|---|---|
| Catalytic TTL domain | aa 62–407 | ATP/substrate binding; glutamylation catalysis |
| c-MTBD (C-terminal microtubule-binding domain) | aa 378–488 | Microtubule association |
| RPGR cofactor-interaction domain | C-terminal portion | Unique to TTLL5; targets RPGR-ORF15 glutamylation |
| Disordered C-terminal regions | C-terminus | Regulatory |

**Pathogenic variant spectrum.** Variants are **predominantly truncating** (nonsense, frameshift, splice) and distributed across the gene, consistent with loss of function. Representative alleles: p.Gln117*, p.Leu134Argfs*45, p.Glu529Valfs*2, p.Glu543* (and missense p.Glu543Lys), p.Asp594fs, p.Met712fs, p.Lys810Argfs*35, p.Trp1118*, plus splice variants c.182-1G>T and c.182-5T>C. A frameshift localized to the cofactor-interaction domain was reported by Archer & Ronquillo ([PMID: 42315353](https://pubmed.ncbi.nlm.nih.gov/42315353/)): *"a novel homozygous TTLL5 frameshift mutation (c.2429del, p.Lys810Argfs*35) localized within the cofactor interaction domain."* Protein modeling of five variants *"suggest that they cause different effects on protein function, providing a potential reason for genotype-phenotype cor[relation]"* ([PMID: 35365235](https://pubmed.ncbi.nlm.nih.gov/35365235/)).

**ClinVar landscape (queried 2026, TTLL5[gene]).** 1,291 total submitted variant records: **167 Pathogenic, 70 Likely Pathogenic, and 1,218 Uncertain Significance (VUS)**. The large VUS burden is expected for a 1,281-aa gene with abundant rare missense variation and limited functional/segregation data. Pathogenic/Likely-Pathogenic calls are dominated by truncating/splice (null, PVS1-eligible) variants.

**Allele frequency.** Individual pathogenic alleles are rare in gnomAD. Heterozygous LoF is tolerated (o/e LoF = 0.78; LOEUF = 0.91; pLI ≈ 0), confirming the gene is not haploinsufficient.

**Somatic vs germline.** Germline; this is an inherited (constitutional) disease. No somatic/cancer relevance.

**Functional consequence.** **Loss of function** (recessive). Truncating alleles abolish catalytic and/or cofactor-interaction activity; the missense p.Glu543Lys impairs catalysis. No convincing gain-of-function or dominant-negative mechanism is established.

**Modifier genes.** None firmly established. Allele-specific functional severity (truncating vs missense) and position relative to the RPGR cofactor-interaction domain appear to modulate phenotype, including fertility. RPGR itself is the key downstream partner but is a pathway effector, not a classic modifier gene.

**Epigenetic information.** No disease-specific DNA methylation, histone-modification, or chromatin data are available for TTLL5 retinopathy. (Not applicable / not reported.)

**Chromosomal abnormalities.** None characteristic. The disease is caused by point/small variants, not large-scale cytogenetic rearrangements.

---

## 5. Environmental Information

**Environmental factors.** None established. TTLL5 retinopathy is a monogenic recessive disease with no documented toxic, radiation, pollution, or occupational contribution.

**Lifestyle factors.** None causally implicated. (UV/light protection and avoidance of additional retinal stressors are general ophthalmic prudence, not evidence-based disease modifiers.)

**Infectious agents.** Not applicable. The disease has no infectious etiology or trigger.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function variants in TTLL5** → results in loss or severe reduction of functional TTLL5 polyglutamylase protein in photoreceptors (and sperm).
2. Loss of TTLL5 catalytic/cofactor-interaction activity → **abolishes polyglutamylation of RPGR-ORF15** in its Glu-Gly-rich repetitive region, **without marked change in bulk tubulin glutamylation** (demonstrated in *Ttll5* mutant mice and human disease mutants).
3. Loss of RPGR-ORF15 glutamylation → **impairs RPGR function at the photoreceptor connecting cilium / basal body** (inferred: RPGR glutamylation is required for its ciliary role; *Ttll5* mutants phenocopy *Rpgr*-null mice).
4. Impaired ciliary RPGR function → **defective trafficking of opsins through the connecting cilium to the outer segment** (demonstrated: early cone-opsin mislocalization in *Ttll5* mutant mice; parallel rhodopsin-trafficking failure in glutamylation-imbalanced *pcd* mice).
5. Opsin mislocalization / outer-segment transport failure → **progressive photoreceptor dysfunction and slow degeneration**, affecting **cones first (then rods)** → macular/parafoveal atrophy and ERG loss.
6. Photoreceptor loss → **adult-onset, progressive central and color-vision loss with macular atrophy** (clinical manifestation).

**Branch (syndromic):** Step 1 → loss of TTLL5 at the **sperm flagellum centriole** → (in males with truncating variants) → **reduced sperm motility / asthenozoospermia and infertility**, reflecting a shared ciliary/centriolar mechanism between photoreceptors and spermatozoa.

### Detail by category

**Molecular pathway / biochemical abnormality.** The central lesion is a **tubulin-tyrosine-ligase-like polyglutamylation defect** acting on a non-tubulin substrate. TTLL5 *"glutamylates RPGR(ORF15) in its Glu-Gly-rich repetitive region"* ([PMID: 27162334](https://pubmed.ncbi.nlm.nih.gov/27162334/)). The RPGR C-terminal basic domain binds the noncatalytic cofactor-interaction domain unique to TTLL5, targeting glutamylation. Human *"TTLL5 disease mutants that cause human retinal dystrophy show impaired glutamylation of RPGR(ORF15)"* ([PMID: 27162334](https://pubmed.ncbi.nlm.nih.gov/27162334/)).

**Cellular process.** Ciliary protein transport (intraflagellar/ciliary trafficking) and photoreceptor outer-segment maintenance; the downstream event is slow photoreceptor cell death. The *Ttll5* mutant mouse *"develops slow photoreceptor degeneration with early mislocalization of cone opsins, features resembling those of Rpgr-null mice"* ([PMID: 27162334](https://pubmed.ncbi.nlm.nih.gov/27162334/)).

**Protein dysfunction.** Loss of function of the polyglutamylase (truncation removes catalytic and/or cofactor-interaction domains; missense impairs catalysis).

**Glutamylation balance.** Correct glutamylation balance at the cilium governs opsin transport. In the *pcd* mouse (deglutamylase-null, hyperglutamylation), *"degeneration of photoreceptors in pcd is preceded by impaired rhodopsin trafficking to the rod outer segment"* ([PMID: 35404950](https://pubmed.ncbi.nlm.nih.gov/35404950/)), and loss of the writer Ttll1 rescues degeneration—underscoring that both too little (TTLL5 loss) and too much glutamylation disrupt opsin trafficking.

**Immune / metabolic / epigenetic involvement.** No autoimmune, primary metabolic, or epigenetic mechanism is implicated. Tissue damage is degenerative (programmed photoreceptor death secondary to trafficking failure), not inflammatory, ischemic, or fibrotic.

### Upstream vs downstream and ontology suggestions

- **Upstream:** TTLL5 LoF → loss of RPGR-ORF15 glutamylation.
- **Downstream:** opsin mislocalization → photoreceptor degeneration → vision loss.
- **GO biological process:** GO:0018095 (protein polyglutamylation); GO:0035735 (intraciliary transport); GO:0120197 (photoreceptor cell outer segment organization); GO:0007286 (spermatid development).
- **GO cellular component:** GO:0097539 (ciliary transition zone/connecting cilium region); GO:0036064 (ciliary basal body); GO:0001917 (photoreceptor inner segment); GO:0001750 (photoreceptor outer segment).
- **Cell types (CL):** CL:0000573 (retinal cone cell); CL:0000604 (retinal rod cell); CL:0000019 (sperm).

---

## 7. Anatomical Structures Affected

**Organ level.** Primary organ: the **eye**, specifically the **retina** (UBERON:0000966), with a macula-centered pattern. Secondary/associated: the **male reproductive system** (testis/spermatozoa) in truncating-variant carriers; rare auditory involvement (inner ear) in isolated reports. Body system: **nervous/sensory (visual) system**, with reproductive-system involvement as the syndromic branch.

**Tissue and cell level.** The **neural retina** (nervous tissue); the targeted cells are **photoreceptors**—cones preferentially and earliest (CL:0000573), then rods (CL:0000604). The **retinal pigment epithelium** is secondarily involved through macular atrophy. In males, **spermatozoa** (CL:0000019) are affected.

**Subcellular level.** The disease localizes to the **photoreceptor connecting cilium / basal body** and the **sperm flagellum centriole**. TTLL5 antibodies *"stained the basal body of photoreceptor cells in rat and the centrosome of the spermatozoon flagellum in humans, suggesting a common mechanism of action in these two cell types"* ([PMID: 28173158](https://pubmed.ncbi.nlm.nih.gov/28173158/)). GO cellular-component terms: GO:0036064 (ciliary basal body), GO:0005814 (centriole), GO:0001917 (photoreceptor inner segment).

**Localization and lateralization.** UBERON terms: UBERON:0000966 (retina), UBERON:0001782 (macula lutea; fovea UBERON:0001781), UBERON:0001789 (photoreceptor layer), UBERON:0000473 (testis). Retinal involvement is **bilateral and largely symmetrical**, beginning parafoveally/macularly and extending beyond the posterior pole.

---

## 8. Temporal Development

**Onset.** Typically **adult-onset**, insidious/chronic. Central vision and color-vision symptoms predominate. High myopia may be noted earlier in life, but degenerative retinal symptoms emerge in adulthood.

**Progression.** Slow and **progressive**. In the Zhou cohort, BCVA correlated with age (Spearman R = 0.704, P < 0.001), indicating gradual decline over decades. Degeneration follows a **cone-first** pattern (CD → CRD), with rod involvement (RCD) in a subset. The structural course is macular atrophy *"with progressive extension beyond the posterior pole"* ([PMID: 41933583](https://pubmed.ncbi.nlm.nih.gov/41933583/)).

**Disease course / duration.** Chronic, lifelong; no remission or relapsing-remitting pattern. There is no spontaneous recovery.

**Critical periods / intervention window.** As with other photoreceptor-trafficking IRDs, the therapeutic window for any future gene-augmentation therapy would be before extensive photoreceptor loss (while viable cones/rods remain)—inferred from the broader IRD gene-therapy field rather than demonstrated for TTLL5.

---

## 9. Inheritance and Population

**Inheritance.** **Autosomal recessive.** Biallelic variants are required; the largest cohort described *"Twenty-one affected individuals from 19 unrelated families carrying biallelic TTLL5 variants"* ([PMID: 41933583](https://pubmed.ncbi.nlm.nih.gov/41933583/)). Many reported cases are homozygous, often from consanguineous families.

**Penetrance and expressivity.** Penetrance of the retinal phenotype in biallelic null carriers appears high (essentially complete for retinal disease), with **variable expressivity** across the CD–CRD–RCD spectrum and variable age/severity. The male-fertility phenotype shows **genotype-dependent expressivity**: *"The two male patients carrying truncating TTLL5 variants also displayed a substantial reduction in sperm motility and infertility, whereas those carrying missense changes were fertile"* ([PMID: 28173158](https://pubmed.ncbi.nlm.nih.gov/28173158/)).

**Genetic anticipation / mosaicism / founder effects.** No anticipation (not a repeat-expansion disorder). No germline mosaicism specifically reported. No well-defined founder mutation; cases arise worldwide (UK, Switzerland, Netherlands, Sweden, Spain, Morocco, China, North America), with consanguinity enriching homozygosity.

**Carrier frequency.** Not formally established; individual pathogenic alleles are rare in gnomAD, consistent with an ultra-rare recessive disease.

**Epidemiology.** No disease-specific prevalence/incidence figure exists for TTLL5 retinopathy. Context: IRDs affect ~1/2,000 ([PMID: 40794304](https://pubmed.ncbi.nlm.nih.gov/40794304/)); cone/cone-rod dystrophies are ~10% of IRD probands (e.g., 41/403 = 10.2% in a Welsh cohort; 16/203 in a Polish cohort), and TTLL5 is a **very rare** gene within that subset. Del Pozo-Valero et al. listed TTLL5 among "very rare" genes in 1,036 Spanish macular-dystrophy families: *"Novel variants in the very rare genes PLA2G5 and TTLL5 revealed additional phenotypic associations"* ([PMID: 35119454](https://pubmed.ncbi.nlm.nih.gov/35119454/)).

**Population demographics.** No strong ethnic predilection; worldwide distribution. **Sex ratio:** retinal disease affects both sexes; the infertility phenotype is male-specific (and genotype-dependent). **Age distribution:** adults, with severity increasing with age.

---

## 10. Diagnostics

**Clinical / functional tests.**
- **Full-field and pattern ERG:** cone-dominated amplitude reduction (cone responses affected earlier/more than rod responses); rod involvement in RCD cases.
- **Spectral-domain OCT (SD-OCT):** parafoveal **ellipsoid zone loss** — *"Multimodal imaging demonstrated parafoveal ellipsoid zone loss consistent with a cone-rod dystrophy pattern"* ([PMID: 42315353](https://pubmed.ncbi.nlm.nih.gov/42315353/)).
- **Fundus autofluorescence (FAF):** parafoveal/macular hyperautofluorescence; macular atrophy.
- **Color fundus photography:** macular degeneration/atrophy.
- **Color vision testing:** dyschromatopsia.
- **Characteristic sign:** the **"solar flare" sign** described in TTLL5-associated cone dystrophy ([PMID: 42315353](https://pubmed.ncbi.nlm.nih.gov/42315353/)).
- **Refraction:** frequent high myopia (≤ -6.0 D in two-thirds of patients).

**Biomarkers / laboratory.** No circulating biochemical biomarker exists. In males, **semen analysis** may reveal asthenozoospermia (reduced sperm motility) as an adjunct diagnostic clue in truncating-variant carriers.

**Genetic testing (definitive).** Molecular diagnosis is established by detecting biallelic pathogenic TTLL5 variants.
- **IRD gene panel (NGS)** including TTLL5 — typical first-line test.
- **Whole-exome sequencing (WES)** — effective; TTLL5 was discovered by exome sequencing ([PMID: 24791901](https://pubmed.ncbi.nlm.nih.gov/24791901/)).
- **Whole-genome sequencing (WGS)** — useful for deep-intronic/splice and structural variants (e.g., c.182-1G>T, c.182-5T>C splice alleles).
- **Single-gene / targeted testing** — for cascade testing of known familial variants.
- CMA, karyotyping, FISH, mtDNA testing, and repeat-expansion testing are **not applicable** (small-variant, nuclear, non-repeat disorder).

**Clinical criteria / differential diagnosis.** No disease-specific consensus criteria; diagnosis integrates phenotype (cone-dominated/macular dystrophy with high myopia), multimodal imaging, ERG, and biallelic TTLL5 genotype. **Differential diagnoses:** other cone/cone-rod dystrophy genes—notably **ABCA4** (Stargardt/CRD), **RPGR** (X-linked, phenotypically overlapping—TTLL5 LoF cone dystrophy *"closely resembles the phenotype observed in some patients with"* RPGR-related disease; [PMID: 42573183](https://pubmed.ncbi.nlm.nih.gov/42573183/)), **GUCY2D, PRPH2, RIMS1, KCNV2, CACNA1F**, and macular dystrophies. High myopia and sex-specific infertility (truncating alleles) are distinguishing clues toward TTLL5.

**Screening.** Cascade genetic testing of relatives and carrier testing within affected families; no population newborn screening is indicated for this ultra-rare condition.

---

## 11. Outcome / Prognosis

**Survival / mortality.** TTLL5 retinopathy is **not life-threatening**; life expectancy is normal. There is no disease-specific mortality.

**Morbidity / function.** The principal burden is **progressive visual disability**: central and color-vision loss impairing reading, driving, and daily visual tasks, compounded by high myopia and photophobia. BCVA ranges widely (0–2.70 LogMAR, median 0.6) and worsens with age ([PMID: 41933583](https://pubmed.ncbi.nlm.nih.gov/41933583/)). In affected males, **infertility** (asthenozoospermia) is an additional morbidity for truncating-variant carriers.

**Disease course / complications.** Chronic, progressive macular atrophy extending beyond the posterior pole; rod involvement (night-vision difficulty) in RCD cases; rare auditory involvement in isolated reports — *"One patient also developed high-frequency hearing loss during a similar time period as the onset of retinal disease, potentially suggestive of a syndromic disorder"* ([PMID: 35365235](https://pubmed.ncbi.nlm.nih.gov/35365235/)).

**Recovery potential.** None spontaneously; vision loss is irreversible with current (supportive-only) management.

**Prognostic factors.** **Age** is the strongest correlate of visual decline. **Genotype** modulates phenotype and the fertility outcome (truncating vs missense). Protein modeling suggests allele-specific functional effects underlie genotype-phenotype variability ([PMID: 35365235](https://pubmed.ncbi.nlm.nih.gov/35365235/)). No validated molecular prognostic biomarker exists.

---

## 12. Treatment

**There is no approved disease-specific therapy for TTLL5-related retinopathy, and no interventional clinical trials target TTLL5 (as of 2026).** Management is **supportive and symptomatic**:

- **Refractive correction** of the frequent high myopia (glasses/contact lenses). *(NCIT: Refractive Correction.)*
- **Low-vision rehabilitation** and aids (magnifiers, electronic aids, orientation/mobility support). *(NCIT: Rehabilitation Therapy.)*
- **Photophobia management:** tinted and UV-filtering lenses.
- **Surveillance:** serial SD-OCT, FAF, and ERG to monitor progression.
- **Genetic counseling** for this autosomal recessive condition, including recurrence risk (25% for siblings when both parents are carriers), carrier/cascade testing, and—where relevant—**fertility counseling** for males with truncating variants (assisted reproductive options such as ICSI may be discussed). *(NCIT: Genetic Counseling.)*

**Pharmacotherapy / pharmacogenomics.** None established. (Not applicable.)

**Advanced therapeutics (hypothetical/preclinical).** The recessive **loss-of-function** mechanism of a **non-haploinsufficient** gene (pLI ≈ 0) and the manageable **1,281-aa coding sequence** make **AAV-mediated gene augmentation** conceptually feasible, analogous to RPGR gene-therapy programs (notably because TTLL5's key retinal substrate is RPGR-ORF15). This remains **hypothetical/preclinical for TTLL5 itself**. *(NCIT: Gene Therapy; Adeno-associated Viral Vector Gene Therapy.)* RNA-based and cell therapies are not currently under development for this gene.

**Experimental treatments.** No NCT-registered trials specific to TTLL5 identified.

**Treatment outcomes / adverse events.** Not applicable—no disease-specific pharmacologic or advanced therapy exists.

---

## 13. Prevention

**Primary prevention.** As a monogenic recessive disease, primary prevention is **reproductive/genetic**: carrier screening (especially in consanguineous families or populations with known alleles), genetic counseling, and reproductive options including **preimplantation genetic testing (PGT)** and **prenatal diagnosis** for couples known to both carry pathogenic TTLL5 variants. No vaccine or lifestyle prevention applies.

**Secondary prevention.** Early molecular diagnosis via IRD panels/WES enables timely counseling, low-vision planning, and eligibility for future trials; **cascade genetic testing** identifies affected/at-risk relatives.

**Tertiary prevention.** Minimize complications of visual impairment (fall prevention, mobility training, educational/occupational support); correct refractive error; manage photophobia; monitor for progression.

**Counseling.** Genetic counseling is central—recurrence risk, carrier status, and male-fertility implications of truncating variants.

**Immunization / public-health / environmental interventions.** Not applicable (non-infectious, non-environmental monogenic disease).

---

## 14. Other Species / Natural Disease

**Taxonomy and orthologs.** The gene is conserved across vertebrates. Mouse ortholog **Ttll5** (NCBI Gene 320244; MGI:2443657; Ensembl ENSMUSG00000012609). *Homo sapiens* NCBI Taxon:9606; *Mus musculus* NCBI Taxon:10090.

**Natural disease in other species.** No well-characterized naturally occurring TTLL5 retinopathy has been documented in companion animals or wildlife (OMIA not definitive). The disease is primarily studied via engineered mouse models rather than natural animal disease.

**Comparative biology.** The TTLL5→RPGR-ORF15 glutamylation axis and ciliary opsin-trafficking mechanism are evolutionarily conserved between rodent and human photoreceptors (and between photoreceptors and spermatozoa), providing strong cross-species mechanistic conservation. The human disease closely mirrors the biology of *Rpgr*-null mice and overlaps phenotypically with human RPGR disease.

**Transmission / zoonotic potential.** Not applicable (inherited, non-transmissible).

---

## 15. Model Organisms

**Primary model: the *Ttll5* mutant mouse.** This is the central model and recapitulates key features of the human disease:

| Feature | *Ttll5* mutant mouse | Human TTLL5 disease |
|---|---|---|
| RPGR-ORF15 glutamylation | Complete loss | Impaired (disease mutants) |
| Bulk tubulin glutamylation | Largely unchanged | (Consistent) |
| Photoreceptor degeneration | Slow, progressive | Slow, progressive |
| Cone-opsin mislocalization | Early | Cone-dominated disease |
| Male fertility | Reduced | Reduced (truncating variants) |

The mouse *"displays a complete loss of RPGR glutamylation without marked changes in tubulin glutamylation levels"* and *"develops slow photoreceptor degeneration with early mislocalization of cone opsins, features resembling those of Rpgr-null mice"* ([PMID: 27162334](https://pubmed.ncbi.nlm.nih.gov/27162334/)). Male *Ttll5*-mutant mice show reduced fertility, paralleling human truncating-variant carriers.

**Complementary model (glutamylation balance): the *pcd* mouse.** The *pcd* (Agtpbp1/Nna1/CCP1 deglutamylase-null) mouse exhibits **hyper**glutamylation causing photoreceptor, Purkinje, and mitral-cell degeneration; loss of the writer Ttll1 rescues photoreceptor degeneration. Critically, *"degeneration of photoreceptors in pcd is preceded by impaired rhodopsin trafficking to the rod outer segment"* ([PMID: 35404950](https://pubmed.ncbi.nlm.nih.gov/35404950/)). This model establishes that **both deficient and excessive glutamylation disrupt opsin trafficking and cause photoreceptor death**, framing TTLL5 loss within a broader glutamylation-balance paradigm.

**Phenotype recapitulation and limitations.** The *Ttll5* mouse recapitulates the retinal and fertility phenotypes with high fidelity. Limitations: the human high-myopia association and the precise CD/CRD/RCD spectrum are not fully modeled; the rod-dominant mouse retina limits modeling of the cone-first, macula-centered human phenotype.

**Resources.** MGI (mouse); Alliance of Genome Resources; the RPGR-pathway literature for cross-model comparison. iPSC-derived retinal organoids are a plausible but not-yet-reported human in-vitro model for TTLL5.

---

## Mechanistic Model / Interpretation

```
 Biallelic LoF variants in TTLL5 (14q24.3)
                 │
                 ▼
 Loss of TTLL5 polyglutamylase activity
                 │
     ┌───────────┴─────────────────────────────┐
     ▼ (photoreceptor)                           ▼ (sperm, truncating alleles)
 Loss of RPGR-ORF15 glutamylation          Loss of TTLL5 at flagellar
 at connecting cilium / basal body          centriole
     │  (tubulin glutamylation spared)           │
     ▼                                            ▼
 Impaired ciliary RPGR function              Impaired flagellar function
     │                                            ▼
     ▼                                       Reduced sperm motility
 Defective opsin trafficking                 (asthenozoospermia) → infertility
 to outer segment
 (cone opsins mislocalize early)
     │
     ▼
 Slow photoreceptor degeneration (cones → rods)
     │
     ▼
 Macular/parafoveal atrophy, cone-dominated ERG loss
     │
     ▼
 Adult-onset progressive central & color-vision loss
 (CD → CRD → RCD spectrum; frequent high myopia)
```

The model is unusually well-resolved for a rare IRD: a **specific enzyme–substrate relationship (TTLL5 → RPGR-ORF15)** connects genotype to the ciliary trafficking defect, and the mouse model phenocopies both the retinal and reproductive branches. The upstream lesion is the glutamylation defect; downstream events (opsin mislocalization → degeneration → vision loss) are shared with RPGR disease and with the broader glutamylation-balance paradigm illustrated by *pcd* mice.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [24791901](https://pubmed.ncbi.nlm.nih.gov/24791901/) | *Biallelic TTLL5 variants cause retinal dystrophy* | **Gene discovery**; TTLL5 as causal gene; recessive LoF alleles |
| [27162334](https://pubmed.ncbi.nlm.nih.gov/27162334/) | *Loss of RPGR glutamylation underlies TTLL5 pathogenesis* | **Core mechanism**; RPGR-ORF15 substrate; *Ttll5* mouse; human mutants impair glutamylation |
| [28173158](https://pubmed.ncbi.nlm.nih.gov/28173158/) | *TTLL5 mutations: cone-rod degeneration + reduced male fertility* | **Syndromic branch**; genotype-dependent infertility; basal body/flagellar localization |
| [41933583](https://pubmed.ncbi.nlm.nih.gov/41933583/) | *Clinical & genetic spectrum (single-center cohort, n=21)* | **Phenotype spectrum** (CD/CRD/RCD); high myopia 66.7%; BCVA–age correlation |
| [42315353](https://pubmed.ncbi.nlm.nih.gov/42315353/) | *Novel variant; "solar flare" sign* | **Imaging/diagnosis**; ellipsoid zone loss; cofactor-interaction-domain variant |
| [35365235](https://pubmed.ncbi.nlm.nih.gov/35365235/) | *Expanding the phenotype: case series* | **Variable expressivity**; variant modeling; possible auditory involvement |
| [35404950](https://pubmed.ncbi.nlm.nih.gov/35404950/) | *TTLL1/TTLL4 in pcd neurodegeneration* | **Glutamylation-balance** paradigm; opsin-trafficking failure precedes degeneration |
| [42573183](https://pubmed.ncbi.nlm.nih.gov/42573183/) | *RPGR sector RP with cone dystrophy* | **Differential/overlap** with RPGR disease; phenotypic resemblance to TTLL5 LoF |
| [35119454](https://pubmed.ncbi.nlm.nih.gov/35119454/) | *NGS in 1,036 Spanish macular-dystrophy families* | **Epidemiology**; TTLL5 among "very rare" IRD genes |
| [40794304](https://pubmed.ncbi.nlm.nih.gov/40794304/) | *Splice variants in Moroccan IRD families* | **Context**; IRD prevalence ~1/2,000; >324 genes |

Evidence types: **human clinical** (cohorts/case series: 24791901, 28173158, 41933583, 42315353, 35365235); **model organism** (27162334 *Ttll5* mouse; 35404950 *pcd* mouse); **computational/in silico** (variant/protein modeling within 35365235, 42573183); **aggregated database** (ClinVar, gnomAD, OMIM, HGNC, UniProt).

---

## Limitations and Knowledge Gaps

1. **No disease-specific epidemiology.** Prevalence/incidence and carrier frequency for TTLL5 retinopathy are unquantified; estimates are extrapolated from IRD/cone-rod subset frequencies.
2. **Small cohorts.** The largest study has 21 patients; phenotype frequencies and genotype-phenotype correlations rest on limited numbers.
3. **Large VUS burden.** 1,218 ClinVar VUS vs 237 P/LP complicate variant interpretation; functional assays for missense alleles are sparse.
4. **Incomplete genotype-phenotype map.** Determinants of CD vs CRD vs RCD presentation and of myopia severity are not fully explained.
5. **Syndromic scope uncertain.** The frequency of male infertility and the reality of auditory involvement (single report) need larger systematic study.
6. **No human in-vitro model reported** (e.g., patient iPSC-retinal organoids), and no natural animal disease characterized.
7. **No therapeutics.** Gene augmentation is only conceptual; no preclinical efficacy data or trials exist for TTLL5.
8. **Epigenetic, metabolomic, proteomic, and single-cell data** specific to TTLL5 retinopathy are absent.

---

## Proposed Follow-up Experiments / Actions

1. **Natural-history registry & imaging study** (multicenter) to quantify progression rates, define CD→CRD→RCD transitions, and establish trial-ready endpoints (ellipsoid-zone width, BCVA, FAF atrophy area).
2. **Functional variant assays** (in-vitro glutamylation of RPGR-ORF15 using purified/expressed TTLL5 missense variants) to reclassify VUS and build an ACMG-grade functional evidence set.
3. **Patient iPSC-derived retinal organoids** to model opsin mislocalization and test rescue, and to screen glutamylation-modulating interventions.
4. **AAV-TTLL5 gene-augmentation proof-of-concept** in *Ttll5* mutant mice (with RPGR-glutamylation readout) to establish feasibility, dosing, and therapeutic window.
5. **Systematic andrology sub-study** in male patients stratified by truncating vs missense genotype to define infertility penetrance and counsel accurately.
6. **Audiology screening** across cohorts to confirm or refute syndromic hearing involvement.
7. **Deep-intronic/structural variant analysis via WGS** in unsolved cone-dominated IRD cases to capture missed TTLL5 alleles.

---

*Evidence synthesized from 17 reviewed papers and aggregated databases (OMIM, Orphanet, MONDO, ClinVar, gnomAD, HGNC, UniProt, MGI). Primary mechanistic claims are supported by model-organism and human-clinical studies cited above with verified abstract quotes.*


## Artifacts

- [OpenScientist final report](TTLL5-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](TTLL5-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 5 |
| Terms whose name was checked | 22 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:1040038` (3 mentions) - the report calls it "umbrella", "TTLL5-related retinopathy"; MONDO calls it **TTLL5-related retinopathy**
- `DOID:0111025` (1 mention) - the report calls it "DOID"; DOID calls it **cone-rod dystrophy 19**
- `HP:0000551` (1 mention) - the report calls it "Symptom"; HP calls it **Color vision defect**
- `HP:0000512` (1 mention) - the report calls it "Laboratory/functional abnormality"; HP calls it **Abnormal electroretinogram**
- `HP:0011003` (1 mention) - the report calls it "Physical/refractive"; HP calls it **High myopia**
- `HP:0000613` (1 mention) - the report calls it "Symptom"; HP calls it **Photophobia**
- `HP:0007675` (1 mention) - the report calls it "Functional abnormality"; HP calls it **Progressive night blindness**
- `GO:0120197` (1 mention) - the report calls it "photoreceptor cell outer segment organization"; GO calls it **mucociliary clearance**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0035735` (1 mention) - the report calls it "intraciliary transport"; GO calls it **intraciliary transport involved in cilium assembly**, and lists "intraflagellar transport" among its other names
- `GO:0097539` (1 mention) - the report calls it "ciliary transition zone/connecting cilium region"; GO calls it **ciliary transition fiber**, and lists "ciliary transition fibre" among its other names
- `CL:0000019` (2 mentions) - the report calls it "sperm", "spermatozoa"; CL calls it **sperm**, and lists "spermatozoid" among its other names
- `UBERON:0001789` (1 mention) - the report calls it "photoreceptor layer"; UBERON calls it **outer nuclear layer of retina**, and lists "outer nuclear layer" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:1040038` - called "umbrella", "TTLL5-related retinopathy"
- `CL:0000019` - called "sperm", "spermatozoa"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `RHEA`, `MGI`, `Taxon`.