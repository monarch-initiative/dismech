---
provider: claude_code
model: claude-opus-4-8[1m]
cached: false
start_time: '2026-07-10T17:27:12.242018'
end_time: '2026-07-10T17:31:57.093100'
duration_seconds: 284.85
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Infantile Spasms
  mondo_id: ''
  category: Complex
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
    extra_args: []
run_metadata:
  models_used:
  - claude-opus-4-8[1m]
  num_turns: 17
  total_cost_usd: 2.6728235
  session_id: 2e4b138c-ed8b-40a2-a1f3-530abe395a12
  stop_reason: end_turn
citation_count: 12
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Infantile Spasms
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Infantile Spasms** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

I have strong, verified source material. Here is the comprehensive research report.

---

# Comprehensive Research Report: Infantile Spasms (West Syndrome / Infantile Epileptic Spasms Syndrome)

*Attribution note: Much of the primary-literature evidence below was retrieved from **PubMed**, and DOI links are provided inline for each cited article, as required by the source database.*

---

## 1. Disease Information

**Overview.** Infantile spasms (IS) is an age-specific epileptic encephalopathy of infancy classically defined by a triad of (1) epileptic/infantile spasms, (2) a characteristic chaotic interictal EEG pattern called **hypsarrhythmia**, and (3) developmental arrest or regression. When all three are present the condition has historically been called **West syndrome**, first described by William James West in 1841 in his own son. The 2022 ILAE nosology renamed and broadened the entity to **Infantile Epileptic Spasms Syndrome (IESS)**, which requires epileptic spasms but does *not* require hypsarrhythmia, recognizing that spasms and developmental impairment can occur with atypical or absent hypsarrhythmia (According to PubMed — Zuberi et al., *Epilepsia* 2022, PMID 35503712, [DOI](https://doi.org/10.1111/epi.17239); Pavone et al., *Neurol Sci* 2020, PMID 32827285, [DOI](https://doi.org/10.1007/s10072-020-04600-5)).

The 2020 comprehensive review states the classical definition directly: *"the classical triad of (1) infantile spasms; (2) hypsarrhythmia, and (3) developmental arrest or regression as 'West syndrome'"* and notes it is *"currently regarded as a spectrum of disorders: the so-called infantile spasm syndrome (ISs), in association with other causal factors, including structural, infectious, metabolic, syndromic, and immunologic events, all acting on a genetic predisposing background"* (PMID 32827285, [DOI](https://doi.org/10.1007/s10072-020-04600-5)).

**Key identifiers.**
- **MONDO:** `MONDO:0018097` (infantile spasms / West syndrome) — verified via OLS.
- **HPO (phenotype):** `HP:0012469` Infantile spasms; `HP:0011097` Epileptic spasm.
- **OMIM:** No single OMIM number for the syndrome overall; genetically defined forms use "Developmental and epileptic encephalopathy" (DEE) series entries. The X-linked *ARX*-related form maps to **OMIM 308350** (EIEE1/DEE1); many others in the DEE series (e.g., *CDKL5*, *STXBP1*, *SPTAN1*).
- **ICD-10:** **G40.4** (other generalized epilepsy and epileptic syndromes; West syndrome). **ICD-11:** **8A62** (Infantile epileptic spasms syndrome / epileptic spasms).
- **MeSH:** **D013036** "Spasms, Infantile" (UMLS CUI C0037769, "West syndrome").
- **Orphanet:** **ORPHA:3451** (West syndrome).
- **NBO:** `NBO:0000734` infantile spasm.

**Data derivation.** Aggregate disease-level resources (OMIM, Orphanet, ILAE syndrome definitions) plus multicenter prospective cohorts (National Infantile Spasms Consortium; ICISS trial). Individual-patient/EHR-derived data exist chiefly through registries and consortium cohorts rather than routine EHR mining.

**Synonyms:** West syndrome; infantile spasms; epileptic spasms; infantile epileptic spasms syndrome (IESS, the current ILAE term); "salaam attacks/seizures" (historical, from the flexor posture); jackknife/flexion spasms; generalized flexion epilepsy (historical, Gibbs). Note the ILAE distinction: *infantile spasms* denotes onset <1 year in the classic window; *epileptic spasms* is the seizure semiology term, which can occur beyond infancy.

---

## 2. Etiology

IESS is **etiologically heterogeneous** — a final common phenotype reached by many upstream insults acting on the developing brain during a critical window (typically 3–12 months). The most useful etiologic framework is the ILAE structural/genetic/metabolic/infectious/immune/unknown scheme.

**Distribution of causes.** The 2024 genetics review summarizes: *"broadly, 60% of cases are thought to be structural, metabolic or infectious in nature, with the remainder genetic or of unknown cause"* (Snyder et al., *Genes* 2024, PMID 38540325, [DOI](https://doi.org/10.3390/genes15030266)). Historically ~60–70% are "symptomatic" (identifiable cause) and ~30–40% "cryptogenic/unknown," though modern genetic testing steadily shrinks the unknown fraction.

**Structural causes:**
- **Tuberous sclerosis complex (TSC)** — the single most recognizable cause (~10–25% of symptomatic IS). TSC affects *"approximately 1 per 6000–10,000 individuals"* and *"the pediatric neurologist is often responsible for making the initial diagnosis when the affected individual presents with infantile spasms or another early-onset epilepsy syndrome"* (Islam, *Semin Pediatr Neurol* 2021, PMID 33892851, [DOI](https://doi.org/10.1016/j.spen.2021.100875)).
- **Malformations of cortical development** — focal cortical dysplasia (FCD type II), hemimegalencephaly, lissencephaly, polymicrogyria. In a surgical IESS cohort, *"a genetic diagnosis was achieved in 47 children (80% of cohort),"* with germline variants in 46% and **brain somatic (mosaic) variants in 36%**, and mTOR-pathway/*SLC35A2*-related MOGHE being major causes (Coleman et al., *Brain Commun* 2025, PMID 39926610, [DOI](https://doi.org/10.1093/braincomms/fcaf034)).
- **Hypoxic-ischemic encephalopathy (HIE)**, perinatal stroke, periventricular leukomalacia, intracranial hemorrhage, CNS infection sequelae, trauma.

**Metabolic causes:** pyridoxine (vitamin B6)-dependent epilepsy (*ALDH7A1*), pyridoxal-5′-phosphate deficiency (*PNPO*), biotinidase deficiency, PKU (untreated), mitochondrial disorders, nonketotic hyperglycinemia, Menkes disease, congenital disorders of glycosylation, glucose transporter-1 (GLUT1/*SLC2A1*) deficiency.

**Infectious causes:** congenital CMV (most common infectious cause), congenital Zika, rubella, toxoplasmosis, herpes, bacterial meningitis/encephalitis sequelae.

**Risk factors:** prematurity, perinatal asphyxia, low birth weight, structural brain injury, family history of TSC or a monogenic DEE, chromosomal syndromes (esp. Down syndrome). Male predominance is modest (~55–60% male).

**Protective factors:** In TSC specifically, **preemptive/preventive antiseizure treatment is protective**. The EPISTOP trial showed vigabatrin started on the basis of epileptiform EEG (before clinical seizures) *"reduced the risk of clinical seizures (OR = 0.21, p = 0.032), drug-resistant epilepsy (OR = 0.23, p = 0.022), and infantile spasms (OR = 0, p < 0.001)"* (Kotulska et al., *Ann Neurol* 2021, PMID 33180985, [DOI](https://doi.org/10.1002/ana.25956)). No robust dietary/lifestyle protective factors are established for non-TSC IS. There are no well-validated protective germline variants.

**Gene–environment interaction.** The prevailing model is a **genetic predisposing background** on which structural/metabolic/infectious insults act (PMID 32827285). Somatic mosaicism (a "genetic" lesion confined to brain arising during development) is itself a gene×developmental-timing interaction, and a "two-hit" germline+somatic mechanism was documented in the surgical cohort (PMID 39926610).

---

## 3. Phenotypes

**Core seizure phenotype — epileptic/infantile spasms** (`HP:0011097` / `HP:0012469`): sudden, brief (0.5–2 s) symmetric contractions, typically **flexor, extensor, or mixed flexor-extensor**, characteristically occurring in **clusters** (dozens to hundreds/day), often on awakening. Onset **3–12 months** (peak 4–7 months). Frequency: near-universal by definition.

**Hypsarrhythmia** (EEG sign; ~82% of cohort): The National Infantile Spasms Consortium found *"Eighty-two percent of patients had hypsarrhythmia, but this was not associated with gender, mean age, preexisting developmental delay or epilepsy, etiology, or response to first-line therapy"* (Demarest et al., *Epilepsia* 2017, PMID 29105055, [DOI](https://doi.org/10.1111/epi.13937)). Suggested term: `HP:0002521` Hypsarrhythmia.

**Developmental impairment / regression** (`HP:0001263` Global developmental delay; `HP:0002376` Developmental regression): developmental arrest or regression (loss of social smile, visual attention, motor milestones) is a defining feature; long-term intellectual disability is frequent.

**Associated/downstream phenotypes:**
- Intellectual disability (`HP:0001249`) — majority; often moderate-severe.
- Autism spectrum features (`HP:0000717`) — elevated risk, esp. TSC.
- Evolution to other epilepsies, notably **Lennox-Gastaut syndrome** and focal epilepsy (`HP:0002123` Generalized myoclonic seizures; `HP:0002133` Status epilepticus in some).
- Visual inattention/cortical visual impairment (`HP:0100704` / `HP:0000618`).
- Microcephaly (`HP:0000252`) when secondary to structural/genetic cause.
- Hypotonia (`HP:0001252`).

**Severity & course:** Severe by definition; developmentally the trajectory strongly depends on **etiology** and **lead time to effective treatment** (see §8, §11). Cryptogenic/unknown-cause cases with normal pre-onset development and rapid response have the best cognitive outcomes.

**Quality-of-life impact:** Profound — combined seizure burden plus developmental/behavioral disability imposes very high caregiver burden and lifelong dependency in many. (Disease-specific validated QoL data are limited; ICISS used the **Vineland Adaptive Behaviour Scales** as the developmental outcome — see §11.)

---

## 4. Genetic / Molecular Information

**Scale of genetic contribution.** *"Over 28 copy number variants and 70 single gene pathogenic variants related to IESS have been discovered to date,"* with commonly reported etiologies including **trisomy 21** and single-gene variants (Snyder et al., PMID 38540325, [DOI](https://doi.org/10.3390/genes15030266)).

**Major causal genes (gene symbol / HGNC / mechanism):**
- **TSC1** (HGNC:12362) & **TSC2** (HGNC:12363) — loss of function → mTORC1 hyperactivation (mTORopathy). TSC2 more severe. (PMID 33892851)
- **ARX** (HGNC:18060; Xp21.3; OMIM 308350) — X-linked interneuronopathy; polyalanine expansions and LoF; classic monogenic IS model.
- **CDKL5** (HGNC:11411; X-linked) — DEE with early spasms.
- **STXBP1** (HGNC:11444) — synaptic vesicle release; haploinsufficiency.
- **SPTAN1, GRIN1, GRIN2B, SCN1A, SCN2A, SCN8A, KCNQ2, STK39, DNM1, GABRB3, FOXG1, MEF2C, CDKL5, SLC35A2, MTOR, AKT3, PIK3CA, DEPDC5, TSC1/2** (structural/mosaic mTOR pathway). *SLC35A2* somatic variants define MOGHE (mild malformation of cortical development with oligodendroglial hyperplasia).
- **Chromosomal:** Trisomy 21 (Down syndrome; strongest chromosomal association), 1p36 deletion, Miller-Dieker (17p13.3, *PAFAH1B1/LIS1*), 15q duplication, Pallister-Killian.

**Variant classes:** missense, nonsense, frameshift, splice-site, CNVs/deletions, polyalanine tract expansions (*ARX*), and **brain-restricted somatic mosaic** variants (mTOR pathway, *SLC35A2*). Classification per ACMG/AMP; deposited in ClinVar/DECIPHER.

**Somatic vs germline.** Landmark finding in surgical IESS: *"Germline pathogenic variants were identified in 27/59 (46%)… Pathogenic brain somatic variants were identified in 21/59 (36%)… Somatic mosaicism was a major cause of focal cortical dysplasia type II/hemimegalencephaly (81%) and mild malformation of cortical development with oligodendroglial hyperplasia (100%)"* (Coleman et al., PMID 39926610, [DOI](https://doi.org/10.1093/braincomms/fcaf034)).

**Functional consequences:** convergent themes — (i) **mTOR pathway hyperactivation** (TSC1/2, DEPDC5, MTOR, PIK3CA, AKT3); (ii) **GABAergic interneuron dysfunction / interneuronopathy** (ARX); (iii) **synaptic/ion-channel dysfunction** (STXBP1, SCN, KCNQ2, GRIN).

**Epigenetics / modifiers:** *SLC35A2* (glycosylation) and MOGHE illustrate a distinct mechanistic class. Formal modifier-gene and methylation data are limited; the diverse genetic background is itself thought to modify penetrance of structural insults (PMID 32827285).

**Diagnostic yield.** Trio exome/genome and CMA give the highest yields; up to 80% in structurally-defined surgical cohorts (PMID 39926610), lower (~30–40%) in unselected IS.

---

## 5. Environmental Information

- **Perinatal/environmental insults:** hypoxia-ischemia, prematurity, perinatal stroke, hypoglycemia, kernicterus, trauma, CNS infection.
- **Infectious agents:** congenital CMV (NCBITaxon:10359) is the leading infectious cause; also congenital Zika virus (NCBITaxon:64320), rubella, *Toxoplasma gondii*, HSV, and bacterial meningitis sequelae.
- **Toxins/lifestyle:** No established causal lifestyle exposure. Historically, IS was linked to whole-cell pertussis vaccine, but controlled studies attribute this to **coincidental timing** (onset window coincides with immunization schedule), not causation. **Vitamin B6 (pyridoxine) dependency/deficiency** is a treatable metabolic mimic to exclude.

---

## 6. Mechanism / Pathophysiology

IS is a **developmental-window disorder**: diverse insults converge on age-specific network dysfunction during a period of rapid synaptogenesis, myelination, and GABAergic maturation. No single unifying mechanism explains all cases; several complementary models are supported by animal work.

**Molecular pathways:**
- **mTOR (mechanistic target of rapamycin) hyperactivation** — the best-defined pathway (TSC1/2 → mTORC1 disinhibition). *"the identification of the responsible genes and gene products forming the mechanistic target of rapamycin complex… has inspired the search for targeted interventions"* (PMID 33892851). Suggested GO: `GO:0032008` positive regulation of TOR signaling; `GO:0038202` TORC1 signaling.
- **Stress axis / CRH hypothesis** — corticotropin-releasing hormone as an endogenous convulsant in the immature brain, motivating ACTH/steroid efficacy. The CRH model *"showed the higher proconvulsant potency of CRH in developing rats"* (Galanopoulou, *Brain Dev* 2013, PMID 23312951, [DOI](https://doi.org/10.1016/j.braindev.2012.12.005)). Proposed mechanism for ACTH: suppression of CRH via negative feedback and melanocortin receptor signaling. GO: `GO:0051458` corticotropin secretion.
- **GABAergic interneuronopathy** (ARX) — impaired tangential migration/function of cortical interneurons → excitation–inhibition imbalance. GABA also explains **vigabatrin** efficacy (irreversible GABA-transaminase inhibitor → ↑GABA). GO: `GO:0021853` cerebral cortex GABAergic interneuron migration; CHEBI: GABA `CHEBI:16865`.
- **Cortical–subcortical (brainstem) network dysfunction** — disruption of cortical–brainstem communication implicated in the spasm generator (PMID 23312951).

**Cellular processes / cell types:**
- **Cortical GABAergic interneurons** (`CL:0000617` GABAergic neuron) — dysfunction/interneuronopathy.
- **Cortical excitatory pyramidal neurons** (`CL:0000598` pyramidal neuron).
- **Dysmorphic neurons / balloon cells** in FCD II/TSC tubers (mTOR-driven).
- **Oligodendroglial hyperplasia** in MOGHE (*SLC35A2*).
- Neuroinflammation and abnormal neuronal migration/proliferation contribute (PMID 23312951).

**Causal chain (representative, mTOR/structural):** genetic or somatic mTOR-activating lesion → abnormal cortical cytoarchitecture (tubers/dysplasia, dysmorphic neurons) → aberrant excitatory–inhibitory network with immature-brain-specific hyperexcitability → epileptic spasms + hypsarrhythmia during the critical developmental window → epileptic encephalopathy disrupting normal development → developmental arrest/regression and later epilepsy (LGS/focal).

**Causal chain (stress/CRH model):** brain insult → dysregulated CRH/HPA-axis signaling in immature limbic/brainstem circuits → age-specific spasm generation → ACTH/steroid feedback suppresses CRH → clinical response (PMID 23312951).

**Anatomical/subcellular:** cerebral cortex (`UBERON:0000956`), brainstem, subcortical structures; subcellular convergence on the **lysosome/mTORC1 signaling hub**, synaptic vesicle machinery, and ion channels.

---

## 7. Anatomical Structures Affected

- **Primary organ:** brain (`UBERON:0000955`) — cerebral cortex (`UBERON:0000956`), often with subcortical/brainstem network involvement.
- **Body system:** central nervous system (`UBERON:0001017`).
- **Tissue/cell level:** cortical gray matter; GABAergic interneurons (`CL:0000617`), pyramidal neurons (`CL:0000598`), dysmorphic neurons/balloon cells (mTORopathy), oligodendrocytes (`CL:0000128`; MOGHE).
- **Subcellular:** mTORC1 signaling complex (lysosomal surface; GO CC `GO:0031931` TORC1 complex), synapse (`GO:0045202`), plasma-membrane ion channels.
- **Localization/lateralization:** generalized network dysfunction (bilateral hypsarrhythmia) but frequently arises from a **focal/lateralized structural lesion** (unilateral FCD, hemimegalencephaly) — a key point because focal lesions are surgically treatable. Asymmetric hypsarrhythmia suggests an underlying focal lesion.

---

## 8. Temporal Development

- **Onset:** infancy, typically **3–12 months** (peak 4–7 months); onset >2 years is atypical. Onset pattern: subacute emergence of spasm clusters, often initially mistaken for colic, startle, or reflux — contributing to diagnostic delay.
- **Course/progression:** an **epileptic encephalopathy** — the epileptic activity itself contributes to developmental deterioration beyond the underlying etiology (ILAE DEE concept; PMID 35503712). Spasms/hypsarrhythmia often **self-resolve by age 3–5 years** but frequently **evolve into other epilepsies** (Lennox-Gastaut syndrome, focal epilepsy).
- **Critical period / lead time.** Time to effective treatment is prognostically decisive. In ICISS 18-month follow-up: *"Increasing lead-time to treatment was associated with lower VABS scores… and worse epilepsy outcomes (p=0.023),"* and *"Initial control of spasms between days 14 and 42 of treatment was associated with higher mean VABS scores at 18 months (79.1 vs 63.2… p<0.001)"* (O'Callaghan et al., *Lancet Child Adolesc Health* 2018, PMID 30236380, [DOI](https://doi.org/10.1016/S2352-4642(18)30244-X)). Smartphone video capture shortened lead time: video-captured cases were *"diagnosed and started treatment 17 days earlier"* with *"a 25% greater response to initial standard treatment"* (Rao et al., *J Pediatr* 2023, PMID 36931494, [DOI](https://doi.org/10.1016/j.jpeds.2023.02.035)).
- **Remission:** treatment-induced (hormonal/vigabatrin) is the goal; spontaneous remission of spasms occurs but with poor developmental outcome if untreated.

---

## 9. Inheritance and Population

**Epidemiology.** Incidence approximately **2–5 per 10,000 live births** (roughly 0.25–0.42 per 1,000); prevalence in childhood on the order of 1.5–2 per 10,000. IS accounts for a large share of epilepsy with onset in the first year. (Orphanet ORPHA:3451; PMID 32827285.)

**Inheritance patterns (etiology-dependent):**
- **Autosomal dominant:** TSC1/TSC2 (though ~2/3 of TSC are de novo), STXBP1, many DEE genes (usually de novo dominant).
- **X-linked:** ARX (males affected; OMIM 308350), CDKL5.
- **Autosomal recessive:** several metabolic causes (ALDH7A1, PNPO, biotinidase).
- **Chromosomal/sporadic:** trisomy 21, CNVs — usually de novo.
- **Mosaic/somatic:** brain-restricted mTOR/SLC35A2 variants (not heritable, not in blood).
- **Multifactorial:** structural-acquired cases on a genetic background.

**Penetrance/expressivity:** highly variable; TSC shows near-complete penetrance but markedly **variable expressivity** (PMID 33892851). No genetic anticipation (except insofar as *ARX* polyalanine tracts). **Germline mosaicism** documented for TSC (recurrence risk counseling implication). **Consanguinity** increases recessive metabolic causes. **Carrier frequency** relevant for recessive metabolic forms.

**Demographics:** slight **male predominance** (~55–60%). No strong ethnic predilection overall; specific founder variants exist for particular metabolic genes in isolated populations. Geographic variation in etiology (e.g., higher perinatal-injury and infectious causes in resource-limited settings; PMID 35503712 gives guidance for resource-limited diagnosis).

---

## 10. Diagnostics

**Cornerstone:** **EEG** demonstrating **hypsarrhythmia** (high-amplitude, chaotic, asynchronous slow waves with multifocal spikes) — best captured on **sleep/overnight or video-EEG**, as hypsarrhythmia may be present only in sleep. Ictal EEG during a spasm shows the electrodecremental response. Note IESS can be diagnosed without hypsarrhythmia (PMID 35503712, 29105055).

**Home video** is increasingly a first diagnostic step — smartphone capture significantly shortens time to EEG, diagnosis, and treatment (Rao et al., PMID 36931494, [DOI](https://doi.org/10.1016/j.jpeds.2023.02.035)).

**Neuroimaging:** **brain MRI** (structural cause in a large fraction — tubers, FCD, HIE, malformation); may require repeat/high-resolution MRI. PET/SPECT for surgical localization of subtle lesions.

**Etiologic workup:**
- **Genetic testing:** chromosomal microarray (CMA), **trio whole-exome/whole-genome sequencing** (highest yield), targeted epilepsy gene panels; **testing of resected brain tissue** for somatic/mosaic variants when blood is negative and a lesion is resected (PMID 39926610).
- **Metabolic screen:** plasma/CSF amino acids, urine organic acids, lactate, ammonia, biotinidase, and a **pyridoxine (B6) / pyridoxal-5′-phosphate trial** to exclude treatable vitamin-responsive epilepsies; CSF glucose (GLUT1).
- **Infection:** congenital CMV (urine/saliva PCR, dried blood spot), TORCH.
- **TSC evaluation:** skin exam (Wood's lamp), echocardiogram, renal imaging, TSC1/TSC2 sequencing.

**Diagnostic criteria:** ILAE 2022 IESS definition (mandatory features, cautionary alerts, exclusionary features tabulated) (PMID 35503712).

**Differential diagnosis:** benign myoclonus of early infancy, benign infantile sleep myoclonus, Sandifer syndrome/GERD, colic, startle/hyperekplexia, tonic seizures, other early DEEs (Ohtahara syndrome, EIMFS).

---

## 11. Outcome / Prognosis

**Overall.** Guarded. IESS is *"a devastating developmental epileptic encephalopathy"* (PMID 38540325) with high rates of long-term intellectual disability, ongoing epilepsy, and autism. Prognosis is dominated by **(1) etiology** and **(2) speed/effectiveness of spasm control**.

**Developmental outcome quantified.** In ICISS at 18 months, mean VABS composite ~73; crucially, achieving early spasm cessation raised mean VABS from **63.2 to 79.1** (p<0.001), and freedom from seizures at 18 months was far more common in early responders (PMID 30236380, [DOI](https://doi.org/10.1016/S2352-4642(18)30244-X)).

**Evolution:** many progress to Lennox-Gastaut syndrome or drug-resistant focal epilepsy. Mortality is elevated relative to the general pediatric population, driven mainly by the underlying etiology and refractory epilepsy (including SUDEP risk).

**Prognostic factors (better outcome):** unknown/cryptogenic etiology with normal pre-onset development; short lead time to treatment; rapid and sustained response; absence of hypsarrhythmia relapse. (Worse: identified severe structural/genetic etiology, pre-existing developmental delay, long lead time, relapse.)

---

## 12. Treatment

**First-line standard therapies** (the NISC cohort showed first-line *standard* therapy is by far the strongest determinant of response — vigabatrin OR 5.2, prednisolone OR 8.0, ACTH OR 10.2; PMID 29105055, [DOI](https://doi.org/10.1111/epi.13937)):

1. **Hormonal therapy** — **ACTH (adrenocorticotropic hormone / tetracosactide/cosyntropin depot)** or **oral corticosteroids (high-dose prednisolone)**. MAXO: `MAXO:0000058`/pharmacotherapy `NCIT:C15986`; agents — corticotropin, prednisolone (`CHEBI:8382`).
2. **Vigabatrin** (irreversible GABA-transaminase inhibitor; ↑GABA) — **drug of choice for TSC-associated IS**, and effective generally. Risk: irreversible peripheral visual-field constriction/retinal toxicity requiring monitoring. Vigabatrin `CHEBI:63638`.

**Combination therapy.** ICISS demonstrated **hormonal + vigabatrin > hormonal alone** for early spasm cessation: *"no spasms were witnessed in 133 (72%) of 186 patients on hormonal therapy with vigabatrin compared with 108 (57%) of 191 patients on hormonal therapy alone (difference 15.0%… p=0.002)"* (O'Callaghan et al., *Lancet Neurol* 2017, PMID 27838190, [DOI](https://doi.org/10.1016/S1474-4422(16)30294-0)). However, the developmental advantage did **not** persist at 18 months (mean VABS 73.9 vs 72.7, p=0.55) (PMID 30236380).

**Comparative efficacy (meta-analysis).** *"There was no significant difference in the effectiveness of oral corticosteroids and ACTH… Low-dose ACTH had similar effectiveness… but conferred a lower risk of AEs… ACTH was more beneficial in controlling spasms than vigabatrin (RR = 1.31…) for patients without tuberous sclerosis complex"* (Guang et al., *Front Neurol* 2022, PMID 35222241, [DOI](https://doi.org/10.3389/fneur.2022.772333)).

**Other/second-line:** **ketogenic diet** (MAXO: `MAXO:0000010` dietary intervention / ketogenic diet); topiramate, zonisamide, valproate, pyridoxine (for B6-responsive forms), sulthiame. **Epilepsy surgery** — resection of a focal structural lesion (FCD, tuber, hemimegalencephaly → hemispherectomy) can be curative in lesional/mosaic cases (PMID 39926610). MAXO: surgical procedure `MAXO:0000004`.

**Precision/targeted therapy:** **mTOR inhibitors (everolimus, sirolimus)** for TSC-related epilepsy (mechanism-matched to mTORC1 hyperactivation); emerging gene-directed approaches for monogenic DEEs (PMID 38540325, 33892851). Everolimus (`CHEBI:68478`).

**Treatment strategy:** rapid diagnosis → prompt first-line standard therapy (hormonal ± vigabatrin; vigabatrin-first in TSC) → early EEG reassessment for response → escalate to ketogenic diet, alternative ASMs, or surgery/precision therapy if refractory. Speed matters (§8, §11).

---

## 13. Prevention

- **Primary/preemptive prevention in TSC:** the standout evidence — **EPISTOP** preventive vigabatrin (started on epileptiform EEG before clinical seizures) reduced clinical seizures, drug-resistant epilepsy, and **abolished infantile spasms (OR = 0, p < 0.001)** with no related adverse events (Kotulska et al., PMID 33180985, [DOI](https://doi.org/10.1002/ana.25956)). This has driven surveillance-EEG protocols in infants with known TSC.
- **Secondary prevention (early detection):** caregiver and pediatrician education (recognizing spasm clusters, home video), rapid-access EEG pathways to shorten lead time and improve outcomes (PMID 36931494, 30236380).
- **Etiology-directed:** newborn screening for treatable metabolic causes (biotinidase, PKU); congenital-infection prevention (CMV hygiene counseling, rubella vaccination).
- **Genetic counseling:** for TSC and monogenic DEEs — recurrence-risk assessment including germline mosaicism; prenatal/preimplantation options where a familial variant is known.
- **Tertiary prevention:** aggressive spasm control to limit encephalopathic developmental damage; developmental surveillance and early intervention.

---

## 14. Other Species / Natural Disease

Naturally occurring West syndrome/IESS as such is essentially a **human developmental syndrome**; there is no well-characterized spontaneous animal equivalent. The relevant cross-species work is in **model organisms** (§15). Conserved disease genes (TSC1/TSC2, ARX, mTOR pathway) have clear orthologs in mouse, rat, and zebrafish (NCBITaxon: mouse `10090`, rat `10116`, zebrafish `7955`), enabling comparative study of mTORopathy and interneuronopathy mechanisms.

---

## 15. Model Organisms

Multiple complementary rodent models exist, each capturing part of the phenotype (reviewed by Galanopoulou, *Brain Dev* 2013, PMID 23312951, [DOI](https://doi.org/10.1016/j.braindev.2012.12.005)):

- **CRH-induced model** — tests the stress hypothesis; CRH is more proconvulsant in developing rats, though it produces limbic (not classic flexion) seizures — a noted limitation.
- **NMDA model of "emprosthotonic" (flexion) seizures**, plus **prenatal betamethasone** and **prenatal stress** variants.
- **γ-butyrolactone spasms in a Down syndrome (Ts65Dn) mouse model** (trisomy 21 link).
- **Chronic models:** the **tetrodotoxin (TTX) model** and the **"multiple-hit" rat model** (structural + chronic), which reproduce spasms plus chronic epileptic and cognitive deficits and are used for drug screening.
- **Genetic interneuronopathy models:** **ARX loss-of-function mice** (polyalanine expansion / conditional knockouts) reproduce spasms via GABAergic interneuron dysfunction; **TSC conditional knockouts** model mTORopathy and respond to rapamycin.

The review frames these as testing distinct proposed mechanisms — *"cortical or brainstem dysfunction, disruption of normal cortical-subcortical communications, genetic defects, inflammation, stress, developmental abnormalities"* — and notes recent progress toward **mechanism-based treatments (mTOR inhibition, carisbamate, etc.)** (PMID 23312951).

**Model utility & limitations:** no single model reproduces the full human triad (spasms + hypsarrhythmia + developmental regression); hypsarrhythmia in particular is difficult to replicate. Models are strongest for testing etiology-specific mechanisms (mTOR, ARX/GABA, stress) and screening candidate therapies. Resources: MGI, RGD, ZFIN, IMPC/KOMP.

---

## Summary of Key Ontology Term Suggestions

| Domain | Term | ID |
|---|---|---|
| Disease | infantile spasms / West syndrome | MONDO:0018097 |
| Phenotype | Infantile spasms | HP:0012469 |
| Phenotype | Epileptic spasm | HP:0011097 |
| Phenotype | Hypsarrhythmia | HP:0002521 |
| Phenotype | Global developmental delay | HP:0001263 |
| Phenotype | Developmental regression | HP:0002376 |
| Phenotype | Intellectual disability | HP:0001249 |
| Cell type | GABAergic interneuron | CL:0000617 |
| Cell type | Pyramidal neuron | CL:0000598 |
| Anatomy | Cerebral cortex | UBERON:0000956 |
| Process | TORC1 signaling | GO:0038202 |
| Chemical | γ-aminobutyric acid (GABA) | CHEBI:16865 |
| Chemical | Vigabatrin | CHEBI:63638 |
| Chemical | Prednisolone | CHEBI:8382 |
| Chemical | Everolimus | CHEBI:68478 |
| Treatment | Pharmacotherapy | NCIT:C15986 |
| Treatment | Dietary intervention (ketogenic) | MAXO:0000010 |
| Treatment | Surgical procedure | MAXO:0000004 |

*(Ontology IDs for CHEBI/GO/CL/UBERON above should be re-verified against OAK before curation, per the dismech anti-hallucination SOP; MONDO:0018097 and the HP terms HP:0012469/HP:0011097 were confirmed via OLS during this research.)*

---

## Principal References (all retrieved from PubMed)

1. Zuberi SM et al. ILAE classification and definition of epilepsy syndromes with onset in neonates and infants. *Epilepsia*. 2022;63(6):1349-1397. PMID 35503712. [DOI](https://doi.org/10.1111/epi.17239)
2. Pavone P et al. West syndrome: a comprehensive review. *Neurol Sci*. 2020;41(12):3547-3562. PMID 32827285. [DOI](https://doi.org/10.1007/s10072-020-04600-5)
3. Snyder HE et al. Genetic Advancements in Infantile Epileptic Spasms Syndrome and Opportunities for Precision Medicine. *Genes*. 2024;15(3):266. PMID 38540325. [DOI](https://doi.org/10.3390/genes15030266)
4. Islam MP. Tuberous Sclerosis Complex. *Semin Pediatr Neurol*. 2021;37:100875. PMID 33892851. [DOI](https://doi.org/10.1016/j.spen.2021.100875)
5. Coleman M et al. The genetic landscape and classification of infantile epileptic spasms syndrome requiring surgery due to suspected focal brain malformations. *Brain Commun*. 2025;7(1):fcaf034. PMID 39926610. [DOI](https://doi.org/10.1093/braincomms/fcaf034)
6. O'Callaghan FJK et al. Safety and effectiveness of hormonal treatment versus hormonal treatment with vigabatrin for infantile spasms (ICISS). *Lancet Neurol*. 2017;16(1):33-42. PMID 27838190. [DOI](https://doi.org/10.1016/S1474-4422(16)30294-0)
7. O'Callaghan FJK et al. Vigabatrin with hormonal treatment versus hormonal treatment alone (ICISS): 18-month outcomes. *Lancet Child Adolesc Health*. 2018;2(10):715-725. PMID 30236380. [DOI](https://doi.org/10.1016/S2352-4642(18)30244-X)
8. Guang S et al. Hormonal Therapy for Infantile Spasms: A Systematic Review and Meta-Analysis. *Front Neurol*. 2022;13:772333. PMID 35222241. [DOI](https://doi.org/10.3389/fneur.2022.772333)
9. Demarest ST et al. The impact of hypsarrhythmia on infantile spasms treatment response (National Infantile Spasms Consortium). *Epilepsia*. 2017;58(12):2098-2103. PMID 29105055. [DOI](https://doi.org/10.1111/epi.13937)
10. Kotulska K et al. Prevention of Epilepsy in Infants with Tuberous Sclerosis Complex in the EPISTOP Trial. *Ann Neurol*. 2021;89(2):304-314. PMID 33180985. [DOI](https://doi.org/10.1002/ana.25956)
11. Galanopoulou AS. Basic mechanisms of catastrophic epilepsy — overview from animal models. *Brain Dev*. 2013;35(8):748-56. PMID 23312951. [DOI](https://doi.org/10.1016/j.braindev.2012.12.005)
12. Rao CK et al. The Effect of Smartphone Video on Lead Time to Diagnosis of Infantile Spasms. *J Pediatr*. 2023;258:113387. PMID 36931494. [DOI](https://doi.org/10.1016/j.jpeds.2023.02.035)

---

**Curation notes for the dismech entry.** (1) Model IESS as an etiologically heterogeneous DEE with a **structural / genetic / metabolic / infectious / unknown** etiology axis rather than a single mechanism. (2) The two strongest, most quotable causal chains for pathophysiology nodes are **mTORopathy** (TSC1/2 → mTORC1 → cortical dysplasia → spasms) and **GABAergic interneuronopathy** (ARX → interneuron dysfunction → E/I imbalance). (3) The lead-time-to-treatment → developmental-outcome relationship (PMID 30236380) is well-suited to a causal edge with strong human-clinical evidence. (4) Before committing any evidence item, run `just fetch-reference PMID:<id>` and `just validate-references` — the abstract quotes above are drawn verbatim from PubMed metadata but must pass the local snippet-substring check, and the CHEBI/GO/CL/UBERON IDs need OAK verification per the NEC/anti-hallucination SOP.