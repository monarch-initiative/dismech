---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-08-28T11:44:04.768642'
end_time: '2026-08-28T11:48:54.875832'
duration_seconds: 290.11
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Charcot-Marie-Tooth Disease Dominant Intermediate B
  mondo_id: ''
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
citation_count: 19
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 4
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Charcot-Marie-Tooth Disease Dominant Intermediate B
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth Disease Dominant Intermediate B** covering all of the
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

# Charcot-Marie-Tooth Disease Dominant Intermediate B: Comprehensive Disease Characteristics

Charcot-Marie-Tooth disease dominant intermediate B (CMTDIB), also known as dynamin-2–related dominant intermediate Charcot-Marie-Tooth neuropathy type B, is a rare autosomal dominant hereditary motor and sensory neuropathy caused by heterozygous mutations in the dynamin 2 (DNM2) gene on chromosome 19p13.2.[1][4][12] It belongs to the broader Charcot-Marie-Tooth (CMT) spectrum, characterized clinically by slowly progressive distal limb weakness and atrophy, sensory loss, areflexia, and deformities such as pes cavus, and electrophysiologically by median motor nerve conduction velocities in the intermediate range between typical demyelinating and axonal CMT.[6][15][16] The defining molecular feature of CMTDIB is that disease-causing DNM2 variants alter clathrin-mediated endocytosis and myelination in Schwann cells and peripheral neurons, in contrast to a distinct set of DNM2 mutations that produce autosomal dominant centronuclear myopathy.[4][13][14] Cohort studies show that CMTDIB generally produces a mild to moderately severe neuropathy with mean age at onset around \(16\) years, a wide age range from early childhood to late adulthood, and very low rates of wheelchair dependence, while some mutations, particularly those affecting Lys558 in the pleckstrin homology (PH) domain, are associated with neutropenia and early cataracts.[15][16] At present, no disease-modifying pharmacologic or gene-targeted therapies exist; management is supportive, based on rehabilitation, orthotic devices, orthopedic surgery when needed, and symptomatic treatment of pain and complications.[6][10] This report synthesizes clinical, genetic, mechanistic, and translational data from human cohorts, mouse models, and in vitro studies to provide a detailed disease characterization suitable for a structured knowledge base, including ontology mappings, evidence types, and remaining gaps in understanding.

## 1. Disease Information

### 1.1 Overview and Clinical Definition

Charcot-Marie-Tooth disease dominant intermediate B is one of the genetically defined intermediate CMT subtypes, distinguished by autosomal dominant inheritance, a classical CMT phenotype, and electrophysiological findings that fall between the traditional demyelinating (CMT1) and axonal (CMT2) categories.[1][6][16] GeneReviews defines dominant intermediate CMT (DI-CMT) as having median motor nerve conduction velocities (NCV) in the range of approximately \(35\)–\(45\) m/s, with clinical findings similar to standard CMT, and notes that NCVs can be highly variable within a family such that some affected individuals show NCVs in the demyelinating range while others fall in the axonal range.[6] CMTDIB is specifically linked to heterozygous mutations in DNM2, a large GTPase involved in vesicle budding, organelle fission and fusion, and clathrin-mediated endocytosis.[1][4][12] Affected individuals present with distal muscle weakness and atrophy beginning in the lower limbs, distal sensory loss, reduced or absent deep tendon reflexes, and frequent foot deformities including pes cavus, often accompanied by extensor digitorum brevis muscle atrophy.[6][8][15]

OMIM uses a number sign with entry MIM #606482 to indicate that CMTDIB and a related axonal type, CMT2M, are caused by heterozygous mutation in DNM2 on chromosome 19p13.2-p12.[1] Züchner and colleagues first mapped this form of dominant intermediate CMT to 19p13.2-p12 and showed that mutations in the pleckstrin homology domain of DNM2 cause dominant intermediate Charcot-Marie-Tooth disease, establishing the genetic basis for CMTDIB.[1][13] Subsequent clinical series, notably the Brain 2009 cohort study of 34 patients from six unrelated families, delineated the phenotypic spectrum, including age at onset, severity, electrophysiologic characteristics, hematologic abnormalities, and nerve biopsy findings.[15][16] CMTDIB is rare and contributes only a small fraction of the overall CMT burden, which itself has a population prevalence estimated around 1 in 2,500, but its study has provided important mechanistic insights into peripheral nerve myelination and endocytosis.[6]

### 1.2 Key Identifiers and Classification

CMTDIB is cataloged under multiple disease taxonomies and classification systems. OMIM designates this phenotype as "Charcot-Marie-Tooth disease, dominant intermediate B" with MIM number 606482 and notes its mapping to chromosome 19p13.2, with DNM2 (MIM 602378) as the causal gene.[1] The same OMIM entry also recognizes "Charcot-Marie-Tooth disease, axonal type 2M" as a related phenotype associated with DNM2 mutations, emphasizing the genetic and clinical overlap between intermediate and axonal forms.[1][6] MedGen and Orphanet describe "Charcot-Marie-Tooth disease dominant intermediate B" as a distinct concept, linking it to the underlying DNM2 gene and noting that some cases include neutropenia as part of the phenotype.[5][11] SNOMED CT includes a concept with the identifier 765745007 corresponding to "Charcot-Marie-Tooth disease, dominant intermediate B, with neutropenia, included."[1][11] Orphanet lists the disease under rare CMT subtypes, with Orphanet identifiers associated with DNM2-related dominant intermediate CMT; OMIM cites ORPHA codes 100044 and 228179 for related entities.[1][11]

Disease ontology classifications place CMTDIB within "Charcot-Marie-Tooth disease" and "hereditary motor and sensory neuropathy," with a specific Disease Ontology (DO) identifier 0110197 assigned to "Charcot-Marie-Tooth disease, dominant intermediate B."[1] ICD-10 and ICD-11 do not have codes specific to CMTDIB; instead, cases are generally coded under broader hereditary neuropathy categories such as G60.0 ("Hereditary motor and sensory neuropathy") in ICD-10. MeSH indexes the broader CMT entity under "Charcot-Marie-Tooth Disease" but does not subdivide into genetic subtypes, so literature on CMTDIB is retrieved within the general CMT descriptor.[6][10] A specific MONDO identifier for CMTDIB is not clearly provided in the available search results, though MONDO does contain entities for "Charcot-Marie-Tooth disease dominant intermediate C" and other intermediate forms, suggesting that a MONDO term for DI-CMTB likely exists but cannot be definitively specified here.[8][19]

The table below summarizes key identifiers and synonyms based on the aggregated resources.

| Category | Identifier / Name | Source |
|---------|-------------------|--------|
| OMIM phenotype | Charcot-Marie-Tooth disease, dominant intermediate B (CMTDIB) – MIM 606482 | OMIM[1] |
| Causal gene | DNM2 (dynamin 2) – MIM 602378 | OMIM[1][12] |
| SNOMED CT | 765745007 "Charcot-Marie-Tooth disease, dominant intermediate B, with neutropenia" | OMIM, MedGen[1][11] |
| Disease Ontology | DOID:0110197 "Charcot-Marie-Tooth disease, dominant intermediate B" | OMIM[1] |
| Orphanet | Rare CMT subtype linked to DNM2; ORPHA identifiers 100044, 228179 (related) | OMIM, Orphanet[1][11] |
| MedGen concept | "Charcot-Marie-Tooth disease dominant intermediate B" (MedGen CUI) | MedGen[5] |

### 1.3 Synonyms and Alternative Names

Several synonyms and alternative names are used for CMTDIB across clinical and genetic literature. OMIM primarily uses "Charcot-Marie-Tooth disease, dominant intermediate B" and "Charcot-Marie-Tooth neuropathy, dominant intermediate B" to delineate the phenotype linked to DNM2 mutations.[1][11] Clinical neurology literature often refers to this entity as "dominant intermediate Charcot-Marie-Tooth neuropathy type B (DI-CMTB)." The Brain 2009 article describing the phenotypic spectrum uses the term "dominant intermediate Charcot-Marie-Tooth neuropathy type B" throughout and emphasizes that it is caused by mutations in dynamin 2.[15][16] UpToDate and other reviews refer to "CMT dominant intermediate B (CMTDIB)" in discussions of genotype–phenotype correlations.[9]

Synonyms that highlight the gene include "DNM2-related Charcot-Marie-Tooth disease," "dynamin 2–associated CMT," and "DNM2-related dominant intermediate CMT."[4][12][15] In cases where neutropenia is present, OMIM and MedGen note "Charcot-Marie-Tooth disease, dominant intermediate B, with neutropenia" as an included phenotype within CMTDIB, reflecting the genotype–phenotype association with certain Lys558 variants.[1][11][16] To distinguish from other intermediate forms, the letter "B" is retained, contrasting with dominant intermediate CMT A, C, and D (CMTDIA, CMTDIC, CMTDID) caused by mutations in other genes such as INF2, YARS1, and MPZ.[1][2][3][6][8]

From an ontology perspective, the disease sits under high-level categories including "Hereditary motor and sensory neuropathy" and "Peripheral demyelinating neuropathy," while more specific terms like "Intermediate Charcot-Marie-Tooth disease" or "Dominant intermediate Charcot-Marie-Tooth neuropathy type B" capture its electrophysiologic distinctiveness.[1][6][16] These synonyms and hierarchical relationships are crucial for harmonizing data across databases and for accurate mapping to ontologies such as MONDO and HPO.

### 1.4 Source of Information: Patient-Level vs Aggregated Resources

Information about CMTDIB comes predominantly from aggregated disease-level resources and cohort studies rather than large-scale EHR-based analyses, reflecting the rarity of the condition. OMIM entry #606482 synthesizes genetic mapping evidence, mutation data, and clinical descriptions from multiple families, including the original linkage studies and subsequent case series.[1] GeneReviews provides a broad overview of CMT, including intermediate forms, and outlines classification schemes, inheritance patterns, and diagnostic approaches based on extensive literature review.[6] Orphanet and MedGen compile structured disease concepts, synonyms, and cross-references from literature, expert-curated databases, and clinical genetics centers.[5][7][8][11]

Primary human evidence consists of well-characterized family-based studies. The Brain 2009 article reports detailed clinical, hematological, electrophysiological, and sural nerve biopsy data from 34 patients in six families with DNM2 mutations, providing the most comprehensive phenotype spectrum analysis for CMTDIB.[15][16] Additional evidence comes from case reports and small series describing novel DNM2 mutations, such as the 2022 report of siblings with a c.1609G>A (p.Gly537Ser) mutation in exon 15, as well as association of DNM2 mutations with other phenotypes like centronuclear myopathy.[12][13] Mechanistic studies, notably Sidiropoulos et al. 2012, used tissue derived from Dnm2-deficient mice to model peripheral nerve features and assess the functional impact of CMT-associated versus CNM-associated DNM2 mutants.[4]

There is, to date, limited use of large clinical registries or EHR-derived datasets specifically focused on CMTDIB. Most epidemiologic and outcome data are extrapolated from broader CMT registries or from the relatively small DNM2-mutant cohorts described in neuromuscular clinics.[6][10][15] Thus, the disease knowledge base for CMTDIB is grounded in expert-curated genetic and clinical data, family-based natural history observations, and mechanistic experimental models rather than in population-level informatics analyses.

## 2. Etiology

### 2.1 Primary Causal Factors: Genetic Basis

