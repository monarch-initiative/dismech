---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8
cached: false
start_time: '2026-07-22T12:17:12.662420'
end_time: '2026-07-22T12:22:42.140356'
duration_seconds: 329.48
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: GRIN2B-Related Developmental and Epileptic Encephalopathy
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-4-8
  web_search_requests: 9
  num_turns: 14
  total_cost_usd: 1.8242624999999997
  session_id: df9c804d-2979-47b9-bc3d-e96f79d7c869
  stop_reason: end_turn
citation_count: 17
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** GRIN2B-Related Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **GRIN2B-Related Developmental and Epileptic Encephalopathy** covering all of the
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

sup Harry — dug through GeneReviews, the OMIM entries, the big Platzer cohort paper, the Frontiers mechanism review, and the recent treatment trials. Here's the whole picture on GRIN2B, laid out to drop straight into a dismech entry. Think of GRIN2B like the volume knob on a synapse's calcium channel that's supposed to get *swapped out* as the brain matures — when it's broken, either the knob is missing or it's welded wide open, and both wreck development in their own way.

---

# GRIN2B-Related Developmental and Epileptic Encephalopathy — Research Report

## 1. Disease Information

**What it is.** GRIN2B-related neurodevelopmental disorder is a single-gene, autosomal-dominant condition caused by heterozygous *de novo* variants in *GRIN2B*, which encodes the GluN2B (NR2B) subunit of the N-methyl-D-aspartate (NMDA) glutamate receptor. Every affected person has developmental delay/intellectual disability (DD/ID); on top of that, a big chunk have epilepsy, autism/behavioral issues, muscle-tone problems, and movement disorders. The "developmental and epileptic encephalopathy" (DEE) framing captures the more severe end — early-onset drug-resistant seizures layered on top of (and worsening) the developmental impairment — but the disorder is really one continuous spectrum from mild ID-without-seizures all the way to catastrophic epileptic encephalopathy.

**Key identifiers.**
- **Gene:** *GRIN2B* — OMIM `*138252`; HGNC:4586 (`hgnc:4586`); chromosome 12p13.1; NCBI Gene 2904.
- **Disease (severe/epileptic end):** Developmental and Epileptic Encephalopathy 27 (DEE27) — OMIM `#616139`; **MONDO:0014505**.
- **Disease (milder end):** Autosomal Dominant Intellectual Developmental Disorder 6 (MRD6, formerly "mental retardation, autosomal dominant 6") — OMIM `#613970`; MONDO:0013655.
- **Orphanet:** GRIN2B is the gene for several ORPHA entries; the broad umbrella "non-specific/syndromic intellectual disability" and "GRIN2B-related" concepts apply. (Worth pulling the exact ORPHA leaf via `just structured-rebuild-orphanet` during curation.)
- **ICD-11:** most naturally 8A61-region DEE / 6A00 disorders of intellectual development, coded by phenotype; there's no GRIN2B-specific ICD code.
- **MeSH:** no gene-specific descriptor; indexed under "Epileptic Syndromes," "Intellectual Disability," "Receptors, N-Methyl-D-Aspartate."

**Data provenance.** Information is a mix of **disease-level aggregated resources** (GeneReviews, OMIM, Orphanet) built from **individual patient case series** — the field's backbone is aggregated cohorts of *de novo* variant carriers (Endele 2010, Lemke 2014, Platzer 2017) plus functional studies. Fewer than a couple hundred individuals are described in detail; a lot of the frequency numbers come from the 61-person clinically-characterized subset in GeneReviews and the 91-person Platzer cohort.

**Synonyms / alternative names:** GRIN2B encephalopathy; GRIN2B-related neurodevelopmental disorder; NMDA-receptor GluN2B/NR2B-related disorder; intellectual disability, autosomal dominant 6; DEE27; part of the broader "GRIN disorders" / "GRIN-related disorders" family (with GRIN1, GRIN2A, GRIN2D).

---

## 2. Etiology

**Primary cause — genetic, monogenic.** Heterozygous pathogenic variants in *GRIN2B*, essentially always **de novo** (arising fresh in the affected child, not inherited). GeneReviews reports that all probands with parental testing had de novo variants; there is **no known environmental or infectious cause**. This is a dominant, high-penetrance Mendelian disorder — the variant *is* the disease.

