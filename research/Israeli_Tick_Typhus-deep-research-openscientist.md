---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-27T23:30:52.282348'
end_time: '2026-09-27T23:47:36.323337'
duration_seconds: 1004.04
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Israeli Tick Typhus
  mondo_id: MONDO:0000230
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
citation_count: 45
reference_validation:
  total_references: 45
  verified: 45
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 45
  on_topic: 24
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 34
  verified: 34
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 31
  labels_matching: 25
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0031137
    reported_labels:
    - Abnormal circulating coagulation protein concentration
    ontology_label: Storage in hepatocytes
  - term_id: HP:0002624
    reported_labels:
    - vasculitis-related manifestations
    ontology_label: Abnormal venous morphology
  - term_id: NCIT:C692
    reported_labels:
    - Doxycycline
    ontology_label: Nimodipine
  - term_id: NCIT:C376
    reported_labels:
    - Chloramphenicol
    ontology_label: Cisplatin
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Israeli_Tick_Typhus-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Israeli_Tick_Typhus-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Israeli Tick Typhus
- **MONDO ID:** MONDO:0000230 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Israeli Tick Typhus** covering all of the
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

# Israeli Tick Typhus (Israeli Spotted Fever): A Comprehensive Disease Characteristics Report

**Disease:** Israeli Tick Typhus / Israeli Spotted Fever (ISF)
**MONDO ID:** MONDO:0000230
**Category:** Infectious Disease (tick-borne spotted-fever-group rickettsiosis)
**Causative agent:** *Rickettsia conorii* subsp. *israelensis*
**Identifiers:** MONDO:0000230 · ICD-10 A77.1 · ICD-11 1C30.0 · MeSH D001907 (Boutonneuse Fever)

---

## Summary

Israeli Tick Typhus, more precisely termed **Israeli Spotted Fever (ISF)**, is a tick-borne, spotted-fever-group (SFG) rickettsiosis caused by the obligate intracellular Gram-negative bacterium ***Rickettsia conorii* subsp. *israelensis***. It is a clinical and etiological variant of **Mediterranean spotted fever (MSF) / boutonneuse fever**, distinguished from the classic *R. conorii* subsp. *conorii* (Malish) strain by multi-locus sequence typing (MLST) and by a more virulent clinical phenotype. The disease is transmitted by the **brown dog tick, *Rhipicephalus sanguineus***, which serves as both vector and reservoir, with domestic dogs acting as amplifying/sentinel hosts. This report synthesizes 16 confirmed findings drawn from 61 papers reviewed across a five-iteration investigation.

The core pathophysiology is a **disseminated small-vessel vasculitis**: rickettsiae enter through the dermis at the tick-bite site, spread hematogenously, and infect **vascular endothelial cells**—most critically in the brain and lungs—driving increased microvascular permeability, edema, platelet/coagulation activation, and multi-organ dysfunction. Clinically, fever and maculopapular rash are near-universal, but unlike classic MSF the diagnostic eschar (*tache noire*) is frequently **absent**, and a history of tick bite is often lacking, which contributes to diagnostic delay. The ISF strain is associated with a **case-fatality of ~20–30%** in hospitalized/severe cohorts, with older age, alcoholism, G6PD deficiency, and delayed treatment as major prognostic risk factors.

Management is straightforward and highly effective when timely: **doxycycline** is the drug of choice and is curative even as a single-day 200 mg course, with josamycin, clarithromycin, and (historically) chloramphenicol as alternatives for children and pregnant women. There is **no vaccine**; prevention rests on tick-bite avoidance and integrated *Rhipicephalus sanguineus* vector control on dogs and premises. ISF is a **zoonosis** whose geographic range—historically the Mediterranean basin (Israel, Italy, Portugal)—is now documented across multiple continents (Iran, Uganda, Ghana), reflecting the global spread of the brown dog tick.

---

## Key Findings

### Finding 1 — Disease identity: ISF is caused by *R. conorii* subsp. *israelensis*, one of four MLST-defined subspecies

