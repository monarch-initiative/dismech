---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-08-27T15:11:04.779006'
end_time: '2026-08-27T15:14:55.046150'
duration_seconds: 230.27
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: hypomyelinating leukodystrophy 15 (EPRS1-related)
  mondo_id: MONDO:0054782
  category: leukodystrophy
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 18
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
- **Disease Name:** hypomyelinating leukodystrophy 15 (EPRS1-related)
- **MONDO ID:** MONDO:0054782 (if available)
- **Category:** leukodystrophy

## Research Objectives

Please provide a comprehensive research report on **hypomyelinating leukodystrophy 15 (EPRS1-related)** covering all of the
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

# Hypomyelinating Leukodystrophy 15 (EPRS1-related): Comprehensive Disease Characteristics

Hypomyelinating leukodystrophy 15 (HLD15) is a rare autosomal recessive neurodevelopmental disorder caused by biallelic pathogenic variants in the **EPRS1** gene, which encodes the bifunctional glutamyl-prolyl aminoacyl-tRNA synthetase that is essential for cytosolic protein translation.[2][7][9] The condition belongs to the broader group of hypomyelinating leukodystrophies, disorders characterized by defective formation and maintenance of central nervous system myelin, and manifests clinically with motor and cognitive impairment, movement disorders, pyramidal signs, and characteristic MRI evidence of diffuse hypomyelination.[1][3][8] Initial descriptions focused on childhood-onset, relatively severe phenotypes, but subsequent reports have broadened the clinical spectrum to include milder, adult-onset disease associated with compound heterozygosity for missense variants and exonic deletions in EPRS1.[4][12][13] Mechanistic work in patient-derived lymphoblastoid cell lines has demonstrated that specific EPRS1 missense variants can alter variant-distal mRNA **m⁶A** site accessibility, impair nuclear export and cytoplasmic translation of the mutant transcript, and lead to pathologically reduced EPRS1 protein levels, providing a direct link between disrupted aminoacyl-tRNA synthetase function and hypomyelination.[1][3] At present there is no curative therapy; management focuses on symptomatic treatment, rehabilitation, serial MRI monitoring, and genetic counseling, while emerging insights into RNA processing, translational control, and oligodendrocyte biology in HLD15 offer potential avenues for future targeted interventions.[1][3][13]

## 1. Disease Information

### 1.1 Definition and Overview

Hypomyelinating leukodystrophy 15 (HLD15) is defined as an autosomal recessive leukodystrophy characterized by diffuse hypomyelination of central nervous system white matter on MRI, accompanied by motor and cognitive impairment, attributable to biallelic pathogenic variants in **EPRS1 (glutamyl-prolyl-tRNA synthetase 1)**.[2][7][9] Hypomyelinating leukodystrophies as a group are distinguished radiologically by persistently reduced myelin signal rather than frank demyelination, typically with homogeneous T2-weighted hyperintensity of supratentorial white matter that does not progress to the confluent cavitation seen in some demyelinating diseases.[1][3][15] In the context of HLD15, affected individuals show variable combinations of dystonia, ataxia, spasticity, dysphagia, optic atrophy, and cognitive decline, with onset most commonly in childhood or adolescence, although adult-onset cases have now been documented.[8][13] The disease results from impaired function of EPRS1, a key enzyme in cytosolic tRNA aminoacylation pathways, and joins other aminoacyl-tRNA synthetase–related leukodystrophies such as those caused by **RARS1** and **DARS1**, emphasizing the importance of translational machinery in myelin development.[1][6]

Khan et al., in their 2024 Nature Communications paper, succinctly framed HLD within the broader category of hypomyelinating leukodystrophies, stating that "Hypomyelinating leukodystrophy (HLD) is an autosomal recessive disorder characterized by defective central nervous system myelination."[1][3] They further noted that "HLD is rare, but comprises the single largest category among undiagnosed genetic leukodystrophies, which collectively impacts ~1 in 7500 live births, representing a major group of neurodevelopmental disorders," emphasizing both the rarity and collective burden of these conditions.[1] Within this group, HLD15 is specifically tied to EPRS1 dysfunction and was delineated by OMIM and subsequent case series as a discrete entity, with characteristic MRI, clinical course, and genetic etiology.[2][4][9] Orphanet and related rare disease resources underscore that hypomyelinating leukodystrophies are primarily pediatric-onset neurologic diseases with high morbidity, though individual subtypes such as HLD15 can present across a broader age range.[6][8]

### 1.2 Identifiers, Synonyms, and Classification

HLD15 is catalogued in multiple biomedical ontologies and databases under specific identifiers that facilitate standardized annotation and data integration. OMIM lists **"Leukodystrophy, hypomyelinating, 15; HLD15"** under entry number **617951**, mapping it to chromosome 1q41 and specifying an autosomal recessive mode of inheritance.[9] The **EPRS1** gene itself is described in OMIM entry **138295** as "GLUTAMYL-PROLYL-tRNA SYNTHETASE 1; EPRS1," with the associated phenotype "Leukodystrophy, hypomyelinating, 15" recorded in the locus-phenotype table.[2] The Monarch Initiative maps HLD15 to the ontology term **MONDO:0054782**, labeled "leukodystrophy, hypomyelinating, 15," and links it to corresponding OMIM phenotype identifiers, highlighting its placement within the MONDO unified disease ontology.[5][11]

Synonyms and alternative names commonly used in the literature include "EPRS1-related hypomyelinating leukodystrophy," "EPRS1-related disorder," and "EPRS1-associated leukodystrophy," as reflected in the 2023 Journal of the Neurological Sciences genotype-phenotype correlation study that referred to "EPRS1-related disorder: A genotype-phenotype correlation."[4] PanelApp Australia, in its "Leukodystrophy – adult onset" gene panel, lists the gene under the historical symbol **EPRS** but links the phenotype specifically to "Leukodystrophy, hypomyelinating, 15, MIM#617951," reinforcing the association.[8] In a broader classification sense, HLD15 falls under the umbrella of **"leukodystrophy"** (e.g., HPO term HP:0002415), **"hypomyelinating leukodystrophy"** (often grouped under OMIM PS312080), and **"neurodevelopmental disorder"**, especially given its early onset and impact on cognitive and motor development.[1][9][15]

International disease classification systems do not currently assign a unique ICD-10 or ICD-11 code to HLD15, and clinical coding generally uses broader categories such as **ICD-10 E75.2 ("Other sphingolipidosis")** or related codes for leukodystrophies and metabolic white matter disorders.[6] Orphanet provides detailed nosology and prevalence for related aaRS leukodystrophies such as **RARS-related autosomal recessive hypomyelinating leukodystrophy** (ORPHA:438114), which is conceptually similar to HLD15 and underscores how individual genetic subtypes are nested within higher-level leukodystrophy categories.[6] For ontology mapping in knowledge bases, HLD15 is most appropriately associated with **MONDO:0054782**, OMIM:617951, and broader leukodystrophy groupings, while EPRS1 should be annotated with its HGNC-approved symbol **EPRS1**, cytogenetic location 1q41, and UniProt identifiers.[2][7][17]

To support structured data integration, the following table summarizes key identifiers, acknowledging that some values (such as MeSH or specific ICD-11 codes) are not yet uniquely assigned to HLD15 and must rely on more general leukodystrophy categories.

