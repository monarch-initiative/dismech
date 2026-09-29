---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-24T20:45:08.014863'
end_time: '2026-09-24T20:48:57.975144'
duration_seconds: 229.96
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: AICA-ribosiduria
  mondo_id: MONDO:0012099
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
citation_count: 20
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 6
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 95
  verified: 86
  not_found: 4
  obsolete: 1
  unverifiable: 4
  confabulation_rate: 0.044
  labels_checked: 29
  labels_matching: 10
  labels_mismatched: 12
  mislabelled_terms:
  - term_id: NCIT:C129830
    reported_labels:
    - Inborn Error of Purine Metabolism; broader class
    ontology_label: Monoallelic Mutation
  - term_id: UBERON:0000967
    reported_labels:
    - choroid of eye
    ontology_label: obsolete adult thoracic sensillum
  - term_id: NCIT:C164023
    reported_labels:
    - metabolite biomarker
    ontology_label: Initial Genomic Sequencing Date
  - term_id: NCIT:C1593
    reported_labels:
    - antiepileptic agent
    ontology_label: Recombinant Chemokine
  - term_id: NCIT:C15689
    reported_labels:
    - seizure prophylaxis
    ontology_label: Drug Resistance Inhibition Treatment
  - term_id: NCIT:C116410
    reported_labels:
    - vision rehabilitation
    ontology_label: Phospholipid-Transporting ATPase ABCA1
  - term_id: NCIT:C15677
    reported_labels:
    - metabolic therapy
    ontology_label: Axillary Lymph Node Dissection
  - term_id: NCIT:C50736
    reported_labels:
    - spinal fusion surgery
    ontology_label: Rupture Of Hyaloid Face
  - term_id: NCIT:C49288
    reported_labels:
    - physical therapy
    ontology_label: AS04 Adjuvant
  - term_id: NCIT:C21240
    reported_labels:
    - occupational therapy
    ontology_label: Translation Process Gene
  - term_id: NCIT:C49287
    reported_labels:
    - speech therapy
    ontology_label: Effective
  - term_id: NCIT:C49154
    reported_labels:
    - supportive care
    ontology_label: Statement
  labels_variant: 7
  unresolved_terms:
  - HP:0007891
  - HP:0008021
  - HP:0003242
  - FMA:50801
  obsolete_terms:
  - term_id: UBERON:0000967
    ontology_label: obsolete adult thoracic sensillum
  unresolvable_prefixes:
  - ORPHA
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** AICA-ribosiduria
- **MONDO ID:** MONDO:0012099 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **AICA-ribosiduria** covering all of the
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

# AICA‑ribosiduria (ATIC deficiency): Comprehensive Disease Characteristics and Mechanistic Overview

AICA‑ribosiduria, also known as ATIC deficiency, is an ultra‑rare autosomal recessive inborn error of de novo purine biosynthesis characterized by accumulation of 5‑amino‑4‑imidazolecarboxamide riboside (AICA‑riboside) and related intermediates, and by a syndromic constellation of severe neurodevelopmental impairment, profound visual deficit due to chorioretinal atrophy, ante‑ and postnatal growth restriction, and progressive, often severe scoliosis.[1][3][14] Since the first description in 2004 of a female infant with congenital blindness, profound neurological impairment, and massive urinary excretion of AICA‑riboside,[3][13] only a handful of further patients have been reported, including three additional severely affected individuals and a long‑term update of the index patient,[12][14] a child from India,[6] and two siblings with a comparatively milder phenotype.[5][17] This tiny case series nevertheless permits delineation of a core clinical picture and a plausible pathophysiologic mechanism centered on biallelic loss‑of‑function variants in the ATIC gene encoding the bifunctional enzyme AICAR transformylase/IMP cyclohydrolase that catalyzes the final two steps of de novo purine synthesis.[11][16] Recent work has expanded the clinical spectrum toward less severe intellectual disability and visual impairment[5][17] and has provided first‑in‑human evidence that suppressing de novo purine biosynthesis by exogenous purine supplementation can reduce the abnormal metabolic signature, suggesting a rational therapeutic avenue in a disorder for which no specific treatment had previously existed.[7] This report synthesizes the available evidence on AICA‑ribosiduria across disease information, etiology, phenotype, molecular mechanisms, anatomy, temporal course, epidemiology, diagnostics, prognosis, treatment, prevention, animal models, and experimental systems, and maps these features to biomedical ontologies (MONDO, HPO, GO, CL, UBERON, CHEBI, NCIT) to support structured disease knowledge base development.

## 1. Disease Information

### 1.1 Overview and nosology

AICA‑ribosiduria is an ultra‑rare Mendelian metabolic disease classified among inborn errors of purine, pyrimidine, or nucleotide metabolism in ICD‑11 and among metabolic disorders in Orphanet and KEGG Disease.[1][8] It represents a specific defect in de novo purine biosynthesis due to deficiency of the bifunctional enzyme AICAR transformylase/IMP cyclohydrolase (protein PURH, gene symbol ATIC), which catalyzes the penultimate and final steps in the pathway converting 5‑phosphoribosylpyrophosphate (PRPP) to inosine monophosphate (IMP).[11][13][16] Biochemically, AICA‑ribosiduria is defined by massive accumulation and urinary excretion of AICA‑riboside, the dephosphorylated nucleoside corresponding to AICAR (also known as ZMP), and by accumulation of AICAR and its di‑ and triphosphate derivatives in erythrocytes and fibroblasts.[3][13] Clinically, the core phenotype initially appeared “neurologically devastating,” with profound intellectual disability, congenital blindness due to chorioretinal atrophy, severe hypotonia, and marked growth retardation.[3][13][14] Subsequent case series have refined this picture into a syndromic association of severe to profound global neurodevelopmental impairment, severe visual impairment, ante‑ and postnatal growth impairment, and severe scoliosis, frequently accompanied by early‑onset epilepsy and dysmorphic facial features.[1][12][14][17]

In nosological terms, AICA‑ribosiduria is recognized as a distinct disease entity by multiple curated resources. Orphanet lists the disease under ORPHA:250977 and categorizes it as an “inborn error of purine metabolism,” with a prevalence below 1 per 1,000,000 and autosomal recessive inheritance.[1][15] OMIM assigns phenotype entry 608688 (“AICA‑ribosiduria due to ATIC deficiency”) and gene entry 601731 (“ATIC, 5‑aminoimidazole‑4‑carboxamide ribonucleotide formyltransferase/IMP cyclohydrolase”) and explicitly links the phenotype to homozygous or compound heterozygous mutations in ATIC at cytogenetic location 2q35.[2][11] MedGen and the Monarch Initiative map the condition to MONDO:0012099, and SNOMED CT includes terms such as “5‑amino‑4‑imidazole carboxamide ribosiduria” and “ATIC deficiency” to represent the disease.[4][9] KEGG Disease lists AICA‑ribosiduria under identifier H00966, placing it within the ICD‑11 rubric 5C55.0Y (“Inborn errors of purine metabolism, other specified”).[8] ICD‑10 classifies the condition under E79.8 (“Other disorders of purine and pyrimidine metabolism”), reflecting its rarity and limited recognition in general coding schemes.[1][8]

### 1.2 Key identifiers and synonyms

Key identifiers across major biomedical databases include OMIM:608688 for the phenotype, OMIM:601731 for the ATIC gene, Orphanet ORPHA:250977, MONDO:0012099, MeSH C563876, and UMLS concept C1837530.[1][2][4][8] These identifiers underpin cross‑resource integration and should be captured explicitly in any disease knowledge base entry. Relevant ontology mappings for disease‑level representation include MONDO:0012099 (AICA‑ribosiduria), NCIT:C129830 (Inborn Error of Purine Metabolism; broader class), and the ICD‑11 concept 5C55.0Y: AICA‑ribosiduria.[4][8]

Common synonyms and alternative names provide important cues for text mining and data harmonization. Orphanet and OMIM list several synonymous labels: “5‑amino‑4‑imidazole carboxamide ribosiduria,” “AICA‑ribosiduria due to ATIC deficiency,” “AICAR transformylase/IMP cyclohydrolase deficiency,” “ATIC deficiency,” “AICA ribosiduria,” and “AICA‑ribosiduria due to ATIC deficiency.”[1][2][4][9][15] Older literature sometimes emphasizes the enzyme defect, referring to “AICAR transformylase deficiency” or “PURH deficiency,” while biochemical descriptions may focus on the hallmark metabolite, for example “AICA‑riboside accumulation syndrome.”[3][13][14] For ontology alignment, “AICA‑ribosiduria due to ATIC deficiency” is the preferred fully specified name in OMIM and MedGen.[2][4]

### 1.3 Data sources and evidence type

Because of its extreme rarity, knowledge about AICA‑ribosiduria is derived almost entirely from aggregated disease‑level resources and a small number of detailed case reports and case series in the primary literature, rather than from large cohorts or electronic health record–based studies. The seminal description by Marie et al. in 2004 reports detailed clinical, biochemical, and molecular findings in a single female infant and includes in vitro assays of patient fibroblasts and recombinant ATIC protein.[3][13] Ramond et al. (2020) present three additional patients from two independent families and a 15‑year clinical update on the index case, providing the most substantial longitudinal natural history data.[12][14] Dewulf et al. (2022) describe two siblings with a milder phenotype and novel ATIC variants, expanding the clinical spectrum.[5][17] A 2022 case report from India contributes another severely affected child and underscores the utility of whole‑exome sequencing (WES) in diagnosis.[6] Finally, a 2024 report on dietary purine supplementation as a treatment strategy provides clinical and biochemical data from a teenage patient.[7]

In addition to these human clinical data, mechanistic understanding relies on biochemical pathway knowledge from KEGG and OMIM, protein function annotations from GeneCards and UniProt, and general purine metabolism literature, supplemented by in vitro studies of AICAR and AICA‑riboside in cell systems.[8][11][13][16] No large‑scale omics datasets, genome‑wide association studies, or population‑based epidemiologic studies exist for AICA‑ribosiduria, and this absence must be explicitly recognized in any comprehensive disease representation.

## 2. Etiology

### 2.1 Genetic causal factors: ATIC loss‑of‑function

The primary and, as far as current evidence indicates, sole causal factor in AICA‑ribosiduria is biallelic germline loss‑of‑function mutation in the ATIC gene located on chromosome 2q35.[1][2][6][11][14][17] ATIC encodes a bifunctional cytosolic enzyme with two distinct catalytic domains: an N‑terminal AICAR formyltransferase (AICARFT; EC 2.1.2.3) that transfers a formyl group from 10‑formyltetrahydrofolate to AICAR, producing formyl‑AICAR (FAICAR), and a C‑terminal IMP cyclohydrolase (IMPCHase; EC 3.5.4.10) that cyclizes FAICAR to inosine monophosphate (IMP).[11][13][16] In the index patient, Marie et al. demonstrated profound deficiency of AICAR transformylase activity and partial deficiency (about 40% of normal) of IMP cyclohydrolase activity in fibroblast extracts.[3][13] Sequencing revealed compound heterozygosity for a missense variant c.1277A>G (p.Lys426Arg; K426R) affecting the transformylase domain and a frameshift variant caused by a duplication–deletion event, both predicted to severely impair ATIC function.[3][13] Recombinant ATIC protein carrying the K426R mutation completely lacked AICAR transformylase activity, while retaining some IMP cyclohydrolase activity, supporting a direct causal relationship between ATIC dysfunction and the biochemical phenotype.[3][13][11]

Subsequent cases have confirmed the requirement for biallelic pathogenic ATIC variants. Ramond et al. described three patients with different combinations of missense, nonsense, and frameshift mutations, all in trans, and all associated with marked accumulation of AICA‑riboside.[12][14] The Indian case report identified compound heterozygosity for a novel splice site variant c.1321‑2A>G and the previously described K426R missense variant, with segregation consistent with autosomal recessive inheritance.[6] Dewulf et al. reported two siblings with a milder phenotype, each carrying a nonsense variant c.421C>T (p.Arg141Ter) and a missense variant c.1753A>G (p.Thr585Ala), again in trans and segregating in the family.[5][17] In all instances, no other plausible genetic cause was identified, and the ATIC variants were absent or extremely rare in population databases (when checked), fulfilling criteria for pathogenicity under ACMG/AMP guidelines.[2][5][6][14][17]

