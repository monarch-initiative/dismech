---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-08-23T15:38:02.031720'
end_time: '2026-08-23T15:42:06.860128'
duration_seconds: 244.83
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neutrophil immunodeficiency syndrome (immunodeficiency 73A with defective
    neutrophil chemotaxis and leukocytosis), caused by dominant-negative RAC2 mutations
  mondo_id: MONDO:0011988
  category: Immunological / inborn error of immunity
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
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 5
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neutrophil immunodeficiency syndrome (immunodeficiency 73A with defective neutrophil chemotaxis and leukocytosis), caused by dominant-negative RAC2 mutations
- **MONDO ID:** MONDO:0011988 (if available)
- **Category:** Immunological / inborn error of immunity

## Research Objectives

Please provide a comprehensive research report on **Neutrophil immunodeficiency syndrome (immunodeficiency 73A with defective neutrophil chemotaxis and leukocytosis), caused by dominant-negative RAC2 mutations** covering all of the
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

# Neutrophil Immunodeficiency Syndrome (Immunodeficiency 73A with Defective Neutrophil Chemotaxis and Leukocytosis) Caused by Dominant-Negative RAC2 Mutations

Neutrophil immunodeficiency syndrome, formally classified as **immunodeficiency 73A with defective neutrophil chemotaxis and leukocytosis (IMD73A)**, is a rare inborn error of immunity caused by dominant-negative mutations in the hematopoietic-specific small Rho GTPase **RAC2**.[11][13][9] This disorder is characterized by early-onset, severe, recurrent bacterial infections, impaired wound healing, and a striking functional defect of neutrophils despite often normal or elevated neutrophil counts.[10][15][18] The best-characterized pathogenic allele is the missense variant **RAC2 c.169G>A (p.Asp57Asn; D57N)**, which produces a mutant protein that fails to bind GTP and exerts a dominant-negative effect on RAC2-dependent signaling, including chemotaxis and NADPH oxidase activation.[10][12][15] Clinically, the syndrome resembles leukocyte adhesion deficiency (LAD), with neutrophilia and poor neutrophil recruitment to tissues, and has been termed LAD type IV in some literature.[10][14] More recent work has expanded the clinical and functional spectrum of RAC2-related immunodeficiency, delineating a continuum from severe combined immunodeficiency (SCID) due to constitutively active mutations, through LAD-like disease due to dominant-negative mutations such as D57N, to later-onset combined immunodeficiency caused by dominant-activating variants.[6][7] The present report focuses specifically on IMD73A due to dominant-negative RAC2 mutations, integrating clinical, genetic, mechanistic, and model-organism data to support ontology-driven disease representation for knowledge base applications.

## 1. Disease Information

### 1.1 Nosology and Conceptual Overview

Immunodeficiency 73A with defective neutrophil chemotaxis and leukocytosis (IMD73A) is an **autosomal dominant primary immunodeficiency** in which the central biological defect is impaired migration and effector function of neutrophils, resulting in increased susceptibility to bacterial infection and poor tissue repair.[11][13][10] The condition is caused by germline heterozygous mutations in **RAC2**, a hematopoietic-specific member of the Rac subfamily of small Rho GTPases that orchestrates actin cytoskeleton dynamics and NADPH oxidase activation in leukocytes.[6][12][16] Clinically, affected infants present with recurrent, often severe bacterial infections, particularly involving skin, soft tissue, and mucosal sites, accompanied by **neutrophilia and leukocytosis** in the peripheral blood but defective chemotaxis toward chemoattractants such as formyl-Met-Leu-Phe (fMLP).[10][11][18] The syndrome is sometimes referred to as **neutrophil immunodeficiency syndrome**, emphasizing the dominant involvement of neutrophil dysfunction, although more recent work has shown that other leukocyte lineages can be affected to varying degrees in different RAC2 mutation classes.[6][7][15]

Conceptually, IMD73A sits at the intersection of disorders of phagocyte function and combined immunodeficiencies. Classic phagocyte disorders such as chronic granulomatous disease (CGD) are defined by defective oxidative burst and microbial killing; in IMD73A, NADPH oxidase activation is impaired in response to specific pathways, but the most distinctive feature is abnormal neutrophil motility and tissue recruitment rather than absolute deficiency of oxidative burst.[10][12][16] At the same time, RAC2 is expressed broadly in hematopoietic cells, and detailed clinical series have revealed lymphopenia and hypogammaglobulinemia in many RAC2-mutant patients, particularly those with constitutively active or activating variants.[6][7] Thus, although the **Mondo Disease Ontology** term **MONDO:0011988** encompasses neutrophil immunodeficiency syndrome, it is increasingly recognized as part of a broader **RAC2-related immunodeficiency spectrum**, with IMD73A representing the LAD-like, neutrophil-dominant subset caused by **dominant-negative** mutations.[6][9]

### 1.2 Identifiers, Synonyms, and Classification

The disorder has been catalogued in multiple biomedical classification systems. In **OMIM**, the condition is listed as **#608203 – Immunodeficiency 73A with defective neutrophil chemotaxis and leukocytosis (IMD73A)**, with inheritance specified as autosomal dominant.[11][13] Genetic Testing Registry (GTR) and ClinGen resources refer to the same entity as **neutrophil immunodeficiency syndrome** and **autosomal dominant immunodeficiency 73B with defective neutrophil chemotaxis**, reflecting some variation in naming but consistently linking the phenotype to **RAC2-related defects of neutrophil migration**.[4][9] Orphanet recognizes a broader category of **RAC2-related combined immunodeficiency–bronchiectasis–cancer-predisposing syndrome (ORPHA:692812)**, which includes patients with activating mutations and combined immunodeficiency; within this umbrella, IMD73A is one of several RAC2-associated immunologic disorders.[3][6]

Common synonyms and alternative names used in the literature include **neutrophil immunodeficiency syndrome**, **RAC2-related neutrophil dysfunction**, **leukocyte adhesion deficiency type IV (LAD-IV)**, and **RAC2 dominant-negative immunodeficiency**.[10][14][15] The LAD-IV designation arises because RAC2 D57N patients present with clinical and laboratory features reminiscent of classical LAD, including recurrent bacterial infections, poor wound healing, and marked neutrophilia, but they lack integrin defects at the cell surface and instead show impaired small GTPase signaling.[10][14] Human Phenotype Ontology (HPO) captures several core manifestations under terms such as **“Neutrophil migratory defect” (HP:0040238)**, defined as an impairment of neutrophil migration toward chemoattractants, and **“Increased susceptibility to infections” (HP:0002719)**, defined as recurrent infections affecting various organs.[8][17]

The information summarized here is derived predominantly from **aggregated disease-level resources and published clinical case series**, rather than raw electronic health record data.[6][10][11][15][18] OMIM entries integrate curated case reports and functional studies; ClinGen publications provide systematic gene–disease validity assessments; and recent case series and case reports in the hematology and immunology literature define the clinical spectrum and mechanistic correlates.[6][7][15] Model organism data from Rac2-deficient mice and zebrafish further support the disease concept by demonstrating that perturbation of RAC2 signaling in neutrophils recapitulates key features of the human syndrome.[1][10][12][16]

## 2. Etiology and Risk Architecture

### 2.1 Genetic Causal Factors

The primary etiological factor in neutrophil immunodeficiency syndrome (IMD73A) is the presence of **heterozygous germline mutations in RAC2** that act in a **dominant-negative** fashion to disrupt RAC2-mediated signaling pathways in neutrophils and other leukocytes.[6][10][15] RAC2 encodes **Rac family small GTPase 2**, a hematopoietic cell–specific member of the Rho GTPase family that cycles between an inactive GDP-bound state and an active GTP-bound state in response to guanine nucleotide exchange factors (GEFs).[6][12][16] Dominant-negative mutations, most notably **p.Asp57Asn (D57N)**, impair GTP binding and stabilize RAC2 in an inactive conformation that can **sequester GEFs**, thereby interfering not only with wild-type RAC2 but also with other GTPases that use the same GEFs, including RAC1.[1][6][10][15] As Williams et al. reported, “Dominant negative mutation of the hematopoietic-specific Rho GTPase, Rac2, is associated with a human phagocyte immunodeficiency,” implicating the D57N allele as causative in a familial neutrophil defect.[1][10]

The **D57N** variant has been identified in multiple unrelated infants presenting with severe bacterial infections, impaired wound healing, and defective neutrophil chemotaxis, with functional assays demonstrating a failure of the mutant protein to bind GTP and to support downstream signaling.[10][15][18] In a landmark series of RAC2-related immunodeficiency, “The first RAC2 mutation, D57N, was identified in an infant with severe bacterial infections, impaired wound healing, and defective neutrophil chemotaxis,” and the mutant protein “acted in a dominant-negative manner, failing to bind GTP.”[6] Subsequent newborn screening identified another infant with the same mutation and similar presentation, and more recent broader cohorts have documented additional individuals with dominant-negative RAC2 variants, all clustering in functional motifs critical for nucleotide binding and GTPase activity.[6][15][18]

ClinGen’s gene–disease validity curation concluded that there is **strong evidence** linking RAC2 mutations to autosomal dominant immunodeficiency with defective neutrophil chemotaxis, based on multiple unrelated probands, consistent segregation, and robust functional data demonstrating impaired Rac2 activity and neutrophil function.[9][10][12] Importantly, the **dominant-negative mechanism** distinguishes IMD73A from RAC2 loss-of-function phenotypes: Rac2-null mice display significant chemotactic and oxidative burst defects, but human D57N mutants exert broader inhibitory effects through GEF sequestration and interference with RAC1, leading to a more complex disturbance of leukocyte migration and retention.[1][10][12][16] There is no evidence that environmental factors alone can cause IMD73A in the absence of such genetic mutations, underscoring its classification as a monogenic inborn error of immunity.[6][11][13]

### 2.2 Genetic Risk Factors Beyond Causal Variants

Because IMD73A is an **autosomal dominant** disorder with high penetrance in mutation carriers, traditional notions of genetic susceptibility loci or polygenic risk factors play a minor role in its etiology.[11][13][9] The presence of a pathogenic dominant-negative **RAC2** variant is sufficient to confer a very high risk of disease, and at present there is no evidence from genome-wide association studies or population-based sequencing that common polymorphisms in RAC2 or interacting genes modulate susceptibility to IMD73A in the general population.[6][9] Population databases such as gnomAD have reported extremely low allele frequencies for known pathogenic RAC2 variants, consistent with strong negative selection and the rarity of the condition, although specific frequency data for D57N and related alleles are not detailed in the available search results.[6][15]

