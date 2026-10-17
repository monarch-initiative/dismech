---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-09T20:55:25.479880'
end_time: '2026-10-09T20:59:49.657971'
duration_seconds: 264.18
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Microcephaly, Epilepsy, and Diabetes Syndrome 2
  mondo_id: MONDO:0025690
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
citation_count: 55
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 21
  on_topic: 7
  validator_version: 0.3.0
term_validation:
  total_terms: 31
  verified: 26
  not_found: 0
  obsolete: 0
  unverifiable: 5
  confabulation_rate: 0.0
  unresolvable_prefixes:
  - ORPHA
  - Taxon
  - Gene
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Microcephaly, Epilepsy, and Diabetes Syndrome 2
- **MONDO ID:** MONDO:0025690 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Microcephaly, Epilepsy, and Diabetes Syndrome 2** covering all of the
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

# Microcephaly, epilepsy, and diabetes syndrome 2 (MEDS2): disease-characteristics report

**MEDS2 is an autosomal-recessive disorder caused by biallelic pathogenic variants in *YIPF5*.** Its characteristic combination is severe early microcephaly, infantile epilepsy, and neonatal or early-childhood diabetes. The strongest disease-specific clinical evidence remains six affected people from five families reported in 2020; a 2024 case report broadened the possible glycemic phenotype to illness-associated, transient hyperglycemia. Consequently, findings from that original series should not be treated as population-wide penetrance estimates. [47][41][89]

**Evidence key.** *Human* denotes affected-person observations; *experimental* denotes human cells, transplanted cells, or animals; *inference* identifies a proposed connection not demonstrated in affected human tissue. The report distinguishes MEDS2 from the wider **MEDS phenotype**, which can also be caused by *IER3IP1* or *TMEM167A*. [47][58]

## 1. Disease information

| Identifier or name | MEDS2 entry and interpretation |
|---|---|
| Preferred name and abbreviation | Microcephaly, epilepsy, and diabetes syndrome 2; **MEDS2**. [41] |
| MONDO | **MONDO:0025690**. [16] |
| Disease OMIM | **619278**; autosomal recessive, mapped to *YIPF5* at **5q31.3**. [41] |
| Causal-gene OMIM | *YIPF5*, **611483**. [41] |
| Orphanet | **ORPHA:306558**, *primary microcephaly-epilepsy-permanent neonatal diabetes syndrome*. **This is a broader entry:** Orphanet maps both OMIM **614231** and **619278** to it, so its description and prevalence must not automatically be assigned specifically to *YIPF5*-MEDS2. [60] |
| ICD-10 / ICD-11 | Orphanet lists **Q87.8 / 8A60.9** for its broader syndrome entry; neither is a demonstrated MEDS2-specific billing or diagnostic code. [60] |
| MeSH | No MEDS2-specific MeSH heading was identified; the 2023 rabbit study is indexed under broader headings including *Microcephaly*. [74] |
| Other names | *YIPF5*-related MEDS; *YIPF5*-related microcephaly, epilepsy, and early-onset diabetes. The Orphanet name above is an overlapping **phenotype-level** name, not an exact synonym restricted to *YIPF5*. [41][60] |

**Data provenance.** The six-person series and 2024 report are observations of individual patients subsequently summarized in publications; OMIM, Orphanet, MONDO, and phenotype aggregators are **aggregated disease-level resources**. No patient-level EHR dataset, representative registry, or disease-specific quality-of-life cohort was identified. [47][89][41][60]

## 2. Etiology, risk, protection, and gene–environment interaction

The established initiating cause is **germline, biallelic *YIPF5* variation with impaired function**, rather than an infection, toxin, or lifestyle exposure. All six originally reported patients came from consanguineous families; unaffected parents carried the relevant variant heterozygously. Consanguinity increases the chance of homozygosity in such families, but is neither a biological requirement nor a population-specific cause. No validated susceptibility locus, modifier gene, protective allele, or environmental measure that prevents MEDS2 was identified. [47][41]

