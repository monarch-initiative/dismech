---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-25T06:52:30.131380'
end_time: '2026-10-25T07:06:49.193316'
duration_seconds: 859.06
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Inflammatory Skin And Bowel Disease Neonatal 2
  mondo_id: MONDO:0014481
  category: Mendelian
  causal_genes: EGFR
  omim_id: OMIM:616069
  synonyms: EGFR neonatal inflammatory skin and bowel disease; inflammatory skin and
    bowel disease, neonatal, type 2; neonatal inflammatory skin and bowel disease
    caused by mutation in EGFR
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
citation_count: 12
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 5
  validator_version: 0.4.0
term_validation:
  total_terms: 32
  verified: 30
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 10
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: CL:0000312
    reported_labels:
    - "Tissue/cell:** epithelial tissue \u2014 keratinocytes"
    ontology_label: keratinocyte
  - term_id: HP:0001596
    reported_labels:
    - Clinical sign
    ontology_label: Alopecia
  - term_id: HP:0200037
    reported_labels:
    - Papule
    ontology_label: Skin vesicle
  - term_id: HP:0005268
    reported_labels:
    - Progeroid facial appearance
    ontology_label: Miscarriage
  labels_variant: 4
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
  path: Inflammatory_Skin_And_Bowel_Disease_Neonatal_2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Inflammatory_Skin_And_Bowel_Disease_Neonatal_2-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Inflammatory Skin And Bowel Disease Neonatal 2
- **MONDO ID:** MONDO:0014481 (if available)
- **Causal gene(s):** EGFR
- **OMIM:** OMIM:616069
- **Synonyms:** EGFR neonatal inflammatory skin and bowel disease; inflammatory skin and bowel disease, neonatal, type 2; neonatal inflammatory skin and bowel disease caused by mutation in EGFR
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Inflammatory Skin And Bowel Disease Neonatal 2** covering all of the
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

# Inflammatory Skin and Bowel Disease, Neonatal, 2 (NISBD2): Comprehensive Disease Characterization

**MONDO:0014481 · OMIM:616069 · Causal gene: _EGFR_ (epidermal growth factor receptor, HGNC:3236)**

---

## Summary

**Inflammatory skin and bowel disease, neonatal, 2 (NISBD2)** is an ultra-rare, autosomal-recessive Mendelian disorder caused by **biallelic loss-of-function mutations in _EGFR_** (epidermal growth factor receptor), located at chromosome 7p11.2 (Ensembl ENSG00000146648, HGNC:3236, NCBI Gene 1956, UniProt P00533). It is critical to state the causal gene explicitly, because the serial disease name ("...neonatal 2") does not name a gene, and the clinically near-identical **NISBD1** (OMIM 614328) is caused by a *different* gene, **_ADAM17_**. NISBD2 is the EGFR form. The disease is defined by the landmark report of Campbell and colleagues (2014), who identified a homozygous loss-of-function missense mutation in *EGFR* (c.1283G>A; p.Gly428Asp) in a male infant with lifelong inflammation of the skin, bowel, and lungs [PMID: 24691054].

Mechanistically, loss of EGFR tyrosine-kinase signaling in skin, gut, and lung epithelium produces aberrant/premature keratinocyte differentiation, chemokine-driven inflammation (CCL2, CCL5, CCL27, CXCL14), and failure of antimicrobial-peptide and skin-barrier protein production, and consequently a severe multi-organ epithelial-inflammatory phenotype. This directly mirrors the "EGFR-inhibitor rash" seen in oncology patients treated with anti-EGFR drugs, and is faithfully recapitulated in mice with epidermis-specific EGFR deletion (EGFR^Δep), which show chemokine-driven skin inflammation, hair-follicle degeneration, barrier failure, impaired host defense, and early lethality [PMID: 23966300; PMID: 24691054].

