---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5-5
cached: false
start_time: '2026-10-02T01:47:53.607256'
end_time: '2026-10-02T01:49:23.325880'
duration_seconds: 89.72
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Serotonin Syndrome
  mondo_id: MONDO:0018546
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
  - claude-sonnet-5-5
  num_turns: 8
  total_cost_usd: 0.8850414000000002
  session_id: 81562984-f39d-5787-be67-7015e0b1b678
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 3
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
citation_count: 1
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 7
  quotes_valid: 7
  relevance_assessed: 13
  on_topic: 6
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 3
  verified: 3
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Serotonin Syndrome
- **MONDO ID:** MONDO:0018546 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Serotonin Syndrome** covering all of the
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

I'll check the key citations against PubMed before writing the report.

My recalled PMIDs were all wrong, so I'll look them up by title.

# Serotonin Syndrome (Serotonin Toxicity): Research Report

**Citation status.** I checked these PMIDs against PubMed this session, and the titles match. Quoted abstract text is limited to the abstracts I retrieved.
- PMID:2035713 Sternbach 1991, Am J Psychiatry
- PMID:15784664 Boyer & Shannon 2005, N Engl J Med (no abstract text was returned)
- PMID:24358002 Volpi-Abadie 2013, Ochsner J
- PMID:27406219 Werneke 2016, BMC Neurol
- PMID:33378846 Werneke 2020, J Integr Neurosci
- PMID:10941349 Mason 2000, Medicine (Baltimore)
- PMID:9034418 Mason 1997, Ann Pharmacother

Hunter criteria (Dunkley 2003) is PMID:12925718, from an author and title search. I did not retrieve its record.

My first-recall PMIDs for Boyer, Sternbach and Dunkley were all wrong. Anything below tagged **[unverified]** comes from general knowledge, has no PMID, and must be sourced before it goes into the knowledge base. Frequencies, odds ratios and incidence figures are mostly in that category. I did not retrieve primary data on them.

---

## 1. Disease Information

**Overview.** Serotonin syndrome (SS), also called serotonin toxicity, is an acute, potentially life-threatening drug-induced condition. Excess serotonergic activity at central and peripheral 5-HT receptors causes mental-status change, neuromuscular hyperactivity and autonomic hyperactivity.

> "Serotonin syndrome is a potentially life-threatening syndrome that is precipitated by the use of serotonergic drugs and overactivation of both the peripheral and central postsynaptic 5HT-1A and, most notably, 5HT-2A receptors." (PMID:24358002, human clinical review)

The condition can follow therapeutic dosing, intentional overdose, or drug interactions (PMID:24358002).

**Identifiers.** The MONDO ID given in the template is MONDO:0018546. I did not verify it. Run `just validate-terms` or an OAK lookup before binding it. ICD-10-CM T43.2X- (poisoning by other antidepressants) with G90.5-style codes is **[unverified]**, and so are the MeSH and ICD-11 identifiers. There is no OMIM or Orphanet entry, because this is an acquired toxic syndrome and not a Mendelian disease.

**Synonyms.** Serotonin toxicity and serotonin toxidrome. "Serotonin storm" is informal and **[unverified]**.

**Data source.** The literature is case reports, case series, poison-center series and reviews. Disease-level criteria are derived from aggregated case data (Hunter criteria, PMID:12925718). Werneke (PMID:27406219) is a meta-analysis of individual cases.

**Classification.** Dismech should probably treat this as a drug-induced adverse-reaction entry, not a heritable disease. See the "side effect as mechanism" family in CLAUDE.md and the design-decisions register on scope.

## 2. Etiology

- **Causal factors.** Exposure to one or more serotonergic agents. Sternbach's review states the most common cause is an interaction "between serotonergic agents and monoamine oxidase inhibitors" (PMID:2035713).
- **Drug classes implicated** (classes are standard textbook content, **[unverified]** per drug):
  - SSRIs, SNRIs, TCAs and MAOIs (the highest-risk partner for combinations).
  - Opioids with serotonergic activity: tramadol, meperidine, fentanyl, methadone. Case support: tramadol with sertraline (PMID:9034418).
  - Linezolid, methylene blue, triptans, lithium, buspirone, trazodone.
  - Dextromethorphan (case: PMID:18007217, pediatric ingestion).
  - Bupropion (case: PMID:20238197).
  - St John's wort, tryptophan, and drugs of abuse such as MDMA, amphetamines and cocaine.
