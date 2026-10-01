---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-01T20:11:50.724881'
end_time: '2026-10-01T20:44:54.753861'
duration_seconds: 1984.03
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Combined Oxidative Phosphorylation Deficiency 35
  mondo_id: MONDO:0054742
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
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 14
  on_topic: 9
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 45
  verified: 41
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 33
  labels_matching: 17
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: HP:0001999
    reported_labels:
    - Physical
    ontology_label: Abnormal facial shape
  - term_id: HP:0001252
    reported_labels:
    - Sign
    ontology_label: Hypotonia
  - term_id: HP:0001508
    reported_labels:
    - Sign
    - failure to thrive
    ontology_label: Failure to thrive
  - term_id: HP:0002151
    reported_labels:
    - hyperlactatemia
    ontology_label: Increased circulating lactate concentration
  - term_id: HP:0011923
    reported_labels:
    - Lab
    - decreased complex I
    ontology_label: Decreased activity of mitochondrial complex I
  - term_id: HP:0008347
    reported_labels:
    - Lab
    - decreased complex IV
    ontology_label: Decreased activity of mitochondrial complex IV
  - term_id: CL:0000540
    reported_labels:
    - Tissue/cell level:** neurons
    - neuron
    ontology_label: neuron
  labels_variant: 9
  obsolete_terms:
  - term_id: GO:0009972
    ontology_label: obsolete cytidine deamination
  unresolvable_prefixes:
  - OMIM
  - UMLS
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Combined_Oxidative_Phosphorylation_Deficiency_35-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Combined_Oxidative_Phosphorylation_Deficiency_35-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Oxidative Phosphorylation Deficiency 35
- **MONDO ID:** MONDO:0054742 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Oxidative Phosphorylation Deficiency 35** covering all of the
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

# Combined Oxidative Phosphorylation Deficiency 35 (COXPD35) — Comprehensive Disease Report

**MONDO:** MONDO:0054742 · **OMIM:** #617873 · **Gene:** *TRIT1* (tRNA isopentenyltransferase 1)
**Category:** Mendelian, autosomal-recessive mitochondrial (nuclear-encoded) disorder
**Report date:** 2026-10-01 · **Evidence base:** Human clinical case reports/series; in vitro (patient fibroblasts, HeLa); model organism (yeast). ~15–20 patients reported worldwide.

> **Scope note.** COXPD35 is an ultra-rare disease documented almost exclusively through single-patient/single-family case reports. Quantitative epidemiology, survival statistics, QoL metrics, and controlled trials **do not exist**. Where a claim rests on general mitochondrial-disease knowledge rather than TRIT1-specific data, this is stated explicitly. Primary citations use PMIDs.

---

## 1. Disease Information

**Overview.** COXPD35 is a rare autosomal-recessive mitochondrial disease caused by biallelic pathogenic variants in *TRIT1*, which encodes tRNA isopentenyltransferase 1 (IPTase). The enzyme adds an isopentenyl group to adenosine-37 (i6A37) in the anticodon loop of a small subset of **both cytosolic and mitochondrial tRNAs**; its loss produces tRNA hypomodification, defective mitochondrial (and cytosolic) protein synthesis, and a combined deficiency of oxidative-phosphorylation (respiratory-chain) complexes. Clinically it is a neurodevelopmental mitochondrial encephalopathy dominated by microcephaly, developmental delay/intellectual disability, and epilepsy (PMID 24901367; PMID 28185376).

**Key identifiers.**
- OMIM: **#617873** (Combined oxidative phosphorylation deficiency 35)
- MONDO: **MONDO:0054742** (cross-refs confirmed via Monarch: **OMIM:617873**, **DOID:0111464**, **UMLS:C4693466**, **MedGen C1639653**)
- Gene: *TRIT1*, **HGNC:20286**, NCBI Gene ID **54802**, Ensembl **ENSG00000043514**, UniProt **Q9H3H1**, chromosome **1p34.2**
- Orphanet: **no COXPD35-specific ORPHA code** (absent from MONDO:0054742 mappings); grouped clinically under "Combined oxidative phosphorylation defect"/non-syndromic mitochondrial encephalopathy
- ICD-10: best fit **E88.49** (other mitochondrial metabolism disorders); ICD-11: **5C53.1** (mitochondrial metabolism disorders). No disease-specific code.
- MeSH: no specific descriptor; indexed under "Mitochondrial Diseases" / "OXPHOS" terms.

