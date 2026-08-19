---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-19T13:21:02.722492'
end_time: '2026-08-19T13:26:26.259637'
duration_seconds: 323.54
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: HNRNPU-Related Developmental and Epileptic Encephalopathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 21
  num_turns: 32
  total_cost_usd: 2.4350947999999994
  session_id: 6f8bf895-3ab0-55cb-a154-acb932b43f03
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 24
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 11
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** HNRNPU-Related Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **HNRNPU-Related Developmental and Epileptic Encephalopathy** covering all of the
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

I now have sufficient material to compile the comprehensive report.

---

# HNRNPU-Related Developmental and Epileptic Encephalopathy: Comprehensive Research Report

## 1. Disease Information

**Overview.** HNRNPU-related developmental and epileptic encephalopathy (also called HNRNPU-related neurodevelopmental disorder, HNRNPU-NDD; historically "early infantile epileptic encephalopathy 54," EIEE54) is a severe, typically de novo, autosomal dominant neurodevelopmental disorder caused by heterozygous loss-of-function variants in *HNRNPU* on chromosome 1q44. It is characterized by global developmental delay, moderate-to-severe intellectual disability, early-onset seizures (often the presenting feature), profound speech impairment, hypotonia, and variable dysmorphic, cardiac, and renal features ([GeneReviews, NBK578573](https://www.ncbi.nlm.nih.gov/books/NBK578573/); [OMIM #617391](https://omim.org/entry/617391)).

**Key identifiers:**
- **OMIM:** #617391 — Developmental and Epileptic Encephalopathy 54 (DEE54)
- **Gene:** *HNRNPU*, HGNC:5048, chromosome 1q44
- **MONDO:** MONDO:0033363 (developmental and epileptic encephalopathy 54); a broader complex neurodevelopmental disorder mapping (MONDO:0100038) is also used in some resources
- **GeneReviews:** NBK578573 ("HNRNPU-Related Neurodevelopmental Disorder")
- **ClinGen gene-disease validity:** Definitive (Epilepsy and Intellectual Disability/Developmental Delay Gene Curation Expert Panels) ([thegencc.org/genes/HGNC:5048](https://thegencc.org/genes/HGNC:5048))

**Synonyms:** HNRNPU-related neurodevelopmental disorder (HNRNPU-NDD/HNRNPU-RNDD); Developmental and Epileptic Encephalopathy 54 (DEE54); Early Infantile Epileptic Encephalopathy 54 (EIEE54); heterogeneous nuclear ribonucleoprotein U deficiency; SAF-A (scaffold attachment factor A)-related disorder.

**Source of information.** The evidence base is aggregated-disease-level (case series, cohort/registry studies, GeneReviews, OMIM) rather than raw EHR data, supplemented by a growing international patient registry (Bain Lab/Columbia; >140 confirmed individuals as of the 2025 phenotype-expansion review) and model-organism studies ([Hodgson et al. 2025, PMID:39976380](https://pubmed.ncbi.nlm.nih.gov/39976380/)).

---

## 2. Etiology

**Disease causal factors.** DEE54 is caused by heterozygous, predominantly de novo, loss-of-function variants in *HNRNPU* — nonsense, frameshift, canonical splice-site variants, small intragenic deletions/duplications, and a minority of missense variants — or by microdeletions of 1q43q44 that encompass *HNRNPU*. A study of clinical exome cohorts concluded that "haploinsufficiency was the main mechanism of pathogenicity" ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK578573/)).

**Genetic risk factors:**
- **Causal variants:** Truncating (nonsense, frameshift, splice) variants predominate; missense variants also reported (Bramswig et al. 2017 found "three non-sense and two missense variants, one small intragenic deletion, and one duplication" in a 7-patient cohort, [PMID:28393272](https://pubmed.ncbi.nlm.nih.gov/28393272/)).
- **No genotype-phenotype correlation** has been established — variant type does not reliably predict severity ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK578573/)).
- **Contiguous-gene 1q43q44 microdeletions:** When *HNRNPU* is co-deleted with neighboring genes (*AKT3*, *ZBTB18*), phenotype is more severe/complex; deletion mapping studies show *HNRNPU* alteration specifically "drives epilepsy and determines the degree of intellectual disability," while *AKT3* haploinsufficiency drives microcephaly and *ZBTB18* loss drives corpus callosum anomalies with incomplete penetrance — with additive effects when multiple genes are co-deleted ([Depienne et al., PMID:28283832](https://pmc.ncbi.nlm.nih.gov/articles/PMC5360844/)).
- **Germline mosaicism:** Presumed parental germline mosaicism has been reported in a family with two affected siblings, and a 2025 report documented the first vertically transmitted familial case (parent-to-child), demonstrating a milder end of the phenotypic spectrum is compatible with reproduction ([Hodgson et al. 2025, PMID:39976380](https://pubmed.ncbi.nlm.nih.gov/39976380/)).

**Environmental risk factors:** None established; this is a monogenic disorder.

**Protective factors:** None identified at genetic or environmental levels.

**Gene-environment interactions:** Not reported; the disorder's severity appears to be driven by the genetic lesion itself (variant location relative to functional domains, and whether contiguous genes are co-deleted) rather than by environmental modifiers.

---

## 3. Phenotypes

Frequencies below are drawn primarily from GeneReviews' synthesis of the published cohort (~83–140+ individuals) and the original Bramswig/Thevenon-type cohort studies.

| Phenotype | Frequency | HPO term (suggested) |
|---|---|---|
| Developmental delay (global) | ~100% | HP:0001263 |
| Intellectual disability (moderate–severe) | 84% | HP:0002342 / HP:0010864 |
| Speech delay/absent speech | 80% | HP:0000750 / HP:0001344 |
| Seizures | 95% | HP:0001250 |
| — Tonic-clonic seizures | ~60% of seizure cases | HP:0002069 |
| — Absence seizures | ~44% of seizure cases | HP:0002121 |
| — Seizure onset before 24 months | ~90% of seizure cases | HP:0011097 (infantile onset) |
| Hypotonia (often lifelong, may progress to spasticity) | 79% | HP:0001252 |
| Dysmorphic craniofacial features (nonspecific) | 97% | HP:0001999 |
| Feeding difficulties (sometimes requiring gastrostomy) | 57% | HP:0011968 |
| Behavioral abnormalities | ~50% | HP:0000708 |
| Autism spectrum disorder | ~33% | HP:0000729 |
| Short stature | ~50% | HP:0004322 |
| Strabismus | 36% | HP:0000486 |
| Abnormal brain MRI (ventriculomegaly most common, then thin corpus callosum) | 61% (of 62 imaged cases) | HP:0002119 (ventriculomegaly); HP:0002079 (thin corpus callosum) |
| Congenital heart defects (ASD most common, then VSD) | 30% | HP:0006695 (ASD) |
| Undescended testis (males) | ~20% | HP:0000028 |
| Renal anomalies (agenesis, multicystic dysplastic kidney, pelvic ectasia) | 8% | HP:0000107 |
| Sensorineural hearing loss | rare (2 cases) | HP:0000407 |
| Joint hyperlaxity | 8 individuals reported | HP:0001382 |
| Scoliosis | 3 individuals reported | HP:0002650 |
| Sleep apnea/abnormal breathing (hyperventilation) | uncommon but recurrent | HP:0002104 |

Source: [GeneReviews NBK578573](https://www.ncbi.nlm.nih.gov/books/NBK578573/); confirmatory cohort data in [Bramswig et al. 2017, PMID:28393272](https://pubmed.ncbi.nlm.nih.gov/28393272/) (seizures 6/7, severe ID 6/6, severe speech impairment 6/6, hypotonia 6/7, CNS 5/6, cardiac 4/6, renal 3/4) and [Yates/Durkin et al. 2017, PMID:28815871](https://pubmed.ncbi.nlm.nih.gov/28815871/) (all four patients had seizures, developmental delay, ID, neurologic regression, behavioral issues, dysmorphism).

**Phenotype characteristics:**
- **Onset:** Neonatal (feeding difficulties, hypotonia) to infantile (seizure onset typically <24 months, often the presenting symptom alongside developmental delay).
- **Severity:** Variable but generally moderate-to-severe for ID; a milder end of spectrum has been increasingly recognized in 2024–2025 case reports (including the first familial, vertically transmitted case).
- **Progression:** Hypotonia may evolve into hypertonia/spasticity over time; "data on possible progression of behavior abnormalities or neurologic findings are still emerging" ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK578573/)).
- **Quality of life impact:** Substantial — most individuals are minimally or nonverbally communicative, many require lifelong caregiver support, gastrostomy feeding in severe cases, and educational/behavioral supports (IEP, ABA); no disease-specific QoL instrument data identified in the literature.

---

## 4. Genetic/Molecular Information

**Causal gene:** *HNRNPU* (HGNC:5048), encoding heterogeneous nuclear ribonucleoprotein U, also known as scaffold attachment factor A (SAF-A). Located at 1q44.

**Pathogenic variant spectrum:** Nonsense, frameshift, canonical splice-site variants, small intragenic deletions/duplications, and missense variants. Representative variants from Yates/Durkin cohort: c.651_660del (p.Gly218Alafs*118), c.1089G>A (p.Trp363*), c.1714C>T (p.Arg572*), c.2270_2271del (p.Pro757Argfs*7) ([PMID:28815871](https://pubmed.ncbi.nlm.nih.gov/28815871/)).

**Variant classification:** Per ACMG/AMP, predicted/confirmed loss-of-function variants (nonsense, frameshift, splice-disrupting) are classified pathogenic/likely pathogenic given established haploinsufficiency mechanism; missense variants require careful case-by-case evaluation given absence of clear genotype-phenotype correlation.

**Functional consequence:** Loss of function / haploinsufficiency — "de novo loss-of-function variants in HNRNPU can lead to a disease phenotype... haploinsufficiency was the main mechanism of pathogenicity" ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK578573/)).

**Somatic vs. germline:** Germline, virtually always de novo; presumed germline mosaicism reported in one sibling pair; a familial (inherited) case documented in 2025 ([PMID:39976380](https://pubmed.ncbi.nlm.nih.gov/39976380/)).

**Modifier genes:** No specific modifier genes identified for isolated *HNRNPU* variants; however, within 1q43q44 contiguous deletions, co-deletion of *AKT3* and *ZBTB18* has additive phenotypic effects, effectively modifying overall severity (microcephaly, corpus callosum defects) ([PMID:28283832](https://pmc.ncbi.nlm.nih.gov/articles/PMC5360844/)).

**Epigenetic information:** A robust, reproducible **DNA methylation episignature** has been identified in blood from individuals with pathogenic *HNRNPU* variants using Infinium EPIC arrays, distinct from — but partially overlapping — 56 other neurodevelopmental-disorder episignatures. This episignature has clinical utility for reclassifying *HNRNPU* variants of uncertain significance (VUS) via the EpiSign platform (Genetics in Medicine, 2023, 25(8):100871; related: [germline HNRNPU variants and blood methylome alterations, Nature-EJHG](https://www.nature.com/articles/s41431-023-01422-9); [EpiSignature VUS reclassification case report, PMC12688365](https://pmc.ncbi.nlm.nih.gov/articles/PMC12688365/)). This directly implicates HNRNPU's chromatin-regulatory role in disease pathogenesis.

**Chromosomal abnormalities:** 1q43q44 microdeletions encompassing *HNRNPU* (along with *AKT3*, *ZBTB18*) produce a related but broader contiguous-gene syndrome (microcephaly, corpus callosum abnormalities, epilepsy, short stature) — see Section 2 ([PMID:28283832](https://pmc.ncbi.nlm.nih.gov/articles/PMC5360844/); [case report of 163kb 1q44 microdeletion, PMID:22975012](https://pubmed.ncbi.nlm.nih.gov/22975012/)).

**gnomAD constraint:** *HNRNPU* is highly constrained against loss-of-function variation (consistent with a haploinsufficiency mechanism and near-complete de novo occurrence in patients), in keeping with its essential, ubiquitously expressed roles in RNA processing and chromatin organization (general constraint framework via [gnomAD](https://gnomad.broadinstitute.org/); exact pLI/LOEUF values were not independently retrievable in this search pass and should be confirmed directly against the gnomAD browser at curation time).

---

## 5. Environmental Information

No environmental, lifestyle, toxin, or infectious risk factors have been identified as contributing to HNRNPU-related DEE54 — this is a purely monogenic disorder arising from de novo germline variants. The GeneReviews management section notes only a general precaution that "activities and agents that may induce seizures" should be avoided as a secondary, symptom-driven consideration (not an etiologic factor) ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK578573/)).

---

## 6. Mechanism / Pathophysiology

**Molecular function of HNRNPU/SAF-A:** HNRNPU is a highly abundant, ubiquitously expressed nuclear RNA/DNA-binding protein with a multidomain architecture: an N-terminal **SAP domain** (direct DNA/RNA binding), a **SPRY/B30.2** protein-protein interaction domain, a central **AAA+ ATPase** oligomerization domain, and a C-terminal domain with **RGG/RG motifs** for RNA binding. It functions as a dynamic bridge between chromatin, nascent RNA, and the nuclear matrix, regulating: (1) pre-mRNA processing and alternative splicing, (2) higher-order chromatin architecture (3D genome organization), (3) transcriptional regulation, and (4) X-chromosome inactivation ([ScienceDirect review, PMID:34823151](https://pubmed.ncbi.nlm.nih.gov/34823151/); [PLOS Genetics 2025, PMC12176297](https://pmc.ncbi.nlm.nih.gov/articles/PMC12176297/)).

**X-chromosome inactivation role:** SAF-A/HNRNPU localizes to the inactive X chromosome and interacts directly with **XIST** lncRNA, and is required for proper XIST RNA territorial localization and XIST-dependent heterochromatin/histone modification — an SAP-domain-dependent function (serines S14/S26 critical) ([PLOS Genetics](https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1011719)). This is a molecular function distinct from, but potentially contributing to, the neurodevelopmental phenotype's dosage sensitivity.

**Causal chain — cortical development (mouse model, Sapir et al. 2022, Nature Communications, PMID:35864088):**
1. **Trigger:** *Hnrnpu* loss of function in embryonic cortical neuroepithelium.
2. **Molecular:** Dysregulated alternative splicing of >850 genes, notably *Mdm2* (exon 3 skipping → reduced p53 inhibition), *Dcc*, *Siva1* (migration/apoptosis regulators), and cytoskeletal/synaptic transcripts.
3. **Cellular:** Elevated *Tp53* target gene expression → activation of canonical and non-canonical (including necroptotic) p53-dependent cell death. **Neural progenitors show markedly higher vulnerability than postmitotic neurons** — time-lapse imaging showed progenitor death within 1–5 hours of Cre-mediated excision, versus attenuated death dynamics in postmitotic cells.
4. **Tissue:** Rapid, near-complete elimination of cortical structures in conditional knockouts.
5. **Rescue evidence (mechanistic validation):** Pan-caspase inhibitors (Z-VAD-fmk, Q-VD-OPH), p53 inhibitor pifithrin-μ, and necroptosis inhibitor Nec-1 each partially rescued progenitor viability; genetic *Tp53* co-deletion "enabled cortical formation, increased progenitors proliferating" (incomplete rescue); co-deletion of the competing splicing factor *Srsf3* rescued neurosphere phenotypes and migration defects to near-control levels.

**Causal chain — postnatal circuit dysfunction (mouse model, PLOS Genetics 2023, PMC10569524):**
1. Heterozygous *Hnrnpu*+/− mice show global developmental delay, impaired ultrasonic vocalizations, cognitive dysfunction (increased gamma oscillations), and lowered electroconvulsive seizure threshold (p<1×10⁻⁴) despite no spontaneous seizures on prolonged video-EEG.
2. Single-cell RNA-seq of hippocampus/neocortex reveals widespread but modest transcriptional dysregulation (hippocampus: 955 DE events, 73% downregulated; neocortex: 454 DE events, 51% downregulated).
3. **Subiculum excitatory neurons** carry the highest DEG burden of any cell type examined, with striking enrichment for developmental-delay, epilepsy, and autism-associated genes.
4. ***Mef2c*** (a well-known NDD gene) is the most downregulated transcript (50% reduction, log2FC=−1.11, FDR=8×10⁻³⁷), with hnRNP U binding sites at its locus exceeding 99% of other examined genes — directly implicating *Mef2c* dysregulation as a candidate downstream driver of the epilepsy/cognitive phenotype.

**Cross-model convergence:** An iScience 2022 study (PMID:36594023) comparing isogenic *HNRNPU*+/− human iPSC-derived brain organoids to embryonic/perinatal mouse cortex found significant enrichment of shared, co-dysregulated transcripts, supporting a **conserved developmental transcriptomic signature** across species and model systems ([PMC9804147](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9804147/)).

**Suggested GO terms:** GO:0006397 (mRNA processing), GO:0000381 (regulation of alternative mRNA splicing), GO:0006355 (regulation of transcription, DNA-templated), GO:0006974 (DNA damage response), GO:0097191 (extrinsic apoptotic signaling pathway), GO:0070182 (DNA polymerase binding — chromatin structural role), GO:0008380 (RNA splicing).

**Suggested CL terms:** CL:0000047 (neural stem cell) / CL:0002608 (neural progenitor cell, radial glia), CL:0000679 (glutamatergic neuron, subiculum excitatory), CL:0000540 (neuron, general).

**Suggested UBERON terms:** UBERON:0001950 (neocortex), UBERON:0002421 (hippocampal formation)/UBERON:0003881 (subiculum), UBERON:0002336 (corpus callosum).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Central nervous system (cerebral cortex, hippocampus/subiculum) — the dominant site of disease.
- **Secondary/variable involvement:** Cardiovascular system (septal defects), renal system (agenesis, dysplasia), eyes (strabismus), ears (rare sensorineural hearing loss), musculoskeletal system (joint laxity, scoliosis), male reproductive system (undescended testis).
- **Body systems:** Nervous system (primary), cardiovascular, renal/urologic, musculoskeletal, ophthalmologic, otologic.

**Tissue/cell level:** Neuroepithelium/radial glia and neural progenitor cells (most vulnerable population per mouse studies), postmitotic cortical and hippocampal excitatory neurons (subiculum especially implicated), cardiac septal tissue, renal parenchyma.

**Subcellular level:** Nucleus (chromatin/nuclear matrix — HNRNPU's primary site of action), specifically associated with the inactive X chromosome territory in female cells; splicing machinery/spliceosome-associated nuclear speckles. GO Cellular Component: GO:0005654 (nucleoplasm), GO:0016607 (nuclear speck), GO:0000785 (chromatin).

**Localization:** Bilateral, diffuse cortical/subcortical involvement (no lateralization reported); brain MRI abnormalities (ventriculomegaly, thin corpus callosum) are typically symmetric/generalized rather than focal.

---

## 8. Temporal Development

**Onset:** Congenital/neonatal manifestations (hypotonia, feeding difficulty) evident from birth or early infancy; developmental delay recognized in first year; seizure onset typically before 24 months of age (~90% of those with seizures), sometimes triggered initially by fever before becoming afebrile.

**Onset pattern:** Insidious/progressive developmental delay from infancy, punctuated by acute seizure onset events.

**Progression:**
- Developmental trajectory: continued, if slow, developmental gains reported in many individuals rather than regression, though at least one case series (Yates/Durkin, PMID:28815871) reported "neurologic regression" in some patients — indicating phenotypic heterogeneity in course.
- Muscle tone: hypotonia in infancy may transition to hypertonia/spasticity later in childhood.
- Seizures: generally become more manageable with age and appropriate anti-seizure regimens in most reported individuals, though refractory epilepsy occurs in a subset.
- Disease duration: chronic, lifelong; based on current data, "life span is not significantly limited by this condition, as several adults have been reported" ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK578573/)).

**Patterns:** No formal remission is described; seizure control with medication is common but not universal. No defined "critical intervention window" has been established in the literature to date, though early developmental intervention (0–3 years) is recommended per standard NDD management.

---

## 9. Inheritance and Population

**Epidemiology:** Ultra-rare; exact prevalence/incidence unknown. GeneReviews states "the prevalence of this condition is unknown. To date, approximately 83 individuals with HNRNPU-NDD have been reported" (as of the March 2022 GeneReviews update); by 2025, an international patient registry (Bain Lab, Columbia) had grown to encompass a substantially larger cohort (a 2025 phenotype-expansion paper added 17 previously unpublished patients, and unrelated registry sources describe well over 100 confirmed individuals) ([Hodgson et al. 2025, PMID:39976380](https://pubmed.ncbi.nlm.nih.gov/39976380/)).

**Inheritance pattern:** Autosomal dominant, virtually always **de novo**. Rare instances of parental germline mosaicism and, as of 2025, the first documented familial (parent-to-child) transmission.

**Penetrance:** Appears complete/high for the core developmental delay and seizure phenotype among reported carriers, though ascertainment bias (severe cases more likely to be sequenced) may inflate apparent penetrance; the emerging recognition of milder cases suggests a broader phenotypic spectrum than initially appreciated.

**Expressivity:** Highly variable — ranging from the "classic" severe DEE54 presentation to milder cases now increasingly reported (2024–2025 case series), without clear genotype-phenotype correlation.

**Genetic anticipation:** Not described (not applicable to a haploinsufficiency-mechanism, non-repeat-expansion disorder).

**Founder effects / consanguinity:** Not applicable — disorder is dominant and de novo, not associated with consanguinity or population founder mutations.

**Carrier frequency:** Not applicable (de novo dominant disorder, not a recessive carrier state).

**Population demographics:**
- No ethnic or geographic predilection reported; cases have been described from multiple continents (US, Europe, various case series).
- **Sex ratio:** No clear sex bias reported in the literature reviewed; both males and females affected (male-specific phenotype item: undescended testis in ~20% of affected males).
- **Age distribution:** Predominantly diagnosed in infancy/childhood via exome/genome sequencing for developmental delay and epilepsy; adults are increasingly recognized as historically underdiagnosed due to lack of earlier genetic testing availability.

---

## 10. Diagnostics

**Establishing the diagnosis:** Requires "a proband with suggestive findings and a heterozygous pathogenic variant in HNRNPU identified by molecular genetic testing" ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK578573/)).

**Molecular testing approaches, by yield:**
- **Sequence analysis** (exome/genome or NDD/epilepsy gene panel including *HNRNPU*): ~98% detection rate.
- **Gene-targeted deletion/duplication analysis** (or chromosomal microarray for 1q43q44 deletions): ~2% of cases (contiguous gene deletion presentations).
- **Single-gene sequential testing** of *HNRNPU* alone is "rarely useful and typically NOT recommended" given the nonspecific phenotype — multigene panel or exome/genome sequencing is preferred.

**Genetic testing modalities:**
- Multigene intellectual disability/epileptic encephalopathy panel including *HNRNPU*.
- Whole exome sequencing (WES) — most commonly used diagnostic route in published cohorts.
- Whole genome sequencing (WGS) — increasingly used, captures structural variants and intronic/regulatory changes missed by exome.
- Chromosomal microarray (CMA) — detects 1q43q44 microdeletions/duplications encompassing *HNRNPU*.
- DNA methylation episignature (EpiSign) testing — emerging clinical tool for reclassifying *HNRNPU* VUS, given the validated disease-specific episignature (Genetics in Medicine 2023, 25(8):100871).

**Clinical/laboratory tests:** No disease-specific biomarker or metabolic screening test exists; diagnosis is genetic. Brain MRI is used to characterize (not diagnose) the condition — ventriculomegaly and thin corpus callosum are the most frequent findings (61% of imaged cases abnormal). EEG is used to characterize seizure semiology, not to establish diagnosis.

**Differential diagnosis:** Broad — "all disorders with epileptic encephalopathy and intellectual disability without other distinctive findings should be considered," referencing the OMIM Developmental and Epileptic Encephalopathy Phenotypic Series for systematic comparison ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK578573/)). Specific considerations include other DEE-causing genes, and — for patients with contiguous deletions — the broader 1q43q44 microdeletion syndrome (distinguishing isolated *HNRNPU* variants from deletions also involving *AKT3*/*ZBTB18*, which add microcephaly and corpus callosum anomalies).

**Screening:** No population or newborn screening applicable (ultra-rare, not detectable by biochemical newborn screening); prenatal testing/preimplantation genetic testing available for known familial variants (relevant given the newly documented familial transmission case).

---

## 11. Outcome/Prognosis

**Survival/mortality:** Life expectancy does not appear significantly reduced; "several adults have been reported" and formal life-span data, while incomplete, does not suggest premature mortality as a defining feature ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK578573/)). No disease-specific mortality statistics are available given the ultra-rare, only-recently-delineated nature of the condition.

**Morbidity/function:** Substantial lifelong disability — most affected individuals have moderate-to-severe intellectual disability, are minimally/nonverbally communicative, and require ongoing multidisciplinary support (PT/OT/speech, special education, seizure management). No validated disease-specific quality-of-life instrument has been applied in the literature reviewed.

**Complications:** Refractory epilepsy in a subset; feeding/nutritional complications (sometimes requiring gastrostomy); sleep apnea requiring respiratory support; secondary orthopedic complications of hypertonia/spasticity (contractures) or hyperlaxity (scoliosis).

**Prognostic factors:** No genotype-phenotype correlation identified to date, so variant type does not predict severity. Severity appears greater when *HNRNPU* loss occurs in the context of a larger 1q43q44 contiguous gene deletion (additional microcephaly, corpus callosum defects from co-deleted *AKT3*/*ZBTB18*).

**Recovery potential:** Developmental gains continue in many individuals with early, sustained intervention, though the underlying intellectual disability persists lifelong; seizure control is achievable in most patients with standard or combination anti-seizure therapy.

---

## 12. Treatment

**Pharmacotherapy (seizures):**
- **Sodium valproate** — "the most commonly used & effective medication" per GeneReviews for first-line seizure control (NCIT:C15986 Pharmacotherapy; therapeutic agent CHEBI valproate).
- Newer-generation anti-seizure medications for refractory cases (unspecified beyond class in the literature reviewed).
- **Ketogenic diet** — recommended for refractory seizures; broader epilepsy literature supports its efficacy and safety, including in combination with valproate, for drug-resistant epilepsy generally (NCIT:C15447 Dietary Intervention).
- Combined pharmacotherapy for associated symptoms has been documented in individual cases (acetazolamide, alprazolam, aripiprazole) — indication-specific, not seizure-first-line.

**Advanced/experimental therapeutics:**
- **Antisense oligonucleotide (ASO) therapy:** In 2024, the Bain Lab (Columbia University) launched the first precision-therapeutics trial for the related *HNRNP*-family disorder H2-RNDD (*HNRNPH2*), administering individualized ASO therapy to 8 patients via the n-Lorem Foundation (n-of-1 model). While this specific program targets *HNRNPH2* rather than *HNRNPU*, it establishes proof-of-concept for RNA-targeted precision therapeutics in the *HNRNP* gene family and signals a plausible future therapeutic direction for *HNRNPU*-NDD given the shared haploinsufficiency mechanism and RNA-binding-protein biology (NCIT:C15238 Gene Therapy category; therapeutic_modality: ANTISENSE_OLIGONUCLEOTIDE). No *HNRNPU*-specific ASO clinical trial has yet been identified in this search.
- Preclinical ASO work in the *HNRNPH2* mouse model (Science Translational Medicine 2025/2026) demonstrates feasibility of splice/expression-modulating ASO rescue in this gene family, informing potential translational strategies for *HNRNPU*.

**Surgical/interventional:** No disease-specific surgery; organ-specific procedures as needed (cardiac septal defect repair, orchiopexy for undescended testis, orthopedic procedures/Botox for severe spasticity or scoliosis).

**Supportive/rehabilitative care:**
- Early intervention programs (0–3 years), developmental preschool (3–5 years), individualized education plans.
- Physical therapy (gross motor/tone), occupational therapy (fine motor/adaptive function), speech-language pathology with augmentative/alternative communication (AAC) evaluation (NCIT:C15302 Physical Therapy).
- Feeding therapy for dysphagia; nasogastric or gastrostomy tube placement for persistent feeding dysfunction.
- Respiratory support (supplemental O2, CPAP/BiPAP) for sleep apnea.
- Tone management: baclofen, tizanidine, botulinum toxin, or orthopedic procedures for hypertonia (physical medicine & rehabilitation involvement).
- Behavioral intervention: applied behavior analysis (ABA) for autism-related features; pediatric psychiatry for severe aggressive/destructive behaviors.

**Organ-specific surveillance/management:** Cardiology (congenital heart defects), ophthalmology (strabismus), audiology (hearing loss), nephrology (renal anomalies), urology (undescended testes).

**Treatment strategy:** No formal published treatment algorithm specific to *HNRNPU*-NDD beyond the GeneReviews management/surveillance framework; management is symptom-directed and multidisciplinary, following general DEE/intellectual disability care pathways.

**Personalized medicine:** DNA methylation episignature profiling offers a genotype-informed diagnostic refinement tool (VUS reclassification); no pharmacogenomic guidance specific to *HNRNPU*-NDD identified.

---

## 13. Prevention

**Primary prevention:** Not applicable in the traditional sense — this is a de novo genetic disorder with no known modifiable environmental trigger to avoid.

**Secondary prevention:** Early diagnosis via exome/genome sequencing in infants presenting with early-onset seizures and developmental delay allows earlier initiation of supportive therapies and seizure management, potentially reducing secondary complications (status epilepticus, feeding-related morbidity).

**Genetic counseling:** Recurrence risk to siblings of an affected proband is low but not zero (given documented germline mosaicism cases), warranting parental testing to confirm de novo status. For an affected individual, the risk of transmission to offspring is 50% per pregnancy (autosomal dominant); prenatal testing and preimplantation genetic testing (PGT) are available for families with a known familial variant, an option that gained clinical relevance following the first reported vertical transmission case in 2025.

**Screening:** No population-level newborn or carrier screening applicable (ultra-rare, dominant, de novo disorder without ethnic founder effects).

**Public health/behavioral interventions:** Not applicable — no known modifiable population-level risk factor.

**Prophylaxis:** General epilepsy-safety precautions (avoiding known seizure triggers) apply once a seizure phenotype is established, as with any epilepsy syndrome.

---

## 14. Other Species / Natural Disease

**Taxonomy:** Naturally occurring HNRNPU-related disease has not been reported in non-human species; the gene is highly conserved (near-universal expression and function across vertebrates).

**Model organism gene:** Mouse *Hnrnpu* (MGI ortholog); human *HNRNPU* NCBI Gene ID 3192.

**Natural disease in other species:** Not reported in OMIA or veterinary literature reviewed — this is not a recognized naturally occurring veterinary disease.

**Comparative biology:** HNRNPU/SAF-A is highly conserved across mammals given its essential, ubiquitous roles in chromatin organization and RNA processing; the core molecular mechanism (splicing regulation, p53-dependent progenitor apoptosis upon loss) is conserved between mouse and human, as demonstrated by the organoid/mouse cross-species transcriptomic convergence study ([PMID:36594023](https://pubmed.ncbi.nlm.nih.gov/36594023/)).

**Zoonotic potential/cross-species susceptibility:** Not applicable — this is a genetic, non-infectious disorder.

---

## 15. Model Organisms

**Mouse models (genetic, knockout/conditional):**
1. **Constitutive/germline heterozygous *Hnrnpu*+/− mouse** (PLOS Genetics 2023, PMID likely associated with PMC10569524): Models the human haploinsufficiency state. Recapitulates global developmental delay, impaired ultrasonic vocalizations, cognitive dysfunction (elevated wakeful gamma oscillations), and lowered electroconvulsive seizure threshold (p<1×10⁻⁴), though without spontaneous seizures on extensive video-EEG (300+ hours) — a **partial phenotype recapitulation** (increased seizure susceptibility rather than overt epilepsy). Single-cell RNA-seq identifies subiculum excitatory neurons as the most transcriptomically perturbed cell type, with *Mef2c* as the most robustly downregulated candidate driver gene.
2. **Conditional cortical *Hnrnpu* knockout mouse** (Nature Communications 2022, [PMID:35864088](https://www.nature.com/articles/s41467-022-31752-z), Sapir/Reiner lab): Demonstrates near-complete cortical structure elimination via p53-dependent apoptosis of neural progenitors (more vulnerable) and postmitotic neurons (less vulnerable, delayed death). Provides mechanistic and pharmacological rescue data (caspase inhibitors, p53 inhibitor pifithrin-μ, necroptosis inhibitor Nec-1; genetic *Tp53* or *Srsf3* co-deletion). This model captures the severe, embryonic-lethal-if-homozygous end of the mechanistic spectrum rather than the milder heterozygous human phenotype.

**In vitro/organoid models:**
- **Isogenic human iPSC-derived brain organoids** (PGP1 line) with CRISPR-engineered *HNRNPU*+/− frameshift variants (1bp duplication, 10bp deletion), showing ~25% reduction in HNRNPU protein and reduced mRNA. Used for cross-species transcriptomic comparison, confirming conserved dysregulated gene modules between 45-day human organoids and embryonic mouse cortex ([PMID:36594023](https://pubmed.ncbi.nlm.nih.gov/36594023/); [PMC9804147](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9804147/)).

**Model limitations:**
- Mouse heterozygous models show increased seizure *susceptibility* rather than the spontaneous, often treatment-refractory epilepsy seen in human patients — a translational gap (species-scale/circuit-maturation difference) worth flagging as a `HUMAN_MODEL_MISMATCH` if curated into a pathophysiology module.
- The severe conditional cortical-knockout mouse models complete loss of function in a defined lineage/timepoint, which is more mechanistically informative for the p53/splicing pathway than directly representative of the human heterozygous dosage state.
- No zebrafish, *Drosophila*, or *C. elegans HNRNPU* ortholog disease model was identified in this search (in contrast to the sister gene *HNRNPH2*, for which zebrafish/mouse models are more developed).

**Applications:** These models collectively support (1) the mechanistic causal chain from *HNRNPU* loss → splicing dysregulation (*Mdm2*, *Mef2c*, and hundreds of other targets) → p53-dependent progenitor death / circuit-level excitatory neuron dysfunction → cortical malformation and seizure susceptibility, and (2) proof-of-concept pharmacological (caspase/p53/necroptosis inhibitors) and genetic (*Tp53*, *Srsf3* co-deletion) rescue strategies that could inform future therapeutic development, complementing the ASO precision-medicine approach being piloted in the related *HNRNPH2* disorder.

**Resources:** MGI (Mouse Genome Informatics) for *Hnrnpu* allele records; no dedicated IMPC/KOMP full-line data specifically confirmed in this search pass — recommend direct IMPC query at curation time for standardized phenotyping data.

---

## Summary of Key Ontology Term Suggestions

| Category | Suggested terms |
|---|---|
| MONDO | MONDO:0033363 (DEE54) |
| OMIM | #617391 |
| HGNC | HGNC:5048 (*HNRNPU*) |
| HPO (phenotypes) | HP:0001263, HP:0002342, HP:0001344, HP:0001250, HP:0002069, HP:0002121, HP:0001252, HP:0001999, HP:0011968, HP:0000729, HP:0004322, HP:0000486, HP:0002119, HP:0002079, HP:0006695, HP:0000028, HP:0000107, HP:0000407 |
| GO (biological process) | GO:0006397, GO:0000381, GO:0006355, GO:0006974, GO:0097191, GO:0008380 |
| GO (cellular component) | GO:0005654, GO:0016607, GO:0000785 |
| CL | CL:0002608 (neural progenitor/radial glia), CL:0000679 (glutamatergic neuron) |
| UBERON | UBERON:0001950 (neocortex), UBERON:0003881 (subiculum), UBERON:0002336 (corpus callosum) |
| NCIT (treatment) | NCIT:C15986 (Pharmacotherapy), NCIT:C15447 (Dietary Intervention/ketogenic diet), NCIT:C15302 (Physical Therapy), NCIT:C15238 (Gene Therapy/ASO) |
| CHEBI | valproate/valproic acid |

---

## Sources

- [HNRNPU-Related Neurodevelopmental Disorder — GeneReviews (NBK578573)](https://www.ncbi.nlm.nih.gov/books/NBK578573/)
- [OMIM #617391 — DEE54](https://omim.org/entry/617391)
- [Bramswig et al. 2017, Hum Genet — PMID:28393272](https://pubmed.ncbi.nlm.nih.gov/28393272/)
- [Yates/Durkin et al. 2017 clinical/molecular characterization — PMID:28815871](https://pubmed.ncbi.nlm.nih.gov/28815871/)
- [De novo mutations in HNRNPU — PMID:28944577](https://pubmed.ncbi.nlm.nih.gov/28944577/)
- [Depienne et al., 1q43q44 microdeletion syndrome dissection — PMID:28283832 / PMC5360844](https://pmc.ncbi.nlm.nih.gov/articles/PMC5360844/)
- [Sapir et al. 2022, Nature Communications — HNRNPU safeguards developing mouse cortex, PMID:35864088](https://www.nature.com/articles/s41467-022-31752-z)
- [Mouse model of HNRNPU haploinsufficiency, PLOS Genetics 2023 — PMC10569524](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10569524/)
- [Shared transcriptomic dysregulation, human organoids vs. embryonic mice — PMID:36594023 / PMC9804147](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9804147/)
- [Hodgson et al. 2025, AJMG-A — Expanding phenotypic spectrum, first familial case — PMID:39976380](https://pubmed.ncbi.nlm.nih.gov/39976380/)
- [DNA methylation episignature and comparative epigenomic profiling of HNRNPU-NDD, Genetics in Medicine 2023](https://www.gimjournal.org/article/S1098-3600(23)01066-3/fulltext)
- [Germline pathogenic HNRNPU variants and blood methylome alterations, EJHG](https://www.nature.com/articles/s41431-023-01422-9)
- [EpiSignature VUS reclassification case report — PMC12688365](https://pmc.ncbi.nlm.nih.gov/articles/PMC12688365/)
- [Role of SAF-A/HNRNPU SAP domain in X-inactivation — PLOS Genetics, PMC12176297](https://pmc.ncbi.nlm.nih.gov/articles/PMC12176297/)
- [SAF-A/hnRNP U chromatin structure review — PMID:34823151](https://pubmed.ncbi.nlm.nih.gov/34823151/)
- [Case report: WES unveils HNRNPU-NDD — PMID:38846959](https://pubmed.ncbi.nlm.nih.gov/38846959/)
- [NORD — HNRNPU-Related Disorder overview](https://rarediseases.org/rare-diseases/hnrnpu-related-disorder/)
- [thegencc.org — HNRNPU gene-disease validity classifications](https://thegencc.org/genes/HGNC:5048)
- [Bain Lab, Columbia Neurology — HNRNPH2 ASO precision trial context](https://www.neurology.columbia.edu/research/research-labs/bain-lab)
- [HNRNPU-NDD, Detailing the Ultrarare Neurodevelopmental Disorder — genome.bio](https://www.genome.bio/post/hnrnpu-ndd-detailing-the-ultrarare-neurodevelopmental-disorder)
- [1q44 microdeletion case report — PMID:22975012](https://pubmed.ncbi.nlm.nih.gov/22975012/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.