---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T07:51:20.464918'
end_time: '2026-10-30T08:06:40.939625'
duration_seconds: 920.47
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Cataract 12 Multiple Types
  mondo_id: MONDO:0012701
  category: Mendelian
  causal_genes: BFSP2
  omim_id: OMIM:611597
  synonyms: CTRCT12
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
citation_count: 18
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 14
  validator_version: 0.4.0
term_validation:
  total_terms: 23
  verified: 21
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 4
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0012701
    reported_labels:
    - MONDO
    ontology_label: cataract 12 multiple types
  - term_id: HP:0007686
    reported_labels:
    - Progressive/congenital cataract
    ontology_label: Abnormal pupillary function
  - term_id: CL:0000148
    reported_labels:
    - Tissue/cell:** lens fiber cells
    ontology_label: melanocyte
  - term_id: NCIT:C157672
    reported_labels:
    - Cataract Surgery
    ontology_label: Indeterminate Nodule Type
  - term_id: NCIT:C15277
    reported_labels:
    - Surgery
    ontology_label: Mastectomy
  - term_id: NCIT:C62314
    reported_labels:
    - Intraocular Lens
    ontology_label: Nanofabrication
  labels_variant: 7
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Cataract_12_Multiple_Types-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Cataract_12_Multiple_Types-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cataract 12 Multiple Types
- **MONDO ID:** MONDO:0012701 (if available)
- **Causal gene(s):** BFSP2
- **OMIM:** OMIM:611597
- **Synonyms:** CTRCT12
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Cataract 12 Multiple Types** covering all of the
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

# Cataract 12, Multiple Types (CTRCT12; MONDO:0012701; OMIM 611597) — Comprehensive Disease Report

**Causal gene: _BFSP2_ (phakinin / CP49; HGNC:1041; NCBI Gene 8419; UniProt Q13515; gene OMIM 603212), encoding a lens-fiber-specific beaded-filament intermediate-filament protein.**

---

## Summary

**Cataract 12, Multiple Types (CTRCT12)** is a Mendelian, non-syndromic, bilateral inherited cataract caused by variants in **_BFSP2_**, the gene encoding **phakinin (also called CP49)**. Phakinin is a lens-fiber-specific intermediate-filament (IF) protein that, together with filensin (BFSP1), assembles the **beaded filament**, a cytoskeletal structure unique to vertebrate lens fiber cells. The "Multiple Types" in the disease name reflects true phenotypic heterogeneity: across reported pedigrees the cataracts range in morphology (nuclear/pulverulent, sutural, lamellar/zonular, cortical) and in age of onset (congenital through juvenile-onset in the second–third decades), and are frequently progressive. The disorder is confined to the eye lens — there is no systemic or extra-ocular involvement.

Most CTRCT12 is **autosomal dominant**. Two founding dominant alleles were independently reported in 2000 — an in-frame deletion **ΔE233** (exon 3) and a missense **R287W** (exon 4, central rod domain) — and both map to _BFSP2_ at chromosome 3q21–q22 (now 3q22.1). Additional dominant alleles include **G112E** (pulverulent + sutural), **R339H** (congenital lamellar), and recurrent **ΔE233** (progressive congenital). A rare **homozygous null** allele causes a milder autosomal recessive diffuse cortical cataract, and — critically — heterozygous carriers of the null are unaffected. This asymmetry (dominant point mutations cause disease, while loss of one allele does not) is the strongest line of evidence that the dominant mutations act through a **dominant-negative / toxic gain-of-function** mechanism rather than haploinsufficiency: mutant phakinin is incorporated into and poisons beaded-filament assembly, increasing lens light scatter.

There is **no gene-specific or pharmacologic therapy**. Management follows general pediatric/inherited cataract practice: surgical lens extraction (lens aspiration ± IOL) for visually significant opacity, combined with optical correction and amblyopia rehabilitation. Because many _BFSP2_ opacities are mild and slowly progressive, surgery is frequently deferred until the opacity becomes visually significant. With timely treatment the visual prognosis is good. The disease models are mammalian/mouse: targeted CP49 knockouts and a naturally occurring ~6-kb _Bfsp2_ deletion present in common inbred strains (129, FVB/N). These reproduce beaded-filament loss and degraded lens optical quality, though frank cataract in knockouts is mild — consistent with the human genetics that frank dominant disease requires a poisoning mutant protein, not mere absence.

---

## Key Findings

### Finding 1 — _BFSP2_ is the causal gene; two founding dominant alleles at 3q21–q22 (F001)

CTRCT12 is caused by mutations in **_BFSP2_**, encoding phakinin/CP49. The gene was established as the cause by two independent 2000 reports of autosomal dominant cataract mapping to chromosome 3q21–q22:

