---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-12T12:53:05.001673'
end_time: '2026-09-12T13:08:52.639202'
duration_seconds: 947.64
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Congenital Factor X Deficiency
  mondo_id: MONDO:0009212
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
citation_count: 35
reference_validation:
  total_references: 35
  verified: 35
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 35
  on_topic: 19
  off_topic: 1
  off_topic_references:
  - PMID:39671302
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 33
  verified: 30
  not_found: 1
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.032
  labels_checked: 26
  labels_matching: 1
  labels_mismatched: 17
  mislabelled_terms:
  - term_id: MONDO:0009212
    reported_labels:
    - MONDO
    ontology_label: congenital factor X deficiency
  - term_id: HP:0001892
    reported_labels:
    - Clinical sign
    ontology_label: Abnormal bleeding
  - term_id: HP:0000421
    reported_labels:
    - Symptom
    ontology_label: Epistaxis
  - term_id: HP:0000978
    reported_labels:
    - Sign
    ontology_label: Bruising susceptibility
  - term_id: HP:0031364
    reported_labels:
    - Sign
    ontology_label: Ecchymosis
  - term_id: HP:0002170
    reported_labels:
    - Sign
    ontology_label: Intracranial hemorrhage
  - term_id: HP:0000132
    reported_labels:
    - Symptom
    ontology_label: Menorrhagia
  - term_id: HP:0008151
    reported_labels:
    - Lab abnormality
    ontology_label: Prolonged prothrombin time
  - term_id: HP:0003645
    reported_labels:
    - Lab abnormality
    ontology_label: Prolonged partial thromboplastin time
  - term_id: HP:0040189
    reported_labels:
    - Lab abnormality
    ontology_label: Scaling skin
  - term_id: CL:0000233
    reported_labels:
    - platelet
    - Platelet (coagulation surface)
    ontology_label: platelet
  - term_id: UBERON:0002107
    reported_labels:
    - Liver (site of FX production)
    ontology_label: liver
  - term_id: UBERON:0000955
    reported_labels:
    - Brain / intracranial space
    ontology_label: brain
  - term_id: UBERON:0000403
    reported_labels:
    - Scalp / subgaleal space
    ontology_label: scalp
  - term_id: UBERON:0000995
    reported_labels:
    - Uterus / endometrium (menorrhagia)
    ontology_label: uterus
  - term_id: UBERON:0002097
    reported_labels:
    - Skin / subcutaneous tissue
    ontology_label: skin of body
  - term_id: GO:0005783
    reported_labels:
    - "Hepatocyte ER (\u03B3-carboxylation, secretion)"
    ontology_label: endoplasmic reticulum
  labels_variant: 8
  unresolved_terms:
  - HP:0002320
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
  path: Congenital_Factor_X_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Congenital_Factor_X_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Factor X Deficiency
- **MONDO ID:** MONDO:0009212 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Factor X Deficiency** covering all of the
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

# Congenital Factor X Deficiency — Comprehensive Disease Characterization Report

**Disease:** Congenital (Hereditary) Factor X Deficiency — "Stuart–Prower factor deficiency"
**MONDO ID:** MONDO:0009212 · **OMIM:** 227600 · **Gene OMIM:** 613872 (*F10*) · **Category:** Mendelian (autosomal recessive)
**Report basis:** 13 confirmed findings · 46 papers reviewed · 5 investigation iterations. Literature-derived from aggregated disease-level resources plus case reports, cohorts/registries, model organisms, and structural studies.

---

## Summary

Congenital Factor X (FX) deficiency is an ultra-rare autosomal recessive bleeding disorder caused by biallelic loss-of-function or dysfunction-inducing variants in the **F10** gene on chromosome **13q34**. F10 encodes coagulation factor X (Stuart–Prower factor), a vitamin K–dependent serine protease synthesized in the liver that sits at the **convergence point of the extrinsic (tissue factor/FVIIa) and intrinsic (FIXa/FVIIIa) coagulation pathways**. Its activated form, FXa, assembles with cofactor FVa, calcium, and phospholipid membranes into the **prothrombinase complex** that converts prothrombin to thrombin — the enzyme that ultimately forms the platelet plug and fibrin clot. When both F10 alleles are defective, FXa output falls, thrombin generation is impaired, and a bleeding diathesis results.

The clinical severity of the disorder correlates strongly with residual FX coagulant activity (FX:C). Severe deficiency (FX:C <1%) manifests in the **neonatal period** with umbilical-stump bleeding and, most gravely, **intracranial and subgaleal hemorrhage**, whereas milder forms cause mucocutaneous bleeding, epistaxis, easy bruising, menorrhagia, and hemarthrosis. Diagnosis rests on the characteristic pattern of **simultaneously prolonged prothrombin time (PT) and activated partial thromboplastin time (APTT)** — a signature of a common-pathway defect — confirmed by a specific FX activity assay, with FX antigen (FX:Ag) measurement distinguishing quantitative (type I) from dysfunctional (type II) disease.

Management is tiered around **factor replacement**: high-purity plasma-derived FX concentrate (pdFX / Coagadex) is the first single-factor–specific product approved in the US and EU and is safe and effective for on-demand treatment, prophylaxis, and perioperative cover; prothrombin complex concentrate (PCC) and fresh frozen plasma (FFP) serve as alternatives where FX concentrate is unavailable, with antifibrinolytics and hormonal therapy as adjuncts. Prophylaxis prevents the otherwise poor outcome of recurrent early-life intracranial hemorrhage. Prevention centers on genetic counseling, carrier/cascade testing, and prenatal/preimplantation diagnosis, particularly relevant given the higher prevalence in consanguineous populations.

---

## 1. Disease Information

