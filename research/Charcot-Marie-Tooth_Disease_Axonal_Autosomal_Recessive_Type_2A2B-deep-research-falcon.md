---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-09T11:34:30.318287'
end_time: '2026-09-09T11:46:20.905536'
duration_seconds: 710.59
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Charcot-Marie-Tooth Disease, Axonal, Autosomal Recessive, Type 2A2B
  mondo_id: MONDO:0014906
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 26
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 60
  verified: 58
  not_found: 1
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.017
  labels_checked: 7
  labels_matching: 0
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: MONDO:0014906
    reported_labels:
    - if available
    - MONDO
    - Subtype-specific disease-resource mapping and human recessive cases
    ontology_label: Charcot-Marie-Tooth disease, axonal, autosomal recessive, type
      2a2b;
  - term_id: HP:0003202
    reported_labels:
    - Core sign; broader MFN2 cohort 72/75 (96%)
    ontology_label: Skeletal muscle atrophy
  - term_id: HP:0001761
    reported_labels:
    - Common secondary musculoskeletal manifestation
    ontology_label: Pes cavus
  - term_id: HP:0000648
    reported_labels:
    - Recognized but nonuniform MFN2-spectrum complication
    ontology_label: Optic atrophy
  - term_id: HP:0003477
    reported_labels:
    - Electrophysiologic/pathologic phenotype
    ontology_label: Peripheral axonal neuropathy
  - term_id: HP:0001270
    reported_labels:
    - Especially severe early-onset disease
    ontology_label: Motor delay
  - term_id: HP:0000365
    reported_labels:
    - Occasional broader-spectrum feature
    ontology_label: Hearing impairment
  unresolved_terms:
  - HP:0001768
  obsolete_terms:
  - term_id: HP:0002355
    ontology_label: obsolete Difficulty walking
    replaced_by: HP:0001288
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Charcot-Marie-Tooth_Disease_Axonal_Autosomal_Recessive_Type_2A2B-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Charcot-Marie-Tooth Disease, Axonal, Autosomal Recessive, Type 2A2B
- **MONDO ID:** MONDO:0014906 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth Disease, Axonal, Autosomal Recessive, Type 2A2B** covering all of the
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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Charcot-Marie-Tooth Disease, Axonal, Autosomal Recessive, Type 2A2B
- **MONDO ID:** MONDO:0014906 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth Disease, Axonal, Autosomal Recessive, Type 2A2B** covering all of the
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


# Research report: Charcot–Marie–Tooth disease, axonal, autosomal recessive, type 2A2B

