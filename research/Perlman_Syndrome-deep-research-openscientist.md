---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-06T19:36:54.967157'
end_time: '2026-11-06T19:52:15.049230'
duration_seconds: 920.08
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Perlman Syndrome
  mondo_id: MONDO:0009965
  category: Mendelian
  causal_genes: DIS3L2
  omim_id: OMIM:267000
  synonyms: nephroblastomatosis - foetal ascites - macrosomia - Wilms tumour; nephroblastomatosis,
    foetal ascites, macrosomia and Wilms tumour; nephroblastomatosis-fetal ascites-macrosomia-Wilms
    tumor syndrome; nephroblastomatosis-fetal ascites-macrosomia-Wilms tumour syndrome;
    renal hamartomas, nephroblastomatosis and fetal gigantism; renal hamartomas, nephroblastomatosis
    and foetal gigantism
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
citation_count: 27
reference_validation:
  total_references: 27
  verified: 27
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 27
  on_topic: 23
  validator_version: 0.5.1
term_validation:
  total_terms: 30
  verified: 28
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 3
  labels_mismatched: 11
  mislabelled_terms:
  - term_id: HP:0001561
    reported_labels:
    - Very frequent
    ontology_label: Polyhydramnios
  - term_id: HP:0001791
    reported_labels:
    - Frequent
    ontology_label: Fetal ascites
  - term_id: HP:0000105
    reported_labels:
    - Very frequent
    ontology_label: Enlarged kidney
  - term_id: HP:0000110
    reported_labels:
    - Frequent
    ontology_label: Renal dysplasia
  - term_id: HP:0001708
    reported_labels:
    - Characteristic precursor
    ontology_label: Right ventricular failure
  - term_id: HP:0002667
    reported_labels:
    - ~64% of neonatal survivors
    ontology_label: Nephroblastoma
  - term_id: HP:0001999
    reported_labels:
    - Characteristic
    ontology_label: Abnormal facial shape
  - term_id: HP:0003271
    reported_labels:
    - Frequent
    ontology_label: Visceromegaly
  - term_id: HP:0001396
    reported_labels:
    - Rare (reported)
    ontology_label: Cholestasis
  - term_id: GO:0006401
    reported_labels:
    - Cellular processes:** RNA catabolism/surveillance
    ontology_label: RNA catabolic process
  - term_id: GO:0005737
    reported_labels:
    - Subcellular compartments:** Cytoplasm
    ontology_label: cytoplasm
  labels_variant: 4
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
  path: Perlman_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Perlman_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Perlman Syndrome
- **MONDO ID:** MONDO:0009965 (if available)
- **Causal gene(s):** DIS3L2
- **OMIM:** OMIM:267000
- **Synonyms:** nephroblastomatosis - foetal ascites - macrosomia - Wilms tumour; nephroblastomatosis, foetal ascites, macrosomia and Wilms tumour; nephroblastomatosis-fetal ascites-macrosomia-Wilms tumor syndrome; nephroblastomatosis-fetal ascites-macrosomia-Wilms tumour syndrome; renal hamartomas, nephroblastomatosis and fetal gigantism; renal hamartomas, nephroblastomatosis and foetal gigantism
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Perlman Syndrome** covering all of the
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

# Perlman Syndrome (DIS3L2): Comprehensive Disease Characteristics Report

**Disease:** Perlman Syndrome
**MONDO ID:** MONDO:0009965 | **OMIM:** 267000 | **Orphanet:** ORPHA:2849
**Causal gene:** **DIS3L2** (DIS3-like 3′→5′ exoribonuclease 2; HGNC:28648; chromosome 2q37.1)
**Inheritance:** Autosomal recessive
**Category:** Mendelian

---

## Summary

Perlman syndrome is a rare, autosomal recessive congenital **overgrowth and Wilms tumor predisposition syndrome** caused by **biallelic loss-of-function variants in the *DIS3L2* gene** on chromosome 2q37.1. *DIS3L2* encodes a cytoplasmic 3′→5′ exoribonuclease of the RNase II/RNB (DIS3) family that specifically recognizes and degrades 3′-oligouridylated RNAs — most famously the uridylated precursors of the let-7 tumor-suppressor microRNA family, but also a broad spectrum of aberrant, highly structured non-coding RNAs. Loss of this RNA-surveillance activity is the initiating molecular lesion of the disease. The causal gene was identified by Astuti et al. in 2012, who mapped the locus to 2q37.1 and demonstrated germline *DIS3L2* mutations in affected individuals, along with somatic *DIS3L2* mutations in sporadic Wilms tumor [PMID: 22306653].

Clinically, Perlman syndrome presents prenatally and neonatally with **polyhydramnios, fetal macrosomia, a distinctive facial dysmorphism, nephromegaly, renal dysplasia with nephroblastomatosis, visceromegaly, facial hypotonia, and multiple congenital anomalies**. The prognosis is poor: most affected neonates die in infancy from respiratory and/or renal failure. Among the minority who survive the neonatal period, approximately **64% develop Wilms tumor and essentially all have developmental delay** [PMID: 18780370]. Because of this high renal cancer risk, Perlman syndrome is formally classified among the Wilms tumor predisposition syndromes, and affected survivors warrant intensive abdominal/renal ultrasound surveillance (typically every ~3 months) per AACR and SIOP-Europe consensus guidelines [PMID: 39466169; PMID: 34134020].

Mechanistically, the disease is best understood as a failure of cytoplasmic RNA quality control. Biallelic *DIS3L2* loss removes oligo(U)-exoribonuclease activity, causing uridylated substrates (pre-let-7 and structured ncRNAs including 7SL/SRP RNA, RMRP, rRNA, tRNA, and snRNA) to accumulate. Downstream, proliferation is derepressed through activation of the **PI3K/AKT signaling pathway** (and AKT–GSK3β signaling), growth-factor dysregulation, and mitotic/spindle abnormalities — a cascade conserved from *Drosophila* to zebrafish to human cells [PMID: 33370287; PMID: 40500755; PMID: 22306653]. Notably, mature let-7 levels are unchanged in DIS3L2-deficient cells and mice, indicating that the tumor-suppressive mechanism is **largely let-7-independent** [PMID: 29950491]. This report integrates nine confirmed findings across the 15 requested domains and flags where evidence is scarce.

---

## Key Findings

