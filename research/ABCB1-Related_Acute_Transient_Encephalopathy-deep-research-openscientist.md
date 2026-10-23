---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-20T23:37:30.854270'
end_time: '2026-10-21T00:10:34.706490'
duration_seconds: 1983.85
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: ABCB1-Related Acute Transient Encephalopathy
  mondo_id: MONDO:0975801
  category: Genetic
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
citation_count: 9
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 6
  validator_version: 0.3.0
term_validation:
  total_terms: 32
  verified: 30
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 19
  labels_matching: 6
  labels_mismatched: 11
  mislabelled_terms:
  - term_id: MONDO:0975801
    reported_labels:
    - MONDO
    ontology_label: encephalopathy, acute transient
  - term_id: HP:0002367
    reported_labels:
    - Symptom
    ontology_label: Visual hallucination
  - term_id: HP:0001257
    reported_labels:
    - Clinical sign
    ontology_label: Spasticity
  - term_id: HP:0001347
    reported_labels:
    - Clinical sign
    ontology_label: Hyperreflexia
  - term_id: HP:0001251
    reported_labels:
    - Clinical sign
    ontology_label: Ataxia
  - term_id: HP:0000651
    reported_labels:
    - Symptom
    ontology_label: Diplopia
  - term_id: HP:0001954
    reported_labels:
    - Trigger-associated
    ontology_label: Recurrent fever
  - term_id: GO:0042493
    reported_labels:
    - response to drug
    ontology_label: GO_0042493
  - term_id: CL:0000540
    reported_labels:
    - neuron, final effector
    ontology_label: neuron
  - term_id: NCIT:C15226
    reported_labels:
    - Supportive Care
    ontology_label: Dilation and Curettage
  - term_id: NCIT:C70742
    reported_labels:
    - Fluid/Hydration Therapy
    ontology_label: Treat
  labels_variant: 2
  obsolete_terms:
  - term_id: GO:0042493
    ontology_label: GO_0042493
    replaced_by: GO:0009410
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ABCB1-Related_Acute_Transient_Encephalopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ABCB1-Related_Acute_Transient_Encephalopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ABCB1-Related Acute Transient Encephalopathy
- **MONDO ID:** MONDO:0975801 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **ABCB1-Related Acute Transient Encephalopathy** covering all of the
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

# ABCB1-Related Acute Transient Encephalopathy (ENPAT): Comprehensive Disease Report

**MONDO:** MONDO:0975801 · **OMIM:** #620950 · **Gene:** *ABCB1* (P-glycoprotein / MDR1) · **Category:** Genetic (autosomal recessive)

---

## Summary