There is **limited clinical evidence of an interaction with physiological stress**: the 2024 patient had severe hyperglycemic episodes during ordinary illnesses that resolved after recovery. Separately, *YIPF5*-deficient experimental β cells were more vulnerable when investigators applied ER stressors. These observations support **illness as a possible trigger of metabolic expression in a genetically susceptible person**, not infection as the cause of MEDS2 or proof that all variants behave this way. *Giannakopoulos and Chrysis, 2024*, *Hormones* 23:831–834, PMID **38632213**, DOI [10.1007/s42000-024-00552-z](https://doi.org/10.1007/s42000-024-00552-z); *De Franco et al., 2020*, PMID **33164986**. [89][47][107]

> **Exact 2024 abstract excerpt:** “short events of severe hyperglycemia, induced by the stress of common illnesses, which completely resolved after recovery.” This is a **single-patient** observation. [89]

## 3. Phenotypes and impact on functioning

The frequencies below refer **only to the six genetically confirmed patients in the original series** unless indicated otherwise. They are not unbiased estimates for all people with MEDS2. Suggested HPO terms annotate findings; an HPO code does not independently validate its frequency. [47][120]

| Phenotype type and finding | Onset, severity, course, and observed frequency | Function or quality-of-life implication; suggested HPO term |
|---|---|---|
| Physical sign — **severe microcephaly** | **6/6**; median head-circumference standard-deviation score **−6.2**. Early developmental abnormality; individual longitudinal head-growth rates were not established. [47][41] | Indicates major brain-development involvement; **Microcephaly HP:0000252**. No MEDS2-specific quality-of-life score is available. [120][47] |
| Clinical manifestation — **epilepsy**, reported as generalized tonic–clonic seizures | **6/6**; reported onset **1–7 months**. Course varies: one child's epilepsy resolved by age **2 years**; a uniform drug-resistance designation is unsupported for the *YIPF5* series. [41][173] | Seizures require safety planning and neurological care; **Bilateral tonic-clonic seizure HP:0002069** or broader **Seizure HP:0001250**. [120][121] |
| Laboratory/clinical diagnosis — **diabetes** | **6/6**; diagnosed from **4 weeks to 20 months** and treated with full-replacement insulin. Two affected sisters retained low but measurable C-peptide more than 10 years after diagnosis. A separate **2024 single case** instead had illness-associated episodes that resolved. [47][89] | Insulin-dependent cases require ongoing glucose measurement and treatment; **Diabetes mellitus HP:0000819**. “Permanent neonatal diabetes” does **not** describe every reported *YIPF5* glycemic presentation. [60][89] |
| Developmental/behavioral-function finding — **severe developmental delay** | Reported in **5/6**; the remaining child reportedly had normal neuromotor development at age five. Speech was absent in several older patients in a later compilation. [47][94] | Likely substantial communication, learning, and care needs where present; **Global developmental delay HP:0001263**. No standardized disability or EQ-5D/SF-36 result was found. [120][47] |
| Growth sign — **low birth weight** | **6/6** in the original report. Reduced fetal insulin secretion is the investigators’ interpretation, rather than a directly measured fetal mechanism. [47] | May add early nutritional and medical needs; **Small for gestational age HP:0001518** is a *suggested* annotation, but birth-weight findings should be checked against gestational-age criteria before assigning it to an individual. [120][47] |
| Possible imaging sign — **enlarged lateral ventricles** | Listed in an aggregated MEDS2 phenotype description as rare; a reliable numerator and longitudinal course were not established from the primary series. [120] | **Lateral ventricle dilatation HP:0006956** only if demonstrated on that person's imaging. [120] |

**Phenotype-boundary caution:** Orphanet additionally describes hypotonia, feeding problems, dysmorphism, cortical gyral simplification, and callosal abnormalities for its **combined syndrome entry**. These should **not** receive a MEDS2-specific frequency—or be entered as confirmed manifestations of each *YIPF5* case—without patient-level supporting evidence. Similarly, a phenotype-aggregator label of “very rare (1%)” for the three defining signs conflicts with their observation in **6/6** original patients and should not be copied as a MEDS2 frequency. [60][47][120]

## 4. Genetic and molecular information

*YIPF5* (**HGNC:24877**; NCBI Gene **81555**; OMIM **611483**; UniProt **Q969M3**) encodes a membrane protein of the early secretory pathway. Five distinct homozygous variants accounted for the original six affected people. The following classifications are **reported ClinVar classifications**, not a new independent ACMG/AMP reassessment. Nucleotide coordinates use the transcript stated by OMIM, **NM_001024947.3**; ClinVar displays corresponding nomenclature on **NM_030799.9**. [61][69][173][40]

| Germline *YIPF5* variant | Class; original human observations | Reported classification and population evidence |
|---|---|---|
| **c.542C>T; p.(Ala181Val)** | Missense; third transmembrane domain; one affected child. [173] | ClinVar **pathogenic**, Variation ID **1064542**; not observed in gnomAD at the original authors’ 2020 query. [40][47] |
| **c.317_319del; p.(Lys106del)** | In-frame, single-amino-acid deletion; cytoplasmic region; one genetically tested affected child. [173] | ClinVar **pathogenic**, ID **1064543**; absent from the authors’ gnomAD query. Four similarly affected siblings were described but **not genotyped**. [40][47] |
| **c.293T>G; p.(Ile98Ser)** | Missense; cytoplasmic region; **two affected sisters**; investigated using patient-derived and engineered stem cells. [173][47] | ClinVar **pathogenic**, ID **1064544**; absent from the authors’ gnomAD query. [40][47] |
| **c.652T>A; p.(Trp218Arg)** | Missense; fourth transmembrane domain; one affected child; subsequently engineered into a rabbit model. [173][74] | ClinVar **pathogenic**, ID **1064545**; absent from the authors’ gnomAD query. [40][47] |
| **c.290G>T; p.(Gly97Val)** | Missense; cytoplasmic region; one affected child. [173] | ClinVar **pathogenic**, ID **1064546**; absent from the authors’ gnomAD query. [40][47] |

These are **affected-family germline findings**, not somatic mutations. “Not seen in gnomAD” describes the **database and date used in the 2020 paper**, not a newly verified zero allele frequency in every population. Experimental results support reduced or altered *YIPF5* function, but **complete knockout is not equivalent to every patient missense allele**; residual function and genotype–phenotype relationships remain uncertain. A listed *YIPF5* **p.(Val175Asp)** ClinVar variant is a **VUS**, not one of the five established original MEDS2 alleles. No MEDS2-specific pathogenic chromosomal rearrangement, repeat expansion, epigenetic signature, or established modifier gene was identified. [47][40][58]

## 5. Environmental information

**Disease causation:** no toxin, radiation, occupation, diet, smoking exposure, or infectious agent has been established as a cause of *YIPF5*-MEDS2. **Disease management and expression:** intercurrent illness may precipitate hyperglycemia in an affected person, based on the 2024 case; ordinary nutrition, glucose monitoring, and avoidance of missed insulin address complications, not the inherited lesion. No zoonotic pathogen or environmentally transmitted route applies. [47][89]

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic germline *YIPF5* variants lead to** reduced or altered function of an early-secretory-pathway membrane protein. This initiating gene–disease relationship is supported by human segregation and experimental models. [47][41]
2. **Altered YIPF5 leads to** cargo-dependent disruption of ER/ER–Golgi trafficking. In β-cell models, it results in **proinsulin retention in the ER**; other cell systems show **increased**, rather than universally decreased, export of particular SURF4-associated cargoes. Thus “all ER export stops” is **not** the supported mechanism. [47][59]
3. **β-cell branch:** retained proinsulin **leads to** ER distension and stress-response activation; persistent or provoked stress **increases susceptibility to** apoptosis and **results in** reduced effective β-cell function and insulin availability. These steps are experimentally demonstrated in human β-cell models; the exact timing of cell loss in patients is **inferred**. [47]
4. **β-cell branch, clinical consequence:** inadequate insulin availability **results in** diabetes and likely contributes to low fetal growth. The diabetes is observed in humans; its proposed contribution to fetal growth is **inferred**. [47]
5. **brain branch:** altered YIPF5-dependent neuronal cargo localization and cortical-cell behavior **leads to** disturbed neuronal maturation and migration in cultured neurons and embryonic animals. A further step from those changes **to human microcephaly is inferred**, not yet demonstrated in patient cortex; the precise route to epilepsy also remains **inferred**. [59][74][47]

> **Exact primary-study abstract excerpt:** “Loss of *YIPF5* function in stem cell–derived islet cells resulted in proinsulin retention in the ER, marked ER stress, and β cell failure.” *De Franco et al.*, published **9 November 2020**, *Journal of Clinical Investigation* 130:6338–6353, PMID **33164986**, DOI [10.1172/JCI141455](https://doi.org/10.1172/JCI141455). **Evidence: human stem-cell and patient-derived in-vitro models**, alongside a human case series. [47]

**Upstream and downstream detail.** Human embryonic-stem-cell-derived *YIPF5* knockout β cells showed **5.5-fold more proinsulin-stained area**, **70% less insulin-stained area**, **80% less cellular insulin**, and markedly distended ER compared with controls. Knockdown increased apoptosis after applied ER stress; *CHOP* knockdown was protective **in cells**, not an established patient treatment. Patient **p.(Ile98Ser)** stem-cell models had a milder basal phenotype but greater vulnerability to stress. Knockout α cells did not show the same ER-distension finding, supporting β-cell selectivity in that experiment rather than pancreas-wide damage. Appropriate suggested process terms include **GO:0034976, response to ER stress; GO:0006915, apoptotic process; and GO:0016192, vesicle-mediated transport**. [47][240]

**Newer neuronal and cargo work.** A **2023** edited rabbit carrying **p.(Trp218Arg)** developed a smaller head, motor abnormalities, reduced survival, and evidence linking cortical-neuron ER stress to disturbed apical-progenitor generation. A **2026** experimental study found YIPF5 interaction with **SURF4**, altered secretome and cell-surface adhesion proteins, and impaired neuritic **L1CAM** localization in rat neurons; embryonic mouse *Yipf5* knockdown shifted labeled cells from ventricular/subventricular zones toward cortical plate and altered neuronal morphology. Its authors explicitly leave unresolved which cargo, calcium, or migration changes cause **human** microcephaly. *Liu et al.*, online **2 May 2023**, PMID **37142085**, DOI [10.1016/j.nbd.2023.106135](https://doi.org/10.1016/j.nbd.2023.106135); *Bruno et al.*, **27 January 2026**, PMID **41717013**, DOI [10.1016/j.isci.2026.114791](https://doi.org/10.1016/j.isci.2026.114791). [74][59]

> **Exact 2026 summary excerpt:** “*In utero* knockdown of *Yipf5* in embryonic mouse brains induces premature neuronal migration and abnormal neuronal morphology.” This supports a **model-organism mechanism**, not proof of the corresponding event in patients. [59]

**Other pathway/omics boundaries.** The disease-specific evidence centers on **secretory trafficking, proinsulin handling, and ER stress**, not a demonstrated MEDS2-specific Wnt, MAPK, PI3K–AKT, or mTOR cascade. A 2026 study supplied **proteomic secretome and surfaceome** results—not a clinical proteomic diagnostic signature—including **832 filtered secreted proteins** and **630 significantly altered surface proteins** in its experimental comparison. No validated MEDS2 patient metabolomic, lipidomic, methylation, single-cell, or spatial-transcriptomic signature was identified. YIPF5 has an experimentally described role in **STING trafficking and DNA-virus innate signaling**, but an immune-deficiency phenotype has **not** been established in MEDS2 patients. [47][59][173]

**Suggested mechanism annotations:** pancreatic β cell **CL:0000169**; neuron **CL:0000540**; pancreatic α cell **CL:0000171**, principally as an experimental comparator; ER/ER membrane **GO:0005783 / GO:0005789** and Golgi apparatus **GO:0005794**. Suggested terms describe relevant processes and compartments; they are not automatically curated direct *YIPF5* GO annotations. [153][199][244][47]

## 7. Anatomical structures affected

| Level | Evidence-based localization and suggested term |
|---|---|
| Organ/system | **Developing brain/cerebral cortex** and **endocrine pancreas** are the principal implicated sites: **UBERON:0000955** brain, **UBERON:0000956** cerebral cortex, **UBERON:0001264** pancreas, **UBERON:0000006** islet of Langerhans. Neurological and glycemic complications can affect other systems secondarily; primary kidney or liver injury has not been established. [47][194] |
| Tissue/cell | Cortical ventricular-zone progenitors and neuronal compartments express *YIPF5* in examined human fetal tissue; experimental disease mechanisms involve pancreatic **β cells CL:0000169**, neurons **CL:0000540**, and developing cortical progenitors. A precise progenitor CL subclass should be assigned only when a study actually identifies it. [47][59][153][199] |
| Subcellular | **ER membrane GO:0005789**, ER **GO:0005783**, ER–Golgi intermediate compartment **GO:0005793**, and Golgi apparatus **GO:0005794**. [47][59][244] |
| Laterality | The reported small-head and systemic diabetic findings are not defined by a characteristic unilateral lesion; no MEDS2-specific anatomical lateralization is established. [47] |

## 8. Temporal development

*YIPF5* dysfunction is present from conception; microcephaly is an early developmental feature. In the original series, epilepsy was diagnosed at **1–7 months**, and diabetes at **4 weeks–20 months**. Diabetes was usually persistent and insulin-treated, while one later case establishes a possible **episodic, illness-associated** glycemic presentation. Five of six original patients had severe developmental delay, but one had comparatively preserved neuromotor development and seizure resolution. There is **no validated MEDS2 staging system**, measured population progression rate, predictable remission schedule, or defined therapeutic critical window. Fetal cortical development and infancy are biologically plausible periods of vulnerability, **inferred** from expression and model experiments rather than an intervention trial. [47][41][89][59]

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two confirmed heterozygous carrier parents, the Mendelian risk for **each pregnancy** is **25% affected, 50% carrier, and 25% neither familial variant**; this is a genetic probability, not a measured MEDS2 recurrence cohort. The original six genetically confirmed patients arose in five consanguineous families and included **three males and three females**; that tiny selected series establishes neither a population sex ratio nor an ethnic restriction. A later compilation locates the original cases in **Turkey and India**. Four additionally reported affected siblings lacked DNA confirmation and must not be included in the six genetically confirmed cases. [41][47][94]

Orphanet’s **less than 1 per 1,000,000** figure concerns its **broader entry**, not a measured *YIPF5*-MEDS2 prevalence. Disease-specific incidence, carrier frequency, penetrance, founder effect, anticipation, and germline-mosaicism rate remain **unquantified**. Clinical expressivity is demonstrably variable, particularly in development and glycemic presentation. [60][47][89]

## 10. Diagnostics

**Clinical suspicion and tests.** Consider MEDS2 when marked early microcephaly and infantile seizures accompany diabetes or unexplained hyperglycemia. Evaluate serial head circumference, development, seizure history, plasma glucose and longer-term glycemic control, and endogenous insulin secretion where informative; use **EEG** to characterize suspected seizures and **brain MRI** to investigate structural abnormalities and alternatives. These clinical tests assess manifestations: **a molecular diagnosis requires identifying an appropriately interpreted biallelic *YIPF5* genotype**. Neither a specific MRI pattern, EEG pattern, biopsy, nor protein/metabolite assay is validated as a standalone MEDS2 diagnostic test. [47][41][60]

**Genetic approach.** The original investigators found *YIPF5* through **whole-genome sequencing** of two unsolved probands and then screened an additional **187** early-diabetes cases lacking a known molecular diagnosis; **three more probands** were found, including the family with a second affected sibling. This **3/187 is a selected unresolved-cohort yield**, not population prevalence. Clinical testing can use an appropriately curated neonatal/monogenic-diabetes panel that includes *YIPF5*, with *IER3IP1*, *TMEM167A*, and other phenotype-appropriate genes considered; exome/genome analysis is useful if panel testing is unrevealing or the phenotype is atypical. Confirm the variants, phase/segregation, and ACMG/AMP interpretation; targeted familial testing then supports cascade assessment. Genomics England lists *YIPF5* on a **neonatal-diabetes** panel. [47][226][58]

**Practice context and differential.** ISPAD’s **2022** guideline recommends **immediate molecular testing for diabetes diagnosed before six months** and consideration at **6–12 months**, particularly with atypical features. The differential includes *IER3IP1*-MEDS1, *TMEM167A*-associated MEDS, other syndromic neonatal-diabetes genes, and other causes of congenital microcephaly and seizures. Unlike *YIPF5*, activating *KCNJ11/ABCC8* disease is a **potassium-channel** subtype that can change diabetes drug selection. Chromosomal microarray, karyotype/FISH, mitochondrial sequencing, and repeat-expansion tests are **not established *YIPF5*-specific confirmatory tests**; use them only for a broader differential when indicated. No validated MEDS2 liquid-biopsy or omics diagnostic was identified. [209][1][58][1]

## 11. Outcomes and prognosis

The condition can entail major neurological disability and sustained need for insulin, but prognosis is **not uniform**. One original genetically confirmed child died at **1.3 years**; four clinically similarly affected, **un-genotyped** siblings in that family reportedly died in infancy. Conversely, two genetically confirmed sisters were reported at **21 and 15 years**, and another child had reported normal neuromotor development at five years with seizures resolved by two. A description of MEDS2 as inevitably fatal in early childhood would therefore contradict the reported patient ages. There are **no reliable five- or ten-year survival rates, life-expectancy estimate, disease-specific mortality rate, validated prognostic biomarker, or standardized quality-of-life scores**. Variant residual function may influence severity, but a predictive genotype–phenotype model has not been established. [41][94][47]

## 12. Treatment and current implementation

**Care is directed at manifestations; there is no established therapy that corrects *YIPF5* function.** The treatments below are clinical strategies or phenotype-based considerations, **not MEDS2 trial-proven response-rate claims**. NCIt terms are suggested annotations only where the concept is appropriate. [47][1]

| Treatment or strategy | MEDS2 evidence and limitations | Suggested annotation |
|---|---|---|
| **Insulin replacement and glucose monitoring** | All six original patients received full-replacement insulin. Tailor treatment to measured glycemia: the separate 2024 report had hyperglycemia that resolved between illnesses. Watch for insulin-associated hypoglycemia and illness-associated glycemic deterioration. Human clinical evidence; no MEDS2 comparative trial. [47][89] | **CHEBI:5931** human insulin; broader **CHEBI:145810** insulin; **NCIT:C15986** pharmacotherapy. [241][245] |
| **Individualized antiseizure treatment, seizure-safety planning, and EEG-guided review** | Epilepsy was reported in all six original patients, with spontaneous or treatment-associated seizure resolution not separable in one child from the available account. No particular antiseizure drug, combination, or response rate is established specifically for MEDS2. [47][41] | **NCIT:C15986** pharmacotherapy; do not annotate a named drug as *administered to a MEDS2 patient* without a patient-level source. [245] |
| **Developmental and supportive care** | Assess feeding, growth, mobility, communication, and learning; offer appropriate physical, occupational, speech, nutritional, and family support according to the individual’s deficits. These are reasonable supportive interventions, **not demonstrated genotype-correcting therapies**. [47] | **NCIT:C49236** therapeutic procedure, when a broad intervention term is needed. [150] |
| **Stress-pathway, gene, RNA, or cell-based therapy** | Cellular *CHOP*/*DP5* knockdown and experimental protection from ER-stressor injury are **mechanistic experiments**, not human treatments. No MEDS2-specific approved gene editing, gene replacement, ASO/siRNA, β-cell transplant, or targeted drug with demonstrated patient benefit was identified. [47] | Record as **experimental mechanism**, not a clinical-intervention outcome. |
| **Ketogenic diet** | A 2023 MEDS case report concerned ***IER3IP1*-related disease**, **not *YIPF5*-MEDS2**. Its reported seizure management and diabetic-ketoacidosis caution must not be converted into MEDS2 efficacy evidence. [1] | No MEDS2-specific treatment annotation supported. |

**Genotype matters:** ISPAD discusses sulfonylurea responsiveness for certain ***KCNJ11/ABCC8*** neonatal-diabetes genotypes, **not** as established treatment for *YIPF5*-MEDS2. A sensible clinical sequence is to stabilize glucose and seizures, obtain comprehensive molecular testing, then revise the individualized plan using the confirmed genotype and clinical course. No MEDS2-specific pharmacogenomic rule or treatment-response percentage has been established. [1][47]

## 13. Prevention

**Primary prevention of a new inherited case** is not achievable through vaccination, sanitation, toxin avoidance, or lifestyle modification. For a family with established variants, **genetic counseling**, carrier testing of relevant relatives, and discussion of reproductive options—including prenatal or preimplantation testing where available and desired—can inform decisions; these are options, not obligations. **Secondary prevention** means recognizing early diabetes/hyperglycemia and seizures and obtaining timely molecular diagnosis. **Tertiary prevention** means treating glycemic and seizure complications, monitoring development and nutrition, and providing rehabilitation. There is no MEDS2-specific vaccine, chemoprophylaxis, or population newborn-screening program established by the cited evidence. [41][209][47]

## 14. Other species and naturally occurring disease

Humans (**NCBI Taxon:9606**) are the species with the defined clinical diagnosis. Orthologous *Yipf5* is identified in mouse (**NCBI Gene:67180**) and rat (**NCBI Gene:361315**). The rabbit *YIPF5* p.(Trp218Arg) disease-relevant finding was **deliberately genome edited**: it is **not evidence of a naturally occurring rabbit breed disorder** or an OMIA-defined natural MEDS2 counterpart. No affected breed/VBO designation, natural veterinary MEDS2 case series, zoonotic transmission, or cross-species infectious transmission was identified. [61][65][74]

## 15. Model organisms and research applications

| Model system | What it reproduces or tests | Important limitation |
|---|---|---|
| **Human EndoC-βH1 knockdown and donor islets** | Tests ER-stressor sensitivity and apoptosis after reduced *YIPF5* expression. [47] | An acute or partial knockdown is not a lifelong patient allele. |
| **Human embryonic-stem-cell knockout and p.(Ile98Ser) knock-in β-like cells; patient iPSCs and corrected controls** | Tests proinsulin retention, ER stress, insulin content, variant effects, and rescue by an isogenic genetic control. [47] | Differentiated cells and knockout severity do not reproduce an entire developing human or every patient variant. |
| **Human islet-like grafts in immunocompromised mice** | Mutant grafts showed reduced human C-peptide and β-cell representation/function relative to control grafts. [47] | Mice received **human cell grafts**; they were not whole-animal hereditary MEDS2 models, and seizures or microcephaly were not assessed. |
| **Genome-edited p.(Trp218Arg) rabbit, 2023** | Reproduces a smaller head, altered motor ability, impaired growth/survival, and cortical developmental/ER-stress findings. [74] | The published abstract does not establish full reproduction of human insulin-dependent diabetes and epilepsy. |
| **Embryonic mouse cortical *Yipf5* knockdown and cultured rat hippocampal neurons, 2026** | Tests premature cortical migration, neuronal morphology, and neuronal **L1CAM** trafficking. [59] | Transient/local knockdown and cultured neurons do not establish a complete postnatal MEDS2 phenotype. |
| **Human-cell knockout/rescue, SURF4 assays, and secretome/surfaceome profiling, 2026** | Identifies cargo-selective trafficking and candidate routes toward cortical pathology. [59] | Much of the profiling used **non-neuronal cells**; a causal human neuronal cargo and clinical biomarker remain unproven. |

**Knowledge-base priority:** curate the **human biallelic *YIPF5*–MEDS2 association and its five original variants as established**; record β-cell ER/proinsulin dysfunction as experimentally supported; and mark the proposed specific routes from trafficking defects to **human** microcephaly and epilepsy as **model-supported but incompletely resolved**. Preserve the distinction between the original persistent-diabetes series, the single 2024 episodic-hyperglycemia report, and observations about the broader, genetically heterogeneous MEDS phenotype. [47][89][74][59][58]

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 21 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 5 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `Taxon`, `Gene`.

26 of 31 terms resolved to a current term; the rest could not be looked up either way.