### Finding 1 — Perlman syndrome is an autosomal recessive overgrowth disorder caused by biallelic *DIS3L2* loss-of-function

Perlman syndrome results from **homozygous or compound heterozygous mutations in *DIS3L2*** (chromosome 2q37.1; OMIM 267000; MONDO:0009965). The *DIS3L2* gene product is a ribonuclease with homology to the DIS3 component of the RNA exosome. As stated in the Morris et al. review: *"Recently a Perlman syndrome locus was mapped to chromosome 2q37 and homozygous or compound heterozygous mutations were characterized in DIS3L2. The DIS3L2 gene product has ribonuclease activity and homology to the DIS3 component of the RNA exosome"* [PMID: 23613427].

The reported mutational spectrum includes **nonsense** (c.127C>T, p.Arg43Ter), **missense** (c.2381G>A, p.Arg794His), and **frameshift** variants (c.2109delC; c.1829_1830insC), as well as a recurrent **homozygous deletion of exon 9** generated by non-allelic homologous recombination (NAHR) between LINE-1 elements. Igarashi et al. documented this structural variant: *"We report the homozygous deletion of exon 9 of DIS3L2 in a Japanese patient with Perlman syndrome. We identified the deletion junction, and implicate a non-allelic homologous recombination (NAHR) between two LINE-1 (L1) elements as the causative mechanism"* [PMID: 23486540]. This has direct diagnostic importance: large exon-level deletions can be **missed by standard sequencing**, so copy-number-sensitive methods are required to avoid false-negative molecular diagnoses. A compound-heterozygous example (c.2109delC maternal; c.1829_1830insC paternal), classified pathogenic under ACMG criteria (PVS1+PS2+PM2), further enriches the known variant spectrum [PMID: 34964966].

### Finding 2 — DIS3L2 is the 3′→5′ exoribonuclease of the LIN28–TUT4/7–DIS3L2 pathway and a quality-control nuclease for uridylated/structured ncRNAs

DIS3L2 belongs to the **RNase II/RNB family** and is a DIS3 homolog, but — unlike DIS3 and DIS3L1 — it **lacks the PIN domain** and does **not** associate with the core RNA exosome, instead functioning as a free cytoplasmic enzyme. It specifically binds and degrades **3′-oligouridylated RNAs**. In the Lin28–let-7 axis, LIN28A/B recruit the terminal uridylyl transferases TUT4/7 to oligouridylate pre-let-7, which DIS3L2 then degrades. Chang et al. established DIS3L2 as the pathway's missing component: *"Here, we identify the Perlman syndrome-associated protein DIS3L2 as an oligo(U)-binding and processing exoribonuclease that specifically targets uridylated pre-let-7 in vivo. This study establishes DIS3L2 as the missing component of the LIN28-TUT4/7-DIS3L2 pathway required for the repression of let-7 in pluripotent cells"* [PMID: 24141620]. Independent biochemical/structural and cell-based work corroborates this role [PMID: 25119025; PMID: 26080928; PMID: 23594738].

The crystal structure of mouse Dis3l2 bound to oligoU RNA reveals **three RNA-binding domains forming an open funnel** with uracil-specificity interactions spanning the first ~12 nucleotides and three distinct "U-specificity zones" that explain substrate recognition [PMID: 25119025]. Beyond let-7, DIS3L2 performs **quality-control decay (Dis3l2-mediated decay, DMD)** of a wide range of aberrant structured ncRNAs: rRNAs, snRNAs, snoRNAs, tRNAs, 7SL, Y RNAs, the RMRP lncRNA, Pol III transcripts, and mRNAs. As Łabno et al. and Pirouz et al. establish: *"This establishes Dis3l2-mediated decay (DMD) as a quality-control pathway that eliminates aberrant ncRNAs"* [PMID: 27498873], and the cytoplasmic DIS3L2-dependent "uridylome" encompasses a broad spectrum of highly structured, aberrantly processed RNAs [PMID: 27647875]. Critically, in DIS3L2-deficient cell lines and mouse models, **mature let-7 levels are unchanged**, demonstrating that *"DIS3L2 loss has no effect on mature let-7 levels"* [PMID: 29950491] — so tumor suppression is not simply mediated by let-7.

### Finding 3 — Clinical phenotype: fetal overgrowth with high neonatal mortality and Wilms tumor predisposition in survivors

The defining features of Perlman syndrome are **polyhydramnios, fetal macrosomia, characteristic facial dysmorphism, nephromegaly, renal dysplasia and nephroblastomatosis, facial hypotonia, and multiple congenital anomalies**. Most patients die in infancy from respiratory and/or renal failure; survivors have developmental delay and a high Wilms tumor risk. The *Three Siblings* case report notes: *"The majority of patients die in infancy due to respiratory and/or renal failure, limiting the reports of patients surviving into childhood"* [PMID: 40704758].

A **genotype–phenotype correlation** is emerging: the homozygous exon-9 deletion is associated with poor survival, while some missense or partial-function alleles (e.g., p.Arg794His) permit prolonged survival into childhood. A recent case report states: *"Survival is predicted by differences among various germline mutations in the DIS3L2 gene on chromosome 2q37.1, with prolonged survival documented in heterozygous mutations allowing partial exoribonuclease function"* [PMID: 42040973]. For Wilms tumor development, a **two-hit model** operates, combining a germline *DIS3L2* lesion with a somatic second hit: *"revealed 1 somatic mutation and 1 familial germline mutation in the DIS3L2 gene, suggesting a 2-hit causation of Wilms tumor"* [PMID: 35700413].

### Finding 4 — DIS3L2 loss drives overgrowth via PI3K/AKT activation and impaired RNA surveillance; recapitulated across model organisms

The proliferative mechanism is conserved and PI3K/AKT-dependent. In *Drosophila*, dis3L2-null and nuclease-dead lines show **catalytic-activity-dependent overproliferation** driven by the growth factor **Idgf2** (homolog of human chitinase-like CHI3L1/YKL-40); in human HEK-293T kidney cells, DIS3L2 loss increases proliferation and activates PI3-Kinase/AKT signaling. Towler et al. report: *"we show that loss of DIS3L2 results in an increase in the PI3-Kinase/AKT signalling pathway, which we subsequently show to contribute towards the proliferation phenotype"* [PMID: 33370287].

