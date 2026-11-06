---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T17:48:50.146016'
end_time: '2026-10-31T18:07:21.502184'
duration_seconds: 1111.36
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: IMPG1-related Dominant Retinopathy
  mondo_id: MONDO:1040036
  category: Mendelian
  causal_genes: IMPG1
  omim_id: not recorded
  synonyms: autosomal dominant IMPG1 retinopathy; autosomal dominant IMPG1-related
    vitelliform macular dystrophy; autosomal dominant IMPG1-related retinitis pigmentosa;
    benign concentric annular macular dystrophy
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 7
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 7
  off_topic: 1
  off_topic_references:
  - PMID:23470504
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 24
  verified: 22
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 5
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: HP:0011506
    reported_labels:
    - Macular dystrophy
    ontology_label: Choroidal neovascularization
  - term_id: HP:0012508
    reported_labels:
    - Symptom
    - Metamorphopsia
    ontology_label: Metamorphopsia
  - term_id: HP:0000662
    reported_labels:
    - Symptom
    - Nyctalopia
    ontology_label: Nyctalopia
  - term_id: HP:0001133
    reported_labels:
    - Clinical sign
    - Constriction of visual field
    ontology_label: Constriction of peripheral visual field
  - term_id: GO:0005578
    reported_labels:
    - proteinaceous ECM
    ontology_label: GO_0005578
  - term_id: UBERON:0013706
    reported_labels:
    - subretinal space
    ontology_label: bone spine
  labels_variant: 9
  obsolete_terms:
  - term_id: GO:0005578
    ontology_label: GO_0005578
    replaced_by: GO:0031012
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: IMPG1-related_Dominant_Retinopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: IMPG1-related_Dominant_Retinopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** IMPG1-related Dominant Retinopathy
- **MONDO ID:** MONDO:1040036 (if available)
- **Causal gene(s):** IMPG1
- **OMIM:** not recorded
- **Synonyms:** autosomal dominant IMPG1 retinopathy; autosomal dominant IMPG1-related vitelliform macular dystrophy; autosomal dominant IMPG1-related retinitis pigmentosa; benign concentric annular macular dystrophy
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **IMPG1-related Dominant Retinopathy** covering all of the
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

# IMPG1-related Dominant Retinopathy — Comprehensive Disease Characterization Report

**Disease:** IMPG1-related Dominant Retinopathy
**MONDO ID:** MONDO:1040036
**Causal gene:** **IMPG1** (Interphotoreceptor Matrix Proteoglycan 1; encodes the protein **SPACR**), chromosome 6q14.1
**Category:** Mendelian, autosomal dominant (with a recessive allelic counterpart)

> **Gene identity (read first):** This report concerns retinopathy caused by **IMPG1** on chromosome **6q14.1** (HGNC:6054; OMIM gene \*602870; UniProt Q17R60/SPACR). Do **not** confuse it with its paralog **IMPG2** (chromosome 3q12, encoding SPACRCAN), which causes a clinically overlapping but genetically distinct retinopathy. "Dominant retinopathy" here refers to the **monoallelic (autosomal dominant)** IMPG1 phenotype — principally **adult-onset vitelliform macular dystrophy (AVMD/VMD4)** with a related pattern-dystrophy / retinitis-pigmentosa (RP91) spectrum.

---

## Summary

IMPG1-related dominant retinopathy is a rare, adult/late-onset Mendelian inherited retinal dystrophy (IRD) caused by heterozygous variants in **IMPG1**, located on chromosome **6q14.1**. IMPG1 encodes **SPACR** (Sialoprotein Associated with Cones and Rods), a 147–150 kDa hyaluronan-binding glycoprotein that forms the macromolecular scaffold of the **interphotoreceptor matrix (IPM)** — the specialized extracellular matrix filling the subretinal space between photoreceptor outer segments and the retinal pigment epithelium (RPE). Despite the "proteoglycan" in the gene symbol, SPACR is a heavily glycosylated glycoprotein that does **not** carry glycosaminoglycan chains. Its paralog, IMPG2 (SPACRCAN), is the other principal IPM component, and the two proteins are functionally interdependent.

The dominant phenotype is chiefly **adult-onset vitelliform macular dystrophy (AVMD; OMIM VMD4, 616151)**, with an overlapping **retinitis pigmentosa spectrum (OMIM RP91, 617304)** and pattern-dystrophy presentations. The disease was defined as a distinct entity by Meunier and colleagues in 2014, who identified IMPG1 (and IMPG2) as causal in BEST1/PRPH2-negative vitelliform families, with the recurrent dominant missense variant **c.713T>G (p.Leu238Arg)**. A key mechanistic insight from this investigation is that IMPG1 is **loss-of-function tolerant** in the general population (gnomAD pLI ≈ 0; observed/expected LoF ≈ 0.92), arguing strongly that the dominant disease is **not** caused by haploinsufficiency but by a **dominant-negative** effect of missense variants. These dominant variants cluster in SPACR's two **SEA domains** — SEA1 (residues ~232–354) variants (e.g., p.Leu238Arg) produce the vitelliform/VMD4 phenotype, whereas SEA2 (residues ~571–684) variants (e.g., p.Leu579Pro) produce the RP91 phenotype.

Mechanistically, mutant SPACR disrupts the SPACR–SPACRCAN (IMPG1–IMPG2) matrix scaffold, impairing photoreceptor–RPE adhesion, retinoid cycling (reduced 11-cis-retinal), and outer-segment maintenance, leading to accumulation of autofluorescent subretinal vitelliform material above a preserved RPE and progressive photoreceptor degeneration. This causal chain is supported by human genetics, human retinal organoid functional studies, a medaka knockdown model, and an **Impg1-knockout mouse** that recapitulates the deposits, ERG attenuation, and photoreceptor-layer degeneration. No disease-specific therapy exists; management is supportive, centered on genetic counseling, low-vision support, and surveillance.