Clinically, NISBD2 presents in the neonatal period with erythroderma/skin erosions, dry scale, alopecia, a papulopustular rash, inflammatory enteropathy with diarrhea, recurrent cutaneous and respiratory infections, and electrolyte imbalance. The prognosis is poor: the index patient died at 2.5 years from skin and chest infections and electrolyte imbalance, and a second independent case (a Roma girl carrying the same homozygous p.Gly428Asp allele) died at 10 months [PMID: 24691054; PMID: 40040597]. The recurrent c.1283G>A (p.Gly428Asp) variant is a **founder allele in the Roma population** and is ClinVar-classified **Pathogenic** (Variation ID 157499; rs606231253); it is essentially absent in the general population (gnomAD v4 AF ≈ 6.2×10⁻⁶, heterozygotes only, no homozygotes). No curative therapy exists; management is supportive.

---

## Key Findings

### Finding 1 — NISBD2 is caused by biallelic loss-of-function _EGFR_ mutations; the recurrent allele is p.Gly428Asp

Whole-exome sequencing of the index male infant identified a **homozygous loss-of-function missense mutation in _EGFR_** (c.1283G>A; p.Gly428Asp). In the original report, the authors state they *"identified a homozygous loss-of-function missense mutation in EGFR (c.1283 G>A; p.Gly428Asp) in a male infant with lifelong inflammation affecting the skin, bowel, and lungs"* [PMID: 24691054]. Functional validation confirmed the loss-of-function class: *"in vitro analysis of the mutant receptor revealed abrogated EGFR phosphorylation and EGF-stimulated downstream signaling"* [PMID: 24691054]. The variant therefore abolishes receptor autophosphorylation and all downstream signaling, satisfying the ACMG PS3 (functional) criterion.

A second, independent, unrelated case reported in 2025 — a 7-month-old Roma girl from a consanguineous family — carried *"the known homozygous EGFR p.G428D and the compound heterozygous ABCC6 p.R518* and p.R1221H variations"* [PMID: 40040597]. This demonstrates that p.Gly428Asp is a **recurrent founder allele**, not a private mutation, with a measurable carrier frequency in the Roma population (PMID: 38019142, *Frequency of EGFR gene variant in Roma Population*). Inheritance is autosomal recessive (OMIM 616069).

### Finding 2 — EGFR gene/variant identifiers and population genetics of p.Gly428Asp

The *EGFR* gene maps to chromosome **7p11.2** (GRCh38: 55,019,017–55,211,628), Ensembl **ENSG00000146648**, **HGNC:3236**. The causal allele **NM_005228.5(EGFR):c.1283G>A (p.Gly428Asp)** is catalogued with the following identifiers:

| Resource | Identifier / Value |
|---|---|
| ClinVar Variation ID | 157499 (**Pathogenic**) |
| dbSNP | rs606231253 |
| OMIM allelic variant | 131550.0007 |
| ClinGen allele | CA170941 |
| UniProt | VAR_072435 |
| GRCh38 position | chr7:55,157,738 G>A |
| GRCh37 position | chr7:55,225,431 G>A |
| gnomAD v4 exomes | AC=9, AN=1,461,876, **AF=6.16×10⁻⁶**, 0 homozygotes |
| gnomAD v2.1 exomes | AC=1, AN=251,476, AF=3.98×10⁻⁶ |

The variant is **germline, biallelic, and loss-of-function**. Only heterozygous carriers are present in the general population, consistent with a rare recessive pathogenic founder allele enriched in the Roma. By ACMG/AMP criteria the variant meets **PS3** (in vitro functional damage), **PM2** (absent/ultra-rare in population databases), and **PM3** (detected in trans / recessive), supporting a **Pathogenic** classification.

### Finding 3 — Mechanism: epidermal EGFR loss drives chemokine-mediated inflammation, barrier/antimicrobial defects, and infection

The downstream consequences of epithelial EGFR loss are best defined in the keratinocyte/mouse system. EGFR inhibition (pharmacologic or genetic) *"induce[s] the expression of chemokines (CCL2, CCL5, CCL27, and CXCL14) in epidermal keratinocytes and impair[s] the production of antimicrobial peptides and skin barrier proteins"* [PMID: 23966300]. The epidermis-specific knockout faithfully reproduces the human disease: *"Mice lacking epidermal EGFR (EGFR(Δep)) show a similar phenotype, which is accompanied by chemokine-driven skin inflammation, hair follicle degeneration, decreased host defense, and deficient skin barrier function, as well as early lethality"* [PMID: 23966300].

