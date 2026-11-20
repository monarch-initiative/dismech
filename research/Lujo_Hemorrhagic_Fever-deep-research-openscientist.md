---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-03T19:33:19.712859'
end_time: '2026-11-03T19:48:35.568830'
duration_seconds: 915.86
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Lujo Hemorrhagic Fever
  mondo_id: MONDO:0017872
  category: Infectious
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: Zambian hemorrhagic fever
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 1800
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 25
reference_validation:
  total_references: 26
  verified: 26
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 5
  quotes_valid: 5
  relevance_assessed: 26
  on_topic: 23
  validator_version: 0.5.1
term_validation:
  total_terms: 46
  verified: 42
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 0
  labels_mismatched: 16
  mislabelled_terms:
  - term_id: HP:0001945
    reported_labels:
    - Symptom
    ontology_label: Fever
  - term_id: HP:0002315
    reported_labels:
    - Symptom
    ontology_label: Headache
  - term_id: HP:0003326
    reported_labels:
    - Symptom
    ontology_label: Myalgia
  - term_id: HP:0025439
    reported_labels:
    - Sign
    ontology_label: Pharyngitis
  - term_id: HP:0100749
    reported_labels:
    - Symptom
    ontology_label: Chest pain
  - term_id: HP:0002014
    reported_labels:
    - Symptom
    ontology_label: Diarrhea
  - term_id: HP:0000988
    reported_labels:
    - Sign
    ontology_label: Skin rash
  - term_id: HP:0011885
    reported_labels:
    - Sign
    ontology_label: Hemorrhage of the eye
  - term_id: HP:0000316
    reported_labels:
    - facial edema
    ontology_label: Hypertelorism
  - term_id: HP:0001892
    reported_labels:
    - Sign
    ontology_label: Abnormal bleeding
  - term_id: HP:0001873
    reported_labels:
    - Lab
    ontology_label: Thrombocytopenia
  - term_id: HP:0002910
    reported_labels:
    - Lab
    ontology_label: Elevated circulating hepatic transaminase concentration
  - term_id: HP:0031273
    reported_labels:
    - Sign
    ontology_label: Shock
  - term_id: HP:0005521
    reported_labels:
    - Lab/sign
    ontology_label: Disseminated intravascular coagulation
  - term_id: HP:0000707
    reported_labels:
    - Sign
    ontology_label: Abnormality of the nervous system
  - term_id: UBERON:0002113
    reported_labels:
    - Secondary involvement:** kidneys
    ontology_label: kidney
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Lujo_Hemorrhagic_Fever-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Lujo_Hemorrhagic_Fever-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lujo Hemorrhagic Fever
- **MONDO ID:** MONDO:0017872 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** Zambian hemorrhagic fever
- **Category:** Infectious

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Lujo Hemorrhagic Fever** covering all of the
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

# Lujo Hemorrhagic Fever: Comprehensive Disease Characterization

**Disease:** Lujo Hemorrhagic Fever (LHF) · **MONDO:** MONDO:0017872 · **Synonym:** Zambian hemorrhagic fever · **Category:** Infectious (viral hemorrhagic fever)

---

## Summary

