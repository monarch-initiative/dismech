---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-28T13:09:41.263438'
end_time: '2026-09-28T13:17:28.775400'
duration_seconds: 467.51
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hereditary Spastic Paraplegia 77
  mondo_id: MONDO:0014882
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 14
reference_validation:
  total_references: 2
  verified: 2
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 2
  on_topic: 1
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 59
  verified: 53
  not_found: 4
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.069
  labels_checked: 51
  labels_matching: 23
  labels_mismatched: 11
  mislabelled_terms:
  - term_id: HP:0002357
    reported_labels:
    - Abnormal gait
    ontology_label: obsolete Dysphasia
  - term_id: HP:0001250
    reported_labels:
    - Spasticity
    - Seizures
    ontology_label: Seizure
  - term_id: HP:0003477
    reported_labels:
    - Extensor plantar response
    ontology_label: Peripheral axonal neuropathy
  - term_id: HP:0002151
    reported_labels:
    - Lactic acidosis
    ontology_label: Increased circulating lactate concentration
  - term_id: GO:0030042
    reported_labels:
    - axonogenesis
    ontology_label: actin filament depolymerization
  - term_id: CL:0000127
    reported_labels:
    - corticospinal neuron
    - astrocytes
    ontology_label: astrocyte
  - term_id: UBERON:0001017
    reported_labels:
    - spinal cord
    ontology_label: central nervous system
  - term_id: UBERON:0001384
    reported_labels:
    - corticospinal tract
    ontology_label: primary motor cortex
  - term_id: UBERON:0000955
    reported_labels:
    - primary motor cortex
    ontology_label: brain
  - term_id: HP:0003541
    reported_labels:
    - Bilateral lower limb spasticity
    ontology_label: Urinary glycosaminoglycan excretion
  - term_id: UBERON:0008897
    reported_labels:
    - foot
    ontology_label: fin
  labels_variant: 17
  unresolved_terms:
  - HP:0001295
  - HP:0007320
  - HP:0002471
  - HP:0002369
  obsolete_terms:
  - term_id: HP:0002357
    ontology_label: obsolete Dysphasia
    replaced_by: HP:0002381
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Spastic Paraplegia 77
- **MONDO ID:** MONDO:0014882 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Spastic Paraplegia 77** covering all of the
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

# Hereditary Spastic Paraplegia 77 (SPG77) / FARS2-Related Later-Onset Spastic Paraplegia

Hereditary spastic paraplegia 77 (SPG77) is a rare, autosomal recessive neurodegenerative disorder that forms the later-onset end of the **FARS2 deficiency** spectrum and is characterized predominantly by slowly progressive spastic paraplegia of the lower limbs, with variable additional neurologic and systemic features.[9][12][13] It is caused by biallelic pathogenic variants in the nuclear-encoded mitochondrial gene **FARS2**, which encodes mitochondrial phenylalanyl-tRNA synthetase (mtPheRS), resulting in impaired mitochondrial translation, dysfunction of oxidative phosphorylation (OXPHOS) complexes, and selective vulnerability of long central motor pathways.[9][11][14] Clinically, SPG77 presents from infancy to childhood with delayed motor milestones, gait disturbance, hyperreflexia, and lower limb spasticity, often accompanied by muscle weakness, hypotonia, and occasional seizures or ocular abnormalities, and it is classified within the heterogeneous group of hereditary spastic paraplegias (HSPs) as a pure or complex form.[7][13] Epidemiologically, FARS2 deficiency is extremely rare, with 37 affected individuals from 25 families reported across the entire phenotypic spectrum as of recent GeneReviews updates, and SPG77 represents approximately 30% of these later-onset, milder cases.[9][12] There is currently no disease-modifying therapy; management is symptomatic and multidisciplinary, focusing on spasticity control, seizure management when present, orthopedic surveillance, and rehabilitative interventions, while genetic counseling, carrier testing, and reproductive options provide the main avenues for primary prevention of new affected cases.[9][12] Experimental work in Drosophila and other model systems has begun to elucidate the mechanistic chain from FARS2 mutation to mitochondrial dysfunction, neuronal impairment, and clinical spasticity, highlighting mtPheRS as a potential target for future precision therapies.[14]

## 1. Disease Information

### 1.1 Clinical and Nosological Overview

Hereditary spastic paraplegia 77 (SPG77) is a form of **autosomal recessive hereditary spastic paraplegia** associated with pathogenic variants in the FARS2 gene, which encodes the mitochondrial phenylalanyl-tRNA synthetase.[8][11][13] Within the broader nosological framework, SPG77 is best understood as the later-onset, spastic paraplegia-predominant phenotype of **FARS2 deficiency**, a disorder whose clinical spectrum ranges from severe infantile-onset epileptic mitochondrial encephalopathy with lactic acidosis to milder childhood-onset spastic paraplegia with relatively preserved cognition and longer survival.[9][12] GeneReviews on FARS2 deficiency emphasizes this continuum, stating that “the spectrum of FARS2 deficiency ranges from the infantile-onset phenotype, characterized by epileptic encephalopathy with lactic acidosis and poor prognosis (70% of affected individuals), to the later-onset phenotype, characterized by spastic paraplegia, less severe neurologic manifestations, and longer survival (30% of affected individuals),” and that the later-onset phenotype corresponds to autosomal recessive spastic paraplegia 77.[9][12] Orphanet similarly defines autosomal recessive spastic paraplegia type 77 as a rare, pure or complex HSP characterized by infancy-to-childhood onset of slowly progressive lower limb spasticity, delayed motor milestones, gait disturbance, hyperreflexia, and muscle abnormalities including weakness, hypotonia, intention tremor, and amyotrophy, with possible ocular and other neurologic manifestations.[13] These descriptions situate SPG77 firmly within the HSP category, but with a distinctive mitochondrial etiology and a recognizable pattern of onset, progression, and associated features.

The disease manifests clinically with motor dysfunction dominated by spasticity and weakness of the lower extremities, resulting in walking difficulties, falls, and the need for assistive devices as severity progresses.[7][9][12][13] In many individuals, the spastic paraplegia is “pure,” meaning largely confined to the corticospinal tract with limited involvement of other neurologic systems, whereas in others it is “complex,” with additional features such as developmental delay or intellectual disability, seizures, ocular abnormalities, dysarthria, or tremor.[9][12][13] The age at symptom onset typically lies between infancy and childhood, with Orphanet listing “infancy to childhood” and ICD-10 coding under the category of hereditary ataxia and spastic paraplegia.[13] GeneReviews notes that later-onset FARS2-related spastic paraplegia should be considered in individuals aged six months and older who have progressive lower-extremity weakness, spasticity, hyperreflexia, and gait difficulty, sometimes accompanied by mild developmental delay or brief seizures that resolve over time.[9][12] Overall, SPG77 constitutes a recognizable entity within the HSP spectrum that is tied to a specific mitochondrial translation defect and that carries implications for both clinical management and molecular diagnosis.

### 1.2 Identifiers, Classification, and Synonyms

SPG77 is well codified across major genetic and disease ontologies, which facilitates its integration into computational knowledge bases. In **OMIM** (Online Mendelian Inheritance in Man), spastic paraplegia 77, autosomal recessive, is assigned phenotype number **617046**, and is mapped to FARS2 at locus **611592** on chromosome 6p25.1.[8][11] OMIM lists “Spastic paraplegia 77, autosomal recessive” as the phenotype designation, with an autosomal recessive inheritance pattern and phenotype mapping key 3, indicating that the gene-locus relationship is established.[8][11] The FARS2 gene entry (611592) notes that Gross mapped FARS2 to 6p25.1 based on alignment of the gene sequence with the GRCh38 genomic sequence, and associates FARS2 with both “Combined oxidative phosphorylation deficiency 14” (MIM 614946) and “Spastic paraplegia 77, autosomal recessive” (MIM 617046), thereby linking SPG77 to the broader category of mitochondrial OXPHOS disorders.[11]

In **Orphanet**, autosomal recessive spastic paraplegia type 77 is listed under the identifier **ORPHA:466722**, with synonyms including “SPG77” and classification as a rare disorder with prevalence <1/1,000,000.[13] Orphanet specifies an autosomal recessive inheritance pattern, age of onset in childhood or infancy, and ICD-10 code **G11.4** within the hereditary ataxia category, underscoring the neurological nature of the disease.[13] In **MedGen**, the concept “Hereditary spastic paraplegia 77” is associated with Concept ID **C5569007**, which is cross-referenced to OMIM 617046 and to MONDO:0014882, and is listed under the name “Hereditary spastic paraplegia 77” with synonyms “Spastic paraplegia 77, autosomal recessive.”[2][3][4][6][10] The **MONDO** ontology entry MONDO:0014882 is referenced in ClinVar submissions and MedGen for this disease, further integrating SPG77 into cross-ontology disease mapping.[2][3][4][6][10]

Other identifiers include **MeSH** (Medical Subject Headings) and **SNOMED CT** codes. MSeqDR’s mitochondrial disease browser references SPG77 under MedGen and MeSH identifiers “617046,” with tree numbers within nervous system disease hierarchies, and lists SPG77 as “Congenital abnormality,” “Genetic disease (inborn),” and “Nervous system disease,” reflecting its congenital onset and neurogenetic nature.[1] SNOMED CT codes associated with FARS2-related phenotypes include concepts for mitochondrial disease and spastic paraplegia as summarized in OMIM’s FARS2 gene entry.[11] Collectively, these identifiers and cross-references allow SPG77 to be consistently recognized in databases such as OMIM, Orphanet, MedGen, ClinVar, and MSeqDR, and ensure interoperability with ontologies such as MONDO (MONDO:0014882) and UMLS (C5569007).[2][3][4][6][8][10][13]

