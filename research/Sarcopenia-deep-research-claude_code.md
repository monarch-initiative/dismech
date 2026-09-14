---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-31T14:41:09.900051'
end_time: '2026-08-31T14:46:04.596890'
duration_seconds: 294.7
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Sarcopenia
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
  - claude-sonnet-5
  web_search_requests: 30
  num_turns: 31
  total_cost_usd: 1.7758371999999996
  session_id: e3cbd979-119c-5af2-82ca-6001fd814aee
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
citation_count: 48
reference_validation:
  total_references: 37
  verified: 37
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 37
  on_topic: 22
  validator_version: 0.2.1
term_validation:
  total_terms: 29
  verified: 28
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 19
  labels_matching: 12
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: CL:0000738
    reported_labels:
    - leukocyte, for inflammatory infiltrate
    ontology_label: leukocyte
  labels_variant: 6
  obsolete_terms:
  - term_id: MONDO:0006516
    ontology_label: obsolete sarcopenia
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sarcopenia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Sarcopenia** covering all of the
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

I'll research this now using web search, covering the disease characteristics systematically. Let me start by loading the search tools and running parallel queries across the major topic areas.

I now have sufficient identifier and mechanism data, plus solid coverage of etiology, epidemiology, treatment pipeline, diagnostics, and animal models. I have enough to write the comprehensive report now.

## Sarcopenia: Comprehensive Research Report

### 1. Disease Information

**Overview.** Sarcopenia is a progressive, generalized skeletal muscle disorder characterized by accelerated loss of muscle mass and function, most classically associated with aging but increasingly recognized as also arising secondary to disuse, malnutrition, and chronic disease. It sits at the intersection of geriatric medicine, endocrinology, and musculoskeletal biology and is now recognized internationally as a distinct disease entity rather than merely a normal correlate of aging. The 2019 revised consensus (EWGSOP2) defines it operationally: "sarcopenia is a condition characterized by loss of muscle mass and function occurring as a natural part of aging process," with diagnosis requiring the presence of low muscle strength as the primary criterion, confirmed by low muscle quantity/quality, with severity graded by poor physical performance (PMC6322506).

