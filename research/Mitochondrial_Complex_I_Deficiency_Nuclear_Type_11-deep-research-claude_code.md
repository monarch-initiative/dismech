---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-20T17:39:04.419167'
end_time: '2026-09-20T17:44:19.738639'
duration_seconds: 315.32
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Mitochondrial Complex I Deficiency, Nuclear Type 11
  mondo_id: MONDO:0032617
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
  web_search_requests: 15
  num_turns: 24
  total_cost_usd: 1.6604534000000002
  session_id: dc83c613-1fba-53b8-9741-f63fb2448a6e
  stop_reason: end_turn
  assistant_text_blocks: 2
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 21
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 30
  verified: 27
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 8
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0032617
    reported_labels:
    - MONDO
    ontology_label: mitochondrial complex I deficiency, nuclear type 11
  labels_variant: 5
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mitochondrial Complex I Deficiency, Nuclear Type 11
- **MONDO ID:** MONDO:0032617 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Complex I Deficiency, Nuclear Type 11** covering all of the
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

I now have sufficient sourced material to compile the report.

I now have comprehensive, well-sourced material. Here is the complete research report.

---

# Mitochondrial Complex I Deficiency, Nuclear Type 11 (MC1DN11) — Comprehensive Research Report

**MONDO:0032617 | OMIM #618234 | Causal gene: *NDUFAF1* (OMIM *606934) | Locus: 15q15.1**

---

## 1. Disease Information