Common synonyms and alternative names for the disease include **“Hereditary spastic paraplegia 77,” “Spastic paraplegia 77, autosomal recessive,” “SPG77,”** and **“FARS2-related later-onset spastic paraplegia.”**[2][3][4][6][9][12][13] Within the mitochondrial disease literature, the broader entity of FARS2 deficiency encompasses both “combined oxidative phosphorylation deficiency 14” and “phenylalanyl-tRNA synthetase deficiency,” as well as “FARS2-related epileptic mitochondrial encephalopathy” and “FARS2-related later-onset spastic paraplegia (SPG77).”[9][11][12] For ontology mapping, the relevant terms would include MONDO:0014882 for hereditary spastic paraplegia 77, HP:0001257 for spastic paraplegia, HP:0002061 for gait disturbance, HP:0001295 for hyperreflexia, and HP:0007320 for mitochondrial complex I deficiency where applicable.

### 1.3 Data Sources and Nature of Information

Information about SPG77 arises primarily from **aggregated disease-level resources** rather than large-scale epidemiologic datasets or electronic health record (EHR) warehouses, reflecting the extreme rarity of the condition. GeneReviews on FARS2 deficiency synthesizes published case reports and small series to describe the clinical spectrum, genotype–phenotype correlations, diagnostic strategies, and management recommendations for the disorder.[9][12] OMIM compiles data from individual case reports, linkage analyses, and functional studies to detail the mapping of FARS2 variants to SPG77 and combined oxidative phosphorylation deficiency 14.[8][11] Orphanet collates information from primary publications and expert input to provide a concise disease definition, prevalence estimates, and core phenotypic features for autosomal recessive spastic paraplegia type 77.[13] ClinVar integrates variant-level information submitted by clinical laboratories and research groups, including classification of FARS2 variants such as c.1082C>T (p.Pro361Leu), c.1255C>T (p.Arg419Cys), c.1256G>A (p.Arg419His), and c.792del (p.Asp265fs) with respect to hereditary spastic paraplegia 77.[2][3][4][6]

The quantitative data on prevalence, incidence, and natural history are limited because reported cases number in the dozens, not thousands. GeneReviews notes that FARS2 deficiency is rare and that, as of its latest review, 37 affected individuals from 25 families have been reported in the literature.[9][12] Among these, approximately 70% have the infantile-onset epileptic encephalopathy phenotype, and 30% have the later-onset spastic paraplegia phenotype corresponding to SPG77.[9][12] Orphanet provides a qualitative prevalence estimate of less than 1 per 1,000,000 for autosomal recessive spastic paraplegia type 77, without specifying incidence rates or population-based figures.[13] These facts underscore that the information used to construct SPG77 knowledge bases comes predominantly from **case-level observational data, curated expert reviews, and genetic variant repositories**, rather than from large controlled trials or population registries.[7][9][12][13]

## 2. Etiology

### 2.1 Primary Causal Factors: FARS2 Deficiency and Mitochondrial Translation Defect

The primary etiologic factor in hereditary spastic paraplegia 77 is **biallelic pathogenic variants in the FARS2 gene**, which encodes the mitochondrial phenylalanyl-tRNA synthetase (mtPheRS), a key enzyme in mitochondrial protein translation.[9][11][12] FARS2 is a nuclear gene located on chromosome 6p25.1, with genomic coordinates approximately 6:5,249,934–5,771,583 in GRCh38, and its gene product resides within the mitochondrial matrix where it catalyzes the aminoacylation of mitochondrial tRNA\(^\text{Phe}\) with phenylalanine.[11][14] This aminoacylation step is essential for the incorporation of phenylalanine into nascent polypeptides encoded by mitochondrial DNA, including several subunits of OXPHOS complexes I, III, IV, and V.[11][14] Loss-of-function or functionally hypomorphic variants in FARS2 impair mtPheRS activity, leading to defective mitochondrial translation, reduced stability and activity of OXPHOS complexes, and secondary defects in cellular energy metabolism.[9][11][14]

GeneReviews explicitly states that “FARS2 deficiency comprises a spectrum of disease severity that ranges between two phenotypes: infantile-onset disease characterized by epileptic encephalopathy with lactic acidosis and poor prognosis (70% of affected individuals) and later-onset spastic paraplegia (30% of affected individuals) associated with less severe neurologic manifestations and longer survival,” and that in both forms, the diagnosis is established in a proband with suggestive findings and biallelic pathogenic variants in FARS2.[9][12] OMIM’s FARS2 gene entry describes multiple missense variants, frameshift changes, and structural deletions that have been identified in individuals with SPG77 or combined oxidative phosphorylation deficiency 14, and notes that these variants affect conserved residues in catalytic domains or C-terminal regions of mtPheRS, thereby compromising enzymatic function.[11] For example, Yang et al. reported a homozygous Asp142Tyr (D142Y) substitution at a highly conserved residue in the catalytic motif in four siblings from a consanguineous Chinese family with autosomal recessive SPG77, highlighting the direct causal link between FARS2 mutation and the spastic paraplegia phenotype.[11]

Functional evidence supports the centrality of FARS2 dysfunction in disease etiology. In a Drosophila model, inactivation of the FARS2 ortholog (dFARS2) leads to developmental delay and seizure behavior, with biochemical studies showing that dFARS2 is required for mitochondrial tRNA aminoacylation, mitochondrial protein stability, and assembly and enzyme activities of OXPHOS complexes.[14] When human FARS2 variants associated with disease are expressed in Drosophila, specific phenotypes are induced: expression of p.G309S causes seizure behaviors, whereas expression of p.D142Y leads to locomotor defects, mimicking human seizure and spasticity manifestations and strengthening the causal connection between FARS2 mutations and neuronal dysfunction.[14] Taken together, these human and model organism data firmly establish **FARS2 deficiency as the primary causal factor** in SPG77, with the etiologic mechanism rooted in mitochondrial tRNA aminoacylation and translation.

### 2.2 Genetic Risk Factors: Causal Variants, Susceptibility, and Modifier Considerations

In the context of SPG77, **genetic risk factors are synonymous with causal variants**, because the disease is monogenic and typically results from biallelic pathogenic FARS2 mutations.[9][11][12] ClinVar documents several FARS2 variants that have been associated with hereditary spastic paraplegia 77, including missense substitutions at conserved residues and a frameshift deletion. For instance, the variant **NM_006567.5(FARS2):c.1082C>T (p.Pro361Leu)** is classified as pathogenic for hereditary spastic paraplegia 77 by OMIM-based submission, with location at Chr6:5,613,185 (GRCh38) and functional consequence as a single nucleotide missense variant affecting the C-terminal domain.[3] The variant **c.1255C>T (p.Arg419Cys)** is reported in two siblings with mitochondrial dysfunction and spastic paraplegia as part of a compound heterozygous genotype; this variant affects a conserved Arg residue in the C-terminal domain, and OMIM describes it as pathogenic for SPG77.[6][11] A related variant **c.1256G>A (p.Arg419His)** is also submitted to ClinVar for hereditary spastic paraplegia 77, indicating that different substitutions at the same residue can confer disease risk.[4] Another variant, **c.792del (p.Asp265fs)**, is a frameshift deletion predicted to truncate the protein and has been submitted in association with hereditary spastic paraplegia 77.[2]

Yang et al. identified a homozygous missense mutation **c.424G>T (Asp142Tyr)** in the FARS2 gene in four siblings from a consanguineous Chinese family with autosomal recessive SPG77, with segregation of the mutation with disease and absence in unaffected relatives, providing genetic evidence of causality.[11] Vernon et al. reported two siblings with mitochondrial dysfunction and spastic paraplegia who were compound heterozygous for a missense variant **c.1255C>T (Arg419Cys)** and a large 116-kb deletion encompassing exon 6 and parts of introns 5 and 6, demonstrating that structural variants can also contribute to disease and highlighting the role of gene dosage.[6][11] These reported variants cluster in functionally important regions of mtPheRS and are presumed to confer **loss-of-function or severe hypomorphic effects**, though precise biochemical characterization exists only for some variants.[11][14]

Beyond these causal variants, there is currently no robust evidence for **common susceptibility alleles or modifier genes** that modulate disease risk or severity in SPG77. GeneReviews notes that formal diagnostic criteria have not been established and that the clinical spectrum is broad, but does not identify specific genetic modifiers.[9][12] The distribution of phenotypes is partly explained by the nature and location of the FARS2 variants: more disruptive variants in catalytic motifs tend to cause severe infantile encephalopathy, whereas variants that partially preserve mtPheRS activity may result in later-onset spastic paraplegia.[9][11][12][14] For example, Nucleic Acids Research analysis of FARS2 deficiency in Drosophila points out that patients carrying homozygous p.Y144C or p.G309S or compound heterozygous p.G309S/p.R153G mutations developed infantile-onset epileptic mitochondrial encephalopathy, whereas p.D142Y was associated with locomotor defects more reflective of spastic paraplegia, suggesting allele-specific phenotypic outcomes.[14] However, these genotype–phenotype correlations are still emerging and have not yet crystallized into clearly defined modifier gene frameworks.

### 2.3 Environmental and Lifestyle Risk Factors

