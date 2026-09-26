---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-24T23:37:26.800026'
end_time: '2026-09-24T23:52:10.896049'
duration_seconds: 884.1
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Trench Fever
  mondo_id: MONDO:0005991
  category: Infectious Disease
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
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 20
  on_topic: 15
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 26
  verified: 26
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 2
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0005991
    reported_labels:
    - if available
    ontology_label: trench fever
  - term_id: HP:0001945
    reported_labels:
    - relapsing, ~5-day periodicity
    ontology_label: Fever
  - term_id: HP:0002653
    reported_labels:
    - shin/tibia
    ontology_label: Bone pain
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Trench_Fever-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Trench_Fever-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Trench Fever
- **MONDO ID:** MONDO:0005991 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Trench Fever** covering all of the
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

# Trench Fever (Bartonella quintana infection): A Comprehensive Disease Characteristics Report

**Disease:** Trench Fever · **MONDO ID:** MONDO:0005991 · **Category:** Infectious Disease
**Causal agent:** *Bartonella quintana* (α-proteobacteria; formerly *Rochalimaea quintana*)
**ICD-10:** A79.0 · **ICD-11:** 1C30.0 · **MeSH:** D014205 (Trench Fever)
Evidence base: aggregated disease-level literature (reviews, case-control studies, one randomized trial, experimental microbiology). No individual EHR or genomic data files were provided; this report synthesizes primary literature retrieved via PubMed (27 papers reviewed, 11 findings confirmed).

---

## Summary