**Lujo hemorrhagic fever is an infectious disease, not a Mendelian genetic disorder — it has no human causal gene.** Its causal agent is **Lujo virus (LUJV)**, a genetically divergent Old World mammarenavirus (family *Arenaviridae*, genus *Mammarenavirus*) first identified during a 2008 nosocomial outbreak in Southern Africa. The template field "Causal gene(s): not recorded" is therefore correct and expected: the relevant "gene" is viral, not host. LUJV is an enveloped, bisegmented, negative-sense/ambisense RNA virus whose full-genome phylogeny places it at the ancestral node of the Old World arenaviruses, almost equidistant from both the Old World (Lassa) and New World serogroups ([PMID: 19478873](https://pubmed.ncbi.nlm.nih.gov/19478873/)).

The entire recognized clinical experience with LHF derives from **a single 2008 outbreak of five cases** (an index patient air-evacuated from Lusaka, Zambia, to Johannesburg, South Africa, plus four healthcare workers infected through nosocomial transmission), with a **case fatality rate of 80% (4 of 5)**. The disease begins as a nonspecific febrile prodrome and progresses over roughly two weeks to a capillary-leak syndrome, disseminated intravascular coagulation (DIC), shock, and multi-organ failure — a course clinically indistinguishable from severe Lassa fever. Notably, overt major hemorrhage is uncommon despite the "hemorrhagic fever" label.

Mechanistically, LUJV is distinguished from all other arenaviruses by its **unique cell-entry pathway**: it uses **neuropilin-2 (NRP2)** as its primary cell-surface receptor and the tetraspanin **CD63** (critically, residue phenylalanine-143 in humans) as an intracellular fusion cofactor in the late endosome — a two-receptor "switch" paradigm analogous to Lassa virus's α-dystroglycan→LAMP1 switch. Its glycoprotein precursor (GPC) is matured by host **site-1 protease (S1P/SKI-1/MBTPS1)** at an RKLM motif, and the virus buds via Z-protein late domains independently of the canonical ESCRT machinery. Disease severity is driven primarily by **host immune dysregulation (cytokine storm)** rather than viral burden. There is **no approved vaccine or antiviral**; management rests on early ribavirin plus intensive supportive care and strict infection control, with numerous candidate countermeasures (CB1-antagonist entry inhibitors, the S1P inhibitor PF-429242, griffithsin, and the MOPEVAC vaccine platform) remaining preclinical.

---

## Key Findings

### Finding 1 — LHF is caused by Lujo virus, a divergent Old World arenavirus; there is no human causal gene

Lujo virus is the etiologic agent of LHF. It is an enveloped, bisegmented negative-sense/ambisense RNA virus of the family *Arenaviridae*, genus *Mammarenavirus*. Full-genome analysis during its discovery showed LUJV to be "unique and branching off the ancestral node of the Old World arenaviruses," with a G1 glycoprotein sequence "highly diverse and almost equidistant from that of other Old World and New World arenaviruses" ([PMID: 19478873](https://pubmed.ncbi.nlm.nih.gov/19478873/)). This places LUJV outside both classical arenavirus serogroups. The name "Lujo" is a portmanteau of **Lu**saka and **Jo**hannesburg, the two cities linked by the 2008 outbreak. Because the disease is infectious, the "causal gene" fields (OMIM, HGNC, causal gene) are not applicable; the disease-level identifier is **MONDO:0017872**.

**Evidence quote:** *"Full genome analyses of LUJV showed it to be unique and branching off the ancestral node of the Old World arenaviruses. The virus G1 glycoprotein sequence was highly diverse and almost equidistant from that of other Old World and New World arenaviruses"* ([PMID: 19478873](https://pubmed.ncbi.nlm.nih.gov/19478873/)).

### Finding 2 — LUJV uses NRP2 as entry receptor and CD63 as intracellular fusion cofactor, distinct from all other arenaviruses

A genome-wide haploid genetic screen identified the transmembrane protein **neuropilin-2 (NRP2)** and the tetraspanin **CD63** as the host factors required for LUJV glycoprotein (GP)-mediated infection. LUJV GP1 binds the **N-terminal (a1/a2) domain of NRP2**, while CD63 stimulates pH-activated LUJV GP-mediated membrane fusion in the late endosome ([PMID: 29120745](https://pubmed.ncbi.nlm.nih.gov/29120745/)). This is mechanistically distinct from Old World arenaviruses (which use α-dystroglycan) and New World arenaviruses (which use transferrin receptor 1); pseudotype studies confirmed LUJV entry is independent of both α-dystroglycan and hTfR1, and depends instead on an unidentified receptor later shown to be NRP2, with additional dependence on Niemann-Pick C1 (NPC1) and cholesterol transport ([PMID: 24741091](https://pubmed.ncbi.nlm.nih.gov/24741091/)). Structural work defined the receptor-binding mode by X-ray crystallography of the GP1–NRP2 complex ([PMID: 30150732](https://pubmed.ncbi.nlm.nih.gov/30150732/)), and cryo-EM of the complete trimeric spike revealed a single NRP2 molecule bound at the apex via an unusual arginine-methionine interaction ([PMID: 39169025](https://pubmed.ncbi.nlm.nih.gov/39169025/)). The host-range determinant is a **phenylalanine at position 143 in the human CD63 large extracellular loop**, which is required for efficient membrane fusion and infection ([PMID: 35164564](https://pubmed.ncbi.nlm.nih.gov/35164564/)).

**Evidence quotes:** *"A genome-wide haploid genetic screen identified the transmembrane protein neuropilin 2 (NRP2) and tetraspanin CD63 as factors for LUJV GP-mediated infection. LUJV GP binds the N-terminal domain of NRP2, while CD63 stimulates pH-activated LUJV GP-mediated membrane fusion"* ([PMID: 29120745](https://pubmed.ncbi.nlm.nih.gov/29120745/)); *"a phenylalanine at position 143 in human CD63 was the key residue for efficient membrane fusion and VSVΔG\*-LUJV/GP infection"* ([PMID: 35164564](https://pubmed.ncbi.nlm.nih.gov/35164564/)).

### Finding 3 — Clinical course: febrile prodrome progressing to shock, DIC, and multi-organ failure

In the 2008 outbreak, illness "typically began with the abrupt onset of fever, malaise, headache, and myalgias followed successively by sore throat, chest pain, gastrointestinal symptoms, rash, minor hemorrhage, subconjunctival injection, and neck and facial swelling over the first week of illness. No major hemorrhage was noted." Neurological signs appeared late. "Shock and multi-organ system failure, often with evidence of disseminated intravascular coagulopathy, ensued in the second week, with death in four of the five cases." The single survivor received early ribavirin plus aggressive supportive care ([PMID: 25393244](https://pubmed.ncbi.nlm.nih.gov/25393244/)). Laboratory features closely mirror Lassa fever — fever, thrombocytopenia, and transaminitis — and the clinical syndrome is "remarkably similar to Lassa hemorrhagic fever," with fever, headache, vomiting, diarrhea, arthralgia, myalgia, and signs of hemorrhagic syndrome ([PMID: 29733163](https://pubmed.ncbi.nlm.nih.gov/29733163/)).

### Finding 4 — Host immune response, not viral burden, drives LHF severity

Two independent animal models converge on the conclusion that **host immune dysregulation determines outcome**. In cynomolgus macaques, LUJV caused mild non-lethal illness, and transcriptomics of PBMCs revealed a **72-hour delay** in the induction of inflammatory, antiviral, and cell-death gene programs compared with lethal Lassa infection ([PMID: 25520505](https://pubmed.ncbi.nlm.nih.gov/25520505/)). In strain 13/N guinea pigs, survival correlated with the immune response rather than viral titer: despite similarly high LUJV titers across lungs, liver, spleen, kidneys, and serum, young females survived with low inflammatory cytokines, whereas adults and young males died with cytokine storms featuring elevated IL-1β, IL-2, IL-6, and CXCL10 ([PMID: 41118368](https://pubmed.ncbi.nlm.nih.gov/41118368/)). This reveals both a central pathogenic mechanism (immunopathology) and age/sex disease modifiers.

**Evidence quotes:** *"survival outcomes strongly correlated with immune responses rather than viral burden. Adult animals and young males developed more severe clinical signs, heightened hematological and biochemical abnormalities, and pronounced cytokine storms, particularly elevated IL-1β, IL-2, IL-6, and CXCL10 levels"* ([PMID: 41118368](https://pubmed.ncbi.nlm.nih.gov/41118368/)); *"We detected a 72-h delay in the induction of host responses to infection during LUJV infection compared to that of the animals infected with LASV... particularly apparent among groups of genes promoting cell death"* ([PMID: 25520505](https://pubmed.ncbi.nlm.nih.gov/25520505/)).

### Finding 5 — Animal models: macaque (mild), guinea pig and STAT-1 KO mouse (partial lethal disease)

No single model fully reproduces fatal human LHF, but complementary systems exist. Cynomolgus macaques develop mild, non-lethal illness ([PMID: 25520505](https://pubmed.ncbi.nlm.nih.gov/25520505/)). Strain 13/N guinea pigs are "a promising model for LUJV pathogenesis," recapitulating hematologic/biochemical abnormalities and age/sex-dependent lethality ([PMID: 41118368](https://pubmed.ncbi.nlm.nih.gov/41118368/)). STAT-1-deficient mice develop a partially lethal disease in which "several key hematological, clinical chemistry, and histologic findings common to LHF disease are recapitulated" ([PMID: 42075721](https://pubmed.ncbi.nlm.nih.gov/42075721/)). Standard inbred mice and hamsters are relatively resistant because their CD63 lacks the human F143 residue required for efficient entry ([PMID: 35164564](https://pubmed.ncbi.nlm.nih.gov/35164564/)). Pseudotyped VSV bearing LUJV GP enables BSL-2 study of entry ([PMID: 24741091](https://pubmed.ncbi.nlm.nih.gov/24741091/); [PMID: 22396728](https://pubmed.ncbi.nlm.nih.gov/22396728/)).

### Finding 6 — Epidemiology: a single 2008 outbreak, 80% CFR, reservoir unknown, no approved countermeasures

"Lujo virus is a novel Old World arenavirus identified in Southern Africa in 2008 as the cause of a viral hemorrhagic fever (VHF) characterized by nosocomial transmission with a high case fatality rate of 80% (4/5 cases)" ([PMID: 27593704](https://pubmed.ncbi.nlm.nih.gov/27593704/)). The index patient from Lusaka, Zambia, was air-evacuated to Johannesburg, with secondary transmission to four healthcare workers. LUJV remains the only strain detected to date ([PMID: 24096270](https://pubmed.ncbi.nlm.nih.gov/24096270/)), and "LUJV remains poorly understood, with no approved treatments, vaccines, or known reservoir" ([PMID: 41118368](https://pubmed.ncbi.nlm.nih.gov/41118368/)). An arenaviral rodent reservoir is presumed but unidentified. Rapid RT-PCR assays were developed for molecular diagnosis ([PMID: 24096270](https://pubmed.ncbi.nlm.nih.gov/24096270/)). LUJV is a BSL-4 / WHO risk-group-4 pathogen.

### Finding 7 — GPC matured by site-1 protease at an RKLM motif; Z-protein drives ESCRT-independent budding

LUJV's glycoprotein precursor GPC is proteolytically cleaved by cellular **site-1 protease (S1P/SKI-1, gene MBTPS1)** at an **RKLM motif**, and the S1P inhibitor PF-429242 reduced LUJV production. The matrix protein Z **late (L) domains are required for efficient virus-like-particle release, but the virus buds independently of the canonical ESCRT factors Tsg101, ALIX/AIP1, and Vps4A/B** ([PMID: 26719243](https://pubmed.ncbi.nlm.nih.gov/26719243/)). Both the S1P maturation step and the Z-driven budding step represent druggable nodes.

**Evidence quotes:** *"LUJV GPC is cleaved by site 1 protease (S1P) at the RKLM motif, and treatment with the S1P inhibitor PF-429242 reduced LUJV production"* and *"The L domains in Z are required for efficient virus-like particle release, but Tsg101, ALIX/AIP1, and Vps4A/B are unnecessary for budding"* ([PMID: 26719243](https://pubmed.ncbi.nlm.nih.gov/26719243/)).

### Finding 8 — Multiple experimental anti-LUJV strategies; only ribavirin used clinically

Using VSV-LUJV/GP pseudotype entry screens, **cannabinoid receptor 1 (CB1) antagonists** rimonabant, AM251, and AM281 were identified as robust inhibitors of LUJV entry ([PMID: 37633192](https://pubmed.ncbi.nlm.nih.gov/37633192/)). FDA-approved drug-library screens identified additional entry inhibitors ([PMID: 34925303](https://pubmed.ncbi.nlm.nih.gov/34925303/)). A recombinant reporter-LUJV high-throughput platform identified six compounds with robust anti-LUJV activity, including agents with prior pan-arenavirus activity ([PMID: 34203149](https://pubmed.ncbi.nlm.nih.gov/34203149/)). The broad-spectrum lectin **griffithsin** blocks LUJV glycoprotein-mediated entry ([PMID: 42037406](https://pubmed.ncbi.nlm.nih.gov/42037406/)). Clinically, only **ribavirin** (with supportive care) has been used, in the single survivor ([PMID: 25393244](https://pubmed.ncbi.nlm.nih.gov/25393244/)). All targeted agents remain preclinical/investigational; none is approved for LHF.

**Evidence quote:** *"Cannabinoid receptor 1 (CB1) antagonists, such as rimonabant, AM251 and AM281, have been identified as robust inhibitors of LUJV entry"* ([PMID: 37633192](https://pubmed.ncbi.nlm.nih.gov/37633192/)).

### Finding 9 — Tissue injury follows shared VHF mechanisms; CD63 is LUJV's intracellular fusion cofactor analogous to LAMP1 for Lassa

Across arenaviral and filoviral hemorrhagic fevers, pathogenesis involves "deficiency of hepatic synthesis of coagulation factors owing to hepatocellular necrosis, cytokine storm, increased permeability by vascular endothelial growth factor, complement activation, and disseminated intravascular coagulation" ([PMID: 23121052](https://pubmed.ncbi.nlm.nih.gov/23121052/)). In a primate Lassa model, shock arose from "biochemical dysfunctions of platelets and endothelial cells," with loss of endothelial prostacyclin production and impaired platelet aggregation despite normal platelet counts ([PMID: 3543155](https://pubmed.ncbi.nlm.nih.gov/3543155/)). LUJV parallels Lassa mechanistically: both are Old World arenaviruses whose GPC first engages a cell-surface receptor, then switches to an intracellular factor for low-pH fusion. Lassa switches from α-dystroglycan to LAMP1 ([PMID: 29295909](https://pubmed.ncbi.nlm.nih.gov/29295909/)), whereas LUJV uses NRP2 then the tetraspanin CD63 (F143) ([PMID: 29120745](https://pubmed.ncbi.nlm.nih.gov/29120745/); [PMID: 35164564](https://pubmed.ncbi.nlm.nih.gov/35164564/)).

**Evidence quotes:** *"The pathogenic mechanisms... include deficiency of hepatic synthesis of coagulation factors owing to hepatocellular necrosis, cytokine storm, increased permeability by vascular endothelial growth factor, complement activation, and disseminated intravascular coagulation"* ([PMID: 23121052](https://pubmed.ncbi.nlm.nih.gov/23121052/)); *"A unique feature of LASV entry is a pH-dependent switch from a primary cell surface receptor (α-dystroglycan) to an endosomal receptor, lysosomal-associated membrane protein (Lamp1)"* ([PMID: 29295909](https://pubmed.ncbi.nlm.nih.gov/29295909/)).

### Finding 10 — NP exoribonuclease likely underlies delayed innate response; MOPEVAC is a candidate vaccine platform

Arenaviral nucleoproteins carry a conserved **DEDDH exoribonuclease (RNase) domain that suppresses type I interferon**; mutating the catalytic residues in Pichinde virus NP abolishes IFN suppression, causing high IFN induction and failure to replicate in IFN-competent cells and guinea pigs ([PMID: 25878103](https://pubmed.ncbi.nlm.nih.gov/25878103/)). By homology, this conserved mechanism provides a molecular basis for the ~72-hour delay in innate/antiviral gene induction in LUJV-infected macaques ([PMID: 25520505](https://pubmed.ncbi.nlm.nih.gov/25520505/)) and for the worsened disease in STAT-1-deficient mice ([PMID: 42075721](https://pubmed.ncbi.nlm.nih.gov/42075721/)). For prevention, a recombinant hyperattenuated Mopeia virus platform (**MOPEVAC**) expressing heterologous arenaviral glycoproteins has been developed as a pan-arenavirus vaccine strategy ([PMID: 29593043](https://pubmed.ncbi.nlm.nih.gov/29593043/)).

**Evidence quote:** *"Previous structural and functional analyses of arenavirus nucleoproteins (NPs) revealed a conserved DEDDH exoribonuclease (RNase) domain that is important for type I interferon (IFN) suppression"* ([PMID: 25878103](https://pubmed.ncbi.nlm.nih.gov/25878103/)).

---

## Report by Template Section

### 1. Disease Information
Lujo hemorrhagic fever is a severe, acute **viral hemorrhagic fever** caused by Lujo virus, an Old World mammarenavirus. The disease is defined at the disease level (not patient-EHR level); essentially all clinical knowledge derives from the aggregated five-case 2008 outbreak and subsequent experimental virology.
- **Mondo:** MONDO:0017872
- **ICD-10:** A96.8 (other arenaviral hemorrhagic fevers); **ICD-11:** arenaviral hemorrhagic fever grouping (1D60.Y)
- **OMIM:** Not applicable (infectious disease, no Mendelian locus)
- **Orphanet:** Listed among rare arenaviral/viral hemorrhagic fevers
- **MeSH:** "Hemorrhagic Fevers, Viral"; "Arenaviridae Infections"
- **Synonyms:** Lujo viral hemorrhagic fever; Zambian hemorrhagic fever
- **Pathogen taxonomy (NCBI Taxon):** Lujo mammarenavirus (taxid 649188); family Arenaviridae; genus Mammarenavirus

### 2. Etiology
**Primary cause:** infection with Lujo virus — an infectious, not genetic, etiology ([PMID: 19478873](https://pubmed.ncbi.nlm.nih.gov/19478873/)). **Risk factors** are exposure-based: close/nosocomial contact with an infected patient or body fluids. Four of the five known cases were healthcare workers infected caring for the index patient ([PMID: 27593704](https://pubmed.ncbi.nlm.nih.gov/27593704/)). No host genetic susceptibility or protective loci have been identified in humans. Experimental models reveal **age and sex as disease modifiers** (young females survived; adults and young males died in guinea pigs) ([PMID: 41118368](https://pubmed.ncbi.nlm.nih.gov/41118368/)). Host **STAT1/type I IFN signaling is protective**, as STAT1-deficient mice develop lethal disease ([PMID: 42075721](https://pubmed.ncbi.nlm.nih.gov/42075721/)). No gene–environment interaction data in humans exist (single small outbreak).

### 3. Phenotypes
| Phenotype | Type | Suggested HPO | Frequency / notes |
|---|---|---|---|
| Fever | Symptom | HP:0001945 | Universal, abrupt onset |
| Headache | Symptom | HP:0002315 | Early prodrome |
| Myalgia | Symptom | HP:0003326 | Early prodrome |
| Malaise/fatigue | Symptom | HP:0025406 / HP:0012378 | Early |
| Sore throat (pharyngitis) | Sign | HP:0025439 | Week 1 |
| Chest pain | Symptom | HP:0100749 | Week 1 |
| Diarrhea / GI symptoms | Symptom | HP:0002014 | Week 1 |
| Skin rash | Sign | HP:0000988 | Week 1 |
| Subconjunctival hemorrhage/injection | Sign | HP:0011885 | Week 1 |
| Facial/neck edema (swelling) | Sign | HP:0000316 (facial edema) | Distinctive late sign |
| Minor hemorrhage | Sign | HP:0001892 | Present; major hemorrhage absent |
| Thrombocytopenia | Lab | HP:0001873 | Lassa-like |
| Elevated transaminases | Lab | HP:0002910 | Transaminitis |
| Shock | Sign | HP:0031273 | Week 2, terminal |
| Disseminated intravascular coagulation | Lab/sign | HP:0005521 | Week 2, terminal |
| Multi-organ failure | Sign | HP:0011024 + multiorgan | Week 2, terminal |
| Neurological signs | Sign | HP:0000707 | Late |

Onset is **adult** in the documented cases, **acute**, and **rapidly progressive** over ~2 weeks. Severity is severe/fatal in 4/5 cases. Quality-of-life measures are not applicable given the acute, high-fatality course. (Clinical features: [PMID: 25393244](https://pubmed.ncbi.nlm.nih.gov/25393244/); [PMID: 29733163](https://pubmed.ncbi.nlm.nih.gov/29733163/).)

### 4. Genetic/Molecular Information
Not applicable in the human-host genetic sense — **no causal human gene, OMIM entry, or pathogenic germline variant**. The relevant molecular biology is viral: the bisegmented genome (L and S segments) encodes the RdRp (L), matrix protein Z, nucleoprotein (NP), and glycoprotein precursor (GPC → GP1/GP2 + stable signal peptide). Host factors functionally required for the viral life cycle (effectively the human "molecular interactors") include **NRP2** (HGNC:8005), **CD63** (HGNC:1692; critical residue F143), **MBTPS1/S1P** (HGNC:15456), and **NPC1** (HGNC:7897) ([PMID: 29120745](https://pubmed.ncbi.nlm.nih.gov/29120745/); [PMID: 35164564](https://pubmed.ncbi.nlm.nih.gov/35164564/); [PMID: 26719243](https://pubmed.ncbi.nlm.nih.gov/26719243/); [PMID: 24741091](https://pubmed.ncbi.nlm.nih.gov/24741091/)). No epigenetic or chromosomal abnormalities apply.

### 5. Environmental Information
The sole environmental/infectious factor is exposure to LUJV. The natural reservoir is **unknown** but presumed to be a rodent by analogy to other arenaviruses ([PMID: 41118368](https://pubmed.ncbi.nlm.nih.gov/41118368/)). Documented human-to-human spread was **nosocomial**, via contact with blood/body fluids ([PMID: 27593704](https://pubmed.ncbi.nlm.nih.gov/27593704/)). **Infectious agent:** Lujo mammarenavirus (NCBI taxid 649188).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating infection → clinical manifestation):**

1. LUJV is introduced via mucosal/percutaneous exposure to infected body fluids, **leading to** infection of permissive cells (dendritic cells, macrophages, endothelium inferred by analogy to Lassa).
2. LUJV GP1 binds the N-terminal domain of cell-surface **NRP2**, **resulting in** receptor-mediated endocytosis ([PMID: 29120745](https://pubmed.ncbi.nlm.nih.gov/29120745/); [PMID: 30150732](https://pubmed.ncbi.nlm.nih.gov/30150732/)).
3. In the acidifying late endosome, engagement of **CD63 (F143)** triggers pH-activated GP2-mediated membrane fusion (a receptor "switch" analogous to Lassa α-DG→LAMP1), **leading to** release of the ribonucleoprotein into the cytoplasm ([PMID: 35164564](https://pubmed.ncbi.nlm.nih.gov/35164564/); [PMID: 29295909](https://pubmed.ncbi.nlm.nih.gov/29295909/)). *(GPC was first primed by host S1P cleavage at RKLM during biogenesis — [PMID: 26719243](https://pubmed.ncbi.nlm.nih.gov/26719243/).)*
4. Viral replication proceeds; the NP **DEDDH exoribonuclease** degrades immunostimulatory RNA, **resulting in** suppression of type I interferon and a **~72-hour delay** in innate antiviral/inflammatory gene induction (inferred for LUJV from conserved arenaviral biology + macaque transcriptomics) ([PMID: 25878103](https://pubmed.ncbi.nlm.nih.gov/25878103/); [PMID: 25520505](https://pubmed.ncbi.nlm.nih.gov/25520505/)).
5. **BRANCH A (controlled response → survival):** an appropriately timed, measured immune response limits immunopathology → mild/non-lethal disease (macaques; young-female guinea pigs) ([PMID: 25520505](https://pubmed.ncbi.nlm.nih.gov/25520505/); [PMID: 41118368](https://pubmed.ncbi.nlm.nih.gov/41118368/)).
6. **BRANCH B (dysregulated response → death):** delayed-then-explosive **cytokine storm** (IL-1β, IL-2, IL-6, CXCL10) **leads to** systemic immunopathology ([PMID: 41118368](https://pubmed.ncbi.nlm.nih.gov/41118368/)).
7. Cytokines + **VEGF-mediated endothelial permeability** and endothelial/platelet biochemical dysfunction (loss of prostacyclin, impaired aggregation) **result in** capillary leak, facial/neck edema, and effusions ([PMID: 23121052](https://pubmed.ncbi.nlm.nih.gov/23121052/); [PMID: 3543155](https://pubmed.ncbi.nlm.nih.gov/3543155/)).
8. Hepatocellular injury/necrosis **leads to** deficient synthesis of coagulation factors; combined with consumptive coagulopathy, this **results in** **DIC** ([PMID: 23121052](https://pubmed.ncbi.nlm.nih.gov/23121052/)).
9. Capillary leak + DIC + vasoplegia **lead to** distributive/hypovolemic **shock** and **multi-organ failure**, the terminal events in week 2 ([PMID: 25393244](https://pubmed.ncbi.nlm.nih.gov/25393244/)).

**Upstream vs downstream:** viral entry/replication and IFN suppression are upstream; cytokine storm, endothelial/platelet dysfunction, and DIC are downstream effectors of tissue injury. **Key GO terms:** viral entry into host cell (GO:0046718), receptor-mediated endocytosis (GO:0006898), fusion of virus membrane with host endosome membrane (GO:0039654), negative regulation of type I interferon production (GO:0032480), inflammatory response (GO:0006954), blood coagulation (GO:0007596), cytokine production (GO:0001816). **Key CL terms:** endothelial cell (CL:0000115), macrophage (CL:0000235), dendritic cell (CL:0000451), hepatocyte (CL:0000182), platelet (CL:0000233), NK cell (CL:0000623). **CHEBI:** ribavirin (CHEBI:63580).

### 7. Anatomical Structures Affected
- **Primary organs/systems:** vascular endothelium / cardiovascular system (UBERON:0001981 blood vessel endothelium; UBERON:0004535 cardiovascular system); liver (UBERON:0002107); hematologic/coagulation system.
- **Secondary involvement:** kidneys (UBERON:0002113), lungs (UBERON:0002048), spleen (UBERON:0002106) — all show high viral titers in guinea pigs ([PMID: 41118368](https://pubmed.ncbi.nlm.nih.gov/41118368/)); CNS (late neurological signs); soft tissue of face/neck (edema).
- **Cell level:** endothelial cells, hepatocytes, platelets, mononuclear phagocytes.
- **Subcellular compartments involved in the viral life cycle (GO cellular component):** late endosome (GO:0005770), endosome membrane (GO:0010008), plasma membrane (GO:0005886), host cell surface. **Localization:** systemic/bilateral; facial and cervical edema is a distinctive regional sign.

### 8. Temporal Development
**Onset:** acute, adult-onset, with abrupt fever after an incubation of roughly 1–2 weeks (arenaviral range). **Progression:** week 1 = febrile prodrome and multisystem symptoms; week 2 = shock, DIC, multi-organ failure, death. **Rate:** rapid. **Course:** monophasic, self-limited in survivors (recovery) or fatal. In the one survivor, early ribavirin and intensive support were associated with recovery ([PMID: 25393244](https://pubmed.ncbi.nlm.nih.gov/25393244/)). The **critical window for intervention** appears to be early, before the week-2 cytokine-storm/DIC cascade.

### 9. Inheritance and Population
**Epidemiology:** a single recognized outbreak (2008), 5 cases, **80% CFR (4/5)** ([PMID: 27593704](https://pubmed.ncbi.nlm.nih.gov/27593704/)). Prevalence/incidence are effectively zero outside this outbreak; true endemic burden is unknown due to under-surveillance in the region ([PMID: 25416679](https://pubmed.ncbi.nlm.nih.gov/25416679/)). **Inheritance:** not applicable (infectious). **Geographic distribution:** Southern Africa — epidemiologically linked to Zambia (Lusaka) and South Africa (Johannesburg). **Sex/age:** too few human cases for a ratio; experimental models show male sex and adult/older age associated with worse outcomes ([PMID: 41118368](https://pubmed.ncbi.nlm.nih.gov/41118368/)).

### 10. Diagnostics
**Laboratory:** thrombocytopenia, transaminitis, coagulopathy (Lassa-like) ([PMID: 29733163](https://pubmed.ncbi.nlm.nih.gov/29733163/)). **Molecular diagnosis of choice:** real-time **RT-PCR** assays specific for Lujo viral RNA, developed and validated against the sole isolate ([PMID: 24096270](https://pubmed.ncbi.nlm.nih.gov/24096270/)). Virus isolation and serology require BSL-4. **BSL-2 surrogate systems** (VSV-LUJV/GP pseudotypes) support research/entry assays ([PMID: 24741091](https://pubmed.ncbi.nlm.nih.gov/24741091/); [PMID: 22396728](https://pubmed.ncbi.nlm.nih.gov/22396728/)). **Differential diagnosis:** Lassa fever (most important — clinically near-identical), Ebola/Marburg, Crimean-Congo hemorrhagic fever, Rift Valley fever, severe malaria, leptospirosis, typhoid, and other septic/DIC syndromes. **Genetic/omics diagnostics:** not applicable for host diagnosis. No newborn/carrier screening applies.

### 11. Outcome/Prognosis
**Mortality:** 80% CFR in the only outbreak. **Prognostic factors:** early antiviral therapy and intensive supportive care (favorable — one survivor); magnitude/timing of the inflammatory cytokine response is the principal determinant of outcome, with cytokine storm predicting death ([PMID: 41118368](https://pubmed.ncbi.nlm.nih.gov/41118368/); [PMID: 25520505](https://pubmed.ncbi.nlm.nih.gov/25520505/)). **Complications:** DIC, hemorrhage, shock, hepatic and multi-organ failure. **Recovery:** survivors can recover; long-term sequelae are undocumented given the tiny cohort. Candidate **prognostic biomarkers:** IL-1β, IL-6, CXCL10 (from models).

### 12. Treatment
**No approved antiviral or vaccine exists** ([PMID: 41118368](https://pubmed.ncbi.nlm.nih.gov/41118368/)). Management is **early ribavirin plus aggressive supportive care** (fluid resuscitation, correction of coagulopathy, organ support), as used in the single survivor ([PMID: 25393244](https://pubmed.ncbi.nlm.nih.gov/25393244/)) — **NCIT: Ribavirin (C790); Supportive Care (C15277)**. **Experimental/preclinical candidates:**

| Strategy | Mechanism / target | Evidence | Status |
|---|---|---|---|
| Ribavirin | Viral RNA synthesis inhibitor | [PMID: 25393244](https://pubmed.ncbi.nlm.nih.gov/25393244/) | Used clinically (survivor) |
| CB1 antagonists (rimonabant, AM251, AM281) | Block LUJV entry | [PMID: 37633192](https://pubmed.ncbi.nlm.nih.gov/37633192/) | Preclinical |
| FDA-approved library hits | Entry inhibition | [PMID: 34925303](https://pubmed.ncbi.nlm.nih.gov/34925303/) | Preclinical |
| Reporter-virus HTS hits (6 compounds) | Various | [PMID: 34203149](https://pubmed.ncbi.nlm.nih.gov/34203149/) | Preclinical |
| Griffithsin (lectin) | Binds GP glycans, blocks entry | [PMID: 42037406](https://pubmed.ncbi.nlm.nih.gov/42037406/) | Preclinical |
| PF-429242 | S1P/SKI-1 inhibitor; blocks GPC maturation | [PMID: 26719243](https://pubmed.ncbi.nlm.nih.gov/26719243/) | Preclinical |

No targeted pharmacogenomics, gene therapy, or cell therapy applies.

### 13. Prevention
**Primary prevention** rests on **strict infection control** (barrier nursing, isolation, PPE, safe handling of body fluids), given nosocomial spread ([PMID: 27593704](https://pubmed.ncbi.nlm.nih.gov/27593704/); [PMID: 29733163](https://pubmed.ncbi.nlm.nih.gov/29733163/)). Timely molecular diagnosis enables patient isolation to prevent onward transmission ([PMID: 24096270](https://pubmed.ncbi.nlm.nih.gov/24096270/)). **Immunization:** no licensed vaccine; the **MOPEVAC** hyperattenuated-Mopeia platform expressing heterologous glycoproteins is a candidate pan-arenavirus vaccine ([PMID: 29593043](https://pubmed.ncbi.nlm.nih.gov/29593043/)). Reservoir control cannot yet be targeted because the reservoir is unidentified.

### 14. Other Species / Natural Disease
**Pathogen:** Lujo mammarenavirus (NCBI taxid 649188). **Presumed reservoir:** an unidentified rodent (zoonotic, by analogy to other arenaviruses) — **zoonotic potential is high but the specific host and spillover route are unknown** ([PMID: 41118368](https://pubmed.ncbi.nlm.nih.gov/41118368/); [PMID: 25416679](https://pubmed.ncbi.nlm.nih.gov/25416679/)). No naturally occurring companion-animal or livestock disease has been reported. Experimental cross-species susceptibility is governed by the host CD63 F143 residue ([PMID: 35164564](https://pubmed.ncbi.nlm.nih.gov/35164564/)).

### 15. Model Organisms
| Model | Type | Recapitulation | Reference |
|---|---|---|---|
| Cynomolgus macaque | NHP | Mild, non-lethal; useful for immune kinetics | [PMID: 25520505](https://pubmed.ncbi.nlm.nih.gov/25520505/) |
| Strain 13/N guinea pig | Rodent | Hematologic/biochemical abnormalities, age/sex-dependent lethality | [PMID: 41118368](https://pubmed.ncbi.nlm.nih.gov/41118368/) |
| STAT1-knockout mouse | Genetic KO rodent | Partial lethal disease; key hematologic/clinical-chemistry/histologic features | [PMID: 42075721](https://pubmed.ncbi.nlm.nih.gov/42075721/) |
| VSV-LUJV/GP pseudotype | In vitro (BSL-2) | Entry only | [PMID: 24741091](https://pubmed.ncbi.nlm.nih.gov/24741091/); [PMID: 22396728](https://pubmed.ncbi.nlm.nih.gov/22396728/) |
| Recombinant reporter LUJV | In vitro HTS | Full replication for drug screening | [PMID: 34203149](https://pubmed.ncbi.nlm.nih.gov/34203149/) |

**Limitation:** wild-type inbred mice/hamsters resist infection (non-human CD63), so humanized-CD63 or IFN-deficient backgrounds are needed; no model perfectly reproduces fatal human LHF.

---

## Mechanistic Model / Interpretation

```
 LUJV exposure (mucosal/percutaneous, nosocomial)
          |
          v
 GP1 binds NRP2 (cell surface)  ──►  endocytosis
          |                              [GPC pre-primed by host S1P @ RKLM]
          v
 Late endosome: CD63 (F143) + low pH  ──►  GP2-driven membrane fusion
          |                                  (analogous to Lassa α-DG→LAMP1)
          v
 Cytoplasmic replication; NP DEDDH exonuclease degrades RNA
          |
          v
 Type I IFN suppressed → ~72 h DELAY in antiviral/inflammatory response
          |
     ┌────┴───────────────────────────┐
     v (measured response)            v (dysregulated response)
  BRANCH A: SURVIVAL             BRANCH B: cytokine storm
  (macaque; young female GP)     (IL-1β, IL-2, IL-6, CXCL10)
                                       |
                                       v
                 VEGF-driven capillary leak + endothelial/platelet
                 dysfunction (loss of prostacyclin) + hepatocellular
                 necrosis (reduced coagulation factors)
                                       |
                                       v
                            DIC → SHOCK → MULTI-ORGAN FAILURE → DEATH
```

The central interpretive insight is that **LHF outcome is an immunological phenotype, not a virological one**: viral titers are comparable in survivors and fatalities, but the timing and intensity of the host inflammatory response diverge ([PMID: 41118368](https://pubmed.ncbi.nlm.nih.gov/41118368/); [PMID: 25520505](https://pubmed.ncbi.nlm.nih.gov/25520505/)). This frames two complementary therapeutic avenues: **block entry/replication early** (NRP2/CD63 entry inhibitors, S1P inhibitors, griffithsin, ribavirin) and **modulate the downstream immunopathology** (anti-cytokine/supportive strategies). LUJV's uniqueness among arenaviruses — the NRP2/CD63 receptor pair — makes it both a mechanistic outlier and a sharply defined drug target.

---

## Evidence Base

| PMID | Role in this report |
|---|---|
| [19478873](https://pubmed.ncbi.nlm.nih.gov/19478873/) | Discovery & phylogeny: LUJV is a distinct Old World arenavirus (Finding 1) |
| [29120745](https://pubmed.ncbi.nlm.nih.gov/29120745/) | NRP2 + CD63 host factors; entry mechanism (Finding 2) |
| [35164564](https://pubmed.ncbi.nlm.nih.gov/35164564/) | CD63 F143 host-range determinant (Findings 2, 5) |
| [30150732](https://pubmed.ncbi.nlm.nih.gov/30150732/) | Crystal structure of GP1–NRP2 (Finding 2) |
| [39169025](https://pubmed.ncbi.nlm.nih.gov/39169025/) | Cryo-EM of trimeric spike; single NRP2 at apex (Finding 2) |
| [24741091](https://pubmed.ncbi.nlm.nih.gov/24741091/) | Pseudotype entry independent of α-DG/TfR1; NPC1/cholesterol dependence (Findings 2, 5) |
| [25393244](https://pubmed.ncbi.nlm.nih.gov/25393244/) | Clinical course & ribavirin in survivor (Finding 3) |
| [29733163](https://pubmed.ncbi.nlm.nih.gov/29733163/) | Lassa-like clinical/lab features; outbreak overview (Finding 3) |
| [41118368](https://pubmed.ncbi.nlm.nih.gov/41118368/) | Guinea pig model; immune (not viral) burden drives outcome (Findings 4, 5, 6) |
| [25520505](https://pubmed.ncbi.nlm.nih.gov/25520505/) | Macaque model; 72-h delayed inflammatory response (Findings 4, 5, 10) |
| [42075721](https://pubmed.ncbi.nlm.nih.gov/42075721/) | STAT-1 KO mouse model (Findings 5, 10) |
| [27593704](https://pubmed.ncbi.nlm.nih.gov/27593704/) | Epidemiology: 80% CFR, nosocomial (Finding 6) |
| [24096270](https://pubmed.ncbi.nlm.nih.gov/24096270/) | RT-PCR diagnostics; single strain (Finding 6) |
| [26719243](https://pubmed.ncbi.nlm.nih.gov/26719243/) | S1P maturation at RKLM; ESCRT-independent budding (Finding 7) |
| [37633192](https://pubmed.ncbi.nlm.nih.gov/37633192/) | CB1 antagonist entry inhibitors (Finding 8) |
| [34925303](https://pubmed.ncbi.nlm.nih.gov/34925303/) | FDA-library entry inhibitors (Finding 8) |
| [34203149](https://pubmed.ncbi.nlm.nih.gov/34203149/) | Reporter-virus HTS; 6 anti-LUJV compounds (Finding 8) |
| [42037406](https://pubmed.ncbi.nlm.nih.gov/42037406/) | Griffithsin blocks entry (Finding 8) |
| [22396728](https://pubmed.ncbi.nlm.nih.gov/22396728/) | BSL-2 pseudotype screening platform (Finding 5) |
| [23121052](https://pubmed.ncbi.nlm.nih.gov/23121052/) | Shared VHF tissue-injury mechanisms (Finding 9) |
| [3543155](https://pubmed.ncbi.nlm.nih.gov/3543155/) | Platelet/endothelial dysfunction in primate Lassa shock (Finding 9) |
| [29295909](https://pubmed.ncbi.nlm.nih.gov/29295909/) | Lassa α-DG→LAMP1 switch paradigm (Finding 9) |
| [25878103](https://pubmed.ncbi.nlm.nih.gov/25878103/) | NP DEDDH exonuclease IFN suppression (Finding 10) |
| [29593043](https://pubmed.ncbi.nlm.nih.gov/29593043/) | MOPEVAC vaccine platform (Finding 10) |
| [22607481](https://pubmed.ncbi.nlm.nih.gov/22607481/) | Arenavirus drug-discovery context (background) |
| [25416679](https://pubmed.ncbi.nlm.nih.gov/25416679/) | Under-surveillance of emerging zoonoses (epidemiology context) |

---

## Limitations and Knowledge Gaps

1. **Single outbreak, n=5.** All human clinical knowledge rests on five cases; incidence, prevalence, full phenotype spectrum, sex ratio, incubation period, and long-term sequelae are essentially unknown.
2. **Reservoir unidentified.** No animal host or spillover route is known, precluding reservoir-targeted prevention and ecological risk assessment.
3. **No fully lethal animal model.** Macaques are mild; guinea pig and STAT-1 KO models are only partially lethal; wild-type rodents resist infection due to non-human CD63.
4. **Mechanistic inference by homology.** The NP-exonuclease IFN-suppression step and some VHF tissue-injury mechanisms (VEGF permeability, DIC) are inferred from related arenaviruses rather than demonstrated directly for LUJV.
5. **No approved countermeasures.** All targeted therapeutics and the MOPEVAC vaccine are preclinical; ribavirin efficacy is anecdotal (one survivor who also received intensive supportive care).
6. **Genomic diversity unknown.** Diagnostics are validated against a single isolate; antigenic/genetic variation across any future strains is uncharacterized.

---

## Proposed Follow-up Experiments / Actions

1. **Reservoir surveillance** in Zambia/Southern Africa — trap and screen rodents by RT-PCR/serology to identify the natural host and define spillover ecology.
2. **Develop a robustly lethal small-animal model** — e.g., humanized-CD63 (F143 knock-in) mice or further-characterized guinea pig strains — to enable rigorous efficacy testing.
3. **Test leading entry inhibitors in vivo** — prioritize CB1 antagonists, griffithsin, and the S1P inhibitor PF-429242 in the guinea pig/STAT-1 KO models, alone and with ribavirin.
4. **Directly validate the NP-exonuclease IFN-suppression mechanism in LUJV** by catalytic-residue mutagenesis, testing attenuation and immunogenicity (toward a rationally attenuated vaccine).
5. **Advance MOPEVAC-LUJV** (Mopeia platform expressing LUJV GPC) through immunogenicity and challenge studies.
6. **Define immunopathology biomarkers** (IL-1β, IL-6, CXCL10) as prognostic/therapeutic-response markers and evaluate host-directed immunomodulation to interrupt the cytokine-storm→DIC→shock cascade.
7. **Broaden and field-deploy diagnostics** — expand RT-PCR design to anticipate genetic variants and distinguish LUJV from Lassa in endemic settings.

---

*Report compiled from a 5-iteration autonomous investigation: 10 confirmed findings, 26 papers reviewed. Lujo hemorrhagic fever is an infectious viral hemorrhagic fever with no human causal gene; the causal agent is Lujo virus (LUJV).*


## Artifacts

- [OpenScientist final report](Lujo_Hemorrhagic_Fever-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Lujo_Hemorrhagic_Fever-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 5 |
| Quoted claims found in source | 5 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 26 |
| On topic | 23 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 46 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 16 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 16 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001945` (1 mention) - the report calls it "Symptom"; HP calls it **Fever**
- `HP:0002315` (1 mention) - the report calls it "Symptom"; HP calls it **Headache**
- `HP:0003326` (1 mention) - the report calls it "Symptom"; HP calls it **Myalgia**
- `HP:0025439` (1 mention) - the report calls it "Sign"; HP calls it **Pharyngitis**
- `HP:0100749` (1 mention) - the report calls it "Symptom"; HP calls it **Chest pain**
- `HP:0002014` (1 mention) - the report calls it "Symptom"; HP calls it **Diarrhea**
- `HP:0000988` (1 mention) - the report calls it "Sign"; HP calls it **Skin rash**
- `HP:0011885` (1 mention) - the report calls it "Sign"; HP calls it **Hemorrhage of the eye**
- `HP:0000316` (1 mention) - the report calls it "facial edema"; HP calls it **Hypertelorism**
- `HP:0001892` (1 mention) - the report calls it "Sign"; HP calls it **Abnormal bleeding**
- `HP:0001873` (1 mention) - the report calls it "Lab"; HP calls it **Thrombocytopenia**
- `HP:0002910` (1 mention) - the report calls it "Lab"; HP calls it **Elevated circulating hepatic transaminase concentration**
- `HP:0031273` (1 mention) - the report calls it "Sign"; HP calls it **Shock**
- `HP:0005521` (1 mention) - the report calls it "Lab/sign"; HP calls it **Disseminated intravascular coagulation**
- `HP:0000707` (1 mention) - the report calls it "Sign"; HP calls it **Abnormality of the nervous system**
- `UBERON:0002113` (1 mention) - the report calls it "Secondary involvement:** kidneys"; UBERON calls it **kidney**