---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-08-27T14:55:30.558067'
end_time: '2026-08-27T15:00:28.924469'
duration_seconds: 298.37
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Charcot-Marie-Tooth disease type 4K (SURF1-related)
  mondo_id: MONDO:0014733
  category: peripheral neuropathy
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
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 6
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Charcot-Marie-Tooth disease type 4K (SURF1-related)
- **MONDO ID:** MONDO:0014733 (if available)
- **Category:** peripheral neuropathy

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth disease type 4K (SURF1-related)** covering all of the
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

# Charcot-Marie-Tooth Disease Type 4K (SURF1-Related): Comprehensive Disease Characteristics and Mechanistic Overview

Charcot-Marie-Tooth disease type 4K (CMT4K), also known as SURF1-related Charcot-Marie-Tooth disease, is a rare autosomal recessive, severe, demyelinating sensorimotor neuropathy that links the classical peripheral neuropathy spectrum of CMT4 to the mitochondrial disease spectrum characterized by cytochrome c oxidase (COX, complex IV) deficiency and lactic acidosis.[1][4][11] Clinically, CMT4K manifests with childhood-onset progressive distal muscle weakness and atrophy of the hands and feet, distal sensory impairment, areflexia, and markedly reduced motor nerve conduction velocities, typically below 25 m/s, together with biochemical evidence of lactic acidosis and isolated complex IV deficiency.[1][4][11][16] The disease is genetically caused by biallelic pathogenic variants in SURF1, a nuclear-encoded assembly factor of mitochondrial complex IV, whose loss of function is also a well-established cause of Leigh syndrome, a subacute, often lethal neurodegenerative encephalopathy of infancy.[3][7][8][17] The recognition of SURF1-related CMT4K in the last decade has expanded the phenotypic spectrum of SURF1 deficiency from central nervous system–predominant Leigh syndrome to a peripheral nerve–predominant demyelinating neuropathy, raising important questions about genotype–phenotype relationships, tissue-specific vulnerability to complex IV defects, and compensatory mitochondrial responses.[4][8][13][14] This report synthesizes current knowledge on CMT4K across disease information, etiology, phenotypes, genetics, environment, mechanism, anatomy, temporal course, inheritance, diagnostics, prognosis, treatment, prevention, comparative biology, and model organisms, integrating human clinical data, mechanistic studies, and animal models to support a structured disease knowledge base.

## 1. Disease Information

### 1.1 Concise Overview and Disease Concept

Charcot-Marie-Tooth disease type 4K is defined as a form of autosomal recessive demyelinating Charcot-Marie-Tooth disease characterized by severe childhood-onset, progressive sensorimotor neuropathy with mitochondrial complex IV deficiency due to SURF1 mutations.[1][4][11][19][20] Orphanet describes SURF1-related CMT4K as a disorder with childhood onset of severe, progressive, demyelinating sensorimotor neuropathy manifesting with distal muscle weakness and atrophy of hands and feet, distal sensory impairment, areflexia, severely reduced motor nerve conduction velocities of 25 m/s or less, and lactic acidosis with mitochondrial complex IV deficiency.[11] OMIM entry 616684 similarly emphasizes that CMT4K is an autosomal recessive demyelinating peripheral neuropathy characterized by onset in the first decade of distal muscle weakness and atrophy associated with impaired distal sensation, often affecting both upper and lower limbs and sometimes accompanied by nystagmus and late-onset cerebellar ataxia; laboratory studies demonstrate increased serum lactate and isolated mitochondrial complex IV deficiency.[1]

The disease belongs to the broader group of autosomal recessive demyelinating CMT (historically termed AR-CMT1), classified as CMT4, which encompasses multiple genetically distinct subtypes with overlapping neuropathic phenotypes but distinct gene defects.[9][15] CMT4K is distinguished within this group by its specific association with SURF1 mutations and the presence of systemic mitochondrial dysfunction, most notably lactic acidosis, and complex IV deficiency, features not typical of most other CMT4 forms.[1][4][11][15] Echaniz-Laguna and colleagues originally identified SURF1 variants in patients with severe childhood-onset demyelinating CMT and lactic acidosis in a consanguineous family, and subsequently in an additional unrelated patient, thus establishing SURF1-associated CMT4 as a distinct entity.[4] Their work led OMIM and Orphanet to recognize CMT4K as the SURF1-related, demyelinating CMT subtype.[1][11][15]

From a disease categorization perspective, CMT4K can be placed at the intersection of peripheral neuropathy and mitochondrial disease. On one hand, it conforms to the classic Charcot-Marie-Tooth pattern of length-dependent, distally accentuated sensorimotor neuropathy with slowly progressive weakness, atrophy, and sensory loss in the extremities, often accompanied by foot deformities and areflexia.[9][10][11] On the other hand, its biochemical and imaging features, including lactic acidosis, isolated complex IV deficiency, and sometimes brain MRI lesions in the basal ganglia and brainstem, align with the mitochondrial encephalomyopathy spectrum typified by SURF1-related Leigh syndrome.[3][4][7][8][17] This dual positioning has significant implications for diagnosis, management, and mechanistic understanding, as it invites careful differentiation from Leigh syndrome while acknowledging shared pathogenic roots in SURF1-mediated COX assembly failure.

### 1.2 Key Identifiers and Classification Codes

CMT4K is well represented across major biomedical ontologies and classification systems. OMIM lists Charcot-Marie-Tooth disease, demyelinating, autosomal recessive, type 4K under phenotype MIM number 616684, with causative gene SURF1 (gene MIM 185620) localized to chromosome 9q34.2.[1][12][15] Orphanet catalogs SURF1-related CMT4K as ORPHA:391351 and classifies it as a rare disorder with prevalence below 1 per 1,000,000.[11] The broader CMT4 group is listed under ORPHA:64749.[9] The Monarch Initiative identifies Charcot-Marie-Tooth disease type 4K with MONDO:0014733, linking it to a demyelinating sensorimotor neuropathy manifesting with distal muscle weakness and atrophy.[5]

Regarding international disease classification, Orphanet reports that SURF1-related CMT4K is coded in ICD-10 as G60.0 (Hereditary motor and sensory neuropathy) and in ICD-11 as 8C20.0 (Hereditary peripheral neuropathy).[11] SNOMED CT codes associated with CMT and related hereditary neuropathies, such as 715796006, are referenced by OMIM for the overarching CMT category, although specific SNOMED identifiers for CMT4K are not consistently distinguished.[15] In terminologies used for genetic testing and clinical decision support, the NCBI Genetic Testing Registry (GTR) indexes CMT4K under condition identifier C4225246, noting SURF1 as the reported causal gene and listing numerous clinical laboratories that offer SURF1 testing as part of CMT or mitochondrial disease panels.[19]

MeSH (Medical Subject Headings) does not typically provide subtype-specific headings for individual CMT forms, but the disease concept maps to broader MeSH headings including "Charcot-Marie-Tooth Disease," "Peripheral Nervous System Diseases," and "Mitochondrial Diseases," reflecting its dual classification. For ontology-based knowledge representation, CMT4K can be associated with MONDO:0014733, HPO terms capturing its phenotypic spectrum, and UBERON terms for the affected anatomical structures, establishing a structured linkage across phenotype, genotype, and anatomy.

### 1.3 Synonyms and Alternative Names

The nomenclature surrounding CMT4K reflects both its historical placement in the CMT classification and its specific genetic etiology. Orphanet lists multiple synonyms for SURF1-related CMT4K, including "CMT4K," "Charcot-Marie-Tooth disease type 4K," "SURF1-related CMT4," and "SURF1-related severe demyelinating Charcot-Marie-Tooth disease."[11] GTR similarly uses the synonyms "CHARCOT-MARIE-TOOTH DISEASE, DEMYELINATING, AUTOSOMAL RECESSIVE, TYPE 4K" and "CHARCOT-MARIE-TOOTH NEUROPATHY, DEMYELINATING, AUTOSOMAL RECESSIVE, TYPE 4K."[19] MalaCards, a curated disease database, describes the entity under "Charcot-Marie-Tooth Disease Type 4K" and emphasizes its characterization as "a subtype of Charcot-Marie-Tooth disease type 4 characterized by childhood onset of a severe, progressive, demyelinating sensorimotor neuropathy."[20]

Historically, CMT4K has been grouped under autosomal recessive demyelinating CMT (AR-CMT1) and sometimes described simply as "SURF1-related CMT4," particularly in early clinical reports.[4][9][15] OMIM initially referenced SURF1-associated demyelinating CMT as "autosomal recessive Charcot-Marie-Tooth disease type 4K" before the term became standard.[1][15] Some authors also highlight the mitochondrial dimension by referring to "CMT4 with SURF1-related complex IV deficiency" to underscore the biochemical abnormality.[4][8] For clarity in knowledge bases, the preferred label is often "Charcot-Marie-Tooth disease type 4K (SURF1-related)," accompanied by the synonym "SURF1-related Charcot-Marie-Tooth disease type 4."

### 1.4 Source Type and Data Aggregation

The information summarized here is derived from aggregated disease-level resources rather than individual electronic health records. OMIM, Orphanet, and Monarch Initiative compile data from published case reports, small clinical series, and molecular genetic studies, including the seminal work by Echaniz-Laguna et al. in Neurology (2013) and additional reports of SURF1 mutations causing Leigh syndrome with peripheral neuropathy.[1][3][4][5][8][11]  

Echaniz-Laguna et al. report:

> "We describe 2 patients from a consanguineous family with demyelinating autosomal recessive CMT disease (CMT4) associated with the homozygous splice site mutation c.107-2A>G in the SURF1 gene, encoding an assembly factor of the mitochondrial respiratory chain complex IV."[4]

This and similar papers are based on small cohorts of deeply phenotyped patients and thus represent high-quality, but limited-scale, human clinical evidence.[3][4][7][8][17] Orphanet’s disease definitions, prevalence estimates, and clinical descriptions derive from systematic expert reviews of such literature.[9][11] OMIM’s clinical synopses likewise aggregate features across reported cases, with an emphasis on genotype-phenotype correlations.[1][2][15]

Because CMT4K is extremely rare, large registries or population-based epidemiologic datasets are lacking, and detailed natural history data are limited. Most available information comes from isolated families identified through genetic studies of CMT or Leigh syndrome, supplemented by mechanistic investigations of SURF1 variants and animal models.[3][4][7][8][13][14][17] Consequently, conclusions about frequency, variability, and prognosis are necessarily based on small numbers and may evolve as more cases are recognized, particularly with increasing use of next-generation sequencing in neuropathy and mitochondrial disease panels.

## 2. Etiology

### 2.1 Primary Causes and Disease Causal Factors

The primary cause of CMT4K is biallelic pathogenic variants in the SURF1 gene, which encodes surfeit locus protein 1, a small hydrophobic protein of the inner mitochondrial membrane that functions as an assembly factor for cytochrome c oxidase (COX; complex IV) of the respiratory chain.[1][4][8][13][14] OMIM explicitly states that autosomal recessive Charcot-Marie-Tooth disease type 4K is caused by homozygous or compound heterozygous mutation in the SURF1 gene on chromosome 9q34.[1] This conclusion is supported by Echaniz-Laguna et al., who identified a homozygous splice-site mutation c.107-2A>G in SURF1 segregating with disease in a consanguineous family with demyelinating CMT4, and by the discovery of additional pathogenic SURF1 variants in an unrelated patient with similar CMT4 phenotype.[4]

The central mechanistic role of SURF1 in COX assembly has long been known from studies in Leigh syndrome, where loss-of-function SURF1 mutations cause isolated complex IV deficiency in multiple tissues.[3][8][13][14] As Lee et al. note:

> "The human surfeit 1 (SURF1) gene encodes a three-hundred amino acid mitochondrial protein necessary for the assembly and maintenance of the COX holoenzyme which is essential for energy production in the human body."[8]

In CMT4K, SURF1 mutations produce a tissue-specific phenotype dominated by demyelinating peripheral neuropathy, which is accompanied by biochemical evidence of complex IV deficiency and lactic acidosis, but without the fulminant encephalopathy and early lethality typical of Leigh syndrome.[1][4][11][8] The mechanistic chain can be conceptualized as germline biallelic SURF1 loss-of-function leading to defective assembly and reduced activity of complex IV in mitochondria, resulting in impaired oxidative phosphorylation, chronic energy shortage, and increased reliance on anaerobic glycolysis. This metabolic derangement yields lactic acidosis and places particular stress on high-energy-demand tissues, notably peripheral nerve and Schwann cells, culminating in demyelinating sensorimotor neuropathy.

