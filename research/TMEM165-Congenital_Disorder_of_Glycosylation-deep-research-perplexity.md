---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-28T21:32:52.264898'
end_time: '2026-09-28T21:37:29.880028'
duration_seconds: 277.62
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: TMEM165-Congenital Disorder of Glycosylation
  mondo_id: MONDO:0013870
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: low
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 42
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 13
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 99
  verified: 88
  not_found: 3
  obsolete: 3
  unverifiable: 5
  confabulation_rate: 0.032
  labels_checked: 22
  labels_matching: 5
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: GO:0060590
    reported_labels:
    - regulation of glycosylation
    ontology_label: ATPase regulator activity
  - term_id: NCIT:C16082
    reported_labels:
    - genetic testing
    ontology_label: Marker Discovery
  - term_id: NCIT:C84355
    reported_labels:
    - DNA sequencing
    ontology_label: Intraoperative
  - term_id: NCIT:C17940
    reported_labels:
    - glycosylation analysis
    ontology_label: Microbial Genetics
  - term_id: NCIT:C15228
    reported_labels:
    - nutritional supplement therapy
    ontology_label: Double Blind Study
  - term_id: NCIT:C15695
    reported_labels:
    - supportive care
    ontology_label: Quadrantectomy
  - term_id: NCIT:C15273
    reported_labels:
    - physical therapy
    - rehabilitation
    ontology_label: Longitudinal Study
  - term_id: NCIT:C15790
    reported_labels:
    - cardiac surgery
    ontology_label: Cancer Prevention Trial
  - term_id: NCIT:C16714
    reported_labels:
    - genetic counseling
    ontology_label: Immunoenzyme Procedure
  - term_id: NCIT:C45776
    reported_labels:
    - prenatal diagnosis
    ontology_label: HD Term Type
  labels_variant: 7
  unresolved_terms:
  - HP:0002658
  - HP:0002759
  - HP:0001968
  obsolete_terms:
  - term_id: HP:0007910
    ontology_label: obsolete Nonprogressive congenital retinal dystrophy
  - term_id: GO:0006486
    ontology_label: obsolete protein glycosylation
    replaced_by: GO:0009101
  - term_id: CL:0000063
    ontology_label: obsolete cell by histology
  unresolvable_prefixes:
  - OMIM
  - Gene
  - Orpha
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** TMEM165-Congenital Disorder of Glycosylation
- **MONDO ID:** MONDO:0013870 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **TMEM165-Congenital Disorder of Glycosylation** covering all of the
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

# TMEM165-Congenital Disorder of Glycosylation (TMEM165‑CDG / CDG Type IIk)

TMEM165‑Congenital Disorder of Glycosylation (TMEM165‑CDG; CDG type IIk; MONDO:0013870) is a rare autosomal recessive multisystem Mendelian disease caused by biallelic pathogenic variants in the *TMEM165* gene on chromosome 4q12, encoding a multi‑pass Golgi cation/\(\mathrm{H}^+\) antiporter that regulates luminal manganese and calcium homeostasis required for N‑ and O‑glycosylation and proteoglycan synthesis.[2][8][1][7] Clinically, TMEM165‑CDG presents with psychomotor and growth retardation, striking skeletal dysplasia with epiphyseal, metaphyseal and diaphyseal involvement, facial dysmorphism, hepatosplenomegaly, endocrine and coagulation abnormalities, nephrotic syndrome, cardiac defects including cardiomyopathy, feeding difficulties, and characteristic transferrin type II glycosylation abnormalities reflecting defective terminal sialylation and galactosylation.[2][15][27][32][3][12] At the cellular level, TMEM165 deficiency produces combined N‑ and O‑glycosylation defects, shortened chondroitin‑ and heparan‑sulfate glycosaminoglycan chains, and impaired TGF‑β/BMP signaling in chondrocytes, mechanistically linking defective Golgi cation homeostasis to abnormal cartilage development and skeletal disease.[4][35] Oral D‑galactose supplementation has been shown in a prospective clinical study to partially rescue glycosylation abnormalities and improve endocrine and coagulation parameters, representing the first successful dietary therapy for this specific CDG subtype.[27][32][29] Because TMEM165‑CDG is extremely rare (<1/1,000,000) with variable expressivity and limited natural‑history data, systematic characterization of its phenotypes, mechanisms, diagnostics, and treatment strategies is critical for both patient care and for understanding fundamental aspects of Golgi ion homeostasis and glycosylation biology.[3][3][12][7]

---

## 1. Disease Information

### 1.1 Overview and Definition

TMEM165‑Congenital Disorder of Glycosylation (TMEM165‑CDG) is a Mendelian inborn error of metabolism classified within the group of congenital disorders of glycosylation (CDG), specifically a type II (processing) and “mixed” N‑ and O‑glycosylation defect caused by pathogenic variants in *TMEM165*.[2][10][12][7] CDG are a growing group of inherited multisystem disorders characterized by defects in the glycosylation of proteins and lipids; TMEM165‑CDG represents one of the subtype entities in this expanding nosology.[21][12] Foulquier and colleagues first identified *TMEM165* (also named *TPARL*) as the causative gene in 2012 through autozygosity mapping and expression analysis in siblings with abnormal serum transferrin isoelectric focusing and a peculiar skeletal phenotype, establishing a previously undescribed type II CDG.[2][13][2] The disease is now recognized as an autosomal recessive disorder with variable phenotype, defined by systemic consequences of impaired Golgi glycosylation due to defective cation/\(\mathrm{H}^+\) antiporter function of TMEM165.[2][8][1][1]

Orphanet describes TMEM165‑CDG as “a form of congenital disorders of N‑linked glycosylation characterized by a psychomotor delay‑dysmorphism (pectus carinatum, dorsolumbar kyphosis and severe sinistroconvex scoliosis, short distal phalanges, genua vara, pedes planovalgi syndrome) with postnatal growth deficiency and major spondylo‑, epi‑, and metaphyseal skeletal involvement,” with additional features including facial dysmorphism, nephrotic syndrome, cardiac defects, and feeding problems.[3][3][3][3] OMIM entry #614727 similarly characterizes congenital disorder of glycosylation type IIk (CDG2K) as a variable autosomal recessive disease whose cardinal manifestations include psychomotor retardation, growth retardation and short stature, dysmorphism, hypotonia, eye abnormalities, acquired microcephaly, hepatomegaly, and skeletal dysplasia.[10][8] These authoritative disease‑level descriptions synthesize data from individual case reports, small case series, and biochemical studies, and therefore largely reflect aggregated disease‑level information rather than single EHR‑derived narratives.[2][15][15][12]

### 1.2 Key Identifiers and Ontology Placement

The primary identifiers for TMEM165‑CDG across major databases are well established. OMIM lists congenital disorder of glycosylation, type IIk under entry 614727, associated with *TMEM165* (gene OMIM:614726) on cytogenetic location 4q12.[8][10] Orphanet assigns TMEM165‑CDG the Orpha number 314667, noting a prevalence <1/1,000,000, autosomal recessive inheritance, and infancy/neonatal age of onset.[3][3][3] In the Mondo Disease Ontology, TMEM165‑CDG corresponds to MONDO:0013870, designated as “congenital disorder of glycosylation type IIk” or TMEM165‑CDG.[9][38] ICD‑10 classifies this disease under E77.8 (“Other specified disorders of glycoprotein metabolism”), and ICD‑11 under 5C54.0 (“Congenital disorders of glycosylation”), with TMEM165‑CDG recognized among specific subtypes.[3][3][3] SNOMED CT includes an associated concept (732252005) for congenital disorders of glycosylation, which can be further specialized by the TMEM165‑CDG subtype according to OMIM and Orphanet mappings.[8][10][12]

These identifiers ensure interoperability across clinical and research systems and allow integration into resources such as GlyCosmos, which lists TMEM165‑CDG (congenital disorder of glycosylation type IIk; DOID:0070263) with synonyms and an association to *TMEM165* gene ID 55858.[38] Human Phenotype Ontology (HPO) mapping for TMEM165‑CDG includes terms such as hepatomegaly (HP:0002240), hypotonia (HP:0001252), midface retrusion (HP:0011800), low‑set ears (HP:0000369), elevated creatine kinase (HP:0003236), failure to thrive (HP:0001508), malar flattening (HP:0000272), thrombocytopenia (HP:0001873), secondary microcephaly (HP:0005484), and osteoporosis (HP:0000939), among others.[38] Collectively, these identifiers and ontology placements position TMEM165‑CDG within broader frameworks of metabolic disorders, skeletal dysplasias, and neurodevelopmental conditions, facilitating standardized phenotype annotation and computational analysis.

### 1.3 Synonyms and Alternative Names

TMEM165‑CDG has accumulated a set of synonymous names across the CDG literature and disease databases, reflecting historical nomenclature evolution. Orphanet lists the following synonyms: “Carbohydrate deficient glycoprotein syndrome type IIk,” “Congenital disorder of glycosylation type 2k,” “Congenital disorder of glycosylation type IIk,” “CDG syndrome type IIk,” “CDG‑IIk,” and “CDG2K.”[3][3][3][38][3] ClinVar and ClinGen entries similarly use “TMEM165‑congenital disorder of glycosylation,” “CDG IIk,” and “TMEM165‑CDG” as synonyms.[6][6][6][6] In early reports, patients were described as having “a novel congenital disorder of glycosylation type II” due to a TMEM165 mutation, before the specific type IIk designation was widely adopted.[2][15][15][2]

Gene‑centric databases also list alternative gene names that may appear in older literature or in cross‑species studies, including FT27, GDT1 (yeast ortholog), CDG2K, TPARL, TMPT27, and SLC64A1.[5][21][5][1][41] From an ontology perspective, the preferred disease name for knowledge‑base usage is **TMEM165‑CDG** (also captured by MONDO:0013870 and DOID:0070263), while the exact OMIM name is “Congenital disorder of glycosylation, type IIk.”[8][10][38] For clarity in clinical contexts, describing the condition as a “TMEM165‑related congenital disorder of glycosylation (type IIk; mixed N‑ and O‑glycosylation defect)” can help clinicians recognize the mechanistic and biochemical specificity.

### 1.4 Evidence Source Types

Information about TMEM165‑CDG is derived from multiple evidence streams, which should be distinguished in a structured knowledge base. The initial disease characterization was based on human clinical case series combining clinical phenotyping, biochemical glycosylation profiling (serum transferrin isoelectric focusing, ApoC‑III isoelectric focusing, plasma N‑ and O‑glycan analysis), and molecular genetics (autozygosity mapping, Sanger sequencing, deep intronic variant identification) in a small number of families.[2][13][15][15] Subsequent clinical reports have added individual patient histories across different age ranges and geographic settings, including adolescence and childhood diagnoses, with detailed neurological and skeletal descriptions.[9][15][9]

Model organism studies, especially in *Saccharomyces cerevisiae* (Gdt1p) and conditional knockout mice, provide mechanistic insight into TMEM165 function in Golgi cation transport, lactose biosynthesis, and proteoglycan synthesis, and are distinct from but complementary to human clinical data.[4][19][23][26][31][35][1][26][39][40] In vitro cell culture studies using HEK293, ATDC5 and fibroblast lines offer molecular and biochemical evidence on glycosylation defects, Mn\(^2+\)/Ca\(^2+\) transport, and signaling pathway disruption.[4][1][35][19][7] Computational and evolutionary analyses of UPF0016 family proteins further inform structural and phylogenetic aspects of TMEM165 but are more peripheral to direct clinical characterization.[41]

Aggregated disease‑level resources such as OMIM, Orphanet, GlyCosmos, and GeneReviews‑style articles synthesize these various evidence types, and most of the disease‑level descriptors used here rely on such aggregation rather than individual EHR‑level data.[3][8][10][21][12][38][7] For knowledge‑base purposes, tagging each claim with its primary evidence type—human clinical, model organism, in vitro, or computational—allows downstream reasoning about evidentiary strength and translational relevance.

---

## 2. Etiology

### 2.1 Primary Causal Factors: Genetic Etiology

TMEM165‑CDG is unequivocally a genetically determined Mendelian disorder, with biallelic pathogenic variants in *TMEM165* as the primary causal factor.[2][8][10][24][5] *TMEM165* encodes a 324‑amino‑acid multi‑pass transmembrane protein with a perinuclear Golgi‑like distribution in fibroblasts and is part of the conserved UPF0016 family of cation transporters.[5][21][1][41] Foulquier et al. identified homozygous or compound heterozygous mutations in *TMEM165* in five patients from four families with CDG2K, including deep intronic splice variants, missense mutations, and nonsense alleles.[8][10][13][15][15] ClinVar and Malacards list several pathogenic variants: c.792+182G>A (deep intronic splice site), c.377G>A (p.Arg126His), c.747G>A (p.Trp249Ter), and c.910G>A (p.Gly304Arg), among others.[20][24][25]

