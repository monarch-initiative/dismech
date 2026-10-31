---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-29T03:30:02.093308'
end_time: '2026-10-29T04:13:45.680292'
duration_seconds: 2623.59
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Familial Juvenile Hyperuricemic Nephropathy Type 2
  mondo_id: MONDO:0013128
  category: Mendelian
  causal_genes: REN
  omim_id: not recorded
  synonyms: ADTKD-REN; FJHN type 2; REN-associated kidney disease; autosomal dominant
    tubulointerstitial kidney disease due to mutations in REN
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
citation_count: 19
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 19
  on_topic: 13
  validator_version: 0.4.0
term_validation:
  total_terms: 25
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 1
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0013128
    reported_labels:
    - MONDO
    ontology_label: familial juvenile hyperuricemic nephropathy type 2
  - term_id: NCIT:C15366
    reported_labels:
    - Kidney transplantation
    ontology_label: Platelet Transfusion
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Familial_Juvenile_Hyperuricemic_Nephropathy_Type_2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Familial_Juvenile_Hyperuricemic_Nephropathy_Type_2-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Familial Juvenile Hyperuricemic Nephropathy Type 2
- **MONDO ID:** MONDO:0013128 (if available)
- **Causal gene(s):** REN
- **OMIM:** not recorded
- **Synonyms:** ADTKD-REN; FJHN type 2; REN-associated kidney disease; autosomal dominant tubulointerstitial kidney disease due to mutations in REN
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Familial Juvenile Hyperuricemic Nephropathy Type 2** covering all of the
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

# Familial Juvenile Hyperuricemic Nephropathy Type 2 (ADTKD-REN): A Comprehensive Disease Characteristics Report

**Disease:** Familial Juvenile Hyperuricemic Nephropathy Type 2
**Preferred modern name:** Autosomal Dominant Tubulointerstitial Kidney Disease due to *REN* mutations (**ADTKD-REN**)
**MONDO ID:** MONDO:0013128 · **OMIM:** 613092 · **Causal gene:** ***REN*** (renin; HGNC:9958; chromosome 1q32.1)

---

## Summary

