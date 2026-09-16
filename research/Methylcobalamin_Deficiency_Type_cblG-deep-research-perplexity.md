---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-08-28T10:55:08.409818'
end_time: '2026-08-28T10:59:39.156314'
duration_seconds: 270.75
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Methylcobalamin Deficiency Type cblG
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
citation_count: 17
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 4
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Methylcobalamin Deficiency Type cblG
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Methylcobalamin Deficiency Type cblG** covering all of the
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

# Methylcobalamin Deficiency Type cblG: Comprehensive Disease Characteristics

Methylcobalamin deficiency type cblG, also known as methionine synthase deficiency, is a rare autosomal recessive inborn error of cobalamin-dependent one-carbon metabolism characterized biochemically by severe hyperhomocysteinemia, homocystinuria, and hypomethioninemia, and clinically by a spectrum of neurodevelopmental, neurologic, and hematologic manifestations ranging from infantile encephalopathy and megaloblastic anemia to adult-onset leukoencephalopathy and psychiatric symptoms.[2][4][7][11][14] At the molecular level, the disorder is caused by biallelic pathogenic variants in the MTR gene on chromosome 1q43, encoding the cobalamin-dependent enzyme methionine synthase, which catalyzes the remethylation of homocysteine to methionine using 5‑methyltetrahydrofolate as methyl donor and methylcobalamin as an essential prosthetic cofactor.[2][6][16] Historically, cellular complementation studies in fibroblasts defined two distinct vitamin B\(_{12}\)-responsive megaloblastic anemia and homocystinuria groups, cblE and cblG, reflecting defects at separate loci in the methylcobalamin-dependent remethylation pathway; subsequent molecular cloning identified MTR as the cblG gene and MTRR (methionine synthase reductase) as the cblE gene, establishing a framework for understanding methionine synthase–related disorders.[1][2][5][6][7] Although fewer than forty individuals with cblG have been described in the literature, accumulating case series and recent reviews show marked phenotypic variability and demonstrate that early diagnosis and institution of high-dose parenteral hydroxocobalamin, betaine, folate/folinic acid, and, in some cases, methionine supplementation can normalize metabolic derangements and substantially improve neurologic and hematologic outcomes, particularly when treatment precedes irreversible brain injury.[7][9][11][14] This report synthesizes current knowledge on cblG across domains including etiology, clinical phenotype, molecular pathophysiology, diagnostics, treatment, prognosis, and epidemiology, and situates the disorder within broader cobalamin metabolism, homocysteine remethylation, and one-carbon biology, providing ontology-linked annotations suitable for computational disease knowledge bases.

## 1. Disease Information

### 1.1 Definition and Clinical Overview

Methylcobalamin deficiency type cblG is defined as a functional deficiency of cobalamin-dependent methionine synthase caused by pathogenic variants in the MTR gene, leading to impaired remethylation of homocysteine to methionine and consequent disturbance of the folate- and cobalamin-dependent one-carbon cycle.[2][6][7][11][16] The biochemical signature of this disorder comprises markedly elevated plasma total homocysteine, homocystinuria, low plasma methionine, and usually normal methylmalonic acid, distinguishing it from other combined remethylation and methylmalonic aciduria defects such as cblC.[2][7][9][11] GeneReviews describes cblG as one of the “disorders of intracellular cobalamin metabolism” associated with selective methylcobalamin deficiency, in contrast to disorders like cblC that affect the synthesis of both methylcobalamin and adenosylcobalamin.[7][9] Clinically, affected individuals may present in infancy with feeding difficulties, failure to thrive, hypotonia, seizures, encephalopathy, microcephaly, and megaloblastic anemia, or in adolescence or adulthood with neuropsychiatric symptoms, gait disturbance, cognitive decline, or acute leukoencephalopathy, reflecting the central role of methionine and methylation reactions in nervous system function.[4][7][11][14] The condition is responsive to pharmacologic doses of vitamin B\(_{12}\), particularly hydroxocobalamin, and adjunctive therapies that bypass the defective methionine synthase pathway, and thus occupies a unique position among inborn errors of metabolism as a potentially treatable cause of severe neurologic disease and thrombotic risk related to hyperhomocysteinemia.[2][7][9][11][14]

### 1.2 Historical Development and Complementation Classification

The concept of cblG emerged from biochemical and cellular studies of patients with vitamin B\(_{12}\)-responsive megaloblastic anemia and homocystinuria in the 1980s, which recognized that some individuals had low intracellular methylcobalamin synthesis and defective methionine biosynthesis despite normal adenosylcobalamin-dependent methylmalonyl-CoA mutase function.[1][5] Rosenblatt and Watkins performed complementation analysis of cultured fibroblasts from patients with megaloblastic anemia and homocystinuria and identified at least two distinct complementation classes, cblE and cblG, both characterized by defective methionine synthase activity but presumed to reflect mutations at separate loci required for cobalamin-dependent methionine biosynthesis.[1][5] In their classic report, they wrote: 

> “Vitamin B12–responsive megaloblastic anemia and homocystinuria: description of two complementation classes, cblE and cblG.”[5]

and proposed the designation cblG for patients with methylcobalamin deficiency and decreased synthase activity, distinguishing them from cblE individuals in whom methionine synthase activity measured in vitro appeared normal but was subject to defective reductive activation.[1][5] Subsequent molecular cloning of the MTR gene in the mid-1990s and identification of mutations in MTR in cblG patients established that cblG is a primary methionine synthase deficiency, whereas cblE is caused by mutations in MTRR, encoding methionine synthase reductase, a flavoprotein that maintains methionine synthase in its active, reduced state.[2][6][7] These developments provided a mechanistic basis for the complementation classes and allowed genotype–phenotype correlations and more precise diagnostic strategies based on sequencing of MTR and MTRR rather than labor-intensive fibroblast complementation assays.[2][6][7][11]

### 1.3 Key Identifiers and Ontology Mapping

Methylcobalamin deficiency type cblG is recognized across multiple curated biomedical databases and disease ontologies. OMIM describes “homocystinuria and megaloblastic anemia due to defect in cobalamin metabolism, cblG complementation type” as an autosomal recessive disorder resulting from defects in intracellular cobalamin metabolism, specifically affecting methionine synthase, with the phenotype encompassing homocystinuria, hyperhomocysteinemia, hypomethioninemia, and megaloblastic anemia.[3][4][7] Orphanet and NORD (National Organization for Rare Disorders) categorize “methylcobalamin deficiency cblG type” as a rare inherited metabolic disease of amino acid metabolism and one-carbon pathway, often manifesting in the first year of life but with a broad age-of-onset range extending into adulthood.[4] MedGen (NCBI) includes a concept entry for “Methylcobalamin deficiency type cblG” linking to human phenotype ontology terms such as megaloblastic anemia, homocystinuria, microcephaly, hypotonia, seizures, severe global developmental delay, and hypomethioninemia.[3][13][15] The NCBI Gene entry for MTR lists “cblG” and “HMAG” among the gene’s aliases, reflecting the disease association and the historical name “homocystinuria-megaloblastic anemia G.”[16] Within the Mondo Disease Ontology, methylcobalamin deficiency type cblG is represented under a label corresponding to the Orphanet and NORD naming conventions; however, the precise numeric identifier is not explicitly visible in the available search result snippet, and thus cannot be definitively confirmed from these data alone.[4] Suggested ontology mappings include a MONDO term for “methylcobalamin deficiency type cblG”, HPO terms such as HP:0001899 (megaloblastic anemia), HP:0001997 (homocystinuria), HP:0002153 (hyperhomocysteinemia), HP:0003262 (hypomethioninemia), HP:0001250 (seizures), HP:0001290 (developmental delay), HP:0001249 (intellectual disability), HP:0001252 (hypotonia), and HP:0000252 (microcephaly), as well as NCIT terms for “Inherited Metabolic Disease”, “Vitamin B12 Deficiency Disorder”, and “Methionine Synthase Deficiency”.

### 1.4 Synonyms and Alternative Names

Multiple synonymous and closely related names have been used for methylcobalamin deficiency type cblG in the literature and databases, reflecting its biochemical basis and historical clinical descriptions. NORD lists synonyms including “HMAG”, “cblG”, “functional methionine synthase deficiency type cblG”, “homocystinuria due to defect in methylation cblG”, “homocystinuria-megaloblastic anemia due to defect in cobalamin metabolism, cblG complementation type”, and “methylcobalamin deficiency cblG type”.[4] MedGen similarly cross-links to terms such as “methionine synthase deficiency”, “homocystinuria and megaloblastic anemia due to cobalamin metabolism defect cblG type”, and “methylmalonic aciduria and homocystinuria type cblG”, although in classical cblG methylmalonic acid levels are typically normal, and the latter term more appropriately applies to disorders like cblD or cblC.[3][7][9][15] Gene-centric resources like NCBI Gene and HGNC list “cobalamin-dependent methionine synthase”, “vitamin B\(_{12}\)-dependent methionine synthase”, “5‑methyltetrahydrofolate-homocysteine methyltransferase”, and the acronym “MS” as alternative names for the MTR gene product.[16] Historically, early biochemical and clinical reports referred to affected individuals as having “homocystinuria and megaloblastic anemia responsive to vitamin B\(_{12}\)” or “hyperhomocysteinemia due to methionine synthase deficiency”, terminology that remains in common descriptive use alongside the cblG complementation class designation.[1][2][5][11]

### 1.5 Data Sources and Evidence Types

The information synthesized in this report arises primarily from aggregated disease-level resources and peer-reviewed clinical and molecular studies rather than individual patient electronic health records, though the underlying clinical data in these sources ultimately derive from case reports, case series, and cohort analyses. GeneReviews provides a comprehensive narrative review of disorders of intracellular cobalamin metabolism, including cblG, based on collation of published cases, biochemical studies, and expert clinical experience, and thus represents a curated secondary source that integrates multiple primary human clinical and biochemical investigations.[7] NORD and Orphanet offer disease summaries based on literature reviews and expert contributions, emphasizing clinical features, diagnosis, and management at the disease level.[4] MedGen, OMIM, and HPO curation compile phenotype, genetic, and clinical associations from primary literature into structured concept entries with ontology mappings.[3][7][13][15] Primary-data sources include classic cellular complementation studies in fibroblasts, such as Rosenblatt and Watkins’ 1987 description of cblE and cblG, and subsequent molecular characterization of the MTR gene and pathogenic variants in large panels of cblG patients, including Watkins et al. (2002, PMID 12068375) and Gulati et al. (1996), which provide detailed genotype data and evidence for recurrent mutations.[1][2][5][6] More recent clinical series, notably Kripps et al. (2022, PMID 34625984), systematically describe the variable clinical presentation and treatment outcomes in a contemporary cohort of cblG patients, while Neurology case reports and series delineate adult-onset manifestations such as leukoencephalopathy.[11][14] Additionally, biochemical intervention studies in related contexts, such as methylcobalamin supplementation to normalize homocysteine in vitamin B\(_{12}\)-deficient vegetarians, provide mechanistic and therapeutic insight into the remethylation pathway even though they involve nutritional rather than genetic deficiency.[8] This diversity of evidence types—human clinical, in vitro cellular, molecular genetic, and biochemical intervention studies—supports a robust, multi-level characterization of methylcobalamin deficiency type cblG.