However, within the broader **RAC2-related immunodeficiency spectrum**, there is emerging evidence that **dosage and zygosity** can influence phenotype. A 2026 case report described two unrelated French-Canadian patients homozygous for **RAC2 c.202C>T (p.Arg68Trp, R68W)**, a variant previously noted among RAC2 disease-associated alleles.[7] Despite markedly reduced RAC2 protein expression, patient-derived cells exhibited **increased effector signaling** in the homozygous state, producing a phenotype that phenocopies dominant gain-of-function RAC2 variants.[7] The authors concluded that “functional hyperactivation was not observed in heterozygous cells, supporting a dosage-dependent mechanism,” and they emphasized that homozygous R68W can cause combined immunodeficiency with features such as bronchiectasis and neoplasms.[7] Although R68W is an **activating** rather than dominant-negative mutation, its dosage-sensitive behavior illustrates that **allelic series and genetic context** can modulate RAC2-related disease expression.

For IMD73A specifically, no modifier genes have been definitively identified, but it is plausible that variants in genes encoding RAC2 regulators (such as specific GEFs, GTPase-activating proteins, or scaffold proteins) or downstream effectors (e.g., components of the NADPH oxidase complex) could modulate the severity of neutrophil dysfunction, infection susceptibility, or response to therapy.[6][12][16] At present, this remains speculative and is not supported by direct human genetic data in the available literature, and therefore such potential modifiers should be treated as hypotheses rather than established risk factors.

### 2.3 Environmental and Lifestyle Risk Factors

There is **no evidence** that environmental exposures, toxins, or lifestyle factors can cause neutrophil immunodeficiency syndrome in the absence of a pathogenic RAC2 mutation, and thus environmental factors are best understood as **modifiers of clinical course** rather than primary etiologic agents.[6][11][13] As with other immunodeficiencies, the **burden and spectrum of infections** experienced by an affected individual depend heavily on environmental microbial exposure, hygiene, vaccination status, and access to antimicrobial prophylaxis.[6][7] For example, one patient with RAC2-related combined immunodeficiency developed early bronchiectasis due to recurrent bacterial respiratory infections; this complication likely reflected both underlying immunologic vulnerability and environmental exposure to respiratory pathogens.[7] However, such observations do not indicate that environment plays a role in the genesis of the disease itself.

Lifestyle factors such as **smoking, nutrition, and physical activity** might influence the severity of infections and tissue healing, particularly in older patients or those with chronic lung disease, but no systematic data specific to IMD73A have been reported.[3][6][7] Similarly, occupational exposures, pollution, or radiation could theoretically exacerbate infection risk or organ damage in immunodeficient individuals, but again, there are no specific studies addressing these questions in RAC2-mutant patients. Given the extreme rarity of the condition and the predominance of pediatric cases, robust epidemiologic studies of environmental risk are unlikely to be feasible, and clinical management focuses instead on minimizing infection exposure and providing prompt antimicrobial therapy.[6][7][15]

### 2.4 Protective Factors and Gene–Environment Interactions

Protective factors for IMD73A are best conceived in terms of **therapeutic interventions** rather than intrinsic biological resistance. Immunoglobulin replacement, antibiotic prophylaxis, and hematopoietic cell transplantation can significantly mitigate infection risk and improve long-term outcomes, functioning as secondary or tertiary preventive measures in affected individuals.[6][7] There is no evidence of **protective genetic variants** that counteract the effects of dominant-negative RAC2 mutations, and given the strong impact of these alleles on core signaling pathways, such protection would likely require profound upregulation of compensatory mechanisms (e.g., RAC1 activity) that has not been observed in human cohorts.[6][12][15][16] 

Gene–environment interactions in IMD73A are therefore primarily **clinical and management-related**: early recognition of the disease through newborn screening or family history allows for the implementation of protective environmental strategies (such as infection control measures and prophylactic antimicrobials), which in turn reduce the frequency and severity of infections, even though they do not alter the underlying genetic defect.[6][7][18] For example, in the case identified through newborn screening, early diagnosis enabled careful monitoring and supportive care, potentially altering the trajectory of disease compared to late-diagnosed individuals.[6][18] These interactions are crucial for prognosis and quality of life but do not imply that environment modifies genetic penetrance in a mechanistically fundamental way.

## 3. Clinical Phenotypes and Natural History

### 3.1 Core Immunologic and Hematologic Phenotypes

The hallmark clinical phenotype of neutrophil immunodeficiency syndrome (IMD73A) is **early-onset recurrent bacterial infections** in the context of **leukocytosis and neutrophilia** but **defective neutrophil chemotaxis and migration**.[10][11][13][18] OMIM’s clinical synopsis for IMD73A emphasizes recurrent infections beginning in infancy, defective neutrophil chemotaxis, and leukocytosis as defining features, consistent across reported cases.[11][13] Human Phenotype Ontology terms capturing these manifestations include **“Increased susceptibility to infections” (HP:0002719)**, **“Recurrent bacterial infections” (HP:0002719 subtypes)**, and **“Neutrophil migratory defect” (HP:0040238)**.[8][17] In functional terms, the neutrophil migratory defect manifests as diminished directional movement toward chemoattractants, impaired polarization and lamellipodia formation, and reduced motility in three-dimensional tissue environments.[10][12][18]

Clinical case reports of RAC2 D57N patients describe severe **bacterial skin and soft tissue infections**, including deep abscesses, cellulitis, and poor wound healing after trauma or surgery.[10][15][18] One infant with D57N presented with severe bacterial infections and impaired wound healing, with functional assays demonstrating absent or drastically impaired chemotaxis to fMLP and markedly reduced respiratory burst in response to fMLP stimulation.[6][10][18] Another patient identified through newborn screening showed similar neutrophil defects and recurrent infections, confirming the reproducibility of the phenotype.[6][18] Importantly, these infections occur despite **elevated peripheral neutrophil counts**, underscoring that the defect lies in neutrophil function rather than production.[10][11][14]

Leukocytosis and neutrophilia in IMD73A mirror features of leukocyte adhesion deficiency, in which leukocytes fail to adhere to and transmigrate through endothelium, resulting in accumulation in the bloodstream.[10][14] In zebrafish models expressing inhibitory Rac2D57N specifically in neutrophils, investigators observed a **tenfold increase in circulating neutrophils** compared with controls, indicating increased mobilization from hematopoietic tissue and defective retention.[10] They concluded that “ectopic expression of Rac2D57N in neutrophils is sufficient to cause a neutrophil immunodeficiency in transgenic zebrafish, establishing RAC2D57N as the causative mutation in the primary human immunodeficiency LAD type IV.”[10] This experimental phenotype aligns closely with human IMD73A and supports the designation of LAD-like disease.

The severity of infections in IMD73A is generally **moderate to severe**, often requiring hospitalization and intravenous antibiotics, and may be complicated by chronic tissue damage if not adequately controlled.[6][10][15][18] However, the number of reported cases remains small, and the full range of severity is not yet fully characterized. Some individuals may experience relatively milder courses under intensive prophylaxis, whereas others develop life-threatening sepsis or organ damage. Nonetheless, given the basic defect in neutrophil migration and killing, the **default assumption** is that IMD73A represents a serious immunodeficiency requiring vigilant management.

### 3.2 Infectious Susceptibility and Wound Healing

The **infectious profile** of IMD73A is dominated by **bacterial pathogens**, particularly those causing skin, soft tissue, and mucosal infections.[6][10][15][18] Reported patients have experienced recurrent cellulitis, deep abscesses, omphalitis, and poor wound healing, reflecting impaired neutrophil recruitment and function at sites of tissue injury.[10][15][18] In experimental models, **rac2^-/-^ zebrafish larvae** are highly susceptible to infection with **Pseudomonas aeruginosa** and **Aspergillus fumigatus**, with defects in neutrophil and macrophage motility leading to decreased recruitment to tissue wounds and infections.[1] The authors noted that “rac2^-/- larvae are highly susceptible to infection with Pseudomonas aeruginosa which can be almost fully rescued by ectopic expression of either Rac2 or Rac1 specifically in neutrophils,” demonstrating that defective Rac2-dependent motility is sufficient to confer susceptibility to opportunistic pathogens.[1]

These findings underscore that RAC2 dysfunction compromises both **innate immune responses to bacterial and fungal pathogens** and **wound healing**, which depends on timely neutrophil and macrophage recruitment.[1][10][16] In human IMD73A, the impaired wound healing is clinically significant: patients may show delayed closure of surgical incisions, persistent drainage from wounds, and exaggerated inflammatory reactions that fail to resolve.[10][15] This phenotype can be captured by HPO terms such as **“Impaired wound healing” (HP:0004220)**, although this specific term is not explicitly cited in the available search results; its conceptual relevance is clear from case descriptions.[6][10][15]

Susceptibility to viral or fungal infections appears less prominent in IMD73A than in combined immunodeficiency forms of RAC2 disease, but some patients have experienced opportunistic infections, particularly when other immune compartments are compromised.[6][7] For example, in the homozygous R68W activating mutation cases, one patient developed severe treatment-refractory cutaneous viral infections and later gynecologic and anal neoplasms associated with chronic viral disease, highlighting that when RAC2 signaling is hyperactive or broadly perturbed, adaptive immunity and cancer surveillance may also be affected.[7] By contrast, D57N-driven IMD73A appears more focused on **neutrophil-mediated antibacterial defense**, although more extensive cohorts would be needed to rule out subtle defects in other compartments.

### 3.3 Laboratory Abnormalities and Functional Phenotypes

The laboratory signature of IMD73A includes **leukocytosis with neutrophilia**, **defective neutrophil chemotaxis**, and **abnormal oxidative burst in response to specific stimuli**, particularly fMLP.[10][11][12][16][18] Routine blood counts typically show elevated total leukocytes and neutrophils, with normal or slightly altered lymphocyte and monocyte counts; platelet and red blood cell indices are generally normal unless secondary effects such as chronic disease anemia are present.[10][11] Flow cytometry of surface markers reveals normal expression of adhesion molecules (e.g., integrins), distinguishing IMD73A from classical LAD, in which integrin expression is reduced or absent.[10][14]

