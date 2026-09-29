---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-24T21:29:06.552609'
end_time: '2026-09-24T21:45:52.414277'
duration_seconds: 1005.86
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Nocardiosis
  mondo_id: MONDO:0017776
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
citation_count: 28
reference_validation:
  total_references: 29
  verified: 29
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 29
  on_topic: 17
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 32
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 7
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: HP:0025503
    reported_labels:
    - Skin abscess
    ontology_label: Anomalous coronary artery arising from the opposite sinus
  - term_id: HP:0032262
    reported_labels:
    - Disseminated infection
    ontology_label: Pulmonary tuberculosis
  - term_id: UBERON:0002048
    reported_labels:
    - Lung
    - Primary organ:** **Lung
    ontology_label: lung
  - term_id: UBERON:0000955
    reported_labels:
    - Brain
    - Most common secondary organ:** **Brain
    ontology_label: brain
  - term_id: UBERON:0002097
    reported_labels:
    - Other sites:** skin/subcutaneous tissue
    ontology_label: skin of body
  - term_id: NCIT:C1649
    reported_labels:
    - Oxazolidinone; key for CNS/severe/resistant disease
    ontology_label: Allovectin-7
  - term_id: NCIT:C312
    reported_labels:
    - Sulfonamide backbone; oral; prophylaxis + treatment
    ontology_label: Bleomycin Sulfate
  - term_id: NCIT:C233
    reported_labels:
    - Aminoglycoside; combination for severe disease
    ontology_label: Aminoglutethimide
  - term_id: NCIT:C61796
    reported_labels:
    - Severe/disseminated, CNS combination
    ontology_label: Ivermectin
  unresolvable_prefixes:
  - NCBI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Nocardiosis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Nocardiosis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Nocardiosis
- **MONDO ID:** MONDO:0017776 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Nocardiosis** covering all of the
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

# Nocardiosis: A Comprehensive Disease Characteristics Report

**Disease:** Nocardiosis · **MONDO:** MONDO:0017776 · **Category:** Infectious Disease
**Report type:** Disease knowledge-base template (15 sections) · **Iterations completed:** 5 · **Findings confirmed:** 8 · **Papers reviewed:** 59
**Evidence base:** Literature synthesis (PubMed). No patient-level data files were provided; all content is derived from aggregated disease-level literature (systematic reviews, multicenter cohorts, case series), not individual EHR data.

---

## Summary

Nocardiosis is an **opportunistic bacterial infection** caused by aerobic, Gram-positive, weakly (partially) acid-fast, branching filamentous actinomycetes of the genus *Nocardia*. It is an **environmentally acquired, non-heritable infectious disease**: the organism lives in soil, decaying vegetation and water, and enters the host by **inhalation** (producing pulmonary disease, the primary presentation) or by **traumatic inoculation** (producing cutaneous/subcutaneous disease, including actinomycetoma). Its defining clinical feature is a strong propensity for **hematogenous dissemination to the central nervous system**, where it forms ring-enhancing brain abscesses carrying a case-fatality of roughly 20–30%. Because the etiology is infectious rather than genetic, the many template sections that assume a Mendelian/heritable disease (causal human genes, inheritance pattern, penetrance, germline variant classification, genetic screening) are **Not Applicable**; the molecular characterization instead centers on **pathogen virulence factors** and **antimicrobial-resistance determinants**.

The disease disproportionately afflicts hosts with impaired **cell-mediated immunity**. The dominant risk factors — corticosteroid therapy, solid-organ and hematopoietic-cell transplantation, high calcineurin-inhibitor (tacrolimus) exposure, low CD4 counts (HIV/AIDS), and anti–GM-CSF autoantibodies — all converge on defective T-cell/macrophage killing. In solid-organ transplant recipients nocardiosis affects 0.04–3.5% of patients and confers a roughly 10-fold higher one-year mortality than in transplant recipients without infection. Diagnosis rests on demonstrating branching, beaded, weakly acid-fast filaments on microscopy, growth on culture (slow, days to weeks), and species-level identification by MALDI-TOF MS, 16S rRNA gene sequencing, MLSA, or whole-genome/metagenomic sequencing. Chest CT typically shows nodules/masses, consolidation and cavitation; brain MRI shows ring-enhancing abscesses with vasogenic edema.

Treatment is prolonged (months) and **species- and susceptibility-guided**. **Linezolid is universally active** against *Nocardia*; trimethoprim-sulfamethoxazole (TMP-SMX) and amikacin cover >90% of isolates and form the backbone of therapy, with carbapenems and third-generation cephalosporins used for severe/disseminated disease and neurosurgical drainage for brain abscesses. Resistance is species-specific and gene-encoded (e.g., *bla*FAR-1 in *N. farcinica*, *bla*AST-1 in *N. cyriacigeorgica*, *gyrA* mutations, 16S rRNA methyltransferases). Prevention is chiefly **dose-dependent TMP-SMX chemoprophylaxis** in high-risk immunosuppressed patients plus minimization of net immunosuppression; no vaccine exists for humans.

---

## Section 1 — Disease Information

**Overview.** Nocardiosis is a localized or disseminated opportunistic infection caused by *Nocardia* spp., environmental actinomycetes. It most often begins as a subacute-to-chronic pulmonary infection and can spread hematogenously, with the CNS the most common secondary site, followed by skin/soft tissue. It is not contagious person-to-person.

**Key identifiers.**
- **MONDO:** MONDO:0017776 (nocardiosis)
- **ICD-10:** A43 (A43.0 pulmonary, A43.1 cutaneous, A43.8 other forms, A43.9 unspecified); **ICD-11:** 1C1F
- **MeSH:** D009617 (Nocardia Infections)
- **OMIM / Orphanet:** Not a Mendelian disorder — no OMIM disease number. Orphanet lists nocardiosis as a rare infectious disease.
- **Causative genus (NCBI Taxonomy):** *Nocardia* (taxid 1817); key species include *N. asteroides*, *N. farcinica*, *N. cyriacigeorgica*, *N. brasiliensis*, *N. otitidiscaviarum*, *N. nova*, *N. seriolae* (fish).

