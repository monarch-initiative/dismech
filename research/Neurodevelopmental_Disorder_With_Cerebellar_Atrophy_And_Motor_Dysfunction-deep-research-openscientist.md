---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-22T16:26:23.647839'
end_time: '2026-10-22T16:40:43.763846'
duration_seconds: 860.12
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Neurodevelopmental Disorder With Cerebellar Atrophy And Motor Dysfunction
  mondo_id: MONDO:0859152
  category: Mendelian
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: NEDCAM; GEMIN5-related neurodevelopmental disorder; GEMIN5 disorder
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
citation_count: 11
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 12
  validator_version: 0.3.0
term_validation:
  total_terms: 26
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 19
  labels_matching: 9
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0859152
    reported_labels:
    - MONDO
    ontology_label: neurodevelopmental disorder with cerebellar atrophy and motor
      dysfunction
  - term_id: DOID:0070443
    reported_labels:
    - DOID
    ontology_label: neurodevelopmental disorder with cerebellar atrophy and motor
      dysfunction
  - term_id: GO:0097504
    reported_labels:
    - Subcellular:** cytoplasm and nuclear gems
    ontology_label: Gemini of Cajal bodies
  - term_id: UBERON:0002037
    reported_labels:
    - cerebellum
    - Primary organ:** brain, specifically the **cerebellum
    ontology_label: cerebellum
  labels_variant: 6
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Neurodevelopmental_Disorder_With_Cerebellar_Atrophy_And_Motor_Dysfunction-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Neurodevelopmental_Disorder_With_Cerebellar_Atrophy_And_Motor_Dysfunction-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder With Cerebellar Atrophy And Motor Dysfunction
- **MONDO ID:** MONDO:0859152 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** NEDCAM; GEMIN5-related neurodevelopmental disorder; GEMIN5 disorder
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder With Cerebellar Atrophy And Motor Dysfunction** covering all of the
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

# Neurodevelopmental Disorder With Cerebellar Atrophy And Motor Dysfunction (NEDCAM): A Comprehensive Disease Characterization

**MONDO:** MONDO:0859152 · **OMIM:** #619333 · **Causal gene:** *GEMIN5* (HGNC:20043, 5q33.2)

---

## Summary