| Resource/Ontology | Identifier / Entry | Label / Description | Notes |
|-------------------|--------------------|---------------------|-------|
| OMIM (phenotype)  | 617951             | Leukodystrophy, hypomyelinating, 15; HLD15 | Autosomal recessive leukodystrophy with EPRS1 causation[9] |
| OMIM (gene)       | 138295             | GLUTAMYL-PROLYL-tRNA SYNTHETASE 1; EPRS1 | Causal gene located at 1q41[2] |
| MONDO             | MONDO:0054782      | leukodystrophy, hypomyelinating, 15 | Mapped to OMIM phenotype; human disease ontology term[5][11] |
| HGNC              | HGNC:23674         | EPRS1              | Approved gene symbol for glutamyl-prolyl-tRNA synthetase 1[2][7] |
| Orphanet (related) | ORPHA:438114      | RARS-related autosomal recessive hypomyelinating leukodystrophy | Different gene (RARS1) but similar clinical category[6] |
| ICD-10            | E75.2              | Other sphingolipidosis | Commonly used for leukodystrophy coding; not HLD15-specific[6] |

### 1.3 Source Type and Evidence Aggregation

Information about HLD15 is derived primarily from aggregated disease-level resources, curated gene–phenotype databases, and a small number of detailed case reports and mechanistic studies, rather than from large-scale registry data or electronic health record analyses. OMIM’s entries for EPRS1 and HLD15 synthesize information from multiple clinical publications, functional studies, and expert curation to present a consolidated picture of the gene’s function and associated phenotype.[2][9] The Monarch Initiative similarly aggregates cross-species and cross-database information, including OMIM linkages, to annotate HLD15 as a disease term within MONDO and connect it to human and model organism data.[5][11]

Primary clinical descriptions have come from a handful of families reported in the literature. Chapleau et al. in 2023 reviewed biallelic EPRS1 pathogenic variants and highlighted that "Biallelic pathogenic variants in EPRS1 have been shown to cause a rare hypomyelinating leukodystrophy previously reported in 4 patients," underscoring the limited but growing patient base.[4] Khan et al. in 2024 described two affected siblings with severe cognitive and motor impairment and progressive hypomyelination, and performed detailed cellular and molecular analyses on patient-derived cells.[1][3] Mitsutake et al. in 2026 reported a 40-year-old woman with adult-onset HLD15 due to compound heterozygosity for a missense variant and an exonic deletion, expanding both the mutational and clinical spectrum.[12][13] These reports rely on individualized clinical and radiologic data, but the disease concept is now consolidated in curated databases, so the knowledge base reflects aggregated disease-level information culled from a relatively small number of well-characterized cases.

Thus, in populating a knowledge base entry, it is important to distinguish between evidence arising from individual case reports and small series, versus consensus statements and database annotations. For HLD15, nearly all detailed phenotypic and mechanistic claims are traceable to specific peer-reviewed papers (e.g., Khan 2024, Mitsutake 2026) and OMIM entries, meaning that each assertion should be linked to the underlying PMID or database record. The rarity of the condition also implies that many aspects of its natural history, epidemiology, and treatment remain incompletely characterized, and these gaps should be explicitly flagged in any structured representation of the disease.

## 2. Etiology

### 2.1 Genetic Causal Factors

The primary and, based on current evidence, exclusive causal factor in hypomyelinating leukodystrophy 15 is the presence of **biallelic pathogenic variants in the EPRS1 gene**, which encodes the glutamyl-prolyl aminoacyl-tRNA synthetase 1.[2][7][9] OMIM states that "Bi-allelic mutations in EPRS, encoding the glutamyl-prolyl-aminoacyl-tRNA synthetase, cause a hypomyelinating leukodystrophy," directly linking the phenotype HLD15 to loss-of-function or functionally disruptive variants in EPRS1.[2] PanelApp Australia classifies EPRS (now EPRS1) as a "Green List (High Evidence)" gene for the "Leukodystrophy – adult onset" panel and specifies that biallelic variants are associated with "Leukodystrophy, hypomyelinating, 15, MIM#617951," confirming expert consensus regarding the gene’s etiologic role.[8]

Khan et al. identified a specific homozygous missense single nucleotide variant in two siblings: **c.4444 C>A; p.Pro1482Thr (rs930995541) in EPRS1 (NM_004446.2)**.[1][3] They wrote: "Exome sequencing of two siblings with severe cognitive and motor impairment and progressive hypomyelination characteristic of HLD revealed homozygosity for a missense single-nucleotide variant (SNV) in EPRS1 (c.4444 C > A; p.Pro1482Thr), encoding glutamyl-prolyl-tRNA synthetase, consistent with HLD15."[1][3] Both parents and an unaffected sibling were heterozygous carriers, consistent with autosomal recessive inheritance, and no alternative diagnosis was identified by exome sequencing, providing strong genetic evidence for causality.[1] Chapleau et al. reviewed previously reported patients with biallelic EPRS1 variants and concluded that "Biallelic pathogenic variants in EPRS1 have been shown to cause a rare hypomyelinating leukodystrophy previously reported in 4 patients," further corroborating the gene–disease link.[4]

Mitsutake et al. expanded the mutational spectrum by describing a patient with **compound heterozygosity**: a heterozygous missense variant in the prolyl-tRNA synthetase domain, **c.3430 C>G; p.Leu1144Val (NM_004446.3)**, and a heterozygous 220-bp deletion spanning exon 15 (**c.1743-30_1932del**).[12][13] Their abstract states: "Whole-exome sequencing identified a heterozygous missense variant in the prolyl-tRNA synthetase domain of EPRS1 (c.3430 C > G; p.Leu1144Val, NM_004446.3), without second variant. Whole-genome sequencing revealed a heterozygous 220-bp deletion spanning exon 15 (c.1743-30_1932del), and segregation analysis confirmed compound heterozygosity."[13] RT-PCR showed exon 15 skipping leading to a frameshift and nonsense-mediated decay, leaving predominant expression of the missense allele; these findings "support loss-of-function for the deletion and classify c.3430 C > G as likely pathogenic under ACMG/AMP criteria," consolidating EPRS1 LOF as the etiologic mechanism.[12][13]

ClinVar documents at least one pathogenic EPRS1 variant linked to HLD15 (accession VCV000523133.9), recorded under "LEUKODYSTROPHY, HYPOMYELINATING, 15," and supported by a submission with literature evidence.[14] GeneCards summarizes that diseases associated with EPRS1 include "Leukodystrophy, Hypomyelinating, 15 and Parkinson's Disease," although the latter association is more speculative, whereas the leukodystrophy link is firmly grounded in OMIM and primary literature.[7] Together, these resources converge on a genetic etiology in which biallelic germline variants—missense, frameshift, and exonic deletions—disrupt EPRS1 function sufficiently to impair myelination during brain development.

### 2.2 Genetic Risk Factors and Variant Types

Within the etiologic framework of HLD15, the key genetic risk factor is carriage of **two deleterious EPRS1 alleles**, with heterozygous carrier status conferring reproductive risk but not known to cause clinical disease. Reported pathogenic or likely pathogenic variants include the homozygous **p.Pro1482Thr** missense change in the C-terminal region of EPRS1, the **p.Leu1144Val** missense variant in the prolyl-tRNA synthetase domain, and the exon 15 deletion leading to frameshift and nonsense-mediated decay.[1][3][12][13] These variants are rare in population datasets, and Khan et al. noted that rs930995541 (Pro1482Thr) is extremely infrequent in public databases, consistent with its pathogenicity and the rarity of HLD15.[1][3] ClinVar’s record for HLD15-associated EPRS1 variant supports classification under ACMG/AMP guidelines, although the specific variant and criteria are detailed in the underlying submission rather than in the search snippet.[14]