**ABCB1-Related Acute Transient Encephalopathy** — catalogued as **"Encephalopathy, acute transient" (ENPAT; OMIM #620950; MONDO:0975801)** — is an ultra-rare, autosomal recessive neurological disorder caused by **biallelic loss-of-function (LoF) variants in *ABCB1***, the gene encoding **P-glycoprotein (P-gp / MDR1)**, the principal ATP-dependent xenobiotic efflux pump of the blood–brain barrier (BBB). When both *ABCB1* alleles are inactivated, the brain loses its active "chemical defense" at the capillary endothelium. The result is a two-hit disease: a constant genetic lesion (P-gp loss) that becomes clinically manifest only when a **trigger** is applied — either a **P-gp–substrate drug** (classically ivermectin) or the **inflammatory milieu of an acute febrile/afebrile illness**. During these triggers, neurotoxic xenobiotics and/or endogenous cytokines accumulate in the CNS and produce a **recurrent but fully reversible encephalopathy** (irritability, visual hallucinations, ataxia, spasticity, pyramidal signs, obtundation, and coma) that resolves within roughly **24–48 hours** with supportive care, leaving normal cognition, imaging, and metabolic studies between episodes.

The entire human evidence base rests on **two independent 2020 reports**: Seo et al. described monozygotic Korean twin sisters with compound-heterozygous LoF *ABCB1* variants and illness-triggered reversible encephalopathy ([PMID: 32627353](https://pubmed.ncbi.nlm.nih.gov/32627353/)), and Baudou et al. described serious ivermectin toxicity in a patient with *ABCB1* nonsense mutations ([PMID: 32813957](https://pubmed.ncbi.nlm.nih.gov/32813957/)). This narrow human dataset is powerfully corroborated by decades of cross-species models of the same molecular defect: **mdr1a knockout mice** (100-fold ivermectin hypersensitivity, impaired brain cytokine clearance) and **naturally MDR1-mutant herding dogs** (Collies, Australian Shepherds) that develop ivermectin and loperamide neurotoxicity.

The practical take-home is simple and high-impact: the disorder is **preventable and manageable** through **lifelong strict avoidance of P-glycoprotein-substrate medications** plus prompt supportive care (hydration, antipyresis, symptomatic management) during intercurrent illness. There is no gene- or drug-specific therapy; the "treatment" is risk-avoidance and genetic counseling.

---

## 1. Disease Information

**Overview.** ENPAT is a monogenic disorder of **CNS xenobiotic clearance**. Affected individuals are developmentally and cognitively normal and are asymptomatic between episodes. Under a trigger (acute illness or a P-gp-substrate drug), they develop acute, self-limited encephalopathy with full recovery. The MedGen/OMIM definition states: *"Acute transient encephalopathy (ENPAT) is characterized by episodes of neurologic dysfunction following treatment with specific medications or onset of acute illness. Neurologic signs include ataxia, spasticity, pyramidal signs, diplopia, vomiting, obtundation, and coma. Symptoms fully resolve in 24 to 48 hours (Baudou et al., 2020; Seo et al., 2020)."*

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | #620950 (ENPAT) |
| MONDO | MONDO:0975801 |
| UMLS | C5975397 |
| MedGen | CUI C5975397 (concept 1874927) |
| Orphanet | **Not available** (no ORPHAcode on OLS4 cross-reference) |
| ICD-10/ICD-11 | No dedicated code identified |
| MeSH | No dedicated descriptor identified |
| Causal gene | *ABCB1* — HGNC:40; NCBI GeneID 5243; Ensembl ENSG00000085563; UniProt P08183; gene OMIM 171050; locus 7q21.12 |

**Synonyms / alternative names.** Encephalopathy, acute transient (ENPAT); ABCB1-related / P-glycoprotein-deficiency encephalopathy. *Gene aliases:* MDR1, P-gp/P-170, CD243, GP170, PGY1, ABC20, CLCS, ENPAT.

**Information source.** The disease-level entity is aggregated from **individual-patient case reports** (two families) into OMIM/MONDO/MedGen. It is therefore a hybrid: ontology-level identifiers built on a very small number of deeply characterized individual patients, supplemented by model-organism data. *(Evidence: F005; [PMID: 32627353](https://pubmed.ncbi.nlm.nih.gov/32627353/).)*

---

## 2. Etiology

**Primary cause — genetic.** The disease is caused by **biallelic (homozygous or compound-heterozygous) loss-of-function variants in *ABCB1***. In the index family, compound-heterozygous LoF variants were identified: a **nonsense allele p.Pro1182X (p.Gln1182Ter)** and a **splice-donor variant c.2786+1G>T** that disrupts exon 23 splicing (producing an 11-bp deletion / exon skipping / intron retention, all frameshifting). Variants segregated from each non-consanguineous parent, were absent from gnomAD and from 1,020 Korean exomes, and left only ~10% residual wild-type protein. *(F001; [PMID: 32627353](https://pubmed.ncbi.nlm.nih.gov/32627353/): "revealed compound heterozygous loss-of-function variants in ABCB1".)*

**Genetic risk factors.** The causal determinant is the biallelic LoF genotype itself. gnomAD contains ~47 heterozygous *ABCB1* LoF alleles but **no homozygotes**, and the estimated carrier-couple probability of two damaging variants is ~**2.8×10⁻⁸** — explaining the extreme rarity. Heterozygous carriers (including the parents) are clinically unaffected, consistent with recessive inheritance.

**Environmental risk factors / triggers.** The genetic lesion is necessary but not sufficient — disease requires a **trigger**:
1. **Acute illness** — febrile or afebrile intercurrent infection with fever, vomiting, abdominal pain (the illness-triggered form; Seo et al.).
2. **P-gp-substrate drugs** — classically **ivermectin**; by extension, other P-gp substrates (loperamide, vinblastine, vincristine, digoxin, etc.) are expected hazards (the drug-triggered form; Baudou et al.). *(F002, F006; [PMID: 32813957](https://pubmed.ncbi.nlm.nih.gov/32813957/).)*

**Protective factors.** No genetic protective modifier is defined. The principal **environmental protective factor is avoidance of P-gp-substrate drugs** and prompt management of intercurrent illness. Residual ~10% wild-type P-gp in the index patients may partly explain the reversible, non-fatal course.

**Gene–environment interaction.** This disease is a textbook **two-hit gene × environment interaction**: a fixed genetic loss of BBB efflux capacity is unmasked only upon exposure to a pharmacologic or inflammatory "second hit." Neither the genotype alone (carriers, interictal patients) nor the trigger alone (in P-gp-competent individuals at standard doses) produces the phenotype.

---

## 3. Phenotypes

**Core clinical picture (episodic, illness-/drug-triggered, fully reversible):** Both index twins had normal developmental milestones. First acute encephalopathy occurred at age **5 years 6 months**, with recurrent episodes (sometimes simultaneous in both twins), each beginning during acute illness. The stereotyped sequence was: **irritability/agitation → visual hallucinations → progressive drowsiness/obtundation with generalized spasticity and hyperreflexia**, lasting **hours to one day**, with **complete recovery** after hydration and symptomatic care and no seizures or sequelae. At last follow-up (14y3m) growth and cognition were fully normal. *(F004; [PMID: 32627353](https://pubmed.ncbi.nlm.nih.gov/32627353/): "recurrent reversible encephalopathy accompanied by acute febrile or afebrile illness".)*

| Phenotype | Type | HPO suggestion | Characteristics |
|---|---|---|---|
| Acute/episodic encephalopathy | Clinical sign | HP:0006846 (Acute encephalopathy) | Childhood onset; episodic/fluctuating; fully reversible in 24–48 h |
| Irritability / agitation | Behavioral | HP:0000737 / HP:0000713 | Early-episode symptom |
| Visual hallucinations | Symptom | HP:0002367 | Mid-episode |
| Obtundation / coma | Clinical sign | HP:0030151 / HP:0001259 | Peak of episode |
| Spasticity | Clinical sign | HP:0001257 | During episode |
| Hyperreflexia / pyramidal signs | Clinical sign | HP:0001347 | During episode |
| Ataxia | Clinical sign | HP:0001251 | Reported (ENPAT definition) |
| Diplopia | Symptom | HP:0000651 | Reported (ENPAT definition) |
| Vomiting / abdominal pain | Symptom | HP:0002013 / HP:0002027 | Accompany triggering illness |
| Episodic fever | Trigger-associated | HP:0001954 | Marks triggering illness |

**Severity / progression / frequency.** Severity is **variable but self-limited** (can reach coma yet reverses fully). Course is **episodic/relapsing with complete interictal recovery** — *not* progressive. Frequency estimates among affected individuals cannot be derived from n=2 families; within affected individuals episodes are recurrent and triggered.

**Quality-of-life impact.** Between episodes QoL is essentially normal (normal cognition, growth, schooling). Burden derives from unpredictability of episodes, need for vigilant drug avoidance, and risk of severe (coma-level) acute events. No formal EQ-5D/SF-36 data exist.

---

## 4. Genetic / Molecular Information

**Causal gene.** ***ABCB1*** (HGNC:40; GeneID 5243; Ensembl ENSG00000085563; UniProt **P08183** — "ATP-dependent translocase ABCB1 / P-glycoprotein 1," 1280 aa; gene OMIM 171050; 7q21.12). *(F005.)*

**Pathogenic variants (from the two human reports and ClinVar).**

| Variant (HGVS) | Protein | Type | ClinVar | Notes |
|---|---|---|---|---|
| nonsense (index) | p.Pro1182X / p.Gln1182Ter | Nonsense | 3340128 | Index twin allele 1 |
| c.2786+1G>T | splice donor, exon 23 | Splice-site | 3340127 | Index twin allele 2; 11-bp del/exon skip/intron retention, frameshift |
| NM_001348946.2:c.2380C>T | p.Arg794Ter | Nonsense | 3340125 | LoF allele |
| NM_000927.4:c.3053_3056del | frameshift | Frameshift | 3340126 | LoF allele |

**Classification.** LoF alleles are classified **pathogenic/likely pathogenic** per ACMG/AMP (null variants in a gene where LoF is the disease mechanism; PVS1-type). *(F009.)*

**Allele frequency.** Index variants were **absent from gnomAD and 1,020 Korean exomes**. gnomAD carries ~47 heterozygous *ABCB1* LoF alleles, **none homozygous**. Carrier-couple probability of two damaging variants ≈ **2.8×10⁻⁸**.

**Origin & functional consequence.** **Germline**, biallelic, **loss-of-function** (not gain-of-function or dominant-negative). Residual ~10% wild-type protein in the index patients. *(F001.)*

**Modifier genes / epigenetics / chromosomal abnormalities.** None established. No DNA-methylation, histone, or structural/aneuploidy findings are reported for this entity. (Note: common pharmacogenetic *ABCB1* polymorphisms such as C3435T [rs1045642] modulate drug handling and stroke/clopidogrel outcomes [PMID: 32468216; 30742211] but are **not** causes of ENPAT.)

---

## 5. Environmental Information

**Environmental / pharmacologic factors.** The dominant environmental determinant is **exposure to P-glycoprotein-substrate drugs**, above all **ivermectin (CHEBI:6078)** — a classic high-affinity P-gp substrate. In P-gp-deficient individuals, loss of BBB efflux lets ivermectin accumulate centrally and potentiate GABA-/glycine-gated chloride currents, producing CNS depression and coma. *(F006, F008; [PMID: 32813957](https://pubmed.ncbi.nlm.nih.gov/32813957/).)* Other P-gp substrates (loperamide, vinca alkaloids, digoxin, many others — *"A number of clinically relevant, structurally and functionally unrelated drugs are substrates for P-gp,"* [PMID: 15500562](https://pubmed.ncbi.nlm.nih.gov/15500562/)) are presumptive hazards.

**Lifestyle factors.** No specific diet/smoking/alcohol associations are known. Avoidance of offending drugs is the key behavioral factor.

**Infectious agents.** No single pathogen causes the disease. Rather, **any acute febrile/afebrile illness** can act as a nonspecific inflammatory trigger; the mechanistic driver is the **cytokine surge**, not a particular organism. *(F002, F004.)*

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

```
1. Biallelic loss-of-function ABCB1 variants (germline)
        | results in
2. Absent/nonfunctional P-glycoprotein at the luminal membrane of
   brain-capillary endothelial cells (BBB efflux pump lost; ~10% residual WT)
        | leads to
3. Loss of active efflux ("chemical defense") at the blood-brain barrier
        | then -- requires a TRIGGER -- branches:
   +-------------------------------+--------------------------------------+
   | BRANCH A (drug-triggered)     | BRANCH B (illness-triggered)         |
   | 4A. Exposure to P-gp substrate| 4B. Acute febrile/afebrile illness   |
   |     (e.g. ivermectin)         |     -> systemic + CNS cytokine surge |
   |        | results in           |     (IL-1b, TNF, IL-6, CCL2)         |
   | 5A. Drug accumulates in CNS   |        | results in                  |
   |     (verified: brain uptake^) | 5B. Failure to clear cytokines from  |
   |        | leads to             |     brain (shown in Mdr1a/b-/- mice) |
   | 6A. Potentiation of GABA-A /  |        | leads to                     |
   |     glycine Cl- currents ->   | 6B. Sustained neuroinflammatory      |
   |     CNS depression            |     milieu / neuronal dysfunction    |
   +---------------+---------------+------------------+-------------------+
                   | converge on
7. Acute, reversible neuronal dysfunction across cerebral + cerebellar
   cortex and deep gray matter (bilateral)
                   | manifests as
8. Clinical encephalopathy: irritability -> hallucinations -> spasticity,
   hyperreflexia, obtundation, coma
                   | followed by (trigger resolves / drug cleared)
9. Full reversal within 24-48 h, normal interictal state
```

Steps 2, 4A, and 5A are **experimentally demonstrated in patients** ([¹¹C]verapamil PET); step 5B is **demonstrated in the knockout-mouse model**; steps 6A/6B/7 are **mechanistically inferred** from pharmacology and animal data.

### Supporting detail

**Protein dysfunction (upstream lesion).** LoF variants eliminate functional P-gp. **P-gp is the major efflux transporter of the BBB** — *"the mdr1a P-glycoprotein is the major P-glycoprotein in the blood-brain barrier and that its absence results in elevated drug levels in many tissues (especially in brain)"* ([PMID: 7910522](https://pubmed.ncbi.nlm.nih.gov/7910522/)). *(F002.)*

**Direct in-patient demonstration of the efflux defect.** Dynamic **[¹¹C]verapamil PET** showed markedly increased brain uptake/retention in the twins (target-to-reference ratios **3.27 and 2.81**) versus carrier parents (**1.10 / 0.61**) and the wild-type sister (**0.27**) — *"The patient brains displayed substantial loss of xenobiotic clearance ability, as demonstrated by [¹¹C]verapamil positron emission tomography (PET) study."* Uptake was increased throughout cerebral and cerebellar cortex and deep gray matter (thalamus, basal ganglia), bilaterally, with **normal structural MRI**. *(F002, F007.)*

**Cytokine-clearance failure (illness-triggered branch).** In **Mdr1a/b⁻/⁻ mice** given LPS (5 mg/kg IP), brain cytokines (*Il1b, Tnf, Il6, Ccl2*) peaked at 3 h in both genotypes but **failed to clear by 24 h in knockouts** — *"The endogenous cytokine clearance from the brain was also decreased in LPS-treated ABCB1 knockout mice compared to controls."* This provides the mechanistic bridge between an acute illness/cytokine surge and sustained CNS dysfunction. *(F002.)*

**Drug-neurotoxicity pharmacology (drug-triggered branch).** Ivermectin's invertebrate target is the glutamate-gated chloride channel; in mammals at high brain concentrations it potentiates **GABA-A and glycine receptor chloride currents**, producing CNS depression/coma. A 2026 integrative review concluded that *"dysfunction of P-glycoprotein (ABCB1/MDR1)-mediated efflux [is] a central determinant of ivermectin neurotoxicity,"* with *"severe neurotoxic events, including encephalopathy, seizures, coma, and death, occurring after supratherapeutic exposure and, in susceptible individuals, even at standard therapeutic doses"* ([PMID: 41837342](https://pubmed.ncbi.nlm.nih.gov/41837342/)). *(F008.)*

**Molecular pathways / processes.** Core process is **ATP-dependent transmembrane xenobiotic efflux (transport), not classical signaling-cascade dysregulation**. Downstream, neuroinflammatory signaling (IL-1β/TNF/IL-6/CCL2) and inhibitory neurotransmission (GABAergic/glycinergic chloride flux) are implicated.

**Suggested ontology terms.** GO:0140359 (ABC-type transporter activity); GO:0042493 (response to drug); GO:0006805 (xenobiotic metabolic process); GO:0150104 (transport across blood–brain barrier). **Cell types (CL):** brain microvascular endothelial cell / CL:0002139 (endothelial cell of vascular tree); CL:0000129 (microglial cell, downstream neuroinflammation); CL:0000540 (neuron, final effector). **Cellular component (GO):** GO:0016324 (apical plasma membrane).

---

## 7. Anatomical Structures Affected

**Organ level.** The **brain / central nervous system (UBERON:0000955 brain; UBERON:0001017 CNS)** is the clinically affected organ. No primary non-CNS organ dysfunction is reported in affected humans (metabolic, hepatic, renal labs normal interictally). *(F007.)*

**Tissue / cell level.** The lesion localizes to the **blood–brain barrier endothelium** — specifically the **luminal (apical) membrane of brain-capillary endothelial cells (brain microvascular endothelial cell)**. P-gp is also physiologically expressed in intestinal epithelium, renal proximal tubule, biliary canalicular membrane, placenta, and adrenal cortex: *"P-gp is expressed by a variety of normal tissues including the intestines, renal tubular cells, brain capillary endothelial cells, biliary canalicular cells, and others, where it functions to actively extrude substrate drugs"* ([PMID: 15500562](https://pubmed.ncbi.nlm.nih.gov/15500562/)). *(F007.)*

**Subcellular level.** **Apical plasma membrane (GO:0016324)** of endothelial cells; P-gp is an integral membrane ATP-dependent transporter (UniProt P08183).

**Localization & lateralization.** PET showed **bilateral, symmetric** increased tracer retention across cerebral and cerebellar cortex and deep gray nuclei (thalamus **UBERON:0001897**, basal ganglia **UBERON:0002420**, cerebellar cortex **UBERON:0002129**). The process is **diffuse and bilateral**, not focal.

---

## 8. Temporal Development

**Onset.** **Pediatric** onset (first reported episode at **5y6m**), consistent with childhood emergence once ambient drug/illness exposures accumulate. Onset of each episode is **acute**, over hours, triggered.

**Progression.** **Non-progressive at the level of the individual**: the underlying disorder is static (fixed genetic efflux deficit), and neurological function is normal between episodes. The **disease course is episodic / relapsing with complete remission** between attacks; each episode is **self-limited**, resolving within **24–48 hours**.

**Patterns.** Remission is **spontaneous / supportive-care-induced** (hydration, antipyresis, symptom management). The key **critical period = the trigger window** (duration of intercurrent illness or presence of the offending drug); intervention during this window (avoidance/removal of trigger, supportive care) is both preventive and therapeutic. *(F004.)*

---

## 9. Inheritance and Population

**Epidemiology.** **Ultra-rare** — only **two families** reported worldwide (Seo et al. 2020; Baudou et al. 2020). No prevalence or incidence figures exist; no Orphanet epidemiologic class is assigned (no ORPHAcode). Carrier-couple probability of two damaging variants ≈ **2.8×10⁻⁸**. *(F005, F009.)*

**Inheritance.** **Autosomal recessive** (biallelic LoF; unaffected heterozygous parents; variant segregation one allele per parent). **Penetrance is trigger-dependent** — the genotype is fully penetrant for *susceptibility*, but clinical episodes require a trigger (conditional/incomplete clinical penetrance). **Expressivity** appears variable (illness-triggered vs drug-triggered forms; episode severity ranges up to coma). No genetic anticipation (not a repeat-expansion disorder). No founder effect, germline mosaicism, or consanguinity documented (index parents non-consanguineous). Carrier frequency is extremely low (no gnomAD homozygotes). *(F001.)*

**Population demographics.** Reported patients are **Korean (twin sisters, Seo et al.)** and a patient with ivermectin toxicity (Baudou et al.); no ethnic predisposition can be inferred from n=2. **Sex ratio** indeterminate (index cases female). **Age distribution:** childhood-onset based on available cases.

---

## 10. Diagnostics

**Clinical / laboratory tests.** Interictal metabolic workup is **normal** and serves mainly to exclude mimics: serum amino acids, acylcarnitine profile, urine organic acids, venous blood gas, lactate, creatine kinase — all normal; **CSF without infection/inflammation**; **brain MRI normal**; **EEG nonspecific without electrographic seizures**. *(F004.)*

**Imaging / functional biomarker.** **Dynamic [¹¹C]verapamil PET** is the key functional diagnostic, directly demonstrating loss of BBB efflux (increased brain uptake/retention; target-to-reference ratios ~2.8–3.3 in patients vs ~0.3–1.1 in controls/carriers). Structural MRI is normal — a useful discriminator. *(F002.)*

**Genetic testing (diagnostic gold standard).** **Molecular confirmation of biallelic LoF *ABCB1* variants.** Recommended approaches: **whole-exome or whole-genome sequencing** (how the index family was solved — "revealed compound heterozygous loss-of-function variants in ABCB1"), or **targeted *ABCB1* sequencing / gene panels** including copy-number and splice analysis. Chromosomal microarray / karyotype / FISH / mtDNA / repeat-expansion testing are **not applicable** (point/splice LoF mechanism). *(F001, F009.)*

**Diagnostic criteria (proposed; no formal guideline exists).** (1) Recurrent, fully reversible encephalopathy triggered by acute illness or a P-gp-substrate drug; (2) normal interictal exam, MRI, and metabolic studies; (3) biallelic LoF *ABCB1* variants; (4) supportive functional evidence of reduced BBB efflux (e.g., [¹¹C]verapamil PET).

**Differential diagnosis.** Metabolic/mitochondrial encephalopathies (excluded by normal metabolic panels/lactate), acute disseminated encephalomyelitis and infectious/autoimmune encephalitis (excluded by normal CSF/MRI), epileptic encephalopathy (no electrographic seizures), hepatic/uremic/toxic encephalopathy, and other drug-toxicity syndromes.

**Screening.** No newborn screening exists. **Cascade carrier testing** of relatives once a familial variant is identified is appropriate.

---

## 11. Outcome / Prognosis

**Survival / mortality.** No disease-specific mortality reported in the human cases; episodes were fully reversible. However, mechanism and model data indicate that **severe exposures can cause coma and, by extrapolation from animal/pharmacovigilance data, potentially death** (*"encephalopathy, seizures, coma, and death"*, [PMID: 41837342](https://pubmed.ncbi.nlm.nih.gov/41837342/)) — so the condition is potentially life-threatening if a high-dose P-gp-substrate exposure occurs. *(F008.)*

**Morbidity / function.** Between episodes, affected individuals are **functionally normal** (normal growth and cognition at 14y follow-up). No chronic disability was documented. *(F004.)*

**Disease course / recovery.** Excellent recovery potential — **complete resolution within 24–48 h** with supportive care and trigger removal; no cumulative deficit across recurrent episodes in the index family.

**Prognostic factors.** Prognosis depends chiefly on **trigger avoidance and prompt recognition**: the main modifiable risk is inadvertent administration of a P-gp-substrate drug. Residual P-gp activity (e.g., ~10% WT in index patients) may favor reversibility.

---

## 12. Treatment

There is **no gene-specific or disease-modifying therapy**. Management is **avoidance + supportive care**.

**Supportive / symptomatic care (acute episode).** Hydration, antipyresis, and symptomatic treatment (antibiotics for the triggering infection when indicated, antiemetics, antihistamines); episodes resolve without seizures or sequelae. *(F004.)* **NCIT suggestions:** NCIT:C15226 (Supportive Care); NCIT:C70742 (Fluid/Hydration Therapy); NCIT:C25218 (Symptomatic Treatment).

**Pharmacotherapy / pharmacogenomics — the central principle.** **Lifelong strict avoidance of P-glycoprotein-substrate medications**, foremost **ivermectin** (and other avermectins, loperamide, vinca alkaloids, digoxin, and numerous other P-gp substrates). This is a **pharmacogenomic contraindication** driven directly by the *ABCB1*-null genotype. *(F006, F008; [PMID: 32813957](https://pubmed.ncbi.nlm.nih.gov/32813957/).)*

**Advanced / experimental therapeutics.** None established. No gene therapy, cell therapy, RNA therapy, targeted therapy, immunotherapy, surgical, or rehabilitative intervention is indicated or reported. No clinical trials (NCT) target this entity.

**Treatment strategy (personalized medicine).** Genotype-guided prescribing: flag the *ABCB1*-null status in the medical record as an absolute contraindication to P-gp substrates; prophylactically manage intercurrent illness; provide an emergency/anesthesia alert card.

---

## 13. Prevention

**Primary prevention.** For a known affected individual: **avoid P-gp-substrate drugs** and manage febrile illnesses early and aggressively (hydration, antipyresis) to blunt the cytokine-surge trigger. This is the single most effective, actionable intervention.

**Secondary prevention.** Early recognition of prodromal symptoms (irritability, hallucinations) during illness/drug exposure enables prompt supportive care and trigger removal, aborting progression to obtundation/coma.

**Tertiary prevention.** Prevent complications of severe episodes (aspiration, injury during obtundation) with standard supportive/ICU-level care as needed.

**Genetic counseling.** Autosomal recessive counseling: 25% recurrence risk for carrier couples; **cascade carrier testing** of relatives; discussion of prenatal/preimplantation options once the familial variants are known. Emphasize that heterozygous carriers are unaffected. **No immunization or public-health/environmental intervention** applies beyond drug-exposure avoidance. *(F001, F009.)*

---

## 14. Other Species / Natural Disease

This disease has **strong, naturally occurring and engineered animal counterparts**, which constitute much of the supporting evidence base.

| Species | Gene / lesion | Phenotype | PMID |
|---|---|---|---|
| Mouse (*Mus musculus*; NCBI Taxon 10090) | *mdr1a* (Abcb1a) knockout; and Mdr1a/b⁻/⁻ | Viable/fertile; **100-fold ↑ ivermectin sensitivity**, 3-fold ↑ vinblastine; elevated brain drug levels; impaired brain cytokine clearance | [7910522](https://pubmed.ncbi.nlm.nih.gov/7910522/) |
| Mouse (CF-1 strain) | Natural P-gp deficiency | Avermectin neurotoxicity at **100-fold lower** doses; deficiency in **intestinal epithelium and brain capillary endothelium** | [9144452](https://pubmed.ncbi.nlm.nih.gov/9144452/) |
| Dog (*Canis lupus familiaris*; NCBI Taxon 9615) | *MDR1/ABCB1* **4-bp deletion ΔMDR1 295-298** | Ivermectin & loperamide neurotoxicity; ↑ toxicity of P-gp-substrate chemotherapeutics | [15500562](https://pubmed.ncbi.nlm.nih.gov/15500562/); [14765742](https://pubmed.ncbi.nlm.nih.gov/14765742/); [14627096](https://pubmed.ncbi.nlm.nih.gov/14627096/); [11939306](https://pubmed.ncbi.nlm.nih.gov/11939306/) |

**Breeds affected (dog).** Herding breeds — **Collies, Australian Shepherds** (and related). In a northwestern-US Collie sample, **35% were homozygous mutant (affected) and 42% carriers** ([PMID: 11939306](https://pubmed.ncbi.nlm.nih.gov/11939306/)). *"An MDR1 polymorphism in herding breed dogs, including collies and Australian shepherds, has been demonstrated to be the cause of ivermectin sensitivity in these breeds"* ([PMID: 15500562](https://pubmed.ncbi.nlm.nih.gov/15500562/)). *(F003, F006.)*

**Orthologous genes.** Mouse *Abcb1a*/*Abcb1b*; canine *ABCB1 (MDR1)* — all orthologs of human *ABCB1*.

**Comparative biology.** The mechanism is **evolutionarily conserved**: in every species, loss of P-gp removes BBB efflux and produces CNS hypersensitivity to P-gp-substrate neurotoxicants — mechanistically identical to human ENPAT. **Veterinary relevance is high** (ivermectin dosing in herding dogs is a routine clinical concern). **No zoonotic transmission** applies (this is a genetic, non-infectious trait).

---

## 15. Model Organisms

**Mouse (mammalian in vivo).** The **mdr1a (and Mdr1a/b double) knockout mouse** is the definitive model, directly recapitulating (i) loss of BBB efflux and elevated brain xenobiotic levels, (ii) 100-fold ivermectin hypersensitivity, and (iii) impaired brain cytokine clearance after LPS — modeling both the **drug-triggered** and **illness-triggered** branches. *"Disruption of the mouse mdr1a P-glycoprotein gene leads to a deficiency in the blood-brain barrier and to increased sensitivity to drugs"* ([PMID: 7910522](https://pubmed.ncbi.nlm.nih.gov/7910522/)). The naturally P-gp-deficient **CF-1 mouse** is a complementary spontaneous model. *(F002, F003.)*

**Dog (natural large-animal model).** MDR1-mutant Collies / Australian Shepherds provide a **naturally occurring** model of the human disease with a clear drug-trigger phenotype.

**Genetic model types available.** Knockout (constitutive single and double), and natural loss-of-function alleles (CF-1 mouse, MDR1 dog). Humanized/knock-in or conditional models for ENPAT-specific variants are not reported.

**Phenotype recapitulation & limitations.** Models faithfully reproduce the **core efflux defect and drug/cytokine accumulation**, strongly supporting causality. Limitations: the mouse "encephalopathy" is read out as drug sensitivity / cytokine kinetics rather than the full human episodic syndrome; the **transient, fully-reversible childhood clinical course** and the specific human triggers are not fully modeled. **Model databases:** MGI (mouse), IMSR/KOMP (strains), OMIA (canine natural disease). *(F003.)*

---

## Mechanistic Model / Interpretation

ENPAT is best understood as a **single-pump "chemical-firewall" failure** at the blood–brain barrier. P-glycoprotein normally sits on the luminal endothelial membrane and pumps lipophilic xenobiotics (and contributes to clearance of inflammatory mediators) back into the blood. Biallelic *ABCB1* LoF removes this firewall. Because the brain has redundancy and only ~10% residual protein remained in the index patients, the deficit is **clinically silent at baseline** and becomes dangerous only when the system is **loaded** by a second hit:

- **Drug load (Branch A):** a P-gp-substrate drug (ivermectin) that is normally excluded now accumulates centrally and potentiates inhibitory (GABA-A/glycine) chloride currents → CNS depression/coma.
- **Inflammatory load (Branch B):** an acute illness floods the brain with cytokines that, lacking P-gp-assisted clearance, persist (shown directly in knockout mice) → neuroinflammatory encephalopathy.

Both branches converge on **diffuse, bilateral, reversible neuronal dysfunction**, and both resolve once the load is removed — explaining the hallmark 24–48 h reversibility and normal interictal state. This model unifies the two human reports, the PET imaging, the knockout-mouse data, and the canine natural disease into one coherent, cross-species-validated causal chain.

---

## Evidence Base

| PMID | Title (abbrev.) | Role | Evidence type |
|---|---|---|---|
| [32627353](https://pubmed.ncbi.nlm.nih.gov/32627353/) | *Biallelic mutations in ABCB1 display recurrent reversible encephalopathy* | **Defining human report** — genotype, phenotype, [¹¹C]verapamil PET, knockout-mouse cytokine data | Human clinical + model organism |
| [32813957](https://pubmed.ncbi.nlm.nih.gov/32813957/) | *Serious Ivermectin Toxicity and Human ABCB1 Nonsense Mutations* | **Second human report** — drug-triggered form | Human clinical |
| [7910522](https://pubmed.ncbi.nlm.nih.gov/7910522/) | *Disruption of mouse mdr1a P-gp gene leads to BBB deficiency…* | P-gp is major BBB pump; 100-fold ivermectin sensitivity | Model organism |
| [9144452](https://pubmed.ncbi.nlm.nih.gov/9144452/) | CF-1 mice P-gp deficiency | Natural BBB/gut P-gp deficiency → avermectin toxicity | Model organism |
| [15500562](https://pubmed.ncbi.nlm.nih.gov/15500562/) | *Therapeutic implications of the MDR-1 gene* | P-gp tissue distribution; canine MDR1 ivermectin sensitivity; many drugs are substrates | Review |
| [11939306](https://pubmed.ncbi.nlm.nih.gov/11939306/) | MDR1 allele frequency in Collies | Natural canine disease epidemiology (35% affected, 42% carriers) | Veterinary |
| [14627096](https://pubmed.ncbi.nlm.nih.gov/14627096/) / [14765742](https://pubmed.ncbi.nlm.nih.gov/14765742/) | Chemo / loperamide toxicity in MDR1 Collies | Drug-substrate toxicity in natural P-gp deficiency | Veterinary |
| [41837342](https://pubmed.ncbi.nlm.nih.gov/41837342/) | Ivermectin neurotoxicity review (2026) | ABCB1/MDR1 efflux failure = central determinant of ivermectin neurotoxicity | Review |

*Note:* Papers on common *ABCB1* polymorphisms in stroke/clopidogrel (e.g., [PMID: 32468216](https://pubmed.ncbi.nlm.nih.gov/32468216/), [PMID: 30742211](https://pubmed.ncbi.nlm.nih.gov/30742211/)) and methamphetamine/ApoE regulation of ABCB1 ([PMID: 22426312](https://pubmed.ncbi.nlm.nih.gov/22426312/)) are **context / pharmacogenetics**, not evidence for the monogenic ENPAT entity.

---

## Limitations and Knowledge Gaps

1. **Extremely small human dataset (n = 2 families).** Prevalence, incidence, sex ratio, penetrance, expressivity, full phenotypic spectrum, and natural history are poorly constrained. Any frequency statement for individual phenotypes is anecdotal.
2. **No Orphanet code / no ICD / no MeSH descriptor** — the entity is newly minted (2020) and not yet integrated into major epidemiologic/clinical coding systems.
3. **Mechanistic steps 6–8 are inferred**, not directly demonstrated in patients; the exact neurochemical events during a human episode (cytokine vs drug contribution, neurotransmitter effects) have not been measured intra-episode.
4. **Trigger thresholds unknown** — which drugs, at what doses, and which illness severities precipitate episodes in P-gp-null humans is uncharacterized.
5. **Genotype–phenotype relationship** (role of residual ~10% P-gp; whether truly null genotypes are more severe/lethal) is untested.
6. **No therapeutic trials**; management rests entirely on mechanistic reasoning and avoidance.
7. **Model gap:** no mouse/organoid model reproduces the full reversible episodic human syndrome or the specific human variants.

---

## Proposed Follow-up Experiments / Actions

1. **International patient registry & GeneMatcher outreach** to identify additional *ABCB1*-biallelic cases and build genotype–phenotype and natural-history data.
2. **Deep phenotyping during an acute episode** — paired serum/CSF cytokine panels, drug-exposure history, and (where feasible) functional efflux imaging — to confirm the inferred steps (cytokine persistence vs drug accumulation) in humans.
3. **Comprehensive P-gp-substrate "avoid list"** curated from DrugBank/PharmGKB, issued as a patient alert card and EHR allergy/contraindication flag.
4. **iPSC-derived BBB-on-chip / brain-microvascular-endothelial models** carrying the patient variants to test drug/cytokine flux and screen candidate protective strategies.
5. **Humanized or variant knock-in mouse** (ENPAT-specific alleles) with a defined illness/drug challenge to model the reversible episodic phenotype.
6. **Pharmacovigilance mining (FAERS)** for severe ivermectin/loperamide CNS toxicity cases to detect undiagnosed *ABCB1*-null individuals.
7. **ClinVar/gnomAD reanalysis** to refine carrier frequency and search for additional biallelic LoF individuals in large sequencing cohorts.
8. **Formal diagnostic-criteria and genetic-counseling guidance** proposed to ClinGen/ACMG given the clear, actionable pharmacogenomic contraindication.

---

*Evidence-source legend: Human clinical (Seo 2020, Baudou 2020); Model organism (mdr1a/Mdr1a/b-knockout and CF-1 mice); Veterinary natural disease (MDR1 herding dogs); Review/integrative (MDR-1 therapeutics review; 2026 ivermectin neurotoxicity review); Computational (gnomAD/ClinVar/OLS4 queries).*


## Artifacts

- [OpenScientist final report](ABCB1-Related_Acute_Transient_Encephalopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ABCB1-Related_Acute_Transient_Encephalopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 19 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 11 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0975801` (3 mentions) - the report calls it "MONDO"; MONDO calls it **encephalopathy, acute transient**
- `HP:0002367` (1 mention) - the report calls it "Symptom"; HP calls it **Visual hallucination**
- `HP:0001257` (1 mention) - the report calls it "Clinical sign"; HP calls it **Spasticity**
- `HP:0001347` (1 mention) - the report calls it "Clinical sign"; HP calls it **Hyperreflexia**
- `HP:0001251` (1 mention) - the report calls it "Clinical sign"; HP calls it **Ataxia**
- `HP:0000651` (1 mention) - the report calls it "Symptom"; HP calls it **Diplopia**
- `HP:0001954` (1 mention) - the report calls it "Trigger-associated"; HP calls it **Recurrent fever**
- `GO:0042493` (1 mention) - the report calls it "response to drug"; GO calls it **GO_0042493**
- `CL:0000540` (1 mention) - the report calls it "neuron, final effector"; CL calls it **neuron**
- `NCIT:C15226` (1 mention) - the report calls it "Supportive Care"; NCIT calls it **Dilation and Curettage**
- `NCIT:C70742` (1 mention) - the report calls it "Fluid/Hydration Therapy"; NCIT calls it **Treat**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0042493` (GO_0042493) (1 mention) - replaced by `GO:0009410`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000129` (1 mention) - the report calls it "microglial cell, downstream neuroinflammation"; CL calls it **microglial cell**
- `NCIT:C25218` (1 mention) - the report calls it "Symptomatic Treatment"; NCIT calls it **Clinical Intervention or Procedure**, and lists "treatment type" among its other names