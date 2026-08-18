---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-18T04:54:05.977734'
end_time: '2026-08-18T04:58:56.050633'
duration_seconds: 290.07
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dilated Cardiomyopathy 1A
  mondo_id: ''
  category: Genetic
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
  num_turns: 14
  total_cost_usd: 1.7488452
  session_id: 8f052cfa-6748-543c-b3ba-b0c81cccbb41
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 31
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 11
  off_topic: 2
  off_topic_references:
  - PMID:17672370
  - DOI:10.1007/s12471-025-01955-2
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dilated Cardiomyopathy 1A
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 1A** covering all of the
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

I'll research Dilated Cardiomyopathy 1A (LMNA-related dilated cardiomyopathy) now and compile the full report inline.

# Research Report: Dilated Cardiomyopathy 1A (LMNA-Related Dilated Cardiomyopathy)

## 1. Disease Information

**Overview.** Dilated Cardiomyopathy 1A (CMD1A) is the autosomal dominant form of dilated cardiomyopathy (DCM) caused by pathogenic variants in *LMNA*, the gene encoding nuclear lamins A and C. It is characterized by left ventricular (LV) enlargement and/or reduced systolic function that is classically **preceded or accompanied by cardiac conduction system disease and/or atrial/ventricular arrhythmias**, distinguishing it clinically from most other genetic DCMs. Disease onset is typically in early-to-mid adulthood (third–fourth decade), and the disorder is notable for a disproportionately high risk of sudden cardiac death (SCD) and malignant ventricular arrhythmia relative to the degree of systolic dysfunction — SCD can be the first clinical presentation, even with a preserved ejection fraction (EF) (Captur et al., *Eur Heart J* 2018, [ahajournals summary](https://academic.oup.com/eurheartj/article/39/10/853/4583488)).

**Key identifiers:**
- **OMIM:** #115200 — CARDIOMYOPATHY, DILATED, 1A; CMD1A ([OMIM 115200](https://www.omim.org/entry/115200))
- **Gene:** *LMNA*, chromosome 1q22 (historically cited as 1q21)
- **MONDO:** MONDO:0007269 (per search results; cross-check against the local dismech MONDO cache before curation)
- **Orphanet:** ORPHA:300751 — "Familial dilated cardiomyopathy with conduction defect due to LMNA mutation" ([Orphanet 300751](https://www.orpha.net/en/disease/detail/300751)); the broader "Dilated cardiomyopathy" entry is ORPHA:154
- **ICD-10-CM:** I42.0 (Dilated cardiomyopathy) — LMNA-DCM has no distinct ICD-10 code and is captured under the generic DCM code
- **MeSH:** Cardiomyopathy, Dilated (D002311); Lamin Type A (D045186)
- **GeneReviews:** *LMNA*-Related Dilated Cardiomyopathy ([NBK1674](https://www.ncbi.nlm.nih.gov/books/NBK1674/)) — the single best-curated clinical synthesis, last formally reviewed by the same expert group that maintains ClinGen's cardiomyopathy gene curation.

**Common synonyms:** LMNA cardiomyopathy; laminopathy (cardiac laminopathy); Lamin A/C cardiomyopathy; CMD1A; Familial dilated cardiomyopathy with conduction system disease (or "DCM-CD"); older/allelic-disorder nomenclature sometimes conflates this with autosomal dominant Emery-Dreifuss muscular dystrophy (EDMD2) when skeletal myopathy is prominent.

**Evidence basis.** The literature is a mix of large multi-center **registries/cohorts** (French national LMNA registry underlying the Wahbi 2019 risk score, n=839; European cohorts from Captur et al., n>400), **family/pedigree studies** establishing autosomal dominant inheritance and penetrance, **single/multi-center retrospective case series** (e.g., the 18-patient series in *J Clin Med* 2021, [MDPI](https://www.mdpi.com/2077-0383/10/21/5075)), and increasingly **iPSC-cardiomyocyte and animal-model mechanistic studies**. Most quantitative clinical estimates (penetrance, arrhythmia risk, transplant rates) come from aggregated registry/cohort data rather than isolated case reports, giving reasonably strong human-clinical evidence for the natural history, though model-organism and iPSC data dominate the mechanistic literature.

---

## 2. Etiology

**Disease causal factor.** CMD1A is caused by heterozygous pathogenic/likely pathogenic variants in *LMNA* (missense, nonsense, frameshift, splice-site, small indels, and whole-gene deletions have all been reported; see HeartRhythm Case Reports on whole-gene deletion, [PMC7360979](https://pmc.ncbi.nlm.nih.gov/articles/PMC7360979/)). *LMNA* is a single genetic locus, but through alternative splicing produces two major nuclear lamina proteins, lamin A and lamin C, both of which are affected by most pathogenic variants.

**Genetic risk factors:**
- **Causal variants** — heterozygous *LMNA* pathogenic variants across the gene; missense variants cluster in the central α-helical rod domain (which mediates lamin dimerization/polymerization) and in the Ig-fold domain of the C-terminal tail.
- **Variant type as a risk modifier** — GeneReviews and multiple cohort studies report that **non-missense variants (truncating variants — nonsense, frameshift, canonical splice-site) and variants affecting specific residues confer a higher risk of malignant ventricular arrhythmia and earlier-onset conduction disease** than missense variants, though this is a probabilistic gradient rather than a strict genotype-phenotype rule (GeneReviews NBK1674; corroborated by the Wahbi 2019 risk score, which weights non-missense variant type as an independent predictor — [Circulation 2019](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.118.039410)).
- **Modifier genes** — no validated modifier locus has been established; some cohort work suggests digenic/oligogenic burden (a second cardiomyopathy-gene variant) may worsen phenotype, but this is not yet a robust, reproducible finding.
- **Family history / de novo status** — the great majority of cases are inherited in an autosomal dominant pedigree; a minority arise de novo (exact proportion not firmly established in the literature reviewed).

**Environmental / non-genetic risk factors:**
- **Sex** — male sex is a consistently reported independent risk factor for malignant ventricular arrhythmia and more severe/earlier disease course (cited in ESC 2023 cardiomyopathy guideline commentary and the Wahbi risk score).
- **Age** — advancing age increases cumulative penetrance (see §9); age at first cardiac abnormality is itself prognostic.
- **Physical/mechanical stress** — because the core mechanism involves mechanical fragility of the cardiomyocyte nucleus (§6), intense physical exertion is mechanistically plausible as an exacerbating factor, paralleling recommendations in other structural cardiomyopathies, though this is inferred from mechanism rather than a dedicated LMNA-specific epidemiological study identified in this search.
- **Standard heart-failure comorbidities** (hypertension, alcohol, obesity) likely modify the phenotype non-specifically but are not LMNA-specific risk factors per se.

**Protective factors.** No genetic or environmental protective factor specific to LMNA-DCM was identified in the literature surveyed; standard guideline-directed medical therapy (GDMT) for heart failure attenuates but does not eliminate progression (§12).

**Gene-environment interaction.** The dominant paradigm is a "two-hit" mechanical/biochemical model: the structurally weakened nuclear lamina (genetic hit) renders cardiomyocyte nuclei abnormally susceptible to mechanical stress from the beating heart and cytoskeletal (LINC-complex-transmitted) forces (environmental/physiological "hit"), producing nuclear envelope rupture, DNA damage, and downstream MAPK/ERK/JNK stress signaling (see §6 and the *Nature Cardiovascular Research* 2025 paper on microtubule forces driving nuclear damage, [Nature CVR](https://www.nature.com/articles/s44161-025-00727-w)).

---

## 3. Phenotypes

**Symptoms/clinical signs (cardiac):**
- **Conduction system disease** (the most characteristic and typically earliest manifestation): progressive PR-interval prolongation → first-degree AV block → second-degree → complete (third-degree) AV block; sinus node dysfunction/bradycardia; sinus arrest with junctional escape rhythms. LMNA variants account for **~33% of all DCM associated with AV conduction disease** and are found in **~5–10% of all idiopathic/familial DCM**, rising to up to **10% of familial DCM** overall.
  - Suggested HPO: **HP:0001678** (Atrioventricular block), **HP:0001635** (Congestive heart failure), **HP:0011712** (First degree atrioventricular block, if graded), **HP:0005180** (Third degree atrioventricular block)
- **Arrhythmias**: atrial fibrillation/flutter (often an early manifestation, sometimes preceding structural disease by years), premature ventricular contractions, non-sustained and sustained ventricular tachycardia, ventricular fibrillation.
  - HPO: **HP:0004308** (Ventricular tachycardia), **HP:0005110** (Atrial fibrillation), **HP:0001664** (Ventricular fibrillation)
- **Dilated cardiomyopathy / heart failure**: LV enlargement with reduced systolic function, symptoms of heart failure (dyspnea, fatigue, orthopnea, edema), and risk of LV mural thrombus with systemic embolization.
  - HPO: **HP:0001644** (Dilated cardiomyopathy), **HP:0001635** (Congestive heart failure), **HP:0002619** (Thromboembolism/systemic embolism-related terms)
- **Sudden cardiac death** — can be the *sentinel* presentation, notably in individuals with only mild/no LV dysfunction; this decoupling of arrhythmic risk from EF is the clinical hallmark that differentiates LMNA-DCM management from typical non-ischemic DCM (where ICD decisions hinge almost entirely on EF).
  - HPO: **HP:0001645** (Sudden cardiac death) if available in the ontology, else general arrhythmia terms.

**Skeletal muscle phenotypes** (present in a subset, overlapping the EDMD2/limb-girdle muscular dystrophy allelic spectrum):
- Muscle weakness ranging from subclinical/absent to a mild limb-girdle pattern; elevated serum creatine kinase (CK).
  - HPO: **HP:0003324** (Generalized muscle weakness), **HP:0003236** (Elevated CK), **HP:0003011** (Abnormality of the musculature)
- Joint contractures (elbow, Achilles, neck extensor rigidity) are classic for the EDMD end of the spectrum but less prominent in "pure" CMD1A.
  - HPO: **HP:0001371** (Flexion contracture)

**Laboratory abnormalities:**
- Elevated CK (variable, often mild)
- NT-proBNP/BNP elevation tracking heart-failure severity (non-specific)

**Phenotype characteristics:**
- **Age of onset**: typically early-to-mid adulthood (20s–40s); conduction disease usually precedes overt DCM by a median of **~7 years** in one cohort (per GeneReviews synthesis of a 64-patient study).
- **Severity/progression**: **progressive** — conduction disease → arrhythmia → ventricular dilation/dysfunction → heart failure, though the tempo is variable; a subset present with malignant arrhythmia/SCD before significant dilation.
- **Frequency data**: in one retrospective cohort, **24%** of genotype-positive individuals developed new-onset LV dysfunction and **7%** developed new-onset heart failure within a defined follow-up window (GeneReviews). LMNA carriers show the **highest incidence rate of disease penetrance among cardiomyopathy genes** studied in a recent multi-gene comparison — **17.7 per 100 person-years** — versus a 9% annual incidence of new cardiac phenotype and 61% cumulative penetrance over 4.4±2.9 years reported in an earlier prospective family study.
- **Quality of life impact**: driven primarily by heart-failure symptom burden and the psychological impact of living with a high SCD risk and (frequently) an ICD; a subset require heart transplantation at a young age (see §11), which itself carries major QoL and life-course implications. No LMNA-DCM-specific EQ-5D/SF-36 dataset was identified in this search; QoL data are generally extrapolated from broader DCM/ICD-recipient literature.

---

## 4. Genetic/Molecular Information

**Causal gene:** ***LMNA*** (HGNC:6636), chromosome 1q22, encoding **prelamin A/lamin A** and **lamin C** via alternative splicing of a single transcript (both are A-type lamins; lamin C lacks the C-terminal CAAX-farnesylation domain present in prelamin A).
- OMIM gene entry: *150330
- Allelic disorders (same gene, different phenotypic spectrum, useful for differential diagnosis and for confirming the gene's pleiotropy): autosomal dominant and recessive Emery-Dreifuss muscular dystrophy (EDMD2/EDMD3), limb-girdle muscular dystrophy type 1B, familial partial lipodystrophy type 2 (Dunnigan), Charcot-Marie-Tooth disease type 2B1, mandibuloacral dysplasia, and Hutchinson-Gilford progeria syndrome (HGPS) — the last caused by a specific *LMNA* c.1824C>T (p.Gly608Gly) splice variant producing progerin.

**Pathogenic variants:**
- **Variant classification**: per ACMG/AMP criteria as curated in ClinVar; the LMNA-cardiomyopathy ClinGen expert panel (part of ClinGen's Cardiomyopathy GCEP) has produced gene-specific ACMG rule specifications.
- **Variant type/class**: missense variants predominate but are distributed across the whole coding sequence rather than clustering in classic "hot-spot" residues; nonsense, frameshift, canonical splice-site, small in-frame/out-of-frame indels, and whole-gene deletions are also reported (e.g., HeartRhythm Case Reports whole-gene deletion case, [PMC7360979](https://pmc.ncbi.nlm.nih.gov/articles/PMC7360979/)).
- **Allele frequency**: pathogenic *LMNA*-DCM variants are essentially absent or present at extremely low frequency in gnomAD population databases, consistent with a highly penetrant, disease-causing (not risk-allele) model; population screening databases are used primarily to rule out benign polymorphisms rather than to estimate carrier frequency of pathogenic alleles.
- **Somatic vs. germline**: germline in essentially all reported cardiac cases (this is a Mendelian cardiomyopathy, not somatic-mosaic in mechanism, though germline mosaicism in a parent of an apparently de novo proband is a recognized possibility relevant to genetic counseling).
- **Functional consequence**: predominantly interpreted as **dominant-negative** and/or **haploinsufficiency**, disrupting lamin A/C polymerization into the nuclear lamina meshwork; there is ongoing mechanistic debate over the relative contribution of structural (mechanical) loss-of-function versus altered lamina-chromatin interaction (gene-regulatory) gain/loss-of-function, discussed further in §6.

**Modifier genes:** none robustly validated; candidate second-hit variants in other cardiomyopathy genes have been proposed in individual case reports but not established as systematic modifiers.

**Epigenetic information:** A-type lamins are themselves major organizers of peripheral heterochromatin via lamina-associated domains (LADs); LMNA mutation is mechanistically linked to **altered chromatin organization and LAD disruption**, which is proposed as a parallel (non-mechanical) disease mechanism — see §6.

**Chromosomal abnormalities:** whole-gene deletion of *LMNA* has been reported as a rare cause of the CMD1A phenotype (functionally equivalent to a null/haploinsufficient allele), but large structural chromosomal rearrangements are not a typical cause.

---

## 5. Environmental Information

- **Environmental toxins**: no specific toxin or occupational exposure has been established as a cause or trigger of LMNA-DCM in the literature surveyed; this is a monogenic disorder with environmental factors acting chiefly as modifiers of expressivity/timing rather than causal agents.
- **Lifestyle factors**: intense physical exertion is mechanistically plausible as an aggravating factor given the mechanical-fragility disease model (§6), though a dedicated exercise-restriction evidence base specific to LMNA-DCM (analogous to exercise guidance in ARVC) was not directly retrieved in this search; general heart-failure lifestyle factors (sodium/fluid intake, alcohol, obesity, sedentary behavior) apply non-specifically once cardiomyopathy is established.
- **Infectious agents**: not implicated; LMNA-DCM is not an infection-associated cardiomyopathy. (A concurrent viral myocarditis could in principle unmask or accelerate disease in a genetically predisposed individual, but this is inferred rather than specifically documented in the sources reviewed.)

---

## 6. Mechanism / Pathophysiology

LMNA-DCM pathogenesis is best understood as a convergence of two non-mutually-exclusive mechanistic hypotheses, both well supported in recent (2022–2025) literature:

**(A) Mechanical/structural hypothesis — nuclear envelope fragility and rupture.**
1. **Trigger**: Heterozygous *LMNA* pathogenic variant → impaired lamin A/C filament assembly and incorporation into the nuclear lamina meshwork underlying the inner nuclear membrane.
2. **Nuclear structural weakening**: Cardiomyocyte nuclei become **mechanically fragile**, with reduced stiffness and structural integrity (UniProt/GO: nuclear lamina, GO:0005652; nuclear envelope, GO:0005635).
3. **Cytoskeletal force transmission**: The **LINC complex** (Linker of Nucleoskeleton and Cytoskeleton — nesprins spanning the outer nuclear membrane, connecting to SUN proteins at the inner nuclear membrane, which anchor to the lamina) transmits actomyosin, microtubule, and desmin intermediate-filament-generated mechanical forces from the beating cardiomyocyte cytoskeleton directly onto the weakened nucleus. Recent work (2025) implicates **microtubule-generated forces specifically** as a key driver of this nuclear damage (*Nature Cardiovascular Research* 2025, [link](https://www.nature.com/articles/s44161-025-00727-w)).
4. **Nuclear envelope rupture**: Repeated contractile cycles cause transient/recurrent rupture of the nuclear envelope in cardiomyocytes.
5. **Downstream consequences**: Nuclear rupture triggers **early transcriptomic changes and innate immune/inflammatory activation** — a mechanism recently shown to be reversible by pharmacologic/genetic **disruption of the LINC complex** in iPSC and mouse models (bioRxiv 2024, [link](https://www.biorxiv.org/content/10.1101/2024.06.11.598511.full.pdf)), directly supporting the mechanical-primary model and identifying LINC disruption as a candidate therapeutic strategy (the basis for the gene-therapy program NVC-001, §12).
6. **DNA damage and stress-kinase activation**: Nuclear envelope compromise triggers DNA damage responses and activates **MAPK cascade branches — ERK1/2 and JNK** — well before overt echocardiographic/histopathological abnormalities appear in the *Lmna*-H222P mouse model (Muchir et al., *J Clin Invest* 2007, PMID: 17672370). This activation is causally linked to disease: pharmacologic MEK1/2 or JNK inhibition initiated even after cardiac dysfunction is detectable significantly improves ejection fraction and reduces LV dilation and fibrosis in this model — the mechanistic rationale that led to the p38/MEK-pathway-targeted drug ARRY-371797 (see §12).

**(B) Gene-regulatory hypothesis — lamina-chromatin (LAD) disruption.**
- A-type lamins organize **lamina-associated domains (LADs)** of peripheral heterochromatin and help position nuclear pores; LMNA mutation disrupts these lamina-chromatin tethering interactions, altering the transcriptional program of cardiomyocytes independent of acute mechanical rupture.
- Both hypotheses are considered complementary contributors, and current mechanistic literature explicitly frames the open question as "whether tissue-specific phenotypes arise from disrupted lamina-chromatin interactions and altered transcription, or from impaired structural function... resulting in nuclear envelope rupture."

**Cellular processes and downstream consequences:**
- **Fibro-fatty infiltration** of the myocardium, concentrated near the cardiac conduction system (basal septum), is the histopathological substrate linking LMNA mutation to the characteristic early AV block — shown by both autopsy series and cardiac MRI late-gadolinium-enhancement (LGE) studies (see §10).
- **Extracellular matrix remodeling**: recent work implicates **LOXL2-mediated ECM remodeling** driven by mutant (p.H222P) A-type lamins in both patient-derived cardiomyocytes and mouse models (bioRxiv 2025, [link](https://www.biorxiv.org/content/10.1101/2025.01.10.632312.full.pdf)), connecting nuclear lamina dysfunction to interstitial fibrosis.
- **Cardiomyocyte proliferative capacity** is restricted in *Lmna*-mutant mice, a proposed contributor to impaired regenerative/compensatory capacity (*Frontiers in Cardiovascular Medicine* 2021).
- **Cytoskeletal modulation**: broader remodeling of the actin/microtubule/desmin cytoskeletal networks has been documented as both a cause and consequence of nuclear mechanical stress (*Am J Physiol Cell Physiol* 2023, [link](https://journals.physiology.org/doi/full/10.1152/ajpcell.00471.2022)).

**Suggested GO terms**: GO:0005652 (nuclear lamina), GO:0034613 (cellular protein localization to nucleus), GO:0034405 (response to fluid shear stress, as a proxy for mechanotransduction), GO:0043065 (positive regulation of apoptotic process), GO:0007254 (JNK cascade), GO:0070371 (ERK1 and ERK2 cascade), GO:0006281 (DNA repair), GO:0030199 (collagen fibril organization / fibrosis-adjacent terms).
**Suggested CL terms**: CL:0000746 (cardiac muscle cell), CL:0002548 (cardiac fibroblast, for the fibrotic/ECM-remodeling arm), CL:0000187 (myofiber/skeletal muscle cell for the myopathic overlap phenotype).

**Causal chain summary (upstream → downstream):**
*LMNA* heterozygous pathogenic variant → defective lamin A/C polymerization/nuclear lamina assembly → mechanically fragile cardiomyocyte nucleus + disrupted LAD/chromatin organization → (mechanical arm) LINC-complex-transmitted cytoskeletal force → nuclear envelope rupture → DNA damage/innate immune activation + ERK1/2-JNK stress kinase activation → (parallel) conduction-system fibro-fatty infiltration and ECM remodeling → clinical manifestations in order of typical appearance: conduction disease → atrial/ventricular arrhythmia → LV dilation/dysfunction → heart failure/SCD.

**Molecular profiling / advanced technologies**: iPSC-cardiomyocyte models carrying patient *LMNA* variants show impaired lamin localization to the nuclear envelope and nuclear damage correlating with genotype (*Mol Biol Cell*, [PMC10846625](https://pmc.ncbi.nlm.nih.gov/articles/PMC10846625/)); single-cell/bulk transcriptomic work in the LINC-disruption bioRxiv study specifically profiles the "early transcriptomic changes and immune activation" signature in cardiomyocytes following nuclear rupture.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary**: heart — specifically the **cardiac conduction system** (sinoatrial node, atrioventricular node, His-Purkinje system) and the **ventricular myocardium** (predominantly left ventricle, with LV enlargement and systolic dysfunction).
- **Secondary**: skeletal muscle (in the myopathic subset, overlapping EDMD2/LGMD1B), systemically via thromboembolic complications from LV mural thrombus (e.g., stroke).
- **Body systems**: cardiovascular system (primary); musculoskeletal system (secondary, variable penetrance).
- Suggested UBERON: UBERON:0000948 (heart), UBERON:0002100 (trunk — for AV node/conduction system region), UBERON:0002082 (cardiac ventricle), UBERON:0006566 (cardiac conduction system, if present in UBERON), UBERON:0001134 (skeletal muscle tissue).

**Tissue and cell level:**
- Cardiac conduction tissue (fibro-fatty infiltration, especially at the **basal interventricular septum**, near the conduction system — this anatomical concentration explains the characteristic early AV block).
- Ventricular myocardium — cardiomyocyte hypertrophy/dilation, interstitial fibrosis.
- Skeletal myofibers (in myopathic cases).
- Suggested CL: CL:0000746 (cardiac muscle cell), CL:1000497 (kidney/vascular not applicable here — omit), CL:0002548 (cardiac fibroblast), CL:0000187 (myofiber).

**Subcellular level:**
- **Nuclear envelope / nuclear lamina** — the primary subcellular site of pathology (GO Cellular Component: GO:0005635 nuclear envelope, GO:0005652 nuclear lamina, GO:0034399 nuclear periphery).
- **LINC complex** components at the inner/outer nuclear membrane.
- Cytoskeletal elements (actin, microtubules, desmin intermediate filaments) as force-transmitting structures, not primary lesion sites but mechanistically central.

**Localization / lateralization:** Not applicable in the lateralized sense (this is a diffuse/global cardiac process), though fibrosis on LGE-CMR shows a characteristic **mid-myocardial, linear pattern concentrated in the basal septum** rather than a subendocardial or patchy distribution — a distinguishing imaging feature (§10).

---

## 8. Temporal Development

- **Onset**: Typically **early-to-mid adulthood** (20s–40s); pediatric-onset cases are described but are less typical than in some other genetic cardiomyopathies. Onset pattern is generally **insidious** for conduction disease (progressive PR prolongation over years) but can be **acute/dramatic** if the first presentation is malignant ventricular arrhythmia or sudden cardiac death.
- **Disease stages** (informal, not a formal staging system in the literature reviewed):
  1. **Pre-clinical/genotype-positive** — asymptomatic carrier, normal ECG/echo.
  2. **Conduction-disease stage** — ECG abnormalities (PR prolongation, bradycardia, AV block) with normal or near-normal LV function; median lag to LV dysfunction ~7 years.
  3. **Arrhythmic stage** — atrial fibrillation, ventricular ectopy/NSVT, elevated SCD risk, which can occur with minimal structural disease.
  4. **Structural/DCM stage** — LV dilation and reduced EF, progressive heart failure.
  5. **End-stage** — refractory heart failure requiring transplantation, or death (SCD or pump failure).
- **Progression rate**: Variable but generally considered **more aggressive and worse-prognosis** than typical idiopathic DCM — LMNA-DCM is repeatedly characterized in the literature as having a "worse clinical prognosis compared to other congenital forms of DCM."
- **Disease course pattern**: **Progressive**, punctuated by discrete arrhythmic events; not classically relapsing-remitting.
- **Remission**: No spontaneous remission is described; treatment (device therapy, GDMT) modifies but does not reverse the underlying course.
- **Critical periods / intervention windows**: The conduction-disease phase (before overt DCM) is considered a critical window for risk stratification and pre-emptive ICD decision-making, since malignant arrhythmia risk can precede — and is not reliably predicted by — the degree of systolic dysfunction that guides ICD decisions in typical DCM.

---

## 9. Inheritance and Population

**Epidemiology:**
- *LMNA* pathogenic variants account for **~5–13%** of idiopathic/familial DCM broadly (making *LMNA* the **second most common gene** implicated in nonsyndromic DCM after *TTN*), rising to **~10% of familial DCM** and **~33% of DCM cases specifically associated with AV conduction disease**.
- No population-wide prevalence/incidence rate (cases per 100,000) for CMD1A specifically was retrieved in this search; it should be estimated indirectly from general DCM prevalence (~1:250–1:500 in some population studies) multiplied by the *LMNA* attributable fraction, or sourced directly from Orphanet's epidemiology table for ORPHA:300751 during KB curation.

**Inheritance pattern**: **Autosomal dominant**, with rare instances of apparent recessive/compound heterozygous *LMNA* variants described for other laminopathies (not typically CMD1A).

**Penetrance**: **Age-dependent and ultimately high** — from studies cited: **~7% penetrance under age 20** rising to **~100% above age 60**, with overall penetrance considered **>90–95% by the seventh decade**. A separate prospective family cohort reported a **9% annual incidence** of newly documented cardiac phenotype among asymptomatic genotype-positive relatives, with **61% cumulative penetrance over 4.4±2.9 years** of follow-up. A large multi-gene comparison found LMNA carriers have the **highest incidence rate of disease penetrance (17.7 per 100 person-years)** among cardiomyopathy genes studied.

**Expressivity**: Highly **variable**, even within families carrying the identical variant — ranging from isolated conduction disease to severe DCM with early heart failure/transplant need to isolated skeletal myopathy, without an established deterministic genotype-phenotype rule (GeneReviews explicitly states "no specific genotype-phenotype correlations have been established," beyond the probabilistic association of non-missense variants with more malignant arrhythmic risk).

**Genetic anticipation**: Not a recognized feature of LMNA-DCM (this is not a repeat-expansion disorder).

**Germline mosaicism**: A recognized possibility relevant to genetic counseling of apparently de novo cases (implying residual recurrence risk for future pregnancies of an unaffected parent), consistent with general principles for autosomal dominant Mendelian disorders, though LMNA-DCM-specific mosaicism case data were not retrieved in this search.

**Founder effects / consanguinity**: No major population-specific founder variant was identified in the sources surveyed; *LMNA* pathogenic variants for CMD1A are generally private/family-specific rather than recurrent founder alleles (in contrast to the specific recurrent HGPS founder variant for progeria).

**Carrier frequency**: Given the near-absence of pathogenic *LMNA*-DCM alleles in gnomAD/population databases, background carrier frequency in the general population is very low; this is a rare, highly penetrant Mendelian disease rather than a common-variant susceptibility locus.

**Population demographics:**
- **Sex ratio**: Both sexes are affected (autosomal dominant), but **male sex is an independent risk factor for malignant ventricular arrhythmia and more severe disease course** — noted consistently in risk-stratification literature (Wahbi score; ESC guideline commentary).
- **Age distribution**: Concentrated in adults aged 20–60, with cumulative penetrance rising steeply with age as above; the disease is described as showing "**young onset, high penetrance, and frequent need for heart transplantation**" relative to other DCM etiologies (Captur et al., *Eur Heart J* 2018).
- **Geographic distribution**: No specific endemic geography identified; large registries are European (French national registry, other European cohorts) — likely reflecting referral/ascertainment patterns rather than a true geographic prevalence gradient, and this should be treated as a data-availability caveat rather than an epidemiological finding.

---

## 10. Diagnostics

**Clinical tests:**
- **12-lead ECG / ambulatory (Holter) ECG** — first-line, often the earliest abnormal test: PR prolongation, AV block (1°→3°), sinus node dysfunction, atrial fibrillation, ventricular ectopy.
  - LOINC candidates: 11524-6 (EKG study), relevant rhythm-strip LOINC panels.
- **Echocardiography** — LV dimensions, ejection fraction, wall motion; used both for diagnosis and serial surveillance.
- **Cardiac MRI with late gadolinium enhancement (LGE-CMR)** — a key diagnostic and prognostic imaging modality. LMNA-DCM shows a **characteristic mid-myocardial, linear LGE pattern concentrated in the basal septum**, correlating with fibrosis near the conduction system and with ECG conduction abnormalities (prolonged PR, widened QRS, atrial fibrillation). LGE burden is an established predictor of major adverse cardiovascular events in DCM generally.
- **Biomarkers**: serum CK (elevated in myopathic cases), NT-proBNP/BNP (heart-failure severity, non-specific). No LMNA-DCM-specific validated circulating biomarker (beyond genetic testing) was identified in this search.
- **Electrophysiology study**: may be used selectively to characterize conduction disease severity, though non-invasive ECG/Holter monitoring is the primary conduction-disease diagnostic.
- **Endomyocardial biopsy / histopathology**: not routine for diagnosis (genetic testing supersedes it), but historical autopsy/biopsy series established the fibro-fatty infiltration pattern near the conduction system that underlies current LGE-CMR interpretation; a 2024 case series specifically examined histopathology in nuclear-envelope lamin-related DCM (*Eur Heart J Case Rep* 2024, [ehjcr](https://academic.oup.com/ehjcr/article/8/8/ytae412/7729962)).

**Genetic testing:**
- **Recommended approach**: comprehensive cardiomyopathy multigene panel (including *LMNA*) or exome sequencing, per GeneReviews.
- **Sequence analysis** detects **>99%** of known *LMNA* pathogenic variants; **deletion/duplication (CNV) analysis** is needed for the remaining **<1%** (relevant for whole-gene-deletion cases).
- **Single-gene testing**: appropriate when a familial variant is already known (cascade testing of at-risk relatives).
- **Chromosomal microarray/karyotyping/FISH**: not primary diagnostic modalities for CMD1A (this is a sequence-level, not typically a large structural, disorder, aside from the rare whole-gene-deletion cases).
- **Mitochondrial DNA testing**: not applicable (LMNA-DCM is nuclear-genome, autosomal).

**Clinical/diagnostic criteria**: No disease-specific formal diagnostic scoring system beyond standard DCM criteria (LV enlargement + systolic dysfunction not explained by ischemia/other secondary cause) combined with a positive *LMNA* genetic test and characteristic conduction-disease phenotype. **Differential diagnosis** includes other genetic DCMs (*TTN*-truncating variants — the most common overall DCM gene — *TNNT2*, *MYH7*, *RBM20*, *FLNC*, *PLN*, *DES*, *SCN5A*), arrhythmogenic cardiomyopathy, sarcoidosis (also causes AV block + cardiomyopathy), and acquired/idiopathic DCM without conduction disease.

**Screening**: **Cascade genetic testing** of first-degree relatives of a confirmed proband is the standard screening strategy, given the autosomal dominant inheritance and high eventual penetrance; genotype-positive relatives then enter structured surveillance (annual evaluation if ECG abnormalities present, every 1–2 years for asymptomatic carriers per GeneReviews management guidance).

---

## 11. Outcome/Prognosis

- **Overall prognosis**: LMNA-DCM is repeatedly characterized as carrying a **worse prognosis than typical non-ischemic/idiopathic DCM**, driven by the disproportionate arrhythmic/SCD risk relative to degree of ventricular dysfunction.
- **Transplantation**: Captur et al. (*Eur Heart J* 2018) specifically highlight **"young onset, high penetrance, and frequent need for heart transplantation"** as defining features of the lamin A/C cardiomyopathy natural history — i.e., a meaningfully higher and earlier heart-transplant burden than in other DCM etiologies.
- **Sudden cardiac death**: SCD risk is a defining prognostic concern; it can occur even with preserved or mildly reduced EF, which is why LMNA-DCM has driven development of a **gene-specific arrhythmic risk calculator** (Wahbi 2019) rather than relying on EF-based general heart-failure ICD criteria alone.
- **Morbidity**: driven by progressive heart failure symptoms, recurrent arrhythmia (and associated ICD shocks/complications), thromboembolic events from LV mural thrombus, and — in the myopathic subset — progressive skeletal weakness.
- **Complications**: complete heart block requiring pacemaker; malignant ventricular arrhythmia requiring ICD (often escalating from pacemaker to ICD as risk becomes apparent); atrial fibrillation with thromboembolic stroke risk; end-stage heart failure.
- **Prognostic factors** (from the validated Wahbi 2019 LMNA-risk VTA calculator and related literature):
  - Male sex
  - Non-missense variant type (frameshift, nonsense, splice-site)
  - LV ejection fraction (particularly <45%)
  - Presence of non-sustained ventricular tachycardia (NSVT)
  - Atrioventricular conduction abnormalities
  - The web-based calculator is publicly available at [lmna-risk-vta.fr](https://lmna-risk-vta.fr/) and has undergone external validation (*Heart Rhythm* 2022/2023, [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1547527122026868)); experts note further refinement (e.g., incorporating variant location, not just type) is an active area of development (per 2025 Medscape coverage of LMNA testing under-utilization).
- **Prognostic biomarkers**: LGE extent/pattern on CMR (§10) functions as an imaging-based prognostic biomarker for adverse cardiovascular events, paralleling its role in DCM generally.

---

## 12. Treatment

**Pharmacotherapy (standard heart-failure GDMT)** — ACE inhibitors/ARBs/ARNI, beta-blockers, mineralocorticoid receptor antagonists, diuretics — applied per general heart-failure-with-reduced-EF guidelines once LV dysfunction is present; NCIT: **NCIT:C15986** (Pharmacotherapy) as the umbrella term, with individual agent classes as `therapeutic_agent` (e.g., NCIT:C2986 ACE Inhibitor class terms, NCIT beta-blocker terms).

**Device therapy** — central to LMNA-DCM management given the arrhythmic/conduction-disease phenotype:
- **Pacemaker implantation** for symptomatic bradyarrhythmia/AV block (guideline-directed pacing indications).
- **Implantable cardioverter-defibrillator (ICD)** — the single most disease-defining treatment decision. The **2023 ESC Cardiomyopathy Guidelines** recommend ICD placement in patients with *LMNA* variants **even above the conventional EF<35% threshold**: **Class IIa** if additional risk factors are present, **Class IIb** if no additional risk factors — an explicit gene-specific deviation from generic EF-based ICD criteria, reflecting the decoupled arrhythmic-vs-structural risk described above. Prophylactic ICD is also specifically considered for **LVEF<45% with NSVT**.
- **Gene-specific risk calculator** (Wahbi 2019 LMNA-risk VTA score; [lmna-risk-vta.fr](https://lmna-risk-vta.fr/)) to guide individualized primary-prevention ICD decisions, validated externally (2022/2023).
- Suggested NCIT: **NCIT:C50123** or related device-implantation terms for ICD/pacemaker (verify exact NCIT code during curation, per dismech convention that DEVICE modality lacks a fully reliable mechanical NCIT-ID mapping).

**Arrhythmia management**: antiarrhythmic pharmacotherapy, catheter ablation (for atrial fibrillation or recurrent VT), in addition to device therapy.

**Advanced/experimental therapeutics:**
- **p38/MAPK-pathway-targeted small molecule — ARRY-371797 (PF-07265803)**, a selective p38α MAPK inhibitor, developed based on the mouse-model finding that ERK1/2 and JNK (MAPK-branch) activation drives disease (§6):
  - **Phase 2 trial + long-term extension**: associated with improved 6-minute walk test at 12 weeks, preserved through 144 weeks, generally well tolerated (*Circ Genom Precis Med* 2022, [ahajournals](https://www.ahajournals.org/doi/10.1161/CIRCGEN.122.003730)).
  - **Phase 3 REALM-DCM trial** (multinational, randomized, placebo-controlled): **did not meet its primary efficacy endpoint** ("futility... without safety concerns"), despite the promising Phase 2 signal (*Circ Heart Fail* 2024, PMID: 38979608, [pubmed](https://pubmed.ncbi.nlm.nih.gov/38979608/)). This is an important negative/futility result underscoring that an unmet treatment need remains for LMNA-DCM specifically.
- **AAV-based gene therapy**:
  - **NVC-001** (Nuevocor) — an AAV-based gene therapy engineered to reduce aberrant mechanical stress on the nucleus and restore nuclear envelope integrity (targeting the mechanical/LINC-complex arm of pathogenesis, §6). **FDA IND clearance announced June 2025**; a first-in-human Phase 1/2 ascending-dose trial was planned to begin **early 2026** ([Nuevocor press release](https://www.prnewswire.com/news-releases/nuevocor-announces-fda-clearance-of-ind-for-nvc-001-for-lmna-related-dilated-cardiomyopathy-302477505.html); [CGTLive coverage](https://www.cgtlive.com/view/nuevocor-snags-ind-clearance-gene-therapy-trial-lmna-dcm)).
  - **AAV9-cTnT-GSLA01** (preclinical) — a cardiac-troponin-T-promoter-driven AAV construct targeting the biomechanical defect; extended lifespan in an *Lmna*-DCM mouse model from a median of **40 days (untreated)** to **51.5–103.5 days**, dose-dependently (bioRxiv 2025).
  - **Gene-supplementation (lamin-A addback) approaches** have shown that non-cardiomyocyte cell types are important therapeutic targets, complicating simple cardiomyocyte-restricted gene supplementation strategies (*JACC: Basic to Translational Science* 2024).
  - **Precise gene editing** of pathogenic Lamin A mutations has been shown to correct cardiac disease in preclinical models (*PNAS* 2025).
- Suggested `therapeutic_modality`: **GENE_THERAPY** for NVC-001/AAV approaches; **SMALL_MOLECULE** for ARRY-371797.

**Surgical/interventional**: cardiac transplantation for end-stage/refractory heart failure — notably needed **more frequently and at a younger age** in LMNA-DCM than in other DCM etiologies (Captur 2018).

**Supportive/rehabilitative**: standard heart-failure supportive care, activity guidance (mechanistically motivated caution around extreme exertion given the mechanical-stress disease model, though formal exercise-restriction guidelines specific to LMNA-DCM were not directly retrieved), and psychosocial support given the young age of onset and high device/transplant burden.

**Treatment strategy / personalized medicine**: Management is explicitly **genotype-guided** in this disease more than in most DCM — the gene-specific ICD threshold and the Wahbi risk calculator represent one of the more mature examples of precision-medicine risk stratification in inherited cardiomyopathy, and current expert commentary (2025) argues that *LMNA* genetic testing remains **"woefully underutilized"** relative to its clinical actionability ([Medscape 2025](https://www.medscape.com/viewarticle/testing-lmna-gene-mutations-woefully-underutilized-can-help-2025a1000inb)).

---

## 13. Prevention

- **Primary prevention**: Not applicable in the classic sense (this is a fully penetrant-eventually Mendelian genetic disease); the closest analog is **avoidance of unnecessary additional cardiac mechanical/arrhythmic risk** (e.g., cautious approach to competitive/extreme exertion), though specific guideline recommendations for LMNA carriers were not directly retrieved in this search.
- **Secondary prevention (early detection)**: **Cascade genetic testing** of at-risk relatives followed by structured cardiac surveillance (ECG/Holter and echocardiography — annual if abnormalities present, every 1–2 years if asymptomatic per GeneReviews) is the primary secondary-prevention strategy, enabling early conduction-disease detection before malignant arrhythmia or advanced structural disease develops.
- **Tertiary prevention**: prophylactic ICD implantation (guided by the gene-specific risk calculator and the ESC 2023 lowered-EF-threshold recommendation) to prevent SCD once risk factors are identified; GDMT to slow heart-failure progression; anticoagulation consideration for LV mural thrombus/atrial fibrillation to prevent thromboembolic stroke.
- **Genetic counseling**: central to management — informing at-risk relatives of the 50% inheritance risk per pregnancy, the variable/unpredictable expressivity, and the eventual near-complete penetrance, plus reproductive options (e.g., preimplantation genetic testing) for affected individuals planning families.
- **Screening programs**: no population-based (non-family-history-triggered) newborn or general screening program exists for LMNA-DCM, consistent with its status as a rare, family-history-driven Mendelian disorder rather than a population-screenable condition.
- **Public health / environmental interventions**: not applicable (no environmental exposure driver identified).

---

## 14. Other Species / Natural Disease

- **Taxonomy**: The core disease-modeling literature is concentrated in **mouse** (*Mus musculus*, NCBITaxon:10090). No naturally occurring veterinary (companion-animal) LMNA-cardiomyopathy analog was identified in this search; this appears to be a predominantly engineered-model (not naturally occurring in other species) disease within the literature surveyed.
- **Gene orthology**: *Lmna* is highly conserved across mammals; mouse *Lmna* is the direct ortholog used in all major animal models discussed below (NCBI Gene mouse Lmna: Gene ID 16905, for reference during curation).
- **Comparative biology**: The nuclear lamina/LINC-complex mechanotransduction mechanism is evolutionarily conserved across metazoans, and analogous laminopathy models exist in *Drosophila* (FlyBase disease model report cross-referenced in initial search results, [FlyBase FBhh0000157](https://flybase.org/reports/FBhh0000157.html)) and have been used to study lamin biology, though the flagship cardiac-phenotyping literature is mouse-based.
- **Zoonotic potential**: not applicable (non-infectious, monogenic disorder).

---

## 15. Model Organisms

**Mouse models** (the dominant and best-characterized system):
- ***Lmna*-H222P knock-in mouse** (Arimura et al., *Hum Mol Genet* 2005, PMID: 15548545) — the flagship model, originally derived from a human family with autosomal dominant Emery-Dreifuss muscular dystrophy. **Homozygous (H222P/H222P) males**: overtly normal embryonic development, but develop **reduced locomotor activity, abnormal stiff gait, chamber dilation, hypokinesia, and conduction defects**, with **death by 9 months of age**; females show a similar but **later-onset** phenotype — a documented **sex-difference finding in the animal model that parallels the human male-risk-factor observation** (§9, §11), strengthening translational relevance. This model:
  - Recapitulates both the skeletal-myopathy and cardiac-conduction/DCM arms of the human phenotype (**high fidelity** for the conduction-disease and DCM features).
  - Revealed the causal **ERK1/2 and JNK (MAPK) activation** occurring *before* detectable structural/functional cardiac abnormality (Muchir et al., *J Clin Invest* 2007), directly motivating the ARRY-371797 clinical program.
  - Has been used to test **MEK1/2 and JNK pharmacologic inhibition**, **AAV gene-supplementation/gene-editing**, and **LOXL2/ECM-remodeling-targeted** therapeutic strategies (§6, §12).
  - **Limitation**: it is a knock-in of one specific human EDMD-associated missense variant; genotype-phenotype heterogeneity in human LMNA-DCM (§9) means this single-variant model cannot fully capture the phenotypic range across the many different pathogenic *LMNA* alleles seen clinically — a **HUMAN_MODEL_MISMATCH**-type caveat worth flagging in curation, since H222P is not itself a DCM1A-specific (vs. EDMD-specific) allele in humans.
  - **Genetic-background modifier effect**: a dedicated study showed the cardiac phenotype severity in this model is modulated by mouse genetic background (*PMC6630059*), a useful caveat for interpreting cross-study variability.
- Additional *Lmna*-mutant mouse alleles (e.g., *Lmna*-null, other missense knock-ins) exist in the broader laminopathy literature, generally used to probe the relative contribution of the EDMD/CMD1A/lipodystrophy phenotypic spectrum, though H222P is the model most directly tied to the cardiac-DCM literature reviewed here.

**Cellular / iPSC models:**
- **Patient-derived iPSC-cardiomyocytes (iPSC-CMs)** carrying pathogenic *LMNA* variants show **impaired lamin localization to the nuclear envelope and nuclear damage** correlating with genotype (*Mol Biol Cell*, [PMC10846625](https://pmc.ncbi.nlm.nih.gov/articles/PMC10846625/); companion review *PMC11357512* on iPSC + animal-model platforms for pathogenic mechanism and novel therapies for LMNA-DCM).
- iPSC-CM systems are used specifically to investigate **nuclear envelope rupture, transcriptomic/immune activation, and LINC-complex-disruption rescue** (bioRxiv 2024 study), and represent a **high-fidelity human-genetic-background model** for the acute mechanical-stress mechanism, complementing the mouse model's organism-level (conduction system, hemodynamics, lifespan) readouts.

**Model characteristics summary:**
| Model | Relationship to human disease | Fidelity | Key limitation |
|---|---|---|---|
| *Lmna*-H222P knock-in mouse | RECAPITULATES conduction disease, DCM, skeletal myopathy | Moderate–High | Single EDMD-associated allele; not itself the most common human CMD1A-causing variant class |
| Patient iPSC-CMs (various *LMNA* variants) | RECAPITULATES nuclear envelope fragility/rupture and downstream transcriptomic/immune signature | High (for cellular/molecular arm) | Lacks organ-level readouts (conduction system anatomy, hemodynamics, lifespan) |
| *Drosophila* lamin models | Used for basic lamin/mechanotransduction biology | Lower (invertebrate, no closed circulatory conduction system analog) | Limited direct cardiac-conduction translational relevance |

**Resources for further model-organism lookup during curation**: MGI (mouse *Lmna* allele records), IMPC/KOMP (for any additional *Lmna* knockout/conditional alleles), Alliance of Genome Resources (cross-species orthology), Cellosaurus (for specific iPSC lines used in the cited studies).

---

## Summary of Key Ontology Term Suggestions for KB Curation

| Category | Suggested term(s) |
|---|---|
| MONDO | MONDO:0007269 (verify against local cache) |
| OMIM | 115200 |
| Orphanet | ORPHA:300751 |
| Causal gene | HGNC:6636 (*LMNA*), lowercase `hgnc:6636` per dismech convention |
| Key HP terms | HP:0001678 (AV block), HP:0001644 (Dilated cardiomyopathy), HP:0004308 (Ventricular tachycardia), HP:0005110 (Atrial fibrillation), HP:0003324 (Muscle weakness), HP:0003236 (Elevated CK) |
| Key GO terms | GO:0005652 (nuclear lamina), GO:0070371/GO:0007254 (ERK/JNK cascades), GO:0006281 (DNA repair) |
| Key CL terms | CL:0000746 (cardiac muscle cell), CL:0002548 (cardiac fibroblast) |
| Key UBERON | UBERON:0000948 (heart), UBERON:0002082 (cardiac ventricle) |
| Treatment NCIT | NCIT:C15986 (Pharmacotherapy), NCIT:C15238 (Gene Therapy) for NVC-001 |

---

## Sources

- [Entry - #115200 - CARDIOMYOPATHY, DILATED, 1A; CMD1A - OMIM](https://www.omim.org/entry/115200)
- [LMNA-Related Dilated Cardiomyopathy - GeneReviews®](https://www.ncbi.nlm.nih.gov/books/NBK1674/)
- [Orphanet: Familial dilated cardiomyopathy with conduction defect due to LMNA mutation](https://www.orpha.net/en/disease/detail/300751)
- [Lamin A/C cardiomyopathy: young onset, high penetrance, and frequent need for heart transplantation - European Heart Journal](https://academic.oup.com/eurheartj/article/39/10/853/4583488)
- [Clinical Features of LMNA-Related Cardiomyopathy in 18 Patients and Characterization of Two Novel Variants - J Clin Med / PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8584896/)
- [Development and Validation of a New Risk Prediction Score for Life-Threatening Ventricular Tachyarrhythmias in Laminopathies - Circulation (Wahbi et al. 2019)](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.118.039410)
- [LMNA-risk VTA calculator](https://lmna-risk-vta.fr/)
- [Timing of cardioverter-defibrillator implantation in patients with cardiac laminopathies — External validation of the LMNA-risk VTA calculator - Heart Rhythm](https://www.sciencedirect.com/science/article/pii/S1547527122026868)
- [2023 European Society of Cardiology guidelines on the management of cardiomyopathies](https://link.springer.com/article/10.1007/s12471-025-01955-2)
- [Testing for LMNA Gene Mutations is 'Woefully Underutilized' - Medscape 2025](https://www.medscape.com/viewarticle/testing-lmna-gene-mutations-woefully-underutilized-can-help-2025a1000inb)
- [Nuclear envelope rupture in cardiomyocytes orchestrates early transcriptomic changes and immune activation in LMNA-DCM that are reversed by LINC complex disruption - bioRxiv 2024](https://www.biorxiv.org/content/10.1101/2024.06.11.598511.full.pdf)
- [Microtubule forces drive nuclear damage in LMNA cardiomyopathy - Nature Cardiovascular Research 2025](https://www.nature.com/articles/s44161-025-00727-w)
- [Nuclear damage in LMNA mutant iPSC-derived cardiomyocytes is associated with impaired lamin localization to the nuclear envelope - Mol Biol Cell / PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10846625/)
- [Modulation of cytoskeleton in cardiomyopathy caused by mutations in LMNA gene - Am J Physiol Cell Physiol 2023](https://journals.physiology.org/doi/full/10.1152/ajpcell.00471.2022)
- [Mouse model carrying H222P-Lmna mutation develops muscular dystrophy and dilated cardiomyopathy similar to human striated muscle laminopathies - Hum Mol Genet 2005](https://academic.oup.com/hmg/article/14/1/155/2355798)
- [Activation of MAPK pathways links LMNA mutations to cardiomyopathy in Emery-Dreifuss muscular dystrophy - J Clin Invest / PMC](https://ncbi.nlm.nih.gov/pmc/articles/PMC1849984)
- [The Mutated p.H222P A-type Lamins Drive Loxl2-Mediated Extracellular Matrix Remodeling - bioRxiv 2025](https://www.biorxiv.org/content/10.1101/2025.01.10.632312.full.pdf)
- [Effect of genetic background on the cardiac phenotype in a mouse model of Emery-Dreifuss muscular dystrophy - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6630059/)
- [REALM-DCM: A Phase 3, Multinational, Randomized, Placebo-Controlled Trial of ARRY-371797 - Circulation: Heart Failure 2024](https://pubmed.ncbi.nlm.nih.gov/38979608/)
- [Efficacy and Safety of ARRY-371797 in LMNA-Related Dilated Cardiomyopathy: A Phase 2 Study - Circ Genom Precis Med 2022](https://www.ahajournals.org/doi/10.1161/CIRCGEN.122.003730)
- [Nuevocor Announces FDA Clearance of IND for NVC-001 for LMNA-Related Dilated Cardiomyopathy](https://www.prnewswire.com/news-releases/nuevocor-announces-fda-clearance-of-ind-for-nvc-001-for-lmna-related-dilated-cardiomyopathy-302477505.html)
- [Nuevocor Snags IND Clearance for Gene Therapy Trial in LMNA DCM - CGTLive](https://www.cgtlive.com/view/nuevocor-snags-ind-clearance-gene-therapy-trial-lmna-dcm)
- [Precise gene editing of pathogenic Lamin A mutations corrects cardiac disease - PNAS 2025](https://www.pnas.org/doi/10.1073/pnas.2515267122)
- [Non-Cell-Autonomous Cardiomyocyte Regulation Complicates Gene Supplementation Therapy for Lmna-Associated Cardiac Defects in Mice - JACC: Basic to Translational Science 2024](https://www.jacc.org/doi/10.1016/j.jacbts.2024.06.004)
- [LMNA-related cardiomyopathy: From molecular pathology to cardiac gene therapy - PMC 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12627347/)
- [Late gadolinium enhanced cardiovascular magnetic resonance of lamin A/C gene mutation related dilated cardiomyopathy - J Cardiovasc Magn Reson](https://link.springer.com/article/10.1186/1532-429X-13-30)
- [Deletion of entire LMNA gene as a cause of cardiomyopathy - HeartRhythm Case Reports / PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7360979/)
- [Nuclear envelope lamin-related dilated cardiomyopathy: a case series including histopathology - Eur Heart J Case Rep 2024](https://academic.oup.com/ehjcr/article/8/8/ytae412/7729962)
- [Contemporary Insights into LMNA Cardiomyopathy - Current Cardiology Reports 2025](https://link.springer.com/article/10.1007/s11886-025-02195-x)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 11 |
| Off topic | 2 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:17672370` (1 mention) - [Diagnosis of breast diseases by mammography in combination with MRI].
  - shared terms: disease
- `DOI:10.1007/s12471-025-01955-2` (2 mentions) - 2023 European Society of Cardiology guidelines on the management of cardiomyopathies
  - shared terms: heart

Weighed against this report's own most characteristic terms: `lmna`, `cardiac`, `disease`, `cardiomyopathy`, `heart`, `lmna-dcm`, `variant`, `conduction`, `nuclear`, `genetic`, `ventricular`, `dcm`, `gene`, `risk`, `lamin`, `pathogenic`, `penetrance`, `model`, `phenotype`, `arrhythmia`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.