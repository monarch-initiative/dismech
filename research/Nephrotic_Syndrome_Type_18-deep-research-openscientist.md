---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-04T19:45:36.658254'
end_time: '2026-11-04T20:02:27.181542'
duration_seconds: 1010.52
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Nephrotic Syndrome Type 18
  mondo_id: MONDO:0032581
  category: Mendelian
  causal_genes: NUP133
  omim_id: OMIM:618177
  synonyms: NPHS18; NUP133-related steroid-resistant nephrotic syndrome
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 22
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 22
  on_topic: 13
  validator_version: 0.5.1
term_validation:
  total_terms: 34
  verified: 33
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 2
  labels_mismatched: 14
  mislabelled_terms:
  - term_id: MONDO:0032581
    reported_labels:
    - MONDO
    ontology_label: nephrotic syndrome, type 18
  - term_id: HP:0000100
    reported_labels:
    - Clinical/lab
    ontology_label: Nephrotic syndrome
  - term_id: HP:0003073
    reported_labels:
    - Lab
    ontology_label: Hypoalbuminemia
  - term_id: HP:0000969
    reported_labels:
    - Clinical sign
    ontology_label: Edema
  - term_id: HP:0003077
    reported_labels:
    - Lab
    ontology_label: Hyperlipidemia
  - term_id: HP:0000097
    reported_labels:
    - Pathology
    ontology_label: Focal segmental glomerulosclerosis
  - term_id: HP:0000252
    reported_labels:
    - Physical
    ontology_label: Microcephaly
  - term_id: HP:0012444
    reported_labels:
    - Imaging/structural
    ontology_label: Brain atrophy
  - term_id: HP:0001252
    reported_labels:
    - Neuro
    ontology_label: Hypotonia
  - term_id: HP:0004936
    reported_labels:
    - Clinical
    ontology_label: Venous thrombosis
  - term_id: HP:0002719
    reported_labels:
    - Clinical
    ontology_label: Recurrent infections
  - term_id: UBERON:0002113
    reported_labels:
    - "Organ level \u2014 primary:** Kidney"
    ontology_label: kidney
  - term_id: UBERON:0000955
    reported_labels:
    - brain / cerebral cortex
    ontology_label: brain
  - term_id: NCBITaxon:7955
    reported_labels:
    - nup133
    ontology_label: Danio rerio
  labels_variant: 6
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Nephrotic_Syndrome_Type_18-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Nephrotic_Syndrome_Type_18-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Nephrotic Syndrome Type 18
- **MONDO ID:** MONDO:0032581 (if available)
- **Causal gene(s):** NUP133
- **OMIM:** OMIM:618177
- **Synonyms:** NPHS18; NUP133-related steroid-resistant nephrotic syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Nephrotic Syndrome Type 18** covering all of the
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

# Nephrotic Syndrome Type 18 (NPHS18 / NUP133-related Steroid-Resistant Nephrotic Syndrome): A Comprehensive Disease Characteristics Report

**Disease:** Nephrotic Syndrome Type 18 (NPHS18)
**Causal gene:** **NUP133** (Nucleoporin 133 kDa; HGNC:29915; NCBI Gene 55746; UniProt Q8WUM0)
**OMIM:** 618177 · **MONDO:** MONDO:0032581 · **Category:** Mendelian, autosomal recessive

---

## Summary