Variant classes in HLD15 include **missense variants** that presumably alter enzymatic activity or structural integrity of the EPRS1 protein, and **structural variants**, such as exon-level deletions, that cause frameshift and loss-of-function through nonsense-mediated decay.[1][3][12][13] The Mitsutake case demonstrates that structural variants may be under-detected by conventional exome sequencing and require genome sequencing or targeted copy-number analyses; they emphasized that "This case represents the first exonic deletion reported in EPRS1. The relatively mild, adult-onset phenotype broadens both mutational and clinical spectra of HLD15 and highlights the importance of structural-variant analysis when only a single candidate variant is detected in recessive leukodystrophy."[13] All reported disease-causing variants are **germline**, inherited from asymptomatic carrier parents, and there is currently no evidence that somatic EPRS1 mutations contribute to leukodystrophy or other neurodegenerative phenotypes.[1][3][12][13]

Allele frequencies in gnomAD or similar databases are not explicitly given in the supplied sources, but the designation of HLD15 as an ultra-rare disease and the classification of variants as pathogenic under ACMG criteria imply very low population frequencies, consistent with recessive inheritance and severe phenotypic consequences.[2][4][9] There is no evidence for common susceptibility alleles or modifier variants that modulate risk of HLD15, and the disease appears to arise only when individuals harbor two deleterious alleles in EPRS1. However, by analogy with other aaRS-related disorders, it remains plausible that differences in residual enzyme activity, domain-specific effects, or interactions with multi-aminoacyl-tRNA synthetase complex components could contribute to intra-familial and inter-individual variability in severity, a hypothesis that warrants further study.[1][6]

### 2.3 Environmental and Lifestyle Risk Factors

No environmental, lifestyle, infectious, or occupational risk factors have been identified that independently cause hypomyelinating leukodystrophy 15 or significantly modify its risk or expression. The current literature and database entries emphasize a strictly **monogenic, autosomal recessive** etiology, with all reported patients having biallelic pathogenic variants in EPRS1 and no suggestion of environmental triggers analogous to those sometimes implicated in acquired demyelinating conditions.[1][2][4][9] Khan et al. describe HLD as an autosomal recessive neurodevelopmental disorder, and their focus is entirely on genetic causation without mention of environmental modifiers.[1][3] Similarly, OMIM and PanelApp attribute HLD15 to biallelic EPRS1 mutations and do not list any environmental factors as contributing to disease risk.[2][8][9]

General leukodystrophy literature distinguishes genetic leukodystrophies from acquired white matter disorders caused by toxins, hypoxia, infections, or immune-mediated processes, and HLD15 belongs to the former category.[1][15] There is no evidence that exposure to specific neurotoxins, nutritional deficiencies, or infections precipitate disease in EPRS1 carriers or accelerate progression in affected individuals, beyond the usual considerations that systemic illness or metabolic stress may transiently worsen neurologic function in patients with underlying white matter disorders. Lifestyle factors such as smoking, alcohol use, or exercise have not been studied in relation to HLD15, and given the rarity and early onset of most cases, it is unlikely that such factors are primary determinants of risk.

### 2.4 Protective Factors and Gene–Environment Interactions

Given the monogenic and highly penetrant nature of HLD15, specific protective genetic variants or environmental exposures have not been identified. Heterozygous carriers appear clinically unaffected, suggesting that one functional EPRS1 allele is sufficient to maintain normal myelination under typical environmental conditions.[1][2][9] Whether differences in diet, metabolic status, or pharmacologic exposures can modulate disease severity in affected individuals through effects on translation, RNA modifications, or oligodendrocyte function remains entirely speculative, as no studies have systematically addressed these questions in HLD15.[1][3][4][13]

Khan et al.’s focus on mRNA **m⁶A** modifications and nuclear export hints at possible broader gene–environment interactions in related pathways, since RNA methylation and translation can be influenced by cellular stress and nutrient availability, but their data in patient lymphoblastoid cells did not explore environmental modulation.[1][3] They showed that the Pro1482Thr variant alters access of METTL3-mediated m⁶A deposition at a variant-distal site, thereby impairing nuclear export and translation of EPRS1 mRNA, a mechanism intrinsic to the mutant transcript rather than dependent on external exposures.[1][3] Thus, at present, HLD15 is best conceptualized as a purely genetic disease in which the genotype (EPRS1 variant combination) is the dominant determinant of risk, and gene–environment interactions, if they exist, await elucidation.

## 3. Phenotypes

### 3.1 Core Neurologic and Systemic Features

The clinical phenotype of hypomyelinating leukodystrophy 15 encompasses a spectrum of neurologic impairments primarily affecting motor function, coordination, and cognition, often accompanied by visual and bulbar involvement. Khan et al. reported that HLD in general is characterized by "severe cognitive and motor impairment with onset in early childhood or adolescence," and their two siblings with HLD15 exhibited progressive hypomyelination and significant neurologic disability.[1][3] PanelApp’s description of EPRS-related leukodystrophy emphasizes that "Onset of motor and cognitive impairment [occurs] in the first or second decade of life. Features include dystonia, ataxia, spasticity, dysphagia, severe optic atrophy, and some have hearing loss. Brain imaging shows hypomyelinating leukodystrophy with thin corpus callosum."[8] These manifestations can be mapped to HPO terms such as **HP:0001263 (Global developmental delay)**, **HP:0001250 (Seizures)** if present, **HP:0001251 (Ataxia)**, **HP:0001252 (Spasticity)**, **HP:0001338 (Dystonia)**, **HP:0002015 (Dysphagia)**, **HP:0000603 (Optic atrophy)**, and **HP:0000365 (Sensorineural hearing impairment)**, although specific frequencies are not yet systematically quantified.

Chapleau et al.’s genotype-phenotype correlation study reviewed four previously reported patients with EPRS1-related hypomyelinating leukodystrophy and noted that the disorder manifests as a rare hypomyelinating leukodystrophy with motor impairment and intellectual disability, though detailed case-by-case phenotypes are not fully captured in the search snippet.[4] Mitsutake et al. described an adult patient whose clinical picture was milder but still encompassed core features: "We describe a 40-year-old woman with mild intellectual disability, ataxia, dystonia, and MRI showing hypomyelination."[13] These symptoms correspond to HPO terms HP:0001250 (Intellectual disability), HP:0001251 (Ataxia), and HP:0001338 (Dystonia), and indicate that even in adult-onset disease the triad of cognitive impairment, cerebellar signs, and movement disorder is characteristic.[13]

RARS1-related hypomyelinating leukodystrophy, while genetically distinct, provides a useful phenotypic comparison. Orphanet describes this disorder as "a rare, genetic leukodystrophy characterized by developmental delay, increased muscle tone leading later to spasticity, mild ataxia, nystagmus, dysarthria, intentional tremor, and mild intellectual disability. Brain imaging reveals supratentorial and infratentorial hypomyelination."[6] Many of these features overlap with HLD15, reinforcing the concept of a shared clinical phenotype among aminoacyl-tRNA synthetase leukodystrophies, with manifestations such as spasticity, ataxia, tremor, and intellectual disability often present.[1][4][6] From a quality-of-life perspective, these symptoms collectively impair ambulation, fine motor skills, communication, and independence, often necessitating long-term assistance in activities of daily living and specialized educational support.

### 3.2 Age of Onset, Symptom Severity, and Progression

Age of onset in HLD15 appears to be variable, with most reported cases presenting in childhood or adolescence, consistent with the neurodevelopmental nature of hypomyelinating leukodystrophies, but at least one case showing adult-onset manifestations. PanelApp indicates that "Onset of motor and cognitive impairment [in EPRS-related leukodystrophy] [occurs] in the first or second decade of life," capturing a typical pediatric or teenage onset.[8] Khan et al.’s affected siblings had severe cognitive and motor impairment with progressive hypomyelination, implying early childhood onset, though the exact ages are not specified in the search snippet.[1][3] Mitsutake et al.’s patient, in contrast, presented with mild intellectual disability and neurologic symptoms that were recognized or became debilitating in adulthood, at age 40, thereby broadening the age-of-onset spectrum.[13]

