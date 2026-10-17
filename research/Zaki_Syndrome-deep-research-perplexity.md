---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-15T07:40:11.633569'
end_time: '2026-10-15T07:44:39.937302'
duration_seconds: 268.3
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Zaki Syndrome
  mondo_id: MONDO:0859209
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
citation_count: 55
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Zaki Syndrome
- **MONDO ID:** MONDO:0859209 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Zaki Syndrome** covering all of the
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

# Zaki syndrome: disease-characteristics research report

**Assessment date:** October 15, 2026  
**Disease:** Zaki syndrome  
**Preferred identifier:** **MONDO:0859209**  
**Mendelian category:** Autosomal-recessive developmental disorder caused by biallelic **WLS** variants

## Executive summary

Zaki syndrome is an ultra-rare, congenital and postnatally evolving multisystem disorder caused by **biallelic germline loss-of-function or hypomorphic variants in WLS**, the transmembrane cargo receptor required for secretion of Wnt ligands. It is characterized most consistently by developmental delay, progressive postnatal microcephaly, short stature, distinctive facial appearance, sparse hair, ocular anomalies, and variable brain, limb, renal, cardiac, dental, and genital abnormalities. OMIM designates the disorder **ZKS, #619648**; MedGen is **C5562037**, and MONDO is **MONDO:0859209**. It must not be confused with **Zaki–Gleeson syndrome**, a separate disorder associated with **DDX59**. [Web:16][Web:22]

The defining 2021 study identified four homozygous missense alleles in 10 people from five families and demonstrated impaired WLS stability, a 60–80% reduction in Wnt secretion, reduced downstream reporter activity, developmental abnormalities in two knock-in mouse lines, and partial prenatal rescue with the GSK3 inhibitor/Wnt-pathway agonist **CHIR99021** (PMID: **34587386**, published September 30, 2021). [Web:32][Web:91] Reports from 2023 added compound-heterozygous inheritance and a severe phenotype including skeletal dysplasia, fractures, dental anomalies and Dandy–Walker malformation (PMIDs **37005218** and **37106064**). [Web:34][Web:109] A literature review through October 2024 found only **13 molecularly confirmed patients and nine pathogenic/likely pathogenic variants**, emphasizing that all frequency and prognosis estimates remain provisional. [Web:24]

---

# 1. Disease information

## 1.1 Definition

Zaki syndrome is a **WLS-related congenital malformation–neurodevelopmental syndrome** resulting from deficient secretion of multiple Wnt ligands during embryogenesis and subsequent tissue growth. Common findings include:

- developmental delay or intellectual disability;
- progressive, predominantly postnatal microcephaly;
- short stature;
- cupped ears, sparse scalp hair/eyebrows, wide nose and mouth, short philtrum and high-arched palate;
- eye, brain, skeletal, renal and cardiac malformations.

The authoritative MedGen definition emphasizes “developmental delay, progressive microcephaly, and short stature,” together with sparse scalp hair, cupped ears, a wide nose/mouth, short philtrum and high-arched palate. [Web:16]

## 1.2 Identifiers and nomenclature

| Resource | Identifier/name | Status and notes |
|---|---|---|
| MONDO | **MONDO:0859209** | Preferred cross-resource disease identifier |
| OMIM | **#619648 — Zaki syndrome; ZKS** | Phenotype entry [Web:16] |
| MedGen | **C5562037**, UID 1794247 | Disease or syndrome [Web:16] |
| OMIM gene | **WLS, *611514** | Causal gene |
| HGNC | **HGNC:30238 — WLS** | Approved human gene symbol [Web:76][Web:129] |
| NCBI Gene | **79971 — WLS** | Human gene |
| Ensembl | **ENSG00000116729** | Human WLS gene [Web:81] |
| UniProtKB | **Q5T9L3** | Human WLS protein [Web:76] |
| Cytogenetic location | **1p31.3** | WLS locus [Web:129] |
| MedGen synonym | “Microcephaly, progressive, with developmental delay, cupped ears, and dysmorphic features” | Descriptive alternative name [Web:19] |
| Orphanet | No dedicated Zaki-syndrome ORPHAcode located | Do **not** use ORPHA:329332; that code denotes DDX59-related Zaki–Gleeson syndrome |
| ICD-10 | No specific code | Usually coded under congenital malformation, microcephaly, developmental disorder or genetic-syndrome categories according to manifestations |
| ICD-11 | No verified disease-specific code located | A general “other specified congenital malformation syndromes” category may be appropriate locally |
| MeSH | No dedicated Zaki syndrome heading located | Literature is indexed using broader terms such as *Congenital Abnormalities*, *Microcephaly*, *Wnt Signaling Pathway* and *Intellectual Disability* |
| SNOMED CT | No specific verified Zaki-syndrome concept found | **764732004 refers to Zaki–Gleeson syndrome**, not WLS-related Zaki syndrome |

### Important naming distinction

**Zaki syndrome is not Zaki–Gleeson syndrome.** Zaki–Gleeson syndrome is microcephaly–cerebellar hypoplasia–cardiac conduction defect syndrome, OMIM 614407/MONDO:0013735/ORPHA:329332, caused by **DDX59**. [Web:22]

## 1.3 Source granularity

The evidence base combines:

- **individual-level human cases:** pedigree, clinical, imaging and sequencing data;
- **aggregated disease-level resources:** OMIM, MedGen, MONDO and ClinVar;
- **aggregated literature review:** 13 patients through October 2024;
- **experimental evidence:** patient fibroblasts, HEK293T cells, patient-derived iPSCs/embryoid bodies and knock-in mice.

No EHR-derived population cohort, claims-based cohort or national disease registry was identified.

---

# 2. Etiology

## 2.1 Primary causal factor

The established cause is **biallelic pathogenic or likely pathogenic germline variation in WLS**. WLS binds palmitoleated Wnt proteins in the endoplasmic reticulum and carries them through the Golgi/secretory pathway to the plasma membrane. Reduced WLS abundance or function therefore decreases secretion of several Wnt ligands rather than disrupting only one ligand. [Web:88][Web:91]

The landmark paper’s key abstract statement was:

> “We identified homozygous mutations in *WLS*, which encodes the Wnt ligand secretion mediator … in 10 affected persons from 5 unrelated families.”  
> — Chai et al., *New England Journal of Medicine*, September 30, 2021; PMID: 34587386. [Web:32]