Thus, the etiological model is a monogenic autosomal recessive disorder in which homozygous or compound heterozygous ATIC loss‑of‑function alleles cause deficiency of de novo IMP synthesis, leading to accumulation of upstream intermediates and consequent multisystem toxicity.[2][11][13][14][17] There is currently no evidence for environmental, infectious, or somatic contributors to disease initiation, though environmental factors may modulate disease expression (see below).[7]

### 2.2 Variant spectrum and putative genotype–phenotype relationships

The spectrum of reported ATIC variants in AICA‑ribosiduria includes missense substitutions affecting conserved residues in either catalytic domain, nonsense mutations introducing premature termination codons, frameshift mutations, and splice site alterations predicted to disrupt correct mRNA processing.[3][6][12][14][17] The K426R missense variant, located within the transformylase region, has been functionally characterized and shown to abolish AICAR transformylase activity while partially preserving IMP cyclohydrolase function.[3][13] Other variants, such as the nonsense allele p.Arg141Ter and missense p.Thr585Ala, have not yet been biochemically characterized in detail but are predicted to severely reduce ATIC function based on domain localization and conservation.[5][17]

Ramond et al. proposed that alteration of transformylase activity might be associated with more severe clinical impairment than alteration of the cyclohydrolase activity, largely based on the profound neurologic deficits in the index patient carrying K426R and a frameshift mutation versus somewhat less catastrophic features in some individuals with mutations more heavily impacting the cyclohydrolase domain.[14] However, they also emphasized that robust genotype–phenotype correlations are not yet established, given the extremely small number of patients and the presence of multiple different variants in most individuals.[1][14][15][17] Orphanet likewise notes that “no genotype–phenotype relationship has been identified,” reflecting this uncertainty.[1][15]

The milder phenotype in the siblings described by Dewulf et al. raises the possibility that specific combinations of ATIC alleles may yield partial residual activity compatible with less severe neurodevelopmental disruption.[5][17] Nevertheless, AICA‑riboside accumulation in these siblings was still markedly elevated, and their intellectual and visual impairments were clinically significant, suggesting that even “milder” variants cross a threshold of purine pathway disruption that leads to disease.[5][17] Future functional studies of individual variants, potentially in cellular or animal models, will be essential to elucidate the structural and catalytic consequences of particular ATIC mutations and to refine genotype–phenotype mapping.

### 2.3 Risk factors: genetic and environmental

Given the Mendelian autosomal recessive etiology, the principal risk factor for AICA‑ribosiduria is carrier status for pathogenic ATIC variants in both parents, leading to a 25% recurrence risk for each pregnancy.[1][2][15] Orphanet notes explicitly that the pattern of inheritance is autosomal recessive and that affected parents have a one‑in‑four risk of having another affected child; this underpins genetic counseling recommendations.[1][15] In populations or families with high levels of consanguinity, the chance of inheriting the same pathogenic ATIC allele from both parents is increased, and consanguinity therefore represents a risk factor for occurrence of AICA‑ribosiduria.[2][6][14] Several reported families involve consanguineous unions or small genetic isolates, although detailed population genetic analysis is lacking.[12][14][17]

Beyond ATIC variants and consanguinity, no genetic susceptibility loci, modifier genes, or common polymorphisms have been associated with AICA‑ribosiduria, reflecting the tiny number of cases and the rarity of ATIC variants in general population databases.[2][5][6][17] Genome‑wide association studies, ClinGen curation, and other large‑scale genetic epidemiology resources do not list AICA‑ribosiduria or ATIC deficiency, and no GWAS signals have been linked to this phenotype. Thus, at present, AICA‑ribosiduria appears to be caused exclusively by rare, highly penetrant ATIC loss‑of‑function variants, without evidence for polygenic risk.

Environmental risk factors in the conventional sense (toxins, lifestyle, occupational exposures, infectious agents) have not been implicated in causing AICA‑ribosiduria, nor is there evidence that such factors significantly modify disease onset or severity. The condition is congenital or neonatal in onset, and the major clinical features are evident in infancy, arguing strongly against acquired environmental etiologies.[1][3][12][14][15] It is conceivable that severe folate deficiency, which would reduce availability of 10‑formyltetrahydrofolate, might exacerbate the functional consequences of ATIC deficiency, but such interactions have not been documented in patients.

### 2.4 Protective factors and gene–environment interactions

Data on protective factors are essentially absent for this ultra‑rare disease. However, recent work suggests that high exogenous purine supply, via a purine‑enriched diet, can suppress de novo purine biosynthesis and thereby reduce accumulation of AICA‑riboside and succinyladenosine in a teenage patient with ATIC deficiency.[7] In this case, urinary excretion of AICA‑riboside and succinyladenosine fell substantially after introduction of a diet enriched in purines, consistent with diversion of nucleotide synthesis toward the salvage pathway.[7] While this intervention targets metabolic flux rather than the underlying genetic defect, it illustrates a form of gene–environment interaction: the environmental modification (dietary purine intake) alters the metabolic consequences of the genetic lesion (ATIC loss‑of‑function), potentially mitigating biochemical toxicity.

The authors of the treatment report interpreted exogenous purine substitution as a “promising treatment approach” rather than a definitive protective factor; nonetheless, their findings imply that environmental manipulation of purine load might confer some protection against metabolite accumulation and perhaps against tissue damage.[7] No evidence exists that such dietary interventions prevent disease occurrence in carriers or fetuses at risk, and their impact on clinical outcomes (neurologic and visual function, growth) remains to be established in longer‑term, multi‑patient studies.

Beyond diet, no systematic data exist on lifestyle factors, micronutrients, or environmental exposures that modify AICA‑ribosiduria severity. The extreme rarity of the condition, the severity of baseline impairment, and the young age of most patients make such studies difficult. As such, any statements about protective environmental factors must be considered speculative and inferred from general principles of purine metabolism rather than from direct evidence.

## 3. Phenotypes

### 3.1 Core neurologic and developmental phenotypes

The most consistent and central phenotype in AICA‑ribosiduria is severe to profound global neurodevelopmental impairment, manifesting as marked intellectual disability, motor delay, and language delay.[1][3][12][14][17] The index patient described by Marie et al. presented in infancy with severe hypotonia, absent motor milestones, and profound neurologic deficits, and over time she remained profoundly intellectually disabled with minimal communication and dependency for all activities of daily living.[3][13][12] Ramond et al. synthesized clinical features across the first four patients (the index case plus three new cases) and defined the neurological picture as “severe‑to‑profound global neurodevelopmental impairment” with early‑onset epilepsy in most cases and frequent pharmacoresistance.[12][14] Dewulf et al.’s two siblings exhibited neurodevelopmental delay involving motor and language skills, but their cognitive impairment was less extreme; they were able to walk, had some verbal communication, and attended special education.[5][17] Nonetheless, even in these “mild” cases, intellectual disability was clinically significant.

Suggested HPO terms for these phenotypes include intellectual disability (HP:0001249), with more specific mapping to severe intellectual disability (HP:0010864) or profound intellectual disability (HP:0002342) in the more severely affected patients.[4][12][14][17] Global developmental delay (HP:0001263) and motor development delay (HP:0001270) capture the early onset of delayed milestones, while hypotonia (HP:0001252) reflects the reduced muscle tone observed in infancy.[3][12][14] Epilepsy (HP:0001250), infantile spasms (HP:0012469) where present, and early‑onset, sometimes pharmacoresistant seizures (HP:0002373) form part of the neurological phenotype.[1][3][12][14][17]

Severity is generally high in the original and Ramond cohorts, with profound deficits evident in infancy and persisting into adolescence and adulthood.[12][14] Symptom onset is prenatal to neonatal, in the sense that impaired brain development appears intrinsic to the disease and clinical signs such as hypotonia, visual deficit, and developmental delay are apparent in the first months of life.[1][3][12][14][15] The progression is relatively stable rather than fluctuating, with developmental gains being limited and plateauing early, and with superimposed complications such as scoliosis and epilepsy.[12][14] Quality of life impact is severe, with patients requiring lifelong, extensive support and being unable to live independently; Orphanet notes that “to date all individuals affected by AICA‑ribosiduria require extensive support.”[1][15] Dewulf et al.’s siblings, while less severely impaired, still had significant limitations in daily functioning and required special educational arrangements.[5][17]

### 3.2 Ocular and visual phenotypes

Severe visual impairment, often present from birth, is a defining feature of AICA‑ribosiduria. Marie et al.’s index patient had congenital blindness, and examination revealed marked chorioretinal atrophy.[3][13] Ramond et al. summarized ocular findings across four patients as “severe visual impairment due to chorioretinal atrophy,” with fundoscopic examination showing diffuse retinal dystrophy and loss of choriocapillaris.[12][14] The Orphanet and MedGen entries likewise emphasize severe visual impairment as a core symptom.[1][4][15] In the two siblings with milder phenotype, ocular involvement included retinal dystrophy and visual impairment, although vision was not completely absent.[5][17]

Relevant HPO terms include visual impairment (HP:0000505), with severe visual impairment (HP:0001141) and blindness (HP:0000618) for the most affected individuals.[4][12][13][14] Chorioretinal atrophy (HP:0007891) and retinal dystrophy (HP:0008021) specifically capture the structural pathology observed on retinal imaging.[12][14][17] Nystagmus (HP:0000639) and optic nerve anomalies (HP:0000602) may be present in some patients, based on broader summarizations of similar disorders and MedGen notes, although detailed ophthalmologic descriptions are limited.[4][18] The age of onset is congenital or neonatal, with parents and physicians noting absent visual tracking and abnormal fundus early in life.[3][12][14]

The impact on quality of life is profound, as blindness or severe visual impairment greatly limits interaction with the environment, learning, and mobility, particularly when combined with major cognitive and motor deficits. Patients depend heavily on caregivers and require specialized multi‑sensory educational approaches and assistive devices. No specific treatment exists for the chorioretinal atrophy, and Orphanet notes that management is limited to standard correction of refractive errors such as hypermetropia when present; the degenerative retinal changes themselves are not amenable to current therapies.[1][15] Suggested UBERON terms for anatomical mapping include retina (UBERON:0000966), choroid of eye (UBERON:0000967), and optic nerve (UBERON:0000949).

### 3.3 Growth and skeletal phenotypes

Ante‑ and postnatal growth impairment is another hallmark of AICA‑ribosiduria. Ramond et al. reported intrauterine growth retardation in several patients, with low birth weight and length, and persistent postnatal growth failure leading to short stature and low weight for age.[12][14] Orphanet describes “ante‑postnatal growth impairment” as a core feature.[1][15] Dewulf et al.’s siblings also had growth retardation, though somewhat less marked than in the severely affected earlier cases.[5][17] Suggested HPO terms include intrauterine growth retardation (HP:0001511), failure to thrive (HP:0001508), and short stature (HP:0004322).[1][12][14][17]

Skeletal involvement is dominated by scoliosis, which in many patients is severe and progressive, requiring orthopedic management. Ramond et al. defined severe scoliosis as part of the core phenotype and noted that spinal curvature worsened with age in the index patient and others.[12][14] Orphanet emphasizes that scoliosis should be evaluated and treated aggressively when present.[1][15] In addition to scoliosis, dysmorphic features of the knees, elbows, and shoulders were noted in the initial case, reflecting abnormal joint and bone development.[3][9][12][14] Patients also exhibit coarse facial features and an upturned nose, suggesting broader skeletal dysmorphogenesis.[2][4][12][14][18] HPO terms capturing these features include scoliosis (HP:0002650), kyphoscoliosis (HP:0002751), joint contractures (HP:0001371), coarse facial features (HP:0000347), and upturned nose (HP:0000463).[2][4][12][14]

