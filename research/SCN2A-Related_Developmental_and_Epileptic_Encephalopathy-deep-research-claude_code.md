---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8
cached: false
start_time: '2026-07-18T14:09:04.232561'
end_time: '2026-07-18T14:14:04.736605'
duration_seconds: 300.5
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: SCN2A-Related Developmental and Epileptic Encephalopathy
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-4-8
  web_search_requests: 7
  num_turns: 9
  total_cost_usd: 1.4949329999999998
  session_id: bd7342a5-0a9f-454c-ad50-145719504f34
  stop_reason: end_turn
citation_count: 21
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SCN2A-Related Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **SCN2A-Related Developmental and Epileptic Encephalopathy** covering all of the
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

I've got a strong evidence base across the clinical, genetic, mechanistic, and therapeutic literature. Writing the full report now.

---

# Research Report: SCN2A-Related Developmental and Epileptic Encephalopathy

sup Harry — here's the deep dive on SCN2A-DEE. Quick framing before we wade in, because it's the thing that makes this whole disease make sense: SCN2A is one of those genes where the *direction* the mutation pushes the channel — turning the volume up (gain-of-function) versus muting it (loss-of-function) — splits the disorder into two almost opposite clinical worlds that happen to share a gene. Think of one sodium channel gene as a thermostat that can get stuck either too hot or too cold, and the whole downstream house behaves completely differently depending on which way it jammed. Hold onto that dichotomy; it's the spine of everything below.

A note on evidence discipline for the curator: I've flagged PMIDs I'm confident about. Snippets below drawn from abstracts should still be run through `just fetch-reference` + `just validate-references` before they land in YAML — treat them as leads, exact-quote-verified only after fetching.

---

## 1. Disease Information

**Overview.** SCN2A-related developmental and epileptic encephalopathy (SCN2A-DEE) is a rare, autosomal-dominant, monogenic neurodevelopmental disorder caused by pathogenic variants in *SCN2A*, the gene encoding the α-subunit of the brain voltage-gated sodium channel **Na_V1.2**. It sits within a broad *SCN2A*-related phenotypic spectrum that ranges from benign self-limited neonatal/infantile epilepsy through severe early- and late-onset epileptic encephalopathy to autism spectrum disorder and intellectual disability *without* epilepsy. The "DEE" label specifically denotes the phenotype where refractory seizures co-occur with — and contribute to — developmental impairment.

