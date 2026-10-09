---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-08T13:33:01.136444'
end_time: '2026-10-08T13:54:30.998144'
duration_seconds: 1289.86
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: ACE-Related Renal Tubular Dysgenesis
  mondo_id: MONDO:0700337
  category: Mendelian
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
citation_count: 25
reference_validation:
  total_references: 25
  verified: 24
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.04
  quotes_checked: 37
  quotes_valid: 37
  relevance_assessed: 24
  on_topic: 18
  unresolved_references:
  - PMID:14713115
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 35
  verified: 33
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 1
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: HP:0001562
    reported_labels:
    - Prenatal sign
    ontology_label: Oligohydramnios
  - term_id: HP:0100736
    reported_labels:
    - Physical manifestation
    ontology_label: Abnormal soft palate morphology
  - term_id: HP:0002089
    reported_labels:
    - Clinical sign
    ontology_label: Pulmonary hypoplasia
  - term_id: HP:0002615
    reported_labels:
    - Clinical sign
    ontology_label: Hypotension
  - term_id: HP:0004719
    reported_labels:
    - Imaging
    ontology_label: Hyperechogenic kidneys
  - term_id: HP:0012622
    reported_labels:
    - Lab/clinical
    ontology_label: Chronic kidney disease
  - term_id: HP:0001903
    reported_labels:
    - Lab
    ontology_label: Anemia
  labels_variant: 6
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
  path: ACE-Related_Renal_Tubular_Dysgenesis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ACE-Related_Renal_Tubular_Dysgenesis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ACE-Related Renal Tubular Dysgenesis
- **MONDO ID:** MONDO:0700337 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ACE-Related Renal Tubular Dysgenesis** covering all of the
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

# ACE-Related Renal Tubular Dysgenesis — Comprehensive Disease Characterization Report

**Disease:** ACE-Related Renal Tubular Dysgenesis (ACE-RTD)
**MONDO ID:** MONDO:0700337 · **OMIM phenotype series:** 267430 (Renal Tubular Dysgenesis) · **Orphanet:** ORPHA:97369 · **Causal gene:** *ACE* (angiotensin I converting enzyme; HGNC:2707; UniProt P12821; EC 3.4.15.1; 17q23.3)
**Category:** Mendelian, autosomal recessive

---

## Summary