## 2.2 Risk factors

| Risk-factor class | Evidence |
|---|---|
| Two pathogenic WLS alleles | Necessary molecular risk factor in confirmed cases |
| Parental carrier status | Two heterozygous parents have a 25% recurrence probability in each pregnancy |
| Consanguinity | Increased the probability of homozygous rare alleles in several original families; it is not biologically necessary because compound-heterozygous cases occur |
| Family history | An affected sibling or known carrier parents substantially raises prior probability |
| Population ancestry | Cases have occurred in Emirati, Egyptian, Native American, Indian, Chinese and other backgrounds; no ancestry-specific susceptibility is established |
| Sex | Both sexes can be affected; no sex-linked mechanism |
| Parental age | No established effect |
| Environmental exposure | No toxin, drug, infection, diet or lifestyle exposure has been shown to cause the syndrome |

The original discovery cohort was enriched for consanguinity, and families 1 and 2 had first-cousin parents. However, a 2023 Chinese case carried compound-heterozygous variants, demonstrating that homozygosity and consanguinity are not required. [Web:34]

## 2.3 Protective factors

No validated human genetic or environmental protective factor is known.

Residual WLS function may act as a **severity modifier**, because all reported disease alleles appear compatible with survival and many are hypomorphic missense substitutions rather than complete null alleles. Apparent milder findings in the small number of compound-heterozygous patients are hypothesis-generating, not an established protective genotype.

Prenatal CHIR99021 partially rescued mutant mice, but this is **experimental model-organism evidence**, not an established human protective exposure or preventive treatment. [Web:91]

## 2.4 Gene–environment interaction

No human gene–environment interaction has been demonstrated. The variable expressivity among people carrying the same p.Tyr392Cys allele could reflect modifiers, stochastic developmental effects, epigenetic state or environmental context, but these remain inferred. The 2025 review specifically cautioned that phenotype differences may reflect other genes, polymorphisms, epigenetic influences or external factors. [Web:24]

---

# 3. Phenotypes

## 3.1 Aggregate phenotype frequencies

The most systematic summary is the literature review of 13 patients available through October 2024. Denominators differ because reporting was incomplete. [Web:24]

| Phenotype | Type | Frequency | Usual onset/course | Suggested HPO term |
|---|---:|---:|---|---|
| Distinctive facial features | Physical sign | 12/12, 100% | Congenital/pediatric; persistent | HP:0001999, Abnormal facial shape |
| Cupped outer ears | Physical sign | 11/12, 91.7% | Congenital; stable | HP:0000378, Cupped ear |
| Sparse scalp hair | Physical sign | 10/11, 90.9% | Early childhood; persistent | HP:0002209, Sparse scalp hair |
| Postnatal microcephaly | Growth/neurologic sign | 10/11, 90.9% | Usually emerges after normal birth size; progressive | HP:0000252, Microcephaly; HP:0005484, Postnatal microcephaly |
| Neurodevelopmental disorder | Functional phenotype | 12/13, 92.3% | Infancy/childhood; chronic | HP:0012759 |
| Skeletal anomalies | Physical sign | 10/12, 83.3% | Mostly congenital; fractures may be later | HP:0000924 |
| Eye anomalies | Physical/functional sign | 9/11, 81.8% | Congenital or early infancy | HP:0000478 |
| Delayed global milestones | Developmental sign | 10/13, 76.9% | Infancy/childhood; persistent | HP:0001263 |
| Gross-motor delay | Developmental sign | 10/13, 76.9% | Infancy/childhood | HP:0002194 |
| Intellectual disability | Behavioral/cognitive | 9/12, 75.0% | Recognized in childhood; variable severity | HP:0001249 |
| High-arched palate | Physical sign | 9/12, 75.0% | Congenital; stable | HP:0000218 |
| Short philtrum | Physical sign | 9/12, 75.0% | Congenital; stable | HP:0000322 |
| Wide/broad nose | Physical sign | 9/12, 75.0% | Congenital; stable | HP:0000445, Wide nose |
| Structural brain anomaly | Imaging finding | 6/8, 75.0% | Congenital; generally non-remitting | HP:0012443 |
| Short stature | Growth sign | 8/12, 66.7% | Usually postnatal; may progress | HP:0004322 |
| Wide mouth | Physical sign | 8/12, 66.7% | Congenital; stable | HP:0000154 |
| Strabismus | Ophthalmic sign | 6/11, 54.5% | Infancy/childhood; potentially treatable | HP:0000486 |
| Syndactyly | Limb malformation | 6/12, 50.0% | Congenital; stable without surgery | HP:0001159 |
| High forehead | Physical sign | 6/12, 50.0% | Congenital/pediatric | HP:0000348 |
| Micrognathia | Physical sign | 6/12, 50.0% | Congenital | HP:0000347 |
| Corpus-callosum hypoplasia | MRI finding | 4/8, 50.0% | Congenital | HP:0002079 |
| Cerebellar-vermis hypoplasia | MRI finding | 4/8, 50.0% | Congenital | HP:0001320 |
| Abnormal neurologic signs | Clinical sign | 5/11, 45.5% | Childhood; variable | HP:0012638 |
| Long fingers/toes | Skeletal sign | 5/12, 41.7% | Congenital | HP:0100807; HP:0010511 |
| Sparse lateral eyebrows | Physical sign | 5/12, 41.7% | Congenital/pediatric | HP:0005338 |
| Median pseudocleft lip | Craniofacial sign | 5/12, 41.7% | Congenital | HP:0011340, Abnormal upper-lip morphology |
| Enlarged fourth ventricle | MRI finding | 3/8, 37.5% | Congenital | HP:0002198 |
| Broad distal finger phalanges | Skeletal sign | 4/12, 33.3% | Congenital | HP:0009882 |
| Anteverted nares | Physical sign | 4/12, 33.3% | Congenital | HP:0000463 |
| Hypotonia | Neurologic sign | 3/11, 27.2% in table | Infancy; variable | HP:0001252 |
| Iris coloboma | Eye malformation | 3/11, 27.3% | Congenital; permanent visual risk | HP:0000612 |
| Renal defects | Organ malformation | 3/12, 25.0% | Congenital | HP:0000077 |
| Patent foramen ovale | Cardiac finding | 3/13, 23.1% | Congenital; may close spontaneously | HP:0001655 |
| Microcornea | Eye malformation | 2/11, 18.2% | Congenital | HP:0000482 |
| Nystagmus | Ophthalmic sign | 2/11, 18.2% | Infancy/childhood | HP:0000639 |
| Optic-disc coloboma | Eye malformation | 2/11, 18.2% | Congenital; permanent | HP:0000588 |
| Renal agenesis | Organ malformation | 2/12, 16.7% | Congenital; permanent | HP:0000104 |
| Scoliosis | Skeletal sign | 2/12, 16.7% | Childhood; potentially progressive | HP:0002650 |