The primary etiologic factor in Charcot-Marie-Tooth disease dominant intermediate B is a germline heterozygous pathogenic variant in the DNM2 gene, encoding dynamin 2, on chromosome 19p13.2-p12.[1][4][12] OMIM explicitly states that "dominant intermediate Charcot-Marie-Tooth (CMT) disease and axonal CMT that map to chromosome 19p, here designated CMTDIB and CMT2M, respectively, are caused by heterozygous mutation in the gene encoding dynamin-2 (DNM2; 602378)."[1] Züchner et al. mapped the disease locus to 19p13.2-p12 and identified missense mutations in the pleckstrin homology domain of DNM2 that segregate with disease in affected families, thereby establishing causality.[1][13] Dynamin 2 is a large mechanoenzyme GTPase that mediates vesicle budding, organelle fission and fusion, and clathrin-coated endocytosis, and it acts with other proteins such as actin, endophilin, and amphiphysin.[12] Pathogenic DNM2 mutations in CMTDIB alter these functions in a manner that produces peripheral neuropathy.

The Brain 2009 cohort and its accompanying mechanistic work demonstrate that dominant intermediate CMTB is consistently associated with specific DNM2 mutations, such as Gly358Arg in the middle domain; Asp551_Glu553del, Lys550fs, Lys558del, and Lys558Glu in the PH domain; and Thr855_Ile856del in the proline-rich C-terminal domain.[15][16] These mutations segregate with disease in respective families and are absent in healthy controls, fulfilling genetic criteria for causality. A more recent case report describes a novel heterozygous missense point mutation in exon 15 of DNM2 (c.1609G>A), resulting in substitution of glycine 537 to serine (p.Gly537Ser) in three family members with dominant intermediate CMTB phenotype.[12][18] ClinVar classifies this variant as pathogenic based on segregation, predicted deleterious effect, and absence in population databases.[18][12]

The genetic etiology is strictly Mendelian and autosomal dominant. GeneReviews notes that CMT hereditary neuropathy can be inherited in autosomal dominant, autosomal recessive, or X-linked manner, and for autosomal dominant CMT, each child of an affected individual has a 50% chance of inheriting the pathogenic variant.[6] For DNM2-related CMTDIB, penetrance appears high, with nearly all heterozygous carriers showing some neuropathic signs, though expressivity is variable.[15][16] In contrast, a different set of DNM2 mutations, often clustered in distinct residues or domains, cause autosomal dominant centronuclear myopathy (CNM) and other neuromuscular phenotypes, a fact that underscores the strong genotype–phenotype specificity in DNM2-related disease.[4][13][14]

### 2.2 Risk Factors: Genetic and Environmental

The dominant risk factor for CMTDIB is the presence of a pathogenic germline DNM2 variant in the heterozygous state. Family history of CMT consistent with autosomal dominant inheritance is a strong predictor of being a carrier and hence of developing disease.[1][6][15] The Brain 2009 study provides evidence across six unrelated families that DNM2 mutations confer high risk of neuropathy, with mean age of onset around \(16\) years and variable severity.[15][16] Heterozygous carriers of Gly358Arg, Lys558Glu, Lys558del, or other mutations all manifested neuropathic symptoms, though with a range of onset ages, indicating age-dependent penetrance rather than incomplete penetrance.[15][16]

Beyond these primary genetic factors, no susceptibility loci, modifier genes, or polygenic risk scores have been convincingly identified that alter risk of CMTDIB. However, GeneReviews notes that more than 80 genes are associated with CMT, and the clinical heterogeneity suggests that background variation in other neuropathy genes, such as MFN2, GJB1, or MPZ, could theoretically modulate disease expression in individuals who also carry DNM2 mutations.[6][2][3] This possibility remains speculative and has not been systematically evaluated in large cohorts. ClinVar and OMIM catalog numerous DNM2 variants classified as likely pathogenic or pathogenic for CMT2M or CMTDIB, but no data indicate the presence of protective alleles or common polymorphisms that substantially influence disease risk.[1][12][18]

Environmental risk factors for CMTDIB are not clearly established. As with other CMT forms, exposures to neurotoxic agents such as certain chemotherapeutic drugs (e.g., vincristine), chronic excessive alcohol use, or poorly controlled diabetes may exacerbate peripheral neuropathy, but these are general neuropathy risk factors and not specific to DNM2-related disease.[6][10] There is no evidence that toxins, infections, or specific occupational exposures can independently cause CMTDIB in the absence of a DNM2 mutation. Age and sex do not appear to be major risk modifiers; the Brain 2009 cohort included both males and females with similar phenotypic expression, and age at onset ranged broadly from 2 to 50 years among carriers.[15][16] Family history remains the primary risk indicator, consistent with autosomal dominant inheritance.

### 2.3 Protective Factors

No specific genetic protective factors have been identified for CMTDIB. Unlike some complex diseases where common variants can confer reduced risk, Mendelian conditions such as DNM2-related CMTDIB are primarily determined by the presence or absence of a highly penetrant pathogenic mutation. The Nature Communications 2025 study, however, introduced an intriguing concept whereby combining a DNM2 myopathy-causing mutation with a neuropathy-causing mutation in the same gene can rescue many phenotypic features in vivo.[13] The authors report that "two distinct disease-causing mutations within the DNM2 gene compensate each other in vivo, leading to corrections of most individual phenotypes," and their data support that DNM2-CNM mutations are gain-of-function while DNM2-CMT mutations are loss-of-function.[13] Although this work is experimental and not a naturally occurring protective mechanism, it demonstrates that opposite functional effects in DNM2 can theoretically ameliorate each other.

Environmental or lifestyle protective factors in CMTDIB are also poorly defined. General recommendations for individuals with hereditary neuropathy include maintaining physical activity within tolerable limits, avoiding obesity, and preventing foot and ankle injuries, as these can help preserve functional capacity and reduce disability.[6][10] Early institution of supportive therapies such as orthotic devices and physical therapy can be considered a form of secondary or tertiary prevention, reducing downstream morbidity and maintaining independence, though they do not alter underlying disease biology.[6][10] There is no evidence that diet, specific supplements, or avoidance of particular exposures can prevent onset of CMTDIB in DNM2 mutation carriers.

### 2.4 Gene–Environment Interactions

Evidence for gene–environment interactions in CMTDIB is limited. The primary causal chain begins with a germline DNM2 mutation that alters dynamin 2 function in clathrin-mediated endocytosis and myelination; downstream processes in Schwann cells and neurons then produce the neuropathic phenotype.[4][13][14] Environmental influences may modulate severity or rate of progression by affecting nerve health generally. For example, exposure to neurotoxic agents or metabolic insults could exacerbate axonal degeneration or myelin pathology in already compromised nerves, but this has been inferred from broader neuropathy literature rather than directly studied in DNM2-mutant cohorts.[6][10][16]

Sidiropoulos et al. used Dnm2-deficient mouse tissue as a model to show that DNM2 function is strictly required for myelination and clathrin-mediated endocytosis in Schwann cells, demonstrating that myelination is "strictly dependent on Dnm2 and clathrin-mediated endocytosis function."[4] This indicates that any environmental factor impairing endocytosis or myelin maintenance could have amplified effects in individuals whose DNM2 function is already compromised. However, such environmental factors have not been systematically cataloged. No CTD (Comparative Toxicogenomics Database)–type evidence specific to DNM2 and CMTDIB was available in the provided search results, and no clinical studies have examined differential susceptibility to environmental toxins in DNM2 mutation carriers versus controls.

In summary, the etiology of CMTDIB is overwhelmingly genetic, rooted in autosomal dominant germline DNM2 mutations with strong, often near-complete penetrance. Risk is determined by carrier status and family history; gene–environment interactions and protective factors remain largely theoretical, and further epidemiologic and mechanistic work would be required to elucidate subtle modifiers of disease expression.

## 3. Phenotypes

### 3.1 Core Neuromuscular Phenotype

The core clinical phenotype of CMTDIB is a classical Charcot-Marie-Tooth presentation with mild to moderately severe distal sensorimotor neuropathy. Patients typically develop progressive weakness and atrophy of the distal muscles of the lower limbs, particularly the peroneal muscles, followed later by involvement of distal upper limb muscles.[1][6][15] GeneReviews describes CMT as causing "muscle weakness and atrophy of the distal extremities, distal sensory loss, reduced or absent deep tendon reflexes, feet deformities, extensor digitorum brevis atrophy," and these features are also characteristic of autosomal dominant intermediate forms, including DI-CMTB.[6][8] The Cleveland Clinic similarly notes that CMT causes "worsening weakness in your feet and hands due to peripheral nerve damage" and sensory symptoms such as numbness, which align with patient reports in DNM2-mutant families.[10]

In the Brain 2009 cohort of 34 patients with DNM2 mutations, the clinical phenotype was described as "classical Charcot-Marie-Tooth phenotype, which was mild to moderately severe since only 3% of the patients were wheelchair-bound."[15][16] Mean age at onset was \(16\) years, with a broad range from \(2\) to \(50\) years, indicating childhood to adult onset.[15][16] Distal weakness and atrophy were universal, often leading to foot drop, difficulty walking, and hand weakness that impaired fine motor tasks. Sensory loss, predominantly in a length-dependent pattern affecting vibration, proprioception, and light touch in the feet and later hands, was commonly reported, consistent with a length-dependent axonal neuropathy component.[15][16]

Reflex changes were prominent. Deep tendon reflexes at the ankles and sometimes knees were reduced or absent, one of the hallmark signs of hereditary peripheral neuropathy.[6][8] Foot deformities, especially pes cavus (high-arched foot) and hammer toes, were frequent and often required orthotic management or orthopedic surgery.[6][8][10] Extensor digitorum brevis muscle atrophy, visible as wasting on the dorsum of the foot, is particularly noted in CMT and was present in many DI-CMTB patients.[6][8] HPO terms that correspond to these phenotypes include distal muscle weakness (HP:0003474), muscle atrophy (HP:0003202), peripheral axonal neuropathy (HP:0003477), sensory loss (HP:0004325), areflexia (HP:0001284), pes cavus (HP:0001761), and hammer toe (HP:0001765).

### 3.2 Electrophysiological Features

Electrophysiological characterization is central to defining CMTDIB as an intermediate neuropathy. GeneReviews specifies that dominant intermediate CMT is defined by motor median nerve conduction velocities in the intermediate range between classic demyelinating and axonal neuropathy, with NCV approximately \(35\)–\(45\) m/s, and notes that within a family, some affected individuals may have NCVs in the demyelinating range and others in the axonal range.[6] The Brain 2009 study provides detailed NCV data for DNM2-mutant families. Median nerve motor conduction velocities were available for 27 nerves in 20 affected members, with overall NCV ranging from \(26.2\) to \(57.0\) m/s.[16]

The authors report that in four families, median motor NCV varied from approximately \(26.0\) m/s to normal values, reflecting a broad "intermediate" spectrum.[16] In two families (Dutch pedigree H20 and Belgian family CMT-72), median motor NCV were less reduced, varying between \(41.0\) and \(46.0\) m/s, thus within the axonal NCV range, and corresponding compound muscle action potential (CMAP) amplitudes were not reduced.[16] Reduced motor median NCV between \(38\) and \(49\) m/s were always associated with normal CMAP amplitudes, whereas more severely reduced CMAP amplitudes were observed in median nerves with motor NCV below \(38\) m/s.[16] In some nerves, both NCV and CMAP were normal; in one individual, NCV was normal but CMAP amplitude was reduced.[16] These data led the authors to conclude that DNM2-mutated CMT families correspond to a broader definition of intermediate CMT, "showing median motor NCV ranging from 25 m/s to normal values," and that the term "intermediate" should be applied at the family level rather than to a single nerve measurement.[16]

