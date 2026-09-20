---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T18:52:36.313859'
end_time: '2026-08-27T18:58:14.092246'
duration_seconds: 337.78
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CYB561-Related Orthostatic Hypotension
  mondo_id: ''
  category: ''
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
  num_turns: 34
  total_cost_usd: 1.5096577999999998
  session_id: 00937d02-a143-56ac-a731-3747f9ee4c64
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 20
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 4
  off_topic: 1
  off_topic_references:
  - PMC:PMC10005133
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CYB561-Related Orthostatic Hypotension
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **CYB561-Related Orthostatic Hypotension** covering all of the
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

I'll research this rare disease using web search tools. Let me start by loading the necessary tools and searching for primary literature.

# CYB561-Related Orthostatic Hypotension: Comprehensive Research Report

## 1. Disease Information

**Overview.** CYB561-related orthostatic hypotension (clinically designated **Orthostatic Hypotension 2, ORTHYP2**; OMIM #618182) is an ultra-rare, autosomal recessive monogenic disorder of catecholamine biosynthesis. It causes severe, lifelong, disabling neurogenic orthostatic hypotension due to a selective, isolated failure to synthesize norepinephrine (noradrenaline) and epinephrine (adrenaline) from dopamine, while sympathetic cholinergic (sweating) and parasympathetic function remain intact. It is biochemically and clinically a phenocopy of dopamine β-hydroxylase (DBH) deficiency but is caused by a different gene — *CYB561* — that encodes an essential redox cofactor-recycling protein rather than the catecholamine-synthesizing enzyme itself (van den Berg et al., *Circ Res* 2018; Shibao et al., *Neurology* 2020).

**Key identifiers:**
- **OMIM phenotype:** #618182 — Orthostatic Hypotension 2 (ORTHYP2)
- **OMIM gene:** *600019 — Cytochrome b561; CYB561 (aliases: CYB561A1, FRRS2, CGCytb)
- **Gene location:** Chromosome 17q23.3 (GRCh38: chr17:63,432,304–63,446,639); NCBI Gene ID 1534; HGNC:2576
- **Protein:** Transmembrane ascorbate-dependent reductase CYB561 (UniProt P49447), 251 amino acids, ~27.6 kDa
- **Related/parent MONDO concept:** MONDO:0005469 (orthostatic hypotension) — a disease-specific MONDO term for the CYB561 subtype specifically has not been confirmed as separately minted at time of writing; ORTHYP2/OMIM:618182 is the authoritative cross-reference to use
- **Note:** This is distinct from **Orthostatic Hypotension 1 (ORTHYP1, OMIM #223360)**, which is dopamine β-hydroxylase (DBH) deficiency itself (chromosome 9q34, *DBH* gene)

**Synonyms/alternative names:** Orthostatic hypotension 2; ORTHYP2; CYB561 deficiency; congenital absence of norepinephrine due to CYB561 mutations; cytochrome b561 deficiency

**Evidence basis:** All clinical knowledge derives from **two published families comprising a total of 4–5 documented patients worldwide** (as of the most recent literature identified) — this is one of the rarest monogenic disorders in the medical literature, described in only two primary papers (2018, 2020). Information is therefore aggregated, case-series-level clinical/biochemical/genetic data plus a knockout mouse model, not large-cohort or EHR-derived data.

---

## 2. Etiology

**Disease causal factor:** Purely genetic — biallelic (homozygous or compound heterozygous) loss-of-function pathogenic variants in *CYB561*. There is no known environmental, infectious, or acquired trigger; the mechanism is a congenital, constitutive metabolic block.

**Genetic risk factors (causal variants identified to date):**
| Variant (HGVS) | Protein change | Type | Family/patients | Zygosity |
|---|---|---|---|---|
| c.262G>A | p.Gly88Arg (G88R) | Missense, exon 3, highly conserved residue in 3rd transmembrane domain | Dutch family (2 sisters) | Homozygous |
| c.131G>A | p.Trp44* (W44X) | Nonsense, exon 2 | American family, sisters (patients 1 & 2) | Homozygous |
| Exon 2 deletion | — | Large deletion (null allele) | American family, patient 4 (Indian-origin) | Compound heterozygous (in trans with below) |
| c.157C>T | p.His53Tyr (H53Y) | Missense, previously unreported, highly conserved site | Same patient 4 | Compound heterozygous |

(van den Berg MP, et al. *Circ Res.* 2018;122(6):846–854, doi:10.1161/CIRCRESAHA.117.311949; Shibao CA, Garland EM, Black BK, Mathias CJ, Grant MB, Root AW, Robertson D, Biaggioni I. "Congenital absence of norepinephrine due to CYB561 mutations." *Neurology.* 2020;94(2):e200–e204, PMID: 31822578, PMCID: PMC6988982)

**Population variant frequency (heterozygous carrier data from gnomAD, cited in OMIM #618182):**
- The G88R-equivalent change (c.262G>C) was found heterozygous in 2 of 126,628 non-Finnish European alleles in gnomAD.
- The W44X nonsense variant was found once in 110,060 non-Finnish European control alleles.
- These very low population frequencies are consistent with an ultra-rare autosomal recessive disorder and argue against significant population stratification of carrier frequency, though systematic gnomAD constraint metrics (pLI, missense Z-score) for *CYB561* were not identified in available sources.

**Environmental risk factors:** None identified — this is a fully penetrant congenital enzymatic/cofactor defect, not modulated by lifestyle, toxins, or occupational exposure. (Volume depletion, heat, prolonged standing, and vasodilating drugs are expected to exacerbate symptoms mechanically, as with any severe orthostatic hypotension, but do not cause the underlying molecular lesion.)

**Protective factors:** None specific to genotype have been reported (too few patients for a genotype-modifier analysis). No protective variants or gene-environment interaction studies exist for this ultra-rare condition.

**Mechanistic link (etiology → pathophysiology bridge):** *CYB561* encodes a six-transmembrane-helix, two-heme-b cytochrome resident in catecholamine secretory vesicle membranes. It transfers electrons from cytoplasmic ascorbate across the vesicle membrane to regenerate ascorbate (from its oxidized semidehydroascorbate/monodehydroascorbate radical form) inside the vesicle lumen. Intravesicular ascorbate is the essential electron-donating cofactor for **dopamine β-hydroxylase (DBH)**, the enzyme that converts dopamine to norepinephrine, and also serves peptidylglycine α-amidating monooxygenase (PAM). Loss-of-function *CYB561* variants abolish intravesicular ascorbate recycling, producing a **functional (secondary) DBH deficiency** despite structurally and enzymatically normal DBH protein and a wild-type *DBH* gene.

---

## 3. Phenotypes

Phenotype data are drawn from the 4 fully characterized patients (2 sibling pairs) in van den Berg 2018 and Shibao 2020.

| Phenotype | Type | Frequency in reported cohort | Onset | Course | HPO suggestion |
|---|---|---|---|---|---|
| Severe orthostatic hypotension | Clinical sign | 4/4 (100%) | Infancy/early childhood, lifelong | Chronic, disabling, non-progressive but persistent | HP:0001278 (Orthostatic hypotension) |
| Syncope/near-syncope on standing | Symptom | Frequent, reported in all patients | Infancy–childhood onward | Episodic, provoked by upright posture | HP:0001279 (Syncope) |
| Lack of compensatory tachycardia on standing | Clinical/physiologic sign | Present (heart rate ratios for sinus arrhythmia and Valsalva normal, but no adequate BP-driven tachycardic compensation) | — | Chronic | HP:0031637 (Impaired ability to increase heart rate with exercise) — closest match; consider free text |
| Impaired Valsalva blood pressure response | Physiologic/laboratory abnormality | 4/4 | — | Chronic | No precise HP term; describe via `Autonomic function test abnormality` HP:0012332 |
| Episodic/recurrent hypoglycemia | Laboratory/clinical | 3/4 (patients 1, 2, 3) — severe enough that patient 2 underwent partial pancreatectomy | Childhood | Episodic | HP:0001943 (Hypoglycemia) |
| Seizures (childhood) | Clinical sign | Reported in at least 3 patients, etiology unclear (possibly hypoglycemia- or hypotension-related) | Childhood | Episodic | HP:0001250 (Seizure) |
| Impaired renal function / decreased GFR | Laboratory abnormality | Reported in OMIM clinical synopsis for a subset of patients | Variable, later-onset | Can be progressive | HP:0012622 (Chronic kidney disease) / HP:0012213 (Abnormal renal physiology) |
| Normal sweating (thermoregulatory/sudomotor function) | Preserved function (negative finding) | 4/4 normal | — | Stable | Relevant as a distinguishing negative — HP:0000970 (Hyperhidrosis)/absence noted |
| Preserved parasympathetic (cardiovagal) function | Preserved function | 4/4 normal (neck suction, phenylephrine responses intact) | — | Stable | — |
| Normal birth and mental/cognitive development | Negative finding | 4/4 | — | — | Explicitly documented as normal — important for distinguishing from syndromic mitochondrial/neurodevelopmental disorders |
| Reduced life expectancy / early mortality | Outcome | One patient (patient 3, brother of patients 1–2) died at age 16 | Childhood/adolescence | — | HP:0034396 (or free text mortality note) |

**Quality of life impact:** Patients describe the orthostatic hypotension as profoundly disabling — near-continuous presyncope/syncope risk on standing severely limits activities of daily living, education, and employment; no formal EQ-5D/SF-36 data have been published for this specific cohort, but qualitative descriptions in both primary papers characterize impact as severe and lifelong until droxidopa treatment. Recurrent, severe hypoglycemia requiring surgical intervention (pancreatectomy) in childhood represents an additional major QoL and safety burden.

**Suggested HPO terms:** HP:0001278 (Orthostatic hypotension), HP:0001943 (Hypoglycemia), HP:0001250 (Seizure), HP:0012622 (Chronic kidney disease), HP:0001279 (Syncope), HP:0012332 (Abnormal autonomic nervous system physiology).

---

## 4. Genetic/Molecular Information

**Causal gene:** *CYB561* (HGNC:2576; NCBI Gene 1534; OMIM *600019); no other gene has been implicated in ORTHYP2.

**Pathogenic variant summary** (see Section 2 table for full HGVS detail):
- **Variant classification:** All four reported alleles are consistent with **pathogenic/loss-of-function** under ACMG/AMP-type reasoning — nonsense (W44X), a large exonic deletion (exon 2), and two missense changes (G88R, H53Y) at residues that are highly evolutionarily conserved and lie within/near transmembrane or heme-coordinating regions critical to redox function. Formal ClinVar submission status for each variant was not independently confirmed in the sources reviewed here; curators should verify current ClinVar classification before citing a specific ACMG category.
- **Variant type spectrum:** missense (2), nonsense (1), whole-exon deletion (1) — i.e., a mix of null and likely hypomorphic/null missense alleles, consistent with a fully recessive loss-of-function mechanism.
- **Allele frequency:** Both missense/nonsense changes are present at very low frequency in gnomAD non-Finnish European controls (2/126,628 and 1/110,060 alleles respectively; see Section 2), consistent with pathogenicity and rarity.
- **Origin:** All variants reported are **germline**; no somatic *CYB561* variants are relevant to this disease phenotype (somatic *CYB561* alterations have been studied in an entirely unrelated context — oncology, see below).
- **Functional consequence:** Loss of CYB561 transmembrane electron-transfer/ascorbate-recycling activity → failure to regenerate intravesicular ascorbate → **functional/secondary loss of DBH catalytic activity** (DBH protein itself and its gene are normal) → failure of dopamine-to-norepinephrine conversion.

**Modifier genes:** None have been identified or proposed; the cohort is far too small (single-digit patients) to support modifier-gene analysis.

**Epigenetic information:** No epigenetic (DNA methylation, histone modification) studies of *CYB561* or ORTHYP2 have been published.

**Chromosomal abnormalities:** None reported beyond the intragenic exon-2 deletion described above; no aneuploidy, translocation, or large structural rearrangement has been implicated.

**Protein structure context:** CYB561 belongs to the cytochrome b561 family of transmembrane ascorbate-dependent reductases, characterized by six transmembrane α-helices with the central four coordinating two b-type heme groups via four conserved histidine residues, enabling trans-bilayer electron transfer from cytoplasmic ascorbate to luminal semidehydroascorbate radical. This structural framework explains why missense substitutions at conserved transmembrane/heme-adjacent residues (G88R, H53Y) are functionally disruptive.

**Suggested ontology terms:** `hgnc:2576` (CYB561 gene), GO terms for molecular function: monodehydroascorbate reductase (NAD(P)H) activity / transmembrane electron transporter activity; GO cellular component: secretory vesicle membrane.

---

## 5. Environmental Information

- **Environmental factors:** None are causal. As with all forms of severe autonomic/neurogenic orthostatic hypotension, non-causal exacerbating factors likely include heat exposure, large meals (postprandial hypotension), dehydration, and vasoactive/vasodilating medications — these are inferred from general orthostatic hypotension physiology rather than reported specifically for CYB561 patients in the literature reviewed.
- **Lifestyle factors:** Not specifically studied in this cohort; general orthostatic hypotension management principles (fluid/salt intake, compression garments, avoidance of prolonged standing) apply by extension from DBH-deficiency and general neurogenic-OH literature, but are not disease-specific findings.
- **Infectious agents:** Not applicable — no infectious trigger or association has been described.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Molecular trigger:** Biallelic loss-of-function *CYB561* variants → absent/non-functional CYB561 transmembrane ascorbate-dependent reductase in catecholamine secretory vesicle membranes (chromaffin cells of adrenal medulla and sympathetic noradrenergic neurons).
2. **Biochemical consequence:** Failure to regenerate reduced ascorbate within the vesicle lumen (via trans-membrane electron transfer from cytosolic ascorbate) → progressive depletion of intravesicular ascorbate.
3. **Enzymatic consequence:** Dopamine β-hydroxylase (DBH), the vesicular enzyme that hydroxylates dopamine to norepinephrine, requires ascorbate as an electron-donating cofactor at each catalytic cycle; without regenerated ascorbate, DBH is catalytically starved — producing a **functional DBH deficiency despite normal DBH protein, normal plasma DBH enzyme activity, and a wild-type *DBH* gene**.
4. **Cellular/systems consequence:** Norepinephrine (and downstream epinephrine, synthesized from norepinephrine in the adrenal medulla) synthesis fails almost completely — plasma norepinephrine and its intraneuronal metabolite DHPG are undetectable, while dopamine and its metabolites remain normal (notably, in contrast to primary DBH deficiency where dopamine accumulates to markedly elevated levels — the authors hypothesize that the loss of ascorbate's local antioxidant capacity within the vesicle instead promotes degradation of DOPA/dopamine rather than their accumulation).
5. **Organ/systemic consequence:** Loss of sympathetic noradrenergic vasoconstrictor tone → inability to maintain blood pressure on standing → severe orthostatic hypotension, syncope, and (in childhood) episodic hypoglycemia (loss of catecholamine-driven counter-regulation) and possible renal hypoperfusion contributing to chronic kidney impairment in some patients.
6. **Selectively spared systems:** Sympathetic **cholinergic** (sudomotor/sweating) and **parasympathetic** (cardiovagal, e.g., heart-rate responses to Valsalva/neck suction/phenylephrine) pathways are intact, because these do not depend on DBH-catalyzed norepinephrine synthesis in the same secretory-vesicle compartment — this selective sparing is a key diagnostic and mechanistic signature of the disease.

**Molecular pathway/players:** Dopamine → (DBH, ascorbate-cofactor-dependent) → norepinephrine → (in adrenal medulla, phenylethanolamine N-methyltransferase, PNMT) → epinephrine. CYB561 operates upstream of DBH as a cofactor-regeneration (ascorbate-recycling) protein, not as part of the catecholamine biosynthetic pathway itself. CYB561 also supports peptidylglycine α-amidating monooxygenase (PAM), another ascorbate-dependent secretory-vesicle enzyme, though a clinical phenotype attributable to PAM dysfunction has not been specifically documented in these patients.

**Cellular processes involved:** Catecholamine biosynthesis and vesicular storage/secretion in chromaffin cells (adrenal medulla) and postganglionic sympathetic noradrenergic neurons; transmembrane electron transport; ascorbate redox cycling.

**Protein dysfunction:** Loss-of-function of a transmembrane electron-transfer protein (not misfolding/aggregation-type pathology as documented; missense variants likely destabilize the heme-coordinating transmembrane architecture).

**Biochemical abnormalities (documented, with values from Shibao et al. 2020):**
- Plasma norepinephrine: undetectable (pre-treatment)
- Plasma DHPG (intraneuronal norepinephrine metabolite): undetectable (pre-treatment)
- Plasma dopamine and dopamine metabolites: normal
- Plasma DBH enzymatic activity: normal (tested in patients 1 and 2) — confirming the defect is upstream/cofactor-related, not in the DBH enzyme itself
- Post-droxidopa treatment: Patient 1 norepinephrine rose to 65 pg/mL, DHPG to 771 pg/mL; Patient 2 norepinephrine rose to 139 pg/mL, DHPG to 1,220 pg/mL — demonstrating that exogenous L-DOPS bypasses the defect and restores measurable norepinephrine synthesis via DOPA-decarboxylase.

**Tissue damage mechanisms:** Chronic hypotension/hypoperfusion is proposed (though not formally proven mechanistically in the literature) as a contributor to the renal dysfunction/reduced GFR noted in some patients; this remains an area of uncertainty rather than an established causal chain.

**Molecular profiling / omics:** No transcriptomic, proteomic, metabolomic, single-cell, or spatial-omics datasets specific to human CYB561-deficient tissue have been published (patient tissue for such studies is essentially unobtainable given the extreme rarity and the non-lethal, non-biopsied nature of the primary affected tissue — sympathetic neurons/adrenal medulla). The main molecular data available are targeted plasma catecholamine/metabolite panels (above) and the knockout mouse brain/adrenal catecholamine profiling described in Section 15.

**Suggested GO terms:** GO:0140905 (or nearest current term for monodehydroascorbate reductase / transmembrane ascorbate-ferrireductase activity), GO:0042423 (catecholamine biosynthetic process), GO:0006584 (catecholamine metabolic process). **Suggested CL terms:** CL:0002673 (adrenal medulla chromaffin cell), CL:0011103 or nearest sympathetic noradrenergic neuron term.

---

## 7. Anatomical Structures Affected

- **Organ level:**
  - **Primary:** Adrenal medulla (chromaffin cells) and postganglionic sympathetic noradrenergic neurons (the norepinephrine-synthesizing tissues where CYB561 is highly expressed in catecholamine secretory vesicles).
  - **Secondary:** Cardiovascular system (functional consequence — inability to maintain blood pressure); kidney (reported impaired GFR/renal dysfunction in a subset of patients, presumed secondary to chronic hypoperfusion, though the pathomechanism is not definitively established); pancreas (implicated only indirectly — partial pancreatectomy was performed in one patient for severe recurrent hypoglycemia, but the pancreas is not a primary site of CYB561 pathology; the hypoglycemia is attributed to loss of catecholamine-mediated glucose counter-regulation).
  - **Body systems:** Cardiovascular (autonomic/neurogenic hypotension), endocrine/metabolic (hypoglycemia), renal, and — via seizures of unclear etiology — potentially neurologic (secondary to hypoglycemia/hypotension rather than primary CNS pathology).

- **Tissue and cell level:** Chromaffin cells of the adrenal medulla; sympathetic noradrenergic (postganglionic) neurons. Suggested UBERON: UBERON:0002001 (adrenal medulla); suggested CL: adrenal medulla chromaffin cell, sympathetic neuron.

- **Subcellular level:** Catecholamine (chromaffin/large dense-core) secretory vesicles — specifically the vesicle membrane, where CYB561 resides as an integral transmembrane protein performing trans-bilayer electron transfer. Suggested GO Cellular Component: GO:0034774 (secretory granule lumen) / GO:0030667 (secretory granule membrane).

- **Localization/lateralization:** Systemic/bilateral — this is a generalized sympathetic noradrenergic defect (adrenal medulla is typically bilateral; sympathetic neurons are distributed throughout the body), not a focal or lateralized process.

---

## 8. Temporal Development

- **Onset:** Infancy or early childhood (explicitly stated in OMIM #618182 clinical description); orthostatic hypotension has been lifelong/present since early life in every reported patient.
- **Onset pattern:** Congenital/insidious — present from earliest life rather than acute onset in adulthood, distinguishing it from acquired autonomic failure syndromes (e.g., pure autonomic failure, multiple system atrophy) that typically present in mid-to-late adulthood.
- **Progression/stages:** No formal staging system exists. The orthostatic hypotension itself appears to be a stable, chronic, lifelong deficit (not neurodegenerative/progressive in the way synucleinopathies are), but individual complications (renal dysfunction, hypoglycemic episodes) can evolve over the patient's lifetime. Patients have been characterized/followed into adulthood (oldest reported patients evaluated at ages 38–39), indicating survival well into adulthood is possible with recognition and treatment, though one sibling (patient 3) died at age 16, indicating the disease carries significant premature-mortality risk if unrecognized/untreated.
- **Course pattern:** Chronic and disabling but not classically "progressive" in a neurodegenerative sense; hypoglycemic and (childhood) seizure episodes are episodic superimposed events rather than a steadily worsening baseline.
- **Duration:** Lifelong/chronic — no spontaneous resolution has been described.
- **Remission patterns:** No spontaneous remission reported; treatment-induced improvement (droxidopa) is substantial and sustained for the orthostatic hypotension component specifically (see Section 12).
- **Critical periods:** Childhood is a particularly high-risk window given the reported severe hypoglycemic episodes (one requiring partial pancreatectomy) and childhood-onset seizures — early diagnosis in infancy/childhood, before catastrophic hypoglycemic or hypotensive events occur, appears to be an important unmet clinical need highlighted implicitly by the case histories.

---

## 9. Inheritance and Population

- **Epidemiology:** No formal prevalence or incidence estimate exists — this is one of the rarest described monogenic disorders, with only 2 families (4–5 patients) reported in the peer-reviewed literature to date (2018 and 2020 publications). It should be considered "ultra-rare" / essentially unquantifiable epidemiologically at this time; extrapolation from gnomAD carrier frequencies (see Section 2) would suggest a theoretical population prevalence far below 1 in 1,000,000, consistent with the observed case count, but no formal birth-prevalence study has been performed.
- **Inheritance pattern:** Autosomal recessive (biallelic pathogenic *CYB561* variants required; heterozygous carriers are unaffected).
- **Penetrance:** Appears to be complete/fully penetrant in the biallelic state based on all reported cases, though the total number of genotyped individuals is far too small for a formal penetrance estimate.
- **Expressivity:** Some variability is noted — e.g., not all patients had documented seizures or renal dysfunction, and severity of hypoglycemia varied (only one patient required pancreatectomy) — but core features (severe orthostatic hypotension, undetectable norepinephrine, preserved cholinergic/parasympathetic function) were consistent across all reported patients.
- **Genetic anticipation:** Not applicable/not reported (no repeat-expansion mechanism involved).
- **Germline mosaicism:** Not reported.
- **Founder effects:** No specific founder mutation/population has been identified; reported families are of Dutch, American (non-Hispanic Caucasian), and Indian ancestry respectively — i.e., globally distributed rather than confined to a single founder population, though the extremely small number of families precludes any definitive geographic/ethnic epidemiology.
- **Consanguinity:** Not explicitly reported as a factor in the published pedigrees (the Dutch sisters were homozygous for G88R and the American sisters homozygous for W44X, which could reflect either consanguinity or a more common regional allele, but this was not specifically discussed in available source summaries).
- **Carrier frequency:** Estimated indirectly from gnomAD data (see Section 2): approximately 1.6–0.9 per 100,000 non-Finnish European alleles for the two specific reported variants — true carrier frequency across all possible pathogenic *CYB561* alleles and populations is unknown.
- **Population demographics:** Reported patients are of Dutch, American (Caucasian non-Hispanic), and Indian ancestry — no clear ethnic predisposition has been established given the small sample.
- **Sex ratio:** Notably, reported adult patients described in detail (patients 1, 2, 4) are female; one male sibling (patient 3) was also affected and died at age 16 — with such a small cohort, no meaningful sex-ratio conclusion can be drawn (autosomal recessive inheritance predicts equal sex distribution).
- **Age distribution:** Patients evaluated ranged from age 13 (deceased at 16) to age 39 at time of clinical description, indicating both childhood and adult survival are possible.

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Plasma catecholamine panel (the key diagnostic test):** Undetectable plasma norepinephrine and DHPG with normal plasma dopamine and dopamine metabolites is the biochemical hallmark. This pattern differs subtly but importantly from classic DBH deficiency, where plasma dopamine is typically markedly *elevated* (accumulated upstream of the enzymatic block) rather than normal — a potentially useful biochemical discriminator, per the mechanistic hypothesis discussed in Shibao et al. 2020.
- **Plasma DBH enzyme activity assay:** Normal in CYB561-deficient patients (tested in 2 patients) — this is the critical test that distinguishes CYB561 deficiency (functional/secondary DBH deficiency) from primary DBH deficiency (ORTHYP1), where plasma DBH activity is absent/markedly reduced.
- **Autonomic function testing:**
  - Valsalva maneuver: exaggerated hypotension during phase 2, absent blood pressure overshoot during phase 4 — abnormal, consistent with sympathetic noradrenergic failure.
  - Heart rate ratios (sinus arrhythmia, Valsalva ratio): normal — indicating intact parasympathetic/cardiovagal function.
  - Cardiovagal baroreflex testing (neck suction, phenylephrine pressor challenge): normal responses.
  - Thermoregulatory sweat testing: normal — indicating intact sympathetic cholinergic function.
  - Tilt-table/orthostatic vital signs: profound blood-pressure drop on standing without compensatory tachycardia.

**Genetic testing:**
- **Recommended approach:** Given the extreme rarity and the specificity of the biochemical phenotype (undetectable norepinephrine/DHPG with normal dopamine and normal plasma DBH activity), targeted Sanger sequencing or a small autonomic-failure/catecholamine gene panel including *CYB561* and *DBH* is reasonable once the biochemical pattern is established; whole-exome sequencing (as was used in the discovery of both reported families) is appropriate when the biochemical pattern is atypical or a panel is unrevealing.
- **Single-gene testing:** *CYB561* sequencing plus deletion/duplication analysis (given that one reported allele was a whole-exon deletion, copy-number-sensitive methods such as MLPA or exome-based CNV calling are important, not sequencing alone).
- **Gene panels:** No dedicated commercial "CYB561 panel" is documented in the sources reviewed; it would logically be included in autonomic-failure/dysautonomia or catecholamine-biosynthesis gene panels alongside *DBH*, *TH* (tyrosine hydroxylase), and *DDC* (aromatic L-amino acid decarboxylase).
- **WES/WGS utility:** Both discovery families were solved by exome/genomic sequencing approaches — this remains the most practical diagnostic route for an ultra-rare, non-panel-covered condition.
- Chromosomal microarray, karyotyping, FISH, mitochondrial DNA testing, and repeat-expansion testing are **not indicated** — this is a single-gene autosomal recessive disorder with no chromosomal or mitochondrial component identified.

**Omics-based diagnostics:** Not part of the standard/reported diagnostic workflow — plasma catecholamine biochemistry plus targeted/exome genetic sequencing are the established diagnostic route; no transcriptomic, proteomic, or liquid-biopsy diagnostic approach is described for this condition.

**Clinical criteria:** No formal consensus diagnostic-criteria statement (e.g., society guideline) exists for CYB561-related orthostatic hypotension specifically, given its recent discovery (2018) and extreme rarity. Diagnosis is currently case-based, built on the combination of (1) lifelong severe orthostatic hypotension, (2) undetectable plasma norepinephrine/DHPG with normal dopamine, (3) normal plasma DBH activity, and (4) biallelic *CYB561* variants.

**Differential diagnosis:**
- **Dopamine β-hydroxylase (DBH) deficiency (ORTHYP1, OMIM #223360):** The principal differential — nearly identical clinical/autonomic phenotype (severe lifelong orthostatic hypotension, ptosis, exercise intolerance, hypoglycemia in some cases) but distinguished biochemically by (a) markedly elevated plasma dopamine (vs. normal in CYB561 deficiency) and (b) absent/low plasma DBH enzyme activity (vs. normal in CYB561 deficiency), and genetically by pathogenic variants in *DBH* rather than *CYB561*.
- **Pure autonomic failure (PAF):** Sporadic, adult-onset (not congenital), and no genetic cause has been established, unlike CYB561 deficiency's clear childhood onset and monogenic recessive basis.
- **Familial dysautonomia (hereditary sensory and autonomic neuropathy type III, *ELP1/IKBKAP*):** Distinguished by prominent sensory neuropathy, absent overflow emotional tearing, hyperadrenergic vomiting crises, and optic neuropathy — features not present in isolated CYB561 deficiency, which spares sensory and cholinergic/parasympathetic pathways.
- **Multiple system atrophy / Parkinson disease with autonomic failure:** Adult-onset synucleinopathies with additional motor/cognitive features, not congenital, and biochemically and genetically distinct.

**Screening:** No newborn screening, carrier screening, or population screening program exists for this condition, consistent with its ultra-rare status and recent (2018) discovery.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No formal survival statistics exist given the tiny reported cohort. One reported patient (patient 3) died at age 16, indicating the disease can be life-threatening, particularly in childhood, likely related to severe hypoglycemic and/or hypotensive/syncopal episodes; other reported patients survived into their 30s. OMIM's clinical description notes that "some patients may also have renal dysfunction and reduced life expectancy," but this is a qualitative characterization rather than a quantified statistic.
- **Morbidity/function:** Severe, lifelong disability from recurrent syncope/presyncope until treatment; recurrent hypoglycemia (one patient required partial pancreatectomy) represents an additional major source of morbidity, particularly in childhood.
- **Quality of life:** Described qualitatively as severely impaired pre-treatment (disabling orthostatic hypotension); improved substantially with droxidopa in the cases reported, though no standardized QoL instrument (EQ-5D, SF-36) data have been published.
- **Complications:** Recurrent hypoglycemia (occasionally requiring surgical intervention), childhood seizures (etiology not definitively established — plausibly hypoglycemia- and/or hypotension-related), and renal dysfunction/decreased GFR in a subset of patients.
- **Recovery potential/prognostic factors:** With droxidopa treatment, plasma norepinephrine and its metabolite DHPG become measurable and orthostatic hypotension substantially improves — indicating that, unlike a neurodegenerative process, the underlying sympathetic neurons remain viable and capable of exocytotic norepinephrine release once the biosynthetic block is bypassed pharmacologically. This is a notably favorable prognostic feature relative to degenerative causes of autonomic failure.
- **Prognostic biomarkers:** Plasma norepinephrine/DHPG levels serve as both diagnostic and treatment-response biomarkers (rising from undetectable to measurable levels with droxidopa, as quantified in Section 6).

---

## 12. Treatment

**Pharmacotherapy (primary, disease-specific):**
- **Droxidopa (L-threo-dihydroxyphenylserine, L-DOPS; brand name Northera®)** is the cornerstone, mechanistically targeted treatment. It is a synthetic norepinephrine precursor that is converted directly to norepinephrine by the enzyme **DOPA-decarboxylase (aromatic L-amino acid decarboxylase)** — a step that is entirely independent of DBH and therefore bypasses the CYB561/DBH cofactor defect altogether.
  - **Dosing (as reported):** 100 mg three times daily was the effective and generally tolerated dose in the reported patients; higher doses caused excessive pressor responses in two patients and nausea in another, indicating a narrow therapeutic window requiring individualized titration.
  - **Efficacy:** Restored measurable plasma norepinephrine (rising from undetectable to 65–139 pg/mL) and DHPG (rising to 771–1,220 pg/mL), with corresponding improvement in orthostatic hypotension symptoms.
  - **NCIT suggestion:** `NCIT:C15986` (Pharmacotherapy) as `treatment_term`, with `therapeutic_agent` bound to the specific compound (droxidopa; NCIT has a specific concept, "Droxidopa," commonly indexed as `NCIT:C77244` — verify exact CURIE against the local NCIT adapter before curating) and `therapeutic_modality: SMALL_MOLECULE`.
- **Comparator/class context:** Droxidopa is the same first-line agent used for classic DBH deficiency (ORTHYP1) and for neurogenic orthostatic hypotension broadly (e.g., in pure autonomic failure, multiple system atrophy, and diabetic autonomic neuropathy), where it is FDA-approved (Northera) for symptomatic neurogenic orthostatic hypotension.

**Supportive/non-pharmacologic care (extrapolated from general severe-orthostatic-hypotension and DBH-deficiency management, not disease-specific trial data):**
- Increased fluid and salt intake, compression garments, physical countermaneuvers, and avoidance of triggers (heat, large meals, prolonged standing) are standard adjunctive measures for severe neurogenic orthostatic hypotension generally; specific trial data for the CYB561 population were not identified.
- Management of hypoglycemia (dietary/monitoring measures; surgical partial pancreatectomy was used in one severe pediatric case, though this is not considered a standard/first-line intervention and reflects an individualized, severe presentation).

**Advanced therapeutics (gene therapy, cell therapy, RNA-based, targeted/immunotherapy):** None have been developed or trialed for this condition — given the extreme rarity (single-digit total reported patients worldwide), there is no commercial or research incentive/infrastructure for such advanced modalities at this time, and no ClinicalTrials.gov-registered interventional trial specific to CYB561-related orthostatic hypotension was identified in the sources reviewed.

**Surgical/interventional:** Partial pancreatectomy was performed in one patient specifically for management of severe, recurrent hypoglycemia — this addresses a complication, not the underlying molecular defect, and is not considered standard-of-care for the disease generally.

**Experimental treatments:** No disease-specific clinical trials (with NCT identifiers) were identified for CYB561-related orthostatic hypotension.

**Treatment outcomes/adverse events:** Dose-limiting adverse effects of droxidopa in this population were excessive pressor response (hypertension) at higher doses in two patients, and nausea in another — consistent with droxidopa's known adverse-event profile in the broader neurogenic-orthostatic-hypotension population (supine hypertension is a well-recognized, dose-related class effect).

**Treatment strategy/algorithm:** No formal published treatment algorithm exists specifically for this ultra-rare condition; management in the literature follows the same individualized dose-titration approach used for droxidopa in DBH deficiency and other neurogenic orthostatic hypotension syndromes — start low, titrate to symptomatic/hemodynamic effect while monitoring for supine hypertension.

**Personalized medicine:** The treatment is inherently mechanism-targeted/personalized in the sense that droxidopa specifically bypasses the identified enzymatic block (dopamine→norepinephrine via DOPA-decarboxylase rather than the defective ascorbate-dependent DBH pathway) — this represents a genotype-informed, mechanism-based therapeutic strategy, though it is empirically the same drug used for the phenotypically similar DBH deficiency rather than a CYB561-specific novel agent.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense — this is a congenital, fully genetically determined disorder with no modifiable environmental cause to intervene upon before disease onset.
- **Secondary prevention (early detection):** No population screening program exists. Given the severe childhood morbidity/mortality risk (hypoglycemia, seizures, and the reported death at age 16), early clinical recognition of the biochemical signature (undetectable norepinephrine/DHPG with normal dopamine and normal DBH activity) in a child with unexplained severe orthostatic hypotension and/or hypoglycemia could in principle allow earlier initiation of droxidopa and closer glycemic monitoring, but this is an inference from the case reports rather than a published screening recommendation.
- **Tertiary prevention:** Droxidopa therapy and, where indicated, targeted management of hypoglycemia (dietary/monitoring strategies preferred over surgery where feasible) function as tertiary prevention against the disease's major complications (syncope-related injury, hypoglycemic seizures, and possibly progressive renal dysfunction from chronic hypoperfusion).
- **Immunization:** Not applicable — non-infectious, non-immune-mediated disorder.
- **Genetic counseling:** Because the disorder is autosomal recessive, genetic counseling for parents of an affected child (recurrence risk 25% per pregnancy) and, where relevant, carrier testing of at-risk family members / prenatal or preimplantation genetic testing in families with a known pathogenic *CYB561* allele would follow standard autosomal-recessive counseling principles, though no disease-specific counseling guideline has been published given the extreme rarity.
- **Public health/environmental interventions:** Not applicable.
- **Prophylaxis:** No prophylactic pharmacologic strategy beyond ongoing droxidopa maintenance therapy has been described.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring CYB561-deficient disease has been reported in any non-human species (companion animals, livestock, or wildlife). No OMIA (Online Mendelian Inheritance in Animals) entry for a natural CYB561-associated disease was identified.
- **Orthologous gene:** Mouse ortholog *Cyb561* (MGI:103253), located on mouse chromosome 11; this ortholog is the basis of the engineered knockout model described in Section 15 (an induced/laboratory model, not a naturally occurring veterinary disease).
- **Comparative biology:** The core biochemical machinery (CYB561–ascorbate–DBH axis) is evolutionarily conserved across vertebrates, and cytochrome b561-family ascorbate reductases are broadly conserved from insects to mammals (structural/functional comparative work exists on insect cytochrome b561 proteins as candidate ferric reductases), but no natural disease phenotype has been documented outside the engineered mouse knockout.
- **Zoonotic potential/cross-species transmission:** Not applicable — this is a non-infectious, purely genetic/metabolic disorder.

---

## 15. Model Organisms

**Mouse knockout model (the only reported animal model):**
- **Model type:** Genetic, constitutive knockout — *Cyb561*-null mice on a C57BL/6NTac genetic background, generated and characterized as part of the original human-disease-discovery study (van den Berg et al., *Circ Res* 2018).
- **Phenotype recapitulation:** Catecholamine and downstream metabolite concentrations were measured in brain and adrenal tissue of 6 *Cyb561* knockout mice. Findings included **decreased norepinephrine and normetanephrine in whole-brain homogenates** compared with wild-type mice, and **decreased normetanephrine and metanephrine in adrenal glands** — biochemically supporting the same norepinephrine-biosynthesis defect proposed for human patients, i.e., the model **partially to substantially recapitulates the core biochemical lesion** (reduced norepinephrine/downstream-metabolite synthesis).
- **Model limitations:** An important caveat emphasized in the literature is that **mice, unlike humans, can synthesize ascorbic acid de novo** (via functional L-gulonolactone oxidase), whereas humans cannot. This is a fundamental species difference that likely blunts the severity of ascorbate depletion — and therefore of the downstream DBH/norepinephrine-synthesis defect — in the mouse model relative to the human disease, meaning the knockout mouse is expected to under-represent the severity of human CYB561 deficiency. Reported physiological/behavioral orthostatic-hypotension phenotyping (e.g., blood pressure telemetry, tilt response) in the knockout mice was not identified as having been performed/published in the sources reviewed here — the mouse data available are limited to tissue catecholamine/metabolite biochemistry rather than a full autonomic-physiology characterization.
- **Applications:** The model supports study of the ascorbate-dependent catecholamine biosynthesis pathway and provides in vivo biochemical validation of the human genetic findings; it would be a candidate platform for testing pharmacologic bypass strategies (e.g., droxidopa) or future gene-replacement approaches, though no such intervention studies in the knockout model were identified in the literature reviewed.
- **Other model systems:** No zebrafish, *Drosophila*, *C. elegans*, yeast, iPSC-derived, or organoid models of CYB561 deficiency were identified. No cell-line (e.g., PC12 chromaffin-like cell) CRISPR-knockout functional studies specific to the disease phenotype were found in the sources reviewed, though CYB561 has been studied via cell-line knockdown/overexpression in unrelated oncology contexts (see note below).

**Note on an unrelated research literature:** A substantial and growing body of recent literature (2023–2025) studies *CYB561* in the context of **cancer biology** — e.g., as a prognostic biomarker and potential therapeutic target in breast cancer (via IRE1–XBP1–SREBF1 and FAK-ERK signaling, and via inhibition of H2AFY degradation), hepatocellular carcinoma, and prostate cancer neuroendocrine differentiation. This oncology literature is **mechanistically and clinically distinct** from CYB561-related orthostatic hypotension (it concerns CYB561 overexpression/dysregulation in tumor cells rather than germline loss-of-function causing autonomic failure) and should not be conflated with the disorder covered in this report, though curators should be aware of it when searching the literature to avoid Named-Entity-Confusion-type misattribution of evidence.

---

## Summary Table of Key Ontology Term Suggestions

| Category | Term |
|---|---|
| Gene | `hgnc:2576` (CYB561) |
| OMIM gene | `600019` |
| OMIM phenotype | `618182` (ORTHYP2) |
| Related MONDO | `MONDO:0005469` (orthostatic hypotension — generic; verify/curate subtype-specific term if one exists) |
| Phenotype (HP) | HP:0001278 Orthostatic hypotension; HP:0001943 Hypoglycemia; HP:0001250 Seizure; HP:0012622 Chronic kidney disease; HP:0001279 Syncope |
| Anatomy (UBERON) | UBERON:0002001 Adrenal medulla |
| Cell type (CL) | Adrenal medulla chromaffin cell; sympathetic noradrenergic neuron |
| Chemical (CHEBI) | Ascorbic acid; dopamine; noradrenaline (norepinephrine); droxidopa |
| Treatment (NCIT) | NCIT:C15986 Pharmacotherapy (treatment_term) + therapeutic_agent: droxidopa |
| Inheritance | Autosomal recessive (HP:0000007) |

---

## Sources

- [Mutations in CYB561 Causing a Novel Orthostatic Hypotension Syndrome — Circulation Research (van den Berg et al., 2018)](https://www.ahajournals.org/doi/10.1161/CIRCRESAHA.117.311949)
- [Full-text repository copy (Radboud University repository)](https://repository.ubn.ru.nl/bitstream/handle/2066/190722/190722.pdf?sequence=1&isAllowed=y)
- [Full-text repository copy (University of Groningen)](https://pure.rug.nl/ws/files/214753191/CIRCRESAHA.117.311949.pdf)
- [Congenital absence of norepinephrine due to CYB561 mutations — Neurology (Shibao et al., 2020) — PubMed](https://pubmed.ncbi.nlm.nih.gov/31822578/)
- [Congenital absence of norepinephrine due to CYB561 mutations — PMC full text (PMC6988982)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6988982)
- [OMIM #618182 — Orthostatic Hypotension 2; ORTHYP2](https://omim.org/entry/618182)
- [OMIM Clinical Synopsis — #618182](https://omim.org/clinicalSynopsis/618182)
- [OMIM *600019 — Cytochrome b561; CYB561](https://www.omim.org/entry/600019)
- [OMIM #223360 — Orthostatic Hypotension 1; ORTHYP1 (DBH deficiency, for comparison)](https://omim.org/entry/223360)
- [CYB561 Gene — GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=CYB561)
- [UniProt P49447 — Transmembrane ascorbate-dependent reductase CYB561](https://www.uniprot.org/uniprotkb/P49447/entry)
- [Cyb561 MGI Mouse Gene Detail — MGI:103253](https://www.informatics.jax.org/marker/MGI:103253)
- [A novel autosomal recessive orthostatic hypotension syndrome — Clinical Autonomic Research commentary (2018)](https://link.springer.com/article/10.1007/s10286-018-0578-z)
- [A New Player in Circulatory Adaptation to Orthostatism — Circulation Research commentary](https://www.ahajournals.org/doi/10.1161/circresaha.118.312749)
- [Dopamine beta-hydroxylase deficiency — MedLink Neurology](https://www.medlink.com/articles/dopamine-beta-hydroxylase-deficiency)
- [Dopamine beta-hydroxylase deficiency — Orphanet](https://www.orpha.net/en/disease/detail/230)
- [Clinical presentation and long-term follow-up of dopamine beta hydroxylase deficiency — Journal of Inherited Metabolic Disease (Wassenberg et al., 2021)](https://onlinelibrary.wiley.com/doi/full/10.1002/jimd.12321)
- [Spectral and Redox Properties of a Recombinant Mouse Cytochrome b561 Protein — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10005133/)
- [CYB561 is a potential therapeutic target for breast cancer — European Journal of Medical Research (2024)](https://link.springer.com/article/10.1186/s40001-024-02010-3)
- [Oncoprotein CYB561 promotes breast cancer lipogenesis — Cell Death Discovery](https://www.nature.com/articles/s41420-026-03101-2)

**Limitations of this report:** This is one of the rarest monogenic disorders in the medical literature, with the entire published human clinical evidence base consisting of two primary papers describing 4–5 total patients across 2 unrelated families. Several fields in the disease-characteristics template above (formal prevalence/incidence, QoL instrument scores, ACMG variant classifications, ClinVar status, gnomAD constraint metrics, autonomic-physiology data in the knockout mouse) could not be populated from the sources reviewed and should be flagged as "not available" rather than inferred when building the knowledge-base entry. Full-text access to the primary Circulation Research paper's tables/figures (patient-by-patient granular data, protein structural modeling) was not obtainable via the tools used here (paywalled/binary PDF); a curator with institutional journal access should verify granular table values directly against the primary source before final KB entry, per this repository's evidence-verification requirements.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 4 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMC:PMC10005133` (2 mentions) - Spectral and Redox Properties of a Recombinant Mouse Cytochrome b561 Protein Suggest Transmembrane Electron Transfer Function.
  - shared terms: cyb561

Weighed against this report's own most characteristic terms: `hypotension`, `orthostatic`, `cyb561`, `patient`, `disease`, `severe`, `norepinephrine`, `dbh`, `clinical`, `gene`, `hypoglycemia`, `autonomic`, `dopamine`, `primary`, `disorder`, `exist`, `genetic`, `identified`, `phenotype`, `deficiency`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.