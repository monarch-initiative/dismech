---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T18:54:55.047007'
end_time: '2026-10-31T19:09:10.394981'
duration_seconds: 855.35
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: '"ANKRD26-Related Thrombocytopenia"'
  mondo_id: MONDO:0008555
  category: Mendelian
  causal_genes: ANKRD26
  omim_id: OMIM:188000
  synonyms: THC2
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
citation_count: 15
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 15
  quotes_valid: 12
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMID:12745278
  - PMID:12161364
  - PMID:39443230
  relevance_assessed: 17
  on_topic: 12
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 28
  verified: 25
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 19
  labels_matching: 11
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0008555
    reported_labels:
    - MONDO
    ontology_label: thrombocytopenia 2
  - term_id: HP:0001873
    reported_labels:
    - Lab abnormality
    ontology_label: Thrombocytopenia
  - term_id: HP:0030401
    reported_labels:
    - Lab/morphology
    ontology_label: Abnormal platelet dense granule ATP/ADP ratio
  - term_id: NCIT:C62492
    reported_labels:
    - eltrombopag
    ontology_label: Denenicokin
  labels_variant: 4
  unresolvable_prefixes:
  - ORPHA
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ANKRD26-Related_Thrombocytopenia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ANKRD26-Related_Thrombocytopenia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** "ANKRD26-Related Thrombocytopenia"
- **MONDO ID:** MONDO:0008555 (if available)
- **Causal gene(s):** ANKRD26
- **OMIM:** OMIM:188000
- **Synonyms:** THC2
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **"ANKRD26-Related Thrombocytopenia"** covering all of the
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

# ANKRD26-Related Thrombocytopenia (THC2): A Comprehensive Disease Characteristics Report

**Disease:** ANKRD26-Related Thrombocytopenia (THC2)
**MONDO ID:** MONDO:0008555 | **OMIM:** 188000 (THC2 phenotype; *ANKRD26* gene MIM 610855) | **Causal gene:** *ANKRD26* (Ankyrin Repeat Domain 26; HGNC:21026; NCBI Gene 22852; chromosome 10p12.1) | **Orphanet:** ORPHA:3322 | **Synonyms:** THC2, Thrombocytopenia 2, ANKRD26-RT
**Category:** Mendelian, autosomal dominant

---

## Summary

**ANKRD26-Related Thrombocytopenia (THC2) is an autosomal-dominant inherited platelet-production disorder caused by germline gain-of-expression point variants (and small indels) in the 5′ untranslated region (5′UTR) of the *ANKRD26* gene.** Despite the serial "thrombocytopenia 2" name, the causal gene is unambiguously *ANKRD26* (not the neighboring *MASTL* or *ACBD5* genes at the same 10p12.1 locus, which were historically proposed and later excluded by fine-mapping). The disease is defined by lifelong, usually mild-to-moderate thrombocytopenia with a hallmark distinguishing feature — **normal platelet size (normocytic platelets)** — which separates it from most other inherited thrombocytopenias that present with macrothrombocytopenia.

The core molecular lesion is loss of transcriptional repression. Recurrent single-nucleotide variants clustered in a highly conserved 19-bp region of the *ANKRD26* 5′UTR abolish binding of the master megakaryopoietic repressors **RUNX1 and FLI1**. Normally these factors silence *ANKRD26* during terminal megakaryocyte (MK) maturation; when their binding is lost, *ANKRD26* expression persists inappropriately. Sustained ANKRD26 protein stabilizes the type I cytokine receptors MPL, EPOR and G-CSFR by preventing their internalization, hyperactivates the **MAPK/ERK** signaling cascade, and impairs proplatelet formation. Single-cell studies further show that elevated ANKRD26 localizes to the centrosome and drives **JUNB-mediated transcriptional activation of p21**, inducing apoptosis of polyploid megakaryocytes — producing the dysmegakaryopoiesis that underlies the low platelet count.

The principal clinical significance of THC2 is not its usually-mild bleeding tendency but its **substantial lifetime predisposition to myeloid malignancy** (AML, MDS, CMML; estimated 10–45% across the RUNX1/ETV6/ANKRD26 group of inherited-thrombocytopenia-with-malignancy-risk disorders). There is no disease-modifying therapy. Management is supportive and centers on avoiding misdiagnosis as immune thrombocytopenia (ITP), perioperative platelet support (with the TPO-receptor agonist eltrombopag as an effective alternative to transfusion), genetic counseling with cascade testing, informed donor selection for any future hematopoietic stem cell transplant, and lifelong hematologic surveillance for clonal evolution.

> **Evidence basis:** This report integrates human clinical cohorts/registries, patient-derived primary megakaryocytes and iPSCs, single-cell bone-marrow profiling, and one murine knockout. No proprietary patient-level/EHR data were used; all content derives from aggregated disease-level literature and ontologies.

---

## 1. Disease Information

**Overview.** THC2 is a Mendelian, autosomal-dominant, non-syndromic inherited thrombocytopenia caused by germline variants in the 5′UTR of *ANKRD26*. It is characterized by mild-to-moderate reduction in platelet count, normal-sized platelets, usually mild (or absent) bleeding, dysmegakaryopoiesis in the bone marrow, and a clinically important predisposition to hematologic (predominantly myeloid) neoplasms.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0008555 |
| OMIM | 188000 (THC2 phenotype); *ANKRD26* gene MIM 610855 |
| Orphanet | ORPHA:3322 |
| Gene (HGNC) | *ANKRD26*, HGNC:21026 |
| NCBI Gene | 22852 |
| Gene locus | 10p12.1 |
| Synonyms | THC2, Thrombocytopenia 2, ANKRD26-related thrombocytopenia (ANKRD26-RT) |

