---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-14T21:39:27.595999'
end_time: '2026-11-14T21:52:09.581767'
duration_seconds: 761.99
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Blastomycosis
  mondo_id: MONDO:0005672
  category: ''
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: Blastomyces dermatitidis caused disease or disorder; Blastomyces dermatitidis
    disease or disorder; Blastomyces dermatitidis infection; Blastomyces dermatitidis
    infectious disease; North American blastomycosis; blastomycotic infection; infection
    by Blastomyces dermatitidis
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
  job_id: 8c0ab2c6-9a0e-48d5-986a-54310201cdef
citation_count: 20
reference_validation:
  total_references: 28
  verified: 28
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 28
  on_topic: 15
  validator_version: 0.5.1
term_validation:
  total_terms: 29
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 10
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: CL:0000625
    reported_labels:
    - "CD8\u207A T cell"
    - "CD4\u207A/CD8\u207A T cell"
    ontology_label: CD8-positive, alpha-beta T cell
  - term_id: NCIT:C1216
    reported_labels:
    - amphotericin B
    ontology_label: Retinyl Acetate
  - term_id: NCIT:C1142
    reported_labels:
    - itraconazole
    ontology_label: Lavendustin A
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Blastomycosis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Blastomycosis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Blastomycosis
- **MONDO ID:** MONDO:0005672 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** Blastomyces dermatitidis caused disease or disorder; Blastomyces dermatitidis disease or disorder; Blastomyces dermatitidis infection; Blastomyces dermatitidis infectious disease; North American blastomycosis; blastomycotic infection; infection by Blastomyces dermatitidis
- **Category:** 

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Blastomycosis** covering all of the
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

# Blastomycosis (MONDO:0005672): A Comprehensive Disease Characterization

## Summary

**Blastomycosis is an infectious, non-genetic disease — there is no human causal gene.** It is caused by inhaling airborne conidia of the thermally dimorphic fungi *Blastomyces dermatitidis* and the cryptic species *B. gilchristii* (with additional species *B. percursus* and *B. helicus* now recognized), which live in moist, acidic soil and decaying vegetation near waterways in endemic regions of North America (the Great Lakes basin and the Ohio, Mississippi, and St. Lawrence River valleys). Because the disease is driven by a fungal pathogen rather than a host mutation, the "causal gene" requested by the template does not apply; the mechanistically relevant genes are **fungal virulence genes** — chiefly *BAD1* (Blastomyces adhesin-1) and *DRK1* (a hybrid histidine kinase governing the dimorphic switch).

Pathogenesis follows a defined causal chain: inhaled conidia reach the alveoli, where host body temperature (37 °C) triggers a *DRK1*-regulated conversion from the infectious mold to the pathogenic broad-based budding yeast. The yeast displays the major virulence adhesin **BAD-1**, which binds host tissue via heparan sulfate and tethers the yeast to macrophages through complement receptor 3 (CR3) and CD14, while suppressing protective TNF-α and blocking T-cell activation through a CD47/thrombospondin-1-mimicking mechanism. Effective host defense depends on **Th17/Tc17 cell-mediated immunity**, which explains why immunosuppressed patients (transplant recipients, those on corticosteroids or TNF-α inhibitors, HIV, hematologic malignancy) develop severe, disseminated disease. The lung is the portal of entry and primary site; hematogenous and lymphatic dissemination targets skin (most common extrapulmonary site), bone, the genitourinary tract (notably prostate), and the central nervous system, producing pyogranulomatous inflammation at all sites.

Clinically, blastomycosis is a notorious mimic — presenting as acute pneumonia (confused with bacterial pneumonia) or chronic pneumonia with weight loss, night sweats, hemoptysis, and a lung mass (confused with tuberculosis or lung carcinoma). Overall mortality is low with timely antifungal therapy (itraconazole for mild–moderate disease; amphotericin B for severe/CNS/immunocompromised/pregnancy, per IDSA 2008 guidelines), but reaches approximately **40% in mechanically ventilated patients with ARDS**. Age, female sex, immunosuppression, and diagnostic delay are the principal adverse prognostic factors. Diagnosis relies on visualizing characteristic broad-based budding yeast on histopathology and culture, supplemented by urine/serum antigen testing and BAD-1 IgG serology. Dogs serve as natural sentinel hosts, and the mouse pulmonary infection model is the standard research system.

---

## Key Findings

### Finding 1 — The disease is caused by thermally dimorphic *Blastomyces* fungi; there is no human causal gene

Blastomycosis is an infectious disease (MONDO:0005672). The causative agents are thermally dimorphic fungi of the genus *Blastomyces*. A landmark phylogenetic analysis of seven nuclear loci (*arf6*, *chs2*, *drk1*, *fads*, *pyrF*, *tub1*, *its-2*) across 78 isolates, using Genealogical Concordance Phylogenetic Species Recognition, identified two reproductively isolated lineages: PS1 = *B. dermatitidis* and PS2 = *B. gilchristii*. Interspecific divergence was four-fold greater than intraspecific divergence, with a fixation index of Fst = 0.772 (P < 0.001), confirming the cryptic species. Additional species — *B. percursus* and *B. helicus* — have since been recognized, with *B. percursus* reported even in non-endemic countries such as Iran.