### Additional reported findings

- Complete soft-tissue syndactyly, ectrodactyly/polysyndactyly and reduced digits.
- Microphthalmia: HP:0000568.
- Dandy–Walker malformation: HP:0001305.
- Skeletal dysplasia and spontaneous fractures: HP:0002652 and HP:0002757.
- Dental anomalies, including tooth agenesis/malformation.
- Cryptorchidism: HP:0000028.
- Congenital diaphragmatic hernia: HP:0000776.
- Hydronephrosis: HP:0000126.
- Alopecia: HP:0001596.
- Seizure in at least one patient: HP:0001250.
- Spastic or unsteady gait and impaired standing/walking.
- Congenital umbilical polyp in the 2025 early-diagnosed infant, an association requiring replication. [Web:24][Web:109]

## 3.2 Severity and quality-of-life impact

Severity is highly variable. Major impacts include:

- **Development and education:** delayed language, motor and social milestones; intellectual disability may require lifelong educational and caregiver support.
- **Mobility:** syndactyly, ectrodactyly, skeletal dysplasia, scoliosis, fractures, hypotonia or spasticity can impair standing, walking and self-care.
- **Vision:** coloboma, microphthalmia, strabismus, nystagmus and optic-disc defects may cause substantial visual disability.
- **Growth and nutrition:** progressive microcephaly and short stature require longitudinal surveillance; feeding effects have not been systematically measured.
- **Renal health:** unilateral renal agenesis may be asymptomatic initially but reduces renal reserve.
- **Psychosocial health:** no syndrome-specific EQ-5D, SF-36, PROMIS or caregiver-burden study has been published.

In the 2025 infant, Gesell developmental quotient was 57.1, mild hypotonia appeared by three months, and head circumference declined from the 25th–50th percentile at birth to approximately −3 SD by eight months, illustrating the postnatal evolution. [Web:24]

---

# 4. Genetic and molecular information

## 4.1 Causal gene

| Attribute | Value |
|---|---|
| Gene | **WLS** |
| Full name | Wnt ligand secretion mediator |
| Aliases | Wntless, EVI, GPR177 |
| HGNC | **HGNC:30238** |
| NCBI Gene | **79971** |
| Ensembl | **ENSG00000116729** |
| OMIM | ***611514** |
| UniProt | **Q5T9L3** |
| Location | **1p31.3** |
| Product | Multi-pass transmembrane Wnt cargo receptor |
| Disease mechanism | Recessive hypomorphic/loss-of-function impairment of Wnt secretion |

## 4.2 Reported disease-associated variants

Transcript numbering differs between reports; therefore HGVS should be normalized against the laboratory’s selected MANE/reference transcript before clinical reporting.

| Variant as reported | Type/domain | Zygosity/report | Interpretation/evidence |
|---|---|---|---|
| **c.271G>A, p.Val91Met** | Missense, extracellular loop | Compound heterozygous | Likely pathogenic; functional reduction of WNT3A and β-catenin; reported population frequency 0.0001087 [Web:24] |
| **c.415C>T, p.Arg139Cys** | Missense, extracellular loop | Compound heterozygous, 2023 Chinese patient | Disease-associated; reduced WLS/WNT3A secretion in vitro [Web:28] |
| **c.1175A>G, p.Tyr392Cys** | Missense, sixth transmembrane domain | Homozygous in five Emirati siblings | ClinVar pathogenic; absent from gnomAD in the original report; reduced protein and Wnt secretion [Web:46] |
| **c.1427A>G, p.Tyr476Cys** | Missense; transcript-dependent numbering | Compound heterozygous Chinese patient | Reported disease-associated; paired with p.Arg139Cys [Web:34] |
| **c.1433A>G, p.Tyr478Cys** | Missense, eighth transmembrane domain | Homozygous in Egyptian and Native American families | ClinVar pathogenic; severe cellular and mouse functional evidence [Web:50] |
| **c.1579G>A, p.Gly527Arg** | Missense near C-terminal ER-targeting region | Homozygous | Likely disease-causing; severe multisystem phenotype, PMID 37106064 [Web:109] |
| **p.Ile531Thr** | Missense near ER-targeting motif | Homozygous | Disease-associated in original cohort |
| **c.1606C>T, p.Arg536Cys** | Missense in ER-targeting motif | Homozygous | ClinVar/OMIM pathogenic; WNT3A/WNT5A secretion reduced approximately 60% [Web:33] |
| **c.1279-1G>C** | Canonical splice-acceptor variant | Compound heterozygous | Pathogenic by PVS1+PM2+PP3+PP4; predicted splice disruption, but direct RNA assay was not reported [Web:24] |

All are **germline** variants. No somatic origin, repeat expansion or mitochondrial mechanism has been implicated.

## 4.3 Variant effects

- Transmembrane p.Tyr392Cys and p.Tyr478Cys reduced ectopically expressed WLS protein by roughly 50%.
- Patient p.Tyr478Cys fibroblasts had **>90% lower WLS protein** than control fibroblasts.
- Mutant cells secreted **60–80% less WNT3A/WNT5A** despite similar intracellular ligand abundance.
- TOPFlash Wnt reporter output fell **50–60%**.
- Mouse embryonic fibroblasts from both knock-in lines had approximately **40% lower WLS protein**. [Web:91]

The demonstrated mechanism is therefore predominantly **partial loss of function/hypomorphism**, not gain of function or dominant negative action.

## 4.4 Population frequency and penetrance

Most reported alleles are absent or extremely rare in reference databases; p.Val91Met was reported at 0.0001087. Because the condition is recessive, heterozygous carrier alleles can occur in unaffected people.

