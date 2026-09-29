---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-24T16:59:42.613284'
end_time: '2026-09-24T17:04:05.313266'
duration_seconds: 262.7
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Immunodeficiency 128
  mondo_id: MONDO:0975834
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
  web_search_requests: 8
  num_turns: 12
  total_cost_usd: 1.1466713999999998
  session_id: fd65d8eb-852b-5a9d-91de-140beff025e2
  stop_reason: end_turn
  assistant_text_blocks: 2
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderBillingError
  status_code: 402
  remedy: the account is out of credits
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 10
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:33529166
  relevance_assessed: 4
  on_topic: 4
  needs_review: true
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 40
  verified: 39
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 15
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0032179
    reported_labels:
    - verify exact CD8 lymphopenia term
    ontology_label: Abnormal circulating globulin concentration
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 128
- **MONDO ID:** MONDO:0975834 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 128** covering all of the
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

I'll research "Immunodeficiency 128" now, using web search and primary sources, then produce the complete report inline.

# Immunodeficiency 128 (IMD128) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Immunodeficiency-128 (IMD128) is an autosomal recessive combined immunodeficiency (CID) caused by a homozygous missense mutation in *COPG1*, which encodes the γ1 subunit of the coat protein complex I (COPI). COPI mediates retrograde vesicular trafficking of cargo — including KDEL-motif-bearing endoplasmic reticulum (ER) chaperones — from the Golgi back to the ER. The single reported kindred (five siblings of consanguineous Omani parents) presented in the first year of life with recurrent bacterial and viral infections, failure to thrive, hepatitis, and progressive bronchiectasis, with a combined (T- and B-cell) immunodeficiency phenotype. The molecular mechanism established by the discovery study is that loss of γ1-COP–mediated KDEL-receptor engagement impairs retrieval of chaperones (BiP/GRP78, calreticulin, protein disulfide isomerase) to the ER, producing exaggerated, activation-induced ER stress and unfolded protein response (UPR) signaling selectively in lymphocytes — explaining the immune-restricted phenotype despite COPI's ubiquitous cellular role (Bainter et al., 2021, PMID:33529166).