**Synonyms / alternative names.** COXPD35; Combined oxidative phosphorylation deficiency 35; TRIT1 deficiency; TRIT1-related mitochondrial disease; tRNA isopentenyltransferase 1 deficiency.

**Information source.** Disease-level knowledge is aggregated from **individual-patient case reports** (EHR-derived descriptions published as case studies) plus functional/biochemical studies in patient cells and model organisms. No registry or EHR-cohort data exist.

---

## 2. Etiology

**Primary cause (genetic).** Biallelic (homozygous or compound-heterozygous) loss-of-function variants in *TRIT1*. The disorder is monogenic and Mendelian; there is no environmental or infectious cause. The first case was a homozygous **p.Arg323Gln** identified by exome sequencing in a patient with "severe combined mitochondrial respiratory chain defects and corresponding perturbation in mitochondrial protein synthesis" (PMID 24901367). Causality was consolidated by matchmaking across additional recessive families (PMID 28185376).

**Genetic risk factors.** The causal genotype is biallelic *TRIT1* LOF. **Consanguinity** increases homozygosity risk (several reported families are consanguineous, e.g., Palestinian case, PMID 41760017; general consanguinity/IEM link, PMID 37453291). No established susceptibility loci or validated modifier genes.

**Environmental / protective factors.** None established. As a fully penetrant recessive metabolic disease, environmental exposures are not primary drivers. (General mitochondrial-disease principle: mitochondrial toxins, fasting/catabolic stress, fever, and certain drugs—e.g., valproate, aminoglycosides—can exacerbate decompensation; **inferred**, not demonstrated for TRIT1.)

**Gene–environment interactions.** Not characterized. Plausibly, intercurrent infection/metabolic stress precipitates seizures and decompensation (as in the Palestinian patient who presented in status epilepticus with concurrent pneumonia, PMID 41760017) — **inferred**.

---

## 3. Phenotypes

Phenotypes compiled from reported cases (PMID 24901367; 28185376; 32948376; 35418828; 36049610; 41760017). Frequencies are qualitative given the tiny N.

| Phenotype | Type | HPO suggestion | Onset | Severity/course | Frequency |
|---|---|---|---|---|---|
| Microcephaly (often progressive) | Physical/sign | HP:0000252 (microcephaly); HP:0005484 (postnatal) | Congenital/infantile | Variable, often progressive | Very common |
| Global developmental delay / intellectual disability | Behavioral/cognitive | HP:0001263; HP:0001249 | Infantile | Mild→severe; often severe | Very common |
| Epilepsy / seizures (incl. pharmaco-resistant, status epilepticus) | Sign/neurologic | HP:0001250; HP:0002133 (status epilepticus) | Early-infantile | Episodic, frequently drug-resistant | Common/characteristic |
| Abnormal EEG | Lab/electrophysiology | HP:0002353 | Infantile | — | Reported |
| Thin/hypoplastic corpus callosum | Imaging/sign | HP:0033725 / HP:0002079 | Congenital | Static structural | Reported |
| Dysmorphic facial features | Physical | HP:0001999 | Congenital | — | Reported |
| Hypotonia / motor impairment | Sign | HP:0001252 | Infantile | Variable | Reported |
| Failure to thrive / feeding difficulty | Sign | HP:0001508 | Infantile | — | Reported |
| Elevated lactate (serum/CSF) | Lab abnormality | HP:0002151 (hyperlactatemia) | — | Variable/inconsistent | Variable |
| Decreased mitochondrial complex I activity | Lab | HP:0011923 | — | — | In biochemically tested cases |
| Decreased mitochondrial complex IV activity | Lab | HP:0008347 | — | — | In biochemically tested cases |

**Additional HPO-curated features** (Monarch annotation set for MONDO:0054742, derived from reported cases):
- **Seizure semiology:** epileptic encephalopathy (HP:0200134), generalized myoclonic seizure (HP:0002123), febrile seizure (HP:0002373).
- **Motor / movement:** generalized hypotonia (HP:0001290), spasticity (HP:0001257), dystonia (HP:0001332), delayed ability to walk (HP:0031936).
- **Speech / cognition:** absent speech (HP:0001344), delayed speech and language development (HP:0000750).
- **Neuroimaging:** cerebral atrophy (HP:0002059) (in addition to thin corpus callosum).
- **Ophthalmologic:** optic disc hypoplasia (HP:0007766), myopia (HP:0000545), esotropia (HP:0000565).

