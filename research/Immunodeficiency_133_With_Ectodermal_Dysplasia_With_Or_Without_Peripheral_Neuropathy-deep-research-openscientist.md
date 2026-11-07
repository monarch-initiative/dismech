---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-26T03:21:15.559261'
end_time: '2026-10-26T03:38:38.770908'
duration_seconds: 1043.21
template_file: templates/disease_pathophysiology_research.md
template_sha: f452f0a9c7e3536175154b9683c45663f686f283
template_variables:
  disease_name: Immunodeficiency 133 With Ectodermal Dysplasia With Or Without Peripheral
    Neuropathy
  mondo_id: MONDO:0979570
  category: Mendelian
  causal_genes: ITPR3
  omim_id: not recorded
  synonyms: IMD133; ITPR3-related combined immunodeficiency; IP3R3 dominant-negative
    combined immunodeficiency
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
  on_topic: 8
  off_topic: 2
  off_topic_references:
  - PMID:27155879
  - PMID:16195467
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 54
  verified: 53
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 21
  labels_matching: 15
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0979570
    reported_labels:
    - if available
    ontology_label: immunodeficiency 133 with ectodermal dysplasia with or without
      peripheral neuropathy
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Immunodeficiency_133_With_Ectodermal_Dysplasia_With_Or_Without_Peripheral_Neuropathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Immunodeficiency_133_With_Ectodermal_Dysplasia_With_Or_Without_Peripheral_Neuropathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 133 With Ectodermal Dysplasia With Or Without Peripheral Neuropathy
- **MONDO ID:** MONDO:0979570 (if available)
- **Causal gene(s):** ITPR3
- **OMIM:** not recorded
- **Synonyms:** IMD133; ITPR3-related combined immunodeficiency; IP3R3 dominant-negative combined immunodeficiency
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 133 With Ectodermal Dysplasia With Or Without Peripheral Neuropathy** covering all of the
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

# Immunodeficiency 133 With Ectodermal Dysplasia With Or Without Peripheral Neuropathy (IMD133): Comprehensive Disease Report

**Disease:** Immunodeficiency 133 With Ectodermal Dysplasia With Or Without Peripheral Neuropathy (IMD133)
**MONDO ID:** MONDO:0979570 · **OMIM:** #621254 · **Causal gene:** **ITPR3** (IP3R3; OMIM 147267; HGNC:6182; chromosome 6p21)
**Synonyms:** IMD133; ITPR3-related combined immunodeficiency; IP3R3 dominant-negative combined immunodeficiency

---

## Summary

