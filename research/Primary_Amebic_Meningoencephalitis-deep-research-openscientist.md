---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-03T08:57:36.274923'
end_time: '2026-11-03T09:09:20.468774'
duration_seconds: 704.19
template_file: templates/disease_pathophysiology_research.md
template_sha: f452f0a9c7e3536175154b9683c45663f686f283
template_variables:
  disease_name: Primary Amebic Meningoencephalitis
  mondo_id: MONDO:0000290
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: Naegleria fowleri infection
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
citation_count: 29
reference_validation:
  total_references: 31
  verified: 31
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 31
  on_topic: 25
  validator_version: 0.5.1
term_validation:
  total_terms: 42
  verified: 40
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 7
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0000290
    reported_labels:
    - if available
    ontology_label: primary amebic meningoencephalitis
  - term_id: HP:0003112
    reported_labels:
    - abnormal CSF
    ontology_label: Abnormal circulating amino acid concentration
  - term_id: CL:0000540
    reported_labels:
    - neurons
    - "Tissue/cell level:** nervous tissue \u2014 **neurons"
    ontology_label: neuron
  - term_id: UBERON:0000955
    reported_labels:
    - Brain
    - Primary organ:** **Brain
    ontology_label: brain
  - term_id: UBERON:0001675
    reported_labels:
    - cribriform plate / olfactory nerve
    ontology_label: trigeminal ganglion
  - term_id: CL:0000125
    reported_labels:
    - astrocytes/glia
    ontology_label: glial cell
  labels_variant: 2
  unresolvable_prefixes:
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Primary_Amebic_Meningoencephalitis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Primary_Amebic_Meningoencephalitis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Primary Amebic Meningoencephalitis
- **MONDO ID:** MONDO:0000290 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** Naegleria fowleri infection
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Primary Amebic Meningoencephalitis** covering all of the
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

# Primary Amebic Meningoencephalitis (PAM) — Comprehensive Disease Profile

**MONDO:** MONDO:0000290 · **Category:** Infectious disease · **Causal agent:** *Naegleria fowleri* (free-living thermophilic amoeba; NCBI Taxon:5763)

> **Causal "gene" note.** PAM is **not a human genetic disease** and has **no human causal gene**. The template's "Causal gene(s): not recorded" field is correct and expected: the disease is produced by infection with the free-living amoeba ***Naegleria fowleri***. Where this report refers to "causal genes," these are **pathogen (amoeba) virulence genes** (e.g., *nfa1*, naegleriapore/*Npa*, cathepsin/serine-protease genes), not host germline genes. All subsequent sections should be read with the pathogen as the etiologic agent.

---

## 1. Disease Information

**Overview.** Primary amebic meningoencephalitis (PAM) is a rapidly progressive, fulminant, almost universally fatal infection of the central nervous system caused by the thermophilic, free-living amoeba *Naegleria fowleri* ("brain-eating amoeba"). Infection occurs when warm fresh water containing the amoeba is forced into the nose; the organism crosses the cribriform plate along the **olfactory nerve** and invades the brain, producing a hemorrhagic, necrotizing meningoencephalitis (PMID: 22919000). Death typically occurs within ~1–2 weeks of symptom onset, with a case-fatality rate >95–97% (PMID: 39432113).

**Key identifiers.**
- **Mondo:** MONDO:0000290
- **ICD-10:** B60.2 (Naegleriasis / primary amebic meningoencephalitis)
- **ICD-11:** 1F55 (Acanthamoebiasis / free-living amoeba infections) → *Naegleria* meningoencephalitis
- **MeSH:** D008836 *Meningoencephalitis*; organism MeSH D009258 *Naegleria*; D054314 *Central Nervous System Protozoal Infections*
- **SNOMED CT:** 36649002 (Primary amebic meningoencephalitis)
- **Orphanet:** Not a classic rare-genetic ORPHA entry; covered under free-living amoebic infections
- **OMIM:** Not applicable (no Mendelian locus)
- **NCBI Taxonomy (agent):** *Naegleria fowleri* Taxon:5763

**Synonyms / alternative names.** Naegleriasis; *Naegleria fowleri* infection; "brain-eating amoeba" infection; amebic meningoencephalitis (primary); PAM; PAME.

