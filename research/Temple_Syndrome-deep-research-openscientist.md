---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T15:43:16.767062'
end_time: '2026-10-24T16:13:47.195186'
duration_seconds: 1830.43
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Temple Syndrome
  mondo_id: MONDO:0100507
  category: Mendelian
  causal_genes: not recorded
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
citation_count: 30
reference_validation:
  total_references: 30
  verified: 30
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 12
  quotes_valid: 11
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:42677749
  relevance_assessed: 30
  on_topic: 16
  off_topic: 1
  off_topic_references:
  - PMID:39889767
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 36
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 29
  labels_matching: 13
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0100507
    reported_labels:
    - MONDO
    ontology_label: multiple congenital anomalies due to 14q32.2 paternally expressed
      gene defect
  - term_id: CL:0000617
    reported_labels:
    - GnRH neuron, approximate
    ontology_label: GABAergic neuron
  - term_id: GO:0005634
    reported_labels:
    - nucleus, site of imprinting lesion
    ontology_label: nucleus
  - term_id: NCIT:C1762
    reported_labels:
    - Recombinant Human Growth Hormone
    ontology_label: Raloxifene Hydrochloride
  - term_id: NCIT:C15190
    reported_labels:
    - Enteral Nutrition
    ontology_label: Needle Biopsy
  labels_variant: 11
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
  path: Temple_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Temple_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Temple Syndrome
- **MONDO ID:** MONDO:0100507 (if available)
- **Causal gene(s):** not recorded
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

Please provide a comprehensive research report on **Temple Syndrome** covering all of the
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

# Temple Syndrome (TS14): A Comprehensive Disease Characteristics Report

**Disease:** Temple syndrome (TS14)
**MONDO ID:** MONDO:0100507 · **OMIM:** #616222 · **Orphanet:** ORPHA:254528
**Causal locus:** Chromosome 14q32.2 imprinted *DLK1-DIO3* domain
**Category:** Mendelian / imprinting disorder

---

## Summary

**Temple syndrome is a rare genomic imprinting disorder of the chromosome 14q32.2 *DLK1-DIO3* domain.** Its defining molecular lesion is the loss of expression of the **paternally expressed, protein-coding genes — chiefly *DLK1* (Delta-Like Non-Canonical Notch Ligand 1), together with *RTL1* and *DIO3*** — combined with biallelic over-expression of the maternally expressed non-coding RNAs of the same cluster (*MEG3*/GTL2, *MEG8*, the *RTL1* antisense transcript, and an embedded miRNA/snoRNA array). This dosage imbalance is produced by three convergent mechanisms, all of which manifest as hypomethylation of the *MEG3/DLK1* intergenic differentially methylated region (IG-DMR) and the *MEG3*-DMR: (1) **maternal uniparental disomy of chromosome 14 [upd(14)mat]**, (2) **isolated paternal epimutation (loss of methylation)** of the IG-DMR/MEG3-DMR, and (3) **paternal microdeletion of 14q32**. In the two largest cohorts the proportions are roughly 29–61% epimutation, 29–88% upd(14)mat, and 5–11% deletion, varying with ascertainment [PMID: 29659920; PMID: 39693239].

**Clinically, TS14 presents as a multi-system growth and metabolic disorder.** Cardinal features are pre- and postnatal growth restriction (most children are small for gestational age), neonatal hypotonia and feeding difficulties, motor and language delay, small hands and feet, later truncal obesity, and **central precocious puberty (CPP)** — the last driven specifically by loss of *DLK1*. Pooled data from 51 published cases gave hypotonia 93%, motor delay 83%, early puberty 86% (mean menarche 10 years 2 months), small hands 87%, small feet 96%, and obesity 49% [PMID: 24891339]. A genetically confirmed 60-patient Japanese cohort reported SGA 88.3%, postnatal short stature 87.0%, and CPP 86.0% [PMID: 39693239]. Cognition is generally normal to mildly reduced (median IQ ~85–91), and adult functional outcome is favourable (98.2% attended college or held jobs), but there is meaningful lifelong cardiometabolic risk — obesity ~20%, hypercholesterolemia ~27%, and early type 2 diabetes ~13% [PMID: 39693239; PMID: 36362517].

**TS14 is clinically important chiefly because it is under-diagnosed and treatable.** It overlaps substantially with Silver-Russell syndrome (SRS) and Prader-Willi syndrome (PWS) and is identified in roughly 2% of patients referred for PWS or SRS testing [PMID: 29159982]. Diagnosis rests on tiered methylation and copy-number/UPD testing of 14q32. Management is supportive and multidisciplinary: recombinant growth hormone (rhGH) improves short- and long-term height and body composition, GnRH-analogue therapy suppresses precocious puberty, and lifelong metabolic surveillance addresses the obesity/dyslipidemia/diabetes risk. No disease-modifying or gene-directed therapy exists. Recurrence risk is low for the common sporadic mechanisms, but paternally inherited 14q32 deletions are Mendelian with a parent-of-origin twist: the *same* deletion transmitted through a mother produces the mirror-image disorder, **Kagami-Ogata syndrome (KOS)**.

---

## Section 1 — Disease Information

