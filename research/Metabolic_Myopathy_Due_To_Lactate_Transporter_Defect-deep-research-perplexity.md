---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-30T11:05:29.437692'
end_time: '2026-10-30T11:10:02.713960'
duration_seconds: 273.28
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Metabolic Myopathy Due To Lactate Transporter Defect
  mondo_id: MONDO:0009501
  category: Mendelian
  causal_genes: SLC16A1
  omim_id: OMIM:245340
  synonyms: erythrocyte lactate transporter defect
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 58
reference_validation:
  total_references: 20
  verified: 19
  not_found: 0
  unverifiable: 1
  confabulation_rate: 0.0
  relevance_assessed: 19
  on_topic: 6
  validator_version: 0.4.0
term_validation:
  total_terms: 35
  verified: 28
  not_found: 0
  obsolete: 0
  unverifiable: 7
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0009501
    reported_labels:
    - MONDO
    ontology_label: metabolic myopathy due to lactate transporter defect
  - term_id: HP:0003236
    reported_labels:
    - Present in the original and expanded cases; exact values and universal frequency
      not published in accessible summaries
    ontology_label: Elevated circulating creatine kinase activity
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  - MGI
  - RGD
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Metabolic Myopathy Due To Lactate Transporter Defect
- **MONDO ID:** MONDO:0009501 (if available)
- **Causal gene(s):** SLC16A1
- **OMIM:** OMIM:245340
- **Synonyms:** erythrocyte lactate transporter defect
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Metabolic Myopathy Due To Lactate Transporter Defect** covering all of the
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

# Metabolic Myopathy Due to Lactate Transporter Defect  
**Disease-characteristics research report — current to 30 October 2026**

## Executive summary and evidence appraisal

**Metabolic myopathy due to lactate transporter defect is an exceptionally rare, exertion-triggered myopathy attributed to heterozygous variants in the causal gene *SLC16A1*, which encodes monocarboxylate transporter 1 (MCT1).** The defining phenotype is impaired erythrocyte and skeletal-muscle lactate transport, with exercise- or heat-associated cramping, stiffness, fatigue, hyperCKemia, and sometimes rhabdomyolysis with myoglobinuria. The correct identifiers are **MONDO:0009501, OMIM:245340, and ORPHA:171690**. This must not be conflated with two allelic *SLC16A1* disorders: MCT1-related ketone-utilization deficiency (OMIM:616095) and promoter-variant exercise-induced hyperinsulinism (OMIM:610021). [7][15][63]

The evidence base is very small and old: the original 1986 patient, an expanded physiologic series of eight males, and molecular study of five cases in 2000. Moreover, the claimed causal missense variants **p.Lys204Glu and p.Gly472Arg showed normal lactate uptake in a later heterologous assay**, and p.Gly472Arg now has benign/VUS submissions in ClinVar. GenCC therefore rates the *SLC16A1*–MONDO:0009501 relationship **Limited**. Accordingly, the disease-level association remains recognized by OMIM and Orphanet, but contemporary variant interpretation should be cautious and should not treat the two historical variants as conclusively pathogenic without patient-specific functional evidence. [128][170][315][372]

**Evidence labels used below**

- **Human clinical:** affected-patient observations or tests.
- **Human genetic:** sequencing/segregation or population data.
- **In vitro:** oocyte, yeast, or cell-culture assays.
- **Model organism:** genetically modified animals.
- **Inferred:** biologically plausible but not demonstrated directly in affected patients.

---

## 1. Disease information

### Definition

This is a dynamic metabolic myopathy in which symptoms occur principally under high glycolytic demand. Orphanet defines it as muscle cramping or stiffness after exercise—especially with heat exposure—with possible post-exertional rhabdomyolysis, myoglobinuria, and elevated serum creatine kinase (CK). [16]

The landmark report described impaired post-exercise decline of skeletal-muscle lactate and defective erythrocyte lactate transport. The authors concluded:

> “The lactate content of the patient's skeletal muscle does not decline normally after exercise and…his red cells are defective in lactate transport.”

