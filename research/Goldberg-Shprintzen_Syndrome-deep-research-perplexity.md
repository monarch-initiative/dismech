---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-09T20:55:28.555057'
end_time: '2026-10-09T20:59:43.618672'
duration_seconds: 255.06
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Goldberg-Shprintzen Syndrome
  mondo_id: MONDO:0012280
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
citation_count: 61
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 4
  off_topic: 2
  off_topic_references:
  - PMID:33252036
  - PMC:PMC12905500
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 36
  verified: 25
  not_found: 0
  obsolete: 1
  unverifiable: 10
  confabulation_rate: 0.0
  obsolete_terms:
  - term_id: CL:0002609
    ontology_label: obsolete neuron of cerebral cortex
    replaced_by: CL:0010012
  unresolvable_prefixes:
  - ORPHA
  - Gene
  - OMIM
  - Taxon
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Goldberg-Shprintzen Syndrome
- **MONDO ID:** MONDO:0012280 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Goldberg-Shprintzen Syndrome** covering all of the
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

# Goldberg–Shprintzen syndrome: disease-characteristics research report

**Goldberg–Shprintzen syndrome (GOSHS; MONDO:0012280) is a rare, autosomal-recessive neurodevelopmental disorder caused by biallelic loss-of-function variants in *KIFBP*.** Its defining clinical pattern combines microcephaly, developmental impairment and characteristic facial features; many, but not all, affected people also have Hirschsprung disease and malformations of cerebral cortical development. It is **not** Shprintzen–Goldberg syndrome, the distinct *SKI*-associated condition. [3][23][51]

**Evidence boundary.** This is an aggregated, disease-level synthesis of published patients, experimental studies, and curated resources—not an analysis of individual electronic health records. The small, inconsistently ascertained case literature supports clinical descriptions but seldom supports population-wide frequencies, treatment-response rates, or survival estimates. In particular, Orphanet’s description says 24 published cases, whereas a 2020 paper identified **37 previously reported people and added nine**; those counts should not be combined as if they were contemporaneous estimates. [1][37]

## 1. Disease information and identifiers

| Identifier or name | Value and interpretation |
|---|---|
| MONDO | **MONDO:0012280**. [3] |
| OMIM phenotype | **609460**, Goldberg–Shprintzen megacolon syndrome. The associated *KIFBP* gene entry is **OMIM 609367**. [51][88] |
| Orphanet | **ORPHA:66629**. [1] |
| MeSH | **C537279**, as cross-referenced by Orphanet. [1] |
| ICD-10; ICD-11 | **Q87.8; LD2F.1Y**, respectively, as listed by Orphanet; these are classification mappings rather than GOSHS-specific molecular diagnoses. [1] |
| UMLS/MedGen; SNOMED CT | **C1836123 / MedGen 332131; SNOMED CT 717822006**. [3] |
| Synonyms | Goldberg–Shprintzen megacolon syndrome; megacolon–microcephaly syndrome; GOSHS. [1][3] |
| Crucial disambiguation | **Shprintzen–Goldberg syndrome** is *SKI*-associated and has a different OMIM/Orphanet entry; its craniosynostosis/connective-tissue phenotype should **not** be imported into this entry. [21][32] |