In **zebrafish**, dis3l2 morphants show neural crest apoptosis, mitotic/spindle defects, and Akt–GSK3β dysregulation: *"dis3l2 regulates neural tissue apoptosis and progenitor functions through the Akt-GSK3β signaling pathway"* [PMID: 40500755]. At the subcellular level, DIS3L2-mediated decay **safeguards 7SL/SRP-dependent ER-targeted translation and ER calcium homeostasis**; its loss causes sustained 7SL uridylation, calcium leak, and impaired stem-cell differentiation: *"Upon DIS3L2 loss, sustained 3'-end uridylation of aberrant 7SL RNA impacts ER-targeted translation and causes ER calcium leakage"* [PMID: 32457326].

### Finding 5 — Gene discovery: germline *DIS3L2* mutations cause Perlman syndrome; DIS3L2 regulates mitosis and cell growth and is mutated in sporadic Wilms tumor

The landmark gene-discovery paper (Astuti et al., 2012, *Nature Genetics*) mapped the Perlman locus and identified the causal gene: *"We mapped a previously unknown susceptibility locus to 2q37.1 and identified germline mutations in DIS3L2, a homolog of the Schizosaccharomyces pombe dis3 gene, in individuals with Perlman syndrome"* [PMID: 22306653]. The same study established DIS3L2's tumor-suppressor function and its relevance to sporadic (non-syndromic) Wilms tumor: *"DIS3L2 inactivation was associated with mitotic abnormalities and altered expression of mitotic checkpoint proteins. DIS3L2 overexpression suppressed the growth of human cancer cell lines, and knockdown enhanced the growth of these cells. We also detected evidence of DIS3L2 mutations in sporadic Wilms tumor"* [PMID: 22306653]. Thus DIS3L2 bridges a rare Mendelian overgrowth syndrome and common pediatric kidney cancer biology.

### Finding 6 — Perlman syndrome is a Wilms tumor predisposition syndrome warranting renal ultrasound surveillance

Perlman syndrome is classified among the Wilms tumor (WT) predisposition syndromes by consensus guidelines. The AACR Pediatric Cancer Working Group update notes: *"members of the AACR Pediatric Cancer Working Group met to update surveillance guidelines for patients with a predisposition to Wilms tumors with a review of recently published evidence and risk estimates"* [PMID: 39466169; PMID: 39320341]. The SIOP-Europe Host Genome Working Group provides an independent consensus: *"the International Society of Pediatric Oncology (SIOP)-Europe Host Genome Working Group and SIOP Renal Tumour Study Group hereby present updated WT surveillance guidelines"* [PMID: 34134020]. These groups recommend **abdominal/renal ultrasound surveillance (typically every ~3 months)** in children at increased WT risk.

Nephroblastomatosis/nephrogenic rests are the precursor lesions for Wilms tumor. Importantly, a large SIOP-WT-2001 analysis found that in **unilateral** Wilms tumor cohorts, the presence of nephrogenic rests did **not** independently worsen relapse-free or overall survival, indicating they are precursor markers rather than independent adverse prognostic factors once a tumor has formed [PMID: 42535789].

### Finding 7 — Prognosis quantified: high neonatal mortality; ~64% of neonatal survivors develop Wilms tumor and all have developmental delay

Alessandri et al. (2008) reviewed 28 reported Perlman syndrome patients and quantified the natural history. The prognosis is poor with high neonatal mortality: *"The prognosis of Perlman syndrome is poor with a high neonatal mortality rate"* [PMID: 18780370]. Among those surviving the neonatal period: *"Among the infants who survived beyond the neonatal period, 64% developed a WT and all had a developmental delay"* [PMID: 18780370]. Frequent manifestations include fetal macrosomia, ascites, polyhydramnios, nephromegaly, renal dysplasia, nephroblastomatosis, and distinctive facies.

Regarding inheritance in practice, reported sibships showed **parental consanguinity in only 2 of 7 families**: *"We review 19 patients from seven sibships with parental consanguinity in two families only"* [PMID: 18780370] — consistent with sporadic autosomal recessive occurrence rather than a requirement for consanguinity. **Cholestasis** has also been reported as a possibly novel feature [PMID: 20726997].

### Finding 8 — Clinical overlap with other overgrowth syndromes but molecular distinction from imprinting disorders

Perlman syndrome shares features (macrosomia, visceromegaly, Wilms tumor risk) with **Beckwith-Wiedemann syndrome** (BWS; 11p15 imprinting/CDKN1C) and **Simpson-Golabi-Behmel syndrome** (SGBS; GPC3), prompting frequent diagnostic confusion [PMID: 18780370; PMID: 24215131; PMID: 38161545]. *"Clinical overlaps with other overgrowth syndromes particularly Beckwith-Wiedemann syndrome and Simpson-Golabi-Behmel syndrome have been emphasized"* [PMID: 18780370].

However, in molecularly confirmed Perlman cases, the 11p15 region/CDKN1C and GPC3 were specifically excluded: *"Genetic or epigenetic alterations of the 11p15 region (involved in the BWS), including mutation of the CDKN1C gene were excluded. No mutation of the GPC3 gene was identified"* [PMID: 18780370]. This establishes Perlman as a **distinct autosomal recessive DIS3L2 disorder**, not an imprinting (BWS) or X-linked (SGBS) condition. Diagnosis therefore requires demonstration of **biallelic *DIS3L2* variants**, with care to detect large exon-9 deletions missed by sequencing [PMID: 23486540; PMID: 22306653].

### Finding 9 — Integrated causal chain: biallelic DIS3L2 loss → RNA-surveillance failure → PI3K/AKT-driven overgrowth and tumorigenesis (largely let-7-independent)

Synthesis of the mechanistic evidence defines the Perlman pathophysiology as a stepwise cascade (detailed in the Mechanistic Model below). The key integration points: (1) biallelic *DIS3L2* loss removes cytoplasmic 3′→5′ oligo(U)-exoribonuclease activity [PMID: 22306653; PMID: 25119025]; (2) uridylated substrates accumulate via failed DIS3L2-mediated decay [PMID: 24141620; PMID: 23594738; PMID: 27498873; PMID: 27647875; PMID: 32457326]; (3) proliferation is derepressed through elevated PI3K/AKT (and AKT-GSK3β) signaling and growth-factor dysregulation, with mitotic/spindle defects [PMID: 33370287; PMID: 40500755; PMID: 22306653]; (4) mature let-7 is unchanged, so tumor suppression is **largely let-7-independent** [PMID: 29950491]; (5) the pathway is conserved from *Drosophila* to humans [PMID: 33370287]. The clinical outcome is fetal overgrowth, nephroblastomatosis, and Wilms tumor (via two-hit somatic inactivation) [PMID: 35700413].

