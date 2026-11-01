---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T03:14:31.853855'
end_time: '2026-10-30T03:31:53.985403'
duration_seconds: 1042.13
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Cardiac Valvular Defect, Developmental
  mondo_id: MONDO:0008913
  category: Mendelian
  causal_genes: PLD1
  omim_id: OMIM:212093
  synonyms: CVDD; PLD1-related congenital heart disease
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
citation_count: 21
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 14
  quotes_valid: 14
  relevance_assessed: 21
  on_topic: 11
  validator_version: 0.4.0
term_validation:
  total_terms: 26
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 1
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: HP:0001633
    reported_labels:
    - Clinical sign
    ontology_label: Abnormal mitral valve morphology
  - term_id: HP:0001638
    reported_labels:
    - Clinical sign
    ontology_label: Cardiomyopathy
  - term_id: HP:0001790
    reported_labels:
    - Physical manifestation
    ontology_label: Nonimmune hydrops fetalis
  - term_id: HP:0001560
    reported_labels:
    - Outcome
    ontology_label: Abnormality of the amniotic fluid
  - term_id: HP:0001667
    reported_labels:
    - Clinical sign
    ontology_label: Right ventricular hypertrophy
  labels_variant: 2
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
  path: Cardiac_Valvular_Defect_Developmental-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Cardiac_Valvular_Defect_Developmental-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cardiac Valvular Defect, Developmental
- **MONDO ID:** MONDO:0008913 (if available)
- **Causal gene(s):** PLD1
- **OMIM:** OMIM:212093
- **Synonyms:** CVDD; PLD1-related congenital heart disease
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Cardiac Valvular Defect, Developmental** covering all of the
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

# Cardiac Valvular Defect, Developmental (CVDD) — Comprehensive Disease Report

**Disease:** Cardiac Valvular Defect, Developmental (CVDD)
**Causal gene:** **PLD1** (Phospholipase D1; HGNC:9067; UniProt Q13393; chromosome 3q26.31)
**MONDO:** MONDO:0008913 | **OMIM:** 212093 | **Inheritance:** Autosomal recessive
**Synonyms:** CVDD; PLD1-related congenital heart disease; PLD1-related cardiac valvular dysplasia

---

## Summary

Cardiac Valvular Defect, Developmental (CVDD) is a rare, autosomal-recessive Mendelian congenital heart disease caused by **biallelic loss-of-function variants in *PLD1* (Phospholipase D1)**. It is critical to anchor this entry to the gene: although the disease name ("cardiac valvular defect") is generic and could be confused with many non-genetic or differently-caused valve disorders, the MONDO:0008913 / OMIM:212093 entity is specifically the PLD1-driven recessive disorder. Affected individuals present predominantly with **congenital right-sided cardiac valve defects** — pulmonary and tricuspid valve stenosis, atresia, and dysplasia — and, in a distinct subset, with **isolated neonatal cardiomyopathy**. The phenotypic spectrum is broad, ranging from recurrent lethal intrauterine fetal demise with hydrops at one extreme to adult-survivable valve disease requiring multiple open-heart surgeries at the other.

Mechanistically, PLD1 is a lipid-signaling enzyme that hydrolyzes phosphatidylcholine to generate the second-messenger lipid **phosphatidic acid (PA)**. Loss-of-function variants — concentrated in the catalytically critical regions of the protein — strongly reduce enzymatic activity, lowering PA production. Because PA signaling (acting through downstream nodes including mTOR, RAF/MEK/ERK, and S6 kinase) feeds into the pathways that drive **endothelial-to-mesenchymal transition (EndMT)**, a pivotal early step in endocardial-cushion valvulogenesis, PLD1 deficiency impairs the formation of normal heart valves during embryogenesis. The landmark study established directly that PLD1 inhibition decreases EndMT, providing the mechanistic link between gene loss and valve malformation.

The disorder was first linked to congenital valve defects in 2017 (Ta-Shma et al.) and definitively established in a 30-patient, 21-family cohort in 2021 (Lahrouchi et al.). The missense variant **p.I668F is an Ashkenazi Jewish founder allele** with a carrier allele frequency of ~2%. Diagnosis rests on fetal/neonatal echocardiography combined with exome or targeted *PLD1* sequencing; management is lesion-specific surgical and palliative cardiac care, as no gene-specific or disease-modifying therapy currently exists. Notably, the constitutive *Pld1*-knockout mouse is viable and models thrombosis/platelet phenotypes rather than the human congenital valve malformation — a key limitation of the available animal models.

---

## Key Findings

### Finding 1 — Biallelic loss-of-function PLD1 variants cause CVDD