Immunodeficiency 133 with ectodermal dysplasia with or without peripheral neuropathy (IMD133) is an ultra-rare multisystem Mendelian disorder caused by variants in **ITPR3**, the gene encoding **IP3R3 (inositol 1,4,5-trisphosphate receptor type 3)** — a subunit of the tetrameric ER calcium-release channel. The disease is driven predominantly by **de novo heterozygous dominant-negative missense variants** (and, less commonly, biallelic/recessive variants) that impair channel function. A single mutant subunit, incorporated into the four-subunit (tetrameric) channel, poisons the whole complex. This is **not** a haploinsufficiency mechanism. The resulting defect depletes endoplasmic reticulum (ER) Ca²⁺ stores and blunts **store-operated Ca²⁺ entry (SOCE)** in T cells, crippling the NFAT- and NF-κB-dependent signaling required for normal T-cell development and activation ([PMID: 39560673](https://pubmed.ncbi.nlm.nih.gov/39560673/)).

The clinical picture is a **combined immunodeficiency (CID)** — recurrent bacterial, viral, and fungal infections beginning in the first months to years of life, T-cell lymphopenia, naive T-cell depletion, hypogammaglobulinemia, and immune dysregulation (immune thrombocytopenia, autoimmune hemolytic anemia, lymphoproliferation). Susceptibility to EBV, VZV, and HPV is prominent, and EBV-driven lymphoma and hemophagocytic lymphohistiocytosis (HLH) are major life-threatening complications. Because IP3R-dependent Ca²⁺ signaling is also essential for ectodermal epithelia (notably enamel-forming ameloblasts) and peripheral nerve, affected individuals variably show **ectodermal dysplasia** (conical/peg-shaped teeth, hypodontia, microdontia, sparse fine hair, hypohidrosis, dysplastic nails) and **demyelinating/intermediate peripheral neuropathy** (allelic with Charcot-Marie-Tooth disease type 1J, CMT1J).

The gene displays a striking **allelic/phenotypic spectrum**: the same gene causes dominant CMT neuropathy (CMT1J) and dominant-negative combined immunodeficiency with ectodermal dysplasia, and the phenotypes can overlap. Fewer than ~20 genetically confirmed IMD133 patients have been reported worldwide. Diagnosis rests on **trio whole-exome/whole-genome sequencing** (to catch de novo variants) or a primary-immunodeficiency gene panel including ITPR3, supported by functional Ca²⁺/SOCE assays. **Hematopoietic stem-cell transplantation (HSCT)** can correct the immune defect, but no targeted or gene therapy currently exists.

---

## Key Findings

### Finding 1 — IMD133 is caused by de novo dominant-negative missense variants in ITPR3 (IP3R3)

Blanco et al. (2025, *J Exp Med*; [PMID: 39560673](https://pubmed.ncbi.nlm.nih.gov/39560673/)) reported **five unrelated patients with de novo missense variants in ITPR3** presenting with combined immunodeficiency, abnormal T-cell Ca²⁺ homeostasis, incompletely penetrant ectodermal dysplasia, and multisystem disease. The authors state: *"We report five unrelated patients with de novo missense variants in ITPR3, encoding a subunit of the inositol 1,4,5-trisphosphate receptor (IP3R)."*

Critically, pathogenicity is **not due to haploinsufficiency**. Instead, *"ITPR3 protein variants interfere with IP3R channel function leading to depletion of ER Ca2+ stores and blunted SOCE in T cells."* Because IP3R3 assembles as a tetramer, one defective subunit disrupts the whole channel — the textbook definition of a **dominant-negative** mechanism. This establishes both the causal gene and the molecular class of lesion.

### Finding 2 — ITPR3 shows an allelic/phenotypic spectrum spanning dominant CMT neuropathy and dominant-negative combined immunodeficiency

ITPR3 variants cause a continuum of disease. On the neuropathy end:
- Rönkkö et al. (2020; [PMID: 32949214](https://pubmed.ncbi.nlm.nih.gov/32949214/)) first proved ITPR3 is a CMT gene: *"Exome sequencing identified a heterozygous ITPR3 p.Val615Met variant segregating with the disease"* (AD family, demyelinating + axonal, onset ~age 30) and a de novo p.Arg2524Cys (onset age 4, severe).
- Beijer et al. (2024; [PMID: 38938188](https://pubmed.ncbi.nlm.nih.gov/38938188/)) identified a recurrent hotspot: *"A recurrent heterozygous missense variant p.Thr1424Met ... was present in 33 affected individuals from nine unrelated families"* — all with slow nerve conduction velocities (CMT1).
- Cabello-Murgui et al. (2024; [PMID: 39287469](https://pubmed.ncbi.nlm.nih.gov/39287469/)) reported *"The c.4271C > T ITPR3 variant causes a late onset CMT that can be considered an intermediate CMT"* — initially misdiagnosed as CIDP.

Peripheral neuropathy, immunodeficiency, and tooth abnormalities can co-occur in the same individuals, which is why the disease name carries the "with or without peripheral neuropathy" qualifier.

### Finding 3 — A spontaneous canine ITPR3-null model recapitulates CMT1J with ectodermal (enamel) involvement

Hytönen et al. (2025; [PMID: 39804930](https://pubmed.ncbi.nlm.nih.gov/39804930/)) identified *"a homozygous nonsense variant in the ITPR3 gene in Lancashire Heeler dogs, presenting with a severe developmental enamel defect and reduced nerve conduction velocity."* At the protein level, *"the nonsense variant in ITPR3 led to a complete absence of full-length IP3R3 protein. Unexpectedly, the protein levels of IP3R1 and IP3R2 were also markedly decreased, suggesting co-regulation,"* and IP3R-mediated Ca²⁺ flux upon GPCR stimulation was reduced. This natural model links ITPR3 loss to both the ectodermal (amelogenesis imperfecta) and neuropathic phenotypes of the human disease.

### Finding 4 — IMD133 = OMIM #621254; a multisystem autosomal-dominant disorder

OMIM #621254 defines IMD133 as caused by heterozygous mutation in ITPR3 (OMIM 147267; HGNC:6182) at 6p21. Reported de novo heterozygous missense variants across the defining cohorts include **A196T, I2506N, R2524C (recurrent), and R2524H** (Blanco et al. 2025; [PMID: 39560673](https://pubmed.ncbi.nlm.nih.gov/39560673/)) and a recurrent **R2524C** in four patients (Molitor et al. 2024, *Sci Adv*; [PMID: 39270020](https://pubmed.ncbi.nlm.nih.gov/39270020/)). Core features: combined immunodeficiency/CVID with recurrent infection in the first months-to-years of life, T-cell lymphopenia and dysfunction, variable ectodermal dysplasia, ± peripheral neuropathy, immune dysregulation, poor growth/short stature, and developmental delay — *"incompletely penetrant ectodermal dysplasia, and multisystem disease."*

### Finding 5 — T-cell phenotype: lymphopenia, naive depletion, restricted TCR, impaired NFAT/NF-κB and mitochondrial/metabolic downregulation

Blanco et al. (2025; [PMID: 39560673](https://pubmed.ncbi.nlm.nih.gov/39560673/)) describe *"defects in late stages of thymic T cell development, and impaired function of peripheral T cells, including inadequate NF-κB- and NFAT-mediated, proliferative, and metabolic responses to activation."* Molitor et al. (2024; [PMID: 39270020](https://pubmed.ncbi.nlm.nih.gov/39270020/)) in R2524C patients found CD4⁺ lymphopenia, quasi-absence of naive CD4⁺ and CD8⁺ cells, increased memory cells, a distinct/restricted TCR repertoire, defective calcium homeostasis, and mitochondrial malfunction, with decreased proliferation and downregulation of metabolic and mitochondrial pathways.

### Finding 6 — Clinical course, complications, and treatment

Per OMIM #621254 and Blanco et al. (2025; [PMID: 39560673](https://pubmed.ncbi.nlm.nih.gov/39560673/)), patients present in the first months-to-years of life with recurrent bacterial, viral, and fungal infections (*"The patients presented with CID, abnormal T cell Ca2+ homeostasis, incompletely penetrant ectodermal dysplasia, and multisystem disease"*), hypogammaglobulinemia/B-cell abnormalities, and immune dysregulation (immune thrombocytopenia, autoimmune hemolytic anemia, lymphoproliferation). Of the 5 Blanco patients: 2 underwent **HSCT** (ages 9 and 3); 2 developed **EBV-driven lymphomas** (ages 22 and 12) requiring chemotherapy then HSCT; the 5th remained clinically well on antibiotic prophylaxis at age 18. The Molitor cohort additionally reported bone-marrow failure in some patients.

### Finding 7 — IP3R3 protein: a tetrameric ER Ca²⁺-release channel poisoned by dominant-negative variants

ITPR3 encodes IP3R3, a ~2,671-amino-acid subunit that assembles as a homo/heterotetramer forming an ER-membrane Ca²⁺ channel, with an N-terminal IP3 ligand-binding (and suppressor) domain and a C-terminal transmembrane channel/pore domain (OMIM 147267). Blanco et al. describe the subunit *"which forms a Ca2+ channel in the endoplasmic reticulum (ER) membrane responsible for the release of ER Ca2+ required to trigger SOCE, and for Ca2+ transfer to other organelles."* Because four subunits co-assemble, a single mutant subunit disrupts the tetramer — the basis for the dominant-negative (not haploinsufficient) mechanism. IP3R3 also localizes to **mitochondria-associated ER membranes (MAMs)**, where it transfers Ca²⁺ to mitochondria to sustain bioenergetics: *"the MAM is a critical cell-signaling junction whereby Bcl-xL dynamically interacts with IP3R3 to coordinate mitochondrial Ca(2+) transfer and alters cellular metabolism in order to increase the cells' bioenergetic capacity"* ([PMID: 27155879](https://pubmed.ncbi.nlm.nih.gov/27155879/)).

### Finding 8 — HPO phenotype spectrum with frequencies

Aggregated across three reports (~11 patients; [PMID: 39560673](https://pubmed.ncbi.nlm.nih.gov/39560673/), [PMID: 39270020](https://pubmed.ncbi.nlm.nih.gov/39270020/), [PMID: 36302985](https://pubmed.ncbi.nlm.nih.gov/36302985/)), see the phenotype table below.

### Finding 9 — Ectodermal dysplasia branch: IP3R-dependent ER Ca²⁺ release feeds SOCE required for enamel/ectodermal development

In dental enamel cells, Nurbaeva et al. (2015; [PMID: 26515404](https://pubmed.ncbi.nlm.nih.gov/26515404/)) found *"inositol 1,4,5-trisphosphate receptor (IP3R) but not ryanodine receptor (RyR) expression was high in enamel cells suggesting that IP3Rs are the main ER Ca(2+) release mechanism."* SOCE-driven Ca²⁺ signals then drive enamel matrix protein gene expression: *"Ca2+ signals enhance the expression of EMPs"* ([PMID: 26232387](https://pubmed.ncbi.nlm.nih.gov/26232387/)). Patients with CRAC-channel (STIM1/ORAI1) mutations develop amelogenesis imperfecta, and in IMD133 ectodermal dysplasia occurs in 4/5 patients, while the canine ITPR3-null model shows severe amelogenesis imperfecta ([PMID: 39804930](https://pubmed.ncbi.nlm.nih.gov/39804930/)).

### Finding 10 — Inheritance heterogeneity and severe EBV-driven HLH

The first ITPR3 immunodeficiency report (Neumann/Ehl et al. 2022, *Cell Mol Immunol*; [PMID: 36302985](https://pubmed.ncbi.nlm.nih.gov/36302985/)) described two unrelated patients with **compound heterozygous (biallelic/recessive)** ITPR3 variants — a 12-year-old with CID (HSCT at age 6) and a 36-year-old with CVID — establishing IP3R defects as a new class of inborn errors of immunity. Subsequent cohorts (Molitor 2024; Blanco 2025) describe **de novo heterozygous dominant-negative** variants. A 2025 report ([PMID: 41019080](https://pubmed.ncbi.nlm.nih.gov/41019080/)) describes two CID patients with ITPR3 mutations presenting with life-threatening severe EBV-associated HLH. Blanco et al. frame the biology: *"The importance of calcium (Ca2+) as a second messenger in T cell signaling is exemplified by genetic deficiencies of STIM1 and ORAI1, which abolish store-operated Ca2+ entry (SOCE) resulting in combined immunodeficiency (CID)."*

### Finding 11 — Model organisms

Mouse (NCBITaxon:10090; *Itpr3* NCBI Gene 16440): Futatsugi et al. (2005, *Science*; [PMID: 16195467](https://pubmed.ncbi.nlm.nih.gov/16195467/)) — *"We show exocrine dysfunction in IP3R2 and IP3R3 double knock-out mice, which caused difficulties in nutrient digestion,"* and *"Despite a normal caloric intake, the double mutants were hypoglycemic and lean."* Single Itpr3-KO mice have mild phenotypes (paralog redundancy). Dog (NCBITaxon:9615): spontaneous ITPR3-null Lancashire Heeler model ([PMID: 39804930](https://pubmed.ncbi.nlm.nih.gov/39804930/)). Cellular models: Jurkat T-cell lines engineered with R2524C reproduce dominant-negative defective Ca²⁺ flux ([PMID: 39270020](https://pubmed.ncbi.nlm.nih.gov/39270020/)); patient fibroblasts and T cells show depleted ER stores and blunted SOCE.

### Finding 12 — Diagnostics and epidemiology

Ultra-rare: fewer than ~20 genetically confirmed patients worldwide; no Orphanet/GBD prevalence estimate. Pathogenic alleles are absent/ultra-rare in gnomAD (CMT hotspot p.Thr1424Met *"gnomAD v4 allele frequency 1.76 × 10-6"*; [PMID: 38938188](https://pubmed.ncbi.nlm.nih.gov/38938188/)). Diagnosis via trio WES/WGS or a PID gene panel including ITPR3. Supportive labs: T-cell lymphopenia (*"significant T cell lymphopenia, defects in late stages of thymic T cell development"*), low CD8⁺/naive T cells, low/abnormal TRECs (potentially detectable on newborn SCID screening), hypogammaglobulinemia/low IgM, restricted TCR, impaired proliferation. Functional confirmation by Fura-2/Fluo-4 Ca²⁺ flux and SOCE assays after thapsigargin or TCR stimulation.

---

## Phenotype Spectrum (HPO terms and frequencies)

| Domain | Phenotype (HPO) | Frequency (aggregated) |
|---|---|---|
| Immune (core) | Combined immunodeficiency (HP:0005387) | 5/5 |
| Immune | Decreased total T cell count (HP:0005403) | 15/15 |
| Immune | Decreased total lymphocyte count (HP:0001888) | 10/10 |
| Immune | Decreased CD8⁺ T cell proportion (HP:0005415) | 8/9 |
| Immune | Decreased naive CD4⁺ (HP:0410378) / CD8⁺ (HP:0410377) | 3/3 |
| Immune | Decreased circulating IgM (HP:0002850) | 4/4 |
| Infection | Pneumonia (HP:0002090) | 4/4 |
| Infection | Bronchiectasis (HP:0002110) | 2/2 |
| Infection | Severe VZV (HP:0032170) | 2/2 |
| Infection | Molluscum contagiosum (HP:0032163) | 2/2 |
| Infection | Persistent EBV viremia (HP:0020072); Warts (HP:0200043) | reported |
| Dysregulation | Autoimmune thrombocytopenia (HP:0001973) | 3/4 |
| Malignancy | Lymphoma (HP:0002665); B-cell (HP:0012191); Hodgkin (HP:0012189) | reported |
| Ectodermal | Ectodermal dysplasia (HP:0000968) | 4/5 |
| Ectodermal | Fine hair (HP:0002213) | 4/5 |
| Ectodermal | Peg-shaped maxillary lateral incisors (HP:0006342) | 3/4 |
| Ectodermal | Conical incisor (HP:0011065); Microdontia (HP:0000691) | reported |
| Ectodermal | Hypodontia (HP:0000668) | 2/4 |
| Ectodermal | Hypohidrosis (HP:0000966) | 1/5 |
| Ectodermal | Sparse eyebrow (HP:0045075) | 2/2 |
| Neuro | Demyelinating peripheral neuropathy (HP:0007108); Polyneuropathy (HP:0001271) | reported |
| Neuro | Global developmental delay (HP:0001263); Intellectual disability (HP:0001249) | reported |
| Neuro | Delayed speech/language (HP:0000750) | 5/5 |
| Neuro | Motor delay (HP:0001270) | 4/4 |
| Neuro | Pes cavus (HP:0001761); Hearing impairment (HP:0000365) | 2/4 (hearing) |
| Growth | Growth delay (HP:0001510) | 4/7 |
| Onset | Infantile onset (HP:0003593) | 6/11 |

---

## Mechanistic Model / Causal Chain

The pathophysiology is organized as a branched causal chain from the initiating mutation to the multisystem clinical manifestations. Steps marked *(inferred)* are mechanistically plausible but not directly demonstrated in IMD133 patients.

```
(1) De novo heterozygous missense variant in ITPR3
     (R2524C/R2524H/I2506N near C-terminal channel domain;
      A196T in N-terminal suppressor/IP3-binding region)       [PMID 39560673, 39270020]
        |
        v
(2) Mutant IP3R3 subunit co-assembles into the tetrameric
    ER Ca2+-release channel and acts DOMINANT-NEGATIVELY
    (altered gating / channel "leakiness"; NOT haploinsufficiency) [PMID 39560673]
        |
        v
(3) Chronic ER Ca2+ store depletion + reduced regulated
    IP3-triggered ER Ca2+ release                               [PMID 39560673]
        |
        +----------------------------+----------------------------+---------------------------+
        v                            v                            v                           v
  BRANCH A (IMMUNE)            BRANCH B (ECTODERMAL)        BRANCH C (NEURAL, inferred)   BRANCH D (GROWTH/METABOLIC)
(4a) blunted SOCE after      (4b) reduced ER Ca2+/SOCE    (4c) impaired IP3R3 Ca2+       reduced ER->mito Ca2+ at MAMs
     TCR engagement               in ameloblasts/              signaling in Schwann          + impaired exocrine secretion
        |                         ectodermal epithelia         cells/axons                      |
        v                            |                            |                              v
(5a) reduced calcineurin/       (5b, inferred) decreased     (5c) dys-/demyelination       poor growth / failure to thrive
     NFAT & NF-kB; impaired         enamel-matrix-protein        and axonal dysfunction     (mouse Itpr2/3 dKO hypoglycemic/lean
     metabolic/mito reprogramming   gene expression & Ca2+          |                        [PMID 16195467];
        |                           for mineralization            v                         MAM bioenergetics [PMID 27155879])
        v                            |                        (6c) intermediate/demyelinating
(6a) defective late thymic          v                             peripheral neuropathy (CMT1J)
     T-cell development          (6b) amelogenesis imperfecta,   [PMID 32949214, 38938188]
        |                            conical/peg teeth,
        v                            hypodontia, sparse fine
(7a) T-cell lymphopenia,             hair, hypohidrosis,
     naive depletion,                dysplastic nails
     restricted TCR,             [PMID 26515404, 26232387;
     B-cell/antibody defects      canine PMID 39804930]
        |
        v
(8a) COMBINED IMMUNODEFICIENCY: recurrent bacterial/viral/fungal infection,
     EBV/VZV/HPV susceptibility, EBV-driven lymphoma/HLH,
     immune dysregulation (ITP, AIHA, lymphoproliferation)
     [PMID 39560673, 39270020, 41019080]
```

**Upstream vs downstream:** Steps 1–3 (mutation → dominant-negative channel → ER Ca²⁺ depletion) are the shared upstream lesion. The four branches are downstream, tissue-specific consequences reflecting where IP3R3-dependent Ca²⁺ signaling is non-redundant.

**Cell types and processes (ontology suggestions):**
- **Biological processes (GO):** release of sequestered calcium ion into cytosol (GO:0051209); store-operated calcium entry (GO:0002115); calcium-mediated signaling (GO:0019722); T cell activation (GO:0042110); positive regulation of NF-κB / NFAT transcription factor activity.
- **Cellular components (GO):** endoplasmic reticulum membrane (GO:0005789); inositol 1,4,5-trisphosphate receptor complex; mitochondria-associated ER membrane (MAM).
- **Cell types (CL):** T cell (CL:0000084), naive T cell (CL:0000898), thymocyte (CL:0000893), ameloblast (CL:0000059), Schwann cell (CL:0002573), B cell (CL:0000236).
- **Anatomy (UBERON):** thymus (UBERON:0002370), tooth enamel/ameloblast layer, peripheral nerve (UBERON:0001021), skin/hair follicle, nail.
- **Chemical (CHEBI):** calcium(2+) (CHEBI:29108), inositol 1,4,5-trisphosphate (CHEBI:16595).

---

## Section-by-Section Content

### 1. Disease Information
IMD133 is an inborn error of immunity with ectodermal and (variable) neuropathic features caused by ITPR3/IP3R3 dysfunction. **Identifiers:** OMIM #621254; MONDO:0979570; gene ITPR3 (OMIM 147267, HGNC:6182). Orphanet/ICD-10/ICD-11/MeSH codes are not yet assigned (ultra-rare, recently delineated). **Synonyms:** IMD133; ITPR3-related combined immunodeficiency; IP3R3 dominant-negative combined immunodeficiency. Information is derived from **individual-patient case series** (not aggregated disease-level registries).

### 2. Etiology
**Causal factor:** monogenic — pathogenic variants in ITPR3. **Genetic risk:** de novo dominant-negative missense (A196T, I2506N, R2524C, R2524H) and, less commonly, biallelic/compound-heterozygous variants. No established environmental risk or protective factors; no modifier genes defined. **Gene-environment interaction:** infectious exposures (EBV, VZV, HPV) unmask/drive the most severe complications (lymphoma, HLH) on the background of the T-cell defect — a gene × pathogen interaction rather than a classical GxE.

### 3. Phenotypes
See the phenotype table above. Onset is typically infantile; severity is variable (mild/conservatively managed to lethal lymphoma/HLH); course is chronic and multisystem. Quality-of-life impact is substantial (recurrent infections, transplant, malignancy risk, dental/dermatologic features, possible neuropathy and developmental delay); no formal QOL instrument data exist for this ultra-rare disease.

### 4. Genetic/Molecular Information
**Causal gene:** ITPR3 (6p21). **Variant types:** missense (dominant-negative, de novo) predominate; nonsense (recessive, canine model). **Classification:** reported disease variants are pathogenic/likely pathogenic per ACMG (de novo occurrence, functional evidence). **Allele frequency:** absent/ultra-rare in gnomAD. **Origin:** germline (de novo or inherited). **Functional consequence:** dominant-negative channel dysfunction (ER Ca²⁺ depletion, blunted SOCE) — not haploinsufficiency. No epigenetic or chromosomal-abnormality mechanism; modifier genes unknown.

### 5. Environmental Information
No causal toxins, radiation, or occupational exposures. **Infectious agents** act as triggers/complicating factors: EBV (lymphoma, HLH), VZV (severe/disseminated), HPV (warts), molluscum contagiosum, plus general bacterial/fungal pathogens.

### 6. Mechanism / Pathophysiology
See the causal-chain diagram and ontology suggestions above. Core pathway: IP3/Ca²⁺ signaling → SOCE (ORAI/STIM) → calcineurin-NFAT and NF-κB (KEGG calcium signaling; Reactome SOCE). Downstream processes: impaired T-cell development/activation, mitochondrial/metabolic reprogramming (MAM Ca²⁺ transfer), enamel mineralization, and peripheral myelination.

### 7. Anatomical Structures Affected
**Primary:** immune system (thymus, T lymphocytes; UBERON:0002370). **Ectodermal derivatives:** teeth/enamel (ameloblasts), hair follicles, skin sweat glands, nails. **Nervous system:** peripheral nerves (Schwann cells/axons). **Secondary/systemic:** growth (short stature), hematologic (cytopenias, bone-marrow failure), lymphoid organs (lymphoproliferation/lymphoma). **Subcellular:** endoplasmic reticulum membrane and MAMs. Lateralization: bilateral/systemic.

### 8. Temporal Development
**Onset:** congenital/infantile for immune and ectodermal features; neuropathy onset variable (childhood to adult, allelic CMT range). **Progression:** chronic, lifelong; punctuated by acute, potentially fatal events (severe infection, EBV lymphoma/HLH). No spontaneous remission; HSCT is curative for the immune component. Critical window: early life, before severe infection/malignancy and with the opportunity for timely HSCT.

### 9. Inheritance and Population
**Inheritance:** predominantly autosomal dominant (de novo); also autosomal recessive (biallelic). **Penetrance:** immune phenotype highly penetrant; ectodermal dysplasia incompletely penetrant. **Expressivity:** highly variable. **Epidemiology:** ultra-rare, <~20 confirmed patients worldwide; no prevalence/incidence estimate. No founder effect, defined carrier frequency, or sex predilection established.

### 10. Diagnostics
**Genetic:** trio WES/WGS (de novo detection) or PID gene panel including ITPR3 (Genomics England PanelApp). **Immunologic labs:** T-cell lymphopenia; low CD8⁺/naive T cells; low/abnormal TRECs (newborn SCID screen may flag); hypogammaglobulinemia/low IgM; restricted TCR; impaired PHA/anti-CD3/CD28 proliferation. **Functional confirmation:** Fura-2/Fluo-4 Ca²⁺ flux and SOCE assays (thapsigargin or TCR stimulation) showing depleted ER stores and blunted SOCE. **Nerve conduction studies** for neuropathy. **Differential diagnosis:** STIM1/ORAI1 CRAC-channelopathies, other CID/CVID, other ectodermal dysplasias, CMT of other genetic causes, CIDP (neuropathy can mimic).

### 11. Outcome/Prognosis
Guarded; depends on infection control, malignancy, and HSCT success. Major mortality drivers: severe/opportunistic infection, EBV-driven lymphoma and HLH, bone-marrow failure. HSCT can be curative for the immunologic defect but carries transplant-related risk and does not reverse established ectodermal or neuropathic features. No large survival dataset exists. Prognostic factors: variant severity, infection/EBV burden, timeliness of transplant.

### 12. Treatment
**Supportive/pharmacologic:** antimicrobial prophylaxis; immunoglobulin replacement (IVIG/SCIG) for hypogammaglobulinemia; antivirals for EBV/VZV; management of autoimmune cytopenias. **Definitive:** **hematopoietic stem-cell transplantation (HSCT; NCIT C15431)** corrects the immune defect. **Malignancy:** chemotherapy for EBV-driven lymphoma, often followed by HSCT; HLH-directed therapy for HLH. No targeted, RNA-based, or gene therapy currently exists. **NCIT suggestions:** Hematopoietic Cell Transplantation (C15431), Immunoglobulin Therapy (C603), Antimicrobial Prophylaxis.

### 13. Prevention
No primary prevention (de novo origin). **Secondary:** newborn SCID screening (low TRECs may detect T-cell lymphopenia early); early genetic diagnosis to enable prophylaxis and transplant planning. **Tertiary:** infection prophylaxis, EBV surveillance, dental/dermatologic care, neuropathy rehabilitation. **Genetic counseling:** mostly de novo (low recurrence) but germline mosaicism cannot be excluded; recessive families require carrier counseling.

### 14. Other Species / Natural Disease
**Dog** (*Canis lupus familiaris*, NCBITaxon:9615): spontaneous homozygous ITPR3 nonsense variant in Lancashire Heelers causes amelogenesis imperfecta + reduced nerve conduction velocity (CMT1J-like) — a natural veterinary model ([PMID: 39804930](https://pubmed.ncbi.nlm.nih.gov/39804930/)). Orthologs: mouse *Itpr3* (NCBI Gene 16440). Evolutionarily conserved Ca²⁺-channel function underlies cross-species phenotype overlap.

### 15. Model Organisms
- **Mouse:** *Itpr2/Itpr3* double-knockout (exocrine dysfunction, hypoglycemia, leanness, impaired growth; [PMID: 16195467](https://pubmed.ncbi.nlm.nih.gov/16195467/)); single *Itpr3*-KO mild (paralog redundancy). Models the growth/metabolic branch; does not fully recapitulate the human dominant-negative immune phenotype.
- **Dog:** spontaneous ITPR3-null (above) — ectodermal + neuropathic recapitulation.
- **Cellular/in vitro:** Jurkat T cells expressing R2524C (dominant-negative Ca²⁺ flux defect; [PMID: 39270020](https://pubmed.ncbi.nlm.nih.gov/39270020/)); patient fibroblasts and primary T cells (depleted ER stores, blunted SOCE).
- **Resources:** MGI (mouse), OMIA (dog), Cellosaurus (Jurkat).

---

## Evidence Base

| PMID | Study (year) | Type | Contribution |
|---|---|---|---|
| [39560673](https://pubmed.ncbi.nlm.nih.gov/39560673/) | Blanco et al. (2025) *J Exp Med* | Human clinical + functional | Defines IMD133: 5 patients, de novo dominant-negative ITPR3 variants, ER Ca²⁺ depletion, blunted SOCE, T-cell defects |
| [39270020](https://pubmed.ncbi.nlm.nih.gov/39270020/) | Molitor et al. (2024) *Sci Adv* | Human + Jurkat model | Recurrent R2524C; naive T-cell depletion, restricted TCR, mitochondrial dysfunction |
| [36302985](https://pubmed.ncbi.nlm.nih.gov/36302985/) | Neumann/Ehl et al. (2022) *Cell Mol Immunol* | Human clinical | First ITPR3 immunodeficiency; biallelic/recessive form; CID + CVID |
| [41019080](https://pubmed.ncbi.nlm.nih.gov/41019080/) | (2025) *Front Immunol* | Human clinical | Severe EBV-driven HLH in ITPR3 CID |
| [32949214](https://pubmed.ncbi.nlm.nih.gov/32949214/) | Rönkkö et al. (2020) | Human + functional | ITPR3 established as CMT gene (p.Val615Met, p.Arg2524Cys) |
| [38938188](https://pubmed.ncbi.nlm.nih.gov/38938188/) | Beijer et al. (2024) | Human cohort | Recurrent p.Thr1424Met hotspot (33 individuals); gnomAD ultra-rarity |
| [39287469](https://pubmed.ncbi.nlm.nih.gov/39287469/) | Cabello-Murgui et al. (2024) | Human clinical | Intermediate adult-onset CMT; CIDP misdiagnosis |
| [39804930](https://pubmed.ncbi.nlm.nih.gov/39804930/) | Hytönen et al. (2025) | Canine model | ITPR3-null dog: amelogenesis imperfecta + neuropathy; IP3R paralog co-regulation |
| [16195467](https://pubmed.ncbi.nlm.nih.gov/16195467/) | Futatsugi et al. (2005) *Science* | Mouse model | Itpr2/3 dKO: exocrine/metabolic/growth phenotype |
| [27155879](https://pubmed.ncbi.nlm.nih.gov/27155879/) | (review) | Mechanistic | IP3R3-Bcl-xL MAM axis; ER→mito Ca²⁺ and bioenergetics |
| [26515404](https://pubmed.ncbi.nlm.nih.gov/26515404/) | Nurbaeva et al. (2015) | In vitro | IP3R is main ER Ca²⁺ release in enamel cells |
| [26232387](https://pubmed.ncbi.nlm.nih.gov/26232387/) | Nurbaeva et al. (2015) | In vitro | SOCE Ca²⁺ signals drive enamel matrix protein genes |

---

## Limitations and Knowledge Gaps

1. **Tiny sample size.** Fewer than ~20 genetically confirmed patients; all frequency and penetrance figures derive from small case series and are not population-based.
2. **Neural branch is inferred.** The Schwann-cell/axon mechanism (Branch C) is extrapolated from allelic CMT studies, not directly demonstrated in IMD133 immunodeficiency patients.
3. **Ectodermal step 5b is inferred.** The link from reduced ameloblast Ca²⁺ to decreased enamel-matrix-protein expression is supported by CRAC-channel and in vitro data, not by direct ITPR3-patient enamel transcriptomics.
4. **Genotype-phenotype correlation is unresolved.** Why some variants favor neuropathy (CMT1J) and others combined immunodeficiency — and why ectodermal dysplasia is incompletely penetrant — is not established.
5. **No validated biomarkers, QOL data, prognostic models, or formal epidemiology** (no Orphanet/GBD/ICD codes).
6. **No disease-specific mouse model** of the human dominant-negative immune phenotype; current mouse data model only the metabolic/growth branch.
7. **No targeted therapy.** HSCT is the only disease-modifying option and addresses only the immune component.

## Proposed Follow-up Experiments / Actions

1. **Knock-in mouse / zebrafish models** carrying human dominant-negative alleles (e.g., R2524C) to test immune, ectodermal, and neural recapitulation and genotype-phenotype links.
2. **Patient iPSC-derived systems:** iPSC→T cells, iPSC→ameloblast-like cells, and iPSC→Schwann cells to directly test each branch's Ca²⁺/SOCE defect and transcriptional consequences.
3. **Structure-function mapping** of IP3R3 variants (cryo-EM/channel electrophysiology) to classify gain-of-function "leak" vs loss-of-function gating defects and correlate with phenotype severity.
4. **Pharmacologic rescue screens:** test whether SOCE potentiators, Ca²⁺-modulating agents, or chaperone strategies restore T-cell Ca²⁺ dynamics in patient cells.
5. **Natural-history registry** (international) to define penetrance, QOL, malignancy incidence, HSCT outcomes, and neuropathy progression.
6. **Newborn-screening analysis:** quantify TREC-based detectability to determine whether IMD133 could be caught on existing SCID panels.
7. **EBV-directed prevention/therapy evaluation** (surveillance, rituximab, EBV-specific CTLs) given the high lymphoma/HLH burden.

---

*Report compiled from 13 confirmed findings and 26 reviewed papers across 5 investigation iterations. Evidence types are distinguished as human clinical, model organism, in vitro, or computational throughout.*


## Artifacts

- [OpenScientist final report](Immunodeficiency_133_With_Ectodermal_Dysplasia_With_Or_Without_Peripheral_Neuropathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Immunodeficiency_133_With_Ectodermal_Dysplasia_With_Or_Without_Peripheral_Neuropathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 8 |
| Off topic | 2 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:27155879` (5 mentions) - The non-apoptotic action of Bcl-xL: regulating Ca(2+) signaling and bioenergetics at the ER-mitochondrion interface.
  - shared terms: cell
- `PMID:16195467` (7 mentions) - IP3 receptor types 2 and 3 mediate exocrine secretion underlying energy metabolism.
  - shared terms: cell

Weighed against this report's own most characteristic terms: `cell`, `itpr3`, `ectodermal`, `patient`, `gene`, `dominant-negative`, `variant`, `soce`, `phenotype`, `neuropathy`, `t-cell`, `immune`, `novo`, `disease`, `defect`, `immunodeficiency`, `model`, `imd133`, `severe`, `hlh`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 54 |
| Resolved | 53 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 21 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0979570` (3 mentions) - the report calls it "if available"; MONDO calls it **immunodeficiency 133 with ectodermal dysplasia with or without peripheral neuropathy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0005415` (1 mention) - the report calls it "Decreased CD8⁺ T cell proportion"; HP calls it **Decreased total CD8+ T cell proportion**
- `HP:0002850` (1 mention) - the report calls it "Decreased circulating IgM"; HP calls it **Decreased circulating IgM concentration**
- `HP:0032170` (1 mention) - the report calls it "Severe VZV"; HP calls it **Severe varicella zoster infection**, and lists "Severe herpes zoster" among its other names
- `HP:0032163` (1 mention) - the report calls it "Molluscum contagiosum"; HP calls it **Unusual molluscum contagiosum**, and lists "Molluscum contagiosum" among its other names
- `HP:0000750` (1 mention) - the report calls it "Delayed speech/language"; HP calls it **Delayed speech and language development**, and lists "Delayed speech" among its other names
