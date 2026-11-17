---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-10T14:16:56.190108'
end_time: '2026-11-10T14:38:49.327963'
duration_seconds: 1313.14
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Thrombocytopenia 6
  mondo_id: MONDO:0014837
  category: Mendelian
  causal_genes: SRC
  omim_id: OMIM:616937
  synonyms: SRC-related thrombocytopenia; THC6; hereditary thrombocytopenia with early-onset
    myelofibrosis
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
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 8
  validator_version: 0.5.1
term_validation:
  total_terms: 39
  verified: 37
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 5
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: HP:0001873
    reported_labels:
    - Lab abnormality
    ontology_label: Thrombocytopenia
  - term_id: HP:0030401
    reported_labels:
    - Lab (ultrastructural)
    ontology_label: Abnormal platelet dense granule ATP/ADP ratio
  - term_id: HP:0001744
    reported_labels:
    - Clinical sign
    ontology_label: Splenomegaly
  - term_id: HP:0002719
    reported_labels:
    - Clinical sign
    ontology_label: Recurrent infections
  - term_id: UBERON:0000178
    reported_labels:
    - blood/hematopoietic system
    ontology_label: blood
  labels_variant: 3
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
  path: Thrombocytopenia_6-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Thrombocytopenia_6-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Thrombocytopenia 6
- **MONDO ID:** MONDO:0014837 (if available)
- **Causal gene(s):** SRC
- **OMIM:** OMIM:616937
- **Synonyms:** SRC-related thrombocytopenia; THC6; hereditary thrombocytopenia with early-onset myelofibrosis
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Thrombocytopenia 6** covering all of the
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

# Thrombocytopenia 6 (THC6) — Comprehensive Disease Characterization

**Causal gene: _SRC_ (proto-oncogene, non-receptor tyrosine-protein kinase c-Src; HGNC:11283; NCBI Gene 6714; UniProt P12931).** Thrombocytopenia 6 is a Mendelian, autosomal-dominant inherited platelet disorder caused by a recurrent **germline gain-of-function missense variant in _SRC_, c.1579G>A p.(Glu527Lys) (E527K)**. It is distinct from the many other numbered "thrombocytopenia" entries (e.g., THC2/ANKRD26, THC5/ETV6), which involve different genes; this report follows the identifiers **OMIM:616937 / MONDO:0014837 / causal gene SRC**.

> Evidence base: The disease is defined by a small number of primary human reports — Turro et al. 2016 (PMID 26936507, landmark discovery, 9 cases), De Kock et al. 2019 (PMID 31204551, second family, de novo), and Palma-Barqueros et al. 2022 (PMID 35349645, third/additional kindred) — supplemented by SRC platelet/megakaryocyte reviews (De Kock & Freson 2020, PMID 33255186) and SRC mouse bone-biology studies (PMID 7689855, PMID 8634424). Evidence types are flagged throughout as *human clinical*, *in vitro*, *model organism*, or *computational*.

---

## 1. Disease Information

**Overview.** THC6 (SRC-related thrombocytopenia, SRC-RT) is an ultra-rare, autosomal-dominant, syndromic **inherited macro-thrombocytopenia**. The phenotype ranges from isolated mild thrombocytopenia to a complex multisystem disease combining bleeding, dysmorphic α-granule–poor giant platelets, **early-onset myelofibrosis**, splenomegaly, bone pathology, and (in some carriers) immunodeficiency and neurological features (PMID 26936507; PMID 35349645). It is notable as the **first reported deleterious germline mutation of SRC**, a classic proto-oncogene (*human clinical / in vitro*; PMID 26936507).

**Key identifiers.**
- OMIM: **616937** (THROMBOCYTOPENIA 6; THC6)
- MONDO: **MONDO:0014837**
- Gene: **SRC**, HGNC:11283, NCBI Gene 6714, Ensembl ENSG00000197122, cytoband **20q11.23**
- Orphanet: ultra-rare inherited thrombocytopenia (no stable prevalence code; part of the "constitutional thrombocytopenia" group)
- ICD-11: **3B64.1Z / 3B64** (constitutional/hereditary thrombocytopenia, unspecified); ICD-10: **D69.42** (congenital and hereditary thrombocytopenia) — mapping is approximate (no THC6-specific code)
- MeSH: closest headings "Thrombocytopenia" (D013921), "Blood Platelet Disorders," "Primary Myelofibrosis"