Somatosensory evoked potentials in the proband of one family showed severely attenuated sensory nerve action potential amplitudes, reduced sensory conduction velocity, and delayed cortical responses, indicating both peripheral and central conduction impairment in severe cases.[16] HPO terms appropriate for these electrophysiological features include abnormal nerve conduction velocity (HP:0003447), reduced compound muscle action potential (HP:0003458), and abnormal somatosensory evoked potentials (HP:0007043). These electrophysiologic characteristics are crucial for differentiating CMTDIB from demyelinating CMT1, axonal CMT2, and acquired demyelinating neuropathies like CIDP.

### 3.3 Nerve Biopsy and Tissue-Level Phenotypes

Histopathologic findings from sural nerve biopsy in DNM2-mutant patients further refine the phenotype. In the Dutch patient with Lys558Glu mutation, sural nerve biopsy showed "diffuse loss of large myelinated fibres, presence of many clusters of regenerating myelinated axons and fibres with focal myelin thickenings—findings very similar to those previously reported in the Australian family."[16] These features reflect a mixed demyelinating and axonal process with ongoing attempted regeneration and remyelination. The absence of onion bulb formations, which are typical in longstanding demyelinating neuropathies such as CMT1A, suggests that the pathophysiologic process differs from classic Schwann cell proliferation and repetitive demyelination-remyelination observed in PMP22 duplication–related CMT.[8][16][19]

Orphanet's description of autosomal dominant intermediate CMT type C, which shares some features with DI-CMTB, notes that nerve biopsies in intermediate CMT show age-dependent axonal degeneration, reduced number of large myelinated fibers, segmental remyelination, and no onion bulbs.[8] These descriptors apply well to the DNM2-mutant biopsies and reinforce the intermediate classification. HPO terms relevant here include axonal degeneration (HP:0003438), reduced number of large myelinated fibres (HP:0003487), segmental demyelination and remyelination (HP:0003436), and absence of onion bulb formation (HP:0003473).

Mechanistic studies in Dnm2-deficient mice indicate that myelination is strictly dependent on Dnm2 and clathrin-mediated endocytosis function in Schwann cells.[4] Sidiropoulos et al. report that peripheral nervous system Schwann cells and neurons expressing CMT-associated DNM2 mutants showed defects in clathrin-mediated endocytosis and that protein surface levels are altered in Schwann cells, leading to myelination defects.[4] These tissue-level abnormalities are consistent with the human biopsy findings and further define the phenotypic spectrum at the cellular and ultrastructural level.

### 3.4 Hematologic and Ocular Phenotypes: Neutropenia and Cataracts

An important extension of the phenotypic spectrum of CMTDIB is the association with neutropenia and early-onset cataracts observed in specific DNM2-mutant families. The Brain 2009 study reports that in Australian and Belgian families carrying two different mutations affecting the same amino acid Lys558 in the PH domain, "Charcot-Marie-Tooth cosegregated with neutropaenia."[15][16] Neutropenia was documented on hematological evaluation and appeared to segregate with the DNM2 mutation, suggesting a shared etiologic basis. In addition, early onset cataracts were observed in one of the CMT families, indicating lens involvement as another DNM2-related phenotype.[15][16]

These findings led the authors to conclude that DNM2 mutations should be screened in autosomal dominant CMT families with intermediate or axonal NCV, particularly "when Charcot-Marie-Tooth is associated with neutropaenia or cataracts."[16] OMIM recognizes "Charcot-Marie-Tooth disease, dominant intermediate B, with neutropenia" as an included phenotype under entry #606482, emphasizing the disease-modifying potential of specific DNM2 variants.[1][11] HPO terms for these phenotypes include neutropenia (HP:0001875), susceptibility to bacterial infections (HP:0002719), and cataract (HP:0000518).

From a mechanistic perspective, neutropenia suggests that DNM2 function is also important in hematopoietic or immune cells, consistent with its ubiquitous expression and role in endocytosis. Cataracts imply a role in lens fiber cell homeostasis or membrane dynamics, though detailed pathophysiological explanations for these extra-neural phenotypes remain to be elucidated. Clinically, the presence of neutropenia may influence infection risk and therefore quality of life and management strategies.

### 3.5 Age of Onset, Severity, and Progression

Age of symptom onset in CMTDIB is variable but typically lies in childhood or adolescence. The Brain 2009 cohort reported a mean age at onset of \(16\) years with a range from \(2\) to \(50\) years, indicating that some individuals present as early as toddlerhood while others have adult-onset disease.[15][16] This wide range illustrates age-dependent penetrance and variable expressivity. GeneReviews, describing CMT more broadly, notes that onset is usually in the first or second decade of life but can be later depending on subtype.[6] For DNM2-related disease, onset tends to be earlier in families with more severe mutations or additional systemic features such as neutropenia, although detailed genotype–age correlations are not fully established.[15][16]

Severity of CMTDIB is generally mild to moderate. Brain 2009 notes that "only 3% of the patients were wheelchair-bound," meaning that most retain ambulation with or without aids.[15][16] Distal weakness and deformities may cause significant functional limitations in running, climbing stairs, and hand-intensive tasks, but many patients can walk independently for decades.[15][16] Cleveland Clinic emphasizes that CMT "usually isn’t harmful to your health" in terms of longevity, though it can substantially affect quality of life and require various therapies for mobility and pain.[10] Disease progression is slowly progressive over years to decades; no episodic or relapsing-remitting pattern is described in DI-CMTB, and spontaneous remission does not occur.[6][15][16]

The progression pattern is one of gradual distal weakness extending proximally, increasing sensory loss, worsening deformities, and occasionally additional complications such as neuropathic pain, falls, and surgical interventions.[6][10][16] Electrophysiologic measures may show gradually declining CMAP amplitudes and modest changes in NCV over time, reflecting cumulative axonal loss more than rapid demyelinating episodes.[16] HPO terms capturing temporal aspects include progressive muscle weakness (HP:0003323), progressive sensory neuropathy (HP:0003448), and slowly progressive course (HP:0003676). Critical periods of vulnerability include childhood and adolescence, when foot deformities develop, and mid-adulthood, when cumulative disability may necessitate mobility aids or orthopedic surgery.

### 3.6 Quality of Life Impact

Quality of life in CMTDIB is influenced by motor, sensory, and systemic manifestations. Cleveland Clinic emphasizes that CMT can affect movement and sensation and that "with the help of special devices and other kinds of care, it’s possible to do many of the things you love," but acknowledges that having a progressive condition can take a toll on mental health and recommends seeking mental health support if distress occurs.[10] These observations apply to DI-CMTB patients, who may face challenges in walking, balance, and hand function, leading to decreased participation in sports or hobbies and increased fatigue.[10][16]

In the Brain 2009 cohort, the relatively low rate of wheelchair dependence suggests a less severe impact on independence compared with many other neuromuscular disorders.[15][16] However, distal weakness and foot deformities often require orthotic devices, and patients may experience chronic pain, increased risk of falls, and difficulty with employment that involves physical labor, all of which negatively affect quality of life. Neutropenia and cataracts add further dimensions: recurrent infections and visual impairment can exacerbate disability and psychological burden.[15][16] While specific EQ-5D or SF-36 data for DI-CMTB are not available in the provided sources, studies of CMT more generally indicate moderate reductions in physical functioning scores and increased emotional distress, emphasizing the need for holistic care.[6][10]

HPO terms related to quality-of-life impact include fatigue (HP:0012378), chronic pain (HP:0012533), decreased ambulation (HP:0002540), and emotional instability (HP:0000741). Addressing these dimensions requires multidisciplinary management, including physical therapy, occupational therapy, orthopedic interventions, pain management, and psychological support.

## 4. Genetic and Molecular Information

### 4.1 Causal Gene and Basic Molecular Function

DNM2 (dynamin 2) is the sole gene with strong evidence of causality for CMTDIB. OMIM notes that CMTDIB and axonal CMT2M mapping to chromosome 19p are caused by heterozygous mutations in DNM2.[1] DNM2 encodes a large GTPase that mediates vesicle budding, organelle fission and fusion, and clathrin-coated endocytosis and cooperates with proteins such as actin, endophilin, and amphiphysin.[12] It is composed of multiple domains: an N-terminal GTPase domain, a middle domain, a lipophilic pleckstrin homology (PH) domain that interacts with membrane phosphatidylinositol 4,5-bisphosphate, a GTPase effector domain, and a proline/arginine-rich (PRD) domain at the C-terminus.[12] These domains coordinate to shape membrane curvature and drive vesicle scission, essential for endocytosis and intracellular trafficking.

DNM2 is ubiquitously expressed, including in Schwann cells, neurons, hematopoietic cells, and lens fibers, consistent with the multi-system phenotypes observed in some mutation carriers.[4][12][15][16] UniProt and gene ontology data (not directly provided in the search results but inferable from general knowledge) associate DNM2 with biological processes such as clathrin-mediated endocytosis (GO:0072583), synaptic vesicle recycling (GO:0099003), and regulation of membrane organization (GO:0061024), and with cellular components including cytoplasm (GO:0005737), plasma membrane (GO:0005886), and clathrin-coated pit (GO:0005905). 

### 4.2 Pathogenic Variant Spectrum

The spectrum of DNM2 pathogenic variants associated with CMTDIB includes multiple missense, in-frame deletion, and frameshift mutations affecting different domains. The Brain 2009 study identified six mutations in six families: Gly358Arg in the middle domain; Asp551_Glu553del, Lys550fs, Lys558del, and Lys558Glu in the PH domain; and Thr855_Ile856del in the proline-rich domain.[15][16] Gly358Arg and Thr855_Ile856del were novel at the time of publication, and Thr855_Ile856del represented the first disease-causing mutation in the proline-rich domain of dynamin 2, expanding the mutational landscape beyond the PH domain.[15][16] All mutations segregated with disease in their respective families and were absent in control populations, providing strong genetic evidence of pathogenicity.

The 2022 case report described a novel heterozygous missense mutation c.1609G>A (p.Gly537Ser) in exon 15 coding for the PH domain in two adult siblings and one child, all with CMT neuropathy phenotype consistent with DI-CMTB.[12] Genetic testing demonstrated that the c.1609G>A variant was present in the proband, her brother, and niece but absent in their father, supporting its segregation with disease.[12] ClinVar entry VCV000246295 confirms the existence of this variant and classifies it as pathogenic, noting that it alters glycine 537 to serine in the PH domain and has been observed in individuals with DNM2-related CMT.[18][12] The article emphasizes that this mutation "expands the repertoire of known mutations associated with autosomal dominant CMT neuropathy" and specifically DI-CMTB.[12]

Other DNM2 mutations cause distinct phenotypes. For example, autosomal dominant centronuclear myopathy (CNM) is frequently associated with DNM2 mutations clustered in specific residues within the PH domain or middle domain but with different functional effects on dynamin 2 activity.[4][13][14] Lethal congenital contractures syndrome type 5 and hereditary spastic paraplegia are also linked to particular DNM2 variants.[12][13] This heterogeneity underscores that both mutation position and functional consequence are critical for determining whether a DNM2 variant causes neuropathy, myopathy, or other phenotypes.

Variant types in CMTDIB include missense substitutions (e.g., Gly358Arg, Gly537Ser, Lys558Glu), in-frame deletions (e.g., Asp551_Glu553del, Lys558del, Thr855_Ile856del), and frameshift mutations (e.g., Lys550fs).[15][16][12] Most variants appear to be rare or private to specific families, consistent with a high degree of allelic heterogeneity. Population allele frequencies from gnomAD or similar databases are not explicitly given in the search results, but the absence of these variants in controls in the Brain 2009 and subsequent reports suggests that pathogenic DNM2 variants are extremely rare in the general population.[15][16][12][18]