ACE-related renal tubular dysgenesis (ACE-RTD) is a severe, usually perinatally lethal, autosomal-recessive disorder of fetal kidney development caused by bi-allelic loss-of-function (LOF) variants in *ACE*, one of four interacting genes of the renin–angiotensin system (RAS). RTD as a whole is caused by bi-allelic defects in *ACE*, *REN*, *AGT*, or *AGTR1*; in the largest reported mutation series (48 unrelated families), *ACE* was the single most frequent causal gene, mutated in two-thirds (64.6%) of families ([PMID: 22095942](https://pubmed.ncbi.nlm.nih.gov/22095942/)). The disorder is defined histopathologically by the absence or poor development of differentiated proximal tubules, and clinically by early-onset and persistent fetal anuria leading to oligohydramnios and the Potter sequence, skull ossification defects, and severe refractory arterial hypotension ([PMID: 23636579](https://pubmed.ncbi.nlm.nih.gov/23636579/)).

The unifying mechanism is hemodynamic rather than morphogenetic: loss of ACE catalytic activity abolishes the conversion of angiotensin I to the vasopressor angiotensin II, producing chronically low fetal renal perfusion pressure that arrests proximal-tubule differentiation and triggers a compensatory surge of renal renin expression ([PMID: 16116425](https://pubmed.ncbi.nlm.nih.gov/16116425/)). The same phenotype can be *acquired* through fetal RAS blockade (in-utero ACE inhibitors, ARBs, NSAIDs) or through fetal hypoperfusion (donor twin of twin-twin transfusion syndrome, congenital hemochromatosis), confirming the convergent hemodynamic pathway ([PMID: 23636579](https://pubmed.ncbi.nlm.nih.gov/23636579/); [PMID: 9841703](https://pubmed.ncbi.nlm.nih.gov/9841703/)).

Although most affected fetuses die in utero or within days of birth from pulmonary hypoplasia, anuria, and intractable hypotension, intensive neonatal blood-pressure support and renal replacement therapy have produced a growing cohort of long-term survivors, who develop chronic kidney disease and a characteristic anemia out of proportion to their renal failure, attributable to loss of angiotensin II–driven erythropoietin regulation ([PMID: 32198635](https://pubmed.ncbi.nlm.nih.gov/32198635/); [PMID: 28629525](https://pubmed.ncbi.nlm.nih.gov/28629525/)). This report synthesizes 10 confirmed findings across 27 reviewed papers, organized against the full disease-characteristics template.

---

## 1. Disease Information

ACE-RTD is a Mendelian disorder of renal tubular development. RTD is "characterised by the absence or poor development of proximal tubules, early onset and persistent anuria (leading to oligohydramnios and the Potter sequence) and ossification defects of the skull" ([PMID: 23636579](https://pubmed.ncbi.nlm.nih.gov/23636579/)). The kidneys are grossly normal-sized but echogenic and **noncystic**, with poor corticomedullary differentiation — a key feature distinguishing RTD from autosomal recessive polycystic kidney disease.

**Key identifiers:**
- **OMIM:** 267430 (Renal Tubular Dysgenesis phenotype series)
- **MONDO:** MONDO:0700337 (ACE-related renal tubular dysgenesis)
- **Orphanet:** ORPHA:97369 (Renal tubular dysgenesis)
- **Gene:** *ACE* — HGNC:2707; NCBI Gene 1636; Ensembl ENSG00000159640; UniProt P12821; chromosome 17q23.3
- **MeSH / ICD:** RTD falls under congenital renal dysplasia/tubular disorders; no single dedicated ICD-10 code (classified under the Q61 group of congenital renal malformations).

**Synonyms / alternative names:** Renal tubular dysgenesis (RTD); autosomal recessive renal tubular dysgenesis (AR-RTD); congenital renal proximal tubular dysgenesis; RTD due to ACE deficiency; primary/familial renal tubular dysgenesis.

**Information source type:** The disease-level knowledge is derived from **aggregated resources** — case series, mutation cohorts, histopathology studies, and animal models — rather than individual EHR data. The largest genetic evidence base is the Gribouval et al. mutation series ([PMID: 22095942](https://pubmed.ncbi.nlm.nih.gov/22095942/)).

---

## 2. Etiology

**Primary cause — genetic (ACE subtype):** Bi-allelic (homozygous or compound heterozygous) loss-of-function variants in *ACE*. More broadly, affected individuals "had homozygous or compound heterozygous mutations in the genes encoding renin, angiotensinogen, angiotensin converting enzyme or angiotensin II receptor type 1" ([PMID: 16116425](https://pubmed.ncbi.nlm.nih.gov/16116425/)). Across RTD, "ACE mutations are the most frequent, observed in two-thirds of families (64.6%)" ([PMID: 22095942](https://pubmed.ncbi.nlm.nih.gov/22095942/)).

**Genetic risk factors:** The sole genetic risk determinant is bi-allelic *ACE* LOF. Consanguinity is a major risk amplifier (homozygosity), and affected sibs with parental consanguinity established recessive inheritance even before the gene was known ([PMID: 2359105](https://pubmed.ncbi.nlm.nih.gov/2359105/)). Carrier parents (heterozygotes) are clinically unaffected.

**Environmental / acquired risk factors (phenocopies):** Fetal exposures that inactivate or bypass the RAS reproduce the phenotype — "Secondary RTD has been observed in various situations, particularly in the donor twin of severe twin-to-twin transfusion syndrome, in foetuses affected with congenital haemochromatosis or in foetuses exposed to RAS blockers" ([PMID: 23636579](https://pubmed.ncbi.nlm.nih.gov/23636579/)). Relevant drug exposures: ACE inhibitors, angiotensin-receptor blockers (ARBs), and NSAIDs during pregnancy.

**Protective factors:** No genetic protective modifier alleles are established. The most important *modifiable* protective factor for an affected neonate is aggressive postnatal management of hypotension and renal failure, which converts an almost uniformly lethal condition into survivable CKD ([PMID: 34957720](https://pubmed.ncbi.nlm.nih.gov/34957720/)).

**Gene–environment interaction:** Genetic and acquired causes **converge on a single intermediate phenotype** — reduced fetal renal perfusion pressure. In a heterozygous *ACE* fetus, additional in-utero RAS blockade could plausibly unmask or worsen renal hypoperfusion, though this specific interaction is inferred rather than directly demonstrated.

---

## 3. Phenotypes

| Phenotype | Type | HPO suggestion | Onset | Severity | Frequency |
|---|---|---|---|---|---|
| Persistent fetal anuria/oliguria | Clinical sign | HP:0001984 (anuria) / HP:0000104 | Fetal/neonatal | Severe | Near-universal |
| Oligohydramnios | Prenatal sign | HP:0001562 | Fetal | Severe | Near-universal |
| Potter sequence (facies, limb contractures) | Physical manifestation | HP:0100736 | Fetal/neonatal | Severe | Common |
| Pulmonary hypoplasia | Clinical sign | HP:0002089 | Neonatal | Severe (often lethal) | Common |
| Refractory arterial hypotension | Clinical sign | HP:0002615 | Neonatal | Severe | Near-universal |
| Skull ossification defect (wide sutures, large fontanelles) | Physical/radiographic | HP:0004331 / HP:0000239 | Congenital | Variable | Cardinal/frequent |
| Absent/poorly developed proximal tubules | Histopathology | HP:0000112 | Fetal | Severe | Defining hallmark |
| Echogenic, noncystic kidneys, poor CMD | Imaging | HP:0004719 | Fetal/neonatal | — | Common |
| Chronic kidney disease (survivors) | Lab/clinical | HP:0012622 | Childhood/adult | Variable | Survivors |
| Anemia disproportionate to renal failure (survivors) | Lab | HP:0001903 | Childhood | Moderate–severe | Survivors |
| Polyuria–polydipsia (survivors) | Symptom | HP:0000103 / HP:0001959 | Childhood | Variable | Survivors |

Cardinal features are captured in the definition: RTD is "characterised by the absence or poor development of proximal tubules, early onset and persistent anuria (leading to oligohydramnios and the Potter sequence) and ossification defects of the skull" ([PMID: 23636579](https://pubmed.ncbi.nlm.nih.gov/23636579/)). A novel associated phenotype — microcolon/intestinal developmental failure — has been reported, "which points to a role of the renin-angiotensin system in gut development" ([PMID: 30071301](https://pubmed.ncbi.nlm.nih.gov/30071301/)).

**Quality-of-life impact:** For the classic form, QoL is dominated by perinatal lethality. In survivors, the burden is that of early-onset CKD/ESRD (dialysis, transplantation, growth impairment, anemia management) — a lifelong, high-intensity medical course.

---

## 4. Genetic / Molecular Information

**Causal gene:** *ACE* (OMIM gene 106180; phenotype RTD 267430). *ACE* is the most frequent RTD gene, and disease severity is similar regardless of which of the four RAS genes is mutated ([PMID: 22095942](https://pubmed.ncbi.nlm.nih.gov/22095942/)).

**Protein biology:** ACE is a zinc metallopeptidase of the gluzincin subfamily. "Angiotensin-I Converting Enzyme (ACE) is a Zinc Metallopeptidase of which the three-dimensional structure was unknown until recently, when the X-ray structure of testis isoform (C-terminal domain of somatic) was determined" ([PMID: 14965309](https://pubmed.ncbi.nlm.nih.gov/14965309/)). Somatic ACE carries **two homologous catalytic (zinc-binding) domains** (N- and C-domain); the testis isoform corresponds to the C-domain. ACE cleaves the C-terminal dipeptide from angiotensin I to generate the vasopressor angiotensin II and also degrades bradykinin.
- GO molecular function: peptidyl-dipeptidase activity (GO:0008241); metallopeptidase activity (GO:0008237).

**Pathogenic variants:** Bi-allelic LOF — nonsense, frameshift, splice-site, and inactivating missense variants — distributed across *ACE*. The Gribouval series reported 54 distinct mutations across 48 families, "most of them novel" ([PMID: 22095942](https://pubmed.ncbi.nlm.nih.gov/22095942/)). Functional consequence: **loss of function** (abolished or inactivated enzyme → no angiotensin II generation). Variant classification is predominantly pathogenic/likely pathogenic under ACMG/AMP for truncating alleles; individual missense alleles may require functional assay.
- **Allele frequency:** Individual pathogenic alleles are rare/private in gnomAD, consistent with a recessive lethal disorder; many are family-specific (founder effects in consanguineous pedigrees).
- **Origin:** Germline.

**Modifier genes:** No formal modifier genes are established. Notably, bi-allelic variants in **RMND1** (a mitochondrial-disease gene) can produce an RTD-like phenotype with *low* renin expression, representing a phenocopy/differential rather than a classic RAS-gene modifier ([PMID: 40366408](https://pubmed.ncbi.nlm.nih.gov/40366408/)).

**Epigenetic information:** No disease-specific DNA-methylation or histone-modification signatures have been reported for ACE-RTD. (Not available.)

**Chromosomal abnormalities:** None characteristic; ACE-RTD is a single-gene disorder, not a copy-number/structural syndrome.

---

## 5. Environmental Information

**Environmental / toxicological factors (phenocopy triggers):** In-utero RAS blockade — ACE inhibitors, ARBs — and NSAIDs reproduce RTD. A representative ACE-RTD case notes: "Acquired cases have been described in the setting of in utero exposure to medications such as nonsteroidal anti-inflammatory medications (NSAIDs) and ACE inhibitors" ([PMID: 35848000](https://pubmed.ncbi.nlm.nih.gov/35848000/)).
- CHEBI anchors: ACE inhibitor (CHEBI:35457), NSAID (CHEBI:35475).

**Lifestyle factors:** Not applicable to the genetic disorder; relevant only insofar as maternal medication use during pregnancy is avoidable.

**Infectious agents:** None. ACE-RTD is non-infectious.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

```
1. Bi-allelic ACE loss-of-function variant (germline)
        └─ leads to → absent or catalytically dead ACE protein (two zinc catalytic domains lost)
2. Loss of ACE peptidyl-dipeptidase activity
        └─ results in → failure to convert angiotensin I → angiotensin II
3. Absent angiotensin II signaling (via AGTR1)
        └─ results in → loss of efferent arteriolar tone & systemic vasopressor drive
        └─ triggers (compensatory) → massive up-regulation of renal renin expression
4. Chronically LOW fetal renal perfusion pressure / low glomerular filtration
        └─ leads to → (BRANCH A) arrest of proximal-tubule differentiation (defining lesion)
        └─ leads to → (BRANCH B) renal arterial-wall thickening (arcuate→afferent arteries)
        └─ leads to → (BRANCH C) persistent fetal anuria
5a. Persistent fetal anuria
        └─ leads to → oligohydramnios → Potter sequence + pulmonary hypoplasia
5b. Absent angiotensin II (systemic)
        └─ leads to → severe refractory neonatal arterial hypotension
5c. Reduced angiotensin II / fetal hypoperfusion (INFERRED)
        └─ leads to → skull ossification defect (membranous calvarial bone)
5d. Loss of angiotensin II–driven EPO regulation (survivors)
        └─ leads to → anemia out of proportion to renal failure
6. Convergent outcome → perinatal death (pulmonary hypoplasia + anuria + hypotension)
        └─ OR (with intensive support) → survivable chronic kidney disease
```

### Detail

**Upstream initiating lesion** is molecular: loss of ACE enzymatic activity. ACE regulates blood pressure via the RAS by cleaving the C-terminal dipeptide from angiotensin I to form the vasopressor angiotensin II — a reaction wholly abolished by bi-allelic LOF (F008; [PMID: 14965309](https://pubmed.ncbi.nlm.nih.gov/14965309/)).

**Core hemodynamic step (central node):** The defect is not a morphogenic failure of a RAS "developmental program" but a perfusion failure. Gribouval et al. "propose that renal lesions and early anuria result from chronic low perfusion pressure of the fetal kidney, a consequence of renin-angiotensin system inactivity" ([PMID: 16116425](https://pubmed.ncbi.nlm.nih.gov/16116425/)). This is corroborated by the acquired forms: in TTTS donor twins "hypoperfusion leading to decreased glomerular filtration is the underlying etiology" ([PMID: 9841703](https://pubmed.ncbi.nlm.nih.gov/9841703/)). The Gubler review reinforces the interpretation: "The absence or poor development of proximal tubules, as well as renal vascular changes, may be attributable to renal hypoperfusion rather than to a morphogenic property of the RAS" ([PMID: 19924102](https://pubmed.ncbi.nlm.nih.gov/19924102/)).

**Branch B — vascular remodeling:** Histology shows "thickening of the renal arterial vasculature, from the arcuate to the afferent arteries" alongside the proximal-tubule lesion ([PMID: 16790508](https://pubmed.ncbi.nlm.nih.gov/16790508/)).

**Compensatory renin surge:** In *ACE*/*AGT*/*AGTR1* defects, renin-producing cells are intensely stimulated because the negative-feedback signal (angiotensin II) is absent — a diagnostic fingerprint (markedly elevated plasma renin, undetectable ACE).

**Branch D — EPO/anemia (survivors):** The RAS modulates erythropoiesis. "RAS regulates EPO, an essential mediator of red cell production... The regulation of EPO expression by Ang II may be responsible for maintaining red blood cell homeostasis" ([PMID: 28629525](https://pubmed.ncbi.nlm.nih.gov/28629525/)). Thus ACE-RTD survivors show "anemia (out of proportion with the level of renal failure)" ([PMID: 32198635](https://pubmed.ncbi.nlm.nih.gov/32198635/)). The kidney's role as a "critmeter" integrating oxygen/perfusion signals to set EPO output provides the anatomical–physiological context ([PMID: 14713115](https://pubmed.ncbi.nlm.nih.gov/14713115/)).

**Pathways / processes / cell types:**
- Molecular pathway: renin–angiotensin system / angiotensin II–AGTR1 signaling (Reactome: Metabolism of Angiotensinogen to Angiotensins).
- Biological processes (GO): regulation of blood pressure (GO:0008217); renal system / nephron tubule development (GO:0072073); angiotensin maturation (GO:0002003); regulation of systemic arterial blood pressure by RAS (GO:0003081).
- Cell types (CL): kidney proximal tubule epithelial cell (CL:1000838 / CL:0002306); juxtaglomerular (renin-secreting) cell (CL:1000697); renal arterial smooth muscle cell; erythroid progenitor cell (CL:0000038).
- Subcellular (GO CC): plasma membrane / cell surface (ACE is a membrane-anchored ectoenzyme), extracellular space.

---

## 7. Anatomical Structures Affected

**Organ level:**
- Primary organ: **kidney** (UBERON:0002113) — specifically the renal cortex/proximal tubule and intrarenal arteries.
- Secondary: **lungs** (UBERON:0002048) — pulmonary hypoplasia via oligohydramnios; **skull/calvaria** (UBERON:0001684 / UBERON:0000209) — ossification defect; **cardiovascular system** — systemic hypotension; **intestine/colon** (UBERON:0001155) — microcolon in the novel association ([PMID: 30071301](https://pubmed.ncbi.nlm.nih.gov/30071301/)).
- Body systems: renal/urinary, cardiovascular, respiratory, skeletal, hematopoietic.

**Tissue and cell level:**
- Renal epithelial tissue — proximal tubule epithelium fails to differentiate (defining lesion): "significantly impacting the proximal tubules of the kidney while maintaining an anatomically normal gross structure" ([PMID: 38649831](https://pubmed.ncbi.nlm.nih.gov/38649831/)).
- Renal arterial smooth muscle — hypertrophy/thickening from arcuate to afferent arteries ([PMID: 16790508](https://pubmed.ncbi.nlm.nih.gov/16790508/)).
- Juxtaglomerular renin-producing cells — hyperplastic/over-expressing.

**Subcellular level:** ACE is a type-I transmembrane ectoenzyme; relevant compartments are the plasma membrane / cell surface (GO:0005886) and extracellular space.

**Localization / lateralization:** Bilateral and symmetric renal involvement; kidneys are diffusely enlarged and echogenic.

---

## 8. Temporal Development

**Onset:** Congenital/fetal. Anuria and oligohydramnios are detectable prenatally (second trimester onward); "Severe defects in proximal tubules were observed in all fetuses from 18 gestational weeks onward" ([PMID: 16790508](https://pubmed.ncbi.nlm.nih.gov/16790508/)). Onset pattern is chronic-progressive in utero with acute neonatal decompensation at birth.

**Progression:**
- Classic course: in-utero or neonatal death within days, from pulmonary hypoplasia, anuria, and refractory hypotension ([PMID: 23636579](https://pubmed.ncbi.nlm.nih.gov/23636579/)).
- Survivor course: progressive chronic kidney disease; "Bi-allelic loss of function mutation of ACE can have atypical and sometimes late presentation with chronic renal failure, anemia... and polyuro-polydipsia" ([PMID: 32198635](https://pubmed.ncbi.nlm.nih.gov/32198635/)). Most surviving RTD patients reach CKD stage 5 at a young age.
- An extreme survival example: a premature infant survived 61 days with anuria (AR-RTD) ([PMID: 40709124](https://pubmed.ncbi.nlm.nih.gov/40709124/)).

**Patterns / critical periods:** The critical window is the perinatal transition — intensive BP support in the first days/weeks determines survival. There is no spontaneous remission; renal damage is permanent.

---

## 9. Inheritance and Population

**Inheritance:** Autosomal recessive, established early: "The disorder is, therefore, thought to be inherited in an autosomal recessive manner" ([PMID: 2359105](https://pubmed.ncbi.nlm.nih.gov/2359105/)).

**Penetrance / expressivity:** Bi-allelic LOF is highly penetrant for the renal/anuric phenotype. Expressivity is variable chiefly in survival and skull-ossification severity; notably, severity is "similar regardless of the mutated gene" across RTD subtypes ([PMID: 22095942](https://pubmed.ncbi.nlm.nih.gov/22095942/)).

**Consanguinity / founder effects:** Consanguinity strongly increases risk (homozygosity); multiple consanguineous pedigrees and a Bedouin survivor cohort illustrate founder/population clustering ([PMID: 34957720](https://pubmed.ncbi.nlm.nih.gov/34957720/)).

**Epidemiology:** RTD is rare but, per one study title, "a not uncommon autosomal recessive disorder leading to oligohydramnios" among RAS-related fetal nephropathies ([PMID: 16790508](https://pubmed.ncbi.nlm.nih.gov/16790508/)). Precise prevalence/incidence figures per 100,000 are not well established (rare disease; likely under-ascertained due to fetal/neonatal lethality). Sex ratio is approximately equal (autosomal). No specific geographic endemicity beyond consanguineous-population clustering.

**Carrier frequency:** Individual pathogenic *ACE* alleles are rare in gnomAD; aggregate carrier frequency is not formally established.

---

## 10. Diagnostics

**Diagnostic signature (biochemical + imaging):** "Basal plasma renin activity was markedly elevated and angiotensin-converting enzyme was undetectable" ([PMID: 32808512](https://pubmed.ncbi.nlm.nih.gov/32808512/)). Imaging shows diffusely enlarged, echogenic, **noncystic** kidneys with poor corticomedullary differentiation; skull X-ray shows large fontanelles / wide sutures.

**Clinical presentation prompting work-up:** "Renal tubular dysgenesis should be suspected in any neonate presenting with renal failure, refractory hypotension, ventilator requirement, hypoplastic lungs, renal ultrasound showing normal-sized echogenic noncystic kidneys with poor corticomedullary differentiation, and antenatal history significant for oligohydramnios" ([PMID: 35848000](https://pubmed.ncbi.nlm.nih.gov/35848000/)).

**Histopathology (gold-standard pathological hallmark):** Absence/paucity of differentiated proximal tubules with renal arterial wall thickening ([PMID: 16790508](https://pubmed.ncbi.nlm.nih.gov/16790508/)). Immunohistochemistry shows absent proximal-tubule ACE/angiotensinogen and strikingly increased renin.

**Genetic testing:** Confirmatory. Whole-exome sequencing identifies bi-allelic *ACE* variants (as in the postnatal-diagnosis case, WES showing "2 pathologic mutations in the angiotensin-converting enzyme (ACE) gene") ([PMID: 35848000](https://pubmed.ncbi.nlm.nih.gov/35848000/)). A targeted **RAS gene panel (ACE, REN, AGT, AGTR1)** is appropriate; whole-genome sequencing is warranted in unsolved cases and has identified phenocopies such as *RMND1* ([PMID: 40366408](https://pubmed.ncbi.nlm.nih.gov/40366408/)).

**Differential diagnosis:** ARPKD (cystic vs noncystic kidneys), other congenital anomalies of the kidney and urinary tract (CAKUT), obstructive uropathy, and acquired/secondary RTD (TTTS donor, congenital hemochromatosis, fetal RAS-blocker exposure). *RMND1*-mitochondrial disease mimics RTD but with **low** (not high) renin ([PMID: 40366408](https://pubmed.ncbi.nlm.nih.gov/40366408/)).

**Screening:** Prenatal — oligohydramnios on ultrasound; family-based cascade genetic testing and prenatal diagnosis in known-mutation families ([PMID: 20122389](https://pubmed.ncbi.nlm.nih.gov/20122389/)).

---

## 11. Outcome / Prognosis

**Survival / mortality:** Historically near-uniformly lethal: "death usually occurs in utero or within days of birth" from pulmonary hypoplasia, anuria, and hypotension ([PMID: 23636579](https://pubmed.ncbi.nlm.nih.gov/23636579/)). "A few long term survivors were reported during the last decade" following intensive neonatal care ([PMID: 34957720](https://pubmed.ncbi.nlm.nih.gov/34957720/)). In a Bedouin cohort, 5 survivors (4 with *ACE* mutations) reached ages 5–20 with variable CKD stages.

**Morbidity:** Survivors have early-onset CKD, often progressing to ESRD requiring dialysis/transplantation, with growth impairment and disproportionate anemia ([PMID: 32198635](https://pubmed.ncbi.nlm.nih.gov/32198635/)). A broader renal-oligohydramnios cohort (including RTD) showed 30% mortality and universal CKD in survivors, but "long-term outcome in survivors is encouraging" with multidisciplinary care ([PMID: 17065192](https://pubmed.ncbi.nlm.nih.gov/17065192/)).

**Prognostic factors:** The decisive factor is the intensity and success of early blood-pressure and renal-replacement support; the trend is that the "overall prognosis of patients with RTD continues to improve with better ventilatory management and renal replacement therapies" ([PMID: 35848000](https://pubmed.ncbi.nlm.nih.gov/35848000/)).

---

## 12. Treatment

ACE-RTD has **no curative therapy**; management is supportive and organ-sustaining.

- **Neonatal stabilization / BP support (NCIT: vasopressor therapy):** Intensive management of refractory hypotension with multiple inotropes/vasopressors is the single most important survival determinant ([PMID: 35848000](https://pubmed.ncbi.nlm.nih.gov/35848000/); [PMID: 34957720](https://pubmed.ncbi.nlm.nih.gov/34957720/)).
- **Respiratory support (NCIT: mechanical ventilation):** For pulmonary hypoplasia; frequently complicated by pneumothoraces ([PMID: 35848000](https://pubmed.ncbi.nlm.nih.gov/35848000/)).
- **Renal replacement therapy (NCIT: dialysis / renal transplantation):** Peritoneal dialysis/hemodialysis for anuria; kidney transplantation in longer-term survivors ([PMID: 17065192](https://pubmed.ncbi.nlm.nih.gov/17065192/)).
- **Anemia management:** Erythropoiesis-stimulating agents / iron, given the EPO-dependent disproportionate anemia ([PMID: 32198635](https://pubmed.ncbi.nlm.nih.gov/32198635/); [PMID: 28629525](https://pubmed.ncbi.nlm.nih.gov/28629525/)).
- **CKD supportive care:** Growth hormone for growth impairment, electrolyte/acid-base management, nutrition ([PMID: 17065192](https://pubmed.ncbi.nlm.nih.gov/17065192/)).
- **Genotype-informed caution:** In the related *AGTR1*-LOF survivor, fludrocortisone was useful "to treat hyperkalemia and salt-wasting," illustrating a mineralocorticoid-based strategy for RAS-deficiency tubulopathy ([PMID: 33768328](https://pubmed.ncbi.nlm.nih.gov/33768328/)). Angiotensin II supplementation is a theoretical but unproven mechanistic target in ACE-RTD.

No gene, cell, or RNA-based therapies exist for ACE-RTD. No NCT-registered disease-specific trials were identified.

---

## 13. Prevention

- **Primary prevention:** Avoid in-utero RAS blockers (ACE inhibitors, ARBs) and NSAIDs in pregnancy to prevent acquired RTD ([PMID: 35848000](https://pubmed.ncbi.nlm.nih.gov/35848000/)). For the genetic disorder, prevention is reproductive.
- **Genetic counseling / reproductive options:** For carrier couples (25% recurrence risk per pregnancy), counseling, prenatal diagnosis, and preimplantation genetic testing are the principal preventive tools; molecular diagnosis "now allow[s] genetic counseling and early prenatal diagnosis" ([PMID: 20122389](https://pubmed.ncbi.nlm.nih.gov/20122389/)).
- **Secondary prevention:** Prenatal detection via oligohydramnios surveillance in at-risk pregnancies; cascade testing in families with a known proband variant.
- **Tertiary prevention:** In survivors, standard CKD complication prevention (anemia, bone-mineral, growth, cardiovascular).

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *ACE* is conserved; mouse *Ace* (NCBI Gene 11421), rat *Ace*. No naturally occurring companion-animal RTD analog is well documented (not reported in OMIA for this specific entity).
- **Comparative biology:** RAS-gene knockouts in mice reproduce key features (see §15) but are milder than human disease — attributed to "differences between mice and humans in the time of nephrogenesis and maturation of the RAS" ([PMID: 19924102](https://pubmed.ncbi.nlm.nih.gov/19924102/)). Evolutionary conservation of the RAS underlies the cross-species recapitulation.
- **Zoonotic potential:** None (genetic, non-infectious).

---

## 15. Model Organisms

Mouse RAS-pathway knockouts partially recapitulate RTD, validating the hemodynamic mechanism while illustrating species limits.

| Model | Renal/vascular phenotype | Severity vs human | Reference |
|---|---|---|---|
| *Ace*−/− (knockout) | Abnormal renal structure/function, hypotension, male sterility; vascular (not proximal-tubule) ACE needed for normal BP | Milder | [PMID: 12777443](https://pubmed.ncbi.nlm.nih.gov/12777443/) |
| *Agt*−/− (angiotensinogen KO) | Renal arterial wall hypertrophy + interstitial fibrosis | Milder | [PMID: 29230587](https://pubmed.ncbi.nlm.nih.gov/29230587/) |
| *Agtr1a*−/− (AT1A receptor KO) | JGA hypertrophy, renin-cell expansion; **no** severe vascular lesions/papillary atrophy | Mildest | [PMID: 9458822](https://pubmed.ncbi.nlm.nih.gov/9458822/) |
| Pharmacologic (early-life captopril/losartan in SHR) | Intrarenal arterial hypertrophy; later malignant hypertension | Induced model | [PMID: 14717927](https://pubmed.ncbi.nlm.nih.gov/14717927/) |

Key quotes: *Ace* "genetic ablation in mice causes abnormal renal structure and functions, hypotension, and male sterility" ([PMID: 12777443](https://pubmed.ncbi.nlm.nih.gov/12777443/)); and for AT1A-KO, "We did not find the severe renal vascular lesions or papillary atrophy that have been observed in angiotensinogen- or angiotensin converting enzyme-deficient animals" ([PMID: 9458822](https://pubmed.ncbi.nlm.nih.gov/9458822/)) — establishing a severity gradient (Ace/Agt > Agtr1a) that mirrors the convergent-hemodynamics model.

**Model limitations:** Mice do not reproduce the full lethal human phenotype (persistent anuria, skull defects), due to timing differences in nephrogenesis/RAS maturation. **Resources:** MGI, IMPC, IMSR for *Ace*/*Agt*/*Agtr1a* alleles.

---

## Key Findings (with evidence)

### F001 — ACE is the most frequent causal gene in autosomal-recessive RTD
In 48 unrelated families with 54 distinct mutations, *ACE* was mutated in 64.6% — "ACE mutations are the most frequent, observed in two-thirds of families" ([PMID: 22095942](https://pubmed.ncbi.nlm.nih.gov/22095942/)). The four causal RAS genes and recessive inheritance were established by Gribouval 2005: affected individuals "had homozygous or compound heterozygous mutations in the genes encoding renin, angiotensinogen, angiotensin converting enzyme or angiotensin II receptor type 1" ([PMID: 16116425](https://pubmed.ncbi.nlm.nih.gov/16116425/)). OMIM 267430.

### F002 — Core phenotype quartet
Fetal anuria → oligohydramnios/Potter sequence, skull ossification defects, and refractory hypotension, with absent/poor proximal tubules as the histological hallmark ([PMID: 23636579](https://pubmed.ncbi.nlm.nih.gov/23636579/)). Histology: "Severe defects in proximal tubules were observed in all fetuses from 18 gestational weeks onward... associated with thickening of the renal arterial vasculature, from the arcuate to the afferent arteries" ([PMID: 16790508](https://pubmed.ncbi.nlm.nih.gov/16790508/)).

### F003 — Mechanism: RAS inactivity → chronic fetal renal hypoperfusion → tubular-differentiation failure
"We propose that renal lesions and early anuria result from chronic low perfusion pressure of the fetal kidney, a consequence of renin-angiotensin system inactivity" ([PMID: 16116425](https://pubmed.ncbi.nlm.nih.gov/16116425/)); the acquired form confirms "hypoperfusion leading to decreased glomerular filtration is the underlying etiology" ([PMID: 9841703](https://pubmed.ncbi.nlm.nih.gov/9841703/)).

### F004 — Phenotype spectrum includes survivors with CKD
"Bi-allelic loss of function mutation of ACE can have atypical and sometimes late presentation with chronic renal failure, anemia (out of proportion with the level of renal failure), and polyuro-polydipsia" ([PMID: 32198635](https://pubmed.ncbi.nlm.nih.gov/32198635/)); "a few long term survivors were reported during the last decade" ([PMID: 34957720](https://pubmed.ncbi.nlm.nih.gov/34957720/)).

### F005 — Mouse RAS-KO models partially recapitulate RTD with a severity gradient
See §15; Ace/Agt-KO show severe vascular lesions, AT1A-KO does not ([PMID: 12777443](https://pubmed.ncbi.nlm.nih.gov/12777443/); [PMID: 9458822](https://pubmed.ncbi.nlm.nih.gov/9458822/)).

### F006 — Acquired (secondary) RTD phenocopies the genetic disease
TTTS donor twin, congenital hemochromatosis, and fetal RAS-blocker exposure cause secondary RTD ([PMID: 23636579](https://pubmed.ncbi.nlm.nih.gov/23636579/)); a novel ACE-RTD–microcolon association "points to a role of the renin-angiotensin system in gut development" ([PMID: 30071301](https://pubmed.ncbi.nlm.nih.gov/30071301/)).

### F007 — Diagnostic signature: high renin + undetectable ACE + noncystic echogenic kidneys
"Basal plasma renin activity was markedly elevated and angiotensin-converting enzyme was undetectable" ([PMID: 32808512](https://pubmed.ncbi.nlm.nih.gov/32808512/)); grossly normal architecture "significantly impacting the proximal tubules... while maintaining an anatomically normal gross structure" ([PMID: 38649831](https://pubmed.ncbi.nlm.nih.gov/38649831/)).

### F008 — ACE is a two-domain zinc gluzincin whose LOF abolishes angiotensin II generation
"Angiotensin-I Converting Enzyme (ACE) is a Zinc Metallopeptidase..." with a known C-domain X-ray structure ([PMID: 14965309](https://pubmed.ncbi.nlm.nih.gov/14965309/)). Two catalytic zinc domains make its loss a biochemical null for angiotensin II production.

### F009 — Disproportionate anemia explained by loss of angiotensin II–driven erythropoiesis
"RAS regulates EPO, an essential mediator of red cell production... The regulation of EPO expression by Ang II may be responsible for maintaining red blood cell homeostasis" ([PMID: 28629525](https://pubmed.ncbi.nlm.nih.gov/28629525/)); survivors show "anemia (out of proportion with the level of renal failure)" ([PMID: 32198635](https://pubmed.ncbi.nlm.nih.gov/32198635/)).

### F010 — Autosomal recessive inheritance established early; skull-ossification mechanism remains inferred
"The disorder is, therefore, thought to be inherited in an autosomal recessive manner" ([PMID: 2359105](https://pubmed.ncbi.nlm.nih.gov/2359105/)). Skull ossification defects are cardinal across RAS subtypes ([PMID: 22095942](https://pubmed.ncbi.nlm.nih.gov/22095942/)), but the molecular basis of the calvarial defect is **not experimentally demonstrated** — inferred to reflect reduced angiotensin II signaling and/or chronic fetal hypoperfusion of membranous bone, paralleling ACE-inhibitor fetopathy.

---

## Mechanistic Model / Interpretation

```
          ┌──────────────────────────────────────────────────────────────┐
          │  Bi-allelic ACE LOF  (OR fetal RAS blockade / hypoperfusion)   │
          └───────────────────────────────┬──────────────────────────────┘
                                           │  no Ang I → Ang II conversion
                                           ▼
                        ┌──────────────────────────────┐
                        │  ABSENT ANGIOTENSIN II SIGNAL │◄── compensatory renin ↑↑
                        └───────┬───────────────┬───────┘
           low renal perfusion │               │ low systemic vascular tone
                               ▼               ▼
         ┌──────────────────────────┐   ┌─────────────────────────┐
         │ Renal: proximal-tubule   │   │ Systemic: refractory     │
         │ differentiation ARREST + │   │ neonatal hypotension     │
         │ arterial wall thickening │   └─────────────────────────┘
         └───────────┬──────────────┘
                     │ persistent fetal anuria
                     ▼
         ┌──────────────────────────┐    ┌───────────────────────────┐
         │ Oligohydramnios → Potter  │    │ Skull ossification defect  │
         │ sequence + pulmonary      │    │ (INFERRED: hypoperfusion   │
         │ hypoplasia                │    │  of membranous bone)       │
         └───────────┬──────────────┘    └───────────────────────────┘
                     ▼
      ┌───────────────────────────────┐   with intensive BP + RRT support
      │ Perinatal death (lungs/anuria/ │ ───────────────► Survivable CKD
      │ hypotension)                   │                   + EPO-dependent anemia
      └───────────────────────────────┘
```

The model's strength is **convergence**: genetically distinct lesions (*ACE*, *REN*, *AGT*, *AGTR1*) and non-genetic insults (TTTS, hemochromatosis, drugs) all funnel through a single node — absent angiotensin II action → fetal renal hypoperfusion — and produce an indistinguishable phenotype of similar severity regardless of gene. This argues that RTD is fundamentally a **perfusion/physiology disorder**, not a developmental-patterning disorder. The mouse severity gradient (Ace/Agt-KO severe; Agtr1a-KO mild) is consistent with the human picture and reinforces that upstream/global RAS loss is more damaging than single-receptor loss.

---

## Evidence Base

| PMID | Role | Support / challenge |
|---|---|---|
| [16116425](https://pubmed.ncbi.nlm.nih.gov/16116425/) | Gene discovery; hypoperfusion mechanism | Supports F001, F003 |
| [22095942](https://pubmed.ncbi.nlm.nih.gov/22095942/) | Largest mutation series; ACE = 64.6% | Supports F001, F010 |
| [23636579](https://pubmed.ncbi.nlm.nih.gov/23636579/) | Authoritative review; cardinal features + acquired forms | Supports F002, F006 |
| [16790508](https://pubmed.ncbi.nlm.nih.gov/16790508/) | Histopathology + vascular thickening | Supports F002 |
| [9841703](https://pubmed.ncbi.nlm.nih.gov/9841703/) | TTTS acquired RTD; hypoperfusion | Supports F003, F006 |
| [32198635](https://pubmed.ncbi.nlm.nih.gov/32198635/) | Atypical/survivor ACE-RTD with anemia | Supports F004, F009 |
| [34957720](https://pubmed.ncbi.nlm.nih.gov/34957720/) | Survivor cohort | Supports F004 |
| [12777443](https://pubmed.ncbi.nlm.nih.gov/12777443/) | Ace-KO mouse | Supports F005 |
| [9458822](https://pubmed.ncbi.nlm.nih.gov/9458822/) | AT1A-KO milder; severity gradient | Supports F005 |
| [29230587](https://pubmed.ncbi.nlm.nih.gov/29230587/) | Agt-KO arterial hypertrophy | Supports F005 |
| [30071301](https://pubmed.ncbi.nlm.nih.gov/30071301/) | ACE-RTD + microcolon novel association | Supports F006 |
| [32808512](https://pubmed.ncbi.nlm.nih.gov/32808512/) | Diagnostic signature (renin↑, ACE undetectable) | Supports F007 |
| [38649831](https://pubmed.ncbi.nlm.nih.gov/38649831/) | Normal gross architecture, proximal-tubule lesion | Supports F007 |
| [14965309](https://pubmed.ncbi.nlm.nih.gov/14965309/) | ACE protein structure (two zinc domains) | Supports F008 |
| [28629525](https://pubmed.ncbi.nlm.nih.gov/28629525/) | Ang II regulates EPO | Supports F009 |
| [2359105](https://pubmed.ncbi.nlm.nih.gov/2359105/) | Early AR inheritance | Supports F010 |
| [35848000](https://pubmed.ncbi.nlm.nih.gov/35848000/) | Diagnostic clues; acquired drug causes; improving prognosis | Context/diagnostics |
| [33768328](https://pubmed.ncbi.nlm.nih.gov/33768328/) | AGTR1-LOF survivor; fludrocortisone | Treatment analogy |
| [40366408](https://pubmed.ncbi.nlm.nih.gov/40366408/) | RMND1 phenocopy (low renin) | Differential diagnosis |
| [17065192](https://pubmed.ncbi.nlm.nih.gov/17065192/) | Renal-oligohydramnios long-term outcome | Prognosis |
| [19924102](https://pubmed.ncbi.nlm.nih.gov/19924102/) | Review; hypoperfusion vs morphogenic; mouse–human difference | Supports F003, F005 |
| [20122389](https://pubmed.ncbi.nlm.nih.gov/20122389/) | Gene distribution; counseling/prenatal dx | Prevention |
| [14717927](https://pubmed.ncbi.nlm.nih.gov/14717927/) | Pharmacologic RAS-blockade arterial model | Supports mechanism |
| [14713115](https://pubmed.ncbi.nlm.nih.gov/14713115/) | Kidney "critmeter" / EPO & Ang II | Supports F009 |
| [40709124](https://pubmed.ncbi.nlm.nih.gov/40709124/) | Infant surviving 61 days with anuria | Prognosis/survival |

---

## Limitations and Knowledge Gaps

1. **Skull ossification mechanism is unproven.** The calvarial defect is cardinal but its molecular basis (reduced angiotensin II signaling vs chronic hypoperfusion of membranous bone) is **inferred**, not experimentally demonstrated (F010).
2. **Epidemiology is imprecise.** No reliable prevalence/incidence per 100,000; the disorder is under-ascertained due to fetal/neonatal lethality and variable prenatal diagnosis.
3. **Mouse models under-recapitulate** the lethal human phenotype (no persistent anuria, no skull defect), limiting mechanistic dissection of the most severe features.
4. **No disease-specific therapeutics.** No trials, gene/cell therapy, or angiotensin-II–replacement strategy has been tested; survivor management is extrapolated from general CKD/neonatology.
5. **Genotype–phenotype correlation is weak** within *ACE* — severity is similar across RAS genes, and specific *ACE* alleles are not clearly tied to survival.
6. **The microcolon/gut association** rests on few cases (n=3) and needs confirmation.

---

## Proposed Follow-up Experiments / Actions

1. **Conditional, temporally-controlled *Ace* knockdown in fetal mice** across the human-equivalent nephrogenesis window to test whether later/graded RAS loss reproduces proximal-tubule arrest and anuria (addresses model-recapitulation gap).
2. **Calvarial-specific studies** (µCT + in-situ angiotensin-signaling readouts) in *Ace*/*Agt*-deficient fetuses to directly test the hypoperfusion-vs-signaling hypothesis for skull under-ossification.
3. **Natural-history registry** of ACE-RTD survivors (BP course, GFR trajectory, anemia/EPO levels, transplant outcomes) to quantify prognosis and define evidence-based management.
4. **Functional classification of *ACE* missense variants** via enzymatic activity/expression assays to improve ACMG classification and prenatal counseling.
5. **Proof-of-concept angiotensin II or RAS-restoration therapy** in neonatal survivors or models, given that absent angiotensin II is the central node.
6. **Systematic screening for *RMND1* and other mitochondrial genes** in RAS-gene-negative RTD-like fetuses to refine the differential (low-renin phenocopies).
7. **Confirm the RTD–microcolon association** in additional cohorts and characterize intestinal RAS expression.

---

*Report compiled from 10 confirmed findings across 27 reviewed papers. Evidence source types span human clinical case series/cohorts, model-organism (mouse) genetics, histopathology, and protein-structural/biochemical data.*


## Artifacts

- [OpenScientist final report](ACE-Related_Renal_Tubular_Dysgenesis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ACE-Related_Renal_Tubular_Dysgenesis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 37 |
| Quoted claims found in source | 37 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 24 |
| On topic | 18 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:14713115` (4 mentions) - Identifier did not resolve to a record

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 14 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001562` (1 mention) - the report calls it "Prenatal sign"; HP calls it **Oligohydramnios**
- `HP:0100736` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Abnormal soft palate morphology**
- `HP:0002089` (1 mention) - the report calls it "Clinical sign"; HP calls it **Pulmonary hypoplasia**
- `HP:0002615` (1 mention) - the report calls it "Clinical sign"; HP calls it **Hypotension**
- `HP:0004719` (1 mention) - the report calls it "Imaging"; HP calls it **Hyperechogenic kidneys**
- `HP:0012622` (1 mention) - the report calls it "Lab/clinical"; HP calls it **Chronic kidney disease**
- `HP:0001903` (1 mention) - the report calls it "Lab"; HP calls it **Anemia**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000112` (1 mention) - the report calls it "Histopathology"; HP calls it **Nephropathy**
- `GO:0008241` (1 mention) - the report calls it "GO molecular function: peptidyl-dipeptidase activity"; GO calls it **peptidyl-dipeptidase activity**
- `CHEBI:35457` (1 mention) - the report calls it "CHEBI anchors: ACE inhibitor"; CHEBI calls it **EC 3.4.15.1 (peptidyl-dipeptidase A) inhibitor**, and lists "ACE inhibitor" among its other names
- `UBERON:0002113` (1 mention) - the report calls it "kidney", "Primary organ: **kidney"; UBERON calls it **kidney**, and lists "reniculate kidney" among its other names
- `UBERON:0002048` (1 mention) - the report calls it "lungs", "Secondary: **lungs"; UBERON calls it **lung**
- `UBERON:0001155` (1 mention) - the report calls it "intestine/colon"; UBERON calls it **colon**, and lists "posterior intestine" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0002113` - called "kidney", "Primary organ: **kidney"
- `UBERON:0002048` - called "lungs", "Secondary: **lungs"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.