**Characteristics.** Onset is typically **neonatal–early-infantile**. Severity is **variable**: the literature explicitly documents "both very severe, with generalized pharmaco-resistant seizures, and mild phenotypes" (PMID 36049610). Course is generally **progressive/static-encephalopathic** with episodic seizures.

**QoL impact.** Severe forms: profound disability, intractable epilepsy, dependence for all care, risk of early death (**data not quantified**; no EQ-5D/SF-36 data). Milder forms retain more function.

---

## 4. Genetic / Molecular Information

**Causal gene.** *TRIT1* (HGNC:20286; OMIM gene *606434*; UniProt **Q9H3H1**), chromosome **1p34.2**. Encodes **tRNA dimethylallyltransferase / tRNA isopentenyltransferase 1 (IPTase)**, a **467-aa**, dual-targeted (**mitochondrial + cytoplasmic**, confirmed UniProt subcellular annotation) enzyme, **EC 2.5.1.75**, catalyzing: adenosine(37) in tRNA + dimethylallyl diphosphate → N6-dimethylallyladenosine(37) in tRNA + diphosphate. Domain architecture: **Pfam PF01715 (IPPT)**; InterPro **IPR027417 (P-loop NTPase fold)** and **IPR003604 (zinc-finger)** — the latter is disrupted by the p.Glu327Lys variant (PMID 32948376). UniProt annotates **6 isoforms**, the molecular basis for the alternative-splicing buffering discussed below (PMID 15870694).

**Representative pathogenic variants (all germline, biallelic recessive).**
- **c.968G>A, p.Arg323Gln** — homozygous, first reported; missense near the tRNA-binding surface (modeled on yeast IPTase co-crystal), severe combined RC defect (PMID 24901367).
- **c.979G>A, p.Glu327Lys** + **c.682+2T>C** (splice) — compound het, Korean siblings; p.Glu327Lys disrupts the zinc-finger/IPT conformation (PMID 32948376).
- Novel missense variant — COXPD35 case (PMID 35418828).
- **Four novel variants in two patients** (missense/splice/truncating) expanding the allelic and phenotypic spectrum (PMID 36049610).
- **Two novel compound-heterozygous variants** — first Palestinian case (PMID 41760017).

**Variant classes:** missense, splice-site (e.g., c.682+2T>C), and truncating (nonsense/frameshift) — all converging on loss of IPTase function. **Classification:** reported variants are pathogenic/likely pathogenic by ACMG (segregation, functional assays, matchmaking; PMID 28185376). **ClinVar:** 208 *TRIT1* records, of which **67 are pathogenic/likely-pathogenic** (accessed 2026; NCBI E-utilities). **Functional consequence:** loss of function (reduced/abolished i6A37 modification), confirmed by complementation (PMID 24901367).

**Population-genetic constraint (gnomAD v4; this analysis).** Ensembl **ENSG00000043514**, chr1:39,838,110–39,883,511 (GRCh38; = 1p34.2). *TRIT1* is **LoF-tolerant**: **pLI ≈ 0** (6.4×10⁻¹³), **observed/expected LoF (LOEUF) = 0.84** (90% CI 0.66–1.08; 43 observed vs 51.2 expected LoF), **missense Z = 0.89**. Individual pathogenic alleles are rare, but some predicted-LoF alleles are relatively common (e.g., p.Arg112GlufsTer36 AF = 7.6×10⁻⁴; p.Arg327Ter AF = 6.4×10⁻⁴). **Interpretation:** heterozygous LoF is tolerated (carriers healthy; recessive inheritance), and because several predicted-LoF alleles are common yet the disease is ultra-rare, many such alleles are likely **not fully penetrant** — consistent with *TRIT1*'s complex alternative splicing in which **only the full-length isoform is catalytically active** (PMID 15870694), allowing residual isoform activity to buffer some truncations. Disease therefore likely requires biallelic variants that abolish activity across functional isoforms.

**Modifier genes / epigenetics / chromosomal abnormalities.** None established for COXPD35. (Separately, *TRIT1* promoter methylation and expression are studied in cancer contexts — PMID 40391218 — but this is unrelated to COXPD35.)

---

## 5. Environmental Information