## 2. Etiology

### 2.1 Genetic Causal Factors: MTR and Methionine Synthase Deficiency

The primary cause of methylcobalamin deficiency type cblG is biallelic pathogenic variants in the MTR gene, which encodes cytosolic cobalamin-dependent methionine synthase (EC 2.1.1.13) on human chromosome 1q43.[2][6][16] MTR catalyzes the methylation of homocysteine to generate methionine, using 5‑methyltetrahydrofolate as the methyl group donor and requiring the presence of an enzyme-bound methylcobalamin prosthetic group for activity, thereby coupling folate and cobalamin metabolism in the remethylation of homocysteine.[2][6][7][16] The coding region of MTR is highly compact and composed of 33 exons and 32 introns spanning at least 60 kb of genomic DNA, a structure elucidated by Watkins et al. in their 2002 Am J Hum Genet article, which defined exon–intron boundaries and facilitated mutation analysis in cblG patients.[2][6] They reported that:

> “The coding region of the human methionine synthase gene is composed of 33 exons and 32 introns… It is a highly compressed gene of 33 exons and 32 introns that spans at least 60 kb.”[2][6]

Mutations in MTR cause a functional deficiency of methionine synthase, impairing the enzyme’s ability to accept methyl groups from 5‑methyltetrahydrofolate and transfer them to homocysteine, and thereby leading to accumulation of homocysteine and decreased synthesis of methionine and downstream S‑adenosylmethionine (SAM).[2][6][7][11] Molecular studies have identified a variety of pathogenic variant types in MTR, including missense, nonsense, frameshift, splice-site, and small insertion/deletion mutations distributed across multiple exons, often affecting conserved catalytic or cobalamin-binding domains.[2][6][11][16] An especially notable missense mutation, P1173L, resulting from a C→T transition in a CpG dinucleotide within exon 24, has been found recurrently in unrelated patients and likely represents a mutational hotspot; in the expanded panel of 24 cblG patients studied by Watkins et al., P1173L was detected in 16 individuals, and haplotype analysis indicated that this mutation had arisen independently on at least two separate genetic backgrounds.[2][6] The authors emphasize:

> “A previously described missense mutation, P1173L, was detected in 16 patients in an expanded panel of 24 patients with cblG. Analysis of haplotypes… demonstrated that this mutation, a C→T transition in a CpG island, has occurred on at least two separate genetic backgrounds.”[2][6]

This finding underscores both the existence of common recurrent pathogenic variants and the role of spontaneous mutagenesis at CpG sites in generating disease alleles.

### 2.2 Genetic Risk and Inheritance: Autosomal Recessive Pattern

Methylcobalamin deficiency type cblG is inherited in an autosomal recessive manner, as confirmed by GeneReviews and multiple case series.[2][4][7][11][16] GeneReviews states that the majority of disorders of intracellular cobalamin metabolism, including cblG, result from biallelic pathogenic variants in genes such as MTR and follow autosomal recessive inheritance.[7] For autosomal recessive disorders, each child of carrier parents has a 25% chance of being affected, a 50% chance of being an asymptomatic carrier, and a 25% chance of being neither affected nor a carrier.[7] MTR is expressed ubiquitously, with gene expression detected in kidney, thyroid, and at least twenty-five other tissues, consistent with the systemic metabolic role of methionine synthase.[16] In cblG, only individuals harboring pathogenic variants on both alleles—either homozygous for a pathogenic variant or compound heterozygous for two different pathogenic variants—develop the disease phenotype, whereas heterozygous carriers are typically asymptomatic, although they may have subtle biochemical changes under certain metabolic stresses.[2][6][7][11][16] The penetrance of cblG appears to be high in individuals with biallelic loss-of-function variants, given the severe impairment of enzyme activity; however, expressivity is markedly variable, with some patients presenting in infancy and others not becoming symptomatic until adulthood, suggesting that genetic, epigenetic, and environmental modifiers influence clinical manifestation.[7][11][14] Consanguinity has been reported in some families, reflecting the role of autosomal recessive inheritance and the increased likelihood of homozygosity for rare pathogenic alleles in consanguineous populations, though systematic epidemiologic data on this aspect are limited.[7][11] Founder effects have not been clearly delineated for cblG in the literature reviewed, but the high frequency of P1173L among studied patients raises the possibility that this mutation may be enriched in certain populations or regions, a hypothesis that requires larger, geographically diverse cohorts for confirmation.[2][6]

### 2.3 Environmental and Nutritional Factors

Because cblG is a monogenic inborn error of metabolism, environmental factors do not cause the disease but can modulate its clinical expression and severity. Nutritional status, particularly dietary intake and absorption of vitamin B\(_{12}\) (cobalamin) and folate, influences the availability of methylcobalamin and 5‑methyltetrahydrofolate, respectively, which serve as substrates and cofactors for methionine synthase.[7][8][9][11] In individuals with partial residual methionine synthase activity due to hypomorphic MTR variants, adequate or supraphysiologic cobalamin and folate supply may sustain some remethylation flux and delay or ameliorate symptom onset, whereas concomitant dietary B\(_{12}\) deficiency—for example, in strict vegetarians or in conditions such as pernicious anemia—could exacerbate hyperhomocysteinemia and neurological vulnerability.[7][8][11] Obersby et al. conducted a randomized double-blind placebo-controlled pilot study in vitamin B\(_{12}\)-deficient vegetarians and showed that oral methylcobalamin supplementation significantly reduced mean baseline plasma total homocysteine from 15.5 µmol/L to 8.4 µmol/L, effectively normalizing levels in many participants.[8] They concluded:

> “The statistical results… demonstrate that methylcobalamin reduced mean baseline plasma tHcy level of 15.5 µmol L\(^{-1}\)… to a post-treatment plasma tHcy level of 8.4 µmol L\(^{-1}\)… The very positive effect of methylcobalamin on lowering plasma tHcy leads to the conclusion that methylcobalamin can… be recommended as a food supplement for all categories of vegetarianism.”[8]

This study illustrates the sensitivity of homocysteine levels to cobalamin supply in nutritional deficiency, and by analogy suggests that pharmacologic doses of cobalamin can partially correct hyperhomocysteinemia in cblG by maximizing residual methionine synthase activity or promoting alternative remethylation pathways. Other environmental factors, such as exposure to nitrous oxide (N\(_2\)O), which oxidizes the cobalt center of cobalamin and irreversibly inactivates methionine synthase, could theoretically precipitate acute neurologic decompensation in individuals with underlying MTR deficiency, as seen in acquired N\(_2\)O-induced myelopathy, although specific cases of N\(_2\)O-triggered crises in cblG have not been widely reported.[7][11] Age and sex do not appear to be strong determinants of risk for cblG itself, although they influence the timing and manifestations of symptom onset; both males and females are affected, and presentations span the life course from infancy to adulthood.[4][7][11][14]

### 2.4 Protective Factors and Modifiers

Protective factors in cblG primarily relate to early diagnosis, prompt initiation of appropriate metabolic treatment, and maintenance of optimal nutritional status for one-carbon metabolism. Kripps et al. (2022) examined clinical presentation and treatment outcomes in a cohort of cblG patients and found that those treated early in life, especially before neurologic symptoms manifested, had more favorable outcomes than those whose diagnosis and therapy were delayed.[11] They emphasize:

> “We demonstrate more favorable outcomes in our patients who were treated early in life, especially those who were treated before neurologic symptoms manifested. Given improved outcomes from treatment of presymptomatic patients, cblG warrants inclusion in newborn screening.”[11]

This suggests that early detection through newborn or early childhood screening, followed by aggressive management with hydroxocobalamin, betaine, folinic acid, and methionine supplementation, can protect against severe neurologic damage and developmental delay.[7][11] Adequate intake of folate and possibly other cofactors involved in homocysteine metabolism (such as vitamin B\(_{6}\) and riboflavin) may also confer partial protection by supporting alternative remethylation routes and minimizing accumulation of toxic metabolites, though direct evidence for such protective effects in cblG is sparse.[7][11] Genetic modifiers, such as polymorphisms in folate pathway genes (e.g., MTHFR) or in genes encoding other enzymes of homocysteine metabolism, could theoretically influence disease severity by altering flux through parallel pathways, but specific modifier alleles have not been systematically characterized in cblG cohorts.[7][11] The recurrent P1173L mutation appears to be associated with severe biochemical deficiency but variable clinical expression depending on treatment timing and other factors, suggesting that genotype–phenotype interactions are complex and modifiable.[2][6][11] Overall, protective factors in cblG center on early, sustained metabolic intervention and avoidance of additional insults to cobalamin-dependent pathways.

### 2.5 Gene–Environment Interactions

Gene–environment interactions in methylcobalamin deficiency type cblG primarily involve the interplay between genetic impairment of methionine synthase and environmental influences on cobalamin and folate status, as well as other metabolic stresses. Individuals with biallelic MTR mutations have reduced methionine synthase activity, and their capacity to respond to environmental variations in cobalamin and folate availability is constrained, but not entirely absent if residual enzyme function remains.[2][6][7][11][16] In such individuals, high-dose parenteral cobalamin can partially overcome the catalytic deficit by saturating the enzyme with cofactor, improving methylcobalamin holoenzyme formation, and supporting both methionine synthase and betaine-homocysteine methyltransferase-mediated remethylation pathways, illustrating a classic example of gene–environment interaction in treatment.[2][7][9][11] Conversely, environmental factors that further reduce cobalamin availability (e.g., malabsorption, nutritional deficiency, N\(_2\)O exposure) may exacerbate the biochemical and clinical manifestations of cblG by diminishing the already compromised remethylation capacity.[7][8][11] GeneReviews notes that newborn screening programs relying solely on elevated C3 or C3/C2 ratios often fail to detect pure remethylation defects such as cblG, which do not exhibit elevated propionylcarnitine, highlighting a gene–environment diagnostic interaction whereby screening algorithms tuned to certain metabolic signals may miss conditions that require different biomarkers, such as low methionine.[7] Chace et al., Weisfeld-Adams et al., and Huemer et al. have shown that detection of low methionine in newborn screening can reveal remethylation disorders, but cblG and cblE are often not identified because their biochemical signatures may not cross conventional cutoffs, underscoring the need to adjust environmental (programmatic) parameters to the specific genetic disease profile.[7] Thus, cblG exemplifies gene–environment interplay in both pathophysiologic expression and public health detection.

## 3. Phenotypes

### 3.1 Core Biochemical Phenotype