### Overview
Mitochondrial Complex I Deficiency, Nuclear Type 11 (MC1DN11) is an ultra-rare autosomal recessive mitochondrial oxidative phosphorylation (OXPHOS) disorder caused by biallelic pathogenic variants in **NDUFAF1** (NADH:ubiquinone oxidoreductase complex assembly factor 1), a nuclear-encoded gene whose product is required for the assembly — not the catalytic core — of mitochondrial respiratory Complex I. It belongs to the broader "isolated Complex I deficiency" disease group (Orphanet **ORPHA:2609**), the single most common biochemical defect among pediatric-onset mitochondrial OXPHOS disorders ([Orphanet: Isolated complex I deficiency](https://www.orpha.net/en/disease/detail/2609)).

The disorder was first delineated clinically by Fassone et al. (2011), who described a French infant with fatal infantile hypertrophic cardiomyopathy (HCM) and isolated Complex I deficiency carrying compound heterozygous *NDUFAF1* missense mutations ([OMIM #618234](https://www.omim.org/entry/618234); PMID:21931170). As of the most recent literature (Kalantari et al., 2025), only **four molecularly confirmed cases** have been reported worldwide, underscoring both its rarity and the still-emerging picture of its phenotypic spectrum ([PubMed 39821332](https://pubmed.ncbi.nlm.nih.gov/39821332/)).

### Key Identifiers
| Resource | Identifier |
|---|---|
| OMIM phenotype | #618234 — MITOCHONDRIAL COMPLEX I DEFICIENCY, NUCLEAR TYPE 11; MC1DN11 |
| OMIM gene | *606934 — NDUFAF1 |
| MONDO | MONDO:0032617 |
| Disease Ontology | DOID:0112089 ([JAX Disease Ontology Browser](https://www.informatics.jax.org/disease/DOID:0112089)) |
| Orphanet (disease group) | ORPHA:2609 (Isolated complex I deficiency) |
| Gene (HGNC) | HGNC:18828, symbol *NDUFAF1* |
| NCBI Gene ID | 51103 |
| Cytogenetic location | 15q15.1 (chr15: 41,387,218–41,409,403, GRCh38) |
| Legacy/synonym gene name | *CIA30* (human homolog of *Neurospora crassa* Cia30) |
| Reference transcript | NM_016013.4 |

### Synonyms
- Mitochondrial respiratory chain complex I deficiency, nuclear type 11
- MC1DN11
- NDUFAF1-related mitochondrial disease / NDUFAF1 deficiency
- (As part of the broader family) Isolated Complex I deficiency; NADH:ubiquinone oxidoreductase deficiency

### Nature of Underlying Data
Information is derived almost entirely from **individual patient case reports** (n=4 published families/patients globally) rather than aggregated disease-level registries — there is no dedicated GeneReviews chapter or large natural-history cohort specific to *NDUFAF1*-MC1DN11 at this time. Broader "isolated Complex I deficiency" epidemiology (used contextually below) is aggregated across many causal genes (Orphanet, MedlinePlus).

**Sources:**
- [OMIM #618234 – MC1DN11](https://www.omim.org/entry/618234)
- [OMIM *606934 – NDUFAF1](https://omim.org/entry/606934)
- [Disease Ontology DOID:0112089](https://www.informatics.jax.org/disease/DOID:0112089)
- [Orphanet: Isolated complex I deficiency (ORPHA:2609)](https://www.orpha.net/en/disease/detail/2609)
- [Kalantari et al. 2025, Am J Med Genet A, PMID:39821332](https://pubmed.ncbi.nlm.nih.gov/39821332/)

---

## 2. Etiology

### Disease Causal Factors
MC1DN11 is a purely **genetic/mechanistic** disease: biallelic (homozygous or compound heterozygous) loss-of-function variants in *NDUFAF1* impair the intramitochondrial chaperone-mediated assembly of Complex I, producing an **isolated, severe Complex I enzymatic deficiency** (~25% of control activity reported in skeletal muscle) without primary environmental or infectious causation ([OMIM #618234](https://www.omim.org/entry/618234)).

### Genetic Risk Factors
- **Causal variants (biallelic, AR):**
  - c.631C>T (p.Arg211Cys) and c.733G>A (p.Gly245Arg) — compound heterozygous missense variants, index French infant (Fassone et al. 2011, PMID:21931170). Both residues are highly conserved; neither variant found in 240 control alleles; each unaffected parent was heterozygous carrier for one variant.
  - c.631C>T (p.Arg211Cys) recurring, in compound heterozygosity with an **intragenic deletion encompassing exon 3** (NM_016013.4) — fourth reported case, Kalantari et al. 2025 (PMID:39821332).
- No common founder variant or population-enriched allele has been reported; each family reported to date carries private variants.
- No modifier genes have been specifically identified for MC1DN11, though general mitochondrial "second-hit" modifiers (mtDNA haplogroup, nuclear background) are plausible by analogy with other Complex I disorders but unstudied here.

### Environmental Risk Factors
- **Viral illness as a decompensation trigger:** in the index case, severe cardiac failure due to hypertrophic cardiomyopathy developed acutely in the context of an intercurrent viral illness at age 15 months, superimposed on a baseline compensated state — consistent with the general principle that catabolic/febrile stress unmasks or worsens mitochondrial energy-production failure ([OMIM #618234](https://www.omim.org/entry/618234)).
- No toxin, occupational, or dietary exposures have been implicated as primary causal factors; age and family history (parental consanguinity/carrier status) are the only recognized epidemiological risk modifiers in nuclear-recessive Complex I deficiencies generally.

### Protective Factors
None specific to *NDUFAF1*/MC1DN11 have been reported in the literature. By extrapolation from the broader Complex I deficiency literature, avoidance of metabolic decompensation triggers (fasting, febrile illness, strenuous exertion) and empiric mitochondrial cofactor supplementation (riboflavin, CoQ10, carnitine) are used supportively, but no genetic or environmental variant has been shown to be protective in this specific disorder.

### Gene-Environment Interactions
The clearest documented interaction is the **infection-triggered decompensation** pattern noted above: a viral illness converted a subclinical/compensated cardiac phenotype into fulminant, fatal heart failure in the index patient. This mirrors the general paradigm across mitochondrial disease in which increased ATP demand or oxidative/inflammatory stress during intercurrent illness exceeds a genetically constrained OXPHOS reserve capacity.

**Sources:** [OMIM #618234](https://www.omim.org/entry/618234); [Kalantari et al. 2025, PMID:39821332](https://pubmed.ncbi.nlm.nih.gov/39821332/)

---

## 3. Phenotypes

Because only four cases are published, frequencies below are described qualitatively per-case rather than as population percentages; this is a fundamental data limitation of an ultra-rare, recently-delineated gene-disease association.

| Phenotype | Type | Onset/Course | Suggested HPO term |
|---|---|---|---|
| Hypertrophic cardiomyopathy | Clinical sign/imaging finding | Infantile onset (index case: cardiac failure at 15 months); severity ranges from apparently isolated/milder (4th case) to fatal (1st case) — progressive in severe cases | HP:0001639 (Hypertrophic cardiomyopathy) |
| Failure to thrive | Clinical sign | Presented at 11 months in index case | HP:0001508 (Failure to thrive) |
| Lactic acidosis | Laboratory abnormality | Present at presentation, variable severity | HP:0003128 (Lactic acidosis) |
| Hypotonia | Clinical sign | Present in index/severe cases | HP:0001252 (Hypotonia) |
| Developmental delay | Clinical sign | Present in more severely affected cases | HP:0001263 (Developmental delay) |
| Intellectual disability | Clinical sign | Reported in some affected individuals | HP:0001249 (Intellectual disability) |
| Myopathy | Clinical sign / biopsy finding | Present with abnormal mitochondrial histology | HP:0003198 (Myopathy) |
| Wolff-Parkinson-White syndrome | Clinical/ECG finding | Reported as an additional cardiac feature | HP:0001716 (Wolff-Parkinson-White syndrome) |
| Cortical visual impairment | Clinical sign | Reported in more severe cases | HP:0100704 (Cortical visual impairment) |
| Pigmentary retinopathy | Clinical sign | Reported in more severe cases | HP:0000580 (Pigmentary retinopathy) |
| Increased lipid deposition in muscle / abnormal mitochondria on biopsy | Laboratory/histopathology | Skeletal muscle biopsy finding | HP:0025580 (Abnormal mitochondrial morphology) — closest available; consider free-text if no exact match |

### Phenotype Characteristics
- **Age of onset:** Infantile (all published cases present in the first ~1–2 years of life; index case at 11 months).
- **Severity/progression:** Markedly **heterogeneous** across the four reported cases — from an "apparently isolated," clinically simpler HCM presentation (Kalantari et al. 2025, 4th case) to a multisystem, fatal infantile cardioencephalomyopathy (Fassone et al. 2011, 1st case) ([PMID:39821332](https://pubmed.ncbi.nlm.nih.gov/39821332/)). The authors of the 2025 report explicitly frame their case as evidence of "the highly heterogeneous clinical presentation associated with this disorder."
- **Frequency among affected individuals:** Cannot be meaningfully quantified given n=4; hypertrophic cardiomyopathy is the one feature present in essentially all published cases and is the unifying diagnostic clue.
- **Quality of life impact:** Not formally measured (no EQ-5D/SF-36/disease-specific QOL studies exist for this gene-specific entity); by clinical inference, severity ranges from major disability/early mortality (severe cardioencephalomyopathy) to a milder course amenable to standard HCM management in the least-affected reported case.

**Sources:** [OMIM #618234 Clinical Synopsis](https://www.omim.org/clinicalSynopsis/618233); [Kalantari et al. 2025, PMID:39821332](https://pubmed.ncbi.nlm.nih.gov/39821332/); [Fassone et al. 2011, PMID:21931170]

---

## 4. Genetic/Molecular Information

### Causal Gene
- **NDUFAF1** (NADH:Ubiquinone Oxidoreductase Complex Assembly Factor 1), HGNC:18828, NCBI Gene 51103, OMIM *606934, chr15q15.1.
- Legacy gene symbol/alias: **CIA30** (human ortholog of *Neurospora crassa* Cia30 protein).
- Encodes a 327-amino-acid, ~37.8 kDa mitochondrial matrix-facing chaperone protein required for Complex I assembly — it is **not** a structural subunit of the mature holoenzyme ([GeneCards: NDUFAF1](https://www.genecards.org/card/NDUFAF1); [Vogel et al. 2005, PMID:16218961]).

### Pathogenic Variants Reported
| Variant (NM_016013.4) | Protein change | Type | Zygosity | Source/case |
|---|---|---|---|---|
| c.631C>T | p.Arg211Cys | Missense | Compound heterozygous | Fassone 2011 (case 1); recurring in Kalantari 2025 (case 4) |
| c.733G>A | p.Gly245Arg | Missense | Compound heterozygous (with c.631C>T) | Fassone 2011 (case 1) |
| Intragenic deletion, exon 3 | Predicted loss of function | Structural/deletion | Compound heterozygous (with c.631C>T) | Kalantari 2025 (case 4) |

- **Variant classification:** Both missense variants affect highly conserved residues; absent from 240 control alleles tested by Fassone et al. Formal ACMG/AMP tiering (e.g., in ClinVar) is not comprehensively documented in the retrieved sources for these specific alleles, but functional data (below) support pathogenicity.
- **Allele frequency:** No population frequency data specific to these alleles were retrieved; general gnomAD-style constraint metrics (pLI/LOEUF) for *NDUFAF1* were not resolved in this search session and should be looked up directly in the gnomAD browser before curation.
- **Somatic vs. germline:** All reported variants are **germline**, biallelic, inherited from heterozygous carrier parents (autosomal recessive).
- **Functional consequences:** Fibroblast/muscle studies show **severe reduction in NDUFAF1 protein levels**, **abnormal Complex I assembly intermediates**, and **isolated severe Complex I enzymatic deficiency** (~25% of control activity in skeletal muscle in the index case) — consistent with a loss-of-function / assembly-failure mechanism rather than dominant-negative gain of function ([OMIM #618234](https://www.omim.org/entry/618234); [PMID:39821332](https://pubmed.ncbi.nlm.nih.gov/39821332/)).

### Modifier Genes
None specifically identified for MC1DN11. The mechanistic partners of NDUFAF1 within the MCIA assembly complex (ECSIT, ACAD9, TMEM126B — see Mechanism section) are plausible candidate modifiers/epistatic partners by biological analogy but are not established modifiers of this specific gene's phenotype.

### Epigenetic Information
No disease-specific epigenetic (DNA methylation/histone) data have been reported for MC1DN11/*NDUFAF1*.

### Chromosomal Abnormalities
No large-scale chromosomal rearrangement (aneuploidy/translocation) mechanism has been reported; the one structural lesion documented is a small **intragenic exon-3 deletion** in *NDUFAF1* itself (Kalantari 2025), not a chromosomal-scale abnormality.

**Ontology suggestions:** Gene — `hgnc:18828` (NDUFAF1); relevant GO Cellular Component — mitochondrial inner membrane; GO Biological Process — mitochondrial respiratory chain complex I assembly (GO:0032981).

**Sources:** [OMIM *606934](https://omim.org/entry/606934); [OMIM #618234](https://www.omim.org/entry/618234); [Vogel et al. 2005, PMID:16218961]; [Kalantari et al. 2025, PMID:39821332]; [GeneCards: NDUFAF1](https://www.genecards.org/card/NDUFAF1)

---

## 5. Environmental Information

- **Environmental/toxic factors:** None established as causal for MC1DN11 specifically. General mitochondrial toxins (e.g., agents that inhibit OXPHOS) are theoretical aggravators by class but are not documented in the four published cases.
- **Lifestyle factors:** Not applicable/not reported — this is an early-infantile-onset monogenic disorder without a lifestyle-modifiable component documented in the literature to date.
- **Infectious agents:** **Intercurrent viral illness** is documented as a precipitant of acute cardiac decompensation in the index (fatal) case, functioning as a physiological stressor rather than a direct causal pathogen — i.e., infection unmasked/exacerbated the underlying genetic Complex I deficiency rather than causing it ([OMIM #618234](https://www.omim.org/entry/618234)).

**Sources:** [OMIM #618234](https://www.omim.org/entry/618234)

---

## 6. Mechanism / Pathophysiology

### Ordered Causal Chain
1. Biallelic pathogenic *NDUFAF1* variants (e.g., p.Arg211Cys / p.Gly245Arg, or missense + exon-3 deletion) **lead to** markedly reduced/destabilized NDUFAF1 protein.
2. Loss of functional NDUFAF1 **disrupts assembly of the Mitochondrial Complex I Intermediate Assembly (MCIA) complex**, in which NDUFAF1 acts as a core scaffolding component together with **ECSIT, ACAD9, and TMEM126B** ([Guerrero-Castillo et al. 2020, PMC bioRxiv/Cell Reports summary](https://www.biorxiv.org/content/10.1101/808311v1.full); [Reactome R-HSA-5689052](https://reactome.org/content/detail/R-HSA-5689052)).
3. A destabilized/absent MCIA complex **results in** failure to properly build the intermediate **ND2-module** (part of the proximal membrane arm, "PP-b") of nascent Complex I, and failure of the MCIA/TIMMDC1-dependent joining step that forms the combined **Q/ND1–ND2 (Q/PP) intermediate** ([Cell Reports 2020, PMID:32320651](https://pubmed.ncbi.nlm.nih.gov/32320651/)).
4. Mechanistically, within the MCIA complex, **ACAD9 forms a homodimeric scaffold**; **ECSIT's C-terminal domain binds ACAD9's vestigial dehydrogenase domain and drives its deflavination**, converting ACAD9 from a fatty-acid β-oxidation enzyme into a dedicated assembly factor, while bringing NDUFAF1 into the complex — a switch NDUFAF1 loss prevents from stabilizing productively ([Science Advances 2022, "Insights into complex I assembly: Function of NDUFAF1 and a link with cardiolipin remodeling"](https://www.researchgate.net/publication/365515145_Insights_into_complex_I_assembly_Function_of_NDUFAF1_and_a_link_with_cardiolipin_remodeling)). This same paper links NDUFAF1 function to **cardiolipin remodeling** in the inner mitochondrial membrane, connecting Complex I assembly failure to broader inner-membrane lipid homeostasis — of particular relevance to the cardiac phenotype, given cardiolipin's central role in cardiomyocyte mitochondrial membrane integrity.
5. Failed/incomplete Complex I assembly **causes** accelerated turnover of partially built intermediates (including the mtDNA-encoded ND1 subunit, which is rapidly degraded when assembly stalls — a general feature of early Complex I assembly defects, [PMC3412381]) and **results in** an isolated, severe deficiency of holo-Complex I enzymatic activity (~25% of normal in the index patient's skeletal muscle).
6. Loss of Complex I (NADH:ubiquinone oxidoreductase) activity **leads to** impaired electron transfer from NADH into the respiratory chain, **causing** (a) reduced proton-motive force and ATP synthesis (energy failure) and (b) **feedback inhibition of the NADH-consuming citric-acid cycle and pyruvate dehydrogenase complex**, which **results in** shunting of pyruvate to lactate and clinically manifest **lactic acidosis** ([EMBO Mol Med review, PMID via Complex I/Leigh syndrome literature](https://link.springer.com/article/10.15252/emmm.202013187)).
7. Chronic cellular energy failure, particularly in **high-energy-demand tissues (cardiomyocytes, neurons, skeletal myocytes)**, **manifests clinically as**:
   - Cardiomyocyte hypertrophy/dysfunction → **hypertrophic cardiomyopathy**, which under superimposed physiological stress (e.g., viral illness increasing metabolic demand) can **decompensate into fatal heart failure** (branch A, severe cases).
   - Neuronal/CNS energy failure → **developmental delay, hypotonia, intellectual disability, cortical visual impairment** (branch B, in more severely affected cases).
   - Skeletal muscle energy failure and structural mitochondrial abnormality (increased lipid deposition, enlarged/abnormal mitochondria on biopsy) → **myopathy, failure to thrive** (branch C).
   - In milder/incompletely penetrant biallelic genotypes (e.g., the fourth reported case), the phenotype may remain an **apparently isolated hypertrophic cardiomyopathy** without the multisystem/neurological involvement seen in the index case — illustrating variable severity depending on residual NDUFAF1/Complex I function (branch D, inferred from genotype-phenotype comparison across the four cases rather than directly demonstrated).

### Molecular Pathways
- Oxidative phosphorylation / electron transport chain, Complex I (NADH:ubiquinone oxidoreductase) — KEGG "Oxidative phosphorylation" pathway; Reactome "Complex I biogenesis" (R-HSA-6799198) and "MCIA complex [mitochondrial inner membrane]" (R-HSA-5689052).
- GO Biological Process: mitochondrial respiratory chain complex I assembly (**GO:0032981**); electron transport chain (**GO:0022900**).

### Cellular Processes
- Failure of mitochondrial protein complex biogenesis/proteostasis (misassembled intermediate degradation).
- Secondary metabolic reprogramming toward anaerobic glycolysis (lactate production) due to feedback inhibition of the TCA cycle.
- Cardiomyocyte hypertrophic remodeling in response to chronic energy deficit.

### Protein Dysfunction
NDUFAF1 dysfunction is a **loss-of-function/protein-instability** mechanism: pathogenic missense variants and an exon deletion destabilize the protein and its incorporation into the MCIA scaffold, rather than producing a toxic gain-of-function aggregate. Relevant ontology: UniProt Q9Y375 (NDUFAF1_HUMAN).

### Metabolic Changes
- Elevated blood/CSF **lactate** and lactate:pyruvate ratio (classic Complex I deficiency biomarker pattern).
- Reduced Complex I-dependent NADH oxidation; secondary effects on the TCA cycle flux.

### Tissue Damage Mechanisms
- Chronic energy deficit and possible reactive oxygen species (ROS) generation from a stalled electron transport chain (a general Complex I-deficiency mechanism; not specifically quantified for *NDUFAF1* in the retrieved literature) contribute to cardiomyocyte and myocyte injury.

### Biochemical Abnormalities
- **Isolated severe Complex I enzymatic deficiency** (~25% of control activity), confirmed biochemically in skeletal muscle in the index case, with normal activity of Complexes II–V (the defining biochemical signature of an "isolated" Complex I defect) ([OMIM #618234](https://www.omim.org/entry/618234)).

### Molecular Profiling / Advanced Technologies
No transcriptomic, proteomic, metabolomic, lipidomic, single-cell, or spatial-omics datasets specific to *NDUFAF1*/MC1DN11 patient tissue were identified in this search. Mechanistic insight instead comes from **biochemical reconstitution and cryo-EM structural studies of the MCIA complex** (Guerrero-Castillo et al.; the ACAD9/ECSIT/NDUFAF1 structural work) and from **patient fibroblast functional studies** (Fassone 2011; Kalantari 2025) showing reduced NDUFAF1 protein and abnormal assembly intermediates by Blue Native PAGE-type approaches.

**Suggested cell types (CL):** cardiac muscle myoblast/cardiomyocyte (CL:0000746); skeletal muscle fiber (CL:0000188); neuron (CL:0000540) — for the neurological phenotypes in severe cases.

**Sources:** [Guerrero-Castillo et al., Cell Reports 2020, PMID:32320651](https://pubmed.ncbi.nlm.nih.gov/32320651/); [Reactome R-HSA-5689052](https://reactome.org/content/detail/R-HSA-5689052); [Science Advances 2022 — NDUFAF1/cardiolipin](https://www.researchgate.net/publication/365515145_Insights_into_complex_I_assembly_Function_of_NDUFAF1_and_a_link_with_cardiolipin_remodeling); [EMBO Mol Med, Complex I deficiency and Leigh syndrome review](https://www.embopress.org/doi/full/10.15252/emmm.202013187); [OMIM #618234](https://www.omim.org/entry/618234); [Kalantari et al. 2025, PMID:39821332](https://pubmed.ncbi.nlm.nih.gov/39821332/)

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary organ:** **Heart** — hypertrophic cardiomyopathy is the unifying feature across all four reported cases, ranging from isolated to life-threatening.
- **Secondary/associated organ involvement:** Central nervous system (developmental delay, intellectual disability, cortical visual impairment, retinopathy), skeletal muscle (myopathy, failure to thrive), and cardiac conduction system (Wolff-Parkinson-White syndrome) in more severely affected individuals.
- **Body systems involved:** Cardiovascular system (primary); nervous system and musculoskeletal system (in severe/multisystem cases).
- Suggested UBERON terms: heart (UBERON:0000948); cardiac muscle tissue (UBERON:0001133); skeletal muscle tissue (UBERON:0001134); brain (UBERON:0000955); retina (UBERON:0000966).

### Tissue and Cell Level
- Cardiac and skeletal muscle: light-microscopic biopsy shows **increased lipid deposition** and **accumulation of enlarged, abnormal mitochondria** — a classic mitochondrial myopathy histopathological pattern.
- Cell types: cardiomyocyte (CL:0000746), skeletal muscle fiber/myocyte (CL:0000188), and (for the neurological features) neurons broadly (CL:0000540); retinal pigment epithelial cells for the pigmentary retinopathy (CL:0002586).

### Subcellular Level
- **Mitochondrion** (GO Cellular Component: mitochondrion, GO:0005739), specifically the **mitochondrial inner membrane** (GO:0005743, where Complex I and the MCIA assembly complex reside) and the **mitochondrial matrix**, where NDUFAF1 chaperone activity operates.

### Localization
- No specific lateralization pattern is expected or reported; the disease affects bilateral/symmetric organ systems (heart, whole-brain/CNS processes) consistent with a systemic energy-metabolism disorder rather than a focal structural lesion.

**Sources:** [OMIM #618234](https://www.omim.org/entry/618234); [GeneCards: NDUFAF1](https://www.genecards.org/card/NDUFAF1)

---

## 8. Temporal Development

### Onset
- **Age of onset:** Infantile — reported presentations at 11 months (failure to thrive, index case) with cardiac decompensation by 15 months; the fourth reported case likewise presented in early childhood with HCM. No adult-onset MC1DN11 case has been reported.
- **Onset pattern:** Can be **insidious** (failure to thrive as an early nonspecific sign) followed by an **acute** decompensation event (viral-illness-triggered heart failure in the index case), i.e., a subacute baseline state punctuated by acute crises.

### Progression
- **Disease stages:** Not formally staged (no consensus staging system exists for this ultra-rare entity); clinically distinguishable as (a) a compensated/subclinical phase, and (b) a decompensated/crisis phase (e.g., acute cardiac failure).
- **Progression rate:** Variable and case-dependent — **rapid/fatal** in the index case (death following viral-illness-triggered decompensation) versus an apparently **more stable/milder** course in the fourth reported case.
- **Disease course pattern:** Best characterized as **chronic with acute exacerbations** in the severe phenotype, versus a more **stable, isolated cardiac** phenotype in the mildest reported case.
- **Disease duration:** Can be fatal in infancy (index case) or persist as a chronic, apparently milder condition managed as HCM (fourth case) — true long-term natural history beyond early childhood is not established given the small number of reported patients.

### Patterns
- **Remission:** No spontaneous or treatment-induced remission has been documented; this is a structural/genetic enzymatic deficiency without a described remitting-relapsing pattern.
- **Critical periods:** Infancy appears to be the critical window of vulnerability across all published cases (onset within the first 1–2 years of life), likely reflecting the high cardiac/CNS energy demands of this developmental period colliding with a fixed genetic OXPHOS capacity deficit; intercurrent febrile/viral illness represents an additional situational "critical period" of vulnerability to acute decompensation.

**Sources:** [OMIM #618234](https://www.omim.org/entry/618234); [Kalantari et al. 2025, PMID:39821332](https://pubmed.ncbi.nlm.nih.gov/39821332/)

---

## 9. Inheritance and Population

### Epidemiology
- **MC1DN11-specific prevalence/incidence:** Not calculable — only **four molecularly confirmed cases** have been published to date (as of the 2025 report), making this one of the rarest of the >30 recognized nuclear-gene Complex I deficiency subtypes.
- **Broader context (isolated Complex I deficiency as a group):** Complex I deficiency is the **single most common enzymatic OXPHOS defect** in pediatric mitochondrial disease, accounting for roughly **40–50%** of childhood-onset OXPHOS disorders; primary mitochondrial disease overall affects at least **~1 in 5,000** individuals, with some estimates of Complex I deficiency incidence specifically around **1 in 50,000 live births** (region-dependent) ([MedlinePlus Genetics — Mitochondrial complex I deficiency](https://medlineplus.gov/genetics/condition/mitochondrial-complex-i-deficiency/); general mitochondrial disease epidemiology literature).

### Inheritance Pattern
- **Autosomal recessive (AR)** — both reported families carry biallelic (compound heterozygous) *NDUFAF1* variants, with unaffected heterozygous carrier parents in the index family ([OMIM #618234](https://www.omim.org/entry/618234)).

### Penetrance / Expressivity
- **Expressivity is markedly variable**, as emphasized by the 2025 report describing the phenotype spectrum as "highly heterogeneous," ranging from a comparatively mild, apparently isolated HCM to fatal infantile cardioencephalomyopathy. No data on incomplete penetrance in carriers (expected to be unaffected, as in classic AR disease) or on genetic anticipation are available — anticipation is not a feature expected in a non-repeat-expansion Mendelian AR disorder and none has been reported.
- **Germline mosaicism, founder effects, carrier frequency:** Not reported/established for *NDUFAF1*-MC1DN11 specifically; each family reported to date carries apparently private variants (no known founder population).
- **Consanguinity:** Not explicitly reported as a factor in the available case descriptions retrieved, though AR disease with private compound-heterozygous variants is compatible with either consanguineous or non-consanguineous unions.

### Population Demographics
- **Affected populations:** Cases reported to date are of **European (French)** and **Italian** ancestry (Fassone 2011 index case; Kalantari 2025 fourth case, Italian institutions); no broader ethnic/geographic clustering has been established given the small case count.
- **Sex ratio:** Insufficient data (n=4) to establish a sex distribution; autosomal recessive inheritance predicts no inherent sex bias.
- **Age distribution:** All reported cases are pediatric (infantile/early childhood onset).

**Sources:** [OMIM #618234](https://www.omim.org/entry/618234); [MedlinePlus Genetics: Mitochondrial complex I deficiency](https://medlineplus.gov/genetics/condition/mitochondrial-complex-i-deficiency/); [Kalantari et al. 2025, PMID:39821332](https://pubmed.ncbi.nlm.nih.gov/39821332/)

---

## 10. Diagnostics

### Clinical Tests
- **Laboratory tests:** Blood/CSF **lactate** (elevated; core biomarker), lactate:pyruvate ratio; skeletal/cardiac muscle biopsy for **biochemical Complex I enzymatic activity assay** (spectrophotometric NADH:ubiquinone oxidoreductase assay) — the index case showed isolated Complex I activity at ~25% of controls with normal other complexes.
- **Biopsy/histopathology:** Skeletal muscle biopsy showing increased lipid deposition and enlarged/abnormal mitochondria (light and electron microscopy); this is a nonspecific but supportive mitochondrial myopathy pattern.
- **Imaging:** Echocardiography is central for detecting and monitoring **hypertrophic cardiomyopathy**; brain MRI would be indicated in cases with neurological involvement (not specifically detailed for this gene in retrieved sources, but standard practice in Complex I deficiency work-up given the association with Leigh syndrome-spectrum imaging findings in other genes within this disease family).
- **Electrophysiology:** ECG for **Wolff-Parkinson-White syndrome** pre-excitation pattern, reported as an associated cardiac feature.
- **Ophthalmologic exam:** For pigmentary retinopathy and cortical visual dysfunction in more severely affected patients.

### Genetic Testing
- **Recommended approach:** Given the biochemical finding of isolated Complex I deficiency, **gene-panel or whole-exome sequencing (WES)** covering the >35 known nuclear Complex I structural and assembly-factor genes (including *NDUFAF1*, the *NDUFS*, *NDUFV*, *NDUFA*, other *NDUFAF* genes, *ACAD9*, *TMEM126B*, *ECSIT*, *TIMMDC1*) is the most efficient diagnostic strategy, given the extensive genetic heterogeneity of this biochemical phenotype.
- **Single-gene testing:** Feasible once biochemical/phenotypic suspicion narrows to *NDUFAF1* specifically (e.g., recurrent pattern of HCM + isolated Complex I deficiency), but WES/panel testing is generally preferred as first-line given phenotypic overlap across many causal genes.
- **Confirmatory functional studies:** Patient fibroblast studies (NDUFAF1 protein levels by Western blot; Complex I assembly intermediates by Blue Native PAGE) provide functional confirmation of variant pathogenicity, as performed in both published functional case studies.
- **Chromosomal microarray/structural variant detection:** Relevant for detecting intragenic deletions such as the exon-3 deletion described in the fourth case — standard WES may miss such structural variants, so complementary deletion/duplication analysis (e.g., MLPA or exome-based CNV calling) is advisable when only one causal allele is found by sequencing.
- **Not applicable:** Mitochondrial DNA testing, karyotyping, FISH, and repeat-expansion testing are not primarily indicated, since MC1DN11 is a nuclear (not mtDNA) AR disorder without a repeat-expansion or chromosomal-abnormality mechanism.

### Omics-Based Diagnostics
No RNA-seq, proteomic, metabolomic, or liquid-biopsy diagnostic modality has been specifically validated or reported for MC1DN11.

### Clinical Criteria / Differential Diagnosis
- No disorder-specific diagnostic consensus criteria exist. Diagnosis rests on the combination of (1) a compatible clinical phenotype (infantile HCM ± multisystem features), (2) biochemically confirmed isolated Complex I deficiency, and (3) biallelic pathogenic *NDUFAF1* variants with supportive functional evidence.
- **Key differentials:** Other genetic causes of infantile hypertrophic cardiomyopathy — sarcomeric-gene HCM, other nuclear Complex I assembly-factor disorders (*ACAD9*, *NDUFAF2*, *TIMMDC1*, *TMEM126B*), *NDUFS2*/*NDUFV2*-related Complex I disease (also associated with HCM/encephalomyopathy), Barth syndrome (cardiolipin-related, mechanistically relevant given NDUFAF1's cardiolipin link), and other primary mitochondrial cardiomyopathies. As the Kalantari 2025 report notes, "genetic causes of HCM are mostly related to sarcomeric genes," making mitochondrial/metabolic causes an important but easily overlooked differential in pediatric HCM work-up.

### Screening
- No population-level newborn or carrier screening program exists for *NDUFAF1* specifically; given its rarity and lack of founder-population enrichment, it is not a target of routine expanded carrier screening panels at this time. Family cascade testing (parental carrier testing, prenatal/preimplantation genetic testing in subsequent pregnancies) is appropriate once a proband's causal variants are identified.

**Sources:** [OMIM #618234](https://www.omim.org/entry/618234); [Kalantari et al. 2025, PMID:39821332](https://pubmed.ncbi.nlm.nih.gov/39821332/); [Fassone et al. 2011, PMID:21931170]

---

## 11. Outcome/Prognosis

### Survival and Mortality
- **Index case (Fassone et al. 2011):** Fatal — death following an episode of severe cardiac failure due to hypertrophic cardiomyopathy precipitated by a viral illness at 15 months of age.
- **Fourth reported case (Kalantari et al. 2025):** Described as clinically "simpler"/milder relative to prior cases, implying a more favorable short-term course, though long-term outcome data were not detailed in the retrieved abstract.
- No formal survival curves, 5-/10-year survival rates, or population-level mortality statistics exist given the extremely small reported cohort (n=4).

### Morbidity and Function
- Morbidity in the more severely affected reported cases includes developmental delay, intellectual disability, hypotonia/myopathy, and visual impairment (cortical visual dysfunction, pigmentary retinopathy) — implying substantial long-term functional impairment when the neurological phenotype is present.
- No standardized quality-of-life instrument data (EQ-5D, SF-36, PROMIS) have been applied to this specific patient population.

### Disease Course / Complications
- **Cardiac decompensation during intercurrent illness** is the dominant, life-threatening complication documented.
- Other complications by extrapolation from the general mitochondrial-disease literature (not specifically confirmed for this gene) could include arrhythmia (supported directly here by the reported Wolff-Parkinson-White association), growth failure, and progressive neurodevelopmental impairment.
- **Recovery potential:** Not established; given the structural/genetic nature of the enzymatic defect, recovery of Complex I function is not expected, though clinical stabilization (e.g., managing HCM medically) appears possible in milder genotype-phenotype combinations.

### Prognostic Factors
- The clearest prognostic signal identified across the four cases is **genotype/phenotype severity heterogeneity** — i.e., some biallelic *NDUFAF1* genotypes are compatible with a milder, isolated-cardiac phenotype, while others (index case) produce a fulminant multisystem, fatal disease. No formal biomarker-based prognostic model exists.
- Intercurrent infectious illness functions as an identified acute prognostic risk factor for decompensation.

**Sources:** [OMIM #618234](https://www.omim.org/entry/618234); [Kalantari et al. 2025, PMID:39821332](https://pubmed.ncbi.nlm.nih.gov/39821332/)

---

## 12. Treatment

There is **no disease-modifying or curative therapy** for MC1DN11 specifically; management follows the general supportive/symptomatic paradigm used across mitochondrial Complex I deficiencies, individualized to the organ systems involved.

### Pharmacotherapy
- **Empiric "mitochondrial cocktail" supplementation:** riboflavin (vitamin B2), thiamine, biotin, coenzyme Q10, and carnitine are used empirically across Complex I deficiency disorders, though robust evidence of efficacy specific to *NDUFAF1*-MC1DN11 is lacking ([UMDF: Complex I Deficiency](https://umdf.org/complex-i-deficiency/)).
  - Suggested NCIT terms: `NCIT:C15986` (Pharmacotherapy) as the generic action, with the specific agents as `therapeutic_agent` (e.g., CHEBI riboflavin, CHEBI coenzyme Q10, CHEBI carnitine).
- **Cardiac medical management:** Standard heart-failure/HCM pharmacotherapy (e.g., beta-blockers, diuretics as clinically indicated) would apply to the cardiac phenotype, though agent-specific details were not reported in the retrieved case literature.
- **Pharmacogenomics:** No *NDUFAF1*-specific pharmacogenomic guidance has been published.

### Advanced Therapeutics
- **Gene therapy, cell therapy, RNA-based therapy, targeted/immunotherapy:** None reported or in development specifically for *NDUFAF1*-MC1DN11 in the retrieved literature. (NCIT `C15238` Gene Therapy would be the relevant term should this become applicable in the future.)

### Surgical and Interventional
- No disease-specific surgical intervention reported; standard cardiology interventions (e.g., for arrhythmia management related to WPW, or advanced heart-failure interventions/transplantation in severe cardiomyopathy) would be considered per general HCM/heart-failure practice, though not specifically documented for this gene in the sources retrieved.

### Supportive and Rehabilitative
- **Dietary intervention:** Ketogenic diet is mentioned as a metabolic therapy option in Complex I deficiency broadly (NCIT `C15447` Dietary Intervention), though its specific use in MC1DN11 patients was not documented in the retrieved sources.
- **Rehabilitation:** Physical/occupational therapy (NCIT `C15302` Physical Therapy) would be applicable for patients with myopathy/hypotonia and developmental delay, per general mitochondrial-disease supportive care standards.
- **Genetic counseling** (NCIT `C15240`) is essential given the AR inheritance pattern and reproductive implications for parents.

### Experimental
- No registered clinical trials (ClinicalTrials.gov) specific to *NDUFAF1*-MC1DN11 were identified in this search.

### Treatment Outcomes
- No systematic treatment-response data exist given the small case series; the Kalantari et al. 2025 authors specifically emphasize that "establishing a genetic diagnosis in mitochondrial cardiomyopathy is challenging," and that precise molecular diagnosis is valuable primarily for **prognostic counseling and reproductive guidance** rather than for guiding a currently available targeted therapy.

### Treatment Strategy
- No disease-specific treatment algorithm or combination-therapy protocol exists; management is individualized and supportive, following general mitochondrial-disease and pediatric-cardiomyopathy practice guidelines.

**Sources:** [UMDF: Complex I Deficiency](https://umdf.org/complex-i-deficiency/); [Kalantari et al. 2025, PMID:39821332](https://pubmed.ncbi.nlm.nih.gov/39821332/)

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense (this is a fixed genetic disease); the only relevant "primary prevention" is **avoidance of known decompensation triggers** — e.g., prompt, aggressive management of intercurrent febrile/viral illness in a known affected child, given the documented risk of viral-illness-triggered fatal cardiac decompensation.
- **Secondary prevention:** Early diagnosis via biochemical Complex I assay and genetic confirmation allows **surveillance echocardiography** to detect and monitor hypertrophic cardiomyopathy before it becomes symptomatic/life-threatening.
- **Tertiary prevention:** Standard heart-failure/arrhythmia management to prevent complications (e.g., WPW-related arrhythmia surveillance) in already-affected individuals.
- **Immunization:** No disease-specific vaccine strategy exists, though standard-schedule immunization (e.g., influenza, RSV prophylaxis where age-appropriate) to reduce the burden of the specific infectious trigger implicated in decompensation would be a reasonable, though unstudied, preventive consideration.
- **Genetic screening/counseling:** **Genetic counseling** for parents of an affected child (recurrence risk 25% per pregnancy under AR inheritance) and **prenatal testing/preimplantation genetic diagnosis** are the primary applicable preventive/family-planning tools once causal variants are identified in a family, per standard AR-disease practice (no MC1DN11-specific screening program exists).
- **Public health/behavioral interventions:** Not applicable to this ultra-rare monogenic disorder.

**Sources:** [OMIM #618234](https://www.omim.org/entry/618234) (inference from documented viral-trigger decompensation and AR inheritance)

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring animal disease model (spontaneous veterinary case) attributable to *NDUFAF1* mutation was identified in this search.
- **Orthologous gene:** *Ndufaf1* is conserved in mouse (MGI:1916952, "NADH:ubiquinone oxidoreductase complex assembly factor 1") and other vertebrates, and the human protein itself is the ortholog of the fungal *Neurospora crassa* Cia30 assembly factor, underscoring deep evolutionary conservation of the Complex I assembly pathway from fungi to humans ([MGI:1916952](https://www.informatics.jax.org/marker/MGI:1916952); [GeneCards: NDUFAF1](https://www.genecards.org/card/NDUFAF1)).
- **Natural disease in companion/wild animals:** Not reported. Other Complex I assembly-factor genes (e.g., *ECSIT*) have documented mouse ENU mutant models with tissue-specific Complex I assembly defects (see Model Organisms below), but no comparable spontaneous *Ndufaf1* veterinary disease was found.
- **Zoonotic potential / cross-species transmission:** Not applicable — this is a non-infectious, purely genetic disorder.

**Sources:** [MGI:1916952](https://www.informatics.jax.org/marker/MGI:1916952); [GeneCards: NDUFAF1](https://www.genecards.org/card/NDUFAF1)

---

## 15. Model Organisms

- **Direct *Ndufaf1* knockout/knock-in models:** No published mouse, zebrafish, *Drosophila*, or *C. elegans* germline knockout model specific to *Ndufaf1* was identified in this search (searches for "Ndufaf1 knockout mouse," "Ndufaf1 zebrafish," and related terms returned no direct hits, in contrast to well-characterized models for sibling genes such as *Ndufs4* and *Ndufs2*). This represents a **documented gap** in the animal-model literature for this specific gene — a mouse gene record exists (MGI:1916952), but no disease-modeling knockout/knock-in phenotype paper was retrieved.
- **In vitro / cellular models used in the literature to date:**
  - **Patient-derived skin fibroblasts** — the primary model system used in both key publications (Fassone 2011; Kalantari 2025) to demonstrate reduced NDUFAF1 protein levels, abnormal Complex I assembly intermediates (by Blue Native PAGE-type analysis), and reduced Complex I enzymatic activity.
  - **Biochemical reconstitution / recombinant protein studies** of the MCIA complex (NDUFAF1 + ECSIT + ACAD9 ± TMEM126B), used to define the structural mechanism of NDUFAF1 function and its cardiolipin-remodeling link, though these are mechanistic protein-complex studies rather than whole-organism or whole-cell-line disease models per se ([Cell Reports 2020, PMID:32320651](https://pubmed.ncbi.nlm.nih.gov/32320651/); Science Advances 2022 cardiolipin paper).
- **Related Complex I assembly-factor animal models (informative by analogy, not direct *NDUFAF1* models):**
  - ***Ndufs4* knockout mouse** — the best-characterized Complex I-deficiency mouse model, recapitulating Leigh-syndrome-like neurological phenotypes and, when cardiac-restricted, severe hypertrophic cardiomyopathy — directly relevant as a phenotypic analogy for the cardiac mechanism seen in MC1DN11, even though it is a different gene (structural subunit vs. assembly factor) ([PLOS ONE, Ndufs4 cardiac knockout HCM model](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0094157); [Brain 2022 Ndufs4 review, PMID via Oxford Academic](https://academic.oup.com/brain/article/145/1/45/6446031)).
  - **ENU-induced *Ecsit* mutant mouse** — demonstrates tissue-specific differences in Complex I assembly defects depending on which MCIA-complex member is disrupted, directly relevant to interpreting NDUFAF1's tissue-specific (notably cardiac) vulnerability ([Cardiovascular Research 2023](https://academic.oup.com/cardiovascres/article/119/12/2213/7216980)).
  - ***ndufs2*−/− zebrafish** — a CRISPR/Cas9 Complex I-deficiency zebrafish model showing impaired survival, neuromuscular dysfunction, and multiple morphological abnormalities, illustrative of the zebrafish platform's utility for future *ndufaf1* modeling ([PMC12338652](https://pmc.ncbi.nlm.nih.gov/articles/PMC12338652/)).

### Model Characteristics and Applications
- **Phenotype recapitulation:** Available *Ndufs4* mouse cardiac-knockout and Leigh-syndrome models recapitulate hypertrophic cardiomyopathy and neurodegeneration respectively, providing indirect mechanistic support for the human MC1DN11 phenotype spectrum, but **no model has yet directly tested loss of NDUFAF1 in vivo**.
- **Model limitations:** Because no *Ndufaf1*-specific animal model exists, extrapolations from *Ndufs4*/*Ecsit* models cannot capture assembly-factor-specific (as opposed to structural-subunit-specific) consequences, and the human genotype-phenotype heterogeneity documented across the four clinical cases (mild vs. fatal) has no corresponding graded animal model to explain it mechanistically.
- **Research applications / opportunity:** Given the conserved fungal-to-human Cia30/NDUFAF1 assembly pathway and the zebrafish/mouse platforms already validated for sibling Complex I genes, generating an *Ndufaf1* zebrafish or mouse model represents a clear, currently unmet research opportunity for studying MCIA-complex-specific pathophysiology and for future therapeutic screening.

**Resources:** [MGI:1916952](https://www.informatics.jax.org/marker/MGI:1916952) (mouse gene record, no disease-model publication linked); [PLOS ONE Ndufs4 cardiac model](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0094157); [Cardiovascular Research 2023, Ecsit ENU mouse](https://academic.oup.com/cardiovascres/article/119/12/2213/7216980); [PMC12338652, ndufs2 zebrafish](https://pmc.ncbi.nlm.nih.gov/articles/PMC12338652/)

---

## Summary of Key Data Gaps (for curation triage)

1. **Only 4 published patients** worldwide — no natural-history cohort, no formal survival/QOL data, no population-level prevalence figure specific to this gene.
2. **No direct *Ndufaf1* animal model** (mouse/zebrafish/fly) has been published; mechanistic inference currently relies on sibling-gene models (*Ndufs4*, *Ecsit*) and in vitro MCIA-complex biochemistry/structural work.
3. **gnomAD constraint metrics (pLI/LOEUF) and formal ClinVar classifications** for the specific reported *NDUFAF1* alleles were not resolved in this search session and should be looked up directly before finalizing variant curation.
4. **No dedicated GeneReviews chapter** exists for MC1DN11/*NDUFAF1*; the disease-specific detail is scattered across OMIM and the four primary case reports.
5. Treatment section is entirely **extrapolated from general Complex I deficiency practice** (mitochondrial cocktail, supportive cardiac care) — no *NDUFAF1*-specific treatment-response or trial data exist.

---

### Master Source List

- [OMIM #618234 — MITOCHONDRIAL COMPLEX I DEFICIENCY, NUCLEAR TYPE 11; MC1DN11](https://www.omim.org/entry/618234)
- [OMIM *606934 — NDUFAF1](https://omim.org/entry/606934)
- [Disease Ontology Browser — DOID:0112089](https://www.informatics.jax.org/disease/DOID:0112089)
- [Orphanet — Isolated complex I deficiency (ORPHA:2609)](https://www.orpha.net/en/disease/detail/2609)
- Fassone E, et al. "Mutations in the mitochondrial complex I assembly factor NDUFAF1 cause fatal infantile hypertrophic cardiomyopathy." J Med Genet. 2011. PMID:21931170.
- Kalantari S, et al. "Mitochondrial Complex I Deficiency: Unraveling the Relevance of NDUFAF1 in Pediatric Hypertrophic Cardiomyopathy." Am J Med Genet A. 2025. [PMID:39821332](https://pubmed.ncbi.nlm.nih.gov/39821332/)
- Vogel RO, et al. "Human mitochondrial complex I assembly is mediated by NDUFAF1." FEBS J. 2005. [PMID:16218961](https://pubmed.ncbi.nlm.nih.gov/16218961/)
- Guerrero-Castillo S, et al. "Dissecting the Roles of Mitochondrial Complex I Intermediate Assembly Complex Factors in the Biogenesis of Complex I." Cell Reports. 2020. [PMID:32320651](https://pubmed.ncbi.nlm.nih.gov/32320651/)
- "Insights into complex I assembly: Function of NDUFAF1 and a link with cardiolipin remodeling." Science Advances. 2022. [ResearchGate summary](https://www.researchgate.net/publication/365515145_Insights_into_complex_I_assembly_Function_of_NDUFAF1_and_a_link_with_cardiolipin_remodeling)
- [Reactome R-HSA-5689052 — MCIA complex [mitochondrial inner membrane]](https://reactome.org/content/detail/R-HSA-5689052)
- [Complex I deficiency and Leigh syndrome through the eyes of a clinician, EMBO Mol Med](https://link.springer.com/article/10.15252/emmm.202013187)
- [MedlinePlus Genetics — Mitochondrial complex I deficiency](https://medlineplus.gov/genetics/condition/mitochondrial-complex-i-deficiency/)
- [UMDF — Complex I Deficiency](https://umdf.org/complex-i-deficiency/)
- [GeneCards — NDUFAF1 (CIA30)](https://www.genecards.org/card/NDUFAF1)
- [MGI:1916952 — Ndufaf1 (mouse)](https://www.informatics.jax.org/marker/MGI:1916952)
- [PLOS ONE — Ndufs4 cardiac-knockout hypertrophic cardiomyopathy mouse model](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0094157)
- [Cardiovascular Research 2023 — ENU Ecsit mouse, tissue-specific Complex I assembly](https://academic.oup.com/cardiovascres/article/119/12/2213/7216980)
- [PMC12338652 — ndufs2−/− zebrafish Complex I deficiency model](https://pmc.ncbi.nlm.nih.gov/articles/PMC12338652/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 14 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032617` (2 mentions) - the report calls it "MONDO"; MONDO calls it **mitochondrial complex I deficiency, nuclear type 11**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001263` (1 mention) - the report calls it "Developmental delay"; HP calls it **Global developmental delay**, and lists "Developmental delay" among its other names
- `HP:0100704` (1 mention) - the report calls it "Cortical visual impairment"; HP calls it **Cerebral visual impairment**, and lists "Cortical visual impairment" among its other names
- `HP:0025580` (1 mention) - the report calls it "Abnormal mitochondrial morphology"; HP calls it **Abnormal right atrium morphology**
- `CL:0000746` (2 mentions) - the report calls it "Cell types: cardiomyocyte"; CL calls it **cardiac muscle cell**, and lists "cardiomyocyte" among its other names
- `UBERON:0000948` (1 mention) - the report calls it "Suggested UBERON terms: heart"; UBERON calls it **heart**, and lists "vertebrate heart" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MGI:1916952` - called "Sources", "Resources", "Ndufaf1"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.