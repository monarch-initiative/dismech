---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-05T14:12:49.183438'
end_time: '2026-09-05T14:26:06.249650'
duration_seconds: 797.07
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Glycogen Storage Disease Due To Aldolase A Deficiency
  mondo_id: MONDO:0012747
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
citation_count: 16
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 11
  validator_version: 0.2.1
term_validation:
  total_terms: 35
  verified: 33
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 0
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: HP:0004804
    reported_labels:
    - Lab / clinical sign
    ontology_label: Congenital hemolytic anemia
  - term_id: HP:0003201
    reported_labels:
    - Clinical event
    ontology_label: Rhabdomyolysis
  - term_id: HP:0003236
    reported_labels:
    - Lab abnormality
    ontology_label: Elevated circulating creatine kinase activity
  - term_id: HP:0002913
    reported_labels:
    - Lab / sign
    ontology_label: Myoglobinuria
  - term_id: HP:0001324
    reported_labels:
    - Physical sign
    ontology_label: Muscle weakness
  - term_id: HP:0004322
    reported_labels:
    - Physical
    ontology_label: Short stature
  - term_id: HP:0001250
    reported_labels:
    - Neurological
    ontology_label: Seizure
  - term_id: HP:0002240
    reported_labels:
    - Sign
    ontology_label: Hepatomegaly
  - term_id: HP:0011800
    reported_labels:
    - Physical
    ontology_label: Midface retrusion
  - term_id: GO:0005829
    reported_labels:
    - GO cellular component:** cytosol
    - Subcellular:** cytosol
    ontology_label: cytosol
  labels_variant: 1
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
  path: Glycogen_Storage_Disease_Due_To_Aldolase_A_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Glycogen_Storage_Disease_Due_To_Aldolase_A_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Glycogen Storage Disease Due To Aldolase A Deficiency
- **MONDO ID:** MONDO:0012747 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Glycogen Storage Disease Due To Aldolase A Deficiency** covering all of the
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

# Glycogen Storage Disease Type XII (Aldolase A Deficiency): A Comprehensive Disease Profile

**Disease:** Glycogen Storage Disease Due To Aldolase A Deficiency (GSD XII)
**MONDO ID:** MONDO:0012747 · **OMIM:** #611881 · **ORPHA:** 57 · **ICD-10:** E74.0
**Gene:** *ALDOA* (HGNC:414; NCBI Gene 226; 16p11.2; UniProt P04075; EC 4.1.2.13)
**Category:** Mendelian (autosomal recessive inborn error of glycolysis)

---

## Summary

Glycogen Storage Disease type XII (GSD XII), also called **aldolase A deficiency**, is an ultra-rare autosomal-recessive inborn error of glycolysis. It is caused by biallelic loss-of-function or destabilizing (thermolabile) mutations in *ALDOA*, the gene encoding **fructose-1,6-bisphosphate aldolase A** on chromosome 16p11.2. Aldolase A (EC 4.1.2.13) is the sole aldolase isozyme expressed in erythrocytes and skeletal muscle, where it catalyzes the fourth reaction of glycolysis — the reversible cleavage of fructose-1,6-bisphosphate (F-1,6-BP) into dihydroxyacetone phosphate (DHAP) and glyceraldehyde-3-phosphate (GAP). Because red blood cells and, during metabolic stress, skeletal muscle depend heavily on glycolytic ATP, loss of aldolase A activity produces energy failure in these two tissues.

The clinical hallmark is a combination of **chronic non-spherocytic hemolytic anemia** and **fever- or exercise-triggered rhabdomyolysis/myoglobinuria**, with variable multisystem involvement that can include developmental delay/intellectual disability, short stature, dysmorphic facies, hepatomegaly, seizures/epilepsy, and — in the most severe neonatal-onset cases — asphyxia, myasthenia, and myocardial damage. A defining molecular feature of many pathogenic variants is **thermolability**: the mutant enzyme is functional at normal body temperature but destabilizes during febrile episodes, which mechanistically explains why fever triggers acute muscle breakdown. In at least one family a thermolabile variant caused isolated fever-induced rhabdomyolysis without any hemolytic anemia, demonstrating tissue-specific vulnerability.

Fewer than ~15 families have been reported worldwide since the first clinical description in 1977, so no reliable prevalence or incidence figures exist. Diagnosis rests on a suggestive biochemical/clinical picture (reticulocytosis, low haptoglobin, elevated LDH/bilirubin; elevated creatine kinase and myoglobinuria during triggers) confirmed by **molecular sequencing of *ALDOA***. Management is entirely supportive — aggressive fever control and antipyresis, avoidance of fasting/exercise triggers, transfusion and splenectomy for anemia, and hydration/renal protection during rhabdomyolysis. A ketogenic diet and in-vitro chemical chaperone rescue (arginine) have been proposed as experimental approaches but no curative therapy exists.

---

## Key Findings

### Finding 1 — GSD XII is caused by biallelic *ALDOA* mutations producing a thermolabile aldolase A enzyme