- **Risk factors.**
  - Polypharmacy with two or more serotonergic mechanisms, including MAOI combinations.
  - Rapid dose escalation, overdose, and switching without adequate washout.
  - Genetic risk: CYP2D6 poor-metabolizer status and serotonin-transporter or receptor polymorphisms are hypothesized. This is **[unverified]**, with no established causal variant.
- **Protective factors.** None established. Prevention is mainly avoidance of risky combinations (see §13).
- **Gene–environment interaction.** Pharmacogenetic influence on drug exposure (CYP2D6, CYP2C19) is plausible and **[unverified]**.

## 3. Phenotypes

The syndrome is a triad (PMID:24358002). The HPO IDs below are **suggestions that must be looked up before binding**, and frequencies are not sourced. The Sternbach features are stated in PMID:2035713.

| Phenotype | Type | Suggested HPO (verify) | Notes |
|---|---|---|---|
| Altered mental status, agitation, confusion | Behavioral/sign | Confusion; Agitation | Mental-status change is part of the triad (PMID:24358002) |
| Restlessness | Symptom | Restlessness | PMID:2035713 |
| Myoclonus | Sign | Myoclonus | PMID:2035713 |
| Hyperreflexia, clonus (inducible, ocular, spontaneous) | Sign | Hyperreflexia; Clonus | Central to the Hunter criteria (PMID:12925718) |
| Tremor | Sign | Tremor | PMID:2035713 |
| Diaphoresis | Sign | Hyperhidrosis | PMID:2035713 |
| Shivering | Sign | Shivering | PMID:2035713 |
| Hyperthermia | Sign | Hyperthermia | Present in only a minority of cases (PMID:27406219) |
| Mydriasis, tachycardia, diarrhea, hypertension | Signs | Mydriasis; Tachycardia; Diarrhea | Autonomic, **[unverified]** |
| Rigidity (lower limbs greater than upper) | Sign | Muscle rigidity | Severe cases, **[unverified]** |
| Rhabdomyolysis, elevated CK, metabolic acidosis | Laboratory | Rhabdomyolysis; Elevated serum creatine kinase | Severe cases, **[unverified]** |

**Characteristics.**
- **Onset.** Typically rapid after the drug exposure, but Werneke found "not all cases seem to be of rapid onset" (PMID:27406219).
- **Severity.** Ranges from mild to life-threatening.
- **Course.** Resolution "typically resolves within 24 hours, but confusion can last for days, and death has been reported" (PMID:2035713).
- **Hyperthermia.** "Only relatively few cases may present with hyperthermia" (PMID:27406219).
- **Quality of life.** No data retrieved. It is a self-limited acute illness for most patients.

## 4. Genetic/Molecular Information

- **Causal genes.** None. It is not a Mendelian disease.
- **Modifier and susceptibility candidates** (all **[unverified]**): CYP2D6 and CYP2C19 (drug clearance), SLC6A4 (serotonin transporter), HTR2A (receptor), MAOA, and TPH2.
- **Epigenetics and chromosomal abnormalities.** Not applicable.
- When a gene is added to `genetic:`, use `relationship_type: MODIFIER` or `SUSCEPTIBILITY`. Do not use `CAUSATIVE`.

## 5. Environmental Information