The progression of scoliosis appears to be gradual and progressive, paralleling general growth and neuromuscular status. In the index patient, severe scoliosis developed during childhood and adolescent years and contributed to physical disability and pain.[12] Quality of life impact is substantial: spinal deformity can impair mobility, cause chronic discomfort, and complicate care, particularly in non‑ambulatory patients. Orthopedic interventions, including bracing and, in some cases, surgical correction, may be considered, but experience is limited.[1][12][15]

### 3.4 Additional systemic phenotypes

In addition to the core neurologic, ocular, growth, and skeletal features, AICA‑ribosiduria is associated, in some patients, with cardiovascular, hepatic, renal, and genital anomalies. Ramond et al. and MedGen note that less common features may include aortic coarctation, chronic hepatic cytolysis, minor genital malformations, and nephrocalcinosis.[2][4][12][14][18] Aortic coarctation (HP:0002136) has been observed in at least one patient, representing a potentially serious congenital heart defect that may require surgical correction.[12][14] Chronic hepatic cytolysis, reflecting persistent elevation of liver transaminases (hypertransaminasemia, HP:0002910), suggests subclinical hepatocellular injury, though overt liver failure has not been reported.[12][14][17] Nephrocalcinosis (HP:0004724), documented in some cases, may predispose to renal impairment or urinary tract complications.[12][14] Minor genital malformations, such as cryptorchidism or hypospadias (HP:0000028, HP:0000047), have also been reported.[2][4][12][14]

Facial dysmorphism, beyond coarse facies and upturned nose, includes features such as thick lips, broad nasal bridge, and other subtle anomalies, although descriptions vary and are not fully standardized.[3][12][14][17] MedGen mentions additional possible features such as microcephaly, abnormal foot or hand posturing, and kyphoscoliosis.[18] These suggest that AICA‑ribosiduria affects multiple systems during embryonic development, consistent with the essential role of purine nucleotides in cell proliferation and differentiation.

Frequency estimates for these additional phenotypes are necessarily imprecise due to small numbers. Ramond et al. characterize them as “less frequently observed,” implying that while they are part of the disease spectrum, they are not universally present.[12][14] The clinical impact varies: aortic coarctation and nephrocalcinosis can be serious and require cardiovascular or nephrologic management, whereas minor genital anomalies may have limited functional significance. From an ontology perspective, these systemic features expand the phenotype profile and should be captured to support comprehensive representation in HPO and related schemas.

### 3.5 Behavioral and quality of life considerations

Structured assessment of behavioral changes and quality of life in AICA‑ribosiduria has not been reported in the literature. Nevertheless, based on the described cognitive and sensory impairments, patients are likely to have major limitations in social interaction, adaptive behavior, and emotional regulation. Severe intellectual disability and blindness inherently restrict communication abilities and the capacity to learn and engage with caregivers and peers. In the milder siblings, social interactions are somewhat more preserved, but they still require special education and support.[5][17]

If one were to apply standardized instruments such as the EQ‑5D or SF‑36, most domains (mobility, self‑care, usual activities, pain/discomfort, anxiety/depression) would be markedly impaired in the severely affected patients.[1][12][14] Informal reports in Ramond et al. indicate that the index patient, now in adulthood, continues to require full‑time care and exhibits limited spontaneous communication.[12] These observations underline the heavy burden placed on families and healthcare systems, and the importance of multidisciplinary supportive care.

### 3.6 Summary of HPO mapping

In summary, key HPO terms for AICA‑ribosiduria include intellectual disability (HP:0001249), severe/profound intellectual disability (HP:0010864, HP:0002342), global developmental delay (HP:0001263), motor delay (HP:0001270), hypotonia (HP:0001252), epilepsy (HP:0001250), early‑onset seizures (HP:0002373), visual impairment (HP:0000505), chorioretinal atrophy (HP:0007891), retinal dystrophy (HP:0008021), intrauterine growth retardation (HP:0001511), failure to thrive (HP:0001508), short stature (HP:0004322), scoliosis (HP:0002650), coarse facies (HP:0000347), upturned nose (HP:0000463), aortic coarctation (HP:0002136), hypertransaminasemia (HP:0002910), nephrocalcinosis (HP:0004724), and genital anomalies (HP:0003242).[1][2][3][4][12][14][17][18] Frequency can at present only be qualitatively categorized (core versus less common), and precise percentages are not available. These mappings provide a foundation for computational phenotype representation in disease knowledge bases.

## 4. Genetic and Molecular Information

### 4.1 ATIC gene and protein function

ATIC (HGNC:795, OMIM:601731) encodes a bifunctional enzyme named 5‑aminoimidazole‑4‑carboxamide ribonucleotide formyltransferase/IMP cyclohydrolase (AICARFT/IMPCHase), also known as PURH, localized to the cytosol and expressed widely across tissues.[11][13][16] The N‑terminal domain (approximately residues 1–330) exhibits AICAR formyltransferase activity, catalyzing the reaction of AICAR (ZMP) with 10‑formyltetrahydrofolate to produce FAICAR and tetrahydrofolate.[13][16] The C‑terminal domain (roughly residues 331–591) has IMP cyclohydrolase activity, converting FAICAR to inosine monophosphate (IMP) via cyclization.[11][13][16] These two reactions constitute steps 9 and 10 of the de novo purine biosynthetic pathway, which begins with PRPP and sequentially produces inosine monophosphate.[13][16]

GeneCards and UniProt note that ATIC is a protein‑coding gene with enzymatic activity in the “de novo purine biosynthetic process,” and that mutation in ATIC results in AICA‑ribosiduria.[16] OMIM describes the ATIC protein as catalyzing the penultimate and final steps of de novo purine biosynthesis and refers to earlier biochemical studies that defined these activities.[11][13] The importance of ATIC in cellular metabolism is underscored by the ubiquity of purine nucleotides as building blocks of DNA and RNA, energy carriers (ATP, GTP), coenzymes (NAD, FAD), and signaling molecules (cAMP, cGMP). Disruption of ATIC function, therefore, has potential consequences for multiple cellular processes, although cells can partially compensate via the purine salvage pathway.[13][16]

Suggested GO terms for ATIC functions include “de novo IMP biosynthetic process” (GO:0006189), “de novo purine nucleobase biosynthetic process” (GO:0006207), “AICAR formyltransferase activity” (GO:0000034), and “IMP cyclohydrolase activity” (GO:0003921). For cellular localization, the ATIC protein is primarily cytosolic, corresponding to GO:0005829 (cytosol).[11][13][16] In terms of pathways, KEGG places ATIC within the purine metabolism pathway (hsa00670) and also notes its involvement in antifolate resistance, given that antifolate drugs can target steps in one‑carbon metabolism linked to purine synthesis.[8]

### 4.2 De novo purine biosynthesis pathway and metabolite context

The de novo purine biosynthetic pathway comprises ten enzymatic steps that convert PRPP to IMP, with several multifunctional enzymes handling multiple steps.[13] AICAR (5‑amino‑1‑(5‑phospho‑β‑D‑ribosyl)imidazole‑4‑carboxamide), also known as ZMP, is the penultimate intermediate in this pathway. It is formed from the preceding intermediate SAICAR (succinyl‑AICAR) by the enzyme adenylosuccinate lyase (ADSL).[13] ATIC’s AICAR formyltransferase domain uses AICAR and 10‑formyltetrahydrofolate to produce FAICAR, and the IMP cyclohydrolase domain then converts FAICAR to IMP.[11][13][16] IMP is the branch point for synthesis of AMP and GMP, the primary purine nucleotides.

In AICA‑ribosiduria, ATIC deficiency leads to accumulation of AICAR and its derivatives. Marie et al. showed that ZMP and its di‑ and triphosphate accumulated in the index patient’s erythrocytes.[3][13] The dephosphorylated nucleoside AICA‑riboside is formed by dephosphorylation of AICAR, most likely via IMP–GMP 5′‑nucleotidase.[3][13] Massive excretion of AICA‑riboside in urine was the biochemical hallmark that led to diagnosis in the initial case.[3][13] Ramond et al. and Dewulf et al. report that patients also exhibit elevated urinary levels of SAICA‑riboside (the nucleoside corresponding to SAICAR) and succinyladenosine (S‑Ado), reflecting upstream effects on ADSL activity and succinylated intermediates.[14][17] These metabolites are shared with adenylosuccinate lyase deficiency, one of the few other known inborn errors of purine biosynthesis.[13]

Suggested CHEBI identifiers for key metabolites include AICAR (CHEBI:18012), inosine monophosphate (IMP; CHEBI:17372), succinyladenosine (CHEBI:18348), and AICA‑riboside (a nucleoside classified as a modified riboside, though a specific CHEBI ID may need verification). The accumulation of AICAR is particularly important because AICAR is a known AMP analog that can activate AMP‑activated protein kinase (AMPK), altering cellular energy metabolism; exogenous AICAR is widely used experimentally to stimulate AMPK.[13] This raises the possibility that ATIC deficiency leads not only to substrate accumulation but also to chronic activation of AMPK, with systemic metabolic consequences.

### 4.3 Pathogenic variants: classes and consequences

Reported ATIC variants in AICA‑ribosiduria fall into several classes: missense substitutions, nonsense mutations, frameshift insertions or deletions, and splice site variants.[3][6][12][14][17] Missense variants such as K426R (c.1277A>G), Q214H (c.642G>C), and Thr585Ala (c.1753A>G) alter amino acid residues within catalytic domains and are predicted to disrupt enzymatic activity.[3][7][14][17] Functional studies of K426R demonstrated complete loss of AICAR formyltransferase activity with retention of about 40% IMP cyclohydrolase activity, confirming a loss‑of‑function effect and illustrating domain‑specific impact.[3][13] Nonsense mutations such as p.Arg141Ter (c.421C>T) introduce premature stop codons, likely leading to truncated proteins subject to nonsense‑mediated decay or severely impaired function.[5][17] Frameshift variants, including the duplication–deletion event described in the index case, similarly produce truncated proteins or aberrant sequences.[3][13][14] Splice site variants such as c.1321‑2A>G are predicted to disrupt normal exon–intron recognition and cause exon skipping or intron retention, with consequent protein dysfunction.[6]

ClinVar and HGMD have not extensively catalogued these variants, given the rarity of the disease, but OMIM notes several as “pathogenic” based on segregation, functional data, and phenotype consistency.[2][11][14] Allele frequencies in population databases such as gnomAD are extremely low or zero, indicating that these are not common polymorphisms.[5][6][17] All known pathogenic variants are germline and segregate in families according to autosomal recessive inheritance; no somatic ATIC mutations have been linked to AICA‑ribosiduria. Somatic ATIC alterations in cancer (e.g., antifolate resistance) represent a different context and are not implicated in this congenital metabolic disorder.[8][16]

The functional consequences of ATIC pathogenic variants can be summarized as partial or complete loss of AICAR formyltransferase and/or IMP cyclohydrolase activities, leading to impaired conversion of AICAR to FAICAR and IMP, accumulation of upstream intermediates, and potentially reduced availability of IMP for downstream AMP/GMP synthesis.[3][13][14][17] Whether IMP production is globally deficient in patients is somewhat less clear, because salvage pathways can supply purines and may compensate in part.[13][16] Nonetheless, the combination of substrate accumulation and altered nucleotide pools appears sufficient to disrupt development and tissue homeostasis.

### 4.4 Modifier genes, epigenetics, and chromosomal abnormalities

No modifier genes have been identified that alter the severity or expression of AICA‑ribosiduria. Variability in phenotypic severity between patients, such as the contrast between the profoundly impaired index case and the milder siblings described by Dewulf et al., is plausibly explained by differences in ATIC variant combinations or stochastic developmental factors rather than by known genetic modifiers.[12][14][17] Given the central role of purine metabolism, it is conceivable that variation in genes encoding salvage pathway enzymes (e.g., HPRT1, APRT) or folate metabolism enzymes could modulate phenotypic expression, but such interactions remain hypothetical and have not been studied in this disease.

