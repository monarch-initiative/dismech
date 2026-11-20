---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-04T18:25:49.693113'
end_time: '2026-11-04T18:39:09.000345'
duration_seconds: 799.31
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: ACTB-Associated Syndromic Thrombocytopenia
  mondo_id: MONDO:0100433
  category: Mendelian
  causal_genes: ACTB
  omim_id: OMIM:620475
  synonyms: ACTB-AST; ACTB-related syndromic thrombocytopenia; thrombocytopenia 8,
    with dysmorphic features and developmental delay
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
citation_count: 17
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 20
  on_topic: 12
  validator_version: 0.5.1
term_validation:
  total_terms: 22
  verified: 21
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 4
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0100433
    reported_labels:
    - MONDO
    ontology_label: ACTB-associated syndromic thrombocytopenia
  - term_id: HP:0001873
    reported_labels:
    - Laboratory abnormality
    ontology_label: Thrombocytopenia
  - term_id: HP:0000252
    reported_labels:
    - Clinical sign
    ontology_label: Microcephaly
  - term_id: HP:0001999
    reported_labels:
    - Physical
    ontology_label: Abnormal facial shape
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ACTB-Associated_Syndromic_Thrombocytopenia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ACTB-Associated_Syndromic_Thrombocytopenia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ACTB-Associated Syndromic Thrombocytopenia
- **MONDO ID:** MONDO:0100433 (if available)
- **Causal gene(s):** ACTB
- **OMIM:** OMIM:620475
- **Synonyms:** ACTB-AST; ACTB-related syndromic thrombocytopenia; thrombocytopenia 8, with dysmorphic features and developmental delay
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **ACTB-Associated Syndromic Thrombocytopenia** covering all of the
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

# ACTB-Associated Syndromic Thrombocytopenia (THC8): Comprehensive Disease Report

**Disease:** ACTB-Associated Syndromic Thrombocytopenia (ACTB-AST)
**Causal gene:** **ACTB** (β-cytoplasmic/non-muscle actin; HGNC:132; chromosome 7p22.1)
**MONDO:** MONDO:0100433 | **OMIM:** 620475 (THROMBOCYTOPENIA 8, WITH DYSMORPHIC FEATURES AND DEVELOPMENTAL DELAY; THC8)
**Synonyms:** ACTB-AST; ACTB-related syndromic thrombocytopenia; Thrombocytopenia 8, with dysmorphic features and developmental delay
**Category:** Mendelian, autosomal dominant

---

## Summary

**ACTB-Associated Syndromic Thrombocytopenia is caused by heterozygous missense variants in *ACTB*, the gene encoding β-cytoplasmic (non-muscle) actin.** The disease-defining lesions cluster in the C-terminal 3′-coding region of the gene (exons 5 and 6). This distinguishes ACTB-AST at the molecular level from Baraitser-Winter cerebrofrontofacial syndrome (BWCFF), which is caused by missense variants elsewhere in *ACTB* (and in the paralog *ACTG1*). ACTB-AST is one of at least eight clinically distinct disorders that arise from the *ACTB*/*ACTG1* "non-muscle actinopathy" spectrum, in which the position and functional class of the variant dictate the resulting phenotype and its severity.

The core clinical triad reported in the defining cohort is **congenital thrombocytopenia with platelet anisotropy (variable platelet size), microcephaly, and mild developmental disability.** Mechanistically, the C-terminal β-actin variants are not simple loss-of-function alleles. Patient-derived fibroblasts and thrombocytes show cohort-specific alterations in β-cytoplasmic actin filament populations, including enhanced recruitment of thrombocytopenia-associated actin-binding proteins (ABPs). In megakaryocytes, this perturbed actin behavior compromises microtubule organization and thereby inhibits the final stages of platelet maturation. ACTB-AST thrombocytopenia is therefore best understood as a **production-type (biogenesis) defect**, rather than an immune-mediated platelet destruction disorder.

Because complete loss of β-actin is embryonic-lethal in mice, the human disorders are necessarily heterozygous and dominant-acting. There is no curative or disease-specific therapy; management is supportive (bleeding precautions, platelet transfusion for hemostatic challenges such as surgery, and developmental/rehabilitative therapies) together with genetic counseling. Diagnosis rests on identifying the characteristic C-terminal *ACTB* missense variant by exome/genome sequencing or inherited-thrombocytopenia/intellectual-disability gene panels, supported by a peripheral blood smear showing thrombocytopenia with platelet anisotropy. The emerging management paradigm for the entire *ACTB*/*ACTG1* spectrum is **variant-level, genotype-driven characterization**. This report is assembled primarily from aggregated, disease-level literature (OMIM, primary cohort reports, and mechanistic reviews) rather than individual EHR records; the foundational cohort is small (six patients), so frequency and natural-history estimates are provisional.

---

## 1. Disease Information

