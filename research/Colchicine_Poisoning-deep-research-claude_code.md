---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-09-01T18:28:14.195142'
end_time: '2026-09-01T18:46:24.007644'
duration_seconds: 1089.81
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Colchicine Poisoning
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-5
  web_search_requests: 6
  num_turns: 48
  total_cost_usd: 4.93412575
  session_id: ea483a32-bfd7-4a9a-bfe7-821590923101
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  - Write
  assistant_text_blocks: 2
citation_count: 10
reference_validation:
  total_references: 59
  verified: 59
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 59
  on_topic: 41
  validator_version: 0.2.1
term_validation:
  total_terms: 93
  verified: 86
  not_found: 0
  obsolete: 0
  unverifiable: 7
  confabulation_rate: 0.0
  labels_checked: 19
  labels_matching: 18
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0017859
    reported_labels:
    - MONDO
    ontology_label: colchicine poisoning
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Colchicine Poisoning
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Colchicine Poisoning** covering all of the
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

I will research colchicine poisoning and write the report inline.

# Colchicine Poisoning — Research Report

**Prepared:** 2026-09-01. **Target:** Colchicine Poisoning. **MONDO:** `MONDO:0017859` (verified against OLS4; label `colchicine poisoning`). **Category:** Complex / toxic exposure disorder.

**Scope note.** This is a toxic exposure disorder, not a Mendelian disease. Sections 4 and 9 are therefore reframed: there are no causal genes, and the genetic content that exists is host pharmacogenetics governing colchicine disposition. Where a template item does not apply, I say so rather than filling it.

**Ontology note.** Every CURIE below was resolved against the EBI Ontology Lookup Service (OLS4) on 2026-09-01 and the returned label is the one printed. Four suggested NCI Thesaurus concepts did not resolve by exact label and are flagged as unresolved. A term resolving is not the same as a term being right for the claim; treat these as leads.

---

## 1. Disease Information

Colchicine poisoning is systemic multi-organ injury caused by exposure to colchicine, a tricyclic lipid-soluble alkaloid of *Colchicum autumnale* and *Gloriosa superba*. It follows deliberate self-poisoning, accidental ingestion of the plant, dosing error, or accumulation when clearance falls. The drug has a narrow therapeutic index and no antidote in routine clinical use.

MONDO's own definition: *"A potentially life-threatening condition from ingesting colchicine drug or Colchicum autumnale plant. It begins with gastrointestinal symptoms causing severe dehydration, progresses to marrow failure within 24 hours, and can result in multi-organ failure including renal failure, cardiac arrest, and shock within 1-3 days."*

### Identifiers

| Vocabulary | Identifier | Note |
|---|---|---|
| MONDO | `MONDO:0017859` | verified, label `colchicine poisoning` |
| Orphanet | `ORPHA:31824` | from MONDO xrefs |
| SNOMED CT | `24354007` | from MONDO xrefs |
| ICD-9-CM | `974.7` | from MONDO xrefs |
| ICD-11 (foundation) | `1617857912` | from MONDO xrefs |
| ICD-10-CM | `T50.4X1A` – `T50.4X4A` (poisoning, by intent); `T50.4X5A` (adverse effect) | "Drugs affecting uric acid metabolism". Crosswalked from ICD-9 974.7. I could not open the ICD-10-CM Table of Drugs page directly (HTTP 403), so the colchicine index entry is inferred, not confirmed. |
| MeSH | `D003078` (Colchicine), subheading `/poisoning` | verified via NCBI E-utilities. There is no colchicine-poisoning descriptor; the concept is drug + subheading. |
| CHEBI (agent) | `CHEBI:23359` colchicine | verified |
| NCIT (agent) | `NCIT:C385` Colchicine | verified |
| OMIM | not applicable | no Mendelian entry; this is an exposure |

**Synonyms:** colchicine toxicity, colchicine intoxication, colchicine overdose, autumn crocus poisoning, meadow saffron poisoning, *Colchicum autumnale* poisoning, *Gloriosa superba* poisoning ("niyangala" poisoning, Sri Lanka), colchicine toxicosis (veterinary).

**Data provenance.** Both. Individual-patient sources dominate the literature (case reports, poison-centre call records, ICU registries). Aggregated disease-level resources contribute the ontology mappings and the national poison-centre denominators. The largest patient-level series are the Sri Lankan *Gloriosa* cohort (n = 297, PMID:30888889), the Turkish paediatric ICU cohort (n = 150, PMID:42499431), the UK paediatric NPIS series (n = 57, PMID:41663238), the Hong Kong clarithromycin co-prescription study (n = 116, PMID:16007523), and a Chinese acute-poisoning series (n = 43, PMID:34484680).

---

## 2. Etiology

### Causal factor

One molecule. Colchicine binds tubulin and blocks microtubule assembly. Everything downstream is that lesion propagating through tissues ranked by how much they need microtubules.

Finkelstein et al. state it plainly (PMID:20586571): *"Colchicine's toxicity is an extension of its mechanism of action - binding to tubulin and disrupting the microtubular network."*

Routes of exposure:

1. **Deliberate self-poisoning** with tablets or with plant material. In the Sri Lankan series, *Gloriosa superba* self-poisoning was the dominant presentation (PMID:30888889).
2. **Accidental plant ingestion.** *Colchicum autumnale* leaves mistaken for wild garlic (*Allium ursinum*) — a documented and recurrent European error (PMID:42043136). *Gloriosa superba* tubers mistaken for ginger (PMID:41628608).
3. **Therapeutic dosing error**, including iatrogenic tenfold overdose (PMID:33898365, a 4-year-old given 0.5 mg/kg).
4. **Accumulation at therapeutic dose** when renal or hepatic clearance falls, or a CYP3A4/P-glycoprotein inhibitor is co-prescribed. This is the commonest fatal mechanism in older patients and produces the chronic neuromyopathic phenotype rather than the acute one.

### Risk factors — environmental and clinical

| Factor | Evidence | Source |
|---|---|---|
| Ingested dose > 0.5 mg/kg | *"High fatality rate was reported after acute ingestions exceeding 0.5 mg/kg. The lowest reported lethal doses of oral colchicine are 7-26 mg."* | PMID:20586571 |
| Dose ≥ 0.8 mg/kg | Survival 28.60% in that band, vs 83.33% at 0.5–0.8 mg/kg and 100% at ≤ 0.5 mg/kg (n = 43) | PMID:34484680 |
| Renal impairment | Independent predictor of death with clarithromycin co-therapy (RR 9.1; 95% CI 1.75–47.06; P < 0.001) | PMID:16007523 |
| Hepatic impairment | Blocks the primary elimination route; the plateau in a poisoned child's blood level was attributed to liver failure | PMID:33898365 |
| CYP3A4 + P-gp inhibitor co-prescription | 9/88 (10.2%) died on concomitant clarithromycin vs 1/28 (3.6%) sequential | PMID:16007523 |
| Any CYP3A4/P-gp inhibitor (FAERS signal) | 37 reporting-odds-ratio and 34 observed/expected safety signals; strongest ROR colchicine + atazanavir with rhabdomyolysis/myopathy, ROR 35.4 (95% CI 12.8–97.6) | PMID:36688283 |
| Statin co-therapy | Statin use was a significant covariate on colchicine clearance in a population PK model; risk concentrated in low-body-weight patients | PMID:40719983 |
| Older age | Median colchicine concentration 4.7 ng/mL (IQR 1.7–6.6) in those over 65 vs 1.2 (IQR 0.2–2.7) under 35 | PMID:30888889 |
| Low body weight | Body weight was a significant predictor of colchicine PK | PMID:40719983 |
| Delayed presentation | *"Delayed presentation, pre-existing renal or liver impairment are associated with poor prognosis."* | PMID:20586571 |
| Polypharmacy, advanced age | Named risk group in the 2026 review | PMID:42618164 |
| Long duration of therapy | 48% of neuromyopathy cases had taken colchicine > 12 months before presenting | PMID:36512928 |

Named interacting drugs (PMID:20586571): *"CYP 3A4 and P-glycoprotein inhibitors, such as clarithromycin, erythromycin, ketoconazole, ciclosporin, and natural grapefruit juice can increase colchicine concentrations. Co-administration with statins may increase the risk of myopathy."* CHEBI leads: clarithromycin `CHEBI:3732` (verified), atorvastatin `CHEBI:39548` (verified).

### Genetic risk factors

There is no disease-causing genotype. There is a transporter genotype that modulates exposure.