Symptom severity can range from moderate to severe, depending on the nature of the underlying EPRS1 variants and possibly other modifying factors. The early-onset siblings described by Khan et al. had "severe cognitive and motor impairment," suggesting a high level of functional disability with significant impact on school performance, motor milestones, and daily independence.[1][3] PanelApp’s description of dystonia, spasticity, dysphagia, severe optic atrophy, and hearing loss implies clinical severity sufficient to compromise mobility, swallowing, and sensory function, often requiring feeding support, assistive devices, and possibly anti-spasticity pharmacotherapy.[8] By contrast, Mitsutake et al.’s adult patient had "mild intellectual disability" and neurologic symptoms (ataxia, dystonia) that, while symptomatic, may allow for greater autonomy, indicating that HLD15 encompasses a range of severities.[13]

Progression is generally **slow and chronic**, with neurologic deficits accumulating over years rather than presenting acutely. Hypomyelinating leukodystrophies, as characterized by Steenweg et al., typically show stable or slowly progressive MRI abnormalities and clinical trajectories, as opposed to rapidly progressive demyelinating conditions.[15] In their MRI pattern recognition study, Steenweg et al. noted that hypomyelinating disorders can be distinguished by persistent myelin deficits without the acute lesions or remyelination seen in other diseases, suggesting a developmental defect rather than ongoing destructive pathology.[15] Khan et al. referred to "progressive hypomyelination" in their siblings, implying that MRI abnormalities and clinical impairment worsened over time, although specific staging and rates of progression are not detailed.[1][3] There is no evidence for episodic or relapsing-remitting courses in HLD15; instead, the disease appears to follow a lifelong trajectory of slowly increasing disability.

### 3.3 MRI and Neuroimaging Phenotype

MRI findings are central to the diagnosis and characterization of HLD15, as they illustrate the hallmark pattern of hypomyelination in central white matter and associated structural changes. Khan et al. highlighted that their siblings had "progressive hypomyelination characteristic of HLD," with serial brain MRI used to monitor disease progression.[1][3] Although the specific imaging sequences and regional involvement are not exhaustively detailed in the snippet, the general pattern in hypomyelinating leukodystrophies includes diffuse, homogeneous T2 hyperintensity of the supratentorial white matter, relative preservation of U-fibers, and often involvement of cerebellar and brainstem tracts.[1][15]

PanelApp’s summary for EPRS-related leukodystrophy notes that "Brain imaging shows hypomyelinating leukodystrophy with thin corpus callosum," indicating that corpus callosum hypoplasia or atrophy is a consistent feature in HLD15.[8] This structural change corresponds to HPO term **HP:0002079 (Thin corpus callosum)** and suggests that callosal axons and their myelination are particularly affected, consistent with generalized white matter involvement. Mitsutake et al.’s adult patient had MRI "showing hypomyelination," but the abstract does not specify whether the corpus callosum was thin; nonetheless, their case reinforces that diffuse hypomyelination remains the radiologic hallmark even in milder adult-onset disease.[13]

Steenweg et al.’s landmark 2010 study on MRI pattern recognition in hypomyelinating disorders provides a conceptual framework for interpreting HLD15 imaging.[15] They wrote: "The aim of this study was to determine the possible role of magnetic resonance imaging pattern recognition in distinguishing different hypomyelinating disorders, which would facilitate the diagnostic process," and after analyzing 112 patients, they concluded that "This study shows that it is possible to separate patients with hypomyelination disorders of known cause in clusters based on magnetic resonance imaging abnormalities alone."[15] Important discriminating items included early cerebellar atrophy, homogeneity of white matter signal, basal ganglia abnormalities, and pontine signal changes.[15] While HLD15 was not among the disorders included in this 2010 series, subsequent case descriptions suggest that its MRI pattern aligns with the hypomyelinating cluster, with diffuse white matter hypomyelination and possible callosal thinning, but without severe cerebellar atrophy or cavitary lesions typical of some other leukodystrophies.[1][8][13]

### 3.4 Quality of Life Impact and Functional Consequences

HLD15 exerts a profound impact on quality of life, primarily through its effects on motor function, cognition, and sensory systems. In severe early-onset cases, global developmental delay and intellectual disability limit educational attainment and independent living, while spasticity, dystonia, and ataxia interfere with ambulation, balance, and fine motor tasks, often necessitating use of wheelchairs, walkers, or orthotic devices.[1][3][8] Dysphagia and bulbar dysfunction can compromise safe swallowing and nutrition, requiring dietary modifications, feeding tube placement, and intensive speech and swallowing therapy.[8] Severe optic atrophy and sensorineural hearing loss, when present, further impair communication and interaction with the environment, complicating rehabilitation efforts.[8]

In milder adult-onset HLD15, as illustrated by Mitsutake et al.’s patient with mild intellectual disability and cerebellar signs, individuals may retain greater independence but still face challenges with employment, social integration, and daily activities requiring coordination and sustained attention.[13] Movement disorders such as dystonia can cause pain, abnormal postures, and functional limitations that impact self-care and mobility, even when cognition is only mildly affected.[8][13] From a psychosocial standpoint, chronic visible disability and dependence on caregivers may contribute to emotional distress, anxiety, and decreased health-related quality of life, although specific quantitative assessments (e.g., SF-36 or EQ-5D scores) have not yet been reported for HLD15.

Given the multi-domain nature of impairment, appropriate HPO terms reflecting quality-of-life impact include **HP:0000716 (Anxiety)**, **HP:0000739 (Depression)** if present, **HP:0007010 (Impaired activities of daily living)**, and **HP:0003758 (Motor delay)**, though these have not been systematically annotated in the limited case literature.[1][3][4][13] In clinical practice, multidisciplinary care involving neurology, rehabilitation medicine, speech therapy, ophthalmology, audiology, and psychology is required to address the diverse functional consequences of HLD15.[1][8] These considerations should be explicitly encoded in knowledge bases to ensure that disease entries capture not only core neurologic signs but also their broader impact on patient well-being and healthcare needs.

## 4. Genetic and Molecular Information

### 4.1 The EPRS1 Gene: Structure, Function, and Pathways

EPRS1 is the human gene encoding **glutamyl-prolyl-tRNA synthetase 1**, a bifunctional aminoacyl-tRNA synthetase responsible for charging tRNA molecules with their cognate amino acids, glutamic acid and proline.[2][7][17] OMIM notes that "Aminoacyl-tRNA synthetases are enzymes that charge tRNAs with their cognate amino acids," and specifies that EPRS is a "multifunctional aminoacyl-tRNA synthetase that catalyzes the aminoacylation of glutamic acid and proline tRNA species (Cerini et al., 1991)."[2] The gene is located at **chromosome 1q41**, with genomic coordinates (GRCh38) 1:219,968,600–220,046,505.[2] UniProt describes EPRS1 as a large cytosolic enzyme that participates in the **multi-aminoacyl-tRNA synthetase complex (MSC)** and is predicted to be active in the cytoplasm, with orthologs in multiple species including zebrafish (eprs1).[11][17]

GeneCards lists EPRS1 under the label "Glutamyl-Prolyl-TRNA Synthetase 1" and associates it with pathways including "Cytosolic tRNA aminoacylation," underscoring its role in the canonical protein translation machinery.[7] The protein contains distinct enzymatic domains for glutamyl- and prolyl-tRNA synthetase activities, as well as regulatory motifs implicated in noncanonical functions such as the GAIT (gamma interferon–activated inhibitor of translation) complex, which modulates selective translation of inflammatory transcripts.[1][3] In addition to its basic housekeeping role in translation, EPRS1 has been implicated in intracellular signaling and gene expression regulation, though the precise contribution of these noncanonical functions to myelination remains incompletely understood.[1][3][7]