---

## Section-by-Section Report

### 1. Disease Information

Perlman syndrome (MONDO:0009965; OMIM 267000; Orphanet ORPHA:2849) is a **rare autosomal recessive congenital overgrowth syndrome with Wilms tumor predisposition**, caused by biallelic variants in **DIS3L2**. It was first described clinically by Perlman and colleagues as a familial syndrome of renal hamartomas, nephroblastomatosis, and fetal gigantism.

- **Key identifiers:** OMIM 267000; MONDO:0009965; Orphanet ORPHA:2849; causal gene DIS3L2 (HGNC:28648). MeSH does not maintain a dedicated descriptor; the condition is typically indexed under overgrowth syndromes / Wilms tumor predisposition. ICD-10 lacks a specific code (grouped under congenital malformation syndromes, e.g., Q87.3 overgrowth syndromes); ICD-11 similarly groups it under syndromic overgrowth.
- **Synonyms:** nephroblastomatosis–fetal ascites–macrosomia–Wilms tumor syndrome; renal hamartomas, nephroblastomatosis and fetal gigantism.
- **Information source:** Knowledge is derived almost entirely from **aggregated disease-level resources and small case series/case reports** (fewer than ~40 molecularly or clinically reported patients worldwide), not from large EHR cohorts.

### 2. Etiology

- **Disease causal factors:** Purely **genetic** — biallelic (homozygous or compound heterozygous) loss-of-function variants in *DIS3L2* [PMID: 22306653; PMID: 23613427]. No environmental or infectious cause.
- **Genetic risk factors:** The causal variants themselves (nonsense, frameshift, missense, and the recurrent exon-9 deletion) are the risk determinants. Wilms tumor development additionally requires a **somatic second hit** at *DIS3L2* (two-hit model) [PMID: 35700413]. Somatic *DIS3L2* mutations also occur in sporadic Wilms tumor [PMID: 22306653].
- **Environmental risk factors:** None established. Consanguinity increases the chance of homozygosity but was present in only 2 of 7 reported sibships [PMID: 18780370].
- **Protective factors:** No genetic or environmental protective factors are documented. By inference, **residual exoribonuclease activity** from partial-function (e.g., missense p.Arg794His) alleles is associated with prolonged survival, functioning as a modifier of severity rather than a protective factor per se [PMID: 42040973].
- **Gene–environment interactions:** None documented; this is a highly penetrant Mendelian disorder.

### 3. Phenotypes

| Phenotype | Type | Onset | Frequency | Suggested HPO |
|---|---|---|---|---|
| Polyhydramnios | Prenatal sign | Fetal | Very frequent | HP:0001561 |
| Fetal macrosomia / overgrowth | Physical | Fetal/neonatal | Very frequent | HP:0001520, HP:0000098 |
| Fetal ascites | Clinical sign | Fetal | Frequent | HP:0001791 |
| Nephromegaly | Physical | Neonatal | Very frequent | HP:0000105 |
| Renal dysplasia | Structural | Congenital | Frequent | HP:0000110 |
| Nephroblastomatosis / nephrogenic rests | Pathologic | Congenital | Characteristic precursor | HP:0001708 |
| Wilms tumor (nephroblastoma) | Neoplasm | Infancy/childhood | ~64% of neonatal survivors | HP:0002667 |
| Distinctive facial dysmorphism | Physical | Congenital | Characteristic | HP:0001999 |
| Facial/generalized hypotonia | Neurologic | Neonatal | Frequent | HP:0000297 / HP:0001252 |
| Developmental delay / intellectual disability | Neurologic | Infancy | ~100% of survivors | HP:0001263 / HP:0001249 |
| Visceromegaly / organomegaly | Physical | Congenital | Frequent | HP:0003271 |
| Cholestasis | Lab/clinical | Neonatal | Rare (reported) | HP:0001396 |

- **Severity:** Severe; most neonates die of respiratory/renal failure [PMID: 40704758; PMID: 18780370].
- **Progression:** Largely congenital/static for malformations; Wilms tumor risk is progressive through early childhood.
- **Quality of life:** Severe impact — high neonatal mortality, and universal developmental delay plus cancer surveillance burden in survivors [PMID: 18780370].

### 4. Genetic / Molecular Information

- **Causal gene:** *DIS3L2* (2q37.1; HGNC:28648; UniProt Q8IYB7). Encodes a cytoplasmic 3′→5′ exoribonuclease (RNase II/RNB family, DIS3 homolog) lacking the PIN domain and exosome association [PMID: 22306653].
- **Variant classes:** nonsense (p.Arg43Ter), missense (p.Arg794His), frameshift (c.2109delC; c.1829_1830insC), and the recurrent **homozygous exon-9 deletion** via LINE-1 NAHR [PMID: 22306653; PMID: 23486540; PMID: 34964966; PMID: 42040973].
- **Variant classification:** Reported variants classified **pathogenic** under ACMG/AMP criteria (e.g., PVS1+PS2+PM2) [PMID: 34964966].
- **Allele frequency:** Pathogenic alleles are exceedingly rare in population databases (gnomAD); no common founder allele established, though the exon-9 deletion recurs via a shared LINE-1 recombination mechanism.
- **Somatic vs germline:** Germline biallelic variants cause the syndrome; **somatic** *DIS3L2* mutations occur in both syndromic (second hit) and sporadic Wilms tumor [PMID: 22306653; PMID: 35700413].
- **Functional consequence:** **Loss of function** (loss of exoribonuclease/RNA-surveillance activity). Tumor-suppressor behavior is demonstrated: overexpression suppresses and knockdown enhances cancer-cell growth [PMID: 22306653].
- **Modifier genes / epigenetics:** No specific modifier genes identified; residual enzyme activity modifies severity (inferred) [PMID: 42040973]. Unlike BWS, Perlman is **not** an imprinting disorder — 11p15/CDKN1C epigenetic alterations are excluded [PMID: 18780370].
- **Chromosomal abnormalities:** The locus is 2q37.1; the exon-9 deletion is a submicroscopic structural variant, not a visible cytogenetic abnormality [PMID: 23486540].

### 5. Environmental Information