The defining biochemical phenotype of methylcobalamin deficiency type cblG consists of hyperhomocysteinemia, homocystinuria, and hypomethioninemia, with normal or only mildly elevated methylmalonic acid concentrations.[2][3][7][11][15] Hyperhomocysteinemia refers to markedly elevated plasma total homocysteine, often exceeding 100 µmol/L in untreated patients, reflecting the block in remethylation from homocysteine to methionine at the level of methionine synthase.[2][7][11] Homocystinuria denotes increased urinary excretion of homocysteine and its disulfides, which is a direct consequence of sustained hyperhomocysteinemia.[2][3][7] Hypomethioninemia, defined as low plasma methionine, arises because the defective MTR enzyme cannot efficiently produce methionine from homocysteine and 5‑methyltetrahydrofolate, leading to diminished methionine and, downstream, reduced S‑adenosylmethionine, the universal methyl donor for numerous methylation reactions.[2][7][11][15] MedGen lists hypomethioninemia as a characteristic laboratory abnormality in cblG and related remethylation disorders, emphasizing its diagnostic value alongside homocystinuria.[15] GeneReviews’ table of biochemical diagnostic markers for disorders of intracellular cobalamin metabolism highlights that MeCbl deficiency cblG is characterized by normal methylmalonic acid, normal C3 acylcarnitine, increased homocysteine, and low methionine, distinguishing it from disorders like cblC that show elevated methylmalonic acid and C3.[7] The biochemical phenotype is typically severe in untreated individuals but can be substantially improved by therapy; Kripps et al. and others have documented significant reductions in homocysteine and increases in methionine following treatment with hydroxocobalamin, betaine, and folinic acid.[9][11][14] Suggested HPO term mappings for this biochemical profile include HP:0002153 (hyperhomocysteinemia), HP:0001997 (homocystinuria), HP:0003262 (hypomethioninemia), and HP:0031773 (abnormal methylmalonic acid concentration—usually normal in cblG).

### 3.2 Hematologic Phenotype: Megaloblastic Anemia

Megaloblastic anemia is a frequent and often early manifestation of cblG, reflecting impaired DNA synthesis due to disruption of folate-dependent one-carbon metabolism.[1][4][7][11] Megaloblastic anemia is characterized by macrocytic red blood cells, hypersegmented neutrophils, and bone marrow findings of nuclear-cytoplasmic asynchrony, and is typically responsive to vitamin B\(_{12}\) supplementation.[4][7] Individuals with cblG commonly present with macrocytic or megaloblastic anemia in infancy, associated with pallor, fatigue, and failure to thrive.[4][7][11] Rosenblatt and Watkins originally described patients with “vitamin B\(_{12}\)-responsive megaloblastic anemia and homocystinuria” in their complementation study, establishing the hematologic component of the cblG phenotype.[1][5] GeneReviews notes that individuals with cblG “characteristically present in the first year of life with neurologic manifestations and megaloblastic anemia,” though hematologic manifestations can also occur later or be overshadowed by neurologic signs.[7] In Kripps et al.’s 2022 series, macrocytic anemia was among the common presenting features, though frequency varied and some adult-onset patients were diagnosed primarily on neurologic grounds.[11] The anemia is reversible with adequate therapy; hydroxocobalamin and folate/folinic acid supplementation restore folate and cobalamin-dependent thymidylate and purine synthesis, enabling normalization of erythropoiesis.[7][11] Suggested HPO terms include HP:0001899 (megaloblastic anemia), HP:0001873 (macrocytic anemia), and HP:0001903 (pallor).

### 3.3 Neurologic and Neurodevelopmental Phenotypes

Neurologic and neurodevelopmental manifestations constitute the most clinically significant phenotype of cblG, reflecting the critical dependence of the central nervous system on methylation reactions and methionine metabolism.[4][7][11][14] In infants and young children, cblG often presents with encephalopathy, developmental delay, hypotonia, seizures, and microcephaly.[4][7][11] NORD summarizes that common features include feeding difficulties, lethargy, seizures, poor muscle tone (hypotonia), developmental delay, and microcephaly, and notes that signs and symptoms typically develop during the first year of life but can range from infancy to adulthood.[4] GeneReviews similarly emphasizes neurologic manifestations in the first year, including weakness, hypotonia, seizures, and mental status changes.[7] Severe global developmental delay is listed as a MedGen concept linked to cblG, underscoring the profound impact on cognitive and motor development when the disorder is untreated or inadequately treated in early childhood.[13] Adult-onset neurologic phenotypes have also been described; a Neurology case series reports methionine synthase deficiency as a rare cause of adult-onset leukoencephalopathy, with clinical onset characterized by cognitive decline, gait disturbance, and white matter abnormalities on MRI.[14] Treatment with intramuscular hydroxocobalamin in these adult patients resulted in normalization of biochemical abnormalities within one year and clinical improvement after three months, highlighting both the reversibility of some neurologic deficits and the importance of recognizing cblG in the differential diagnosis of leukoencephalopathy.[14] Kripps et al. report that clinical presentation in cblG is highly variable, “ranging from seizures, encephalopathy, macrocytic anemia, hypotonia, and feeding difficulties in the neonatal period to onset of psychiatric symptoms or acute neurologic changes in adolescence or adulthood,” reflecting the spectrum of neurologic phenotypes that can arise from methionine synthase deficiency.[11] Suggested HPO terms include HP:0001250 (seizures), HP:0001290 (developmental delay), HP:0001249 (intellectual disability), HP:0001252 (hypotonia), HP:0000252 (microcephaly), HP:0001288 (gait disturbance), HP:0001298 (leukoencephalopathy), and HP:0002315 (encephalopathy). The impact on quality of life is substantial; severely affected children may be unable to attain independent ambulation or communication, and adult patients with leukoencephalopathy can experience significant disability in daily functioning, though formal quality-of-life measurements such as EQ‑5D or SF‑36 have not been systematically reported for cblG.

### 3.4 Psychiatric and Behavioral Phenotypes

Beyond overt neurologic deficits, cblG can manifest with psychiatric and behavioral abnormalities, particularly in adolescent and adult-onset cases. Kripps et al. note that in some individuals, initial manifestations include psychiatric symptoms, such as mood disturbances, psychosis, or behavioral changes, prior to more obvious neurologic signs.[11] Adult patients described in Neurology and other reports have presented with cognitive decline, personality changes, and behavioral disturbances, prompting evaluation for neurodegenerative or psychiatric disorders before metabolic screening identified hyperhomocysteinemia and cblG.[11][14] These symptoms can be understood within the context of global cerebral hypomethylation and white matter dysfunction resulting from chronic methionine and SAM deficiency, which may affect neurotransmitter systems, synaptic plasticity, and myelin integrity.[7][11][14] Suggested HPO terms include HP:0000717 (psychosis), HP:0000729 (depression), HP:0000739 (personality changes), and HP:0001289 (cognitive impairment). Although detailed behavioral phenotyping using systems such as DSM or RDoC has not been published for cblG, the qualitative descriptions indicate that psychiatric manifestations can significantly impair social functioning and quality of life, often improving when metabolic treatment is instituted.

### 3.5 Growth, Feeding, and Somatic Phenotypes

Infants and young children with cblG often exhibit feeding difficulties, failure to thrive, and poor growth, which may be secondary to neurologic impairment, anorexia from illness, or direct metabolic effects.[4][7][11] NORD notes that common features include feeding difficulties and lethargy, which can contribute to poor weight gain and developmental delay.[4] Hypotonia and weakness may exacerbate feeding problems, making oral intake challenging and necessitating enteral support in some cases.[4][7][11] Microcephaly, reflecting reduced head growth, is a frequent manifestation in severely affected children and correlates with underlying brain hypomyelination and developmental delay.[4][7][13] Some individuals may also exhibit failure to thrive and stunting, though systematic anthropometric data are limited.[7][11] Suggested HPO terms include HP:0001508 (failure to thrive), HP:0001265 (poor feeding), HP:0000252 (microcephaly), and HP:0001510 (growth delay). The impact on quality of life is significant, as caregivers must manage complex feeding regimens and neurologic disability.

### 3.6 Phenotypic Variability, Onset, and Progression

A central feature of cblG is its marked phenotypic variability in terms of age of onset, symptom severity, and progression. GeneReviews states that individuals with cblG “characteristically present in the first year of life with neurologic manifestations and megaloblastic anemia; however, phenotypic variability ranges from infantile to adult presentation,” reflecting a continuum of disease expression.[7] Kripps et al. reiterate this variability, noting presentations from neonatal seizures and encephalopathy to adolescent or adult psychiatric and neurologic symptoms.[11] Some patients experience a rapidly progressive course with early developmental arrest and severe neurologic disability, while others have a more insidious, slowly progressive course manifesting as white matter disease or cognitive impairment in adulthood.[11][14] The progression of biochemical abnormalities is generally stable in untreated individuals, with persistent hyperhomocysteinemia and hypomethioninemia, but clinical manifestations can progress as cumulative damage accrues in the nervous system and vasculature.[7][11][14] Treatment can alter the course dramatically, stabilizing or partially reversing neurologic deficits and preventing further deterioration, particularly if started early.[7][9][11][14] The frequency of specific phenotypes among affected individuals is difficult to quantify accurately due to the small number of reported cases, but megaloblastic anemia, hyperhomocysteinemia, homocystinuria, neurologic symptoms (seizures, hypotonia, developmental delay), and microcephaly appear to be common in infantile-onset cases, whereas adult-onset cases may more frequently present with leukoencephalopathy and psychiatric changes.[4][7][11][14]

## 4. Genetic and Molecular Information

### 4.1 The MTR Gene: Structure, Expression, and Function

The MTR gene (HGNC:7468) encodes 5‑methyltetrahydrofolate-homocysteine methyltransferase, also known as cobalamin-dependent methionine synthase, a critical enzyme in the remethylation of homocysteine to methionine.[2][6][16] NCBI Gene describes MTR as a protein-coding gene located on chromosome 1q43, with an exon count of 33 and official synonyms including “methionine synthase,” “cobalamin-dependent methionine synthase,” and “HMAG,” reflecting its disease association with homocystinuria-megaloblastic anemia G.[16] Watkins et al. characterized the structure of the MTR gene, identifying exon–intron boundaries and demonstrating that it is a highly compressed gene spanning at least 60 kb, with several introns of variable size.[2][6] MTR expression is ubiquitous, with RNA detected in kidney (RPKM 5.8), thyroid (RPKM 4.9), and many other tissues, consistent with the need for methionine and methylation reactions in diverse cell types.[16] At the protein level, methionine synthase is a large, multi-domain enzyme that binds methylcobalamin and 5‑methyltetrahydrofolate and catalyzes a transfer of a methyl group from the folate to homocysteine, producing methionine and tetrahydrofolate, thereby linking folate and cobalamin cycles.[2][6][7][16] The enzyme’s activity depends on the presence of methylcobalamin at the cobalt center of cobalamin and on periodic reductive activation by methionine synthase reductase (MTRR), which uses NADPH to re-reduce oxidized cobalamin.[2][6][7] Suggested GO terms for MTR include GO:0008705 (methionine synthase activity), GO:0006730 (one-carbon metabolic process), and GO:0006564 (lysine biosynthetic process via aspartate pathway; though more broadly, GO:0006555 methionine metabolic process).

### 4.2 Pathogenic Variant Spectrum and Classification