Functional assays are critical for diagnosis. In D57N patients, **chemotaxis assays to fMLP** show markedly reduced migration, often “absent or drastically impaired,” and **respiratory burst assays** demonstrate severely reduced superoxide production in response to fMLP stimulation.[6][10][18] Interestingly, responses to other stimuli, such as phorbol ester, may be partially preserved, reflecting the agonist-specific role of Rac2 in NADPH oxidase activation.[12][16] In Rac2-deficient murine neutrophils, investigators observed “agonist-specific defects in neutrophil functions including chemoattractant-stimulated filamentous actin polymerization and chemotaxis, and superoxide production elicited by phorbol ester, fMLP, or IgG-coated particles, despite expression of the highly homologous Rac1 isoform.”[16] These mouse data parallel human IMD73A and support the use of **fMLP-stimulated chemotaxis and respiratory burst** as phenotypic assays.

Human neutrophils utilize RAC1 and RAC2 differentially depending on chemoattractant concentration. Zhang et al. reported that “both Rac1 and Rac2 are required for normal neutrophil chemotaxis and motility in response to formyl peptides, while only Rac2 is absolutely required for fMLP-stimulated NADPH oxidase activity.”[12] They showed that at low fMLP concentrations, Rac1 activation is sufficient for chemotaxis, whereas at high concentrations, Rac2 activation is required for continuous expansion of the leading-edge lamellipodium and superoxide generation.[12] In this context, dominant-negative RAC2 mutations such as D57N selectively disrupt **high-concentration chemoattractant responses**, impairing efficient migration into sites of intense inflammation and bacterial invasion, and compromising oxidative killing.[10][12] The HPO term **“Abnormal neutrophil chemotaxis” (as part of HP:0040238)** is thus directly grounded in these functional abnormalities.[8][12]

### 3.4 Quality of Life Impact

Although data on long-term quality of life in IMD73A are limited due to the rarity of the condition, extrapolation from case descriptions and related RAC2 immunodeficiencies suggests that **daily functioning and well-being can be substantially affected**, particularly if infections are frequent or severe.[6][7][10][15] Recurrent hospitalizations for bacterial infections, repeated courses of antibiotics, and the need for surgical drainage of abscesses impose significant physical and psychological burdens on patients and families, especially when symptoms begin in infancy.[6][10] Pain, fatigue, and limitations in physical activity during acute infections can interfere with normal developmental milestones in children and with schooling and social participation in older individuals.

In patients with broader RAC2-related combined immunodeficiency, chronic lung disease such as bronchiectasis, persistent viral skin disease, and progressive organ involvement (e.g., kidney dysfunction due to light-chain deposition disease) further compromise quality of life.[7] The 2026 R68W case report described complex multidisciplinary management including immunoglobulin therapy, oncologic surveillance, and eventually hematopoietic cell transplantation, which, while improving immunologic function, entailed substantial treatment-related morbidity.[7] These experiences highlight the importance of **comprehensive supportive care**, psychological support, and long-term monitoring in RAC2-related disorders, including IMD73A.

Quality-of-life instruments such as SF-36 or EQ-5D have not, to our knowledge, been systematically applied to IMD73A cohorts, but disease-specific assessments could capture domains such as physical functioning, pain, emotional well-being, and social participation. From an ontology perspective, these impacts are relevant to **International Classification of Functioning, Disability and Health (ICF)** constructs, even though specific ICF codes are beyond the scope of the current search results. Clinicians should be aware that even when infections are controlled, the chronic reality of living with a rare immunodeficiency can shape patients’ psychological and social experiences in profound ways.

## 4. Genetic and Molecular Characteristics

### 4.1 The RAC2 Gene and Protein

RAC2 is a **hematopoietic cell–specific small GTPase** belonging to the Rac subfamily of Rho family GTPases, encoded in humans on chromosome 22q13 (in mice on chromosome 15).[6][5] The protein functions as a molecular switch, cycling between an inactive GDP-bound state and an active GTP-bound state, and is activated by guanine nucleotide exchange factors (GEFs) in response to receptor signaling.[1][6][10] Once active, RAC2 orchestrates **actin cytoskeleton remodeling**, **cell migration**, and **NADPH oxidase activation**, among other processes critical for innate and adaptive immunity.[6][12][16] In immune cells, RAC2 is particularly important in neutrophils, macrophages, mast cells, and lymphocytes; in mast cells, Rac2 regulates protease gene expression, and in dendritic cells, Rac1 and Rac2 control the formation of dendrites.[5][6]

UniProt and related protein databases (though not directly cited in the search results) annotate RAC2 with Gene Ontology (GO) biological process terms such as **“neutrophil chemotaxis” (GO:0030593)**, **“superoxide anion generation” (related to NADPH oxidase activity)**, **“regulation of actin cytoskeleton organization” (GO:0030036)**, and **“small GTPase-mediated signal transduction” (GO:0007264).[6][12][16] Cellular component terms include **“cytoplasm” (GO:0005737)** and **“plasma membrane” (GO:0005886)**, reflecting RAC2’s localization at the cell cortex where it interacts with actin and membrane-associated oxidase complexes.[12][16]

### 4.2 Pathogenic Dominant-Negative Variants

The prototypical dominant-negative variant causing IMD73A is **RAC2 c.169G>A (p.Asp57Asn, D57N)**, located in a conserved motif essential for GTP binding and hydrolysis.[10][15][18] Structural and biochemical studies have shown that D57N **fails to bind GTP**, rendering RAC2 inactive and unable to relay upstream signals.[6][10][15] Importantly, the mutant protein also **sequesters GEFs**, preventing them from activating wild-type RAC2 and potentially other small GTPases such as RAC1, thereby exerting a **dominant-negative effect** beyond simple loss of RAC2 function.[1][6][10][15] As reviewed in a zebrafish immunodeficiency study, “The Rac2D57N mutant exerts its dominant negative effect through sequestration of guanine nucleotide exchange factors (GEFs), and any other Rho GTPase that requires the activity of a Rac2D57N-sequestered GEF could be inhibited by this mutant.”[1]

Clinically, **all five patients** with D57N reported in one series had absent or drastically impaired chemotaxis to fMLP, and three tested patients had absent or severely reduced neutrophil respiratory burst in response to fMLP.[6] These functional defects mirror RAC2’s dominant role in high-concentration chemoattractant responses and NADPH oxidase activation, as elucidated in human neutrophil studies showing that RAC2 is absolutely required for fMLP-stimulated superoxide production and for the continuous expansion of the leading-edge lamellipodium in strong chemoattractant gradients.[12] Additional dominant-negative variants affecting similar functional domains of RAC2 have been described, although detailed characterization is less extensive than for D57N.[6][15] In all cases, the variant type is **missense**, altering a single amino acid rather than causing truncation; the consequence is a structurally intact but dysfunctional protein capable of interfering with normal RAC2 function.

From an ACMG/AMP standpoint, D57N and similar dominant-negative RAC2 missense variants would be classified as **pathogenic**, based on strong functional evidence, multiple affected individuals, recurrence of the same variant in unrelated families, and consistency with the gene’s known mechanism of disease.[6][9][10][15] Allele frequencies in population databases are extremely low or absent, supporting their pathogenicity, although specific frequency values are not provided in the available search results.[6][15] These variants are **germline** rather than somatic, arising in the germ cells of affected parents or de novo in the proband, and they confer constitutional immunodeficiency rather than localized disease.[6][10][15]

### 4.3 Relationship to Other RAC2 Mutational Classes

Recent work has clarified that RAC2 can cause distinct immunodeficiency phenotypes depending on the **direction and magnitude of functional alteration**. A 2023–2024 clinical and functional spectrum study concluded that “mutations in the small Rho-family guanosine triphosphate hydrolase RAC2, critical for actin cytoskeleton remodeling and intracellular signal transduction, are associated with neonatal severe combined immunodeficiency (SCID), infantile neutrophilic disorder resembling leukocyte adhesion deficiency (LAD), and later-onset combined immune deficiency (CID).”[6] They further stated that “constitutively active RAS-like mutations caused neonatal SCID, dominant-negative mutations caused LAD-like disease, whereas dominant-activating mutations caused CID.”[6] In this framework, IMD73A corresponds to the **LAD-like** subset driven by **dominant-negative** mutations, principally D57N.

Constitutively active “RAS-like” mutations, which lock RAC2 in a GTP-bound state and drive continuous signaling, result in **profound lymphopenia and SCID**, with near-total absence of peripheral neutrophils in some patients.[6] Dominant-activating mutations, which increase RAC2 activity without full constitutive activation, produce **combined immunodeficiency** characterized by hypogammaglobulinemia, recurrent sinopulmonary infections, and bronchiectasis, as well as lymphoproliferation and cancer predisposition, exemplified by the homozygous R68W cases.[6][7] In contrast, dominant-negative mutations like D57N primarily affect **neutrophil migration and oxidative burst**, yielding the LAD-like phenotype with neutrophilia and recurrent bacterial infections.[6][10][15][18]

This allelic series underscores the importance of **functional characterization** in RAC2 variant interpretation. As the authors of the spectrum study emphasized, “RAC2 mutant proteins exhibit aberrant function although no singular test is sufficient to determine functional consequence,” and proper evaluation should integrate expression and signaling assays.[6] They noted that reduced steady-state expression alone may be misleading, as in R68W, where low protein levels coexist with hyperactivation in homozygous cells.[7] For IMD73A, dominant-negative behavior is defined by impaired GTP binding, GEF sequestration, and suppression of wild-type RAC2 activity, rather than simple haploinsufficiency.[1][6][10][15]

### 4.4 Modifier Genes, Epigenetic and Chromosomal Considerations

To date, **no specific modifier genes** have been conclusively associated with IMD73A; most published cases attribute the phenotype entirely to RAC2 mutation.[6][10][15][18] Mouse models suggest that **RAC1** can partially compensate for RAC2 deficiency in some contexts, particularly in low-concentration chemoattractant responses; however, RAC1 cannot fully substitute for RAC2 in NADPH oxidase activation or high-concentration chemotaxis.[12][16] In rac2^-/- zebrafish, overexpression of **Rac1 in neutrophils** can partially rescue neutrophil recruitment to wounds and survival after infection, indicating overlapping but not redundant functions.[1] Nonetheless, the presence of normal RAC1 alleles does not prevent disease in human D57N carriers, likely because dominant-negative RAC2 interferes with shared GEFs and signaling modules.[1][6][10][12] 