**Disease:** Charcot–Marie–Tooth disease, axonal, autosomal recessive, type 2A2B (CMT2A2B)  
**MONDO:** [MONDO:0014906](https://monarchinitiative.org/disease/MONDO:0014906)  
**Category:** Mendelian peripheral neuropathy  
**Evidence cutoff:** emphasis on literature available through 2024

## Executive summary and evidence boundary

CMT2A2B is an exceptionally rare, autosomal-recessive, usually early-onset axonal sensorimotor neuropathy caused by **biallelic germline pathogenic variants in MFN2**, encoding mitofusin-2. It is best regarded as the recessive part of the MFN2-neuropathy spectrum and should not be conflated with CMT2A2A, the much more common dominant/de-novo MFN2 disorder. Open Targets directly maps MONDO:0014906 to MFN2, with a strong disease–target score (0.811); its weak MPZ association appears to reflect nonspecific CMT evidence rather than an established second cause of CMT2A2B. (OpenTargets Search: Charcot-Marie-Tooth disease type 2A2B-MFN2)

The evidence base is small: mostly individual families, one or a few biallelic cases embedded in broader MFN2 cohorts, and mechanistic studies dominated by heterozygous variants such as p.Arg94Gln. Consequently, subtype-specific prevalence, penetrance, survival, quality-of-life, biomarker, and treatment-response estimates do not exist. Findings extrapolated from broader MFN2-CMT2A are labeled accordingly. (abati2024charcot–marie‐toothtype2a pages 1-2, abati2024charcot–marie‐toothtype2a pages 10-11)

The following table provides a compact knowledge-base summary.

| Knowledge-base field | Summary | Evidence scope | Ontology suggestions | Evidence |
|---|---|---|---|---|
| Identity / identifier | Charcot–Marie–Tooth disease, axonal, autosomal recessive, type 2A2B (CMT2A2B); **MONDO:0014906**. It is the biallelic/recessive portion of the MFN2-related CMT2A spectrum and should not be conflated with predominantly dominant CMT2A2A. | Subtype-specific disease-resource mapping and human recessive cases | MONDO:0014906 | (OpenTargets Search: Charcot-Marie-Tooth disease type 2A2B-MFN2, asif2023homozygousmutationsin pages 1-2, abati2024charcot–marie‐toothtype2a pages 10-11) |
| Causal gene / inheritance | **MFN2** (mitofusin 2); germline biallelic pathogenic variants cause autosomal-recessive disease. Compound-heterozygous and homozygous families are reported; heterozygous MFN2 disease is usually classified separately as dominant CMT2A2A. | Subtype-specific human genetic evidence | MFN2; autosomal recessive inheritance (HP:0000007) | (ando2017clinicalandgenetic pages 6-9, asif2023homozygousmutationsin pages 1-2, abati2024charcot–marie‐toothtype2a pages 10-11) |
| Core phenotype | Length-dependent motor and sensory peripheral neuropathy with distal lower-limb weakness and wasting, foot deformity/foot drop, gait impairment, depressed reflexes, and sensory loss; severe cases may develop proximal or upper-limb involvement. Optic atrophy, vocal-cord dysfunction, dysphagia, spasticity, and respiratory/diaphragmatic weakness occur in parts of the wider MFN2 spectrum but are not established as uniformly characteristic of CMT2A2B. | Core pattern supported by recessive families; frequencies and uncommon features mainly from broader MFN2-CMT2A cohorts | HP:0009830 distal muscle weakness; HP:0003202 muscle atrophy; HP:0001761 pes cavus; HP:0001284 areflexia; HP:0000763 sensory neuropathy; HP:0000648 optic atrophy | (ando2017clinicalandgenetic pages 4-6, ando2017clinicalandgenetic pages 6-9, asif2023homozygousmutationsin pages 1-2, ando2017clinicalandgenetic pages 1-4) |
| Onset / course | Usually chronic and progressive; biallelic disease is often early-onset and severe, although expressivity is variable. Across a broader MFN2 cohort, mean onset was **12 ± 14 years** (range 0–59); this statistic must not be assigned directly to CMT2A2B. | Early severity supported by biallelic cases; numeric estimate is broader-spectrum evidence | HP:0003593 infantile onset; HP:0011463 childhood onset; HP:0003676 progressive disorder | (ando2017clinicalandgenetic pages 4-6, ando2017clinicalandgenetic pages 6-9, abati2024charcot–marie‐toothtype2a pages 1-2, ando2017clinicalandgenetic pages 1-4) |
| Diagnostic signature | Clinical examination plus nerve-conduction studies/EMG showing a predominantly axonal sensorimotor neuropathy, followed by identification of pathogenic/likely pathogenic **MFN2 variants in trans**. Some MFN2 cases have intermediate or reduced velocities, so a strict conduction-velocity threshold cannot exclude the diagnosis. Parental testing establishes phase; broad neuropathy panels, exome, or genome sequencing help detect dual diagnoses and copy-number or noncoding variants. | Human subtype and broader CMT diagnostic evidence | HP:0003477 peripheral axonal neuropathy; NCIT:C15709 genetic testing; NCIT:C16809 electromyography | (ando2017clinicalandgenetic pages 6-9, asif2023homozygousmutationsin pages 1-2, ando2017clinicalandgenetic pages 9-12, ando2017clinicalandgenetic pages 1-4) |
| Mechanism | Dysfunctional MFN2 perturbs outer-mitochondrial-membrane fusion, mitochondrial distribution/axonal transport, mitophagy, and mitochondria–ER contacts; altered calcium handling and ER stress then promote distal axonal degeneration. Whether individual biallelic alleles act through loss of function, altered conformation, or combined functional insufficiency is variant-dependent and incompletely resolved. | Mechanistic chain is inferred mainly from dominant MFN2 patient cells and CMT2A models, not demonstrated comprehensively in CMT2A2B | GO:0008053 mitochondrial fusion; GO:0047497 mitochondrial transport along microtubule; GO:0000423 mitophagy; GO:0034976 response to ER stress; GO:0090394 negative regulation of axon extension | (bernardmarissal2019alteredinterplaybetween pages 1-2, abati2024charcot–marie‐toothtype2a pages 1-2, larrea2019mfn2mutationsin pages 3-4, larrea2019mfn2mutationsin pages 1-2) |
| Management | No approved disease-modifying therapy. Multidisciplinary supportive care includes PT/OT, stretching and appropriately dosed exercise, ankle–foot orthoses or mobility aids, orthopedic evaluation for deformity/scoliosis, pain and fall management, and assessment of vision, hearing, swallowing, vocal-cord, and respiratory function when clinically indicated. | Standard CMT/MFN2-spectrum practice; no CMT2A2B-specific comparative trials | NCIT:C15329 physical therapy; NCIT:C15714 occupational therapy; NCIT:C150575 orthotic device; NCIT:C17173 supportive care | (abati2024charcot–marie‐toothtype2a pages 1-2, rudnikschoneborn2020charcotmarietoothdiseaseand pages 1-2, estevezarias2022geneticapproachesand pages 16-17) |
| Experimental therapies | Preclinical approaches include allosteric mitofusin agonists, MFN1 augmentation, ER-stress/MAM modulation, HDAC6 inhibition, and combined mutant-MFN2 RNA interference plus wild-type MFN2 replacement. Rescue has been reported in cells and animal models, but efficacy and safety in humans—and relevance to recessive loss-of-function disease—remain unproven. | Broader MFN2-CMT2A preclinical evidence only | NCIT:C16558 gene therapy; NCIT:C62795 RNA interference; NCIT:C1909 small-molecule therapeutic agent | (bernardmarissal2019alteredinterplaybetween pages 1-2, abati2024invivoand pages 111-114, abati2024charcot–marie‐toothtype2a pages 12-12) |
| Epidemiology | Subtype-specific prevalence, incidence, carrier frequency, sex ratio, and geographic distribution are unknown. CMT overall is often estimated at about **1 in 2,500**, while MFN2 variants accounted for **63/801 (8%)** axonal CMT cases in one Japanese referral cohort; neither figure estimates CMT2A2B prevalence. Consanguinity increases the probability of homozygous recessive disease. | No population-based CMT2A2B estimate; broader CMT/MFN2 referral data only | Orphan rare genetic neuropathy; no additional subtype epidemiology identifier asserted | (ando2017clinicalandgenetic pages 4-6, asif2023homozygousmutationsin pages 1-2, rudnikschoneborn2020charcotmarietoothdiseaseand pages 1-2) |
| Major evidence gaps | No robust subtype-specific natural-history cohort, penetrance estimate, validated genotype–phenotype model, survival or quality-of-life statistics, biomarker, omics signature, treatment-response rate, or interventional trial. Most mechanistic and therapeutic evidence derives from heterozygous R94Q or other dominant models and requires validation in biallelic patient-derived neurons and allele-specific models. | Explicit knowledge gaps | Evidence should be tagged as human case report, broader-spectrum cohort, in vitro, or model-organism inference | (abati2024charcot–marie‐toothtype2a pages 2-3, abati2024charcot–marie‐toothtype2a pages 1-2, abati2024charcot–marie‐toothtype2a pages 10-11) |


*Table: Compact summary of disease identity, phenotype, genetics, mechanism, diagnosis, management, epidemiology, and research gaps. It distinguishes direct CMT2A2B evidence from findings extrapolated from the broader MFN2-related CMT2A spectrum.*

## 1. Disease information

### Definition and nomenclature

CMT2A2B is a hereditary motor-and-sensory peripheral neuropathy in which biallelic MFN2 dysfunction principally injures long peripheral axons. Typical manifestations are progressive distal weakness and wasting, foot deformity, impaired gait, reduced reflexes, and sensory loss; unusually severe disease can begin in infancy or childhood and extend proximally. (ando2017clinicalandgenetic pages 4-6, ando2017clinicalandgenetic pages 6-9, asif2023homozygousmutationsin pages 1-2)

**Preferred and alternative names** include:

- Charcot–Marie–Tooth disease, axonal, autosomal recessive, type 2A2B
- CMT2A2B; AR-CMT2A
- Autosomal-recessive MFN2-related Charcot–Marie–Tooth disease
- Recessive MFN2-related axonal neuropathy
- Historical reports may simply say “recessive CMT2A,” “CMT2A,” or “hereditary motor and sensory neuropathy type II.” These labels are ambiguous because most CMT2A is dominant.

**Identifiers.** MONDO:0014906 is directly supported. MFN2-related CMT2A is commonly associated with **OMIM phenotype 609260**, although database subdivision into dominant 2A2A and recessive 2A2B is not uniform. No uniquely specific ICD-10-CM, ICD-11, or MeSH code separates CMT2A2B: coding normally uses the broader hereditary motor-and-sensory neuropathy/Charcot–Marie–Tooth category. Exact Orphanet and subtype-specific SNOMED identifiers were not established in the retrieved evidence and should not be inferred.

This report synthesizes **aggregated disease-resource, published family/cohort, human-cell, and model-organism evidence**, not individual EHR data. Open Targets records five MFN2 evidence items and cites PMIDs 15064763, 18458227, 19889647, 20350294, 24604904, and 27604308 across the wider MFN2 association. (OpenTargets Search: Charcot-Marie-Tooth disease type 2A2B-MFN2)

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factor

The initiating cause is biallelic pathogenic or likely pathogenic **MFN2** variation inherited in trans. Both homozygous and compound-heterozygous disease have been reported. A 2023 study of a consanguineous Pakistani family identified homozygous MFN2 **c.334G>A** in four affected relatives and reported autosomal-recessive segregation; WES was followed by Sanger confirmation. (asif2023homozygousmutationsin pages 1-2)

A Japanese cohort documented compound heterozygosity **p.Arg280His/p.Arg250Trp**, with earlier disease than observed with heterozygous p.Arg280His. Other literature summarized in that cohort included p.Arg250Trp in trans with a truncating p.Arg400Ter allele. These observations support a dosage/genetic-burden model, but effects remain allele-specific. (ando2017clinicalandgenetic pages 6-9, ando2017clinicalandgenetic pages 9-12)

### Risk factors

- **Genetic:** two disease-causing MFN2 alleles; parental consanguinity; family history compatible with recessive inheritance. Coincident pathogenic variants in another neuropathy gene may modify the phenotype: a Japanese patient carrying MFN2 p.Thr105Met and PMP22 p.Arg159Cys had an unusually early and complex presentation. (ando2017clinicalandgenetic pages 9-12)
- **Age and sex:** age affects clinical expression because disease is progressive, but neither age nor sex causes the disorder. No reliable sex-ratio difference is known.
- **Environmental/infectious:** no toxin, infection, diet, smoking pattern, occupation, or lifestyle exposure is established as a cause or susceptibility factor for CMT2A2B.

### Protective factors and gene–environment interaction

No validated protective MFN2 allele, modifier allele, dietary factor, drug, or exposure has been identified. MFN1 abundance can rescue MFN2-mutant phenotypes experimentally, making the **MFN1:MFN2 balance** a plausible biological modifier, but not a clinically validated human protective factor. Experimental findings also imply that metabolic stress or neurotoxic exposure could worsen vulnerable axons, yet no CMT2A2B-specific gene–environment interaction has been demonstrated. (abati2024charcot–marie‐toothtype2a pages 1-2, abati2024charcot–marie‐toothtype2a pages 12-12)

## 3. Phenotypes

Because there is no sufficiently large CMT2A2B cohort, frequencies below are either qualitative or explicitly drawn from the broader MFN2 spectrum.

| Phenotype | Type and characteristics | Suggested HPO term |
|---|---|---|
| Distal lower-limb weakness | Core clinical sign; usually early, bilateral, progressive; may spread to proximal legs and hands | HP:0009053 / HP:0009830 |
| Distal muscle wasting | Core sign; broader MFN2 cohort 72/75 (96%) | HP:0003202 |
| Hyporeflexia/areflexia | Core sign; broader cohort 60/61 (98%) | HP:0001265 / HP:0001284 |
| Foot drop, steppage gait, running difficulty | Common functional manifestation | HP:0003376; HP:0001768; HP:0002355 |
| Pes cavus/foot deformity | Common secondary musculoskeletal manifestation | HP:0001761 |
| Sensory loss | Variable; vibration particularly affected; broader cohort 33/54 (61%) | HP:0000763; HP:0003648 |
| Axonal sensorimotor neuropathy | Electrophysiologic/pathologic phenotype | HP:0003477 |
| Delayed motor milestones | Especially severe early-onset disease | HP:0001270 |
| Optic atrophy/visual loss | Recognized but nonuniform MFN2-spectrum complication | HP:0000648 |
| Vocal-cord paresis, dysphagia, tongue atrophy | Rare complex-spectrum manifestations | HP:0001605; HP:0002015; HP:0000223 |
| Spasticity/pyramidal signs | Rare; may indicate central involvement or dual diagnosis | HP:0001257; HP:0003487 |
| Hearing loss | Occasional broader-spectrum feature | HP:0000365 |
| Diaphragmatic/respiratory weakness | Rare but clinically important in severe recessive reports | HP:0009113; HP:0002791 |
| Scoliosis/contractures | Secondary to chronic weakness and imbalance | HP:0002650; HP:0001371 |

In the 2017 Japanese MFN2 series, distal weakness, atrophy, and hyporeflexia occurred in 99%, 96%, and 98%, respectively; these are **not CMT2A2B-specific frequencies**. The cohort also associated optic atrophy with p.Arg104Trp, p.Arg104Leu, and p.Arg364Trp; vocal-cord paralysis with p.Arg364Trp; spasticity with p.Leu710Pro; and dysphagia/tongue atrophy with p.Ala220Thr. (ando2017clinicalandgenetic pages 4-6, ando2017clinicalandgenetic pages 6-9)

**Quality of life.** Weakness, falls, foot deformity, fatigue, sensory impairment, and loss of ambulation can impair schooling, employment, self-care, mobility, and social participation. Visual, bulbar, or respiratory involvement adds major burden. No EQ-5D, SF-36, PROMIS, or CMT-specific quality-of-life statistics have been published specifically for CMT2A2B.

## 4. Genetic and molecular information

### Gene and protein

- **Gene:** MFN2, mitofusin 2; Ensembl ENSG00000116688. (OpenTargets Search: Charcot-Marie-Tooth disease type 2A2B-MFN2)
- **Product:** a dynamin-family GTPase located mainly in the outer mitochondrial membrane and also associated with endoplasmic-reticulum/mitochondrial contact regions.
- **Origin:** germline, not somatic.
- **Inheritance:** biallelic pathogenic variants in CMT2A2B; heterozygous dominant/de-novo variants generally belong to CMT2A2A.

### Variant classes and interpretation

Documented MFN2 disease alleles include missense, nonsense, frameshift, in-frame deletion, and insertion variants. Missense changes in or near the GTPase and helical domains predominate in the broader spectrum. Variant effect cannot be inferred from class alone: different substitutions may impair fusion, conformational switching, transport, mitophagy, or organelle tethering, and some produce gain-, loss-, or dominant-negative behavior. (ando2017clinicalandgenetic pages 9-12, abati2024charcot–marie‐toothtype2a pages 1-2)

For a CMT2A2B diagnosis, both variants should be classified independently under ACMG/AMP criteria and shown to be **in trans**. Population-frequency thresholds must be evaluated against gnomAD ancestry-specific data at the time of interpretation; the retrieved studies do not provide stable gnomAD frequencies for all reported recessive alleles. A variant absent or rare in controls is not pathogenic by itself. The Japanese study classified p.Lys109Arg as pathogenic after confirming de-novo occurrence and absence from control databases and classified 14 additional variants as likely pathogenic; these examples concern the broader MFN2 spectrum. (ando2017clinicalandgenetic pages 6-9, ando2017clinicalandgenetic pages 9-12)

**Modifier genes:** MFN1 is a strong experimental modifier; coincident PMP22 variation may increase burden. No validated clinical modifier panel exists. **Epigenetics:** no reproducible CMT2A2B-specific DNA-methylation, histone, or chromatin signature is known. **Chromosomal abnormalities:** no recurrent aneuploidy, translocation, or inversion defines this disease; rare MFN2 copy-number changes can be detected by appropriately designed sequencing assays, but biallelic CNV disease is not well characterized. (ando2017clinicalandgenetic pages 9-12, abati2024charcot–marie‐toothtype2a pages 12-12)

## 5. Environmental information

CMT2A2B is not infectious, toxic, radiation-induced, or lifestyle-caused. There is no evidence for zoonotic transmission. Clinically, avoidable secondary insults—diabetes, nutritional deficiency, alcohol misuse, compressive injury, and known neurotoxic medications—may add to neuropathy burden, but this is general neurologic prudence rather than a demonstrated CMT2A2B interaction. Exercise should be individualized to preserve conditioning without overuse injury.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic pathogenic MFN2 variants lead to** quantitatively or qualitatively deficient mitofusin-2 function in neurons.
2. **Abnormal MFN2 leads to** impaired outer-mitochondrial-membrane fusion and/or abnormal MFN2 conformational/GTPase cycling; the exact defect is variant-dependent.
3. **This leads to** abnormal mitochondrial morphology, clustering, quality control, and mitophagy, with impaired interaction with mitochondrial transport machinery. (abati2024charcot–marie‐toothtype2a pages 2-3, abati2024charcot–marie‐toothtype2a pages 1-2)
4. **In parallel, altered MFN2 leads to** disrupted mitochondria–ER contact sites, abnormal calcium handling, and ER stress; this branch is demonstrated in broader MFN2-CMT2A models but remains inferred for most biallelic alleles. (bernardmarissal2019alteredinterplaybetween pages 1-2, larrea2019mfn2mutationsin pages 3-4)
5. **Fusion/transport/contact-site defects lead to** deficient delivery and positioning of healthy mitochondria along long motor and sensory axons, particularly at distal terminals.
6. **Distal energetic, calcium, and organelle-quality-control failure results in** length-dependent axonal dysfunction and “dying-back” degeneration, often without initial neuronal-cell-body death. (bernardmarissal2019alteredinterplaybetween pages 1-2)
7. **Axon loss leads to** denervation, reduced compound action-potential amplitudes, muscle wasting, weakness, sensory loss, areflexia, foot deformity, and gait disability.
8. **Branch—optic, bulbar, respiratory, or corticospinal involvement leads to** visual loss, vocal-cord/dysphagic symptoms, ventilatory weakness, or spasticity in selected severe genotypes; why these tissues are variably involved remains unresolved. (ando2017clinicalandgenetic pages 6-9)

### Pathways, processes, and ontology suggestions

Relevant processes include mitochondrial fusion (**GO:0008053**), mitochondrial organization (**GO:0007005**), mitochondrial transport along microtubules (**GO:0047497**), mitophagy (**GO:0000423**), calcium-ion homeostasis (**GO:0055074**), response to ER stress (**GO:0034976**), axon maintenance (**GO:0048679**), and regulation of autophagy (**GO:0010506**). Relevant compartments are outer mitochondrial membrane (**GO:0005741**), mitochondrion (**GO:0005739**), axon (**GO:0030424**), ER membrane (**GO:0005789**), and mitochondria-associated ER membrane/contact site.

Primary vulnerable cells are peripheral motor neurons (**CL:0000100**, motor neuron), peripheral sensory neurons (**CL:0000101**, sensory neuron), especially long dorsal-root-ganglion projections, retinal ganglion cells (**CL:0000740**) when optic atrophy occurs, and secondarily denervated skeletal myocytes (**CL:0000188**). Schwann cells are not thought to be the initiating lesion, although secondary axon–glia effects are plausible.

Human fibroblast studies found altered MAM function correlated with clinical severity but preserved respiratory-chain function, arguing that CMT2A should not automatically be labeled a primary oxidative-phosphorylation deficiency. (larrea2019mfn2mutationsin pages 3-4, larrea2019mfn2mutationsin pages 1-2)

### Molecular profiling and advanced technologies

Patient fibroblast transcriptomics reported altered proliferation/extracellular-matrix pathways and mTORC2–AKT activation, but this came from heterozygous MFN2 disease and is not a validated diagnostic signature. Patient-derived iPSC motor and sensory neurons reproduce mitochondrial-distribution and transport defects. No validated CMT2A2B single-cell atlas, spatial transcriptomic map, proteomic biomarker, metabolomic/lipidomic signature, or multi-omics classifier exists. (abati2024charcot–marie‐toothtype2a pages 2-3, abati2024charcot–marie‐toothtype2a pages 10-11)

## 7. Anatomical structures affected

- **Primary system:** peripheral nervous system; long motor and sensory axons in peripheral nerves.
- **Anatomic sites:** peripheral nerve (**UBERON:0001021**), spinal nerve, ventral spinal root, dorsal-root ganglion (**UBERON:0000044**), neuromuscular junction (**UBERON:0002204**), distal limb musculature, foot and ankle.
- **Secondary tissues:** denervated skeletal muscle (**UBERON:0001134**), tendons/joints and spine through imbalance and contracture.
- **Occasional extended sites:** optic nerve (**UBERON:0000962**) and retinal ganglion-cell axons; corticospinal pathways; recurrent laryngeal/vagal motor structures; diaphragm.
- **Localization:** typically bilateral and length-dependent, beginning in the feet/legs and later involving hands. Clinical asymmetry should prompt evaluation for superimposed entrapment, orthopedic disease, or another neuropathy.
- **Subcellular sites:** outer mitochondrial membrane, mitochondrial network, axonal microtubule-transport apparatus, ER, and mitochondria–ER contacts. (ando2017clinicalandgenetic pages 6-9, bernardmarissal2019alteredinterplaybetween pages 1-2)

## 8. Temporal development

CMT2A2B usually has insidious infantile or childhood onset, although the limited reports prevent a precise distribution. Severe biallelic disease may progress rapidly early in life; other MFN2 disease is slowly progressive. Across all MFN2 genotypes in the Japanese cohort, mean onset was **12 ± 14 years** (range 0–59), and sporadic cases began earlier than familial dominant cases (7.6 ± 10 versus 15 ± 16 years); these values must not be assigned directly to recessive CMT2A2B. (ando2017clinicalandgenetic pages 4-6)

A practical, nonvalidated staging framework is: (1) delayed milestones/running difficulty or distal foot weakness; (2) foot drop, pes cavus, falls and sensory loss; (3) hand/proximal involvement and need for orthoses or mobility aids; and (4) severe multisystem disability in selected patients. Disease is lifelong and progressive, without spontaneous remission. No proven critical treatment window exists, although the biology favors intervention before irreversible axon loss.

## 9. Inheritance and population

Inheritance is autosomal recessive (**HP:0000007**). When both parents are confirmed heterozygous carriers of the familial alleles, each pregnancy has a 25% probability of an affected child, 50% probability of a carrier, and 25% probability of inheriting neither allele. Because some MFN2 alleles can have heterozygous effects, apparently unaffected parents should nevertheless receive neurologic examination, segregation analysis, and variant-specific counseling.

Penetrance of established biallelic pathogenic genotypes appears high in reported families, but ascertainment is too small to claim complete penetrance. Expressivity is variable; anticipation is not established. Germline mosaicism has not been shown to be a characteristic mechanism. Consanguinity increases the likelihood of homozygosity and was present in the 2023 Pakistani family. Founder effects and population carrier frequencies are unknown. (asif2023homozygousmutationsin pages 1-2)

**Epidemiology:** CMT overall is often estimated near **1:2,500**, but CMT2A2B is far rarer and has no population-based prevalence or incidence estimate. In one Japanese referral cohort, MFN2 variants explained 63/801 (8%) axonal CMT cases, but only one compound-heterozygous case was identified; this illustrates rarity without providing a population prevalence. No reliable sex ratio, geographic gradient, or ancestry-specific incidence is available. (ando2017clinicalandgenetic pages 4-6, rudnikschoneborn2020charcotmarietoothdiseaseand pages 1-2)

## 10. Diagnostics

### Clinical and electrophysiologic diagnosis

Evaluation should include pedigree, developmental history, neurologic examination, foot/spine assessment, and standardized disability measurement such as CMT Neuropathy Score/CMT Examination Score. Nerve-conduction studies and EMG generally show chronic axonal sensorimotor neuropathy: reduced motor and sensory amplitudes, relatively preserved or mildly/intermediately slowed velocities, denervation, neurogenic motor units, and reduced recruitment. The Pakistani family had motor and sensory velocities below 38 m/s and EMG evidence of denervation, illustrating that strict “axonal” velocity cutoffs can fail. (asif2023homozygousmutationsin pages 1-2)

In the broader Japanese MFN2 cohort, mean median and tibial motor velocities were 51 ± 7.5 and 38 ± 8.2 m/s, respectively. Some MFN2 cases are intermediate or demyelinating; MFN2 should therefore not be excluded solely because velocity is under 38 m/s. (ando2017clinicalandgenetic pages 6-9, ando2017clinicalandgenetic pages 9-12)

Ancillary testing is phenotype-driven: ophthalmologic examination/OCT and visual evoked potentials for visual symptoms; audiology; swallow and laryngoscopic assessment; pulmonary function including sitting/supine forced vital capacity when respiratory or diaphragmatic weakness is suspected; spine/foot radiographs for surgical planning; and MRI when central signs are disproportionate. Nerve biopsy is usually unnecessary after molecular confirmation and would be expected to show axonal loss with secondary myelin changes rather than a pathognomonic lesion.

### Genetic-testing algorithm

1. Confirm a hereditary sensorimotor neuropathy clinically and electrophysiologically.
2. Use a comprehensive inherited-neuropathy panel including **MFN2**, with deletion/duplication calling; in demyelinating presentations, test PMP22 duplication/deletion.
3. If one MFN2 variant is found in suspected recessive disease, search for a second allele using exon-level CNV analysis, genome sequencing, and—where justified—RNA studies for splice effects.
4. Perform parental/relative testing to establish phase and segregation.
5. Reassess both variants under current ACMG/AMP criteria and ancestry-matched population data.
6. If negative, use WES/WGS and periodic reanalysis; consider dual diagnoses. Targeted CMT panels produced a definite diagnosis in 67/220 (30%) cases and a VUS in another 33%; GJB1, MFN2, and MPZ accounted for 39% of confirmed diagnoses. (ando2017clinicalandgenetic pages 9-12, estevezarias2022geneticapproachesand pages 16-17)

CMA, karyotyping, and FISH are not first-line tests for isolated CMT2A2B. Mitochondrial-DNA and repeat-expansion testing are considered only when the phenotype suggests an alternative disorder. RNA-seq is currently a problem-solving assay rather than a routine diagnostic.

### Differential diagnosis

Major alternatives include dominant MFN2-CMT2A2A; PMP22-CMT1A; MPZ, GJB1, GDAP1, SORD, HSPB1, NEFL, DYNC1H1 and other inherited neuropathies; hereditary spastic paraplegia; distal hereditary motor neuropathy; spinal muscular atrophy; Friedreich ataxia; mitochondrial optic neuropathies; CIDP; toxic, nutritional, diabetic, and inflammatory neuropathies. CIDP is more likely with subacute, relapsing, or fluctuating disease, conduction block/temporal dispersion, elevated CSF protein, and treatment response, whereas CMT is usually chronic, symmetric, and accompanied by longstanding foot deformity. (rudnikschoneborn2020charcotmarietoothdiseaseand pages 1-2)

**Screening:** population or newborn screening is not established. Cascade testing of adult relatives is appropriate after molecular confirmation. Predictive testing of minors is most defensible where childhood surveillance or early rehabilitation would alter care.

## 11. Outcome and prognosis

The disorder causes chronic morbidity rather than a predictable acute mortality syndrome. Disability ranges from mild ambulatory neuropathy to severe childhood weakness, loss of independent mobility, deformity, visual impairment, dysphagia, or respiratory weakness. Biallelic disease tends to be earlier and more severe than many heterozygous presentations, but exceptions and allele-specific effects prevent deterministic counseling. (ando2017clinicalandgenetic pages 6-9, abati2024charcot–marie‐toothtype2a pages 1-2)

No CMT2A2B-specific 5- or 10-year survival, mortality rate, life-expectancy estimate, recovery rate, or validated prognostic biomarker exists. Most CMT patients have near-normal lifespan, but this broad statement should be qualified in severe recessive cases with bulbar or respiratory involvement. Function lost through axonal degeneration is usually not spontaneously recovered; rehabilitation, orthoses, and surgery can improve safety and function without reversing the molecular disease.

Potential adverse prognostic indicators are very early onset, rapid milestone loss, proximal weakness, severe axonal amplitude loss, optic/bulbar/respiratory involvement, scoliosis, and two functionally severe alleles. These remain clinical judgments rather than validated CMT2A2B prediction rules.

## 12. Treatment and applications

### Current real-world management

There is no FDA- or EMA-approved disease-modifying therapy for MFN2-CMT2A or specifically CMT2A2B; the 2024 model review states that no “resolutive treatment” is available. Management is multidisciplinary and supportive. (abati2024charcot–marie‐toothtype2a pages 1-2)

- **PT/exercise:** stretching, balance and gait training, low-to-moderate aerobic and strengthening activity, fall prevention, and contracture prevention—**NCIT:C15329, Physical Therapy**.
- **OT:** hand function, school/work adaptation, energy conservation, and adaptive equipment—**NCIT:C15714, Occupational Therapy**.
- **Devices:** ankle–foot orthoses, custom footwear, canes/walkers, and wheelchairs as indicated—orthotic/assistive-device concepts.
- **Orthopedics:** selected tendon transfer, cavovarus reconstruction, Achilles procedures, or scoliosis management after specialist evaluation—**NCIT surgical procedure concepts**.
- **Symptoms:** standard neuropathic-pain medicines when needed; treatment of cramps, musculoskeletal pain, sleep problems, and fatigue. There is no MFN2-specific pharmacogenomic recommendation.
- **Complex disease:** ophthalmology/low-vision services, audiology, speech/swallow therapy, nutrition, laryngology, and respiratory support when indicated.

Evidence for PT, orthoses, and surgery is largely general CMT evidence rather than CMT2A2B trials. (estevezarias2022geneticapproachesand pages 16-17)

### Experimental therapies and 2023–2024 developments

1. **Allosteric mitofusin agonists:** improved mitochondrial fusion/transport and reversed neuromuscular degeneration in mouse CMT2A models; deficits recurred after withdrawal, and even old mice responded. This is preclinical and most directly relevant to conformationally impaired alleles. (mccray2021axonalcharcotmarietoothdisease pages 15-16)
2. **MFN1 augmentation:** rescued neurologic and retinal phenotypes in p.Arg94Gln mice, supporting mitofusin-balance correction. A 2023 retinal study and 2023 in-vitro MFN2 p.Lys357Thr rescue extend this strategy. (abati2024charcot–marie‐toothtype2a pages 12-12)
3. **RNA interference plus gene replacement:** 2023–2024 work combined mutant-MFN2 suppression with wild-type MFN2 replacement. Patient-derived motor-neuron phenotypes improved, but one early mouse experiment showed vector/context-dependent toxicity, emphasizing dosage, promoter, immunogenicity, and off-target risks. (abati2024invivoand pages 111-114, abati2024charcot–marie‐toothtype2a pages 12-12)
4. **MAM/ER-stress modulation:** experimentally strengthened ER–mitochondria contacts or reduced ER stress, restoring mitochondrial morphology and preventing axonal degeneration. (bernardmarissal2019alteredinterplaybetween pages 1-2)
5. **HDAC6 inhibition:** intended to improve tubulin acetylation and axonal transport; evidence remains preclinical. (abati2024charcot–marie‐toothtype2a pages 12-12)

No MFN2/CMT2A2B interventional trial was identified in the ClinicalTrials.gov search, and there are no subtype-specific response rates or adverse-event estimates. Gene-silencing strategies designed for dominant-negative alleles may not translate directly to recessive loss-of-function disease; biallelic CMT2A2B may instead favor carefully dosed gene augmentation, but that remains hypothetical.

## 13. Prevention

**Primary prevention** through lifestyle or vaccination is not applicable to a germline Mendelian disorder. Reproductive prevention options after identifying both familial variants include genetic counseling, carrier testing of partners/relatives, preimplantation genetic testing for monogenic disease, chorionic-villus sampling, amniocentesis, donor gametes, and adoption. Counseling must address uncertain variant interpretation and possible heterozygous manifestations.

**Secondary prevention** consists of cascade diagnosis and early baseline neurologic, orthopedic, visual, bulbar, and respiratory assessment. No population or newborn-screening program is established.

**Tertiary prevention** aims to prevent falls, contractures, ulcers, avoidable deconditioning, scoliosis progression, aspiration, and respiratory complications through rehabilitation, orthoses, foot care, vaccination according to ordinary schedules, weight/metabolic management, and timely assistive ventilation where required. There is no disease-specific chemoprophylaxis.

## 14. Other species and natural disease

No well-established naturally occurring veterinary syndrome specifically equivalent to human biallelic MFN2-CMT2A2B was identified. MFN2 orthologs are highly conserved across vertebrates and invertebrates, supporting comparative modeling, but engineered phenotypes should not be mislabeled as natural disease. The condition has no infectious transmission or zoonotic potential.

Relevant experimental taxa include **Mus musculus** (NCBI Taxon 10090), **Danio rerio** (7955), and **Drosophila melanogaster** (7227; ortholog *marf*). Breed-specific VBO annotations are not applicable based on current evidence.

## 15. Model organisms and experimental systems

- **Mouse:** neuronal transgenic MFN2 p.Arg94Gln models show early visual/neurologic deficits, fragmented mitochondrial accumulation, and axonal degeneration without equivalent cell-body loss. Strengths are mammalian anatomy and treatment testing; limitations include dominant transgene dosage, variant specificity, and incomplete modeling of biallelic human disease. (bernardmarissal2019alteredinterplaybetween pages 1-2, abati2024charcot–marie‐toothtype2a pages 10-11)
- **Zebrafish:** mfn2 depletion reduced 24-hour survival from 90% to 60%, disrupted motor-neuron/NMJ development, and impaired escape behavior. An mfn2 p.Leu285Ter model developed reduced size from day 60, progressive mortality after day 175, and swimming velocity of 12.11 ± 7.55 versus 28 cm/s. Strengths are live developmental imaging and throughput; limitations include morpholino artifacts and species differences. (abati2024charcot–marie‐toothtype2a pages 2-3)
- **Drosophila:** *marf* mutant/knockdown systems show variant-dependent mitochondrial clustering or excessive fusion, locomotor phenotypes, and permit rapid modifier screens. They lack vertebrate myelinated peripheral-nerve anatomy. (abati2024charcot–marie‐toothtype2a pages 1-2)
- **Human fibroblasts:** useful for MAM, calcium, autophagy, and mitochondrial assays, but not axon biology. Some patient fibroblasts showed altered MAM function without respiratory-chain deficiency. (larrea2019mfn2mutationsin pages 1-2)
- **Patient iPSC-derived motor/sensory neurons:** most disease-relevant in-vitro system for axonal transport, allele correction, and gene-therapy testing; maturation and culture length remain limitations. (abati2024charcot–marie‐toothtype2a pages 2-3, abati2024charcot–marie‐toothtype2a pages 10-11)

The highest-priority model gap is an allelic series of **biallelic patient-derived neurons and knock-in animals** that reproduces physiological MFN2 expression. The 2024 expert review stresses that model interpretation depends on mutant-protein dosage, human regulatory context, and the poor current genotype–phenotype correlation. (abati2024charcot–marie‐toothtype2a pages 10-11)

## Key recent and landmark references

- **Asif et al.** “Homozygous Mutations in GDAP1 and MFN2 Genes Resulted in Autosomal Recessive Forms of Charcot–Marie–Tooth Disease in Consanguineous Pakistani Families.” *DNA and Cell Biology*, published November 2023. DOI/URL: https://doi.org/10.1089/dna.2023.0169. Abstract-level conclusion: WES/Sanger analysis identified an MFN2 c.334G>A variant segregating with recessive CMT in a consanguineous family. (asif2023homozygousmutationsin pages 1-2)
- **Abati et al.** “Charcot–Marie-Tooth Type 2A In Vivo Models: Current Updates.” *Journal of Cellular and Molecular Medicine*, published May 2024. DOI/URL: https://doi.org/10.1111/jcmm.18293. The review summarizes fusion/fission, mitophagy, axonal-transport and model-validity evidence and states that no curative treatment is available. (abati2024charcot–marie‐toothtype2a pages 2-3, abati2024charcot–marie‐toothtype2a pages 1-2)
- **Ando et al.** “Clinical and genetic diversities of Charcot-Marie-Tooth disease with MFN2 mutations in a large case study.” *Journal of the Peripheral Nervous System* 22:191–199, published July 2017. DOI/URL: https://doi.org/10.1111/jns.12228. In 1,334 suspected CMT cases, 79 carried pathogenic/likely pathogenic MFN2 variants, including one compound-heterozygous patient. (ando2017clinicalandgenetic pages 4-6, ando2017clinicalandgenetic pages 6-9)
- **Bernard-Marissal et al.** “Altered interplay between endoplasmic reticulum and mitochondria in Charcot–Marie–Tooth type 2A neuropathy.” *PNAS* 116:2328–2337, published January 2019. DOI/URL: https://doi.org/10.1073/pnas.1810932116. The abstract reports that mutant MFN2 produced reduced ER–mitochondrial contacts, ER stress, calcium-handling defects, altered mitochondrial transport, and distal axonal degeneration. (bernardmarissal2019alteredinterplaybetween pages 1-2)
- **Larrea et al.** “MFN2 mutations in Charcot–Marie–Tooth disease alter mitochondria-associated ER membrane function but do not impair bioenergetics.” *Human Molecular Genetics* 28:1782–1800, published January 2019. DOI/URL: https://doi.org/10.1093/hmg/ddz008. The authors’ central abstract conclusion is that MFN2-CMT2A is a MAM-related disorder but not necessarily a respiratory-chain-deficiency disease. (larrea2019mfn2mutationsin pages 1-2)
- **Polke et al.** “Recessive axonal Charcot-Marie-Tooth disease due to compound heterozygous mitofusin 2 mutations.” *Neurology* 77:168–173, published July 2011. DOI/URL: https://doi.org/10.1212/WNL.0b013e3182242d4d. This is a foundational report for recessive/compound-heterozygous MFN2 disease. (abati2024charcot–marie‐toothtype2a pages 10-11)

## Knowledge gaps requiring explicit database flags

No reliable CMT2A2B-specific data are currently available for incidence, population prevalence, carrier frequency, sex ratio, penetrance, survival, life expectancy, quantitative quality of life, validated biomarkers, epigenomics, single-cell/spatial profiling, natural veterinary disease, treatment-response rate, or clinical-trial efficacy. Most molecular work uses dominant MFN2 variants; applying it to biallelic disease is biologically plausible but inferential. Future studies should prioritize international case aggregation, allele-specific functional assays, longitudinal CMT outcome measures, patient-derived axonal models, and genotype-appropriate gene-augmentation studies. (abati2024charcot–marie‐toothtype2a pages 2-3, abati2024charcot–marie‐toothtype2a pages 1-2, abati2024charcot–marie‐toothtype2a pages 10-11)

References

1. (OpenTargets Search: Charcot-Marie-Tooth disease type 2A2B-MFN2): Open Targets Query (Charcot-Marie-Tooth disease type 2A2B-MFN2, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (abati2024charcot–marie‐toothtype2a pages 1-2): Elena Abati, Mafalda Rizzuti, Alessia Anastasia, Giacomo Pietro Comi, Stefania Corti, and Federica Rizzo. Charcot–marie‐tooth type 2a in vivo models: current updates. Journal of Cellular and Molecular Medicine, May 2024. URL: https://doi.org/10.1111/jcmm.18293, doi:10.1111/jcmm.18293. This article has 8 citations and is from a peer-reviewed journal.

3. (abati2024charcot–marie‐toothtype2a pages 10-11): Elena Abati, Mafalda Rizzuti, Alessia Anastasia, Giacomo Pietro Comi, Stefania Corti, and Federica Rizzo. Charcot–marie‐tooth type 2a in vivo models: current updates. Journal of Cellular and Molecular Medicine, May 2024. URL: https://doi.org/10.1111/jcmm.18293, doi:10.1111/jcmm.18293. This article has 8 citations and is from a peer-reviewed journal.

4. (asif2023homozygousmutationsin pages 1-2): Muhammad Asif, Chien-Chun Chiou, Malik Fiaz Hussain, Manzoor Hussain, Zureesha Sajid, Muhammad Gulsher, Afifa Raheem, Adil Khan, Nasreen Nasreen, Andrzej Kloczkowski, Mubashir Hassan, Furhan Iqbal, and Chien-Chin Chen. Homozygous mutations in <i>gdap1</i> and <i>mfn2</i> genes resulted in autosomal recessive forms of charcot–marie–tooth disease in consanguineous pakistani families. Nov 2023. URL: https://doi.org/10.1089/dna.2023.0169, doi:10.1089/dna.2023.0169. This article has 3 citations and is from a peer-reviewed journal.

5. (ando2017clinicalandgenetic pages 6-9): Masahiro Ando, Akihiro Hashiguchi, Yuji Okamoto, Akiko Yoshimura, Yu Hiramatsu, Junhui Yuan, Yujiro Higuchi, Jun Mitsui, Hiroyuki Ishiura, Ayako Umemura, Koichi Maruyama, Takeshi Matsushige, Shinichi Morishita, Masanori Nakagawa, Shoji Tsuji, and Hiroshi Takashima. Clinical and genetic diversities of charcot‐marie‐tooth disease with mfn2 mutations in a large case study. Journal of the Peripheral Nervous System, 22:191-199, Jul 2017. URL: https://doi.org/10.1111/jns.12228, doi:10.1111/jns.12228. This article has 50 citations and is from a peer-reviewed journal.

6. (ando2017clinicalandgenetic pages 4-6): Masahiro Ando, Akihiro Hashiguchi, Yuji Okamoto, Akiko Yoshimura, Yu Hiramatsu, Junhui Yuan, Yujiro Higuchi, Jun Mitsui, Hiroyuki Ishiura, Ayako Umemura, Koichi Maruyama, Takeshi Matsushige, Shinichi Morishita, Masanori Nakagawa, Shoji Tsuji, and Hiroshi Takashima. Clinical and genetic diversities of charcot‐marie‐tooth disease with mfn2 mutations in a large case study. Journal of the Peripheral Nervous System, 22:191-199, Jul 2017. URL: https://doi.org/10.1111/jns.12228, doi:10.1111/jns.12228. This article has 50 citations and is from a peer-reviewed journal.

7. (ando2017clinicalandgenetic pages 1-4): Masahiro Ando, Akihiro Hashiguchi, Yuji Okamoto, Akiko Yoshimura, Yu Hiramatsu, Junhui Yuan, Yujiro Higuchi, Jun Mitsui, Hiroyuki Ishiura, Ayako Umemura, Koichi Maruyama, Takeshi Matsushige, Shinichi Morishita, Masanori Nakagawa, Shoji Tsuji, and Hiroshi Takashima. Clinical and genetic diversities of charcot‐marie‐tooth disease with mfn2 mutations in a large case study. Journal of the Peripheral Nervous System, 22:191-199, Jul 2017. URL: https://doi.org/10.1111/jns.12228, doi:10.1111/jns.12228. This article has 50 citations and is from a peer-reviewed journal.

8. (ando2017clinicalandgenetic pages 9-12): Masahiro Ando, Akihiro Hashiguchi, Yuji Okamoto, Akiko Yoshimura, Yu Hiramatsu, Junhui Yuan, Yujiro Higuchi, Jun Mitsui, Hiroyuki Ishiura, Ayako Umemura, Koichi Maruyama, Takeshi Matsushige, Shinichi Morishita, Masanori Nakagawa, Shoji Tsuji, and Hiroshi Takashima. Clinical and genetic diversities of charcot‐marie‐tooth disease with mfn2 mutations in a large case study. Journal of the Peripheral Nervous System, 22:191-199, Jul 2017. URL: https://doi.org/10.1111/jns.12228, doi:10.1111/jns.12228. This article has 50 citations and is from a peer-reviewed journal.

9. (bernardmarissal2019alteredinterplaybetween pages 1-2): Nathalie Bernard-Marissal, Gerben van Hameren, Manisha Juneja, Christophe Pellegrino, Lauri Louhivuori, Luca Bartesaghi, Cylia Rochat, Omar El Mansour, Jean-Jacques Médard, Marie Croisier, Catherine Maclachlan, Olivier Poirot, Per Uhlén, Vincent Timmerman, Nicolas Tricaud, Bernard L. Schneider, and Roman Chrast. Altered interplay between endoplasmic reticulum and mitochondria in charcot–marie–tooth type 2a neuropathy. Proceedings of the National Academy of Sciences, 116:2328-2337, Jan 2019. URL: https://doi.org/10.1073/pnas.1810932116, doi:10.1073/pnas.1810932116. This article has 115 citations and is from a highest quality peer-reviewed journal.

10. (larrea2019mfn2mutationsin pages 3-4): Delfina Larrea, Marta Pera, Adriano Gonnelli, Rubén Quintana–Cabrera, H Orhan Akman, Cristina Guardia-Laguarta, Kevin R Velasco, Estela Area-Gomez, Federica Dal Bello, Diego De Stefani, Rita Horvath, Michael E Shy, Eric A Schon, and Marta Giacomello. Mfn2 mutations in charcot–marie–tooth disease alter mitochondria-associated er membrane function but do not impair bioenergetics. Human Molecular Genetics, 28:1782-1800, Jan 2019. URL: https://doi.org/10.1093/hmg/ddz008, doi:10.1093/hmg/ddz008. This article has 142 citations and is from a domain leading peer-reviewed journal.

11. (larrea2019mfn2mutationsin pages 1-2): Delfina Larrea, Marta Pera, Adriano Gonnelli, Rubén Quintana–Cabrera, H Orhan Akman, Cristina Guardia-Laguarta, Kevin R Velasco, Estela Area-Gomez, Federica Dal Bello, Diego De Stefani, Rita Horvath, Michael E Shy, Eric A Schon, and Marta Giacomello. Mfn2 mutations in charcot–marie–tooth disease alter mitochondria-associated er membrane function but do not impair bioenergetics. Human Molecular Genetics, 28:1782-1800, Jan 2019. URL: https://doi.org/10.1093/hmg/ddz008, doi:10.1093/hmg/ddz008. This article has 142 citations and is from a domain leading peer-reviewed journal.

12. (rudnikschoneborn2020charcotmarietoothdiseaseand pages 1-2): Sabine Rudnik-Schöneborn, Michaela Auer-Grumbach, and Jan Senderek. Charcot-marie-tooth disease and hereditary motor neuropathies – update 2020. Medizinische Genetik, 32:207-219, Sep 2020. URL: https://doi.org/10.1515/medgen-2020-2038, doi:10.1515/medgen-2020-2038. This article has 38 citations.

13. (estevezarias2022geneticapproachesand pages 16-17): Berta Estévez-Arias, Laura Carrera-García, Andrés Nascimento, Lara Cantarero, Janet Hoenicka, and Francesc Palau. Genetic approaches and pathogenic pathways in the clinical management of charcot-marie-tooth disease. Journal of Translational Genetics and Genomics, 6:333-352, Jan 2022. URL: https://doi.org/10.20517/jtgg.2022.04, doi:10.20517/jtgg.2022.04. This article has 13 citations.

14. (abati2024invivoand pages 111-114): E Abati. In vivo and in vitro evaluation of the combination of rna interfering and gene therapy for treating mitofusin2-related diseases. Unknown journal, 2024.

15. (abati2024charcot–marie‐toothtype2a pages 12-12): Elena Abati, Mafalda Rizzuti, Alessia Anastasia, Giacomo Pietro Comi, Stefania Corti, and Federica Rizzo. Charcot–marie‐tooth type 2a in vivo models: current updates. Journal of Cellular and Molecular Medicine, May 2024. URL: https://doi.org/10.1111/jcmm.18293, doi:10.1111/jcmm.18293. This article has 8 citations and is from a peer-reviewed journal.

16. (abati2024charcot–marie‐toothtype2a pages 2-3): Elena Abati, Mafalda Rizzuti, Alessia Anastasia, Giacomo Pietro Comi, Stefania Corti, and Federica Rizzo. Charcot–marie‐tooth type 2a in vivo models: current updates. Journal of Cellular and Molecular Medicine, May 2024. URL: https://doi.org/10.1111/jcmm.18293, doi:10.1111/jcmm.18293. This article has 8 citations and is from a peer-reviewed journal.

17. (mccray2021axonalcharcotmarietoothdisease pages 15-16): Brett A. McCray and Steven S. Scherer. Axonal charcot-marie-tooth disease: from common pathogenic mechanisms to emerging treatment opportunities. Neurotherapeutics, 18:2269-2285, Oct 2021. URL: https://doi.org/10.1007/s13311-021-01099-2, doi:10.1007/s13311-021-01099-2. This article has 94 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Charcot-Marie-Tooth_Disease_Axonal_Autosomal_Recessive_Type_2A2B-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 60 |
| Resolved | 58 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 7 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014906` (9 mentions) - the report calls it "if available", "MONDO", "Subtype-specific disease-resource mapping and human recessive cases"; MONDO calls it **Charcot-Marie-Tooth disease, axonal, autosomal recessive, type 2a2b;**
- `HP:0003202` (2 mentions) - the report calls it "Core sign; broader MFN2 cohort 72/75 (96%)"; HP calls it **Skeletal muscle atrophy**
- `HP:0001761` (2 mentions) - the report calls it "Common secondary musculoskeletal manifestation"; HP calls it **Pes cavus**
- `HP:0000648` (2 mentions) - the report calls it "Recognized but nonuniform MFN2-spectrum complication"; HP calls it **Optic atrophy**
- `HP:0003477` (2 mentions) - the report calls it "Electrophysiologic/pathologic phenotype"; HP calls it **Peripheral axonal neuropathy**
- `HP:0001270` (1 mention) - the report calls it "Especially severe early-onset disease"; HP calls it **Motor delay**
- `HP:0000365` (1 mention) - the report calls it "Occasional broader-spectrum feature"; HP calls it **Hearing impairment**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0001768` (1 mention) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0002355` (obsolete Difficulty walking) (1 mention) - replaced by `HP:0001288`

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0014906` - called "if available", "MONDO", "Subtype-specific disease-resource mapping and human recessive cases"