Current evidence does not support **environmental, lifestyle, infectious, or occupational exposures** as primary risk factors for SPG77, which is fundamentally a monogenic, autosomal recessive disorder.[9][12][13] The disease arises from inherited or de novo germline variants in FARS2, and there is no indication that toxins, diet, radiation, or infections directly cause the mutation or trigger disease onset in the absence of the underlying genetic defect.[9][12][13] In contrast to multifactorial neurodegenerative conditions such as sporadic spasticity or motor neuron diseases, SPG77’s pathogenesis is tightly linked to the mitochondrial translational defect, and there is no evidence from GeneReviews, Orphanet, or OMIM of any environmental exposures that substantially modify the risk of developing SPG77 in carriers.[9][11][12][13]

Family history and **consanguinity** serve as important contextual risk factors. OMIM notes that in the D142Y family described by Yang et al., the parents were consanguineous Chinese, and four siblings were homozygous for the FARS2 mutation.[11] This underscores the role of consanguineous marriage in increasing the likelihood of homozygosity for rare recessive variants, thereby elevating the risk of autosomal recessive disorders such as SPG77 in offspring. GeneReviews indicates that FARS2 deficiency is inherited in an autosomal recessive manner, and that at conception, each sibling of an affected individual has a 25% chance of being affected, a 50% chance of being an asymptomatic carrier, and a 25% chance of being unaffected and not a carrier.[12] Although consanguinity itself is not a mechanistic etiologic factor, it acts as a **population-genetic risk parameter** that increases the probability of biallelic pathogenic variants, particularly in small or isolated populations.

Lifestyle factors such as smoking, exercise, and diet have not been systematically studied in SPG77 due to the small numbers of patients, and no specific recommendations exist beyond general principles for neurologic and mitochondrial disorders.[9][12] Similarly, infectious agents have not been implicated in either the initiation or exacerbation of SPG77. This absence of data strongly suggests that **SPG77 is essentially a genetic disease with negligible environmental contribution to primary risk**, although environmental factors may influence symptom severity and quality of life, as in any chronic neurologic condition.

### 2.4 Protective Factors and Gene–Environment Interactions

To date, **no genetic protective variants or modifier alleles** have been convincingly identified that reduce the risk or severity of SPG77 in individuals with pathogenic FARS2 variants.[9][11][12][14] While variation in mitochondrial DNA haplogroups or nuclear-encoded mitochondrial proteins theoretically could modulate the impact of FARS2 mutations by altering OXPHOS capacity or mitochondrial biogenesis, such hypotheses remain speculative and have not been validated in the small number of known cases.[9][12] Given the rarity of FARS2 deficiency and SPG77, systematic searches for protective factors (e.g., in gnomAD or GWAS catalogs) have not been reported, and the available literature focuses on pathologic variants rather than on protective ones.[9][11][12][14]

Environmental protective factors also remain undefined. GeneReviews discusses valproic acid, a commonly used anticonvulsant that can induce liver failure in persons with mitochondrial diseases, noting that some individuals with FARS2 deficiency received valproic acid without evidence of liver dysfunction or worsening of liver disease, and that “given the limited number of affected individuals reported to date, no general recommendation can be made.”[9][12] This remark underscores the difficulty of drawing conclusions about drug safety or protective effects in such a small cohort and highlights that no specific environmental exposures have been identified as beneficial in reducing disease expression. Nutritional supplements often used in mitochondrial disease, such as coenzyme Q10, L-carnitine, or riboflavin, have been administered empirically in some cases, but controlled evidence of protective effects in SPG77 is lacking.[9][12]

Consequently, **gene–environment interactions** in SPG77 are essentially unknown. The causal chain runs predominantly from germline FARS2 mutations to mitochondrial translation defect and neuronal dysfunction, with limited or no documented modulation by environmental influences.[9][12][14] For knowledge base purposes, SPG77 can be classified as a **monogenic, largely environment-independent Mendelian disease**, with consanguinity serving as a population-level risk factor and without clearly defined protective factors.

## 3. Phenotypes

### 3.1 Core Motor Phenotypes: Spastic Paraplegia and Gait Disturbance

The defining phenotype of SPG77 is **spastic paraplegia**, manifested by weakness, spasticity, and exaggerated reflexes of the lower extremities, leading to gait disturbances and walking difficulties.[9][12][13] GeneReviews describes the later-onset FARS2 phenotype as characterized by spastic paraplegia in all affected individuals, with lower-extremity weakness, spasticity, and hyperreflexia associated with walking difficulties, and notes that spastic paraplegia can be pure or complicated by other neurologic findings.[9][12] Orphanet’s disease definition emphasizes “slowly progressive lower limb spasticity, delayed motor milestones, gait disturbances, hyperreflexia and various muscle abnormalities, including weakness, hypotonia, intention tremor and amyotrophy,” providing a succinct summary of the core motor manifestations.[13] These features are typical of hereditary spastic paraplegias and reflect dysfunction of the corticospinal tracts and possibly spinal cord motor interneurons.[7]

From an ontology perspective, the core motor phenotypes can be mapped to several **HPO terms**. Spastic paraplegia corresponds to **HP:0001257**, which denotes progressive spasticity of the lower limbs. Gait disturbance can be encoded as **HP:0001288 (Gait ataxia)** or more specifically **HP:0002357 (Abnormal gait)**, although in SPG77 the gait is often spastic rather than ataxic, with scissoring and circumduction.[7][9][12][13] Hyperreflexia corresponds to **HP:0001347 (Hyperreflexia)**, and lower limb muscle weakness to **HP:0007340 (Lower limb muscle weakness)**. The combination of weakness and spasticity may also be captured by **HP:0002061 (Spastic gait)** and **HP:0001250 (Spasticity)**. Muscle amyotrophy, often observed in chronic spastic paraplegia, is represented by **HP:0003202 (Muscle wasting)**. Together, these HPO terms provide a structured representation of the motor phenotype for computational applications.

The age of onset of motor symptoms in SPG77 spans **infancy to childhood**, with both Orphanet and GeneReviews noting that later-onset FARS2-related spastic paraplegia occurs in individuals aged at least six months and often in early childhood.[9][12][13] Symptom severity is generally **moderate to severe**, but variable: some individuals have pure spastic paraplegia with preserved cognitive function and independence in ambulation into adolescence or adulthood, whereas others develop significant disability requiring wheelchairs or assistive devices, particularly as contractures and orthopedic complications accumulate.[9][12][13] Symptom progression is typically **slow and progressive**, not acute or episodic, consistent with the neurodegenerative nature of HSP, although the rate of progression may vary between families and individuals.[7][9][12][13] Frequency among affected individuals is essentially universal for spastic paraplegia in SPG77 cases, as GeneReviews states that all individuals with the later-onset phenotype had spastic paraplegia.[9][12]

The impact of these motor phenotypes on **quality of life** is substantial. Progressive spasticity and weakness lead to difficulty walking, climbing stairs, running, and maintaining balance, limiting participation in school, work, and social activities.[7][9][12] Pain from muscle spasms, fatigue from increased effort of movement, and falls contribute to morbidity, while psychological effects such as anxiety, depression, and social withdrawal may ensue.[7] Although formal quality-of-life metrics such as SF-36 or EQ-5D have not been reported specifically for SPG77, data from HSP cohorts indicate that lower limb spasticity significantly impairs mobility, independence in activities of daily living, and overall well-being.[7] In knowledge base terms, these motor manifestations can be linked to **ICF (International Classification of Functioning) codes** for mobility and self-care limitations, and mapped to EQ-5D domains of pain/discomfort and mobility.

### 3.2 Non-Motor Neurologic Phenotypes: Developmental, Seizure, and Ocular Features

Beyond the core motor phenotype, SPG77 can exhibit a range of **non-motor neurologic and systemic features**, making it a complex HSP in some individuals.[9][12][13] GeneReviews notes that in the later-onset phenotype, some individuals have developmental delay or intellectual disability that is less severe than in the infantile-onset phenotype; for example, five of six affected individuals developed expressive language.[9][12] Brief seizures that resolve over time are also reported in some later-onset cases, indicating that epileptiform activity can accompany spastic paraplegia but tends to be milder and non-progressive compared to the infantile epileptic encephalopathy form.[9][12] Orphanet includes “ocular abnormalities (e.g. strabismus, ptosis)” among possible associated manifestations, along with dysarthria, seizures, extensor plantar responses, and intention tremor.[13] These features broaden the phenotype beyond pure corticospinal tract involvement.

The developmental and cognitive phenotype can be captured by HPO terms such as **HP:0001263 (Developmental delay)** and **HP:0001249 (Intellectual disability)**, typically in mild or moderate forms for SPG77.[9][12] Expressive language delay may be coded as **HP:0002471 (Expressive language delay)**. Seizures are represented by **HP:0001250 (Seizures)** or more specific subtypes depending on electroclinical features, such as myoclonic seizures or generalized tonic–clonic seizures, although SPG77 seizures are often brief and self-limited.[9][12] Ocular abnormalities such as strabismus and ptosis map to **HP:0000486 (Strabismus)** and **HP:0000508 (Ptosis)**.[13] Dysarthria corresponds to **HP:0001260 (Dysarthria)**, while extensor plantar response is represented by **HP:0003477 (Extensor plantar response)**, reflecting corticospinal tract dysfunction.[13] Intention tremor can be coded as **HP:0002080 (Intention tremor)**. Collectively, these terms facilitate detailed phenotypic annotation of SPG77.

The **age of onset** of non-motor features varies. Developmental delay is typically evident in infancy or early childhood, as delays in motor milestones and speech become apparent, whereas seizures may appear in infancy or childhood but often resolve over time.[9][12] Ocular features may be congenital or develop over the course of disease. The **severity** of non-motor manifestations tends to be **mild to moderate** compared to the infantile encephalopathic phenotype, with GeneReviews explicitly distinguishing the less severe neurologic manifestations and better developmental outcomes in the later-onset group.[9][12] Symptom progression may be partially progressive for cognitive and speech abilities (as children acquire skills), but seizures are often **episodic** and may remit, while ocular features and dysarthria may be relatively **stable or slowly progressive**.[9][12][13]

