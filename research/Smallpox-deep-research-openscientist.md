---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T23:38:07.569575'
end_time: '2026-10-30T23:53:21.052240'
duration_seconds: 913.48
template_file: templates/disease_pathophysiology_research.md
template_sha: f452f0a9c7e3536175154b9683c45663f686f283
template_variables:
  disease_name: Smallpox
  mondo_id: MONDO:0004651
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: Variola virus caused disease or disorder; Variola virus disease or disorder;
    Variola virus infectious disease; ordinary smallpox
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
citation_count: 32
reference_validation:
  total_references: 32
  verified: 32
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 3
  relevance_assessed: 32
  on_topic: 23
  validator_version: 0.4.0
term_validation:
  total_terms: 30
  verified: 30
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 9
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0004651
    reported_labels:
    - if available
    - MONDO
    ontology_label: smallpox
  - term_id: HP:0000987
    reported_labels:
    - Permanent, disfiguring; healed survivors
    ontology_label: Atypical scarring of skin
  - term_id: NCIT:C171621
    reported_labels:
    - Tecovirimat
    ontology_label: Impact of Events Scale
  - term_id: NCIT:C97660
    reported_labels:
    - Brincidofovir
    ontology_label: Abemaciclib
  labels_variant: 7
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Smallpox-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Smallpox-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Smallpox
- **MONDO ID:** MONDO:0004651 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** Variola virus caused disease or disorder; Variola virus disease or disorder; Variola virus infectious disease; ordinary smallpox
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Smallpox** covering all of the
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

# Smallpox (Variola virus disease) — Comprehensive Disease Characterization Report

**Disease:** Smallpox
**MONDO ID:** MONDO:0004651
**Category:** Infectious Disease
**Causal agent:** *Variola virus* (VARV), an *Orthopoxvirus* (NCBI Taxon 10255) — **no human causal gene**

---

## Summary

