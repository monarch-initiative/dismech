---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T03:39:43.489780'
end_time: '2026-10-15T04:06:14.406217'
duration_seconds: 1590.92
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Early-onset Familial Hypoaldosteronism
  mondo_id: MONDO:0035320
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
citation_count: 13
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 14
  validator_version: 0.3.0
term_validation:
  total_terms: 24
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 1
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: HP:0002902
    reported_labels:
    - Lab abnormality
    ontology_label: Hyponatremia
  - term_id: HP:0002153
    reported_labels:
    - Lab abnormality
    ontology_label: Hyperkalemia
  - term_id: HP:0001942
    reported_labels:
    - Lab abnormality
    ontology_label: Metabolic acidosis
  - term_id: HP:0001508
    reported_labels:
    - Clinical sign
    ontology_label: Failure to thrive
  - term_id: HP:0001944
    reported_labels:
    - Clinical sign
    ontology_label: Dehydration
  - term_id: HP:0002013
    reported_labels:
    - Symptom
    ontology_label: Vomiting
  - term_id: HP:0011046
    reported_labels:
    - Lab abnormality
    ontology_label: Agenesis of primary maxillary central incisor
  - term_id: HP:0000848
    reported_labels:
    - Lab abnormality
    ontology_label: Increased circulating renin concentration
  - term_id: UBERON:0001228
    reported_labels:
    - adrenal cortex zona glomerulosa
    ontology_label: renal papilla
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Early-onset_Familial_Hypoaldosteronism-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Early-onset_Familial_Hypoaldosteronism-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Early-onset Familial Hypoaldosteronism
- **MONDO ID:** MONDO:0035320 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Early-onset Familial Hypoaldosteronism** covering all of the
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

# Early-onset Familial Hypoaldosteronism (Aldosterone Synthase Deficiency / CYP11B2 Deficiency)
### Comprehensive Disease Characterization Report

---

## Summary

**Early-onset Familial Hypoaldosteronism is isolated aldosterone synthase deficiency (ASD)**, also known as corticosterone methyloxidase (CMO) deficiency types I and II. It is an autosomal recessive inborn error of steroidogenesis caused by biallelic loss-of-function variants in **CYP11B2**, the gene encoding the mitochondrial cytochrome P450 enzyme **aldosterone synthase**. CYP11B2 catalyzes the terminal three steps of aldosterone biosynthesis (11β-hydroxylation → 18-hydroxylation → 18-oxidation) in the adrenal **zona glomerulosa**. When the enzyme fails, aldosterone cannot be synthesized while cortisol and sex-steroid synthesis remain fully intact, producing an **isolated mineralocorticoid deficiency**.

Affected neonates and infants present in the first weeks to months of life with a renal **salt-wasting** phenotype: hyponatremia, hyperkalemia, metabolic acidosis, dehydration, recurrent vomiting, feeding difficulty, and failure to thrive. The biochemical hallmark is **high plasma renin activity** with **low (CMO I) or inappropriately normal (CMO II) aldosterone** and **normal cortisol**. The absence of skin hyperpigmentation and the normal cortisol distinguish ASD from both aldosterone-resistance disorders (pseudohypoaldosteronism type 1, PHA1) and from salt-wasting congenital adrenal hyperplasia (CAH). CMO II is further distinguished by a **pathognomonic elevation of the 18-hydroxycorticosterone/aldosterone ratio**.

The disorder is eminently treatable: mineralocorticoid replacement with **fludrocortisone** (with sodium chloride supplementation in infancy) rapidly corrects electrolytes and produces catch-up growth, usually within ~2 months. Prognosis is excellent when recognized early, whereas untreated salt-wasting crises can be lethal in infancy. Remarkably, the clinical phenotype ameliorates with age (increasing dietary salt intake and maturing renal mineralocorticoid sensitivity), so fludrocortisone can frequently be **discontinued by mid-childhood** even though the enzymatic defect persists biochemically for life. The disease is ultra-rare globally but enriched in consanguineous and founder populations — most notably **~1 in 4,000 births among Jews of Iranian origin**, who carry the founder CYP11B2 haplotype p.R181W + p.V386A.

---

## Disease Identity and Key Identifiers

**Early-onset Familial Hypoaldosteronism (MONDO:0035320)** is synonymous with **aldosterone synthase deficiency (ASD)** / **corticosterone methyloxidase deficiency**. Two biochemically defined forms exist:

| Form | OMIM | Biochemistry | Enzymatic lesion |
|------|------|--------------|------------------|
| CMO I (type 1) | 203400 | No detectable aldosterone; low/normal 18-OHB | Loss of both 18-hydroxylase and 18-oxidase activity |
| CMO II (type 2) | 610600 | Low–normal aldosterone; markedly elevated 18-OHB; high 18-OHB/aldosterone ratio | 18-hydroxylase retained, 18-oxidase lost |

**Common synonyms / alternative names:** aldosterone synthase deficiency; corticosterone methyloxidase deficiency types I and II (CMO I/II); corticosterone 18-methyloxidase deficiency; isolated hypoaldosteronism; congenital hypoaldosteronism; familial hypoaldosteronism.

