---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-14T22:31:48.566892'
end_time: '2026-11-14T22:42:28.582626'
duration_seconds: 640.02
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Necatoriasis
  mondo_id: MONDO:0005870
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: Necator americanus hookworm infection
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    save_artifacts: true
    artifact_max_bytes: 5242880
    artifact_keep_runtime: false
    artifact_extra_extensions: []
    artifact_include_globs: []
    artifact_exclude_globs: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
run_metadata:
  job_id: afeffeb7-7b66-4078-a30b-2a9d9d3d3dcf
citation_count: 12
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 9
  validator_version: 0.5.1
term_validation:
  total_terms: 32
  verified: 29
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 12
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: GO:0042493
    reported_labels:
    - response to drug
    ontology_label: GO_0042493
  - term_id: CL:0000584
    reported_labels:
    - "enterocyte \u2014 mucosal surface the worm feeds on"
    - Tissue/cell level:** Intestinal epithelium/enterocytes
    ontology_label: enterocyte
  - term_id: NCIT:C29257
    reported_labels:
    - Mebendazole
    ontology_label: Miconazole Nitrate
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0042493
    ontology_label: GO_0042493
    replaced_by: GO:0009410
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
  path: Necatoriasis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Necatoriasis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Necatoriasis
- **MONDO ID:** MONDO:0005870 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** Necator americanus hookworm infection
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Necatoriasis** covering all of the
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

# Necatoriasis (MONDO:0005870): A Comprehensive Disease Characteristics Report

## Summary

**Necatoriasis is an infectious soil-transmitted helminthiasis caused by the blood-feeding nematode *Necator americanus*, not a genetic human disorder.** The research template lists "causal gene(s): not recorded," and this is correct and expected: necatoriasis has **no human causal gene**. It is a parasitic infection, and its molecular drivers are the *parasite's own* genes/proteins — most notably the blood-digestion enzymes *Na*-APR-1 (an aspartic protease) and *Na*-GST-1 (a glutathione S-transferase), which are also the leading human hookworm vaccine antigens. Any attempt to map this disease to a Mendelian human gene (as the template warns for serially named genetic disorders) would be a category error. The causal agent is the organism *Necator americanus* (NCBI Taxon:51031), the predominant human hookworm species worldwide.

The disease mechanism is mechanically and nutritionally simple but globally devastating. Infective third-stage (L3) larvae living in warm, moist soil penetrate intact human skin (usually the feet), migrate via the bloodstream to the lungs, ascend the airway, are swallowed, and mature into adult worms that attach to the small-intestinal mucosa. There they feed on host blood for many years, aided by a host immune response that is largely ineffective and switches to an immune-tolerant state. The net result is chronic intestinal blood loss producing **iron-deficiency anemia** and **hypoproteinemia**, with the heaviest burden in children and women of childbearing age. Globally, hookworm (of which *N. americanus* is the dominant species) infects an estimated **406–480 million people** and causes roughly **4 million disability-adjusted life years (DALYs)** annually, concentrated among the poor in tropical and subtropical regions with inadequate sanitation.

Clinically, necatoriasis is diagnosed by stool microscopy (Kato-Katz) or, more sensitively, qPCR, and treated effectively with single-dose **albendazole** (cure rates ~72–96%, superior to mebendazole) alongside iron supplementation. Because anthelmintics do not prevent reinfection, control depends on mass drug administration (MDA/preventive chemotherapy), improvements in water, sanitation and hygiene (WASH), and an investigational recombinant vaccine (*Na*-GST-1 + *Na*-APR-1[M74] on Alhydrogel) — currently the only human soil-transmitted helminth vaccine in clinical trials. This report synthesizes four confirmed findings and 14 reviewed papers across all 15 requested template sections, flagging where information reflects the infectious (rather than genetic) nature of the disease.

---

## Key Findings

### Finding 1 — Necatoriasis is caused by the blood-feeding nematode *Necator americanus*; no human "causal gene" applies