No environmental or infectious causes have been implicated in CMT4K. The disease is unequivocally monogenic, with SURF1 variants acting in a Mendelian autosomal recessive manner. However, the same gene can cause a spectrum of phenotypes, from pure Leigh syndrome to peripheral neuropathy–dominant CMT4K, suggesting that variation in residual complex IV activity, tissue-specific compensatory pathways, or coexisting genetic modifiers may influence phenotypic expression.[4][7][8][13][14]

### 2.2 Genetic Risk Factors

In CMT4K, genetic risk factors and causal variants are essentially synonymous, because the disease arises from high-penetrance, pathogenic alleles in SURF1. Echaniz-Laguna et al. identified several SURF1 variants associated with demyelinating CMT4, including the homozygous splice-site mutation c.107-2A>G in intron 2, which abolishes the invariant AG splice acceptor site and produces no normally spliced transcript, leading to complete absence of SURF1 protein.[4] They also reported a compound heterozygous configuration with a missense change c.574C>T (p.Arg192Trp) and a novel deletion c.799_800del, both predicted to severely impair protein function.[4]  

In their Neurology paper, the authors state:

> "The c.107-2A>G mutation produced no normally spliced transcript, leading to SURF1 absence. However, complex IV remained partially functional in muscle and fibroblasts."[4]

This observation suggests that even complete SURF1 absence may allow partial complex IV assembly in some tissues, perhaps via alternative assembly factors or compensatory mechanisms, and that tissue-specific residual COX activity may modulate disease phenotype.

More recently, a 2026 study in Frontiers in Neurology examined five children with clinical Leigh syndrome harboring SURF1 variants and identified six variant sites, including four novel changes: c.314-317delTGCC (p.L105Qfs*7), c.588+1_588+3delGTA (splicing), c.655G>T (p.Glu219), and c.515+3G>C.[7] Reverse transcription-quantitative PCR demonstrated significantly reduced SURF1 mRNA expression in patients compared with their parents, confirming the loss-of-function nature of these variants.[7] Although this cohort presented predominantly with Leigh syndrome rather than CMT4K, it underscores the diversity of pathogenic SURF1 variants, comprising frameshift, splice-site, and missense changes that converge on reduced or absent functional protein.[3][7][8][17]

From a risk-factor perspective, individuals who are heterozygous carriers of pathogenic SURF1 variants are usually clinically unaffected but have an elevated risk of having affected children if their partner is also a carrier, reflecting classic autosomal recessive inheritance.[1][11][19] Consanguinity greatly increases the likelihood that both parents carry the same pathogenic allele, thus raising risk for offspring, as illustrated by the consanguineous family described by Echaniz-Laguna et al.[4] Carrier frequency for SURF1 pathogenic variants is not well quantified at the population level, but given the rarity of reported CMT4K and SURF1-related Leigh syndrome, pathogenic alleles appear to be very uncommon in the general population.[8][11][17] Population databases such as gnomAD typically show extremely low allele frequencies for known pathogenic SURF1 variants, consistent with the disease’s rarity, though explicit figures are not reported in the sources reviewed here.

There is no evidence that common genetic variants or polygenic susceptibility contribute appreciably to CMT4K risk. The disease is driven by rare, high-impact mutations in a single gene, and additional common variants likely play at most a minor role in modulating severity or tissue-specific expression.

### 2.3 Environmental and Lifestyle Risk Factors

Given the clearly monogenic etiology of CMT4K, environmental and lifestyle risk factors are not known to cause the disease in the absence of SURF1 mutations. None of the clinical series or reviews of SURF1-associated CMT or Leigh syndrome implicate toxins, radiation, occupational exposures, infections, or lifestyle behaviors as primary etiologic factors.[3][4][7][8][17] The onset of symptoms in childhood, often in the first decade, in patients with biallelic SURF1 mutations argues strongly for a genetically determined origin, and the presence of biochemical hallmarks such as isolated complex IV deficiency further reinforces this conclusion.[1][4][8][11]

That said, environmental factors may influence disease course and severity in individuals with SURF1 deficiency. For Leigh syndrome, Lee et al. emphasize that patients should avoid anti-epileptic drugs such as valproate, which can exacerbate mitochondrial dysfunction and worsen outcomes.[8] By extension, exposure to medications or toxins that impair mitochondrial respiration—such as some antiretrovirals, chemotherapeutic agents, or environmental pollutants—might aggravate symptoms or speed progression in CMT4K, although direct evidence is lacking. Likewise, severe systemic stressors such as infections, fever, or hypoxia could exacerbate metabolic decompensation in SURF1-deficient individuals, potentially precipitating episodes of worsening neuropathy or encephalopathy.

Lifestyle factors such as diet, physical activity, and alcohol consumption may influence general health and functional status in CMT4K patients, but they are not established risk determinants for disease onset. In the broader CMT population, structured exercise and physiotherapy can improve functional outcomes and delay complications,[18] whereas excessive alcohol or poor nutrition could worsen neuropathic symptoms. However, these influences are non-specific and not unique to CMT4K.

### 2.4 Protective Factors

Explicit protective factors for CMT4K have not been defined in human studies. No genetic variants have been convincingly shown to mitigate disease severity or reduce risk in carriers of pathogenic SURF1 alleles. Likewise, no environmental exposures are known to confer protection against neuropathy in this context. The rarity of CMT4K and the limited number of reported cases make systematic identification of modifiers challenging.

Nonetheless, insights from Surf1 knockout mice suggest that biological compensatory mechanisms may partially protect against severe phenotypes. Agostino et al. reported that constitutive Surf1 knockout in mice causes high embryonic lethality, early post-natal mortality, and profound COX deficiency in skeletal muscle and liver, but with surprisingly little brain involvement.[13] Pulliam et al. later showed that complex IV deficient Surf1^−/− mice exhibit enhanced median lifespan (~20% increase) and robust activation of mitochondrial biogenesis, the Nrf2 antioxidant response, and the mitochondrial unfolded protein response (UPR^MT^).[14] They conclude:

> "Loss of complex IV assembly factor Surf1 in mice results in compensatory responses including mitochondrial biogenesis, the nrf2 pathway and the mitochondrial unfolded protein response. This compensatory response may contribute to the lack of deleterious phenotypes under basal conditions."[14]

These findings imply that intrinsic cellular pathways—such as upregulation of PGC-1α–mediated mitochondrial biogenesis and activation of stress-response programs—can partially counteract complex IV deficiency and reduce phenotypic severity, at least in certain tissues.[14] Whether similar protective responses operate in human SURF1-related CMT4K or Leigh syndrome remains speculative, but they suggest potential therapeutic directions aimed at enhancing mitochondrial resilience.

In clinical practice, optimization of metabolic status through adequate nutrition, avoidance of mitochondrial toxins, and possible use of ketogenic diets or cofactor supplementation may provide modest protective effects against progression, as has been suggested in Leigh syndrome.[8] Yet, evidence for such benefits in CMT4K specifically is lacking, and any protective effect is likely partial and supportive rather than curative.

### 2.5 Gene–Environment Interactions

Specific gene–environment interactions that influence CMT4K risk or phenotype have not been rigorously characterized. The fundamental causal chain in this disease—biallelic SURF1 loss-of-function leading to complex IV deficiency and neuropathy—does not require environmental triggers and is sufficient to produce disease.[1][4][8][11] Unlike multifactorial disorders in which common variants interact with environmental exposures to modulate risk, CMT4K is primarily determined by rare, high-impact Mendelian alleles.

Nevertheless, gene–environment interactions may influence the expression of SURF1-related disease in broader terms. For Leigh syndrome, environmental stressors such as intercurrent infections, fever, or fasting can precipitate metabolic crises and neurologic deterioration, highlighting how environmental stress interacts with underlying mitochondrial vulnerability.[8][17] Anti-epileptic drugs that impair mitochondrial function, notably valproate, can exacerbate disease in SURF1-associated LS, representing a clear gene–drug interaction.[8] It is reasonable to extrapolate that similar interactions could modulate disease course in CMT4K, in which peripheral nerves and muscles are already metabolically stressed by complex IV deficiency.

At a mechanistic level, environmental influences that upregulate mitochondrial biogenesis, enhance antioxidant defenses, or otherwise support oxidative phosphorylation might ameliorate symptoms. Exercise training, for example, can increase mitochondrial content and function in skeletal muscle, and might theoretically enhance tolerance to complex IV defects, though no controlled studies have examined this in CMT4K.[14][18] Conversely, exposures that generate oxidative stress or inhibit respiratory chain function could worsen nerve damage. As of now, these considerations remain theoretical and underscore gaps in knowledge about gene–environment interplay in SURF1-related neuropathy.

## 3. Phenotypes

### 3.1 Core Neuromuscular Phenotypes

The defining phenotypes of CMT4K are those of a severe, demyelinating sensorimotor peripheral neuropathy. Orphanet describes SURF1-related CMT4K as characterized by childhood onset of severe, progressive, demyelinating sensorimotor neuropathy manifesting with distal muscle weakness and atrophy of hands and feet, distal sensory impairment (particularly diminished vibration and pinprick sensation in the lower limbs), areflexia, and severely reduced motor nerve conduction velocities of 25 m/s or less.[11] OMIM echoes this description, noting that CMT4K presents in the first decade with distal muscle weakness and atrophy in upper and lower limbs, along with impaired distal sensation.[1]

Distal muscle weakness, often beginning in the ankles and feet and later involving the hands, corresponds to HPO term *Distal muscle weakness* (HP:0003551). Muscle atrophy in these regions can be annotated as *Muscle wasting* (HP:0003202), while the associated foot deformities, such as pes cavus or hammer toes, frequently observed in CMT, map to HPO terms like *Pes cavus* (HP:0001761).[9][10][11] Sensory loss, particularly for vibration and pain, can be captured with *Reduced vibration sense* (HP:0002521) and *Hypesthesia* (HP:0006903). Areflexia, especially in the Achilles and patellar reflexes, corresponds to *Absent tendon reflexes* (HP:0001284).

Electrophysiologically, CMT4K is a demyelinating neuropathy, with motor nerve conduction velocities below 25 m/s, often markedly reduced compared with normal values, consistent with HPO term *Reduced motor nerve conduction velocity* (HP:0003431).[4][11][16] Echaniz-Laguna et al. emphasize that all three patients with SURF1-associated CMT4 had severe childhood-onset neuropathy, motor nerve conduction velocities under 25 m/s, and lactic acidosis.[4][16] Such values firmly place CMT4K in the demyelinating CMT category rather than the axonal CMT2 forms, which typically retain higher conduction velocities with reduced amplitudes.[10][15]

The severity of neuropathy is generally high. Orphanet characterizes CMT4 as more severe than other CMT forms, with earlier onset and higher likelihood of disability, and notes that CMT4K is a severe subtype within this group.[9][11] Patients often exhibit progressive gait difficulties, frequent falls, and hand dysfunction limiting fine motor tasks, reflecting a substantial impact on activities of daily living. The neuropathy usually progresses over years, causing increasing distal weakness and atrophy, though systematic staging systems for CMT4K specifically have not been established.

### 3.2 Mitochondrial and Systemic Phenotypes

Beyond neuropathy, CMT4K is distinguished by systemic mitochondrial features. Lactic acidosis is a prominent laboratory abnormality, reflecting impaired oxidative phosphorylation and increased reliance on anaerobic glycolysis. Orphanet explicitly includes lactic acidosis with mitochondrial complex IV deficiency as part of SURF1-related CMT4K.[11] Echaniz-Laguna et al. likewise report lactic acidosis in all three patients with SURF1-associated CMT4.[4][16] This phenotype corresponds to HPO term *Lactic acidosis* (HP:0003128) and *Elevated serum lactate* (HP:0002151).

Complex IV deficiency, specifically isolated cytochrome c oxidase deficiency, is another core biochemical phenotype. OMIM notes that laboratory studies in CMT4K show increased serum lactate and isolated mitochondrial complex IV deficiency.[1] Lee et al. describe SURF1 as an assembly factor essential for COX stability, and report that SURF1 mutations cause Leigh syndrome with predominantly complex IV deficiency.[8] In the context of CMT4K, complex IV deficiency is typically demonstrated in muscle or fibroblast biopsies using enzyme assays or histochemical COX staining.[1][4][8] HPO term *Cytochrome c oxidase deficiency* (HP:0002850) can be used to annotate this abnormality.