GSD XII is inherited in an autosomal-recessive manner; affected individuals carry two pathogenic *ALDOA* alleles while heterozygous parents are clinically unaffected. The first molecularly defined case, reported by Kishi and colleagues in 1987 ([PMID: 2825199](https://pubmed.ncbi.nlm.nih.gov/2825199/)), carried a homozygous **c.386A>G (p.Asp128Gly)** substitution. This variant produces a **highly thermolabile erythrocyte enzyme**, a conclusion confirmed by recombinant expression in *E. coli*: *"the 128th amino acid, aspartic acid, was replaced with glycine (GAT to GGT)."* Subsequent site-directed-mutagenesis work ([PMID: 2229018](https://pubmed.ncbi.nlm.nih.gov/2229018/)) established that aspartate at position 128 is required for thermal stability, since substitution rendered the enzyme thermolabile and susceptible to tryptic digestion, with CD spectra revealing conformational change.

The variant spectrum has since broadened. Yao et al. (2004; [PMID: 14615364](https://pubmed.ncbi.nlm.nih.gov/14615364/)) described a severe compound-heterozygous case: *"The paternal allele encoded a nonsense mutation, Arg303X, in the enzyme-active site. The maternal allele encoded a missense mutation, Cys338Tyr, predicted to cause enzyme instability."* More recent reports added **c.971C>T (p.Ala324Val)** (Kara 2021; [PMID: 34171939](https://pubmed.ncbi.nlm.nih.gov/34171939/)) and homozygous **c.619G>A (p.Glu207Lys)** in two affected brothers (Sun 2024; [PMID: 39223030](https://pubmed.ncbi.nlm.nih.gov/39223030/)), where *"the genotypes in the parents were heterozygous."*

**Variant table (reported pathogenic *ALDOA* alleles):**

| Variant (protein) | cDNA | Type | Zygosity reported | Key phenotype | Reference |
|---|---|---|---|---|---|
| p.Asp128Gly | c.386A>G | Missense (thermolabile) | Homozygous | Hemolytic anemia | [PMID: 2825199](https://pubmed.ncbi.nlm.nih.gov/2825199/) |
| p.Glu207Lys | c.619G>A | Missense | Homozygous | Severe neonatal, multi-organ | [PMID: 39223030](https://pubmed.ncbi.nlm.nih.gov/39223030/) |
| p.Arg303X | c.907C>T | Nonsense (active site) | Compound het | Severe, fatal rhabdomyolysis | [PMID: 14615364](https://pubmed.ncbi.nlm.nih.gov/14615364/) |
| p.Cys338Tyr | c.1013G>A | Missense (destabilizing) | Compound het | Severe | [PMID: 14615364](https://pubmed.ncbi.nlm.nih.gov/14615364/) |
| p.Ala324Val | c.971C>T | Missense | — | Hemolytic anemia + rhabdomyolysis | [PMID: 34171939](https://pubmed.ncbi.nlm.nih.gov/34171939/) |

Because loss-of-function and instability are the shared functional theme, the classification of these variants under ACMG/AMP criteria is **pathogenic/likely pathogenic**, supported by functional evidence (recombinant thermolability assays) and, for p.Arg303X, a null mechanism (nonsense at the active site).

### Finding 2 — Aldolase A is a homotetrameric TIM-barrel enzyme; destabilizing mutations disrupt tetramer assembly

Human muscle aldolase A is a **tetramer of four identical subunits**, each folded as an eight-stranded α/β (TIM) barrel with an active-site Schiff-base lysine near the barrel center. The crystal structure of human muscle aldolase (Gamblin 1990; [PMID: 2335208](https://pubmed.ncbi.nlm.nih.gov/2335208/)) established this architecture: *"The active protein is a tetramer of 4 identical subunits each of which is composed of an eight-stranded alpha/beta-barrel structure."*

The structural basis of disease was illuminated by the crystal structure of the D128V variant (an engineered mimic of the clinical D128G mutation) in rabbit muscle aldolase (Sherawat 2008; [PMID: 18453690](https://pubmed.ncbi.nlm.nih.gov/18453690/)): *"The D128V mutation causes aldolase to lose intermolecular contacts with the neighboring subunit at one of the two interfaces of the tetramer."* The mutation yields a catalytically active but destabilized **dimer** rather than the normal tetramer. This is consistent with the broader biophysical principle that oligomerization stabilizes aldolase and preserves the mobility of catalytic loops (elastic-network normal-mode analysis, [PMID: 25982518](https://pubmed.ncbi.nlm.nih.gov/25982518/)): oligomeric assembly *"not only stabilizes the aldolase structures… but also allows the enzyme to achieve the required dynamics for its functional loops."* Loss of a subunit interface therefore both destabilizes the protein (explaining thermolability) and can impair catalytic dynamics.

### Finding 3 — Clinical spectrum: fever/exercise-triggered rhabdomyolysis and hemolytic anemia with variable multisystem involvement

Across roughly ten published families, the recurring features are:

- **Chronic non-spherocytic hemolytic anemia** — often transfusion-dependent, frequently improved by splenectomy (Yao 2004; [PMID: 14615364](https://pubmed.ncbi.nlm.nih.gov/14615364/): *"transfusion-dependent anemia until splenectomy at age 3 and increasing muscle weakness, with death at age 4 associated with rhabdomyolysis and hyperkalemia"*).
- **Episodic rhabdomyolysis / myoglobinuria** — triggered by febrile illness or exercise (Mamoune 2014; [PMID: 25392908](https://pubmed.ncbi.nlm.nih.gov/25392908/): *"Myoglobinuria was always triggered by febrile illnesses. We show that the underlying mechanism involves an exacerbation of aldolase A deficiency at high temperatures that affected myoblasts but not erythrocytes."*).
- **Muscle weakness**, sometimes progressive (Yao 2004; [PMID: 14615364](https://pubmed.ncbi.nlm.nih.gov/14615364/)).
- **Developmental/neurological features** — developmental delay, intellectual disability, short stature, dysmorphic (midfacial hypoplasia) facies, hepatomegaly (Lowry 1977; [PMID: 890096](https://pubmed.ncbi.nlm.nih.gov/890096/)).
- **Newly expanded phenotypes** — epilepsy/seizures (Santoro 2022; [PMID: 35246226](https://pubmed.ncbi.nlm.nih.gov/35246226/)) and severe neonatal onset with asphyxia, myasthenia, myocardial damage, and anemia (Sun 2024; [PMID: 39223030](https://pubmed.ncbi.nlm.nih.gov/39223030/)).

Crucially, the phenotype can dissociate: a thermolabile mutant caused **isolated fever-induced recurrent rhabdomyolysis without hemolytic anemia** ([PMID: 25392908](https://pubmed.ncbi.nlm.nih.gov/25392908/)), because thermolability affected myoblasts but not erythrocytes — direct evidence of tissue-specific vulnerability and of variable expressivity.

**Phenotype table with suggested HPO terms:**

| Phenotype | Type | HPO term | Onset / severity | Frequency (qualitative) |
|---|---|---|---|---|
| Non-spherocytic hemolytic anemia | Lab / clinical sign | HP:0004804 | Childhood; mild–severe (transfusion-dependent) | Common (cardinal) |
| Rhabdomyolysis (fever/exercise) | Clinical event | HP:0003201 | Childhood; episodic, severe | Common (cardinal) |
| Elevated creatine kinase | Lab abnormality | HP:0003236 | With episodes | Common |
| Myoglobinuria | Lab / sign | HP:0002913 | With episodes | Common |
| Muscle weakness | Physical sign | HP:0001324 | Childhood; variable/progressive | Variable |
| Developmental delay / intellectual disability | Neurodevelopmental | HP:0001263 / HP:0001249 | Childhood | Subset |
| Short stature | Physical | HP:0004322 | Childhood | Subset |
| Seizures / epilepsy | Neurological | HP:0001250 | Childhood | Rare/newly reported |
| Hepatomegaly | Sign | HP:0002240 | Childhood | Subset |
| Facial dysmorphism / midface hypoplasia | Physical | HP:0011800 | Congenital | Subset |

### Finding 4 — Pathophysiology: aldolase A deficiency blocks step 4 of glycolysis, causing ATP-depletion energy failure

Aldolase A (EC 4.1.2.13) catalyzes the **reversible cleavage of fructose-1,6-bisphosphate into DHAP and glyceraldehyde-3-phosphate** — the fourth step of glycolysis (Yao 2004; [PMID: 14615364](https://pubmed.ncbi.nlm.nih.gov/14615364/): *"converts fructose-1,6-bisphosphate to dihydroxyacetone phosphate and glyceraldehyde-3-phosphate"*; Papadopoulos 2021; [PMID: 33665120](https://pubmed.ncbi.nlm.nih.gov/33665120/)). Because it is the **sole aldolase isozyme in erythrocytes and skeletal muscle**, its deficiency directly lowers glycolytic ATP output in those tissues.

- **Red blood cells** depend entirely on glycolysis for ATP (they lack mitochondria). Reduced/thermolabile aldolase shortens red-cell lifespan → **chronic non-spherocytic hemolytic anemia**.
- **Skeletal muscle** relies heavily on glycolysis during febrile or exertional catabolic states. Thermolabile enzyme collapse during fever produces acute energy failure → **rhabdomyolysis** ([PMID: 25392908](https://pubmed.ncbi.nlm.nih.gov/25392908/)).

Upstream substrate (F-1,6-BP) and glycolytic intermediates accumulate, and glycogen accumulates in muscle — the reason the disorder is classified as a glycogen storage disease (GSD XII) despite being an enzymopathy of glycolysis rather than glycogen breakdown per se. GSD XII sits within the broader family of muscle glycolytic-defect myopathies (PFK/Tarui, PGAM2, β-enolase, aldolase A) reviewed by Vissing and colleagues ([PMID: 30397902](https://pubmed.ncbi.nlm.nih.gov/30397902/)), in which higher-intensity exercise provokes cramps and rhabdomyolysis and pre-exercise carbohydrate can *worsen* glycolytic (as opposed to glycogenolytic) defects.

### Finding 5 — *ALDOA* gene identity, tissue expression, and a distinct oncologic (gain-of-expression) context

*ALDOA* (HGNC:414; NCBI Gene 226; chromosome 16p11.2; UniProt P04075; EC 4.1.2.13) encodes fructose-bisphosphate aldolase A, the predominant/sole isozyme in skeletal muscle and erythrocytes; *ALDOB* (liver/kidney) and *ALDOC* (brain) are the paralogous isozymes ([PMID: 33665120](https://pubmed.ncbi.nlm.nih.gov/33665120/): *"Aldolase A (ALDOA), is the predominant isoform of aldolase in skeletal muscle and erythrocytes that catalyzes the reversible…"*).

Importantly, the Mendelian **loss-of-function** disease is mechanistically opposite to the **gain-of-expression** role of ALDOA in cancer. Under hypoxia, HIF-1α drives ALDOA overexpression, which acts as a glycolytic driver and "moonlighting" protein interacting with Wnt/β-catenin, EGFR/MAPK, Akt, and cytoskeletal partners, correlating with poor prognosis (Niu 2021; [PMID: 33813748](https://pubmed.ncbi.nlm.nih.gov/33813748/): *"we identified aldolase A (ALDOA), a key enzyme in glycolysis and gluconeogenesis, as an essential driver for HCC cell growth under hypoxia"*; Tang 2024; [PMID: 39120781](https://pubmed.ncbi.nlm.nih.gov/39120781/): *"these enzymes also have various pathological and physiological functions through distinct signaling pathways such as Wnt/β-catenin, EGFR/MAPK, Akt, and HIF-1α"*). This cancer literature is included for gene-annotation completeness only; it is **not** part of the GSD XII disease mechanism.

### Finding 6 — Diagnosis relies on molecular *ALDOA* sequencing after a suggestive biochemical picture

Diagnostic clues combine (1) chronic non-spherocytic hemolytic anemia (reticulocytosis, low haptoglobin, elevated LDH and unconjugated bilirubin) and (2) episodic rhabdomyolysis with elevated creatine kinase and myoglobinuria during fever/exercise ([PMID: 14615364](https://pubmed.ncbi.nlm.nih.gov/14615364/); [PMID: 34171939](https://pubmed.ncbi.nlm.nih.gov/34171939/); [PMID: 25392908](https://pubmed.ncbi.nlm.nih.gov/25392908/)). Reduced/thermolabile erythrocyte aldolase A activity can be demonstrated biochemically but the assay is not widely available. Definitive diagnosis is by **molecular sequencing of *ALDOA*** (Kara 2021; [PMID: 34171939](https://pubmed.ncbi.nlm.nih.gov/34171939/): *"Diagnosis should be confirmed by the mutation analysis of ALDOA gene."*). In practice, whole-exome sequencing or hereditary-anemia / metabolic-myopathy gene panels are the pragmatic route.

**Differential diagnosis** spans the other glycolytic erythroenzymopathies and metabolic myopathies:

| Condition | Gene | Distinguishing feature |
|---|---|---|
| Pyruvate kinase deficiency | *PKLR* | Most common glycolytic hemolytic anemia; no rhabdomyolysis ([PMID: 30681718](https://pubmed.ncbi.nlm.nih.gov/30681718/)) |
| Phosphofructokinase / Tarui (GSD VII) | *PFKM* | Exertional myopathy + hemolysis; carbohydrate worsens ([PMID: 30397902](https://pubmed.ncbi.nlm.nih.gov/30397902/)) |
| Triosephosphate isomerase deficiency | *TPI1* | Hemolysis + severe neurological disease |
| Phosphoglycerate kinase deficiency | *PGK1* | X-linked; hemolysis + myopathy + CNS |
| Hexokinase deficiency | *HK1* | Hemolysis ± neurological ([PMID: 33361148](https://pubmed.ncbi.nlm.nih.gov/33361148/)) |
| McArdle disease (GSD V) | *PYGM* | Exertional rhabdomyolysis; no hemolysis ([PMID: 30397902](https://pubmed.ncbi.nlm.nih.gov/30397902/)) |
| CPT II deficiency | *CPT2* | Fasting/exercise rhabdomyolysis; no hemolysis |

### Finding 7 — Inheritance, epidemiology, and management

Inheritance is **autosomal recessive**: affected individuals carry two mutant alleles and heterozygous parents are unaffected ([PMID: 39223030](https://pubmed.ncbi.nlm.nih.gov/39223030/); consanguineous parents in [PMID: 890096](https://pubmed.ncbi.nlm.nih.gov/890096/)). The disorder is **ultra-rare** — fewer than ~15 families reported worldwide since 1977, and Orphanet classifies it as ultra-rare (Kara 2021; [PMID: 34171939](https://pubmed.ncbi.nlm.nih.gov/34171939/): *"an ultra rare autosomal recessively inherited GSD"*). No true prevalence or incidence figures are available. Both sexes are affected; consanguinity and founder homozygosity are noted in several families.

**Management is entirely supportive** — there is no curative therapy:

- Aggressive fever control / antipyresis and avoidance of fasting and strenuous exercise (the main triggers).
- Red-cell transfusions and splenectomy for hemolytic anemia.
- Aggressive hydration and renal protection during rhabdomyolysis episodes.
- Experimental/nutritional strategies: a **ketogenic diet** has been proposed to supply an alternative energy substrate to muscle and neurons (Santoro 2022; [PMID: 35246226](https://pubmed.ncbi.nlm.nih.gov/35246226/): *"we propose a new therapeutic approach based on ketogenic diet in order to supply an energetic substrate for skeletal muscle and neurons"*); and **arginine** rescued mutant enzyme activity in vitro as a chemical chaperone ([PMID: 25392908](https://pubmed.ncbi.nlm.nih.gov/25392908/)).

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic *ALDOA* mutation** (missense/nonsense; e.g., D128G, E207K, R303X, C338Y, A324V) → altered aldolase A polypeptide. *(demonstrated: sequencing across families)*
2. The mutation **disrupts an intersubunit interface / destabilizes the fold** → the enzyme fails to assemble a stable homotetramer, forming a destabilized dimer, and/or is intrinsically thermolabile. *(demonstrated structurally for D128V, [PMID: 18453690](https://pubmed.ncbi.nlm.nih.gov/18453690/); biochemically for D128G, [PMID: 2229018](https://pubmed.ncbi.nlm.nih.gov/2229018/))*
3. Thermolability **leads to loss of catalytic activity, worsened at elevated temperature** (fever) → the fourth step of glycolysis (F-1,6-BP → DHAP + GAP) is blocked. *(demonstrated: [PMID: 25392908](https://pubmed.ncbi.nlm.nih.gov/25392908/))*
4. Blocked glycolysis **results in reduced ATP production** in the two tissues where ALDOA is the only aldolase — erythrocytes and skeletal muscle. *(inferred from enzymology + tissue expression)*

   **Branch A — erythrocytes:** ATP depletion **shortens red-cell lifespan** → chronic non-spherocytic hemolytic anemia → reticulocytosis, low haptoglobin, high LDH/bilirubin; splenic clearance of damaged cells (splenectomy helps). *(demonstrated clinically)*

   **Branch B — skeletal muscle:** during fever or exercise, thermolabile-enzyme collapse **causes acute energy failure and myofiber breakdown** → rhabdomyolysis, elevated CK, myoglobinuria → risk of hyperkalemia and acute kidney injury. Glycogen accumulates upstream (hence "GSD"). *(demonstrated clinically; [PMID: 14615364](https://pubmed.ncbi.nlm.nih.gov/14615364/))*

   **Branch C — variable multisystem:** in severe genotypes, energy failure may extend to neurons (developmental delay, seizures), heart (myocardial damage), and growth (short stature, dysmorphism). *(inferred / associative; [PMID: 39223030](https://pubmed.ncbi.nlm.nih.gov/39223030/), [PMID: 35246226](https://pubmed.ncbi.nlm.nih.gov/35246226/))*

```
   ALDOA mutation (biallelic)
            │
            ▼
   Destabilized / thermolabile aldolase A
   (tetramer → dimer; loss of interface)
            │  worsens with fever ↑T
            ▼
   Glycolysis step 4 blocked
   (F-1,6-BP ⟶ DHAP + GAP fails)
            │
            ▼
   ATP depletion in ALDOA-only tissues
        ┌───────────────┼─────────────────┐
        ▼               ▼                 ▼
   RBC (no mito)   Skeletal muscle    CNS/heart/growth
   hemolytic       fever/exercise-    (severe genotypes)
   anemia          triggered          DD, seizures,
   (HP:0004804)    rhabdomyolysis     myocardial damage
                   (HP:0003201)
```

### Upstream vs downstream

- **Upstream (initiating):** *ALDOA* genotype and the resulting protein-stability defect.
- **Central node:** temperature-dependent glycolytic block and ATP depletion.
- **Downstream (clinical):** hemolysis, rhabdomyolysis, and secondary organ effects — all consequences of the same energetic lesion but with tissue-specific thresholds that explain phenotypic dissociation (e.g., muscle-only disease when a variant is thermolabile in myoblasts but not erythrocytes).

### Ontology annotations

- **Gene/protein:** *ALDOA* (HGNC:414), UniProt P04075.
- **GO biological process:** glycolytic process (GO:0006096), canonical glycolysis (GO:0061621), fructose-bisphosphate aldolase activity (GO:0004332).
- **GO cellular component:** cytosol (GO:0005829).
- **Cell types (CL):** erythrocyte (CL:0000232), skeletal muscle fiber / myoblast (CL:0000188, CL:0000515).
- **Anatomy (UBERON):** blood (UBERON:0000178), skeletal muscle tissue (UBERON:0001134); secondary — spleen (UBERON:0002106), kidney (UBERON:0002113), liver (UBERON:0002107), heart (UBERON:0000948), brain (UBERON:0000955).
- **Chemical entities (CHEBI):** fructose-1,6-bisphosphate (CHEBI:78682), dihydroxyacetone phosphate (CHEBI:57642), glyceraldehyde-3-phosphate (CHEBI:59776), ATP (CHEBI:30616).
- **Treatment (NCIT):** blood transfusion (NCIT:C15326), splenectomy (NCIT:C51749), ketogenic diet (NCIT:C92955).

---

## Section-by-Section Detail

### 1. Disease Information
Aldolase A deficiency (GSD XII) is a Mendelian metabolic disorder defined by biallelic *ALDOA* pathogenic variants. Identifiers: MONDO:0012747; OMIM #611881; ORPHA:57; ICD-10 E74.0. Synonyms: "glycogen storage disease type XII", "GSD 12", "ALDOA deficiency", "red-cell/muscle aldolase deficiency", "hereditary aldolase A deficiency". Information is derived from **aggregated disease-level resources** plus **individual case reports** (there is no EHR-scale dataset given the rarity).

### 2. Etiology
The sole cause is genetic — biallelic loss-of-function/destabilizing *ALDOA* variants. There is **no environmental or infectious cause**. Recognized **triggers** of acute episodes (a true gene–environment interaction) are **febrile illness, strenuous exercise, and fasting**, which precipitate rhabdomyolysis by exacerbating the enzyme's thermolability/energetic marginality ([PMID: 25392908](https://pubmed.ncbi.nlm.nih.gov/25392908/)). Consanguinity is a risk factor for homozygosity ([PMID: 890096](https://pubmed.ncbi.nlm.nih.gov/890096/)). No protective genetic or environmental factors are established.

### 3. Phenotypes
See Finding 3 and the HPO table above.

### 4. Genetic / Molecular Information
Causal gene *ALDOA* (16p11.2). Pathogenic variants are predominantly **missense** (thermolabile/destabilizing) with at least one **nonsense** allele (R303X). Functional consequence is **loss of function** via protein instability / impaired tetramer assembly. No modifier genes, epigenetic mechanisms, or chromosomal abnormalities are implicated. Allele frequencies for these private variants are effectively absent from gnomAD.

### 5. Environmental Information
None causal. Fever, exercise, and fasting are episode triggers (see Etiology). No toxins, radiation, occupational exposures, or infectious agents are involved.

### 6. Mechanism / Pathophysiology
See the ordered causal chain above.

### 7. Anatomical Structures Affected
- **Primary organs/tissues:** blood/erythrocytes (UBERON:0000178; CL:0000232) and skeletal muscle (UBERON:0001134; CL:0000188).
- **Secondary involvement:** spleen (hemolysis sequestration; UBERON:0002106), kidney (myoglobinuric AKI; UBERON:0002113), liver (hepatomegaly; UBERON:0002107), heart (myocardial damage in severe cases; UBERON:0000948), brain (developmental delay/seizures; UBERON:0000955).
- **Body systems:** hematologic, musculoskeletal; secondarily renal, hepatic, cardiovascular, nervous.
- **Subcellular:** cytosol (GO:0005829), where glycolysis occurs.
- **Lateralization:** systemic/bilateral (not applicable as a focal lesion).

### 8. Temporal Development
Onset ranges from **neonatal/congenital** (severe multi-organ cases; [PMID: 39223030](https://pubmed.ncbi.nlm.nih.gov/39223030/)) to **childhood**. Course is **chronic and lifelong**, punctuated by **episodic** acute rhabdomyolytic crises triggered by fever/exercise. Hemolytic anemia is chronic and may be transfusion-dependent until splenectomy. Critical intervention windows are during febrile illnesses (antipyresis) and metabolic stress.

### 9. Inheritance and Population
Autosomal recessive; ultra-rare (<15 families). No prevalence/incidence, sex ratio, or founder-population data beyond scattered consanguineous families. Penetrance appears complete in biallelic carriers; **expressivity is highly variable**. Carrier frequency is unknown but presumed very low.

### 10. Diagnostics
Biochemistry: hemolysis panel (reticulocytes↑, haptoglobin↓, LDH↑, bilirubin↑) and, during crises, CK↑↑ and myoglobinuria. Erythrocyte aldolase activity/thermolability assay (specialized). **Confirmatory test: *ALDOA* sequencing** (WES or hereditary-anemia/metabolic-myopathy panels). Differential diagnosis table above.

### 11. Outcome / Prognosis
Highly variable. Mild cases survive into adulthood with supportive care; severe compound-heterozygous or neonatal-onset cases can be **fatal in early childhood** (e.g., death at age 4 from rhabdomyolysis/hyperkalemia, [PMID: 14615364](https://pubmed.ncbi.nlm.nih.gov/14615364/)). No quantitative survival statistics exist. Main morbidity drivers: recurrent rhabdomyolysis (renal risk), transfusion-dependent anemia, and neurodevelopmental impairment in a subset.

### 12. Treatment
Entirely supportive (see Finding 7). NCIT: blood transfusion (C15326), splenectomy (C51749), ketogenic diet (C92955). Experimental: ketogenic diet ([PMID: 35246226](https://pubmed.ncbi.nlm.nih.gov/35246226/)), arginine chemical chaperone ([PMID: 25392908](https://pubmed.ncbi.nlm.nih.gov/25392908/)). No approved pharmacotherapy, gene therapy, or enzyme replacement.

### 13. Prevention
Primary prevention is **genetic counseling** for at-risk/consanguineous families, with carrier testing and prenatal/preimplantation options once familial variants are known. Tertiary prevention (preventing crises/complications): antipyresis, trigger avoidance, prompt hydration during illness. No immunization or population screening applies.

### 14. Other Species / Natural Disease
Human orthologue *Aldoa* exists in mouse (NCBI Gene 11674) and other vertebrates, but **no naturally occurring animal disease** is documented. Aldolase is broadly conserved (structural/mechanistic studies exist in rabbit, parasites, bacteria, and yeast), but these are enzymology surrogates, not disease models. No zoonotic relevance.

### 15. Model Organisms
No faithful published knock-in mouse recapitulating the deficiency. Experimental systems: (1) **recombinant human aldolase A variants** in *E. coli* (thermolability characterization; [PMID: 2229018](https://pubmed.ncbi.nlm.nih.gov/2229018/)), (2) **patient-derived myoblasts** ([PMID: 25392908](https://pubmed.ncbi.nlm.nih.gov/25392908/)), and (3) **rabbit muscle aldolase D128V crystal structures** as a structural surrogate ([PMID: 18453690](https://pubmed.ncbi.nlm.nih.gov/18453690/)). A constitutive *Aldoa* knockout is predicted to be embryonic-lethal, limiting straightforward whole-animal modeling.

---

## Evidence Base

| PMID | Study / type | How it supports the profile |
|---|---|---|
| [2825199](https://pubmed.ncbi.nlm.nih.gov/2825199/) | Kishi 1987 — first molecular case (human clinical + in vitro) | First pathogenic *ALDOA* missense (D128G) causing a thermolabile enzyme |
| [2229018](https://pubmed.ncbi.nlm.nih.gov/2229018/) | Recombinant D128G characterization (in vitro) | Asp128 required for thermal stability; mutant thermolabile, trypsin-susceptible, conformationally altered |
| [14615364](https://pubmed.ncbi.nlm.nih.gov/14615364/) | Yao 2004 — compound het case (human clinical) | R303X/C338Y; severe transfusion-dependent anemia + fatal rhabdomyolysis; defines enzymatic reaction |
| [25392908](https://pubmed.ncbi.nlm.nih.gov/25392908/) | Mamoune 2014 (human clinical + in vitro) | Thermolabile mutant → fever-induced rhabdomyolysis without hemolysis; tissue-specific thermolability; arginine rescue |
| [34171939](https://pubmed.ncbi.nlm.nih.gov/34171939/) | Kara 2021 — new case + review (human clinical) | Novel A324V; ultra-rare AR; molecular *ALDOA* testing is confirmatory |
| [39223030](https://pubmed.ncbi.nlm.nih.gov/39223030/) | Sun 2024 — two brothers (human clinical) | Homozygous E207K; severe neonatal multi-organ phenotype; AR inheritance confirmed in parents |
| [35246226](https://pubmed.ncbi.nlm.nih.gov/35246226/) | Santoro 2022 — new phenotype (human clinical) | Epilepsy + rhabdomyolysis; proposes ketogenic-diet therapy |
| [890096](https://pubmed.ncbi.nlm.nih.gov/890096/) | Lowry 1977 — first clinical description | Growth/developmental retardation, midface hypoplasia, hepatomegaly; consanguineous parents |
| [2335208](https://pubmed.ncbi.nlm.nih.gov/2335208/) | Gamblin 1990 — human aldolase crystal structure | Homotetrameric TIM-barrel architecture |
| [18453690](https://pubmed.ncbi.nlm.nih.gov/18453690/) | Sherawat 2008 — D128V variant structure | Structural mechanism: mutation abolishes a tetramer interface → destabilized dimer |
| [25982518](https://pubmed.ncbi.nlm.nih.gov/25982518/) | Aldolase dynamics (computational) | Oligomerization stabilizes structure and preserves catalytic-loop dynamics |
| [33665120](https://pubmed.ncbi.nlm.nih.gov/33665120/) | Papadopoulos 2021 — review | Gene/protein identity, tissue distribution, reaction |
| [30397902](https://pubmed.ncbi.nlm.nih.gov/30397902/) | Vissing — glycogen-metabolism myopathies review | Places GSD XII in the glycolytic-myopathy family; management principles |
| [33813748](https://pubmed.ncbi.nlm.nih.gov/33813748/) / [39120781](https://pubmed.ncbi.nlm.nih.gov/39120781/) | ALDOA in cancer | Contrasting gain-of-expression context (gene annotation only) |

**Evidence-source composition:** the GSD XII literature is dominated by **single-family human clinical case reports** supplemented by **in-vitro recombinant enzyme studies** and **X-ray crystallography** (largely on rabbit muscle aldolase as a structural surrogate). No population cohorts, natural-history studies, or faithful animal models of the deficiency exist.

---

## Limitations and Knowledge Gaps

1. **Extreme rarity → weak epidemiology.** With <15 families, all prevalence, penetrance, expressivity, carrier-frequency, and sex-ratio statements are qualitative. Penetrance appears complete for biallelic carriers, but expressivity is highly variable and genotype–phenotype correlation is only partially defined.
2. **Genotype–phenotype correlation is incomplete.** Why some variants cause muscle-only disease, others hemolysis-only, and others severe multisystem disease is only partly explained by tissue-specific thermolability; the biophysical determinants deserve systematic study.
3. **No approved disease-directed therapy.** Ketogenic diet and arginine chaperone rescue are hypotheses from single reports and in-vitro work, not trial-validated.
4. **No faithful animal model**, limiting mechanistic and preclinical therapeutic work.
5. **Diagnostic biochemistry is not standardized/widely available** (erythrocyte aldolase thermolability assay), so diagnosis depends on access to sequencing.
6. **Literature retrieval limitation:** several relevant case reports lacked machine-readable abstracts, so some clinical details rest on secondary review summaries rather than primary abstract quotes.

---

## Proposed Follow-up Experiments / Actions

1. **Curate an international variant/phenotype registry.** Systematically collect all published *ALDOA* deficiency cases into a ClinVar-linked table with per-variant thermostability (Tm), tissue-specific activity, and phenotype, to build genotype–phenotype and thermolability–severity correlations.
2. **Recombinant thermostability panel.** Express each clinical variant (D128G, E207K, C338Y, A324V, R303X-null) and measure Tm, tetramer/dimer equilibrium (SEC-MALS), and activity at 37 °C vs 40 °C to quantitatively test the thermolability model and rank variant severity.
3. **Chemical-chaperone screen.** Extend the arginine finding ([PMID: 25392908](https://pubmed.ncbi.nlm.nih.gov/25392908/)) by screening osmolytes/pharmacological chaperones on patient myoblasts and recombinant enzyme, measuring rescue of activity and thermostability — a plausible repurposing route.
4. **Isogenic iPSC / knock-in model.** Introduce patient variants into iPSCs and differentiate to erythroid and myogenic lineages to model tissue-specific ATP failure and test ketogenic/substrate-supplementation and chaperone interventions.
5. **Small pilot of ketogenic diet or trigger-avoidance protocols** in known patients, with CK, hemolysis markers, and quality-of-life endpoints, coordinated through rare-disease networks.
6. **Structural work on the human (not rabbit) variants** to confirm interface disruption for E207K, C338Y, and A324V and to guide chaperone design.


## Artifacts

- [OpenScientist final report](Glycogen_Storage_Disease_Due_To_Aldolase_A_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Glycogen_Storage_Disease_Due_To_Aldolase_A_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 11 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0004804` (2 mentions) - the report calls it "Lab / clinical sign"; HP calls it **Congenital hemolytic anemia**
- `HP:0003201` (2 mentions) - the report calls it "Clinical event"; HP calls it **Rhabdomyolysis**
- `HP:0003236` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Elevated circulating creatine kinase activity**
- `HP:0002913` (1 mention) - the report calls it "Lab / sign"; HP calls it **Myoglobinuria**
- `HP:0001324` (1 mention) - the report calls it "Physical sign"; HP calls it **Muscle weakness**
- `HP:0004322` (1 mention) - the report calls it "Physical"; HP calls it **Short stature**
- `HP:0001250` (1 mention) - the report calls it "Neurological"; HP calls it **Seizure**
- `HP:0002240` (1 mention) - the report calls it "Sign"; HP calls it **Hepatomegaly**
- `HP:0011800` (1 mention) - the report calls it "Physical"; HP calls it **Midface retrusion**
- `GO:0005829` (2 mentions) - the report calls it "GO cellular component:** cytosol", "Subcellular:** cytosol"; GO calls it **cytosol**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006096` (1 mention) - the report calls it "GO biological process:** glycolytic process"; GO calls it **glycolytic process**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HGNC:414` - called "ALDOA", "Gene/protein:** *ALDOA"
- `GO:0005829` - called "GO cellular component:** cytosol", "Subcellular:** cytosol"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.