Pathogenic variants in MTR associated with cblG include a diverse spectrum of missense, nonsense, frameshift, splice-site, and small insertion/deletion mutations that disrupt methionine synthase’s catalytic function or stability.[2][6][11][16] Watkins et al. (2002) analyzed a cohort of 24 cblG patients and identified multiple pathogenic variants affecting different exons and domains of MTR, including the recurrent missense mutation P1173L and other substitutions, truncations, and splice alterations.[2][6] They documented genotype diversity, noting that “mutations in the MTR gene… result in the methylcobalamin deficiency G (cblG) disorder,” and that coding-region variants often cluster in regions encoding conserved functional motifs.[2][6] Gulati et al. (1996) and Leclerc et al. (1996, 1997) earlier reported pathogenic variants in MTR underlying methionine synthase deficiency; although detailed variant lists are not present in the snippet, these studies contributed to the identification of the gene’s disease role.[2] In Kripps et al.’s 2022 series, genetic analysis confirmed biallelic pathogenic MTR variants in all cblG patients, supporting the causal link between MTR mutations and the clinical phenotype.[11] Variant types can be classified according to ACMG/AMP guidelines, with many variants meeting criteria for pathogenicity based on predicted loss of function (nonsense, frameshift, canonical splice-site) or deleterious missense substitutions affecting highly conserved residues with supporting functional data demonstrating reduced methionine synthase activity.[2][6][11] Allele frequencies in population databases such as gnomAD are generally extremely low, consistent with the rarity of cblG, and there is no evidence of somatic mutations in MTR causing cblG-like phenotypes outside of germline contexts.[2][6][16] Suggested ClinVar annotations would categorize P1173L and other recurrent disease alleles as “pathogenic” or “likely pathogenic,” while common polymorphisms in MTR may be classified as benign or of uncertain significance, potentially modulating remethylation capacity but not causing overt disease.[2][6][11]

### 4.3 Functional Consequences: Loss-of-Function Mechanisms

Pathogenic variants in MTR cause functional deficiency of methionine synthase, typically through loss-of-function mechanisms such as impaired protein folding, reduced enzyme stability, disrupted cobalamin binding, or direct compromise of catalytic activity.[2][6][11][16] Missense mutations affecting residues in the cobalamin-binding domain or folate-binding domain can reduce the enzyme’s ability to form an active holoenzyme with methylcobalamin or to interact with 5‑methyltetrahydrofolate, diminishing methyl transfer efficiency.[2][6][7][16] Nonsense and frameshift mutations introduce premature termination codons, likely triggering nonsense-mediated mRNA decay or producing truncated, nonfunctional proteins that cannot perform remethylation.[2][6][11][16] Splice-site mutations can lead to exon skipping, intron retention, or cryptic splicing, altering the protein structure and abrogating function.[2][6][11] In vitro enzyme assays using patient fibroblasts demonstrate markedly reduced methionine synthase activity, and complementation analysis shows that cblG cells cannot be complemented by wild-type MTR expression, confirming the gene-specific defect.[1][2][5][6] The resultant loss of methionine synthase activity causes accumulation of homocysteine and depletion of methionine and S‑adenosylmethionine, profoundly impacting methylation reactions across DNA, RNA, proteins, and lipids.[2][7][11][14] There is no evidence that gain-of-function or dominant-negative MTR variants play a role in cblG; all characterized alleles are consistent with recessive loss-of-function mechanisms.[2][6][11]

### 4.4 Modifier Genes and Epigenetic Considerations

Modifier genes in cblG have not been systematically elucidated in the available literature, but genes involved in folate metabolism, homocysteine clearance, and methylation homeostasis could theoretically modify disease severity and expression.[7][11] For example, polymorphisms in MTHFR, the enzyme that converts 5,10‑methylenetetrahydrofolate to 5‑methyltetrahydrofolate, might influence the availability of folate substrate for methionine synthase, thereby modulating hyperhomocysteinemia severity.[7] Similarly, variants in CBS (cystathionine β‑synthase), which directs homocysteine toward transsulfuration rather than remethylation, could alter the balance of homocysteine metabolism in cblG, exacerbating or mitigating biochemical abnormalities.[7] GeneReviews notes that CBS deficiency is characterized by elevated serum methionine rather than hypomethioninemia, distinguishing it from remethylation disorders like cblG, but interactions between these pathways are important for differential diagnosis.[7] Epigenetic changes, such as global DNA hypomethylation, are expected in cblG due to SAM deficiency, and may contribute to clinical manifestations; however, specific epigenomic profiles in cblG have not been systematically characterized.[7][11][14] Suggested GO terms for biological processes impacted include GO:0006306 (DNA methylation), GO:0019438 (methylation), and GO:0043414 (biomass metabolic process), while epigenetic ontology terms in resources such as DiseaseMeth or MethBase would be relevant for future research.

### 4.5 Chromosomal Abnormalities and Structural Genomic Features

No recurrent large-scale chromosomal abnormalities (such as aneuploidy, translocations, or inversions) have been associated with cblG; the disorder arises from sequence-level mutations in MTR.[2][6][11][16] Genomic structural features of the MTR locus include its location on chromosome 1q43, a region that may harbor other genes relevant to metabolism and neurologic function.[16] NCBI Genome Data Viewer locates MTR at NC_000001.11 (236,795,281..236,903,981) on GRCh38, reflecting its precise genomic coordinates.[16] While structural variation such as copy-number changes affecting MTR could theoretically cause methionine synthase deficiency, such events have not been reported in the cblG literature, and chromosomal microarray or karyotyping are not primary diagnostic tools for cblG.[7][11] Suggested dbVar or DGV entries could be consulted for rare structural variants involving MTR in broader genomic datasets, but their clinical significance in cblG remains to be defined.

## 5. Environmental Information

### 5.1 Non-Genetic Contributing Factors

Non-genetic contributing factors to cblG primarily modulate disease severity rather than cause the disorder. Vitamin B\(_{12}\) status, folate intake, and general nutritional health are key environmental determinants of homocysteine metabolism.[7][8][9][11] In the general population, vegetarians and vegans are known to be at risk of vitamin B\(_{12}\) deficiency due to lack of animal products, leading to elevated plasma total homocysteine and increased risk of cardiovascular disease; Obersby et al. demonstrated that methylcobalamin supplementation effectively lowers homocysteine in such individuals.[8] While this study involves nutritional deficiency rather than genetic methionine synthase deficiency, it illustrates the sensitivity of homocysteine levels to cobalamin status and underscores the potential importance of maintaining adequate B\(_{12}\) intake in cblG patients to optimize residual enzyme function.[8][11] Environmental toxins that interfere with cobalamin metabolism, such as nitrous oxide, can inactivate methionine synthase and thereby mimic or exacerbate cblG, but these exposures are typically acute and reversible compared to the chronic, genetic defect in cblG.[7][11] Occupational exposures, radiation, and pollution have not been implicated in cblG pathogenesis. Infectious agents do not cause cblG, though infections may precipitate metabolic decompensation in affected individuals by increasing metabolic demands and oxidative stress.

### 5.2 Lifestyle Factors

Lifestyle factors such as diet, alcohol consumption, smoking, and exercise do not directly cause cblG but can influence the risk of complications, particularly thrombotic events related to hyperhomocysteinemia.[2][7][11] Elevated homocysteine has been linked to cardiovascular disease, stroke, and venous thrombosis in the general population, and individuals with cblG have markedly elevated homocysteine levels if untreated, potentially increasing their vascular risk.[2][8][11] Maintaining a healthy lifestyle with avoidance of smoking, moderation of alcohol intake, and regular exercise may help reduce overall cardiovascular risk in cblG patients, though specific studies in this population are lacking.[7][11] Dietary patterns emphasizing adequate protein, cobalamin, folate, and other B vitamins support one-carbon metabolism and may mitigate biochemical abnormalities when combined with medical therapy.[7][8][11] However, given the genetic basis of methionine synthase deficiency, lifestyle interventions alone cannot normalize homocysteine without pharmacologic treatment.

### 5.3 Infectious Agents

There is no evidence that specific infectious agents cause or directly trigger cblG. However, infections may exacerbate metabolic stress and precipitate neurologic or hematologic decompensation in individuals with underlying methionine synthase deficiency, as is common in many inborn errors of metabolism.[7][11] Standard infection control and vaccination strategies appropriate for the general population are recommended, but no special infectious disease precautions specific to cblG have been reported.

## 6. Mechanism and Pathophysiology

### 6.1 Overview of Cobalamin and Folate-Dependent One-Carbon Metabolism

The pathophysiology of methylcobalamin deficiency type cblG is best understood in the context of cobalamin and folate-dependent one-carbon metabolism, particularly the methionine cycle and homocysteine remethylation pathways.[2][7][9][11][16] Cobalamin (vitamin B\(_{12}\)) functions as a cofactor in two major enzymatic reactions in humans: the cytosolic methionine synthase reaction, which uses methylcobalamin to transfer a methyl group from 5‑methyltetrahydrofolate to homocysteine, forming methionine, and the mitochondrial methylmalonyl-CoA mutase reaction, which uses adenosylcobalamin to isomerize methylmalonyl-CoA to succinyl-CoA.[7][9] Disorders of intracellular cobalamin metabolism can affect the synthesis or use of either or both coenzyme forms, leading to selective or combined biochemical abnormalities.[7][9] In cblG, the defect lies in methionine synthase itself, causing selective methylcobalamin deficiency at the level of enzyme function, while adenosylcobalamin and methylmalonyl-CoA mutase activity are generally normal, explaining the absence of significant methylmalonic acid elevation.[2][7][11] The methionine synthase reaction links the folate cycle, which generates 5‑methyltetrahydrofolate from 5,10‑methylenetetrahydrofolate via MTHFR, with the methionine cycle, which converts homocysteine to methionine and then to S‑adenosylmethionine.[2][7][16] SAM is a universal methyl donor for numerous methyltransferases, including those involved in DNA, RNA, protein, phospholipid, and neurotransmitter methylation.[7][11][14] Disruption of methionine synthase therefore has widespread consequences across cellular methylation reactions, particularly in tissues with high methylation demands such as the central nervous system.

### 6.2 Upstream Defect: Methionine Synthase Dysfunction

The upstream pathogenic event in cblG is loss-of-function mutation in MTR, leading to methionine synthase dysfunction. Methionine synthase requires an enzyme-bound methylcobalamin prosthetic group and interacts with 5‑methyltetrahydrofolate and homocysteine in a catalytic cycle that transfers the methyl group to homocysteine, forming methionine and tetrahydrofolate.[2][6][16] Mutations in MTR reduce the enzyme’s ability to form an active holoenzyme, bind substrates, or carry out methyl transfer, resulting in decreased conversion of homocysteine to methionine.[2][6][11][16] Cellular complementation studies in fibroblasts derived from cblG patients demonstrate deficient methionine biosynthesis by intact cells, as measured by incorporation of label from 5‑[14C]methyl-tetrahydrofolate into acid-precipitable material, confirming that methionine synthase activity is impaired.[1][2][5] The JCI article reporting genetic heterogeneity among patients with methylcobalamin deficiency notes that methionine biosynthesis by intact cells is deficient in cultured skin fibroblasts from all cblG patients, and that this deficiency correlates with decreased methionine synthase activity measured in vitro.[1] These findings support the role of MTR as the upstream locus whose mutation initiates the biochemical cascade in cblG.

### 6.3 Metabolic Consequences: Hyperhomocysteinemia and Hypomethioninemia

