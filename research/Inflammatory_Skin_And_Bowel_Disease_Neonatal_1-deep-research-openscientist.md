---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-28T22:35:05.776251'
end_time: '2026-10-28T23:19:54.731971'
duration_seconds: 2688.96
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Inflammatory Skin and Bowel Disease, Neonatal, 1
  mondo_id: MONDO:0013693
  category: Mendelian
  causal_genes: ADAM17
  omim_id: not recorded
  synonyms: not recorded
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
citation_count: 17
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 12
  validator_version: 0.4.0
term_validation:
  total_terms: 40
  verified: 39
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 21
  labels_matching: 10
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: HP:0004421
    reported_labels:
    - Systolic hypertension
    ontology_label: Elevated systolic blood pressure
  - term_id: UBERON:0002107
    reported_labels:
    - hepatitis
    ontology_label: liver
  - term_id: UBERON:0000948
    reported_labels:
    - cardiomyopathy/myocarditis
    ontology_label: heart
  - term_id: NCIT:C2367
    reported_labels:
    - TNF Inhibitor
    ontology_label: Triazene Derivative CB10-277
  - term_id: NCIT:C1972
    reported_labels:
    - Monoclonal Antibody
    ontology_label: Deferoxamine Hydrochloride
  - term_id: NCIT:C1130
    reported_labels:
    - Budesonide
    ontology_label: Hydroxyl Radical
  - term_id: NCIT:C15190
    reported_labels:
    - Nutritional Support
    ontology_label: Needle Biopsy
  labels_variant: 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Inflammatory_Skin_And_Bowel_Disease_Neonatal_1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Inflammatory_Skin_And_Bowel_Disease_Neonatal_1-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Inflammatory Skin and Bowel Disease, Neonatal, 1
- **MONDO ID:** MONDO:0013693 (if available)
- **Causal gene(s):** ADAM17
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Inflammatory Skin and Bowel Disease, Neonatal, 1** covering all of the
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

# Neonatal Inflammatory Skin and Bowel Disease, Type 1 (NISBD1) — Comprehensive Disease Report

**Disease:** Inflammatory Skin and Bowel Disease, Neonatal, 1 (NISBD1)
**MONDO ID:** MONDO:0013693 · **OMIM:** #614328
**Causal gene:** **ADAM17** (a disintegrin and metalloproteinase 17; also called **TACE**, TNF-α-converting enzyme; HGNC:195)
**Inheritance:** Autosomal recessive · **Category:** Mendelian

---

## Summary

**Neonatal Inflammatory Skin and Bowel Disease type 1 (NISBD1)** is an ultra-rare, autosomal-recessive Mendelian disorder caused by **biallelic loss-of-function (LOF) variants in ADAM17** (TACE). ADAM17 is the principal cell-surface "sheddase" that proteolytically releases the active, soluble forms of **EGFR ligands** (TGF-α, amphiregulin, HB-EGF) and of **TNF-α** from the plasma membrane. When ADAM17 activity is lost, epithelial tissues fail to receive EGFR-ligand–driven developmental and barrier-maintenance signals, and inflammatory cytokine signaling becomes dysregulated. The result is a neonatal-onset multi-system disease dominated by inflammatory skin disease, inflammatory/secretory bowel disease, and hair/nail abnormalities.

Clinically, affected neonates present with a **collodion membrane at birth, diffuse scaly erythematous skin / erythroderma, evanescent pustules, chronic watery diarrhea, failure to thrive, and recurrent bacterial infections/sepsis**. Additional features include **fragile or absent hair (atrichia), nail dystrophy, esophageal strictures**, and variable multi-organ involvement (hepatitis, cardiomyopathy, hypertension). Mortality in infancy and childhood is substantial, driven by sepsis and cardiac disease. Fewer than ~10 families have been reported worldwide since the disease was first defined in 2011, and consanguinity is a recurrent feature.

The mechanistic basis is now well-supported. ADAM17-null mice phenocopy EGFR/TGF-α-pathway deficiency; conditional deletions reproduce the hair-follicle, skin-barrier, and colonic-inflammation phenotypes; and the obligate ADAM17 cofactors iRhom1/iRhom2 (RHBDF1/RHBDF2) tune enzyme maturation and activity — with *gain-of-function* iRHOM2 mutations causing the mirror-image skin disease tylosis with esophageal cancer. Crucially, **NISBD1 (ADAM17 loss) and NISBD2 (EGFR loss) form an allelic series along a single pathway**, confirming that the pathology runs through the **ADAM17 → EGFR-ligand → EGFR** epithelial axis. Management is supportive plus anti-inflammatory/biologic therapy (notably combined anti-TNF-α + IL-12/23 blockade for skin, budesonide for gut); no curative therapy exists.