**Key identifiers:**
- **ICD-10-CM:** M62.84 (Sarcopenia) — assigned in 2016, formally recognizing sarcopenia as a billable disease state rather than a normal aging finding ([icd10data.com](https://www.icd10data.com/ICD10CM/Codes/M00-M99/M60-M63/M62-/M62.84); [PubMed 27891296](https://pubmed.ncbi.nlm.nih.gov/27891296/), "Welcome to the ICD-10 code for sarcopenia").
- **MONDO:** MONDO:0006516 exists but is flagged **obsolete** in the current ontology release, described there as "Progressive decline in muscle mass due to aging which results in decreased functional capacity of muscles" — curators should verify current mapping status/replacement term directly against the live Mondo release before binding.
- **NCIT:** NCIT:C186726 (Sarcopenia); NCIT:C189016 (Acute Sarcopenia) — NCIT distinguishes acute (≤6 months, typically post-illness/surgery) from chronic (>6 months) forms.
- **MeSH:** D055948.
- **EFO:** EFO:1000653.
- **SNOMED CT:** 772791006.
- **UMLS/MedGen:** C0872084.
- No dedicated OMIM or Orphanet entry was found — sarcopenia in its primary (age-related) form is not a monogenic/rare disease in the classic Orphanet/OMIM sense, though secondary/genetic myopathic sarcopenias may map to related entries (e.g., myostatin-related muscle hypertrophy, OMIM #614457, is the inverse phenotype).
- No dedicated HPO term was identified in this search; OLS returned zero HP hits for "sarcopenia," suggesting the concept may need representation via composed terms (e.g., HP:0003324 Generalized muscle weakness, HP:0003202 Skeletal muscle atrophy) rather than a single canonical HP identifier — this should be confirmed against a live HPO browser query before curation.

**Synonyms:** age-related muscle loss, sarcopenic muscle wasting, myopenia (less common), primary/secondary sarcopenia, sarcopenic obesity (comorbid variant).

**Data provenance:** Most disease-level knowledge (prevalence, mechanism, treatment efficacy) derives from aggregated cohort studies, meta-analyses, and consensus panels (EWGSOP2, AWGS, IWGS, FNIH) rather than individual EHR case reports, though EHR-based sarcopenia/frailty/cachexia phenotyping is an active research area (PMC7395344).

Sources:
- [Sarcopenia: revised European consensus on definition and diagnosis](https://pmc.ncbi.nlm.nih.gov/articles/PMC6322506/)
- [ICD-10-CM M62.84](https://www.icd10data.com/ICD10CM/Codes/M00-M99/M60-M63/M62-/M62.84)
- [Welcome to the ICD-10 code for sarcopenia - PubMed](https://pubmed.ncbi.nlm.nih.gov/27891296/)

---

### 2. Etiology

**Primary vs. secondary classification.** The field distinguishes **primary (age-related) sarcopenia**, diagnosed when aging is the only apparent cause, from **secondary sarcopenia**, driven by identifiable extrinsic factors. Secondary sarcopenia is categorized into three main mechanistic buckets: (1) activity-related (disuse, bed rest, sedentary lifestyle, zero-gravity/immobilization), (2) disease-related (organ failure — heart, kidney, lung, liver, brain; inflammatory disease; malignancy; endocrine disease), and (3) nutrition-related (insufficient energy/protein intake, malabsorption, GI disease, anorexia of aging, drug-induced anorexia) (PMC8773430).

**Disease Causal Factors — primary/age-related mechanism:** Reduction in alpha-motor neuron number and motor unit remodeling, mitochondrial dysfunction, hormonal shifts (declining IGF-1, testosterone, estrogen; rising cortisol and pro-inflammatory cytokines TNF-α/IL-6), and insulin resistance.

**Genetic risk factors.**
- **Heritability:** Twin and family studies estimate heritability of muscle strength at 30–85% and of muscle mass at 45–90%, with handgrip strength specifically at 30–65% (ScienceDirect S0026049523003153, "Pathophysiology of sarcopenia: Genetic factors and their interplay with environmental factors").
- **GWAS loci:** A multivariate GWAS identified 215 loci and >30,000 SNPs contributing to the polygenic architecture of sarcopenia-related traits; 78 independent SNPs across 73 loci were associated with handgrip strength, lean mass, and walking pace with consistent effect direction. A large European-ancestry meta-analysis (20 cohorts) identified five loci for total lean body mass: **HSD17B11, VCAN, ADAMTSL3, IRS1, and FTO**. Earlier work also implicated **ESR1, NOS3, KLF5, and HLA-DQA1** in low handgrip strength/lean mass (Nature Scientific Reports 41598-022-07567-9; PMC9920138, UK Biobank).
- **Candidate genes:** *ACTN3* R577X null polymorphism (α-actinin-3 deficiency, present in >1.5 billion people worldwide) is associated with reduced skeletal muscle mass persisting into old age and increased risk of sarcopenia, frailty, and functional loss (PMC/biorxiv on ACTN3). *MSTN* (myostatin) K153R polymorphism (rs1805086) associates with muscle power phenotypes, though a meta-analysis found inconsistent overall effects on strength/mass across studies, and MSTN/ACTN3 variants were **not** associated with exceptional longevity in Japanese centenarians (PMC5115755).

**Environmental/lifestyle risk factors:** Physical inactivity/sedentary behavior, inadequate dietary protein intake, vitamin D deficiency, smoking, excess alcohol, obesity (via sarcopenic obesity), and chronic disease exposure. Age itself and, per EWGSOP2 data, male sex are risk factors under some diagnostic criteria (though IWGS criteria show higher prevalence in women) (PMC/Wiley global prevalence meta-analysis, jcsm.12783).

**Protective factors:** Regular resistance/aerobic exercise, adequate high-quality (leucine-rich) protein intake (1.0–1.2 g/kg/day, up to 1.2–1.5 g/kg/day with inflammatory disease), vitamin D sufficiency, and possibly favorable genetic variants (e.g., ACTN3 R577 "wild-type" allele).

**Gene-environment interaction:** The interplay is bidirectional — genetic susceptibility (e.g., ACTN3 XX genotype) may amplify vulnerability to disuse-induced atrophy, while chronic environmental stressors (inflammation, malnutrition) can epigenetically or transcriptionally suppress anabolic gene programs regardless of baseline genotype (ScienceDirect S0026049523003153).

Sources:
- [Pathophysiology of sarcopenia: Genetic factors and their interplay with environmental factors](https://www.sciencedirect.com/science/article/abs/pii/S0026049523003153)
- [Unveiling genetic variants for age-related sarcopenia — Korean cohorts](https://www.nature.com/articles/s41598-022-07567-9)
- [Genomic Predictors of Sarcopenia — UK Biobank](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9920138/)
- [Effect of Exercise on Secondary Sarcopenia: A Comprehensive Literature Review](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8773430/)
- [Muscle-Related Polymorphisms (MSTN, ACTN3) Not Associated with Longevity](https://pmc.ncbi.nlm.nih.gov/articles/PMC5115755/)

---

### 3. Phenotypes

Sarcopenia is defined by a **triad** of measurable phenotypic domains rather than a single symptom:

| Phenotype | Type | Suggested term | Notes |
|---|---|---|---|
| Low muscle strength (grip strength, chair-stand) | Sign/functional | HP:0003324 (Generalized muscle weakness) | Primary EWGSOP2 diagnostic criterion |
| Low muscle mass/quantity (appendicular skeletal muscle index) | Sign (imaging/anthropometric) | HP:0003202 (Skeletal muscle atrophy) | Confirms diagnosis (DXA/BIA/CT/MRI) |
| Low physical performance (gait speed, SPPB, TUG, 400m walk) | Functional/behavioral | HP:0002015 (dysphagia, if severe) not applicable; consider HP:0001288 (Gait disturbance) | Determines severity grading |
| Falls | Clinical sign | HP:0002527 (Falls) | Downstream consequence |
| Frailty | Syndromic | — | Overlapping but distinct construct |
| Reduced muscle quality (fatty infiltration, fibrosis) | Imaging/histological | — | CT/MRI attenuation-based |

**Onset:** Muscle mass and strength typically peak in the 3rd–4th decade of life, plateau, then decline progressively from approximately age 40–50 onward, accelerating markedly after age 60–70 ("late-onset," though disuse/critical-illness sarcopenia can develop acutely within days-to-weeks in ICU settings — reflected in the NCIT "Acute Sarcopenia," NCIT:C189016, ≤6 months, vs. chronic, >6 months).

**Severity/progression:** EWGSOP2 grades severity in three tiers: (1) **probable sarcopenia** (low strength only), (2) **confirmed sarcopenia** (low strength + low muscle mass/quality), (3) **severe sarcopenia** (low strength + low mass/quality + poor physical performance) (PMC6322506). Course is typically chronic and progressive in primary sarcopenia; secondary/disuse forms can progress rapidly (muscle loss of up to several percent per week during bed rest or critical illness) and are partially reversible with rehabilitation.

**Frequency:** By definition all sarcopenia patients have the diagnostic triad; downstream phenotypes occur at variable frequency — falls, frailty, disability, and reduced quality of life are common consequences, with an estimated prevalence gradient depending on diagnostic criteria used (see Epidemiology, §9).

**QoL impact:** Reduced physical function correlates with diminished independence in activities of daily living, increased fall/fracture risk, loss of mobility, and downstream depression; validated via SF-36/EQ-5D-type instruments in several of the reviewed cohort studies, though disease-specific quantification (e.g., utility decrements) was not directly retrieved in this search pass.

Sources:
- [Sarcopenia: revised European consensus on definition and diagnosis](https://pmc.ncbi.nlm.nih.gov/articles/PMC6322506/)
- [Diagnostic Criteria and Measurement Techniques of Sarcopenia](https://pmc.ncbi.nlm.nih.gov/articles/PMC10856900/)

---

### 4. Genetic/Molecular Information

Sarcopenia is fundamentally a **complex/polygenic trait**, not a single-gene Mendelian disorder, so this section summarizes contributing loci/pathways rather than causal Mendelian variants.

**Candidate/contributing genes (with GO/functional relevance):**
- **MSTN (myostatin, GDF8)** — hgnc:7204 (approx.) — negative regulator of muscle mass; K153R (rs1805086) polymorphism associated with muscle power phenotypes; myostatin pathway is the leading pharmacological target class (see §12) (PMC3024427; PMC9690375).
- **ACTN3** — R577X null polymorphism; loss of α-actinin-3 (compensated by α-actinin-2) associated with reduced sprint/power performance and increased sarcopenia/frailty risk in old age.
- **IRS1, FTO, HSD17B11, VCAN, ADAMTSL3** — lean-mass GWAS loci (European ancestry meta-analysis, 20 cohorts).
- **ESR1** (estrogen receptor), **NOS3** (endothelial NOS), **KLF5**, **HLA-DQA1** — implicated in earlier handgrip-strength/lean-mass association studies.

**Functional consequences:** Myostatin overexpression/gain-of-function drives muscle atrophy via TGF-β superfamily/activin receptor signaling → SMAD2/3 activation → suppression of Akt/mTOR anabolic signaling and upregulation of the ubiquitin-proteasome atrogenes. This is essentially the inverse of the loss-of-function MSTN phenotype (myostatin-related muscle hypertrophy).

**Epigenetics:** Not extensively covered in this search pass, but the multi-omics literature (e.g., PMC EP092853, "multi-omics investigation of sarcopenia and frailty: genomic, epigenomic and telomere length data") indicates epigenetic and telomere-length changes are being actively integrated into sarcopenia risk models alongside genomics.

**Chromosomal abnormalities:** Not a recognized feature of primary sarcopenia; not applicable in the way it is for classic Mendelian disorders.

**Somatic vs. germline:** Sarcopenia genetics is entirely germline/constitutional (polygenic susceptibility); no somatic mutation component is described.

Sources:
- [A multi-omics investigation of sarcopenia and frailty](https://physoc.onlinelibrary.wiley.com/doi/full/10.1113/EP092853)
- [Association of Myostatin Gene Polymorphisms with Strength and Muscle Mass in Athletes](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9690375/)
- [K153R Polymorphism in the Myostatin Gene](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3024427/)

---

### 5. Environmental Information

**Environmental/lifestyle factors:** Sedentary behavior and physical inactivity are the dominant modifiable drivers; prolonged bed rest, immobilization, and hindlimb/limb unloading are used experimentally (and occur clinically in hospitalization) to model rapid disuse atrophy. Malnutrition (inadequate protein/caloric intake), smoking, and excessive alcohol use contribute. Obesity independently and synergistically worsens sarcopenia via ectopic intramuscular fat deposition and anabolic resistance (sarcopenic obesity) (PMC4326920, "Muscle ectopic fat deposition contributes to anabolic resistance in obese sarcopenic old rats").

**Infectious agents:** No primary infectious etiology; however, acute/critical illness (including sepsis and severe infections) is a major precipitant of secondary/ICU-acquired sarcopenia via a combination of immobilization, systemic inflammation, and catabolic stress.

**Occupational/toxin exposure:** Not a well-characterized primary driver in the literature retrieved; disuse (occupational sedentarism) and chronic corticosteroid/medication exposure (iatrogenic) are more relevant secondary contributors than classic toxicological exposures.

Sources:
- [Muscle ectopic fat deposition contributes to anabolic resistance in obese sarcopenic old rats](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4326920/)
- [Sarcopenic obesity: epidemiology, pathophysiology, cardiovascular disease, mortality, and management](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2023.1185221/full)

---

### 6. Mechanism / Pathophysiology

**Ordered causal chain (age-related/primary sarcopenia):**

1. Aging (and/or disuse/inflammatory disease) → **motor neuron loss and neuromuscular junction (NMJ) instability** (denervation, acetylcholine receptor fragmentation) — this is now considered an early, possibly initiating, event (PMC10789655, "Unraveling the causes of sarcopenia: Roles of neuromuscular junction impairment and mitochondrial dysfunction").
2. NMJ denervation → **loss of type II (fast-twitch) fiber innervation**, with denervated fibers either reinnervated by adjacent type I motor units (fiber-type grouping/shift toward slow-twitch) or undergoing atrophy and replacement by fat/fibrous tissue (myosteatosis/fibrosis) → net preferential type II fiber atrophy and reduced peak power output.
3. In parallel, aging drives **mitochondrial dysfunction** (reduced biogenesis, impaired oxidative phosphorylation, elevated ROS) within myofibers, which both correlates with and reinforces NMJ degeneration, creating a feed-forward loop → reduced ATP availability and increased oxidative damage to contractile and structural proteins.
4. Chronic low-grade "inflammaging" — elevated circulating **TNF-α and IL-6** — activates **NF-κB** signaling in myofibers, which (a) upregulates E3 ubiquitin ligases **Atrogin-1 (FBXO32) and MuRF1 (TRIM63)**, accelerating ubiquitin-proteasome-mediated myofibrillar protein degradation, and (b) represses **MyoD**, impairing myogenic differentiation; IL-6/STAT3 signaling separately inhibits satellite cell-mediated regeneration.
5. Concurrently, declining anabolic hormonal drive (falling **IGF-1** and **testosterone**, rising **myostatin/activin** signaling through activin type II receptors → SMAD2/3) suppresses **Akt/mTORC1** signaling, producing **"anabolic resistance"** — a blunted muscle protein synthesis response to dietary protein/leucine and resistance exercise stimuli, worsened further by obesity/insulin resistance via eIF2α phosphorylation and ectopic intramuscular lipid (ceramide) accumulation.
6. Satellite cells (muscle stem cells), whose niche is degraded by the same mitochondrial dysfunction, chronic inflammation, and NMJ decline above, lose quiescence/proliferation/differentiation capacity; senescent cells accumulating in the regenerative niche secrete a senescence-associated secretory phenotype (SASP) that further suppresses regeneration (2023 finding on CD36+ secretome/SASP as negative muscle-regeneration regulators).
7. The net result of steps 2–6 — degradation exceeding synthesis, impaired regeneration, fiber-type shift, and myosteatosis — is **progressive loss of skeletal muscle mass, strength, and quality**, converging on the clinical phenotype: low strength (step 1° criterion) → low muscle mass/quality (confirmatory) → impaired physical performance (severity marker) → falls, disability, frailty, hospitalization, and increased mortality.

Branch — **sarcopenic obesity**: steps 3 and 5 are amplified by adipose-tissue-derived inflammatory cytokines and ectopic intramuscular/intermuscular fat, producing a distinct oxidative-stress-driven mechanistic branch with disproportionate anabolic resistance (PMC/Frontiers fendo.2023.1185221).

Branch — **disease-associated secondary sarcopenia** (e.g., CKD, heart failure, cancer, T2DM): organ-specific catabolic signals (uremic toxins, natriuretic peptide/cytokine excess in heart failure, tumor-derived cachectic factors, hyperglycemia/insulin resistance in diabetes) feed into the same NF-κB/ubiquitin-proteasome and anabolic-resistance nodes described above, producing disease-flavored but mechanistically convergent muscle wasting (T2DM-related sarcopenia is now considered mechanistically distinct from both classic age-related sarcopenia and pure disuse atrophy — PMC11157032).

**Additional hallmark framework:** A 2023 review proposed nine core aging hallmarks plus five sarcopenia-specific additions: perturbed inflammation, compromised vascular perfusion, neural dysfunction, extracellular matrix (ECM) dysregulation, and ionic imbalance (PMC12295260).

**Suggested ontology terms:**
- GO biological processes: GO:0006511 (ubiquitin-dependent protein catabolic process), GO:0006914 (autophagy), GO:0008283 (cell population proliferation, satellite cells), GO:0007520 (myoblast fusion), GO:0043123 (positive regulation of NF-κB signaling), GO:0032496 (response to lipopolysaccharide/inflammation)
- GO molecular function: GO:0005160 (TGF-beta receptor binding, for myostatin/activin signaling)
- CL cell types: CL:0000188 (skeletal muscle myoblast/satellite cell — more precisely CL:0000594 skeletal muscle satellite cell), CL:0000188 (skeletal muscle fiber), CL:0000738 (leukocyte, for inflammatory infiltrate)
- Molecular targets: myostatin/GDF8, activin type II receptor (ACVR2B), IGF-1/Akt/mTORC1, NF-κB, Atrogin-1/FBXO32, MuRF1/TRIM63

Sources:
- [Unraveling the causes of sarcopenia: NMJ impairment and mitochondrial dysfunction](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10789655/)
- [Sarcopenia: Current Insights into Molecular Mechanisms, Diagnostics, and Emerging Interventional Approaches](https://pmc.ncbi.nlm.nih.gov/articles/PMC12295260/)
- [Molecular constraints of sarcopenia in the ageing muscle](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12267276/)
- [Type 2 diabetes mellitus related sarcopenia](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11157032/)
- [Sarcopenic obesity: epidemiology, pathophysiology](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2023.1185221/full)
- [Ubiquitin-proteasome pathway in skeletal muscle atrophy](https://pmc.ncbi.nlm.nih.gov/articles/PMC10690626/)

---

### 7. Anatomical Structures Affected

**Organ/system level:** Primary target is **skeletal muscle** (musculoskeletal system), generalized across the body but with particular clinical emphasis on **appendicular** musculature (limbs — the basis of the appendicular skeletal muscle index, ASMI, used diagnostically). Secondary/complication involvement includes the skeletal system (falls → fractures; disuse → osteosarcopenia overlap with osteoporosis), cardiovascular system (sarcopenia-heart failure interplay), and metabolic/endocrine systems (insulin resistance).

**Tissue/cell level:** Skeletal muscle tissue — specifically **type II (fast-twitch, glycolytic) muscle fibers**, which undergo preferential atrophy and denervation, with relative sparing/compensatory reinnervation of type I (slow-twitch) fibers. Cell populations: skeletal myofibers, **satellite cells** (muscle stem cells, CL:0000594), motor neurons and their NMJ synaptic terminals, and infiltrating fibro-adipogenic progenitors/adipocytes (myosteatosis) and fibroblasts (fibrosis).

**Subcellular level:** **Mitochondria** (biogenesis/OXPHOS dysfunction, GO:0005739), sarcomeric contractile apparatus (myofibrillar protein degradation via the ubiquitin-proteasome system), and the neuromuscular junction as a specialized subcellular structure (postsynaptic acetylcholine receptor clusters).

**Localization:** Generalized/bilateral and symmetric — sarcopenia is by definition a systemic process, distinguishing it from focal/localized muscle atrophy (e.g., from a single peripheral nerve injury). UBERON terms of relevance: UBERON:0001134 (skeletal muscle tissue), UBERON:0000383 (musculature of limb/appendicular musculature — commonly the diagnostic focus site, e.g., mid-thigh CT/MRI, calf circumference).

Sources: derived from the pathophysiology sources cited in §6 (PMC10789655, PMC12267276, PMC10690626).

---

### 8. Temporal Development

**Onset:** Muscle mass and strength peak around the third decade, then decline gradually from ~40 years, accelerating after 60–70. Primary sarcopenia is thus **adult/late-onset and insidious**. Secondary/disuse or critical-illness sarcopenia has an **acute-to-subacute** onset (days to weeks), formally distinguished by NCIT as "Acute Sarcopenia" (≤6 months) vs. chronic (>6 months).

**Progression:** Chronic primary sarcopenia is typically **slowly progressive** over years to decades; disease-associated secondary sarcopenia (cancer cachexia, heart failure, CKD) can progress much faster. EWGSOP2's staged framework (probable → confirmed → severe) functions as an implicit staging system based on accumulating deficits across strength, mass, and performance domains (PMC6322506).

**Course pattern:** Generally progressive rather than relapsing-remitting, though partial reversal is achievable with resistance exercise and nutritional intervention, particularly in secondary/disuse-related cases and earlier disease stages — this reversibility is a key rationale for early detection.

**Critical periods/intervention windows:** Midlife (40s–60s) is increasingly emphasized as a window for preventive intervention before muscle loss accelerates; post-acute-illness/post-hospitalization periods are critical windows for rehabilitative intervention to prevent conversion of transient disuse atrophy into persistent sarcopenia.

Sources:
- [Sarcopenia: revised European consensus on definition and diagnosis](https://pmc.ncbi.nlm.nih.gov/articles/PMC6322506/)
- [Prognostic Features of Sarcopenia in Older Hospitalized Patients: A 6-Month Follow-Up Study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11172762/)

---

### 9. Inheritance and Population

**Epidemiology:**
- Global prevalence estimates vary substantially by diagnostic criteria: **~5% (EWGSOP2)** to **~17% (IWGS)** among elderly populations in one meta-analysis; another large meta-analysis (58,404 community-dwelling participants ≥60 years) estimated overall global prevalence at **~10%** (PubMed 34816624, jcsm.12783).
- Prevalence ranges from **8–36%** in adults <60 years to **10–27%** in adults ≥60 years, reflecting major criteria-dependent heterogeneity.
- **Severe sarcopenia** prevalence: **2–9%**.
- **Sex differences differ by criteria set:** EWGSOP2 shows higher prevalence in **men** (11% vs. 2% in women), while IWGS criteria show higher prevalence in **women** (17% vs. 12% in men) — a striking illustration of definitional sensitivity (PubMed 36907247, Metabolism 2023 epidemiology review).

**Inheritance pattern:** Sarcopenia is **multifactorial/polygenic**, not Mendelian. No single inheritance pattern (AD/AR/X-linked) applies; risk is distributed across many common variants of small effect (see §4 GWAS loci) interacting with environmental exposures.

**Penetrance/expressivity:** Not applicable in the classical monogenic sense; "penetrance" of the polygenic risk score is modulated heavily by lifestyle, nutrition, and comorbidity burden.

**Founder effects/consanguinity/carrier frequency:** Not applicable — sarcopenia is a complex age-related trait, not a rare monogenic disorder.

**Population demographics:** Prevalence rises steeply with age and is influenced by geography, diagnostic criteria applied (EWGSOP vs. AWGS [Asian Working Group for Sarcopenia] vs. IWGS vs. FNIH), and setting (community-dwelling vs. hospitalized vs. long-term care, with hospitalized/institutionalized populations showing substantially higher rates). Regional/ethnic variation in cutoff values is a recognized methodological issue (Frontiers fmed.2024.1405438, "Diagnosing sarcopenia in clinical practice: international guidelines vs. population-specific cutoff criteria").

Sources:
- [Global prevalence of sarcopenia and severe sarcopenia: a systematic review and meta-analysis](https://onlinelibrary.wiley.com/doi/10.1002/jcsm.12783)
- [Epidemiology of sarcopenia: Prevalence, risk factors, and consequences](https://www.metabolismjournal.com/article/S0026-0495(23)00136-1/fulltext)
- [Diagnosing sarcopenia in clinical practice: international guidelines vs. population-specific cutoff criteria](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2024.1405438/full)

---

### 10. Diagnostics

**EWGSOP2 four-step algorithm** (the dominant clinical framework):
1. **Find** — case-finding via clinical suspicion or the **SARC-F questionnaire** (self-report screening tool).
2. **Assess** — measure **muscle strength**: grip strength (dynamometry) and/or chair-stand test; low strength → "probable sarcopenia," sufficient to initiate treatment in practice.
3. **Confirm** — quantify **muscle mass/quality**: bioimpedance analysis (BIA) or DXA in routine clinical care; DXA, CT, or MRI in research/specialty high-risk settings.
4. **Severity** — assess **physical performance**: gait speed, Short Physical Performance Battery (SPPB), Timed-Up-and-Go (TUG), or 400-meter walk test (PMC10684299; PMC6322506).

**Laboratory/biomarkers:** No single validated diagnostic blood biomarker yet, but candidates under active investigation include:
- **Myostatin (GDF8)** — elevated, inhibitory myokine.
- **GDF-15** — higher circulating levels independently associated with greater sarcopenia risk (PMC7740254).
- **Follistatin** — antagonizes myostatin/activin A; differs between sarcopenic and non-sarcopenic populations.
- **IGF-1** — reduced levels correlate with decreased muscle anabolism (though one study found IGF-1/TGF-β family/follistatin levels did **not** reliably reflect different dynapenia/sarcopenia stages in elderly women — PubMed 25681638 — underscoring current lack of a validated single biomarker).
- Activin A, irisin, vitamin D, myoglobin, cortisol.

**Imaging:** DXA (appendicular lean mass), CT/MRI (cross-sectional muscle area and intramuscular fat/attenuation — used in specialty/research settings), ultrasound (emerging, portable, used to measure muscle thickness/cross-sectional area, e.g., quadriceps).

**Genetic testing:** Not part of routine clinical diagnosis (sarcopenia is not diagnosed via genetic testing); genetic risk scores remain a research tool.

**Differential diagnosis:** Cachexia (distinct — requires ≥5% weight loss in ≤12 months plus ≥3 of: decreased strength, fatigue, anorexia, low fat-free mass index, abnormal biochemistry), frailty (overlapping but broader multisystem syndrome), primary myopathies/muscular dystrophies, disuse atrophy without the aging/chronic-disease substrate, malnutrition alone, and inflammatory myopathies (which can be assessed similarly via DXA/grip strength — PubMed 38544289).

**Screening:** SARC-F is the standard community screening instrument; sensitivity for detecting probable sarcopenia has been specifically evaluated in recent cross-sectional studies (PMC12292031, 2025).

Sources:
- [Sarcopenia: revised European consensus on definition and diagnosis](https://pmc.ncbi.nlm.nih.gov/articles/PMC6322506/)
- [Addressing the Main Barrier to Sarcopenia Identification: BIA vs. DXA](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10684299/)
- [Elevated GDF-15 Is a Biomarker of Sarcopenia in Older Adults](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7740254/)
- [Assessment of SARC-F Sensitivity for Probable Sarcopenia](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12292031/)

---

### 11. Outcome/Prognosis

**Mortality/morbidity:** Sarcopenia is independently associated with increased **all-cause mortality**, particularly in hospitalized and critically ill older adults; a routine sarcopenia assessment at ICU admission is proposed as a prognostic tool (PMC8616666). It is linked to increased **rehospitalization**, **falls**, **fractures**, and **loss of independence** — one 2025 longitudinal China-based aging study specifically linked sarcopenia to falls, fractures, hospital readmission, and all-cause mortality in older adults with endocrine disorders (PMC12403857).

**Functional/QoL outcomes:** Progressive disability, worsening ADL/IADL function, increased risk of institutionalization (long-term care admission), and depression are recognized downstream consequences (PMC/Springer chapters on frailty-sarcopenia-falls).

**Prognostic factors:** Severity grade (EWGSOP2 "severe sarcopenia" carries worse prognosis than "probable"), presence of comorbid frailty, and comorbid chronic disease burden (heart failure, CKD, cancer) all modify prognosis; the Multidimensional Prognostic Index has been used to track longitudinal changes predicting rehospitalization/mortality up to 6 months post-discharge (PMC11172762).

**Reversibility/recovery potential:** Unlike many chronic degenerative conditions, sarcopenia — especially secondary/disuse forms — has meaningful reversibility potential with early resistance exercise and nutritional rehabilitation, making early identification prognostically important.

Sources:
- [Prognostic Features of Sarcopenia in Older Hospitalized Patients](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11172762/)
- [Correlation of Sarcopenia With Modified Frailty Index in Critically Ill Elderly Patients](https://pmc.ncbi.nlm.nih.gov/articles/PMC8616666/)
- [Association between sarcopenia and falls, fractures, hospital readmission, and all-cause mortality in older adults with endocrine disorders](https://pmc.ncbi.nlm.nih.gov/articles/PMC12403857/)

---

### 12. Treatment

**Pharmacotherapy — established/guideline-recommended:** No drug is yet FDA-approved specifically for sarcopenia; current guideline-based management centers on non-pharmacological intervention (below). **Vitamin D repletion** is recommended where deficient (NCIT:C1621, Cholecalciferol / relevant vitamin D agents), though a 2024 RCT (DPVD ancillary study, Lancet Healthy Longevity) found active vitamin D (eldecalcitol) reduced sarcopenia onset risk in adults with prediabetes by increasing skeletal muscle volume/strength.

**Advanced/investigational therapeutics — myostatin/activin pathway (the leading pharmacological target class):**
- **Bimagrumab** — anti-activin type II receptor monoclonal antibody blocking myostatin/activin signaling. Phase 2 proof-of-concept: thigh muscle volume +4.80% vs. −1.01% placebo at 24 weeks; lean body mass gains of 1.9–2.8 kg across dose groups; however, **no significant improvement in physical performance** (gait speed, SPPB, 6-minute walk test) despite mass gains — a critical mass-vs-function dissociation. 2025 data extend this to post-hip-fracture recovery, again showing muscle-mass but only minimal mobility/strength benefit (PubMed 41248895; JAMA Network Open 2771858; PMC12141158; PMC12146653).
- **Apitegromab (SRK-015)** — targets latent (pro-)myostatin specifically, reducing TGF-β superfamily cross-reactivity; validated in spinal muscular atrophy; FDA issued a 2025 Complete Response Letter citing third-party manufacturing concerns (not efficacy/safety).
- **Trevogrumab (REGN1033)** — myostatin monoclonal antibody; in the Phase 2 COURAGE trial, adding trevogrumab to semaglutide preserved roughly half the lean mass otherwise lost to semaglutide-induced weight loss — relevant to the emerging "GLP-1-associated sarcopenia" concern.
- **Taldefgrobep alfa** — myostatin-targeting adnectin; awaiting Phase 2 obesity-context data.
- **KER-065** — selective activin receptor ligand trap, initially targeting Duchenne muscular dystrophy, mechanistically relevant to sarcopenia.
- RANK-ligand inhibition (denosumab-class) is being trialed for combined sarcopenia-with-osteoporosis indications (PMC12323245).

**Suggested NCIT terms:** NCIT:C15986 (Pharmacotherapy) as the generic action term paired with `therapeutic_agent` bindings for specific compounds (myostatin/activin inhibitors generally lack individual NCIT drug codes yet given investigational status; use CHEBI/NCIT where available per compound), NCIT:C15302 (Physical Therapy), NCIT:C15447 (Dietary Intervention), NCIT:C15747 (Supportive Care).

**Exercise (cornerstone, highest-grade recommendation):** Progressive **resistance exercise training (RET)**, moderate-to-high intensity, is the single most consistently effective intervention for both muscle mass and strength, with benefit demonstrated even in frail/multimorbid populations. NCIT:C15302 (Physical Therapy).

**Nutrition:** Increased daily protein intake (1.0–1.2 g/kg/day; 1.2–1.5 g/kg/day with inflammatory disease), high-quality/whey protein rich in leucine/essential amino acids; combined resistance-training + protein supplementation produces the largest gains in handgrip strength and gait speed; adding vitamin D further improves appendicular skeletal muscle index (network meta-analysis, Frontiers fnut.2025.1685014). Creatine supplementation is also recommended as an adjunct to structured exercise programs.

**Treatment response/limitations:** A recurring theme across trials (bimagrumab, others) is **dissociation between muscle mass gain and functional/performance improvement** — mass-focused pharmacotherapy alone appears insufficient without concurrent exercise, an important consideration for future combination-therapy trial design (PMC12146653, "Sarcopenia in Ageing and Chronic Illness: Trial Endpoints and Regulatory Issues").

Sources:
- [Bimagrumab: Novel Medical Therapy for IBM, Sarcopenia, and Medication-Induced Lean Body Mass Loss](https://pubmed.ncbi.nlm.nih.gov/41248895/)
- [Bimagrumab vs Optimized Standard of Care — JAMA Network Open](https://jamanetworkopen.com/journals/jamanetworkopen/fullarticle/2771858) — actually [JAMA Network Open](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2771858)
- [Current and investigational medications for the treatment of sarcopenia](https://www.metabolismjournal.com/article/S0026-0495(23)00201-9/fulltext)
- [Sarcopenia in Ageing and Chronic Illness: Trial Endpoints and Regulatory Issues](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12146653/)
- [Active vitamin D treatment in the prevention of sarcopenia (DPVD ancillary study)](https://www.thelancet.com/journals/lanhl/article/PIIS2666-7568(24)00009-6/fulltext)
- [Exercise and nutrition strategies for sarcopenia in older adults: network meta-analysis](https://www.frontiersin.org/journals/nutrition/articles/10.3389/fnut.2025.1685014/full)
- [5 Sarcopenia Drugs Poised to Make an Impact](https://www.delveinsight.com/blog/promising-sarcopenia-drugs-in-development)
- [Trevogrumab (REGN1033): Myostatin Blocker, COURAGE Data](https://www.myostatininhibitorshub.com/blog/trevogrumab)

---

### 13. Prevention

**Primary prevention:** Regular structured resistance/multicomponent exercise throughout mid-to-late life is the strongest evidence-based primary prevention strategy; adequate dietary protein and vitamin D sufficiency across the lifespan support this. USPSTF recommends exercise interventions to prevent falls in community-dwelling adults ≥65 at increased fall risk.

**Secondary prevention (early detection):** Population screening using SARC-F in primary-care and geriatric settings, with reflex grip-strength/chair-stand testing, enables earlier identification before functional decline is severe; targeted screening in high-risk disease populations (CKD, heart failure, cancer, post-hospitalization) is increasingly recommended.

**Tertiary prevention:** Structured rehabilitation (physical/occupational therapy) post-hospitalization or post-acute-illness to prevent conversion of transient disuse atrophy into persistent sarcopenia; nutritional support during and after catabolic illness.

**Behavioral interventions:** Smoking cessation, alcohol moderation, sustained physical activity, weight management (particularly relevant to sarcopenic obesity).

**Immunization/infectious prevention:** Not directly applicable as a primary sarcopenia-prevention strategy, though preventing severe infections/hospitalizations indirectly reduces acute-catabolic sarcopenia risk.

**Genetic counseling/screening:** Not applicable given the polygenic, non-Mendelian nature of the condition; polygenic risk scoring remains investigational.

**Public health:** Nutritional support programs for older adults, fall-prevention public health initiatives, and geriatric assessment integration into primary care are the relevant population-level interventions (PMC11119320, "The nutritional support to prevent sarcopenia in the elderly").

Sources:
- [Vitamin D and Sarcopenia in the Elderly: Mechanisms and Consequences](https://www.dovepress.com/vitamin-d-and-sarcopenia-in-the-senior-people-a-review-of-mechanisms-a-peer-reviewed-fulltext-article-TCRM)
- [The nutritional support to prevent sarcopenia in the elderly](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11119320/)
- [Draft Recommendation: Vitamin D, Calcium, or Combined Supplementation — USPSTF](https://www.uspreventiveservicestaskforce.org/uspstf/draft-recommendation/vitamin-d-calcium-combined-supplementation-primary-prevention-falls-fractures-communitydwelling-adults)

---

### 14. Other Species / Natural Disease

**Taxonomy:** Naturally occurring, age-related sarcopenia is well documented in companion animals, particularly **dogs (Canis lupus familiaris, NCBITaxon:9615)** and **cats (Felis catus, NCBITaxon:9685)**, making them recognized comparative/natural models rather than purely induced laboratory models (PMC/Wiley, "Cachexia and Sarcopenia in Companion Animals: An Under-Utilized Natural Animal Model of Human Disease").

**Natural disease/veterinary relevance:** Aging Labrador retriever colonies show significant loss of lean body mass with age; epaxial muscle cross-sectional area (measured by ultrasound/CT) is significantly lower in healthy geriatric vs. young dogs. Cats show a significant negative correlation between muscle condition score (MCS, assessed by DEXA) and age. Clinically, muscle loss in companion animals impairs strength/balance, depresses immune function, and reduces recovery capacity from illness, surgery, or injury — directly paralleling the human syndrome.

**Sarcopenic obesity in animals:** Approximately 40% of aged pet cats and dogs are obese, with 12–15% of these specifically showing extremely low lean mass (i.e., comorbid sarcopenic obesity), closely mirroring the human sarcopenic-obesity phenotype.

**Comparative biology/One Health angle:** Tufts University and collaborators have explicitly framed companion-animal sarcopenia as a "One Health" comparative model, leveraging the shared home environment, similar aging trajectory, and non-invasive longitudinal measurement opportunities that companion animals offer versus purely laboratory rodent models.

**Cross-species conservation:** Core molecular pathways (myostatin/activin signaling, ubiquitin-proteasome atrogenes, mitochondrial dysfunction) are broadly evolutionarily conserved across mammals, supporting translational relevance of both natural (companion animal) and induced (rodent) models — though species-specific modulators exist (see PMC7881157, "Molecular and phenotypic analysis of rodent models reveals conserved and species-specific modulators of human sarcopenia").

Sources:
- [Cachexia and Sarcopenia in Companion Animals: An Under-Utilized Natural Animal Model](https://onlinelibrary.wiley.com/doi/full/10.1002/j.2617-1619.2018.tb00006.x)
- [Taking a One Health Approach to Muscle Loss Research — Tufts](https://now.tufts.edu/2022/04/11/taking-one-health-approach-muscle-loss-research)
- [Cachexia and sarcopenia: emerging syndromes of importance in dogs and cats](https://pubmed.ncbi.nlm.nih.gov/22111652/)
- [Molecular and phenotypic analysis of rodent models reveals conserved and species-specific modulators of human sarcopenia](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7881157/)

---

### 15. Model Organisms

**Model types and induction strategies:**
- **Natural aging models** — considered the **most representative/suitable** model, as it most closely resembles the human aging process compared to genetic or accelerated-senescence models (though slow and resource-intensive). **Aged Fischer-344/Brown Norway F1 hybrid rats** are a widely used strain, showing progressive skeletal muscle atrophy with age while remaining relatively disease-free until advanced age — a valuable feature for isolating pure aging effects from comorbid pathology.
- **Senescence-accelerated models** — **SAMP8 (senescence-accelerated mouse-prone 8)** mice are commonly used for accelerated-timeline aging studies, including metabolic changes in specific muscles (e.g., extensor digitorum longus).
- **Genetic modification models** — e.g., muscle-specific **OPA1 knockout** mice (mitochondrial dynamics disruption) recapitulate sarcopenia-relevant pathophysiology; a 2024 JCI paper describes a mouse sarcopenia model revealing **sex- and age-specific differences** in phenotypic/molecular characteristics.
- **Induced-atrophy models** — hindlimb unloading/suspension, surgical or chemical denervation, and immobilization are used to model the disuse-related mechanistic arm specifically (complementary to, but mechanistically distinct from, natural aging models).

**Evaluation methods:** Grip strength testing, treadmill/rotarod functional performance, muscle mass and fiber cross-sectional area quantification, fiber-type distribution analysis, and (in genetic models) targeted molecular pathway readouts (mitochondrial function, UPS activity, satellite cell markers).

**Model limitations:** Genetically modified and senescence-accelerated models can decouple specific pathway perturbations from the full multifactorial aging process, so findings may not fully generalize to naturally aging (and especially human) sarcopenia; natural aging models, while more representative, are slow, costly and confounded by comorbid age-related pathology in longer-lived strains.

**Applications:** Rodent models are used to dissect individual mechanistic contributions (mitochondrial, NMJ, satellite cell, inflammatory) that are difficult to isolate in human cohort studies, and to test candidate pharmacological interventions (myostatin/activin pathway antagonists in particular) prior to human trials.

Sources:
- [Mouse models of accelerated aging in musculoskeletal research](https://www.sciencedirect.com/science/article/pii/S1568163723002775)
- [Animal models of sarcopenia — Aging Cell](https://onlinelibrary.wiley.com/doi/full/10.1111/acel.13223)
- [Two Types of Mouse Models for Sarcopenia Research](https://pmc.ncbi.nlm.nih.gov/articles/PMC8441530/)
- [JCI - Mouse sarcopenia model reveals sex- and age-specific differences](https://www.jci.org/articles/view/172890)
- [The recent development, application, and future prospects of muscle atrophy animal models](https://onlinelibrary.wiley.com/doi/full/10.1002/mef2.70008)

---

## Curation Notes for dismech KB Entry

1. **MONDO binding needs live verification.** MONDO:0006516 returned as obsolete in this search — before binding `disease_term`, run the standard OAK/OLS lookup workflow (per the `dismech-terms` skill) to find the current, non-obsolete replacement term, if one exists, rather than trusting this report's identifier.
2. **No canonical single HP term surfaced** for "sarcopenia" itself in this search pass — the phenotype triad (low strength/low mass/low performance) likely needs to be represented via component HP terms rather than one umbrella term; verify directly against a live HPO instance during curation.
3. **This is a polygenic/complex-disease entry**, not a Mendelian one — the `genetic:` section should likely use `relationship_type: SUSCEPTIBILITY` for the GWAS loci listed (IRS1, FTO, HSD17B11, VCAN, ADAMTSL3, ESR1, NOS3, KLF5, HLA-DQA1) and for ACTN3/MSTN polymorphisms, not causal variant framing.
4. **The bimagrumab mass-vs-function dissociation** is a mechanistically important, citable nuance worth capturing explicitly in a `treatments[].evidence` or `notes` field — several independent trials (2017 phase 2, JAMA Network Open, 2025 post-hip-fracture) converge on the same finding.
5. **NCIT already codes "Acute Sarcopenia" (NCIT:C189016) distinctly from chronic** — this could inform a `temporality` qualifier (ACUTE/CHRONIC) on phenotype/pathophysiology descriptors per the Descriptor Qualifier Slots convention.
6. All PMIDs/URLs above should be run through the standard `just fetch-reference` and snippet-verification workflow before being embedded as `evidence:` blocks in any KB YAML — this report is a research lead, not pre-verified curation content.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 37 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 37 |
| On topic | 22 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 19 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CL:0000738` (1 mention) - the report calls it "leukocyte, for inflammatory infiltrate"; CL calls it **leukocyte**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `MONDO:0006516` (obsolete sarcopenia) (2 mentions)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCIT:C189016` (3 mentions) - the report calls it "Acute Sarcopenia", "NCIT already codes "Acute Sarcopenia"; NCIT calls it **Acute Sarcopenia**
- `GO:0008283` (1 mention) - the report calls it "cell population proliferation, satellite cells"; GO calls it **cell population proliferation**
- `GO:0043123` (1 mention) - the report calls it "positive regulation of NF-κB signaling"; GO calls it **positive regulation of canonical NF-kappaB signal transduction**, and lists "positive regulation of I-kappaB kinase/NF-kappaB signaling" among its other names
- `GO:0032496` (1 mention) - the report calls it "response to lipopolysaccharide/inflammation"; GO calls it **response to lipopolysaccharide**
- `GO:0005160` (1 mention) - the report calls it "TGF-beta receptor binding, for myostatin/activin signaling"; GO calls it **transforming growth factor beta receptor binding**, and lists "TGF-beta receptor binding" among its other names
- `CL:0000188` (2 mentions) - the report calls it "skeletal muscle fiber"; CL calls it **cell of skeletal muscle**, and lists "skeletal muscle cell" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCIT:C189016` - called "Acute Sarcopenia", "NCIT already codes "Acute Sarcopenia"