Downstream of methionine synthase dysfunction, homocysteine accumulates and methionine synthesis is impaired, producing the characteristic biochemical phenotype of hyperhomocysteinemia, homocystinuria, and hypomethioninemia.[2][3][7][11][15] Homocysteine is a sulfur-containing amino acid that occupies a central position in the methionine cycle; under normal conditions, it can be remethylated to methionine via methionine synthase (using 5‑methyltetrahydrofolate) or via betaine-homocysteine methyltransferase (using betaine as methyl donor), or directed toward the transsulfuration pathway via CBS to form cystathionine and cysteine.[2][7] In cblG, the methionine synthase route is severely compromised, placing greater burden on alternative pathways; if these cannot fully compensate, homocysteine accumulates in plasma and urine.[2][7][11] GeneReviews emphasizes that cblG is characterized biochemically by “hyperhomocysteinemia and hypomethioninemia,” distinguishing it from CBS deficiency, which features elevated methionine.[7] Hypomethioninemia arises because methionine synthesis from homocysteine is impaired, and dietary methionine may not suffice to maintain normal levels, especially in children with poor intake or increased demand.[2][7][11][15] Reduced methionine availability, in turn, leads to decreased synthesis of S‑adenosylmethionine via methionine adenosyltransferase, impairing global methylation reactions.[7][11][14] The metabolic disturbance affects numerous systems; homocysteine itself exerts toxic effects on endothelial cells, neurons, and other cell types through mechanisms involving oxidative stress, excitotoxicity, and endothelial dysfunction, while hypomethioninemia contributes to impaired protein synthesis and methylation-dependent regulation.[2][7][11][14]

### 6.4 Cellular and Tissue-Level Mechanisms: Hypomethylation and Myelin Damage

At the cellular level, cblG leads to widespread hypomethylation of DNA, RNA, proteins, and lipids due to SAM deficiency, with particularly profound effects in the nervous system where methylation plays critical roles in myelination, neurotransmitter metabolism, and gene regulation.[7][11][14] Methionine and SAM are required for the methylation of phospholipids such as phosphatidylethanolamine to phosphatidylcholine, essential for myelin membrane integrity, and for methylation of myelin basic protein and other structural components.[7][11][14] Chronic methionine synthase deficiency thus impairs myelin formation and maintenance, contributing to white matter abnormalities observed in MRI studies of cblG patients, including leukoencephalopathy with diffuse or patchy demyelination.[11][14] Adult-onset leukoencephalopathy described in Neurology is attributed to methionine synthase deficiency and demonstrates reversible or partially reversible white matter changes upon treatment with hydroxocobalamin.[14] DNA hypomethylation may alter gene expression patterns, affecting neuronal development, synaptic function, and responses to injury. In hematopoietic tissues, impaired folate and cobalamin-dependent one-carbon metabolism leads to defective thymidylate and purine synthesis, producing megaloblastic anemia through nuclear–cytoplasmic maturation asynchrony.[7][11] In endothelial cells and the vascular system, elevated homocysteine induces oxidative stress, promotes LDL oxidation, and impairs nitric oxide signaling, potentially increasing the risk of thrombosis and vascular disease, as established in broader hyperhomocysteinemia literature.[2][8][11] Suggested GO terms for processes impacted include GO:0006306 (DNA methylation), GO:0007272 (ensheathment of neurons—myelination), GO:0006950 (response to stress), and GO:0008219 (cell death).

### 6.5 Immune System and Tissue Damage Mechanisms

Direct involvement of the immune system in cblG pathophysiology has not been extensively characterized, but chronic hyperhomocysteinemia and hypomethylation may contribute to inflammatory and immune dysregulation. Homocysteine has been shown in other contexts to promote pro-inflammatory cytokine production, oxidative stress, and endothelial activation, which could predispose to vascular inflammation and damage.[2][8] Tissue damage mechanisms in cblG include oxidative stress in the brain and vasculature due to homocysteine-mediated generation of reactive oxygen species, leading to lipid peroxidation and membrane injury, particularly in myelin and neuronal membranes.[2][7][11][14] White matter damage observed as leukoencephalopathy on MRI likely reflects a combination of hypomyelination, demyelination, and axonal injury driven by metabolic insufficiency rather than primary immune attack.[11][14] Necrosis or apoptosis of neurons and glial cells may occur in severe, untreated cases, contributing to irreversible neurologic deficits. In the bone marrow, megaloblastic changes result from disrupted DNA synthesis rather than direct tissue injury, though anemia and pancytopenia can lead to secondary complications such as fatigue and increased infection risk.[7][11] Suggested GO terms include GO:0006979 (response to oxidative stress), GO:0008219 (cell death), and GO:0006954 (inflammatory response).

### 6.6 Molecular Profiling and Omics Perspectives

Formal transcriptomic, proteomic, metabolomic, and lipidomic profiling studies specific to cblG have not been widely reported, but extrapolation from broader one-carbon metabolism and homocysteine research suggests characteristic omics signatures. Transcriptomics in cblG would be expected to reveal altered expression of genes involved in myelination, synaptic function, and methylation-sensitive pathways, with possible upregulation of stress response genes and downregulation of myelin-related genes. Proteomics might show reduced levels of myelin proteins, altered methylated protein isoforms, and changes in enzymes of the one-carbon pathway. Metabolomics would confirm elevated homocysteine, low methionine, altered SAM and S‑adenosylhomocysteine ratios, and possibly changes in folate intermediates, while lipidomics would highlight altered phosphatidylcholine and sphingomyelin composition in myelin. These multi-omics signatures could be investigated in future research using platforms such as GEO, PRIDE, HMDB, and Metabolomics Workbench, and integrated with clinical phenotypes to refine disease mechanisms. Single-cell and spatial transcriptomics in brain tissue from cblG models could reveal cell-type specific vulnerability of oligodendrocytes, astrocytes, and neurons to methionine synthase deficiency, and functional genomics screens might identify modifiers of homocysteine toxicity and methylation capacity. Currently, however, such advanced omics data remain speculative in cblG and are inferred from related disorders rather than directly observed.

## 7. Anatomical Structures Affected

### 7.1 Organ-Level Involvement

Methylcobalamin deficiency type cblG primarily affects the central nervous system and hematopoietic system, with secondary involvement of the vascular system and other organs. The brain, encompassing structures such as the cerebral white matter (UBERON:0002435), cortex (UBERON:0000956), basal ganglia (UBERON:0002435), and cerebellum (UBERON:0002037), is a major site of pathology, as evidenced by neurologic symptoms and MRI-detected leukoencephalopathy.[7][11][14] White matter tracts in the supratentorial and infratentorial regions are particularly affected, reflecting the high demand for methylation in myelin maintenance.[11][14] The spinal cord may also be involved, though specific data are limited; by analogy with acquired cobalamin deficiency myelopathy, posterior column damage could occur. The bone marrow (UBERON:0002371) and peripheral blood are affected in megaloblastic anemia, with macrocytic red cells and ineffective erythropoiesis.[7][11] The liver (UBERON:0002107), kidney (UBERON:0002113), and other organs participate in homocysteine and methionine metabolism, but overt organ-specific damage beyond metabolic disturbance is less well characterized. The cardiovascular system, including arteries and veins (UBERON:0001620, UBERON:0004537), may be impacted via hyperhomocysteinemia-associated endothelial dysfunction and thrombosis risk, although specific reports of vascular events in cblG are sparse.[2][8][11] Overall, cblG can be categorized as a multisystem metabolic disorder with predominant neurologic and hematologic manifestations.

### 7.2 Tissue and Cell-Type Involvement

At the tissue level, nervous tissue, hematopoietic tissue, and endothelial tissue are key sites of pathology. In the central nervous system, white matter tissue comprising myelinated axons, oligodendrocytes, astrocytes, and microglia is particularly vulnerable to methionine and methylation deficiency.[7][11][14] Oligodendrocytes (CL:0000128) are responsible for myelin formation and maintenance; impaired methylation and phospholipid synthesis in these cells likely contribute to hypomyelination and demyelination seen in leukoencephalopathy.[11][14] Neurons (CL:0000540) and astrocytes (CL:0000127) also depend on methylation for synaptic plasticity, neurotransmitter metabolism, and supportive functions; their dysfunction manifests as seizures, encephalopathy, and cognitive impairment.[7][11][14] In the bone marrow, erythroid precursors (CL:0000556) exhibit megaloblastic changes due to impaired DNA replication, causing macrocytic anemia.[7][11] Endothelial cells (CL:0000115) lining blood vessels are exposed to elevated homocysteine and may suffer oxidative damage, predisposing to vascular complications.[2][8] Hepatocytes and renal tubular cells participate in homocysteine clearance and methionine metabolism, but specific histopathologic changes in these tissues have not been reported in cblG. Suggested CL terms for cell types involved include oligodendrocyte (CL:0000128), neuron (CL:0000540), astrocyte (CL:0000127), erythroid progenitor cell (CL:0000556), and endothelial cell (CL:0000115).

### 7.3 Subcellular Localization and Compartmental Effects

Subcellular compartments involved in cblG pathophysiology include the cytosol, where methionine synthase resides and where homocysteine and 5‑methyltetrahydrofolate interact, and the nucleus, where DNA methylation patterns are altered by SAM deficiency.[2][6][7][16] Methionine synthase is a cytosolic enzyme (GO:0005829, cytosol), and its dysfunction directly affects cytosolic one-carbon flux and methionine production.[2][6][16] The nucleus (GO:0005634) is affected via hypomethylation of DNA and histones, altering epigenetic regulation. Mitochondria (GO:0005739) participate indirectly in one-carbon metabolism and may experience oxidative stress due to homocysteine, though mitochondrial cobalamin-dependent methylmalonyl-CoA mutase is generally intact in cblG.[7][9] The endoplasmic reticulum and Golgi apparatus may be impacted by disrupted phospholipid methylation, affecting membrane composition. Cellular compartments associated with SAM-dependent methyltransferases (GO:0008168) are functionally compromised due to substrate deficiency. These subcellular perturbations collectively contribute to tissue-level dysfunction in nervous and hematopoietic systems.

### 7.4 Anatomical Localization and Lateralization

Anatomical localization of neurologic lesions in cblG, particularly in adult-onset leukoencephalopathy, has been described in Neuroimaging studies, which show diffuse or patchy white matter abnormalities that can be bilateral and symmetric or asymmetric depending on severity and treatment status.[14] Leukoencephalopathy in methionine synthase deficiency often involves the periventricular, subcortical, and cerebellar white matter, with MRI showing T2 hyperintensities that may improve with therapy.[11][14] There is no consistent lateralization pattern; lesions are typically bilateral, reflecting systemic metabolic insult. Microcephaly in infants reflects global reduced brain growth rather than focal structural defects. Hematologic manifestations are systemic, affecting the entire erythroid compartment.

## 8. Temporal Development

### 8.1 Age of Onset and Onset Patterns