Epigenetic information specific to AICA‑ribosiduria is not available. There are no reports of disease‑associated changes in DNA methylation, histone modifications, or chromatin architecture in ATIC‑deficient patients, nor of epigenetic regulation of ATIC expression leading to similar phenotypes. ATIC is a housekeeping metabolic gene broadly expressed in proliferating cells, and epigenetic modulation may be relatively constrained. As such, epigenetics does not currently form part of the disease mechanism, although future multi‑omics studies might explore whether chronic metabolic stress in ATIC deficiency induces secondary epigenetic changes.

Large‑scale chromosomal abnormalities (aneuploidy, translocations, inversions) have not been associated with AICA‑ribosiduria. All reported patients harbor point mutations or small indels in ATIC on an otherwise structurally normal chromosome 2.[2][6][12][14][17] Chromosomal microarray (CMA) and karyotyping are not primary diagnostic tools for this disease, except as part of broader evaluation of developmental delay where they may help rule out other syndromic causes.

### 4.5 Molecular profiling and omics data

To date, there are no published transcriptomics, proteomics, metabolomics, or lipidomics datasets specifically profiling ATIC‑deficient patients beyond targeted measurement of purine metabolites. The biochemical hallmark—elevated urinary AICA‑riboside, SAICA‑riboside, and succinyladenosine, and accumulated AICAR and derivatives in erythrocytes and fibroblasts—constitutes a focused metabolomic signature.[3][13][14][17] Broad untargeted metabolomics or integrated multi‑omics analyses have not been reported.

Single‑cell, spatial transcriptomics, and functional genomics screens (CRISPR, RNAi) have not been applied to AICA‑ribosiduria as a clinical entity. However, in experimental contexts, CRISPR knockout or knockdown of ATIC in cell lines has been used to study purine metabolism and antifolate resistance, though not specifically linked to the patient phenotype.[8][16] These models could in principle be leveraged to explore disease mechanisms, but the literature connecting them to human AICA‑ribosiduria cases is sparse.

## 5. Environmental Information

### 5.1 Environmental factors and lifestyle

As an inborn error of metabolism caused by germline ATIC mutations, AICA‑ribosiduria is not induced by environmental toxins, radiation, pollution, smoking, alcohol, or infectious agents. None of the case reports implicate such factors in disease onset, and the congenital/neonatal presentation strongly argues for a purely genetic etiology.[1][3][6][12][14][15][17] Environmental exposures may influence general health and comorbidities in patients, but they are not primary drivers of the disease.

Lifestyle factors such as diet, physical activity, and exposure to folate or other vitamins might modulate metabolic flux through purine pathways and could theoretically affect disease severity. The purine‑enriched diet intervention described by Dewulf et al. indicates that high dietary purine intake can suppress de novo synthesis and reduce accumulation of toxic intermediates.[7] However, this is a therapeutic manipulation rather than a naturally occurring lifestyle factor. No systematic data are available on the baseline diets of patients or their impact on clinical course.

### 5.2 Infectious agents

No infectious agents are associated with AICA‑ribosiduria. The disease does not appear to confer specific susceptibility to infections beyond what might arise from severe disability and immobility (e.g., respiratory infections in bed‑bound individuals). Immune system involvement is not a central feature, and there is no suggestion of an autoimmune or immunodeficiency component.[1][3][12][14]

### 5.3 Environmental modulation of metabolism

The main environmental factor that interacts mechanistically with AICA‑ribosiduria is exogenous purine supply. Dewulf et al. reported that increasing dietary purine intake led to reduced urinary excretion of AICA‑riboside and succinyladenosine in a teenage patient with ATIC deficiency.[7] The interpretation is that high purine availability favors salvage pathways (recycling of hypoxanthine, guanine, and adenine) and downregulates de novo synthesis, thereby lowering flux through the impaired ATIC‑dependent steps.[7] This represents a targeted environmental modulation of metabolic pathways and may, over time, mitigate tissue exposure to toxic intermediates.

From an ontology perspective, dietary purine intake can be conceptualized as a chemical exposure (CHEBI:26401 for purine) and a clinical intervention (NCIT:C15666 for dietary therapy). The interaction with ATIC deficiency is a classic gene–environment interaction at the metabolic level. However, evidence for clinical benefit beyond metabolite normalization remains limited to a single case, and further studies are needed to evaluate whether such environmental modulation improves neurological, ocular, or growth outcomes.

## 6. Mechanism / Pathophysiology

### 6.1 Ordered causal chain from mutation to phenotype

Step 1: Biallelic loss‑of‑function mutation in the ATIC gene leads to reduced or absent AICAR formyltransferase and impairments in IMP cyclohydrolase enzymatic activity in cells of multiple tissues.[3][11][13][14][17]

Step 2: ATIC enzymatic deficiency results in impaired conversion of AICAR (ZMP) to FAICAR and FAICAR to IMP, which in turn leads to intracellular accumulation of AICAR and its di‑ and triphosphate derivatives (ZMP, ZDP, ZTP) and to increased formation of AICA‑riboside through dephosphorylation of AICAR.[3][13][14][17]

Step 3: Accumulated AICAR and its nucleoside AICA‑riboside are exported or leak from cells, leading to massive urinary excretion of AICA‑riboside and elevated levels of related intermediates such as SAICA‑riboside and succinyladenosine, reflecting upstream perturbation of de novo purine synthesis.[3][13][14][17]

Step 4: Chronic intracellular accumulation of AICAR and related metabolites leads to activation of AMP‑activated protein kinase (AMPK) and disruption of cellular energy metabolism, nucleotide balance, and one‑carbon metabolism, inferred from known effects of AICAR as an AMP analog in experimental systems.[13]

Step 5: Metabolic dysregulation in neural progenitor cells, neurons, and glia results in impaired neurodevelopment, synaptogenesis, and myelination, leading to severe global neurodevelopmental impairment, hypotonia, and susceptibility to seizures.[3][12][13][14][17]

Step 6: In retinal and choroidal tissues, ATIC dysfunction and metabolite accumulation lead to chorioretinal dystrophy and atrophy, possibly via direct cytotoxicity to photoreceptors and retinal pigment epithelial cells, resulting in congenital or early‑onset severe visual impairment.[3][12][13][14][17]

Step 7: In growth plate chondrocytes and osteoblasts, purine pathway disruption and general metabolic stress impair proliferation and matrix production, contributing to intrauterine and postnatal growth retardation and to skeletal deformities such as severe scoliosis and joint dysmorphism.[12][14][17]

Step 8: In cardiovascular, hepatic, renal, and genital tissues, metabolite toxicity and energy imbalance may lead to additional anomalies such as aortic coarctation, chronic hepatic cytolysis, nephrocalcinosis, and minor genital malformations, though the specific tissue‑level mechanisms are less well characterized and remain partly inferred.[2][4][12][14][18]

Step 9: Over time, systemic accumulation of toxic metabolites and chronic energy stress result in permanent structural damage to central nervous system, retina, skeleton, and other organs, leading to a stable but severely impaired clinical phenotype with limited developmental gains and progressive musculoskeletal complications.[12][14]

Step 10: Environmental modulation of purine metabolism, such as a purine‑enriched diet, can suppress de novo synthesis in favor of salvage, reducing metabolite accumulation and urinary excretion, which may alleviate metabolic stress and potentially slow further tissue damage, although this benefit is inferred from biochemical improvement and has yet to be fully demonstrated clinically.[7]

### 6.2 Molecular pathways: purine metabolism and AMPK signaling

The central molecular pathway implicated in AICA‑ribosiduria is de novo purine metabolism (KEGG hsa00670), specifically the terminal steps converting AICAR to FAICAR and IMP.[8][13][16] ATIC deficiency leads to a bottleneck at this stage, with upstream accumulation of AICAR. AICAR is structurally similar to AMP and is known to activate AMP‑activated protein kinase (AMPK), a master regulator of cellular energy homeostasis.[13] In experimental systems, exogenous AICAR is widely used as a pharmacological AMPK activator, promoting catabolic pathways (e.g., fatty acid oxidation, glucose uptake) and inhibiting anabolic processes (e.g., protein and lipid synthesis) in response to “energy stress.” By analogy, chronic endogenous accumulation of AICAR in ATIC‑deficient cells is likely to result in sustained AMPK activation.

AMPK activation and altered purine pools can affect numerous downstream pathways. Reduced IMP availability may limit synthesis of AMP and GMP, potentially impacting DNA and RNA synthesis, cell cycle progression, and proliferation.[13][16] One‑carbon metabolism, linked via 10‑formyltetrahydrofolate, may be perturbed, with implications for nucleotide synthesis and methylation reactions. At the same time, salvage pathways may be upregulated to compensate, utilizing hypoxanthine, guanine, and adenine recycled from nucleic acid turnover.[7][8][13] The interplay between de novo and salvage pathways defines the overall nucleotide supply, and ATIC deficiency shifts the balance toward salvage.

Suggested GO terms for these processes include “purine nucleotide biosynthetic process” (GO:0006164), “AMP‑activated protein kinase signaling” (GO:0032147), and “cellular response to energy stress” (GO:0071322). While direct measurement of AMPK activity in ATIC‑deficient patients has not been reported, the mechanistic inference from AICAR’s known properties is strong. AICA‑riboside itself, when taken up by cells, is phosphorylated back to AICAR and can thereby contribute to AMPK activation, further enhancing metabolic stress.[3][13]

### 6.3 Cellular processes: proliferation, apoptosis, and differentiation

At the cellular level, ATIC deficiency and metabolite accumulation likely impact proliferation, apoptosis, and differentiation. Purine nucleotides are essential for DNA replication; impaired de novo synthesis may slow cell cycle progression, particularly in rapidly dividing embryonic cells such as neural progenitors and chondrocytes.[13][16] Energy stress and AMPK activation can induce cell cycle arrest and promote autophagy, facilitating adaptation to nutrient limitation.[13] In the developing brain, such alterations may reduce the number of neurons and glia, impair axonal growth, and affect synapse formation.

In addition, toxic metabolites may have direct cytotoxic effects. Ramond et al. note that “data from literature points toward a cytotoxic mechanism of the accumulated AICA‑riboside,” suggesting that high intracellular concentrations of AICA‑riboside and related intermediates damage cells.[14] This cytotoxicity may involve oxidative stress, mitochondrial dysfunction, or interference with nucleoside transport and metabolism. Experimental exposure of control fibroblasts to AICA‑riboside led to accumulation of AICAR in patient cells but not in controls, indicating altered metabolic handling and supporting a distinct cellular stress response in ATIC deficiency.[3][13]

Suggested GO terms include “regulation of cell proliferation” (GO:0042127), “apoptotic process” (GO:0006915), and “cell differentiation” (GO:0030154). The exact balance between proliferation impairment and increased cell death in specific tissues (brain, retina, bone) remains to be quantified, but the net effect is reduced tissue growth and function.

### 6.4 Protein dysfunction: structural and catalytic aspects

Protein dysfunction in AICA‑ribosiduria arises from missense and truncating variants that alter ATIC’s structure and catalytic sites. The K426R mutation, located in the transformylase region, replaces a lysine residue with arginine; functional studies showed that recombinant K426R ATIC lacks AICAR transformylase activity, implying that Lys426 is critical for catalysis or substrate binding.[3][13] Other missense variants in the cyclohydrolase domain, such as Thr585Ala and Q214H, may affect folding or active site geometry, reducing IMP production.[7][17] Nonsense and frameshift variants likely result in truncated proteins lacking one or both catalytic domains, or in unstable proteins degraded by cellular quality control mechanisms.[3][6][14][17]