**Information source type.** Disease-level, aggregated from **case reports, CDC Free-Living Ameba (FLA) surveillance, and systematic reviews** (PMID: 32369575, 26582886). Because PAM is extremely rare, there are no large EHR cohorts; evidence is predominantly individual case/autopsy data pooled at the disease level.

---

## 2. Etiology

**Primary cause (infectious).** The sole cause is infection with *Naegleria fowleri*, a thermophilic free-living amoeba found worldwide in warm fresh water (lakes, ponds, rivers, hot springs, geothermal water) and in inadequately disinfected recreational/treated water (pools, splash pads, tap water) (PMID: 40146665, 22919000, 27123690). The amoeba has three life stages: **trophozoite** (invasive, feeding), **flagellate** (transient), and **cyst** (environmentally resistant). Only the trophozoite invades tissue.

**Route of entry.** Intranasal instillation of contaminated water (swimming, diving, splashing, hot-spring bathing, **religious ablution/wudu**, and **nasal/sinus irrigation with neti pots using contaminated tap water**) (PMID: 22919000, 21291600). In Karachi, Pakistan, a cluster of 13 PAM cases occurred in people with **no aquatic exposure**, with infection attributed to **ablution with tap water**; N. fowleri was subsequently detected in Karachi municipal tap water (11/39 samples) under conditions of high temperature, low chlorine, and high coliform counts (PMID: 21291600, 39780139).

**Risk factors (environmental/behavioral).**
- **Warm-freshwater nasal exposure** — strongest risk; swimming/diving is the most common exposure and lakes/ponds/reservoirs the most common source (PMID: 32369575).
- **Male sex** (~75–76% of cases) (PMID: 32369575, 26582886).
- **Young age** (children/adolescents; median 12–14 years) (PMID: 32369575, 26582886).
- **Warm climate / summer months / southern latitudes**, with geographic expansion northward attributed to climate warming (PMID: 22919000, 26582886).
- **Inadequately disinfected treated water** (splash pads, pools, household plumbing) (PMID: 40146665, 22919000).
- **Nasal irrigation with non-sterile tap water** (PMID: 22919000).

**Genetic risk/protective factors (host).** None established — PAM is not a heritable disorder and no human susceptibility/protective loci are validated. (Not applicable.)

**Protective factors (environmental).** Keeping water out of the nose; using nose clips; using sterile/distilled/boiled water for nasal irrigation; adequate water chlorination (free chlorine ≥1 ppm) — all reduce risk (CDC guidance; PMID: 40146665).

**Gene–environment interactions (host).** Not applicable (no human genetic component). The relevant interaction is **pathogen virulence gene expression × host nasal exposure/temperature**: thermophilic growth (optimal ~42–45 °C) and virulence-gene upregulation on contact with host cells drive invasion (PMID: 40096149, 33843581).

---

## 3. Phenotypes

PAM is clinically **biphasic**, progressing from nonspecific flu-like illness to fulminant meningoencephalitis (PMID: 26582886). Onset is **acute**, typically 1–9 days (median ~5 days) after exposure; course is **rapidly progressive**, death in a median of ~5 days from symptom onset.

| Phenotype | Type | Frequency | HPO suggestion |
|---|---|---|---|
| Fever | symptom/sign | ~79–92% | HP:0001945 Fever |
| Headache (severe, frontal) | symptom | ~58–83% | HP:0002315 Headache |
| Nausea / vomiting | symptom | common/high | HP:0002018 Nausea; HP:0002013 Vomiting |
| Nuchal rigidity / meningismus | sign | common | HP:0031179 Nuchal rigidity |
| Altered mental status / confusion | sign | ~50%+ | HP:0001298 Encephalopathy |
| Seizures | sign | ~41% | HP:0001250 Seizure |
| Photophobia | symptom | common | HP:0000613 Photophobia |
| Anosmia / altered taste/smell | sign | early, characteristic | HP:0000458 Anosmia |
| Coma | sign | late | HP:0001259 Coma |
| Cranial nerve palsies, raised ICP | sign | late | HP:0002493 Upper motor neuron dysfunction; HP:0002118 (↑ICP-related) |