The typical age of onset in cblG is within the first year of life, with many infants presenting in the neonatal period or early infancy with neurologic symptoms and megaloblastic anemia.[4][7][11] GeneReviews notes that individuals with cblG “characteristically present in the first year of life,” though it explicitly acknowledges that phenotypic variability includes infantile to adult presentations.[7] NORD reports that signs and symptoms in methylcobalamin deficiency cblG type usually develop during the first year of life, but that age of onset can range from infancy to adulthood.[4] Early-onset presentations often follow an acute or subacute pattern, with rapid development of encephalopathy, seizures, hypotonia, feeding difficulties, and anemia over weeks to months.[4][7][11] Adult-onset cases, including those described in Neurology, typically exhibit an insidious or sometimes acute onset of cognitive decline, gait disturbance, or psychiatric symptoms, with MRI-detected white matter changes evolving over months.[11][14] The onset pattern in adolescent and adult cases can be subacute, with symptoms developing over several weeks, or chronic and slowly progressive. The presence of milder, subclinical biochemical abnormalities may precede clinical symptom onset, particularly in individuals with partial residual enzyme activity.

### 8.2 Disease Progression and Staging

The progression of cblG is variable and depends strongly on treatment timing and adequacy. In untreated infants with severe methionine synthase deficiency, disease progression can be rapid and devastating, leading to profound developmental delay, microcephaly, and irreversible neurologic deficits within the first two years of life.[4][7][11] In such cases, one can conceptualize early-stage disease as encompassing nonspecific symptoms like feeding difficulties and mild hypotonia, intermediate stages as featuring seizures, encephalopathy, and megaloblastic anemia, and advanced stages as involving severe developmental arrest, microcephaly, and spasticity.[4][7] In adolescent and adult-onset cblG, progression may be more gradual, with initial psychiatric or cognitive symptoms followed by motor deficits and leukoencephalopathy; however, acute worsening can occur during metabolic stress or when homocysteine levels rise further.[11][14] Treatment can arrest progression and even reverse some features, particularly at early stages; hydroxocobalamin therapy in adult leukoencephalopathy patients led to clinical improvement within three months and normalization of biochemical abnormalities within one year.[14] Kripps et al. demonstrate that early-treated patients have more favorable long-term outcomes, with better cognitive and motor function than those treated after significant neurologic damage has occurred.[11] Disease course patterns thus include progressive untreated disease, stable or improved disease under treatment, and potentially relapsing-remitting episodes of neurologic decompensation associated with metabolic stress or treatment lapses.

### 8.3 Disease Duration and Lifelong Course

CblG is a chronic, lifelong disorder; genetic methionine synthase deficiency persists throughout life, and continuous or recurrent treatment is necessary to maintain metabolic control and prevent relapse.[2][7][11][14] With adequate therapy, individuals can survive into adolescence and adulthood, although their quality of life and functional status depend on the severity of early neurologic involvement.[7][11][14] In the absence of treatment, severely affected infants may die in early childhood due to complications of neurologic dysfunction, infections, or metabolic crises, although precise mortality rates are not well documented given the small number of reported cases.[7][11] Late-diagnosed adult patients may have chronic leukoencephalopathy and cognitive impairment, but with treatment can achieve partial recovery and stabilization.[14] Thus, disease duration spans the entire lifespan of affected individuals, with a trajectory shaped by diagnosis timing and therapy.

### 8.4 Remission Patterns and Critical Periods

Remission in cblG is best understood as treatment-induced biochemical and clinical improvement rather than spontaneous remission. Kripps et al. and Neurology case reports show that hydroxocobalamin and adjunctive therapies can induce remission of hyperhomocysteinemia and hypomethioninemia and alleviate neurologic symptoms, especially when instituted early.[11][14] In adult leukoencephalopathy, remission of MRI abnormalities and clinical improvement occurred over months to a year of treatment.[14] However, spontaneous remission without treatment has not been reported; the genetic defect is fixed. Critical periods in cblG include the first year of life, during which brain development is rapid and particularly vulnerable to methylation deficit; early treatment during this period can prevent irreversible damage.[4][7][11] Kripps et al. emphasize that treatment before neurologic symptoms manifest leads to significantly better outcomes than later treatment, underscoring infancy as a critical window for intervention.[11] Similarly, early adolescence may represent a critical period in adult-onset cases, as some patients developed acute leukoencephalopathy in late teenage years or early adulthood and benefited from prompt treatment.[11][14] These observations support inclusion of cblG in newborn screening programs to identify affected individuals at birth or shortly thereafter, allowing presymptomatic therapy.[7][11]

## 9. Inheritance and Population Characteristics

### 9.1 Epidemiology and Prevalence

The true prevalence of cblG is unknown, reflecting its rarity and the limited number of reported cases. GeneReviews notes that fewer than 40 cases have been described for cblE and cblG combined, and fewer than 20 cases each for several other cobalamin metabolism disorders such as cblD, cblF, cblJ, and cblX.[7] This suggests that cblG likely affects far fewer than one per 100,000 births and may have an incidence on the order of 1:1,000,000 or lower, though precise figures are not available.[7][11] In contrast, cblC, the most common cobalamin metabolism defect, has an estimated incidence of 1:200,000 births, with newborn screening suggesting higher incidence in certain populations such as Hispanics in California.[7][9] The rarity of cblG complicates epidemiologic estimation, and underdiagnosis due to nonspecific symptoms and lack of routine homocysteine measurement likely contributes to an apparent lower prevalence in published literature.[7][11][14] No large-scale population-based registries have systematically captured cblG cases, and national or global burden-of-disease estimates are not available.

### 9.2 Inheritance Pattern, Penetrance, and Expressivity

CblG follows an autosomal recessive inheritance pattern, with biallelic MTR pathogenic variants required for disease expression and heterozygous carriers generally asymptomatic.[2][4][7][11][16] Penetrance in individuals with biallelic loss-of-function MTR mutations appears to be high; severe biochemical abnormalities and clinical manifestations are observed in most such individuals, although some may have milder or late-onset presentations depending on residual activity and modifiers.[7][11][14] Expressivity is markedly variable, ranging from severe infantile encephalopathy and developmental arrest to adolescent or adult-onset psychiatric and neurologic symptoms with leukoencephalopathy.[4][7][11][14] This variability reflects differences in mutation severity, nutritional status, and treatment timing. Genetic anticipation, in the sense of increasing severity in successive generations due to repeat expansions, is not relevant in cblG; there is no evidence of such mechanisms in MTR. Germline mosaicism has not been reported but could theoretically occur, as in other autosomal recessive disorders, affecting recurrence risk estimates. Founder effects, wherein specific pathogenic MTR variants are enriched in particular populations, have not been definitively established, although the recurrent P1173L mutation’s high frequency among studied cases suggests that regional enrichment is possible.[2][6] The role of consanguinity in cblG is likely similar to that in other autosomal recessive disorders, increasing the probability of homozygosity for rare pathogenic alleles, but specific data on consanguinity frequency in cblG families are limited.[7][11]

### 9.3 Population Demographics and Geographic Distribution

Detailed demographic analysis of cblG is hampered by the small number of reported cases and lack of population-based studies. Published cases have arisen from diverse geographic regions, including North America and Europe, reflecting the global distribution of cobalamin metabolism disorders.[2][4][7][11][14] GeneReviews notes that cblG and cblE are rare syndromes, but does not identify particular ethnic or geographic predispositions.[7] The P1173L mutation appears in multiple unrelated patients, suggesting either a mutational hotspot or founder effect, but haplotype analysis by Watkins et al. indicates that this mutation arose independently on at least two different genetic backgrounds, arguing against a single founder.[2][6] Sex distribution in cblG appears roughly equal; both males and females are affected, and no strong sex bias has been reported.[4][7][11][14] Age distribution reflects the variable onset; infants, children, adolescents, and adults have all been described, with early-onset cases often showing more severe neurologic disability.[4][7][11][14] Carrier frequency in the general population is unknown but likely extremely low; gnomAD and similar population databases may contain occasional heterozygous MTR pathogenic variants but not enough data to estimate precise carrier rates. Geographic distribution of specific variants such as P1173L could be elucidated by mining global population data, but such analyses have not been published for cblG.

## 10. Diagnostics

### 10.1 Clinical and Biochemical Testing

Diagnosis of cblG involves recognition of characteristic clinical features and confirmation by biochemical and genetic testing. Clinically, suspicion arises in infants with megaloblastic anemia, neurologic manifestations (seizures, hypotonia, developmental delay, encephalopathy), and microcephaly, or in adolescents/adults with unexplained hyperhomocysteinemia, homocystinuria, neurologic symptoms, and normal methylmalonic acid.[4][7][11][14] Laboratory evaluation typically includes complete blood count and smear to detect macrocytic or megaloblastic anemia, and metabolic testing for plasma total homocysteine, plasma methionine, and urine homocystine.[2][3][7][11][15] Hyperhomocysteinemia and homocystinuria, combined with hypomethioninemia and normal methylmalonic acid, strongly suggest a remethylation defect and specifically point toward cblG or cblE.[2][3][7][11][15] GeneReviews’ diagnostic table highlights that MeCbl deficiency cblG shows normal C3 acylcarnitine, normal methylmalonic acid, increased homocysteine, and low methionine, whereas other disorders such as cblC show elevated methylmalonic acid and C3.[7] LOINC codes and laboratory ontology terms would map to tests such as “Homocysteine [Mass/volume] in Serum or Plasma” and “Methionine [Moles/volume] in Serum or Plasma.” Additional biochemical assessments, including vitamin B\(_{12}\) and folate levels, help distinguish nutritional deficiency from genetic remethylation disorders. Enzyme assays in fibroblasts, measuring methionine synthase activity and methionine biosynthesis from labeled 5‑methyltetrahydrofolate, can confirm functional deficiency, though such assays are now less commonly used in routine diagnosis.[1][2][5] Complementation analysis with cblE or cblG reference fibroblast lines can differentiate cblG from cblE, but genetic testing has largely superseded these labor-intensive methods.[1][2][5][7]

### 10.2 Genetic Testing Strategies

Genetic testing for cblG focuses on sequencing the MTR gene to identify biallelic pathogenic variants. Single-gene testing of MTR, using Sanger sequencing or targeted next-generation sequencing panels, is appropriate when biochemical and clinical features strongly suggest methionine synthase deficiency.[2][6][11][16] Gene panels for homocysteine metabolism disorders or cobalamin metabolism defects typically include MTR, MTRR, MMACHC, MMADHC, and other relevant genes, allowing simultaneous evaluation of multiple pathways.[7][9][11] Whole exome sequencing (WES) or whole genome sequencing (WGS) can be particularly useful in atypical presentations or where biochemical findings are ambiguous, and have been employed successfully in diagnosing cblG in some cases.[11] ClinVar and GTR list multiple laboratories offering MTR testing, though specific entries are not detailed in the provided search results. Chromosomal microarray and karyotyping are not primary diagnostic tools for cblG, as structural chromosomal aberrations are not characteristic. Mitochondrial DNA testing and repeat expansion testing are likewise not relevant. Genetic testing confirms the diagnosis when biallelic pathogenic MTR variants are identified, and supports genetic counseling regarding recurrence risk and carrier status in family members.[2][6][7][11][16]

### 10.3 Imaging and Electrophysiological Studies