No environmental, lifestyle, or infectious etiologic factors. COXPD35 is purely genetic. Intercurrent illness/metabolic stress may act as a **trigger for decompensation** (inferred; PMID 41760017 describes presentation with concurrent pneumonia). Standard mitochondrial-disease caution regarding mitotoxic drugs applies but is not TRIT1-specific.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain
1. **Biallelic LOF variants in *TRIT1*** → loss/reduction of tRNA isopentenyltransferase (IPTase) enzymatic activity (demonstrated; PMID 24901367).
2. Reduced IPTase activity **results in i6A37 hypomodification** of the A36-A37-A38 anticodon-loop subset of tRNAs in **both cytosol and mitochondria** (demonstrated in patient cells; PMID 24901367; substrate set defined in PMID 24126054).
3. Affected substrates: cytosolic **tRNA-Ser(AGA/CGA/UGA)** and **selenocysteine tRNA[Ser]Sec(UCA)**; mitochondrial **mt-tRNA-Ser(UCN)** and **mt-tRNA-Trp(UCA)** (PMID 24126054).
4. i6A37 loss **leads to** decreased **translational efficiency and fidelity** in a codon-specific manner (yeast-established principle; PMID 24901367).
5. Impaired **mitochondrial protein synthesis leads to** reduced levels of mtDNA-encoded OXPHOS subunits → **combined respiratory-chain (complex I/III/IV) deficiency** (decreased select mitochondrial proteins shown; PMID 28185376).
6. **Branch (cytosolic, demonstrated in model):** i6A37 loss also impairs **cytosolic translation** of specific codon-biased mRNAs. In *S. pombe*, the "mitochondrial-like" ATP/energy deficit is **fully rescued by a cytosol-only IPTase** and by cytosolic tRNA overexpression — cy-tRNA-Tyr is rate-limiting, and Tyr-codon-rich mRNAs encode carbon-metabolizing (often mitochondrially localized) enzymes (PMID 26857223). This shows the OXPHOS/energy phenotype is **not exclusively** due to mt-tRNA hypomodification; a cytosolic-translation branch contributes (human cytosolic substrates differ — tRNA-Ser/SeC).
7. **Branch (selenoprotein):** reduced i6A37 on tRNA[Ser]Sec may **impair selenoprotein translation** (UGA recoding), potentially compromising antioxidant defense — **inferred** (PMID 24126054 shows tRNA[Ser]Sec is a partial substrate; selenoprotein/tRNA[Ser]Sec interplay studied in PMID 34768885).
7. Deficient OXPHOS → **ATP-synthesis failure and secondary oxidative stress** → energy crisis in metabolically demanding **neurons** → **impaired brain growth (microcephaly), neurodevelopmental delay, and neuronal hyperexcitability (epilepsy)** (clinical phenotype; PMID 28185376).
8. **Clinical manifestation:** mitochondrial encephalopathy with variable severity set by residual TRIT1 activity.

### Checklist coverage
- **Molecular pathway:** tRNA wobble/anticodon modification → mitochondrial translation → OXPHOS/electron transport chain (KEGG oxidative phosphorylation; Reactome mitochondrial translation).
- **Cellular processes:** mitochondrial translation (GO:0032543), tRNA isopentenylation / tRNA wobble modification (GO:0006400 tRNA modification; GO:0009972 cytokinin biosynthesis-related transferase activity not applicable), bioenergetic failure, likely neuronal apoptosis (inferred).
- **Protein dysfunction:** loss of function; missense variants destabilize the catalytic/zinc-finger and tRNA-binding regions (PMID 24901367; 32948376).
- **Metabolic changes:** reduced ATP, lactate elevation (variable), combined complex deficiency.
- **Biochemical abnormality:** deficiency of i6A37 modification (enzyme-substrate defect); EC 2.5.1.75 (tRNA dimethylallyltransferase).
- **Immune involvement:** none (not an immunologic disease).
- **Tissue-damage mechanism:** chronic energy deficit + oxidative stress in CNS.