Frequencies from Indian systematic review (fever 79.2%, headache 58.3%, seizures 41.6%; PMID: 42764041) and Kerala series (fever 91.7%, headache 83.3%, altered mental status 50%; PMID: 41873284).

**Laboratory-abnormality phenotypes (CSF).** Resembles bacterial meningitis: elevated opening pressure, **neutrophilic pleocytosis** (median 2400 cells/µL), **low glucose** (median 23 mg/dL), **high protein** (median 365 mg/dL); **motile trophozoites on wet mount** are diagnostic (PMID: 26582886). HPO: HP:0002922 Increased CSF protein; HP:0003112 (abnormal CSF); low CSF glucose.

**Severity / progression.** Uniformly **severe** and **progressive**; essentially no stable or episodic course. **Quality-of-life impact:** for the few survivors, outcomes range from full recovery to severe neurological sequelae (cognitive, motor deficits); for the vast majority the outcome is death, so QoL instruments (EQ-5D/SF-36) are not meaningfully applied at the population level.

---

## 4. Genetic / Molecular Information

**Human causal genes:** **None** (not a genetic disease).

**Pathogen (amoeba) "virulence genes" (the functional equivalent of causal molecular drivers):**
- ***nfa1*** — encodes a ~13.1 kDa pseudopod/food-cup protein central to contact-dependent cytolysis; a validated virulence/vaccine antigen (PMID: 22955499).
- **Naegleriapores / *Npa* (A and B)** — pore-forming, membrane-permeabilizing polypeptides causing host-cell lysis (PMID: 39432113).
- **Cathepsin B and serine/cysteine proteases** — degrade host extracellular matrix and tissue; secreted and packaged in extracellular vesicles (PMID: 39432113, 40312759).
- **Leishmanolysin (GP63-like metalloprotease)** — adhesion/enzymatic virulence, identified in EV proteome (PMID: 40312759).
- **Mp2CL5** membrane protein; **lysozyme, cystatin, hemerythrin** (host-defense evasion, brain migration, lethal infection) (PMID: 40096149).
- **Lectins** mediating adhesion (PMID: 32716210).

**Genome.** *N. fowleri* genome sequenced; comparative genomics distinguishes pathogenic *N. fowleri* from non-pathogenic *N. gruberi*, though several "virulence" homologs are shared, implying regulation/expression (not mere presence) determines pathogenicity (PMID: 33843581, 31797948).

**Variant classification / allele frequency / somatic-vs-germline / modifier genes / epigenetics / chromosomal abnormalities (human):** **Not applicable** — there are no human pathogenic variants, ClinVar entries, gnomAD frequencies, or chromosomal findings for this infectious disease.

---

## 5. Environmental Information

- **Environmental reservoir:** warm fresh water worldwide — lakes, ponds, rivers, hot springs, geothermal discharge, poorly maintained pools/splash pads, and warm tap/plumbing water (PMID: 40146665, 22919000). Thermophilic: thrives up to ~45 °C.
- **Climate sensitivity:** warming water temperatures expand the amoeba's range; northward spread of US cases documented (PMID: 22919000, 26582886).
- **Lifestyle/behavioral factors:** recreational freshwater activities (swimming, diving, water-skiing, splash pads), hot-spring bathing, and **nasal/sinus irrigation** with untreated tap water (PMID: 22919000).
- **Infectious agent (NCBI Taxonomy):** *Naegleria fowleri* (Taxon:5763), phylum Percolozoa, class Heterolobosea. Related non-pathogenic congener: *N. gruberi*. Other pathogenic FLA causing distinct CNS disease: *Acanthamoeba* spp., *Balamuthia mandrillaris* (granulomatous amebic encephalitis), *Sappinia* (PMID: 33843581).

---

## 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating exposure → clinical manifestation):**