**Synonyms.** SRC-related thrombocytopenia (SRC-RT); THC6; hereditary thrombocytopenia with early-onset myelofibrosis.

**Information source.** Disease-level knowledge is derived from **individual-patient case series** (not aggregated EHR registries), because the disorder is ultra-rare with <20 genetically confirmed patients reported worldwide.

---

## 2. Etiology

**Primary cause — genetic.** THC6 is a monogenic disorder caused by the heterozygous germline **SRC c.1579G>A, p.(Glu527Lys)** gain-of-function variant (*human clinical / in vitro*; PMID 26936507). No environmental or infectious cause initiates the disease.

**Genetic risk factors.**
- *Causal variant:* SRC p.E527K — the only recurrent pathogenic allele reported to date; classified **pathogenic** (ACMG/AMP) given de novo occurrence, functional gain-of-function data, absence from population databases, and segregation (PMID 26936507; PMID 31204551; PMID 35349645).
- *Susceptibility loci / modifier genes:* none established. Variable expressivity implies unidentified genetic/epigenetic modifiers. Downstream signaling partners **CSK** (C-terminal Src kinase; sets the pTyr530 brake), **BTK**, **PLCG2**, and integrin β3 (**ITGB3**) are mechanistic partners and plausible (unproven) modifier candidates.

**Environmental / lifestyle risk factors.** None causal. As general modifiers of bleeding risk: antiplatelet drugs (aspirin, NSAIDs), anticoagulants, trauma, and surgery increase bleeding; these are *exacerbating* rather than *causal* factors.

**Protective factors.** No genetic or environmental protective factors are established. Mechanistically, **SRC kinase inhibition** reverses the cellular defect in vitro (PMID 26936507) — a therapeutic rather than naturally protective lever.

**Gene–environment interactions.** Not characterized. The superimposed immune/ITP-like features in some carriers (PMID 35349645) could reflect gene–immune-environment interplay, but this is inferred, not demonstrated.

---

## 3. Phenotypes

Variable expressivity is a hallmark — even within one family, phenotypes range from isolated thrombocytopenia to full syndromic disease (PMID 35349645).

| Phenotype | Type | HPO term | Onset | Severity / course | Frequency |
|---|---|---|---|---|---|
| Thrombocytopenia (platelets ~38–139 ×10⁹/L) | Lab abnormality | HP:0001873 | Congenital/childhood | Mild–moderate, chronic, fluctuating | Essentially all patients |
| Large/giant platelets, anisocytosis | Lab/cell sign | HP:0011869; ↑MPV HP:0011877 | Congenital | Variable | Most |
| Platelet α-granule paucity | Lab (ultrastructural) | HP:0030401 | Congenital | — | Reported |
| Mucocutaneous bleeding (bruising, epistaxis, menorrhagia, GI) | Symptom/sign | HP:0000978; HP:0000421; HP:0000132 | Childhood–adult | Mild–moderate, episodic | Common |
| Early-onset myelofibrosis + trilineage dysplasia | Clinical/path sign | HP:0011974; HP:0012145 | Childhood–adult | Progressive in subset | Subset |
| Splenomegaly | Clinical sign | HP:0001744 | Variable | — | Subset |
| Bone disease (osteopenia/osteoporosis, bone pain, fractures) | Clinical sign | HP:0000939; HP:0003025 | Variable | — | Subset |
| Immune defects / recurrent infections | Clinical sign | HP:0002719 | Variable | — | 4/7 carriers in one kindred (PMID 35349645) |
| Neurological (specific language impairment, epilepsy) | Behavioral/neuro | HP:0000750; HP:0001250 | Childhood | Variable | Some family members (PMID 35349645) |

**Quality-of-life impact.** No formal EQ-5D/SF-36/PROMIS data exist for THC6. Expected impact: bleeding-related activity restriction, fatigue/transfusion burden if myelofibrosis progresses, and neurodevelopmental/educational impact where language impairment or epilepsy occur. Qualitative only.

---

## 4. Genetic / Molecular Information