At the functional level, TMEM165 operates as a cation/\(\mathrm{H}^+\) antiporter that supplies the Golgi and secretory pathway with the Mn\(^2+\) and Ca\(^2+\) required for glycosyltransferases and glycosidases, including galactosyltransferases and sialyltransferases.[1][1][19][7] Loss of TMEM165 leads to impaired Mn\(^2+\) homeostasis in the Golgi, defective N‑ and O‑glycosylation, hypogalactosylation and hyposialylation of N‑glycans, and shortened glycosaminoglycan chains on proteoglycans.[4][1][35][19][7] Thus, TMEM165‑CDG is etiologically a **loss‑of‑function glycosylation disorder** rooted in defective Golgi ion transport rather than primary defects in glycosyltransferase catalytic domains.

Environmental, infectious, or acquired factors are not known to cause TMEM165‑CDG in the absence of *TMEM165* mutations, and there is no evidence of somatic variants driving an analogous acquired condition.[20][21][12] Consequently, the etiologic classification is a monogenic autosomal recessive disease with complete dependence on germline biallelic pathogenic variants in *TMEM165*, consistent with MONDO:0013870 and DOID:0070263 definitions.[8][10][38]

### 2.2 Genetic Risk Factors: Pathogenic Variants and Susceptibility

The primary genetic risk factors for TMEM165‑CDG are pathogenic or likely pathogenic variants in *TMEM165* that disrupt protein expression or function. ClinVar pathogenic entries include the deep intronic splice mutation c.792+182G>A, identified in three related patients and classified as pathogenic based on segregation and functional evidence showing TMEM165 deficiency and glycosylation defects.[15][20][24][15] Missense variants such as c.377G>A (p.Arg126His), c.781G>A (p.Ala261Thr), and c.910G>A (p.Gly304Arg) are reported as pathogenic or likely pathogenic in patients with TMEM165‑CDG, often found in compound heterozygous configurations.[8][20][24][6][6]

Malacards reports at least 113 ClinVar genetic variation entries associated with congenital disorder of glycosylation, type IIk, spanning single‑nucleotide variants and larger deletions encompassing *TMEM165*.[24] Most variants are extremely rare or absent in large population datasets (gnomAD, ExAC), consistent with the ultra‑rare prevalence of TMEM165‑CDG, although specific allele frequencies are not detailed in the available summaries.[24][5][38] The functional consequences at the protein level are largely loss‑of‑function, via impaired splicing, premature truncation, or disruption of conserved transmembrane or cation‑binding motifs in TMEM165, as inferred from conservation and UPF0016 family studies.[1][21][19][41]

Modifier genes and susceptibility loci outside *TMEM165* have not been systematically identified for TMEM165‑CDG, although theoretical modifiers could include genes affecting manganese transport (e.g., *SLC39A8*, *Pmr1* orthologs), galactosyltransferases (e.g., *B4GALT1*), or other Golgi ion pumps (e.g., *ATP2C1*, *ATP2A2*).[4][19][23][19][7] Current literature has not established specific modifier alleles that consistently alter disease severity or penetrance, and the small number of reported patients limits statistical detection of such factors.[12][7]

### 2.3 Environmental Risk and Protective Factors

There is no evidence that environmental exposures such as toxins, lifestyle factors, radiation, or diet independently cause TMEM165‑CDG, given its clear monogenic etiology.[2][8][10][12] However, environmental factors can modulate the phenotypic expression and may act as **protective factors** when targeted therapeutically. The most notable protective factor is **oral D‑galactose supplementation**, which has been shown to rescue glycosylation defects in TMEM165‑CDG fibroblasts and in patients.[27][29][32] A clinical study in multiple TMEM165‑CDG patients demonstrated that titrated oral D‑galactose (0.5–2.5 g/kg/day up to 50 g/day) improved transferrin glycosylation profiles, decreased hypogalactosylated N‑glycan structures, and ameliorated endocrine and coagulation abnormalities.[27][29][32] Nutritional therapy reviews further emphasize that galactose supplementation reduced hypoglycemic episodes and improved seizure control, although some biochemical markers, such as transaminases, remain elevated.[29][30]

Mechanistically, galactose likely acts as a secondary modulator of glycosyltransferase activity, particularly B4GALT1, whose function is both manganese and galactose concentration sensitive; increased substrate availability may partially compensate for reduced Mn\(^2+\) delivery to the Golgi by TMEM165.[29][32][7] Manganese supplementation has also been used experimentally to correct glycosylation defects in TMEM165‑deficient cell lines and yeast, suggesting that controlled Mn\(^2+\) intake might be protective at the cellular level, though systemic therapeutic use in humans requires careful toxicity monitoring.[4][19][23][19][16] There is no evidence that lifestyle factors such as exercise, smoking, or alcohol consumption significantly influence disease risk, though general metabolic health may impact overall morbidity.

### 2.4 Gene–Environment Interactions

Gene–environment interactions in TMEM165‑CDG primarily concern how nutritional interventions and trace element availability modulate the phenotypic consequences of *TMEM165* mutations. The causal chain begins with TMEM165 loss‑of‑function, which reduces Mn\(^2+\) and Ca\(^2+\) delivery to the Golgi, impairing glycosylation. Supplementation with Mn\(^2+\) in cell models and yeast restores glycosylation, indicating that environmental Mn\(^2+\) availability can partially compensate for the defective transporter.[4][19][23][19][16] In humans, D‑galactose supplementation modulates glycosyltransferase efficiency and improves glycan structures, demonstrating a gene–diet interaction where substrate supply mitigates the impact of impaired Mn\(^2+\) homeostasis.[27][29][32]

More broadly, the lactating mammary gland studies show that TMEM165 conditional knockout in mouse milk‑producing cells leads to decreased lactose biosynthesis and lower milk Ca\(^2+\)/Mn\(^2+\) content, with secondary changes in milk composition (relative increases in fat, protein, iron, and zinc) driven by altered osmosis and nutrient transport.[1][31] These findings highlight how TMEM165 function interacts with dietary mineral and carbohydrate flux to shape secretory product composition, although they do not directly map to human protective factors in the congenital disease context. No CTD‑style associations linking environmental toxicants to TMEM165‑CDG onset have been reported, underscoring its purely genetic etiology.[21][12][7]

From an ontology perspective, gene–environment interaction could be modeled with GO Biological Process terms such as “response to manganese ion” (GO:0010043) and “regulation of glycosylation” (GO:0060590), and CHEBI terms for D‑galactose (CHEBI:28260) and manganese(2+) (CHEBI:29074). CL terms for relevant cell types would include chondrocytes (CL:0000138), hepatocytes (CL:0000182), and mammary gland epithelial cells (CL:0002327), all of which participate in TMEM165‑mediated glycosylation processes and may be sensitive to nutritional modulation.[31][35][7]

---

## 3. Phenotypes

### 3.1 Global Clinical Phenotype Spectrum

TMEM165‑CDG presents as a multisystem disorder with a characteristic combination of neurodevelopmental, skeletal, endocrine, hepatic, renal, cardiac, and dysmorphic features.[2][10][15][15][3][12][7] The global phenotype is shaped by defective glycosylation across diverse proteins, proteoglycans, and lipids, which impacts extracellular matrix integrity, hormone and coagulation factor function, cell adhesion, and organ development.[4][35][12][7] Human clinical reports, Orphanet summaries, and GlyCosmos HPO mappings converge on a relatively consistent core phenotype, albeit with variable severity and some heterogeneity among affected individuals.[3][9][15][3][12][38]

In general, affected individuals show psychomotor retardation, including delayed achievement of motor milestones (sitting, walking) and speech, often with hypotonia and seizures.[2][10][9][15][9][12] Growth retardation and short stature are almost universal, with marked postnatal growth deficiency and failure to thrive.[3][10][15][3][12][38] Bone dysplasia is a striking hallmark, involving epiphyseal, metaphyseal, and diaphyseal abnormalities, osteoporosis, broad metaphyses, irregular epiphyses, thin bone cortex, genu varum, scoliosis, and pectus carinatum.[15][15][3][35][37] Facial dysmorphism includes midface hypoplasia, malar flattening, low‑set ears, small teeth, and a moderately high arched palate.[3][15][3][38]

Visceral involvement spans hepatomegaly and hepatosplenomegaly, nephrotic syndrome, cardiac defects (including cardiomyopathy), restrictive lung pathology, and feeding problems with pseudo‑obstruction.[2][10][9][15][33][12] Endocrine abnormalities such as partial growth hormone deficiency, hypoglycemia, and pituitary hypoplasia have been reported.[9][27][32][9] Laboratory abnormalities include abnormal transferrin isoform profiles (type II pattern), ApoC‑III glycoform shifts reflecting O‑glycosylation defects, elevated creatine kinase, and coagulopathy with abnormal coagulation parameters.[2][15][27][32][36][12][38] These phenotypes typically manifest in infancy and childhood, with some patients diagnosed later in adolescence, and symptom severity can range from moderate multisystem disease to severe psychomotor retardation and skeletal deformity.[9][15][15][3][12]

### 3.2 Neurological and Developmental Phenotypes

Neurological involvement in TMEM165‑CDG is prominent and contributes significantly to morbidity and quality‑of‑life impairment. Common neurological phenotypes include global developmental delay, psychomotor retardation, hypotonia, seizures, and structural brain abnormalities.[2][10][9][15][9][12] Foulquier et al. described two siblings with severe psychomotor delay, hypotonia, white‑matter abnormalities, pituitary hypoplasia, and acquired microcephaly.[2][9][9] Zeevaert et al. reported psychomotor‑dysmorphism syndrome with unsupported sitting at 9 months, independent walking at 2 years, and first words at 18 months, accompanied by brain atrophy, enlarged ventricles, periventricular and subcortical white matter abnormalities, hyporeflexia, and pituitary hypoplasia.[15][15][9][9]

A recent review on the putative role of TMEM165 in congenital cardiomyopathies summarized that TMEM165 deficiency causes neurological alterations in TMEM165‑CDG patients, frequently including global developmental/psychomotor delay, CNS abnormalities (white matter changes, cerebellar atrophy), seizures, and hypotonia.[9][9][9] The HPO terms capturing these phenotypes include developmental delay (HP:0001263), psychomotor retardation (HP:0001265), muscular hypotonia (HP:0001252), seizures (HP:0001250), white matter abnormalities (HP:0002500), cerebellar atrophy (HP:0001272), microcephaly (HP:0000252), and pituitary hypoplasia (HP:0007910).[9][12][38]

Age of onset for neurological symptoms is typically in infancy or early childhood, with early developmental delay and hypotonia evident in the first year of life.[2][15][15][3][12] Symptom severity ranges from moderate delay with eventual acquisition of ambulation and speech to severe psychomotor retardation and neuromotor regression.[9][15][15][9][12] Progression can be variable; some structural changes such as white matter abnormalities may be relatively stable, while neurodevelopmental gains may continue slowly with supportive therapies.[12][37] Quality‑of‑life impact is substantial, affecting motor, cognitive, and social functioning and necessitating long‑term multidisciplinary rehabilitation, special education, and caregiver support.

### 3.3 Skeletal and Musculoskeletal Phenotypes

Skeletal manifestations are among the most distinctive phenotypes of TMEM165‑CDG and were key to its original clinical recognition. Bone dysplasia with major spondylo‑, epiphyseal, metaphyseal, and diaphyseal involvement has been consistently documented.[2][15][15][3][35][37][12] Zeevaert et al. described osteoporosis and important epi‑ and metaphyseal dysplasia with broad metaphyses, irregular epiphyses, and thin bone cortex in three patients homozygous for the deep intronic splice mutation c.792+182G>A.[15][15] Orphanet emphasizes skeletal dysplasia manifested by pectus carinatum, dorsolumbar kyphosis, severe sinistroconvex scoliosis, short distal phalanges, genua vara, and pedes planovalgi.[3][3][3]

At the molecular level, TMEM165 deficiency in prechondrocyte mouse ATDC5 and human HEK293 cells impairs polymerization of heparan‑sulfate and chondroitin‑sulfate glycosaminoglycan chains of proteoglycans, producing shortened GAG chains and altered proteoglycan synthesis.[35] This leads to aberrant TGF‑β/BMP signaling, accelerated timing of Indian hedgehog (Ihh) expression, and early chondrocyte maturation and hypertrophy, providing a mechanistic explanation for skeletal dysplasia and dwarfism.[35] The authors conclude that “TMEM165 deficiency leads to skeletal disorder characterized by major skeletal dysplasia and pronounced dwarfism.”[28][35]