Such structural perturbations can be conceptualized with InterPro or Pfam domain architectures, where the transformylase and cyclohydrolase domains are annotated as distinct modules. The loss of catalytic activity is a classic loss‑of‑function effect, fitting into the ACMG category of “null variants in a gene where loss of function is a known mechanism of disease.”[2][11][14] Suggested GO terms for protein dysfunction include “loss of protein function” (not a standard GO term but conceptually linked to “negative regulation of catalytic activity” GO:0008270) and “protein folding” (GO:0006457).

### 6.5 Metabolic changes and tissue damage mechanisms

Metabolic changes in AICA‑ribosiduria include accumulation of AICAR and AICA‑riboside, elevated SAICA‑riboside and succinyladenosine, and possibly altered levels of ATP, GTP, and other nucleotides.[3][13][14][17] These changes can increase osmotic load, perturb intracellular signaling, and disrupt energy balance. The cytotoxic mechanism of AICA‑riboside, as suggested by Ramond et al., may involve incorporation into nucleic acids or interference with DNA/RNA polymerases, though specific studies are lacking.[14] Succinylated nucleosides (SAICA‑riboside, succinyladenosine) have been implicated in neurotoxicity in adenylosuccinate lyase deficiency, and their accumulation in AICA‑ribosiduria may similarly contribute to brain and retinal damage.[13][17]

Tissue damage likely occurs via a combination of metabolic stress, impaired nucleotide supply, and direct toxicity to mitochondria and other organelles. In the retina, photoreceptor and retinal pigment epithelial cells are highly metabolically active and rely on robust nucleotide and energy supply; chronic purine pathway disruption may cause degeneration and chorioretinal atrophy.[3][12][14][17] In the brain, neurons and oligodendrocytes may be particularly vulnerable to purine imbalance, resulting in impaired synaptic connectivity and myelination. In bone and cartilage, metabolic stress may impair matrix synthesis, leading to skeletal deformities.

Suggested GO terms include “response to oxidative stress” (GO:0006979), “mitochondrial dysfunction” (mapped via “mitochondrial organization” GO:0007005), and “cell death” (GO:0008219). Subcellular compartments likely involved include mitochondrion (GO:0005739), nucleus (GO:0005634), cytosol (GO:0005829), and lysosome (GO:0005764) in the context of autophagy.

### 6.6 Immune system involvement and epigenetic changes

The immune system does not appear to be centrally involved in AICA‑ribosiduria. There are no reports of chronic inflammation, autoimmunity, or immunodeficiency specific to the disease.[1][3][12][14] While severe disability may predispose to infections, these are secondary complications rather than primary features. Consequently, immune pathways and epigenetic changes have not been a focus of mechanistic studies.

Epigenetic changes may occur as secondary phenomena in chronically stressed cells, but no direct evidence has been reported. Future research could explore whether long‑term ATIC deficiency and purine imbalance affect DNA methylation patterns or histone marks in neural tissue, potentially contributing to altered gene expression.

### 6.7 Cell types and ontology mapping

Key cell types involved in AICA‑ribosiduria include neural progenitor cells, neurons (CL:0000540), astrocytes (CL:0000127), oligodendrocytes (CL:0000128), retinal photoreceptors (CL:0000210), retinal pigment epithelial cells (CL:0000746), chondrocytes (CL:0000138), osteoblasts (CL:0000148), skeletal muscle cells (CL:0000737), hepatocytes (CL:0000182), renal tubular epithelial cells (CL:0002518), and vascular endothelial cells (CL:0000096).[12][14][17][18] All of these cell types depend on robust purine nucleotide supply for proliferation, differentiation, and function, and are therefore vulnerable to ATIC deficiency.

Mapping to CL terms supports structured representation of cell‑type–specific vulnerability. For example, damage to CL:0000210 photoreceptor cells in UBERON:0000966 retina underlies HP:0007891 chorioretinal atrophy. Impaired proliferation of CL:0000138 chondrocytes in UBERON:0002419 vertebral column growth plates contributes to HP:0002650 scoliosis. Dysfunction of CL:0000540 neurons in UBERON:0000955 brain leads to HP:0001249 intellectual disability and HP:0001250 epilepsy. These mappings illustrate how ATIC deficiency acts across diverse cell types via a common metabolic defect.

## 7. Anatomical Structures Affected

### 7.1 Organ‑level involvement

Organ‑level involvement in AICA‑ribosiduria is multisystemic, with primary effects on the central nervous system (CNS), eyes, musculoskeletal system (spine and extremities), and growth system (whole‑body development), and secondary involvement of cardiovascular, hepatic, renal, and genital organs.[1][2][3][12][14][17][18] The CNS, particularly the cerebral cortex, subcortical structures, and cerebellum, is the main site of neurodevelopmental impairment, manifesting as intellectual disability, epilepsy, and hypotonia.[3][12][14] UBERON terms capturing these structures include brain (UBERON:0000955), cerebral cortex (UBERON:0000956), and cerebellum (UBERON:0002037).

The eyes, specifically the retina and choroid, are profoundly affected, leading to chorioretinal atrophy and severe visual impairment.[3][12][14][17] UBERON:0000966 (retina) and UBERON:0000967 (choroid of eye) represent these structures. The vertebral column (UBERON:0002419), ribs, and associated musculature constitute the skeletal system impacted by scoliosis and musculoskeletal deformities.[12][14][17] The cardiovascular system, particularly aorta (UBERON:0000947), can be involved via aortic coarctation.[12][14] The liver (UBERON:0002107) shows cytolysis in some patients, while kidneys (UBERON:0002113) exhibit nephrocalcinosis.[12][14][17] Genital organs (e.g., testis UBERON:0000473, penis UBERON:0000989) are affected in patients with minor genital malformations.[12][14]

Secondary organ involvement may arise from chronic immobility and skeletal deformity, such as restrictive lung disease due to severe scoliosis, though such complications have not been systematically reported. The endocrine system per se is not prominently featured in case descriptions, but growth impairment may reflect subtle endocrine interactions.

### 7.2 Tissue and cell‑level involvement

At the tissue level, AICA‑ribosiduria affects nervous tissue (neuronal and glial networks), photoreceptor and retinal pigment epithelial tissues in the eye, hyaline cartilage in growth plates, bone tissue in vertebrae and long bones, cardiac muscle and vascular endothelium in the heart and aorta, liver parenchyma, and renal interstitium.[3][12][14][17][18] Nervous tissue comprises neurons, astrocytes, oligodendrocytes, and microglia; these cells rely on balanced nucleotide supply for axonal growth, synaptic transmission, myelination, and neuroinflammatory homeostasis. In the retina, photoreceptors and retinal pigment epithelial cells support phototransduction and maintenance of the outer segments; purine metabolism is critical for their high energy demands.

Chondrocytes in the growth plate and osteoblasts in bone matrix are responsible for longitudinal growth and bone formation, and are particularly sensitive to metabolic disruptions during development. Skeletal muscle fibers depend on ATP for contraction and may be affected indirectly via hypotonia and reduced activity.[3][12][14] Hepatocytes metabolize purines and ammonium; chronic cytolysis suggests metabolic stress. Renal tubular epithelial cells handle reabsorption and secretion of metabolites, and deposition of calcium salts (nephrocalcinosis) indicates perturbation of mineral metabolism.

Cell Ontology terms provide structured representation of these cell types, as noted above. Tissue types can be categorized as nervous tissue (FMA:50801), epithelial tissues (e.g., retinal pigment epithelium), connective tissue (cartilage, bone), muscle tissue (skeletal and cardiac), and parenchymal tissues (liver, kidney). The broad involvement of multiple tissues underscores the systemic nature of ATIC deficiency.

### 7.3 Subcellular compartments and localization

Subcellular compartments implicated in AICA‑ribosiduria include the cytosol, where ATIC resides and de novo purine synthesis occurs, mitochondria, which are affected by energy stress and potential toxicity of accumulated nucleotides, nucleus, where DNA replication and transcription depend on nucleotide pools, and lysosomes, involved in autophagic responses.[11][13][16] GO cellular component terms such as cytosol (GO:0005829), mitochondrion (GO:0005739), nucleus (GO:0005634), and lysosome (GO:0005764) provide granularity.

Localization of ATIC within the cytosolic compartment allows interactions with other purine pathway enzymes and with folate metabolism. AICAR and its derivatives may diffuse within cells; their effects on AMPK and other sensors occur primarily in the cytosol and nucleus. Mitochondrial function may be perturbed by altered ATP/ADP ratios and reactive oxygen species generated under metabolic stress.

### 7.4 Lateralization and symmetry

Clinical descriptions of scoliosis suggest that spinal deformity can be asymmetric, with curves favoring one side, but detailed lateralization patterns are not consistently reported.[12][14] Chorioretinal atrophy appears bilateral, affecting both eyes.[3][12][14][17] Neurologic impairment is diffuse and not lateralized. Aortic coarctation is anatomically localized to a segment of the aorta but does not have a lateral counterpart. Thus, lateralization is not a central feature of the disease phenotype.

## 8. Temporal Development

### 8.1 Onset: prenatal and neonatal

AICA‑ribosiduria is a congenital disorder with onset in the prenatal or neonatal period. Orphanet specifies age of onset as “antenatal, infancy, neonatal,” reflecting the observation that growth retardation and structural anomalies may be evident in utero, while neurologic and visual deficits are apparent soon after birth.[1][15] Intrauterine growth retardation has been documented in several patients, indicating that ATIC deficiency affects embryonic and fetal development.[12][14][17] Congenital blindness suggests that chorioretinal atrophy develops during fetal retinal maturation.[3][13]

Postnatal onset of overt symptoms, such as hypotonia, developmental delay, seizures, and failure to thrive, occurs within the first months of life. The Indian case report describes a child presenting early with neurodevelopmental delay and visual impairment.[6] The two mild siblings also showed developmental delay from infancy, though their cognitive impairment became fully apparent in later childhood.[5][17] Overall, the onset pattern is chronic and insidious in terms of metabolic defect, but clinically acute in the sense that major deficits are present from early infancy.

### 8.2 Progression and disease course

The disease course of AICA‑ribosiduria is characterized by early severe impairment, limited developmental gains, and progressive musculoskeletal complications, with relatively stable cardiometabolic status. Ramond et al.’s long‑term follow‑up of the index patient into adulthood shows that profound intellectual disability and blindness persisted, while scoliosis progressed and required ongoing orthopedic management.[12] Epilepsy, when present, may be pharmacoresistant and can contribute to additional morbidity.[12][14] Growth impairment continues throughout childhood, resulting in short stature and low weight.[12][14][17]

The progression rate of neurologic and visual deficits is rapid in early life (as they become apparent) but stabilizes thereafter, with limited recovery potential. Scoliosis and skeletal deformities progress gradually with growth, potentially reaching a plateau in adulthood. Hepatic cytolysis and nephrocalcinosis may persist but do not necessarily lead to organ failure within the limited observational periods.[12][14][17] The overall pattern is chronic and lifelong, with little remission.

Disease stages can be conceptualized as early (infancy: emergent neurologic and visual deficits, initial growth retardation), intermediate (childhood: consolidation of severe disability, onset/progression of scoliosis, epilepsy), and advanced (adolescence/adulthood: stable profound impairment, established musculoskeletal deformity, ongoing supportive care). However, formal staging schemes do not exist for this ultra‑rare disorder.

### 8.3 Remission, critical periods, and intervention windows

Spontaneous remission of AICA‑ribosiduria does not occur; the genetic defect and metabolic consequences are persistent. Treatment‑induced remission in terms of clinical symptoms has not yet been demonstrated, although biochemical remission (reduced metabolite excretion) has been achieved through dietary intervention.[7] Critical periods of vulnerability include fetal development of the CNS and retina, where purine metabolism is vital for proliferation and differentiation, and early postnatal brain development. Interventions aimed at reducing metabolite toxicity (e.g., exogenous purines) might be most effective if introduced early, though human data are not yet available.