**Overview.** Temple syndrome (TS14) is a rare, clinically recognizable imprinting disorder caused by absence of the paternally expressed genes and/or over-expression of the maternally expressed non-coding RNAs within a single imprinted cluster on human chromosome 14q32 [PMID: 32592473]. It was delineated as a distinct entity and given its eponym by Ioannides et al. in 2014 after analysis of 51 published cases of what had previously been called the "maternal UPD14 phenotype," honouring clinician-geneticist I. Karen Temple [PMID: 24891339].

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM | #616222 |
| MONDO | MONDO:0100507 |
| Orphanet | ORPHA:254528 |
| HGNC genes | *DLK1* (HGNC:2907), *MEG3* (HGNC:14575), *RTL1* (HGNC:35814), *MEG8*, *DIO3* |

**Synonyms / alternative names:** maternal uniparental disomy 14 syndrome; upd(14)mat phenotype/syndrome; TS14; 14q32.2 maternal imprinting defect [PMID: 34460908; PMID: 39693239].

**Information source.** This report is derived from aggregated disease-level resources (OMIM, Orphanet, MONDO) and from published clinical cohorts and case series (human clinical evidence), supplemented by model-organism and in-vitro mechanistic studies. It is not EHR/individual-patient derived.

---

## Section 2 — Etiology

**Primary cause — genetic/epigenetic.** TS14 is a constitutional (epi)genetic disorder with **no infectious, toxic, or classical lifestyle cause.** The primary lesion is a parent-of-origin dosage imbalance at 14q32.2 produced by three mechanisms [PMID: 38715103; PMID: 32592473; PMID: 29659920]:

1. **Maternal uniparental disomy of chromosome 14 [upd(14)mat]** — typically a maternal meiosis-I nondisjunction error followed by postzygotic trisomy-14 rescue (occasionally monosomy rescue or a mitotic error), which explains the occasional co-occurrence of TS14 with mosaic trisomy 14 [PMID: 30181735; PMID: 33746039].
2. **Isolated primary epimutation** — sporadic loss of methylation at the paternal IG-DMR/MEG3-DMR [PMID: 26395259; PMID: 25351781].
3. **Paternal 14q32 microdeletion** — heritable and Mendelian [PMID: 38715103].

**Genetic risk factors.** The causal "variants" are the (epi)genetic lesions above. There are no established common susceptibility loci or modifier alleles with proven effect on TS14 risk. Multilocus imprinting disturbance (MLID) can co-affect other imprinted loci (e.g., 11p15), sometimes attributable to variants in methylation-machinery genes, and represents an etiologic modifier rather than an independent cause [PMID: 35266280].

**Environmental risk factors.** (1) **Advanced maternal age** is associated with the meiotic nondisjunction that underlies upd(14)mat via trisomy rescue [PMID: 30181735]. (2) **Assisted reproductive technology (ART)** is a recognized (though not TS14-specific) risk for imprinting epimutations: "ART procedures, especially ovarian hyperstimulation, in vitro fertilization (IVF), and embryo culture, coincide with critical periods of epigenetic reprogramming and may contribute to epimutations in imprinting control regions" [PMID: 41153459].

**Protective factors.** No protective alleles or environmental protective factors are established for TS14.

**Gene–environment interactions.** The *DLK1-MEG3* methylation state is environmentally sensitive: preeclampsia exposure is associated with hypermethylation of the IG-DMR and altered *DLK1/MEG3* expression in umbilical vessels, illustrating that environmental stress can perturb this locus [PMID: 30234781]. This is mechanistically illustrative rather than a demonstrated cause of TS14.

---

## Section 3 — Phenotypes

TS14 phenotypes are predominantly physical manifestations, clinical signs, and some behavioural/neurodevelopmental features, with a few laboratory abnormalities (dyslipidemia, hyperglycemia) emerging later in life.

| Phenotype | HPO term (suggested) | Type | Onset | Frequency | Source |
|---|---|---|---|---|---|
| Intrauterine / prenatal growth restriction | HP:0001511 | Physical | Prenatal | 67–88% SGA; 100% IUGR in some cohorts | PMID: 39693239; PMID: 36362517 |
| Postnatal short stature | HP:0004322 | Physical | Childhood (~2 y) | 87% | PMID: 39693239 |
| Muscular hypotonia | HP:0001252 | Clinical sign | Neonatal | 71–100% (pooled 93%) | PMID: 24891339; PMID: 36362517 |
| Feeding difficulties | HP:0011968 | Clinical sign | Neonatal | 53–86% | PMID: 42026594; PMID: 36362517 |
| Motor delay | HP:0001270 | Behavioural/neuro | Infancy | 83% | PMID: 24891339 |
| Delayed speech / language | HP:0000750 | Behavioural/neuro | Childhood | Common | PMID: 42026594 |
| Small hands | HP:0200055 | Physical | Congenital | 87% | PMID: 24891339 |
| Small feet | HP:0001773 | Physical | Congenital | 96% | PMID: 24891339 |
| Truncal obesity / weight gain | HP:0001956 | Physical | Later childhood | ~20–49% | PMID: 24891339; PMID: 39693239 |
| Central precocious puberty | HP:0000826 | Clinical sign | Childhood | 86–89% | PMID: 39693239; PMID: 36362517 |
| Intellectual/developmental disability (mild) | HP:0001249 | Behavioural/neuro | Childhood | ~22% (IQ median ~85–91) | PMID: 39693239; PMID: 36362517 |
| Hypercholesterolemia | HP:0003124 | Lab abnormality | ≥6 y | 26.5% | PMID: 39693239 |
| Diabetes mellitus (type 2) | HP:0000819 | Lab abnormality | ≥9 y | 12.8% | PMID: 39693239 |