The canonical OMIM disease entity is **Developmental and Epileptic Encephalopathy 11 (DEE11)**, "an autosomal dominant seizure disorder characterized by neonatal or infantile onset of refractory seizures with resultant delayed neurologic development and persistent neurologic abnormalities" (OMIM #613721).

**Key identifiers.**
- **Gene:** *SCN2A* — OMIM **182390**; HGNC **10588** (`hgnc:10588`); chromosome **2q24.3**; NCBI Gene 6326; UniProt **Q99250** (SCN2A_HUMAN, Na_V1.2).
- **Disease:** OMIM **#613721** (DEE11). MONDO candidate: **MONDO:0012588** (developmental and epileptic encephalopathy, 11) — *verify against the broader "SCN2A-related" grouping term with OAK before binding.* Orphanet: the SCN2A-DEE phenotype is captured under ORPHA entries for early infantile DEE / malignant migrating partial seizures of infancy (confirm exact ORPHA code).
- **ICD-10:** G40.4 (other generalized epilepsy and epileptic syndromes) is the usual proxy code; **ICD-11:** 8A61 (developmental and epileptic encephalopathies).
- **MeSH:** covered under "Spasms, Infantile" / "Epilepsy, Generalized" / "Epileptic Syndromes"; no SCN2A-specific MeSH descriptor.

**Synonyms / alternative names:** SCN2A encephalopathy; SCN2A-related epilepsy; DEE11; early infantile epileptic encephalopathy 11 (EIEE11, older term); *SCN2A* epileptic encephalopathy; Na_V1.2 channelopathy; benign familial neonatal-infantile seizures (BFNIS, the mild end of the same spectrum, distinct phenotype).

**Data provenance:** Information is drawn from aggregated disease-level resources (OMIM, Orphanet, GeneReviews, HPO) and cohort literature (Wolff et al. 2017; Sanders et al. 2018), *not* from individual EHR records. The large phenotype cohorts (e.g., Wolff 2017, n=201) are curated case aggregations rather than population EHR extractions.

Sources: [OMIM #613721](https://omim.org/entry/613721), [OMIM 182390](https://omim.org/entry/182390), [MalaCards DEE11](https://www.malacards.org/card/developmental_and_epileptic_encephalopathy_11).

---

## 2. Etiology

**Primary cause — genetic.** SCN2A-DEE is caused by **heterozygous pathogenic variants in *SCN2A***, the great majority arising **de novo** (new mutations not inherited from either parent). There is no infectious, environmental, or acquired cause of the core disorder; it is a pure monogenic channelopathy. The severity and clinical direction are set by *how* the variant alters Na_V1.2 biophysics:

- **Gain-of-function (GoF)** variants → increased channel activity/neuronal hyperexcitability → **early-onset (<3 months) seizures / DEE**.
- **Loss-of-function (LoF)** variants → reduced channel activity → **late-onset (>3 months) epilepsy and/or autism/intellectual disability**, often without early seizures.

> "SCN2A pathogenic variants cause either gain or loss of channel function, which correlates well with the clinical phenotype. Gain-of-function variants are associated with early-onset seizures... whereas loss-of-function results in late-onset severe epilepsy and/or autism." (synthesized from the genotype–phenotype literature; **Wolff et al. 2017, PMID 28379373**; **Sanders et al. 2018, PMID 30301539**).

**Genetic risk factors.** The causal variant itself is the risk factor — there is no known common susceptibility locus. Recurrent DEE-causing GoF hotspots include **p.Arg1882Gln (R1882Q)** and **p.Arg853Gln (R853Q)** (note R853Q is functionally a LoF/mixed variant associated with later onset and treatment resistance), **p.Leu1563Val**, **p.Glu1211Lys**, and **p.Met1770Leu**, among others. De novo occurrence in a gene under strong evolutionary constraint (very low tolerance to LoF in gnomAD; high pLI) is the dominant "risk mechanism."

**Environmental risk factors.** None established for causation. Advanced **paternal age** is a general risk factor for de novo mutations across the genome and is a plausible (not disorder-specific) contributor. Sex is not a strong risk modifier (see §9). No toxin, infection, or occupational exposure is implicated.

**Protective factors.** None genetic or environmental are established for disease occurrence. On the *therapeutic-response* axis, the GoF-vs-LoF distinction is the closest thing to a "modifier": GoF patients respond to sodium-channel blockers, whereas the same drugs are ineffective or harmful in LoF patients — a functional-genotype modifier of outcome rather than of onset.

**Gene–environment interactions.** Not a meaningful axis for this monogenic disorder; the phenotype is variant-determined. Fever and intercurrent illness can *trigger* seizures (as in most epilepsies) but do not modify the underlying etiology.

Sources: [Wolff et al. 2017, Brain](https://academic.oup.com/brain/article/140/5/1316/3098477), [PubMed 28379373](https://pubmed.ncbi.nlm.nih.gov/28379373/).

---

## 3. Phenotypes

The phenotype is bimodal along the GoF/LoF axis. Below, phenotypes are grouped with suggested HPO terms, onset, severity, course, and approximate frequency. Frequencies are cohort estimates (chiefly Wolff 2017, n=201; Sanders 2018) and should carry their own evidence when a `frequency:` band is asserted.

**Core seizure / epilepsy phenotypes:**

| Phenotype | HPO term | Onset | Frequency | Notes |
|---|---|---|---|---|
| Seizures (any) | **HP:0001250** Seizure | Neonatal→childhood | Very frequent in DEE subset | Defining feature of the DEE phenotype |
| Neonatal onset seizures | **HP:0032807** Neonatal seizure / **HP:0002643** Neonatal onset | <28 days (GoF) | Common in early-onset GoF | |
| Infantile spasms / epileptic spasms | **HP:0012469** Infantile spasms | ~3–12 mo | Subset progress to West syndrome | Hypsarrhythmia on EEG |
| Focal-onset seizures | **HP:0007359** Focal-onset seizure | Variable | Frequent | tonic, tonic-clonic, focal, multifocal |
| Tonic seizures | **HP:0032792** Tonic seizure | Early | Frequent (GoF) | |
| Migrating focal seizures of infancy | **HP:0032794** (migrating focal) | Neonatal/infantile | *SCN2A* a major cause of EIMFS | Severe end |
| Status epilepticus | **HP:0002133** Status epilepticus | Variable | Occasional | |
| Absence / myoclonic seizures | **HP:0002121** Absence / **HP:0001336** Myoclonus | >3 mo | More common in later-onset | "absence and myoclonic seizures were more common in patients with seizure onset after 3 months" (OMIM) |
| Pharmacoresistant epilepsy | **HP:0002133**/**HP:0011171** | — | ~50% intractable | ~half achieve seizure freedom in childhood |

**Developmental / neurological phenotypes:**

| Phenotype | HPO term | Severity | Frequency |
|---|---|---|---|
| Global developmental delay | **HP:0001263** | Moderate–profound | Very frequent |
| Intellectual disability | **HP:0001249** | Mild→profound | Very frequent (esp. severe DEE) |
| Autism spectrum disorder / autistic behavior | **HP:0000729** | — | Frequent, esp. LoF |
| Absent/impaired speech | **HP:0001344** Absent speech | — | Frequent in severe DEE |
| Axial hypotonia | **HP:0008936** | — | Frequent (infancy) |
| Spasticity / hypertonia | **HP:0001257** / **HP:0001276** | — | Occasional (later) |
| Movement disorder (choreoathetosis, dystonia) | **HP:0100022** Abnormal movement / **HP:0002072** Chorea / **HP:0001332** Dystonia | — | Occasional; described in later-onset LoF |
| Microcephaly (acquired) | **HP:0000252** | — | Occasional |
| Cortical visual impairment | **HP:0100704** | — | Occasional in severe DEE |
| Feeding difficulties | **HP:0011968** | — | Frequent in severe forms |
| Ataxia / episodic ataxia | **HP:0001251** | — | Occasional (LoF spectrum) |

**Phenotype characteristics summary.**
- **Onset:** Bimodal — GoF ~neonatal to <3 months; LoF ~later infancy/childhood, sometimes with seizures only after 1–3 years or none at all (autism/ID-predominant).
- **Severity:** Highly variable; recurrent GoF hotspots (e.g., R1882Q) trend toward the most severe DEE with profound ID.
- **Progression:** Encephalopathy is typically **static-to-progressive** in early life; seizures may improve in childhood in ~50% even as developmental impairment persists — an important dissociation between seizure control and developmental trajectory.
- **QoL impact:** Severe DEE causes profound dependence — non-verbal status, inability to walk, gastrostomy feeding, and high caregiver burden; the autism/ID-predominant LoF end causes lifelong support needs but with more preserved motor function.

Sources: [OMIM #613721](https://omim.org/entry/613721), [Wolff et al. 2017](https://academic.oup.com/brain/article/140/5/1316/3098477), [FamilieSCN2A clinical info](https://www.scn2a.org/scn2a-related-disorders/clinical-information/).

---

## 4. Genetic / Molecular Information

**Causal gene.** ***SCN2A*** (Sodium Voltage-Gated Channel Alpha Subunit 2); HGNC:10588; OMIM 182390; 2q24.3. Encodes **Na_V1.2**, a ~2,005-aa transmembrane protein with four homologous domains (DI–DIV), each containing six segments (S1–S6); the S4 segments are voltage sensors and the DIII–DIV linker mediates fast inactivation. Na_V1.2 is expressed in the axon initial segment and unmyelinated/proximal axons of excitatory (glutamatergic) neurons, and dominates action-potential initiation and backpropagation early in development.

**Pathogenic variants.**
- **Type/class:** Overwhelmingly **de novo missense** variants; also nonsense, frameshift, splice-site, and whole-gene deletions (the latter cluster on the LoF/autism-ID end). "SCN2A mutations are predominantly de novo missense mutations."
- **Classification:** Per ACMG/AMP — many recurrent variants (R1882Q, R853Q, L1563V, etc.) are **Pathogenic**; novel missense variants are frequently **VUS** until functional testing resolves GoF vs LoF. Curate against **ClinVar** and **ClinGen** validity assertions (`CGGV:` if available).
- **Allele frequency:** Essentially absent from population databases (**gnomAD**) — consistent with de novo, highly penetrant, deleterious variants. *SCN2A* is strongly LoF-constrained (high pLI/low LOEUF).
- **Somatic vs germline:** Germline (de novo in the proband); rare parental **germline/somatic mosaicism** explains occasional recurrence in siblings (relevant to recurrence-risk counseling).
- **Functional consequence — the crux:**
  - **GoF:** enhanced persistent current, impaired inactivation, hyperpolarizing shift of activation → neuronal hyperexcitability → early seizures. Sensitive to sodium-channel blockers.
  - **LoF / haploinsufficiency:** reduced current density, loss of function → later epilepsy and/or ASD/ID. Sodium-channel blockers ineffective or worsening.
  - **Mixed variants:** some variants show combined GoF+LoF biophysics (e.g., certain EIMFS variants), blurring the dichotomy (**PMC9109789**; **Neurology Genetics 2025, PMC12854296**).

**Modifier genes.** No robust modifier gene established. Genetic background likely modulates severity (as in mouse strains) but this is not clinically actionable.

**Epigenetics / chromosomal abnormalities.** No disorder-specific methylation signature is established. Large **2q24.3 deletions/CNVs** spanning *SCN2A* (± neighboring *SCN1A*, *SCN3A*) produce contiguous-gene phenotypes and fall on the LoF/ASD-ID end — detectable by chromosomal microarray.

Suggested GO/gene annotations: `SCN2A` (`hgnc:10588`); GO:0005248 voltage-gated sodium channel activity; GO:0001518 voltage-gated sodium channel complex; GO:0019228 neuronal action potential; GO:0086010 membrane depolarization during action potential.

Sources: [GeneCards SCN2A](https://www.genecards.org/cgi-bin/carddisp.pl?gene=SCN2A), [Sanders et al. 2018 review PDF](https://www.scn2a.org/pdf/Progress_in_Understanding_and_Treating_SCN2A_Mediated_Diseases.pdf).

---

## 5. Environmental Information

Not a substantial contributor. SCN2A-DEE is monogenic and de novo. No toxin, radiation, pollution, occupational exposure, lifestyle factor, or infectious agent causes the disorder. As with epilepsy generally, **fever, sleep deprivation, and intercurrent illness** can *provoke* seizures in an already-established channelopathy, but these are triggers, not etiologic factors. This section is largely **not applicable**.

---

## 6. Mechanism / Pathophysiology

**The central causal chain (GoF arm):**

1. **De novo GoF missense variant in *SCN2A*** → altered Na_V1.2 gating (impaired fast inactivation, increased persistent Na⁺ current, hyperpolarized activation).
2. → **Increased Na⁺ influx and neuronal hyperexcitability** in glutamatergic cortical/hippocampal neurons (Na_V1.2 concentrated at the axon initial segment).
3. → **Excitation–inhibition imbalance and hypersynchronous network firing.**
4. → **Recurrent seizures / status epilepticus** beginning in the neonatal-to-early-infantile window.
5. → **Epileptic encephalopathy:** ongoing epileptiform activity plus the primary channel defect impair synaptic development → developmental delay, ID, and (in severe cases) regression.

This maps cleanly onto the dismech **`epilepsy_excitation_inhibition_imbalance`** module (conserved epilepsy pathway: ion-channel/synaptic dysfunction → excitation/inhibition imbalance → neuronal hyperexcitability and hypersynchrony → seizure generation → recurrent unprovoked seizures). The GoF arm is a textbook conformer at `epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance`.

**The LoF arm (mechanistically distinct):**

1. **LoF/haploinsufficiency variant** → reduced Na_V1.2 current.
2. → In **immature** neurons (where Na_V1.2 dominates AP initiation) → **hypoexcitability** and impaired action-potential firing/backpropagation → disrupted dendritic excitability, synaptic plasticity, and circuit maturation → **ASD/ID**.
3. → Paradoxically, in **mature** cortex, homeostatic/compensatory changes can produce network hyperexcitability and **later-onset seizures** — "immature glutamatergic cortical neurons from Scn2a+/− mice display decreased neuronal excitability, but mature neurons... are hyperexcitable."

This developmental-switch pathophysiology — the same gene causing hypoexcitability early and hyperexcitability late — is the mechanistic key to why one gene yields both autism-without-epilepsy and epilepsy phenotypes, and was worked out largely in mouse models (Spratt et al. 2019 Neuron; the *Scn2a* rodent-model review, **PMC11601800**).

**Cell types / compartments involved:**
- **Cell types (CL):** glutamatergic/excitatory cortical pyramidal neuron (**CL:0000598** pyramidal neuron; **CL:0000679** glutamatergic neuron); hippocampal pyramidal neurons. Na_V1.2 is chiefly excitatory-neuron-restricted (contrast Na_V1.1/*SCN1A* in interneurons — hence the opposite drug logic).
- **Subcellular (GO CC):** **axon initial segment (GO:0043194)**; node of Ranvier / axolemma; plasma membrane voltage-gated sodium channel complex (GO:0001518).
- **Biological processes (GO):** GO:0019228 neuronal action potential; GO:0086010 membrane depolarization during action potential; GO:0099509 regulation of presynaptic cytosolic calcium; GO:0050804 modulation of chemical synaptic transmission.

**Protein dysfunction:** Not misfolding/aggregation — this is a **gating/biophysical** defect. GoF variants shift the channel toward the open/non-inactivating state; LoF variants reduce functional channel density or trafficking. Functional consequence is resolved by patch-clamp electrophysiology and, increasingly, **patient iPSC-derived neurons**, which show "distinctive in vitro phenotypes" separating GoF and LoF cases (J Neurosci 2024, **jneurosci.org/content/44/8/e0692232023**).

**Metabolic / immune involvement:** None primary. No metabolic derangement, no autoimmune/inflammatory component. This is a pure electrical-signaling disorder — do not over-curate metabolic or immune mechanisms.

**Tissue damage:** No structural neurodegeneration is intrinsic; most brains are structurally normal on MRI (though rare cases with polymicrogyria/opercular dysplasia are reported — ScienceDirect S2950221724000242). "Damage" is functional — disrupted circuit development plus potential secondary injury from prolonged seizures/status epilepticus.

**Molecular profiling / advanced tech:** iPSC-derived neuron models (in vitro electrophysiology, GoF vs LoF separation); dynamic action-potential clamp; CRISPR-activation and cis-regulation functional-genomics rescue in mouse (SFARI 2025 report). Transcriptomic/proteomic disease signatures are model-derived, not clinical biomarkers.

Sources: [J Neurosci iPSC study](https://www.jneurosci.org/content/44/8/e0692232023), [Scn2a rodent model review PMC11601800](https://pmc.ncbi.nlm.nih.gov/articles/PMC11601800/), [Sanders 2018](https://www.scn2a.org/pdf/Progress_in_Understanding_and_Treating_SCN2A_Mediated_Diseases.pdf).

---

## 7. Anatomical Structures Affected

- **Organ / system:** Central nervous system, primarily **cerebral cortex** and **hippocampus** (**UBERON:0000955** brain; **UBERON:0000956** cerebral cortex; **UBERON:0002421** hippocampal formation). Body system: **nervous system** (UBERON:0001016). No primary involvement of other organ systems.
- **Tissue/cell level:** Gray-matter neuronal tissue; specifically **excitatory glutamatergic pyramidal neurons** (CL:0000598) of neocortex and hippocampus. GABAergic interneurons are relatively spared (mechanistically important — the inverse of *SCN1A*/Dravet).
- **Subcellular:** **Axon initial segment (GO:0043194)** and proximal axon — where Na_V1.2 sets AP threshold; also nodes of Ranvier and somatodendritic membrane for backpropagation.
- **Localization / lateralization:** Bilateral, diffuse cortical involvement; seizures may be focal/multifocal or generalized. Structural MRI is usually normal (bilateral, non-lesional). Rare malformation-of-cortical-development cases are the exception.

Sources: [Sanders 2018](https://www.scn2a.org/pdf/Progress_in_Understanding_and_Treating_SCN2A_Mediated_Diseases.pdf), [ScienceDirect polymicrogyria case](https://www.sciencedirect.com/science/article/pii/S2950221724000242).

---

## 8. Temporal Development

- **Onset:** Bimodal and **variant-determined**. GoF/DEE → **neonatal to <3 months** (often first days of life). LoF → **>3 months to years**, and the autism/ID-predominant subset may never develop epilepsy. Onset pattern is typically **acute** for seizures against a **chronic/insidious** developmental backdrop.
- **Stages / course:**
  - *Early-onset GoF DEE:* neonatal seizures → possible evolution to **West syndrome / infantile spasms** (3–12 mo) → childhood epilepsy with variable control. Encephalopathy tracks alongside.
  - *Later-onset:* childhood epilepsy, sometimes with movement disorder and episodic ataxia in the LoF spectrum.
- **Progression rate:** Variable. About **half of patients achieve seizure freedom during childhood; the other half remain intractable** (OMIM). Crucially, seizure improvement does **not** guarantee developmental improvement — cognitive impairment often persists.
- **Course pattern:** Chronic, lifelong. Seizures can be relapsing or evolve through age-dependent syndromes; developmental impairment is generally static-to-slowly-progressive rather than neurodegenerative.
- **Critical periods:** The **early-infantile window** is both the period of maximal seizure burden and the developmental window where intervention could most plausibly alter trajectory — the rationale for early functional testing to guide drug choice, and for the emerging ASO trials targeting infants.

Sources: [OMIM #613721](https://omim.org/entry/613721), [Wolff et al. 2017](https://academic.oup.com/brain/article/140/5/1316/3098477).

---

## 9. Inheritance and Population

**Epidemiology.**
- *SCN2A*-related disorders have an **estimated prevalence around 8 per 100,000**, with disease-causing variants arising in roughly **7.5 per 100,000 births** (FamilieSCN2A / cohort estimates). Over 1,000 individuals have been identified worldwide, and numbers are rising with expanded genetic testing. For a structured `Prevalence` record: `measure_type: BIRTH_PREVALENCE` or `POINT_PREVALENCE`, `prevalence_class: BAND_1_5_PER_10000`, `rate_per_100000: 7.5–8.0`, with the source phrasing in `notes`. *SCN2A* is among the most frequently implicated single genes in DEE and in de novo ASD.
- Incidence is not precisely established; de novo occurrence and ascertainment through sequencing complicate rate estimates.

**Inheritance (genetic).**
- **Pattern:** **Autosomal dominant** (**HP:0000006**); the overwhelming majority are **de novo** (`relationship_type` causal; onset from a new heterozygous variant).
- **Penetrance:** Effectively **complete/high** for pathogenic de novo DEE variants; the *mild familial* BFNIS end shows near-complete penetrance too but for a benign phenotype.
- **Expressivity:** **Highly variable** — even the same recurrent variant can produce a range of severity.
- **Anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Documented (parental gonadal/somatic mosaicism) — recurrence risk to siblings is low but **not zero** (~1–2% empiric), which matters for counseling.
- **Founder effects / consanguinity:** Not relevant — de novo dominant, no ancestry-specific founder alleles, no consanguinity role.
- **Carrier frequency:** Not applicable (dominant, de novo).

**Population demographics.**
- **Affected populations:** No ethnic/geographic predilection — occurs worldwide across all ancestries (expected for de novo dominant).
- **Sex ratio:** Roughly **equal (≈1:1)**; *SCN2A* is autosomal, so no strong sex bias, though ASD ascertainment can skew reported series slightly male.
- **Age distribution:** Onset in neonatal period through early childhood; the population is predominantly pediatric, with a growing cohort of surviving adolescents/adults.

Sources: [FamilieSCN2A clinical info](https://www.scn2a.org/scn2a-related-disorders/clinical-information/), [Decoding SCN2A Variants (J Clin Med 2025, PMC12156426)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12156426/).

---

## 10. Diagnostics

**Genetic testing — the diagnostic anchor.**
- **First-line:** **Next-generation sequencing** — epilepsy/DEE **gene panels**, **whole-exome sequencing (WES)**, or **whole-genome sequencing (WGS)** identify the causal *SCN2A* variant. Given the DEE presentation, early genetic testing is now standard of care because the result **directly changes treatment** (GoF → sodium-channel blockers; LoF → avoid them). MAXO: `MAXO:0000922`-family genetic testing / molecular diagnostic actions.
- **Chromosomal microarray (CMA):** detects 2q24.3 deletions/CNVs involving *SCN2A* (LoF/ASD-ID end).
- **Single-gene *SCN2A* testing:** appropriate when the phenotype strongly suggests it (e.g., neonatal-onset SCB-responsive seizures).
- **Variant interpretation:** ACMG/AMP classification via **ClinVar/ClinGen**; **functional characterization** (patch-clamp, iPSC-neuron electrophysiology) is increasingly used to resolve GoF vs LoF for VUS and to guide therapy — arguably the most consequential "diagnostic" beyond variant detection.

**Clinical / supportive tests:**
- **EEG:** seizure characterization; may show multifocal epileptiform discharges, **hypsarrhythmia** (if West syndrome), or migrating focal ictal patterns. Emerging work explores EEG features as correlates of variant function and outcome (medRxiv 2023.10.24.23296360).
- **Brain MRI:** usually **normal**; excludes structural/malformative mimics (rare polymicrogyria/opercular dysplasia cases exist).
- **Metabolic workup / lumbar puncture:** typically normal — used mainly to exclude treatable metabolic epilepsies (e.g., pyridoxine-dependent, GLUT1) in the differential before or alongside genetic testing.

**Differential diagnosis:** other DEE genes — *SCN1A* (Dravet; note opposite drug logic), *SCN8A*, *KCNQ2*, *KCNT1* (EIMFS), *STXBP1*, *CDKL5*, *PRRT2*; treatable metabolic epilepsies (pyridoxine-dependent/ALDH7A1, PNPO deficiency, GLUT1). The distinguishing feature is the *SCN2A* variant plus its functional direction and the SCB-response pattern.

**Screening:** No population newborn screening. **Cascade testing** of parents (for recurrence risk and mosaicism) and reproductive counseling (prenatal/PGT for a known familial variant, chiefly relevant to mosaic parents) apply.

Sources: [Efficacy of sodium channel blockers, PMID 27876397](https://pubmed.ncbi.nlm.nih.gov/27876397/), [EEG insights medRxiv](https://www.medrxiv.org/content/10.1101/2023.10.24.23296360.full.pdf).

---

## 11. Outcome / Prognosis

- **Survival / mortality:** No single reliable survival figure; life expectancy is reduced in severe DEE, with risk of **SUDEP (sudden unexpected death in epilepsy)**, status epilepticus, and complications of profound disability (aspiration, respiratory infection). Milder LoF/ASD-ID phenotypes have near-normal life expectancy.
- **Morbidity / disability:** Severe DEE → profound intellectual disability, non-verbal status, motor impairment, need for gastrostomy and full-time care. This is the dominant burden.
- **Disease course:** ~**50% achieve seizure freedom in childhood**; the remainder have intractable epilepsy. Developmental/cognitive impairment frequently **persists despite seizure control**.
- **Prognostic factors:**
  - **Age of onset** — earlier onset (neonatal GoF, especially recurrent severe variants like R1882Q) predicts worse developmental outcome.
  - **Functional variant class** — GoF-early tends to be SCB-responsive (better seizure control) but can still carry severe encephalopathy; LoF/late is SCB-resistant.
  - **Specific variant identity** — recurrent hotspots have characteristic severity signatures.
- **Prognostic biomarkers:** No validated molecular biomarker; **variant function** (GoF/LoF from electrophysiology or in-silico prediction) is the best available prognostic/therapeutic stratifier; EEG features under investigation.

Sources: [Wolff et al. 2017](https://academic.oup.com/brain/article/140/5/1316/3098477), [OMIM #613721](https://omim.org/entry/613721).

---

## 12. Treatment

Treatment is **genotype/function-directed** — the single most important precision-medicine lesson in the whole disorder. It's the closest thing in epilepsy to reading the thermostat before you touch the dial.

**Pharmacotherapy — the GoF/LoF split:**

- **GoF (early-onset, <3 months):** **Sodium-channel blockers (SCBs) are first-line and often effective.** Agents: **phenytoin**, **carbamazepine**, **oxcarbazepine**, **lacosamide**, **lamotrigine**, **zonisamide**. Documented dramatic responses to IV phenytoin loading in refractory neonatal cases.
  > "Patients with the early seizure onset respond better to antiepileptic drugs that non-selectively block sodium channel function, such as phenytoin." (**Wong et al. 2016, PMID 27876397** — *verify exact quote on fetch*)

  MAXO/agents: `treatment_term` NCIT:C15986 Pharmacotherapy; `therapeutic_agent` CHEBI — phenytoin (**CHEBI:8107**), carbamazepine (**CHEBI:3387**), lamotrigine (**CHEBI:6367**), oxcarbazepine (**CHEBI:7822**), lacosamide (**CHEBI:31771** — verify), zonisamide (**CHEBI:10127** — verify). `therapeutic_modality: SMALL_MOLECULE`.

- **LoF (late-onset >3 months, and ASD/ID):** **SCBs are ineffective or can worsen seizures** — avoid as monotherapy. Use broad-spectrum agents: **levetiracetam**, **valproate**, **benzodiazepines**, **topiramate**; and consider **ketogenic diet** (MAXO:0000088 dietary intervention / NCIT ketogenic diet term). Response is generally poorer than in the GoF group.

**Precision / disease-modifying therapies (the frontier):**

- **Antisense oligonucleotides (ASOs) — GoF-directed.** **Elsunersen (PRAX-222)**, an intrathecally-administered ASO designed to **selectively lower *SCN2A* expression** in GoF patients, is the flagship program (Praxis Precision Medicines). In the **EMBRAVE** Phase 1/2 study, early data showed a **44% median seizure reduction after three monthly intrathecal doses**; topline results were slated for the first half of 2026. Regulatory status: **FDA Breakthrough Therapy Designation** (June 2026), **Orphan Drug**, **Rare Pediatric Disease** designations, plus EMA **Orphan/PRIME**. Registrational trial **NCT07019922** (recruiting); earlier **NCT05737784**. `therapeutic_modality: ANTISENSE_OLIGONUCLEOTIDE`; `aso_mechanism: RNASE_H_KNOCKDOWN`; `target_gene: SCN2A (hgnc:10588)`. This maps to the dismech **`antisense_oligonucleotide_therapy#Pathogenic mRNA Accumulation`** conformance target (RNase-H knockdown paradigm). A published case reports ASO treatment in a preterm infant with early-onset SCN2A-DEE (**PMC12283366 / PMC12854296**-adjacent — verify).

- **Upregulation strategies — LoF-directed (preclinical).** Because LoF needs *more* Na_V1.2, ASO knockdown is exactly wrong; instead, **CRISPR-activation (CRISPRa)** and **cis-regulation gene therapy** to *increase* endogenous *Scn2a* expression have rescued neural excitability and behavioral phenotypes in *Scn2a⁺/⁻* mice (SFARI 2025; ScienceDirect S266732582300033X). Still preclinical.

**Supportive / rehabilitative:** developmental therapies — **physical therapy (MAXO:0000011)**, **occupational therapy**, **speech therapy**, feeding/nutrition support (gastrostomy where needed, MAXO supportive care `MAXO:0000950`), and management of comorbid autism/behavior. **Genetic counseling (MAXO:0000079)** for the family.

**Pharmacogenomics:** The operative "pharmacogenomic" axis here is the *SCN2A variant's own functional class* dictating SCB response — not classic CYP-based metabolism (though standard phenytoin/carbamazepine PGx — e.g., HLA-B*15:02 for carbamazepine SJS risk — still applies to those drugs).

**Treatment strategy:** Confirm variant → determine GoF vs LoF (functional data or informed prediction) → **GoF: SCB first-line**; **LoF: avoid SCBs, use broad-spectrum ± ketogenic diet** → escalate to precision ASO (GoF) as trials mature.

Sources: [Praxis FDA Breakthrough release](https://www.globenewswire.com/news-release/2026/06/22/3315249/0/en/Praxis-Precision-Medicines-Receives-FDA-Breakthrough-Therapy-Designation-for-Elsunersen.html), [NCT07019922](https://clinicaltrials.gov/study/NCT07019922), [NCT05737784](https://clinicaltrials.gov/study/NCT05737784), [Wong et al. PMID 27876397](https://pubmed.ncbi.nlm.nih.gov/27876397/), [SFARI cis-regulation rescue](https://www.sfari.org/2025/11/19/cis-regulation-therapy-rescues-scn2a-related-neurological-dysfunction/).

---

## 13. Prevention

- **Primary prevention:** None possible for a de novo dominant disorder — you can't prevent a new mutation. No vaccine, no modifiable risk factor.
- **Secondary prevention / early detection:** **Rapid genetic diagnosis** in a neonate/infant with unexplained seizures is the actionable lever — it enables **function-directed treatment** early, potentially reducing seizure burden and (hoped, unproven) improving developmental trajectory. This is prevention of *complications*, not of disease occurrence.
- **Tertiary prevention:** Optimizing seizure control (correct drug class), SUDEP-risk mitigation, managing feeding/respiratory complications, and developmental support to maximize function.
- **Genetic counseling & reproductive options:** For families with an affected child, counseling covers the **low-but-nonzero sibling recurrence risk** from parental mosaicism; **prenatal diagnosis / preimplantation genetic testing** are options when a familial (mosaic) variant is known. MAXO:0000079 genetic counseling.
- **Public health / behavioral / immunization:** Not applicable.

Sources: [FamilieSCN2A clinical info](https://www.scn2a.org/scn2a-related-disorders/clinical-information/).

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *SCN2A* is conserved across mammals. Mouse ortholog ***Scn2a*** (NCBI Gene 110876; MGI); rat *Scn2a*; conserved across vertebrates. **NCBITaxon:10090** (*Mus musculus*), **NCBITaxon:10116** (*Rattus norvegicus*).
- **Natural disease in other species:** No well-characterized naturally-occurring *SCN2A* channelopathy is established in companion animals or wildlife analogous to the human disorder — the animal knowledge base here is dominated by **engineered models**, not natural disease (check **OMIA** for any spontaneous variants). This section is largely **not applicable** beyond experimental models.
- **Comparative biology:** The developmental expression switch (Na_V1.2 dominant in immature excitatory neurons, partly ceded to Na_V1.6/*SCN8A* with maturation) is conserved rodent↔human, which is *why* mouse models are informative. **Evolutionary conservation** of the four-domain sodium-channel architecture is deep (across the *SCN* gene family).
- **Zoonosis / transmission:** Not applicable — genetic disorder, not transmissible.

Sources: [Scn2a rodent model review, PMC11601800](https://pmc.ncbi.nlm.nih.gov/articles/PMC11601800/).

---

## 15. Model Organisms

**Mouse is the workhorse** and the models split neatly along the human GoF/LoF axis:

- **LoF / haploinsufficiency model — *Scn2a⁺/⁻* (heterozygous knockout):** Viable and fertile. Recapitulates the **autism/ID + late-seizure** end: reduced excitability of immature neurons but hyperexcitable mature neurons; impaired hippocampal excitability, excitatory synaptic drive, LTP, and spatial learning/memory (**PMC6582764**); anxiety, sociability, memory-flexibility, and hyperactivity phenotypes, with **ampakine CX516 rescuing hyperactivity** (**PMC6437867**). Spratt et al. (Neuron 2019) established the dendritic-excitability mechanism. **Applications:** modeling the ASD/ID arm and testing **expression-*restoring*** therapies (CRISPRa, cis-regulation, AAV-*Scn2a* gene therapy — SFARI 2025).
- **GoF models:** knock-in of specific human GoF variants recapitulate early-onset seizures/hyperexcitability and are the substrate for testing **expression-*lowering*** ASOs (gapmer ASOs reduce seizures in GoF-modeling mice — the preclinical basis for elsunersen; bioRxiv 2020.09.09.289900).
- **Conditional / cell-type-specific models:** Cre-based conditional knockouts dissect excitatory-neuron-specific contributions and developmental timing.
- **In vitro / cellular:** **Patient iPSC-derived neurons** distinguish GoF vs LoF functionally in a human background (J Neurosci 2024); **heterologous expression** (HEK/*Xenopus*) for patch-clamp biophysics; **dynamic action-potential clamp** for functional prediction.

**Phenotype recapitulation & limitations:** Mouse models reproduce the core electrophysiology and many behaviors, and their GoF/LoF dichotomy mirrors humans well — a genuine strength. **Limitations:** rodents don't capture human-specific cortical development, the full cognitive/language phenotype, or the precise developmental timing of the Na_V1.2→Na_V1.6 handoff; strain background modifies severity; and behavioral autism analogs are imperfect proxies. For dismech curation, tag mouse/iPSC evidence as **MODEL_ORGANISM / IN_VITRO** respectively — keep it distinct from human-clinical support for human phenotypes.

**Resources:** MGI (mouse *Scn2a*), IMPC/KOMP (knockout alleles), Cellosaurus (iPSC lines), and the FamilieSCN2A-supported model repositories.

Sources: [Scn2a rodent model review PMC11601800](https://pmc.ncbi.nlm.nih.gov/articles/PMC11601800/), [Scn2a+/− behavior/CX516, PMC6437867](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6437867/), [Hippocampal Scn2a haploinsufficiency, PMC6582764](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6582764/), [gene-therapy review](https://www.sciencedirect.com/science/article/pii/S266732582300033X).

---

## Curation-ready summary (dismech hooks)

- **Module conformance:** Primary → **`epilepsy_excitation_inhibition_imbalance`** (GoF arm; `#Excitation-Inhibition Imbalance`). Treatment → **`antisense_oligonucleotide_therapy`** (`#Pathogenic mRNA Accumulation`, RNase-H knockdown, elsunersen). Consider a **`cardiac_ion_channel_repolarization`**-style channelopathy framing conceptually, but epilepsy module is the correct fit.
- **Key genes/terms:** `SCN2A` (`hgnc:10588`), Na_V1.2 (UniProt Q99250); GO:0005248, GO:0043194, GO:0019228; CL:0000598 pyramidal neuron; UBERON:0000956 cerebral cortex.
- **Anchor PMIDs (verify snippets before YAML):** **28379373** (Wolff 2017 Brain — genotype/phenotype + therapeutic implications); **30301539** (Sanders 2018 Trends Neurosci — GoF/LoF framework); **27876397** (Wong 2016 — SCB efficacy in early-onset); Spratt 2019 Neuron (haploinsufficiency mechanism — confirm PMID); iPSC J Neurosci 2024 (44(8):e0692232023).
- **Genotype-directed therapy is the headline** — curate the GoF→SCB-responsive vs LoF→SCB-resistant split explicitly, with separate evidence for each direction, and the ASO (GoF-lowering) vs upregulation (LoF-raising) therapeutic mirror-image.

**The one-line mental model to carry into curation:** *same gene, two opposite failures of one sodium channel — jammed-open (GoF) burns early with seizures and answers to sodium-channel blockers; jammed-shut (LoF) starves developing circuits into autism/ID and shrugs those same drugs off — and the whole treatment strategy, down to whether you add or subtract the gene's own message, hinges on which way it broke.*

One caveat worth repeating for the record: several 2026-dated regulatory items (elsunersen Breakthrough designation, EMBRAVE topline) come straight from company press releases and trial registries — solid for the treatment-pipeline narrative, but they're not peer-reviewed literature, so cite them as `evidence_source: OTHER` (or the trial's `clinicaltrials:` reference) rather than dressing them up as clinical-trial primary evidence.