1. **Contaminated warm freshwater is forced into the nasal cavity** (swimming, diving, hot-spring bathing, or nasal irrigation) → deposits *N. fowleri* trophozoites on the **olfactory/nasal mucosa** (*demonstrated*, PMID: 22919000).
2. Trophozoites **adhere to nasal mucosa** via lectins/food-cup (Nfa1) structures and begin feeding on epithelium → local mucosal damage (*demonstrated in vitro/animal*, PMID: 32716210, 22955499).
3. Amoebae **migrate along olfactory nerve fibers through the cribriform plate** into the olfactory bulbs (*demonstrated; explains early anosmia*, PMID: 22919000).
4. In the CNS, trophozoites perform **contact-dependent trogocytosis/phagocytosis ("food-cup" ingestion of neural cells)**, driven by **actin dynamics regulated by Arp2/3 and Src kinase** (*demonstrated*, PMID: 40096149).
5. Simultaneously, **contact-independent cytolysis** occurs via secreted and **extracellular-vesicle–delivered virulence factors** — naegleriapores (pore formation), cathepsin B/serine proteases, phospholipases, leishmanolysin — causing **hemolysis, increased membrane permeability, and necrosis** (*demonstrated in vitro*, PMID: 40312759, 39432113).
6. Tissue destruction + amoebic antigens **trigger a massive innate inflammatory response** (neutrophil and eosinophil influx, cytokine release) → **necrotizing, hemorrhagic meningoencephalitis** with cerebral edema (*demonstrated; neutrophils central to host defense*, PMID: 2628288, 27525348).
7. Cerebral edema and inflammation → **raised intracranial pressure**, uncal/tonsillar herniation → **brainstem compression** (*inferred from clinical/autopsy data*, PMID: 25667249).
8. → **Coma and death**, typically within days (*demonstrated clinical outcome*, PMID: 26582886).

**Branch:** Beyond primary olfactory-bulb invasion, autopsy and animal data indicate **extra-CNS hematogenous dissemination** can occur (relevant to transplant-transmission risk) (PMID: 24279908).

**Molecular pathways / cellular processes.**
- Host-cell ingestion: **actin cytoskeleton remodeling (Arp2/3, Src kinase)** — GO:0030041 actin filament polymerization; GO:0006909 phagocytosis; "trogocytosis" (PMID: 40096149).
- Cytolysis: **pore-forming/membrane permeabilization** (naegleriapores) — GO:0051715 cytolysis in another organism; GO:0006887 EV/exocytosis.
- Proteolysis: **cysteine/serine protease activity** — GO:0006508 proteolysis (PMID: 39432113).
- Metabolic shift: brain-passaged amoebae show altered **lipid storage/utilization** vs axenic culture (Raman microspectroscopy) (PMID: 40096149).
- Immune involvement: innate-dominant **neutrophilic/eosinophilic** inflammation; adaptive immunity can be protective in animal models (PMID: 2628288, 646016).

**Tissue-damage mechanisms:** necrosis, hemorrhage, phagocytic "nibbling" of neurons, protease-mediated matrix degradation, oxidative inflammatory injury.

**Molecular profiling (transcriptomics/proteomics).** RNA-seq across life stages shows stage-specific regulation of the cytoskeletal machinery: **nf-profilin** (actin-binding regulator) is high in cysts and membrane-localized, whereas **nf-actin** localizes to cytoplasm, pseudopodia, and **food-cup** structures of trophozoites; during cyst→trophozoite conversion on host-cell contact, profilin falls and actin rises — directly linking the transcriptome to the invasive food-cup apparatus (PMID: 40016342, 36839446). Secretome/EV proteomics identified >1000 proteins including leishmanolysin and serine proteases (PMID: 40312759). Brain-passaged vs axenic amoebae differ metabolically in lipid storage/utilization (Raman spectroscopy) (PMID: 40096149). Transcriptomic profiling of the "brain-eating amoeba" host interaction further catalogs virulence-associated expression (PMID: 39735262). Phylogenomics places *N. fowleri* in phylum Heterolobosea, new order **Naegleriida** (PMID: 39826589).

**Suggested ontology terms:** GO:0006909 (phagocytosis), GO:0030041 (actin polymerization), GO:0006508 (proteolysis), GO:0019835 (cytolysis), GO:0006954 (inflammatory response); CL:0000540 neuron, CL:0000127 astrocyte, CL:0000775 neutrophil; UBERON:0002264 olfactory bulb, UBERON:0000955 brain.

---

