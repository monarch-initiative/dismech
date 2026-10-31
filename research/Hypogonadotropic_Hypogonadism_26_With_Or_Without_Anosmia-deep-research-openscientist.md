---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-19T04:48:44.513277'
end_time: '2026-10-19T05:06:05.012531'
duration_seconds: 1040.5
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hypogonadotropic Hypogonadism 26 With or Without Anosmia
  mondo_id: MONDO:0030534
  category: Mendelian
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
citation_count: 31
reference_validation:
  total_references: 31
  verified: 31
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 31
  on_topic: 12
  off_topic: 1
  off_topic_references:
  - PMID:34753367
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 27
  verified: 25
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 7
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: HP:0000044
    reported_labels:
    - Lab/clinical
    ontology_label: Hypogonadotropic hypogonadism
  - term_id: HP:0000458
    reported_labels:
    - Clinical sign
    ontology_label: Anosmia
  - term_id: HP:0000054
    reported_labels:
    - Physical
    ontology_label: Micropenis
  - term_id: HP:0000028
    reported_labels:
    - Physical
    ontology_label: Cryptorchidism
  - term_id: HP:0008734
    reported_labels:
    - Physical
    ontology_label: Decreased testicular size
  - term_id: HP:0001363
    reported_labels:
    - Physical
    ontology_label: Craniosynostosis
  - term_id: UBERON:0001301
    reported_labels:
    - preoptic area
    ontology_label: epididymis
  labels_variant: 4
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
  path: Hypogonadotropic_Hypogonadism_26_With_Or_Without_Anosmia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hypogonadotropic_Hypogonadism_26_With_Or_Without_Anosmia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypogonadotropic Hypogonadism 26 With or Without Anosmia
- **MONDO ID:** MONDO:0030534 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypogonadotropic Hypogonadism 26 With or Without Anosmia** covering all of the
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

# Hypogonadotropic Hypogonadism 26 With or Without Anosmia (HH26): Comprehensive Disease Characterization Report

**Disease:** Hypogonadotropic Hypogonadism 26 With or Without Anosmia
**MONDO ID:** MONDO:0030534 | **OMIM:** #619718 | **Causal gene:** TCF12 (HGNC:11623)
**Category:** Mendelian (congenital GnRH deficiency / Kallmann syndrome)

---

## Summary