The foundational genetic finding (Lahrouchi et al., 2021) identified **30 patients from 21 unrelated families** of diverse ancestries carrying **biallelic *PLD1* variants**, discovered through whole-exome sequencing of a cohort of 2,718 congenital heart disease (CHD) patients augmented by GeneMatcher-based international matchmaking. The phenotype was predominantly **congenital cardiac valve defects, strongly biased to the right side of the heart** (pulmonary and tricuspid valves). The authors wrote that they "*identified 30 patients from 21 unrelated families of different ancestries with biallelic phospholipase D1 (PLD1) variants who presented predominantly with congenital cardiac valve defects*" ([PMID: 33645542](https://pubmed.ncbi.nlm.nih.gov/33645542/)).

A second, distinct phenotype was also established: "*We also associated recessive PLD1 variants with isolated neonatal cardiomyopathy*" ([PMID: 33645542](https://pubmed.ncbi.nlm.nih.gov/33645542/)). This indicates that PLD1 deficiency can manifest either as a structural valvular defect or as a primary myocardial disorder in the neonatal period.

Crucially, the molecular consequence is loss of enzymatic function: "*PLD1 missense variants were overrepresented in regions of the protein critical for catalytic activity, and, correspondingly, we observed a strong reduction in enzymatic activity for most of the mutant proteins in an enzymatic assay*" ([PMID: 33645542](https://pubmed.ncbi.nlm.nih.gov/33645542/)). This establishes the **loss-of-function mechanism** and explains why the disorder is recessive — a single functional allele produces sufficient enzyme, while biallelic loss crosses a critical threshold during valvulogenesis. The inheritance is autosomal recessive; the disorder maps to OMIM 212093 and MONDO:0008913.

### Finding 2 — Mechanism: PLD1 loss reduces EndMT and impairs valvulogenesis; p.I668F is an Ashkenazi Jewish founder variant

The same cohort study provided the central mechanistic demonstration. Using functional assays, the authors showed that "*PLD1 inhibition decreased endothelial-mesenchymal transition, an established pivotal early step in valvulogenesis*" ([PMID: 33645542](https://pubmed.ncbi.nlm.nih.gov/33645542/)). EndMT is the developmental process by which endocardial endothelial cells delaminate, migrate, and transform into the mesenchymal cells that populate the endocardial cushions — the primordia of the cardiac septa and valves. By connecting reduced PLD1 activity to reduced EndMT, this result links the biochemical defect (lowered phosphatidic acid production) to the developmental failure (abnormal valve formation).

The study also delineated the population genetics of one key variant: "*we established that p.I668F is a founder variant among Ashkenazi Jews (allele frequency of ~2%)*" ([PMID: 33645542](https://pubmed.ncbi.nlm.nih.gov/33645542/)). A carrier allele frequency of ~2% is high for a recessive disease allele and has direct implications for carrier screening and genetic counseling in the Ashkenazi Jewish population.

### Finding 3 — PLD1 enzymology and regulation

PLD1 (UniProt Q13393; HGNC:9067; gene on chromosome 3q26.31) **hydrolyzes phosphatidylcholine to generate the lipid second-messenger phosphatidic acid (PA)**. Structural studies of the human enzyme (Bowling et al., 2020; Metrick et al., 2020) revealed that PLD1 is directly and synergistically regulated by protein kinase C (PKC), the small GTPases Arf and Rho, and the membrane phosphoinositide PIP2. As stated: "*phospholipase D1 (PLD1) hydrolyzes phosphatidylcholine to generate the lipid second-messenger phosphatidic acid, which plays roles in disease processes such as thrombosis and cancer. PLD1 is directly and synergistically regulated by protein kinase C, Arf and Rho GTPases*" ([PMID: 32198492](https://pubmed.ncbi.nlm.nih.gov/32198492/)).

The product, PA, is a pleiotropic signaling lipid: "*Mammalian phospholipase D (PLD) generates phosphatidic acid, a dynamic lipid secondary messenger involved with a broad spectrum of cellular functions including but not limited to metabolism, migration, and exocytosis*" ([PMID: 33495125](https://pubmed.ncbi.nlm.nih.gov/33495125/)). The relevance to EndMT is the involvement in cell migration, a core feature of the endocardial-cushion transformation. PA exerts its effects through downstream effectors including mTOR and the RAF/MEK/ERK cascade: the pathway maps "*mechanistic connections to disease through mTOR and RAF/MEK/ERK signaling*" ([PMID: 41173720](https://pubmed.ncbi.nlm.nih.gov/41173720/)). These nodes intersect the canonical signaling arms governing valve development (see Mechanistic Model below).

### Finding 4 — Pld1-knockout mice model thrombosis, not congenital valve defects

A key translational caveat emerges from the mouse literature. Constitutive *Pld1*(−/−) mice (Elvers et al., 2010) are **viable and fertile** and display **platelet/thrombosis phenotypes** rather than overt congenital valve malformation: "*platelets from Pld1(-/-) mice displayed impaired alpha(IIb)beta(3) integrin activation in response to major agonists and defective glycoprotein Ib-dependent aggregate formation under high shear conditions. These defects resulted in protection from thrombosis and ischemic brain infarction without affecting tail bleeding times*" ([PMID: 20051593](https://pubmed.ncbi.nlm.nih.gov/20051593/)).

Pharmacologic PLD inhibition reproduces the anti-thrombotic protection: "*pharmacological PLD inhibition might provide a safe therapeutic strategy to prevent arterial thrombosis and ischemic stroke*" ([PMID: 23868933](https://pubmed.ncbi.nlm.nih.gov/23868933/)). PLD1 also regulates platelet-mediated inflammation ([PMID: 28711718](https://pubmed.ncbi.nlm.nih.gov/28711718/)) and TNF-α/sepsis responses ([PMID: 29968773](https://pubmed.ncbi.nlm.nih.gov/29968773/)). The absence of a reported congenital valve phenotype in the knockout mouse — despite the clear human valvulogenesis defect — points to species differences in developmental robustness or redundancy and is an important limitation for mechanistic and preclinical work.

### Finding 5 — First linkage (2017) and the full allelic/phenotypic spectrum

PLD1 was first linked to congenital valve malformations in 2017 by Ta-Shma et al., who studied two families and identified **p.His442Pro, p.Thr495fs32\*, and the splice variant c.2882+2T>C**, affecting pulmonic, tricuspid, and mitral valves, with functional support from a yeast PLD sporulation assay: "*Three mutations, p.His442Pro, p.Thr495fs32\* and c.2882+2T>C, were identified in the*" families, and "*The findings support a role for PLD1 in normal heart valvulogenesis*" ([PMID: 27799408](https://pubmed.ncbi.nlm.nih.gov/27799408/)).

The 2021 Lahrouchi study expanded the cohort to 30 patients across 21 families ([PMID: 33645542](https://pubmed.ncbi.nlm.nih.gov/33645542/)). The phenotypic spectrum is wide:
- **Most severe / lethal:** recurrent intrauterine fetal demise and non-immune fetal hydrops, including a remarkable report of three consecutive affected fetuses with homozygous PLD1 variants and recurrent right-ventricular valve dysplasia ([PMID: 37770978](https://pubmed.ncbi.nlm.nih.gov/37770978/)).
- **Adult-survivable:** a 2026 case report of a proband with a 17-year history of valve disease who underwent three open-heart surgeries, carrying novel compound heterozygous PLD1 variants ([PMID: 42591229](https://pubmed.ncbi.nlm.nih.gov/42591229/)).

The broader recessive contribution to CHD was quantified in a large exome study of 5,424 probands: "*Rare damaging RGs were estimated to contribute to at least 2.2% of CHD, with greater enrichment among laterality phenotypes (5.4%) versus other subsets (1.4%)*" ([PMID: 40030011](https://pubmed.ncbi.nlm.nih.gov/40030011/)), situating PLD1 within the recessive-gene category of congenital heart disease.

### Finding 6 — PLD1/PA intersects the canonical endocardial-cushion EndMT network

The endocardial cushions, derived from the atrioventricular canal and the outflow tract, are the primordia of the cardiac septa and valves. EndMT converts endocardial cells into cushion mesenchyme and is governed by a well-defined network. As summarized in a 2026 review: "*Various signaling pathways, including TGFβ/BMP, Wnt, Notch, Hippo/YAP, PI3K/AKT, VEGF, and mechanical stress, are involved in the modulation of endocardial cell proliferation, migration, and mesenchymal transition. Transcription factors, such as SMAD, SNAIL, TWIST, TBX2, SOX9, KLF2/4, and NFATc1, exert distinct effects on endocardial EndMT*" ([PMID: 42600378](https://pubmed.ncbi.nlm.nih.gov/42600378/)). Importantly, "*Improper morphogenesis of the endocardial cushion leads to septal and valvular abnormalities, which contribute to the largest proportion of congenital heart diseases*" ([PMID: 42600378](https://pubmed.ncbi.nlm.nih.gov/42600378/)) — precisely the CVDD phenotype.

PLD1-derived PA signals through mTOR and RAF/MEK/ERK ([PMID: 41173720](https://pubmed.ncbi.nlm.nih.gov/41173720/)) and via S6 kinase, where PA "*acts as a leukocyte chemoattractant … through S6 kinase signaling*" and drives actin polymerization and chemotaxis ([PMID: 20304930](https://pubmed.ncbi.nlm.nih.gov/20304930/)). These nodes map onto the PI3K/AKT/mTOR and MAPK arms of the EndMT network, providing a plausible molecular bridge from PLD1 loss to defective EndMT. A human iPSC valve-differentiation platform demonstrates that other CHD genes (e.g., Noonan-syndrome RAS/MAPK variants) cause EndMT defects biased toward specific valve interstitial-cell subtypes ([PMID: 41648231](https://pubmed.ncbi.nlm.nih.gov/41648231/)), offering a validated model approach directly applicable to PLD1.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic loss-of-function variants in *PLD1*** (missense in catalytic regions, frameshift, nonsense, or splice variants) **lead to** strongly reduced PLD1 catalytic activity *(demonstrated in enzymatic assays — [PMID: 33645542](https://pubmed.ncbi.nlm.nih.gov/33645542/))*.
2. Reduced PLD1 activity **results in** diminished hydrolysis of phosphatidylcholine and therefore **lower production of phosphatidic acid (PA)** *(enzymology established — [PMID: 32198492](https://pubmed.ncbi.nlm.nih.gov/32198492/), [PMID: 33495125](https://pubmed.ncbi.nlm.nih.gov/33495125/))*.
3. Lowered PA **leads to** attenuated signaling through PA-dependent effectors — mTOR, RAF/MEK/ERK, and S6 kinase — nodes that drive cell migration and the mesenchymal program *(PA→S6K/migration demonstrated in leukocytes, [PMID: 20304930](https://pubmed.ncbi.nlm.nih.gov/20304930/); PA→mTOR/ERK mapping [PMID: 41173720](https://pubmed.ncbi.nlm.nih.gov/41173720/) — **inferred** for cardiac endocardium)*.
4. Reduced PA-dependent signaling **results in** decreased **endothelial-to-mesenchymal transition (EndMT)** in the endocardium *(directly demonstrated: PLD1 inhibition decreased EndMT — [PMID: 33645542](https://pubmed.ncbi.nlm.nih.gov/33645542/))*.
5. Impaired EndMT **leads to** defective population and remodeling of the **endocardial cushions** of the atrioventricular canal and outflow tract *(EndMT is the pivotal early step in valvulogenesis — [PMID: 33645542](https://pubmed.ncbi.nlm.nih.gov/33645542/), [PMID: 42600378](https://pubmed.ncbi.nlm.nih.gov/42600378/))*.
6. Abnormal endocardial-cushion morphogenesis **results in** structural **cardiac valve malformations**, predominantly right-sided (pulmonary/tricuspid stenosis, atresia, dysplasia). **Branch:** in a distinct subset the same lesion **results in** **isolated neonatal cardiomyopathy** rather than a structural valve defect *(both phenotypes documented — [PMID: 33645542](https://pubmed.ncbi.nlm.nih.gov/33645542/))*.
7. Depending on lesion severity, the valve malformation **leads to** a spectrum of outcomes: **lethal intrauterine fetal demise / hydrops** ([PMID: 37770978](https://pubmed.ncbi.nlm.nih.gov/37770978/)) at the severe extreme, through neonatal heart failure, to **adult-survivable valve disease** requiring repeated surgery ([PMID: 42591229](https://pubmed.ncbi.nlm.nih.gov/42591229/)).

### Schematic

```
 PLD1 biallelic LoF variants
        │  (reduced catalytic activity — demonstrated)
        ▼
 ↓ Phosphatidylcholine → Phosphatidic acid (PA)
        │  (PA second-messenger pool falls)
        ▼
 ↓ PA-dependent signaling ── mTOR ── RAF/MEK/ERK ── S6K
        │  (intersects PI3K/AKT/mTOR + MAPK arms of EndMT network)
        ▼
 ↓ EndMT in endocardium  ◄── TGFβ/BMP, Notch, Wnt, Hippo/YAP, VEGF
        │                      TFs: SNAIL, TWIST, SOX9, NFATc1, TBX2
        ▼
 Defective endocardial-cushion morphogenesis (AV canal + outflow tract)
        │
        ├────────────► Right-sided valve defects (pulmonary/tricuspid)
        └────────────► Isolated neonatal cardiomyopathy  [BRANCH]
        │
        ▼
 Spectrum: fetal demise/hydrops ── neonatal heart failure ── adult valve disease
```

### Upstream vs downstream, cells, and processes

- **Upstream:** the *PLD1* mutation and the resulting PA deficit are the proximal, gene-specific lesions.
- **Downstream / convergent:** the EndMT machinery (TGFβ/BMP, Notch, Wnt, Hippo/YAP, PI3K/AKT, VEGF; transcription factors SNAIL, TWIST, SOX9, NFATc1) is shared with many other CHD genes, explaining phenotypic overlap with other valve disorders.
- **Cell types involved:** endocardial endothelial cells (CL:0002350 endocardial cell / CL:0000115 endothelial cell) undergoing transition to cushion mesenchymal cells / valve interstitial cells (CL:0000057 fibroblast lineage).
- **Biological processes (GO):** endothelial-to-mesenchymal transition (GO:0003198 cardiac epithelial-to-mesenchymal transition / GO:0001837 EMT), heart valve morphogenesis (GO:0003179), phosphatidic acid biosynthetic process (GO:0006654), phospholipase D activity (GO:0004630).
- **Anatomy (UBERON):** cardiac valves, specifically pulmonary valve (UBERON:0002146) and tricuspid valve (UBERON:0002147); endocardial cushion (UBERON:0002062); cardiac outflow tract (UBERON:0004145); myocardium (UBERON:0002349).

---

## Comprehensive Section-by-Section Content

### 1. Disease Information
CVDD is a rare autosomal-recessive congenital heart disease of the cardiac valves caused by biallelic PLD1 loss-of-function variants. **Identifiers:** OMIM 212093; MONDO:0008913; gene PLD1 (HGNC:9067). The disease is captured at the disease level in aggregated resources (OMIM, MONDO) and has been characterized from individual patient/family case series and a multi-family cohort (human clinical evidence). **Synonyms:** CVDD; PLD1-related congenital heart disease; PLD1-related cardiac valvular dysplasia. ICD-10 maps broadly to congenital malformations of cardiac valves (Q22 for pulmonary/tricuspid valve anomalies; Q24 other). Information is derived from aggregated disease-level resources and primary case/cohort literature rather than EHR mining.

### 2. Etiology
**Primary cause:** genetic — biallelic (homozygous or compound heterozygous) loss-of-function variants in *PLD1* ([PMID: 33645542](https://pubmed.ncbi.nlm.nih.gov/33645542/), [PMID: 27799408](https://pubmed.ncbi.nlm.nih.gov/27799408/)). **Genetic risk factors:** carrier status for pathogenic PLD1 variants; the p.I668F founder allele (~2% in Ashkenazi Jews) markedly raises risk in that population; consanguinity increases homozygosity risk. **Environmental/infectious factors:** none established as causal for this Mendelian disorder. **Protective factors:** none specifically identified; a single functional PLD1 allele is protective (recessive disease, carriers unaffected). **Gene–environment interactions:** not characterized for CVDD.

### 3. Phenotypes
| Phenotype | Type | Suggested HPO | Onset | Frequency | Severity/Course |
|---|---|---|---|---|---|
| Pulmonary valve stenosis/atresia/dysplasia | Clinical sign (structural) | HP:0001642 / HP:0010450 | Congenital/fetal | Predominant (right-sided) | Severe; progressive without intervention |
| Tricuspid valve dysplasia/regurgitation/atresia | Clinical sign (structural) | HP:0010446 / HP:0005180 | Congenital/fetal | Common | Variable; can be severe |
| Mitral valve involvement | Clinical sign | HP:0001633 | Congenital | Less common | Variable |
| Neonatal cardiomyopathy | Clinical sign | HP:0001638 | Neonatal | Distinct subset | Severe |
| Non-immune fetal hydrops | Physical manifestation | HP:0001790 | Fetal | Severe cases | Often lethal |
| Intrauterine fetal demise / stillbirth | Outcome | HP:0001560 | Fetal | Severe cases | Lethal |
| Right ventricular hypoplasia / single-ventricle physiology | Clinical sign | HP:0001667 | Congenital | Severe cases | Severe |

Severity is **variable** (lethal fetal to adult-survivable). **Quality-of-life impact:** substantial in survivors — repeated cardiac surgery, chronic heart-failure risk, and lifelong cardiology follow-up ([PMID: 42591229](https://pubmed.ncbi.nlm.nih.gov/42591229/)). Disease-specific QoL instruments have not been applied in published CVDD cohorts.

### 4. Genetic / Molecular Information
**Causal gene:** *PLD1* (HGNC:9067; chromosome 3q26.31; UniProt Q13393). **Variant types reported:** missense (e.g., p.His442Pro, p.Ile668Phe, p.Arg816Pro, p.Arg391Cys), frameshift (p.Thr495fs32\*), splice-site (c.2882+2T>C; c.1062-59A>G), and compound heterozygous combinations ([PMID: 27799408](https://pubmed.ncbi.nlm.nih.gov/27799408/), [PMID: 33645542](https://pubmed.ncbi.nlm.nih.gov/33645542/), [PMID: 33142350](https://pubmed.ncbi.nlm.nih.gov/33142350/), [PMID: 39553471](https://pubmed.ncbi.nlm.nih.gov/39553471/)). **Classification:** pathogenic/likely pathogenic per ACMG, supported by functional enzymatic assays showing reduced activity. **Functional consequence:** loss of function (reduced catalysis); missense variants cluster in catalytic regions ([PMID: 33645542](https://pubmed.ncbi.nlm.nih.gov/33645542/)). **Allele frequency:** p.I668F ~2% in Ashkenazi Jews (founder); other variants rare/novel in gnomAD. **Origin:** germline. **Modifier genes / epigenetics / chromosomal abnormalities:** not established for CVDD; note that 3q26 microdeletions potentially unmasking PLD1 were considered but not confirmed as a CHD mechanism in one report ([PMID: 36345653](https://pubmed.ncbi.nlm.nih.gov/36345653/)).

### 5. Environmental Information
No environmental, lifestyle, or infectious agents are established as causal or contributory to CVDD. It is a monogenic recessive disorder. (Not applicable.)

### 6. Mechanism / Pathophysiology
See the **Mechanistic Model** section above for the full ordered causal chain and diagram. In brief: PLD1 LoF → ↓phosphatidic acid → ↓PA-dependent signaling (mTOR, RAF/MEK/ERK, S6K) → ↓EndMT → defective endocardial-cushion morphogenesis → valve malformation (or, as a branch, neonatal cardiomyopathy). Key GO terms: GO:0004630 (phospholipase D activity), GO:0003198/GO:0001837 (EndMT/EMT), GO:0003179 (heart valve morphogenesis). Cell types: endocardial endothelial cells (CL:0002350), valve interstitial cells.

### 7. Anatomical Structures Affected
**Primary organ:** heart — specifically the cardiac valves, with right-sided predominance (pulmonary valve UBERON:0002146; tricuspid valve UBERON:0002147; mitral valve UBERON:0002135 less commonly). **Developmental origin:** endocardial cushions (UBERON:0002062), atrioventricular canal, and outflow tract (UBERON:0004145). **Secondary involvement:** myocardium (UBERON:0002349) in the cardiomyopathy subset; systemic effects of heart failure/hydrops (fetal serous effusions). **Body system:** cardiovascular. **Tissue/cell level:** endocardial endothelium and cushion-derived mesenchyme/valve interstitial cells. **Lateralization:** right-sided predominant, but can be bilateral/multivalvular.

### 8. Temporal Development
**Onset:** congenital, with lesions arising during embryonic valvulogenesis; detectable prenatally by fetal echocardiography (as early as the late first/second trimester) ([PMID: 37770978](https://pubmed.ncbi.nlm.nih.gov/37770978/)). **Onset pattern:** structural and present at birth (or fetal). **Course:** ranges from lethal fetal demise to chronic lifelong valve disease; progression in survivors can require staged/repeated surgical intervention ([PMID: 42591229](https://pubmed.ncbi.nlm.nih.gov/42591229/)). **Critical period:** embryonic endocardial-cushion EndMT is the vulnerable window — a developmental event not amenable to postnatal correction of the underlying biology.

### 9. Inheritance and Population
**Inheritance:** autosomal recessive. **Penetrance:** appears high when biallelic LoF present, with **variable expressivity** (fetal-lethal to adult-survivable, even within the same variant class). **Founder effect:** p.I668F in Ashkenazi Jews (~2% allele frequency) ([PMID: 33645542](https://pubmed.ncbi.nlm.nih.gov/33645542/)). **Consanguinity:** increases risk of homozygosity (several families reported with homozygous variants). **Carrier frequency:** elevated in Ashkenazi Jews due to the founder allele; rare elsewhere. **Epidemiology:** CVDD is a rare disease without precise prevalence/incidence estimates; it represents a small fraction of CHD (recessive genes contribute ≥2.2% of CHD overall — [PMID: 40030011](https://pubmed.ncbi.nlm.nih.gov/40030011/)). **Sex ratio:** no strong sex bias reported (autosomal). **Geographic/variant distribution:** founder variant concentrated in Ashkenazi Jewish populations; other variants reported across diverse ancestries including Chinese and Japanese cohorts ([PMID: 33142350](https://pubmed.ncbi.nlm.nih.gov/33142350/), [PMID: 37770978](https://pubmed.ncbi.nlm.nih.gov/37770978/)).

### 10. Diagnostics
**Imaging:** fetal and neonatal **echocardiography** is the primary diagnostic modality, revealing right-sided valve stenosis/atresia/dysplasia, regurgitation, ventricular hypoplasia, and cardiomyopathy ([PMID: 37770978](https://pubmed.ncbi.nlm.nih.gov/37770978/)). **Genetic testing:** diagnosis confirmed by **whole-exome sequencing (WES)** or **targeted PLD1 sequencing**; WES is recommended for CHD fetuses without aneuploidy/pathogenic CNV on chromosomal microarray (CMA) ([PMID: 33142350](https://pubmed.ncbi.nlm.nih.gov/33142350/)). CMA/CNV-seq is first-line to exclude aneuploidy and 22q11.2 deletion, then WES ([PMID: 39205944](https://pubmed.ncbi.nlm.nih.gov/39205944/)). Prenatal diagnosis with Sanger confirmation of parental carrier status and splice-variant RT-PCR validation has been reported ([PMID: 39553471](https://pubmed.ncbi.nlm.nih.gov/39553471/)). **Functional confirmation:** enzymatic activity assays and yeast sporulation assays support variant pathogenicity ([PMID: 33645542](https://pubmed.ncbi.nlm.nih.gov/33645542/), [PMID: 27799408](https://pubmed.ncbi.nlm.nih.gov/27799408/)). **Differential diagnosis:** other causes of right-sided congenital valve disease and non-immune fetal hydrops, including Ebstein's anomaly and other monogenic/oligogenic CHD ([PMID: 38884760](https://pubmed.ncbi.nlm.nih.gov/38884760/)); aneuploidies and 22q11.2 deletion syndrome. **Screening:** carrier screening for p.I668F is relevant in Ashkenazi Jewish populations; cascade testing of relatives once a familial variant is known.

### 11. Outcome / Prognosis
Prognosis is **highly variable and lesion-dependent**. At the severe end, CVDD causes recurrent intrauterine fetal demise and non-immune hydrops (lethal) ([PMID: 37770978](https://pubmed.ncbi.nlm.nih.gov/37770978/)). Neonatal cardiomyopathy carries high morbidity/mortality. Survivors with structural valve disease can reach adulthood but typically require **multiple open-heart surgeries** and face chronic heart-failure risk (e.g., a proband with a 17-year disease history and three surgeries) ([PMID: 42591229](https://pubmed.ncbi.nlm.nih.gov/42591229/)). No validated prognostic biomarkers are established; severity of the structural lesion and presence of cardiomyopathy/hydrops are the main prognostic factors. Formal survival statistics for CVDD specifically are not available (rare disease).

### 12. Treatment
There is **no gene-specific or disease-modifying therapy**. Management is **lesion-specific surgical and interventional cardiac care**: balloon valvuloplasty, surgical valvotomy/valve repair or replacement, and staged palliation for single-ventricle physiology, as dictated by the anatomic defect ([PMID: 42591229](https://pubmed.ncbi.nlm.nih.gov/42591229/)). Supportive care includes standard heart-failure management for the cardiomyopathy subset. Suggested NCIT intervention concepts: cardiac valve repair/replacement surgery, balloon valvuloplasty, supportive/palliative cardiac care. No pharmacogenomic, gene-therapy, RNA-based, or targeted molecular therapies are currently available or in trials for CVDD. Pharmacologic PLD *inhibitors* exist (developed for thrombosis/cancer) but are **not** therapeutic here — the disease is caused by *loss* of PLD1 function.

### 13. Prevention
**Primary prevention:** genetic counseling and **carrier screening** (notably for p.I668F in Ashkenazi Jewish couples); for at-risk couples, **preimplantation genetic testing (PGT)** or **prenatal diagnosis** (CVS/amniocentesis with targeted variant testing) enables informed reproductive decisions ([PMID: 39553471](https://pubmed.ncbi.nlm.nih.gov/39553471/), [PMID: 36923242](https://pubmed.ncbi.nlm.nih.gov/36923242/)). **Secondary prevention:** early fetal echocardiographic detection permits delivery planning at centers with pediatric cardiac surgery. **Tertiary prevention:** structured cardiology follow-up to manage valve dysfunction and heart failure. No vaccine or environmental interventions apply.

### 14. Other Species / Natural Disease
**Orthologs:** *Pld1* is conserved across mammals (mouse NCBI Gene 18805), with functional orthologs in zebrafish, Drosophila, and yeast (the yeast PLD sporulation assay was used for functional validation — [PMID: 27799408](https://pubmed.ncbi.nlm.nih.gov/27799408/)). A naturally occurring canine model of tricuspid valve malformation exists and is discussed in the context of tricuspid valve developmental disease, though not specifically attributed to PLD1 ([PMID: 38884760](https://pubmed.ncbi.nlm.nih.gov/38884760/)). No zoonotic potential (non-infectious genetic disease).

### 15. Model Organisms
**Mouse:** constitutive *Pld1*-knockout mice are viable/fertile and exhibit **platelet/thrombosis phenotypes** (impaired αIIbβ3 activation, protection from arterial thrombosis and ischemic stroke) rather than congenital valve malformation ([PMID: 20051593](https://pubmed.ncbi.nlm.nih.gov/20051593/), [PMID: 23868933](https://pubmed.ncbi.nlm.nih.gov/23868933/)); they also model platelet-mediated inflammation ([PMID: 28711718](https://pubmed.ncbi.nlm.nih.gov/28711718/)) and TNF-α/sepsis responses ([PMID: 29968773](https://pubmed.ncbi.nlm.nih.gov/29968773/)). **Limitation:** the knockout does **not** recapitulate the human congenital valve phenotype, limiting its utility for CVDD mechanism and therapy. **Yeast:** PLD sporulation assay provides a functional readout for variant pathogenicity ([PMID: 27799408](https://pubmed.ncbi.nlm.nih.gov/27799408/)). **Human iPSC valve-differentiation platforms** generate valve interstitial-cell subtypes and model EndMT defects for other CHD genes ([PMID: 41648231](https://pubmed.ncbi.nlm.nih.gov/41648231/)) — a promising, directly applicable system for PLD1 that has not yet been formally deployed for CVDD.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role in this report |
|---|---|---|---|
| [33645542](https://pubmed.ncbi.nlm.nih.gov/33645542/) | *Biallelic LoF variants in PLD1 cause congenital right-sided cardiac valve defects and neonatal cardiomyopathy* | Human cohort (30 pts/21 families) + functional | **Primary/landmark**: gene, phenotype, LoF mechanism, EndMT link, p.I668F founder |
| [27799408](https://pubmed.ncbi.nlm.nih.gov/27799408/) | *Congenital valvular defects associated with deleterious mutations in PLD1* | Human (2 families) + yeast assay | First linkage of PLD1 to valvulogenesis (2017) |
| [32198492](https://pubmed.ncbi.nlm.nih.gov/32198492/) | *Crystal structure of human PLD1 … activation by PIP2* | Structural/in vitro | PLD1 enzymology and regulation (PKC, Arf, Rho, PIP2) |
| [33495125](https://pubmed.ncbi.nlm.nih.gov/33495125/) | *Structure and regulation of human phospholipase D* | Review/structural | PA as pleiotropic second messenger (migration) |
| [41173720](https://pubmed.ncbi.nlm.nih.gov/41173720/) | *Phosphatidic acid at the crossroads of membrane dynamics* | Review | PA downstream signaling via mTOR, RAF/MEK/ERK |
| [20304930](https://pubmed.ncbi.nlm.nih.gov/20304930/) | *Phosphatidic acid … acts through S6 kinase signaling* | In vitro | PA → S6K → migration/chemotaxis (EndMT-relevant) |
| [42600378](https://pubmed.ncbi.nlm.nih.gov/42600378/) | *Regulation of EndMT in endocardial cushion development* | Review | Canonical EndMT network PLD1/PA intersects |
| [41648231](https://pubmed.ncbi.nlm.nih.gov/41648231/) | *Dysregulated TGFβ-ERK … Noonan-associated PVS* | iPSC model | EndMT/valve-differentiation model approach |
| [20051593](https://pubmed.ncbi.nlm.nih.gov/20051593/) | *Impaired αIIbβ3 … in mice lacking PLD1* | Mouse model | Pld1-KO models thrombosis, not valve defect |
| [23868933](https://pubmed.ncbi.nlm.nih.gov/23868933/) | *Pharmacological inhibition of PLD protects mice from thrombosis* | Mouse/pharmacology | PLD inhibition → anti-thrombotic phenotype |
| [37770978](https://pubmed.ncbi.nlm.nih.gov/37770978/) | *Triple repeated fetal CHD linked to PLD1 mutation* | Human case report | Severe fetal-lethal end of spectrum |
| [42591229](https://pubmed.ncbi.nlm.nih.gov/42591229/) | *Novel compound het PLD1 variants* (2026) | Human case report | Adult-survivable end of spectrum |
| [40030011](https://pubmed.ncbi.nlm.nih.gov/40030011/) | *Recessive genetic contribution to CHD in 5,424 probands* | Human cohort | Recessive-gene contribution context |
| [33142350](https://pubmed.ncbi.nlm.nih.gov/33142350/) | *CMA + ES in fetuses with CHD* | Human cohort | Diagnostic yield, novel PLD1 variants |
| [39553471](https://pubmed.ncbi.nlm.nih.gov/39553471/) | *Prenatal detection of compound het PLD1 variants* | Human case | Prenatal diagnosis, splice variant |
| [38884760](https://pubmed.ncbi.nlm.nih.gov/38884760/) | *Molecular Pathways and Animal Models of Ebstein's Anomaly* | Review | Differential dx / canine tricuspid model |

**Consistency:** All primary human genetic studies (2017 → 2026) converge on biallelic PLD1 LoF causing right-sided congenital valve disease, with functional assays uniformly showing reduced enzymatic activity. The EndMT mechanism is supported by one direct functional demonstration ([PMID: 33645542](https://pubmed.ncbi.nlm.nih.gov/33645542/)) and is biologically coherent with the independently characterized EndMT network ([PMID: 42600378](https://pubmed.ncbi.nlm.nih.gov/42600378/)) and PA signaling literature. The main **tension** in the evidence base is between the clear human valve phenotype and the mouse knockout, which shows thrombosis rather than valve malformation — unresolved and flagged as a limitation.

---

## Limitations and Knowledge Gaps

1. **No faithful animal model.** The constitutive *Pld1*-knockout mouse does not reproduce congenital valve defects ([PMID: 20051593](https://pubmed.ncbi.nlm.nih.gov/20051593/)), leaving the in-vivo developmental mechanism without a validated mammalian model. Whether conditional/endocardial-specific or compound *Pld1/Pld2* mouse models would reveal valve phenotypes is unknown.
2. **EndMT mechanism partly inferred.** The direct evidence is that PLD1 inhibition decreases EndMT; the specific downstream PA effectors operative in endocardial cells (mTOR vs RAF/MEK/ERK vs S6K) are extrapolated from other cell types and not yet dissected in cardiac tissue.
3. **Genotype–phenotype correlation incomplete.** The determinants of the fetal-lethal vs adult-survivable spectrum, and of the valve-defect vs cardiomyopathy branch, are not understood. Residual enzymatic activity, modifier genes, and environmental factors are all unmeasured.
4. **Epidemiology unquantified.** Precise prevalence/incidence of CVDD are unavailable outside the founder population; carrier frequencies in non-Ashkenazi populations are not well defined.
5. **No disease-specific QoL, natural-history, or survival data.** Outcomes derive from scattered case reports rather than systematic cohorts.
6. **No therapeutics beyond surgery.** No molecular or gene-directed treatment exists or is in trial.

---

## Proposed Follow-up Experiments / Actions

1. **Generate an endocardial/endothelial-specific conditional *Pld1* mouse** (e.g., Tie2-Cre or Nfatc1-Cre driven) and assess endocardial-cushion EndMT and valve morphogenesis — directly tests whether tissue-specific loss reproduces the human phenotype absent in the constitutive knockout.
2. **Deploy the human iPSC valve-differentiation platform for PLD1** ([PMID: 41648231](https://pubmed.ncbi.nlm.nih.gov/41648231/)): CRISPR-engineer patient variants (p.I668F, p.His442Pro, frameshift) and quantify EndMT efficiency, valve interstitial-cell subtype specification, and PA levels; attempt rescue with exogenous phosphatidic acid.
3. **Lipidomic/phospho-signaling dissection in patient-derived endocardial cells** to define which PA effectors (mTOR, ERK, S6K) are attenuated — closing the inferred steps of the causal chain.
4. **Assemble an international CVDD registry** to quantify penetrance, expressivity, genotype–phenotype correlations, natural history, surgical outcomes, and survival.
5. **Formalize carrier-screening recommendations** for p.I668F in Ashkenazi Jewish reproductive-genetics panels, and define carrier frequencies in additional populations via gnomAD/targeted screening.
6. **Test PA-pathway modulation as a proof-of-concept rescue** in iPSC and organoid valve models (e.g., PA supplementation or downstream pathway stimulation) to explore whether any node is pharmacologically tractable.

---

*Evidence source legend: human clinical = patient/family cohorts and case reports; model organism = mouse/yeast; in vitro = enzymatic/structural/cell assays; computational = variant prediction. This report integrates 6 confirmed findings and 36 reviewed papers across 5 iterations.*


## Artifacts

- [OpenScientist final report](Cardiac_Valvular_Defect_Developmental-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Cardiac_Valvular_Defect_Developmental-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 14 |
| Quoted claims found in source | 14 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 21 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 8 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001633` (1 mention) - the report calls it "Clinical sign"; HP calls it **Abnormal mitral valve morphology**
- `HP:0001638` (1 mention) - the report calls it "Clinical sign"; HP calls it **Cardiomyopathy**
- `HP:0001790` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Nonimmune hydrops fetalis**
- `HP:0001560` (1 mention) - the report calls it "Outcome"; HP calls it **Abnormality of the amniotic fluid**
- `HP:0001667` (1 mention) - the report calls it "Clinical sign"; HP calls it **Right ventricular hypertrophy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0001837` (2 mentions) - the report calls it "EndMT/EMT"; GO calls it **epithelial to mesenchymal transition**, and lists "EMT" among its other names
- `GO:0004630` (2 mentions) - the report calls it "phospholipase D activity"; GO calls it **D-type glycerophospholipase activity**, and lists "phospholipase D activity" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.