## 7. Anatomical Structures Affected

- **Primary organ:** **Brain** (UBERON:0000955), especially **olfactory bulbs** (UBERON:0002264), frontal lobes, and basal cisterns; **meninges** (UBERON:0002360). Nervous system (central).
- **Portal of entry tissue:** **nasal/olfactory epithelium** (UBERON:0001707 nasal cavity; UBERON:0001997 olfactory epithelium) and **cribriform plate / olfactory nerve** (UBERON:0001675).
- **Secondary / disseminated involvement:** rare extra-CNS spread (lung, heart, kidney reported at autopsy), relevant to transplant risk (PMID: 24279908).
- **Tissue/cell level:** nervous tissue — **neurons** (CL:0000540), **astrocytes/glia** (CL:0000125); inflammatory infiltrate of **neutrophils** (CL:0000775) and **eosinophils** (CL:0000771).
- **Subcellular (host damage):** plasma-membrane disruption (pore-forming peptides); for the amoeba, **food cup / pseudopod (amoebic phagocytic structure)**, lysosomes/EVs (GO:0005764 lysosome; GO:1903561 extracellular vesicle).
- **Lateralization:** typically **bilateral** but may begin **asymmetric** reflecting unilateral olfactory-tract seeding; progresses to diffuse cerebral involvement.

---

## 8. Temporal Development

- **Onset:** **Acute**. Incubation ~1–9 days (median ~5) after nasal exposure (PMID: 26582886).
- **Stages:** (i) **Early** — nonspecific flu-like: fever, headache, nausea/vomiting, altered smell/taste; (ii) **Late** — CNS: meningismus, confusion, seizures, focal deficits, coma (PMID: 26582886).
- **Progression rate:** **Rapid/fulminant.** Median time from symptom onset to death ~5 days; most die within 1–2 weeks (PMID: 32369575, 26582886).
- **Course pattern:** monophasic, progressive; no relapsing–remitting or episodic form.
- **Duration/remission:** self-limited only in the sense of rapid death; **treatment-induced survival is rare** and depends on very early recognition (PMID: 25667249).
- **Critical window for intervention:** the first **24–72 hours** after symptom onset — survival correlates with early diagnosis and immediate combination therapy (PMID: 27525348, 25667249).

---

## 9. Inheritance and Population

- **Inheritance:** **Not applicable** (infectious; no germline transmission, penetrance, anticipation, founder effects, or carrier frequency).
- **Incidence/prevalence:** Extremely rare. **~0–8 US cases/year** (CDC); ~381 global cases reported through 2018 (PMID: 32369575); ~142 US cases 1937–2013 (PMID: 26582886). True incidence likely underestimated due to misdiagnosis.
- **Case-fatality rate:** **>95–97%**; only ~7 confirmed survivors globally in the 2018 review (PMID: 32369575, 39432113).
- **Sex ratio:** male-predominant ~3:1 (75–76% male) (PMID: 32369575, 26582886).
- **Age distribution:** predominantly **children and adolescents**, median 12–14 years, though cases span 13 days to 85 years (PMID: 42764041).
- **Geographic distribution:** worldwide in warm climates; US cases concentrated in **southern-tier states** (Texas, Florida — Florida accounts for >25% of US cases) with **northward expansion** (Minnesota, Kansas, Indiana) linked to warming (PMID: 23621053, 22919000). Substantial case loads reported from **Pakistan, India, Australia**, and other warm regions (PMID: 42764041, 41873284). **Pakistan (Karachi)** is notable for a **non-recreational, ablution/tap-water–associated** disease pattern (13-case cluster; N. fowleri confirmed in municipal tap water), reflecting high ambient temperature, under-chlorination, and degraded distribution systems (PMID: 21291600, 39780139).

---

## 10. Diagnostics

