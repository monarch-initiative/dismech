---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-12T04:05:21.159630'
end_time: '2026-10-12T04:07:01.081020'
duration_seconds: 99.92
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Crimean-Congo Hemorrhagic Fever
  mondo_id: MONDO:0020501
  category: Infectious
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
  - claude-haiku-5-5
  - claude-sonnet-5-5
  web_search_requests: 3
  num_turns: 5
  total_cost_usd: 0.8379712000000001
  session_id: c5bca049-79dd-565a-9d58-3e2354d3de80
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 8
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 1
  validator_version: 0.3.0
term_validation:
  total_terms: 45
  verified: 45
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 15
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0030138
    reported_labels:
    - Ecchymosis
    ontology_label: Excessive bleeding from superficial cuts
  - term_id: NCIT:C15747
    reported_labels:
    - verify
    ontology_label: Supportive Care
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Crimean-Congo Hemorrhagic Fever
- **MONDO ID:** MONDO:0020501 (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Crimean-Congo Hemorrhagic Fever** covering all of the
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

# Crimean-Congo Hemorrhagic Fever (CCHF): Research Report for the dismech Knowledge Base

**Provenance and verification status**

- I ran three web searches. They confirmed Bente et al. 2013 (PMID 23906741), Zivcec et al. 2016 (PMID 27110812), a 2021 systematic review of treatment, and CDC/ECDC/WHO-regional fact-sheet statements.
- Everything else comes from my background knowledge and is a lead, not a verified binding.
- **Every PMID other than the two above, and every ontology CURIE below, was written from memory and was not looked up.** Under the project rules, run `just fetch-reference` on each PMID and look up each CURIE (`runoak` or the cache) before binding it.
- I give no verbatim snippets, because I did not have abstract text to copy. Snippets must be taken from `references_cache/` after fetching.
- I did not run a 2023–2024 literature sweep. The anchors below are older reviews plus the search results, and newer primary work should be added.
- I gave no NCT numbers, because I could not verify any.

---

## 1. Disease Information

**Overview.** CCHF is an acute, often severe zoonotic viral hemorrhagic fever. It is caused by Crimean-Congo hemorrhagic fever orthonairovirus (CCHFV), a tick-borne virus. Its main vector and reservoir are *Hyalomma* ticks. Livestock act as amplifying hosts, and humans are infected by tick bite or contact with infected blood or tissue. Human-to-human nosocomial spread occurs. The disease was characterized in Crimea in 1944 and linked to the Congo in 1969 (CDC fact sheet, https://stacks.cdc.gov/view/cdc/24528).

**Identifiers.**
- The MONDO ID was supplied by the task as MONDO:0020501 and is unverified.
- I did not look up OMIM, Orphanet, ICD-10 (A98.0), ICD-11 or MeSH. The ICD-10 code is from memory. Look up the others.

**Synonyms.** Crimean hemorrhagic fever, Congo fever, Central Asian hemorrhagic fever, CCHF, Crimean-Congo haemorrhagic fever.

**Data origin.** The sources are aggregated disease-level literature and surveillance, not EHR.

**Entry-level classification (CLAUDE.md "Infectious Disease Entry Granularity").**
- CCHF is a single named pathogen–syndrome pair.
- It needs at least one NCBITaxon-bound `infectious_agent`, a `transmission` route list, `agent_life_cycle` with hosts and vectors, and a `progression:` list of phases.
- Regional clades (Africa 1–3, Europe 1–2, Asia 1–2, with the exact lineage names to be checked in the literature) are not a reason for `has_subtypes` unless documented to differ in presentation or severity. If they are kept lumped, use a `Deliberately lumped.` review note.

---

## 2. Etiology

**Causal agent.**
- CCHFV is a negative-sense, tripartite-RNA virus in the genus *Orthonairovirus*, family *Nairoviridae*, order *Bunyavirales*.
- NCBITaxon for the species is probably 1980519. Verify this.
- The three segments are:
  - **S**, encoding the nucleoprotein (N).
  - **M**, encoding the glycoprotein precursor, which is cleaved into Gn, Gc, GP38, the mucin-like domain and NSm.
  - **L**, encoding the RNA-dependent RNA polymerase, which carries an OTU-domain deubiquitinase/deISGylase activity.
- Reviews: Bente 2013 (PMID 23906741); Zivcec 2016 (PMID 27110812); a clinician-oriented review of virology, pathogenesis and pathology (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11060449/).

**Risk factors (environmental/occupational).**
- Exposure to *Hyalomma* ticks, and slaughtering or handling of viremic livestock. Farmers, abattoir workers, veterinarians and shepherds are at higher risk.
- Healthcare workers and family caregivers are exposed to blood and body fluids. Nosocomial spread has occurred through improper sterilization, reused needles and contaminated supplies (CDC sheet).
- Military and outdoor workers are exposed to tick bites.
- Outbreaks occur in the warm season, when tick activity is high, and around the Eid slaughter period. I recall this pattern, but no citation was retrieved.

**Genetic risk and protective factors.** No validated human susceptibility or protective variants are known to me. Host genetic studies exist, but I cannot cite them. Mark this as not available unless a literature sweep finds one.

**Protective factors.** Tick avoidance, repellents and protective clothing. Livestock acaricide use and PPE for care workers reduce exposure.

**Gene–environment interactions.** Not applicable or not established.

---

## 3. Phenotypes

The clinical course is classically divided into incubation, pre-hemorrhagic, hemorrhagic and convalescent phases. Typical figures:

- Incubation is about 1–3 days after a tick bite and about 5–6 days after contact with blood, with a maximum of about 13 days. This is from memory and should be confirmed in Bente 2013.
- Onset is sudden.
- The hemorrhagic phase starts around day 3–5.
- Death usually occurs on days 5–14 (CDC sheet, https://stacks.cdc.gov/view/cdc/24528).
- Frequencies below are rough qualitative bands from my recollection. Obtain quantitative values from cohort studies, such as the Turkish and Iranian series, and cite them.

| Phenotype | HP (verify) | Frequency | Phase |
|---|---|---|---|
| Fever | HP:0001945 | Very frequent | Pre-hemorrhagic |
| Headache | HP:0002315 | Frequent | Pre-hemorrhagic |
| Myalgia | HP:0003326 | Frequent | Pre-hemorrhagic |
| Nausea/vomiting | HP:0002018 / HP:0002013 | Frequent | Pre-hemorrhagic |
| Abdominal pain | HP:0002027 | Frequent | Pre-hemorrhagic |
| Diarrhea | HP:0002014 | Frequent | Pre-hemorrhagic |
| Thrombocytopenia | HP:0001873 | Very frequent | Lab |
| Leukopenia | HP:0001882 | Frequent | Lab |
| Elevated hepatic transaminases | HP:0002910 | Very frequent | Lab |
| Disseminated intravascular coagulation | HP:0005521 | Severe cases | Hemorrhagic |
| Petechiae | HP:0000967 | Frequent in severe cases | Hemorrhagic |
| Ecchymosis | HP:0030138 | Frequent in severe cases | Hemorrhagic |
| Epistaxis | HP:0000421 | Frequent in severe cases | Hemorrhagic |
| Gastrointestinal hemorrhage | HP:0002239 | Severe cases | Hemorrhagic |
| Hematuria | HP:0000790 | Severe cases | Hemorrhagic |
| Hepatomegaly | HP:0002240 | Occasional | |
| Splenomegaly | HP:0001744 | Occasional | |
| Hypotension / shock | HP:0002615 | Fatal cases | |
| Acute kidney injury | HP:0001919 | Severe cases | |
| Confusion | HP:0001289 | Occasional | |

Laboratory signs also include elevated AST, ALT, LDH and CK, and prolonged PT/aPTT. Bleeding often begins around illness day 4 and lasts about two weeks in severe cases (CDC sheet).

**Severity and progression.**
- The disease is acute, with a spectrum from subclinical or mild to fulminant.
- Hemorrhagic manifestations are not present in all cases.
- Convalescence can take weeks, with asthenia.

**Quality of life.** Post-recovery fatigue and weakness occur. I have no recalled quantitative QoL data. Mark as not available.

---

## 4. Genetic/Molecular Information

CCHF is not a heritable disorder. There are no causal human genes.

**Viral molecular features.**
- The glycoprotein precursor is processed by host proteases (SKI-1/S1P and furin).
- Reported host entry factors include LDLR, which I recall from a 2024 paper that I could not verify, and possibly nucleolin. Look up the primary papers.
- The L-protein OTU domain removes ubiquitin and ISG15 from host and viral proteins. This blunts the interferon (IFN) and NF-κB responses.
- N protein binds viral RNA to form ribonucleoprotein complexes.
- Viral phylogeny shows high diversity and segment reassortment.

**Host genetics.** No validated host variants. A host gene such as the IFN pathway genes could be annotated only as mechanism, not as causal.

**Epigenetic and chromosomal.** Not applicable.

---

## 5. Environmental Information

- **Infectious agent.** CCHFV (see section 2).
- **Vector.** *Hyalomma* ticks, mainly *H. marginatum* in Eurasia and *H. truncatum* in Africa. NCBITaxon IDs for the ticks need lookup; I do not trust my recall of them.
- **Hosts.** Livestock (cattle, sheep, goats) develop asymptomatic viremia. Wild small mammals and birds host immature ticks. Ostriches are a recognized susceptible host.
- **Climate and landscape.** Warming, land-use change and livestock movement are proposed drivers of range expansion into southern Europe. This claim needs a citation.
- **Environmental `triggers` / ECTO.** An exposure such as "tick bite" or "exposure to livestock blood" needs searches in ECTO. Do not assume a term exists; record the exact queries and results.

---

## 6. Mechanism / Pathophysiology

**Causal chain (inferred steps flagged).**

1. A *Hyalomma* tick bite, or contact with infected blood or tissue, introduces CCHFV into skin or mucosa.
2. The virus enters local dendritic cells, monocytes and macrophages through glycoprotein-mediated attachment and endocytosis. Receptor details are not settled (section 4).
3. These cells carry the virus to regional lymph nodes and then the bloodstream (primary viremia). This is the generally accepted model and is partly inferred from animal data.
4. The virus spreads to the liver, spleen, lymphoid tissue, and other organs. Hepatocytes, Kupffer cells and endothelial cells are major targets (Bente 2013; PMC11060449).
5. Viral antagonism of innate immunity, notably through the OTU deISGylase, allows high-level replication. This is supported by in vitro and mouse data. High viremia correlates with fatal outcome in human cohorts.
6. Infected antigen-presenting cells and endothelial cells release large amounts of pro-inflammatory mediators (IL-6, TNF-α, IL-10, IFN-γ, others). Fatal cases show a cytokine storm and an HLH-like state. This is supported by human data but is partly correlational.
7. Endothelial activation and damage increase vascular permeability. Platelets are consumed or become dysfunctional. Hepatic injury reduces clotting factor synthesis.
8. The result is DIC, thrombocytopenia, hemorrhage, and multi-organ failure, which lead to shock and death.
9. **Branch.** In survivors, adaptive immunity, with neutralizing and non-neutralizing antibodies and T cells, clears the virus during convalescence. Early rise of IgM and IgG correlates with survival. This is inferred from clinical cohort and animal data.

**Cell types (CL, verify).** Dendritic cell CL:0000451; macrophage CL:0000235; monocyte CL:0000576; hepatocyte CL:0000182; Kupffer cell CL:0000091; endothelial cell CL:0000115; platelet CL:0000233.

**GO candidates (verify).** Viral entry into host cell GO:0046718; inflammatory response GO:0006954; blood coagulation GO:0007596; apoptotic process GO:0006915. For IFN antagonism, search GO for the viral suppression-of-host-interferon-signaling terms.

**Omics.** Transcriptomic and proteomic studies of patient blood exist. I did not retrieve them and do not cite any here.

---

## 7. Anatomical Structures Affected

- **Primary organs.** Liver (UBERON:0002107), spleen (UBERON:0002106), lymph nodes (UBERON:0000029), blood vessels / endothelium (UBERON:0001981).
- **Secondary involvement.** Kidney (UBERON:0002113), lung (UBERON:0002048), adrenal gland (UBERON:0002369), skin (UBERON:0002097), gastrointestinal tract, and CNS in some cases.
- **Systems.** Hematologic, hepatic, vascular, renal, immune.
- **Pathology.** Hepatic necrosis, hemophagocytosis, and widespread hemorrhage are described. Cite a pathology source such as PMC11060449.
- **Lateralization.** Not applicable.

---

## 8. Temporal Development

- **Onset.** Acute, over 1–13 days after exposure, depending on route.
- **Phases.** Incubation → pre-hemorrhagic (about 1–7 days) → hemorrhagic (short, 2–3 days) → convalescence (about 10–20 days or more). Phase durations are from memory and need Bente 2013 to confirm.
- **Course.** Self-limited. Death, when it occurs, is usually days 5–14.
- **Critical periods.** Early antiviral treatment is thought to matter most. Evidence for this is weak (section 12).
- **Remission.** Spontaneous recovery in survivors. Reinfection is considered uncommon, but I have no citation.

---

## 9. Inheritance and Population

- **Not a genetic disease.** Inheritance fields are not applicable.
- **Geography.** Eastern Europe, the Mediterranean, northwestern China, central Asia, Africa, the Middle East and the Indian subcontinent (CDC sheet). Hyalomma ticks' range is wider than the range of recognized disease.
- **Countries with notable burden (from memory; add citations).** Turkey (hundreds to thousands of cases per year since its 2002 emergence), Iran, Pakistan, Afghanistan, Iraq, Russia, the Balkans, Uganda and South Africa. Spain and Greece have reported cases more recently.
- **Incidence and prevalence.** No reliable global figure. Use `measure_type: ANNUAL_INCIDENCE` with an explicit `rate_denominator`, and cite national surveillance sources.
- **Sex and age.** Most cases are in adult men with agricultural or occupational exposure. This is a recalled pattern; confirm with a cohort source.
- **Case-fatality.** Sources range widely: 2–50% in one fact sheet, 10–40% in a WHO regional sheet, and 26% to over 80% in untreated cases as cited by treatment reviews (search results above). The variation reflects the setting, case ascertainment and care quality. Record each as a separate prevalence-style source rather than averaging.

---

## 10. Diagnostics

- **Virological.**
  - RT-PCR is the main test in the acute phase.
  - Viral antigen detection and virus isolation are possible but require BSL-4 containment.
- **Serological.** IgM and IgG ELISA or immunofluorescence. IgM appears around day 5–7 and is usually absent in fatal cases. Confirm this against a source.
- **General laboratory.**
  - Thrombocytopenia, leukopenia, elevated AST/ALT/LDH/CK, and prolonged PT/aPTT.
  - Hypofibrinogenemia and elevated D-dimer in DIC.
  - For LOINC bindings, use the project's `just loinc-seed-cache` workflow. Do not type labels.
- **Severity scoring.** There are published severity scores that use platelet count, WBC, AST/ALT, aPTT and fibrinogen. A South African scheme dates from 1989. I cannot give its exact thresholds or PMID reliably.
- **Differential.** Other viral hemorrhagic fevers (Ebola, Lassa, Rift Valley fever, hantavirus), leptospirosis, rickettsioses, meningococcemia, malaria, TTP/HUS, sepsis with DIC, and tick-borne infections such as tularemia.
- **Genetic testing, imaging, biopsy.** Not applicable. Post-mortem pathology is possible with biosafety precautions.
- **Screening.** None for asymptomatic people. Contact tracing and monitoring apply after exposure.

---

## 11. Outcome/Prognosis

- **Mortality.** Varies by region and care, from low single digits in some well-resourced series to above 30–40% in others (see section 9). I am not confident about any single figure.
- **Prognostic factors reported in cohorts.** High viral load, high AST/ALT/LDH/CK, low platelets, prolonged coagulation times, advanced age, and early bleeding or neurologic signs. These are widely reported but need primary citations, such as Turkish and Iranian cohorts.
- **Complications.** Hemorrhage, shock, multi-organ failure, secondary infection, HLH-like syndrome.
- **Sequelae.** Prolonged asthenia, and reported hair loss, neuropathy and memory changes in some survivors. I have no citation.
- **Health care workers.** Nosocomial infections carry high mortality in some outbreaks.

---

## 12. Treatment

**Supportive care is the mainstay.** This includes fluid and electrolyte management, replacement of platelets, plasma and red cells according to bleeding and DIC, organ support, and early ICU care. NCIT: Supportive Care NCIT:C15747 (verify).

**Antivirals.**
- **Ribavirin** is used widely. A 2021 systematic review found that some studies confirmed clinical efficacy and others did not, and concluded that efficacy is questionable and randomized trials are needed (https://brieflands.com/articles/iji-113427). The search surfaced a meta-analysis (Arab-Bafrani et al.) reporting reduced mortality, but I could not verify it. CHEBI for ribavirin is probably CHEBI:63580; verify. NCIT treatment_term would be Pharmacotherapy (NCIT:C15986) with `therapeutic_agent`.
- **Favipiravir** is called promising in reviews but unproven in humans (same review). A mouse study found favipiravir and ribavirin protected immunocompetent mice from lethal CCHFV infection, even when treatment was delayed. Mark this as `MODEL_ORGANISM`.
- **Convalescent plasma / immunoglobulin** has been used. A CDC-style sheet mentions ribavirin early plus convalescent plasma. Evidence is limited.
- **Monoclonal antibodies** targeting GP38 and Gn/Gc show protection in animals. This is a research stage and should be recorded as experimental.

**Clinical trials.** I have not searched ClinicalTrials.gov, ICTRP or other registries, and I give no identifiers. Run `just fetch-reference` on any NCT you find.

**Vaccines.** A Bulgarian inactivated vaccine derived from suckling-mouse brain is used locally. There is no widely licensed vaccine. Candidate platforms (MVA, adenovirus, DNA, mRNA) are preclinical or early clinical, per my recollection. Cite primary papers after a search. The WHO R&D Blueprint priority listing needs verifying.

**Pharmacogenomics.** Not applicable.

---

## 13. Prevention

- **Primary.** Avoid tick habitats. Use repellents and long clothing, inspect the body and remove ticks promptly. Use acaricides on livestock, and wear gloves and protective gear when handling animals. Observe appropriate slaughter and meat-handling practice.
- **Healthcare.** Standard and contact/droplet precautions and PPE. Safe handling of needles and sharps, and safe laboratory handling of specimens.
- **Post-exposure prophylaxis.** Oral ribavirin has been used for high-risk exposures, but evidence is limited.
- **Public health.** Surveillance, One Health collaboration among human and veterinary sectors, and safe burial practices.
- **Secondary and tertiary.** Early recognition and referral. Genetic counseling and genetic screening are not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy.** Humans (NCBITaxon:9606). Cattle, sheep, goats and other livestock are asymptomatic hosts. Hares, hedgehogs and small mammals carry immature ticks. Ostriches are susceptible. Look up the taxon IDs.
- **Vector taxa.** *Hyalomma marginatum*, *H. truncatum*, and other *Hyalomma* species. *Rhipicephalus* and other genera may also be involved. Look up the taxon IDs.
- **Veterinary relevance.** Animals rarely show disease. They are important as amplifiers and as sentinels in seroprevalence surveys. OMIA is for inherited disease and is not applicable.
- **Zoonosis.** Yes. Humans are incidental hosts.
- **Comparative biology.** Tick-borne transmission and persistence in tick populations, including transstadial and transovarial transmission, explain endemicity. Cite from Bente 2013.

---

## 15. Model Organisms

- **Mouse.**
  - Wild-type adult mice are resistant to lethal infection.
  - Mice lacking the type I IFN receptor (*Ifnar*−/−) or STAT-1 develop lethal, hemorrhagic-type disease. Humanized and immunocompromised models also exist. These details are from memory, so cite primary papers.
  - Immunocompetent mice treated with antibody against IFNAR have been used. The favipiravir and ribavirin study above used an immunocompetent mouse model.
- **Nonhuman primates.** Cynomolgus macaques develop infection with mild or no disease, in contrast to severe human disease. I recall a model of this type, but I cannot verify the citation.
- **Other.** Hamster and guinea pig models are reported, and cell lines such as SW-13 and Huh7 are widely used. Tick cell lines are used for tick–virus work.
- **Limitations.** Immunocompetent small animals do not reproduce the human course, so IFN-deficient models bias toward immune-evasion questions. The mismatch could be recorded as a `HUMAN_MODEL_MISMATCH` discussion, and `evidence_source` for these studies is `MODEL_ORGANISM`.
- **Resources.** MGI and IMPC lines for *Ifnar1* and *Stat1* knockouts. Cellosaurus for cell lines.

---

## Suggested next steps for curation

1. Run `just fetch-reference` for PMIDs 23906741 and 27110812, then for the PMC reviews found above, and take every snippet from the cached text.
2. Run a PubMed sweep for 2022–2026: cohorts with quantitative symptom and lab frequencies, the LDLR receptor work, favipiravir and ribavirin trials, and vaccine and monoclonal antibody candidates.
3. Look up every CURIE above (HP, CL, UBERON, GO, CHEBI, NCIT, NCBITaxon, MONDO) before use.
4. Run the ECTO searches for tick-bite and livestock exposures and record the queries and results.
5. Add the phase list under `progression:` and the `infectious_agent`, `transmission` and `agent_life_cycle` blocks. Check `kb/modules/` for a fitting hemorrhagic or endothelial-dysfunction module before writing nodes.

## Sources

- [Bente et al. 2013, Antiviral Research 100(1):159–189, PMID 23906741](https://w3id.org/oc/corpus/be/4804766) (bibliographic details only)
- [Zivcec et al. 2016, Viruses, PMID 27110812](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4848600) (identified in the search; I did not confirm the PMC link maps to this paper)
- [CCHFV for Clinicians: Virology, Pathogenesis, and Pathology](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11060449/)
- [CCHFV: Current Advances and Future Prospects of Antiviral Strategies](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8310003/)
- [Systematic review of treatment strategies in CCHF, Int J Infect](https://brieflands.com/articles/iji-113427)
- [Favipiravir and ribavirin protect immunocompetent mice from lethal CCHFV infection](https://www.medchemexpress.com/publications/37611878.html)
- [CDC CCHF fact sheet](https://stacks.cdc.gov/view/cdc/24528)
- [ECDC CCHF factsheet for healthcare professionals](https://www.ecdc.europa.eu/en/node/16562)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 45 |
| Resolved | 45 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 20 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0030138` (1 mention) - the report calls it "Ecchymosis"; HP calls it **Excessive bleeding from superficial cuts**
- `NCIT:C15747` (1 mention) - the report calls it "verify"; NCIT calls it **Supportive Care**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001882` (1 mention) - the report calls it "Leukopenia"; HP calls it **Decreased total leukocyte count**, and lists "Leukopenia" among its other names
- `HP:0002910` (1 mention) - the report calls it "Elevated hepatic transaminases"; HP calls it **Elevated circulating hepatic transaminase concentration**, and lists "Elevated transaminases" among its other names
- `HP:0002615` (1 mention) - the report calls it "Hypotension / shock"; HP calls it **Hypotension**