Epigenetic modifications and large-scale chromosomal abnormalities have not been reported as primary etiologic factors in IMD73A, and RAC2-associated immunodeficiency is understood as a **single-gene, sequence-level disease**.[6][11][13] Chromosomal microarray and karyotyping are expected to be normal in IMD73A patients, aside from incidental findings unrelated to disease. Epigenetic profiling of RAC2 expression across hematopoietic lineages would be valuable for understanding cell-type specificity of disease mechanisms, but such data are not presently available in the search results. Similarly, no evidence links IMD73A to copy-number variants or translocations involving RAC2.

## 5. Environmental and Infectious Context

### 5.1 Environmental Factors and Lifestyle

In the specific case of neutrophil immunodeficiency syndrome caused by dominant-negative RAC2 mutations, environmental factors are **secondary determinants** of disease expression, influencing infection exposure rather than the presence or absence of disease.[6][11][13] Given the monogenic, autosomal dominant nature of IMD73A, individuals with pathogenic RAC2 mutations will have neutrophil dysfunction irrespective of environmental conditions, although the **clinical impact** of this dysfunction depends heavily on microbial exposures, vaccination, and healthcare access.[6][7][10] For example, an infant living in a setting with high pathogen burden, poor sanitation, or limited access to antibiotics may experience more frequent and severe infections than a genetically identical individual in a low-exposure, high-resource environment.

Lifestyle factors such as **smoking**, **diet**, and **exercise** may indirectly influence disease course by modulating general health and organ resilience, particularly in patients with chronic lung disease (e.g., bronchiectasis) from recurrent infections.[3][7] However, there is no direct evidence that such factors alter neutrophil chemotaxis or RAC2 signaling in IMD73A. Nutritional deficiencies, for instance, could compromise wound healing and immune function, but they would act as additive burdens rather than fundamental etiologic factors in RAC2-mutant individuals.

### 5.2 Pathogens and Infectious Triggers

Although RAC2 mutations themselves are the primary cause of IMD73A, **pathogens play an essential role in clinical expression**, as infections reveal and amplify the underlying neutrophil defect.[6][10][15][18] The common bacterial pathogens in reported IMD73A cases include **Staphylococcus aureus**, **Streptococcus species**, and Gram-negative organisms typical of skin and soft tissue infections, though specific microbiologic details are limited in the summarized literature.[10][15][18] Similar pathogens cause infections in other neutrophil disorders and provide a context for empiric and targeted antibiotic therapy.

Experimental work in zebrafish and mice has highlighted **Pseudomonas aeruginosa**, **Aspergillus fumigatus**, and various opsonized particles as key test pathogens for assessing Rac2-dependent host defense.[1][10][16] In **rac2^-/- zebrafish larvae**, susceptibility to P. aeruginosa and A. fumigatus is markedly increased, with defective neutrophil and macrophage motility leading to poor recruitment to infection sites.[1] In **Rac2-deficient mice**, Fcgamma receptor–mediated phagocytosis of IgG-coated sheep red blood cells and NADPH oxidase activity in response to phorbol ester or FcgammaR stimulation are significantly decreased, although responses to serum-opsonized zymosan are preserved.[16] These findings suggest that RAC2-dependent pathways are particularly critical for certain modes of phagocytosis and oxidative burst, and that pathogens exploiting these pathways (e.g., encapsulated bacteria requiring opsonization) may pose special risks for RAC2-mutant patients.

There is no evidence that specific pathogens **cause** IMD73A or induce RAC2 mutations; rather, they act as **triggers of clinical episodes** in genetically predisposed individuals. However, recurrent or chronic infections, such as those leading to bronchiectasis in RAC2-related combined immunodeficiency, may create a vicious cycle of tissue damage and further susceptibility.[3][6][7] From an ontology perspective, relevant infectious agents can be represented using NCBI Taxonomy identifiers (e.g., taxon IDs for P. aeruginosa, A. fumigatus, S. aureus), although these identifiers are not explicitly cited in the search results.

## 6. Mechanisms and Pathophysiology

### 6.1 Neutrophil Chemotaxis and Motility Defects

The central mechanistic hallmark of IMD73A is **defective neutrophil chemotaxis and motility**, arising from disruption of RAC2-mediated actin cytoskeleton dynamics and cell polarization.[6][10][12][16] In normal neutrophils, RAC1 and RAC2 are differentially activated in response to chemoattractant gradients, orchestrating the formation and extension of lamellipodia at the leading edge.[12] Zhang et al. demonstrated that “Rac1 activation is an important determinant for initiating cell spreading and the initial formation of the lamellipodium, while Rac2 activation is required for the continuous expansion and maintenance of the leading edge lamellipodium upon fMLP stimulation.”[12] They further showed that at low fMLP concentrations, Rac1-dominated responses suffice for directional migration without triggering a superoxide burst, whereas at high concentrations, Rac2 activation is essential for rapid migration and NADPH oxidase activation.[12]

Dominant-negative RAC2 mutations such as D57N interfere with this finely tuned system by **abolishing RAC2 activation** and sequestering GEFs, thereby preventing both RAC2 and potentially RAC1 from receiving upstream signals.[1][6][10][12][15] As a result, neutrophils in IMD73A can undergo initial cell spreading but fail to form a large, stable leading-edge lamellipodium, exhibiting reduced motility and poor responsiveness to chemoattractant gradients.[12] In vitro, pretreatment with Rac2-T17N, another inhibitory mutant, inhibited neutrophil chemotaxis overall, and Rac2-deficient cells “never formed a large leading edge lamellipodium and were largely non-responsive to the chemoattractant.”[12] These observations correspond closely to the functional defects observed in D57N patient neutrophils, which show absent or severely impaired chemotaxis to fMLP.[6][10][18]

In vivo imaging studies in zebrafish have provided compelling evidence that RAC2 is necessary for **neutrophil 3D motility and polarity**. Deng et al. expressed human inhibitory Rac2D57N in neutrophils and used live imaging to show that Rac2 signaling is essential for the polarization of F-actin dynamics and PI(3)K signaling during motile responses.[10] They concluded that “Rac2 signaling is necessary for both neutrophil 3D motility and CXCR4-mediated neutrophil retention in hematopoietic tissue, thereby limiting neutrophil mobilization, a critical first step in the innate immune response.”[10] In Rac2 morphants or Rac2D57N zebrafish larvae, neutrophils displayed impaired polarization, reduced motility, and increased mobilization into the circulation, mirroring the leukocytosis and tissue recruitment defects in IMD73A.[10]

These mechanistic insights can be mapped onto Gene Ontology biological process terms such as **“neutrophil chemotaxis” (GO:0030593)**, **“regulation of cell migration” (GO:0030334)**, and **“actin filament organization” (GO:0030048)**, and onto Cell Ontology terms such as **“neutrophil” (CL:0000775)** as the primary affected cell type.[12][16] The causal chain from RAC2 mutation to clinical phenotype thus begins with **impaired small GTPase activation**, proceeds through **defective actin remodeling and lamellipodia formation**, and culminates in **failed neutrophil recruitment to sites of infection and tissue injury**, leading to recurrent infections and poor wound healing.[1][6][10][12][15][16]

### 6.2 NADPH Oxidase and Oxidative Burst Dysfunction

In addition to motility defects, RAC2 plays a critical role in **activation of the phagocyte NADPH oxidase complex**, which generates superoxide and downstream reactive oxygen species for microbial killing.[6][12][16] Kim and Dinauer showed that “Rac2 is an essential regulator of neutrophil nicotinamide adenine dinucleotide phosphate (NADPH) oxidase activation in response to specific signaling pathways,” particularly those mediated by fMLP and Fc receptors.[12][16] In Rac2-deficient mice, neutrophils exhibited severe defects in superoxide production in response to phorbol ester, fMLP, or IgG-coated particles, while responses to other stimuli were variably affected.[16] These data indicate that Rac2 is indispensable for **agonist-specific oxidative burst** activation.

In human D57N patients, functional assays have documented **absent or severely reduced neutrophil respiratory burst in response to fMLP**, alongside defective chemotaxis.[6][10][18] The clinical and functional spectrum study noted that “RAC2 is a critical component of the phagocyte NADPH oxidase complex, with mutations causing either absent or increased levels of stimulus-induced superoxide,” and that in D57N patients, fMLP-triggered respiratory burst is severely compromised.[6] This mechanistic defect contributes to impaired microbial killing at infection sites, compounding the effects of poor neutrophil recruitment.

From a biochemical perspective, NADPH oxidase activation involves the assembly of membrane-bound and cytosolic components, including gp91^phox, p22^phox, p47^phox, p67^phox, p40^phox, and Rac2, at the plasma membrane or phagosomal membrane, where electron transfer from NADPH to oxygen generates superoxide (\(\mathrm{O_2^-}\)).[6][12][16] RAC2’s role includes binding to p67^phox and modulating membrane localization and conformational activation of the oxidase complex.[6][12] Dominant-negative RAC2 mutations disrupt these interactions, preventing proper assembly or activation and thereby reducing superoxide generation. The relevant GO terms include **“superoxide anion generation” (GO:0019430)**, **“NADPH oxidase complex assembly” (GO:0043023)**, and **“immune response to bacterium” (GO:0006955)**.[6][12][16]

The downstream consequences of oxidative burst failure include impaired killing of engulfed bacteria, delayed clearance of infection, and increased risk of dissemination. Unlike CGD, in which NADPH oxidase defects are often global and absolute, IMD73A exhibits **stimulus-specific oxidative defects**, with some pathways (e.g., phorbol ester) still partially functional, reflecting RAC1 and other GTPases’ contributions. Nonetheless, the combination of motility and oxidase defects in D57N patients yields a **distinct pathophysiologic profile** that explains their LAD-like clinical presentation.[6][10][12][16][18]

### 6.3 Broader Immune Cell and Host Defense Functions