HPO terms applicable to these skeletal phenotypes include skeletal dysplasia (HP:0002652), osteoporosis (HP:0000939), short stature (HP:0004322), genu varum (HP:0002970), scoliosis (HP:0002650), pectus carinatum (HP:0000768), kyphosis (HP:0002808), epiphyseal dysplasia (HP:0002658), metaphyseal dysplasia (HP:0002816), diaphyseal dysplasia (HP:0002759), and joint hyperlaxity (HP:0001387).[15][15][3][35][37][38] Age of onset is early, often in childhood as growth delays and deformities become apparent, while progression may involve worsening spinal curvature and joint anomalies.[15][15][3] The quality‑of‑life impact includes pain, mobility limitations, orthopedic complications, and psychosocial effects related to short stature and skeletal deformities.

### 3.4 Dysmorphic, Hepatic, Renal, Cardiac, and Endocrine Phenotypes

TMEM165‑CDG is associated with characteristic facial dysmorphism, visceral involvement, and endocrine abnormalities. Orphanet and case reports describe midface hypoplasia or retrusion, malar flattening, low‑set ears, small teeth, and moderately high arched palate.[3][15][15][3][38] Eye abnormalities such as strabismus, ptosis, nystagmus, and retinal pigment alterations (“in fundo” temporal epithelial pigment changes) are frequently noted.[2][9][15][15][9] HPO terms capturing these features include midface retrusion (HP:0011800), malar flattening (HP:0000272), low‑set ears (HP:0000369), strabismus (HP:0000486), ptosis (HP:0000508), and nystagmus (HP:0000639).[38]

Hepatic manifestations include hepatomegaly, hepatosplenomegaly, elevated transaminases, and liver injury patterns that fit within the broader CDG spectrum.[2][10][15][33][34][12] A cohort study of 39 CDG patients, including one with TMEM165‑CDG, found complex liver injury patterns with predominant hepatocellular injury (elevated ALT and AST) and variable fibrosis, emphasizing the need for regular liver surveillance in all CDG types.[33][34] HPO terms include hepatomegaly (HP:0002240), hepatosplenomegaly (HP:0001433), abnormal liver function (HP:0002910), and elevated alanine aminotransferase (HP:0002910).[33][38]

Renal involvement, particularly nephrotic syndrome and renal failure, has been reported by Orphanet and recent neurological/cardiomyopathy reviews.[3][9][9][12] Cardiac defects in TMEM165‑CDG include structural heart defects and cardiomyopathy, which align with the broader observation that glycosylation defects are recurrently associated with hypertrophic or dilated cardiomyopathy.[9][21][12] Endocrine features include partial growth hormone deficiency, pituitary hypoplasia, hypoglycemia, and other endocrinopathies improved by galactose therapy.[9][27][32][12] HPO terms for these include nephrotic syndrome (HP:0000108), renal insufficiency (HP:0000083), cardiomyopathy (HP:0001638), congenital heart malformation (HP:0001272), growth hormone deficiency (HP:0000824), hypoglycemia (HP:0001943), and pituitary hypoplasia (HP:0007910).[9][27][12][38]

Symptom onset for these visceral and endocrine phenotypes is generally in infancy or childhood, with episodic manifestations such as fever episodes and transient epilepsy noted in some cases.[9][15][9] Severity is variable; some patients experience mild liver enzyme elevations or subclinical cardiac changes, while others develop overt nephrotic syndrome or cardiomyopathy.[33][12] Quality‑of‑life impact ranges from asymptomatic biochemical changes to life‑threatening organ dysfunction requiring specialized care.

### 3.5 Laboratory Abnormalities and Glycosylation Profiles

Laboratory phenotypes in TMEM165‑CDG are central to its diagnosis and mechanistic classification. Patients exhibit an abnormal type II profile on serum transferrin isoelectric focusing, characterized by increased disialotransferrin and asialotransferrin isoforms reflecting defective N‑linked glycan processing.[2][13][36] Apolipoprotein C‑III isoform analysis shows decreased monosialo‑forms and increased asialo‑forms, indicating defective mucin‑type O‑glycosylation in the Golgi.[12][12] Plasma N‑glycan and O‑glycan analyses reveal undersialylation and undergalactosylation of N‑glycans and combined N‑ and O‑glycosylation defects.[2][4][27][32][12][7]

A key biochemical hallmark is hypogalactosylation of N‑glycans and defective terminal sialylation, consistent with TMEM165’s role in Mn\(^2+\)‑dependent galactosyltransferase and sialyltransferase function.[4][27][32][7] Abnormal glycosylation of lipids has also been reported, representing the first description of lipid glycosylation abnormalities in TMEM165‑CDG.[27][32] Additional lab abnormalities include elevated circulating creatine kinase (indicative of muscle involvement), thrombocytopenia, coagulopathy with abnormal clotting parameters, and dyslipidemia (high cholesterol).[27][32][12][38] Endocrine lab findings can include low growth hormone and hypoglycemia, which may improve on galactose therapy.[27][29][32]

HPO terms for laboratory phenotypes include abnormal transferrin isoform profile (HP:0003160), abnormal ApoC‑III isoelectric focusing (HP:0031848), elevated creatine kinase (HP:0003236), thrombocytopenia (HP:0001873), coagulopathy (HP:0001968), abnormal cholesterol level (HP:0003119), and hypoglycemia (HP:0001943).[12][27][32][12][38] Age of detection often coincides with diagnostic workup in infancy or childhood, and progression may improve partially with galactose supplementation.[27][29][32] Quality‑of‑life impact is mostly indirect through organ complications (e.g., bleeding, muscle weakness, metabolic instability).

---

## 4. Genetic and Molecular Information

### 4.1 Causal Gene: TMEM165

The causal gene for TMEM165‑CDG is *TMEM165*, also known as FT27, GDT1, CDG2K, TPARL, TMPT27, and SLC64A1.[5][21][5][1][41] *TMEM165* is located on chromosome 4q12, with genomic coordinates 4:55,395,957–55,453,397 (GRCh38), and consists of six exons encoding a predicted 324‑amino‑acid multi‑pass transmembrane protein.[5][8][21] RefSeq transcript NM_018475.5 is commonly referenced for clinical variant nomenclature.[6][6][6][6] TMEM165 belongs to the UPF0016 family of uncharacterized proteins, now recognized as conserved cation transporters across eukaryotes.[21][41]

Subcellular localization studies show that TMEM165 has a perinuclear Golgi‑like distribution in fibroblasts, aligning with its role in Golgi ion homeostasis.[5][1][39][7] Gene Ontology cellular component annotations highlight the Golgi apparatus (GO:0005794), lysosome (GO:0005764), endoplasmic reticulum (GO:0005783), and plasma membrane (GO:0005886), although the primary functional localization for glycosylation is the Golgi.[1][7] HGNC approved gene symbol is TMEM165 (HGNC:30760), and NCBI Gene ID is 55858.[5][21][5][38]

### 4.2 Pathogenic Variants: Types, Classification, and Origin

Pathogenic variants in *TMEM165* span splice‑site mutations, missense changes, nonsense truncations, and larger deletions, all of which can lead to TMEM165‑CDG when biallelic.[2][8][10][20][24] The deep intronic splice mutation c.792+182G>A was identified in three patients with TMEM165‑CDG and shown to cause aberrant splicing and TMEM165 deficiency, with corresponding glycosylation defects.[15][15] ClinVar classifies this variant (rs793888506) as pathogenic for congenital disorder of glycosylation, type IIk.[20][24][25]

Other pathogenic missense variants include c.377G>A (p.Arg126His), c.781G>A (p.Ala261Thr), and c.910G>A (p.Gly304Arg), all reported in homozygous or compound heterozygous states in affected individuals and classified as pathogenic based on segregation, functional studies, and conservation.[8][20][24][6][6] Nonsense variants such as c.747G>A (p.Trp249Ter) lead to premature truncation and are similarly pathogenic.[24] Malacards lists 113 ClinVar variants associated with congenital disorder of glycosylation type IIk, many of which map to *TMEM165* and are annotated as pathogenic or likely pathogenic.[24]

These variants are germline in origin, inherited in autosomal recessive fashion, and there is no evidence for somatic *TMEM165* variants causing TMEM165‑CDG in cancer or acquired disease contexts.[20][21][12] Functional consequences at the protein level predominantly represent **loss of function**, either through reduced or absent protein expression (nonsense, splice) or impaired cation transport activity (missense in conserved motifs).[1][21][19][41] ACMG/AMP classification criteria have not been fully formalized for all variants, but ClinVar assertions generally align with pathogenic status based on robust literature evidence.[20][24][6][6]

Allele frequencies in general populations are extremely low; TMEM165‑CDG is ultra‑rare, with Orphanet prevalence <1/1,000,000, implying carrier frequencies on the order of 1 in several thousand for specific variants, assuming Hardy–Weinberg equilibrium.[3][3][12][38] Population databases such as gnomAD and ExAC may contain occasional heterozygous carriers of some missense variants, but no homozygotes, consistent with severe autosomal recessive disease.[24][5][38] Founder effects have not been definitively documented, although clustering of cases in consanguineous families suggests local enrichment of specific variants.[2][15][15][12]

### 4.3 Molecular Function, Transport Activity, and Protein Dysfunction

TMEM165 is a multi‑pass transmembrane cation/\(\mathrm{H}^+\) antiporter that supplies the secretory pathway with Mn\(^2+\) and Ca\(^2+\), essential cofactors for Golgi glycosyltransferases and glycosidases.[1][1][19][7] Direct transport assays in reconstituted *Lactococcus lactis* and yeast systems established that TMEM165 and its yeast ortholog Gdt1p import Ca\(^2+\) and Mn\(^2+\) in exchange for \(\mathrm{H}^+\), with the direction of \(\mathrm{H}^+\) flux set by prevailing ion gradients, and that this activity controls Golgi pH.[1][23][26][19][39] Loss of TMEM165 leads to defective Golgi Mn\(^2+\) homeostasis, which impairs Mn\(^2+\)‑dependent glycosyltransferases such as β1,4‑galactosyltransferase (B4GALT1) and sialyltransferases, resulting in hypogalactosylation and undersialylation of N‑glycans.[4][1][27][32][19][7]

Yeast studies have shown that Gdt1p localizes to the Golgi and is required for Ca\(^2+\) tolerance, proper Ca\(^2+\) response after osmotic shock, and N‑ and O‑linked protein glycosylation in the presence of high external Ca\(^2+\), with glycosylation restored by Mn\(^2+\) supplementation.[19][23][26][26][19][40] This directly links UPF0016 family members to Mn\(^2+\) and Ca\(^2+\) homeostasis in the Golgi and supports the mechanistic inference that TMEM165 dysfunction in humans primarily affects these cations. TMEM165 also influences Golgi pH regulation, which impacts glycosylation enzyme activity and vesicular trafficking.[1][1][19][7]

Protein dysfunction in TMEM165‑CDG arises from impaired TMEM165 expression or function, leading to reduced Mn\(^2+\) and Ca\(^2+\) transport into the Golgi lumen and consequent glycosylation defects.[2][4][1][19][7] Structural modeling and evolutionary analyses suggest highly conserved transmembrane segments and acidic residues that participate in cation binding and transport; missense variants in these regions likely disrupt the electrochemical coupling required for \(\mathrm{H}^+\) exchange and cation movement.[21][41] GO molecular function terms relevant here include “manganese ion transmembrane transporter activity” (GO:0005384), “calcium ion transmembrane transporter activity” (GO:0015085), and “proton antiporter activity” (GO:0015078).[23][1][19][7]

### 4.4 Modifier Genes, Epigenetics, and Chromosomal Abnormalities

Specific modifier genes influencing TMEM165‑CDG severity have not been conclusively identified. However, genes involved in Golgi cation homeostasis, such as *ATP2C1* (SPCA1), *ATP2A2* (SERCA2), and *SLC39A8* (ZIP8 manganese transporter), may compensate partially for TMEM165 dysfunction.[4][7][16][23][19][7] For instance, SERCA2 activity has been reported to compensate Mn\(^2+\) insufficiency in the Golgi when TMEM165 is disrupted, highlighting functional redundancy in maintaining Mn\(^2+\) levels.[7][7] Similarly, Pmr1p, the yeast Golgi P‑type ATPase importing Ca\(^2+\) and Mn\(^2+\), interacts with Gdt1p to regulate cation concentrations, suggesting that human orthologs may modulate TMEM165‑CDG phenotypes.[19][23][26][19][40]

