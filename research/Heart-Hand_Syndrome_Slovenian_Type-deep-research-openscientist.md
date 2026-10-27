---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-27T17:28:26.451723'
end_time: '2026-10-27T17:45:17.680158'
duration_seconds: 1011.23
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Heart-Hand Syndrome, Slovenian Type
  mondo_id: MONDO:0012417
  category: Mendelian
  causal_genes: LMNA
  omim_id: not recorded
  synonyms: atriodigital dysplasia, Slovenian type; cardiac conduction disease-dilated
    cardiomyopathy-brachydactyly syndrome; HHS Slovenian type
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 15
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 12
  validator_version: 0.4.0
term_validation:
  total_terms: 33
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 5
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0100264
    reported_labels:
    - Symphalangism affecting the phalanges
    ontology_label: Proximal symphalangism
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Heart-Hand_Syndrome_Slovenian_Type-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Heart-Hand_Syndrome_Slovenian_Type-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Heart-Hand Syndrome, Slovenian Type
- **MONDO ID:** MONDO:0012417 (if available)
- **Causal gene(s):** LMNA
- **OMIM:** not recorded
- **Synonyms:** atriodigital dysplasia, Slovenian type; cardiac conduction disease-dilated cardiomyopathy-brachydactyly syndrome; HHS Slovenian type
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Heart-Hand Syndrome, Slovenian Type** covering all of the
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

# Heart-Hand Syndrome, Slovenian Type — Comprehensive Disease Report

**MONDO:** MONDO:0012417 · **OMIM:** #610140 · **Causal gene:** *LMNA* (lamin A/C; HGNC:6636; NCBI Gene 4000; Ensembl ENSG00000160789; UniProt P02545; cytoband 1q22)

---

## Summary

**Heart-Hand Syndrome, Slovenian Type is an ultra-rare, autosomal dominant Mendelian laminopathy caused by a heterozygous germline splice-site mutation in the *LMNA* gene — c.1609-12T>G (IVS9-12 T>G).** *LMNA* encodes the nuclear intermediate-filament proteins lamin A and lamin C (produced by alternative splicing of a single gene), which form the nuclear lamina underlying the inner nuclear membrane. The Slovenian mutation creates a cryptic splice site that retains 11 intronic nucleotides in the mRNA, introducing a frameshift and producing a truncated lamin A/C protein with demonstrable nuclear-envelope abnormalities in patient fibroblasts [PMID: 18611980]. Although the syndrome's name ("heart-hand") superficially evokes Holt-Oram syndrome (a *TBX5* disorder), this is a genetically and phenotypically distinct entity driven by *LMNA*, and must not be confused with it.

Clinically, the disorder is a **dual-system disease**: (1) an adult-onset, progressive cardiac laminopathy featuring sinoatrial and atrioventricular conduction disease, atrial and ventricular tachyarrhythmias, dilated cardiomyopathy (DCM), and a high risk of sudden cardiac death; and (2) a **congenital, distinctive brachydactyly that is mild in the hands and more severe in the feet** (foot-predominant), which distinguishes it from the thumb/radial-ray anomalies of Holt-Oram syndrome. The entity was defined in a single large Slovenian four-generation kindred with 10 affected members [PMID: 15996213], and the causal *LMNA* mutation was identified subsequently [PMID: 18611980]. Linkage analysis formally excluded the loci for Holt-Oram syndrome, ulnar-mammary syndrome, brachydactyly type B, Robinow syndrome, and cardiac conduction disease/Brugada syndrome.

**Management** follows the broader *LMNA*-cardiomyopathy paradigm: genotype-guided implantable cardioverter-defibrillator (ICD) and pacemaker therapy for sudden-death prevention (beyond standard LVEF-based criteria), standard heart-failure pharmacotherapy, cascade genetic screening of relatives, avoidance of high-intensity competitive sport, and emerging disease-modifying therapy with the selective p38α-MAPK inhibitor ARRY-371797 (PF-07265803). The underlying mechanisms — nuclear-lamina fragility, microtubule-force–driven nuclear damage, hyperactivated MAPK and dysregulated WNT/β-catenin signaling, and RUNX1-driven fibrotic remodeling — have been established largely in *LMNA* cardiomyopathy models (the Lmna^H222P/H222P mouse and patient-derived iPSC-cardiomyocytes) rather than in Slovenian-type patients specifically.