Although IMD73A is defined primarily by neutrophil dysfunction, RAC2 is expressed in multiple immune cell types, and dominant-negative mutations may affect **macrophages, mast cells, and lymphocytes** to varying degrees.[5][6][16] In Rac2-deficient murine macrophages, investigators observed “selective defects paralleling many of the observed functional defects in Rac2-null neutrophils,” including decreased Fcgamma receptor–mediated phagocytosis of IgG-coated sheep red blood cells and diminished NADPH oxidase activity in response to phorbol ester or FcgammaR stimulation.[16] Interestingly, phagocytosis and oxidant production stimulated by serum-opsonized zymosan were normal in Rac2-null macrophages, indicating that Rac2’s role is pathway-specific.[16] Macrophage morphology and actin polymerization during certain stimuli were also similar to wild-type, suggesting that Rac1 can compensate in some aspects.[16]

In **rac2^-/- zebrafish larvae**, both neutrophils and macrophages show defective basic motility and recruitment to tissue wounds and infections, leading to increased susceptibility to P. aeruginosa and A. fumigatus.[1] The authors noted that “re-expression of Rac2 in either neutrophils or macrophages can partially rescue the susceptibility of rac2^-/- larvae to Pseudomonas infection,” indicating that RAC2 function in both lineages is important for host defense.[1] Moreover, overexpression of Rac1 in neutrophils partially rescued neutrophil recruitment and survival, underscoring the interplay between Rac isoforms.[1]

In human RAC2-related immunodeficiency beyond IMD73A, significant T- and B-lymphopenia and low immunoglobulins have been observed in most patients with constitutively active or activating mutations, and lymphoproliferation and autoimmunity have been reported.[6][7] For IMD73A specifically, lymphocyte counts and immunoglobulin levels may be closer to normal, but subtle effects on adaptive immunity cannot be excluded, given RAC2’s roles in T and B cell receptor signaling and cytoskeletal remodeling.[6] Thus, the clinical phenotype reflects not only neutrophil dysfunction but also **broader perturbations of immune cell behavior**, particularly in more severe RAC2 mutation classes.

From an ontology standpoint, affected cell types include **neutrophils (CL:0000775)**, **macrophages (CL:0000584)**, **mast cells (CL:0000097)**, and **T and B lymphocytes (CL:0000084, CL:0000236)**.[5][6][16] Relevant GO processes encompass **“phagocytosis” (GO:0006909)**, **“Fc-gamma receptor signaling pathway” (GO:0038094)**, **“regulation of lymphocyte activation” (GO:0051249)**, and **“immune system process” (GO:0002376).**[6][16] IMD73A occupies a specific niche within this broader network, emphasizing neutrophil chemotaxis and oxidative burst while acknowledging RAC2’s multifaceted roles across leukocyte subsets.

### 6.4 Tissue Damage and Systems-Level Pathophysiology

The tissue-level consequences of RAC2 dysfunction in IMD73A include **persistent infection foci**, **chronic inflammation**, and **delayed tissue repair**, which can culminate in structural damage such as scarring and, in broader RAC2-related disease, bronchiectasis.[3][6][7][10][15] In the lungs, repeated bacterial infections and impaired clearance can lead to destruction of bronchial walls, mucus accumulation, and permanent airway dilatation, characteristic of bronchiectasis, as documented in patients with activating RAC2 mutations and combined immunodeficiency.[3][7] Although bronchiectasis has not been systematically reported in D57N-driven IMD73A, the underlying risk is present wherever neutrophil-mediated host defense is compromised.

Chronic infection and inflammation can also drive **tissue remodeling and fibrosis**, mediated by macrophages, fibroblasts, and other stromal cells responding to persistent damage signals.[6][7][16] In the context of RAC2-related immunodeficiency, lymphoproliferation and organ involvement such as kidney dysfunction due to light-chain deposition disease illustrate how ongoing immune activation and dysregulated lymphocyte function can injure tissues.[7] In IMD73A, repeated skin and soft tissue infections may result in scarring, contractures, or cosmetic deformities, impacting function and quality of life.[10][15] 

At a systems level, IMD73A reflects a **failure of the innate immune system to mount an effective first-line response**, leading to overburdening of adaptive immunity and increasing reliance on antibiotics and other external supports.[6][10][15] GO terms such as **“innate immune response” (GO:0045087)**, **“inflammatory response” (GO:0006954)**, and **“wound healing” (GO:0042060)** are pertinent to this broader pathophysiologic picture. The causal chain from RAC2 mutation to clinical outcome involves multiple hierarchical steps: molecular dysfunction (RAC2/GTP binding and GEF interaction), cellular defects (neutrophil motility and oxidative burst), tissue-level failure (infection persistence and poor healing), and organ-level damage (scarring, bronchiectasis, organ failure), ultimately manifesting as increased infection susceptibility and long-term morbidity.[1][6][7][10][12][15][16]

## 7. Anatomical Structures and Cell Types Affected

### 7.1 Organ and System-Level Involvement

The primary anatomical structures affected in IMD73A are those involved in **hematopoiesis and immune surveillance**, including **bone marrow**, **blood**, and **peripheral tissues** where neutrophils are recruited to fight infection and participate in wound healing.[1][6][10][16] Bone marrow (UBERON:0002365) is the site of neutrophil production; in IMD73A, production is generally normal or increased, but neutrophils fail to retain properly in hematopoietic tissue due to altered RAC2/CXCR4 signaling.[10] Deng et al. showed that Rac2 signaling is required for CXCR4-mediated neutrophil retention in hematopoietic tissue, and that inhibitory Rac2 mutations partially rescue neutrophil retention in a zebrafish model of WHIM syndrome, indicating that RAC2 is a key regulator of neutrophil mobilization.[10]

The **blood** (UBERON:0000178) is the reservoir where neutrophils accumulate in IMD73A, leading to leukocytosis and neutrophilia.[10][11][14] Endothelial barriers in the vasculature and post-capillary venules are critical anatomical sites for neutrophil adhesion and transmigration; while integrin expression is normal in IMD73A, RAC2-dependent cytoskeletal and signaling events are required for effective diapedesis, and their disruption contributes to defective tissue recruitment.[10][12] Peripheral tissues including **skin (UBERON:0002097)**, **subcutaneous tissue**, **mucosal surfaces**, and the **lungs (UBERON:0002048)** are common infection sites in RAC2-related disease, as evidenced by recurrent skin infections, wound healing defects, and bronchiectasis in combined immunodeficiency cases.[3][6][7][10][15]

The **respiratory system** is particularly vulnerable in patients with activating RAC2 mutations, who often develop recurrent sinopulmonary infections and bronchiectasis.[3][6][7] In IMD73A, the risk of lung involvement depends on infection history, but the underlying neutrophil defect places the lungs at risk in any case. The **integumentary system** (skin and soft tissue) is repeatedly involved due to superficial and deep infections and wound healing problems.[10][15] The **lymphoid system** (lymph nodes, spleen, thymus) may also be affected in broader RAC2-related disease, manifesting as lymphadenopathy and lymphoproliferation, though this is less prominent in purely neutrophil-dominant IMD73A.[6][7]

### 7.2 Tissue and Cell-Level Structures

At the tissue level, IMD73A primarily involves **connective tissues**, **epithelia**, and **vascular endothelium**, where neutrophils interact with pathogens and participate in inflammatory responses. Infection foci in skin and soft tissue often involve dermis and subcutaneous fat, where neutrophils would normally infiltrate, phagocytose bacteria, and coordinate with macrophages and lymphocytes to clear infection.[10][15] In IMD73A, neutrophils fail to arrive or arrive late, resulting in prolonged infection and tissue damage.

The key cell populations targeted include **neutrophils (CL:0000775)** and **macrophages (CL:0000584)**, as well as other leukocytes that utilize RAC2 for cytoskeletal remodeling and signaling.[1][6][16] In Rac2-null mice, macrophage accumulation during peritoneal inflammation is reduced, and macrophages show specific defects in Fcgamma receptor–mediated phagocytosis and NADPH oxidase activation, paralleling neutrophil defects.[16] Mast cells and dendritic cells also rely on RAC2 for protease gene expression and dendrite formation, respectively, although their roles in IMD73A pathophysiology have not been emphasized in human case reports.[5][6]

At the **hematopoietic tissue level**, CXCR4-expressing neutrophil precursors and mature neutrophils interact with stromal cells and chemokine gradients to regulate retention and mobilization.[10] RAC2’s role in CXCR4 signaling affects these interactions, and inhibitory mutations lead to defective retention and excessive mobilization, contributing to neutrophilia.[10] The relevant tissues include bone marrow sinusoids, stromal niches, and the microvascular environment.

### 7.3 Subcellular Compartments

RAC2 is localized primarily in the **cytoplasm and plasma membrane**, where it interacts with actin filaments, membrane lipids, and NADPH oxidase components.[6][12][16] The subcellular compartments involved in IMD73A pathophysiology include the **leading-edge cortex**, where lamellipodia form during chemotaxis; the **phagosomal membrane**, where NADPH oxidase assembly occurs; and **signaling microdomains** associated with receptors such as fMLP receptors and Fc receptors.[12][16] Gene Ontology cellular component terms such as **“plasma membrane” (GO:0005886)**, **“cytoskeleton” (GO:0005856)**, and **“phagosome” (GO:0045335)** are directly relevant to RAC2-mediated processes.

Dominant-negative RAC2 mutations disrupt subcellular localization and activation patterns of RAC2, leading to failure of **F-actin polarization** at the leading edge and impaired recruitment of oxidase complex components to the phagosome or plasma membrane.[10][12][16] Live imaging in zebrafish has visualized these defects in real time, showing altered distribution of F-actin and PI(3)K signaling in Rac2-deficient neutrophils.[10] These subcellular changes translate into macroscopic defects in chemotaxis and microbial killing.

## 8. Temporal Development and Disease Course

### 8.1 Age of Onset and Pattern of Onset

IMD73A typically presents in **early infancy**, with recurrent bacterial infections emerging within the first months of life.[6][10][11][13][18] OMIM’s clinical synopsis for IMD73A notes that onset is in early infancy, consistent with reported cases.[11][13] The first D57N patient described in the literature was an infant with severe bacterial infections and impaired wound healing; another D57N patient was identified through newborn screening for T cell lymphopenia, indicating that RAC2-related neutrophil immunodeficiency can be detected even before overt clinical symptoms in some instances.[6][18]