- **Causal gene:** SRC (HGNC:11283; OMIM *190090; chr20q11.23). Encodes the 536-aa non-receptor tyrosine kinase c-Src with SH3, SH2, and kinase (SH1) domains plus an N-terminal myristoylation/membrane-anchor and a C-terminal regulatory tail.
- **Pathogenic variant:** **c.1579G>A, p.(Glu527Lys)**, NM_005417. Type: **missense**. Classification: **Pathogenic** (ACMG/AMP: PS3 functional, PS2/PM6 de novo, PM1 critical regulatory region adjacent to pTyr530, PM2 absent from gnomAD, PP1 segregation). It is the sole recurrent disease allele reported (PMID 26936507; PMID 31204551; PMID 35349645).
- **Allele frequency:** essentially **absent from gnomAD / 1000 Genomes / ExAC** (consistent with a highly penetrant disease allele).
- **Origin:** **germline**; arises both **inherited** (multigenerational kindreds) and **de novo** (PMID 31204551). SRC is somatically activated in many cancers, but THC6 is defined by the germline allele.
- **Functional consequence:** **gain of function / constitutive activation.** E527K lies immediately adjacent to the autoinhibitory C-terminal phosphotyrosine (pTyr530) and **"predicts loss of SRC's self-inhibitory capacity,"** confirmed in vitro by increased kinase activity and enhanced activation-loop Tyr419 autophosphorylation (PMID 26936507, *in vitro / computational*). (Note: residue numbering — E527/Y530 in the 536-aa isoform correspond to the classic E524/Y527 and avian Y416/Y527 conventions.)
- **Modifier genes:** none proven (see §2).
- **Epigenetic information:** no disease-specific methylation/chromatin data available.
- **Chromosomal abnormalities:** none; THC6 is a point-mutation disorder (no CNV/translocation association). Bone marrow may show trilineage **dysplasia** but not a defining karyotype.

---

## 5. Environmental Information

- **Environmental factors / toxins / radiation:** none implicated as causal.
- **Lifestyle factors:** no causal role; antiplatelet agents and alcohol can worsen bleeding tendency (general principle).
- **Infectious agents:** not a cause. Recurrent infections observed in some carriers are a *consequence* of the associated immune defect, not a trigger (PMID 35349645).

*Not applicable / not available for most environmental sub-items — THC6 is a purely genetic disorder.*

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Germline SRC c.1579G>A (p.E527K) mutation** occurs adjacent to the C-terminal regulatory tyrosine (pTyr530) → **leads to** loss of the intramolecular pTyr530–SH2 autoinhibitory clamp (*computational/in vitro*; PMID 26936507).
2. Loss of the clamp → **results in** SRC being locked in the open, catalytically active conformation with enhanced autophosphorylation at activation-loop Tyr419 → **constitutive kinase activity** (*in vitro*; PMID 26936507).
3. Constitutive SRC activity → **leads to** globally enhanced tyrosine phosphorylation in platelets and megakaryocytes (MKs); the active form predominates in patient platelets (*human clinical*; PMID 26936507).
   - **Branch A (platelet-production defect, primary):** hyperactive SRC → **drives** formation of Tyr419-SRC–positive **podosomes** that **induce altered actin cytoskeletal organization** in MKs → **results in** reduced **proplatelet formation** → **thrombocytopenia** with dysmorphic, size-variable, **α-granule–poor** platelets. This step is **pharmacologically reversible by SRC inhibition** (*human clinical / in vitro*; PMID 26936507).
   - **Branch B (marrow/fibrosis):** abnormal MK signaling in a hypercellular marrow with trilineage dysplasia → **contributes to** **early-onset myelofibrosis** (reticulin fibrosis) and splenomegaly / extramedullary hematopoiesis (*human clinical*; PMID 26936507). Patient stem cells form more myeloid and MK colonies in vitro.
   - **Branch C (bone):** SRC is essential for **osteoclast** ruffled-border formation and bone resorption; dysregulated SRC activity → **leads to** abnormal bone remodeling and bone disease. Inferred from the central role of SRC in osteoclasts (*model organism*; Src-knockout mouse osteopetrosis, PMID 7689855).
   - **Branch D (immune/neuro):** constitutive activation of downstream **BTK** and **PLCG2**, with increased ERK phosphorylation in B cells on sIgM crosslinking → **contributes to** immune dysregulation / recurrent infections; neurological features (language impairment, epilepsy) reflect SRC's broad CNS expression (mechanism inferred) (*human clinical*; PMID 35349645).
