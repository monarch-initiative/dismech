---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-15T12:17:40.901899'
end_time: '2026-10-15T12:22:19.949054'
duration_seconds: 279.05
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Cataract 5 Multiple Types
  mondo_id: MONDO:0007290
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
citation_count: 54
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 10
  validator_version: 0.3.0
term_validation:
  total_terms: 51
  verified: 48
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 4
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: DOID:0110255
    reported_labels:
    - Disease Ontology
    ontology_label: cataract 5 multiple types
  - term_id: NCBITaxon:9615
    reported_labels:
    - Dog, Staffordshire Bull Terrier
    - Dog, French Bulldog and Miniature Pinscher
    - Dog, Australian Shepherd and related Miniature/Toy Shepherds
    ontology_label: Canis lupus familiaris
  obsolete_terms:
  - term_id: HP:0010700
    ontology_label: obsolete Total cataract
    replaced_by: HP:0000518
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cataract 5 Multiple Types
- **MONDO ID:** MONDO:0007290 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cataract 5 Multiple Types** covering all of the
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

# Cataract 5, multiple types — comprehensive disease-characteristics report

**Disease:** Cataract 5, multiple types  
**Preferred symbol:** CTRCT5  
**MONDO:** MONDO:0007290  
**OMIM phenotype:** 116800  
**Causal gene:** *HSF4*  
**Inheritance:** Autosomal dominant  
**Evidence scope:** Human pedigrees and sporadic patients, supplemented by mouse, zebrafish, canine, cell-culture, transcriptomic, and proteomic experiments.

> **Important nomenclature boundary:** CTRCT5 is the autosomal-dominant, usually isolated cataract phenotype caused principally by heterozygous *HSF4* variants in its DNA-binding domain. It should not be conflated with **Cataract 12, multiple types (OMIM 611597)** caused by *BFSP2*, or automatically merged with recessive *HSF4*-related cataract.

---

## 1. Disease information

### 1.1 Definition and overview

Cataract 5, multiple types is a rare Mendelian lens disorder characterized by congenital, infantile, or early-childhood lens opacities with markedly variable morphology. Documented forms include lamellar, zonular, nuclear, pulverulent, anterior-polar, stellate, perinuclear, total, and “Marner-type” cataracts. The disorder is usually bilateral and progressive, although unilateral or very mild disease has been reported. It is caused by heterozygous germline variants in *HSF4*, encoding heat-shock transcription factor 4, on chromosome 16q22.1. [361][363]

The landmark gene-discovery study reported:

> “We screened individuals of three Chinese families for mutations in HSF4 … and discovered that in each family, a distinct missense mutation, predicted to affect the DNA-binding domain of the protein, segregates with the disorder.”  
> — Bu et al., *Nature Genetics*, published June 24, 2002; PMID: **12089525** ([PubMed](https://pubmed.ncbi.nlm.nih.gov/12089525/)). [48]

### 1.2 Identifiers and synonyms

| Resource | Identifier/name |
|---|---|
| MONDO | **MONDO:0007290**, cataract 5 multiple types |
| OMIM phenotype | **116800**, Cataract 5, multiple types |
| OMIM gene | **602438**, *HSF4* |
| Orphanet | **ORPHA:91492** |
| MedGen | **C0266537**, UID 78608 |
| Disease Ontology | **DOID:0110255** |
| MeSH | **D002386**, Cataract; congenital qualifier may be applied |
| ICD-10-CM | No CTRCT5-specific code; use **Q12.0** for cataract present congenitally or **H26.0/H26.01–H26.09** for infantile/juvenile cataract according to morphology and laterality |
| ICD-11 | No genotype-specific CTRCT5 code identified; code under congenital/developmental cataract with extension codes for laterality where supported |
| HGNC | *HSF4*, **HGNC:5227** |
| NCBI Gene | **3299** |
| UniProt | **Q9ULV5** |
| Cytogenetic locus | **16q22.1** |
| MANE transcript | **NM_001374675** |
| Synonyms | CTRCT5; cataract 5, lamellar; lamellar cataract; Marner cataract; cataract, Marner type; CAM; CTM; zonular HSF4-related cataract |

OMIM designates the phenotype autosomal dominant and maps it to *HSF4* at 16q22.1. MeSH classifies cataracts according to morphology or etiology under D002386. [271][361]

### 1.3 Data provenance

The knowledge base is **aggregated disease-level information**, not a single EHR-derived phenotype. Its principal sources are:

- Historical multigeneration pedigrees, including 132 affected individuals over eight generations in the original Marner family.
- Molecularly characterized Chinese and Danish families.
- Sporadic patients, including at least one de novo case.
- ClinVar laboratory submissions and aggregated diagnostic cohorts.
- Experimental mouse, zebrafish, and lens-cell models.

The large Danish family had mainly zonular cataract, with nuclear, anterior-polar, or stellate forms in some relatives; the Chinese linkage family had lamellar opacity surrounding a clear embryonic nucleus, with earliest recognized onset at 15 months. [96]

---

## 2. Etiology

### 2.1 Primary causal factor

The established cause of CTRCT5 is a **heterozygous germline pathogenic or likely pathogenic variant in *HSF4***. Dominant variants are concentrated in the highly conserved N-terminal α-helical DNA-binding domain and are predominantly missense substitutions. The clustering and functional studies support impaired DNA binding and, for at least some variants, a dominant-negative mechanism rather than simple haploinsufficiency. [121][124][418]

*HSF4* is a constitutively trimerized heat-shock transcription factor that controls lens-specific transcription, epithelial-cell proliferation, fiber-cell differentiation, proteostasis, autophagy, lysosomal function, and organelle removal. Cataract-causing variants can impair heat-shock-element recognition, protein–DNA contacts, protein folding, or oligomerization. [71]

### 2.2 Risk factors

| Risk-factor class | CTRCT5-specific assessment |
|---|---|
| Pathogenic *HSF4* allele | Primary and sufficient Mendelian risk factor in most molecularly confirmed families |
| Affected parent | Approximately 50% transmission risk for each pregnancy |
| Family history | Strong indication for molecular testing and early ophthalmic surveillance |
| De novo variant | Documented; absence of family history does not exclude CTRCT5 |
| Sex | No established sex bias; autosomal inheritance predicts similar susceptibility in males and females |
| Ancestry | Families have been reported in China, Denmark, Britain, Australia, Pakistan, Tunisia, and other populations; no validated ancestry-specific prevalence estimate |
| Consanguinity | Not expected to be important for dominant CTRCT5, but relevant to recessive *HSF4*-related cataract and other cataract genes |
| Age | Onset is usually congenital or early childhood, but penetrance and clinical recognition can be age dependent |
| UV, smoking, diabetes, corticosteroids, trauma, radiation | Established risks for acquired cataract generally, but not demonstrated causes of CTRCT5 |
| Maternal infection or metabolic disease | Differential causes of congenital cataract, not causal factors in molecularly confirmed CTRCT5 |

### 2.3 Protective factors

No penetrance-reducing human *HSF4* allele or validated genetic modifier has been established. Similarly, no diet, supplement, drug, or lifestyle intervention has been shown to prevent *HSF4*-mediated cataract.

Reasonable general eye-health measures—avoiding smoking, unnecessary ocular radiation, trauma, and excessive UV exposure, and controlling diabetes—may reduce superimposed acquired lens injury but should **not** be represented as primary prevention of this Mendelian disorder.

### 2.4 Gene–environment interaction

Direct human gene–environment evidence for CTRCT5 is limited. Experimentally, *Hsf4* deficiency increases UVB-induced senescence in mouse lens epithelial cells, with increased p21^Cip1^ and senescence-associated cytokines. HSF4 normally binds the *Cdkn1a/p21* promoter and recruits EZH2, increasing repressive H3K27me3. This supplies a plausible interaction between impaired HSF4 function and environmental oxidative/UV stress, but it is not yet a quantified clinical interaction in CTRCT5 families (PMID: **34339841**). [413]

Functional testing also found that five congenital-cataract HSF4 substitutions inhibited DNA binding, whereas weaker age-related-cataract substitutions had little effect, leading the investigators to suggest that other genetic and environmental factors may be necessary for the latter variants (PMID: **20670914**). [418]

---

## 3. Phenotypes

Frequencies for individual morphologies cannot be estimated reliably because published families are small, ascertainment differs, and morphology may change with age.

| Phenotype/type | Characteristics, onset and progression | Approximate frequency/evidence | Functional or quality-of-life effect | Suggested HPO |
|---|---|---|---|---|
| Cataract/lens opacity; clinical sign | Congenital to early childhood; usually bilateral; severity mild to visually significant; often progressive | Defining feature | Reduced acuity, glare, contrast loss; severe disease causes deprivation amblyopia or blindness | **HP:0000518** Cataract; **HP:0000519** Developmental cataract |
| Lamellar cataract; sign | Opaque lamella around a clear embryonic nucleus; earliest observed onset 15 months in the original Chinese family | Recurrent, but no pooled percentage | Central lamellar opacity may obstruct the visual axis | **HP:0007971** Lamellar cataract |
| Zonular cataract; sign | Predominant morphology in the large Marner pedigree; usually early-childhood and progressive | Common in Marner family | Variable visual loss depending on density and central extent | **HP:0010920** Zonular cataract |
| Nuclear cataract; sign | Embryonic or fetal nucleus opacity, sometimes total nuclear involvement | Reported across families | High amblyopia risk when dense and central | **HP:0100018** Nuclear cataract |
| Pulverulent cataract; sign | Fine dispersed opacities in primary lens fibers, often denser near Y-suture ends | Qualitatively reported | Mild opacities may be asymptomatic; dense clusters reduce acuity/contrast | **HP:0010693** Pulverulent cataract |
| Anterior-polar cataract; sign | May accompany zonular/stellate Marner cataract | Minority of reported patients | Small lesions may be visually insignificant; larger lesions can produce anisometropia | **HP:0001134** Anterior polar cataract |
| Stellate/Y-sutural opacity; sign | Star-shaped or concentrated along lens sutures | Reported in the Marner spectrum | Effect depends on density and central location | **HP:0010921** Sutural cataract, if locally accepted |
| Perinuclear cataract; sign | Opacity surrounding the nucleus; clear embryonic nucleus may remain | Reported with p.Ser105Thr and p.Leu114Pro | Variable acuity loss | **HP:0007971** or **HP:0100018**, with free-text morphology |
| Total cataract; sign | Entire lens significantly opaque; reported with several dominant *HSF4* variants | Several recent Chinese families | Severe visual deprivation and leukocoria; urgent treatment | **HP:0010700** Total cataract |
| Progressive cataract; temporal feature | Opacity can increase in density and distribution through childhood | Prominent in historical pedigrees | Increasing visual disability and eventual surgery | **HP:0007834** Progressive cataract |
| Unilateral/asymmetric disease | Usually bilateral, but unilateral lamellar cataract and markedly asymmetric severity have been reported | Uncommon | Anisometropia and particularly severe amblyopia risk | **HP:0012373** Unilateral; annotate eye-specific laterality |
| Leukocoria/abnormal red reflex; sign | Usually dense central or total cataract | Not quantified | Triggers urgent differential diagnosis, especially exclusion of retinoblastoma | **HP:0000555** Leukocoria |
| Reduced visual acuity/visual impairment; symptom/sign | Secondary to central opacity, amblyopia, or postoperative complications | Expected in visually significant disease | Reading, mobility, education, sports, and independence may be affected | **HP:0000505** Visual impairment |
| Amblyopia; complication | Deprivation or anisometropic; especially severe in unilateral disease or delayed treatment | Common in visually significant childhood cataract | Can remain permanent after anatomically successful surgery | **HP:0000646** Amblyopia |
| Strabismus; complication/sign | Secondary to poor vision or asymmetric input | Variable | Impaired binocular vision and psychosocial impact | **HP:0000486** Strabismus |
| Nystagmus; complication/sign | Usually indicates early bilateral visual deprivation | Variable; generally severe disease | Predicts limited visual development | **HP:0000639** Nystagmus |

The recognized disease-level HPO set explicitly includes nuclear, zonular, pulverulent, anterior-polar, and lamellar cataracts. Clinical descriptions additionally support progressive, bilateral early-childhood opacities with substantial intrafamilial variation. [362][363]

In a broader treated-childhood-cataract cohort, median functional visual ability indicated moderate impairment, and mean vision-related quality-of-life score was 65.67 where 96 represented normal. These values are not CTRCT5-specific but describe the likely burden of clinically significant pediatric cataract. [140]

---

## 4. Genetic and molecular information

### 4.1 Gene annotation

| Field | Annotation |
|---|---|
| Gene | *HSF4*, heat shock transcription factor 4 |
| HGNC | HGNC:5227 |
| NCBI Gene | 3299 |
| OMIM gene | 602438 |
| UniProt | Q9ULV5 |
| Location | chr16q22.1; GRCh38 approximately chr16:67.16–67.17 Mb |
| Protein class | DNA-binding heat-shock transcription factor |
| Major functional domains | N-terminal DNA-binding domain; hydrophobic heptad-repeat/oligomerization regions; transcriptional regulatory regions |
| Relevant isoforms | HSF4A and HSF4B have different transcriptional activities |
| Disease mechanism | Dominant DNA-binding-domain variants: impaired DNA binding/dominant interference; recessive variants outside the DBD: loss of function |
| Germline/somatic | CTRCT5 is germline; no somatic mechanism is established |

### 4.2 Principal dominant variants

Transcript numbering differs between publications. For example, historical p.Ala20Asp/p.Leu115Pro/p.Arg120Cys can appear as p.Ala19Asp/p.Leu114Pro/p.Arg119Cys on newer transcripts.

| HGVS reported in modern literature | Protein change | Type | Human phenotype/evidence | Classification/population evidence |
|---|---|---|---|---|
| c.56C>A | p.Ala19Asp | Missense; de novo | Infantile lamellar cataract | Pathogenic/likely pathogenic historical disease variant; absent from parents in original case |
| c.69G>T | p.Lys23Asn | Missense | AD congenital cataract in Chinese family | Reported pathogenic; DBD variant |
| c.187T>C | p.Phe63Leu | Missense | Bilateral congenital total cataract | Likely pathogenic; absent from 1000 Genomes, ExAC, gnomAD and 112 matched controls |
| c.190A>G | p.Lys64Glu | Missense | Lamellar pediatric cataract in British and Australian families | Reported pathogenic/likely pathogenic; DBD |
| c.218G>A | p.Arg73His | Missense | AD congenital cataract | Functionally/structurally predicted to impair HSE recognition |
| c.218G>T | p.Arg73Leu | Missense | Bilateral congenital total cataract | Likely pathogenic; absent from population databases and controls |
| c.233A>G | p.Tyr78Cys | Missense | Congenital nuclear cataract | Likely pathogenic; segregation plus rarity; computational evidence mixed |
| c.233-1G>A | — | Canonical splice acceptor | Congenital total cataract | Pathogenic by study ACMG assessment; no reported RNA validation |
| c.256A>G | p.Ile86Val | Missense | Unilateral lamellar cataract; carrier father had mild cortical clefts/lamellar separation at 46 | Historical disease-associated variant; illustrates variable expressivity |
| c.314G>C | p.Ser105Thr | Missense | Congenital perinuclear cataract | Likely pathogenic; absent from 1000 Genomes, ExAC, gnomAD and controls |
| c.341T>C | p.Leu114Pro | Missense | Lamellar opacity around clear nucleus | ClinVar pathogenic; predicted protein-folding disruption |
| c.355C>T | p.Arg119Cys | Missense | Zonular-stellate Marner cataract with anterior-polar opacity | ClinVar pathogenic; impairs HSE recognition |
| c.360+1G>A | — | Splice donor | Familial pediatric cataract | Reported likely pathogenic in a diagnostic cohort |
| Large deletion including *HSF4* | Whole-gene deletion | Copy-number loss | Reported under CTRCT5/age-related cataract submissions | ClinVar pathogenic submission, but phenotype-specific dosage evidence is less mature than for DBD missense variants |

The five variants found in a 42-family southeast-Chinese cohort accounted for **11.9%** of that selected cohort; this is not a population prevalence. Four missense variants were classified as likely pathogenic and c.233-1G>A as pathogenic, but their direct functional evidence was largely computational rather than biochemical. [95]

### 4.3 Molecular consequences

Five congenital-cataract-associated missense variants inhibited HSF4 DNA binding in vitro, linking the variants to reduced expression of lens proteins. Structural modeling suggests four nonexclusive mechanisms:

1. Loss of heat-shock-element recognition.
2. Perturbation of direct protein–DNA contacts.
3. Destabilization or misfolding of the DNA-binding domain.
4. Impaired HSF4 oligomerization. [71][418]

Dominant-negative action is plausible because HSF4 is constitutively trimeric: incorporation of a DBD-mutant subunit may poison DNA binding by the complex. This is mechanistically stronger for DBD missense variants than for whole-gene deletions.

### 4.4 Modifier genes and epigenetics

No validated human modifier gene predicts CTRCT5 severity. Experimental pathway partners include:

- *CRYAB*, *CRYGS*, *BFSP1*, *BFSP2*: lens structural/proteostasis targets.
- *DNASE2B*: fiber-cell denucleation.
- *ATG9A*: autophagosome formation.
- *TP53*, *CDKN1A*, *FAS*, *BAX*: cell-cycle and differentiation network.
- *EZH2*: HSF4-recruited histone methyltransferase.
- *PAX6*, BRG1/SMARCA4 and SNF2H/SMARCA5: broader lens differentiation and chromatin context.

HSF4 can recruit EZH2 to increase H3K27me3 at the *CDKN1A/p21* promoter in experimental lens cells. This is an epigenetic mechanism of HSF4 action, but no CTRCT5-specific diagnostic methylation signature is established. [413]

### 4.5 Chromosomal abnormalities

No recurrent CTRCT5-defining translocation, inversion, or aneuploidy is known. Rare deletions encompassing *HSF4* have been submitted as pathogenic, so deletion/duplication analysis is appropriate when sequence testing is negative, especially if additional congenital abnormalities suggest a contiguous-gene disorder. [93]

---

## 5. Environmental information

CTRCT5 is primarily genetic. There is no infectious agent, toxin, or nutritional deficiency necessary for disease.

| Factor | Relevance |
|---|---|
| UVB/oxidative stress | Plausible exacerbating stress based on HSF4-deficient lens-cell senescence; not quantified clinically |
| Ionizing radiation | General cataract risk; interaction with *HSF4* is unknown |
| Smoking, diabetes, corticosteroids | General acquired-cataract risks; no CTRCT5-specific effect demonstrated |
| Maternal rubella, CMV, toxoplasmosis, syphilis | Important alternative etiologies for congenital cataract, not triggers of confirmed CTRCT5 |
| Galactosemia/hypocalcemia | Metabolic differential diagnoses, not CTRCT5 mechanisms |
| Diet, alcohol, exercise | No disease-specific association |
| Occupational exposure | Not relevant to typical congenital/early-childhood presentation |

---

## 6. Mechanism and pathophysiology

### 6.1 Ordered causal chain

1. **A heterozygous germline *HSF4* DNA-binding-domain variant leads to** altered HSF4 folding, heat-shock-element recognition, protein–DNA interaction, or oligomer function.
2. **Defective HSF4 transcriptional activity leads to** reduced expression of lens crystallins and cytoskeletal genes, including *CRYGS*, *CRYAB*, *BFSP1*, and *BFSP2*.
3. **Reduced crystallin/chaperone and beaded-filament expression leads to** impaired protein stability, abnormal fiber-cell architecture, and protein/inclusion accumulation.
4. **Deficient HSF4 regulation of *TP53*, *FAS*, *BAX*, and growth-factor networks leads to** abnormal epithelial proliferation and mistimed fiber-cell differentiation.
5. **Reduced *DNASE2B* transcription leads to** incomplete degradation of lens-fiber nuclei.
6. **Reduced *ATG9A* transcription leads to** defective autophagosome biogenesis and maturation.
7. **Autophagic and lysosomal defects lead to** persistence of nuclei, mitochondria, endoplasmic reticulum, and Golgi in differentiating lens fibers.
8. **Persistent organelles and disordered fiber cells lead to** light scattering and loss of lens transparency.
9. **Lens opacity leads to** lamellar, nuclear, zonular, stellate, anterior-polar, perinuclear, or total cataract.
10. **Central dense opacity during visual development leads to** deprivation amblyopia, nystagmus, strabismus, and permanent visual impairment if treatment is delayed.

Steps 2–7 are strongly demonstrated in knockout/mutant animals and cultured lens cells but remain partly **inferred** for each individual human dominant variant.

### 6.2 Lens structural-gene branch

In *Hsf4*-null mice, *Crygs*, *Bfsp1*, and *Bfsp2* are markedly downregulated; *Bfsp1* and *Bfsp2* mRNA fell more than sevenfold at eight weeks. The mice develop progressive postnatal opacity, swollen/disorganized fibers, and altered αA-crystallin post-translational modification (PMID corresponding to the 2009 study). [186][265]

Suggested ontology annotations:

- **GO:0002088** lens development in camera-type eye
- **GO:0070306** lens fiber-cell differentiation
- **GO:0070307** lens fiber-cell development
- **GO:0070309** lens fiber-cell morphogenesis
- **GO:0005212** structural constituent of eye lens

### 6.3 Cell-cycle and differentiation branch

HSF4 stabilizes nuclear p53, activates p21, and imposes G1/S arrest in cultured human lens epithelial cells. Cataract-causing mutants did not stabilize p53 normally (PMID: **25940838**). [200]

In *hsf4*-null zebrafish, lens epithelial cells overproliferate, fiber cells become overabundant and disorganized, activated caspase-3 and p53 decline, and terminal organelle elimination fails. Partial rescue by *tp53*, *fas*, or *bax* mRNA supports a causal HSF4→p53/FAS/BAX differentiation axis (PMID: **28981088**). [202][256]

Suggested terms:

- GO:0007049 cell cycle
- GO:0000082 G1/S transition
- GO:0043065 positive regulation of apoptotic process
- CL:0002224 lens epithelial cell
- CL:0011004 lens fiber cell

### 6.4 Denucleation branch

HSF4 binds the *DNASE2B* promoter and promotes DNase IIβ expression and activity. HSF4 knockdown in zebrafish caused reduced DNase activity and incomplete lens-fiber denucleation (PMID: **23507146**). [182]

Suggested terms:

- GO:0044804 autophagy of nucleus
- GO:1903008 organelle disassembly
- GO:0070306 lens fiber-cell differentiation

### 6.5 Autophagy branch — principal 2023 development

A 2023 mouse and cell study found that HSF4 directly activates *ATG9A*. In HSF4^del42^ lenses, 417 genes were downregulated and 82 upregulated at both postnatal day 3 and day 7; ATG9A protein was markedly reduced. Autophagosome initiation, maturation, lysosome colocalization, and clearance of mitochondria, ER and Golgi were impaired. ChIP localized HSF4 binding to heat-shock elements in the *Atg9a* promoter (PMID: **37266953**, published June 1, 2023). [218]

> “Our findings demonstrate that HSF4 facilitates organelle degradation probably by transcriptionally activating autophagy during lens terminal differentiation.” [355]

Relevant terms:

- **GO:0006914** autophagy
- **GO:0016236** macroautophagy
- **GO:0097352** autophagosome maturation
- **GO:0005776** autophagosome
- GO:0005739 mitochondrion
- GO:0005783 endoplasmic reticulum
- GO:0005794 Golgi apparatus
- GO:0005634 nucleus

### 6.6 Lysosome/mTOR branch

HSF4 regulates *CRYAB*. Experimental evidence suggests αB-crystallin stabilizes an ATP6V1A–mTORC1 complex needed for lysosomal acidification. In *hsf4*-null zebrafish, reduced *cryaba* and increased lysosomal pH are proposed to impair organelle degradation. [187]

### 6.7 Immune and metabolic involvement

CTRCT5 is not primarily inflammatory, autoimmune, or metabolic. Secondary oxidative stress and senescence-associated cytokines are plausible downstream phenomena. No reproducible blood, aqueous-humor, or systemic metabolomic signature exists.

### 6.8 Molecular profiling and advanced technology

| Technology | Findings/status |
|---|---|
| Bulk transcriptomics | HSF4^del42^ mouse lenses: 417 shared downregulated and 82 upregulated genes at P3/P7; autophagy genes including *Atg9a* affected |
| Proteomics | HSF4-mutant vs wild-type human lens epithelial cells showed 23 differentially expressed proteins among 104 quantified, including histone and ribosomal proteins; exploratory |
| ChIP/reporter assays | Direct HSF4 regulation demonstrated for *ATG9A* and *DNASE2B* |
| Single-cell RNA sequencing | No validated CTRCT5-specific human single-cell atlas identified |
| Spatial transcriptomics | No disease-specific spatial study identified |
| Metabolomics/lipidomics | No validated CTRCT5 signature |
| Patient-derived lens organoids/iPSC | General lens organoids express *HSF4*, but no mature patient-specific therapeutic platform is established |
| CRISPR | Used to generate HSF4^del42^ mice and knockout lens epithelial cells; research, not clinical therapy |

---

## 7. Anatomical structures affected

| Level | Structure | Suggested ontology |
|---|---|---|
| Organ | Eye, principally crystalline lens | UBERON:0000970 eye; **UBERON:0000965 lens of camera-type eye** |
| Tissue | Lens anterior epithelium | **UBERON:0005614** |
| Tissue | Epithelium of lens | **UBERON:0001803** |
| Cell | Lens epithelial cell | **CL:0002224** |
| Cell | Lens fiber cell | **CL:0011004** |
| Lens regions | Embryonic/fetal nucleus, lamellae, cortex, sutures, anterior pole, posterior subcapsular region | Use morphology and laterality attributes |
| Subcellular | Nucleus, autophagosome, lysosome, ER, mitochondrion, Golgi, cytoskeleton/beaded filaments | GO:0005634, GO:0005776, GO:0005764, GO:0005783, GO:0005739, GO:0005794 |

The lens contains a proliferating epithelium and a bulk mass of terminally differentiated fiber cells; both are affected experimentally, with terminal fiber-cell organelle clearance being particularly important. [386]

Disease is usually bilateral but may be asymmetric or, rarely, unilateral. There is no established systemic-organ involvement in classic human CTRCT5.

---

## 8. Temporal development

### 8.1 Onset and course

- **Typical onset:** congenital, infantile, or early childhood.
- **Earliest documented in the original Chinese family:** 15 months, although other molecularly confirmed families had cataract at birth.
- **Pattern:** insidious developmental opacity rather than acute inflammation.
- **Course:** stable in some small opacities but commonly progressive.
- **Duration:** lifelong unless the lens is surgically removed.
- **Stage concept:** small/non-visually significant opacity → enlarging or denser central opacity → visually significant cataract → amblyopia/strabismus/nystagmus → postoperative aphakia or pseudophakia with lifelong surveillance.

### 8.2 Critical period

The critical window is early visual development. Visually significant unilateral cataract is generally removed at approximately **4–6 weeks**, and bilateral cataracts by **6–8 weeks**, balancing amblyopia prevention against anesthesia and glaucoma risk. [151][153]

The historical suggestion of genetic “anticipation” in the Marner pedigree is not supported by a repeat-expansion mechanism and may reflect ascertainment or age-dependent recognition. It should not be encoded as proven anticipation.

---

## 9. Inheritance and population

### 9.1 Inheritance characteristics

| Characteristic | Assessment |
|---|---|
| Mode | Autosomal dominant |
| Recurrence risk | 50% per pregnancy for an affected heterozygous parent |
| De novo occurrence | Documented |
| Penetrance | Apparently high in major pedigrees but not formally quantified; mild or late-recognized carriers occur |
| Expressivity | Markedly variable within and between families |
| Sex ratio | No demonstrated sex difference |
| Anticipation | Historically suggested, not molecularly established |
| Germline mosaicism | Theoretically possible but not specifically documented; residual recurrence risk remains after an apparently de novo variant |
| Founder effect | None firmly established for human CTRCT5 |
| Consanguinity | Not a major factor for dominant CTRCT5 |
| Carrier frequency | Not established; pathogenic alleles are individually very rare |
| Somatic mosaicism | Not established but technically possible |

### 9.2 Epidemiology

No CTRCT5-specific prevalence or incidence estimate is available. It is considerably rarer than congenital cataract as a group.

For context, pooled congenital-cataract prevalence is about **4.24 per 10,000** persons, with substantial geographic heterogeneity; childhood cataract prevalence ranges from 0.32–22.9 per 10,000 and incidence from 1.8–3.6 per 10,000 children per year. These are not *HSF4*-specific figures. [136][137]

In one selected Chinese familial congenital-cataract cohort, *HSF4* variants were found in 5/42 families (**11.9%**), but referral and candidate-gene selection prevent generalization. [95]

---

## 10. Diagnostics

### 10.1 Clinical evaluation

| Test | Role/findings |
|---|---|
| Newborn red-reflex examination | Detects absent, asymmetric, dull, or white reflex; immediate referral if abnormal |
| Dilated slit-lamp examination | Defines opacity size, density, layer, morphology, capsular defects and laterality |
| Age-appropriate visual acuity/fixation | Assesses functional significance and amblyopia |
| Cycloplegic refraction | Detects anisometropia and refractive amblyopia |
| Ocular alignment and nystagmus assessment | Identifies complications of visual deprivation |
| Intraocular pressure/corneal diameter | Baseline and postoperative glaucoma surveillance |
| Dilated fundus examination | Excludes retinal/optic-nerve disease |
| B-scan ultrasonography | Used when a dense cataract prevents posterior-segment visualization |
| Ocular biometry/keratometry | Required for surgical planning and IOL calculations |

AAP/AAO/AAPOS recommendations support red-reflex examination from the newborn period, with referral for an abnormal reflex. [287][289]

### 10.2 Laboratory investigations

For an otherwise healthy child with a clear dominant family history and a pathogenic *HSF4* variant, broad metabolic and infectious testing has low expected yield. If bilateral cataract is unexplained or accompanied by systemic signs, selectively consider:

- Urine reducing substances.
- Erythrocyte galactose-1-phosphate uridyltransferase and galactokinase.
- Serum glucose, calcium, phosphate, renal and liver tests.
- Infection testing for rubella, CMV, toxoplasmosis, herpes/varicella and syphilis, guided by maternal/neonatal history.
- Additional metabolic studies based on phenotype.

A 2023 retrospective study found that although 68% of tested children had positive TORCH IgG, no infection was confirmed; initial galactosemia or urine-reducing-substance abnormalities were likewise not confirmed. The authors concluded that genetic testing should be strongly considered and infection/metabolic tests should be clinically targeted (PMID: **37717619**). [307]

### 10.3 Genetic testing strategy

1. **Multigene congenital/childhood cataract panel** including *HSF4*, crystallins, connexins, transcription factors, membrane proteins, and syndromic cataract genes.
2. Ensure **deletion/duplication analysis** and adequate coverage of *HSF4* coding exons and splice junctions.
3. If a known familial *HSF4* variant exists, use targeted testing for relatives, prenatal diagnosis, or preimplantation testing.
4. If panel-negative, use trio **WES or WGS**, particularly with atypical ocular/systemic findings.
5. Reanalyze negative or VUS results periodically.
6. Confirm pathogenic variants and segregation by an orthogonal method where clinically required.

In a diverse US pediatric cohort published February 28, 2023, diagnostic yields were **46.2% for WES**, **37.5% for targeted cataract panels**, and **11% for microarray**; 16% of reviewed variants had discrepant reclassifications, emphasizing periodic reassessment (PMID: **36980880**). [166][174]

CMA, karyotyping, and FISH are not first-line tests for isolated familial CTRCT5 but may be appropriate with developmental delay, dysmorphism, multiple congenital anomalies, or a suspected genomic deletion. Mitochondrial and repeat-expansion tests are not routine.

### 10.4 Variant interpretation

- Use current ACMG/AMP criteria.
- Confirm transcript and residue numbering.
- Strong evidence includes DBD location, absence/rarity in gnomAD, segregation, de novo status, functional impairment of DNA binding, and consistent cataract morphology.
- Do not diagnose CTRCT5 from a VUS alone.
- Recessive variants outside the DBD require biallelic interpretation and may represent a different *HSF4*-related disease entity.

### 10.5 Differential diagnosis

| Differential | Distinguishing features/tests |
|---|---|
| Other isolated genetic cataracts | Similar morphology; multigene panel distinguishes *CRYAA/B*, *CRYBB2*, *CRYGD*, *GJA3*, *GJA8*, *MIP*, *BFSP1/2*, *MAF*, *PITX3*, etc. |
| Persistent fetal vasculature | Usually unilateral, microphthalmia, retrolental fibrovascular stalk |
| Retinoblastoma | Leukocoria with retinal mass/calcification; urgent dilated examination and ultrasound/imaging |
| Coats disease | Retinal telangiectasia and exudation rather than lens opacity |
| Retinopathy of prematurity | Prematurity and retinal vascular disease |
| Congenital glaucoma | Enlarged cloudy cornea, raised IOP, Haab striae |
| Maternal infection | Systemic/neonatal features plus targeted microbiologic evidence |
| Galactosemia | Feeding intolerance, jaundice, liver disease, sepsis risk, metabolic confirmation |
| Lowe syndrome | Cataract plus hypotonia, renal Fanconi syndrome and neurodevelopmental findings |
| Myotonic dystrophy and other syndromes | Extralenticular clinical findings and distinct molecular tests |

---

## 11. Outcome and prognosis

### 11.1 Survival and mortality

Classic isolated CTRCT5 is not expected to reduce life expectancy and has no known disease-specific mortality. Five- and ten-year survival statistics are therefore not applicable.

### 11.2 Visual prognosis

Prognosis depends mainly on:

- Opacity density, size and location.
- Unilateral versus bilateral disease.
- Age at recognition and surgery.
- Duration of visual deprivation.
- Quality and adherence to optical correction and patching.
- Associated nystagmus or strabismus.
- Postoperative glaucoma, visual-axis opacity, refractive error and retinal complications.

Anatomical removal of the cataract does not reverse established amblyopia. In the Infant Aphakia Treatment Study of unilateral congenital cataract, only about **25%** achieved 20/40 or better and **44%** had 20/200 or worse vision at age 10.5 years, despite specialist treatment; this is not *HSF4*-specific but illustrates the importance of early visual development. [341][344]

### 11.3 Complications

- Deprivation or anisometropic amblyopia.
- Strabismus and loss of stereopsis.
- Nystagmus in severe early bilateral disease.
- Glare, reduced contrast sensitivity and educational limitations.
- Surgical inflammation and visual-axis opacification.
- Aphakic or pseudophakic refractive error and progressive myopic shift.
- Secondary glaucoma requiring lifelong surveillance.
- Rare retinal detachment.

At ten years after unilateral infant cataract surgery, IATS estimated a **22%** cumulative glaucoma probability and **40%** probability of glaucoma or glaucoma-suspect status; rates were similar after primary IOL and aphakic/contact-lens management. [343]

---

## 12. Treatment

### 12.1 Current treatment algorithm

| Clinical situation | Management | Suggested NCIT intervention concept |
|---|---|---|
| Small peripheral/non-visually significant opacity | Observation, serial acuity/refraction, red-reflex photography where useful | Observation |
| Refractive error without major obstruction | Spectacles or contact lens; treat anisometropia | Corrective lens therapy |
| Visually significant unilateral cataract | Early cataract extraction, usually around 4–6 weeks if present from birth | Cataract surgery; lens extraction |
| Visually significant bilateral cataracts | Surgery generally by 6–8 weeks, commonly sequential operations | Cataract surgery |
| Infant left aphakic | Contact lens or aphakic spectacles, followed by later secondary IOL where appropriate | Contact lens therapy; intraocular lens implantation |
| Primary IOL in an infant | Individualized; no superior long-term acuity and more early reoperations in IATS | Intraocular lens implantation |
| Amblyopia | Immediate optical rehabilitation plus occlusion/patching or atropine when appropriate | Amblyopia therapy; occlusion therapy |
| Postoperative inflammation | Topical corticosteroid and cycloplegic regimen under ophthalmic care | Corticosteroid therapy |
| Secondary glaucoma | Medication, laser or glaucoma surgery according to severity | Glaucoma therapy/surgery |
| Low vision after treatment | Low-vision aids and educational accommodations | Vision rehabilitation |

A central opacity larger than approximately 3 mm, obscured fundus reflex, poor fixation, strabismus, or nystagmus generally indicates visual significance. [151]

### 12.2 Surgical details

Typical pediatric surgery may include:

- Lens aspiration/lensectomy.
- Anterior capsulotomy.
- Primary posterior capsulotomy and anterior vitrectomy in young children to reduce visual-axis opacification.
- Aphakic correction or age-dependent IOL implantation.
- Immediate and sustained amblyopia treatment.

In the randomized IATS, primary IOL implantation did **not** produce better visual acuity at age 10.5 years than aphakia corrected initially with contact lenses. The IOL group underwent more additional intraocular procedures—71 versus 38 by ten years. [336][341]

### 12.3 Pharmacotherapy

No medication reverses or reliably prevents established CTRCT5. Pharmacotherapy is supportive and perioperative rather than genotype-specific:

- Topical corticosteroids for postoperative inflammation.
- Cycloplegics/mydriatics postoperatively as indicated.
- Glaucoma-lowering medication when needed.
- Atropine penalization in selected amblyopia cases.

No established CPIC or PharmGKB genotype-guided prescribing recommendation exists for *HSF4*.

### 12.4 Experimental therapy

The major recent experimental lead is autophagy enhancement. In HSF4^del42^ mice, rapamycin—an mTOR inhibitor, **CHEBI:9168**—increased LC3-II, reduced p62, and improved removal of retained mitochondria, ER and Golgi. The study used 10 μM ex vivo and 7.5 mg/kg intraperitoneally in neonatal mice. It did not demonstrate restoration of human vision or establish pediatric safety. [348]

Therefore:

- Rapamycin is **not recommended clinically** for CTRCT5.
- No approved *HSF4* gene replacement, CRISPR, ASO, siRNA, mRNA, stem-cell or lens-regeneration treatment exists.
- No genotype-specific human clinical trial with an established NCT identifier was identified.
- Gene editing faces the additional challenge that dominant DBD variants may require allele-specific correction or silencing rather than simple gene supplementation.

---

## 13. Prevention

### 13.1 Primary prevention

The mutation cannot presently be prevented after conception. Reproductive options after identifying the familial variant include:

- Genetic counseling.
- Partner/family testing as appropriate.
- Prenatal diagnosis by chorionic-villus sampling or amniocentesis.
- IVF with preimplantation genetic testing for monogenic disease.
- Use of donor gametes or adoption.

Prenatal genotype predicts risk but not reliably cataract morphology or severity because expressivity is variable.

### 13.2 Secondary prevention

- Red-reflex examination in newborns and at subsequent well-child visits.
- Early ophthalmic assessment of infants with an affected parent.
- Cascade testing for the familial variant.
- Serial slit-lamp examinations in mildly affected or genotype-positive children.
- Prompt treatment before irreversible amblyopia.

### 13.3 Tertiary prevention

- Rapid postoperative optical correction.
- Sustained amblyopia therapy and adherence support.
- Lifelong IOP/glaucoma surveillance.
- Management of refractive change and visual-axis opacification.
- Low-vision, educational and psychosocial support when needed.

There is no relevant immunization or antimicrobial prophylaxis for genetic CTRCT5. Rubella vaccination prevents rubella-associated congenital cataract generally but does not prevent *HSF4*-mediated disease.

---

## 14. Other species and natural disease

| Species/breed | Taxonomy/ortholog | Natural phenotype and variant | Relevance |
|---|---|---|---|
| Dog, Boston Terrier | *Canis lupus familiaris*, NCBITaxon:9615; canine *HSF4* NCBI Gene 489766 | Recessive exon-9 cytosine insertion causing frameshift/truncation; early-onset bilateral progressive cataract | Strong natural large-animal homolog; PMID: **17611257** |
| Dog, Staffordshire Bull Terrier | NCBITaxon:9615 | Same/similar exon-9 insertion, g.85286582_85286583insC; recessive | Veterinary carrier screening and breeding relevance |
| Dog, French Bulldog and Miniature Pinscher | NCBITaxon:9615 | HSF4 insertion reported as recessive cataract risk in breed-screening literature | Commercial genetic testing |
| Dog, Australian Shepherd and related Miniature/Toy Shepherds | NCBITaxon:9615 | c.971delC/g.85286582delC; dominant or codominant with incomplete penetrance; heterozygotes often posterior cataract, homozygotes more severe nuclear/mature cataract | Approximately 17-fold increased binocular-cataract risk in carriers; PMID: **19883468** |
| Giant panda | *Ailuropoda melanoleuca*, NCBITaxon:9646 | A missense *HSF4* variant was reported in pandas with cataract, but causal certainty and phenotype terminology are less secure | Comparative evidence only |

Canine *HSF4* cataract illustrates how different lesions at the same locus produce recessive or semidominant disease and variable morphology. HSF4-associated cataracts have been reported in Australian/Miniature/Toy Shepherds, Boston Terriers, Staffordshire Bull Terriers, French Bulldogs, and Miniature Pinschers. [228][229]

There is no zoonotic potential and no cross-species transmission; these are independent inherited disorders.

---

## 15. Model organisms

| Model | Lesion/model type | Recapitulated features | Principal applications and limitations |
|---|---|---|---|
| *Hsf4* knockout mouse, *Mus musculus* NCBITaxon:10090; NCBI Gene 26386 | Targeted null by homologous recombination | Early postnatal progressive cataract, swollen/disorganized fibers, reduced γ-crystallins, *Bfsp1/2*, inclusion-like material, abnormal epithelial proliferation/differentiation | Strong lens-development model; null allele does not exactly model dominant human DBD variants |
| Lop11/ldis1 mouse | Early transposable-element insertion in intron 9 causing aberrant splicing/truncation | Recessive total cataract with vacuoles by approximately three weeks | Natural mutational model; inheritance differs from CTRCT5 |
| HSF4^del42^ mouse | CRISPR deletion of 42 amino acids in exon 5 region | Congenital cataract, senescence, defective autophagic flux and organelle clearance | Current autophagy/rapamycin model; deletion is not a common human CTRCT5 allele |
| *hsf4*-null zebrafish, *Danio rerio* NCBITaxon:7955; ZFIN gene ZDB-GENE-050306-18 | TALEN knockout | Early-onset cataract, epithelial overproliferation, disordered fibers, reduced p53/caspase-3 and failed denucleation | Excellent live developmental imaging and rescue assays; fish lens development differs from human infancy |
| HSF4-knockdown zebrafish | Morpholino/knockdown | Reduced *dnase2b*, incomplete denucleation | Demonstrates HSF4–DNASE2B pathway; transient knockdown limitations |
| Cultured human lens epithelial cells | Wild-type or mutant HSF4 transfection/knockout | Altered DNA binding, p53 stabilization, G1/S arrest, autophagy and proteomic changes | Human cellular context but does not reproduce mature avascular lens architecture |
| Ex vivo mouse lens | HSF4^del42^ lenses cultured with rapamycin | Partial improvement in membrane-bound-organelle clearance | Useful pharmacology platform; not proof of restored transparency or visual function |
| Lens organoids | 3-D differentiation models expressing *PAX6*, *PROX1*, *HSF4*, *CRYAB* | Elements of lens epithelial/fiber differentiation | Promising for patient-specific modeling; CTRCT5 validation remains limited |

The 2004 knockout study summarized its central observation as:

> “HSF4-null mice had cataract with abnormal lens fiber cells containing inclusion-like structures, probably due to decreased expression of γ-crystallin.” [197]

The 2009 investigators concluded that knockout mice only **partially** mimic human HSF4 cataract, an important limitation because the human dominant disorder usually involves a heterozygous DBD missense allele rather than biallelic absence of protein. [265]

---

## Overall evidence assessment

- **Gene–disease validity:** Strong/definitive for *HSF4* and autosomal-dominant CTRCT5, supported by linkage, segregation, de novo occurrence, variant clustering, functional assays, and multiple animal models. GenCC assessments identify a strong-to-definitive relationship. [29]
- **Core phenotype:** Isolated, usually bilateral, congenital or early-childhood cataract with variable morphology and frequent progression.
- **Best-supported human mechanism:** Dominant DBD variants impair HSF4 DNA-binding/transcriptional function.
- **Best-supported downstream biology:** Abnormal crystallin and beaded-filament expression, epithelial proliferation/fiber differentiation, p53 signaling, DNASE2B-mediated denucleation, lysosomal function, and ATG9A-dependent autophagy.
- **Major 2023–2024 development:** Identification of the HSF4→ATG9A autophagy axis and partial rescue of organelle-clearance defects with rapamycin in mice, complemented by a 2024 synthesis of HSF4 transgenic cataract models. This remains preclinical. [348][184]
- **Current standard of care:** Early detection, timely cataract extraction when visually significant, immediate optical correction, intensive amblyopia management, and lifelong glaucoma/refractive surveillance.
- **Principal knowledge gaps:** CTRCT5-specific prevalence, formal penetrance estimates, longitudinal natural history by genotype, human modifier genes, patient-derived single-cell/spatial data, and a safe molecular treatment that preserves or restores the native lens.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 51 |
| Resolved | 48 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 6 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0110255` (2 mentions) - the report calls it "Disease Ontology"; DOID calls it **cataract 5 multiple types**
- `NCBITaxon:9615` (4 mentions) - the report calls it "Dog, Staffordshire Bull Terrier", "Dog, French Bulldog and Miniature Pinscher", "Dog, Australian Shepherd and related Miniature/Toy Shepherds"; NCBITaxon calls it **Canis lupus familiaris**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0010700` (obsolete Total cataract) (1 mention) - replaced by `HP:0000518`

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCBITaxon:9615` - called "Dog, Staffordshire Bull Terrier", "Dog, French Bulldog and Miniature Pinscher", "Dog, Australian Shepherd and related Miniature/Toy Shepherds"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.