Non-motor neurologic phenotypes substantially influence **quality of life**, especially through impacts on communication, learning, social integration, and visual function.[7][9][12] Developmental delay and intellectual disability may limit educational attainment and employment opportunities, while seizures impose safety concerns, restrict activities such as swimming or driving, and can be stigmatizing.[7][9][12] Ocular abnormalities like strabismus or ptosis may affect visual acuity and cause cosmetic concerns that impact self-esteem.[13] Awareness of these features is crucial for comprehensive management and counseling, and in knowledge bases they can be linked to **CL terms** for cortical neurons and ocular motor neurons, as well as **GO processes** for neurodevelopment and synaptic function.

### 3.3 Laboratory and Imaging Phenotypes

Although SPG77 is primarily defined by clinical neurologic phenotypes, several **laboratory and imaging findings** may be present and can be useful for diagnosis and mechanistic understanding. In the broader FARS2 deficiency spectrum, infantile-onset cases often show lactic acidosis, elevated lactate on blood or CSF testing, and metabolic signatures of mitochondrial OXPHOS dysfunction.[9][12] Later-onset SPG77 cases are less likely to have overt lactic acidosis, but mild elevations or other mitochondrial biomarkers may occasionally be observed, reflecting subclinical energy metabolism defects.[9][12] These laboratory abnormalities correspond to HPO terms such as **HP:0002151 (Lactic acidosis)** and can be encoded via LOINC terms for serum or CSF lactate levels.

Neuroimaging findings in hereditary spastic paraplegia are variable and may include thinning of the corpus callosum, periventricular white matter changes, and corticospinal tract signal abnormalities.[7] Specific imaging patterns for SPG77 have not been extensively characterized due to the small number of cases, but mitochondrial encephalopathy forms of FARS2 deficiency often show cortical and subcortical lesions, basal ganglia involvement, or diffuse white matter changes on MRI.[9][12] In later-onset spastic paraplegia, imaging may be normal or show subtle corticospinal tract changes, spinal cord atrophy, or brainstem involvement.[7][9][12] Such imaging features can be mapped to HPO terms like **HP:0002143 (Abnormal brain MRI)**, **HP:0002369 (Cerebral white matter abnormalities)**, and **HP:0002079 (Corpus callosum hypoplasia)** where appropriate.

Electrophysiologically, individuals with the infantile phenotype have abnormal EEG patterns, including hypsarrhythmia in some cases, whereas later-onset SPG77 rarely exhibits persistent EEG abnormalities and may only show transient epileptiform discharges during brief seizures.[9][12] EMG and nerve conduction studies are often normal or show mild distal axonal changes, as SPG77 primarily affects central motor pathways rather than peripheral nerves.[7][9][12] These data contribute to the diagnostic workup but are not pathognomonic. The absence of distinctive, disease-specific imaging or electrophysiologic markers in SPG77 underscores the importance of **genetic testing** for definitive diagnosis.

### 3.4 Phenotype Progression, Variability, and Quality of Life Impact

The **progression** of phenotypes in SPG77 follows a largely **slowly progressive course**, typical of hereditary spastic paraplegias. Motor symptoms begin in infancy or childhood with delayed walking, clumsiness, and gait abnormalities, and gradually worsen over years, leading to increased spasticity, weakness, and functional impairment.[7][9][12][13] Contractures, scoliosis, and foot deformities may develop as secondary orthopedic complications, further restricting mobility.[9][12] GeneReviews recommends routine monitoring of orthopedic complications such as contractures, scoliosis, and foot deformities in individuals with later-onset FARS2-related spastic paraplegia, emphasizing that these musculoskeletal changes are integral to disease progression.[9][12] Non-motor features such as seizures may remit over time, whereas developmental and cognitive trajectories may show some catch-up, particularly in expressive language, although residual deficits often persist.[9][12]

Phenotypic **variability** is marked both between and within families, reflecting differences in underlying FARS2 variants, potential modifiers, and environmental influences.[9][11][12][14] The same variant, such as D142Y, can produce similar phenotypes in multiple siblings, but other families with different variants display diverse combinations of spastic paraplegia, epilepsy, and developmental delay.[11][14] GeneReviews highlights that spastic paraplegia can be “pure” or “complicated,” indicating that some individuals have isolated motor involvement while others have additional neurologic features.[9][12] This variability underscores the need for individualized clinical assessment and caution when extrapolating prognosis across patients.

The **quality of life impact** of SPG77 is considerable across multiple domains. Motor disability undermines independence in activities of daily living, mobility, and participation in work and social life, while cognitive and language deficits can impair communication and education.[7][9][12] Seizures add a layer of unpredictability and anxiety, and ocular abnormalities may affect visual functioning and self-image.[13] Although formal quality-of-life instruments have not been systematically applied to SPG77, extrapolation from HSP and mitochondrial disease cohorts suggests significant reductions in physical functioning, role limitations, and social participation, with psychological distress as a common comorbidity.[7][9][12] For knowledge base entries, linking SPG77 phenotypes to EQ-5D dimensions and SF-36 subscales can capture these impacts and support integrative analyses of disease burden.

## 4. Genetic and Molecular Information

### 4.1 The FARS2 Gene: Structure, Function, and Annotation

The **FARS2 gene** encodes the mitochondrial phenylalanyl-tRNA synthetase (**mtPheRS**), a nuclear-encoded enzyme that plays an essential role in mitochondrial protein translation.[11][14] OMIM lists FARS2 under gene MIM number **611592**, with cytogenetic location **6p25.1** and GRCh38 genomic coordinates approximately 6:5,249,934–5,771,583.[11] FARS2 spans multiple exons and produces a protein that is targeted to mitochondria via an N-terminal mitochondrial targeting sequence, where it binds mitochondrial tRNA\(^\text{Phe}\) and catalyzes its aminoacylation with phenylalanine.[11][14] This reaction is a crucial step in mitochondrial translation, as aminoacylated tRNA\(^\text{Phe}\) is required for the incorporation of phenylalanine into nascent polypeptides encoded by mitochondrial DNA, including core subunits of complexes I (NADH dehydrogenase), III (cytochrome bc\(_1\)), IV (cytochrome c oxidase), and V (ATP synthase).[11][14]

The FARS2 protein contains identifiable domains, including a highly conserved **catalytic domain** involved in aminoacylation and C-terminal regions that contribute to tRNA binding and overall structural stability.[11][14] OMIM notes that variants such as D142Y affect a highly conserved residue in the catalytic motif of aminoacylation at the interface of the anticodon stem–binding domain, underscoring the functional importance of this site.[11] Nucleic Acids Research further elaborates that dFARS2 (the Drosophila ortholog) deficiency leads to defects in mitochondrial tRNA\(^\text{Phe}\) metabolism, translation, and the assembly and activity of OXPHOS complexes.[14] These insights support annotation of FARS2 with **Gene Ontology (GO)** terms such as **GO:0006418 (tRNA aminoacylation for protein translation)**, **GO:0005739 (mitochondrion)**, and **GO:0006419 (alanyl-tRNA aminoacylation)** analogously, though specifically for phenylalanyl-tRNA synthetase.

From an HGNC perspective, FARS2 is recognized as “phenylalanyl-tRNA synthetase 2, mitochondrial,” and its protein product can be linked to **UniProt** entries containing structural and functional information.[11] In ontology terms, FARS2 is associated with **NCIT gene concept C118666** (if mapped) and can be tied to mitochondrial translation pathways in Reactome and KEGG. The gene’s dual association with combined oxidative phosphorylation deficiency 14 (MIM 614946) and SPG77 (MIM 617046) reflects the broad phenotypic spectrum of FARS2-related disorders, emphasising the need for careful genotype–phenotype mapping in disease knowledge bases.[11]

### 4.2 Pathogenic Variants in SPG77: Types, Locations, and Consequences

Multiple **pathogenic FARS2 variants** have been described in individuals with SPG77 and related phenotypes. These variants span a range of types, including missense substitutions, frameshift deletions, and structural deletions, and cluster in functionally important domains of the protein.[2][3][4][6][11][14]

Missense variants are the most commonly reported in SPG77. Yang et al. identified a homozygous **c.424G>T (p.Asp142Tyr, D142Y)** variant in exon 2 of FARS2 in four siblings from a consanguineous Chinese family, with clinical features of autosomal recessive spastic paraplegia.[11] The D142Y substitution occurs at a highly conserved residue in the catalytic motif of aminoacylation and is predicted to severely impair mtPheRS activity.[11][14] ClinVar entries record additional missense variants, including **c.1082C>T (p.Pro361Leu)**, **c.1255C>T (p.Arg419Cys)**, and **c.1256G>A (p.Arg419His)**.[3][4][6] The Pro361Leu variant affects a conserved residue in the C-terminal domain, and OMIM’s ClinVar-linked submission labels it as pathogenic for hereditary spastic paraplegia 77.[3] The Arg419Cys and Arg419His variants both alter a conserved arginine residue in the C-terminal domain; Arg419Cys was described in two siblings with mitochondrial dysfunction and spastic paraplegia in conjunction with a large deletion, and is considered pathogenic.[6][11] These variants exemplify how single amino acid changes at conserved positions in catalytic or C-terminal domains can lead to SPG77.