- **ΔE233** — an in-frame deletion in exon 3, in family ADCC-3 (Jakobs et al. 2000). This was explicitly the **first** inherited cataract shown to be caused by a mutation in a cytoskeletal protein: *"we found that a deletion mutation, DeltaE233, is associated with cataracts in this family. This is the first report of an inherited cataract that is caused by a mutation in a cytoskeletal protein"* [PMID: 10739768](https://pubmed.ncbi.nlm.nih.gov/10739768/).
- **R287W** — a nonconservative missense substitution in exon 4 affecting a conserved arginine in the central rod (coiled-coil) domain, causing a juvenile-onset progressive cataract: *"We predicted that this led to a nonconservative R287W substitution in exon 4 that cosegregated with cataracts. This mutation alters an evolutionarily conserved arginine residue in the central rod domain of the intermediate filament"* [PMID: 10729115](https://pubmed.ncbi.nlm.nih.gov/10729115/).

Subsequently reported dominant alleles broaden the mutational spectrum: **G112E** [PMID: 24654948](https://pubmed.ncbi.nlm.nih.gov/24654948/), **R339H** (G1091A, exon 5) [PMID: 18958306](https://pubmed.ncbi.nlm.nih.gov/18958306/), and recurrent **ΔE233** in a progressive Chinese family mapping to 3q22.1 with LOD 3.99 [PMID: 17982427](https://pubmed.ncbi.nlm.nih.gov/17982427/). In every pedigree the variant cosegregated with disease and was absent from 100–200 control chromosomes.

### Finding 2 — Dominant mechanism is dominant-negative, not haploinsufficiency (F002)

Aldahmesh et al. (2011) identified a novel **homozygous, likely null** _BFSP2_ mutation causing **autosomal recessive diffuse cortical cataract** in a consanguineous family, with **no phenotype in heterozygous carriers**: *"a novel BFSP2 mutation causes autosomal recessive diffuse cortical cataract with scattered lens opacities"* and *"The likely null nature of both mutations and lack of manifestation in heterozygotes strongly argues for a mechanism other than loss of function in the previously reported dominant mutations in these two genes"* [PMID: 21836522](https://pubmed.ncbi.nlm.nih.gov/21836522/).

The logic is decisive: because losing one allele is asymptomatic, the heterozygous dominant alleles (ΔE233, R287W, etc.) cannot be causing disease by simply halving protein dose. Instead, mutant phakinin is produced and **disrupts normal beaded-filament assembly** — a dominant-negative/toxic gain-of-function effect. The structural rationale supports this: the key residues lie in or near the conserved central rod (coiled-coil) domain required for coassembly with filensin, so a mutant subunit can be incorporated into and poison the heteropolymer.

### Finding 3 — Beaded filaments are required for lens optical quality (mouse knockouts) (F003)

Two independent CP49/_Bfsp2_ knockout mouse lines establish the function of the beaded filament:

- Targeted CP49 deletion (Alizadeh et al. 2002) abolished beaded filaments and sharply reduced filensin protein (filensin mRNA unchanged), producing a progressive, age-worsening loss of optical clarity: *"The absence of CP49 causes a subtle loss of optical clarity in the ocular lens, a loss that worsens with age"* [PMID: 12454043](https://pubmed.ncbi.nlm.nih.gov/12454043/).
- An independent CP49 knockout (Sandilands et al. 2003) found disrupted beaded filaments with deteriorated light-scatter/optical properties but **no frank cataract**: *"no cataract was observed despite the fact that the beaded filaments of the lens fibre cells had been disrupted. Light scatter and the lens optical properties had, however, deteriorated in the CP49 knockout lenses"* [PMID: 12573667](https://pubmed.ncbi.nlm.nih.gov/12573667/).

The milder knockout phenotype (optical degradation without frank cataract) reinforces Finding 2: absence of phakinin is comparatively mild, whereas human dominant disease requires a poisoning mutant protein. Beaded filaments also interact with Aquaporin 0 (AQP0), contribute to lens biomechanics, and are required for cold-cataract formation [PMID: 34087204](https://pubmed.ncbi.nlm.nih.gov/34087204/); [PMID: 32913386](https://pubmed.ncbi.nlm.nih.gov/32913386/). An important experimental confounder is that common inbred strains **129 and FVB/N carry a natural ~6-kb _Bfsp2_ deletion** and lack beaded-filament proteins [PMID: 17065509](https://pubmed.ncbi.nlm.nih.gov/17065509/).

### Finding 4 — Gene/protein annotation: phakinin/CP49, a tailless lens-specific IF protein at 3q22.1 (F004)

Authoritative identifiers: Gene symbol **BFSP2**; **NCBI Gene 8419**; **HGNC:1041**; gene OMIM **603212** (phenotype CTRCT12 OMIM **611597**); **Ensembl ENSG00000170819**; **UniProt Q13515**; cytogenetic location **3q22.1** (GRCh38 chr3:133,400,056–133,475,222, + strand); protein-coding. Aliases: CP47, CP49, CTRCT12, LIFL-L, PHAKOSIN.

Phakinin and filensin are two lens-specific IF-like proteins expressed only after fiber-cell differentiation begins; they coassemble into the beaded filament. CP49 is structurally distinctive — completely tailless — while filensin has a short rod domain and a very large C-terminal tail; neither forms filaments alone: *"Whilst CP49 is completely tailless, filensin has a rather short rod domain and extremely large C-terminal tail domain. In vitro, CP49 and filensin do not form IFs on their own"* [PMID: 15777782](https://pubmed.ncbi.nlm.nih.gov/15777782/).

### Finding 5 — Epidemiology: a rare cause within pediatric cataract (~2–3/10,000 births), predominantly AD (F005)

A population-based Australian study estimated pediatric cataract incidence at **2.2 per 10,000 births** and found autosomal dominant inheritance predominant among familial cases: *"421 patients with paediatric cataract were identified, which gives an estimated incidence of 2.2 per 10,000 births"* and *"The mode of inheritance was autosomal dominant in 30 families, X linked in four, autosomal recessive in two, and uncertain in three"* [PMID: 12084750](https://pubmed.ncbi.nlm.nih.gov/12084750/). Contemporary cohorts achieve a molecular diagnosis in ~80% of bilateral pediatric cataract, with crystallin genes most common and _BFSP2_ a **minor** contributor [PMID: 38874774](https://pubmed.ncbi.nlm.nih.gov/38874774/). CTRCT12 has no separate prevalence estimate; it is one of ≥26 inherited cataract genes [PMID: 28526010](https://pubmed.ncbi.nlm.nih.gov/28526010/). Reported _BFSP2_ pedigrees are predominantly Chinese, with European (German ADCC-3), US, and Saudi (recessive) families.

### Finding 6 — Treatment is non-gene-specific surgery + rehabilitation (F006)

No pharmacologic or gene-targeted therapy exists; management follows general pediatric cataract guidelines. *"lens opacity obscuring the red reflex in preverbal children and visual acuity of less than 20/40 is an absolute indication for lens aspiration"* [PMID: 31317088](https://pubmed.ncbi.nlm.nih.gov/31317088/). Surgery is recommended early for visually significant opacity (~6 weeks for unilateral, 6–8 weeks for bilateral) to prevent amblyopia; lens aspiration with posterior capsulotomy/anterior vitrectomy is used in children <6 years, with IOL implantation generally considered in patients older than 1 year. The principal under-2-years decision is IOL vs primary aphakia: *"Two options currently considered for children under 2 years of age with bilateral congenital cataracts are: (i) intraocular lens (IOL) implantation; or (ii) leaving a child with primary aphakia"* [PMID: 36107778](https://pubmed.ncbi.nlm.nih.gov/36107778/). Because many _BFSP2_ opacities are mild/progressive (juvenile-onset), surgery may be deferred until the opacity is visually significant.

### Finding 7 — Conservation and model organisms (F007)

_BFSP2_ is evolutionarily conserved (HomoloGene 20791): mouse _Bfsp2_ (NCBI 107993, MGI:1333828, chr 9 F1), rat (501046), dog (608938), cow (281645), chicken (396141), zebrafish _bfsp2_ (494090), _Xenopus_ (100486639), rhesus (717551), chimp (460708). The principal disease models are mouse: targeted CP49 knockouts [PMID: 12454043](https://pubmed.ncbi.nlm.nih.gov/12454043/); [PMID: 12573667](https://pubmed.ncbi.nlm.nih.gov/12573667/), the natural ~6-kb deletion in strains 129/FVB/N: *"FVB/N mice obtained from all four US distributors were shown to harbor a 6-kb deletion of the CP49 gene identical with that previously reported in mouse strain 129"* [PMID: 17065509](https://pubmed.ncbi.nlm.nih.gov/17065509/) — which *"will effectively generate a CP49 knockout"* [PMID: 15777782](https://pubmed.ncbi.nlm.nih.gov/15777782/) — and the filensin (_Bfsp1_) knockout, whose lenses also lose CP49 beaded filaments.

### Finding 8 — Phenotype spectrum: variable bilateral opacities, congenital to juvenile, often progressive (F008)

Across _BFSP2_ pedigrees, morphology and onset are heterogeneous — hence "multiple types": embryonal-nuclear pulverulent with sutural opacities (G112E) — *"All affected individuals presented pulverulent opacities in the embryonal nucleus and sutures"* [PMID: 24654948](https://pubmed.ncbi.nlm.nih.gov/24654948/); juvenile-onset progressive with a clear lens at birth developing opacity in the 2nd–3rd decades (R287W) — *"Juvenile-onset cataracts are distinguished from congenital cataracts by the initial clarity of the lens at birth and the gradual development of lens opacity in the second and third decades of life"* [PMID: 10729115](https://pubmed.ncbi.nlm.nih.gov/10729115/); progressive congenital (ΔE233) [PMID: 17982427](https://pubmed.ncbi.nlm.nih.gov/17982427/); congenital lamellar (R339H) [PMID: 18958306](https://pubmed.ncbi.nlm.nih.gov/18958306/); and recessive diffuse cortical cataract in the null state [PMID: 21836522](https://pubmed.ncbi.nlm.nih.gov/21836522/). Opacities are bilateral and non-syndromic.

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** Cataract 12, Multiple Types (CTRCT12) is a Mendelian, isolated (non-syndromic), bilateral inherited lens opacity caused by variants in **_BFSP2_** (phakinin/CP49). "Multiple types" denotes morphological and onset heterogeneity rather than distinct diseases.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| Disease (phenotype) OMIM | 611597 (CTRCT12) |
| MONDO | MONDO:0012701 |
| Gene OMIM | 603212 (BFSP2) |
| Gene (HGNC) | HGNC:1041, BFSP2 |
| NCBI Gene | 8419 |
| Ensembl | ENSG00000170819 |
| UniProt | Q13515 |
| Cytogenetic locus | 3q22.1 |
| ICD-11 | 9B10.2Y (other specified congenital/developmental cataract) — general cataract mapping, no CTRCT12-specific code |
| MeSH | Cataract (D002386); no CTRCT12-specific term |

**Synonyms / alternative names.** CTRCT12; Cataract 12, multiple types; cataract associated with _BFSP2_/CP49/phakinin. Gene aliases: CP47, CP49, PHAKOSIN, LIFL-L.

**Information source.** Derived from **aggregated disease-level resources** (OMIM, ClinVar-style variant reports) and from **individual multi-generational pedigree studies** (family-based linkage and sequencing). Not from large EHR datasets.

### 2. Etiology

**Primary cause — genetic.** Germline pathogenic variants in _BFSP2_. Founding dominant alleles **ΔE233** (exon 3 in-frame deletion) [PMID: 10739768] and **R287W** (exon 4, rod domain) [PMID: 10729115], plus **G112E** [PMID: 24654948], **R339H** [PMID: 18958306], recurrent **ΔE233** [PMID: 17982427], and a recessive **null** allele [PMID: 21836522].

**Genetic risk factors.** The causal variant itself is the determinant; CTRCT12 is monogenic with high penetrance. No established common susceptibility loci or modifier genes are specific to CTRCT12.

**Environmental risk factors.** Not applicable to the Mendelian form. General (age-related/secondary) cataract risk factors — UV exposure, smoking, diabetes, corticosteroids — are **not** causes of CTRCT12 and should not be conflated with it.

**Protective factors.** No genetic or environmental protective factors are established for CTRCT12.

**Gene–environment interactions.** None demonstrated for CTRCT12. (Mouse work shows beaded filaments are required for cold-cataract formation — a temperature×genotype interaction in model systems — but this is not an established human environmental modifier [PMID: 32913386].)

### 3. Phenotypes

The lens is the sole affected organ; disease is bilateral and non-syndromic.

| Phenotype | HPO term | Characteristics / allele association |
|---|---|---|
| Cataract (bilateral) | HP:0000518 | Core feature; all pedigrees |
| Nuclear cataract | HP:0100018 | Embryonal-nucleus opacity (G112E) |
| Pulverulent cataract | HP:0010920 | Powder-like opacities (G112E) |
| Sutural cataract | HP:0100017 | Along Y-sutures (G112E) |
| Lamellar/zonular cataract | HP:0007971 | Congenital lamellar (R339H) |
| Cortical cataract | HP:0100019 | Diffuse cortical, recessive null |
| Progressive/congenital cataract | HP:0007686 | Progressive course (ΔE233; R287W) |
| Visual impairment | HP:0000505 | Secondary to opacity |
| Autosomal dominant inheritance | HP:0000006 | Most pedigrees |
| Autosomal recessive inheritance | HP:0000007 | Null allele |

- **Phenotype type:** clinical sign / physical manifestation (lens opacity on slit-lamp), with secondary symptom of reduced vision.
- **Age of onset:** congenital to juvenile-onset (opacity developing in the 2nd–3rd decades for R287W) [PMID: 10729115].
- **Severity:** variable (mild to visually significant).
- **Progression:** often progressive/age-worsening; some stable.
- **Frequency among affected:** cataract is fully penetrant within pedigrees; morphology varies by allele.
- **Quality-of-life impact:** when visually significant and untreated in childhood, risk of amblyopia and lifelong visual disability; excellent functional outcomes with timely surgery. No CTRCT12-specific EQ-5D/SF-36 data.

### 4. Genetic / Molecular Information

**Causal gene.** _BFSP2_ (HGNC:1041; NCBI 8419; gene OMIM 603212), 3q22.1.

**Pathogenic variants.**

| Variant | Type | Exon/domain | Phenotype | Inheritance | PMID |
|---|---|---|---|---|---|
| ΔE233 (p.Glu233del) | in-frame deletion | exon 3 | AD congenital, progressive | AD | 10739768; 17982427 |
| R287W | missense | exon 4, central rod | juvenile-onset progressive | AD | 10729115 |
| G112E | missense | — | pulverulent nuclear + sutural | AD | 24654948 |
| R339H (G1091A) | missense | exon 5 | congenital lamellar | AD | 18958306 |
| homozygous null | loss of function | — | diffuse cortical | AR | 21836522 |

- **Classification:** reported alleles cosegregate and are absent from 100–200 controls → pathogenic/likely pathogenic by family evidence.
- **Allele frequency:** private/rare; not population-frequent in gnomAD.
- **Somatic vs germline:** germline.
- **Functional consequence:** dominant alleles → **dominant-negative/gain-of-function** (poisoning beaded-filament assembly); recessive null → **loss of function** [PMID: 21836522].

**Modifier genes.** Filensin/_BFSP1_ is an obligate assembly partner; its loss also ablates CP49 filaments, but no formal human modifier is established. **Epigenetic** and **chromosomal abnormality** contributions: none implicated in CTRCT12.

### 5. Environmental Information

Not applicable to the Mendelian disease. No toxins, lifestyle factors, or infectious agents cause or trigger CTRCT12. (Secondary/age-related cataract has environmental drivers, but these are a separate entity.)

### 6. Mechanism / Pathophysiology

**Ordered causal chain (dominant form):**

1. A dominant _BFSP2_ mutation (e.g., ΔE233 or R287W in/near the conserved central rod domain) **leads to** production of a structurally abnormal phakinin subunit.
2. The mutant subunit **is incorporated into** the phakinin–filensin heteropolymer and **disrupts** normal beaded-filament assembly (dominant-negative) — *inferred* from the structural rod-domain location plus the genetic evidence that heterozygous null is asymptomatic [PMID: 21836522].
3. Disrupted/destabilised beaded filaments **result in** loss of the fiber-cell IF cytoskeleton and secondary loss/destabilisation of filensin (demonstrated in KO: filensin protein falls though mRNA is unchanged) [PMID: 12454043].
4. Cytoskeletal disorganisation **leads to** altered fiber-cell architecture, membrane organisation, and perturbed interaction with AQP0, degrading the lens refractive-index gradient and biomechanics [PMID: 34087204].
5. These changes **result in** increased intracellular light scatter [PMID: 12573667].
6. Increased light scatter **manifests as** a clinically visible lens opacity (cataract), which in several alleles **progresses** with age [PMID: 12454043; 17982427].

**Branch (recessive null):** Homozygous loss of phakinin **leads to** absence of beaded filaments and a milder, diffuse cortical opacity; heterozygotes are unaffected [PMID: 21836522].

- **Upstream:** mutation → mutant protein → filament poisoning. **Downstream:** light scatter → opacity → visual impairment.
- **Cell types / processes involved:** lens fiber cells (CL:0000148, lens fiber cell); intermediate filament cytoskeleton organization (GO:0045104); beaded filament assembly; lens development in camera-type eye (GO:0002088); visual perception (GO:0007601).
- **Subcellular compartment:** cytoplasmic intermediate filament / cytoskeleton (GO:0005882, intermediate filament; GO:0045111, intermediate filament cytoskeleton); plasma-membrane–associated organisation.
- **Molecular profiling:** no transcriptomic/proteomic/metabolomic signature specific to human CTRCT12; mouse KO shows selective loss of filensin protein with preserved mRNA [PMID: 12454043].

### 7. Anatomical Structures Affected

- **Organ:** eye lens (UBERON:0000965). No secondary organ involvement; body system = visual/sensory.
- **Tissue/cell:** lens fiber cells (CL:0000148); the opacity is intrinsic to differentiated fiber cells where beaded filaments are expressed.
- **Subcellular:** intermediate filament cytoskeleton (GO:0045111); fiber-cell plasma membrane region.
- **Localization:** bilateral; opacity site varies by allele (nuclear/embryonal nucleus, sutures, lamellar/zonular layer, cortex).

### 8. Temporal Development

- **Onset:** congenital in many dominant alleles (ΔE233, R339H, G112E); juvenile-onset (clear lens at birth, opacity developing in the 2nd–3rd decades) for R287W [PMID: 10729115].
- **Onset pattern:** insidious/chronic.
- **Progression:** frequently progressive and age-worsening (ΔE233 [PMID: 17982427]; KO optical clarity worsens with age [PMID: 12454043]); some stable.
- **Course:** chronic, lifelong; opacity does not spontaneously remit — "remission" is treatment-induced (surgical removal). **Critical period:** early childhood is the critical window for preventing deprivation amblyopia in congenital/early cases.

### 9. Inheritance and Population

- **Epidemiology:** no CTRCT12-specific prevalence; nested within pediatric cataract incidence of **~2.2 per 10,000 births** [PMID: 12084750]; _BFSP2_ is a minor contributor relative to crystallin genes [PMID: 38874774].
- **Inheritance:** predominantly **autosomal dominant** (HP:0000006); a rare **autosomal recessive** null form (HP:0000007) [PMID: 21836522].
- **Penetrance:** high/complete within reported pedigrees; **expressivity variable** (morphology and onset differ even for the same allele across families).
- **Anticipation / germline mosaicism:** not reported.
- **Founder effects / consanguinity:** recessive null reported in a consanguineous family [PMID: 21836522]; many dominant pedigrees are Chinese, but no established founder allele.
- **Carrier frequency:** low; private alleles.
- **Demographics:** reported families predominantly Chinese, plus European, US, and Saudi. **Sex ratio** ~1:1 (autosomal). Age distribution: presents in infancy/childhood through early adulthood.

### 10. Diagnostics

- **Clinical examination:** slit-lamp biomicroscopy is the primary diagnostic (documents morphology, laterality, progression); red-reflex testing for screening in preverbal children [PMID: 31317088]. Visual acuity assessment.
- **Biomarkers / labs / imaging:** no biochemical biomarker; imaging not required for diagnosis (B-scan ultrasound if fundus view obscured).
- **Genetic testing:** confirmatory. Recommended approach — **gene panels** for congenital/inherited cataract (including crystallins, connexins, _BFSP1/BFSP2_, _MIP_, _MAF_, _HSF4_, _PITX3_) or **whole-exome sequencing**, achieving ~80% diagnostic yield [PMID: 38874774]. Single-gene _BFSP2_ testing is appropriate when phenotype/pedigree points to it. WGS, CMA, karyotyping, FISH, mtDNA, and repeat-expansion testing are generally **not** indicated for isolated CTRCT12.
- **Omics-based diagnostics:** not used clinically.
- **Clinical criteria / differential diagnosis:** diagnosis by bilateral lens opacity + confirmatory _BFSP2_ variant. Differentials: other inherited cataract genes (crystallins CRYAA/CRYAB/CRYB/CRYG, connexins GJA3/GJA8, _MIP_, _MAF_, _HSF4_), syndromic cataracts, and metabolic/secondary cataract.
- **Screening:** cascade testing of at-risk relatives once the familial variant is known; red-reflex screening in neonates/infants.

### 11. Outcome / Prognosis

- **Survival/mortality:** CTRCT12 is **not life-limiting**; no excess mortality. Normal life expectancy.
- **Morbidity/function:** the principal morbidity is visual — reduced acuity and, if untreated in the critical period, deprivation amblyopia. With timely surgery and optical/amblyopia management, visual prognosis is generally good.
- **Complications:** largely treatment-related — visual axis opacification, glaucoma, retinal detachment, and amblyopia are the main concerns in pediatric cataract surgery [PMID: 16855998; 36107778].
- **Recovery potential:** excellent functional recovery with surgery for visually significant opacity; mild/stable opacities may never require intervention.
- **Prognostic factors:** opacity density/location, laterality, age at detection and treatment (earlier treatment → lower amblyopia risk). No molecular prognostic biomarker.

### 12. Treatment

- **Pharmacotherapy:** none disease-specific; no gene-targeted drug.
- **Advanced therapeutics (gene/cell/RNA):** none in clinical use for CTRCT12; purely theoretical given dominant-negative mechanism (allele-silencing approaches would be conceptually rational but are not developed).
- **Surgical/interventional (standard of care):** lens aspiration/extraction for visually significant opacity. *"lens opacity obscuring the red reflex in preverbal children and visual acuity of less than 20/40 is an absolute indication for lens aspiration"* [PMID: 31317088]. Technique in young children: lens aspiration with posterior capsulotomy/anterior vitrectomy; IOL implantation generally considered after age 1. NCIT suggestions: **NCIT:C157672 (Cataract Surgery)**, **NCIT:C15277 (Surgery)**, **NCIT:C62314 (Intraocular Lens)**.
- **Optical/supportive & rehabilitative:** aphakic correction (contact lens/aphakic glasses) vs IOL in under-2s [PMID: 36107778]; amblyopia therapy (patching), refractive correction.
- **Experimental:** no CTRCT12-specific trials.
- **Treatment strategy:** timing-driven (early surgery for dense bilateral/unilateral congenital opacity to prevent amblyopia; defer for mild/progressive juvenile opacity until visually significant). Personalized element = genotype confirms diagnosis and informs family planning, not drug choice.

### 13. Prevention

- **Primary prevention:** not possible for a germline Mendelian disorder; **genetic counseling** and reproductive options (prenatal testing, preimplantation genetic diagnosis) can prevent transmission once the familial variant is known.
- **Secondary prevention:** neonatal/infant **red-reflex screening** for early detection; prompt referral.
- **Tertiary prevention:** timely surgery + amblyopia management to prevent irreversible visual deprivation; post-operative monitoring for glaucoma and visual-axis opacification.
- **Immunization / public health / environmental / prophylaxis:** not applicable.
- **Counseling:** autosomal dominant → 50% transmission risk; cascade testing of relatives.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs (HomoloGene 20791):** mouse _Bfsp2_ (NCBI 107993), rat (501046), dog (608938), cow (281645), chicken (396141), zebrafish _bfsp2_ (494090), _Xenopus_ (100486639), rhesus (717551), chimp (460708). BFSP2/CP49 is a vertebrate lens-fiber–specific IF; the beaded filament is unique to vertebrate lens fiber cells.
- **Natural disease in animals:** no well-characterised naturally occurring _BFSP2_ cataract reported in companion animals/wildlife in this investigation; the natural ~6-kb _Bfsp2_ deletion in laboratory mouse strains 129/FVB/N is the notable natural variant [PMID: 17065509].
- **Comparative biology:** mechanism (beaded-filament loss → degraded optics) is evolutionarily conserved across mammalian lenses.
- **Transmission/zoonosis:** not applicable (genetic, non-infectious).

### 15. Model Organisms

- **Model type:** mammalian (mouse) is primary.
- **Specific systems & genetic models:**
  - Targeted **CP49/_Bfsp2_ knockout** (Alizadeh 2002) — beaded filaments abolished, filensin protein reduced, progressive optical-clarity loss [PMID: 12454043].
  - Independent **CP49 knockout** (Sandilands 2003) — disrupted beaded filaments, deteriorated light scatter, no frank cataract [PMID: 12573667].
  - **Natural ~6-kb _Bfsp2_ deletion** in inbred strains 129 and FVB/N — effectively a CP49 knockout and an important confounder in lens studies [PMID: 17065509; 15777782].
  - **Filensin (_Bfsp1_) knockout** — also loses CP49 beaded filaments; shows cold-cataract and AQP0-related distortion changes [PMID: 32913386; 34087204].
- **Phenotype recapitulation:** models reproduce beaded-filament loss and degraded lens optical quality, capturing the cytoskeletal mechanism. **Limitation:** knockouts are loss-of-function and produce a milder phenotype than the human **dominant-negative** disease, so they model the recessive/null end better than the dominant alleles; no knock-in of a human dominant allele (e.g., R287W, ΔE233) was identified in this investigation.
- **Resources:** MGI (_Bfsp2_ MGI:1333828), IMPC/IMSR for mouse lines.

---

## Mechanistic Model / Interpretation

```
  Dominant BFSP2 mutation (ΔE233, R287W, G112E, R339H)
            │  (rod-domain / assembly-critical)
            ▼
  Abnormal phakinin subunit produced
            │  incorporated into heteropolymer
            ▼
  DOMINANT-NEGATIVE poisoning of phakinin–filensin
  beaded-filament assembly        ── branch ──►  AR null allele (homozygous LOF)
            │                                      │  no mutant protein; het unaffected
            ▼                                      ▼
  Loss/destabilisation of beaded filaments     Absence of beaded filaments
  (+ secondary filensin protein loss)          (milder: diffuse cortical cataract)
            │
            ▼
  Fiber-cell cytoskeletal disorganisation;
  altered AQP0 interaction, biomechanics,
  refractive-index gradient
            │
            ▼
  Increased intracellular light scatter
            │
            ▼
  Bilateral lens opacity (nuclear/pulverulent,
  sutural, lamellar, cortical) — often progressive
            │
            ▼
  Visual impairment ± amblyopia  ──►  surgical lens extraction + optical/amblyopia rehab
```

The central interpretive insight unifying the genetics and the mouse models is the **dominant-negative hypothesis**. Human heterozygous null carriers are unaffected and homozygous null causes only a mild recessive cortical cataract [PMID: 21836522]; mouse CP49 knockouts likewise show degraded optics but mild/absent frank cataract [PMID: 12573667]. Yet heterozygous point mutations/in-frame deletions cause dominant, sometimes congenital, cataract. The only coherent reconciliation is that the dominant mutant protein is expressed, enters the beaded-filament heteropolymer, and actively poisons its assembly — a toxic gain-of-function that is more damaging than simple absence. The rod-domain localisation of R287W (and proximity of ΔE233) to the coiled-coil assembly interface provides the structural rationale.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in findings |
|---|---|---|
| [10739768](https://pubmed.ncbi.nlm.nih.gov/10739768/) | AD cataract with BFSP2 deletion (ΔE233) | Defines gene; first cytoskeletal-protein cataract |
| [10729115](https://pubmed.ncbi.nlm.nih.gov/10729115/) | Juvenile-onset locus 3q21–q22, R287W | Second founding allele; juvenile-onset phenotype |
| [21836522](https://pubmed.ncbi.nlm.nih.gov/21836522/) | Recessive BFSP2/PITX3 mutations | Establishes dominant-negative (non-LOF) mechanism |
| [24654948](https://pubmed.ncbi.nlm.nih.gov/24654948/) | G112E pulverulent + sutural | Expands phenotype spectrum |
| [18958306](https://pubmed.ncbi.nlm.nih.gov/18958306/) | R339H congenital lamellar | Expands allele/phenotype spectrum |
| [17982427](https://pubmed.ncbi.nlm.nih.gov/17982427/) | E233del progressive AD, 3q22.1 | Recurrent allele; progressive phenotype |
| [12454043](https://pubmed.ncbi.nlm.nih.gov/12454043/) | CP49 KO (targeted) | Beaded filaments required for optical clarity |
| [12573667](https://pubmed.ncbi.nlm.nih.gov/12573667/) | CP49 KO (independent) | Filament disruption → light scatter, no frank cataract |
| [17065509](https://pubmed.ncbi.nlm.nih.gov/17065509/) | FVB/N natural Bfsp2 deletion | Natural null mouse model / confounder |
| [15777782](https://pubmed.ncbi.nlm.nih.gov/15777782/) | Lens IF cytoskeleton review | CP49 tailless; obligate coassembly with filensin |
| [32913386](https://pubmed.ncbi.nlm.nih.gov/32913386/) | CP49/filensin & cold cataract | Beaded filaments required for cold cataract |
| [34087204](https://pubmed.ncbi.nlm.nih.gov/34087204/) | BF proteins & AQP0 | Beaded filament–AQP0 interaction, optics |
| [12084750](https://pubmed.ncbi.nlm.nih.gov/12084750/) | Australian pediatric cataract aetiology | Incidence 2.2/10,000; AD predominance |
| [38874774](https://pubmed.ncbi.nlm.nih.gov/38874774/) | BPC genetics Israel/Palestine | ~80% yield; BFSP2 minor contributor |
| [28526010](https://pubmed.ncbi.nlm.nih.gov/28526010/) | Cx50 D47N / cataract gene count | ≥26 inherited cataract genes context |
| [31317088](https://pubmed.ncbi.nlm.nih.gov/31317088/) | Pediatric cataract management | Surgical indication/standard of care |
| [36107778](https://pubmed.ncbi.nlm.nih.gov/36107778/) | Cochrane: bilateral congenital cataract <2y | IOL vs aphakia options |
| [16855998](https://pubmed.ncbi.nlm.nih.gov/16855998/) | Cochrane: bilateral congenital cataract surgery | VAO reduction; surgical evidence |

**Consistency.** The gene-defining pedigree studies (10739768, 10729115) and later alleles (17982427, 18958306, 24654948) are mutually reinforcing for causation. The mechanism finding (21836522) is independently corroborated by the milder knockout phenotypes (12454043, 12573667). No paper in the reviewed set contradicts the dominant-negative model.

---

## Limitations and Knowledge Gaps

1. **No direct biochemical proof of dominant-negative assembly in human disease.** The mechanism is strongly inferred from genetics (het null asymptomatic) plus structural reasoning, but in vitro coassembly assays of each dominant mutant with filensin were not reviewed here.
2. **No knock-in animal model of a human dominant allele.** Available mouse models are loss-of-function (knockout/natural deletion), which model the recessive/null end better than the dominant disease — a gap for therapeutic and mechanistic studies.
3. **No CTRCT12-specific epidemiology.** Prevalence/incidence are only inferable from the broader pediatric cataract literature; _BFSP2_ is a minor contributor.
4. **Genotype–phenotype correlation is incomplete.** Why specific alleles produce nuclear vs lamellar vs cortical morphology is not mechanistically resolved; expressivity is variable even within a reported allele.
5. **Population/ethnic distribution is ascertainment-biased** toward Chinese pedigrees; true global distribution and any founder effects are unknown.
6. **No omics signature** (transcriptomic/proteomic/metabolomic) exists for human CTRCT12.

## Proposed Follow-up Experiments / Actions

1. **In vitro coassembly assays** of each dominant mutant phakinin (ΔE233, R287W, G112E, R339H) with wild-type filensin to directly test and quantify the dominant-negative effect on filament formation.
2. **Knock-in mouse (or lens organoid/iPSC) models** of a human dominant allele (e.g., R287W) to recapitulate the dominant phenotype and provide a therapeutic test bed.
3. **Structural modeling/cryo-EM** of mutant-containing beaded filaments to map how rod-domain substitutions disrupt the coiled-coil assembly interface.
4. **Allele-selective silencing proof-of-concept** (ASO/siRNA/CRISPR) targeting the mutant allele in patient-derived cells, exploiting the benign heterozygous-null state.
5. **Genotype–phenotype registry** aggregating all _BFSP2_ families to correlate allele with morphology, onset, and progression, and to estimate penetrance/expressivity rigorously.
6. **Targeted gnomAD/population screening** of _BFSP2_ to estimate carrier frequency of null and dominant alleles and probe founder effects.

---

*Evidence source legend: human clinical/genetic = pedigree linkage/sequencing and surgical guidelines; model organism = mouse knockout/natural-mutant lines; in vitro = coassembly/structural (reviewed); computational = ortholog/identifier databases. All mechanistic and clinical claims are cited to PMIDs above.*


## Artifacts

- [OpenScientist final report](Cataract_12_Multiple_Types-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Cataract_12_Multiple_Types-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 23 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 17 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012701` (2 mentions) - the report calls it "MONDO"; MONDO calls it **cataract 12 multiple types**
- `HP:0007686` (1 mention) - the report calls it "Progressive/congenital cataract"; HP calls it **Abnormal pupillary function**
- `CL:0000148` (2 mentions) - the report calls it "Tissue/cell:** lens fiber cells"; CL calls it **melanocyte**
- `NCIT:C157672` (1 mention) - the report calls it "Cataract Surgery"; NCIT calls it **Indeterminate Nodule Type**
- `NCIT:C15277` (1 mention) - the report calls it "Surgery"; NCIT calls it **Mastectomy**
- `NCIT:C62314` (1 mention) - the report calls it "Intraocular Lens"; NCIT calls it **Nanofabrication**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000518` (1 mention) - the report calls it "Cataract (bilateral)"; HP calls it **Cataract**
- `HP:0010920` (1 mention) - the report calls it "Pulverulent cataract"; HP calls it **Zonular cataract**
- `HP:0100017` (1 mention) - the report calls it "Sutural cataract"; HP calls it **Capsular cataract**
- `HP:0007971` (1 mention) - the report calls it "Lamellar/zonular cataract"; HP calls it **Lamellar cataract**
- `HP:0000006` (2 mentions) - the report calls it "Autosomal dominant inheritance", "autosomal dominant", "Inheritance:** predominantly **autosomal dominant"; HP calls it **Autosomal dominant inheritance**
- `GO:0045111` (2 mentions) - the report calls it "Subcellular:** intermediate filament cytoskeleton"; GO calls it **intermediate filament cytoskeleton**
- `UBERON:0000965` (1 mention) - the report calls it "Organ:** eye lens"; UBERON calls it **lens of camera-type eye**, and lists "eye lens" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000006` - called "Autosomal dominant inheritance", "autosomal dominant", "Inheritance:** predominantly **autosomal dominant"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.