4. Platelet number reduction + mild platelet-function impairment → **results in** the clinical **bleeding** phenotype (*human clinical*).

### Detail by category
- **Molecular pathways:** SRC-family-kinase (SFK) signaling; ITAM/GPVI and integrin αIIbβ3 **outside-in** signaling; SRC→SYK→BTK→PLCγ2 and SRC→RAS/MAPK(ERK) cascades (PMID 33255186; PMID 35349645). KEGG/Reactome anchors: Reactome "GPVI-mediated activation cascade," "Integrin αIIbβ3 signaling."
- **Cellular processes:** actin cytoskeleton organization, podosome assembly, megakaryocyte maturation/proplatelet formation, bone resorption, B-cell receptor signaling.
- **Protein dysfunction:** gain-of-function via disrupted autoinhibition (not misfolding/aggregation). PDB references for SRC autoinhibited conformation: **1FMK, 2SRC**; AlphaFold AF-P12931.
- **Immune involvement:** constitutive BTK/PLCγ2/ERK activation; recurrent infections in a subset — a mixed immunodeficiency/autoimmune picture (PMID 35349645).
- **Tissue-damage mechanism:** marrow **fibrosis** (reticulin deposition) is the principal tissue-injury readout.
- **GO terms (BP):** GO:0018108 peptidyl-tyrosine phosphorylation; GO:0004715 non-membrane-spanning protein tyrosine kinase activity; GO:0030036 actin cytoskeleton organization; GO:0030220 platelet formation; GO:0002576 platelet degranulation; GO:0045453 bone resorption.
- **GO terms (CC):** GO:0031091 platelet alpha granule; GO:0002102 podosome; GO:0005856 cytoskeleton.
- **Cell types (CL):** CL:0000556 megakaryocyte; CL:0000233 platelet; CL:0000092 osteoclast; CL:0000236 B cell; CL:0000037 hematopoietic stem cell.
- **Molecular profiling:** no published transcriptomic/proteomic/metabolomic datasets specific to THC6; key experimental readouts are phospho-tyrosine Western blots and MK colony/proplatelet assays (PMID 26936507).

**Upstream vs downstream:** the mutation and constitutive kinase activity are **upstream**; podosome/actin dysregulation and impaired proplatelet formation are **midstream**; thrombocytopenia, myelofibrosis, bone disease, bleeding are **downstream** manifestations.

---

## 7. Anatomical Structures Affected

- **Organ level — primary:** **bone marrow** (UBERON:0002371) and the **blood/hematopoietic system** (UBERON:0000178); **bone/skeleton** (UBERON:0001474).
- **Secondary involvement:** **spleen** (UBERON:0002106; splenomegaly, extramedullary hematopoiesis); **skin/mucosa** (UBERON:0002097; bleeding/bruising); **immune system**; **central nervous system** (UBERON:0001017; language impairment, epilepsy — subset).
- **Body systems:** hematologic, skeletal, immune, and (variably) nervous systems.
- **Tissue/cell level:** connective/hematopoietic marrow stroma (fibrosis); target cells — **megakaryocytes** (CL:0000556), **platelets** (CL:0000233), **osteoclasts** (CL:0000092), **B lymphocytes** (CL:0000236).
- **Subcellular (GO CC):** platelet **α-granules** (GO:0031091; deficient), **podosomes** (GO:0002102), actin **cytoskeleton** (GO:0005856); plasma-membrane inner leaflet (SRC myristoyl anchor).
- **Localization / laterality:** systemic/bilateral (hematologic disease); no lateralization.

---

## 8. Temporal Development

- **Onset:** **congenital/pediatric** thrombocytopenia (present from early life), often detected incidentally; syndromic features (myelofibrosis, bone, splenomegaly) may be recognized in childhood or adulthood. Pattern is **chronic/insidious** (PMID 26936507; PMID 35349645).
- **Progression:** thrombocytopenia is generally **stable/fluctuating** and lifelong; **myelofibrosis can be progressive** in a subset (hence "early-onset myelofibrosis"). Platelet counts fluctuate (e.g., 38–139 ×10⁹/L) (PMID 35349645).
- **Disease course / duration:** chronic, lifelong.
- **Remission:** no spontaneous remission of the genetic disorder; apparent "responses" to corticosteroids/splenectomy reflect a superimposed immune component or spleen removal rather than cure (PMID 35349645).
- **Critical periods / intervention windows:** avoiding misdiagnosis as ITP (and thus unnecessary immunosuppression/splenectomy) is the key actionable window; perioperative and peripartum periods require bleeding-risk management.

