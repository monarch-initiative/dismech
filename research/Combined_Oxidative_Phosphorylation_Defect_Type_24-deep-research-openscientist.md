---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-17T16:19:36.914717'
end_time: '2026-09-17T16:58:50.387481'
duration_seconds: 2353.47
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Combined Oxidative Phosphorylation Defect Type 24
  mondo_id: MONDO:0014547
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
citation_count: 11
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 12
  validator_version: 0.2.1
term_validation:
  total_terms: 35
  verified: 33
  not_found: 1
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.029
  labels_checked: 4
  labels_matching: 0
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0000407
    reported_labels:
    - Cardinal feature; isolated (DFNB94) or with CNS disease
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0002415
    reported_labels:
    - Severe subgroup
    ontology_label: Leukodystrophy
  - term_id: HP:0003128
    reported_labels:
    - Supports diagnosis
    ontology_label: Lactic acidosis
  - term_id: HP:0001518
    reported_labels:
    - 7/8 in diabetes cohort
    ontology_label: Small for gestational age
  unresolved_terms:
  - HP:0007303
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Combined_Oxidative_Phosphorylation_Defect_Type_24-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Combined_Oxidative_Phosphorylation_Defect_Type_24-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Oxidative Phosphorylation Defect Type 24
- **MONDO ID:** MONDO:0014547 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Oxidative Phosphorylation Defect Type 24** covering all of the
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

# Combined Oxidative Phosphorylation Deficiency 24 (COXPD24 / NARS2-Related Disease): A Comprehensive Disease Characterization

**Disease:** Combined Oxidative Phosphorylation Defect Type 24
**MONDO:** MONDO:0014547 · **OMIM:** #616239 · **Gene:** *NARS2* (OMIM *612803; HGNC:24406) · **Category:** Mendelian, autosomal recessive

---

## Summary