**Key identifiers:**
- **OMIM phenotype:** #620983 — IMMUNODEFICIENCY 128; IMD128 (https://omim.org/entry/620983)
- **OMIM gene:** *615525 — COATOMER PROTEIN COMPLEX, SUBUNIT GAMMA-1; COPG1
- **Gene symbol / HGNC:** COPG1, HGNC:2236
- **Cytogenetic location:** 3q21.3
- **MONDO:** MONDO:0975834 (as supplied by the curation stub — not independently cross-verified against a MONDO release in this session; verify with `runoak` before binding)
- **Inheritance:** Autosomal recessive
- **Primary literature source:** Bainter W, et al. "Combined immunodeficiency due to a mutation in the γ1 subunit of the coat protein I complex." *J Clin Invest.* 2021. PMID:33529166 (https://www.jci.org/articles/view/140494)

**Synonyms/alternative names:** COPG1 deficiency; γ1-COP deficiency; combined immunodeficiency due to COPG1 mutation. No ICD-10/ICD-11 code specific to this ultra-rare monogenic entity was found (it would fall under the broad "Combined immunodeficiency, unspecified" / D81 family in ICD-10). No dedicated MeSH heading exists; it is indexed under "Severe Combined Immunodeficiency" and "COPI Vesicle Coat"-adjacent terms in PubMed.

**Data provenance:** All disease-level information here derives from a single aggregated disease-mechanism study (whole-exome sequencing of an index family plus mechanistic mouse/cell-line follow-up) rather than an EHR-based cohort or registry — this is a gene-discovery paper, not population-level disease surveillance. There is no OMIM Clinical Synopsis text retrievable in this session (OMIM blocked direct fetch with HTTP 403); the clinical/laboratory detail below is drawn from the JCI primary article and searches, not the OMIM Clinical Synopsis itself — **this is a gap to independently verify against OMIM's full entry before curation** (flagging per the attribution rule: I did not access omim.org directly).

---

## 2. Etiology

**Disease Causal Factor:** Purely genetic/monogenic. Homozygosity for the *COPG1* missense variant c.1954A>G (p.Lys652Glu, p.K652E) is the sole reported cause. No environmental, infectious, or multifactorial contribution to disease initiation is described; the clinical phenotype's severity, however, is modulated by environmental microbial exposure (see Mechanism section — mouse cohousing data).

**Genetic risk factors:**
- The single causal variant identified to date is homozygous *COPG1* p.K652E (Bainter et al. 2021, PMID:33529166), found in 5 affected siblings, heterozygous (carrier, unaffected) in both parents — consistent with autosomal recessive inheritance.
- **Consanguinity** is the dominant identified genetic/demographic risk factor: the parents were first-degree or close relatives from Oman, and consanguinity is the mechanism by which a rare recessive allele became homozygous in multiple siblings.
- No modifier genes, no digenic contribution, and no other *COPG1* alleles have been reported in the literature to date — this remains a single-family, single-variant disease as of this search (September 2026).
- I was unable to retrieve COPG1-specific gnomAD constraint metrics (pLI / LOEUF / missense Z) in this session; this should be pulled directly from the gnomAD browser before curation rather than assumed. COPG1 is broadly expressed and essential (it is the major γ-COP paralog used in most tissues, versus the minor paralog γ2-COP/COPG2), so a priori it is plausible the gene is constrained against loss-of-function, but I have no sourced number to cite.

**Environmental risk factors:** None reported as causal. However, environmental microbial exposure is a documented **disease-severity modifier** (not a cause): in the *Copg1^K652E* mouse model, animals raised under specific-pathogen-free (SPF) conditions had a comparatively mild baseline phenotype (hypogammaglobulinemia, defective antibody responses, but grossly normal lymphocyte numbers/proliferation), whereas cohousing with pet-store mice (i.e., exposure to a naturalistic, diverse microbial burden) for 22 days precipitated overt disease: progressive weight loss to ~70% of baseline, T-cell lymphopenia, severely impaired T-cell proliferation, hypergammaglobulinemia, and elevated serum TNF-α, IFN-γ, and IL-6 (Bainter et al. 2021, PMID:33529166). This is strong evidence for a **gene-by-environment interaction**: the *COPG1* mutation creates increased susceptibility to ER stress under the high secretory demand imposed by real-world pathogen exposure, and a low-antigen-burden environment can mask or attenuate the phenotype.

**Protective factors:** None identified in the human literature. In the mouse model, the chemical chaperone **tauroursodeoxycholic acid (TUDCA)** — a bile-acid-derived ER-stress-relieving agent — substantially reversed multiple phenotypic and molecular defects both in vitro and in vivo (see Treatment, below); this is best framed as a pharmacologic/therapeutic rescue rather than a naturally occurring protective factor, but it is directly relevant to the disease's gene-environment mechanism (buffering ER stress reduces phenotype severity).

**Gene-environment interaction:** As above — the core mechanistic insight of the primary paper is precisely a G×E interaction: γ1-COP loss of function creates latent ER-stress vulnerability that is unmasked specifically by the high secretory/proliferative demand lymphocytes experience upon antigenic/microbial activation. This is the central causal-chain logic for the mechanism section below.

---

## 3. Phenotypes

All phenotypes below are drawn from the 5-patient Omani sibling cohort in Bainter et al. 2021 (PMID:33529166); frequencies are reported as fractions of 5 unless stated otherwise. Suggested HPO terms are provided for KB curation; these are leads and must be verified against the HPO ontology before binding.

| Phenotype | Type | Onset/Frequency | Suggested HPO term |
|---|---|---|---|
| Recurrent bacterial respiratory infections (H. influenzae, S. pneumoniae, Moraxella) | Symptom/clinical sign | Onset in first year of life; all 5 patients | HP:0002090 Bronchopneumonia / HP:0011947 Recurrent bronchopulmonary infections |
| Bronchiectasis | Physical/imaging finding | Chronic; 3/5 patients | HP:0002110 Bronchiectasis |
| Chronic/persistent CMV viremia | Laboratory abnormality | Persistent; all 5 patients | HP:0033132 (or free-text — no dedicated "CMV viremia" HPO term is standard; consider HP:0002718 Recurrent infections plus a `qualifiers`/notes annotation naming the pathogen) |
| Chronic EBV viremia | Laboratory abnormality | Persistent; 2/5 patients | see above |
| Parvovirus B19 viremia | Laboratory abnormality | 1/5 patients | see above |
| Failure to thrive (weight/height <3rd percentile) | Physical/growth | Chronic, early-onset | HP:0001508 Failure to thrive |
| Hepatitis | Clinical sign | Present in all 5 patients | HP:0012115 Chronic hepatitis (or HP:0002240 Hepatomegaly if hepatomegaly specifically documented — verify from full text) |
| Death from respiratory failure/multiorgan dysfunction | Outcome | Patient 4, age 3.5 years | HP:0002205 Recurrent respiratory infections as contributor; mortality is an outcome field, not an HPO phenotype |
| CD4+ T-cell lymphopenia | Laboratory abnormality | Severe; all 5 patients (with one patient reported normal at birth, declining later) | HP:0005403 CD4-positive T-cell lymphopenia |
| Variable/modest CD8+ T-cell lymphopenia | Laboratory abnormality | Variable; present in a subset | HP:0032179 (verify exact CD8 lymphopenia term) |
| Decreased NK cells | Laboratory abnormality | Variable | HP:0040218 Decreased NK cell number (verify) |
| Poor T-cell proliferation to PHA/anti-CD3 | Laboratory/functional | Present | HP:0032234 Impaired T cell proliferation (verify) |
| Impaired antibody production / poor vaccine response (tetanus, diphtheria, HBV, measles) | Laboratory/functional | Poor booster response (<4-fold titer rise); absent HBV and measles responses | HP:0002846 Abnormal T cell physiology / HP:0002846-adjacent; more precisely HP:0031409 Abnormal antibody level or a vaccine-response-specific term — verify |
| Diminished in-vitro IgG secretion (B cells stimulated with anti-CD40+IL-4) | Laboratory/functional (ex vivo assay) | Present | Not a clinical HPO phenotype per se — functional assay finding, appropriate for `biochemical`/functional description rather than `phenotypes` |
| Elevated or normal serum IgG; normal/near-normal IgA, IgM | Laboratory | Variable | HP:0002850 Decreased circulating IgG level does NOT apply uniformly (IgG was normal/elevated) — do not over-assert |

**Severity/progression:** Onset is uniformly in the first year of life (congenital/infantile-onset CID). The course is progressive in at least one patient (fatal at 3.5 years) and chronic/persistent in survivors (chronic viremia, progressive bronchiectasis). Severity appears to fluctuate with microbial/antigenic exposure burden, consistent with the mouse-model G×E data above — this is an inference from the animal model, not directly demonstrated longitudinally in the human patients within the source material I retrieved.

**Quality of life impact:** Not formally studied (no PROMIS/EQ-5D/SF-36 data found); QoL impact can be reasonably inferred as substantial given chronic infection burden, growth failure, and one death, but this is inference, not sourced measurement — flag as such in any KB `notes:`.

---

## 4. Genetic/Molecular Information

**Causal gene:** *COPG1* (HGNC:2236; OMIM *615525; chromosome 3q21.3). Encodes the γ1 subunit of the heptameric coatomer (COPI) complex (subunits α/COPA, β/COPB1, β′/COPB2, γ/COPG1, δ/ARCN1, ε/COPE, ζ/COPZ1), which coats vesicles budding from the Golgi for retrograde transport to the ER.

**Pathogenic variant:**
- **Variant:** c.1954A>G; p.Lys652Glu (p.K652E) (NM_016128 reference transcript implied by standard nomenclature; exact transcript ID not independently confirmed in this session — verify before curation)
- **Zygosity:** Homozygous in all 5 affected siblings; heterozygous (carrier, clinically unaffected) in both parents
- **Variant type:** Missense
- **Classification:** Not independently retrieved from ClinVar in this session — should be checked via ClinVar/VarSome before curation (the variant is very likely listed given the JCI publication, but I have not confirmed the classification string)
- **Population frequency:** Not found in the search results retrieved (gnomAD-specific allele frequency for this exact variant was not confirmed in this session — should be checked directly)
- **Origin:** Germline
- **Functional consequence:** Loss-of-function at the level of a specific protein-protein interaction (structural/interaction-selective LOF) rather than global loss of γ1-COP protein or complete abrogation of all COPI function. Structural modeling in the primary paper predicts the mutation disrupts two stabilizing bonds in the appendage domain of γ1-COP: "a salt bridge between K652 and the carboxyl side chain of E757 and a hydrogen bond between K652 and the main chain carbonyl oxygen of D762" (Bainter et al. 2021, PMID:33529166). Functionally, the mutant coatomer retains normal binding to classic dilysine-motif cargo (e.g., Wbp1) but loses direct binding to the KDEL receptor (KDELR) cytoplasmic tail — i.e., a **selective, cargo-specific trafficking defect**, not a general COPI assembly failure.

**Modifier genes:** None established. The paper does note that the paralogous subunit γ2-COP (encoded by *COPG2*) does not compensate for γ1-COP loss in lymphoid tissue, which may explain the immune-restricted phenotype despite COPI's role in all cells — γ2-COP may substitute sufficiently in non-lymphoid tissues, a mechanistic hypothesis rather than a formally proven modifier relationship.

**Epigenetic information:** None reported; not applicable/not studied for this disorder.

**Chromosomal abnormalities:** None — this is a single-nucleotide missense substitution, not a structural/copy-number variant.

**Suggested gene binding for KB:** `gene_term` → `hgnc:2236` (COPG1); `functional_impact_category` on the `genetic_context` block should likely be a selective/partial loss-of-function category (e.g., `PARTIAL_LOSS_OF_FUNCTION`) rather than a full `LOSS_OF_FUNCTION`, given the interaction-selective mechanism — this is a curatorial judgment call to make against the primary paper's own framing, not something I am asserting definitively here.

---

## 5. Environmental Information

**Environmental factors:** Not causal for disease initiation (monogenic recessive disease). The key environmental factor is **microbial/antigenic exposure burden as a disease-severity modifier**, demonstrated experimentally in the mouse model via cohousing with pet-store mice (a standard model for simulating "wild"/naturalistic microbial exposure) versus SPF housing (Bainter et al. 2021, PMID:33529166). No human environmental epidemiology (toxin, occupational, pollution) is relevant or reported.

**Lifestyle factors:** Not applicable — this is an early-onset monogenic pediatric CID; no lifestyle/behavioral contribution is described.

**Infectious agents:** Infection is a *consequence/manifestation* of the immunodeficiency rather than a cause of the disease itself, but specific pathogens recur prominently and are clinically important for the disease's natural history:
- Bacterial: *Haemophilus influenzae*, *Streptococcus pneumoniae*, *Moraxella* species (recurrent respiratory infections/pneumonia)
- Viral (chronic/persistent viremia, reflecting impaired antiviral clearance): cytomegalovirus (CMV, all 5 patients), Epstein-Barr virus (EBV, 2/5 patients), parvovirus B19 (1/5 patients)

For an `environmental[]` entry in a KB curation, these would likely be modeled with `environmental_effect: EXACERBATES` or as downstream infection phenotypes rather than as `TRIGGERS` of the underlying disease (the disease is present from birth/genetically; infections exacerbate/reveal the clinical course).

---

## 6. Mechanism / Pathophysiology

### Causal chain (ordered, from the primary paper's mechanistic model)

1. Homozygous *COPG1* c.1954A>G (p.K652E) **disrupts** the appendage-domain structure of γ1-COP, abolishing two predicted stabilizing bonds (K652–E757 salt bridge; K652–D762 hydrogen bond). *(Demonstrated: structural modeling + biochemical binding assays.)*
2. The structurally altered γ1-COP **fails to bind** the cytoplasmic KDEL-receptor (KDELR) tail, while retaining normal binding to classic dilysine-motif cargo such as Wbp1 — i.e., a cargo-selective defect in coatomer function rather than global COPI failure. *(Demonstrated: direct binding assays.)*
3. Loss of coatomer–KDELR engagement **impairs retrograde Golgi-to-ER retrieval** of KDEL-bearing ER-resident chaperones — BiP/GRP78, calreticulin, protein disulfide isomerase (PDI) — leaving them mislocalized toward/at the Golgi instead of recycled to the ER. *(Demonstrated: patient fibroblast VSVGts-KDELR/GM130 colocalization assay showing impaired retrograde transport.)*
4. Chronic chaperone mislocalization **reduces the ER's folding/quality-control capacity**, which is normally buffered at baseline but becomes rate-limiting under high secretory demand. *(Inferred from downstream UPR activation data; not directly visualized as "folding failure" per se.)*
5. Upon lymphocyte activation (antigen receptor engagement, cytokine stimulation), the massive increase in secretory protein synthesis (immunoglobulin in B cells; cytokines in T cells) **exceeds the ER's now-diminished folding capacity**, precipitating pathological ER stress selectively in activated — but not resting — B and T cells. *(Demonstrated: increased Xbp1/spliced Xbp1 (sXbp1), elevated BiP (Hspa5) expression, PERK-pathway activation with increased CHOP in activated mutant cells; reduced ER size in mutant B cells.)*
6. Sustained/exaggerated unfolded protein response (UPR) signaling in activated B cells **impairs IgG secretion** despite normal plasmablast differentiation and normal class-switch recombination — i.e., a post-differentiation secretory bottleneck rather than a defect in B-cell developmental commitment. *(Demonstrated: normal CSR/plasmablast markers, but diminished IgG output.)*
7. In activated T cells, UPR/PERK-CHOP activation **drives increased apoptosis** and reduced cell viability, which secondarily **reduces IFN-γ output** (a viability effect, not an intrinsic cytokine-production defect) while proliferation and activation-marker expression remain broadly normal. *(Demonstrated: apoptosis assays; proliferation and marker studies.)*
8. Clinically, impaired antigen-specific antibody production (from step 6) and impaired T-cell survival/effector persistence (from step 7) together **produce a combined humoral and cellular immunodeficiency**, manifesting as recurrent bacterial respiratory infections, chronic viremia (CMV/EBV/parvovirus B19), and poor vaccine responses. *(Clinical observation in the index family, connected to the cellular mechanism by the paper's overall argument — this final clinical link is the paper's central inferential claim rather than a directly traced single-cell-to-bedside proof.)*
9. **Branch — environmental modulation:** Under low antigenic burden (SPF housing in mice), the residual UPR-buffering capacity is sufficient to keep the phenotype relatively mild (hypogammaglobulinemia, poor antibody response only); under high/naturalistic microbial exposure (pet-store cohousing), cumulative secretory/proliferative demand overwhelms buffering, producing overt lymphopenia, weight loss, and systemic inflammatory cytokine elevation (TNF-α, IFN-γ, IL-6) — showing the causal chain above is exposure-dependent in severity, not fixed. *(Demonstrated directly in the mouse model.)*
10. **Therapeutic rescue arm:** Pharmacologic ER-stress relief with TUDCA (a chemical chaperone) normalizes sXbp1/Hspa5 expression, restores B-cell IgG secretion, corrects T-cell survival/IFN-γ output in vitro, and reverses antibody-response defects and the pet-store-exposure-induced phenotype in vivo — providing causal (not merely correlative) support for steps 4–8 by showing that relieving ER stress specifically reverses the downstream immune defects. *(Demonstrated: in vitro and in vivo TUDCA rescue experiments.)*

### Category detail

- **Molecular pathways:** COPI-mediated retrograde vesicular trafficking (Golgi→ER); KDEL-receptor cargo-retrieval pathway; IRE1–XBP1 and PERK–CHOP arms of the unfolded protein response (UPR). Suggested GO terms: GO:0006890 (retrograde vesicle-mediated transport, Golgi to ER); GO:0030968 (endoplasmic reticulum unfolded protein response); GO:0036498 (IRE1-mediated unfolded protein response); GO:0036499 (PERK-mediated unfolded protein response).
- **Cellular processes:** Activation-induced apoptosis in T cells (GO:0006915 apoptotic process); impaired antibody secretion in B cells (GO:0002377 immunoglobulin production, or more specifically antibody secretion process — verify exact GO ID); ER stress response (GO:0034976 response to endoplasmic reticulum stress).
- **Protein dysfunction:** γ1-COP loses a specific protein-protein interaction (KDELR binding) via disruption of two intramolecular stabilizing bonds in its appendage domain — a structurally localized, interaction-selective defect rather than global misfolding/instability of γ1-COP itself. Suggested UniProt entry: COPG1_HUMAN (UniProt Q9Y678).
- **Biochemical abnormalities:** Defective KDEL-receptor engagement by coatomer; secondary chaperone (BiP/GRP78, calreticulin, PDI) mislocalization; secondary XBP1 splicing and CHOP induction as UPR markers.
- **Immune system involvement:** Combined immunodeficiency — impaired humoral immunity (poor specific antibody responses despite normal B-cell numbers/differentiation) and impaired cellular immunity (CD4+ T-lymphopenia, reduced T-cell survival upon activation, poor T-cell proliferation to mitogen/anti-CD3). This is not autoimmunity/immune dysregulation (contrast with COPA syndrome, below) but a bona fide immunodeficiency.
- **Cell types/tissue involvement:** Activated CD4+ and CD8+ T cells; activated (antigen/CD40+IL-4-stimulated) B cells and plasmablasts. Suggested CL terms: CL:0000624 (CD4-positive, alpha-beta T cell), CL:0000625 (CD8-positive, alpha-beta T cell), CL:0000236 (B cell), CL:0000980 (plasmablast).
- **Advanced/omics data:** No transcriptomic, proteomic, single-cell, or spatial datasets were identified as publicly deposited for this specific disease in the sources retrieved; the primary paper's UPR-marker data (Xbp1/sXbp1, Hspa5, CHOP) were generated by targeted qPCR/immunoblot rather than genome-wide profiling, as best I can determine from the retrieved summary. Verify against the full JCI methods/supplement before asserting "no omics data exist."

### Cross-paralog comparative mechanism (relevant differential/context)

Other COPI-subunit diseases illustrate that different subunits within the same heptameric complex can produce distinct immunophenotypes:
- **COPA syndrome** (autosomal dominant, *COPA*, α-COP; OMIM #601924 gene) causes an immune **dysregulation**/autoinflammatory phenotype (interstitial lung disease ± pulmonary hemorrhage, inflammatory arthritis, immune-mediated kidney disease), mechanistically linked to aberrant STING pathway activation from COPI deficiency (Nature Communications 2022, PMID:35484149; Watkin et al., PMC6372856).
- **COPB1 deficiency** (*COPB1*, β-COP) causes Baralle–Macken syndrome, combining neurodevelopmental features (global developmental delay, intellectual disability, early-onset cataracts) with combined immunodeficiency features (neutropenia, lymphopenia, impaired specific antibody responses) — a broader multisystem phenotype than IMD128 (PMID:41676145).
- **COPB2** loss-of-function variants cause a distinct skeletal/microcephaly phenotype, without the same immunodeficiency emphasis.

This positions IMD128/COPG1 deficiency as the coatomer-subunit disorder with the most immunologically "pure" combined-immunodeficiency phenotype identified to date, useful context for the KB's `classifications` (IUIS immunodeficiency category) and for distinguishing lump/split decisions from COPA syndrome and COPB1 deficiency, which should remain separate disease entries given their genetically and mechanistically distinct (dominant immune-dysregulation vs. recessive multisystem vs. recessive pure-CID) natures.

---

## 7. Anatomical Structures Affected

- **Organ level:** Primary — respiratory system (recurrent pneumonia, bronchiectasis) and lymphoid/immune system (lymphopenia, impaired antibody production). Secondary — liver (hepatitis, present in all 5 patients), growth (failure to thrive, a systemic/endocrine-adjacent secondary effect). Suggested UBERON terms: UBERON:0001004 (respiratory system), UBERON:0002048 (lung), UBERON:0002107 (liver), UBERON:0002405 (immune system).
- **Tissue/cell level:** Bronchial/pulmonary tissue (bronchiectasis); hepatic parenchyma; lymphoid tissue — specifically activated T and B lymphocytes as the mechanistically critical cell population (see Mechanism section for CL terms).
- **Subcellular level:** Endoplasmic reticulum (chaperone retrieval failure, UPR activation; GO:0005783 endoplasmic reticulum) and Golgi apparatus (site of COPI vesicle budding and KDELR mislocalization; GO:0005794 Golgi apparatus). Suggested GO Cellular Component terms: GO:0030137 (COPI-coated vesicle), GO:0000139 (Golgi membrane).
- **Localization:** No lateralization pattern reported (systemic/multi-organ, bilateral pulmonary disease implied by "bronchiectasis" without laterality specified).

---

## 8. Temporal Development

- **Onset:** Infantile — recurrent infections beginning in the first year of life in all 5 reported patients. One patient (P5) had normal CD4+/CD8+ counts documented at birth, suggesting T-cell lymphopenia may develop postnatally/progressively rather than being present in utero — an important nuance for framing "onset."
- **Onset pattern:** Insidious/chronic rather than acute, punctuated by recurrent infectious episodes.
- **Progression:** Progressive and chronic. Bronchiectasis (an anatomically progressive, largely irreversible airway process) developed in 3/5 patients. One patient (P4) died at 3.5 years of age from respiratory failure and multiorgan dysfunction, indicating a potentially fatal, progressive course in at least a subset.
- **Disease course pattern:** Chronic-persistent with recurrent infectious exacerbations (viremia is described as "persistent"/"chronic" rather than episodic-clearing).
- **Duration:** Chronic, lifelong in survivors (no report of spontaneous resolution).
- **Remission:** No spontaneous remission reported; TUDCA-based pharmacologic rescue in the mouse model is the only intervention shown to reverse (not merely stabilize) components of the phenotype, and this is preclinical, not yet a demonstrated human remission-inducing therapy.
- **Critical periods:** Infancy/early childhood is the critical period for clinical presentation and, per the fatal case, mortality risk; no data on prenatal/neonatal screening windows.

---

## 9. Inheritance and Population

- **Epidemiology:** IMD128 is described in exactly one kindred (5 affected siblings from one consanguineous Omani family) as of the primary 2021 publication — no formal prevalence or incidence estimate exists; it should be classified as ultra-rare / cases-in-literature only (n=5) for any `Prevalence` record (`measure_type: CASES_IN_LITERATURE`, `prevalence_class: NOT_YET_DOCUMENTED` or an ultra-rare qualitative tier if only "rare" language is used — do not fabricate a numeric rate).
- **Inheritance pattern:** Autosomal recessive (confirmed — homozygous in affected siblings, heterozygous carrier parents).
- **Penetrance:** Appears complete among the 5 homozygous siblings reported (all were symptomatic), though the sample size is too small to make a formal penetrance estimate, and possible variability is suggested by P5's normal birth T-cell counts versus later lymphopenia.
- **Expressivity:** Variable — bronchiectasis in 3/5, chronic EBV viremia in 2/5, parvovirus B19 in only 1/5, and one death versus four survivors, indicating substantial variable expressivity even within one sibship carrying the identical genotype. This variability is consistent with — and mechanistically explained by — the gene-by-environment (microbial exposure) interaction demonstrated in the mouse model.
- **Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).
- **Germline mosaicism:** Not reported/not applicable (biallelic inheritance from two heterozygous carrier parents, not mosaicism).
- **Founder effect:** Not established as a population founder variant; the variant was identified in one extended consanguineous family. Whether it represents an Omani/Arabian Peninsula founder allele versus a private familial variant is not determined from the sources retrieved.
- **Consanguinity role:** Central — consanguinity is the mechanism by which the rare recessive allele reached homozygosity in this family; this is explicitly the demographic context of the discovery.
- **Carrier frequency:** Not established/not found in population databases in this session.
- **Population demographics:** Only Omani (Arabian Peninsula, Middle Eastern) ancestry is documented. No data on other populations, geographic distribution, sex ratio (the paper does not appear to specify sex distribution among the 5 siblings in the material retrieved — verify from full text), or age distribution beyond the pediatric-onset pattern described above.

---

## 10. Diagnostics

**Laboratory tests (as performed in the index cohort):**
- Complete blood count with lymphocyte subset flow cytometry (CD4+, CD8+, B-cell, NK-cell enumeration)
- T-cell proliferation assays (response to PHA and anti-CD3 stimulation)
- Quantitative serum immunoglobulins (IgG, IgA, IgM)
- Specific antibody titers to tetanus, diphtheria, hepatitis B, and measles (pre/post-booster)
- In vitro B-cell functional assay: IgG secretion following anti-CD40 + IL-4 stimulation
- Viral load monitoring (CMV, EBV, parvovirus B19 PCR/viremia)
- Liver function tests (given universal hepatitis)

**Genetic testing:**
- Whole-exome sequencing (WES) was the diagnostic modality that identified the causal *COPG1* variant in this family — appropriate as first-tier testing in a suspected novel/undiagnosed CID, especially in a consanguineous pedigree where a homozygosity-mapping-informed WES approach is efficient.
- No commercial single-gene or panel test specific to *COPG1* CID was confirmed as available in this session (this is a very recently described, single-family gene-disease relationship; coverage on standard primary immunodeficiency gene panels should be checked directly against panel providers such as Invitae/GeneDx/Blueprint Genetics, and against Genomics England PanelApp, which does list *COPG1* on its "Primary immunodeficiency or monogenic inflammatory bowel disease" panel per the search result above — https://panelapp.genomicsengland.co.uk/panels/398/gene/COPG1/).
- Sanger sequencing was used to confirm the WES-identified variant and to test parental carrier status.

**Genetic testing utility (general/inferred):** For a CID presenting with the described phenotype, WES or WGS is likely to have higher diagnostic yield than a targeted panel given the extreme rarity/novelty of the gene-disease association; a comprehensive primary immunodeficiency gene panel that includes *COPG1* would also be reasonable.

**Clinical criteria:** No standardized diagnostic criteria (e.g., ESID/PAGID criteria for CID) specific to IMD128 exist; diagnosis rests on the combination of clinical phenotype plus molecular confirmation of biallelic pathogenic *COPG1* variants. Differential diagnosis should include other combined immunodeficiencies (SCID variants, other coatomer-subunit disorders such as COPB1 deficiency/Baralle–Macken syndrome, and other CIDs presenting with infantile recurrent infection, failure to thrive, and hepatitis) — distinguishing features from COPB1 deficiency include the presence of neurodevelopmental impairment and cataracts in the latter, which are not reported in IMD128.

**Screening:** No newborn screening protocol exists for this ultra-rare, recently described condition; it would not currently be detected by standard SCID newborn screening (TREC assay), since the reported patients had detectable (if reduced/declining) T-cell populations rather than a classic SCID-level absence of T cells — this is an inference based on the described lymphopenia pattern, not a directly stated TREC result.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** Of 5 reported patients, 1 (P4) died at age 3.5 years from respiratory failure and multiorgan dysfunction; the other 4 were alive at the time of publication (specific follow-up ages/duration not confirmed in the material retrieved in this session — verify from full text). This gives an observed case-fatality of 1/5 in the only reported cohort — far too small a sample for a formal survival-rate estimate, and this should be presented as raw case count, not extrapolated to a population rate.
- **Morbidity:** Chronic bronchiectasis (3/5) represents a significant, largely irreversible morbidity affecting long-term pulmonary function. Chronic viremia (CMV/EBV/parvovirus B19) represents ongoing infectious morbidity. Hepatitis (5/5) represents chronic hepatic morbidity of unspecified severity/etiology attribution (viral vs. direct ER-stress-related hepatocyte injury is not distinguished in the sources retrieved).
- **Complications:** Bronchiectasis, chronic viral infection/viremia, growth failure, and (in one case) fatal multiorgan dysfunction.
- **Quality of life:** Not formally measured (see Section 3).
- **Prognostic factors:** No formal prognostic model exists. Based on the mouse-model data, cumulative microbial/antigenic exposure burden is a plausible severity/prognostic modifier, and early recognition with reduced-exposure management (analogous to protective isolation in other CIDs) plus prompt antimicrobial and immunoglobulin support would be the biologically rational, though not yet clinically validated in humans, prognosis-modifying strategy.

---

## 12. Treatment

**Established human clinical management:** The primary source material retrieved does not specify the exact clinical management regimen used for the 5 index patients (e.g., whether IVIG replacement, prophylactic antimicrobials, or hematopoietic stem cell transplantation were used) — I could not confirm these details from the sources available in this session, and this should be verified directly from the JCI full text/supplement before curating specific `treatments:` entries with NCIT bindings. Given the phenotype (combined immunodeficiency with impaired antibody responses and recurrent bacterial/viral infection), **standard-of-care management for CID** would conventionally include:
- Immunoglobulin replacement therapy (IVIG/SCIG) — NCIT term candidate: generic Pharmacotherapy (NCIT:C15986) with `therapeutic_agent` bound to an immunoglobulin product, if directly documented in the source
- Antimicrobial prophylaxis
- Consideration of hematopoietic stem cell transplantation (HSCT) as the only potentially curative option for a genetically defined CID

**These are inferred, standard-of-care possibilities based on the disease category, not confirmed treatments documented for this specific cohort in the sources I retrieved — do not curate them into a KB entry as disease-specific evidence without independently sourcing the exact treatment history from the full JCI article or a follow-up case report.**

**Investigational/preclinical (mechanistically validated in the mouse model, not yet a clinical therapy):**
- **Tauroursodeoxycholic acid (TUDCA)** — an ER-stress-relieving chemical chaperone (a bile acid derivative). In the *Copg1^K652E* mouse model, TUDCA:
  - Normalized sXbp1 and Hspa5 mRNA expression to wild-type levels in mutant B cells in vitro
  - Restored IgG secretion in LPS+IL-4-stimulated mutant B cells in vitro
  - Corrected T-cell survival and IFN-γ secretion upon anti-CD3+anti-CD28 stimulation in vitro
  - Normalized IgG anti-TNP antibody responses to both T-independent and T-dependent antigens in vivo
  - Partially reversed cachexia, reversed T-cell lymphopenia, corrected defective T-cell proliferation, and decreased sXbp1 expression when administered during pet-store microbial exposure in vivo
  - Had no significant effect on wild-type control mice (supporting specificity of the rescue to the mutant genotype)
  (All: Bainter et al. 2021, PMID:33529166.)

  TUDCA is an FDA-approved-adjacent compound in other contexts (it is marketed/used off-label as a chemical chaperone in some settings), but **no human clinical trial of TUDCA specifically for IMD128/COPG1 deficiency was found** in this search — this represents a clear translational-research gap rather than an established therapy. Suggested NCIT candidate if curated as an experimental treatment: NCIT:C15986 (Pharmacotherapy) with `therapeutic_agent` bound to a CHEBI term for tauroursodeoxycholic acid (CHEBI ID not independently verified in this session).

**Treatment strategy note for KB curation:** Given the strength of the mechanistic rescue data, this disease is a strong candidate for a `mechanistic_hypotheses`/`discussions` entry (`kind: KNOWLEDGE_GAP` or a treatment-hypothesis framing) noting that TUDCA and other UPR-modulating agents represent a mechanistically grounded but clinically untested therapeutic avenue — this should be explicitly flagged as preclinical/model-organism evidence (`evidence_source: MODEL_ORGANISM` and `IN_VITRO` as appropriate, split by evidence item per the mixed-source rule) and not conflated with an approved human treatment.

---

## 13. Prevention

No primary, secondary, or tertiary prevention strategies specific to IMD128 were found. As an autosomal recessive monogenic disease identified in a consanguineous family, the only directly applicable prevention modalities are the general ones applicable to any newly characterized recessive disorder:
- **Genetic counseling** for the family and extended consanguineous kindred regarding recurrence risk (25% for each future pregnancy of carrier parents) — NCIT:C15240 (Genetic Counseling)
- **Carrier screening / prenatal or preimplantation genetic testing** could in principle be offered to the family once the causal variant is known, though no report of this being implemented was found
- **Cascade/family testing** of at-risk relatives given the consanguineous pedigree structure

No population-level newborn screening, vaccination strategy, or public-health intervention exists for this condition, consistent with its status as a single-family, recently discovered ultra-rare disease.

---

## 14. Other Species / Natural Disease

**Taxonomy:** No naturally occurring veterinary/animal disease caused by spontaneous *COPG1* mutation was identified in the search (no OMIA entry found in this session). NCBI Taxon: Homo sapiens (NCBITaxon:9606) is the only species with reported natural disease.

**Gene orthologs:** *Copg1* is highly conserved; mouse ortholog *Copg1* (used directly to generate the engineered model below). No comparative/orthology database identifiers were independently retrieved in this session (e.g., specific NCBI Gene ID for mouse *Copg1* was not confirmed here).

**Natural disease in other species:** None reported — this is not a known veterinary disease.

**Comparative biology:** The mouse model (below) represents an *engineered*, not naturally occurring, disease model, but demonstrates strong evolutionary conservation of the underlying γ1-COP/KDELR/UPR mechanism between mouse and human.

---

## 15. Model Organisms

**Genetic model:** CRISPR/Cas9-generated *Copg1^K652E* knock-in mouse, homozygous for the orthologous patient mutation, engineered specifically to recapitulate the human disease (Bainter et al. 2021, PMID:33529166). This is a precise, patient-variant-matched knock-in model (not a knockout), directly testing the pathogenicity and mechanism of the identified human allele.

**Phenotype recapitulation:**
- Under SPF (low pathogen exposure) conditions: normal lymphocyte development/numbers, normal T-cell proliferation, but hypogammaglobulinemia and defective antibody responses — a partial/subclinical recapitulation.
- Under naturalistic microbial exposure (pet-store mouse cohousing, 22 days): progressive weight loss (to ~70% baseline), T-cell lymphopenia (CD3+, CD4+, CD8+), severely impaired T-cell proliferation, hypergammaglobulinemia, and elevated pro-inflammatory cytokines (TNF-α, IFN-γ, IL-6) — a much closer recapitulation of the overt human clinical phenotype (though the human patients had hepatitis and bronchiectasis, which are not described as reproduced in the mouse model in the material retrieved).
- Mechanistically, the mouse model reproduced the key cellular findings from human patient cells: increased ER stress markers (sXbp1, Hspa5/BiP, CHOP) in activated T and B cells, and increased T-cell apoptosis upon activation.

**Model limitations:** The SPF-housed mouse alone substantially underrepresents disease severity relative to the human phenotype, which is itself the paper's key insight (motivating the environmentally "dirty" cohousing paradigm to unmask the phenotype) — i.e., standard SPF vivarium conditions are explicitly identified as a limitation for recapitulating this particular immunodeficiency. No mouse data on hepatitis, bronchiectasis, or mortality were reported in the material retrieved, so the pulmonary/hepatic end-organ damage seen in human patients is not clearly reproduced (or at least was not described in the summary I retrieved) — flag as an unconfirmed gap rather than asserting either a positive or negative finding without checking the full paper.

**Other model systems:**
- **Patient-derived skin fibroblasts** were used to demonstrate impaired retrograde COPI transport (increased colocalization of a VSVGts-KDELR fusion reporter with the Golgi marker GM130) — an in vitro human cellular model directly from affected individuals, valuable for confirming variant pathogenicity independent of the mouse system.
- No zebrafish, *Drosophila*, *C. elegans*, yeast, iPSC, or organoid models of *COPG1* deficiency were identified in the sources retrieved for this session.

**Research applications:** The mouse model is directly useful for studying (1) the UPR/ER-stress mechanism of lymphocyte-restricted immunodeficiency, (2) gene-by-environment interaction in primary immunodeficiency severity, and (3) preclinical testing of ER-stress-modulating therapeutics (TUDCA), as already demonstrated.

**Resources:** No specific repository/stock number (JAX, MMRRC, IMSR) for the *Copg1^K652E* mouse line was found in the search results retrieved in this session — this should be checked directly against IMSR/MGI before citing a specific resource identifier.

---

## Summary of Key Gaps and Verification Needs (for curator follow-up)

This report should be treated as a **lead**, per this repository's evidence-discipline rules — every CURIE, exact quote, and identifier above needs independent verification before being written into a KB YAML file:
1. OMIM full Clinical Synopsis text was not directly retrievable (403 error) — re-fetch from omim.org or via an authenticated/cached source before finalizing phenotype frequencies and any additional clinical detail.
2. gnomAD constraint metrics (pLI/LOEUF) for *COPG1*, and population allele frequency for the specific c.1954A>G variant, were not found/confirmed in this session.
3. ClinVar classification of the variant was not independently confirmed.
4. Exact human clinical management (IVIG, antimicrobial prophylaxis, HSCT) for the 5 index patients was not confirmed from the sources retrieved — do not assume standard CID management was actually used for this family without checking the JCI full text/methods.
5. Sex distribution and precise ages/follow-up duration of the 4 surviving siblings were not confirmed.
6. MONDO:0975834 mapping was taken from the task's own stub metadata and not independently cross-checked against a live MONDO release in this session.
7. Transcript reference (e.g., NM_ accession) for the c.1954A>G nomenclature was not independently confirmed.

**All quoted material above in quotation marks is copied directly, as reported by the fetched source, from the JCI article's text (via WebFetch summarization) or from search-engine-generated summaries of PubMed/JCI content — these are AI-mediated retrievals of the primary source, not my own reading of the original PDF, and should be re-verified against the original JCI article text (open access: https://www.jci.org/articles/view/140494) before being used as an exact-quote `snippet:` in KB evidence items**, per this repository's rule that a snippet must be an exact source substring verified at curation time, not a paraphrase relayed through an intermediate tool.

---

### Sources

- [Entry - #620983 - IMMUNODEFICIENCY 128; IMD128 - OMIM](https://omim.org/entry/620983)
- [Entry - *615525 - COATOMER PROTEIN COMPLEX, SUBUNIT GAMMA-1; COPG1 - OMIM](https://omim.org/entry/615525)
- [JCI - Combined immunodeficiency due to a mutation in the γ1 subunit of the coat protein I complex (Bainter et al., 2021, PMID:33529166)](https://www.jci.org/articles/view/140494)
- [Gene: COPG1 — Genomics England PanelApp (Primary immunodeficiency panel)](https://panelapp.genomicsengland.co.uk/panels/398/gene/COPG1/)
- [COPG1 curation results — ClinGen](https://search.clinicalgenome.org/kb/genes/HGNC:2236)
- [COPG1 Gene - GeneCards](https://genecards.org/cgi-bin/carddisp.pl?gene=COPG1)
- [Deficiency in coatomer complex I causes aberrant activation of STING signalling — Nature Communications, PMID:35484149](https://www.nature.com/articles/s41467-022-29946-6)
- [Genetics of COPA syndrome — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6372856/)
- [Expanding the clinical and immunological phenotypes of COPB1 deficiency, PMID:41676145](https://pubmed.ncbi.nlm.nih.gov/41676145/)
- [COATOMER PROTEIN COMPLEX, SUBUNIT ALPHA; COPA - OMIM](https://www.omim.org/entry/601924)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 4 |
| On topic | 4 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:33529166` *(abstract only)*: "a salt bridge between K652 and the carboxyl side chain of E757 and a hydrogen bond between K652 and the main chain carbonyl oxygen of D762"
  - Text part not found as substring: 'a salt bridge between K652 and the carboxyl side chain of E757 and a hydrogen bond between K652 and the main chain carbonyl oxygen of D762' (note: only abstract available for PMID:33529166, full text may contain this excerpt)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 17 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0032179` (1 mention) - the report calls it "verify exact CD8 lymphopenia term"; HP calls it **Abnormal circulating globulin concentration**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006890` (1 mention) - the report calls it "retrograde vesicle-mediated transport, Golgi to ER"; GO calls it **retrograde vesicle-mediated transport, Golgi to endoplasmic reticulum**, and lists "retrograde vesicle-mediated transport, Golgi to ER" among its other names