In the human index patient, molecular profiling of lesional skin corroborated the mechanism: *"Microarray analysis on the patient's skin highlighted disturbed differentiation/premature terminal differentiation of keratinocytes and upregulation of several inflammatory/innate immune response networks"* [PMID: 24691054]. The inflammatory infiltrate in the mouse model is dominated by dendritic cells, macrophages, granulocytes, mast cells, and T cells; skin toxicity was **not** rescued by Rag2, MyD88, or CCL2 deficiency, nor by Langerhans-cell/hair-follicle ablation — but mast-cell inhibition reduced T-cell influx, implicating mast cells as an amplifying node. Reduced keratinocyte cytotoxic activity against *Staphylococcus aureus* links the barrier/antimicrobial defect directly to the clinical propensity for skin infection.

### Finding 4 — Clinical phenotype: multi-organ epithelial inflammation with early death

The index patient (Campbell 2014) had lifelong inflammation of skin, bowel, and lungs from the neonatal period. *"During the first year of life, his skin showed erosions, dry scale, and alopecia. Subsequently, there were numerous papules and pustules—similar to the rash seen in patients receiving EGFR inhibitor drugs"* [PMID: 24691054]. Outcome was fatal: *"The boy died at the age of 2.5 years from extensive skin and chest infections as well as electrolyte imbalance"* [PMID: 24691054].

The second case independently delineated the same multisystem syndrome: *"inflammatory skin, alopecia, progeroid features, electrolyte imbalance, recurrent infections, and premature death"*, with death at 10 months [PMID: 40040597]. The EGFR^Δep mouse adds hair-follicle degeneration and barrier failure to the phenotypic spectrum [PMID: 23966300].

### Finding 5 — NISBD2 (EGFR) and NISBD1 (ADAM17) are pathway-convergent

NISBD2's principal differential diagnosis, **NISBD1** (OMIM 614328), is caused by biallelic loss-of-function variants in **_ADAM17_** (e.g., compound heterozygous p.Cys567Arg / p.Cys600Tyr). ADAM17 is *"the major sheddase that processes more than 80 substrates, including tumour necrosis factor-α (TNFα)"* [PMID: 33953303] — and, critically, it releases the EGFR-activating ligands TGF-α, amphiregulin, and HB-EGF. NISBD1 siblings presented with *"erythroderma with exudate in whole body, recurrent skin infection and sepsis and prolonged diarrhoea"* [PMID: 33953303], clinically overlapping NISBD2.

The two diseases are therefore **mechanistically convergent on the same EGFR ligand–receptor signaling axis**: ADAM17 deficiency (NISBD1) starves the receptor of ligand, whereas EGFR mutation (NISBD2) disables the receptor itself. Both abolish downstream EGFR signaling in skin and gut epithelium, explaining the near-identical phenotype.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic _EGFR_ loss-of-function mutation** (homozygous c.1283G>A; p.Gly428Asp) **leads to** a receptor that cannot autophosphorylate [demonstrated in vitro, PMID: 24691054].
2. Loss of EGFR kinase activity **results in** abolished activation of downstream cascades (canonically RAS–MAPK/ERK and PI3K–AKT) in epithelial cells [inferred from EGFR biology; functional loss demonstrated].
3. Absent EGFR signaling in keratinocytes **leads to** disturbed/premature terminal keratinocyte differentiation [demonstrated by patient skin microarray, PMID: 24691054].
4. In parallel, loss of EGFR signaling **results in** induction of keratinocyte chemokines CCL2, CCL5, CCL27, CXCL14 **and** impaired production of antimicrobial peptides and skin-barrier proteins [demonstrated, PMID: 23966300].
   - **Branch A (inflammation):** chemokine induction **recruits** dendritic cells, macrophages, granulocytes, mast cells, and T cells → chemokine-driven skin inflammation; mast cells **amplify** T-cell influx [demonstrated in mouse, PMID: 23966300].
   - **Branch B (barrier/host-defense):** reduced antimicrobial peptides + barrier proteins + reduced keratinocyte cytotoxicity against *S. aureus* **leads to** deficient barrier and decreased host defense → recurrent skin/chest infections [demonstrated, PMID: 23966300; clinical, PMID: 24691054].