Frameshift and structural variants also contribute to SPG77. ClinVar lists **c.792del (p.Asp265fs, p.Asp265Thrfs*29)** as a pathogenic frameshift variant in FARS2 associated with hereditary spastic paraplegia 77.[2] This deletion is predicted to alter the reading frame and truncate the protein, likely resulting in loss of function. Vernon et al. reported a **116-kb interstitial deletion** spanning nucleotides 5,610,223–5,726,369 of chromosome 6, including all of exon 6 and parts of introns 5 and 6 of FARS2, in two siblings with mitochondrial dysfunction and spastic paraplegia.[6][11] This deletion, in compound heterozygosity with the Arg419Cys missense variant, reduces functional FARS2 dosage and contributes to disease.[6][11] Such structural variants underscore the need for gene-targeted deletion/duplication analysis as part of comprehensive genetic testing.

Variant classification follows ACMG/AMP guidelines and is reflected in ClinVar entries, which label variants such as Pro361Leu and Arg419Cys as **pathogenic** based on literature review and OMIM assertion.[3][6] Some variants, such as Gly141Glu (c.422G>A), may be classified as of **uncertain significance** pending further functional and clinical evidence, as indicated by MSeqDR’s listing of an NM_006567.5(FARS2):c.422G>A variant with uncertain significance for SPG77.[1] Overall, SPG77-associated variants predominantly appear to be **loss-of-function or severe hypomorphic** in nature, affecting the enzyme’s catalytic activity, tRNA binding, or structural integrity, and thereby impairing mitochondrial translation.[11][14] These can be annotated in knowledge bases with variant type (missense, frameshift, deletion), ClinVar classification, and predicted functional consequence (loss of function, impaired aminoacylation).

### 4.3 Variant Origin, Allele Frequency, and Population Distribution

SPG77 is driven by **germline variants**, inherited in an autosomal recessive pattern, and no somatic variants have been implicated in its pathogenesis.[9][11][12] GeneReviews explicitly describes FARS2 deficiency as inherited in an autosomal recessive manner and does not mention somatic mosaicism or acquired FARS2 mutations.[12] All reported SPG77 cases involve biallelic variants that are either homozygous (as in the D142Y family) or compound heterozygous (as in the Arg419Cys plus deletion family), with variants present in germline DNA in all tissues.[11] This allows for carrier testing and reproductive counseling based on standard Mendelian principles.[12]

Allele frequencies of SPG77-associated FARS2 variants in population databases such as gnomAD, ExAC, or 1000 Genomes are not detailed in the provided sources, but the extreme rarity of reported patients and the nature of the variants (often absent or very rare in controls) imply that these alleles are **ultra-rare**, with minor allele frequencies likely below 0.0001.[9][11][12][13] GeneReviews emphasizes that FARS2 deficiency is rare and that only 37 individuals from 25 families have been reported, which is consistent with a very low carrier frequency for pathogenic alleles.[9][12] Orphanet’s prevalence estimate of <1/1,000,000 for SPG77 likewise points to extreme rarity.[13] The D142Y variant appears to be a **founder mutation** in a specific consanguineous Chinese family, and may be absent from wider population datasets.[11] Similarly, Arg419Cys and other variants likely occur in specific families or small populations.

Geographically, SPG77 cases have been reported from diverse regions, including **China** (D142Y family), **European populations**, and other groups, suggesting that FARS2-related spastic paraplegia is not restricted to a single ethnicity.[11][9][12] However, the total number of cases is too small to draw definitive conclusions about geographic or ethnic distribution. For knowledge bases, FARS2 variants can be annotated as **germline**, with autosomal recessive inheritance, ultra-rare allele frequencies, and possible founder effects in specific families.

### 4.4 Modifier Genes, Epigenetics, and Chromosomal Abnormalities

As noted previously, **modifier genes** that influence SPG77 severity or penetrance have not been clearly identified. The variability of phenotype across FARS2 deficiency may be partly explained by the nature of the primary FARS2 variants, with more disruptive catalytic domain variants producing severe encephalopathy and milder C-terminal variants producing spastic paraplegia, but this remains speculative.[9][11][12][14] No studies have systematically evaluated nuclear or mitochondrial modifier loci in SPG77, and knowledge base entries should therefore flag modifier information as **unknown or not established**.

Epigenetic mechanisms such as DNA methylation or histone modifications have not been reported as primary drivers of SPG77.[9][12] Given that FARS2 deficiency arises from coding sequence changes in a nuclear gene, epigenetic alterations may modulate gene expression, but there is no direct evidence that epigenetic dysregulation contributes to disease onset or progression in SPG77. Similarly, larger **chromosomal abnormalities**, such as aneuploidies or translocations, are not implicated; structural variants described in SPG77 are intragenic deletions within FARS2, such as the 116-kb deletion involving exon 6.[6][11] This deletion can be cataloged in databases such as DECIPHER or dbVar as a pathogenic structural variant affecting FARS2, but it does not reflect broader chromosomal instability.

In summary, the **genetic architecture** of SPG77 is relatively simple, centered on biallelic FARS2 loss-of-function variants, with little evidence for complex polygenic or epigenetic contributions. Knowledge bases should reflect this simplicity while remaining open to future discoveries of modifiers or epigenetic influences.

## 5. Environmental Information

### 5.1 Environmental and Occupational Factors

Available data strongly indicate that **environmental factors**, including toxins, radiation, and occupational exposures, are not primary contributors to the onset of SPG77, which is fundamentally a Mendelian genetic disease.[9][12][13] Neither GeneReviews nor Orphanet mention specific environmental agents that increase risk for FARS2-related spastic paraplegia.[9][12][13] Unlike toxic neuropathies or sporadic motor neuron diseases where exposures to heavy metals, solvents, or pesticides can play a causal role, SPG77’s pathogenesis is rooted in inherited mitochondrial translation defects and appears largely insensitive to external toxicants in terms of disease initiation.

However, environmental factors may still modulate **symptom severity and progression**. For instance, physical inactivity, poor nutrition, and inadequate orthopedic care can exacerbate spasticity and muscle weakness, leading to more rapid functional decline.[7][9][12] Conversely, supportive environments that promote regular physical therapy, safe mobility, and balanced diet may help maintain muscle strength, flexibility, and overall health, though these influences are nonspecific and apply broadly to neurologic disorders. Knowledge bases can therefore note that environmental exposures are not established etiologic factors, but that general health-related behaviors may influence disease experience.

### 5.2 Lifestyle Factors

Lifestyle factors such as **smoking, alcohol consumption, and exercise** have not been specifically studied in SPG77, and no data suggest that they significantly alter primary disease risk.[9][12] Nonetheless, individuals with spastic paraplegia may benefit from lifestyle modifications aimed at maintaining cardiovascular fitness, muscle strength, and joint mobility, including low-impact exercise, stretching, and weight management.[7][9][12] Excessive alcohol use and smoking are generally discouraged in patients with neurologic disorders due to their adverse effects on overall health and potential interactions with medications.

Dietary interventions commonly employed in mitochondrial diseases, such as high-fat ketogenic diets or supplementation with mitochondrial cofactors (e.g., coenzyme Q10, L-carnitine), have not been systematically evaluated in SPG77 but might be considered empirically in selected cases.[9][12] GeneReviews does not recommend specific dietary regimens, instead emphasizing symptomatic management and supportive care.[9][12] Knowledge bases should therefore treat lifestyle factors as **general health modifiers rather than disease-specific etiologic or protective factors**.

### 5.3 Infectious Agents

No **infectious agents**—bacteria, viruses, fungi, or parasites—have been implicated in the causation or triggering of SPG77.[9][12][13] FARS2 deficiency arises from germline mutations, and the disease course typically reflects chronic neurodegenerative processes rather than sequelae of an acute infection. Viral encephalitis, post-infectious myelitis, or parasitic infections can produce spasticity or gait disturbance, but these conditions are clinically and etiologically distinct from hereditary spastic paraplegia, and there is no evidence that such infections transform a FARS2 carrier into an affected individual.[7][9][12]

Infections may, however, complicate disease management by exacerbating seizures or affecting overall health. Children with neurologic disabilities are at increased risk for aspiration pneumonia, urinary tract infections, and other complications, particularly if mobility or feeding is impaired.[9][12] Preventing common infections via vaccination and hygiene measures remains important, but does not constitute primary prevention of SPG77. Knowledge bases should note **no infectious etiology** for SPG77, while documenting that infections can impact morbidity in affected individuals.

### 5.4 Summary of Environmental Contributions

In synthesis, SPG77 is best classified as an **environmentally neutral, monogenic disease**, where environmental factors do not materially influence primary risk but may modestly affect symptom severity and quality of life.[9][12][13] This contrasts with complex disorders where gene–environment interactions are central to pathogenesis. For SPG77, knowledge bases should emphasize the absence of known environmental causative or protective factors, and focus on genetic and mechanistic information.

## 6. Mechanism and Pathophysiology

### 6.1 Ordered Causal Chain from Mutation to Clinical Manifestation