The pattern of onset is generally **acute** in the sense that infections appear suddenly and may be severe, but the underlying genetic defect is present from birth, making the disease **congenital**.[6][11][13] There is no evidence of adult-onset IMD73A due to D57N; RAC2-related combined immunodeficiency forms with activating mutations may present later in childhood or adulthood, but IMD73A itself is a **pediatric disorder**.[6][7] The onset of symptoms can be influenced by environmental exposure and diagnostic vigilance; infants in high-resource settings may be diagnosed earlier due to newborn screening or immunologic workups.

### 8.2 Progression, Course, and Duration

The **course of IMD73A** is **chronic and lifelong**, as the underlying genetic defect persists, but the **phenotypic expression** may fluctuate depending on infection exposure, treatment, and age.[6][10][15] Recurrent infections are the dominant clinical episodes, and between infections, patients may be relatively asymptomatic. The progression rate of tissue damage and complications depends on the frequency and severity of infections; individuals with frequent, poorly controlled infections may develop chronic sequelae such as scarring or organ dysfunction more rapidly than those whose infections are promptly treated.[6][7][15]

In RAC2-related combined immunodeficiency with activating mutations, the disease course can be more **progressive**, with cumulative organ involvement such as bronchiectasis and neoplasms over years.[3][7] The homozygous R68W patient developed early bronchiectasis that initially responded to immunoglobulin replacement therapy, then experienced severe cutaneous viral infections, and later gynecologic and anal neoplasms, illustrating a multi-decade disease trajectory.[7] By contrast, IMD73A’s main long-term risk is recurrent bacterial infection and its sequelae; whether cancer risk is increased remains unknown.

Disease duration is effectively **lifelong** unless curative interventions such as **hematopoietic cell transplantation (HCT)** are performed.[6][7] In the R68W case, HCT resulted in sustained clinical improvement and likely altered the natural history.[7] HCT has also been considered and used in some RAC2 SCID cases.[6] For IMD73A, HCT may be considered in severe, refractory cases, potentially offering a cure by replacing hematopoietic stem cells with donor cells lacking the RAC2 mutation.

### 8.3 Remission, Critical Periods, and Windows of Intervention

Spontaneous remission of IMD73A is **not expected**, as the disease is genetic and constitutional.[6][11][13] However, **treatment-induced remission** of infection episodes is common with appropriate antibiotics and supportive care, and infection frequency can be reduced by prophylactic measures.[6][7][15] Critical periods of vulnerability include **early infancy and childhood**, when immune systems are still developing and exposure to pathogens is high, and when structural damage from infections can have long-term consequences.[6][10][11][15]

Windows of opportunity for intervention include **early diagnosis**, which allows for prompt prophylaxis, vaccination optimization, and consideration of advanced therapies such as HCT before irreversible organ damage occurs.[6][7][18] Newborn screening for T cell lymphopenia led to early identification of a D57N patient, demonstrating that immunologic screening programs can detect RAC2-related immunodeficiency in asymptomatic infants.[6][18] Genetic counseling and family-based cascade screening can identify at-risk relatives and enable early intervention.

## 9. Inheritance, Population Genetics, and Epidemiology

### 9.1 Inheritance Pattern, Penetrance, and Expressivity

IMD73A due to dominant-negative RAC2 mutations follows an **autosomal dominant** inheritance pattern.[11][13][9] OMIM lists inheritance as autosomal dominant, and ClinGen’s gene–disease validity curation reinforces this, noting strong evidence for the relationship between RAC2 and autosomal dominant immunodeficiency with defective neutrophil chemotaxis.[9][11][13] The D57N mutation has been documented in multiple unrelated families, with affected heterozygous individuals transmitting the mutation to offspring with similar phenotypes.[6][10][15][18]

Penetrance appears to be **high**, as all documented heterozygous carriers of D57N have exhibited significant neutrophil dysfunction and clinical manifestations, although the small number of cases limits precise estimates.[6][10][15][18] Expressivity may be **variable**, with differences in infection frequency, severity, and tissue involvement across individuals, influenced by environmental exposure, medical care, and perhaps subtle genetic modifiers.[6][7][15] There is no evidence of genetic anticipation, germline mosaicism, or polygenic contribution specific to IMD73A in the available literature.[6][11][13]

### 9.2 Population Distribution, Founder Effects, and Carrier Frequency

RAC2-related immunodeficiency, including IMD73A, is **extremely rare**, with Orphanet estimating prevalence of RAC2-related combined immunodeficiency syndromes as **<1 per 1,000,000**.[3] IMD73A itself has been described in only a small number of patients worldwide, making precise prevalence and incidence estimates impossible.[6][10][15][18] No specific ethnic or geographic predilection has been reported for D57N; cases have been identified in diverse populations.[6][10][15][18] By contrast, the homozygous R68W activating mutation has been found in two unrelated French-Canadian patients, suggesting a possible **founder effect** or localized enrichment, although this relates to activating mutations rather than IMD73A.[7]

Carrier frequency for D57N and other dominant-negative RAC2 variants in the general population is expected to be **extremely low**, likely below detection thresholds in broad population databases such as gnomAD, given the severe phenotype and negative selection.[6][15] Population genetics data specific to RAC2 variants are not presented in the available search results. The sex ratio among reported cases appears approximately balanced, with both males and females affected, consistent with autosomal inheritance.[6][10][15][18] Age distribution is skewed toward infants and children, reflecting early onset and the pediatric focus of immunodeficiency research.[6][10][11][13]

### 9.3 Epidemiologic Burden

Given its rarity, IMD73A contributes minimally to the **global burden of disease** in quantitative terms, but its importance lies in its **mechanistic insights into neutrophil biology** and as a prototype of Rac2-related immunodeficiency.[6][10][12][15][16] Epidemiologic data on mortality, hospitalization rates, and quality of life are not available in aggregate form, and knowledge is based on case reports and small series.[6][7][10][15][18] These reports indicate that IMD73A can cause significant morbidity, with repeated hospitalizations and risk of severe infection, but with appropriate management, survival into childhood and beyond is feasible.[6][10][15][18]

## 10. Diagnostics and Screening

### 10.1 Clinical and Laboratory Evaluation

Diagnosis of IMD73A requires integration of **clinical history**, **laboratory findings**, and **functional assays**. Clinically, suspicion should arise in infants or children with **recurrent severe bacterial infections**, poor wound healing, and **leukocytosis with neutrophilia**, particularly when integrin expression is normal, ruling out classical LAD.[10][11][13][14] Laboratory evaluation includes complete blood count, differential white cell count, immunoglobulin levels, and flow cytometry of leukocyte surface markers, which together help distinguish IMD73A from other immunodeficiencies.[6][10][15]

Functional testing is crucial. **Neutrophil chemotaxis assays** to fMLP or other chemoattractants can demonstrate impaired directional migration, often “absent or drastically impaired” in D57N patients.[6][10][18] **Respiratory burst assays**, such as dihydrorhodamine (DHR) flow cytometry, measure superoxide production in response to stimuli; in IMD73A, fMLP-triggered respiratory burst is absent or severely reduced, whereas phorbol ester responses may be variably affected.[6][10][12][16] These assays correspond to HPO terms such as **“Neutrophil migratory defect” (HP:0040238)** and laboratory abnormality terms reflecting oxidative burst defects.[8][12]

Imaging studies, biopsies, and pathology findings are generally secondary, used to assess infections and complications rather than to diagnose the underlying immunodeficiency. For example, CT scans of the chest may reveal bronchiectasis in combined immunodeficiency forms, and skin biopsies of chronic lesions may show nonspecific inflammation.[3][7] There are no specific radiologic or histopathologic hallmarks uniquely diagnostic of IMD73A.

### 10.2 Genetic Testing Strategies

Once clinical and functional suspicion is established, **genetic testing** for RAC2 mutations is indicated. The **NIH Genetic Testing Registry (GTR)** lists **neutrophil immunodeficiency syndrome** under RAC2, with testing approaches including single-gene sequencing and inclusion of RAC2 in immunodeficiency gene panels.[4] Whole exome sequencing (WES) or whole genome sequencing (WGS) can identify RAC2 variants as part of broader searches for inborn errors of immunity, especially when the phenotype is atypical or when multiple genes are considered.[6][15] Given the growing recognition of RAC2’s role in SCID, LAD-like disease, and CID, many next-generation sequencing panels now include RAC2 among candidate genes.

Single-gene testing may be cost-effective and efficient when functional assays strongly suggest RAC2 involvement, as in classical IMD73A presentations with defective fMLP chemotaxis and oxidative burst. However, the **functional diversity of RAC2 mutations** argues for broad sequencing approaches and careful interpretation. As the clinical spectrum study emphasized, “RAC2 mutant proteins exhibit aberrant function although no singular test is sufficient to determine functional consequence,” and evaluating suspected RAC2-related immunodeficiency should integrate both expression and signaling assays.[6] Reduced expression alone may not indicate loss of function, as hyperactive variants such as R68W can have low steady-state expression but increased signaling in homozygous cells.[7]

Chromosomal microarray, karyotyping, FISH, mitochondrial DNA testing, and repeat expansion assays are not directly relevant to IMD73A, as RAC2-related disease is caused by **sequence-level nuclear gene mutations**.[6][11][13] Omics-based diagnostics such as RNA-seq, proteomics, metabolomics, or epigenomics may provide research insights into pathway perturbations but are not currently standard clinical practice for IMD73A.

### 10.3 Differential Diagnosis and Clinical Criteria

Differential diagnosis of IMD73A includes other **phagocyte disorders** and **leukocyte adhesion deficiency syndromes**. Classical LAD type I involves mutations in ITGB2 encoding CD18, leading to impaired integrin-mediated adhesion, delayed umbilical cord separation, severe bacterial infections, and neutrophilia; integrin expression is reduced or absent.[10][14] In IMD73A, integrin expression is normal, but neutrophils still fail to migrate effectively due to RAC2 dysfunction.[10][14] LAD type IV (RAC2 mutation) has been proposed as a distinct category, emphasizing the convergence of clinical features with a different molecular pathogenesis.[10][14]

