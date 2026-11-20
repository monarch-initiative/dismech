---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-06T19:40:51.698071'
end_time: '2026-11-06T20:09:54.789421'
duration_seconds: 1743.09
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Multiple Self-Healing Squamous Epithelioma
  mondo_id: MONDO:0007566
  category: Mendelian
  causal_genes: TGFBR1
  omim_id: OMIM:132800
  synonyms: Ferguson-Smith syndrome; Ferguson-Smith disease; Ferguson-Smith tumor;
    Ferguson-Smith tumour; MSSE; familial primary self-healing squamous epithelioma
    of the skin, Ferguson-Smith type; multiple keratoacanthoma, Ferguson-Smith type;
    multiple self healing epithelioma of Ferguson-Smith
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
citation_count: 26
reference_validation:
  total_references: 26
  verified: 26
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 26
  on_topic: 15
  validator_version: 0.5.1
term_validation:
  total_terms: 30
  verified: 28
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 11
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0007566
    reported_labels:
    - MONDO
    ontology_label: multiple self-healing squamous epithelioma
  - term_id: HP:0000987
    reported_labels:
    - abnormal skin morphology
    ontology_label: Atypical scarring of skin
  - term_id: CHEBI:63631
    reported_labels:
    - acitretin
    ontology_label: topiramate
  - term_id: NCIT:C1878
    reported_labels:
    - Acitretin
    ontology_label: Darbepoetin Alfa
  - term_id: NCIT:C780
    reported_labels:
    - Triamcinolone
    ontology_label: Attenuated Corynebacterium Parvum
  labels_variant: 1
  unresolvable_prefixes:
  - Orphanet
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Multiple_Self-Healing_Squamous_Epithelioma-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Multiple_Self-Healing_Squamous_Epithelioma-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Multiple Self-Healing Squamous Epithelioma
- **MONDO ID:** MONDO:0007566 (if available)
- **Causal gene(s):** TGFBR1
- **OMIM:** OMIM:132800
- **Synonyms:** Ferguson-Smith syndrome; Ferguson-Smith disease; Ferguson-Smith tumor; Ferguson-Smith tumour; MSSE; familial primary self-healing squamous epithelioma of the skin, Ferguson-Smith type; multiple keratoacanthoma, Ferguson-Smith type; multiple self healing epithelioma of Ferguson-Smith
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Multiple Self-Healing Squamous Epithelioma** covering all of the
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

# Multiple Self-Healing Squamous Epithelioma (MSSE / Ferguson-Smith Disease): A Comprehensive Disease Characteristics Report

**Disease:** Multiple Self-Healing Squamous Epithelioma (MSSE)
**Causal gene:** **TGFBR1** (TGF-β receptor type 1)
**MONDO:** MONDO:0007566 · **OMIM:** 132800 · **Orphanet:** 65748 · **NCIT:** C4461 · **DOID:** 5585 · **UMLS:** C0546476 · **MeSH:** C536150 · **SNOMED CT:** 254659009 · **MedGen:** 154270
**Category:** Mendelian (autosomal dominant)

---

## Summary

Multiple Self-Healing Squamous Epithelioma (MSSE), also known as **Ferguson-Smith disease**, is a rare autosomal-dominant hereditary skin-cancer syndrome caused by germline **loss-of-function (LOF) variants in TGFBR1**, the gene encoding **transforming growth factor-β receptor type 1**. In this disease TGFBR1 behaves as a classic tumour-suppressor gene: affected individuals carry one defective germline allele, and tumours additionally show somatic loss of heterozygosity (LOH) with loss of the remaining wild-type allele. The hallmark of the disease is the recurrent eruption of multiple skin tumours that histologically resemble well-differentiated squamous cell carcinoma (SCC) / keratoacanthoma (KA): these grow rapidly over weeks, invade locally, and then **spontaneously regress** after several months, leaving deep, disfiguring facial scars and shallower limb scars. Lesions predominate on sun-exposed skin.

A central and scientifically interesting feature of TGFBR1 biology is that the same gene produces **two distinct allelic disorders**. MSSE results from **loss-of-function** variants (nonsense, frameshift, splice-site, and extracellular ligand-binding-domain missense changes), whereas **Loeys-Dietz syndrome (LDS)** — a connective-tissue/aortopathy disorder — results from **dominant-negative missense** variants in the serine/threonine kinase domain. The divergence is attributable to mutation nature and location, haploinsufficiency versus dominant-negative mechanisms, hypomorphicity, and modifier genes/environment. Haplotype studies further indicate MSSE has a **digenic/multilocus aetiology**, requiring a permissive second locus within a chromosome 9q22.3 haplotype adjacent to TGFBR1, which likely explains why some TGFBR1-LOF carriers develop MSSE while others (or those with kinase-domain missense variants) manifest LDS or overlapping phenotypes.

Mechanistically, loss of TGF-β/SMAD2/3 growth-suppressive signalling releases keratinocytes from cell-cycle control, predisposing sun-exposed skin to invasive KA/SCC-like tumours; the characteristic **spontaneous regression** is immune/inflammation-mediated, associated with a cytotoxic CD8+ T-lymphocyte response and an infiltrate rich in **plasmacytoid dendritic cells**, with apoptosis executed via Fas/Fas-ligand and granzyme-B/perforin pathways. Prognosis for survival is good (no cardiovascular risk, unlike LDS); morbidity derives from recurrent lesions and disfiguring scarring. Management uses oral **acitretin**, topical **5-fluorouracil**, intralesional **triamcinolone**, surgical excision, and (in aggressive cases) EGFR-targeted therapy — while **radiotherapy is strictly avoided** because it severely exacerbates the disease.

---

## 1. Disease Information