In some patients, particularly those overlapping with Leigh syndrome phenotypes, brain MRI abnormalities are observed, including putaminal and periaqueductal lesions. Orphanet lists brain MRI abnormalities in SURF1-related CMT4K, specifically putaminal and periaqueductal lesions.[11] Echaniz-Laguna et al. report that two patients with SURF1-associated CMT4 had brain MRI abnormalities and later developed cerebellar ataxia years after polyneuropathy.[4] These imaging findings are typical of Leigh syndrome and correspond to HPO terms such as *Basal ganglia abnormality* (HP:0002134) and *Abnormality of the periaqueductal gray* (HP:0007090), though the latter is less commonly used.

### 3.3 Additional Neurological Phenotypes

CMT4K can be associated with additional neurological features beyond peripheral neuropathy. Orphanet notes that patients may present kyphoscoliosis, nystagmus, hearing loss, cerebellar ataxia, and/or brain MRI abnormalities.[11] Kyphoscoliosis—combined kyphosis and scoliosis—is a common complication in severe CMT and corresponds to HPO term *Kyphoscoliosis* (HP:0002933). Nystagmus, involuntary rhythmic eye movements, maps to *Nystagmus* (HP:0000639). Hearing loss, which may be sensorineural, corresponds to *Hearing impairment* (HP:0000365). Cerebellar ataxia, reflecting involvement of cerebellar circuits and manifesting as gait ataxia, dysmetria, and dysarthria in some cases, aligns with *Cerebellar ataxia* (HP:0001251).[11]

These features are not universally present; rather, they occur variably and tend to appear later in the disease course, often years after onset of neuropathy.[1][4][11] Echaniz-Laguna et al. describe patients who developed cerebellar ataxia years after the onset of polyneuropathy, suggesting a progressive extension of pathology from peripheral nerves to central structures.[4] Similarly, Lee et al. note that SURF1-associated Leigh syndrome can present with peripheral neuropathy and myelination defects in nerve biopsies, highlighting that SURF1 deficiency affects both central and peripheral nervous systems.[8] In CMT4K, the emphasis is on peripheral demyelination, but the overlapping features remind clinicians to consider brain imaging and audiologic assessment when evaluating patients.

### 3.4 Age of Onset, Severity, Progression, and Frequency

The age of onset in CMT4K is consistently reported as childhood. OMIM states that CMT4K is characterized by onset in the first decade.[1] Orphanet specifies childhood onset for SURF1-related CMT4K, and the broader CMT4 group is described as having onset in infancy or childhood.[9][11] Echaniz-Laguna’s patients developed symptoms in early childhood, including gait difficulties and distal weakness.[4] Thus, CMT4K should be classified as a pediatric-onset, insidious, chronic disorder, with symptoms emerging gradually rather than acutely.

Symptom severity is generally high. Orphanet describes CMT4 as usually more severe than other CMT types, with earlier onset and more pronounced disability.[9] SURF1-related CMT4K is characterized as severe and progressive.[11][20] Motor nerve conduction velocities below 25 m/s indicate substantial demyelination, and the combination of distal weakness, atrophy, and sensory loss often leads to significant functional impairment by adolescence or early adulthood.[4][11][16] Patients frequently require orthotic support or assistive devices for ambulation and may develop hand dysfunction that limits self-care and employment, underscoring the high impact on quality of life.

The disease course is progressive and chronic lifelong. In contrast to Leigh syndrome, which often leads to death before age ten,[8] CMT4K typically allows survival into adulthood, albeit with cumulative disability. Orphanet notes that CMT in general is a slowly progressive neuropathy that causes eventual disability but does not usually reduce life expectancy, except in some early-onset CMT4 forms with severe respiratory complications.[9] CMT4K, while severe, does not appear to be associated with early mortality in the limited reported cases, though long-term data are sparse.[1][4][11] Progression is gradual, with distal weakness and atrophy worsening over years; cerebellar ataxia and kyphoscoliosis may appear later, reflecting disease extension.[4][11]

In terms of frequency among affected individuals, specific phenotypic frequencies are difficult to quantify due to the very small number of reported CMT4K cases worldwide. Orphanet estimates the prevalence of SURF1-related CMT4K as less than one per million, reflecting extreme rarity.[11] Within CMT4 cohorts, Echaniz-Laguna et al. found SURF1 mutations in 2 of 41 families (5%) presenting with CMT4 after exclusion of known CMT4 genes.[4] This suggests that among genetically unresolved severe autosomal recessive demyelinating neuropathies, SURF1-related CMT4K may account for a few percent of cases, though confirmation in larger cohorts is needed.

### 3.5 Quality of Life Impact

The impact of CMT4K on quality of life is substantial, as is typical for severe demyelinating CMT. The combination of progressive distal weakness, muscle atrophy, sensory loss, and deformities leads to significant limitations in mobility, dexterity, and independence. Patients may struggle with walking, climbing stairs, balance, and fine hand tasks such as writing or buttoning clothes. Orthopedic complications such as foot deformities and kyphoscoliosis can cause pain, fatigue, and additional functional restrictions.[9][11][18]

Rehabilitation studies in the broader CMT population, while not specific to CMT4K, underscore the functional impact and potential benefits of physiotherapy. Corrado et al. highlight that CMT causes significant muscular deficits, restricts daily activities, and involves severe disability, and find that strength or endurance training improves functionality and activities of daily living.[18] They note:

> "The Charcot–Marie–Tooth disease (CMT) causes significant muscular deficits in the affected patients, restricts daily activities (ADL), and involves a severe disability. Although the conservative intervention is the only treatment for the disease, there is no scientific evidence so far on rehabilitation treatment."[18]

These statements apply to CMT4K, where no disease-modifying therapy exists and supportive measures are central to preserving function. Patients may experience psychological distress, social isolation, and reduced participation in work or education due to physical limitations.

Quality-of-life instruments such as EQ-5D, SF-36, and disease-specific tools for neuropathy could be used to quantify the impact of CMT4K, though no published studies have focused on this subtype. Based on clinical descriptions, affected individuals would likely report impairments in mobility, self-care, usual activities, and pain/discomfort dimensions, with variable effects on anxiety/depression. Early recognition and comprehensive rehabilitation are crucial for mitigating these impacts.

### 3.6 Suggested HPO Phenotype Terms

To structure phenotypic information in a disease knowledge base, the following HPO terms aptly capture CMT4K features, embedded here in narrative form rather than as a list. Distal muscle weakness (HP:0003551) and muscle wasting (HP:0003202) describe the core motor phenotype. Reduced vibration sense (HP:0002521) and hypesthesia (HP:0006903) represent distal sensory impairment. Absent tendon reflexes (HP:0001284) correspond to areflexia. Reduced motor nerve conduction velocity (HP:0003431) captures the demyelinating electrophysiology. Lactic acidosis (HP:0003128) and elevated serum lactate (HP:0002151) represent metabolic abnormalities. Cytochrome c oxidase deficiency (HP:0002850) encodes the biochemical defect. Kyphoscoliosis (HP:0002933), nystagmus (HP:0000639), hearing impairment (HP:0000365), and cerebellar ataxia (HP:0001251) reflect additional neurologic and orthopedic features. Basal ganglia abnormalities (HP:0002134) and abnormal MRI signal in the brainstem (HP:0002487) can represent the putaminal and periaqueductal lesions described in some patients.[4][8][11]

## 4. Genetic and Molecular Information

### 4.1 Causal Gene and Gene Annotation

The causal gene for CMT4K is SURF1, surfeit locus protein 1, a nuclear gene encoding a mitochondrial inner membrane protein required for proper assembly of complex IV (cytochrome c oxidase) of the respiratory chain.[1][4][8][13][14] OMIM identifies SURF1 under gene MIM 185620, located at chromosome 9q34.2, and associates biallelic SURF1 mutations with both Leigh syndrome and CMT4K.[1] Orphanet and GTR confirm SURF1 as the defining gene in SURF1-related CMT4K.[11][19]

SURF1 is a small hydrophobic protein of approximately 300 amino acids, localized to the mitochondrial inner membrane, with a role in assembling the 13 subunits of the COX holoenzyme.[14] Pulliam et al. emphasize:

> "Surfeit locus protein 1 (Surf1) is a nuclear encoded small hydrophobic protein localized to the mitochondrial inner membrane that aides in the initial assembly of 13 subunits of the cytochrome c oxidase (COX, Complex IV) holoenzyme."[14]

Functionally, SURF1 participates in the stabilization and incorporation of COX subunits into functional complexes, and its loss of function leads to reduced complex IV content and activity, often with minimal impact on other electron transport chain complexes.[13][14] Gene Ontology (GO) terms that describe SURF1’s role include *mitochondrial inner membrane* (GO:0005743) and *cytochrome c oxidase assembly* (GO:0008535), while *oxidative phosphorylation* (GO:0006119) captures the broader process affected.

### 4.2 Pathogenic Variant Types and Functional Consequences

Pathogenic SURF1 variants in CMT4K and Leigh syndrome encompass a range of types, including splice-site mutations, nonsense variants, frameshift deletions, and missense changes, most of which are predicted or demonstrated to cause loss of function. In the CMT4K cohort studied by Echaniz-Laguna et al., the key variants included a homozygous splice-site mutation c.107-2A>G in intron 2, abolishing the canonical AG acceptor site, and a compound heterozygous configuration comprising a missense variant c.574C>T (p.Arg192Trp) and a novel frameshift deletion c.799_800del.[4] The splice-site change resulted in complete absence of normally spliced SURF1 transcripts, and Western blot analysis showed absence of SURF1 protein.[4]

The authors report:

> "The c.107-2A>G mutation produced no normally spliced transcript, leading to SURF1 absence. However, complex IV remained partially functional in muscle and fibroblasts."[4]

This observation underscores that SURF1 loss of function can greatly reduce complex IV assembly and activity, but residual function may persist via alternative assembly pathways in some tissues. The missense variant p.Arg192Trp affects a conserved arginine residue and has been previously implicated in Leigh syndrome, whereas the c.799_800del frameshift likely introduces a premature stop codon and leads to truncated, unstable protein.[4][8]

In the 2026 Frontiers in Neurology study of SURF1-related Leigh syndrome, CW and colleagues identified six SURF1 variants across five patients, including four novel changes: c.314-317delTGCC (p.L105Qfs*7), c.588+1_588+3delGTA (splicing), c.655G>T (p.Glu219), and c.515+3G>C.[7] They used RT-qPCR to show significantly lower SURF1 mRNA expression in patients compared with parents, confirming that these variants reduce transcript stability or splicing efficiency.[7] The variants comprised both frameshift and splice-site changes, again consistent with a loss-of-function mechanism. Similar variant spectra have been reported in other SURF1-related Leigh syndrome cohorts, such as the Turkish series analyzed by Kose et al., who note that pathogenic SURF1 variants are common causes of Leigh syndrome and typically result in isolated complex IV deficiency.[17]

From the standpoint of ACMG/AMP variant classification, these SURF1 mutations are considered pathogenic or likely pathogenic, based on their absence from general population databases, segregation with disease, predicted or demonstrated loss of function, and functional evidence of reduced SURF1 protein and COX activity.[3][4][7][8][17] Most are germline variants inherited in an autosomal recessive fashion; somatic SURF1 mutations have not been implicated in CMT4K.

Allele frequencies in population databases such as gnomAD are extremely low for known pathogenic SURF1 variants, consistent with disease rarity. While explicit frequencies are not provided in the reviewed sources, the near-absence of these variants in large populations, combined with their strong functional impact, supports their classification as rare, high-penetrance alleles.

Functionally, SURF1 variants act through loss of function, leading to reduced or absent assembly of complex IV and consequent reduction in COX activity. There is no evidence of gain-of-function, dominant negative, or toxic effects. Modifier effects may arise from differences in residual enzyme activity, tissue-specific expression, or compensatory pathways, but these are secondary phenomena rather than primary variant mechanisms.[4][14]

### 4.3 Modifier Genes and Genetic Modulation

