---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-25T17:25:28.840850'
end_time: '2026-10-25T17:50:25.899461'
duration_seconds: 1497.06
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Neurodevelopmental Disorder With Or Without Variable Movement Or Behavioral
    Abnormalities
  mondo_id: MONDO:0859225
  category: Mendelian
  causal_genes: KCNN2
  omim_id: not recorded
  synonyms: KCNN2-related neurodevelopmental disorder; NEDMAB
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
citation_count: 7
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 5
  validator_version: 0.4.0
term_validation:
  total_terms: 25
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 14
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0859225
    reported_labels:
    - NEDMAB** (target disease)
    ontology_label: neurodevelopmental disorder with or without variable movement
      or behavioral abnormalities
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Neurodevelopmental_Disorder_With_Or_Without_Variable_Movement_Or_Behavioral_Abnormalities-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Neurodevelopmental_Disorder_With_Or_Without_Variable_Movement_Or_Behavioral_Abnormalities-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder With Or Without Variable Movement Or Behavioral Abnormalities
- **MONDO ID:** MONDO:0859225 (if available)
- **Causal gene(s):** KCNN2
- **OMIM:** not recorded
- **Synonyms:** KCNN2-related neurodevelopmental disorder; NEDMAB
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder With Or Without Variable Movement Or Behavioral Abnormalities** covering all of the
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

# Neurodevelopmental Disorder With Or Without Variable Movement Or Behavioral Abnormalities (NEDMAB): A KCNN2-Related Disorder

**MONDO:** MONDO:0859225 · **OMIM:** 619725 · **Causal gene:** *KCNN2* (OMIM 605879; HGNC:6291; NCBI Gene 3781; chr5q22.3) · **Category:** Mendelian, autosomal dominant

---

## Summary

**Neurodevelopmental Disorder With Or Without Variable Movement Or Behavioral Abnormalities (NEDMAB)** is a rare autosomal-dominant Mendelian disorder caused by heterozygous — usually *de novo* — variants in **KCNN2**, the gene encoding the **small-conductance calcium-activated potassium channel SK2 (KCa2.2)**. The pathogenic mechanism is **haploinsufficiency**: loss-of-function variants reduce functional SK2 channel activity, abolishing the SK2-mediated **medium afterhyperpolarization (mAHP)** that normally follows action-potential bursts, thereby dysregulating neuronal firing — with cerebellar Purkinje cells prominently implicated. The disorder was delineated by Mochel and colleagues in 2020 (*Brain*), who reported 11 patients and demonstrated through patch-clamp electrophysiology that the causal variants reduce SK2 channel function.

Clinically, NEDMAB presents with **motor and language developmental delay, intellectual disability**, and **early-onset movement disorders** that combine **cerebellar ataxia and/or extrapyramidal signs**; brain MRI may show white-matter abnormalities. Importantly, *KCNN2*-related disease is best understood as a **phenotypic continuum** rather than a single syndrome: the same gene causes an allelic, milder movement-predominant disorder — **Myoclonic Dystonia-34 (DYT34, OMIM 619724)** — and heterozygous *KCNN2* variants have also been reported in familial **essential tremor-plus** and **myoclonus-dystonia syndrome**, often in cognitively normal individuals. This spectrum reflects **variable expressivity** of a shared ion-channel defect.

There is currently **no disease-modifying therapy**; management is **supportive and symptom-directed** (developmental/rehabilitative therapies and symptomatic treatment of the movement disorder). Because the underlying lesion is reduced SK2 current, **SK2/KCa2.2 positive allosteric modulators** represent a rational, mechanism-based experimental therapeutic direction. The structural basis of SK2 gating — a calmodulin-gated, voltage-independent channel opened by Ca²⁺-driven conformational change of the S4–S5 linker — is now resolved by cryo-EM, providing a framework to interpret how missense variants abolish channel opening.

---

## Key Findings

### Finding 1 — *KCNN2* (SK2 channel) haploinsufficiency causes autosomal-dominant NEDMAB