### 4.3 Variant Classification and Functional Consequences

ClinVar and OMIM classify DNM2 variants associated with CMTDIB as pathogenic or likely pathogenic based on segregation, predicted functional impact, and consistency with known disease mechanisms.[1][18][12] The c.1609G>A (p.Gly537Ser) variant, for example, is labeled pathogenic in ClinVar, and the case report provides functional and clinical evidence supporting this classification.[12][18] Brain 2009 establishes pathogenicity for the six mutations studied via cosegregation, absence in controls, and consistency with neuropathy phenotypes.[15][16] Variants such as Lys558Glu and Lys558del have additional phenotype associations (neutropenia) that support a broader impact on DNM2 function.[15][16]

Mechanistic studies differentiate DNM2 mutations causing CMTDIB from those causing CNM. Sidiropoulos et al. noted that "mutations in dynamin 2 (DNM2) lead to dominant intermediate Charcot-Marie-Tooth neuropathy type B, while a different set of DNM2 mutations cause autosomal dominant centronuclear myopathy" and aimed to elucidate disease mechanisms in DI-CMTB and explain tissue-specific defects associated with different DNM2 mutations.[4] Using Dnm2-deficient mouse peripheral nerve tissue, they found that DNM2 mutants associated with DI-CMTB, but not CNM mutants, impaired myelination and caused defects in clathrin-mediated endocytosis in Schwann cells and neurons.[4] As a consequence, protein surface levels were altered in Schwann cells, and myelination was strictly dependent on Dnm2 and clathrin-mediated endocytosis function.[4] These results led them to propose that altered endocytosis is a major contributing factor to disease mechanisms in DI-CMTB.[4]

The Nature Communications 2025 study provides further insight, reporting that DNM2-CNM mutations are gain-of-function, increasing dynamin activity, whereas DNM2-CMT mutations are loss-of-function, reducing activity.[13] The authors combined a CNM mutation with a CMT mutation in DNM2 in vivo and observed mutual compensation, leading to correction of most phenotypes, thereby experimentally validating opposite functional directions.[13] These findings suggest that CMTDIB pathogenic variants cause partial loss of dynamin 2 function, particularly in clathrin-mediated endocytosis and membrane remodeling in Schwann cells and peripheral neurons, which leads to impaired myelination and axonal support.

From an ACMG/AMP standpoint, DNM2 variants in CMTDIB can be classified as pathogenic based on the following criteria: strong segregation (PS4), functional studies supporting damaging effect (PS3), location in a well-established functional domain (PM1), absence from controls in large databases (PM2), and well-established disease-gene relationship (PP1).[4][13][15][16][18] Functional consequences fall under loss-of-function (hypomorphic) effects in endocytosis and myelination pathways rather than truncating loss-of-function causing complete absence of protein, as many variants are missense or in-frame deletions.[4][13][15][16][12]

### 4.4 Somatic vs Germline Origin and Mosaicism

CMTDIB is caused by germline heterozygous mutations in DNM2 transmitted in autosomal dominant fashion. All reported families show vertical transmission from affected parent to affected child, with approximately 50% of offspring inheriting the variant, consistent with germline origin.[1][15][16][12] There is no evidence that somatic DNM2 mutations restricted to peripheral nerves or muscle cause CMTDIB; such somatic mutations, if they exist, would likely manifest differently and have not been described in the CMT literature. COSMIC and cancer-related datasets, which catalog somatic mutations, are not relevant to this hereditary neuropathy.

Germline mosaicism has not been systematically studied in CMTDIB, but as with other autosomal dominant disorders, it is theoretically possible that a parent could have somatic mosaicism for a DNM2 pathogenic variant and transmit it to a child, leading to apparent de novo cases.[6] The c.1609G>A case report notes that the variant was absent in the father but present in the offspring, suggesting either a de novo event in the proband or maternal transmission from an affected or mosaic mother; the available snippet indicates absence in the father but does not clarify maternal genotype.[12][18] As such, while mosaicism cannot be excluded, most DNM2 mutations in CMTDIB are inherited.

### 4.5 Modifier Genes, Epigenetic and Chromosomal Abnormalities

No specific modifier genes have been conclusively identified for CMTDIB. Some DNM2 mutations produce additional phenotypes such as neutropenia and cataracts, indicating that mutation-specific effects, possibly mediated by differential domain involvement or altered protein–protein interactions, can modify clinical expression.[15][16] However, these modifiers are intrinsic to the DNM2 mutation itself rather than separate genetic loci. Background variation in other neuropathy genes may influence severity in individual patients, but large-scale studies evaluating this possibility have not been published.[6]

Epigenetic changes, such as DNA methylation or histone modifications affecting DNM2 expression, have not been implicated in CMTDIB. ENCODE and Roadmap Epigenomics projects provide general epigenomic maps, but no specific data link epigenetic dysregulation of DNM2 to CMT phenotypes in humans in the available sources. Similarly, large-scale chromosomal abnormalities (aneuploidy, translocations, inversions) involving chromosome 19p13.2 have not been reported as causes of CMTDIB; instead, pathogenic lesions are point mutations and small indels within the DNM2 coding sequence.[1][12][18] DECIPHER and structural variant databases may catalog 19p13.2 rearrangements, but such variants have not been associated with classical DI-CMTB phenotypes in the literature referenced here.

In summary, the genetic and molecular foundation of CMTDIB is a set of rare, highly penetrant germline DNM2 variants that partially disrupt dynamin 2’s role in clathrin-mediated endocytosis and myelination, leading to a characteristic intermediate neuropathy with occasional systemic manifestations.

## 5. Environmental Information

### 5.1 Non-Genetic Contributing Factors

Given that CMTDIB is a Mendelian disorder caused by DNM2 mutations, non-genetic contributing factors play a relatively minor role in disease onset but may modulate disease severity and progression. No specific environmental toxins, radiation exposures, or pollutants have been implicated as triggers of CMTDIB in individuals without DNM2 mutations.[1][4][6] General environmental contributors to neuropathy, such as chronic exposure to heavy metals, solvents, or chemotherapy agents, can exacerbate underlying nerve dysfunction but do not cause CMTDIB per se.[6][10]

In clinical practice, neurologists often advise individuals with hereditary neuropathy to avoid neurotoxic medications, particularly vincristine, which is known to cause severe neuropathy in patients with underlying CMT, especially CMT1A.[6] Although explicit data for DNM2-related CMT are limited, similar caution is reasonable. Alcohol overuse and uncontrolled diabetes can worsen peripheral nerve function and are therefore considered modifiable environmental factors that may increase morbidity in CMTDIB patients.[6][10] However, no studies provide quantitative data on such interactions specifically in DNM2-mutant cohorts.

Lifestyle factors such as physical activity, diet, and smoking may influence general health and vulnerability to complications but have not been directly tied to CMTDIB pathophysiology. Smoking is known to impair microvascular perfusion, which could theoretically exacerbate neuropathy, whereas regular low-impact exercise might help maintain muscle strength and reduce functional decline.[6][10] Again, these relationships are extrapolated from broader neuromuscular literature rather than disease-specific studies.

### 5.2 Infectious Agents and Co-morbidities

There is no evidence that infectious agents directly cause or trigger CMTDIB. Unlike postinfectious neuropathies such as Guillain–Barré syndrome or CIDP, CMTDIB arises from germline genetic defects and follows a chronic, slowly progressive course without acute postinfectious onset.[6][10][16] Nevertheless, neutropenia observed in some DNM2-mutant families increases susceptibility to bacterial infections and potentially to viral infections, making infectious complications an important morbidity factor.[15][16] In these cases, infections exacerbate disability and may require prophylactic antibiotics or granulocyte colony-stimulating factor, but they are not primary etiologic factors for the neuropathy itself.

Co-morbidities such as diabetes, autoimmune disorders, or thyroid dysfunction may coexist with CMTDIB, as they do in the general population, and could contribute to neuropathy severity. However, no data indicate increased prevalence of such co-morbidities in DNM2-mutant patients. Management of co-morbid conditions remains important for optimizing overall nerve health and function.

### 5.3 Gene–Environment Context

In summary, environmental and lifestyle factors in CMTDIB mainly modulate clinical course rather than act as primary causes. Avoidance of neurotoxins, control of metabolic risk factors, and maintenance of physical fitness can be considered supportive measures to reduce secondary nerve damage and maximize functional capacity.[6][10] The causal chain remains fundamentally genetic, rooted in DNM2 mutations, and no environmental exposures have been demonstrated to initiate CMTDIB in non-carriers.

## 6. Mechanism and Pathophysiology

### 6.1 Molecular Pathways: Clathrin-Mediated Endocytosis and Myelination

The central pathophysiologic mechanism in CMTDIB involves disruption of clathrin-mediated endocytosis (CME) and related membrane remodeling processes in Schwann cells and peripheral neurons due to DNM2 loss-of-function mutations. Dynamin 2 is a mechanoenzyme that assembles at the neck of budding vesicles, hydrolyzes GTP, and drives membrane scission, thus completing endocytic events.[12][4][13] In Schwann cells, CME regulates the internalization and recycling of surface receptors and adhesion molecules that are critical for myelination and axonal support.

Sidiropoulos et al. conducted a mechanistic study using tissue from Dnm2-deficient mice to model peripheral nerve features and assess the impact of disease-associated DNM2 mutations.[4] They report:

> "Mutations in dynamin 2 (DNM2) lead to dominant intermediate Charcot-Marie-Tooth neuropathy type B, while a different set of DNM2 mutations cause autosomal dominant centronuclear myopathy… We used tissue derived from Dnm2-deficient mice to establish an appropriate peripheral nerve model and found that dominant intermediate Charcot-Marie-Tooth neuropathy type B-associated dynamin 2 mutants, but not autosomal dominant centronuclear myopathy mutants, impaired myelination. In contrast to autosomal dominant centronuclear myopathy mutants, Schwann cells and neurons from the peripheral nervous system expressing dominant intermediate Charcot-Marie-Tooth neuropathy mutants showed defects in clathrin-mediated endocytosis. We demonstrate that, as a consequence, protein surface levels are altered in Schwann cells. Furthermore, we discovered that myelination is strictly dependent on Dnm2 and clathrin-mediated endocytosis function. Thus, we propose that altered endocytosis is a major contributing factor to the disease mechanisms in dominant intermediate Charcot-Marie-Tooth neuropathy type B."[4]

This quote encapsulates the causal chain: DNM2 mutations impair CME in Schwann cells and neurons, leading to altered surface protein levels (e.g., receptors and adhesion molecules), which in turn disrupt myelination. As myelin sheaths are essential for high-speed conduction and axonal survival, these defects produce mixed demyelinating and axonal neuropathy, reflected in intermediate NCV and loss of large myelinated fibers.[16] GO terms relevant to these processes include clathrin-mediated endocytosis (GO:0072583), myelination (GO:0042552), regulation of neuron projection development (GO:0010975), and axon ensheathment (GO:0008366).

The PH domain of DNM2 binds membrane phosphatidylinositol 4,5-bisphosphate (PIP2), a critical lipid in plasma membrane signaling and CME.[12][13] Mutations in the PH domain (e.g., Asp551_Glu553del, Lys558Glu, Gly537Ser) alter DNM2’s membrane-binding properties, thereby impairing endocytic vesicle formation and scission. CHEBI terms relevant to this aspect include phosphatidylinositol 4,5-bisphosphate (CHEBI:18348). Dysfunctional interaction between dynamin 2 and PIP2 or other membrane lipids in Schwann cells likely underlies the impaired myelination observed in DNM2-mutant mice and humans.[4][12][13][16]