Penetrance appears high for individuals with two strongly deleterious alleles, but exact penetrance cannot be estimated from 13–14 reported patients. Expression is clearly variable.

## 4.5 Modifiers, epigenetics and chromosomal abnormalities

- No validated modifier gene is known.
- No syndrome-specific methylation signature or histone/chromatin abnormality has been reported.
- No recurrent deletion, duplication, inversion, translocation or aneuploidy defines the disease.
- Copy-number or regulatory variants affecting both WLS alleles remain theoretically possible but are not established causes.
- No founder allele has been formally demonstrated, although p.Tyr392Cys recurred within one consanguineous Emirati pedigree and p.Tyr478Cys occurred in more than one ancestry.

---

# 5. Environmental information

| Factor | Current evidence |
|---|---|
| Toxins/pollution/radiation | No causal association |
| Maternal medication | No established association |
| Smoking, alcohol, diet or exercise | No established disease-specific effect |
| Occupational exposure | No established effect |
| Infectious agent | None; this is not congenital Zika syndrome |
| Transmission | Genetic, not contagious |
| Gene–environment interaction | Unproven |
| Lifestyle modification of risk | Not applicable to disease occurrence once the biallelic genotype is present |

Environmental factors may influence general pregnancy or developmental outcomes, but none has been shown specifically to produce or prevent WLS-related Zaki syndrome.

---

# 6. Mechanism and pathophysiology

## 6.1 Ordered causal chain

1. **Biallelic hypomorphic or loss-of-function WLS variants lead to reduced WLS abundance, impaired trafficking, or defective cargo-receptor activity.**
2. **Defective WLS leads to reduced ER-to-Golgi-to-plasma-membrane transport and secretion of palmitoleated Wnt ligands.**
3. **Reduced extracellular Wnt availability leads to deficient canonical β-catenin and noncanonical Wnt signaling in Wnt-producing and neighboring cells.**
4. **Reduced developmental Wnt signaling leads to tissue-specific vulnerability according to each tissue’s Wnt dosage requirements and developmental timing.**
5. **In neural progenitors, deficient signaling leads to abnormal cell-cycle progression, with intermediate progenitors stalling in S and G2/M phases, resulting in reduced neurogenesis.**
6. **Reduced neurogenesis and abnormal cortical organization lead to small brain size, progressive microcephaly, developmental delay and intellectual disability.**
7. **Inferred branch—deficient craniofacial, ocular and ectodermal Wnt signaling leads to facial dysmorphism, coloboma/microphthalmia, sparse hair and dental anomalies.**
8. **Deficient limb-bud and somite/tail-bud signaling leads to syndactyly, ectrodactyly, digit-number abnormalities, vertebral/tail defects and skeletal dysplasia.**
9. **Deficient metanephric/renal-medullary Wnt signaling leads to renal agenesis, hydronephrosis or other renal malformations.**
10. **Deficient cardiac developmental signaling is inferred to lead to patent foramen ovale, patent ductus arteriosus and other congenital heart defects.**
11. **Experimental GSK3 inhibition by CHIR99021 leads to β-catenin stabilization downstream of WLS and results in partial rescue of embryoid-body and mouse developmental phenotypes.**

## 6.2 Molecular pathway detail

Wnt proteins are lipid-modified by PORCN in the ER. WLS binds the modified ligands, escorts them through the Golgi and secretory vesicles, and releases them at the plasma membrane. WLS is subsequently recycled through endosomes and the retromer system. It occupies the **ER, Golgi, vesicular/endosomal and plasma-membrane compartments**. [Web:85][Web:88]

Relevant ontology suggestions:

| Biological component/process | Suggested ontology term |
|---|---|
| Wnt signaling | GO:0016055 |
| Canonical Wnt signaling | GO:0060070 |
| Protein secretion | GO:0009306 |
| Intracellular protein transport | GO:0006886 |
| Vesicle-mediated transport | GO:0016192 |
| Neurogenesis | GO:0022008 |
| Cell cycle | GO:0007049 |
| Regulation of cell proliferation | GO:0042127 |
| Embryonic morphogenesis | GO:0048598 |
| Endoplasmic reticulum | GO:0005783 |
| Golgi apparatus | GO:0005794 |
| Endosome | GO:0005768 |
| Plasma membrane | GO:0005886 |

## 6.3 Cellular and tissue processes

### Nervous system

Single-nucleus RNA sequencing of embryonic mutant mouse brain demonstrated markedly reduced neurogenesis and abnormal cell-cycle progression in intermediate neural progenitors. Mutant brains showed reduced size, fewer cortical neurons, defective cortical lamination, ectopias, disrupted pial basement membrane and a severely defective hippocampal dentate gyrus. [Web:91]

Suggested cell terms:

- neural progenitor cell — **CL:0011020**;
- neuron — **CL:0000540**;
- cerebral-cortex neuron — use the appropriate subtype-specific CL term where known;
- fibroblast — **CL:0000057**;
- induced pluripotent stem cell — **CL:0002248**.

### Renal, limb and ectodermal development

Mouse findings and known ligand biology suggest:

- WNT7B-related signaling contributes to renal-medullary morphogenesis;
- WNT3A/WNT5A signaling contributes to somite, caudal-axis and limb morphogenesis;
- WNT10B-related biology is relevant to split-foot/digit development;
- epithelial Wls deletion in mice impairs hair growth.

These mappings are mechanistically plausible but do not establish that any one ligand alone causes each human phenotype.

## 6.4 Metabolic, immune and tissue-damage findings

- No primary metabolic-enzyme deficiency has been identified.
- No reproducible serum, urine, metabolomic, lipidomic or proteomic signature is available.
- Extensive biochemical testing in the first family was normal.
- No primary autoimmunity, immunodeficiency or chronic inflammatory mechanism is established.
- Tissue abnormalities primarily reflect altered developmental specification, proliferation and morphogenesis rather than ischemia, fibrosis or necrosis.
- No disease-specific epigenomic or spatial-transcriptomic dataset has been published.

## 6.5 Molecular profiling and advanced technologies

