---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-18T17:35:05.967653'
end_time: '2026-09-18T17:49:23.976405'
duration_seconds: 858.01
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Chronic Lymphocytic Inflammation With Pontine Perivascular Enhancement
    Responsive To Steroids
  mondo_id: MONDO:0017297
  category: Complex
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
citation_count: 24
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 25
  on_topic: 18
  validator_version: 0.2.1
term_validation:
  total_terms: 25
  verified: 23
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 0
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: UBERON:0002240
    reported_labels:
    - Secondary/extension:** cervical & thoracic spinal cord
    ontology_label: spinal cord
  - term_id: HP:0000651
    reported_labels:
    - Common; sometimes predominant
    ontology_label: Diplopia
  - term_id: HP:0001260
    reported_labels:
    - Common
    ontology_label: Dysarthria
  - term_id: HP:0003401
    reported_labels:
    - Common; early
    ontology_label: Paresthesia
  - term_id: HP:0000639
    reported_labels:
    - Frequent
    ontology_label: Nystagmus
  - term_id: HP:0002015
    reported_labels:
    - Occasional
    ontology_label: Dysphagia
  - term_id: HP:0100543
    reported_labels:
    - Occasional
    ontology_label: Cognitive impairment
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Chronic_Lymphocytic_Inflammation_With_Pontine_Perivascular_Enhancement_Responsive_To_Steroids-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Chronic_Lymphocytic_Inflammation_With_Pontine_Perivascular_Enhancement_Responsive_To_Steroids-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chronic Lymphocytic Inflammation With Pontine Perivascular Enhancement Responsive To Steroids
- **MONDO ID:** MONDO:0017297 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Chronic Lymphocytic Inflammation With Pontine Perivascular Enhancement Responsive To Steroids** covering all of the
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

# CLIPPERS: Chronic Lymphocytic Inflammation With Pontine Perivascular Enhancement Responsive To Steroids — Comprehensive Disease Report

**MONDO ID:** MONDO:0017297 | **Category:** Complex | **Report date:** 2026-09-18

Evidence base: aggregated disease-level literature (case reports, case series, retrospective cohorts, systematic reviews) — **no primary patient-level dataset was provided**. All quantitative statements come from the published literature cited by PMID.

---

## Summary

**Chronic Lymphocytic Inflammation with Pontine Perivascular Enhancement Responsive to Steroids (CLIPPERS)** is a rare, corticosteroid-responsive inflammatory syndrome of the central nervous system (CNS), first delineated in 2010. It is defined by the triad of (1) subacute pontocerebellar/brainstem clinical symptoms (most commonly gait ataxia, diplopia, dysarthria, and facial paresthesia), (2) a pathognomonic MRI signature of punctate and curvilinear gadolinium-enhancing lesions ("salt-and-pepper" or "pepper-like") predominantly peppering the pons and hindbrain, and (3) a perivascular, predominantly CD4+ T-lymphocytic inflammatory infiltrate on histopathology. The disease is exquisitely responsive to high-dose corticosteroids but follows a relapsing-remitting course that requires long-term steroid-sparing immunosuppression to prevent cumulative brainstem/cerebellar atrophy and permanent disability.

The single most important conceptual advance since the original description is that **CLIPPERS is a syndrome, not a unitary disease** — it is a diagnosis of exclusion that is genetically and etiologically heterogeneous. Most cases appear idiopathic/autoimmune, but approximately **one-third of tested adults carry germline mutations in hemophagocytic lymphohistiocytosis (HLH) genes** (notably *PRF1* and *UNC13D*), defining a treatable genetic subgroup; approximately **16% of cases are associated with malignancy** (chiefly hematologic); and some cases are triggered by or associated with **Epstein–Barr virus (EBV)**. Several mimics — CNS lymphoma, Erdheim–Chester disease, GFAP astrocytopathy, MOGAD, neurosarcoidosis, and primary CNS angiitis — must be excluded, and some "CLIPPERS-like" presentations are early manifestations of lymphoma.

CLIPPERS is ultra-rare: the entire evidence base since 2010 comprises roughly **140 patients across 100 studies** plus a handful of retrospective cohorts, with no population-based prevalence estimate, no validated animal model, and no primary or secondary prevention. Onset is typically adult (mean ~46 years; range 3–79) with a male predominance (~60%). Prognosis is favorable with sustained immunosuppression but poor if untreated — untreated relapses can progress to death. Pediatric CLIPPERS is more aggressive and often steroid-dependent or steroid-resistant. This report synthesizes 13 confirmed findings drawn from 37 reviewed papers across the full disease-characteristics template.

---

## Key Findings

### Finding 1 — Definition and pathognomonic imaging/pathology

CLIPPERS is a rare steroid-responsive CNS inflammatory syndrome centered on the pons and hindbrain, characterized by a distinctive "salt-and-pepper" gadolinium-enhancement pattern. In the 2017 formal diagnostic-criteria study (Tobin et al., *Brain*), CLIPPERS was diagnosed in 23 patients with a median age of onset of 58 years and a male predominance (18 male : 5 female). The hallmark MRI finding is punctate and curvilinear gadolinium-enhancing lesions ("pepper-like") predominantly in the pons, brainstem, and cerebellum, sometimes extending to the spinal cord. A **definite** diagnosis requires demonstration of a perivascular, T-cell-predominant inflammatory infiltrate on biopsy.

