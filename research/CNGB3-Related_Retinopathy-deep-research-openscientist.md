---
provider: openscientist
model: openscientist-autonomous
cached: true
start_time: '2026-11-03T00:16:16.498901'
end_time: '2026-11-03T00:16:23.147968'
duration_seconds: 6.65
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: CNGB3-Related Retinopathy
  mondo_id: MONDO:0100446
  category: Mendelian
  causal_genes: CNGB3
  omim_id: not recorded
  synonyms: CNGB3 retinopathy
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
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 31
reference_validation:
  total_references: 31
  verified: 31
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 17
  quotes_valid: 17
  relevance_assessed: 31
  on_topic: 30
  validator_version: 0.4.0
term_validation:
  total_terms: 32
  verified: 30
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 6
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0100446
    reported_labels:
    - 'OMIM #262300'
    - MONDO
    ontology_label: CNGB3-related retinopathy
  - term_id: CL:0000573
    reported_labels:
    - cone photoreceptor cell
    - 'Primary cell type: **cone photoreceptor cell'
    - cone photoreceptors
    ontology_label: retinal cone cell
  labels_variant: 2
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
  path: CNGB3-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: CNGB3-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CNGB3-Related Retinopathy
- **MONDO ID:** MONDO:0100446 (if available)
- **Causal gene(s):** CNGB3
- **OMIM:** not recorded
- **Synonyms:** CNGB3 retinopathy
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **CNGB3-Related Retinopathy** covering all of the
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

# CNGB3-Related Retinopathy (Achromatopsia Type 3): Comprehensive Disease Report

**Target disease:** CNGB3-Related Retinopathy — MONDO:0100446 — OMIM #262300 (Achromatopsia 3)
**Causal gene:** **CNGB3** (cyclic nucleotide-gated channel beta 3; HGNC:2153; NCBI Gene 54714; Ensembl ENSG00000170289; UniProt Q9NQW8; chromosome 8q21.3), encoding the β (modulatory) subunit of the cone cyclic nucleotide-gated (CNG) cation channel.

---

## Summary

**CNGB3-related retinopathy is a congenital, autosomal recessive cone dysfunction syndrome ("achromatopsia," ACHM) caused by biallelic loss-of-function variants in *CNGB3*, the gene encoding the modulatory β-subunit of the cone cyclic nucleotide-gated cation channel.** Loss of a functional cone CNG channel abolishes the final step of cone phototransduction, producing the clinical tetrad of severely reduced visual acuity (~20/200), absent or severely impaired color discrimination, photophobia/photoaversion, and infantile (pendular) nystagmus, with a characteristic electroretinogram (ERG) pattern of absent photopic (cone) responses and preserved scotopic (rod) responses. The disease is present from birth and was historically regarded as "stationary," but longitudinal structural and functional imaging demonstrates slow progressive cone loss over years.

*CNGB3* is the single most common achromatopsia gene, accounting for approximately 45–50% of all cases, and achromatopsia overall affects roughly 1 in 30,000 people, making it the most common cone dysfunction syndrome. A single frameshift founder allele, **c.1148delC (p.Thr383fs)**, accounts for roughly 70% of all *CNGB3* mutant alleles, which simplifies molecular diagnosis and has important implications for carrier screening and genotype-targeted therapy. The core pathophysiology is a **loss-of-function cone channelopathy**: loss of the channel abolishes the light-sensitive conductance, and disturbed intracellular Ca²⁺/cGMP–PKG signaling together with endoplasmic reticulum (ER) stress and unfolded-protein-response–associated apoptosis drives slow cone degeneration while sparing rods. This has been established in *Cngb3⁻/⁻* mice, cone-dominant (*Nrl⁻/⁻*) ER-stress models, and a naturally occurring canine model.

Management is currently **supportive** — tinted/red-filter contact lenses or spectacles to reduce photophobia, refractive correction, low-vision aids, and genetic counseling. The leading experimental therapy is **AAV-mediated *CNGB3* gene replacement**, which rescues cone function in dog and mouse models. The first-in-human trial (AAV8-hCARp.hCNGB3, NCT03001310) demonstrated acceptable safety but **no consistent efficacy signal at 6 months**, highlighting the central translational challenge: the therapeutic window, cone target availability, and functional plasticity of a lifelong-deprived visual system.

---

## 1. Disease Information

