---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-20T12:12:18.514215'
end_time: '2026-08-20T12:17:59.198528'
duration_seconds: 340.68
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: DENND5A-Related Developmental and Epileptic Encephalopathy
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
  web_search_requests: 20
  num_turns: 31
  total_cost_usd: 2.2672345
  session_id: 6f8bf895-3ab0-55cb-a154-acb932b43f03
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 22
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 7
  on_topic: 7
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** DENND5A-Related Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **DENND5A-Related Developmental and Epileptic Encephalopathy** covering all of the
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

I now have enough primary-literature detail to compile the full report.

I have sufficient primary-literature detail now to compile the comprehensive report.

I now have comprehensive primary-source data. Let me write the full research report.

# DENND5A-Related Developmental and Epileptic Encephalopathy: Comprehensive Research Report

## 1. Disease Information

**Overview.** DENND5A-related developmental and epileptic encephalopathy (also designated **Developmental and Epileptic Encephalopathy 49, DEE49**) is a severe, autosomal recessive neurodevelopmental disorder caused by biallelic loss-of-function (or partial loss-of-function) variants in *DENND5A*. It belongs to the broader clinical/genetic category of "epileptic encephalopathies" — catastrophic infantile-onset epilepsies with refractory seizures and cognitive arrest that are usually attributable to abnormal brain development rather than solely to the seizures themselves. The original description states: *"Epileptic encephalopathies are a catastrophic group of epilepsies characterized by refractory seizures and cognitive arrest, often resulting from abnormal brain development. Here, we have identified an epileptic encephalopathy additionally featuring cerebral calcifications and coarse facial features caused by recessive loss-of-function mutations in DENND5A"* (Suri et al., 2016, PMID: [27866705](https://pubmed.ncbi.nlm.nih.gov/27866705/)).

**Key identifiers:**
- **OMIM disease entry:** #617281 — Developmental and Epileptic Encephalopathy 49 (DEE49)
- **OMIM gene entry:** *617278 — DENN Domain-Containing Protein 5A (DENND5A)
- **HGNC:** HGNC:19344
- **NCBI Gene ID:** 23258
- **Cytogenetic location:** 11p15.4 (chromosome 11)
- **Orphanet:** DENND5A is included on the Orphanet "Molecular diagnosis of Epileptic Encephalopathy" gene panel (EPI02v17.1) and the "Molecular diagnosis of Fetal Akinesia" gene panel; a disease-specific ORPHA number search returned an unreliable/unconfirmed value in secondary sources during this research (candidate ORPHA:1934 could not be independently verified against Orphanet's own disorder pages and should be confirmed directly at orpha.net before use).
- **MONDO:** Not confirmed via direct Mondo lookup during this research; should be cross-referenced against the OMIM #617281 xref.
- **NIH Genetic Testing Registry (GTR):** condition C4310635 ("Developmental and epileptic encephalopathy, 49")
- **Related umbrella:** ILAE Developmental and Epileptic Encephalopathy (DEE) nosology

**Synonyms/alternative names:**
- Developmental and Epileptic Encephalopathy 49 (DEE49)
- Epileptic Encephalopathy, Early Infantile, 49 (EIEE49) — the pre-2020 ILAE nomenclature used in earlier OMIM/literature entries (e.g., Anazi et al. 2017 refers to "EIEE49")
- DENND5A deficiency

**Evidence basis.** The disease is characterized almost entirely from aggregated, disease-level resources built from case series/cohort studies (not large-scale EHR data): the founding 2016 report of 2 families (4 affected individuals) (PMID:27866705), a 2017 exome-sequencing cohort report identifying 2 additional patients (Anazi et al., PMID:27431290), and the definitive natural-history/mechanism cohort study that expanded the total reported cohort to 23–24 individuals from 21–22 families with 30 unique variants (Rodrigues et al., *Nature Communications* 2024, PMID: [39174524](https://pubmed.ncbi.nlm.nih.gov/39174524/); preprint PMID:38352438 on medRxiv).

---

## 2. Etiology

**Disease causal factor:** Purely genetic/Mendelian. DEE49 is caused by **biallelic (homozygous or compound heterozygous) pathogenic variants in *DENND5A*** — there is no known environmental, infectious, or acquired etiology described in the literature.

### Genetic risk factors
- **Inheritance pattern:** Autosomal recessive. Disease requires two pathogenic alleles (homozygous or compound heterozygous).
- **Causal gene:** *DENND5A* (HGNC:19344, chr 11p15.4), encoding a DENN-domain guanine nucleotide exchange factor (GEF).
- **Consanguinity as a risk factor:** The founding families were consanguineous — *"A consanguineous family from Saudi Arabia (family 1) presented with two affected sisters with epileptic encephalopathy"* and *"In family 2, the parents are first cousins"* (PMID:27866705). Anazi et al. 2017 (PMID:27431290) likewise identified the D541G variant in "2 unrelated girls, each born of consanguineous parents." Consanguinity elevates the a priori risk of biallelic rare-variant disease and is consistent with the recessive model.
- **Variant spectrum (from the 2024 cohort, n=24 individuals/22 families):** 30 unique variants — 25 coding-sequence variants, 2 copy-number variants (CNVs), and 3 intronic splice-site variants — distributed across the DENN domain (9 variants), RUN1 domain (2), PLAT domain (6), RUN2 domain (4), and inter-domain linker regions (4). 14 individuals were homozygous and 10 compound heterozygous.
- **Genotype-severity correlation (modifier effect of variant class):** Biallelic frameshift/nonsense (complete loss-of-function) variants are associated with significantly worse neurological outcomes than missense variants (p = 0.0004 in the 2024 cohort) — i.e., variant type itself acts as a severity-modifying factor. Three individuals with specific variant combinations (p.K485E/p.R1159W; an exon 1–14 duplication; p.P955L/p.T136R) had markedly milder or non-DEE presentations (no seizures, normal MRI in some), illustrating that not every biallelic *DENND5A* genotype produces classic DEE49 and that variant-specific functional characterization is needed for interpretation.

### Environmental risk factors
None reported. No toxin, occupational, infectious, or lifestyle exposure has been associated with DEE49 causation; this is consistent with its status as a monogenic recessive disorder.

### Protective factors
None specifically documented. No protective genetic modifier or environmental protective factor has been reported in the literature to date.

### Gene-environment interactions
Not applicable/not reported — no evidence of gene-environment interaction has been described for this monogenic disorder.

---

## 3. Phenotypes

Phenotype frequency data below are drawn from the 2024 *Nature Communications* natural-history cohort (Rodrigues et al., PMID:39174524; n = 24 individuals, 11 female/13 male, mean age 9.0 years, from 22 families), supplemented by the original OMIM clinical synopsis (#617281) and the 2016/2017 case reports.

| Phenotype | Frequency | Notes / HPO term suggestion |
|---|---|---|
| Global developmental delay / intellectual disability | 23/24 (96%) | Near-universal; **HP:0001263** (Global developmental delay), **HP:0001249** (Intellectual disability) |
| Seizures | 21/24 (87.5%) | Mean onset 4.8 months (range includes neonatal onset per OMIM); focal-to-bilateral tonic-clonic most common. **HP:0001250** (Seizure), **HP:0032792** (Neonatal onset seizure), **HP:0002007** (Frontal release signs — not applicable; use **HP:0032917** Bilateral tonic-clonic seizure with focal onset if precise typing needed) |
| Microcephaly | 16/24 (67%) | Primary/congenital in many cases; OFC percentile highly variable. **HP:0000252** (Microcephaly) |
| Ventriculomegaly | 15/24 (63%) | Often with normal head circumference (dissociates from microcephaly). **HP:0002119** (Ventriculomegaly) |
| Hypertonia / spasticity | 14/24 (58%) | **HP:0001276** (Hypertonia), **HP:0001257** (Spasticity) — note OMIM synopsis lists hypotonia as well; tone findings can evolve from early hypotonia to later spasticity |
| Hypotonia | Reported in OMIM synopsis (majority) | **HP:0001252** (Hypotonia) |
| Cerebral hypoplasia / reduced brain volume | 13/24 (54%) | Gray/white matter volume reduction on MRI. **HP:0006872** (Cerebral hypoplasia) |
| Hyperreflexia | 13/24 (54%) | **HP:0001347** (Hyperreflexia) |
| Nonverbal status / absent speech | 15/24 (63%) | **HP:0001344** or **HP:0002465** (Absent speech) |
| Corpus callosum dysgenesis/agenesis/hypoplasia | Multiple cases (documented in both 2016 and 2024 series) | **HP:0002079** (Hypoplasia of the corpus callosum) / **HP:0001274** (Agenesis of corpus callosum) |
| Brain (basal ganglia/periventricular/diencephalic) calcifications | Multiple cases, including the original 2 sisters | **HP:0002514** (Basal ganglia calcification) / **HP:0030955** (Cerebral calcification) |
| Coarse facial features | All 4 original affected individuals, and additional cohort members | **HP:0000280** (Coarse facial features) |
| Specific facial features: open mouth, tented full upper lip, thick everted lower lip, short philtrum, large nostrils | Documented in original family | **HP:0000212** (Tented upper lip vermilion), **HP:0000232** (Everted lower lip vermilion), **HP:0000322** (Short philtrum), **HP:0000463** (Anteverted nares/large nostrils) |
| Frontal bossing | Per OMIM clinical synopsis | **HP:0002007** — actually **HP:0011220** (Frontal bossing) |
| Dandy-Walker malformation / posterior fossa cyst / hypoplastic vermis / diffuse hydrocephalus | Subset of cases | **HP:0001305** (Dandy-Walker malformation), **HP:0002365** (Poor head control) — use **HP:0007360** (Aplasia/Hypoplasia of the cerebellar vermis) |
| Intellectual disability severity | Severe (9), profound (3), moderate (2) of characterized subset | Severity spectrum — **HP:0010864** (Severe ID), **HP:0002187** (Profound ID) |

**Age of onset:** Neonatal-to-infantile. OMIM's clinical synopsis specifically notes "onset of seizures in the neonatal period" for the classic/severe presentation; the broader 2024 cohort reports mean seizure onset at 4.8 months (i.e., early infantile more often than strictly neonatal), reflecting phenotypic heterogeneity linked to variant type.

**Severity and progression:** Presentation ranges from a severe, classic DEE49 phenotype (neonatal/early-infantile refractory seizures, profound global developmental delay, absent speech, microcephaly, spasticity, coarse facies, and brain calcifications) to milder phenotypes without seizures or with normal neuroimaging in individuals carrying specific missense/hypomorphic variant combinations. The disease course is generally **progressive/static-severe** rather than degenerative — the core insult (impaired neurogenesis in utero) is developmental, but epilepsy itself can be refractory and lifelong, and developmental impairment is lifelong.

**Quality of life impact:** Not formally measured with standardized instruments (e.g., no EQ-5D/PROMIS data identified in the literature). Qualitatively, the cohort literature documents severe impact on independent function: the majority are nonverbal (63%), have global developmental delay (96%), and many have severe-to-profound intellectual disability, implying lifelong dependency for activities of daily living, consistent with other severe DEEs.

---

## 4. Genetic/Molecular Information

### Causal gene
**DENND5A** (DENN Domain-Containing Protein 5A; also historically known as RAB6IP1 — Rab6-interacting protein 1), HGNC:19344, NCBI Gene ID 23258, chromosome 11p15.4. OMIM gene entry *617278; disease entry #617281 (DEE49).

### Protein domain structure and function
DENND5A contains:
- A **DENN domain**, "an evolutionarily ancient enzymatic module conferring guanine nucleotide exchange factor (GEF) activity to multiple proteins serving as GEFs for Rabs, which are key regulators of membrane trafficking" (PMID:27866705).
- **RUN1 domain**: binds **Rab6**, which "regulates membrane trafficking and localizes to the trans-Golgi network (TGN)."
- **RUN2 (C-terminal RUN) domain**: interacts with **sorting nexin 1**.
- **PLAT domain**: site of several disease-associated variants in the expanded cohort (6/30 unique variants).
- DENND5A functions as a **GEF for Rab39** (Rab39A and/or Rab39B).
- The protein contains an **autoinhibitory intramolecular interaction** between the DENN domain and the RUN1/PLAT domains, producing a "closed" conformation that masks binding sites for apical polarity-complex proteins; an "open" conformation is required for DENND5A to bind **MUPP1** (Multi-PDZ Protein 1) and **PALS1**, core components of the **Crumbs apical polarity complex** that governs symmetric division of neural progenitor cells (Rodrigues et al. 2024, PMID:39174524). The patient variant **p.Arg710His (R710H)** destabilizes the closed state and increases MUPP1/PALS1 binding — a gain-of-interaction consequence of a disease variant, distinct from simple loss of GEF activity.
- Subcellular localization: DENND5A localizes to the trans-Golgi network/recycling endosome compartment via Rab6, and a distinct pool localizes to **γ-tubulin-positive centrosomes** in neural progenitor cells, implicated in anchoring astral microtubules to the apical cortex to maintain mitotic spindle parallelism.
- DENND5A is "detected predominantly in neuronal tissues with highest levels during development" and is expressed at highest levels in brain, with additional expression in peripheral nervous system and hematopoietic tissue (GeneCards/NCBI).

### Pathogenic variants (specific examples reported in the literature)
| Variant (cDNA/protein) | Zygosity | Source | PMID |
|---|---|---|---|
| c.517_518delGA (p.Asp173Profs*8) | Homozygous, family 1 (2 sisters) | Suri et al. 2016 | 27866705 |
| c.2547delG (p.Lys850Serfs*11) | Homozygous, family 2 | Suri et al. 2016 | 27866705 |
| c.1622A>G (p.Asp541Gly, D541G) | Homozygous, 2 unrelated girls | Anazi et al. 2017 | 27431290 |
| c.949+1G>A (splice) | — | ClinVar RCV001808304, "Developmental and epileptic encephalopathy, 49" | — |
| c.2129G>A (p.Arg710His, R710H) | — | Functional/structural characterization; destabilizes autoinhibited "closed" state | Rodrigues et al. 2024 (39174524); ClinVar RCV000623720 |
| 30 unique variants total (25 coding SNVs/indels, 2 CNVs, 3 intronic splice-site variants) across DENN, RUN1, PLAT, RUN2, and linker regions | 14 homozygous / 10 compound heterozygous | Rodrigues et al. 2024 cohort (n=24) | 39174524 |

- **Variant classification:** Predominantly classified as pathogenic/likely pathogenic per ACMG/AMP criteria in ClinVar and by segregation with disease in consanguineous families; frameshift/nonsense variants are predicted loss-of-function.
- **Functional consequence:** Predominantly **loss of function** (frameshift/nonsense truncations, splice-disrupting variants leading to reduced/absent protein), though at least one missense variant (R710H) produces a distinct **gain-of-interaction** mechanism (increased MUPP1/PALS1 binding via disrupted autoinhibition) rather than simple loss of GEF activity — illustrating allelic/mechanistic heterogeneity within the same gene.
- **Population allele frequency:** Not specifically reported in the literature retrieved; as an ultra-rare recessive disease, pathogenic *DENND5A* alleles are expected to be rare/absent in gnomAD population databases (specific frequencies were not available in the sources reviewed here and should be confirmed directly in gnomAD before curation).
- **Somatic vs. germline:** All reported variants are germline.
- **Modifier genes:** None specifically identified; however, variant *type* (missense vs. frameshift/nonsense) functions as an intragenic severity modifier (p=0.0004 correlation with worse neurological outcome for truncating variants).
- **Epigenetic information / chromosomal abnormalities:** No epigenetic (DNA methylation) mechanism reported. Two of the 30 reported variants in the expanded cohort are **copy-number variants** (including at least one exon 1–14 duplication), representing structural rather than point-mutation lesions.

### Gene family context
*DENND5A* is one of two members of the DENND5 subfamily; its paralog *DENND5B* causes a distinct (largely non-overlapping) neurodevelopmental disorder via de novo variants, with DENND5B-mutant cells showing defective intracellular vesicle trafficking with impaired lipid uptake/distribution (PMID from PMC10940048/AJHG 2024). Both proteins interact with Rab6, Rab11, and Rab39, and are implicated in synaptic vesicle axonal trafficking and neurotransmitter release.

---

## 5. Environmental Information

No environmental factors, lifestyle factors, or infectious agents have been implicated in DEE49 causation or modification in the literature reviewed. This is expected for a fully penetrant autosomal recessive Mendelian disorder.

---

## 6. Mechanism / Pathophysiology

The pathophysiology of DENND5A-related DEE has been substantially clarified by the 2024 *Nature Communications* study (Rodrigues et al., PMID:39174524), which used patient-derived iPSCs, CRISPR knockout iPSC lines, a knock-in mouse model, and a zebrafish CRISPR F0 model to define a coherent causal chain from molecular lesion to clinical phenotype.

### Causal chain (upstream → downstream)

1. **Molecular loss:** Biallelic *DENND5A* variants → complete or near-complete loss of functional DENND5A protein (or, for select missense variants such as R710H, altered/gain-of-interaction function via disrupted domain autoinhibition).
2. **Apical polarity complex disruption:** Loss of DENND5A → impaired/altered interaction with **MUPP1** and **PALS1**, core Crumbs-complex apical polarity proteins → disrupted apical polarity complex in neural progenitor cells.
3. **Centrosome/spindle misorientation:** Loss of the DENND5A centrosomal pool → impaired anchoring of astral microtubules to the apical cortex → misalignment of the mitotic spindle in dividing apical neural progenitors. Quantitatively, wild-type iPSC-derived neural rosette progenitors divide with a mean spindle angle of 57.1° (median 65.4°, symmetric/parallel divisions), whereas DENND5A-knockout progenitors divide with a mean spindle angle of 26.0° (median 20.1°) — "an overwhelming majority of KO cells divided with spindle angles <45°," indicating oblique/asymmetric division.
4. **Loss of symmetric self-renewing division / premature differentiation:** Spindle misorientation biases inheritance of apical polarity determinants unequally between daughter cells, pushing progenitor daughters away from the apical proliferative niche and biasing them toward neuronal differentiation rather than continued self-renewal. Functionally, DENND5A-KO neural progenitor cells proliferate more slowly (614 vs. 1,008 cells per well at 48 hours in wild-type; p<0.0001) and differentiate prematurely into β-III-tubulin-positive neurons at markedly higher rates (47.29% vs. 10.67% in wild-type; p<0.0001) despite maintenance-medium conditions.
5. **Shortened neurogenesis / progenitor pool depletion:** Premature exit from the proliferative/self-renewing progenitor compartment shortens the overall neurogenic period and depletes the progenitor pool prematurely.
6. **Structural brain consequences:** Reduced/altered neurogenesis manifests as **microcephaly**, **ventriculomegaly**, **cortical malformation**, and **corpus callosum dysgenesis** — the core neuroimaging findings of the disorder.
7. **Functional/network consequences:** Ectopically positioned and prematurely generated neurons plus resulting circuit hyperexcitability → **seizures** → secondary/compounding neurodevelopmental impairment (global developmental delay, intellectual disability).

### Independent, complementary mechanism from the founding (2016) study — membrane trafficking / neurotrophin receptor signaling
The original discovery paper proposed a parallel/earlier mechanistic hypothesis centered on **Rab-GEF-dependent membrane trafficking of neurotrophin receptors**:
- DENND5A's RUN1 domain binds **Rab6** (trans-Golgi network trafficking regulator); its RUN2 domain binds **sorting nexin 1**; DENND5A additionally acts as a GEF for **Rab39**.
- *"Knockdown of DENND5A leads to striking alterations in neuronal development, and these changes appear to result from upregulation of neurotrophin receptors, leading to enhanced downstream signaling"* (PMID:27866705).
- In PC12 cells, DENND5A knockdown led to **upregulation of TrkA** and *"significantly enhanced NGF-induced differentiation."* In cultured cortical neurons, DENND5A knockdown led to **upregulation of TrkB**.
- Proposed mechanism: loss of DENND5A impairs Rab-dependent lysosomal targeting/degradation of Trk (neurotrophin) receptors, causing their aberrant stabilization at the cell surface; increased Trk levels drive enhanced ERK/Erk activation, altering neurite outgrowth. In neuroblastoma cell contexts, unliganded TrkA overexpression/activation has separately been linked to apoptosis, leading the authors to hypothesize that *"upregulation of Trk receptors due to DENND5A deficiency could lead to increased apoptosis in the developing brain"* — though the authors explicitly note *"the mechanisms whereby loss of DENND5A leads to enhanced amounts of neurotrophin receptor remain unknown."*

These two mechanistic threads (apical-polarity/mitotic-spindle-driven premature neurogenesis, and Rab-GEF-dependent neurotrophin receptor trafficking/signaling dysregulation) are not mutually exclusive and both stem from DENND5A's core role as a Rab-GEF/membrane-trafficking regulator; the 2024 paper represents the more mechanistically resolved and cohort-validated model.

### Cell types and biological processes implicated
- **Apical (radial glial) neural progenitor cells** — primary affected cell type; Cell Ontology candidate: **CL:0002608** (radial glial cell) or **CL:0000060** (neural progenitor cell)
- **Cortical/pyramidal neurons** — downstream, prematurely generated
- **PC12 cells / cortical neurons in vitro** — model systems for neurotrophin signaling studies

### Suggested GO terms
- GO:0007095 — mitotic cell cycle G2/M transition / more precisely **GO:0000280** (nuclear division) and **GO:0051301** (cell division)
- GO:0033045 — regulation of sister chromatid segregation (spindle-orientation adjacent)
- **GO:0051654** — establishment of mitotic spindle localization / **GO:0000132** (establishment of mitotic spindle orientation)
- GO:0005093 — Rab GDP-dissociation inhibitor binding / **GO:0005085** (guanyl-nucleotide exchange factor activity)
- GO:0032313 — regulation of Rab GTPase activity
- GO:0045175 — basolateral protein secretion (apical-basal polarity adjacent) / **GO:0045197** (establishment or maintenance of epithelial cell apical/basal polarity)
- GO:0030154 — cell differentiation; GO:0022008 — neurogenesis
- GO:0008285 — negative regulation of cell population proliferation

### Suggested CHEBI/protein/complex references
- Crumbs polarity complex components: CRB2, MUPP1/PATJ, PALS1
- Rab GTPases: RAB6A, RAB39A, RAB39B
- Neurotrophin receptors: NTRK1 (TrkA), NTRK2 (TrkB)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary organ:** Central nervous system (brain), specifically cerebral cortex, ventricular system, corpus callosum, basal ganglia, and (in a subset) posterior fossa/cerebellum.
- **Secondary involvement:** Facial skeleton/soft tissue (coarse facial features are a recognized dysmorphic feature, though not a distinct "organ" pathology per se — likely a downstream/coincidental developmental field effect rather than a primary independent lesion).
- **Body systems:** Nervous system (primary); musculoskeletal system secondarily via hypotonia/spasticity and motor impairment.

Suggested UBERON terms:
- UBERON:0000955 — brain
- UBERON:0001851 — cortex (cerebral cortex)
- UBERON:0002037 — cerebellum
- UBERON:0002316 — white matter of corpus callosum / UBERON:0002336 — corpus callosum-adjacent structure
- UBERON:0002020 — gray matter
- UBERON:0002450 — basal ganglion
- UBERON:0035927 — lateral ventricle (ventriculomegaly site)

**Tissue and cell level:**
- Neuroepithelium / apical neural progenitor (radial glia) niche lining the ventricular zone — the primary site of the mitotic spindle-misorientation defect.
- Cortical neurons (downstream, prematurely and ectopically generated).

**Subcellular level:**
- **Centrosome** (γ-tubulin-positive) — DENND5A localization site relevant to spindle orientation. GO Cellular Component: **GO:0005813** (centrosome).
- **Trans-Golgi network** — Rab6-dependent trafficking compartment. GO:0005802 (trans-Golgi network).
- **Recycling endosome** — Rab39-related trafficking. GO:0055037 (recycling endosome).
- **Mitotic spindle** — GO:0072686 (mitotic spindle).
- **Apical plasma membrane / adherens junction** — site of Crumbs-complex polarity signaling. GO:0016327 (apicolateral plasma membrane).

**Localization:** Findings are generally bilateral/diffuse (e.g., bilateral basal ganglia calcifications, generalized microcephaly, bilateral ventriculomegaly) rather than lateralized/asymmetric, consistent with a global developmental defect in neurogenesis rather than a focal lesion.

---

## 8. Temporal Development

**Onset:** Congenital/neonatal-to-early-infantile. The classic severe phenotype has neonatal-onset seizures (per OMIM clinical synopsis); the broader 2024 cohort documents a mean seizure onset of 4.8 months, reflecting a spectrum from neonatal to infantile onset depending on variant severity. The underlying neurodevelopmental insult (impaired progenitor symmetric division) is prenatal, occurring during cortical neurogenesis.

**Onset pattern:** Insidious-to-acute for seizures (which can present abruptly); the structural brain phenotype (microcephaly, ventriculomegaly, corpus callosum dysgenesis) is congenital and often detectable on prenatal or early postnatal imaging.

**Progression:**
- The structural/developmental brain lesion itself is a fixed, non-degenerative, prenatally-established encephalopathy (progenitor pool is not being progressively lost postnatally by a distinct ongoing pathological process, as far as reported).
- The **clinical course** is one of static-to-progressive global developmental impairment plus **refractory, ongoing epilepsy** — the DEE label specifically denotes that ongoing epileptic activity itself may contribute to progressive cognitive/developmental decline, a hallmark of the DEE nosological category generally.
- Disease duration: chronic, lifelong (no reported spontaneous resolution).

**Patterns:**
- No formal remission-pattern data identified.
- No specific "critical period" intervention window has been established in the literature reviewed, although the underlying mechanism (a defect in prenatal apical progenitor symmetric division) implies that the therapeutic window for any mechanism-targeted intervention would need to act prenatally or in early neurogenesis to affect the structural brain phenotype — postnatal interventions would primarily target seizure control and developmental support rather than reversing the structural lesion.

---

## 9. Inheritance and Population

**Epidemiology:** DEE49 is an ultra-rare disorder. No formal population prevalence or incidence estimate was identified in the literature retrieved (consistent with fewer than ~30 published cases worldwide as of the 2024 cohort study). Given ultra-rarity and recessive inheritance concentrated in consanguineous families (Saudi Arabian, and other reported ancestries in the expanded cohort), it likely falls into an Orphanet prevalence class of "<1/1,000,000" or "unknown/not yet documented" pending a systematic prevalence study.

**Inheritance pattern:** Autosomal recessive (AR), confirmed by segregation analysis in multiple consanguineous families and by the pattern of homozygous/compound heterozygous genotypes across the full reported cohort (14 homozygous, 10 compound heterozygous of 24 individuals).

**Penetrance:** Appears to be high/complete for the core homozygous loss-of-function genotype, though phenotypic expressivity is broad (see below) and a subset of biallelic genotypes (particular missense combinations) produce mild-to-absent DEE phenotype, suggesting either incomplete penetrance or (more likely, per the authors) genuinely hypomorphic/less pathogenic alleles rather than true non-penetrance of fully pathogenic alleles.

**Expressivity:** Markedly **variable** — ranging from classic severe neonatal-onset DEE49 with microcephaly, refractory seizures, brain calcifications, and coarse facies, to milder presentations with global developmental delay alone, autism spectrum disorder without seizures, or normal neuroimaging, correlating substantially with variant class (truncating vs. missense) and specific residue/domain affected.

**Genetic anticipation:** Not reported/not applicable (no repeat-expansion mechanism involved).

**Germline mosaicism:** Not specifically reported in the literature reviewed.

**Founder effects:** Not formally established, though the concentration of reported cases in consanguineous Middle Eastern (Saudi Arabian) families in the founding reports raises the possibility of population-specific founder or recurrent alleles; this should be confirmed against gnomAD/regional population databases.

**Consanguinity:** A clearly documented risk factor — both founding families (Suri et al. 2016) and the Anazi et al. 2017 cases arose from consanguineous unions, consistent with autosomal recessive inheritance of a very rare allele.

**Carrier frequency:** Not established in the literature reviewed; expected to be very low/population-specific given the disorder's rarity.

**Population demographics:**
- **Affected populations:** Cases have been reported predominantly from consanguineous families, initially Saudi Arabian; the expanded 2024 cohort (22 families) likely includes broader geographic/ethnic representation, though a systematic geographic breakdown was not retrieved in this research pass.
- **Sex ratio:** The 2024 cohort comprised 11 female and 13 male individuals (~1.2:1 male:female) — roughly balanced, consistent with autosomal (non-X-linked) inheritance.
- **Age distribution:** Cohort mean age 9.0 years at time of study (pediatric-to-young-adult range), consistent with a disorder identified and studied primarily in the pediatric population.

---

## 10. Diagnostics

**Clinical/laboratory tests:** No disease-specific biochemical biomarker has been identified; diagnosis relies on genetic testing plus clinical/neuroimaging correlation.

**Neuroimaging (a key diagnostic pillar):**
- **Brain MRI:** ventriculomegaly, cerebral hypoplasia (reduced brain volume), corpus callosum dysgenesis/agenesis/hypoplasia, and in a subset, Dandy-Walker malformation, posterior fossa cyst, hypoplastic cerebellar vermis, or diffuse hydrocephalus.
- **Head CT:** basal ganglia and periventricular/diencephalic calcifications (as in the original two affected sisters, who had "multiple small foci of calcification in the basal ganglia").
- The authors explicitly recommend: *"Individuals with corpus callosum volume changes and/or microcephaly should be screened for DENND5A variants."*

**Electrophysiology:**
- **EEG:** Would be expected to show epileptiform activity consistent with the clinical seizure semiology (focal-to-bilateral tonic-clonic being most common), though specific EEG pattern data (e.g., burst-suppression, hypsarrhythmia) were not detailed in the sources retrieved here and should be confirmed against the primary cohort paper's supplementary phenotype tables.

**Genetic testing (the primary diagnostic modality):**
- **Whole-exome sequencing (WES)** was the diagnostic method in essentially all reported cases (Suri et al. 2016 used WES in consanguineous families; Anazi et al. 2017 identified their variant via WES of 337 individuals with intellectual disability).
- **Gene panels:** DENND5A is included on Orphanet's "Molecular diagnosis of Epileptic Encephalopathy" gene panel (EPI02v17.1) and commercial early-onset/syndromic epilepsy gene panels (e.g., Genomics England PanelApp "Early onset or syndromic epilepsy" panel and "Hydrocephalus" panel — reflecting the ventriculomegaly/hydrocephalus phenotype overlap).
- **Chromosomal microarray (CMA):** relevant given that 2 of 30 reported variants in the expanded cohort were copy-number variants (deletions/duplications), so CMA/exome CNV calling should be part of a complete diagnostic workup, not single-gene sequencing alone.
- **Single-gene Sanger confirmation:** used in the founding studies to confirm and segregate WES-identified variants within families.
- Whole-genome sequencing (WGS) would be expected to have superior sensitivity for detecting intronic splice-site variants (3 of 30 reported variants were intronic).

**Screening:** No population-based or newborn screening program exists for this ultra-rare recessive disorder. Carrier screening/genetic counseling is relevant primarily in the context of known consanguinity or a family history of an affected individual, given the well-documented consanguinity association.

**Differential diagnosis:** Other genetic developmental and epileptic encephalopathies presenting with microcephaly, ventriculomegaly, and/or corpus callosum abnormalities (the broader DEE gene panel differential), and other syndromes with coarse facial features and brain calcification (e.g., Aicardi-Goutières syndrome and other interferonopathies presenting with basal ganglia calcification, though these have distinct immunological/inflammatory markers not described for DEE49).

---

## 11. Outcome/Prognosis

**Survival/mortality:** No formal survival statistics (5-year/10-year survival, mortality rate) were identified in the literature reviewed; DEE49 is not generally described as directly life-limiting in the sources reviewed, though refractory epilepsy in severe DEEs generally carries elevated mortality risk (e.g., SUDEP risk common to the DEE category broadly) — disease-specific mortality data for DEE49 specifically were not available in this research pass.

**Morbidity/function:**
- Global developmental delay is nearly universal (96% in the 2024 cohort).
- 63% of affected individuals are nonverbal.
- Intellectual disability severity in a characterized subset: severe (9 cases), profound (3 cases), moderate (2 cases) — indicating substantial lifelong functional impairment for most affected individuals.
- No standardized quality-of-life instrument data (EQ-5D, SF-36, PROMIS) were identified for this specific disorder.

**Complications:** Refractory seizures represent the dominant ongoing complication; hypertonia/spasticity (58%) and hyperreflexia (54%) suggest a significant proportion develop upper motor neuron signs contributing to motor disability.

**Prognostic factors:** The single strongest documented prognostic factor is **variant class** — biallelic frameshift/nonsense (complete loss-of-function) genotypes correlate with significantly worse neurological outcome scores than missense genotypes (p=0.0004), making genotype a genuinely predictive prognostic biomarker in this disease, unusual among ultra-rare DEEs for having this level of genotype-phenotype resolution in a cohort of this size.

**Recovery potential:** No disease-modifying therapy exists; the structural neurodevelopmental lesion (established prenatally via impaired progenitor symmetric division) is not expected to be reversible with current management, which remains supportive/symptomatic (see Treatment section).

---

## 12. Treatment

**No disease-specific, mechanism-targeted therapy currently exists for DEE49.** Management is symptomatic/supportive, following general principles for developmental and epileptic encephalopathies:

**Pharmacotherapy (symptomatic seizure control):**
- Standard anti-seizure medications (ASMs) as used broadly across refractory pediatric DEEs (e.g., valproate, levetiracetam, and other agents used per individual seizure semiology); no DEE49-specific ASM efficacy data (e.g., a published responder series to a particular ASM) were identified in this literature pass.
- **NCIT suggestion:** NCIT:C15986 (Pharmacotherapy) as the generic treatment_term for ASM use, with individual agents specified via `therapeutic_agent` (CHEBI) once specific regimens are documented from a primary source.

**Dietary/non-pharmacological therapy:**
- The **ketogenic diet** is a generally effective option for drug-resistant epilepsy broadly (per general epilepsy literature reviewed: ~16% seizure-free, ~56% with >50% seizure reduction in general drug-resistant cohorts), and would be a reasonable consideration for refractory DEE49 seizures by extrapolation from general DEE/drug-resistant epilepsy management principles — but no DEE49-specific ketogenic diet outcome data were identified in the literature reviewed.
- **NCIT suggestion:** NCIT:C15447 (Dietary Intervention).

**Supportive/rehabilitative care:**
- Physical therapy, occupational therapy, and speech/communication therapy are indicated given the high prevalence of hypotonia/spasticity, motor impairment, and nonverbal status, per general standard-of-care principles for severe DEEs (not DEE49-specific published data).
- **NCIT suggestions:** NCIT:C15302 (Physical Therapy), NCIT:C121351 (Occupational Therapy — per general NCIT catalog), NCIT:C159273 (Speech Therapy).

**Genetic counseling:**
- Recommended for families given the autosomal recessive inheritance pattern and documented consanguinity association, to inform recurrence-risk counseling (25% recurrence risk for future pregnancies of carrier parents) and prenatal/preimplantation testing options once a familial pathogenic variant is identified.
- **NCIT suggestion:** NCIT:C15240 (Genetic Counseling).

**Experimental/targeted therapy:** None identified in clinical trials (no NCT-registered interventional trial specific to DENND5A/DEE49 was found in this research pass). Given the mechanistic insight that DENND5A loss disrupts a Crumbs-complex/apical-polarity-dependent mitotic spindle orientation mechanism during a narrow prenatal neurogenic window, there is currently no plausible postnatal molecular correction strategy (e.g., no ASO, gene-replacement, or small-molecule approach has been reported), distinguishing this from other monogenic DEEs where postnatal genetic/RNA-based therapies are more mechanistically tractable (since the core lesion is developmental/structural rather than an ongoing biochemical deficiency).

**Treatment outcomes / algorithms:** No DEE49-specific treatment-response or treatment-algorithm data were identified; management follows general drug-resistant/DEE epilepsy treatment algorithms (sequential ASM trials, consideration of dietary therapy, and supportive multidisciplinary care).

---

## 13. Prevention

No primary, secondary, or tertiary prevention strategy specific to DEE49 exists beyond standard genetic counseling and reproductive options available for any autosomal recessive Mendelian disorder once a causative variant is identified in a family:

- **Genetic counseling** for at-risk (particularly consanguineous) families, informing 25% recurrence risk per pregnancy for carrier couples.
- **Prenatal diagnosis / preimplantation genetic diagnosis (PGD)** would be technically feasible once a familial pathogenic variant is molecularly confirmed, though no specific published program or uptake data for DEE49 were identified.
- **Carrier screening**: not part of any standard population carrier-screening panel given the disorder's extreme rarity; relevant primarily in the context of known family history or specific consanguineous-community carrier programs (not documented specifically for *DENND5A* in the sources reviewed).
- No immunization, public-health, or environmental-intervention prevention strategy applies, consistent with the disorder's purely genetic etiology.

---

## 14. Other Species / Natural Disease

**Mouse:** *Dennd5a* orthologue is annotated in Mouse Genome Informatics (MGI:1201681). A **knock-in mouse model** homozygous for the human-equivalent frameshift variant (c.517_518delGA / p.D173Pfs*8) was generated and characterized in the 2024 study:
- MRI (7 Tesla): significantly enlarged lateral ventricles (WT 4.8 mm³ vs. KI 6.6 mm³; p=0.034) — ventriculomegaly without overt microcephaly, recapitulating a key human phenotype (dissociation of ventriculomegaly from microcephaly seen in a subset of patients).
- Reduced *Dennd5a* mRNA expression in brain tissue (p=0.046), consistent with nonsense-mediated decay of the frameshift transcript.
- **Increased seizure susceptibility**: shorter latency to seizure onset upon 4-aminopyridine (potassium channel blocker) challenge (WT latency 23.60 s vs. KI 11.67 s; p=0.007) — a pharmacoconvulsant-provoked seizure-susceptibility phenotype directly modeling the human epilepsy phenotype.
- Histology of the adult subventricular zone: significantly increased proportion of NeuN-positive (mature) neurons (WT 39.6% vs. KI 58.8%; p=0.001), directly supporting the "premature neuronal differentiation at the expense of progenitor self-renewal" mechanism inferred from human iPSCs.

**Zebrafish:** F0 CRISPR knockout larvae (*dennd5a* orthologue) showed:
- Reduced head size
- Increased hindbrain ventricle size (p=0.028) — a ventriculomegaly analog
- Altered locomotor activity during light/dark cycle assays
- Reduced visual and acoustic startle responses
- Reduced eye size

This cross-species conservation (mouse ventriculomegaly + seizure susceptibility; zebrafish microcephaly-like/ventricular phenotypes) across two independent vertebrate model systems substantially strengthens causality and supports the fundamental, evolutionarily conserved developmental importance of DENND5A in neurogenesis.

**Naturally occurring disease in companion/veterinary species:** No naturally occurring *DENND5A*-associated disease in companion animals or livestock was identified (no OMIA entry found in this search); the described animal models are exclusively laboratory-induced (CRISPR/knock-in), not naturally occurring veterinary disease.

**Comparative biology:** The core mechanism (Crumbs-complex-dependent apical progenitor symmetric division controlling neurogenesis output) is a deeply conserved developmental biology pathway across vertebrates, explaining why both mouse and zebrafish models recapitulate aspects of the human phenotype despite species differences in brain complexity.

---

## 15. Model Organisms

| Model type | System | Genetic modification | Key phenotypes recapitulated | Fidelity/limitations |
|---|---|---|---|---|
| Human iPSC (cellular model) | Patient-derived and CRISPR-KO iPSC-derived neural progenitor cells (neural rosette assay) | DENND5A knockout / patient-derived lines | Mitotic spindle misorientation (57.1°→26.0° mean angle), reduced proliferation, premature β-III-tubulin+ neuronal differentiation | High fidelity for the core cell-autonomous progenitor mechanism; does not model whole-organism seizure phenotype |
| Mouse (in vivo genetic model) | Knock-in mouse, homozygous p.D173Pfs*8 (human-equivalent frameshift) | CRISPR knock-in | Ventriculomegaly (MRI), reduced brain *Dennd5a* mRNA, increased seizure susceptibility (4-AP challenge), increased mature (NeuN+) neuron proportion in SVZ | Recapitulates ventriculomegaly and seizure susceptibility; did not show overt microcephaly in all mice (partial fidelity to the human microcephaly phenotype — a HUMAN_MODEL_MISMATCH-type caveat) |
| Zebrafish (in vivo genetic model) | F0 CRISPR knockout larvae | CRISPR/Cas9 F0 knockout | Reduced head size, increased hindbrain ventricle size, altered locomotor activity, reduced visual/acoustic startle, reduced eye size | Useful for rapid high-throughput phenotype screening; F0 mosaic knockout (not stable germline line) is a limitation on genotype-phenotype precision |
| Rat pheochromocytoma cell line (PC12) | In vitro neurotrophin-signaling model | DENND5A knockdown (siRNA/shRNA) | Upregulated TrkA, enhanced NGF-induced differentiation | Cancer cell line model of neurotrophin receptor trafficking, not neurogenesis per se; complements but is mechanistically distinct from the 2024 progenitor-division model |
| Primary cultured cortical neurons | In vitro | DENND5A knockdown | Upregulated TrkB | Post-mitotic neuron model; informative for the neurotrophin-signaling arm of the mechanism, not the progenitor-division arm |

**Resources:** MGI:1201681 (mouse *Dennd5a* gene page); no dedicated public repository line accession numbers (e.g., IMSR/EMMA/MMRRC ID) were identified in this research pass for the specific knock-in line — this should be confirmed directly from the *Nature Communications* 2024 paper's Methods/Data Availability section if a specific strain repository accession is needed for curation.

---

## Summary of Key Ontology Term Suggestions for KB Curation

- **Disease:** OMIM:617281; HGNC gene: `hgnc:19344` (DENND5A)
- **Inheritance:** HP:0000007 (Autosomal recessive inheritance)
- **Key phenotypes:** HP:0001250 (Seizure), HP:0000252 (Microcephaly), HP:0002119 (Ventriculomegaly), HP:0002079 (Hypoplasia of the corpus callosum), HP:0030955 (Cerebral calcification), HP:0000280 (Coarse facial features), HP:0001263 (Global developmental delay), HP:0001276 (Hypertonia), HP:0001252 (Hypotonia), HP:0001347 (Hyperreflexia), HP:0006872 (Cerebral hypoplasia)
- **Cell types:** CL:0002608 (radial glial cell) / neural progenitor cell equivalent
- **Biological processes (GO):** GO:0000132-type spindle-orientation terms, GO:0022008 (neurogenesis), GO:0005085 (guanyl-nucleotide exchange factor activity), GO:0045197 (epithelial apical/basal polarity establishment/maintenance)
- **Anatomy (UBERON):** UBERON:0000955 (brain), UBERON:0001851 (cerebral cortex), UBERON:0002450 (basal ganglion), UBERON:0035927 (lateral ventricle)
- **Treatments (NCIT):** NCIT:C15986 (Pharmacotherapy, for ASMs), NCIT:C15447 (Dietary Intervention, ketogenic diet), NCIT:C15240 (Genetic Counseling), NCIT:C15302 (Physical Therapy)

---

## Sources

- [Epileptic Encephalopathy Caused by Mutations in the Guanine Nucleotide Exchange Factor DENND5A - PubMed (PMID:27866705)](https://pubmed.ncbi.nlm.nih.gov/27866705/)
- [Epileptic Encephalopathy Caused by Mutations in the Guanine Nucleotide Exchange Factor DENND5A - PMC (full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5142110/)
- [Epileptic Encephalopathy Caused by Mutations in the Guanine Nucleotide Exchange Factor DENND5A - AJHG (Cell Press)](https://www.cell.com/ajhg/fulltext/S0002-9297(16)30442-6)
- [Entry - *617278 - DENN DOMAIN-CONTAINING PROTEIN 5A; DENND5A - OMIM](https://omim.org/entry/617278)
- [Entry - #617281 - DEVELOPMENTAL AND EPILEPTIC ENCEPHALOPATHY 49; DEE49 - OMIM](https://omim.org/entry/617281)
- [Clinical Synopsis - #617281 - DEE49 - OMIM](https://omim.org/clinicalSynopsis/617281)
- [Developmental and epileptic encephalopathy, 49 - NIH Genetic Testing Registry (GTR)](https://www.ncbi.nlm.nih.gov/gtr/conditions/C4310635/)
- [Loss of symmetric cell division of apical neural progenitors drives DENND5A-related developmental and epileptic encephalopathy - PMC (PMID:39174524)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10863025/)
- [Loss of symmetric cell division of apical neural progenitors drives DENND5A-related developmental and epileptic encephalopathy - Nature Communications](https://www.nature.com/articles/s41467-024-51310-z)
- [DENND5A epileptic encephalopathy features global developmental delay, seizures and ventriculomegaly - medRxiv (preprint)](https://www.medrxiv.org/content/10.1101/2022.08.23.22278845v1)
- [Loss of symmetric cell division of apical neural progenitors drives DENND5A-related developmental and epileptic encephalopathy - medRxiv v3](https://www.medrxiv.org/content/10.1101/2022.08.23.22278845v3.full)
- [DENND5A Gene - GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=DENND5A)
- [DENND5A (Early onset or syndromic epilepsy) - Gene - Genomics England PanelApp](https://panelapp.genomicsengland.co.uk/panels/402/gene/DENND5A/)
- [Gene: DENND5A (Hydrocephalus) - Genomics England PanelApp](https://panelapp.genomicsengland.co.uk/panels/179/gene/DENND5A/)
- [NM_015213.4(DENND5A):c.949+1G>A AND Developmental and epileptic encephalopathy, 49 - ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV001808304/)
- [NM_015213.4(DENND5A):c.2129G>A (p.Arg710His) AND Inborn genetic diseases - ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV000623720/)
- [Dennd5a MGI Mouse Gene Detail - MGI:1201681](https://informatics.jax.org/marker/MGI:1201681)
- [Gene discovered to cause rare, severe neurological disease - McGill University Newsroom](https://www.mcgill.ca/newsroom/channels/news/gene-discovered-cause-rare-severe-neurological-disease-264507)
- [De novo variants in DENND5B cause a neurodevelopmental disorder - AJHG](https://www.cell.com/ajhg/pdf/S0002-9297(24)00033-8.pdf)
- [De novo variants in DENND5B cause a neurodevelopmental disorder - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10940048/)
- [Orphanet: Molecular diagnosis of Epileptic Encephalopathy gene panel EPI02v17.1](https://www.orpha.net/consor/cgi-bin/ClinicalLabs_Search.php?lng=EN&data_id=104665)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 7 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.