---

## Key Findings

### Finding 1 — IMPG1 causes autosomal dominant adult-onset vitelliform macular dystrophy (VMD4)

IMPG1 (encoding SPACR, chromosome 6q14) is an established cause of autosomal dominant adult-onset vitelliform macular dystrophy. The landmark study by Meunier et al. (2014) screened 49 families with vitelliform maculopathy negative for mutations in the two previously known genes (BEST1 and PRPH2). They identified IMPG1 as causal in 3 families (11 patients), with autosomal dominant families 1 and 2 both carrying the recurrent missense variant **c.713T>G (p.Leu238Arg)**. Together, IMPG1 and its paralog IMPG2 accounted for approximately **8%** of BEST1/PRPH2-negative vitelliform families, establishing these genes as a meaningful contributor to the genetic architecture of VMD.

Clinically, the dominant IMPG1 vitelliform phenotype is characterized by **late onset (mean ~42 years)** and **moderate visual impairment (mean visual acuity ~20/40)**. A diagnostically important feature is that the vitelliform material sits **above a preserved RPE**, and the **electrooculogram (EOG) is normal or borderline** — distinguishing IMPG1/IMPG2 VMD from the BEST1-related (Best disease, abnormal EOG) and PRPH2-related forms.

> *"families 1 and 2 had the c.713T→G (p.Leu238Arg) mutation in IMPG1"* — [PMID: 25085631](https://pubmed.ncbi.nlm.nih.gov/25085631/)
>
> *"IMPG1 and IMPG2 are new causal genes in 8% of families negative for BEST1 and PRPH2 mutations."* — [PMID: 25085631](https://pubmed.ncbi.nlm.nih.gov/25085631/)

### Finding 2 — Dual inheritance and a broad phenotypic spectrum (VMD, pattern dystrophy, retinitis pigmentosa)

IMPG1 retinopathy displays **both autosomal dominant and autosomal recessive** inheritance and a phenotypic spectrum spanning vitelliform macular dystrophy, pattern dystrophy, and retinitis pigmentosa (RP). Olivier et al. (2021, *J Med Genet*) used exome sequencing in an autosomal dominant RP family to reveal an IMPG1 splice variant; the same variant recurred in families with either RP or VMD, alongside 8 additional families with missense or nonsense IMPG1 variants. Critically, the variant originally described in 2004 as **"benign concentric annular macular dystrophy" (BCAMD; p.Leu579Pro)** was **reclassified as RP with early macular involvement**, resolving the historical nomenclature and placing BCAMD firmly within the IMPG1 RP spectrum.

Registry-scale data reinforce the dominant predominance: in the IRD-PT registry (Francisco et al., 2026), IMPG1 cases were **87.5% autosomal dominant** (contrasting with IMPG2, which was 75% recessive). Al-Khuzaei et al. (2025) reported two IMPG1 patients, both **monoallelic** (one AVMD, one pattern dystrophy), presenting at advanced ages (81 and 72 years), underscoring the late-onset character of the dominant disease.

> *"This study discusses a previously unreported association between monoallelic or biallelic IMPG1 variants and RP."* — [PMID: 32817297](https://pubmed.ncbi.nlm.nih.gov/32817297/)
>
> *"the clinical diagnosis of the IMPG1 retinopathy-associated variant, originally described as benign concentric annular macular dystrophy, was also revised to RP with early macular involvement"* — [PMID: 32817297](https://pubmed.ncbi.nlm.nih.gov/32817297/)
>
> *"IMPG2 (75.0% AR) and IMPG1 (87.5% AD) caused RP and adult-onset vitelliform macular dystrophy."* — [PMID: 42321002](https://pubmed.ncbi.nlm.nih.gov/42321002/)

### Finding 3 — SPACR is essential for photoreceptor survival; the Impg1-knockout mouse recapitulates human disease

SPACR is required for photoreceptor survival, and loss of IMPG1 produces a retinal phenotype in model organisms that mirrors the human disease. Olivier, Brabet, and colleagues (2022, *Genes*) characterized an **Impg1-deficient (knockout) mouse** that develops **autofluorescent deposits** (visible on fundus imaging and SD-OCT), **attenuated ERG responses from ~9 months of age**, **photoreceptor-layer degeneration**, and — on transmission electron microscopy — **disruption of the interphotoreceptor matrix and of the RPE**. The mice also show a **decrease in 11-cis-retinal**, linking IMPG1 loss to impaired retinoid (visual) cycling. SPACR and its paralog SPACRCAN (IMPG2) are the main components of the IPM. Complementary evidence comes from medaka fish: morpholino knockdown of impg1/impg2 (Olivier 2021) produced **shortened rod and cone outer segments**.

> *"our results demonstrate the essential role of SPACR in maintaining photoreceptors"* — [PMID: 36140676](https://pubmed.ncbi.nlm.nih.gov/36140676/)
>
> *"SD-OCT of Impg1-/- mice shows a degeneration of the photoreceptor layer, and transmission electron microscopy shows a disruption of the IPM and the retinal pigment epithelial cells."* — [PMID: 36140676](https://pubmed.ncbi.nlm.nih.gov/36140676/)
>
> *"The decrease in the concentration of the chromophore 11-cis-retinal supports this loss of photoreceptors."* — [PMID: 36140676](https://pubmed.ncbi.nlm.nih.gov/36140676/)

### Finding 4 — SPACR is a hyaluronan-binding glycoprotein forming the IPM scaffold (not a GAG-bearing proteoglycan)

SPACR, the IMPG1 gene product, is the hyaluronan-binding glycoprotein that constitutes the structural scaffold of the insoluble IPM. Acharya et al. (1998) demonstrated that SPACR is the prominent **147–150 kDa** band in the IPM, localizes to the matrix surrounding both rods and cones, and possesses a **functional hyaluronan-binding domain**. Despite the "proteoglycan" in the gene name, SPACR is **not a chondroitin-sulfate proteoglycan**: it lacks a GAG attachment site and resists chondroitinase ABC digestion. Instead it carries abundant **N- and O-linked glycoconjugates** and a **mucin-like domain** (PMID 9719680). The sialic-acid-rich O-linked glycans (e.g., NeuAcα2-3Galβ1-3GalNAc) contribute to the polyanionic character of the IPM and provide sites for cross-linking into the ordered IPM lattice. The hyaluronan-binding motif maps near the C-terminus and competitively binds heparin as well (PMID 18466325, PMID 18786170). In chick, SPACR expression parallels the development of adhesion between the neural retina and the RPE (PMID 11991949).

> *"We present evidence that SPACR has a functional hyaluronan binding domain, suggesting that interactions between SPACR and hyaluronan may serve to form the basic macromolecular scaffold, which comprises the insoluble interphotoreceptor matrix."* — [PMID: 9813076](https://pubmed.ncbi.nlm.nih.gov/9813076/)
>
> *"SPACR is the most prominent 147-150-kDa band present in the interphotoreceptor matrix and is the gene product of IMPG1"* — [PMID: 9813076](https://pubmed.ncbi.nlm.nih.gov/9813076/)
>
> *"SPACR is not a chondroitin sulfate proteoglycan"* — [PMID: 9813076](https://pubmed.ncbi.nlm.nih.gov/9813076/)

### Finding 5 — IMPG1 is required for human photoreceptor outer-segment and IPM development (retinal organoid evidence)

Human in-vitro evidence confirms that IMPG1 is required for photoreceptor outer-segment and IPM development. Felemban et al. (2018) showed that in human pluripotent stem cell (hPSC)-derived retinal organoids, IMPG1 and IMPG2 are expressed in the developing IPM, and that this expression pattern is **conserved between human retina and organoids**. Functional blockade of **CD44 and IMPG1** disrupted the development of photoreceptors, their inner/outer segments and connecting cilia, and impaired IPM formation — with **IMPG1 having an earlier and more significant impact** than CD44. CD44 is the hyaluronan receptor on Müller cell microvilli, linking the SPACR–hyaluronan scaffold to a defined cellular partner.

> *"Blocking the action of CD44 and IMPG1 in pluripotent stem cell derived retinal organoids affected the development of photoreceptors, their inner/outer segments and connecting cilia and disrupted IPM formation, with IMPG1 having an earlier and more significant impact."* — [PMID: 29777959](https://pubmed.ncbi.nlm.nih.gov/29777959/)

### Finding 6 — IMPG1 is LoF-tolerant in gnomAD → dominant disease is likely dominant-negative

Population constraint data argue that the dominant disease mechanism is **dominant-negative** rather than haploinsufficiency. gnomAD v4 constraint metrics for IMPG1 (ENSG00000112706) show **pLI ≈ 0** (5.3×10⁻²⁷), an **observed/expected LoF ratio of 0.92** (85 observed vs 92.0 expected loss-of-function variants), a **LOEUF upper bound of 1.11**, a LoF Z-score of 0.62, and a missense Z-score of −0.91. Collectively these indicate that IMPG1 is **not constrained** against heterozygous loss of function — i.e., the general population tolerates IMPG1 null alleles well, so simple haploinsufficiency is an unlikely disease mechanism.

Consistent with this, the autosomal **dominant** phenotype is driven predominantly by recurrent **missense** variants (e.g., p.Leu238Arg, p.Leu579Pro, p.Asp423Glu) rather than truncating/null alleles, whereas **biallelic/null** genotypes produce recessive RP. The most parsimonious interpretation is that mutant SPACR monomers poison the SPACR–SPACRCAN matrix assembly (dominant-negative), while a single null allele — leaving one functional copy — is insufficient to cause disease. (Evidence source: computational/population genetics; gnomAD. ClinVar lists on the order of ~117 pathogenic + ~53 likely pathogenic IMPG1 variants.)

### Finding 7 — Dominant variants cluster in SPACR's two SEA domains (SEA1→VMD4; SEA2→RP91)

A clear genotype–phenotype architecture emerges from mapping pathogenic variants onto the SPACR protein. UniProt Q17R60 (SPACR, 797 aa) annotates: a signal peptide (residues 1–20); **SEA domain 1 at residues 232–354**; **SEA domain 2 at residues 571–684**; and a central O-glycosylated **mucin-like cluster** (O-GalNAc at Thr403/421/432/442) with multiple N-glycosylation sites. SEA (Sea-urchin sperm protein, Enterokinase, Agrin) domains are proteolytically processed modules found in many heavily glycosylated membrane-associated proteins, and SEA-domain mutations are broadly disease-relevant.

- The recurrent dominant **vitelliform** variant **p.Leu238Arg** (rs713993045) lies inside **SEA1** and is annotated "in **VMD4**."
- The **p.Leu579Pro** variant (rs1782008883; the original "BCAMD" allele) lies inside **SEA2** and is annotated "in **RP91**"; additional RP91 variants map to residues 613 and 626, also within/adjacent to SEA2.
- The novel VMD variant **p.Asp423Glu** (Nguyen/Al-Khuzaei cohorts) lies in the inter-SEA mucin-like O-glycosylation region.

> *"Mutations within these domains are linked to a range of pathologies, including various cancers and congenital disorders, underscoring their clinical importance."* — [PMID: 39930241](https://pubmed.ncbi.nlm.nih.gov/39930241/)

| Variant (protein) | cDNA / rsID | SPACR domain | Phenotype | OMIM | Inheritance |
|---|---|---|---|---|---|
| p.Leu238Arg | c.713T>G / rs713993045 | SEA1 (232–354) | Vitelliform macular dystrophy | VMD4 (616151) | AD |
| p.Asp423Glu | — | Inter-SEA mucin region | Vitelliform macular dystrophy (novel) | VMD4 | AD (monoallelic) |
| p.Leu579Pro | c.1736T>C / rs1782008883 | SEA2 (571–684) | RP with early macular involvement (orig. "BCAMD") | RP91 (617304) | AD |
| variants at res. 613, 626 | — | SEA2 (adjacent) | Retinitis pigmentosa | RP91 | AD |

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** IMPG1-related dominant retinopathy is a rare inherited retinal dystrophy in which heterozygous variants in **IMPG1/SPACR** disrupt the interphotoreceptor matrix, producing adult/late-onset macular and/or rod–cone degeneration. The dominant disease most often presents as **adult-onset vitelliform macular dystrophy** (yellowish subretinal deposits in the macula) and, less commonly, as a **retinitis pigmentosa** spectrum.

**Key identifiers.**
- **Mondo:** MONDO:1040036
- **Causal gene:** IMPG1 (HGNC:6054); protein SPACR (UniProt Q17R60); gene OMIM \*602870
- **OMIM (allelic disorders):** Vitelliform macular dystrophy 4 (**VMD4, 616151**); Retinitis pigmentosa 91 (**RP91, 617304**)
- **Orphanet:** within the "adult-onset vitelliform macular dystrophy" / "retinitis pigmentosa" rare-disease groupings
- **ICD-10/ICD-11:** H35.5 (hereditary retinal dystrophy) / ICD-11 9B70–9B71 region; **MeSH:** closest terms "Vitelliform Macular Dystrophy," "Retinitis Pigmentosa," "Retinal Dystrophies"

**Synonyms / alternative names:** autosomal dominant IMPG1 retinopathy; autosomal dominant IMPG1-related vitelliform macular dystrophy; autosomal dominant IMPG1-related retinitis pigmentosa; benign concentric annular macular dystrophy (BCAMD — now reclassified as RP with early macular involvement).

**Source type.** Information is derived from **aggregated disease-level resources** (OMIM, Orphanet, ClinVar, gnomAD, UniProt) plus **primary clinical case series/cohorts** and **experimental model studies** — not from individual EHR records.

### 2. Etiology

**Primary cause — genetic.** The disease is **monogenic**: pathogenic variants in IMPG1. There is no environmental or infectious cause.

**Genetic risk factors.** Causal, recurrent dominant variants include **p.Leu238Arg** (SEA1; VMD4), **p.Leu579Pro** (SEA2; RP91), and **p.Asp423Glu** (inter-SEA region). A splice variant can produce RP or VMD within a single family. Biallelic (null/missense) genotypes cause **recessive RP**. The paralog **IMPG2** causes a clinically overlapping retinopathy, and the two proteins are functionally interdependent.

**Environmental / lifestyle risk factors.** None established. Age modifies *expression* (late onset) but is not a cause. No sex predilection has been reported.

**Protective factors.** None specifically identified. Because IMPG1 LoF is tolerated in gnomAD, heterozygous null alleles in the population do not cause dominant disease — relevant to interpreting incidental findings, but not a "protective" intervention.

**Gene–environment interactions.** None documented.

### 3. Phenotypes

| Phenotype | Type | Suggested HPO | Onset | Severity | Progression | Frequency |
|---|---|---|---|---|---|---|
| Vitelliform (yellowish subretinal) macular deposits | Clinical sign (imaging) | HP:0011506 (Macular dystrophy) | Adult (mean ~42 y) | Moderate | Progressive | Characteristic of dominant VMD form |
| Reduced visual acuity / central vision loss | Symptom | HP:0000572 (Visual loss) | Adult | Mild–moderate (mean VA ~20/40) | Slowly progressive | Common |
| Metamorphopsia (distorted central vision) | Symptom | HP:0012508 | Adult | Mild | Fluctuating/progressive | Variable |
| Night blindness (nyctalopia) | Symptom | HP:0000662 | Variable | Variable | Progressive | RP-spectrum |
| Peripheral/constricted visual field | Clinical sign | HP:0001133 | Variable | Variable | Progressive | RP-spectrum |
| Abnormal fundus autofluorescence | Imaging abnormality | — | Adult | — | Progressive | Characteristic |
| Reduced/attenuated ERG responses | Lab abnormality | HP:0000512 (Abnormal ERG) | Later/RP-spectrum | Variable | Progressive | RP-spectrum |
| Normal/borderline EOG (distinguishing) | Lab abnormality | — | — | — | Stable | Distinguishes from BEST1 |

**Quality of life.** The dominant vitelliform form generally causes **moderate** central-vision impairment with preserved independence for most daily tasks early on; reading, driving, and fine central tasks are most affected. The RP-spectrum form carries greater burden through night blindness and peripheral field loss. No disease-specific EQ-5D/SF-36 data were identified; impact is inferred from macular dystrophy and RP literature generally.

### 4. Genetic / Molecular Information

- **Causal gene:** **IMPG1**, chromosome **6q14.1**; gene OMIM \*602870; HGNC:6054. 797-aa protein SPACR (UniProt Q17R60).
- **Pathogenic variants:** predominantly **missense** for dominant disease (p.Leu238Arg, p.Leu579Pro, p.Asp423Glu, and variants at res. 613/626); **splice** variants and **nonsense/truncating** variants also reported, the latter more associated with recessive disease. ClinVar: ~117 pathogenic + ~53 likely pathogenic IMPG1 variants (ACMG/AMP).
- **Allele frequencies:** dominant pathogenic missense variants are rare/absent-to-very-low in gnomAD; general LoF variants are present at frequencies consistent with LoF tolerance.
- **Origin:** germline. No somatic involvement.
- **Functional consequences:** dominant missense variants in SEA1/SEA2 most likely act by a **dominant-negative** mechanism (poisoning the SPACR/SPACRCAN scaffold); biallelic null → **loss of function** → recessive RP.
- **Modifier genes:** IMPG2 is a strong candidate functional modifier given SPACR–SPACRCAN interdependence; CD44 (hyaluronan receptor) is a mechanistic partner. No formal modifier mapping exists.
- **Epigenetic / chromosomal abnormalities:** none implicated.

### 5. Environmental Information

No environmental factors, lifestyle factors, toxins, or infectious agents are implicated. This is a purely Mendelian disorder.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A **heterozygous missense variant** in an IMPG1 **SEA domain** (SEA1, e.g. p.Leu238Arg; or SEA2, e.g. p.Leu579Pro) **leads to** production of a structurally abnormal SPACR monomer.
2. The mutant SPACR **results in** a dominant-negative disruption of the SPACR–SPACRCAN (IMPG1–IMPG2) matrix assembly (*inferred* from LoF tolerance in gnomAD plus the missense-driven dominant genetics; the exact biochemical poisoning step is not yet directly demonstrated).
3. Disrupted SPACR **leads to** destabilization of the hyaluronan-anchored IPM scaffold and impaired photoreceptor–RPE / Müller-microvillus (CD44) adhesion.
4. A compromised IPM **results in** defective trafficking of retinoids and other molecules across the subretinal space (*demonstrated*: 11-cis-retinal reduced in Impg1-knockout mice; IRBP docking depends on IPM domains).
5. Impaired outer-segment support and retinoid cycling **lead to** accumulation of shed outer-segment/autofluorescent material as **subretinal vitelliform deposits above a preserved RPE** (observed in patients and knockout mice).
6. Chronic matrix/metabolic stress **results in** progressive **photoreceptor degeneration**, ERG attenuation, and vision loss — in the macula → **vitelliform macular dystrophy**; **branch:** with SEA2 variants or biallelic null → **rod–cone degeneration (retinitis pigmentosa)** with field loss and nyctalopia.

```
IMPG1 SEA-domain missense (heterozygous)
        │  (SEA1→macula/VMD4 ; SEA2→RP91)
        ▼
Abnormal SPACR monomer ──► dominant-negative poisoning of SPACR/SPACRCAN scaffold
        ▼
Destabilized hyaluronan-anchored IPM  ◄── CD44 (Müller microvilli) interaction impaired
        ▼
Impaired retinoid trafficking (↓11-cis-retinal) + loss of photoreceptor–RPE adhesion
        ▼
Autofluorescent subretinal (vitelliform) deposits above preserved RPE
        ▼
Progressive photoreceptor degeneration ──► ERG attenuation ──► vision loss
                                           └─► branch: RP (field loss, nyctalopia)
```

**Molecular pathways / cellular processes.** Extracellular matrix organization; hyaluronan binding and cross-linking; cell–matrix adhesion; the visual (retinoid) cycle. Relevant GO terms: **GO:0030198** (extracellular matrix organization), **GO:0005540** (hyaluronic acid binding), **GO:0007601** (visual perception), **GO:0042574** (retinal metabolic process).

**Protein dysfunction.** SEA-domain missense substitutions alter SPACR structure; given SEA domains' role in glycoprotein processing/assembly, the likely defect is impaired matrix incorporation/oligomerization (dominant-negative), not enzymatic loss. **Cell types:** rod photoreceptor (**CL:0000604**), cone photoreceptor (**CL:0000573**), retinal pigment epithelial cell (**CL:0002586**), Müller glial cell (**CL:0000636**). **Subcellular:** interphotoreceptor matrix / extracellular region (**GO:0005578** proteinaceous extracellular matrix); photoreceptor outer segment (**GO:0001750**) and connecting cilium secondarily affected.

**Molecular profiling.** IMPG1/IMPG2 expression is photoreceptor/retina-specific and developmentally regulated, rising as outer segments elaborate (chick, rat, mouse, human-organoid data). No disease-specific proteomic/metabolomic signatures beyond reduced 11-cis-retinal in the mouse model.

### 7. Anatomical Structures Affected

- **Organ:** eye (**UBERON:0000970**), specifically the **retina** (**UBERON:0000966**) and **macula lutea** (**UBERON:0005390**) for the VMD form.
- **Tissue/cell:** photoreceptor layer (rods **CL:0000604**, cones **CL:0000573**); retinal pigment epithelium (**UBERON:0001782** / **CL:0002586**); Müller glia (**CL:0000636**); the **interphotoreceptor/subretinal matrix** (**UBERON:0013706** subretinal space).
- **Subcellular:** interphotoreceptor matrix / extracellular region; photoreceptor outer segment and connecting cilium secondarily affected.
- **Localization:** **bilateral**, typically symmetric; macula-centered in VMD, more diffuse in RP.

### 8. Temporal Development

- **Onset:** **adult/late-onset** (dominant VMD mean ~42 y; some monoallelic cases present in the 7th–9th decades). Pattern: **insidious/chronic**.
- **Progression:** slowly **progressive**; vision typically **moderately** impaired in VMD. RP-spectrum cases show progressive field constriction and ERG decline. In the mouse model, ERG attenuation begins ~9 months.
- **Course / duration:** **chronic, lifelong**. No spontaneous remission. Critical intervention windows are undefined, but earlier stages (before extensive photoreceptor loss) are the logical target for any future therapy.

### 9. Inheritance and Population

- **Epidemiology:** rare; precise prevalence/incidence not established. Within IRD cohorts, IMPG1+IMPG2 account for ~1.45% of IRD patients (Nguyen et al., 2024; PMID 39858590) and ~8% of BEST1/PRPH2-negative vitelliform families (Meunier 2014).
- **Inheritance:** predominantly **autosomal dominant** (87.5% of IMPG1 cases in the IRD-PT registry); also **autosomal recessive** (biallelic) for RP.
- **Penetrance / expressivity:** appears **age-dependent** and **variable**; the same variant can manifest as RP or VMD within a family (variable expressivity).
- **Anticipation / mosaicism / founder effects / consanguinity:** not established; recurrent variants (p.Leu238Arg, p.Leu579Pro) reflect mutational recurrence rather than confirmed founders. Consanguinity is relevant to the recessive form.
- **Carrier frequency:** IMPG1 LoF alleles are present in gnomAD (LoF-tolerant), so heterozygous nulls are relatively common but non-pathogenic for dominant disease.
- **Demographics:** reported across European and other populations; no strong ethnic predilection; **no clear sex bias**.

### 10. Diagnostics

- **Imaging (cornerstone):** fundus photography (vitelliform/yellow macular lesion or pigmentary RP changes), **fundus autofluorescence** (hyperautofluorescent deposits), **SD-OCT** (subretinal hyperreflective vitelliform material **above a preserved RPE**), fluorescein angiography.
- **Electrophysiology:** **EOG normal/borderline** (key discriminator from BEST1 disease); **ERG** normal in early VMD, attenuated in RP-spectrum disease (HP:0000512).
- **Genetic testing (confirmatory):** targeted single-gene testing, **IRD gene panels** (which include IMPG1/IMPG2), **whole-exome** and **whole-genome sequencing**. Variant classification per ACMG/AMP using ClinVar/ClinGen. CMA/karyotype/FISH/mtDNA/repeat testing are **not indicated**.
- **Differential diagnosis:** Best vitelliform macular dystrophy (BEST1; abnormal EOG), PRPH2-related pattern dystrophy/AVMD, acquired (age-related) AVMD, other RP genes (for the RP form), and IMPG2 retinopathy (clinically overlapping paralog).

### 11. Outcome / Prognosis

- **Survival/mortality:** the disease is **not life-limiting**; normal life expectancy. No disease-specific mortality.
- **Morbidity/function:** **visual** morbidity — moderate central vision loss in VMD (mean VA ~20/40), more substantial functional loss in RP-spectrum cases (field constriction, night blindness). Legal blindness is possible in advanced RP.
- **Course:** chronic, slowly progressive; **complications** include geographic atrophy/photoreceptor loss over the lesion. Recovery is not expected (no retinal regeneration).
- **Prognostic factors:** variant location (SEA2/RP phenotype generally carries wider retinal involvement than SEA1/VMD), biallelic status (recessive RP), age, and extent of photoreceptor/ERG loss at presentation.

### 12. Treatment

- **No disease-specific or disease-modifying therapy exists.** Management is **supportive**: low-vision aids and rehabilitation, visual-function monitoring, and **genetic counseling**. (NCIT: Supportive Care; Genetic Counseling; Low Vision Aids.)
- **Pharmacotherapy / pharmacogenomics:** none established. No approved drugs.
- **Advanced therapeutics:** none approved. Conceptually, because dominant disease is likely dominant-negative, **allele-specific gene silencing (ASO/siRNA)** or gene correction would be more rational than simple gene augmentation; **gene augmentation** may suit the recessive (loss-of-function) form. All are hypothetical/pre-clinical.
- **Surgical/interventional:** none specific.
- **Experimental/clinical trials:** no IMPG1-specific trials identified.
- **Treatment strategy:** a genotype-guided framework (SEA1 vs SEA2; mono- vs biallelic) would inform any future precision approach.

### 13. Prevention

- **Primary prevention:** not applicable (genetic disease). **Genetic counseling** and reproductive options (prenatal testing, preimplantation genetic testing) are available for at-risk families.
- **Secondary prevention:** **cascade genetic testing** of relatives; periodic ophthalmic surveillance of carriers to detect onset and manage visual function early.
- **Tertiary prevention:** low-vision rehabilitation, monitoring/managing complications; general retinal-health measures (e.g., smoking cessation, UV protection) are prudent though not evidence-based for this specific gene.
- **Public health/immunization/prophylaxis:** not applicable.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** IMPG1 orthologs exist across vertebrates — mouse *Impg1* (**NCBI Gene 16011**), plus orthologs in rat, chick, medaka/zebrafish, and Xenopus. SPACR/SPACRCAN biology has been characterized in **chick** (PMID 11991949, 16469746, 18466325), **rat** (PMID 11406817, 9778409), **mouse** (PMID 12589770, 36140676), and **Xenopus** (PMID 23470504).
- **Natural disease in animals:** no well-documented naturally occurring IMPG1 retinopathy in companion animals is recorded here; the disease is primarily studied via engineered/knockdown models.
- **Comparative biology:** the IPM, SPACR/SPACRCAN composition, hyaluronan scaffold, and CD44 partnership are **evolutionarily conserved**, making cross-species models informative. Mechanisms of outer-segment support are conserved.
- **Transmission:** none (non-infectious, non-zoonotic).

### 15. Model Organisms

| Model | Type | Genetic manipulation | Phenotype recapitulation | Reference |
|---|---|---|---|---|
| **Impg1-knockout mouse** | Mammalian in vivo | Constitutive KO | Autofluorescent deposits, SD-OCT photoreceptor-layer degeneration, ERG attenuation from ~9 mo, IPM/RPE disruption on TEM, ↓11-cis-retinal — **strong** recapitulation | [PMID: 36140676](https://pubmed.ncbi.nlm.nih.gov/36140676/) |
| **Medaka fish** | Vertebrate in vivo | impg1/impg2 morpholino knockdown | Shortened rod and cone outer segments — models developmental OS defect | Olivier 2021 (J Med Genet) |
| **Human retinal organoids (hPSC)** | In vitro, human | CD44/IMPG1 functional blockade | Disrupted photoreceptor / IS-OS / connecting cilium and IPM development; IMPG1 earlier/greater impact | [PMID: 29777959](https://pubmed.ncbi.nlm.nih.gov/29777959/) |
| Chick / rat / Xenopus retina | Vertebrate, descriptive | — | SPACR/SPACRCAN localization, hyaluronan binding, developmental expression, IRBP docking | PMIDs 11991949, 11406817, 23470504 |

**Model limitations:** the mouse KO models **loss of function** (recessive-type mechanism), not the human **dominant-negative** missense state; a **knock-in** of p.Leu238Arg or p.Leu579Pro is needed to faithfully model dominant disease. Morpholino knockdown is transient/developmental; organoids capture development but not chronic adult-onset degeneration. **Resources:** MGI (mouse *Impg1*), IMPC/KOMP, ZFIN (zebrafish), Cellosaurus (hPSC lines).

---

## Mechanistic Model / Interpretation

The unifying model is that **SPACR is the structural glue of the subretinal compartment**. It binds hyaluronan near its C-terminus to form the insoluble IPM lattice, co-assembles with SPACRCAN (IMPG2), and engages CD44 on Müller microvilli — together maintaining photoreceptor–RPE adhesion and a conduit for retinoid/IRBP trafficking. Any insult to this scaffold degrades outer-segment support and the visual cycle, which manifests first as accumulation of autofluorescent (vitelliform) material and then as photoreceptor death.

The **genotype–mechanism correlation** is the central intellectual contribution of this investigation:

- **gnomAD LoF-tolerance (F006)** rules out haploinsufficiency as the dominant mechanism — a single IMPG1 null is benign in the population.
- Therefore the **dominant, missense, SEA-domain-clustered** variants (F007) must act by a **dominant-negative** route, with mutant SPACR corrupting the scaffold that wild-type SPACR and SPACRCAN would otherwise build.
- **SEA1 vs SEA2** position tracks with phenotype (macular/VMD4 vs rod–cone/RP91), suggesting the two SEA modules make functionally distinct contributions to matrix assembly across retinal regions.
- The **recessive RP** form, driven by biallelic null/severe alleles, fits a conventional loss-of-function mechanism — consistent with a single null being tolerated while complete deficiency is not, as proven by the knockout mouse.

This two-mechanism picture (dominant-negative missense vs recessive null) has direct therapeutic implications: allele-specific silencing for dominant disease; gene augmentation for recessive disease.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [25085631](https://pubmed.ncbi.nlm.nih.gov/25085631/) | IMPG1/IMPG2 vitelliform frequency & pattern (Meunier 2014) | Human clinical cohort | F001 — AD VMD; p.Leu238Arg; 8% of BEST1/PRPH2-neg families |
| [32817297](https://pubmed.ncbi.nlm.nih.gov/32817297/) | Pathogenic IMPG1 variants / dual inheritance (Olivier 2021) | Human clinical + genetics | F002 — AD & AR; RP/VMD spectrum; BCAMD→RP reclassification |
| [42321002](https://pubmed.ncbi.nlm.nih.gov/42321002/) | IRD-PT registry dual-inheritance genes | Human registry | F002 — IMPG1 87.5% AD |
| [36140676](https://pubmed.ncbi.nlm.nih.gov/36140676/) | SPACR essential / Impg1-KO mouse (Olivier-Brabet 2022) | Model organism | F003 — KO recapitulates deposits, degeneration, ↓11-cis-retinal |
| [9813076](https://pubmed.ncbi.nlm.nih.gov/9813076/) | SPACR hyaluronan-binding IPM glycoprotein (Acharya 1998) | In vitro/biochemical | F004 — scaffold role; not a CS-proteoglycan |
| [9719680](https://pubmed.ncbi.nlm.nih.gov/9719680/) | SPACR glycoconjugate characterization | In vitro | F004 — N/O-glycans, mucin-like, sialylated |
| [29777959](https://pubmed.ncbi.nlm.nih.gov/29777959/) | hPSC retinal organoid IMPG1/CD44 (Felemban 2018) | Human in vitro | F005 — IMPG1 required for OS/IPM development |
| [18466325](https://pubmed.ncbi.nlm.nih.gov/18466325/) / [18786170](https://pubmed.ncbi.nlm.nih.gov/18786170/) | HA-binding motif / heparin competition | In vitro | F004 — C-terminal HABM |
| [14691150](https://pubmed.ncbi.nlm.nih.gov/14691150/) | BCAMD locus 6p12.3-q16 → IMPG1 p.Leu579Pro | Human linkage | F002/F007 — SEA2 RP allele |
| [39858590](https://pubmed.ncbi.nlm.nih.gov/39858590/) | Prevalence of IMPG1/IMPG2 in IRD cohort | Human cohort | Epidemiology (1.45% of IRDs); novel p.Asp423Glu |
| [39930241](https://pubmed.ncbi.nlm.nih.gov/39930241/) | Critical roles of SEA domains | Review | F007 — SEA-domain mutations are disease-relevant |
| 11991949 / 11406817 / 12589770 / 16469746 / 23470504 | SPACR/SPACRCAN comparative biology | Model/comparative | F004 — conserved IPM biology, IRBP docking |

**gnomAD v4** (computational): IMPG1 pLI≈0, o/e LoF=0.92, LOEUF upper=1.11 → underpins F006.

---

## Limitations and Knowledge Gaps

1. **Dominant-negative mechanism is inferred, not proven.** F006 rests on population constraint plus the missense-dominant/null-recessive pattern; no biochemical experiment has yet shown mutant SPACR poisoning wild-type scaffold assembly. The existing mouse models loss of function, not the dominant missense state.
2. **Genotype–phenotype rule (SEA1→VMD, SEA2→RP) is based on few variants.** Larger cohorts are needed to test whether the correlation is robust or has exceptions (variable expressivity already blurs it).
3. **Penetrance and natural history are poorly quantified.** No prospective natural-history study; progression rates, conversion from VMD to atrophy, and sex/ethnic distributions are not well defined.
4. **Epidemiology is imprecise** — only cohort-relative frequencies (~1.45% of IRDs; ~8% of BEST1/PRPH2-neg VMD) are available; no population prevalence.
5. **No therapeutics or trials** exist; QoL data are extrapolated from generic macular-dystrophy/RP literature, not IMPG1-specific.
6. Some supporting citations are drawn from abstracts/snippets; a few newer cohort papers (e.g., PMID 41465146) had no abstract available for verification.

## Proposed Follow-up Experiments / Actions

1. **Generate SEA-domain knock-in mice** (p.Leu238Arg and p.Leu579Pro) to directly test the dominant-negative hypothesis and the SEA1-vs-SEA2 phenotype branch; compare to the existing KO.
2. **Biochemical co-assembly assays** — express WT and mutant SPACR with SPACRCAN in vitro (and in organoids) to measure whether mutant SPACR impairs scaffold formation, hyaluronan binding, or CD44 engagement.
3. **Deep variant curation** across ClinVar/large IRD cohorts to statistically test the SEA1→VMD / SEA2→RP correlation and refine ACMG classification.
4. **Prospective multimodal-imaging natural-history study** (FAF, SD-OCT, ERG/EOG) to define progression, penetrance, and conversion to atrophy.
5. **Therapeutic proof-of-concept:** allele-specific ASO/siRNA knockdown for dominant alleles in patient-derived organoids; AAV-IMPG1 augmentation for the recessive form.
6. **Standardize IMPG1 on IRD gene panels** and promote cascade testing and genetic counseling for at-risk relatives.

---

### Ontology Appendix (suggested terms)

- **Disease:** MONDO:1040036; OMIM 616151 (VMD4), 617304 (RP91)
- **Gene/protein:** HGNC:6054 (IMPG1); UniProt Q17R60 (SPACR); gene OMIM \*602870
- **HPO:** HP:0011506 (Macular dystrophy), HP:0000572 (Visual loss), HP:0012508 (Metamorphopsia), HP:0000662 (Nyctalopia), HP:0001133 (Constriction of visual field), HP:0000512 (Abnormal ERG)
- **GO:** GO:0030198 (ECM organization), GO:0005540 (hyaluronic acid binding), GO:0007601 (visual perception), GO:0042574 (retinal metabolic process), GO:0005578 (proteinaceous ECM)
- **CL:** CL:0000604 (rod), CL:0000573 (cone), CL:0002586 (RPE cell), CL:0000636 (Müller glial cell)
- **UBERON:** UBERON:0000966 (retina), UBERON:0005390 (macula lutea), UBERON:0001782 (RPE), UBERON:0013706 (subretinal space)
- **CHEBI:** 11-cis-retinal, hyaluronic acid (CHEBI:16336)
- **NCIT:** Supportive Care, Genetic Counseling, Low Vision Aids


## Artifacts

- [OpenScientist final report](IMPG1-related_Dominant_Retinopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](IMPG1-related_Dominant_Retinopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 7 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:23470504` (1 mention) - Cone outer segment and Müller microvilli pericellular matrices provide binding domains for interphotoreceptor retinoid-binding protein (IRBP).
  - shared terms: retinal, model

Weighed against this report's own most characteristic terms: `impg1`, `spacr`, `dominant`, `disease`, `variant`, `gene`, `impg2`, `vmd`, `vitelliform`, `genetic`, `macular`, `phenotype`, `retinal`, `dystrophy`, `sea2`, `spacrcan`, `leu238arg`, `leu579pro`, `loss`, `model`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 20 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0011506` (2 mentions) - the report calls it "Macular dystrophy"; HP calls it **Choroidal neovascularization**
- `HP:0012508` (2 mentions) - the report calls it "Symptom", "Metamorphopsia"; HP calls it **Metamorphopsia**
- `HP:0000662` (2 mentions) - the report calls it "Symptom", "Nyctalopia"; HP calls it **Nyctalopia**
- `HP:0001133` (2 mentions) - the report calls it "Clinical sign", "Constriction of visual field"; HP calls it **Constriction of peripheral visual field**
- `GO:0005578` (2 mentions) - the report calls it "proteinaceous ECM"; GO calls it **GO_0005578**
- `UBERON:0013706` (2 mentions) - the report calls it "subretinal space"; UBERON calls it **bone spine**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005578` (GO_0005578) (2 mentions) - replaced by `GO:0031012`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000512` (3 mentions) - the report calls it "Abnormal ERG"; HP calls it **Abnormal electroretinogram**, and lists "Abnormal ERG" among its other names
- `GO:0030198` (2 mentions) - the report calls it "ECM organization"; GO calls it **extracellular matrix organization**
- `CL:0000604` (3 mentions) - the report calls it "rod"; CL calls it **retinal rod cell**, and lists "rod" among its other names
- `CL:0000573` (3 mentions) - the report calls it "cone"; CL calls it **retinal cone cell**, and lists "cone" among its other names
- `CL:0002586` (3 mentions) - the report calls it "RPE cell"; CL calls it **retinal pigment epithelial cell**, and lists "RPE" among its other names
- `CL:0000636` (3 mentions) - the report calls it "Müller glial cell"; CL calls it **Mueller cell**, and lists "Müller cell" among its other names
- `UBERON:0005390` (2 mentions) - the report calls it "macula lutea"; UBERON calls it **cortical layer I**, and lists "molecular layer" among its other names
- `UBERON:0001782` (2 mentions) - the report calls it "RPE"; UBERON calls it **pigmented layer of retina**, and lists "RPE" among its other names
- `CHEBI:16336` (1 mention) - the report calls it "CHEBI:** 11-cis-retinal, hyaluronic acid"; CHEBI calls it **hyaluronic acid**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HGNC:6054` - called "Causal gene:** IMPG1", "IMPG1"
- `HP:0012508` - called "Symptom", "Metamorphopsia"
- `HP:0000662` - called "Symptom", "Nyctalopia"
- `HP:0001133` - called "Clinical sign", "Constriction of visual field"