**Severity/progression.** Core features (growth restriction, small hands/feet, hypotonia) are congenital and largely stable/non-progressive. The metabolic phenotype (obesity, dyslipidemia, early diabetes) is progressive/age-dependent. Precocious puberty is episodic in presentation but reversible with treatment. Expressivity is variable.

**Quality-of-life impact.** TS14 affects growth, feeding, motor/language development, and psychosocial function; psycho-behavioral problems were reported in ~53% of one cohort [PMID: 36362517]. Despite early special-education enrolment (~43–54%), the great majority achieve independent adult function [PMID: 39693239]. No TS14-specific EQ-5D/SF-36 data are available.

---

## Section 4 — Genetic / Molecular Information

**Causal genes and domain architecture.** The disorder maps to the imprinted *DLK1-DIO3* domain at 14q32.2. "The domain contains three imprinted protein-coding genes, Dlk1, Rtl1 and Dio3, expressed from the paternally inherited chromosome and several imprinted large and small noncoding RNA genes expressed from the maternally inherited homolog" [PMID: 18471925]. Loss of the paternal program (DLK1, RTL1, DIO3) plus gain of the maternal program (MEG3/GTL2, MEG8, RTL1as, miRNAs/snoRNAs) produces TS14 [PMID: 38715103].

- **DLK1** (HGNC:2907; OMIM *176290) — the principal driver of the precocious-puberty and adiposity phenotype. "Loss-of-function mutations in DLK1 … have been linked to central precocious puberty (CPP) and increased body fat in girls" [PMID: 42677749].
- **MEG3/GTL2** (HGNC:14575), **MEG8**, **RTL1/RTL1as** (HGNC:35814), **DIO3** — maternally or paternally expressed cluster members contributing to the imbalance.

**Pathogenic variants / lesion classes.**

| Mechanism | Lesion class | Approx. frequency (Geoffron, n=28) | Consequence |
|---|---|---|---|
| IG-DMR/MEG3-DMR epimutation | Primary epigenetic LOM | 60.7% | Silences paternal DLK1/RTL1 |
| upd(14)mat | Whole-chromosome UPD (structural) | 28.6% | Loss of paternal alleles |
| Paternal 14q32 microdeletion | Structural deletion | 10.7% | Loss of paternal copy |

"Seventeen (60.7%) patients showed loss of methylation of the MEG3/DLK1 intergenic differentially methylated region by epimutation. Eight (28.6%) patients had maternal uniparental disomy of chromosome 14 and three (10.7%) had a paternal deletion in 14q32.2" [PMID: 29659920]. Proportions differ by cohort and referral pattern; in the 60-patient Japanese cohort upd(14)mat predominated (31/60) [PMID: 39693239].

**Variant classification / origin.** The lesions are germline/constitutional (not somatic). Deletions are classed pathogenic; epimutations and UPD are pathogenic epigenetic/structural events rather than ACMG sequence variants. Allele-frequency databases (gnomAD etc.) are not applicable to UPD/epimutation. A rare novel structural mechanism — **interchromosomal template-switching** forming DUP-TRP/INV-DUP complex rearrangements and generating segmental UPD(14)mat — has been described: "these CGRs may lead to genetic abnormalities in carriers due to dosage-sensitive genes mapping within the copy-number variant regions" [PMID: 31014393].

**Functional consequence.** Net effect is **loss of function of paternally expressed genes** (DLK1/RTL1/DIO3) with **gain of expression of maternally expressed non-coding RNAs**.

**Modifier genes.** No robust modifier genes are established. MLID can co-involve machinery genes affecting multiple loci [PMID: 35266280]. In SRS, pathogenic *PLAG1* variants secondarily deregulate the MEG8:Int2-DMR of the 14q32 cluster, connecting this domain to a wider growth-disorder network [PMID: 41276848].

**Epigenetic information.** The germline **IG-DMR** (methylated on the paternal allele) hierarchically controls imprinting across the domain, with the somatic **MEG3-DMR** downstream; paternal loss of IG-DMR methylation is the unifying biomarker of TS14 [PMID: 18471925; PMID: 25351781].

**Chromosomal abnormalities.** upd(14)mat (± mosaic trisomy 14 or small supernumerary marker chromosome 14) and paternal 14q32 microdeletions [PMID: 33746039; PMID: 30181735].

---

## Section 5 — Environmental Information

TS14 has **no established toxic, occupational, pollution, dietary, or infectious cause.** Environmental relevance is confined to (a) ART-associated epimutation risk during epigenetic reprogramming windows [PMID: 41153459; PMID: 39889767] and (b) demonstration that the *DLK1-MEG3* methylation state is modifiable by gestational stress such as preeclampsia [PMID: 30234781]. No infectious agents are implicated.

---

## Section 6 — Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)