| Technology | Findings |
|---|---|
| Patient fibroblast proteomics/Western blot | >90% lower WLS in p.Tyr478Cys patient cells |
| Wnt secretion assays | 60–80% lower secreted WNT3A/WNT5A |
| TOPFlash reporter | 50–60% lower Wnt-responsive luciferase |
| Patient iPSC embryoid bodies | Approximately 50% smaller; size restored by CHIR99021 |
| Mouse single-nucleus RNA-seq | Reduced neurogenesis; intermediate progenitor cell-cycle arrest |
| Spatial transcriptomics | No disease-specific report |
| Human single-cell profiling | No report |
| CRISPR screen | No syndrome-specific screen identified |
| Metabolomics/lipidomics | No report |
| Multi-omics integration | No report |

---

# 7. Anatomical structures affected

| Level | Structure/system | Role | Suggested ontology |
|---|---|---|---|
| Organ | Brain | Primary; microcephaly, callosal/vermis defects, Dandy–Walker spectrum | UBERON:0000955 |
| Organ | Eye | Primary; coloboma, microphthalmia, microcornea, strabismus | UBERON:0000970 |
| Organ | Kidney | Primary congenital malformation; agenesis/hydronephrosis | UBERON:0002113 |
| Organ | Heart | Variable congenital defects | UBERON:0000948 |
| Organ/tissue | Skin and hair follicle | Sparse hair/alopecia | UBERON:0002097; UBERON:0002073 |
| Organ/tissue | Skeleton and limb | Syndactyly, ectrodactyly, fractures, scoliosis | UBERON:0002101 |
| Tissue | Cerebral cortex | Reduced neuron number, lamination defects in mice | UBERON:0000956 |
| Tissue | Cerebellar vermis | Hypoplasia | UBERON:0004728 |
| Tissue | Corpus callosum | Hypoplasia | UBERON:0002336 |
| Tissue | Hippocampal dentate gyrus | Severe reduction in mouse model | UBERON:0001885 |
| Tissue | Renal medulla/metanephros | Developmental vulnerability in mice | UBERON:0000362 |
| Craniofacial | Palate, jaw, nose, ears, lips | Dysmorphic features | Site-specific UBERON/FMA terms |
| Oral | Teeth, palate, jaw | Dental anomalies and high-arched palate | UBERON:0001091 |
| Genitourinary | Testis | Cryptorchidism in one reported patient | UBERON:0000473 |

Most findings are bilateral or midline. Eye coloboma, renal agenesis and limb anomalies can be unilateral or asymmetric; no consistent lateralization is established.

At subcellular level, WLS dysfunction involves the ER, Golgi, endosomes, secretory vesicles and plasma membrane.

---

# 8. Temporal development

## 8.1 Onset

The pathogenic process begins **prenatally during embryogenesis**. Structural malformations are congenital, but growth and neurodevelopmental features may emerge after birth.

Notably, the reviewed patients were generally reported to have term birth with normal birth weight, length and head circumference. Microcephaly and short stature often became evident during infancy or by two years. [Web:24]

## 8.2 Course

| Phase | Typical manifestations |
|---|---|
| Prenatal | Mild short femur or reduced fetal biometry may occur; renal, cardiac, eye or limb anomalies may be detectable |
| Neonatal | Congenital dysmorphism, syndactyly, eye/renal/cardiac malformations; head size may still be normal |
| Infancy | Emerging microcephaly, growth faltering, hypotonia, impaired visual response and developmental delay |
| Childhood | Persistent/progressive microcephaly and short stature; intellectual, speech and motor disability become clearer |
| Later childhood/adolescence | Mobility limitations, scoliosis, fracture risk or renal monitoring needs may become more apparent |
| Adult course | Essentially unknown because published cohorts are very small and predominantly pediatric |

The disorder is chronic and lifelong. It is not known to have relapsing–remitting episodes or spontaneous remission. Structural abnormalities generally do not regress, although patent foramen ovale, strabismus or surgically correctable skeletal defects may improve with standard care.

The principal inferred critical period is early embryogenesis, when Wnt signaling specifies organs and body pattern. Whether a later postnatal therapeutic window exists is unknown.

---

# 9. Inheritance and population

## 9.1 Epidemiology

No population prevalence or incidence estimate is available. The disorder is appropriately described as **ultra-rare**.

- 10 affected people from five families were reported in 2021.
- Additional 2023 cases raised the molecularly documented total.
- The literature review through October 2024 analyzed **13 patients with nine pathogenic/likely pathogenic variants**. [Web:24]
- No national registry, newborn-screening estimate or population carrier-frequency study exists.

A prevalence “per 100,000” cannot be calculated reliably from published case counts.

## 9.2 Mendelian inheritance

| Feature | Current conclusion |
|---|---|
| Mode | Autosomal recessive |
| Affected genotype | Homozygous or compound heterozygous pathogenic WLS variants |
| Recurrence risk | 25% affected, 50% carrier and 25% unaffected/noncarrier per pregnancy when both parents are carriers |
| Penetrance | Probably high for qualifying biallelic genotypes, but unquantified |
| Expressivity | Variable |
| Anticipation | Not expected; no repeat expansion |
| Germline mosaicism | Not reported, but low residual recurrence risk is theoretically possible after an apparently de novo variant |
| Consanguinity | Present in several original pedigrees but not required |
| Founder effect | Not established |
| Carrier phenotype | Heterozygous relatives in recessive families were clinically unaffected |
| Carrier frequency | Unknown |

A 2023 study found extremely rare **heterozygous** WLS missense variants among patients with isolated dental anomalies, but this does not yet establish a consistent dominant WLS disorder or imply that all Zaki-syndrome carriers have dental disease. PMID: **36374649**, published May 31, 2023. [Web:107][Web:108]

## 9.3 Demographics

No reliable male:female ratio is available. The condition has been reported across geographically and ancestrally diverse populations, arguing against restriction to one population. Ascertainment through consanguineous cohorts likely biases the currently observed distribution.

---

# 10. Diagnostics

## 10.1 Diagnostic principle

There are no consensus clinical criteria. Diagnosis requires:

1. compatible developmental/malformation phenotype;
2. identification of **two pathogenic or likely pathogenic WLS variants in trans**;
3. segregation analysis where possible;
4. functional RNA/protein assays when variant interpretation remains uncertain.

## 10.2 Recommended clinical evaluation

