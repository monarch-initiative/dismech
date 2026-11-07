---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-22T13:25:31.747311'
end_time: '2026-10-22T13:30:23.863817'
duration_seconds: 292.12
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Neurodevelopmental Disorder With Microcephaly And Structural Brain
    Anomalies
  mondo_id: MONDO:0032779
  category: Mendelian
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: not recorded
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
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder With Microcephaly And Structural Brain Anomalies
- **MONDO ID:** MONDO:0032779 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder With Microcephaly And Structural Brain Anomalies** covering all of the
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

# Comprehensive research report: Neurodevelopmental disorder with microcephaly and structural brain anomalies

**Neurodevelopmental disorder with microcephaly and structural brain anomalies (NEDMIBA) is caused by biallelic pathogenic variants in *DYNC1I2*, not *SMPD4*.** It is an exceptionally rare autosomal-recessive neurodevelopmental disorder characterized by congenital or early progressive microcephaly, developmental delay/intellectual disability, dysmorphic facial features, and a reproducible neuroimaging pattern involving simplified cortical gyration, reduced cerebral white matter, and hypogenesis or agenesis of the corpus callosum. The relevant identifiers are **MONDO:0032779** and **OMIM:618492**; the similarly named *SMPD4*-related disorder includes **arthrogryposis** and is a different condition, OMIM:618622. [MedGen](https://www.ncbi.nlm.nih.gov/medgen/C5193123) and OMIM explicitly associate MONDO:0032779/OMIM:618492 with *DYNC1I2* at 2q31.1. [17][86]

**Evidence cut-off:** 22 October 2026. The disease-specific evidence base remains extremely small: the defining 2019 report contains five individuals from three families, and a 2024 Pakistani cohort republishes the same c.607+1G>A family/phenotype rather than clearly establishing a new independent series. Consequently, percentages below are descriptive—not reliable population-frequency estimates. [40][255]

---

## 1. Disease information

### Definition

NEDMIBA is a syndromic disorder of prenatal/early brain development caused by loss or marked impairment of the cytoplasmic dynein-1 intermediate-chain protein DYNC1I2. The defining human study reported:

> “three unrelated families comprising five affected individuals with an overlapping, complex neurodevelopmental disorder characterized by microcephaly, intellectual disability, cerebral malformations, and dysmorphic facial features.”

Ansar et al., *American Journal of Human Genetics*, published online 9 May 2019; 104:1073–1087; DOI: [10.1016/j.ajhg.2019.04.002](https://doi.org/10.1016/j.ajhg.2019.04.002); **PMID:31079899**. [40]

### Identifiers and nomenclature

| Resource | Identifier/name | Status and interpretation |
|---|---|---|
| MONDO | **MONDO:0032779** | Target identifier specified in the query; maps to *DYNC1I2*-related NEDMIBA. [17] |
| OMIM disease | **618492** | Neurodevelopmental disorder with microcephaly and structural brain anomalies; autosomal recessive. [86] |
| OMIM gene | **603331** | *DYNC1I2*. [46] |
| MedGen | **C5193123**, UID 1677276 | NEDMIBA; gene *DYNC1I2*. [35] |
| UMLS | **C5193123** | Through the MedGen concept record. [17] |
| MeSH | **D065886** | A broader neurodevelopmental-disorders heading, not a uniquely disease-specific identifier. [105] |
| Orphanet |  | No dedicated ORPHA record was located for *DYNC1I2*-NEDMIBA. |
| ICD-10/ICD-11 |  | No disease-specific code located. Coding normally uses manifestations such as developmental disorder/intellectual disability, congenital microcephaly, epilepsy, and corpus-callosum malformation. |
| GeneReviews |  | No disease-specific GeneReviews chapter; NCBI explicitly lists “GeneReviews: Not available.” [39] |
| Common abbreviation | **NEDMIBA** | Neurodevelopmental disorder with microcephaly and structural brain anomalies. [33] |
| Published descriptive synonym | **DYNC1I2-related syndromic microcephaly** | Useful but not a separate ontology entry. |

### Source granularity

The evidence comes from:

1. **Individual-level human clinical data:** pedigrees, examinations, MRI, WES/CMA and segregation in five deeply described patients.
2. **Aggregated disease resources:** OMIM, MedGen, MONDO, ClinVar and HPO largely summarize those same individuals.
3. **Experimental evidence:** CRISPR/morpholino zebrafish and human-mRNA complementation.

It is **not** based on population EHRs, registries, natural-history cohorts or controlled clinical studies.

---

## 2. Etiology

### Primary causal factor

The established cause is **germline biallelic *DYNC1I2* dysfunction**:

- Homozygous canonical splice-site variant;
- Compound heterozygous nonsense plus missense variants;
- Compound heterozygosity for a missense allele and a deletion encompassing *DYNC1I2*.

The inheritance and segregation pattern is autosomal recessive. OMIM recognizes homozygous and compound-heterozygous *DYNC1I2* variants as causal. [86][277]

### Risk and protective factors

| Factor class | Current evidence |
|---|---|
| Pathogenic genetic risk | Two pathogenic/likely pathogenic alleles in *DYNC1I2*. Loss-of-function is the best-supported mechanism. |
| Consanguinity | Increases the probability that both parents carry the same rare allele. The original Pakistani family involved third-cousin parents; this is a reproductive risk factor, not a biological modifier of severity. |
| Family history | An affected sibling or known parental carrier status substantially raises recurrence risk. |
| Sex | No established sex effect; the defining five patients comprised two males and three females. |
| Ancestry/founder effect | c.740A>G, p.Tyr247Cys was present in four heterozygous Ashkenazi Jewish individuals in the historical gnomAD dataset, but no founder effect was demonstrated. c.607+1G>A occurred in a consanguineous Pakistani family; population-specific enrichment has not been established. |
| Environmental, infectious or lifestyle risk | None demonstrated for genetically confirmed NEDMIBA. Prenatal infection, toxins and nutritional factors are important differential causes of microcephaly but are not known causes or modifiers of *DYNC1I2*-NEDMIBA. |
| Protective variants/modifier genes | None reported. |
| Protective diet, medication or exposure | None known. |
| Gene–environment interaction | Not studied. |

The 2024 Pakistani NDD cohort again classified homozygous c.607+1G>A as pathogenic and associated it with microcephaly, short stature, developmental delay, impaired intellect, aggressive behavior and facial dysmorphism. Because the authors and family description overlap the 2019 report, this should be treated as confirmatory re-reporting, not as an independent prevalence estimate. Paracha et al., 30 August 2024, DOI: [10.3389/fmed.2024.1424753](https://doi.org/10.3389/fmed.2024.1424753), **PMID:39281811**. [255][302]

---

## 3. Phenotypes

### Cohort-level phenotype table

Frequencies are calculated from the five individuals in PMID:31079899. “3/3 MRI” means that only three patients underwent or had reported MRI.

| Phenotype type | Clinical phenotype and HPO suggestion | Onset/severity/course | Observed frequency | Functional or quality-of-life impact |
|---|---|---|---:|---|
| Sign | Microcephaly — **HP:0000252** | Congenital in the two infants with detailed birth data; postnatal head growth can fall progressively farther below the mean; severe, down to −6.67 SD | **5/5** | Correlates with major cognitive and motor disability; requires serial growth and neurologic surveillance. |
| Developmental | Global developmental delay — **HP:0001263** | Infancy/early childhood; severe and lifelong | **5/5** | Delayed motor, language, adaptive and cognitive function; dependence on caregivers. |
| Cognitive | Intellectual disability — **HP:0001249**; severe ID **HP:0010864** | Childhood onward; severe in the three adults | **5/5** | Major limitation of education, independent living and decision-making. |
| Developmental | Delayed speech/language — **HP:0000750** | Early childhood; persistent | **5/5** | Dysarthric or very limited communication; one child used a few signs at 25 months. |
| Developmental | Motor delay — **HP:0001270** | Infancy; variable but marked | **5/5** | One child remained unable to walk at 25 months; long-term ambulation data are sparse. |
| Physical | Facial dysmorphism — **HP:0001999** | Congenital, stable | **5/5** | Primarily diagnostic; no direct functional burden shown. |
| MRI sign | Simplified gyral pattern — **HP:0009879** | Congenital developmental malformation; apparently non-episodic | **3/3 MRI** | Marker of abnormal cortical development and severe neurodevelopmental impairment. [225] |
| MRI sign | Corpus-callosum agenesis — **HP:0001274**, or hypoplasia — **HP:0002079** | Congenital; near-complete, partial or hypogenetic | **3/3 MRI** | Likely contributes to impaired interhemispheric connectivity, cognition and motor function. [226][238] |
| MRI sign | Reduced cerebral white-matter volume/white-matter hypoplasia | Congenital/early developmental | **3/3 MRI or narrative** | Likely affects long-range connectivity; no disease-specific tractography studies. |
| MRI sign | Ventricular enlargement/colpocephaly | Congenital/secondary to callosal and white-matter abnormalities | At least **2/3 MRI** | Imaging marker; clinical effect cannot be separated from the broader brain malformation. |
| MRI sign | Cerebral cortical and brainstem hypoplasia | Congenital | Explicit in the imaged adult; broader OMIM summary includes both | Likely contributes to global neurologic disability. |
| Neurologic sign | Seizures — **HP:0001250** | Infancy in both reported children; course and seizure type not specified | **2/5** | Risk of injury, hospitalization and additional developmental burden. |
| Neurologic sign | Spasticity — **HP:0001257** | Infancy/childhood; diffuse in one child | **1/5** | Impairs mobility, positioning and care; risk of contractures. |
| Neurologic sign | Hypotonia — **HP:0001252** | Present at 25 months in one child | **1/5** | Contributes to gross-motor and postural delay. |
| Neurologic sign | Hyperreflexia — **HP:0001347** | First year/early childhood | **1/5** | Upper-motor-neuron sign; may precede or coexist with abnormal tone. |
| Behavioral | ADHD — **HP:0007018**; aggressive behavior — **HP:0000718** | Childhood/adulthood; persistent in reported siblings | **3/5** | Family stress, safety and participation limitations. |
| Speech sign | Dysarthria — **HP:0001260**; hypernasal speech | Childhood/adulthood | **3/5** | Reduces intelligibility and functional communication. |
| Growth | Short stature — **HP:0004322** | Childhood/adult | **3/5 clearly documented** | May affect mobility/equipment needs; no endocrine mechanism established. |
| Musculoskeletal | Joint hypermobility — **HP:0001382** | Infancy/childhood | **1/5** | Potential joint instability; isolated observation. |
| Auditory | Unilateral hearing impairment — **HP:0000365**, due to cochlear malformation | Congenital/infancy | **1/5** | Communication burden; requires audiologic support. |
| Gastrointestinal | Gastroesophageal reflux — **HP:0002020** | First year | **1/5** | Feeding discomfort, aspiration and growth risk. |
| Endocrine | Hypothyroidism — **HP:0000821** | Infancy/childhood, timing unspecified | **1/5** | Treatable contributor to growth and developmental problems; may be coincidental. |
| Vascular/skin | Multiple hemangiomas — **HP:0001028** | Infancy | **1/5** | Uncertain relationship to *DYNC1I2*. |
| Infectious/ENT | Recurrent otitis media and upper respiratory infections | First year | **1/5** | Hearing and respiratory morbidity; no primary immunodeficiency demonstrated. |

Core HPO annotations in MedGen include microcephaly, global developmental delay, simplified gyral pattern, short stature, spasticity and hypotonia. [87]

### Facial phenotype

Reported features include:

- Upslanting palpebral fissures — HP:0000582;
- Anteverted nares — HP:0000463;
- Bulbous nose — HP:0000414;
- Sloping forehead;
- Prominent eyes/nose;
- Irregular ear helices.

### Patient-level severity

- The three Pakistani siblings survived to **20, 32 and 34 years**, with severe intellectual disability, delayed speech and motor milestones, short stature and behavioral problems.
- The European/Ashkenazi male had congenital microcephaly, diffuse spasticity, seizures and complex callosal agenesis.
- The Eastern European female’s head circumference progressed from −2.07 SD at birth to −6.37 SD at four months and −6.67 SD at 25 months; she was social and had a pincer grasp and a few signs but could not walk at 25 months.

No EQ-5D, SF-36, PROMIS, caregiver-burden or disease-specific quality-of-life instrument has been used.

---

## 4. Genetic and molecular information

### Gene and protein

| Field | Value |
|---|---|
| Gene | ***DYNC1I2***, dynein cytoplasmic 1 intermediate chain 2 |
| HGNC | **HGNC:2964** |
| NCBI Gene | **1781** |
| OMIM gene | **603331** |
| Ensembl | **ENSG00000077380** |
| UniProt | **Q13409** |
| Cytogenetic location | **2q31.1** |
| GRCh38 location | chr2:171,687,469–171,750,158, plus strand |
| MANE/clinical transcript | **NM_001378.3**; original report used NM_001378.2 |
| Protein | Cytoplasmic dynein 1 intermediate chain 2; non-catalytic accessory component of the cytoplasmic dynein-1 motor |
| Main function | Links dynein to cargo/adaptor proteins and supports minus-end-directed microtubule transport of organelles and vesicles |

NCBI describes DYNC1I2 as a non-catalytic component of cytoplasmic dynein-1, and reports multiple alternatively spliced transcripts. [47][332] UniProt Q13409 assigns cytoplasmic/cytoskeletal localization and cargo/adaptor-linking function. [140]

### Established disease alleles

| Variant, original transcript | Type/origin | Patients and phase | Population data at publication | Functional/classification evidence |
|---|---|---|---|---|
| **NM_001378.2:c.607+1G>A**; current NM_001378.3 nomenclature unchanged | Germline canonical splice-donor SNV | Homozygous in three Pakistani siblings; segregated in recessive pedigree | Absent from 300 local controls and gnomAD | Predicted loss of function; patient RNA unavailable. ClinVar **pathogenic**, Variation ID 635399. [94][337] |
| **c.740A>G, p.Tyr247Cys** | Germline missense | In trans with a 374-kb deletion in one patient; in trans with p.Gln290Ter in another | Historical gnomAD MAF **1.8×10⁻⁵**; four heterozygotes, reported as Ashkenazi Jewish; no homozygotes cited | Highly conserved; structural modeling predicts impaired interactions; human mutant mRNA failed to rescue zebrafish knockdown. ClinVar **pathogenic**, Variation ID 635400. [294] |
| **c.868C>T, p.Gln290Ter** | Germline nonsense | In trans with p.Tyr247Cys in one patient | Absent from gnomAD in the defining study | Premature termination, predicted truncated/absent protein; failed zebrafish rescue. ClinVar **pathogenic**, Variation ID 635401. [93][339] |
| **arr[hg19] 2q31.1(172,318,311–172,692,048)×1** | Germline 374-kb deletion | Paternally inherited; in trans with maternal p.Tyr247Cys | Not previously represented in DECIPHER at publication | Deletes *DCAF17, CYBRD1, DYNC1I2* and *SLC25A12*. The phenotype implicates *DYNC1I2*, but contributions from other deleted genes cannot be completely excluded. |

All are constitutional/germline. Somatic mosaic disease has not been reported.

### Consequences and uncertainties

- **Primary mechanism:** partial or complete loss of DYNC1I2 function.
- **p.Tyr247Cys:** best interpreted as a hypomorphic/damaging loss-of-function missense allele, not demonstrated gain of function.
- **Splice variant:** predicted loss of normal splicing but not RNA-confirmed.
- **Dominant-negative mechanism:** not supported.
- **Modifier genes:** none established.
- **Epigenetic signature:** no methylation episignature or disease-specific chromatin alteration reported.
- **Large chromosomal lesions:** only the heterozygous 374-kb deletion above; no recurrent deletion syndrome is established.
- **ClinGen:** no disease-specific expert-panel gene-validity or dosage-sensitivity classification was located.
- **HGMD:** access-dependent; no additional independently validated published disease alleles were identified in the open literature.

---

## 5. Environmental information

No toxin, radiation, pollutant, medication, nutritional deficiency, alcohol exposure, smoking exposure, occupational factor or infectious agent is known to cause genetically confirmed NEDMIBA.

Environmental and infectious histories remain clinically important because congenital infections—such as cytomegalovirus, Zika virus and toxoplasmosis—and prenatal teratogens can produce microcephaly and structural brain anomalies. Those are **differential diagnoses**, not established *DYNC1I2* gene–environment interactions.

There is likewise no evidence that exercise, diet, vitamins, vaccination or avoidance of a particular exposure changes penetrance or severity after conception.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function or damaging *DYNC1I2* variants lead to reduced or dysfunctional DYNC1I2 intermediate-chain activity.**
2. **DYNC1I2 dysfunction leads to impaired assembly/regulation of the cytoplasmic dynein-1 cargo-transport complex** and probably weakens intermediate-chain interactions with dynein heavy/light chains and dynactin.
3. **Impaired dynein function leads to abnormal mitotic-spindle morphology and delayed/prolonged mitosis**—demonstrated in zebrafish *dync1i2a* knockdown, but not yet in patient-derived neural progenitors.
4. **Prolonged mitosis leads to increased apoptosis**—supported by increased phospho-histone-H3- and TUNEL-positive cells in zebrafish and rescue by human wild-type *DYNC1I2* mRNA.
5. **Increased progenitor-cell loss is inferred to lead to reduced production/survival of developing neural cells**, resulting in congenital and postnatal microcephaly.
6. **In parallel, disturbed dynein-dependent intracellular and axonal transport leads to disorganized axon tracts and reduced midline crossing** in zebrafish.
7. **Disrupted progenitor survival plus axonal organization is inferred to result in simplified cortical gyration, reduced white matter and corpus-callosum hypogenesis/agenesis.**
8. **These structural and connectivity abnormalities lead to developmental delay, intellectual disability, motor impairment, abnormal tone, speech impairment and seizures.**
9. **A craniofacial-development branch leads to altered cartilage patterning and facial dysmorphism**, demonstrated as increased ceratohyal angle in zebrafish but only indirectly linked to human facial findings.

The authors’ key abstract statement was:

> “We monitored cell death and cell cycle progression in *dync1i2a* zebrafish models and observed significantly increased apoptosis, likely due to prolonged mitosis caused by abnormal spindle morphology.”

PMID:31079899. [36]

### Molecular and cellular detail

DYNC1I2 is one of the two human cytoplasmic dynein-1 intermediate chains. Dynein-1 consists of force-generating DYNC1H1 heavy chains plus intermediate, light-intermediate and light chains. DYNC1I2 helps couple this motor to dynactin, cargo and adaptor proteins. NCBI annotations place it in the cytoplasmic dynein complex, centrosome, microtubules, cytoplasm and cytoskeleton. [142]

The p.Tyr247 residue lies in a linker near WD40 structural elements. Modeling suggested that substitution with cysteine could remove normal tyrosine interactions, create inappropriate disulfide interactions during folding, impair dimerization, or weaken binding to other dynein components. This remains a structural prediction rather than a direct biochemical measurement.

### Experimental effect sizes

In zebrafish:

- F0 CRISPR disruption of *dync1i2a* reduced head area by **7%** and increased ceratohyal angle by **5°**.
- Splice-blocking morpholino reduced head size by **10%** and increased ceratohyal angle by **30°** at the highest tested dose.
- Knockdown increased TUNEL-positive apoptotic cells and phospho-histone-H3-positive mitotic cells.
- Prophase/metaphase spindle abnormalities increased.
- Wild-type human mRNA rescued head, craniofacial, apoptosis and neural-patterning phenotypes.
- p.Tyr247Cys-equivalent and p.Gln290Ter-equivalent mRNAs did not rescue.
- Disruption of the second paralog, *dync1i2b*, did not produce the same head phenotype.

ZFIN recognizes the CRISPR and morpholino *dync1i2a* models as experimental models of autosomal-recessive primary microcephaly. [120]

### Pathways, cell types and ontology suggestions

| Level | Suggested ontology annotations |
|---|---|
| Molecular function | Dynein heavy-chain binding; dynein light-chain binding; cargo/adaptor coupling |
| Biological process | Microtubule-based movement — **GO:0007018**; retrograde axonal transport — **GO:0008090**; mitotic spindle organization — **GO:0007052**; apoptotic process — **GO:0006915**; nervous-system development — **GO:0007399** |
| Cellular component | Cytoplasmic dynein complex — **GO:0030286**; microtubule — **GO:0005874**; centrosome — **GO:0005813**; cytoplasm — **GO:0005737**; cytoskeleton — **GO:0005856**; mitotic spindle — **GO:0072686** |
| Primary inferred vulnerable cell | Neural progenitor cell — **CL:0011020** [244] |
| Downstream cell | Central nervous system neuron — **CL:2000029**; neuroblast — **CL:0000337** [240] |
| Additional plausible cell types | Developing callosal projection neuron, cortical excitatory neuron, oligodendrocyte-lineage cell; these have not been directly tested in NEDMIBA |

No disease-specific patient transcriptomics, single-cell RNA sequencing, spatial transcriptomics, proteomics, metabolomics, lipidomics, patient iPSC, cortical-organoid or CRISPR-screen dataset has been published. There is also no demonstrated primary immune, inflammatory, metabolic or mitochondrial mechanism.

---

## 7. Anatomical structures affected

| Scale | Structures | Evidence and ontology suggestions |
|---|---|---|
| Organ/system | Central nervous system/brain | Primary affected organ; **UBERON:0000955** brain |
| Cortex | Cerebral cortex, bilateral but sometimes asymmetric gyral simplification | **UBERON:0000956** cerebral cortex. [248] |
| Commissural white matter | Corpus callosum—rostrum, genu, body and splenium | Hypogenesis, partial agenesis or near-complete agenesis; **UBERON:0002336** corpus callosum. [242] |
| Cerebral white matter | Reduced cortical/cerebral white-matter volume | Present across imaged patients; candidate annotation: cerebral white matter |
| Brainstem | Brainstem hypoplasia | Clearly reported in one adult and summarized in OMIM |
| Ventricular system | Colpocephaly, prominent ventricles, enlarged posterior horns/large trigones | Likely secondary to callosal and white-matter maldevelopment |
| Posterior fossa | Mega cisterna magna | One patient |
| Cochlea | Unilateral structural cochlear defect | One patient; association remains uncertain |
| Musculoskeletal system | Abnormal tone and joint hypermobility | Probably secondary neurologic involvement rather than primary muscle disease |
| Subcellular | Cytoplasmic dynein complex, microtubules, centrosome, mitotic spindle, vesicles | Direct protein and model-organism evidence |

The brain abnormalities are generally bilateral/midline. One adult had more pronounced gyral simplification in the right hemisphere, but systematic lateralization has not been established.

---

## 8. Temporal development and natural history

### Onset and course

- **Prenatal/congenital:** brain malformations originate during fetal neurodevelopment. Congenital microcephaly was documented in both infants with detailed birth information.
- **Early postnatal:** head growth may progressively decelerate. One child changed from −2.07 SD at birth to −6.67 SD by 25 months.
- **Infancy:** global developmental delay, seizures, abnormal reflexes/tone, reflux and poor head growth may become apparent.
- **Childhood and adulthood:** intellectual, language, motor and behavioral disabilities persist.
- **Duration:** lifelong.
- **Remission:** no spontaneous or treatment-induced remission reported.
- **Neurodegeneration:** not established. Mild adult brain atrophy was observed in one individual, but there is insufficient longitudinal evidence to classify NEDMIBA as a progressive neurodegenerative disease.
- **Critical period:** fetal cortical progenitor proliferation, mitosis and commissural-axon development are the most likely biological vulnerability windows. Clinically, infancy and early childhood are critical for seizure recognition, hearing assessment, communication support and habilitation.

No formal staging system or prospective natural-history study exists.

---

## 9. Inheritance and population

### Inheritance

| Characteristic | Current conclusion |
|---|---|
| Mode | **Autosomal recessive** |
| Penetrance | Appeared complete for reported biallelic pathogenic genotypes, but the sample is too small for a formal estimate |
| Expressivity | Variable: severe ID in adults; variable tone, seizures and systemic findings |
| Anticipation | Not applicable; no repeat expansion |
| Germline mosaicism | Not reported; theoretically possible but not demonstrated |
| Founder effect | None proven |
| Consanguinity | Present in the homozygous Pakistani pedigree |
| Sex ratio | 2 males:3 females in the defining cohort; no sex bias demonstrated |
| Standard recurrence risk | If both parents carry one pathogenic allele: 25% affected, 50% unaffected carrier and 25% unaffected non-carrier per pregnancy |
| Carrier phenotype | Heterozygous parents were clinically unaffected |
| Carrier frequency | Unknown |

### Epidemiology

- **Prevalence:** unknown.
- **Incidence:** unknown.
- **Disease registry:** none located.
- **Geographic distribution:** documented in a Pakistani consanguineous family and two unrelated families with European/Eastern European/Ashkenazi Jewish ancestry.
- **Number of well-characterized published individuals:** five in three families.
- **Population burden:** cannot be extrapolated from general microcephaly statistics.

OMIM continues to summarize only the five 2019 patients. [261] The 2024 paper’s Family 12 reproduces the same c.607+1G>A allele and essentially the same three-person Pakistani phenotype, indicating likely overlap with the original pedigree. [255][286]

---

## 10. Diagnostics

### Clinical recognition

Consider NEDMIBA when the following cluster is present:

1. Congenital or severe progressive microcephaly;
2. Global developmental delay/intellectual disability;
3. Simplified gyral pattern;
4. Marked corpus-callosum hypogenesis/agenesis and reduced white matter;
5. Dysmorphic facies;
6. Recessive inheritance, consanguinity or affected siblings.

There are no formal diagnostic criteria. Molecular confirmation requires pathogenic/likely pathogenic variants affecting both *DYNC1I2* alleles, with phase established whenever possible.

### Recommended work-up

| Test | Use in suspected NEDMIBA |
|---|---|
| Serial occipitofrontal circumference, length/height and weight | Establish congenital versus postnatal microcephaly and growth trajectory |
| Developmental and neurologic assessment | Quantify cognition, language, motor function, tone and reflex abnormalities |
| Brain MRI | Preferred imaging; evaluate gyration, corpus callosum, cerebral white matter, brainstem, ventricles and posterior fossa |
| EEG | Indicated for seizures, spells, regression or abnormal movements; not supported as routine screening in all asymptomatic patients |
| Audiology and ENT assessment | Especially because structural unilateral hearing loss and recurrent otitis occurred |
| Ophthalmology | Reasonable baseline evaluation in severe neurodevelopmental disease, although no defining ocular phenotype is known |
| Thyroid function | Clinically indicated; hypothyroidism occurred in one child but is not a validated biomarker |
| Feeding/swallowing and nutrition assessment | For reflux, poor growth, choking or aspiration concern |
| Genetic testing | Trio ES/GS or a comprehensive microcephaly/cortical-malformation/NDD panel including *DYNC1I2*, with CNV analysis |
| Chromosomal microarray | Can detect a deletion encompassing *DYNC1I2* and other pathogenic CNVs; may miss small sequence variants |
| Sanger/orthogonal testing | Confirm candidate variants and test segregation/phase |
| RNA analysis | Helpful for splice variants such as c.607+1G>A if an informative tissue is available |
| Karyotype/FISH | Low yield unless a large rearrangement is suspected; not sufficient for most *DYNC1I2* variants |
| Metabolic testing | Guided by clinical findings; no characteristic NEDMIBA biochemical marker |
| Mitochondrial or repeat-expansion testing | Not specifically indicated unless the phenotype suggests an alternative diagnosis |

The ACMG guideline strongly recommends exome or genome sequencing as a first- or second-tier test for pediatric congenital anomalies, developmental delay or intellectual disability. Manickam et al., 1 July 2021, DOI: [10.1038/s41436-021-01242-6](https://doi.org/10.1038/s41436-021-01242-6), PMID:34211152. [166][170]

### Test-selection strategy

1. **Preferred:** trio genome sequencing, or trio exome sequencing with validated SNV/indel and exon-level CNV detection.
2. **Alternative:** broad microcephaly/brain-malformation/NDD panel including *DYNC1I2*.
3. **If one allele is found:** actively search for exon/gene deletions, structural variants, deep intronic variants and phase.
4. **If c.607+1G>A is found:** confirm zygosity and segregation; RNA testing can demonstrate splice effect.
5. **If p.Tyr247Cys is found:** do not diagnose on a single heterozygous allele; search for a second pathogenic allele.
6. **Reanalysis:** periodically reinterpret negative ES data because structural and noncoding variants may initially be missed.

### Differential diagnosis

| Differential | Gene/etiology | Distinguishing clues |
|---|---|---|
| NEDMABA | ***SMPD4***, OMIM:618622 | Arthrogryposis, contractures, prenatal growth restriction and neonatal respiratory distress are prominent; this is the most easily confused disease name. [12] |
| NMIHBA | ***PRUNE1***, OMIM:617481 | Profound hypotonia with peripheral spasticity, cerebral/cerebellar atrophy and delayed myelination; often neurodegenerative course. [30] |
| Primary microcephaly | ***ASPM, WDR62, CDK5RAP2*** and others | May be less syndromic; WDR62 can produce extensive cortical malformations |
| Tubulinopathy | ***TUBA1A, TUBB2B, TUBB3*** | Lissencephaly/polymicrogyria, basal-ganglia dysmorphism and characteristic tract abnormalities |
| Dynein-related disease | ***DYNC1H1*** | Usually autosomal dominant; may include cortical malformation, neuropathy or spinal muscular atrophy |
| Congenital infection | CMV, Zika, toxoplasmosis and others | Maternal/infectious history, calcifications, ocular/hearing findings and pathogen testing |
| Chromosomal/CNV disorder | Numerous | Additional congenital anomalies; detected by CMA/GS |

### Screening

NEDMIBA is not part of routine newborn screening. Appropriate targeted approaches are:

- Cascade carrier testing for adult relatives after a familial molecular diagnosis;
- Partner testing for known carriers;
- Prenatal diagnosis by CVS or amniocentesis;
- Preimplantation genetic testing for monogenic disease;
- Fetal neurosonography/MRI as adjuncts, recognizing that imaging cannot reliably exclude the molecular disorder early in gestation.

---

## 11. Outcomes and prognosis

### Survival

No survival curve, mortality rate or life-expectancy estimate exists. The three affected siblings alive at 20, 32 and 34 years show that survival into adulthood is possible. No deaths were reported in the defining cohort.

### Morbidity and function

The main long-term burden is neurologic:

- Severe intellectual and adaptive disability;
- Limited or dysarthric speech;
- Delayed or absent independent walking;
- Epilepsy in some patients;
- Spasticity or hypotonia;
- Behavioral dysregulation;
- Hearing impairment and feeding/reflux problems in individual cases.

Recovery of normal brain size or correction of the congenital structural malformations is not expected. Functional gains may nevertheless occur with seizure control, communication aids, education and intensive habilitation.

### Potential prognostic indicators

Evidence is insufficient for validated prognostic biomarkers. Plausible indicators requiring study include:

- Degree and trajectory of microcephaly;
- Extent of callosal agenesis and white-matter loss;
- Seizure burden;
- Ability to acquire head control, sitting and early communication;
- Null/null versus hypomorphic genotypes.

The survival of homozygous c.607+1G>A adults shows that this allele is not invariably lethal. There is no demonstrated genotype–phenotype correlation separating p.Tyr247Cys from null alleles.

---

## 12. Treatment

There is **no disease-modifying treatment, approved targeted therapy, gene therapy, RNA therapy or registered NEDMIBA-specific clinical trial**. Management is symptom-directed and multidisciplinary.

| Intervention | Indication/strategy | Evidence level and outcome | Suggested NCIT intervention term |
|---|---|---|---|
| Early developmental intervention | Begin as soon as delay is recognized | General GDD/ID evidence and expert consensus; no NEDMIBA-specific response rate | Early Intervention |
| Physical therapy | Delayed gross motor skills, hypotonia, spasticity, positioning and contracture prevention | Supportive; goals are mobility and prevention of secondary disability | Physical Therapy |
| Occupational therapy | Fine motor, adaptive function, equipment and activities of daily living | Supportive | Occupational Therapy |
| Speech-language therapy | Speech delay, dysarthria and communication impairment | Supportive; augmentative communication may be essential | Speech and Language Therapy |
| Augmentative and alternative communication | Minimal or unintelligible speech | Individualized devices, signs or communication boards | Assistive Communication Device |
| Antiseizure medication | Treat according to seizure type and standard pediatric epilepsy practice | No preferred drug or disease-specific pharmacogenomic rule | Anticonvulsant Therapy |
| Spasticity management | Stretching, positioning, orthoses; consider oral agents or botulinum toxin according to severity | No disease-specific studies | Spasticity Management; Botulinum Toxin Therapy |
| Feeding/reflux care | Feeding evaluation, positioning, diet modification and standard reflux therapy | One reported patient had reflux; treatment individualized | Nutritional Support; Gastroesophageal Reflux Treatment |
| Audiology/hearing support | Cochlear/hearing defect or recurrent otitis | Hearing aid or other device as appropriate | Hearing Aid Device |
| Thyroid replacement | Biochemically confirmed hypothyroidism | Treat as standard hypothyroidism; not a therapy for DYNC1I2 dysfunction | Thyroid Hormone Replacement Therapy |
| Behavioral support | ADHD, irritability or aggression | Behavioral assessment; medication only according to standard indications | Behavioral Therapy |
| Genetic counseling | Recurrence risk, cascade testing and reproductive options | Central component of care | Genetic Counseling |
| Orthopedic surveillance | Spasticity, poor mobility, hypermobility and contracture risk | Extrapolated from severe motor disability care | Orthopedic Assessment |

Current general GDD guidance favors family-centered multidisciplinary care involving neurology, genetics, developmental pediatrics, physical/occupational/speech therapy, psychology, education, nutrition and social work. [181][192]

No pharmacogenomic associations involving *DYNC1I2* and antiseizure or behavioral medications are established.

---

## 13. Prevention

### Primary prevention

The pathogenic variants cannot be prevented through diet, vaccination or lifestyle modification. For families with a molecular diagnosis, reproductive options include:

- Carrier testing of at-risk relatives;
- Preconception partner testing;
- IVF with PGT-M;
- Prenatal diagnosis by CVS or amniocentesis;
- Use of donor gametes where desired.

### Secondary prevention/early detection

- Early recognition of faltering head growth;
- Prompt developmental assessment;
- MRI and genomic testing;
- Early identification of seizures, hearing impairment, feeding problems and hypothyroidism;
- Immediate referral to habilitation services rather than waiting for complete etiologic work-up.

### Tertiary prevention

- Seizure treatment and safety planning;
- PT/positioning/orthoses to reduce contractures and secondary deformity;
- Swallow and nutrition management to reduce aspiration and malnutrition;
- Hearing correction and communication support;
- Behavioral and caregiver support;
- Routine immunization and infection prevention according to standard schedules.

There is no relevant disease-specific vaccine, antimicrobial prophylaxis or environmental public-health intervention.

---

## 14. Other species and natural disease

| Species | Taxonomy/ortholog | Natural disease status | Comparative relevance |
|---|---|---|---|
| Human | *Homo sapiens*, NCBI Taxon **9606**; *DYNC1I2*, Gene 1781 | Naturally occurring Mendelian NEDMIBA | Reference disease |
| Mouse | *Mus musculus*, Taxon **10090**; *Dync1i2*, MGI:107750 | No recognized spontaneous veterinary counterpart resembling human NEDMIBA | ENU homozygotes show only a trend toward slight locomotor deficit; targeted knockout resources exist. [124][125] |
| Zebrafish | *Danio rerio*, Taxon **7955**; *dync1i2a* and *dync1i2b* | No natural veterinary disease reported | *dync1i2a* disruption is the principal mechanistic model |
| Rat and other vertebrates | Conserved orthologs | No corresponding natural syndrome identified | Support evolutionary conservation of dynein function |

No breed-specific disorder, VBO term, zoonotic potential or cross-species transmission applies. This is a constitutional genetic disorder, not an infectious disease.

---

## 15. Model organisms and experimental systems

| Model | Genetic manipulation | Phenotype recapitulated | Principal application | Limitations/resource |
|---|---|---|---|---|
| Zebrafish F0 CRISPR | Mosaic disruption of *dync1i2a* | Reduced head area, altered craniofacial cartilage patterning | Tests developmental requirement | Mosaic rather than stable germline model; fish have two paralogs |
| Zebrafish morpholino | Splice suppression of *dync1i2a* | Microcephaly-like head reduction, increased ceratohyal angle, disorganized axon tracts, reduced optic tectum | Cell-cycle, apoptosis and neuroanatomical studies | Morpholino off-target/transient-effect concerns |
| Zebrafish human-mRNA rescue | Wild-type or variant human *DYNC1I2* mRNA | Wild-type rescued phenotype; p.Tyr247Cys and p.Gln290Ter did not | Functional variant classification | Overexpression/rescue assay may not model endogenous dosage |
| Zebrafish *dync1i2b* disruption | CRISPR or morpholino | No comparable head-size phenotype | Paralog-specificity control | Does not exclude subtler or later functions |
| Mouse ENU model | Homozygous *Dync1i2* allele | Trend toward mild locomotor deficit | Mammalian motor-function studies | Poorly recapitulates severe human cortical phenotype |
| Mouse targeted allele | *Dync1i2* tm1a(EUCOMM)Wtsi, convertible to knockout | Broad IMPC phenotyping resources | Conditional/tissue-specific studies | A disease-specific cortical-development characterization has not been published |
| Patient-derived cells/iPSCs | None reported | — | Would allow direct splice, spindle and neural-progenitor studies | Major evidence gap |
| Cerebral organoids | None reported | — | Could test progenitor survival, cortical growth and callosal-neuron differentiation | Major evidence gap |

The Alliance recognizes one mouse, one rat and two zebrafish orthologs for human *DYNC1I2*. [125][126] The strongest current model remains the 2019 zebrafish work; no 2023–2024 disease-specific organoid, iPSC, single-cell or therapeutic-model study was located.

---

## Current expert interpretation and research priorities

The most defensible interpretation is that NEDMIBA is a **dynein-complex neurodevelopmental disorder in which impaired DYNC1I2 function disrupts neural-progenitor mitosis and axonal organization**. The human genetic evidence is compelling because of recessive segregation across three families, recurrence of p.Tyr247Cys in two unrelated cases, rarity of alleles, and zebrafish rescue assays. Nevertheless, the mechanism linking dynein dysfunction to the precise human cortical and callosal malformations remains partly inferential.

Highest-priority knowledge gaps are:

1. Additional independently ascertained patients and complete phenotyping;
2. RNA confirmation of c.607+1G>A;
3. Patient fibroblast/iPSC neural-progenitor and cerebral-organoid models;
4. Stable *dync1i2a* zebrafish and conditional neural mouse knockouts;
5. Natural-history, seizure, communication and quality-of-life data;
6. Identification of genotype–phenotype and modifier relationships;
7. Evaluation of whether early restoration of DYNC1I2 expression can rescue progenitor loss before irreversible brain malformation occurs.

At present, clinical implementation is therefore centered on **accurate molecular diagnosis, recurrence-risk counseling, early developmental therapy, seizure surveillance and individualized management of hearing, feeding, tone and behavioral complications**, rather than targeted molecular treatment.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 49 |
| Resolved | 43 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 5 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032779` (4 mentions) - the report calls it "if available", "MONDO"; MONDO calls it **neurodevelopmental disorder with microcephaly and structural brain anomalies**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `CL:0000337` (CL_0000337) (1 mention) - replaced by `CL:0000031`

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0032779` - called "if available", "MONDO"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `MGI`.