---

## Key Findings

### Finding 1 — The disease is an *LMNA* laminopathy caused by the splice mutation c.1609-12T>G

Renou and colleagues identified a heterozygous *LMNA* mutation, **c.1609-12T>G (IVS9-12 T>G)**, segregating with disease in the originally reported Slovenian family [PMID: 18611980]. The mutation lies in intron 9 and *"creates a new cryptic splicing site with the retention of 11 intronic nucleotides in the mRNA."* This retention shifts the reading frame and yields a prematurely truncated lamin A/C protein. Crucially, analysis of fibroblasts from two affected family members *"identified for the first time a truncated lamin A/C protein resulting from the frame shift created by the new splicing site, together with nuclear envelope abnormalities confirming that this LMNA mutation is pathogenic"* [PMID: 18611980]. The authors concluded that *"this new heart-hand syndrome should therefore be considered as a new kind of laminopathy."*

This finding anchors the disease firmly to *LMNA*, the gene named in the research template, and provides direct molecular evidence (protein truncation + nuclear-envelope abnormality) that the variant is disease-causing rather than merely co-segregating. **Variant classification:** splice-site (intronic, splice-region/cryptic-splice-activating); per ACMG/AMP logic, pathogenic given co-segregation, functional protein-level consequence, and absence from population databases. **Functional consequence:** production of a truncated lamin A/C — a combination of loss of normal lamin function and a likely dominant-negative/structurally deleterious effect on the lamina meshwork.

### Finding 2 — Clinical phenotype: adult-onset progressive conduction disease, DCM, sudden death, and foot-predominant brachydactyly

Sinkovec et al. described a four-generation family with 10 affected members *"suffering from adult-onset progressive sinoatrial and atrioventricular conduction disease, sudden death due to ventricular tachyarrhythmia, dilated cardiomyopathy, and a unique type of brachydactyly with mild hand involvement (short distal, middle, proximal phalanges and clinodactyly) and more severe foot involvement"* [PMID: 15996213]. The foot involvement is strikingly severe and specific: short distal and proximal phalanges and metatarsals, short or absent middle phalanges, terminal symphalangism, duplication of the bases of the second metatarsals, extra ossicles, and syndactyly. Renou et al. corroborated the cardiac/skeletal dyad, reporting *"adult onset progressive conduction system disease, atrial and ventricular tachyarrhythmias, sudden death, dilated cardiomyopathy, and brachydactyly with predominant foot involvement"* [PMID: 18611980].

**Phenotype table with suggested HPO terms:**

| Phenotype | Type | Onset | HPO term (suggested) |
|---|---|---|---|
| Sinoatrial/AV conduction disease (progressive heart block) | Clinical sign (ECG) | Adult-onset, progressive | HP:0001678 (Atrioventricular block); HP:0011675 (Arrhythmia) |
| Atrial tachyarrhythmia (AF/flutter) | Clinical sign | Adult | HP:0004749 (Atrial arrhythmia) |
| Ventricular tachyarrhythmia (VT/VF) | Clinical sign | Adult | HP:0004756 (Ventricular arrhythmia) |
| Dilated cardiomyopathy | Physical/imaging | Adult | HP:0001644 (Dilated cardiomyopathy) |
| Sudden cardiac death | Outcome | Adult | HP:0001645 (Sudden cardiac death) |
| Brachydactyly, hand (mild) | Physical malformation | Congenital | HP:0001156 (Brachydactyly) |
| Clinodactyly | Physical malformation | Congenital | HP:0030084 (Clinodactyly) |
| Foot brachydactyly / short metatarsals (severe) | Physical malformation | Congenital | HP:0001831 (Short toe); HP:0010743 (Short metatarsal) |
| Symphalangism (terminal, feet) | Physical malformation | Congenital | HP:0100264 (Symphalangism affecting the phalanges) |
| Syndactyly (feet) | Physical malformation | Congenital | HP:0001159 (Syndactyly) |