- **Exposures.** Pharmacological only, with the agents listed in §2. For ECTO binding, search the exact exposure terms and record the queries, per the dismech-terms rules. Use `environmental[].influences_mechanisms` with `environmental_effect: TRIGGERS`.
- **Lifestyle.** Recreational drugs (MDMA, cocaine) and supplements (St John's wort, tryptophan) are **[unverified]** as to relative contribution.
- **Infectious agents.** None.

## 6. Mechanism / Pathophysiology

**Causal chain** (steps 1–4 and 6 are textbook-level; sources are PMID:24358002, PMID:2035713 and PMID:33378846, and step 5 is inferred):
1. A serotonergic drug, or a combination, is taken. Mechanisms include increased synthesis (tryptophan), increased release (amphetamines, MDMA), reduced reuptake (SSRIs, SNRIs, TCAs), reduced metabolism (MAOIs, linezolid, methylene blue), or direct agonism (buspirone, triptans, LSD).
2. Extracellular serotonin (5-HT) rises or the receptors are directly stimulated. This leads to
3. over-activation of postsynaptic 5-HT receptors, "most notably 5HT-2A" and also 5-HT1A (PMID:24358002). This leads to
4. neuromuscular hyperactivity (clonus, hyperreflexia, tremor, rigidity), autonomic instability, and altered mental status.
5. In severe cases, sustained muscle activity produces hyperthermia, rhabdomyolysis and acidosis. This step is **inferred**, not shown as a demonstrated mechanism in the retrieved sources.
6. Multi-organ complications follow: DIC, renal failure and death.

**Branching.** The pharmacology differs by trigger. MAOI plus another serotonergic drug causes massive synaptic 5-HT, while overdose of a reuptake inhibitor causes a more graded rise. The 5-HT2A contribution to hyperthermia, and the role of 5-HT1A in the mild to moderate presentation, are debated and **[unverified]** here.

**Suggested ontology terms** (look up before binding; none are verified):
- GO: serotonin receptor signaling pathway; serotonin uptake and metabolic process.
- CL: serotonergic neuron; skeletal muscle fiber.
- CHEBI: serotonin; the individual drugs.

**Molecular profiling, single-cell and spatial data, multi-omics, CRISPR screens.** I found none.

## 7. Anatomical Structures Affected

- **Primary.** Central nervous system. The key serotonergic nuclei are the brainstem raphe nuclei **[unverified]**, with projections to the cortex and spinal cord.
- **Peripheral.** Skeletal muscle (hyperactivity), gut (diarrhea, since most body 5-HT is enterochromaffin-derived **[unverified]**), and the autonomic nervous system.
- **Secondary.** Kidney (rhabdomyolysis-related injury) and the hematologic system (DIC) in severe cases.
- **Subcellular.** Plasma membrane 5-HT receptors and presynaptic terminals.
- **Laterality.** Bilateral and symmetric.

## 8. Temporal Development

- **Onset.** Any age, acute to subacute. Rapid onset is typical, but not universal (PMID:27406219).
- **Stages.** Mild, moderate and severe grades are used clinically (PMID:24358002 describes a spectrum), but I did not retrieve a staging source.
- **Course.** Self-limited once the offending agent is stopped (PMID:2035713). A long half-life agent or a MAOI can prolong it.
- **Critical period.** The first hours after a new combination or dose change. This is clinical lore and **[unverified]**.

## 9. Inheritance and Population

- **Inheritance.** Not applicable. Do not add an `inheritance:` block.
- **Epidemiology.** I did not retrieve incidence data. Specific incidence figures, poison-center counts and the proportion of antidepressant-treated patients affected are **[unverified]**. Mild cases are likely underrecognized (PMID:24358002 emphasizes awareness and diagnostic accuracy).
- **Demographics.** There is no known sex or ethnic predilection. Pediatric cases occur, for example after dextromethorphan (PMID:18007217) and in a 12-year-old with a mixed SS/NMS presentation (PMID:30964850).

## 10. Diagnostics

- **Diagnosis is clinical.** There is no confirmatory laboratory test.
- **Criteria.**
  - Sternbach (PMID:2035713), the original system.
  - Hunter Serotonin Toxicity Criteria (Dunkley, PMID:12925718).
  - Werneke's meta-analysis found "little agreement between current criteria systems for the diagnosis of serotonin syndrome" (PMID:27406219).
  - The Hunter criteria, with their emphasis on clonus and hyperreflexia, are widely preferred. That preference is **[unverified]** by the sources I retrieved.
- **Differential diagnosis.** Neuroleptic malignant syndrome (NMS), anticholinergic toxicity, malignant hyperthermia, sepsis and CNS infection, and withdrawal states. NMS and SS can be hard to separate (PMID:30964850, PMID:32940904). Distinguishing features are onset tempo, clonus and hyperreflexia (SS) versus bradyreflexia and "lead-pipe" rigidity (NMS). The distinctions are **[unverified]** in the sources I read.
- **Laboratory work-up.** CK, electrolytes, renal function, coagulation, ABG and drug screen, to look for complications and exclude mimics (**[unverified]**).
- **Genetic testing, imaging, screening.** Not applicable.

## 11. Outcome / Prognosis

- Most cases resolve within about 24 hours of stopping the agent (PMID:2035713).
- "Death has been reported" (PMID:2035713). I did not retrieve mortality rates.
- **Complications** in severe cases: rhabdomyolysis, DIC, renal failure and seizures (**[unverified]**).
- **Prognostic factors.** Severity at presentation, extent of hyperthermia, and the offending agent's half-life (**[unverified]**).

## 12. Treatment

- **Core management** (PMID:2035713): "discontinuation of the suspected serotonergic agent and institution of supportive measures."
- **Supportive care.** IV fluids, sedation with benzodiazepines, and external cooling. NCIT: Supportive Care (NCIT:C15747, listed in CLAUDE.md).
- **Pharmacological antidote.** Cyproheptadine, a 5-HT2A antagonist, is the usual choice for moderate cases. I have not retrieved a source for its efficacy and it **needs one**. Chlorpromazine and olanzapine are alternatives, and I have not sourced those either.
- **Severe disease.** Intubation, paralysis with a non-depolarizing agent, and ICU care. Antipyretics are ineffective because the hyperthermia is muscular, not hypothalamic. All **[unverified]**.
- **Case-level report.** Propofol therapy after dextromethorphan ingestion (PMID:18007217); management of severe hypertension in SS (PMID:30886699).
- **Pharmacogenomics.** No guideline-level recommendation found.
- **Clinical trials.** I did not search ClinicalTrials.gov. No randomized trials of treatment are known to me, and that is **[unverified]**.
- **Suggested NCIT terms** (look up each CURIE, don't copy): Supportive Care `NCIT:C15747`; Pharmacotherapy `NCIT:C15986` with `therapeutic_agent` bound to CHEBI for cyproheptadine.

## 13. Prevention

- **Primary.** Avoid combining serotonergic agents. Observe MAOI washout intervals (about 2 weeks for most, longer for fluoxetine **[unverified]**). Use prescribing alerts. Educate clinicians and patients (PMID:24358002).
- **Secondary and tertiary.** Early recognition and drug withdrawal prevent progression. After an episode, document the culprit combination and avoid re-challenge.
- **Vaccines, screening, genetic counseling.** Not applicable.

## 14. Other Species / Natural Disease

- Serotonin toxicity occurs in dogs and cats (e.g., after SSRI or 5-HTP ingestion), and I did not retrieve a citation. It is **[unverified]**.
- NCBITaxon IDs to bind after lookup: *Canis lupus familiaris*, *Felis catus*.
- OMIA does not apply, since this is not a heritable disease.
- Not zoonotic.

## 15. Model Organisms

- **Rodent models** are drug-induced (MAOI plus a serotonin precursor or releaser, or direct agonists such as 5-MeO-DMT). The behavioral "serotonin syndrome" scoring in rats and mice (forepaw treading, hindlimb abduction, Straub tail, tremor) is textbook content and **[unverified]** here.
- **Fidelity.** Reproduces the neuromuscular and thermoregulatory signs. The limits are species differences in 5-HT receptor distribution and the absence of the human drug-combination context.
- In dismech, put animal data under `animal_models:` and link it to the pathograph with `modeled_mechanisms`. Use `evidence_source: MODEL_ORGANISM`.
- Genetic models (e.g., SERT or MAOA knockouts, Tph2 manipulations) are **[unverified]**.

---

## Curation notes for dismech

- **Entry type.** Likely a `DISEASE` (drug toxidrome) with no genes or inheritance. Check the stub's `entry_type` first.
- **Mechanism chain nodes** to model:
  1. Serotonergic drug exposure.
  2. Increased synaptic serotonin.
  3. 5-HT2A (and 5-HT1A) over-activation.
  4. Neuromuscular hyperactivity.
  5. Hyperthermia and rhabdomyolysis.
- **Evidence still needed.** Each of these is **[unverified]** above and needs a sourced PMID with an exact abstract quote (via `just fetch-reference`): Hunter criteria, cyproheptadine efficacy, incidence, mortality, and the CYP2D6 and other genetic contributions.
- **Hunter criteria.** `just fetch-reference PMID:12925718` before citing.
- **Boyer & Shannon (PMID:15784664).** No abstract text was returned. Fetch it into `references_cache/` and quote from there.

## Sources (retrieved this session)

- PubMed E-utilities esearch, esummary and efetch for the PMIDs listed at the top, e.g. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=15784664,24358002,2035713,27406219,33378846

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 7 |
| Quoted claims found in source | 7 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 13 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.