Modifier genes that influence CMT4K severity or phenotype have not been clearly identified. However, the phenotypic heterogeneity of SURF1 deficiency—ranging from classic Leigh syndrome to peripheral neuropathy–dominant CMT4K and milder atypical courses—suggests that genetic background can influence expression.[3][4][7][8][17] Lee et al. explicitly state that no clear genotype–phenotype correlation has been found for SURF1 mutations, and that the same genotype can present with different MRI images and clinical courses.[8]  

They remark:

> "SURF1 mutations present as typical or atypical LS, indicating disease involved in different brain tissues. The same genotype can present with different MRI images in patients. No clear phenotype or genotype was found for SURF1 mutations."[8]

This lack of straightforward correlation implies that other genetic factors—either within mitochondrial pathways or more broadly—may modulate tissue-specific vulnerability, compensatory responses, or threshold effects. Candidate modifier genes might include those involved in mitochondrial biogenesis (e.g., PGC-1α), antioxidant defense (e.g., Nrf2 pathway), or other respiratory chain assembly factors. Pulliam et al.’s findings in Surf1^−/− mice, showing upregulation of PGC-1α and other mitochondrial markers, point to functional networks that could influence phenotype.[14]

In CMT4K specifically, the presence or absence of central nervous system manifestations such as cerebellar ataxia or Leigh-type MRI lesions might be influenced by modifier genes, but no systematic analyses exist. Larger cohorts and genome-wide approaches would be needed to identify modifiers. Until then, modifier gene information for CMT4K remains speculative.

### 4.4 Epigenetic Information and Chromosomal Abnormalities

No epigenetic alterations—such as DNA methylation changes, histone modifications, or chromatin remodeling—have been implicated as primary drivers of CMT4K. SURF1-related disease is caused by coding and splice-site variants that directly impair protein function.[3][4][7][8][17] Epigenetic profiling has not been reported for SURF1-deficient peripheral nerve or muscle. It is plausible that cellular stress and metabolic changes could induce secondary epigenetic responses, but these have not been characterized.

Similarly, large-scale chromosomal abnormalities such as aneuploidy, translocations, or inversions are not associated with CMT4K. OMIM, Orphanet, and clinical reports describe disease in the context of normal karyotypes except for the point mutations, small insertions/deletions, and splice-site variants in SURF1.[1][4][11][15] Chromosomal microarray is not part of the routine diagnostic strategy unless additional congenital anomalies suggest a broader genomic disorder.

### 4.5 Molecular Profiling: Transcriptomics, Proteomics, and Metabolomics

Molecular profiling of SURF1-related disease has focused mainly on targeted assays rather than high-throughput omics. RT-qPCR analyses in the 2026 Frontiers cohort demonstrated reduced SURF1 mRNA expression in patients, confirming the deleterious impact of variants on transcript levels.[7] Western blot and enzyme assays in earlier studies have shown decreased SURF1 protein and reduced complex IV activity, with relatively preserved activity of other respiratory chain complexes.[4][13][14] These targeted proteomic and enzymatic analyses establish that SURF1 deficiency leads to isolated complex IV deficiency at the protein and functional level.

Pulliam et al. extended molecular profiling in Surf1^−/− mice to assess markers of mitochondrial biogenesis and stress responses, showing increased levels of PGC-1α and voltage-dependent anion channel (VDAC), indicating enhanced mitochondrial content, and differential activation of the mitochondrial unfolded protein response in skeletal muscle and Nrf2 antioxidant pathway in heart.[14] While not full proteomic or transcriptomic profiling, these assays provide an initial view of altered gene expression patterns in response to complex IV deficiency.

Metabolically, lactic acidosis and altered lactate/pyruvate ratios are key signatures of SURF1-related disease, including CMT4K.[1][4][8][11] Elevated lactate reflects increased glycolytic flux and impaired oxidative phosphorylation, while pyruvate levels and ratios provide clues about the site of respiratory chain dysfunction. Lee et al. summarize that patients with SURF1-associated Leigh syndrome often have elevated lactate levels in blood and CSF, although specific metabolomic profiling beyond these markers is scarce.[8] In CMT4K, lactic acidosis is documented, but comprehensive metabolomics has not been performed.[4][11]

To represent these molecular phenotypes in ontologies, GO terms such as *oxidative phosphorylation* (GO:0006119), *mitochondrial respiratory chain complex IV* (GO:0005751), and *response to oxidative stress* (GO:0006979) can be used, while metabolite-level abnormalities can be annotated with CHEBI terms for lactate (CHEBI:28358) and pyruvate (CHEBI:15361).

## 5. Environmental Information

### 5.1 Non-Genetic Contributing Factors

In the strict etiologic sense, non-genetic environmental factors do not cause CMT4K. The disease is a monogenic, autosomal recessive neuropathy driven by SURF1 loss-of-function. None of the core resources—OMIM, Orphanet, or major clinical series—identify environmental toxins, radiation, pollution, or occupational exposures as primary etiologic agents.[1][4][8][11][17] The pathophysiology hinges on intrinsic mitochondrial dysfunction resulting from genetic defects.

However, as with other mitochondrial disorders, environmental factors can influence disease expression and severity. Lee et al. note that mitochondrial disease management is largely supportive and that treatment outcomes for SURF1-associated Leigh syndrome are unsatisfactory, in part because patients are vulnerable to metabolic stressors.[8] They highlight that anti-epileptic drugs such as valproate, which cause mitochondrial dysfunction, should be avoided in patients with SURF1-associated LS presenting with seizures.[8] This example illustrates how environmental exposures (medications) can exacerbate disease in genetically susceptible individuals.

Likewise, severe infections, fever, or hypoxic stress can worsen mitochondrial function and precipitate clinical deterioration in SURF1-deficient patients. For CMT4K, episodes of acute worsening of neuropathy might be triggered by such stressors, though specific case descriptions are sparse. In the absence of robust data, clinicians generally advise minimizing exposure to mitochondrial toxins and managing systemic illnesses promptly, in line with broader mitochondrial disease care principles.

### 5.2 Lifestyle Factors

Lifestyle factors have not been implicated in causing CMT4K, but they can influence the functional status and quality of life of patients. Physical activity and physiotherapy are particularly relevant. Corrado et al. review rehabilitation in CMT and conclude that strength or endurance training improves functionality and activities of daily living, endorsing physiotherapy as a useful tool to manage CMT.[18] They report that individual training programs contributed to improved muscle strength in both upper and lower limbs across trials.[18] These findings support structured exercise and rehabilitation as beneficial lifestyle interventions for CMT4K patients, helping to maintain mobility and delay complications.

Dietary patterns may also affect metabolic resilience in SURF1-related disorders. In Leigh syndrome, ketogenic diets and coenzyme Q or cofactor supplementation are commonly used and have shown variable efficacy.[8] A ketogenic diet, by providing ketone bodies as alternative fuel for the brain and muscle, may reduce reliance on impaired oxidative phosphorylation pathways and improve energy balance, though data in CMT4K specifically are lacking.[8] Still, diet-based interventions can be considered as adjuncts in comprehensive care.

Alcohol consumption, smoking, and other lifestyle factors that adversely impact overall health could exacerbate neuropathic symptoms or complicate management, but they are not disease-specific risk factors. Patients with severe neuropathy may adopt more sedentary lifestyles because of functional limitations, which can lead to deconditioning and secondary morbidity. Encouraging appropriate, safe physical activity and addressing lifestyle-related comorbidities is therefore part of holistic management rather than primary prevention.

### 5.3 Infectious Agents

No infectious agents have been implicated in the cause or triggering of CMT4K. The disease is not known to be infectious, transmissible, or associated with particular pathogens. While intercurrent infections can stress mitochondria and precipitate decompensation in Leigh syndrome, they do so as nonspecific triggers rather than etiologic factors.[8][17] There is no evidence that specific bacteria, viruses, or parasites cause SURF1 mutations or directly induce CMT4K-like neuropathy.

## 6. Mechanism and Pathophysiology

### 6.1 Molecular Pathways: Oxidative Phosphorylation and Complex IV Assembly

The central molecular pathway in CMT4K is mitochondrial oxidative phosphorylation, particularly the assembly and function of complex IV (cytochrome c oxidase). SURF1 encodes an assembly factor essential for COX holoenzyme formation, and its deficiency leads to decreased complex IV content and activity.[8][13][14] Pulliam et al. describe complex IV as the terminal enzyme of the electron transport chain, facilitating the transfer of electrons from cytochrome c to molecular oxygen to form water, thereby contributing to the proton gradient used for ATP synthesis.[14]  

They state:

> "Complex IV facilitates the final transfer of electrons in the electron transport chain (ETC) from cytochrome c to molecular oxygen forming water and thus plays a key role in mitochondrial oxidative phosphorylation."[14]

GO terms such as *mitochondrial respiratory chain complex IV* (GO:0005751) and *oxidative phosphorylation* (GO:0006119) encapsulate this pathway. SURF1’s role in *cytochrome c oxidase assembly* (GO:0008535) is critical; loss-of-function mutations disrupt assembly, leading to isolated COX deficiency while leaving other respiratory chain complexes relatively intact.[13][14]

In SURF1-deficient human patients, including those with CMT4K, muscle and fibroblast homogenates show reduced COX activity, often around 15–30% of normal, with preserved activity of complexes I–III.[3][4][8] Santoro et al. reported a five-year-old boy with Leigh syndrome and peripheral neuropathy whose muscle biopsy showed decreased COX stain and biochemical analyses revealed cytochrome c oxidase deficiency with 15% residual activity.[3] Echaniz-Laguna et al. found that complex IV remained partially functional in muscle and fibroblasts of CMT4K patients despite complete absence of SURF1 protein, suggesting alternative assembly routes or incomplete dependence on SURF1 in certain tissues.[4]

Pathway-wise, defective COX assembly leads to impaired electron transfer to oxygen, reduced proton pumping, diminished ATP synthesis, and increased leakage of electrons that can generate reactive oxygen species (ROS). Cells respond by increasing glycolytic flux to maintain ATP production, resulting in elevated lactate and metabolic acidosis.[8] Over time, chronic energy deficiency and oxidative stress damage high-demand tissues, notably peripheral nerves, muscle, and, in Leigh syndrome, brain regions with high metabolic needs such as basal ganglia and brainstem.

### 6.2 Cellular Processes: Energy Failure, Demyelination, and Stress Responses

At the cellular level, SURF1 deficiency activates multiple processes relevant to CMT4K pathophysiology, including energy failure, demyelination, and stress response pathways. Peripheral nerves, especially long axons supplying distal extremities, are highly energy-dependent, requiring continuous ATP to maintain ion gradients, synaptic transmission, and axonal transport. Schwann cells, which myelinate peripheral axons, also rely on oxidative phosphorylation to support myelin synthesis and maintenance. In CMT4K, complex IV deficiency in these cell types impairs energy production, leading to functional failure and structural demyelination.

Echaniz-Laguna et al. and Santoro et al. provide histopathologic evidence of demyelinating neuropathy in SURF1-deficient patients. Santoro’s Leigh syndrome case with peripheral neuropathy showed ultrastructural nerve biopsy findings of a defect in myelination.[3] Lee et al. note that patients with SURF1-associated LS can have nerve biopsies revealing myelination defects and peripheral neuropathy.[8] These findings support a causal chain in which SURF1 loss-of-function leads to COX deficiency, energy failure in Schwann cells and axons, and consequent demyelination and axonal dysfunction.

Cellular processes involved include *myelination* (GO:0042552), *axon maintenance* (GO:0007411), and *response to oxidative stress* (GO:0006979). Mitochondrial stress triggers compensatory responses such as mitochondrial biogenesis, unfolded protein responses, and antioxidant pathways. In Surf1^−/− mice, Pulliam et al. found increased markers of mitochondrial biogenesis, including PGC-1α and VDAC, as well as upregulation of the mitochondrial unfolded protein response in skeletal muscle and induction of the Nrf2 antioxidant response pathway in heart.[14] These processes help mitigate energy deficits and reduce ROS damage, contributing to surprisingly mild phenotypes under basal conditions.

Cell types involved in CMT4K include Schwann cells (CL:0000219), peripheral sensory and motor neurons (CL:0000100 and CL:0000102), skeletal muscle fibers (CL:0002385), and, in cases with central involvement, neurons of the basal ganglia and brainstem (CL:0000679). The mitochondrial compartment (GO:0005739) and mitochondrial inner membrane (GO:0005743) are central subcellular structures affected by SURF1 deficiency.

