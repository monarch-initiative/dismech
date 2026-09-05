---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T23:29:14.163339'
end_time: '2026-09-01T23:44:32.562917'
duration_seconds: 918.4
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Familial Episodic Pain Syndrome With Predominantly Lower Limb Involvement
  mondo_id: ''
  category: Disease
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
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 10
  validator_version: 0.2.1
term_validation:
  total_terms: 31
  verified: 28
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 25
  labels_matching: 13
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: HP:0025277
    reported_labels:
    - "Fluctuating course/episodic \u2014 episodic pain"
    ontology_label: Gustatory sweating
  - term_id: HP:0003394
    reported_labels:
    - "limb pain \u2014 muscle pain proxy"
    ontology_label: Muscle spasm
  - term_id: HP:0500152
    reported_labels:
    - "Cold\u2011induced pain/temperature sensitivity"
    ontology_label: Hypocystinemia
  - term_id: GO:0045211
    reported_labels:
    - axon/terminal
    ontology_label: postsynaptic membrane
  - term_id: UBERON:0001132
    reported_labels:
    - trigeminal ganglion
    ontology_label: parathyroid gland
  labels_variant: 7
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Familial_Episodic_Pain_Syndrome_With_Predominantly_Lower_Limb_Involvement-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Familial_Episodic_Pain_Syndrome_With_Predominantly_Lower_Limb_Involvement-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Familial Episodic Pain Syndrome With Predominantly Lower Limb Involvement
- **MONDO ID:**  (if available)
- **Category:** Disease

## Research Objectives

Please provide a comprehensive research report on **Familial Episodic Pain Syndrome With Predominantly Lower Limb Involvement** covering all of the
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

# Familial Episodic Pain Syndrome With Predominantly Lower Limb Involvement — Comprehensive Disease Characterization

*Autonomous discovery report — evidence base: human clinical case series/pedigrees, in vitro electrophysiology, and knock-in/knockout mouse models. Primary literature cited by PMID.*

---

## Summary (Answer to the Research Question)