**Neurodevelopmental Disorder with Cerebellar Atrophy and Motor Dysfunction (NEDCAM)** is a rare, autosomal-recessive Mendelian neurodevelopmental disease caused by **biallelic loss-of-function variants in *GEMIN5*** (gem nuclear organelle associated protein 5; HGNC:20043; NCBI Gene 25929; Ensembl ENSG00000082516; UniProt Q8TEQ6; cytoband 5q33.2; gene OMIM *607005). Despite the serial, gene-agnostic disease name, the causal gene is unambiguously *GEMIN5*, the largest subunit of the Survival Motor Neuron (SMN) complex and the snRNA-recognition factor that initiates spliceosomal small nuclear ribonucleoprotein (snRNP) assembly. The disorder was first delineated as a distinct entity in 2021 when two groups independently reported cohorts of affected individuals with biallelic *GEMIN5* variants ([PMID: 33963192](https://pubmed.ncbi.nlm.nih.gov/33963192/); [PMID: 34569062](https://pubmed.ncbi.nlm.nih.gov/34569062/)).

The core clinical triad consists of **global/motor developmental delay, infantile hypotonia, and cerebellar ataxia with cerebellar atrophy or hypoplasia on MRI**. In the 30-patient discovery cohort, motor delay, global developmental delay, and cerebellar atrophy were each present in essentially 100% of individuals, with near-universal speech delay (~96%) and hypotonia (~90%), and frequent ataxia (~70%). The phenotypic spectrum is broad: at one end it extends to early-infantile developmental and epileptic encephalopathy (EIDEE), and at the other to a late/advanced presentation in an elderly patient with progressive ataxia, spastic paraparesis, bulbar dysfunction, dementia, and combined frontotemporal plus cerebellar atrophy.

Mechanistically, pathogenic variants reduce GEMIN5 protein stability and abundance, impair dimerization through its central tetratricopeptide-repeat (TPR) domain, and disrupt both snRNP biogenesis and GEMIN5's independent translational regulatory functions — a coherent **loss-of-function** model supported by patient cells, iPSC-derived neurons, and *Drosophila*/zebrafish models. A particularly promising therapeutic lead has emerged: **SMN is a genetic modifier of GEMIN5-mediated neurodegeneration**, and raising SMN levels — via gene replacement or the antisense oligonucleotide nusinersen — upregulates endogenous GEMIN5 and rescues molecular deficits in disease models. No disease-specific therapy currently exists; management is supportive.

---

## Key Findings

### Finding 1 — NEDCAM is caused by biallelic loss-of-function variants in *GEMIN5*

The foundational discovery establishing NEDCAM as a Mendelian entity came from Kour et al. (2021), who identified **30 affected individuals from 22 unrelated families** carrying biallelic *GEMIN5* variants. As the authors state verbatim: *"Here, we have identified 30 affected individuals from 22 unrelated families presenting with developmental delay, hypotonia, and cerebellar ataxia harboring biallelic variants in the GEMIN5 gene"* ([PMID: 33963192](https://pubmed.ncbi.nlm.nih.gov/33963192/)). This single study established the gene, the autosomal-recessive inheritance pattern, and the core clinical phenotype.

The disease mechanism is **loss of function**. The same study demonstrated that *"Mutations in GEMIN5 perturb the subcellular distribution, stability, and expression of GEMIN5 protein and its interacting partners in patient iPSC-derived neurons, suggesting a potential loss-of-function mechanism"* ([PMID: 33963192](https://pubmed.ncbi.nlm.nih.gov/33963192/)). *GEMIN5* maps to chromosome 5q33.2 (transcript NM_015465), and the disorder is recorded as OMIM #619333.

### Finding 2 — GEMIN5 is a multidomain RNA-binding protein with distinct functional modules

GEMIN5's domain architecture is central to understanding how different variants cause disease. The protein comprises three principal functional regions:

| Region | Domain | Function |
|--------|--------|----------|
| N-terminus | WD40 repeats | Recognition and binding of small nuclear (sn)RNAs; initiates snRNP assembly |
| Middle | Extended TPR-like dimerization domain | Self-assembles into a canoe-shaped dimer; hub for protein–protein interactions |
| C-terminus | Non-canonical RNA-binding site (RBS1) | Translational regulation; binds SMN Tudor domain |

Moreno-Morcillo et al. (2020) solved the crystal structure of the dimerization domain: *"we solved the crystal structure of an extended tetratricopeptide (TPR)-like domain in human Gemin5 that self-assembles into a previously unknown canoe-shaped dimer"* ([PMID: 31799608](https://pubmed.ncbi.nlm.nih.gov/31799608/)). Reviews describe the N-terminal module's role: *"The protein is responsible for the recognition of small nuclear (sn)RNAs through its N-terminal region, and therefore for snRNP assembly"* ([PMID: 40176294](https://pubmed.ncbi.nlm.nih.gov/40176294/)). Beyond snRNP assembly, GEMIN5 independently **down-regulates global translation** while its C-terminal half promotes translation of its own mRNA and partitions mRNAs into polysomes ([PMID: 39819844](https://pubmed.ncbi.nlm.nih.gov/39819844/)).

### Finding 3 — The phenotypic spectrum spans from NEDCAM to epileptic encephalopathy and late-onset neurodegeneration

While the core NEDCAM phenotype is developmental/cognitive delay, infantile hypotonia, cerebellar ataxia, and cerebellar atrophy/hypoplasia, the spectrum is notably broad. Saida et al. (2021) independently confirmed that *"biallelic loss-of-function variants in GEMIN5 cause cerebellar atrophy/hypoplasia"* ([PMID: 34569062](https://pubmed.ncbi.nlm.nih.gov/34569062/)).

Zhang et al. (2024) expanded the spectrum to the severe epileptic end, reporting that *"the association between biallelic GEMIN5 variants and early-infantile developmental and epileptic encephalopathies (EIDEEs) has not been reported"* until their study, which also explored correlations between epilepsy and the sub-regional location of variants within the gene ([PMID: 38773790](https://pubmed.ncbi.nlm.nih.gov/38773790/)). At the opposite temporal extreme, an advanced/aged presentation has been documented in a 79-year-old woman with progressive ataxia, spastic paraparesis, contractures, bulbar dysfunction, dementia, and **striking frontotemporal atrophy in addition to cerebellar atrophy** ([PMID: 42800983](https://pubmed.ncbi.nlm.nih.gov/42800983/)), indicating a potentially progressive neurodegenerative trajectory in some individuals.

### Finding 4 — SMN upregulation is a leading candidate therapeutic strategy

The most actionable mechanistic insight is that **SMN acts as a genetic modifier of GEMIN5 disease**. Fortuna et al. (2023) reported: *"we identified SMN as a genetic suppressor of GEMIN5-mediated neurodegeneration in vivo"* ([PMID: 37369805](https://pubmed.ncbi.nlm.nih.gov/37369805/)). Critically for drug repurposing, they showed that *"an increase in SMN expression by either SMN gene therapy replacement or the antisense oligonucleotide (ASO), Nusinersen, significantly upregulated the endogenous levels of GEMIN5"* ([PMID: 37369805](https://pubmed.ncbi.nlm.nih.gov/37369805/)). SMN binds the C-terminus of GEMIN5 via its Tudor domain, and SMN upregulation ameliorated defective snRNP biogenesis and splicing defects in mammalian cells and in mutant GEMIN5-derived iPSC neurons. Because nusinersen and SMN gene replacement (onasemnogene abeparvovec) are already FDA-approved for spinal muscular atrophy, this represents a biologically-grounded repurposing opportunity.

### Finding 5 — Model organisms recapitulate GEMIN5 loss

Multiple cross-species models reproduce disease features, strengthening causal inference:

- **Drosophila:** Knockdown of *rigor mortis*, the fly homolog of *GEMIN5*, reproduces the motor phenotype — *"knock down of rigor mortis, the fly homolog of human GEMIN5, leads to developmental defects, motor dysfunction, and a reduced lifespan"* ([PMID: 33963192](https://pubmed.ncbi.nlm.nih.gov/33963192/)).
- **Zebrafish:** Models for null variants p.(Arg733Thrfs\*6) and p.(Ala1305Leufs\*14) *"exhibited complete lethality at 2 weeks and recapitulated a distinct dysplastic phenotype"* ([PMID: 34569062](https://pubmed.ncbi.nlm.nih.gov/34569062/)).
- **Human iPSC-derived neurons** from patients serve as a patient-specific in vitro model.

A dedicated review summarizes the current animal models of NEDCAM ([PMID: 38526274](https://pubmed.ncbi.nlm.nih.gov/38526274/)).

### Finding 6 — Pathogenic variants reduce protein stability and disrupt dimerization and snRNP assembly

The molecular consequence of pathogenic variants is reduced functional GEMIN5. Saida et al. (2021) demonstrated by Western blot in patient lymphoblastoid cells that *"Western blotting analysis using lymphoblastoid cell lines derived from both affected individuals showed significantly reduced levels of GEMIN5 protein"* ([PMID: 34569062](https://pubmed.ncbi.nlm.nih.gov/34569062/)). Francisco-Velilla et al. (2022) extended this, showing functional and structural deficiencies of disease-associated variants, with dimerization-defective variants exhibiting decreased protein levels and reduced ribosome association ([PMID: 35393353](https://pubmed.ncbi.nlm.nih.gov/35393353/)).

Reported variant types span the full loss-of-function spectrum:

| Variant class | Examples (cDNA / protein) |
|---------------|---------------------------|
| Frameshift | c.2196dupA p.Arg733Thrfs\*6; c.3913delG p.Ala1305Leufs\*14 |
| Nonsense | c.4496dupA p.Tyr1499\*; p.Leu508\* |
| Missense | c.1831G>A p.Val611Met; c.2705T>A p.Leu902Gln; c.2911C>G p.Gln971Glu |
| In-frame indel (TPR domain) | c.3162_3164del p.Asp1054_Ala1055delinsGlu |

The TPR-domain in-frame variant is illustrative: *"a novel homozygous 3bp-deletion NM_015465.5:c.3162_3164del that leads to the loss of NM_015465.5 (NP_056280.2):p.(Asp1054_Ala1055delinsGlu) amino acid in one of the α-helixes of the tetratricopeptide repeats"* ([PMID: 36980979](https://pubmed.ncbi.nlm.nih.gov/36980979/)). Inheritance is autosomal recessive (biallelic), with variants occurring compound heterozygous or homozygous (the latter frequently in consanguineous families).

### Finding 7 — Confirmed cross-reference identifiers

Database cross-references were verified via EBI OLS4 and mygene.info:

| Resource | Identifier |
|----------|-----------|
| MONDO | MONDO:0859152 |
| OMIM (disease) | #619333 |
| DOID | DOID:0070443 |
| MedGen | C5543427 |
| UMLS | C5543427 |
| Gene symbol | GEMIN5 (HGNC:20043) |
| NCBI Gene | 25929 |
| Ensembl | ENSG00000082516 |
| UniProt | Q8TEQ6 |
| Gene OMIM | *607005 |
| Cytoband | 5q33.2 |

Synonyms: **NEDCAM**, GEMIN5 disorder, GEMIN5-related neurodevelopmental disorder.

### Finding 8 — Quantified HPO phenotype frequencies

From HPO/OMIM:619333 annotations (derived from the Kour 2021 discovery cohort, n≈27–30):

| Phenotype | HPO term | Frequency |
|-----------|----------|-----------|
| Motor delay | HP:0001270 | 30/30 (100%) |
| Global developmental delay | HP:0001263 | 30/30 (100%) |
| Cerebellar atrophy | HP:0001272 | 30/30 (100%) |
| Delayed speech and language development | HP:0000750 | 26/27 (96%) |
| Hypotonia | HP:0001252 | 26/29 (90%) |
| Ataxia | HP:0001251 | 19/27 (70%) |
| Hyperreflexia (brisk reflexes) | HP:0001348 | 15/25 (60%) |
| Appendicular hypotonia | HP:0012389 | 13/29 (45%) |
| Inability to walk | HP:0002540 | 8/27 (30%) |
| Progressive course | HP:0003676 | 6/28 (21%) |
| Areflexia | HP:0001284 | 4/25 (16%) |

Onset: infantile 21/30 (70%), congenital 7/29 (24%), childhood 1/29. Inheritance: autosomal recessive (HP:0000007). ClinVar lists 411 *GEMIN5* submissions, including 92 pathogenic and 28 likely pathogenic.

---

## Full Report by Section

### 1. Disease Information

NEDCAM is a rare autosomal-recessive neurodevelopmental disorder characterized by the triad of developmental delay, cerebellar atrophy, and motor dysfunction. **Key identifiers:** MONDO:0859152; OMIM #619333; DOID:0070443; MedGen/UMLS C5543427. No dedicated Orphanet, ICD-10/ICD-11, or MeSH entry was confirmed in this investigation (it would fall under broad categories such as ICD-11 LD90 "developmental anomalies" or hereditary ataxia groupings). **Synonyms:** NEDCAM; GEMIN5 disorder; GEMIN5-related neurodevelopmental disorder. The information is derived from **aggregated disease-level resources and published patient cohorts** (OMIM, HPO, primary literature) rather than individual EHR data; the phenotype frequencies originate from the pooled discovery cohort of 30 patients.

### 2. Etiology

**Primary cause — genetic.** NEDCAM is a monogenic Mendelian disorder caused exclusively by **biallelic (autosomal-recessive) loss-of-function variants in *GEMIN5*** ([PMID: 33963192](https://pubmed.ncbi.nlm.nih.gov/33963192/)). There is no environmental, infectious, or multifactorial contribution to disease causation.

- **Genetic risk factors:** The causal variants themselves (see Section 4). No independent susceptibility loci or GWAS signals apply to this monogenic disorder.
- **Modifier genes:** *SMN1/SMN2* (SMN) is a confirmed modifier — SMN dosage suppresses GEMIN5-mediated neurodegeneration ([PMID: 37369805](https://pubmed.ncbi.nlm.nih.gov/37369805/)). Sub-regional variant location within *GEMIN5* may modify the likelihood of epilepsy ([PMID: 38773790](https://pubmed.ncbi.nlm.nih.gov/38773790/)).
- **Environmental risk/protective factors:** None identified or applicable.
- **Gene–environment interactions:** None reported.
- **Consanguinity** increases risk of homozygous variants and is a relevant demographic factor in affected families.

### 3. Phenotypes

The phenotype is dominated by neurological/neurodevelopmental features (see Finding 8 table for frequencies). All are **clinical signs/neurodevelopmental manifestations** rather than laboratory abnormalities (no consistent biochemical marker exists). Key features:

- **Motor/global developmental delay** (HP:0001270, HP:0001263) — ~100%, infantile onset, moderate-to-severe.
- **Cerebellar atrophy/hypoplasia** (HP:0001272) — ~100%, an imaging hallmark.
- **Delayed speech/language** (HP:0000750) — ~96%.
- **Hypotonia** (HP:0001252), often infantile, ~90%.
- **Cerebellar ataxia** (HP:0001251) — ~70%.
- **Hyperreflexia** (HP:0001348, ~60%) and, less often, **areflexia** (HP:0001284, ~16%), indicating variable upper/lower motor involvement.
- **Inability to walk** (HP:0002540) — ~30%.
- **Seizures/epileptic encephalopathy** at the severe end of the spectrum ([PMID: 38773790](https://pubmed.ncbi.nlm.nih.gov/38773790/)).
- **Advanced/late features:** spastic paraparesis, contractures, bulbar dysfunction, dementia, frontotemporal atrophy ([PMID: 42800983](https://pubmed.ncbi.nlm.nih.gov/42800983/)).

**Age of onset:** predominantly infantile (70%) to congenital (24%). **Severity:** variable, moderate to severe. **Progression:** mostly stable developmental delay, but ~21% show a progressive course, and late presentations suggest neurodegeneration. **Quality of life:** substantial impact — motor and cognitive disability, speech impairment, and (in a subset) non-ambulation profoundly affect daily functioning and independence.

### 4. Genetic / Molecular Information

**Causal gene:** *GEMIN5* (HGNC:20043; NCBI 25929; Ensembl ENSG00000082516; UniProt Q8TEQ6; gene OMIM *607005; 5q33.2; transcript NM_015465). **Inheritance:** autosomal recessive (biallelic; compound heterozygous or homozygous). **Variant classes:** frameshift, nonsense, missense, splice, and in-frame indels (see Finding 6 table). **Functional consequence:** loss of function via reduced protein stability/abundance and impaired dimerization, snRNP assembly, and translational regulation ([PMID: 34569062](https://pubmed.ncbi.nlm.nih.gov/34569062/); [PMID: 35393353](https://pubmed.ncbi.nlm.nih.gov/35393353/)). **ClinVar:** 411 submissions (92 pathogenic, 28 likely pathogenic). **Allele frequency:** individual pathogenic variants are rare in gnomAD, consistent with a rare recessive disorder. **Somatic vs germline:** germline. **Modifier genes:** SMN. **Epigenetic/chromosomal abnormalities:** none specifically implicated.

### 5. Environmental Information

Not applicable. NEDCAM is a purely genetic Mendelian disorder with no documented environmental, lifestyle, toxic, or infectious contributors.

### 6. Mechanism / Pathophysiology

**Causal chain (initiating lesion → clinical manifestation):**

1. Biallelic loss-of-function variant in *GEMIN5* → **leads to** reduced GEMIN5 protein stability, abundance, and altered subcellular distribution ([PMID: 33963192](https://pubmed.ncbi.nlm.nih.gov/33963192/); [PMID: 34569062](https://pubmed.ncbi.nlm.nih.gov/34569062/)).
2. Reduced/dysfunctional GEMIN5 → **impairs** dimerization (TPR domain) and snRNA recognition (WD40 domain) ([PMID: 31799608](https://pubmed.ncbi.nlm.nih.gov/31799608/); [PMID: 35393353](https://pubmed.ncbi.nlm.nih.gov/35393353/)).
3. Impaired snRNA delivery to the SMN complex → **results in** defective spliceosomal snRNP biogenesis → **causes** downstream splicing defects (inferred to perturb neuronal transcriptomes).
   - **Branch A:** Loss of GEMIN5 translational-regulatory function → dysregulated (de-repressed) global translation and altered polysome partitioning of mRNAs ([PMID: 39819844](https://pubmed.ncbi.nlm.nih.gov/39819844/)).
4. Combined snRNP and translational dysregulation → **leads to** impaired development/maintenance of neurons, with the cerebellum particularly vulnerable (inferred from the cerebellar-atrophy phenotype).
5. Cerebellar (and in severe/late cases, cortical/frontotemporal) neurodegeneration/hypoplasia → **produces** the clinical phenotype: developmental delay, hypotonia, ataxia, motor dysfunction, and — at the severe end — epileptic encephalopathy ([PMID: 38773790](https://pubmed.ncbi.nlm.nih.gov/38773790/)).

**Modifier branch:** Increasing SMN → upregulates endogenous GEMIN5 and rescues snRNP/splicing deficits → suppresses neurodegeneration ([PMID: 37369805](https://pubmed.ncbi.nlm.nih.gov/37369805/)).

```
GEMIN5 biallelic LoF variant
        │
        ▼
↓ GEMIN5 protein stability/level, mislocalization
        │
        ├──────────────► ↓ snRNA recognition (WD40) + ↓ dimerization (TPR)
        │                        │
        │                        ▼
        │                 defective snRNP assembly ──► splicing defects
        │
        └──────────────► loss of translational regulation ──► dysregulated translation
                                 │
                                 ▼
                     impaired neuronal development/maintenance
                                 │
                                 ▼
              cerebellar atrophy/hypoplasia (± cortical atrophy)
                                 │
                                 ▼
      developmental delay · hypotonia · ataxia · motor dysfunction
                      (± epileptic encephalopathy)

   [SMN ↑  ═══►  ↑ GEMIN5, rescued snRNP/splicing  ═══► suppressed neurodegeneration]
```

- **Molecular pathways/processes:** snRNP biogenesis (SMN complex), spliceosome assembly, translational control. **GO terms:** GO:0000387 (spliceosomal snRNP assembly), GO:0006412 (translation), GO:0006417 (regulation of translation).
- **Protein dysfunction:** reduced stability, impaired dimerization, loss of function.
- **Subcellular compartments:** cytoplasm (predominant) and nuclear gems; **GO:0005737** (cytoplasm), **GO:0097504** (Gemini of coiled bodies / gems).
- **Cell types:** neurons, particularly cerebellar neurons; **CL:0000540** (neuron), **CL:0000121** (Purkinje cell, inferred).

### 7. Anatomical Structures Affected

- **Primary organ:** brain, specifically the **cerebellum** (UBERON:0002037). Imaging shows cerebellar atrophy/hypoplasia (~100%).
- **Secondary:** cerebral cortex / frontotemporal lobes in advanced disease (UBERON:0000956).
- **Body system:** central nervous system (UBERON:0001017).
- **Tissue/cell level:** nervous tissue; neurons (CL:0000540), with cerebellar Purkinje/granule neurons implicated by the atrophy pattern.
- **Subcellular:** cytoplasm and nuclear gems (GO:0097504).
- **Lateralization:** bilateral, symmetric cerebellar involvement.

### 8. Temporal Development

**Onset:** predominantly **infantile** (70%) and **congenital** (24%), rarely childhood. **Onset pattern:** chronic/insidious developmental. **Progression:** developmental delay is often relatively stable, but ~21% display a progressive course; late-onset/advanced cases show frank progressive neurodegeneration (ataxia, spasticity, dementia, cortical atrophy) ([PMID: 42800983](https://pubmed.ncbi.nlm.nih.gov/42800983/)). **Course:** chronic, lifelong. **Critical period:** early infancy is the key window for developmental and potential therapeutic intervention.

### 9. Inheritance and Population

**Inheritance:** autosomal recessive (biallelic), HP:0000007. **Penetrance:** essentially complete for the core phenotype. **Expressivity:** highly variable (NEDCAM core → EIDEE → late neurodegeneration). **Epidemiology:** no formal prevalence/incidence has been established; the disorder is **ultra-rare**, with ~30+ reported families as of the discovery cohort. **Consanguinity** contributes homozygous cases. **Founder effects/carrier frequency:** not specifically established; individual pathogenic alleles are rare in gnomAD. **Sex ratio:** no strong sex bias reported (recessive). **Geographic distribution:** worldwide, drawn from 22 unrelated families across multiple populations.

### 10. Diagnostics

**Genetic testing is the diagnostic cornerstone.** Diagnosis is established by identifying biallelic pathogenic *GEMIN5* variants via **whole-exome or whole-genome sequencing** (WES/WGS), or multigene neurodevelopmental/ataxia panels that include *GEMIN5*. Single-gene testing or targeted variant confirmation is appropriate once a variant is identified; segregation/parental testing confirms biallelic (trans) configuration. **Imaging:** brain MRI is key, revealing cerebellar atrophy/hypoplasia (and frontotemporal atrophy in advanced cases) — a strong diagnostic clue ([PMID: 34569062](https://pubmed.ncbi.nlm.nih.gov/34569062/); [PMID: 42800983](https://pubmed.ncbi.nlm.nih.gov/42800983/)). **EEG** is indicated when seizures are present (EIDEE subset). Variant interpretation follows ACMG/AMP guidelines with ClinVar/ClinGen reference. **Differential diagnosis:** other recessive congenital/childhood cerebellar ataxias and hypoplasias (e.g., pontocerebellar hypoplasias, CACNA1A-related disorders, other SMN-complex/snRNP disorders), distinguished by the specific *GEMIN5* genotype and the characteristic motor-predominant delay with cerebellar atrophy. No specific biochemical biomarker exists; Western blot showing reduced GEMIN5 is a research-level confirmation ([PMID: 34569062](https://pubmed.ncbi.nlm.nih.gov/34569062/)).

### 11. Outcome / Prognosis

Prognosis is **chronic and lifelong** with significant neurodevelopmental disability. Core morbidity includes motor dysfunction, cognitive impairment, speech impairment, and non-ambulation in a subset (~30%). A minority show progressive deterioration; the elderly case demonstrates survival into the 8th decade but with accumulating neurodegenerative burden ([PMID: 42800983](https://pubmed.ncbi.nlm.nih.gov/42800983/)). The EIDEE subset carries the poorest prognosis owing to severe epilepsy. No formal survival statistics exist. **Prognostic factors** likely include variant type/location (epilepsy association) and residual GEMIN5 function. Quality of life is substantially reduced; no validated disease-specific QoL instrument has been reported.

### 12. Treatment

**No disease-specific or curative therapy currently exists; management is supportive.** Supportive/rehabilitative care includes physical therapy, occupational therapy, and speech therapy for motor and communication deficits; anti-seizure medications for the epileptic subset; and nutritional/feeding support for bulbar dysfunction. **Leading experimental strategy — SMN upregulation:** boosting SMN via SMN gene-replacement therapy or the antisense oligonucleotide **nusinersen** raises endogenous GEMIN5 and rescues molecular deficits in cells and iPSC neurons ([PMID: 37369805](https://pubmed.ncbi.nlm.nih.gov/37369805/)); both modalities are already approved for spinal muscular atrophy, making this a plausible repurposing candidate (**NCIT suggestion:** nusinersen; gene therapy). No pharmacogenomic, immunotherapeutic, or surgical interventions apply. No completed clinical trials specific to NEDCAM are reported.

### 13. Prevention

Prevention is **genetic and reproductive**, not population/behavioral. Options include **genetic counseling** for affected families (25% recurrence risk per pregnancy for carrier couples), **carrier/cascade screening** of relatives, **prenatal diagnosis**, and **preimplantation genetic testing (PGT-M)** once the familial variants are known. There is no primary/secondary public-health prevention, immunization, or lifestyle modification applicable to this monogenic disorder. Consanguinity counseling is relevant in affected populations.

### 14. Other Species / Natural Disease

No naturally occurring companion-animal or wildlife NEDCAM disease is documented in OMIA. **Orthologous/model genes:** *Drosophila melanogaster* **rigor mortis** (the fly *GEMIN5* homolog) and zebrafish *gemin5* are functional orthologs used in modeling (see Section 15). GEMIN5/SMN-complex function is **evolutionarily conserved** across metazoans, underpinning the validity of invertebrate and fish models. No zoonotic or cross-species transmission applies (non-infectious genetic disorder).

### 15. Model Organisms

| Model | Type | Phenotype recapitulation | Reference |
|-------|------|--------------------------|-----------|
| *Drosophila* (*rigor mortis* knockdown) | Invertebrate, genetic | Developmental defects, motor dysfunction, reduced lifespan — captures motor phenotype | [PMID: 33963192](https://pubmed.ncbi.nlm.nih.gov/33963192/) |
| Zebrafish (null variants p.Arg733Thrfs\*6, p.Ala1305Leufs\*14) | Vertebrate, genetic | Complete lethality at 2 weeks; distinct dysplastic phenotype — captures developmental severity | [PMID: 34569062](https://pubmed.ncbi.nlm.nih.gov/34569062/) |
| Patient iPSC-derived neurons | In vitro, human | Perturbed GEMIN5 distribution/stability, snRNP/splicing defects — captures cell-level molecular pathology | [PMID: 33963192](https://pubmed.ncbi.nlm.nih.gov/33963192/) |

**Available genetic model types:** knockdown (fly), null variant (zebrafish), and patient-derived iPSC neurons. **Limitations:** the zebrafish null causes complete lethality, limiting study of chronic/progressive phenotypes; invertebrate models cannot reproduce the human cerebellar-specific anatomy; iPSC neurons lack full tissue/circuit context. A dedicated review summarizes current NEDCAM models and future directions ([PMID: 38526274](https://pubmed.ncbi.nlm.nih.gov/38526274/)). **Resources:** MGI, ZFIN, FlyBase (rigor mortis), and patient iPSC lines.

---

## Mechanistic Model / Interpretation

NEDCAM is best understood as a **snRNP-biogenesis and translational-regulation deficiency disorder**. A single molecular lesion — reduced functional GEMIN5 — propagates along two convergent branches (defective snRNP assembly and dysregulated translation) to impair the development and maintenance of neurons, with the cerebellum being the most vulnerable structure. The breadth of the phenotypic spectrum (NEDCAM core ↔ EIDEE ↔ late frontotemporal/cerebellar neurodegeneration) is plausibly explained by **variant-specific residual function** and **sub-regional variant location**, modulated by SMN dosage. The SMN–GEMIN5 modifier relationship is the single most translationally important finding: it provides both a mechanistic bridge to the well-characterized SMA biology and a ready-made pharmacological toolkit (nusinersen, SMN gene replacement) for therapeutic testing.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|------|-----------------|---------------------|
| [33963192](https://pubmed.ncbi.nlm.nih.gov/33963192/) | *Loss of function mutations in GEMIN5 cause a neurodevelopmental disorder* | Foundational — gene, inheritance, cohort, LoF mechanism, fly model, HPO frequencies |
| [34569062](https://pubmed.ncbi.nlm.nih.gov/34569062/) | *Pathogenic variants in GEMIN5 cause cerebellar atrophy* | Independent confirmation; reduced protein (WB); zebrafish model |
| [31799608](https://pubmed.ncbi.nlm.nih.gov/31799608/) | *Structural basis for the dimerization of Gemin5* | TPR dimerization domain crystal structure |
| [40176294](https://pubmed.ncbi.nlm.nih.gov/40176294/) | *Understanding GEMIN5 Interactions* | WD40 snRNA recognition; selective translation |
| [39819844](https://pubmed.ncbi.nlm.nih.gov/39819844/) | *GEMIN5 and neurodevelopmental diseases* | Domain architecture; translational regulation; dimerization-defective variants |
| [38773790](https://pubmed.ncbi.nlm.nih.gov/38773790/) | *Expanding the clinical phenotype... EIDEE* | Spectrum expansion to epileptic encephalopathy; variant sub-region correlation |
| [42800983](https://pubmed.ncbi.nlm.nih.gov/42800983/) | *Advanced Presentation... in an Elderly Female* | Late/progressive phenotype; frontotemporal + cerebellar atrophy |
| [37369805](https://pubmed.ncbi.nlm.nih.gov/37369805/) | *SMN regulates GEMIN5 expression... modifier* | Therapeutic lead — SMN modifier; nusinersen/gene therapy rescue |
| [35393353](https://pubmed.ncbi.nlm.nih.gov/35393353/) | *Functional and structural deficiencies of Gemin5 variants* | Variant-level functional/structural deficits; reduced ribosome association |
| [36980979](https://pubmed.ncbi.nlm.nih.gov/36980979/) | *Biallelic Truncating Variant in TPR Domain* | TPR in-frame variant example; intellectual disability + cerebral atrophy |
| [38526274](https://pubmed.ncbi.nlm.nih.gov/38526274/) | *Function and dysfunction of GEMIN5* (review) | Comprehensive NEDCAM review; animal models; treatment directions |
| [30563832](https://pubmed.ncbi.nlm.nih.gov/30563832/) | *Composition of the SMN complex* | Background on SMN-complex composition |
| [40592581](https://pubmed.ncbi.nlm.nih.gov/40592581/) | *Proteins that recognize U7 snRNA...* | Context on Gemin5 snRNA-substrate specificity |

All quoted snippets above are verbatim from the cited abstracts and were verified during the investigation.

---

## Limitations and Knowledge Gaps

1. **Small cohort basis.** Essentially all phenotype frequencies derive from a single ~30-patient discovery cohort; broader, independent natural-history data are lacking.
2. **No epidemiological data.** Prevalence, incidence, carrier frequency, and founder effects are unquantified.
3. **Genotype–phenotype correlation is preliminary.** The variant sub-region/epilepsy correlation needs validation in larger series.
4. **Therapeutic evidence is preclinical.** SMN-upregulation rescue has been shown only in cells, iPSC neurons, and model organisms — no human clinical trial data exist.
5. **Mechanistic inference.** The specific cerebellar vulnerability and the relative contributions of the snRNP vs translational branches to clinical disease remain partly inferred rather than directly demonstrated.
6. **No validated biomarker** or disease-specific QoL instrument exists.
7. **Model limitations.** Zebrafish nulls are lethal; no faithful mammalian (mouse) model of the chronic human phenotype was identified in this investigation.

---

## Proposed Follow-up Experiments / Actions

1. **Establish a conditional/hypomorphic mouse model** of *Gemin5* to recapitulate chronic cerebellar atrophy and enable preclinical therapeutic testing (circumventing zebrafish lethality).
2. **Preclinical trial of nusinersen and SMN gene replacement** in GEMIN5-deficient iPSC-neuron and animal models, with quantitative snRNP/splicing and behavioral endpoints — the highest-priority translational step ([PMID: 37369805](https://pubmed.ncbi.nlm.nih.gov/37369805/)).
3. **Systematic genotype–phenotype study** across an expanded international cohort to validate the variant sub-region ↔ epilepsy/severity correlation ([PMID: 38773790](https://pubmed.ncbi.nlm.nih.gov/38773790/)).
4. **Longitudinal natural-history registry** to define progression rates, the frequency of late neurodegeneration, and survival.
5. **Cerebellar-specific transcriptomic/splicing profiling** (patient iPSC-derived cerebellar organoids) to directly test which downstream splicing/translation targets drive neuronal loss and to nominate biomarkers.
6. **Structure-guided variant functional assays** across the WD40, TPR, and C-terminal domains to build a quantitative map of residual function for ACMG variant classification.

---

*Report compiled from 8 confirmed findings and 13 reviewed papers over 5 investigation iterations. All mechanistic and clinical claims are attributed to the primary literature cited above.*


## Artifacts

- [OpenScientist final report](Neurodevelopmental_Disorder_With_Cerebellar_Atrophy_And_Motor_Dysfunction-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Neurodevelopmental_Disorder_With_Cerebellar_Atrophy_And_Motor_Dysfunction-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 19 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0859152` (3 mentions) - the report calls it "MONDO"; MONDO calls it **neurodevelopmental disorder with cerebellar atrophy and motor dysfunction**
- `DOID:0070443` (2 mentions) - the report calls it "DOID"; DOID calls it **neurodevelopmental disorder with cerebellar atrophy and motor dysfunction**
- `GO:0097504` (2 mentions) - the report calls it "Subcellular:** cytoplasm and nuclear gems"; GO calls it **Gemini of Cajal bodies**
- `UBERON:0002037` (1 mention) - the report calls it "cerebellum", "Primary organ:** brain, specifically the **cerebellum"; UBERON calls it **cerebellum**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001272` (2 mentions) - the report calls it "Cerebellar atrophy", "Cerebellar atrophy/hypoplasia"; HP calls it **Cerebellar atrophy**
- `HP:0000750` (2 mentions) - the report calls it "Delayed speech and language development", "Delayed speech/language"; HP calls it **Delayed speech and language development**, and lists "Delayed speech" among its other names
- `HP:0001251` (2 mentions) - the report calls it "Ataxia", "Cerebellar ataxia"; HP calls it **Ataxia**, and lists "Cerebellar ataxia" among its other names
- `HP:0001348` (2 mentions) - the report calls it "Hyperreflexia (brisk reflexes)"; HP calls it **Brisk reflexes**
- `HP:0003676` (1 mention) - the report calls it "Progressive course"; HP calls it **Progressive**, and lists "Progressive disorder" among its other names
- `UBERON:0001017` (1 mention) - the report calls it "Body system:** central nervous system"; UBERON calls it **central nervous system**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0001272` - called "Cerebellar atrophy", "Cerebellar atrophy/hypoplasia"
- `HP:0000750` - called "Delayed speech and language development", "Delayed speech/language"
- `HP:0001251` - called "Ataxia", "Cerebellar ataxia"
- `UBERON:0002037` - called "cerebellum", "Primary organ:** brain, specifically the **cerebellum"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.