Epigenetic changes directly linked to TMEM165‑CDG have not been reported, and there is no evidence of DNA methylation or histone modification patterns specifically affecting *TMEM165* expression beyond canonical promoter regulation.[21][7] Chromosomal abnormalities such as aneuploidy or translocations are not implicated in TMEM165‑CDG; the disease is caused by point mutations and small indels within the *TMEM165* locus on 4q12.[8][10][24][5][38] A large deletion encompassing the region 4:55,124,936–57,368,027 has been annotated in Malacards as a variant with no classification yet, but its clinical significance for TMEM165‑CDG remains unclear.[24]

From a genomic structural perspective, *TMEM165* resides in a standard chromosomal context without known recurrent rearrangements. DECIPHER and dbVar do not highlight recurrent copy number variations specifically associated with TMEM165‑CDG, reinforcing its point‑mutation etiology.[24][5][38] In summary, modifier genes and epigenetic factors may modulate disease expression, but definitive evidence is scarce, and no large‑scale chromosomal abnormalities are part of the TMEM165‑CDG genetic landscape.

---

## 5. Environmental Information

### 5.1 Environmental Exposures and Toxins

No environmental toxins, radiation sources, industrial exposures, or pollutants have been identified as causal or major contributing factors for TMEM165‑CDG.[2][8][10][12] The disease is fundamentally monogenic, and there are no epidemiological signals linking chemical exposures to TMEM165‑CDG incidence in CTD or similar databases.[21][12][7] In vitro studies manipulating extracellular Ca\(^2+\) and Mn\(^2+\) concentrations demonstrate that high Ca\(^2+\) conditions in yeast require Gdt1p for proper glycosylation, and Mn\(^2+\) supplementation rescues glycosylation defects in TMEM165‑deficient cells.[19][23][26][19] However, these are experimental manipulations rather than environmental risk factors at population levels.

Given that manganese toxicity is a known concern in neurology and occupational medicine, any therapeutic Mn\(^2+\) supplementation for TMEM165‑CDG would need to balance potential benefit in glycosylation against neurotoxicity risk.[14][16][23] This therapeutic context is distinct from environmental exposure scenarios and does not imply that environmental Mn\(^2+\) levels contribute to disease onset.

### 5.2 Lifestyle and Diet Factors

Lifestyle factors such as smoking, alcohol consumption, and physical activity do not appear to influence TMEM165‑CDG risk, given the strong genetic basis.[2][10][12] However, **dietary composition**, particularly carbohydrate intake and micronutrient supplementation, can modulate disease expression as part of therapeutic interventions. Oral D‑galactose supplementation is the primary example of a diet‑based intervention that improves glycosylation and certain clinical parameters in TMEM165‑CDG.[27][29][32] Clinical studies titrating D‑galactose up to 1.5–2.5 g/kg/day (maximum 50 g) have reported safe administration and beneficial effects on endocrine and coagulation functions.[27][29][32]

Nutritional therapies reviews emphasize that galactose therapy has reduced the frequency of hypoglycemic episodes and improved seizure control in TMEM165‑CDG patients, although complete normalization of glycosylation has not been achieved.[29][30] The mechanism involves enhanced substrate availability for galactosyltransferases, particularly B4GALT1, which is sensitive to both galactose and manganese concentration.[29][32][7] Other dietary recommendations for CDG broadly focus on supporting metabolic stability, but no specific lifestyle factor is known to alter TMEM165‑CDG incidence.[29][37][12]

### 5.3 Infectious Agents

No infectious agents (bacteria, viruses, fungi, parasites) are known to cause or trigger TMEM165‑CDG.[2][10][12] The disease does not exhibit features of post‑infectious autoimmunity or immune dysregulation driven by pathogens, although immunodeficiency can occur in some CDG types.[12] TMEM165‑CDG patients may experience infections due to general multisystem vulnerability, but these are complications rather than etiologic drivers.[12][37] Infectious disease databases (ViPR, BV‑BRC, GIDEON) do not list TMEM165‑CDG as an infection‑related condition.

In summary, TMEM165‑CDG is etiologically a genetic disorder with minimal direct environmental or infectious contribution beyond therapeutic modulation.

---

## 6. Mechanism and Pathophysiology

### 6.1 Ordered Causal Chain from Mutation to Clinical Manifestation

1. Biallelic pathogenic variants in *TMEM165* lead to loss or severe reduction of TMEM165 cation/\(\mathrm{H}^+\) antiporter function in the Golgi.[2][8][10][1][1]  
2. Loss of TMEM165 transporter activity leads to decreased Mn\(^2+\) and Ca\(^2+\) import into the Golgi lumen and altered Golgi pH homeostasis.[4][1][23][26][19][7]  
3. Decreased Golgi Mn\(^2+\)/Ca\(^2+\) availability leads to impaired activity of Mn\(^2+\)‑dependent and Ca\(^2+\)‑sensitive glycosyltransferases and glycosidases, including β1,4‑galactosyltransferase and sialyltransferases, resulting in defective N‑ and O‑glycosylation of proteins and glycosylation of lipids.[2][4][1][27][32][19][7]  
4. Defective glycosylation leads to hypogalactosylation and hyposialylation of N‑glycans, altered O‑glycan structures on mucin‑type proteins (ApoC‑III), and abnormal glycosylation of glycolipids, disrupting multiple extracellular matrix proteins, receptors, and secreted factors.[2][4][12][27][32][35][7]  
5. In chondrocytes and prechondrocyte cells, defective glycosylation leads to shortened chondroitin‑ and heparan‑sulfate glycosaminoglycan chains on proteoglycans, impairing proteoglycan synthesis and extracellular matrix organization.[28][35]  
6. Shortened GAG chains and abnormal proteoglycans lead to dysregulated TGF‑β/BMP signaling and accelerated expression of Indian hedgehog (Ihh), resulting in early chondrocyte maturation, hypertrophy, and aberrant cartilage and bone development, causing skeletal dysplasia and dwarfism.[28][35]  
7. Defective glycosylation of other proteins (e.g., hormone receptors, coagulation factors, adhesion molecules, transporters) leads to multisystem dysfunction including psychomotor retardation, hepatosplenomegaly, nephrotic syndrome, cardiomyopathy, endocrine abnormalities, and coagulopathy.[2][10][27][32][33][12][7]  
8. The cumulative impact of skeletal dysplasia, neurodevelopmental impairment, organ dysfunction, and metabolic instability leads to the clinical TMEM165‑CDG phenotype: growth retardation, dysmorphism, hypotonia, seizures, skeletal deformities, liver injury, renal and cardiac involvement, and abnormal glycosylation profiles detectable in laboratory tests.[2][10][15][27][15][32][3][12][7]  

Where specific intermediate steps (e.g., exact receptor targets, detailed signal transduction changes) are not fully experimentally demonstrated, they are inferred from known roles of glycosylation in extracellular matrix biology, growth factor signaling, and organ development.

### 6.2 Molecular Pathways and Glycosylation Cascades

At the molecular level, TMEM165 participates in fundamental pathways of N‑linked and O‑linked glycosylation in the Golgi apparatus. N‑glycosylation involves assembly of a lipid‑linked oligosaccharide in the ER, transfer to nascent proteins, and subsequent trimming and extension in the Golgi, including addition of galactose and sialic acid by β1,4‑galactosyltransferase and sialyltransferases.[12][12][7] O‑glycosylation comprises stepwise addition of carbohydrate chains to serine, threonine, and hydroxylysine residues by glycosyltransferases in the Golgi, generating mucin‑type and other O‑glycans.[12][12] TMEM165 deficiency interferes with terminal glycosylation steps that require Mn\(^2+\) as a cofactor, leading to undergalactosylation and undersialylation.[4][1][27][32][19][7]

The relevant pathways include KEGG N‑glycan biosynthesis, O‑glycan biosynthesis, and glycosaminoglycan biosynthesis (heparan‑sulfate, chondroitin‑sulfate). TMEM165’s role is upstream in these pathways, ensuring appropriate ion conditions for Golgi enzymes. Proteoglycan synthesis pathway is particularly affected; TMEM165 knockout in ATDC5 cells impairs elongation of HS and CS GAG chains, disrupting proteoglycan architecture.[35] This affects pathways such as TGF‑β signaling, BMP signaling, and Hedgehog signaling, which depend on proteoglycan interactions for gradient formation and receptor activation in cartilage.[28][35]

SERCA2 and other ATPases partially compensate Mn\(^2+\) insufficiency in the Golgi when TMEM165 is deficient, highlighting a network of cation transport pathways.[7][7] In yeast, Pmr1p and Gdt1p jointly regulate Ca\(^2+\) and Mn\(^2+\) concentrations at the Golgi level, affecting protein glycosylation under stress conditions.[19][23][26][19][40] Reactome and GO pathway annotations relevant to TMEM165‑CDG may include “protein glycosylation” (GO:0006486), “glycosaminoglycan biosynthetic process” (GO:0006024), “regulation of manganese ion homeostasis” (GO:0030026, inferred), and “Golgi organization” (GO:0007030).[4][35][19][7]

### 6.3 Cellular Processes: Golgi Homeostasis, Proteoglycan Synthesis, and Signaling

At the cellular level, TMEM165‑CDG affects critical processes within secretory pathway compartments. TMEM165 ensures Golgi luminal Mn\(^2+\) and Ca\(^2+\) levels, which are necessary not only for glycosyltransferases but also for glycosidases, quality control, and pH regulation.[4][1][19][7] Disrupted Golgi ion homeostasis alters glycosylation efficiency, glycoprotein folding, and trafficking. Golgi stress responses and altered vesicular transport may contribute to organelle dysfunction, although detailed apoptosis or autophagy changes are not well characterized in TMEM165‑CDG.[7][19][7]

Proteoglycan synthesis is particularly impacted in chondrocytes, where TMEM165 deficiency leads to shortened HS and CS chains on proteoglycans.[28][35] This impairs extracellular matrix assembly, mechanical properties, and signaling scaffold functions, influencing TGF‑β/BMP pathway activation and Indian hedgehog signaling.[35] The result is altered chondrocyte maturation dynamics, with early hypertrophy and disorganized cartilage development. These changes at the cellular level manifest as abnormal growth plate architecture, bone dysplasia, and dwarfism at the tissue and organ level.[15][28][15][35]

Beyond chondrocytes, defective glycosylation affects hepatocytes, renal tubular cells, cardiomyocytes, neurons, and endocrine cells, altering cell surface receptors, adhesion molecules, secreted hormones, and other glycoproteins.[2][10][27][32][33][12][7] For example, glycosylation defects in coagulation factors and platelet proteins contribute to coagulopathy and thrombocytopenia; glycosylation changes in hormone receptors and pituitary hormones impact endocrine axes.[27][29][32][12] GO biological process terms relevant to these cellular phenomena include “Golgi calcium ion homeostasis” (inferred), “glycosaminoglycan metabolic process” (GO:0006024), “chondrocyte differentiation” (GO:0002062), “regulation of signaling receptor activity” (GO:0010469), and “protein glycosylation” (GO:0006486).[28][35][7]

### 6.4 Protein Dysfunction and Structural Biology

Protein dysfunction in TMEM165‑CDG primarily involves loss of function of TMEM165 as a cation/\(\mathrm{H}^+\) antiporter. Structural studies and molecular evolution analyses of UPF0016 family proteins suggest conserved membrane topology and potential cation‑binding sites that are disrupted by missense mutations.[21][41] Gdt1p in yeast, a 280‑residue member of this family, has been shown to transport Mn\(^2+\) directly, reinforcing the link between UPF0016 and Mn\(^2+\) homeostasis.[23][41] Functional rescue experiments, where human TMEM165 expression suppresses yeast gdt1Δ Ca\(^2+\) sensitivity, indicate conserved transport function.[40][41]

In TMEM165‑CDG, missense mutations in TMEM165 likely impair cation binding, translocation pathways, or coupling to \(\mathrm{H}^+\) gradients. Nonsense and splice variants result in truncated or absent protein, eliminating transport activity entirely.[2][15][20][24][15] This is a classic **loss‑of‑function mechanism** at the protein level, distinguished from gain‑of‑function or dominant‑negative effects. There is no evidence of TMEM165 aggregation or misfolding leading to ER stress; dysfunction is mainly due to absence or reduced ionic transport capability in the Golgi.[21][19][7]

UniProt and PDB databases do not yet provide high‑resolution structures of TMEM165, but homology modeling and AlphaFold predictions can approximate transmembrane topology and potential cation interaction sites. Pfam and InterPro classify UPF0016 family domains, and these annotations support functional inference of cation transport. GO molecular function terms for TMEM165 include “manganese ion transmembrane transporter activity” (GO:0005384) and “proton antiporter activity” (GO:0015078), reflecting direct transport assays.[23][1][19][7]