---

## 9. Inheritance and Population

- **Epidemiology:** **ultra-rare**; <20 genetically confirmed patients from a handful of unrelated families reported worldwide (PMID 35349645: "genetic diagnosis of the disease has only been reported in 7 patients from 3 unrelated families"). No reliable prevalence/incidence estimate exists.
- **Inheritance:** **autosomal dominant** (PMID 35349645).
- **Penetrance:** appears **high** for thrombocytopenia; **variable expressivity** for syndromic features.
- **Expressivity:** **highly variable**, intra- and inter-familial (isolated thrombocytopenia → full syndrome) (PMID 35349645).
- **Anticipation:** not a repeat-expansion disorder; no anticipation.
- **De novo / mosaicism:** **de novo occurrence documented** (PMID 31204551); germline mosaicism not specifically reported.
- **Founder effect / consanguinity:** none; recurrence reflects independent mutation of the same nucleotide, not a founder haplotype. Consanguinity irrelevant (dominant).
- **Carrier frequency:** not applicable (dominant, fully penetrant-for-thrombocytopenia; allele absent from gnomAD).
- **Demographics:** reported in European populations (British, Belgian, Spanish); no established ethnic predilection. **No sex bias** (autosomal). Age distribution: present from childhood, recognized across the lifespan.

---

## 10. Diagnostics

- **Laboratory:** CBC — thrombocytopenia with **increased MPV** and anisocytosis; peripheral smear/flow cytometry — **large-to-giant dysmorphic platelets**, **increased immature platelet fraction (>15%)**; **light transmission aggregometry** — mildly impaired function; **electron microscopy** — **α-granule paucity** (PMID 26936507; PMID 35349645). LOINC anchors: platelet count 777-3; MPV 32623-1.
- **Bone marrow biopsy:** hypercellular marrow, **reticulin myelofibrosis**, **trilineage dysplasia**, dysmorphic megakaryocytes (PMID 26936507).
- **Imaging:** ultrasound/CT for **splenomegaly**; skeletal imaging/DXA for bone disease.
- **Biomarker (research):** elevated active-SRC and global platelet phospho-tyrosine; constitutive BTK/PLCγ2 activation (PMID 35349645) — not yet standard clinical assays.
- **Genetic testing (definitive):** targeted **NGS inherited-platelet-disorder gene panels**, **whole-exome**, or **whole-genome sequencing** identifying **SRC c.1579G>A p.(Glu527Lys)**; single-gene Sanger confirmation and **cascade testing** of relatives (PMID 26936507; general IPD workflows PMID 31249973, PMID 42082146). CMA/karyotype/FISH are generally uninformative (point mutation).
- **Clinical criteria / differential diagnosis:** no formal society criteria; diagnosis rests on phenotype + molecular confirmation. **Differential:** immune thrombocytopenia (ITP), **MYH9-related disease** and other inherited macrothrombocytopenias, Bernard–Soulier syndrome, gray platelet syndrome (α-granule deficiency), and **primary myelofibrosis**. Distinguishing feature: family history + SRC genotype; the ITP overlap is the key pitfall (PMID 35349645).
- **Screening:** no population/newborn screening. **Cascade genetic screening** of at-risk relatives and **genetic counseling** are appropriate; prenatal/PGT is theoretically possible for known-variant families.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** no formal survival statistics. Prognosis depends on **myelofibrosis** progression and bleeding severity; isolated-thrombocytopenia patients may have near-normal life expectancy, whereas progressive myelofibrosis carries greater morbidity/mortality risk (inferred from phenotype; PMID 26936507).
- **Morbidity/disability:** bleeding, transfusion dependence if marrow failure advances, bone disease/fractures, and neurodevelopmental impact (language impairment, epilepsy) in a subset.
- **QoL measures:** none validated for THC6.
- **Complications:** significant hemorrhage (surgery/trauma/peripartum), progression to marrow fibrosis/cytopenias, recurrent infections (immune subset), splenomegaly-related issues.
- **Recovery potential:** the underlying genetic defect is non-reversible; targeted SRC inhibition is investigational.
- **Prognostic factors:** degree of marrow fibrosis, platelet count/bleeding history, presence of syndromic features; **no validated prognostic biomarker**. Whether THC6 confers a myeloid-malignancy predisposition (as some germline platelet-disorder genes do) is **not established** and warrants surveillance.