1. A parent-of-origin lesion at 14q32.2 occurs — **upd(14)mat**, **paternal IG-DMR/MEG3-DMR epimutation**, or **paternal 14q32 microdeletion** — *leads to* loss of the paternal allele's contribution across the domain [PMID: 38715103].
2. Loss of paternal IG-DMR methylation *results in* silencing of the paternally expressed protein-coding genes **DLK1, RTL1, DIO3** and biallelic activation of the maternally expressed non-coding RNAs **MEG3, MEG8, RTL1as** and the embedded miRNA/snoRNA cluster [PMID: 18471925; PMID: 25351781].
3. **Loss of DLK1** (a Notch-pathway non-canonical ligand) *leads to* dysregulated GnRH-axis timing and altered adipogenesis, *resulting in* **central precocious puberty** and **increased body fat** [PMID: 42677749]. (The precise circuit is still being resolved and appears to act up- or downstream of GnRH neurons — *inferred* from iPSC modelling [PMID: 40924042].)
4. Loss of paternal gene dosage across the domain (*DLK1/RTL1*) *results in* impaired fetal/placental growth signalling, *leading to* **pre- and postnatal growth restriction** and **small hands/feet** (*inferred* from mouse upd(12) and *Dlk1*-null models) [PMID: 17449025; PMID: 42677749].
5. Reduced muscle maturation and connective-tissue/skeletal effects *lead to* **neonatal hypotonia and feeding difficulties** (*inferred* from the mouse upd(12) muscle/bone phenotype) [PMID: 17449025].
6. Loss of DLK1's restraint on adipogenesis plus later positive energy balance *leads to* **truncal obesity**, which *results in* **dyslipidemia and type 2 diabetes** in later life (though hypercholesterolemia/diabetes can precede overt obesity) [PMID: 39693239; PMID: 26395259].

Where the mechanism **branches:** the identical structural deletion produces **TS14 if paternally inherited** but the mirror disorder **Kagami-Ogata syndrome if maternally inherited** — opposite dosage, opposite (overgrowth) phenotype [PMID: 39210340].

### Supporting mechanistic detail

- **Molecular pathways.** DLK1 is a non-canonical Notch ligand; its activation during neuronal differentiation induces Wnt-pathway genes and alters neural fate, linking DLK1 dosage to neurodevelopment and pubertal timing [PMID: 40924042]. RTL1 is reciprocally regulated by RTL1as-encoded microRNAs: "these results suggest that RTL1as-encoded microRNA functions as a repressor of RTL1" [PMID: 22917972].
- **Cellular processes.** Skeletal-muscle maturation, bone formation, placental growth/organization, adipocyte differentiation, and GnRH-neuron ontogeny [PMID: 17449025; PMID: 40924042]. The domain's miRNAs (e.g., miR-127-3p) regulate cell-cycle arrest/senescence in model systems [PMID: 33279585].
- **Protein dysfunction.** Loss of function of DLK1 (and RTL1/DIO3 proteins). DIO3 is a deiodinase affecting local thyroid-hormone metabolism — a plausible contributor to growth/metabolic features (*inferred*).
- **Metabolic changes.** Increased adiposity, dyslipidemia, and early insulin resistance/T2DM [PMID: 39693239].
- **Suggested ontology terms.** GO: GO:0007219 (Notch signaling), GO:0045444 (fat cell differentiation), GO:0001701 (in utero embryonic development). CL: CL:0000136 (adipocyte), CL:0000187 (muscle cell), CL:0000617 (GnRH neuron, approximate). CHEBI: cholesterol (CHEBI:16113), glucose (CHEBI:17234).

---

## Section 7 — Anatomical Structures Affected

- **Organ/system level.** Endocrine system (hypothalamic-pituitary-gonadal axis — precocious puberty; metabolic/endocrine — obesity, dyslipidemia, T2DM); musculoskeletal system (hypotonia, short stature, small hands/feet); nervous system (motor/language delay, mild ID); digestive (neonatal feeding difficulties); and the placenta prenatally. Fatty-liver disease has been reported as a newer-recognized feature [PMID: 33746039].
- **Tissue/cell level.** Skeletal muscle, bone/connective tissue, adipose tissue, and GnRH neurons are the principal targets (*inferred* from model organisms) [PMID: 17449025; PMID: 40924042].
- **Subcellular level.** DIO3 and thyroid-hormone handling implicate cytoplasmic/membrane compartments; the central lesion is nuclear/chromatin (DMR methylation). GO cellular-component: GO:0005634 (nucleus, site of imprinting lesion).
- **Localization / lateralization.** Effects are systemic and bilateral/symmetric; body asymmetry (characteristic of SRS) is generally absent in TS14, aiding differentiation [PMID: 25351781].
- **Suggested UBERON terms.** UBERON:0001013 (adipose tissue), UBERON:0001134 (skeletal muscle), UBERON:0002107 (liver), UBERON:0001898 (hypothalamus), UBERON:0000992 (ovary), UBERON:0001987 (placenta).

---

## Section 8 — Temporal Development