At the molecular level, EPRS1 activity ensures that tRNA\(^\text{Glu}\) and tRNA\(^\text{Pro}\) are properly charged, a prerequisite for accurate incorporation of glutamate and proline into nascent polypeptides.[2][17] Disruption of EPRS1 function, whether by reduced protein levels or altered catalytic efficiency, is expected to globally impair protein synthesis and potentially exert more pronounced effects in cell types with high translational demands, such as oligodendrocytes during myelination.[1][3] GO terms appropriate for annotating EPRS1 function include **GO:0004810 (tRNA aminoacylation for protein translation)**, **GO:0006418 (tRNA aminoacylation)**, and **GO:0006412 (translation)**, and cellular component terms such as **GO:0005829 (cytosol)**.[2][7][17]

### 4.2 Spectrum of Pathogenic Variants in EPRS1

To date, a small but growing set of pathogenic or likely pathogenic EPRS1 variants have been reported in association with HLD15. Khan et al. identified a **homozygous missense variant c.4444 C>A; p.Pro1482Thr (rs930995541)** in two siblings, in whom both parents and an unaffected brother were heterozygous carriers.[1][3] They noted that "Patient lymphoblastoid cell lines express markedly reduced EPRS1 protein due to dual defects in nuclear export and cytoplasmic translation of variant EPRS1 mRNA," linking this specific variant to functional compromise.[1][3] Chapleau et al. summarized previously reported EPRS1-related hypomyelinating leukodystrophy cases and highlighted multiple biallelic missense variants, though the exact residues were not detailed in the search snippet.[4]

Mitsutake et al. reported the first **compound heterozygous** case and the first **exonic deletion** in EPRS1 associated with HLD15.[12][13] They described a heterozygous missense variant **c.3430 C>G; p.Leu1144Val (NM_004446.3)** located in the prolyl-tRNA synthetase domain, together with a heterozygous 220-bp deletion spanning exon 15 (**c.1743-30_1932del**).[13] RT-PCR revealed that the deletion caused exon 15 skipping, resulting in a frameshift truncating variant (p.Asn582Serfs*10) that underwent nonsense-mediated decay, leaving predominant expression of the missense allele.[13] These findings support classification of the deletion as a **loss-of-function** structural variant and the missense change as **likely pathogenic** under ACMG/AMP criteria (PM1, PM2, PM3, PP3).[13]

ClinVar’s record VCV000523133.9 lists at least one EPRS1 variant associated with "LEUKODYSTROPHY, HYPOMYELINATING, 15" and includes submissions referencing the OMIM phenotype entry and the primary literature.[14] While the specific variant in this record is not exposed in the search snippet, it likely corresponds to a missense change identified in early case reports and classified as pathogenic or likely pathogenic based on segregation and functional data.[2][4][14] Taken together, the variant spectrum in HLD15 currently comprises **missense substitutions in critical enzymatic domains** and **exonic deletions causing frameshift and nonsense-mediated decay**, all in the germline and inherited in an autosomal recessive pattern.[1][3][12][13][14]

The following table summarizes key reported EPRS1 variants associated with HLD15, alongside their domain location, zygosity, and clinical context, as derived from the supplied sources.

| Variant (cDNA / protein) | Domain / Region | Zygosity | Clinical Context | Evidence |
|---------------------------|----------------|---------|------------------|----------|
| c.4444 C>A; p.Pro1482Thr (rs930995541) | C-terminal region, likely within regulatory domain | Homozygous | Two siblings with severe cognitive and motor impairment and progressive hypomyelination (HLD15) | Khan et al. 2024 (PMID:38769304)[1][3] |
| c.3430 C>G; p.Leu1144Val (NM_004446.3) | Prolyl-tRNA synthetase domain | Heterozygous, in compound heterozygous state | 40-year-old woman with mild intellectual disability, ataxia, dystonia, MRI hypomyelination (adult-onset HLD15) | Mitsutake et al. 2026 (PMID:41721156)[12][13] |
| c.1743-30_1932del; p.Asn582Serfs*10 | Exon 15 deletion causing frameshift | Heterozygous, in compound heterozygous state | Same adult patient; variant leads to nonsense-mediated decay and functional LOF | Mitsutake et al. 2026[12][13] |
| Pathogenic missense variants (various) | Enzymatic domains | Biallelic (compound heterozygous or homozygous) | Four previously reported pediatric patients with hypomyelinating leukodystrophy | Chapleau et al. 2023[4] |
| ClinVar pathogenic variant(s) | Not specified in snippet | Likely biallelic | Associated with "LEUKODYSTROPHY, HYPOMYELINATING, 15" | ClinVar VCV000523133.9[14] |

### 4.3 Variant Classification, Allele Frequency, and Penetrance

Reported EPRS1 variants in HLD15 have been classified according to ACMG/AMP guidelines as **pathogenic** or **likely pathogenic**, based on criteria including location in critical domains (PM1), absence from general population databases (PM2), segregation with disease in families (PM3), and computational predictions supporting deleteriousness (PP3).[12][13][14] Mitsutake et al. explicitly stated that their missense variant c.3430 C>G; p.Leu1144Val was "classified as likely pathogenic under ACMG/AMP criteria (PM1, PM2, PM3, PP3)," reflecting careful adherence to guideline-based interpretation.[13] Khan et al. did not formally present ACMG criteria but described strong segregation and functional impairment for Pro1482Thr, supporting its pathogenic status.[1][3]

Allele frequencies for these variants are extremely low, consistent with the rarity of HLD15. Khan et al. referred to rs930995541 as a missense SNV present in public databases but with very low minor allele frequency, compatible with a recessive disease allele.[1][3] Mitsutake et al. implied that their missense variant was absent or extremely rare in population datasets (hence PM2), though specific gnomAD frequencies are not given in the abstract.[13] Since HLD15 is an autosomal recessive disease with severe manifestations, it is anticipated that pathogenic EPRS1 variants remain at very low frequencies in population cohorts and may exhibit regional clustering reflecting consanguinity or founder effects, although such patterns have not yet been systematically described.[2][4][9]

Penetrance appears to be **complete** for biallelic pathogenic EPRS1 variants, as all reported homozygous or compound heterozygous individuals have exhibited clinically significant neurologic phenotypes and MRI evidence of hypomyelination.[1][3][4][13] Heterozygous carriers, such as the parents and unaffected sibling in Khan et al.’s family, are clinically normal, indicating that a single functional allele suffices to maintain normal myelination.[1][3] Expressivity, however, is **variable**, as evidenced by the contrast between severe pediatric cases and the milder adult-onset case reported by Mitsutake et al., suggesting that specific variant combinations and residual enzyme activity levels modulate phenotype severity.[4][12][13] There is no evidence of genetic anticipation or germline mosaicism in HLD15, and all described cases involve classical recessive inheritance from carrier parents.[1][2][9][13]

### 4.4 Functional Consequences: Loss of EPRS1 Protein and mRNA Processing Defects

The most detailed mechanistic characterization of a pathogenic EPRS1 variant in HLD15 comes from Khan et al., who investigated the consequences of the homozygous p.Pro1482Thr missense change in patient-derived lymphoblastoid cell lines.[1][3] They found that this variant causes **dual defects in nuclear export and cytoplasmic translation of the EPRS1 mRNA**, ultimately resulting in pathologically low levels of EPRS1 protein. Their abstract states: "Patient lymphoblastoid cell lines express markedly reduced EPRS1 protein due to dual defects in nuclear export and cytoplasmic translation of variant EPRS1 mRNA."[1][3] Importantly, they identified alterations in variant-distal mRNA **m⁶A** site accessibility, mediated by the METTL3 methyltransferase, which impaired mRNA export and translation; hence the paper’s title: "Homozygous EPRS1 missense variant causing hypomyelinating leukodystrophy-15 alters variant-distal mRNA m6A site accessibility."[1][3]