The foundational study establishing *KCNN2* as a disease gene is Mochel et al. 2020 (*Brain*) [PMID: 33242881](https://pubmed.ncbi.nlm.nih.gov/33242881/). The authors identified **11 patients**: a *de novo* frameshift deletion in the index case, plus 9 additional patients carrying *de novo* variants (1 nonsense, 1 splice-site, 6 missense, 1 in-frame deletion), and one family with a **maternally inherited missense variant** (demonstrating that the disorder can be transmitted). Crucially, they performed **patch-clamp electrophysiology on six variants**; all but one (which was reclassified to a variant of uncertain significance) produced a **loss-of-function** of SK2 channels.

The authors concluded that *"heterozygous variants, likely causing a haploinsufficiency of the KCNN2 gene, lead to novel autosomal dominant neurodevelopmental movement disorders mirroring phenotypes previously described in rodents"* and that *"All variants tested but one, which was reclassified to uncertain significance, led to a loss-of-function of SK2 channels."* These two statements jointly establish the **genetic mechanism (haploinsufficiency)**, the **inheritance pattern (autosomal dominant)**, and the **functional consequence (loss of function)**.

**Variant spectrum (from Mochel 2020):**

| Variant class | Count | Inheritance observed |
|---|---|---|
| Frameshift deletion | 1 (index case) | *de novo* |
| Nonsense | 1 | *de novo* |
| Splice-site | 1 | *de novo* |
| Missense | 6 | mostly *de novo*; 1 family inherited |
| In-frame deletion | 1 | *de novo* |

Ontology anchors: gene **HGNC:6291 (KCNN2)**; disease **MONDO:0859225**; inheritance **HP:0000006 (Autosomal dominant inheritance)**.

### Finding 2 — Core phenotype: developmental delay, intellectual disability, and an early-onset movement disorder

NEDMAB's core clinical picture combines a neurodevelopmental component with a movement-disorder component. In Mochel 2020, patients had *"motor and language developmental delay, intellectual disability often associated with early-onset movement disorders comprising cerebellar ataxia and/or extrapyramidal symptoms."* The index patient specifically had *"learning disabilities, cerebellar ataxia and white matter abnormalities on brain MRI,"* documenting **CNS white-matter involvement** in addition to the cerebellar and extrapyramidal signs. A subsequent review (Rahman 2023) reiterated that loss-of-function *KCNN2* patients *"typically exhibit extrapyramidal symptoms, cerebellar ataxia, motor and language developmental delays, and intellectual disabilities."*

**Suggested HPO terms:**

| Phenotype | HPO term | Notes |
|---|---|---|
| Motor developmental delay | HP:0001270 (Motor delay) | Common |
| Speech/language delay | HP:0000750 (Delayed speech and language development) | Common |
| Intellectual disability | HP:0001249 | Common, variable severity |
| Cerebellar ataxia | HP:0001251 / HP:0001260 | Early onset |
| Dystonia | HP:0001332 | Variable (extrapyramidal) |
| Tremor | HP:0001337 | Variable |
| Myoclonus | HP:0001336 | Variable |
| White-matter abnormality on MRI | HP:0002500 (Abnormality of the cerebral white matter) | Index case |
| Behavioral abnormalities | HP:0000708 | Variable (named in the disorder title) |

Onset is **pediatric/early childhood**; severity is **variable**.

### Finding 3 — Mechanism: SK2 sets the medium afterhyperpolarization and tunes excitability; Purkinje cells are a key substrate

SK2/KCa2.2 is a **voltage-independent** potassium channel activated **solely by intracellular Ca²⁺**. Rahman 2023 [PMID: 37466411](https://pubmed.ncbi.nlm.nih.gov/37466411/) describes that *"KCa2.x channels inhibit excitatory postsynaptic potentials (EPSPs) in neuronal dendrites and contribute to the medium afterhyperpolarization (mAHP) that follows the action potential bursts."* Loss of this current removes a brake on neuronal firing. The same review links the channel to cerebellar pathology: *"rat cerebellar Purkinje cells express KCa2.2 channels, which are crucial for various cellular processes during development and maturation,"* and notes that KCa2.2 is a promising drug target in **spinocerebellar ataxias**, which feature dysregulated Purkinje firing.

Consistent with a conserved mechanism, **rodent *Kcnn2* mutants** show abnormal gait/locomotor activity, tremor, and memory deficits — phenotypes that the human disorder was explicitly described as "mirroring" (Mochel 2020). This cross-species concordance strengthens the causal inference from channel loss to the movement/cognitive phenotype.

Ontology anchors: **GO:0016286 (small conductance calcium-activated potassium channel activity)**; **GO:0019722 (calcium-mediated signaling)**; cell type **CL:0000121 (Purkinje cell)**; biological process **GO:0001508 (action potential)**.

### Finding 4 — The *KCNN2* phenotype spectrum extends to isolated/familial movement disorders (milder end, variable expressivity)

Beyond the severe neurodevelopmental cohort, heterozygous *KCNN2* variants cause milder, movement-predominant, often cognitively-normal phenotypes:

1. **Myoclonus-dystonia syndrome (MDS).** Krygier et al. 2026 (*Front Neurol*) [PMID: 41982418](https://pubmed.ncbi.nlm.nih.gov/41982418/) list *KCNN2* (alongside *KCTD17* and the classic *SGCE*) as a genetic cause of MDS, noting that *"Myoclonus-dystonia syndrome (MDS) is a clinically and genetically heterogeneous movement disorder characterized by myoclonus and dystonia as its core features."*
2. **Essential tremor-plus.** d'Apolito et al. 2023 (*Genes*) [PMID: 37510285](https://pubmed.ncbi.nlm.nih.gov/37510285/) *"identified a novel heterozygous missense variant in potassium calcium[-activated channel KCNN2]"* — NM_021614.3:c.1145G>A, p.Gly382Asp — **segregating in an Italian family** with autosomal-dominant essential tremor and variable expressivity (kinetic tremor onset ~age 20 in the mother).
3. *KCNN2* also appears among dystonia genes in large-scale exome cohorts (Thomsen et al. 2025, *Ann Clin Transl Neurol*, PMID 40533913).

This establishes a **clinical continuum** from severe NDD to isolated familial tremor/myoclonus-dystonia, reflecting **variable expressivity** of a shared channelopathy.

### Finding 5 — *KCNN2* underlies two allelic OMIM disorders: NEDMAB (619725) and DYT34 (619724)

OMIM/NCBI formalize the continuum as **two allelic autosomal-dominant disorders** of the same gene (*KCNN2*, gene MIM **605879**):

| OMIM phenotype | Name | Abbrev. | MONDO |
|---|---|---|---|
| 619725 | Neurodevelopmental disorder with or without variable movement or behavioral abnormalities | **NEDMAB** (target disease) | MONDO:0859225 |
| 619724 | Dystonia 34, myoclonic | **DYT34** | — |

The two entries codify the severe (neurodevelopmental) and milder (isolated myoclonus-dystonia) ends of the same molecular spectrum. Both are autosomal dominant.

### Finding 6 — Structural basis of SK2 gating: a calmodulin-gated channel; missense variants likely disrupt Ca²⁺/CaM-to-pore coupling

SK channels are gated **not by voltage but by Ca²⁺ via constitutively associated calmodulin (CaM)**. Cryo-EM of the human SK4–CaM complex (Lee & MacKinnon 2018, *Science*) [PMID: 29724949](https://pubmed.ncbi.nlm.nih.gov/29724949/) shows that *"Four CaM molecules bind to one channel tetramer"* — the CaM C-lobe binds constitutively while the N-lobe engages the S4–S5 linker in a Ca²⁺-dependent manner — and that *"The S4-S5 linker, which contains two distinct helices, undergoes conformational changes upon CaM binding to open the channel pore."* An intrinsically disordered fragment couples Ca²⁺/CaM binding to pore opening; a **V407F substitution increases SK2 Ca²⁺ sensitivity ~6-fold** (Nam et al. 2018, [PMID: 30013223](https://pubmed.ncbi.nlm.nih.gov/30013223/)), proving this region is a functional lever. Disease **missense variants are inferred** (not all individually demonstrated structurally) to disrupt this Ca²⁺/CaM-to-pore coupling, producing loss of function.

Ontology anchors: **GO:0005516 (calmodulin binding)**; **GO:0008076 (voltage-gated potassium channel complex)**; subcellular **GO:0005886 (plasma membrane)**; chemical entities **CHEBI:29108 (calcium(2+))**, **CHEBI:29103 (potassium(1+))**.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **heterozygous loss-of-function variant** in *KCNN2* (frameshift, nonsense, splice, in-frame deletion, or missense) arises — most often *de novo*, occasionally inherited — **which leads to** reduced quantity or function of SK2/KCa2.2 channel subunits.
2. For truncating/splice variants, nonsense-mediated decay or non-functional protein **results in** ~50% dosage (haploinsufficiency); for missense variants, the altered subunit **results in** impaired Ca²⁺/calmodulin-to-pore coupling and reduced channel opening (inferred from structure + patch-clamp; demonstrated for 5 of 6 tested variants).
3. Reduced SK2 current **leads to** loss of the **medium afterhyperpolarization (mAHP)** that normally follows action-potential bursts (demonstrated for SK2 physiology; GO:0001508).
4. Loss of the mAHP brake **results in** **dysregulated neuronal firing / hyperexcitability** and altered dendritic integration of EPSPs.
5. Because SK2 is highly expressed in **cerebellar Purkinje cells** (and thalamic reticular, hippocampal, and other neurons), the firing dysregulation **leads to** abnormal cerebellar output and basal-ganglia/thalamocortical circuit dysfunction.
   - **Branch A (cerebellar):** → cerebellar ataxia, tremor, and (index case) white-matter changes.
   - **Branch B (extrapyramidal / basal-ganglia–thalamic):** → dystonia, myoclonus, extrapyramidal signs (the DYT34 / myoclonus-dystonia end).
   - **Branch C (developmental / cortical):** → motor and language developmental delay, intellectual disability, behavioral abnormalities.
6. The **severity of circuit disruption** (modified by variant type, residual channel function, genetic background, and heteromeric SK1/SK3 assembly) **determines** position on the clinical continuum from severe NEDMAB to isolated familial tremor/myoclonus-dystonia (variable expressivity).

```
 KCNN2 LoF variant (de novo/inherited, AD)
        │ haploinsufficiency / impaired Ca²⁺-CaM gating
        ▼
 ↓ SK2 (KCa2.2) current
        │
        ▼
 Loss of medium afterhyperpolarization (mAHP)
        │
        ▼
 Neuronal firing dysregulation / hyperexcitability
        │
   ┌────┼───────────────┬────────────────────┐
   ▼    ▼               ▼                    ▼
 Cerebellum      Basal ganglia/thalamus   Cortex/development
 (Purkinje)                                     │
   │                 │                          │
   ▼                 ▼                          ▼
 Ataxia, tremor   Dystonia, myoclonus     DD, ID, behavior
   └──────────── Clinical continuum: NEDMAB ⇄ DYT34 ──────────┘
```

**Upstream vs downstream:** the mutation and reduced SK2 current are upstream; loss of mAHP and firing dysregulation are proximal/intermediate; cerebellar/extrapyramidal circuit dysfunction and the developmental phenotype are downstream. **Cell types:** Purkinje cells (CL:0000121), plus thalamic reticular neurons, hippocampal pyramidal neurons, and glutamatergic neurons broadly.

---

## Section-by-Section Report

### 1. Disease Information
NEDMAB is a rare autosomal-dominant neurodevelopmental disorder caused by *KCNN2*. **Identifiers:** OMIM 619725; MONDO:0859225; gene *KCNN2* OMIM 605879 / HGNC:6291 / NCBI Gene 3781. ICD-10/ICD-11, MeSH, and Orphanet-specific codes are not firmly established for this recently delineated entity (not recorded). **Synonyms:** KCNN2-related neurodevelopmental disorder; NEDMAB. Disease-level information is derived from **aggregated resources (OMIM) and primary case-series literature**, not from EHR/individual-patient registries.

### 2. Etiology
**Primary cause:** monogenic — heterozygous loss-of-function variants in *KCNN2*. **Genetic risk factors:** the causal variants themselves (de novo in most; inherited in some families). No susceptibility loci, modifier genes, or environmental/toxic/infectious contributors are established. **Protective factors:** none identified. **Gene–environment interactions:** none documented. This is a classic Mendelian channelopathy without a known environmental component.

### 3. Phenotypes
See Finding 2 (HPO table). **Types:** developmental (motor/language delay, ID), movement (ataxia, dystonia, tremor, myoclonus — clinical signs), behavioral abnormalities, imaging (white-matter) findings. **Onset:** pediatric/early childhood. **Severity:** variable (severe NEDMAB to mild tremor). **Progression:** developmental features relatively stable/non-degenerative; movement features may be episodic/fluctuating. **Frequency:** developmental delay and ID near-universal in the severe cohort; ataxia/extrapyramidal signs common but variable. **QoL impact:** substantial in severe cases (ID + motor disability); minimal-to-moderate at the tremor end. Formal QoL instrument data (EQ-5D/SF-36) not available.

### 4. Genetic / Molecular Information
**Causal gene:** *KCNN2* (OMIM 605879, HGNC:6291), encoding SK2/KCa2.2. **Variant types:** frameshift, nonsense, splice-site, in-frame deletion, and missense (e.g., p.Gly382Asp in familial tremor). **Classification:** pathogenic/likely pathogenic per functional (patch-clamp) evidence; one tested variant reclassified to VUS. **Functional consequence:** loss of function → haploinsufficiency (missense variants inferred to impair Ca²⁺/CaM gating). **Allele frequency:** pathogenic variants rare/absent in gnomAD; *KCNN2* is constrained. **Origin:** germline (de novo or inherited); no somatic involvement. **Modifier genes, epigenetics, chromosomal abnormalities:** none specifically established (heteromeric SK1/SK3 co-assembly is a plausible biological modifier of residual current).

### 5. Environmental Information
Not applicable — no environmental, lifestyle, or infectious contributors are known for this monogenic disorder.

### 6. Mechanism / Pathophysiology
See the ordered causal chain and diagram above (Findings 3 and 6).

### 7. Anatomical Structures Affected
**Organ/system:** central nervous system (UBERON:0001017). **Primary structures:** cerebellum (UBERON:0002037) — particularly Purkinje cells (CL:0000121); basal ganglia/thalamus circuitry (extrapyramidal signs); cerebral white matter (UBERON:0002316; abnormal on MRI in the index case). **Tissue:** nervous tissue. **Subcellular:** plasma membrane (GO:0005886) — the SK2–calmodulin channel complex. **Lateralization:** bilateral/symmetric (typical of a diffuse channelopathy).

### 8. Temporal Development
**Onset:** congenital-to-early-childhood (developmental delay recognized in infancy/early childhood; movement features early onset). **Course:** largely non-degenerative/stable developmental disability; movement component may fluctuate. **Duration:** chronic, lifelong. **Critical period:** early neurodevelopment, during which SK2 contributes to Purkinje cell maturation — suggesting a developmental window relevant to intervention timing (inferred).

### 9. Inheritance and Population
**Inheritance:** autosomal dominant (HP:0000006). **Penetrance/expressivity:** variable expressivity is prominent (the NEDMAB–DYT34–tremor continuum); penetrance appears high but variable expression occurs within families. **De novo vs inherited:** most severe cases de novo; milder phenotypes can be transmitted. **Epidemiology:** ultra-rare; precise prevalence/incidence not established (tens of reported patients). No founder effects, consanguinity role, or sex predominance documented; no defined geographic/ethnic clustering.

### 10. Diagnostics
Diagnosis rests on **molecular genetic testing** — exome/genome sequencing or neurodevelopmental/movement-disorder gene panels including *KCNN2*; single-gene testing is appropriate when the phenotype is suggestive. Variant interpretation is supported by **functional patch-clamp assays** demonstrating loss of SK2 function (research-grade confirmation). **Supportive tests:** brain MRI (may show white-matter abnormalities); clinical neurological/developmental assessment. No specific biomarker, biochemical, or metabolic test is diagnostic. **Differential diagnosis:** other genetic causes of developmental delay with ataxia/dystonia/tremor/myoclonus (e.g., *SGCE*, *KCTD17*, SCA genes, other channelopathies).

### 11. Outcome / Prognosis
NEDMAB is **non-lethal and chronic**; no disease-specific mortality or survival data indicate reduced life expectancy. Morbidity derives from intellectual disability and motor disability; prognosis correlates with position on the severity continuum (variant type, residual channel function). Formal natural-history, disability-outcome, and QoL data are lacking. No validated prognostic biomarkers exist.

### 12. Treatment
**No disease-modifying therapy** is approved. Management is **supportive and symptomatic**: developmental and rehabilitative therapies (physical, occupational, speech therapy), special education, and symptomatic treatment of the movement disorder (standard anti-tremor/anti-dystonia agents as clinically indicated). **Mechanism-based experimental direction:** because the lesion is reduced SK2 current, **SK2/KCa2.2 positive allosteric modulators** (e.g., CyPPA, NS309 classes — used experimentally) are a rational candidate strategy; SK modulators are of interest in spinocerebellar ataxia and neuroprotection research — SK positive modulators prevent ferroptosis/excitotoxicity in neuronal cells ([PMID: 38242037](https://pubmed.ncbi.nlm.nih.gov/38242037/)). No gene, cell, or RNA therapies are in clinical use. Disorder-specific pharmacogenomic data are not established.

### 13. Prevention
No primary prevention exists for a de novo monogenic disorder. **Genetic counseling** is the principal preventive tool: autosomal-dominant recurrence risk (up to 50% for an affected transmitting parent; low but non-zero for de novo cases due to possible germline mosaicism). Prenatal/preimplantation genetic testing is feasible once a familial variant is known. No immunization, screening-program, or environmental interventions apply.

### 14. Other Species / Natural Disease
**Orthologs:** mouse *Kcnn2*, rat *Kcnn2* (NCBI Gene). **Rodent models** recapitulate key features: *Kcnn2* mutants show abnormal gait/locomotor activity, tremor, and memory deficits (Mochel 2020 explicitly noted the human disorder "mirrors" rodent phenotypes). No naturally occurring companion-animal/wildlife disease is catalogued in OMIA for this gene. The channel and its mAHP role are evolutionarily conserved across mammals (strong basis for comparative study). No zoonotic/transmission relevance.

### 15. Model Organisms
**Mouse** is the principal model: knockout/mutant *Kcnn2* lines reproduce motor (gait, locomotor, tremor) and cognitive (memory) phenotypes, providing good face validity for the movement and cognitive components. **In vitro:** heterologous expression (HEK293) with **patch-clamp** is the workhorse for variant functional classification (used in Mochel 2020). Cryo-EM structural models (SK4–CaM; [PMID: 29724949](https://pubmed.ncbi.nlm.nih.gov/29724949/)) enable in-silico interpretation of missense variants. **Limitations:** rodent models may not fully capture human intellectual disability/behavioral phenotypes; patient-specific iPSC-derived neuronal/organoid models are an underdeveloped but promising resource. **Resources:** MGI (mouse), IMPC/IMSR for alleles.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [33242881](https://pubmed.ncbi.nlm.nih.gov/33242881/) | *Variants in the SK2 channel gene (KCNN2) lead to dominant neurodevelopmental movement disorders* (Mochel 2020, Brain) | **Primary/landmark.** Delineates NEDMAB; 11 patients; patch-clamp proves loss of function; establishes haploinsufficiency + AD inheritance; core phenotype; rodent concordance. Supports Findings 1–3. |
| [37466411](https://pubmed.ncbi.nlm.nih.gov/37466411/) | *KCa2.2 (SK2) channel review* (Rahman 2023) | **Mechanistic review.** mAHP/EPSP inhibition; Purkinje expression; drug-target rationale. Supports Finding 3. |
| [41982418](https://pubmed.ncbi.nlm.nih.gov/41982418/) | *Beyond SGCE: myoclonus-dystonia genetics* (Krygier 2026) | Places *KCNN2* among MDS genes. Supports Finding 4 (milder end). |
| [37510285](https://pubmed.ncbi.nlm.nih.gov/37510285/) | *Novel KCNN2 variant in familial essential tremor* (d'Apolito 2023) | Familial AD missense (p.Gly382Asp); variable expressivity. Supports Finding 4. |
| [29724949](https://pubmed.ncbi.nlm.nih.gov/29724949/) | *Activation mechanism of human SK-calmodulin channel (cryo-EM)* (Lee & MacKinnon 2018, Science) | Structural basis of CaM gating; S4–S5 conformational change. Supports Finding 6. |
| [30013223](https://pubmed.ncbi.nlm.nih.gov/30013223/) | *V-to-F substitution alters SK2 Ca²⁺ sensitivity* (Nam 2018) | Identifies a functional lever region; proves gating can be tuned by single residues. Supports Finding 6. |
| [38242037](https://pubmed.ncbi.nlm.nih.gov/38242037/) | *SK positive modulators prevent ferroptosis/excitotoxicity* | Therapeutic rationale for SK activation. Supports Treatment section. |
| 40533913 | *Dystonia gene cohort* (Thomsen 2025) | *KCNN2* among dystonia genes. Supports Finding 4. |

Supporting physiology papers (SK channel assembly and function; PMIDs 25421315, 31001092, 27357310, 37837643, 37469037, 30389838, 28714070, 38631563) corroborate SK2 biology — heteromeric SK1/SK2 assembly, mAHP control, thalamic reticular pacemaking, and hippocampal/amygdala excitability roles — reinforcing the mechanism but not specific to NEDMAB clinical claims.

**Evidence source types:** human clinical (Mochel, d'Apolito, Krygier, Thomsen); model organism (rodent *Kcnn2* phenotypes); in vitro (patch-clamp functional assays); computational/structural (cryo-EM, structure–function).

---

## Limitations and Knowledge Gaps

- **Small cohorts.** The disorder is ultra-rare; the defining study reported 11 patients, and the broader spectrum rests on scattered families/case reports. Prevalence, penetrance, and natural history are not quantified.
- **Variant functional data are partial.** Patch-clamp was performed on 6 reported variants; genotype–phenotype correlations (which variants give severe vs mild disease) remain incompletely mapped, and missense-to-pore-coupling disruption is largely **inferred** from structure, not individually demonstrated for each variant.
- **No standardized clinical identifiers.** ICD/MeSH/Orphanet codes and formal diagnostic criteria are not firmly established.
- **No therapeutics tested in patients.** SK2 positive modulators are a mechanistic hypothesis; no clinical trials exist for NEDMAB.
- **QoL, prognosis, and disability outcome data are absent.**
- **Continuum boundaries are fuzzy.** The relationship between NEDMAB (619725) and DYT34 (619724) — whether driven by specific variant classes, modifiers, or stochastic expressivity — is not resolved.
- **Citation re-verification.** Two citation snippets were flagged as "mismatch" in the internal knowledge state (PMIDs 37466411, 29724949); exact quote wording should be re-verified against source abstracts before publication-grade use.

---

## Proposed Follow-up Experiments / Actions

1. **Genotype–phenotype mapping:** systematically patch-clamp all reported *KCNN2* variants (including DYT34 and tremor variants) to correlate residual SK2 current with clinical severity; test whether truncating variants cluster at the severe end.
2. **Patient-derived iPSC neurons/organoids:** model NEDMAB variants in human cerebellar/cortical neurons to measure mAHP loss and firing dysregulation, and to screen SK2 positive modulators (CyPPA, NS309, newer activators) for functional rescue.
3. **Conditional mouse models:** Purkinje-cell–specific and forebrain-specific *Kcnn2* haploinsufficiency to dissect the cerebellar (ataxia/tremor) vs extrapyramidal vs developmental branches of the causal chain.
4. **Structural modeling of missense variants:** map each disease missense onto the SK2–CaM cryo-EM framework (S4–S5 linker, Ca²⁺/CaM interface) to predict and then test gating defects.
5. **Natural-history registry and standardized outcomes:** establish a *KCNN2* patient registry capturing HPO-coded phenotypes, MRI findings, and validated QoL/disability instruments; pursue formal ICD/Orphanet coding.
6. **Preclinical therapeutic proof-of-concept:** test SK2 positive allosteric modulators in *Kcnn2*-haploinsufficient mice for rescue of gait/tremor/cognition, as a bridge to a first-in-disease trial.
7. **Verify and finalize citations:** re-check the exact abstract wording for the two snippets flagged as "mismatch" (PMIDs 37466411, 29724949) before knowledge-base ingestion.

---

*Report compiled from a 5-iteration autonomous investigation; 6 confirmed findings; 15 papers reviewed. Primary basis: Mochel et al., Brain 2020 (PMID 33242881).*


## Artifacts

- [OpenScientist final report](Neurodevelopmental_Disorder_With_Or_Without_Variable_Movement_Or_Behavioral_Abnormalities-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Neurodevelopmental_Disorder_With_Or_Without_Variable_Movement_Or_Behavioral_Abnormalities-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 5 |
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
| Terms whose name was checked | 17 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0859225` (4 mentions) - the report calls it "NEDMAB** (target disease)"; MONDO calls it **neurodevelopmental disorder with or without variable movement or behavioral abnormalities**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002500` (1 mention) - the report calls it "Abnormality of the cerebral white matter"; HP calls it **Abnormal cerebral white matter morphology**, and lists "Abnormality of the cerebral white matter" among its other names
- `HP:0000708` (1 mention) - the report calls it "Behavioral abnormalities"; HP calls it **Atypical behavior**, and lists "Behavioral abnormality" among its other names