**Upstream vs downstream:** *TRIT1* LOF and tRNA hypomodification are **upstream**; OXPHOS deficiency, energy failure, and neurologic manifestations are **downstream**. **Cell types:** neurons (CL:0000540), potentially skeletal myocytes (CL:0000188), fibroblasts used as model. **GO terms:** GO:0006400 (tRNA modification), GO:0032543 (mitochondrial translation), GO:0006119 (oxidative phosphorylation). **Subcellular:** mitochondrion (GO:0005739), cytosol (GO:0005829).

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** brain/CNS (UBERON:0000955; brain). Secondary: skeletal muscle (UBERON:0001134) in some mitochondrial presentations. **Body system:** nervous system (predominant).
- **Imaging-defined sites:** cerebral cortex (microcephaly), **corpus callosum** (thinning/hypoplasia; UBERON:0002336).
- **Tissue/cell level:** neurons (CL:0000540); patient dermal fibroblasts (CL:0000057) used experimentally.
- **Subcellular:** **mitochondrion** (GO:0005739; UBERON cell component) — primary; **cytosol** (GO:0005829) for cytosolic tRNA modification.
- **Lateralization:** bilateral/diffuse CNS involvement.

---

## 8. Temporal Development

- **Onset:** congenital to early-infantile; seizures and delay typically manifest in the **first months of life** (PMID 32948376).
- **Pattern:** chronic, static-to-progressive encephalopathy with **episodic seizures**; metabolic decompensation can be acute (status epilepticus; PMID 41760017).
- **Progression rate:** variable — severe lethal infantile forms vs milder slowly-progressive forms (PMID 36049610).
- **Duration:** lifelong.
- **Critical period:** early neurodevelopment (first years) is the window of greatest vulnerability and of potential supportive-intervention benefit (inferred; PMID 37453291 emphasizes early recognition in neurometabolic epilepsies).
- **Remission:** none; seizures may be partially controlled but not cured.

---

## 9. Inheritance and Population

- **Inheritance:** **autosomal recessive** (PMID 28185376).
- **Penetrance:** effectively complete for biallelic LOF; **expressivity variable** (PMID 36049610).
- **Anticipation / germline mosaicism:** not applicable/not reported.
- **Consanguinity / founder effects:** consanguinity contributes (homozygous cases; PMID 41760017); no defined founder allele.
- **Carrier frequency:** heterozygous carriers asymptomatic (gnomAD: *TRIT1* is LoF-tolerant, pLI≈0, LOEUF 0.84; this analysis). A naive cumulative predicted-LoF allele frequency of ~2.1×10⁻³ would imply a carrier rate of ~1/236 and recessive incidence ~1/223,000 — but this **markedly overestimates** true disease frequency because many predicted-LoF alleles appear non-penetrant (see §4), so the real incidence is far lower.
- **Epidemiology:** **ultra-rare** — only ~a dozen+ patients reported worldwide ("Only 10 patients have been reported," PMID 36049610; "Only six cases … reported worldwide" earlier, PMID 32948376). Prevalence/incidence **not quantifiable** but observed frequency is far below the naive gnomAD prediction, indicating reduced penetrance of many LoF alleles; likely <<1/1,000,000 for the clinically recognized disease.
- **Demographics:** reported across diverse populations (European, Korean — PMID 32948376, Turkish — PMID 35418828, Palestinian — PMID 41760017). **Sex ratio:** no sex bias expected (autosomal); not formally reported. **Age distribution:** pediatric-onset.

---

## 10. Diagnostics

- **Primary diagnostic route:** **genetic testing** — whole-exome sequencing (WES) is the workhorse that established the diagnosis in essentially all reported cases, confirmed by **Sanger sequencing** (PMID 41760017; 32948376; 28185376). WGS, mitochondrial/nuclear gene panels, and single-gene *TRIT1* testing are alternatives. Chromosomal microarray/karyotype/FISH are generally normal (point-variant disease).
- **Biochemical/clinical tests:** respiratory-chain enzyme assays in muscle/fibroblasts show **combined complex deficiency**; serum/CSF **lactate** may be elevated (variable). Research-grade assay: **i6A37 quantification** in tRNA (mass spec/HPLC) is diagnostic/functional confirmation (PMID 24901367; 24126054).
- **Functional confirmation:** yeast complementation and TRIT1-rescue of patient fibroblasts validate variant pathogenicity (PMID 24901367; 15870694). A **tRNA-modification-sensitive northern blot** (differential probe annealing to modified vs unmodified tRNA) can quantify i6A37 hypomodification on specific tRNAs and has been used to characterize TRIT1 and other tRNA-modification-enzyme deficiencies (PMID 34930808).
- **Imaging:** brain MRI — microcephaly, thin corpus callosum, non-specific changes (PMID 41760017). **EEG** — epileptiform/abnormal background.
- **Differential diagnosis:** other combined-OXPHOS deficiencies and mitochondrial aminoacyl-tRNA synthetase / tRNA-modification disorders (e.g., MTO1, GTPBP3, TRMU, MARS2, other COXPD subtypes), early-infantile epileptic encephalopathies, and other causes of microcephaly + epilepsy + developmental delay. Distinguished by gene identification.
- **Screening:** no newborn screening; **cascade/carrier testing** of relatives and **prenatal/preimplantation testing** feasible once familial variants are known.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** no cohort statistics. Severe forms carry high morbidity and risk of early childhood death; milder forms survive with disability (PMID 36049610). Disease-specific mortality **not quantified**.
- **Morbidity/function:** profound neurodevelopmental disability, drug-resistant epilepsy, dependence for care in severe cases.
- **Complications:** status epilepticus, aspiration/respiratory infections (e.g., pneumonia; PMID 41760017), feeding failure, metabolic decompensation.
- **Prognostic factors:** **residual TRIT1/i6A37 activity** (genotype–phenotype correlation: truncating/severe LOF → worse) appears to drive severity (PMID 36049610); earlier/more severe seizures portend worse outcome (general neurometabolic principle, PMID 37453291).
- **QoL measures:** none published.