- **ABCB1** (`HGNC:40`, P-glycoprotein) is the efflux transporter that limits colchicine absorption and drives biliary/renal efflux. A 2025 systematic review concluded that *"P-glycoprotein is considered a key transporter protein as it regulates the absorption, distribution, and excretion of several drugs, including colchicine. In diseases like FMF, ABCB1 polymorphisms have been shown to affect the response to colchicine, potentially leading to treatment resistance or altered toxicity"* (PMID:40136464).
- A two-case series with muscle transcript data reported *"the descriptive finding of reduced ABCB1 transcript levels in the colchicine myopathy patients"* (PMID:31178824). Both cases were on rosuvastatin. That is descriptive, n = 2, and hypothesis-generating.
- **CYP3A4** (`HGNC:2637`) and **CYP3A5** (`HGNC:2638`) are the metabolic route. I found no adequately powered study linking a CYP3A5 expressor genotype to colchicine toxicity risk. Stated as absence of evidence, not evidence of absence.

**Assessment.** No validated pharmacogenetic test guides colchicine dosing today. CPIC has no colchicine guideline that I located. The tractable genetic risk story is ABCB1 expression, and it is not yet actionable.

### Protective factors

- **Genetic:** none identified.
- **Environmental / clinical:** early presentation and early gastrointestinal decontamination. Recovery followed presentation one hour after a 1.38 mg/kg ingestion, against a fatal outcome at 0.39–0.65 mg/kg presenting at 44 hours (both discussed in PMID:34229452). Dose reduction in renal or hepatic impairment. Avoiding CYP3A4/P-gp inhibitor co-prescription outright: *"these 2 drugs should not be coprescribed, because of the risk of fatality"* (PMID:16007523).
- Restarting colchicine at reduced dose after neuromyopathy was usually tolerated — 73% had no symptom recurrence in 15 rechallenged cases (PMID:36512928).

### Gene–environment interaction

The interaction is pharmacokinetic and it is the core of the disease. A patient with reduced ABCB1 function, or a CYP3A4 inhibitor on board, or a failing kidney, converts a therapeutic dose into a toxic exposure without any change in what was swallowed. The Hong Kong data quantify one arm of it (PMID:16007523). The FAERS disproportionality analysis maps the drug space (PMID:36688283). The genotype arm is characterised but not quantified (PMID:40136464).

---

## 3. Phenotypes

Colchicine poisoning runs in three overlapping phases. Finkelstein et al. define them (PMID:20586571): *"Colchicine poisoning presents in three sequential and usually overlapping phases: 1) 10-24 h after ingestion - gastrointestinal phase mimicking gastroenteritis may be absent after intravenous administration; 2) 24 h to 7 days after ingestion - multi-organ dysfunction. Death results from rapidly progressive multi-organ failure and sepsis."*

### Phase 1 — gastrointestinal (0–24 h)

| Phenotype | HPO suggestion (verified label) | Frequency / note |
|---|---|---|
| Nausea and vomiting | `HP:0002018` Nausea; `HP:0002013` Vomiting | 64.7% of 150 paediatric cases (PMID:42499431) |
| Abdominal pain | `HP:0002027` Abdominal pain | 36.7% (PMID:42499431) |
| Diarrhea | `HP:0002014` Diarrhea | 24% paediatric (PMID:42499431); universal in experimentally poisoned calves (PMID:9764409) |
| Leukocytosis | `HP:0001974` Leukocytosis | Early, and a diagnostic trap — it reads as sepsis |
| Hypotension / hypovolaemic shock | `HP:0002615` Hypotension | From fluid and electrolyte loss |
| Lactic acidosis | `HP:0003128` Lactic acidosis | Part of the named toxidrome |

The toxidrome to recognise (PMID:20586571): *"Colchicine poisoning should be suspected in patients with access to the drug and the typical toxidrome (gastroenteritis, hypotension, lactic acidosis, and prerenal azotemia)."*

**Severity/progression:** acute onset, self-limited in mild exposure, or the opening of a fatal course. Around half of UK paediatric cases were symptomatic at presentation, gastrointestinal upset in 39% (PMID:41663238). Asymptomatic presentation does not exclude later systemic toxicity — the UK authors state exactly that.

### Phase 2 — multi-organ dysfunction (24 h – 7 days)

| Phenotype | HPO suggestion | Frequency / note |
|---|---|---|
| Pancytopenia | `HP:0001876` Pancytopenia | The defining haematological lesion |
| Neutropenia | `HP:0001875` Neutropenia | Grade 4 reported (PMID:36319015) |
| Thrombocytopenia | `HP:0001873` Thrombocytopenia | Nadir 13 × 10⁹/L in one ECLS survivor (PMID:26230148) |
| Anemia | `HP:0001903` Anemia | Grade 2 upward (PMID:36319015) |
| Bone marrow hypocellularity | `HP:0005528` Bone marrow hypocellularity | Structural correlate |
| Disseminated intravascular coagulation | `HP:0005521` Disseminated intravascular coagulation | Coagulation system most frequently affected in paediatric MODS, 26% (PMID:42499431) |
| Acute kidney injury | `HP:0001919` Acute kidney injury | Only mild AKI after *Gloriosa* ingestion (PMID:30888889); severe and dialysis-refractory in tablet overdose (PMID:34229452) |
| Elevated hepatic transaminase | `HP:0002910` Elevated hepatic transaminase | AST an independent MODS predictor (PMID:42499431) |
| Hepatic failure | `HP:0001399` Hepatic failure | Centrilobular necrosis at autopsy (PMID:37222938) |
| Rhabdomyolysis | `HP:0003201` Rhabdomyolysis | Mild after *Gloriosa*; marked in tablet overdose |
| Elevated creatine kinase | `HP:0003236` Elevated circulating creatine kinase activity | Kuncl: *"always presents with elevation of serum creatine kinase"* (PMID:3035372) |
| Cardiac arrhythmia | `HP:0011675` Arrhythmia | Second-degree AV block documented in a poisoned dog (PMID:31883205) |
| Cardiac arrest | `HP:0001695` Cardiac arrest | A leading terminal event |
| Respiratory distress / hypoxemia | `HP:0002098` Respiratory distress; `HP:0012418` Hypoxemia | ARDS reported (PMID:9786547) |
| Hypocalcemia | `HP:0002901` Hypocalcemia | (PMID:9786547, PMID:34229452) |
| Hyponatremia | `HP:0002902` Hyponatremia | Including SIADH after *Gloriosa* |
| Hypoglycemia | `HP:0001943` Hypoglycemia | Refractory in one fatal case (PMID:34229452) |
| Seizure | `HP:0001250` Seizure | With encephalopathy from cerebral oedema |
| Sepsis | `HP:0100806` Sepsis | Death route via neutropenia; *Candida dubliniensis* isolated post mortem in one case (PMID:34229452) |

Cardiovascular collapse, not marrow failure, is the usual proximate cause of death in acute oral poisoning — a claim carried in the Cozza review and worth flagging as a review-level statement rather than a primary result. The Chinese series is the primary support: *"The causes of death were cardiovascular and bone marrow hematopoietic failures"* (PMID:34484680).

### Phase 3 — recovery (7–21 days)

| Phenotype | HPO suggestion | Note |
|---|---|---|
| Rebound leukocytosis | `HP:0001974` Leukocytosis | Marrow escape |
| Alopecia | `HP:0001596` Alopecia | Days 5–16 post ingestion; historically documented as alopecia totalis after suicidal overdose (PMID:14164521) |

Finkelstein: *"Recovery typically occurs within a few weeks of ingestion, and is generally a complete recovery barring complications of the acute illness"* (PMID:20586571).

### Chronic / therapeutic-dose phenotype: colchicine neuromyopathy

A separate clock, a separate presentation, and misdiagnosed more often than not. Kuncl's 1987 description remains canonical (PMID:3035372): *"It usually presents with proximal weakness and always presents with elevation of serum creatine kinase; both features remit within three to four weeks after the drug is discontinued. The accompanying axonal polyneuropathy is mild and resolves slowly."* And: *"colchicine myoneuropathy is usually misdiagnosed initially, either as probable polymyositis or as uremic neuropathy."*

| Phenotype | HPO suggestion | Frequency |
|---|---|---|
| Proximal muscle weakness | `HP:0003701` Proximal muscle weakness | Predominant symptom in 143 reviewed cases (PMID:36512928) |
| Myopathy (vacuolar) | `HP:0003198` Myopathy | Lysosome/autophagic-vacuole accumulation (PMID:3035372); imaged and re-reported 2019–2025 (PMID:31819001, PMID:39870408) |
| Peripheral axonal neuropathy | `HP:0003477` Peripheral axonal neuropathy | Combined neuropathy + myopathy in 72/143 (51%) (PMID:36512928) |

Mean total daily dose in the neuromyopathy series was 1.25 ± 0.60 mg — ordinary therapeutic dosing (PMID:36512928). 117/143 (82%) had a significant comorbidity or a probable drug–drug interaction; 57 (40%) had both. Cessation gave complete resolution in 70% of cases at a median of 21 days.