**Human clinical evidence:** Fishbein, *Science*, **5 December 1986**, PMID **3775384**, DOI [10.1126/science.3775384](https://doi.org/10.1126/science.3775384). [76]

### Identifiers and names

| Resource | Identifier/name |
|---|---|
| MONDO | **MONDO:0009501** |
| OMIM phenotype | **245340**, erythrocyte lactate transporter defect |
| Causal gene OMIM | ***SLC16A1*: 600682** |
| Orphanet | **ORPHA:171690** |
| MedGen/UMLS | **C1855577** |
| SNOMED CT | **766715000** |
| MeSH Supplementary Concept | **C565449**, introduced 15 November 2011 |
| ICD-10 | **G72.8**, other specified myopathies |
| ICD-11 | No uniquely disease-specific code identified; a broader metabolic/myopathy code must be selected according to local coding rules |
| NCBI Gene | **6566** |
| HGNC | **HGNC:10922** |
| Ensembl | **ENSG00000155380** |
| UniProt | **P53985** |

OMIM maps the phenotype to chromosome **1p13.2**, *SLC16A1*, and autosomal-dominant inheritance. Orphanet supplies ICD-10 G72.8 but no disease-specific prevalence or age-of-onset estimate. [47][63] MeSH lists “Lactate Transporter Defect, Myopathy due to” as an entry term and explicitly notes mutation in *SLC16A1*. [329]

**Synonyms**

- Erythrocyte lactate transporter defect
- Lactate transporter defect, myopathy due to
- Symptomatic deficiency in lactate transport
- SDLT
- MCT1-associated lactate-transport myopathy

### Nature of the data

The report is based predominantly on **individual patients and small research cohorts**, not EHR-scale or registry epidemiology. OMIM, Orphanet, MONDO, MedGen, MeSH, ClinVar and GTR are **aggregated disease-level resources** that curate those few publications. No GeneReviews chapter or disease-specific natural-history registry was found; NCBI explicitly lists GeneReviews as unavailable. [29]

---

## 2. Etiology, risk and protective factors

### Primary cause

The proposed primary cause is a **germline, monoallelic *SLC16A1* defect** reducing MCT1-mediated proton-coupled lactate transport in erythrocytes and skeletal muscle. The molecular paper found three heterozygous subjects with transport rates **40–50% of normal** and two other subjects at **60–65%**. The authors wrote:

> “We presume that these mutations are responsible for their subnormal lactate transport, and hence their muscle injury under environmental stress.”

Merezhinskaya et al., *Muscle & Nerve*, **January 2000**, PMID **10590411**, DOI [10.1002/(SICI)1097-4598(200001)23:1<90::AID-MUS12>3.0.CO;2-M](https://doi.org/10.1002/(SICI)1097-4598(200001)23:1%3C90::AID-MUS12%3E3.0.CO;2-M). [46]

That statement was explicitly a presumption, however, and later functional evidence did not confirm impaired lactate uptake for the historical variants.

### Risk factors

| Factor | Evidence and interpretation |
|---|---|
| Heterozygous historical *SLC16A1* variants | Proposed causal factor, but gene–disease validity is limited and variant-level evidence is disputed. |
| Intense or anaerobic exercise | Principal clinical trigger; increases lactate/H⁺ production and transport demand. |
| Heat exposure | Reported trigger/amplifier in all five subjects in the molecular series; likely increases metabolic and dehydration stress. |
| Repeated strenuous activity | Associated with recurrent cramping and, in two historical patients, progressive stiffness over 5–7 years. |
| Male sex | All reported series subjects were male, but ascertainment was heavily military/exercise based; this does not prove sex-linked susceptibility. |
| Family history | Expected to increase risk under an autosomal-dominant model, but robust multigenerational penetrance data are absent. |
| Dehydration | Plausibly increases rhabdomyolysis/renal risk but has not been tested specifically in this disease. |

The eight-person physiologic series comprised males aged **14–56 years**; all were generally healthy but had elevated CK and partial transport loss of **50–75%**. [87]

### Protective factors

No disease-specific protective allele, modifier, controlled diet study, or preventive drug has been established. Reasonable protective measures are:

- avoiding exhaustive activity and exercise in high heat;
- maintaining hydration and cooling;
- gradual conditioning below the individual symptom threshold;
- stopping activity with cramps, stiffness, marked fatigue, or dark urine;
- prompt rhabdomyolysis management.

These are risk-reduction measures based on triggers and general rhabdomyolysis practice, not trial-proven disease-modifying therapy.

### Gene–environment interaction

This is a strong candidate for a threshold interaction: partial transporter capacity may suffice at rest but become inadequate when **exercise increases lactate/H⁺ flux**, especially with heat or dehydration. Three genetically reported patients had 40–50% normal erythrocyte transport, yet symptoms appeared mainly under environmental stress. [353] Penetrance is therefore likely stress-dependent and incomplete, although it has never been measured formally.

No infectious agent, toxin, radiation, smoking exposure, alcohol effect, occupational exposure, or immune trigger has been demonstrated as causal.

---

## 3. Phenotypes

Reported frequencies below are calculated from the historical eight-person series where possible; denominators may overlap, and the series was not population-based.

| Phenotype/type | Characteristics and frequency | Suggested HPO term | Functional/QOL effect |
|---|---|---|---|
| Exercise-induced muscle cramps — symptom/sign | 3/8 had cramps alone; another 2/8 had cramps plus stiffness, thus approximately **5/8 (62.5%)** if categories were exclusive. Episodic, exertion-related. | **HP:0003710** Exercise-induced muscle cramps | Interrupts strenuous exercise and may impair occupation or athletics. |
| Exercise-induced muscle stiffness — symptom/sign | Reported in 2/8 with progression over 5–7 years; severity variable. | **HP:0008967** | Reduced mobility/performance after exertion. |
| Exercise-induced fatigue/intolerance — symptom | Included in disease ontology annotations; frequency unquantified. | **HP:0009020** Exercise-induced muscle fatigue | Limits sustained or high-intensity activity. |
| Rhabdomyolysis after exercise — acute manifestation | **2/8 (25%)** in the historical series; episodic and potentially severe. | **HP:0009045** Exercise-induced rhabdomyolysis; broader **HP:0003201** | Emergency care may be required; risk of electrolyte or renal complications. |
| Myoglobinuria — laboratory/clinical sign | Occurred with rhabdomyolysis in 2/8. | **HP:0002913** Myoglobinuria; **HP:0003652** if recurrent | Dark urine; potential nephrotoxicity. |
| Elevated circulating CK — laboratory abnormality | Present in the original and expanded cases; exact values and universal frequency not published in accessible summaries. | **HP:0003236** | Objective evidence of muscle injury; persistent hyperCKemia may prompt workup. |
| Delayed intramuscular lactate clearance — functional biomarker | Demonstrated in the original patient and one 2000-series patient. | No highly specific established HPO term; use abnormal lactate metabolism/abnormal exercise physiology | Mechanistically informative; specialized research test. |
| Reduced erythrocyte lactate transport — laboratory abnormality | All five selected 2000 subjects were below the normal 95% envelope; three were at 40–50% and two at 60–65% of mean normal. | Suggested custom phenotype; map to abnormal cellular lactate transport where supported | Biomarker rather than directly perceived impairment. |
| Severe exertional chest-wall pain — symptom | Original patient had three brief episodes over five years, beginning around age 21 and reported at age 26; initially considered cardiac pain. | **HP:0100749** Chest pain may be used, with exertional qualifier | Can mimic cardiac ischemia and provoke emergency evaluation. |
| Minimal/asymptomatic presentation | 1/8 had minimal symptoms despite biochemical deficiency. | **HP:0003828** Variable expressivity, if used at disease level | Supports incomplete penetrance/threshold effects. |
| EMG and biopsy findings | The 2000 cases reportedly had **normal EMG and normal muscle biopsy**, despite MedGen’s generic “EMG abnormality” annotation. | Do not encode “EMG abnormality” for these reported patients; consider normal findings as diagnostic qualifiers | Helps distinguish episodic metabolic dysfunction from structural myopathy. |

The HPO identifiers for exertional cramps, fatigue, stiffness, CK elevation, exercise-induced rhabdomyolysis and myoglobinuria are supported by MedGen/HPO records. [269][275][64][418][422][427]

No validated EQ-5D, SF-36, PROMIS, pain, fatigue, or disease-specific quality-of-life study exists. The likely impact is chiefly avoidance of strenuous activity, reduced athletic/occupational performance, and anxiety or morbidity surrounding rhabdomyolysis.

---

## 4. Genetic and molecular information

### Gene and protein

- **Gene:** *SLC16A1*, HGNC:10922; NCBI Gene 6566; 1p13.2.
- **Protein:** MCT1, UniProt P53985; approximately 500 amino acids and 12 transmembrane helices.
- **Transcript:** MANE Select **NM_003051.4**, protein **NP_003042.3**.
- **Cell-surface trafficking:** requires ancillary proteins basigin/CD147 (**BSG**) or embigin (**EMB**), with preferential binding to BSG. [305]
- **Function:** reversible proton-coupled transport of lactate, pyruvate, acetate, ketone bodies and other monocarboxylates; direction depends on proton and substrate gradients. [121]
- **Localization:** principally plasma membrane, including basal/basolateral and apical membranes in tissue-specific contexts. [300]

### Historically asserted variants and present interpretation

| Variant | Original evidence | Population data/current interpretation | Functional evidence |
|---|---|---|---|
| **NM_003051.4:c.610A>G, p.Lys204Glu; rs80358222; ClinVar 8914** | Heterozygous in original patient; conserved residue in cytoplasmic loop between TM6–7; absent from 90 controls; erythrocyte transport 40–50% normal. | Very rare: approximately 7/595,686 gnomAD exomes and 3/149,202 gnomAD genomes in dbSNP; historical OMIM/ClinVar pathogenic assertion. [92] | *Xenopus* oocytes: lactate uptake **14.6±0.4** versus WT **14.9±1.3 pmol/min/oocyte**, *p*>0.05; normal plasma-membrane localization. |
| **NM_003051.4:c.1414G>A, p.Gly472Arg; rs72552271; ClinVar 8915** | Heterozygous in two unrelated males; nonconserved C-terminal site; absent from 90 controls; transport 40–50% normal. | Too common for a fully penetrant ultrarare AD disorder: ClinVar reports gnomAD exome 0.00012 and other datasets up to 0.00062. Current submissions include **benign**, **VUS**, and an old literature-only pathogenic assertion. [372] | Oocytes: **15.5±1.2** versus WT **14.9±1.3**, *p*>0.05; normal localization. |
| **c.1470T>A, p.Asp490Glu; rs1049434** | Found in two symptomatic subjects with 60–65% transport; subsequently recognized as common. | ClinVar **benign** for MONDO:0009501. [319] | Increased rather than decreased uptake at 100 μM lactate: **20.1±0.7** versus 14.9±1.3; altered kinetic parameters at other concentrations. |

The 2015 experiment, PMID **25371203**, found:

> “None of the mutants showed an effect on the correct localization of the protein in the plasma membrane.”

and no significant uptake reduction for K204E or G472R. [170]

### Interpretation

The historical data support a real **low-lactate-transport phenotype**, but they do not conclusively prove that K204E or G472R caused it. Possible explanations include:

1. a disease mechanism not reproduced by acute oocyte uptake at one substrate concentration;
2. impaired interaction with BSG, regulation, stability or muscle-specific trafficking;
3. another undetected variant or gene;
4. physiological low-transport outliers;
5. ascertainment or linkage error.

The GenCC **Limited** classification is therefore appropriate. [315] No modifier gene, protective allele, reproducible epigenetic signature, recurrent CNV, translocation, aneuploidy, somatic driver, or chromosomal rearrangement has been established.

### Allelic disorders that must remain separate

- **MCT1 deficiency/ketone-utilization disorder, OMIM:616095:** coding loss-of-function variants, monoallelic or biallelic, causing recurrent ketoacidosis. A 2014 study found eight inactivating mutations and genotype correlation with severity, protein level and transport capacity (PMID **25390740**). [357]
- **Exercise-induced hyperinsulinism, OMIM:610021:** activating promoter variants causing inappropriate MCT1 expression in pancreatic β cells and exercise-triggered insulin secretion. This is gain of inappropriate expression, not lactate-transport myopathy. [358]

Variants known only from those conditions should not automatically be annotated as causal for MONDO:0009501.

---

## 5. Environmental and lifestyle information

The principal documented exposures are **strenuous exercise and heat**. Exercise raises glycolytic lactate and proton production, while heat may add dehydration, perfusion and metabolic stress. These exposures trigger manifestations but do not create the underlying Mendelian susceptibility. [353]

There is no evidence that smoking, alcohol, dietary deficiency, pollution, occupational chemicals, radiation, medications, bacterial/viral/fungal/parasitic infection, or autoimmunity initiates this disease. Fasting and infection are important triggers for the distinct *SLC16A1* ketone-utilization disorder, but should not be imported into this myopathy without direct evidence.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **A putative heterozygous *SLC16A1* lesion leads to reduced effective MCT1-dependent lactate/H⁺ transport capacity** in erythrocytes and skeletal muscle; the transport defect is demonstrated, but attribution to the historical variants is uncertain.
2. **Reduced transport capacity leads to delayed transmembrane lactate/H⁺ movement during high glycolytic demand**, demonstrated by abnormal erythrocyte clearance and delayed post-exercise muscle-lactate decline.
3. **Intense exercise, especially with heat, leads to production of lactate and H⁺ faster than residual transport can accommodate**, a strongly supported physiological inference.
4. **This mismatch is inferred to result in intracellular lactate/H⁺ accumulation and reduced pH homeostasis** in active myofibers.
5. **Acidic/metabolic stress is inferred to cause painful cramps, stiffness, fatigue and impaired extreme performance.**
6. **If stress exceeds cellular tolerance, it results in sarcolemmal injury or myofiber necrosis/rhabdomyolysis**, releasing CK and myoglobin.
7. **Released myoglobin leads to myoglobinuria and may branch to renal tubular injury/acute kidney injury**, although kidney failure has not been documented specifically in the published MONDO:0009501 patients.
8. **A compensatory branch may lead to altered NAD⁺/SIRT1/PGC-1α signaling, mitochondrial biogenesis and oxidative-fiber remodeling**, demonstrated in muscle-specific mouse knockout but not in affected humans.

### Transporter-level mechanism

MCT1 is a reversible H⁺/monocarboxylate cotransporter. A 2023 mechanistic study in transporter-deficient yeast identified **Lys38, Asp309 and Arg313** as key residues. Its model is:

1. protonation of Lys38 attracts lactate;
2. lactate accepts the proton;
3. proton transfer to Asp309 breaks the Asp309–Arg313 salt bridge;
4. MCT1 switches to an inward-open state and releases lactate/H⁺.

The authors concluded:

> “Our experimental data provide evidence for the bound substrate itself to accept and shuttle a proton from Lys 38 to Asp 309 initiating transport.”

Schumann et al., *PNAS Nexus*, **18 January 2023**, PMID **36874278**, DOI [10.1093/pnasnexus/pgad007](https://doi.org/10.1093/pnasnexus/pgad007). This is **in vitro yeast evidence**, not patient-variant testing. [111]

### Metabolic and cellular consequences

The proximal abnormality is transport, not a glycolytic enzyme deficiency. Relevant processes include:

- plasma-membrane lactate/H⁺ symport;
- intracellular pH homeostasis;
- lactate shuttle between glycolytic and oxidative myofibers;
- conversion of lactate to pyruvate by LDH;
- TCA-cycle substrate supply;
- NAD⁺/NADH balance;
- mitochondrial biogenesis and oxidative phosphorylation.

A 2024 muscle-specific *Slc16a1* knockout study found that circulating lactate contributed approximately **50% of intramuscular lactate** in quadriceps, tibialis anterior and gastrocnemius and approximately **40% in soleus;** traced intramuscular malate was reported as derived exclusively from circulating lactate under that protocol. The knockout increased intracellular lactate, oxidative fibers, mitochondrial proteins and treadmill endurance but reduced maximal grip force. [213]

The authors wrote:

> “MCT1-mediated lactate shuttle has an active role in promoting mitochondrial biogenesis and TCA flux.”

Zhang et al., *Science Advances*, **26 June 2024**, PMID **38924407**, DOI [10.1126/sciadv.adn4508](https://doi.org/10.1126/sciadv.adn4508). This is **male-mouse and C2C12 evidence** and cannot be assumed to reproduce human episodic rhabdomyolysis.

### Immune, tissue-damage and omics findings

- No primary autoimmunity, immunodeficiency or chronic inflammatory mechanism is known.
- Oxidative stress was not increased in the 2024 muscle-knockout study.
- Human patient transcriptomics, proteomics, metabolomics, lipidomics, single-cell, spatial-transcriptomic and multi-omic studies are unavailable.
- Mouse gastrocnemius RNA-seq showed enrichment of oxidative phosphorylation, citrate-cycle, pyruvate-metabolism, HIF-1 and mitochondrial-organization programs; data accession **PRJNA1013718**. [213]
- No disease-specific CRISPR screen, iPSC-derived muscle model or organoid has validated the historical variants.

### Suggested ontology terms

**GO biological process/function**

- GO:0035879 plasma membrane lactate transport
- GO:0055085 transmembrane transport
- GO:0006089 lactate metabolic process
- GO:0006099 tricarboxylic acid cycle
- GO:0006119 oxidative phosphorylation
- GO:0051453 regulation of intracellular pH
- GO:0006835 dicarboxylic acid transport, where appropriate
- GO:0022857 transmembrane transporter activity
- GO:0015129 lactate transmembrane transporter activity, subject to current GO validation

**GO cellular component**

- GO:0005886 plasma membrane
- GO:0005743 mitochondrial inner membrane only where supported by the experimental context
- GO:0005739 mitochondrion

**Cell Ontology**

- CL:0000188 cell of skeletal muscle
- CL:0000232 erythrocyte
- More specific slow/fast skeletal-muscle fiber terms may be added if supported by the ontology release.

---

## 7. Anatomical structures affected

| Level | Structure and ontology suggestion | Evidence |
|---|---|---|
| Primary organ | Skeletal muscle organ — **UBERON:0014892** | Exercise-induced symptoms and muscle injury. |
| Primary tissue | Skeletal muscle tissue — **UBERON:0001134** | MCT1 is present in skeletal muscle; delayed lactate decline demonstrated. |
| Cell | Skeletal myofiber — **CL:0000188** | Principal symptomatic cell population. |
| Cell | Erythrocyte — **CL:0000232** | Readily assayed transport defect and historical disease name. |
| Fiber subtype | Oxidative type I/IIA/IIX fibers; fast tissue **UBERON:0006908** where applicable | Mouse data show MCT1 enrichment in oxidative/non-IIB fibers. |
| Subcellular | Plasma membrane — **GO:0005886** | Primary established compartment. |
| Possible secondary organ | Kidney | At risk during myoglobinuric rhabdomyolysis, but disease-specific renal injury has not been reported. |
| Chest-wall site | Thoracic skeletal musculature | Original patient’s exertional chest pain was attributed to chest-wall myopathy. |

The disorder is systemic rather than lateralized; no consistent unilateral, asymmetric, cardiac, respiratory, bulbar or CNS muscle involvement is documented. Although MCT1 is widely expressed, the OMIM:245340 phenotype is predominantly skeletal-muscle/erythrocyte based.

---

## 8. Temporal development

- **Onset:** incompletely defined. The original patient had episodes during the five years preceding age 26, suggesting onset around 21. The expanded cohort ranged from 14 to 56 years, but those are ages at ascertainment rather than onset. [87]
- **Pattern:** episodic and acute after exertion; otherwise patients may appear healthy.
- **Progression:** not inherently proven progressive. Two of eight developed progressive stiffness over 5–7 years, while one had minimal symptoms.
- **Duration:** presumed lifelong genetic susceptibility.
- **Remission:** symptoms and CK/rhabdomyolysis can resolve after rest and acute care, but the transport phenotype is presumed persistent.
- **Critical period:** high-intensity activity and heat exposure; intervention is most useful before or at the earliest symptoms of muscle injury.
- No validated staging system, longitudinal progression rate, or age-dependent penetrance curve exists.

---

## 9. Inheritance and population characteristics

### Inheritance

OMIM and Orphanet classify the disease as **autosomal dominant**, based on heterozygous findings in three molecularly reported patients. [47][63]

However:

- formal penetrance is unknown;
- expressivity is variable, ranging from minimal symptoms to rhabdomyolysis;
- no genetic anticipation is expected or reported;
- no germline mosaicism, founder variant, consanguinity effect or recurrent de novo rate is known;
- no carrier frequency can be validly calculated because the causal status of the historical variants is unsettled.

### Epidemiology

No reliable prevalence or incidence exists. Orphanet leaves both prevalence and age of onset blank. [345] The published clinical base includes:

- one original patient;
- eight physiologically defined males, probably overlapping the original case;
- five molecular-study subjects, again including the original patient;
- only three with the two historically asserted missense variants.

Thus, these should not be summed as 14 independent genetically confirmed cases.

No ethnic, geographic or founder enrichment has been established. All eight historical physiologic subjects were male, but this is likely ascertainment bias rather than a true male-limited trait. No sex-ratio estimate is defensible.

---

## 10. Diagnostics

### Recommended diagnostic strategy

1. **Recognize the phenotype:** recurrent cramps, stiffness, fatigue, chest-wall pain, CK elevation, dark urine or rhabdomyolysis after intense exercise/heat.
2. **During an attack:** CK, electrolytes, creatinine/eGFR, urinalysis, urine/plasma myoglobin, AST/ALT, blood gas where severe, lactate and pyruvate.
3. **Between attacks:** repeat CK; renal, thyroid and hepatic studies; plasma acylcarnitines, amino acids and urine organic acids to investigate alternative metabolic myopathies.
4. **Genetic testing first:** a comprehensive rhabdomyolysis/metabolic-myopathy NGS panel including *SLC16A1*, with copy-number analysis where validated; WES/WGS if negative.
5. **Phenotype/variant confirmation:** segregation testing and, where available, erythrocyte lactate-transport studies.
6. **Ancillary testing:** nonischemic forearm or exercise testing, EMG, muscle MRI/MRS and delayed biopsy only when genetics/biochemistry remain inconclusive.

Current rhabdomyolysis guidance supports genomic testing for recurrent episodes, unexplained very high CK, persistent hyperCKemia, family history or longstanding exercise intolerance. [255] GTR lists **22 clinical tests** under this condition, including single-gene and metabolic-myopathy panel testing. [237]

### Disease-specific and general tests

| Test | Expected/possible finding | Limitations |
|---|---|---|
| Serum CK | Elevated at baseline or after exertion | Nonspecific. |
| Urine myoglobin | Positive during rhabdomyolysis | Short detection window. |
| Renal/electrolyte profile | Usually normal between events; may become abnormal in severe rhabdomyolysis | No disease-specific sensitivity data. |
| Blood lactate | May be abnormal after exercise | Resting lactate may be normal; collection artifacts common. |
| Erythrocyte lactate clearance assay | Approximately 40–50% of normal in three historical genetic cases | Specialized, nonstandardized and rarely clinically available. |
| Exercise/ischemic forearm testing | Delayed muscle-lactate decline in reported case(s) | Ischemic protocols carry discomfort/rhabdomyolysis risk; modern nonischemic testing is preferred. |
| EMG | Normal in molecularly reported subjects | Normal result does not exclude disease. |
| Muscle biopsy | Normal in reported subjects | Low yield outside differential diagnosis; avoid during acute necrosis. |
| Muscle MRS | Potentially measures delayed lactate handling | Research/specialist use; no validated cutoff. |

### Genetic-test utility

- **Single-gene sequencing:** suitable when phenotype and transport studies strongly implicate MCT1.
- **Panel:** preferred in most patients because differential diagnosis is broad and historical *SLC16A1* pathogenicity is uncertain. GTR lists a rhabdomyolysis/metabolic-myopathy NGS panel containing *SLC16A1*. [233]
- **WES/WGS:** useful when panel testing is negative, to find alternative genes or regulatory/structural variants.
- **RNA sequencing:** potentially useful for splice variants, but no disease-specific validation.
- **CMA/karyotype/FISH:** low expected yield unless syndromic CNV features are present.
- **mtDNA testing:** indicated only when mitochondrial features suggest a mitochondrial differential.
- **Repeat-expansion testing:** not relevant to this specific mechanism unless another diagnosis is suspected.

A historical K204E or G472R finding should be interpreted under current ACMG/AMP criteria, incorporating frequency, segregation, phenotype specificity and functional testing—not simply inherited from old OMIM labels.

### Differential diagnosis

| Differential | Distinguishing clues/tests |
|---|---|
| McArdle disease, *PYGM* | Early exercise cramps, second-wind phenomenon; absent lactate rise on exercise testing. |
| Tarui disease, *PFKM* | Carbohydrate worsens exercise tolerance; hemolysis may occur. |
| LDHA deficiency | Exertional cramps/myoglobinuria and abnormal lactate/pyruvate conversion. |
| CPT II deficiency, *CPT2* | Prolonged exercise, fasting, illness or cold triggers; abnormal acylcarnitines may help. |
| VLCAD/other fatty-acid oxidation disorders | Endurance/fasting/illness triggers; acylcarnitine and molecular diagnosis. |
| RYR1-related exertional rhabdomyolysis/malignant hyperthermia | Heat/exercise trigger, anesthesia susceptibility; calcium-release mechanism. |
| LPIN1-related rhabdomyolysis | Often severe childhood attacks with illness/fasting. |
| Mitochondrial myopathy | Multisystem findings, lactate elevation, mtDNA/nuclear-gene defects and biopsy abnormalities. |
| *SLC16A1* ketone-utilization deficiency | Recurrent ketoacidosis, usually childhood/fasting/infection related rather than isolated exertional myopathy. |
| Exercise-induced hyperinsulinism | Exercise-associated hypoglycemia with inappropriate insulin, caused by regulatory gain-of-expression variants. |
| Acquired rhabdomyolysis | Drugs/toxins, infection, extreme unaccustomed exercise, endocrine/electrolyte causes. |

No standardized diagnostic criteria or validated screening biomarker exists.

---

## 11. Outcome and prognosis

No 5- or 10-year survival, mortality rate, life-expectancy estimate, disability-adjusted life-year analysis or validated prognostic model is available.

The limited case descriptions suggest that many affected people are otherwise healthy and symptoms are primarily episodic, but outcomes range from minimal impairment to recurrent rhabdomyolysis and progressive stiffness. The main foreseeable serious complication is acute kidney injury, hyperkalemia or other systemic complications of rhabdomyolysis; this is a general mechanistic risk rather than a documented frequency in this exact disease.

Potential prognostic indicators—none validated—include:

- residual erythrocyte transport activity;
- severity/frequency of prior rhabdomyolysis;
- baseline and post-exercise CK;
- ability to avoid triggers;
- renal injury during previous events;
- variant function and inheritance;
- coexisting metabolic or neuromuscular disease.

Recovery from an isolated attack should be possible with rest and acute care, but the inherited susceptibility remains. No quality-of-life instrument or long-term functional cohort has been reported.

---

## 12. Treatment

### Disease-specific evidence

There is **no approved pharmacologic, gene, RNA, cell, surgical or targeted therapy** for MONDO:0009501, and no disease-specific interventional trial or response-rate dataset was identified. No pharmacogenomic guidance exists.

### Practical management

| Intervention | Role and evidence | Suggested NCIT intervention term |
|---|---|---|
| Avoid exhaustive exercise/heat | Primary long-term trigger avoidance; based on human trigger observations | Exercise Modification; Risk Reduction |
| Individualized graded activity | Maintain conditioning below symptom threshold; extrapolated from metabolic-myopathy care | Physical Therapy; Exercise Therapy |
| Hydration and cooling | Reduce heat/dehydration burden and renal risk | Supportive Care; Hydration |
| Stop activity at warning symptoms | Cramps, stiffness, unusual fatigue, pain or dark urine should prompt rest and assessment | Patient Education |
| Acute IV isotonic fluids | Standard management for clinically significant rhabdomyolysis, tailored to renal/cardiac status | Intravenous Fluid Therapy |
| Electrolyte and renal monitoring | Detect hyperkalemia and acute kidney injury | Laboratory Monitoring |
| Nephrology/critical-care support | Severe rhabdomyolysis, oliguria, electrolyte disturbance; dialysis if conventionally indicated | Renal Replacement Therapy |
| Physical/occupational therapy | For persistent stiffness, deconditioning or work adaptation | Physical Therapy; Occupational Therapy |
| Genetic counseling | Explain uncertain evidence, recurrence risks and allelic disorders | Genetic Counseling |

General metabolic-myopathy guidance recommends careful progressive exercise and symptom-triggered intensity reduction, while rhabdomyolysis is managed with fluids, electrolyte prevention/correction and dialysis when necessary. [239][240]

**Not established:** bicarbonate supplementation, dichloroacetate, lactate-lowering drugs, antioxidants, carnitine, creatine, ketogenic diets or MCT1 inhibitors. MCT1 inhibition would mechanistically reduce transport further and should not be used experimentally outside an approved protocol. Conversely, the 2024 mouse study’s enhanced endurance after muscle-specific knockout is compensatory model biology, not evidence that inhibiting MCT1 is safe in patients.

---

## 13. Prevention

### Primary prevention

Because this is Mendelian, no vaccine or population lifestyle intervention prevents the genotype. Reproductive options after a convincingly pathogenic familial variant is established include:

- preconception genetic counseling;
- partner/family testing where clinically appropriate;
- prenatal diagnosis;
- preimplantation genetic testing.

These options require special caution because variant pathogenicity and penetrance for MONDO:0009501 are uncertain.

### Secondary prevention

- Cascade testing may be offered only for a well-supported familial variant.
- Baseline CK and counseling in at-risk relatives may be reasonable.
- No newborn or population carrier-screening program is indicated.
- Asymptomatic variant carriers should not be labeled affected on the basis of p.Gly472Arg alone given its current benign/VUS evidence.

### Tertiary prevention

- avoid known exercise/heat thresholds;
- remain well hydrated;
- use gradual warm-up and conditioning;
- provide an emergency plan for dark urine, severe pain, weakness or reduced urine output;
- check renal function and electrolytes after significant attacks;
- review drugs and illnesses that independently increase rhabdomyolysis risk.

There is no applicable immunization, infectious prophylaxis, sanitation or vector-control intervention.

---

## 14. Other species and natural disease

No confirmed naturally occurring veterinary equivalent of human MONDO:0009501 was found.

| Species | Taxon/gene information | Natural-disease evidence |
|---|---|---|
| Human, *Homo sapiens* | Taxon 9606; *SLC16A1* Gene 6566 | Target disease. |
| Mouse, *Mus musculus* | Taxon 10090; *Slc16a1* Gene **20501**, MGI:106013 | Engineered models; no established natural homologous myopathy. [465] |
| Rat, *Rattus norvegicus* | Taxon 10116; *Slc16a1* Gene **25027** | Ortholog and physiological studies; no confirmed natural disease. [476] |
| Horse, *Equus caballus* | Taxon 9796; *SLC16A1* Gene **100009694** | MCT1 polymorphisms examined in exercise-associated myopathy, but variants were **not associated** with erythrocyte transport activity or myopathy. [183][476] |
| Zebrafish, *Danio rerio* | Taxon 7955; duplicated orthologs including *slc16a1a* Gene **100534752** and another paralog | Comparative/model potential; no confirmed natural equivalent. [463][474] |

In seven horses with post-exercise myopathy and three controls, MCT1/CD147 coding polymorphisms did not correlate with lactate transport or disease, arguing against a demonstrated equine natural model. [183] The disorder is noninfectious and has no zoonotic or cross-species transmission potential.

---

## 15. Model organisms and experimental systems

| Model | Main findings/applications | Limitations |
|---|---|---|
| Global *Slc16a1* null mouse | Homozygous knockout is embryonically lethal, showing essential developmental function. | Does not model viable heterozygous human exertional disease. |
| *Slc16a1*+/− mouse | Develops normally; on high-fat diet had 24.8% lower body weight after 16 weeks, less insulin resistance and no hepatic steatosis. PMID **24367518**. [496] | Primarily systemic metabolic/obesity model; no reported recapitulation of human rhabdomyolysis. |
| Skeletal-muscle-specific *Slc16a1* knockout mouse | Increased intramuscular lactate, oxidative-fiber shift, mitochondrial biogenesis and treadmill endurance; reduced maximal grip; NAD⁺–SIRT1–PGC-1α adaptation. PMID **38924407**. [213] | Complete tissue-specific deletion in young male mice; compensatory adaptation differs from historical heterozygous human variants. |
| C2C12 myotubes with knockdown or AZD3965 | Increased intracellular lactate, glycolytic/TCA flux, NAD⁺, SIRT1 activity and PGC-1α stability. | Immortalized mouse cells; pharmacologic inhibition is not equivalent to patient disease. |
| *Xenopus laevis* oocytes expressing K204E/G472R | Both variants localized normally and had WT-like uptake at 100 μM lactate. PMID **25371203**. [128] | Single concentration, nonmuscle membrane context; does not assess chronic regulation or BSG-dependent human-muscle physiology comprehensively. |
| Transporter-deficient *Saccharomyces cerevisiae* expressing human MCT1 | Resolved proton/lactate mechanism involving Lys38, Asp309 and Arg313. PMID **36874278**. [111] | Mechanistic reconstitution, not a disease-phenotype model. |
| Human erythrocytes and exercised muscle | Directly demonstrated impaired transport and delayed lactate clearance in patients. PMIDs **3775384**, **10590411**. | Very small cohorts; historical assays not widely standardized. |

The best future disease model would be a **patient-derived iPSC skeletal-myotube system** or CRISPR knock-in model containing K204E/G472R alongside corrected isogenic controls, tested under heat and high-glycolytic demand with BSG expression, lactate/H⁺ flux, intracellular pH, membrane localization and myofiber-injury endpoints. This has not yet been reported.

---

# Recent developments and expert interpretation

Although no 2023–2024 study expanded the human MONDO:0009501 cohort, recent work materially changes mechanistic interpretation:

1. **2023 transport mechanism:** biochemical reconstitution demonstrated substrate-mediated proton relay through Lys38–lactate–Asp309, refining how MCT1 couples lactate and H⁺ transport. [111]
2. **2024 muscle physiology:** isotope tracing, transcriptomics and metabolomics in mice showed that MCT1-dependent lactate flux influences mitochondrial biogenesis, fiber type and TCA-cycle fuel selection. [213]
3. **Modern variant reassessment:** p.Gly472Arg has a current benign ClinVar submission, appreciable population frequency and no demonstrated reduction in oocyte lactate uptake. [372]
4. **Gene–disease validity:** GenCC rates the exact *SLC16A1*–MONDO:0009501 relationship **Limited**, reflecting the tiny historical cohort and contradictory functional evidence. [315]

The most defensible current conclusion is therefore: **a clinically observed partial lactate-transport phenotype exists, and MCT1 is biologically relevant, but the causal certainty of the historically reported missense variants—and hence the molecular boundaries of MONDO:0009501—requires re-evaluation using contemporary genomics and functional assays.**

## Key primary literature

| Publication date | Citation and URL | Evidence |
|---|---|---|
| **5 Dec 1986** | Fishbein WN. *Lactate transporter defect: a new disease of muscle.* Science 234:1254–1256. PMID **3775384**. [PubMed](https://pubmed.ncbi.nlm.nih.gov/3775384/) | Original human clinical case and transport phenotype. |
| **1988** | Fishbein et al. *Clinical assay of the human erythrocyte lactate transporter I/II.* PMIDs **3395513**, **3395514** | Assay development and normal reference data. |
| **Jan 2000** | Merezhinskaya et al. *Mutations in MCT1 cDNA in patients with symptomatic deficiency in lactate transport.* PMID **10590411**. [PubMed](https://pubmed.ncbi.nlm.nih.gov/10590411/) | Five human cases; historical variant association. |
| **4 Nov 2014 / 23 Jan 2015 issue** | Sasaki et al. *Functional characterization of 5-oxoproline transport via SLC16A1/MCT1.* PMID **25371203**. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4303682/) | Oocyte functional testing contradicting reduced transport for K204E/G472R. |
| **18 Jan 2023** | Schumann et al. *Human monocarboxylate transporters accept and relay protons via the bound substrate.* PMID **36874278**. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9982067/) | Detailed MCT1 proton/lactate transport mechanism. |
| **26 Jun 2024** | Zhang et al. *Lactate transported by MCT1 plays an active role in promoting mitochondrial biogenesis and enhancing TCA flux in skeletal muscle.* PMID **38924407**. [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11204292/) | Mouse muscle knockout, RNA-seq and isotope-tracing study. |

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 1 |
| References weighed for topical relevance | 19 |
| On topic | 6 |
| Off topic | 0 |

19 of 20 references resolved; the rest could not be looked up either way.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 7 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009501` (12 mentions) - the report calls it "MONDO"; MONDO calls it **metabolic myopathy due to lactate transporter defect**
- `HP:0003236` (1 mention) - the report calls it "Present in the original and expanded cases; exact values and universal frequency not published in accessible summaries"; HP calls it **Elevated circulating creatine kinase activity**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`, `MGI`, `RGD`.