The two components differ in timing: the **skeletal phenotype is congenital and static**, while the **cardiac phenotype is adult-onset and relentlessly progressive**. This temporal split is clinically important — young carriers may show only subtle brachydactyly and must be followed for later cardiac decompensation.

### Finding 3 — Mechanism: weakened nuclear lamina and microtubule-driven nuclear damage

The upstream lesion is loss of lamina integrity. As stated succinctly in the LMNA-cardiomyopathy literature, *"Mutations in LMNA, which encodes lamin A/C, weaken the nuclear lamina, leading to nuclear damage and muscle disease"* [PMID: 41073815]. The Slovenian truncated protein directly produces nuclear-envelope abnormalities in patient fibroblasts [PMID: 18611980], providing the patient-specific link to this general mechanism.

The proximate driver of nuclear injury in cardiomyocytes was clarified by Amiad Pavlov et al.: in lamin A/C-deficient hearts, **microtubule forces — rather than LINC-complex-transmitted contractile strain — create local stress concentrations that damage the fragile nucleus.** Critically, *"Microtubule disruption prevented nuclear damage and preserved cardiac function in lamin A/C deficiency"* [PMID: 41073815], nominating the microtubule cytoskeleton as a mechanistic driver and candidate therapeutic target.

### Finding 4 — Downstream signaling: MAPK hyperactivation, WNT/β-catenin suppression, RUNX1-driven EndoMT

Model systems reveal the signaling cascades that translate nuclear damage into myocardial dysfunction. In the Lmna^H222P/H222P knock-in mouse, MAPK branches (ERK, JNK, p38) are hyperactivated, and pharmacological blockade improves cardiac function [PMID: 30319452; PMID: 27649756]. WNT/β-catenin signaling is decreased with reduced connexin-43; Le Dour et al. showed that *"Activation of WNT/β-catenin activity with 6-bromoindirubin-3'-oxime improved cardiac contractility and ameliorated intraventricular conduction defects in LmnaH222P/H222P mice, which was associated with increased expression of myocardial connexin 43"* [PMID: 28069793] — directly linking the WNT/connexin-43 axis to the conduction defects that define this disease. More recently, RUNX1-driven endothelial-to-mesenchymal transition (EndoMT) was identified as a fibrotic remodeling mechanism in human LMNA-DCM hearts and the H222P mouse, where *"Genetic and pharmacological RUNX1 inhibition strategies were evaluated in vitro and in vivo"* [PMID: 42578927].

### Finding 5 — *LMNA* genotype confers among the highest arrhythmic and heart-failure risk in DCM

Large cohort data place *LMNA* among the most dangerous DCM genotypes. In a multicentre genotype-first analysis of 534 DCM patients with (likely) pathogenic variants, *"FLNC, LMNA, DSP, and PLN variants were linked to arrhythmias"* and *"the genotype-first approach showed that LMNA, FLNC, and BAG3 variants had the highest risk for heart failure"* endpoints [PMID: 40938777]. This independently corroborates the sudden-death-prone, heart-failure-progressive natural history observed in the Slovenian kindred and justifies aggressive, genotype-guided risk management.

### Finding 6 — Inheritance: autosomal dominant with incomplete, age-dependent penetrance

Cardiolaminopathies are autosomal dominant with incomplete penetrance. In 27 families, *"Sixty of 94 (64%) were phenotypically affected whereas 34 were only genotypically affected"* [PMID: 18926329]; events included heart transplants, sudden cardiac deaths, and appropriate ICD interventions. Importantly, *"New York Heart Association functional class III to IV and highly dynamic competitive sports for ≥10 years were independent predictors of total events"* [PMID: 18926329], identifying intense competitive sport as a modifiable lifestyle risk factor. Vytopil et al. emphasize that *"incomplete penetrance of dominant mutations in the LMNA gene is a common feature… asymptomatic carriers face high risk of sudden cardiac death"* [PMID: 12467752], underscoring the value of cascade screening. Because the Slovenian variant is itself a splice-site mutation — a category flagged as adverse in LMNA risk models — carriers warrant heightened surveillance.