### Quality of life

I found no colchicine-poisoning-specific EQ-5D, SF-36, or PROMIS data. Stated as a gap. Functional impact is inferable per phenotype: neuromyopathy causes reversible proximal weakness with a median 21-day resolution (PMID:36512928); acute survivors of the multi-organ phase carry ICU-course morbidity (dialysis, ventilation, transfusion burden — 15 red-cell, 13 platelet, and 7 plasma units in one survivor, PMID:26230148); alopecia is cosmetic and reversible.

---

## 4. Genetic / Molecular Information

**Causal genes: none.** This is an exposure disorder. There is no pathogenic variant, no variant classification, no allele frequency, no somatic/germline distinction, no chromosomal abnormality, and no epigenetic disease mechanism to report. Any KB entry should record these as *not applicable* rather than empty.

What genetics does contribute:

**Host disposition genes.**

| Gene | HGNC (verified) | Role |
|---|---|---|
| ABCB1 | `HGNC:40` | P-glycoprotein efflux; polymorphism alters colchicine exposure and toxicity risk (PMID:40136464, PMID:31178824) |
| CYP3A4 | `HGNC:2637` | Principal oxidative metabolism (PMID:29359661) |
| CYP3A5 | `HGNC:2638` | Same subfamily; no colchicine-specific toxicity association found |

**Drug target genes.** Colchicine's target is the αβ-tubulin heterodimer. Representative human genes: TUBA1A `HGNC:20766`, TUBB `HGNC:20778`. Note this is a *drug target*, not a disease gene — the binding site is intact wild-type tubulin, and that is precisely why the poisoning is universal rather than genotype-restricted.

**Therapy-relevant gene.** CSF3 `HGNC:2438` (colony stimulating factor 3) is the gene product administered as filgrastim in the rescue of the marrow phase.

**Chromosomal effects — a genuine molecular finding, and a real one.** Colchicine is a spindle poison, so it produces aneugenic effects. Chromosomal aberrations have been tracked serially alongside marrow suppression in acute human poisoning (PMID:35237367; title and journal confirmed, abstract not indexed in PubMed, so I have not read the numbers). This is a downstream consequence of the exposure, not an inherited abnormality.

**Epigenetics:** no colchicine-poisoning methylation or chromatin dataset located in ENCODE, Roadmap, or the literature search. Gap.

---

## 5. Environmental Information

**The exposure is the disease.** Suggested ECTO-style framing: exposure to colchicine via ingestion; exposure to *Colchicum autumnale* plant material via ingestion; exposure to *Gloriosa superba* tuber via ingestion. I did not resolve ECTO CURIEs for these and will not guess them — the correct move is an ECTO search at curation time, and recording the absence in `notes` if nothing fits.

**Plant sources.** *Colchicum autumnale* (autumn crocus, meadow saffron) and *Gloriosa superba* (glory lily, "niyangala"). The 2018 pharmacology review calls colchicine *"a tricyclic, lipid-soluble alkaloid derived from the plant of the Lily family Colchicum autumnale, sometimes called the 'autumn crocus'"* (PMID:29359661). Cattle poisoning material additionally contained demecolcine alongside colchicine (PMID:9764409).

**Occupational / agricultural.** Livestock exposure from mown meadow forage. A Swiss organic dairy herd showed apathy, hypothermia, and reduced milk yield after eating cut forage containing autumn crocus leaves, and bulk milk tested positive for colchicine by LC-MS/MS two weeks after the event, negative at five weeks (PMID:40905265). That makes colchicine a food-chain hazard as well as a clinical one.

**Lifestyle factors.** Grapefruit juice is a named CYP3A4 inhibitor raising colchicine concentration (PMID:20586571). Alcohol appears in chronic-toxicity case narratives as a comorbid factor (PMID:35047617). Foraging for wild garlic is the specific behaviour behind European accidental plant poisoning (PMID:42043136).

**Infectious agents.** None cause this disease. Infection enters as a *consequence*: neutropenic sepsis is a death route (PMID:20586571, PMID:34229452). There is a second, inverse relationship worth noting — colchicine is being studied *against* NLRP3-driven inflammation in COVID-19 and influenza, which puts more colchicine into more hands and widens the exposed population (PMID:42589484).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Colchicine is absorbed from the gut and enters cells.** It is lipid-soluble and distributes widely, with an apparent volume of distribution of 4.87 ± 2.05 L/kg in patients with normal renal function (PMID:8035398). Absorption and efflux are gated by P-glycoprotein; metabolism is hepatic via CYP3A4 (PMID:29359661). **Leads to** an intracellular colchicine burden, highest in myeloid cells, which preferentially accumulate the drug (PMID:42589484).
2. **Intracellular colchicine binds the αβ-tubulin heterodimer at the colchicine site.** Ravelli et al. determined the structure at 3.5 Å and state the mechanism: *"the tubulin-colchicine complex sheds light on the mechanism of colchicine's activity: we show that colchicine binds at a location where it prevents curved tubulin from adopting a straight structure, which inhibits assembly"* (PMID:15014504). GO leads: `GO:0015631` tubulin binding, `GO:0008017` microtubule binding. **Leads to** step 3.
3. **Tubulin is locked in the curved conformation and cannot polymerise.** Loss of lateral contacts between protofilaments follows. **Leads to** net microtubule depolymerisation. GO: `GO:0046785` microtubule polymerization (blocked), `GO:0007017` microtubule-based process, `GO:0005874` microtubule (cellular component).
4. **The microtubule network collapses in every cell that has taken up drug.** The consequence list is enumerated by Finkelstein et al. (PMID:20586571): *"affected cells experience impaired protein assembly, decreased endocytosis and exocytosis, altered cell morphology, decreased cellular motility, arrest of mitosis, and interrupted cardiac myocyte conduction and contractility."* GO: `GO:0006887` exocytosis, `GO:0006897` endocytosis, `GO:0008088` axo-dendritic transport, `GO:0005819` spindle. **The chain branches here.** Four branches follow, on different clocks.

**Branch A — mitotic arrest in rapidly dividing tissue (hours to days; the lethal branch).**

5a. Spindle assembly fails in cells attempting mitosis. GO: `GO:0007052` mitotic spindle organization, `GO:0000278` mitotic cell cycle, `GO:0051301` cell division. **Leads to** metaphase arrest.
6a. Arrested cells die by apoptosis. This is directly demonstrated, not inferred. Experimental *Colchicum* poisoning in cattle showed *"cellular injury caused by autumn crocus was closely associated with apoptosis"* by in-situ DNA strand-break analysis and electron microscopy (PMID:10458107, MODEL_ORGANISM). In mice, colchicine raised duodenal crypt apoptotic indices with the highest values in the deepest crypt regions (PMID:15865323, MODEL_ORGANISM). GO: `GO:0006915` apoptotic process.
7a. **Gut arm:** intestinal crypt enterocytes (`CL:0000584` enterocyte) die, the mucosal barrier is lost, and secretory diarrhoea with massive fluid and electrolyte loss follows. Calf histology confirms the target: *"necrosis and degeneration with karyopyknosis and karyorrhexis were shown in the basal cell layer of the tongue, esophagus, forestomach, renal pelvis, urinary bladder, neck cell layer of the abomasal gastric glands, and intestinal cryps"* (PMID:9764409). **Leads to** hypovolaemia, hypotension, lactic acidosis, prerenal azotemia — phase 1.
8a. **Marrow arm:** haematopoietic progenitors (`CL:0000037` hematopoietic stem cell, `CL:0000763` myeloid cell, `CL:0000556` megakaryocyte) arrest and die in `UBERON:0002371` bone marrow. **Leads to** pancytopenia at 24 h to 7 days, with neutropenia the dangerous component. **Leads to** neutropenic sepsis and bleeding.

**Branch B — cardiac (hours to days; the usual proximate cause of death in acute overdose).**

5b. Microtubule disruption interferes with cardiac myocyte (`CL:0000746` cardiac muscle cell) conduction and contractility (PMID:20586571). A 2024 case report puts it as *"Direct cellular toxicity interferes with myocardial contractility, leading to cardiovascular collapse"* (PMID:39484332). **Leads to** arrhythmia, reduced ejection fraction, refractory cardiogenic shock. Ejection fraction fell to 5–10% in one survivor before extracorporeal support (PMID:26230148). **Leads to** cardiac arrest.

**Branch C — neuromuscular (weeks to years; the therapeutic-dose branch).**