**Information source.** The knowledge in this report derives predominantly from **aggregated disease-level resources** — cohort studies, inherited-thrombocytopenia registries (Italian and Japanese), case series, and functional laboratory studies — rather than from individual EHR records. The largest clinical description is a cohort of 78 patients from 21 families [PMID: 21467542](https://pubmed.ncbi.nlm.nih.gov/21467542/).

---

## 2. Etiology

**Disease causal factors.** THC2 is a purely **genetic (Mendelian)** disorder. There is no known environmental, infectious, or acquired cause of the primary disease. The causal lesion is a germline point mutation (or small deletion) in the conserved 19-bp region of the *ANKRD26* 5′UTR that disrupts RUNX1/FLI1 repressor binding, producing a **gain of ANKRD26 expression** (not haploinsufficiency) [PMID: 21211618](https://pubmed.ncbi.nlm.nih.gov/21211618/).

**Genetic risk factors.** The causal variants themselves are the primary genetic risk factor. Six distinct 5′UTR mutations were originally identified across 8 unrelated families, all clustered in the conserved 19-bp hotspot and absent from 500 controls and the 1000 Genomes database [PMID: 21211618](https://pubmed.ncbi.nlm.nih.gov/21211618/). Recurrent hotspot positions span roughly nucleotides −140 to −113 (e.g., c.-128G>A, c.-127A>T, c.-126T>G, c.-125T>G, c.-118C>T, c.-116C>T, c.-113A>C), plus later-described variants such as the deletion c.-129_-112del that disrupts the RUNX1-binding site [PMID: 40954090](https://pubmed.ncbi.nlm.nih.gov/40954090/).

**Modifier genes.** *GATA2* acts as a **positive regulator** of *ANKRD26* transcription in myeloid-derived cells, opposing RUNX1/FLI1 repression and adding a regulatory layer to the GATA2–ANKRD26 axis [PMID: 38817334](https://pubmed.ncbi.nlm.nih.gov/38817334/). Somatic driver mutations acquired in hematopoietic regulators on the germline *ANKRD26* background are the key modifiers of malignant transformation risk (see §4, §11).

**Environmental / lifestyle / protective factors.** No environmental risk factors, protective variants, or gene–environment interactions have been established for THC2. This is consistent with a monogenic germline disorder. *Not applicable / not available* for most environmental subcategories.

---

## 3. Phenotypes

THC2 phenotypes are predominantly **laboratory abnormalities** and **hemorrhagic clinical signs**, usually mild.

| Phenotype | Type | HPO suggestion | Onset | Severity | Frequency |
|---|---|---|---|---|---|
| Thrombocytopenia | Lab abnormality | HP:0001873 | Congenital/lifelong | Mild–moderate | ~100% (defining) |
| Normal platelet size (normocytic) | Lab/morphology | (normal MPV; absence of HP:0011877) | Lifelong | — | Nearly all patients |
| Bleeding tendency (mild; mucocutaneous, bruising) | Clinical sign | HP:0001892 (abnormal bleeding) | Variable | Mild | ~25–30% |
| Glycoprotein Ia (ITGA2/GPIa) deficiency | Lab abnormality | HP:0011869 (platelet dysfunction) | Lifelong | — | Majority of cases |
| α-granule deficiency | Lab/morphology | HP:0030401 | Lifelong | — | Majority of cases |
| Dysmegakaryopoiesis (marrow) | Lab/pathology | HP:0012757 | Lifelong | — | Characteristic |
| Elevated serum thrombopoietin | Lab abnormality | — | Lifelong | — | Common |
| Predisposition to myeloid neoplasia | Clinical course | HP:0004377 (hematological neoplasm) | Adult (variable) | Severe when present | 10–45% (group estimate) |
| Occasional high hemoglobin / leukocytosis | Lab abnormality | HP:0001899 / HP:0001974 | Variable | Mild | A few cases |

**Characteristics.** In the 78-patient / 21-family cohort, "thrombocytopenia and bleeding tendency were usually mild. Nearly all patients had no platelet macrocytosis, and this characteristic distinguishes THC2 from most other forms of inherited thrombocytopenia. In the majority of cases, platelets were deficient in glycoprotein Ia and α-granules, whereas in vitro platelet aggregation was normal" [PMID: 21467542](https://pubmed.ncbi.nlm.nih.gov/21467542/). A more recent multicenter cohort tempered the "normal aggregation" description: platelet aggregation was impaired in 90% of all inherited-thrombocytopenia patients studied, with heterogeneous activation and granule secretion, and bleeding tendency present in 25–30% of ANKRD26-RT (and RUNX1-RT) patients — "Bleeding tendency was present in 25%-30% of RUNX1-RT and ANKRD26-RT patients. Platelet aggregation was impaired in 90% of all patients, while reduced activation and granule secretion were heterogeneous" [PMID: 40670159](https://pubmed.ncbi.nlm.nih.gov/40670159/).

**Quality of life impact.** Because bleeding is generally mild, the day-to-day QoL impact of the thrombocytopenia itself is modest for most patients. The dominant QoL burden is **psychological and surveillance-related** — living with a cancer-predisposition diagnosis and undergoing lifelong monitoring — and the morbidity of any malignancy that develops. Formal EQ-5D/SF-36 data specific to THC2 are *not available*.

---

## 4. Genetic / Molecular Information

**Causal gene.** *ANKRD26* (Ankyrin Repeat Domain 26), 10p12.1, HGNC:21026, NCBI Gene 22852. *ANKRD26* is the evolutionary ancestor of the primate-specific *POTE* proapoptotic gene family [PMID: 21211618](https://pubmed.ncbi.nlm.nih.gov/21211618/).

**Pathogenic variants.**
- **Variant type/class:** Predominantly single-nucleotide substitutions in the 5′UTR; also small deletions (e.g., c.-129_-112del). These are **regulatory (non-coding) variants**, an unusual class for a Mendelian disorder.
- **Location:** Clustered in a highly conserved 19-bp sequence of the 5′UTR, spanning approximately nucleotides −140 to −113.
- **Classification (ACMG/AMP):** The recurrent hotspot 5′UTR variants are classified **pathogenic/likely pathogenic** in ClinVar; novel 5′UTR variants outside the canonical hotspot and coding variants of uncertain significance (VUS) require functional interpretation.
- **Allele frequency:** Extremely rare — original mutations absent from 500 controls and the 1000 Genomes database [PMID: 21211618](https://pubmed.ncbi.nlm.nih.gov/21211618/).
- **Origin:** **Germline.** Somatic mutations in other genes accrue on this background during leukemic transformation.
- **Functional consequence:** **Gain of expression** (not loss of function / not haploinsufficiency). "The luciferase reporter assay suggests that these 5′ UTR mutations might enhance *ANKRD26* expression," and "available data from an animal model and Dr. Watson's genome give evidence against haploinsufficiency as the pathogenetic mechanism" [PMID: 21211618](https://pubmed.ncbi.nlm.nih.gov/21211618/).

**Mechanistic basis of the gain of expression.** THC2 5′UTR mutations cause **loss of RUNX1 and FLI1 binding**: "THC2-associated mutations in the 5′ UTR of ANKRD26 resulted in loss of runt-related transcription factor 1 (RUNX1) and friend leukemia integration 1 transcription factor (FLI1) binding" [PMID: 24430186](https://pubmed.ncbi.nlm.nih.gov/24430186/). A Japanese registry independently confirmed a novel variant that "disrupted the runt-related transcription factor 1 (RUNX1)-binding site, leading to ANKRD26 overexpression and possible haematopoietic abnormalities," with higher transcript levels (p<0.001), reduced proplatelet formation, and lower nuclear ploidy [PMID: 40954090](https://pubmed.ncbi.nlm.nih.gov/40954090/).

**Modifier genes.** *GATA2* positively regulates *ANKRD26* [PMID: 38817334](https://pubmed.ncbi.nlm.nih.gov/38817334/). Somatic drivers in hematopoietic regulators determine transformation [PMID: 35751752](https://pubmed.ncbi.nlm.nih.gov/35751752/).

**Epigenetic / chromosomal.** No recurrent epigenetic signature or large chromosomal abnormality defines germline THC2. Clonal cytogenetic/molecular changes appear only with malignant transformation. *Not applicable* for the primary disorder.

---

## 5. Environmental Information

No environmental factors, lifestyle factors, or infectious agents are known to cause or trigger THC2. It is a monogenic germline disorder. General hematologic prudence (avoiding unnecessary antiplatelet agents, and caution with leukemogenic exposures given the cancer predisposition) is advisable, but no specific environmental trigger is established. **Not applicable** for environmental etiology.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A germline point mutation (or small deletion) arises in the conserved 19-bp region of the *ANKRD26* 5′UTR → **destroys the RUNX1/FLI1 repressor binding site** (demonstrated) [PMID: 24430186].
2. Loss of RUNX1/FLI1 binding → **failure to silence *ANKRD26* during terminal megakaryopoiesis** → sustained/elevated ANKRD26 protein (demonstrated by reporter assays and patient MKs) [PMID: 21211618, 24430186].
3. Elevated ANKRD26 **binds and stabilizes the type I cytokine receptors MPL, EPOR and G-CSFR by preventing their internalization** → increased receptor signaling and cytokine hypersensitivity (demonstrated) [PMID: 36794499].
4. Increased MPL/TPO signaling → **hyperactivation of the MAPK/ERK cascade** (demonstrated) [PMID: 24430186].
5. **Branch A — maturation/proplatelet defect:** MAPK/ERK hyperactivation → **impaired proplatelet formation** by megakaryocytes; ERK inhibition completely rescues proplatelet formation in vitro, proving causality [PMID: 24430186].
6. **Branch B — apoptotic depletion of mature MKs:** elevated ANKRD26 localizes to the **centrosome** (implicating mitotic regulation) → drives **JUNB-mediated transcriptional activation of p21** → **apoptosis of polyploid megakaryocytes** (demonstrated by single-cell profiling) [PMID: 41538704].
7. Branches A+B converge → **dysmegakaryopoiesis**: expansion of megakaryocyte progenitors (MkP) with loss of polyploid/terminal MKs and reduced platelet output (demonstrated) [PMID: 41538704].
8. Reduced effective platelet production → **mild-to-moderate thrombocytopenia with normal-sized platelets** and compensatory elevated serum thrombopoietin (clinical observation) [PMID: 21467542].
9. **Separate long-term branch — leukemogenesis:** the germline gain-of-expression background + acquisition of **somatic driver mutations** in hematopoietic regulators → clonal evolution → **MDS / AML / CMML** (demonstrated/inferred two-hit model) [PMID: 35751752].

### Mechanism schematic

```
 5'UTR mutation (conserved 19-bp)
        │ abolishes
        ▼
 RUNX1 / FLI1 repressor binding  ◄──(GATA2 positively regulates ANKRD26)
        │ loss of silencing
        ▼
 Persistent / elevated ANKRD26 ──────────────┐
        │                                     │ centrosome localization
        │ stabilizes receptors                ▼
        ▼                              JUNB → p21 (CDKN1A)
 MPL / EPOR / G-CSFR  (no internalization)     │
        │ ↑ signaling / cytokine hypersensitivity
        ▼                                      ▼
 MAPK / ERK hyperactivation          Apoptosis of polyploid MKs
        │                                      │
        ▼                                      │
 Impaired proplatelet formation ◄──────────────┘
        │
        ▼
 Dysmegakaryopoiesis (MkP expansion, polyploid-MK loss)
        │
        ▼
 Normocytic mild–moderate THROMBOCYTOPENIA
        │  (+ germline background + somatic drivers over decades)
        ▼
 Predisposition to MDS / AML / CMML
```

**Supporting quotes.** "persistent ANKRD26 expression in isolated MKs increased signaling via the thrombopoietin/myeloproliferative leukemia virus oncogene (MPL) pathway and impaired proplatelet formation by MKs. Importantly, we demonstrated that ERK inhibition completely rescued the in vitro proplatelet formation defect" [PMID: 24430186]. "ANKRD26 interacts with and crucially modulates the activity of MPL, EPOR and G-CSFR, three homodimeric type I cytokine receptors that regulate blood cell production. Higher than normal levels of ANKRD26 prevent the receptor internalization that leads to increased signaling and cytokine hypersensitivity" [PMID: 36794499]. "Confocal imaging localized ANKRD26 to the centrosome, implicating it in mitotic regulation during MK maturation. Mechanistically, we discovered that elevated ANKRD26 induces apoptosis in polyploid MKs via JUNB-mediated transcriptional activation" [PMID: 41538704].

**Pathways and ontology mapping.** Molecular pathways: TPO–MPL signaling; MAPK/ERK cascade (KEGG hsa04010); type I cytokine receptor signaling (MPL, EPOR, CSF3R). Cellular processes: megakaryocyte maturation/polyploidization (endomitosis), proplatelet formation, apoptosis. Protein dysfunction: ANKRD26 overexpression is a **gain-of-function at the expression level** that dysregulates receptor trafficking. **Suggested GO terms:** GO:0030220 (platelet formation), GO:0002576 (platelet degranulation), GO:0000278 (mitotic cell cycle), GO:0006915 (apoptotic process), GO:0019221 (cytokine-mediated signaling pathway). **Suggested CL terms:** CL:0000556 (megakaryocyte), CL:0000763 (myeloid cell), CL:0000037 (hematopoietic stem cell), CL:0000233 (platelet).

---

## 7. Anatomical Structures Affected

- **Primary organ/tissue:** Bone marrow (UBERON:0002371), specifically the megakaryocytic lineage; peripheral blood platelets.
- **Body system:** Hematopoietic / hematologic system (UBERON:0002390 bone marrow; UBERON:0000178 blood).
- **Cell populations:** Megakaryocytes and their progenitors (CL:0000556 megakaryocyte; megakaryocyte progenitor), hematopoietic stem/progenitor cells (CL:0000037), platelets (CL:0000233). Multilineage receptor modulation (MPL/EPOR/G-CSFR) means erythroid and granulocytic lineages can be subtly affected (occasional high hemoglobin/leukocytes) [PMID: 21467542, 36794499].
- **Subcellular level:** **Centrosome** (GO:0005813) — site of ANKRD26 localization implicating mitotic regulation; cytoplasmic membrane receptor-trafficking machinery; nucleus (JUNB/p21 transcriptional program).
- **Localization/lateralization:** Systemic (bone marrow throughout the skeleton); not lateralized. *Not applicable* for unilateral/bilateral descriptors.

---

## 8. Temporal Development

- **Onset:** Congenital/lifelong thrombocytopenia (present from birth, often detected incidentally in childhood or adulthood). Onset is **insidious/chronic**, not acute.
- **Progression of the thrombocytopenia:** Generally **stable** and non-progressive over life; the platelet count does not typically deteriorate from the primary lesion alone.
- **Critical transition:** The clinically decisive event is **malignant transformation** to MDS/AML/CMML, which can occur at variable ages in adulthood and reflects acquisition of somatic driver mutations.
- **Diagnostic latency:** Genetic diagnosis is typically **delayed ~20 years** from first detection of thrombocytopenia [PMID: 40670159](https://pubmed.ncbi.nlm.nih.gov/40670159/).
- **Duration:** Chronic, lifelong. No spontaneous remission of the thrombocytopenia.

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal dominant** (germline). Offspring of an affected parent have a 50% transmission risk.
- **Penetrance:** High penetrance for the thrombocytopenia; **incomplete and variable penetrance** for the malignancy phenotype.
- **Expressivity:** Variable (bleeding, blood-count abnormalities, malignancy risk differ among carriers).
- **Prevalence/frequency:** THC2 is rare at the population level but **relatively frequent among inherited thrombocytopenias** — it accounted for 21/210 (~10%) families in the Italian inherited-thrombocytopenia database: "Because THC2 affected 21 of the 210 families in our database, it has to be considered one of the less rare forms of inherited thrombocytopenia" [PMID: 21467542](https://pubmed.ncbi.nlm.nih.gov/21467542/). It is systematically **under-diagnosed** because inherited thrombocytopenias are frequently missed — "we suspect that inherited thrombocytopenias are underreported because their diagnosis is often missed" [PMID: 12745278](https://pubmed.ncbi.nlm.nih.gov/12745278/).
- **Anticipation / mosaicism / founder effects / consanguinity:** No genetic anticipation (not a repeat-expansion disorder). As a dominant disorder, consanguinity is not a driver. No established founder effect, though recurrent hotspot mutations arise independently. *Specific carrier-frequency and founder data: not available.*
- **Sex ratio / ethnicity / geography:** No strong sex bias reported; described across European (Italian) and Japanese registries, consistent with broad geographic distribution. Precise sex ratios and population-specific prevalence are *not available*.

---

## 10. Diagnostics

**Clinical/laboratory workup.**
- **CBC with platelet indices:** Mild-to-moderate thrombocytopenia with **normal mean platelet volume (MPV)** — the key discriminator. Platelet size/volume is the primary branch point in inherited-thrombocytopenia diagnostic algorithms: "The different forms have been classified into 3 groups depending on platelet volume … it is one of the most useful [criteria] in diagnostic algorithms" [PMID: 12161364](https://pubmed.ncbi.nlm.nih.gov/12161364/). ANKRD26-RT falls in the **normal-sized-platelet group** [PMID: 36591709](https://pubmed.ncbi.nlm.nih.gov/36591709/).
- **Peripheral blood smear:** Normal-sized platelets; useful to exclude macrothrombocytopenias.
- **Platelet function testing:** Historically normal aggregation; more recent data show frequently impaired aggregation and heterogeneous granule secretion; frequent GPIa (ITGA2) and α-granule deficiency [PMID: 21467542, 40670159].
- **Serum thrombopoietin:** Often elevated, consistent with a production (dysmegakaryopoietic) defect [PMID: 21467542].
- **Bone marrow:** Dysmegakaryopoiesis; single-cell studies show MkP expansion and polyploid-MK reduction [PMID: 41538704].

**Genetic testing (definitive).** Diagnosis rests on **targeted sequencing of the *ANKRD26* 5′UTR**, performed either as single-gene testing or within NGS **inherited-platelet-disorder / MDS-AML-predisposition panels** that also cover *RUNX1* and *ETV6*. WES/WGS can detect the variant but the non-coding 5′UTR hotspot must be specifically covered and interpreted. Karyotyping/CMA/FISH are reserved for assessing clonal evolution, not for primary diagnosis.

**Clinical criteria & differential diagnosis.** Key differentials are the other **normal-platelet-size inherited thrombocytopenias with malignancy risk — RUNX1-RT and ETV6-RT** — and, critically, **acquired immune thrombocytopenia (ITP)**, which is the most common and most consequential misdiagnosis (leading to inappropriate immunosuppression or splenectomy).

**Screening.** No newborn screening. **Cascade genetic testing** of at-risk relatives is recommended once the familial 5′UTR variant is identified.

---

## 11. Outcome / Prognosis

- **Thrombocytopenia prognosis:** Generally benign; bleeding is usually mild and life expectancy from the platelet disorder alone is normal.
- **Dominant prognostic driver — malignancy:** Inherited thrombocytopenia with germline *RUNX1*, *ETV6* or *ANKRD26* variants "carries a high risk (10%-45%) of developing haematological malignancy (IT-HM)" [PMID: 40670159](https://pubmed.ncbi.nlm.nih.gov/40670159/). Reported ANKRD26-associated neoplasms include **AML, MDS, and CMML** [PMID: 35751752](https://pubmed.ncbi.nlm.nih.gov/35751752/); in the 2025 cohort, ANKRD26-RT cases included B-ALL (Ph+), MDS and breast cancer, with one-third of the combined IT cohort developing malignancy [PMID: 40670159].
- **Transformation mechanism:** "Acute myeloid leukemia, myelodysplastic syndrome, and chronic myelomonocytic leukemia have been reported to occur in the context of germline variants in ANKRD26, with the development of somatic driver mutations in hematopoietic regulators playing an important role in malignant transformation" (two-hit model) [PMID: 35751752].
- **Prognostic factors:** Development of cytopenias beyond baseline, new dysplasia, or clonal cytogenetic/molecular abnormalities signal progression and warrant urgent evaluation.
- **QoL/disability:** Low from the thrombocytopenia; substantial if malignancy develops.

---

## 12. Treatment

**General principle:** No disease-modifying therapy exists. Management is **supportive**, and most patients with mild bleeding require **no chronic treatment**.

**Pharmacotherapy / TPO-receptor agonists.** The TPO-RA **eltrombopag** (NCIT:C62492) effectively raises platelet counts perioperatively. In a case series of inherited thrombocytopenias that included ANKRD26-RT, eltrombopag at 50 mg/day started ~3 weeks before surgery produced a favorable platelet response in **14 of 15 procedures**, preventing bleeding complications and offering an alternative to platelet transfusion: "Nine patients with confirmed ITs (MYH9-related disease, ANKRD26-related thrombocytopenia [-RT], ITGA2B/ITGB3-RT, ACTN1-RT) underwent 15 surgical procedures. Eltrombopag was administered at 50 mg/d, initiated approximately 3 weeks prior to surgery" and "A favorable platelet response occurred in 14 of 15 procedures" [PMID: 42620598](https://pubmed.ncbi.nlm.nih.gov/42620598/).

**Supportive/interventional.**
- Perioperative platelet support (platelet transfusion or TPO-RA) for surgery/trauma.
- **Avoid unnecessary antiplatelet drugs** and avoid splenectomy / immunosuppression driven by ITP misdiagnosis.
- Antifibrinolytics (e.g., tranexamic acid) for mucosal bleeding where appropriate (general IT practice).

**Advanced therapeutics.** **Allogeneic hematopoietic stem cell transplantation (HSCT; NCIT:C15431)** is reserved for progression to MDS/AML. Germline status critically informs **donor selection — related donors must be screened to avoid using a donor carrying the familial *ANKRD26* variant**: the role of HSCT "in managing MDS, particularly in patients with germline syndromes, is reviewed, emphasizing the need for optimal donor selection and personalized treatment approaches" [PMID: 39443230](https://pubmed.ncbi.nlm.nih.gov/39443230/). No approved gene, RNA, or targeted therapy exists for THC2 itself; ERK-pathway inhibition rescues the proplatelet defect in vitro and is a mechanistic lead, not a clinical therapy [PMID: 24430186].

**Pharmacogenomics / personalized medicine:** Treatment is genotype-aware chiefly through germline-status-guided surveillance and transplant donor selection rather than drug-metabolism pharmacogenomics.

---

## 13. Prevention

- **Primary prevention:** **None** — THC2 is a germline autosomal-dominant condition; the disease cannot be prevented in a mutation carrier.
- **Secondary prevention:** **Periodic CBC and bone-marrow surveillance** for early detection of clonal evolution/MDS-AML; early recognition of dysplasia enables timely intervention.
- **Tertiary prevention:** Avoid unnecessary antiplatelet drugs, immunosuppression, and splenectomy from ITP misdiagnosis; provide perioperative platelet support; treat malignant transformation promptly.
- **Genetic counseling:** Central to management — 50% offspring transmission risk, cascade testing of relatives, and **informed donor selection for HSCT**. *ANKRD26* is confirmed as a germline MDS-predisposition gene: "hereditary conditions that affect platelet production and count, such as RUNX1, ETV6, and ANKRD26 … contribute to an increased risk of MDS" [PMID: 39443230](https://pubmed.ncbi.nlm.nih.gov/39443230/).
- **Reproductive options:** Preimplantation genetic testing (PGT) and prenatal diagnosis are available once the familial 5′UTR variant is known.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *ANKRD26* is conserved in mouse (*Ankrd26*; NCBI Taxon:10090). *ANKRD26* is the ancestor of the primate-specific *POTE* gene family [PMID: 21211618].
- **Natural disease in other species:** No naturally occurring animal homolog of THC2 (gain-of-expression thrombocytopenia) has been described. *Not applicable* for companion-animal/wildlife natural disease.
- **Comparative biology:** Importantly, the mouse *Ankrd26* **knockout models loss of function, not THC2.** *Ankrd26*−/− mice develop hyperphagia, obesity and gigantism via a **ciliopathy** of hypothalamic appetite/energy-homeostasis centers — and do **not** develop thrombocytopenia: "disruption of this gene causes hyperphagia, obesity and gigantism in mice. In the present study, we looked for the mechanisms that induce hyperphagia in the Ankrd26-/- mice and found defects in primary cilia in regions of the central nervous system that control appetite and energy homeostasis" [PMID: 24633808](https://pubmed.ncbi.nlm.nih.gov/24633808/). This divergence is itself evidence that THC2 is a gain-of-expression disease, not haploinsufficiency.
- **Zoonotic potential:** None (non-transmissible genetic disorder).

---

## 15. Model Organisms

| Model | Type | What it captures | Limitation |
|---|---|---|---|
| *Ankrd26*−/− mouse | Mammalian knockout (loss of function) | ANKRD26 LoF biology (ciliopathy, obesity) | **Does NOT recapitulate THC2**; no thrombocytopenia [PMID: 24633808] |
| Patient primary megakaryocytes | Human ex vivo | RUNX1/FLI1-binding loss, MPL/ERK hyperactivation, proplatelet defect, ERK-rescue | Limited cell numbers; culture artifacts [PMID: 24430186] |
| Patient bone marrow single-cell (scRNA-seq) | Human ex vivo | MkP expansion, polyploid-MK apoptosis, JUNB-p21 mechanism | Observational; 4 patients [PMID: 41538704] |
| Patient-derived iPSC line (e.g., CGOi001-A) | Human in vitro | ANKRD26-mutant hematopoietic differentiation | Differentiation efficiency; emerging resource (PMID 41643484) |
| Cytokine-receptor overexpression cell lines | In vitro | MPL/EPOR/G-CSFR trafficking/signaling | Reductionist [PMID: 36794499] |

**Key point:** Because THC2 is caused by a **gain of expression**, the standard mouse knockout models the wrong allele direction. The faithful disease-relevant systems are **human patient-derived** (primary MKs, iPSC-derived hematopoietic cells, single-cell bone marrow profiling). No fully faithful animal model of the gain-of-expression thrombocytopenia currently exists — a notable knowledge gap.

---

## Mechanistic Model / Interpretation

The pathophysiology of THC2 is now coherent and converges from two independent experimental programs onto a unified model. The **initiating lesion is regulatory, not coding**: 5′UTR mutations in a conserved 19-bp window strip away RUNX1/FLI1 repression, so *ANKRD26* — normally switched off as megakaryocytes mature — stays on. The downstream consequences bifurcate but reinforce the same endpoint:

- A **signaling branch** (Bluteau et al.; Basso-Valentina et al.) in which excess ANKRD26 protein stabilizes MPL/EPOR/G-CSFR, raises TPO/MPL signaling, and hyperactivates MAPK/ERK, blocking proplatelet formation — causally proven because ERK inhibition fully rescues proplatelet formation.
- An **apoptotic branch** (Chen et al., single-cell) in which centrosome-localized ANKRD26 drives JUNB→p21 transcription to kill polyploid megakaryocytes, depleting the mature cells that make platelets while progenitors (MkP) accumulate.

Both branches yield **dysmegakaryopoiesis** → fewer platelets of normal size → the characteristic normocytic, mild-to-moderate thrombocytopenia with compensatory high TPO. Layered on top, a **leukemogenic trajectory** emerges over decades as somatic driver mutations accrue on the germline background, explaining the 10–45% malignancy predisposition that dominates prognosis. The *GATA2*-positive / *RUNX1-FLI1*-negative regulatory tug-of-war over *ANKRD26* ties the predisposition genes into a single regulatory circuit.

Clinically, the single most actionable insight is **diagnostic discrimination**: normal platelet size + autosomal-dominant family history should trigger targeted *ANKRD26* 5′UTR sequencing and divert the patient away from an ITP label, averting harmful immunosuppression/splenectomy and enrolling them in lifelong malignancy surveillance.

---

## Evidence Base

| PMID | Role | Key contribution |
|---|---|---|
| [21211618](https://pubmed.ncbi.nlm.nih.gov/21211618/) | Landmark (genetics) | Identifies *ANKRD26* 5′UTR 19-bp hotspot; gain-of-expression, not haploinsufficiency |
| [24430186](https://pubmed.ncbi.nlm.nih.gov/24430186/) | Landmark (mechanism) | RUNX1/FLI1-binding loss → MPL/MAPK-ERK hyperactivation → proplatelet defect; ERK-inhibition rescue |
| [36794499](https://pubmed.ncbi.nlm.nih.gov/36794499/) | Mechanism | ANKRD26 modulates MPL/EPOR/G-CSFR internalization → cytokine hypersensitivity |
| [41538704](https://pubmed.ncbi.nlm.nih.gov/41538704/) / [42911644](https://pubmed.ncbi.nlm.nih.gov/42911644/) | Recent landmark | Single-cell: MkP expansion, polyploid-MK apoptosis via centrosomal ANKRD26 + JUNB-p21 |
| [21467542](https://pubmed.ncbi.nlm.nih.gov/21467542/) | Landmark (clinical) | 78 patients/21 families: normocytic platelets, mild bleeding, GPIa/α-granule deficiency, leukemia risk; ~10% of IT families |
| [40670159](https://pubmed.ncbi.nlm.nih.gov/40670159/) | Recent cohort | 10–45% malignancy risk; bleeding in 25–30%; impaired aggregation in 90%; ~20-yr diagnostic delay |
| [35751752](https://pubmed.ncbi.nlm.nih.gov/35751752/) | Review | AML/MDS/CMML spectrum; somatic-driver two-hit transformation |
| [40954090](https://pubmed.ncbi.nlm.nih.gov/40954090/) | Registry | Japanese registry: novel variant disrupts RUNX1 site → overexpression, reduced proplatelets, lower ploidy |
| [38817334](https://pubmed.ncbi.nlm.nih.gov/38817334/) | Mechanism/modifier | GATA2 as positive regulator of *ANKRD26*; confirms core THC2 definition |
| [24633808](https://pubmed.ncbi.nlm.nih.gov/24633808/) | Model organism | *Ankrd26* KO = ciliopathy/obesity, NOT thrombocytopenia (supports non-haploinsufficiency) |
| [42620598](https://pubmed.ncbi.nlm.nih.gov/42620598/) | Treatment | Eltrombopag effective perioperatively (14/15 procedures) incl. ANKRD26-RT |
| [39443230](https://pubmed.ncbi.nlm.nih.gov/39443230/) | Management | Germline-informed donor selection/counseling for HSCT in MDS predisposition |
| [12161364](https://pubmed.ncbi.nlm.nih.gov/12161364/) / [12745278](https://pubmed.ncbi.nlm.nih.gov/12745278/) / [36591709](https://pubmed.ncbi.nlm.nih.gov/36591709/) | Diagnostics | Platelet-size classification; under-diagnosis of inherited thrombocytopenia |

Evidence sources span **human clinical cohorts/registries** (21467542, 40670159, 40954090), **human ex vivo/in vitro functional studies** (24430186, 36794499, 41538704), and **model organism** work (24633808). No contradictions exist in the mechanistic model; the main evolution is the refinement of "normal platelet aggregation" (2011) toward "frequently impaired/heterogeneous function" (2025).

---

## Limitations and Knowledge Gaps

1. **No faithful animal model** of the gain-of-expression disease; the mouse knockout models the opposite allele direction.
2. **Malignancy risk is a group estimate** (10–45% across RUNX1/ETV6/ANKRD26) rather than a precise *ANKRD26*-specific, age-stratified figure; penetrance determinants are incompletely defined.
3. **Variant interpretation** for novel non-canonical 5′UTR variants and coding VUS remains challenging; functional assays (reporter/transcript quantitation) are not universally standardized.
4. **Epidemiology** — precise prevalence/incidence, sex ratio, and ethnicity-specific data are not well quantified; the disorder is under-diagnosed.
5. **No QoL instruments** validated specifically for THC2.
6. **Surveillance protocols** (frequency/modality of CBC and marrow monitoring) are not standardized by prospective evidence; preventive/leukemia-interception therapies are aspirational.

---

## Proposed Follow-up Experiments / Actions

1. **Build a conditional gain-of-expression model** (megakaryocyte-specific *Ankrd26* overexpression or 5′UTR knock-in of a RUNX1-site-disrupting mutation) to recapitulate normocytic thrombocytopenia and test leukemia predisposition in vivo.
2. **iPSC-based mechanistic dissection** using patient lines (e.g., CGOi001-A) to validate the JUNB-p21 apoptotic branch and screen ERK-pathway or JUNB/p21 modulators as proplatelet-restoring agents.
3. **Prospective natural-history registry** to derive *ANKRD26*-specific, age-stratified malignancy penetrance and define evidence-based surveillance intervals.
4. **Standardized diagnostic pathway**: embed MPV + autosomal-dominant history as a trigger for *ANKRD26* 5′UTR sequencing in thrombocytopenia panels to reduce ITP misdiagnosis and the ~20-year diagnostic delay.
5. **Functional classification pipeline** (luciferase reporter + transcript quantitation + RUNX1/FLI1 ChIP) to resolve non-canonical 5′UTR VUS for ACMG/AMP classification.
6. **Clonal-surveillance biomarkers**: longitudinal somatic-mutation tracking (serial NGS/liquid biopsy of hematopoietic clones) to detect pre-leukemic evolution and enable early intervention.

---

*Report compiled from a 5-iteration autonomous investigation; 10 confirmed findings, 29 papers reviewed. Evidence types: human clinical cohort/registry, human ex vivo/in vitro functional, and model organism.*


## Artifacts

- [OpenScientist final report](ANKRD26-Related_Thrombocytopenia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ANKRD26-Related_Thrombocytopenia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 15 |
| Quoted claims found in source | 12 |
| Quoted claims **not** found in source | 3 |
| References weighed for topical relevance | 17 |
| On topic | 12 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:12745278` *(abstract only)*: "we suspect that inherited thrombocytopenias are underreported because their diagnosis is often missed"
  - closest text in source: "We, therefore, suspect that inherited thrombocytopenias are underreported because their diagnosis is often missed"
- `PMID:12161364` *(abstract only)*: "The different forms have been classified into 3 groups depending on platelet volume … it is one of the most useful [criteria] in diagnostic algorithms"
  - closest text in source: "The different forms have been classified into 3 groups depending on platelet volume"
- `PMID:39443230` *(abstract only)*: "hereditary conditions that affect platelet production and count, such as RUNX1, ETV6, and ANKRD26 … contribute to an increased risk of MDS"
  - closest text in source: "It delves into hereditary conditions that affect platelet production and count, such as RUNX1, ETV6, and ANKRD26, detailing their clinical features and how they contribute to an increased risk of MDS"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 19 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008555` (2 mentions) - the report calls it "MONDO"; MONDO calls it **thrombocytopenia 2**
- `HP:0001873` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Thrombocytopenia**
- `HP:0030401` (1 mention) - the report calls it "Lab/morphology"; HP calls it **Abnormal platelet dense granule ATP/ADP ratio**
- `NCIT:C62492` (1 mention) - the report calls it "eltrombopag"; NCIT calls it **Denenicokin**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0011869` (1 mention) - the report calls it "platelet dysfunction"; HP calls it **Abnormal platelet function**
- `HP:0012757` (1 mention) - the report calls it "Lab/pathology"; HP calls it **Abnormal neuron morphology**
- `UBERON:0002371` (1 mention) - the report calls it "Primary organ/tissue:** Bone marrow"; UBERON calls it **bone marrow**
- `GO:0005813` (1 mention) - the report calls it "Centrosome", "Subcellular level:** **Centrosome"; GO calls it **centrosome**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005813` - called "Centrosome", "Subcellular level:** **Centrosome"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `Taxon`.