Multi-locus sequence typing of 39 isolates/tick amplicons resolved four *R. conorii* genotypes: the **Malish** type, **Indian tick typhus (ITTR)** type, **Astrakhan fever (AFR)** type, and the **Israeli spotted fever (ISFR)** type. Pairwise similarity across the *16S rRNA, gltA, ompA, ompB,* and *sca4* loci ranged 98.2–100%, supporting classification at the **subspecies (not species) rank** ([PMID: 15766388](https://pubmed.ncbi.nlm.nih.gov/15766388/)). ISF is therefore *R. conorii* subsp. *israelensis*, a member of the *R. conorii* complex and a variant of Mediterranean spotted fever / boutonneuse fever ([PMID: 28408252](https://pubmed.ncbi.nlm.nih.gov/28408252/)).

> *"Among the 39 isolates or tick amplicons studied, four MLST genotypes were identified: i) the Malish type; ii) the ITTR type; iii) the AFR type; and iv) the ISFR type."* — [PMID: 15766388](https://pubmed.ncbi.nlm.nih.gov/15766388/)

**Key identifiers:** MONDO:0000230; **ICD-10 A77.1** (Spotted fever due to *Rickettsia conorii*; includes Boutonneuse/Marseilles/Mediterranean tick fever); **ICD-11 1C30.0**; **MeSH D001907** (Boutonneuse Fever); NCBI Taxonomy pathogen *Rickettsia conorii* subsp. *israelensis*. **Synonyms:** Israeli spotted fever, Israeli tick typhus, a form of Mediterranean spotted fever / boutonneuse fever / fièvre boutonneuse. Information is derived from **aggregated disease-level sources** (case series, cohorts, case reports), not single-patient EHR data.

### Finding 2 — The ISF strain is more virulent than Malish; alcoholism and older age predict fatal outcome

A prospective Portuguese study of **140 strain-identified *R. conorii* patients (1994–2006; 71 Malish, 69 ISF)** found that **29 adults (21%) died**, and that fatal outcome was **significantly more likely with the ISF strain**, with **alcoholism** identified as a risk factor ([PMID: 18582199](https://pubmed.ncbi.nlm.nih.gov/18582199/)). The pathophysiology of fatal disease involved significantly greater incidence of petechial rash, gastrointestinal symptoms, obtundation/confusion, dehydration, tachypnea, hepatomegaly, leukocytosis, coagulopathy, azotemia, hyperbilirubinemia, and elevated hepatic enzymes and creatine kinase.

> *"A fatal outcome was significantly more likely for patients infected with the ISF strain, and alcoholism was a risk factor."* — [PMID: 18582199](https://pubmed.ncbi.nlm.nih.gov/18582199/)

Note a nuance: a separate Portuguese analysis (n=94) found that neither eschar presence (Malish 49% vs ISF 39%) nor fatality differed *statistically* between strains ([PMID: 16481514](https://pubmed.ncbi.nlm.nih.gov/16481514/)), suggesting the "greater severity" concept, while supported by the larger prospective cohort and Israeli national data, should be interpreted with the caveat of cohort-dependent effect sizes.

### Finding 3 — Pathophysiology: endothelial infection drives vasculitis, platelet/coagulation activation, and microthrombi

In MSF patients, in vivo biochemical evidence showed **TXA2-dependent platelet activation** (urinary 11-dehydro-TXB2), **thrombin generation** (prothrombin fragment 1+2), and **endothelial dysfunction** (plasma endothelin-1) ([PMID: 8584998](https://pubmed.ncbi.nlm.nih.gov/8584998/)). In *R. conorii*-infected mice, rickettsiae localize to the endothelium and selectively modulate antioxidant enzymes (GPx, GR, G6PD, SOD); the antioxidant alpha-lipoic acid was protective, implicating **oxidative injury** ([PMID: 15120155](https://pubmed.ncbi.nlm.nih.gov/15120155/)). Severe ISF can progress to **purpura fulminans and DIC** ([PMID: 29664383](https://pubmed.ncbi.nlm.nih.gov/29664383/)).

> *"Our results provide biochemical evidence for the occurrence of TXA2-dependent platelet activation and thrombin generation in vivo, together with endothelial dysfunction."* — [PMID: 8584998](https://pubmed.ncbi.nlm.nih.gov/8584998/)

### Finding 4 — Clinical phenotype: fever and rash near-universal; eschar frequently ABSENT

In **70 Israeli children**, fever occurred in 100%, rash 98.5%, myalgia 54%, vomiting 40%; thrombocytopenia 75%, hyponatremia 62.5%; 16% hospitalized; 1 death ([PMID: 2710586](https://pubmed.ncbi.nlm.nih.gov/2710586/)). Fatal Israeli pediatric cases showed **irreversible shock, encephalopathy, renal failure, and bleeding, with death within 24 h**, often with **no eschar and no tick-bite history** ([PMID: 8286624](https://pubmed.ncbi.nlm.nih.gov/8286624/)). A Palestinian pediatric cohort (n=18) reported fever and rash 100%, eschar rare (6%), GI 44%, neurological 28%, arthralgia/myalgia 33%, thrombocytopenia 56%, and universally good outcomes with prompt doxycycline ([PMID: 41795239](https://pubmed.ncbi.nlm.nih.gov/41795239/)).

> *"the major clinical features were fever (100%), skin rash (98.5%), myalgia (54%) and vomiting (40%). Thrombocytopenia (75%) and hyponatremia (62.5%) were common"* — [PMID: 2710586](https://pubmed.ncbi.nlm.nih.gov/2710586/)

> *"None of the patients had a history of tick bite, and no tache noire was noted. One child presented without rash"* — [PMID: 8286624](https://pubmed.ncbi.nlm.nih.gov/8286624/)

**Documented complications:** hemophagocytic lymphohistiocytosis/HLH ([PMID: 35169573](https://pubmed.ncbi.nlm.nih.gov/35169573/), [PMID: 40693676](https://pubmed.ncbi.nlm.nih.gov/40693676/)), purpura fulminans ([PMID: 29664383](https://pubmed.ncbi.nlm.nih.gov/29664383/), [PMID: 40580427](https://pubmed.ncbi.nlm.nih.gov/40580427/)), Guillain-Barré syndrome ([PMID: 41768953](https://pubmed.ncbi.nlm.nih.gov/41768953/)), and multi-organ failure in children ([PMID: 26905298](https://pubmed.ncbi.nlm.nih.gov/26905298/)).

**Suggested HPO terms:** HP:0001945 (Fever), HP:0000988 (Skin rash), HP:0003326 (Myalgia), HP:0002013 (Vomiting), HP:0001873 (Thrombocytopenia), HP:0002902 (Hyponatremia), HP:0002240 (Hepatomegaly), HP:0001298 (Encephalopathy), HP:0001919 (Acute kidney injury), HP:0031137 (Abnormal circulating coagulation protein concentration), HP:0002624 (vasculitis-related manifestations).

### Finding 5 — Epidemiology: summer, dog-associated, Mediterranean basin with expanding range

The ISF strain is documented in **Israel, Italy (Sicily, Sardinia), and Portugal** ([PMID: 28408252](https://pubmed.ncbi.nlm.nih.gov/28408252/)), and *R. conorii* subsp. *israelensis* has been detected in ticks/patients in **Iran** ([PMID: 38254000](https://pubmed.ncbi.nlm.nih.gov/38254000/), [PMID: 35365079](https://pubmed.ncbi.nlm.nih.gov/35365079/)), **Uganda** ([PMID: 37498943](https://pubmed.ncbi.nlm.nih.gov/37498943/)), **Ghana (first record)** ([PMID: 41958159](https://pubmed.ncbi.nlm.nih.gov/41958159/)), and ticks in **Israel** ([PMID: 35816829](https://pubmed.ncbi.nlm.nih.gov/35816829/)). Seasonality is **late spring/summer**, linked to *Rhipicephalus sanguineus* activity and climate variability/low precipitation ([PMID: 17114701](https://pubmed.ncbi.nlm.nih.gov/17114701/)). Dogs serve as a reservoir: **38.5% of 400 healthy Portuguese dogs were seropositive**, and the ISF strain was detected in dog blood ([PMID: 21771547](https://pubmed.ncbi.nlm.nih.gov/21771547/)).

> *"R. conorii subsp. israelensis, which belongs to the R. conorii complex, is the agent of Israeli spotted fever (ISF); apart from Israel, it has also been found in Italy (Sicily and Sardinia) and in different regions of Portugal."* — [PMID: 28408252](https://pubmed.ncbi.nlm.nih.gov/28408252/)

### Finding 6 — Molecular mechanism: Sca-family autotransporters mediate adhesion, invasion, and actin-based motility

Surface cell antigen (Sca) autotransporters—**Sca0/OmpA, Sca5/OmpB, and Sca2**—mediate host-cell adhesion, invasion, and intracellular motility. **Sca2** (~1800-aa monomeric autotransporter) is sufficient to mediate adherence and invasion of human endothelial cells and drives assembly of **long, unbranched actin tails** for intracellular movement; it is the **only known functional mimic of eukaryotic formins** ([PMID: 22612237](https://pubmed.ncbi.nlm.nih.gov/22612237/)). Cryo-EM shows Sca2 forms a formin FH2-dimer-like "doughnut" encircling two actin subunits ([PMID: 37028467](https://pubmed.ncbi.nlm.nih.gov/37028467/)).

> *"A rickettsial autotransporter from Rickettsia conorii, Sca2, has been shown to be sufficient to mediate both adherence and invasion of human endothelial cells and to participate in intracellular actin-based motility."* — [PMID: 22612237](https://pubmed.ncbi.nlm.nih.gov/22612237/)

> *"Sca2... is the only known functional mimic of eukaryotic formins"* — [PMID: 37028467](https://pubmed.ncbi.nlm.nih.gov/37028467/)

**Suggested GO terms:** GO:0007155 (cell adhesion), GO:0070358 (actin polymerization-dependent cell motility), GO:0030036 (actin cytoskeleton organization).

### Finding 7 — Mechanism of vascular leak: VE-cadherin phosphorylation, nitric oxide, and ROS drive hyperpermeability

SFG rickettsial infection of microvascular endothelial cells activates **tyrosine phosphorylation of VE-cadherin** (peak ~72 h post-infection), reducing VE-cadherin junctional interactions and increasing permeability ([PMID: 22720111](https://pubmed.ncbi.nlm.nih.gov/22720111/)). Increased permeability is partly due to intracellular rickettsiae and partly to host pro-inflammatory defenses, with dissociation of endothelial adherens junctions ([PMID: 17957455](https://pubmed.ncbi.nlm.nih.gov/17957455/)); **nitric oxide** from infected ECs both limits rickettsial proliferation and alters barrier integrity ([PMID: 16481520](https://pubmed.ncbi.nlm.nih.gov/16481520/)). The full pathogenetic sequence—dermal entry → hematogenous spread to endothelium (esp. brain and lungs) → increased permeability, edema, and immunity via NK cells, IFN-γ, TNF-α, RANTES, antibodies, and CTLs—is defined in the SFG rickettsioses ([PMID: 12860594](https://pubmed.ncbi.nlm.nih.gov/12860594/)).

> *"infection of R. montanensis significantly activated tyrosine phosphorylation of VE-cadherin beginning at 48 hr and reaching a peak at 72 hr p.i."* — [PMID: 22720111](https://pubmed.ncbi.nlm.nih.gov/22720111/)

> *"The pathogenetic sequence includes rickettsial entry into the dermis, hematogenous dissemination to vascular endothelial cells (most critically in brain and lungs), increased vascular permeability, edema, and immunity mediated by NK cells, IFN-gamma, TNF-alpha, RANTES, antibodies, and cytotoxic T lymphocytes."* — [PMID: 12860594](https://pubmed.ncbi.nlm.nih.gov/12860594/)

### Finding 8 — Anatomical structures affected: vascular endothelium is the primary target; skin, brain, lung, kidney, liver, GI tract involved

The **microvascular/vascular endothelial cell** is the primary target; disseminated endothelial infection produces increased permeability and edema most critically in **brain and lungs** ([PMID: 12860594](https://pubmed.ncbi.nlm.nih.gov/12860594/), [PMID: 22720111](https://pubmed.ncbi.nlm.nih.gov/22720111/)). Documented organ involvement in ISF/MSF spans skin (rash, eschar, edema), CNS (encephalopathy, meningoencephalitis, Guillain-Barré), lungs (tachypnea, non-cardiogenic pulmonary edema), kidney (azotemia, acute tubular necrosis), liver (hepatomegaly, transaminitis, hyperbilirubinemia), GI tract, spleen, and the hematologic system (thrombocytopenia, coagulopathy, DIC, purpura fulminans) ([PMID: 18582199](https://pubmed.ncbi.nlm.nih.gov/18582199/), [PMID: 8286624](https://pubmed.ncbi.nlm.nih.gov/8286624/), [PMID: 29664383](https://pubmed.ncbi.nlm.nih.gov/29664383/)).

> *"hematogenous dissemination to vascular endothelial cells (most critically in brain and lungs), increased vascular permeability, edema"* — [PMID: 12860594](https://pubmed.ncbi.nlm.nih.gov/12860594/)

**Suggested UBERON/CL/GO terms:** UBERON:0001981 (blood vessel), UBERON:0001986 (endothelium), CL:0000115 (endothelial cell), CL:0002139 (endothelial cell of vascular tree); UBERON:0002097 (skin), UBERON:0000955 (brain), UBERON:0002048 (lung), UBERON:0002113 (kidney), UBERON:0002107 (liver); GO:0005912 (adherens junction), GO:0005923 (bicellular tight junction), GO:0005911 (cell-cell junction).

### Finding 9 — Prevention is non-pharmacologic: no vaccine; tick-bite avoidance and vector control

No licensed human vaccine exists for *R. conorii*/SFG rickettsiae; prevention depends on **avoiding tick bites and controlling the brown dog tick**. Integrated vector control (surveillance, residual acaricide spraying, dog tick collars, public outreach) substantially reduced *Rhipicephalus sanguineus* populations and rickettsial risk in a California program ([PMID: 41146265](https://pubmed.ncbi.nlm.nih.gov/41146265/)). Effective canine ectoparasiticides include **isoxazolines (e.g., lotilaner)** and combination endectocides ([PMID: 42045933](https://pubmed.ncbi.nlm.nih.gov/42045933/)); pyrethroid acaricides target the tick voltage-gated sodium channel but **resistance is emerging** ([PMID: 41272771](https://pubmed.ncbi.nlm.nih.gov/41272771/)). Early empiric doxycycline is the key **secondary-prevention** measure against fatal outcomes.

> *"the integrated intervention substantially reduced tick populations at the affected site. Both adult and immature stages of Rh. sanguineus s.l. declined following sequential treatments."* — [PMID: 41146265](https://pubmed.ncbi.nlm.nih.gov/41146265/)

### Finding 10 — ISF is a zoonosis: dogs are reservoir/sentinel hosts

*R. conorii* subsp. *israelensis* DNA has been detected in *Rhipicephalus sanguineus* dog ticks in **Ghana** (first record; 3.95% of pools; [PMID: 41958159](https://pubmed.ncbi.nlm.nih.gov/41958159/)), **Uganda** ([PMID: 37498943](https://pubmed.ncbi.nlm.nih.gov/37498943/)), and **Israel** ([PMID: 35816829](https://pubmed.ncbi.nlm.nih.gov/35816829/)); the ISF strain was detected in Portuguese dog blood with 38.5% seropositivity ([PMID: 21771547](https://pubmed.ncbi.nlm.nih.gov/21771547/)). The tick maintains the agent transovarially/transstadially, and the ISF strain is better tolerated by the tick than Malish ([PMID: 19421877](https://pubmed.ncbi.nlm.nih.gov/19421877/)). Naturally infected species include domestic dogs (*Canis lupus familiaris*, **NCBI Taxon 9615**) and the tick vector (*Rhipicephalus sanguineus*, **NCBI Taxon 34632**).

> *"This study reports the first molecular detection of R. conorii subsp. israelensis in Ghana."* — [PMID: 41958159](https://pubmed.ncbi.nlm.nih.gov/41958159/)

### Finding 11 — Treatment: doxycycline is drug of choice; josamycin/clarithromycin are alternatives

A randomized trial of **1-day doxycycline vs 5-day josamycin in 59 MSF patients** showed all recovered uneventfully with no significant difference; single-day doxycycline is effective, easy, and inexpensive ([PMID: 2193627](https://pubmed.ncbi.nlm.nih.gov/2193627/)). An RCT of **clarithromycin vs doxycycline/josamycin (n=40, incl. 13 children <14 y)** found no significant difference in time to defervescence (2.67 vs 2.22 d) or symptom resolution, with no adverse reactions or relapses ([PMID: 26711765](https://pubmed.ncbi.nlm.nih.gov/26711765/)). Josamycin is favored first-choice in **children and pregnant women** ([PMID: 1884779](https://pubmed.ncbi.nlm.nih.gov/1884779/)). Chloramphenicol is effective but carries bone-marrow toxicity, so tetracyclines are preferred.

> *"One-day doxycycline therapy is an effective, easy, and inexpensive treatment. Josamycin is a useful therapeutic alternative that may be particularly convenient for pregnant women and patients with a history of allergy to tetracyclines."* — [PMID: 2193627](https://pubmed.ncbi.nlm.nih.gov/2193627/)

> *"clarithromycin is a good alternative to doxycycline or josamycin in the treatment of MSF."* — [PMID: 26711765](https://pubmed.ncbi.nlm.nih.gov/26711765/)

**Suggested NCIT/CHEBI terms:** NCIT:C692 (Doxycycline), NCIT:C1032 (Clarithromycin), NCIT:C376 (Chloramphenicol); CHEBI:50845 (doxycycline), CHEBI:3732 (clarithromycin).

### Finding 12 — Temporal course & prognosis: acute, self-limited after ~6-day incubation; excellent with early treatment

Onset is **acute after a short (~5–7 day) incubation**; severe ISF can progress to neurologic and multi-organ failure within days, with recovery achievable if appropriate antibiotics start early ([PMID: 14964019](https://pubmed.ncbi.nlm.nih.gov/14964019/)). Fatal pediatric ISF progressed to shock, encephalopathy, and renal failure with death within 24 h of admission ([PMID: 8286624](https://pubmed.ncbi.nlm.nih.gov/8286624/)). In the strain-identified Portuguese cohort, **29/140 (21%) adults died**, fatality significantly higher for ISF ([PMID: 18582199](https://pubmed.ncbi.nlm.nih.gov/18582199/)). **Prognostic factors for death:** ISF strain, older age, alcoholism, delayed treatment, G6PD deficiency, petechial/purpuric rash, obtundation, coagulopathy, azotemia, hepatic dysfunction.

> *"Clinical disease was characterized by irreversible shock, encephalopathy, renal failure, bleeding tendency, and death within 24 hours of admission."* — [PMID: 8286624](https://pubmed.ncbi.nlm.nih.gov/8286624/)

### Finding 13 — Diagnosis: IFA serology (gold standard) plus PCR/sequencing of skin biopsy targeting gltA/ompA

In 128 confirmed MSF patients, **IFA** showed seroconversion or ≥4-fold titre rise in 97 (77%) and a single high titre in 16 (12.7%); **skin-biopsy PCR** was positive in 77/106 (72.6%), with similar yield from eschar (73%) and maculopapular rash (70%) specimens ([PMID: 23168048](https://pubmed.ncbi.nlm.nih.gov/23168048/)). Real-time PCR of skin biopsy plus **DNA sequencing of *gltA* and *ompA*** enables species/subspecies identification ([PMID: 40608626](https://pubmed.ncbi.nlm.nih.gov/40608626/)), and ISF has been specifically confirmed by real-time PCR + IFA in case reports ([PMID: 38254000](https://pubmed.ncbi.nlm.nih.gov/38254000/)).

> *"Using IFA, seroconversion or a fourfold or greater rise in titre was observed in 97 (77%) patients, whereas a single high titre was demonstrated in 16 (12.7%) patients. According to PCR analysis, 77 (72.6%) of 106 biopsy samples showed positive results."* — [PMID: 23168048](https://pubmed.ncbi.nlm.nih.gov/23168048/)

**Common laboratory abnormalities (LOINC-relevant):** thrombocytopenia, hyponatremia, elevated transaminases, hyperbilirubinemia, elevated CRP, azotemia, elevated creatine kinase. **Differential diagnosis:** other SFG rickettsioses (African tick-bite fever — more numerous eschars, [PMID: 41244315](https://pubmed.ncbi.nlm.nih.gov/41244315/)), meningococcemia, leptospirosis, viral exanthems, and other causes of fever + rash. There is **no genetic testing, newborn screening, or omics-based diagnostic** relevant to this infectious disease.

### Finding 14 — Animal models: susceptible C3H/HeN(J) vs resistant C57BL/6 mice; immunity via NK cells, IFN-γ, CD4 Th1

**C3H/HeN and C3H/HeJ mice** are susceptible and develop lethal disseminated infection with endothelial targeting; **C57BL/6 mice are resistant** ([PMID: 17403875](https://pubmed.ncbi.nlm.nih.gov/17403875/)). NK-cell depletion enhances susceptibility, and early control is **IFN-γ/IL-12 dependent** ([PMID: 11504408](https://pubmed.ncbi.nlm.nih.gov/11504408/)). Susceptible C3H mice show delayed CD4+ Th1/Th2 responses and higher Foxp3+ Tregs. The ISF (ISTT) strain differs from Malish in tick biology: it caused less tick mortality and higher tick infection prevalence (35–66% vs <5%) in *Rhipicephalus sanguineus* ([PMID: 19421877](https://pubmed.ncbi.nlm.nih.gov/19421877/)). Tick saliva modulates host inflammation (IL-1β, NF-κB) during transmission ([PMID: 26011701](https://pubmed.ncbi.nlm.nih.gov/26011701/)).

> *"depletion of NK cell activity with antibody to asialo GM1 enhanced the susceptibility of C3H/HeN mice to infection with R. conorii"* — [PMID: 11504408](https://pubmed.ncbi.nlm.nih.gov/11504408/)

> *"exposure to ISTT strain had lesser effect on tick survival and resulted in 35-66% prevalence of infection"* — [PMID: 19421877](https://pubmed.ncbi.nlm.nih.gov/19421877/)

**Model organisms:** *Mus musculus* (NCBI Taxon 10090) — inbred C3H/HeN, C3H/HeJ (susceptible), C57BL/6 (resistant); primary human microvascular/umbilical vein endothelial cells for in vitro work. **Recapitulation:** disseminated endothelial infection, vasculitis, and lethal multi-organ disease are well reproduced in susceptible mice; **limitations** include that eschar/tache noire formation and the human tick-bite transmission route are incompletely modeled without live tick infestation.

### Finding 15 — Israeli national epidemiology: predominant SFG rickettsiosis, ~30% case-fatality, coastal clustering

A nationwide Israeli study (2010–2019) identified **42 hospitalized SFG rickettsiosis cases (36 autochthonous)**; the *R. conorii* Israeli tick typhus strain was most prevalent (**33/42, 79%**), required intensive care in 52%, and had a **30% fatality rate**. History of tick bite was present in only **5%**; eschar in **12%**; leukocytosis more common than leukopenia; **72% resided along the Mediterranean shoreline** ([PMID: 34286684](https://pubmed.ncbi.nlm.nih.gov/34286684/)). A seroepidemiologic survey of two Israeli villages found **69/85 (81%) dogs vs 14/136 (10%) humans** anti-*R. conorii* seropositive, establishing canine serology as a sensitive sentinel for human exposure ([PMID: 17620644](https://pubmed.ncbi.nlm.nih.gov/17620644/)). ISF in Sicily can be traced back to 1987–1991, with 3/5 patients severe and 1 death ([PMID: 16333093](https://pubmed.ncbi.nlm.nih.gov/16333093/)).

> *"The most prevalent species was the Rickettsia conorii Israeli tick typhus strain (n = 33, 79%); infection with this species necessitated intensive care for 52% of patients and was associated with a 30% fatality rate. A history of tick bite was rare, found for only 5% of patients; eschar was found in 12%"* — [PMID: 34286684](https://pubmed.ncbi.nlm.nih.gov/34286684/)

> *"Sixty-nine of 85 (81%) canine sera and 14 of 136 (10%) of human sera had anti-R. conorii antibodies."* — [PMID: 17620644](https://pubmed.ncbi.nlm.nih.gov/17620644/)

### Finding 16 — Genetic/molecular etiology: an infectious, not Mendelian, disease

ISF is an **infectious**, not a Mendelian genetic, disease; there are **no human causal genes, pathogenic variants, inheritance patterns, penetrance/expressivity considerations, founder effects, carrier frequencies, or chromosomal abnormalities** to report. Host genetic modifiers of severity are plausible but under-characterized: **G6PD deficiency** is repeatedly cited as a risk factor for severe/fatal MSF, consistent with the oxidative-injury mechanism and the selective modulation of G6PD observed in infected tissues ([PMID: 15120155](https://pubmed.ncbi.nlm.nih.gov/15120155/)). In animal models, host background (C3H vs C57BL/6) strongly determines susceptibility, implying host genetic control of outcome ([PMID: 17403875](https://pubmed.ncbi.nlm.nih.gov/17403875/)). The relevant "genome" for causal variants is that of the **pathogen** (*sca0/ompA, sca5/ompB, sca2, sca4, gltA, 16S rRNA*), which defines strain identity and virulence.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

```
1.  Infected Rhipicephalus sanguineus tick bite inoculates R. conorii subsp. israelensis
    into the dermis  ──leads to──▶
2.  Sca0/OmpA + Sca5/OmpB mediate adhesion to vascular endothelial cells  ──results in──▶
3.  Receptor-mediated invasion of endothelial cells (Sca2 sufficient for entry)  ──leads to──▶
4.  Intracellular replication + Sca2 formin-mimic actin-based motility  ──drives──▶
5.  Cell-to-cell spread and hematogenous dissemination to systemic microvasculature
        (brain and lungs most critical)  ──results in──▶
6.  Endothelial injury:
        ├── VE-cadherin tyrosine phosphorylation → adherens-junction dissociation
        ├── Nitric oxide + reactive oxygen species (ROS) → peroxidative membrane damage
        └── Pro-inflammatory host response (NK cells, IFN-γ, TNF-α, RANTES, CTLs)
                                                          ──all converge on──▶
7.  Increased microvascular permeability → interstitial edema (cerebral, pulmonary)
        + small-vessel vasculitis  ──in parallel with──▶
8.  Platelet activation (TXA2) + thrombin generation → procoagulant state, microthrombi
                                                          ──branches──▶
        ├── Usual course: self-limited vasculitis → fever + maculopapular rash
        │        → RESOLUTION with early doxycycline
        └── Severe/ISF-strain course: DIC, purpura fulminans, HLH, shock,
                 encephalopathy, renal failure, multi-organ failure → DEATH (20–30%)
```

Steps 1–5 and the endothelial tropism (step 6) are **experimentally demonstrated** (in vitro human ECs, mouse models, patient biopsies). The relative contribution of intrinsic rickettsial cytotoxicity vs host immunopathology to permeability (step 7) is **partly inferred**; both are supported ([PMID: 17957455](https://pubmed.ncbi.nlm.nih.gov/17957455/)). Why the ISF strain is more virulent than Malish at the molecular level is **not yet mechanistically resolved**—it is an empirical epidemiologic/clinical observation ([PMID: 18582199](https://pubmed.ncbi.nlm.nih.gov/18582199/), [PMID: 34286684](https://pubmed.ncbi.nlm.nih.gov/34286684/)).

### Upstream vs downstream summary

| Level | Mechanism | Evidence source | GO/CL suggestion |
|---|---|---|---|
| Upstream (trigger) | Tick inoculation; Sca-mediated adhesion/invasion | In vitro, cryo-EM ([PMID: 22612237](https://pubmed.ncbi.nlm.nih.gov/22612237/), [PMID: 37028467](https://pubmed.ncbi.nlm.nih.gov/37028467/)) | GO:0007155 cell adhesion; CL:0000115 endothelial cell |
| Middle | Actin-based motility; hematogenous spread | In vitro, mouse ([PMID: 15120155](https://pubmed.ncbi.nlm.nih.gov/15120155/)) | GO:0070358 actin polymerization-based movement |
| Downstream (effector) | VE-cadherin phosphorylation, NO/ROS, permeability | In vitro human ECs ([PMID: 22720111](https://pubmed.ncbi.nlm.nih.gov/22720111/), [PMID: 16481520](https://pubmed.ncbi.nlm.nih.gov/16481520/)) | GO:0005923 tight junction; GO:0034220 ion transmembrane transport |
| Terminal (clinical) | Vasculitis, edema, DIC, multi-organ failure | Patient cohorts ([PMID: 18582199](https://pubmed.ncbi.nlm.nih.gov/18582199/), [PMID: 34286684](https://pubmed.ncbi.nlm.nih.gov/34286684/)) | HP:0002624 vasculitis; HP:0001928 coagulopathy |

### Strain comparison table

| Feature | Malish (*R. conorii* subsp. *conorii*) | ISF (*R. conorii* subsp. *israelensis*) |
|---|---|---|
| MLST genotype | Malish type | ISFR type ([PMID: 15766388](https://pubmed.ncbi.nlm.nih.gov/15766388/)) |
| Eschar (tache noire) | ~49% (Portugal) | ~39% (Portugal); ~5–12% (Israel) ([PMID: 16481514](https://pubmed.ncbi.nlm.nih.gov/16481514/), [PMID: 34286684](https://pubmed.ncbi.nlm.nih.gov/34286684/)) |
| Virulence / fatality | Lower | Higher; fatal outcome significantly more likely ([PMID: 18582199](https://pubmed.ncbi.nlm.nih.gov/18582199/)) |
| Tick infection prevalence | <5% | 35–66%; better tolerated by tick ([PMID: 19421877](https://pubmed.ncbi.nlm.nih.gov/19421877/)) |

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [15766388](https://pubmed.ncbi.nlm.nih.gov/15766388/) | MLST subspecies of *R. conorii* | Defines ISF as subsp. *israelensis*; taxonomy backbone |
| [18582199](https://pubmed.ncbi.nlm.nih.gov/18582199/) | Fatal *R. conorii* risk factors (Portugal) | Core evidence: ISF strain virulence, 21% fatality, alcoholism |
| [34286684](https://pubmed.ncbi.nlm.nih.gov/34286684/) | SFG rickettsioses in Israel 2010–2019 | National epidemiology; 79% ISF, 30% fatality, coastal clustering |
| [12860594](https://pubmed.ncbi.nlm.nih.gov/12860594/) | Pathogenic mechanisms of *Rickettsia* | Full pathogenetic causal chain and immune mediators |
| [22720111](https://pubmed.ncbi.nlm.nih.gov/22720111/) | Rickettsiae + VE-cadherin (AFM) | Molecular basis of endothelial hyperpermeability |
| [22612237](https://pubmed.ncbi.nlm.nih.gov/22612237/) | Sca2 domains | Sca2 adhesion/invasion/motility |
| [37028467](https://pubmed.ncbi.nlm.nih.gov/37028467/) | Cryo-EM of Sca2 | Formin-like core structure |
| [8584998](https://pubmed.ncbi.nlm.nih.gov/8584998/) | Coagulation/platelet activation in MSF | In vivo procoagulant state, endothelial dysfunction |
| [2710586](https://pubmed.ncbi.nlm.nih.gov/2710586/) | Spotted fever in Israeli children | Symptom/lab frequencies |
| [8286624](https://pubmed.ncbi.nlm.nih.gov/8286624/) | Fatal ISF in children | Absence of eschar/tick history; rapidly fatal course |
| [41795239](https://pubmed.ncbi.nlm.nih.gov/41795239/) | Palestinian pediatric cohort | Modern pediatric phenotype; benign with early Rx |
| [23168048](https://pubmed.ncbi.nlm.nih.gov/23168048/) | MSF in Turkey | Diagnostic yield of IFA + biopsy PCR |
| [40608626](https://pubmed.ncbi.nlm.nih.gov/40608626/) | Rickettsiosis case series | gltA/ompA sequencing for species ID |
| [2193627](https://pubmed.ncbi.nlm.nih.gov/2193627/) | RCT doxycycline vs josamycin | First-line therapy evidence |
| [26711765](https://pubmed.ncbi.nlm.nih.gov/26711765/) | RCT clarithromycin | Macrolide alternative for children |
| [21771547](https://pubmed.ncbi.nlm.nih.gov/21771547/) | *R. conorii* in Portuguese dogs | Reservoir/sentinel role of dogs |
| [17620644](https://pubmed.ncbi.nlm.nih.gov/17620644/) | Seroepidemiology, Israeli villages | Dogs 81% vs humans 10% seropositive |
| [19421877](https://pubmed.ncbi.nlm.nih.gov/19421877/) | ISTT vs Malish in ticks | Strain difference in vector biology |
| [17403875](https://pubmed.ncbi.nlm.nih.gov/17403875/) | Dendritic cells & susceptibility | C3H susceptible vs C57BL/6 resistant model |
| [11504408](https://pubmed.ncbi.nlm.nih.gov/11504408/) | NK/IFN-γ early immunity | Protective immune mechanism |
| [28408252](https://pubmed.ncbi.nlm.nih.gov/28408252/) | ISF in Sicily | Geographic distribution; disease identity |
| [16481514](https://pubmed.ncbi.nlm.nih.gov/16481514/) | Eschar in ISF patients | Nuance: no statistical eschar/severity difference in one cohort |
| [41146265](https://pubmed.ncbi.nlm.nih.gov/41146265/) | Integrated vector control (California) | Prevention via *Rh. sanguineus* control |
| [41958159](https://pubmed.ncbi.nlm.nih.gov/41958159/) | ISF agent in Ghana ticks | Expanding geographic range; zoonotic cycle |

**Challenging / nuancing evidence:** [PMID: 16481514](https://pubmed.ncbi.nlm.nih.gov/16481514/) found no *statistically significant* difference in eschar frequency or fatality between Malish and ISF in a 94-patient Portuguese cohort, tempering the "greater severity" narrative that is otherwise strongly supported by the larger prospective cohort ([PMID: 18582199](https://pubmed.ncbi.nlm.nih.gov/18582199/)) and Israeli national data ([PMID: 34286684](https://pubmed.ncbi.nlm.nih.gov/34286684/)). The most likely reconciliation is that strain virulence interacts with host factors (age, alcoholism, G6PD status) and treatment timing, so cohort composition strongly influences the observed effect size.

---

## Limitations and Knowledge Gaps

1. **Molecular basis of ISF hypervirulence is unresolved.** Why *R. conorii* subsp. *israelensis* causes higher fatality than Malish is documented epidemiologically but not explained at the genomic/proteomic level. No comparative virulence-factor study isolating the responsible loci was identified.
2. **No dedicated ISF pathophysiology datasets.** Most mechanistic findings derive from related SFG rickettsiae (*R. rickettsii, R. montanensis*) and MSF broadly, not ISF-specific experiments. Extrapolation is reasonable but formally an inference.
3. **Human host-genetic modifiers are under-characterized.** G6PD deficiency is repeatedly cited but lacks a large, controlled association study for ISF specifically.
4. **Epidemiology is likely under-ascertained.** Rare tick-bite history and frequent absence of eschar cause diagnostic delay and underdiagnosis; true incidence/prevalence figures (cases per 100,000) are not well established outside hospitalized cohorts.
5. **No quality-of-life instruments (EQ-5D, SF-36) have been applied** to ISF survivors; long-term sequelae (e.g., post-GBS, post-HLH) are described only in case reports.
6. **Publication/selection bias toward severe cases.** Case reports over-represent complications (purpura fulminans, HLH), while population data ([PMID: 41795239](https://pubmed.ncbi.nlm.nih.gov/41795239/)) suggest most pediatric disease is benign when treated early.
7. **No omics (transcriptomics/proteomics/metabolomics) profiling specific to ISF** was found; molecular-profiling sections are supported only by model-organism antioxidant-enzyme and lncRNA studies.

---

## Proposed Follow-up Experiments / Actions

1. **Comparative genomics/transcriptomics of ISF vs Malish strains** in matched human microvascular endothelial cell infections to pinpoint virulence determinants (candidate loci: *sca* family, *rickA*, toxin-antitoxin modules). Read out permeability (TEER), VE-cadherin phosphorylation, and cytokine induction.
2. **Case-control study of G6PD deficiency and other host modifiers** (HLA, cytokine polymorphisms) in strain-confirmed ISF cohorts to quantify the contribution of host genetics to fatality.
3. **Prospective natural-history and QoL study** (EQ-5D/PROMIS) of ISF survivors, including neurological and hematologic sequelae, to fill the outcomes/prognosis gap.
4. **Enhanced One-Health surveillance** integrating canine serology (a sensitive sentinel; [PMID: 17620644](https://pubmed.ncbi.nlm.nih.gov/17620644/)) and tick molecular screening across the expanding geographic range (Iran, sub-Saharan Africa) to define true incidence and detect range expansion driven by *Rhipicephalus sanguineus* spread and climate change.
5. **Evaluate acaricide-resistance management** for *Rh. sanguineus* (isoxazoline rotation) given emerging VGSC pyrethroid-resistance mutations ([PMID: 41272771](https://pubmed.ncbi.nlm.nih.gov/41272771/)), and model integrated vector-control programs for ISF-endemic coastal communities.
6. **Clinician decision-support/awareness intervention**: because tick bite and eschar are frequently absent, promote empiric doxycycline for summer fever+rash in endemic/coastal areas to shorten the treatment delay that drives mortality.

---

## Consensus Answer

Israeli Tick Typhus (Israeli spotted fever; MONDO:0000230) is a tick-borne spotted-fever-group rickettsiosis caused by the obligate intracellular bacterium *Rickettsia conorii* subsp. *israelensis*, transmitted by the brown dog tick *Rhipicephalus sanguineus* with dogs as the amplifying reservoir. It infects vascular endothelial cells to produce a disseminated small-vessel vasculitis presenting as fever and maculopapular rash (with the tache noire/eschar frequently absent), and the more virulent ISF strain can progress to severe multi-organ disease with case-fatality reaching ~20–30% in hospitalized/severe cases. Prompt empiric doxycycline is the first-line treatment and is highly effective when started early.


## Artifacts

- [OpenScientist final report](Israeli_Tick_Typhus-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Israeli_Tick_Typhus-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 45 |
| Resolved | 45 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 45 |
| On topic | 24 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 31 |
| Terms named correctly | 25 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0031137` (1 mention) - the report calls it "Abnormal circulating coagulation protein concentration"; HP calls it **Storage in hepatocytes**
- `HP:0002624` (2 mentions) - the report calls it "vasculitis-related manifestations"; HP calls it **Abnormal venous morphology**
- `NCIT:C692` (1 mention) - the report calls it "Doxycycline"; NCIT calls it **Nimodipine**
- `NCIT:C376` (1 mention) - the report calls it "Chloramphenicol"; NCIT calls it **Cisplatin**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0002097` (1 mention) - the report calls it "skin"; UBERON calls it **skin of body**, and lists "skin" among its other names
- `NCIT:C1032` (1 mention) - the report calls it "Clarithromycin"; NCIT calls it **Cactinomycin**