Hypogonadotropic Hypogonadism 26 with or without anosmia (**HH26**; OMIM #619718, MONDO:0030534) is a rare Mendelian form of congenital isolated GnRH deficiency (isolated gonadotropin-releasing hormone deficiency, IGD) caused by **loss-of-function (haploinsufficiency) variants in TCF12**, a class I basic helix-loop-helix (bHLH) "E-protein" transcription factor located on chromosome 15q21. It was defined by Davis and colleagues in 2020, who reported 13 families (12 autosomal dominant and 1 autosomal recessive) carrying loss-of-function TCF12 mutations and presenting with an **anosmic form of IGD — i.e., Kallmann syndrome** ([PMID: 32620954](https://pubmed.ncbi.nlm.nih.gov/32620954/)). Notably, TCF12 was already a well-established cause of coronal craniosynostosis, so HH26 represents a second, developmentally distinct phenotype arising from reduced TCF12 dosage.

Mechanistically, TCF12 acts through bHLH heterodimerization. As a class I E-protein it partners with class II bHLH factors such as TWIST1 and ASCL1, and these dosage-sensitive dimer combinations govern neural crest and craniofacial development as well as the embryonic specification, differentiation, and migration of GnRH neurons. GnRH (LHRH) neurons originate in the olfactory/nasal placode and migrate along terminal/vomeronasal/olfactory nerve scaffolds across the nasal septum into the forebrain (preoptic area/hypothalamus). When this developmental program fails — combined with olfactory bulb agenesis/hypoplasia — the result is the dual phenotype of **hypogonadotropic hypogonadism plus anosmia** that defines Kallmann syndrome. In zebrafish, loss of *tcf12* perturbs GnRH neuronal patterning and attenuates orthologous *tcf3a/b* and *stub1*, with restored *STUB1* mRNA rescuing the *tcf12* loss, directly linking TCF12 to a mechanistic network of IGD genes.

Clinically, HH26 presents as absent/incomplete puberty with low sex steroids and inappropriately low/normal gonadotropins. The reported cohort was strongly male-predominant (13 males, 1 female), consistent with the broader Kallmann syndrome sex skew. The condition is **lifelong but treatable** with sex-steroid-based pubertal induction and gonadotropin or pulsatile GnRH therapy for fertility; approximately **10–20% of congenital HH patients undergo spontaneous reversal** of HPG-axis function. There is no gene-specific or curative therapy. This report compiles disease information, etiology, phenotypes, genetics, mechanism, anatomy, temporal development, epidemiology, diagnostics, prognosis, treatment, prevention, and model-organism data across the 15 requested domains, flagging where HH26-specific evidence is sparse and general Kallmann syndrome/CHH evidence is used by extension.

---

## Key Findings

### Finding 1 — HH26 is caused by loss-of-function variants in TCF12

OMIM #619718 defines HH26 as caused by heterozygous mutation in **TCF12** (gene MIM 600480; HGNC:11623; chromosome 15q21), with one homozygous (autosomal recessive) patient reported. The defining clinical-genetic study, *TCF12 haploinsufficiency causes autosomal dominant Kallmann syndrome and reveals network-level interactions between causal loci* (Davis et al. 2020), reported **13 families (12 autosomal dominant and one autosomal recessive)** with an anosmic form of IGD carrying loss-of-function TCF12 mutations. As the authors state verbatim: *"we report 13 families (12 autosomal dominant and one autosomal recessive) with an anosmic form of IGD (Kallmann syndrome) with loss-of-function mutations in TCF12, a locus also known to cause syndromic and non-syndromic craniosynostosis"* ([PMID: 32620954](https://pubmed.ncbi.nlm.nih.gov/32620954/)). This establishes TCF12 loss-of-function as the direct cause, the predominantly autosomal dominant inheritance, and the dual-phenotype relationship with craniosynostosis.

### Finding 2 — TCF12 regulates GnRH neuron patterning via E-protein dimerization, with a defined mechanistic network

TCF12 is a **class I E-protein** that heterodimerizes with class II bHLH proteins such as TWIST1. Sharma et al. (2013) demonstrated that *"TCF12 encodes one of three class I E proteins that heterodimerize with class II bHLH proteins such as TWIST1. We show that TCF12 and TWIST1 act synergistically in a transactivation assay"* ([PMID: 23354436](https://pubmed.ncbi.nlm.nih.gov/23354436/)), establishing the dosage-sensitive synergy underlying both craniosynostosis and, by extension, GnRH-neuron development. In zebrafish, Davis et al. showed that *"loss of tcf12 in zebrafish larvae perturbs GnRH neuronal patterning with concomitant attenuation of the orthologous expression of tcf3a/b, encoding a binding partner of TCF12, and stub1"* ([PMID: 32620954](https://pubmed.ncbi.nlm.nih.gov/32620954/)). Restoring *STUB1* mRNA rescued the *tcf12*-loss phenotype in vivo, connecting TCF12 to STUB1 (itself mutated in syndromic IGD) within a network of interacting causal loci.

### Finding 3 — Phenotype: Kallmann syndrome with strong male predominance; anosmia from olfactory bulb/GnRH neuron developmental failure

The HH26 index cohort comprised **13 males and 1 female** (strong male skew), all with anosmic IGD ([PMID: 32620954](https://pubmed.ncbi.nlm.nih.gov/32620954/)). The anatomical basis is the shared embryonic origin of GnRH neurons and the olfactory system: *"LHRH neurons originate in the medial olfactory placode of the developing nose, migrate across the nasal septum and enter the forebrain with the nervus terminalis, arching into the septal-preoptic area and hypothalamus"* ([PMID: 2645530](https://pubmed.ncbi.nlm.nih.gov/2645530/)). Failed migration combined with olfactory bulb agenesis produces the coupled hypogonadotropic hypogonadism and anosmia (also Cho et al. 2019, [PMID: 31355196](https://pubmed.ncbi.nlm.nih.gov/31355196/)). The broader Kallmann syndrome context: *"KS is a heterogeneous disorder affecting 1 in 5000 males, with a three to fivefold of males over females"* ([PMID: 25071724](https://pubmed.ncbi.nlm.nih.gov/25071724/)).

### Finding 4 — Course: lifelong but reversible in ~10% of males

Approximately **10% of male individuals with CHH undergo reversal** with sustained HPG-axis activation and/or fertility after discontinuing hormonal treatment: *"Approximately 10% of male individuals with CHH undergo reversal with sustained hypothalamic-pituitary-gonadal (HPG) axis activation and/or fertility after discontinuing hormonal treatment"* ([PMID: 41206002](https://pubmed.ncbi.nlm.nih.gov/41206002/)). Genotype influences reversal probability: *"Pathogenic variants in GNRHR favor reversal while ANOS1 variants virtually exclude HPG axis recovery"* ([PMID: 41206002](https://pubmed.ncbi.nlm.nih.gov/41206002/)). In the largest reversal cohort, patients without reversal were more likely to have anosmia, cryptorchidism, complete absence of puberty, and oligogenicity ([PMID: 38437850](https://pubmed.ncbi.nlm.nih.gov/38437850/)). Fertility is achievable with pulsatile GnRH or combined gonadotropin (hCG + FSH) therapy ([PMID: 19912242](https://pubmed.ncbi.nlm.nih.gov/19912242/)).

### Finding 5 — Diagnosis and treatment: biochemical HPG profiling, olfactory/MRI assessment, hormone + gonadotropin therapy

Per the European Consensus Statement (Boehm et al. 2015), CHH is diagnosed by absent/incomplete puberty with low sex steroids and inappropriately low/normal gonadotropins, after excluding other pituitary dysfunction; *"The association of CHH with a defective sense of smell (anosmia or hyposmia), which is found in ∼50% of patients with CHH is termed Kallmann syndrome and results from incomplete embryonic migration of GnRH-synthesizing neurons"* ([PMID: 26194704](https://pubmed.ncbi.nlm.nih.gov/26194704/)). The same consensus notes: *"Patients typically require lifelong treatment, yet ∼10-20% of patients exhibit a spontaneous recovery of reproductive function"* ([PMID: 26194704](https://pubmed.ncbi.nlm.nih.gov/26194704/)). In infancy, inhibin B and AMH measured during minipuberty discriminate CHH (INHB cutoff ~100 pg/mL after 180 days: Se/Sp 100%/100%; [PMID: 40193582](https://pubmed.ncbi.nlm.nih.gov/40193582/)). Gonadotropin therapy in male infants significantly increases penile length and inhibin B and promotes testicular descent in 73% ([PMID: 39673783](https://pubmed.ncbi.nlm.nih.gov/39673783/)).

### Finding 6 — TCF12 variant spectrum (LoF/NMD), reduced penetrance, and animal models

TCF12 craniosynostosis-associated variants are predominantly truncating: of 38 heterozygous variants, 14 nonsense, 15 frameshift, 7 splicing, and 2 missense, with mutant-allele under-expression consistent with nonsense-mediated decay → haploinsufficiency ([PMID: 23354436](https://pubmed.ncbi.nlm.nih.gov/23354436/)). HH26/Kallmann variants are likewise loss-of-function ([PMID: 32620954](https://pubmed.ncbi.nlm.nih.gov/32620954/)). Penetrance is incomplete (craniosynostosis non-penetrance ~47% among variant-carrying relatives), and gnomAD constraint is only modest (pLI≈0.02, LOEUF≈0.61), reflecting incomplete penetrance. Animal models demonstrate dosage sensitivity: *"mice doubly heterozygous for loss-of-function mutations in Tcf12 and Twist1 have severe coronal synostosis"* ([PMID: 23354436](https://pubmed.ncbi.nlm.nih.gov/23354436/)), and *"loss of tcf12 in zebrafish larvae perturbs GnRH neuronal patterning"* ([PMID: 32620954](https://pubmed.ncbi.nlm.nih.gov/32620954/)).

### Finding 7 — TCF12/HEB is an E-protein forming TWIST1 heterodimers that drive neural crest differentiation

Proteomic/transcriptomic profiling shows *"TWIST1 homodimers and heterodimers with TCF3, TCF4, and TCF12 E-proteins are the predominant dimer combinations"* in craniofacial mesenchyme ([PMID: 32179550](https://pubmed.ncbi.nlm.nih.gov/32179550/)), and *"TWIST1-E-protein heterodimers activate the differentiation of mesoderm and neural crest cells, which is accompanied by the epithelial-to-mesenchymal transition"* ([PMID: 32179550](https://pubmed.ncbi.nlm.nih.gov/32179550/)), whereas TWIST1 homodimers maintain the progenitor state. TCF12 (HEB) also heterodimerizes with class II bHLH ASCL1 and E-protein TCF3 ([PMID: 40187474](https://pubmed.ncbi.nlm.nih.gov/40187474/)). Repeated targeted literature searches identified no additional TCF12-specific hypogonadotropic hypogonadism cohorts beyond Davis et al. 2020 — the single-cohort evidence base is a key limitation.

---

## Full Section-by-Section Report

### 1. Disease Information

**Overview.** HH26 is a congenital form of isolated GnRH deficiency presenting as hypogonadotropic hypogonadism, frequently (in the reported cohort, invariably) accompanied by anosmia — i.e., Kallmann syndrome. It is one of the numbered hypogonadotropic hypogonadism loci (HH1–HH>26) distinguished by causal gene; HH26 corresponds to TCF12.

**Key identifiers:**
- **OMIM:** #619718 (Hypogonadotropic hypogonadism 26 with or without anosmia; HH26)
- **Gene MIM:** 600480 (TCF12)
- **MONDO:** MONDO:0030534
- **HGNC:** 11623 (TCF12)
- **Orphanet:** Subsumed under Kallmann syndrome (ORPHA:478) / congenital hypogonadotropic hypogonadism
- **ICD-10:** E23.0 (Hypopituitarism, includes Kallmann syndrome); **ICD-11:** 5A61.0 (Hypogonadotropic hypogonadism)
- **MeSH:** Kallmann Syndrome (D017436); Hypogonadism (D007006)

**Synonyms:** HH26; TCF12-related Kallmann syndrome; TCF12 haploinsufficiency Kallmann syndrome; isolated GnRH deficiency with anosmia (TCF12 type).

**Information source type:** Aggregated disease-level resource (OMIM) derived from a primary multi-family research cohort ([PMID: 32620954](https://pubmed.ncbi.nlm.nih.gov/32620954/)); not EHR-derived.

### 2. Etiology

**Primary cause — genetic.** Loss-of-function variants in **TCF12** (haploinsufficiency), inherited predominantly autosomal dominant (12/13 families), rarely autosomal recessive (1/13) ([PMID: 32620954](https://pubmed.ncbi.nlm.nih.gov/32620954/)).

**Genetic risk/modifier factors.** CHH/Kallmann syndrome is frequently **oligogenic** (10–20% of cases carry >1 rare variant; [PMID: 40958510](https://pubmed.ncbi.nlm.nih.gov/40958510/), [PMID: 29280744](https://pubmed.ncbi.nlm.nih.gov/29280744/)). Network partners/modifiers in the TCF12 network include **STUB1, TCF3 (tcf3a/b orthologs), and TWIST1** ([PMID: 32620954](https://pubmed.ncbi.nlm.nih.gov/32620954/)). Other IGD genes (ANOS1/KAL1, FGFR1, FGF8, PROK2, PROKR2, CHD7, SEMA3A, GNRHR) may act as second hits.

**Environmental risk factors.** No established environmental cause; this is a monogenic developmental disorder. Sex (male predominance) is the principal non-genetic demographic association. Family history is relevant given autosomal dominant inheritance.

**Protective factors.** No validated genetic or environmental protective factors specific to HH26. In CHH generally, GNRHR variants and Pasqualini (fertile eunuch) subtype features associate with higher reversal probability ([PMID: 38437850](https://pubmed.ncbi.nlm.nih.gov/38437850/)).

**Gene-environment interactions.** None established for HH26; the disorder is essentially fully genetically/developmentally determined, with incomplete penetrance likely driven by genetic background (modifiers) rather than environment.

### 3. Phenotypes

| Phenotype | Type | HPO term | Onset | Severity/Frequency |
|---|---|---|---|---|
| Hypogonadotropic hypogonadism | Lab/clinical | HP:0000044 | Congenital | Defining; 100% |
| Anosmia/hyposmia | Clinical sign | HP:0000458 | Congenital | Defining in cohort (anosmic IGD) |
| Absent/delayed puberty | Clinical sign | HP:0000823 / HP:0000826 | Adolescence | High |
| Micropenis | Physical | HP:0000054 | Congenital (male) | Subset of males |
| Cryptorchidism | Physical | HP:0000028 | Congenital (male) | Subset of males |
| Infertility | Clinical | HP:0000789 (male) / HP:0008222 | Adult | High untreated |
| Decreased testicular size | Physical | HP:0008734 | Adolescence/adult | Common |
| Craniosynostosis (allelic) | Physical | HP:0001363 | Congenital | In a subset (TCF12 locus overlap) |

**Characteristics.** Onset is congenital/developmental, manifesting biochemically from fetal/neonatal life (absent minipuberty) and clinically as absent puberty. Severity is variable (consistent with incomplete penetrance). Course is **stable/non-progressive** developmentally but produces lifelong hypogonadism unless treated; ~10–20% reverse. Olfactory bulb hypoplasia/agenesis is detectable on MRI.

**Quality of life.** Untreated CHH impairs sexual development, fertility, bone mineral density, body composition (lower appendicular lean mass relative to FSH; [PMID: 41073368](https://pubmed.ncbi.nlm.nih.gov/41073368/)), and psychosocial well-being; treatment substantially restores secondary sexual characteristics and function.

### 4. Genetic/Molecular Information

**Causal gene:** TCF12 (Transcription Factor 12; alias HEB), HGNC:11623, chromosome 15q21, gene MIM 600480. Encodes a class I bHLH E-protein.

**Pathogenic variants.** Predominantly **loss-of-function / truncating**: nonsense, frameshift, and splice-site variants, plus large deletions/microdeletions (e.g., TCF12 microdeletion from complex chromosomal rearrangement; [PMID: 24648389](https://pubmed.ncbi.nlm.nih.gov/24648389/)). Across the craniosynostosis spectrum, 38 variants comprised 14 nonsense, 15 frameshift, 7 splicing, 2 missense, with mutant-allele under-expression consistent with **nonsense-mediated decay** ([PMID: 23354436](https://pubmed.ncbi.nlm.nih.gov/23354436/)). HH26 variants are likewise LoF ([PMID: 32620954](https://pubmed.ncbi.nlm.nih.gov/32620954/)). Classification: pathogenic/likely pathogenic per ACMG for truncating LoF. **Functional consequence: loss of function via haploinsufficiency** (dosage-sensitive).

**Allele frequency/constraint.** gnomAD constraint is modest (pLI≈0.02, LOEUF≈0.61), reflecting incomplete penetrance and exclusion of pediatric phenotypes from reference cohorts.

**Origin:** Germline (both inherited and de novo reported). No somatic component.

**Modifier genes:** STUB1, TCF3, TWIST1, and broader IGD oligogenic loci ([PMID: 32620954](https://pubmed.ncbi.nlm.nih.gov/32620954/)).

**Epigenetics / chromosomal abnormalities:** No disease-specific methylation signature established. Large structural TCF12 deletions (15q21) via chromosomal rearrangements can cause haploinsufficiency ([PMID: 24648389](https://pubmed.ncbi.nlm.nih.gov/24648389/)).

**Suggested gene/GO annotations:** HGNC:11623 (TCF12); GO:0046983 (protein dimerization activity); GO:0000981 (DNA-binding transcription factor activity, RNA pol II-specific).

### 5. Environmental Information

No environmental, lifestyle, toxic, or infectious agents are implicated in HH26. It is a monogenic developmental disorder. (Not applicable / no evidence.)

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A heterozygous **loss-of-function variant in TCF12** (nonsense/frameshift/splice/deletion) **leads to** degradation of the mutant transcript by nonsense-mediated decay → reduced TCF12 (E-protein) dosage (**haploinsufficiency**) ([PMID: 23354436](https://pubmed.ncbi.nlm.nih.gov/23354436/), [PMID: 32620954](https://pubmed.ncbi.nlm.nih.gov/32620954/)).
2. Reduced TCF12 **results in** deficient availability of class I E-protein for heterodimerization with class II bHLH partners (TWIST1, ASCL1) and with other E-proteins (TCF3) ([PMID: 23354436](https://pubmed.ncbi.nlm.nih.gov/23354436/), [PMID: 40187474](https://pubmed.ncbi.nlm.nih.gov/40187474/)).
3. Diminished bHLH heterodimer activity **leads to** impaired transcriptional programs required for neural-crest/placode-derived development. **[Branch A — craniofacial]** In cranial suture mesenchyme, reduced TWIST1–TCF12 dimer activity **results in** premature suture fusion → coronal craniosynostosis ([PMID: 32179550](https://pubmed.ncbi.nlm.nih.gov/32179550/), [PMID: 23354436](https://pubmed.ncbi.nlm.nih.gov/23354436/)). **[Branch B — reproductive/olfactory]** In the olfactory placode, reduced bHLH activity **leads to** defective specification, differentiation, and migration of GnRH neurons and defective olfactory bulb formation (*inferred from zebrafish; direct human developmental demonstration lacking*) ([PMID: 32620954](https://pubmed.ncbi.nlm.nih.gov/32620954/)).
4. In the reproductive branch, impaired GnRH-neuron patterning **results in** failure of GnRH neurons to migrate from the nasal placode along terminal/vomeronasal/olfactory nerve scaffolds into the hypothalamus ([PMID: 2645530](https://pubmed.ncbi.nlm.nih.gov/2645530/), [PMID: 31355196](https://pubmed.ncbi.nlm.nih.gov/31355196/)).
5. Absence of hypothalamic GnRH neurons **leads to** deficient pulsatile GnRH secretion → inadequate pituitary LH/FSH → low sex steroids = **hypogonadotropic hypogonadism** ([PMID: 26194704](https://pubmed.ncbi.nlm.nih.gov/26194704/)).
6. Concurrent olfactory bulb agenesis/hypoplasia **results in** anosmia; the combination **manifests** as Kallmann syndrome ([PMID: 26194704](https://pubmed.ncbi.nlm.nih.gov/26194704/), [PMID: 23760293](https://pubmed.ncbi.nlm.nih.gov/23760293/)).
7. Network modifier step: TCF12 loss **attenuates** *tcf3a/b* and *stub1*; restoring *STUB1* **rescues** the phenotype, indicating TCF12 operates within an interacting IGD gene network (*demonstrated in zebrafish*) ([PMID: 32620954](https://pubmed.ncbi.nlm.nih.gov/32620954/)).

```
TCF12 LoF variant
      │ (NMD → haploinsufficiency)
      ▼
Reduced E-protein dosage ──► ↓ bHLH heterodimers (TWIST1/ASCL1/TCF3)
      │                                   │
      ├── Branch A: cranial suture ──► premature fusion ──► craniosynostosis
      │
      └── Branch B: olfactory placode
                 │ ↓ GnRH neuron specification/migration + OB agenesis
                 ▼
          GnRH neurons absent in hypothalamus
                 │
      ┌──────────┴──────────┐
      ▼                      ▼
  ↓ GnRH pulses         Olfactory bulb failure
      ▼                      ▼
  ↓ LH/FSH → ↓ sex      Anosmia
   steroids
      └──────────┬──────────┘
                 ▼
         KALLMANN SYNDROME (HH26)
```

**Molecular pathways:** bHLH transcriptional network; FGF8/FGFR1 signaling is a parallel/intersecting pathway required for GnRH neuron emergence ([PMID: 18566132](https://pubmed.ncbi.nlm.nih.gov/18566132/)). **Cellular processes:** neuronal differentiation, neuronal migration, EMT of neural crest ([PMID: 32179550](https://pubmed.ncbi.nlm.nih.gov/32179550/)). **Protein dysfunction:** loss of function via reduced dimerization-competent E-protein. **Cell types:** GnRH (LHRH) neurons; olfactory ensheathing/placodal cells; cranial neural crest; suture mesenchyme.

**Suggested ontology terms:** GO:0007399 (nervous system development); GO:0001764 (neuron migration); GO:0021772 (olfactory bulb development); GO:0030154 (cell differentiation); GO:0046983 (protein dimerization activity); CL:0000029 (neural crest cell); neuron (GnRH neuron); UBERON:0002264 (olfactory placode).

### 7. Anatomical Structures Affected

- **Organ/system level:** Endocrine (hypothalamic-pituitary-gonadal axis), nervous (olfactory system), reproductive (gonads). Primary: hypothalamus (absent GnRH neurons), olfactory bulb. Secondary: pituitary (reduced gonadotrope stimulation), testes/ovaries (hypogonadism), bone (reduced BMD), skeleton/skull (craniosynostosis subset).
- **Tissue/cell level:** GnRH (LHRH) neurons (olfactory-placode-derived); olfactory sensory neurons; cranial neural crest / suture mesenchyme. CL terms: GnRH neuron; CL:0000029 (neural crest cell).
- **Subcellular:** Nucleus (GO:0005634) — site of TCF12 transcriptional activity; DNA-binding transcription factor complex.
- **Localization / UBERON:** UBERON:0002264 (olfactory placode); olfactory bulb; UBERON:0001898 (hypothalamus); UBERON:0001301 (preoptic area); UBERON:0000990 (reproductive system). Lateralization: bilateral (olfactory bulbs may be asymmetric/unilaterally hypoplastic in some KS; [PMID: 23760293](https://pubmed.ncbi.nlm.nih.gov/23760293/)).

### 8. Temporal Development

- **Onset:** Congenital (developmental defect in embryogenesis); biochemically evident in neonatal minipuberty (absent gonadotropin/testosterone surge), clinically at expected puberty.
- **Onset pattern:** Chronic/insidious; non-acute.
- **Progression:** Developmentally stable (non-progressive lesion); hypogonadism is persistent lifelong without treatment.
- **Course pattern:** Chronic lifelong; a minority (~10–20%) show spontaneous reversal ([PMID: 26194704](https://pubmed.ncbi.nlm.nih.gov/26194704/), [PMID: 38437850](https://pubmed.ncbi.nlm.nih.gov/38437850/)).
- **Critical periods:** Fetal GnRH-neuron migration window (irreversible developmental defect); neonatal **minipuberty** (1–6 months) is a key diagnostic and therapeutic window ([PMID: 41880614](https://pubmed.ncbi.nlm.nih.gov/41880614/), [PMID: 39673783](https://pubmed.ncbi.nlm.nih.gov/39673783/)); adolescence for pubertal induction.

### 9. Inheritance and Population

- **Epidemiology:** No HH26-specific prevalence. Kallmann syndrome overall affects ~**1 in 5,000 males**, with a **3–5 fold male predominance** ([PMID: 25071724](https://pubmed.ncbi.nlm.nih.gov/25071724/)). HH26 is a rare subset of this.
- **Inheritance pattern:** Predominantly **autosomal dominant** (12/13 families); rare autosomal recessive (1/13) ([PMID: 32620954](https://pubmed.ncbi.nlm.nih.gov/32620954/)).
- **Penetrance:** **Incomplete** (by analogy with TCF12 craniosynostosis non-penetrance ~47% among variant carriers; [PMID: 23354436](https://pubmed.ncbi.nlm.nih.gov/23354436/)).
- **Expressivity:** Variable (anosmic vs normosmic; ± craniosynostosis; severity of reproductive phenotype).
- **Anticipation:** Not applicable (not a repeat-expansion disorder).
- **Founder effects / consanguinity:** None established for TCF12; consanguinity relevant only to the single AR family.
- **Sex ratio:** Strongly male-predominant in the HH26 cohort (13:1) and in KS generally (3–5:1 M:F).
- **Carrier frequency:** Not established; incomplete penetrance complicates estimation.

### 10. Diagnostics

**Clinical/laboratory tests:**
- Basal hormones: low testosterone/estradiol with **inappropriately low or normal LH/FSH** ([PMID: 26194704](https://pubmed.ncbi.nlm.nih.gov/26194704/)).
- Infancy (minipuberty window): **inhibin B** and **AMH** discriminate CHH — INHB ~100 pg/mL after 180 days gives Se/Sp 100%/100% ([PMID: 40193582](https://pubmed.ncbi.nlm.nih.gov/40193582/)).
- GnRH/GnRH-analog stimulation tests; inhibin B as Sertoli-cell marker.
- **Smell testing** (e.g., BSIT/UPSIT) to classify anosmia/hyposmia ([PMID: 23760293](https://pubmed.ncbi.nlm.nih.gov/23760293/)).
- **MRI of olfactory structures:** olfactory bulb/sulcus hypoplasia or agenesis (found in ~40–85% of KS; [PMID: 23760293](https://pubmed.ncbi.nlm.nih.gov/23760293/), [PMID: 25883924](https://pubmed.ncbi.nlm.nih.gov/25883924/)); pituitary MRI to exclude structural lesions.

**Genetic testing:** NGS **gene panels** for IGD/CHH (46–60+ genes including TCF12) ([PMID: 40508017](https://pubmed.ncbi.nlm.nih.gov/40508017/), [PMID: 34198905](https://pubmed.ncbi.nlm.nih.gov/34198905/)); **WES/WGS** for novel/network discovery; chromosomal microarray to detect TCF12 15q21 deletions ([PMID: 24648389](https://pubmed.ncbi.nlm.nih.gov/24648389/)). Variant interpretation per ACMG/AMP.

**Clinical criteria:** European Consensus — absent/incomplete puberty + low sex steroids + low/normal gonadotropins, excluding other pituitary dysfunction ([PMID: 26194704](https://pubmed.ncbi.nlm.nih.gov/26194704/)). **Differential diagnosis:** constitutional delay of growth and puberty (CDGP — major pitfall), functional hypothalamic hypogonadism, combined pituitary hormone deficiency, CHARGE syndrome (CHD7), other syndromic IGD (SEMA3A, FGFR1).

**Screening:** Cascade genetic testing of relatives given autosomal dominant inheritance; newborn/minipuberty hormonal screening in at-risk infants.

### 11. Outcome / Prognosis

- **Survival/mortality:** Not a life-limiting disorder; **normal life expectancy** with treatment. No disease-specific mortality.
- **Morbidity:** Infertility, osteoporosis/low BMD, altered body composition (reduced lean mass; [PMID: 41073368](https://pubmed.ncbi.nlm.nih.gov/41073368/)), psychosocial impact of delayed/absent puberty.
- **Recovery:** ~10–20% spontaneous reversal; fertility achievable in the majority with gonadotropin/pulsatile GnRH therapy ([PMID: 26194704](https://pubmed.ncbi.nlm.nih.gov/26194704/), [PMID: 19912242](https://pubmed.ncbi.nlm.nih.gov/19912242/)).
- **Prognostic factors for reversal:** Larger testicular volume, no micropenis, higher FSH (Pasqualini subtype), GNRHR variants favor reversal; anosmia, cryptorchidism, complete absence of puberty, oligogenicity, and ANOS1 variants predict non-reversal ([PMID: 38437850](https://pubmed.ncbi.nlm.nih.gov/38437850/)).

### 12. Treatment

**Pharmacotherapy / hormone replacement:**
- **Testosterone** (males) for pubertal induction and maintenance (NCIT:C2281); **estrogen + progesterone** (females) ([PMID: 38683021](https://pubmed.ncbi.nlm.nih.gov/38683021/)).
- **Fertility induction:** pulsatile **GnRH** or **gonadotropins — hCG + FSH** ([PMID: 19912242](https://pubmed.ncbi.nlm.nih.gov/19912242/)); in women, ovulation induction/IVF ([PMID: 37170100](https://pubmed.ncbi.nlm.nih.gov/37170100/), [PMID: 34753367](https://pubmed.ncbi.nlm.nih.gov/34753367/), [PMID: 42633415](https://pubmed.ncbi.nlm.nih.gov/42633415/)).
- **Infant gonadotropin therapy** during minipuberty increases penile length, inhibin B, and promotes testicular descent (73%) ([PMID: 39673783](https://pubmed.ncbi.nlm.nih.gov/39673783/), [PMID: 38924109](https://pubmed.ncbi.nlm.nih.gov/38924109/)).

**Advanced/experimental:** No gene therapy, cell therapy, RNA therapy, or TCF12-targeted therapy exists. Treatment is symptomatic hormone replacement.

**Treatment strategy:** Individualized by age, sex, and fertility goals; combination hCG+FSH; genotype-informed counseling about reversal probability. Lifelong monitoring with periodic trial off-treatment to detect reversal.

**Side effects:** Standard androgen/estrogen/gonadotropin adverse effects; prolonged childhood testosterone may complicate later fertility induction if gonadotropin therapy is delayed ([PMID: 42299415](https://pubmed.ncbi.nlm.nih.gov/42299415/)).

**NCIT suggestions:** Testosterone therapy (NCIT:C2281); Gonadotropin therapy; Hormone replacement therapy (NCIT:C15417).

### 13. Prevention

- **Primary prevention:** Not possible (congenital genetic disorder).
- **Secondary prevention / early detection:** Minipuberty hormonal screening (inhibin B, AMH) in at-risk infants ([PMID: 40193582](https://pubmed.ncbi.nlm.nih.gov/40193582/)); early diagnosis enables timely pubertal induction and fertility preservation.
- **Tertiary prevention:** Hormone replacement prevents osteoporosis and metabolic/body-composition sequelae; fertility therapy addresses infertility.
- **Genetic counseling:** Essential given autosomal dominant inheritance with incomplete penetrance; cascade testing; prenatal/preimplantation genetic testing possible where a familial variant is known.
- **Immunization/public health:** Not applicable.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** Human TCF12 (NCBI Gene 6938); mouse *Tcf12* (NCBI Gene 21406); zebrafish *tcf12*. Highly conserved bHLH E-protein family.
- **Natural disease:** No well-characterized spontaneous animal disease corresponding to HH26; information derives from engineered models.
- **Comparative biology:** The GnRH-neuron olfactory-placode origin and migration is conserved across vertebrates ([PMID: 9915559](https://pubmed.ncbi.nlm.nih.gov/9915559/), [PMID: 2645530](https://pubmed.ncbi.nlm.nih.gov/2645530/)); E-protein/TWIST1 bHLH dimerization is deeply conserved.
- **Zoonotic potential:** Not applicable.

### 15. Model Organisms

| Model | Type | Finding | Reference |
|---|---|---|---|
| Zebrafish *tcf12* loss | Vertebrate | Perturbed GnRH neuronal patterning; attenuated *tcf3a/b*, *stub1*; rescued by *STUB1* mRNA | [PMID: 32620954](https://pubmed.ncbi.nlm.nih.gov/32620954/) |
| *Tcf12+/−;Twist1+/−* mouse | Mammalian | Severe coronal craniosynostosis (dosage-sensitive genetic interaction) | [PMID: 23354436](https://pubmed.ncbi.nlm.nih.gov/23354436/) |
| FNC-B4 human GnRH neuroblasts | In vitro | GnRH expression/migration regulated by androgen/leptin (reversal mechanism) | [PMID: 19040620](https://pubmed.ncbi.nlm.nih.gov/19040620/) |

**Phenotype recapitulation:** The zebrafish model directly recapitulates the GnRH-neuron developmental defect central to HH26 and demonstrates the mechanistic network (STUB1 rescue). The mouse double-heterozygote captures the craniosynostosis (allelic) branch and the haploinsufficiency/dosage mechanism. **Limitations:** No published mouse model of the HH26 reproductive phenotype specifically; zebrafish cannot fully model human hypothalamic-pituitary endocrinology.

---

## Mechanistic Model / Interpretation

The unifying theme of HH26 is **dosage-sensitive bHLH transcriptional control of neural-crest/placode-derived development**. TCF12 is one of three class I E-proteins; it functions only as a dimer. By partnering with TWIST1 (and ASCL1, TCF3), it builds transcriptional complexes that drive two spatially distinct developmental programs: cranial suture/neural-crest differentiation (craniofacial branch) and GnRH-neuron specification/migration coupled to olfactory bulb formation (reproductive-olfactory branch). Because the system is haploinsufficient, a single truncating allele — degraded by nonsense-mediated decay — drops functional E-protein below the threshold needed for one or both programs, explaining why the **same gene produces either craniosynostosis or Kallmann syndrome (or both)** and why **penetrance is incomplete** (genetic-background modifiers tune whether a given tissue crosses its threshold).

The reproductive phenotype flows from a developmental "experiment of nature": GnRH neurons are uniquely born outside the brain in the olfactory placode and must migrate into the hypothalamus along olfactory/terminal nerve scaffolds. TCF12 insufficiency derails this migration (shown in zebrafish) at the same time olfactory bulbs fail to form — hence the obligate coupling of hypogonadism and anosmia. The zebrafish STUB1-rescue result is the strongest mechanistic evidence that TCF12 does not act alone but anchors an interacting network of IGD loci, rationalizing the oligogenic architecture seen across CHH.

Downstream, the clinical picture is entirely predictable from "no hypothalamic GnRH neurons": no GnRH pulses → low LH/FSH → low sex steroids → absent puberty, micropenis/cryptorchidism in males, and infertility — all **bypassable** pharmacologically by supplying the missing downstream signals (GnRH, gonadotropins, sex steroids), which is why the disorder is treatable despite being developmental and why a minority reverse when residual GnRH neurons mature.

---

## Evidence Base

| PMID | Role | Key contribution |
|---|---|---|
| [32620954](https://pubmed.ncbi.nlm.nih.gov/32620954/) | Defining | TCF12 LoF causes AD Kallmann syndrome (13 families); zebrafish GnRH patterning defect; STUB1 network/rescue |
| [23354436](https://pubmed.ncbi.nlm.nih.gov/23354436/) | Mechanism | TCF12 E-protein/TWIST1 synergy; truncating variant spectrum → NMD/haploinsufficiency; mouse Tcf12/Twist1 synostosis |
| [32179550](https://pubmed.ncbi.nlm.nih.gov/32179550/) | Mechanism | TWIST1–TCF12 heterodimers drive neural crest differentiation/EMT |
| [40187474](https://pubmed.ncbi.nlm.nih.gov/40187474/) | Mechanism | TCF12 (HEB) heterodimerizes with ASCL1 and TCF3 |
| [2645530](https://pubmed.ncbi.nlm.nih.gov/2645530/) | Anatomy/dev | GnRH neurons originate in olfactory placode, migrate to hypothalamus |
| [31355196](https://pubmed.ncbi.nlm.nih.gov/31355196/) | Anatomy/dev | Nasal placode development, GnRH migration, Kallmann syndrome review |
| [18566132](https://pubmed.ncbi.nlm.nih.gov/18566132/) | Mechanism | FGF8/FGFR1 required for GnRH neuron emergence (parallel pathway) |
| [25071724](https://pubmed.ncbi.nlm.nih.gov/25071724/) | Epidemiology | KS ~1/5000 males, 3–5× male predominance |
| [26194704](https://pubmed.ncbi.nlm.nih.gov/26194704/) | Diagnosis/Tx | European Consensus: CHH/KS definition, ~50% anosmia, lifelong treatment, 10–20% reversal |
| [38437850](https://pubmed.ncbi.nlm.nih.gov/38437850/) | Prognosis | Two reversal classes; genotype/phenotype predictors |
| [41206002](https://pubmed.ncbi.nlm.nih.gov/41206002/) | Prognosis | ~10% male reversal; GNRHR favors, ANOS1 excludes reversal |
| [40193582](https://pubmed.ncbi.nlm.nih.gov/40193582/) | Diagnosis | Inhibin B/AMH diagnose CHH in infancy |
| [39673783](https://pubmed.ncbi.nlm.nih.gov/39673783/) | Treatment | Infant gonadotropin therapy promotes testicular descent (73%) |
| [19912242](https://pubmed.ncbi.nlm.nih.gov/19912242/) | Treatment | Pulsatile GnRH/gonadotropins for fertility |
| [24648389](https://pubmed.ncbi.nlm.nih.gov/24648389/) | Genetics | TCF12 15q21 microdeletion causes haploinsufficiency |

**Consistency:** The TCF12→Kallmann causal link rests on a **single primary cohort** (Davis et al. 2020) reinforced by independent craniosynostosis genetics and conserved developmental biology. The mechanistic (E-protein/TWIST1, GnRH migration) and clinical (CHH diagnosis/treatment/prognosis) literature is robust and convergent.

---

## Limitations and Knowledge Gaps

1. **Single-cohort causal evidence.** The entire TCF12–HH26 association derives from one study ([PMID: 32620954](https://pubmed.ncbi.nlm.nih.gov/32620954/)). Repeated targeted searches found no independent replication cohort. ClinGen gene-disease validity for TCF12–HH is therefore likely limited/moderate rather than definitive.
2. **No HH26-specific epidemiology.** Prevalence, incidence, penetrance, and expressivity figures are extrapolated from Kallmann syndrome/CHH generally.
3. **Human mechanism inferred from zebrafish.** The GnRH-neuron migration defect is demonstrated in zebrafish, not in human tissue; the olfactory-bulb/placode step in humans is inferred.
4. **Genotype–phenotype relationships** (anosmic vs normosmic, ± craniosynostosis) within TCF12 carriers are not well characterized.
5. **No disease-specific treatment or model** for the reproductive phenotype; no epigenetic, proteomic, or metabolomic profiling specific to HH26.
6. **Female phenotype** is poorly characterized (only 1 female in the defining cohort).

---

## Proposed Follow-up Experiments / Actions

1. **Replication cohort / variant curation.** Query large IGD/CHH sequencing datasets (GeneMatcher, DECIPHER, ClinVar) for additional TCF12 LoF carriers to strengthen gene-disease validity and define the variant spectrum and penetrance.
2. **Conditional mouse model** of *Tcf12* loss in GnRH neurons / olfactory placode to directly test the reproductive branch in a mammal and quantify phenotype recapitulation.
3. **Human iPSC-derived GnRH neuron / olfactory placode organoids** carrying patient TCF12 variants to confirm the migration/differentiation defect in human cells.
4. **Network validation.** Test the TCF12–STUB1–TCF3–TWIST1 interaction in GnRH-neuron contexts (co-IP, ChIP-seq, CRISPR epistasis) to map direct transcriptional targets.
5. **Genotype–phenotype study** correlating TCF12 variant type/position with anosmia, craniosynostosis, reversal, and sex differences.
6. **Reversal biomarker study** in TCF12-genotyped patients to test whether TCF12 variants behave like GNRHR (favoring reversal) or ANOS1 (excluding it).

---

*Report compiled from 7 confirmed findings and 46 reviewed papers over a 5-iteration autonomous investigation. Evidence source types: human clinical (cohort/consensus), model organism (zebrafish, mouse), in vitro (human GnRH neuroblasts), and computational (gnomAD constraint).*


## Artifacts

- [OpenScientist final report](Hypogonadotropic_Hypogonadism_26_With_Or_Without_Anosmia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hypogonadotropic_Hypogonadism_26_With_Or_Without_Anosmia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 31 |
| On topic | 12 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:34753367` (3 mentions) - Management of congenital hypogonadotropic hypogonadism in females.
  - shared terms: hypogonadism

Weighed against this report's own most characteristic terms: `tcf12`, `gnrh`, `hh26`, `variant`, `craniosynostosis`, `kallmann`, `syndrome`, `anosmia`, `twist1`, `phenotype`, `hypogonadism`, `olfactory`, `gene`, `igd`, `migration`, `male`, `cohort`, `chh`, `zebrafish`, `neuron`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 18 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000044` (1 mention) - the report calls it "Lab/clinical"; HP calls it **Hypogonadotropic hypogonadism**
- `HP:0000458` (1 mention) - the report calls it "Clinical sign"; HP calls it **Anosmia**
- `HP:0000054` (1 mention) - the report calls it "Physical"; HP calls it **Micropenis**
- `HP:0000028` (1 mention) - the report calls it "Physical"; HP calls it **Cryptorchidism**
- `HP:0008734` (1 mention) - the report calls it "Physical"; HP calls it **Decreased testicular size**
- `HP:0001363` (1 mention) - the report calls it "Physical"; HP calls it **Craniosynostosis**
- `UBERON:0001301` (1 mention) - the report calls it "preoptic area"; UBERON calls it **epididymis**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0000981` (1 mention) - the report calls it "DNA-binding transcription factor activity, RNA pol II-specific"; GO calls it **DNA-binding transcription factor activity, RNA polymerase II-specific**
- `CL:0000029` (2 mentions) - the report calls it "neural crest cell"; CL calls it **neural crest derived neuron**
- `UBERON:0002264` (2 mentions) - the report calls it "olfactory placode"; UBERON calls it **olfactory bulb**, and lists "olfactory lobe" among its other names
- `GO:0005634` (1 mention) - the report calls it "Subcellular:** Nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.