---

## 12. Treatment

**No disease-specific or curative therapy exists.** Management is **supportive and multidisciplinary** (general mitochondrial-disease standard; PMID 30024619).

- **Seizure control / pharmacotherapy:** standard antiepileptic drugs; many patients are **pharmaco-resistant** (PMID 36049610). Acute status epilepticus managed with benzodiazepines + phenytoin and supportive care (PMID 41760017). *Caution:* avoid valproate where mitochondrial dysfunction suspected (general principle).
- **Metabolic/"mitochondrial cocktail" (NCIT: Coenzyme Q10 therapy, etc.):** antioxidants and enzyme cofactors — **Coenzyme Q10/ubiquinone, riboflavin (vitamin B2), creatine monohydrate, α-lipoic acid, L-carnitine, arginine/citrulline, folinic acid, vitamins C/E/K** — are used empirically; evidence is low-quality and non-specific to TRIT1 (PMID 30024619). NCIT terms: Coenzyme Q10, Riboflavin, Levocarnitine, Thiamine.
- **Nutritional support:** individualized caloric/nutrient support; avoid fasting/catabolic stress (PMID 30024619).
- **Supportive/rehabilitative:** physical, occupational, speech therapy; feeding support (NG/gastrostomy); respiratory care; developmental support.
- **Advanced/experimental therapeutics:** **none approved**; no gene, cell, or RNA therapy trials for COXPD35. Gene replacement is a theoretical future avenue (complementation already restores the biochemical defect in vitro — PMID 24901367) but **not clinical**.
- **Pharmacogenomics / targeted / immunotherapy:** not applicable.

---

## 13. Prevention

- **Primary prevention:** **genetic counseling** for at-risk/consanguineous families; carrier testing; **prenatal diagnosis and preimplantation genetic testing** once familial *TRIT1* variants are known. No vaccine/behavioral prevention (non-infectious, non-lifestyle disease).
- **Secondary prevention:** early genetic diagnosis via WES enables timely supportive care and seizure management (PMID 37453291 stresses early recognition in neurometabolic epilepsies).
- **Tertiary prevention:** aggressive seizure control, infection prophylaxis, nutrition, and avoidance of mitotoxic drugs/catabolic stress to limit complications (inferred/general).
- **Public-health/environmental interventions:** not applicable beyond consanguinity counseling in high-prevalence communities.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs (NCBI Taxon; evolutionary conservation):** IPTase is deeply conserved — *E. coli* **MiaA**, *S. cerevisiae* **Mod5**, *S. pombe* **Tit1**, *C. elegans* **GRO-1**, human **TRIT1** (PMID 24126054). This conservation underpins cross-species functional assays.
- **Natural disease in animals:** no naturally occurring TRIT1 disease reported in companion animals/wildlife (OMIA — *not documented*). Veterinary relevance: none established.
- **Comparative biology:** substrate repertoire is **narrower in humans** (4 cytosolic tRNA-Ser/SeC substrates) than in yeasts, which modify a broader tRNA set (PMID 24126054) — relevant when extrapolating yeast phenotypes.
- **Transmission/zoonosis:** not applicable (genetic disease).