> *"CLIPPERS was diagnosed in 23 patients (18 male and five female) and 12 patients had a non-CLIPPERS diagnosis. CLIPPERS patients' median age of onset was 58 years"* — [PMID: 29050399](https://pubmed.ncbi.nlm.nih.gov/29050399/)

> *"The prerequisite for definite CLIPPERS is the perivascular T-cell-predominant inflammatory infiltration observed on pathological analysis."* — [PMID: 38286842](https://pubmed.ncbi.nlm.nih.gov/38286842/)

### Finding 2 — Relapsing-remitting course requiring long-term immunosuppression

CLIPPERS follows a relapsing-remitting course; untreated disease progresses to disability and death. In the nationwide series of 12 patients (Taieb et al., 2012), 42 relapses were analyzed with a mean relapse duration of 2.5 months and a mean Expanded Disability Status Scale (EDSS) at relapse of 4, improving to a residual EDSS of 1.9 after pulse corticosteroids. Biopsy showed perivascular CD4+ T lymphocytes in 5/7 cases with an increased CD4:CD8 ratio. Critically, one patient with untreated relapses progressed to EDSS 10 (death), and patients not maintained on long-term corticosteroids had higher annualized relapse rates. Multiple 2025–2026 case reports confirm that relapses are typically tied to steroid taper and are controlled with steroid-sparing agents (methotrexate, mycophenolate mofetil).

> *"Thirty-eight of 42 relapses were treated with pulse corticosteroid therapy, which led to improvement, with a mean residual EDSS score of 1.9"* — [PMID: 22777259](https://pubmed.ncbi.nlm.nih.gov/22777259/)

> *"In 1 patient with untreated relapses, scores on the EDSS progressively increased to a score of 10 at death."* — [PMID: 22777259](https://pubmed.ncbi.nlm.nih.gov/22777259/)

### Finding 3 — Paraneoplastic/pre-lymphomatous and genetic mimics

CLIPPERS can be a paraneoplastic or pre-lymphomatous mimic, and inborn errors of immunity underlie some (especially pediatric) cases. Multiple biopsy-confirmed cases show CLIPPERS-like presentations preceding or accompanying lymphoma (B-cell, cutaneous/peripheral T-cell lymphoma). Genetic associations include compound heterozygous *UNC13D* (Munc13-4) variants producing a CLIPPERS-like syndrome, and pediatric reviews flag *PRF1* (perforin) mutations with links to HLH/EBV-driven lymphoproliferation, sometimes requiring hematopoietic stem cell transplant.

> *"We report two patients with CLIPPERS-like brain MRI findings who carried the same missense UNC13D variant in one allele along with deleterious variants in the opposite allele."* — [PMID: 41781714](https://pubmed.ncbi.nlm.nih.gov/41781714/)

> *"Future pediatric workup should include genetic studies because of commonly associated mutations such as PRF1."* — [PMID: 41401665](https://pubmed.ncbi.nlm.nih.gov/41401665/)

> *"CLIPPERS-like presentations have been increasingly recognized as potential early manifestations of underlying lymphoma, most commonly B-cell types."* — [PMID: 41550451](https://pubmed.ncbi.nlm.nih.gov/41550451/)

### Finding 4 — Phenotype and epidemiology

In a systematic review of 140 patients from 100 studies (Al-Chalabi et al., 2022), the mean age was 46 ± 18 years, 60% were male, ataxia was the most common presenting symptom, 16% of cases were associated with malignancy (mostly hematologic), and the overall relapse rate was 59.2%. The core clinical tetrad from case series comprises gait ataxia, diplopia (internuclear ophthalmoplegia / cranial nerve VI palsy / skew deviation), cerebellar dysarthria, and facial paresthesia; nystagmus, dysphagia, and cognitive impairment also occur. The original 2010 description reported patients presenting with episodic diplopia or facial paresthesias followed by brainstem/myelopathic symptoms.

> *"We identified 100 case reports and series including a total of 140 patients with CLIPPERS (mean age: 46±18 years and males were 60%)... Ataxia was the most common presenting symptom. Sixteen percent of the cases were associated with malignancy, mostly hematologic malignancies. The overall relapse rate was 59.2%"* — [PMID: 36029706](https://pubmed.ncbi.nlm.nih.gov/36029706/)

> *"All eight patients (five female, three male) presented with episodic diplopia or facial paresthesias with subsequent brainstem and occasionally myelopathic symptoms and had a favourable initial response to high dose glucocorticosteroids."* — [PMID: 20639547](https://pubmed.ncbi.nlm.nih.gov/20639547/)

### Finding 5 — Pathophysiology and mimics

CLIPPERS pathophysiology is an immune-mediated, predominantly CD4+ T-cell perivascular inflammation of the hindbrain, with a defined MRI signature and important neoplastic/histiocytic mimics. Pathology consistently shows a perivascular and parenchymal T-lymphocytic (predominantly CD4+) infiltrate with variable CD20+ B cells; some Chinese series notably reported CD20+ B-cell-dominant infiltrates in a subset. The etiology "remains unclear but is believed to involve immune-mediated mechanisms." The MRI signature (2010) is symmetric curvilinear gadolinium enhancement "peppering the pons" and extending to medulla, brachium pontis, cerebellum, midbrain, and occasionally spinal cord; lesions lack restricted diffusion, have little perilesional edema, and are typically ≤3 mm. Key mimics with distinct pathophysiology include Erdheim–Chester disease (clonal histiocytes with MAPK-ERK/BRAF activation), CNS lymphoma, GFAP astrocytopathy, MOGAD, neurosarcoidosis, and primary CNS angiitis.

> *"All patients had symmetric curvilinear gadolinium enhancement peppering the pons and extending variably into the medulla, brachium pontis, cerebellum, midbrain and occasionally spinal cord."* — [PMID: 20639547](https://pubmed.ncbi.nlm.nih.gov/20639547/)

> *"ECD is a histiocytic neoplasm characterized by multiorgan infiltration of clonal histiocytes carrying activating variants of the MAPK-ERK pathway. Neurologic involvement occurs in up to 40% of ECD with frequent brainstem lesions that can mimic acquired neuroinflammatory disorders, such as CLIPPERS."* — [PMID: 39047207](https://pubmed.ncbi.nlm.nih.gov/39047207/)

> *"The etiology of CLIPPERS remains unclear, but it is believed to involve immune-mediated mechanisms."* — [PMID: 40821365](https://pubmed.ncbi.nlm.nih.gov/40821365/)

### Finding 6 — Treatment ladder

High-dose corticosteroids induce remission; long-term steroid-sparing immunosuppression prevents relapse; IVIg is ineffective; and pediatric disease is aggressive. Induction typically uses high-dose IV methylprednisolone (e.g., 1 g/day × 5 days), producing rapid clinical and radiological improvement. Maintenance uses long-term low-dose corticosteroid or corticosteroid plus an immunosuppressant; agents reported include methotrexate, mycophenolate mofetil, rituximab, cyclophosphamide, hydroxychloroquine, azathioprine, natalizumab, and infliximab. IVIg showed poor efficacy for both acute treatment and relapse prevention. Pediatric CLIPPERS is more aggressive, often steroid-dependent/resistant, with deaths and progression to EBV-driven B-cell lymphoma; genetic cases may require hematopoietic stem cell transplant.

> *"Long-term low-dose corticosteroid maintenance therapy or corticosteroids coupled with immunosuppressants are recommended to prevent"* [relapse] — [PMID: 38286842](https://pubmed.ncbi.nlm.nih.gov/38286842/)

> *"IVIg had a poor effect on the acute phase of CLIPPERS symptoms. Compared with other immunosuppressants, IVIg is less effective in suppressing the relapse of CLIPPERS."* — [PMID: 36938308](https://pubmed.ncbi.nlm.nih.gov/36938308/)

> *"CLIPPERS disease in children is aggressive, with poor response to immunotherapy."* — [PMID: 30146710](https://pubmed.ncbi.nlm.nih.gov/30146710/)

### Finding 7 — Diagnosis of exclusion

CLIPPERS diagnosis rests on characteristic MRI plus supportive CSF findings (mild lymphocytic pleocytosis, elevated protein), with biopsy reserved for red flags. CSF typically shows mild lymphocytic pleocytosis and elevated protein, with inconstant oligoclonal bands (4/12 in the Taieb series) and an increased CD4:CD8 T-cell ratio. No specific serum/CSF biomarker exists. Diagnosis follows the 2017 criteria: subacute pontocerebellar symptoms + punctate/curvilinear "salt-and-pepper" hindbrain gadolinium enhancement (individual lesions ≤3 mm, T2 abnormality not exceeding enhancement, no mass effect/restricted diffusion) + exclusion of mimics. "Probable" is clinicoradiologic; "definite" adds perivascular T-cell biopsy confirmation. Biopsy is strongly advised when red flags are present. Emerging tools include CSF circulating tumor DNA (ctDNA) to unmask occult lymphoma.

> *"We evaluated clinical, radiological and pathological features of patients referred for suspected CLIPPERS and propose diagnostic criteria to discriminate CLIPPERS from non-CLIPPERS aetiologies."* — [PMID: 29050399](https://pubmed.ncbi.nlm.nih.gov/29050399/)

> *"Cerebrospinal fluid (CSF) analysis showed lymphocytic pleocytosis and elevated protein, while infectious and neoplastic causes were ruled out."* — [PMID: 41249905](https://pubmed.ncbi.nlm.nih.gov/41249905/)

### Finding 8 — HLH-gene mutations define a treatable genetic subgroup

A substantial subset (~one-third) of adult CLIPPERS carries germline HLH-gene mutations. In Taieb et al. 2021, among a cohort of 36 CLIPPERS-2017 patients, 12 consented to genetic testing of 8 primary HLH genes; mutations were identified in 4/12 (three with biallelic variants). HLH-associated genes govern cytotoxic granule-mediated killing: *PRF1* (perforin, HGNC:8664, OMIM 170280), *UNC13D* (Munc13-4, HGNC:23147, OMIM 608897), *STX11*, *STXBP2*, plus *RAB27A*, *LYST*, *SH2D1A*, and *XIAP*. An independent report described compound-heterozygous *UNC13D* variants with downregulated Munc13-4 protein producing CLIPPERS-like disease.

> *"In our patients presenting with adult-onset CLIPPERS, one-third have HLH gene mutations. This genetic treatable condition should be searched in patients with CLIPPERS, especially in those presenting with atypical findings."* — [PMID: 33658321](https://pubmed.ncbi.nlm.nih.gov/33658321/)

> *"identified to have compound heterozygous UNC13D variants along with downregulated Munc13-4 p[rotein]"* — [PMID: 41781714](https://pubmed.ncbi.nlm.nih.gov/41781714/)

### Finding 9 — Anatomical distribution

CLIPPERS centers on the pons/hindbrain but extends to spinal cord and supratentorial regions. Primary sites: pons (UBERON:0000988), middle cerebellar peduncle/brachium pontis, cerebellum (UBERON:0002037), medulla (UBERON:0001896), and midbrain (UBERON:0001891). Frequent extension: cervical/thoracic spinal cord (UBERON:0002240) with nodular enhancement and myelopathy/spastic paraparesis; supratentorial white matter, thalamus, basal ganglia, internal capsule, and corpus callosum/splenium. The affected tissue is CNS nervous tissue with perivascular (angiocentric) small-vessel targeting; lesions are typically bilateral/symmetric. Onset is subacute, mostly in adults (median ~46–58 years, reported ages 3–79), with a chronic relapsing-remitting course. Asymmetric or unilateral lesions are atypical and constitute a red flag.

> *"MRI showed characteristic punctate hyper-intensities with enhancement in the brain stem, cerebellar peduncles, and optic chiasm and diffuse nodular enhancement throughout the cervical and thoracic spinal cord."* — [PMID: 29055484](https://pubmed.ncbi.nlm.nih.gov/29055484/)

> *"predominantly involving the pons and cerebellar hemispheres, with additional foci in the left internal capsule, splenium of the corpus callosum, and supratentorial subcortical white matter"* — [PMID: 41749027](https://pubmed.ncbi.nlm.nih.gov/41749027/)

### Finding 10 — Prognosis

CLIPPERS prognosis is favorable with sustained treatment, but recurrent untreated attacks cause cumulative brainstem/cerebellar atrophy and permanent disability. As stated by Abkur et al. (2017), long-term immunosuppression appears mandatory to achieve sustained remission and prevent atrophy-related disability. In the Taieb series, pulse steroids reduced mean EDSS from 4 (relapse) to a residual 1.9; patients off long-term steroids had higher annualized relapse rates; one untreated patient reached EDSS 10 (death). Prognostic red flags for worse outcome or an alternative diagnosis include steroid resistance, atypical/large (>3 mm) lesions, mass effect, longitudinally extensive transverse myelitis, systemic symptoms, young/pediatric onset, and underlying malignancy or an HLH-gene mutation.

> *"Long-term immunosuppression appears to be mandatory in order to achieve sustained remission and prevent disability related to atrophy of the structures involved in repeated attacks."* — [PMID: 28110629](https://pubmed.ncbi.nlm.nih.gov/28110629/)

### Finding 11 — Idiopathic etiology; EBV and occult lymphoma as triggers

CLIPPERS is idiopathic/immune-mediated with no established environmental or lifestyle risk factors; EBV and occult lymphoma are recognized triggers/associations. Etiology and pathogenesis are explicitly stated as unknown in multiple sources. No toxin, radiation, occupational, dietary, smoking, or alcohol risk factor has been established. Recognized associations/triggers include intracranial EBV infection accompanying CLIPPERS, EBV-driven B-cell lymphoma emerging during pediatric CLIPPERS, and occult hematologic/solid malignancy in ~16%. The main non-modifiable "risk factors" are the immune/genetic host state (adult age, male sex, HLH-gene carriage) rather than exogenous exposures.

> *"Its etiology and pathogenesis are unknown, that together with the polymorphic and sometimes confounding neurological manifestations, and radiological findings represent a real diagnostic and therapeutic challenge for clinicians."* — [PMID: 33851608](https://pubmed.ncbi.nlm.nih.gov/33851608/)

> *"we report a case of CLIPPERS presenting with intracranial Epstein-Barr virus (EBV) infection and diffuse white matter involvement."* — [PMID: 27861371](https://pubmed.ncbi.nlm.nih.gov/27861371/)

### Finding 12 — Ultra-rare, sporadic; no animal model; no primary prevention

CLIPPERS is an ultra-rare, sporadic, adult-onset syndrome with no formal prevalence estimate, no animal models, and no primary prevention. It is described as "very rare" with "only a few sporadic cases reported," and the largest synthesis is a systematic review of just 140 patients from 100 studies since the 2010 first description. No population-based incidence/prevalence figure exists in Orphanet or registries. Knowledge is derived entirely from aggregated case reports, case series, and a few retrospective cohorts (not EHR/population datasets). No validated animal (mouse/rat/zebrafish) or in vitro model of CLIPPERS exists; the HLH-gene subgroup shares biology with established *Prf1*-/- and *Unc13d* (jinx) HLH mouse models, but these model HLH — not CLIPPERS specifically. No natural analogue disease has been reported in other species (OMIA has no CLIPPERS entry). No primary or secondary prevention or vaccination applies; "prevention" is limited to tertiary prevention (maintenance immunosuppression to prevent relapse-related atrophy) and genetic counseling for the autosomal-recessive HLH-gene subgroup.

> *"A very rare inflammatory disease of CNS, CLIPPERS syndrome, was recently described and only a few sporadic cases are reported in the medical literature."* — [PMID: 33851608](https://pubmed.ncbi.nlm.nih.gov/33851608/)

> *"We identified 100 case reports and series including a total of 140 patients with CLIPPERS"* — [PMID: 36029706](https://pubmed.ncbi.nlm.nih.gov/36029706/)

### Finding 13 — Consolidated synthesis

Integrating all findings: CLIPPERS is a steroid-responsive CD4+ T-cell perivascular hindbrain inflammatory syndrome, heterogeneous in cause, requiring lifelong immunosuppression. Its four pillars are (1) definition/imaging; (2) relapsing course with maintenance need; (3) etiologic heterogeneity — idiopathic autoimmune majority, autosomal-recessive HLH-gene subgroup in ~1/3 of tested adults (*PRF1*/*UNC13D*), paraneoplastic (~16% malignancy), and EBV-associated; (4) diagnosis of exclusion via 2017 criteria with CSF lymphocytic pleocytosis and no specific biomarker; treated by a ladder of high-dose corticosteroids → steroid-sparing agents (methotrexate, MMF, rituximab, natalizumab), with IVIg ineffective and HSCT for genetic/aggressive cases; and it is ultra-rare (~140 total reported cases) with no animal model and only tertiary prevention.

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** CLIPPERS is a rare CNS inflammatory syndrome, first named in 2010 (Pittock et al.), defined by subacute brainstem/cerebellar dysfunction, a distinctive "salt-and-pepper" pontine gadolinium enhancement pattern, and a perivascular T-cell inflammatory infiltrate that responds dramatically to corticosteroids.

**Key identifiers.** MONDO:0017297. It lacks a distinct OMIM number (it is not a single-gene Mendelian disorder). No dedicated ICD-10 code exists; it is generally coded under CNS inflammatory/demyelinating disease categories. It is recognized in the neuroimmunology literature and included in registries such as the Indian IMSRN cohort ([PMID: 42011245](https://pubmed.ncbi.nlm.nih.gov/42011245/), where CLIPPERS represented only 0.06% — 3 of 4,976 — of CNS demyelinating/allied disorders).

**Synonyms.** "CLIPPERS syndrome"; "CLIPPERS-like syndrome" (for cases pending exclusion of mimics). A supratentorial variant, **SLIPPERS** (Supratentorial Lymphocytic Inflammation with Parenchymal Perivascular Enhancement Responsive to Steroids), is described but its independent existence is debated ([PMID: 34345468](https://pubmed.ncbi.nlm.nih.gov/34345468/), [PMID: 37626547](https://pubmed.ncbi.nlm.nih.gov/37626547/), [PMID: 41718297](https://pubmed.ncbi.nlm.nih.gov/41718297/)).

**Source of information.** Disease-level, derived from aggregated case reports, case series, and small retrospective cohorts — not large EHR/population datasets (Findings 1, 12).

### 2. Etiology

**Primary causes.** Idiopathic/immune-mediated in the majority (Findings 5, 11). A treatable **genetic subgroup** carries biallelic HLH-gene mutations (~1/3 of tested adults; Finding 8). A **paraneoplastic** subgroup (~16%) is associated with malignancy, mostly hematologic (Finding 4). An **infectious/EBV-associated** subgroup exists (Finding 11).

**Genetic risk factors.** *PRF1* (perforin), *UNC13D* (Munc13-4), and other primary HLH genes (*STX11*, *STXBP2*, *RAB27A*, *LYST*, *SH2D1A*, *XIAP*) — cytotoxic-granule pathway genes (Finding 8).

**Environmental risk factors.** None established. Non-modifiable host factors: adult age, male sex, HLH-gene carriage (Finding 11).

**Protective factors.** None described (not reported / not applicable).

**Gene–environment interactions.** Plausibly, HLH-gene hypomorphism impairs cytotoxic clearance of EBV-infected/antigen-presenting cells, permitting EBV-driven or antigen-driven T-cell perivascular inflammation — an inferred mechanism, not demonstrated (Findings 3, 8, 11).

### 3. Phenotypes

| Phenotype | Type | Frequency / notes | Suggested HPO |
|---|---|---|---|
| Gait ataxia | Clinical sign | Most common presenting symptom | HP:0002066 / HP:0001251 |
| Diplopia (INO, CN VI palsy, skew) | Symptom/sign | Common; sometimes predominant | HP:0000651 |
| Dysarthria (cerebellar) | Clinical sign | Common | HP:0001260 |
| Facial paresthesia | Symptom | Common; early | HP:0003401 |
| Nystagmus | Clinical sign | Frequent | HP:0000639 |
| Dysphagia | Symptom | Occasional | HP:0002015 |
| Cognitive impairment | Symptom | Occasional | HP:0100543 |
| Spastic paraparesis/myelopathy | Sign | With spinal cord involvement | HP:0001258 |

**Characteristics.** Onset subacute, adult-predominant (mean ~46 yrs, range 3–79); severity variable; progression episodic/relapsing-remitting and progressive if untreated; relapse rate ~59% (Findings 4, 9). **CSF:** mild lymphocytic pleocytosis, elevated protein, increased CD4:CD8 ratio (Finding 7). **Quality of life:** driven by disability from brainstem/cerebellar dysfunction; EDSS improves from ~4 (relapse) to residual ~1.9 with treatment (Findings 2, 10).

### 4. Genetic/Molecular Information

**Causal genes (subgroup).** *PRF1* (HGNC:8664, OMIM 170280), *UNC13D* (HGNC:23147, OMIM 608897); additional HLH genes as above (Finding 8).

**Pathogenic variants.** Compound heterozygous/biallelic missense and deleterious variants; e.g., a hypomorphic *UNC13D* missense variant with a deleterious variant in trans, and downregulated Munc13-4 protein (Findings 3, 8). Variant classification per ACMG/AMP: pathogenic/likely pathogenic in described families; functional consequence is **loss of function** (impaired cytotoxic degranulation). Somatic vs germline: **germline**. Population allele frequencies for individual HLH variants are typically rare (gnomAD); specific per-variant frequencies were not enumerated in the CLIPPERS literature reviewed.

**Modifier genes / epigenetics / chromosomal abnormalities.** Not established for CLIPPERS (not reported).

### 5. Environmental Information

No environmental, occupational, or lifestyle factors are established (Finding 11). **Infectious agents:** EBV is a recognized association/trigger (intracranial EBV infection with CLIPPERS; EBV-driven B-cell lymphoma in pediatric CLIPPERS) — [PMID: 27861371](https://pubmed.ncbi.nlm.nih.gov/27861371/), [PMID: 30146710](https://pubmed.ncbi.nlm.nih.gov/30146710/). CHEBI-relevant therapeutic entities include prednisolone/methylprednisolone (CHEBI:8378 / CHEBI:6888).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

```
1. Predisposing host state — germline HLH-gene hypomorphism (PRF1/UNC13D loss of
   function) OR occult neoplasm OR EBV infection OR unknown idiopathic trigger
        │  leads to
        ▼
2. Impaired cytotoxic-lymphocyte granule-mediated killing (inferred, for the
   HLH-gene subgroup) OR sustained antigenic stimulation
        │  results in
        ▼
3. Failure to clear activated antigen-presenting cells / infected cells →
   persistent T-cell activation (inferred)
        │  leads to
        ▼
4. Angiocentric homing of predominantly CD4+ T lymphocytes (± CD20+ B cells) to
   small vessels of the pons/hindbrain (demonstrated on biopsy)
        │  results in
        ▼
5. Perivascular ("perivascular-cuffing") lymphocytic inflammation with
   blood–brain-barrier disruption → punctate/curvilinear gadolinium enhancement
   ("salt-and-pepper") (demonstrated: MRI + histology)
        │  leads to
        ▼
6. Local tissue dysfunction of pontocerebellar tracts and cranial-nerve nuclei →
   ataxia, diplopia, dysarthria, facial paresthesia (demonstrated clinically)
        │  branch (untreated / recurrent attacks)
        ▼
7. Cumulative brainstem/cerebellar atrophy → permanent disability, death
   (demonstrated: EDSS progression to 10 in an untreated patient)
        │  branch (some cases)
        ▼
7'. Evolution to / unmasking of CNS or systemic lymphoma (demonstrated in
    paraneoplastic subgroup)
```

**Molecular/cellular detail.** Immune-mediated perivascular inflammation (GO:0006954 inflammatory response; GO:0002250 adaptive immune response). Cell types: CD4+ T lymphocyte (CL:0000624), CD8+ T lymphocyte (CL:0000625), B lymphocyte (CL:0000236). For the HLH-gene subgroup, the defective process is cytotoxic-granule exocytosis/regulated secretory pathway (GO:0045055; perforin/Munc13-4 function). The MAPK-ERK pathway is relevant only to the Erdheim–Chester mimic, not CLIPPERS itself (Finding 5). Upstream = host predisposition (genetic/neoplastic/infectious); downstream = perivascular T-cell inflammation and tissue injury.

### 7. Anatomical Structures Affected

- **Primary:** pons (UBERON:0000988), middle cerebellar peduncle/brachium pontis, cerebellum (UBERON:0002037), medulla (UBERON:0001896), midbrain (UBERON:0001891).
- **Secondary/extension:** cervical & thoracic spinal cord (UBERON:0002240), supratentorial white matter, thalamus, basal ganglia, internal capsule, corpus callosum/splenium, optic chiasm.
- **Body system:** central nervous system (nervous system).
- **Tissue/cell:** CNS nervous tissue; perivascular (angiocentric) small vessels; CD4+ T lymphocytes (CL:0000624), variable CD20+ B cells (CL:0000236).
- **Lateralization:** typically bilateral/symmetric; unilateral/asymmetric is a red flag (Finding 9).

### 8. Temporal Development

Onset subacute, adult-predominant (median ~46–58 yrs; reported 3–79). Course: chronic relapsing-remitting; mean relapse duration ~2.5 months; ~59% relapse rate; progressive and potentially fatal if untreated. Remission is treatment-induced (steroid pulse); relapses cluster around steroid taper/discontinuation. Critical intervention window: early corticosteroid initiation and sustained maintenance to prevent irreversible atrophy (Findings 2, 4, 9, 10).

### 9. Inheritance and Population

**Epidemiology.** Ultra-rare; no formal prevalence/incidence figure exists (~140 total reported patients). Male predominance (~60%). **Inheritance (genetic subgroup):** autosomal recessive (biallelic HLH-gene variants); the idiopathic majority is sporadic/non-Mendelian. Penetrance, expressivity, anticipation, mosaicism, founder effects, consanguinity, and carrier frequencies specific to CLIPPERS are not characterized. **Demographics:** no defined ethnic/geographic predisposition; cases reported worldwide (Findings 8, 12).

### 10. Diagnostics

- **Imaging (key):** MRI with gadolinium — punctate/curvilinear "salt-and-pepper" enhancement in pons/hindbrain; lesions ≤3 mm, no restricted diffusion, minimal edema, no mass effect.
- **CSF:** mild lymphocytic pleocytosis, elevated protein, increased CD4:CD8 ratio, inconstant oligoclonal bands; **no specific biomarker**.
- **Biopsy:** perivascular T-cell (CD4+ predominant) infiltrate; required for **definite** diagnosis and when red flags present.
- **Genetic testing:** panel of primary HLH genes (*PRF1*, *UNC13D*, *STX11*, *STXBP2*, *RAB27A*, *LYST*, *SH2D1A*, *XIAP*) recommended, especially with atypical features (Finding 8).
- **Emerging:** CSF ctDNA to detect occult lymphoma (Finding 7).
- **Criteria:** 2017 Tobin/Mayo criteria — "probable" (clinicoradiologic) vs "definite" (plus biopsy).
- **Differential diagnosis:** CNS lymphoma (PCNSL), Erdheim–Chester disease, GFAP astrocytopathy, MOGAD, NMOSD, neurosarcoidosis, primary CNS angiitis, Behçet, Susac syndrome (Findings 5, 7).

### 11. Outcome/Prognosis

Favorable with sustained immunosuppression (residual EDSS ~1.9); poor if untreated (progression to EDSS 10/death). Chief complication is cumulative brainstem/cerebellar atrophy from repeated attacks. Worse-prognosis red flags: steroid resistance, large/atypical lesions, mass effect, longitudinally extensive transverse myelitis, systemic symptoms, pediatric onset, malignancy, HLH-gene mutation (Finding 10).

### 12. Treatment

| Line | Intervention | Notes | Suggested NCIT |
|---|---|---|---|
| Induction | High-dose IV methylprednisolone (e.g., 1 g/day × 5 d) | Rapid clinical/radiologic response | C29383 (Corticosteroid) |
| Maintenance | Low-dose corticosteroid ± steroid-sparing agent | Prevents relapse-related atrophy | C29383 |
| Steroid-sparing | Methotrexate, mycophenolate mofetil | Sustains remission | C642 (Methotrexate); C61501 (MMF) |
| Steroid-sparing (alt.) | Rituximab, cyclophosphamide, azathioprine, hydroxychloroquine, natalizumab, infliximab | Case-based use | C1702 (Rituximab); C405 (Cyclophosphamide) |
| Not recommended | IVIg | Poor efficacy acutely and for relapse prevention | C513 (IVIG) |
| Genetic/aggressive | Hematopoietic stem cell transplant | For HLH-gene/pediatric refractory cases | C15431 (HSCT) |

Pharmacogenomics/personalized medicine: genotype-guided care applies to the HLH-gene subgroup (consider HSCT and HLH-directed management). (Finding 6.)

### 13. Prevention

No primary or secondary prevention or vaccination applies. **Tertiary prevention** = maintenance immunosuppression to prevent relapse-related atrophy and disability. **Genetic counseling** is relevant for the autosomal-recessive HLH-gene subgroup. Surveillance for occult malignancy is prudent given ~16% association (Findings 6, 10, 12).

### 14. Other Species / Natural Disease

No naturally occurring CLIPPERS analogue is reported in other species (OMIA has no entry; Finding 12). Orthologous HLH-pathway genes exist across mammals (*Prf1*, *Unc13d* in mouse; NCBI Taxon 10090). No zoonotic or cross-species transmission (not applicable — CLIPPERS is non-infectious/immune-mediated).

### 15. Model Organisms

No validated animal or in vitro model of CLIPPERS exists. The HLH-gene subgroup shares biology with established HLH mouse models — *Prf1*-/- (perforin knockout) and *Unc13d* (jinx) mice — but these recapitulate **HLH**, not CLIPPERS's pontine perivascular phenotype (Finding 12). Model resources for the underlying genes: MGI (mouse), plus IMPC/KOMP knockout lines for *Prf1*/*Unc13d*. A key limitation is that no model reproduces the hallmark salt-and-pepper hindbrain enhancement.

---

## Mechanistic Model / Interpretation

CLIPPERS is best understood as a **radiologic-histologic reaction pattern** (perivascular, CD4+ T-cell-predominant hindbrain inflammation producing salt-and-pepper enhancement) that can arise from multiple upstream causes rather than a single etiologic disease. The unifying downstream event is angiocentric lymphocytic inflammation of pontine/cerebellar small vessels with blood–brain-barrier breakdown; the divergent upstream drivers are (a) idiopathic autoimmunity, (b) biallelic HLH-gene loss of function impairing cytotoxic clearance, (c) paraneoplasia/occult lymphoma, and (d) EBV.

```
        ┌─────────────── UPSTREAM DRIVERS (heterogeneous) ───────────────┐
        │  Idiopathic     HLH-gene LOF      Occult neoplasm     EBV       │
        │  autoimmune    (PRF1/UNC13D)      (~16%)           infection    │
        └───────┬───────────────┬───────────────┬───────────────┬────────┘
                └───────────────┴───────┬───────┴───────────────┘
                                        ▼
              CONVERGENT LESION: perivascular CD4+ T-cell inflammation
                        of pons/hindbrain small vessels
                                        ▼
              MRI SIGNATURE: punctate/curvilinear "salt-and-pepper"
                         gadolinium enhancement (≤3 mm)
                                        ▼
              CLINICAL: ataxia, diplopia, dysarthria, facial paresthesia
                                        ▼
        ┌───────────────── OUTCOME (treatment-dependent) ────────────────┐
        │  Treated → remission (EDSS ~1.9)  │  Untreated → atrophy, death │
        └────────────────────────────────────────────────────────────────┘
```

This model explains why CLIPPERS is a **diagnosis of exclusion**, why genetic testing and malignancy surveillance are essential, and why the same corticosteroid-responsive phenotype can carry radically different prognoses depending on the upstream driver.

---

## Evidence Base

| PMID | Contribution | Supports finding(s) |
|---|---|---|
| [29050399](https://pubmed.ncbi.nlm.nih.gov/29050399/) | 2017 diagnostic criteria; cohort of 23 CLIPPERS vs 12 non-CLIPPERS; age/sex | F1, F7, F13 |
| [22777259](https://pubmed.ncbi.nlm.nih.gov/22777259/) | 12-patient series; 42 relapses; EDSS outcomes; death untreated; CD4 biopsy | F2, F10 |
| [36029706](https://pubmed.ncbi.nlm.nih.gov/36029706/) | Systematic review 140 patients; epidemiology, 16% malignancy, 59.2% relapse | F4, F11, F12, F13 |
| [20639547](https://pubmed.ncbi.nlm.nih.gov/20639547/) | Original 2010 description; MRI signature; presenting symptoms | F1, F4, F5 |
| [33658321](https://pubmed.ncbi.nlm.nih.gov/33658321/) | HLH-gene mutations in ~1/3 of adult CLIPPERS | F8, F13 |
| [41781714](https://pubmed.ncbi.nlm.nih.gov/41781714/) | Compound-het UNC13D with downregulated Munc13-4 in CLIPPERS-like disease | F3, F8 |
| [41401665](https://pubmed.ncbi.nlm.nih.gov/41401665/) | Pediatric CLIPPERS; PRF1; genetic workup recommended | F3, F6 |
| [41550451](https://pubmed.ncbi.nlm.nih.gov/41550451/) | CLIPPERS-like as early lymphoma manifestation; CSF ctDNA | F3, F7 |
| [38286842](https://pubmed.ncbi.nlm.nih.gov/38286842/) | Contemporary review; pathology prerequisite; maintenance therapy; no biomarker | F1, F6, F7 |
| [39047207](https://pubmed.ncbi.nlm.nih.gov/39047207/) | Erdheim–Chester (MAPK-ERK) mimic of CLIPPERS | F5 |
| [40821365](https://pubmed.ncbi.nlm.nih.gov/40821365/) | Immune-mediated etiology; advanced MRI | F5 |
| [36938308](https://pubmed.ncbi.nlm.nih.gov/36938308/) | IVIg ineffective | F6 |
| [30146710](https://pubmed.ncbi.nlm.nih.gov/30146710/) | Aggressive pediatric disease; EBV-driven lymphoma | F6, F11 |
| [41249905](https://pubmed.ncbi.nlm.nih.gov/41249905/) | Typical CSF profile; exclusionary diagnosis | F7 |
| [29055484](https://pubmed.ncbi.nlm.nih.gov/29055484/) | Spinal cord + optic chiasm involvement | F9 |
| [41749027](https://pubmed.ncbi.nlm.nih.gov/41749027/) | Pontocerebellar predominance with supratentorial extension | F9 |
| [28110629](https://pubmed.ncbi.nlm.nih.gov/28110629/) | Atrophy from repeated attacks; mandatory long-term immunosuppression | F10 |
| [33851608](https://pubmed.ncbi.nlm.nih.gov/33851608/) | Idiopathic; very rare/sporadic | F11, F12 |
| [27861371](https://pubmed.ncbi.nlm.nih.gov/27861371/) | Intracranial EBV association | F11 |
| [41756550](https://pubmed.ncbi.nlm.nih.gov/41756550/) | Corpus callosum involvement; MMF maintenance; relapse on taper | F2, F9 |
| [33498046](https://pubmed.ncbi.nlm.nih.gov/33498046/) | CD20+ B-cell-dominant infiltrate in a subset (challenges CD4+ canon) | F5 |

**Supporting registry context:** [PMID: 42011245](https://pubmed.ncbi.nlm.nih.gov/42011245/) (IMSRN) records CLIPPERS at only 0.06% of CNS demyelinating/allied disorders, corroborating extreme rarity.

---

## Limitations and Knowledge Gaps

1. **Evidence quality is low.** The entire literature is case reports, small series, and a single systematic review (~140 patients). No randomized trials, no population registries, and no formal prevalence estimate exist.
2. **No specific biomarker.** Diagnosis remains exclusionary; the boundary between CLIPPERS and mimics (PCNSL, ECD, GFAP astrocytopathy, MOGAD, PACNS) is imperfect, and some "CLIPPERS" cases are misclassified lymphoma or vasculitis.
3. **Mechanism largely inferred.** The link from HLH-gene loss of function → impaired cytotoxicity → perivascular T-cell inflammation is biologically plausible but not experimentally demonstrated in CLIPPERS tissue.
4. **Genetic penetrance/frequency unknown.** How often HLH-gene carriers develop CLIPPERS, and the population frequency of the relevant variants in CLIPPERS patients, are not quantified.
5. **B-cell vs T-cell heterogeneity.** Some series report CD20+ B-cell-dominant infiltrates ([PMID: 33498046](https://pubmed.ncbi.nlm.nih.gov/33498046/)), challenging the "CD4+ T-cell" canonical model.
6. **No animal model** reproduces the pontine salt-and-pepper phenotype, limiting mechanistic and therapeutic research.
7. **Pediatric vs adult disease** may be biologically distinct entities ([PMID: 30146710](https://pubmed.ncbi.nlm.nih.gov/30146710/)).

---

## Proposed Follow-up Experiments / Actions

1. **Systematic HLH-gene sequencing in all new CLIPPERS cases** (adult and pediatric) with functional degranulation assays (perforin expression, CD107a mobilization) to quantify the genetic subgroup and confirm loss of function.
2. **Prospective CSF ctDNA and T-cell-receptor clonality studies** at diagnosis and relapse to systematically detect occult lymphoma and refine the paraneoplastic fraction.
3. **International CLIPPERS registry** with standardized 2017-criteria phenotyping, MRI, biopsy, genetics, and longitudinal EDSS to generate the first prevalence/incidence estimates and natural-history data.
4. **Comparative immunohistochemistry meta-analysis** to resolve the CD4+ T-cell vs CD20+ B-cell heterogeneity and its clinical/prognostic correlates.
5. **Head-to-head observational comparison of steroid-sparing agents** (methotrexate vs MMF vs rituximab) for relapse prevention and atrophy protection.
6. **Develop a conditional/hypomorphic HLH-gene mouse challenged with an EBV-analogue (MHV-68) or antigenic stimulation** to test whether cytotoxic-clearance failure can generate perivascular hindbrain inflammation.
7. **Standardized malignancy-surveillance protocol** (whole-body PET/CT, hematologic workup) for CLIPPERS patients given the ~16% malignancy association.

---

*Report compiled from 13 confirmed findings and 37 reviewed papers over 5 investigation iterations. Ontology suggestions: MONDO:0017297; HPO terms per Section 3; GO:0006954, GO:0002250, GO:0045055; CL:0000624, CL:0000625, CL:0000236; UBERON:0000988, 0002037, 0001896, 0001891, 0002240; NCIT terms per Section 12.*


## Artifacts

- [OpenScientist final report](Chronic_Lymphocytic_Inflammation_With_Pontine_Perivascular_Enhancement_Responsive_To_Steroids-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Chronic_Lymphocytic_Inflammation_With_Pontine_Perivascular_Enhancement_Responsive_To_Steroids-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 25 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 8 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0002240` (2 mentions) - the report calls it "Secondary/extension:** cervical & thoracic spinal cord"; UBERON calls it **spinal cord**
- `HP:0000651` (1 mention) - the report calls it "Common; sometimes predominant"; HP calls it **Diplopia**
- `HP:0001260` (1 mention) - the report calls it "Common"; HP calls it **Dysarthria**
- `HP:0003401` (1 mention) - the report calls it "Common; early"; HP calls it **Paresthesia**
- `HP:0000639` (1 mention) - the report calls it "Frequent"; HP calls it **Nystagmus**
- `HP:0002015` (1 mention) - the report calls it "Occasional"; HP calls it **Dysphagia**
- `HP:0100543` (1 mention) - the report calls it "Occasional"; HP calls it **Cognitive impairment**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0000988` (3 mentions) - the report calls it "Primary:** pons"; UBERON calls it **pons**