5c. Microtubule-dependent intracellular transport fails in muscle and in long axons (`CL:0000540` neuron; `UBERON:0001630` muscle organ; `UBERON:0001021` nerve). Kuncl inferred the mechanism from morphology: *"The morphologic changes in muscle suggest that the pathogenesis involves disruption of a microtubule-dependent cytoskeletal network that interacts with lysosomes"* (PMID:3035372). GO: `GO:0005764` lysosome, `GO:0006914` autophagy. **This step is explicitly inferred, not demonstrated.**
6c. Lysosomes and autophagic vacuoles accumulate. **Leads to** vacuolar myopathy with proximal weakness and elevated creatine kinase, plus a slower axonal polyneuropathy. Reversible on withdrawal.

**Branch D — hepatic, renal, and the feedback loop.**

5d. Hepatocyte (`CL:0000182` hepatocyte, `UBERON:0002107` liver) injury and renal tubular injury (`UBERON:0002113` kidney) occur, with centrilobular hepatic necrosis at autopsy (PMID:37222938).
6d. **This closes a positive feedback loop.** Colchicine's principal elimination is hepatic with enterohepatic recirculation and 10–30% renal (PMID:33898365). Damaging both organs slows clearance of the poison damaging them. Cozza et al. make the point directly: *"With our patient having both liver and kidneys impairment, this could have led to his progression of MOF"* (PMID:34229452). Toxicokinetic confirmation: blood colchicine plateaued for six days in a poisoned child, *"indicating impeded elimination resulting from liver failure"* (PMID:33898365).

7. **Convergence:** hypovolaemia, cardiogenic shock, pancytopenia, coagulopathy, and impaired clearance converge on multi-organ dysfunction syndrome and death. Recovery, when it comes, follows the reverse order of organ involvement — *"the order of organ damage was digestive tract, coagulation, muscle, heart, hematopoietic, lung, liver, and kidney, while the recovery order was digestive tract, coagulation, heart, hematopoietic, lung, muscle, kidney, and liver"* (PMID:34484680).

### The therapeutic mechanism is the same lesion, dialled down

At therapeutic dose the same tubulin binding produces the anti-inflammatory effect: *"Colchicine interferes with several inflammatory pathways including adhesion and recruitment of neutrophils, superoxide production, inflammasome activation, the RhoA/Rho effector kinase (ROCK) pathway and the tumor necrosis factor alpha (TNF-α) -induced nuclear factor κΒ (NF-κΒ) pathway attenuating the inflammatory response"* (PMID:29359661). GO leads: `GO:0030595` leukocyte chemotaxis, `GO:0072559` NLRP3 inflammasome complex. There is no separate toxic mechanism to find. The therapeutic window is quantitative, which is exactly why it is narrow.

### Multi-omics

- **Transcriptomics:** the only disease-relevant human transcript measurement I found is reduced ABCB1 transcript in muscle from two colchicine-myopathy patients (PMID:31178824). No GEO series specific to colchicine poisoning was located.
- **Proteomics / metabolomics / lipidomics / single-cell / spatial:** none located for this disorder. Gaps.
- **Biomarker panel work (the closest thing to omics here):** the Sri Lankan study measured serum creatinine, cystatin C, creatine kinase, and urinary KIM-1, clusterin, albumin, β2-microglobulin, cystatin C, NGAL, osteopontin, and trefoil factor 3 in 45 patients, and concluded *"Ingestion of Gloriosa superba caused only mild acute kidney injury (AKI) and rhabdomyolysis"* (PMID:30888889).
- **Functional genomics screens:** none specific to colchicine poisoning. Colchicine is widely used *as a reagent* in cell-biology screens, which is a different claim and should not be curated as disease evidence.

---

## 7. Anatomical Structures Affected

**Primary targets — highest mitotic index and highest drug uptake.**

| Structure | UBERON (verified) | Injury |
|---|---|---|
| Bone marrow | `UBERON:0002371` | Progenitor arrest, hypocellularity, pancytopenia |
| Intestine | `UBERON:0000160` | Crypt enterocyte apoptosis, mucosal barrier loss |
| Colon | `UBERON:0001155` | Secretory diarrhoea |
| Hair follicle | `UBERON:0002073` | Anagen arrest → alopecia days 5–16 |

**Secondary / systemic involvement.**

| Structure | UBERON | Injury |
|---|---|---|
| Heart | `UBERON:0000948` | Contractility and conduction failure; septal microinfarct at autopsy (PMID:37222938) |
| Liver | `UBERON:0002107` | Transaminitis, centrilobular necrosis, acute liver failure |
| Kidney | `UBERON:0002113` | AKI, tubular injury; renal-pelvis epithelial necrosis in calves (PMID:9764409) |
| Muscle organ | `UBERON:0001630` | Vacuolar myopathy, rhabdomyolysis |
| Nerve | `UBERON:0001021` | Axonal polyneuropathy |
| Lung | `UBERON:0002048` | ARDS, respiratory failure |

**Body systems:** digestive, haematopoietic and immune, cardiovascular, renal, hepatobiliary, neuromuscular, respiratory, integumentary.

**Cell populations (Cell Ontology, verified).**

| Cell type | CL | Role |
|---|---|---|
| enterocyte | `CL:0000584` | crypt apoptosis, phase 1 |
| hematopoietic stem cell | `CL:0000037` | progenitor arrest |
| myeloid cell | `CL:0000763` | preferential drug accumulation (PMID:42589484) |
| neutrophil | `CL:0000775` | chemotaxis inhibition; necrobiosis reported (PMID:42053158) |
| megakaryocyte | `CL:0000556` | thrombocytopenia |
| cardiac muscle cell | `CL:0000746` | contractility/conduction failure |
| hepatocyte | `CL:0000182` | centrilobular necrosis |
| neuron | `CL:0000540` | axonal transport failure |

Also implicated in the cattle model: Kupffer cells, renal tubular epithelial cells, and lymphocytes (PMID:9764409).

**Subcellular (GO cellular component, verified):** `GO:0005874` microtubule, `GO:0005819` spindle, `GO:0005764` lysosome, `GO:0072559` NLRP3 inflammasome complex.

**Lateralization:** not applicable. The distribution is systemic and symmetric. Neuromyopathy is bilateral and proximal.

---

## 8. Temporal Development

**Onset.** Any age. Acute in overdose, insidious in accumulation. The two clocks are the disease's defining structural feature.

- **Acute overdose:** gastrointestinal onset at 10–24 h (PMID:20586571), sometimes earlier. Peak serum concentration at 0.5–3.0 h post ingestion (PMID:34229452).
- **Chronic accumulation:** 48% of neuromyopathy cases had been on colchicine more than 12 months (PMID:36512928). One reported case had taken it for 23 years before presenting with neuromyopathy, gastric ulcers, and myelosuppression (PMID:35047617).

**Stages.**

| Phase | Window | Content |
|---|---|---|
| 1 — Gastrointestinal | 0–24 h | Vomiting, diarrhoea, abdominal pain, leukocytosis, hypovolaemia, lactic acidosis |
| 2 — Multi-organ dysfunction | 24 h – 7 days | Shock, arrhythmia, AKI, liver failure, pancytopenia, DIC, rhabdomyolysis, encephalopathy, seizures. Death occurs here. |
| 3 — Recovery | 7–21 days | Organ recovery, rebound leukocytosis, alopecia |

**Progression rate.** Rapid. Deaths in the reported series occur on hospital days 7–8 (PMID:34229452, PMID:9786547, PMID:37222938). Experimental calves died within 63 hours (PMID:9764409). A poisoned dog was euthanised at ~24 hours (PMID:14992256). Minipigs given 0.25 mg/kg IV required euthanasia at a mean 22.5 h (SD 3.2) (PMID:29334816).

**Course pattern.** Acute, monophasic, self-limited if survived. Not relapsing. Not chronic — with the exception of the chronic-accumulation neuromyopathy, which is progressive while the drug continues and remits on withdrawal.

**Duration.** Acute illness resolves over days to a few weeks. Neuromyopathy resolves at a median of 21 days after cessation (PMID:36512928).

**Remission.** Treatment-facilitated and spontaneous. There is no antidote to induce it; withdrawal plus supportive care is the mechanism.

**Critical periods — the intervention windows.**

- **< 60 min:** gastric lavage may be warranted for very large recent ingestions (PMID:20586571).
- **First hours:** early activated charcoal. Presentation at 1 hour was associated with recovery from 1.38 mg/kg; presentation at 44 hours with death at a lower dose (PMID:34229452).
- **1–3 hours (experimental):** Fab given 1 or 3 h after colchicine gave survival to study end without marked cardiotoxicity; the same dose at 6 h did not prevent toxicity (PMID:29334816). That is the sharpest therapeutic-window result in the field.

---

## 9. Population and Epidemiology

**Inheritance: not applicable.** There is no inheritance pattern, penetrance, expressivity, anticipation, germline mosaicism, founder effect, consanguinity role, or carrier frequency, because this is an exposure disorder. Record as *not applicable*.

### Incidence and case fatality