Neuroimaging, particularly MRI, is valuable in assessing white matter involvement and leukoencephalopathy in cblG, especially in adolescent and adult patients with neurologic symptoms.[11][14] MRI may show diffuse or patchy T2-weighted hyperintensities in supratentorial and cerebellar white matter, sometimes mimicking demyelinating disorders or leukodystrophies.[11][14] Treatment-induced changes in MRI, with partial or complete resolution of lesions after hydroxocobalamin therapy, support the diagnosis and indicate reversibility of metabolic white matter damage.[14] CT scanning is less sensitive for white matter changes and is not preferred. EEG can reveal seizure activity or diffuse slowing in encephalopathic infants, while EMG and nerve conduction studies may be less informative unless peripheral neuropathy is present. No specific electrophysiologic signature is unique to cblG, but such studies help characterize neurologic involvement.

### 10.4 Pathology and Biopsy Findings

Histopathologic examination in cblG is rarely performed, but bone marrow biopsies may show megaloblastic changes, including giant metamyelocytes, enlarged erythroid precursors, and nuclear–cytoplasmic dissociation, characteristic of folate and cobalamin deficiency.[7][11] Brain biopsy or autopsy in severe cases could reveal white matter demyelination and gliosis, but such data are scarce. Pathology findings primarily reflect biochemical and cellular defects in one-carbon metabolism rather than specific structural lesions.

### 10.5 Clinical Criteria and Differential Diagnosis

There are no formal diagnostic criteria codified by professional societies for cblG, but a combination of clinical, biochemical, and genetic findings establishes the diagnosis. ICD‑10 and ICD‑11 codes may classify cblG under “Other disorders of amino-acid metabolism” or “Other metabolic disorders”, though specific cblG codes are not detailed in the search results. Differential diagnosis includes other causes of homocystinuria and hyperhomocysteinemia, such as CBS deficiency, MTHFR deficiency, and combined cobalamin metabolism disorders like cblC, cblD, and cblF.[7][9][11] CBS deficiency features elevated homocysteine and methionine, lens dislocation, skeletal abnormalities, and thromboembolism, and responds to vitamin B\(_{6}\) in some cases; biochemical differentiation is based on elevated methionine rather than low methionine.[7] MTHFR deficiency presents with severe neurologic impairment and elevated homocysteine but normal methionine, and does not show megaloblastic anemia.[7] CblC presents with both hyperhomocysteinemia and methylmalonic acidemia, often with microangiopathy and ocular abnormalities, and is caused by MMACHC mutations.[7][9] Nutritional vitamin B\(_{12}\) deficiency causes megaloblastic anemia and elevated homocysteine and methylmalonic acid, but is distinguished by low serum B\(_{12}\) and response to dietary correction.[7][8] Recognizing the pattern of low methionine, normal methylmalonic acid, and elevated homocysteine is crucial in differentiating cblG from these conditions.[2][7][11][15]

### 10.6 Screening and Newborn Detection

Newborn screening for cblG is challenging because conventional tandem mass spectrometry programs typically target elevated acylcarnitines such as C3 (propionylcarnitine) and metabolic markers like methylmalonic acid, which are not elevated in pure remethylation defects.[7] GeneReviews notes that detection of cblD-homocystinuria, cblE, and cblG “do not have elevated C3 and are often not identified on newborn screening,” highlighting a limitation of existing screening algorithms.[7] Chace et al., Weisfeld-Adams et al., and Huemer et al. have argued for including low methionine measurement in newborn screening to detect remethylation disorders, but practical implementation remains limited.[7] Kripps et al. emphasize that cblG warrants inclusion in newborn screening due to the improved outcomes observed in presymptomatic patients treated early, underscoring the potential benefits of adding homocysteine or methionine assays to newborn panels.[11] Carrier screening for MTR pathogenic variants is not routinely performed but could be offered in high-risk families or populations. Prenatal testing and preimplantation genetic diagnosis are possible when familial MTR mutations are known, enabling early detection and intervention planning.

## 11. Outcome and Prognosis

### 11.1 Survival, Mortality, and Life Expectancy

Formal survival and mortality statistics for cblG are not available due to the small number of documented cases, but the available literature suggests that, with adequate treatment, many individuals can survive into adolescence and adulthood, while untreated severe cases may result in early death.[7][11][14] GeneReviews notes that disorders of intracellular cobalamin metabolism can be associated with significant morbidity and mortality, particularly in early-onset forms with multisystem involvement.[7][9] In cblG, mortality may result from severe neurologic disability, respiratory complications, infections, or vascular events related to hyperhomocysteinemia, though specific data are scarce.[7][11] Adult-onset cases described in Neurology survived and improved with treatment, indicating that life expectancy can be near-normal with appropriate therapy, albeit with potential residual neurologic deficits.[14] The overall prognosis varies widely, with factors such as age at diagnosis, treatment timing, mutation severity, and comorbid conditions influencing survival.

### 11.2 Morbidity, Disability, and Quality of Life

Morbidity in cblG is substantial, particularly in early-onset cases with severe neurodevelopmental impairment. Many affected infants and children experience significant developmental delay, intellectual disability, motor dysfunction, and microcephaly, limiting their ability to achieve independence and necessitating long-term supportive care.[4][7][11][13] Hematologic morbidity includes recurrent anemia and fatigue, which can be managed with treatment. Hyperhomocysteinemia may contribute to vascular morbidity, increasing the risk of thrombosis and cardiovascular disease, though specific incidence data are lacking.[2][8][11] Disability outcomes include inability to walk, talk, or perform self-care in severely affected individuals, and moderate disability in those with milder neurologic involvement. Adult-onset patients may suffer cognitive impairment and gait disturbance, affecting employment and social functioning, but can experience improvement with therapy.[11][14] Formal quality-of-life assessments using instruments such as EQ‑5D, SF‑36, or PROMIS have not been reported specifically for cblG, but qualitative descriptions indicate high burden of disease and caregiving stress. Early-treated patients have better functional outcomes and quality of life than late-treated counterparts, reinforcing the importance of early detection.[11]

### 11.3 Disease Course, Complications, and Recovery Potential

The disease course in cblG ranges from rapidly progressive infancy-onset encephalopathy to slowly evolving adult-onset leukoencephalopathy. Complications include seizures, spasticity, respiratory compromise, feeding difficulties requiring gastrostomy, and risk of thrombotic events, though systematic data on complications are limited.[4][7][11][14] Recovery potential depends on the extent of established neurologic damage at the time of treatment initiation; early biochemical correction can prevent further damage and allow partial or near-complete functional recovery in some cases, whereas irreversible deficits such as microcephaly and severe intellectual disability may persist despite treatment.[7][11] Neurology reports of adult methionine synthase deficiency show significant recovery of white matter lesions and neurologic function upon hydroxocobalamin therapy, illustrating that even chronic white matter damage can be partially reversible.[14] Kripps et al. demonstrate that early-treated patients, particularly those treated before neurologic symptoms, have more favorable outcomes, underscoring the value of presymptomatic treatment.[11] Prognostic factors therefore include age at onset, age at diagnosis, mutation severity, baseline neurologic status, and adequacy of treatment.

### 11.4 Prognostic Biomarkers and Factors

Biochemical markers such as plasma total homocysteine and plasma methionine serve as prognostic indicators in cblG; persistent high homocysteine and low methionine despite treatment may correlate with poorer outcomes, whereas normalization of these indices suggests good metabolic control and likely better prognosis.[2][7][9][11][14] MRI findings of leukoencephalopathy can serve as imaging biomarkers; reversal or improvement of white matter lesions with treatment indicates favorable prognosis, while progressive demyelination despite therapy portends worse outcomes.[11][14] Genetic factors, such as mutation type and location within MTR, may influence prognosis, although specific genotype–phenotype correlations are not fully delineated; severe truncating mutations may be associated with more profound deficiency and earlier onset than some missense mutations.[2][6][11] Age at treatment initiation is a critical prognostic factor; earlier treatment predicts better developmental outcomes and lower morbidity.[7][11] No formal prognostic models or biomarker panels have been published for cblG, but integration of biochemical, imaging, and genetic data could support future prognostic tools.

## 12. Treatment

### 12.1 Pharmacologic Therapy: Hydroxocobalamin, Betaine, Folates, and Methionine

Standard treatment for methylcobalamin deficiency type cblG involves high-dose parenteral hydroxocobalamin (vitamin B\(_{12}\)), betaine (trimethylglycine), folate or folinic acid, and, in some cases, methionine supplementation.[4][7][9][11][14] Hydroxocobalamin is preferred over cyanocobalamin because it is more efficiently converted to active coenzyme forms and may better support intracellular cobalamin pools.[7][9][11][14] In cblG, hydroxocobalamin serves to maximize residual methionine synthase activity by saturating the enzyme with cofactor, facilitating methylcobalamin holoenzyme formation in cells with partial function.[2][7][9][11][14] Betaine provides an alternative methyl donor for homocysteine via betaine-homocysteine methyltransferase, bypassing the defective methionine synthase pathway and reducing homocysteine levels while generating methionine.[7][9][11] Folic acid or folinic acid (5‑formyltetrahydrofolate) supports the folate cycle and may increase 5‑methyltetrahydrofolate availability, further assisting remethylation.[7][9][11] Methionine supplementation can be used in some patients to correct hypomethioninemia directly, though caution is needed to avoid excessively high levels.[11] Kripps et al. describe medical management of cblG using hydroxocobalamin, betaine, folinic acid, and methionine supplementation, noting that treatment improves biochemical profiles, with lowering of total homocysteine and increasing methionine.[11] Neurology reports indicate that intramuscular hydroxocobalamin therapy in adult methionine synthase deficiency normalized biochemical abnormalities within one year and produced clinical improvement within three months.[14] GeneReviews similarly recommends high-dose parenteral hydroxocobalamin and betaine, along with folate, as mainstays of therapy for remethylation disorders.[7][9]

Suggested NCIT clinical intervention terms include “Hydroxocobalamin Injection”, “Betaine Therapy”, “Folic Acid Therapy”, “Folinic Acid Therapy”, and “Methionine Supplementation.” Mechanistically, these pharmacologic therapies act at both upstream and downstream levels, enhancing residual methionine synthase function, providing alternative remethylation routes, and correcting substrate deficiencies.

### 12.2 Advanced Therapeutics: Gene and Cell-Based Approaches

There are currently no approved gene therapy or cell-based therapies specifically targeting cblG, but the monogenic nature of MTR deficiency makes it a plausible candidate for future gene replacement or editing strategies. Viral vectors such as AAV, lentivirus, or CRISPR/Cas9-based systems could theoretically deliver functional MTR to target tissues, particularly the liver or central nervous system, restoring methionine synthase activity.[2][6][16] However, challenges include achieving sufficient expression in diverse tissues, avoiding immune responses, and ensuring precise regulation of one-carbon metabolism. No clinical trials of gene therapy for cblG are registered in ClinicalTrials.gov based on the information provided, and current management relies on pharmacologic approaches. Cell therapy, such as hematopoietic stem cell transplantation, is not indicated in cblG, as the defect is systemic and involves multiple tissues. RNA-based therapies, monoclonal antibodies, and immunotherapies are not currently relevant. Future research may explore gene editing of MTR in induced pluripotent stem cells and their differentiation into hepatocytes or neurons, but such approaches remain investigational.