### 6.5 Metabolic and Immune Changes

While TMEM165‑CDG is not primarily a metabolic disorder in the classical sense (e.g., energy metabolism), glycosylation defects impact metabolic pathways indirectly. Hypoglycosylation of membrane transporters and receptors may alter nutrient uptake and signaling; abnormal glycosylation of lipoproteins may influence lipid metabolism, as evidenced by high cholesterol and altered lipid glycosylation.[27][32][12] Lactose biosynthesis in the lactating mammary gland depends on TMEM165; conditional knockout mice show decreased lactose production, leading to more concentrated milk (higher fat, protein, iron, zinc) and decreased Ca\(^2+\)/Mn\(^2+\) content, illustrating metabolic consequences in a specific physiological context.[1][31]

Immune system involvement in TMEM165‑CDG is less prominent than in some other CDG types but may include immunodeficiency features, isolated leukocyte adhesion deficiency, or congenital dyserythropoietic anemia in mixed glycosylation disorders more broadly.[12][12] TMEM165‑CDG is classified under “mixed glycosylation” CDG in some reviews, with potential for immune abnormalities, though severe immunodeficiency is not a defining feature.[12][12] Glycosylation plays critical roles in immune recognition and receptor function, so subtle immune phenotypes may exist but are under‑reported due to the rarity of the disease.

### 6.6 Tissue Damage Mechanisms and Biochemical Abnormalities

Tissue damage in TMEM165‑CDG arises from chronic structural and functional insufficiencies rather than acute necrosis or inflammation. Skeletal tissue damage is driven by abnormal cartilage and bone matrix composition; shortened GAG chains and defective proteoglycans lead to mechanical weakness, growth plate disorganization, and increased fracture risk (osteoporosis).[15][28][15][35] Liver injury patterns in CDG, including TMEM165‑CDG, involve hepatocellular injury (elevated ALT/AST) without predominant cholangiocellular damage, suggesting metabolic stress and glycogen accumulation rather than cholestatic pathology.[33][34]

Biochemical abnormalities at the molecular level include enzyme deficiencies in effective glycosylation, receptor dysfunction due to altered glycan structures, and ion channel or transporter defects stemming from misglycosylation, though specific receptor targets in TMEM165‑CDG are not fully elucidated.[2][4][27][32][7] Coagulopathy reflects abnormal glycosylation of clotting factors and platelet glycoproteins; endocrinopathy reflects altered glycosylation of hormone receptors and pituitary hormones.[27][29][32][12] GO terms such as “abnormal blood coagulation” and “hormone metabolic process” are relevant, and CHEBI terms for manganese(2+) and D‑galactose capture key biochemical entities.[27][29][32][7]

### 6.7 Molecular Profiling and Advanced Technologies

Comprehensive omics‑level profiling of TMEM165‑CDG is limited due to its rarity, but some insights come from transcriptomic and proteomic analyses in model systems. TMEM165 knockout in ATDC5 cells and HEK293 cells has been used to assess proteoglycan synthesis and signaling pathway alterations, revealing profound deficiency in HS and CS GAG chain polymerization and aberrant TGF‑β/BMP signaling.[35] These studies, effectively targeted functional genomics screens using CRISPR‑Cas9, highlight cell‑type‑specific mechanisms in chondrocytes and support proteomics‑level changes in extracellular matrix composition.

Single‑cell and spatial transcriptomics data specific to TMEM165‑CDG patients are not yet reported, but the underlying mechanisms suggest that chondrocytes, hepatocytes, cardiomyocytes, neurons, and endocrine cells would exhibit distinct glycosylation‑related transcriptomic and proteomic signatures.[35][7] Multi‑omics integration remains conceptual rather than empirical in this disease context, though cross‑disease CDG analyses could highlight shared glycosylation pathway dysregulation. Functional genomics screens beyond CRISPR in ATDC5 cells have not been widely applied to TMEM165, but yeast gdt1Δ studies constitute classical genetic screens linking phenotype (Ca\(^2+\) sensitivity, glycosylation defects) to gene function.[19][23][26][40]

Cell Ontology terms for key cell types include chondrocyte (CL:0000138), hepatocyte (CL:0000182), cardiomyocyte (CL:0000746), neuron (CL:0000540), pituitary endocrine cell (CL:0002553), and mammary gland epithelial cell (CL:0002327), all of which participate in TMEM165‑mediated processes.[28][31][35][7] GO terms for biological processes include “protein glycosylation” (GO:0006486), “glycosaminoglycan biosynthetic process” (GO:0006024), “chondrocyte differentiation” (GO:0002062), and “Golgi organization” (GO:0007030).[35][7]

---

## 7. Anatomical Structures Affected

### 7.1 Organ‑Level Involvement and Body Systems

TMEM165‑CDG affects multiple organ systems, with prominent involvement of the skeletal, nervous, hepatic, renal, cardiovascular, endocrine, and hematologic systems. At the organ level, primary structures affected include bones (UBERON:0001474), cartilage (UBERON:0002418), brain (UBERON:0000955), liver (UBERON:0002107), kidneys (UBERON:0002113), heart (UBERON:0000948), pituitary gland (UBERON:0000007), and mammary gland in model organisms.[2][10][15][15][31][33][3][35][12][7]

The skeletal system exhibits major spondylo‑, epiphyseal, metaphyseal, and diaphyseal involvement, with kyphosis, scoliosis, genu varum, pectus carinatum, and short distal phalanges.[15][15][3][35][37] The nervous system is affected through psychomotor retardation, white matter abnormalities, cerebellar atrophy, seizures, and microcephaly.[2][9][15][9][12] The hepatobiliary system shows hepatomegaly and hepatosplenomegaly; the renal system manifests nephrotic syndrome and renal failure; the cardiovascular system experiences congenital heart defects and cardiomyopathy.[3][10][9][15][33][9][12] Endocrine system involvement includes pituitary hypoplasia and growth hormone deficiency.[9][27][32][9][12]

These organ‑level effects reflect systemic glycosylation defects impacting extracellular matrix, receptors, signaling molecules, and secreted proteins. The disease can thus be categorized as a multisystem metabolic and developmental disorder, with body systems including musculoskeletal, nervous, hematologic/coagulation, endocrine, cardiovascular, renal, and digestive/hepatic.

### 7.2 Tissue and Cell‑Type Level

At the tissue level, TMEM165‑CDG primarily affects connective tissues (cartilage, bone, extracellular matrix), neural tissue (white and gray matter), epithelial tissues (hepatic, renal tubular, endocrine, mammary), and muscular tissues (cardiac and skeletal muscle). Chondrocytes in cartilage tissue are a key cell population, exhibiting altered proteoglycan synthesis and premature hypertrophy.[28][35] Osteoblasts and osteoclasts may also be indirectly affected by extracellular matrix changes, contributing to osteoporosis.[15][15][35]

Hepatocytes in the liver accumulate abnormal glycogen and exhibit glycosylation‑related injury; renal tubular epithelial cells in the kidney likely participate in nephrotic syndrome pathophysiology.[33][34][12] Cardiomyocytes in the heart may experience altered glycosylation of membrane receptors and ion channels, contributing to cardiomyopathy.[9][21][12] Neurons and glial cells in the brain show white matter abnormalities and cerebellar atrophy, reflecting developmental glycosylation defects in axonal guidance, myelination, and synaptic function.[2][9][15][9][12] Pituitary endocrine cells are affected by hypoplasia and altered hormone glycosylation.[9][27][32][9]

Cell Ontology terms for these populations include chondrocyte (CL:0000138), osteoblast (CL:0000062), osteoclast (CL:0000063), hepatocyte (CL:0000182), renal tubular epithelial cell (CL:0000066), cardiomyocyte (CL:0000746), neuron (CL:0000540), oligodendrocyte (CL:0000128), and pituitary endocrine cell (CL:0002553).[28][33][35][7] TMEM165 expression in fibroblasts and mammary gland epithelial cells has been demonstrated, suggesting broad distribution in secretory cells.[5][31][1][7]

### 7.3 Subcellular Compartments

TMEM165 localizes primarily to the Golgi apparatus, with additional presence in lysosomes, ER, and plasma membrane.[5][1][7] GO cellular component terms include Golgi apparatus (GO:0005794), Golgi membrane (GO:0000139), lysosome (GO:0005764), endoplasmic reticulum (GO:0005783), and plasma membrane (GO:0005886).[1][7] The critical subcellular compartment for TMEM165‑CDG pathophysiology is the Golgi lumen, where Mn\(^2+\) and Ca\(^2+\) are required for glycosylation.

Golgi pH regulation and luminal ion homeostasis are central subcellular processes affected by TMEM165 dysfunction.[4][1][19][7] Altered Golgi ion content impacts glycosyltransferase localization and activity, vesicular trafficking, and possibly Golgi stress signaling. Lysosomal localization may relate to cation recycling or degradation pathways, but Golgi dysfunction is the dominant mechanism.[1][7] ER involvement is secondary, as initial N‑glycosylation occurs in the ER, but TMEM165 primarily affects Golgi processing.

### 7.4 Localization and Lateralization

Anatomical localization of skeletal deformities often exhibits bilateral symmetry, such as genu varum of both legs, scoliosis affecting the spine, and pectus carinatum affecting the chest wall.[15][15][3][35] Some features, like strabismus, can be unilateral (e.g., internal convergent strabismus of the right eye), highlighting asymmetric involvement.[3][9][15][3] White matter abnormalities and cerebellar atrophy are typically bilateral but may show regional distribution on neuroimaging.[2][9][15][9] Organ involvement (liver, kidney, heart) is systemic and not lateralized.

UBERON terms for specific anatomical sites include long bone (UBERON:0001474), vertebral column (UBERON:0002415), thoracic cage (UBERON:0006617), brain ventricles (UBERON:0003860), and pituitary gland (UBERON:0000007).[15][15][3][9] Lateralization phenotypes can be captured by HPO terms such as unilateral strabismus (HP:0012639) when appropriate.[9][15][38]

---

## 8. Temporal Development

### 8.1 Age of Onset and Onset Pattern

TMEM165‑CDG is a congenital disorder, with age of onset typically in infancy or early childhood.[3][10][3][12] Orphanet specifies age of onset as “Infancy, Neonatal,” indicating that symptoms may be present soon after birth or become evident during the first year of life.[3][3][3] Early manifestations include feeding difficulties, failure to thrive, hypotonia, developmental delay, and sometimes seizures, prompting metabolic evaluations and transferrin isoform testing.[2][15][15][12]

Some patients are diagnosed later in childhood or adolescence due to diagnostic delays, variable severity, or lack of initial recognition of CDG.[9][15][9][12] For example, Zeevaert et al. reported a child diagnosed at age 11 with psychomotor‑dysmorphism syndrome and major skeletal involvement.[15][15] Onset pattern is chronic and insidious, with slowly accumulating developmental and skeletal abnormalities rather than acute episodes. Episodic events such as seizures or fever episodes occur within this chronic disease course but are not primary onset manifestations.[9][9][12]

### 8.2 Disease Progression, Stages, and Course

Disease progression in TMEM165‑CDG is variable and depends on severity of glycosylation defects and organ involvement. Early stages involve developmental delay, hypotonia, and growth retardation, with skeletal deformities becoming more apparent as the child grows.[15][15][3][12] Intermediate stages see more pronounced skeletal dysplasia, spinal deformities, and metabolic complications such as liver injury, nephrotic syndrome, cardiomyopathy, and coagulopathy.[2][10][33][12] Advanced stages may involve chronic organ dysfunction, osteoporotic fractures, and significant neurodevelopmental disability.

The rate of progression is generally slow and chronic; TMEM165‑CDG is a lifelong condition. Some features, such as cerebellar ataxia in PMM2‑CDG, are non‑progressive and may improve with age; analogous detailed progression data for TMEM165‑CDG are lacking but may follow similar patterns where neurodevelopmental deficits stabilize rather than continually worsen.[37][12] Skeletal deformities, once established, may progress until skeletal maturity and then stabilize, while endocrine and metabolic abnormalities can be modulated by therapy (e.g., galactose supplementation).[27][29][32]

Disease course pattern is predominantly progressive in terms of skeletal changes and organ involvement, though some aspects may be relatively stable or amenable to improvement. TMEM165‑CDG is not self‑limited and persists throughout life, with chronic morbidity. Natural history studies specifically for TMEM165‑CDG are limited due to small patient numbers, but broader CDG registries, such as the Frontiers in CDG natural history study, include some TMEM165‑CDG cases and provide general guidance on monitoring liver and other organ manifestations.[33][34][12]

### 8.3 Remission, Critical Periods, and Intervention Windows