---

## 12. Treatment

No disease-specific approved therapy exists; management is extrapolated from inherited thrombocytopenia practice (PMID 32527953; PMID 18278172).

- **Supportive hemostatic care (mainstay):** **antifibrinolytics** — tranexamic acid (CHEBI:48669; NCIT C47720) / aminocaproic acid for mucosal bleeding and procedures; **platelet transfusion** (NCIT C15360) for major bleeding or surgical cover; **avoid antiplatelet agents/NSAIDs**; desmopressin may be considered for procedures (general practice).
- **Caution — ITP overtreatment:** because SRC-RT mimics ITP, patients have received **corticosteroids** and **splenectomy** (NCIT C15431); in one kindred four adults underwent splenectomy with sustained platelet counts >75 ×10⁹/L and transient corticosteroid responses — suggesting a real but incomplete immune component, while underscoring the risk of **inappropriate splenectomy** (PMID 35349645). **Correct genetic diagnosis prevents harmful over-treatment.**
- **Mechanism-targeted (investigational):** **SRC tyrosine kinase inhibitors** (e.g., **dasatinib**, NCIT C62491; saracatinib/AZD0530) **rescued proplatelet formation** in patient-derived and E527K-transduced megakaryocytes in vitro (PMID 26936507) — strong proof-of-concept, but **no clinical trial in THC6** has been reported. Paradox/caveat: SRC inhibitors themselves can cause thrombocytopenia/bleeding, so clinical translation would require careful dose-finding.
- **Advanced therapeutics:** gene therapy, RNA-based, or allele-selective approaches are conceptually attractive (dominant single recurrent allele) but not developed. Allogeneic **hematopoietic stem cell transplantation** is the only potentially curative option conceivable for severe marrow failure/myelofibrosis but is unreported for THC6 specifically.
- **Pharmacogenomics:** not applicable beyond the target itself.
- **Treatment strategy / personalized medicine:** genotype-guided — confirm SRC p.E527K, then prioritize conservative hemostatic management, bleeding-risk counseling, and myelofibrosis/bone surveillance; reserve SRC-inhibitor concepts for research settings.
- **NCIT terms:** C62491 Dasatinib; C1967 Tyrosine Kinase Inhibitor; C47720 Tranexamic Acid; C15431 Splenectomy; C15360 Transfusion; C15431/stem-cell C15431→C96746 HSCT.

---

## 13. Prevention

- **Primary prevention:** not possible (genetic). **Genetic counseling** for autosomal-dominant 50% transmission risk; options include prenatal diagnosis and **preimplantation genetic testing** for families with the known variant.
- **Secondary prevention:** **cascade genetic testing** of relatives for early identification; baseline/periodic monitoring of platelet counts, marrow (if indicated), and bone health.
- **Tertiary prevention:** prevent bleeding complications (avoid antiplatelet drugs, pre-procedural tranexamic acid/platelet cover), monitor/manage myelofibrosis and bone disease, manage infections in the immune subset.
- **Immunization / public-health / environmental measures:** standard care; no disease-specific vaccine or environmental intervention. Routine vaccination is prudent given the immune-defect subset.
- **Prophylaxis:** peri-operative/peripartum antifibrinolytics and platelet support as needed.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** SRC is highly conserved. Orthologs: mouse *Src* (NCBI Gene 20779; Taxon 10090), rat *Src* (Taxon 10116), zebrafish *src* (Taxon 7955), with homologs across vertebrates (HomoloGene group for SRC).
- **Natural disease in other species:** **no naturally occurring animal homolog of THC6** is catalogued (no OMIA entry for a spontaneous SRC-E527K thrombocytopenia). Not applicable.
- **Veterinary relevance:** none established.
- **Comparative biology:** SRC's role in osteoclast-mediated bone resorption and in platelet/MK signaling is evolutionarily conserved; the opposing bone phenotypes of human GOF disease vs mouse LOF osteopetrosis illustrate SRC dosage sensitivity in the skeleton.
- **Transmission / zoonosis:** not applicable (non-infectious genetic disease).

---

## 15. Model Organisms