| Population | Measure | Value | Source |
|---|---|---|---|
| UK children < 18 | Minimum incidence | 0.41 cases/million children/year (57 cases over 2011–2021) | PMID:41663238 |
| UK children | Case fatality | 4/57 (7%); MOF in 7/57 (12%); systemic toxicity 12/57 (21.1%) | PMID:41663238 |
| Sri Lanka, *Gloriosa superba* self-poisoning | Case fatality | 10% (29/297) | PMID:30888889 |
| Türkiye, paediatric ICU | MODS rate | 26.7% of 150; single-organ failure 7.3%; no organ failure 66% | PMID:42499431 |
| China, acute colchicine poisoning | Survival by dose | 100% (≤0.5 mg/kg), 83.33% (0.5–0.8), 28.60% (≥0.8) | PMID:34484680 |
| Hong Kong, clarithromycin co-prescription | Mortality | 10.2% concomitant vs 3.6% sequential | PMID:16007523 |
| FAERS reports with colchicine + CYP3A4/P-gp inhibitor + AE | Severity | 61% hospitalisation, 24% death among reports stating severity (n = 787) | PMID:36688283 |

**Prevalence:** not a meaningful measure for an acute poisoning. Use incidence and case fatality.

**Geographic distribution.** Two distinct epidemiologies.

- **Pharmaceutical overdose:** wherever colchicine is prescribed. Expanding, because indications are expanding — gout and familial Mediterranean fever have been joined by pericarditis, coronary artery disease, and cardiovascular event prevention (PMID:42618164, PMID:41663238).
- **Plant poisoning:** *Gloriosa superba* in South Asia, notably Sri Lanka, where it accounts for a large share of plant poisonings; *Colchicum autumnale* in Europe, both as foraging error and as livestock/pasture exposure (Switzerland, Germany, Italy, Croatia).

**Age distribution.** Bimodal in paediatrics: 40% under 5 years (accidental) and 52% over 13 years (deliberate), in the Turkish cohort (PMID:42499431). UK median age 7 years, range 0–17 (PMID:41663238). Adult self-poisoning cases cluster in young adults; accumulation toxicity clusters in the elderly. Age is a strong mortality signal — *"Fatal outcomes and high concentrations were both much more common in the elderly"* (PMID:30888889).

**Sex ratio.** No reliable sex ratio located for colchicine poisoning specifically. Sex was a significant covariate in colchicine population pharmacokinetics (PMID:40719983), which is a disposition finding, not an incidence one. Gap.

**Affected populations.** No ethnic predisposition established. Ethnicity was tested as a covariate in the population PK model and was not among the significant predictors (PMID:40719983). Familial Mediterranean fever populations carry elevated exposure by virtue of lifelong therapy, not by susceptibility.

---

## 10. Diagnostics

**The diagnosis is clinical and historical.** No routine assay confirms it in time to matter. One 2023 case notes plainly: *"Unfortunately, specific tests of colchicine toxicity were not routinely available"* (PMID:37813551).

### Establishing the diagnosis

Finkelstein et al. (PMID:20586571): *"History of ingestion of tablets, parenteral administration, or consumption of colchicine-containing plants suggest the diagnosis."*

The differential trap is sepsis. A patient with vomiting, diarrhoea, leukocytosis, hypotension, and lactate looks septic, and a 2023 case report exists specifically because the toxicity mimicked septic shock (PMID:37813551).

### Laboratory tests

- **Full blood count with differential**, serially. Watches for the phase-2 nadir and the phase-3 rebound. This is the single most informative repeated test.
- **Creatine kinase** — always elevated in colchicine myopathy (PMID:3035372).
- **Renal panel, liver panel, lactate, coagulation screen (PT/INR, fibrinogen, D-dimer), electrolytes including calcium, magnesium, phosphate, sodium, potassium, glucose.** Calcium, magnesium, potassium, phosphate, and glucose derangements are all documented (PMID:34229452).
- **Plasma colchicine concentration** — the best prognostic test, and the least available. Assayed by HPLC or LC-MS/MS in research settings.

### Biomarkers

The strongest quantitative result in the field is prognostic, not diagnostic (PMID:30888889): *"The area under the receiver operating characteristic curve (AUC-ROC) for uncorrected admission colchicine level was highly predictive of a fatal outcome, and this improved even further with two methods we developed to correct for the expected change with time. The best method had an AUC-ROC of 0.98 (95%CI 0.94-1.00) in predicting death, with 100% sensitivity and 96% specificity at the best cut-point."*

Reference concentration context: the nominal therapeutic range is 0.5–3 ng/mL (PMID:40719983). Fatal cases in the Sri Lankan cohort had admission medians of 7.8 ng/mL (IQR 5.8–18.7) against 1.2 (0–2.3) in survivors. LOINC codes exist for the routine chemistry and haematology panels; I did not resolve a LOINC code for a plasma colchicine assay and will not invent one.

### Imaging and functional studies

- **Echocardiography** — detects the reduced ejection fraction that defines the cardiogenic-shock phase (PMID:34229452, PMID:26230148).
- **ECG** — arrhythmia and conduction block surveillance.
- **Muscle MRI** — described in colchicine myopathy; the first published muscle-MRI data appeared in 2019 (PMID:31178824).
- **Electromyography** — *"Electromyography of proximal muscles shows a myopathy that is marked by abnormal spontaneous activity"* (PMID:3035372). Nerve conduction studies show the axonal polyneuropathy.
- **CT abdomen/pelvis and chest X-ray** were unremarkable in one severe case (PMID:34229452), so normal imaging does not reassure.

### Biopsy and pathology

- **Muscle biopsy:** vacuolar myopathy. Kuncl: *"The myopathy is vacuolar, marked by accumulation of lysosomes and autophagic vacuoles unrelated to necrosis or to the mild denervation in distal muscles"* (PMID:3035372).
- **Bone marrow:** hypocellularity; massive neutrophil necrobiosis has been reported (PMID:42053158, title-level).
- **Autopsy:** centrilobular hepatic necrosis and cardiac septal microinfarct (PMID:37222938). Post-mortem bile assay is informative for toxicokinetics — 27 ng/mL in that case.
- **Post-mortem muscle biochemistry** is being developed forensically in rats (PMID:41547239).

### Genetic testing

Not indicated for diagnosis. WGS, WES, gene panels, single-gene testing, chromosomal microarray, karyotype, FISH, mtDNA testing, and repeat-expansion testing all have no diagnostic role here. ABCB1 genotyping is a research tool for susceptibility (PMID:31178824, PMID:40136464), not a clinical test.

### Screening

No population screening exists, and none is indicated. The preventable pathway is prescription screening — automated interaction checking for CYP3A4/P-gp inhibitors and dose review against renal function.

### Differential diagnosis

| Condition | Distinguishing feature |
|---|---|
| Septic shock | Colchicine gives early leukocytosis then profound neutropenia; sepsis rarely inverts that way at 24–72 h. Exposure history decides it. (PMID:37813551) |
| Acute gastroenteritis | Colchicine progresses to marrow failure and cardiogenic shock; gastroenteritis does not |
| Other cytotoxic/antimitotic overdose | Requires exposure history |
| Polymyositis | Kuncl: colchicine myoneuropathy *"is usually misdiagnosed initially, either as probable polymyositis or as uremic neuropathy"* (PMID:3035372). CK rises in both; the vacuolar biopsy and the remission on withdrawal separate them |
| Uraemic neuropathy | Same paper, same trap. Renal impairment coexists, which is what makes it hard |
| Arsenic or thallium poisoning | Both give GI phase then alopecia. Toxicological assay separates them |

---

## 11. Outcome and Prognosis

### Mortality

There is no single case-fatality rate. It depends on dose, timing, age, and organ reserve. Reported figures span 7% to 10% in unselected poison-centre and plant-ingestion populations, and rise steeply with dose (see the epidemiology table in section 9).

**The dose–prognosis rule, and its erosion.** The classical rule attributed to Bismuth and colleagues holds that ingestion below 0.5 mg/kg predicts survival and above 0.8 mg/kg predicts death. It is repeated in nearly every review. I could not retrieve the primary Bismuth publication in this search and flag that as an unverified secondary attribution.

Three recent findings contradict the rule's hard edges:

1. Survival was 28.6%, not 0%, in the ≥0.8 mg/kg band (n = 43) (PMID:34484680).
2. Paediatric national-cohort data state directly: *"MODS can develop at ingestion doses lower than 0.5 mg/kg, which have historically been considered safe"* (PMID:42499431).
3. UK paediatric fatalities occurred across 0.21 to 1.45 mg/kg, all mixed overdoses (PMID:41663238).

And a fourth, arguing the opposite direction (PMID:42589484): *"The widely accepted belief that total doses of 7-7.5 mg are inherently lethal appears to reflect historical cases complicated by drug interactions and/or hepatic or renal impairment, rather than toxicity attributable to colchicine dose alone."*