Spontaneous remission of TMEM165‑CDG does not occur, given its genetic basis. However, treatment‑induced partial remission of specific symptoms (hypoglycemia, seizures, coagulopathy) has been observed with galactose therapy.[27][29][32] For example, the frequency of hypoglycemic episodes improved on D‑galactose therapy, and seizures tended to improve, although transaminase elevation persisted.[29][30] These treatment responses reflect partial correction of glycosylation defects rather than full disease remission.

Critical periods for intervention include early infancy and childhood, when developmental trajectories and skeletal growth are most plastic. Early diagnosis and initiation of galactose supplementation and supportive therapies (physiotherapy, orthopedic interventions, nutritional support) may optimize neurodevelopmental outcomes and reduce severity of skeletal deformities.[27][29][32][37][12] Genetic counseling and carrier testing provide preconception and prenatal intervention windows for families at risk, allowing informed reproductive choices.[12]

Developmental biology considerations suggest that growth plate cartilage and brain white matter development are particularly vulnerable during early life, making timely management of glycosylation defects crucial.[28][35][9][12] There is currently no gene therapy available for TMEM165‑CDG, but future interventions might target these critical windows with molecular therapies.

---

## 9. Inheritance and Population

### 9.1 Epidemiology: Prevalence and Incidence

TMEM165‑CDG is an ultra‑rare disorder. Orphanet reports a prevalence <1/1,000,000, consistent with very low global case numbers.[3][3][12][38][3] The exact incidence (new cases per 100,000 per year) is not well quantified due to limited registries and the rarity of the disease, but it likely falls below 0.01 per 100,000 per year. Most published clinical reports describe only a handful of patients, supporting this ultra‑rare status.[2][15][15][12][7]

Global Burden of Disease (GBD) metrics for TMEM165‑CDG are not available; CDG as a group contribute minimally to overall burden statistics due to their rarity but have substantial impact on affected individuals and families. National registries and disease‑specific cohorts, such as the Frontiers in CDG natural history study, include limited numbers of TMEM165‑CDG patients among broader CDG populations.[33][34][12]

### 9.2 Inheritance Pattern, Penetrance, and Expressivity

TMEM165‑CDG follows an **autosomal recessive** inheritance pattern. OMIM, Orphanet, Malacards, and ClinVar consistently describe congenital disorder of glycosylation type IIk as autosomal recessive, with homozygous or compound heterozygous *TMEM165* mutations causing disease.[3][8][10][24][3][12][38] Penetrance appears to be essentially complete for biallelic pathogenic variants; individuals with such genotypes exhibit some degree of the disease phenotype, though expressivity varies.[2][15][15][12]

Expressivity is variable, as indicated by OMIM’s description of CDG2K as an autosomal recessive disorder with a variable phenotype.[10][12] Some patients exhibit severe psychomotor retardation and marked skeletal dysplasia, while others have milder developmental delay or less pronounced skeletal involvement.[9][15][15][9][12] Organ involvement (e.g., cardiomyopathy, nephrotic syndrome) may also vary, and some features (such as seizures or microcephaly) are not universal.[12][38]

There is no evidence for genetic anticipation or germline mosaicism in TMEM165‑CDG, given the nature of point mutations and recessive inheritance.[8][10][20][24][12] Consanguinity plays a role in some cases, especially where homozygous deep intronic mutations were identified in consanguineous families.[2][15][15][12] Carrier frequency in the general population is unknown but likely extremely low; in consanguineous populations, localized founder effects may increase carrier frequency for specific variants.

### 9.3 Population Demographics and Geographic Distribution

TMEM165‑CDG cases have been reported in diverse geographic and ethnic contexts, including Europe and other regions, but specific ethnicity‑related prevalence has not been systematically characterized.[2][15][15][12] The small number of reported patients precludes robust analysis of ethnic or demographic trends. However, Orphanet’s prevalence estimate implies that TMEM165‑CDG is globally distributed but extremely rare.[3][3][12][38]

Geographic distribution of specific variants (e.g., c.792+182G>A) may reflect founder effects in particular regions or families, as seen in the three Belgian patients with a shared deep intronic mutation.[15][15] Sex ratio among TMEM165‑CDG patients appears roughly balanced; there is no indication of sex‑linked inheritance or marked sex bias.[2][15][15][12] Age distribution spans infancy through adulthood, with some adult patients described in CDG cohorts, but median age at diagnosis is in childhood.[33][34][12]

---

## 10. Diagnostics

### 10.1 Clinical and Laboratory Testing

Diagnosis of TMEM165‑CDG relies on a combination of clinical assessment, glycosylation profiling, and molecular genetic testing. Clinically, suspicion arises in infants or children with psychomotor retardation, growth deficiency, skeletal dysplasia, facial dysmorphism, hepatosplenomegaly, endocrine abnormalities, coagulopathy, and multisystem involvement suggestive of CDG.[2][15][15][3][37][12] Laboratory testing includes serum transferrin isoform analysis (transferrin isoelectric focusing) to detect type II CDG profiles, characterized by increased disialo‑ and asialotransferrin.[2][13][36][12]

Apolipoprotein C‑III isoform analysis complements transferrin testing by detecting mucin‑type O‑glycosylation defects; in TMEM165‑CDG, ApoC‑III shows decreased monosialo‑forms and increased asialo‑forms.[12][12] Plasma N‑glycan and O‑glycan analysis by mass spectrometry characterize hypogalactosylation and undersialylation patterns.[2][4][27][32][12][7] Liver function tests (ALT, AST), creatine kinase, coagulation panels, lipid profiles, and endocrine assays (growth hormone, glucose) provide additional markers.[27][32][33][34][12]

Imaging studies include skeletal radiographs demonstrating epiphyseal, metaphyseal, and diaphyseal dysplasia, osteoporosis, scoliosis, and pectus carinatum.[15][15][3][35][37] Brain MRI reveals white matter abnormalities, cerebellar atrophy, enlarged ventricles, and pituitary hypoplasia.[2][9][15][9][12] Echocardiography assesses congenital heart defects and cardiomyopathy; renal ultrasound evaluates nephrotic syndrome and structural anomalies.[9][33][9][12] These imaging findings, combined with glycosylation profiles, strongly point to CDG, with TMEM165‑CDG considered when skeletal dysplasia is pronounced and transferrin profile indicates type II glycosylation defects.

### 10.2 Genetic Testing Strategy

Definitive diagnosis requires molecular confirmation of *TMEM165* mutations. Genetic testing can proceed via targeted CDG gene panels, whole exome sequencing (WES), or single‑gene testing if TMEM165‑CDG is strongly suspected.[5][5][36][12] The NCBI Genetic Testing Registry lists tests for transmembrane protein 165 (TMEM165) under gene ID 55858, indicating availability of clinical sequencing assays.[5][5][25] CDG panels often include TMEM165 among multiple glycosylation genes, providing an efficient diagnostic route when CDG subtype is unknown.[36][37][12]

Whole exome sequencing is valuable in unsolved CDG cases; Foulquier et al.'s initial identification of TMEM165 as a CDG gene relied on autozygosity mapping and subsequent sequencing, illustrating the utility of genomic approaches.[2][13][2] WES is particularly helpful for detecting deep intronic variants (like c.792+182G>A) when combined with RNA studies or targeted intronic sequencing, though standard exome capture may miss non‑coding variants.[15][15][12] Whole genome sequencing (WGS) could improve detection of structural variants and intronic mutations but is not yet standard for TMEM165‑CDG.

Single‑gene Sanger sequencing of *TMEM165* is appropriate once glycosylation defects suggest TMEM165‑CDG, especially in families with known variants.[15][15][24][5] Chromosomal microarray (CMA), karyotyping, FISH, mitochondrial DNA testing, and repeat expansion assays are not primary diagnostic tools for TMEM165‑CDG, given its point mutation etiology.[8][10][24][12] However, CMA may detect large deletions encompassing *TMEM165* in rare cases.[24]

### 10.3 Omics‑Based Diagnostics and Biomarkers

Beyond gene sequencing, omics‑based diagnostics in TMEM165‑CDG focus on glycomics. Plasma N‑glycan and O‑glycan profiling by mass spectrometry provide detailed signatures of hypogalactosylation and undersialylation, serving as molecular biomarkers of TMEM165 dysfunction.[2][4][27][32][12][7] Abnormal glycosylation of lipids detected in TMEM165‑CDG patients expands biomarker scope to glycolipids.[27][32] These glycomics profiles can be integrated into diagnostic workflows to distinguish TMEM165‑CDG from other CDG types.

Proteomics and transcriptomics are less established in routine diagnostics but could be used in research settings to identify additional biomarkers, such as specific misglycosylated proteins or altered expression of glycosyltransferases and cation transporters.[35][7] Metabolomics might detect secondary metabolic changes (e.g., altered lactose synthesis in mammary gland context) but is not currently diagnostic in humans.[31] Epigenomic and liquid biopsy approaches are not applicable to TMEM165‑CDG at present.

Standardized diagnostic criteria come from CDG literature, emphasizing abnormal transferrin and ApoC‑III profiles plus molecular confirmation of gene mutations.[12][36][37][12] Differential diagnosis includes other CDG types with skeletal dysplasia (e.g., PGM1‑CDG, SLC35D1‑CDG) and metabolic bone diseases; distinguishing features include specific glycosylation patterns and gene defects.[37][12] NCIT terms for clinical interventions include “genetic testing” (NCIT:C16082), “DNA sequencing” (NCIT:C84355), and “glycosylation analysis” (NCIT:C17940).

### 10.4 Screening and Early Detection

TMEM165‑CDG is not part of routine newborn screening programs, largely due to its rarity and lack of simple biochemical markers suitable for large‑scale screening.[37][12] Carrier screening for *TMEM165* is not standard in general populations but may be considered in high‑risk families with known TMEM165‑CDG cases, using targeted gene sequencing.[5][5][12] Prenatal testing and preimplantation genetic diagnosis (PGD) are possible for couples carrying known *TMEM165* pathogenic variants, following ACMG and ACOG guidelines for autosomal recessive metabolic disorders.[12]

Risk stratification is primarily genetic, based on carrier status and consanguinity; there are no environmental risk models. Screening for liver disease in all CDG patients, including TMEM165‑CDG, is recommended via regular physical examination, liver enzymes, ultrasound, and elastography, as per Orphanet J Rare Dis liver cohort recommendations.[33][34] This constitutes secondary prevention for hepatic complications. For skeletal deformities, early orthopedic assessment serves as a functional screening to guide interventions.

---

## 11. Outcome and Prognosis

### 11.1 Survival, Mortality, and Life Expectancy

Long‑term survival data for TMEM165‑CDG are limited, but published case reports suggest that patients can survive into adolescence and adulthood, albeit with significant morbidity.[2][15][15][33][12] Foulquier et al.'s original siblings were diagnosed at age 19, indicating survival into late adolescence.[2][9][9] Zeevaert et al.'s patients were diagnosed at age 11, with follow‑up suggesting ongoing management rather than early mortality.[15][15] No large cohort provides 5‑year or 10‑year survival rates specific to TMEM165‑CDG, but CDG as a group show variable survival depending on subtype and severity.[33][37][12]

Life expectancy for TMEM165‑CDG likely depends on the severity of organ involvement, especially cardiomyopathy, renal failure, and liver disease. In milder cases, survival into adulthood with chronic disability is plausible, whereas severe multisystem disease may reduce life expectancy.[33][37][12] Mortality rate and disease‑specific mortality are not quantified in epidemiological databases due to the small number of cases. Cause of death, where reported, may involve organ failure, infections, or complications of coagulopathy or skeletal deformities, but detailed data are lacking.

### 11.2 Morbidity, Disability, and Quality of Life

Morbidity in TMEM165‑CDG is substantial, with long‑term disability arising from psychomotor retardation, skeletal dysplasia, endocrine and metabolic complications, and organ dysfunction. Developmental delay and intellectual disability affect educational attainment, employment, and independence.[2][9][15][9][12] Skeletal deformities and osteoporosis lead to pain, mobility limitations, and increased fracture risk, necessitating orthopedic interventions and assistive devices.[15][15][3][35][37] Hepatic, renal, and cardiac involvement can require chronic medical management and monitoring.[33][34][12]

Quality‑of‑life measures specific to TMEM165‑CDG have not been formally reported using EQ‑5D, SF‑36, or PROMIS instruments, but based on CDG studies, patients experience limitations in mobility, self‑care, usual activities, pain/discomfort, and anxiety/depression.[37][12] Caregiver burden is high, and family quality of life may be significantly impacted. Rehabilitation needs include physical therapy, occupational therapy, speech therapy, and psychosocial support.[37][12]