**Smallpox is not a genetic disease.** Despite the "causal gene" field of the research template, smallpox (MONDO:0004651) is an acute, systemic, human-restricted **infectious disease caused by the Variola virus (VARV)**, a large (~186 kb) double-stranded DNA virus of the genus *Orthopoxvirus* (family *Poxviridae*). VARV encodes ~200 proteins and replicates entirely in the host-cell cytoplasm; more than 80 of its proteins — concentrated in the terminal regions of the genome — carry out host immune-evasion functions rather than classic housekeeping roles [PMID: 12941397](https://pubmed.ncbi.nlm.nih.gov/12941397/). The disease was the first (and to date only human disease) to be deliberately eradicated: the last endemic natural case occurred in Somalia in 1977, and the World Health Organization certified global eradication in 1980 [PMID: 42135325](https://pubmed.ncbi.nlm.nih.gov/42135325/). Because VARV stocks are retained and routine vaccination ceased decades ago, leaving populations immunologically naïve, smallpox remains a Category A biodefense concern [PMID: 42576544](https://pubmed.ncbi.nlm.nih.gov/42576544/).

Pathogenesis proceeds from respiratory-mucosal entry, through a **monocyte-associated cell-associated viremia** that disseminates virus to lymphoid tissues, skin, oral mucosa, gastrointestinal tract, reproductive organs and liver, to a characteristic **synchronous, deep-seated, centrifugal vesiculopustular rash** [PMID: 15477589](https://pubmed.ncbi.nlm.nih.gov/15477589/). Severe (flat and hemorrhagic) forms involve cytokine-driven coagulopathy and multi-organ failure. Clinical outcome tracks disease type: discrete ordinary smallpox ~10% case-fatality, confluent ~50–75%, and flat/hemorrhagic forms >95%, with variola major averaging ~30% in the unvaccinated and variola minor (alastrim) <1% [PMID: 42135325](https://pubmed.ncbi.nlm.nih.gov/42135325/), [PMID: 42576544](https://pubmed.ncbi.nlm.nih.gov/42576544/).

Smallpox was eradicated through **ring vaccination and isolation** using live vaccinia-based vaccines; post-exposure vaccination within ~3–4 days can prevent or attenuate disease. Modern countermeasures comprise the vaccinia-based vaccines **ACAM2000** (replication-competent) and **MVA-BN/JYNNEOS** (non-replicating), plus two FDA Animal-Rule antivirals: **tecovirimat** (TPOXX; inhibits the VP37/p37 envelope protein required for extracellular virion egress) and **brincidofovir** (Tembexa; a lipid-conjugated oral prodrug of the DNA-polymerase inhibitor cidofovir) [PMID: 41740032](https://pubmed.ncbi.nlm.nih.gov/41740032/), [PMID: 36688308](https://pubmed.ncbi.nlm.nih.gov/36688308/).

---

## 1. Disease Information

Smallpox is an acute contagious systemic viral illness caused by the Variola virus. Humans are the **only natural host** — there is no animal reservoir, a feature that made global eradication feasible.

**Key identifiers:**

| Resource | Identifier |
|----------|-----------|
| MONDO | MONDO:0004651 |
| ICD-10 | B03 |
| ICD-11 | 1E70 |
| MeSH | D012899 (Smallpox) |
| NCBI Taxonomy (agent) | Variola virus, Taxon 10255 |
| OMIM | Not applicable (not a Mendelian genetic disorder) |
| Orphanet | Not a rare genetic disease; historical infectious disease |

**Synonyms:** Variola; variola vera; variola major; variola minor (alastrim); Variola virus infectious disease; ordinary smallpox.

**Information source type:** Disease-level aggregated resources (WHO eradication records, historical clinical series, and modern animal-model and vaccinology studies), **not** individual-patient EHR data — no new natural cases have occurred since 1977. The *ICD2Vec* framework notably identified smallpox (ICD-10 B03) among diseases semantically similar to COVID-19 [PMID: 37054960](https://pubmed.ncbi.nlm.nih.gov/37054960/).

---

## 2. Etiology

**Primary cause — infectious:** Variola virus, an *Orthopoxvirus* closely related to vaccinia, cowpox and monkeypox (mpox) viruses. VARV is a large dsDNA virus (~186 kb, ~200 genes) that replicates in the cytoplasm within viral "factories." There is **no genetic, toxic, or metabolic etiology** — smallpox is entirely virus-driven [PMID: 12941397](https://pubmed.ncbi.nlm.nih.gov/12941397/).

**Risk factors (environmental/behavioral):**
- Close contact with an infected person (respiratory droplets, direct contact with lesions or contaminated fomites such as bedding).
- Lack of prior vaccination (populations born after ~1980 are largely immunologically naïve) [PMID: 42576544](https://pubmed.ncbi.nlm.nih.gov/42576544/).
- Crowding, household exposure, and healthcare settings pre-eradication.
- Pregnancy and immunocompromise historically predisposed to more severe (including hemorrhagic) disease.

**Genetic risk factors:** No validated human host-susceptibility loci are established for VARV, reflecting the absence of modern population studies (eradicated before genomic epidemiology). Host genetic variation in innate/adaptive immune genes is plausible but not characterized.

**Protective factors:** Prior smallpox vaccination (vaccinia immunity) is strongly protective and conferred durable, decades-long protection (see Finding F007). Historical smallpox vaccination still provides ~70% residual cross-protection against the related mpox virus decades later [PMID: 39176988](https://pubmed.ncbi.nlm.nih.gov/39176988/).

**Gene–environment interactions:** Not characterized for smallpox. The dominant determinant of outcome was vaccination status and clinical form, not host genotype.

---

## 3. Phenotypes

Smallpox follows a stereotyped clinical course after a **7–19 day incubation** (typically 10–14 days). Key phenotypes:

| Phenotype | Type | Characteristics | Suggested HPO term |
|-----------|------|-----------------|--------------------|
| Febrile prodrome (high fever, malaise, headache, backache) | Symptom | Acute onset, precedes rash by 2–4 days; severe | HP:0001945 (Fever) |
| Enanthem (oral/pharyngeal mucosal lesions) | Clinical sign | Appears with/just before skin rash; infectious | HP:0000164 (Oral mucosa abnormality) |
| Synchronous vesiculopustular rash | Physical manifestation | Deep-seated, firm, "pearl-like" pustules all at the **same stage**; centrifugal (face/extremities > trunk) | HP:0200041 (Vesicle); HP:0000987 (Atypical scarring of skin) |
| Lesions on palms and soles | Physical manifestation | Characteristic, distinguishes from varicella | — |
| Umbilicated pustules | Physical manifestation | Central depression | HP:0200039 (Papule) |
| Pitted/pock scarring | Physical manifestation (sequela) | Permanent, disfiguring; healed survivors | HP:0000987 |
| Hemorrhagic diathesis (flat/hemorrhagic forms) | Laboratory/clinical | Thrombocytopenia, D-dimer elevation, mucosal bleeding | HP:0001892 (Abnormal bleeding); HP:0001873 (Thrombocytopenia) |
| Leukocytosis | Laboratory abnormality | Profound in lethal disease (macaque model) | HP:0001974 (Leukocytosis) |

The **synchronous progression** (all lesions evolving together: macule → papule → vesicle → pustule → crust) and the **centrifugal distribution** are the classic phenotypic signatures distinguishing smallpox from chickenpox (varicella), in which lesions appear in crops at different stages.

**WHO (Rao) clinical types and frequency among affected individuals:**
- Ordinary (~90%)
- Modified (in partially immune/vaccinated)
- Flat/malignant (rare, >95% fatal)
- Hemorrhagic (rare, >95% fatal)
- Variola minor (alastrim; <1% fatal)

**Quality-of-life impact:** Acute disease was debilitating and often fatal; survivors suffered permanent pockmark scarring, blindness from corneal involvement, and limb deformities. Standardized QoL instruments (EQ-5D/SF-36) were not applied historically.

---

## 4. Genetic / Molecular Information

**This is not a host-genetic disease.** The relevant "genetics" are those of the **viral genome**:

- **Genome:** ~186 kb linear dsDNA with covalently closed hairpin termini and inverted terminal repeats; ~200 open reading frames; cytoplasmic replication [PMID: 12941397](https://pubmed.ncbi.nlm.nih.gov/12941397/).
- **Immune-evasion gene complement:** >80 proteins in the terminal genome regions encode host-interaction/immune-evasion functions. Orthopoxviruses carry the **largest antidefense-gene complement of any animal virus family**, shaped by ancient gene capture and recent gene loss [PMID: 34253028](https://pubmed.ncbi.nlm.nih.gov/34253028/).
- **Phylogeny (viral strain variation):** Analysis of ~48 VARV genomes resolves **two clades** — Clade 1 (variola major variants) and Clade 2 (West African and variola minor/alastrim strains) — mapping onto the virulence divide [PMID: 28749451](https://pubmed.ncbi.nlm.nih.gov/28749451/). Ancient genomes (a ~400-year-old Lithuanian mummy; 60-/160-year-old Prague museum specimens) fall basal or represent extinct European lineages, confirming deep evolutionary history [PMID: 28749451](https://pubmed.ncbi.nlm.nih.gov/28749451/), [PMID: 33022266](https://pubmed.ncbi.nlm.nih.gov/33022266/).

**Human host genes:** No causal human gene, HGNC entry, ClinVar variant, gnomAD allele frequency, or chromosomal abnormality applies. Sections on pathogenic variants, modifier genes, epigenetics, and chromosomal abnormalities are **not applicable** to this infectious disease.

---

## 5. Environmental Information

**Infectious agent:** Variola virus (NCBI Taxon 10255), genus *Orthopoxvirus*, family *Poxviridae*. Transmitted human-to-human via respiratory droplets/aerosols, direct contact with lesion material, and contaminated fomites (bedding, clothing). Patients are most infectious from rash onset through the first 7–10 days of rash [PMID: 21431786](https://pubmed.ncbi.nlm.nih.gov/21431786/).

**Environmental/lifestyle factors:** No toxins, radiation, diet, or occupational chemical exposures cause smallpox. Crowding and inadequate isolation facilitated spread historically. The disease has no environmental reservoir — eradication was possible precisely because VARV cannot persist outside humans.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating infection → clinical manifestation)

1. **Inhalation of VARV-laden droplets/aerosol** deposits virus on the oropharyngeal/respiratory mucosa, which **leads to** infection of mucosal epithelial cells and local macrophages (demonstrated in the aerosol monkeypox macaque surrogate: early lung replication) [PMID: 25653439](https://pubmed.ncbi.nlm.nih.gov/25653439/).
2. **Viral entry** into host cells via a multi-protein, glycosaminoglycan (GAG)-dependent attachment system — ~4 mature-virion membrane proteins bind heparan/chondroitin sulfate or laminin — followed by an 11–12-protein entry-fusion complex that fuses at the plasma membrane or in acidified endosomes after macropinocytosis; this **results in** cytoplasmic release of the viral core [PMID: 22754644](https://pubmed.ncbi.nlm.nih.gov/22754644/), [PMID: 38321165](https://pubmed.ncbi.nlm.nih.gov/38321165/).
3. **Infected migratory monocytes/macrophages** carry virus to draining lymph nodes, establishing a **monocyte-associated cell-associated viremia** that **leads to** systemic dissemination (primary viremia) [PMID: 15477589](https://pubmed.ncbi.nlm.nih.gov/15477589/).
4. **Viral immune-evasion proteins** (>80 encoded) **suppress** host defense: the secreted complement regulator **SPICE** (smallpox inhibitor of complement enzymes) anchors to cells via heparan/chondroitin-sulfate GAGs and inhibits complement at the **C3 convertase** step via combined decay-acceleration and factor-I cofactor activity, with human-pathway selectivity — molecularly mirroring VARV's human host-restriction; chemokine- and cytokine-binding proteins further blunt innate immunity [PMID: 18768877](https://pubmed.ncbi.nlm.nih.gov/18768877/), [PMID: 19667083](https://pubmed.ncbi.nlm.nih.gov/19667083/), [PMID: 28724763](https://pubmed.ncbi.nlm.nih.gov/28724763/).
5. **Secondary viremia** seeds the skin, oral mucosa, GI tract, reproductive organs, and liver, where viral replication in dermal/epithelial cells **produces** the enanthem and the deep-seated vesiculopustular exanthem [PMID: 15477589](https://pubmed.ncbi.nlm.nih.gov/15477589/).
6. **In severe disease**, massive viral replication and a dysregulated cytokine response (elevated IL-1ra, IL-6, IFN-γ in the aerosol model) **drive** coagulation activation (thrombocytopenia, D-dimer elevation), depletion of T-cell-dependent lymphoid areas, and **multi-organ hemorrhagic diathesis** — the lethal flat/hemorrhagic phenotype [PMID: 15477589](https://pubmed.ncbi.nlm.nih.gov/15477589/), [PMID: 25653439](https://pubmed.ncbi.nlm.nih.gov/25653439/).

### Branch point

```
                    VARV respiratory entry
                            │
                 monocyte-associated viremia
                            │
            ┌───────────────┴───────────────┐
   Controlled replication            Uncontrolled replication +
   + adaptive immunity                cytokine storm + coagulopathy
            │                                 │
   Ordinary/discrete rash            Flat / hemorrhagic smallpox
   (CFR ~10-30%)                      (CFR >95%)
```

### Mechanistic detail by category

- **Molecular pathways:** GAG-mediated attachment (heparan sulfate CHEBI:28815; chondroitin sulfate); complement cascade inhibition at C3/C5 convertase; interferon and chemokine signaling suppression.
- **Protein dysfunction (viral, not host):** The chondroitin-sulfate-binding protein **D8** bends the host membrane to drive fusion-pore formation [PMID: 38321165](https://pubmed.ncbi.nlm.nih.gov/38321165/). SPICE achieves complement inhibition equal to or greater than host regulators [PMID: 18768877](https://pubmed.ncbi.nlm.nih.gov/18768877/).
- **Immune system involvement:** Complement evasion (SPICE), impaired NK function, lymphopenia, and cytokine storm are central; the host response is both protective and, when dysregulated, pathogenic.
- **Tissue-damage mechanisms:** Direct cytopathic viral replication in epithelium plus immune-mediated injury; hemorrhagic forms involve coagulopathy and endothelial compromise.

**Suggested GO terms:** GO:0019062 (virion attachment to host cell), GO:0046718 (viral entry into host cell), GO:0052170 (symbiont-mediated suppression of host innate immune response), GO:0030449 (regulation of complement activation), GO:0001816 (cytokine production).
**Suggested CL terms:** CL:0000576 (monocyte), CL:0000235 (macrophage), CL:0000312 (keratinocyte), CL:0000084 (T cell).

---

## 7. Anatomical Structures Affected

**Organ/system level:**
- **Primary:** Skin (UBERON:0002097) and mucous membranes — oral/pharyngeal mucosa (UBERON:0000344), respiratory tract (UBERON:0000065, entry site).
- **Lymphoreticular system:** lymph nodes (UBERON:0000029), spleen (UBERON:0002106), tonsil (UBERON:0002372) — sites of viral amplification [PMID: 15477589](https://pubmed.ncbi.nlm.nih.gov/15477589/), [PMID: 25653439](https://pubmed.ncbi.nlm.nih.gov/25653439/).
- **Secondary:** Gastrointestinal tract (UBERON:0000160), liver (UBERON:0002107), reproductive organs, eyes (corneal scarring → blindness), and in severe disease, systemic involvement with coagulopathy.
- **Body systems:** integumentary, respiratory, lymphatic/immune, hematologic, hepatic.

**Tissue/cell level:** Epithelial tissue (epidermis, mucosal epithelium); dermal fibroblasts; monocytes/macrophages (vehicle of dissemination; CL:0000576/CL:0000235); depletion of T-cell-dependent lymphoid zones.

**Subcellular level:** Viral replication occurs in **cytoplasmic viral factories** (GO:0030430, host cytoplasm) — distinctively, poxviruses do **not** require the nucleus for replication. Virion assembly and envelopment traverse the ER/Golgi and plasma-membrane compartments.

**Localization/lateralization:** Rash is **bilateral and symmetric**, centrifugal (denser on face, forearms, hands, feet, including palms and soles).

---

## 8. Temporal Development

- **Onset:** Acute. Incubation 7–19 days (commonly 10–14), followed by abrupt febrile prodrome lasting 2–4 days, then rash.
- **Stages:** (1) Incubation (asymptomatic); (2) prodrome (fever, prostration); (3) early rash/enanthem (most infectious); (4) pustular rash; (5) scabbing/resolution or death. The aerosol macaque model documented temperature peak at day 6 with concurrent skin pox [PMID: 25653439](https://pubmed.ncbi.nlm.nih.gov/25653439/).
- **Progression rate:** Rapid, self-limited over ~3–4 weeks in survivors; crusts separate leaving pitted scars. Death in fatal cases typically occurred in the second week.
- **Course pattern:** Monophasic acute illness (not relapsing/chronic). No chronic or latent carrier state.
- **Infectious period:** From rash onset through the first 7–10 days of rash [PMID: 21431786](https://pubmed.ncbi.nlm.nih.gov/21431786/).
- **Critical intervention window:** Post-exposure vaccination within ~3–4 days can prevent or attenuate disease — the basis for ring vaccination [PMID: 21431786](https://pubmed.ncbi.nlm.nih.gov/21431786/).

---

## 9. Inheritance and Population

- **Inheritance:** None — infectious, not heritable. Sections on penetrance, expressivity, anticipation, mosaicism, founder effects, consanguinity, and carrier frequency are **not applicable**.
- **Epidemiology (historical):** Before eradication, smallpox was endemic worldwide and caused an estimated ~300 million deaths in the 20th century alone. Last endemic natural case: Somalia, October 1977; WHO certified eradication in 1980 [PMID: 42135325](https://pubmed.ncbi.nlm.nih.gov/42135325/). Current incidence/prevalence: **zero** (eradicated).
- **Geographic distribution:** Formerly global. The two viral clades map geographically — Clade 2 includes West African and alastrim (variola minor) strains [PMID: 28749451](https://pubmed.ncbi.nlm.nih.gov/28749451/).
- **Sex ratio:** No strong sex predilection; outcome driven by vaccination status, age, pregnancy, and clinical form rather than sex.
- **Age distribution:** All ages susceptible when unvaccinated; young children and the elderly had higher case-fatality historically.

---

## 10. Diagnostics

**Clinical diagnosis (historical):** Based on the characteristic synchronous, deep-seated, centrifugal vesiculopustular rash with palm/sole involvement and febrile prodrome.

**Laboratory confirmation:**
- **PCR / real-time PCR** on lesion material — the modern confirmatory standard for orthopoxvirus/VARV identification.
- **Electron microscopy** — brick-shaped orthopoxvirus virions in vesicle fluid (identifies genus, not species).
- **Serology / immunohistochemistry** — supportive; IHC localizes viral antigen in tissue (used in the macaque model) [PMID: 15477589](https://pubmed.ncbi.nlm.nih.gov/15477589/).
- **Viral culture and genome sequencing** for definitive speciation and clade assignment [PMID: 28749451](https://pubmed.ncbi.nlm.nih.gov/28749451/).

**Laboratory abnormalities in severe disease:** profound leukocytosis, thrombocytopenia, elevated creatinine, and D-dimer elevation (coagulation activation) [PMID: 15477589](https://pubmed.ncbi.nlm.nih.gov/15477589/).

**Clinical criteria:** WHO case definition (acute onset of fever ≥38.3°C followed by firm, deep-seated vesicles/pustules at the same stage of development).

**Differential diagnosis:** Chickenpox (varicella — superficial, pleomorphic lesions in crops, central distribution, spares palms/soles), **mpox/monkeypox** (prominent lymphadenopathy, milder course), disseminated herpes zoster, drug eruptions, and other vesicular illnesses [PMID: 41600835](https://pubmed.ncbi.nlm.nih.gov/41600835/).

**Genetic testing:** Not applicable (no host gene). "Genetic testing" here means **viral** genome sequencing for strain/clade confirmation.

**Screening:** No population screening applies (eradicated disease); surveillance focuses on bioterrorism preparedness and differentiating from mpox.

---

## 11. Outcome / Prognosis

**Case fatality by clinical type (unvaccinated):**

| Clinical form | Approximate frequency | Case-fatality rate |
|---------------|----------------------|--------------------|
| Discrete ordinary | Common | ~10% |
| Confluent ordinary | — | ~50–75% |
| Flat (malignant) | Rare | >95% |
| Hemorrhagic | Rare | >95% |
| Variola major (overall) | ~90% of cases | ~30% |
| Variola minor (alastrim) | — | <1% |

Sources: [PMID: 42135325](https://pubmed.ncbi.nlm.nih.gov/42135325/), [PMID: 42576544](https://pubmed.ncbi.nlm.nih.gov/42576544/).

**Recovery:** Survivors develop lifelong immunity. Sequelae include permanent pockmark scarring (often facial, disfiguring), blindness from keratitis/corneal scarring, and occasionally limb deformities (osteomyelitis variolosa) or encephalitis.

**Prognostic factors:** Clinical type (flat/hemorrhagic forms near-uniformly fatal), vaccination status (vaccinated patients had milder "modified" disease), age (worse in very young and elderly), pregnancy (predisposed to hemorrhagic form), and extent of confluent rash. Early hemorrhagic manifestations and marked thrombocytopenia/coagulopathy portended death [PMID: 15477589](https://pubmed.ncbi.nlm.nih.gov/15477589/).

---

## 12. Treatment

Historically, treatment was **supportive only** (fluids, nutrition, wound care, prevention/treatment of secondary bacterial infection). Modern FDA-approved specific antivirals, developed under the **Animal Rule** (human efficacy trials being impossible/unethical for an eradicated disease):

| Drug | Trade name | Target / mechanism | Basis of approval | NCIT |
|------|-----------|--------------------|--------------------|------|
| **Tecovirimat** | TPOXX | Inhibits orthopoxvirus **VP37/p37** envelope protein required for extracellular (enveloped) virion formation/egress | NHP mpox & rabbitpox models | NCIT:C171621 (Tecovirimat) |
| **Brincidofovir** | Tembexa | Lipid-conjugated **oral prodrug of cidofovir**; viral **DNA-polymerase inhibitor** | Ectromelia (mouse) & rabbitpox (rabbit) surrogate models | NCIT:C97660 (Brincidofovir) |

- Tecovirimat is "approved for smallpox treatment under the Food and Drug Administration Animal Rule on the basis of efficacy in nonhuman primate models of mpox" [PMID: 41740032](https://pubmed.ncbi.nlm.nih.gov/41740032/).
- "Brincidofovir adds a second oral agent to treat smallpox, with a different mechanism of action than tecovirimat" [PMID: 36688308](https://pubmed.ncbi.nlm.nih.gov/36688308/).
- **Cidofovir** (parent compound; DNA-polymerase inhibitor) has activity against orthopoxviruses and reduces MPXV replication in mouse respiratory tract [PMID: 39243894](https://pubmed.ncbi.nlm.nih.gov/39243894/); it is nephrotoxic and not formally smallpox-approved.

**Important caveat on efficacy evidence:** In a randomized human **mpox** (clade II) trial, tecovirimat showed **no benefit over placebo** (83% vs 84% lesion resolution by day 29), underscoring that smallpox approval rests on **animal efficacy data, not human smallpox trials**, and that antiviral efficacy against human orthopoxvirus disease remains uncertain [PMID: 41740032](https://pubmed.ncbi.nlm.nih.gov/41740032/). Emerging tecovirimat resistance (VP37 mutations) is a further concern, motivating combination regimens [PMID: 41038284](https://pubmed.ncbi.nlm.nih.gov/41038284/).

**Pharmacogenomics / gene therapy / cell therapy / targeted & immunotherapy:** Not applicable in the conventional oncologic/genetic sense; the "targeted therapy" here is the host- and virus-directed small-molecule antivirals above.

---

## 13. Prevention

Prevention is the triumph of smallpox control and the reason for its eradication.

**Primary prevention — vaccination (vaccinia-based, cross-protective):**

| Vaccine | Platform | Key properties |
|---------|----------|----------------|
| **Dryvax** (1st gen) | Replication-competent vaccinia (calf lymph) | Eradication-era vaccine; durable immunity 40–80 years [PMID: 40311645](https://pubmed.ncbi.nlm.nih.gov/40311645/) |
| **ACAM2000** (2nd gen) | Clonal replication-competent vaccinia | Current US stockpile; defined risk profile [PMID: 42576544](https://pubmed.ncbi.nlm.nih.gov/42576544/) |
| **MVA-BN / JYNNEOS** (3rd gen) | Non-replicating Modified Vaccinia Ankara | Safer for immunocompromised; sustained memory ≥5 years with strong booster effect [PMID: 41819114](https://pubmed.ncbi.nlm.nih.gov/41819114/) |

- **Edward Jenner's cowpox-based vaccination (1796)** founded the field of immunization and underpinned eradication [PMID: 39371745](https://pubmed.ncbi.nlm.nih.gov/39371745/).
- Protective immunity must target **both virion forms** — the intracellular mature virion (IMV) and extracellular enveloped virion (EEV) — because of the dual-virion architecture of orthopoxviruses; rational vaccines target IMV antigens (A27/L1 ≈ A29L/M1R) and EEV antigens (B5/A33 ≈ B6R/A35R) [PMID: 41941064](https://pubmed.ncbi.nlm.nih.gov/41941064/). A DNA "4pox" vaccine targeting L1, A27, B5, A33 protected rabbits against lethal aerosol rabbitpox [PMID: 34851148](https://pubmed.ncbi.nlm.nih.gov/34851148/).

**Public-health strategy:** **Ring vaccination plus case isolation** — identifying cases and vaccinating contacts and contacts-of-contacts — eradicated the disease. Post-exposure vaccination within ~3–4 days prevents/attenuates illness [PMID: 21431786](https://pubmed.ncbi.nlm.nih.gov/21431786/).

**Vaccine safety (serious adverse events of replication-competent vaccinia):** postvaccinial encephalitis, progressive vaccinia, eczema vaccinatum, and generalized vaccinia — "vaccination can accompany complications, such as postvaccinial encephalitis, progressive vaccinia, eczema vaccinatum, and generalized vaccinia" [PMID: 21431786](https://pubmed.ncbi.nlm.nih.gov/21431786/). Death rates are strain-dependent: ~1.4 deaths/million for NYCBH strain vs ~8.4/million for Lister strain [PMID: 16933957](https://pubmed.ncbi.nlm.nih.gov/16933957/). Myocarditis and dilated cardiomyopathy are additional recognized risks [PMID: 26004568](https://pubmed.ncbi.nlm.nih.gov/26004568/). MVA-BN avoids these replication-associated risks, making it suitable for immunocompromised recipients.

---

## 14. Other Species / Natural Disease

- **Host range:** VARV is **strictly human-restricted** with **no animal reservoir** — the decisive biological fact enabling eradication. SPICE's human-complement selectivity (vs vaccinia VCP's bovine-complement preference) is a molecular correlate of this host-restriction [PMID: 28724763](https://pubmed.ncbi.nlm.nih.gov/28724763/).
- **Zoonotic potential:** None for VARV itself. However, **related orthopoxviruses are zoonotic** — monkeypox/mpox virus (from African rodents/primates), cowpox, and novel orthopoxviruses (e.g., a distinct lineage in an Alaska resident) cause human disease, and rising incidence is attributed to waning post-smallpox-vaccination immunity [PMID: 28329402](https://pubmed.ncbi.nlm.nih.gov/28329402/).
- **Comparative biology:** Orthopoxviruses share genome architecture and immune-evasion gene families shaped by ancient gene capture and recent gene loss [PMID: 34253028](https://pubmed.ncbi.nlm.nih.gov/34253028/). Avipoxviruses (fowlpox, penguin/pigeon poxviruses) are more distantly related but carry VARV B22R orthologues, illustrating deep poxvirus gene conservation [PMID: 24919868](https://pubmed.ncbi.nlm.nih.gov/24919868/).

---

## 15. Model Organisms

Because VARV infects only humans and live virus is restricted to two WHO-authorized high-containment laboratories, **surrogate models** are essential and form the regulatory basis for antiviral and vaccine approval:

| Model system | Virus used | Use / phenotype recapitulation | Reference |
|--------------|-----------|-------------------------------|-----------|
| Cynomolgus macaque | **Variola** (Harper/India strains), IV high dose | Reproduces monocyte-associated viremia, lymphoid/skin/mucosal/GI/liver dissemination, leukocytosis, thrombocytopenia, D-dimer rise, hemorrhagic diathesis; requires non-physiologic high dose | [PMID: 15477589](https://pubmed.ncbi.nlm.nih.gov/15477589/) |
| Cynomolgus macaque | **Aerosolized monkeypox** | Recapitulates respiratory entry → lung replication → spread to tonsil/spleen/nodes/colon by day 4 → fever peak day 6 with skin pox; IL-1ra/IL-6/IFN-γ surge | [PMID: 25653439](https://pubmed.ncbi.nlm.nih.gov/25653439/) |
| Rabbit | **Rabbitpox** (aerosol) | Models respiratory, low-dose exposure akin to natural smallpox; used for 4pox DNA vaccine and tecovirimat efficacy | [PMID: 34851148](https://pubmed.ncbi.nlm.nih.gov/34851148/) |
| Mouse | **Ectromelia** (mousepox); intranasal MPXV | Brincidofovir approval surrogate; cidofovir/brincidofovir reduce respiratory viral load | [PMID: 36688308](https://pubmed.ncbi.nlm.nih.gov/36688308/), [PMID: 39243894](https://pubmed.ncbi.nlm.nih.gov/39243894/) |
| In vitro | Vaccinia (prototype) | Entry/fusion mechanics (D8, entry-fusion complex), gene function via transient complementation | [PMID: 22754644](https://pubmed.ncbi.nlm.nih.gov/22754644/), [PMID: 31240675](https://pubmed.ncbi.nlm.nih.gov/31240675/) |

**Model limitations:** No model fully reproduces the human-restricted, low-dose respiratory transmission and the full spectrum of human clinical forms; macaque variola requires large intravenous inocula, and mpox/rabbitpox/mousepox are related-but-distinct viruses. This surrogacy is precisely why antivirals are approved under the Animal Rule rather than on human efficacy.

---

## Key Findings (Consolidated)

### F001 — Smallpox is caused by Variola virus, not a human gene; eradicated 1980
VARV (NCBI Taxon 10255) is a ~186 kb dsDNA *Orthopoxvirus* encoding ~200 proteins and replicating in the cytoplasm. Over 80 proteins in the genome terminal regions carry immune-evasion functions. WHO certified eradication in 1980; retained stocks and loss of population immunity sustain biodefense concern. *"Smallpox, eradicated globally in 1980, remains a major biodefense concern due to retained Variola virus stocks and the absence of population immunity following cessation of routine vaccination."* [PMID: 42576544](https://pubmed.ncbi.nlm.nih.gov/42576544/); [PMID: 12941397](https://pubmed.ncbi.nlm.nih.gov/12941397/).

### F002 — Pathogenesis: monocyte-associated viremia → lymphoid dissemination → multi-organ hemorrhagic diathesis
*"After inoculation, variola was disseminated by means of a monocytic cell-associated viremia"* with antigen in lymphoid tissue, skin, oral mucosa, GI tract, reproductive system, and liver [PMID: 15477589](https://pubmed.ncbi.nlm.nih.gov/15477589/). The aerosol mpox macaque model documents the temporal sequence from respiratory entry to systemic spread and rash [PMID: 25653439](https://pubmed.ncbi.nlm.nih.gov/25653439/).

### F003 — Countermeasures: tecovirimat + brincidofovir (Animal Rule) plus ACAM2000/MVA-BN vaccines
Tecovirimat targets VP37/p37 (egress); brincidofovir is an oral DNA-polymerase inhibitor prodrug — both FDA-approved via animal models [PMID: 41740032](https://pubmed.ncbi.nlm.nih.gov/41740032/), [PMID: 36688308](https://pubmed.ncbi.nlm.nih.gov/36688308/). Vaccinia vaccination carries rare serious adverse events (~1 death/million) [PMID: 21431786](https://pubmed.ncbi.nlm.nih.gov/21431786/), [PMID: 16933957](https://pubmed.ncbi.nlm.nih.gov/16933957/).

### F004 — Clinical classification & case fatality
Ordinary (~90%), modified, flat, hemorrhagic forms plus variola minor; CFR ~10% (discrete) to >95% (flat/hemorrhagic); variola major ~30%, minor <1%. Last natural case 1977; eradication 1980 [PMID: 42135325](https://pubmed.ncbi.nlm.nih.gov/42135325/), [PMID: 42576544](https://pubmed.ncbi.nlm.nih.gov/42576544/), [PMID: 21431786](https://pubmed.ncbi.nlm.nih.gov/21431786/).

### F005 — Two-clade VARV phylogeny mapping onto the virulence divide
*"Based on the genomes of 48 strains, two clades are differentiated: Clade 1 includes variants of variola major, and clade 2 includes West African and variola minor (Alastrim) strains"* [PMID: 28749451](https://pubmed.ncbi.nlm.nih.gov/28749451/). Orthopoxviruses have the largest antidefense-gene complement of any animal virus family [PMID: 34253028](https://pubmed.ncbi.nlm.nih.gov/34253028/).

### F006 — GAG-dependent entry machinery; SPICE inhibits human complement at C3 convertase
*"Four viral proteins associated with the MV membrane facilitate attachment by binding to glycosaminoglycans or laminin on the cell surface"* [PMID: 22754644](https://pubmed.ncbi.nlm.nih.gov/22754644/). SPICE anchors via heparan/chondroitin sulfate and inhibits complement at the C3 convertase step [PMID: 18768877](https://pubmed.ncbi.nlm.nih.gov/18768877/), with human-pathway selectivity mirroring host restriction [PMID: 28724763](https://pubmed.ncbi.nlm.nih.gov/28724763/).

### F007 — Dual-virion vaccine antigens; decades-long immune durability
Protective immunity must target IMV and EEV antigens; both first- and third-generation vaccines elicit antibodies, with strongest responses to EEV antigens B5 and A33, retained 40–80 years after Dryvax [PMID: 40311645](https://pubmed.ncbi.nlm.nih.gov/40311645/). T-cell responses are more sustained than waning antibody [PMID: 41012133](https://pubmed.ncbi.nlm.nih.gov/41012133/); historical vaccination confers ~70% residual cross-protection against mpox [PMID: 39176988](https://pubmed.ncbi.nlm.nih.gov/39176988/).

---

## Mechanistic Model / Interpretation

```
INFECTION → ENTRY → DISSEMINATION → IMMUNE EVASION → TISSUE INJURY → OUTCOME

Respiratory       GAG-dependent        Monocyte-          SPICE blocks        Epithelial        Ordinary
droplet/aerosol → attachment (4    →   associated     →   complement @   →    replication   →   smallpox
on oropharynx     MV proteins) +       viremia to         C3 convertase;      → rash;           (CFR ~10-30%)
                  11-12 protein        lymph nodes,        chemokine/          enanthem
                  entry-fusion         spleen, skin,       cytokine binders                        OR
                  complex              mucosa, liver       blunt innate                         Flat/hemorrhagic
                                                           immunity            Cytokine storm    (CFR >95%)
                                                                               + coagulopathy →
                                                                               multi-organ
                                                                               failure
```

The coherent narrative: VARV is an exquisitely human-adapted orthopoxvirus whose large immune-evasion arsenal (exemplified by human-selective SPICE) permits efficient dissemination via host monocytes. Disease severity is a **branch** determined by the balance between viral replication/immune-evasion and the host adaptive/cytokine response — tipping toward lethal coagulopathic failure in flat/hemorrhagic forms. The same dual-virion biology that complicates vaccine design (needing both IMV and EEV antigens) also explains why vaccinia-based immunity is broadly cross-protective and remarkably durable, which made ring vaccination of a reservoir-free, strictly human pathogen sufficient for eradication.

---

## Evidence Base (selected)

| PMID | Role |
|------|------|
| [12941397](https://pubmed.ncbi.nlm.nih.gov/12941397/) | VARV genome content & immune-evasion gene complement |
| [42576544](https://pubmed.ncbi.nlm.nih.gov/42576544/) | Eradication date, biodefense, ACAM2000 safety |
| [42135325](https://pubmed.ncbi.nlm.nih.gov/42135325/) | Somalia 1976–77 outbreak data; eradication 1980 |
| [15477589](https://pubmed.ncbi.nlm.nih.gov/15477589/) | Variola macaque model — viremia & dissemination |
| [25653439](https://pubmed.ncbi.nlm.nih.gov/25653439/) | Aerosol mpox macaque — temporal pathogenesis & cytokines |
| [28749451](https://pubmed.ncbi.nlm.nih.gov/28749451/) | Two-clade VARV phylogeny; historical specimens |
| [34253028](https://pubmed.ncbi.nlm.nih.gov/34253028/) | Orthopoxvirus antidefense-gene evolution |
| [22754644](https://pubmed.ncbi.nlm.nih.gov/22754644/) | Poxvirus entry machinery |
| [38321165](https://pubmed.ncbi.nlm.nih.gov/38321165/) | D8 drives membrane curvature for fusion |
| [18768877](https://pubmed.ncbi.nlm.nih.gov/18768877/) | SPICE GAG anchoring & C3 convertase inhibition |
| [19667083](https://pubmed.ncbi.nlm.nih.gov/19667083/) | SPICE functional sites; inhibitory mAb |
| [28724763](https://pubmed.ncbi.nlm.nih.gov/28724763/) | SPICE human-pathway selectivity vs VCP |
| [41740032](https://pubmed.ncbi.nlm.nih.gov/41740032/) | Tecovirimat Animal-Rule approval; mpox trial null result |
| [36688308](https://pubmed.ncbi.nlm.nih.gov/36688308/) | Brincidofovir as second oral smallpox antiviral |
| [21431786](https://pubmed.ncbi.nlm.nih.gov/21431786/) | Vaccination strategy, adverse events, post-exposure window |
| [16933957](https://pubmed.ncbi.nlm.nih.gov/16933957/) | Strain-dependent vaccine adverse-event rates |
| [40311645](https://pubmed.ncbi.nlm.nih.gov/40311645/) | EEV antigen dominance; 40–80 yr durability |
| [41012133](https://pubmed.ncbi.nlm.nih.gov/41012133/) | Durable T-cell vs waning antibody |
| [39176988](https://pubmed.ncbi.nlm.nih.gov/39176988/) | ~70% residual cross-protection vs mpox |
| [34851148](https://pubmed.ncbi.nlm.nih.gov/34851148/) | 4pox DNA vaccine (L1/A27/B5/A33) |
| [41941064](https://pubmed.ncbi.nlm.nih.gov/41941064/) | Dual-virion rational/mRNA vaccine design |

---

## Limitations and Knowledge Gaps

1. **No human efficacy data** for antivirals or modern vaccines against actual smallpox — all approvals rest on surrogate animal models (Animal Rule). The negative tecovirimat mpox trial [PMID: 41740032](https://pubmed.ncbi.nlm.nih.gov/41740032/) raises genuine uncertainty about real-world efficacy against human orthopoxvirus disease.
2. **Surrogate-model fidelity:** Variola macaque models require non-physiologic high IV doses; mpox/rabbitpox/mousepox are related but distinct viruses, so pathogenesis inferences carry extrapolation risk.
3. **Host-susceptibility genetics are uncharacterized** — eradication preceded modern GWAS/omics, so no human susceptibility or modifier loci exist.
4. **Correlates of protection remain undefined** — the relative contribution of antibody vs T-cell immunity to durable protection is not fully resolved [PMID: 41012133](https://pubmed.ncbi.nlm.nih.gov/41012133/).
5. **Molecular pathophysiology of the hemorrhagic form** (cytokine-storm/coagulopathy triggers) is inferred from animal models rather than demonstrated in humans.
6. **Antiviral resistance** (tecovirimat VP37 mutations) threatens monotherapy efficacy, and combination-therapy evidence is immature [PMID: 41038284](https://pubmed.ncbi.nlm.nih.gov/41038284/).

---

## Proposed Follow-up Experiments / Actions

1. **Define immune correlates of protection** by longitudinally measuring IMV- vs EEV-directed antibody and T-cell responses after MVA-BN and correlating with protection in NHP challenge, to establish a surrogate endpoint usable for regulatory decisions.
2. **Combination antiviral studies** (tecovirimat + brincidofovir/cidofovir) in NHP variola and rabbitpox models to pre-empt resistance and strengthen the countermeasure stockpile.
3. **Structural/functional targeting of SPICE** — advance the inhibitory monoclonal antibody [PMID: 19667083](https://pubmed.ncbi.nlm.nih.gov/19667083/) as an adjunct therapeutic that restores complement-mediated clearance.
4. **Next-generation multivalent mRNA vaccines** co-targeting conserved IMV (A27/L1) and EEV (B5/A33) antigens, evaluated for durability, imprinting effects, and cross-clade/pan-orthopox coverage [PMID: 41941064](https://pubmed.ncbi.nlm.nih.gov/41941064/).
5. **Preparedness surveillance** leveraging digitized historical outbreak data [PMID: 42135325](https://pubmed.ncbi.nlm.nih.gov/42135325/) and rapid PCR/sequencing diagnostics to distinguish re-emergent VARV (bioterror scenario) from circulating mpox and novel orthopoxviruses [PMID: 28329402](https://pubmed.ncbi.nlm.nih.gov/28329402/).
6. **Characterize residual population immunity** in pre-1980 vaccinated cohorts to inform ring-vaccination feasibility should VARV re-emerge.

---

*Report compiled from 7 confirmed findings and 51 reviewed papers over 5 investigation iterations. Evidence types span human clinical/historical, nonhuman-primate and rodent models, in vitro mechanistic, and computational/phylogenetic sources.*


## Artifacts

- [OpenScientist final report](Smallpox-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Smallpox-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 32 |
| On topic | 23 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 20 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0004651` (4 mentions) - the report calls it "if available", "MONDO"; MONDO calls it **smallpox**
- `HP:0000987` (2 mentions) - the report calls it "Permanent, disfiguring; healed survivors"; HP calls it **Atypical scarring of skin**
- `NCIT:C171621` (1 mention) - the report calls it "Tecovirimat"; NCIT calls it **Impact of Events Scale**
- `NCIT:C97660` (1 mention) - the report calls it "Brincidofovir"; NCIT calls it **Abemaciclib**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000164` (1 mention) - the report calls it "Oral mucosa abnormality"; HP calls it **Abnormality of the dentition**, and lists "Dental abnormality" among its other names
- `HP:0200039` (1 mention) - the report calls it "Papule"; HP calls it **Pustule**, and lists "Pimple" among its other names
- `HP:0001974` (1 mention) - the report calls it "Leukocytosis"; HP calls it **Increased total leukocyte count**, and lists "Leukocytosis" among its other names
- `GO:0046718` (1 mention) - the report calls it "viral entry into host cell"; GO calls it **symbiont entry into host cell**, and lists "viral entry into host cell" among its other names
- `UBERON:0002097` (1 mention) - the report calls it "Primary:** Skin"; UBERON calls it **skin of body**, and lists "entire skin" among its other names
- `UBERON:0000029` (1 mention) - the report calls it "Lymphoreticular system:** lymph nodes"; UBERON calls it **lymph node**
- `UBERON:0000160` (1 mention) - the report calls it "Secondary:** Gastrointestinal tract"; UBERON calls it **intestine**, and lists "intestinal tract" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0004651` - called "if available", "MONDO"