The original molecular study, published **9 May 2005**, linked homozygous *KIAA1279*—the former name for *KIFBP*—nonsense variants to central and enteric nervous-system malformations. Its abstract states: “homozygous nonsense mutations in KIAA1279 … underlie this syndromic form of Hirschsprung disease and generalized polymicrogyria.” [PMID: **15883926**](https://pubmed.ncbi.nlm.nih.gov/15883926/). [151]

## 2. Etiology: causal, risk, protective, and environmental factors

**Established cause:** pathogenic variants affecting both germline *KIFBP* alleles, usually nonsense, frameshift, splice-disrupting or exon-deletion variants; some missense variants reduce protein abundance. A 2020 human-patient and transfected-cell study found that truncating variants produced no detectable KIFBP protein, while the tested missense variants reduced expression. The authors concluded: “reduced, as well as lack of KIFBP expression can lead to GOSHS.” Published **16 September 2020**; [PMID: **32939943**](https://pubmed.ncbi.nlm.nih.gov/32939943/). [37][154]

**Risk and variation:** having two disease-causing alleles is the established genetic risk; family history and consanguinity can increase the chance that both parents transmit the same rare recessive allele. Hirschsprung disease is variably expressed even among siblings carrying the same *KIFBP* variant. Proposed genetic or stochastic modifiers remain **unconfirmed**: in a small analysis, selected common *RET*, *NRG1*, and *SEMA3A* SNPs did not significantly explain Hirschsprung status (*p*=0.526). A mouse study found a *Kif1bp–Ret* interaction affecting **vagal stomach innervation**, but did **not** demonstrate an interaction explaining delayed enteric neural-crest migration. [37][38][151]

**Not established:** no protective allele, protective diet, toxin, lifestyle exposure, pathogen, or reproducible gene–environment interaction has been identified for GOSHS onset. Nutrition, infection prevention, and bowel care can influence **complications**; they do not correct the inherited cause. No GOSHS-specific epigenetic mechanism has been demonstrated. [37][1]

## 3. Phenotypes

The table distinguishes **cohort observations** from **resource descriptions**. The strongest numerical disease-specific estimate is Hirschsprung disease in **24/34 people (~71%)** in the 2020 literature-assembled dataset; this is not a population prevalence. Orphanet describes cerebral MRI abnormalities in **about half** of patients. Its HPO sign page places terms in frequency groupings, but its initially listed signs have no visible frequency-group heading in the retrieved page; they should **not** be interpreted as 100% penetrant. [37][1][226]

| Phenotype type | Phenotype and suggested HPO term | Onset, severity, course, frequency, and functional impact |
|---|---|---|
| Physical manifestation | **Microcephaly — HP:0000252** | Congenital or early infancy; prominent but severity varies. Small brain/head size accompanies developmental disability; an exact unbiased frequency is unavailable. [1][37][226] |
| Gastrointestinal sign/pathology | **Aganglionic megacolon / Hirschsprung disease — HP:0002251** | Congenital; **24/34 (~71%)** in a published-case compilation. Presentation ranges from constipation to neonatal obstruction; untreated obstruction can threaten life and bowel function. [37][1][226] |
| Developmental/behavioral manifestation | **Global developmental delay — HP:0001263** | Recognized in infancy or childhood; often substantial, particularly for expressive language. Affects communication, schooling, and independence; no validated syndrome-wide percentage or quality-of-life score. [1][141] |
| Neurocognitive manifestation | **Intellectual disability — HP:0001249** | Childhood recognition; commonly moderate to severe in clinical descriptions, with variable expressivity. Long-term support needs vary. [1][226] |
| Neuromuscular sign | **Hypotonia — HP:0001252** | Usually early-life; Orphanet’s HPO listing calls it *very frequent*, but no reliable patient denominator is supplied. Can compound motor and feeding difficulties. [1][226] |
| Brain-imaging sign | **Polymicrogyria — HP:0002126** | Congenital cortical malformation, sometimes focal or generalized; variable among families. Potential developmental and seizure burden should be assessed individually. [1][185] |
| Brain-imaging sign | **Pachygyria — HP:0001302** | Congenital; Orphanet HPO listing calls it *frequent*. An imaging finding, not a separate disease stage. [226][37] |
| Brain-imaging sign | **Corpus-callosum hypoplasia — HP:0002079** | Congenital; *frequent* in Orphanet’s HPO listing. Possible contribution to impaired interhemispheric connectivity is mechanistic inference. [226][151] |
| Brain-imaging sign | **Ventriculomegaly — HP:0002119** | Prenatally or postnatally detectable; *frequent* in Orphanet’s HPO listing; clinical effect depends on context. [226][136] |
| Neurological sign | **Seizures — HP:0001250** | Variable onset and occurrence; *frequent* in Orphanet’s HPO listing, but present in only some individually described patients. Episode severity and burden vary. [226][37] |
| Peripheral-neurological sign | **Peripheral, including axonal, neuropathy** | Childhood or later detection; sensory/motor impact varies. Some reported patients had mixed axonal/demyelinating findings; no dependable syndrome-wide frequency or single specific HPO subtype is established here. [37][145] |
| Craniofacial signs | **Ptosis — HP:0000508; hypertelorism — HP:0000316; wide nasal bridge — HP:0000431; pointed chin — HP:0000307** | Typically apparent at birth, sometimes clearer with age. Features aid recognition but are not independently diagnostic; ptosis may affect vision and warrants eye assessment. [1][226] |
| Eye manifestations | **Iris coloboma — HP:0000612; hypermetropia, megalocornea, corneal disease** | Variable; vision or corneal symptoms may require treatment. Iris coloboma is listed as *very frequent* by Orphanet HPO, while individual clinical series differ in ascertainment. [226][1][37] |
| Growth/skeletal findings | **Short stature — HP:0004322; scoliosis and digital anomalies** | Growth concerns emerge in childhood; highly variable. Scoliosis or limb findings may affect mobility. [1][37][226] |
| Cardiovascular/urogenital findings | **Ventricular septal defect; aortic regurgitation; vesicoureteral reflux; genital or renal anomalies** | Congenital and **variable**, not defining findings. Their presence determines organ-specific monitoring and intervention. [1][3] |
| Newly reported adult manifestations | **Progressive ataxia, ophthalmoparesis, hypogonadotropic hypogonadism** | Reported in **four affected siblings** with a homozygous *KIFBP* variant; early-adulthood-onset progression was described for the first time. These findings must not be treated as established frequencies or the universal course. Published **February 2024**, online **30 October 2023**; [PMID: **37903629**](https://pubmed.ncbi.nlm.nih.gov/37903629/). [24] |

**Quality-of-life evidence:** no GOSHS-specific EQ-5D, SF-36, or PROMIS cohort estimate was identified in these sources. Effects on continence, communication, mobility, learning, and caregiver burden are clinically plausible and individually important, but should not be presented as measured GOSHS outcomes. Orphanet explicitly recommends individualized developmental assessment to improve quality of life. [1][125]

## 4. Genetic and molecular information

| Gene or variant class | Evidence and knowledge-base interpretation |
|---|---|
| **Causal gene:** *KIFBP* (**HGNC:23419; NCBI Gene:26128; OMIM:609367**), 10q22.1 | Also called *KIAA1279* or *KIF1BP* in older papers. The associated phenotype is OMIM:609460. Use current approved symbol ***KIFBP***, not *SKI*. [82][86][136] |
| **Germline truncating variants** | Established recessive loss-of-function class; examples include **c.268C>T (p.Arg90Ter)**, **c.250G>T (p.Glu84Ter)**, **c.604_605delAG (p.Arg202IlefsTer2)**, and exon deletions. The 2020 study reports its truncating patient variants as pathogenic by ACMG assessment. These are **germline**, not tumor-somatic drivers. [37][50] |
| **Functionally investigated missense variants** | **c.565C>T (p.Pro189Ser)** was reported homozygous and *pathogenic* in the study, absent from its cited gnomAD exome and genome samples (**AC 0** in each). **c.68A>G (p.Glu23Gly)** and **c.1279A>G (p.Ser427Gly)** occurred together in another patient, reduced expression in transfected cells, but were described as **likely benign by the stated ACMG assessment**; their role must not be upgraded to definitively pathogenic solely from that experiment. Reported 2020 gnomAD exome allele frequencies were **0.001707** and **2.44×10⁻⁵**, respectively—not current universal frequencies. [37] |
| **2024 case-level variants** | An August 2024 case report labeled homozygous **c.1694_1695del (p.Glu565AlafsTer16)** *likely pathogenic*; however, a related exon-7 deletion had been catalogued earlier, so it is not securely a novel recurrent allele. An October 2024 report described homozygous **p.Glu98Ter** but supplied inconsistent notation and lacked parental segregation testing. These reports broaden individual observations, not population estimates. [48][37][47] |
| **Modifiers, epigenetics, chromosomal findings** | No validated GOSHS-specific modifier gene, protective variant, DNA-methylation signature, anticipation mechanism, or characteristic aneuploidy/translocation. **Intragenic exon deletions** are relevant structural *KIFBP* alleles; a chromosome-wide rearrangement is not the established cause. [37][51] |

The 2020 authors found **no clear variant-position/severity correlation** and proposed a KIFBP-expression threshold as one explanation for variable presentation. That proposal is mechanistically plausible, not a validated prognostic biomarker or individual-patient prediction rule. [PMID: **32939943**](https://pubmed.ncbi.nlm.nih.gov/32939943/). [37]

## 5. Environmental information

No environmental toxin, radiation exposure, smoking pattern, diet, occupational exposure, or infectious agent is established as a **cause** of GOSHS. Infections can instead occur **downstream** of complications: a 2024 patient report describes bacteremia during severe bowel/respiratory illness, which does not make the bacterium a cause of the genetic syndrome. Likewise, nutrition and access to surgical care can alter outcomes without changing genotype. No GOSHS-specific CheBI exposure or prophylactic chemical should be annotated as etiologic. [48][1]

## 6. Mechanism and pathophysiology

**Ordered causal chain — demonstrated steps and inferences separated:**

1. **Biallelic germline *KIFBP* loss-of-function leads to absent or reduced KIFBP protein**; this is supported by patient genetics and variant-expression experiments. [37][151]
2. **Altered KIFBP abundance leads to dysregulation of interactions with selected kinesin motors and the actin–microtubule cytoskeleton**; protein interactions and motor inhibition are experimentally demonstrated, but the exact effects of each patient allele in each developing tissue remain inferred. [234][211][234]
3. **Cytoskeletal/motor dysregulation leads to impaired neurite extension, axonal organization, and neuronal migration/survival** in zebrafish and mouse perturbation models; extension of every modeled effect to human tissue is **inferred**. [92][225]
4. **Enteric branch:** impaired development **leads to delayed enteric neural-crest colonization** in knockout mouse embryos; failure to populate the **human distal bowel** is the **inferred species-sensitive step**, resulting in aganglionosis → dysmotility, constipation or obstruction. Mouse and zebrafish bowel can be fully ganglionated at birth despite model defects. [38][151]
5. **Cerebral branch:** impaired neuronal migration, dendritic growth, callosal axon extension, and survival **leads to abnormal cortical organization/connectivity** in models; their contribution to human polymicrogyria, callosal hypoplasia, microcephaly and developmental disability is **inferred**, not proven lesion by lesion. [225]
6. **Possible parallel cerebral branch:** KIFBP depletion **leads to midbody/cytokinesis defects** in cultured dividing cells; reduced neural-progenitor production **may lead to microcephaly**, but that final link remains a **hypothesis**, not a demonstrated GOSHS patient mechanism. [224]

At the protein level, cryo-EM and biochemical work showed that KIFBP can bind and remodel selected kinesin motor heads, obstructing their microtubule-binding surface. This describes **normal KIFBP molecular activity**: loss of an inhibitor can have complex, context-dependent developmental consequences and should not be simplified to “all kinesin transport decreases.” [PMID: **33252036**](https://pubmed.ncbi.nlm.nih.gov/33252036/) (2020); [PMID: **34797717**](https://pubmed.ncbi.nlm.nih.gov/34797717/) (2021). [219][211]

**Experimental detail and annotation candidates:**

| Mechanistic process | Evidence level; cells and candidate ontology terms |
|---|---|
| Neuronal migration and morphogenesis | **Mouse in vivo / cultured neurons:** embryonic cortical *Kbp* shRNA impaired migration; at postnatal day 6, **34.3% ± 4.9%** of labeled cells remained ectopic in white matter, with reduced dendritic and callosal axon growth. Rescue by shRNA-resistant Kbp supported perturbation specificity. Candidate **GO:0001764** neuron migration; **GO:0007409** axonogenesis; **CL:0002609** neuron of cerebral cortex. [PMID: **31736709**](https://pubmed.ncbi.nlm.nih.gov/31736709/) (2019). [225][180][183] |
| Axonal microtubules and enteric development | **Zebrafish mutant / mouse knockout:** axonal microtubule disorganization, reduced outgrowth and later degeneration in fish; delayed **Sox10-positive** enteric neural-crest-cell wavefront in mouse embryos. Candidate **GO:0007017** microtubule-based process; **CL:0002607** enteric neural crest cell. Fish: [PMID: **18192286**](https://pubmed.ncbi.nlm.nih.gov/18192286/) (2008); mouse: [PMID: **29192291**](https://pubmed.ncbi.nlm.nih.gov/29192291/) (2017). [92][151][179] |
| Cytokinesis and possible microcephaly mechanism | **Cultured-cell interaction/knockdown:** KIFBP interacts with CITK, localizes to the midbody and is needed for normal midbody maturation and abscission. Abstract: “cytokinesis failure may contribute to the microcephaly phenotype”—**the authors’ proposed clinical link**. Candidate **GO:0000910** cytokinesis. [PMID: **34100550**](https://pubmed.ncbi.nlm.nih.gov/34100550/) (2021). [224][182] |
| Cell survival | **Mouse cortical-neuron perturbation:** increased cleaved caspase-3 after Kbp knockdown; the initiating cause of apoptosis is unresolved. Candidate **GO:0006915** apoptosis. [PMID: **31736709**](https://pubmed.ncbi.nlm.nih.gov/31736709/). [225][182] |
| Mitochondrial/metabolic hypothesis | **Human fibroblasts:** three reported truncating variants led to transcript decay and protein loss, yet respiratory-chain-complex activity was **normal** and KIFBP did **not** colocalize with mitochondria in control fibroblasts. Consequently, a primary oxidative-phosphorylation deficiency is **not established**. [PMID: **23427148**](https://pubmed.ncbi.nlm.nih.gov/23427148/) (2013). [223] |

**Not established as disease mechanisms:** a GOSHS-specific Wnt/MAPK/mTOR/PI3K-AKT cascade, immune or inflammatory primary lesion, disease-specific metabolomic/lipidomic or epigenomic signature, single-cell or spatial-transcriptomic disease atlas, or validated multi-omics diagnostic profile. Cultured-cell, imaging, proteomic-interaction, and cryo-EM results should not be relabeled as such profiles. [225][224][211]

## 7. Anatomical structures affected

| Level | Structures, localization, and suggested ontology terms |
|---|---|
| Primary organ/system | **Brain and nervous system**—particularly cerebral cortex (**UBERON:0000956**), callosal pathways (**UBERON:0002336**), and peripheral nerves; **distal large intestine/enteric nervous system** when Hirschsprung disease occurs. Suggested cells: cortical neuron **CL:0002609**, enteric neural crest cell **CL:0002607**. [1][151][167][179] |
| Tissue/cell | Cortical neural progenitors and migrating neurons; embryonic enteric neural-crest-derived cells, enteric ganglion cells, and developing autonomic axons. These are developmental populations, not evidence of an acquired inflammatory attack. [225][151] |
| Secondary involvement | Eye/cornea, cardiac structures, kidneys/urinary tract, skeletal tissues, growth, and respiratory health variably; these are **not required** to establish the molecular diagnosis. [1][37] |
| Subcellular | Cytoplasmic microtubules and actin-associated structures, axonal projections, and the **midbody** during cell division. Earlier mitochondrial-localization proposals are not uniformly supported by patient-fibroblast experiments. Appropriate GO cellular-component **labels** include cytoplasm, microtubule and midbody; assign exact accession IDs only after ontology-version validation. [223][224][211] |
| Lateralization | No consistent right-versus-left disease localization is established. Cerebral malformations may be focal or generalized; a 2024 individual had bilaterally asymmetric periventricular volume loss. [1][47] |

## 8. Temporal development

GOSHS begins **prenatally as a developmental disorder**; microcephaly and bowel obstruction may become apparent in the neonatal period, whereas intellectual disability becomes measurable through childhood. Facial differences can become more recognizable with age. The condition is lifelong rather than relapsing–remitting, but **individual manifestations differ**: congenital structural findings are generally persistent; bowel symptoms may improve after treatment; and progressive adult ataxia was newly reported in one family in 2023/2024. There is no validated mild/intermediate/end-stage classification, progression rate, or spontaneous-remission estimate. Prenatal neural and enteric development, neonatal bowel decompression, and early developmental support are the most evident intervention windows. [1][24][125]

## 9. Inheritance and population

| Population or inheritance measure | Best-supported assessment |
|---|---|
| Inheritance; recurrence | **Autosomal recessive.** When both parents are heterozygous carriers of the familial pathogenic variants, each pregnancy has **25% affected, 50% carrier, 25% neither** probabilities under the standard Mendelian model. [1][151] |
| Penetrance and expressivity | Penetrance of the **entire molecular syndrome** is not precisely estimated. Hirschsprung disease has **incomplete/variable expression**: **24/34** reported individuals in the 2020 compilation had it, including families discordant for the bowel phenotype. Do not equate its penetrance with syndrome penetrance. [37] |
| Prevalence | Orphanet estimates **<1 per 1,000,000**, equivalent to **<0.1 per 100,000**; ascertainment is uncertain. [1] |
| Incidence; carrier frequency; sex ratio | **No reliable disease-specific estimate** identified. Hirschsprung disease’s general-population sex ratio must not be substituted for a GOSHS ratio. [1][125] |
| Geography, founder effects, anticipation, mosaicism | Families from multiple geographic backgrounds have been reported; no validated worldwide founder allele, geographic incidence pattern, genetic anticipation, or quantified germline-mosaicism risk. Consanguinity aided identification in some families but is not required. [151][37] |

## 10. Diagnostics

**Clinical suspicion:** microcephaly and developmental delay with Hirschsprung disease or cortical malformation—**or the neural phenotype without Hirschsprung disease**—warrant molecular evaluation. No standalone consensus diagnostic score or syndrome-specific circulating biomarker is established. [3][37]

| Test or assessment | Purpose and interpretation |
|---|---|
| *KIFBP* sequencing, with deletion/duplication assessment | **Molecular confirmation:** identify and classify two pathogenic/likely pathogenic variants **in trans**, or a homozygous causal variant; examine segregation where possible. A phenotype alone or a single VUS does not establish the same molecular certainty. Targeted single-gene testing is reasonable when findings and familial variants are known. [37][151] |
| Neurodevelopmental/Hirschsprung or brain-malformation multigene panel; trio WES/WGS | Useful when signs overlap other syndromes, Hirschsprung disease is absent, or the causal gene is unclear. **WES** identified an atypical 2020 patient and was used in 2024 case reports. WGS can assess coding and otherwise difficult-to-detect variants when earlier testing is unrevealing; a GOSHS-specific incremental diagnostic yield is unavailable. [37][48][47] |
| Copy-number analysis | Include *KIFBP* exon-level deletions where indicated. Chromosomal microarray can evaluate broader developmental-delay differentials, but a normal CMA does **not** exclude sequence-level *KIFBP* disease. Routine karyotype/FISH, mitochondrial DNA, and repeat-expansion testing do not target the established cause. [37][51] |
| Rectal suction or surgical biopsy | **Confirm suspected Hirschsprung disease** by adequate submucosal sampling and absent ganglion cells; appropriate histology may include H&E and calretinin/peripherin assessment. The underlying Hirschsprung guideline recommends histologic confirmation **before pull-through**. [PMID: **32586397**](https://pubmed.ncbi.nlm.nih.gov/32586397/) (2020). [125][1] |
| Abdominal radiograph/contrast enema; anorectal manometry | Evaluate obstruction, the likely transition zone, or an absent recto-anal inhibitory reflex; **none replaces diagnostic rectal histology**. [125][37] |
| Brain MRI; examination and targeted tests | Characterize cortical, callosal and other malformations. Use developmental assessment, ophthalmology, growth/nutrition review, neurological examination ± nerve studies, EEG **if seizures are suspected**, and cardiac/renal assessment according to findings. These evaluate manifestations, not the causal genotype. [1][37][47] |

**Differential:** especially ***ZEB2*-related Mowat–Wilson syndrome** and Baraitser–Winter syndrome for overlapping microcephaly/developmental and facial findings; consider other genetic causes of syndromic Hirschsprung disease and cortical malformations. **Do not substitute the *SKI*-associated Shprintzen–Goldberg diagnosis**, which has a different defining constellation. Molecular testing resolves ambiguous presentations. [1][3][21]

No validated GOSHS-specific RNA-seq, proteomic, metabolomic, methylation, or liquid-biopsy clinical diagnostic exists. Symptom-directed investigation in an affected child is distinct from population newborn screening. [37][1]

## 11. Outcome and prognosis

**There are no reliable GOSHS-specific five- or ten-year survival rates, mortality rates, or life-expectancy estimates.** Orphanet says long-term prognosis depends on the nature and severity of associated birth defects. Individual clinical reports document survival into adulthood—including a **28-year-old** in the 2020 study and the adult-affected family reported in 2024—but cannot define average survival. A neonatal sibling death from postoperative sepsis in one family illustrates potential complication severity, not an estimated mortality rate. [1][37][24]

Long-term morbidity can involve developmental disability, speech difficulty, neuropathy, visual problems, and treated or persistent bowel dysfunction. Hirschsprung-specific guidance notes that constipation, incontinence, and enterocolitis can continue after surgery, but its outcome percentages **must not be relabeled as GOSHS-specific rates**. Neither variant position, KIFBP protein level, nor a serum marker is validated to forecast an individual GOSHS course. [1][125][37]

## 12. Treatment and real-world implementation

**Treatment is complication-directed; no therapy is established to restore KIFBP function.** The following are care approaches or, where indicated, extrapolations from Hirschsprung disease guidelines—not GOSHS-specific efficacy trials. [1][125]

| Clinical need | Intervention and suggested NCIt annotation | Evidence, outcomes, and cautions |
|---|---|---|
| Confirmed Hirschsprung disease with obstruction | Specialist bowel decompression, often **saline rectal irrigations** before definitive **pull-through surgery**; a stoma when decompression fails or complications require it. Suggested broad NCIt **Surgical Procedure C15329**; use a more specific, verified procedure term in a coded record. | ERNICA recommends histologic confirmation, decompression and surgery once stable and growing. Its rectosigmoid guidance is **not a GOSHS-specific trial**; operative approach depends on disease extent and clinical status. [125][209] |
| Hirschsprung-associated enterocolitis | Urgent surgical assessment; admitted patients may require **IV fluids, broad-spectrum antibiotics and rectal washouts**. Suggested broad NCIt **Therapeutic Procedure C49236** where a more specific verified term is unavailable. | Treat as a potentially severe **downstream complication**, not as an infectious cause of GOSHS. ERNICA guidance provides the management basis; drug selection depends on clinical setting. [125][181] |
| Developmental, speech and motor impairment | Individualized early intervention, education, speech-language and physical/occupational rehabilitation. Candidate NCIt **Physical Therapy C15302** and **Speech Language Therapy C159273**; verify local terminology version. | Supported as individualized supportive care by Orphanet; **no syndrome-specific response percentage** exists. [1][208][209] |
| Ocular, cardiac, renal, skeletal, neurological complications | Specialist assessment and manifestation-specific treatment; antiseizure medication **only if clinically indicated**, not universal prophylaxis. | Orphanet recommends multidisciplinary care; there is no established GOSHS-specific drug or pharmacogenomic prescribing rule. [1][37] |
| Family planning | Genetic counseling; candidate NCIt **Genetic Counseling C15240**. | Confirm molecular findings and explain recessive reproductive risks, testing options, and phenotype variability. [1][208] |

**Investigational status:** no disease-modifying drug, gene replacement/editing, RNA therapy, cell therapy, immunotherapy, genotype-directed medication, or established GOSHS-specific treatment response rate is supported by the retrieved clinical evidence. Orphanet’s website category count for “clinical trial(s)” is **not** evidence that an interventional KIFBP trial exists; no verified GOSHS-specific NCT identifier is supplied here. **In vitro** restoration of expression in an experimental model is not a patient therapy. [1][225]

## 13. Prevention

| Prevention level | Disease-specific interpretation |
|---|---|
| Primary | There is **no demonstrated vaccine, diet, exposure avoidance, or medication** that prevents a child who inherits two causal variants from having GOSHS. For a family with known variants, offer counseling and discuss **carrier, prenatal, or preimplantation genetic testing** according to preferences and local practice; these are reproductive options, not treatment of an affected person. [1] |
| Secondary | Targeted **family testing** and prompt assessment of neonatal stooling/obstruction, growth, vision and development can enable earlier recognition and management. Orphanet notes that prenatal molecular diagnosis is possible once familial variants are known; ultrasound suspicion alone is difficult and requires confirmation. No established population newborn-screening program is identified. [1][125] |
| Tertiary | Manage confirmed bowel aganglionosis and promptly recognize enterocolitis; provide developmental support and monitoring tailored to actual cardiac, ocular, urogenital or skeletal abnormalities. Routine age-appropriate immunization remains ordinary healthcare, **not GOSHS-specific prophylaxis**. [1][125] |

## 14. Other species and naturally occurring disease

**Confirmed syndrome:** humans, *Homo sapiens* (**NCBI Taxon:9606**). Ortholog-based **experimental phenotypes** have been studied in house mouse, *Mus musculus* (**Taxon:10090**; *Kifbp*, **NCBI Gene:72320**, MGI:1919570), and zebrafish, *Danio rerio* (**Taxon:7955**; *kifbp*, **ZFIN:ZDB-GENE-070117-1989**). These are **models**, not documented naturally occurring Goldberg–Shprintzen syndrome in an animal breed. No verified veterinary breed/VBO association, animal-to-human transmission, or zoonotic potential applies to this inherited disorder. [107][111][151][92]

## 15. Model organisms and research applications

| Model | Recapitulated findings, limitations, and application |
|---|---|
| **CRISPR/Cas9 *Kif1bp* exon-1 knockout mice**, two independent lines | **Model evidence:** smaller brains and olfactory bulbs, thin anterior commissure, defective vagal/sympathetic innervation and delayed embryonic enteric-neural-crest colonization. Both lines died **within 3–4 hours of birth** with respiratory failure signs. **Important limitation:** ganglion cells occupied the entire bowel by birth—**not** a faithful human Hirschsprung phenotype; mice cannot model long-term adult human outcomes. Useful for developmental neurobiology and species comparison. [PMID: **29192291**](https://pubmed.ncbi.nlm.nih.gov/29192291/) (2017); MGI:1919570. [151][107] |
| **Zebrafish *kifbp* mutant**, including ZFIN-listed *kifbp*^st23/st23^ | **Model evidence:** reduced early axonal-outgrowth speed, disrupted axonal microtubules and later axonal degeneration. **Limitation:** no full human-like distal-bowel aganglionosis demonstrated. Useful for live imaging and axon-growth mechanisms. [PMID: **18192286**](https://pubmed.ncbi.nlm.nih.gov/18192286/) (2008); ZFIN:ZDB-GENE-070117-1989. [92][111][151] |
| **Mouse embryonic cortical shRNA and primary-neuron cultures** | **Model evidence:** migration, arborization, axonal-projection and apoptosis findings; shRNA-resistant *Kbp* rescued the tested migration phenotype. **Limitation:** partial, spatially restricted knockdown is not a patient’s lifelong biallelic genotype. Useful for distinguishing cell-development processes. [PMID: **31736709**](https://pubmed.ncbi.nlm.nih.gov/31736709/) (2019). [225] |
| **Human fibroblasts; SH-SY5Y and transfected HEK293T cells; dividing-cell assays** | **In vitro evidence:** patient-variant transcript/protein effects, actin–microtubule associations, neurite growth, and CITK/midbody function. **Limitation:** these assays do not replicate a developing human enteric or cerebral tissue or prove treatment efficacy. [PMID: **23427148**](https://pubmed.ncbi.nlm.nih.gov/23427148/); [PMID: **32939943**](https://pubmed.ncbi.nlm.nih.gov/32939943/); [PMID: **34100550**](https://pubmed.ncbi.nlm.nih.gov/34100550/). [223][37][224] |

**Knowledge-base conclusion:** annotate ***KIFBP* biallelic germline loss of function** as the established initiating cause; annotate developmental cytoskeletal, enteric-neural-crest and cortical-neuron processes with their **model or in-vitro evidence provenance**; and keep hypothesized cytokinesis-to-microcephaly and expression-threshold effects separate from demonstrated human causal steps. Record **Hirschsprung disease as variable**, not obligatory, and do not merge this entry with *SKI*-associated Shprintzen–Goldberg syndrome. [37][151][224][21]

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 4 |
| Off topic | 2 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:33252036` (2 mentions) - The mechanism of kinesin inhibition by kinesin-binding protein.
  - shared terms: molecular, cell
- `PMC:PMC12905500` (1 mention) - Rules of the road: how to turn off kinesin motors.
  - shared terms: molecular, cell

Weighed against this report's own most characteristic terms: `kifbp`, `disease`, `variant`, `gosh`, `developmental`, `established`, `goshs-specific`, `bowel`, `hirschsprung`, `phenotype`, `patient`, `molecular`, `genetic`, `syndrome`, `cause`, `individual`, `validated`, `cell`, `clinical`, `assessment`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 10 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `CL:0002609` (obsolete neuron of cerebral cortex) (2 mentions) - replaced by `CL:0010012`

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `Gene`, `OMIM`, `Taxon`, `MGI`.

25 of 36 terms resolved to a current term; the rest could not be looked up either way.