### 6.3 Protein Dysfunction: Loss of SURF1 and COX Defects

Protein dysfunction in CMT4K centers on SURF1 and, downstream, on COX subunits. SURF1 loss-of-function, due to nonsense, frameshift, or splice-site variants, results in reduced or absent protein in mitochondria, disrupting the assembly process of complex IV.[4][7][8][13][14] This leads to misassembly or instability of COX subunits, lowering the amount of functional enzyme complexes in the inner membrane and reducing the electron transport chain’s capacity.

UniProt and structural databases treat SURF1 as a small multi-pass membrane protein, but detailed structural analyses are limited. Functional studies, however, demonstrate that its absence leads to an isolated reduction in complex IV activity without affecting other complexes—an unusual pattern compared with primary mutations in COX subunits, which can sometimes have broader effects.[13][14] This specificity underscores SURF1’s role as an assembly factor rather than a core catalytic subunit.

The downstream effect on COX can be represented by decreased activity of heme a3 and copper centers that facilitate electron transfer. Without adequate COX, electrons accumulate upstream, causing increased reduction of cytochrome c and potential backward pressure on complexes III and I, with increased ROS production. These processes contribute to oxidative damage of lipids, proteins, and DNA in affected cells, compounding the primary energy deficit.

### 6.4 Metabolic Changes: Lactic Acidosis and Energy Shifts

Metabolically, SURF1-related CMT4K exhibits lactic acidosis and altered lactate/pyruvate balance, as noted in clinical descriptions.[1][4][8][11] Reduced oxidative phosphorylation capacity forces cells to rely more heavily on glycolysis for ATP production. Pyruvate generated by glycolysis is normally transported into mitochondria and oxidized by pyruvate dehydrogenase, feeding into the tricarboxylic acid cycle and electron transport chain. In complex IV deficiency, electron flow and ATP synthesis are impaired, leading to accumulation of NADH and feedback inhibition of glycolysis and pyruvate oxidation. Cells adapt by converting pyruvate to lactate via lactate dehydrogenase, regenerating NAD+ and allowing continued glycolytic ATP production, at the cost of lactic acid accumulation.[8]

Clinically, this manifests as elevated serum and sometimes CSF lactate, with symptoms such as fatigue, muscle pain, and, in severe cases, metabolic acidosis. HPO terms *Lactic acidosis* (HP:0003128) and *Elevated serum lactate* (HP:0002151) encode this metabolic shift. In Leigh syndrome, lactic acidosis can be profound and episodic, correlating with disease exacerbations.[8][17] In CMT4K, lactic acidosis appears chronic but may fluctuate with stressors.

Other metabolic changes may include elevated ketone bodies in patients treated with ketogenic diets, as well as alterations in amino acid and lipid metabolism secondary to mitochondrial dysfunction, but these have not been systematically profiled. HMDB and metabolomics resources could, in future, characterize broader metabolic signatures.

### 6.5 Immune System and Tissue Damage Mechanisms

The immune system does not appear to play a primary pathogenic role in CMT4K. There is no evidence of autoimmunity, immunodeficiency, or chronic inflammation as causal drivers. However, mitochondrial dysfunction can modulate innate immune responses, and chronic oxidative stress may promote low-level inflammation in affected tissues. These processes could contribute to tissue damage, fibrosis, and secondary changes over time, particularly in muscle and peripheral nerve, though direct evidence in SURF1-related CMT4K is lacking.

Tissue damage mechanisms in CMT4K are dominated by energy failure, oxidative stress, and structural demyelination. Schwann cells and axons suffer from ATP shortage and ROS damage, leading to myelin breakdown, axonal degeneration, and eventual loss of nerve fibers. Muscle fibers atrophy in response to denervation and reduced activity, while kyphoscoliosis develops due to chronic imbalance in paraspinal musculature and skeletal growth under neuropathic conditions.[9][11][18] Necrosis is not a prominent feature; instead, chronic degenerative changes predominate.

### 6.6 Epigenetic Changes and Advanced Molecular Technologies

Epigenetic changes in SURF1-related disease have not been characterized, and advanced technologies such as single-cell analysis, spatial transcriptomics, and multi-omics integration have not yet been applied to CMT4K in published studies. However, the disease provides an attractive model for such investigations, as it involves distinct tissue vulnerabilities and compensatory mechanisms that might be elucidated by cell-type–specific profiling.

For example, single-cell RNA sequencing of peripheral nerve could reveal differential expression of mitochondrial stress-response genes in Schwann cells versus axons, while spatial transcriptomics could map metabolic adaptations in regions of demyelination. Multi-omics integration combining genomics, transcriptomics, proteomics, and metabolomics could elucidate pathways that determine whether SURF1 deficiency manifests as Leigh syndrome, CMT4K, or intermediate phenotypes.

Until such data are available, mechanistic understanding relies on targeted assays and animal studies, as described above.

### 6.7 Causal Chain from Initial Trigger to Clinical Manifestation

Synthesizing the mechanistic data, the causal chain in CMT4K can be described as follows. The initial trigger is a germline biallelic pathogenic variant in SURF1, inherited in an autosomal recessive pattern.[1][4][11] This variant leads to loss of functional SURF1 protein in mitochondria, disrupting the assembly of complex IV.[4][7][8][13][14] As a result, COX content and activity are reduced, causing isolated complex IV deficiency in the respiratory chain.[3][4][8][13][14] This defect impairs oxidative phosphorylation, reducing ATP production and increasing electron leakage and ROS generation.[8][14]

Cells respond by upregulating glycolysis, leading to increased lactate production and lactic acidosis.[1][4][8][11] High-energy-demand tissues, especially peripheral nerves and Schwann cells, are particularly vulnerable. Energy failure in these cells compromises ion homeostasis, axonal transport, and myelin maintenance, resulting in demyelinating neuropathy characterized by reduced conduction velocities and loss of distal function.[3][4][8][11][16] Chronic neuropathy leads to muscle atrophy, foot and hand deformities, kyphoscoliosis, and progressive weakness.[9][11][18] In some patients, central nervous system regions such as the basal ganglia and brainstem also suffer, producing Leigh-type MRI lesions and cerebellar ataxia.[4][8][17] Compensatory mechanisms, including mitochondrial biogenesis, UPR^MT^, and antioxidant pathways, may partially mitigate damage in certain tissues, influencing phenotypic variability.[14]

Upstream mechanisms in this chain include the genetic defect and disrupted COX assembly; downstream mechanisms include energy failure, ROS damage, demyelination, and structural degeneration. Biological processes involved span oxidative phosphorylation, myelination, axon maintenance, response to oxidative stress, and mitochondrial biogenesis (GO:0006119, GO:0042552, GO:0007411, GO:0006979, GO:0009887). Cell types include Schwann cells, motor and sensory neurons, skeletal muscle fibers, and, where central involvement exists, neurons of the basal ganglia and cerebellum (CL:0000219, CL:0000100, CL:0000102, CL:0002385, CL:0000679). Anatomical structures affected include peripheral nerves of the lower and upper limbs (UBERON:0001021 for sciatic nerve), skeletal muscle (UBERON:0001134), spine (UBERON:0001132), cerebellum (UBERON:0002037), and basal ganglia (UBERON:0006101).

## 7. Anatomical Structures Affected

### 7.1 Organ-Level Involvement

CMT4K primarily affects components of the nervous system, particularly the peripheral nervous system, and secondarily impacts musculoskeletal structures. The peripheral nerves of the lower and upper limbs, including the sciatic and peroneal nerves in the legs and median and ulnar nerves in the arms, are the main sites of demyelinating neuropathy.[9][10][11][4] These nerves belong to the peripheral nervous system (UBERON:0000010) and are critical for motor and sensory function in distal extremities.

Muscles innervated by these nerves, especially distal muscles of the feet, ankles, hands, and wrists, undergo denervation atrophy, leading to weakness and structural changes. Skeletal muscle (UBERON:0001134) and associated tendons and joints are thus secondarily affected. Foot deformities such as pes cavus involve bones and ligaments of the foot (UBERON:0001444), while kyphoscoliosis affects the vertebral column (UBERON:0001132).

In some patients, central nervous system structures are also involved. Brain MRI in SURF1-related disease can show lesions in the basal ganglia, particularly the putamen, and in brainstem regions such as the periaqueductal gray.[4][8][11][17] These structures belong to the brain (UBERON:0000955), basal ganglia (UBERON:0006101), and midbrain (UBERON:0001891). Cerebellar ataxia implies involvement of the cerebellum (UBERON:0002037). Hearing loss suggests damage to the auditory system, potentially the cochlea (UBERON:0000007) or auditory nerve.

From a body systems perspective, CMT4K involves the nervous system (central and peripheral), musculoskeletal system, and, to a lesser extent, metabolic system due to lactic acidosis. Cardiovascular, respiratory, digestive, and endocrine systems are typically spared, although severe neuromuscular weakness in some CMT4 forms can affect respiration.[9][11]

### 7.2 Tissue and Cell Types

At the tissue level, CMT4K affects nervous tissue and skeletal muscle tissue. Nervous tissue includes peripheral nerve fascicles composed of myelinated and unmyelinated axons ensheathed by Schwann cells, supported by connective tissue and vascular elements. The primary pathological lesion is demyelination and axonal degeneration within these nerves.[3][4][8][11] Schwann cells (CL:0000219) and peripheral sensory and motor neurons (CL:0000100 and CL:0000102) are the key cell populations targeted.

Skeletal muscle tissue (UBERON:0001134), composed of multinucleated muscle fibers (CL:0002385), undergoes denervation and atrophy due to loss of motor innervation. Muscle fibers may also suffer from intrinsic mitochondrial dysfunction in SURF1 deficiency, as indicated by reduced COX histochemical reaction and mitochondrial proliferation observed in Surf1 knockout mice and some Leigh syndrome patients.[13][8] Thus, both neural and muscular tissues are directly impacted.

In the central nervous system, neurons of the basal ganglia and brainstem are particularly vulnerable in Leigh syndrome, due to their high metabolic demands and specific mitochondrial characteristics.[8][17] In CMT4K, central involvement is less pronounced but still observed in some patients, evidenced by cerebellar ataxia and MRI lesions.[4][11] Neurons in these regions (CL:0000679) and glial cells may be affected.

### 7.3 Subcellular Structures and Localization

At the subcellular level, mitochondria (GO:0005739) are the primary compartment affected, specifically the mitochondrial inner membrane (GO:0005743) where complex IV resides. SURF1 localizes to this inner membrane and participates in the assembly of COX, so its absence disrupts inner membrane architecture and function.[14] The electron transport chain complexes and ATP synthase, also located in the inner membrane, are indirectly affected by complex IV deficiency.

Other subcellular structures involved include myelin sheaths, composed of multilamellar membranes produced by Schwann cells, although these are not separate organelles but rather extensions of Schwann cell membrane. Demyelination reflects damage or degeneration of these structures. Axonal cytoskeleton and transport machinery, including microtubules and mitochondrial trafficking systems, may be secondarily impacted by energy deficits.

Localization is predominantly bilateral and symmetric, as is typical for length-dependent neuropathies. Distal muscles and nerves of both lower and upper limbs are affected, often with more severe involvement of the legs than arms due to longer nerve lengths.[9][10][11] Nystagmus and hearing loss, when present, also suggest bilateral involvement. Asymmetry can occur with individual variation, but the disease is largely symmetric in distribution.

## 8. Temporal Development

### 8.1 Onset Characteristics

CMT4K typically begins in childhood, often in the first decade of life. OMIM states that CMT4K onset is in the first decade, and Orphanet lists childhood as the age of onset.[1][11] Echaniz-Laguna’s patients developed gait difficulties and distal weakness in early childhood.[4] The onset pattern is insidious, with gradual appearance of clumsiness, foot deformities, and difficulty running or climbing stairs, rather than acute episodes.

Symptoms may initially be subtle, and diagnosis is often delayed until school age when physical demands reveal deficits. In some cases, developmental milestones may be slightly delayed due to reduced muscle strength, but gross motor milestones are usually achieved. There is no evidence that CMT4K is congenital in the sense of being clinically apparent at birth, although the genetic defect is present from conception.

### 8.2 Disease Progression and Staging