**Synonyms / alternative names.** Nocardia infection; nocardial infection; actinomycetoma / Nocardial mycetoma (for the chronic subcutaneous form). Historically many cases were attributed to "*N. asteroides* complex" before molecular taxonomy split it into distinct species.

**Information source.** The evidence base is a mix of **individual patient reports/case series** (EHR-derived clinical cohorts) and **aggregated disease-level resources** (systematic reviews, multicenter case-control studies). No population-level germline registry applies.

---

## Section 2 — Etiology

**Primary cause — infectious.** Nocardiosis is caused by infection with *Nocardia* spp. As one review states, *"Nocardia are uncommon pathogens that disproportionately afflict the immunocompromised host"* ([PMID: 29668123](https://pubmed.ncbi.nlm.nih.gov/29668123/)). Acquisition is by inhalation of soil dust (pulmonary/disseminated disease) or by percutaneous trauma with soil/plant contamination (cutaneous disease, actinomycetoma).

**Risk factors (host, non-genetic).** Impaired **cell-mediated immunity** is the central predisposing state:
- **Corticosteroid therapy** — the single most common predisposing factor; in a systematic review of CNS nocardiosis, corticosteroid use was present in 55.8% of patients ([PMID: 35700710](https://pubmed.ncbi.nlm.nih.gov/35700710/)).
- **Solid-organ transplantation (SOT)** — affects 0.04–3.5% of recipients; independent risk factors include high calcineurin-inhibitor trough levels (OR 6.11, 95% CI 2.58–14.51), tacrolimus use (OR 2.65, 95% CI 1.17–6.00) and corticosteroid dose (OR 1.12 per unit, 95% CI 1.03–1.22) ([PMID: 27090987](https://pubmed.ncbi.nlm.nih.gov/27090987/)).
- **Hematopoietic-cell transplantation (HCT)** and delayed CD4 T-cell recovery.
- **High-dose methylprednisolone and CMV infection** (independent risk factors in renal transplant recipients; [PMID: 39254072](https://pubmed.ncbi.nlm.nih.gov/39254072/)).
- **HIV/AIDS with low CD4 counts.**
- **Anti–GM-CSF autoantibodies / autoimmune pulmonary alveolar proteinosis** (French multicenter study, PMID 38915339).
- **Chronic lung disease** (bronchiectasis, COPD), **diabetes mellitus**, connective tissue disease, malignancy.
- **Sulfonamide allergy label** — associated with higher nocardiosis risk in SOT (HR 3.85, 95% CI 1.44–10.30), likely via avoidance of protective TMP-SMX prophylaxis ([PMID: 39136148](https://pubmed.ncbi.nlm.nih.gov/39136148/)).

**Genetic risk factors (human host).** No established Mendelian susceptibility gene. Rare monogenic immunodeficiencies affecting phagocyte/T-cell function (e.g., chronic granulomatous disease) can predispose to *Nocardia*, but there is no disease-causing germline locus. Anti–GM-CSF autoantibody-driven susceptibility is acquired, not inherited. **This subsection is largely Not Applicable.**

**Protective factors.** **TMP-SMX chemoprophylaxis** reduces risk in a dose-dependent manner (see Section 13). No genetic protective variant is defined.

**Gene–environment interactions.** Not applicable in the human host in a Mendelian sense. The relevant interaction is **iatrogenic immunosuppression × environmental exposure** (soil/dust) — pharmacologic suppression of cell-mediated immunity converts an environmental saprophyte into a lethal pathogen.

---

## Section 3 — Phenotypes

Phenotypes are **infection manifestations**, not heritable traits. HPO terms below are suggested for knowledge-base mapping.

| Phenotype | Type | Frequency / notes | Suggested HPO |
|---|---|---|---|
| Pulmonary infection (pneumonia, nodules, cavitation) | Clinical/imaging | ~64% of cases (28/44) ([PMID: 41319540](https://pubmed.ncbi.nlm.nih.gov/41319540/)) | HP:0002090 (Pneumonia); HP:0100750 (Pulmonary nodules) |
| Fever | Symptom | Very common (100% in bacteremia series) | HP:0001945 (Fever) |
| Cough, dyspnea | Symptom | Common in pulmonary disease | HP:0012735 (Cough); HP:0002094 (Dyspnea) |
| Brain abscess / CNS involvement | Clinical | Most common secondary site; 86.9% of CNS cases show brain abscess ([PMID: 35700710](https://pubmed.ncbi.nlm.nih.gov/35700710/)) | HP:0025186 (Brain abscess); HP:0002383 (Encephalitis) |
| Focal neurological deficit / altered mental status | Sign | In CNS disease | HP:0034332 (Cognitive decline); HP:0002011 (CNS abnormality) |
| Cutaneous/subcutaneous abscess, actinomycetoma | Physical | Primary cutaneous (immunocompetent) or metastatic (disseminated) | HP:0025503 (Skin abscess) |
| Disseminated multi-organ infection | Clinical | ~30% (13/44) ([PMID: 41319540](https://pubmed.ncbi.nlm.nih.gov/41319540/)) | HP:0032262 (Disseminated infection) |
| Weight loss, malaise | Constitutional | Chronic presentations | HP:0001824 (Weight loss) |

- **Age of onset:** Predominantly adults; mean age ~55 ± 16 y in CNS series ([PMID: 35700710](https://pubmed.ncbi.nlm.nih.gov/35700710/)). Not congenital.
- **Severity:** Variable — from indolent cutaneous lesions to fatal disseminated/CNS disease.
- **Progression:** Subacute to chronic; can be rapidly progressive in severely immunosuppressed hosts.
- **Quality-of-life impact:** Substantial in disseminated/CNS disease (neurological sequelae, prolonged multi-month therapy, hospitalization); disease-specific QoL instruments are not established.

---

## Section 4 — Genetic / Molecular Information

**Human causal genes: Not Applicable.** Nocardiosis is infectious; there is no human causal gene, pathogenic germline variant, ACMG/AMP variant classification, modifier gene, inheritance-linked epigenetic lesion, or chromosomal abnormality. Sections requiring gnomAD allele frequency, somatic vs germline origin, and human variant nomenclature do not apply.

**Molecular characterization instead centers on the pathogen genome.** *Nocardia* virulence and resistance are gene-encoded (detailed in Sections 5, 6, 12). Genomic analysis of *N. seriolae* and clinical isolates identified virulence-associated genes including *sodA* (superoxide dismutase), *katG* (catalase), and mycolic-acid/cell-wall biosynthesis genes (*pks13*, *fadD32*, *pcaA*, *mftF*) ([PMID: 40827537](https://pubmed.ncbi.nlm.nih.gov/40827537/)). Resistance determinants include *bla*FAR-1, *bla*AST-1, *aph(2″)*, *gyrA* Ser83Ala, and a 16S rRNA m1A1408 methyltransferase ([PMID: 37527397](https://pubmed.ncbi.nlm.nih.gov/37527397/)).

---

## Section 5 — Environmental Information

**Environmental reservoir.** *Nocardia* is a ubiquitous soil saprophyte found in soil, decaying organic/plant matter, dust and water. Exposure to soil and dust (gardening, agriculture, construction) is the principal environmental risk; several case reports link disease to occupational/recreational soil exposure.

**Lifestyle factors.** Smoking and chronic lung disease increase pulmonary susceptibility; alcohol use and diabetes are frequent comorbidities. These are host-modifying rather than direct causal factors.

**Infectious agents (the cause).** Human disease is caused by multiple *Nocardia* species. Predominant clinical isolates include *N. asteroides*, *N. farcinica*, and *N. cyriacigeorgica* ([PMID: 41319540](https://pubmed.ncbi.nlm.nih.gov/41319540/)); *N. brasiliensis* is the classic cause of actinomycetoma; *N. otitidiscaviarum* shows unpredictable susceptibility; *N. seriolae* causes fish nocardiosis. *N. farcinica* is characteristically multidrug-resistant and over-represented in brain/disseminated disease.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Environmental exposure** — the host inhales soil/dust aerosols containing *Nocardia*, **or** the organism is inoculated through broken skin (trauma). → leads to
2. **Deposition in alveoli (or dermis)** and encounter with resident macrophages. → leads to
3. **Phagocytosis by macrophages**, which would normally kill the organism. → but
4. **Immune-evasion branch:** *Nocardia* resists intracellular killing. Secreted **catalase (*katG*) and superoxide dismutase (*sodA*)** detoxify reactive oxygen species; the **mycolic-acid–rich cell wall** (built by *pks13*, *fadD32*, *pcaA*, *mftF*) resists phagolysosomal degradation; secreted **proteases** damage tissue and **immunosuppressive metabolites (e.g., brasilicardin A)** blunt local immunity ([PMID: 40827537](https://pubmed.ncbi.nlm.nih.gov/40827537/); [PMID: 33956121](https://pubmed.ncbi.nlm.nih.gov/33956121/)). → results in
5. **Intracellular survival and replication within macrophages** — favored when host **cell-mediated immunity is impaired** (corticosteroids, calcineurin inhibitors, low CD4). → leads to
6. **Local suppurative/granulomatous inflammation.** In the lung: pneumonia, nodules, consolidation and cavitation. A local **anti-inflammatory (immunosuppressive) microenvironment coexists with a systemic acquired immune response** ([PMID: 22825801](https://pubmed.ncbi.nlm.nih.gov/22825801/)). Nitric oxide (eNOS) is required for actinomycetoma lesion formation in mice ([PMID: 33956121](https://pubmed.ncbi.nlm.nih.gov/33956121/)). → then branches
7a. **Containment branch (competent immunity):** granuloma / macrophage barrier walls off the organism → localized, indolent disease.
7b. **Dissemination branch (impaired immunity):** organisms breach the local barrier and enter the bloodstream. → leads to
8. **Hematogenous spread** to the **CNS** (most common secondary site), skin/soft tissue, and other organs. → results in
9. **Ring-enhancing brain abscess** with surrounding vasogenic edema. → leads to
10. **Clinical manifestation:** focal neurological deficit, altered mental status, seizures; untreated or delayed, **death** (CNS case-fatality ~23%).

*(Steps 4–5 are supported by pathogen genomics and animal models; the human host-side detail is inferred from clinical association with cell-mediated immune defects rather than mechanistically demonstrated in humans.)*

### Detail by category
- **Molecular pathways / cellular processes:** Macrophage phagocytosis and oxidative burst; ROS detoxification; granuloma formation; chronic inflammation. Suggested GO terms: GO:0006909 (phagocytosis), GO:0000302 (response to reactive oxygen species), GO:0006954 (inflammatory response), GO:0006801 (superoxide metabolic process).
- **Protein dysfunction (pathogen):** Mycolic-acid synthesis enzymes and antioxidant enzymes are gain-of-function virulence assets, not host defects.
- **Immune involvement:** Host defect is impaired **cell-mediated immunity** (T-cell/macrophage axis); IFN-γ–driven macrophage activation is protective (demonstrated in fish models, [PMID: 33045332](https://pubmed.ncbi.nlm.nih.gov/33045332/)).
- **Tissue damage mechanisms:** Suppuration/necrosis (abscess), protease-mediated tissue destruction, granulomatous fibrosis.
- **Cell types (CL terms):** macrophage (CL:0000235), neutrophil (CL:0000775), T cell (CL:0000084), CD4+ T cell (CL:0000624).

---

## Section 7 — Anatomical Structures Affected

- **Primary organ:** **Lung** (UBERON:0002048) — the portal of entry for inhaled disease; pulmonary infection in ~64% of cases.
- **Most common secondary organ:** **Brain** (UBERON:0000955) — brain abscess in the vast majority of CNS cases.
- **Other sites:** skin/subcutaneous tissue (UBERON:0002097), bone/joint/bursa, pericardium, lymph nodes, bloodstream (bacteremia), eye, kidney.
- **Body systems:** respiratory, nervous (CNS), integumentary, and (when disseminated) systemic/cardiovascular.
- **Tissue level:** lung parenchyma (alveolar epithelium and interstitium), brain parenchyma, dermis/subcutis.
- **Cell populations (CL):** macrophage (CL:0000235), neutrophil (CL:0000775).
- **Subcellular (GO cellular component):** phagosome/phagolysosome (GO:0045335 / GO:0032010) is the key intracellular niche.
- **Localization/lateralization:** Pulmonary lesions often multifocal/bilateral; brain abscesses may be single or multiple, unilateral or bilateral.

---

## Section 8 — Temporal Development

- **Onset:** Predominantly **adult**; subacute to chronic (insidious) course. In SOT, median onset is **17.5 months post-transplant** ([PMID: 27090987](https://pubmed.ncbi.nlm.nih.gov/27090987/)). Acute fulminant presentations occur in severe immunosuppression.
- **Progression:** From localized pulmonary focus to disseminated/CNS disease over weeks to months if untreated. Cavitation is more frequent in immunosuppressed and disseminated disease.
- **Course pattern:** Progressive without treatment; treatment-responsive but requires **prolonged (weeks to ≥6–12 months) therapy** to prevent relapse.
- **Duration:** Not self-limited; chronic if untreated.
- **Critical period:** Early diagnosis and drainage are decisive — delay increases CNS/dissemination and mortality. Prophylaxis interruption during immunosuppression transitions is a recognized trigger.

---

## Section 9 — Inheritance and Population

- **Inheritance:** **Not Applicable** — infectious, non-heritable. No inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity role, or carrier frequency.
- **Epidemiology:** Estimated incidence historically ~500–1,000 US cases/year (increasing with immunosuppressed populations); precise population incidence is uncertain and under-reported. In SOT, cumulative incidence 0.04–3.5% ([PMID: 27090987](https://pubmed.ncbi.nlm.nih.gov/27090987/)).
- **Demographics:** **Male predominance** (~70.8% male in CNS series); mean age ~55 y ([PMID: 35700710](https://pubmed.ncbi.nlm.nih.gov/35700710/)). Notably, **~34% of CNS cases were immunocompetent**, so immunocompetence does not exclude the diagnosis.
- **Geographic distribution:** Worldwide; actinomycetoma (*N. brasiliensis*) is more common in tropical/subtropical regions. Species distribution varies by region (e.g., *N. cyriacigeorgica* common in India, [PMID: 40112638](https://pubmed.ncbi.nlm.nih.gov/40112638/)).

---

## Section 10 — Diagnostics

**Microbiology (gold standard).** Direct microscopy of Gram-stained smears shows **branching, beaded, filamentous Gram-positive rods** that are **weakly/partially acid-fast** on modified Kinyoun stain. Gram-stained smears are emphasized as a valuable, easily-overlooked diagnostic step ([PMID: 36636850](https://pubmed.ncbi.nlm.nih.gov/36636850/)). Culture is slow (days to weeks). Species identification uses **MALDI-TOF MS, 16S rRNA gene sequencing, MLSA, WGS, and metagenomic next-generation sequencing (mNGS)** ([PMID: 42258415](https://pubmed.ncbi.nlm.nih.gov/42258415/)).

**Imaging.**
- **Chest CT:** Multiple/solitary nodules or masses are the most common finding (94.12% in one series), with ground-glass opacities (76.47%), patchy consolidation (73.53%), and cavitation (52.94%) ([PMID: 37185005](https://pubmed.ncbi.nlm.nih.gov/37185005/)). Cavitation is significantly more frequent in immunosuppressed than immunocompetent patients (**85% vs 29%, p = 0.005**, [PMID: 37185005](https://pubmed.ncbi.nlm.nih.gov/37185005/)) and in disseminated vs localized disease (64.3% vs 32.8%, [PMID: 38529577](https://pubmed.ncbi.nlm.nih.gov/38529577/)).
- **Brain MRI/CT (contrast):** ring-enhancing abscess(es) with vasogenic edema.

**Susceptibility testing.** Broth microdilution (CLSI) for TMP-SMX, linezolid, amikacin, carbapenems, third-generation cephalosporins, amoxicillin-clavulanate, moxifloxacin, minocycline. Species identification predicts likely resistance patterns.

**Clinical criteria / differential diagnosis.** No formal scoring system; diagnosis is microbiological. Differential includes tuberculosis, actinomycosis, fungal infection (aspergillosis, cryptococcosis), metastatic malignancy and lung cancer — pulmonary and CNS nocardiosis frequently **mimic malignancy** ([PMID: 42007821](https://pubmed.ncbi.nlm.nih.gov/42007821/)).

**Screening / genetic testing:** Not applicable (no germline component).

---

## Section 11 — Outcome / Prognosis

- **CNS nocardiosis case-fatality:** **22.8%** overall ([PMID: 35700710](https://pubmed.ncbi.nlm.nih.gov/35700710/)); nocardial brain abscesses carry a **20–55% mortality** ([PMID: 39780099](https://pubmed.ncbi.nlm.nih.gov/39780099/)).
- **SOT nocardiosis:** one-year all-cause mortality **16.2% vs 1.3%** in matched controls — a **10-fold increase** ([PMID: 28329348](https://pubmed.ncbi.nlm.nih.gov/28329348/)); 12-month mortality ~16.8% in a multicenter SOT cohort, with liver transplantation and shorter symptom-to-presentation time independently associated with death ([PMID: 36303280](https://pubmed.ncbi.nlm.nih.gov/36303280/)).
- **Prognostic factors:** immunosuppression intensity, CNS/disseminated involvement, species (*N. farcinica* worse), delayed diagnosis. **Surgery improves survival** in CNS disease (multivariate OR 2.4, 95% CI 0.99–4.11, p = 0.046, [PMID: 35700710](https://pubmed.ncbi.nlm.nih.gov/35700710/)).
- **Complications:** brain abscess rupture, respiratory failure, multi-organ dissemination, relapse if therapy is too short.
- **Recovery:** Good with early, susceptibility-guided, adequately prolonged therapy plus drainage; poor when diagnosis is delayed.

---

## Section 12 — Treatment

**Backbone pharmacotherapy.** *Nocardia* susceptibility is favorable to a defined set of agents:

| Agent | Activity across isolates | Notes | Suggested NCIT |
|---|---|---|---|
| **Linezolid** | **100%** (universally active) | Oxazolidinone; key for CNS/severe/resistant disease | NCIT:C1649 |
| **TMP-SMX (cotrimoxazole)** | **93%** | Sulfonamide backbone; oral; prophylaxis + treatment | NCIT:C312 |
| **Amikacin** | **91%** | Aminoglycoside; combination for severe disease | NCIT:C233 |
| **Carbapenems (imipenem/meropenem)** | High | Severe/disseminated, CNS combination | NCIT:C61796 |
| **Third-gen cephalosporins (ceftriaxone/cefotaxime)** | Species-dependent | *N. farcinica* often resistant (*bla*FAR-1) | NCIT:C548 |

Data: Israeli WGS study of 138 strains — *"Linezolid was active against all isolates, followed by trimethoprim/sulfamethoxazole (93%) and amikacin (91%)"* ([PMID: 37527397](https://pubmed.ncbi.nlm.nih.gov/37527397/)); Indian series — *"All tested isolates were susceptible to linezolid and 96% susceptible to amikacin"* ([PMID: 40112638](https://pubmed.ncbi.nlm.nih.gov/40112638/)).

**Species-specific resistance (gene-encoded):** *bla*FAR-1 → ceftriaxone resistance in *N. farcinica*; *bla*AST-1 → amoxicillin-clavulanate resistance in *N. cyriacigeorgica*/*N. neocaledoniensis*; *aph(2″)* → tobramycin resistance; *gyrA* Ser83Ala → ciprofloxacin resistance; 16S rRNA m1A1408 methyltransferase → amikacin resistance ([PMID: 37527397](https://pubmed.ncbi.nlm.nih.gov/37527397/)).

**Treatment strategy.**
- **Localized pulmonary/cutaneous:** TMP-SMX (monotherapy can be effective in SOT — favorable outcome in 19/24 patients completing ≥30 days, [PMID: 34143917](https://pubmed.ncbi.nlm.nih.gov/34143917/)).
- **Severe/disseminated/CNS:** **combination therapy** (e.g., TMP-SMX + linezolid ± amikacin/carbapenem), often 2–3 drugs initially, then oral step-down; total duration typically **6–12 months** (longer in CNS/immunosuppressed).
- **Surgical drainage** of brain and large soft-tissue abscesses improves outcomes.
- **Personalized approach:** therapy is **species/susceptibility-guided** via molecular ID and antimicrobial susceptibility testing.
- **Pharmacogenomics:** relevant to the sulfonamide component (sulfa hypersensitivity) but no *Nocardia*-specific PGx.

---

## Section 13 — Prevention

- **Primary prevention:** **TMP-SMX chemoprophylaxis** in high-risk immunosuppressed patients. An individual-patient-data meta-analysis of SOT recipients is titled *"Trimethoprim-sulfamethoxazole significantly reduces the risk of nocardiosis in solid organ transplant recipients"* and assessed *"its dose-response relationship, its effect on preventing disseminated nocardiosis, and the risk of TMP-SMX resistance in case of breakthrough infection"* ([PMID: 37865337](https://pubmed.ncbi.nlm.nih.gov/37865337/)). Protection is **dose-dependent**: low-dose (thrice-weekly, PJP-dosing) cotrimoxazole *"was not found to prevent nocardiosis"* ([PMID: 27090987](https://pubmed.ncbi.nlm.nih.gov/27090987/)), whereas higher/daily dosing is protective.
- **Breakthrough infections** occur despite prophylaxis and in-vitro susceptibility ([PMID: 42135975](https://pubmed.ncbi.nlm.nih.gov/42135975/)), reflecting host-immunity and drug-exposure factors; prophylaxis **rarely selects resistance** ([PMID: 29668123](https://pubmed.ncbi.nlm.nih.gov/29668123/)).
- **Minimize net immunosuppression** where clinically feasible.
- **Environmental/occupational caution:** reduce soil/dust exposure in severely immunosuppressed patients (gloves, masks for gardening).
- **De-labeling sulfa allergy** before transplant to preserve access to protective prophylaxis ([PMID: 39136148](https://pubmed.ncbi.nlm.nih.gov/39136148/)).
- **Immunization:** **No human vaccine** exists.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy of affected hosts:** Humans (*Homo sapiens*, NCBI:9606) and many animals. *Nocardia* is a natural pathogen of **fish** (*N. seriolae*), **dogs, cattle, and other mammals** ([PMID: 4604823](https://pubmed.ncbi.nlm.nih.gov/4604823/)).
- **Fish nocardiosis:** *N. seriolae* causes chronic granulomatous disease in >40 species of cultured marine/freshwater fish (largemouth bass, snakehead, amberjack, channel catfish), causing major aquaculture losses ([PMID: 38641217](https://pubmed.ncbi.nlm.nih.gov/38641217/); [PMID: 40827537](https://pubmed.ncbi.nlm.nih.gov/40827537/)).
- **Comparative pathology:** Granuloma formation is conserved across teleosts and mammals; teleost granulomas form a macrophage "barrier" via an epithelialization program ([PMID: 41443521](https://pubmed.ncbi.nlm.nih.gov/41443521/)).
- **Zoonotic potential:** Low/negligible for direct animal-to-human transmission; humans and animals are independently infected from the shared **environmental soil/water reservoir**.

---

## Section 15 — Model Organisms

- **Murine models:** The **C57BL/6 footpad actinomycetoma model** (*N. brasiliensis*) reproduces chronic granulomatous lesions; **eNOS-knockout mice** are protected from actinomycetoma, with increased T-cell proliferation and lower TNF-α — establishing that nitric oxide is required for lesion development ([PMID: 33956121](https://pubmed.ncbi.nlm.nih.gov/33956121/)).
- **Fish models:** Largemouth bass, snakehead (*Channa argus*), amberjack, and channel catfish infected with *N. seriolae* recapitulate chronic granulomatous disease and macrophage barrier biology; used to study pathogenesis, immune response (IFN-γ), and vaccine/adjuvant development ([PMID: 38641217](https://pubmed.ncbi.nlm.nih.gov/38641217/); [PMID: 41443521](https://pubmed.ncbi.nlm.nih.gov/41443521/); [PMID: 33045332](https://pubmed.ncbi.nlm.nih.gov/33045332/); [PMID: 29665356](https://pubmed.ncbi.nlm.nih.gov/29665356/)).
- **Phenotype recapitulation:** Both systems reproduce **granuloma formation, macrophage-centered immunity, and chronicity**. Limitations: rodent/fish models do not fully mirror the human iatrogenic-immunosuppression context (transplant, corticosteroids) or human CNS abscess dissemination.

---

## Key Findings (with expanded evidence)

### Finding 1 — Opportunistic infection: lung primary, CNS most common secondary site
In a retrospective series of 44 nocardiosis cases, pulmonary infection occurred in 28/44 (64%), disseminated disease in 13/44 (30%), and extrapulmonary single-organ disease in 3/44; 40/44 had comorbidities and 13/44 were on long-term glucocorticoids/immunosuppressants ([PMID: 41319540](https://pubmed.ncbi.nlm.nih.gov/41319540/)). Predominant isolates were *N. asteroides*, *N. farcinica*, and *N. cyriacigeorgica*. The opportunistic nature is captured succinctly: *"Nocardia are uncommon pathogens that disproportionately afflict the immunocompromised host"* ([PMID: 29668123](https://pubmed.ncbi.nlm.nih.gov/29668123/)).

### Finding 2 — CNS nocardiosis: ~23% case-fatality; *N. farcinica* predominates; surgery improves survival
A systematic review of adult CNS nocardiosis (129 papers) found mean age 55 ± 16 y, 70.8% male, *N. farcinica* the commonest species (39.6%), corticosteroid use the most common predisposing factor (55.8%), brain abscess in 86.9%, and **overall case-fatality 22.8%**; surgery independently improved survival (OR 2.4, 95% CI 0.99–4.11, p = 0.046) ([PMID: 35700710](https://pubmed.ncbi.nlm.nih.gov/35700710/)). Nocardial brain abscesses account for ~2% of all brain abscesses but carry **20–55% mortality** ([PMID: 39780099](https://pubmed.ncbi.nlm.nih.gov/39780099/)).

### Finding 3 — Corticosteroids, transplantation and cell-mediated immune defects dominate risk
In renal transplant recipients, *"High-dose methylprednisolone and cytomegalovirus infection were independent risk factors for Nocardia infection"* ([PMID: 39254072](https://pubmed.ncbi.nlm.nih.gov/39254072/)). TMP-SMX prophylaxis provides imperfect protection but does not select resistance: *"The use of TMP-SMX prophylaxis was not associated with TMP-SMX-resistant Nocardia"* ([PMID: 29668123](https://pubmed.ncbi.nlm.nih.gov/29668123/)).

### Finding 4 — Nocardiosis affects 0.04–3.5% of SOT recipients; immunosuppression intensity is the driver
The European multicenter case-control study (117 cases/234 controls) identified *"high calcineurin inhibitor trough levels in the month before diagnosis (odds ratio [OR], 6.11; 95% confidence interval [CI], 2.58-14.51), use of tacrolimus (OR, 2.65; 95% CI, 1.17-6.00) and corticosteroid dose (OR, 1.12; 95% CI, 1.03-1.22)"* as independent risk factors, and found *"low-dose cotrimoxazole prophylaxis was not found to prevent nocardiosis"* ([PMID: 27090987](https://pubmed.ncbi.nlm.nih.gov/27090987/)). One-year mortality was *"10-fold higher in SOT patients with nocardiosis than in those without"* ([PMID: 28329348](https://pubmed.ncbi.nlm.nih.gov/28329348/)).

### Finding 5 — Virulence: ROS-detoxifying enzymes, mycolic-acid wall, proteases, immunosuppressive metabolites
Genomics identified *"espG, mftF, pcaA, fadD32, pks13, narJ, feoB, sodA, katG and mceF"* virulence-associated genes ([PMID: 40827537](https://pubmed.ncbi.nlm.nih.gov/40827537/)). *N. brasiliensis "produces proteases that may play a role in tissue damage, as well as immunosuppressive molecules, such as brasilicardin A"*, and nitric oxide is required for lesions: *"Inflammation and actinomycetoma were prevented in genetically modified [eNOS-knockout] mice infected with N. brasiliensis"* ([PMID: 33956121](https://pubmed.ncbi.nlm.nih.gov/33956121/)).

### Finding 6 — Linezolid universally active; TMP-SMX and amikacin >90%; resistance species-specific
*"Linezolid was active against all isolates, followed by trimethoprim/sulfamethoxazole (93%) and amikacin (91%)"*, with resistance linked to defined determinants such as *"blaFAR-1 in N. farcinica (resistance to ceftriaxone)"* ([PMID: 37527397](https://pubmed.ncbi.nlm.nih.gov/37527397/)). An independent Indian cohort confirmed *"All tested isolates were susceptible to linezolid and 96 % susceptible to amikacin"* ([PMID: 40112638](https://pubmed.ncbi.nlm.nih.gov/40112638/)).

### Finding 7 — Diagnosis: microscopy/culture + molecular ID; characteristic CT and MRI findings
Pulmonary CT most commonly shows nodules/masses, ground-glass opacities, consolidation and cavitation — *"Multiple or solitary nodules represented the most common CT feature (n = 32, 94.12%), followed by ground-glass opacities (n = 26, 76.47%), patchy consolidations (n = 25, 73.53%), cavitations (n = 18, 52.94%)"* — with cavitation associated with immunosuppression (*"85% vs 29%, P = 0.005"*) ([PMID: 37185005](https://pubmed.ncbi.nlm.nih.gov/37185005/)). Molecular species identification uses *"16S rRNA gene sequencing, multilocus sequence analysis (MLSA), matrix-assisted laser desorption ionization-time-of-flight mass spectrometry (MALDI-TOF MS), whole-genome sequencing (WGS), and metagenomic next-generation sequencing (mNGS)"* ([PMID: 42258415](https://pubmed.ncbi.nlm.nih.gov/42258415/)).

### Finding 8 — Prevention: dose-dependent TMP-SMX prophylaxis; rarely selects resistance
The IPD meta-analysis assessed *"its dose-response relationship, its effect on preventing disseminated nocardiosis, and the risk of TMP-SMX resistance in case of breakthrough infection"* ([PMID: 37865337](https://pubmed.ncbi.nlm.nih.gov/37865337/)), reconciling why *"low-dose cotrimoxazole prophylaxis was not found to prevent nocardiosis"* ([PMID: 27090987](https://pubmed.ncbi.nlm.nih.gov/27090987/)) — protection is dose-dependent.

---

## Mechanistic Model / Interpretation

```
ENVIRONMENT (soil, dust, water)
        │  inhalation / traumatic inoculation
        ▼
   ALVEOLAR (or dermal) DEPOSITION
        │  phagocytosis by macrophages
        ▼
   PATHOGEN IMMUNE EVASION ─── katG/sodA (ROS detox)
        │                  ├── mycolic-acid wall (pks13, fadD32, pcaA)
        │                  ├── secreted proteases (tissue damage)
        │                  └── brasilicardin A (local immunosuppression)
        ▼
   INTRACELLULAR SURVIVAL & REPLICATION
        │  (permitted when host cell-mediated immunity is impaired:
        │   corticosteroids, calcineurin inhibitors, low CD4, anti–GM-CSF Ab)
        ▼
   LOCAL SUPPURATIVE / GRANULOMATOUS INFLAMMATION (pneumonia, nodules, cavitation)
        │
        ├──[competent immunity]──► granuloma containment → localized disease
        │
        └──[impaired immunity]───► HEMATOGENOUS DISSEMINATION
                                       │
                                       ▼
                           CNS ► ring-enhancing BRAIN ABSCESS (+ skin, other organs)
                                       │
                                       ▼
                    focal deficit / altered mental status → DEATH (~20–30%)
```

The unifying theme is a **two-hit model**: (1) a pathogen equipped to survive inside macrophages and (2) a host whose **cell-mediated immunity is pharmacologically or immunologically disabled**. Upstream events are environmental exposure and immune-evasion virulence; the pivotal branch point is host immune competence, which determines containment versus dissemination. Therapeutic and preventive levers act at defined points: **prophylaxis** (block establishment), **antibiotics** (kill intracellular organisms), **surgery** (evacuate abscess), and **immunosuppression minimization** (restore containment).

---

## Evidence Base

| PMID | Study | Contribution |
|---|---|---|
| [27090987](https://pubmed.ncbi.nlm.nih.gov/27090987/) | European SOT case-control (117/234) | Quantifies immunosuppression risk factors; low-dose prophylaxis inadequate |
| [28329348](https://pubmed.ncbi.nlm.nih.gov/28329348/) | European SOT outcomes | 10-fold excess 1-year mortality |
| [29668123](https://pubmed.ncbi.nlm.nih.gov/29668123/) | Transplant review (Duke cohort) | Opportunistic nature; prophylaxis does not select resistance |
| [35700710](https://pubmed.ncbi.nlm.nih.gov/35700710/) | CNS systematic review (129 papers) | 22.8% case-fatality; *N. farcinica*; surgery benefit |
| [37527397](https://pubmed.ncbi.nlm.nih.gov/37527397/) | WGS of 138 isolates (Israel) | Linezolid 100%; gene-encoded resistance |
| [40112638](https://pubmed.ncbi.nlm.nih.gov/40112638/) | Indian susceptibility series | Independent confirmation of linezolid/amikacin activity |
| [37185005](https://pubmed.ncbi.nlm.nih.gov/37185005/) | CT of pulmonary nocardiosis | CT feature frequencies; cavitation ↔ immunosuppression |
| [42258415](https://pubmed.ncbi.nlm.nih.gov/42258415/) | ID/AST review | Molecular diagnostic methods |
| [37865337](https://pubmed.ncbi.nlm.nih.gov/37865337/) | IPD meta-analysis | Dose-dependent TMP-SMX prevention |
| [40827537](https://pubmed.ncbi.nlm.nih.gov/40827537/) | *N. seriolae* genomics | Virulence genes (sodA, katG, mycolic-acid) |
| [33956121](https://pubmed.ncbi.nlm.nih.gov/33956121/) | eNOS-KO mouse model | Proteases, brasilicardin A; NO required for lesions |
| [39254072](https://pubmed.ncbi.nlm.nih.gov/39254072/) | Renal transplant (Pakistan) | Methylprednisolone, CMV as independent risks |
| [39780099](https://pubmed.ncbi.nlm.nih.gov/39780099/) | CNS abscess case/review | Brain-abscess frequency and 20–55% mortality |
| [36303280](https://pubmed.ncbi.nlm.nih.gov/36303280/) | SOT cohort (n=125) | 12-mo mortality; liver Tx and delay as prognostic factors |
| [34143917](https://pubmed.ncbi.nlm.nih.gov/34143917/) | TMP-SMX monotherapy in SOT | Monotherapy effective in most SOT cases |
| [39136148](https://pubmed.ncbi.nlm.nih.gov/39136148/) | Sulfa allergy label cohort | Sulfa label ↑ nocardiosis risk (HR 3.85) |
| [22825801](https://pubmed.ncbi.nlm.nih.gov/22825801/) | *N. brasiliensis* immunology | Systemic immunity vs local immunosuppressive microenvironment |
| [41443521](https://pubmed.ncbi.nlm.nih.gov/41443521/) | Teleost granuloma study | Conserved macrophage-barrier granuloma biology |

---

## Limitations and Knowledge Gaps

1. **Template mismatch.** This template assumes a heritable/Mendelian disease. For an infectious disease, sections on causal human genes, inheritance, penetrance, germline variant classification, and genetic screening are **Not Applicable**; molecular content necessarily shifts to pathogen biology.
2. **Epidemiology is under-characterized.** True population incidence/prevalence is uncertain because nocardiosis is not reportable in most jurisdictions and is under-diagnosed. Regional species-distribution and burden data are inadequate in many settings.
3. **Evidence quality.** Much of the clinical literature is retrospective case series and single-center cohorts; randomized treatment trials are essentially absent. Treatment durations and regimens are guided by expert consensus, not RCTs.
4. **Host-side mechanism is inferred.** The requirement for intact cell-mediated immunity is established by clinical association and animal models; direct human mechanistic proof (which T-cell/macrophage pathways fail under specific drugs) is incomplete.
5. **In-vitro/in-vivo discordance.** Breakthrough disease despite in-vitro susceptibility ([PMID: 42135975](https://pubmed.ncbi.nlm.nih.gov/42135975/)) shows susceptibility testing imperfectly predicts outcome.
6. **Species-level resistance heterogeneity.** *N. otitidiscaviarum* and inter-strain variability complicate empiric therapy ([PMID: 42143233](https://pubmed.ncbi.nlm.nih.gov/42143233/)).

---

## Proposed Follow-up Experiments / Actions

1. **Prospective incidence registry** stratified by immunosuppression regimen to define modern population burden and optimal prophylaxis dosing/duration.
2. **Randomized/adaptive trial of prophylaxis dosing** (single-strength daily vs thrice-weekly) in SOT/HCT to formalize the dose-response signal from [PMID: 37865337](https://pubmed.ncbi.nlm.nih.gov/37865337/).
3. **WGS-linked antimicrobial-resistance surveillance** to build species→resistance prediction rules (extending *bla*FAR-1/*bla*AST-1/*gyrA*/16S-methyltransferase mapping) enabling genotype-guided empiric therapy before phenotypic AST returns.
4. **Comparative-effectiveness study of TMP-SMX monotherapy vs combination** for disseminated/CNS disease, powered for mortality (current analyses are underpowered, [PMID: 36303280](https://pubmed.ncbi.nlm.nih.gov/36303280/)).
5. **Host-immunity biomarkers** (CD4 recovery, anti–GM-CSF autoantibody screening) to risk-stratify and target prophylaxis.
6. **Rapid molecular diagnostics** (mNGS/tNGS) validation to shorten time-to-species-ID and drainage decisions.
7. **Mechanistic dissection** of macrophage killing defects under calcineurin inhibitors/corticosteroids using human macrophage-*Nocardia* infection models to connect the two-hit model to actionable host-directed therapy.

---

*Report compiled from 8 confirmed findings and 59 reviewed papers across 5 investigation iterations. Evidence types span human clinical cohorts/case-control studies, systematic reviews, pathogen genomics, and murine/teleost model-organism studies.*


## Artifacts

- [OpenScientist final report](Nocardiosis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Nocardiosis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 29 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 29 |
| On topic | 17 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 16 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0025503` (1 mention) - the report calls it "Skin abscess"; HP calls it **Anomalous coronary artery arising from the opposite sinus**
- `HP:0032262` (1 mention) - the report calls it "Disseminated infection"; HP calls it **Pulmonary tuberculosis**
- `UBERON:0002048` (1 mention) - the report calls it "Lung", "Primary organ:** **Lung"; UBERON calls it **lung**
- `UBERON:0000955` (1 mention) - the report calls it "Brain", "Most common secondary organ:** **Brain"; UBERON calls it **brain**
- `UBERON:0002097` (1 mention) - the report calls it "Other sites:** skin/subcutaneous tissue"; UBERON calls it **skin of body**
- `NCIT:C1649` (1 mention) - the report calls it "Oxazolidinone; key for CNS/severe/resistant disease"; NCIT calls it **Allovectin-7**
- `NCIT:C312` (1 mention) - the report calls it "Sulfonamide backbone; oral; prophylaxis + treatment"; NCIT calls it **Bleomycin Sulfate**
- `NCIT:C233` (1 mention) - the report calls it "Aminoglycoside; combination for severe disease"; NCIT calls it **Aminoglutethimide**
- `NCIT:C61796` (1 mention) - the report calls it "Severe/disseminated, CNS combination"; NCIT calls it **Ivermectin**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0002048` - called "Lung", "Primary organ:** **Lung"
- `UBERON:0000955` - called "Brain", "Most common secondary organ:** **Brain"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `NCBI`.