1. Biallelic pathogenic variants in the nuclear gene FARS2 lead to reduced or dysfunctional mitochondrial phenylalanyl-tRNA synthetase (mtPheRS) activity.[9][11][14]  
2. Impaired mtPheRS activity leads to defective aminoacylation of mitochondrial tRNA\(^\text{Phe}\), resulting in reduced availability of charged tRNA for mitochondrial translation.[11][14]  
3. Defective mitochondrial tRNA\(^\text{Phe}\) aminoacylation leads to decreased synthesis of mitochondrial DNA–encoded polypeptides, including critical subunits of oxidative phosphorylation (OXPHOS) complexes I, III, IV, and V.[11][14]  
4. Reduced synthesis and stability of mtDNA-encoded OXPHOS subunits lead to impaired assembly and enzyme activities of OXPHOS complexes, resulting in mitochondrial respiratory chain dysfunction.[11][14]  
5. Mitochondrial respiratory chain dysfunction leads to diminished ATP production and increased production of reactive oxygen species (ROS), causing cellular energy failure and oxidative stress, particularly in neurons with high energy demand; this step is partly inferred from general mitochondrial pathophysiology.[9][12][14]  
6. Chronic energy failure and oxidative stress in long corticospinal tract neurons lead to axonal degeneration, synaptic dysfunction, and demyelination in descending motor pathways, causing spastic paraplegia; this step is inferred from HSP pathophysiology.[7][9]  
7. In some individuals, more severe mitochondrial dysfunction leads to widespread cortical and subcortical neuronal impairment, resulting in epileptic encephalopathy, lactic acidosis, and developmental delay, reflecting the infantile-onset FARS2 phenotype.[9][12][14]  
8. In others, partially preserved mtPheRS function leads to more restricted vulnerability of corticospinal neurons, producing later-onset spastic paraplegia with relative sparing of cortical networks and thus milder cognitive and seizure manifestations.[9][11][12][14]  
9. Secondary orthopedic and musculoskeletal changes, including contractures, scoliosis, and muscle amyotrophy, result from chronic spasticity and weakness, further exacerbating gait disturbance and disability.[9][12][13]  

### 6.2 Molecular Pathways: Mitochondrial Translation and OXPHOS Dysfunction

At the **molecular level**, SPG77 reflects dysfunction in **mitochondrial translation pathways** and consequent **oxidative phosphorylation (OXPHOS) impairment**. FARS2 encodes mtPheRS, which catalyzes the charging of mitochondrial tRNA\(^\text{Phe}\) with phenylalanine, a prerequisite for incorporating this amino acid into mito-encoded proteins.[11][14] This process is part of the broader pathway of mitochondrial translation, which can be annotated with GO terms such as **GO:0006428 (tRNA aminoacylation)** and **GO:0006415 (translation)** and KEGG pathways for mitochondrial protein synthesis. Nucleic Acids Research demonstrates that inactivation of dFARS2 in Drosophila leads to defects in mitochondrial tRNA\(^\text{Phe}\) metabolism, decreased translation of mitochondrial proteins, and impaired assembly and activity of OXPHOS complexes, thereby providing mechanistic evidence for this pathway.[14]

The OXPHOS system comprises complexes I–V in the inner mitochondrial membrane, which mediate electron transport and ATP synthesis. mtDNA encodes 13 polypeptides that form core subunits of these complexes. Defective aminoacylation of mitochondrial tRNA\(^\text{Phe}\) reduces synthesis of these polypeptides, leading to incomplete or unstable OXPHOS complexes.[11][14] This dysfunction manifests biochemically as decreased respiratory chain activity, reduced ATP production, and increased ROS generation, which can be described via GO terms **GO:0006119 (oxidative phosphorylation)** and **GO:0006120 (mitochondrial electron transport, NADH to ubiquinone)**. In human FARS2 deficiency, combined oxidative phosphorylation deficiency 14 (MIM 614946) is the label used for infantile cases, highlighting that the same molecular pathway underlies both severe encephalopathy and later-onset spastic paraplegia.[11][12]

The link from FARS2 deficiency to specific OXPHOS complexes has been demonstrated in both patient-derived cells and animal models. Drosophila dFARS2 deficiency leads to reduced assembly and activity of complexes I, III, IV, and V, implicating broad OXPHOS compromise.[14] In human infantile FARS2-related encephalopathy, biochemical assays often show complex I deficiency and lactic acidosis, typical of mitochondrial respiratory chain disorders.[9][12] In SPG77, the OXPHOS impairment may be milder or more tissue-specific, leading primarily to chronic energy insufficiency in corticospinal neurons rather than acute systemic metabolic crises. This tissue specificity reflects differences in mitochondrial demands and reserve capacity across cell types.

### 6.3 Cellular Processes: Neuronal Vulnerability, Apoptosis, and Axonal Degeneration

At the **cellular level**, SPG77 involves selective vulnerability of **upper motor neurons** in the corticospinal tracts, which are long, highly energy-dependent neurons connecting the motor cortex to spinal motor circuits.[7][9] These neurons depend heavily on ATP for maintaining ion gradients, synaptic transmission, and axonal transport. Chronic OXPHOS impairment in FARS2 deficiency compromises these processes, leading to cumulative stress, impaired axonal transport, and eventual degeneration.[9][12][14] This can be characterized with GO terms such as **GO:0007268 (synaptic transmission)**, **GO:0006811 (ion transport)**, and **GO:0030042 (axonogenesis)**, as well as CL terms such as **CL:0000127 (corticospinal neuron)** or more generally **CL:0000107 (pyramidal neuron)**.

Mitochondrial dysfunction activates cellular stress pathways, including oxidative stress responses, unfolded protein response, and possibly intrinsic apoptosis pathways. ROS generation and ATP depletion can trigger activation of pro-apoptotic factors, mitochondrial permeability transition, and caspase cascades, culminating in neuronal cell death.[9][12][14] This is consistent with GO terms **GO:0006915 (apoptotic process)** and **GO:0008219 (cell death)**. In long axons, chronic energy failure may lead to “dying-back” axonopathy, where distal axonal segments degenerate first, leading to weakness and spasticity.[7][9] Demyelination or loss of myelinating oligodendrocytes in the corticospinal tracts may also occur secondarily, further impairing conduction velocity and amplifying spasticity.

Importantly, not all neurons are equally affected. Cortical interneurons and peripheral motor neurons may retain sufficient mitochondrial function to avoid severe degeneration, explaining why SPG77 primarily affects upper motor neuron pathways and leads to spastic paraplegia rather than peripheral neuropathy or diffuse encephalopathy.[7][9][12] In more severe FARS2 phenotypes, however, widespread cortical and subcortical involvement occurs, with seizures and global developmental delay, indicating more extensive neuronal vulnerability.[9][12][14] Thus, SPG77 represents the milder end of a continuum where neuronal vulnerability is graded by the extent and severity of mitochondrial dysfunction.

### 6.4 Metabolic Changes and Biochemical Abnormalities

SPG77 shares metabolic features with other mitochondrial disorders, though they are often less pronounced than in infantile FARS2 encephalopathy. The central metabolic abnormality is **impaired oxidative phosphorylation**, leading to reduced ATP generation and increased reliance on anaerobic glycolysis.[11][14] This shift can produce **lactic acidosis**, especially under stress conditions, though in SPG77 lactic acidosis may be mild or absent compared to infantile cases.[9][12] Elevated lactate reflects incomplete oxidation of pyruvate due to impaired electron transport chain function and can be captured with HPO term **HP:0002151 (Lactic acidosis)** and CHEBI term **CHEBI:18050 (lactate)**.

Secondary metabolic changes include increased generation of **reactive oxygen species (ROS)** such as superoxide and hydrogen peroxide, which can damage mitochondrial and cellular components and activate redox-sensitive signaling pathways.[14] ROS production is not directly measured in clinical practice but is inferred from the known effects of OXPHOS dysfunction. Lipid metabolism may be altered as mitochondria play roles in fatty acid oxidation and phospholipid synthesis, but specific lipidomic signatures for FARS2 deficiency have not been reported. Amino acid metabolism may be perturbed due to changes in mitochondrial protein turnover and metabolic flux, though again direct evidence in SPG77 is limited.

Biochemically, FARS2 deficiency can be described as an **enzyme deficiency of mtPheRS**, with downstream consequences for OXPHOS complexes. This can be annotated with BRENDA enzyme information for phenylalanyl-tRNA synthetase, and GO terms such as **GO:0004827 (phenylalanyl-tRNA ligase activity)**. Combined oxidative phosphorylation deficiency 14 (MIM 614946) reflects a specific biochemical abnormality where multiple complexes are affected, likely due to impaired assembly of mito-encoded subunits.[11][12] For SPG77, biochemical testing may show modest complex I deficiency or normal profiles, reflecting the subtler metabolic impact in milder phenotypes.

### 6.5 Immune System and Tissue Damage Mechanisms

There is no evidence that **immune-mediated mechanisms** such as autoimmunity or chronic inflammation are central drivers of SPG77. The disease does not exhibit features of inflammatory demyelination, such as those seen in multiple sclerosis or neuromyelitis optica, nor is there evidence of autoantibodies targeting neuronal or mitochondrial antigens.[7][9][12] The tissue damage in SPG77 arises from **metabolic stress, oxidative injury, and neurodegeneration** rather than from immune attack. This can be contrasted with immune-related GO terms like **GO:0006954 (inflammatory response)**, which do not appear prominently in SPG77 pathophysiology.

Tissue damage mechanisms, therefore, revolve around **oxidative stress and energy failure**, as described above. Chronic mitochondrial dysfunction leads to cumulative damage to axons and myelin in corticospinal tracts, possibly through mechanisms such as lipid peroxidation, protein nitration, and DNA damage, which ultimately compromise neuronal integrity.[9][12][14] In skeletal muscle, chronic spasticity and disuse lead to muscle fiber atrophy and replacement by connective tissue, contributing to amyotrophy and contractures.[13] These processes can be linked to GO terms **GO:0008150 (biological process)** such as **GO:0006979 (response to oxidative stress)** and **GO:0001501 (skeletal system development)**, and to UBERON terms such as **UBERON:0001017 (spinal cord)** and **UBERON:0001384 (corticospinal tract)** for anatomical localization.

### 6.6 Molecular Profiling and Advanced Technologies