### 6.2 Cellular Processes: Schwann Cell and Neuron Dysfunction

At the cellular level, CMTDIB pathophysiology involves Schwann cell dysfunction, impaired axon–Schwann cell communication, and axonal degeneration. Schwann cells, the myelinating glia of the peripheral nervous system, rely on precise endocytic regulation to modulate receptors for axonal signals (e.g., neuregulins) and to maintain myelin membrane composition. In DNM2-mutant Schwann cells, CME and internalization of such receptors are impaired, leading to aberrant signaling, defective myelin formation, and shorter or unstable internodes.[4][16] CL terms appropriate for these cell types include Schwann cell (CL:0000540), peripheral neuron (CL:0000107), and myelinating Schwann cell (CL:0000749).

Sidiropoulos et al. showed that Schwann cells and neurons expressing DI-CMTB mutants exhibited distinct defects in CME compared to CNM-associated mutants.[4] This indicates that DNM2 mutations exert cell-type–specific effects: CMT mutations predominantly disrupt Schwann cell endocytosis and myelination, whereas CNM mutations primarily affect skeletal muscle cells and T-tubule formation.[4][13][14] The downstream consequences in CMTDIB include axonal degeneration, as myelin defects compromise metabolic support and trophic signaling to axons, leading to length-dependent axon loss and sensory and motor deficits.[16]

Apoptosis and autophagy may be secondary processes contributing to nerve degeneration. Chronic endocytic dysfunction may lead to accumulation of mislocalized receptors and damaged membranes, activating stress pathways and potentially triggering Schwann cell apoptosis or axonal degeneration, although direct evidence for apoptosis in DNM2-mutant peripheral nerves is limited.[4][16] GO terms that may capture these downstream processes include axon degeneration (GO:0030425), regulation of apoptotic process (GO:0042981), and response to endoplasmic reticulum stress (GO:0034976).

### 6.3 Protein Dysfunction: Loss-of-Function vs Gain-of-Function Dynamics

The distinction between DNM2 mutations causing CMTDIB and those causing CNM is mechanistically important. Sidiropoulos et al. and the Nature Communications study collectively suggest that DNM2-CMT mutations are loss-of-function, particularly in CME and myelination, whereas DNM2-CNM mutations are gain-of-function, increasing dynamin activity in muscle cells.[4][13][14] The Nature Communications article states that "our in vitro and in vivo data shed light on the pathomechanism and support that DNM2-CNM mutations are gain-of-function while DNM2-CMT are loss-of-function."[13]

In CMTDIB, missense or in-frame deletions in the PH domain or middle domain reduce DNM2’s ability to bind membranes or oligomerize properly, thereby impairing vesicle scission. In the case of Gly537Ser or Lys558Glu, structural modeling suggests altered PH domain conformation, reducing affinity for PIP2 and thereby hampering recruitment to the plasma membrane.[12][13] Brain 2009 notes that Gly358Arg and Thr855_Ile856del represent novel site-specific alterations in the middle and proline-rich domains, respectively, indicating that multiple domains can be affected and that these changes have specific impacts on dynamin 2’s interactions with binding partners and regulatory proteins.[15][16]

Protein dysfunction is thus characterized by hypomorphic DNM2 activity in Schwann cells and neurons, leading to incomplete or inefficient CME and myelination. This partial loss-of-function fits well with the intermediate electrophysiologic phenotype and mild to moderate clinical severity: dynamin 2 function is not completely absent, but reduced to levels incompatible with fully normal peripheral nerve function.[4][13][16] In contrast, CNM mutants may increase dynamin 2’s propensity to oligomerize or hydrolyze GTP, causing excessive membrane fission in muscle cells and disrupting T-tubule architecture.[13][14]

### 6.4 Metabolic and Biochemical Changes

Direct metabolic changes in CMTDIB have not been extensively characterized. Unlike mitochondrial neuropathies or metabolic disorders where specific enzyme deficiencies lead to bioenergetic failure, DNM2-related neuropathy centers on membrane trafficking and myelination. However, impaired CME and membrane recycling may indirectly affect metabolic processes in Schwann cells and neurons by altering receptor signaling for growth factors and trophic support, which could influence glucose uptake and lipid metabolism needed for myelin synthesis.[4][16]

Myelin formation requires substantial lipid and cholesterol synthesis, and disruption of myelination in CMTDIB suggests altered local lipid metabolism in Schwann cells. Lipidomics signatures have not been explicitly reported but would be a promising avenue for future study. KEGG pathways involving endocytosis (hsa04144) and axon guidance (hsa04360) may be relevant, and interplay with metabolic pathways such as fatty acid metabolism (hsa01212) and sphingolipid metabolism (hsa00600) could be inferred. Biochemical abnormalities at the molecular level include defective CME (a functional defect rather than a classical enzyme deficiency) and receptor dysfunction due to altered trafficking. UniProt data on dynamin 2 note its GTPase activity, so mutations may also influence GTP hydrolysis kinetics, but specific enzymatic data for CMTDIB mutants are not provided in the available sources.[4][12][13]

### 6.5 Immune System Involvement and Tissue Damage Mechanisms

Immune system involvement in CMTDIB is primarily indirect through neutropenia in certain DNM2-mutant families. Neutropenia suggests impaired granulopoiesis or increased neutrophil apoptosis, potentially linked to DNM2’s role in CME in hematopoietic cells. Brain 2009 notes that in Australian and Belgian families with Lys558 mutations, neutropenia co-segregated with CMT.[15][16] This implies that DNM2 dysfunction can also affect immune cell trafficking, receptor expression, or survival. However, CMTDIB is not an autoimmune neuropathy; there is no evidence of immune-mediated attack on peripheral nerves, no demyelinating episodes consistent with CIDP, and no autoantibodies identified as disease drivers.[16]

Tissue damage mechanisms in peripheral nerves involve chronic myelin defects and axonal degeneration. Loss of large myelinated fibres, presence of clusters of regenerating myelinated axons, and focal myelin thickenings observed in sural nerve biopsies reflect repeated cycles of damage and repair.[16] Oxidative stress and mitochondrial dysfunction may contribute secondarily to axonal degeneration, as is common in chronic neuropathies, but specific data for DNM2-mutant nerves are not available in the sources provided.[4][16] GO terms such as myelin sheath (GO:0043209), axon (GO:0030424), and response to oxidative stress (GO:0006979) capture processes likely involved, but further mechanistic studies would be needed to detail oxidative or inflammatory contributions.

### 6.6 Molecular Profiling and Advanced Technologies

The available literature does not report comprehensive transcriptomic, proteomic, metabolomic, or single-cell profiling specifically for human CMTDIB tissues. However, Sidiropoulos et al. used in vitro analyses of Schwann cells and neurons expressing DNM2 mutants to study CME, indicating that functional genomics approaches can elucidate disease mechanisms.[4] Their work likely involved imaging, biochemical assays, and possibly proteomic analysis of surface proteins, but explicit omics datasets are not mentioned in the abstract.[4]

The Nature Communications 2025 study represents an advanced mechanistic investigation, combining mouse models with in vitro assays to analyze phenotypic rescue by dual mutations.[13] This multi-omics integration at the experimental level demonstrates how DNM2 functional states influence cellular phenotypes, though specific transcriptomic or proteomic datasets are not detailed in the provided snippet.[13] Single-cell analysis of peripheral nerve cell types, spatial transcriptomics of nerve biopsies, or CRISPR-based screens targeting DNM2 interactors have not yet been reported for CMTDIB in the sources provided, but they represent promising future directions.

In summary, the mechanism and pathophysiology of CMTDIB pivot on DNM2 loss-of-function mutations that impair clathrin-mediated endocytosis in Schwann cells and neurons, leading to defective myelination, axonal degeneration, and intermediate neuropathy, with occasional systemic manifestations such as neutropenia and cataracts. This causal chain from gene mutation to cellular dysfunction to clinical phenotype is supported by human biopsies and mouse models.

## 7. Anatomical Structures Affected

### 7.1 Organ-Level Involvement

The primary organ system affected in CMTDIB is the peripheral nervous system (PNS), particularly the somatic motor and sensory nerves of the distal limbs. UBERON terms relevant include peripheral nervous system (UBERON:0000010) and peripheral nerve (UBERON:0003700). Peripheral nerve damage leads to secondary involvement of skeletal muscle, manifested as distal muscle atrophy in the legs and arms, but muscle pathology is secondary to denervation rather than primary myopathic changes.[6][15][16]

Body systems involved include the nervous system, musculoskeletal system, immune system (in neutropenia-associated variants), and visual system (cataracts). The musculoskeletal system shows structural changes such as pes cavus, hammer toes, scoliosis, and joint contractures due to chronic imbalanced muscle forces.[6][8][10][16] The immune system involvement manifests as decreased neutrophil counts, potentially increasing infection risk and involving hematopoietic tissues like bone marrow.[15][16][1] Lens involvement in cataracts indicates ocular system and crystalline lens pathology.[15][16]

Cardiovascular, digestive, and respiratory systems are not directly affected by CMTDIB; however, mobility limitations and chronic disease can indirectly impact cardiovascular fitness and respiratory mechanics through reduced physical activity. Endocrine system involvement has not been reported. Overall, the disease is localized primarily to peripheral nerves and associated structures.

### 7.2 Tissue and Cell-Level Involvement

At the tissue level, CMTDIB affects nervous tissue, particularly myelinated peripheral nerve fibers, and connective tissue structures in the feet and hands. Myelinated axons and their myelin sheaths, produced by Schwann cells, are the principal sites of pathology, as reflected in sural nerve biopsy findings and electrophysiologic abnormalities.[16] Skeletal muscle tissue undergoes denervation atrophy, especially in distal muscles such as the peroneal group and intrinsic hand muscles.[6][15][16]

Cell types involved include Schwann cells, which form the myelin sheath; peripheral motor and sensory neurons; neutrophils (in neutropenia-associated variants); and lens fiber cells (in cataract-associated variants).[4][15][16] CL terms for these cell types include Schwann cell (CL:0000540), peripheral neuron (CL:0000107), neutrophil (CL:0000775), and lens fiber cell (CL:0000738). DNM2 is expressed in these cells, and its dysfunction manifests differently depending on cell type and domain affected, explaining the nerve-restricted phenotype in most variants and the multi-system phenotype in some.

### 7.3 Subcellular Compartments and Localization

At the subcellular level, CMTDIB impacts cellular compartments involved in endocytosis and membrane trafficking. DNM2 localizes to the cytoplasm and plasma membrane, particularly at clathrin-coated pits, and to intracellular vesicles.[12][4][13] GO cellular component terms include clathrin-coated pit (GO:0005905), coated vesicle (GO:0030136), cytoplasmic vesicle (GO:0031410), and plasma membrane (GO:0005886). Mutations in DNM2 alter its recruitment to these structures, impairing vesicle scission and CME.

Localization of nerve damage is length-dependent and symmetric, affecting distal segments of peripheral nerves first. Clinically, this manifests as a stocking–glove distribution of motor and sensory deficits, with bilateral symmetry and distal predominance.[6][10][15][16] HPO terms reflecting this pattern include distal symmetric polyneuropathy (HP:0005529). There is no unilateral or focal involvement typical of compressive neuropathies; instead, CMTDIB follows the classic diffuse hereditary neuropathy pattern.

## 8. Temporal Development

### 8.1 Onset: Age and Pattern

CMTDIB onset is typically chronic and insidious, beginning with subtle distal weakness or clumsiness in childhood or adolescence. Brain 2009 reports a mean age at onset of \(16\) years, with a range of \(2\) to \(50\) years across 34 patients, indicating pediatric to adult onset.[15][16] The youngest cases may present with delayed motor milestones or early foot deformities, while adult-onset cases may notice progressive weakness or sensory symptoms in their 30s or 40s.[15][16] GeneReviews similarly notes that CMT generally has onset in the first or second decade, especially for dominant forms.[6]