MSSE is a rare, inherited skin-cancer predisposition syndrome in which affected individuals develop multiple, recurrent, histologically malignant-appearing cutaneous tumours that undergo spontaneous regression ([PMID: 22533930](https://pubmed.ncbi.nlm.nih.gov/22533930/)). It was first described in Scottish families by Ferguson-Smith and is therefore eponymously named.

**Key identifiers (verified via Monarch/MONDO):**

| Resource | Identifier |
|----------|-----------|
| MONDO | MONDO:0007566 |
| OMIM (disease) | 132800 |
| Orphanet | 65748 |
| NCIT | C4461 |
| DOID | 5585 |
| UMLS | C0546476 |
| MeSH | C536150 |
| SNOMED CT | 254659009 |
| MedGen | 154270 |
| Gene (TGFBR1) | HGNC:11772; Ensembl ENSG00000106799; OMIM 190181; chr9:99,104,038–99,154,192 (GRCh38); cytoband 9q22.33 |

**Synonyms:** Ferguson-Smith syndrome / disease / tumour; MSSE; familial primary self-healing squamous epithelioma of the skin, Ferguson-Smith type; multiple keratoacanthoma, Ferguson-Smith type; multiple self-healing epithelioma of Ferguson-Smith.

**Information source:** Information is derived almost entirely from **aggregated disease-level resources** — OMIM, Orphanet, and primary literature based on a small worldwide set of affected families (18 families / 67 individuals in the defining mutation study) — rather than from large EHR/population datasets, reflecting the condition's ultra-rarity.

---

## 2. Etiology

**Primary cause — genetic.** MSSE is caused by germline **loss-of-function monoallelic mutations in TGFBR1** acting as a tumour-suppressor gene. High-throughput sequencing of the chromosome 9 disease locus followed by dideoxy sequencing identified **11 distinct monoallelic TGFBR1 mutations in 18 affected families**, firmly establishing TGFBR1 as causative ([PMID: 21358634](https://pubmed.ncbi.nlm.nih.gov/21358634/)). The variant spectrum — mutations in the extracellular ligand-binding domain plus a series of truncating mutations in the kinase domain — indicates a clear genotype–phenotype correlation with loss of function.

> *"Subsequent dideoxy sequencing of TGFBR1 identified 11 distinct monoallelic mutations in 18 affected families, firmly establishing TGFBR1 as the causative gene."* — [PMID: 21358634](https://pubmed.ncbi.nlm.nih.gov/21358634/)

**Two-hit tumour-suppressor mechanism.** Molecular analysis of MSSE tumours demonstrated **loss of heterozygosity of the MSSE region with loss of the normal allele**, the first evidence that MSSE acts as a tumour suppressor ([PMID: 16170343](https://pubmed.ncbi.nlm.nih.gov/16170343/)).

> *"We also report the first molecular analysis of MSSE tumours showing loss of heterozygosity of the MSSE region, with loss of the normal allele, providing the first evidence that MSSE is a tumour suppressor gene."* — [PMID: 16170343](https://pubmed.ncbi.nlm.nih.gov/16170343/)

**Genetic risk factors / digenic aetiology.** TGFBR1 was initially *excluded* because it lies outside the extensive chromosome 9 haplotype shared by Scottish families; evidence now supports a **digenic/multilocus model** requiring a second linked locus within the chr9q22.3 Scottish haplotype adjacent to TGFBR1 ([PMID: 24747516](https://pubmed.ncbi.nlm.nih.gov/24747516/); [PMID: 23358096](https://pubmed.ncbi.nlm.nih.gov/23358096/); [PMID: 33256177](https://pubmed.ncbi.nlm.nih.gov/33256177/)).

> *"MSSE can now be regarded as a digenic/multilocus disease in view of the evidence of a second linked locus necessary for pathogenesis located within the Scottish haplotype."* — [PMID: 24747516](https://pubmed.ncbi.nlm.nih.gov/24747516/)

**Environmental risk factors.** Lesions predominate on sun-exposed skin (face, limbs), implicating **ultraviolet (UV) radiation**. Because MSSE lesions are keratoacanthomas, the broader KA risk factors apply: UV exposure, chemical carcinogens, chemical peels, trauma, thermal burns, scarring skin conditions, and immunosuppression ([PMID: 16683389](https://pubmed.ncbi.nlm.nih.gov/16683389/)).

> *"In addition to ultraviolet exposure, KAs have also been associated with chemical carcinogens, chemical peels, genetic factors, chronic skin conditions that produce scarring, trauma and thermal burns."* — [PMID: 16683389](https://pubmed.ncbi.nlm.nih.gov/16683389/)

**Gene–environment interactions.** **Radiotherapy** provokes severe exacerbation with eruptive new SCCs/KAs ([PMID: 19874360](https://pubmed.ncbi.nlm.nih.gov/19874360/); [PMID: 28101021](https://pubmed.ncbi.nlm.nih.gov/28101021/)), and MSSE has arisen in a patient under systemic immunosuppression for rheumatoid arthritis ([PMID: 37625788](https://pubmed.ncbi.nlm.nih.gov/37625788/)) — both demonstrating that environmental/iatrogenic factors interact with the germline TGFBR1 defect to modulate lesion burden.

**Protective factors.** No specific genetic or dietary protective factors are established for MSSE. By inference, **sun protection** and **avoidance of radiotherapy and skin trauma** reduce lesion induction. No protective modifier alleles have been reported.

---

## 3. Phenotypes

The defining phenotype is **self-healing squamous epithelioma** (HPO canonical term **HP:0034720**). Lesions are **clinical signs / physical manifestations**: multiple tumours resembling crateriform squamous carcinomas that are locally invasive but regress spontaneously after several months, leaving deep disfiguring facial scars and shallower limb scars ([PMID: 24747516](https://pubmed.ncbi.nlm.nih.gov/24747516/)).

> *"multiple tumours resembling crateriform squamous carcinomas are locally invasive but regress spontaneously after several months, leaving deep disfiguring facial scars and shallower scars on the limbs"* — [PMID: 24747516](https://pubmed.ncbi.nlm.nih.gov/24747516/)

| Phenotype | HPO term | Type | Onset | Severity / course | Frequency |
|-----------|----------|------|-------|-------------------|-----------|
| Self-healing squamous epithelioma (KA/SCC-like tumours) | HP:0034720 | Clinical sign / neoplasm | Variable: adolescence → late adulthood (7th decade cases reported) | Rapid growth (weeks) → local invasion → spontaneous regression (months); episodic/recurrent | Defining feature (≈100%) |
| Facial scarring (disfiguring) | HP:0000987 (abnormal skin morphology) | Physical manifestation | Follows lesion regression | Deep, disfiguring; progressive scar accumulation | High |
| Limb/extremity tumours & scars | — | Physical manifestation | Variable | Shallower scars | Common |
| Predilection for sun-exposed sites | — | Distribution feature | — | — | Characteristic |

**Age of onset** is variable and age-dependent in expressivity; a confirmed late-onset case presented in a woman in her 60s ([PMID: 28101021](https://pubmed.ncbi.nlm.nih.gov/28101021/)).

> *"We report the case of a woman in her 60s with confirmed multiple self-healing squamous epitheliomas (MSSE) Ferguson-Smith."* — [PMID: 28101021](https://pubmed.ncbi.nlm.nih.gov/28101021/)

**Quality-of-life impact:** The principal burden is cosmetic and psychosocial — **recurrent disfiguring facial scarring** — rather than mortality. Lesions can occasionally ulcerate and behave aggressively, requiring surgery and reconstruction ([PMID: 38541097](https://pubmed.ncbi.nlm.nih.gov/38541097/)).

**Note on allelic overlap:** Several HPO terms annotated to the OMIM/MONDO entry — Arterial tortuosity (HP:0005116), Ascending tubular aorta aneurysm (HP:0004970), Talipes equinovarus (HP:0001762), Bifid uvula (HP:0000193), Hypertelorism (HP:0000316) — reflect **allelic Loeys-Dietz overlap** rather than classic MSSE features and should not be attributed to typical MSSE.

---

## 4. Genetic / Molecular Information

**Causal gene:** **TGFBR1** (HGNC:11772; gene OMIM 190181; Ensembl ENSG00000106799; chr9q22.33).

**Pathogenic variants.** MSSE alleles are **germline, private (family-specific) mutations**: nonsense, frameshift, splice-site, and extracellular ligand-binding-domain missense changes, all producing **loss of function** ([PMID: 21358634](https://pubmed.ncbi.nlm.nih.gov/21358634/)).

> *"The nature of the sequence variants, which include mutations in the extracellular ligand-binding domain and a series of truncating mutations in the kinase domain, indicates a clear genotype-phenotype correlation between loss-of-function TGFBR1 mutations and MSSE."* — [PMID: 21358634](https://pubmed.ncbi.nlm.nih.gov/21358634/)

**Allelic disorder contrast (MSSE vs LDS):**

| Feature | MSSE | Loeys-Dietz syndrome (LDS) |
|---------|------|-----------------------------|
| Variant class | Nonsense, frameshift, splice-site, extracellular-domain missense | Kinase (STK)-domain missense |
| Mechanism | Loss of function / haploinsufficiency | Dominant-negative |
| System | Skin (tumour suppressor) | Connective tissue / aorta |
| Cardiovascular risk | None | Aortic aneurysm/dissection |

> *"Conversely, nonsense, frameshift, or specific missense changes in the ligand-binding extracellular domain cause multiple self-healing squamous epithelioma (MSSE) lacking the cardiovascular phenotype."* — [PMID: 36599937](https://pubmed.ncbi.nlm.nih.gov/36599937/)

Functional splicing assays confirm the mechanism: an MSSE intron-4 splice variant (c.806-2A>C) produces an out-of-frame/truncating transcript (p.Asn270Thrfs*8 → LOF), whereas a comparable LDS variant yields in-frame dominant-negative products ([PMID: 29706644](https://pubmed.ncbi.nlm.nih.gov/29706644/)).

> *"Our results support the previously proposed but not yet approved mechanism that dominant-negative and truncating variants in STK domain induce LDS and MSSE, respectively."* — [PMID: 29706644](https://pubmed.ncbi.nlm.nih.gov/29706644/)

Rare patients carrying **kinase-domain missense** variants display **overlapping MSSE + LDS** features (e.g., p.Gly222Arg; [PMID: 30513140](https://pubmed.ncbi.nlm.nih.gov/30513140/), [PMID: 38112607](https://pubmed.ncbi.nlm.nih.gov/38112607/), [PMID: 39933850](https://pubmed.ncbi.nlm.nih.gov/39933850/)). A broad review attributes phenotypic divergence to mutation nature/location, hypomorphicity, haploinsufficiency vs dominant-negative effects, and modifier genes/environment ([PMID: 40612107](https://pubmed.ncbi.nlm.nih.gov/40612107/)).

> *"Multiple Self-healing Squamous Epithelioma (MSSE), a rare familial skin cancer, is linked to mutations in these genes."* — [PMID: 40612107](https://pubmed.ncbi.nlm.nih.gov/40612107/)

**Constraint metrics (gnomAD v4, GRCh38).** TGFBR1 is **intolerant to loss-of-function and missense variation**, concordant with the MSSE LOF mechanism: pLI = 0.91; LOEUF = 0.53 (observed/expected LoF = 20/55.1; oe_lof = 0.36); LoF Z = 4.01; missense Z = 3.99.

**Somatic vs germline.** The causal variant is **germline**; tumours acquire a **somatic second hit (LOH)** removing the wild-type allele ([PMID: 16170343](https://pubmed.ncbi.nlm.nih.gov/16170343/)).

**Allele frequency.** MSSE alleles are absent from population databases (private family mutations), supporting ACMG criterion PM2 (absence from gnomAD) alongside PVS1 for null variants.

**ClinVar.** NCBI ClinVar (queried Nov 2026) holds ~1,306 TGFBR1 variant records (~594 pathogenic), of which ~50–81 are explicitly annotated to "multiple self-healing squamous epithelioma," supporting single-gene diagnostic testing (finding F015). Variant classification follows ACMG via LOF criteria (PVS1 for null variants + PM2 for absence from gnomAD).

**Modifier genes / chromosomal abnormalities.** A permissive **second locus within chr9q22.3** acts as a modifier/necessary co-factor ([PMID: 24747516](https://pubmed.ncbi.nlm.nih.gov/24747516/); [PMID: 23358096](https://pubmed.ncbi.nlm.nih.gov/23358096/)). No recurrent large-scale aneuploidies or translocations are reported. No MSSE-specific epigenetic signature has been characterized.

---

## 5. Environmental Information

- **Environmental factors:** UV radiation (sun-exposed predilection), chemical carcinogens, chemical peels, trauma, thermal burns, and scarring skin conditions — all recognized KA inducers ([PMID: 16683389](https://pubmed.ncbi.nlm.nih.gov/16683389/)).
- **Iatrogenic:** **Radiotherapy** strongly exacerbates MSSE, causing extensive eruptive mid-facial SCCs/KAs ([PMID: 19874360](https://pubmed.ncbi.nlm.nih.gov/19874360/)).

> *"extensive, eruptive mid-facial squamous cell carcinomas (SCCs) and keratoacanthomas (KAs) consequent to radiotherapy"* — [PMID: 19874360](https://pubmed.ncbi.nlm.nih.gov/19874360/)

- **Immune status:** Immunosuppression (post-transplant, and a reported RA immunosuppression case) promotes KA/MSSE lesions ([PMID: 16683389](https://pubmed.ncbi.nlm.nih.gov/16683389/); [PMID: 37625788](https://pubmed.ncbi.nlm.nih.gov/37625788/)).

> *"Immunosuppressed patients, especially after transplantation, also develop KAs."* — [PMID: 16683389](https://pubmed.ncbi.nlm.nih.gov/16683389/)

- **Infectious agents:** Not an established cause of MSSE. (HPV is linked to some sporadic KAs but is not implicated in germline MSSE.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A **germline loss-of-function TGFBR1 variant** (nonsense/frameshift/splice-site/extracellular-domain missense) **reduces functional TGF-β type I receptor** → TGFBR1 haploinsufficiency (demonstrated: LOF spectrum, gnomAD constraint).
2. In a skin keratinocyte, a **somatic second hit (LOH)** removes the wild-type TGFBR1 allele → **complete loss of TGF-β receptor signalling** in that clone (demonstrated: tumour LOH, [PMID: 16170343](https://pubmed.ncbi.nlm.nih.gov/16170343/)).
3. Loss of receptor signalling **abolishes TGF-β/SMAD2/3 activation** → loss of SMAD-driven induction of cell-cycle inhibitors (p21^WAF1^, p12^CDK2-AP1^) (demonstrated in keratinocytes, [PMID: 17217620](https://pubmed.ncbi.nlm.nih.gov/17217620/)).
4. Loss of growth suppression **releases keratinocytes from cell-cycle control** → clonal proliferation, invasion (inferred for MSSE; supported by cSCC data, [PMID: 29581863](https://pubmed.ncbi.nlm.nih.gov/29581863/)).
5. On **sun-exposed skin (UV co-factor)** this yields a rapidly growing, locally invasive **keratoacanthoma/SCC-like tumour** (demonstrated clinically, [PMID: 24747516](https://pubmed.ncbi.nlm.nih.gov/24747516/)).
6. **Branch — spontaneous regression:** the tumour triggers an **immune/inflammatory response** → infiltration by cytotoxic CD8+ T lymphocytes (with CD4+ helpers) and **plasmacytoid dendritic cells** → tumour-cell **apoptosis via Fas/FasL and granzyme-B/perforin** → spontaneous regression leaving a scar (demonstrated: pDC infiltrate in regressed MSSE KA, [PMID: 28101021](https://pubmed.ncbi.nlm.nih.gov/28101021/); CTL/granzyme-B mechanism in KA, [PMID: 16497444](https://pubmed.ncbi.nlm.nih.gov/16497444/)).

```
Germline TGFBR1 LOF (one allele)
        │ haploinsufficiency
        ▼
Somatic LOH (loss of wild-type allele in keratinocyte)
        │ complete loss of TGF-β receptor
        ▼
No SMAD2/3 activation ──► ↓ p21^WAF1^, ↓ p12^CDK2-AP1^
        │ loss of growth suppression       (+ UV co-factor)
        ▼
Keratoacanthoma / SCC-like tumour (rapid growth, local invasion)
        │
        ├──► Immune recognition: CD8+ CTL + pDC infiltrate
        │        │ Fas/FasL + granzyme-B/perforin apoptosis
        │        ▼
        │   SPONTANEOUS REGRESSION → disfiguring scar
        │
        └──► (iatrogenic branch) Radiotherapy → severe exacerbation, eruptive new lesions
```

### Molecular pathways and supporting detail

- **TGF-β/SMAD signalling (upstream driver).** TGF-β1 treatment of normal keratinocytes suppresses growth via upregulation of p-SMAD2, p12^CDK2-AP1^ and p21^WAF1^; these effects are lost in SCC lines with disrupted TGF-β–SMAD signalling ([PMID: 17217620](https://pubmed.ncbi.nlm.nih.gov/17217620/)). Inactivating mutations in TGF-β receptors are genetic drivers of sporadic and murine cSCC, and reduced SMAD2/3 activation independently predicts increased cSCC depth ([PMID: 29581863](https://pubmed.ncbi.nlm.nih.gov/29581863/)).

> *"Inactivating mutations in transforming growth factor beta (TGF-β) receptors have been identified amongst genetic drivers of sporadic tumours and murine models of cSCC, suggesting a tumour suppressor function for TGF-β in normal skin"* — [PMID: 29581863](https://pubmed.ncbi.nlm.nih.gov/29581863/)

> *"TGF-beta1 treatment of normal keratinocytes suppressed cell growth with upregulation of p-Smad2, p12(CDK2-AP1), and p21(WAF1) expression"* — [PMID: 17217620](https://pubmed.ncbi.nlm.nih.gov/17217620/)

- **Cellular processes:** cell-cycle dysregulation (loss of p21/p12 checkpoint induction), epithelial proliferation/invasion, and immune-mediated apoptosis during regression.
- **Immune involvement (downstream, regression):** cytotoxic CD8+ T-lymphocyte response with CD4+ helpers; plasmacytoid dendritic cell infiltrate; Fas/FasL and granzyme-B/perforin effector pathways ([PMID: 16497444](https://pubmed.ncbi.nlm.nih.gov/16497444/); [PMID: 28101021](https://pubmed.ncbi.nlm.nih.gov/28101021/)).

> *"the tumor regression is dependent mainly on the immune response mediated by cytotoxic T lymphocytes (CD8+), together with helper T cells (CD4+)"* — [PMID: 16497444](https://pubmed.ncbi.nlm.nih.gov/16497444/)

> *"revealed an increased inflammatory infiltrate with numerous plasmacytoid dendritic cells in the regressed KA in comparison to the mature one, speaking in favor of an inflammation-mediated regression process"* — [PMID: 28101021](https://pubmed.ncbi.nlm.nih.gov/28101021/)

**Suggested ontology terms:** GO:0007179 (transforming growth factor beta receptor signaling pathway); GO:0008285 (negative regulation of cell population proliferation); GO:0007049 (cell cycle); GO:0006915 (apoptotic process); GO:0006954 (inflammatory response). Cell types: CL:0000312 (keratinocyte); CL:0000784 (plasmacytoid dendritic cell); CL:0000625 (CD8-positive, alpha-beta T cell). Chemicals (CHEBI): CHEBI:63631 (acitretin), CHEBI:46345 (5-fluorouracil).

---

## 7. Anatomical Structures Affected

- **Organ level:** **Skin** is the sole primary organ affected (integumentary system). No secondary organ involvement in classic MSSE (cardiovascular involvement belongs to the allelic LDS phenotype, not MSSE).
- **Tissue/cell level:** **Epithelial tissue** — specifically the stratified squamous epidermis; the targeted cell population is the **keratinocyte** (CL:0000312). Desmoglein (Dsg1/Dsg3) staining is uniformly preserved throughout the non-keratinized layers of MSSE tumours — similar to actinic keratoacanthoma and distinct from invasive SCC ([PMID: 9705163](https://pubmed.ncbi.nlm.nih.gov/9705163/)).

> *"All eight tumors showed uniform pericellular Dsg staining throughout the nonkeratinized layers of the neoplastic epithelium. This pattern is entirely similar to that observed in actinic KA"* — [PMID: 9705163](https://pubmed.ncbi.nlm.nih.gov/9705163/)

- **Subcellular level:** TGFBR1 is a transmembrane receptor (plasma membrane, GO:0005886); SMAD effectors shuttle to the nucleus (GO:0005634).
- **Localization (UBERON):** skin of face (UBERON:0008200 head skin), skin of limb (UBERON:0002097 skin of body; limb skin), with **predilection for sun-exposed sites**. Distribution is typically **bilateral/multifocal** (multiple recurrent lesions), not strictly lateralized.

---

## 8. Temporal Development

- **Onset:** Variable and **age-dependent in expressivity** — reported from adolescence through late adulthood, including a confirmed presentation in the 7th decade ([PMID: 28101021](https://pubmed.ncbi.nlm.nih.gov/28101021/)). Onset of individual lesions is **acute/subacute** (rapid growth over weeks).
- **Progression:** Individual lesions follow a stereotyped **episodic course** — rapid growth → local invasion → spontaneous regression over several months — leaving a scar ([PMID: 24747516](https://pubmed.ncbi.nlm.nih.gov/24747516/)). The disease as a whole is **chronic and recurrent/lifelong**, with new crops of lesions and accumulating scars.
- **Remission patterns:** Spontaneous regression of each lesion is the defining pattern; treatment (acitretin, intralesional steroid) can accelerate/limit lesions.
- **Critical periods / caution:** **Radiotherapy** at any time can trigger severe eruptive exacerbation and should be avoided ([PMID: 19874360](https://pubmed.ncbi.nlm.nih.gov/19874360/); [PMID: 28101021](https://pubmed.ncbi.nlm.nih.gov/28101021/)).

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal dominant** ([PMID: 22533930](https://pubmed.ncbi.nlm.nih.gov/22533930/); [PMID: 21358634](https://pubmed.ncbi.nlm.nih.gov/21358634/)).

> *"Ferguson-Smith disease (MSSE) is an autosomal dominant inherited disease with multiple, recurrent, histologically malignant tumours that undergo spontaneous regression."* — [PMID: 22533930](https://pubmed.ncbi.nlm.nih.gov/22533930/)

- **Epidemiology:** **Ultra-rare.** The defining mutation study identified TGFBR1 mutations in only **18 families (67 individuals)** worldwide ([PMID: 21358634](https://pubmed.ncbi.nlm.nih.gov/21358634/); [PMID: 22758773](https://pubmed.ncbi.nlm.nih.gov/22758773/)). Precise prevalence/incidence are not established (Orphanet:65748).

> *"mutations of the TGFBR1 gene were demonstrated in 18 families (67 individuals) with Ferguson-Smith disease"* — [PMID: 22758773](https://pubmed.ncbi.nlm.nih.gov/22758773/)

- **Penetrance / expressivity:** High penetrance with **variable, age-dependent expressivity** (onset and lesion burden vary). A permissive **9q22.3 modifier locus** contributes to whether a TGFBR1-LOF carrier manifests MSSE (digenic model) ([PMID: 24747516](https://pubmed.ncbi.nlm.nih.gov/24747516/)).
- **Founder effects / population:** Originally described in **Scottish families** with a founder-like haplotype, but subsequently identified across **multiple ethnic groups with distinct at-risk haplotypes**, arguing against a single founder mutation and suggesting MSSE may be more common than originally thought ([PMID: 17554363](https://pubmed.ncbi.nlm.nih.gov/17554363/)).

> *"The haplotypes for polymorphic markers segregating with MSSE in non-Scottish and Scottish families differ, suggesting that MSSE is not caused by a founder mutation and might be more common than originally thought."* — [PMID: 17554363](https://pubmed.ncbi.nlm.nih.gov/17554363/)

- **Sex ratio / age distribution:** No strong sex predilection established; onset spans adolescence to late adulthood. Consanguinity is not a factor (dominant). Germline mosaicism and carrier frequency are not specifically characterized.

---

## 10. Diagnostics

- **Clinical diagnosis:** Recognition of multiple rapidly growing, crateriform, self-regressing squamous tumours on sun-exposed skin in a patient with a positive family history.
- **Histopathology / IHC:** Lesions resemble well-differentiated SCC/keratoacanthoma. **Desmoglein (Dsg) immunostaining is uniformly preserved**, matching actinic KA and distinguishing MSSE lesions from invasive SCC ([PMID: 9705163](https://pubmed.ncbi.nlm.nih.gov/9705163/)) — a useful adjunct, since routine histology cannot reliably separate KA from SCC ([PMID: 22758773](https://pubmed.ncbi.nlm.nih.gov/22758773/)).
- **Genetic testing:** **Single-gene testing of TGFBR1** is the confirmatory approach; WES/WGS or panels including TGFBR1 are alternatives. ClinVar holds curated MSSE-associated TGFBR1 records (germline, private, pathogenic LOF alleles) (finding F015). CMA/karyotyping/FISH/mtDNA/repeat-expansion testing are **not applicable** (single-gene LOF point mutations).
- **Differential diagnosis:** sporadic keratoacanthoma, invasive cutaneous SCC, multiple KA syndromes (e.g., Grzybowski, Witten-Zak), Muir-Torre syndrome, and the allelic **Loeys-Dietz syndrome** (distinguished by connective-tissue/aortic features and kinase-domain missense variants).
- **Omics / imaging / electrophysiology:** No disease-specific biomarker, imaging, or electrophysiology test; diagnosis is clinical + histological + molecular.
- **Screening:** Cascade genetic testing of at-risk relatives in known families; no population-level newborn/carrier screening (ultra-rare, dominant).

---

## 11. Outcome / Prognosis

- **Survival / mortality:** **Excellent survival.** Unlike the allelic LDS, MSSE carries **no cardiovascular risk**; lesions regress spontaneously and the disease is not life-threatening.
- **Morbidity / function:** Principal burden is **recurrent disfiguring scarring** (deep facial scars, shallower limb scars) and psychosocial impact ([PMID: 24747516](https://pubmed.ncbi.nlm.nih.gov/24747516/)). Occasional lesions ulcerate or behave aggressively, requiring excision and reconstruction ([PMID: 38541097](https://pubmed.ncbi.nlm.nih.gov/38541097/)).
- **Disease course:** Chronic, recurrent, lifelong with spontaneous per-lesion remission.
- **Prognostic factors:** Lesion frequency/burden and exposure to exacerbating factors (radiotherapy, immunosuppression, UV). No validated molecular prognostic biomarker beyond the causal genotype.

---

## 12. Treatment

No curative therapy exists; management controls lesion burden and treats aggressive lesions.

| Modality | Agent / approach | Evidence | NCIT suggestion |
|----------|------------------|----------|-----------------|
| Systemic retinoid | **Oral acitretin** (treatment of choice; e.g., 0.5 mg/kg/day) | [PMID: 19874360](https://pubmed.ncbi.nlm.nih.gov/19874360/); [PMID: 38541097](https://pubmed.ncbi.nlm.nih.gov/38541097/) | NCIT:C1878 (Acitretin) |
| Topical chemotherapy | **5-Fluorouracil 5%** (often with acitretin) | [PMID: 38541097](https://pubmed.ncbi.nlm.nih.gov/38541097/) | NCIT:C505 (Fluorouracil) |
| Intralesional corticosteroid | **Triamcinolone acetonide** (acts on proliferation phase; good for multiple lesions) | [PMID: 28101021](https://pubmed.ncbi.nlm.nih.gov/28101021/) | NCIT:C780 (Triamcinolone) |
| Surgery | Excision + plastic reconstruction for ulcerated/invasive lesions | [PMID: 38541097](https://pubmed.ncbi.nlm.nih.gov/38541097/) | NCIT:C15329 (Surgical Procedure) |
| EGFR-targeted + chemo | **Cetuximab + cisplatin** for multiple aggressive KAs | [PMID: 33871373](https://pubmed.ncbi.nlm.nih.gov/33871373/) | NCIT:C1723 (Cetuximab); NCIT:C376 (Cisplatin) |
| **Avoid** | **Radiotherapy** — severe exacerbation | [PMID: 19874360](https://pubmed.ncbi.nlm.nih.gov/19874360/); [PMID: 28101021](https://pubmed.ncbi.nlm.nih.gov/28101021/) | — |

> *"We found oral acitretin to be the treatment of choice."* — [PMID: 19874360](https://pubmed.ncbi.nlm.nih.gov/19874360/)

> *"Multiple keratoacanthomas on her extremities were successfully treated with oral acitretin (0.5 mg/kg/day) in combination with topical Fluorouracil (5-FU) 5%, while excision and plastic surgery restoration were performed"* — [PMID: 38541097](https://pubmed.ncbi.nlm.nih.gov/38541097/)

> *"Intralesional triamcinolone acetate injection is a safe and easy to use method also effective for multiple lesions."* — [PMID: 28101021](https://pubmed.ncbi.nlm.nih.gov/28101021/)

**Pharmacogenomics / advanced therapeutics:** No gene/cell/RNA therapy exists for MSSE. Targeted anti-EGFR therapy is used empirically for aggressive lesions. No MSSE-specific registered clinical-trial programs (NCT) are established.

---

## 13. Prevention

- **Primary prevention:** No way to prevent the inherited mutation; **sun protection** and **avoidance of skin trauma, chemical peels, and radiotherapy** reduce lesion induction (inferred from KA risk factors, [PMID: 16683389](https://pubmed.ncbi.nlm.nih.gov/16683389/); radiotherapy caution, [PMID: 19874360](https://pubmed.ncbi.nlm.nih.gov/19874360/)).
- **Secondary prevention:** Regular dermatological surveillance for early identification/treatment of lesions; early retinoid therapy to limit crops.
- **Tertiary prevention:** Timely excision of ulcerated/aggressive lesions; careful management to minimize scarring.
- **Genetic counseling:** Autosomal-dominant counseling (50% offspring risk); cascade genetic testing of at-risk relatives; prenatal/preimplantation testing is theoretically possible given known family variants.
- **Immunization / public health / prophylaxis:** Not applicable (non-infectious Mendelian disease).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** MSSE is described in **humans** (NCBI Taxon 9606). No naturally occurring MSSE is documented in companion animals or wildlife (not in OMIA as a recognized natural homolog for this specific syndrome).
- **Orthologous gene:** *Tgfbr1* is highly conserved — mouse *Tgfbr1* (NCBI Gene 21812), rat *Tgfbr1* — enabling model-organism study.
- **Comparative biology / evolutionary conservation:** The TGF-β/SMAD tumour-suppressor axis is deeply conserved; its loss produces cutaneous SCC in mice (see Section 15), supporting conservation of the disease mechanism even where the exact human syndrome is not naturally reproduced.
- **Zoonotic potential:** None (non-infectious).

---

## 15. Model Organisms

No single model fully recapitulates MSSE (germline TGFBR1 LOF + 9q modifier + spontaneous regression). However, **mouse models of downstream TGF-β/SMAD effector loss** strongly support the tumour-suppressor mechanism:

| Model | Genotype | Phenotype | Evidence |
|-------|----------|-----------|----------|
| Epidermis-specific Smad4 KO | *Smad4^-/-^* keratinocytes | Spontaneous malignant cutaneous **SCC** (3–13 months); blocked TGF-β/BMP signalling, loss of p21, Pten inactivation, AKT/cyclin D1 activation | [PMID: 16170355](https://pubmed.ncbi.nlm.nih.gov/16170355/); [PMID: 18618014](https://pubmed.ncbi.nlm.nih.gov/18618014/) |
| Keratinocyte-specific Smad2 KO | *Smad2^-/-^* keratinocytes | Accelerated chemically-induced skin tumours; malignant progression with EMT via Snail | [PMID: 18618014](https://pubmed.ncbi.nlm.nih.gov/18618014/) |

> *"all MT mice developed spontaneous malignant skin tumors from 3 months to 13 months of age. The majority of tumors are malignant squamous cell carcinomas"* — [PMID: 16170355](https://pubmed.ncbi.nlm.nih.gov/16170355/)

> *"Smad4-/- mouse epidermis develops spontaneous skin squamous cell carcinomas (SCCs)"* — [PMID: 18618014](https://pubmed.ncbi.nlm.nih.gov/18618014/)

**Recapitulation & limitations:** These models confirm that disrupting the TGF-β/SMAD axis in keratinocytes is sufficient to cause cutaneous SCC — validating the upstream mechanism — but they **do not reproduce the self-healing/spontaneous-regression phenotype** or the digenic 9q modifier requirement central to human MSSE. **Resources:** MGI (mouse), RGD (rat). In-vitro keratinocyte and SCC cell-line models demonstrate the TGF-β1 → p-SMAD2 → p21/p12 growth-suppression axis ([PMID: 17217620](https://pubmed.ncbi.nlm.nih.gov/17217620/)).

---

## Mechanistic Model / Interpretation

MSSE is best understood as a **two-hit tumour-suppressor disease with an immune "brake" that forces regression**. The germline LOF TGFBR1 allele primes keratinocytes; a somatic second hit (LOH) in sun-exposed skin eliminates residual TGF-β signalling, releasing SMAD2/3-dependent cell-cycle control (↓p21, ↓p12) and allowing a rapidly growing, locally invasive KA/SCC-like tumour. Crucially, these tumours retain features of keratoacanthoma (preserved desmoglein, well-differentiated histology) and are **highly immunogenic**, so a cytotoxic CD8+ T-cell / plasmacytoid-dendritic-cell response drives Fas/FasL- and granzyme-B-mediated apoptosis and spontaneous regression — leaving a scar. The genotype–phenotype logic is the report's most elegant insight: **the same gene causes two opposite-system diseases** depending on variant mechanism (LOF/haploinsufficiency → skin tumours in MSSE; dominant-negative kinase-domain missense → connective-tissue/aortopathy in LDS), modulated by a permissive 9q22.3 modifier locus and environment (UV, radiotherapy, immunosuppression).

---

## Evidence Base (key literature)

| PMID | Role |
|------|------|
| [21358634](https://pubmed.ncbi.nlm.nih.gov/21358634/) | **Landmark:** establishes TGFBR1 LOF mutation spectrum as causal in 18 families |
| [16170343](https://pubmed.ncbi.nlm.nih.gov/16170343/) | LOH with loss of wild-type allele → tumour-suppressor proof |
| [24747516](https://pubmed.ncbi.nlm.nih.gov/24747516/) | Digenic/multilocus model; clinical course; scarring |
| [17554363](https://pubmed.ncbi.nlm.nih.gov/17554363/) | Multiple ethnic groups; not a single founder mutation |
| [36599937](https://pubmed.ncbi.nlm.nih.gov/36599937/) / [29706644](https://pubmed.ncbi.nlm.nih.gov/29706644/) | MSSE (LOF) vs LDS (dominant-negative) genotype–phenotype |
| [40612107](https://pubmed.ncbi.nlm.nih.gov/40612107/) | Review: hypomorphicity, haploinsufficiency, modifiers |
| [29581863](https://pubmed.ncbi.nlm.nih.gov/29581863/) / [17217620](https://pubmed.ncbi.nlm.nih.gov/17217620/) | TGF-β/SMAD2/3 keratinocyte tumour suppression |
| [16170355](https://pubmed.ncbi.nlm.nih.gov/16170355/) / [18618014](https://pubmed.ncbi.nlm.nih.gov/18618014/) | Mouse Smad4/Smad2 KO → spontaneous cutaneous SCC |
| [28101021](https://pubmed.ncbi.nlm.nih.gov/28101021/) / [16497444](https://pubmed.ncbi.nlm.nih.gov/16497444/) | Immune-mediated regression (pDC; CTL/granzyme-B/Fas) |
| [9705163](https://pubmed.ncbi.nlm.nih.gov/9705163/) | Desmoglein IHC distinguishes MSSE/KA from SCC |
| [19874360](https://pubmed.ncbi.nlm.nih.gov/19874360/) / [38541097](https://pubmed.ncbi.nlm.nih.gov/38541097/) / [33871373](https://pubmed.ncbi.nlm.nih.gov/33871373/) | Treatment: acitretin, 5-FU, surgery, cetuximab; radiotherapy caution |
| [22533930](https://pubmed.ncbi.nlm.nih.gov/22533930/) / [22758773](https://pubmed.ncbi.nlm.nih.gov/22758773/) | AD inheritance; rarity (18 families / 67 individuals) |

---

## Limitations and Knowledge Gaps

- **Ultra-rarity:** Evidence derives from ~18 families; no formal prevalence/incidence, penetrance quantification, or sex-ratio data exist.
- **Unidentified second locus:** The digenic 9q22.3 modifier gene is inferred from haplotype data but **not molecularly identified**.
- **Regression mechanism:** Immune-mediated regression in MSSE is supported by a single detailed case (pDC infiltrate) plus KA analogy; the precise trigger and the role of restored vs residual TGF-β signalling remain uncharacterized.
- **No faithful animal model:** Existing mouse models capture SCC formation from TGF-β/SMAD loss but not the self-healing phenotype or 9q modifier.
- **No omics datasets:** No MSSE-specific transcriptomic/proteomic/metabolomic/epigenomic signatures are published.
- **Genotype–phenotype overlap:** Kinase-domain missense cases blur the MSSE/LDS boundary, complicating counseling.

---

## Proposed Follow-up Experiments / Actions

1. **Identify the chr9q22.3 modifier locus** via deep sequencing and functional dissection of the at-risk haplotype shared by MSSE families, to explain MSSE-vs-LDS divergence.
2. **Single-cell / spatial transcriptomics of matched growing vs regressing MSSE lesions** to define the immune regression program (pDC, CD8+ CTL states, interferon signatures) and identify immunomodulatory therapeutic targets.
3. **Build a faithful mouse model** combining epidermal *Tgfbr1* haploinsufficiency with the candidate 9q modifier and UV exposure to recapitulate self-healing tumours.
4. **Systematic ClinVar/HGMD variant curation** of MSSE vs LDS alleles with functional (splicing/receptor-signalling) assays to refine ACMG classification and genotype–phenotype rules.
5. **Prospective registry** across the known families to quantify prevalence, penetrance, onset distribution, lesion burden, and treatment response (acitretin, 5-FU, intralesional steroid, cetuximab).
6. **Formalize management guidance** emphasizing sun protection and an explicit contraindication to radiotherapy.

---

*Evidence source types: predominantly human clinical/genetic (case series, family linkage, ClinVar) and in-vitro keratinocyte/SCC studies; mechanistic support from mouse model organism studies; computational constraint metrics from gnomAD.*


## Artifacts

- [OpenScientist final report](Multiple_Self-Healing_Squamous_Epithelioma-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Multiple_Self-Healing_Squamous_Epithelioma-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 26 |
| On topic | 15 |
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
| Terms whose name was checked | 17 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0007566` (2 mentions) - the report calls it "MONDO"; MONDO calls it **multiple self-healing squamous epithelioma**
- `HP:0000987` (1 mention) - the report calls it "abnormal skin morphology"; HP calls it **Atypical scarring of skin**
- `CHEBI:63631` (1 mention) - the report calls it "acitretin"; CHEBI calls it **topiramate**
- `NCIT:C1878` (1 mention) - the report calls it "Acitretin"; NCIT calls it **Darbepoetin Alfa**
- `NCIT:C780` (1 mention) - the report calls it "Triamcinolone"; NCIT calls it **Attenuated Corynebacterium Parvum**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0034720` (2 mentions) - the report calls it "Self-healing squamous epithelioma (KA/SCC-like tumours)"; HP calls it **Self-healing squamous epithelioma**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Orphanet`.