> *"the sexual, dimorphic fungus Blastomyces dermatitidis, the causative agent of blastomycosis"* — [PMID: 23533607](https://pubmed.ncbi.nlm.nih.gov/23533607/)

> *"Blastomycosis is caused by a thermally dimorphic fungus that thrives in moist acidic soil"* — [PMID: 36675937](https://pubmed.ncbi.nlm.nih.gov/36675937/)

**Ontology terms:** MONDO:0005672 (blastomycosis); NCBI:txid6190 (*Blastomyces dermatitidis*). **Key identifiers:** ICD-10 B40; ICD-11 1F2A; MeSH D001759; no OMIM/Orphanet genetic entry (infectious disease). **Synonyms:** North American blastomycosis; Gilchrist disease; *Blastomyces dermatitidis* infection; blastomycotic infection. Information is derived from aggregated disease-level resources and case series, not individual genetic/EHR patient data.

### Finding 2 — BAD-1 adhesin is the major virulence factor driving pathogenesis and immune evasion

BAD-1 (Blastomyces adhesin-1) is a 120-kDa surface protein composed of a short N-terminal region, a core of ~30–41 tandem 17-amino-acid disulfide-constrained repeats (critical for virulence), and a C-terminal EGF-like domain that anchors the protein to yeast-cell-surface chitin. Deleting half the tandem repeats impairs pathogenicity. BAD-1 binds heparin/heparan sulfate (Kd ≈ 33 ± 14 nM) via WxxWxxW thrombospondin-1-like motifs, tethers yeast to macrophages via complement receptor 3 (CR3) and CD14, and suppresses protective TNF-α. It blocks T-cell activation via a CD47-dependent mechanism and shifts the cytokine balance toward immune tolerance (less IL-12/IFN-γ, more IL-10). It is also a high-capacity calcium-binding protein (~27 Ca²⁺/mol), which contributes to its structure and environmental calcium acquisition. Functionally, BAD-1 is a **gain-of-virulence adhesin/immunomodulator**.

> *"The tandem repeats of BAD-1 thus confer pathogenicity, harbor motifs that bind heparin, and suppress T-cell activation via a CD47-dependent mechanism, mimicking mammalian TSP-1."* — [PMID: 23853587](https://pubmed.ncbi.nlm.nih.gov/23853587/)

> *"BAD1 binds yeast to macrophages (Mphi) via CR3 and CD14 and suppresses TNF-alpha, which is required for resistance."* — [PMID: 15585870](https://pubmed.ncbi.nlm.nih.gov/15585870/)

**Ontology terms / processes:** GO:0007155 (cell adhesion); GO:0008201 (heparin binding); GO:0005509 (calcium ion binding); GO:0002862 (negative regulation of inflammatory response to antigenic stimulus). Target cell: CL:0000583 (alveolar macrophage).

### Finding 3 — Protective host defense requires Th17/Tc17 cellular immunity

In mouse models, vaccine-induced Th17 (CD4⁺ IL-17⁺) cells are **necessary and sufficient** for protection against *Blastomyces*. IL-6 and IL-1/IL-17R signaling drive their differentiation, and the mannose receptor senses surface mannan to induce Th17 differentiation. In hosts lacking CD4⁺ T cells, IL-17-producing CD8⁺ (Tc17) cells mediate protection in a neutrophil-dependent manner, requiring intrinsic MyD88–Akt1–mTOR and IL-1R/TLR2 signaling. This dependence on cell-mediated immunity explains the heightened risk of severe disseminated disease in patients with impaired T-cell immunity (transplantation, corticosteroids, TNF-α inhibitors, HIV).

> *"Vaccine-induced T-helper 17 (Th17) cells are necessary and sufficient to protect against fungal infection."* — [PMID: 23788728](https://pubmed.ncbi.nlm.nih.gov/23788728/)

> *"Tc17 cells are indispensable in antifungal vaccine immunity in hosts lacking CD4(+) T cells"* — [PMID: 22829762](https://pubmed.ncbi.nlm.nih.gov/22829762/)

**Ontology terms:** CL:0000899 (Th17 cell); CL:0000625 (CD8⁺ T cell); CL:0000775 (neutrophil); GO:0072539 (Th17 cell differentiation); GO:0032620 (IL-17 production).

### Finding 4 — Prognosis: low overall mortality but ~40% in ventilated ARDS; age and female sex worsen outcome

A nationwide analysis (Nationwide Inpatient Sample 2006–2014, n = 1,848 hospitalized) found that 11.9% required mechanical ventilation (MV); mortality was **39.7% on MV versus 2.5% without MV** (P < .01), with a median time to death on MV of 12 days. Multivariate predictors of death were female sex (OR 1.84, 95% CI 1.06–3.20) and increasing age (OR 1.64 per decade, 95% CI 1.33–2.02). ARDS complicates up to 10% of hospitalized pulmonary blastomycosis and historically carries 50–90% mortality. A separate population-based national study reported crude inpatient mortality of 5% (children) and 7% (adults).

> *"mortality for patients on MV is high at ~40%"* — [PMID: 32227089](https://pubmed.ncbi.nlm.nih.gov/32227089/)

> *"Acute respiratory distress syndrome (ARDS) complicates up to 10% of pulmonary blastomycosis in hospitalized patients and carries a mortality of 50-90%"* — [PMID: 25851019](https://pubmed.ncbi.nlm.nih.gov/25851019/)

| Outcome measure | Value | Source |
|---|---|---|
| Mortality on mechanical ventilation | 39.7% | [PMID: 32227089](https://pubmed.ncbi.nlm.nih.gov/32227089/) |
| Mortality without MV | 2.5% | [PMID: 32227089](https://pubmed.ncbi.nlm.nih.gov/32227089/) |
| ARDS frequency (hospitalized pulmonary) | up to 10% | [PMID: 25851019](https://pubmed.ncbi.nlm.nih.gov/25851019/) |
| ARDS historical mortality | 50–90% | [PMID: 25851019](https://pubmed.ncbi.nlm.nih.gov/25851019/) |
| Crude inpatient mortality (adults) | 7% | [PMID: 16477560](https://pubmed.ncbi.nlm.nih.gov/16477560/) |
| Transplant 1-year mortality | 26.3% (attributable 21.1%) | [PMID: 39731672](https://pubmed.ncbi.nlm.nih.gov/39731672/) |
| Female sex (death predictor) | OR 1.84 (1.06–3.20) | [PMID: 32227089](https://pubmed.ncbi.nlm.nih.gov/32227089/) |
| Age per decade (death predictor) | OR 1.64 (1.33–2.02) | [PMID: 32227089](https://pubmed.ncbi.nlm.nih.gov/32227089/) |

### Finding 5 — Treatment: itraconazole for mild–moderate disease; amphotericin B for severe/CNS/immunocompromised/pregnancy

Per IDSA guidelines (2008 update), all immunocompromised patients and those with progressive pulmonary or any extrapulmonary disease require treatment; mild acute pulmonary disease in immunocompetent hosts may self-resolve but needs close follow-up. **Amphotericin B** (lipid formulation preferred) is first-line for life-threatening, CNS, immunocompromised, or azole-failure disease and is the only approved agent in pregnancy. **Itraconazole** is the preferred step-down and primary azole for mild-to-moderate disease. CNS disease requires lipid amphotericin B induction followed by prolonged oral azole, with **voriconazole** preferred for its CNS penetration. Typical total therapy is 6–12 months (≥12 months for CNS/bone disease).

> *"Amphotericin B is the treatment of choice for patients who are immunocompromised, have life-threatening or central nervous system (CNS) disease, or for whom azole treatment has failed"* — [PMID: 10770729](https://pubmed.ncbi.nlm.nih.gov/10770729/)

> *"we recommend initial treatment with a lipid formulation of amphotericin B followed by a prolonged course of oral azole therapy, preferably voriconazole"* — [PMID: 20166817](https://pubmed.ncbi.nlm.nih.gov/20166817/)

**NCIT / CHEBI terms:** CHEBI:6076 (itraconazole); CHEBI:2682 (amphotericin B); CHEBI:10023 (voriconazole); NCIT:C1216 (amphotericin B); NCIT:C1142 (itraconazole).

### Finding 6 — Diagnosis: broad-based budding yeast on culture/histopathology, plus antigen and BAD-1 serology

The gold standard is visualization of characteristic **broad-based, single-budding, thick-walled yeast** on histopathology/wet mount and growth in culture (dimorphic mold at 25 °C, yeast at 37 °C). Urine/serum *Blastomyces* (galactomannan) antigen EIA is sensitive for disseminated/severe disease (positive in 23/23 patients in a transplant cohort) but **cross-reacts extensively with Histoplasma**. The second-generation BAD-1 IgG EIA showed overall sensitivity 50% and specificity 90.2% (36 cases vs 370 controls), with the highest sensitivity (80%) in non-immunocompromised chronic disease and lowest in acute (35%) or immunocompromised (37.5%) disease. PCR/ITS sequencing enables species-level identification.

> *"a sensitivity of 50% and specificity of 90.2%"* — [PMID: 41553334](https://pubmed.ncbi.nlm.nih.gov/41553334/)

> *"Urine antigen testing was positive in all patients in whom it was performed (23/23)"* — [PMID: 21749587](https://pubmed.ncbi.nlm.nih.gov/21749587/)

| Diagnostic test | Performance | Note |
|---|---|---|
| Histopathology/culture (broad-based budding yeast) | Gold standard | Culture may take weeks |
| Urine antigen EIA | High sensitivity in disseminated disease (23/23) | Cross-reacts with *Histoplasma* |
| BAD-1 IgG EIA (overall) | Sens 50%, Spec 90.2% | Sens 80% in chronic immunocompetent disease |
| PCR / ITS sequencing | Species-level ID | Confirmatory |

### Finding 7 — Risk factors: environmental/soil exposure near waterways plus iatrogenic immunosuppression; male predominance

Infection is acquired by inhaling conidia aerosolized from disturbed moist acidic soil and decaying vegetation near waterways in endemic North America. Occupational (forestry, outdoor work) and recreational (camping, fishing, hunting, excavation) exposures are established. A GIS study confirmed that cases live closer to inland waterways than controls (median 690 vs 1,170 m, P = 0.003). Male predominance is seen in most series (e.g., 65% of cutaneous cases male). Immunosuppression (solid-organ/HCT transplant, corticosteroids, TNF-α inhibitors, HIV, hematologic malignancy) predisposes to severe disseminated disease, with transplant 1-year mortality of 26.3% (attributable 21.1%) and supratherapeutic immunosuppression in 42%. **No human genetic susceptibility locus is established.**

> *"closer to inland waterways than a random sample of 6528 controls (median 690 versus 1170 meters; P=0.003)"* — [PMID: 20041579](https://pubmed.ncbi.nlm.nih.gov/20041579/)

> *"Despite appropriate treatment, 1-year mortality was high at 26.3%, with attributable mortality of 21.1%"* — [PMID: 39731672](https://pubmed.ncbi.nlm.nih.gov/39731672/)

### Finding 8 — Anatomy: lung is primary; dissemination to skin (most common), bone, genitourinary tract, and CNS

The portal of entry is the lung (UBERON:0002048) after conidial inhalation; pulmonary disease ranges from asymptomatic to chronic pneumonia to ARDS. Extrapulmonary dissemination is hematogenous/lymphatic. Skin (UBERON:0002097) is the most common extrapulmonary site, presenting as verrucous or ulcerative lesions — in one cutaneous series, 65% had extracutaneous involvement and half lacked clinically significant pulmonary disease. Other sites: bone/osteoarticular (UBERON:0002481), genitourinary tract including prostate (UBERON:0002367), and CNS (UBERON:0001017) as meningitis, intracranial mass, or epidural abscess. Histopathology shows suppurative **pyogranulomatous** inflammation with broad-based budding yeast.

> *"It commonly presents as a pulmonary infection and frequently disseminates to the skin"* — [PMID: 38718236](https://pubmed.ncbi.nlm.nih.gov/38718236/)

> *"CNS blastomycosis manifested as epidural abscess (1 of 22), meningitis (7 of 22), intracranial mass lesions (10 of 22)"* — [PMID: 20166817](https://pubmed.ncbi.nlm.nih.gov/20166817/)

**Cell types involved:** CL:0000583 (alveolar macrophage); CL:0000775 (neutrophil); CL:0000624/CL:0000625 (CD4⁺/CD8⁺ T cell).

### Finding 9 — Animal disease and models: dogs are natural sentinel hosts; mouse pulmonary infection is the standard research model

Dogs (NCBI:txid9615) develop naturally occurring blastomycosis with the same geographic clustering as humans; the estimated mean annual canine incidence was ~1,420 per 100,000 in endemic north-central Wisconsin, with waterway proximity (95% of cases within 400 m) and excavation exposure as risk factors — making dogs sentinels for human risk. Cats and wildlife are also susceptible. The disease is **not transmitted person-to-person** (not contagious), although rare direct inoculation (dog bite, laboratory accident) is documented. The standard experimental model is the mouse (*Mus musculus*, NCBI:txid10090) intranasal/intratracheal pulmonary infection, used to define BAD-1 virulence and Th17/Tc17 vaccine immunity; attenuated BAD-1-deleted strains serve as live vaccines in mice.

> *"The estimated mean annual incidence of blastomycosis in dogs in this region was 1420:100,000"* — [PMID: 7666297](https://pubmed.ncbi.nlm.nih.gov/7666297/)

> *"The adhesin BAD1 is required for virulence of Blastomyces dermatitidis in a pulmonary model of infection"* — [PMID: 16805092](https://pubmed.ncbi.nlm.nih.gov/16805092/)

### Finding 10 — Temperature-dependent dimorphic switch governed by DRK1 histidine kinase initiates pathogenesis

*Blastomyces* grows as an infectious mold producing conidia at environmental temperature (~25 °C) and converts to the pathogenic broad-based budding yeast at host body temperature (37 °C). This thermal phase transition is controlled by the hybrid histidine kinase **DRK1**, described as "a global regulator of dimorphism and virulence in *Blastomyces dermatitidis* and *Histoplasma capsulatum*." DRK1 is required for yeast-phase conversion, BAD-1 expression, cell-wall remodeling, and virulence. The resulting yeast phase then displays BAD-1 and evades immunity (Finding 2).

> *"a hybrid histidine kinase, DRK1, a global regulator of dimorphism and virulence in Blastomyces dermatitidis and Histoplasma capsulatum"* — [PMID: 21842181](https://pubmed.ncbi.nlm.nih.gov/21842181/)

### Finding 11 — Temporal course: ~3–6 week incubation; acute or chronic pneumonia; notorious clinical mimic

After inhalation, incubation is typically weeks (commonly ~3–6 weeks; range up to 3 months). The course branches: many immunocompetent exposures are asymptomatic/self-limited; symptomatic disease presents either as acute pneumonia (misdiagnosed as pneumococcal pneumonia) or as subacute/chronic pneumonia with weight loss, night sweats, hemoptysis, and a lung mass mimicking tuberculosis or lung carcinoma. Extrapulmonary disease is "protean," with skin lesions (verrucous/warty or ulcerative) most common and misdiagnosed as keratoacanthoma, pyoderma gangrenosum, or carcinoma. Onset is predominantly in adults; the disease is progressive if untreated (not relapsing-remitting), with cure achievable on prolonged (6–12 month) antifungal therapy.

> *"Blastomycosis can present as an acute pneumonia which is often misdiagnosed as acute pneumococcal pneumonia or the infection may present as a chronic pneumonia along with weight loss, night sweats, hemoptysis, and a lung mass suggesting tuberculosis or carcinoma of the lung"* — [PMID: 25125734](https://pubmed.ncbi.nlm.nih.gov/25125734/)

---

## Section-by-Section Characterization (Template Coverage)

### 1. Disease Information
Blastomycosis is a systemic fungal infection acquired by inhaling conidia of thermally dimorphic *Blastomyces* species. Identifiers: MONDO:0005672; ICD-10 B40; ICD-11 1F2A; MeSH D001759; no OMIM/Orphanet genetic entry (it is infectious, not Mendelian). Synonyms include North American blastomycosis, Gilchrist disease, and *Blastomyces dermatitidis* infection. Evidence is derived from aggregated disease-level resources, cohort studies, and case series.

### 2. Etiology
**Causal factor:** infectious/environmental — inhalation of *Blastomyces* conidia from soil (Findings 1, 7, 10). **Risk factors:** environmental/occupational/recreational soil disturbance near waterways; male sex; immunosuppression (transplant, steroids, TNF-α inhibitors, HIV, malignancy). **Protective factors:** intact Th17/Tc17 cellular immunity (Finding 3). **No genetic risk/protective locus is established.** **Gene–environment interaction:** host immune competence × environmental exposure determines whether infection is contained or progresses to severe/disseminated disease.

### 3. Phenotypes
Pulmonary: cough, dyspnea, fever, hemoptysis (HP:0002105), night sweats (HP:0030166), weight loss (HP:0001824), lung mass. Cutaneous: verrucous/ulcerative skin lesions (HP:0200039). Osteoarticular: osteomyelitis (HP:0002754), arthritis. Genitourinary: prostatitis, epididymo-orchitis. CNS: meningitis (HP:0001287), intracranial mass, epidural abscess. Severe: ARDS (HP:0002878), respiratory failure (HP:0002878). Onset is adult-predominant; severity ranges mild to fatal; progression is progressive if untreated.

### 4. Genetic/Molecular Information
**Not applicable to the human host** — no causal gene, no pathogenic human variants, no inheritance. The mechanistically relevant genes are **fungal**: *BAD1* (virulence adhesin) and *DRK1* (dimorphism regulator). No human modifier genes, epigenetic changes, or chromosomal abnormalities are established for susceptibility.

### 5. Environmental Information
Environmental reservoir: moist acidic soil and decaying organic matter near waterways. Lifestyle/occupational factors: forestry, excavation, camping, fishing, hunting. Infectious agent: *Blastomyces dermatitidis* / *B. gilchristii* / *B. percursus* / *B. helicus* (NCBI Taxonomy; fungi, Ascomycota, Onygenales).

### 6. Mechanism / Pathophysiology
See the ordered causal chain below (synthesizes Findings 2, 3, 10).

### 7. Anatomical Structures Affected
Primary: lung (UBERON:0002048). Secondary: skin (UBERON:0002097), bone (UBERON:0002481), genitourinary tract/prostate (UBERON:0002367), CNS (UBERON:0001017). Body systems: respiratory, integumentary, musculoskeletal, genitourinary, nervous. Tissue reaction: pyogranulomatous inflammation.

### 8. Temporal Development
Incubation ~3–6 weeks (up to 3 months); acute or chronic/insidious onset; progressive if untreated; curable over 6–12 months of therapy (≥12 months for CNS/bone). Not relapsing-remitting.

### 9. Inheritance and Population
No inheritance (infectious). Endemic to the Great Lakes basin and Ohio/Mississippi/St. Lawrence River valleys; male predominance; adult-predominant age distribution. Geographic range appears to be broadening (cases now reported in Newfoundland and *B. percursus* in Iran).

### 10. Diagnostics
Culture + histopathology (broad-based budding yeast) = gold standard; urine/serum antigen EIA (cross-reacts with *Histoplasma*); BAD-1 IgG EIA (Sens 50%, Spec 90.2%); PCR/ITS sequencing for species ID; imaging (CT: masses, infiltrates, cavitation). Differential diagnosis: bacterial pneumonia, tuberculosis, lung carcinoma, histoplasmosis, other dimorphic mycoses.

### 11. Outcome/Prognosis
Low overall mortality with treatment; ~40% on mechanical ventilation; ARDS historically 50–90%; transplant 1-year mortality 26.3%. Prognostic factors: age, female sex, immunosuppression, diagnostic delay, ARDS.

### 12. Treatment
Itraconazole (mild–moderate); amphotericin B lipid formulation (severe/CNS/immunocompromised/pregnancy); voriconazole for CNS step-down. Duration 6–12 months. No gene/cell/RNA therapies (not applicable).

### 13. Prevention
Primary prevention: avoid soil disturbance in endemic areas; antifungal prophylaxis is not routinely recommended but considered in high-risk transplant patients. No licensed human vaccine (candidates exist in mouse models). Not a vaccine-preventable disease at present. Public health: awareness and surveillance; environmental risk reduction limited by ubiquitous soil reservoir.

### 14. Other Species / Natural Disease
Dogs (NCBI:txid9615) are the principal natural host and human sentinel; cats and wildlife are also susceptible. Zoonotic transmission is essentially absent (no person-to-person or routine animal-to-person spread); rare direct inoculation (dog bite) reported. Veterinary relevance is high in endemic regions.

### 15. Model Organisms
Mouse (*Mus musculus*, NCBI:txid10090) intranasal/intratracheal pulmonary infection is the standard model and recapitulates pulmonary infection, BAD-1-dependent virulence, and Th17/Tc17 vaccine immunity. Attenuated BAD-1-deleted strains serve as live vaccines. Limitation: mouse models emphasize vaccine immunity and may not fully reproduce human chronic disseminated disease.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Environmental reservoir:** *Blastomyces* grows as a mold in moist, acidic soil and decaying vegetation near waterways → produces airborne conidia.
2. **Soil disturbance / exposure** (excavation, forestry, recreation) → **aerosolizes conidia**, which are **inhaled** into the lung.
3. Conidia reach the alveoli → exposure to **host body temperature (37 °C)** → **DRK1 hybrid histidine kinase** signals the **mold-to-yeast dimorphic switch** (*leads to* yeast-phase conversion, BAD-1 expression, cell-wall remodeling).
4. Yeast phase expresses **BAD-1 adhesin** on its surface → BAD-1 **binds host lung tissue and extracellular matrix** via heparan sulfate (WxxWxxW/TSP-1-like motifs) and **tethers yeast to macrophages** via CR3 and CD14.
5. BAD-1 **suppresses TNF-α** and **blocks T-cell activation** (CD47-dependent, mimicking thrombospondin-1) → **immune evasion** (*results in* reduced IL-12/IFN-γ, increased IL-10).
6. **Branch A — effective host response:** intact **Th17/Tc17 cellular immunity** (mannose-receptor → IL-6/IL-1 → IL-17; neutrophil recruitment) → **containment**, asymptomatic or self-limited infection.
7. **Branch B — impaired host response** (immunosuppression) → uncontrolled replication → **pyogranulomatous pneumonia** → **hematogenous/lymphatic dissemination** to skin, bone, genitourinary tract, and CNS.
8. Severe pulmonary branch → **diffuse alveolar damage / ARDS** → respiratory failure → **~40% mortality on mechanical ventilation** (inferred link between fungal burden, inflammation, and alveolar-capillary injury).
9. **Intervention point:** antifungal therapy (itraconazole or amphotericin B) halts replication → **cure over 6–12 months** if diagnosis is timely; diagnostic delay worsens the ARDS branch.

```
 Soil mold (25°C) --conidia--> INHALATION --> Alveolus
        |                                         |
        |                               [37°C] DRK1 switch
        v                                         v
  (environmental                           YEAST + BAD-1
   reservoir)                                     |
                        +----------------+--------+--------+
                        | heparan-sulfate|  CR3/CD14 bind  |
                        | tissue binding | TNF-a suppress  |
                        +--------+-------+--------+--------+
                                 |                |
                        CD47/TSP-1 T-cell block (immune evasion)
                                 |
                 +---------------+----------------+
                 |                                |
      Th17/Tc17 INTACT                   Th17/Tc17 IMPAIRED
         (containment)                   (immunosuppression)
                 |                                |
        asymptomatic/self-limited      progressive pneumonia
                                                  |
                                    +-------------+-------------+
                                    |                           |
                           DISSEMINATION                  ARDS / resp failure
                     (skin>bone>GU>CNS)              (~40% mortality on MV)
```

**Upstream vs downstream:** The *DRK1* dimorphic switch and *BAD1* expression are the most upstream fungal determinants; host Th17/Tc17 immunity is the upstream determinant of outcome. Downstream events — dissemination, pyogranulomatous tissue injury, and ARDS — are consequences of the balance between fungal virulence and host cellular immunity.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports finding(s) |
|---|---|---|
| [23533607](https://pubmed.ncbi.nlm.nih.gov/23533607/) | *Phylogenetic analysis reveals cryptic species B. gilchristii* | F1 (etiology, cryptic species) |
| [36675937](https://pubmed.ncbi.nlm.nih.gov/36675937/) | *Blastomycosis: mycological and clinical aspects* | F1 (dimorphism, soil reservoir) |
| [23853587](https://pubmed.ncbi.nlm.nih.gov/23853587/) | *Fungal adhesin binds heparin, mimics thrombospondin-1* | F2 (BAD-1 structure/immune evasion) |
| [15585870](https://pubmed.ncbi.nlm.nih.gov/15585870/) | *CR3 for TNF-α suppression, immune evasion* | F2 (macrophage binding, TNF-α) |
| [26396244](https://pubmed.ncbi.nlm.nih.gov/26396244/) | *BAD-1 binding to GAGs enhanced by PDI* | F2 (adhesin mechanism) |
| [16243837](https://pubmed.ncbi.nlm.nih.gov/16243837/) | *Calcium binding by BAD-1* | F2 (BAD-1 biochemistry) |
| [23788728](https://pubmed.ncbi.nlm.nih.gov/23788728/) | *IL-1 enhances vaccine-induced Th17* | F3 (Th17 immunity) |
| [22829762](https://pubmed.ncbi.nlm.nih.gov/22829762/) | *Tc17 cells mediate vaccine immunity in CD4-deficient hosts* | F3 (Tc17 immunity) |
| [26367276](https://pubmed.ncbi.nlm.nih.gov/26367276/) | *MyD88-Akt1-mTOR coordinates Tc17/Tc1* | F3 (Tc17 signaling) |
| [26931447](https://pubmed.ncbi.nlm.nih.gov/26931447/) | *Mannose receptor required for Th17 induction* | F3 (innate sensing) |
| [32227089](https://pubmed.ncbi.nlm.nih.gov/32227089/) | *Outcomes with severe blastomycosis and respiratory failure* | F4 (mortality predictors) |
| [25851019](https://pubmed.ncbi.nlm.nih.gov/25851019/) | *ECMO for blastomycosis-related ARDS* | F4 (ARDS mortality) |
| [16477560](https://pubmed.ncbi.nlm.nih.gov/16477560/) | *Hospitalizations for endemic mycoses* | F4 (crude mortality) |
| [10770729](https://pubmed.ncbi.nlm.nih.gov/10770729/) | *IDSA practice guidelines (2000)* | F5 (treatment) |
| [18462107](https://pubmed.ncbi.nlm.nih.gov/18462107/) | *IDSA blastomycosis guidelines, 2008 update* | F5 (treatment) |
| [20166817](https://pubmed.ncbi.nlm.nih.gov/20166817/) | *CNS blastomycosis: diagnosis and treatment* | F5, F8 (CNS treatment/anatomy) |
| [41553334](https://pubmed.ncbi.nlm.nih.gov/41553334/) | *BAD-1 IgG EIA for diagnosis* | F6 (serology performance) |
| [21749587](https://pubmed.ncbi.nlm.nih.gov/21749587/) | *Histoplasmosis & blastomycosis after SOT* | F6 (urine antigen) |
| [20041579](https://pubmed.ncbi.nlm.nih.gov/20041579/) | *Blastomycosis in urban SE Wisconsin* | F7 (waterway risk) |
| [39731672](https://pubmed.ncbi.nlm.nih.gov/39731672/) | *Blastomycosis in SOT/HCT recipients* | F4, F7 (transplant mortality) |
| [38718236](https://pubmed.ncbi.nlm.nih.gov/38718236/) | *Review of cutaneous blastomycosis in Wisconsin* | F8 (anatomy, skin) |
| [7666297](https://pubmed.ncbi.nlm.nih.gov/7666297/) | *Epidemiology of blastomycosis in dogs* | F9 (canine sentinel) |
| [16805092](https://pubmed.ncbi.nlm.nih.gov/16805092/) | *Non-adhesive mechanisms of BAD1* | F9, F2 (mouse model) |
| [21842181](https://pubmed.ncbi.nlm.nih.gov/21842181/) | *DRK1 global regulator of dimorphism* | F10 (dimorphic switch) |
| [25125734](https://pubmed.ncbi.nlm.nih.gov/25125734/) | *The endemic mimic: blastomycosis misdiagnosed* | F11 (temporal course, mimicry) |

Across the 45 papers reviewed, the evidence base is consistent: multiple independent case series and cohort studies (transplant, HSCT, SLE, ICU) converge on immunosuppression and diagnostic delay as the dominant drivers of severe disease and mortality, while mechanistic mouse and in-vitro work (BAD-1, DRK1, Th17/Tc17) provides a coherent molecular explanation. The donor-derived and transplant reviews (PMID 37991084, 38444820, 29782660) emphasize disseminated disease and high attributable mortality in immunocompromised hosts, reinforcing Findings 3 and 7. Emerging reports of *B. percursus* in Iran (PMID 42470501) and an endogenous case in Newfoundland (PMID 42403492) indicate the geographic range is broadening — possibly with climate change.

**Evidence source types:** Human clinical (epidemiology, outcomes, diagnostics, treatment guidelines); model organism (mouse pulmonary infection for BAD-1/DRK1/Th17-Tc17; dogs as natural hosts); in vitro (BAD-1 biochemistry, adhesion assays); computational (phylogenetics, GIS spatial analysis).

---

## Limitations and Knowledge Gaps

1. **No human causal gene / host genetics unexplored.** Blastomycosis is infectious, so the template's genetic sections (causal genes, pathogenic variants, inheritance, penetrance, carrier frequency) are **not applicable**. No human genetic susceptibility locus has been established, although host immune-gene defects (e.g., in T-cell immunity) are plausible modifiers that have not been systematically mapped by GWAS.
2. **Immunology derived largely from mouse vaccine models.** The Th17/Tc17 protection paradigm comes from murine experiments; direct confirmation of these mechanisms in human natural infection is limited.
3. **Antigen test cross-reactivity.** Urine/serum galactomannan antigen cross-reacts extensively with *Histoplasma* and related dimorphic fungi, limiting specificity; the more specific BAD-1 IgG EIA has only 50% overall sensitivity.
4. **Epidemiology underestimated.** True incidence/prevalence is uncertain because blastomycosis is not nationally reportable in all jurisdictions, most cases are not hospitalized, and diagnostic delay is common. Precise per-100,000 incidence figures are region-specific.
5. **Species-level clinical differences unclear.** The clinical and prognostic implications of infection by *B. gilchristii*, *B. percursus*, or *B. helicus* versus *B. dermatitidis* are not yet well characterized.
6. **No approved human vaccine.** Protective vaccine immunity is established in mice but no licensed human vaccine exists.
7. **ARDS mechanism inferred.** The step linking fungal burden/inflammation to alveolar-capillary injury and ARDS is clinically observed but not mechanistically dissected in humans.

---

## Proposed Follow-up Experiments / Actions

1. **Host genetic susceptibility study.** Conduct a case–control or exome/GWAS analysis of severe vs. self-limited blastomycosis to test whether variants in T-cell/IL-17-axis genes (e.g., *IL17RA*, *CARD9*, *STAT3*, *STAT1*) modify disease severity — addressing the open question of host genetic modifiers.
2. **Species-stratified outcome analysis.** Use PCR/ITS typing to stratify a prospective cohort by *Blastomyces* species and correlate species with dissemination pattern, ARDS risk, and mortality.
3. **Improve diagnostics.** Develop and validate a multiplex antigen/antibody assay (BAD-1-specific plus species-discriminating targets) to overcome *Histoplasma* cross-reactivity and raise sensitivity in acute and immunocompromised disease.
4. **Antifungal prophylaxis trial in high-risk transplant recipients** in endemic regions, given the 26.3% 1-year transplant mortality and association with intensified immunosuppression.
5. **Translate Th17/Tc17 vaccine findings** toward a human vaccine candidate (e.g., attenuated BAD-1-deleted strain or subunit), prioritizing immunosuppressed and occupationally exposed populations.
6. **Climate/geographic surveillance.** Expand soil and sentinel (canine) surveillance beyond the classical Great Lakes/river-valley foci in light of endogenous cases now reported in non-traditional regions (Newfoundland, Iran).
7. **Mechanistic ARDS study.** Characterize the alveolar immune response (single-cell/spatial transcriptomics of lung in the mouse model) during severe infection to define the pathway from fungal burden to diffuse alveolar damage and identify adjunctive host-directed therapy targets.

---

*Report compiled from 11 confirmed findings and 45 reviewed papers over 5 investigation iterations. All mechanistic and clinical claims are cited to primary literature by PMID. Blastomycosis is an infectious disease (MONDO:0005672) with no human causal gene; the mechanistically central genes are the fungal virulence genes BAD1 and DRK1.*


## Artifacts

- [OpenScientist final report](Blastomycosis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Blastomycosis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 28 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 16 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CL:0000625` (2 mentions) - the report calls it "CD8⁺ T cell", "CD4⁺/CD8⁺ T cell"; CL calls it **CD8-positive, alpha-beta T cell**
- `NCIT:C1216` (1 mention) - the report calls it "amphotericin B"; NCIT calls it **Retinyl Acetate**
- `NCIT:C1142` (1 mention) - the report calls it "itraconazole"; NCIT calls it **Lavendustin A**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000899` (1 mention) - the report calls it "Th17 cell"; CL calls it **T-helper 17 cell**, and lists "Th17 cell" among its other names
- `GO:0072539` (1 mention) - the report calls it "Th17 cell differentiation"; GO calls it **T-helper 17 cell differentiation**
- `GO:0032620` (1 mention) - the report calls it "IL-17 production"; GO calls it **interleukin-17 production**, and lists "IL-17 production" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000625` - called "CD8⁺ T cell", "CD4⁺/CD8⁺ T cell"