### Finding 7 — Management: ICD for sudden-death prevention and emerging p38α inhibitor therapy

*LMNA* mutations confer high sudden-death risk, and *"mutations in some known disease genes, including LMNA, have been associated with a high risk of SD"* [PMID: 23946316], supporting earlier, genotype-guided ICD implantation that does not wait for LVEF ≤35%. For disease modification, the oral selective p38α-MAPK inhibitor ARRY-371797/PF-07265803 showed benefit in a phase 2 open-label study of 12 symptomatic LMNA-DCM patients — *"ARRY-371797 was well tolerated and resulted in potential increases in functional capacity and lower concentrations of cardiac biomarker NT-proBNP in patients with"* LMNA-DCM [PMID: 36515663] (6-minute walk +69 m at week 12; NT-proBNP 1409→848 pg/mL; LVEF stabilized). Benefits were durable to ~120 weeks in the long-term extension, where mean 6MWT increased by >30 m (>10%) and NT-proBNP reductions were maintained with good tolerability [PMID: 36114020]. The pivotal phase 3 REALM-DCM trial (NCT02351856) followed.

### Finding 8 — Diagnosis rests on *LMNA* sequencing plus cardiac/skeletal workup; distinguished from Holt-Oram

Diagnosis is clinical (adult-onset conduction disease + DCM + foot-predominant brachydactyly) confirmed by *LMNA* molecular testing — single-gene testing or a cardiomyopathy gene panel/WES — identifying c.1609-12T>G. Formal differential diagnosis was established by linkage: *"linkage exclusion of Holt-Oram syndrome, ulnar-mammary syndrome, brachydactyly type B or Robinow syndrome, and cardiac conduction disease or Brugada syndrome loci suggest that we report on a new hereditary heart-hand syndrome"* [PMID: 15996213]. The prototypical heart-hand syndrome, Holt-Oram (TBX5), is distinct: *"Holt-Oram syndrome (HOS) is a rare autosomal dominant disorder characterized by upper limb and congenital heart anomalies, with an estimated incidence of 1 in 100,000 live births"* [PMID: 42677002] — i.e., radial-ray/thumb malformations with congenital septal defects (ASD/VSD), whereas the Slovenian type has **foot-predominant brachydactyly, no septal defects, and adult-onset progressive conduction/myopathic disease**.

### Finding 9 — Disease identity, identifiers, and ultra-rare epidemiology (single kindred)

**Identifiers:** MONDO:0012417; OMIM #610140 (HEART-HAND SYNDROME, SLOVENIAN TYPE; HHS); causal gene *LMNA* (HGNC:6636; NCBI Gene 4000; Ensembl ENSG00000160789; UniProt P02545; cytoband 1q22; encodes lamins A and C by alternative splicing). **Synonyms:** atriodigital dysplasia, Slovenian type; cardiac conduction disease–dilated cardiomyopathy–brachydactyly syndrome; HHS Slovenian type. **ICD:** no dedicated ICD-10/ICD-11 or MeSH descriptor exists; best-fit descriptive ICD-10 codes are I42.0 (dilated cardiomyopathy), I44/I45 (conduction disorders), and a Q87.4-type congenital malformation syndrome code. **Epidemiology:** described in a single large Slovenian four-generation kindred — *"We identified a family with 10 affected members in four generations"* [PMID: 15996213] — so prevalence is unknown and plausibly <1 in 1,000,000; the evidence base is derived from **individual-patient family studies, not aggregated registries**.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