**Not applicable.** No environmental factors, lifestyle factors, toxins, or infectious agents are implicated. Perlman syndrome is a fully genetic Mendelian disorder [PMID: 22306653; PMID: 23613427].

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic loss-of-function variants in *DIS3L2*** (homozygous/compound heterozygous) **result in** loss of functional cytoplasmic 3′→5′ oligo(U)-exoribonuclease [PMID: 22306653; PMID: 25119025].
2. Loss of DIS3L2 catalytic activity **leads to** failure of Dis3l2-mediated decay (DMD) of 3′-oligouridylated RNAs [PMID: 27498873].
3. DMD failure **results in** accumulation of uridylated substrates: pre-let-7 and aberrant structured ncRNAs (7SL/SRP RNA, RMRP, rRNA, tRNA, snRNA, Y RNA) [PMID: 24141620; PMID: 23594738; PMID: 27647875; PMID: 32457326].
4a. Accumulation of aberrant 7SL RNA **leads to** impaired ER-targeted translation and ER calcium leakage, disturbing cell homeostasis and stem-cell differentiation [PMID: 32457326].
4b. (Branch) Loss of DIS3L2 **leads to** increased **PI3K/AKT signaling** and growth-factor dysregulation (Idgf2/CHI3L1 homolog in *Drosophila*), **resulting in** cell overproliferation [PMID: 33370287].
4c. (Branch) Loss of DIS3L2 **leads to** mitotic abnormalities, altered mitotic-checkpoint protein expression, and AKT–GSK3β dysregulation (*inferred to contribute* to overgrowth and neural-crest apoptosis) [PMID: 22306653; PMID: 40500755].
5. Overproliferation and dysregulated growth signaling **result in** fetal overgrowth (macrosomia, visceromegaly, nephromegaly) and nephroblastomatosis [PMID: 18780370].
6. A **somatic second hit** at *DIS3L2* in a nephrogenic rest **leads to** Wilms tumor (two-hit model) [PMID: 35700413].
7. Note: mature **let-7 is unchanged** in DIS3L2-deficient cells/mice, so tumor suppression is **largely let-7-independent** — the operative driver is the broader RNA-surveillance failure converging on PI3K/AKT [PMID: 29950491].

- **Molecular pathways:** PI3K/AKT (GO:0043491), AKT-GSK3β; LIN28–TUT4/7–DIS3L2 uridylation/decay axis.
- **Cellular processes:** RNA catabolism/surveillance (GO:0006401), mitotic cell cycle regulation (GO:0007346), apoptosis (GO:0006915, neural crest), ER-targeted translation, calcium homeostasis.
- **Protein dysfunction:** Loss of function of the exoribonuclease; open-funnel 3-RBD architecture recognizing oligoU over ~12 nt [PMID: 25119025].
- **Subcellular compartments:** Cytoplasm (GO:0005737), endoplasmic reticulum (GO:0005783), spindle/mitotic apparatus.
- **Cell types:** Renal progenitor/blastemal cells (nephroblastomatosis → Wilms), neural crest cells, pluripotent/stem cells.
- **Suggested GO/CL terms:** GO:0000175 (3′-5′ exoribonuclease activity), GO:0071028 (nuclear mRNA surveillance — analogous cytoplasmic QC), GO:0043491 (PI3K/AKT); renal blastemal cell / nephron progenitor cell.

### 7. Anatomical Structures Affected

- **Primary organ:** **Kidney** (UBERON:0002113) — nephromegaly, renal dysplasia, nephroblastomatosis, Wilms tumor.
- **Secondary/other organs:** Liver and other viscera (visceromegaly; cholestasis reported) [PMID: 20726997]; lungs (respiratory failure as cause of death); brain/CNS (developmental delay, hypotonia); craniofacial structures (dysmorphism).
- **Body systems:** Renal/urinary, nervous, hepatobiliary, musculoskeletal (overgrowth), respiratory (secondary failure).
- **Tissue/cell level:** Renal metanephric blastema / nephrogenic rests (precursor to Wilms tumor); neural crest derivatives.
- **Subcellular:** Cytoplasm and ER (RNA decay, SRP-dependent translation, calcium homeostasis) [PMID: 32457326].
- **Localization/lateralization:** Nephromegaly and nephroblastomatosis are typically **bilateral**; Wilms tumor may be unilateral or bilateral.
- **Suggested UBERON terms:** UBERON:0002113 (kidney), UBERON:0002107 (liver), UBERON:0000955 (brain), UBERON:0002048 (lung).

### 8. Temporal Development

- **Onset:** **Congenital/prenatal** — detected in utero via polyhydramnios, macrosomia, ascites, and nephromegaly; often diagnosed prenatally or at birth [PMID: 24215131; PMID: 38161545].
- **Progression:** Malformations are congenital; the dominant evolving risk is **Wilms tumor**, arising in infancy/early childhood from nephroblastomatosis.
- **Course/duration:** High neonatal mortality from respiratory/renal failure; survivors have a chronic, lifelong course marked by developmental delay and cancer surveillance [PMID: 40704758; PMID: 18780370].
- **Critical period:** Early childhood is the window of maximal Wilms tumor risk and the rationale for intensive ultrasound surveillance [PMID: 39466169; PMID: 34134020].

### 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive** [PMID: 22306653].
- **Penetrance:** High/essentially complete for the overgrowth phenotype; Wilms tumor penetrance ~64% among neonatal survivors [PMID: 18780370].
- **Expressivity:** Variable, correlating with residual enzyme activity (genotype–phenotype gradient) [PMID: 42040973].
- **Epidemiology:** **Extremely rare** (fewer than ~40 reported patients); no reliable prevalence/incidence estimates — Orphanet lists it as <1/1,000,000. Both sexes affected; no strong sex bias documented.
- **Consanguinity:** Contributory but not required (2/7 reported sibships) [PMID: 18780370].
- **Founder effect / carrier frequency:** No established founder allele; carrier frequency unknown (too rare for reliable gnomAD estimates). The exon-9 deletion recurs via LINE-1-mediated NAHR rather than common ancestry [PMID: 23486540].

### 10. Diagnostics