- **CSF analysis:** bacterial-meningitis-like profile — **neutrophilic pleocytosis, low glucose, high protein, raised opening pressure** (PMID: 26582886).
- **Direct microscopy (first-line, rapid):** **wet-mount of fresh CSF** showing **motile trophozoites** — positive in 95.8% of Indian cases; Giemsa/Wright/trichrome staining (do NOT rely on Gram stain) (PMID: 42764041, 23710088).
- **Molecular confirmation:** **real-time PCR** of CSF/tissue (CDC) — definitive; **LAMP** assays for rapid water/clinical detection (PMID: 35020127, 25822175). PCR confirmation is underused in resource-limited settings (only 2/24 Indian cases) (PMID: 42764041).
- **Culture:** CSF on non-nutrient agar with *E. coli* overlay; flagellation test (trophozoite→flagellate in distilled water) (PMID: 35020127).
- **Immunologic:** immunohistochemistry/indirect immunofluorescence on tissue; antigen detection.
- **Imaging:** CT/MRI shows nonspecific cerebral edema, basal meningeal enhancement, hemorrhage; often normal early (PMID: 26582886).
- **Clinical criteria / differential diagnosis:** PAM should be suspected in **acute meningoencephalitis with recent freshwater nasal exposure** (PMID: 40146665). **Differential:** bacterial meningitis, viral/herpes encephalitis, fungal meningitis, tuberculous meningitis — distinguished by motile amoebae on wet mount and PCR, and by negative bacterial/viral cultures (PMID: 27123690).
- **Screening:** No asymptomatic screening exists (too rare, too rapid); environmental water testing (PCR/LAMP) supports outbreak investigation (PMID: 25822175).
- **Suggested LOINC concepts:** CSF cell count/differential, CSF glucose, CSF protein, *Naegleria* PCR.

---

## 11. Outcome / Prognosis

- **Mortality:** **>95–97%**; historically near-uniformly fatal (PMID: 32369575, 39432113).
- **Survival:** only a handful of confirmed survivors worldwide; **3 well-documented North American survivors** by mid-2010s (PMID: 25667249, 27525348).
- **Prognostic factors:** **time to diagnosis and treatment** is the dominant determinant; early presentation (flu-like stage), prompt combination antimicrobials, aggressive ICP control, and therapeutic hypothermia are associated with survival (PMID: 25667249, 27525348).
- **Morbidity in survivors:** variable — from near-complete recovery to permanent neurological deficits (cognitive, motor, visual).
- **Complications:** cerebral edema, herniation, raised ICP, seizures, status epilepticus, hydrocephalus (PMID: 25667249).
- **Disease-specific mortality:** essentially all deaths attributable directly to CNS infection within days–weeks.

---

## 12. Treatment

**No single proven cure; management is a multidrug + neurocritical-care bundle started emergently on suspicion.**

- **Amphotericin B** (polyene antifungal; amebicidal) — **backbone**, given **IV and intrathecal/intraventricular**; mainstay in nearly all regimens (used in 91.6% of Indian cases) (PMID: 42764041, 23710088). NCIT: Amphotericin B (C280).
- **Miltefosine** (alkylphosphocholine; investigational, CDC-provided) — added to regimens of recent survivors (PMID: 26679626, 25667249). NCIT: Miltefosine (C61769).
- **Adjunct antimicrobials:** azithromycin, fluconazole (or other azoles), rifampin — commonly combined (PMID: 27525348).
- **Neurocritical care:** aggressive management of **elevated intracranial pressure** using traumatic-brain-injury principles, CSF diversion (intraventricular shunt), and **therapeutic (targeted) hypothermia** — credited in survivors (PMID: 25667249, 27525348). NCIT: Therapeutic Hypothermia.
- **Supportive care:** mechanical ventilation, seizure control, dexamethasone for edema.
- **Treatment outcomes:** despite therapy, most cases are fatal; survival clusters around early-treated, miltefosine-containing, hypothermia-managed cases (PMID: 26679626).
- **Experimental / preclinical pipeline:** A high-throughput phenotypic screen of 12,000 **ReFRAME** compounds found 58 potent inhibitors (IC50 <1 µM) of free-living amoebae, including **19 active against *N. fowleri***; 19 compounds killed *N. fowleri* in vitro **within 24 h** — faster than current drugs — including **HDAC inhibitors** (quisinostat, panobinostat, pracinostat, dacinostat, fimepinostat), **HSP90 inhibitors** (radicicol, NVP-HSP990), halofuginone, fumagillin, bardoxolone, solithromycin, and acriflavine (PMID: 32970675). Natural products (e.g., *Pinus densiflora* leaf extract, IC50 62.3 µg/mL) are selectively amebicidal while sparing rat glial cells (PMID: 38835258). None are yet approved for human PAM.
- **Personalized/experimental:** no approved targeted therapy. Pharmacogenomics not applicable (pathogen, not host-genome driven).