Disease progression in CMT4K is chronic and slowly progressive, but staging systems specific to this subtype have not been established. Based on broader CMT literature and case descriptions, one can conceptualize stages as early, intermediate, and advanced, though these are descriptive rather than formally codified. In early childhood, patients show mild distal weakness, occasional falls, and subtle foot deformities. In adolescence and early adulthood, weakness and atrophy become more pronounced, leading to gait abnormalities, difficulty with fine hand tasks, and potential need for orthoses.[9][10][11][18]

In advanced stages, kyphoscoliosis, hand deformities, and severe distal weakness may limit ambulation and self-care. Cerebellar ataxia and nystagmus, when present, often emerge later, years after polyneuropathy onset.[4][11] Brain MRI lesions may develop or become more visible as disease progresses. Despite these progressive changes, many patients retain some ambulatory capacity into adulthood, unlike Leigh syndrome, which often leads to death before age ten.[8]

Progression rate is generally slow compared with acute or subacute neurological disorders. However, there may be periods of more rapid decline associated with systemic stressors, such as illness or puberty-related growth spurts, which can stress neuromuscular systems. The disease course is stable in the sense of continuous progression rather than relapsing-remitting; remission is not typical.

### 8.3 Disease Duration and Critical Periods

CMT4K is a lifelong chronic disease. Symptoms persist and gradually worsen throughout life. Unlike Leigh syndrome, which often leads to early death, CMT4K patients may survive into adulthood, though long-term outcome data are limited.[1][4][11][8] Orphanet notes that CMT usually does not reduce life expectancy unless severe respiratory complications occur in some CMT4 forms.[9] For CMT4K, no systematic survival analyses exist, but the reported patients did not die in childhood from neuropathy-related causes.

Critical periods may include childhood and adolescence, when growth, motor development, and social integration are occurring. Early intervention with rehabilitation and orthotic management during these periods can influence long-term outcomes by preventing contractures, optimizing gait, and supporting participation.[9][18] Another critical period may occur when central nervous system manifestations, such as cerebellar ataxia or brain MRI lesions, emerge, requiring reevaluation and adjustment of management strategies.[4][11][17]

Remission patterns are not described; symptoms do not spontaneously improve, although rehabilitation can enhance function. Treatment-induced improvements may be achievable in terms of strength and endurance, but they represent functional gains rather than disease reversal.[18]

## 9. Inheritance and Population Characteristics

### 9.1 Inheritance Pattern

CMT4K follows an autosomal recessive inheritance pattern. OMIM and Orphanet explicitly identify CMT4K as autosomal recessive demyelinating CMT caused by homozygous or compound heterozygous SURF1 mutations.[1][11][15] GTR also lists autosomal recessive inheritance for CMT4K.[19] In such a pattern, affected individuals inherit one pathogenic SURF1 allele from each parent, who are typically asymptomatic carriers.

Penetrance appears to be high—virtually complete—among individuals with biallelic loss-of-function SURF1 variants, although phenotypic expression can vary between CMT4K and Leigh syndrome. Expressivity is variable, as the same genotype may lead to different degrees of central or peripheral involvement, but in all reported CMT4K cases, peripheral neuropathy is pronounced.[4][8] There is no evidence of genetic anticipation, as SURF1 mutations do not involve repeat expansions.

Germline mosaicism has not been reported for SURF1-related CMT4K. Founder effects may exist in certain populations where specific SURF1 variants recur, such as the Turkish cohort of Leigh syndrome patients, but detailed population genetics for CMT4K-specific variants are lacking.[17] Consanguinity plays a notable role in some cases; Echaniz-Laguna’s initial CMT4K family was consanguineous, facilitating homozygosity for the c.107-2A>G SURF1 mutation.[4]

Carrier frequency for SURF1 pathogenic alleles in the general population is unknown but presumed to be very low, given the rarity of disease. In populations with high rates of consanguinity or where specific variants have founder effects, local carrier frequencies may be higher.

### 9.2 Epidemiology: Prevalence and Incidence

CMT4K is an extremely rare disease. Orphanet reports its prevalence as less than 1 per 1,000,000, reflecting only a handful of identified families worldwide.[11] CMT as a whole has a prevalence of approximately 1 in 2,500, making it one of the most common inherited neurologic disorders.[10] Within CMT, autosomal recessive demyelinating forms (CMT4) are less common, with estimated prevalence between 1 and 5 per 10,000.[9] Within CMT4, CMT4K represents a very small fraction.

Echaniz-Laguna et al. found SURF1 mutations in 2 of 41 families (about 5%) in a cohort of genetically undefined CMT4 patients, suggesting that SURF1-related CMT4K might account for a modest proportion of severe AR demyelinating neuropathies not attributable to known CMT4 genes.[4] However, this cohort was specialized and may not reflect broader population frequencies. There are no reliable incidence data for CMT4K; given its rarity, incidence is likely well below 1 per 100,000 per year, and many cases may remain undiagnosed, especially in regions without access to advanced genetic testing.

### 9.3 Population Demographics and Geographic Distribution

Specific demographic patterns for CMT4K are difficult to ascertain due to the small number of reported cases. The initial CMT4K family described by Echaniz-Laguna et al. was consanguineous, and the additional unrelated patient came from a separate population.[4] SURF1-related Leigh syndrome cohorts include patients from diverse ethnic groups, including Caucasian and Turkish populations.[8][17] The 2026 Frontiers cohort of five Chinese children with SURF1-related Leigh syndrome further expands the geographic distribution.[7]

These data suggest that SURF1 pathogenic variants occur worldwide, and CMT4K could appear in any population, though detection depends on diagnostic capacity. There is no evidence of particular ethnic or geographic predilection for CMT4K specifically, beyond potential founder effects in certain regions. Sex ratio among reported SURF1-related cases appears roughly balanced; the 2026 Frontiers cohort included four female and one male patient with Leigh syndrome.[7] CMT4K cases have not shown sex-specific differences.

Age distribution is skewed toward childhood onset, with patients presenting in the first decade and living into adolescence and adulthood. No cases of late-onset CMT4K in older adults have been described, though milder SURF1-associated phenotypes may exist undetected.

## 10. Diagnostics

### 10.1 Clinical Evaluation and Neurological Examination

Diagnosis of CMT4K begins with clinical suspicion based on characteristic signs of severe, childhood-onset demyelinating neuropathy. Neurological examination reveals distal weakness and atrophy in the feet and hands, reduced or absent tendon reflexes, and sensory loss for vibration and pain in the distal lower limbs.[1][4][9][10][11] Foot deformities such as pes cavus and hammer toes may be evident, and gait analysis may show steppage gait due to foot drop. Kyphoscoliosis, hand deformities, and nystagmus or cerebellar signs may be present depending on disease stage.[11]

Given the overlapping features with other CMT4 forms, detailed family history and assessment for consanguinity are important, as is careful documentation of age at onset, progression, and associated systemic features such as lactic acidosis or brain MRI abnormalities. The presence of lactic acidosis and complex IV deficiency should raise suspicion for a mitochondrial etiology, including SURF1-related CMT4K.[1][4][11]

### 10.2 Electrophysiological Testing

Nerve conduction studies (NCS) and electromyography (EMG) are crucial for confirming demyelinating neuropathy and distinguishing CMT4K from axonal CMT2 or other neuropathies. Echaniz-Laguna et al. report that all three patients with SURF1-associated CMT4 had motor nerve conduction velocities below 25 m/s, indicative of demyelinating pathology.[4][16] These low velocities, combined with reduced amplitudes in some nerves, support a diagnosis of demyelinating CMT.[10][15]

HPO term *Reduced motor nerve conduction velocity* (HP:0003431) captures this electrophysiological phenotype. EMG may show signs of chronic denervation, such as increased insertional activity, fibrillation potentials, and polyphasic motor unit potentials. NCS help distinguish CMT4K from acquired demyelinating neuropathies, which may show conduction block or temporal dispersion, features not typical of hereditary neuropathies.

### 10.3 Laboratory Tests and Biomarkers

Laboratory evaluation in suspected CMT4K should include serum lactate measurement and, if feasible, lactate/pyruvate ratios, given the association with lactic acidosis.[1][4][8][11] Elevated serum lactate (HP:0002151) and lactic acidosis (HP:0003128) support a mitochondrial respiratory chain disorder. Other routine blood tests may be normal, but assessment of creatine kinase and liver enzymes can help document muscle involvement and rule out other conditions.

Specific enzyme assays to measure complex IV activity in muscle or fibroblast homogenates provide strong diagnostic evidence. In CMT4K, complex IV activity is reduced, often in isolation, with normal activities of complexes I–III.[1][4][8][13][14] Histochemical COX staining on muscle biopsies can show reduced cytochrome c oxidase activity, as described by Santoro et al. in a Leigh syndrome patient with peripheral neuropathy.[3][8]

Biomarkers such as lactate, COX activity, and possibly mtDNA copy number or markers of mitochondrial biogenesis could be considered, though they are not routinely measured in clinical practice for CMT4K. FDA and BEST biomarker frameworks do not yet list specific biomarkers for this disease.

### 10.4 Imaging Studies

Brain MRI is recommended in patients with SURF1-related disease, especially when central nervous system symptoms such as cerebellar ataxia, nystagmus, or developmental delay are present. In Leigh syndrome, MRI often shows symmetric lesions in the basal ganglia and brainstem.[8][17] Echaniz-Laguna et al. report that two patients with SURF1-associated CMT4 had brain MRI abnormalities, including putaminal and periaqueductal lesions, and later developed cerebellar ataxia.[4] Orphanet lists such MRI abnormalities as part of SURF1-related CMT4K.[11]

These imaging findings help differentiate CMT4K from pure peripheral neuropathies without central involvement and support a diagnosis of mitochondrial encephalomyopathy. Radiopaedia and other imaging resources describe typical Leigh syndrome MRI patterns, but not specific to CMT4K. In some CMT4K patients, brain MRI may be normal or show mild nonspecific changes, especially early in disease, highlighting phenotypic variability.

Nerve ultrasound or MRI neurography could, in principle, show enlargement or structural changes in peripheral nerves, but such imaging has not been reported for CMT4K specifically. Spine X-rays or MRI can document kyphoscoliosis.

### 10.5 Histopathology and Biopsy Findings

Muscle biopsy in SURF1-related disease may show reduced COX staining and mitochondrial proliferation, as reported in Surf1 knockout mice and some human Leigh syndrome cases.[13][8] Santoro et al. observed decreased COX stain in skeletal muscle of a Leigh syndrome patient with SURF1 mutation, and nerve biopsy showed a defect of myelination.[3] Lee et al. note that muscle biopsies may appear normal if COX histochemistry is not included, despite underlying mitochondrial disease.[8]

In CMT4K, nerve biopsy would likely show demyelination, onion bulb formations, and axonal loss, consistent with severe demyelinating neuropathy. Echaniz-Laguna et al. did not detail nerve biopsy findings extensively, but the clinical and electrophysiological picture strongly supports such pathology.[4] Histopathology thus can confirm demyelination and complex IV deficiency, but biopsy is invasive and increasingly supplanted by genetic testing.

### 10.6 Genetic Testing Strategies

Genetic testing is central to definitive diagnosis of CMT4K. Recommended approaches include multigene panels for CMT and mitochondrial disease, whole exome sequencing (WES), or whole genome sequencing (WGS), depending on local resources. After clinical and electrophysiological confirmation of demyelinating CMT, genetic testing typically begins with known CMT1 and CMT4 genes. In patients with severe childhood-onset demyelinating neuropathy and additional features such as lactic acidosis, brain MRI abnormalities, and cerebellar ataxia, Echaniz-Laguna et al. suggest that SURF1 should be systematically screened.[4][16]

They write:

> "We found SURF1 mutations in 5% of families (2/41) presenting with CMT4. SURF1 should be systematically screened in patients with childhood-onset severe demyelinating neuropathy and additional features such as lactic acidosis, brain MRI abnormalities, and cerebellar ataxia developing years after polyneuropathy."[4]

GTR lists multiple clinical laboratories offering SURF1 testing, either as single-gene tests for SURF1-associated Leigh syndrome or within broader panels for mitochondrial disease or CMT.[19] WES or WGS can identify SURF1 variants even when not specifically suspected and is increasingly used in undiagnosed neuropathies.

Chromosomal microarray, karyotyping, and FISH are not typically indicated unless there are additional congenital anomalies suggesting a chromosomal syndrome. Mitochondrial DNA testing is relevant for other causes of Leigh syndrome but not for SURF1-related CMT4K, since SURF1 is nuclear encoded.[8][17]