```
1.  Germline heterozygous LMNA splice mutation c.1609-12T>G (intron 9)
        │  creates a cryptic splice site
        ▼
2.  Retention of 11 intronic nucleotides in LMNA mRNA  [demonstrated, PMID 18611980]
        │  frameshift
        ▼
3.  Truncated lamin A/C protein  [demonstrated in patient fibroblasts]
        │  disrupts assembly of the nuclear lamina meshwork
        ▼
4.  Weakened/fragile nuclear lamina + nuclear-envelope abnormalities  [demonstrated]
        │
        ├──► CARDIAC BRANCH (adult-onset, progressive) ───────────────────────────┐
        │                                                                          │
        │  5a. In contracting cardiomyocytes, MICROTUBULE forces concentrate       │
        │      mechanical stress on the fragile nucleus → nuclear damage           │
        │      [demonstrated in LMNA-deficient hearts, PMID 41073815; inferred     │
        │       for Slovenian variant specifically]                               │
        │          ▼                                                               │
        │  6a. Mechanotransduction / signaling dysregulation:                      │
        │        • MAPK (ERK/JNK/p38) hyperactivation  [model, PMID 30319452]      │
        │        • WNT/β-catenin ↓ → connexin-43 ↓  [model, PMID 28069793]         │
        │        • RUNX1-driven endothelial-to-mesenchymal transition (EndoMT)     │
        │          → fibrosis  [human + model, PMID 42578927]                      │
        │          ▼                                                               │
        │  7a. Conduction-system degeneration + myocardial fibrosis +              │
        │      contractile failure                                                 │
        │          ▼                                                               │
        │  8a. Sinoatrial/AV block → atrial & ventricular tachyarrhythmias →        │
        │      dilated cardiomyopathy → heart failure → SUDDEN CARDIAC DEATH        │
        │      [clinical, PMID 15996213; 18611980]                                 │
        │                                                                          │
        └──► SKELETAL BRANCH (congenital, static) ─────────────────────────────────┘
             5b. Lamina dysfunction in developing limb mesenchyme/chondrocytes
                 perturbs digit/metatarsal patterning  [mechanism inferred; the
                 molecular link between LMNA and foot-predominant brachydactyly is
                 NOT established]
                 ▼
             6b. Foot-predominant brachydactyly: short/absent phalanges, short
                 metatarsals, symphalangism, syndactyly, extra ossicles; mild hand
                 involvement + clinodactyly  [clinical, PMID 15996213]
```

**Upstream vs downstream.** Steps 1–4 (mutation → truncated protein → fragile lamina) are the shared upstream trigger for both branches. The cardiac branch's microtubule-force step (5a) and the downstream MAPK/WNT/RUNX1 signaling (6a) are **mechanistically demonstrated in LMNA cardiomyopathy models** and are therefore strongly inferred — but not individually proven — for the Slovenian variant. The skeletal branch (5b–6b) remains the biggest mechanistic gap: how a lamina defect produces a *foot-predominant* digital malformation is unknown and represents a genuinely novel, unexplained developmental phenotype for *LMNA*.