- **Prenatal/imaging:** Ultrasound showing polyhydramnios, macrosomia, fetal ascites, bilateral nephromegaly, and characteristic renal appearance; CT/MRI of renal abnormalities [PMID: 18780370; PMID: 20726997; PMID: 24215131].
- **Laboratory:** No specific biomarker; cholestasis (elevated conjugated bilirubin) reported [PMID: 20726997].
- **Genetic testing (confirmatory):** Demonstration of **biallelic pathogenic *DIS3L2* variants**. Recommended approaches: whole-exome sequencing (WES) or targeted overgrowth/Wilms-predisposition gene panels; Sanger confirmation. **Copy-number/deletion analysis (e.g., MLPA, exon-level CMA) is essential** because large deletions (exon 9) are missed by sequence-only approaches [PMID: 22306653; PMID: 23486540; PMID: 34964966].
- **Histopathology:** Renal dysplasia, nephroblastomatosis/nephrogenic rests, and Wilms tumor on biopsy/nephrectomy specimens [PMID: 42535789].
- **Clinical criteria & differential diagnosis:** No formal consensus criteria; diagnosis is clinical-plus-molecular. Key differentials: **Beckwith-Wiedemann syndrome** (11p15 imprinting/CDKN1C), **Simpson-Golabi-Behmel syndrome** (GPC3), prune belly syndrome, and WT1-related syndromes (Denys-Drash) — distinguished by their molecular tests and by excluding 11p15/GPC3 alterations [PMID: 18780370; PMID: 24215131; PMID: 38161545; PMID: 34106634].
- **Screening/surveillance:** Serial **renal/abdominal ultrasound ~every 3 months** in survivors for early Wilms tumor detection [PMID: 39466169; PMID: 34134020].

### 11. Outcome / Prognosis

- **Mortality:** **High neonatal mortality** from respiratory and/or renal failure; the majority die in infancy [PMID: 40704758; PMID: 18780370].
- **Survivor outcomes:** Among neonatal survivors, **~64% develop Wilms tumor and essentially all have developmental delay** [PMID: 18780370].
- **Prognostic factors:** Genotype is the dominant prognostic factor — **residual exoribonuclease activity** (partial-function/missense alleles) predicts prolonged survival, whereas the homozygous exon-9 deletion predicts poor survival [PMID: 42040973; PMID: 40704758].
- **Complications:** Renal failure, respiratory failure, Wilms tumor, developmental/intellectual disability, cholestasis [PMID: 18780370; PMID: 20726997].
- **Wilms-tumor-specific prognosis:** Wilms tumor in general has favorable survival with standard therapy; presence of nephrogenic rests did not worsen relapse/overall survival in unilateral WT cohorts [PMID: 42535789].

### 12. Treatment

There is **no disease-specific or curative therapy**; management is supportive and oncologic.

- **Supportive/neonatal care:** Respiratory and renal support for critically ill neonates; nutritional support; management of cholestasis [PMID: 40704758; PMID: 20726997]. (NCIT: supportive care C15277.)
- **Wilms tumor therapy:** Standard pediatric nephroblastoma protocols — **surgery (nephrectomy/nephron-sparing)**, **chemotherapy** (vincristine, actinomycin-D ± doxorubicin per SIOP/COG), and radiotherapy for higher-stage disease [PMID: 42535789; PMID: 34503817]. (NCIT: nephrectomy C15387; chemotherapy C15632.)
- **Surveillance as management:** Intensive renal ultrasound to enable early, organ-sparing tumor resection [PMID: 39466169; PMID: 34134020].
- **Pharmacogenomics / advanced/targeted/gene/cell/RNA therapies:** **None established.** Mechanistically, the PI3K/AKT axis is a plausible future target (inferred from [PMID: 33370287]), but no clinical interventions exist.
- **Rehabilitation:** Developmental support/early intervention for survivors with developmental delay [PMID: 18780370].

### 13. Prevention

- **Primary prevention:** Not possible (germline genetic disorder). **Genetic counseling** for at-risk families, with 25% recurrence risk per pregnancy for carrier couples.
- **Reproductive options:** Prenatal diagnosis and **preimplantation genetic testing** where the familial variants are known; prenatal ultrasound can raise suspicion (polyhydramnios, macrosomia, nephromegaly, ascites) [PMID: 24215131; PMID: 38161545].
- **Secondary/tertiary prevention:** **Renal ultrasound surveillance** (~every 3 months) in affected survivors to detect Wilms tumor early and prevent advanced-stage complications [PMID: 39466169; PMID: 34134020].
- **Counseling:** Genetic counseling regarding autosomal recessive inheritance, carrier testing of parents/relatives, and the role of consanguinity (contributory but not required) [PMID: 18780370].

### 14. Other Species / Natural Disease

- **Orthologous genes:** *DIS3L2* is conserved; functional orthologs studied in mouse (*Dis3l2*), zebrafish (*dis3l2*), and *Drosophila* (*dis3L2*), and the ancestral *dis3* in *S. pombe* [PMID: 22306653; PMID: 33370287; PMID: 40500755].
- **Natural disease in other species:** No naturally occurring Perlman-syndrome-equivalent disease is documented in companion animals or wildlife (not reported in OMIA).
- **Comparative biology:** The DIS3L2 RNA-surveillance and PI3K/AKT overgrowth mechanism is **evolutionarily conserved from flies to humans**, validating cross-species modeling [PMID: 33370287].
- **Zoonotic/transmission:** Not applicable (non-infectious genetic disorder).

### 15. Model Organisms

| Model | Type | Key findings | Recapitulation | PMID |
|---|---|---|---|---|
| *Drosophila* dis3L2-null / nuclease-dead | Invertebrate, genetic | Catalytic-activity-dependent overproliferation via Idgf2; PI3K/AKT link | Overgrowth/proliferation mechanism | [PMID: 33370287] |
| Zebrafish dis3l2 morphant | Vertebrate | Neural crest apoptosis, mitotic/spindle defects, Akt-GSK3β dysregulation | Developmental + signaling aspects | [PMID: 40500755] |
| Mouse embryonic stem cells / Dis3l2 knockdown | Mammalian cellular | pre-let-7 stabilization; mature let-7 unchanged; DMD of ncRNAs | Molecular/RNA-surveillance | [PMID: 23594738; PMID: 29950491; PMID: 27498873] |
| Human HEK-293T (kidney) DIS3L2 loss | In vitro human | Increased proliferation + PI3K/AKT activation | Proliferation mechanism in kidney cells | [PMID: 33370287] |
| Human cell lines (CLIP uridylome; 7SL/ER) | In vitro human | Broad uridylome; 7SL/SRP, ER translation, Ca²⁺ leak | Subcellular mechanism | [PMID: 27647875; PMID: 32457326] |