### 12.3 Supportive and Rehabilitative Care

Supportive care is crucial for individuals with cblG, particularly those with severe neurologic and developmental disabilities. This includes seizure management with antiepileptic drugs, physical therapy to address hypotonia and motor deficits, occupational therapy for fine motor skills and daily living activities, speech therapy for communication, and nutritional support for feeding difficulties.[4][7][11] Often, multidisciplinary care involving neurologists, metabolic specialists, hematologists, dietitians, and therapists is necessary. Rehabilitation aims to maximize functional independence and quality of life, even when some deficits are irreversible. Management of anemia may involve transfusions in acute settings and long-term vitamin supplementation. Psychological support for patients and families is important, given the chronic nature of the disorder and caregiving demands.

### 12.4 Experimental Treatments and Clinical Trials

No specific experimental treatments or clinical trials targeting cblG are highlighted in the provided search results. However, broader research on homocysteine-lowering therapies, such as folate, vitamin B\(_{6}\), riboflavin, and other methyl donors, may inform adjunctive strategies in cblG.[8] Betaine is already an established therapy for remethylation disorders and is used experimentally in other hyperhomocysteinemia contexts.[7][9][11] Larger clinical trials may eventually evaluate the comparative effectiveness of different cobalamin forms (hydroxocobalamin versus methylcobalamin) in cblG, though current evidence suggests hydroxocobalamin is preferred.

### 12.5 Treatment Outcomes and Personalized Medicine

Treatment outcomes in cblG are strongly influenced by timing of therapy initiation and individual genetic background. Kripps et al. report that treatment leads to improvement in biochemical profiles and, in many cases, stabilization or improvement of neurologic function, with early-treated patients achieving better outcomes.[11] Neurology reports similarly show normalization of homocysteine and methionine levels and clinical recovery in adult leukoencephalopathy patients upon hydroxocobalamin therapy.[14] Side effects and adverse events associated with cblG therapies are generally mild; hydroxocobalamin injections may cause discomfort or rare hypersensitivity, and betaine can cause gastrointestinal symptoms at high doses.[7][9][11] Personalized medicine approaches in cblG would consider mutation type, residual enzyme activity, and individual response to therapies, tailoring doses of hydroxocobalamin, betaine, and folate accordingly. Pharmacogenomics, such as polymorphisms in folate pathway genes or drug-metabolizing enzymes, could influence response to therapy, but specific data are not available. Integrating genetic, biochemical, imaging, and clinical data will be key to optimizing personalized care in cblG.

## 13. Prevention

### 13.1 Primary Prevention

Primary prevention of cblG, in the sense of preventing disease occurrence, is not generally possible because the disorder is caused by inherited biallelic pathogenic MTR variants. However, genetic counseling for at-risk couples (e.g., carriers of MTR pathogenic variants) can inform reproductive choices and potentially reduce incidence through options such as preimplantation genetic diagnosis and prenatal testing.[7][11][16] Public health measures focusing on adequate dietary intake of vitamin B\(_{12}\) and folate are important for preventing nutritional hyperhomocysteinemia but do not prevent cblG. No vaccine or specific prophylactic medication exists to prevent methionine synthase deficiency.

### 13.2 Secondary Prevention: Screening and Early Detection

Secondary prevention in cblG centers on early detection and treatment to prevent or mitigate complications. Newborn screening programs that include measurement of homocysteine or methionine could detect cblG presymptomatically.[7][11] GeneReviews notes that detection by newborn screening depends on C3 and C3/C2 ratio cutoffs and the availability of detection of low methionine, and that cblG often is not identified on newborn screening under current conditions.[7] Kripps et al. argue that cblG warrants inclusion in newborn screening due to improved outcomes from treatment of presymptomatic patients.[11] Implementing newborn screening for remethylation disorders would involve adding assays for homocysteine or low methionine to standard panels, with appropriate cutoffs and confirmatory testing. Once detected, early treatment with hydroxocobalamin and betaine can prevent severe neurologic damage and improve long-term prognosis.[7][9][11][14] Carrier screening in high-risk populations and cascade screening of family members can identify carriers and affected individuals early.

### 13.3 Tertiary Prevention: Complication Management

Tertiary prevention aims to prevent complications in individuals with established cblG. This includes maintaining optimal metabolic control with regular hydroxocobalamin injections, betaine, and folate supplementation, and monitoring homocysteine and methionine levels to adjust therapy.[7][9][11][14] Preventing vascular complications requires attention to cardiovascular risk factors and possibly additional measures in individuals with particularly high homocysteine. Managing neurologic complications involves seizure control, spasticity treatment, and rehabilitation to prevent contractures and functional decline. Regular follow-up with metabolic specialists, neurologists, and hematologists is essential.

### 13.4 Counseling and Public Health Considerations

Genetic counseling is crucial for families affected by cblG, providing information on inheritance, recurrence risk, carrier testing, and reproductive options.[7][11][16] Counselors can explain the autosomal recessive pattern, the 25% recurrence risk per pregnancy when both parents are carriers, and the availability of prenatal and preimplantation testing. Public health interventions for cblG primarily involve awareness and education among clinicians to recognize hyperhomocysteinemia and remethylation defects, and advocacy for newborn screening inclusion. Environmental interventions, such as reducing nitrous oxide exposure in vulnerable patients, may be considered. Prophylactic medications beyond hydroxocobalamin and betaine are not available.

## 14. Other Species and Natural Disease

### 14.1 Cross-Species Considerations and Orthologous Genes

Methionine synthase and its encoding gene MTR have orthologs in diverse species, including rodents, zebrafish, and other vertebrates, reflecting evolutionary conservation of one-carbon metabolism.[16] NCBI Gene lists orthologs of human MTR in model organisms, although specific details are not provided in the snippet.[16] These orthologs perform similar catalytic functions, remethylating homocysteine to methionine. Naturally occurring MTR mutations in animals causing cblG-like phenotypes have not been widely reported in the veterinary literature, and no specific OMIA entry for methionine synthase deficiency is noted in the available data. However, given the conserved role of methionine synthase, it is plausible that such disorders exist in companion animals but are underrecognized. Comparative pathology studies could reveal similar neurologic and hematologic manifestations in animals with MTR mutations.

### 14.2 Zoonotic Potential and Transmission

CblG is a genetic disorder with no infectious component and thus has no zoonotic potential. It is not transmissible between species except via inheritance of genetic variants within a species.

## 15. Model Organisms

### 15.1 Experimental Models of Methionine Synthase Deficiency

Specific, well-characterized model organisms for cblG, such as Mtr knockout mice, are not described in the provided search results. However, experimental disruption of methionine synthase in model organisms has been studied to understand one-carbon metabolism. Complete knockout of Mtr in mice may be embryonic lethal, given the essential role of methionine synthase in methylation and development, though data are not provided here. Conditional or hypomorphic models could recapitulate aspects of cblG, including hyperhomocysteinemia, hypomethioninemia, and neurologic deficits, and could be used to study pathophysiology and test therapies. Cellular models, such as patient-derived fibroblasts or induced pluripotent stem cells carrying MTR mutations, serve as in vitro models of cblG, allowing investigation of methionine synthase activity, homocysteine metabolism, and drug responses.[1][2][5][6] Complementation analysis in fibroblast lines was historically used as an experimental model to define cblE and cblG.[1][5] Overall, model organism data for cblG are limited in the literature reviewed, and future research should develop robust animal and cellular models to advance understanding and treatment.

### 15.2 Applications and Limitations

Model systems for methionine synthase deficiency, once established, would enable detailed study of brain development under hypomethylation, white matter pathology, vascular effects of hyperhomocysteinemia, and response to therapies such as hydroxocobalamin and betaine. Limitations may include species differences in homocysteine metabolism and folate pathways, and difficulties in modeling human cognitive and psychiatric symptoms. Nonetheless, comparative models could provide valuable mechanistic insights.

## Conclusion

Methylcobalamin deficiency type cblG is a rare, autosomal recessive inborn error of cobalamin-dependent one-carbon metabolism caused by biallelic pathogenic variants in the MTR gene encoding methionine synthase.[2][6][7][11][16] The upstream defect—loss-of-function in methionine synthase—results in a selective remethylation block with severe hyperhomocysteinemia, homocystinuria, and hypomethioninemia, while methylmalonic acid levels remain normal, distinguishing cblG from combined cobalamin metabolism disorders.[2][3][7][9][11][15] Clinically, cblG manifests with a broad phenotypic spectrum ranging from infantile-onset encephalopathy, seizures, hypotonia, developmental delay, microcephaly, and megaloblastic anemia to adolescent and adult-onset psychiatric symptoms, cognitive decline, and leukoencephalopathy.[4][7][11][14] At the mechanistic level, chronic methionine and S‑adenosylmethionine deficiency leads to global hypomethylation affecting DNA, proteins, and lipids, with particular impact on myelination and brain function, while homocysteine toxicity contributes to vascular and neuronal injury.[2][7][11][14] The central nervous system and hematopoietic system are the primary anatomical sites of pathology, with oligodendrocytes, neurons, erythroid precursors, and endothelial cells being key affected cell types.[7][11][13][14] 

Diagnosis relies on recognizing the biochemical profile of elevated homocysteine, low methionine, homocystinuria, and normal methylmalonic acid, supported by genetic testing identifying biallelic MTR variants.[2][3][6][7][11][15][16] Neuroimaging, particularly MRI, can reveal leukoencephalopathy in adult-onset cases, while bone marrow examination may show megaloblastic changes.[7][11][14] Differential diagnosis includes CBS deficiency, MTHFR deficiency, and cblC and related cobalamin metabolism disorders, which differ in methionine and methylmalonic acid patterns.[7][9][11] 

Treatment with high-dose parenteral hydroxocobalamin, betaine, folate or folinic acid, and methionine supplementation is effective in improving biochemical abnormalities and often in stabilizing or reversing neurologic and hematologic manifestations, especially when initiated early.[7][9][11][14] Kripps et al. provide compelling evidence that presymptomatic treatment or early therapy leads to better outcomes, advocating for inclusion of cblG in newborn screening.[11] Neurology reports demonstrate the reversibility of adult-onset leukoencephalopathy with hydroxocobalamin therapy.[14] As a monogenic but treatable metabolic disorder, cblG represents a paradigmatic example of how early recognition of inborn errors of metabolism can transform prognosis.

Current challenges include underdiagnosis due to nonspecific symptoms and lack of homocysteine screening, limited epidemiologic data on prevalence and natural history, and incomplete understanding of modifier genes and epigenetic changes. Research priorities encompass development of robust animal and cellular models, detailed omics profiling to delineate molecular signatures, refinement of newborn screening strategies incorporating homocysteine and methionine measurements, and exploration of gene-based therapies targeting MTR. Ontology-based annotation of cblG, including mapping to MONDO, HPO, GO, CL, UBERON, CHEBI, and NCIT terms, enables integration into computational knowledge bases and supports precision medicine and decision support tools. By synthesizing clinical, molecular, biochemical, and mechanistic data, this report provides a comprehensive foundation for further research, improved diagnosis, optimized treatment, and ultimately better outcomes for individuals with methylcobalamin deficiency type cblG.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.