**Familial Juvenile Hyperuricemic Nephropathy Type 2 is caused by heterozygous germline mutations in the *REN* gene, which encodes renin** — the rate-limiting enzyme of the renin–angiotensin–aldosterone system (RAAS). This is the single most important fact to anchor the entry: although the historical name emphasizes "hyperuricemia," the disease is fundamentally a *REN* proteinopathy and a form of Autosomal Dominant Tubulointerstitial Kidney Disease (ADTKD). Under the modern KDIGO consensus nomenclature it is designated **ADTKD-REN**, replacing older terms such as FJHN type 2, MCKD, and UAKD ([PMID: 25738250](https://pubmed.ncbi.nlm.nih.gov/25738250/)). It is distinct from **FJHN type 1**, which is caused by *UMOD* (uromodulin).

The disease presents as a distinctive **hyporeninemia syndrome**: affected children develop anemia (disproportionate to their degree of kidney impairment), mild hypotension, mild hyperkalemia, metabolic acidosis, and — beginning in the teenage years — hyperuricemia and gout. Overlying this is a **slowly progressive chronic kidney disease (CKD)** with a bland urinary sediment, culminating in end-stage kidney disease (ESKD) typically between the fifth and seventh decades of life. The mechanism is a **dominant-toxic gain of function**: mutant (pre)prorenin misfolds and is mislocalized — to the cytoplasm (signal-peptide variants), the endoplasmic reticulum–Golgi intermediate compartment and ER (prosegment and mature-renin variants), or mitochondria — injuring the specialized renin-producing juxtaglomerular cells and driving tubular atrophy and interstitial fibrosis.

Management is **supportive and mechanism-based**. Fludrocortisone can improve blood pressure and GFR; urate-lowering therapy (allopurinol) treats gout; and RAAS-blocking drugs (ACE inhibitors, ARBs), NSAIDs, and diuretics must be avoided because they aggravate the underlying hyporeninemic, volume-depleted physiology. Kidney transplantation is curative of renal failure and the disease does not recur in the allograft, because the defect is intrinsic to the patient's native renin-producing cells. Genotype predicts severity: signal-peptide variants present earliest and reach ESKD soonest, mature-renin variants latest.

---

## 1. Disease Information

**Overview.** ADTKD-REN is a rare monogenic kidney disorder characterized by progressive tubular atrophy and interstitial fibrosis, bland urinary sediment, autosomal dominant inheritance, and a cardinal set of systemic features attributable to renin deficiency. *"ADKTKD-REN is associated with signs of hyporeninemia: mild hypotension, mild hyperkalemia, anemia in childhood, and hyperuricemia and gout in the teenage years"* ([PMID: 28284384](https://pubmed.ncbi.nlm.nih.gov/28284384/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0013128 |
| OMIM | 613092 |
| Gene | *REN* (HGNC:9958) |
| Modern name | ADTKD-REN (KDIGO consensus) |

**Synonyms / alternative names:** ADTKD-REN; FJHN type 2; REN-associated kidney disease; autosomal dominant tubulointerstitial kidney disease due to mutations in *REN*. Historical umbrella terms that once included this entity: Familial Juvenile Hyperuricemic Nephropathy (FJHN), Medullary Cystic Kidney Disease (MCKD), and Uromodulin-Associated Kidney Disease (UAKD) — now disambiguated by gene ([PMID: 25738250](https://pubmed.ncbi.nlm.nih.gov/25738250/)).

**A critical disambiguation.** The historical label "Familial Juvenile Hyperuricemic Nephropathy" most often refers to the ***UMOD*-**related disease (FJHN type 1 / ADTKD-UMOD on chromosome 16), *not* the *REN* disease. *"Familial juvenile hyperuricaemic nephropathy (FJHN)... has been shown to be genetically identical to medullary cystic kidney disease (MCKD) type II... a mutant uromodulin (UMOD) is the real culprit"* ([PMID: 26872483](https://pubmed.ncbi.nlm.nih.gov/26872483/)). The present report, per the supplied MONDO ID and causal gene, concerns **FJHN type 2 = the *REN* disease (ADTKD-REN)**.

**Source of information.** Evidence is derived almost entirely from aggregated disease-level resources: an international multi-family cohort, case reports, functional/cell-biology studies, and registry data (e.g., the Wake Forest Rare Inherited Kidney Disease Registry), rather than large EHR datasets.

---

## 2. Etiology

**Primary cause — genetic.** ADTKD-REN is a Mendelian, autosomal dominant disorder caused by heterozygous germline mutations in *REN*. There is no infectious or primary environmental cause. The mutations exert a **dominant-toxic (gain-of-function) effect** on renin-producing cells: *"It is likely that expression of the mutant proteins has a dominant toxic effect gradually reducing the viability of renin-expressing cells"* ([PMID: 19664745](https://pubmed.ncbi.nlm.nih.gov/19664745/)).

**Genetic risk factors.** The causal variants themselves are the risk factor; they are private/family-specific, absent from population databases (gnomAD), and cluster in three regions of preprorenin (signal peptide, prosegment, mature protein). Variant *location* is the principal determinant of severity and age of onset (see Sections 4 and 9).

**Environmental / lifestyle modifiers (iatrogenic).** No environmental cause initiates the disease, but several exposures **worsen** it by compounding hyporeninemia and volume depletion: ACE inhibitors, angiotensin-receptor blockers, NSAIDs, and diuretics. Dehydration/volume depletion can precipitate acute kidney injury. These are "avoidance" rather than causal factors.

**Protective factors.** No validated genetic protective alleles or modifier genes are established. Mechanistically, mineralocorticoid replacement (fludrocortisone) and adequate salt/volume status counteract the hyporeninemic physiology (Section 12). Later-position (mature-renin) variants are relatively "protective" of kidney longevity compared with signal-peptide variants.

**Gene–environment interaction.** The dominant interaction is pharmacologic: RAAS blockade superimposed on an already renin-deficient system produces exaggerated hypotension, hyperkalemia, and GFR decline. This is a predictable genotype × drug interaction rather than a classic GxE susceptibility effect.

---

## 3. Phenotypes

ADTKD-REN produces a stereotyped cluster of laboratory abnormalities and clinical signs. Onset of the systemic ("hyporeninemia") features is typically **childhood**, while kidney failure is a slowly progressive adult endpoint.

| Phenotype | Type | Onset | Frequency / notes | Suggested HPO term |
|---|---|---|---|---|
| Anemia (childhood, normocytic, disproportionate to CKD) | Lab abnormality | Childhood | Characteristic, early | HP:0001903 Anemia |
| Hyperuricemia | Lab abnormality | Teenage years | Characteristic | HP:0002149 Hyperuricemia |
| Gout | Clinical sign | Teenage years–adulthood | Common | HP:0001997 Gout |
| Chronic kidney disease / decreased GFR | Clinical sign | Childhood → adult progression | Universal | HP:0012622 Chronic kidney disease |
| Hyperkalemia (mild) | Lab abnormality | Childhood | Common | HP:0002153 Hyperkalemia |
| Metabolic acidosis | Lab abnormality | Childhood | Common | HP:0001942 Metabolic acidosis |
| Hypotension (mild) | Clinical sign | Childhood | Common | HP:0002615 Hypotension |
| Bland urinary sediment / mild or no proteinuria | Lab abnormality | Throughout | Universal | HP:0000093 Proteinuria (low-grade/absent) |
| Hyporeninemia (low plasma renin) | Lab abnormality | Congenital/childhood | Mechanistic hallmark | — |
| Progression to ESKD | Clinical outcome | 5th–7th decade | Universal if untreated | HP:0003774 Stage 5 chronic kidney disease |

*"ADTKD-REN presents in childhood with mild hypotension, CKD, hyperkalemia, acidosis, and anemia"* ([PMID: 34021396](https://pubmed.ncbi.nlm.nih.gov/34021396/)). The anemia is notable for being *"out of keeping with [the] degree of renal impairment"* ([PMID: 28701203](https://pubmed.ncbi.nlm.nih.gov/28701203/)).

**Severity and progression.** Severity is variable and genotype-dependent; the course is slowly progressive (CKD) with episodic acute decompensations provoked by volume depletion or offending drugs. **Quality-of-life impact** derives from lifelong CKD, fatigue/anemia, recurrent gout, and — in untreated disease — dialysis dependence; formal QoL instrument data specific to ADTKD-REN are not available in the reviewed literature.

---

## 4. Genetic / Molecular Information

**Causal gene.** ***REN*** (renin), chromosome 1q32.1; OMIM gene 179820; HGNC:9958. Renin is synthesized as **preprorenin**: an N-terminal signal (leader) peptide, a prosegment, and the mature renin enzyme.

**Variant architecture.** Pathogenic variants are predominantly **missense substitutions and small in-frame insertions/deletions** that cluster in the preprorenin leader peptide and, less often, the prosegment and mature protein. The founding discovery identified dominant leader-sequence variants: *"mutations resulting either in the deletion (p.Leu16del) or the amino acid exchange (p.Leu16Arg) of a single leucine residue in the signal sequence of renin. Both mutations decrease signal sequence hydrophobicity and are predicted by bioinformatic analyses to damage targeting and cotranslational translocation of preprorenin into the endoplasmic reticulum"* ([PMID: 19664745](https://pubmed.ncbi.nlm.nih.gov/19664745/)).

Representative reported variants by region:

| Region | Example variants | Reference |
|---|---|---|
| Signal peptide | p.Leu16del, p.Leu16Arg, c.49T>C p.Trp17Arg, c.58T>C p.Cys20Arg, p.Trp10Arg | [19664745](https://pubmed.ncbi.nlm.nih.gov/19664745/), [28701203](https://pubmed.ncbi.nlm.nih.gov/28701203/), [21084044](https://pubmed.ncbi.nlm.nih.gov/21084044/) |
| Prosegment | Multiple (prosegment group) | [32750457](https://pubmed.ncbi.nlm.nih.gov/32750457/) |
| Mature renin | p.Leu381Pro (L381P), c.1172C>G p.Thr391Arg (T391R) | [31406136](https://pubmed.ncbi.nlm.nih.gov/31406136/), [31586593](https://pubmed.ncbi.nlm.nih.gov/31586593/) |

**Variant classification.** Variants are germline and heterozygous, co-segregate with disease, are absent from population databases (gnomAD), and are predicted deleterious; they are classified **pathogenic / likely pathogenic** under ACMG/AMP criteria. For example, T391R was *"predicted... to affect protein stability and 3D structure"* ([PMID: 31586593](https://pubmed.ncbi.nlm.nih.gov/31586593/)), and L381P *"affects an evolutionary conserved residue, co-segregates with renal disease, is not found in population databases and is predicted to be deleterious"* ([PMID: 31406136](https://pubmed.ncbi.nlm.nih.gov/31406136/)).

**Functional consequence.** **Dominant-toxic gain of function** (proteotoxicity), not simple haploinsufficiency — the mutant protein's mislocalization and the cellular stress it triggers are the drivers ([PMID: 19664745](https://pubmed.ncbi.nlm.nih.gov/19664745/)). Note that the original discovery paper also observed reduced/abolished renin biosynthesis and secretion, so a **loss of normal renin output** compounds the toxic effect.

**Modifier genes / epigenetics / chromosomal abnormalities.** No established modifier genes, disease-specific epigenetic signatures, or chromosomal abnormalities. Severity is chiefly governed by *REN* variant position.

---

## 5. Environmental Information

ADTKD-REN has **no environmental, toxic, occupational, or infectious cause**. The only clinically relevant non-genetic factors are **iatrogenic/physiologic aggravators**:

- **Drugs to avoid:** ACE inhibitors, ARBs, NSAIDs, and diuretics (worsen hypotension, hyperkalemia, AKI risk).
- **Volume status:** dehydration and intercurrent illness can precipitate acute decline.

No infectious agents are implicated. (By contrast, the *MUC1* subtype carries an infection-related mortality risk unrelated to this gene — [PMID: 39696072](https://pubmed.ncbi.nlm.nih.gov/39696072/) — which does not apply to ADTKD-REN.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A heterozygous germline **missense/in-frame *REN* variant** (in the signal peptide, prosegment, or mature renin) **leads to** a structurally abnormal preprorenin.
2. The abnormal leader peptide **reduces signal-sequence hydrophobicity**, which **impairs recognition and co-translational translocation across the ER membrane** (signal-peptide variants) — **resulting in** aberrant delivery of non-glycosylated preprorenin into the **cytoplasm** (demonstrated for p.Cys20Arg).
3. **Branch A (signal-peptide variants):** cytoplasmic/mistranslocated preprorenin, and in some cases **mitochondrial mis-rerouting**, **leads to** mitochondrial import defects and **fragmentation** of the mitochondrial network (demonstrated for W17R).
4. **Branch B (prosegment variants):** mutant prorenin/renin **is deposited in the ER–Golgi intermediate compartment**, **resulting in** decreased prorenin secretion.
5. **Branch C (mature-renin variants, e.g., L381P):** mutant prorenin **is retained in the ER**, **inducing the Unfolded Protein Response (UPR)/ER stress** (upregulation of MANF, CRELD2).
6. These convergent proteotoxic insults (ER stress and/or mitochondrial damage) **result in** progressive **injury and loss of renin-producing juxtaglomerular (JG) cells** — a dominant-toxic effect that gradually reduces their viability.
7. Loss/dysfunction of JG cells **leads to** two downstream branches:
   - **Branch i — Hyporeninemia → low angiotensin II:** reduced renin **results in** reduced angiotensin II, which **leads to** mild hypotension, impaired aldosterone-dependent potassium/acid handling (hyperkalemia, metabolic acidosis), reduced angiotensin-II–facilitated erythropoiesis (**childhood anemia**), and reduced urate excretion (**hyperuricemia/gout**).
   - **Branch ii — Structural kidney injury:** loss of renin-lineage cells and chronic tubular stress **lead to** tubular atrophy, interstitial fibrosis, and vascular abnormality, **resulting in** slowly progressive CKD → ESKD.

```
 REN mutation (signal / prosegment / mature)
        │
        ├─ signal → ↓hydrophobicity → failed ER translocation → cytoplasmic preprorenin
        │                                           └─(some)→ mitochondrial mis-targeting → fragmentation
        ├─ prosegment → deposition in ER–Golgi intermediate compartment → ↓secretion
        └─ mature → ER retention → UPR / ER stress (MANF, CRELD2)
                         │
                         ▼
          Proteotoxic injury & loss of juxtaglomerular (renin+) cells
                         │
        ┌────────────────┴───────────────────────────┐
   ↓ renin → ↓ angiotensin II                   structural injury
        │                                             │
  hypotension, hyperkalemia,                   tubular atrophy +
  acidosis, anemia, hyperuricemia              interstitial fibrosis
        │                                             │
        └──────────────► progressive CKD ◄────────────┘
                                 │
                                ESKD (5th–7th decade)
```

### Supporting detail

**Variant-specific mislocalization** ([PMID: 32750457](https://pubmed.ncbi.nlm.nih.gov/32750457/)): *"REN signal peptide mutations reduced hydrophobicity of the signal peptide, which is necessary for recognition and translocation across the endoplasmic reticulum, leading to aberrant delivery of preprorenin into the cytoplasm. REN mutations in the prosegment led to deposition of prorenin and renin in the endoplasmic reticulum-Golgi intermediate compartment and decreased prorenin secretion. Mutations in mature renin led to deposition of the mutant prorenin in the endoplasmic reticulum."*

**Mitochondrial branch** ([PMID: 37283036](https://pubmed.ncbi.nlm.nih.gov/37283036/)): *"they lead to full or partial mistargeting of the mutated proteins to mitochondria. The mutated pre-pro-sequence of renin is necessary and sufficient to drive mitochondrial rerouting, mitochondrial import defect and fragmentation."* A patient-inspired study confirmed that **ER stress is not universal** — the W17R variant activated mitochondrial dysfunction rather than the ER pathway, while L381P activated the UPR (MANF, CRELD2), indicating mechanistic heterogeneity across variants ([PMID: 38520530](https://pubmed.ncbi.nlm.nih.gov/38520530/)).

**ER stress / UPR branch** ([PMID: 31406136](https://pubmed.ncbi.nlm.nih.gov/31406136/)): L381P *"leads to its ER retention and induction of the Unfolded Protein Response in cell models and to defective pronephros development in zebrafish,"* pointing at *"ER homeostasis as a common pathway affected in ADTKD-REN."*

**JG-cell loss → fibrosis.** Loss of renin-producing cells is intrinsically fibrogenic: in mouse models, *"As a consequence of the disappearance of renin-producing cells, the kidneys developed striking vascular abnormalities and prominent striped fibrosis"* ([PMID: 20056748](https://pubmed.ncbi.nlm.nih.gov/20056748/)). The resulting histology is the ADTKD hallmark: *"progressive tubular atrophy and interstitial fibrosis"* ([PMID: 41480152](https://pubmed.ncbi.nlm.nih.gov/41480152/)).

**Anemia mechanism (Branch i detail).** Angiotensin II promotes erythropoiesis both as an erythroid growth factor and an EPO secretagogue: *"Ang II is a physiologically important regulator of erythropoiesis... a growth factor of erythroid progenitors and, in cooperation with erythropoietin, increases red blood cell mass... [and] acts as an erythropoietin secretagogue"* ([PMID: 20400218](https://pubmed.ncbi.nlm.nih.gov/20400218/)). Model-organism evidence: ACE-knockout mice have *"a normocytic anemia... Infusion of angiotensin II for 2 weeks increased hematocrit to near normal levels. These data suggest that angiotensin II facilitates erythropoiesis"* ([PMID: 11104792](https://pubmed.ncbi.nlm.nih.gov/11104792/)). Clinically, ACE inhibition lowers Ang II and EPO and worsens anemia ([PMID: 2474097](https://pubmed.ncbi.nlm.nih.gov/2474097/)). In ADTKD-REN, the same loss of Ang II explains anemia that appears in childhood, before significant CKD.

**Ontology suggestions.** GO biological processes: GO:0034976 response to ER stress / GO:0030968 IRE1-mediated UPR; GO:0006886 intracellular protein transport; GO:0002018 regulation of systemic arterial blood pressure by renin–angiotensin. GO cellular components: GO:0005783 ER, GO:0005793 ER–Golgi intermediate compartment, GO:0005739 mitochondrion, GO:0005737 cytoplasm. CL cell types: CL:0000648 juxtaglomerular cell (renin-producing cell); kidney tubule epithelial cell.

---

## 7. Anatomical Structures Affected

- **Primary organ:** kidney (UBERON:0002113), specifically the **renal cortex** and the **juxtaglomerular apparatus / afferent arteriole**.
- **Primary cell population:** **juxtaglomerular (renin-producing) cells** (CL:0000648) — the specialized smooth-muscle-derived cells of the afferent arteriole.
- **Tissue-level injury:** renal **tubules** (tubular atrophy) and the **tubulointerstitium** (interstitial fibrosis); epithelial and connective tissue compartments ([PMID: 41480152](https://pubmed.ncbi.nlm.nih.gov/41480152/), [PMID: 28284384](https://pubmed.ncbi.nlm.nih.gov/28284384/)).
- **Subcellular compartments:** endoplasmic reticulum (GO:0005783), ER–Golgi intermediate compartment (GO:0005793), mitochondrion (GO:0005739), cytoplasm (GO:0005737).
- **Secondary / systemic involvement:** hematopoietic system (anemia), systemic vasculature/blood pressure (hypotension), acid–base and potassium homeostasis, and purine metabolism (hyperuricemia → joints in gout).
- **Laterality:** bilateral (both kidneys), symmetric.

---

## 8. Temporal Development

**Onset.** The hyporeninemia features (anemia, mild hypotension, electrolyte/acid–base abnormalities) are present from **childhood**; hyperuricemia and gout emerge in the **teenage years**. An important exception is the **mature-renin (L381P) adult-onset form**, in which disease presents in adulthood — *"delineates an adult form of ADTKD-REN, a condition which has usually its onset in childhood"* ([PMID: 31406136](https://pubmed.ncbi.nlm.nih.gov/31406136/)). A patient was diagnosed only after *"forty years of renal disease"* ([PMID: 28701203](https://pubmed.ncbi.nlm.nih.gov/28701203/)), underscoring frequent delayed diagnosis.

**Onset pattern:** chronic, insidious, slowly progressive, with episodic acute worsening from volume depletion or offending drugs.

**Progression / disease course.** Lifelong, progressive CKD advancing through stages to ESKD. Age at ESKD is genotype-stratified (Section 9). Overall ADTKD: *"The mean age of ESRD is approximately 45, but the range is from 17 to >75"* ([PMID: 28284384](https://pubmed.ncbi.nlm.nih.gov/28284384/)).

**Critical window for intervention.** Early genetic diagnosis permits avoidance of nephrotoxic/RAAS drugs, mineralocorticoid replacement, anemia and urate management, and — importantly — **pre-emptive living-donor transplant planning** via cascade testing ([PMID: 28701203](https://pubmed.ncbi.nlm.nih.gov/28701203/)).

---

## 9. Inheritance and Population

**Inheritance.** Autosomal dominant, heterozygous, germline. High penetrance with **variable expressivity** governed principally by variant location. No repeat-expansion mechanism; genetic anticipation is not a feature. Founder effects/consanguinity are not relevant (dominant, private variants).

**Epidemiology.** ADTKD-REN is rare; precise prevalence/incidence figures are not established, and cases are likely under-ascertained because the phenotype mimics other causes of CKD. Identification of adult-onset variants is expected to raise the estimated prevalence ([PMID: 31406136](https://pubmed.ncbi.nlm.nih.gov/31406136/)).

**Genotype–phenotype correlation (the largest cohort).** In an international cohort of **111 individuals from 30 families**, variants segregated into three groups with distinct severity ([PMID: 32750457](https://pubmed.ncbi.nlm.nih.gov/32750457/)):

| Group | n | Mean age at presentation | Mean age at ESKD |
|---|---|---|---|
| Signal peptide | 69 | 19.7 y | 53.1 y |
| Prosegment | 27 | 22.4 y | 50.8 y |
| Mature renin | 15 | 37 y | 63.6 y (significantly slower; HR 0.367) |

*"Signal group patients were most severely affected, presenting at a mean age of 19.7 years, with the prosegment group presenting at 22.4 years, and the mature group at 37 years"* and the mature group had *"a rate of progression to end stage kidney disease (63.6 years) that was significantly slower vs. the signal (53.1 years) and prosegment groups (50.8 years) (significant hazard ratio 0.367)"* ([PMID: 32750457](https://pubmed.ncbi.nlm.nih.gov/32750457/)).

**Population demographics.** Reported in multiple populations (e.g., a first Tunisian ADTKD-REN family — [PMID: 31586593](https://pubmed.ncbi.nlm.nih.gov/31586593/); Caucasian families — [PMID: 28701203](https://pubmed.ncbi.nlm.nih.gov/28701203/)). No strong ethnic predilection, geographic clustering, or sex bias is established; consistent with autosomal dominant inheritance, the expected sex ratio is ~1:1.

---

## 10. Diagnostics

**Laboratory tests (the diagnostic fingerprint).** Low plasma renin and aldosterone; anemia (often normocytic, disproportionate to CKD); hyperuricemia; mild hyperkalemia; metabolic acidosis; elevated creatinine/reduced eGFR; and a **bland urinary sediment with minimal/no proteinuria** — a key discriminator from glomerular disease ([PMID: 34021396](https://pubmed.ncbi.nlm.nih.gov/34021396/), [PMID: 28284384](https://pubmed.ncbi.nlm.nih.gov/28284384/)).

**Biomarkers.** Low plasma renin activity/concentration is the pathophysiologic biomarker; hyperuricemia and childhood anemia are supportive clinical biomarkers.

**Histopathology (biopsy).** Nonspecific but characteristic: tubular atrophy and interstitial fibrosis without glomerular or vascular immune deposits; biopsy supports but does not establish the diagnosis ([PMID: 41480152](https://pubmed.ncbi.nlm.nih.gov/41480152/)).

**Genetic testing (definitive).** Diagnosis is confirmed by identifying a heterozygous pathogenic *REN* variant. Because ADTKD subtypes (REN, UMOD, HNF1B, MUC1) overlap clinically and *"standard nephrological diagnosis did not provide [a] clear subtype... until genetic testing was performed,"* a **multigene ADTKD panel (Sanger or NGS of UMOD, REN, HNF1B, ± MUC1)** or targeted single-gene *REN* sequencing is recommended ([PMID: 31586593](https://pubmed.ncbi.nlm.nih.gov/31586593/)). **Exome sequencing** detected the adult-onset L381P variant ([PMID: 31406136](https://pubmed.ncbi.nlm.nih.gov/31406136/)). Note: *MUC1* (dupC) requires specialized assays and is often missed on standard NGS — relevant for differential testing but not for *REN* itself.

**Differential diagnosis.** Other ADTKD subtypes — **ADTKD-UMOD** (gout-predominant, no childhood anemia/hypotension), **ADTKD-HNF1B** (kidney structural/cystic anomalies plus extrarenal features), **ADTKD-MUC1** (CKD as sole manifestation) — plus other causes of chronic tubulointerstitial disease ([PMID: 34021396](https://pubmed.ncbi.nlm.nih.gov/34021396/), [PMID: 41480152](https://pubmed.ncbi.nlm.nih.gov/41480152/)). The combination of **childhood anemia + hypotension + hyperkalemia/acidosis** points specifically to *REN*.

**Screening.** Cascade genetic testing of at-risk relatives is central — both for early management and, critically, to **exclude affected relatives as living kidney donors** ([PMID: 28701203](https://pubmed.ncbi.nlm.nih.gov/28701203/)).

---

## 11. Outcome / Prognosis

**Renal prognosis.** Progressive CKD to ESKD is the defining outcome; timing depends on genotype (signal ~53 y, prosegment ~51 y, mature ~64 y; overall ADTKD range 17–>75 y) ([PMID: 32750457](https://pubmed.ncbi.nlm.nih.gov/32750457/), [PMID: 28284384](https://pubmed.ncbi.nlm.nih.gov/28284384/)).

**Curability by transplantation.** Kidney transplantation corrects renal failure and the disease **does not recur** in the graft, because the pathology resides in the patient's own native renin-producing cells. Cascade testing enabled a successful **pre-emptive live-donor transplant** ([PMID: 28701203](https://pubmed.ncbi.nlm.nih.gov/28701203/)).

**Morbidity / quality of life.** Lifelong anemia, recurrent gout, electrolyte/acid–base disturbances, and eventual dialysis dependence (if not transplanted) drive morbidity. Life expectancy is largely determined by CKD management and transplant access; disease-specific mortality and formal QoL metrics are not quantified in the reviewed literature.

**Prognostic factors.** The dominant prognostic factor is **variant position** (signal/prosegment = earlier, faster; mature = later, slower). Standard CKD prognostics (eGFR trajectory, proteinuria — typically low here) also apply.

---

## 12. Treatment

Management is **supportive and mechanism-directed**; there is no gene-specific or disease-modifying therapy.

| Intervention | Rationale / evidence | NCIT-type term |
|---|---|---|
| **Fludrocortisone** (mineralocorticoid) | Replaces deficient mineralocorticoid effect; increased BP and eGFR in an affected 10-year-old and stabilized renal function over 4 years in another patient | Fludrocortisone (NCIT:C29060) |
| **Allopurinol / urate-lowering therapy** | Treats hyperuricemia and gout | Allopurinol (NCIT:C551) |
| **Anemia management** (iron, ESAs as needed) | Corrects childhood/CKD anemia | Erythropoiesis-stimulating agent |
| **CKD care / renal replacement** | Standard progression management; dialysis at ESKD | Hemodialysis (NCIT:C15248) |
| **Kidney transplantation** | Curative of renal failure; no recurrence | Kidney transplantation (NCIT:C15366) |
| **AVOID: ACEi, ARBs, NSAIDs, diuretics** | Aggravate hypotension, hyperkalemia, AKI risk | — |

**Direct evidence for fludrocortisone:** *"Treatment with fludrocortisone in an affected 10-year-old child resulted in an increase in blood pressure and estimated glomerular filtration rate"* ([PMID: 21084044](https://pubmed.ncbi.nlm.nih.gov/21084044/)); a subsequent report noted *"fludrocortisone treatment has shown efficacy in stabilizing the renal function of our patient over a four-year period without significant side effects"* ([PMID: 38520530](https://pubmed.ncbi.nlm.nih.gov/38520530/)). Allopurinol has historically been used for the hyperuricemia/gout component ([PMID: 26872483](https://pubmed.ncbi.nlm.nih.gov/26872483/)).

**Experimental / precision directions.** Because ER-stress markers (MANF, CRELD2) are induced by some variants (e.g., L381P) but not others (e.g., W17R, which is mitochondrial), these have been proposed as **stratification biomarkers for a targeted-therapy subgroup** ([PMID: 38520530](https://pubmed.ncbi.nlm.nih.gov/38520530/)). No approved gene, cell, or RNA therapy exists.

---

## 13. Prevention

- **Primary prevention:** not applicable to a dominant Mendelian disease; the actionable analog is **genetic counseling** and reproductive options (prenatal/preimplantation genetic testing) for carrier families.
- **Secondary prevention:** **cascade genetic screening** of at-risk relatives for early diagnosis, early avoidance of RAAS blockers/NSAIDs/diuretics, and proactive anemia/urate/CKD management ([PMID: 28701203](https://pubmed.ncbi.nlm.nih.gov/28701203/)).
- **Tertiary prevention:** slowing CKD progression (BP and volume optimization with fludrocortisone, urate control, anemia correction), and timely pre-emptive transplantation.
- **Counseling:** autosomal dominant 50% transmission risk; relatives who may serve as living donors must be genotyped first to avoid using an affected donor.
- Immunization, vector control, and environmental interventions are not applicable.

---

## 14. Other Species / Natural Disease

- **Human gene:** *REN* (NCBI Gene 5972). **Orthologs:** mouse *Ren1/Ren2* (NCBI Gene 19701/19702), rat *Ren* (NCBI Gene 24716), zebrafish *ren*.
- **Model/comparative biology:** zebrafish expressing mutant renin (L381P) show **defective pronephros development**, and the renin–angiotensin system is deeply evolutionarily conserved and essential for kidney development across species ([PMID: 31406136](https://pubmed.ncbi.nlm.nih.gov/31406136/), [PMID: 15942783](https://pubmed.ncbi.nlm.nih.gov/15942783/)).
- **Naturally occurring disease:** no well-documented spontaneous ADTKD-REN ortholog disease in companion animals or wildlife is recorded (OMIA entry not established in the reviewed literature).
- **Transmission / zoonosis:** not applicable (non-infectious, genetic).

---

## 15. Model Organisms

| Model | Type | What it captures | Reference |
|---|---|---|---|
| **Zebrafish** expressing mutant renin (L381P) | Vertebrate, in vivo | Defective pronephros development; demonstrates pathogenicity and developmental role | [PMID: 31406136](https://pubmed.ncbi.nlm.nih.gov/31406136/) |
| **Stable mammalian cell lines** (WT vs W17R, W10R, L381P renin) | In vitro | ER-stress activation (luciferase/RT-qPCR for MANF, CRELD2), subcellular localization (confocal), mitochondrial network analysis | [PMID: 38520530](https://pubmed.ncbi.nlm.nih.gov/38520530/) |
| **Transfected cell systems** (e.g., p.Cys20Arg, p.Leu16del) | In vitro | Mislocalization (cytoplasmic preprorenin), UPR induction, reduced cell growth, decreased secretion | [PMID: 21084044](https://pubmed.ncbi.nlm.nih.gov/21084044/), [PMID: 19664745](https://pubmed.ncbi.nlm.nih.gov/19664745/) |
| **ACE-knockout mice** (RAAS loss surrogate) | Mammalian, in vivo | Models the anemia arm — normocytic anemia reversible with Ang II infusion | [PMID: 11104792](https://pubmed.ncbi.nlm.nih.gov/11104792/) |
| **Dicer-deletion / renin-cell-loss mice** | Mammalian, in vivo | Consequences of losing renin-producing JG cells: vascular abnormalities + striped fibrosis | [PMID: 20056748](https://pubmed.ncbi.nlm.nih.gov/20056748/) |

**Phenotype recapitulation.** Cellular and zebrafish models faithfully reproduce the **molecular lesion** (mislocalization, ER stress/UPR, mitochondrial fragmentation) and, in zebrafish, a **developmental renal phenotype**. **Limitations:** no single model fully reproduces the slowly progressive adult human tubulointerstitial fibrosis plus the full hyporeninemia syndrome; the ACE-KO and renin-cell-loss mice model individual downstream arms (anemia; fibrosis) rather than the primary *REN* proteinopathy.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [19664745](https://pubmed.ncbi.nlm.nih.gov/19664745/) | Dominant renin gene mutations (early-onset hyperuricemia, anemia, CKF) | Founding discovery; leader-peptide variants, reduced hydrophobicity, dominant-toxic effect |
| [32750457](https://pubmed.ncbi.nlm.nih.gov/32750457/) | International cohort (111 pts / 30 families) | Genotype–phenotype groups; variant-specific mislocalization; ESKD timing |
| [37283036](https://pubmed.ncbi.nlm.nih.gov/37283036/) | Leader/pro-segment mutants misrouted to mitochondria | Mitochondrial mistargeting/fragmentation branch |
| [38520530](https://pubmed.ncbi.nlm.nih.gov/38520530/) | Not all paths lead to the ER (W17R/W10R/L381P) | ER stress not universal; W17R mitochondrial; MANF/CRELD2 biomarkers; 4-yr fludrocortisone efficacy |
| [31406136](https://pubmed.ncbi.nlm.nih.gov/31406136/) | Adult-onset ADTKD-REN, L381P in mature protein | Mature-protein variant; UPR; zebrafish pronephros defect; expands phenotype/prevalence |
| [31586593](https://pubmed.ncbi.nlm.nih.gov/31586593/) | Tunisian family, T391R | Novel pathogenic variant; importance of subtype genetic diagnosis |
| [21084044](https://pubmed.ncbi.nlm.nih.gov/21084044/) | Family with dominant REN mutation + fludrocortisone | Cys20Arg cytoplasmic accumulation; direct fludrocortisone efficacy |
| [28701203](https://pubmed.ncbi.nlm.nih.gov/28701203/) | Novel REN mutation after 40 years (Trp17Arg) | Diagnostic delay; cascade testing enabling pre-emptive live-donor transplant |
| [28284384](https://pubmed.ncbi.nlm.nih.gov/28284384/) | ADTKD review | Cardinal hyporeninemia syndrome; ESKD age distribution |
| [34021396](https://pubmed.ncbi.nlm.nih.gov/34021396/) | ADTKD: more than HNF1β | Childhood presentation; differential diagnosis; registry data |
| [25738250](https://pubmed.ncbi.nlm.nih.gov/25738250/) | KDIGO consensus | Nomenclature (ADTKD-REN), classification, diagnostic criteria |
| [41480152](https://pubmed.ncbi.nlm.nih.gov/41480152/) | UMOD/REN phenotype overlap case | Histology (tubular atrophy, interstitial fibrosis) |
| [20056748](https://pubmed.ncbi.nlm.nih.gov/20056748/) | Dicer maintains JG cells | Loss of renin cells → vascular abnormality + striped fibrosis |
| [20400218](https://pubmed.ncbi.nlm.nih.gov/20400218/) | RAS and erythropoiesis | Ang II as erythroid growth factor / EPO secretagogue (anemia mechanism) |
| [11104792](https://pubmed.ncbi.nlm.nih.gov/11104792/) | ACE-KO mice anemia | Model evidence that low Ang II causes anemia |
| [2474097](https://pubmed.ncbi.nlm.nih.gov/2474097/) | ACE inhibitors worsen anemia | Clinical corroboration of Ang II–anemia link |
| [26872483](https://pubmed.ncbi.nlm.nih.gov/26872483/) | FJHN → uromodulin | Disambiguation of FJHN terminology; allopurinol history |

**Evidence-type mix:** human clinical cohort/case reports (REN variant identification, treatment, prognosis); in vitro/cell-model mechanistic studies; zebrafish and mouse in vivo models for developmental and downstream (anemia, fibrosis) arms.

---

## Limitations and Knowledge Gaps

1. **Rarity and ascertainment.** Fewer than ~150 well-characterized patients are reported; true prevalence/incidence are unknown and likely underestimated, especially for adult-onset mature-protein variants.
2. **Mechanistic heterogeneity unresolved.** ER stress is not a universal mechanism — some variants act via mitochondrial dysfunction ([PMID: 38520530](https://pubmed.ncbi.nlm.nih.gov/38520530/)). The quantitative contribution of proteotoxicity vs. simple loss of renin output to JG-cell death is not settled.
3. **No direct animal model of the full human disease.** Downstream arms (anemia, fibrosis) are modeled in separate systems; a knock-in mouse carrying a human *REN* leader-peptide variant recapitulating the complete syndrome was not identified in the reviewed literature.
4. **Treatment evidence is thin.** Fludrocortisone benefit rests on small case reports/series, not randomized trials; allopurinol evidence is historically non-randomized ([PMID: 26872483](https://pubmed.ncbi.nlm.nih.gov/26872483/)). No disease-modifying therapy exists.
5. **Quantitative phenotype frequencies and QoL metrics** specific to ADTKD-REN are not available.
6. **Note on one anemia citation.** Two anemia-mechanism snippets were flagged as approximate matches to the stored abstracts; the mechanistic conclusion (Ang II facilitates erythropoiesis) is nonetheless supported by converging mouse ([PMID: 11104792](https://pubmed.ncbi.nlm.nih.gov/11104792/)) and clinical ([PMID: 2474097](https://pubmed.ncbi.nlm.nih.gov/2474097/)) evidence.

---

## Proposed Follow-up Experiments / Actions

1. **Variant-stratified biomarker validation.** Prospectively measure plasma/urinary MANF and CRELD2 across signal/prosegment/mature variant carriers to test whether ER-stress markers identify a UPR-targetable subgroup ([PMID: 38520530](https://pubmed.ncbi.nlm.nih.gov/38520530/)).
2. **Knock-in mouse model.** Generate a mouse carrying a human signal-peptide *REN* variant to reproduce the integrated syndrome (hyporeninemia, anemia, progressive tubulointerstitial fibrosis) and test fludrocortisone and chemical-chaperone/UPR-modulating interventions.
3. **Natural-history registry study.** Pool international cases to derive robust, genotype-specific eGFR-decline trajectories, phenotype frequencies, and QoL data.
4. **Controlled therapeutic trial.** Evaluate fludrocortisone (and/or chemical chaperones) in a multicenter registry-embedded trial with eGFR slope and anemia as endpoints.
5. **Pharmacologic proteostasis rescue.** Screen chemical chaperones / autophagy or UPR modulators in the established mutant-renin cell lines and zebrafish to reduce mislocalized (pre)prorenin toxicity.
6. **Clinical practice alert.** Embed "avoid ACEi/ARB/NSAID/diuretic" and "genotype potential living donors" decision support into nephrology/transplant workflows for any ADTKD-REN diagnosis.

---

*Report compiled from the ADTKD-REN knowledge state (7 confirmed findings; 26 papers reviewed). Causal gene: **REN** (renin), chromosome 1q32.1; MONDO:0013128; OMIM 613092.*


## Artifacts

- [OpenScientist final report](Familial_Juvenile_Hyperuricemic_Nephropathy_Type_2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Familial_Juvenile_Hyperuricemic_Nephropathy_Type_2-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 8 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013128` (3 mentions) - the report calls it "MONDO"; MONDO calls it **familial juvenile hyperuricemic nephropathy type 2**
- `NCIT:C15366` (1 mention) - the report calls it "Kidney transplantation"; NCIT calls it **Platelet Transfusion**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005783` (2 mentions) - the report calls it "Subcellular compartments:** endoplasmic reticulum"; GO calls it **endoplasmic reticulum**
- `CL:0000648` (2 mentions) - the report calls it "juxtaglomerular (renin-producing) cells"; CL calls it **kidney granular cell**, and lists "juxtaglomerular cell" among its other names
- `UBERON:0002113` (1 mention) - the report calls it "Primary organ:** kidney"; UBERON calls it **kidney**, and lists "reniculate kidney" among its other names
- `NCIT:C29060` (1 mention) - the report calls it "Fludrocortisone"; NCIT calls it **Flurazepam Hydrochloride**
- `NCIT:C551` (1 mention) - the report calls it "Allopurinol"; NCIT calls it **Hydralazine Hydrochloride**, and lists "Apressin" among its other names