Other differential diagnoses include chronic granulomatous disease (CGD), which presents with recurrent infections and oxidative burst defects, but often with normal chemotaxis and different patterns of susceptibility; severe congenital neutropenia, characterized by neutropenia rather than neutrophilia; and combined immunodeficiencies affecting both innate and adaptive immunity.[6][10][16] Clinical criteria specific to IMD73A would include autosomal dominant inheritance, early-onset recurrent bacterial infections, leukocytosis, defective neutrophil chemotaxis and fMLP-induced oxidative burst, and RAC2 mutation with dominant-negative functional behavior.

Screening in asymptomatic individuals is generally limited to **family members** of known RAC2-mutant patients, using genetic testing and possibly functional assays. Newborn screening for T cell lymphopenia incidentally detected a D57N patient, suggesting that broader immunologic screening can uncover RAC2-related immunodeficiency earlier than symptom-based diagnosis.[6][18] However, routine population screening for IMD73A is not currently implemented, given its rarity.

## 11. Outcomes, Prognosis, and Predictive Factors

### 11.1 Survival, Mortality, and Life Expectancy

Data on survival and mortality in IMD73A are limited to case reports and small series, but available evidence suggests that **with appropriate management, many patients can survive into childhood and beyond**.[6][7][10][15][18] Severe infections in infancy pose significant risks, and mortality may occur in untreated or inadequately treated cases, but systematic mortality rates are not reported.[6][10][15][18] In RAC2-related combined immunodeficiency, long-term survival has been achieved with immunoglobulin replacement therapy, antimicrobial prophylaxis, and, in some cases, hematopoietic cell transplantation.[6][7] One R68W patient underwent HCT and achieved sustained clinical improvement, indicating that curative interventions can significantly alter life expectancy.[7]

For IMD73A, life expectancy likely depends on **infection control**, **organ damage**, and access to advanced therapies. Patients with frequent severe infections and chronic complications such as bronchiectasis (if present) may have reduced life expectancy compared with those whose infections are effectively prevented or treated. However, specific survival statistics such as five-year or ten-year survival rates have not been published, and the rarity of the condition precludes robust epidemiologic analyses.[3][6][7][10][15]

### 11.2 Morbidity, Disability, and Quality of Life

Morbidity in IMD73A is primarily driven by **recurrent infections**, resulting in repeated hospitalizations, antibiotic courses, and potential surgical interventions for abscess drainage or management of complications.[6][10][15][18] Persistent infections and poor wound healing can lead to scarring, functional limitations, and psychological distress. In broader RAC2-related immunodeficiency, bronchiectasis, persistent viral disease with oncogenic complications, lymphoproliferation, and organ dysfunction such as kidney disease significantly add to morbidity.[3][6][7]

Disability outcomes may include limitations in physical activity due to chronic lung disease, pain or reduced mobility from musculoskeletal infections or surgeries, and social restrictions related to infection avoidance. Quality-of-life measures have not been systematically applied, but physical functioning, emotional well-being, and social participation are likely affected, particularly in severe cases. These impacts highlight the need for multidisciplinary supportive care, including infectious disease, immunology, pulmonology, surgery, rehabilitation, and psychological services.[6][7][10][15]

### 11.3 Prognostic Factors and Biomarkers

Prognostic factors in IMD73A include **severity and frequency of infections**, **extent of organ damage**, **type of RAC2 mutation**, and **availability of advanced therapies**. Dominant-negative mutations like D57N produce LAD-like disease with neutrophilia and recurrent bacterial infections; the prognosis may be more favorable than in SCID-like constitutively active mutations, which cause profound lymphopenia and high mortality in infancy.[6] Dominant-activating mutations associated with CID and cancer predisposition may have more complex, long-term prognostic implications.[6][7]

Functional assays of neutrophil chemotaxis and oxidative burst could serve as **prognostic biomarkers**, with more severely impaired function correlating with higher infection risk. However, systematic correlations have not been reported. Genetic markers such as specific RAC2 variants can inform prognosis by indicating mutation class (dominant-negative versus activating) and expected phenotype. Early identification through newborn screening or family history is also prognostic, as it enables intervention before irreversible damage occurs.[6][7][18]

## 12. Therapeutic Approaches

### 12.1 Supportive and Antimicrobial Management

The cornerstone of IMD73A management is **aggressive infection control** through **antibiotic therapy**, **antimicrobial prophylaxis**, and **supportive care**. Antibiotic therapy (NCIT:C15208) should be tailored to the likely pathogens and tissue sites, with intravenous therapy for severe infections and oral regimens for milder episodes.[6][10][15][18] Antimicrobial prophylaxis (NCIT:C91859), including continuous low-dose antibiotics, can reduce infection frequency in high-risk patients, although careful monitoring for resistance and side effects is necessary.[6][7]

**Immunoglobulin replacement therapy (NCIT:C88722)** can support humoral immunity in patients with hypogammaglobulinemia or recurrent infections, particularly in RAC2-related combined immunodeficiency forms.[6][7] In the R68W case, immunoglobulin replacement improved bronchiectasis and infection control initially.[7] While IMD73A is primarily a neutrophil disorder, some patients may benefit from immunoglobulin therapy if antibody responses are impaired or if infections remain frequent despite antibiotics.[6][7][15]

Supportive care includes wound management, surgical drainage of abscesses, pain control, nutrition optimization, and rehabilitation. Vaccination, including pneumococcal, influenza, and other appropriate immunizations, should be optimized, taking into account any immunodeficiency-related contraindications. These strategies fall under **supportive care (NCIT:C16226)** and **infection prophylaxis** categories.

### 12.2 Hematopoietic Cell Transplantation and Advanced Therapies

For severe RAC2-related immunodeficiency, including SCID and some combined immunodeficiency forms, **hematopoietic cell transplantation (HCT; NCIT:C15206)** has been used as a curative therapy.[6][7] Transplantation replaces the patient’s hematopoietic stem cells with donor cells carrying wild-type RAC2, thereby restoring normal leukocyte function. In the R68W homozygous activating mutation case, HCT resulted in sustained clinical improvement, with resolution of lymphoproliferation and improved organ function.[7] HCT has also been reported in RAC2 SCID patients, with varying outcomes depending on transplant timing and complications.[6]

For IMD73A due to D57N, HCT has been considered in severe, refractory cases, although specific published outcomes are limited. The rationale is strong: given the hematopoietic-specific expression of RAC2, replacing the hematopoietic compartment should correct the neutrophil defect and resolve infection susceptibility. However, HCT carries risks of graft-versus-host disease, infection, and transplant-related mortality, and careful risk–benefit assessment is needed.[6][7]

Beyond HCT, **gene therapy** represents a potential future avenue. Gene addition or gene editing approaches targeting hematopoietic stem cells could correct RAC2 mutations while preserving autologous cells, reducing risks associated with allogeneic transplantation. As of the available literature, RAC2-specific gene therapy trials have not yet been reported, but the success of gene therapy in other phagocyte disorders such as CGD suggests conceptual feasibility. CRISPR/Cas9-based correction of D57N or other dominant-negative variants could, in principle, restore RAC2 function.

### 12.3 Personalized and Precision Medicine Approaches

Personalized medicine in IMD73A involves **genotype-guided management**, where the specific RAC2 mutation informs prognosis and treatment. For example, patients with constitutively active RAC2 mutations require urgent, aggressive management due to SCID-like phenotype, whereas those with dominant-negative mutations may benefit from targeted neutrophil support and prophylaxis.[6] Patients with activating mutations and cancer predisposition, such as R68W, need long-term oncologic surveillance and possibly early HCT.[7]

Pharmacogenomics, in the sense of drug metabolism variants affecting antibiotic or immunosuppressant response, has not been specifically studied in IMD73A, but general principles apply. Personalized infection prophylaxis regimens, vaccination strategies, and timing of HCT can be tailored based on clinical course, functional assays, and family preferences. As more RAC2 variants are discovered and functionally characterized, an integrated genotype–phenotype map will enable increasingly precise risk stratification and therapy selection.

## 13. Prevention and Counseling

### 13.1 Primary, Secondary, and Tertiary Prevention

Primary prevention of IMD73A, in the sense of preventing disease occurrence, is challenging because the condition is monogenic and typically arises from inherited or de novo mutations. However, **genetic counseling** and **reproductive options** such as preimplantation genetic diagnosis or prenatal testing can prevent transmission in families with known RAC2 mutations, representing a form of primary prevention.[6][11][13] Secondary prevention includes **early detection** through newborn screening, immunologic evaluation in high-risk families, and functional assays in symptomatic infants.[6][18] Tertiary prevention focuses on reducing complications in affected individuals through infection prophylaxis, supportive care, and timely HCT, as discussed above.[6][7][10][15]

### 13.2 Immunization, Screening, and Risk Stratification

Immunization strategies for IMD73A should follow general pediatric and immunodeficiency guidelines, including routine vaccines and additional coverage for encapsulated bacteria and influenza. Live vaccines may require caution depending on the severity of immunodeficiency; in SCID-like RAC2 mutations, live vaccines are contraindicated.[6] Screening programs such as newborn T cell lymphopenia screening incidentally detect some RAC2-related immunodeficiency cases, and expansion of neonatal screening to broader immunologic parameters could identify IMD73A earlier.[6][18]

Risk stratification involves identifying individuals at high risk based on family history, known RAC2 mutations, and functional assays. Genetic counseling (supported by NSGC and ACMG guidelines) is essential for families, explaining inheritance patterns, recurrence risks, and reproductive options. Cascade screening of relatives allows for early identification and intervention.

### 13.3 Public Health and Environmental Interventions

Given the rarity of IMD73A, public health interventions are limited to **general infection control measures** and **awareness among clinicians**. Early recognition by pediatricians, immunologists, and infectious disease specialists can prevent delays in diagnosis and treatment. Environmental interventions such as improving sanitation, reducing exposure to pathogens, and optimizing nutrition are broadly beneficial but not specific to IMD73A.

## 14. Other Species and Natural Disease

### 14.1 Natural RAC2-Related Disease in Animals

There are **no reports of naturally occurring RAC2 mutation–associated neutrophil immunodeficiency syndrome in companion animals or livestock** in the available search results. OMIA and veterinary databases might, in principle, contain such reports, but the current literature primarily focuses on experimental models rather than spontaneous disease.[1][5][12][16] Thus, IMD73A remains a human-specific entity at present, although the underlying RAC2 biology is conserved across vertebrates.

### 14.2 Comparative Pathology and Evolutionary Conservation