The rule was a plank laid across a stream, and the stream has moved.

### Prognostic factors

| Factor | Direction | Source |
|---|---|---|
| Admission plasma colchicine concentration | Strongest single predictor; AUC-ROC 0.98 with time correction | PMID:30888889 |
| Ingested dose per kg | Independent MODS predictor in children | PMID:42499431 |
| Baseline PRISM III score | Independent MODS predictor | PMID:42499431 |
| Admission sodium, creatinine, AST | Independent MODS predictors | PMID:42499431 |
| Age > 65 | Higher concentrations, higher fatality | PMID:30888889 |
| Delayed presentation | Poor prognosis | PMID:20586571 |
| Pre-existing renal or hepatic impairment | Poor prognosis | PMID:20586571, PMID:16007523 |
| Development of pancytopenia | RR 23.4 (95% CI 4.48–122.7; P < 0.001) for death in the clarithromycin cohort | PMID:16007523 |
| Longer overlapped interacting-drug therapy | RR 2.16 (95% CI 1.41–3.31; P ≤ 0.01) | PMID:16007523 |

**A 2026 prediction tool exists and is not ready.** A bicentre French–Italian nomogram using admission colchicine concentration and time since ingestion was developed on 52 patients and validated on three small cohorts (n = 25, 13, 16). The authors' own conclusion is the correct framing: *"An exploratory nomogram for early risk stratification of mortality after colchicine poisoning is presented. Clinical implementation requires prospective multicenter validation with adequate statistical power"* (PMID:42522392). Do not curate this as a validated instrument.

### Recovery and morbidity

Survivors generally recover completely: *"Recovery typically occurs within a few weeks of ingestion, and is generally a complete recovery barring complications of the acute illness"* (PMID:20586571). Neuromyopathy resolved completely in 70% of cases at a median of 21 days after cessation (PMID:36512928).

Complications during the course: neutropenic sepsis (fungaemia documented, PMID:34229452), DIC with diffuse bleeding, dialysis-requiring AKI, ARDS, cardiac arrest, cerebral oedema with seizures, and the iatrogenic burden of ECMO and massive transfusion.

**Life expectancy:** unaffected in survivors. No long-term excess-mortality cohort located. Gap.

**Quality-of-life instruments:** none reported for this disorder. Gap.

---

## 12. Treatment

**There is no antidote in clinical use.** Every guideline statement reduces to decontaminate early, support aggressively, and rescue the marrow. Cozza et al.: *"There is currently no antidote or directed therapy available for colchicine overdose"* (PMID:34229452).

### Decontamination

| Intervention | Evidence | NCIT suggestion |
|---|---|---|
| Activated charcoal, including multiple-dose | *"Timely gastrointestinal decontamination should be considered with activated charcoal"* (PMID:20586571). Rationale is enterohepatic recirculation. | `NCIT:C77524` Activated Charcoal (verified; this is the agent, not the action) |
| Gastric lavage | *"very large, recent (<60 min) ingestions may warrant gastric lavage"* (PMID:20586571) | No NCIT term resolved by exact label. Flag for curation. |

**A caveat that matters.** The theoretical case for multiple-dose charcoal targeting enterohepatic recirculation is weaker than it looks. From the fatal adolescent case with a measured post-mortem bile concentration (PMID:37222938): *"Assuming that activated charcoal would be able to adsorb 100% of biliary colchicine, using the bile concentration obtained above, only 0.0162mg of colchicine per day would be able to be adsorbed and eliminated by activated charcoal in this patient."* Independently, no measurable clearance from charcoal was observed in a monitored paediatric case (PMID:33898365).

### Supportive care — the mainstay

| Intervention | Role | NCIT suggestion |
|---|---|---|
| Aggressive fluid and electrolyte replacement | Phase-1 hypovolaemia | `NCIT:C116537` Fluid Therapy (verified) |
| Vasopressors | Refractory shock; three agents plus stress-dose steroids in one case (PMID:34229452) | No exact-label NCIT term resolved for "Vasopressor Agent". Flag. |
| Mechanical ventilation | Respiratory failure | `NCIT:C70909` Mechanical Ventilation (verified) |
| Blood product support | DIC, thrombocytopenia; 15 RBC + 13 platelet + 7 FFP units in one survivor (PMID:26230148) | `NCIT:C15192` Blood Transfusion; `NCIT:C15366` Platelet Transfusion; `NCIT:C89783` Fresh Frozen Plasma (all verified) |
| General supportive care | Framing term | `NCIT:C15747` Supportive Care (verified) |

### Marrow rescue — G-CSF

The best-supported specific intervention. Two early case reports established it: pancytopenia resolved after a single 300 µg subcutaneous dose in one patient (PMID:1384817) and after doses on days 4, 5, 6, and 8 in another (PMID:7530779). Katz et al. conclude: *"The use of G-CSF appears to be beneficial in alleviating bone marrow depression in colchicine overdose situations."* The 2010 systematic review folds it into the standard of care: *"Supportive treatments including administration of granulocyte colony-stimulating factor are the mainstay of treatment"* (PMID:20586571).

The Chinese series adds thrombopoietin: *"Different doses of recombinant human granulocyte colony-stimulating factor and recombinant human thrombopoietin can shorten the severity and duration of neutropenia and thrombocytopenia"* (PMID:34484680).

NCIT suggestions: `NCIT:C1474` Filgrastim (verified), `NCIT:C26078` Granulocyte Colony-Stimulating Factor (verified), `NCIT:C15986` Pharmacotherapy (verified, generic action). Gene: CSF3 `HGNC:2438`.

### Extracorporeal support and elimination

**The distinction to hold onto: extracorporeal *support* works; extracorporeal *elimination* does not.** Colchicine's large volume of distribution and intracellular binding put it out of reach.

- Only 5.2% of a dose was recovered in dialysate in a formal renal-impairment PK study (PMID:25385362).
- In a monitored poisoned child: *"We observed no significant clearance from renal replacement therapy, nor activated charcoal, during this period... extracorporeal techniques do not seem to improve colchicine elimination"* (PMID:33898365).

Support, by contrast, has saved lives. A 68-year-old with an ejection fraction of 5–10% survived on venoarterial ECLS: *"ECLS allowed good cardiac contractility recovery within a few days, with complications including bleeding made controllable"* (PMID:26230148). It is not universally successful — a 2024 report documents the challenges and limitations of VA-ECMO plus a microaxial flow pump in colchicine overdose (PMID:39484332), and a 13-year-old died despite VA-ECMO and exchange transfusion (PMID:37222938).

Plasma exchange has recent support. One 2025 case describes complete recovery with early therapeutic plasma exchange plus G-CSF and intensive care (PMID:41151150), and plasma exchange combined with continuous veno-venous haemodiafiltration *"can increase survival time"* in the 43-case series (PMID:34484680). NCIT: `NCIT:C15304` Plasmapheresis (verified); `NCIT:C171507` Extracorporeal Membrane Oxygenation (verified); `NCIT:C15248` Hemodialysis (verified). No exact-label NCIT term resolved for continuous renal replacement therapy — flag.

### Adjuncts of uncertain benefit

- **N-acetylcysteine** for colchicine-associated liver failure. Used off-protocol; liver enzymes normalised 48 hours after administration in one case, though the patient still died (PMID:34229452). The authors are explicit that no protocol exists. CHEBI `CHEBI:22198` acetylcysteine; NCIT `NCIT:C200` Acetylcysteine (both verified).
- **Intravenous lipid emulsion.** Used in a *Colchicum autumnale* case that recovered (PMID:42043136) and in a surviving dog (PMID:31883205). The 2026 nursing review calls IV lipid emulsion and NAC *"promising"* (PMID:42618164). That is case-level evidence, and it should be curated as such.

### The experimental antidote — colchicine-specific Fab fragments

The one intervention aimed at the lesion itself. Goat-derived colchicine-specific Fab produced full recovery in a woman who ingested 60 mg, published in the New England Journal of Medicine (PMID:7845428; no abstract is indexed, so I quote no text from it).

The definitive preclinical study is the Göttingen minipig model (PMID:29334816). It answers the timing question and it is unambiguous: *"Colchicine-specific Fab given early, in equimolar dose, bound colchicine, eliciting its movement into the blood, and preventing severe toxicity. Clinical studies are now needed to determine how soon this antidote must be given to work in human poisoning."* The internal contrast is the finding: full-neutralising Fab at 6 h *"did not prevent toxicity (euthanasia at 29.1 [SD = 3.4] h)"*, while the same dose at 1 or 3 h gave *"survival to study end without marked cardiotoxicity."*