**"Familial Episodic Pain Syndrome With Predominantly Lower Limb Involvement" is the SCN11A‑related subtype of familial episodic pain syndrome (FEPS3; OMIM #615552), an autosomal‑dominant sodium channelopathy of peripheral nociceptors.** It is caused by heterozygous **gain‑of‑function missense variants in *SCN11A***, which encodes the voltage‑gated sodium channel **NaV1.9** that sets the resting membrane potential (RMP) of small‑diameter dorsal‑root‑ganglion (DRG) nociceptors. Gain‑of‑function shifts NaV1.9 activation to more hyperpolarized voltages, depolarizes the RMP, and renders nociceptors hyperexcitable, producing **early‑childhood‑onset, paroxysmal, cold‑/fatigue‑/weather‑triggered episodic pain predominantly in the distal lower limbs** that characteristically **attenuates with age**. A closely related, phenotypically overlapping subtype (**FEPS2**, OMIM #615551) is caused by gain‑of‑function *SCN10A*/NaV1.8 variants; FEPS1 (*TRPA1*, #615040) predominantly affects the upper body.

---

## 1. Disease Information

**Overview.** Familial episodic pain syndrome (FEPS) is a group of rare autosomal‑dominant disorders characterized by **early‑childhood onset of severe, self‑limited episodes of pain affecting mainly the distal extremities, which tend to attenuate or diminish with age** (Shen 2022, PMID 36051609: *"Familial episodic pain syndromes (FEPS) are one of the distinctive syndromes characterized by early-childhood onset of severe episodic pain mainly affecting the distal extremities and tend to attenuate or diminish with age"*). The subtype with **predominantly lower‑limb involvement** corresponds to the tetrodotoxin‑resistant sodium‑channel FEPS subtypes — chiefly **FEPS3 (*SCN11A*/NaV1.9)**, with **FEPS2 (*SCN10A*/NaV1.8)** as a closely related alternative. In Japanese kindreds the syndrome was originally described as "infantile limb pain episodes" / paroxysmal limb intolerable pain, with pain most frequently in the **knees and ankles** (Noguchi 2017, PMID 30549873).

**Key identifiers.**
- **OMIM:** #615552 — Episodic Pain Syndrome, Familial, 3 (FEPS3; *SCN11A*). Related: #615551 (FEPS2; *SCN10A*); #615040 (FEPS1; *TRPA1*).
- **Gene OMIM:** *SCN11A* 604385; *SCN10A* 604427.
- **MONDO (suggested):** MONDO term for "familial episodic pain syndrome 3" (SCN11A‑related FEPS); parent "familial episodic pain syndrome."
- **ICD‑10:** best fit G90.09 / R52 (pain, disorders of autonomic/peripheral nervous system) — no dedicated code. **ICD‑11:** 8D89 / MG30 (chronic/neuropathic pain categories) — no dedicated code.
- **MeSH:** no dedicated descriptor; indexed under "Pain," "Sodium Channelopathies," "NAV1.9 Voltage-Gated Sodium Channel."
- **Orphanet:** rare monogenic pain syndrome (ultra‑rare; no established ORPHA prevalence class).

**Synonyms / alternative names.** Familial Episodic Pain Syndrome 3; FEPS3; SCN11A‑related familial episodic pain; Nav1.9 channelopathy (episodic pain form); "infantile limb pain episodes"; paroxysmal limb intolerable pain; familial episodic limb pain. (FEPS2 synonyms: Familial Episodic Pain Syndrome 2; SCN10A/Nav1.8‑related FEPS.)

**Source of information.** Derived from **aggregated disease‑level resources and individual pedigree/case‑series reports** (multigenerational families, mostly Japanese and Chinese, plus European cases), combined with in‑vitro and animal functional studies — **not** from population EHR datasets.

---

## 2. Etiology

**Disease causal factors — genetic.** FEPS3 is a **monogenic channelopathy**. The primary cause is a heterozygous **gain‑of‑function (GoF) missense variant in *SCN11A*** (NaV1.9). FEPS2 is caused analogously by GoF *SCN10A* (NaV1.8) variants. There is **no infectious or neoplastic etiology**; environment acts only as a trigger of episodes, not as a cause.

**Genetic risk factors (causal variants).** Recurrent/known pathogenic *SCN11A* variants include **p.Arg222His (R222H)**, **p.Arg222Ser (R222S)**, **p.Arg225Cys (R225C)**, **p.Phe814Cys (F814C)**, **p.Phe1146Ser (F1146S)**, **p.Val1184Ala (V1184A)**, **p.Leu811Phe (L811F)**, and **p.Asn816Lys (N816K)** (Kabata 2018, PMID 30557356; Huang 2019, PMID 31551682; Nagao 2025, PMID 39058404; Leipold 2015, PMID 26645915). All are germline, heterozygous, autosomal‑dominant.

**Environmental risk factors.** Not causal; **cold exposure, physical fatigue, and weather change** precipitate attacks (Noguchi 2017, PMID 30549873). Age is an inverse "risk factor" — episodes are most frequent in early childhood and diminish through adolescence.

**Protective factors.** No genetic protective alleles are established. **Environmental/behavioral protection:** warming the affected limb relieves pain, and avoidance of cold/fatigue reduces episode frequency (Noguchi 2017, PMID 30549873). In animal models, **transcutaneous cholesterol** reversed NaV1.9‑mediated hypersensitivity (Amsalem 2018, PMID 29459435), suggesting a candidate protective intervention.

**Gene–environment interactions.** The germline GoF variant lowers nociceptor threshold; **environmental modulators of NaV1.9 push already‑sensitized neurons over threshold**: (i) cold — GoF confers **cold‑resistant hyperexcitability** (Leipold 2015, PMID 26645915); (ii) inflammation lowers membrane cholesterol, moving NaV1.9 out of lipid rafts and enhancing its activation (Amsalem 2018, PMID 29459435); (iii) inflammatory mediators (bradykinin, ATP, PGE2, histamine, 5‑HT) directly excite NaV1.9⁺ afferents (Hockley 2014, PMID 24972070).

---

## 3. Phenotypes

**Core phenotype (symptom).** Paroxysmal, severe **episodic pain of the distal limbs, predominantly lower limbs** (knees, ankles > wrists, elbows). Episodes last **~15–30 minutes**, recur **several times per day**, are **triggered by fatigue and precede bad weather**, the affected region **feels cold**, and **warming relieves** the pain (Noguchi 2017, PMID 30549873: *"The pain typically lasts for 15-30 min and recurs several times a day. The pain is often induced by fatigue and is a prelude of bad weather. The affected regions feel cold in the patients, and warming the lesions relieves the symptoms."*).
- **HPO:** HP:0012531 (Pain); HP:0012532 (Chronic pain); HP:0025277 (Fluctuating course/episodic — episodic pain); HP:0003394 (limb pain — muscle pain proxy); HP:0002829 (Arthralgia — joint pain); HP:0001943 sensitivity.

**Associated phenotypes (variant‑dependent).**
- **Gastrointestinal:** episodic abdominal pain and chronic constipation with some variants (e.g., N816K), reflecting NaV1.9 expression in myenteric neurons (Huang 2019, PMID 31551682). HPO: HP:0002027 (Abdominal pain); HP:0002019 (Constipation).
- **Cold intolerance / cold‑aggravated pain** (Leipold 2015, PMID 26645915). HPO: HP:0500152 (Cold‑induced pain/temperature sensitivity).
- **Essential tremor** co‑segregation with R225C (Leng 2017, PMID 28298626). HPO: HP:0001337 (Tremor).

**Phenotype characteristics.**
- **Age of onset:** neonatal–early childhood/infancy (HP:0011463 childhood onset; often infantile onset).
- **Severity:** moderate–severe pain during episodes; **variable** expressivity between and within families.
- **Progression:** **episodic/fluctuating**, characteristically **spontaneously mitigating with age** (adolescence).
- **Frequency among affected:** distal‑limb pain is the defining feature (essentially 100% of affected); GI and tremor features are variant‑specific minorities.

**Quality‑of‑life impact.** During childhood, recurrent daily painful episodes can disrupt sleep, activity, and schooling; because episodes are self‑limited and remit with age, **long‑term disability is low** and life expectancy is unaffected. No disease‑specific QoL instrument (EQ‑5D/SF‑36/PROMIS) data are published.

---

## 4. Genetic / Molecular Information

**Causal genes.**
- ***SCN11A*** — HGNC:10583; NCBI Gene 11280; Ensembl ENSG00000168356; UniProt **Q9UI33** (NaV1.9/SCN11A); chromosome **3p22.2**; OMIM gene 604385. Encodes the α‑subunit of the tetrodotoxin‑resistant voltage‑gated sodium channel **NaV1.9**.
- ***SCN10A*** (FEPS2) — HGNC:10582; NCBI Gene 6336; UniProt Q9Y5Y9 (NaV1.8); 3p22.2; OMIM 604427.

**Pathogenic variants (SCN11A).** Missense, germline, heterozygous. Representative: **R222H, R222S, R225C, F814C, F1146S, V1184A, L811F, N816K**. Located in functionally critical regions (e.g., L811 in the DII/S6 helix important for voltage‑sensor→pore coupling; Nagao 2025, PMID 39058404). **Classification:** most reported variants are **Pathogenic/Likely Pathogenic** per ACMG (segregation + functional GoF evidence); novel variants may be VUS pending functional testing. **Variant type/class:** point missense (no frameshift/nonsense/structural variants reported for the episodic‑pain phenotype). **Allele frequency:** absent or ultra‑rare in gnomAD (consistent with high penetrance and dominant pathogenicity). **Origin:** **germline** (no somatic/COSMIC relevance). **Functional consequence:** **gain of function** (hyperpolarized activation, larger persistent/window current, RMP depolarization).

**Genotype–phenotype / allelic spectrum.** *SCN11A* is pleiotropic: modest GoF → **FEPS3 / painful small‑fiber neuropathy**; extreme GoF (sustained depolarization block) → **congenital insensitivity to pain (CIP)**. The **same residue diverges by substitution**: **L811Phe → FEPS**, **L811Pro → CIP** (Nagao 2025, PMID 39058404). R225C additionally associates with **essential tremor** (Leng 2017, PMID 28298626).

**Modifier genes.** **PRMT7** methylates NaV1.9 (Arg519) and up‑regulates NaV1.9 current and neuronal excitability — a candidate excitability modifier and drug target (Ma 2022, PMID 34326297).

**Epigenetic information.** No disease‑specific DNA‑methylation/histone changes reported. (Post‑translational **arginine methylation** of the channel by PRMT7 is a molecular—not genomic—regulatory layer.)

**Chromosomal abnormalities.** None; FEPS3 is a single‑nucleotide missense disorder, not a copy‑number/structural condition.

---

## 5. Environmental Information

- **Environmental factors:** **Cold ambient temperature** and **falling barometric pressure / bad weather** trigger episodes (Noguchi 2017, PMID 30549873). No toxin, radiation, or occupational exposure is implicated as a cause.
- **Lifestyle factors:** **Physical fatigue/exertion** is a major trigger; rest and warming mitigate. No association with smoking/alcohol/diet as causes.
- **Infectious agents:** **None** — not an infectious or immune‑mediated disease.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **heterozygous germline gain‑of‑function missense variant in *SCN11A*** alters the NaV1.9 channel protein *(demonstrated: genetics + in vitro)*.
2. The variant **shifts NaV1.9 voltage‑dependence of activation to more hyperpolarized potentials and enlarges the persistent/window current** *(demonstrated: voltage‑clamp; Leipold 2015; Huang 2019)* → **results in** more channels open near rest.
3. Increased subthreshold Na⁺ influx **depolarizes the resting membrane potential of small‑diameter C‑fiber DRG nociceptors** *(demonstrated: current‑clamp in DRG neurons)*.
4. RMP depolarization brings the membrane closer to firing threshold → **leads to** a **reduced action‑potential threshold and increased firing frequency (nociceptor hyperexcitability)** *(demonstrated)*; the hyperexcitability is **retained at cold temperatures** ("cold‑resistant") *(demonstrated: Leipold 2015)*.
5. Environmental modulators (cold, inflammation‑driven membrane‑cholesterol loss, inflammatory mediators, PRMT7 methylation) **further potentiate NaV1.9**, pushing sensitized neurons over threshold *(demonstrated in models; inferred as the trigger mechanism in patients)*.
6. Hyperexcitable distal‑limb nociceptive afferents generate **ectopic/amplified nociceptive signaling** *(inferred from cellular data)* →
7. **leads to** the **clinical episodic, cold‑/fatigue‑triggered distal (predominantly lower‑limb) pain** *(clinical)*.
   - **Branch (variant‑dependent):** NaV1.9 in **myenteric/enteric neurons** → episodic abdominal pain + constipation (Huang 2019). NaV1.9 effects on broader neuronal excitability → **essential tremor** with R225C (Leng 2017).
   - **Branch (allelic):** extreme GoF → sustained depolarization/inactivation block → **loss of firing → congenital insensitivity to pain** (opposite phenotype).
8. **Age‑dependent attenuation** *(clinical; mechanism inferred)* — episodes diminish through adolescence, possibly via developmental changes in channel expression/nociceptor maturation.

### Detail by category
- **Molecular pathways / biochemical abnormality:** primary defect is an **ion‑channel (voltage‑gated Na⁺ channel) dysfunction**; NaV1.9 is the threshold channel with the most hyperpolarized activation among VGSCs and sets RMP (Köster 2025, PMID 39836077). Downstream: action‑potential electrogenesis and neurotransmitter release from nociceptor terminals. Modulation by inflammatory mediator signaling (bradykinin/ATP/PGE2), lipid‑raft/cholesterol biology, and PRMT7 arginine‑methylation.
- **Cellular processes:** neuronal membrane depolarization, action‑potential generation, nociceptor sensitization/hyperexcitability (not apoptosis/inflammation‑driven tissue destruction).
- **Protein dysfunction:** **gain of function** via altered gating (not misfolding/aggregation); molecular‑dynamics work suggests some variants (L811F) increase structural stability and impede necessary conformational changes (Nagao 2025, PMID 39058404).
- **Immune involvement:** none primary; inflammation is a **modulatory trigger**, not an autoimmune mechanism.
- **Tissue damage:** **none** — pain is due to aberrant neuronal signaling, not tissue injury; no fibrosis/necrosis/ischemia.
- **Suggested ontology terms:** GO:0086010 (membrane depolarization during action potential); GO:0019228 (neuronal action potential); GO:0035725 (sodium ion transmembrane transport); GO:0005248 (voltage‑gated sodium channel activity, MF); GO:0050966 (detection of noxious stimulus). Cell types: **CL:0000198 (nociceptor)**, CL:0002249 / CL:0000101 (sensory/DRG neuron), CL:0011103 (enteric neuron). Subcellular: GO:0005886 (plasma membrane), GO:0045211 (axon/terminal), GO:0045121 (membrane raft).

---

## 7. Anatomical Structures Affected

- **Organ/system level:** **peripheral nervous system** (somatosensory), specifically primary sensory neurons; secondary involvement of the **enteric nervous system** (GI symptoms with some variants). Body system: **nervous (sensory)** and **digestive** (variant‑dependent).
- **Tissue/cell level:** **nervous tissue** — small‑diameter **C‑fiber nociceptors** and Aδ nociceptors of the **dorsal root ganglia** and **trigeminal ganglia**; **myenteric neurons** for GI features (Huang 2019, PMID 31551682). CL:0000198 (nociceptor); CL:0000101 (sensory neuron).
- **Subcellular level:** neuronal **plasma membrane**, including **cholesterol‑rich lipid rafts** from which NaV1.9 redistributes upon sensitization (Amsalem 2018, PMID 29459435). GO CC: GO:0005886, GO:0045121 (membrane raft).
- **Localization (UBERON):** **UBERON:0000044 (dorsal root ganglion)**; UBERON:0001132 (trigeminal ganglion); UBERON:0002240 (spinal cord dorsal horn, downstream); distal limb targets — **UBERON:0002103 (hindlimb)/UBERON:0003823 (leg)**, knees/ankles. **Lateralization: bilateral** (both legs) and typically symmetric/migratory.

---

## 8. Temporal Development

- **Onset:** **congenital/infantile to early childhood**; onset pattern is **recurrent‑paroxysmal (acute episodes on a chronic predisposition)**.
- **Progression:** **episodic/fluctuating**, **not progressive**; individual episodes are self‑limited (~15–30 min). Over years the disorder **spontaneously attenuates**, typically remitting or markedly improving **around adolescence** (Noguchi 2017, PMID 30549873; Shen 2022, PMID 36051609).
- **Disease duration:** symptomatic phase is **childhood‑limited** in most; the underlying genotype is lifelong and can manifest as milder adult sensitivity.
- **Remission:** predominantly **spontaneous/age‑dependent**; treatment‑induced relief is symptomatic.
- **Critical periods:** childhood (peak symptom burden and the window for supportive management and trigger avoidance).

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal dominant** (heterozygous). 50% offspring recurrence risk.
- **Penetrance / expressivity:** high but **variable penetrance**; **variable expressivity** in age of remission, episode frequency, and presence of GI/tremor features. No confirmed anticipation, mosaicism, or consanguinity requirement (dominant, not recessive).
- **Founder effect:** **p.R222H is a founder mutation in the Tohoku region of Japan** (7 of 48 families) (Kabata 2018, PMID 30557356: *"A founder mutation, SCN11A p.R222H was confirmed to be frequently observed in patients with FEP in the Tohoku region of Japan"*).
- **Carrier frequency:** not established; pathogenic alleles are ultra‑rare/absent in gnomAD.
- **Epidemiology:** **ultra‑rare**; no reliable prevalence/incidence per 100,000 is published. Reported cohorts are largely **Japanese** (≥48 families) and **Chinese**, with additional **European** cases.
- **Geographic distribution of variants:** R222H enriched in Tohoku, Japan; R225C reported in Chinese kindreds; V1184A (cold‑aggravated) in European cases.
- **Sex ratio / age distribution:** autosomal dominant → **no strong sex bias (≈1:1)**; affected individuals are predominantly **children/adolescents**.

---

## 10. Diagnostics

- **Clinical diagnosis** rests on the **characteristic history**: autosomal‑dominant family history + early‑childhood recurrent, self‑limited, cold/fatigue‑triggered distal (lower‑limb) pain relieved by warmth. No specific routine **laboratory** abnormality or **biomarker**; inflammatory markers, imaging (X‑ray/MRI), and standard **nerve conduction studies** are typically **normal** (large myelinated fibers spared) — useful mainly to exclude alternatives.
- **Electrophysiology:** conventional NCS usually normal; research‑level microneurography/skin biopsy for small‑fiber assessment may be considered (small‑fiber pathology overlaps the SCN11A spectrum).
- **Genetic testing (definitive):** **single‑gene sequencing or a hereditary‑pain/sodium‑channelopathy gene panel** including ***SCN11A*, *SCN10A*, *SCN9A*, *TRPA1***; **WES/WGS** for atypical/panel‑negative cases. CMA, karyotyping, FISH, mtDNA, and repeat‑expansion testing are **not indicated** (point‑mutation disorder). Variant interpretation benefits from **functional (electrophysiology) confirmation** given the GoF/LoF‑to‑phenotype divergence.
- **Diagnostic criteria:** no formal society criteria; diagnosis is molecular + clinical.
- **Differential diagnosis:** **growing pains** (benign, no family‑segregating molecular cause), **erythromelalgia / inherited erythromelalgia (SCN9A)** — but erythromelalgia features red, hot, hyperperfused extremities (opposite of the cold sensation here) (Klein‑Weigel 2018, PMID 29299961), **paroxysmal extreme pain disorder (SCN9A)**, **Fabry disease**, **small‑fiber neuropathy**, juvenile idiopathic arthritis, and autoinflammatory periodic syndromes.
- **Screening:** **cascade genetic testing** of at‑risk relatives once a familial variant is identified. No newborn/population screening.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** **normal life expectancy; no disease‑specific mortality.** Not a life‑threatening condition.
- **Morbidity/function:** morbidity is **episodic childhood pain** with possible sleep/activity disruption; **long‑term disability is minimal** because episodes remit with age.
- **Disease course/complications:** benign natural history with **spontaneous mitigation around adolescence**; complications limited to variant‑specific GI symptoms (constipation) or comorbid essential tremor (R225C).
- **Recovery potential:** high — most patients improve substantially without disease‑modifying therapy.
- **Prognostic factors:** specific variant (biophysical severity), presence of GI/tremor features; **age** is the dominant prognostic factor (improvement over time). No validated prognostic biomarker.

---

## 12. Treatment

*No disease‑specific approved therapy; management is symptomatic and the condition is largely self‑limiting.*

- **Supportive care (first‑line):** **warming** affected limbs (relieves pain), **avoidance of cold and fatigue** (Noguchi 2017, PMID 30549873). NCIT: Supportive Care (C15272).
- **Pharmacotherapy (off‑label, symptomatic):** simple analgesics/**NSAIDs**; **state‑dependent sodium‑channel blockers** — **carbamazepine**, **lidocaine**, **mexiletine**. Carbamazepine can act as an **activation modulator** that partially normalizes gain‑of‑function sodium‑channel gating (Han 2018, PMID 30135145). NCIT: Carbamazepine (C376), Lidocaine, Mexiletine, NSAID (C198).
- **Pharmacogenomics / precision medicine:** genotype‑guided rationale — GoF NaV1.9 is the direct target; **NaV1.9‑selective blockers are investigational** (preclinical/early development), highlighted for cold pain and small‑fiber neuropathy (Chen 2025, PMID 40206072). PRMT7 inhibition (e.g., DS‑437) reduces NaV1.9 currents and pain hypersensitivity in mice — a candidate strategy (Ma 2022, PMID 34326297). Transcutaneous **cholesterol** reversed NaV1.9‑mediated hypersensitivity in models (Amsalem 2018, PMID 29459435).
- **Advanced therapeutics (gene/cell/RNA):** none in clinical use; conceptually amenable to allele‑selective ASO/gene‑editing given the dominant GoF mechanism (future direction).
- **Surgical/interventional:** not applicable.
- **Treatment outcomes/adverse events:** no controlled trial data; management guided by general neuropathic‑pain practice and drug‑specific safety profiles.

---

## 13. Prevention

- **Primary prevention:** not possible (germline genetic cause); **preconception/prenatal genetic counseling** and options (PGT/prenatal testing) can prevent transmission where desired.
- **Secondary prevention:** **cascade genetic testing** of relatives for early recognition; early trigger‑avoidance counseling.
- **Tertiary prevention:** minimize episode burden via **avoidance of cold/fatigue** and prompt warming; manage variant‑specific complications (e.g., constipation).
- **Immunization / public‑health / environmental interventions:** not applicable.
- **Counseling:** **genetic counseling** for autosomal‑dominant 50% recurrence risk and variable expressivity is central. NCIT: Genetic Counseling (C15311).
- **Prophylaxis:** no established prophylactic drug; behavioral trigger avoidance is the mainstay.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** human *SCN11A* (NaV1.9). Mouse ***Scn11a*** — NCBI Gene 24046; MGI:1345149 (Chr 9). Rat *Scn11a* ortholog exists. NaV1.9 (originally NaN/SNS2) is **evolutionarily conserved** across mammals with conserved nociceptor‑restricted expression.
- **Natural disease in other species:** **no naturally occurring animal disease** cataloged in OMIA for SCN11A episodic pain; disease knowledge in animals comes from **engineered models**, not spontaneous veterinary cases.
- **Comparative biology:** mouse NaV1.9 gating and DRG expression closely parallel human, enabling faithful modeling; **conservation of the RMP‑setting/threshold role** underlies the translational validity.
- **Transmission:** not applicable (non‑infectious, non‑zoonotic).

---

## 15. Model Organisms

- **Model type:** mammalian — **mouse (*Mus musculus*, NCBI Taxon 10090)**; plus in‑vitro heterologous expression (HEK293, DRG electroporation) and patient‑derived DRG‑neuron electrophysiology.
- **Genetic models:**
  - **Knock‑in (disease‑variant) mice:** **Scn11a‑R222S** — hypersensitive to hot and cold stimuli, increased DRG input impedance and evoked AP firing (Noguchi 2017, PMID 30549873). **F802C** and **F1125S** (orthologues of human F814C/F1146S) — elevated RMP and increased AP firing to high input current; F1125S also increases firing probability at low input (Kabata 2018, PMID 30557356). **A796G** knock‑in used in modifier studies (Ma 2022, PMID 34326297).
  - **Knockout (loss‑of‑function) mice:** **NaV1.9‑null** — reduced nociceptor excitability, +55% C‑fiber electrical threshold, higher mechanical thresholds, impaired noxious heat sensing (Hoffmann 2017, PMID 27780178); attenuated visceral afferent activation (Hockley 2014, PMID 24972070); NaV1.8/NaV1.9 double‑KO mildly affects acute pain and deregulates C‑LTMR/neuropeptide genes (Alves‑Simões 2025, PMID 39382328).
- **Phenotype recapitulation:** **strong** — GoF knock‑ins reproduce the cardinal DRG hyperexcitability and thermal/cold hypersensitivity; reciprocal KO produces the opposite (hyposensitivity), establishing causality bidirectionally.
- **Limitations:** mice model **peripheral electrophysiology and behavioral proxies**, not the subjective, episodic, weather‑triggered nature of human pain or its spontaneous adolescent remission; genetic background and orthologue‑residue differences require care.
- **Applications:** target validation, variant functional classification, and testing of NaV1.9‑directed and modifier (PRMT7, cholesterol) therapeutics.
- **Resources:** MGI/IMPC/IMSR for *Scn11a* alleles.

---

## Supported and Refuted Hypotheses

**Supported:**
1. The lower‑limb‑predominant FEPS is a **NaV1.9 (SCN11A) gain‑of‑function channelopathy** (multiple kindreds + electrophysiology + mouse models).
2. **Nociceptor RMP depolarization → hyperexcitability** is the mechanistic core (in vitro + KI/KO).
3. **Autosomal‑dominant** inheritance with a **Japanese R222H founder** effect.
4. **Cold/fatigue trigger episodes via physiological modulation of NaV1.9.**
5. **Benign, age‑attenuating natural history.**

**Refuted / excluded:**
- Not caused by tissue damage, inflammation‑as‑primary, infection, or structural/chromosomal abnormality.
- Not an erythromelalgia phenotype (patients feel **cold**, relieved by warmth — the inverse of erythromelalgia).

## Limitations & Future Directions
- No population‑level prevalence, sex‑ratio, or QoL‑instrument data; cohorts are small and geographically skewed (Japan/China).
- Ambiguity in whether the exact source label ("predominantly lower limb") intends **FEPS3 (SCN11A)** vs **FEPS2 (SCN10A)** — both cause distal, predominantly lower‑limb episodic pain; FEPS3 is the best‑characterized match and the primary focus here, with FEPS2 covered as the close alternative.
- No controlled treatment trials; **NaV1.9‑selective analgesics and allele‑selective genetic therapies** are the key future opportunities.

---

*Evidence source key: human clinical (pedigrees/case series) — PMIDs 30549873, 30557356, 31551682, 28298626, 39058404, 26645915; in vitro/electrophysiology — 39836077, 30135145, 34326297, 29459435; mouse models — 30549873, 30557356, 27780178, 24972070, 39382328; reviews — 36051609, 29299961, 40206072.*


## Artifacts

- [OpenScientist final report](Familial_Episodic_Pain_Syndrome_With_Predominantly_Lower_Limb_Involvement-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Familial_Episodic_Pain_Syndrome_With_Predominantly_Lower_Limb_Involvement-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 25 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0025277` (1 mention) - the report calls it "Fluctuating course/episodic — episodic pain"; HP calls it **Gustatory sweating**
- `HP:0003394` (1 mention) - the report calls it "limb pain — muscle pain proxy"; HP calls it **Muscle spasm**
- `HP:0500152` (1 mention) - the report calls it "Cold‑induced pain/temperature sensitivity"; HP calls it **Hypocystinemia**
- `GO:0045211` (1 mention) - the report calls it "axon/terminal"; GO calls it **postsynaptic membrane**
- `UBERON:0001132` (1 mention) - the report calls it "trigeminal ganglion"; UBERON calls it **parathyroid gland**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002829` (1 mention) - the report calls it "Arthralgia — joint pain"; HP calls it **Arthralgia**, and lists "Arthritic pain" among its other names
- `GO:0005248` (1 mention) - the report calls it "voltage‑gated sodium channel activity, MF"; GO calls it **voltage-gated sodium channel activity**
- `GO:0050966` (1 mention) - the report calls it "detection of noxious stimulus"; GO calls it **detection of mechanical stimulus involved in sensory perception of pain**, and lists "perception of pain, detection of mechanical stimulus" among its other names
- `CL:0000101` (2 mentions) - the report calls it "sensory/DRG neuron", "sensory neuron"; CL calls it **sensory neuron**
- `CL:0011103` (1 mention) - the report calls it "enteric neuron"; CL calls it **sympathetic neuron**
- `UBERON:0002240` (1 mention) - the report calls it "spinal cord dorsal horn, downstream"; UBERON calls it **spinal cord**, and lists "spinal cord structure" among its other names
- `UBERON:0003823` (1 mention) - the report calls it "leg"; UBERON calls it **hindlimb zeugopod**, and lists "leg" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000101` - called "sensory/DRG neuron", "sensory neuron"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.