**Overview.** ACTB-Associated Syndromic Thrombocytopenia (THC8) is an ultra-rare autosomal-dominant Mendelian disorder in which heterozygous missense variants in the C-terminal portion of *ACTB* (β-cytoplasmic actin) produce a syndromic form of inherited thrombocytopenia accompanied by microcephaly and mild developmental disability. The defining report described six patients with heterozygous variants clustered in the 3′-coding region of *ACTB* (exons 5 and 6), and emphasized that their clinical features are *distinct* from Baraitser-Winter cerebrofrontofacial syndrome ([PMID: 30315159](https://pubmed.ncbi.nlm.nih.gov/30315159/)): *"Here, we report six patients with previously undescribed heterozygous variants clustered in the 3'-coding region of ACTB. Patients present with clinical features distinct from BWCFF, including mild developmental disability, microcephaly, and thrombocytopenia with platelet anisotropy."*

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | 620475 (THC8) |
| MONDO | MONDO:0100433 |
| Causal gene | *ACTB*, HGNC:132, NCBI Gene 60, UniProt P60709 |
| Cytogenetic locus | 7p22.1 |
| ICD-10 (closest) | D69.4x (other primary thrombocytopenia) — no ACTB-AST-specific code |
| ICD-11 (closest) | 3B64.1 (congenital/hereditary thrombocytopenia) — no specific code |
| Orphanet | No distinct ACTB-AST entry identified; related actinopathies under Baraitser-Winter spectrum |
| MeSH (closest) | Thrombocytopenia (D013921); no specific descriptor |

**Synonyms / alternative names.** ACTB-AST; ACTB-related syndromic thrombocytopenia; Thrombocytopenia 8, with dysmorphic features and developmental delay (THC8).

**Information source type.** Primarily **aggregated, disease-level** evidence (OMIM, the Latham et al. primary cohort, and reviews of *ACTB*/*ACTG1* non-muscle actinopathies). Not derived from large EHR datasets; the evidence base is a small number of individually reported patients.

---

## 2. Etiology

**Primary cause — genetic.** The disease is monogenic: heterozygous, typically *de novo* missense variants in the 3′-coding region (exons 5–6, C-terminus) of *ACTB* ([PMID: 30315159](https://pubmed.ncbi.nlm.nih.gov/30315159/)). There is no infectious or environmental cause of the primary disorder.

**Genetic risk factors.** The causal variant *is* the disease determinant; there are no known susceptibility loci or polygenic contributions. Within the broader *ACTB*/*ACTG1* actinopathy spectrum, the specific variant determines which of ≥8 disorders results and how severe it is ([PMID: 41529692](https://pubmed.ncbi.nlm.nih.gov/41529692/)).

**Environmental / lifestyle risk factors.** None established. As a congenital Mendelian condition, there are no recognized toxic, occupational, dietary, or lifestyle risk factors. Advanced paternal age is a general (non-specific) consideration for *de novo* variants but has not been specifically studied here.

**Protective factors.** No genetic modifier alleles or environmental protective factors have been identified. The only "protective" genetic consideration is the general observation that biallelic loss of β-actin is incompatible with life (see §4, §15), constraining observed disease to heterozygous states.

**Gene–environment interactions.** None described. The phenotype is driven by the germline variant and its intrinsic effect on actin dynamics.

---

## 3. Phenotypes

The defining cohort (n=6) reported a consistent syndromic combination. Frequencies below are qualitative given the small sample.

| Phenotype | Type | Suggested HPO | Onset | Severity | Frequency (cohort) |
|---|---|---|---|---|---|
| Thrombocytopenia | Laboratory abnormality | HP:0001873 | Congenital/neonatal | Mild–moderate | Core / near-universal |
| Platelet anisotropy (variable platelet size) | Laboratory/morphologic | HP:0011877 (anisocytosis of platelets) | Congenital | — | Core feature |
| Microcephaly | Clinical sign | HP:0000252 | Congenital | Variable | Common |
| Mild developmental disability / intellectual disability | Behavioral/developmental | HP:0001263; HP:0001249 | Childhood | Mild | Common |
| Facial dysmorphism (reported across ACTB pLoF-type patients) | Physical | HP:0001999 | Congenital | Mild | Variable |

**Phenotype characteristics.** Onset is congenital; thrombocytopenia is present from the neonatal period and is non-progressive (a stable production defect rather than progressive marrow failure). Severity is at the milder end of the actinopathy spectrum — explicitly contrasted with the severe cortical malformations and dysmorphism of BWCFF ([PMID: 30315159](https://pubmed.ncbi.nlm.nih.gov/30315159/); [PMID: 42107038](https://pubmed.ncbi.nlm.nih.gov/42107038/)). The related ACTB predicted-loss-of-function (pLoF) group shows mild developmental abnormalities and immunological symptoms, with facial dysmorphism distinct from BWCFF ([PMID: 42107038](https://pubmed.ncbi.nlm.nih.gov/42107038/)).

**Quality-of-life impact.** No formal EQ-5D/SF-36/PROMIS data exist for ACTB-AST. Inferred impact: bleeding risk (bruising, mucocutaneous bleeding, perioperative hemorrhage) from thrombocytopenia, plus developmental/learning support needs from mild intellectual disability. Microcephaly may carry additional neurodevelopmental impact.

---

## 4. Genetic / Molecular Information

**Causal gene.** *ACTB* (β-cytoplasmic actin), 7p22.1; HGNC:132; NCBI Gene 60; UniProt P60709.

**Pathogenic variants.**
- **Location/class:** Heterozygous **missense** variants clustered in the **3′-coding region (exons 5 and 6)**, encoding the C-terminus of β-cytoplasmic actin ([PMID: 30315159](https://pubmed.ncbi.nlm.nih.gov/30315159/)).
- **Classification:** Pathogenic / likely pathogenic by ACMG/AMP criteria (de novo occurrence, absent from population databases, clustering in a functional hotspot, concordant phenotype).
- **Allele frequency:** Effectively absent from gnomAD and other population databases (private, de novo).
- **Origin:** Germline; reported as **de novo** (autosomal dominant).
- **Functional consequence:** Not a simple null. The C-terminal variants act through altered actin filament dynamics and aberrant actin-binding-protein (ABP) recruitment — a dominant, gain-of-abnormal-function/dominant-negative-like effect on the cytoskeleton rather than classic haploinsufficiency ([PMID: 30315159](https://pubmed.ncbi.nlm.nih.gov/30315159/)).

**Relationship to other *ACTB* variant classes.** The C-terminal missense ACTB-AST variants are distinct from:
- **BWCFF-type missense variants** (elsewhere in *ACTB*/*ACTG1*) that dysregulate actin polymerization–depolymerization and cause neuronal migration defects — the severe end of the spectrum ([PMID: 41529692](https://pubmed.ncbi.nlm.nih.gov/41529692/)): *"A subset of disease-associated missense variants causes dysregulated actin polymerization-depolymerization and neuronal migration defects. In contrast, nonsense, frameshift, and missense variants enhancing protein degradation cause milder phenotypes or are benign."*
- **True loss-of-function *ACTB* alleles** (deletions, nonsense, frameshift) causing a separate pleiotropic developmental disorder with reduced *ACTB* mRNA ([PMID: 29220674](https://pubmed.ncbi.nlm.nih.gov/29220674/)): *"We describe heterozygous ACTB deletions and nonsense and frameshift mutations in 33 individuals with developmental delay, apparent intellectual disability, increased frequency of internal organ malformations."*
- **ACTB pLoF missense/in-frame deletions** (e.g., G302A, S338-I341del) that reduce protein stability/expression and modulate cytoskeletal reorganization ([PMID: 42887317](https://pubmed.ncbi.nlm.nih.gov/42887317/)).

**Variant-specific phenotype illustration.** The recurrent de novo *ACTB* **p.Ser348Leu** variant causes a *different* C-terminal-region syndrome — syndromic neonatal diabetes with hearing loss, neurodevelopmental features, and intestinal atresia — and notably, *"None of the 96 cases with other ACTB pathogenic variants in the Human Gene Mutation Database had diabetes"* ([PMID: 42107907](https://pubmed.ncbi.nlm.nih.gov/42107907/)). This underscores that ACTB-AST is defined by *particular* C-terminal variants, not by any C-terminal variant.

**Modifier genes / epigenetics / chromosomal abnormalities.** None specifically established for ACTB-AST. Thrombocytopenia-associated ABPs are mechanistic partners (see §6) rather than formal modifier loci.

---

## 5. Environmental Information

No environmental factors, lifestyle factors, or infectious agents are implicated in the causation of ACTB-AST. The disorder is a congenital, germline, monogenic condition. Environmental considerations are limited to **avoiding bleeding risk** (e.g., antiplatelet agents such as NSAIDs/aspirin, contact-injury exposure) as a management consideration rather than an etiologic factor.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A **heterozygous de novo missense variant** in the C-terminal 3′-coding region (exons 5–6) of *ACTB* **results in** production of a structurally altered β-cytoplasmic actin monomer. *(Demonstrated — variant identification.)*
2. The mutant β-actin **leads to** cohort-specific changes in β-cytoplasmic actin filament populations in patient cells (fibroblasts, thrombocytes). *(Demonstrated — patient-cell imaging + in silico modeling.)*
3. These altered filaments **result in** enhanced/aberrant recruitment of **thrombocytopenia-associated actin-binding proteins (ABPs)**. *(Demonstrated.)*
4. Perturbed actin dynamics and ABP engagement **compromise microtubule organization** within maturing megakaryocytes (actin–microtubule crosstalk is essential for platelet biogenesis). *(Demonstrated in patient megakaryocytes/thrombocytes.)*
5. Disrupted actin–microtubule coordination **inhibits the final stages of platelet maturation** (proplatelet formation/terminal platelet release). *(Demonstrated — co-examination of actin and microtubule constituents.)*
6. Impaired terminal maturation **leads to** reduced and size-variable platelet output → **congenital thrombocytopenia with platelet anisotropy** (a production-type defect). *(Demonstrated clinically.)*
7. In parallel, altered β-actin cytoskeletal function in neural/developmental tissues **contributes to** **microcephaly and mild developmental disability**. *(Inferred — consistent with β-actin's essential developmental roles; not fully mechanistically dissected for this variant class.)*

```
ACTB C-terminal missense (exons 5-6)
          │
          ▼
 Altered β-cytoplasmic actin monomer / filament populations
          │
          ├────────────► Enhanced recruitment of thrombocytopenia-associated ABPs
          │                               │
          ▼                               ▼
 Compromised microtubule organization in megakaryocytes
          │
          ▼
 Inhibited FINAL stages of platelet maturation (production defect)
          │
          ├──────────────► Thrombocytopenia
          └──────────────► Platelet anisotropy

 (parallel branch, inferred)
 Altered β-actin function in neurodevelopment ──► microcephaly, mild developmental disability
```

### Mechanistic detail

- **Molecular pathways / cellular processes.** The core process is **actin cytoskeleton organization and dynamics** (GO:0030036 actin cytoskeleton organization; GO:0007010 cytoskeleton organization) coordinated with **microtubule organization** (GO:0000226) during **platelet formation** (GO:0030220) and **megakaryocyte differentiation** (GO:0030219). The general principle is established: *"Rearrangements of the microtubule (MT) and actin cytoskeleton are pivotal for platelet biogenesis. Hence, defects in actin- or MT-regulatory proteins are associated with platelet disorders in humans and mice"* ([PMID: 32407474](https://pubmed.ncbi.nlm.nih.gov/32407474/)). Supporting megakaryocyte biology: Cdc42/Pak-dependent F-actin dynamics structure the demarcation membrane system ([PMID: 26991240](https://pubmed.ncbi.nlm.nih.gov/26991240/)), and the spectrin-based membrane skeleton is required for proplatelet/platelet formation ([PMID: 21566095](https://pubmed.ncbi.nlm.nih.gov/21566095/)).
- **Protein dysfunction.** C-terminal substitutions alter β-actin's filament behavior and its interaction surface for ABPs rather than abolishing the protein — a dominant perturbation of cytoskeletal function. Key supporting statements from the defining paper: *"these β-CYA mutations inhibit the final stages of platelet maturation by compromising microtubule organization"* and the variants cause *"the enhanced recruitment of thrombocytopenia-associated actin binding proteins (ABPs)"* ([PMID: 30315159](https://pubmed.ncbi.nlm.nih.gov/30315159/)). (Contrast: pLoF variants reduce protein stability/expression — [PMID: 42887317](https://pubmed.ncbi.nlm.nih.gov/42887317/); [PMID: 42107038](https://pubmed.ncbi.nlm.nih.gov/42107038/).)
- **Cytoskeletal reorganization evidence (related variants).** ACTB pLoF variants (G302A, S338-I341del) modulate focal adhesions, cell stiffness, and cofilin/myosin-light-chain phosphorylation in patient fibroblasts — demonstrating that C-terminal/pLoF ACTB variants reshape cytoskeletal mechanics and regulatory signaling ([PMID: 42887317](https://pubmed.ncbi.nlm.nih.gov/42887317/)).
- **Immune involvement.** Thrombocytopenia here is **production-type, not immune-mediated**. (The related ACTB pLoF group can show immunological symptoms — [PMID: 42107038](https://pubmed.ncbi.nlm.nih.gov/42107038/) — but this is not the primary ACTB-AST mechanism.)
- **Subcellular localization.** Cytoplasmic actin cytoskeleton (GO:0015629 actin cytoskeleton; GO:0005856 cytoskeleton); cortical/submembranous networks of megakaryocytes and platelets.

**Cell types (CL):** megakaryocyte (CL:0000556), platelet/thrombocyte (CL:0000233), and fibroblast (CL:0000057, as experimental model tissue). **Anatomical process:** platelet biogenesis in bone marrow.

---

## 7. Anatomical Structures Affected

**Organ/system level.**
- **Hematopoietic system / bone marrow** (UBERON:0002371 bone marrow; UBERON:0000178 blood) — primary site of defective platelet production.
- **Blood / circulating platelets** — site of the measurable thrombocytopenia and anisotropy.
- **Central nervous system / brain** (UBERON:0000955) — microcephaly and developmental disability (secondary developmental involvement).

**Tissue and cell level.**
- Megakaryocytes (CL:0000556) in bone marrow; platelets (CL:0000233) in peripheral blood.
- Patient **fibroblasts** (CL:0000057) used as the accessible cell model demonstrating altered β-actin filament populations.

**Subcellular level.**
- **Actin cytoskeleton** (GO:0015629) and **microtubule cytoskeleton** (GO:0005874); cortical cytoplasm of megakaryocytes/platelets.

**Localization / lateralization.** Systemic (not lateralized). Thrombocytopenia is a whole-blood finding; microcephaly is a bilateral/symmetric craniofacial feature.

---

## 8. Temporal Development

- **Onset.** Congenital. Thrombocytopenia is present from the neonatal period; microcephaly is congenital; developmental disability becomes apparent through childhood. Onset pattern is **chronic/congenital**, not acute.
- **Progression.** The thrombocytopenia reflects a fixed production defect and is best characterized as **stable/non-progressive** rather than progressive marrow failure. Developmental disability is static (a developmental, not neurodegenerative, condition).
- **Disease course.** Lifelong (chronic). No relapsing-remitting pattern; no spontaneous remission expected because the defect is constitutional.
- **Critical periods.** Perioperative and traumatic/bleeding-risk windows are the principal clinically actionable periods (need for platelet support). Early childhood is the window for developmental/educational intervention.

---

## 9. Inheritance and Population

- **Inheritance pattern.** Autosomal dominant; variants reported as **de novo** ([PMID: 30315159](https://pubmed.ncbi.nlm.nih.gov/30315159/)).
- **Penetrance / expressivity.** Presumed high penetrance for the carried variant; expressivity across the small cohort appears relatively consistent for the core triad, though the overall *ACTB*/*ACTG1* spectrum shows marked variant-dependent expressivity ([PMID: 41529692](https://pubmed.ncbi.nlm.nih.gov/41529692/)).
- **Epidemiology.** **Ultra-rare.** No formal prevalence/incidence estimates exist; the defining cohort comprised six patients. No population-based registry data.
- **Why only heterozygous/dominant.** Complete β-actin knockout is embryonic-lethal in mice, so biallelic LoF is incompatible with human life, constraining all observed *ACTB* disorders to the heterozygous state ([PMID: 21900491](https://pubmed.ncbi.nlm.nih.gov/21900491/)): *"We generated whole-body β-actin-knockout (Actb(-/-)) mice and demonstrated that β-actin is required for early embryonic development."*
- **Anticipation / mosaicism / founder effects / consanguinity / carrier frequency.** No genetic anticipation (not a repeat-expansion disorder). De novo origin means consanguinity and carrier frequency are not relevant; germline mosaicism is theoretically possible (documented for the allelic BWCFF — [PMID: 32506774](https://pubmed.ncbi.nlm.nih.gov/32506774/)) but not specifically reported for ACTB-AST. No founder effects.
- **Demographics.** No sex predilection or ethnic/geographic clustering reported given the small numbers.

---

## 10. Diagnostics

**Recommended approach.** Diagnosis is **molecular**, achieved by identifying the characteristic C-terminal (exons 5–6) *ACTB* missense variant, combined with hematologic confirmation of thrombocytopenia with platelet anisotropy.

**Clinical/laboratory tests.**
- **Complete blood count** with platelet count: thrombocytopenia (HP:0001873; LOINC platelet count 777-3).
- **Peripheral blood smear**: platelet anisotropy / variable platelet size (HP:0011877).
- Mean platelet volume (MPV) and platelet morphology review support the production-type picture.

**Genetic testing (GTR/GeneReviews paradigm).**
- **Whole-exome sequencing (WES)** or **whole-genome sequencing (WGS)** — highest-yield, able to detect the de novo missense variant and exclude phenocopies.
- **Inherited-thrombocytopenia gene panels** and/or **intellectual-disability panels** that include *ACTB*.
- **Single-gene *ACTB* sequencing** when the syndrome is clinically suspected.
- Chromosomal microarray/karyotype/FISH are generally uninformative (no large structural lesion); mitochondrial and repeat-expansion testing are not applicable.

**Clinical criteria / differential diagnosis.** No formal consensus criteria. Key differentials:
- **Baraitser-Winter cerebrofrontofacial syndrome** (ACTB/ACTG1 missense elsewhere; severe cortical malformation, coloboma, distinctive facies — [PMID: 30315159](https://pubmed.ncbi.nlm.nih.gov/30315159/), [PMID: 27625340](https://pubmed.ncbi.nlm.nih.gov/27625340/)).
- **ACTB loss-of-function pleiotropic developmental disorder** (deletions/nonsense/frameshift — [PMID: 29220674](https://pubmed.ncbi.nlm.nih.gov/29220674/)).
- Other **inherited thrombocytopenias** (e.g., MYH9-related disease and other giant-platelet syndromes — [PMID: 18278172](https://pubmed.ncbi.nlm.nih.gov/18278172/)); other actin/ABP-related platelet disorders.
- *ACTB* p.Ser348Leu syndromic neonatal diabetes ([PMID: 42107907](https://pubmed.ncbi.nlm.nih.gov/42107907/)) — different C-terminal variant, different syndrome.

**Screening.** Cascade testing is largely moot given de novo origin; targeted variant testing can be offered to confirm de novo status and inform recurrence risk.

---

## 11. Outcome / Prognosis

- **Survival / mortality.** No disease-specific mortality data. The thrombocytopenia is mild-to-moderate and production-type; life expectancy is not clearly reduced, though bleeding risk exists during surgery/trauma. No evidence base for 5-/10-year survival figures (not a malignancy).
- **Morbidity / function.** Chief morbidities are **bleeding tendency** (bruising, mucocutaneous and perioperative bleeding) and **neurodevelopmental** impact (mild intellectual disability, microcephaly-related).
- **Disease course / complications.** Chronic, stable course. Complications are bleeding events under hemostatic challenge and developmental/educational needs.
- **Recovery potential.** The underlying defect is not reversible; supportive measures mitigate complications. Developmental outcomes are generally in the mild range.
- **Prognostic factors.** The **specific variant** is the dominant prognostic determinant across the *ACTB*/*ACTG1* spectrum — variant class predicts severity and organ involvement ([PMID: 41529692](https://pubmed.ncbi.nlm.nih.gov/41529692/)). Severity of thrombocytopenia and any additional organ features further modulate prognosis.

> **Caveat on malignancy:** Somatic *ACTB* mutations occur in certain neoplasms (e.g., tubular adenomas of the breast codon-95 hotspot — [PMID: 41456879](https://pubmed.ncbi.nlm.nih.gov/41456879/); MiT-fusion PEComas — [PMID: 42331846](https://pubmed.ncbi.nlm.nih.gov/42331846/)), and AML has been reported in the allelic BWCFF ([PMID: 27868373](https://pubmed.ncbi.nlm.nih.gov/27868373/)). A specific cancer predisposition for ACTB-AST is **not established**; this remains an open question.

---

## 12. Treatment

**No curative or disease-specific therapy exists.** Management is **supportive and genotype-informed** ([PMID: 41529692](https://pubmed.ncbi.nlm.nih.gov/41529692/); [PMID: 30315159](https://pubmed.ncbi.nlm.nih.gov/30315159/)).

**Supportive / hematologic.**
- **Bleeding precautions**; avoid antiplatelet agents (NSAIDs/aspirin) where possible.
- **Platelet transfusion** for significant bleeding or hemostatic challenge (surgery, trauma, delivery) — NCIT "Platelet Transfusion" (C15360).
- Antifibrinolytics (e.g., tranexamic acid) are a reasonable adjunct for mucosal bleeding by analogy to other inherited thrombocytopenias (not ACTB-AST-specific evidence).

**Developmental / rehabilitative.**
- Early-intervention, special education, physical/occupational/speech therapy for developmental disability (NCIT "Rehabilitation Therapy" C15917; "Supportive Care" C15277).

**Advanced/experimental therapeutics.** None. No gene therapy, cell therapy, RNA-based therapy, or targeted therapy is available or in trials for ACTB-AST. **No ACTB-AST-specific clinical trials are registered.**

**Pharmacogenomics.** Not applicable (no disease-specific drug).

**Treatment strategy.** The authoritative framework is **variant-level, genotype-driven management** — the *ACTB*/*ACTG1* correlation work provides *"a template for the personalized genetic variant-level-driven management of the pleiotropic allelic single-gene disorders"* ([PMID: 41529692](https://pubmed.ncbi.nlm.nih.gov/41529692/)).

---

## 13. Prevention

- **Primary prevention.** None possible for a de novo germline Mendelian disorder.
- **Secondary prevention.** Early diagnosis to institute bleeding precautions and developmental support; preoperative platelet count assessment and planning.
- **Tertiary prevention.** Prevent bleeding complications (avoid antiplatelet drugs, pre-procedure platelet support); optimize developmental outcomes through early intervention.
- **Genetic counseling.** Recommended. De novo origin implies low recurrence risk for parents, but germline mosaicism cannot be fully excluded; affected individuals carry 50% transmission risk. Prenatal/preimplantation testing is feasible once the familial variant is known.
- **Immunization / public health / environmental interventions.** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs.** *ACTB* is highly conserved. Mouse ortholog *Actb* (NCBI Gene 11461; NCBI Taxon 10090); β-actin is essential across vertebrates.
- **Natural disease in other species.** No naturally occurring animal homolog of ACTB-AST is documented in OMIA; the evidence comes from engineered mouse models (see §15).
- **Comparative biology / conservation.** β-actin's roles in cell growth, migration, and the G-actin pool are evolutionarily conserved, so disease mechanisms are expected to be conserved at the cellular level ([PMID: 21900491](https://pubmed.ncbi.nlm.nih.gov/21900491/)).
- **Zoonotic potential.** Not applicable (non-infectious genetic disorder).

---

## 15. Model Organisms

- **Mouse (*Mus musculus*, NCBI Taxon 10090).** Whole-body β-actin knockout (*Actb*⁻/⁻) mice are **embryonic-lethal**: *"We generated whole-body β-actin-knockout (Actb(-/-)) mice and demonstrated that β-actin is required for early embryonic development"* ([PMID: 21900491](https://pubmed.ncbi.nlm.nih.gov/21900491/)). *Actb*⁻/⁻ MEFs showed severe growth impairment and migration defects (not seen in γ-actin-null MEFs), with altered G-actin/F-actin ratio and changed cell-cycle/motility gene expression — establishing β-actin's unique, non-redundant cellular functions.
- **Patient-derived cellular models (in vitro).** Patient **fibroblasts** demonstrate cohort-specific β-actin filament changes and enhanced ABP recruitment ([PMID: 30315159](https://pubmed.ncbi.nlm.nih.gov/30315159/)); ACTB pLoF fibroblasts (G302A, S338-I341del) reveal altered stiffness, focal adhesions, and cofilin/MLC phosphorylation ([PMID: 42887317](https://pubmed.ncbi.nlm.nih.gov/42887317/)). Patient **megakaryocytes/thrombocytes** were used to demonstrate the microtubule-organization defect.
- **Model characteristics / limitations.** The embryonic-lethal full knockout cannot model the heterozygous, dominant-acting missense human disease; **knock-in of specific C-terminal variants** would be required to recapitulate ACTB-AST. No such disease-specific knock-in model is reported. Megakaryocyte culture systems (e.g., from murine fetal liver) are available tools for platelet-biogenesis studies ([PMID: 22130704](https://pubmed.ncbi.nlm.nih.gov/22130704/)).
- **Resources.** MGI (*Actb*), IMPC, and standard megakaryocyte/iPSC-derived platelet culture platforms.

---

## Mechanistic Model / Interpretation

ACTB-AST sits in the **middle of the non-muscle actinopathy severity spectrum**. The organizing principle, now formalized across *ACTB*/*ACTG1*, is that **the variant's position and functional class determine the disorder**:

| Variant class | Molecular effect | Representative disorder | Severity |
|---|---|---|---|
| Missense, polymerization-dysregulating | Dysregulated actin polymerization/depolymerization; neuronal migration defects | Baraitser-Winter CFF syndrome | Severe |
| **Missense, C-terminal (exons 5–6)** | **Altered filament dynamics; aberrant ABP recruitment; disrupted actin–MT crosstalk** | **ACTB-AST (THC8)** | **Mild–moderate, syndromic** |
| Specific C-terminal (e.g., p.Ser348Leu) | Variant-specific functional change | Syndromic neonatal diabetes | Variable, organ-specific |
| Nonsense/frameshift/deletion (true LoF) | Reduced *ACTB* mRNA/protein | ACTB pLoF pleiotropic developmental disorder | Mild, distinct facies, immune features |

The thrombocytopenia is the discriminating feature of ACTB-AST and is mechanistically a **platelet-production (biogenesis) defect**, not peripheral destruction. The mutant β-actin perturbs the actin filament populations that must coordinate with the microtubule marginal band and demarcation membrane system during terminal megakaryocyte maturation. Because *"defects in actin- or MT-regulatory proteins are associated with platelet disorders"* ([PMID: 32407474](https://pubmed.ncbi.nlm.nih.gov/32407474/)), a C-terminal β-actin lesion that enhances recruitment of thrombocytopenia-associated ABPs and compromises microtubule organization logically truncates the final step of proplatelet/platelet release — yielding fewer, size-variable platelets (anisotropy).

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [30315159](https://pubmed.ncbi.nlm.nih.gov/30315159/) | *Variants in exons 5 and 6 of ACTB cause syndromic thrombocytopenia* | **Defining paper**: variant location, phenotype, mechanism (ABP recruitment, microtubule/maturation defect) |
| [41529692](https://pubmed.ncbi.nlm.nih.gov/41529692/) | *Molecular genotype-phenotype correlation in ACTB/ACTG1 non-muscle actinopathies* | ≥8-disorder spectrum; variant-class→severity; variant-level management paradigm |
| [29220674](https://pubmed.ncbi.nlm.nih.gov/29220674/) | *ACTB Loss-of-Function Mutations Result in a Pleiotropic Developmental Disorder* | Distinguishes true-LoF *ACTB* disorder from ACTB-AST |
| [42887317](https://pubmed.ncbi.nlm.nih.gov/42887317/) | *Non-muscle actinopathy-associated LoF actin variants modulate cytoskeletal reorganization* | Cellular mechanism of ACTB pLoF variants (focal adhesions, cofilin/MLC) |
| [42107907](https://pubmed.ncbi.nlm.nih.gov/42107907/) | *ACTB p.Ser348Leu in syndromic neonatal diabetes* | Variant-specificity within C-terminal region |
| [42107038](https://pubmed.ncbi.nlm.nih.gov/42107038/) | *Overview of cytoskeletal actin mutations (review)* | Spectrum framing; pLoF group features |
| [21900491](https://pubmed.ncbi.nlm.nih.gov/21900491/) | *β-Actin specifically controls cell growth, migration, and the G-actin pool* | Essentiality; embryonic lethality of KO; why disease is heterozygous |
| [32407474](https://pubmed.ncbi.nlm.nih.gov/32407474/) | *Actin/microtubule crosstalk during platelet biogenesis* | General principle linking actin/MT defects to platelet disorders |
| [26991240](https://pubmed.ncbi.nlm.nih.gov/26991240/) | *Cdc42-dependent F-actin dynamics in megakaryocytes* | F-actin role in demarcation membrane system |
| [21566095](https://pubmed.ncbi.nlm.nih.gov/21566095/) | *Spectrin-based membrane skeleton in platelet formation* | Cytoskeletal requirement for proplatelet/platelet formation |
| [22130704](https://pubmed.ncbi.nlm.nih.gov/22130704/) | *Visualization/manipulation of megakaryocyte cytoskeleton* | Methodological model for platelet biogenesis studies |
| [18278172](https://pubmed.ncbi.nlm.nih.gov/18278172/) | *Congenital disorders associated with platelet dysfunctions* | Differential diagnosis context (giant-platelet/production disorders) |
| [27625340](https://pubmed.ncbi.nlm.nih.gov/27625340/), [27096712](https://pubmed.ncbi.nlm.nih.gov/27096712/), [32588558](https://pubmed.ncbi.nlm.nih.gov/32588558/), [32506774](https://pubmed.ncbi.nlm.nih.gov/32506774/), [35054877](https://pubmed.ncbi.nlm.nih.gov/35054877/) | BWCFF clinical reports | Differential diagnosis; germline mosaicism; expressivity |
| [27868373](https://pubmed.ncbi.nlm.nih.gov/27868373/), [41456879](https://pubmed.ncbi.nlm.nih.gov/41456879/), [42331846](https://pubmed.ncbi.nlm.nih.gov/42331846/) | Actinopathy/somatic-ACTB neoplasia | Open question of malignancy association |

**Evidence source types:** human clinical cohort (30315159), human genomic/molecular review (41529692, 42107038), in-vitro patient-cell (42887317, 30315159), model organism (21900491), and megakaryocyte biology (32407474, 26991240, 21566095, 22130704).

---

## Limitations and Knowledge Gaps

1. **Small defining cohort (n=6).** Frequency, penetrance, expressivity, and natural-history estimates are provisional; precise phenotype frequencies (e.g., % with microcephaly vs ID) are not robustly quantified.
2. **No epidemiology.** No prevalence/incidence data; no registry; no sex/ethnic/geographic data.
3. **Mechanism partly inferred.** The thrombocytopenia mechanism (ABP recruitment → microtubule disorganization → impaired terminal maturation) is directly supported, but the neurodevelopmental branch (microcephaly, ID) is inferred from β-actin's general developmental roles rather than variant-specific experiments.
4. **No ACTB-AST-specific animal model.** Only embryonic-lethal global KO exists; no knock-in of the C-terminal variants.
5. **No therapeutics or trials.** No disease-specific treatment, biomarker-driven therapy, or registered clinical trial.
6. **Malignancy risk unresolved.** Somatic *ACTB* mutations occur in some tumors and AML has been reported in allelic BWCFF, but germline ACTB-AST cancer risk is unknown.
7. **Ontology/identifier gaps.** No dedicated ICD-10/11, Orphanet, or MeSH code; mapping relies on parent "thrombocytopenia" terms.

---

## Proposed Follow-up Experiments / Actions

1. **Expand the patient cohort** via GeneMatcher/Matchmaker Exchange to refine genotype–phenotype correlation, phenotype frequencies, and natural history.
2. **Generate variant-specific knock-in mouse and iPSC-megakaryocyte models** of the C-terminal *ACTB* variants to directly test the proplatelet-formation defect and quantify platelet output.
3. **Define the ABP interactome** of mutant vs wild-type β-actin (e.g., proximity-labeling proteomics) to identify the specific thrombocytopenia-associated ABPs recruited.
4. **Live-imaging of actin–microtubule crosstalk** in patient-derived megakaryocytes during proplatelet formation to pinpoint the maturation-arrest step.
5. **Systematically assess neurodevelopmental and microcephaly mechanisms** in neuronal models derived from patient iPSCs.
6. **Evaluate malignancy surveillance need** by aggregating longitudinal outcomes across the actinopathy spectrum.
7. **Formalize diagnostic criteria and ontology coverage** (dedicated MONDO child, HPO frequency annotations, ICD-11 extension code).

---

*Report compiled from aggregated, disease-level literature. Primary evidence anchor: Latham et al. (2018), [PMID: 30315159](https://pubmed.ncbi.nlm.nih.gov/30315159/). Spectrum/management framework: Di Donato et al. (2026), [PMID: 41529692](https://pubmed.ncbi.nlm.nih.gov/41529692/).*


## Artifacts

- [OpenScientist final report](ACTB-Associated_Syndromic_Thrombocytopenia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ACTB-Associated_Syndromic_Thrombocytopenia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 20 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 22 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 13 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0100433` (2 mentions) - the report calls it "MONDO"; MONDO calls it **ACTB-associated syndromic thrombocytopenia**
- `HP:0001873` (2 mentions) - the report calls it "Laboratory abnormality"; HP calls it **Thrombocytopenia**
- `HP:0000252` (1 mention) - the report calls it "Clinical sign"; HP calls it **Microcephaly**
- `HP:0001999` (1 mention) - the report calls it "Physical"; HP calls it **Abnormal facial shape**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0011877` (2 mentions) - the report calls it "anisocytosis of platelets"; HP calls it **Increased mean platelet volume**, and lists "Large platelets" among its other names
- `GO:0000226` (1 mention) - the report calls it "microtubule organization"; GO calls it **microtubule cytoskeleton organization**
- `CL:0000057` (2 mentions) - the report calls it "fibroblasts", "Patient **fibroblasts"; CL calls it **fibroblast**
- `UBERON:0000955` (1 mention) - the report calls it "Central nervous system / brain"; UBERON calls it **brain**, and lists "suprasegmental levels of nervous system" among its other names
- `GO:0005874` (1 mention) - the report calls it "microtubule cytoskeleton"; GO calls it **microtubule**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000057` - called "fibroblasts", "Patient **fibroblasts"