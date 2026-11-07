---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-05T17:58:32.723892'
end_time: '2026-11-05T18:14:55.380271'
duration_seconds: 982.66
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Hemoglobin M Disease
  mondo_id: MONDO:0018023
  category: Mendelian
  causal_genes: HBB
  omim_id: OMIM:617971
  synonyms: M hemoglobinopathy; methemoglobinemia, beta type
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
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 21
  on_topic: 11
  off_topic: 1
  off_topic_references:
  - PMID:8504100
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 22
  verified: 21
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 2
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0018023
    reported_labels:
    - MONDO
    ontology_label: hemoglobin M disease
  - term_id: HP:0012119
    reported_labels:
    - Lab abnormality
    ontology_label: Methemoglobinemia
  - term_id: HP:0012418
    reported_labels:
    - Lab/sign
    ontology_label: Hypoxemia
  - term_id: HP:0012378
    reported_labels:
    - Symptom
    ontology_label: Fatigue
  - term_id: NCIT:C15277
    reported_labels:
    - NCIT suggestions:** Supportive Care
    ontology_label: Mastectomy
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hemoglobin_M_Disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hemoglobin_M_Disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hemoglobin M Disease
- **MONDO ID:** MONDO:0018023 (if available)
- **Causal gene(s):** HBB
- **OMIM:** OMIM:617971
- **Synonyms:** M hemoglobinopathy; methemoglobinemia, beta type
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Hemoglobin M Disease** covering all of the
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

# Hemoglobin M Disease (β type) — Comprehensive Disease Characterization Report

**Disease:** Hemoglobin M Disease | **MONDO:** MONDO:0018023 | **OMIM:** 617971
**Causal gene:** **HBB** (β-globin, HGNC:4827, 11p15.4) | **Category:** Mendelian, autosomal dominant
**Synonyms:** M hemoglobinopathy; methemoglobinemia, beta type; Hb M disease; congenital methemoglobinemia type 3

---

## Summary

**Hemoglobin M disease is a rare, autosomal-dominant structural hemoglobinopathy caused by heterozygous missense mutations in the β-globin gene *HBB* that replace a heme-coordinating amino-acid residue, locking the affected globin subunit in the oxidized (ferric, Fe³⁺) methemoglobin state and producing lifelong, benign, oxygen-refractory cyanosis.** Although the disease name ("methemoglobinemia, beta type") does not itself name the gene, the causal gene for the β-type is unambiguously *HBB*; α-chain variants of the same structural class (e.g., Hb M-Boston, Hb M-Iwate) arise in *HBA1/HBA2* and are catalogued under separate OMIM/MONDO entries. This report concerns the *HBB*-encoded β-chain form.

The molecular lesion is a substitution of one of the residues that cradle the heme iron — most classically the distal E7 histidine (**Hb M-Saskatoon, β63 His→Tyr, HBB:c.190C>T**), the proximal F8 histidine (**Hb M-Hyde Park/Akita, β92 His→Tyr**), or the E11 valine (**Hb M-Milwaukee-1, β67 Val→Glu**). The introduced tyrosine (or glutamate) forms a covalent-like phenolate–ferric-iron bond that stabilizes the heme iron in the Fe³⁺ state, which cannot bind oxygen, and simultaneously distorts the quaternary structure of the tetramer, lowering (distal variants) or raising (proximal β92 variant) the oxygen affinity of the remaining normal subunits. This methemoglobin is structurally "locked" and therefore cannot be reduced back to functional hemoglobin by the physiological cytochrome-b5-reductase system or by therapeutic reducing agents (methylene blue, vitamin C) — the key distinction from the recessive enzymatic form.

Clinically, patients present with lifelong central cyanosis, chocolate-brown blood, a diagnostic **"saturation gap"** (low pulse-oximetry SpO₂ with discordantly normal arterial PaO₂), and methemoglobin levels typically 10–35%. The condition is usually benign and asymptomatic; most patients require no treatment. The principal clinical hazards are **misdiagnosis** (as congenital heart disease, pulmonary hypertension, or hypoxemia) and **perioperative mismanagement** (misinterpreting the saturation gap, administering oxidant drugs). Diagnosis rests on co-oximetry, Hb electrophoresis/HPLC/isoelectric focusing, and definitive *HBB* sequencing. Unlike the enzymatic (CYB5R3) form, Hb M disease has no established natural animal model — naturally occurring hereditary methemoglobinemia in dogs and cats is the recessive CYB5R3-deficiency form.

---

## 1. Disease Information

**Overview.** Hemoglobin M disease is one of the two principal forms of *congenital* methemoglobinemia. It is caused by amino-acid substitutions in the globin chains themselves (structural hemoglobinopathy), as distinct from the second congenital form — recessive deficiency of the enzyme NADH-cytochrome b5 reductase (CYB5R3) — and from the far more common *acquired* (drug/toxin-induced) methemoglobinemia. In Hb M disease, a fraction of circulating hemoglobin is permanently maintained as methemoglobin because the mutant subunit stabilizes heme iron in the ferric (Fe³⁺) state. Cyanosis becomes clinically apparent once methemoglobin reaches ~15% of total hemoglobin.