The causal chain elucidated by Khan et al. can be summarized as follows. The Pro1482Thr missense change alters the conformation or interaction profile of the EPRS1 mRNA-protein complex, affecting access of METTL3 to a distal adenosine residue that is normally methylated to N\(^6\)-methyladenosine (m⁶A).[1][3] This change in m⁶A deposition results in impaired recognition by nuclear export machinery, causing retention of EPRS1 transcripts in the nucleus.[1][3] Additionally, the variant induces defects in cytoplasmic translation, further reducing protein synthesis from the mutant mRNA.[1][3] The net effect is a substantial reduction in EPRS1 protein levels in patient cells—effectively a **loss-of-function** at the protein level—even though the variant is missense rather than truncating.[1][3] This mechanism illustrates how missense variants can cause LOF through RNA processing and translational regulation, not only through direct catalytic defects.

Mitsutake et al.’s case provides complementary evidence of functional LOF from structural variants. Exon 15 deletion (c.1743-30_1932del) caused exon skipping and a frameshift variant p.Asn582Serfs*10, which underwent nonsense-mediated decay, "leaving predominant expression of the paternally inherited missense allele."[13] They concluded that "These findings support loss-of-function for the deletion and classify c.3430 C > G as likely pathogenic," reinforcing that both missense and truncating alleles can contribute to reduced EPRS1 function.[12][13] The adult-onset phenotype in this compound heterozygote suggests that residual EPRS1 activity from the missense allele may suffice to permit delayed onset and milder disease, whereas more severe LOF combinations likely produce childhood-onset, severe HLD15.[4][12][13]

At the cellular level, reduced EPRS1 protein impairs tRNA aminoacylation, leading to deficits in protein translation, particularly in cell types with high demands for myelin protein synthesis, such as oligodendrocytes. GO terms reflecting these mechanisms include **GO:0006412 (translation)**, **GO:0006368 (mRNA processing)**, and **GO:0006397 (mRNA export from nucleus)**, while the m⁶A modification is captured by terms such as **GO:0009452 (RNA modification)**.[1][3][17] In summary, EPRS1 variants in HLD15 exert their pathogenic effects largely through **loss of protein function** mediated by defects in mRNA processing and translation, leading to hypomyelination and neurologic disease.

### 4.5 Modifier Genes, Epigenetic Information, and Chromosomal Abnormalities

No specific modifier genes or epigenetic factors have been identified that modulate the severity or expression of HLD15. While Khan et al.’s work implicates METTL3-mediated m⁶A deposition in the pathogenesis of the Pro1482Thr variant, they did not report genetic variation in METTL3 or other RNA methyltransferases as contributors to disease variability.[1][3] Instead, METTL3 appears to act as a **functional partner** in a pathway perturbed by the EPRS1 variant, but not as a genetic modifier per se. Similarly, components of the nuclear export machinery and multi-aminoacyl-tRNA synthetase complex may interact with EPRS1, but their germline variation has not yet been linked to differences in HLD15 phenotype.[1][3][7]

Epigenetic profiling specific to HLD15 has not been reported, and there is no evidence for chromatin, DNA methylation, or histone modification changes unique to the disease beyond the mRNA methylation effects described above.[1][3] Chromosomal abnormalities, such as large deletions, translocations, or inversions involving the 1q41 region, have not been associated with HLD15 in the literature or OMIM.[2][9] The structural variant reported by Mitsutake et al. is an intragenic exon-level deletion within EPRS1 rather than a cytogenetically visible chromosomal rearrangement, and it is best conceptualized as a gene-level structural mutation rather than a broader chromosomal abnormality.[12][13]

Thus, at present, HLD15 appears to be driven by **gene-level mutations in EPRS1**, with no identified modifier genes or epigenetic alterations beyond the transcript-specific m⁶A changes described in the Pro1482Thr variant. Future studies employing whole-genome sequencing, epigenome profiling, and transcriptomics in larger cohorts may reveal additional layers of regulation, but such data are not yet available in the published record.

## 5. Environmental Information

### 5.1 Non-genetic Contributing Factors

Hypomyelinating leukodystrophy 15 is fundamentally a monogenic disorder and, as such, non-genetic environmental factors have not been implicated as primary causes. The literature and database entries focus exclusively on the genetic etiology in EPRS1, with no mention of environmental exposures such as toxins, radiation, or pollutants as contributing to disease onset.[1][2][4][9] This contrasts with acquired white matter disorders, where environmental factors can play a major role, but HLD15 remains firmly in the realm of inherited leukodystrophies.[1][15]

That said, general considerations about environmental influences on neurologic health still apply. For example, severe prematurity, hypoxic-ischemic injury, or nutritional deficiencies can independently affect myelin development, but these factors are not documented as co-triggers or modifiers in reported HLD15 cases.[1][3][4][13] Multi-center leukodystrophy cohorts routinely control for such confounders when attributing white matter abnormalities to genetic causes, and the segregation of EPRS1 variants in families with autosomal recessive inheritance patterns further supports a primary genetic etiology.[2][4][9]

### 5.2 Lifestyle and Infectious Factors

Lifestyle factors such as smoking, alcohol consumption, diet, and physical activity have not been studied in relation to HLD15 risk or severity. Given the typical childhood or adolescent onset of disease, many patients develop neurologic manifestations long before lifestyle factors become prominent determinants of health, and the small number of reported adult-onset cases is insufficient to draw conclusions about lifestyle-modulated phenotypic variation.[8][13] Similarly, infectious agents have not been reported as triggers or significant modifiers of HLD15, and there is no suggestion that viral or bacterial infections precipitate decompensation in the manner of some immune-mediated demyelinating disorders.[1][3][15]

For clinical care, standard recommendations regarding vaccination, infection prevention, and healthy lifestyle choices remain important for general health, but they are not currently recognized as disease-specific interventions for HLD15. In knowledge base entries, this lack of evidence should be explicitly noted, to avoid implying unsupported causal roles for environmental or lifestyle factors in this genetically determined leukodystrophy.

## 6. Mechanism and Pathophysiology

### 6.1 Aminoacyl-tRNA Synthetases and Myelination

The pathophysiology of HLD15 must be understood in the context of a broader class of leukodystrophies caused by defects in aminoacyl-tRNA synthetases (aaRS), enzymes that catalyze the charging of tRNA molecules with their cognate amino acids and are essential for protein translation.[2][6][7] Khan et al. drew attention to this group, stating: "Additionally, bi-allelic missense variants in genes encoding three other aaRSs—RARS1, DARS1, and EPRS1, cause childhood-onset HLD, specifically HLD9, HBSL (hypomyelination with brain stem and spinal cord involvement and leg spasticity), and HLD15, respectively."[1] This observation underscores the central role of aaRSs in central nervous system myelination and suggests that oligodendrocytes are particularly vulnerable to translational deficits.

RARS1-related autosomal recessive hypomyelinating leukodystrophy, as described by Orphanet, manifests with developmental delay, spasticity, ataxia, and hypomyelination of both supratentorial and infratentorial white matter.[6] DARS1-related HBSL similarly features hypomyelination with brain stem and spinal cord involvement, leg spasticity, and other neurologic impairments.[1][6] These disorders share clinical and MRI characteristics with HLD15, strengthening the inference that disrupted cytosolic tRNA aminoacylation and impaired translation in oligodendrocytes is a common pathogenic mechanism in aaRS leukodystrophies. GO terms that capture these processes include **GO:0006412 (translation)**, **GO:0006418 (tRNA aminoacylation)**, and **GO:0042552 (myelination)**, and cell types of interest include **CL:0000127 (oligodendrocyte)** and **CL:0000540 (neuron)**.