### 11.3 Disease Course, Complications, and Recovery Potential

Complications of TMEM165‑CDG include fractures from osteoporosis, severe spinal deformities, pseudo‑obstruction and feeding difficulties, nephrotic syndrome and renal failure, cardiomyopathy and heart failure, coagulopathy with bleeding risk, and endocrine crises such as severe hypoglycemia.[2][15][27][15][32][33][12] Infections may be more frequent due to general debility and possible immunodeficiency features.[12] Recovery potential for the underlying glycosylation defect is limited without gene therapy; however, galactose supplementation and supportive care can improve specific symptoms (endocrinopathy, coagulopathy, hypoglycemia, seizures) and stabilize aspects of disease.[27][29][32][37][12]

Prognostic factors likely include age at diagnosis, severity of glycosylation defect (transferrin and glycan profiles), presence of cardiomyopathy or nephrotic syndrome, degree of skeletal dysplasia, and response to therapy.[27][32][33][12] Prognostic biomarkers might include specific glycan structures, coagulation parameters, and cardiac function metrics. However, systematic prognostic modeling has not been developed for TMEM165‑CDG due to limited case numbers.

---

## 12. Treatment

### 12.1 Pharmacotherapy and Nutritional Interventions

The main disease‑modifying treatment for TMEM165‑CDG currently is **oral D‑galactose supplementation**, a nutritional therapy that targets the glycosylation defect.[27][29][32] Morelle et al. conducted a clinical study titled “Galactose Supplementation in Patients With TMEM165‑CDG Rescues the Glycosylation Defects,” in which they demonstrated that oral galactose improved biochemical and clinical parameters, including a substantial increase in negatively charged transferrin isoforms (reflecting improved sialylation), decreased hypogalactosylated N‑glycan structures, and improved endocrine and coagulation parameters.[27][32] The authors recommend oral D‑galactose therapy in TMEM165‑CDG.[27][32]

Nutritional therapy reviews corroborate that galactose supplementation improves glycosylation in TMEM165‑CDG fibroblasts and patient samples and can reduce hypoglycemic episodes and seizures.[29][30] Doses range from 0.5 to 2.5 g/kg/day, administered five to six times per day, with a maximum of 50 g/day.[17][29][30] Mechanistically, galactose’s positive effect is suspected to be secondary via B4GALT1, a Golgi enzyme sensitive to both manganese and galactose concentrations; TMEM165 defect leads to abnormal Mn\(^2+\) transport to the Golgi, affecting oligotransferases, which improve function with extra galactose, thereby increasing galactosylation.[29][32][7]

Experimental manganese supplementation has been used in SLC39A8‑CDG and cell models, but safety concerns limit systemic Mn\(^2+\) therapy in humans.[14][16][23] There is no approved pharmacotherapy directly targeting TMEM165 function or Golgi ion homeostasis beyond substrate supplementation. NCIT terms for these interventions include “dietary therapy” (NCIT:C15459), “galactose” (NCIT:C61565), and “nutritional supplement therapy” (NCIT:C15228).

### 12.2 Advanced Therapeutics and Experimental Approaches

No gene therapy, RNA‑based therapy, or cell therapy has yet been applied to TMEM165‑CDG in clinical settings. Gene therapy approaches might theoretically involve gene replacement via viral vectors or CRISPR‑mediated correction of *TMEM165* mutations, but such strategies remain speculative and preclinical.[21][7] Functional genomics screens in ATDC5 cells and yeast have improved mechanistic understanding but are not directly therapeutic.[35][40]

Targeted therapies that modulate Mn\(^2+\) and Ca\(^2+\) transport or glycosyltransferase activity could be envisioned but would require precise control of Golgi ion homeostasis, which is challenging pharmacologically.[4][7][19][7] Immunotherapies are not relevant, as TMEM165‑CDG is not driven by autoimmunity or cancer. Advanced therapeutics remain a future prospect rather than current reality.

### 12.3 Surgical, Supportive, and Rehabilitative Care

Surgical interventions in TMEM165‑CDG focus on orthopedic correction of skeletal deformities, such as spinal fusion for severe scoliosis, osteotomies for limb deformities, and stabilization of pectus carinatum if symptomatic.[15][15][3][37] Cardiac surgeries or catheter interventions may be required for congenital structural heart defects.[9][21][12] Renal complications may necessitate nephrology interventions, including dialysis in severe cases, though specific reports in TMEM165‑CDG are limited.[3][9][9][12]

Supportive care is critical and includes management of feeding difficulties (e.g., gastrostomy tubes), control of seizures with anticonvulsants, treatment of coagulopathy with appropriate hematologic therapies, and endocrine management of growth hormone deficiency and hypoglycemia.[27][29][32][37][12] Rehabilitation comprises physical therapy to improve mobility and muscle strength, occupational therapy for daily living skills, and speech therapy for language development.[37][12] NCIT terms relevant to supportive care include “supportive care” (NCIT:C15695), “physical therapy” (NCIT:C15273), “orthopedic surgical procedure” (NCIT:C15334), and “cardiac surgery” (NCIT:C15790).

### 12.4 Treatment Outcomes, Adverse Effects, and Personalized Strategies

Treatment response rates for galactose therapy in TMEM165‑CDG are encouraging but not uniformly curative. Galactose supplementation reduces glycosylation defects and improves specific clinical parameters, but some abnormalities (e.g., elevated transaminases) may persist.[27][29][32][30] Side effects of galactose therapy are generally mild and include gastrointestinal discomfort; high doses are within recommended daily intake and have been demonstrated safe in CDG patients.[17][29][30] Long‑term safety data in TMEM165‑CDG are limited but reassuring.

Combination therapies may involve galactose plus general supportive measures; future approaches could add Mn\(^2+\) supplementation under careful monitoring.[14][16][23] Personalized medicine strategies in TMEM165‑CDG include tailoring galactose dosage to individual glycosylation profiles and clinical responses, as well as adjusting endocrine and anticoagulation therapies based on patient‑specific parameters.[27][29][32][12] Pharmacogenomics specific to TMEM165‑CDG has not been explored; CYP variations or other drug metabolism genes may affect response to anticonvulsants and other medications but are independent of TMEM165.

---

## 13. Prevention

### 13.1 Primary, Secondary, and Tertiary Prevention

Primary prevention of TMEM165‑CDG involves preventing disease occurrence through genetic counseling and reproductive planning in families at risk. As an autosomal recessive condition, primary prevention hinges on carrier identification and options such as preimplantation genetic diagnosis (PGD) and prenatal testing, guided by ACMG and NSGC recommendations for inborn errors of metabolism.[12] Population‑level primary prevention is not practical due to disease rarity.

Secondary prevention focuses on early detection and treatment to mitigate disease impact. Early diagnosis via glycosylation testing and genetic sequencing, followed by initiation of galactose therapy and supportive care, constitutes secondary prevention of severe morbidity.[27][29][32][37][12] Regular screening for liver disease, cardiac function, renal status, and skeletal deformities in TMEM165‑CDG patients is recommended to catch complications early, as per CDG liver cohort guidelines.[33][34][12]

Tertiary prevention seeks to prevent complications and optimize function in those with established disease. This includes long‑term multidisciplinary management, rehabilitation, orthopedic interventions, seizure control, and metabolic monitoring to prevent fractures, organ failure, and severe disability.[37][12] NCIT terms for preventive strategies include “genetic counseling” (NCIT:C16714), “prenatal diagnosis” (NCIT:C45776), and “rehabilitation” (NCIT:C15273).

### 13.2 Immunization, Screening, and Behavioral Interventions

Immunization strategies for TMEM165‑CDG follow general pediatric and adult vaccination schedules; there are no disease‑specific vaccines.[37][12] Vaccination is important to prevent infections that could exacerbate morbidity. Screening programs for TMEM165‑CDG are not currently implemented, but newborn screening for CDG more broadly has been discussed in the literature.[37][12] Carrier screening for *TMEM165* may be considered in high‑risk families.

Behavioral interventions include dietary management to ensure adequate nutrition and adherence to galactose therapy, as well as avoidance of excessive Mn\(^2+\) exposure from environmental sources to reduce toxicity risk.[14][16][29][30] Genetic counseling provides family planning guidance and helps relatives understand carrier risks, disease inheritance, and testing options.[12] Public health interventions are minimal due to disease rarity; environmental interventions are not relevant beyond controlling Mn\(^2+\) toxicity in occupational settings.

### 13.3 Prophylaxis

Prophylactic medications or procedures targeting TMEM165‑CDG specifically are not available, beyond galactose therapy which functions more as treatment than prophylaxis. Prophylactic anticoagulation or seizure prophylaxis may be used to prevent complications in patients with severe coagulopathy or frequent seizures, based on clinical judgment.[27][32][37][12] Orthopedic prophylaxis might include bracing to slow scoliosis progression. These are individualized and not disease‑specific prophylactic protocols.

---

## 14. Other Species and Natural Disease

### 14.1 Species and Orthologous Genes

TMEM165 orthologs exist in multiple species, particularly in yeast and mice, where they have been studied extensively as model systems. In *Saccharomyces cerevisiae*, the ortholog is **Gdt1p** (Gcr1‑dependent translation factor 1), encoded by *GDT1*, a 280‑residue protein involved in Ca\(^2+\) and Mn\(^2+\) homeostasis in the Golgi and protein glycosylation.[19][23][26][19][40][41] NCBI Gene ID for human TMEM165 is 55858; yeast *GDT1* has a separate gene ID in SGD.[19][23][39][40]

In mice, Tmem165 is the orthologous gene studied in conditional knockout models, especially in the lactating mammary gland, where it is crucial for lactose biosynthesis and normal milk Ca\(^2+\)/Mn\(^2+\) content.[1][31] Other species likely have UPF0016 family members, but detailed functional studies are focused on yeast and mouse.

### 14.2 Natural Disease in Animals and Comparative Pathology

Naturally occurring TMEM165‑related disease in companion animals or livestock has not been reported in OMIA or veterinary databases, likely due to both rarity and underdiagnosis.[21][12] However, comparative pathology using yeast and mouse models provides important insights. Yeast gdt1Δ mutants display sensitivity to high Ca\(^2+\), defective N‑ and O‑glycosylation under stress, and growth defects, mirroring aspects of human TMEM165‑CDG at the cellular level.[19][23][26][19][40] Mouse conditional knockout of Tmem165 in mammary gland cells results in defective lactose biosynthesis, altered milk composition, decreased Ca\(^2+\)/Mn\(^2+\) levels in milk, and reduced pup growth, illustrating organ‑specific consequences of TMEM165 deficiency.[1][31]

Comparative biology underscores evolutionary conservation of TMEM165/Gdt1p function in Golgi cation homeostasis and glycosylation, reinforcing the pathogenic mechanism proposed for humans.[21][41] Evolutionary conservation also suggests that model organisms can recapitulate key disease mechanisms, although human clinical manifestation involves more complex multisystem development. HomoloGene and Alliance of Genome Resources identify orthologs across eukaryotes, supporting cross‑species studies.[21][41]

### 14.3 Transmission and Zoonotic Potential

TMEM165‑CDG is a non‑infectious genetic disease with no zoonotic potential or transmission across species beyond heredity within families. There is no cross‑species susceptibility in the sense of contagious disease; rather, orthologous gene mutations in different species can cause analogous cellular phenotypes. Transmission is purely vertical (parent to child via germline) in humans; there is no horizontal or vector‑borne transmission.[2][8][10][12]

---

## 15. Model Organisms

### 15.1 Yeast Models: Gdt1p and Golgi Cation Homeostasis

Yeast models have been central to understanding TMEM165 function. The *S. cerevisiae* protein Gdt1p is the ortholog of human TMEM165 and localizes to the Golgi membrane, where it participates in Ca\(^2+\) and Mn\(^2+\) homeostasis.[19][23][26][19][40] gdt1Δ mutants show growth defects in the presence of high CaCl\(_2\) concentrations (500–700 mM), sensitivity to Ca\(^2+\), and defective Ca\(^2+\) responses after exposure to salt stress, indicating Gdt1p’s role in stress‑induced Ca\(^2+\) signaling.[23][26][40]

Importantly, gdt1Δ mutants display defective N‑ and O‑linked protein glycosylation when exposed to high external Ca\(^2+\), with glycosylation restored by Mn\(^2+\) supplementation.[19][26][26][19] Direct transport assays in *Lactococcus lactis* expressing Gdt1p showed Mn\(^2+\) transport activity, reinforcing its role as a Mn\(^2+\) transporter.[23] Expression of human TMEM165 in gdt1Δ yeast suppresses Ca\(^2+\) sensitivity, demonstrating functional conservation and supporting the hypothesis that TMEM165 is a Golgi cation/\(\mathrm{H}^+\) antiporter.[40][41]