**Suggested chemical/intervention ontology terms:** CHEBI:2682 amphotericin B; CHEBI:75291 miltefosine; CHEBI:2955 azithromycin; CHEBI:46081 fluconazole; CHEBI:28077 rifampicin; NCIT therapeutic hypothermia; NCIT ventriculostomy/CSF shunt.

---

## 13. Prevention

**Prevention is primarily behavioral and environmental — there is no vaccine for human use.**

- **Primary prevention:** **keep water out of the nose** during warm-freshwater activities; use **nose clips** or hold the nose when jumping/diving; avoid stirring up sediment in warm shallow water (CDC guidance).
- **Nasal irrigation & ablution safety:** use only **sterile, distilled, or previously boiled-and-cooled water** in neti pots / sinus-rinse devices, and for **religious ablution (wudu)** where tap water may be under-chlorinated (PMID: 22919000, 21291600).
- **Water-system control:** adequate **chlorination/disinfection** of pools and splash pads; proper design/operation of treated recreational water venues (PMID: 40146665).
- **Secondary prevention:** clinician awareness for **early recognition** of PAM in meningoencephalitis with freshwater exposure → faster diagnosis/treatment (PMID: 40146665, 26582886).
- **Public-health measures:** environmental water surveillance (PCR/LAMP), outbreak investigation, and public education in endemic/warm regions (PMID: 25822175).
- **Immunization:** experimental **DNA vaccine against *nfa1*** induces protective Th1/Th2 immunity in mice — **no human vaccine** (PMID: 22955499).

---

## 14. Other Species / Natural Disease

- **Agent taxonomy:** *Naegleria fowleri*, NCBI Taxon:5763 (Heterolobosea, Percolozoa).
- **Host range / experimental hosts:** **Mice** are the standard experimental host and develop a disease resembling human PAM after intranasal inoculation (PMID: 646016, 669800).
- **Natural disease in cattle (*Bos taurus*, NCBI Taxon:9913):** A documented outbreak killed nine 10–20-month-old **Holstein heifers** in California (summers 1998–1999) that drank untreated warm surface water (>42 °C); autopsy showed **necrosuppurative hemorrhagic meningoencephalitis with olfactory lobes/nerves most severely affected**, N. fowleri confirmed by IHC and culture — "the disease in cattle closely resembles primary amoebic meningoencephalitis in humans" (PMID: 16475525). This establishes PAM as a genuine **naturally occurring** cross-species disease sharing route of entry, climate dependence, and pathology. Veterinary relevance: include *Naegleria* meningoencephalitis in summer bovine CNS differentials in hot regions.
- **Zoonotic potential:** **None in the classic sense** — not transmitted animal-to-human or human-to-human; acquisition is strictly **environmental** (waterborne via nose). (Rare iatrogenic concern: organ-transplant transmission from infected donors — PMID: 24279908.)
- **Comparative biology:** non-pathogenic congener *N. gruberi* and related *Willaertia magna* share some virulence-gene homologs but lack full pathogenicity, enabling comparative virulence studies (PMID: 31797948, 33843581).

---

## 15. Model Organisms

- **Mouse (BALB/c, others):** the principal in vivo model; **intranasal** inoculation reproduces olfactory-nerve invasion and lethal meningoencephalitis (PMID: 646016, 669800). Used to study innate (neutrophil) defense, protective immunity, passive immunization, and DNA vaccination (PMID: 2628288, 2486833, 22955499).
  - *Phenotype recapitulation:* high — mirrors route of entry, CNS pathology, rapid lethality, and sex/age-dependent susceptibility (females and older mice more resistant; PMID: 669800).
  - *Limitations:* dose/route differences (IV vs intranasal), accelerated course, and species differences in immune response.