Necatoriasis is defined by infection with *Necator americanus*, a soil-transmitted hookworm nematode. As the landmark review *Hookworm infection* states: *"Hookworms are soil-transmitted nematode parasites that can reside for many years in the small intestine of their human hosts; Necator americanus is the predominant infecting species. Adult worms feed on the blood of a host and can cause iron deficiency anaemia, especially in high-risk populations (children and women of childbearing age). Almost 500 million people in developing tropical countries are infected"* ([PMID: 27929101](https://pubmed.ncbi.nlm.nih.gov/27929101/)).

This establishes the three defining features of the disease: (1) the etiologic agent is a parasite, not a mutation; (2) the primary pathology is iron-deficiency anemia from blood feeding; and (3) the burden is enormous and concentrated in poor tropical populations. The "causal gene" field in the research template is therefore **not applicable** — the appropriate identifier is the organism (NCBI Taxon:51031, *Necator americanus*), and the relevant molecular players are parasite genes, not human disease alleles. Host genetic susceptibility to hookworm (e.g., quantitative trait loci affecting worm burden) exists in the literature as a modifier of intensity but is not a causal determinant of whether the disease exists.

### Finding 2 — Core pathophysiology: intestinal blood loss from adult-worm feeding → iron-deficiency anemia and hypoproteinemia

Adult *N. americanus* worms attach to the small-intestinal mucosa and ingest blood. Each worm causes approximately **0.03–0.05 mL of host blood loss per day** (a widely cited literature value), so worm burden scales directly with anemia severity. Critically, the host immune response fails to clear the worms. As the review notes: *"Humans mount an immune response to hookworms, but it is mostly unsuccessful at removing adult worms from the bowel. Accordingly, the host switches to an immune-tolerant state that enables hookworms to reside in the gut for many years"* ([PMID: 27929101](https://pubmed.ncbi.nlm.nih.gov/27929101/)). This immune tolerance is the mechanistic basis for the chronicity — worms persist for years, producing cumulative blood and iron loss.

At the molecular level, the worm's blood-digestion machinery is the engine of the pathology. *"Necator americanus aspartic protease-1 (Na-APR-1) and N americanus glutathione S-transferase-1 (Na-GST-1) are involved in the digestion and detoxification of haemoglobin in the hookworm digestive tract"* ([PMID: 32926834](https://pubmed.ncbi.nlm.nih.gov/32926834/)). *Na*-APR-1 cleaves host hemoglobin; *Na*-GST-1 helps detoxify the heme released during that digestion. These enzymes are simultaneously the mechanism of host harm and the rational targets for a feeding/pathology-blocking vaccine (see Finding 3).

### Finding 3 — Treatment: single-dose albendazole is effective (~72–96% cure); mebendazole less so; MDA is the mainstay but reinfection is common

Benzimidazole anthelmintics are the backbone of treatment and control. A systematic review of maternal outcomes found: *"Gestational treatment with albendazole had cure rates up to 90% for hookworm and Ascaris, but only 50% for Trichuris. Mebendazole had an overall cure rate of ≤ 70% for Ascaris, hookworm and Trichuris"* ([PMID: 31641774](https://pubmed.ncbi.nlm.nih.gov/31641774/)). An earlier landmark meta-analysis quantified single-dose efficacy against hookworm specifically: albendazole 72% cure (95% CI 59–81%), mebendazole only 15% (95% CI 1–27%), and pyrantel pamoate 31% (95% CI 19–42%) ([PMID: 18430913](https://pubmed.ncbi.nlm.nih.gov/18430913/)). A 2024 meta-analysis reported albendazole egg-reduction rates of 93.4% against hookworm versus poor mebendazole performance ([PMID: 38696109](https://pubmed.ncbi.nlm.nih.gov/38696109/)). **Albendazole is clearly the drug of choice for hookworm.**

Drugs do not prevent reinfection: *"Although anthelmintic drugs are available and widely used, their efficacy varies and the drugs do not prevent reinfection. Thus, other control strategies aimed at improving water quality, sanitation and hygiene are needed"* ([PMID: 27929101](https://pubmed.ncbi.nlm.nih.gov/27929101/)). This limitation motivates the vaccine program. The bivalent recombinant vaccine targeting the blood-digestion pathway is advancing: *"only the hookworm vaccine against N. americanus is in the clinical trial"* among STH vaccines ([PMID: 36586174](https://pubmed.ncbi.nlm.nih.gov/36586174/)), with phase 1 dose-escalation trials completed in Gabonese adults ([PMID: 32926834](https://pubmed.ncbi.nlm.nih.gov/32926834/)) and school-aged children ([PMID: 38513684](https://pubmed.ncbi.nlm.nih.gov/38513684/)).

### Finding 4 — Epidemiology and risk: 406–480 million infected; poverty and poor sanitation are the dominant risk factors

Hookworm is the most impactful human STH by disease burden: *"Hookworm infections are classified as the most impactful of the human soil-transmitted helminth (STH) infections, causing a disease burden of ∼4 million disability-adjusted life years, with a global prevalence of 406-480 million infections"* ([PMID: 32342850](https://pubmed.ncbi.nlm.nih.gov/32342850/)). Risk is fundamentally a function of poverty and inadequate sanitation. A Solomon Islands qPCR survey found *N. americanus* prevalence of 54.5% and identified a strong protective effect of sanitation: *"Owning a household latrine was associated with a lower risk of N. americanus infection (AOR 0.41, 95% CI 0.24-0.68)"* ([PMID: 35604904](https://pubmed.ncbi.nlm.nih.gov/35604904/)). In rural Kenya, individuals in the lowest socio-economic households were at greatest risk of hookworm infection ([PMID: 30814567](https://pubmed.ncbi.nlm.nih.gov/30814567/)). Most infections are of light intensity (~85.7%), but even light chronic infection contributes to iron depletion in nutritionally vulnerable people.

---

## Report by Template Section

### 1. Disease Information

**Overview.** Necatoriasis is a chronic intestinal helminthiasis caused by the hookworm *Necator americanus*. It is one of the "neglected tropical diseases" and the dominant cause of human hookworm disease worldwide (the other agent, *Ancylostoma duodenale*, is more regionally restricted). The clinical hallmark is iron-deficiency anemia from chronic intestinal blood loss.

**Key identifiers.**
| Resource | Identifier |
|---|---|
| MONDO | MONDO:0005870 (necatoriasis) |
| MeSH | Necatoriasis (D009391); Hookworm Infections (D006725) |
| ICD-10 | B76.1 (Necatoriasis); B76.9 (Hookworm disease, unspecified) |
| ICD-11 | 1F6A.1 (Necatoriasis) / 1F6A (Hookworm disease) |
| NCBI Taxonomy (agent) | *Necator americanus*, Taxon:51031 |
| Orphanet | Not a rare disease — common NTD; limited Orphanet entry |
| OMIM | Not applicable (not a Mendelian human disorder) |

**Synonyms:** *Necator americanus* hookworm infection; New World hookworm infection; American hookworm disease; necatoriosis. "Hookworm disease" and "ancylostomiasis" are related but broader/distinct (ancylostomiasis refers to *Ancylostoma* infection).

**Data source nature:** Information is derived from **aggregated disease-level resources** — epidemiological surveys, systematic reviews/meta-analyses, clinical trials, and parasitology reviews — rather than individual patient EHR records.

### 2. Etiology

**Primary cause (infectious).** Infection with *Necator americanus*. Transmission is percutaneous: infective filariform (L3) larvae in soil penetrate skin (classically the feet of barefoot individuals). This contrasts with *Ascaris* and *Trichuris*, which are acquired by fecal-oral ingestion.

**Risk factors (environmental/behavioral — the operative category here):**
- **Poverty / low socio-economic position** — strongest determinant ([PMID: 30814567](https://pubmed.ncbi.nlm.nih.gov/30814567/)).
- **Lack of sanitation infrastructure** — absence of latrines; open defecation contaminating soil ([PMID: 35604904](https://pubmed.ncbi.nlm.nih.gov/35604904/)).
- **Walking barefoot / skin contact with contaminated soil.**
- **Warm, moist tropical/subtropical climate** favoring larval survival.
- **Agricultural occupation** and rural residence.
- **Age/sex:** children and women of childbearing age bear disproportionate anemia burden due to higher baseline iron demands ([PMID: 27929101](https://pubmed.ncbi.nlm.nih.gov/27929101/)).

**Genetic risk factors (host):** Not causal. Host genetic variation may modify worm-burden intensity (heritability of hookworm intensity is reported in family studies), but no pathogenic human variant causes the disease. **Not applicable as a Mendelian determinant.**

**Protective factors:** Latrine ownership (AOR 0.41) ([PMID: 35604904](https://pubmed.ncbi.nlm.nih.gov/35604904/)); footwear; improved WASH; higher socio-economic position; preventive chemotherapy (MDA). No established human genetic protective allele.

**Gene–environment interactions:** Not applicable in the Mendelian sense. The relevant interaction is parasite–host–environment: soil contamination (environment) + skin exposure (behavior) + nutritional status (host iron reserves) jointly determine clinical severity.

### 3. Phenotypes

| Phenotype | Type | HPO suggestion | Onset / course | Frequency |
|---|---|---|---|---|
| Iron-deficiency anemia | Lab abnormality / clinical sign | HP:0001891 (Iron deficiency anemia); HP:0001903 (Anemia) | Chronic, insidious; progressive with worm burden | Core feature in moderate–heavy infection |
| Hypoproteinemia / hypoalbuminemia | Lab abnormality | HP:0003075 (Hypoproteinemia); HP:0003073 (Hypoalbuminemia) | Chronic | Heavy infection |
| "Ground itch" (cutaneous larval entry) | Symptom/sign (skin) | HP:0000989 (Pruritus); HP:0000988 (Skin rash) | Acute, at site of larval penetration | At exposure |
| Pulmonary symptoms (cough, Löffler-like) during larval migration | Symptom | HP:0012735 (Cough) | Acute, transient, ~1 week post-infection | Variable |
| Abdominal pain / epigastric discomfort | Symptom | HP:0002027 (Abdominal pain) | Subacute–chronic | Common |
| Diarrhea | Symptom | HP:0002014 (Diarrhea) | Variable | Common |
| Fatigue / weakness | Symptom | HP:0012378 (Fatigue) | Chronic (anemia-driven) | Common when anemic |
| Growth stunting / impaired cognition (children) | Developmental | HP:0001510 (Growth delay) | Childhood, chronic | Heavy chronic infection |
| Eosinophilia | Lab abnormality | HP:0001880 (Eosinophilia) | Subacute–chronic | Frequent |

**Severity/progression:** Largely proportional to worm burden and host iron reserves; ranges from asymptomatic light infection to severe anemia, protein-losing enteropathy, and (historically) anasarca/edema in heavy pediatric infection. Most infections are light-intensity (~85.7%).

**Quality-of-life impact:** Chronic anemia causes fatigue, reduced work capacity, impaired child development and school performance; in pregnancy it worsens maternal anemia and adverse birth outcomes. The disease is a quantified contributor to the ~4 million DALYs attributed to hookworm ([PMID: 32342850](https://pubmed.ncbi.nlm.nih.gov/32342850/)).

### 4. Genetic/Molecular Information

**Causal human genes:** **None — not applicable.** Necatoriasis is not a hereditary disorder; there is no OMIM gene entry, no pathogenic variant, no inheritance pattern, no modifier-gene map for the disease itself.

**Relevant parasite molecules (the actual molecular drivers):**
- ***Na*-APR-1** — *N. americanus* aspartic protease-1; cleaves host hemoglobin in the worm gut. Vaccine antigen used in catalytically inactivated form *Na*-APR-1[M74] ([PMID: 32926834](https://pubmed.ncbi.nlm.nih.gov/32926834/), [PMID: 38513684](https://pubmed.ncbi.nlm.nih.gov/38513684/)).
- ***Na*-GST-1** — *N. americanus* glutathione S-transferase-1; heme detoxification during blood digestion; lead vaccine antigen ([PMID: 32926834](https://pubmed.ncbi.nlm.nih.gov/32926834/)).
- Other hookworm molecules of interest (from the broader literature): anticoagulant peptides, tissue-migration metalloproteases/hyaluronidases, and acetylcholinesterases — not individually verified within this investigation.

**Epigenetics / chromosomal abnormalities (human):** Not applicable.

### 5. Environmental Information

- **Environmental factors:** Fecally contaminated warm, moist, shaded soil is the reservoir for infective L3 larvae. Open defecation, absence of latrines, and inadequate sewage drive soil contamination ([PMID: 35604904](https://pubmed.ncbi.nlm.nih.gov/35604904/)).
- **Lifestyle factors:** Barefoot walking, subsistence agriculture, poor hygiene, and poverty ([PMID: 30814567](https://pubmed.ncbi.nlm.nih.gov/30814567/)).
- **Infectious agent:** *Necator americanus* (Phylum Nematoda, Order Strongylida, Family Ancylostomatidae), NCBI Taxon:51031. The predominant human hookworm species globally ([PMID: 27929101](https://pubmed.ncbi.nlm.nih.gov/27929101/)).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating event → clinical manifestation):**

1. Infective L3 larvae in contaminated soil **contact and penetrate** intact human skin (usually feet) → local cutaneous inflammation ("ground itch"). *(Demonstrated.)*
2. Larvae **enter dermal blood/lymphatic vessels** and are carried to the **lungs**, breaking into alveoli → transient pulmonary inflammation (cough, Löffler-like syndrome). *(Demonstrated.)*
3. Larvae **ascend the bronchial tree, are swallowed**, and reach the **small intestine**, where they mature into adult worms. *(Demonstrated.)*
4. Adult worms **attach to the small-intestinal mucosa** and ingest blood; secreted anticoagulants keep attachment sites bleeding. *(Demonstrated.)*
5. Worm-gut enzymes ***Na*-APR-1 digest hemoglobin** and ***Na*-GST-1 detoxify liberated heme**, enabling the worm to use host blood as food ([PMID: 32926834](https://pubmed.ncbi.nlm.nih.gov/32926834/)). *(Demonstrated at the molecular level.)*
6. Host mounts an immune response but it **fails to clear adult worms**; host **switches to an immune-tolerant state** → worms persist for years ([PMID: 27929101](https://pubmed.ncbi.nlm.nih.gov/27929101/)). *(Demonstrated.)*
7. **Chronic intestinal blood loss** (~0.03–0.05 mL/worm/day) **leads to** depletion of body iron stores → **iron-deficiency anemia**; concurrent protein loss **leads to** hypoproteinemia/hypoalbuminemia. *(Demonstrated/quantified.)*
   - **Branch A:** In children → impaired growth, cognitive deficits. *(Demonstrated epidemiologically.)*
   - **Branch B:** In pregnancy → maternal anemia, adverse birth outcomes. *(Demonstrated.)*
8. Severe/prolonged anemia and hypoproteinemia **result in** fatigue, reduced work capacity, edema, and developmental/economic harm → the ~4 million DALY burden ([PMID: 32342850](https://pubmed.ncbi.nlm.nih.gov/32342850/)). *(Demonstrated.)*

```
Soil L3 larvae → skin penetration → blood → LUNG → trachea → swallowed →
SMALL INTESTINE → adult worm attaches → blood feeding (Na-APR-1 / Na-GST-1) →
host immune tolerance → chronic blood + protein loss →
IRON-DEFICIENCY ANEMIA + HYPOPROTEINEMIA → fatigue, stunting, maternal anemia → DALYs
```

**Molecular/cellular processes:** Hemoglobin proteolysis (*Na*-APR-1) and heme detoxification (*Na*-GST-1) in the parasite; a Th2/regulatory host immune response (eosinophilia, IgE) that is non-protective and tolerogenic. **GO term suggestions:** GO:0006508 (proteolysis), GO:0042167 (heme catabolic process), GO:0042493 (response to drug), GO:0002376 (immune system process). **Cell types involved (CL):** CL:0000235 (macrophage), CL:0000771 (eosinophil), CL:0000584 (enterocyte — mucosal surface the worm feeds on), CL:0000232 (erythrocyte — depleted). **Tissue damage mechanism:** mechanical mucosal injury + ongoing hemorrhage at attachment sites, not fibrosis or autoimmunity.

### 7. Anatomical Structures Affected

- **Primary organ:** Small intestine — jejunum/upper small bowel mucosa (UBERON:0002108 small intestine; UBERON:0002115 jejunum). Site of adult-worm attachment and blood feeding.
- **Secondary / transit organs:** Skin (UBERON:0002097) at larval entry; lung (UBERON:0002048) during migration; blood (UBERON:0000178) as transit and depleted compartment.
- **Body systems:** Digestive system (primary), hematologic system (anemia), respiratory system (transient), integumentary system (entry).
- **Tissue/cell level:** Intestinal epithelium/enterocytes (CL:0000584); erythrocytes (CL:0000232, net loss); eosinophils (CL:0000771).
- **Subcellular (parasite):** Worm digestive-tract lumen/surface where hemoglobin digestion occurs; relevant GO cellular component for the secreted vaccine enzymes includes GO:0005576 (extracellular region).
- **Localization/laterality:** Diffuse within small intestine; not lateralized.

### 8. Temporal Development

- **Onset:** Not congenital. Acquired at any age after soil exposure; "ground itch" is acute (hours–days post-penetration); pulmonary phase ~1 week; patency (eggs in stool) ~5–8 weeks after infection.
- **Progression:** Chronic and insidious. Adult worms live for years (commonly 3–10 years for *N. americanus*). Anemia develops gradually as iron stores deplete; severity tracks cumulative worm burden and reinfection.
- **Course pattern:** Chronic/persistent with repeated reinfection in endemic settings; fluctuates with exposure and treatment.
- **Remission:** Treatment-induced clearance of adult worms with albendazole; spontaneous worm death occurs over years, but reinfection is the norm absent sanitation improvements.
- **Critical period:** Childhood and pregnancy are windows of greatest vulnerability (iron demand) and greatest benefit from intervention.

### 9. Inheritance and Population

- **Inheritance:** **Not applicable** — infectious, not heritable. No penetrance, expressivity, anticipation, mosaicism, founder effect, or carrier frequency.
- **Epidemiology:** Global prevalence **406–480 million infections**; ~**4 million DALYs** ([PMID: 32342850](https://pubmed.ncbi.nlm.nih.gov/32342850/)). Local prevalence can be very high (e.g., 54.5% by qPCR in a Solomon Islands community [PMID: 35604904](https://pubmed.ncbi.nlm.nih.gov/35604904/); 53.6% in rural northeast Madagascar [PMID: 42960522](https://pubmed.ncbi.nlm.nih.gov/42960522/)).
- **Geographic distribution:** Tropical and subtropical sub-Saharan Africa, Southeast Asia, the Pacific, Latin America, and the Caribbean — warm, moist regions with poverty and poor sanitation. *N. americanus* is the dominant global species; *A. duodenale* has a more focal distribution.
- **Demographics:** Affects both sexes; disease burden (anemia) is heaviest in children and women of childbearing age ([PMID: 27929101](https://pubmed.ncbi.nlm.nih.gov/27929101/)). Strong inverse association with socio-economic position ([PMID: 30814567](https://pubmed.ncbi.nlm.nih.gov/30814567/)).

### 10. Diagnostics

- **Microscopy (gold-standard field method):** Stool examination for characteristic thin-shelled hookworm eggs; **Kato-Katz** for quantitative egg counts (eggs per gram → intensity classification: light/moderate/heavy). Cannot distinguish *Necator* from *Ancylostoma* eggs morphologically.
- **Molecular (most sensitive, species-specific):** **qPCR** on stool detects and speciates *N. americanus*, revealing substantially higher true prevalence than microscopy ([PMID: 35604904](https://pubmed.ncbi.nlm.nih.gov/35604904/)). Useful as endemicity approaches elimination.
- **Larval culture:** Harada-Mori / coproculture to hatch and identify L3 larvae for speciation.
- **Laboratory abnormalities:** Microcytic hypochromic anemia; low serum ferritin/iron; **eosinophilia** (HP:0001880); hypoalbuminemia in heavy infection. Relevant LOINC-type tests: hemoglobin, ferritin, stool ova and parasites.
- **Imaging/endoscopy:** Not routine; worms are occasionally seen incidentally at endoscopy.
- **Genetic testing / omics / newborn screening:** **Not applicable** (infectious disease).
- **Differential diagnosis:** Other STHs (*Ascaris*, *Trichuris*, *Strongyloides*), other causes of iron-deficiency anemia (dietary, GI bleeding, menorrhagia), *Ancylostoma duodenale* infection, and zoonotic *A. ceylanicum* (increasingly recognized by qPCR; [PMID: 42960522](https://pubmed.ncbi.nlm.nih.gov/42960522/), [PMID: 32342850](https://pubmed.ncbi.nlm.nih.gov/32342850/)).

### 11. Outcome / Prognosis

- **Mortality:** Low direct mortality; the disease is chronic and debilitating rather than rapidly fatal. Severe anemia can contribute to death in vulnerable groups (young children, pregnant women) but necatoriasis is primarily a morbidity (DALY) burden — ~4 million DALYs ([PMID: 32342850](https://pubmed.ncbi.nlm.nih.gov/32342850/)).
- **Morbidity:** Chronic iron-deficiency anemia, fatigue, reduced work productivity, impaired childhood growth and cognition, adverse pregnancy outcomes. Emerging evidence links hookworm to altered cardiometabolic/energy status: *N. americanus* infection was negatively associated with BMI in rural Madagascar ([PMID: 42960522](https://pubmed.ncbi.nlm.nih.gov/42960522/)).
- **Recovery:** Excellent with treatment — anthelmintic clearance plus iron repletion reverses anemia. The limiting factor for durable recovery is **reinfection** in endemic settings.
- **Prognostic factors:** Worm burden/intensity, host iron/nutritional reserves, age, pregnancy, and reinfection pressure.

### 12. Treatment

**Pharmacotherapy (NCIT/CHEBI suggestions in parentheses):**
- **Albendazole** (NCIT:C28864; CHEBI:16664) — benzimidazole; single oral 400 mg dose; drug of choice for hookworm; cure ~72% (single dose, [PMID: 18430913](https://pubmed.ncbi.nlm.nih.gov/18430913/)) up to ~90% ([PMID: 31641774](https://pubmed.ncbi.nlm.nih.gov/31641774/)); egg-reduction ~93% ([PMID: 38696109](https://pubmed.ncbi.nlm.nih.gov/38696109/)).
- **Mebendazole** (NCIT:C29257) — less effective against hookworm as single dose (cure ~15–49%); multi-day dosing improves efficacy ([PMID: 18430913](https://pubmed.ncbi.nlm.nih.gov/18430913/), [PMID: 31641774](https://pubmed.ncbi.nlm.nih.gov/31641774/)).
- **Pyrantel pamoate** — alternative; ~31% single-dose cure against hookworm ([PMID: 18430913](https://pubmed.ncbi.nlm.nih.gov/18430913/)).
- **Iron supplementation** — adjunctive, to correct iron-deficiency anemia.

| Drug | Single-dose hookworm cure rate | Source |
|---|---|---|
| Albendazole | 72% (95% CI 59–81%); up to 90% | [PMID: 18430913](https://pubmed.ncbi.nlm.nih.gov/18430913/); [PMID: 31641774](https://pubmed.ncbi.nlm.nih.gov/31641774/) |
| Mebendazole | 15% (95% CI 1–27%); ≤70% overall | [PMID: 18430913](https://pubmed.ncbi.nlm.nih.gov/18430913/); [PMID: 31641774](https://pubmed.ncbi.nlm.nih.gov/31641774/) |
| Pyrantel pamoate | 31% (95% CI 19–42%) | [PMID: 18430913](https://pubmed.ncbi.nlm.nih.gov/18430913/) |

**Advanced / experimental — vaccine:** Bivalent recombinant **Na-GST-1 + Na-APR-1[M74] on Alhydrogel** (± GLA-AF adjuvant) targets the worm blood-digestion pathway to block feeding and prevent anemia. It is the only human STH vaccine in clinical trials ([PMID: 36586174](https://pubmed.ncbi.nlm.nih.gov/36586174/)), with completed phase 1 trials in Gabonese adults ([PMID: 32926834](https://pubmed.ncbi.nlm.nih.gov/32926834/)) and children (ClinicalTrials.gov NCT02839161; [PMID: 38513684](https://pubmed.ncbi.nlm.nih.gov/38513684/)), developed by the Sabin Vaccine Institute PDP / HOOKVAC consortium ([PMID: 27040400](https://pubmed.ncbi.nlm.nih.gov/27040400/)). Both antigens induced dose-dependent IgG and were well tolerated; the month 0/2/6 schedule gave higher responses ([PMID: 38513684](https://pubmed.ncbi.nlm.nih.gov/38513684/)).

**Side effects:** Benzimidazoles are generally well tolerated (mild GI). Vaccine reactogenicity was mild-to-moderate injection-site pain, headache, and fever; no vaccine-related serious adverse events ([PMID: 38513684](https://pubmed.ncbi.nlm.nih.gov/38513684/)).

**Pharmacogenomics / gene therapy / cell therapy / targeted immunotherapy:** Not applicable.

### 13. Prevention

- **Primary prevention:** WASH — latrine construction and use (protective AOR 0.41, [PMID: 35604904](https://pubmed.ncbi.nlm.nih.gov/35604904/)), safe sewage disposal, footwear, health education. Preventive chemotherapy / **mass drug administration (MDA)** with albendazole targeting school-age children, preschool children, and women of reproductive age (WHO strategy).
- **Secondary prevention:** Screen-and-treat in endemic populations; antenatal deworming (albendazole in 2nd/3rd trimester) to prevent maternal anemia ([PMID: 31641774](https://pubmed.ncbi.nlm.nih.gov/31641774/)).
- **Tertiary prevention:** Iron supplementation and repeat deworming to prevent recurrent anemia.
- **Immunization:** Investigational vaccine (see Section 12); intended for pediatric use in endemic low/middle-income countries as part of an elimination strategy ([PMID: 27040400](https://pubmed.ncbi.nlm.nih.gov/27040400/)).
- **Key limitation:** Because drugs do not prevent reinfection ([PMID: 27929101](https://pubmed.ncbi.nlm.nih.gov/27929101/)), durable control requires combining MDA with sanitation and (prospectively) vaccination.

### 14. Other Species / Natural Disease

- **Taxonomy of agent:** *Necator americanus* (NCBI Taxon:51031). Related human/zoonotic hookworms: *Ancylostoma duodenale* (Taxon:51022), *Ancylostoma ceylanicum* (zoonotic, increasingly detected by qPCR; [PMID: 42960522](https://pubmed.ncbi.nlm.nih.gov/42960522/)), *Ancylostoma caninum* (dog hookworm, cause of zoonotic eosinophilic enteritis and cutaneous larva migrans).
- **Zoonotic relevance:** *N. americanus* is primarily a human parasite with limited zoonotic reservoir, but zoonotic ancylostomiasis (*A. ceylanicum*, *A. caninum*) is a recognized, continually neglected zoonosis ([PMID: 32342850](https://pubmed.ncbi.nlm.nih.gov/32342850/)).
- **Comparative biology:** Hookworm disease mechanisms (skin penetration, blood feeding, anemia) are conserved across ancylostomatid species infecting dogs, cats, and other mammals; this underpins animal models.

### 15. Model Organisms

- **Hamster model:** The Syrian golden hamster is a permissive host supporting patent *N. americanus* infection and is used to test anthelmintics and human hookworm vaccine antigens (blood-feeding, egg-output endpoints).
- **Rodent / *Nippostrongylus brasiliensis* model:** The rat hookworm-like nematode is a classic laboratory surrogate for studying Th2 anti-helminth immunity and lung-migration biology, though it does not reproduce chronic human blood-feeding anemia.
- ***Ancylostoma ceylanicum* in hamsters/dogs:** A tractable hookworm that completes its life cycle in rodents, widely used as a surrogate for drug and vaccine testing because it causes blood-feeding and anemia analogous to human disease.
- **Model limitations:** No model fully recapitulates the years-long chronic human infection with host immune tolerance and cumulative iron depletion; permissiveness for *N. americanus* is restricted.
- **Databases:** WormBase / WormBase ParaSite (parasite genomes, including *N. americanus*), Alliance of Genome Resources.

---

## Mechanistic Model / Interpretation

Necatoriasis is best understood as a **nutritional disease produced by a mechanical, blood-feeding parasite that the host immune system tolerates rather than clears.** The entire clinical picture flows from one engine — adult worms converting host blood into worm nutrition in the small intestine — amplified by two conditions: (1) immune tolerance that lets worms persist for years, and (2) host iron/protein demand that determines whether chronic loss becomes clinically significant anemia. This explains why the disease is simultaneously ubiquitous (hundreds of millions infected) and often silent (most infections light-intensity), yet devastating at population scale among children and pregnant women whose iron margins are thin.

The molecular corollary — that the worm's hemoglobin-digestion enzymes (*Na*-APR-1, *Na*-GST-1) are both the cause of harm and the vaccine target — is the central translational insight. Blocking blood digestion is predicted to starve the worm and prevent anemia simultaneously, which is why the bivalent Alhydrogel vaccine is the most advanced of all human STH vaccines. The control paradox is equally clear: drugs cure the infection but not the exposure, so sustainable elimination requires coupling chemotherapy with sanitation and, prospectively, immunization.

---

## Evidence Base

| PMID | Title (abbreviated) | Role in this report |
|---|---|---|
| [27929101](https://pubmed.ncbi.nlm.nih.gov/27929101/) | *Hookworm infection* (review) | Defines agent, blood-feeding → anemia, immune tolerance, reinfection, control needs |
| [32926834](https://pubmed.ncbi.nlm.nih.gov/32926834/) | *Na-GST-1/Na-APR-1 phase 1, Gabonese adults* | Molecular mechanism (hemoglobin digestion/detox); vaccine safety/immunogenicity |
| [38513684](https://pubmed.ncbi.nlm.nih.gov/38513684/) | *Na-APR-1/Na-GST-1 phase 1, children, Gabon* | Pediatric vaccine trial; dosing schedule; safety |
| [27040400](https://pubmed.ncbi.nlm.nih.gov/27040400/) | *Advancing a vaccine to prevent hookworm disease and anemia* | Vaccine rationale, target product profile, DALY context |
| [36586174](https://pubmed.ncbi.nlm.nih.gov/36586174/) | *STH vaccines: where are we now?* | N. americanus vaccine is the only STH vaccine in trials |
| [18430913](https://pubmed.ncbi.nlm.nih.gov/18430913/) | *Efficacy of current drugs vs STH (meta-analysis)* | Quantifies albendazole 72% vs mebendazole 15% hookworm cure |
| [31641774](https://pubmed.ncbi.nlm.nih.gov/31641774/) | *STH treatment in pregnancy (meta-analysis)* | Albendazole up to 90% cure; mebendazole ≤70% |
| [38696109](https://pubmed.ncbi.nlm.nih.gov/38696109/) | *Albendazole vs mebendazole in children (meta-analysis)* | Albendazole ERR ~93% vs hookworm |
| [28947636](https://pubmed.ncbi.nlm.nih.gov/28947636/) | *Recommended STH drugs (network meta-analysis)* | Corroborates drug-efficacy ranking |
| [32342850](https://pubmed.ncbi.nlm.nih.gov/32342850/) | *Zoonotic Ancylostomiasis update* | Global prevalence 406–480M, ~4M DALYs; zoonotic context |
| [35604904](https://pubmed.ncbi.nlm.nih.gov/35604904/) | *qPCR STH survey, Solomon Islands* | N. americanus 54.5%; latrine protective AOR 0.41 |
| [30814567](https://pubmed.ncbi.nlm.nih.gov/30814567/) | *Household SEP and infection risk, Kenya* | Poverty as dominant risk factor |
| [31207897](https://pubmed.ncbi.nlm.nih.gov/31207897/) | *Mapping STH in Rwanda* | Endemicity mapping / at-risk populations |
| [42960522](https://pubmed.ncbi.nlm.nih.gov/42960522/) | *Hookworm, energy status & CVD, Madagascar* | N. americanus 53.6%; links to BMI/cardiometabolic status; A. ceylanicum co-circulation |

---

## Limitations and Knowledge Gaps

1. **Genetic-template mismatch (expected):** The research template is structured for Mendelian disorders. For necatoriasis, Sections 4 (human causal genes), 9 (inheritance/penetrance), 10 (genetic/omics diagnostics), and much of 12 (gene/cell therapy) are **not applicable**. These are documented as such rather than forced.
2. **Per-worm blood-loss figure** (0.03–0.05 mL/day) is a classic literature value not independently re-verified within this investigation; precise modern per-worm quantification varies by study.
3. **Host genetic susceptibility** to worm-burden intensity is biologically plausible and reported elsewhere but was not the focus and is not a disease determinant; it remains an open modifier question.
4. **Drug-efficacy heterogeneity:** cure-rate estimates vary widely by diagnostic method, egg-count intensity, follow-up interval, and single- vs multi-dose regimens; benzimidazole efficacy may be declining in some settings (possible emerging resistance), which the meta-analyses flag.
5. **Vaccine efficacy data** are limited to phase 1 (safety/immunogenicity); no phase 2/3 protective-efficacy results are yet available.
6. **Zoonotic *A. ceylanicum***, increasingly detected by qPCR, complicates "necatoriasis" prevalence estimates based on microscopy and may be under-recognized.

## Proposed Follow-up Actions

1. **Confirm and cite per-worm blood-loss quantification** from a primary physiological study to firm up the anemia dose–response claim.
2. **Compile WHO/GBD endemicity maps and country-level prevalence** to populate geographic-distribution fields with current figures.
3. **Track the hookworm vaccine's phase 2 controlled human infection / efficacy trials** for updated protective-efficacy evidence.
4. **Assess benzimidazole efficacy trends over time** (egg-reduction-rate monitoring) to flag possible emerging resistance, per the meta-analysis recommendations.
5. **Add host-immunology detail** (Th2/IgE/eosinophil mechanisms of tolerance) with primary immunology citations to deepen Section 6.
6. **Integrate qPCR-based species-resolved surveillance** to separate true *N. americanus* burden from co-circulating *Ancylostoma* species.

---

*Report compiled from 4 confirmed findings and 14 reviewed papers. Evidence sources: human clinical trials, epidemiological surveys, and systematic reviews/meta-analyses. This is an infectious disease (soil-transmitted helminthiasis); where the template presumes a heritable genetic etiology, those fields are explicitly marked not applicable.*


## Artifacts

- [OpenScientist final report](Necatoriasis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Necatoriasis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 18 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0042493` (1 mention) - the report calls it "response to drug"; GO calls it **GO_0042493**
- `CL:0000584` (2 mentions) - the report calls it "enterocyte — mucosal surface the worm feeds on", "Tissue/cell level:** Intestinal epithelium/enterocytes"; CL calls it **enterocyte**
- `NCIT:C29257` (1 mention) - the report calls it "Mebendazole"; NCIT calls it **Miconazole Nitrate**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0042493` (GO_0042493) (1 mention) - replaced by `GO:0009410`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001880` (2 mentions) - the report calls it "Eosinophilia", "eosinophilia"; HP calls it **Increased total eosinophil count**, and lists "Eosinophilia" among its other names
- `CL:0000232` (2 mentions) - the report calls it "erythrocyte — depleted"; CL calls it **erythrocyte**
- `UBERON:0002097` (1 mention) - the report calls it "Secondary / transit organs:** Skin"; UBERON calls it **skin of body**, and lists "skin organ" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0001880` - called "Eosinophilia", "eosinophilia"
- `CL:0000584` - called "enterocyte — mucosal surface the worm feeds on", "Tissue/cell level:** Intestinal epithelium/enterocytes"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.