It remains unavailable. *"Although a specific experimental treatment (Fab fragment antibodies) for colchicine poisoning has been used, it is not commercially available"* (PMID:20586571). Not licensed in the United States or Europe as of the most recent reports.

### Pharmacogenomics of treatment

None. There is no genotype-guided therapy for colchicine poisoning. ABCB1 genotype is a susceptibility question, not a treatment-selection one.

### Gene, cell, RNA, targeted, and immunotherapies

None applicable, with the single exception that the Fab antidote is an antibody-fragment biologic. No gene therapy, no CRISPR, no ASO or siRNA, no CAR-T, no checkpoint inhibitor has any role.

### Surgery

No surgical intervention treats colchicine poisoning. Vascular access for ECMO/ECLS and dialysis is procedural, not therapeutic.

### Treatment algorithm

1. Establish the exposure history. Contact poison control. Colchicine looks like sepsis and like gastroenteritis; the history is the diagnosis.
2. Decontaminate if early — charcoal, lavage only for very large ingestions inside 60 minutes.
3. Admit to intensive care regardless of how well the patient looks. Deterioration is delayed and steep.
4. Aggressive fluid and electrolyte resuscitation; vasopressors for shock.
5. Serial full blood counts. Give G-CSF for neutropenia. Consider thrombopoietin for thrombocytopenia.
6. Blood products for DIC and bleeding.
7. Renal replacement for uraemia and volume — for organ support, not for drug removal.
8. Consider ECLS/VA-ECMO for refractory cardiogenic shock.
9. Consider plasma exchange, NAC, and lipid emulsion as adjuncts on case-level evidence.
10. Watch for neutropenic sepsis. Cover it early.

---

## 13. Prevention

Prevention is where nearly all the achievable benefit sits, because treatment is supportive and the antidote does not exist.

### Primary prevention

- **Do not co-prescribe colchicine with a dual CYP3A4/P-gp inhibitor.** The strongest single recommendation in the field (PMID:16007523): *"Since there are other drugs for treatment of pneumonia and gout, these 2 drugs should not be coprescribed, because of the risk of fatality."* Reinforced by FAERS-wide signal detection: *"Avoiding the interaction or monitoring for toxicity in patients when co-prescribing colchicine and these agents is highly recommended"* (PMID:36688283).
- **Dose reduction in renal or hepatic impairment.** *"For those with liver or kidney dysfunction, the dose of colchicine needs to be reduced"* (PMID:34229452).
- **Dose ceilings.** Population PK modelling supports ≤ 1.5 mg daily as carrying low toxicity risk, with the caveat that *"Higher colchicine dosages of > 1.5 mg daily may exceed the proposed upper limit of safety in individuals with low body weight who are taking statins"* (PMID:40719983).
- **Plant misidentification education.** Wild garlic vs autumn crocus (PMID:42043136); ginger vs *Gloriosa* tuber (PMID:41628608). This is public health education with a concrete target.
- **Household medicine storage**, given the under-5 accidental peak (PMID:42499431).
- **Agricultural pasture management** to keep *Colchicum autumnale* out of forage, which protects livestock and the milk supply (PMID:40905265).

### Secondary prevention

- Serial blood-count monitoring in patients on long-term colchicine with renal impairment or an interacting drug. The myelosuppression review targets exactly this group: *"The majority of patients with myelosuppression had preexisting renal impairment or concomitant CYP3A4 or P-gp inhibitor use. Caution should be taken in this subset of patients with increased monitoring"* (PMID:36319015).
- Consider colchicine in any patient on the drug who presents with proximal weakness or unexplained cytopenia. The 23-year case is the cautionary one (PMID:35047617): *"the patient's medication history should never be ignored."*
- Early recognition and poison-centre involvement in suspected acute exposure.

### Tertiary prevention

- Withdraw colchicine at the first sign of neuromyopathy. Resolution follows in 70% of cases at a median 21 days (PMID:36512928).
- Rechallenge, if needed, at reduced dose: 73% of 15 rechallenged patients had no recurrence (PMID:36512928).
- Neutropenic precautions and early antimicrobial cover during the marrow phase.

### Not applicable

Immunisation, genetic screening, carrier screening, preimplantation or prenatal testing, and genetic counselling have no role. Record as *not applicable*.

### Risk stratification

Electronic prescribing alerts on the colchicine + CYP3A4/P-gp inhibitor pair, and renal-function-linked dose checks, are the practical tools. No validated clinical risk score exists for pre-exposure risk; the 2026 nomogram is post-exposure and unvalidated (PMID:42522392).

---

## 14. Other Species and Natural Disease

Colchicine poisons every animal tested. There is no species-specific resistance mechanism, because the target is conserved tubulin.

**Taxonomy of affected species** (NCBI Taxonomy identifiers given as leads; I resolved MONDO, HP, GO, CL, UBERON, CHEBI, and NCIT against OLS this session, but not NCBITaxon):

| Species | Common | Evidence |
|---|---|---|
| *Bos taurus* | Cattle | Fatal experimental and natural poisoning; 11 calves fed crude or dehydrated *Colchicum* bulbs all died or were euthanised within 63 h (PMID:9764409). A fatal heifer case confirmed by mass spectrometry (PMID:20093699). Herd exposure in a Swiss dairy (PMID:40905265). |
| *Canis lupus familiaris* | Dog | One fatal accidental ingestion of an owner's medication, euthanised at ~24 h (PMID:14992256); one survival after a tenfold prescribing error (PMID:31883205). |
| *Rattus norvegicus* | Rat | Experimental toxicity and Fab studies (PMID:41547239, PMID:25858137). |
| *Mus musculus* | Mouse | Crypt apoptosis, passive-immunisation studies (PMID:15865323, PMID:2815097). |
| *Sus scrofa* (Göttingen minipig) | Pig | Purpose-built critical-care toxicity model (PMID:29334816). |
| *Oryctolagus cuniculus* | Rabbit | Active immunisation against colchicine (PMID:2734802). |

**Breeds.** Brown Swiss cattle in the Swiss dairy incident (PMID:40905265); a toy poodle cross (PMID:14992256) and a Pomeranian (PMID:31883205) in the canine reports. No breed predisposition — these are exposure accidents, not breed traits. VBO identifiers not resolved.

**Orthologous genes.** Tubulin and ABCB1 orthologues are broadly conserved across mammals. I did not resolve NCBI Gene identifiers for the animal orthologues.

**Natural disease and veterinary importance.** Substantial in ruminant medicine, where autumn crocus in pasture or hay is a recognised livestock hazard in northern and eastern Germany and elsewhere (PMID:11413718). Small-animal poisoning is accidental household or prescribing exposure. Canine presentation mirrors human: *"Gastrointestinal signs, symptoms of cerebral edema, cardiac arrhythmias, and neutropenia were documented"* (PMID:31883205).

**Comparative pathology.** The cross-species similarity is close enough to be diagnostically useful. From the calf study (PMID:9764409): *"The lesion of the present acute crocus poisoning of cattle closely resembled those reported in humans with colchicine intoxication."* Same targets: alimentary epithelium, haematopoietic and lymphoid tissue, renal tubular epithelium, Kupffer cells. Same mechanism: apoptosis of arrested dividing cells (PMID:10458107).

**Evolutionary conservation.** The colchicine-binding site on tubulin is conserved across eukaryotes, which is why colchicine works as a mitotic-arrest reagent in plants, fungi, and animals, and why the poisoning is species-general.

**Zoonotic potential and cross-species transmission.** None — this is a chemical exposure, not an infection. There is, however, a genuine **food-chain transfer** route: colchicine appears in milk from exposed dairy cattle, with a bulk sample positive at two weeks and negative at five weeks after the incident (PMID:40905265). Colchicine is not permitted as a pharmacologically active substance in food-producing animals under EU Regulation No 37/2010, and no maximum residue limit or withdrawal period exists.

---

## 15. Model Organisms

**No genetic model exists, and none is needed.** Colchicine poisoning is induced by administering colchicine. Knockout, knock-in, transgenic, conditional, and humanised models are all not applicable as *disease* models. (A transporter-deficient model such as an *Abcb1*-null mouse would model the susceptibility, not the poisoning, and I found no published use of one for this purpose.)

### Induced models