5. The same epithelial defect in **gut** epithelium **leads to** inflammatory enteropathy with prolonged diarrhea → fluid/electrolyte loss [clinical; mechanism inferred by analogy].
6. In **lung/airway** epithelium, loss of EGFR signaling **contributes to** pulmonary inflammation and susceptibility to chest infection [clinical, PMID: 24691054].
7. Combined cutaneous + respiratory infection and electrolyte imbalance **results in** early death (infancy to early childhood) [clinical, PMID: 24691054; PMID: 40040597].

### Pathway-convergence diagram

```
   NISBD1 (ADAM17 LoF)                 NISBD2 (EGFR LoF)
         │                                   │
   ADAM17 sheddase fails          EGFR p.Gly428Asp cannot
   to release EGFR ligands        autophosphorylate
   (TGF-a, AREG, HB-EGF)                      │
         │                                   │
         └──────────► LOSS OF EGFR SIGNALING ◄┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
  Aberrant kerat.    Chemokines up       Antimicrobial
  differentiation    (CCL2/5/27,         peptides &
                     CXCL14)             barrier proteins down
        │                   │                   │
        ▼                   ▼                   ▼
   Skin/epithelial    Immune-cell         Infection
   fragility          infiltration        (S. aureus, chest)
        └───────────────────┴───────────────────┘
                            ▼
         Multi-organ epithelial inflammation
         (skin, bowel, lung) + electrolyte imbalance
                            ▼
                   Early death (infancy)
```

### Ontology term suggestions