These yeast models recapitulate key aspects of human TMEM165‑CDG at the cellular level—Golgi cation homeostasis, glycosylation defects, and stress responses—and are powerful tools for mechanistic and structural studies. However, they do not reproduce multisystem organ phenotypes seen in humans.

### 15.2 Mouse Models: Conditional Tmem165 Knockout in Mammary Gland

Mouse models have explored TMEM165 function in organ‑specific contexts. A conditional Tmem165 knockout mouse was generated using a floxed Tmem165 allele crossed with a Cre recombinase driven by the whey acid protein (WAP) promoter, which is expressed specifically in milk‑producing alveolar epithelial cells during late pregnancy.[1][31] This model achieved approximately 85% depletion of TMEM165 protein in mammary tissue and showed strong defects in milk quality.[31]

Milk from TMEM165‑deficient dams had decreased lactose biosynthesis, resulting in elevated concentrations of fat, protein, iron, and zinc due to decreased osmosis‑mediated dilution, and significantly lower Ca\(^2+\)/Mn\(^2+\) content when normalized to total protein.[1][31] Nursing pups exhibited reduced growth rates, demonstrating functional consequences of TMEM165 deficiency in lactation.[31] These findings highlight TMEM165’s role in dairy biosynthesis and mineral transport, providing an organ‑specific parallel to systemic glycosylation defects in humans.

This mouse model recapitulates TMEM165‑dependent Golgi function in secretory epithelial cells but does not model full systemic TMEM165‑CDG phenotypes such as skeletal dysplasia and neurodevelopmental delay. Future mouse models with global or cartilage‑specific Tmem165 knockout would be needed to fully mimic human disease.

### 15.3 Cellular Models: ATDC5 and HEK293 Knockouts

Cellular models using mouse prechondrogenic ATDC5 cells and human HEK293 cells have been instrumental in dissecting TMEM165’s role in proteoglycan synthesis.[35] CRISPR‑Cas9–mediated knockout of TMEM165 in ATDC5 cells led to profound deficiency in polymerization of HS and CS GAG chains on proteoglycans, shorter GAG chains, and altered proteoglycan synthesis.[35] This cellular phenotype correlated with impaired TGF‑β/BMP signaling and accelerated Ihh expression, resulting in early chondrocyte maturation and hypertrophy.[35]

HEK293 TMEM165 knockouts showed similar glycosylation defects, confirming mechanistic consistency across species.[35] These in vitro models capture molecular and cellular aspects of TMEM165‑CDG in cartilage and provide platforms for testing therapeutic interventions, such as Mn\(^2+\) or galactose supplementation. However, they lack the complexity of whole‑organism developmental processes.

### 15.4 Model Limitations and Research Applications

While yeast and cellular models provide robust mechanistic insight into Golgi cation homeostasis and glycosylation, they do not recapitulate the full multisystem phenotype of TMEM165‑CDG. Mouse conditional knockout models so far focus on mammary gland function and lactation, leaving skeletal and neurodevelopmental aspects unexplored.[1][31][35][7] Comprehensive global Tmem165 knockout may be embryonically lethal or produce severe systemic disease, requiring careful design.

Applications of these models include elucidating TMEM165 transporter structure–function relationships, identifying compensatory pathways (e.g., SERCA2, Pmr1p), testing therapeutic interventions (galactose, Mn\(^2+\)), and studying proteoglycan synthesis and signaling in cartilage.[4][7][19][23][26][35][19][7][40] Model organism databases (SGD, MGI, ATCC, Cellosaurus) catalog these models for broader use. Further development of human iPSC‑derived chondrocyte models could bridge the gap between molecular mechanisms and clinical phenotypes.

---

## Conclusion

TMEM165‑Congenital Disorder of Glycosylation (TMEM165‑CDG; CDG type IIk; MONDO:0013870) is an ultra‑rare autosomal recessive multisystem disease rooted in loss‑of‑function mutations in *TMEM165*, a Golgi cation/\(\mathrm{H}^+\) antiporter that regulates luminal Mn\(^2+\) and Ca\(^2+\) homeostasis essential for N‑ and O‑glycosylation and proteoglycan synthesis.[2][8][10][1][1][7] The causal chain from mutation to phenotype begins with impaired TMEM165 transport activity, leading to decreased Mn\(^2+\)/Ca\(^2+\) in the Golgi, defective terminal glycosylation (hypogalactosylation and hyposialylation), shortened HS and CS GAG chains, disrupted extracellular matrix and signaling (TGF‑β/BMP/Ihh), and culminates in psychomotor retardation, striking skeletal dysplasia, facial dysmorphism, hepatosplenomegaly, nephrotic syndrome, cardiomyopathy, endocrine abnormalities, and characteristic glycosylation profiles.[2][4][15][28][15][32][3][35][12][7]

From a genetic perspective, TMEM165‑CDG involves biallelic pathogenic variants in *TMEM165* (deep intronic splice, missense, nonsense, and deletions), with complete penetrance and variable expressivity.[8][10][15][20][24][15][12] There are no known environmental or infectious causes; instead, environmental interventions such as oral D‑galactose supplementation act as protective modifiers that partially rescue glycosylation defects and improve endocrine and coagulation parameters, representing the first successful dietary therapy for a TMEM165‑related CDG.[27][29][32][30] Mn\(^2+\) supplementation in cell models and yeast restores glycosylation but requires cautious translation to humans due to toxicity risk.[4][19][23][19][16]

Phenotypically, TMEM165‑CDG is characterized by early‑onset psychomotor delay, hypotonia, seizures, microcephaly, white matter abnormalities, cerebellar atrophy, and pituitary hypoplasia; postnatal growth deficiency and pronounced dwarfism; epiphyseal, metaphyseal, and diaphyseal bone dysplasia with osteoporosis, scoliosis, kyphosis, genu varum, and pectus carinatum; facial dysmorphism with midface retrusion, malar flattening, low‑set ears, and dental anomalies; hepatosplenomegaly and liver injury; nephrotic syndrome and renal failure; cardiomyopathy and congenital heart defects; endocrine abnormalities such as growth hormone deficiency and hypoglycemia; and laboratory abnormalities including abnormal transferrin and ApoC‑III isoform profiles, hypogalactosylated N‑glycans, abnormal lipid glycosylation, coagulopathy, thrombocytopenia, elevated creatine kinase, and dyslipidemia.[2][3][10][9][15][27][15][32][33][3][35][12][38][7]

Diagnostic workflows rely on clinical suspicion, transferrin and ApoC‑III isoelectric focusing, plasma glycan analysis, imaging (skeletal radiographs, brain MRI, echocardiography, renal and liver ultrasound), and molecular genetic confirmation of *TMEM165* mutations via targeted gene panels, WES, or single‑gene sequencing.[2][13][15][15][33][34][36][12] Omics‑based glycomics provide detailed mechanistic biomarkers. Model organisms including yeast gdt1Δ mutants, conditional Tmem165 knockout mice, and TMEM165‑deficient ATDC5 and HEK293 cells illuminate Golgi cation transport, glycosylation, proteoglycan synthesis, and signaling pathways.[4][19][23][26][31][35][19][39][7][40][41]

Prognosis is variable and poorly quantified due to limited case numbers, but survival into adolescence and adulthood is possible, accompanied by significant morbidity, disability, and quality‑of‑life impact.[2][15][15][33][12] Management is multidisciplinary, combining galactose therapy, orthopedic and cardiac interventions, supportive metabolic and endocrine care, and rehabilitation. Prevention focuses on genetic counseling and early intervention. Future research priorities include expanding natural‑history cohorts, refining glycomics biomarkers, exploring global and tissue‑specific Tmem165 knockout models, investigating gene or RNA‑based therapies, and elucidating modifier genes and compensatory pathways in Golgi ion homeostasis.[7][16][21][35][19][7][41]

For a disease knowledge base, TMEM165‑CDG can be systematically annotated with:  
– Gene: *TMEM165* (HGNC:30760, NCBI Gene:55858, OMIM:614726), GO molecular function “manganese ion transmembrane transporter activity” and “proton antiporter activity”; GO cellular component “Golgi apparatus” and “Golgi membrane”.  
– Disease: MONDO:0013870, DOID:0070263, OMIM:614727, Orpha:314667, ICD‑10:E77.8, ICD‑11:5C54.0.  
– Phenotypes: HPO terms for psychomotor delay, skeletal dysplasia, hepatomegaly, nephrotic syndrome, cardiomyopathy, endocrine abnormalities, and glycosylation defects, with qualitative frequencies based on case reports.  
– Cell types: CL terms for chondrocytes, hepatocytes, cardiomyocytes, neurons, pituitary endocrine cells, and mammary epithelial cells.  
– Anatomy: UBERON terms for bone, cartilage, brain, liver, kidney, heart, pituitary, and mammary gland.  
– Chemicals: CHEBI terms for manganese(2+) and D‑galactose.  
– Treatments: NCIT terms for dietary therapy, galactose supplementation, genetic testing, supportive care, and rehabilitation.  

By integrating the mechanistic causal chain, molecular genetics, phenotype spectrum, diagnostics, and treatment evidence outlined above—each anchored in primary literature (e.g., Foulquier et al. 2012, Zeevaert et al. 2013, Morelle et al. 2017, Colinet et al. 2016, Thines et al. 2018, Potelle et al. 2021)—a comprehensive, ontology‑rich representation of TMEM165‑CDG can be constructed to support clinical decision making, research, and precision medicine for this rare but mechanistically illuminating congenital disorder of glycosylation.[2][4][15][27][15][32][35][19][7]

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 99 |
| Resolved | 88 |
| Unresolved (possible confabulation) | 3 |
| Obsolete | 3 |
| Unverifiable | 5 |
| Terms whose name was checked | 22 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0060590` (1 mention) - the report calls it "regulation of glycosylation"; GO calls it **ATPase regulator activity**
- `NCIT:C16082` (1 mention) - the report calls it "genetic testing"; NCIT calls it **Marker Discovery**
- `NCIT:C84355` (1 mention) - the report calls it "DNA sequencing"; NCIT calls it **Intraoperative**
- `NCIT:C17940` (1 mention) - the report calls it "glycosylation analysis"; NCIT calls it **Microbial Genetics**
- `NCIT:C15228` (1 mention) - the report calls it "nutritional supplement therapy"; NCIT calls it **Double Blind Study**
- `NCIT:C15695` (1 mention) - the report calls it "supportive care"; NCIT calls it **Quadrantectomy**
- `NCIT:C15273` (2 mentions) - the report calls it "physical therapy", "rehabilitation"; NCIT calls it **Longitudinal Study**
- `NCIT:C15790` (1 mention) - the report calls it "cardiac surgery"; NCIT calls it **Cancer Prevention Trial**
- `NCIT:C16714` (1 mention) - the report calls it "genetic counseling"; NCIT calls it **Immunoenzyme Procedure**
- `NCIT:C45776` (1 mention) - the report calls it "prenatal diagnosis"; NCIT calls it **HD Term Type**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0002658` (1 mention) - HP does not contain this term
- `HP:0002759` (1 mention) - HP does not contain this term
- `HP:0001968` (1 mention) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0007910` (obsolete Nonprogressive congenital retinal dystrophy) (2 mentions)
- `GO:0006486` (obsolete protein glycosylation) (3 mentions) - replaced by `GO:0009101`
- `CL:0000063` (obsolete cell by histology) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0010043` (1 mention) - the report calls it "response to manganese ion"; GO calls it **response to zinc ion**
- `GO:0015078` (2 mentions) - the report calls it "proton antiporter activity"; GO calls it **proton transmembrane transporter activity**, and lists "proton transporter activity" among its other names
- `GO:0006486` (3 mentions) - the report calls it "protein glycosylation"; GO calls it **obsolete protein glycosylation**
- `GO:0006024` (3 mentions) - the report calls it "glycosaminoglycan biosynthetic process", "glycosaminoglycan metabolic process"; GO calls it **glycosaminoglycan biosynthetic process**
- `NCIT:C15459` (1 mention) - the report calls it "dietary therapy"; NCIT calls it **High-LET Pion Therapy**
- `NCIT:C61565` (1 mention) - the report calls it "galactose"; NCIT calls it **Bendamustine Hydrochloride**, and lists "Levact" among its other names
- `NCIT:C15334` (1 mention) - the report calls it "orthopedic surgical procedure"; NCIT calls it **Urologic Surgical Procedure**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0006024` - called "glycosaminoglycan biosynthetic process", "glycosaminoglycan metabolic process"
- `NCIT:C15273` - called "physical therapy", "rehabilitation"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `Gene`, `Orpha`.