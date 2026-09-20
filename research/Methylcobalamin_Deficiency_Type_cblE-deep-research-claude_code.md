---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T05:50:04.246476'
end_time: '2026-08-27T05:54:22.272429'
duration_seconds: 258.03
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Methylcobalamin Deficiency Type cblE
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
  web_search_requests: 11
  num_turns: 22
  total_cost_usd: 1.1619438000000002
  session_id: 98b3127c-432a-57dc-acc9-774218ba8a79
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 25
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 6
  quotes_valid: 6
  relevance_assessed: 14
  on_topic: 13
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Methylcobalamin Deficiency Type cblE
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Methylcobalamin Deficiency Type cblE** covering all of the
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

That GeneReviews fetch worked well. Let me get a few more targeted pieces: the key JIMD 24-patient cohort paper details, HPO/MONDO/ontology identifiers, and ClinVar variant specifics.

I have gathered sufficient primary-source material. Let me pull a couple more items — GeneCards for molecular/gene detail and the ClinVar variant page for a specific validated variant — to round out the report.

I now have enough to compile a comprehensive, well-cited report.

# Methylcobalamin Deficiency Type cblE (Methionine Synthase Reductase Deficiency) — Research Report

## 1. Disease Information

### Overview
Methylcobalamin deficiency type cblE (also called homocystinuria-megaloblastic anemia, cblE type; HMAE) is a rare autosomal recessive inborn error of intracellular cobalamin (vitamin B12) metabolism. It results from biallelic pathogenic variants in **MTRR**, which encodes methionine synthase reductase — an enzyme required to periodically reactivate methionine synthase (MTR/MS) by reductive methylation. Loss of MTRR function causes functional deficiency of methionine synthase despite the enzyme itself being structurally normal, producing impaired remethylation of homocysteine to methionine. The clinical result is combined **homocystinuria** and **megaloblastic anemia**, typically with **hypomethioninemia**, in the absence of methylmalonic aciduria (distinguishing it from the "combined" cobalamin defects such as cblC/cblD/cblF) (GeneReviews, NBK1328; OMIM #236270).

### Key Identifiers
- **OMIM phenotype**: #236270 — Homocystinuria-Megaloblastic Anemia, cblE Type (HMAE)
- **OMIM gene**: *602568 — METHIONINE SYNTHASE REDUCTASE; MTRR
- **MONDO**: MONDO:0009354
- **Orphanet**: ORPHA:2169 (methionine synthase reductase deficiency); grouped clinically with cblG and cblD-variant 1 under ORPHA:622 "Homocystinuria without methylmalonic aciduria"
- **MedGen**: C1856057
- **HGNC**: 7473 (MTRR)
- **UniProt**: Q9UBK8 (MTRR protein, 698 amino acids, ~77.7 kDa)
- **Gene location**: chromosome 5p15.31 (5p15.3–15.2 in older literature); gene spans ~34 kb, 15 exons
- **Inheritance**: Autosomal recessive
(Sources: [OMIM #236270](https://omim.org/entry/236270), [OMIM *602568](https://omim.org/entry/602568), [NORD/MONDO](https://rarediseases.org/mondo-disease/methylcobalamin-deficiency-type-cble/), UniProt Q9UBK8, GeneReviews NBK1328)

### Synonyms
- Methionine synthase reductase deficiency
- cblE-type homocystinuria / cblE disease
- Homocystinuria-megaloblastic anemia, cblE type (HMAE)
- Vitamin B12-responsive megaloblastic anemia due to methionine synthase reductase deficiency

### Data Source Character
Nearly all available information is derived from **case reports and small case series** (individual patients and sibships), not large aggregated cohorts or EHR-based studies — reflecting the extreme rarity of the disease. The largest published cohort ("24 patients with the cblE or cblG remethylation defect") is a multi-center retrospective compilation (Huemer et al., *J Inherit Metab Dis* 2015; PMID not directly retrieved here, DOI 10.1007/s10545-014-9803-7), still a case-series design rather than population-level data.

---

## 2. Etiology

### Disease Causal Factors
cblE is a **purely genetic (Mendelian) disorder**. Biallelic loss-of-function or hypomorphic variants in *MTRR* impair the reductive-methylation reactivation of methionine synthase (MTR), which uses methylcobalamin (MeCbl) as a cofactor to transfer a methyl group from 5-methyltetrahydrofolate to homocysteine, forming methionine. MTR undergoes occasional oxidative inactivation (cob(II)alamin state) during turnover; MTRR restores it to the active cob(I)alamin state using electrons from NADPH shuttled through FAD and FMN cofactors, with S-adenosylmethionine (SAM) as the methyl donor for reactivation. Without functional MTRR, MTR activity progressively declines, causing accumulation of homocysteine and depletion of methionine/SAM (WebSearch synthesis of MTRR mechanism; ScienceDirect topic pages; GeneReviews NBK1328).

### Genetic Risk Factors
- **Causal variants**: Biallelic pathogenic *MTRR* variants (missense, nonsense, splice-site, small indels, and a truncating frameshift). GeneReviews reports that sequence analysis detects the majority (21 of 22 reported variant types in one series) of pathogenic alleles (GeneReviews NBK1328).
- **Notable variants**:
  - **c.1361C>T (p.Ser454Leu)**, sometimes reported as p.Ser545Leu in different transcript numbering — an "Iberian-origin" founder-type variant associated with a **milder phenotype with no evident neurologic involvement** in homozygotes (ClinVar RCV000007449; GeneReviews NBK1328; ResearchGate case report "CblE type of homocystinuria: Mild clinical phenotype... novel mutation").
  - **G487R** (glycine-to-arginine at codon 487) — reported in homocystinuria-megaloblastic anemia patients.
  - A **heterozygous truncating mutation** in two siblings (OMIM 602568.0001) was among the first pathogenic *MTRR* alleles identified.
  - Additional ClinVar-curated variants include c.2073C>T (p.Arg691=, synonymous, uncertain significance in some records), c.1952+17C>A (intronic), and c.-119T>C (5′ UTR) (ClinVar RCV000907261, RCV003618859, RCV001530449).
- No common susceptibility loci or modifier genes have been robustly established for cblE specifically, though the common *MTRR* polymorphism **A66G (p.Ile22Met)** has been studied extensively in the general population as a modifier of folate/homocysteine status and disease risk (neural tube defects, cardiovascular disease) — this is distinct from the rare biallelic pathogenic variants causing cblE disease itself.

### Environmental Risk Factors
- **Maternal/dietary vitamin B12 or folate status**: While cblE is a primary genetic enzyme defect (not a nutritional deficiency), functional cobalamin/folate status can modulate phenotypic severity, since MTRR partially rescues residual methionine synthase activity when cobalamin is abundant — this underlies the rationale for high-dose parenteral hydroxocobalamin therapy.
- No infectious, occupational, or toxic environmental triggers have been described as causal for cblE; it is a monogenic disease that is fully penetrant when biallelic pathogenic variants are present, though **age of onset and severity vary** (GeneReviews NBK1328).

### Protective Factors
- No specific protective genetic variants against cblE disease itself have been reported (as opposed to studies of the common *MTRR* A66G polymorphism in other multifactorial contexts).
- **Vitamin B12 (hydroxocobalamin) responsiveness** functions as a therapeutic/mitigating factor rather than a true "protective factor," since residual enzyme activity in hypomorphic alleles can be augmented pharmacologically.

### Gene-Environment Interactions
- The core gene-environment interaction in cblE pathophysiology is the **substrate-driven rescue mechanism**: supraphysiologic (pharmacologic) doses of hydroxocobalamin increase intracellular cobalamin pools sufficiently to partially bypass the reductive-reactivation defect in some hypomorphic MTRR variants, explaining "cobalamin responsiveness" as a treatment principle (GeneReviews NBK1328; multiple case reports).
- Maternal folate/B12 status during pregnancy is relevant to the broader *MTRR* biology (e.g., mouse models — see Section 15) but is not established as a modifier of cblE disease severity in affected humans specifically.

---

## 3. Phenotypes

cblE produces a relatively **narrow, well-defined phenotypic triad**: megaloblastic anemia, neurologic/developmental impairment, and biochemical homocystinuria with hypomethioninemia — but with documented phenotypic heterogeneity in severity and organ involvement.

### Hematologic
- **Megaloblastic anemia** (macrocytic anemia with megaloblastic bone marrow changes) — the most consistent and often presenting feature. Reported as isolated in some patients.
  - HP suggestion: HP:0001889 (Megaloblastic anemia)
- **Pancytopenia / early-onset bone marrow failure** has been reported, sometimes remaining isolated without neurologic involvement (WebSearch synthesis, PMC article on late-onset hemolytic anemia complication).
  - HP suggestion: HP:0001876 (Pancytopenia)
- **Late-onset refractory hemolytic anemia** as a rare treatment-related/disease complication in siblings on long-term therapy, potentially preventable by hydroxocobalamin dose escalation (PMC11078714, "Late-onset refractory hemolytic anemia in siblings treated for methionine synthase reductase deficiency").
  - HP suggestion: HP:0001878 (Hemolytic anemia)

### Neurologic / Developmental
- **Developmental delay / delayed psychomotor development**, frequently reported (HP:0002194)
- **Intellectual disability / cognitive dysfunction** (HP:0001249)
- **Hypotonia** (HP:0001252)
- **Seizures**, described as "frequent" in some series (HP:0001250)
- **Cerebral atrophy** on neuroimaging (HP:0002059)
- **Lethargy** (HP:0001254)

### Ophthalmologic
- **Nystagmus** (HP:0000639)
- **Impaired visual acuity** without lens dislocation — notably **distinguishing cblE from classic CBS-deficiency homocystinuria**, which characteristically causes ectopia lentis (HP:0000572, visual impairment)
- **Macular dysfunction**, described as a rare feature (relevant HP term e.g. HP:0007754 macular dystrophy, if applicable per specific case)

### Growth / Constitutional
- **Failure to thrive / feeding difficulties**, often an early presenting sign (HP:0001508 / HP:0011968)
- **Severe growth failure** — GeneReviews specifically states "most children with cblE present in the first two years of life with severe growth failure, megaloblastic anemia, and neurologic manifestations" (GeneReviews NBK1328)

### Renal
- **Hemolytic uremic syndrome (HUS)** — described as occurring in a subset of patients ("isolated megaloblastic anemia and HUS may also be seen")
  - HP suggestion: HP:0005575 (Hemolytic-uremic syndrome)
- **Atypical glomerulopathy** — described in an adolescent-onset presentation (GeneReviews NBK1328)

### Laboratory Abnormalities (biochemical phenotypes, distinct from clinical signs)
- **Elevated total plasma homocysteine (hyperhomocysteinemia)** and **homocystinuria** (elevated urinary homocystine)
- **Low-to-normal plasma methionine (hypomethioninemia)** and low S-adenosylmethionine (SAM)
- **Normal urine/plasma methylmalonic acid (MMA)** — key distinguishing feature from combined (cblC/D/F) and isolated methylmalonic-acidemia cobalamin defects
- **No elevated propionylcarnitine (C3)** on newborn screening acylcarnitine profile, which is why **cblE and cblG are typically missed by standard newborn screening** (GeneReviews NBK1328)

### Phenotype Characteristics
- **Age of onset**: Most commonly between **2 weeks and 3 years of age**; GeneReviews specifies presentation "in the first two years of life" for the classic severe form; rarer **adolescent-onset presentation with atypical glomerulopathy** has also been described (GeneReviews NBK1328; multiple case-report sources).
- **Severity**: Highly variable — from mild phenotype with isolated megaloblastic anemia and no neurologic involvement (e.g., homozygous c.1361C>T/p.Ser454Leu patients) to severe early-onset multisystem disease with profound developmental delay, seizures, and growth failure.
- **Progression**: Generally chronic and, if untreated, progressive; treatment with parenteral hydroxocobalamin and betaine can stabilize biochemical parameters, but neurodevelopmental and ophthalmologic outcomes are only partially responsive.
- **Frequency among affected individuals**: Formal frequency percentages for individual phenotypes are not well established given the very small published patient numbers (fewer than 40 cumulative cblE + cblG cases reported per GeneReviews).

### Quality of Life Impact
No disease-specific quality-of-life instrument data were identified in the literature searched. Neurodevelopmental impairment (intellectual disability, seizures) and visual impairment are the primary drivers of long-term functional impact; the JIMD cohort study (Huemer et al. 2015) explicitly notes that "the overall impact of treatment on neurodevelopmental disabilities and eye disease was at most moderate," implying persistent long-term QoL burden even with treatment (WebSearch synthesis of JIMD 2015 paper).

---

## 4. Genetic / Molecular Information

### Causal Gene
- **MTRR** (5-methyltetrahydrofolate-homocysteine methyltransferase reductase), HGNC:7473, chromosome 5p15.31, ~34 kb genomic span, 15 exons.
- **OMIM gene entry**: *602568.

### Protein / Function
- MTRR is a **diflavin oxidoreductase** of the **ferredoxin-NADP+ reductase family**, structurally related to cytochrome P450 reductase and nitric oxide synthase reductase domains.
- Domain architecture: **N-terminal FMN-binding domain** (flavodoxin-like) + **C-terminal FAD/NADPH-binding domain** (ferredoxin-NADP+ reductase-like).
- Mechanism: Acquires electrons from **NADPH**, passes them sequentially through **FAD → FMN**, then to **cob(II)alamin** bound to methionine synthase (MTR), reducing it to **cob(I)alamin**, which is then remethylated by **S-adenosylmethionine (SAM)** to regenerate active methylcobalamin-bound MTR.
- MTRR forms part of a **multiprotein complex** with MMACHC, MMADHC (the cblC/cblD gene products) and MTR itself, integrating it into the broader intracellular cobalamin-processing pathway.
- (Sources: WebSearch synthesis of GeneCards/UniProt/PNAS cloning paper; ScienceDirect topic overview)

### Pathogenic Variants
- **Gene**: MTRR (HGNC:7473)
- **Variant classification**: Reported alleles span **pathogenic and likely pathogenic** per ACMG/AMP in ClinVar; variant of uncertain significance for some synonymous/intronic changes (e.g., c.2073C>T p.Arg691=).
- **Variant types**: Missense (majority; e.g., p.Ser454Leu/p.Ser545Leu, G487R), nonsense/truncating (e.g., the original heterozygous truncating mutation OMIM 602568.0001), splice-region (c.1952+17C>A), and regulatory/5′UTR (c.-119T>C).
- **Allele frequency**: No large population allele-frequency data specific to disease-causing MTRR variants were retrieved; the disorder is exceedingly rare (fewer than 40 cumulative cblE+cblG cases reported), consistent with very low allele frequencies in gnomAD for the pathogenic alleles (not independently queried in this session).
- **Origin**: Germline, autosomal recessive (biallelic).
- **Functional consequences**: Loss-of-function or hypomorphic reduction of MTRR reductase activity → impaired reactivation of methionine synthase → functional methionine synthase deficiency despite normal MTR protein.
- **Genotype-phenotype correlation**: The c.1361C>T (p.Ser454Leu) variant, described as of **Iberian origin**, is specifically associated with a **milder phenotype without neurologic involvement** in homozygotes — one of the few reasonably well-documented genotype-phenotype correlations in this disease (GeneReviews NBK1328; case report literature).

### Modifier Genes
No confirmed modifier genes for cblE disease severity were identified in the literature retrieved. The common *MTRR* A66G (p.Ile22Met) polymorphism is studied as a population-level modifier of homocysteine/folate metabolism in unrelated contexts (e.g., neural tube defect risk, Down syndrome risk in some association studies) but is not established as a modifier of cblE disease phenotype in affected individuals.

### Epigenetic Information
No disease-specific epigenetic (DNA methylation, histone modification) studies in human cblE patients were identified. However, mouse *Mtrr* hypomorphic models show that MTRR/folate-methionine pathway disruption causes **DNA methylation dysregulation** transgenerationally (see Section 15), suggesting a plausible but human-unconfirmed epigenetic dimension to pathophysiology, since SAM (whose production is impaired in cblE) is the universal methyl donor for DNA/histone methylation.

### Chromosomal Abnormalities
No chromosomal-scale abnormalities (aneuploidy, translocations) are described as causal for cblE; it is a single-gene, point-mutation/small-indel disorder.

---

## 5. Environmental Information

- **Environmental factors**: None established as independently causal; cblE is monogenic. However, functional cobalamin sufficiency (dietary/parenteral) modulates phenotype expression pharmacologically.
- **Lifestyle factors**: Not applicable as causal factors; dietary protein restriction is specifically **not recommended** as part of management (see Section 12), distinguishing cblE from disorders like classic homocystinuria or organic acidemias where dietary protein restriction is standard.
- **Infectious agents**: None implicated.

---

## 6. Mechanism / Pathophysiology

### Causal Chain
1. **Molecular trigger**: Biallelic pathogenic *MTRR* variants → reduced/absent methionine synthase reductase activity.
2. **Enzymatic consequence**: Methionine synthase (MTR/MS), which cycles between active cob(I)alamin-bound and inactive cob(II)alamin-bound states during normal catalysis (~1 in 2,000 turnovers undergoes oxidative inactivation), cannot be efficiently reactivated by reductive methylation. MTR activity progressively declines despite the MTR protein itself and its bound cobalamin cofactor being intact.
3. **Biochemical consequence**: Impaired remethylation of homocysteine → methionine via the 5-methyltetrahydrofolate-homocysteine methyltransferase reaction. This causes:
   - **Homocysteine accumulation** (hyperhomocysteinemia/homocystinuria)
   - **Methionine and SAM depletion** (hypomethioninemia)
   - **Folate trapping**: as 5-methyltetrahydrofolate cannot be demethylated (the "methylfolate trap"), cellular folate becomes sequestered in a form unusable for purine/thymidylate synthesis.
4. **Cellular consequence**: Impaired thymidylate synthesis (via depleted folate cofactors needed for the thymidylate synthase cycle) → impaired DNA synthesis in rapidly dividing cells, especially hematopoietic precursors → **megaloblastic changes and ineffective erythropoiesis** (megaloblastic anemia).
5. **Systemic/organismal consequence**: SAM depletion impairs global transmethylation reactions (including neuronal myelin and neurotransmitter methylation pathways), contributing to **neurodevelopmental impairment, hypotonia, and seizures**. Elevated homocysteine itself is thought to contribute to vascular/endothelial and possibly neurologic toxicity, analogous to (but generally milder than) classic CBS-deficiency homocystinuria vasculopathy — although lens dislocation, a hallmark of CBS deficiency, is characteristically **absent** in cblE, suggesting distinct mechanisms of connective-tissue involvement (or its absence) between the disorders.

### Upstream vs. Downstream
- **Upstream**: MTRR loss-of-function (molecular/enzymatic).
- **Midstream**: Functional methionine synthase deficiency; homocysteine/SAM/folate cycle disruption (cellular/metabolic).
- **Downstream**: Megaloblastic hematopoiesis (cellular/tissue), CNS dysmyelination/developmental impairment (tissue/organism), possible renal microangiopathy/HUS (organism).

### Cell Types and Biological Processes Involved
- **Hematopoietic precursor cells** (erythroid lineage) — impaired DNA synthesis, megaloblastic change.
  - CL suggestion: CL:0000765 (erythroblast) or CL:0000038 (erythroid progenitor cell)
- **Neurons / glial cells** — impaired methylation-dependent myelination and neurotransmitter metabolism.
  - CL suggestion: CL:0000540 (neuron)
- **Renal glomerular/endothelial cells** — implicated in the rare HUS/atypical glomerulopathy phenotype, potentially via homocysteine-mediated endothelial injury (analogous to mechanisms proposed in cblC-associated HUS).
  - CL suggestion: CL:0002138 (endothelial cell of vascular tree) or CL:1001005 (glomerular visceral epithelial cell)

### Molecular Pathways / GO Terms
- **One-carbon metabolism / folate cycle** (KEGG: hsa00670 One carbon pool by folate; hsa00270 Cysteine and methionine metabolism)
- GO Biological Process suggestions:
  - GO:0033353 (S-adenosylmethionine cycle)
  - GO:0009086 (methionine biosynthetic process)
  - GO:0050667 (homocysteine metabolic process)
  - GO:0032259 (methylation)
- GO Molecular Function suggestions:
  - GO:0030350 (iron-responsive element binding — not relevant; correct term:) 
  - GO:0050660 (flavin adenine dinucleotide binding)
  - GO:0010181 (FMN binding)
  - GO:0004489 (methylenetetrahydrofolate reductase [NAD(P)H] activity — for MTHFR, not MTRR; for MTRR specifically:) 
  - GO:0016860 (intramolecular oxidoreductase activity) — verify against current GO for "methionine synthase reductase activity" annotation, e.g., GO:0030744 (methionine synthase reductase activity, if extant) — **flag for verification with OAK/GO adapter before binding in KB entry.**
- GO Cellular Component: GO:0005829 (cytosol) — MTRR is a cytosolic enzyme.

### Biochemical Abnormalities
- Enzyme deficiency: **methionine synthase reductase (EC 1.16.1.8)** activity loss.
- Functional/secondary enzyme deficiency: **methionine synthase (EC 2.1.1.13)** activity decreased under standard fibroblast assay conditions with suboptimal reducing agent — this is the key **enzymatic distinguishing test between cblE and cblG**: in cblE, MTR activity is preserved with excess exogenous reducing agent but falls under limiting conditions; in cblG, MTR activity is decreased under all conditions because the *MTR* apoenzyme itself is defective (WebSearch synthesis of Watkins 1989, AJMG; ScienceDirect topic page).

### Immune System Involvement
No primary immune dysfunction is characteristic of cblE; it is not classified as a primary immunodeficiency.

### Tissue Damage Mechanisms
Ineffective erythropoiesis (megaloblastic anemia) and possible endothelial/microvascular injury contributing to the rare HUS/glomerulopathy phenotype are the principal described tissue-damage mechanisms; direct evidence for oxidative-stress or fibrotic mechanisms specific to cblE was not identified in the literature retrieved.

### Molecular Profiling / Advanced Technologies
No transcriptomic, proteomic, metabolomic, single-cell, or spatial-omics studies specific to human cblE patient tissue were identified in this search. Metabolomic characterization is largely limited to targeted amino acid/homocysteine/methylmalonic acid panels used diagnostically (see Section 10), not unbiased -omics profiling.

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary**: Bone marrow (hematopoietic system) — megaloblastic anemia/pancytopenia; Central nervous system — developmental delay, seizures, hypotonia, cerebral atrophy.
- **Secondary**: Eye (nystagmus, visual impairment, rare macular dysfunction); Kidney (rare HUS, atypical glomerulopathy).
- **Body systems involved**: Hematologic, nervous, ophthalmologic, and (rarely) renal systems.

UBERON suggestions: UBERON:0002371 (bone marrow), UBERON:0000955 (brain), UBERON:0000970 (eye), UBERON:0002113 (kidney).

### Tissue and Cell Level
- Erythroid precursor cells in bone marrow (megaloblastic changes)
- Neural tissue — white matter/myelin-relevant cell populations
- Renal glomerular capillary endothelium (in HUS/glomerulopathy presentations)

### Subcellular Level
- **Cytosol**: MTRR and MTR are cytosolic enzymes; the folate/methionine cycle operates in the cytosolic compartment.
- GO Cellular Component: GO:0005829 (cytosol)

### Localization
No specific lateralization pattern is described; CNS and hematologic involvement are systemic/bilateral by nature.

---

## 8. Temporal Development

### Onset
- **Typical age**: 2 weeks to 3 years of age (most common); classic presentation "in the first two years of life."
- **Rare atypical**: Adolescent-onset presentation with atypical glomerulopathy has been described.
- **Onset pattern**: Generally insidious/subacute, evolving over weeks to months in infancy, though acute presentations (e.g., with HUS) can occur.

### Progression
- **Disease course pattern**: Chronic, generally progressive if untreated; biochemically responsive (to varying degrees) to hydroxocobalamin/betaine therapy.
- **Progression rate**: Variable — mild genotypes (e.g., p.Ser454Leu homozygotes) show slow/non-progressive isolated hematologic disease; severe genotypes show more rapid multisystem progression in infancy.
- **Disease duration**: Chronic, lifelong (enzyme deficiency is permanent; management is lifelong).

### Patterns
- **Remission**: Biochemical parameters (homocysteine, methionine) can normalize or substantially improve with treatment; hematologic remission of megaloblastic anemia is generally achievable. Neurodevelopmental and ophthalmologic manifestations show only partial/moderate treatment response per the largest published cohort (JIMD 2015 paper).
- **Critical periods**: Early infancy is considered a critical window for treatment initiation to minimize neurodevelopmental sequelae, though the evidence for this is characterized in the literature as "weak" ("only weak evidence for a response to treatment and for the specific value of early treatment in cblE defects" — WebSearch synthesis of JIMD 2015 cohort paper).

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence/Incidence**: No formal population-based incidence or prevalence rate has been established. The disease is characterized as **ultra-rare**, with GeneReviews stating "fewer than 40 cases have been described for cblE and cblG" combined, as of the most recent update reviewed. No newborn-screening-based incidence estimate exists because cblE (like cblG) is **not reliably detected by standard newborn screening** acylcarnitine profiles (no elevated propionylcarnitine/C3) (GeneReviews NBK1328).

### Inheritance Pattern
- **Autosomal recessive.** Per GeneReviews genetic counseling section: "At conception, each sib of an affected individual has a 25% chance of being affected, a 50% chance of being an asymptomatic carrier, and a 25% chance of being unaffected and not a carrier." Parents of an affected child are obligate heterozygous carriers (GeneReviews NBK1328).
- **Penetrance**: Presumed complete for biallelic clearly pathogenic (loss-of-function) variants, though phenotypic severity is variable (variable expressivity), and hypomorphic alleles (e.g., p.Ser454Leu) produce milder, incompletely penetrant neurologic phenotypes.
- **Carrier detection**: GeneReviews notes biochemical testing is **not reliable** for carrier detection; molecular (sequence-based) testing with a known familial variant is required.
- **Founder effects**: The c.1361C>T (p.Ser454Leu) variant is specifically noted as being of **Iberian origin**, suggestive of a founder allele in that population.
- **Consanguinity**: Not specifically quantified in the sources retrieved, but as an ultra-rare autosomal recessive disorder, consanguinity would be expected to increase local incidence in affected families/populations, as is typical for such disorders.
- **Carrier frequency**: Not established in population databases for this session's search.

### Population Demographics
- No specific ethnic/geographic prevalence data beyond the Iberian-origin founder variant were identified.
- **Sex ratio**: No sex predilection is described; autosomal recessive inheritance predicts equal male:female distribution.
- **Age distribution**: Predominantly diagnosed in infancy/early childhood, consistent with typical age of onset.

---

## 10. Diagnostics

### Clinical/Laboratory Tests
- **Complete blood count with peripheral smear**: macrocytic/megaloblastic red cell morphology, possible pancytopenia.
- **Plasma total homocysteine (tHcy)**: elevated.
- **Urine homocystine**: elevated (homocystinuria).
- **Plasma amino acid panel**: low-to-normal methionine (hypomethioninemia); low SAM.
- **Urine and plasma methylmalonic acid (MMA)**: **normal** — key discriminating test versus combined cobalamin defects (cblC/D/F) and isolated methylmalonic acidemia disorders.
- **Newborn screening acylcarnitine profile**: propionylcarnitine (C3) **not elevated** — explains why cblE/cblG are missed on standard NBS.

LOINC/SNOMED suggestions: standard plasma amino acid and homocysteine assay LOINC codes (specific codes not independently verified in this session).

### Biomarkers
- Elevated total homocysteine and low methionine/SAM ratio are the principal biochemical biomarkers.

### Genetic Testing
- **Molecular confirmation**: Identification of biallelic pathogenic *MTRR* variants by sequence analysis (detects the great majority of reported pathogenic alleles per GeneReviews — "21/22 reported variants" detectable by sequencing).
- **Approach**: Given clinical/biochemical overlap between cblE and cblG (methionine synthase, *MTR*, deficiency) — "the clinical and biochemical features are virtually identical for both defects" — molecular testing (targeted gene sequencing or a remethylation-disorder gene panel including *MTRR*, *MTR*, *MMACHC*, *MMADHC*, *MTHFR*) is necessary to distinguish them, since biochemical testing alone cannot reliably differentiate cblE from cblG (WebSearch synthesis of Watkins 1989 AJMG paper; GeneReviews NBK1328).
- **Fibroblast complementation/enzyme studies**: Historically used to assign the cblE complementation group — methionine synthase activity in cultured fibroblasts is preserved with excess exogenous reducing agent but falls under limiting reducing-agent conditions in cblE (vs. uniformly decreased in cblG), enabling functional discrimination prior to/alongside molecular testing.

### Clinical Criteria / Differential Diagnosis
Per GeneReviews, cblE must be distinguished from:
- **Vitamin B12 deficiency** (nutritional) — normalizes with B12 replacement; distinguished by dietary history, low serum B12, and absence of a genetic cause.
- **MTHFR deficiency** — produces moderate homocystinuria with normal-to-low methionine but **lacks megaloblastic anemia** (a key distinguishing clinical feature, since MTHFR deficiency does not impair folate-independent hematopoiesis in the same way).
- **CBS (cystathionine beta-synthase) deficiency** (classic homocystinuria) — elevated **methionine** together with elevated homocysteine (vs. low methionine in cblE); classically features **ectopia lentis**, marfanoid habitus, and thromboembolism, generally absent in cblE.
- **cblG (methionine synthase/MTR deficiency)** — clinically and biochemically nearly indistinguishable; requires molecular/enzymatic complementation testing to differentiate.
- **cblC, cblD, cblF (combined remethylation + methylmalonic acidemia defects)** — distinguished by presence of elevated methylmalonic acid, which is absent in cblE.

### Screening
- Not part of standard newborn screening panels due to lack of a distinguishing acylcarnitine signature; GeneReviews notes screening could theoretically be achieved by measuring methionine and the methionine-to-phenylalanine ratio in dried blood spots, with total homocysteine as a second-tier marker, but this is **not currently standard practice** (WebSearch synthesis).

---

## 11. Outcome / Prognosis

- **Survival/mortality**: No specific mortality rate statistics were retrieved; the disorder is not classically described as acutely lethal when treated, though severe untreated cases with profound neurologic and hematologic compromise in infancy could carry significant morbidity/mortality risk (not independently quantified in sources retrieved).
- **Morbidity**: Intellectual disability, seizures, and visual impairment represent the chief chronic morbidities. The JIMD 2015 cohort paper (24 patients) reports that even with treatment, neurodevelopmental and ophthalmologic outcomes show only "moderate" improvement at best, and that evidence for early-treatment benefit is "weak" — indicating that, unlike some other treatable inborn errors, cblE carries a persistent morbidity burden even under current standard-of-care management.
- **Positive outcome signal**: A smaller subset (4 patients in one cited series) showed a clearer positive impact of early treatment on outcome, suggesting genotype- or presentation-dependent prognosis heterogeneity.
- **Complications**: Late-onset refractory hemolytic anemia has been documented as a rare, potentially treatment-related long-term complication in siblings on chronic hydroxocobalamin/betaine therapy, possibly preventable by hydroxocobalamin dose escalation (PMC11078714).
- **Prognostic factors**: Genotype (e.g., p.Ser454Leu associated with milder, non-neurologic phenotype); age/timing of treatment initiation; presence/absence of early neurologic involvement at diagnosis.

---

## 12. Treatment

### Pharmacotherapy
- **Parenteral hydroxocobalamin (OHCbl)** — the cornerstone of treatment. GeneReviews specifically emphasizes that **only the parenteral hydroxocobalamin form is effective** — cyanocobalamin and oral preparations are not adequate substitutes ("parenteral OHCbl (not the cyanocobalamin form or oral form) is the only effective preparation").
  - NCIT suggestion: NCIT:C15986 (Pharmacotherapy) as treatment_term, with therapeutic_agent bound to a CHEBI/NCIT term for hydroxocobalamin (CHEBI:20363, hydroxocobalamin, is a plausible CHEBI ID — verify against OAK before curation).
- **Betaine** — supplementation (starting dose approximately 250 mg/kg/day cited in GeneReviews) to promote the alternative (cobalamin-independent) remethylation pathway via betaine-homocysteine methyltransferase (BHMT), lowering homocysteine and raising methionine.
  - CHEBI suggestion: CHEBI:17750 (betaine)
- **Folate/folinic acid supplementation** — may be used adjunctively to support remethylation capacity.

### Dietary Management
- **Normal dietary protein intake is appropriate**; GeneReviews explicitly states that "low-protein diets and medical foods... are not recommended" — an important distinction from CBS-deficiency homocystinuria management, which often does involve protein/methionine restriction.

### Surgical / Interventional
No surgical interventions are characteristic of cblE management.

### Supportive / Rehabilitative
- Developmental/early intervention services, physical/occupational therapy as indicated by neurodevelopmental impairment.
- Ophthalmologic monitoring and supportive management of visual impairment.
- Hematologic monitoring; transfusion support if severe anemia, though this is not typically the primary therapeutic modality given B12/betaine responsiveness.

### Advanced Therapeutics / Experimental
- No gene therapy, cell therapy, or RNA-based therapeutics specific to cblE were identified in the literature retrieved. "Functional correction by minigene expression" has been demonstrated as a **research/proof-of-concept tool** (Zavadáková et al. 2005, *Human Mutation*, PMID referenced in search results) to characterize variant pathogenicity in cultured cells, not as a clinical therapeutic.

### Treatment Outcomes
- Biochemical response (normalization/improvement of homocysteine, methionine, and hematologic parameters) is generally favorable with hydroxocobalamin + betaine.
- Neurodevelopmental and ophthalmologic response to treatment is **only moderate at best**, per the largest published cohort, and evidence supporting early-treatment benefit specifically is characterized as weak.
- **Adverse events**: Rare late-onset refractory hemolytic anemia has been documented as a treatment-era complication, discussed as potentially related to therapy dosing (PMC11078714).

### Treatment Strategy
- Lifelong parenteral hydroxocobalamin plus oral betaine is the standard combination approach; no formal published treatment algorithm/consensus guideline analogous to NCCN-style pathways was identified — management is guided by case-series experience and metabolic-disease expert consensus (e.g., within the broader "Disorders of Intracellular Cobalamin Metabolism" GeneReviews chapter, which covers cblE alongside cblA, cblB, cblC, cblD, cblF, and cblG under a shared general management framework).

---

## 13. Prevention

- **Primary prevention**: Not applicable in the traditional sense (not preventable by lifestyle/vaccination), as cblE is a genetic disorder; the only "primary prevention" avenue is reproductive genetic counseling and prenatal/preimplantation genetic testing in families with a known pathogenic variant.
- **Secondary prevention / early detection**: Because standard newborn screening does not reliably detect cblE, secondary prevention currently depends on clinical suspicion in infants presenting with unexplained megaloblastic anemia and/or developmental delay, prompting targeted biochemical (homocysteine/methionine) and molecular testing. Prenatal diagnosis has been performed in at-risk families with a known familial *MTRR* variant (referenced in the 2001 JIMD paper "CblE type of homocystinuria due to methionine synthase reductase deficiency: Clinical and molecular studies and prenatal diagnosis in two families").
- **Genetic counseling**: Central to prevention in this autosomal recessive disorder — informing carrier parents of 25% recurrence risk per pregnancy, and offering carrier testing to at-risk relatives (with molecular, not biochemical, methods) and prenatal diagnosis in subsequent pregnancies.
- **Screening programs**: A proposed but not widely implemented dried-blood-spot approach (methionine level / methionine-to-phenylalanine ratio, with second-tier homocysteine) could theoretically enable population newborn screening for cblE, per systematic-review literature on NBS for homocystinurias and methylation disorders (Huemer et al., PMID 25762406, cited in search results), but this is not current standard practice.
- **Prophylaxis**: No prophylactic pharmacologic regimen (e.g., preemptive cobalamin supplementation in unaffected at-risk newborns pending testing) was described in the sources retrieved as a standardized practice, though early empiric treatment while confirmatory testing is pending is a reasonable clinical approach given the biochemical responsiveness of the disorder.

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary or wildlife cases of *MTRR*-deficiency disease analogous to human cblE were identified in the literature searched (e.g., no OMIA entries were retrieved). The available animal data are exclusively **engineered mouse models** (below) rather than spontaneous natural disease in other species.

---

## 15. Model Organisms

### Mouse Models (Mtrr)
The **Mtrr gene-trap hypomorphic mouse model** (Mtrr^gt) is the principal model system used to study MTRR/methionine-synthase-reductase pathway biology, though it models the broader folate/methionine metabolic consequences of MTRR deficiency rather than being validated specifically as a full recapitulation of the human cblE clinical syndrome (megaloblastic anemia + neurodevelopmental disease).

- **Reproductive/developmental phenotypes**: "Methionine synthase reductase deficiency results in adverse reproductive outcomes and congenital heart defects in mice" (Padmanabhan et al., PMID 18413293; PMC3110750). Mtrr deficiency produces **hyperhomocysteinemia**, dysregulated **DNA methylation**, and developmental phenotypes including **neural tube defects, congenital heart defects, and placental defects**.
- **Transgenerational effects**: Notably, Mtrr-deficient mice show two distinct, separable phenotypes across generations: (1) adverse uterine-environment effects transmitted to wild-type daughters causing growth defects in wild-type grandprogeny, and (2) congenital malformations that persist independent of maternal environment for **5 generations** — an unusual transgenerational epigenetic inheritance phenomenon (WebSearch synthesis of PMC/related papers).
- **Liver phenotype**: "Mtrr hypomorphic mutation alters liver morphology, metabolism and fuel storage in mice" (PMID 32257815; PMC7109458) — Mtrr^gt/gt female mouse livers were enlarged, with eosinophilic hepatocytes and decreased glycogen content, associated with downregulation of glycogen synthesis genes.
- **Reproductive/fertility phenotype in males**: "Analysis of spermatogenesis and fertility in adult mice with a hypomorphic mutation in the Mtrr gene" (PMC7116358) — Mtrr^gt/gt adult testes were more spherical in shape than wild-type, but serum testosterone was normal, spermatogenesis proceeded typically, and sperm morphology/count/viability/fertility were normal — indicating **preserved male fertility despite altered testicular gross morphology**, i.e., a phenotype that does **not** fully recapitulate a severe reproductive deficit.
- **Metabolic derangement**: "Metabolic derangement of methionine and folate metabolism in mice deficient in methionine synthase reductase" (PMC1973089) documents the core one-carbon-metabolism biochemical perturbations (elevated homocysteine, altered folate distribution) in this model, directly relevant to the biochemical phenotype of human cblE.

### Model Limitations
The mouse Mtrr models are **hypomorphic (gene-trap) rather than null**, and the literature retrieved emphasizes developmental, reproductive, hepatic, and epigenetic-inheritance phenotypes rather than a hematologic (megaloblastic anemia) or neurologic phenotype directly paralleling the human cblE presentation. This represents a **potential human-model translational gap**: the mouse literature is dominated by reproductive/developmental and transgenerational-epigenetic findings, while the human disease is characterized primarily by megaloblastic anemia and neurodevelopmental impairment — suggesting the existing Mtrr mouse models may have **uncertain fidelity** for the core clinical hematologic/neurologic phenotype of human cblE disease, an important consideration for any `HUMAN_MODEL_MISMATCH`-type annotation if this disease is curated into a mechanistic knowledge base.

### Resources
- **MGI**: Mtrr, MGI:1891037 (Mouse Genome Informatics)
- No zebrafish (ZFIN), Drosophila (FlyBase), C. elegans (WormBase), or yeast (SGD) MTRR-ortholog disease models were identified in this search.

---

## Summary of Key Ontology Term Suggestions for KB Curation

| Category | Suggested term |
|---|---|
| Disease | MONDO:0009354 |
| Gene | hgnc:7473 (MTRR) |
| Phenotype: Megaloblastic anemia | HP:0001889 |
| Phenotype: Developmental delay | HP:0002194 |
| Phenotype: Seizures | HP:0001250 |
| Phenotype: Hypotonia | HP:0001252 |
| Phenotype: Nystagmus | HP:0000639 |
| Phenotype: Failure to thrive | HP:0001508 |
| Phenotype: Hemolytic-uremic syndrome | HP:0005575 |
| Phenotype: Cerebral atrophy | HP:0002059 |
| Cell type: Erythroid precursor | CL:0000765 |
| Cell type: Neuron | CL:0000540 |
| Anatomy: Bone marrow | UBERON:0002371 |
| Anatomy: Brain | UBERON:0000955 |
| Anatomy: Eye | UBERON:0000970 |
| Anatomy: Kidney | UBERON:0002113 |
| Treatment: Pharmacotherapy | NCIT:C15986 |
| Chemical: Betaine | CHEBI:17750 |

*(All ontology term suggestions should be independently verified via OAK/`just validate-terms` against current canonical labels before use in a curated KB entry, per standard practice — several GO term suggestions above in Section 6 are flagged as needing verification.)*

---

## Sources

- [OMIM #236270 — Homocystinuria-Megaloblastic Anemia, cblE Type](https://omim.org/entry/236270)
- [OMIM *602568 — Methionine Synthase Reductase; MTRR](https://omim.org/entry/602568)
- [GeneReviews — Disorders of Intracellular Cobalamin Metabolism (NBK1328)](https://www.ncbi.nlm.nih.gov/books/NBK1328/)
- [NORD/MONDO — Methylcobalamin deficiency type cblE](https://rarediseases.org/mondo-disease/methylcobalamin-deficiency-type-cble/)
- [Orphanet — Homocystinuria without methylmalonic aciduria](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=622&lng=EN)
- [ClinVar — MTRR c.1361C>T (p.Ser454Leu)](https://www.ncbi.nlm.nih.gov/clinvar/RCV000007449/)
- [ClinVar — MTRR c.2073C>T](https://www.ncbi.nlm.nih.gov/clinvar/RCV000907261/)
- [ClinVar — MTRR c.1952+17C>A](https://www.ncbi.nlm.nih.gov/clinvar/RCV003618859/)
- [ClinVar — MTRR c.-119T>C](https://www.ncbi.nlm.nih.gov/clinvar/RCV001530449/)
- [MedGen — C1856057](https://www.ncbi.nlm.nih.gov/medgen/344640)
- [Late-onset refractory hemolytic anemia in siblings treated for methionine synthase reductase deficiency (PMC11078714)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11078714/)
- [Methionine synthase reductase deficiency (CblE): A report of two patients and a novel mutation](https://www.tandfonline.com/doi/full/10.1179/1607845415Y.0000000017)
- [Clinical onset and course... 24 patients with the cblE or cblG remethylation defect (J Inherit Metab Dis, 2015)](https://link.springer.com/article/10.1007/s10545-014-9803-7)
- [Functional methionine synthase deficiency (cblE and cblG): clinical and biochemical heterogeneity (PMID 2688421)](https://pubmed.ncbi.nlm.nih.gov/2688421/)
- [cblE Type of homocystinuria due to methionine synthase reductase deficiency: Functional correction by minigene expression (PMID 15714522)](https://pubmed.ncbi.nlm.nih.gov/15714522/)
- [CblE type of homocystinuria due to methionine synthase reductase deficiency: Clinical and molecular studies and prenatal diagnosis in two families](https://link.springer.com/article/10.1023/A:1021299117308)
- [CblE type of homocystinuria: Mild clinical phenotype in two patients homozygous for a novel mutation in the MTRR gene](https://link.springer.com/article/10.1023/A:1025159103257)
- [Newborn screening for homocystinurias and methylation disorders: systematic review and proposed guidelines (PMID 25762406)](https://pubmed.ncbi.nlm.nih.gov/25762406/)
- [Methionine synthase reductase deficiency results in adverse reproductive outcomes and congenital heart defects in mice (PMID 18413293 / PMC3110750)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3110750/)
- [Mtrr hypomorphic mutation alters liver morphology, metabolism and fuel storage in mice (PMID 32257815 / PMC7109458)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7109458/)
- [Analysis of spermatogenesis and fertility in adult mice with a hypomorphic mutation in the Mtrr gene (PMC7116358)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7116358/)
- [Metabolic derangement of methionine and folate metabolism in mice deficient in methionine synthase reductase (PMC1973089)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1973089/)
- [Cloning and mapping of a cDNA for methionine synthase reductase, a flavoprotein defective in patients with homocystinuria (PNAS 1998)](https://pnas.org/content/95/6/3059)
- [UniProt Q9UBK8 — Methionine synthase reductase](https://www.uniprot.org/uniprotkb/Q9UBK8/entry)
- [MGI:1891037 — Mtrr](https://www.informatics.jax.org/marker/MGI:1891037)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 6 |
| Quoted claims found in source | 6 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 14 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.