> *"Congenital methaemoglobinaemia is of two types. The first is haemoglobin M disease (several variants) which is due to the presence of amino acid substitutions in either the alpha or beta chains."* — [PMID: 3537620](https://pubmed.ncbi.nlm.nih.gov/3537620/)

> *"The condition arises from three main pathologies: mutations in globin genes causing Haemoglobin-M, inherited deficiency of the enzyme cytochrome b5 reductase (CytB5R)... and exposure to some oxidising agents."* — [PMID: 42381511](https://pubmed.ncbi.nlm.nih.gov/42381511/)

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0018023 |
| OMIM | 617971 (methemoglobinemia, beta type) |
| Causal gene | HBB (HGNC:4827; NCBI Gene 3043; Ensembl ENSG00000244734) |
| MeSH | Hemoglobin M / Methemoglobinemia (D008708) |
| ICD-10 | D74.0 (congenital methemoglobinemia) |
| ICD-11 | 3A51 (methemoglobinemia) |
| Orphanet | Congenital methemoglobinemia (related entry) |

**Synonyms:** M hemoglobinopathy; methemoglobinemia, beta type; Hb M disease. Named structural β-variants include Hb M-Saskatoon, Hb M-Hyde Park (= Hb M-Akita = Hb M-Milwaukee-2), Hb M-Milwaukee-1, and Hb Tübingen.

**Evidence source type.** The disease-level characterization here is derived from a combination of **aggregated disease-level resources** (OMIM, reviews) and **individual-patient case reports** (the dominant literature format for this ultra-rare condition, each contributing a confirmed *HBB* genotype and phenotype).

---

## 2. Etiology

**Primary cause — genetic.** Hb M disease is caused by **heterozygous germline missense mutations in *HBB*** that substitute a heme-contact residue of the β-globin chain. Because a single mutant allele produces an abnormal, dysfunctional hemoglobin that actively perturbs the tetramer, the disease is **autosomal dominant**.

> *"Congenital methaemoglobinaemia due to haemoglobin M is an autosomal dominant disorder characterised by lifelong cyanosis."* — [PMID: 26494721](https://pubmed.ncbi.nlm.nih.gov/26494721/)

**Genetic risk factors.** The causal variants are the risk factors; there are no separate susceptibility loci. Documented β-chain pathogenic variants include:
- **Hb M-Saskatoon:** HBB:c.190C>T, p.His64Tyr (β63(E7)His→Tyr, distal histidine)
- **Hb M-Hyde Park/Akita/Milwaukee-2:** HBB codon 92 CAC>TAC (β92(F8)His→Tyr, proximal histidine)
- **Hb M-Milwaukee-1:** β67(E11)Val→Glu
- **Hb Tübingen:** HBB:c.320T>A, β106(G8)Leu→Gln

**Environmental / modifying factors.** Oxidizing agents (local anesthetics, benzocaine, dapsone, nitrites, and other drugs; inhaled nitric oxide in neonates) do not *cause* Hb M disease but **exacerbate** total methemoglobin burden on top of the structural baseline, and are therefore to be avoided. Age, sex, and family history (a cyanotic parent) are not risk factors per se but inform diagnosis.

**Protective factors.** None established genetically or environmentally. There is no known protective allele or dietary modifier.

**Gene–environment interaction.** The central interaction is between the fixed structural methemoglobin fraction (from *HBB*) and superimposed oxidant exposure: an oxidant stimulus raises MetHb further and can convert a benign baseline into symptomatic hypoxia — most dangerously in neonates and perioperatively.

---

## 3. Phenotypes

| Phenotype | Type | HPO suggestion | Onset | Severity | Frequency |
|---|---|---|---|---|---|
| Central cyanosis | Clinical sign | HP:0000961 (Cyanosis) | Congenital→after HbF switch (β variants: 3–6 mo) | Mild/cosmetic | Universal (defining) |
| Methemoglobinemia | Lab abnormality | HP:0012119 | Lifelong | 10–35% MetHb | Universal |
| Chocolate-brown blood | Clinical sign | — | Lifelong | — | Universal |
| Low SpO₂ with normal PaO₂ ("saturation gap") | Lab/sign | HP:0012418 | Lifelong | SpO₂ ~45–85% | Universal |
| Mild hemolytic anemia | Lab abnormality | HP:0001878 (Hemolytic anemia) | Lifelong | Mild | Only in unstable proximal variants (Hb M-Hyde Park) |
| Fatigue | Symptom | HP:0012378 | Variable | Mild/absent | Minority |

**Phenotype characteristics.** Overall the disease is remarkably benign: *"Patients with Hb M appear cyanotic but are usually asymptomatic"* ([PMID: 38159101](https://pubmed.ncbi.nlm.nih.gov/38159101/)). Course is **stable/non-progressive and lifelong**. Reported MetHb levels: Hb M-Saskatoon 12–34%; proximal variants add mild hemolysis.

**Quality-of-life impact.** Minimal for most; the main burdens are cosmetic cyanosis, repeated unnecessary cardiopulmonary workups, and anxiety from misdiagnosis. No validated disease-specific QoL instrument exists for this ultra-rare condition.

---

## 4. Genetic / Molecular Information

**Causal gene.** *HBB* (β-globin), OMIM 141900, HGNC:4827, chromosome 11p15.4.

**Pathogenic variants (β-chain Hb M).**

| Variant | HGVS / protein | Residue role | Functional consequence |
|---|---|---|---|
| Hb M-Saskatoon | HBB:c.190C>T, p.His64Tyr (β63 E7 His→Tyr) | Distal histidine | Ferric lock; cyanosis |
| Hb M-Hyde Park/Akita/Milwaukee-2 | codon 92 CAC>TAC (β92 F8 His→Tyr) | Proximal histidine | Ferric lock; unstable Hb, mild hemolysis; ↑O₂ affinity, loss of cooperativity |
| Hb M-Milwaukee-1 | β67(E11)Val→Glu | Heme-pocket E11 | Glutamate–iron bond; ferric lock |
| Hb Tübingen | HBB:c.320T>A (β106 G8 Leu→Gln) | G8 | Methemoglobinemia; co-migrates with HbF |

> *"Hemoglobin electrophoresis and whole-genome sequencing identified a heterozygous HBB:c.190C > T (p.His64Tyr) mutation, confirming the diagnosis of Hb M Saskatoon-associated methemoglobinemia."* — [PMID: 41881274](https://pubmed.ncbi.nlm.nih.gov/41881274/)

> *"the missense mutation is located in the HBB gene (HBB: c.190 C > T p.His64Tyr), which was described as Hb M Saskatoon disease. This mutation has been reported worldwide in fewer than ten cases."* — [PMID: 41116143](https://pubmed.ncbi.nlm.nih.gov/41116143/)

> *"Hb-M Hyde Park, also known as Hb-M Akita is a rare type of hereditary Hb M due to autosomal dominant mutation of CAC>TAC on codon 92 of β globin gene resulting in the replacement of histidine by tyrosine on β globin chain."* — [PMID: 28096792](https://pubmed.ncbi.nlm.nih.gov/28096792/)

- **Variant classification:** Pathogenic (ACMG/AMP) — established gene-disease mechanism, co-segregation, functional data.
- **Variant type/class:** Missense (single-nucleotide substitutions altering heme-contact residues).
- **Allele frequency:** Extremely rare; private/family-level. Hb M-Saskatoon reported in <10 cases worldwide. Not present at appreciable frequency in gnomAD.
- **Origin:** Germline; dominant. Arises as inherited or as *de novo* dominant mutation.
- **Functional consequence:** **Gain-of-abnormal-function / dominant structural effect** — the mutant subunit stabilizes ferric heme (methemoglobin) and perturbs tetramer allostery; not a classical loss-of-function.

**Modifier genes.** No specific modifier genes established for Hb M disease. (By contrast, co-inherited CYB5R3 status or oxidant-metabolism genes could theoretically modulate total MetHb burden.)

**Epigenetic information.** Not applicable — the phenotype is driven by a coding structural change, not epigenetic dysregulation. The developmental γ→β globin switch (regulated epigenetically at the β-globin locus) governs *onset timing* but is physiological, not disease-specific.

**Chromosomal abnormalities.** None — this is a point-mutation disorder, not a structural/copy-number disorder.

---

## 5. Environmental Information

- **Environmental / toxic factors:** Oxidizing drugs and chemicals (benzocaine and other topical/local anesthetics, dapsone, nitrites/nitrates, aniline dyes, quinolones) raise MetHb and should be avoided — they do not cause Hb M but compound it.
- **Lifestyle factors:** None causally relevant.
- **Infectious agents:** Not applicable — Hb M disease is purely genetic. (Note: acquired methemoglobinemia can follow infection-related drug exposure, but that is a separate entity.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A heterozygous *HBB* missense mutation **substitutes a heme-coordinating residue** of β-globin (distal His→Tyr, proximal His→Tyr, or E11 Val→Glu). → *leads to*
2. The introduced side chain (tyrosine phenolate, or glutamate carboxylate) **forms a direct bond to the heme iron**, displacing/replacing the normal proximal-histidine coordination. → *results in*
3. The heme iron is **stabilized in the ferric (Fe³⁺) oxidized state** (methemoglobin) in the mutant subunit, which **cannot reversibly bind O₂**. → *and in parallel*
4. The altered tertiary structure of the mutant subunit **perturbs the quaternary (T↔R) equilibrium** of the tetramer. → *branches:*
   - **4a. Distal-histidine variants** (Hb M-Boston α-analog; Hb M-Saskatoon β63) **stabilize the deoxy (T) quaternary state**, *lowering* the O₂ affinity of the normal subunits → *contributes to cyanosis.*
   - **4b. Proximal-histidine β-variant** (Hb M-Hyde Park, β92) *raises* O₂ affinity ~3–4× with **complete loss of cooperativity**, and yields an **unstable hemoglobin** → *mild hemolysis.*
5. The mutant ferric heme is **structurally resistant to reduction** by the NADH-cytochrome-b5-reductase system and by exogenous reducing agents. → *results in*
6. A **persistent circulating methemoglobin fraction (~10–35%)** that reduces effective oxygen-carrying capacity. → *leads to*
7. **Lifelong central cyanosis**, chocolate-brown blood, and a **saturation gap** (low SpO₂, normal PaO₂), clinically benign in most patients. *(Onset timed to the γ→β globin switch for β variants.)*

### Structural basis (demonstrated by X-ray crystallography)

The landmark structure of **Hb M-Boston** (α58 His→Tyr — the α-chain distal-E7 analog of the β-chain Hb M-Saskatoon) directly demonstrated the mechanism:

> *"the ferric iron atoms in the abnormal alpha subunits are bonded to the phenolate side chains of the tyrosines that have replaced the distal histidines; the iron atoms are displaced to the distal side of the porphyrin ring and are not bonded to the proximal histidines. The resulting changes in tertiary structure of the alpha subunits stabilize the hemoglobin tetramer in the quaternary deoxy structure, which lowers the oxygen affinity of the normal beta subunits and causes cyanosis."* — [PMID: 4521212](https://pubmed.ncbi.nlm.nih.gov/4521212/)

Spectroscopic work (CD/absorption) separates the two mechanistic classes:

> *"the proximal histidine replaced Hbs M (Hb M Iwate and Hb M Hyde Park) showed considerably different CD spectra from those of the distal histidine replaced ones (Hb M Boston and Hb M Saskatoon)."* — [PMID: 3994720](https://pubmed.ncbi.nlm.nih.gov/3994720/)

The proximal β92 variant is functionally distinct:

> *"The oxygen binding property of Hb M Hyde Park is characterized by 3 to 4 times higher oxygen affinity than that for normal hemoglobin, complete loss of cooperativity, and substantially preserved Bohr effect."* — [PMID: 7390859](https://pubmed.ncbi.nlm.nih.gov/7390859/)

### Classification of β-chain Hb M variants

```
                 β-globin heme pocket
                 ┌─────────────────────────┐
  DISTAL (E7)    │   His63 → Tyr            │  Hb M-Saskatoon
  heme contact   │   (stabilizes T state,   │  (distal class;
                 │    ↓ O2 affinity)        │   analog of Hb M-Boston α58)
                 ├─────────────────────────┤
  PROXIMAL (F8)  │   His92 → Tyr            │  Hb M-Hyde Park/Akita
  heme contact   │   (unstable Hb,          │  (proximal class;
                 │    ↑ O2 affinity,        │   mild hemolysis)
                 │    loss of cooperativity)│
                 ├─────────────────────────┤
  E11 pocket     │   Val67 → Glu            │  Hb M-Milwaukee-1
                 │   (carboxylate–Fe bond)  │
                 └─────────────────────────┘
```

- **Molecular pathway / biochemistry:** Heme redox chemistry — Fe²⁺↔Fe³⁺; the lesion is a fixed ferric lock.
- **Cellular process:** Within the erythrocyte, impaired oxygen transport; in unstable (proximal) variants, denatured globin → Heinz bodies → mild hemolysis.
- **Cell type involved:** Erythrocyte / erythroid lineage (**CL:0000232** erythrocyte; **CL:0000038** erythroid progenitor).
- **GO terms:** oxygen transport (GO:0015671); oxygen carrier activity (GO:0005344); heme binding (GO:0020037); hemoglobin complex (GO:0005833).
- **CHEBI:** methemoglobin/ferriheme (CHEBI related); heme b (CHEBI:26355); dioxygen (CHEBI:15379).
- **Immune involvement / metabolic / epigenetic changes:** Not applicable as primary mechanisms.
- **Molecular profiling / single-cell / CRISPR screens:** No transcriptomic/proteomic/metabolomic disease signatures are relevant; mechanism is resolved at the protein-structural level via crystallography and spectroscopy.

---

## 7. Anatomical Structures Affected

- **Organ/system level:** Hematologic system (blood). Secondary/apparent involvement: skin and mucous membranes (visible cyanosis — UBERON:0002097 skin). No true cardiac, pulmonary, hepatic, renal, or neurological organ damage in the benign β forms.
- **Tissue/cell level:** Erythrocytes (CL:0000232), produced in bone marrow (UBERON:0002371). Hemolysis in unstable variants recruits the spleen (UBERON:0002106) for RBC clearance.
- **Subcellular level:** The heme prosthetic group within the hemoglobin tetramer in the erythrocyte cytosol (GO:0005833 hemoglobin complex). No organelle (mitochondria/ER/nucleus) is the primary site.
- **Localization / lateralization:** Systemic and bilateral (cyanosis of lips, nail beds, and mucosa). Not focal or lateralized.
- **UBERON terms:** blood (UBERON:0000178); bone marrow (UBERON:0002371); skin (UBERON:0002097).

---

## 8. Temporal Development

**Onset.** Congenital in genotype, but **clinical onset timing is diagnostic of the affected globin gene**, tracking the developmental hemoglobin switch:

- **α-chain Hb M variants** → symptomatic **from birth** (α-globin expressed in fetal and adult Hb).
- **γ-chain (Hb F-M) variants** → **transient neonatal cyanosis** that resolves as fetal γ-globin is replaced.
- **β-chain (*HBB*) Hb M disease** → cyanosis becomes manifest **only after the perinatal HbF(γ)→HbA(β) switch (~3–6 months)**.

> *"Methemoglobinemia in newborns presents with cyanosis and hypoxemia, which can be mistaken for congenital heart disease or pulmonary hypertension."* — [PMID: 41853735](https://pubmed.ncbi.nlm.nih.gov/41853735/)

> *"Hereditary causes of methemoglobinemia should be considered for newborns with persistent cyanosis with low SpO₂..."* — [PMID: 41853735](https://pubmed.ncbi.nlm.nih.gov/41853735/) (same report documents an oxidant, inhaled nitric oxide, exacerbating neonatal methemoglobinemia)

**Onset pattern:** Insidious/chronic, non-acute.
**Progression:** Stable, non-progressive. **Disease course:** Chronic, lifelong, non-relapsing.
**Progression rate:** None (essentially static baseline MetHb).
**Remission:** No spontaneous or treatment-induced remission — the structural variant is permanent.
**Critical periods:** Neonatal period (oxidant vulnerability, diagnostic confusion) and perioperative windows.

---

## 9. Inheritance and Population

- **Inheritance pattern:** **Autosomal dominant** ([PMID: 26494721](https://pubmed.ncbi.nlm.nih.gov/26494721/)). Affected individuals are typically **heterozygous**.
- **Penetrance:** Complete for the biochemical/cyanosis phenotype (lifelong cyanosis in heterozygotes).
- **Expressivity:** Variable in symptom burden (most asymptomatic; proximal variants add mild hemolysis).
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism / consanguinity:** Not relevant (dominant, not recessive; no consanguinity requirement — contrast CYB5R3 deficiency).
- **Founder effects / carrier frequency:** Variants are private/family-specific and ultra-rare; no founder populations or meaningful carrier frequency.
- **Epidemiology:** Extremely rare; prevalence/incidence not reliably quantified. Individual β-variants reported in single-digit numbers of families worldwide (Hb M-Saskatoon: <10 cases).
- **Population demographics:** Sporadic across ethnicities; no strong sex predilection (dominant, autosomal). Reported across Chinese, Malay, European, and other populations.

> *"This mutation has been reported worldwide in fewer than ten cases."* — [PMID: 41116143](https://pubmed.ncbi.nlm.nih.gov/41116143/)

---

## 10. Diagnostics

**Diagnostic hallmark — the "saturation gap."** Low pulse-oximetry SpO₂ (e.g., 45–85%) with discordantly **normal or high arterial PaO₂** (often >140 mmHg), elevated MetHb on co-oximetry, and **dark chocolate-brown blood**, with **cyanosis unresponsive to supplemental oxygen**.

> *"We report an 18-year-old male presenting with marked cyanosis, chocolate-brown blood, markedly reduced arterial oxygen saturation, normal arterial partial pressure of oxygen, and elevated methemoglobin levels."* — [PMID: 41881274](https://pubmed.ncbi.nlm.nih.gov/41881274/)

> *"Recognition of a saturation gap is essential when oximetry findings are discordant..."* — [PMID: 41988351](https://pubmed.ncbi.nlm.nih.gov/41988351/)

**Clinical laboratory tests.**
- **Co-oximetry** (multi-wavelength) — quantifies MetHb% (LOINC methemoglobin assays). Standard pulse oximetry is unreliable.
- **Arterial blood gas** — normal PaO₂ confirms the saturation gap.
- **Hb electrophoresis / HPLC / isoelectric focusing** — detects the abnormal band. Caution: electrophoresis can mislead (e.g., Hb Tübingen co-migrates with HbF, falsely elevating HbF to 52.3%, corrected by HPLC).

> *"Hemoglobin electrophoresis revealed a false elevation of Hb F (52.3%) due to co-migration of Hb Tübingen with Hb F, which was validated by HPLC showing normal γ-globin levels."* — [PMID: 41918241](https://pubmed.ncbi.nlm.nih.gov/41918241/)

**Genetic testing (definitive).** *HBB* sequencing by Sanger, whole-exome (WES), or whole-genome (WGS) sequencing. WGS identified Hb M-Saskatoon (HBB:c.190C>T) in a recent case. Single-gene *HBB* testing or a hemoglobinopathy gene panel is the targeted approach; CMA/karyotype/FISH/mtDNA/repeat-expansion testing are **not** applicable.

**Brewer's methemoglobin reduction test** distinguishes enzymatic (reducible) from structural Hb M (non-reducible) methemoglobinemia; HPLC/molecular testing confirms.

**Differential diagnosis:**
1. Congenital heart disease / pulmonary hypertension (especially neonates).
2. Recessive CYB5R3 (cytochrome-b5-reductase) deficiency — enzymatic, autosomal recessive, methylene-blue–responsive.
3. Acquired/drug-induced methemoglobinemia — history of oxidant exposure, methylene-blue–responsive.
4. Other low-O₂-affinity/high-affinity hemoglobinopathies.

**Screening.** Not part of routine newborn screening for this specific ultra-rare structural variant; cascade *HBB* testing of relatives of a proband is appropriate.

---

## 11. Outcome / Prognosis

- **Survival / life expectancy:** Normal. Hb M disease is benign and does not shorten life.
- **Mortality:** No disease-specific mortality in the uncomplicated β forms; the realistic risk is **iatrogenic** (perioperative mismanagement, inappropriate oxidant therapy, or unnecessary invasive cardiac workups).
- **Morbidity / disability:** Minimal — cosmetic cyanosis; mild hemolytic anemia only in unstable proximal variants (Hb M-Hyde Park).
- **Complications:** Mild hemolysis (proximal variants); diagnostic delay and misdiagnosis across decades (cases diagnosed as late as age 79).
- **Recovery:** Not applicable — stable lifelong trait; no "recovery" because no decline.
- **Prognostic factors:** Variant class (distal vs proximal) predicts whether hemolysis accompanies cyanosis; baseline MetHb% predicts degree of visible cyanosis. Prognosis is uniformly favorable.

> *"Patients with Hb M appear cyanotic but are usually asymptomatic."* — [PMID: 38159101](https://pubmed.ncbi.nlm.nih.gov/38159101/)

---

## 12. Treatment

**Core principle: Hb M disease usually requires no specific treatment.** The cyanosis is benign and the structurally locked methemoglobin is **not correctable by reducing agents**.

**Why reducing agents fail.** Methylene blue is first-line for acquired/enzymatic methemoglobinemia, but in Hb M the ferric heme is structurally stabilized; vitamin C is likewise ineffective:

> *"Despite undergoing vitamin C therapy, the patient's symptoms of cyanosis and fatigue persisted."* — [PMID: 39854759](https://pubmed.ncbi.nlm.nih.gov/39854759/)

> *"Cyanosis with low peripheral oxygen saturation is unresponsive to oxygen therapy despite normal partial pressure of oxygen."* — [PMID: 38159101](https://pubmed.ncbi.nlm.nih.gov/38159101/)

**Perioperative / anesthetic management — the principal clinical intervention.** Preoperative recognition, avoidance of oxidizing agents (especially local/topical anesthetics), **co-oximetry (not pulse-oximetry) monitoring**, and multidisciplinary planning.

> *"Patients with Hb M appear cyanotic but are usually asymptomatic. ... As such, close attention should be paid during anesthesia."* — [PMID: 38159101](https://pubmed.ncbi.nlm.nih.gov/38159101/)

> *"...though rare, congenital methemoglobinemia poses fatal risks during surgery. Its management involves preoperative recognition and optimization, ... avoiding precipitating or oxidizing agents..."* — [PMID: 39224766](https://pubmed.ncbi.nlm.nih.gov/39224766/)

**For severe/acquired methemoglobin burden (not for the baseline Hb M fraction itself):** IV methylene blue (contraindicated in G6PD deficiency), high-dose vitamin C, exchange transfusion, and potentially hyperbaric oxygen.

> *"Alternative therapies include high-dose vitamin C, exchange transfusion and potentially hyperbaric oxygen."* — [PMID: 42381511](https://pubmed.ncbi.nlm.nih.gov/42381511/)

- **Pharmacogenomics:** Screen for **G6PD deficiency** before any methylene blue (risk of hemolysis / paradoxical worsening).
- **Advanced therapeutics (gene/cell/RNA/targeted/immuno):** None approved or in trials specifically for Hb M disease; the benign nature makes them unwarranted.
- **NCIT suggestions:** Supportive Care (NCIT:C15277); Patient Monitoring; Methylene Blue (NCIT:C61964, for acquired context); Ascorbic Acid (NCIT:C737); Blood Transfusion / Exchange Transfusion.

---

## 13. Prevention

- **Primary prevention:** Not possible (germline mutation). **Genetic counseling** for affected families — autosomal dominant, 50% transmission risk per pregnancy; prenatal/preimplantation testing is technically feasible but rarely pursued given benignity.
- **Secondary prevention:** Correct early diagnosis to **prevent iatrogenic harm** — avoid unnecessary cardiac catheterization, and flag the patient's chart to avoid oxidant drugs.
- **Tertiary prevention:** Perioperative protocols; avoidance of oxidizing agents; co-oximetry monitoring; MedicAlert documentation.
- **Immunization / public health / environmental interventions:** Not applicable (not infectious/environmental).
- **Counseling:** Genetic counseling is the central preventive measure (reassurance about benign prognosis + cascade testing).

---

## 14. Other Species / Natural Disease

**Key comparative-biology point:** Naturally occurring hereditary methemoglobinemia in animals is the **enzymatic CYB5R3-deficiency** form — **not** globin-structural Hb M disease.

> *"Hereditary methemoglobinemia associated with nicotinamide adenine dinucleotide-cytochrome b5 reductase (b5R) deficiency is a rare autosomal recessive disorder in animals."* — [PMID: 33342963](https://pubmed.ncbi.nlm.nih.gov/33342963/)

> *"nonsynonymous b5R gene (CYB5R3) variants have been reported to be associated with canine and feline hereditary methemoglobinemia..."* — [PMID: 33342963](https://pubmed.ncbi.nlm.nih.gov/33342963/)

- **Species / taxonomy:** Dog (*Canis familiaris*, NCBI:txid9615) and cat (*Felis catus*, NCBI:txid9685) — but for the *enzymatic* form (e.g., a Pomeranian family, CYB5R3 p.Ile194Leu).
- **Orthologs:** *HBB* orthologs exist across mammals, but no naturally occurring structural **Hb M** hemoglobinopathy is established as a veterinary disease.
- **Comparative pathology / veterinary relevance:** The veterinary counterpart maps to recessive CYB5R3 deficiency (human OMIM "recessive congenital methemoglobinemia"), not to Hb M disease.
- **Zoonotic potential / transmission:** None (genetic, non-transmissible).

**Implication:** Hb M disease is essentially a **human-described structural hemoglobinopathy with no established natural animal model.**

---

## 15. Model Organisms

- **Established disease-specific animal model:** **None.** There is no widely used knock-in mouse or other animal model that recapitulates β-chain Hb M disease.
- **Mechanistic model systems used instead:** The mechanism has been resolved almost entirely through **in vitro / structural biology** on purified human variant hemoglobins — X-ray crystallography (Hb M-Boston, [PMID: 4521212](https://pubmed.ncbi.nlm.nih.gov/4521212/)), CD/EPR/resonance-Raman and femtosecond-IR spectroscopy ([PMID: 3994720](https://pubmed.ncbi.nlm.nih.gov/3994720/); [PMID: 12128200](https://pubmed.ncbi.nlm.nih.gov/12128200/); [PMID: 8504100](https://pubmed.ncbi.nlm.nih.gov/8504100/)), functional O₂-binding assays ([PMID: 7390859](https://pubmed.ncbi.nlm.nih.gov/7390859/)), and **computational molecular-dynamics** prediction of novel variants ([PMID: 36837579](https://pubmed.ncbi.nlm.nih.gov/36837579/)).
- **Genetic models (KO/KI/transgenic/humanized):** Not reported for Hb M specifically; humanized globin mice exist for other hemoglobinopathies but are not applied to Hb M.
- **Model limitations:** The absence of an animal model means natural-history and therapeutic questions rely on human case reports and biophysics — adequate given the disease's benignity but limiting for mechanistic branch-specific studies.

---

## Mechanistic Model / Interpretation

The unifying model is a **single-residue structural lesion that produces a fixed ferric-heme lock plus an allosteric perturbation**, with the clinical picture flowing deterministically from where in the heme pocket the substitution falls:

```
HBB missense (heme-contact residue)
        │
        ▼
Tyr-phenolate (or Glu-carboxylate) → ferric iron bond
        │
        ▼
Mutant subunit locked as methemoglobin (Fe3+, cannot bind O2)
        │
        ├── Distal His (β63, Saskatoon) → T-state stabilized → ↓O2 affinity of normal subunits
        │
        └── Proximal His (β92, Hyde Park) → unstable Hb + ↑O2 affinity, no cooperativity → mild hemolysis
        │
        ▼
Persistent MetHb 10–35% + resistant to reductase/methylene blue/vitamin C
        │
        ▼
Lifelong benign cyanosis • chocolate-brown blood • saturation gap
   (β onset after HbF→HbA switch, ~3–6 mo)
        │
        ▼
Main hazard = misdiagnosis & perioperative oxidant exposure (iatrogenic, preventable)
```

**Upstream vs downstream:** The *HBB* mutation and the ferric-tyrosine bond are the upstream, invariant drivers; the quaternary-structure/oxygen-affinity perturbation is the branch point; cyanosis and the saturation gap are the downstream, universal readouts; hemolysis is a downstream feature restricted to the unstable (proximal) branch.

---

## Evidence Base

| PMID | Role | Key contribution |
|---|---|---|
| [3537620](https://pubmed.ncbi.nlm.nih.gov/3537620/) | Supports | Defines Hb M as globin-chain substitution form of congenital methemoglobinemia |
| [26494721](https://pubmed.ncbi.nlm.nih.gov/26494721/) | Supports | Autosomal dominant, lifelong cyanosis; neonatal benign cyanosis |
| [42381511](https://pubmed.ncbi.nlm.nih.gov/42381511/) | Supports | Three etiologies of methemoglobinemia; 2nd-line therapies |
| [41881274](https://pubmed.ncbi.nlm.nih.gov/41881274/) | Supports | Hb M-Saskatoon HBB:c.190C>T genotype; diagnostic cluster |
| [41116143](https://pubmed.ncbi.nlm.nih.gov/41116143/) | Supports | Variant nomenclature + global rarity (<10 cases) |
| [38159101](https://pubmed.ncbi.nlm.nih.gov/38159101/) | Supports | Benign, O₂-unresponsive cyanosis; anesthetic caution |
| [39854759](https://pubmed.ncbi.nlm.nih.gov/39854759/) | Supports | Vitamin C ineffective in confirmed Hb M family |
| [28096792](https://pubmed.ncbi.nlm.nih.gov/28096792/) | Supports | Hb M-Hyde Park codon 92 mutation; CHD misdiagnosis pitfall |
| [9494043](https://pubmed.ncbi.nlm.nih.gov/9494043/) | Supports | Codon 92 identity across Hyde Park/Akita/Milwaukee-2 |
| [7390859](https://pubmed.ncbi.nlm.nih.gov/7390859/) | Supports | Quantified O₂-binding of proximal β92 variant |
| [41988351](https://pubmed.ncbi.nlm.nih.gov/41988351/) | Supports | Saturation gap recognition; perioperative management |
| [41918241](https://pubmed.ncbi.nlm.nih.gov/41918241/) | Supports / caution | Hb Tübingen; electrophoresis co-migration artifact |
| [4521212](https://pubmed.ncbi.nlm.nih.gov/4521212/) | Supports (landmark) | X-ray proof of ferric-phenolate bond, T-state lock |
| [3994720](https://pubmed.ncbi.nlm.nih.gov/3994720/) | Supports | Proximal vs distal structural classification (CD) |
| [41853735](https://pubmed.ncbi.nlm.nih.gov/41853735/) | Supports | Neonatal methemoglobinemia; oxidant (iNO) exacerbation |
| [39224766](https://pubmed.ncbi.nlm.nih.gov/39224766/) | Supports | Perioperative risk and management algorithm |
| [33342963](https://pubmed.ncbi.nlm.nih.gov/33342963/) | Supports | Animal hereditary methemoglobinemia = CYB5R3, not Hb M |
| [41639689](https://pubmed.ncbi.nlm.nih.gov/41639689/) | Context | Systematic review of recessive (CYB5R3) congenital methemoglobinemia (contrast entity) |

---

## Limitations and Knowledge Gaps

1. **Ultra-rarity and case-report–driven evidence.** Each β-variant is known from a handful of families; there are no cohort, registry, or natural-history studies, so frequencies and QoL metrics are qualitative.
2. **No animal model.** Mechanistic understanding rests on human biophysics (crystallography, spectroscopy, MD); branch-specific (proximal vs distal) physiology has not been studied in vivo.
3. **β vs α attribution.** Much structural detail derives from the **α-chain** prototype Hb M-Boston; while mechanistically analogous to the β distal variant (Hb M-Saskatoon), direct β63 crystallographic data are sparser.
4. **No modifier-gene data.** Whether CYB5R3 or oxidant-metabolism genotypes modulate the baseline MetHb% in Hb M carriers is unstudied.
5. **Epidemiology absent.** True prevalence/incidence, sex ratio, and geographic distribution are unquantified.
6. **Diagnostic pitfalls persist.** Electrophoresis artifacts (HbF co-migration) and late diagnoses (into the 8th decade) indicate ongoing under-recognition.

---

## Proposed Follow-up Experiments / Actions

1. **Curate a variant-level knowledge-base table** linking each β Hb M variant (Saskatoon, Hyde Park/Akita, Milwaukee-1, Tübingen) to HBB HGVS, heme-pocket residue class, MetHb range, hemolysis status, and O₂-affinity direction.
2. **Deposit/aggregate ClinVar entries** for each confirmed *HBB* Hb M variant with ACMG classification and the supporting case PMIDs.
3. **Draft a perioperative/anesthesia checklist** (co-oximetry, oxidant-avoidance list, G6PD screen before methylene blue) as a reusable clinical artifact — the single highest-yield intervention given that mortality here is iatrogenic.
4. **Model-prediction pipeline:** apply molecular-dynamics screening (as in [PMID: 36837579](https://pubmed.ncbi.nlm.nih.gov/36837579/)) to predict novel heme-contact *HBB* substitutions likely to cause Hb M, to aid VUS interpretation.
5. **Newborn-cyanosis diagnostic algorithm:** formalize the onset-timing rule (α = from birth; γ = transient neonatal; β = after HbF→HbA switch) into a decision tree to speed differentiation from congenital heart disease and CYB5R3 deficiency.
6. **Genetic counseling template** for autosomal dominant transmission emphasizing benign prognosis and cascade *HBB* testing.


## Artifacts

- [OpenScientist final report](Hemoglobin_M_Disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hemoglobin_M_Disease-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 21 |
| On topic | 11 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:8504100` (3 mentions) - Determination of Fe-CO geometry in the subunits of carbonmonoxy hemoglobin M Boston using femtosecond infrared spectroscopy.
  - shared terms: hemoglobin

Weighed against this report's own most characteristic terms: `variant`, `disease`, `cyanosis`, `hbb`, `methemoglobinemia`, `hemoglobin`, `proximal`, `structural`, `congenital`, `m-saskatoon`, `chain`, `globin`, `benign`, `park`, `hemolysis`, `gene`, `mutation`, `cyb5r3`, `autosomal`, `genetic`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 22 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 10 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0018023` (2 mentions) - the report calls it "MONDO"; MONDO calls it **hemoglobin M disease**
- `HP:0012119` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Methemoglobinemia**
- `HP:0012418` (1 mention) - the report calls it "Lab/sign"; HP calls it **Hypoxemia**
- `HP:0012378` (1 mention) - the report calls it "Symptom"; HP calls it **Fatigue**
- `NCIT:C15277` (1 mention) - the report calls it "NCIT suggestions:** Supportive Care"; NCIT calls it **Mastectomy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000232` (2 mentions) - the report calls it "Tissue/cell level:** Erythrocytes"; CL calls it **erythrocyte**
- `GO:0015671` (1 mention) - the report calls it "GO terms:** oxygen transport"; GO calls it **oxygen transport**
- `UBERON:0000178` (1 mention) - the report calls it "UBERON terms:** blood"; UBERON calls it **blood**, and lists "vertebrate blood" among its other names