The onset pattern is chronic rather than acute. There are no rapid-onset episodes like those seen in Guillain–Barré syndrome; instead, symptoms emerge slowly over months to years. Early signs include tripping, ankle sprains, difficulty running, and foot deformities; sensory loss may be subtle initially.[6][10][16] Electrophysiologic abnormalities may precede overt clinical symptoms in some carriers, but systematic pre-symptomatic NCV screening data are limited. HPO term for insidious onset is insidious onset (HP:0003819).

### 8.2 Progression: Stages and Rate

Disease progression in CMTDIB is slow and lifelong, with gradual worsening of distal weakness, sensory loss, and deformities. While formal staging systems for CMTDIB have not been established, one can conceptually distinguish early stages (mild distal weakness and foot deformities), intermediate stages (pronounced distal weakness, balance difficulties, hand involvement), and advanced stages (severe distal weakness, potential need for walking aids, significant hand disability).[6][10][15][16] Brain 2009’s observation that only 3% of patients were wheelchair-bound suggests that most individuals remain in early or intermediate stages for many years.[15][16]

Progression rate varies among individuals and families, influenced by mutation type and possibly other genetic and environmental factors. NCV and CMAP measurements may show gradual declines over decades, reflecting ongoing axonal loss.[16] There is no relapsing-remitting pattern; the course is monotonic and progressive. HPO terms relevant to progression include slowly progressive course (HP:0003676) and lifelong persistence (HP:0003699).

### 8.3 Disease Duration and Course Pattern

CMTDIB is a chronic lifelong condition. Once symptoms appear, they persist and gradually worsen; there is no spontaneous resolution. GeneReviews emphasizes that hereditary neuropathies including CMT are chronic and that disease duration spans decades.[6] Cleveland Clinic notes that CMT "rarely affect[s] how long you live," reinforcing that disease is long-lasting but not typically life-shortening.[10]

Course pattern is progressive, with no known remissions. Treatment-induced improvements may occur in functional capacity (e.g., with orthotics or physical therapy), but they do not reverse the underlying neuropathy. Disease course may plateau in late adulthood when maximal nerve damage has occurred, but data on late-stage progression in DNM2-mutant cohorts are limited.

### 8.4 Remission Patterns and Critical Periods

Spontaneous or treatment-induced remission is not characteristic of CMTDIB. Supportive therapies can slow functional decline and improve quality of life but do not induce remission in the neurological sense.[6][10] Critical periods of vulnerability include growth phases in childhood and adolescence, when skeletal deformities can worsen, and early adulthood, when cumulative nerve damage may begin to significantly impact function and occupational abilities.[6][10][16] Early intervention with orthotics and physical therapy during these periods can mitigate deformities and optimize long-term outcomes.

From a developmental biology perspective, the window of active myelination in peripheral nerves, which continues into adolescence, may represent a critical period during which DNM2 dysfunction exerts maximal effects on myelin formation. Sidiropoulos et al.'s demonstration that myelination is strictly dependent on Dnm2 and CME underscores the importance of this developmental window.[4]

## 9. Inheritance and Population

### 9.1 Inheritance Pattern, Penetrance, and Expressivity

CMTDIB follows an autosomal dominant inheritance pattern. OMIM and GeneReviews both emphasize that autosomal dominant CMT, including DNM2-related forms, confer a 50% risk to offspring of affected individuals.[1][6] DNM2 mutations in CMTDIB are heterozygous; homozygous or compound heterozygous states have not been described and may be deleterious or lethal.[1][4][12]

Penetrance appears high but age-dependent. In the Brain 2009 families, nearly all heterozygous carriers of DNM2 mutations exhibited neuropathic signs by adulthood, although severity varied and some had very mild symptoms.[15][16] Age-dependent penetrance means that a young child carrying a DNM2 mutation may be asymptomatic but will likely develop clinical features over time. Expressivity is variable: the age of onset, severity of weakness and sensory loss, degree of deformities, and presence of systemic features (neutropenia, cataracts) differ between individuals, even within families carrying the same mutation.[15][16]

Genetic anticipation, characterized by earlier onset or increased severity in successive generations, is not reported in CMTDIB and is not expected given that DNM2 mutations are point mutations rather than repeat expansions. Germline mosaicism may occur rarely, but most cases are inherited rather than de novo.[6][12] Consanguinity does not play a particular role, as the disease is dominant; however, consanguinity could increase the likelihood of other recessive neuropathic conditions co-occurring.

### 9.2 Epidemiology: Prevalence and Incidence

Specific prevalence and incidence figures for CMTDIB are not available in the provided sources. Overall CMT prevalence is estimated at approximately 1 in 2,500 individuals in some populations, but DNM2-related forms constitute only a small fraction of CMT cases.[6][10] Orphanet considers intermediate CMT subtypes, including DI-CMTB, to be rare hereditary neuropathies.[7][8][11] The rarity of reported DNM2-mutant families (six families in the Brain 2009 cohort, plus several subsequent case reports) suggests that CMTDIB may have a prevalence in the range of a few per million or fewer, though precise estimates would require large genetic screening studies.

Incidence, defined as new cases per year, is similarly unknown for DI-CMTB. Given the autosomal dominant inheritance and family clustering, incidence is largely determined by reproduction within affected families rather than random new mutations. De novo mutations such as c.1609G>A may contribute sporadic cases.[12][18] Population-based registries for CMT do not typically report subtype-specific incidence figures for DNM2-related disease.

### 9.3 Population Demographics: Sex, Age, Ethnicity, and Geography

Sex ratio in CMTDIB appears to be roughly equal, consistent with autosomal inheritance. The Brain 2009 cohort included both male and female patients with similar phenotypes; no sex-specific differences are reported.[15][16] Age distribution among affected individuals reflects the range of onset ages and the lifelong nature of the disease; individuals in childhood, adolescence, and adulthood are all represented.[15][16]

Ethnic and geographic distribution of specific DNM2 variants shows some clustering. Gly358Arg was initially reported in a Spanish family, Asp551_Glu553del and Lys550fs in North American families, Lys558del in a Belgian family, Lys558Glu in Australian and Dutch families, and Thr855_Ile856del in a Belgian family.[15][16] The c.1609G>A (p.Gly537Ser) mutation was described in a family of unspecified nationality in the 2022 report.[12] These data suggest that many DNM2 mutations are family-specific and arise independently in different populations, rather than being widespread founder mutations. No particular ethnic group is known to have significantly higher prevalence of DNM2-related CMT.

Geographically, CMTDIB has been described in Europe (Spain, Belgium, Netherlands), North America, and Australia, reflecting its presence in diverse populations.[15][16] Global variation in prevalence may exist but is likely driven by opportunity for genetic diagnosis and referral patterns to neuromuscular centers, rather than actual differences in underlying gene mutation rates.

### 9.4 Carrier Frequency and Founder Effects

Carrier frequency for specific DNM2 pathogenic variants is extremely low in the general population, given that CMTDIB is rare and most mutations are private to individual families.[15][16][12][18] gnomAD and similar population databases have not reported these variants in controls, or report them at extremely low frequencies, supporting their classification as rare deleterious alleles.[18][12] Consequently, carrier screening for DNM2 mutations is not performed routinely except in families with known disease.

Founder effects, where a single mutation becomes prevalent in a specific population due to historical factors, have not been clearly documented for DNM2-related CMT. While some families with the same mutation (e.g., Lys558Glu) exist in both Australia and the Netherlands, this may reflect shared ancestry or independent mutation events.[15][16] Larger haplotype analysis would be required to determine founder status; such data are not provided in the available sources.

## 10. Diagnostics

### 10.1 Clinical Evaluation and Electrophysiology

Diagnostic evaluation of CMTDIB begins with clinical assessment of neuropathic symptoms, signs, and family history. The presence of distal muscle weakness, atrophy, sensory loss, reduced reflexes, and foot deformities, especially in the setting of autosomal dominant family clustering, prompts consideration of CMT.[6][10][15][16] Cleveland Clinic notes that CMT usually affects muscle control and sensation in the feet and hands, and that neurologic examination can identify weakness and sensory deficits.[10] GeneReviews emphasizes the importance of detailed neurologic evaluation and documentation of family history across multiple generations.[6]

Electrophysiologic testing with nerve conduction studies (NCS) and electromyography (EMG) is essential. In CMTDIB, median motor nerve NCV typically fall into the intermediate range, from about \(26\) m/s to normal values, with many patients showing NCVs between \(35\) and \(45\) m/s.[6][16] CMAP amplitudes may be normal or reduced, depending on severity and specific family.[16] The combination of intermediate or slightly reduced NCV with reduced CMAPs and distal sensory responses supports a diagnosis of intermediate CMT rather than pure demyelinating or axonal CMT.[16] Somatosensory evoked potentials can show attenuated sensory nerve action potentials and delayed cortical responses in severe cases.[16]

Electrophysiologic data help distinguish CMTDIB from other neuropathies. Demyelinating CMT1A typically shows NCV below \(38\) m/s with marked slowing and demyelinating features on EMG, whereas axonal CMT2 shows normal or slightly reduced NCV with reduced CMAP amplitudes.[16][6] Acquired demyelinating neuropathies like CIDP show conduction blocks and temporal dispersion, which are generally absent in CMTDIB.[16] LOINC codes can be used to identify specific NCS and EMG tests in EHR systems, although these are not detailed in the provided sources.

### 10.2 Biopsy Findings

Sural nerve biopsy is not routinely required for diagnosing hereditary neuropathy but can be useful in atypical cases or when genetic testing is inconclusive. In DNM2-mutant CMTDIB, sural nerve biopsy reveals diffuse loss of large myelinated fibres, clusters of regenerating myelinated axons, and focal myelin thickenings, without onion bulb formations.[16] These findings correspond to a chronic mixed demyelinating and axonal neuropathy with ongoing remyelination and regeneration, consistent with intermediate CMT.[16]

Histopathology can help differentiate CMTDIB from other neuropathies. For example, CMT1A shows numerous onion bulbs due to repeated cycles of demyelination and remyelination, whereas CMTDIB lacks these structures.[8][16][19] Inflammatory neuropathies show perivascular inflammatory infiltrates and macrophage-mediated demyelination, which are not features of hereditary DNM2-related neuropathy.[16] SNOMED CT and pathology ontologies can represent these histologic features for structured reporting.

### 10.3 Genetic Testing and Omics-Based Diagnostics

Genetic testing is the definitive diagnostic tool for CMTDIB. GeneReviews notes that more than 80 genes are associated with CMT and recommends genetic testing to confirm diagnosis and guide counseling.[6] For CMTDIB, sequencing of DNM2 is required, ideally as part of a comprehensive CMT gene panel. The presence of a heterozygous pathogenic or likely pathogenic DNM2 variant in an individual with compatible clinical and electrophysiologic phenotype confirms the diagnosis.[1][12][15][16][18]

Single-gene testing of DNM2 may be indicated when phenotype strongly suggests DI-CMTB, especially in families with neutropenia or early cataracts, as Brain 2009 recommends screening DNM2 in autosomal dominant CMT families with intermediate or axonal NCV and these systemic features.[16] However, given the wide genetic heterogeneity of CMT, many centers now use multigene panels or whole-exome sequencing (WES) for undifferentiated hereditary neuropathy, which efficiently capture DNM2 alongside other CMT genes.[6] Whole-genome sequencing (WGS) is useful for detecting non-coding or structural variants but may not be necessary for DNM2 coding variants, which are typically point mutations or small indels.[1][12][18]