To date, **advanced molecular profiling** methods such as transcriptomics, proteomics, metabolomics, and single-cell analysis have only begun to be applied to FARS2 deficiency, primarily in research settings. Nucleic Acids Research’s Drosophila study effectively uses proteomic and biochemical analysis to show that dFARS2 deficiency leads to reduced levels of mitochondrial proteins and impaired OXPHOS complexes.[14] However, systematic multi-omics profiling of human SPG77 tissues has not been reported, likely due to the rarity of the disease and limited access to affected tissues.

Single-cell analysis and spatial transcriptomics could, in principle, reveal cell-type-specific mitochondrial translational defects and neuronal vulnerability patterns in SPG77, but such data are not currently available. Similarly, functional genomic screens using CRISPR or RNAi in cell lines could elucidate pathways modulating FARS2-related phenotypes, but no reports specific to SPG77 exist. Consequently, knowledge bases should note that **multi-omics and single-cell data are not yet available for SPG77**, and that mechanistic insights are derived primarily from candidate gene models, biochemical assays, and animal models.

### 6.7 Upstream vs Downstream Mechanisms and Cell Types Involved

Within the causal chain, **upstream mechanisms** include the primary FARS2 mutation and resulting mtPheRS deficiency, defective tRNA aminoacylation, and impaired mitochondrial translation.[9][11][14] These upstream events occur in all cells expressing FARS2, but their functional impact varies by cell type. **Downstream mechanisms** include OXPHOS dysfunction, energy failure, ROS generation, activation of stress and apoptotic pathways, axonal degeneration, and clinical manifestations such as spasticity and seizures.[9][12][14]

The **cell types** most involved in SPG77 pathophysiology are upper motor neurons of the corticospinal tract (CL:0000127, CL:0000107), spinal cord motor neurons (CL:0000100), and possibly cerebellar and brainstem neurons in more complex cases.[7][9][12] Skeletal muscle fibers (CL:0000187) are indirectly affected by spasticity and disuse, leading to amyotrophy. Glial cells such as oligodendrocytes (CL:0002453) may be involved in demyelination secondary to axonal degeneration. Ontologically, the anatomical structures affected include the **motor cortex (UBERON:0000955)**, **internal capsule (UBERON:0002208)**, **brainstem (UBERON:0002298)**, and **spinal cord (UBERON:0001017)**, corresponding to the central motor pathways.

The overall pathophysiology of SPG77 thus integrates nuclear gene mutation, mitochondrial translation defects, OXPHOS dysfunction, selective neuronal vulnerability, and chronic neurodegeneration, yielding the clinical phenotype of hereditary spastic paraplegia.

## 7. Anatomical Structures Affected

### 7.1 Organ-Level Involvement: Central Nervous System and Musculoskeletal System

SPG77 primarily affects the **central nervous system (CNS)**, specifically the **motor system**, and secondarily involves the **musculoskeletal system**. The CNS structures implicated include the **motor cortex**, the **corticospinal tracts** traversing the internal capsule, brainstem, and spinal cord, and in some cases, cortical and subcortical regions involved in cognition and seizure generation.[7][9][12][13] The musculoskeletal system is affected via chronic spasticity and weakness, leading to contractures, scoliosis, foot deformities, and muscle amyotrophy.[9][12][13]

Anatomically, the **body systems** involved are primarily the **nervous system** and **musculoskeletal system**. Nervous system disease categorization is reflected in MSeqDR’s listing of SPG77 under nervous system disease tree numbers and slim mappings.[1] Musculoskeletal involvement is evident from Orphanet’s mention of muscle abnormalities, including weakness, hypotonia, tremor, and amyotrophy, and GeneReviews’ emphasis on orthopedic complications.[9][12][13] The cardiovascular, respiratory, digestive, and endocrine systems are not directly affected by SPG77, although severe infantile FARS2 phenotypes may have systemic metabolic manifestations.[9][12]

### 7.2 Tissue and Cell-Level Involvement

At the **tissue level**, SPG77 affects **nervous tissue** within the CNS, particularly white matter tracts (myelinated axons) and cellular layers of the motor cortex. It also involves **skeletal muscle tissue**, which responds to chronic upper motor neuron dysfunction with changes in tone, reflexes, and morphology.[7][9][12][13] Nervous tissue involvement can be localized to the corticospinal tracts, spinal cord anterior horn regions (though lower motor neurons are relatively spared), and occasionally cortical grey matter.[7][9][12] Muscle tissue involvement manifests as spasticity-induced stiffness, muscle fiber atrophy, and increased connective tissue deposition.

At the **cellular level**, as noted above, **upper motor neurons** (corticospinal neurons) are central to SPG77 pathology. These can be mapped to Cell Ontology terms such as CL:0000127 (corticospinal neuron) or CL:0000107 (pyramidal neuron). **Spinal interneurons** and **lower motor neurons** may also be affected indirectly through altered synaptic input and chronic spasticity. **Skeletal muscle fibers** (CL:0000187) respond to abnormal neural input with changes in fiber type, atrophy, and contracture formation. **Oligodendrocytes** (CL:0002453) and **astrocytes** (CL:0000127) might be involved in response to axonal degeneration, but direct evidence is limited.

### 7.3 Subcellular Components: Mitochondria and Related Compartments

The primary subcellular compartment involved in SPG77 is the **mitochondrion**, particularly the mitochondrial matrix where mtPheRS operates and the inner mitochondrial membrane where OXPHOS complexes reside.[11][14] This can be annotated with GO cellular component terms such as **GO:0005739 (mitochondrion)**, **GO:0005759 (mitochondrial matrix)**, and **GO:0005743 (mitochondrial inner membrane)**. FARS2 protein is localized to the mitochondrial matrix, and its dysfunction directly affects mitochondrial translation and respiratory chain function.[11][14]

Other subcellular compartments indirectly involved include the **axon** and **synapse**, where mitochondrial supply of ATP is crucial for maintaining membrane potentials, vesicle recycling, and neurotransmitter release. GO terms such as **GO:0030424 (axon)** and **GO:0045202 (synapse)** capture these structures. In diseases like SPG77, impaired mitochondrial function in these compartments leads to synaptic failure and axonal degeneration. Nuclear compartments and cytosolic protein synthesis are less directly affected, though compensatory mechanisms may attempt to maintain cellular energy balance.

### 7.4 Localization and Lateralization

Clinically, SPG77 presents predominantly with **bilateral lower limb involvement**, as spasticity and weakness affect both legs symmetrically.[7][9][12][13] Upper limb involvement may be milder or absent in many cases, reflecting the somatotopic organization of corticospinal tracts and differential vulnerability.[7] This bilateral, symmetric pattern is characteristic of hereditary spastic paraplegia and can be captured by HPO terms such as **HP:0003541 (Bilateral lower limb spasticity)**. Lateralization is not a major feature; unilateral or markedly asymmetric presentations are more suggestive of structural lesions rather than genetic HSP.

Anatomical localization in knowledge bases can use **UBERON** terms such as **UBERON:0000955 (primary motor cortex)**, **UBERON:0002208 (internal capsule)**, **UBERON:0002298 (brainstem)**, and **UBERON:0001017 (spinal cord)** to represent the central motor pathways affected. For musculoskeletal localization, terms such as **UBERON:0000978 (lower limb)** and **UBERON:0008897 (foot)** may be relevant.

## 8. Temporal Development

### 8.1 Age of Onset and Onset Pattern

SPG77 typically has **infancy-to-childhood onset**, with first symptoms appearing between six months of age and early school years.[9][12][13] GeneReviews specifies that FARS2-related later-onset spastic paraplegia should be considered in individuals aged six months and older with spastic paraplegia, and Orphanet lists age of onset as “Childhood, Infancy.”[9][12][13] Clinically, parents may notice delayed motor milestones, such as delayed sitting, crawling, or walking, or early gait abnormalities such as toe-walking, stiffness, or clumsiness. In some cases, onset may be insidious, with subtle signs progressing over months before diagnosis.

The **onset pattern** is typically **chronic and insidious**, rather than acute or subacute. There are no reports of SPG77 presenting as a sudden onset of spasticity due to an acute lesion, which would suggest stroke or spinal cord injury. Instead, symptoms gradually emerge as cortical motor pathways slowly degenerate or fail to mature properly under mitochondrial stress. Seizures, when present in SPG77, may have a more acute onset but usually occur in the context of chronic neurologic vulnerability rather than as isolated events.[9][12]

### 8.2 Disease Progression and Course

The **progression** of SPG77 is **slow and progressive**, with motor symptoms gradually worsening over years.[7][9][12][13] Early in the course, children may have mild gait disturbances and slightly increased reflexes, but still walk independently. Over time, spasticity increases, leading to stiffness, scissoring gait, and difficulty with stairs and running. Contractures, scoliosis, and foot deformities can develop, further limiting mobility.[9][12][13] GeneReviews recommends routine monitoring for orthopedic complications in later-onset FARS2-related spastic paraplegia, highlighting their role in disease progression.[9][12] The disease is **chronic and lifelong**, and although the rate of progression may vary, it generally does not remit spontaneously.

The **disease course pattern** can be described as **progressive without remissions** for motor symptoms, in contrast to relapsing-remitting disorders such as multiple sclerosis.[7] Seizures, however, may follow an **episodic** pattern and may resolve over time in later-onset FARS2 cases, leading to a mixed course where some symptoms improve while others worsen.[9][12] Developmental delays and cognitive deficits may show partial improvement with therapies and maturation, but residual impairments often remain. The overall pattern thus combines progressive motor disability with variable trajectories for non-motor features.

### 8.3 Disease Duration and Critical Periods