---

## 15. Model Organisms

- **Yeast (primary functional models):** *S. cerevisiae* **Mod5** and *S. pombe* **Tit1** are used for **complementation assays** to test human *TRIT1* variant function and nonsense-suppressor activity (PMID 15870694; 24901367). Yeast established that i6A37 loss reduces translational efficiency/fidelity codon-specifically. The *S. pombe* **tit1-Δ** deletion is a functional disease model reproducing a **"mitochondrial-like" metabolic deficiency** (reduced ATP, impaired growth on glycerol/under rapamycin) that is dissectible to a cytosolic-tRNA mechanism (PMID 26857223).
- **Bacterial/invertebrate orthologs:** *E. coli* MiaA; *C. elegans* GRO-1 (clk-type/developmental-timing phenotypes) — comparative references (PMID 24126054).
- **Human cell models:** patient-derived **fibroblasts** (i6A37 deficiency; rescued by WT-TRIT1 transduction — PMID 24901367) and **HeLa** siRNA-knockdown (substrate mapping — PMID 24126054).
- **Phenotype recapitulation:** yeast/cell models faithfully reproduce the **biochemical** defect (i6A37 loss, translation perturbation) and allow genotype–function correlation, but **do not** reproduce the human neurodevelopmental/epilepsy phenotype. A dedicated vertebrate (mouse/zebrafish) COXPD35 disease model is **not reported** — a search of the Alliance of Genome Resources returned no characterized mouse *Trit1* disease allele/model (accessed 2026), highlighting a key resource gap. *C. elegans* **gro-1** (IPTase ortholog) mutants show developmental-timing/clock phenotypes and provide comparative insight into i6A37 biology.
- **Applications:** variant pathogenicity classification, mechanism of translation defect, substrate identification, and complementation proof-of-concept for gene replacement.

---

## Supported vs. Refuted Hypotheses

**Supported:**
- COXPD35 is caused by biallelic LOF in *TRIT1* (PMID 24901367; 28185376).
- Core phenotype = microcephaly + developmental delay/ID + epilepsy, with a severity spectrum (PMID 28185376; 36049610).
- Mechanism = i6A37 tRNA hypomodification impairing mitochondrial (and cytosolic) translation → combined OXPHOS deficiency (PMID 24901367; 24126054; 28185376).
- Autosomal-recessive, ultra-rare; diagnosis by WES + Sanger (PMID 32948376; 41760017).

**Refuted / not applicable:**
- Environmental, infectious, or lifestyle etiology (none).
- Existence of curative or disease-specific pharmacotherapy (none; supportive only).
- Dominant/X-linked/mitochondrial-DNA inheritance (it is nuclear autosomal-recessive).

## Limitations & Future Directions
- Evidence rests on <~20 patients; no epidemiologic, survival, or QoL data; genotype–phenotype correlation is suggestive but statistically underpowered.
- No vertebrate disease model; no trials. Future needs: a knock-in mouse/zebrafish model, systematic i6A37 biomarker assays, natural-history registry, and exploration of selenoprotein/antioxidant contributions and AAV gene-replacement given in vitro rescue.

---

### Key Ontology Terms
- **MONDO:** MONDO:0054742 · **Gene/HGNC:** HGNC:20286 (*TRIT1*)
- **HPO (core):** HP:0000252 (microcephaly), HP:0001263 (global developmental delay), HP:0001249 (intellectual disability), HP:0001250 (seizures), HP:0002133 (status epilepticus), HP:0200134 (epileptic encephalopathy), HP:0002123 (generalized myoclonic seizure), HP:0002079 (hypoplasia of corpus callosum), HP:0002059 (cerebral atrophy), HP:0002151 (hyperlactatemia), HP:0011923 (decreased complex I), HP:0008347 (decreased complex IV)
- **HPO (additional):** HP:0001290 (hypotonia), HP:0001257 (spasticity), HP:0001332 (dystonia), HP:0001344 (absent speech), HP:0007766 (optic disc hypoplasia), HP:0000545 (myopia), HP:0000565 (esotropia), HP:0001508 (failure to thrive)
- **GO:** GO:0006400 (tRNA modification), GO:0032543 (mitochondrial translation), GO:0006119 (oxidative phosphorylation); GO:0005739 (mitochondrion), GO:0005829 (cytosol)
- **CL:** CL:0000540 (neuron), CL:0000057 (fibroblast)
- **UBERON:** UBERON:0000955 (brain), UBERON:0002336 (corpus callosum), UBERON:0001134 (skeletal muscle)
- **CHEBI:** CHEBI:dimethylallyl-diphosphate (DMAPP, isopentenyl donor); i6A (N6-isopentenyladenosine)
- **NCIT (treatment):** Coenzyme Q10, Riboflavin, Levocarnitine (supportive/empiric)