- **Onset.** Congenital/neonatal: growth restriction is prenatal; hypotonia and feeding difficulties present at birth. Onset is insidious/chronic rather than acute.
- **Progression.** Core dysmorphic/growth features are stable and non-progressive. Puberty becomes precocious in childhood (mean menarche ~10 years 2 months) [PMID: 24891339]. The metabolic phenotype is progressive and age-dependent — hypercholesterolemia from ≥6 years, diabetes from ≥9 years [PMID: 39693239].
- **Disease course.** Chronic and lifelong but compatible with normal life expectancy and favourable adult function [PMID: 39693239].
- **Critical periods / intervention windows.** Infancy/early childhood for feeding support and growth-hormone initiation (benefit shown with early start); pre-pubertal window for GnRH-analogue therapy; lifelong metabolic surveillance thereafter [PMID: 36977395; PMID: 39693239].

---

## Section 9 — Inheritance and Population

- **Epidemiology.** Exact prevalence and incidence are **unknown**; TS14 is rare and recognized as under-diagnosed, detected in ~2% of patients referred for PWS or SRS testing [PMID: 29159982; PMID: 24891339].
- **Inheritance pattern.** Most cases are **sporadic/de novo** (upd(14)mat from maternal nondisjunction + trisomy rescue; sporadic epimutation). **Deletion-based cases are Mendelian with a parent-of-origin effect** — paternal transmission → TS14; maternal transmission of the same deletion → Kagami-Ogata syndrome [PMID: 39210340].
- **Penetrance / expressivity.** High penetrance for the core phenotype among those with the lesion; expressivity is variable. No genetic anticipation (not a repeat-expansion disorder).
- **Germline mosaicism / founder effects / consanguinity.** No established founder effects; consanguinity is not a driver (this is not autosomal-recessive). Mosaic trisomy 14 can coexist with upd(14)mat [PMID: 30181735; PMID: 33746039].
- **Population demographics.** No strong ethnic/geographic predilection; cases are reported across European, Japanese, and Chinese populations [PMID: 39693239; PMID: 42026594]. No consistent sex bias is established, although precocious-puberty ascertainment skews some cohorts toward girls.

---

## Section 10 — Diagnostics

**Tiered molecular approach** (all three mechanisms share MEG3-DMR hypomethylation):

1. **First-line — methylation analysis** of the MEG3/DLK1 IG-DMR and MEG3-DMR by methylation-specific MLPA (MS-MLPA; ME032/ME034 kits) or bisulfite pyrosequencing detects the hypomethylation common to all three mechanisms [PMID: 40229547; PMID: 25351781].
2. **Microsatellite / SNP-array genotyping** of parent–child trios distinguishes upd(14)mat [PMID: 33746039].
3. **MLPA / chromosomal microarray / FISH** detect paternal 14q32 microdeletions [PMID: 40229547].

**Prenatal diagnosis.** NIPT followed by amniotic MS-MLPA/CMA/FISH can detect imprinted 14q32 abnormalities, including recurrent KOS/TS14 in at-risk families [PMID: 40229547; PMID: 39210340].

**Clinical/laboratory findings.** Lab monitoring for lipids and glucose given cardiometabolic risk; endocrine evaluation (LH/FSH, bone age) for precocious puberty.

**Differential diagnosis.** Silver-Russell syndrome (11p15/upd(7)mat), Prader-Willi syndrome (15q11-q13), and Schaaf-Yang syndrome (*MAGEL2*), distinguished by locus-specific methylation testing. "Most patients with 14q32.2 disruption fulfill the criteria for a clinical diagnosis of SRS" [PMID: 29659920], and "The most common genetic diagnoses were Temple syndrome (formerly known as maternal uniparental disomy 14), Schaaf-Yang syndrome…" in PWS-like cohorts [PMID: 34460908]. Testing for TS14 is recommended when PWS/SRS testing is negative [PMID: 36362517].

---

## Section 11 — Outcome / Prognosis

**Survival and cognition are generally favourable.** Life expectancy is essentially normal; there are no TS14-specific mortality data indicating reduced survival. In the 60-patient Japanese cohort, "42.9% of patients were enrolled in special classes in childhood, whereas 98.2% of patients attended college or had jobs in adulthood" [PMID: 39693239]. Median IQ is ~85–91 [PMID: 36362517].

**Morbidity is cardiometabolic.** Long-term risks: intellectual/developmental disability 21.6%, neurodevelopmental disorders 21.6%, obesity 20.0%, hypercholesterolemia 26.5% (≥6 y), and diabetes mellitus 12.8% (≥9 y) [PMID: 39693239]. Importantly, hypercholesterolemia and diabetes sometimes preceded obesity and were controllable with oral medication, underscoring the need for early metabolic surveillance [PMID: 39693239; PMID: 26395259].

**Prognostic factors.** Earlier diagnosis permits earlier GH/GnRH-analogue intervention and metabolic monitoring, improving growth and (likely) cardiometabolic outcomes. Final adult height without treatment is reduced (median ~ −2.04 SDS) [PMID: 24891339].

---

## Section 12 — Treatment

Management is **supportive, multidisciplinary, and non-curative** — no disease-modifying or gene-directed therapy exists.