> **Note on disease identity.** The identifiers in the task (MONDO:0013693 + ADAM17) point unambiguously to NISBD1. It must be distinguished from the phenotypically overlapping **NISBD2 (OMIM #616069)**, caused by biallelic variants in **EGFR** — a different gene acting immediately **downstream** of ADAM17 in the same pathway. That very overlap is strong evidence that NISBD1 pathology is EGFR-pathway driven. All content below refers to the ADAM17 (NISBD1) entity.

---

## Key Findings

### Finding 1 — NISBD1 is caused by biallelic loss-of-function variants in ADAM17 (TACE)

The founding report by **Blaydon et al. (NEJM 2011)** mapped autosomal-recessive neonatal inflammatory skin and bowel lesions in a consanguineous sibpair to a loss-of-function mutation in ADAM17. Patient peripheral-blood mononuclear cells (PBMCs) showed **impaired LPS-induced TNF-α release but elevated IL-1β and IL-6**, consistent with loss of the enzyme that normally sheds membrane pro-TNF-α. The authors concluded: *"We identified a loss-of-function mutation in ADAM17, which encodes a disintegrin and metalloproteinase 17 (also called tumor necrosis factor α [TNF-α]-converting enzyme, or TACE), as the probable cause of this syndrome"* ([PMID: 22010916](https://pubmed.ncbi.nlm.nih.gov/22010916/)).

The gene–disease relationship has been reproduced in multiple independent families with diverse LOF alleles:
- **Bandsma et al. (2015)**: homozygous frameshift `NM_003183.4:c.308dupA`, producing a premature stop codon — *"We identified a novel homozygous frameshift mutation in ADAM17 (NM_003183.4:c.308dupA) leading to a premature stop codon"* ([PMID: 25804906](https://pubmed.ncbi.nlm.nih.gov/25804906/)).
- **Imoto et al. (2021)**: functionally confirmed compound-heterozygous **missense** variants `c.1699T>C (p.Cys567Arg)` and `c.1799G>A (p.Cys600Tyr)`, validated in an Adam10/17 double-knockout mouse-fibroblast shedding assay ([PMID: 33953303](https://pubmed.ncbi.nlm.nih.gov/33953303/)).
- **Samuelov et al. (2022)**: a complex compound-heterozygous defect — a large deletion of exons 6–7 plus a splice variant causing exon-17 skipping ([PMID: 34993966](https://pubmed.ncbi.nlm.nih.gov/34993966/)).
- **Malhi et al. (2026)** and **Chang et al. (2026)**: additional homozygous alleles, including `c.436G>A; p.Gln146Lys`, expanding the phenotype ([PMID: 42015567](https://pubmed.ncbi.nlm.nih.gov/42015567/), [PMID: 40968583](https://pubmed.ncbi.nlm.nih.gov/40968583/)).

**Evidence type:** human clinical + in vitro functional confirmation. The convergence of nonsense, frameshift, missense, large-deletion, and splice alleles — all LOF — firmly establishes ADAM17 haploinsufficiency/null as the cause.

### Finding 2 — ADAM17 is the major sheddase of EGFR ligands and TNF-α; its loss impairs epithelial development

ADAM17 processes **more than 80 substrates**, most importantly the EGFR-family growth factors and pro-TNF-α (Imoto 2021, [PMID: 33953303](https://pubmed.ncbi.nlm.nih.gov/33953303/)). **Peschon et al. (Science 1998)** showed that TACE/ADAM17-null mice fail to process TGF-α and phenocopy EGFR-pathway deficiency, concluding: *"The phenotype of mice lacking TACE suggests an essential role for soluble TGFalpha in normal development and emphasizes the importance of protein ectodomain shedding in vivo"* ([PMID: 9812885](https://pubmed.ncbi.nlm.nih.gov/9812885/)). **Edwards et al. (2008)** summarize the enzyme's physiological role: *"ADAM-17 is required for generation of the active forms of Epidermal Growth Factor Receptor (EGFR) ligands, and its function is essential for the development of epithelial tissues"* ([PMID: 18762209](https://pubmed.ncbi.nlm.nih.gov/18762209/)).

This establishes the mechanistic "why": ADAM17 loss simultaneously (a) **removes the proteolytic step that generates active EGFR ligands**, starving epithelial tissue of EGFR-driven proliferation/differentiation/barrier signals, and (b) **alters TNF-α and other cytokine processing**, dysregulating inflammation.

### Finding 3 — iRhom2/iRhom1 (RHBDF2/RHBDF1) are obligate cofactors controlling ADAM17 maturation and activation

ADAM17 does not act alone. Cryo-EM structures demonstrate that **iRhom2 promotes ADAM17 trafficking and enzyme maturation and retains the inhibitory prodomain to prevent premature activation**. **Lu et al. (2024)**: *"iRhom2 interacts with the ADAM17 TMD to promote ADAM17 trafficking and enzyme maturation"* ([PMID: 38781971](https://pubmed.ncbi.nlm.nih.gov/38781971/)); **Maciag et al. (2025)** add structural detail on prodomain-mediated inhibition and a cytoplasmic re-entry loop involved in activation ([PMID: 40512800](https://pubmed.ncbi.nlm.nih.gov/40512800/)).

The clinical mirror image is instructive: **gain-of-function iRHOM2 mutations cause tylosis with esophageal cancer (TOC)** by *increasing* ADAM17 maturation/activity. **Brooke et al. (2014)**: *"TOC-associated mutations in iRHOM2 cause an increase in the maturation and activity of ADAM17 in epidermal keratinocytes, resulting in significantly upregulated shedding of ADAM17 substrates, including EGF-family growth factors and pro-inflammatory cytokines"* ([PMID: 24643277](https://pubmed.ncbi.nlm.nih.gov/24643277/)). NISBD1 (too little ADAM17 activity) and TOC (too much) thus bracket the same axis — strong orthogonal support for the pathway.

### Finding 4 — NISBD1 skin inflammation responds to combined anti-TNF-α and IL-12/23 blockade

**Samuelov et al. (2022)** reported a NISBD1 patient with erythroderma, atrichia, nail dystrophy, esophageal strictures, intractable diarrhea and failure to thrive (complex compound-heterozygous ADAM17 defect). *"Skin manifestations dramatically improved in response to combined anti-tumour necrosis factor-α and interleukin-12/23 blockade, while gastrointestinal symptoms were controlled with budesonide"* ([PMID: 34993966](https://pubmed.ncbi.nlm.nih.gov/34993966/)). This provides the best-documented targeted therapeutic strategy and reinforces the inflammatory cytokine component of the disease.

### Finding 5 — Mouse Adam17 models recapitulate key NISBD1 features via EGFR-ligand shedding

| Model | Phenotype | NISBD1 feature modeled | PMID |
|---|---|---|---|
| Adam17-null (germline) | Perinatal/embryonic lethal; open-eye-at-birth; skin/epithelial defects; phenocopies EGFR/TGF-α deficiency | Skin barrier / epithelial immaturity | [9812885](https://pubmed.ncbi.nlm.nih.gov/9812885/) |
| Tace/Sox9 conditional (hair-follicle stem cells) | Brittle hair, prolonged anagen, progressive whole-body hair loss, loss of CD34+ bulge cells | Fragile hair / atrichia | [22696231](https://pubmed.ncbi.nlm.nih.gov/22696231/) |
| Systemic/intestinal Adam17 deletion | Severe DSS colitis; impaired EGFR activation, epithelial proliferation, mucus/goblet-cell production, barrier function | Bowel inflammation | [27077118](https://pubmed.ncbi.nlm.nih.gov/27077118/) |
| iRhom gain/loss (cub/toc) | Skin/hair phenotypes dependent on amphiregulin + Adam17 | ADAM17→AREG→EGFR dependence | [37282854](https://pubmed.ncbi.nlm.nih.gov/37282854/) |

**Nagao et al. (2012)**: *"Tace/Sox9 mice were born with brittle hair with prolonged anagen phase. They underwent diffuse, progressive, and ultimately whole-body hair loss by 20 weeks old"* ([PMID: 22696231](https://pubmed.ncbi.nlm.nih.gov/22696231/)). **Shimoda et al. (2016)**: *"Mice with systemic deletion of Adam17 developed severe dextran sulfate sodium-induced colitis"* ([PMID: 27077118](https://pubmed.ncbi.nlm.nih.gov/27077118/)). These models causally link ADAM17 loss to the skin, hair, and gut arms of the human disease through impaired EGFR signaling.

### Finding 6 — Phenotype spectrum: neonatal erythroderma/pustules, intractable diarrhea, failure to thrive, infections, hair/nail defects, multi-organ involvement

The core triad across families is **chronic watery diarrhea, failure to thrive, and skin disease**. **Chang et al. (2026)**: *"characterized by chronic diarrhea, failure to thrive, rash, and recurrent bacterial infections. Cutaneous manifestations include the presence of a collodion membrane at birth, diffuse scaly erythematous patches and thin plaques, evanescent pustules, and/or erythroderma"* ([PMID: 40968583](https://pubmed.ncbi.nlm.nih.gov/40968583/)). Additional features include fragile/absent hair (atrichia), nail dystrophy, and esophageal strictures (Samuelov 2022, [PMID: 34993966](https://pubmed.ncbi.nlm.nih.gov/34993966/)).

Multi-organ dysfunction is documented. **Bandsma et al. (2015)**: *"the patient developed unexplained systolic hypertension and nonspecific hepatitis with apoptosis"*, with recurrent sepsis causing death at 10 months and diminished T-cell TNF-α/IL-2 production ([PMID: 25804906](https://pubmed.ncbi.nlm.nih.gov/25804906/)). Cardiac disease is a recognized cause of death (see Finding 7). An atypical patient presented with pyoderma-gangrenosum-like ulcerations and pyostomatitis-like mucosal involvement but **no bowel disease** ([PMID: 42015567](https://pubmed.ncbi.nlm.nih.gov/42015567/)), underscoring variable expressivity.

### Finding 7 — Ultra-rare autosomal-recessive disorder with complete penetrance, variable expressivity, and high early mortality

Inheritance is autosomal recessive (OMIM #614328), requiring biallelic ADAM17 LOF; **fewer than ~10 families have been reported worldwide since 2011**, frequently consanguineous. Penetrance appears complete but **expressivity varies from survivable chronic disease to fatal infantile course**. Mortality drivers include sepsis (death at 10 months — Bandsma 2015) and cardiac disease. **Blaydon et al. (2011)**: *"The girl died suddenly at 12 years of age from parvovirus B19-associated myocarditis; her brother had mild cardiomyopathy"* ([PMID: 22010916](https://pubmed.ncbi.nlm.nih.gov/22010916/)). Diagnosis is genomic — WES/WGS or targeted ADAM17 sequencing plus deletion/splicing analysis; **a 2024 study** supports an upfront WGS approach for these barrier/immune disorders: *"Upfront genome-wide analysis by whole genome sequencing (WGS) will shorten the time to diagnosis, save patients from unnecessary investigations, and reduce morbidity and mortality"* ([PMID: 39381601](https://pubmed.ncbi.nlm.nih.gov/39381601/)).

### Finding 8 — NISBD1 (ADAM17) and NISBD2 (EGFR) are an allelic series along one pathway

**NISBD2** (OMIM #616069) is an autosomal-recessive, EGFR-associated early-infantile disease. **Karabinos et al. (2025)**: *"Neonatal inflammatory skin and bowel disease 2 is an epidermal growth factor receptor (EGFR)-associated autosomal recessive early-infantile disease with inflammatory skin, alopecia, progeroid features, electrolyte imbalance, recurrent infections, and premature death"* ([PMID: 40040597](https://pubmed.ncbi.nlm.nih.gov/40040597/)). EGFR-null mice show postnatal lethality with epithelial immaturity and intestinal lesions: *"The mildest form of EGF-R inactivation leads to epithelial immaturity and postnatal death due to respiratory failure and necrotizing enterocolitis-like lesions in the intestine"* ([PMID: 9562519](https://pubmed.ncbi.nlm.nih.gov/9562519/)). Because ADAM17 generates the soluble ligands that activate EGFR, the near-identical phenotypes place NISBD1 and NISBD2 at **consecutive steps of a single ADAM17 → EGFR-ligand → EGFR epithelial axis** — the strongest internal validation of the proposed mechanism.

---

## Section-by-Section Report

### 1. Disease Information

NISBD1 is a Mendelian, autosomal-recessive genodermatosis-plus-enteropathy of neonatal onset, caused by loss of ADAM17 sheddase function. It combines severe inflammatory skin disease, inflammatory/secretory bowel disease, hair and nail defects, and heightened infection susceptibility.

**Key identifiers:**
- **MONDO:** MONDO:0013693
- **OMIM:** #614328 (Inflammatory skin and bowel disease, neonatal, 1)
- **Orphanet:** NISBD / ADAM17 deficiency (listed under neonatal inflammatory skin and bowel disease)
- **ICD-10:** no specific code; mapped under congenital ichthyosiform erythroderma + inflammatory enteropathy categories (e.g., Q80.x / K52.x as closest approximations)
- **MeSH:** no dedicated descriptor; indexed via ADAM17 Protein, erythroderma, and inflammatory bowel disease terms

**Synonyms / alternative names:** NISBD1; ADAM17 deficiency; neonatal inflammatory skin and bowel disease due to ADAM17 mutation; inflammatory skin and bowel disease, neonatal, type 1.

**Information source:** Disease-level knowledge derives from aggregated OMIM/Orphanet entries and a small number of **individual-patient case reports/series** (fewer than ~10 families). There is no large EHR-derived cohort; all data are case-based.

### 2. Etiology

**Primary cause:** Genetic — biallelic (homozygous or compound-heterozygous) loss-of-function variants in **ADAM17** (Findings 1–2). The disease is fully genetic; no environmental or infectious cause initiates it, although infections are frequent *complications*.

**Genetic risk factors:** The causal variants themselves (LOF ADAM17 alleles) are the entire genetic risk. **Consanguinity** markedly raises risk by increasing homozygosity for rare recessive LOF alleles. No common susceptibility loci or GWAS signals apply (this is monogenic).

**Modifier genes:** iRhom1/iRhom2 (RHBDF1/RHBDF2) and downstream EGFR-pathway genes are biologically plausible modifiers of residual ADAM17 activity/expressivity (Finding 3), but no formal human modifier has been proven. Variable expressivity (e.g., absence of bowel disease in one patient, [PMID: 42015567](https://pubmed.ncbi.nlm.nih.gov/42015567/)) suggests modifiers and/or allele-specific residual function.

**Environmental risk factors:** None causal. Postnatal microbial exposure and barrier breakdown drive the infectious complications. **Protective factors:** none genetically established; supportive measures (infection prophylaxis, nutrition) mitigate severity. **Gene–environment interactions:** the genetic barrier/immune defect sensitizes patients to environmental microbes (bacterial skin infection, sepsis) — a gene→environment susceptibility relationship rather than a modifying GxE effect.

### 3. Phenotypes

| Phenotype | Type | Onset | Frequency | Suggested HPO |
|---|---|---|---|---|
| Erythroderma / scaly erythematous patches | Clinical sign (skin) | Neonatal | Very frequent | HP:0001019 (Erythroderma) |
| Collodion membrane at birth | Physical manifestation | Congenital | Frequent | HP:0007479 / collodion membrane |
| Pustular skin lesions (evanescent) | Clinical sign | Neonatal | Frequent | HP:0200039 (Pustule) |
| Chronic watery diarrhea | Symptom (GI) | Neonatal | Very frequent | HP:0002028 (Chronic diarrhea) |
| Failure to thrive | Clinical sign | Neonatal/infancy | Very frequent | HP:0001508 (Failure to thrive) |
| Recurrent bacterial infections / sepsis | Clinical sign | Infancy | Frequent | HP:0002718 (Recurrent bacterial infections) |
| Fragile hair / atrichia | Physical manifestation | Infancy | Frequent | HP:0011362 / HP:0001596 (Alopecia) |
| Nail dystrophy (paronychia) | Physical manifestation | Infancy | Frequent | HP:0008404 (Nail dysplasia) |
| Esophageal strictures | Clinical sign | Variable | Occasional | Esophageal stricture |
| Hepatitis with apoptosis | Lab/pathology | Variable | Occasional | HP:0200119 (Hepatitis) |
| Cardiomyopathy / myocarditis | Clinical sign | Childhood | Occasional (fatal) | HP:0001638 (Cardiomyopathy) |
| Systolic hypertension | Lab/sign | Variable | Rare | HP:0004421 (Systolic hypertension) |

**Severity:** Severe, often life-threatening in infancy; **progression:** chronic with episodic flares; **variable expressivity** documented. **Quality-of-life impact** is profound in affected infants (chronic skin pain/pruritus, malabsorption, hospitalization, infection burden), though no formal QoL instrument data exist for this ultra-rare disease.

### 4. Genetic / Molecular Information

- **Causal gene:** ADAM17 (chromosome 2p25.1; OMIM *603639; HGNC:195; UniProt P78536).
- **Variant classification:** Reported variants are **pathogenic/likely pathogenic** (ACMG/AMP), functionally confirmed in several cases.
- **Variant types reported:** nonsense/frameshift (`c.308dupA`), missense (`p.Cys567Arg`, `p.Cys600Tyr`, `p.Gln146Lys`), large multi-exon deletion (exons 6–7), and splice variant (exon-17 skipping). The cysteine-substitution missense variants disrupt disulfide-dependent folding of the metalloprotease/disintegrin region, abolishing shedding (Imoto 2021).
- **Allele frequency:** All causal alleles are ultra-rare/private in gnomAD; biallelic LOF of ADAM17 is essentially absent in the general population, consistent with severe recessive disease.
- **Origin:** Germline, recessive. No somatic-mosaicism cases reported.
- **Functional consequence:** **Loss of function** (reduced/absent ADAM17 sheddase activity). Complete LOF in originally described patients; missense alleles cause functional LOF.
- **Modifier genes / epigenetics / chromosomal abnormalities:** No epigenetic mechanism or chromosomal abnormality is implicated; iRhom cofactors are mechanistic modulators (Finding 3) but not reported disease modifiers in patients.

### 5. Environmental Information

NISBD1 has **no environmental or infectious cause**. Environmental factors are relevant only as **triggers of complications**: cutaneous/systemic bacterial infection and sepsis arise because of the defective skin barrier and dysregulated immunity. No toxin, occupational exposure, lifestyle, or dietary factor is etiologic. Infectious agents (e.g., *Staphylococcus* and other skin/gut flora; parvovirus B19 in one fatal myocarditis case) act opportunistically on the genetically impaired host.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic LOF variants in ADAM17** (nonsense/frameshift/missense/deletion/splice) reduce or abolish ADAM17 (TACE) protein/activity. *(demonstrated — Findings 1–2)*
2. Loss of ADAM17 **results in failure of ectodomain shedding** of membrane-anchored EGFR ligands (TGF-α, amphiregulin, HB-EGF) and of pro-TNF-α. *(demonstrated — Peschon 1998; Edwards 2008)*
3. Failure to release soluble EGFR ligands **leads to deficient EGFR (ErbB1) signaling** in epithelial tissues. *(demonstrated in models — Nagao 2012; Shimoda 2016)*
4. Deficient EGFR signaling **results in impaired epithelial proliferation, differentiation, barrier formation, and goblet-cell/mucus production**. *(demonstrated)*
   - **Branch A (skin/hair):** → defective stratum-corneum barrier and hair-follicle stem-cell niche → **collodion membrane, erythroderma, pustules, fragile hair/atrichia, nail dystrophy**.
   - **Branch B (gut):** → impaired colonic epithelial protection → **intestinal inflammation, chronic secretory/inflammatory diarrhea, failure to thrive**.
5. Barrier breakdown plus dysregulated cytokine processing (loss of orderly TNF-α shedding; elevated IL-1β/IL-6; impaired T-cell TNF-α/IL-2) **leads to recurrent bacterial infection and sepsis**. *(demonstrated — Blaydon 2011; Bandsma 2015)*
6. Systemic inflammation and still-incompletely-defined mechanisms **contribute to multi-organ involvement** — hepatitis, hypertension, cardiomyopathy/myocarditis. *(observed; mechanism partly inferred)*
7. Sepsis and cardiac disease **are the principal causes of early mortality**. *(demonstrated)*

**Molecular pathways:** EGFR/ErbB (MAPK-ERK, PI3K-AKT downstream); TNF/TNF-receptor signaling. **Cellular processes:** epithelial proliferation/differentiation (GO:0030855 epithelial cell differentiation), keratinocyte differentiation (GO:0030216), inflammatory response (GO:0006954), hair-follicle development (GO:0001942), membrane-protein ectodomain proteolysis (GO:0006509). **Protein dysfunction:** loss of metalloprotease catalytic function (GO:0004222 metalloendopeptidase activity) due to truncation, misfolding (cysteine variants), or absent protein. **Immune involvement:** combined barrier-immunodeficiency and dysregulated innate cytokine milieu (elevated IL-1β/IL-6, impaired TNF-α release). **Tissue damage:** inflammatory epithelial injury of skin and gut from loss of trophic/protective EGFR signaling plus secondary infection.

**Upstream vs downstream:** ADAM17 LOF (upstream) → EGFR-ligand deficiency → EGFR signaling loss → epithelial failure and inflammation (downstream). The NISBD1↔NISBD2 allelic series (Finding 8) confirms ADAM17 is immediately upstream of EGFR.

**Suggested CL cell types:** keratinocyte (CL:0000312), basal epidermal cell (CL:0002187), hair-follicle stem/bulge cell, intestinal epithelial cell (CL:0002563), goblet cell (CL:0000160), T cell (CL:0000084), macrophage (CL:0000235).

### 7. Anatomical Structures Affected

- **Primary organs:** **Skin** (UBERON:0002097) and **intestine/colon** (UBERON:0000160 / UBERON:0001155); **hair follicle** (UBERON:0002073); **nail** (UBERON:0001705); **esophagus** (UBERON:0001043).
- **Secondary / systemic:** liver (UBERON:0002107 — hepatitis), heart (UBERON:0000948 — cardiomyopathy/myocarditis), vasculature (hypertension), immune system.
- **Body systems:** integumentary, digestive, cardiovascular, hepatic, immune.
- **Tissue/cell level:** stratified squamous epithelium of skin/esophagus; intestinal columnar epithelium with goblet cells; hair-follicle stem-cell (bulge, CD34+) compartment.
- **Subcellular:** plasma membrane (GO:0005886) — the site of ADAM17 sheddase activity; secretory/trafficking compartments (ER/Golgi) relevant to ADAM17 maturation via iRhom cofactors.
- **Lateralization:** bilateral/generalized skin and diffuse gut involvement (not lateralized).

### 8. Temporal Development

- **Onset:** **Neonatal / congenital** (collodion membrane at birth; skin and GI disease within the first days–weeks of life).
- **Onset pattern:** acute neonatal presentation, chronic course.
- **Progression:** chronic, with episodic inflammatory flares and recurrent infections; hair/nail and GI features persist.
- **Disease course:** chronic lifelong in survivors; high early mortality (infancy–childhood). No spontaneous remission; partial, treatment-induced improvement reported with biologics (Finding 4).
- **Critical periods:** the neonatal–infancy window is both the period of greatest vulnerability (sepsis, failure to thrive) and the key window for supportive/anti-inflammatory intervention.

### 9. Inheritance and Population

- **Inheritance:** Autosomal recessive (OMIM #614328).
- **Penetrance:** complete (biallelic LOF → disease). **Expressivity:** variable (survivable chronic disease to fatal infantile course; one patient lacked bowel disease).
- **Epidemiology:** ultra-rare; **<10 families reported worldwide** since 2011. Precise prevalence/incidence are not established (orphan-level, likely <1/1,000,000).
- **Consanguinity:** major contributor (several homozygous cases from consanguineous unions).
- **Founder effects:** none established; alleles are largely private.
- **Carrier frequency:** not formally estimated; biallelic LOF essentially absent from gnomAD.
- **Sex ratio:** no sex bias reported (autosomal). **Geographic distribution:** cases reported across multiple regions (Europe, Middle East, South Asia, East Asia), without a defined endemic focus.

### 10. Diagnostics

- **Genetic testing (definitive):** WES or WGS, or targeted ADAM17 sequencing, **plus** copy-number/deletion analysis and RNA/splicing assessment (needed to detect large deletions and splice variants, as in Samuelov 2022). WGS-first is advocated for faster diagnosis of such barrier/immune disorders ([PMID: 39381601](https://pubmed.ncbi.nlm.nih.gov/39381601/)).
- **Functional confirmation:** cell-based shedding assays (e.g., Adam10/17 double-knockout fibroblasts) to classify missense VUS as LOF (Imoto 2021).
- **Laboratory/immunology:** impaired LPS-induced TNF-α release with elevated IL-1β/IL-6 (patient PBMCs); diminished T-cell TNF-α/IL-2 production (Bandsma 2015). These support but do not alone diagnose.
- **Histopathology:** skin biopsy shows psoriasiform/inflammatory changes with barrier abnormality; gut biopsy shows inflammatory enteropathy.
- **Differential diagnosis:** **NISBD2 (EGFR)** — nearly identical, distinguished only by gene; Netherton syndrome (SPINK5); other congenital ichthyosiform erythrodermas; very-early-onset/monogenic IBD (e.g., IL-10/IL-10R defects); primary immunodeficiency with skin/gut inflammation; acrodermatitis enteropathica. Genetic testing resolves the differential.
- **Screening:** no population newborn screen; **cascade carrier testing** of relatives and genetic counseling are appropriate once the familial variant is known.

### 11. Outcome / Prognosis

- **Mortality:** high in infancy/childhood. Documented deaths: sepsis at 10 months (Bandsma 2015); sudden death at 12 years from parvovirus B19 myocarditis (Blaydon 2011). **Cardiac disease and sepsis are the main disease-attributable causes of death.**
- **Morbidity:** chronic skin disease, malabsorption/failure to thrive, recurrent infections, hair/nail disability, esophageal stricture.
- **Recovery potential:** no cure; partial symptomatic improvement achievable (biologics for skin, budesonide for gut). Survivors face chronic lifelong disease.
- **Prognostic factors:** severity/organ extent (especially cardiac involvement and sepsis frequency); residual ADAM17 function (allele-dependent); timeliness of supportive care and infection control.

### 12. Treatment

No curative therapy exists; management is **supportive + anti-inflammatory/biologic + genotype-aware**.

| Modality | Example | Rationale / evidence | NCIT suggestion |
|---|---|---|---|
| Anti-TNF-α biologic | infliximab/etanercept-class | Skin improvement in combination regimen (Samuelov 2022) | NCIT:C2367 (TNF Inhibitor) |
| IL-12/23 blockade | ustekinumab-class | Combined with anti-TNF, "dramatically improved" skin ([PMID: 34993966](https://pubmed.ncbi.nlm.nih.gov/34993966/)) | NCIT:C1972 (Monoclonal Antibody) |
| Enteric corticosteroid | budesonide | Controlled GI symptoms (Samuelov 2022) | NCIT:C1130 (Budesonide) |
| Anti-infective therapy / prophylaxis | antibiotics | Treat/prevent recurrent bacterial infection & sepsis | NCIT:C258 (Antibiotic) |
| Nutritional support | enteral/parenteral nutrition | Failure to thrive, malabsorption | NCIT:C15190 (Nutritional Support) |
| Skin barrier care | emollients, wound care | Barrier dysfunction | — |

- **Pharmacogenomics:** none disease-specific established.
- **Advanced therapeutics:** gene/cell/RNA therapies are conceptually attractive (monogenic recessive LOF) but **none are in trials** for NISBD1. Recombinant/topical EGFR-ligand supplementation (e.g., amphiregulin) is mechanistically rational and restored barrier function in ADAM17-deficient cells in vitro ([PMID: 42803585](https://pubmed.ncbi.nlm.nih.gov/42803585/)) but remains experimental.
- **Personalized approach:** genotype/functional-assay–guided; biologic selection targeting the dysregulated cytokines.

### 13. Prevention

- **Primary prevention:** not possible (genetic). **Genetic counseling** for consanguineous/affected families; **carrier testing** and **prenatal / preimplantation genetic diagnosis** where the familial ADAM17 variant is known.
- **Secondary prevention:** early genetic diagnosis (WGS-first) to shorten the diagnostic odyssey and start supportive care/biologics sooner ([PMID: 39381601](https://pubmed.ncbi.nlm.nih.gov/39381601/)).
- **Tertiary prevention:** aggressive infection prophylaxis, nutritional optimization, cardiac surveillance (given fatal myocarditis/cardiomyopathy risk), and skin-barrier management to prevent complications.
- **Immunization:** standard pediatric immunization is appropriate; no disease-specific vaccine.
- **Public-health/environmental interventions:** not applicable beyond infection control.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** Human ADAM17 (NCBI Gene 6868). Orthologs: mouse *Adam17* (NCBI Gene 11491); conserved across vertebrates (rat, zebrafish). High evolutionary conservation of the ADAM17–iRhom–EGFR axis.
- **Natural disease in other species:** No well-characterized spontaneous ADAM17-deficiency disease in companion animals is recorded in OMIA for NISBD1; knowledge is from engineered mouse models (Finding 5).
- **Comparative biology:** Adam17-null mice phenocopy EGFR/TGF-α deficiency (open-eye-at-birth, skin/epithelial defects), establishing cross-species conservation of the mechanism (Peschon 1998, [PMID: 9812885](https://pubmed.ncbi.nlm.nih.gov/9812885/)).
- **Zoonotic potential:** none (genetic disease).

### 15. Model Organisms

| Model | Type | Genetic strategy | Recapitulation | Key limitation | PMID |
|---|---|---|---|---|---|
| Adam17-null mouse | Mammalian, in vivo | Germline knockout | Epithelial/skin defects, phenocopy of EGFR/TGF-α loss | Perinatal/embryonic lethality limits adult study | [9812885](https://pubmed.ncbi.nlm.nih.gov/9812885/) |
| Tace/Sox9 conditional mouse | Mammalian, in vivo | Hair-follicle-SC conditional KO | Brittle hair, progressive alopecia, bulge-cell loss | Tissue-restricted; models hair arm only | [22696231](https://pubmed.ncbi.nlm.nih.gov/22696231/) |
| Intestinal/systemic Adam17 KO mouse | Mammalian, in vivo | Conditional/systemic KO | Severe DSS colitis, impaired EGFR-dependent epithelial protection | Chemically induced colitis, not spontaneous | [27077118](https://pubmed.ncbi.nlm.nih.gov/27077118/) |
| iRhom cub/toc mice | Mammalian, in vivo | iRhom2 gain/loss | ADAM17–amphiregulin–EGFR-dependent skin/hair phenotypes | Models cofactor axis, not ADAM17 LOF directly | [37282854](https://pubmed.ncbi.nlm.nih.gov/37282854/) |
| Adam10/17 double-KO MEFs | In vitro cellular | Double knockout fibroblasts | Shedding-assay platform to test human variants | No tissue architecture | [33953303](https://pubmed.ncbi.nlm.nih.gov/33953303/) |

These models collectively reproduce the skin-barrier, hair-follicle, and bowel-inflammation arms of NISBD1 and causally tie them to impaired EGFR-ligand shedding. **Resource databases:** MGI, IMPC, IMSR for the mouse alleles; Cellosaurus for the Adam10/17-DKO fibroblast line.

---

## Mechanistic Model / Interpretation

```
 Biallelic LOF ADAM17 variants (nonsense/frameshift/missense/deletion/splice)
                 │  [demonstrated]
                 ▼
     Loss of ADAM17 (TACE) sheddase activity at the plasma membrane
                 │  [demonstrated]
        ┌────────┴─────────────────────────────┐
        ▼                                        ▼
 Failure to shed EGFR ligands             Dysregulated TNF-α / cytokine
 (TGF-α, amphiregulin, HB-EGF)            processing (↓TNF-α shedding;
        │                                 ↑IL-1β, ↑IL-6; ↓T-cell TNF-α/IL-2)
        ▼                                        │
 Deficient EGFR (ErbB1) signaling               │
 (MAPK-ERK, PI3K-AKT)                            │
        │                                        │
   ┌────┴──────┐                                 │
   ▼           ▼                                 ▼
 SKIN/HAIR    GUT epithelium            Immune dysregulation +
 epithelial   (↓proliferation,          barrier breakdown
 failure      ↓mucus/goblet,                   │
   │           barrier loss)                    ▼
   ▼               ▼                     Recurrent bacterial
 Erythroderma,  Chronic diarrhea,        infection / sepsis
 collodion,     failure to thrive              │
 pustules,          │                          ▼
 atrichia,          └──────────►  Multi-organ: hepatitis,
 nail dystrophy                   hypertension, cardiomyopathy/
                                  myocarditis  →  EARLY MORTALITY
```

The decisive evidence that this chain is correct — rather than merely plausible — is the **NISBD1 (ADAM17-loss) ↔ NISBD2 (EGFR-loss) allelic series** (Finding 8): knocking out either the enzyme that makes the ligand or the receptor it activates produces near-identical neonatal skin + bowel + hair disease, and both are mirrored by the opposite (gain-of-function iRHOM2) disease TOC. Human genetics, mouse models, and structural biology thus triangulate on one axis.

---

## Evidence Base

| PMID | Study | Role in this report |
|---|---|---|
| [22010916](https://pubmed.ncbi.nlm.nih.gov/22010916/) | Blaydon 2011 (NEJM) | Founding paper: ADAM17 LOF causes NISBD1; cytokine data; cardiac mortality |
| [25804906](https://pubmed.ncbi.nlm.nih.gov/25804906/) | Bandsma 2015 | Second family (c.308dupA); multi-organ dysfunction; sepsis death |
| [33953303](https://pubmed.ncbi.nlm.nih.gov/33953303/) | Imoto 2021 | Compound-het missense LOF, functionally confirmed; ADAM17 >80 substrates |
| [34993966](https://pubmed.ncbi.nlm.nih.gov/34993966/) | Samuelov 2022 | Complex allele; anti-TNF + IL-12/23 + budesonide response |
| [40968583](https://pubmed.ncbi.nlm.nih.gov/40968583/) | Chang 2026 | Core phenotype spectrum definition |
| [42015567](https://pubmed.ncbi.nlm.nih.gov/42015567/) | Malhi 2026 | Atypical phenotype; expressivity; novel allele (p.Gln146Lys) |
| [9812885](https://pubmed.ncbi.nlm.nih.gov/9812885/) | Peschon 1998 (Science) | TACE-null mouse; ectodomain shedding essential; EGFR phenocopy |
| [18762209](https://pubmed.ncbi.nlm.nih.gov/18762209/) | Edwards 2008 | ADAM17 generates active EGFR ligands; epithelial development |
| [22696231](https://pubmed.ncbi.nlm.nih.gov/22696231/) | Nagao 2012 | Hair-follicle phenotype model |
| [27077118](https://pubmed.ncbi.nlm.nih.gov/27077118/) | Shimoda 2016 | Colitis/EGFR epithelial protection model |
| [37282854](https://pubmed.ncbi.nlm.nih.gov/37282854/) | Rabinowitsch 2023 | iRhom–ADAM17–amphiregulin–EGFR dependence |
| [38781971](https://pubmed.ncbi.nlm.nih.gov/38781971/) | Lu 2024 (cryo-EM) | iRhom2 controls ADAM17 maturation/activity |
| [40512800](https://pubmed.ncbi.nlm.nih.gov/40512800/) | Maciag 2025 (cryo-EM) | ADAM17–iRhom2 activation/inhibition structure |
| [24643277](https://pubmed.ncbi.nlm.nih.gov/24643277/) | Brooke 2014 | GOF iRHOM2/ADAM17 in TOC — mirror-image skin disease |
| [40040597](https://pubmed.ncbi.nlm.nih.gov/40040597/) | Karabinos 2025 | Defines NISBD2 (EGFR) counterpart |
| [9562519](https://pubmed.ncbi.nlm.nih.gov/9562519/) | Miettinen 1997 | EGFR-null epithelial/intestinal disease |
| [39381601](https://pubmed.ncbi.nlm.nih.gov/39381601/) | 2024 | WGS-first diagnosis of barrier/immune disorders |

**Evidence-type mix:** human clinical case reports/series (diagnosis, phenotype, treatment); in vitro functional assays (variant validation); mouse models (causal mechanism); cryo-EM structural biology (cofactor regulation). This multi-modal convergence makes the ADAM17→EGFR-ligand→EGFR model robust despite the tiny patient population.

---

## Limitations and Knowledge Gaps

1. **Extremely small sample:** <10 families worldwide; no cohort-level prevalence, incidence, penetrance, or natural-history statistics. All frequencies are qualitative.
2. **Phenotype–genotype correlation unresolved:** why some patients lack bowel disease, or develop cardiomyopathy/hepatitis, is unexplained; modifier genes (iRhom paralogs, EGFR-axis genes) are hypothesized but unproven in humans.
3. **Mechanism of extracutaneous/extraintestinal organ damage** (cardiac, hepatic, vascular) is observed but not mechanistically dissected; whether it is primary (ADAM17 loss in those tissues) or secondary (systemic inflammation/infection) is unclear.
4. **Treatment evidence is anecdotal:** the anti-TNF + IL-12/23 regimen rests on single-patient experience, not controlled trials; optimal regimen and durability are unknown.
5. **No curative or disease-modifying therapy**; gene/EGFR-ligand-replacement approaches are untested in patients.
6. **No validated QoL or outcome instruments** for this ultra-rare condition.

---

## Proposed Follow-up Experiments / Actions

1. **International patient registry & genotype–phenotype database** — pool the <10 known families to quantify penetrance, organ-involvement frequencies, mortality, and allele-specific severity.
2. **Standardized functional-assay pipeline** for all new ADAM17 variants (Adam10/17-DKO fibroblast shedding) to classify VUS and correlate residual activity with severity.
3. **Mechanistic study of cardiac/hepatic involvement** using tissue-specific Adam17 conditional mice to determine whether organ damage is cell-autonomous or inflammation-driven.
4. **Preclinical EGFR-ligand/pathway rescue** — test topical/recombinant amphiregulin or EGFR agonism for skin/gut barrier restoration (rationale: AREG rescued barrier in ADAM17-deficient epithelium in vitro, [PMID: 42803585](https://pubmed.ncbi.nlm.nih.gov/42803585/)).
5. **Prospective evaluation of biologic regimens** (anti-TNF ± IL-12/23, and alternatives) via an N-of-1/registry-embedded framework given rarity.
6. **Cascade carrier screening and reproductive counseling** (PGD/prenatal testing) offered systematically to consanguineous and affected families.
7. **Early-WGS diagnostic pathway** adoption to shorten the diagnostic odyssey and enable earlier supportive/biologic intervention.

---

*Report compiled from 8 confirmed findings across 33 reviewed papers. All quoted abstract text is verbatim from the cited PMIDs. Evidence types are distinguished throughout as human clinical, model organism, in vitro, or structural/computational.*


## Artifacts

- [OpenScientist final report](Inflammatory_Skin_And_Bowel_Disease_Neonatal_1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Inflammatory_Skin_And_Bowel_Disease_Neonatal_1-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 21 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0004421` (1 mention) - the report calls it "Systolic hypertension"; HP calls it **Elevated systolic blood pressure**
- `UBERON:0002107` (1 mention) - the report calls it "hepatitis"; UBERON calls it **liver**
- `UBERON:0000948` (1 mention) - the report calls it "cardiomyopathy/myocarditis"; UBERON calls it **heart**
- `NCIT:C2367` (1 mention) - the report calls it "TNF Inhibitor"; NCIT calls it **Triazene Derivative CB10-277**
- `NCIT:C1972` (1 mention) - the report calls it "Monoclonal Antibody"; NCIT calls it **Deferoxamine Hydrochloride**
- `NCIT:C1130` (1 mention) - the report calls it "Budesonide"; NCIT calls it **Hydroxyl Radical**
- `NCIT:C15190` (1 mention) - the report calls it "Nutritional Support"; NCIT calls it **Needle Biopsy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0008404` (1 mention) - the report calls it "Nail dysplasia"; HP calls it **Nail dystrophy**
- `HP:0200119` (1 mention) - the report calls it "Hepatitis"; HP calls it **Acute hepatitis**
- `UBERON:0002097` (1 mention) - the report calls it "Skin", "Primary organs:** **Skin"; UBERON calls it **skin of body**, and lists "skin organ" among its other names
- `GO:0005886` (1 mention) - the report calls it "Subcellular:** plasma membrane"; GO calls it **plasma membrane**, and lists "cellular membrane" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0002097` - called "Skin", "Primary organs:** **Skin"