Opportunities for intervention include prenatal diagnosis (allowing informed reproductive decisions) and early postnatal diagnosis enabling prompt initiation of supportive therapies (physical, occupational, visual rehabilitation) and experimental metabolic treatments.[1][6][15] Genetic counseling is a key preventive strategy at the family level.

## 9. Inheritance and Population

### 9.1 Epidemiology: prevalence and incidence

AICA‑ribosiduria is exceedingly rare. Orphanet estimates prevalence as less than 1 per 1,000,000, and notes that only four affected individuals from three independent families had been reported worldwide as of 2020.[1][15] Ramond et al.’s 2020 paper adds three new cases and a long‑term update on the index case, bringing the total to four historical patients.[12][14] Dewulf et al. (2022) add two siblings with milder phenotype, and the Indian case report contributes one more patient, suggesting that at least seven individuals from five families have been described.[5][6][17] The treatment report referencing a teenage patient with K426R and Q214H variants may represent one of these previously reported patients or an additional case.[7] In any event, the global number of documented individuals remains in the single digits.

Incidence, defined as new cases per 100,000 per year, has not been formally estimated, but given the paucity of reports over two decades, it is likely on the order of 0.001–0.01 per 100,000 or lower. AICA‑ribosiduria meets criteria for an ultra‑rare disease and falls under the category of “orphan” conditions. No national registries or population‑based surveillance programs exist for this specific disorder.

### 9.2 Inheritance pattern, penetrance, and expressivity

The inheritance pattern is autosomal recessive. All reported patients carry homozygous or compound heterozygous pathogenic variants in ATIC, and unaffected family members are heterozygous carriers.[1][2][6][12][14][15][17] Orphanet and OMIM explicitly classify AICA‑ribosiduria as autosomal recessive, and genetic counseling resources emphasize a 25% recurrence risk for carrier couples.[1][2][15] This pattern suggests complete penetrance for severe biochemical defect in individuals with biallelic ATIC loss‑of‑function variants.

Clinical penetrance—the extent to which metabolite accumulation translates into overt disease—appears high, as all documented biallelic ATIC variant carriers have presented with significant neurodevelopmental and visual impairment.[3][6][12][14][17] There is, however, variability in expressivity, with some patients exhibiting more profound intellectual disability and blindness, and others having milder cognitive and visual deficits.[5][17] Dewulf et al.’s siblings illustrate this variable expressivity, yet their biochemical signature remains similar to that of more severely affected individuals.[17] There is no evidence for age‑dependent penetrance (e.g., late‑onset forms), and symptoms manifest in infancy.

Genetic anticipation, in which disease severity increases in successive generations, is not observed. Germline mosaicism has not been reported, though it cannot be excluded given small family sizes. Founder effects have not been documented for ATIC variants, but some recurrent mutations (such as K426R) suggest possible localized clustering.[3][6][12][14]

Carrier frequency in the general population is unknown but presumably extremely low, given the rarity of reported cases and the absence of common ATIC variants in population databases.[2][5][6][17] In consanguineous families or isolated populations, carrier frequency may be higher for particular variants.

### 9.3 Population demographics, sex ratio, and geographic distribution

Affected individuals reported to date come from diverse geographic backgrounds, including European families (Belgium, France), an Indian family, and possibly other regions.[6][12][14][17] The index patient described by Marie et al. was European.[3][13] Dewulf et al.’s siblings were reported from a European center, and Ramond et al.’s cases likely span French/Belgian cohorts.[12][14][17] The Indian case represents the first report from India.[6] Thus, AICA‑ribosiduria appears to occur sporadically across populations, without a clear geographic clustering, although the small numbers limit inference.

Sex ratio cannot be reliably estimated from the limited data set. The index patient was female,[3][13] and subsequent cases include both males and females, but detailed reporting is incomplete. Given autosomal recessive inheritance, there is no expected sex bias.

Age distribution reflects congenital onset and lifelong persistence. Patients are diagnosed in infancy or early childhood and have been followed into adolescence and young adulthood.[12][14] The oldest reported individual, the index patient, reached 20 years of age as of the 2020 Orphanet update.[1][15] Life expectancy beyond this is unknown.

## 10. Diagnostics

### 10.1 Clinical and biochemical tests

Diagnostic evaluation of AICA‑ribosiduria hinges on detecting characteristic purine metabolites and confirming ATIC gene mutations. The initial clue in Marie et al.’s index case was a positive urinary Bratton–Marshall test, a colorimetric assay that detects aromatic amines, suggesting accumulation of AICA‑riboside.[3][13] Subsequent high‑performance liquid chromatography (HPLC) analysis revealed massive excretion of AICA‑riboside in urine, establishing the biochemical hallmark.[3][13] Orphanet notes that a positive urine Bratton–Marshall test can suggest AICA‑riboside accumulation, and that definitive diagnosis can be confirmed by HPLC analysis.[1][15]

Ramond et al. and Dewulf et al. report that patients exhibit elevated levels of AICA‑riboside, SAICA‑riboside, and succinyladenosine in urine, and that these metabolites can be quantified by HPLC or mass spectrometry as part of specialized purine metabolite panels.[14][17] This pattern, while overlapping with adenylosuccinate lyase deficiency, shows distinctive AICA‑riboside predominance. In erythrocytes and fibroblasts, accumulation of AICAR and its di‑ and triphosphate derivatives (ZMP, ZDP, ZTP) can be measured via chromatographic or mass spectrometric methods.[3][13]

Suggested LOINC terms include codes for urinary purine metabolite measurements and aminoimidazolecarboxamide riboside quantification, though specific codes may not yet exist for this rare disorder. Clinical laboratories offering purine metabolite analysis typically provide custom assays. Standard blood chemistry may reveal elevated liver transaminases (hypertransaminasemia) in some patients, consistent with hepatic cytolysis.[12][14][17] Imaging studies such as MRI of the brain can show structural abnormalities (e.g., corpus callosum agenesis or other malformations) in related disorders, but specific brain imaging findings in AICA‑ribosiduria have not been comprehensively reported.[18]

Electrophysiologic testing with EEG can confirm epilepsy and characterize seizure types, while visual electrophysiology (electroretinography) may demonstrate retinal dysfunction. However, these are supportive rather than diagnostic tests. Histopathology of retina or brain tissue has not been reported, given ethical constraints.

### 10.2 Genetic testing approaches

Genetic testing plays a central role in confirming AICA‑ribosiduria and distinguishing it from other causes of severe developmental delay and purine metabolism disorders. Orphanet notes that diagnosis is more realistically suspected after exome, genome, or gene panel sequencing reveals two pathogenic loss‑of‑function variants in ATIC in a biallelic pattern.[1][15] Whole‑exome sequencing (WES) has been instrumental in identifying ATIC variants in recent cases, including the Indian child and the milder siblings.[6][17] In the Indian case, WES identified a novel splice site variant and the known K426R missense variant, and segregation analysis confirmed inheritance from heterozygous carrier parents.[6] Dewulf et al. similarly used WES to detect their patients’ variants.[17]

Single‑gene testing of ATIC may be performed when purine metabolite profiles strongly suggest AICA‑ribosiduria. Gene panels for inborn errors of metabolism or intellectual disability may include ATIC, though given the rarity of the disease, inclusion is not universal. Chromosomal microarray and karyotyping are useful to exclude other genetic syndromes but are not diagnostic for ATIC point mutations.[2][6][14][17]

Whole‑genome sequencing (WGS) could theoretically detect ATIC variants, including structural variants or deep intronic changes, but specific WGS applications have not yet been reported in this disease. Mitochondrial DNA testing, FISH, and repeat expansion testing are not relevant, as the defect is nuclear, non‑repeat, and non‑structural. ClinVar lists ATIC variants associated with AICA‑ribosiduria, supporting variant interpretation.

Prenatal diagnosis is possible when pathogenic variants have been identified in a family member. Orphanet notes that prenatal diagnostic testing, via chorionic villus sampling or amniocentesis, can detect ATIC mutations in at‑risk pregnancies, allowing informed reproductive decisions.[1][15] Preimplantation genetic diagnosis (PGD) and carrier screening might be considered in high‑risk families, although data are limited.

### 10.3 Omics‑based diagnostics and biomarkers

Beyond targeted genetic and metabolite testing, omics‑based diagnostics have not been developed specifically for AICA‑ribosiduria. Transcriptomic or proteomic signatures unique to ATIC deficiency are not known. However, the metabolite profile—high urinary AICA‑riboside, SAICA‑riboside, and succinyladenosine—constitutes a robust biomarker set for the disease.[3][13][14][17] In the context of inborn errors of metabolism, these metabolites can be included in expanded newborn screening research panels, though routine screening is unlikely due to low prevalence.

The treatment study demonstrates that monitoring urinary AICA‑riboside and succinyladenosine levels can serve as biomarkers of therapeutic response to dietary purine supplementation.[7] For structured representation, these biomarkers may be mapped to NCIT terms such as “metabolite biomarker” (NCIT:C164023) and “succinyladenosine level measurement.”

### 10.4 Clinical criteria and differential diagnosis

There are no standardized clinical diagnostic criteria for AICA‑ribosiduria akin to DSM or society guidelines, primarily because of its rarity. Nonetheless, Ramond et al. propose a clinical definition based on shared phenotypic features across four patients: a syndromic association of severe‑to‑profound global neurodevelopmental impairment, severe visual impairment due to chorioretinal atrophy, ante‑postnatal growth impairment, and severe scoliosis, with frequent coarse facies and upturned nose, early‑onset epilepsy, and occasional aortic coarctation, hepatic cytolysis, genital anomalies, and nephrocalcinosis.[14] This constellation, together with the biochemical signature of AICA‑riboside accumulation, can serve as de facto diagnostic criteria.

Differential diagnosis includes other inborn errors of purine metabolism such as adenylosuccinate lyase deficiency, which also features succinyladenosine and SAICA‑riboside accumulation but lacks massive AICA‑riboside excretion and has a somewhat different clinical profile.[13] Disorders of purine salvage (e.g., hypoxanthine‑guanine phosphoribosyltransferase deficiency causing Lesch–Nyhan syndrome) present with hyperuricemia, self‑injurious behavior, and dystonia, distinct from AICA‑ribosiduria.[13] Mitochondrial disorders, chromosomal syndromes, and other metabolic diseases can cause severe developmental delay and visual impairment, but specific metabolite patterns and genetic testing distinguish them.

### 10.5 Screening and early detection

Population‑based screening for AICA‑ribosiduria is not currently implemented, given its ultra‑rare nature and the technical complexity of metabolite analysis. Newborn screening programs focus on more prevalent metabolic disorders. However, targeted screening in high‑risk families, via carrier testing and prenatal diagnosis, is feasible.[1][15] Cascade screening of relatives to identify ATIC carriers and inform reproductive decisions may be recommended by genetic counselors.

In research settings, extended metabolomic screening of infants with unexplained severe developmental delay and visual impairment could potentially detect AICA‑riboside and related metabolites, prompting focused genetic testing. Whether such approaches are cost‑effective remains uncertain.

## 11. Outcome / Prognosis

### 11.1 Survival, life expectancy, and mortality

Data on survival and life expectancy in AICA‑ribosiduria are limited to the handful of reported cases. Orphanet notes that life expectancy is unknown, with the oldest individual being 20 years of age as of the 2020 update.[1][15] Ramond et al.’s long‑term follow‑up of the index patient indicates that she survived into adulthood despite profound disability and severe scoliosis, suggesting that, at least in some cases, life expectancy may extend into the third decade.[12] There are no reports of early mortality directly attributable to the metabolic defect, though complications such as severe epilepsy, respiratory compromise from scoliosis, or cardiac anomalies could increase mortality risk.

Mortality rates cannot be estimated given the tiny sample. Disease‑specific mortality—deaths directly attributable to AICA‑ribosiduria—has not been formally documented, and it is possible that with intensive supportive care, patients may live many years. However, given the severity of impairment, life expectancy may be reduced compared to the general population.