### 10.7 Clinical Criteria and Differential Diagnosis

There are no formal society guidelines specifying diagnostic criteria for CMT4K, but a practical clinical picture includes severe childhood-onset demyelinating sensorimotor neuropathy, lactic acidosis, isolated complex IV deficiency, and biallelic SURF1 mutations.[1][4][11] Differential diagnosis encompasses other CMT4 subtypes, such as CMT4C caused by SH3TC2 mutations, which also present with distal weakness, atrophy, and sensory loss but lack mitochondrial features.[10][15] Charcot-Marie-Tooth disease type 4C, for example, is caused by recessive SH3TC2 mutations and presents with predominantly distal weakness and muscle atrophy, but without lactic acidosis or complex IV deficiency.[10]

Other differentials include acquired demyelinating neuropathies such as chronic inflammatory demyelinating polyradiculoneuropathy (CIDP), but these often show conduction block, inflammatory CSF, and respond to immunotherapy, whereas hereditary CMT does not.[10] Mitochondrial myopathies and encephalomyopathies such as Leigh syndrome are also differentials; in Leigh syndrome, central neurologic signs and MRI lesions dominate, and peripheral neuropathy may be mild or absent.[8][17] The presence of severe demyelinating neuropathy in the setting of SURF1 mutations tilts diagnosis toward CMT4K.

## 11. Outcome and Prognosis

### 11.1 Survival and Mortality

Because CMT4K is rare and reported in only a few families, robust survival statistics are not available. However, data from CMT and SURF1-related Leigh syndrome offer context. Orphanet notes that CMT is generally a slowly progressive neuropathy that causes eventual disability but does not usually reduce life expectancy, except in some early-onset CMT4 forms with severe respiratory complications.[9] CMT4K, while severe, has not been associated with early death in reported cases, suggesting that life expectancy may be near normal, provided respiratory function remains adequate and central involvement is mild.

By contrast, SURF1-associated Leigh syndrome is associated with poor prognosis and early mortality. Lee et al. state that the majority of patients with Leigh syndrome will have poor neurodevelopmental outcomes and often die before age ten, and that it is rare for patients to live beyond twenty years.[8] They note that treatment is largely supportive and outcomes are unsatisfactory.[8][17] These stark differences highlight that the phenotype—Leigh syndrome versus CMT4K—has major prognostic implications, even though both are caused by SURF1 mutations.

In CMT4K, survival is more favorable, but disability can be significant. No specific five-year or ten-year survival rates have been reported, but anecdotal evidence indicates that patients can survive into adulthood with ongoing neuropathy.

### 11.2 Morbidity, Disability, and Quality of Life

Morbidity in CMT4K is substantial, due to chronic neuropathy and secondary musculoskeletal complications. Disability outcomes include reduced mobility, need for orthoses or walking aids, limitations in fine motor tasks, and possible spinal deformities such as kyphoscoliosis.[9][11][18] Pain and fatigue can accompany neuropathy and deformities, affecting daily functioning.

Corrado et al. emphasize the disability burden of CMT in general, noting that the disease restricts daily activities and results in severe disability.[18] They find that physiotherapy and orthoses can improve muscle strength and functional outcomes, but evidence is still emerging.[18] In CMT4K, which is among the more severe forms, disability is likely to be greater than in mild CMT1A, and rehabilitation is crucial to maximize function.

Quality-of-life measures such as SF-36 or PROMIS have not been specifically applied to CMT4K, but based on clinical descriptions, patients would likely have reduced scores in physical functioning, role physical, and bodily pain domains. Emotional and social functioning may also be affected, particularly if disability leads to social isolation or occupational limitations. Early and continuous support, including psychological counseling, can help mitigate these impacts.

### 11.3 Complications and Recovery Potential

Complications in CMT4K can include orthopedic problems such as foot deformities, joint contractures, and kyphoscoliosis, as well as falls and injuries due to gait instability. Respiratory complications are possible in severe CMT4 forms where respiratory muscles are involved, but have not been prominently reported in CMT4K.[9][11] Hearing loss may complicate communication, and cerebellar ataxia can increase fall risk.

Recovery potential is limited, as CMT4K is a degenerative genetic disorder. However, functional improvements are possible through rehabilitation, orthotic management, and sometimes surgical interventions (e.g., corrective foot surgery). Corrado et al. report that strength or endurance training improves functionality and activities of daily living, and that physiotherapy contributes to improved muscle strength.[18] Such interventions do not reverse neuropathy but can enhance compensatory mechanisms.

Prognostic factors may include age at onset, severity of initial neuropathy, presence of central nervous system involvement, and access to rehabilitation services. Patients with earlier onset and more severe lactic acidosis or MRI lesions may have worse outcomes. Genetic factors, such as specific SURF1 variants and residual complex IV activity, may also influence prognosis, though data are limited.[4][8][14]

## 12. Treatment

### 12.1 Pharmacotherapy and Symptomatic Management

There is currently no curative therapy for CMT4K or SURF1-associated Leigh syndrome.[8][9][11] Treatment is largely supportive and symptomatic. Pharmacological interventions focus on managing neuropathic pain, spasticity, and associated symptoms. Drugs such as gabapentin, pregabalin, or duloxetine can be used for neuropathic pain, while non-opioid analgesics may manage musculoskeletal pain due to deformities. These treatments are generic to neuropathy and not specific to CMT4K.

Lee et al. discuss treatment for SURF1-associated Leigh syndrome, noting that a ketogenic diet is most often prescribed and has proven to be effective in some cases, and that coenzyme Q and other cofactors are commonly used but with inconsistent results.[8] These metabolic therapies aim to support mitochondrial function and provide alternative energy sources. While specific evidence in CMT4K is lacking, similar approaches might be considered, especially in patients with lactic acidosis or central involvement. However, caution is warranted, and treatment decisions should be individualized.

Importantly, valproate and other drugs that impair mitochondrial function should be avoided in SURF1-deficient patients.[8] This recommendation reflects pharmacogenomic considerations, where genetic variants affecting mitochondrial pathways influence drug toxicity. PharmGKB and CPIC have not yet issued specific guidelines on SURF1, but the principle of avoiding mitochondrial toxins in mitochondrial disease is well recognized.

### 12.2 Advanced Therapeutics: Gene and Cell-Based Approaches

As of the latest available data, no gene therapy or cell-based therapy has been approved or tested in clinical trials specifically for SURF1-related CMT4K. Theoretically, gene replacement therapy using viral vectors to deliver functional SURF1 to affected tissues could correct complex IV assembly and ameliorate disease, but challenges include targeting peripheral nerves and central structures, achieving sufficient expression, and addressing widespread tissue involvement.

CRISPR-based gene editing might be used to correct SURF1 mutations in patient-derived induced pluripotent stem cells (iPSCs), which could then be differentiated into neural or muscle cells for transplantation. However, such approaches remain experimental, and safety, efficacy, and ethical issues need to be addressed.

RNA-based therapies such as antisense oligonucleotides (ASOs) could potentially modulate splicing of SURF1 transcripts in splice-site mutations, restoring normal splicing. However, specific ASOs for SURF1 have not been reported, and development would require substantial preclinical work.

### 12.3 Surgical and Orthopedic Interventions

Surgical interventions in CMT4K primarily address orthopedic complications. Corrective foot surgery may be performed to treat severe pes cavus or other foot deformities, improving gait and reducing pain.[9][18] Spinal surgery may be needed for severe kyphoscoliosis to prevent progression and relieve pain. Orthopedic management, including braces, orthoses, and supportive footwear, is important to maintain mobility and prevent joint deformities.

Orphanet notes that treatment for CMT is mainly symptomatic, involving rehabilitation therapy and orthopedic management of joint deformities, muscle weakness, and somatosensory deficits, including use of orthoses or surgical treatment of clubfoot, hand deformities, or scoliosis, along with pain management and respiratory assistance when necessary.[9] These principles apply to CMT4K.

### 12.4 Rehabilitation and Supportive Care

Rehabilitation is a cornerstone of CMT4K management. Corrado et al. review the evidence for rehabilitation in CMT and conclude that physiotherapy treatment is useful to manage CMT, with strength or endurance training improving functionality and activities of daily living.[18] They find that individual training programs improved muscle strength in both upper and lower limbs and that orthoses can be helpful, particularly in pediatric populations with foot deformities and balance alterations.[18]

They write:

> "Physiotherapy treatment is a useful tool to manage CMT; more studies on a larger number of cases are needed to define orthosis utility and to establish the gold standard of the treatment."[18]

For CMT4K, a comprehensive rehabilitation program should include physical therapy for strength and balance, occupational therapy for fine motor skills and activities of daily living, and, where needed, speech therapy for dysarthria or swallowing difficulties in cases with central involvement. Orthoses such as ankle-foot orthoses (AFOs) can stabilize the ankle and improve gait, while hand splints may support grip.

Supportive care also encompasses pain management, psychological support, nutritional counseling, and social services. Respiratory support may be required in advanced cases with respiratory muscle involvement, though this is not typical for CMT4K.

### 12.5 Experimental Treatments and Clinical Trials

No clinical trials specifically targeting SURF1-related CMT4K are reported in the sources reviewed. Trials for Leigh syndrome and other mitochondrial disorders may include SURF1-related patients, testing drugs that enhance mitochondrial function, such as EPI-743 (a para-benzoquinone) or idebenone, or nutritional interventions like ketogenic diets and cofactor cocktails.[8][17] These treatments aim to improve energy metabolism and reduce oxidative stress.

Given the rarity of CMT4K, inclusion in broader mitochondrial disease trials may be the most feasible route for experimental therapies. ClinicalTrials.gov and WHO ICTRP could be consulted for current trials, although details are beyond the scope of the sources provided.

### 12.6 Treatment Outcomes and Personalized Medicine

Treatment outcomes in SURF1-related disease are generally unsatisfactory, especially in Leigh syndrome.[8] CMT4K, while less lethal, remains without disease-modifying therapy, and supportive interventions primarily slow complications rather than halt neuropathy. Physiotherapy shows benefits, but evidence is limited and trials are small.[18] Orthotic use is helpful in specific contexts but lacks standardized protocols.[18]

Personalized medicine approaches in CMT4K would involve tailoring rehabilitation and orthotic strategies to individual needs, considering disease severity, central involvement, and family circumstances. Genotype-guided treatment—for example, targeting specific SURF1 variants with splicing modulators or gene therapy—remains aspirational.

NCIT terms such as *Physical Therapy* (NCIT:C15220), *Orthopedic Procedure* (NCIT:C50779), *Mitochondrial Disease Therapy* (NCIT:C122060), and *Pain Management* (NCIT:C15732) can be used to annotate interventions.

## 13. Prevention

### 13.1 Primary Prevention

Primary prevention of CMT4K, in the sense of preventing disease occurrence, is challenging because the disease is monogenic and typically arises in families without prior knowledge of carrier status. However, genetic counseling and carrier screening can help reduce risk in high-risk families. Identification of SURF1 carriers through family-based testing and, potentially, population-based screening in communities with known founder mutations or high consanguinity could inform reproductive decisions.

Preventive strategies might include preconception carrier screening, prenatal testing, or preimplantation genetic diagnosis (PGD) for couples at known risk. ACMG and ACOG guidelines support such options for severe autosomal recessive disorders, though specific recommendations for CMT4K have not been formalized. WHO and CDC do not list CMT4K among population screening targets, reflecting its rarity.

### 13.2 Secondary Prevention: Early Detection and Intervention

Secondary prevention aims at early detection and intervention to reduce severity and complications. Newborn screening for CMT4K is not currently implemented, but early diagnosis through clinical recognition and genetic testing can allow timely initiation of rehabilitation, orthotic management, and, where appropriate, metabolic therapies. Early treatment may prevent contractures, optimize muscle strength, and improve long-term functional outcomes.

Screening of at-risk siblings in families with known SURF1 mutations can identify affected children early. Cascade screening within families, including parents, siblings, and extended relatives, allows detection of carriers and informs family planning. GTR lists clinical laboratories capable of testing SURF1 and diagnosing CMT4K.[19]

### 13.3 Tertiary Prevention: Complication Management