Combined Oxidative Phosphorylation Deficiency 24 (COXPD24) is an ultra-rare, autosomal-recessive, multisystem mitochondrial disorder caused by biallelic pathogenic variants in **NARS2**, the nuclear gene encoding the **mitochondrial asparaginyl-tRNA synthetase** (mt-AsnRS). NARS2 charges mitochondrial tRNA-Asn with asparagine, an obligatory step in the intramitochondrial translation of the 13 OXPHOS subunits encoded by mtDNA. When NARS2 function is lost, charged mt-tRNA-Asn falls, mitochondrial protein synthesis fails, and the cell manifests a **combined oxidative phosphorylation deficiency—predominantly of complex I and complex IV**—which is the defining biochemical hallmark of the disease ([PMID: 25385316](https://pubmed.ncbi.nlm.nih.gov/25385316/); [PMID: 25807530](https://pubmed.ncbi.nlm.nih.gov/25807530/)).

Clinically, COXPD24/NARS2 disease is strikingly **phenotypically variable and genotype-graded**, spanning a continuous spectrum from isolated nonsyndromic sensorineural hearing loss (DFNB94) at the mild end to severe, early-onset Leigh and Alpers-type encephalopathy with refractory epilepsy, developmental delay/intellectual disability, myopathy, spastic paraplegia, and ataxia at the severe end. **Sensorineural hearing loss is a cardinal feature**, and **neonatal/infantile insulin-dependent diabetes** has recently been recognized as an important part of the phenotype, reflecting a critical role for NARS2 in pancreatic β-cells ([PMID: 33596490](https://pubmed.ncbi.nlm.nih.gov/33596490/); [PMID: 40887432](https://pubmed.ncbi.nlm.nih.gov/40887432/)). Onset is typically neonatal to early childhood; severe encephalopathic forms carry high early mortality, whereas isolated deafness is compatible with long survival.

Diagnosis rests on **molecular genetics (whole-exome/whole-genome sequencing)**, supported by elevated blood/CSF lactate, characteristic MRI (symmetric Leigh-type basal ganglia/thalamus/brainstem lesions, or progressive cerebral atrophy and delayed myelination), and muscle-biopsy demonstration of combined complex I + IV deficiency. **No disease-modifying therapy exists**; management is supportive (antiepileptic drugs, hearing rehabilitation, developmental therapies, nutritional support, insulin for the diabetic subgroup), and prevention is limited to genetic counseling with carrier, prenatal, and preimplantation genetic testing. Substrate (L-asparagine) supplementation is a rational but unproven experimental strategy, and class-level trials of amino-acid supplementation in related mitochondrial aminoacyl-tRNA synthetase disorders have not met efficacy endpoints.

---

## Key Findings

### Finding 1 — COXPD24 is caused by biallelic (autosomal-recessive) *NARS2* variants

COXPD24 (OMIM #616239) maps to **NARS2** (OMIM *612803; HGNC:24406) on **chromosome 11q14.1**, which encodes the mitochondrial asparaginyl-tRNA synthetase. The gene-disease relationship is supported by multiple independent consanguineous and compound-heterozygous families. Vanlander et al. (2015) reported two siblings with a homozygous **c.822G>C** splice-site variant producing exon-7 skipping and a combined complex I + IV deficiency in skeletal muscle: *"The reported variant in NARS2 results in a combined OXPHOS complex deficiency involving complex I and IV, making NARS2 a new member of disease-associated aaRS2"* ([PMID: 25385316](https://pubmed.ncbi.nlm.nih.gov/25385316/)). In the same year, Simon et al. established the broader allelic spectrum—**homozygous p.Val213Phe** causing nonsyndromic deafness (DFNB94), and **compound heterozygous p.Tyr323\*/p.Asn381Ser** causing Leigh syndrome: *"Here we demonstrate association of variants in the mitochondrial asparaginyl-tRNA synthetase NARS2 with human hearing loss and Leigh syndrome"* ([PMID: 25807530](https://pubmed.ncbi.nlm.nih.gov/25807530/)). Biallelic inheritance is confirmed across subsequent case series.

### Finding 2 — Mechanism: reduced charged mt-tRNA-Asn impairs mitochondrial translation, and the defect is complementable

The molecular lesion is a reduction in **aminoacylated (charged) mitochondrial tRNA-Asn**. In EBV-transformed lymphoblasts from affected siblings, *"a specific decrease in the amount of charged mt-tRNA(Asn) was demonstrated as compared with controls"* ([PMID: 25385316](https://pubmed.ncbi.nlm.nih.gov/25385316/)). Downstream, patient Leigh-syndrome fibroblasts show decreased steady-state mt-tRNA-Asn, reduced oxygen consumption rate (OCR), and reduced electron transport chain (ETC) activity. Crucially, these deficits are rescued by wild-type NARS2 but not by the mutant protein: *"we show that a decrease in oxygen consumption rates (OCR) and electron transport chain (ETC) activity can be rescued by overexpression of wild type NARS2"* ([PMID: 25807530](https://pubmed.ncbi.nlm.nih.gov/25807530/)). Structural mechanisms differ by variant: p.Asn381Ser disrupts NARS2 homodimerization and lowers protein levels, while the truncating p.Tyr323\* yields undetectable protein. BN-PAGE in-gel activity confirms decreased complex I and IV activity plus complex V subcomplexes. This complementation experiment provides direct causal proof that the respiratory-chain defect is a consequence of NARS2 loss of function.

### Finding 3 — A phenotypically variable multisystem disorder; hearing loss is cardinal, neonatal diabetes newly recognized

Sofou et al. (2021) systematically reviewed ~19 patients and concluded that *"sensorineural hearing impairment is a cardinal feature of early-onset NARS2 associated disease, either isolated or in combination with central nervous system disease"* ([PMID: 33596490](https://pubmed.ncbi.nlm.nih.gov/33596490/)). Reported phenotypes span nonsyndromic sensorineural hearing loss (DFNB94), Leigh syndrome, Alpers syndrome, infantile-onset refractory epilepsy/epileptic encephalopathy, epilepsia partialis continua, developmental delay/intellectual disability, myopathy, spastic paraplegia, and ataxia. In 2025, Donis et al. expanded the phenotype: among 397 early-onset diabetes patients, 8 carried homozygous NARS2 missense variants [p.(Phe216Leu) ×4, p.(Thr180Asn) ×3, p.(Val440Leu) ×1]; all had insulin-dependent (neonatal) diabetes diagnosed before 6 months (median 4 weeks), 7/8 had low birthweight, 7/8 had epilepsy, and 6/8 had developmental delay. The authors concluded *"NDM is an important feature of COXPD-24 and highlights a critical role for NARS2 in the insulin-secreting pancreatic β-cell"* ([PMID: 40887432](https://pubmed.ncbi.nlm.nih.gov/40887432/)).

### Finding 4 — Genetics: LoF-tolerant nuclear gene; ultra-rare AR disease with genotype–phenotype correlation

gnomAD constraint metrics for NARS2 (ENSG00000137513) show **pLI ≈ 0** and **observed/expected LoF (oe_lof) = 0.95** (90% CI 0.77–1.18), indicating heterozygous loss-of-function is tolerated—exactly as expected for a recessive disease gene where carriers are unaffected. Disease alleles are overwhelmingly biallelic missense or splice variants, frequently homozygous in consanguineous families: p.Pro214Leu (recurrent Scandinavian; [PMID: 33596490](https://pubmed.ncbi.nlm.nih.gov/33596490/)), p.Ile182Lys (Iranian; [PMID: 34374940](https://pubmed.ncbi.nlm.nih.gov/34374940/)), p.His167Arg (Turkish; [PMID: 36661119](https://pubmed.ncbi.nlm.nih.gov/36661119/)), c.822G>C splice ([PMID: 25385316](https://pubmed.ncbi.nlm.nih.gov/25385316/)), and p.Val213Phe (DFNB94; [PMID: 25807530](https://pubmed.ncbi.nlm.nih.gov/25807530/)). Severity cosegregates with the biochemical/structural impact of the variant: *"The severity of the genetic lesions and their effects on NARS2 protein structure cosegregate with the phenotype"* ([PMID: 25807530](https://pubmed.ncbi.nlm.nih.gov/25807530/)).

### Finding 5 — Treatment is supportive; substrate supplementation is experimental and unproven

No disease-modifying therapy or approved drug exists. Management is symptomatic: antiepileptic drugs for seizures, hearing aids/cochlear implants, developmental/physical/occupational therapy, nutritional support, and insulin for the neonatal-diabetes subgroup. Class-level evidence from related mitochondrial aminoacyl-tRNA synthetase (mt-ARS) disorders is discouraging: a 2-year open-label pilot of substrate amino-acid supplementation in AARS2/DARS2 leukoencephalopathy was *"safe and well tolerated by all patients, but efficacy endpoints were not met as no significant improvements were observed in global, cognitive, or motor scores"* ([PMID: 41075682](https://pubmed.ncbi.nlm.nih.gov/41075682/)). A broad aaRS review notes *"amino acid supplementation and dietary interventions have shown effect in select cases, while gene therapy is being explored for dominant ARS-related neuropathies"* ([PMID: 42028791](https://pubmed.ncbi.nlm.nih.gov/42028791/)). By analogy the rational (unproven) substrate for NARS2 is **L-asparagine (CHEBI:22653)**. Because COXPD24 is a mitochondrial disorder, **valproic acid should be avoided or used cautiously** ([PMID: 36661119](https://pubmed.ncbi.nlm.nih.gov/36661119/)).

### Finding 6 — Anatomy & subcellular localization

UniProt Q96I59 describes NARS2 as a 477-amino-acid **class II aminoacyl-tRNA synthetase localized to the mitochondrial matrix**, with an N-terminal mitochondrial transit peptide (residues 1–14). It catalyzes the ATP-dependent, two-step attachment of asparagine to mt-tRNA-Asn (Asn + ATP → Asn-AMP → charged tRNA). Disease targets multiple tissues: **CNS** (basal ganglia, thalamus, brainstem in Leigh syndrome; cortex/global atrophy and delayed myelination in Alpers-like disease), **inner ear/cochlea** (sensorineural hearing loss), **skeletal muscle** (myopathy with combined complex I/IV deficiency), and **endocrine pancreas/β-cells** (neonatal diabetes). CNS and cochlear involvement is typically bilateral/symmetric: *"Leigh syndrome, which is a neurodegenerative disease characterized by symmetric, bilateral lesions in the basal ganglia, thalamus, and brain stem"* ([PMID: 25807530](https://pubmed.ncbi.nlm.nih.gov/25807530/)).

### Finding 7 — Diagnosis

Definitive diagnosis is genetic. Supporting evidence includes: (1) **biochemistry**—elevated serum/CSF lactate and myocardial/muscle enzymes; (2) **muscle biopsy**—combined complex I + IV deficiency by spectrophotometry and BN-PAGE, plus complex V subcomplexes (*"a combined complex I and IV deficiency in skeletal muscle"*, [PMID: 25385316](https://pubmed.ncbi.nlm.nih.gov/25385316/)); (3) **neuroimaging**—Leigh-type symmetric lesions or Alpers-like cerebral atrophy with delayed myelination, and epileptiform EEG/epilepsia partialis continua; (4) **molecular genetics**—trio-based WES or WGS identifying biallelic NARS2 variants, with rapid WES shortening the diagnostic odyssey (*"Rapid whole exome sequencing was performed revealing novel biallelic variants in NARS2"*, [PMID: 30327238](https://pubmed.ncbi.nlm.nih.gov/30327238/)); and (5) **functional confirmation**—decreased charged mt-tRNA-Asn, rescue assays, and LC-MS/MS aminoacylation assays to classify variants of uncertain significance.

### Finding 8 — Temporal course & prognosis

Onset is usually neonatal to early childhood (e.g., 9-month-old with status epilepticus, [PMID: 41426993](https://pubmed.ncbi.nlm.nih.gov/41426993/); 4.5-month-old, [PMID: 36661119](https://pubmed.ncbi.nlm.nih.gov/36661119/); neonatal diabetes median 4 weeks, [PMID: 40887432](https://pubmed.ncbi.nlm.nih.gov/40887432/)), though nonsyndromic deafness may present in childhood. The disease is chronic, progressive, and lifelong with no spontaneous remission. The early-onset encephalopathic form sharing Alpers/Leigh features *"was characterized by more severe disease course and poorer survival compared to the other NARS2 associated phenotypes"* ([PMID: 33596490](https://pubmed.ncbi.nlm.nih.gov/33596490/)). Severe cases include rapidly progressive intractable epilepsy with global brain atrophy and death around 9 months (*"focal status epilepticus that progressed to lethal epileptic encephalopathy"*, [PMID: 30327238](https://pubmed.ncbi.nlm.nih.gov/30327238/)) and fatal refractory status epilepticus ([PMID: 34415467](https://pubmed.ncbi.nlm.nih.gov/34415467/)). The mild end—isolated sensorineural hearing loss—is compatible with prolonged survival.

### Finding 9 — Model systems & comparative biology

Human **NARS2 = NCBI Gene 79731**; conserved orthologs include mouse *Nars2* (Gene 244141), rat *Nars2*, zebrafish *nars2*, and the essential yeast mitochondrial AsnRS ortholog *SLM5* (YCR024C). Published disease models are **cellular/in vitro**—patient-derived fibroblasts and EBV-transformed lymphoblasts showing decreased charged mt-tRNA-Asn, reduced OCR/ETC activity, and rescue by wild-type NARS2 (*"a decrease in oxygen consumption rates (OCR) and electron transport chain (ETC) activity can be rescued by overexpression of wild type NARS2"*, [PMID: 25807530](https://pubmed.ncbi.nlm.nih.gov/25807530/)). High-throughput LC-MS/MS aminoacylation assays in patient fibroblasts classify variants (*"developed a high-throughput LC-MS/MS-based aminoacylation assay to measure aaRS activity in patient-derived fibroblasts"*, [PMID: 42028791](https://pubmed.ncbi.nlm.nih.gov/42028791/)). No dedicated knockout/knock-in animal model has been prominently reported, and no naturally occurring NARS2 disease is catalogued in OMIA; complete loss of the mitochondrial AsnRS is expected to be lethal, limiting constitutive-null organismal models.

### Finding 10 — Etiology is purely monogenic; identifiers and prevention

COXPD24 is a Mendelian, autosomal-recessive disorder caused solely by biallelic NARS2 variants. There are **no established environmental, infectious, toxic, lifestyle, or dietary causal or protective factors**, and no somatic/acquired etiology (all variants are germline). The only genetic risk factor is inheritance of two damaging NARS2 alleles; consanguinity increases the risk of homozygosity. As in other mitochondrial disorders, intercurrent catabolic stressors (febrile illness, fasting) may precipitate metabolic decompensation (inferred from general mitochondrial biology, not NARS2-specific data). A representative statement: COXPD24 is *"a rare mitochondrial and a multisystem autosomal recessive disorder"* ([PMID: 34374940](https://pubmed.ncbi.nlm.nih.gov/34374940/)). Prevention is limited to genetic counseling, cascade carrier testing, prenatal diagnosis, and preimplantation genetic testing (PGT-M) once familial variants are known.

---

## Section-by-Section Report

### 1. Disease Information
COXPD24 is a rare autosomal-recessive multisystem mitochondrial disorder of oxidative phosphorylation caused by defective intramitochondrial translation. **Key identifiers:** MONDO:0014547; OMIM #616239 (Combined oxidative phosphorylation deficiency 24); gene NARS2 (OMIM *612803, HGNC:24406, NCBI Gene 79731, Ensembl ENSG00000137513, UniProt Q96I59); allelic phenotype nonsyndromic deafness DFNB94. Broad ontology mappings: ICD-10 E88.49/E88.40 (disorders of mitochondrial metabolism), ICD-11 5C53.1x (disorders of mitochondrial OXPHOS), MeSH grouping Mitochondrial Diseases (D028361). **Synonyms:** COXPD24; NARS2-related disease/disorder; mitochondrial asparaginyl-tRNA synthetase deficiency. **Data source:** disease-level information is aggregated from individual patient reports and small case series consolidated in systematic reviews ([PMID: 33596490](https://pubmed.ncbi.nlm.nih.gov/33596490/)), not from EHR-scale registries.

### 2. Etiology
**Causal factor:** purely genetic—biallelic pathogenic NARS2 variants. **Genetic risk:** two damaging NARS2 alleles; consanguinity elevates homozygosity risk; recurrent founder-type alleles (e.g., Scandinavian p.Pro214Leu). **Environmental risk/protective factors:** none established. **Gene–environment interaction:** none proven; catabolic stress may act as a nonspecific decompensation trigger (inferred).

### 3. Phenotypes
| Phenotype | Type | Onset | Frequency / Notes | Suggested HPO |
|---|---|---|---|---|
| Sensorineural hearing loss | Clinical sign | Congenital/childhood | Cardinal feature; isolated (DFNB94) or with CNS disease | HP:0000407 |
| Refractory epilepsy / epileptic encephalopathy | Clinical sign | Infantile | Common in severe forms; epilepsia partialis continua reported | HP:0011097, HP:0200134 |
| Global developmental delay / intellectual disability | Clinical sign | Infantile | Frequent | HP:0001263, HP:0001249 |
| Leigh syndrome (symmetric basal ganglia lesions) | Imaging/clinical | Infantile | Severe subgroup | HP:0002415 |
| Alpers-like progressive encephalopathy / brain atrophy | Imaging/clinical | Infantile | Severe, poor survival | HP:0002059, HP:0007303 |
| Myopathy / hypotonia | Clinical sign | Infantile | Combined complex I/IV deficiency on biopsy | HP:0003198, HP:0001252 |
| Spastic paraplegia / ataxia | Clinical sign | Variable | Milder spectrum | HP:0001258, HP:0001251 |
| Neonatal/insulin-dependent diabetes | Lab/clinical | Neonatal (median 4 wk) | Newly recognized; β-cell involvement | HP:0000857, HP:0100651 |
| Lactic acidosis | Lab abnormality | Variable | Supports diagnosis | HP:0003128 |
| Low birthweight | Physical | Congenital | 7/8 in diabetes cohort | HP:0001518 |

**Severity/progression:** variable and genotype-graded, generally progressive; severe encephalopathic forms are life-limiting. **Quality-of-life impact:** major in severe forms (profound disability, seizures, sensory loss); disease-specific QoL instruments have not been applied.

### 4. Genetic/Molecular Information
**Causal gene:** NARS2 (11q14.1). **Variant classes:** predominantly missense and splice-site; also nonsense/truncating (p.Tyr323\*). **Representative variants:** c.822G>C splice, p.Val213Phe, p.Asn381Ser, p.Tyr323\*, p.Pro214Leu, p.Ile182Lys, p.His167Arg, p.Phe216Leu, p.Thr180Asn, p.Val440Leu. **Population frequency:** disease alleles are ultra-rare; gnomAD shows NARS2 is LoF-tolerant (pLI≈0, oe_lof≈0.95), consistent with recessive inheritance. **Origin:** germline (no somatic disease). **Functional consequence:** loss of function via reduced aminoacylation, impaired dimerization (p.Asn381Ser), or absent protein (p.Tyr323\*). **Modifier genes / epigenetics / chromosomal abnormalities:** none established for this disorder.

### 5. Environmental Information
No environmental, occupational, toxic, lifestyle, or infectious factors are implicated. Not applicable as a causal or protective category for this monogenic disease.

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**
1. Biallelic NARS2 variants **lead to** a structurally/functionally defective mitochondrial asparaginyl-tRNA synthetase (loss of function; reduced dimerization or absent protein).
2. Defective mt-AsnRS **results in** reduced aminoacylation (charging) of mitochondrial tRNA-Asn (directly demonstrated: decreased charged mt-tRNA-Asn).
3. Reduced charged mt-tRNA-Asn **impairs** mitochondrial translation of the 13 mtDNA-encoded OXPHOS subunits.
4. Impaired mitochondrial translation **causes** a combined OXPHOS assembly/activity defect, predominantly of complex I and complex IV (with complex V subcomplexes on BN-PAGE).
5. Combined OXPHOS deficiency **leads to** reduced oxygen consumption and ATP production (reduced OCR/ETC activity; rescuable by wild-type NARS2).
6. Bioenergetic failure **results in** cell/tissue dysfunction in high-energy-demand tissues, branching to:
   - CNS neurons → Leigh/Alpers encephalopathy, epilepsy, developmental regression (bilateral symmetric basal ganglia/thalamus/brainstem, or cortical atrophy).
   - Cochlear/inner-ear cells → sensorineural hearing loss.
   - Skeletal myocytes → myopathy/hypotonia.
   - Pancreatic β-cells → impaired insulin secretion → neonatal diabetes (inferred mechanism from β-cell energy dependence).
7. Progressive tissue injury **culminates in** the clinical manifestations and, in severe forms, early death.

**Molecular/cellular detail:** biological process—mitochondrial translation (GO:0032543), asparaginyl-tRNA aminoacylation (GO:0006421); cellular component—mitochondrial matrix (GO:0005759). Cell types (CL): neuron (CL:0000540), cochlear hair cell (CL:0000589/CL:0002494), skeletal muscle cell (CL:0000188), pancreatic beta cell (CL:0000169). Metabolic consequence: energy-metabolism failure with lactic acidosis (CHEBI:24996 lactate). Immune involvement: none characteristic.

### 7. Anatomical Structures Affected
**Primary organs/systems:** central nervous system (UBERON:0000955 brain; basal ganglia UBERON:0002420; thalamus UBERON:0001897; brainstem UBERON:0002298), inner ear/cochlea (UBERON:0001844), skeletal muscle (UBERON:0001134), endocrine pancreas/islets (UBERON:0000006). **Subcellular:** mitochondrial matrix (GO:0005759). **Laterality:** CNS and cochlear involvement typically bilateral/symmetric.

### 8. Temporal Development
**Onset:** congenital to early childhood; most severe cases neonatal–infantile. **Pattern:** subacute-to-chronic, progressive; may show acute decompensations (status epilepticus, stroke-like episodes). **Stages/course:** progressive neurodegeneration in severe forms; stable/slowly progressive in isolated deafness. **Duration:** lifelong. **Remission:** none spontaneous. **Critical period:** early infancy is the key window for diagnosis and supportive intervention.

### 9. Inheritance and Population
**Inheritance:** autosomal recessive. **Epidemiology:** ultra-rare; precise prevalence/incidence not established (fewer than ~40 reported patients). **Penetrance:** high for biallelic damaging genotypes; **expressivity** highly variable and genotype-dependent. **Anticipation:** not applicable (not a repeat-expansion disorder). **Founder effects/consanguinity:** recurrent homozygous alleles in consanguineous populations (Scandinavian, Iranian, Turkish). **Carrier frequency:** low; heterozygous carriers are unaffected (LoF-tolerant gene). **Sex ratio:** no sex bias (autosomal). **Geographic distribution:** worldwide, individual families.

### 10. Diagnostics
**First-line:** whole-exome or whole-genome sequencing (trio-based preferred). **Supportive labs:** elevated blood/CSF lactate, myocardial/muscle enzymes. **Imaging:** MRI (Leigh-type symmetric lesions; Alpers-like atrophy; delayed myelination). **Electrophysiology:** EEG (epileptiform activity, epilepsia partialis continua). **Muscle biopsy:** combined complex I + IV deficiency (spectrophotometry, BN-PAGE). **Functional/omics:** mt-tRNA-Asn charging assays, wild-type rescue, LC-MS/MS aminoacylation for VUS resolution. **Differential diagnosis:** other mt-ARS disorders (AARS2, DARS2, YARS2, IARS2), other Leigh/Alpers etiologies, and other causes of nonsyndromic deafness or neonatal diabetes. **Screening:** cascade carrier testing of relatives; no newborn screening.

### 11. Outcome / Prognosis
Prognosis is **genotype-linked and often severe**. Early-onset Leigh/Alpers-type disease has poor survival with high early mortality; isolated sensorineural hearing loss is compatible with normal lifespan. **Morbidity** in severe forms is profound (refractory epilepsy, developmental disability, sensory loss, insulin-dependent diabetes). **Prognostic factors:** age of onset, encephalopathic phenotype, and structural/biochemical severity of the variant. No validated prognostic biomarkers beyond genotype and lactate.

### 12. Treatment
**Supportive only:** antiepileptic drugs (avoid/limit valproate; NCIT anticonvulsant therapy), hearing rehabilitation (hearing aids, cochlear implants; NCIT), developmental/physical/occupational/speech therapy, nutritional support, and insulin for the neonatal-diabetes subgroup (NCIT insulin therapy). **Experimental:** L-asparagine (CHEBI:22653) substrate repletion—rational but unproven; class-level amino-acid supplementation trials in mt-ARS leukoencephalopathies were safe but ineffective ([PMID: 41075682](https://pubmed.ncbi.nlm.nih.gov/41075682/)). **Advanced therapeutics:** no approved gene, cell, or RNA therapy; gene therapy for ARS disorders is being explored mainly for dominant neuropathies. **Pharmacogenomics:** valproate caution in mitochondrial disease.

### 13. Prevention
No primary prevention (no vaccine, no modifiable risk factor). **Secondary/tertiary:** early diagnosis and supportive management of complications. **Genetic prevention:** genetic counseling, cascade carrier testing, prenatal diagnosis, and preimplantation genetic testing (PGT-M) once familial variants are identified.

### 14. Other Species / Natural Disease
Conserved orthologs: mouse *Nars2* (NCBI Gene 244141), rat *Nars2*, zebrafish *nars2*, yeast *SLM5* (essential mitochondrial AsnRS). No naturally occurring NARS2 disease is catalogued in companion animals or wildlife (OMIA). No zoonotic relevance. The mitochondrial translation mechanism is evolutionarily conserved, but organismal disease has not been reported outside humans.

### 15. Model Organisms
Established models are **cellular/in vitro**: patient-derived skin fibroblasts and EBV-transformed lymphoblasts recapitulating decreased charged mt-tRNA-Asn, reduced OCR/ETC activity, and complementation by wild-type NARS2. High-throughput LC-MS/MS aminoacylation assays in patient fibroblasts serve variant classification. **Limitation:** no dedicated knockout/knock-in mouse, zebrafish, or fly disease model is prominently reported; constitutive nulls are expected to be embryonic-lethal, favoring conditional/hypomorphic or iPSC-derived approaches for future work.

---

## Mechanistic Model / Interpretation

```
 Biallelic NARS2 variants (missense / splice / nonsense)
        │  loss of function (reduced dimerization, low/absent protein)
        ▼
 Defective mitochondrial asparaginyl-tRNA synthetase (mt matrix)
        │
        ▼
 ↓ Charged mt-tRNA-Asn        ← directly demonstrated (PMID 25385316)
        │
        ▼
 Impaired mitochondrial translation of 13 OXPHOS subunits
        │
        ▼
 Combined OXPHOS deficiency (complex I + IV; complex V subcomplexes)
        │
        ▼
 ↓ OCR / ETC activity  ── rescuable by WT NARS2 (PMID 25807530)
        │
        ▼  bioenergetic failure in high-energy tissues
        ├──► CNS neurons  → Leigh / Alpers encephalopathy, epilepsy, DD/ID
        ├──► cochlear cells → sensorineural hearing loss (cardinal)
        ├──► skeletal muscle → myopathy / hypotonia
        └──► pancreatic β-cells → neonatal insulin-dependent diabetes
                                   (severity graded by variant impact)
```

The disease is a textbook example of a **mitochondrial translation defect**: a single enzymatic step (Asn-tRNA charging) constrains synthesis of the mtDNA-encoded OXPHOS subunits, producing a **combined** rather than isolated respiratory-chain deficiency. The consistency of the genotype–phenotype correlation—structural severity predicting clinical severity—supports a **dosage/residual-activity model** in which hypomorphic alleles yield tissue-restricted phenotypes (e.g., deafness only) while more damaging biallelic combinations yield multisystem encephalopathy.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [25385316](https://pubmed.ncbi.nlm.nih.gov/25385316/) | Homozygous splice-site NARS2, two siblings | Establishes combined complex I + IV deficiency and reduced charged mt-tRNA-Asn |
| [25807530](https://pubmed.ncbi.nlm.nih.gov/25807530/) | NARS2 → deafness & Leigh syndrome | Gene-disease proof; complementation rescue; genotype–phenotype correlation |
| [33596490](https://pubmed.ncbi.nlm.nih.gov/33596490/) | Phenotypic variability & natural history | Hearing loss cardinal; early-onset form has poorer survival |
| [40887432](https://pubmed.ncbi.nlm.nih.gov/40887432/) | Neonatal diabetes in COXPD-24 | Expands phenotype; β-cell involvement |
| [34374940](https://pubmed.ncbi.nlm.nih.gov/34374940/) | Novel phenotype/genotype spectrum | Confirms OMIM ID, AR multisystem nature |
| [36661119](https://pubmed.ncbi.nlm.nih.gov/36661119/) | Turkish variant with T1DM | Valproate caution; WES shortens diagnosis |
| [30327238](https://pubmed.ncbi.nlm.nih.gov/30327238/) | Lethal rapidly progressive epilepsy | Rapid WES diagnosis; fatal course |
| [34415467](https://pubmed.ncbi.nlm.nih.gov/34415467/) | Fatal refractory status epilepticus | Severe end of spectrum |
| [41426993](https://pubmed.ncbi.nlm.nih.gov/41426993/) | Stroke-like lesion & status epilepticus | Infantile onset; lactate, MRI features |
| [36523694](https://pubmed.ncbi.nlm.nih.gov/36523694/) | Nonsyndromic SNHL from NARS2 | Confirms DFNB94 phenotype |
| [42028791](https://pubmed.ncbi.nlm.nih.gov/42028791/) | aaRS variant classification & therapy | Functional assays; therapeutic landscape |
| [41075682](https://pubmed.ncbi.nlm.nih.gov/41075682/) | Amino-acid supplementation trial (mt-ARS) | Safe but no efficacy—class-level therapy evidence |
| [41404429](https://pubmed.ncbi.nlm.nih.gov/41404429/) | Tyrosine supplementation in YARS2/MLASA2 | Modest gains in select cases (analogy) |

Evidence is predominantly **human clinical** (case reports/series and one systematic review) plus **in vitro** functional studies in patient-derived cells. There are no randomized trials, and no NARS2-specific therapeutic trial exists.

---

## Limitations and Knowledge Gaps

- **Small sample size:** fewer than ~40 patients reported worldwide; prevalence/incidence are unknown and phenotype frequencies are largely qualitative.
- **No animal model:** no established knockout/knock-in organismal model limits mechanistic and preclinical therapeutic work; constitutive nulls are likely lethal.
- **Genotype–phenotype resolution incomplete:** while structural severity correlates with clinical severity, the basis of tissue-specificity (e.g., why some alleles cause deafness only) is not fully explained.
- **β-cell mechanism inferred:** the pathway from OXPHOS deficiency to impaired insulin secretion is plausible but not directly demonstrated in NARS2 β-cells.
- **No proven therapy:** L-asparagine repletion is untested in NARS2; class-level supplementation trials were negative.
- **No modifier genes, epigenetic, or environmental data** are available for this disorder.

---

## Proposed Follow-up Experiments / Actions

1. **Establish a natural-history registry** aggregating all reported and unpublished cases to quantify phenotype frequencies, survival, and genotype–phenotype correlations.
2. **Generate iPSC-derived models** (neurons, cochlear-like organoids, β-cells) from patients to test tissue-specific bioenergetic phenotypes and the β-cell insulin-secretion defect directly.
3. **Develop conditional/hypomorphic mouse or zebrafish models** to enable in vivo mechanistic and preclinical therapeutic studies without constitutive lethality.
4. **Test L-asparagine substrate repletion** in patient-derived cells (aminoacylation, OCR/ETC rescue) as a rational precursor to any clinical evaluation.
5. **Standardize variant functional classification** using the LC-MS/MS aminoacylation assay to reclassify VUS and refine genotype–phenotype models.
6. **Explore AAV/gene-replacement feasibility** for NARS2 given its recessive loss-of-function mechanism and successful in vitro complementation.
7. **Confirm ontology/identifier mappings** (ICD-11 5C53.1x, MONDO:0014547) and add HPO frequency annotations to the knowledge base entry.

---

*Evidence source types: human clinical (case reports/series, systematic review), in vitro (patient fibroblasts/lymphoblasts, complementation, LC-MS/MS assays), and computational (gnomAD constraint, UniProt/ontology annotation). Citations use PubMed IDs (PMIDs). Where information was unavailable for this ultra-rare disorder, this is stated explicitly.*


## Artifacts

- [OpenScientist final report](Combined_Oxidative_Phosphorylation_Defect_Type_24-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Combined_Oxidative_Phosphorylation_Defect_Type_24-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 4 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000407` (1 mention) - the report calls it "Cardinal feature; isolated (DFNB94) or with CNS disease"; HP calls it **Sensorineural hearing impairment**
- `HP:0002415` (1 mention) - the report calls it "Severe subgroup"; HP calls it **Leukodystrophy**
- `HP:0003128` (1 mention) - the report calls it "Supports diagnosis"; HP calls it **Lactic acidosis**
- `HP:0001518` (1 mention) - the report calls it "7/8 in diabetes cohort"; HP calls it **Small for gestational age**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0007303` (1 mention) - HP does not contain this term