### 11.2 Morbidity, disability outcomes, and quality of life

Morbidity in AICA‑ribosiduria is high, with substantial disability across physical, cognitive, sensory, and social domains. Profound intellectual disability and blindness severely limit autonomy, learning, and interaction. Severe scoliosis and hypotonia impair mobility and may cause pain. Epilepsy adds further morbidity and may be refractory to treatment.[3][12][14][17] Chronic hepatic cytolysis and nephrocalcinosis, while often subclinical, represent ongoing organ stress.[12][14][17]

Long‑term functional outcomes, as illustrated by the index patient, involve dependence on caregivers for all activities of daily living, limited communication, and restricted participation in social and educational activities.[12] Dewulf et al.’s siblings have somewhat better functional capacity, able to walk and communicate to some extent, but still require special education and long‑term support.[17] Thus, even milder cases carry significant disability.

Quality of life measures have not been formally applied, but given the clinical descriptions, EQ‑5D or SF‑36 scores would likely be markedly low in most domains for severely affected patients, and moderate to low in milder cases. Parents and caregivers bear a substantial psychosocial burden.

### 11.3 Disease course: complications and recovery potential

Complications of AICA‑ribosiduria include progression of scoliosis, potentially requiring orthopedic intervention; seizures and their sequelae; visual complications including strabismus or photophobia; and secondary issues such as contractures, pressure sores, and respiratory infections in immobile patients.[12][14][17] Cardiovascular complications from aortic coarctation may necessitate surgical repair and carry their own risks.[12][14] Hepatic and renal anomalies may predispose to later organ dysfunction, though this has not yet been documented.

Recovery potential from core neurologic and visual deficits appears limited, as these arise from developmental structural changes. Rehabilitation can maximize function within constraints but cannot reverse blindness or profound intellectual disability. In milder cases, developmental progress is possible, and interventions such as speech therapy and special education may improve outcomes.[5][17] Whether metabolic interventions like purine‑enriched diet can enhance recovery remains unknown.

### 11.4 Prognostic factors and biomarkers

Prognostic factors may include the specific ATIC variants and residual enzymatic activity, though robust genotype–phenotype correlations are not yet established.[14][17] Early onset and severity of growth retardation, scoliosis, and visual impairment likely predict more severe long‑term disability. Presence of cardiac anomalies (aortic coarctation) may influence survival.

Biomarkers such as levels of AICA‑riboside, SAICA‑riboside, and succinyladenosine provide insight into metabolic burden but their correlation with clinical severity has not been fully explored.[14][17] The degree of reduction in these metabolites under treatment could serve as a prognostic marker for therapeutic response, but data are currently limited to one patient.[7]

## 12. Treatment

### 12.1 Pharmacotherapy and symptomatic management

Until recently, there was no disease‑specific pharmacotherapy for AICA‑ribosiduria. Orphanet states that “there is no preventive, curative, or specific treatment to date,” and recommends management according to standard protocols for epilepsy, visual impairment, scoliosis, and developmental delay.[1][15] Antiepileptic drugs are used to control seizures, though early‑onset epilepsy may be pharmacoresistant.[12][14] Choices of antiepileptic agents (e.g., valproate, levetiracetam, topiramate) follow general pediatric epilepsy guidelines, and there are no data on specific pharmacogenomic interactions with ATIC deficiency. Suggested NCIT terms include “antiepileptic agent” (NCIT:C1593) and “seizure prophylaxis” (NCIT:C15689).

For visual impairment, standard ophthalmologic management, including correction of refractive errors (e.g., hypermetropia) and provision of low‑vision aids, is recommended. Orphanet notes that chorioretinal atrophy itself has no specific treatment.[1][15] NCIT terms such as “vision rehabilitation” (NCIT:C116410) and “low vision aids” can be applied.

Pain management for scoliosis and musculoskeletal deformities may involve analgesics (NCIT:C596), muscle relaxants, and supportive devices (bracing). No specific pharmacotherapy targets purine metabolism in AICA‑ribosiduria, though antifolate drugs theoretically interact with purine synthesis and might exacerbate the defect; their use should be cautious.

### 12.2 Advanced therapeutics: gene, cell, and RNA‑based therapies

As of the latest reports, no gene therapies, cell therapies, or RNA‑based therapies have been developed or tested specifically for AICA‑ribosiduria. In principle, gene replacement or editing of ATIC could restore de novo purine synthesis, but the practical challenges of delivering such therapy to the CNS, retina, and skeletal system are substantial. CRISPR‑based correction in embryonic or fetal cells would be necessary to prevent developmental defects, raising ethical and technical issues.

Cell therapies, such as stem cell transplantation, have not been applied. RNA‑based therapies (antisense oligonucleotides, siRNA targeting mutant ATIC transcripts) would face similar delivery and timing hurdles. At present, advanced therapeutics remain theoretical possibilities rather than active interventions.

### 12.3 Targeted metabolic therapy: purine‑enriched diet

The most promising disease‑targeted treatment reported to date is suppression of de novo purine biosynthesis in favor of salvage via a purine‑enriched diet. In the 2024 study, a teenage patient with ATIC deficiency (compound heterozygous for K426R and Q214H) was given a diet enriched in purines. Following this intervention, excessive secretion of AICA‑riboside and succinyladenosine was significantly reduced.[7] The authors concluded that by suppressing de novo purine biosynthesis in favor of purine salvage, exogenous purine substitution represents a promising treatment approach for AICA‑ribosiduria.[7]

This strategy directly targets the metabolic mechanism: increased dietary purines provide substrates for salvage pathways (via HPRT and APRT), reducing the need for de novo synthesis and decreasing flux through the ATIC‑dependent steps. Less AICAR is produced, and less AICA‑riboside accumulates. The intervention can be mapped to NCIT terms such as “dietary intervention” (NCIT:C15666) and “metabolic therapy” (NCIT:C15677).

Clinical outcomes beyond metabolite reduction have not yet been described in detail; it is unclear whether neurologic function, vision, or growth improved. The teenage age at intervention may limit potential reversal of established structural damage. Nevertheless, this study demonstrates proof‑of‑concept that metabolic flux can be manipulated, and paves the way for earlier, more comprehensive trials.

### 12.4 Surgical and interventional procedures

Orthopedic surgery may be required for severe scoliosis, particularly when spinal curvature threatens respiratory function or causes significant pain. Bracing and physical therapy may precede surgery. Cardiac surgery may be necessary in patients with aortic coarctation. These procedures are guided by general orthopedic and cardiology practice rather than disease‑specific protocols.[12][14] NCIT terms such as “spinal fusion surgery” (NCIT:C50736) and “aortic coarctation repair” can be assigned.

Ophthalmologic surgeries are not indicated for chorioretinal atrophy, as the underlying photoreceptor loss is not surgically reversible.

### 12.5 Supportive and rehabilitative care

Supportive care is paramount. Orphanet emphasizes multidisciplinary management, including referral to an experienced neuropediatrician, ophthalmologist, orthopedic specialist, and early intervention programs.[1][15] Neurodevelopment should be supported through speech therapy, occupational therapy, and physical therapy, aiming to maximize functional abilities and prevent secondary complications such as contractures.[1][12][15][17] NCIT terms such as “physical therapy” (NCIT:C49288), “occupational therapy” (NCIT:C21240), and “speech therapy” (NCIT:C49287) capture these interventions.

Nutritional support is important given failure to thrive, and may involve high‑calorie diet, feeding assistance, or gastrostomy tube placement. Psychosocial support for families, including counseling and respite care, is critical given the high caregiving burden.

### 12.6 Experimental treatments and clinical trials

As of the current literature, no registered clinical trials specifically target AICA‑ribosiduria. The purine‑enriched diet intervention was performed in a single patient and reported as a case study rather than a formal trial.[7] Experimental approaches could include trials of exogenous purine supplementation in infants diagnosed early, with careful monitoring of metabolites and clinical outcomes, but such studies have not yet begun.

Other experimental options might explore modulation of AMPK, folate supplementation, or coenzyme support, though their rationale is less direct and they have not been tested.

### 12.7 Treatment outcomes, side effects, and personalized medicine

Treatment outcomes are largely descriptive. Antiepileptic drugs may reduce seizure frequency but often do not fully control epilepsy. Orthopedic interventions can stabilize scoliosis but carry typical surgical risks. The purine‑enriched diet reduced metabolite excretion without reported major side effects, but long‑term consequences of high purine intake (e.g., hyperuricemia, gout) must be considered.[7] Personalized medicine approaches, such as tailoring metabolic therapy to specific ATIC variants or residual enzyme activity, are conceptually attractive but have not been implemented.

Pharmacogenomics data regarding ATIC and drug metabolism are sparse. ATIC is a target of antifolate chemotherapeutics in cancer, and variants may influence antifolate sensitivity, but these contexts are far from congenital AICA‑ribosiduria.[8][16] Nonetheless, caution may be warranted in using antifolate drugs in patients with ATIC deficiency.

## 13. Prevention

### 13.1 Primary prevention

Primary prevention of AICA‑ribosiduria, in the sense of preventing disease occurrence, relies on genetic counseling and reproductive decision‑making in families known to carry pathogenic ATIC variants. Orphanet recommends genetic counseling for affected families and notes that for parents of an affected child, the risk of recurrence is 25% for each future pregnancy.[1][15] Carrier testing of at‑risk relatives can identify heterozygous carriers and inform choices such as avoiding consanguineous unions, using donor gametes, or undertaking PGD.

Population‑level primary prevention measures (e.g., general screening programs) are unlikely given the ultra‑rare nature of the disorder. Public health interventions such as vaccination, sanitation, or environmental controls do not apply.

### 13.2 Secondary prevention: early detection and intervention

Secondary prevention involves early detection of disease and prompt initiation of supportive and possibly metabolic therapies to minimize complications. Prenatal diagnosis via ATIC mutation testing in chorionic villus or amniotic samples can identify affected fetuses, allowing parents to consider continuation or termination of pregnancy.[1][15] Newborn screening is not currently performed, but early postnatal diagnosis based on clinical suspicion and metabolite testing can enable early intervention programs.

Early physical and occupational therapy can reduce contractures and improve gross motor function. Early visual rehabilitation and tactile stimulation can maximize sensory experiences for blind infants. Early introduction of purine‑enriched diet (if confirmed effective and safe) could reduce metabolite toxicity during critical brain and retinal developmental periods, representing secondary prevention of severe tissue damage.

### 13.3 Tertiary prevention: preventing complications

Tertiary prevention aims to prevent complications and optimize function in individuals with established disease. Aggressive management of scoliosis, including bracing and timely surgery, can prevent severe spinal deformity and respiratory compromise.[1][12][15] Effective seizure control reduces risk of injury and developmental regression. Monitoring for hepatic and renal anomalies enables early intervention to avoid organ damage.

Behavioral interventions to support communication, social engagement, and emotional regulation can improve quality of life. Counseling for families helps prevent caregiver burnout and psychosocial complications. NCIT terms such as “tertiary prevention” and “supportive care” (NCIT:C49154) capture these interventions.

### 13.4 Genetic counseling and risk stratification

Genetic counseling is a cornerstone of prevention. Counselors can explain autosomal recessive inheritance, recurrence risk, carrier implications, and available testing options. Risk stratification within families identifies individuals who might benefit from carrier screening, PGD, or prenatal testing. ACMG guidelines for counseling in autosomal recessive conditions apply.[1][2][15]

### 13.5 Prophylaxis and preventive medications

No prophylactic medications specific to AICA‑ribosiduria exist. General prophylaxis against epilepsy (antiepileptic drugs) and infections (vaccinations) follow standard pediatric practice. If purine‑enriched diet is validated, it may serve as a preventive metabolic regimen, but at present it is experimental.[7]

## 14. Other Species / Natural Disease

### 14.1 Species affected and orthologous genes