### 6.2 EPRS1 mRNA m⁶A Modifications, Nuclear Export, and Translation

The most distinctive mechanistic insight in HLD15 comes from Khan et al.’s demonstration that the Pro1482Thr variant alters **variant-distal mRNA m⁶A site accessibility**, leading to defects in nuclear export and cytoplasmic translation of EPRS1 mRNA.[1][3] They showed that the mutant EPRS1 transcript exhibits reduced methylation at a distal adenosine by METTL3, which compromises recognition by nuclear export receptors and diminishes export from the nucleus to the cytoplasm.[1][3] As a result, EPRS1 mRNA accumulates in the nucleus and is less available for translation in the cytoplasm, effectively reducing protein synthesis even though the coding sequence encodes a full-length protein.[1][3]

Their abstract emphasizes this dual defect: "Patient lymphoblastoid cell lines express markedly reduced EPRS1 protein due to dual defects in nuclear export and cytoplasmic translation of variant EPRS1 mRNA."[1][3] Furthermore, they highlight that the variant affects **m⁶A site accessibility** at a location distant from the variant itself, illustrating that missense changes can exert long-range effects on RNA structure and post-transcriptional modifications.[1][3] This mechanism integrates several molecular pathways: mRNA transcription, RNA modification (m⁶A), nuclear export, and translation, each of which is vital for robust protein production. GO terms relevant to this chain include **GO:0006397 (mRNA processing)**, **GO:0006406 (mRNA export from nucleus)**, and **GO:0009452 (RNA modification)**.

This mechanistic model situates EPRS1 at an intersection of translational control and RNA epigenetics, and suggests that oligodendrocytes may be particularly sensitive to EPRS1 shortages during developmental windows of active myelination. Diminished EPRS1 levels would lead to reduced charging of tRNA\(^\text{Glu}\) and tRNA\(^\text{Pro}\), impairing synthesis of proteins rich in these amino acids, which may include key myelin structural proteins and enzymes required for lipid synthesis.[1][3][7] The impact may be amplified by the cell’s inability to compensate via other aaRSs, leading to selective vulnerability in white matter tracts.

### 6.3 Consequences for Oligodendrocytes and Myelin

While direct studies of oligodendrocyte biology in HLD15 are not yet reported, the clinical and MRI phenotype strongly suggests that oligodendrocytes are the primary cell type affected. Hypomyelinating leukodystrophies are characterized by insufficient formation and maintenance of myelin sheaths around CNS axons, a process driven by oligodendrocytes that depends on high-level synthesis of myelin proteins such as myelin basic protein (MBP) and proteolipid protein 1 (PLP1), as well as complex lipid biosynthesis.[1][15] Translational capacity in oligodendrocytes must be robust to meet this demand, making them particularly vulnerable to aaRS dysfunction.

In HLD15, reduced EPRS1 protein likely impairs global translation in oligodendrocytes, disrupting myelin production and leading to diffuse hypomyelination of white matter tracts, as seen on MRI.[1][3][8][13] The thin corpus callosum noted in PanelApp’s description indicates that callosal axons, which are heavily myelinated, are especially affected, consistent with oligodendrocyte dysfunction across midline commissural fibers.[8] Over time, chronic hypomyelination may lead to secondary axonal damage, contributing to progressive motor and cognitive impairment.

Cell ontology terms relevant to this pathophysiology include **CL:0000127 (oligodendrocyte)**, **CL:0000540 (neuron)**, and **CL:0000120 (astrocyte)**, as glial-neuronal interactions are crucial for myelin formation. GO biological process terms such as **GO:0042552 (myelination)**, **GO:0007272 (ensheathment of neurons)**, and **GO:0019226 (transmission of nerve impulse)** capture the downstream functional consequences of myelin deficits. In this causal chain, EPRS1 LOF is an upstream event leading to translational deficits in oligodendrocytes, which in turn cause hypomyelination, axonal dysfunction, and clinical neurologic manifestations.

### 6.4 Upstream vs Downstream Mechanisms and Tissue Damage

In the pathophysiologic hierarchy of HLD15, **EPRS1 gene mutation** is the upstream initiating event, triggering a cascade of molecular and cellular abnormalities. At the molecular level, downstream effects include altered mRNA m⁶A modifications, defective nuclear export, impaired translation, and depletion of EPRS1 protein.[1][3][12][13] At the cellular level, oligodendrocytes fail to produce sufficient myelin, leading to structural deficits in white matter tissue, as documented by MRI.[1][8][13] Beyond this, downstream mechanisms may include axonal degeneration due to lack of trophic support from myelin, synaptic dysfunction, and neurodevelopmental anomalies affecting cortical and subcortical circuits.

Tissue damage in HLD15 is characterized not by acute necrosis or inflammation but by **developmental hypomyelination**, a failure to fully myelinate axons, resulting in persistent white matter immaturity.[1][15] Steenweg et al.’s MRI pattern recognition study distinguishes hypomyelinating disorders by their homogeneously abnormal white matter signal without focal lesions, cavitations, or contrast enhancement typical of inflammatory demyelinating diseases.[15] Thus, in HLD15, tissue damage is best conceptualized as **non-inflammatory, non-ischemic structural underdevelopment**, though secondary degenerative changes may occur over time.

Immune system involvement in HLD15 has not been reported, and there is no evidence of autoimmunity, immunodeficiency, or chronic inflammation driving disease progression.[1][3][4][13][15] Biochemical abnormalities, beyond EPRS1 LOF, have not been systematically characterized, but given the central role of EPRS1 in aminoacylation, metabolic changes in amino acid usage and protein synthesis are likely. CHEBI terms related to glutamic acid (CHEBI:16015) and proline (CHEBI:26209) may be relevant for capturing the biochemical context, although direct metabolomic profiling in HLD15 is not available in the current literature.

### 6.5 Molecular Profiling and Advanced Technologies

Khan et al.’s study likely employed transcriptomic approaches (RNA-seq) to characterize mRNA export and translation defects, although the search snippet does not detail the methods. They investigated m⁶A site accessibility and METTL3-mediated methylation in EPRS1 transcripts, which would require advanced molecular profiling techniques such as MeRIP-seq (methylated RNA immunoprecipitation sequencing) or CLIP-seq.[1][3] Their findings represent a form of functional genomics analysis that identifies specific alterations in RNA processing and modification associated with a pathogenic variant.

Beyond this, there are no reports of comprehensive multi-omics studies in HLD15, such as large-scale transcriptomics, proteomics, metabolomics, or lipidomics performed on patient brain tissue or induced pluripotent stem cell (iPSC)-derived oligodendrocytes. Single-cell analysis, spatial transcriptomics, and CRISPR-based functional screens have not yet been applied to EPRS1-related hypomyelinating leukodystrophy.[1][3][4][13] However, given the central role of translation and RNA modification in the disease, future applications of single-cell RNA-seq and spatial transcriptomics in model systems or patient-derived cells could reveal cell-type-specific vulnerabilities and regional heterogeneity in the CNS.

In the absence of such data, annotations in knowledge bases should focus on the mechanistic insights available—namely, the mRNA m⁶A/nuclear export/translation pathway—and note that comprehensive molecular profiling is currently lacking. This will help guide future research priorities and inform the development of more nuanced disease models that integrate multi-omics data when available.

## 7. Anatomical Structures Affected

### 7.1 Organ-Level Involvement: Central Nervous System