| Domain | Evaluation |
|---|---|
| Growth | Serial height, weight and occipitofrontal circumference plotted longitudinally |
| Development | Standardized cognitive, motor, language and adaptive assessment |
| Neurology | Neurologic examination; EEG only if seizures or concerning spells |
| Brain | MRI to assess corpus callosum, cerebellar vermis, fourth ventricle and Dandy–Walker spectrum |
| Ophthalmology | Dilated examination, optic-disc/iris evaluation, refraction, ocular alignment and visual-function testing |
| Renal | Renal/bladder ultrasound; blood pressure, serum creatinine/eGFR and urinalysis |
| Cardiac | Echocardiogram and ECG at diagnosis |
| Skeletal | Examination for syndactyly, ectrodactyly, scoliosis and limb-length abnormalities; radiographs as indicated |
| Bone health | Calcium, phosphate, alkaline phosphatase, vitamin D and DXA/radiographs if fractures or skeletal dysplasia |
| Dental | Early dental/orthodontic examination and panoramic imaging when age appropriate |
| Genital | Examination for cryptorchidism or other congenital anomalies |
| Hearing | Baseline audiology, although hearing loss is not a core established feature |
| Laboratory chemistry | No diagnostic biochemical assay; testing is directed by manifestations |

Biopsy is not routinely diagnostic. There is no validated circulating biomarker.

## 10.3 Genetic-testing strategy

- **Trio WES or WGS:** preferred when multiple congenital anomalies, microcephaly and developmental delay are unexplained. Both homozygous and compound-heterozygous WLS variants can be detected.
- **Multigene panels:** WLS should be included on developmental-disorder, microcephaly, eye-coloboma, fetal-anomaly, CAKUT, congenital-heart and Mendelian-disease panels. PanelApp lists WLS as a biallelic gene across several relevant panels. [Web:125]
- **Single-gene sequencing:** appropriate when the phenotype and family segregation strongly indicate Zaki syndrome; deletion/duplication analysis should be added if only one allele is found.
- **CMA:** useful for the general work-up of multiple congenital anomalies but does not reliably detect most reported WLS single-nucleotide variants.
- **Karyotype/FISH:** not first-line unless a cytogenetic abnormality is suspected.
- **RNA sequencing:** useful for suspected splice variants such as c.1279-1G>C, although this particular variant currently lacks direct patient-RNA confirmation.
- **mtDNA and repeat-expansion testing:** not specifically indicated.
- **Prenatal testing:** targeted familial-variant testing by CVS or amniocentesis; fetal exome/genome sequencing may be considered for multiple anomalies.
- **Preimplantation genetic testing:** technically feasible for known familial variants.

The early-diagnosis report recommends targeted skeletal panels for isolated short femur/skeletal findings and WES/WGS when additional structural anomalies are present. [Web:121]

## 10.4 Differential diagnosis

| Differential | Distinguishing considerations |
|---|---|
| DDX59-related Zaki–Gleeson syndrome | Severe microcephaly, cerebellar hypoplasia and cardiac conduction block; different gene and identifiers |
| Focal dermal hypoplasia/PORCN-related disorder | X-linked dominant, characteristic dermal hypoplasia and limb defects; mechanistically related Wnt-secretion defect |
| Robinow syndrome/WNT5A-pathway disorders | Mesomelia, genital and vertebral abnormalities; distinct gene/pathway phenotype |
| WNT10A/WNT10B disorders | Ectodermal/dental and limb phenotypes, usually without the full WLS multisystem pattern |
| Primary autosomal-recessive microcephaly | Microcephaly dominates, usually without characteristic eye/renal/limb constellation |
| Dandy–Walker spectrum disorders | Cerebellar malformation may dominate; WLS testing indicated when accompanied by sparse hair, syndactyly and progressive microcephaly |
| Chromatinopathies | Developmental delay and dysmorphism, but molecular testing distinguishes them |
| Microcephalic osteodysplastic primordial dwarfism | Severe prenatal/postnatal growth restriction and skeletal phenotype |
| Congenital infection, including Zika | Exposure/infection evidence; destructive rather than inherited WLS mechanism |
| Phenylketonuria/metabolic microcephaly | Biochemical abnormalities and newborn-screening findings |

## 10.5 Screening

There is no population or newborn screen. Appropriate screening consists of:

- cascade testing of at-risk relatives;
- carrier testing for reproductive partners in known families;
- prenatal or preimplantation testing after familial variants are established.

---

# 11. Outcome and prognosis

## 11.1 Survival

No five-year, ten-year, mortality-rate or life-expectancy data exist. Perinatal lethality occurred in **homozygous knock-in mice**, but should not be directly extrapolated to humans. Published human patients have survived into childhood and at least adolescence; a compound-heterozygous Chinese patient was reported at age 16. [Web:34]

There is currently no evidence that all affected people have markedly shortened life expectancy, but severe renal, cardiac, neurologic or skeletal complications could affect prognosis.

## 11.2 Morbidity

Expected long-term morbidity includes:

- intellectual, speech and motor disability;
- impaired vision;
- growth restriction and microcephaly;
- gait and mobility limitations;
- fracture or scoliosis complications in severe skeletal disease;
- reduced renal reserve after unilateral agenesis;
- need for congenital-heart surveillance;
- dental and orthodontic burden.

No formal ICF, EQ-5D, SF-36, PROMIS or disease-specific quality-of-life data exist.

## 11.3 Prognostic factors

Possible but unvalidated factors include:

- degree of residual WLS protein and Wnt secretion;
- variant location/domain;
- homozygous versus compound-heterozygous state;
- extent of brain, kidney, heart and eye malformations;
- early developmental trajectory.

Preliminary domain correlations suggested more wide mouth and fewer long digits with transmembrane variants, and more broad distal phalanges with variants near the ER-targeting motif. These analyses involved very small cell counts and multiple comparisons and must not be considered clinically predictive. [Web:24]

No validated prognostic biomarker or severity score exists.

---

# 12. Treatment

## 12.1 Current standard of care

There is **no approved disease-modifying therapy**. Management is individualized, multidisciplinary and phenotype-directed.