### Primary References (PMID)
24901367 · 28185376 · 24126054 · 26857223 · 34930808 · 34768885 · 15870694 · 32948376 · 35418828 · 36049610 · 41760017 · 30024619 · 37453291 · 40391218


## Artifacts

- [OpenScientist final report](Combined_Oxidative_Phosphorylation_Deficiency_35-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Combined_Oxidative_Phosphorylation_Deficiency_35-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 14 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 45 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 33 |
| Terms named correctly | 17 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001999` (1 mention) - the report calls it "Physical"; HP calls it **Abnormal facial shape**
- `HP:0001252` (1 mention) - the report calls it "Sign"; HP calls it **Hypotonia**
- `HP:0001508` (2 mentions) - the report calls it "Sign", "failure to thrive"; HP calls it **Failure to thrive**
- `HP:0002151` (2 mentions) - the report calls it "hyperlactatemia"; HP calls it **Increased circulating lactate concentration**
- `HP:0011923` (2 mentions) - the report calls it "Lab", "decreased complex I"; HP calls it **Decreased activity of mitochondrial complex I**
- `HP:0008347` (2 mentions) - the report calls it "Lab", "decreased complex IV"; HP calls it **Decreased activity of mitochondrial complex IV**
- `CL:0000540` (3 mentions) - the report calls it "Tissue/cell level:** neurons", "neuron"; CL calls it **neuron**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0009972` (obsolete cytidine deamination) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002353` (1 mention) - the report calls it "Lab/electrophysiology"; HP calls it **EEG abnormality**, and lists "Abnormal electroencephalogram" among its other names
- `HP:0002079` (2 mentions) - the report calls it "hypoplasia of corpus callosum"; HP calls it **Hypoplasia of the corpus callosum**, and lists "Hypoplasia of corpus callosum" among its other names
- `HP:0200134` (2 mentions) - the report calls it "Seizure semiology:** epileptic encephalopathy", "epileptic encephalopathy"; HP calls it **Epileptic encephalopathy**
- `HP:0001290` (2 mentions) - the report calls it "Motor / movement:** generalized hypotonia", "hypotonia"; HP calls it **Generalized hypotonia**
- `HP:0001344` (2 mentions) - the report calls it "Speech / cognition:** absent speech", "absent speech"; HP calls it **Absent speech**
- `HP:0002059` (2 mentions) - the report calls it "Neuroimaging:** cerebral atrophy", "cerebral atrophy"; HP calls it **Cerebral atrophy**
- `HP:0007766` (2 mentions) - the report calls it "Ophthalmologic:** optic disc hypoplasia", "optic disc hypoplasia"; HP calls it **Optic disc hypoplasia**
- `GO:0032543` (3 mentions) - the report calls it "Cellular processes:** mitochondrial translation", "mitochondrial translation"; GO calls it **mitochondrial translation**
- `UBERON:0001134` (2 mentions) - the report calls it "skeletal muscle"; UBERON calls it **skeletal muscle tissue**, and lists "skeletal muscle" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0001508` - called "Sign", "failure to thrive"
- `HP:0011923` - called "Lab", "decreased complex I"
- `HP:0008347` - called "Lab", "decreased complex IV"
- `HP:0200134` - called "Seizure semiology:** epileptic encephalopathy", "epileptic encephalopathy"
- `HP:0001290` - called "Motor / movement:** generalized hypotonia", "hypotonia"
- `HP:0001344` - called "Speech / cognition:** absent speech", "absent speech"
- `HP:0002059` - called "Neuroimaging:** cerebral atrophy", "cerebral atrophy"
- `HP:0007766` - called "Ophthalmologic:** optic disc hypoplasia", "optic disc hypoplasia"
- `GO:0032543` - called "Cellular processes:** mitochondrial translation", "mitochondrial translation"
- `CL:0000540` - called "Tissue/cell level:** neurons", "neuron"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `UMLS`.