Trench fever is a **louse-borne bacterial infection** caused by *Bartonella quintana*, a small, fastidious, facultatively intracellular α-proteobacterium that is **restricted to a single natural reservoir — humans — and a single principal vector, the human body louse (*Pediculus humanus humanus*)**. First characterized in 1915 among soldiers in the trenches of World War I (hence the name), the disease has re-emerged over the past three decades as **"urban trench fever"** among homeless and socially marginalized populations in high-income cities in the US and Europe ([PMID: 16494745](https://pubmed.ncbi.nlm.nih.gov/16494745/)). It is fundamentally a **disease of poverty and body-louse infestation**, not a genetic disease; there are no known human causal genes, susceptibility loci, or heritable risk factors.

Clinically, *B. quintana* produces a **broad spectrum** running from the classic self-limited relapsing febrile illness ("five-day fever," with headache and severe shin/tibial bone pain) through **chronic afebrile bacteremia**, **blood-culture-negative endocarditis**, **chronic lymphadenopathy**, and — particularly in immunocompromised hosts such as people with HIV — the **vasoproliferative disorders bacillary angiomatosis and peliosis** ([PMID: 16494745](https://pubmed.ncbi.nlm.nih.gov/16494745/); [PMID: 15891120](https://pubmed.ncbi.nlm.nih.gov/15891120/)). Two mechanistic axes dominate the pathophysiology: (1) the laterally acquired **Trw type IV secretion system (T4SS)** mediates host-specific adhesion to and invasion of erythrocytes, producing the hallmark long-lasting intraerythrocytic bacteremia; and (2) a suite of factors — the **Vomps** trimeric autotransporter adhesins, the **VirB/VirD4 T4SS with its Bep effectors**, and the **BafA autotransporter (a VEGF analog)** — converge on **HIF-1/VEGF signaling** to drive endothelial proliferation, tube formation, and angiogenesis ([PMID: 20548954](https://pubmed.ncbi.nlm.nih.gov/20548954/); [PMID: 32678094](https://pubmed.ncbi.nlm.nih.gov/32678094/); [PMID: 21536788](https://pubmed.ncbi.nlm.nih.gov/21536788/); [PMID: 23163798](https://pubmed.ncbi.nlm.nih.gov/23163798/)).

Diagnosis rests on serology, blood culture (often prolonged), and molecular detection (PCR of *gltA*/*ftsZ*/16S rRNA). The best-supported treatment for chronic bacteremia is **doxycycline plus gentamicin**, validated by a randomized open trial (eradication in 7/7 per-protocol treated vs 2/9 controls, P=0.003) ([PMID: 12821469](https://pubmed.ncbi.nlm.nih.gov/12821469/)) and a systematic review/meta-analysis ([PMID: 23602630](https://pubmed.ncbi.nlm.nih.gov/23602630/)). Prevention is fundamentally **body-louse control and improved hygiene/social conditions**; there is no vaccine. This report synthesizes 11 confirmed findings across all 15 template sections.

---

## Key Findings

### Finding 1 — Trench fever is caused by *Bartonella quintana*, a human-restricted, louse-borne pathogen

*Bartonella quintana* is an α-proteobacterium (formerly *Rochalimaea quintana*) whose lifestyle is **restricted to human hosts and louse vectors**. It was the first *Bartonella* species definitively linked to human disease and was characterized as the agent of trench fever, a disease **"described in 1915 on the basis of natural and experimental infections in soldiers"** ([PMID: 16494745](https://pubmed.ncbi.nlm.nih.gov/16494745/)). After decades of relative obscurity, it re-emerged as a pathogen of the **urban homeless**: in a study of homeless persons, *B. quintana* was isolated from blood culture in **5.3% of patients** ([PMID: 15643300](https://pubmed.ncbi.nlm.nih.gov/15643300/)).

The verbatim evidence: *"Bartonella quintana, a pathogen that is restricted to human hosts and louse vectors, was first characterized as the agent of trench fever. The disease was described in 1915 on the basis of natural and experimental infections in soldiers"* ([PMID: 16494745](https://pubmed.ncbi.nlm.nih.gov/16494745/)).

**Key identifiers:** MONDO:0005991; ICD-10 A79.0; ICD-11 1C30.0; MeSH D014205. This is an **infectious, aggregated disease-level entity** — knowledge is derived from case series, cohort studies, microbiology, and molecular biology, not from Mendelian/EHR genetic resources (no OMIM/Orphanet gene entry applies because it is not heritable). Common synonyms: five-day fever, quintan fever, His-Werner disease, shin bone fever, wolhynia fever, urban trench fever.

### Finding 2 — *B. quintana* causes a clinical spectrum from classic trench fever to chronic bacteremia, endocarditis, and bacillary angiomatosis

*B. quintana* is **"responsible for a wide spectrum of conditions, including chronic bacteremia, endocarditis, and bacillary angiomatosis"** ([PMID: 16494745](https://pubmed.ncbi.nlm.nih.gov/16494745/)). The classic acute syndrome is a relapsing fever recurring at ~5-day intervals ("quintana" = fifth), with **headache, dizziness, and characteristic severe pain in the shins/tibiae**. Beyond the acute illness, chronic afebrile bacteremia can persist for months; endocarditis is an important severe outcome. In a series from Sfax, Tunisia, *B. quintana* endocarditis **"represents 9.8% of all endocarditis"** in that setting, with high IgG titers (≥1:800) supporting the diagnosis ([PMID: 15891120](https://pubmed.ncbi.nlm.nih.gov/15891120/)). Chronic infection can also present as isolated lymphadenopathy/adenomegaly, including in seronegative patients ([PMID: 8727894](https://pubmed.ncbi.nlm.nih.gov/8727894/)). In immunocompromised hosts (notably HIV), the organism drives **vasoproliferative** disease — bacillary angiomatosis and peliosis.

| Clinical syndrome | Host context | Key features | HPO/phenotype terms |
|---|---|---|---|
| Classic trench fever | Immunocompetent | Relapsing 5-day fever, headache, severe shin/bone pain | Fever HP:0001945; Headache HP:0002315; Bone pain HP:0002653 |
| Chronic afebrile bacteremia | Homeless, louse-exposed | Persistent intraerythrocytic bacteremia | Bacteremia HP:0031864 |
| Blood-culture-negative endocarditis | Valvulopathy/chronic infection | Vegetations, high IgG titers; may need valve surgery | Endocarditis HP:0100584 |
| Chronic lymphadenopathy | Sometimes seronegative | Adenomegaly | Lymphadenopathy HP:0002716 |
| Bacillary angiomatosis / peliosis | Immunocompromised (HIV) | Vasoproliferative skin/bone/visceral lesions | Cutaneous vascular lesions |

### Finding 3 — Trw T4SS mediates erythrocyte invasion; BafA drives VEGF-dependent angiogenesis

Two experimentally demonstrated virulence mechanisms anchor the pathophysiology.

**(1) Erythrocyte invasion via the Trw T4SS.** Using signature-tagged mutagenesis in surrogate *Bartonella* species, the **Trw type IV secretion system** was shown to be directly involved in erythrocyte adhesion; its genes **"encode components of the type IV secretion system (T4SS) Trw, demonstrating that this virulence factor laterally acquired by the Bartonella lineage is directly involved in adherence to erythrocytes"** ([PMID: 20548954](https://pubmed.ncbi.nlm.nih.gov/20548954/)). This host-specific adhesion enables the hallmark **long-lasting intraerythrocytic bacteremia**.

**(2) VEGF-driven vasoproliferation via BafA.** The *Bartonella* autotransporter **BafA acts as a VEGF analog**: **"BafA interacts with vascular endothelial growth factor (VEGF) receptor-2 and activates the downstream signaling pathway, suggesting that BafA functions as a VEGF analog. A BafA homolog from a related pathogen, Bartonella quintana, is also functional"** ([PMID: 32678094](https://pubmed.ncbi.nlm.nih.gov/32678094/)). This explains the vasoproliferative lesions (bacillary angiomatosis) directly at the molecular level.

### Findings 4 & 10 — Treatment: doxycycline + gentamicin eradicates chronic bacteremia (randomized + meta-analytic evidence)

The best-supported regimen for **chronic *B. quintana* bacteremia** is **doxycycline plus gentamicin**. A **randomized open trial** (Foucault, Raoult, Brouqui 2003) in homeless patients with blood-culture-positive *B. quintana* compared gentamicin 3 mg/kg/day IV for 14 days + doxycycline 200 mg/day orally for 28 days versus no treatment. **"Intention-to-treat analysis of 20 included patients showed eradication of bacteremia in 7 out of 9 treated patients versus 2 out of 11 untreated controls (P = 0.01). In the per-protocol analysis, eradication was obtained for 7 out of 7 treated patients versus 2 out of 9 untreated controls (P = 0.003)"** ([PMID: 12821469](https://pubmed.ncbi.nlm.nih.gov/12821469/)).

A **systematic review and meta-analysis** of human bartonellosis treatment corroborates this: **"In chronic bacteremia, gentamicin and doxycycline significantly increased the resolution rate"** ([PMID: 23602630](https://pubmed.ncbi.nlm.nih.gov/23602630/)) — though the authors note the evidence base is limited and dominated by observational studies at high risk of bias. Expert-guideline regimens (Rolain et al. 2004) extend this: **endocarditis** typically requires prolonged therapy (often doxycycline + an aminoglycoside) and may require **valve surgery**; **bacillary angiomatosis** responds to macrolides (erythromycin) or doxycycline given for months. NCIT term suggestions: Doxycycline (NCIT:C692), Gentamicin (NCIT:C575), Erythromycin (NCIT:C608).

### Finding 5 — *B. quintana* has a reduced ~1.58 Mb genome shaped by secondary genome reduction; T4SS drives host adaptation

Comparative genomics of the genus shows *Bartonella* are α-proteobacteria with **host-restricted lifestyles characterized by long-lasting intraerythrocytic infection in a specific mammalian reservoir and arthropod transmission**. Among sequenced genomes (circular chromosomes 1.44–2.62 Mb; 1,283–2,136 genes; a synthenic core of 959 genes), *B. quintana* underwent **"massive secondary genome reduction"** — it has the **smallest genome (~1.58 Mb, ~1,300 genes)** — consistent with adaptation to a single human host plus louse vector ([PMID: 19696500](https://pubmed.ncbi.nlm.nih.gov/19696500/)). The **type IV secretion systems (Trw, VirB/VirD4)** were laterally acquired and are **"type IV secretion systems that adopted prominent roles in host adaptation and specificity"** ([PMID: 19696500](https://pubmed.ncbi.nlm.nih.gov/19696500/)). This reductive evolution reflects the pathogen's dependence on host-derived metabolites (host-integrated metabolism) and its narrow ecological niche.

### Finding 6 — Bacillary angiomatosis is epidemiologically linked to homelessness, low income, and lice, with subcutaneous and lytic bone lesions

A case-control study of 49 HIV-associated bacillary angiomatosis-peliosis patients versus 96 matched controls found that **23/49 (47%) were *B. quintana*** and **26/49 (53%) *B. henselae***. Crucially, tissue tropism differed by species: **"Subcutaneous and lytic bone lesions were strongly associated with B. quintana, whereas peliosis hepatis was associated exclusively with B. henselae"** ([PMID: 9407154](https://pubmed.ncbi.nlm.nih.gov/9407154/)). Risk factors also segregated: patients **"with B. quintana were clustered and were characterized by low income (P=0.003), homelessness (P = 0.004), and exposure to lice (P= 0.03)"**, whereas *B. henselae* was tied to cat/flea exposure ([PMID: 9407154](https://pubmed.ncbi.nlm.nih.gov/9407154/)). This confirms both the **skin/bone tissue tropism** of *B. quintana* and its **socioeconomic risk profile**.

### Finding 7 — Transmission is via infectious body-louse feces (horizontal); no true transovarial (vertical) transmission

Humans acquire *B. quintana* through **contaminated body-louse feces**, not the louse bite directly: **"Horizontal transmission from the body louse vector (Pediculus humanus humanus) to a human host occurs through contact with infectious louse feces containing a high concentration of the bacteria"** — typically inoculated into skin abrasions or bite-scratch excoriations ([PMID: 35803580](https://pubmed.ncbi.nlm.nih.gov/35803580/)). Controlled experiments testing vertical transmission found bacterial DNA on egg surfaces (fecal contamination of the egg sheath) but no viable organisms internally: **"viable B. quintana could not be cultured from the hemolymph of adult female lice or from within eggs that were surface sterilized, indicating a lack of true transovarial transmission"** ([PMID: 35803580](https://pubmed.ncbi.nlm.nih.gov/35803580/)). Vertical transfer therefore **"probably has a limited impact on the dynamics of transmission to humans."** This has direct public-health implications: interrupting the human↔louse cycle (delousing) breaks transmission.

### Finding 8 — Vomps adhesins and the VirB/D4 T4SS–Bep effector system converge on HIF-1/VEGF to drive vasoproliferation

*B. quintana* expresses **variably expressed outer membrane proteins (Vomps)**, which are **trimeric autotransporter adhesins (TAAs)** analogous to *B. henselae*'s **Bartonella adhesin A (BadA)**. In a study of adherence under static and bloodstream-like dynamic flow, investigators **"analyzed three different TAAs (Bartonella adhesin A [BadA] of Bartonella henselae, variably expressed outer membrane proteins [Vomps] of Bartonella quintana, and Yersinia adhesin A [YadA] of Yersinia enterocolitica) for mediating bacterial adherence to ECM and endothelial cells"** ([PMID: 21536788](https://pubmed.ncbi.nlm.nih.gov/21536788/)) — establishing Vomps as *B. quintana*'s ECM/endothelial adhesins (binding fibronectin, collagen).

Mechanistically, in the closely related *B. henselae* the pathway is well defined: **"Expression of Bartonella adhesin A (BadA) is crucial for bacterial autoagglutination, adhesion to host cells, binding to extracellular matrix proteins and proangiogenic reprogramming via activation of hypoxia inducible factor (HIF)-1"** ([PMID: 18627378](https://pubmed.ncbi.nlm.nih.gov/18627378/)). In parallel, the **VirB/VirD4 T4SS** delivers effector proteins into endothelial cells: **"VirB/D4 translocates several Bartonella effector proteins (Beps) into the cytoplasm of infected ECs, resulting, e.g. in uptake of bacterial aggregates via the invasome structure, inhibition of apoptosis and activation of a proangiogenic phenotype"** ([PMID: 23163798](https://pubmed.ncbi.nlm.nih.gov/23163798/)). Notably, BadA and VirB/D4 are frequently mutually exclusive during in vitro passage — a phase-variation phenomenon relevant to culture-dependent diagnostics.

### Finding 9 — Humans are the primary reservoir, but *B. quintana* DNA is increasingly detected in animals; dogs model *Bartonella* endocarditis

The natural reservoir of *B. quintana* is **humans (NCBI Taxon 9606)**, transmitted by the body louse. However, molecular surveys increasingly detect *B. quintana* DNA in **non-human hosts**. A survey of pet cats in Urmia, Iran found **"15 % of the cats (30 out of 200 blood samples) tested positive for the B. quintana gene, with a 95 % confidence interval of 10.71 % to 20.61 %"** (100% sequence identity to the reference) ([PMID: 38199070](https://pubmed.ncbi.nlm.nih.gov/38199070/)). For comparative disease modeling, **dogs** develop naturally occurring *Bartonella* endocarditis, making **"canids... the most interesting naturally occurring animal model for the human disease"** ([PMID: 12860639](https://pubmed.ncbi.nlm.nih.gov/12860639/)). Experimental mechanistic work uses **surrogate rodent-adapted species** — **"mouse-specific Bartonella birtlesii, human-specific Bartonella quintana, cat-specific Bartonella henselae and rat-specific Bartonella tribocorum"** in adhesion/invasion assays ([PMID: 20548954](https://pubmed.ncbi.nlm.nih.gov/20548954/)) — and the body louse itself serves as an in-vivo vector model.

### Finding 11 — Epidemiology: ~5% of sheltered homeless bacteremic; rising; worldwide wherever body lice occur

In a 4-year study of 930 homeless people in Marseilles, **lice were found in 22%**, and *B. quintana* was **isolated from blood culture in 50 (5.3%)**; critically, **"the number of bacteremic patient increased from 3.4% to 8.4% (p = 0.02) over the 4 years of the study"** — evidence of a rising trend ([PMID: 15643300](https://pubmed.ncbi.nlm.nih.gov/15643300/)). Geographically, the pathogen is **cosmopolitan wherever body-louse infestation occurs**: a molecular survey of body lice detected **"the presence of B. quintana in lice collected from all locations except the Congo"** — spanning France, Russia, Peru, Zimbabwe, and Burundi ([PMID: 9986818](https://pubmed.ncbi.nlm.nih.gov/9986818/)). *B. quintana* is one of only **three body-louse-borne human pathogens**, alongside *Rickettsia prowazekii* (epidemic typhus) and *Borrelia recurrentis* (louse-borne relapsing fever); co-exposure occurs, with documented *R. prowazekii* seroconversion in a *B. quintana*-bacteremic homeless person ([PMID: 15891141](https://pubmed.ncbi.nlm.nih.gov/15891141/)).

---

## Mechanistic Model / Interpretation

### Ordered causal chain: from louse feces to clinical disease

```
1.  Body louse (Pediculus humanus humanus) feeds on a bacteremic human
        │ leads to
2.  B. quintana replicates in the louse gut and is shed in LOUSE FECES
    (high bacterial concentration; NOT transovarial — no vertical spread)
        │ results in
3.  Contaminated feces inoculated into skin abrasions / bite-scratch
    excoriations of a new human host (horizontal transmission)
        │ leads to
4.  Bacteria seed a primary niche (endothelial cells / dermal tissue)
        │ then (via Trw T4SS)
5.  Trw type IV secretion system mediates HOST-SPECIFIC ADHESION to and
    INVASION of erythrocytes
        │ results in
6.  Long-lasting INTRAERYTHROCYTIC BACTEREMIA (immune-privileged niche;
    enables relapsing fever + chronic bacteremia + louse re-acquisition)
        │
        ├─► BRANCH A (acute/chronic systemic disease):
        │       relapsing 5-day fever, headache, severe shin/bone pain;
        │       chronic afebrile bacteremia → endocarditis (valve
        │       vegetations, culture-negative)
        │
        └─► BRANCH B (vasoproliferative disease, esp. immunocompromised):
                Vomps (TAAs) adhere to ECM (fibronectin/collagen) + endothelium
                        │ + VirB/D4 T4SS translocates Bep effectors
                        │ + BafA autotransporter binds VEGFR-2 (VEGF analog)
                        │ results in
                HIF-1 activation → VEGF secretion (autocrine/paracrine loop)
                inhibition of endothelial apoptosis; invasome-mediated uptake
                        │ leads to
                ENDOTHELIAL PROLIFERATION → tube formation → ANGIOGENESIS
                        │ results in
                Bacillary angiomatosis (skin, LYTIC BONE lesions),
                vasoproliferative tumors
```

**Upstream vs downstream.** The **initiating lesion** is environmental/behavioral (louse infestation + poverty), not genetic. The **most upstream molecular event** in host colonization is Trw-mediated erythrocyte tropism, which sustains the bacteremic reservoir. The **vasoproliferative arm** is downstream of endothelial adhesion (Vomps/BadA) and effector delivery (VirB/D4-Bep, BafA), all converging on the **HIF-1 → VEGF** hub. Note that Trw (erythrocyte invasion) and VirB/D4 (endothelial reprogramming) are distinct T4SSs with distinct target cells. The HIF-1/VEGF steps are directly demonstrated for *B. henselae* BadA and **inferred** for *B. quintana* via its homologous Vomps and functional BafA homolog.

**Cell types and processes (ontology suggestions).**
- Erythrocyte (CL:0000232) — intracellular niche; GO:0007155 cell adhesion; GO:0044409 entry into host.
- Endothelial cell (CL:0000115) — angiogenesis target; GO:0001525 angiogenesis; GO:0043066 negative regulation of apoptotic process; GO:0001666 response to hypoxia (HIF-1).
- Anatomical sites (UBERON): blood (UBERON:0000178), skin/dermis (UBERON:0002067), bone (UBERON:0001474), heart valve/endocardium (UBERON:0002165), lymph node (UBERON:0000029), liver (peliosis, mainly *B. henselae*; UBERON:0002107).
- Chemical/biomarker entities (CHEBI): doxycycline (CHEBI:50845); gentamicin (CHEBI:27412).

### Comparative species pathophysiology

| Feature | *B. quintana* (trench fever) | *B. henselae* (cat-scratch) |
|---|---|---|
| Reservoir / vector | Human / body louse | Cat / cat flea |
| Adhesin (TAA) | Vomps | BadA |
| Risk factors | Homelessness, poverty, lice | Cat contact, flea exposure |
| BA tissue tropism | Subcutaneous + **lytic bone** lesions | **Peliosis hepatis** |
| Genome | ~1.58 Mb (most reduced) | ~1.9 Mb |

---

## Section-by-Section Template Coverage

- **§1 Disease Info / §5 Infectious agent:** *B. quintana* (α-proteobacterium); MONDO:0005991, ICD-10 A79.0, ICD-11 1C30.0, MeSH D014205. Synonyms: five-day/quintan/shin-bone/wolhynia fever, His-Werner disease, urban trench fever. Aggregated disease-level knowledge.
- **§2 Etiology / risk factors:** Infectious etiology; risk = homelessness, poverty, low income, body-louse infestation, poor hygiene, cold climate/crowding, alcoholism; immunosuppression (HIV) for vasoproliferative disease. **No genetic causal or protective factors** (not heritable); no meaningful gene-environment interaction reported.
- **§3 Phenotypes:** Fever HP:0001945 (relapsing, ~5-day periodicity), Headache HP:0002315, Bone pain HP:0002653 (shin/tibia), Splenomegaly HP:0001744, Bacteremia HP:0031864, Endocarditis HP:0100584, Lymphadenopathy HP:0002716. Onset acute (adult, occupational/social exposure); severity variable (mild self-limited → severe endocarditis).
- **§4 Genetic/molecular:** **Not applicable to the human host** — no causal genes, pathogenic variants, modifier genes, or chromosomal abnormalities. Relevant "genes" are *bacterial* virulence loci: *trw* (T4SS), *virB/virD4* (T4SS + *bep* effectors), *vomp* family, *bafA*.
- **§6 Mechanism:** See causal chain above.
- **§7 Anatomy:** Blood/erythrocytes (primary), vascular endothelium, skin/dermis, bone (lytic lesions), cardiac valves/endocardium, lymph nodes, spleen.
- **§8 Temporal:** Incubation ~15–30 days; acute relapsing fever often self-limited over weeks; chronic bacteremia/endocarditis can persist months–years if untreated (chronic, insidious course).
- **§9 Epidemiology:** ~5% bacteremia prevalence in sheltered homeless (rising); worldwide wherever body lice occur; predominantly adult; male predominance in homeless cohorts (demographic, not biological). Not inherited — inheritance/penetrance/expressivity sections not applicable.
- **§10 Diagnostics:** Serology (IFA IgG, titers ≥1:800 support endocarditis), prolonged blood culture, PCR/sequencing of *gltA*, *ftsZ*, 16S rRNA; histopathology (Warthin-Starry silver stain) for bacillary angiomatosis; echocardiography for endocarditis. Differential: culture-negative endocarditis (*Coxiella*, *Tropheryma*), other *Bartonella*, epidemic typhus, relapsing fever.
- **§11 Prognosis:** Acute trench fever generally self-limited and non-fatal; endocarditis carries substantial morbidity/mortality and often needs valve surgery; good response to appropriate antibiotics.
- **§12 Treatment:** Doxycycline + gentamicin (chronic bacteremia, RCT-supported); doxycycline ± aminoglycoside for endocarditis (+ surgery); macrolides/doxycycline for bacillary angiomatosis.
- **§13 Prevention:** Body-louse control (delousing, hygiene, insecticide-treated clothing), improved housing/social conditions, health education; no vaccine ([PMID: 20822446](https://pubmed.ncbi.nlm.nih.gov/20822446/)).
- **§14 Other species:** Human reservoir (NCBI:txid9606); molecular detection in cats/dogs/other animals; dogs = natural endocarditis model.
- **§15 Model organisms:** Surrogate rodent-adapted *Bartonella* (*B. birtlesii*, *B. tribocorum*); body louse as vector model; endothelial-cell and erythrocyte in-vitro assays.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports finding(s) | Contribution |
|---|---|---|---|
| [16494745](https://pubmed.ncbi.nlm.nih.gov/16494745/) | *B. quintana characteristics and clinical management* | F1, F2 | Causal agent, host/vector restriction, 1915 origin, clinical spectrum, diagnostics |
| [15643300](https://pubmed.ncbi.nlm.nih.gov/15643300/) | *Ectoparasitism... 930 homeless, Marseilles* | F1, F11 | 5.3% bacteremia; rising 3.4%→8.4%; 22% louse prevalence |
| [20548954](https://pubmed.ncbi.nlm.nih.gov/20548954/) | *Trw T4SS mediates host-specific RBC adhesion* | F3, F9 | Trw T4SS = erythrocyte invasion; surrogate species models |
| [32678094](https://pubmed.ncbi.nlm.nih.gov/32678094/) | *BafA activates host VEGF pathway* | F3 | BafA = VEGF analog binding VEGFR-2; *B. quintana* homolog functional |
| [15891120](https://pubmed.ncbi.nlm.nih.gov/15891120/) | *High prevalence of B. quintana endocarditis, Sfax* | F2 | Endocarditis burden (9.8% of all endocarditis) |
| [23602630](https://pubmed.ncbi.nlm.nih.gov/23602630/) | *Treatment outcomes of human bartonellosis (meta-analysis)* | F4 | Doxy+gentamicin ↑ resolution of chronic bacteremia |
| [12821469](https://pubmed.ncbi.nlm.nih.gov/12821469/) | *Randomized trial gentamicin+doxycycline* | F10 | RCT: 7/7 vs 2/9 eradication (P=0.003) |
| [19696500](https://pubmed.ncbi.nlm.nih.gov/19696500/) | *Genomics of host-restricted Bartonella* | F5 | Massive secondary genome reduction; T4SS host adaptation |
| [9407154](https://pubmed.ncbi.nlm.nih.gov/9407154/) | *Molecular epidemiology of bacillary angiomatosis* | F6 | Skin/bone tropism; low income/homeless/lice associations |
| [35803580](https://pubmed.ncbi.nlm.nih.gov/35803580/) | *Vertical transmission in body lice* | F7 | Horizontal fecal transmission; no transovarial spread |
| [21536788](https://pubmed.ncbi.nlm.nih.gov/21536788/) | *TAA-dependent adherence under flow* | F8 | Vomps = *B. quintana* TAA; ECM/endothelial adhesion |
| [23163798](https://pubmed.ncbi.nlm.nih.gov/23163798/) | *BadA interferes with VirB/D4 effector translocation* | F8 | VirB/D4-Bep proangiogenic, anti-apoptotic reprogramming |
| [18627378](https://pubmed.ncbi.nlm.nih.gov/18627378/) | *BadA head crucial for host cell interaction* | F8 | TAA adhesion → HIF-1 activation |
| [38199070](https://pubmed.ncbi.nlm.nih.gov/38199070/) | *B. quintana in pet cats, Iran* | F9 | 15% cat detection — expanding host range |
| [12860639](https://pubmed.ncbi.nlm.nih.gov/12860639/) | *Persistent Bartonella bacteremia in humans/animals* | F9 | Dogs as natural endocarditis model |
| [9986818](https://pubmed.ncbi.nlm.nih.gov/9986818/) | *Body lice as tools for surveillance* | F11 | Worldwide distribution in lice |
| [15891141](https://pubmed.ncbi.nlm.nih.gov/15891141/) | *Autochthonous epidemic typhus + B. quintana* | F11 | Co-circulation of louse-borne pathogens |
| [20822446](https://pubmed.ncbi.nlm.nih.gov/20822446/) | *Arthropod-borne diseases & social disorder* | F4 (prevention) | Vector control as primary prevention |
| [11871479](https://pubmed.ncbi.nlm.nih.gov/11871479/) | *Infections in the homeless* | F1, F6 | Homeless disease context |
| [8727894](https://pubmed.ncbi.nlm.nih.gov/8727894/) | *B. quintana in seronegative hemodialyzed patient* | F2 | Chronic adenomegaly; seronegative presentation; gentamicin response |

---

## Limitations and Knowledge Gaps

1. **Mechanistic inference across species.** Much of the vasoproliferative signaling detail (HIF-1 activation, VirB/D4-Bep effector biology, BadA structure–function) is demonstrated in *B. henselae* and **inferred for *B. quintana*** via the homologous Vomps/BafA systems. Direct *B. quintana* endothelial-reprogramming studies are comparatively sparse. The BafA VEGFR-2 interaction was shown functional for the *B. quintana* homolog, but the full downstream cascade in *B. quintana* is extrapolated.

2. **Treatment evidence is thin.** The pivotal RCT enrolled only 20 patients ([PMID: 12821469](https://pubmed.ncbi.nlm.nih.gov/12821469/)), and the meta-analysis explicitly flags that most treatment evidence is observational and at high risk of bias ([PMID: 23602630](https://pubmed.ncbi.nlm.nih.gov/23602630/)). Optimal duration for endocarditis, and management of relapse, remain guideline/expert-opinion driven.

3. **Epidemiology is likely underestimated.** Fastidious culture requirements and non-specific clinical presentation mean cases are under-ascertained; prevalence figures derive largely from urban homeless cohorts in France and may not generalize globally. Population-level incidence rates (new cases/100,000/yr) are not well established.

4. **Expanding host range uncertain in significance.** Detection of *B. quintana* DNA in cats, dogs, non-human primates, and other animals ([PMID: 38199070](https://pubmed.ncbi.nlm.nih.gov/38199070/)) raises the question of whether animals are competent reservoirs or incidental/spillover hosts. Whether these represent transmission risk to humans is unresolved.

5. **No human genetic component** — the template's genetic/variant/inheritance/heritable-model sections are **not applicable**; any "susceptibility" is socioeconomic and behavioral, not genomic.

6. **Quality-of-life and disability data** specific to trench fever (EQ-5D, SF-36, PROMIS) are essentially absent in the literature; QoL impact is inferred from the burden of chronic bacteremia/endocarditis and the comorbidities of the affected homeless population.

---

## Proposed Follow-up Experiments / Actions

1. **Direct *B. quintana* vasoproliferation assays.** Test purified *B. quintana* BafA and Vomps in human endothelial cells for HIF-1 stabilization, VEGF secretion, tube formation, and apoptosis inhibition — to replace *B. henselae* inference with species-specific data.

2. **Larger, multicenter treatment trial.** A pragmatic RCT (or well-designed prospective registry) across multiple homeless-service settings to define the optimal antibiotic regimen and duration for chronic bacteremia and endocarditis, and to quantify relapse.

3. **Global surveillance via body lice.** Extend the molecular-surveillance approach ([PMID: 9986818](https://pubmed.ncbi.nlm.nih.gov/9986818/)) to systematically map *B. quintana* prevalence in body lice and homeless populations worldwide, including incidence estimation.

4. **Reservoir-competence studies in animals.** Determine whether cats/dogs/primates with detectable *B. quintana* DNA harbor viable, transmissible bacteria and whether alternative arthropod vectors participate — clarifying zoonotic risk.

5. **Public-health intervention evaluation.** Rigorously evaluate delousing/hygiene/housing interventions for their effect on *B. quintana* incidence, integrating vector control per [PMID: 20822446](https://pubmed.ncbi.nlm.nih.gov/20822446/).

6. **Biomarker/diagnostic development.** Develop rapid point-of-care serologic or molecular assays suited to low-resource, homeless-service settings to improve case ascertainment and shorten time-to-treatment.

---

## Consensus Answer

Trench fever is a **louse-borne bacterial infection caused by *Bartonella quintana*** (MONDO:0005991; ICD-10 A79.0), a human-restricted α-proteobacterium transmitted through the feces of the body louse (*Pediculus humanus humanus*) and re-emerging among the urban homeless worldwide. It is **not a genetic disease** — risk is socioeconomic (homelessness, poverty, body lice, poor hygiene; immunosuppression for vasoproliferative forms) — and it spans a clinical spectrum from classic relapsing five-day fever with shin pain to chronic bacteremia, culture-negative endocarditis, and bacillary angiomatosis, driven mechanistically by **Trw-T4SS–mediated erythrocyte invasion** plus **Vomps/BadA-, VirB/D4-Bep–, and BafA-driven HIF-1/VEGF endothelial proliferation**. It is effectively treated with **doxycycline plus gentamicin** (randomized-trial evidence) and prevented by **body-louse control**; no vaccine exists.


## Artifacts

- [OpenScientist final report](Trench_Fever-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Trench_Fever-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 20 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 5 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005991` (5 mentions) - the report calls it "if available"; MONDO calls it **trench fever**
- `HP:0001945` (2 mentions) - the report calls it "relapsing, ~5-day periodicity"; HP calls it **Fever**
- `HP:0002653` (2 mentions) - the report calls it "shin/tibia"; HP calls it **Bone pain**