- **In vitro / cellular models:** co-culture with **human fibrosarcoma cells**, MDCK epithelial cells, and primary nasal epithelial cells to dissect contact-dependent trogocytosis and EV-mediated cytopathy (PMID: 40096149, 40312759).
- **Omics models:** axenic vs brain-passaged trophozoite proteomics/transcriptomics and secretome/EV proteomics for virulence-factor discovery (PMID: 40096149, 39735262, 33843581).
- **Resources:** ATCC strains of *N. fowleri*; CDC Free-Living and Intestinal Amebas Laboratory (surveillance, PCR, strain archiving).

---

## Evidence Source Legend
Human clinical/epidemiologic: PMID 32369575, 26582886, 42764041, 41873284, 40146665, 27123690, 23621053, 22919000, 23710088, 35020127, 25667249, 26679626, 27525348, 24279908, 21291600, 39780139. In vitro/mechanistic: PMID 40096149, 40312759, 39432113, 32716210, 40016342, 36839446, 39735262. Experimental therapeutics (in vitro/preclinical): PMID 32970675, 38835258. Model organism (mouse): PMID 646016, 669800, 2628288, 2486833, 22955499. Natural animal disease (veterinary): PMID 16475525. Genomics/phylogenomics: PMID 33843581, 31797948, 39826589.

## Supported vs Refuted Hypotheses
**Supported:** (1) PAM is a pathogen-caused infectious disease with **no human causal gene** (etiology = *N. fowleri*). (2) Exposure is overwhelmingly **warm-freshwater nasal entry** with olfactory-nerve CNS invasion. (3) Disease is **>95–97% fatal**, predominantly in **young males**. (4) Cytopathy is dual — **contact-dependent actin/food-cup trogocytosis** plus **contact-independent EV/pore-forming/protease cytolysis**. (5) **Non-recreational tap-water routes** (ablution, neti-pot) are real and epidemiologically important. (6) PAM occurs as a **natural cross-species disease** (cattle) and is well modeled in **intranasally-inoculated mice**.
**Refuted / not applicable:** Any human Mendelian inheritance, susceptibility/protective loci, ClinVar variants, chromosomal abnormalities, genetic testing, carrier screening, or genetic counseling role — none exist for this infectious disease. Person-to-person and classic zoonotic animal-to-human transmission are **not** supported (acquisition is strictly environmental; rare iatrogenic transplant risk aside).

## Limitations & Future Directions
Evidence is dominated by rare case reports and pooled surveillance (no RCTs; survivorship anecdotal). Optimal drug regimen and the independent contribution of hypothermia remain undefined. Priorities: validated early rapid diagnostics (point-of-care PCR/LAMP), new amebicidal drugs crossing the blood–brain barrier, and climate-driven surveillance as the amoeba's geographic range expands.


## Artifacts

- [OpenScientist final report](Primary_Amebic_Meningoencephalitis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Primary_Amebic_Meningoencephalitis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 31 |
| On topic | 25 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 15 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0000290` (3 mentions) - the report calls it "if available"; MONDO calls it **primary amebic meningoencephalitis**
- `HP:0003112` (1 mention) - the report calls it "abnormal CSF"; HP calls it **Abnormal circulating amino acid concentration**
- `CL:0000540` (2 mentions) - the report calls it "neurons", "Tissue/cell level:** nervous tissue — **neurons"; CL calls it **neuron**
- `UBERON:0000955` (2 mentions) - the report calls it "Brain", "Primary organ:** **Brain"; UBERON calls it **brain**
- `UBERON:0001675` (1 mention) - the report calls it "cribriform plate / olfactory nerve"; UBERON calls it **trigeminal ganglion**
- `CL:0000125` (1 mention) - the report calls it "astrocytes/glia"; CL calls it **glial cell**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0030041` (2 mentions) - the report calls it "actin polymerization"; GO calls it **actin filament polymerization**
- `UBERON:0002360` (1 mention) - the report calls it "meninges"; UBERON calls it **meninx**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `Taxon:5763` - called "Naegleria fowleri", "Heterolobosea, Percolozoa"
- `CL:0000540` - called "neurons", "Tissue/cell level:** nervous tissue — **neurons"
- `UBERON:0000955` - called "Brain", "Primary organ:** **Brain"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.