Tertiary prevention in CMT4K focuses on preventing complications in those already affected. Rehabilitation and orthopedic management are central, as they can delay or reduce musculoskeletal complications such as contractures, deformities, and falls.[9][18] Regular monitoring of spine alignment, foot posture, and joint range of motion allows timely interventions, including physiotherapy and surgery when necessary.

Metabolic monitoring, especially of lactate levels, can identify episodes of decompensation. Avoidance of mitochondrial toxins such as valproate and prompt treatment of infections reduce risk of metabolic crises.[8] Respiratory surveillance in severe cases helps detect respiratory muscle weakness early.

Genetic counseling also plays a tertiary preventive role by helping affected individuals understand recurrence risk and options for future pregnancies.

### 13.4 Behavioral Interventions and Public Health Measures

Behavioral interventions in CMT4K include promoting safe physical activity, adherence to rehabilitation programs, and avoidance of substances that could exacerbate neuropathy, such as excessive alcohol. Health education for patients and families is important to encourage adherence and prevent injuries.

Public health interventions are limited given the disease’s rarity. However, awareness campaigns within neurology and genetics communities can improve recognition and diagnosis. Environmental interventions, such as reducing exposure to mitochondrial toxins, are relevant to broader mitochondrial disease prevention but not specific to CMT4K.

### 13.5 Prophylactic Medications and Procedures

No prophylactic medications specifically prevent CMT4K or its progression. Coenzyme Q or vitamin supplementation may be used empirically in mitochondrial disease, but evidence of prophylactic benefit is limited and inconsistent.[8] Orthotic use can prevent falls and joint deformities, serving a prophylactic role in musculoskeletal complications.[18] Surgical correction of severe deformities can prevent pain and further disability.

NCIT terms such as *Genetic Counseling* (NCIT:C15915), *Prenatal Diagnosis* (NCIT:C25558), *Preimplantation Genetic Diagnosis* (NCIT:C61486), and *Orthotic Device* (NCIT:C49810) can annotate preventive interventions.

## 14. Other Species and Natural Disease

### 14.1 Species Affected and Orthologous Genes

SURF1 is conserved across mammals and many other taxa, with orthologous genes in mice, rats, and other species. NCBI Gene lists Surf1 orthologs in Mus musculus and other model organisms.[13][14] However, naturally occurring CMT4K-like disease in non-human species has not been reported. Veterinary databases such as OMIA focus on hereditary diseases in animals but do not list SURF1-related neuropathy as a recognized condition.

Nevertheless, the function of Surf1 in mice mirrors its role in humans. Agostino et al. created a constitutive Surf1 knockout mouse to model human SURF1 deficiency.[13] They report high post-implantation embryonic lethality in Surf1^−/− mice, early post-natal mortality, and profound isolated COX deficiency in skeletal muscle and liver, with morphological abnormalities in muscle but no obvious brain abnormalities.[13] These findings indicate that Surf1 is essential for COX function across species, and that deficits can cause mitochondrial disease.

### 14.2 Natural Disease in Animals and Comparative Pathology

No naturally occurring SURF1-related neuropathy akin to CMT4K has been described in companion animals or livestock. Comparative pathology therefore focuses on induced models rather than spontaneous disease. The Surf1 knockout mouse recapitulates some aspects of human mitochondrial disease but differs in phenotype; notably, mice lack overt neurological symptoms and show enhanced longevity despite reduced COX activity.[13][14]

This divergence offers valuable comparative insights. It suggests that species differences in mitochondrial biogenesis, stress responses, and tissue-specific energy demands can modulate disease expression. In humans, brain and peripheral nerves are highly susceptible to SURF1-related defects, whereas in mice, muscle and liver bear the brunt of pathology and compensatory mechanisms mitigate overt neurologic deficits.[13][14] Understanding these differences could illuminate mechanisms of tissue vulnerability and help design therapies that mimic protective responses observed in mice.

From an evolutionary perspective, the conservation of SURF1 and its role in COX assembly underscores the importance of oxidative phosphorylation across species. HomoloGene and other orthology databases demonstrate that SURF1 and COX subunits are conserved, reflecting evolutionary pressure to maintain efficient energy production. Pathogenic variants in these genes reveal the functional constraints and phenotypic consequences of perturbing conserved pathways.

### 14.3 Zoonotic Potential and Cross-Species Susceptibility

CMT4K is a genetic, non-infectious disease with no zoonotic potential. It cannot be transmitted between species via infectious agents. Cross-species susceptibility to SURF1-related disease is determined by the presence of orthologous Surf1 genes and the impact of mutations on COX function. Experimental models demonstrate that Surf1 deficiency can cause mitochondrial disease in mice, but natural cross-species transmission does not occur.[13][14]

## 15. Model Organisms

### 15.1 Surf1 Knockout Mouse Model

The primary model organism for SURF1-related disease is the Surf1 knockout mouse. Agostino et al. report the creation of a constitutive Surf1 knockout mouse, describing it as the first mammalian model for a nuclear disease gene of a human mitochondrial disorder.[13] They note:

> "We report here the creation of a constitutive knockout mouse for SURF1, a gene encoding one of the assembly proteins involved in the formation of cytochrome c oxidase (COX). Loss-of-function mutations of SURF1 cause Leigh syndrome associated with an isolated and generalized COX deficiency in humans."[13]

The murine phenotype includes high post-implantation embryonic lethality affecting approximately 90% of Surf1^−/− individuals, early-onset mortality in surviving post-natal mice, significant deficits in muscle strength and motor performance, profound isolated COX defect in skeletal muscle and liver, and morphological abnormalities of skeletal muscle characterized by reduced COX histochemical reaction and mitochondrial proliferation.[13] Notably, there are no obvious abnormalities in brain morphology and virtual absence of overt neurological symptoms.[13]

This model constitutes a useful tool to investigate the function of Surf1, understand pathogenesis of Surf1 deficiency in vivo, and evaluate treatment efficacy. It recapitulates key biochemical features—isolated COX deficiency and muscle mitochondrial changes—but does not fully reproduce human Leigh syndrome or CMT4K phenotypes.

### 15.2 Complex IV Deficient Surf1−/− Mice and Compensatory Responses

Pulliam et al. extended the characterization of Surf1^−/− mice, focusing on mitochondrial biogenesis and stress responses.[14] They found that Surf1−/− mice have a greater than 50% reduction in COX activity, yet exhibit enhanced median lifespan (~20% increase) compared to wild-type littermates, with no deleterious phenotype under basal conditions.[14] The loss of Surf1 resulted in a 71% and 53% decrease in COX activity in heart and skeletal muscle, respectively, without affecting other ETC complexes.[14]

They observed increased markers of mitochondrial biogenesis (PGC-1α and VDAC) in heart and skeletal muscle, and tissue-specific activation of stress responses: skeletal muscle showed upregulation of UPR^MT^, while heart exhibited induction of the Nrf2 antioxidant response pathway.[14] These compensatory responses likely contribute to the mild phenotype and enhanced longevity, highlighting the potential for adaptive mechanisms to mitigate complex IV deficiency.

The Surf1−/− mouse model thus provides a platform to study mitochondrial biogenesis, stress responses, and therapeutic interventions that might enhance similar compensation in humans. It also raises intriguing questions about species differences in mitochondrial regulation and the relationship between respiratory chain defects and aging.

### 15.3 Model Limitations and Applications

While Surf1 knockout mice are invaluable for studying complex IV deficiency, they have significant limitations as models for human CMT4K. They do not develop severe demyelinating peripheral neuropathy or central Leigh syndrome, and thus do not reproduce the full spectrum of human SURF1-related disease.[13][14] Their enhanced longevity contrasts with early lethality in human Leigh syndrome, highlighting species differences.

These limitations mean that the Surf1−/− mouse is better suited to studying biochemical and cellular mechanisms—such as COX assembly, mitochondrial biogenesis, and stress responses—rather than clinical neuropathy or encephalopathy. Application areas include testing metabolic therapies (ketogenic diet, cofactor supplementation), gene therapy approaches, and pharmacologic activation of PGC-1α or Nrf2 pathways.

Additional models, such as conditional knockout mice targeting SURF1 in specific tissues (e.g., nervous system) or patient-derived cellular models (fibroblasts, iPSCs differentiated into neurons or Schwann cells), could better recapitulate CMT4K. Such models would allow tissue-specific investigations of demyelination and neuropathy, bridging the gap between biochemical defects and clinical phenotypes.

Resources such as MGI and IMSR catalogue Surf1 knockout mouse lines, enabling researchers to access and use these models. Future work may integrate Surf1−/− models with other genetic manipulations to study modifier genes and combined mitochondrial defects.

## Conclusion

Charcot-Marie-Tooth disease type 4K (SURF1-related) occupies a unique position at the intersection of hereditary peripheral neuropathy and mitochondrial disease. It is defined by autosomal recessive biallelic SURF1 loss-of-function, leading to defective assembly of complex IV and isolated cytochrome c oxidase deficiency, and clinically manifests as severe childhood-onset demyelinating sensorimotor neuropathy with lactic acidosis and often additional central nervous system features such as cerebellar ataxia and Leigh-like MRI lesions.[1][4][8][11][17] Its rarity, with prevalence below 1 per 1,000,000, and phenotypic overlap with other CMT4 forms and SURF1-associated Leigh syndrome, mean that diagnosis requires high clinical suspicion and integration of electrophysiological, biochemical, and genetic data, notably nerve conduction studies, lactate levels, complex IV assays, and SURF1 sequencing.[1][4][8][11][19]

Mechanistically, CMT4K exemplifies how disruption of a mitochondrial assembly factor can produce tissue-specific disease. SURF1 deficiency impairs complex IV function, causing energy failure and lactic acidosis, but the phenotypic expression ranges from central encephalomyopathy (Leigh syndrome) to peripheral neuropathy (CMT4K). Compensatory mitochondrial biogenesis and stress responses, well documented in Surf1−/− mice, likely influence this spectrum, and tissue-specific differences in metabolic demands and regulatory pathways modulate vulnerability.[13][14] The causal chain—from germline SURF1 mutations to COX deficiency, oxidative phosphorylation impairment, lactic acidosis, and demyelination—provides a coherent framework for understanding disease pathophysiology, even as details of genotype–phenotype correlations remain unresolved.[3][4][8][14][17]

Clinically, CMT4K poses significant challenges in management. There is no curative therapy; treatment is largely supportive and focuses on rehabilitation, orthopedic interventions, pain management, and avoidance of mitochondrial toxins.[8][9][11][18] Physiotherapy and orthotic use can improve functional outcomes and delay complications, underscoring the importance of comprehensive rehabilitative care.[18] Metabolic therapies used in Leigh syndrome, such as ketogenic diets and cofactor supplementation, may have a role but require more evidence in CMT4K.[8] Genetic counseling is essential for affected families, given autosomal recessive inheritance and the potential for carrier screening, prenatal testing, and preimplantation genetic diagnosis.

Research opportunities abound. The phenotypic diversity of SURF1-related disease invites studies of modifier genes, tissue-specific mitochondrial regulation, and factors that determine central versus peripheral involvement. Advanced omics technologies—single-cell transcriptomics, spatial transcriptomics, and multi-omics integration—could reveal cell-type–specific mechanisms in peripheral nerve and brain. Model organisms, including Surf1−/− mice and patient-derived cellular models, provide platforms to test therapies that enhance mitochondrial biogenesis or stress responses. Ultimately, CMT4K exemplifies how insights from rare monogenic disorders can inform fundamental biology of energy metabolism, neurodegeneration, and aging.

For disease knowledge bases, CMT4K should be represented by standardized identifiers (OMIM:616684, ORPHA:391351, MONDO:0014733), causal gene annotation (SURF1, HGNC:11481, OMIM:185620), and comprehensive phenotype mapping using HPO terms for distal weakness, demyelinating neuropathy, lactic acidosis, complex IV deficiency, kyphoscoliosis, cerebellar ataxia, and MRI abnormalities.[1][4][5][8][11][15][17] Cell type, anatomy, and process ontologies (CL, UBERON, GO) can encode involvement of Schwann cells, peripheral nerves, skeletal muscle, basal ganglia, and oxidative phosphorylation pathways. Treatment annotations using NCIT terms for rehabilitation, orthopedic surgery, metabolic therapy, and genetic counseling will capture current practice. As knowledge evolves, particularly with new cases and mechanistic studies, the representation of CMT4K will refine our understanding of SURF1’s role in human disease and inform improved diagnostic, therapeutic, and preventive strategies.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.