- **Model types available:** Invertebrate (fly), vertebrate (zebrafish), mammalian cellular (mouse ESC), and human cell lines.
- **Limitations:** No reported mouse model fully recapitulates the complete human syndromic phenotype (overgrowth + nephroblastomatosis + Wilms tumor) in a single system; models emphasize isolated mechanistic aspects. Loss of *DIS3L2* does **not** alter mature let-7, so let-7-centric models do not capture the tumor-suppressive mechanism [PMID: 29950491].
- **Resources:** MGI (mouse), ZFIN (zebrafish), FlyBase (*Drosophila*).

---

## Mechanistic Model / Interpretation

```
   Biallelic DIS3L2 loss-of-function (2q37.1)
   (nonsense / frameshift / missense / exon-9 LINE-1 NAHR deletion)
                         │  [PMID 22306653, 23486540]
                         ▼
   Loss of cytoplasmic 3'->5' oligo(U) exoribonuclease activity
                         │  [PMID 24141620, 25119025]
                         ▼
   Failure of Dis3l2-mediated decay (DMD) of 3'-uridylated RNAs
                         │  [PMID 27498873, 27647875]
          ┌──────────────┼───────────────────────────┐
          ▼              ▼                            ▼
  pre-let-7           aberrant 7SL / SRP RNA       rRNA/tRNA/snRNA/
  accumulates         accumulates                  RMRP accumulate
          │              │  [PMID 32457326]           │
          │              ▼                            │
          │      impaired ER translation +            │
          │      ER Ca2+ leak; stem-cell defects      │
          │                                           │
          ▼ (NOTE: mature let-7 UNCHANGED)            │
   let-7-INDEPENDENT ────────────────────────────────┘
          │  [PMID 29950491]
          ▼
   PI3K/AKT activation (+ AKT-GSK3beta), growth-factor (Idgf2)
   dysregulation, mitotic/spindle & checkpoint abnormalities
                         │  [PMID 33370287, 40500755, 22306653]
                         ▼
   Cell overproliferation / impaired apoptosis
                         │
                         ▼
   Fetal overgrowth: macrosomia, visceromegaly, nephromegaly,
   nephroblastomatosis, dysmorphism, developmental delay
                         │  [PMID 18780370, 40704758]
                         ▼
   + somatic second hit at DIS3L2 in nephrogenic rest (2-hit)
                         │  [PMID 35700413]
                         ▼
                   WILMS TUMOR (~64% of neonatal survivors)
```