- **Zebrafish (Danio rerio; Taxon 7955) — disease model:** expression of **mutant src recapitulated patient phenotypes** in vivo, providing a gain-of-function model aligned with the human disease (*model organism*; PMID 26936507). Resource: ZFIN.
- **Mouse (Mus musculus; Taxon 10090) — mechanism models (loss-of-function):** germline **Src-knockout** mice develop **osteopetrosis** from osteoclast ruffled-border failure, persisting to 9–10 months without remission (PMID 7689855); **Hck/Src double-knockout** mice show severe osteopetrosis with extramedullary hematopoiesis, anemia, and leukopenia, revealing partial SFK functional overlap in osteoclasts (PMID 8634424). These are LOF (opposite perturbation to the human GOF disease) but establish SRC's non-redundant role in bone and marrow. Resources: MGI, IMPC/IMSR.
- **Cellular / in vitro models:** COS-7 overexpression of E527K SRC (kinase-activity/phospho-Tyr419 assays); **patient-derived and lentiviral E527K-transduced hematopoietic stem cells → megakaryocytes** reproducing impaired proplatelet formation, rescued by SRC inhibition (PMID 26936507). iPSC-MK models are a logical extension (not yet reported).
- **Model characteristics:** zebrafish GOF captures the disease direction; mouse LOF captures the bone pathway but not the thrombocytopenia direction. **Limitation:** no mouse knock-in E527K model has been reported, leaving a gap for in vivo GOF hematologic modeling.
- **Applications:** dissecting MK cytoskeletal/podosome biology, testing SRC-inhibitor rescue, and studying SRC in bone remodeling.

---

## Evidence Summary (key PMIDs)
- **26936507** — Turro et al. 2016, *Sci Transl Med* — discovery; E527K gain-of-function; MK/platelet/bone phenotype; zebrafish & in vitro models; SRC-inhibitor rescue (landmark, *human clinical + in vitro + model organism*).
- **31204551** — De Kock et al. 2019 — second family, **de novo** SRC variant (*human clinical*).
- **35349645** — Palma-Barqueros et al. 2022 — additional 3-generation kindred; variable expressivity; ITP overlap/splenectomy; BTK/PLCγ2 activation; immune & neuro features (*human clinical*).
- **33255186** — De Kock & Freson 2020 — SRC (patho)biology in platelets/MKs (review).
- **7689855 / 8634424** — Src-knockout mouse osteopetrosis / osteoclast biology (*model organism*).
- **32527953 / 18278172** — Nurden & Nurden — inherited thrombocytopenia framework & management (reviews).

## Limitations and Future Directions
- Ultra-rare (<20 patients): phenotype frequencies and natural history are imprecise; no QoL, survival, or prevalence statistics.
- Single recurrent allele studied; modifier genes explaining variable expressivity are unknown.
- No in vivo mammalian GOF knock-in model; no clinical trial of SRC inhibitors; malignancy-predisposition risk unquantified.
- Priorities: knock-in mouse / iPSC-MK models, careful SRC-inhibitor dose-finding studies, longitudinal natural-history and myelofibrosis-progression data, and clarification of the immune/neurological components.


## Artifacts

- [OpenScientist final report](Thrombocytopenia_6-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Thrombocytopenia_6-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 39 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 13 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001873` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Thrombocytopenia**
- `HP:0030401` (1 mention) - the report calls it "Lab (ultrastructural)"; HP calls it **Abnormal platelet dense granule ATP/ADP ratio**
- `HP:0001744` (1 mention) - the report calls it "Clinical sign"; HP calls it **Splenomegaly**
- `HP:0002719` (1 mention) - the report calls it "Clinical sign"; HP calls it **Recurrent infections**
- `UBERON:0000178` (1 mention) - the report calls it "blood/hematopoietic system"; UBERON calls it **blood**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000236` (2 mentions) - the report calls it "B lymphocytes"; CL calls it **B cell**, and lists "B lymphocyte" among its other names
- `UBERON:0002371` (1 mention) - the report calls it "bone marrow", "Organ level — primary:** **bone marrow"; UBERON calls it **bone marrow**
- `UBERON:0001474` (1 mention) - the report calls it "bone/skeleton"; UBERON calls it **bone element**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0002371` - called "bone marrow", "Organ level — primary:** **bone marrow"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.