| Intervention | Evidence / effect | Source | NCIT (suggested) |
|---|---|---|---|
| **Recombinant growth hormone (rhGH)** | 1 yr: height +1.31 SDS, HV 5.30 cm/yr. 5 yr: height SDS −1.78 → +0.11; fat-mass% SDS fell, lean-body-mass SDS rose | PMID: 30836360; PMID: 36977395 | Recombinant Human Growth Hormone (NCIT:C1762) |
| **GnRH-analogue therapy** | Ameliorated central precocious puberty in 32/60 patients | PMID: 39693239 | GnRH Analogue |
| **Neonatal tube/supportive feeding** | For feeding difficulties/failure to thrive | PMID: 26395259 | Enteral Nutrition (NCIT:C15190) |
| **Physiotherapy / OT / speech therapy** | For hypotonia, motor and language delay | PMID: 36362517 | Rehabilitation Therapy (NCIT:C15917) |
| **Metabolic management (statins/oral hypoglycemics, diet)** | Dyslipidemia/early T2DM controllable with oral medication | PMID: 39693239 | — |

GH response in TS14 is "similar to the response in patients treated under the small for gestational age indication" [PMID: 30836360]. Over 5 years, "mean (95% CI) height SDS increased significantly during 5 years of GH treatment from -1.78 (-2.52; -1.04) to 0.11 (-0.66; 0.87). Fat mass percentage SDS decreased significantly during the first year of GH, and lean body mass (LBM) SDS and LBM index increased significantly" [PMID: 36977395]. No pharmacogenomic, gene-therapy, cell-therapy, RNA-based, immunotherapy, or TS14-specific surgical treatments are established.

---

## Section 13 — Prevention

- **Primary prevention.** None available for the genetic lesion. Counselling about advanced-maternal-age nondisjunction risk and ART-associated imprinting-defect risk is relevant [PMID: 30181735; PMID: 41153459].
- **Secondary prevention.** Early recognition via testing TS14 in PWS/SRS-like infants with negative primary testing [PMID: 36362517]; prenatal detection in deletion-carrier families (NIPT + confirmatory MS-MLPA/CMA/FISH) [PMID: 40229547].
- **Tertiary prevention.** Lifelong surveillance and management of growth and cardiovascular risk factors, as explicitly recommended: "improved diagnosis and long-term monitoring, especially of growth and cardiovascular risk factors, is required" [PMID: 24891339].
- **Genetic counselling.** Essential for deletion carriers given the parent-of-origin recurrence of TS14 vs KOS [PMID: 39210340]. No vaccine or public-health/environmental prevention applies.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy / orthology.** The human 14q32 domain is syntenic with **mouse distal chromosome 12** (*Mus musculus*, NCBI Taxon 10090). Orthologues: *Dlk1*, *Rtl1/Peg11*, *Dio3*, *Meg3/Gtl2*, *Meg8*, *Rian/Mirg* [PMID: 18471925].
- **Natural disease in animals.** No well-characterized naturally occurring Temple-syndrome analogue is documented in companion animals or wildlife (no evidence found).
- **Comparative biology / evolutionary conservation.** The imprinted architecture and parent-of-origin regulation of the DLK1-DIO3 domain are conserved between human and mouse, making the mouse a valid model of the dosage imbalance [PMID: 18471925; PMID: 17449025].
- **Transmission.** Not applicable — TS14 is non-infectious and non-zoonotic.

---

## Section 15 — Model Organisms

- **Mouse uniparental disomy chromosome 12 [upd(12)].** Reproduces the TS14-type dosage imbalance and causes "defects in skeletal muscle maturation, bone formation, placenta size and organization and prenatal lethality" [PMID: 17449025] — recapitulating the muscle/growth/placental aspects of TS14; prenatal lethality is a limitation not seen in human TS14.
- **Dlk1-knockout mouse.** Shows growth retardation, increased adiposity/obesity, and metabolic changes recapitulating core TS14 features; a recent study found "Dlk1-deficient mice achieve puberty despite low body weight and low levels of leptin and kisspeptin," informing the DLK1–puberty link [PMID: 42677749].
- **Human iPSC / stem-cell models.** hPSC *DLK1*-edited lines reveal a dual role of DLK1 in GnRH neuron ontogeny, with timing-dependent effects on GnRH lineage commitment [PMID: 40924042]. iPSC models of imprinting disorders are feasible but prone to culture-induced hypermethylation of the MEG3/DLK1:IG-DMR unless specialized media/hypoxic conditions are used [PMID: 36578048].
- **In-vitro domain biology.** Mouse chromosome-12 miRNA (e.g., miR-127-3p) studies illuminate cell-cycle/senescence regulation by the cluster [PMID: 33279585].
- **Limitations.** Full upd(12) mouse shows prenatal lethality; single-gene (*Dlk1*) models capture the metabolic/pubertal axis but not the full multi-gene imbalance; iPSC models require careful methylation control.
- **Resources.** MGI (mouse), Alliance of Genome Resources.

---

## Mechanistic Model / Interpretation

```
 Paternal 14q32 lesion (upd(14)mat / IG-DMR epimutation / paternal deletion)
                              |
                              v
        Loss of paternal IG-DMR methylation  --> unified biomarker: MEG3-DMR hypomethylation
                              |
        +---------------------+---------------------+
        v                                           v
  Silence paternal genes                    Activate maternal ncRNAs (biallelic)
   DLK1 v , RTL1 v , DIO3 v                  MEG3 ^ , MEG8 ^ , RTL1as ^ , miRNAs ^
        |                                           |
        v                                           v
  DLK1 loss -> GnRH-axis dysregulation       RTL1as miRNA represses RTL1 (reinforces loss)
  + increased adipogenesis                   -> placental/growth effects
        |
        +--> Central precocious puberty (86-89%)
        +--> Pre/postnatal growth restriction, small hands/feet
        +--> Hypotonia, feeding difficulties (muscle immaturity)
        +--> Truncal obesity -> dyslipidemia -> early T2DM

 PARENT-OF-ORIGIN BRANCH (deletion carriers):
   Paternal transmission --> TS14 (loss of paternal program)
   Maternal transmission --> Kagami-Ogata syndrome (mirror / overgrowth)
```