**Overview.** CNGB3-related retinopathy is the *CNGB3* genetic subtype of **achromatopsia (ACHM)**, also called rod monochromatism or complete/incomplete achromatopsia. It is a congenital, autosomal recessive, non-progressive-to-slowly-progressive retinal disorder of isolated cone photoreceptor dysfunction. "Achromatopsia is the most common cone dysfunction syndrome, affecting 1 in 30,000 people. It is an autosomal recessive disorder" ([PMID: 39273686](https://pubmed.ncbi.nlm.nih.gov/39273686/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0100446 |
| OMIM | #262300 (Achromatopsia 3, ACHM3) |
| Gene | *CNGB3* — HGNC:2153; NCBI Gene 54714; Ensembl ENSG00000170289; UniProt Q9NQW8 |
| Gene locus | 8q21.3 |
| Orphanet | ORPHA:49382 (Achromatopsia) |
| MeSH | Color Vision Defects / Achromatopsia |
| ICD-10 | H53.51 (color vision deficiency / achromatopsia) |
| ICD-11 | 9D45 (color vision deficiencies) |

**Synonyms / alternative names:** CNGB3 retinopathy; achromatopsia type 3 (ACHM3); rod monochromacy / rod monochromatism; complete achromatopsia (typical) and incomplete achromatopsia (atypical); total color blindness; cone dysfunction syndrome (CNGB3 subtype).

**Information source.** The information in this report is derived almost entirely from **aggregated disease-level resources** (OMIM, Orphanet, HPO) and from **human clinical case series/cohort studies** plus **model-organism and in-vitro mechanistic studies** — not from individual EHR records.

---

## 2. Etiology

**Primary cause — genetic.** The disease is monogenic and recessive: it requires two pathogenic alleles (homozygous or compound heterozygous) in *CNGB3*. "CNGB3 encoding the beta subunit of the cyclic nucleotide-gated ion channel in cone photoreceptors is the major achromatopsia gene" ([PMID: 28795510](https://pubmed.ncbi.nlm.nih.gov/28795510/)). There are **no established environmental, infectious, toxic, or lifestyle causes**; the disease is not acquired.

**Genetic risk factors.**
- The sole causal factor is biallelic pathogenic variation in *CNGB3*.
- The predominant allele, **c.1148delC (p.Thr383fs)**, "accounts for over 70% of all CNGB3 mutant alleles" ([PMID: 15657609](https://pubmed.ncbi.nlm.nih.gov/15657609/)). An equivalent designation, p.T383fsX, "accounted for 75% (18/24) of disease-associated alleles; intragenic SNPs in unrelated patients revealed transmission of a common haplotype consistent with a founder effect" ([PMID: 17265047](https://pubmed.ncbi.nlm.nih.gov/17265047/)).
- **Consanguinity** increases the chance of homozygosity for recessive alleles; several cohorts comprise consanguineous families (e.g., [PMID: 42099125](https://pubmed.ncbi.nlm.nih.gov/42099125/)).

**Environmental risk factors.** None known. Age and sex are not risk factors; the disease is congenital and affects males and females equally.

**Protective factors.** No genetic or environmental protective factors are established. In principle, inheriting only one pathogenic allele (heterozygous carrier) is non-disease-causing.

**Gene–environment interactions.** None demonstrated. Bright-light exposure exacerbates the *symptom* of photophobia but is not a disease modifier. There is no evidence that any exposure modifies the rate of cone degeneration.

---

## 3. Phenotypes

The clinical phenotype is highly stereotyped across cohorts. In a genetically confirmed ACHM cohort (n=21), "All patients experienced difficulties with color vision, 20 of 21 (95.2%) had photosensitivity, and 18 of 21 patients reported congenital nystagmus" ([PMID: 41867372](https://pubmed.ncbi.nlm.nih.gov/41867372/)). Hallmark features (vision loss, photophobia, color blindness, refractive error, nystagmus) are consistently reported across cohorts ([PMID: 42099125](https://pubmed.ncbi.nlm.nih.gov/42099125/)).

| Phenotype | Type | Onset | Severity | Course | Frequency | HPO term |
|---|---|---|---|---|---|---|
| Color vision loss (achromatopsia) | Symptom / lab (color testing) | Congenital | Severe (complete) to moderate (incomplete) | Stable/slowly progressive | ~100% | HP:0011520 (Defective cone cell function); HP:0000551 (Abnormal color vision) |
| Photophobia / photoaversion | Symptom | Infancy | Moderate–severe | Stable | ~95% | HP:0000613 (Photophobia) |
| Infantile nystagmus (pendular) | Clinical sign | Neonatal/infancy (first months) | Variable; may dampen with age | Often improves | ~85–95% | HP:0001339 (Congenital nystagmus); HP:0000639 (Nystagmus) |
| Reduced visual acuity (~20/200) | Symptom / lab | Congenital | Severe | Slowly progressive | ~100% | HP:0000572 (Visual loss); HP:0007843 (Reduced visual acuity) |
| Absent/reduced photopic ERG | Lab abnormality | Congenital | Severe | Stable | ~100% | HP:0000512 (Abnormal electroretinogram) |
| Refractive error (hyperopia; myopia in some) | Sign | Childhood | Mild–moderate | Stable | Common | HP:0000540 (Hyperopia); HP:0000545 (Myopia) |
| Foveal hypoplasia / EZ disruption | Structural (OCT) | Congenital | Variable | Slowly progressive | Common | HP:0007750 (Foveal hypoplasia) |
| Central scotoma / eccentric fixation | Sign | Childhood | Moderate | Stable | Variable | HP:0000603 (Central scotoma) |

**ERG signature:** "most patients with a normal scotopic response and absent photopic response on electroretinogram" ([PMID: 41867372](https://pubmed.ncbi.nlm.nih.gov/41867372/)) — preserved rod function, absent cone function. This rod/cone dissociation is diagnostic.

**Complete vs. incomplete ACHM.** Complete (typical) achromatopsia shows total loss of color discrimination and acuity ~20/200; incomplete forms retain some residual color vision and slightly better acuity. *CNGB3* most commonly causes complete achromatopsia.

**Quality-of-life impact.** Lifelong low vision, disabling photophobia (bright light markedly worsens function), and nystagmus affect education, mobility, inability to drive, and glare in daily life. In the first-in-human gene therapy trial, 21/23 participants reported some patient-reported QoL benefit, underscoring the measurable daily-functioning burden ([PMID: 37172884](https://pubmed.ncbi.nlm.nih.gov/37172884/)). No disease-specific validated EQ-5D/SF-36 datasets were identified in this investigation.

---

## 4. Genetic / Molecular Information

**Causal gene.** *CNGB3* (OMIM *605080), 8q21.3, encodes the β (modulatory) subunit of the cone CNG channel. The functional cone channel is a heterotetramer of **three CNGA3 (α) + one CNGB3 (β)** subunits. CNGA3 forms the pore; CNGB3 modulates ligand sensitivity, ion permeation, and regulation by calmodulin and phosphoinositides (PMID: 36430626; PMID: 23530136).

**Contribution to disease.** "Of these, 485 (45.2%) carried mutations in CNGB3" out of 1074 families clinically diagnosed with achromatopsia ([PMID: 28795510](https://pubmed.ncbi.nlm.nih.gov/28795510/)); independently, "mutations in the CNGB3 gene are responsible for approximately 50% of all patients with achromatopsia" ([PMID: 15657609](https://pubmed.ncbi.nlm.nih.gov/15657609/)). Combined, "Mutations in the cone CNG channel subunits CNGA3 and CNGB3 account for >70% of all known cases of achromatopsia" ([PMID: 22493484](https://pubmed.ncbi.nlm.nih.gov/22493484/)).

**Pathogenic variants.**
- **Predominant allele:** c.1148delC (p.Thr383fsX, a.k.a. p.Thr383IlefsX13) — a 1-bp frameshift deletion producing a premature stop and loss of function; >70% of *CNGB3* mutant alleles ([PMID: 15657609](https://pubmed.ncbi.nlm.nih.gov/15657609/); [PMID: 17265047](https://pubmed.ncbi.nlm.nih.gov/17265047/)).
- **Variant classes:** predominantly loss-of-function — frameshift, nonsense, splice-site, and large copy-number variations (CNVs/deletions were part of the mutation spectrum reported in [PMID: 28795510](https://pubmed.ncbi.nlm.nih.gov/28795510/)). Missense variants occur but are a minority.
- **Classification:** c.1148delC is **Pathogenic** (ACMG/AMP: null variant in a gene where LOF is a known mechanism, PVS1 + founder/segregation evidence).
- **Allele frequency:** c.1148delC is present at low frequency in gnomAD consistent with a recessive-disease carrier allele; exact population frequencies were not re-derived in this investigation.
- **Origin:** **germline** only; no somatic contribution.
- **Functional consequence:** **loss of function** of the cone CNG channel β-subunit. (By contrast, some *CNGA3* missense variants, e.g., R410W, confer a gain of spontaneous channel activity — see Mechanism.)

**Modifier genes.** No robust disease-severity modifier genes are established for *CNGB3* ACHM. The phenotype (complete vs. incomplete) is primarily allele-driven.

**Epigenetic information.** No disease-specific DNA-methylation or histone-modification changes are established for CNGB3 retinopathy.

**Chromosomal abnormalities.** Large *CNGB3* deletions/CNVs are part of the allelic spectrum ([PMID: 28795510](https://pubmed.ncbi.nlm.nih.gov/28795510/)), but gross aneuploidy or translocations are not features of this disorder.

---

## 5. Environmental Information

**Environmental factors:** None causally implicated. This is a monogenic disease.
**Lifestyle factors:** None. Bright-light environments worsen photophobic *symptoms* but do not cause or modify the disease.
**Infectious agents:** Not applicable — no infectious etiology.

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function variants in *CNGB3*** (most often c.1148delC) **lead to** absent or non-functional CNGB3 β-subunit protein in cone photoreceptors.
2. Loss of the β-subunit **results in** a non-functional or absent cone CNG channel heterotetramer (3×CNGA3 + 1×CNGB3), impairing channel assembly, trafficking, and gating.
3. The defective channel **abolishes** the light-regulated inward Na⁺/Ca²⁺ conductance that normally closes in response to light-driven cGMP hydrolysis — i.e., **loss of the final step of cone phototransduction**.
4. Loss of cone phototransduction **produces** the immediate clinical phenotype: absent photopic ERG, severe color-vision loss, reduced acuity, photophobia, and (via abnormal foveal visual input during development) infantile nystagmus and foveal hypoplasia. *(Rods are spared because they use a distinct CNGA1/CNGB1 channel — scotopic ERG is preserved.)*
5. In parallel, channel deficiency **causes** disturbed intracellular **Ca²⁺/cGMP homeostasis**. (Branch A) Elevated cGMP/PKG signaling with **RYR2 (ryanodine receptor 2) upregulation** **leads to** ER Ca²⁺ dysregulation and protein mislocalization. (Branch B) In certain gain-of-function channel contexts, **spontaneously active channels** admit excess Ca²⁺.
6. ER Ca²⁺ dysregulation and accumulation of mislocalized/misfolded cone proteins **trigger** the **unfolded protein response / ER stress** (↑Grp78/BiP, ↑phospho-eIF2α, ↑CHOP).
7. Sustained ER stress **activates** calpains and caspase-12/caspase-7, **resulting in** **ER-stress–associated cone apoptosis**.
8. Progressive cone apoptosis **produces** the slow structural cone degeneration (EZ disruption, cone-density decline) observed longitudinally, narrowing the therapeutic window — while rods remain intact.

> Steps 1–4 are well demonstrated in human patients and mouse models. Steps 5–7 are demonstrated in cone-dominant mouse models (*Cng*⁻/⁻;*Nrl*⁻/⁻) and in-vitro systems; their quantitative contribution in human CNGB3 retina is inferred.

### Supporting detail

**Molecular pathways / biochemistry.** The affected pathway is **cone phototransduction** (KEGG hsa04744; Reactome "Visual phototransduction"). The cone CNG channel (CNGA3/CNGB3) is the terminal effector. Downstream disturbances involve **cGMP–PKG signaling** and **ER-stress/UPR** (PERK–eIF2α–ATF4–CHOP; IRE1; ATF6). In CNG-deficient cones, "up-regulation of the cysteine protease calpains and cleavage of caspase-12 and caspase-7 were found in the channel-deficient retinas, suggesting an endoplasmic reticulum stress-associated apoptosis" ([PMID: 22493484](https://pubmed.ncbi.nlm.nih.gov/22493484/)).

**Ca²⁺/cGMP–PKG and RYR2.** RYR2 upregulation contributes to cGMP/PKG-signaling-induced cone degeneration ([PMID: 32173907](https://pubmed.ncbi.nlm.nih.gov/32173907/)) and to impaired protein localization under ER Ca²⁺ dysregulation ([PMID: 31182474](https://pubmed.ncbi.nlm.nih.gov/31182474/)).

**Aberrant channel activity (related channelopathy insight).** An achromatopsia *CNGA3* mutation illustrates a complementary gain-of-function route to cone death: "CNGA3_R410W/CNGB3 and TAX4_R421W channels are spontaneously active without cGMP and induce cell death, suggesting cone degeneration triggered by spontaneous CNG channel activity as a possible cause of achromatopsia" ([PMID: 35233102](https://pubmed.ncbi.nlm.nih.gov/35233102/)). For *CNGB3* LOF, loss of conductance (not spontaneous activity) is the dominant mechanism.

**ER retrotranslocation as a modifiable node.** Overexpression of the E3 ubiquitin ligase **synoviolin-1 (SYVN1/HRD1)** promotes ER retrotranslocation, reduces ER stress, and preserves cones in CNG-channel deficiency ([PMID: 39215566](https://pubmed.ncbi.nlm.nih.gov/39215566/)) — nominating the UPR/ERAD axis as a neuroprotective target.

**Cell types & GO/CL terms.**
- Primary cell type: **cone photoreceptor cell** (CL:0000573); subtypes L/M/S cones.
- Biological processes: **detection of light stimulus involved in visual perception / phototransduction** (GO:0007602, GO:0050908); **cGMP-gated cation channel activity** (GO:0005223); **response to ER stress / UPR** (GO:0034976, GO:0030968); **apoptotic process** (GO:0006915).
- Chemical entities (CHEBI): cGMP (CHEBI:16356), Ca²⁺ (CHEBI:29108), Na⁺ (CHEBI:29101).

**Molecular profiling.** In *CNGB3⁻/⁻* mice, M-opsin, cone transducin, and cone arrestin were reduced 50–60% by 1 month and cone opsin mislocalized to the ONL/OPL ([PMID: 21273547](https://pubmed.ncbi.nlm.nih.gov/21273547/)) — a proteomic/trafficking signature of cone stress. No human transcriptomic/proteomic/metabolomic disease signatures were identified in this investigation.

---

## 7. Anatomical Structures Affected

**Organ level.** Primary organ: the **eye (retina)**; specifically the **neural retina** and the **fovea/macula** (cone-rich central retina). Secondary involvement: oculomotor system (nystagmus). Body system: **visual/nervous system** only. No systemic/extraocular involvement.

**Tissue & cell level.** Affected tissue: **photoreceptor layer of the neural retina** (nervous tissue). Targeted cells: **cone photoreceptors** (CL:0000573) — L, M, and S cones. **Rods are spared** (scotopic ERG preserved; [PMID: 21273547](https://pubmed.ncbi.nlm.nih.gov/21273547/), [PMID: 41867372](https://pubmed.ncbi.nlm.nih.gov/41867372/)).

**Subcellular level (GO cellular component).** Cone **outer segment / connecting cilium** plasma membrane (channel location; GO:0001750 photoreceptor outer segment); **endoplasmic reticulum** (GO:0005783) — site of UPR/ER stress; **plasma membrane** (GO:0005886). Opsin mislocalizes to the inner segment/outer nuclear layer in disease.

**Localization (UBERON).** Retina (UBERON:0000966); fovea centralis (UBERON:0001782); macula lutea (UBERON:0002776); photoreceptor layer / outer nuclear layer (UBERON:0001789). **Lateralization: bilateral and symmetric.**

---

## 8. Temporal Development

**Onset.** **Congenital** — cone dysfunction is present from birth. Symptoms (nystagmus, photophobia) are usually noticed within the **first months of life**; onset of initial symptom at a mean of ~0.88 ± 1.07 years in one preschool cohort (PMID: 40241905). Onset pattern is **chronic/insidious** rather than acute.

**Progression.** Historically classified as "stationary," but modern longitudinal data show **slow functional and structural progression**:
- Structurally relatively stable over months: in 41 CNGB3 patients imaged over 6–26 months, "Foveal cone structure showed little or no change in this group of subjects with CNGB3-associated achromatopsia" (EZ grade unchanged in 34/41) ([PMID: 28145975](https://pubmed.ncbi.nlm.nih.gov/28145975/)).
- Functionally slowly progressive over years: "ACHM is a progressive disease in terms of BCVA, MS and ERG responses, and affects slowly the structural integrity of the retina" — BCVA declined ~0.012 logMAR/year and macular sensitivity −0.16 dB/year ([PMID: 33562422](https://pubmed.ncbi.nlm.nih.gov/33562422/)).
- CNGA3 foveal cone mosaic declines ~2%/year, "a similar rate of change to CNGB3-associated ACHM (2% decline per year)" ([PMID: 39365261](https://pubmed.ncbi.nlm.nih.gov/39365261/)).

**Disease course.** Lifelong/chronic; non-remitting. There is **no spontaneous remission**.

**Critical period / therapeutic window.** Because cone structure is relatively preserved early and declines slowly, there is a **finite window** for cone-directed gene therapy, best defined by direct imaging of photoreceptor structure rather than age alone ([PMID: 28145975](https://pubmed.ncbi.nlm.nih.gov/28145975/)). This argues for early intervention in childhood.

---

## 9. Inheritance and Population

**Epidemiology.** Achromatopsia overall: **~1 in 30,000** ("Achromatopsia is the most common cone dysfunction syndrome, affecting 1 in 30,000 people"; [PMID: 39273686](https://pubmed.ncbi.nlm.nih.gov/39273686/)). CNGB3 accounts for ~45–50% of these ([PMID: 28795510](https://pubmed.ncbi.nlm.nih.gov/28795510/); [PMID: 15657609](https://pubmed.ncbi.nlm.nih.gov/15657609/)), implying a CNGB3-specific prevalence on the order of ~1 in 60,000.

**Inheritance.** **Autosomal recessive** (AD/X-linked/mitochondrial excluded). "It is an autosomal recessive disorder" ([PMID: 39273686](https://pubmed.ncbi.nlm.nih.gov/39273686/)).

**Penetrance / expressivity.** Essentially **complete penetrance** in biallelic individuals; expressivity ranges from complete to incomplete achromatopsia, largely allele-dependent.

**Genetic anticipation / mosaicism.** Not applicable (no repeat expansion); germline mosaicism not a recognized feature.

**Founder effect.** Strong — the c.1148delC / p.T383fs allele reflects a **common founder haplotype**: "intragenic SNPs in unrelated patients revealed transmission of a common haplotype consistent with a founder effect" ([PMID: 17265047](https://pubmed.ncbi.nlm.nih.gov/17265047/)).

**Consanguinity.** Elevates recessive-homozygote risk; documented in consanguineous cohorts ([PMID: 42099125](https://pubmed.ncbi.nlm.nih.gov/42099125/)).

**Carrier frequency.** Consistent with ~1/30,000 ACHM and CNGB3's ~50% share, the population carrier frequency for CNGB3 pathogenic alleles is roughly on the order of ~1/120–1/170 (derived from Hardy-Weinberg; exact gnomAD figure not re-derived here).

**Population demographics.** Occurs worldwide. The c.1148delC founder allele is especially common in populations of European descent. Specific founder mutations underlie high local prevalence in some isolated/consanguineous populations. **Sex ratio ~1:1** (autosomal). Age distribution: present from birth, all ages affected.

---

## 10. Diagnostics

**Electrophysiology — the key functional test.** Full-field ERG shows **absent/severely reduced photopic (cone) and 30-Hz flicker responses with preserved scotopic (rod) responses** — the diagnostic signature ([PMID: 41867372](https://pubmed.ncbi.nlm.nih.gov/41867372/)). Specialized cycle-by-cycle ERG methods can validate very low-amplitude cone responses in advanced disease (PMID: 38558093).

**Imaging.** **Spectral-domain OCT (SD-OCT)** grades foveal structure on a 5-point scale (continuous ellipsoid zone → EZ disruption → EZ absence → hyporeflective zone → outer retinal atrophy) and detects foveal hypoplasia (PMID: 24148654). **Adaptive optics scanning light ophthalmoscopy (AOSLO)** directly images the cone mosaic / peak cone density (PMID: 39365261, PMID: 28145975). **Fundus autofluorescence (FAF)** and infrared imaging reveal foveal/parafoveal abnormalities. Handheld SD-OCT enables assessment in preverbal children (PMID: 24676353).

**Color vision & psychophysics.** Color vision testing (e.g., Berson plates, anomaloscope) confirms severe/complete color deficiency; photoaversion testing documents photophobia.

**Genetic testing — definitive.** Molecular confirmation is essential for diagnosis, prognosis, and gene-therapy eligibility. Recommended approach:
- **Targeted ACHM gene panel / NGS panel** covering the six ACHM genes (**CNGA3, CNGB3, GNAT2, PDE6C, PDE6H, ATF6**) is first-line; panels detect SNVs and CNVs.
- **Single-variant / single-gene testing** is efficient given the common c.1148delC founder allele (test for it first in appropriate populations).
- **Whole-exome sequencing (WES)** is useful for panel-negative cases; periodic reanalysis increases yield (PMID: 39189993).
- **Chromosomal microarray / MLPA** for suspected large CNGB3 deletions.
- Electrophysiology-guided genetic testing maximizes molecular diagnosis in pediatric IRD (PMID: 35456422).

**Differential diagnosis.** Blue cone monochromatism (X-linked, *OPN1LW/OPN1MW*; better acuity, myopia, preserved S-cones — PMID: 40736816); other ACHM subtypes (CNGA3, GNAT2, PDE6C, ATF6 — ATF6 shows near-absent foveal cones, PMID: 31237654; PDE6C often with myopia and progressive maculopathy, PMID: 31826238); cone/cone-rod dystrophy; Leber congenital amaurosis; oculocutaneous albinism and other causes of infantile nystagmus / foveal hypoplasia (PMID: 35157951, PMID: 40232708).

**Screening.** Carrier screening (especially for the c.1148delC founder allele), cascade testing of relatives, and prenatal/preimplantation genetic testing are available for known-mutation families. Achromatopsia is not part of standard newborn metabolic screening but is often identified during work-up of infantile nystagmus.

---

## 11. Outcome / Prognosis

**Survival / mortality.** Achromatopsia is **not life-limiting**; life expectancy is **normal**. No disease-specific mortality.

**Morbidity / function.** Lifelong **visual disability**: best-corrected acuity typically ~20/200, disabling photophobia, inability to drive, dependence on low-vision aids, and impacts on education and daily functioning. Visual disability is stable to slowly worsening.

**Disease course / complications.** No systemic complications. The main "complication" is slow progressive cone loss (BCVA ~0.012 logMAR/year; [PMID: 33562422](https://pubmed.ncbi.nlm.nih.gov/33562422/)) which gradually erodes the cone substrate available for future therapy.

**Recovery potential.** Without treatment, the deficit is permanent. Gene therapy aims to restore/preserve cone function but has not yet shown consistent clinical efficacy (see Treatment).

**Prognostic factors.** Residual cone structure (EZ integrity, peak cone density on OCT/AOSLO) is a better predictor of therapeutic potential than age ([PMID: 28145975](https://pubmed.ncbi.nlm.nih.gov/28145975/)). Earlier intervention, before cone loss, is expected to yield better outcomes. Genotype alone does not reliably predict photoreceptor preservation (PMID: 24676353).

---

## 12. Treatment

### Current standard: supportive care
- **Tinted / red or magenta filter contact lenses or spectacles** to reduce photophobia and improve contrast (NCIT: tinted lens / optical device).
- **Refractive correction** and **low-vision aids** (magnifiers, high-contrast materials).
- **Dark / cutoff sunglasses** outdoors.
- **Genetic counseling** for families (recessive inheritance, carrier testing).

### Advanced therapeutics — gene therapy (experimental, lead approach)

**Rationale.** Because CNGB3 ACHM is a monogenic loss-of-function disease with a slow-degenerating, accessible target (cones), **AAV-mediated CNGB3 gene replacement** is the primary therapeutic strategy. "Up to 80% of the patients carry mutations in the genes CNGA3 and CNGB3... a number of promising gene supplementation therapy programs have been initiated" (PMID: 28095637).

**First-in-human trial (NCT03001310).** Subretinal **AAV8-hCARp.hCNGB3** in 23 CNGB3-ACHM patients (11 adults, 12 children): "AAV8-hCARp.hCNGB3 (11 adults, 12 children) was safe and generally well tolerated. Intraocular inflammation occurred in 9 of 23 participants" (mostly mild/moderate, two serious dose-limiting events); but "There was no consistent pattern of change from baseline to week 24 for any efficacy assessment" ([PMID: 37172884](https://pubmed.ncbi.nlm.nih.gov/37172884/)). Individual improvements were seen in color vision (6/23), photoaversion (11/20), and QoL (21/23).

**Preclinical support.**
- **Canine model:** AAV5 expressing human or canine CNGB3 under a cone-opsin promoter "rescued cone photoreceptor function, but at high doses was associated with an inflammatory response (focal chorioretinitis) consistent with immune-mediated toxicity" ([PMID: 29020838](https://pubmed.ncbi.nlm.nih.gov/29020838/)).
- **Mouse model:** *Cngb3⁻/⁻* mice recapitulate early-onset, slowly progressive cone dysfunction, providing a platform for therapy ([PMID: 21273547](https://pubmed.ncbi.nlm.nih.gov/21273547/)).

### Neuroprotective / adjunct strategies (preclinical)
- **ER-stress modulation:** SYVN1/synoviolin-1 overexpression reduces ER stress and preserves cones ([PMID: 39215566](https://pubmed.ncbi.nlm.nih.gov/39215566/)) — a candidate adjunct to prolong the treatment window.
- **Targeting cGMP/PKG–RYR2 signaling** is a proposed route to slow degeneration (PMID: 32173907, PMID: 31182474).

### Not applicable
No approved pharmacotherapy, no pharmacogenomics, no surgical / immunotherapy / cell-therapy options are established. No disease-specific drug exists.

---

## 13. Prevention

- **Primary prevention:** Not possible (congenital genetic disease). Prevention is reproductive/genetic: **genetic counseling**, **carrier screening** (particularly for the c.1148delC founder allele), **cascade testing**, and reproductive options including **preimplantation genetic testing (PGT)** and **prenatal diagnosis** for known-mutation families.
- **Secondary prevention:** Early diagnosis via infantile-nystagmus work-up (ERG + genetic testing) enables early low-vision support and candidacy for emerging gene therapy.
- **Tertiary prevention:** Photoprotection (tinted lenses) to maximize residual function and comfort; low-vision rehabilitation; educational accommodations.
- **Immunization / public health / environmental interventions:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Dog (*Canis lupus familiaris*, NCBI Taxon 9615):** Naturally occurring **CNGB3 achromatopsia / "canine day blindness"** (e.g., Alaskan Malamute, German Shorthaired Pointer) is a validated large-animal model; AAV-CNGB3 rescues cone function ([PMID: 29020838](https://pubmed.ncbi.nlm.nih.gov/29020838/)). Orthologous gene: canine *CNGB3*.
- **Mouse (*Mus musculus*, NCBI Taxon 10090):** *Cngb3* knockout recapitulates the disease ([PMID: 21273547](https://pubmed.ncbi.nlm.nih.gov/21273547/)); ortholog *Cngb3* (MGI).
- **Comparative biology:** The cone CNG channel and phototransduction cascade are evolutionarily conserved across vertebrates, so disease mechanisms translate well between dog, mouse, and human.
- **Transmission / zoonosis:** Not applicable (genetic, non-transmissible).

---

## 15. Model Organisms

| Model | Type | Genetic design | Phenotype recapitulation | Key reference |
|---|---|---|---|---|
| *Cngb3⁻/⁻* mouse | Mammalian, in vivo | Knockout | Early-onset, slowly progressive cone dysfunction; cone ERG ~50% WT by P15 → ~20% by 12 mo; cone density ~80%→~50%; opsin mislocalization; **rods spared** | [PMID: 21273547](https://pubmed.ncbi.nlm.nih.gov/21273547/) |
| *Cng*⁻/⁻;*Nrl*⁻/⁻ cone-dominant mouse | Mammalian, in vivo | Compound KO (cone-enriched retina) | ER-stress/UPR-associated cone apoptosis (↑Grp78/BiP, ↑CHOP, caspase-12/-7 cleavage) | [PMID: 22493484](https://pubmed.ncbi.nlm.nih.gov/22493484/) |
| CNGB3-mutant dog (day blindness) | Mammalian, large animal, natural | Naturally occurring CNGB3 mutation | Cone dysfunction; AAV-CNGB3 rescues cone function; proof-of-concept for human gene therapy | [PMID: 29020838](https://pubmed.ncbi.nlm.nih.gov/29020838/) |
| Heterologous channel expression (e.g., Xenopus oocytes / HEK) | In vitro | Mutant CNG channel expression | Mechanistic dissection of channel gating/activity (e.g., spontaneous activity of CNGA3 R410W) | [PMID: 35233102](https://pubmed.ncbi.nlm.nih.gov/35233102/) |

**Mouse strengths:** faithful cone-functional phenotype and rod sparing; tractable for gene therapy and neuroprotection studies.
**Mouse limitations:** rod-dominant retina (no macula/fovea), so the human foveal-cone and nystagmus phenotypes are not reproduced; the cone-dominant *Nrl⁻/⁻* cross partly addresses cone density.
**Dog strengths:** cone-rich *area centralis*, eye size comparable to human, enabling subretinal AAV delivery testing and dose/toxicity assessment.
**Resources:** MGI (mouse *Cngb3*); canine models via academic colonies; Alliance of Genome Resources for orthology.

---

## Mechanistic Model / Interpretation

```
 Biallelic CNGB3 LOF (e.g., c.1148delC, p.Thr383fs)
                │
                ▼
 Absent/non-functional CNGB3 β-subunit
                │
                ▼
 Defective cone CNG channel (3×CNGA3 + 1×CNGB3)
                │
        ┌───────┴───────────────────────────────┐
        ▼                                         ▼
 Loss of light-regulated                 Disturbed Ca²⁺ / cGMP–PKG
 cation conductance                       homeostasis; RYR2 ↑
        │                                         │
        ▼                                         ▼
 LOSS OF CONE PHOTOTRANSDUCTION            ER Ca²⁺ dysregulation +
        │                                  protein mislocalization
        ▼                                         │
 Immediate clinical phenotype                     ▼
 • absent photopic ERG                     ER stress / UPR
 • color-vision loss                       (↑BiP, ↑CHOP, p-eIF2α)
 • ↓acuity (~20/200)                              │
 • photophobia                                    ▼
 • infantile nystagmus                     calpain ↑, caspase-12/-7
 (RODS SPARED → scotopic ERG normal)              │
                                                  ▼
                                         ER-stress cone APOPTOSIS
                                                  │
                                                  ▼
                                      Slow progressive cone loss
                                      → narrowing therapeutic window
```

**Upstream vs downstream.** Upstream: CNGB3 LOF → non-functional channel (defines the disease and the immediate, largely non-progressive functional deficit). Downstream: Ca²⁺/cGMP dysregulation → ER stress → apoptosis (drives the slow degenerative, progressive component). Therapeutically, **gene replacement targets the upstream lesion**, while **ER-stress/UPR modulation (e.g., SYVN1) targets the downstream degeneration** to widen the treatment window.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [28795510](https://pubmed.ncbi.nlm.nih.gov/28795510/) | CNGB3 mutation spectrum incl. CNVs, 552 patients | Human cohort | CNGB3 = major ACHM gene; 45.2% of 1074 families; β-subunit |
| [15657609](https://pubmed.ncbi.nlm.nih.gov/15657609/) | CNGB3 accounts for 50% of AR achromatopsia | Human cohort | ~50% of ACHM; c.1148delC >70% of alleles |
| [17265047](https://pubmed.ncbi.nlm.nih.gov/17265047/) | p.T383fsX founder effect | Human genetics | Founder allele, 75% of disease alleles, shared haplotype |
| [37172884](https://pubmed.ncbi.nlm.nih.gov/37172884/) | First-in-human AAV8-hCNGB3 (NCT03001310) | Human trial | Safe; no consistent efficacy at wk 24 |
| [35233102](https://pubmed.ncbi.nlm.nih.gov/35233102/) | ACHM channel mutation structure/function | In vitro | Aberrant channel activity → cone death |
| [41867372](https://pubmed.ncbi.nlm.nih.gov/41867372/) | ACHM genotype/phenotype cohort | Human cohort | Phenotype frequencies; ERG pattern |
| [39273686](https://pubmed.ncbi.nlm.nih.gov/39273686/) | Gene Therapy for Achromatopsia | Review | Prevalence 1/30,000; AR |
| [28145975](https://pubmed.ncbi.nlm.nih.gov/28145975/) | Longitudinal foveal cone structure CNGB3 | Human imaging | Structural stability over months |
| [33562422](https://pubmed.ncbi.nlm.nih.gov/33562422/) | Longitudinal ACHM study | Human cohort | Slow functional progression over years |
| [39365261](https://pubmed.ncbi.nlm.nih.gov/39365261/) | Foveal cone mosaic CNGA3 | Human imaging | ~2%/yr cone decline, like CNGB3 |
| [29020838](https://pubmed.ncbi.nlm.nih.gov/29020838/) | AAV5-CNGB3 in CNGB3-mutant dogs | Animal model | Functional rescue; dose-dependent toxicity |
| [21273547](https://pubmed.ncbi.nlm.nih.gov/21273547/) | Cngb3⁻/⁻ mouse | Animal model | Early-onset slow cone decline; rods spared |
| [22493484](https://pubmed.ncbi.nlm.nih.gov/22493484/) | ER stress in CNG-channel deficiency | Animal/in vitro | ER-stress-associated cone apoptosis; >70% ACHM from CNGA3/CNGB3 |
| [32173907](https://pubmed.ncbi.nlm.nih.gov/32173907/) | RYR2 in cGMP/PKG cone degeneration | Animal/in vitro | Ca²⁺/cGMP–PKG downstream mechanism |
| [31182474](https://pubmed.ncbi.nlm.nih.gov/31182474/) | RYR2 & protein mislocalization | Animal/in vitro | ER Ca²⁺ dysregulation |
| [39215566](https://pubmed.ncbi.nlm.nih.gov/39215566/) | SYVN1 overexpression preserves cones | Animal/in vitro | ER-stress modulation as neuroprotection |

---

## Limitations and Knowledge Gaps

1. **No consistent human efficacy for gene therapy.** The first-in-human AAV8-hCNGB3 trial showed safety but no consistent efficacy at 6 months ([PMID: 37172884](https://pubmed.ncbi.nlm.nih.gov/37172884/)). Whether longer follow-up, different vectors/promoters/doses, younger patients, or cortical plasticity limits explain the result remains unresolved.
2. **Progression rate uncertainty.** Different modalities (OCT grade vs. BCVA vs. AOSLO cone density) give different pictures; precise CNGB3-specific decline rates and the optimal intervention window need larger natural-history cohorts.
3. **Downstream mechanism quantification in humans.** The Ca²⁺/cGMP–PKG → ER-stress → apoptosis cascade is established mainly in mouse/in-vitro cone-dominant models; its quantitative contribution in human CNGB3 retina is inferred.
4. **No human omics signatures.** Transcriptomic/proteomic/metabolomic disease signatures for human CNGB3 retina were not identified.
5. **Model limitations.** Mice lack a fovea (the key human phenotype locus); the human nystagmus and foveal-hypoplasia phenotypes are not fully recapitulated.
6. **Population genetics detail.** Exact gnomAD allele/carrier frequencies for c.1148delC were not re-derived in this investigation.

---

## Proposed Follow-up Experiments / Actions

1. **Refine the therapeutic window:** Prospective multi-year natural-history study combining AOSLO cone density, OCT EZ grading, BCVA, and chromatic psychophysics specifically in genotyped CNGB3 patients to define intervention cutoffs.
2. **Next-generation gene therapy:** Test improved cone-specific promoters, optimized AAV capsids/doses, and intervention in young children; incorporate perioperative immunosuppression informed by the canine chorioretinitis finding ([PMID: 29020838](https://pubmed.ncbi.nlm.nih.gov/29020838/)).
3. **Combine replacement with neuroprotection:** Preclinically test AAV-CNGB3 plus ER-stress modulation (SYVN1/UPR-targeting) to preserve cones and widen the window ([PMID: 39215566](https://pubmed.ncbi.nlm.nih.gov/39215566/)).
4. **Address cortical plasticity:** Pair gene therapy with structured visual training/rehabilitation to help a lifelong-deprived cone pathway "learn" to use restored signals.
5. **Human molecular profiling:** Apply single-cell/snRNA-seq and proteomics to patient-derived retinal organoids/iPSC-cones to map the human ER-stress signature and nominate adjunct drug targets.
6. **Carrier-screening and founder-allele programs:** Deploy targeted c.1148delC screening in high-frequency populations to support counseling and reproductive options.

---

*Evidence source legend:* Human clinical (cohort/trial/imaging), model organism (mouse/dog), in vitro (heterologous channel expression, retinal explant/organoid), and computational/review sources are distinguished in the Evidence Base table.


## Artifacts

- [OpenScientist final report](CNGB3-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](CNGB3-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 17 |
| Quoted claims found in source | 17 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 31 |
| On topic | 30 |
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
| Terms whose name was checked | 10 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0100446` (2 mentions) - the report calls it "OMIM #262300", "MONDO"; MONDO calls it **CNGB3-related retinopathy**
- `CL:0000573` (2 mentions) - the report calls it "cone photoreceptor cell", "Primary cell type: **cone photoreceptor cell", "cone photoreceptors"; CL calls it **retinal cone cell**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0007750` (1 mention) - the report calls it "Foveal hypoplasia"; HP calls it **Hypoplasia of the fovea**, and lists "Foveal hypoplasia" among its other names
- `GO:0005223` (1 mention) - the report calls it "cGMP-gated cation channel activity"; GO calls it **intracellularly cGMP-activated cation channel activity**, and lists "intracellular cGMP activated cation channel activity" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0100446` - called "OMIM #262300", "MONDO"
- `CL:0000573` - called "cone photoreceptor cell", "Primary cell type: **cone photoreceptor cell", "cone photoreceptors"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.