The central interpretive insight is that Perlman syndrome is a **cytoplasmic RNA quality-control disease**. The historical emphasis on let-7 (because DIS3L2 is the pathway's terminal nuclease) is mechanistically incomplete: steady-state mature let-7 is unchanged on DIS3L2 loss [PMID: 29950491], so the tumor-suppressive and overgrowth phenotypes derive from the **broader surveillance failure** — accumulation of aberrant structured ncRNAs and consequent PI3K/AKT-driven overproliferation. This reframes DIS3L2 as a general guardian of the cytoplasmic transcriptome whose loss produces growth dysregulation and cancer predisposition.

---

## Evidence Base

| PMID | Role in this report | Evidence type |
|---|---|---|
| [PMID: 22306653](https://pubmed.ncbi.nlm.nih.gov/22306653/) | Gene discovery; DIS3L2 tumor suppressor; sporadic WT mutations | Human genetics + in vitro |
| [PMID: 23613427](https://pubmed.ncbi.nlm.nih.gov/23613427/) | Locus, inheritance, enzyme identity | Review |
| [PMID: 23486540](https://pubmed.ncbi.nlm.nih.gov/23486540/) | Exon-9 deletion via LINE-1 NAHR; diagnostic pitfall | Case/molecular |
| [PMID: 24141620](https://pubmed.ncbi.nlm.nih.gov/24141620/) | DIS3L2 = terminal nuclease of LIN28-TUT4/7 pathway | In vitro/mechanistic |
| [PMID: 25119025](https://pubmed.ncbi.nlm.nih.gov/25119025/) | Crystal structure; oligoU recognition | Structural |
| [PMID: 23594738](https://pubmed.ncbi.nlm.nih.gov/23594738/) | Dis3l2 degrades uridylated pre-let-7 (mESC) | Model organism |
| [PMID: 27498873](https://pubmed.ncbi.nlm.nih.gov/27498873/) | DMD as ncRNA quality-control pathway | Mechanistic |
| [PMID: 27647875](https://pubmed.ncbi.nlm.nih.gov/27647875/) | DIS3L2-dependent uridylome of structured ncRNAs | Human in vitro |
| [PMID: 32457326](https://pubmed.ncbi.nlm.nih.gov/32457326/) | 7SL/SRP, ER translation, Ca²⁺ homeostasis | In vitro/mechanistic |
| [PMID: 29950491](https://pubmed.ncbi.nlm.nih.gov/29950491/) | Mature let-7 unchanged → let-7-independent | In vitro/model |
| [PMID: 33370287](https://pubmed.ncbi.nlm.nih.gov/33370287/) | PI3K/AKT-driven proliferation; conserved fly↔human | Model organism + human cells |
| [PMID: 40500755](https://pubmed.ncbi.nlm.nih.gov/40500755/) | Akt-GSK3β, neural crest apoptosis | Model organism (zebrafish) |
| [PMID: 18780370](https://pubmed.ncbi.nlm.nih.gov/18780370/) | Prognosis: 64% WT, developmental delay; BWS/SGBS exclusion | Human review/case series |
| [PMID: 40704758](https://pubmed.ncbi.nlm.nih.gov/40704758/) | High neonatal mortality; attenuated sibling cases | Human case report |
| [PMID: 42040973](https://pubmed.ncbi.nlm.nih.gov/42040973/) | Genotype-survival correlation; prolonged survival | Human case report |
| [PMID: 35700413](https://pubmed.ncbi.nlm.nih.gov/35700413/) | Two-hit Wilms tumor causation | Human case report |
| [PMID: 34964966](https://pubmed.ncbi.nlm.nih.gov/34964966/) | Compound het variants; ACMG classification | Human case/molecular |
| [PMID: 39466169](https://pubmed.ncbi.nlm.nih.gov/39466169/) | AACR WT surveillance guidelines | Guideline |
| [PMID: 39320341](https://pubmed.ncbi.nlm.nih.gov/39320341/) | AACR WT/hepatoblastoma surveillance update | Guideline |
| [PMID: 34134020](https://pubmed.ncbi.nlm.nih.gov/34134020/) | SIOP-Europe WT surveillance guidelines | Guideline |
| [PMID: 42535789](https://pubmed.ncbi.nlm.nih.gov/42535789/) | Nephrogenic rests and relapse risk | Human cohort |
| [PMID: 24215131](https://pubmed.ncbi.nlm.nih.gov/24215131/) | BWS/Perlman clinical overlap | Human case |
| [PMID: 38161545](https://pubmed.ncbi.nlm.nih.gov/38161545/) | DIS3L2 deletion; prenatal diagnosis; differentials | Human case |
| [PMID: 20726997](https://pubmed.ncbi.nlm.nih.gov/20726997/) | Cholestasis as novel feature | Human case |
| [PMID: 34503817](https://pubmed.ncbi.nlm.nih.gov/34503817/) | Pediatric cancer predisposition syndrome management | Review |

---

## Limitations and Knowledge Gaps

1. **Extreme rarity:** Fewer than ~40 molecularly/clinically characterized patients exist worldwide; prevalence, incidence, carrier frequency, and sex ratio are not reliably quantified. All clinical data come from small case series and reports, not EHR or registry cohorts.
2. **Prognosis estimates are small-sample:** The frequently cited "64% Wilms tumor" figure derives from a single review of neonatal survivors (small denominator) and may be subject to ascertainment bias [PMID: 18780370].
3. **Genotype–phenotype correlation is inferential:** The link between residual exoribonuclease activity and survival rests on a handful of case reports, not a systematic functional-genomic series [PMID: 42040973].
4. **Mechanistic gaps:** Although PI3K/AKT activation and let-7-independence are established, the exact molecular bridge from accumulated structured ncRNAs to PI3K/AKT activation is not fully resolved, and no model fully recapitulates the complete human syndrome.
5. **No disease-specific therapy or clinical trials:** Management is entirely supportive/oncologic; no targeted, gene, cell, or RNA therapies exist or are in trials.
6. **Epigenetics/omics:** No disease-specific methylation signature, proteomic, or metabolomic profile has been reported for patient tissue.

---

## Proposed Follow-up Experiments / Actions

1. **Functional allele series:** Systematically express patient *DIS3L2* variants (nonsense, frameshift, missense, exon-9 deletion) and quantify residual exoribonuclease activity to formalize the genotype–severity correlation [extends PMID: 42040973].
2. **Conditional kidney mouse model:** Generate a renal-progenitor-specific *Dis3l2* knockout to test whether it recapitulates nephroblastomatosis/Wilms tumor and to map the two-hit timeline [extends PMID: 22306653; PMID: 35700413].
3. **Bridge the ncRNA→PI3K/AKT gap:** Use CLIP + phosphoproteomics in DIS3L2-null kidney cells to identify which accumulated uridylated substrate(s) drive PI3K/AKT activation [extends PMID: 27647875; PMID: 33370287].
4. **Therapeutic proof-of-concept:** Test PI3K/AKT pathway inhibitors in DIS3L2-deficient models for anti-proliferative effect, as a rationale for future precision intervention [extends PMID: 33370287].
5. **Registry and surveillance audit:** Establish an international Perlman syndrome registry to refine prevalence, survival, and the yield/interval of renal ultrasound surveillance [extends PMID: 39466169; PMID: 34134020].
6. **Diagnostic standardization:** Formalize a testing algorithm mandating copy-number analysis (MLPA/exon-CMA) alongside WES to avoid missing exon-9 deletions [extends PMID: 23486540].

---

*Report compiled from 9 confirmed findings and 33 reviewed papers across 5 investigation iterations. Evidence types span human clinical/genetic, model organism (Drosophila, zebrafish, mouse), in vitro, and structural studies.*


## Artifacts

- [OpenScientist final report](Perlman_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Perlman_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 27 |
| On topic | 23 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 18 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 11 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001561` (1 mention) - the report calls it "Very frequent"; HP calls it **Polyhydramnios**
- `HP:0001791` (1 mention) - the report calls it "Frequent"; HP calls it **Fetal ascites**
- `HP:0000105` (1 mention) - the report calls it "Very frequent"; HP calls it **Enlarged kidney**
- `HP:0000110` (1 mention) - the report calls it "Frequent"; HP calls it **Renal dysplasia**
- `HP:0001708` (1 mention) - the report calls it "Characteristic precursor"; HP calls it **Right ventricular failure**
- `HP:0002667` (1 mention) - the report calls it "~64% of neonatal survivors"; HP calls it **Nephroblastoma**
- `HP:0001999` (1 mention) - the report calls it "Characteristic"; HP calls it **Abnormal facial shape**
- `HP:0003271` (1 mention) - the report calls it "Frequent"; HP calls it **Visceromegaly**
- `HP:0001396` (1 mention) - the report calls it "Rare (reported)"; HP calls it **Cholestasis**
- `GO:0006401` (1 mention) - the report calls it "Cellular processes:** RNA catabolism/surveillance"; GO calls it **RNA catabolic process**
- `GO:0005737` (1 mention) - the report calls it "Subcellular compartments:** Cytoplasm"; GO calls it **cytoplasm**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0043491` (2 mentions) - the report calls it "Molecular pathways:** PI3K/AKT", "PI3K/AKT"; GO calls it **phosphatidylinositol 3-kinase/protein kinase B signal transduction**, and lists "PI3K-PKB/Akt pathway" among its other names
- `GO:0000175` (1 mention) - the report calls it "3′-5′ exoribonuclease activity"; GO calls it **3'-5'-RNA exonuclease activity**, and lists "3'-5' exoribonuclease activity" among its other names
- `GO:0071028` (1 mention) - the report calls it "nuclear mRNA surveillance — analogous cytoplasmic QC"; GO calls it **nuclear mRNA surveillance**
- `UBERON:0002113` (2 mentions) - the report calls it "Kidney", "Primary organ:** **Kidney", "kidney"; UBERON calls it **kidney**, and lists "reniculate kidney" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0043491` - called "Molecular pathways:** PI3K/AKT", "PI3K/AKT"
- `UBERON:0002113` - called "Kidney", "Primary organ:** **Kidney", "kidney"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.