The unifying insight is **dosage reciprocity**: the three mechanisms converge on the same methylation biomarker and the same net dosage imbalance, while the DLK1-DIO3 domain's sensitivity to parent-of-origin makes TS14 and KOS mechanistic mirror images.

---

## Evidence Base (key literature)

| PMID | Role |
|---|---|
| [24891339](https://pubmed.ncbi.nlm.nih.gov/24891339/) | Eponym origin; pooled phenotype frequencies & growth metrics from 51 cases |
| [32592473](https://pubmed.ncbi.nlm.nih.gov/32592473/) | Defines 14q32 locus, parent-of-origin mechanisms, TS14↔KOS relationship |
| [38715103](https://pubmed.ncbi.nlm.nih.gov/38715103/) | Three mechanisms; gene-dosage imbalance; clinical features |
| [29659920](https://pubmed.ncbi.nlm.nih.gov/29659920/) | Mechanism frequencies; SRS overlap |
| [39693239](https://pubmed.ncbi.nlm.nih.gov/39693239/) | Largest cohort (n=60) — phenotype frequencies, morbidity, outcome, treatment |
| [30836360](https://pubmed.ncbi.nlm.nih.gov/30836360/) | rhGH 1-year growth response |
| [36977395](https://pubmed.ncbi.nlm.nih.gov/36977395/) | Long-term (5-yr) GH/body-composition benefit |
| [42026594](https://pubmed.ncbi.nlm.nih.gov/42026594/) | Chinese cohort phenotype & GH therapy |
| [42677749](https://pubmed.ncbi.nlm.nih.gov/42677749/) | DLK1 LOF → CPP & adiposity (mouse) |
| [40924042](https://pubmed.ncbi.nlm.nih.gov/40924042/) | DLK1 mechanism in GnRH neuron ontogeny; iPSC model |
| [18471925](https://pubmed.ncbi.nlm.nih.gov/18471925/) | Domain architecture; IG-DMR hierarchy |
| [17449025](https://pubmed.ncbi.nlm.nih.gov/17449025/) | Mouse upd(12) model phenotype |
| [22917972](https://pubmed.ncbi.nlm.nih.gov/22917972/) | RTL1as miRNA represses RTL1 |
| [39210340](https://pubmed.ncbi.nlm.nih.gov/39210340/) | Parent-of-origin recurrence (TS14 mother → KOS offspring) |
| [31014393](https://pubmed.ncbi.nlm.nih.gov/31014393/) | Novel template-switching mechanism for UPD(14)mat |
| [29159982](https://pubmed.ncbi.nlm.nih.gov/29159982/) | Under-diagnosis rate (2.1% of PWS referrals) |
| [40229547](https://pubmed.ncbi.nlm.nih.gov/40229547/) | Diagnostic modalities (MS-MLPA, FISH, CMA, NIPT) |
| [34460908](https://pubmed.ncbi.nlm.nih.gov/34460908/) | Synonym (maternal UPD14); PWS-like differential dx |
| [36362517](https://pubmed.ncbi.nlm.nih.gov/36362517/) | Body composition, IQ, testing recommendation (n=15) |
| [26395259](https://pubmed.ncbi.nlm.nih.gov/26395259/) | Isolated epimutation case; metabolic risk |
| [41153459](https://pubmed.ncbi.nlm.nih.gov/41153459/) | ART epimutation risk |
| [35266280](https://pubmed.ncbi.nlm.nih.gov/35266280/) | Multilocus imprinting disturbance (11p15 + 14q32) |
| [30234781](https://pubmed.ncbi.nlm.nih.gov/30234781/) | Gene–environment interaction (preeclampsia, DLK1-MEG3) |
| [30181735](https://pubmed.ncbi.nlm.nih.gov/30181735/) | Trisomy-rescue origin (TS14 + mosaic trisomy 14) |

---

## Limitations and Knowledge Gaps

1. **Epidemiology is undefined.** No reliable prevalence or incidence figures exist; TS14 is recognized as under-diagnosed [PMID: 24891339; PMID: 29159982].
2. **Ascertainment bias.** Reported mechanism proportions and phenotype frequencies vary widely between cohorts (e.g., upd(14)mat ~29% vs ~52%) because referral routes (precocious puberty vs growth clinics vs PWS/SRS testing) differ [PMID: 29659920; PMID: 39693239].
3. **Mechanistic attribution is partly inferred.** The specific contribution of each gene (DLK1 vs RTL1 vs DIO3) to each clinical feature relies heavily on mouse/iPSC models; the exact pathway from DLK1 loss to CPP remains incompletely resolved and appears to act up-/downstream of GnRH neurons [PMID: 40924042].
4. **Treatment evidence is limited and short-to-medium term.** GH and GnRH-analogue data derive from small, retrospective, uncontrolled cohorts; long-term adult cardiometabolic and final-height outcomes with treatment are not fully quantified.
5. **No disease-modifying therapy or validated biomarkers of progression** exist, and there are no TS14-specific quality-of-life instruments.
6. **Sex-ratio and population-genetic data are sparse**, and there are no natural animal-disease analogues.

---

## Proposed Follow-up Experiments / Actions

1. **Establish a prospective international TS14 registry** with uniform molecular and phenotyping protocols to resolve true prevalence, mechanism-specific genotype–phenotype correlations, and long-term cardiometabolic outcomes.
2. **Controlled/longitudinal treatment studies** of rhGH and GnRH-analogue therapy with adult final-height, body-composition, lipid, and glucose endpoints; test whether early GH initiation (<2 y) modifies metabolic trajectory.
3. **Dissect DLK1's CPP mechanism** using conditional/temporally controlled DLK1 models and patient iPSC-derived hypothalamic/GnRH-neuron organoids to define whether the pubertal defect is pre- or post-synaptic to GnRH neurons [building on PMID: 40924042].
4. **Define metabolic-surveillance thresholds**: prospectively characterize the onset sequence of hypercholesterolemia, obesity, and T2DM to set evidence-based screening intervals, given that lipids/glucose can precede obesity [PMID: 39693239].
5. **Quantify ART-associated epimutation risk specifically for 14q32** in large ART-conceived cohorts to inform preconception and prenatal counselling [PMID: 41153459].
6. **Develop methylation-based multi-locus diagnostic panels** (and refine NIPT workflows) to improve early/prenatal detection and reduce diagnostic delay, especially in PWS/SRS-like infants with negative first-line testing [PMID: 40229547; PMID: 36362517].

---

*Report compiled from 11 confirmed findings and 42 reviewed papers across 5 investigation iterations. Evidence types: human clinical cohorts/case series (primary), model-organism (mouse upd(12), Dlk1-KO), and in-vitro (iPSC, placental) studies.*


## Artifacts

- [OpenScientist final report](Temple_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Temple_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 30 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 12 |
| Quoted claims found in source | 11 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 30 |
| On topic | 16 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:42677749` *(abstract only)*: "Loss-of-function mutations in DLK1 … have been linked to central precocious puberty (CPP) and increased body fat in girls"
  - closest text in source: "Loss-of-function mutations in DLK1, encoding Delta Like Non-Canonical Notch Ligand 1, have been linked to central precocious puberty (CPP) and increased body fat in girls, suggesting a role in the connection between metabolism and reproduction"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:39889767` (2 mentions) - Effects of Assisted Reproductive Technology on Genetics, Obstetrics, and Neonatal Outcomes.
  - shared terms: disorder

Weighed against this report's own most characteristic terms: `ts14`, `dlk1`, `upd`, `growth`, `q32`, `mechanism`, `cohort`, `metabolic`, `puberty`, `phenotype`, `mat`, `domain`, `model`, `methylation`, `disorder`, `precocious`, `gene`, `risk`, `rtl1`, `epimutation`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 29 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 11 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0100507` (2 mentions) - the report calls it "MONDO"; MONDO calls it **multiple congenital anomalies due to 14q32.2 paternally expressed gene defect**
- `CL:0000617` (1 mention) - the report calls it "GnRH neuron, approximate"; CL calls it **GABAergic neuron**
- `GO:0005634` (1 mention) - the report calls it "nucleus, site of imprinting lesion"; GO calls it **nucleus**
- `NCIT:C1762` (1 mention) - the report calls it "Recombinant Human Growth Hormone"; NCIT calls it **Raloxifene Hydrochloride**
- `NCIT:C15190` (1 mention) - the report calls it "Enteral Nutrition"; NCIT calls it **Needle Biopsy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001511` (1 mention) - the report calls it "Intrauterine / prenatal growth restriction"; HP calls it **Intrauterine growth retardation**, and lists "Intrauterine growth restriction" among its other names
- `HP:0004322` (1 mention) - the report calls it "Postnatal short stature"; HP calls it **Short stature**
- `HP:0001252` (1 mention) - the report calls it "Muscular hypotonia"; HP calls it **Hypotonia**, and lists "Muscular hypotonia" among its other names
- `HP:0000750` (1 mention) - the report calls it "Delayed speech / language"; HP calls it **Delayed speech and language development**, and lists "Delayed speech" among its other names
- `HP:0001956` (1 mention) - the report calls it "Truncal obesity / weight gain"; HP calls it **Truncal obesity**
- `HP:0000826` (1 mention) - the report calls it "Central precocious puberty"; HP calls it **Precocious puberty**
- `HP:0001249` (1 mention) - the report calls it "Intellectual/developmental disability (mild)"; HP calls it **Intellectual disability**
- `HP:0000819` (1 mention) - the report calls it "Diabetes mellitus (type 2)"; HP calls it **Diabetes mellitus**
- `GO:0007219` (1 mention) - the report calls it "Notch signaling"; GO calls it **Notch signaling pathway**
- `UBERON:0001134` (1 mention) - the report calls it "skeletal muscle"; UBERON calls it **skeletal muscle tissue**, and lists "skeletal muscle" among its other names
- `NCIT:C15917` (1 mention) - the report calls it "Rehabilitation Therapy"; NCIT calls it **Arterial Embolization**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.