| Model | System | Protocol | Recapitulation | Limitations | Source |
|---|---|---|---|---|---|
| **Göttingen minipig critical-care model** | *Sus scrofa* | 0.25 mg/kg colchicine IV over 1 h | Best available. *"intravenous infusion of 0.25 mg/kg colchicine over 1 h produced reproducible pharmacokinetics (AUC0-20 343 [SD = 21] µg/L/h), acute multi-organ injury, and cardiotoxicity requiring euthanasia a mean of 22.5 (SD = 3.2) h after dosing."* Purpose-built for antidote timing. | Intravenous, so it bypasses the gastrointestinal phase and first-pass metabolism entirely. Oral dosing was tried and abandoned: *"Initial studies indicated that oral dosing produced variable pharmacokinetics and time-to-euthanasia."* The 22-hour endpoint precedes the human marrow phase, so myelosuppression is not modelled. | PMID:29334816 |
| **Rat acute lethal model** | *Rattus norvegicus*, Sprague Dawley, n = 60 | Single oral 4.9 mg/kg; death in 8–10 h | Forensic post-mortem biochemistry in skeletal, cardiac, and smooth muscle. Time-dependent falls in pH, Na⁺, ATP, glycogen; rises in CRP, LDH, Ca²⁺, K⁺, lactate. | Death at 8–10 h models only hyperacute toxicity. Immunohistochemistry for cytochrome c oxidase and Na⁺/K⁺-ATPase did *not* differ between groups — a negative result worth carrying. | PMID:41547239 |
| **Bovine feeding model** | *Bos taurus*, 11 calves | Crude or dehydrated *Colchicum autumnale* bulbs, oral | Recapitulates the human histopathology closely; established apoptosis as the death mechanism by TUNEL and electron microscopy. | Plant material, so the exposure includes demecolcine alongside colchicine. All animals died within 63 h. Ruminant gastrointestinal anatomy differs (forestomach, abomasum). | PMID:9764409, PMID:10458107 |
| **Mouse crypt-apoptosis model** | *Mus musculus*, C3H/S | Single i.p. colchicine, sacrifice 4 h later | Models the phase-1 target lesion specifically: crypt enterocyte apoptosis, highest in the deepest crypt regions. | Single-tissue, single-endpoint. Also shows circadian dependence — *"the colchicine cytotoxicity due to its apoptotic-inducing effect depends on the dosing time during the 24 h in this mouse strain"* — which means dosing time is a confounder in every rodent colchicine experiment. | PMID:15865323 |
| **Rat and rabbit Fab-clearance models** | Rat, rabbit | Colchicine ± specific antibody or Fab | Antidote pharmacokinetics only. Fab fragments enhance urinary colchicine clearance in the rat. | Disposition models, not disease models. Do not use them to support a clinical-outcome claim. | PMID:25858137, PMID:1545388, PMID:2734802, PMID:2815097 |
| **Beagle sustained-release PK model** | *Canis lupus familiaris* | Colchicine sustained-release microspheres | Formulation work on toxicity mitigation | Pharmaceutical development, not poisoning | PMID:41759985 (title-level; abstract not read) |

### In vitro

No dedicated organoid, iPSC, or organ-chip model of colchicine poisoning was located. Colchicine is ubiquitous *as a reagent* in microtubule cell biology, which is a different thing and should not be curated as disease-model evidence. Lymphocyte efflux experiments with colchicine-specific Fab exist (PMID:7562471).

### Applications and gaps

**What the models answer well:** antidote timing (minipig), mechanism of cell death (cattle, mouse), post-mortem forensic markers (rat), antidote pharmacokinetics (rat, rabbit).

**What no model currently answers:** the human myelosuppressive phase, which is the phase that most drives clinical management. Every acute model kills the animal before day 3. That is the most obvious gap in the field, and it means G-CSF, thrombopoietin, and plasma exchange rest on human case-level evidence with no preclinical counterpart.

### Resources

MGI, RGD, and the Alliance of Genome Resources index colchicine as a chemical perturbagen rather than as a disease model. There is no colchicine-poisoning model repository. Models are constructed per study.

---

## Evidence source classification summary

For downstream curation, grading each citation by the study type it reports:

| Evidence source | PMIDs |
|---|---|
| HUMAN_CLINICAL | 20586571, 34229452, 16007523, 3035372, 36512928, 36319015, 30888889, 41663238, 42499431, 34484680, 42522392, 37222938, 33898365, 26230148, 39484332, 41151150, 42043136, 1384817, 7530779, 9786547, 20661070, 35047617, 37813551, 8035398, 25385362, 40719983, 31178824, 42618164, 14164521 |
| MODEL_ORGANISM | 29334816, 41547239, 9764409, 10458107, 15865323, 25858137, 1545388, 2734802, 2815097, 14992256, 31883205, 20093699, 40905265 |
| IN_VITRO | 15014504 (X-ray crystallography of the tubulin–colchicine–stathmin complex), 7562471 |
| OTHER | 40136464 (systematic review of transporter genetics), 36688283 (spontaneous-report disproportionality analysis), 42589484 (narrative dosing reappraisal), 29359661 (narrative pharmacology review) |

Note two grading subtleties for curation. First, PMID:36688283 is a FAERS disproportionality analysis — spontaneous reports, not a study of patients, and the reporting odds ratios are signals, not risks. Second, PMID:15014504 is structural biology; it supports the molecular mechanism claim and nothing clinical.

---

## Confirmed gaps

Stated plainly, so nobody curates around them:

- No sex ratio for colchicine poisoning incidence.
- No quality-of-life instrument data.
- No long-term survivor cohort or excess-mortality data.
- No colchicine-poisoning transcriptomic, proteomic, metabolomic, lipidomic, single-cell, or spatial dataset located. No GEO series.
- No epigenetic data.
- No LOINC code resolved for a plasma colchicine assay.
- No ECTO exposure terms resolved for colchicine or the two source plants.
- Four NCI Thesaurus concepts did not resolve by exact label: gastric lavage, therapeutic plasma exchange, continuous renal replacement therapy, vasopressor agent.
- The primary Bismuth publication behind the 0.5 / 0.8 mg/kg prognostic rule was not retrieved; every citation of it here is secondary.
- PMID:7845428 (the NEJM Fab case) has no PubMed abstract, so no quote is available from it.
- PMID:35237367, PMID:42053158, PMID:39870408, and PMID:41361680 are cited at title level only; their abstracts are not indexed in PubMed.

---

## Sources

Primary literature is cited by PMID throughout. Web resources consulted:

- [Colchicine poisoning: the dark side of an ancient drug — PubMed](https://pubmed.ncbi.nlm.nih.gov/20586571/)
- [The Ugly Side of Colchicine (PMC full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10725528/)
- [Insight into tubulin regulation from a complex with colchicine and a stathmin-like domain — Nature](https://www.nature.com/articles/nature02393)
- [RCSB PDB 1SA0: tubulin–colchicine–stathmin-like domain complex](https://www.rcsb.org/structure/1SA0)
- [Fatal interaction between clarithromycin and colchicine in patients with renal insufficiency — Clinical Infectious Diseases](https://academic.oup.com/cid/article-abstract/41/3/291/336398)
- [Drugs that interact with colchicine via CYP3A4 and P-glycoprotein inhibition (FAERS) — Annals of Pharmacotherapy](https://journals.sagepub.com/doi/10.1177/10600280221148031)
- [Factors contributing to colchicine toxicity — Medsafe New Zealand](https://www.medsafe.govt.nz/profs/PUArticles/March2025/Factors-contributing-to-colchicine-toxicity.html)
- [Colchicine toxicity — Utah Poison Control Center bulletin](https://poisoncontrol.utah.edu/sites/g/files/zrelqx281/files/media/documents/2021/toxicology-vol19-iss1.pdf)
- [Treatment of severe colchicine overdose with colchicine-specific Fab fragments — NEJM](https://www.nejm.org/doi/full/10.1056/NEJM199503093321004)
- [ICD-10-CM T50.4X1A](https://icdlist.com/icd-10/T50.4X1A)
- EBI Ontology Lookup Service (OLS4) API, for all MONDO/HP/GO/CL/UBERON/CHEBI/NCIT resolution
- HGNC REST API, for gene identifiers
- NCBI E-utilities (PubMed, MeSH), for abstracts and descriptors

---

**Report summary.** Colchicine poisoning is one molecular lesion — tubulin bound, microtubules unable to assemble — reaching every organ on different clocks. The gut and marrow fail first because they divide fastest; the heart fails because contraction needs an intact cytoskeleton; muscle and nerve fail slowest because axonal transport degrades over months. The liver and kidney injury closes a loop by slowing clearance of the poison. Mortality tracks dose, admission plasma concentration, age, and delay to presentation, but the classical 0.5/0.8 mg/kg prognostic rule is now contradicted from both directions by 2023–2026 data. Treatment is decontamination, intensive support, and G-CSF; extracorporeal circuits support the failing heart but do not remove the drug. The one mechanism-directed therapy, colchicine-specific Fab, works in the minipig if given within three hours and is not commercially available anywhere.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 59 |
| Resolved | 59 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 59 |
| On topic | 41 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 93 |
| Resolved | 86 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 7 |
| Terms whose name was checked | 19 |
| Terms named correctly | 18 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0017859` (2 mentions) - the report calls it "MONDO"; MONDO calls it **colchicine poisoning**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