Comparative studies in mice and zebrafish have demonstrated **evolutionary conservation of RAC2’s role in neutrophil function**, supporting the relevance of these models for understanding human IMD73A.[1][5][10][12][16] Rac2 knockout mice exhibit chemotactic and oxidative burst defects in neutrophils and macrophages, mirroring human D57N functional phenotypes.[12][16] Rac2^-/- zebrafish larvae display defects in neutrophil and macrophage motility, impaired recruitment to wounds and infections, and increased susceptibility to P. aeruginosa and A. fumigatus, paralleling human infection susceptibility.[1]

These models reveal that RAC2’s role in actin cytoskeleton remodeling, chemotaxis, and NADPH oxidase activation is conserved across species, and they allow detailed dissection of cell-type–specific and pathway-specific functions. HomoloGene and related orthology databases (not directly cited here) confirm RAC2 orthologs in multiple species, including mice (NCBI Gene 19354) and zebrafish. The comparative pathology highlights that RAC2-related neutrophil dysfunction is a general consequence of Rac2 disruption, even though IMD73A itself is defined in humans.

## 15. Model Organisms and Research Applications

### 15.1 Mouse Rac2-Null Models

Rac2-deficient mice have been extensively used to study RAC2 function in neutrophils and macrophages.[12][16][14] In these mice, **neutrophils exhibit agonist-specific defects** in filamentous actin polymerization, chemotaxis, and superoxide production, particularly in response to phorbol ester, fMLP, and IgG-coated particles.[16] Macrophages show similar selective defects in Fcgamma receptor–mediated phagocytosis and NADPH oxidase activation, while some responses such as serum-opsonized zymosan-induced phagocytosis remain normal.[16] These models demonstrate that RAC2 is a relatively minor isoform in macrophages but plays non-overlapping roles with RAC1 in regulating host defense functions.[16]

Rac-null leukocytes (Rac1/Rac2 double knockout) show increased inflammation-mediated alveolar bone loss and phenotypes resembling human leukocyte adhesion deficiency, leading to the term **LAD type IV** for Rac2-related disease.[14] These models are particularly valuable for understanding **neutrophil retention and mobilization**, as well as the balance between RAC1 and RAC2 function in chemotaxis and oxidative burst.[12][14][16] They recapitulate many aspects of IMD73A at the functional level, though mice do not carry the specific D57N dominant-negative mutation.

### 15.2 Zebrafish RAC2D57N and rac2^-/- Models

Zebrafish have emerged as powerful models for **live imaging of leukocyte behavior** and for modeling human immunodeficiency disorders.[1][10] Deng et al. created a zebrafish model of primary immune deficiency by expressing human inhibitory Rac2D57N specifically in neutrophils, demonstrating essential roles for Rac2 in 3D motility, polarization of F-actin and PI(3)K signaling, and CXCR4-mediated neutrophil retention.[10] They observed increased mobilization of neutrophils from hematopoietic tissue, impaired recruitment to wounds and infections, and increased susceptibility to infection.[10] These phenotypes closely mirror human IMD73A and support the designation of RAC2D57N as causative for LAD-like neutrophil immunodeficiency.[10]

Separately, rac2^-/- zebrafish larvae have been used to study RAC2’s role in both neutrophils and macrophages.[1] These larvae have defects in basic motility and recruitment to tissue wounds and bacterial infections, leading to high susceptibility to P. aeruginosa and A. fumigatus.[1] Re-expression of Rac2 in neutrophils or macrophages can partially rescue susceptibility, and overexpression of Rac1 in neutrophils can rescue neutrophil recruitment and partially rescue survival, illustrating functional overlap.[1] Remarkably, rac2^-/- neutrophils do not display altered polarity or mobilization from hematopoietic tissue, in contrast to Rac2D57N-expressing neutrophils, suggesting that **dominant-negative mutants** have distinct phenotypic consequences compared with null alleles.[1][10]

These zebrafish models allow high-resolution **live imaging** of cell behavior in vivo, enabling visualization of neutrophil migration, retention, and interactions with pathogens and tissue structures. They have been instrumental in elucidating RAC2’s dual roles in motility and retention, and in demonstrating how inhibitory mutations alter CXCR4 signaling and neutrophil mobilization.[10] As such, they are invaluable for mechanistic research and for testing potential therapeutic interventions in a whole-organism context.

### 15.3 In Vitro and Cellular Models

In vitro models using human neutrophils, including pharmacologic inhibition of RAC2 and expression of dominant-negative constructs such as Rac2-T17N, have been used to dissect RAC1 versus RAC2 functions in chemotaxis and oxidative burst.[12] Zhang et al. treated human neutrophils with Rac2-T17N and observed impaired chemotaxis and lamellipodia formation, supporting the specific role of RAC2 in sustaining migration and superoxide production at high fMLP concentrations.[12] These cellular models complement animal models and allow precise manipulation of signaling pathways under controlled conditions.

Patient-derived leukocytes from RAC2-mutant individuals are perhaps the most relevant cellular models. Functional assays in D57N patient neutrophils have demonstrated absent or drastically impaired chemotaxis to fMLP and severely reduced respiratory burst, confirming the mechanistic predictions from mouse and zebrafish models.[6][10][18] In the R68W homozygous activating mutation cases, patient-derived cells exhibited increased effector signaling despite reduced RAC2 expression, highlighting dosage-dependent hyperactivation.[7] These observations underscore the importance of **functional assays and mechanistic studies in patient cells** for variant interpretation and personalized care.

### 15.4 Model Limitations and Future Directions

Despite their strengths, model organisms have limitations. Rac2-null mice do not fully capture the dominant-negative behavior of D57N, and differences in immune system organization between mice and humans can affect extrapolation.[12][16] Zebrafish models provide powerful imaging but may differ in immune cell repertoires and pathogen interactions.[1][10] In vitro models simplify complex tissue environments and may not reflect the full spectrum of RAC2 functions across cell types.

Future directions include **multi-omics profiling** of RAC2-mutant patient cells, single-cell analyses of immune cell heterogeneity, and spatial transcriptomics to map RAC2-dependent processes within tissues. Functional genomics screens using CRISPR or RNAi could identify modifiers of RAC2 signaling and potential therapeutic targets. Gene therapy and gene editing studies in animal models could pave the way for clinical translation. Continued collection of RAC2-mutant patient data, with systematic phenotyping and mechanistic assays, will refine the genotype–phenotype map and support precision medicine in RAC2-related immunodeficiency, including IMD73A.

## Conclusion

Neutrophil immunodeficiency syndrome, formally recognized as **immunodeficiency 73A with defective neutrophil chemotaxis and leukocytosis (IMD73A)**, represents a rare but mechanistically illuminating inborn error of immunity caused by **dominant-negative mutations in RAC2**, most notably the **p.Asp57Asn (D57N)** variant.[6][10][11][13][15][18] At the molecular level, dominant-negative RAC2 mutations abolish GTP binding and sequester GEFs, disrupting RAC2 and potentially RAC1 signaling, and thereby impairing actin cytoskeleton remodeling, neutrophil chemotaxis, and NADPH oxidase activation.[1][6][10][12][16] At the cellular level, neutrophils exhibit defective polarization, motility, and oxidative burst, particularly in response to high-concentration chemoattractant gradients such as fMLP, leading to **Neutrophil migratory defect (HP:0040238)** and **Increased susceptibility to infections (HP:0002719)**.[8][12][17] At the tissue and clinical level, patients present in early infancy with recurrent severe bacterial infections, poor wound healing, leukocytosis, and neutrophilia, in a pattern reminiscent of leukocyte adhesion deficiency but mediated by small GTPase dysfunction rather than integrin defects.[6][10][11][14][15][18]

The broader RAC2-related immunodeficiency spectrum includes SCID-like disease due to constitutively active mutations, LAD-like IMD73A due to dominant-negative mutations, and combined immunodeficiency with bronchiectasis and cancer predisposition due to activating variants such as R68W.[3][6][7] This allelic series underscores the centrality of RAC2 in hematopoietic cell biology and reveals how different directions of functional perturbation—loss, dominant-negative inhibition, hyperactivation—produce distinct immunologic phenotypes. Experimental models in Rac2-null mice and zebrafish expressing Rac2D57N or rac2^-/- provide strong mechanistic support, reproducing chemotactic and oxidative burst defects, impaired neutrophil retention and mobilization, and increased susceptibility to bacterial and fungal pathogens.[1][10][12][16]

Diagnostic evaluation of IMD73A relies on integration of clinical history, laboratory findings, functional assays of neutrophil chemotaxis and oxidative burst, and genetic testing for RAC2 mutations.[4][6][10][11][13][18] Treatment focuses on infection control through antibiotics, prophylaxis, and supportive care, with immunoglobulin replacement and HCT reserved for more severe or combined immunodeficiency forms.[6][7][10][15] Prevention and counseling emphasize early diagnosis, family-based genetic testing, and reproductive options. The rarity of IMD73A limits epidemiologic data, but case reports and series indicate significant morbidity and potential for favorable outcomes with appropriate management.[6][7][10][15][18]

From an ontology and knowledge-base perspective, IMD73A can be represented by **MONDO:0011988**, mapped to causal gene **RAC2 (HGNC:9801)**, biological processes such as **neutrophil chemotaxis (GO:0030593)** and **NADPH oxidase activation**, cell types including **neutrophils (CL:0000775)** and **macrophages (CL:0000584)**, anatomical locations such as **bone marrow (UBERON:0002365)** and **blood (UBERON:0000178)**, and clinical interventions including **antibiotic therapy (NCIT:C15208)**, **immunoglobulin replacement (NCIT:C88722)**, and **hematopoietic cell transplantation (NCIT:C15206)**.[1][3][4][6][10][11][12][15][16] As more RAC2 variants are discovered and characterized, this representation will need to evolve to capture the full spectrum of RAC2-related immunodeficiency, while maintaining IMD73A as a distinct LAD-like entity defined by dominant-negative RAC2-mediated neutrophil dysfunction.

Ultimately, IMD73A offers a compelling example of how **precision dissection of a single small GTPase’s function** can illuminate fundamental aspects of immune cell biology, inform clinical diagnosis and management, and guide the development of targeted therapies. Continued integration of human clinical data, model organism studies, and mechanistic research will be essential for advancing our understanding of RAC2-related disease and improving outcomes for affected patients.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.