**Genetic risk factors.**
- The causal lesion itself: a pathogenic *GRIN2B* variant (see §4).
- *GRIN2B* is one of the most mutation-intolerant genes in the genome, which is *why* de novo hits there are so consequential: **pLI = 1.00, LOEUF = 0.06 (extreme loss-of-function intolerance), missense Z-score = 5.42** in gnomAD ([gnomAD constraint](https://gnomad.broadinstitute.org/gene/ENSG00000273079)). Essentially no loss-of-function variants are seen in the healthy population, so any real LoF hit is high-impact.
- **Advanced paternal age** is the generic risk factor for de novo mutations broadly, but it has not been specifically quantified for *GRIN2B*.

**Protective factors.** None established. There are no known protective alleles or modifier variants that rescue the phenotype, and no lifestyle/dietary protective factors (this isn't a multifactorial disease). *L-serine and NMDA antagonists are treatments, not prevention* (see §12).

**Gene–environment interactions.** Not a meaningful axis for this disorder — it's driven by the germline (or post-zygotic mosaic) variant. The one "environmental" modulator worth noting mechanistically is **activity-dependent regulation of the GluN2B→GluN2A developmental switch**: synaptic activity normally times the swap of GluN2B for GluN2A during the third postnatal week (rodent), so the developmental window itself is a biological context that shapes when/how the variant bites (Frontiers review, [PMC9873235](https://pmc.ncbi.nlm.nih.gov/articles/PMC9873235/)).

---

## 3. Phenotypes

Frequencies below are from the GeneReviews clinically-characterized cohort (n≈61 unless noted; [Platzer & Myers, GeneReviews, PMID:29851452](https://www.ncbi.nlm.nih.gov/books/NBK501979/)). Onset is infantile-to-early-childhood for essentially all features.

| Phenotype | Frequency | HPO suggestion | Notes |
|---|---|---|---|
| Developmental delay / intellectual disability | **100%** (mild 15% / moderate 24% / severe-profound 61%) | HP:0001263 (Global developmental delay) / HP:0001249 (Intellectual disability) | Defining feature; severity variable |
| Hypotonia | **56%** (34/61); ~15% need tube feeding | HP:0001252 (Hypotonia); feeding: HP:0011968 (Feeding difficulties) | |
| Epilepsy / seizures | **51%** (31/61) | HP:0001250 (Seizure) | See breakdown below |
| Autism spectrum disorder / behavioral issues | **26%** (16/61) | HP:0000717 (Autism); HP:0000708 (Behavioral abnormality) | |
| Spasticity | **23%** (14/61) | HP:0001257 (Spasticity) | |
| Microcephaly | **18%** (11/61) | HP:0000252 (Microcephaly) | |
| Movement disorder (dystonic/dyskinetic/choreiform) | **10%** (6/61) | HP:0001300 (Parkinsonism)? no — use HP:0001332 (Dystonia), HP:0002072 (Chorea), HP:0100022 (Abnormal movement) | |
| Cortical visual impairment | **8%** (5/61) | HP:0100704 (Cerebral visual impairment) | |
| Developmental regression | **7%** (4/61) | HP:0002376 (Developmental regression) | |
| Malformation of cortical development (MRI) | **13%** (6/47) | HP:0002536 (Abnormal cortical gyration) / HP:0007younger — use HP:0002119 (Ventriculomegaly)? better HP:0032046 (Abnormal cerebral cortex morphology) | Polymicrogyria, cortical dysplasia |
| Cerebral atrophy (MRI) | **9%** (4/47) | HP:0002059 (Cerebral atrophy) | |

**Speech and motor milestones.** Delayed speech and motor development is near-universal; some individuals **never develop speech or independent walking**. Suggest HP:0000750 (Delayed speech and language development), HP:0002540 (Inability to walk).

**Epilepsy sub-phenotyping** (within the 31 with epilepsy):
- Generalized seizures: **58%** (18/31) — HP:0002197 (Generalized-onset seizure)
- Focal seizures: **48%** (15/31) — HP:0007359 (Focal-onset seizure)
- Epileptic (infantile) spasms: **35%** (11/31), most meeting **West syndrome** criteria — HP:0012469 (Infantile spasms)
- Onset: birth to age 9 years; ~**50% drug-resistant** — HP:0011171 (Refractory epilepsy)

**Additional/associated features reported:** strabismus, cortical visual impairment, feeding difficulties, hyperkinesis/ADHD-like features, stereotypies, and occasionally hyperphagia/obesity in some series.

**Quality-of-life impact.** No GRIN2B-specific EQ-5D/SF-36 data. Impact is dominated by the severe-profound ID majority (61%): most affected individuals need lifelong assistance with daily living, communication supports, and — where epilepsy is refractory — carry the additional QoL burden of drug-resistant seizures and their treatment side effects. Non-verbal, non-ambulatory individuals at the profound end represent the highest care-dependency group.

---

## 4. Genetic / Molecular Information

**Causal gene.** *GRIN2B* (OMIM `*138252`; HGNC:4586; 12p13.1). Encodes GluN2B/NR2B, a regulatory subunit of the heterotetrameric NMDA receptor (two obligate GluN1 + two GluN2/GluN3 subunits).

**Variant landscape.**
- **Missense** is the dominant class (~65% of disease-associated GRIN variants overall), typically clustering in functionally critical domains and associated with the **more severe** end. Platzer 2017 found missense variants significantly enriched for severe ID (**p = 0.0079**, Fisher's exact; [PMID:28377535](https://pubmed.ncbi.nlm.nih.gov/28377535/)).
- **Protein-truncating variants** (nonsense, frameshift, splice-site) and whole/partial-gene deletions — "null alleles" — trend toward **milder-to-moderate ID** and are less often associated with severe epilepsy.
- **Structural:** the original Endele 2010 report found *GRIN2B* disrupted by **chromosomal translocation breakpoints** in ID/epilepsy patients ([PMID:20890276](https://pubmed.ncbi.nlm.nih.gov/20890276/)).
- **Detection:** GeneReviews — sequence analysis picks up ~95% (82/86), deletion/dup or CMA the remaining ~5% (4/86).

**Landmark variant examples:**
- **N615I and V618G** — de novo missense in the **M2 re-entrant pore loop**; *increase Ca²⁺ permeability and reduce Mg²⁺ block → gain of function*; West syndrome/severe DD (Lemke 2014, [PMID:24272827](https://pubmed.ncbi.nlm.nih.gov/24272827/)).
- **E413G, C461F** (ligand-binding domain) — reduced surface expression / trafficking defects → loss of function.
- **G689C, G689S** — ~**1,000–2,000-fold lower glutamate EC50** (bizarrely, a *loss*-type consequence via non-functional NMDARs at synapses despite altered agonist potency).
- **C456Y** — modeled as a knock-in mouse (see §15).

**Variant classification.** Under ACMG/AMP, established recurrent de novo missense in constrained domains are typically **Pathogenic/Likely Pathogenic** (PS2 de novo, PM1 mutational hotspot, PM2 absent from gnomAD, PP3 in silico). Given GRIN2B's extreme constraint, novel LoF variants readily reach LP/P; missense VUS require functional data to resolve. Curate against **ClinVar** and **ClinGen** (`CGGV:` gene-disease validity and `CGDS:` dosage) records during entry-building.

**Allele frequency.** Pathogenic variants are **absent from population databases** (gnomAD) — consistent with de novo origin and pLI 1.00 / LOEUF 0.06 constraint.

**Somatic vs germline.** Germline de novo is the rule; **post-zygotic/parental mosaicism** is documented and underlies the ~1% empiric recurrence risk quoted to families.

**Functional consequence — the key duality.** Variants split into **gain-of-function (GoF)** (↑Ca²⁺ flux, ↓Mg²⁺ block, ↑agonist potency, slowed deactivation) versus **loss-of-function (LoF)** (trafficking failure, non-functional channels, haploinsufficiency). Some truncating/translocation variants act **dominant-negative** by co-assembling mutant with wild-type subunits into hybrid receptors (Freunscht et al.; Frontiers review [PMC9873235](https://pmc.ncbi.nlm.nih.gov/articles/PMC9873235/)). **This GoF/LoF distinction is the single most therapeutically important fact about the disorder** (see §12).

**Modifier genes / epigenetics / chromosomal abnormalities.** No established modifier genes. An open hypothesis is compensatory **GluN2A** upregulation modulating severity. No disorder-specific epigenetic signature is established (unlike some ID genes, GRIN2B lacks a validated DNA-methylation "episignature" to date). Large 12p13.1 deletions/translocations disrupting GRIN2B are the relevant chromosomal lesions.

---

## 5. Environmental Information

**Not applicable / minimal.** This is a de novo monogenic disorder with no established environmental, lifestyle, toxic, or infectious contributors. There are no dietary, occupational, or exposure risk factors. (The only "environmental" levers are therapeutic — dietary L-serine supplementation and NMDA-antagonist drugs — covered under Treatment.) Curate §5 as **not applicable** for causation.

---

## 6. Mechanism / Pathophysiology

**Normal biology.** GluN2B is the developmentally dominant GluN2 subunit: in rodent cortex/hippocampus, most NMDARs contain GluN2B early postnatally (peaking ~3rd postnatal week), then a "**2A/2B switch**" gradually replaces it with GluN2A as circuits mature. GluN2B-containing NMDARs mediate the slow, high-Ca²⁺ component of glutamatergic transmission critical for **neuronal differentiation, dendritogenesis, synaptogenesis, circuit refinement, and synaptic plasticity (LTP/LTD)**. Domains: extracellular **amino-terminal domain (ATD)**, **ligand-binding domain (LBD, S1/S2)** binding glutamate, four membrane segments **M1–M4** (M2 = re-entrant pore loop lining the Ca²⁺-conducting channel), and a long **intracellular C-terminal domain** for trafficking/signaling scaffolds (PSD-95, CaMKII).

**Causal chain — two convergent arms:**

**Arm A — Gain of function (pore/linker variants, e.g., N615I, V618G):**
1. Missense in M2 re-entrant loop / M2–M3 linker → **↓ Mg²⁺ block + ↑ Ca²⁺ permeability**, and/or slowed channel deactivation.
2. → **excess Ca²⁺ influx and NMDAR-mediated excitation** at rest/subthreshold.
3. → **neuronal hyperexcitability**, excitotoxic stress, disrupted excitation/inhibition balance.
4. → **early-onset seizures / West syndrome + severe DD** (upstream = channel biophysics; downstream = network hyperexcitability and developmental encephalopathy).
- GO: GO:0004972 (NMDA glutamate receptor activity), GO:0005262/GO:0070588 (calcium ion transmembrane transport), GO:0051966 (regulation of synaptic transmission, glutamatergic), GO:0060079 (excitatory postsynaptic potential).

**Arm B — Loss of function / haploinsufficiency (trafficking & LBD variants, truncations):**
1. Variant → **impaired surface trafficking / non-functional channels / reduced dendritic targeting** (e.g., E413G, C461F, S2-loop truncations not reaching the membrane).
2. → **reduced NMDAR-mediated Ca²⁺ signaling** during the critical developmental window.
3. → **suppressed neural-progenitor→neuron differentiation** (iPSC data), **impaired dendrite length/branching** (724t truncation — reduced elongation, increased pruning), **fewer functional synaptic NMDARs**.
4. → **cortical malformation** (in ~13%), impaired circuit formation, DD/ID (often with less severe or no epilepsy).
- GO: GO:0021954/GO:0022008 (CNS neuron differentiation/neurogenesis), GO:0016358 (dendrite development), GO:0050808 (synapse organization), GO:0060291 (long-term synaptic potentiation), GO:0016311/plasticity terms.

**Convergent downstream:** both arms funnel into **abnormal synaptic plasticity** (impaired LTP/LTD — the C456Y knock-in mouse shows selectively impaired NMDAR-dependent LTD with intact synapse density) and **disrupted cortical circuit assembly**, producing the shared DD/ID core.

**Protein dysfunction.** Misassembly/trafficking failure (LoF) vs biophysical channel gain (GoF); **dominant-negative** poisoning of wild-type receptors via hybrid tetramers for some truncations. UniProt Q13224 (GRIN2B_HUMAN); structural context from cryo-EM NMDAR structures (PDB e.g. 4PE5, 5FXG-class).

**Cell types & anatomy involved:** glutamatergic (excitatory) **cortical pyramidal neurons** (CL:0000598 pyramidal neuron / CL:0000679 glutamatergic neuron), **hippocampal neurons**, and broadly CNS neurons; subcellularly the **postsynaptic density / dendritic spine** (GO:0014069 postsynaptic density, GO:0043197 dendritic spine, GO:0098794 postsynapse), **plasma membrane** (GO:0005886), and ER trafficking machinery.

**Molecular profiling.** iPSC-derived neuron models (single-cell/functional genomics) show the differentiation and dendrite deficits above; no large-scale disease-specific transcriptomic/proteomic/metabolomic signature is established. Immune involvement: none (this is not an autoimmune/inflammatory encephalopathy — important to distinguish from anti-NMDAR *autoimmune* encephalitis, which is mechanistically unrelated despite the shared receptor).

---

## 7. Anatomical Structures Affected

- **Primary organ/system:** brain / central nervous system — **cerebral cortex** (UBERON:0000956), **hippocampus** (UBERON:0002421), **basal ganglia** (UBERON:0002420, enlarged/dysplastic in some), **corpus callosum** (UBERON:0002336, hypoplastic in some). Body system: **nervous system** (UBERON:0001016).
- **Secondary/complications:** musculoskeletal (tone abnormalities, contractures secondary to spasticity), GI (feeding difficulty/tube dependence), visual pathway (cortical visual impairment — the defect is cortical, not ocular).
- **Tissue/cell level:** **nervous tissue**; excitatory glutamatergic neurons — pyramidal neurons (CL:0000598), glutamatergic neurons (CL:0000679); cortical neuron populations. Cortical malformations (polymicrogyria, cortical dysplasia, hippocampal dysplasia) reflect disrupted neuronal migration/organization.
- **Subcellular:** postsynaptic density and dendritic spines of excitatory synapses (GO:0014069, GO:0043197); plasma membrane channel; dendritic arbor.
- **Localization/lateralization:** bilateral, generally diffuse CNS involvement; cortical malformations may be diffuse or focal/regional; **microcephaly** is a whole-brain volumetric sign.

---

## 8. Temporal Development

- **Onset:** congenital-to-infantile. DD is apparent in infancy/early childhood; **epilepsy onset ranges birth to ~9 years** (many in infancy, esp. West syndrome/spasms). Pattern is typically **insidious/chronic-developmental** rather than acute — though seizure onset can be abrupt, and DEE27 notes development can be "normal prior to seizure onset, after which cognitive/motor delays become apparent" in the epilepsy-driven subset.
- **Progression:** predominantly a **static (non-degenerative) encephalopathy** — the underlying lesion is developmental, and most individuals do not neurodegenerate. **Developmental regression is uncommon (~7%)**, often peri-seizure-onset. Disability is **lifelong/chronic**.
- **Course pattern:** stable-with-developmental-plateau for the core ID; epilepsy course varies (some refractory/persistent, some more controlled; ~50% drug-resistant).
- **Critical periods:** the **GluN2B→GluN2A developmental switch window** (early postnatal, activity-dependent) is the mechanistically critical window — and, hopefully, the therapeutic window; the C456Y mouse work suggests **early correction of the LTD defect improves later behavior**, hinting at an early-intervention opportunity.
- **Remission:** no spontaneous remission of ID; seizure remission is treatment-dependent and variable.

---

## 9. Inheritance and Population

- **Inheritance pattern:** **autosomal dominant** (HP:0000006), essentially always **de novo**. Penetrance reported as **100%** in GeneReviews. Expressivity is **highly variable** (mild ID → profound encephalopathy), correlated partly with variant class (null vs missense) and GoF/LoF mechanism.
- **Recurrence risk:** ~**1%** empiric (accounting for possible parental germline/somatic mosaicism); documented mosaicism cases exist.
- **Genetic anticipation:** not applicable (not a repeat-expansion disorder).
- **Founder effects / consanguinity / carrier frequency:** not applicable — de novo dominant, so no founder alleles, no consanguinity role, and no meaningful carrier frequency (pathogenic alleles absent from gnomAD).
- **Epidemiology:** exact prevalence **unknown**; a rare disease. GRIN2B variants account for **~0.2%** of neurodevelopmental disorder / childhood-onset epilepsy cohorts; **fewer than ~100–200** well-characterized individuals published. For a `Prevalence` record, this is best coded qualitatively (`RARE`/`ULTRA_RARE`, or Orphanet `NOT_YET_DOCUMENTED`) rather than a fabricated rate.
- **Sex ratio:** no strong sex bias established (autosomal); roughly equal.
- **Geographic/ethnic distribution:** worldwide, pan-ethnic; no population clustering (consistent with de novo origin).

---

## 10. Diagnostics

- **Genetic testing (definitive).** Diagnosis rests on identifying a heterozygous pathogenic *GRIN2B* variant or deletion:
  - **Exome (WES) or genome (WGS) sequencing** — highest yield in undiagnosed DD/ID/epilepsy; the usual route to a GRIN2B diagnosis.
  - **Multigene epilepsy/ID/DEE panels** including GRIN2B (and GRIN1/GRIN2A/GRIN2D).
  - **Single-gene sequencing** if GRIN2B specifically suspected.
  - **Chromosomal microarray (CMA)** / gene-targeted del-dup for the ~5% caught by copy-number/structural lesions (12p13.1 deletions, translocations).
  - GeneReviews detection split: sequencing ~95%, del/dup or CMA ~5%.
  - **Trio testing** (parents + proband) is key to establishing de novo status → strengthens ACMG PS2 and pathogenicity call.
- **Functional confirmation.** For missense VUS, **electrophysiology in heterologous systems** (measuring Ca²⁺ permeability, Mg²⁺ block, agonist EC50, surface expression) determines **GoF vs LoF** — increasingly clinically actionable because it steers therapy.
- **Supportive/phenotyping studies (not diagnostic on their own):**
  - **EEG** — characterize seizures; **hypsarrhythmia** in West syndrome; interictal epileptiform discharges (LOINC-codeable neurophysiology).
  - **Brain MRI** — screen for malformation of cortical development (polymicrogyria, cortical dysplasia), corpus callosum hypoplasia, basal ganglia/hippocampal dysplasia, cerebral atrophy.
  - Developmental/cognitive assessment; ophthalmology for cortical visual impairment.
- **No routine biochemical biomarker** — there's no blood/CSF metabolite or enzyme assay for GRIN2B disorder (differentiate sharply from anti-NMDAR *autoimmune* encephalitis, which **does** have CSF autoantibodies — a critical differential when acute).
- **Differential diagnosis:** other GRIN disorders (GRIN1/GRIN2A/GRIN2D), other DEE genes (STXBP1, SCN2A, CDKL5, KCNQ2, etc.), Rett/Rett-like, Angelman, other cortical-malformation and ID syndromes. Distinguish by gene, EEG pattern, MRI, and (acutely) from autoimmune NMDAR encephalitis.
- **Screening.** No population/newborn screening (rare, de novo). Relevant genetic-counseling screening is **cascade/recurrence-risk assessment** for future pregnancies, given mosaicism risk.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** GRIN2B disorder is **not primarily life-limiting**; there's no established reduced life expectancy for the disorder as a whole. Mortality risk, where present, tracks the severe end — refractory epilepsy (with attendant SUDEP risk), aspiration/feeding complications, and immobility-related morbidity in profoundly affected, non-ambulatory individuals. No disorder-specific survival statistics are published.
- **Morbidity/function:** dominated by **lifelong intellectual disability** (profound in the majority) with communication and mobility impairment; many are non-verbal and/or non-ambulatory. Spasticity, dystonia, feeding difficulty, and cortical visual impairment add functional burden.
- **Prognostic factors:** **variant class and functional mechanism** are the strongest — missense (esp. in pore/LBD/M3) → more severe ID (p=0.0079); null/truncating → milder-moderate ID. **Refractory epilepsy** (~50%) and **cortical malformation** predict worse developmental outcome. GoF pore variants → severe early epilepsy/West syndrome.
- **Recovery potential:** the core ID is static, not reversible; realistic goals are developmental gains with therapy and seizure control. The mouse "early-correction" data raise cautious hope that mechanism-matched drugs started early could improve trajectory — unproven in humans.
- **QoL measures:** no GRIN2B-specific validated instruments; caregiver-burden and non-verbal QoL tools apply.

---

## 12. Treatment

**The organizing principle: match the drug to the mechanism (GoF vs LoF).** There are **no FDA-approved GRIN2B-specific therapies yet**; care is supportive plus mechanism-guided off-label/trial agents.

**Mechanism-matched pharmacotherapy (the big story):**
- **Gain-of-function variants → NMDA-receptor antagonism.**
  - **Memantine** (uncompetitive NMDAR channel blocker; CHEBI:64312). A 2026 Epilepsia multi-patient study (Karnstedt et al., [PMID:41489401](https://pubmed.ncbi.nlm.nih.gov/41489401/)) reported improvements in behavior, development, and seizure frequency in individuals with GRIN GoF variants; earlier single-case reports (Pierson et al. 2014, in GRIN2A GoF) documented seizure reduction. MAXO: pharmacotherapy (`MAXO:0000058` treatment / `NCIT:C15986` Pharmacotherapy for the KB pattern; therapeutic_agent CHEBI memantine).
  - **Radiprodil** — a **GluN2B-selective negative allosteric modulator**; the Phase 1b **HONEYCOMB** study (industry, GRIN2B/GRIN GoF) reported significant seizure-frequency reduction ([NeurologyLive coverage](https://www.neurologylive.com/view/radiprodil-significantly-reduces-seizure-frequency-phase-1b-honeycomb-study-grin-related-neurodevelopmental-disorder)). This is the most GRIN2B-tailored agent in development.
- **Loss-of-function / null variants → NMDA-receptor potentiation.**
  - **L-serine** (dietary precursor boosting the co-agonist D-serine; CHEBI:17115). A 2022 case series (Soto et al., [PMID:34997442](https://pubmed.ncbi.nlm.nih.gov/34997442/)) found improvements in behavior, EEG, and seizure frequency in GRIN-related disorder due to **null** variants; n-of-1 crossover trial protocols in GRIN2B LoF children are underway ([PMC10746402](https://pmc.ncbi.nlm.nih.gov/articles/PMC10746402/)). MAXO: dietary intervention (`MAXO:0000088`) / supplementation.
  - **Caution:** giving the *wrong* mechanism drug (e.g., an NMDA antagonist to an LoF patient, or L-serine to a GoF patient) is theoretically harmful — hence the push for functional variant classification before treating.

**Anti-seizure management (standard):** conventional ASMs per seizure type; ~50% are drug-resistant. For infantile spasms/West syndrome, standard first-line (ACTH/corticosteroids, vigabatrin) applies; consider mechanism-matched add-on (memantine for GoF). MAXO: pharmacotherapy (`MAXO:0000058`).

**Supportive / rehabilitative (the backbone of care):**
- Physical, occupational, and speech/language therapy — MAXO:0000011 (physical therapy), MAXO physiotherapy/OT/speech terms.
- Management of spasticity/dystonia (e.g., baclofen, botulinum toxin), feeding support (gastrostomy where needed), visual supports for cortical visual impairment, behavioral/ASD interventions.
- Genetic counseling — MAXO:0000079.

**Pharmacogenomics.** The relevant "PGx" here is unusual: it's the **causal variant's own functional class (GoF/LoF)** that dictates drug choice — a genotype-directed, precision-medicine model rather than classic drug-metabolism PGx.

---

## 13. Prevention

- **Primary prevention:** none possible for a de novo dominant disorder — you can't prevent a fresh germline mutation. No vaccine, no modifiable risk factor.
- **Secondary prevention / early detection:** early genetic diagnosis (WES/WGS) in a child with DD/epilepsy → enables mechanism-matched therapy and early developmental intervention (the plausible "critical window" for benefit). Early EEG/MRI to catch and treat West syndrome promptly.
- **Tertiary prevention:** prevent complications — seizure control (SUDEP/injury reduction), aspiration prevention/feeding management, spasticity/contracture prevention via PT, vision and behavioral supports.
- **Reproductive counseling:** for families with an affected child, **genetic counseling** on the ~1% recurrence risk (mosaicism), with options including **prenatal testing** or **preimplantation genetic testing (PGT)** in future pregnancies once the familial variant is known — MAXO:0000079 (genetic counseling).
- **Immunization / public-health / environmental interventions:** not applicable.

---

## 14. Other Species / Natural Disease

- **Orthologs:** *Grin2b* is deeply conserved across vertebrates — mouse (*Grin2b*, NCBI Gene 14812; MGI:95822), rat (*Grin2b*), zebrafish (*grin2b*), and the receptor family extends to invertebrates (*C. elegans nmr-1/nmr-2*, *Drosophila Nmdar2*). Alliance of Genome Resources / HomoloGene document the orthology.
- **Taxonomy:** most relevant experimental species — *Mus musculus* (NCBITaxon:10090), *Rattus norvegicus* (NCBITaxon:10116), *Danio rerio* (NCBITaxon:7955).
- **Natural disease in other species:** no well-characterized spontaneous naturally-occurring *GRIN2B* disorder documented in companion animals (OMIA has no flagship GRIN2B entry comparable to the human disease); the disease knowledge is essentially all human + engineered models.
- **Comparative biology:** the NMDAR GluN2B subunit and the developmental 2B→2A switch are evolutionarily conserved mechanisms, which is exactly why rodent models recapitulate core features — strong evolutionary conservation of the disease-relevant biology.
- **Zoonosis:** not applicable (genetic, non-transmissible).

---

## 15. Model Organisms

- **Mouse — constitutive knockout (`Grin2b−/−`):** **perinatally lethal** — pups fail to suckle (impaired trigeminal/brainstem pattern formation) and die within days; can be kept alive short-term by hand-feeding. Demonstrates GluN2B is essential for neonatal survival and shows **suppressed LTD** and impaired whisker-barrel patterning. **Heterozygous `Grin2b+/−` mice are viable** → useful for studying haploinsufficiency (one WT copy suffices for survival). (Reviewed in [PMC9873235](https://pmc.ncbi.nlm.nih.gov/articles/PMC9873235/).)
- **Mouse — knock-in disease variants:**
  - **GluN2B-C456Y knock-in:** **impaired NMDAR-dependent LTD** with preserved synapse density/postsynaptic structure; anxiety-like behavior — and notably, **early pharmacological correction of the LTD defect improved adult behavior** ([PLOS Biology, C456Y model](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3000717)). A worked model of "selective plasticity defect → behavior."
  - Additional **Grin2b-mutant mice** show anterior cingulate **functional hyperconnectivity underlying sensory hypersensitivity** ([Mol Psychiatry 2024](https://www.nature.com/articles/s41380-024-02572-y)), relevant to the ASD phenotype.
- **Rat model:** a **GRIN2B rat model shows absence seizures and sleep–wake abnormalities** ([PMC12779324](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12779324/)) — recapitulating the epilepsy dimension.
- **Cellular / iPSC models:** **patient iPSC-derived neurons** and heterologous expression (HEK/Xenopus oocyte electrophysiology) are the workhorses for GoF/LoF classification — showing suppressed neural-progenitor differentiation, impaired dendrite growth (724t truncation), and altered channel biophysics (N615I/V618G GoF; G689C/S agonist-potency shifts).
- **Model types available:** constitutive KO, heterozygous KO, conditional (floxed) alleles, and knock-in point mutants — resources via **MGI/IMPC/KOMP**; rat via **RGD**; zebrafish via **ZFIN**.
- **Phenotype recapitulation & limits:** mouse/rat capture LTD/plasticity deficits, learning/memory impairment, seizures, and ASD-like circuit/behavioral features — good face validity. **Limitations:** rodents can't model the full human intellectual-disability/language phenotype, the human-specific cortical developmental timeline differs, and the constitutive KO's neonatal lethality forces reliance on conditional/knock-in strategies to study postnatal roles. Use `evidence_source: MODEL_ORGANISM` for all of these; keep them distinct from the human clinical phenotype claims.

---

## Curation notes for the dismech entry

A few things worth flagging as you build this out:
- **The GoF/LoF axis is the entry's spine.** Model it explicitly — two mechanistic arms (Arm A pore/Ca²⁺-hyperexcitation → seizures; Arm B trafficking/haploinsufficiency → impaired neurodevelopment) converging on abnormal synaptic plasticity + DD/ID. The `mechanistic_hypotheses` + `hypothesis_groups` machinery fits this two-arm structure nicely, and it directly gates the treatment pattern (memantine/radiprodil `target_mechanisms` on the GoF node; L-serine on the LoF node).
- **This could `conforms_to` `epilepsy_excitation_inhibition_imbalance`** (`#Excitation-Inhibition Imbalance`) for the seizure arm — a natural module fit.
- **Verify every PMID before committing** per the DR/anti-hallucination SOP. The high-confidence, search-verified ones: **20890276** (Endele 2010, Nat Genet), **24272827** (Lemke 2014, Ann Neurol — N615I/V618G GoF/West), **28377535** (Platzer 2017, J Med Genet — the cohort + frequencies), **29851452** (GeneReviews), **34997442** (L-serine null variants), **41489401** (memantine GoF, Epilepsia 2026). Run `just fetch-reference` on each and confirm exact-quote snippets against the cached abstract before use — I've paraphrased throughout, so none of the above are quote-ready yet.
- **NEC check:** GRIN2B sits near GRIN2A/GRIN2D/GRIN1 (a numbered/related-gene series → moderate NEC risk). Confirm the MONDO you anchor on (MONDO:0014505 DEE27 vs MONDO:0013655 MRD6) matches the intended severity framing, and that report content is about **2B**, not 2A.
- **Prevalence:** code qualitatively (`RARE`/`ULTRA_RARE`), don't invent a rate — the literature only gives "~0.2% of NDD/epilepsy cohorts, <100–200 described."

**Sources:**
- [GRIN2B-Related Neurodevelopmental Disorder — GeneReviews (PMID:29851452)](https://www.ncbi.nlm.nih.gov/books/NBK501979/)
- [Frontiers/PMC9873235 — pathophysiological mechanisms review](https://pmc.ncbi.nlm.nih.gov/articles/PMC9873235/)
- [OMIM #616139 DEE27](https://omim.org/entry/616139) · [OMIM *138252 GRIN2B](https://omim.org/entry/138252)
- [Endele 2010, Nat Genet, PMID:20890276](https://pubmed.ncbi.nlm.nih.gov/20890276/) · [Lemke 2014, Ann Neurol, PMID:24272827](https://pubmed.ncbi.nlm.nih.gov/24272827/) · [Platzer 2017, J Med Genet, PMID:28377535](https://pubmed.ncbi.nlm.nih.gov/28377535/)
- [Soto 2022, L-serine null variants, PMID:34997442](https://pubmed.ncbi.nlm.nih.gov/34997442/) · [Karnstedt 2026, memantine GoF, PMID:41489401](https://pubmed.ncbi.nlm.nih.gov/41489401/) · [Radiprodil HONEYCOMB coverage](https://www.neurologylive.com/view/radiprodil-significantly-reduces-seizure-frequency-phase-1b-honeycomb-study-grin-related-neurodevelopmental-disorder)
- [C456Y knock-in mouse, PLOS Biology](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3000717) · [Grin2b-mutant mouse, Mol Psychiatry 2024](https://www.nature.com/articles/s41380-024-02572-y) · [GRIN2B rat model, PMC12779324](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12779324/)
- [NORD — GRIN-related disorders](https://rarediseases.org/rare-diseases/grin-related-disorders/) · [gnomAD constraint / SFARI GRIN2B](https://gene.sfari.org/database/human-gene/GRIN2B)