| Intervention | Indication | Suggested NCIt concept |
|---|---|---|
| Physical therapy | Hypotonia, delayed gross motor development, gait impairment | Physical Therapy, NCIt:C15308 |
| Occupational therapy | Fine-motor and self-care limitations | Occupational Therapy |
| Speech/language therapy | Speech and language delay; augmentative communication if needed | Speech Therapy, NCIt:C15313 |
| Developmental/educational intervention | Global delay and intellectual disability | Early Intervention |
| Ophthalmologic correction | Refraction, amblyopia, strabismus and visual rehabilitation | Ophthalmologic Procedure |
| Strabismus surgery | Selected significant ocular misalignment | Strabismus Surgery |
| Orthopedic/hand-foot surgery | Function-limiting syndactyly or severe limb deformity | Orthopedic Surgery |
| Scoliosis management | Observation, bracing or surgery according to standard criteria | Spinal Orthosis; Spinal Fusion |
| Fracture/bone-health management | Fractures or low bone density | Fracture Management |
| Cryptorchidism surgery | Undescended testis | Orchiopexy |
| Cardiology care | Hemodynamically important congenital defect | Cardiac Procedure |
| Renal surveillance | Agenesis, hydronephrosis or reduced function | Renal Function Assessment |
| Dental/orthodontic care | Tooth anomalies and malocclusion | Dental Procedure; Orthodontic Treatment |
| Seizure medication | Only when epilepsy is documented | Anticonvulsant Therapy |
| Genetic counseling | Recurrence risk and reproductive options | Genetic Counseling, NCIt:C15238 |

No disease-specific pharmacogenomic recommendations exist.

## 12.2 Experimental Wnt-pathway therapy

**CHIR99021** is a small-molecule GSK3 inhibitor that stabilizes β-catenin and enhances canonical Wnt transcription. In patient-derived embryoid bodies, it restored reduced body size. In pregnant knock-in mice, twice-daily intraperitoneal administration beginning at embryonic day 4.5 produced:

- near-complete tail rescue in p.Tyr478Cys mice and partial rescue in p.Tyr392Cys mice;
- reduction of hydronephrosis from **75.0% to 22.7%**;
- 16.4% greater dorsoventral brain width;
- 14.3% greater cortical thickness;
- 25.4% more CUX1-positive neurons;
- 16.0% more CTIP2-positive neurons;
- 150.3% more dentate-gyrus cells. [Web:91]

The paper concluded:

> “Administration of a pharmacologic Wnt agonist partially restored embryonic development.”  
> — Chai et al., 2021; PMID 34587386. [Web:32]

This is **preclinical evidence only**. Systemic prenatal activation of Wnt signaling could disrupt embryogenesis or promote tumorigenic processes, so CHIR99021 should not be used clinically outside appropriately reviewed research. The authors expressly stated that maternal and fetal safety requires careful study. [Web:91]

## 12.3 Advanced therapeutics and trials

| Modality | Status |
|---|---|
| Gene replacement | No clinical program identified |
| CRISPR/gene editing | No clinical program identified |
| Antisense/siRNA/mRNA | No clinical program identified |
| Cell therapy | No indication or trial |
| Immunotherapy | Not mechanistically indicated |
| Approved targeted drug | None |
| Registered Zaki-syndrome interventional trial | None identified |
| Human CHIR99021 trial | None identified for this disease |
| NIH research | R01HD119284 studies Wntless mechanisms; it lists no clinical study [Web:93] |

---

# 13. Prevention

## 13.1 Primary prevention

Because the disease is genetic, smoking cessation, diet, exercise, vaccination and environmental remediation do not specifically prevent it.

For known carrier couples, primary reproductive options include:

- preconception genetic counseling;
- partner testing;
- IVF with preimplantation genetic testing for monogenic disease;
- use of donor gametes;
- prenatal diagnosis by CVS or amniocentesis.

## 13.2 Secondary prevention/early detection

- Cascade carrier testing in relatives.
- Early WES/WGS in infants with progressive microcephaly plus eye, hair, limb, renal or cardiac abnormalities.
- Prenatal ultrasound surveillance for growth, limb, renal, cardiac and CNS anomalies in at-risk pregnancies.
- Early ophthalmology, neurodevelopmental, renal and cardiac evaluation after diagnosis.

There is no general-population carrier or newborn-screening program.

## 13.3 Tertiary prevention

Tertiary measures include:

- amblyopia prevention and visual rehabilitation;
- early developmental therapies;
- renal-protective monitoring and avoidance of unnecessary nephrotoxins in patients with solitary kidney;
- treatment of scoliosis and bone fragility;
- timely orchiopexy;
- management of congenital heart disease;
- fall and fracture prevention;
- educational, mobility and communication supports.

No vaccine, antimicrobial prophylaxis or public-health sanitation measure is relevant to disease prevention.

---

# 14. Other species and natural disease

| Topic | Evidence |
|---|---|
| Naturally occurring veterinary Zaki syndrome | No confirmed naturally occurring WLS-associated homologous syndrome identified |
| Companion-animal breed predisposition | None established |
| Zoonotic potential | None |
| Cross-species transmission | Not applicable |
| Evolutionary conservation | WLS/Wntless function is strongly conserved across metazoans |
| Mouse | *Mus musculus*, NCBI Taxon **10090**; Wls knock-in and conditional models |
| Fruit fly | *Drosophila melanogaster*, Taxon **7227**; *wls/evi/sprinter* controls Wingless secretion and retromer-dependent recycling |
| Human | *Homo sapiens*, Taxon **9606** |

Wntless biology was initially delineated in invertebrate and cellular systems. Drosophila studies show that Wls is a multi-pass transmembrane protein required for Wingless secretion and recycled from endosome to Golgi by the retromer. [Web:86]

There is no infectious transmission, zoonosis or veterinary public-health relevance.

---

# 15. Model organisms and experimental models