**Cell types and compartments involved.** Primary cell types: cardiomyocytes (CL:0000746), cardiac conduction-system cells / pacemaker cells (CL:0000182-adjacent), cardiac fibroblasts (CL:0002548), and endocardial/endothelial cells undergoing EndoMT (CL:0000115). Developmentally, limb-bud mesenchyme and chondrocytes (CL:0000138). Subcellular compartments: **nuclear lamina / nuclear envelope (GO:0005652 nuclear lamina; GO:0005635 nuclear envelope)**, nucleoskeleton, and the microtubule cytoskeleton (GO:0005874). Biological processes (suggested GO): nuclear envelope organization (GO:0006998), cardiac conduction (GO:0061337), regulation of heart contraction (GO:0008016), endothelial-to-mesenchymal transition, Wnt signaling pathway (GO:0016055), MAPK cascade (GO:0000165). Anatomy (suggested UBERON): heart (UBERON:0000948), cardiac conduction system / sinoatrial node (UBERON:0002351), atrioventricular node (UBERON:0002352), myocardium (UBERON:0002349), metatarsal bone (UBERON:0001448), phalanx of pes (UBERON:0001449).

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [18611980](https://pubmed.ncbi.nlm.nih.gov/18611980/) | *Heart-hand syndrome of Slovenian type: a new kind of laminopathy* | Human clinical + in vitro (fibroblasts) | F1 (causal splice mutation c.1609-12T>G; truncated protein; nuclear-envelope abnormality); F2 (phenotype); F9 (identity) |
| [15996213](https://pubmed.ncbi.nlm.nih.gov/15996213/) | *Familial progressive sinoatrial and AV conduction disease… a new type of heart-hand syndrome?* | Human clinical + linkage | F2 (full phenotype, foot-predominant brachydactyly); F8 (differential dx via linkage exclusion); F9 (single kindred) |
| [41073815](https://pubmed.ncbi.nlm.nih.gov/41073815/) | *Microtubule forces drive nuclear damage in LMNA cardiomyopathy* | Model organism / mechanistic | F3 (lamina weakening → nuclear damage; microtubules as driver/target) |
| [28069793](https://pubmed.ncbi.nlm.nih.gov/28069793/) | *Decreased WNT/β-catenin signalling… DCM caused by LMNA* | Mouse (H222P) | F4 (WNT/β-catenin↓, connexin-43↓, conduction defects reversible) |
| [42578927](https://pubmed.ncbi.nlm.nih.gov/42578927/) | *RUNX1-driven EndoMT contributes to remodelling in LMNA cardiomyopathy* | Human tissue + mouse | F4 (RUNX1-EndoMT fibrosis as target) |
| [30319452](https://pubmed.ncbi.nlm.nih.gov/30319452/) | *Role of Lamin A/C mutations in signaling defects leading to cardiomyopathies* | Review | F4 (MAPK hyperactivation) |
| [27649756](https://pubmed.ncbi.nlm.nih.gov/27649756/) | *Animal and iPSC modeling of cardiac laminopathy* | Review | F4 (MAPK-targeted strategies; iPSC-CM platform) |
| [31220270](https://pubmed.ncbi.nlm.nih.gov/31220270/) | *Performance alteration in a mouse model of EDMD (Lmna gene mutation)* | Mouse (H222P) | Model (H222P recapitulates DCM + conduction block + skeletal myopathy) |
| [40938777](https://pubmed.ncbi.nlm.nih.gov/40938777/) | *Impact of genotype-phenotype associations on prognosis in DCM* | Human cohort (n=534) | F5 (LMNA among highest arrhythmia/HF risk) |
| [18926329](https://pubmed.ncbi.nlm.nih.gov/18926329/) | *Long-term outcome and risk stratification in dilated cardiolaminopathies* | Human cohort (27 families) | F6 (64% penetrance; sport & NYHA III-IV as predictors) |
| [12467752](https://pubmed.ncbi.nlm.nih.gov/12467752/) | *Frequent low-penetrance LMNA mutations causing EDMD* | Human genetics | F6 (incomplete penetrance; asymptomatic-carrier SCD risk) |
| [23946316](https://pubmed.ncbi.nlm.nih.gov/23946316/) | *Modifying ICD patient selection in non-ischaemic DCM* | Review/guidance | F7 (LMNA high SD risk → genotype-guided ICD) |
| [36515663](https://pubmed.ncbi.nlm.nih.gov/36515663/) | *Efficacy and safety of ARRY-371797 in LMNA-DCM* | Phase 2 trial (n=12) | F7 (p38α inhibitor improves 6MWT, lowers NT-proBNP) |
| [36114020](https://pubmed.ncbi.nlm.nih.gov/36114020/) | *Long-term efficacy/safety of ARRY-371797 in LMNA-DCM* | Phase 2 extension | F7 (durable benefit to ~120 weeks; REALM-DCM phase 3) |
| [42677002](https://pubmed.ncbi.nlm.nih.gov/42677002/) | *Holt-Oram syndrome… case report* | Human clinical | F8 (characterizes the TBX5 heart-hand syndrome to be distinguished) |

**Interpretive note on evidence strength.** The two disease-defining papers (PMID 15996213, 18611980) are the *only* primary sources describing Slovenian-type patients, and both derive from one kindred. All mechanistic depth (microtubules, MAPK, WNT, RUNX1) and all therapeutic evidence (ICD, p38α inhibitor) come from the **broader *LMNA* cardiomyopathy field** and are extrapolated to this specific variant. This extrapolation is biologically reasonable (same gene, same protein-level consequence class, same cardiac phenotype) but has not been tested in Slovenian-type patients.

---

## Section-by-Section Reference Data

- **Etiology (§2):** Monogenic; single heterozygous germline *LMNA* splice variant c.1609-12T>G. No environmental cause. Key modifiable risk marker: ≥10 years of high-intensity competitive sport (adverse) [PMID: 18926329]. No protective alleles or environmental protective factors documented. Gene–environment interaction: mechanical/exercise load plausibly accelerates nuclear damage in the mechanically fragile myocardium (consistent with the microtubule-force mechanism, PMID 41073815).
- **Environmental information (§5):** No toxins, infectious agents, or pollutants implicated. Lifestyle: strenuous competitive athletics is an event predictor in cardiolaminopathy.
- **Anatomy (§7):** Primary organ — heart (conduction system, myocardium). Skeletal — bones of the feet (metatarsals, phalanges) > hands. Subcellular — nuclear lamina/envelope, microtubule cytoskeleton. Lateralization: bilateral skeletal involvement.
- **Temporal development (§8):** Skeletal — congenital, static. Cardiac — adult-onset, chronic, progressive (conduction disease typically precedes/accompanies DCM), punctuated by potentially fatal arrhythmic events.
- **Inheritance & population (§9):** Autosomal dominant; incomplete, age-dependent penetrance (~64% in cardiolaminopathy cohorts); variable expressivity; founder-type private variant confined to one Slovenian kindred; sex ratio not reliably estimable; ultra-rare (<1/1,000,000).
- **Diagnostics (§10):** ECG/Holter (conduction block, atrial/ventricular arrhythmia), echocardiography/cardiac MRI (DCM, fibrosis), skeletal radiographs of hands/feet (brachydactyly pattern), and *LMNA* molecular testing (single-gene or panel/WES). NT-proBNP as a disease-activity/therapy biomarker. Differential: Holt-Oram (TBX5), ulnar-mammary, brachydactyly type B, Robinow, Brugada/isolated conduction disease — all excluded by linkage [PMID: 15996213].
- **Prognosis (§11):** Guarded; high sudden-death and heart-failure risk (among worst DCM genotypes, PMID 40938777); cohort outcomes include heart transplantation and sudden cardiac death [PMID: 18926329].
- **Treatment (§12) with suggested NCIT terms:** ICD implantation (cardioverter-defibrillator), permanent pacemaker, guideline-directed heart-failure therapy (beta-blockers, ACE-I/ARB/ARNI, MRA), anticoagulation for atrial arrhythmia, antiarrhythmics/catheter ablation as needed, heart transplantation for end-stage disease, and investigational p38α-MAPK inhibitor ARRY-371797/PF-07265803 (NCT02351856). Avoid competitive endurance sport.
- **Prevention (§13):** No primary prevention (monogenic). Secondary — cascade genetic testing of relatives, serial cardiac surveillance of carriers, early ICD/pacemaker. Genetic counseling for 50% offspring transmission risk; prenatal/PGT technically feasible given the known familial variant.
- **Model organisms (§15):** No Slovenian-variant-specific model exists. The Lmna^H222P/H222P knock-in mouse (NCBI Gene: Lmna, mouse ID 16905) recapitulates DCM with conduction block and skeletal (EDMD) myopathy [PMID: 31220270] and is the workhorse for mechanism (MAPK, WNT/β-catenin, RUNX1) and therapy testing. Patient-derived iPSC-cardiomyocytes provide a complementary human platform [PMID: 27649756]. **Limitation:** these models reproduce the cardiac/muscle phenotype but **do not model the foot-predominant brachydactyly**, the feature most unique to the Slovenian type.
- **Other species (§14):** Orthologous gene *Lmna* exists across mammals (mouse *Lmna*, NCBI Gene 16905). No naturally occurring animal counterpart of the Slovenian heart-hand syndrome is documented in OMIA. Not zoonotic/transmissible.

---

## Limitations and Knowledge Gaps

1. **Single-kindred evidence base.** The entire clinical definition rests on one Slovenian family (10 affected individuals) across two primary papers [PMID: 15996213; 18611980]. Penetrance, expressivity, sex ratio, and natural-history quantification specific to this variant cannot be estimated from aggregated data.
2. **Unexplained skeletal mechanism.** The molecular path from a lamina defect to a *foot-predominant* brachydactyly with symphalangism and metatarsal anomalies is entirely unknown. No model reproduces it, and it is atypical for *LMNA*, which usually spares limb patterning.
3. **Extrapolated mechanism and therapy.** Microtubule-force nuclear damage, MAPK/WNT/RUNX1 signaling, ICD benefit, and p38α-inhibitor efficacy are all derived from general *LMNA*-DCM models/cohorts, not Slovenian-type patients.
4. **No variant-level population data.** c.1609-12T>G is absent from standard population databases (expected for a private familial variant); formal ACMG splicing evidence (RNA assay beyond the original fibroblast work) in additional carriers is lacking.
5. **No dedicated ICD/MeSH coding**, complicating registry capture and epidemiology.

## Proposed Follow-up Experiments / Actions

1. **Identify and phenotype additional kindreds/carriers** (GeneMatcher, cardiomyopathy-panel databases) to refine penetrance, expressivity, and the arrhythmia/heart-failure event rate for c.1609-12T>G specifically.
2. **Model the skeletal phenotype:** generate a knock-in mouse or iPSC-derived limb-bud/chondrocyte organoid carrying c.1609-12T>G (or an equivalent truncating splice allele) to test whether lamina truncation perturbs digit/metatarsal patterning, and probe candidate limb-patterning pathways (e.g., WNT, BMP) in that context.
3. **Direct mechanistic test in a variant-specific iPSC-cardiomyocyte line:** confirm microtubule-force–driven nuclear damage (PMID 41073815), MAPK hyperactivation, and WNT/connexin-43 suppression, and screen p38α inhibition, microtubule stabilization/destabilization, and RUNX1 inhibition for rescue.
4. **Prospective cardiac surveillance protocol** for all living carriers (annual ECG/Holter/echo/MRI, NT-proBNP), with pre-specified genotype-guided ICD thresholds, to generate natural-history data.
5. **Pursue inclusion in LMNA-DCM therapeutic trials** (e.g., p38α-inhibitor programs) where eligibility criteria permit, given the shared cardiac mechanism.
6. **Formal variant re-classification dossier** (ACMG/AMP) consolidating segregation, the fibroblast functional data, and any new RNA/splicing assays to lock in a Pathogenic classification in ClinVar.

---

*Report compiled from 9 confirmed findings and 23 reviewed papers over a 5-iteration autonomous investigation. Evidence source types are annotated per claim (human clinical, model organism, in vitro, review). The causal gene for Heart-Hand Syndrome, Slovenian Type is **LMNA**.*


## Artifacts

- [OpenScientist final report](Heart-Hand_Syndrome_Slovenian_Type-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Heart-Hand_Syndrome_Slovenian_Type-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 8 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0100264` (1 mention) - the report calls it "Symphalangism affecting the phalanges"; HP calls it **Proximal symphalangism**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0004749` (1 mention) - the report calls it "Atrial arrhythmia"; HP calls it **Atrial flutter**
- `HP:0004756` (1 mention) - the report calls it "Ventricular arrhythmia"; HP calls it **Ventricular tachycardia**