Chromosomal microarray, karyotyping, FISH, and mitochondrial DNA testing are generally not relevant for CMTDIB, as large-scale chromosomal abnormalities or mitochondrial mutations are not implicated.[1][6] Repeat expansion testing is reserved for diseases like Huntington disease or some spinocerebellar ataxias and is not pertinent to DNM2-related CMT. Omics-based diagnostics such as RNA sequencing or proteomics have not yet entered routine clinical practice for CMTDIB but may in the future provide deeper insights into disease mechanisms.

### 10.4 Clinical Criteria and Differential Diagnosis

Standardized diagnostic criteria for CMTDIB specifically are not formally codified in international guidelines, but diagnostic features include autosomal dominant family history, classical CMT phenotype, intermediate NCV, and confirmed DNM2 mutation.[1][6][15][16] ICD-11 and ICD-10 code patients under hereditary neuropathy categories but do not differentiate subtypes. UpToDate and neuromuscular society guidelines emphasize the need for integrating clinical, electrophysiologic, and genetic data.[9][6]

Differential diagnosis includes other hereditary neuropathies such as CMT1A (PMP22 duplication), CMT2A (MFN2 mutations), intermediate CMT types C and D (YARS1 and MPZ mutations), and X-linked CMT1X (GJB1 mutations).[2][3][6][8][19] These subtypes can mimic CMTDIB clinically but differ in electrophysiologic pattern and genetic basis. For acquired neuropathies, CIDP, diabetic neuropathy, toxic neuropathies, and vasculitic neuropathies must be considered. CIDP presents with proximal weakness, conduction block, elevated CSF protein, and inflammatory findings on biopsy; diabetic neuropathy includes metabolic risk factors and distinct clinical patterns. The absence of inflammatory markers, metabolic derangements, and conduction block, combined with family history and DNM2 mutation, supports CMTDIB.

### 10.5 Screening and Cascade Testing

Population-wide screening for DNM2 mutations is not performed given the rarity of CMTDIB. However, cascade genetic testing in families with known DNM2 mutations is advisable. GeneReviews recommends that once a pathogenic variant is identified in a proband, testing of at-risk relatives should be offered to clarify their carrier status and enable early intervention.[6] As autosomal dominant inheritance implies a 50% risk to offspring, prenatal or preimplantation genetic diagnosis may be considered in family planning decisions.[6]

Newborn screening is not conducted for CMTDIB or CMT in general, as early detection does not currently lead to specific disease-modifying interventions. Carrier screening in the general population is not indicated due to low carrier frequency and absence of pre-symptomatic therapies.

## 11. Outcome and Prognosis

### 11.1 Survival and Life Expectancy

CMTDIB, like most forms of CMT, rarely affects life expectancy. Cleveland Clinic states that CMT "rarely affect[s] how long you live," emphasizing that while it is a progressive condition, it is not typically life-threatening.[10] GeneReviews similarly describes hereditary neuropathies as chronic but not usually associated with increased mortality.[6] Brain 2009 does not report early mortality in its DNM2-mutant cohort, and the relatively mild to moderate severity of neuropathy suggests that survival is near-normal.[15][16]

Mortality directly attributable to CMTDIB is extremely rare, and disease-specific mortality statistics are not available. Indirect mortality could occur through complications such as severe infections in neutropenia, but this has not been systematically documented. Overall, CMTDIB is best characterized as a disabling rather than lethal disease.

### 11.2 Morbidity, Disability, and Quality of Life

Morbidity in CMTDIB arises from chronic distal weakness, sensory loss, deformities, and systemic complications in some variants. Patients may have difficulty walking, balancing, running, using their hands for fine tasks, and may develop chronic pain.[6][10][15][16] Foot deformities can cause gait instability, predispose to falls and sprains, and require orthotic or surgical treatment.[6][8][10] Hand weakness can limit occupational choices and everyday activities such as writing and tool use.[15][16]

Disability outcomes vary widely. Brain 2009 notes that only 3% of patients were wheelchair-bound, indicating that most maintain some level of independent ambulation, albeit often with braces or walking aids.[15][16] However, the presence of neutropenia increases infection risk, potentially leading to hospitalizations and functional decline, while cataracts can impair vision and necessitate surgery.[15][16] Psychological morbidity, including depression and anxiety, can arise from coping with a progressive hereditary condition.[10]

Quality of life measures such as EQ-5D or SF-36 have not been specifically reported for DI-CMTB in the sources provided, but broader CMT studies show moderate reductions in physical function domains and variable impact on emotional and social functioning.[6][10] Cleveland Clinic emphasizes that mental health support is important and that "having a condition that gets worse over time can take a toll on your mental health."[10] These considerations highlight the need for comprehensive rehabilitative and psychosocial care.

### 11.3 Disease Course, Complications, and Recovery Potential

The disease course is chronic and gradually progressive. Complications include foot deformities requiring surgery, joint contractures, falls and fractures, neuropathic pain, infections in neutropenia, and visual impairment from cataracts.[6][10][15][16] Recovery potential is limited in terms of reversing neuropathic damage, but functional improvements are possible through rehabilitation and assistive devices. Muscle strength can be partially maintained or improved, and pain and deformities can be managed, enhancing quality of life.[6][10]

Prognostic factors include age at onset, severity of NCV and CMAP abnormalities, mutation type, and presence of systemic features. Early-onset cases or those with more severe electrophysiologic abnormalities may have greater disability, whereas late-onset or milder NCV reductions are associated with less severe morbidity.[16] Lys558 mutations associated with neutropenia may predict higher infection risk and more complicated course.[15][16] However, quantitative prognostic models have not been developed for CMTDIB.

### 11.4 Prognostic Biomarkers

No validated prognostic biomarkers specific to CMTDIB exist. Electrophysiologic measures such as NCV and CMAP amplitudes provide some prognostic information; more severe reduction correlates with more advanced neuropathy and greater disability.[16] The presence of neutropenia on hematologic testing signals increased risk of infection and may represent a prognostic biomarker for systemic complications in Lys558-mutant families.[15][16] Genetic mutation type itself serves as a prognostic indicator, as certain variants (e.g., PH domain vs PRD mutations) may have different severity profiles, though detailed genotype–prognosis correlations are still emerging.[15][16][12][13]

Future biomarkers might include neurofilament levels, imaging markers of nerve integrity, or omics-based signatures of endocytic dysfunction, but these are not yet established for CMTDIB. 

## 12. Treatment

### 12.1 Pharmacotherapy and Symptomatic Management

Currently, there is no disease-modifying pharmacological treatment specifically approved for CMTDIB or for CMT in general. Cleveland Clinic notes that "there’s no way to cure CMT or treat the condition directly. But therapies and medicines can help manage your symptoms."[10] Symptomatic pharmacotherapy focuses on neuropathic pain management, muscle cramps, and in some cases depression or anxiety. Commonly used drugs include gabapentin, pregabalin, duloxetine, tricyclic antidepressants, and topical agents, although these are not specific to DNM2-related disease.[6][10]

For neutropenia-associated variants, hematologic management may involve granulocyte colony-stimulating factor (G-CSF) or prophylactic antibiotics, though specific guidelines for DNM2-related neutropenia have not been published. Cataracts are treated surgically when they significantly impair vision. NCIT terms relevant to such interventions include "analgesic" (NCIT:C444), "anticonvulsant" (used for neuropathic pain, NCIT:C288), and "cataract extraction" (NCIT:C41097).

Pharmacogenomics has not yet been applied to CMTDIB; no evidence suggests that DNM2 mutations affect drug metabolism, efficacy, or toxicity beyond general neuropathy considerations. However, caution is advised with neurotoxic agents like vincristine, as they can cause severe exacerbation of neuropathy in CMT patients.[6]

### 12.2 Advanced Therapeutics: Gene and RNA-Based Strategies

Advanced therapeutics for DNM2-related disease are in preclinical or early clinical stages, primarily in the context of centronuclear myopathy. RNA-based therapies such as antisense oligonucleotides (ASOs) or gene editing approaches targeting DNM2 have been proposed for CNM, aiming to reduce overactive DNM2 expression or correct gain-of-function mutations.[13][14] For CMTDIB, where DNM2 mutations are loss-of-function, strategies would need to restore or enhance dynamin 2 activity, potentially through gene replacement or small molecules that increase function.

The Nature Communications 2025 study demonstrates that combining CNM-causing and CMT-causing DNM2 mutations in mouse models can rescue phenotypes, suggesting that fine-tuning dynamin 2 activity to an optimal level could be therapeutic.[13] This conceptual framework opens the possibility of pharmacologic or genetic interventions that modulate DNM2 function bidirectionally depending on disease phenotype. However, no human clinical trials of gene therapy or RNA-based therapy for CMTDIB are reported in the available sources.

### 12.3 Surgical and Interventional Treatments

Surgical interventions in CMTDIB are primarily orthopedic. Foot surgery to correct pes cavus, hammer toes, or equinovarus deformities can improve gait, reduce pain, and prevent skin breakdown.[6][8][10] Tendon transfers, osteotomies, and arthrodesis may be performed depending on deformity severity. NCIT terms such as "orthopedic surgical procedure" (NCIT:C15220) and "tendon transfer" (NCIT:C38680) apply to these interventions.

Cataract surgery is standard for DNM2-mutant patients with significant lens opacity. Neutropenia management may involve bone marrow biopsy and hematologic interventions, though not surgical per se.

### 12.4 Supportive and Rehabilitative Care

Supportive care is the cornerstone of CMTDIB management. Cleveland Clinic lists physical and occupational therapy, braces, walkers, wheelchairs, special footwear, surgery for skeletal deformities, and medications for chronic pain as common treatments for CMT.[10] GeneReviews similarly emphasizes multidisciplinary management, including rehabilitation, orthotics, assistive devices, and psychosocial support.[6]

Physical therapy focuses on strengthening unaffected muscles, maintaining flexibility, and improving balance. Occupational therapy addresses hand weakness and fine motor deficits, teaching compensatory strategies and recommending adaptive equipment. Orthotic devices such as ankle–foot orthoses (AFOs) stabilize ankle joints, improve gait, and reduce falls. NCIT terms relevant here include "physical therapy" (NCIT:C15220, when used broadly), "orthotic device" (NCIT:C50198), and "rehabilitation therapy" (NCIT:C68622).

Psychological support is important to manage the emotional impact of living with a progressive disease. Cleveland Clinic explicitly mentions that "having a condition that gets worse over time can take a toll on your mental health," recommending mental health interventions when needed.[10] 

### 12.5 Experimental Treatments and Clinical Trials

No active clinical trials specifically targeting DNM2-related CMTDIB are mentioned in the available search results. However, preclinical work in DNM2-related CNM suggests that dynamin-modulating therapies could be developed.[13][14] Small molecules enhancing or inhibiting dynamin GTPase activity, ASOs correcting aberrant splicing, or CRISPR-based gene editing may eventually be explored for DNM2-related neuropathy.

Functional genomics screens in cell lines and animal models could identify modifiers or interacting pathways that are druggable. For example, enhancing alternative endocytic pathways or supporting myelin maintenance through other mechanisms might mitigate the consequences of DNM2 loss-of-function. DepMap and other functional genomics resources have not yet been used specifically for CMTDIB in the sources provided, but these approaches represent future research directions.

### 12.6 Treatment Outcomes, Algorithms, and Personalized Approaches