- **Gene:** CYP11B2 (cytochrome P450 family 11 subfamily B member 2), chromosome **8q24.3**
- **Protein:** Aldosterone synthase (UniProt **P19099**)
- **Inheritance:** Autosomal recessive
- **Category:** Mendelian inborn error of steroidogenesis

The disease knowledge here is derived predominantly from **aggregated disease-level resources** (OMIM, Orphanet) and from the primary clinical/genetic literature — single consanguineous kindreds, founder-population cohorts, and a handful of multicenter case series — rather than from large EHR-scale individual-patient datasets.

---

## Key Findings

### Finding 1 — CYP11B2 loss of function causes isolated aldosterone deficiency

Biallelic inactivating mutations in CYP11B2 (chr8q24.3, encoding the mitochondrial cytochrome P450 aldosterone synthase) cause an **isolated** defect in aldosterone biosynthesis. The two clinical forms, CMO I (OMIM 203400) and CMO II (OMIM 610600), are distinguished by residual terminal enzyme activity. A critical quantitative principle is that **enzymatic activity must generally fall below ~1% of normal** before aldosterone biosynthesis is measurably impaired, reflecting substantial functional reserve in the pathway. Documented pathogenic variants include p.Gly452Arg, p.Thr185Ile, the compound R173K+E198D+V386A allele, and in-frame deletion of Arg173.