| Model | Type | Key findings | Strengths | Limitations |
|---|---|---|---|---|
| Wls p.Tyr392Cys knock-in mouse | Mammalian, precise genetic model | Approximately 40% lower WLS in fibroblasts; neural-tube, tail, vertebral, digit, kidney and brain defects; perinatal lethality | Human-allele-specific; permits prenatal treatment studies | More severe/lethal than reported human course |
| Wls p.Tyr478Cys knock-in mouse | Mammalian, precise genetic model | Global Wnt-reporter reduction; hydronephrosis, reduced digits, microbrain, cortical and hippocampal abnormalities | Strong phenotype recapitulation; single-nucleus profiling | Species and dosage differences |
| TCF/Lef:H2B-GFP reporter cross | Mouse pathway reporter | Reduced Wnt activity in face, heart, spine, tail bud, metanephros and neural tissues | Anatomical mapping of pathway deficit | Reporter reflects selected canonical Wnt outputs |
| Patient fibroblasts | Human primary cells | >90% lower WLS in p.Tyr478Cys cells; impaired Wnt secretion | Direct patient evidence | Limited developmental context |
| WLS-null HEK293T complementation | Human in-vitro functional assay | Mutant WLS caused 60–80% lower WNT3A/WNT5A secretion and 50–60% lower TOPFlash output | Quantitative variant-function testing | Artificial overexpression/cell-line context |
| Patient-derived iPSCs | Human cellular model | Mutant iPSCs viable | Genetically patient-specific | Do not independently reproduce organogenesis |
| Patient-derived embryoid bodies | Human 3-D in-vitro model | Approximately 50% smaller; size restored with CHIR99021 | Models early pregastrulation-like development and drug response | Not an intact embryo or organ |
| Mouse single-nucleus RNA-seq | Advanced molecular model | Reduced neurogenesis and S/G2-M stalling in intermediate progenitors | Cell-type-resolved mechanism | Embryonic mouse brain only |
| Conditional epidermal Wls knockout | Mammalian induced genetic model | Hair-growth defect | Supports ectodermal mechanism | Not a full Zaki-syndrome model |
| Drosophila wls/evi models | Invertebrate genetic model | Defective Wingless secretion and retromer recycling | Highly tractable and evolutionarily conserved | Limited correspondence to human organs |

The mouse models reproduce nervous-system, kidney and limb abnormalities especially well. They also demonstrate that different tissues have different Wnt-dose thresholds. Their perinatal lethality and severe caudal defects indicate that they may model the severe end of the human allelic spectrum rather than the average reported patient. [Web:91]

---

# Evidence appraisal and research gaps

## Strong evidence

- Biallelic **WLS** variants cause Zaki syndrome.
- WLS variants reduce WLS protein stability/function and Wnt secretion.
- The condition is autosomal recessive and multisystem.
- Knock-in mice reproduce major developmental abnormalities.
- CHIR99021 can partially rescue cellular and prenatal mouse phenotypes.

## Moderate evidence

- Progressive postnatal microcephaly, distinctive facial features, neurodevelopmental impairment, sparse hair, eye and skeletal anomalies are core phenotypes.
- Renal and cardiac defects are recurrent but incompletely penetrant.
- Compound-heterozygous alleles can cause disease.

## Preliminary or uncertain

- Variant-domain/genotype–phenotype correlations.
- A systematically milder compound-heterozygous course.
- Umbilical polyps as part of the phenotype.
- Dominant dental effects in heterozygous carriers.
- Human efficacy or safety of prenatal Wnt agonism.
- Adult natural history, survival, fertility and life expectancy.

## Highest-priority research needs

1. International registry and longitudinal natural-history cohort.
2. Standardized developmental, ophthalmic, renal, skeletal and quality-of-life outcomes.
3. Systematic reanalysis of WLS variants using a single reference transcript.
4. RNA studies for splice variants and assays for all newly reported alleles.
5. Human neural, renal and ocular organoid models.
6. Maternal–fetal toxicology and dose-window studies of pathway modulation.
7. Investigation of safer tissue-selective or temporally restricted Wnt rescue.
8. Adult follow-up, reproductive outcomes and penetrance studies in carrier families.

---

## Key literature

| Publication | Date | Evidence type | Key contribution |
|---|---|---|---|
| Chai et al. **A Human Pleiotropic Multiorgan Condition Caused by Deficient Wnt Secretion.** *N Engl J Med.* 2021;385:1292–1301. PMID **34587386**. DOI: 10.1056/NEJMoa2033911. [PubMed URL](https://pubmed.ncbi.nlm.nih.gov/34587386/) | September 30, 2021 | Human clinical, in vitro, iPSC and mouse | Disease discovery; 10 patients/5 families; mechanism and prenatal mouse rescue [Web:32] |
| Yu et al. **Compound heterozygous variants in WLS gene causes Zaki syndrome.** *Clin Genet.* 2023;104:226–229. PMID **37005218**. DOI: 10.1111/cge.14334. [PubMed URL](https://pubmed.ncbi.nlm.nih.gov/37005218/) | August 2023; online April 2, 2023 | Human case and in vitro | First reported Chinese case and compound-heterozygous alleles [Web:34] |
| **Expanding the phenotypic spectrum and clinical severity associated with WLS gene.** *J Hum Genet.* 2023;68:607–613. PMID **37106064**. DOI: 10.1038/s10038-023-01152-2. [PubMed URL](https://pubmed.ncbi.nlm.nih.gov/37106064/) | September 2023; online April 28, 2023 | Human case | p.Gly527Arg; Dandy–Walker malformation, microphthalmia, dental anomalies, fractures [Web:109] |
| Kantaputra et al. **Mutations in the WLS are associated with dental anomalies, torus palatinus, and torus mandibularis.** *Eur J Orthod.* 2023;45:317–323. PMID **36374649**. DOI: 10.1093/ejo/cjac068. [Article URL](https://academic.oup.com/ejo/article/45/3/317/6827302) | May 31, 2023 | Human case series | Possible heterozygous WLS contribution to dental phenotypes [Web:107] |
| **Early diagnosed Zaki syndrome: identification of two novel WLS variants and a literature review.** *Italian Journal of Pediatrics.* [Full-text URL](https://pmc.ncbi.nlm.nih.gov/articles/PMC12229024/) | July 5, 2025 | Human infant, functional assay and review through October 2024 | p.Val91Met and c.1279-1G>C; 13-patient aggregate frequency analysis [Web:24] |

**Overall conclusion:** Zaki syndrome is a newly delineated, ultra-rare, autosomal-recessive Wnt-secretion disorder with strong human genetic and functional evidence implicating **WLS loss of function**. Present care is supportive and surveillance-based. Prenatal Wnt-pathway rescue is biologically compelling but remains confined to cellular and mouse models and is not ready for clinical use.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

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