**Nephrotic Syndrome Type 18 (NPHS18) is a rare autosomal-recessive, steroid-resistant nephrotic syndrome (SRNS) caused by biallelic (homozygous or compound-heterozygous) hypomorphic variants in *NUP133***, the gene encoding nucleoporin 133 kDa — a scaffold component of the outer-ring Nup84/Y-complex of the nuclear pore complex (NPC). The disease was defined when Braun et al. (2018) identified recessive mutations in four outer-ring nucleoporin genes — *NUP107*, *NUP85*, *NUP133*, and *NUP160* — across 13 families with SRNS ([PMID: 30179222](https://pubmed.ncbi.nlm.nih.gov/30179222/)). Despite NUP133 being a ubiquitously expressed, essential housekeeping protein, its disease manifestations are strikingly tissue-restricted, predominantly affecting the kidney's glomerular podocytes and, in syndromic forms, the developing brain.

The core mechanistic insight is that loss of NUP133 function activates **CDC42**, a Rho-family GTPase and a key effector of SRNS pathogenesis, in podocytes. This leads to foot-process effacement, focal segmental glomerulosclerosis (FSGS) — seen in ~89% of nucleoporin-SRNS biopsies — and progression to kidney failure at a median age of ~13 years for NUP133. The phenotype spans a continuum from **kidney-limited SRNS** (Braun 2018) to syndromic **Galloway-Mowat syndrome (GAMOS)** featuring microcephaly, brain malformation, and early-onset nephrotic syndrome (Fujita 2018, [PMID: 30427554](https://pubmed.ncbi.nlm.nih.gov/30427554/)). Why a ubiquitous scaffold nucleoporin causes selective podocyte and neuronal disease is explained by cell-type-specific differentiation dependence: Nup133 is dispensable for pluripotency but required for neuroectodermal/neuronal differentiation and for maintaining the highly specialized, non-regenerating podocyte.

Clinically, NUP133-SRNS is **resistant to immunosuppression** (steroids, calcineurin inhibitors, mycophenolate, rituximab). Management is therefore supportive and nephroprotective (RAAS blockade, diuretics, statins, thromboprophylaxis), with **kidney transplantation** as definitive therapy for kidney failure — favored because podocyte-intrinsic genetic SRNS has low post-transplant recurrence. The single greatest genotype-guided benefit of early genetic diagnosis is avoiding prolonged, toxic, ineffective immunosuppression. This report synthesizes 12 confirmed findings across 43 reviewed papers into a complete disease knowledge base entry.

---

## 1. Disease Information

**Overview.** NPHS18 is a monogenic (Mendelian) form of steroid-resistant nephrotic syndrome. Nephrotic syndrome is clinically defined by nephrotic-range proteinuria (>3.5 g/day in adults; >40 mg/m²/h in children), hypoalbuminemia (<2.5–3 g/dL), peripheral edema, and hyperlipidemia. In NPHS18 the glomerular lesion is characteristically **focal segmental glomerulosclerosis (FSGS)** with podocyte foot-process effacement on electron microscopy. The disease belongs to the broader class of **nucleoporin-associated SRNS ("nucleoporopathies")**, caused by mutations in genes encoding the NPC. *NUP133* sits on the same disease axis as its physical binding partner *NUP107* and the other outer-ring nucleoporin genes (*NUP107*, *NUP85*, *NUP160*) and inner-ring genes (*NUP93*, *NUP205*).

*(This disease serial number refers specifically to NUP133 — not to be confused with other NPHS numbers mapping to NPHS1/NPHS2/PLCE1, etc.)*

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | 618177 |
| MONDO | MONDO:0032581 |
| Gene (HGNC) | NUP133 / HGNC:29915 |
| NCBI Gene | 55746 |
| UniProt | Q8WUM0 |
| Ensembl | ENSG00000069248 (chr1q42.12) |
| Reference transcript | NM_018230.3 (protein 1156 aa) |

**Synonyms / alternative names:** NPHS18; NUP133-related steroid-resistant nephrotic syndrome; NUP133-related nucleoporopathy; (syndromic form) Galloway-Mowat syndrome due to NUP133.

**Information source.** Disease-level characterization derives from aggregated resources (OMIM, Orphanet, ClinVar, gnomAD, UniProt) and from primary case reports/series of individual patients (Braun 2018; Fujita 2018; reviews such as Yao 2025, [PMID: 39331077](https://pubmed.ncbi.nlm.nih.gov/39331077/)). It is a rare disease known from a modest number of families worldwide; no large EHR-based registry specific to NUP133 exists.

---

## 2. Etiology

**Primary cause — genetic.** NPHS18 is caused exclusively by **biallelic loss-of-function/hypomorphic variants in *NUP133***. Inheritance is autosomal recessive; both alleles must be affected. Reported disease alleles include splice-site, missense, and frameshift variants (Section 4). There is no environmental or infectious cause; the nephrotic syndrome is a direct consequence of the podocyte-intrinsic genetic defect.

**Genetic risk factors.** The sole risk factor is carriage of two pathogenic *NUP133* alleles. **Consanguinity** substantially enriches recessive SRNS, as biallelic (often homozygous) variants are more likely in offspring of related parents (Azouaou 2026 Algerian consanguineous cohort, [PMID: 41612037](https://pubmed.ncbi.nlm.nih.gov/41612037/); Soliman 2025, [PMID: 40402239](https://pubmed.ncbi.nlm.nih.gov/40402239/)). Modifier genes within the Y-complex (e.g., *NUP107*) are plausible contributors to expressivity because NUP133 function depends on NUP107 binding, but specific modifier alleles are not established.

**Environmental risk / protective factors.** None identified. Because this is a Mendelian podocytopathy, classical environmental risk factors (toxins, lifestyle, infections) and protective factors (diet, exposures) are **not applicable** to disease causation. Supportive measures (sodium restriction, nephroprotection) modify disease *course*, not disease *occurrence*.

**Gene–environment interactions.** No specific GxE interactions are documented. Disease penetrance in biallelic carriers appears high; environmental modulation of severity has not been demonstrated.

---

## 3. Phenotypes

NPHS18 presents a spectrum from isolated (kidney-limited) SRNS to syndromic GAMOS. Core and extrarenal phenotypes with suggested HPO terms:

| Phenotype | Type | HPO term | Onset / severity / frequency |
|---|---|---|---|
| Nephrotic syndrome | Clinical/lab | HP:0000100 | Childhood (median ~9 y); severe; near-universal |
| Proteinuria (nephrotic-range) | Lab | HP:0000090 / HP:0003076 | Childhood; progressive; universal |
| Hypoalbuminemia | Lab | HP:0003073 | Concurrent with onset; frequent |
| Edema | Clinical sign | HP:0000969 | Presenting feature; frequent |
| Hyperlipidemia | Lab | HP:0003077 | Concurrent; frequent |
| Focal segmental glomerulosclerosis | Pathology | HP:0000097 | ~89% of nucleoporin-SRNS biopsies |
| Podocyte foot-process effacement | Pathology (EM) | — | Characteristic; near-universal |
| Stage 5 CKD / kidney failure | Clinical | HP:0003774 / HP:0000083 | Median ~13 y (NUP133); progressive |
| Microcephaly (GAMOS) | Physical | HP:0000252 | Congenital; syndromic subset |
| Brain atrophy/anomalies (GAMOS) | Imaging/structural | HP:0012444 | Syndromic subset |
| Developmental delay / intellectual disability | Behavioral/neuro | HP:0001263 / HP:0001249 | Syndromic subset |
| Hypotonia | Neuro | HP:0001252 | Syndromic subset |
| Venous thrombosis (NS complication) | Clinical | HP:0004936 | Secondary complication |
| Increased infection susceptibility | Clinical | HP:0002719 | Secondary complication |

**Characteristics.** Onset is typically **childhood** (median ~9 years for NUP133; Yao 2025, [PMID: 39331077](https://pubmed.ncbi.nlm.nih.gov/39331077/)). The course is **steroid-resistant and progressive**, advancing to kidney failure. Extrarenal manifestations of nucleoporin-SRNS include "neurological disorders, growth and development disorders, cardiovascular disorders, and congenital malformations" (Yao 2025). In the syndromic (GAMOS) form, Fujita et al. documented microcephaly, brain anomalies including focal cortical dysplasia type IIa on autopsy, and early-onset nephrotic syndrome with FSGS ([PMID: 30427554](https://pubmed.ncbi.nlm.nih.gov/30427554/)).

**Quality-of-life impact.** Progression to dialysis/transplantation and (in GAMOS) neurodevelopmental impairment substantially reduce quality of life. Disease-specific QoL instruments have not been applied to this rare disorder; impact is inferred from the severity of pediatric kidney failure and neurodisability. Secondary complications (thrombosis, infection) from the hypercoagulable, immunocompromised nephrotic state add further morbidity (Ponticelli 2023, [PMID: 37466816](https://pubmed.ncbi.nlm.nih.gov/37466816/)).

---

## 4. Genetic / Molecular Information

**Causal gene.** *NUP133* (HGNC:29915; disease OMIM 618177), chr1q42.12, ENSG00000069248; reference transcript NM_018230.3 encoding a 1156-amino-acid protein (UniProt Q8WUM0).

**Pathogenic variants.** Disease-causing alleles are rare and biallelic. Key reported variants:

| Variant (NM_018230.3) | Type | Phenotype | Functional effect | Source |
|---|---|---|---|---|
| c.3335-11T>A (9-bp intronic insertion, exons 25–26) | Splice-site | GAMOS (syndromic) | Impairs NUP133–NUP107 interaction | Fujita 2018 [PMID: 30427554](https://pubmed.ncbi.nlm.nih.gov/30427554/) |
| Compound-het / homozygous missense & splice alleles | Missense/splice | SRNS (kidney-limited) | Weaken neighboring NPC-subunit interactions | Braun 2018 [PMID: 30179222](https://pubmed.ncbi.nlm.nih.gov/30179222/) |
| p.Lys966Asn | Missense | SRNS | Structurally modeled | Wang 2023 [PMID: 37041680](https://pubmed.ncbi.nlm.nih.gov/37041680/) |
| c.1393dup (p.Ser465fs) | Frameshift | (ClinVar likely-pathogenic) | Loss of function | ClinVar |

**Variant classification landscape.** ClinVar (queried Nov 2026) held 477 *NUP133* records but only **1 gene-specific likely-pathogenic small variant** (c.1393dup / p.Ser465fs), alongside 117 VUS and 39 (likely-)benign entries; the "Pathogenic" entries are large 1q copy-number gains spanning many genes rather than NUP133-specific. Consequently, most validated disease alleles reside in the **primary literature**, not ClinVar. This VUS-dominated landscape underscores the interpretive challenge in SRNS genetics (see Interpretative Challenges case, [PMID: 42422724](https://pubmed.ncbi.nlm.nih.gov/42422724/)).

**Allele frequency / population constraint.** gnomAD v2.1.1 constraint for NUP133: **pLI = 0.00017** (not haploinsufficient), observed/expected LoF = 66/146.2 ≈ **0.45** (LOEUF ≈ 0.554), lof_z = 5.63, missense Z = 1.12. The low pLI indicates heterozygous loss-of-function is tolerated in the general population — consistent with recessive inheritance and healthy carriers — while the moderate oe_lof (~0.45) indicates partial depletion of biallelic LoF. This constraint profile is the molecular-genetic signature of an autosomal-recessive, carrier-tolerated disease gene.

**Somatic vs germline.** All disease variants are **germline**. No somatic involvement.

**Functional consequences.** Variants are **loss-of-function / hypomorphic**, destabilizing the Y-complex and weakening NUP133–NUP107 binding; no gain-of-function or dominant-negative mechanism is implicated.

**Modifier genes.** Not formally established; Y-complex paralogs (*NUP107*, *NUP85*, *NUP160*) are mechanistically related genes causing overlapping SRNS.

**Epigenetic / chromosomal abnormalities.** No disease-specific epigenetic mechanism is described. Large 1q copy-number gains encompassing NUP133 exist in ClinVar but are not the recessive point-mutation mechanism of NPHS18.

---

## 5. Environmental Information

**Not applicable as a cause.** NPHS18 is a purely genetic Mendelian disorder. No environmental toxins, radiation, pollution, occupational exposures, lifestyle factors, or infectious agents cause or trigger the disease. Environmental factors are relevant only to the general management of nephrotic syndrome (e.g., sodium intake affecting edema) and to secondary complications (e.g., infection risk in the immunocompromised nephrotic state), not to disease etiology.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic hypomorphic *NUP133* variants** (splice/missense/frameshift) → **reduce functional NUP133 protein** and weaken its binding to the neighboring nucleoporin **NUP107** (demonstrated by co-IP; Braun 2018, Fujita 2018).
2. Impaired NUP133–NUP107 interaction → **destabilizes the Nup84/Y-complex of the NPC outer ring** → **defective nuclear pore complex assembly** (demonstrated in vitro; Rogg 2022, [PMID: 35455939](https://pubmed.ncbi.nlm.nih.gov/35455939/)).
3. Defective NPC assembly → **perturbed nucleocytoplasmic transport and altered transcriptome composition**; NUP133 also participates in YAP/TAZ nuclear-import complexes (Ester 2023, [PMID: 37565816](https://pubmed.ncbi.nlm.nih.gov/37565816/)) → altered nuclear signaling (partly inferred).
4. In podocytes specifically → **activation of CDC42** (Rho-family GTPase; a "key effector of SRNS pathogenesis") and **cytoskeletal dysregulation** (demonstrated by CRISPR/Cas9 KO in human podocytes; Braun 2018).
5. CDC42 activation + actin-cytoskeleton disruption → **podocyte injury and foot-process effacement** → breakdown of the glomerular filtration barrier → **nephrotic-range proteinuria** (demonstrated in zebrafish/Xenopus models; Braun 2018, Cianciolo Cosentino 2019 [PMID: 30894603](https://pubmed.ncbi.nlm.nih.gov/30894603/)).
6. Sustained podocyte loss (podocytes cannot regenerate) → **focal segmental glomerulosclerosis (FSGS)** → progressive nephron loss → **kidney failure (median ~13 y)**.

**Branch (neural, GAMOS):** Steps 2–3 in neural progenitors → impaired neuroectodermal/neuronal differentiation and loss of nuclear-envelope integrity (Orniacki 2023 [PMID: 37305998](https://pubmed.ncbi.nlm.nih.gov/37305998/); Taniguchi 2025 [PMID: 40205196](https://pubmed.ncbi.nlm.nih.gov/40205196/)) → **microcephaly, cortical malformation, developmental delay**.

```
NUP133 biallelic hypomorphic variants
        │
        ▼
Weakened NUP133–NUP107 binding ──► Destabilized Y-complex / defective NPC assembly
        │                                      │
        ▼                                      ▼
Perturbed nucleocytoplasmic transport,   (neural progenitors)
altered transcriptome, YAP/TAZ import    impaired neuronal differentiation
        │                                      │
        ▼ (podocyte)                           ▼
CDC42 activation + cytoskeletal           Microcephaly, cortical dysplasia,
dysregulation                             developmental delay  (GAMOS branch)
        │
        ▼
Foot-process effacement → proteinuria → FSGS → kidney failure
```

### Detail by category

- **Molecular pathways:** CDC42/Rho-GTPase signaling (central, downstream podocyte effector); Hippo–YAP/TAZ nuclear import (NUP133 is a component of YAP/TAZ complexes; NUP205 required for their nuclear import — Ester 2023). Upstream: nucleocytoplasmic transport / mRNA export machinery.
- **Cellular processes:** NPC assembly (GO:0051292), mRNA export from nucleus (GO:0006406), protein import into nucleus (GO:0006606), regulation of Rho-GTPase activity, cytoskeleton organization, podocyte foot-process maintenance; in GAMOS, neuronal differentiation and nuclear-envelope integrity.
- **Protein dysfunction:** Loss-of-function/hypomorphic — destabilized scaffold, weakened Y-complex contacts; not aggregation or GoF.
- **Immune involvement:** None primary (disease is immunosuppression-resistant, arguing against an immune-mediated podocytopathy). Secondary infection susceptibility arises from urinary immunoglobulin loss.
- **Tissue damage mechanism:** Podocyte injury → glomerulosclerosis/fibrosis; podocytes are terminally differentiated and non-regenerating, so loss is irreversible.
- **Molecular profiling:** In vitro human podocyte models show NUP133 controls NPC assembly, transcriptome composition, and cytoskeleton regulation (Rogg 2022). Single-cell/proteomic work on the related NUP160 KO mouse confirms Cdc42 dysregulation in podocytes (Qiao 2025, [PMID: 40298220](https://pubmed.ncbi.nlm.nih.gov/40298220/)).

**Upstream vs downstream:** The NPC-scaffold/Y-complex defect is **upstream**; CDC42 activation, cytoskeletal collapse, foot-process effacement, and FSGS are **downstream**. Cell types: podocyte (CL:0000653, glomerular visceral epithelial cell), neurons/neural progenitors. Key GO biological processes: GO:0006406 (mRNA export), GO:0051292 (NPC assembly), GO:0001822 (kidney development), GO:0072006 (nephron development).

---

## 7. Anatomical Structures Affected

- **Organ level — primary:** Kidney (UBERON:0002113), specifically the renal glomerulus (UBERON:0000074). Secondary involvement: whole urinary system; systemic effects of nephrotic syndrome. In GAMOS, the **brain / cerebral cortex** (UBERON:0000955) is primarily affected.
- **Body systems:** Renal/urinary (primary); nervous system (syndromic GAMOS); cardiovascular and hematologic (secondary — thrombosis, hyperlipidemia); immune (secondary infection risk).
- **Tissue/cell level:** Glomerular visceral epithelial cells — **podocytes (CL:0000653)** — are the central target; the glomerular basement membrane (UBERON:0002196) is secondarily disrupted. Neurons/neural progenitors in GAMOS.
- **Subcellular level:** **Nuclear pore complex (GO:0005643)** and **nuclear pore outer ring (GO:0031080)**; nuclear envelope; nucleus. NUP133 also localizes to kinetochore/centromere during mitosis.
- **Localization / lateralization:** Bilateral, diffuse glomerular involvement; microcephaly is symmetric/global.

---

## 8. Temporal Development

- **Onset:** Childhood; median age at onset ~9 years for NUP133-associated SRNS (Yao 2025, [PMID: 39331077](https://pubmed.ncbi.nlm.nih.gov/39331077/)). GAMOS forms present earlier (congenital microcephaly with early-onset nephrotic syndrome). Onset pattern is insidious/subacute with progressive proteinuria.
- **Progression:** Chronic and progressive. FSGS → declining GFR → **Stage 5 CKD/kidney failure at median ~13 years** for NUP133 (contrast: NUP93 ~3.7 y, NUP107 ~6.9 y). Progression rate is comparatively slower among nucleoporins for NUP133.
- **Disease course pattern:** Progressive (not relapsing-remitting); steroid-resistant, so no treatment-induced remission is expected. Duration: chronic/lifelong.
- **Patterns / critical periods:** No spontaneous remission. The key intervention window is **early genetic diagnosis** to redirect care away from ineffective immunosuppression and toward nephroprotection and transplant planning.

| Nucleoporin gene | Median onset (y) | Median age at kidney failure (y) |
|---|---|---|
| NUP85 | 7 | 8.5 |
| NUP93 | 3 | 3.7 |
| NUP107 | 4.1 | 6.9 |
| **NUP133** | **9** | **13** |
| NUP160 | 7 | 15 |
| NUP205 | 2 | 7 |

*(Yao 2025, [PMID: 39331077](https://pubmed.ncbi.nlm.nih.gov/39331077/))*

---

## 9. Inheritance and Population

- **Inheritance pattern:** **Autosomal recessive.** Biallelic (homozygous or compound-heterozygous) variants required. Supported by gnomAD constraint (pLI ≈ 0; carriers healthy).
- **Penetrance / expressivity:** Penetrance in biallelic carriers appears high; expressivity is **variable**, spanning kidney-limited SRNS to syndromic GAMOS even for overlapping gene defects.
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not reported.
- **Consanguinity / founder effects:** Consanguinity strongly enriches recessive SRNS; NUP133 disease is frequently homozygous in consanguineous families (Fujita 2018; Azouaou 2026 [PMID: 41612037](https://pubmed.ncbi.nlm.nih.gov/41612037/)). No specific founder allele is established.
- **Carrier frequency:** Not precisely defined; heterozygous LoF alleles are tolerated and present at low frequency in gnomAD.
- **Epidemiology:** No precise prevalence/incidence figures exist for NPHS18 specifically — it is an ultra-rare subset of monogenic SRNS. Context: ~30% of pediatric SRNS is monogenic (Nagano 2022, [PMID: 36176665](https://pubmed.ncbi.nlm.nih.gov/36176665/)), rising to 56.1% with WGS in early-onset consanguineous cohorts (Soliman 2025, [PMID: 40402239](https://pubmed.ncbi.nlm.nih.gov/40402239/)). NUP133 is one of several nucleoporin genes within this monogenic fraction.
- **Population demographics:** Reported across diverse populations; enriched in consanguineous populations (e.g., Middle Eastern, North African, South/Southeast Asian cohorts). No strong sex bias is expected for a recessive glomerular disorder. Age distribution: predominantly pediatric onset.

---

## 10. Diagnostics

- **Clinical/laboratory:** Nephrotic-range proteinuria (urine protein:creatinine, 24-h protein), serum albumin (hypoalbuminemia), serum lipids (hyperlipidemia). Clinical diagnosis of nephrotic syndrome = proteinuria + hypoalbuminemia + edema + hyperlipidemia.
- **Biopsy / pathology:** Kidney biopsy typically shows **FSGS** (light microscopy) with **diffuse foot-process effacement** on electron microscopy — present in ~89% of nucleoporin-SRNS biopsies (Yao 2025). Related nucleoporin studies show ultrastructural podocyte vacuolization, GBM changes, and ER dilation (Chen 2025, [PMID: 39814977](https://pubmed.ncbi.nlm.nih.gov/39814977/)).
- **Genetic testing (definitive):** Molecular confirmation is essential. Recommended approach:
  - **Targeted NGS gene panels** (SRNS/nephrotic-syndrome panels including NUP133 and paralogs) — most cost-effective, recommended first-line (Cheng 2024, [PMID: 38654395](https://pubmed.ncbi.nlm.nih.gov/38654395/); Yao 2025).
  - **Whole-exome sequencing (WES)** — adds ~8.7% yield over panels.
  - **Whole-genome sequencing (WGS)** — adds ~4.3% over WES; highest overall yield (56.1% in early-onset consanguineous cohorts).
  - Single-gene testing and cDNA/minigene splice assays confirm candidate variants (e.g., c.3335-11T>A splice effect).
  - CMA/karyotype/FISH/mtDNA/repeat-expansion testing: **not applicable** (point/splice recessive variants, not structural/mitochondrial/repeat disease).
- **Clinical criteria / differential diagnosis:** Differentiate from other monogenic SRNS/podocytopathies (NPHS1, NPHS2, PLCE1, WT1/Denys-Drash, LAMB2, TRPC6, COQ6, WDR73) and from immune-mediated primary FSGS/minimal change disease (which are steroid- or rituximab-responsive). GAMOS differential includes other KEOPS-complex (OSGEP/TP53RK/TPRKB/LAGE3/GON7) and WDR73/WDR4/PRDM15 genes (Zhang 2025, [PMID: 40533795](https://pubmed.ncbi.nlm.nih.gov/40533795/)).
- **Screening:** Cascade genetic testing of at-risk relatives; carrier testing in consanguineous families. No population newborn screening exists for this ultra-rare disorder.

---

## 11. Outcome / Prognosis

- **Renal prognosis:** Poor without transplant. Progressive FSGS → **kidney failure at median ~13 years** for NUP133 (Yao 2025). Immunosuppression does not alter the natural history.
- **Survival/mortality:** No disease-specific survival statistics for NPHS18 alone; prognosis is governed by progression to kidney failure (manageable by dialysis/transplant) and, in GAMOS, by neurological severity. GAMOS carries higher early mortality due to brain involvement.
- **Morbidity/QoL:** Pediatric kidney failure, dialysis dependence, transplant, and (in syndromic cases) neurodevelopmental disability. Secondary complications: venous/arterial thrombosis, infection, cardiovascular risk (Ponticelli 2023, [PMID: 37466816](https://pubmed.ncbi.nlm.nih.gov/37466816/)).
- **Post-transplant outcome:** Favorable relative to immune-mediated FSGS — genetic (podocyte-intrinsic) SRNS has **low recurrence** after transplantation (~12.5% for nucleoporin-SRNS, reported only for NUP93; Yao 2025), because the defect is not a circulating permeability factor.
- **Prognostic factors:** Genotype (which nucleoporin; NUP133 has comparatively later kidney failure), age at onset, presence of syndromic/neurological features, and degree of FSGS/fibrosis at biopsy.

---

## 12. Treatment

**Core principle: NUP133-SRNS is immunosuppression-resistant.** "Most affected individuals are resistant to immunosuppressants" (Yao 2025, [PMID: 39331077](https://pubmed.ncbi.nlm.nih.gov/39331077/)). Therapy is supportive/nephroprotective and, ultimately, kidney replacement.

| Treatment | Class / NCIT | Rationale |
|---|---|---|
| ACE inhibitors / ARBs | RAAS blockade (NCIT C734 ACE inhibitor; Angiotensin Receptor Antagonist) | Antiproteinuric, nephroprotective |
| Loop diuretics + sodium restriction | Diuretic | Manage edema |
| Statins | HMG-CoA reductase inhibitor | Manage hyperlipidemia |
| Anticoagulation / thromboprophylaxis | Anticoagulant | Counter nephrotic hypercoagulability (urinary anticoagulant loss) |
| Vaccination / infection prevention | — | Counter urinary immunoglobulin loss |
| **Kidney transplantation** | NCIT C15366 | Definitive therapy for kidney failure; low recurrence |

- **Immunosuppression (steroids, CNIs, MMF, rituximab):** Generally **ineffective** in monogenic nucleoporin-SRNS; prolonged ineffective immunosuppression causes net harm (toxicity: e.g., CNI-induced pancreatitis, infections — see [PMID: 42422724](https://pubmed.ncbi.nlm.nih.gov/42422724/)). Avoiding this is the main genotype-guided benefit of early diagnosis (Berke 2026, [PMID: 42707999](https://pubmed.ncbi.nlm.nih.gov/42707999/)).
- **Advanced therapeutics (gene/RNA/cell therapy):** None approved or in trials for NUP133. Experimental mechanistic interest centers on the **CDC42 axis** downstream of NUP133 (Braun 2018).
- **Pharmacogenomics / personalized medicine:** The key personalized-medicine action is genotype-guided de-escalation of immunosuppression and transplant planning.
- **Supportive care:** Nutrition, blood-pressure control, cardiovascular risk management, management of CKD complications (Ponticelli 2023; Braun 2025 [PMID: 40760331](https://pubmed.ncbi.nlm.nih.gov/40760331/)).

---

## 13. Prevention

- **Primary prevention:** None exists for a Mendelian recessive disorder.
- **Secondary/tertiary prevention:** Early genetic diagnosis to (a) stop ineffective/toxic immunosuppression, (b) institute nephroprotection (RAAS blockade), and (c) prevent complications (thromboprophylaxis, infection prevention, cardiovascular risk management).
- **Genetic counseling:** Autosomal recessive — **25% recurrence risk per pregnancy** for carrier couples. Offer carrier testing of relatives and reproductive options: prenatal diagnosis and **preimplantation genetic testing (PGT)**. Consanguinity counseling is particularly important in high-consanguinity populations.
- **Immunization / public health / environmental interventions:** Not applicable to disease prevention (genetic etiology); standard vaccination is advisable given nephrotic infection risk.

---

## 14. Other Species / Natural Disease

- **Conservation:** NUP133 is evolutionarily conserved from yeast to human; the *S. cerevisiae* Nup84–Nup133 Y-complex is structurally characterized (Nordeen 2020, [PMID: 33247142](https://pubmed.ncbi.nlm.nih.gov/33247142/)).
- **Orthologs:** Mouse *Nup133* (NCBI Gene 234865; NCBITaxon:10090); zebrafish *nup133* (NCBITaxon:7955); *Xenopus* (NCBITaxon:8355); *S. cerevisiae NUP133* (NCBITaxon:4932).
- **Natural disease in other species:** **None catalogued** — no naturally occurring NUP133 disease is recorded in OMIA for companion animals or wildlife. No veterinary relevance or zoonotic potential (the disease is genetic, not transmissible).

---

## 15. Model Organisms

| Model | Type | Phenotype recapitulation | Source |
|---|---|---|---|
| Zebrafish *nup133* morphant | In vivo vertebrate | Proteinuria, podocyte foot-process effacement, kidney cysts, microcephaly, reduced neurons | Cianciolo Cosentino 2019 [PMID: 30894603](https://pubmed.ncbi.nlm.nih.gov/30894603/); Fujita 2018 [PMID: 30427554](https://pubmed.ncbi.nlm.nih.gov/30427554/) |
| *Xenopus nup133* morpholino | In vivo vertebrate | Disrupted glomerulogenesis; rescued by WT but not mutant mRNA | Braun 2018 [PMID: 30179222](https://pubmed.ncbi.nlm.nih.gov/30179222/) |
| Human podocyte CRISPR/Cas9 KO | In vitro cellular | CDC42 activation; transcriptome/cytoskeleton dysregulation | Braun 2018; Rogg 2022 [PMID: 35455939](https://pubmed.ncbi.nlm.nih.gov/35455939/) |
| Mouse ESC / neural progenitors (Nup133-deficient) | In vitro differentiation | Normal pluripotency; defective neuronal differentiation | Orniacki 2023 [PMID: 37305998](https://pubmed.ncbi.nlm.nih.gov/37305998/); Taniguchi 2025 [PMID: 40205196](https://pubmed.ncbi.nlm.nih.gov/40205196/) |
| Podocyte-specific *Nup160* KO mouse (paralog) | In vivo mammalian | Proteinuria, foot-process fusion, Cdc42 dysregulation (validates pathway) | Qiao 2025 [PMID: 40298220](https://pubmed.ncbi.nlm.nih.gov/40298220/) |

- **Model limitations:** Constitutive *Nup133*-null mice are **not a viable disease model** — the gene is essential/embryonic-lethal. Conditional (podocyte-specific) and cellular models are therefore required. Zebrafish/Xenopus morphants model developmental renal and neural phenotypes well but are transient knockdowns.
- **Applications:** These systems established the CDC42 pathway (podocyte models), the neuronal-differentiation dependence (mESC), and the renal developmental phenotype (fish/frog), collectively supporting the tissue-specific-vulnerability model.
- **Resources:** MGI (mouse), ZFIN (zebrafish), Xenbase (Xenopus), SGD (yeast), Alliance of Genome Resources.

---

## Mechanistic Model / Interpretation

The unifying insight of NPHS18 is **cell-type-specific vulnerability to a ubiquitous housekeeping defect**. NUP133 is a scaffold nucleoporin required for assembling every nuclear pore in every cell, yet biallelic hypomorphic variants produce a phenotype largely confined to podocytes (renal) and, when more severe, developing neurons (GAMOS). Three observations reconcile this paradox:

1. **The variants are hypomorphic, not null** — complete loss is embryonic-lethal (mouse); patients retain partial NUP133 function, placing stress on the most-vulnerable cell types.
2. **Podocytes and neurons are uniquely sensitive** — podocytes are terminally differentiated, non-regenerating cells maintaining an elaborate actin-based foot-process architecture; neurons depend on NUP133 for differentiation and nuclear-envelope integrity. mESC experiments show Nup133 is dispensable for pluripotency but essential for neuroectodermal/neuronal differentiation.
3. **A specific downstream effector (CDC42) links the nuclear-pore defect to podocyte injury** — providing a mechanistic "final common pathway" shared across outer-ring nucleoporin SRNS (NUP107/NUP85/NUP133 activate CDC42; NUP160 loss likewise dysregulates Cdc42).

This model positions the NPC-scaffold/Y-complex defect **upstream** and CDC42-driven cytoskeletal collapse, foot-process effacement, and FSGS **downstream**, with a GAMOS branch when neural progenitors are affected during development. Protein-structural context: NUP133 comprises an N-terminal β-propeller (harboring an amphipathic lipid-packing-sensor, ALPS, membrane-anchoring motif) and a C-terminal α-solenoid that binds NUP107; it recruits NUP107 and ELYS to membrane fenestrations during post-mitotic NPC reassembly (Nordeen 2020 [PMID: 33247142](https://pubmed.ncbi.nlm.nih.gov/33247142/); Bilir 2019 [PMID: 30821042](https://pubmed.ncbi.nlm.nih.gov/30821042/)).

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [30179222](https://pubmed.ncbi.nlm.nih.gov/30179222/) | Mutations in multiple NPC components cause NS | **Landmark:** defines NUP133 as a causal SRNS gene; CDC42 activation mechanism; Xenopus rescue |
| [30427554](https://pubmed.ncbi.nlm.nih.gov/30427554/) | Homozygous splicing mutation in NUP133 causes GAMOS | Syndromic spectrum; c.3335-11T>A; impaired NUP133–NUP107 binding; zebrafish neural+renal phenotype |
| [39331077](https://pubmed.ncbi.nlm.nih.gov/39331077/) | Nucleoporin-associated SRNS (review) | Epidemiology (onset ~9 y, kidney failure ~13 y), 89% FSGS, immunosuppression resistance, extrarenal spectrum |
| [35455939](https://pubmed.ncbi.nlm.nih.gov/35455939/) | NUP133 controls NPC assembly, transcriptome, cytoskeleton | Podocyte-specific pathomechanism |
| [37565816](https://pubmed.ncbi.nlm.nih.gov/37565816/) | NUP205/YAP-TAZ in podocytes | NUP133 is a YAP/TAZ-complex component; Hippo-pathway link |
| [37305998](https://pubmed.ncbi.nlm.nih.gov/37305998/) | Y-complex nucleoporins in neuronal progenitors | Tissue-specific differentiation dependence |
| [40205196](https://pubmed.ncbi.nlm.nih.gov/40205196/) | Nuclear pores safeguard nuclear-envelope integrity | Neuronal differentiation dependence; GAMOS relevance |
| [30894603](https://pubmed.ncbi.nlm.nih.gov/30894603/) | Moderate Nup133 deficiency → glomerular damage (zebrafish) | Renal phenotype recapitulation |
| [40298220](https://pubmed.ncbi.nlm.nih.gov/40298220/) | Nup160 KO mouse dysregulates Cdc42 | Validates CDC42 pathway in a mammalian in-vivo paralog model |
| [33247142](https://pubmed.ncbi.nlm.nih.gov/33247142/) | Yeast Nup84–Nup133 structure, ALPS motif | Protein architecture/conservation |
| [30821042](https://pubmed.ncbi.nlm.nih.gov/30821042/) | Nup133/Nup153 in NPC assembly | NUP133 recruits NUP107 and ELYS |
| [37041680](https://pubmed.ncbi.nlm.nih.gov/37041680/) | NUP133 p.Lys966Asn structural modeling | Variant-level functional insight |
| [36176665](https://pubmed.ncbi.nlm.nih.gov/36176665/) | Genetic characteristics of FSGS | ~30% of pediatric SRNS is monogenic |
| [40402239](https://pubmed.ncbi.nlm.nih.gov/40402239/) | WGS in early-onset SRNS | 56.1% diagnostic yield in consanguineous families |
| [38654395](https://pubmed.ncbi.nlm.nih.gov/38654395/) | Genetic testing modalities in SRNS | Panel vs WES vs WGS yields/costs |
| [37466816](https://pubmed.ncbi.nlm.nih.gov/37466816/) | NS pathophysiology and consequences | Hypercoagulability/thromboprophylaxis rationale |

---

## Limitations and Knowledge Gaps

1. **Rarity:** NPHS18 is known from a small number of families; precise prevalence/incidence, penetrance, and carrier frequency are undefined. No large natural-history cohort exists.
2. **Variant landscape:** ClinVar is dominated by VUS (117) with only one gene-specific likely-pathogenic small variant; most validated alleles are in primary literature. Variant interpretation remains a major clinical challenge.
3. **Genotype–phenotype correlation:** The determinants of the SRNS-vs-GAMOS spectrum (why some biallelic variants cause isolated kidney disease and others cause neuro-renal syndrome) are incompletely understood; modifier genes are unproven.
4. **CDC42 mechanism:** How NPC dysfunction mechanistically activates CDC42 in podocytes (direct vs indirect, transport-dependent vs transcriptional) is not fully resolved.
5. **No definitive mammalian NUP133 kidney model:** Constitutive knockout is lethal; a podocyte-specific *Nup133* conditional mouse (analogous to the existing *Nup160* model) is lacking.
6. **No disease-modifying therapy:** Treatment is entirely supportive; no gene/RNA/cell therapy or CDC42-targeted drug exists for patients.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a podocyte-specific conditional *Nup133* knockout mouse** (mirroring the *Nup160^podo−/−^* model) to definitively characterize the in-vivo renal pathomechanism and test the CDC42 hypothesis causally.
2. **Reclassify *NUP133* VUS** via systematic functional assays (minigene/splice assays, NUP107 co-IP binding, podocyte CDC42 activation) and ClinGen variant curation to reduce the VUS burden.
3. **Test CDC42-pathway inhibition** (e.g., CDC42/Rac inhibitors) in human podocyte and zebrafish models as a candidate targeted therapy for nucleoporin-SRNS.
4. **Build a NUP133 genotype–phenotype registry** linking specific alleles to SRNS-only vs GAMOS outcomes and to age at kidney failure, to improve prognostic counseling.
5. **Define carrier frequency and population distribution** using gnomAD and targeted consanguineous-cohort sequencing to inform reproductive counseling and cascade testing.
6. **Patient-derived iPSC podocyte/kidney-organoid models** carrying patient NUP133 variants to study transcriptome/cytoskeleton phenotypes and screen for rescuing compounds.


## Artifacts

- [OpenScientist final report](Nephrotic_Syndrome_Type_18-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Nephrotic_Syndrome_Type_18-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 22 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 22 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 14 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032581` (2 mentions) - the report calls it "MONDO"; MONDO calls it **nephrotic syndrome, type 18**
- `HP:0000100` (1 mention) - the report calls it "Clinical/lab"; HP calls it **Nephrotic syndrome**
- `HP:0003073` (1 mention) - the report calls it "Lab"; HP calls it **Hypoalbuminemia**
- `HP:0000969` (1 mention) - the report calls it "Clinical sign"; HP calls it **Edema**
- `HP:0003077` (1 mention) - the report calls it "Lab"; HP calls it **Hyperlipidemia**
- `HP:0000097` (1 mention) - the report calls it "Pathology"; HP calls it **Focal segmental glomerulosclerosis**
- `HP:0000252` (1 mention) - the report calls it "Physical"; HP calls it **Microcephaly**
- `HP:0012444` (1 mention) - the report calls it "Imaging/structural"; HP calls it **Brain atrophy**
- `HP:0001252` (1 mention) - the report calls it "Neuro"; HP calls it **Hypotonia**
- `HP:0004936` (1 mention) - the report calls it "Clinical"; HP calls it **Venous thrombosis**
- `HP:0002719` (1 mention) - the report calls it "Clinical"; HP calls it **Recurrent infections**
- `UBERON:0002113` (1 mention) - the report calls it "Organ level — primary:** Kidney"; UBERON calls it **kidney**
- `UBERON:0000955` (1 mention) - the report calls it "brain / cerebral cortex"; UBERON calls it **brain**
- `NCBITaxon:7955` (1 mention) - the report calls it "nup133"; NCBITaxon calls it **Danio rerio**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0051292` (2 mentions) - the report calls it "Cellular processes:** NPC assembly", "NPC assembly"; GO calls it **nuclear pore complex assembly**, and lists "nuclear pore assembly" among its other names
- `GO:0006406` (2 mentions) - the report calls it "mRNA export"; GO calls it **mRNA export from nucleus**, and lists "mRNA-nucleus export" among its other names
- `CL:0000653` (2 mentions) - the report calls it "Tissue/cell level:** Glomerular visceral epithelial cells — **podocytes"; CL calls it **podocyte**, and lists "glomerular visceral epithelial cell" among its other names
- `GO:0005643` (1 mention) - the report calls it "Subcellular level:** **Nuclear pore complex"; GO calls it **nuclear pore**, and lists "nuclear pore complex" among its other names
- `NCBITaxon:8355` (1 mention) - the report calls it "Xenopus"; NCBITaxon calls it **Xenopus laevis**
- `NCBITaxon:4932` (1 mention) - the report calls it "S. cerevisiae NUP133"; NCBITaxon calls it **Saccharomyces cerevisiae**, and lists "Mycoderma cerevisiae" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0051292` - called "Cellular processes:** NPC assembly", "NPC assembly"