> *"Pathogenic variants in CYP11B2 result in corticosterone methyloxidase type I deficiency (CMO I), an orphan condition with a potentially lethal electrolyte imbalance in infancy."* — [PMID: 41229259](https://pubmed.ncbi.nlm.nih.gov/41229259/)

> *"Many mutations have been documented in each of these genes; in general enzymatic activity must be reduced to <1% of normal for aldosterone biosynthesis to be impaired."* — [PMID: 15134805](https://pubmed.ncbi.nlm.nih.gov/15134805/)

> *"The first, corticosterone methyloxidase type I (CMO I or type 1 deficiency), is characterized by no detectable aldosterone secretion, a low or normal secretion of the steroid 18OHB"* — [PMID: 9814506](https://pubmed.ncbi.nlm.nih.gov/9814506/)

### Finding 2 — Clinical presentation: neonatal/infantile salt wasting with a high-renin, low-aldosterone profile

Patients present in the neonatal period or early infancy with failure to thrive, feeding problems, recurrent vomiting and dehydration, severe **hyponatremia**, **hyperkalemia**, and **metabolic acidosis**. The laboratory hallmark is markedly **elevated plasma renin activity** with **low (CMO I)** or **inappropriately normal (CMO II)** plasma aldosterone. Because cortisol synthesis is unaffected, this is an isolated mineralocorticoid defect. The pathognomonic biochemical signature of CMO II is an elevated **18-hydroxycorticosterone/aldosterone ratio**.

> *"We studied an infant with failure to thrive and persistent hyponatremia despite oral sodium supplementation. Initial analyses revealed highly elevated plasma renin but normal values of plasma aldosterone."* — [PMID: 22931312](https://pubmed.ncbi.nlm.nih.gov/22931312/)

> *"diagnosed initially in the neonatal period because of severe hyponatremia, hyperkalemia, metabolic acidosis, and failure to thrive"* — [PMID: 41229259](https://pubmed.ncbi.nlm.nih.gov/41229259/)

> *"presented with failure to thrive and feeding problems at age 6 weeks. Important laboratory findings were low plasma sodium and elevated potassium and renin."* — [PMID: 9838244](https://pubmed.ncbi.nlm.nih.gov/9838244/)

### Finding 3 — Diagnosis by steroid profiling and CYP11B2 sequencing; treatment with fludrocortisone is highly effective and often discontinuable

Biochemical diagnosis rests on **multisteroid analysis** demonstrating the pathognomonic elevation of the 18-hydroxycorticosterone/aldosterone ratio (CMO II) together with elevated precursors (11-deoxycorticosterone [DOC], corticosterone, 18-OHDOC). Molecular confirmation is by CYP11B2 sequencing. **Mineralocorticoid replacement with fludrocortisone** (± sodium chloride supplementation in infancy) corrects the electrolyte disturbance and produces **catch-up growth**. Because distal-tubular aldosterone responsiveness matures with age and dietary salt intake rises, **treatment can frequently be discontinued** in later childhood without deterioration — in one documented case, stopped at age 9 years without relapse.

> *"revealing a pathognomonic pattern with a highly elevated ratio of 18-OH-corticosterone to aldosterone"* — [PMID: 22931312](https://pubmed.ncbi.nlm.nih.gov/22931312/)

> *"Treatment with fludrocortisone resulted in catch-up growth. Discontinuation of treatment at the age of 9 years was later possible without any clinical or biochemical deterioration."* — [PMID: 22931312](https://pubmed.ncbi.nlm.nih.gov/22931312/)

> *"secrete increased amounts of the steroid precursors DOC, corticosterone, and 18OHDOC, and are subject to salt wasting and poor growth"* — [PMID: 9814506](https://pubmed.ncbi.nlm.nih.gov/9814506/)

### Finding 4 — Pathophysiology and differential diagnosis

The isolated nature of the defect (normal cortisol, no hyperpigmentation) is the central clinical discriminator from aldosterone-resistance disorders and from CAH. ASD must be separated from **pseudohypoaldosteronism type 1 (PHA1)** — a *resistance* disorder in which aldosterone is HIGH — and from **21-hydroxylase deficiency CAH** (low cortisol, ambiguous genitalia, hyperpigmentation).

> *"Aldosterone synthase deficiency (ASD), which is caused by a genetic defect in CYP11B2, involves a deficiency in aldosterone alone."* — [PMID: 41905953](https://pubmed.ncbi.nlm.nih.gov/41905953/)

> *"ASD must also be differentiated from another disease, pseudohypoaldosteronism type 1 (PHA1), which involves resistance to aldosterone. PHA1a is caused by a heterozygous defect in NR3C2, which encodes the mineralocorticoid receptor. PHA1b is an autosomal recessive disorder caused by defects in the 3 epithelial sodium channel subunits"* — [PMID: 41905953](https://pubmed.ncbi.nlm.nih.gov/41905953/)

> *"Aldosterone is synthesized in the adrenal zona glomerulosa via the action of the mitochondrial cytochrome P450 enzyme aldosterone synthase (CYP11B2) through sequential enzyme reactions."* — [PMID: 41229259](https://pubmed.ncbi.nlm.nih.gov/41229259/)

### Finding 5 — Epidemiology and founder mutations (Jews of Iranian origin, ~1/4,000)

CMO II deficiency is relatively frequent among **Jews of Iranian origin**, with an estimated incidence of **1 in 4,000 births**. Affected individuals are homozygous for **two** CYP11B2 missense variants, **p.R181W and p.V386A**, inherited together on a founder haplotype. Functional expression showed that R181W reduces 18-hydroxylase and abolishes 18-oxidase activity while leaving 11β-hydroxylase intact, whereas V386A causes a small reduction in 18-hydroxycorticosterone production. Critically, individuals homozygous for **R181W alone (n=8)** or **V386A alone (n=3)** were asymptomatic, demonstrating that the two variants act **additively** to produce disease. Globally the disorder is ultra-rare; most other reports are single consanguineous kindreds, consistent with autosomal recessive inheritance.

> *"CMO-II deficiency is frequent among Jews from Iran (1 in 4000 births)"* — [PMID: 8481357](https://pubmed.ncbi.nlm.nih.gov/8481357/)

> *"two candidate mutations, R181W and V386A, were found in the CYP11B2 genes"* — [PMID: 1594605](https://pubmed.ncbi.nlm.nih.gov/1594605/)

> *"R181W reduced 18-hydroxylase and abolished 18-oxidase activities but left 11 beta-hydroxylase activity intact, whereas V386A caused a small but consistent reduction in the production of 18-hydroxycorticosterone"* — [PMID: 1594605](https://pubmed.ncbi.nlm.nih.gov/1594605/)

> *"All individuals affected with CMO-II deficiency were homozygous for both mutations, whereas eight asymptomatic subjects were homozygous for R181W alone and three were homozygous for V386A alone"* — [PMID: 1594605](https://pubmed.ncbi.nlm.nih.gov/1594605/)

### Finding 6 — Enzyme biochemistry: a three-step mitochondrial P450 reaction

Aldosterone synthase (CYP11B2, UniProt P19099) is a mitochondrial cytochrome P450 that converts **11-deoxycorticosterone to aldosterone** via three sequential reactions: **11β-hydroxylation** (→ corticosterone), **18-hydroxylation** (→ 18-hydroxycorticosterone), and **18-oxidation** (→ aldosterone). The enzyme coordinates its substrate at a catalytic **heme** moiety in the substrate-binding pocket (demonstrated structurally with the inhibitor dexfadrostat). Disease variants are characterized functionally in heterologous expression systems (cultured mammalian cells; fission yeast *Schizosaccharomyces pombe*) by measuring residual 11β-/18-hydroxylase and 18-oxidase activity. CMO I variants abolish all terminal activity (no aldosterone, low 18-OHB), whereas CMO II variants retain 18-hydroxylase but lose 18-oxidase (normal/low aldosterone, high 18-OHB).

> *"The aldosterone synthase, CYP11B2, catalyses the conversion of 11-deoxycorticosterone to aldosterone, a process that requires three steps: a hydroxylation at position 11β to form corticosterone, another one at position 18 to produce 18-hydroxycorticosterone, and, finally, an oxidation at position 18 to form aldosterone."* — [PMID: 21237269](https://pubmed.ncbi.nlm.nih.gov/21237269/)

> *"precisely coordinates with the catalytic heme moiety in the space of the CYP11B2 substrate binding pocket forming a tight and stable complex"* — [PMID: 37827219](https://pubmed.ncbi.nlm.nih.gov/37827219/)

> *"the heterologous expression of the mutants of CYP11B2 in fission yeast (Schizosaccharomyces pombe) followed by steroid bioconversion assays for the enzymatic characterisation of the investigated mutants"* — [PMID: 21237269](https://pubmed.ncbi.nlm.nih.gov/21237269/)

**Relevant CHEBI entities:** aldosterone (CHEBI:27584), corticosterone (CHEBI:16827), 11-deoxycorticosterone (CHEBI:16973), 18-hydroxycorticosterone, potassium(1+) (CHEBI:29103), sodium(1+) (CHEBI:29101).

### Finding 7 — Natural history and prognosis (multicenter cohort data)

A multicenter cohort of **16 patients from 12 families (8 female)** quantified the natural history: median age at presentation **3.1 months** (range 0.4–8.1), with poor weight gain the most common presenting symptom (**56.3%**). Median age at starting fludrocortisone was **3.6 months**, and catch-up growth was achieved a median of **2 months** after treatment began. Fludrocortisone was successfully **discontinued in 5/16 patients at a median age of 6.0 years** (range 2.2–7.6). Importantly, reduced aldosterone synthase activity **persisted biochemically** even after discontinuation, confirming that clinical remission reflects compensatory maturation (increasing dietary salt, maturing renal mineralocorticoid sensitivity) rather than resolution of the enzyme defect.

> *"Catch-up growth was achieved at median 2 months (range: 0.5 to 14.5) after treatment. Fludrocortisone could be stopped in 5 patients at a median age of 6.0 years (range: 2.2 to 7.6)."* — [PMID: 34415991](https://pubmed.ncbi.nlm.nih.gov/34415991/)

> *"Sixteen patients from 12 families were included (8 females; median age at presentation: 3.1 months, range: 0.4 to 8.1). The most common symptom was poor weight gain (56.3%)."* — [PMID: 34415991](https://pubmed.ncbi.nlm.nih.gov/34415991/)

> *"Plasma steroid profiles revealed reduced aldosterone synthase activity both at diagnosis and after discontinuation of treatment compared to age-matched controls."* — [PMID: 34415991](https://pubmed.ncbi.nlm.nih.gov/34415991/)

### Finding 8 — Variant spectrum and the CYP11B1 homology pitfall

Pathogenic CYP11B2 variants span **all molecular classes** and are enriched in consanguineous populations: missense (p.T185I — most common at **40%** in a Turkish cohort; also p.Y195H, p.F130L, p.G452W, p.G288S, p.G452R, p.R181W, p.V386A, p.E198D), nonsense (p.Q338stop), frameshift (p.Ser344Profs*9), splice-site (c.1200+1G>A, c.1122-18G>A), and in-frame deletions (p.E198del, p.I339_E343del, p.K175del, deletion of Arg173). Novel variants continue to be reported in Palestinian, Turkish, Arab, Chinese, Indian, and Polish patients from consanguineous or founder backgrounds. Variants are germline, biallelic (homozygous or compound heterozygous), and loss-of-function, classified pathogenic/likely pathogenic under ACMG criteria with functional/structural support. A key diagnostic caveat: **CYP11B2 shares ~95% sequence identity with the neighboring CYP11B1 gene**, creating sequencing pitfalls and risk of chimeric/unequal-crossover alleles.

> *"We identified 6 novel (p.Y195H, c.1200 + 1G > A, p.F130L, p.E198del, c.1122-18G > A, p.I339_E343del) and 4 previously described CYP11B2 variants. The most common variant (40%) was p.T185I."* — [PMID: 34415991](https://pubmed.ncbi.nlm.nih.gov/34415991/)

> *"revealed three homozygous pathogenic variants: p.Ser344Profs*9, p.G452W in two patients from an extended family, and p.Q338stop"* — [PMID: 33438832](https://pubmed.ncbi.nlm.nih.gov/33438832/)

> *"describe potential pitfalls in CYP11B2 sequencing due to its homology to CYP11B1"* — [PMID: 39700478](https://pubmed.ncbi.nlm.nih.gov/39700478/)

### Finding 9 — Formal diagnostic criteria separate ASD from PHA1 and CAH

A consensus diagnostic framework (Japanese Intractable Adrenal Disorders Research) defines ASD by: **(clinical)** salt-wasting symptoms — poor feeding, vomiting, dehydration, poor weight gain — **AND absence of skin pigmentation**; plus **(laboratory)** low serum sodium with high serum potassium; low-to-normal plasma aldosterone with high plasma renin activity/active renin concentration; and **no low blood cortisol**. Diagnoses of exclusion include PHA1 and 21-hydroxylase deficiency. This operationalizes the key discriminators: aldosterone is LOW/normal in ASD (deficiency) vs HIGH in PHA1 (resistance); cortisol is normal in ASD vs low in salt-wasting CAH; and there is no hyperpigmentation.

> *"1) Presents with salt-wasting symptoms (poor feeding, vomiting, dehydration, poor weight gain). 2) No skin pigmentation."* — [PMID: 41905953](https://pubmed.ncbi.nlm.nih.gov/41905953/)

> *"2) Low to normal plasma aldosterone and high plasma renin activity or high plasma active renin concentration. 3) No low blood cortisol level."* — [PMID: 41905953](https://pubmed.ncbi.nlm.nih.gov/41905953/)

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **biallelic loss-of-function CYP11B2 mutation** (germline, homozygous or compound heterozygous) **leads to** deficient or absent aldosterone synthase protein/activity in the adrenal zona glomerulosa.
2. Deficient aldosterone synthase activity **results in** failure of the terminal reactions of aldosterone biosynthesis — specifically 18-hydroxylation and/or 18-oxidation of corticosterone.
3. This **leads to** profound aldosterone deficiency (CMO I: no aldosterone; CMO II: low/inappropriately normal aldosterone with accumulated 18-hydroxycorticosterone — hence the diagnostic high 18-OHB/aldosterone ratio).
4. Loss of circulating aldosterone **results in** loss of mineralocorticoid-receptor–driven ENaC and Na⁺/K⁺ transport in the aldosterone-sensitive distal nephron (*inferred from the known physiology of MR/ENaC signaling*).
5. Impaired distal sodium reabsorption and potassium/H⁺ secretion **lead to** renal sodium wasting with impaired potassium and acid excretion.
6. This **results in** hyponatremia, hyperkalemia, metabolic acidosis, and hypovolemia.
7. Hypovolemia and hyponatremia **lead to** compensatory activation of the renin–angiotensin system (**hyperreninemia**), which cannot be translated into aldosterone because the enzymatic block is downstream.
8. The net effect **results in** a neonatal/infantile salt-wasting crisis with dehydration, vomiting, and failure to thrive — potentially lethal if untreated.

**Branch point (preserved pathway):** Because the lesion is specific to the terminal zona-glomerulosa enzyme, **cortisol and sex-steroid synthesis are unaffected**. This branch explains the two defining clinical negatives — **normal cortisol** and **no hyperpigmentation** — which separate ASD from salt-wasting CAH and from primary adrenal insufficiency.

**Age-dependent amelioration branch:** Over time, **increasing dietary salt intake** and **maturing renal tubular mineralocorticoid sensitivity** compensate for the persistent enzyme deficit, allowing clinical (but not biochemical) remission and discontinuation of therapy by mid-childhood.

### Compact pathway diagram

```
CYP11B2 biallelic LOF mutation
        │
        ▼
↓ Aldosterone synthase activity (zona glomerulosa mitochondria)
        │
        ▼
Block of 18-hydroxylation / 18-oxidation of corticosterone
        │
        ├── CMO I  → no aldosterone, low/normal 18-OHB
        └── CMO II → low/normal aldosterone, HIGH 18-OHB  ⇒ ↑18-OHB/aldo ratio
        │
        ▼
Aldosterone deficiency        ╌╌╌╌╌  Cortisol/sex steroids PRESERVED
        │                             (⇒ normal cortisol, NO hyperpigmentation)
        ▼
↓ MR→ENaC / Na-K transport in distal nephron  (inferred)
        │
        ▼
Renal Na⁺ wasting + impaired K⁺/H⁺ excretion
        │
        ▼
Hyponatremia + Hyperkalemia + Metabolic acidosis + Hypovolemia
        │
        ▼
Compensatory RAAS activation → HIGH renin (aldosterone cannot rise)
        │
        ▼
Salt-wasting crisis, failure to thrive (lethal if untreated)
        │
        ▼
Fludrocortisone ± NaCl → electrolyte correction + catch-up growth
        │
        ▼
Age-dependent amelioration (↑dietary salt, ↑tubular MR sensitivity)
   → therapy often discontinuable by mid-childhood
```

### Ontology term suggestions

| Domain | Term(s) |
|--------|---------|
| Disease (MONDO) | MONDO:0035320 (Early-onset Familial Hypoaldosteronism) |
| Gene (HGNC) | CYP11B2 |
| Phenotype (HPO) | Hyponatremia (HP:0002902); Hyperkalemia (HP:0002153); Metabolic acidosis (HP:0001942); Failure to thrive (HP:0001508); Dehydration (HP:0001944); Vomiting (HP:0002013); Hypoaldosteronism (HP:0011046); Increased circulating renin level (HP:0000848); Salt craving (HP:0003108) |
| Biological process (GO) | Aldosterone biosynthetic process (GO:0032342); steroid biosynthetic process (GO:0006694); sodium ion transport (GO:0006814); potassium ion homeostasis (GO:0055075) |
| Cellular component (GO) | Mitochondrion (GO:0005739); mitochondrial inner membrane (GO:0005743) |
| Cell type (CL) | Adrenal cortex zona glomerulosa cell; (kidney) principal cell of the collecting duct |
| Anatomy (UBERON) | Adrenal gland / adrenal cortex (UBERON:0001235); zona glomerulosa (UBERON:0001228); kidney (UBERON:0002113); distal convoluted tubule / collecting duct |
| Chemical (CHEBI) | Aldosterone (CHEBI:27584); corticosterone (CHEBI:16827); 11-deoxycorticosterone (CHEBI:16973); sodium(1+) (CHEBI:29101); potassium(1+) (CHEBI:29103) |
| Treatment (NCIT) | Fludrocortisone; sodium chloride supplementation |

---

## Section-by-Section Characterization

### 1. Disease Information
Isolated aldosterone synthase deficiency (CMO I/II), an autosomal recessive inborn error of adrenal steroidogenesis. Identifiers: MONDO:0035320; OMIM 203400 (CMO I) and 610600 (CMO II); gene CYP11B2 (8q24.3); protein UniProt P19099. Synonyms as listed above. Information derived from aggregated disease-level resources and primary clinical literature.

### 2. Etiology
**Causal factor:** purely genetic — biallelic loss-of-function CYP11B2 variants. **Genetic risk factors:** founder/consanguineous backgrounds dramatically raise risk (e.g., Iranian-Jewish R181W+V386A haplotype). No established environmental causes; the disease is monogenic. **Protective/modifier factors:** none proven genetically, but *dietary salt intake* and *maturation of renal mineralocorticoid sensitivity* act as powerful acquired modifiers of clinical severity with age. **Gene–environment interaction:** the principal interaction is between the fixed enzymatic deficit and dietary sodium availability — high salt intake offsets renal sodium wasting and underlies age-dependent remission.

### 3. Phenotypes

| Phenotype | Type | HPO | Onset | Frequency / notes |
|-----------|------|-----|-------|-------------------|
| Hyponatremia | Lab abnormality | HP:0002902 | Neonatal/infantile | Core feature |
| Hyperkalemia | Lab abnormality | HP:0002153 | Neonatal/infantile | Core feature |
| Metabolic acidosis | Lab abnormality | HP:0001942 | Neonatal/infantile | Common |
| Failure to thrive / poor weight gain | Clinical sign | HP:0001508 | Infantile | 56.3% most common presenting symptom (PMID 34415991) |
| Recurrent vomiting | Symptom | HP:0002013 | Infantile | Common |
| Dehydration | Clinical sign | HP:0001944 | Infantile | Common, can be severe |
| Elevated plasma renin | Lab abnormality | HP:0000848 | Neonatal/infantile | Diagnostic hallmark |
| Low/inappropriately normal aldosterone | Lab abnormality | HP:0011046 | Neonatal/infantile | Core; defines deficiency |

**Severity:** severe in infancy (potentially lethal salt-wasting crises), self-ameliorating with age. **Progression:** episodic crises early; overall course improves (clinical remission by mid-childhood). **Quality of life:** major in untreated infancy; excellent with timely treatment and after age-related remission.

### 4. Genetic / Molecular Information
**Causal gene:** CYP11B2 (8q24.3). **Variant classes:** missense, nonsense, frameshift, splice-site, and in-frame deletions — all germline, biallelic, loss-of-function (see Finding 8). **Allele frequencies:** pathogenic alleles are rare globally but locally common on founder haplotypes (e.g., R181W+V386A in Iranian Jews). **Functional consequence:** loss of function (reduced/absent 18-hydroxylase and/or 18-oxidase activity). **Diagnostic caveat:** ~95% homology with CYP11B1 risks mis-mapping and chimeric alleles. No epigenetic or large chromosomal mechanisms are established for this disorder.

### 5. Environmental Information
No toxic, infectious, or occupational cause. The one environmentally modifiable factor is **dietary sodium**: low intake unmasks/worsens salt wasting; higher intake (and salt supplementation) mitigates it.

### 6. Mechanism / Pathophysiology
See the ordered causal chain and diagram above. Upstream: CYP11B2 LOF → zona glomerulosa mitochondrial enzyme failure. Downstream: aldosterone deficiency → distal-nephron sodium wasting → electrolyte derangement → RAAS activation. Preserved branch: intact cortisol/androgen synthesis.

### 7. Anatomical Structures Affected
- **Primary organ:** adrenal gland, specifically the **adrenal cortex zona glomerulosa** (UBERON:0001228), site of the enzymatic defect.
- **Secondary (functionally affected) organ:** **kidney** — aldosterone-sensitive distal nephron (distal convoluted tubule, connecting tubule, collecting duct principal cells), where mineralocorticoid action is lost.
- **Body system:** endocrine (adrenal steroidogenesis) and renal/electrolyte-regulatory.
- **Subcellular compartment:** **mitochondrion** (GO:0005739) — aldosterone synthase is a mitochondrial inner-membrane P450.
- **Lateralization:** bilateral (systemic hormonal deficiency).

### 8. Temporal Development
**Onset:** neonatal to early infancy (median presentation ~3.1 months; range 0.4–8.1). **Pattern:** acute salt-wasting crises on a chronic genetic background. **Course:** severe early, then progressive clinical amelioration with age. **Remission:** treatment can be discontinued in a substantial fraction (5/16; median 6.0 years) — a treatment-withdrawable clinical remission despite persistent biochemical deficit. **Critical period:** infancy is the window of vulnerability (crisis risk) and of therapeutic opportunity.

### 9. Inheritance and Population
**Inheritance:** autosomal recessive. **Penetrance:** essentially complete for biallelic LOF genotypes, though expressivity varies (CMO I vs II; allele-dependent). **Epidemiology:** ultra-rare globally; **~1/4,000 births among Jews of Iranian origin** (founder effect). **Founder effect:** R181W+V386A compound haplotype. **Consanguinity:** major driver — most non-founder cases arise in consanguineous Palestinian, Turkish, Arab, Chinese, Indian kindreds. **Sex ratio:** no strong sex bias (cohort 8/16 female). **Carrier frequency:** elevated in founder/consanguineous populations; heterozygotes are asymptomatic.

### 10. Diagnostics
**Laboratory:** serum electrolytes (↓Na⁺, ↑K⁺, acidosis); **plasma renin activity (high)**; **plasma aldosterone (low/inappropriately normal)**; **multisteroid profiling** showing elevated DOC, corticosterone, 18-OHDOC, and the **pathognomonic high 18-OHB/aldosterone ratio** (CMO II); **normal cortisol**. **Genetic testing:** CYP11B2 single-gene sequencing or targeted adrenal/steroidogenesis gene panels; WES/WGS for atypical cases — with careful handling of CYP11B1 homology. **Clinical criteria:** salt-wasting symptoms + no skin pigmentation + the laboratory profile above (Finding 9). **Differential diagnosis:** PHA1 (high aldosterone, resistance), salt-wasting CAH / 21-hydroxylase deficiency (low cortisol, virilization, hyperpigmentation), secondary PHA (renal/urologic disease, UTI/reflux). **Screening:** cascade/carrier testing in affected families and founder populations.

### 11. Outcome / Prognosis
**Excellent** with early recognition and mineralocorticoid replacement: normal growth and development, catch-up growth within ~2 months. **Mortality:** untreated infantile salt-wasting crises can be fatal. **Morbidity:** minimal once treated. **Prognostic factors:** timeliness of diagnosis and treatment; CMO subtype. Long-term, many patients achieve treatment-free clinical remission while retaining a subclinical enzyme defect.

### 12. Treatment
**Mainstay:** **fludrocortisone** (synthetic mineralocorticoid; NCIT: Fludrocortisone), ± **sodium chloride supplementation** in infancy. Corrects electrolytes, restores volume, enables catch-up growth. **Pharmacogenomics / advanced/gene/cell/RNA therapies:** none established or required — the disorder is managed effectively by hormone replacement. **Treatment strategy:** initiate in infancy, titrate to electrolytes/renin/growth, and attempt **supervised discontinuation in mid-childhood** once salt tolerance and renal sensitivity mature. **Adverse events:** standard mineralocorticoid excess risks (hypertension, hypokalemia) if overdosed — monitored by electrolytes and blood pressure.

### 13. Prevention
No primary prevention (monogenic). **Secondary prevention:** early detection and prompt fludrocortisone prevent crises and failure to thrive. **Genetic counseling / screening:** autosomal recessive counseling, carrier and cascade testing in founder/consanguineous families; prenatal/preimplantation options where a familial variant is known. **Tertiary prevention:** electrolyte monitoring and salt management to prevent recurrent crises.

### 14. Other Species / Natural Disease
Human disease (NCBI Taxon 9606). Murine models of aldosterone synthase deficiency (**aldosterone synthase-deficient mice**) are used experimentally to study renal potassium/sodium handling (e.g., tissue-kallikrein and NCC studies). Orthologous gene: mouse *Cyp11b2*. No prominent naturally occurring companion-animal counterpart is established in the reviewed literature.

### 15. Model Organisms
**Mouse** is the principal model: aldosterone synthase (*Cyp11b2*)-deficient mice recapitulate aldosterone-independent physiology and have been used to dissect distal-nephron potassium handling and renal adaptation (e.g., PMID 20624970 used aldosterone synthase-deficient mice to show aldosterone-independent control of tissue kallikrein). **In vitro:** heterologous expression in cultured mammalian cells and **fission yeast (*S. pombe*)** enables steroid-bioconversion assays to functionally classify CYP11B2 variants (PMID 21237269). **Applications:** variant functional characterization, steroidogenesis pathway dissection, renal electrolyte physiology. **Limitations:** rodent adrenal zonation and steroid profiles differ from humans; in vitro systems isolate enzymatic activity but not whole-organism salt handling.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports |
|------|-----------------|----------|
| [15134805](https://pubmed.ncbi.nlm.nih.gov/15134805/) | *Aldosterone synthase deficiency and related disorders* | <1% residual activity threshold; overview |
| [9814506](https://pubmed.ncbi.nlm.nih.gov/9814506/) | *Isolated ASD caused by E198D and V386A* | CMO I vs II biochemistry; elevated precursors |
| [41229259](https://pubmed.ncbi.nlm.nih.gov/41229259/) | *ASD with coexisting celiac disease* | Orphan, lethal infantile electrolyte imbalance; zona glomerulosa mitochondrial synthesis |
| [22931312](https://pubmed.ncbi.nlm.nih.gov/22931312/) | *Homozygous CYP11B2 in infant with CMO II* | High renin/normal aldosterone; 18-OHB/aldo ratio; fludrocortisone + discontinuation at 9y |
| [9838244](https://pubmed.ncbi.nlm.nih.gov/9838244/) | *Homozygous deletion of Arg-173, CMO II* | Infantile onset; hyponatremia, hyperkalemia, high renin |
| [41905953](https://pubmed.ncbi.nlm.nih.gov/41905953/) | *Congenital aldosterone deficiency and its resistance* | Isolated deficiency; PHA1 differential; formal diagnostic criteria |
| [8481357](https://pubmed.ncbi.nlm.nih.gov/8481357/) | *11β-hydroxylase/CMO-II in Jews of Morocco/Iran* | 1/4,000 incidence in Iranian Jews |
| [1594605](https://pubmed.ncbi.nlm.nih.gov/1594605/) | *CYP11B2 mutations causing CMO II* | R181W + V386A founder variants; additive two-variant requirement; functional data |
| [21237269](https://pubmed.ncbi.nlm.nih.gov/21237269/) | *S. pombe system for CMO-causing mutations* | Three-step enzymatic mechanism; yeast functional assay |
| [37827219](https://pubmed.ncbi.nlm.nih.gov/37827219/) | *CYP11B2 inhibition by dexfadrostat* | Heme/substrate-pocket active-site structure |
| [34415991](https://pubmed.ncbi.nlm.nih.gov/34415991/) | *Catch-up growth and discontinuation of fludrocortisone in ASD* | Cohort demographics; catch-up growth; discontinuation; persistent biochemical defect; variant spectrum |
| [33438832](https://pubmed.ncbi.nlm.nih.gov/33438832/) | *CYP11B2 deficiency in Palestinian infants* | Frameshift/missense/nonsense variants; consanguinity; genetic heterogeneity |
| [39700478](https://pubmed.ncbi.nlm.nih.gov/39700478/) | *Cracking the code of ASD: genetics and biochemistry* | CYP11B1 homology sequencing pitfall |

Supporting/contextual literature also reviewed: PMID 32539318 (CMO II novel mutations), 41426917 (ASD type I novel variant, neonate), 37332400 (CMO1 case reports), 35848593 (novel CYP11B2 variant), 15179565 and 22764468 (differential diagnosis: selective hypoaldosteronism vs PHA1), 38324138 and 38027139 (chimeric CYP11B1/CYP11B2 alleles), 41709876 (rare CAH subtypes including ASD), 6507399 (Iranian-Jewish CMO II child). Several RAAS/renal-physiology and mouse-model papers (e.g., 20624970, 23447069, 20049674) provide mechanistic context for aldosterone action and model-organism applications.

---

## Limitations and Knowledge Gaps

1. **Small evidence base.** The disorder is ultra-rare; most data come from single kindreds, founder cohorts, and one 16-patient multicenter series. There are no large-scale prevalence, incidence, or outcome datasets outside founder populations.
2. **Downstream nephron step is inferred.** The loss of MR→ENaC signaling in the distal nephron is drawn from general mineralocorticoid physiology rather than disease-specific tissue studies in ASD patients.
3. **Genotype–phenotype relationships are incompletely resolved.** The boundary between CMO I and CMO II is biochemical and allele-dependent, and some variants produce intermediate phenotypes; residual-activity thresholds are approximate.
4. **Quality-of-life and long-term outcome data are sparse.** Formal QoL instruments (EQ-5D, SF-36, PROMIS) have not been applied; long-term adult outcomes after childhood remission are under-characterized.
5. **No omics-scale molecular profiling** (transcriptomic/proteomic/metabolomic) specific to ASD adrenal tissue was identified; mechanism rests on enzymology and steroid biochemistry.
6. **Diagnostic homology pitfall** (CYP11B2/CYP11B1 ~95% identity) may cause under- or mis-diagnosis in laboratories not using homology-aware methods.

---

## Proposed Follow-up Experiments / Actions

1. **Build an international ASD registry** capturing genotype, steroid profiles (including 18-OHB/aldosterone ratio), treatment course, age at discontinuation, and long-term adult outcomes to firm up natural history and penetrance/expressivity.
2. **Systematic functional classification** of all reported CYP11B2 variants in a standardized assay (e.g., *S. pombe* or mammalian expression) to produce a quantitative residual-activity ladder predicting CMO I vs II vs intermediate phenotypes.
3. **Homology-aware diagnostic protocols** (long-read sequencing, MLPA/CNV analysis) to resolve CYP11B1/CYP11B2 chimeras and prevent misclassification; validate against known founder haplotypes.
4. **Prospective QoL and growth outcome study** using standardized instruments, including after treatment discontinuation, to document remission durability and any late relapse risk.
5. **Mechanistic confirmation of the distal-nephron step** in patient-derived or model systems (e.g., renal organoids/iPSC-derived tubular cells) to move the MR→ENaC step from inferred to demonstrated.
6. **Carrier-screening evaluation** in founder/consanguineous populations (Iranian-Jewish, Palestinian, Turkish, Arab cohorts) to quantify carrier frequency and inform genetic counseling and prenatal/preimplantation options.

---

*Report compiled from 9 confirmed findings and 38 reviewed papers over 5 investigation iterations. Evidence types span human clinical case reports/series, in vitro functional expression assays, structural biology, and model-organism studies.*


## Artifacts

- [OpenScientist final report](Early-onset_Familial_Hypoaldosteronism-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Early-onset_Familial_Hypoaldosteronism-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 11 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002902` (2 mentions) - the report calls it "Lab abnormality"; HP calls it **Hyponatremia**
- `HP:0002153` (2 mentions) - the report calls it "Lab abnormality"; HP calls it **Hyperkalemia**
- `HP:0001942` (2 mentions) - the report calls it "Lab abnormality"; HP calls it **Metabolic acidosis**
- `HP:0001508` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Failure to thrive**
- `HP:0001944` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Dehydration**
- `HP:0002013` (2 mentions) - the report calls it "Symptom"; HP calls it **Vomiting**
- `HP:0011046` (2 mentions) - the report calls it "Lab abnormality"; HP calls it **Agenesis of primary maxillary central incisor**
- `HP:0000848` (2 mentions) - the report calls it "Lab abnormality"; HP calls it **Increased circulating renin concentration**
- `UBERON:0001228` (2 mentions) - the report calls it "adrenal cortex zona glomerulosa"; UBERON calls it **renal papilla**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005739` (2 mentions) - the report calls it "mitochondrion", "Subcellular compartment:** **mitochondrion"; GO calls it **mitochondrion**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005739` - called "mitochondrion", "Subcellular compartment:** **mitochondrion"