Naturally occurring AICA‑ribosiduria has not been reported in other species. There are no entries in OMIA (Online Mendelian Inheritance in Animals) describing ATIC deficiency as a spontaneous veterinary disease. However, ATIC orthologs exist in many organisms, including mice, rats, zebrafish, Drosophila, C. elegans, yeast, and bacteria, reflecting the evolutionary conservation of de novo purine biosynthesis.[11][13][16] NCBI Gene lists orthologous ATIC genes across taxa.

In yeast and bacterial systems, ATIC homologs (often annotated as purH) have been studied extensively in the context of purine biosynthesis and antifolate resistance, providing insight into enzyme structure and function.[8][11][13] These experimental models, while not natural disease systems, inform understanding of ATIC biology.

### 14.2 Natural disease and veterinary relevance

No natural veterinary disease equivalent to human AICA‑ribosiduria has been described. Purine metabolism disorders in animals are rare, and most reported conditions involve uric acid excretion abnormalities (e.g., Dalmatian hyperuricosuria) rather than ATIC deficiency. Thus, the veterinary relevance of AICA‑ribosiduria is minimal, although knowledge of purine metabolism is broadly applicable.

### 14.3 Comparative pathology and evolution of mechanism

Comparative pathology suggests that de novo purine biosynthesis is essential across species, and that disruption of key enzymes such as ATIC is likely lethal or severely deleterious. In model organisms, ATIC (purH) knockout can impair growth and viability, underscoring its fundamental role.[11][13][16] The evolutionary conservation of ATIC structure and function supports the plausibility of similar disease mechanisms across species, even if natural disease has not been observed.

From an evolutionary perspective, the rarity of ATIC deficiency in humans may reflect strong negative selection against biallelic loss‑of‑function, given the severe developmental consequences. Heterozygous carriers, by contrast, appear unaffected, allowing low‑frequency persistence of deleterious alleles.

### 14.4 Zoonotic potential and cross‑species susceptibility

AICA‑ribosiduria is not infectious and has no zoonotic potential. Cross‑species susceptibility to purine metabolism defects arises only in experimental contexts where ATIC genes are manipulated.

## 15. Model Organisms

### 15.1 Types of models and systems

While no dedicated animal models have been developed specifically to replicate human AICA‑ribosiduria, experimental systems with ATIC manipulation exist. In yeast, purH mutants lacking AICAR formyltransferase and/or IMP cyclohydrolase activity have been studied to dissect purine biosynthesis.[11][13] In bacteria, ATIC homologs are important for growth, and knockout mutants require salvage pathways or exogenous purines.[8][11] In mammalian cell lines, ATIC knockdown or inhibition has been used to study antifolate drug responses.

These models are in vitro or cellular rather than whole‑organism disease models. They illustrate biochemical and metabolic consequences of ATIC deficiency but do not recapitulate complex developmental phenotypes such as neurodevelopmental impairment and chorioretinal atrophy.

### 15.2 Genetic models: knockout and knock‑in

Full knockout of ATIC in a mammalian organism (e.g., mouse) would likely be embryonically lethal or cause severe developmental defects, though specific data are not widely reported. Conditional knockout models, where ATIC is deleted in specific tissues (brain, retina), could theoretically be used to study tissue‑specific mechanisms, but such models have not been described in the AICA‑ribosiduria literature.

Knock‑in models carrying human disease variants (e.g., K426R) would allow exploration of partial loss‑of‑function and phenotype. The absence of such models reflects the ultra‑rare nature of the disease and limited research focus.

### 15.3 Phenotype recapitulation and limitations

Existing experimental models recapitulate purine metabolic defects but not the full human phenotype. Yeast and bacterial purH mutants show impaired growth and nucleotide imbalance but lack complex neural and retinal structures. Mammalian cell lines with ATIC knockdown exhibit changes in nucleotide pools and AMPK activation but cannot exhibit developmental delay or scoliosis.

The main limitations are therefore organismal complexity and tissue specificity. To fully model AICA‑ribosiduria, a vertebrate organism with developed CNS and retina is required, and ATIC deficiency must be introduced in a way that allows survival. Zebrafish or mouse models could be promising, but they have not yet been developed.

### 15.4 Applications for research

Despite limitations, existing ATIC‑focused models provide valuable tools to study enzyme structure, catalytic mechanisms, and interactions with antifolate drugs. They can be used to screen potential small‑molecule modulators of ATIC or salvage pathways, informing metabolic therapy. In vitro models can also be used to test the effects of increased exogenous purines on metabolite accumulation, paralleling the human treatment study.[7]

Future model development could focus on conditional ATIC knockout in neural and retinal tissues to explore developmental mechanisms, or on induced pluripotent stem cell (iPSC)–derived neurons and retinal organoids from ATIC‑deficient patients.

## Conclusion

AICA‑ribosiduria (ATIC deficiency) is an ultra‑rare, autosomal recessive inborn error of de novo purine biosynthesis that exemplifies how disruption of a seemingly mundane metabolic pathway can produce a devastating multisystem developmental disorder. At the molecular level, biallelic loss‑of‑function ATIC mutations impair AICAR formyltransferase and IMP cyclohydrolase activities, leading to accumulation of AICAR and its nucleoside AICA‑riboside, as well as related intermediates such as SAICA‑riboside and succinyladenosine.[3][13][14][17] These metabolites, together with altered nucleotide pools and likely chronic activation of AMPK, create a state of metabolic stress and cytotoxicity in developing tissues, particularly the brain and retina. The clinical result is a characteristic syndrome of severe to profound global neurodevelopmental impairment, congenital or early‑onset severe visual impairment due to chorioretinal atrophy, ante‑ and postnatal growth retardation, and progressive severe scoliosis, accompanied by dysmorphic facial features, early‑onset epilepsy, and occasional cardiovascular, hepatic, renal, and genital anomalies.[1][2][3][12][14][15][17][18]

From a genetic standpoint, AICA‑ribosiduria is a monogenic disorder with complete penetrance for biochemical defect and high penetrance for clinical manifestations. Variant classes include missense, nonsense, frameshift, and splice site changes, with K426R being the best characterized missense allele demonstrating complete loss of AICAR transformylase activity.[3][13] While some variability in clinical severity exists, as illustrated by the milder siblings reported by Dewulf et al., robust genotype–phenotype correlations are not yet established.[5][14][17] Environmental risk factors are not implicated in disease onset, but metabolic gene–environment interactions, particularly exogenous purine supplementation, can modulate metabolite accumulation and represent a promising therapeutic avenue.[7]

Diagnostic pathways combine clinical recognition of the syndromic phenotype, targeted metabolite analysis (urinary AICA‑riboside, SAICA‑riboside, succinyladenosine), and genetic testing (WES, ATIC sequencing).[1][3][6][12][14][15][17] Prenatal diagnosis is feasible when familial ATIC variants are known, providing options for at‑risk couples.[1][15] Prognosis is guarded: patients experience severe lifelong disability, and while survival into adulthood is possible, life expectancy beyond the second decade is uncertain.[1][12][15] There is currently no curative or gene‑directed therapy. Management focuses on multidisciplinary supportive care—antiepileptic treatment, ophthalmologic and orthopedic interventions, early rehabilitation—while experimental metabolic therapy with purine‑enriched diet has shown encouraging biochemical results in a single case.[1][7][12][14][15]

Mechanistically, AICA‑ribosiduria highlights the importance of purine metabolism not only for cellular proliferation but also for tissue‑specific development and function. The concentration of pathology in CNS, retina, and skeletal system reflects the high metabolic and proliferative demands of these tissues during development. Mapping disease features to ontologies such as MONDO, HPO, GO, CL, UBERON, CHEBI, and NCIT facilitates integration into knowledge bases and supports computational reasoning about disease mechanisms and phenotypes. At present, research gaps include the absence of animal models that faithfully recapitulate the human phenotype, lack of large‑scale omics data, and limited understanding of long‑term outcomes and therapeutic responses.

Future directions for AICA‑ribosiduria research and management should prioritize: systematic collection of clinical and biochemical data from all known and newly diagnosed patients; functional characterization of additional ATIC variants to refine genotype–phenotype relationships; development of vertebrate models or patient‑derived organoids to study tissue‑specific mechanisms; and controlled trials of metabolic interventions such as purine‑enriched diet introduced as early as possible in life. For families affected by this ultra‑rare disorder, improved genetic counseling, prenatal diagnosis, and supportive care protocols can already make a substantial difference. At a broader level, AICA‑ribosiduria serves as a paradigmatic example of how integrating clinical, biochemical, and molecular data, even from very small case series, can delineate a distinctive disease entity, provide insights into fundamental biology, and open avenues for rational therapy in the realm of inborn errors of metabolism.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 95 |
| Resolved | 86 |
| Unresolved (possible confabulation) | 4 |
| Obsolete | 1 |
| Unverifiable | 4 |
| Terms whose name was checked | 29 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 12 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCIT:C129830` (1 mention) - the report calls it "Inborn Error of Purine Metabolism; broader class"; NCIT calls it **Monoallelic Mutation**
- `UBERON:0000967` (2 mentions) - the report calls it "choroid of eye"; UBERON calls it **obsolete adult thoracic sensillum**
- `NCIT:C164023` (1 mention) - the report calls it "metabolite biomarker"; NCIT calls it **Initial Genomic Sequencing Date**
- `NCIT:C1593` (1 mention) - the report calls it "antiepileptic agent"; NCIT calls it **Recombinant Chemokine**
- `NCIT:C15689` (1 mention) - the report calls it "seizure prophylaxis"; NCIT calls it **Drug Resistance Inhibition Treatment**
- `NCIT:C116410` (1 mention) - the report calls it "vision rehabilitation"; NCIT calls it **Phospholipid-Transporting ATPase ABCA1**
- `NCIT:C15677` (1 mention) - the report calls it "metabolic therapy"; NCIT calls it **Axillary Lymph Node Dissection**
- `NCIT:C50736` (1 mention) - the report calls it "spinal fusion surgery"; NCIT calls it **Rupture Of Hyaloid Face**
- `NCIT:C49288` (1 mention) - the report calls it "physical therapy"; NCIT calls it **AS04 Adjuvant**
- `NCIT:C21240` (1 mention) - the report calls it "occupational therapy"; NCIT calls it **Translation Process Gene**
- `NCIT:C49287` (1 mention) - the report calls it "speech therapy"; NCIT calls it **Effective**
- `NCIT:C49154` (1 mention) - the report calls it "supportive care"; NCIT calls it **Statement**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0007891` (3 mentions) - HP does not contain this term
- `HP:0008021` (2 mentions) - HP does not contain this term
- `HP:0003242` (1 mention) - HP does not contain this term
- `FMA:50801` (1 mention) - FMA does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `UBERON:0000967` (obsolete adult thoracic sensillum) (2 mentions)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006207` (1 mention) - the report calls it "de novo purine nucleobase biosynthetic process"; GO calls it **'de novo' pyrimidine nucleobase biosynthetic process**
- `GO:0000034` (1 mention) - the report calls it "AICAR formyltransferase activity"; GO calls it **adenine deaminase activity**, and lists "adenine aminase activity" among its other names
- `GO:0003921` (1 mention) - the report calls it "IMP cyclohydrolase activity"; GO calls it **GMP synthase activity**
- `NCIT:C15666` (2 mentions) - the report calls it "dietary intervention"; NCIT calls it **Radiofrequency Ablation**, and lists "Radiofrequency Interstitial Ablation" among its other names
- `GO:0032147` (1 mention) - the report calls it "AMP‑activated protein kinase signaling"; GO calls it **activation of protein kinase activity**
- `GO:0071322` (1 mention) - the report calls it "cellular response to energy stress"; GO calls it **cellular response to carbohydrate stimulus**
- `GO:0042127` (1 mention) - the report calls it "regulation of cell proliferation"; GO calls it **regulation of cell population proliferation**, and lists "regulation of cell proliferation" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`.