Hypomyelinating leukodystrophy 15 primarily affects the **central nervous system (CNS)**, with particular involvement of cerebral white matter, corpus callosum, and possibly cerebellar and brainstem tracts. Brain MRI in HLD15 shows diffuse hypomyelination of supratentorial white matter, reflected in homogeneous T2-weighted hyperintensity and reduced myelin-related signal, as well as structural thinning of the corpus callosum.[1][8][13][15] PanelApp explicitly notes that "Brain imaging shows hypomyelinating leukodystrophy with thin corpus callosum," indicating a characteristic involvement of this midline structure.[8] UBERON terms relevant to these anatomical structures include **UBERON:0000955 (brain)**, **UBERON:0002435 (corpus callosum)**, and **UBERON:0002037 (cerebral white matter)**.

Cerebellar and brainstem involvement has not been specifically detailed for HLD15 in the supplied sources, but by analogy with other hypomyelinating leukodystrophies, it is plausible that infratentorial white matter tracts may also show hypomyelination.[6][15] Orphanet’s description of RARS-related hypomyelinating leukodystrophy notes "supratentorial and infratentorial hypomyelination," suggesting that aaRS-related disorders can affect both cerebrum and cerebellum.[6] Steenweg et al. identified MRI clusters characterized by pontine and cerebellar signal abnormalities in specific hypomyelinating disorders, though HLD15 was not directly included.[15] In future MRI analyses of HLD15, annotating involvement of structures such as **UBERON:0002037 (cerebral white matter)**, **UBERON:0002280 (cerebellar white matter)**, and **UBERON:0002185 (brainstem)** will aid pattern recognition.

Peripheral nervous system involvement has not been reported, and clinical features such as spasticity, dystonia, and ataxia are best explained by central white matter and corticospinal tract involvement rather than peripheral nerve pathology.[1][3][4][8][13] Other organ systems—cardiovascular, respiratory, gastrointestinal—are not directly affected by HLD15, although complications such as aspiration pneumonia can occur secondary to dysphagia, and reduced mobility can affect cardiometabolic health. From an anatomical ontology perspective, the primary body system involved is the **nervous system (UBERON:0001016)**, with secondary impacts on musculoskeletal function and sensory organs (eyes and ears) due to optic atrophy and hearing loss.[8]

### 7.2 Tissue and Cell-Level Involvement

At the tissue level, HLD15 predominantly involves **white matter**, composed of myelinated axons and glial cells, especially oligodendrocytes. Histopathologic studies specific to HLD15 have not been published, but general leukodystrophy pathology shows reduced myelin density, oligodendrocyte abnormalities, and relatively preserved gray matter, consistent with the MRI pattern.[1][15] Tissue ontology terms such as **UBERON:0002067 (cerebral cortex)** and **UBERON:0002037 (cerebral white matter)** can capture the distribution of involvement.

Cell-level involvement centers on **oligodendrocytes (CL:0000127)**, which produce myelin in the CNS and depend heavily on translational capacity to synthesize myelin proteins and lipids.[1][3][6][15] Neurons (CL:0000540) are indirectly affected by hypomyelination, as the lack of myelin impairs action potential conduction and may lead to axonal degeneration, but there is no evidence that neuronal intrinsic defects drive the disease.[1][15] Astrocytes (CL:0000120) and microglia (CL:0000129) may respond to white matter pathology, but HLD15 is not characterized by inflammatory gliosis or demyelination, distinguishing it from acquired inflammatory disorders.[1][15]

In knowledge base entries, cell ontology annotations should emphasize oligodendrocytes as the primary cell type, with neurons as secondary targets and astrocytes/microglia as possible responders. Biological process GO terms such as **GO:0042552 (myelination)** and **GO:0007272 (ensheathment of neurons)** are appropriate. These annotations will support modeling of cell-type-specific mechanisms in future studies.

### 7.3 Subcellular Localization and Structures

At the subcellular level, HLD15 pathophysiology involves multiple compartments, including **nucleus**, **cytoplasm**, and **ribosomes**, reflecting the pathways of mRNA processing and translation. UniProt and ZFIN note that EPRS1 is predicted to be active in the **cytoplasm**, consistent with its role as a cytosolic aminoacyl-tRNA synthetase and its participation in the multi-aminoacyl-tRNA synthetase complex.[11][17] GO cellular component terms that capture this include **GO:0005829 (cytosol)** and **GO:0005840 (ribosome)**. However, Khan et al.’s work highlights the importance of **nuclear** processes, as variant EPRS1 mRNA shows defective export from the nucleus, making **GO:0005634 (nucleus)** a relevant component.[1][3]

The causal chain involves transcription of EPRS1 mRNA in the nucleus, m⁶A modification by METTL3, nuclear export of the transcript, and cytoplasmic translation on ribosomes, with EPRS1 protein then localizing to the cytosol where it aminoacylates tRNAs.[1][3][17] Defects at any step can contribute to reduced EPRS1 protein levels. Subcellular structures such as **nuclear pore complexes**, **RNA granules**, and **translation initiation complexes** may be involved, though these have not been directly studied in HLD15. Cellular component GO terms such as **GO:0005737 (cytoplasm)**, **GO:0005654 (nucleoplasm)**, and **GO:0005840 (ribosome)** can be used to annotate these aspects.

### 7.4 Localization and Lateralization in the CNS

White matter abnormalities in HLD15 are **bilateral**, affecting both hemispheres, as hypomyelination is a diffuse process rather than a focal lesion.[1][8][13][15] The thin corpus callosum indicates midline involvement, but there is no evidence for lateralization such as left-right asymmetry or predilection for specific lobes.[8] Steenweg et al.’s cluster analysis of hypomyelinating disorders showed patterns that involve symmetric abnormalities of cerebral white matter, basal ganglia, and brainstem structures, supporting the concept of bilateral and systemic involvement.[15]

Specific anatomical sites, such as **UBERON:0000955 (brain)**, **UBERON:0002435 (corpus callosum)**, **UBERON:0002037 (cerebral white matter)**, and **UBERON:0002280 (cerebellar white matter)**, should be annotated to capture the distribution of pathology. These annotations will support imaging-based decision support and pattern recognition tools that rely on mapping MRI findings to disease entities.

## 8. Temporal Development

### 8.1 Onset Patterns

HLD15 typically presents with an **insidious** onset of neurologic symptoms in childhood or adolescence, consistent with its classification as a neurodevelopmental disorder. PanelApp notes that "Onset of motor and cognitive impairment [in EPRS-related leukodystrophy] [occurs] in the first or second decade of life," indicating that many patients develop symptoms during school-age years.[8] Khan et al.’s siblings had severe cognitive and motor impairment and progressive hypomyelination, implying early childhood onset, though the exact age is not provided.[1][3] The disease is chronic rather than acute, with signs emerging gradually as developmental milestones are missed or regressed.[1][3][4]

Mitsutake et al.’s case demonstrates that **adult-onset** HLD15 is possible, with clinical manifestations recognized at age 40 in a woman with mild intellectual disability and cerebellar signs.[13] This suggests that, in some individuals with residual EPRS1 function, developmental myelination is sufficient to prevent early severe disease, and symptoms may be delayed until later adulthood, perhaps as compensatory mechanisms fail or cumulative microstructural damage manifests clinically.[12][13] Overall, onset patterns range from childhood to mid-adulthood, with chronic, insidious development rather than acute episodes.

### 8.2 Disease Progression and Course

HLD15 follows a **chronic, progressive** course, with neurologic impairment tending to worsen over years and MRI showing persistent hypomyelination that may become more pronounced over time. Khan et al. refer to "progressive hypomyelination characteristic of HLD" in their siblings, indicating that both radiologic and clinical features advanced over the observation period.[1][3] Serial MRI is recommended to monitor disease course, as noted in their statement that "patient management includes serial brain MRI to monitor hypomyelination, genetic testing

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