Treatment outcomes in CMTDIB depend on timely initiation of supportive care and management of complications. Patients who receive early orthotic support and physical therapy tend to maintain ambulation longer and have fewer falls.[6][10][16] Surgical correction of foot deformities can improve quality of life but carries risks and must be carefully timed. Pain management improves comfort but may not affect disease progression.

Formal treatment algorithms for CMTDIB have not been established, but general CMT pathways involve initial diagnosis and genetic confirmation, followed by assessment of functional status, initiation of rehabilitation and orthotics, monitoring for complications, and periodic reassessment.[6][10] Personalized approaches may include genotype-specific counseling: for example, families with Lys558 mutations should be monitored for neutropenia and infections, while those with cataract-associated mutations should receive regular ophthalmologic evaluations.[15][16]

NCIT clinical intervention terms can be mapped to these treatments, providing a structured vocabulary for clinical pathways. Personalized medicine in CMTDIB remains largely at the level of genetic counseling and complications management rather than targeted molecular therapy.

## 13. Prevention

### 13.1 Primary, Secondary, and Tertiary Prevention

Primary prevention of CMTDIB involves preventing the occurrence of disease in offspring of carriers. As the disease is autosomal dominant, genetic counseling is essential for affected individuals and at-risk relatives.[6] Options include preimplantation genetic diagnosis (PGD), prenatal testing, and informed family planning. ACMG guidelines and GeneReviews emphasize discussing these options and providing psychosocial support.[6]

Secondary prevention focuses on early detection and intervention to reduce morbidity. In families with known DNM2 mutations, early neurological evaluation of at-risk children can identify signs of neuropathy and foot deformities, enabling early orthotic support and physical therapy to minimize progression and optimize function.[6][10][16] Screening for neutropenia and cataracts in Lys558-mutant families constitutes secondary prevention of systemic complications.[15][16]

Tertiary prevention aims to prevent complications and reduce disability in individuals with established CMTDIB. Measures include fall prevention strategies, infection prophylaxis in neutropenic patients, timely orthopedic surgery, and comprehensive rehabilitation.[6][10][15][16] These interventions can significantly improve quality of life even though they do not reverse neuropathy.

### 13.2 Screening and Early Detection Programs

No population-wide screening programs exist for CMTDIB, given its rarity and lack of disease-modifying therapies. Instead, targeted screening in families with known DNM2 mutations is recommended. Genetic testing of at-risk relatives allows early diagnosis and counseling.[6] Newborn screening is not performed for CMT. However, as genomic sequencing becomes more common, incidental detection of DNM2 variants may occur, requiring careful interpretation and counseling.

Risk stratification within affected families is mainly based on genetic status and phenotype severity. EEG or imaging-based screening is not relevant. Clinical guidelines emphasize neurologic and orthopedic surveillance rather than formal screening programs.[6][10]

### 13.3 Behavioral and Environmental Interventions

Behavioral interventions to reduce risk of complications include maintaining physical activity within safe limits, avoiding high-risk activities that could cause falls or injuries, and adhering to orthotic and therapy regimens.[6][10] For neutropenic patients, infection prevention measures such as hand hygiene, avoiding crowded places during outbreaks, and prompt treatment of infections are important.

Public health interventions are not directly applicable to CMTDIB given its hereditary nature and low prevalence. Environmental interventions such as reducing exposure to neurotoxins may be recommended for individuals with hereditary neuropathy generally but do not constitute population-level measures.[6][10]

### 13.4 Genetic Counseling

Genetic counseling is a critical preventive strategy in CMTDIB. GeneReviews outlines counseling for autosomal dominant CMT, advising discussion of inheritance pattern, recurrence risk, options for prenatal diagnosis and PGD, and implications for family members.[6] Counselors should address psychosocial aspects, such as guilt, fear, and decision-making about reproduction. NSGC and ACMG guidelines support these practices.

Counseling also includes education about disease course, treatment options, and lifestyle modifications. For families with specific DNM2 mutations, counsel must address systemic manifestations such as neutropenia and cataracts.[15][16] 

## 14. Other Species and Natural Disease

### 14.1 Species and Orthologous Genes

DNM2 orthologs exist in many species, including mice, rats, zebrafish, and invertebrates. NCBI Gene catalogs Dnm2 for mouse (Gene ID: 13430) and other organisms. These orthologs share domain architecture and function in CME, enabling comparative studies of dynamin 2 function and mutation effects.

Natural disease resembling CMTDIB has not been reported in companion animals or livestock. OMIA and veterinary literature do not list dynamin 2–associated hereditary neuropathies in domestic species in the available search results. Veterinary relevance is therefore limited to experimental models rather than clinical cases.

### 14.2 Comparative Pathology and Evolutionary Conservation

Comparative pathology using Dnm2-mutant mice demonstrates that dynamin 2 is essential for myelination in peripheral nerves and for skeletal muscle function in CNM models.[4][13][14] This conservation of function across species supports the use of mouse models for studying CMTDIB mechanisms. Evolutionary conservation of dynamin 2 domains and interactions implies that human mutations will generate similar cellular phenotypes in model organisms.

Cross-species susceptibility to DNM2 mutations is likely present in mammals, but natural hereditary neuropathy due to Dnm2 mutations has not been documented outside experimental models. Zoonotic potential is not applicable, as CMTDIB is a non-infectious genetic disorder.

## 15. Model Organisms

### 15.1 Mouse Models of DNM2-Related Neuropathy

The most informative model organisms for CMTDIB are Dnm2-deficient or Dnm2-mutant mice. Sidiropoulos et al. used tissue from Dnm2-deficient mice as a peripheral nerve model to study disease mechanisms.[4] They expressed human DNM2 mutants associated with DI-CMTB in Schwann cells and neurons and compared their effects to CNM-associated mutants.[4] The mouse model recapitulated key features: impaired myelination, defects in CME, and altered surface protein levels in Schwann cells.[4] These findings validate the causal relationship between DNM2 mutations, CME disruption, and myelination defects and provide a platform for testing therapeutic interventions.

The Nature Communications 2025 study also used mouse models to examine the effects of combining CNM and CMT mutations in Dnm2, demonstrating that opposing functional mutations could rescue phenotypes.[13] This sophisticated genetic model illustrates how dynamin 2 activity level determines neuromuscular outcomes and supports the idea that modulating DNM2 function could be therapeutic.

### 15.2 Model Characteristics, Limitations, and Applications

Mouse models recapitulate many human CMTDIB features, including myelination defects, reduced NCV, and peripheral nerve pathology, making them valuable for mechanistic studies.[4][13] However, differences in nerve length, gait, and lifespan limit the direct translation of some functional outcomes. Mice may not fully reproduce distal symmetric polyneuropathy over long distances as in humans, and behavioral manifestations differ.

These models are used to study disease pathways, test genetic rescue strategies, and evaluate potential drugs that modulate endocytosis or myelination. Dnm2-deficient mice and transgenic models expressing human DNM2 mutants can be used in functional genomics screens to identify modifiers and interacting proteins.[4][13] However, specific therapeutic interventions tested in these models have not yet progressed to human trials.

Other model systems, such as zebrafish or Drosophila with altered dynamin function, could be used to study axon guidance and synaptic vesicle recycling but are less relevant for myelination, which is a mammalian-specific process. Cell culture models using Schwann cell lines or iPSC-derived Schwann cells expressing DNM2 mutants provide in vitro systems for studying CME and myelin membrane dynamics.[4] These in vitro models complement in vivo mouse data.

### 15.3 Resources and Future Directions

Model organism databases such as MGI catalog Dnm2 mouse lines. Research applications include dissecting the roles of different DNM2 domains in nerve and muscle, exploring domain-specific rescue strategies, and testing pharmacologic agents that modulate dynamin activity.[4][13][14] Limitations include the artificial nature of some models and the difficulty of modeling nuanced human phenotypes like pain or subtle sensory deficits.

Future directions involve creating humanized mouse models expressing patient-specific DNM2 mutations, using CRISPR to edit DNM2 in vivo, and applying single-cell RNA-seq and spatial transcriptomics to peripheral nerve tissues in these models. Integrating multi-omics data from models and human biopsies will deepen understanding of CMTDIB mechanisms and guide targeted therapies.

## Conclusion

Charcot-Marie-Tooth disease dominant intermediate B is a rare, autosomal dominant hereditary motor and sensory neuropathy caused by heterozygous DNM2 loss-of-function mutations, primarily affecting clathrin-mediated endocytosis and myelination in Schwann cells and peripheral neurons.[1][4][13][15][16] Clinically, it presents with a classical CMT phenotype—distal weakness and atrophy, sensory loss, areflexia, foot deformities—with intermediate nerve conduction velocities bridging demyelinating and axonal categories.[6][16] The disease typically begins in childhood or adolescence, progresses slowly, and produces mild to moderate disability, with most patients remaining ambulatory and life expectancy near normal.[10][15][16] Specific DNM2 variants, particularly those affecting Lys558 in the PH domain, can add systemic manifestations such as neutropenia and early cataracts, expanding the phenotypic spectrum and underscoring the gene’s multi-system roles.[1][15][16]

Mechanistic studies using Dnm2-deficient mice and in vitro models demonstrate that DI-CMTB-associated DNM2 mutants impair myelination and clathrin-mediated endocytosis in Schwann cells and neurons, alter surface protein levels, and thereby disrupt axon–glia communication and myelin maintenance.[4] These data support a causal chain from DNM2 mutation to CME dysfunction to myelination defects and ultimately to mixed demyelinating–axonal neuropathy, with loss-of-function dynamics distinguishing CMT mutations from gain-of-function CNM mutations.[4][13][14] The phenotypic rescue observed in mice carrying both CNM and CMT mutations suggests that dynamin 2 activity can be tuned and that future therapies might aim to restore normal activity levels.[13]

Diagnosis of CMTDIB relies on integrating clinical, electrophysiologic, and genetic data. Intermediate NCV and sural nerve biopsy findings of loss of large myelinated fibers and remyelination clusters point to intermediate CMT, while identification of a heterozygous pathogenic DNM2 variant confirms DI-CMTB.[1][6][16][18][12] Differential diagnosis includes other hereditary CMT subtypes and acquired neuropathies, which are distinguishable by electrophysiology, histology, and genetic testing.[6][8][16][19] Treatment is currently supportive, focusing on physical and occupational therapy, orthotic devices, orthopedic surgery for foot deformities, symptomatic pharmacotherapy, and management of systemic complications such as neutropenia and cataracts.[6][10][15][16] Genetic counseling is vital for family planning and early care; cascade testing in affected families allows early diagnosis and intervention.[6]

Research gaps remain substantial. There is limited epidemiologic data on prevalence and incidence of CMTDIB, few longitudinal studies detailing natural history and quality of life, and no disease-modifying therapies in clinical use. Mechanistic studies have illuminated CME and myelination pathways, but more work is needed to map downstream signaling, metabolic changes, and potential modifiers. Omics-based profiling of human nerve tissues and advanced model organism studies will be important for identifying therapeutic targets. The emerging understanding that DNM2-CMT mutations are loss-of-function, while DNM2-CNM mutations are gain-of-function, provides a conceptual framework for precision therapies that adjust dynamin 2 activity and underscores the broader significance of CMTDIB as a window into fundamental membrane dynamics in health and disease.[4][13][14]

This comprehensive characterization of CMTDIB—encompassing genetic, clinical, pathophysiologic, and translational dimensions—provides a robust foundation for structured disease knowledge bases. By mapping phenotypes to HPO, biological processes to GO, cell types to CL, anatomical structures to UBERON, and interventions to NCIT, and by distinguishing evidence from human clinical cohorts, mouse models, and in vitro studies, it supports nuanced data integration and highlights critical areas for future research and therapeutic development.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.