SPG77 is a **chronic lifelong condition**, with onset in infancy or childhood and persistence into adolescence and adulthood. The **duration** of disease spans decades, and affected individuals often face lifelong disability. In contrast, the infantile FARS2 phenotype has a shorter disease duration, with many children dying in early childhood due to severe epileptic encephalopathy and lactic acidosis.[9][12] GeneReviews notes that more than half of children with infantile-onset FARS2 deficiency die in early childhood, whereas later-onset cases have longer survival.[9][12]

There are **critical periods** of vulnerability and opportunity for intervention. Early childhood represents a critical window for establishing motor skills, correcting orthopedic deformities, and providing rehabilitative therapies that can maximize functional outcomes.[9][12][13] Failure to provide physical therapy, orthotic management, and orthopedic interventions during this period may lead to irreversible contractures and severe disability. Another critical period arises around puberty, when growth spurts can exacerbate scoliosis and musculoskeletal imbalances; close monitoring and interventions during this time may mitigate severe deformities.[9][12]

### 8.4 Remission Patterns and Temporal Variability

Motor symptoms in SPG77 do not **remit spontaneously**, and remission is not a recognized feature of the disease. However, as noted, seizures in later-onset FARS2 cases may **resolve over time**, representing partial remission in the epileptic phenotype.[9][12] Cognitive and language deficits may also improve with maturation and therapy, though not necessarily reaching normal levels. Consequently, the temporal pattern is varied across symptom domains: motor disability is steadily progressive, seizures and some developmental features may show partial remission or improvement, and orthopedic complications may be amenable to surgical correction or orthotic management, leading to local improvements.

Knowledge bases should capture these temporal nuances by annotating motor symptoms as chronic and progressive, seizures as episodic with possible remission, and developmental features as dynamic with partial catch-up.

## 9. Inheritance and Population

### 9.1 Inheritance Pattern, Penetrance, and Expressivity

SPG77 follows an **autosomal recessive** inheritance pattern. GeneReviews states that FARS2 deficiency, including SPG77, is inherited in an autosomal recessive manner, and that at conception each sibling of an affected individual has a 25% chance of being affected, a 50% chance of being an asymptomatic carrier, and a 25% chance of being unaffected and not a carrier.[12] OMIM similarly lists spastic paraplegia 77, autosomal recessive, with inheritance “AR.”[8][11] ClinVar submissions for FARS2 variants associated with hereditary spastic paraplegia 77 also assume autosomal recessive inheritance.[2][3][4][6]

Penetrance for **pathogenic biallelic FARS2 variants** appears to be **complete or near-complete**, as all individuals reported with such variants show some manifestation of FARS2 deficiency, though the specific phenotype (infantile encephalopathy vs later-onset spastic paraplegia) may vary.[9][11][12][14] Expressivity is **variable**, with a spectrum ranging from severe infantile-onset epileptic encephalopathy with lactic acidosis and poor prognosis to milder childhood-onset spastic paraplegia with modest developmental delay and longer survival.[9][12][14] GeneReviews emphasizes this spectrum and the fact that the same gene (FARS2) can underlie both phenotypes.[9][12] This variability likely reflects differences in variant type, location, and residual mtPheRS activity, rather than incomplete penetrance.

There is no evidence of **genetic anticipation**, as FARS2 deficiency does not involve unstable repeat expansions and does not show progressive worsening across generations beyond what is expected from autosomal recessive inheritance.[9][11][12] Germline mosaicism has not been reported, and most FARS2 variants appear to be fully present in parental germline DNA. Knowledge bases should therefore classify SPG77 as an autosomal recessive disorder with complete penetrance of biallelic pathogenic variants and variable expressivity across a clinical spectrum.

### 9.2 Epidemiology: Prevalence and Incidence

SPG77 is an **extremely rare** disorder. Orphanet reports a prevalence of **<1 / 1,000,000** for autosomal recessive spastic paraplegia type 77.[13] GeneReviews notes that FARS2 deficiency, encompassing both infantile and later-onset phenotypes, has been reported in **37 individuals from 25 families**.[9][12] Given that SPG77 represents approximately 30% of FARS2 deficiency cases, the number of published SPG77 individuals is likely in the low tens.[9][12][13]

Formal **incidence** rates for SPG77 have not been established, as population-based registries do not exist for such rare conditions. The incidence is likely well below 1 per million live births, and may vary significantly by population due to founder effects and consanguinity patterns.[11][13] For global burden of disease calculations, SPG77 would contribute minimally to overall HSP prevalence but remains important at an individual and family level.

### 9.3 Population Demographics and Geographic Distribution

SPG77 has been reported in families from different geographic regions and ethnic backgrounds. Yang et al. described four affected siblings from a **consanguineous Chinese family**, indicating that FARS2 mutations and SPG77 can occur in East Asian populations.[11] Other cases have been reported in European and other populations, based on GeneReviews and OMIM summaries.[9][11][12] However, the total number of families (25 across all FARS2 phenotypes

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 2 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 59 |
| Resolved | 53 |
| Unresolved (possible confabulation) | 4 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 51 |
| Terms named correctly | 23 |
| Terms named as a **different** term | 11 |
| Terms whose name is worth a second look | 17 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002357` (1 mention) - the report calls it "Abnormal gait"; HP calls it **obsolete Dysphasia**
- `HP:0001250` (2 mentions) - the report calls it "Spasticity", "Seizures"; HP calls it **Seizure**
- `HP:0003477` (1 mention) - the report calls it "Extensor plantar response"; HP calls it **Peripheral axonal neuropathy**
- `HP:0002151` (2 mentions) - the report calls it "Lactic acidosis"; HP calls it **Increased circulating lactate concentration**
- `GO:0030042` (1 mention) - the report calls it "axonogenesis"; GO calls it **actin filament depolymerization**
- `CL:0000127` (4 mentions) - the report calls it "corticospinal neuron", "astrocytes"; CL calls it **astrocyte**
- `UBERON:0001017` (3 mentions) - the report calls it "spinal cord"; UBERON calls it **central nervous system**
- `UBERON:0001384` (1 mention) - the report calls it "corticospinal tract"; UBERON calls it **primary motor cortex**
- `UBERON:0000955` (2 mentions) - the report calls it "primary motor cortex"; UBERON calls it **brain**
- `HP:0003541` (1 mention) - the report calls it "Bilateral lower limb spasticity"; HP calls it **Urinary glycosaminoglycan excretion**
- `UBERON:0008897` (1 mention) - the report calls it "foot"; UBERON calls it **fin**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0001295` (1 mention) - HP does not contain this term
- `HP:0007320` (1 mention) - HP does not contain this term
- `HP:0002471` (1 mention), reported as "Expressive language delay" - HP does not contain this term
- `HP:0002369` (1 mention), reported as "Cerebral white matter abnormalities" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0002357` (obsolete Dysphasia) (1 mention) - replaced by `HP:0002381`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002061` (2 mentions) - the report calls it "Spastic gait"; HP calls it **Lower limb spasticity**, and lists "Spastic lower limb" among its other names
- `HP:0001288` (1 mention) - the report calls it "Gait ataxia"; HP calls it **Gait disturbance**, and lists "Gait abnormalities" among its other names
- `HP:0001263` (1 mention) - the report calls it "Developmental delay"; HP calls it **Global developmental delay**, and lists "Developmental delay" among its other names
- `HP:0002143` (1 mention) - the report calls it "Abnormal brain MRI"; HP calls it **Abnormal spinal cord morphology**
- `HP:0002079` (1 mention) - the report calls it "Corpus callosum hypoplasia"; HP calls it **Hypoplasia of the corpus callosum**, and lists "Corpus callosum hypoplasia" among its other names
- `GO:0006428` (1 mention) - the report calls it "tRNA aminoacylation"; GO calls it **isoleucyl-tRNA aminoacylation**
- `GO:0006415` (1 mention) - the report calls it "translation"; GO calls it **translational termination**, and lists "translation termination" among its other names
- `GO:0007268` (1 mention) - the report calls it "synaptic transmission"; GO calls it **chemical synaptic transmission**, and lists "synaptic transmission" among its other names
- `GO:0006811` (1 mention) - the report calls it "ion transport"; GO calls it **monoatomic ion transport**, and lists "ion transport" among its other names
- `CL:0000107` (3 mentions) - the report calls it "pyramidal neuron"; CL calls it **autonomic neuron**
- `CHEBI:18050` (1 mention) - the report calls it "lactate"; CHEBI calls it **L-glutamine**, and lists "GLUTAMINE" among its other names
- `GO:0004827` (1 mention) - the report calls it "phenylalanyl-tRNA ligase activity"; GO calls it **proline-tRNA ligase activity**, and lists "prolinyl-tRNA ligase activity" among its other names
- `GO:0008150` (1 mention) - the report calls it "biological process"; GO calls it **biological_process**, and lists "biological process" among its other names
- `CL:0000187` (2 mentions) - the report calls it "Skeletal muscle fibers"; CL calls it **muscle cell**, and lists "muscle fiber" among its other names
- `CL:0002453` (2 mentions) - the report calls it "Oligodendrocytes"; CL calls it **oligodendrocyte precursor cell**, and lists "Polydendrocyte" among its other names
- `UBERON:0002208` (2 mentions) - the report calls it "internal capsule"; UBERON calls it **sternebra**, and lists "sternebral bone" among its other names
- `UBERON:0000978` (1 mention) - the report calls it "lower limb"; UBERON calls it **leg**, and lists "lower extremity" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0001250` - called "Spasticity", "Seizures"
- `CL:0000127` - called "corticospinal neuron", "astrocytes"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.