- **Gene/Protein:** EGFR (HGNC:3236); UniProt P00533. GO biological processes: *epidermal growth factor receptor signaling pathway* (GO:0007173), *keratinocyte differentiation* (GO:0030216), *epidermis development* (GO:0008544), *regulation of inflammatory response* (GO:0050727), *antimicrobial humoral response* (GO:0019730), *establishment of skin barrier* (GO:0061436). GO cellular component: *plasma membrane* (GO:0005886), *receptor complex* (GO:0043235).
- **Cell types (CL):** keratinocyte (CL:0000312), epidermal cell (CL:0000362), enterocyte/intestinal epithelial cell (CL:0000584 / CL:0002563), mast cell (CL:0000097), macrophage (CL:0000235), dendritic cell (CL:0000451), T cell (CL:0000084).
- **Anatomy (UBERON):** skin/epidermis (UBERON:0001003), intestine (UBERON:0000160), lung (UBERON:0002048), hair follicle (UBERON:0002073).
- **Chemical/ligand (CHEBI/protein):** EGF, TGF-α, amphiregulin, HB-EGF (EGFR ligands).
- **Disease (MONDO):** MONDO:0014481 (NISBD2); differential MONDO for NISBD1 (ADAM17).

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | How it supports / informs findings |
|---|---|---|---|
| [24691054](https://pubmed.ncbi.nlm.nih.gov/24691054/) | *Epithelial inflammation resulting from an inherited loss-of-function mutation in EGFR* | Human clinical + in vitro | **Defining paper.** Identifies causal gene, variant (c.1283G>A; p.Gly428Asp), homozygosity, LoF functional class, and full clinical phenotype/outcome. Patient skin microarray shows aberrant keratinocyte differentiation + inflammatory networks. |
| [40040597](https://pubmed.ncbi.nlm.nih.gov/40040597/) | *Severe ABCC6-induced GACI overshadowed by EGFR-associated NISBD2 in a Roma girl* | Human clinical | Second independent case with the **same homozygous p.G428D** allele in a consanguineous Roma family; confirms founder allele and multisystem phenotype (progeroid features, electrolyte imbalance, premature death at 10 mo). |
| [23966300](https://pubmed.ncbi.nlm.nih.gov/23966300/) | *Epidermal EGFR controls cutaneous host defense and prevents inflammation* | Model organism (mouse) + in vitro | Mechanistic backbone. EGFR^Δep mice recapitulate human phenotype; defines chemokine induction (CCL2/5/27, CXCL14), barrier/antimicrobial failure, host-defense defect, early lethality. |
| [33953303](https://pubmed.ncbi.nlm.nih.gov/33953303/) | *Compound heterozygous ADAM17 LoF variants cause NISBD1* | Human clinical + functional | Establishes NISBD1 (ADAM17) as the pathway-convergent differential; ADAM17 sheds EGFR ligands, linking the two diseases to one axis. |
| [38019142](https://pubmed.ncbi.nlm.nih.gov/38019142/) | *Frequency of EGFR Gene Variant in Roma Population* | Population genetics | Supports founder-allele interpretation of p.Gly428Asp in the Roma. |
| [7618085](https://pubmed.ncbi.nlm.nih.gov/7618085/) | *Strain-dependent epithelial defects in mice lacking the EGF receptor* | Model organism (mouse) | Classic Egfr-null model: open eyes, immature lungs, epidermal defects, perinatal lethality; shows EGFR regulates epithelial proliferation/differentiation and strong genetic-background modifier effect. |

**Supporting / contextual literature on EGFR-inhibitor dermatologic toxicity** (the pharmacologic phenocopy of NISBD2, informing supportive management): prophylactic tetracyclines/doxycycline and topical corticosteroids reduce grade ≥2 acneiform rash [PMID: 42151517; PMID: 32609305; PMID: 30607677; PMID: 33392769; PMID: 33028137], and azithromycin is an alternative in tetracycline intolerance [PMID: 42541756]. These EGFRi-rash management data are the closest evidence-based analogue for the cutaneous component of NISBD2, though not studied in NISBD2 patients directly.

---

## Section-by-Section Report

### 1. Disease Information
NISBD2 is an ultra-rare autosomal-recessive, neonatal-onset multisystem **epithelial inflammatory disorder** caused by biallelic *EGFR* loss of function. Identifiers: **MONDO:0014481**, **OMIM 616069**, gene **EGFR** (HGNC:3236; OMIM 131550). Orphanet lists it under neonatal inflammatory skin and bowel disease; specific ICD-10/ICD-11 and MeSH codes are not uniquely assigned (closest: ICD-11 rare-disease and congenital ichthyosiform/erythroderma categories — not disease-specific). Synonyms: *EGFR neonatal inflammatory skin and bowel disease; inflammatory skin and bowel disease, neonatal, type 2; neonatal inflammatory skin and bowel disease caused by mutation in EGFR*. Information is derived from **individual patient case reports** (n≈2 molecularly confirmed) plus aggregated gene/variant databases and a mouse model — not from EHR-scale cohorts.

### 2. Etiology
**Causal factor:** genetic — homozygous (or compound heterozygous) loss-of-function *EGFR* variants; the recurrent allele is c.1283G>A (p.Gly428Asp). **Genetic risk:** consanguinity and Roma ancestry (founder allele). **Environmental risk/protective/GxE factors:** none established; this is a monogenic disorder. Infection is a *downstream consequence* (barrier failure), not a cause. No protective alleles identified. The *EGFR*-null mouse literature shows a strong **genetic-background modifier effect** on survival [PMID: 7618085], suggesting modifier genes may influence human expressivity (inferred).

### 3. Phenotypes
| Phenotype | Type | HPO suggestion | Onset | Frequency |
|---|---|---|---|---|
| Neonatal erythroderma / skin erosions, dry scale | Clinical sign | HP:0001019 (Erythroderma); HP:0200041 (Skin erosion) | Neonatal | Core |
| Alopecia | Clinical sign | HP:0001596 | Infancy | Reported in both cases |
| Papulopustular ("EGFRi-like") rash | Clinical sign | HP:0200037 (Papule) / pustules | First year | Reported |
| Inflammatory enteropathy / diarrhea | Symptom | HP:0002014 (Diarrhea) | Neonatal | Core |
| Recurrent skin/respiratory infections | Clinical sign | HP:0002719 (Recurrent infections) | Early | Core |
| Electrolyte imbalance | Lab abnormality | HP:0003111 (Abnormal blood electrolyte concentration) | Early | Both cases |
| Pulmonary inflammation | Clinical sign | HP:0002090 (Pneumonia) | Early | Index case |
| Progeroid features | Physical | HP:0005268 (Progeroid facial appearance) | Infancy | Case 2 |

Severity is **severe**, progression is **progressive**, and quality-of-life impact is profound given neonatal onset and early lethality.

### 4. Genetic / Molecular Information
**Causal gene:** *EGFR* (HGNC:3236; chr7p11.2). **Variant:** NM_005228.5:c.1283G>A, p.Gly428Asp; **missense** with loss-of-function consequence (abrogated phosphorylation). **Classification:** ClinVar Pathogenic (Variation ID 157499); ACMG PS3+PM2+PM3. **Allele frequency:** gnomAD v4 AF 6.16×10⁻⁶, no homozygotes. **Origin:** germline, biallelic. **Functional consequence:** loss of function (receptor cannot autophosphorylate or transduce EGF signal). **Modifier genes:** none proven in humans; strain-dependent modifiers in mouse. **Epigenetic/chromosomal:** none implicated. (In case 2, co-occurring *ABCC6* variants caused a separate GACI phenotype — not part of NISBD2.)

### 5. Environmental Information
No environmental, lifestyle, or infectious *causes*. Infectious agents (notably *Staphylococcus aureus* and respiratory pathogens) act as **secondary complications** of the barrier/host-defense defect [PMID: 23966300].

### 6. Mechanism / Pathophysiology
See **Mechanistic Model** above for the ordered causal chain, branch diagram, and ontology terms. In brief: EGFR LoF → loss of RAS-MAPK/PI3K-AKT epithelial signaling → (a) aberrant keratinocyte differentiation, (b) chemokine-driven immune infiltration, (c) antimicrobial/barrier failure → multi-organ epithelial inflammation and infection → early death. Key molecular pathway: **EGFR/ErbB signaling (KEGG hsa04012; Reactome R-HSA-177929)**. Immune involvement is innate-dominant inflammation (not autoimmunity). Mast cells amplify T-cell recruitment.

### 7. Anatomical Structures Affected
- **Primary organs:** skin/epidermis (UBERON:0001003), intestine (UBERON:0000160), lung (UBERON:0002048).
- **Secondary:** hair follicles (UBERON:0002073; degeneration), systemic effects of electrolyte imbalance.
- **Tissue/cell:** epithelial tissue — keratinocytes (CL:0000312), intestinal epithelial cells (CL:0002563), airway epithelium; infiltrating immune cells (mast cells, macrophages, dendritic cells, T cells, granulocytes).
- **Subcellular:** plasma-membrane receptor complex (GO:0043235); signaling defect at the cell surface.
- **Lateralization:** bilateral/generalized (whole-body skin involvement).

### 8. Temporal Development
**Onset:** congenital/neonatal. **Pattern:** chronic-progressive from birth. **Course:** lifelong, progressive, lethal in infancy to early childhood (2.5 years and 10 months in the two reported cases). No remission observed. The neonatal period is the critical window; there is no demonstrated intervention that alters the natural history.

### 9. Inheritance and Population
**Inheritance:** autosomal recessive (OMIM 616069). **Penetrance:** presumed complete in biallelic carriers (both reported homozygotes affected). **Expressivity:** likely variable (ages at death differ). **Epidemiology:** prevalence not formally estimated — ultra-rare (<10 molecularly confirmed individuals reported). **Founder effect:** p.Gly428Asp is a Roma founder allele with measurable carrier frequency [PMID: 38019142]. **Consanguinity:** contributory (case 2 consanguineous). **Carrier frequency (general population):** ~6×10⁻⁶ (gnomAD, heterozygotes only). **Sex:** both sexes affected (male index, female case 2); no sex bias established.

### 10. Diagnostics
**Genetic testing is definitive:** single-gene *EGFR* sequencing, targeted p.Gly428Asp testing (especially in Roma/consanguineous families), gene panels (primary immunodeficiency / ichthyosis / very-early-onset IBD panels), or **WES/WGS**. **Supporting tests:** skin biopsy (disturbed/premature keratinocyte terminal differentiation, inflammatory infiltrate) [PMID: 24691054]; serum electrolytes; infection work-up/cultures. **Differential diagnosis:** NISBD1 (*ADAM17*) — clinically near-identical, distinguished only by gene [PMID: 33953303]; Netherton syndrome, other congenital ichthyosiform erythrodermas, very-early-onset IBD, immunodeficiency-associated dermatitis. **Screening:** carrier/cascade screening in at-risk Roma families; prenatal/preimplantation testing feasible for known familial variant.

### 11. Outcome / Prognosis
**Prognosis is poor.** Both molecularly confirmed patients died in infancy/early childhood (2.5 y; 10 mo) from infection and electrolyte imbalance [PMID: 24691054; PMID: 40040597]. Major complications: sepsis, pneumonia, cutaneous infections, dehydration/electrolyte derangement, failure to thrive. No survival statistics exist beyond case reports. Prognostic factors are not formally defined; infection control and electrolyte stability are the practical determinants of survival.

### 12. Treatment
**No curative therapy.** Management is **supportive**: aggressive infection prophylaxis/treatment, skin-barrier care/emollients, nutritional support, and electrolyte repletion. The cutaneous component is a biologic phenocopy of EGFR-inhibitor rash, so EGFRi-rash evidence is the nearest guide: prophylactic **tetracyclines/doxycycline** plus **topical corticosteroids** reduce grade ≥2 acneiform rash [PMID: 42151517; PMID: 32609305; PMID: 30607677], with **azithromycin** as an alternative in tetracycline intolerance [PMID: 42541756] — though none has been formally tested in NISBD2. Conceptually, because EGFR itself is nonfunctional, **EGFR-ligand supplementation would not rescue NISBD2** (unlike the ADAM17-deficient NISBD1, where ligand/pathway restoration is mechanistically plausible). NCIT suggestions: *Doxycycline (C721)*, *Topical Corticosteroid (C1127)*, *Supportive Care (C15277)*. No approved gene/cell/RNA therapy.

### 13. Prevention
Primary prevention is **genetic**: carrier screening and genetic counseling in Roma/consanguineous families, cascade testing of relatives, and reproductive options (prenatal diagnosis, preimplantation genetic testing) for the known familial p.Gly428Asp allele. Secondary/tertiary prevention in affected infants = early infection surveillance, barrier protection, and electrolyte management to forestall complications. No vaccine or environmental intervention applies.

### 14. Other Species / Natural Disease
No naturally occurring companion-animal homolog of NISBD2 is catalogued in OMIA. The orthologous gene is mouse *Egfr* (NCBI Gene 13649). Comparative biology is strong: *Egfr*-null and epidermis-specific *Egfr* knockout mice reproduce epithelial-differentiation defects, skin inflammation, immature lungs, and perinatal/early lethality, with notable strain-dependent modifier effects [PMID: 7618085; PMID: 23966300]. Evolutionary conservation of EGFR epithelial function is high across vertebrates and even invertebrates (EGFR/EGF signaling conserved to *Drosophila*).

### 15. Model Organisms
- **Mouse — constitutive _Egfr_ knockout:** epithelial defects (open eyes, rudimentary whiskers, immature lungs, epidermal defects), growth retardation, mid-gestation-to-perinatal lethality; phenotype strongly modified by genetic background [PMID: 7618085]. *Recapitulation:* partial (captures epithelial/lung involvement; many die before the full postnatal skin/gut phenotype).
- **Mouse — epidermis-specific _Egfr_ knockout (EGFR^Δep):** the best disease model — chemokine-driven skin inflammation, hair-follicle degeneration, barrier failure, decreased host defense, early lethality [PMID: 23966300]. *Recapitulation:* high for the cutaneous/inflammatory axis.
- **In vitro:** patient-derived and mutant-receptor cell assays demonstrating abolished phosphorylation/signaling [PMID: 24691054]; keratinocyte models of EGFR-inhibitor chemokine induction [PMID: 23966300].
- **Limitations:** constitutive KO lethality limits study of chronic multi-organ disease; mouse-vs-human differences in skin/immune biology; no reported zebrafish/organoid NISBD2-specific model. Resources: MGI (mouse *Egfr*), IMPC/KOMP conditional alleles.

---

## Limitations and Knowledge Gaps

1. **Extremely small human evidence base** — only two molecularly confirmed patients (one defining case plus one 2025 case), both homozygous for the same founder allele. Phenotypic range, penetrance, and expressivity are therefore poorly bounded.
2. **Single recurrent variant** — nearly all human knowledge derives from p.Gly428Asp; the consequences of other biallelic *EGFR* LoF genotypes (e.g., nonsense/frameshift, compound heterozygotes) in humans are essentially unknown and may be more severe or embryonic-lethal.
3. **Mechanism in gut and lung is inferred by analogy** to the well-characterized skin/keratinocyte model; organ-specific human molecular data for bowel and lung are limited.
4. **No therapeutic evidence specific to NISBD2** — supportive-care recommendations are extrapolated from EGFR-inhibitor rash oncology literature, not from NISBD2 trials.
5. **No epidemiologic estimates** — prevalence/incidence are unquantified; Roma carrier frequency is reported but general-population burden is negligible and undefined.
6. **Modifier genetics** suggested by mouse strain effects remain unexplored in humans.

## Proposed Follow-up Experiments / Actions

1. **Establish an international NISBD2 registry / GeneMatcher outreach** to collect additional molecularly confirmed cases and genotype–phenotype correlations beyond p.Gly428Asp.
2. **Patient-derived iPSC → keratinocyte/intestinal/airway organoids** carrying p.Gly428Asp to dissect organ-specific EGFR-loss transcriptomes (single-cell RNA-seq) and test candidate rescue strategies.
3. **Conditional, inducible gut- and lung-specific _Egfr_ knockouts** to directly test the inferred enteropathy and pulmonary steps of the causal chain.
4. **Targeted Roma-population carrier screening study** to quantify p.Gly428Asp carrier frequency precisely and inform genetic-counseling programs.
5. **Preclinical evaluation of downstream-pathway agonism** (e.g., direct RAS-MAPK/PI3K-AKT pathway modulation) in EGFR^Δep mice and organoids, since upstream ligand supplementation cannot rescue a dead receptor — distinguishing NISBD2 therapeutic logic from NISBD1.
6. **Prospective supportive-care protocol** adapting EGFRi-rash prophylaxis (doxycycline + topical corticosteroids) with infection surveillance and electrolyte management, with structured outcome capture.

---

*Report compiled from 5 discovery iterations, 6 confirmed findings, and 25 reviewed papers. Evidence types: human clinical case reports (PMID: 24691054, 40040597), functional/model-organism studies (PMID: 23966300, 7618085, 33953303), population genetics (PMID: 38019142, gnomAD/ClinVar), and contextual EGFRi-toxicity management literature.*


## Artifacts

- [OpenScientist final report](Inflammatory_Skin_And_Bowel_Disease_Neonatal_2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Inflammatory_Skin_And_Bowel_Disease_Neonatal_2-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 18 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CL:0000312` (2 mentions) - the report calls it "Tissue/cell:** epithelial tissue — keratinocytes"; CL calls it **keratinocyte**
- `HP:0001596` (1 mention) - the report calls it "Clinical sign"; HP calls it **Alopecia**
- `HP:0200037` (1 mention) - the report calls it "Papule"; HP calls it **Skin vesicle**
- `HP:0005268` (1 mention) - the report calls it "Progeroid facial appearance"; HP calls it **Miscarriage**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0014481` (3 mentions) - the report calls it "NISBD2"; MONDO calls it **inflammatory skin and bowel disease, neonatal, 2**, and lists "NISBD2" among its other names
- `GO:0043235` (2 mentions) - the report calls it "receptor complex", "Subcellular:** plasma-membrane receptor complex"; GO calls it **signaling receptor complex**
- `UBERON:0001003` (2 mentions) - the report calls it "Primary organs:** skin/epidermis"; UBERON calls it **skin epidermis**
- `HP:0003111` (1 mention) - the report calls it "Abnormal blood electrolyte concentration"; HP calls it **Abnormal circulating electrolyte concentration**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0043235` - called "receptor complex", "Subcellular:** plasma-membrane receptor complex"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.