Congenital Factor X deficiency is **"a rare autosomal recessive bleeding disorder caused by mutations in the F10 gene located on chromosome 13q34-ter"** ([PMID: 30507709](https://pubmed.ncbi.nlm.nih.gov/30507709/)). Factor X, originally named **Stuart–Prower factor**, is a plasma glycoprotein that plays a pivotal role in the coagulation cascade.

**Key identifiers:**

| Resource | Identifier |
|----------|-----------|
| MONDO | MONDO:0009212 |
| OMIM (phenotype) | 227600 (Factor X deficiency) |
| OMIM (gene) | 613872 (F10) |
| Orphanet | ORPHA:328 (Hereditary factor X deficiency) |
| ICD-10 | D68.2 (Hereditary deficiency of other clotting factors) |
| ICD-11 | 3B12.0 |
| MeSH | D005166 (Factor X Deficiency) |
| HGNC | HGNC:3528 (F10) |
| UniProt | P00742 (FA10_HUMAN) |

**Synonyms / alternative names:** Hereditary factor X deficiency (HFXD), Stuart–Prower factor deficiency, Stuart factor deficiency, congenital FX deficiency.

**Data provenance:** The evidence in this report is derived from **aggregated disease-level resources** — case reports, multicentre genotype–phenotype cohorts, disease registries (EN-RBD, PRO-RBDD), and clinical trials — rather than from individual-patient EHR extracts.

---

## 2. Etiology

**Disease causal factors.** The disorder is **monogenic and genetic**. It is caused by biallelic pathogenic variants in **F10**, inherited in an autosomal recessive fashion. There is no environmental or infectious cause of the *congenital* form. (A distinct **acquired** FX deficiency exists — associated with AL amyloidosis, autoimmune disease such as Sjögren's syndrome, and transient inhibitors — but this is etiologically separate and is discussed only for differential diagnosis.)

**Genetic risk factors.** The causal variants are within F10 itself. A multicentre cohort **"identified 22 separate mutations, including 15 missense mutations, 2 deletions, 4 splice site mutations, and 1 nonsense mutation"** among 24 individuals, with 149 F10 mutations reported to date at the time of that study ([PMID: 30507709](https://pubmed.ncbi.nlm.nih.gov/30507709/)). Missense variants predominate. Because the disorder is recessive, **carrier (heterozygous) status** in both parents is the fundamental genetic risk factor for an affected child.

**Environmental risk factors.** **Consanguinity** is the dominant modifiable risk determinant at the population level — the disorder is markedly more prevalent in populations with high rates of consanguineous marriage (Iran, Turkey, Pakistan, Egypt). Consanguineous unions increase the probability that both parents carry the same rare F10 allele; documented pedigrees explicitly attribute homozygous disease to consanguineous marriage (e.g., the p.Val298Met Chinese pedigree, [PMID: 27264807](https://pubmed.ncbi.nlm.nih.gov/27264807/)). No toxic, occupational, or lifestyle exposure causes the congenital disease.

**Protective factors.** No genetic protective alleles or environmental protective factors have been established for congenital FX deficiency. Heterozygous carriers with FX:C 40–50% are typically asymptomatic, effectively conferring a "protected" phenotype relative to homozygotes, but this reflects gene dosage rather than a distinct protective mechanism.

**Gene–environment interactions.** The principal interaction is between the recessive F10 genotype and the sociocultural environment of consanguinity, which raises homozygosity rates. Vitamin K status and hepatic function modulate overall FX levels (FX is vitamin K–dependent), so intercurrent liver disease, vitamin K deficiency, or vitamin K antagonist exposure can compound a congenital deficiency — an environmental modifier of the biochemical phenotype rather than a cause.

---

## 3. Phenotypes

The phenotype is a **hemorrhagic diathesis** whose severity tracks residual FX:C. Bleeding spans mucocutaneous, deep-tissue, and life-threatening central-nervous-system bleeds.

| Phenotype | Type | HPO term | Frequency / severity | Onset |
|-----------|------|----------|----------------------|-------|
| Abnormal / prolonged bleeding | Clinical sign | HP:0001892 | Universal in severe disease | Neonatal–variable |
| Epistaxis | Symptom | HP:0000421 | 11/12 (91%) in a severe cohort | Childhood |
| Easy bruising / ecchymoses | Sign | HP:0000978 | 11/12 (91%) | Childhood |
| Hemarthrosis | Sign | HP:0005261 / HP:0003268 | 10/12 (83%) | Childhood |
| Umbilical stump bleeding | Sign | HP:0031364 | Characteristic of severe neonatal disease | Neonatal |
| Intracranial hemorrhage | Sign | HP:0002170 | Recurrent in severe disease; high morbidity | Neonatal–infancy |
| Subgaleal / subdural hematoma | Sign | HP:0002320 | Reported in neonatal severe disease | Neonatal |
| Menorrhagia | Symptom | HP:0000132 | Common in affected women | Adolescence–adult |
| Prolonged PT | Lab abnormality | HP:0008151 | Universal | Congenital |
| Prolonged APTT | Lab abnormality | HP:0003645 | Universal | Congenital |
| Reduced factor X activity | Lab abnormality | HP:0040189 | Universal (diagnostic) | Congenital |

**Age of onset.** Severe disease presents **neonatally**: *"Early neonatal bleeding, including umbilical and subgaleal hemorrhage, may be the initial manifestations of severe congenital FX deficiency, even in the absence of family history"* ([PMID: 42144914](https://pubmed.ncbi.nlm.nih.gov/42144914/)). Milder deficiency may present in childhood or be detected incidentally in adulthood.

**Severity and frequency.** In a 12-patient severe cohort, *"the most frequent bleeding episodes in patients were epistaxis and easy bruising (11/12, 91%), followed by haemarthroses (10/12, 83%)"* ([PMID: 26222694](https://pubmed.ncbi.nlm.nih.gov/26222694/)). Severity is graded by FX:C (see §8/§10).

**Symptom progression.** The bleeding tendency is **lifelong and episodic** — punctuated by spontaneous bleeds and provoked by trauma, surgery, or childbirth — rather than steadily progressive. Severity is generally stable for a given genotype.

**Quality of life impact.** Recurrent bleeds, joint damage from hemarthroses, menorrhagia, and the burden of prophylactic infusions affect daily functioning; disease-specific QoL data are limited, but the plain-language pdFX summary notes that patients' *"health and daily lives were impacted in different ways by HFXD"* ([PMID: 42253376](https://pubmed.ncbi.nlm.nih.gov/42253376/)).

---

## 4. Genetic / Molecular Information

**Causal gene.** **F10** (HGNC:3528; OMIM 613872), located on **chromosome 13q34-ter** ([PMID: 30507709](https://pubmed.ncbi.nlm.nih.gov/30507709/)). It comprises 8 exons and encodes the ~488-residue mature factor X protein.

**Protein domain architecture.** FX is *"composed of the γ-carboxyglutamic acid (GLA) domain, two epidermal growth factor domains (EGF-1 and EGF-2), and the serine protease (SP) domain"* ([PMID: 35059555](https://pubmed.ncbi.nlm.nih.gov/35059555/)); equivalently *"an N-terminal γ-carboxyglutamate (Gla) domain, two epidermal growth factor-like (EGF) domains, and a C-terminal trypsin-like serine protease (SP) domain"* ([PMID: 30644641](https://pubmed.ncbi.nlm.nih.gov/30644641/)). The **vitamin K–dependent γ-carboxylation of GLA-domain glutamates** is required for calcium binding and phospholipid-membrane association.

**Variant spectrum.** An *"interactive FX variant database"* analyzed **180 genetic variants** across all four domains (GLA, EGF-1, EGF-2, SP), yielding genotype–severity insight ([PMID: 35059555](https://pubmed.ncbi.nlm.nih.gov/35059555/)); HGMD previously cataloged **>149 F10 mutations**. Missense variants predominate. Representative pathogenic variants documented in the reviewed literature:

| Variant (protein) | cDNA / exon | Domain | Effect | Reference |
|-------------------|-------------|--------|--------|-----------|
| p.Val298Met | g.27881G>A, exon 8 | SP | Homozygous; secondary-structure change; FX:C 1% | [PMID: 27264807](https://pubmed.ncbi.nlm.nih.gov/27264807/) |
| p.Phe71Ser | c.212T>C, exon 2 | GLA | Disrupts Ca²⁺-binding hydrogen bonds | [PMID: 41451502](https://pubmed.ncbi.nlm.nih.gov/41451502/) |
| p.Val424Phe | c.1270G>T, exon 8 | SP | Steric hindrance in catalytic domain | [PMID: 41451502](https://pubmed.ncbi.nlm.nih.gov/41451502/) |
| p.Gln249Pro | homozygous | SP | FX:C <1%, severe bleeding | [PMID: 42506896](https://pubmed.ncbi.nlm.nih.gov/42506896/) |
| p.Gly262Asp | — | SP | Recurrent; type II deficiency | [PMID: 26222694](https://pubmed.ncbi.nlm.nih.gov/26222694/) |
| p.Leu487Phe | novel | SP | Iranian cohort | [PMID: 35140190](https://pubmed.ncbi.nlm.nih.gov/35140190/) |
| p.Pro343Ser (FX Friuli) | — | SP | Dysfunctional; normal RVVT | [PMID: 28030967](https://pubmed.ncbi.nlm.nih.gov/28030967/) |

**Variant classification.** By ACMG/AMP criteria, most reported F10 variants are **pathogenic / likely pathogenic**; bioinformatic conservation analyses (e.g., Phe71, Val424 are highly conserved) support pathogenicity ([PMID: 41451502](https://pubmed.ncbi.nlm.nih.gov/41451502/)).

**Functional consequences.** Two functional classes:
- **Type I (quantitative):** concordant reduction of FX activity and antigen (loss of protein).
- **Type II (dysfunctional / qualitative):** reduced activity with normal/near-normal antigen (defective protein). *"FX:Ag was reduced in all patients, consistent with type II deficiency"* in one cohort ([PMID: 26222694](https://pubmed.ncbi.nlm.nih.gov/26222694/)); type II variants like FX Friuli show discordant assay behavior. The overarching molecular consequence is **loss of function** — reduced generation of active FXa.

**Allele frequency.** Individual pathogenic F10 alleles are very rare in gnomAD (consistent with disease prevalence of 1:500,000–1:1,000,000). Specific alleles cluster in consanguineous founder populations.

**Somatic vs germline.** All congenital variants are **germline**. (Somatic/acquired FX loss occurs in amyloidosis but is not genetic.)

**Modifier genes / epigenetics / chromosomal abnormalities.** No specific modifier genes, epigenetic mechanisms, or large-scale chromosomal abnormalities have been established as drivers of congenital FX deficiency; the disorder is essentially fully explained by F10 genotype plus vitamin K–dependent post-translational modification. Residual FX:C is the principal determinant of phenotype.

---

## 5. Environmental Information

Congenital FX deficiency is a **purely genetic disorder** with no environmental, toxic, lifestyle, or infectious cause. The relevant environmental factors are:
- **Consanguinity** (sociocultural), which increases homozygosity and thus disease incidence in certain populations.
- **Vitamin K availability and hepatic function**, which modulate FX synthesis and can aggravate the biochemical deficiency (FX is a vitamin K–dependent hepatic glycoprotein).
- **No infectious agents** cause the congenital disease. (Historically, plasma-derived products carried viral-transmission risk, motivating high-purity/pathogen-reduced concentrates — a treatment-related, not disease-causing, consideration.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic pathogenic F10 variant** (missense/frameshift/nonsense/splice/deletion) → **leads to** reduced synthesis (type I) or production of a dysfunctional FX protein (type II).
2. Reduced/defective FX → **results in** impaired vitamin K–dependent GLA-domain function and/or impaired serine-protease catalytic activity → **leads to** lower functional plasma FX and reduced conversion of zymogen FX to the active protease FXa.
3. Upstream, *"Tissue factor (TF) and factor VIIa (FVIIa) form the [extrinsic complex] together with FX on phosphatidylserine-containing membranes, leading to FX activation by TF:FVIIa"* ([PMID: 39671302](https://pubmed.ncbi.nlm.nih.gov/39671302/)); the intrinsic FIXa/FVIIIa (tenase) complex activates FX in parallel. With defective FX, **both** activation routes yield less FXa. *(This is the branch point where extrinsic and intrinsic pathways converge on FX.)*
4. Reduced FXa → **results in** deficient assembly of the **prothrombinase complex** — *"the enzyme factor Xa (fXa), the cofactor fVa, Ca2+ and phospholipids, [which] activates the zymogen prothrombin to the protease thrombin"* ([PMID: 35427420](https://pubmed.ncbi.nlm.nih.gov/35427420/)).
5. Deficient prothrombinase → **leads to** decreased **thrombin generation**.
6. Decreased thrombin → **results in** reduced fibrinogen-to-fibrin conversion, impaired platelet activation, and an unstable clot: *"FX plays a pivotal role in the coagulation cascade, activating thrombin to promote platelet plug formation and prevent excess blood loss"* ([PMID: 35059555](https://pubmed.ncbi.nlm.nih.gov/35059555/)).
7. Impaired clot formation → **leads to** the clinical bleeding phenotype: umbilical, mucocutaneous, joint, and intracranial hemorrhage, with severity scaling inversely with residual FX:C.

### Detail by category

- **Molecular pathways:** The **blood coagulation cascade** — extrinsic (TF:FVIIa), intrinsic (FIXa:FVIIIa tenase), and common pathway (prothrombinase). GO:0007596 (blood coagulation), GO:0007597 (intrinsic pathway), GO:0007598 (extrinsic pathway).
- **Protein dysfunction:** GLA-domain variants (e.g., p.Phe71Ser) disrupt Ca²⁺ binding and membrane association; SP-domain variants (e.g., p.Val424Phe, p.Val298Met) alter catalytic/structural integrity. Loss of function is the unifying consequence.
- **Biochemical abnormalities:** Deficiency of a serine protease (FXa; GO:0004252, serine-type endopeptidase activity) at the pivotal convergence of coagulation; requires vitamin K–dependent γ-glutamyl carboxylation (GO:0017187).
- **Cellular processes / cell types:** Coordinated on phosphatidylserine-exposing **platelet** (CL:0000233) surfaces and TF-bearing cells; **hepatocytes** (CL:0000182) synthesize FX. Structural work confirms FX engages membranes via its GLA domain (cryo-EM of prothrombin–prothrombinase, [PMID: 35427420](https://pubmed.ncbi.nlm.nih.gov/35427420/); membrane-bound TF:FVIIa:FX model, [PMID: 39671302](https://pubmed.ncbi.nlm.nih.gov/39671302/)).
- **Tissue damage mechanism:** Not a primary tissue-destructive disease; damage is **secondary to hemorrhage** (intracranial bleeding → neurological injury; hemarthrosis → joint damage).
- **Immune involvement:** None in the congenital form. (Immune/autoimmune mechanisms characterize *acquired* FX deficiency — separate entities.)
- **Metabolic changes:** No systemic metabolic derangement; the "metabolic" defect is confined to vitamin K–dependent carboxylation of FX.

**Upstream vs downstream:** F10 genotype (upstream) → reduced FXa → reduced prothrombinase/thrombin (midstream) → impaired fibrin/platelet plug → bleeding (downstream clinical manifestation).

---

## 7. Anatomical Structures Affected

**Body system:** **Hematologic / coagulation (blood) system** — a systemic plasma-protein deficiency, so bleeding can affect any site.

| Level | Structure | Ontology term |
|-------|-----------|---------------|
| Organ (synthesis) | Liver (site of FX production) | UBERON:0002107 |
| Fluid / tissue | Blood / plasma | UBERON:0000178 |
| Primary clinical targets | Umbilical stump (neonate) | UBERON:0002331 |
| | Brain / intracranial space | UBERON:0000955 |
| | Scalp / subgaleal space | UBERON:0000403 |
| | Joints / synovial cavity | UBERON:0002217 |
| | Nasal mucosa (epistaxis) | UBERON:0001707 |
| | Uterus / endometrium (menorrhagia) | UBERON:0000995 |
| | Skin / subcutaneous tissue | UBERON:0002097 |
| Cell types | Hepatocyte (synthesis) | CL:0000182 |
| | Platelet (coagulation surface) | CL:0000233 |
| Subcellular | Extracellular region / plasma; PS-containing membranes | GO:0005576 |
| | Hepatocyte ER (γ-carboxylation, secretion) | GO:0005783 |

**Lateralization:** Bleeding is site-dependent and typically not lateralized; intracranial bleeds may be focal.

---

## 8. Temporal Development

**Onset.** **Congenital** — the deficiency is present from birth. Severe disease presents in the **neonatal period** (umbilical, subgaleal, intracranial hemorrhage); moderate/mild disease may present in childhood or later. The onset pattern of individual bleeds is **acute/episodic** on a chronic constitutional background.

**Severity classification by FX:C:**

| System | Severe | Moderate | Mild |
|--------|--------|----------|------|
| Traditional | FX:C <1% | FX:C 1–5% | FX:C 6–10% |
| EN-RBD (revised) | FX:C <10% | FX:C 10–40% | FX:C >40% |

*"HFXD is traditionally classified by severity as severe (FX:C <1%), moderate (FX:C = 1%-5%), or mild (FX:C = 6%-10%)"* ([PMID: 41104456](https://pubmed.ncbi.nlm.nih.gov/41104456/)); the revised EN-RBD criteria define *"severe (FX:C <10%), moderate (FX:C = 10%-40%), and mild (FX:C >40%)."* Phenotype heterogeneity exists: *"Seven patients with FX:C >40% had bleeding episodes that required treatment, and 3 of them experienced multiple bleeding episodes"* ([PMID: 41104456](https://pubmed.ncbi.nlm.nih.gov/41104456/)).

**Progression / course.** **Chronic, lifelong**, and **episodic/fluctuating** rather than progressive. Severity is stable for a given genotype. No spontaneous remission occurs; "remission" of the bleeding tendency is treatment-induced (factor replacement/prophylaxis).

**Critical periods.** The **neonatal/early-infancy window** is the period of greatest vulnerability to catastrophic intracranial hemorrhage and the key window for prophylactic intervention. Surgery, trauma, childbirth, and menstruation are recurring high-risk periods across life.

---

## 9. Inheritance and Population

**Epidemiology.** Ultra-rare. Estimated prevalence of severe disease is approximately **1 in 500,000 to 1 in 1,000,000** (HFXD affects 1:500,000–1:1,000,000 people worldwide; [PMID: 29707881](https://pubmed.ncbi.nlm.nih.gov/29707881/)). In rare-bleeding-disorder cohorts, FX deficiency is a small minority of cases (e.g., 0.36% in a north-eastern Iran survey, [PMID: 23114518](https://pubmed.ncbi.nlm.nih.gov/23114518/); 4.2% of inherited coagulation defects in an Egyptian pediatric series, [PMID: 22610136](https://pubmed.ncbi.nlm.nih.gov/22610136/)).

**Inheritance.** **Autosomal recessive** ([PMID: 30507709](https://pubmed.ncbi.nlm.nih.gov/30507709/)). Affected individuals are homozygous or compound heterozygous; heterozygous carriers have ~50% FX levels and are usually asymptomatic.

**Penetrance / expressivity.** Biallelic pathogenic genotypes are essentially fully penetrant for a laboratory phenotype (reduced FX:C), but **clinical expressivity is variable** and correlates with residual FX:C. Heterozygotes with FX:C 40–50% show no bleeding tendency.

**Genetic anticipation:** Not applicable (not a repeat-expansion disorder).

**Consanguinity and founder effects.** Consanguinity is central: the disorder is enriched in consanguineous populations, and homozygous variants recur through consanguineous marriage (e.g., [PMID: 27264807](https://pubmed.ncbi.nlm.nih.gov/27264807/)). Region-specific/founder variants occur (e.g., FX Friuli in an Italian population, [PMID: 28030967](https://pubmed.ncbi.nlm.nih.gov/28030967/); recurrent p.Gly262Asp, [PMID: 26222694](https://pubmed.ncbi.nlm.nih.gov/26222694/)).

**Population demographics.** Higher prevalence in Iran, Turkey, Pakistan, Egypt, and other regions with consanguineous marriage. As an autosomal recessive trait, the **sex ratio is approximately 1:1**, though females carry additional bleeding burden from menorrhagia and obstetric hemorrhage.

---

## 10. Diagnostics

**Screening coagulation tests.** The diagnostic hallmark is **simultaneous prolongation of PT and APTT**, reflecting FX's position at the convergence of extrinsic and intrinsic pathways. *"Diagnosis was made by abnormal results of Coagulation factors screening mainly Prothrombin time, Activated partial thromboplastin time, Russell's viper venom test, mixing tests factor X assay"* ([PMID: 9145616](https://pubmed.ncbi.nlm.nih.gov/9145616/)).

**Confirmatory / classifying assays:**
- **FX coagulant activity (FX:C)** — one-stage clotting assay; the diagnostic and severity-grading measure.
- **FX antigen (FX:Ag)** — ELISA; distinguishes **type I** (activity and antigen both reduced) from **type II** (activity reduced, antigen normal/near-normal). *"FX:Ag was reduced in all patients, consistent with type II deficiency"* ([PMID: 26222694](https://pubmed.ncbi.nlm.nih.gov/26222694/)).
- **Russell's viper venom time (RVVT)** and **mixing studies** — RVVT directly activates FX; useful for characterizing variants. Some dysfunctional variants behave atypically: FX Friuli shows *"prolonged partial thromboplastin time, prolonged prothrombin time but normal Russell viper venom clotting time"* ([PMID: 28030967](https://pubmed.ncbi.nlm.nih.gov/28030967/)), and a rare variant with normal APTT and RVVT despite prolonged PT has been described ([PMID: 4014297](https://pubmed.ncbi.nlm.nih.gov/4014297/)). Assaying FX through all three activation routes reveals molecular heterogeneity ([PMID: 3970856](https://pubmed.ncbi.nlm.nih.gov/3970856/)).

**Genetic testing.** Direct **F10 sequencing** (all 8 exons and flanking regions) confirms the diagnosis, identifies the causal variant(s), and enables carrier/cascade and prenatal testing. Single-gene testing is sufficient given the monogenic etiology; rare-bleeding-disorder panels are an alternative. WGS/WES are rarely needed but can be used when the phenotype is ambiguous. Chromosomal microarray/karyotyping/FISH are not indicated (no chromosomal abnormality involved).

**Differential diagnosis:**
- **Hemorrhagic disease of the newborn (vitamin K deficiency)** — a key mimic; severe congenital FX deficiency *"may be misdiagnosed as hemorrhagic disease of the newborn"* ([PMID: 15036435](https://pubmed.ncbi.nlm.nih.gov/15036435/)).
- **Acquired FX deficiency** — AL amyloidosis (mildly-to-severely reduced FX, e.g., [PMID: 42622220](https://pubmed.ncbi.nlm.nih.gov/42622220/)), autoimmune/Sjögren-associated ([PMID: 42227468](https://pubmed.ncbi.nlm.nih.gov/42227468/)), and transient inhibitor-mediated ([PMID: 9495379](https://pubmed.ncbi.nlm.nih.gov/9495379/)) forms; distinguished by later onset, absent family history, associated systemic disease, and (for inhibitors) incomplete correction on mixing.
- Other common-pathway factor deficiencies (FV, FII), combined VKD-factor deficiency, and vitamin K antagonist effect.

**Screening for asymptomatic individuals.** Cascade/carrier testing within affected families (via the known familial F10 variant) and prenatal diagnosis are the applicable approaches; there is no routine population newborn screen for FX deficiency.

---

## 11. Outcome / Prognosis

**Mortality / morbidity.** The chief threat to life and long-term function is **intracranial hemorrhage**, particularly in severe neonatal disease. Untreated severe disease historically carries a poor prognosis; an infant with severe FX deficiency had *"three intracranial hemorrhages in the first 6 months of life"* before prophylaxis ([PMID: 1530121](https://pubmed.ncbi.nlm.nih.gov/1530121/)), and siblings with severe disease presented with *"severe intracranial bleeding"* in which plasma replacement was not efficacious ([PMID: 15036435](https://pubmed.ncbi.nlm.nih.gov/15036435/)).

**Effect of treatment.** Prognosis is transformed by prophylaxis: prophylactic prothrombin complex infusions *"may prevent the poor outcome usually described in these patients"* ([PMID: 1530121](https://pubmed.ncbi.nlm.nih.gov/1530121/)), and modern high-purity pdFX prophylaxis provides excellent bleed prevention (see §12). With adequate replacement, life expectancy approaches normal and joint/neurological morbidity is markedly reduced.

**Disease course / complications.** Lifelong bleeding risk; complications include **hemophilic arthropathy** from recurrent hemarthrosis, **neurological sequelae** from ICH, obstetric hemorrhage and miscarriage in affected women, and, in resource-limited settings, transfusion-transmitted infection from older plasma products.

**Prognostic factors.** **Residual FX:C is the dominant prognostic biomarker** — *"Mutations leading to a FX:C of less than 1% are associated with severe bleeding symptoms confirming the strong correlation between clinical severity and FX:C"* ([PMID: 35140190](https://pubmed.ncbi.nlm.nih.gov/35140190/)); *"Severe bleeding in FX deficiency is associated with FX:C <5%, while milder deficiencies often present minimal symptoms"* ([PMID: 42506896](https://pubmed.ncbi.nlm.nih.gov/42506896/)). Genotype (homozygous/compound-heterozygous; GLA/SP-domain variants) and early ICH history further stratify risk. Access to specific factor replacement is a major determinant of outcome.

---

## 12. Treatment

**First-line: high-purity plasma-derived FX concentrate (pdFX / Coagadex).** pdFX is *"the first single-factor replacement therapy indicated for hereditary FX deficiency"* and is *"a safe and efficacious treatment option in patients aged ≥12 years with hereditary FX deficiency"* ([PMID: 27797267](https://pubmed.ncbi.nlm.nih.gov/27797267/)), approved in the US and EU for **on-demand treatment, prophylaxis, and perioperative management**. Phase 3 trials rated efficacy excellent with no inhibitor development, including in children <12 years ([PMID: 29707881](https://pubmed.ncbi.nlm.nih.gov/29707881/)), women/girls ([PMID: 29460388](https://pubmed.ncbi.nlm.nih.gov/29460388/)), and specific cohorts ([PMID: 29545231](https://pubmed.ncbi.nlm.nih.gov/29545231/)).

**Prophylaxis dosing.** *"Routine prophylaxis with pdFX be initiated at 25 IU/kg twice weekly in adults/adolescents ≥12 years of age, and at a dosage of 40 IU/kg twice weekly in children <12 years of age"* ([PMID: 35499465](https://pubmed.ncbi.nlm.nih.gov/35499465/)). On-demand dosing targets FX:C >5 IU/dL for hemostasis.

**Alternatives / adjuncts (tiered).** *"In centers where FX concentrate is unavailable, PCC and FFP provide effective hemostatic coverage"* ([PMID: 41836993](https://pubmed.ncbi.nlm.nih.gov/41836993/)) — demonstrated in perioperative pseudotumor evacuation. Real-world management combines modalities: *"treatments included antifibrinolytics, hormonal therapy, and factor replacement"* ([PMID: 41104456](https://pubmed.ncbi.nlm.nih.gov/41104456/)).

| Tier | Agent | NCIT-type term | Role / notes |
|------|-------|----------------|--------------|
| 1st line | Plasma-derived FX concentrate (pdFX/Coagadex) | Coagulation Factor X (Human) | Specific single-factor replacement; on-demand, prophylaxis, perioperative |
| Alternative | Prothrombin complex concentrate (PCC) | Prothrombin Complex Concentrate | Contains FX; thrombotic risk; use when pdFX unavailable |
| Alternative | Fresh frozen plasma (FFP) | Fresh Frozen Plasma | Broad replacement; volume-overload risk |
| Adjunct | Antifibrinolytics (tranexamic acid) | Tranexamic Acid | Mucosal bleeds, menorrhagia, dental/surgical |
| Adjunct | Hormonal therapy | Hormone Therapy | Menorrhagia management in women |

**Perioperative and obstetric management.** Factor replacement targets hemostatic FX:C perioperatively; obstetric care requires prophylaxis given elevated miscarriage/antenatal-hemorrhage rates (§13).

**Treatment outcomes / safety.** pdFX has minimal side effects, high treatment-success rates (98% in women/girls; [PMID: 29460388](https://pubmed.ncbi.nlm.nih.gov/29460388/)), and no inhibitor development reported. PCC carries thrombotic risk and FFP carries volume-overload and (for non–pathogen-reduced products) infection risk.

**Pharmacogenomics / advanced therapeutics.** No pharmacogenomic dosing guidance is established. **Gene therapy** is not yet clinically available for FX deficiency but is conceptually attractive (single, hepatically expressed gene); zebrafish and mouse models support target validation (§14–15).

---

## 13. Prevention

Because congenital FX deficiency is genetic, prevention is **reproductive and genetic**, not lifestyle-based.

- **Genetic counseling and carrier/cascade testing:** As an autosomal recessive disorder enriched in consanguineous families, identifying carriers via the familial F10 variant is central.
- **Prenatal and preimplantation diagnosis:** *"Advances in preconception genetic counselling and prenatal diagnosis, including non-invasive prenatal testing (NIPT) and preimplantation genetic diagnosis (PGD), are crucial for informed reproductive choices and delivery planning"* ([PMID: 41988968](https://pubmed.ncbi.nlm.nih.gov/41988968/)).
- **Reproductive/obstetric management (secondary prevention):** FX deficiency and *"other severe factor deficiencies … are associated with higher rates of miscarriage and antenatal haemorrhage, often requiring prophylactic factor replacement"* ([PMID: 41988968](https://pubmed.ncbi.nlm.nih.gov/41988968/)). Mode-of-delivery decisions aim to minimize cranial bleeding risk in an affected fetus.
- **Tertiary prevention (preventing complications):** Prophylactic factor replacement prevents recurrent intracranial hemorrhage and hemarthropathy ([PMID: 1530121](https://pubmed.ncbi.nlm.nih.gov/1530121/)).
- **Immunization / public-health / behavioral prevention:** Not applicable to a monogenic coagulopathy (beyond general trauma-avoidance counseling and hepatitis B vaccination for patients receiving blood products).

---

## 14. Other Species / Natural Disease

**Naturally occurring disease.** Congenital FX deficiency occurs spontaneously in non-human species, supporting cross-species conservation of the coagulation pathway. In a domestic cat: *"Severe congenital deficiency of factor X was diagnosed in a 3-year-old castrated male domestic shorthair cat with clinical signs of generalized seizures and prolonged bleeding after venipuncture"* ([PMID: 9290823](https://pubmed.ncbi.nlm.nih.gov/9290823/)); the seizures reflected intracranial bleeding, and reduced FX activity plus prolonged RVVT in the dam and a sibling indicated heritability — a natural phenocopy of severe human disease.

**Taxonomy / orthologs.** F10 is conserved across vertebrates; orthologs include mouse *F10* (NCBI Gene ID 14058), rat *F10*, zebrafish *f10*, and cat *F10*. The vitamin K–dependent coagulation factor family is evolutionarily ancient ([PMID: 30644641](https://pubmed.ncbi.nlm.nih.gov/30644641/)).

**Comparative biology.** Mammals (cat, mouse) show severe/lethal phenotypes with FX deficiency, whereas zebrafish tolerate severe common-pathway defects better: *"Deficiency of factor X (F10) in humans is a rare bleeding disorder with a heterogeneous phenotype and limited therapeutic options"* was studied via genome editing in zebrafish, which revealed *"unexpected tolerance of severe defects in the common pathway"* ([PMID: 28576875](https://pubmed.ncbi.nlm.nih.gov/28576875/)). This species difference is informative about pathway redundancy.

**Zoonotic potential:** None (genetic disorder).

---

## 15. Model Organisms

**Mouse (mammalian) knockout — closest phenotypic model.** Targeted deletion of the exons encoding mature FX produces a faithful model of severe human disease: *"homozygous deficiency results in partial embryonic lethality at embryonic day (E) 11.5-12.5 with signs of massive bleeding"* and *"the majority of those that survive to term die within 5 days, most frequently from intraabdominal bleeding"* ([PMID: 12161341](https://pubmed.ncbi.nlm.nih.gov/12161341/)); survivors die between P5–P20 from intraabdominal, subcutaneous, or intracranial bleeding. Comparative knockout work situates FX among coagulation factors in development: *"Factor X (FX) deficiency causes partial embryonic lethality between E11.5-12.5. FX-/- mice that were born died from fatal neonatal bleeding"* ([PMID: 11841337](https://pubmed.ncbi.nlm.nih.gov/11841337/)).

**Model recapitulation and limitations.** The mouse knockout **recapitulates fatal neonatal/perinatal hemorrhage** (including intracranial bleeding), mirroring severe human disease. Its principal limitation is **embryonic/perinatal lethality of the complete null**, precluding study of chronic adult disease; hypomorphic/knock-in alleles (e.g., FX Friuli chimeric mice) are needed to model milder, survivable phenotypes.

**Zebrafish.** CRISPR/genome-edited *f10* zebrafish are available and reveal that *"severe defects in the common pathway"* are unexpectedly tolerated ([PMID: 28576875](https://pubmed.ncbi.nlm.nih.gov/28576875/)) — useful for therapeutic screening and pathway-redundancy studies, but a weaker phenocopy of the mammalian bleeding phenotype.

**Applications.** These models support study of coagulation-pathway biology, FX's developmental roles beyond hemostasis, and preclinical testing of replacement and gene-therapy strategies.

**Model resources:** MGI (mouse *F10*), ZFIN (zebrafish *f10*), Alliance of Genome Resources.

---

## Mechanistic Model / Interpretation

```
   Biallelic F10 variant (13q34)
   [missense >> deletion/splice/nonsense]
              |
              v
   down synthesis (type I)  OR  dysfunctional FX protein (type II)
              |
              v
   down functional zymogen FX in plasma
              |
     +--------+--------+
     v                 v
 Extrinsic          Intrinsic
 TF:FVIIa  --->  FX  <---  FIXa:FVIIIa (tenase)
 (PMID 39671302)
     +--------+--------+
              v
        down FXa generated
              |
              v
   down Prothrombinase (FXa.FVa.Ca2+.PL)   (PMID 35427420)
              |
              v
      down Thrombin generation
              |
              v
  down Fibrin + down platelet plug stability   (PMID 35059555)
              |
              v
   BLEEDING  -- severity is inversely proportional to residual FX:C
   (neonatal umbilical/ICH in FX:C <1%;
    mucocutaneous/menorrhagia/hemarthrosis in milder)
```

The central organizing principle is a **dose–response relationship between residual FX coagulant activity and bleeding severity**. Because FX is the single non-redundant convergence node of both coagulation pathways, even partial loss produces a measurable dual PT/APTT prolongation, and profound loss (<1%) produces catastrophic neonatal hemorrhage. Every downstream clinical, diagnostic, prognostic, and therapeutic feature flows from this quantitative relationship: FX:C is simultaneously the diagnostic analyte, the severity classifier, the prognostic biomarker, and the treatment target (maintain FX:C >5 IU/dL).

---

## Evidence Base

| PMID | Contribution | Evidence type |
|------|-------------|---------------|
| [30507709](https://pubmed.ncbi.nlm.nih.gov/30507709/) | AR inheritance, F10/13q34, variant spectrum (22 mutations) | Human, multicentre cohort |
| [35059555](https://pubmed.ncbi.nlm.nih.gov/35059555/) | Domain architecture; 180-variant database; FX's role in thrombin/plug | Human, database/review |
| [35140190](https://pubmed.ncbi.nlm.nih.gov/35140190/) | FX:C <1% ↔ severe bleeding; novel Leu487Phe | Human cohort (Iran) |
| [42506896](https://pubmed.ncbi.nlm.nih.gov/42506896/) | FX:C <5% severe threshold; p.Gln249Pro | Human case series |
| [42144914](https://pubmed.ncbi.nlm.nih.gov/42144914/) | Neonatal umbilical/subgaleal presentation | Human case report |
| [26222694](https://pubmed.ncbi.nlm.nih.gov/26222694/) | Phenotype frequencies; type II via FX:Ag; p.Gly262Asp | Human cohort |
| [41104456](https://pubmed.ncbi.nlm.nih.gov/41104456/) | Traditional & EN-RBD severity classes; multimodal treatment | Human case series |
| [12161341](https://pubmed.ncbi.nlm.nih.gov/12161341/) | FX−/− mouse embryonic lethality + neonatal bleeding | Model organism |
| [11841337](https://pubmed.ncbi.nlm.nih.gov/11841337/) | Comparative coagulation-factor knockouts | Model organism |
| [27797267](https://pubmed.ncbi.nlm.nih.gov/27797267/) | pdFX as safe/effective single-factor therapy | Human trial |
| [35499465](https://pubmed.ncbi.nlm.nih.gov/35499465/) | pdFX prophylaxis dosing | Human review |
| [29707881](https://pubmed.ncbi.nlm.nih.gov/29707881/) | pdFX in children <12; prevalence 1:500k–1M | Human trial |
| [9145616](https://pubmed.ncbi.nlm.nih.gov/9145616/) | Diagnostic assay panel (PT/APTT/RVVT/FX assay) | Human case |
| [28030967](https://pubmed.ncbi.nlm.nih.gov/28030967/) | FX Friuli type II variant; atypical RVVT | Human |
| [35427420](https://pubmed.ncbi.nlm.nih.gov/35427420/) | Cryo-EM prothrombin–prothrombinase (mechanism) | Structural |
| [39671302](https://pubmed.ncbi.nlm.nih.gov/39671302/) | Membrane TF:FVIIa:FX extrinsic complex (mechanism) | Structural/computational |
| [9290823](https://pubmed.ncbi.nlm.nih.gov/9290823/) | Natural feline FX deficiency | Veterinary |
| [28576875](https://pubmed.ncbi.nlm.nih.gov/28576875/) | Zebrafish f10 model; pathway tolerance | Model organism |
| [1530121](https://pubmed.ncbi.nlm.nih.gov/1530121/) | Prophylaxis prevents recurrent ICH | Human case |
| [15036435](https://pubmed.ncbi.nlm.nih.gov/15036435/) | ICH in siblings; HDN misdiagnosis | Human case |
| [41988968](https://pubmed.ncbi.nlm.nih.gov/41988968/) | Reproductive risk, NIPT/PGD prevention | Human review |
| [41836993](https://pubmed.ncbi.nlm.nih.gov/41836993/) | PCC/FFP as alternatives | Human case |
| [30644641](https://pubmed.ncbi.nlm.nih.gov/30644641/) | VKD domain architecture; family evolution | Review |

---

## Limitations and Knowledge Gaps

1. **Rarity limits statistics.** All human evidence derives from case reports and small cohorts (n = 6–24); no large randomized trials or population-scale registries with hard survival endpoints exist. Frequency figures (e.g., 91% epistaxis) come from single small cohorts and may not generalize.
2. **Genotype–phenotype resolution is incomplete.** Although FX:C predicts severity well, the phenotypic heterogeneity among FX:C >40% patients ([PMID: 41104456](https://pubmed.ncbi.nlm.nih.gov/41104456/)) indicates unexplained modifiers; variant-level functional data are sparse for many alleles.
3. **No modifier genes / epigenetics established** — a genuine gap rather than a negative finding.
4. **Model limitations.** The complete FX-null mouse is perinatally lethal, precluding adult-disease modeling; zebrafish tolerate the defect, weakening phenocopy fidelity. Hypomorphic mammalian models for milder disease are underdeveloped.
5. **No dedicated omics.** No transcriptomic, proteomic, or metabolomic signatures specific to congenital FX deficiency were found; the disorder is defined at the single-gene/single-protein level.
6. **Prognostic quantification.** Precise mortality/ICH incidence rates and long-term QoL metrics under modern prophylaxis are not well quantified in the reviewed literature.
7. **Gene therapy absent.** No clinical gene-therapy data for FX deficiency yet exist despite biological plausibility.

---

## Proposed Follow-up Experiments / Actions

1. **Curate a comprehensive genotype–phenotype matrix** from the interactive FX variant database ([PMID: 35059555](https://pubmed.ncbi.nlm.nih.gov/35059555/)), mapping domain-specific variants (GLA vs EGF vs SP) to FX:C and bleeding scores, to explain the FX:C >40% heterogeneity.
2. **Develop hypomorphic / knock-in mouse models** (allelic series reproducing FX:C of ~1%, 5%, 10%) to study survivable chronic disease and test prophylaxis regimens.
3. **Preclinical AAV gene-therapy studies** targeting hepatic F10 expression, using established mouse/zebrafish models to test durability and hemostatic correction.
4. **Prospective natural-history registry** with standardized bleeding scores (ISTH-BAT), FX:C, genotype, and QoL instruments (SF-36/PROMIS) to quantify prognosis under modern pdFX prophylaxis.
5. **Functional characterization of type II variants** (activity-normal-antigen) via recombinant expression and thrombin-generation assays to refine mechanistic classification.
6. **Population carrier-frequency studies** in consanguineous populations using gnomAD-anchored F10 allele frequencies to inform screening programs.

---

## Consensus Answer

Congenital Factor X deficiency (MONDO:0009212; OMIM 227600) is an ultra-rare (~1:500,000–1:1,000,000) autosomal recessive bleeding disorder caused by biallelic, predominantly missense pathogenic variants in **F10** (chromosome 13q34) encoding the vitamin K–dependent serine protease factor X, which sits at the convergence of the extrinsic and intrinsic coagulation pathways. Reduced or dysfunctional FX lowers FXa/prothrombinase assembly and thrombin generation, producing a bleeding phenotype whose severity correlates inversely with residual FX coagulant activity (FX:C): severe disease (FX:C <1%) presents neonatally with umbilical-stump and intracranial hemorrhage, while milder forms cause mucocutaneous bleeding, menorrhagia, and hemarthrosis. It is diagnosed by concurrently prolonged PT and APTT with a confirmatory reduced FX:C assay (FX:Ag distinguishing type I from type II) and managed with factor replacement—high-purity plasma-derived FX concentrate (pdFX/Coagadex) first-line, or PCC/FFP plus antifibrinolytic and hormonal adjuncts—where prophylaxis prevents the otherwise poor outcome of recurrent intracranial hemorrhage.


## Artifacts

- [OpenScientist final report](Congenital_Factor_X_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Congenital_Factor_X_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 35 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 35 |
| On topic | 19 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:39671302` (7 mentions) - Membrane-bound model of the ternary complex between factor VIIa/tissue factor and factor X.
  - shared terms: coagulation

Weighed against this report's own most characteristic terms: `deficiency`, `bleeding`, `disease`, `f10`, `congenital`, `phenotype`, `severe`, `variant`, `coagulation`, `intracranial`, `hemorrhage`, `type`, `clinical`, `severity`, `disorder`, `genotype`, `reduced`, `vitamin`, `cohort`, `pathway`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 26 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 17 |
| Terms whose name is worth a second look | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009212` (3 mentions) - the report calls it "MONDO"; MONDO calls it **congenital factor X deficiency**
- `HP:0001892` (1 mention) - the report calls it "Clinical sign"; HP calls it **Abnormal bleeding**
- `HP:0000421` (1 mention) - the report calls it "Symptom"; HP calls it **Epistaxis**
- `HP:0000978` (1 mention) - the report calls it "Sign"; HP calls it **Bruising susceptibility**
- `HP:0031364` (1 mention) - the report calls it "Sign"; HP calls it **Ecchymosis**
- `HP:0002170` (1 mention) - the report calls it "Sign"; HP calls it **Intracranial hemorrhage**
- `HP:0000132` (1 mention) - the report calls it "Symptom"; HP calls it **Menorrhagia**
- `HP:0008151` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Prolonged prothrombin time**
- `HP:0003645` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Prolonged partial thromboplastin time**
- `HP:0040189` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Scaling skin**
- `CL:0000233` (2 mentions) - the report calls it "platelet", "Platelet (coagulation surface)"; CL calls it **platelet**
- `UBERON:0002107` (1 mention) - the report calls it "Liver (site of FX production)"; UBERON calls it **liver**
- `UBERON:0000955` (1 mention) - the report calls it "Brain / intracranial space"; UBERON calls it **brain**
- `UBERON:0000403` (1 mention) - the report calls it "Scalp / subgaleal space"; UBERON calls it **scalp**
- `UBERON:0000995` (1 mention) - the report calls it "Uterus / endometrium (menorrhagia)"; UBERON calls it **uterus**
- `UBERON:0002097` (1 mention) - the report calls it "Skin / subcutaneous tissue"; UBERON calls it **skin of body**
- `GO:0005783` (1 mention) - the report calls it "Hepatocyte ER (γ-carboxylation, secretion)"; GO calls it **endoplasmic reticulum**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0002320` (1 mention), reported as "Sign" - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0007597` (1 mention) - the report calls it "intrinsic pathway"; GO calls it **blood coagulation, intrinsic pathway**
- `GO:0007598` (1 mention) - the report calls it "extrinsic pathway"; GO calls it **blood coagulation, extrinsic pathway**
- `CL:0000182` (2 mentions) - the report calls it "hepatocytes", "Hepatocyte (synthesis)"; CL calls it **hepatocyte**
- `UBERON:0000178` (1 mention) - the report calls it "Blood / plasma"; UBERON calls it **blood**
- `UBERON:0002331` (1 mention) - the report calls it "Umbilical stump (neonate)"; UBERON calls it **umbilical cord**
- `UBERON:0002217` (1 mention) - the report calls it "Joints / synovial cavity"; UBERON calls it **synovial joint**
- `UBERON:0001707` (1 mention) - the report calls it "Nasal mucosa (epistaxis)"; UBERON calls it **nasal cavity**
- `GO:0005576` (1 mention) - the report calls it "Extracellular region / plasma; PS-containing membranes"; GO calls it **extracellular region**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000233` - called "platelet", "Platelet (coagulation surface)"
- `CL:0000182` - called "hepatocytes", "Hepatocyte (synthesis)"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.