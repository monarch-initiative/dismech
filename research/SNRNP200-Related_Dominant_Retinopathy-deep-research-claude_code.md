---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-25T16:35:48.306748'
end_time: '2026-10-25T16:37:52.163669'
duration_seconds: 123.86
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: SNRNP200-Related Dominant Retinopathy
  mondo_id: MONDO:0800098
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
  - claude-haiku-5-5
  - claude-sonnet-5-5
  web_search_requests: 3
  num_turns: 20
  total_cost_usd: 0.9847889999999999
  session_id: d98baee9-c229-5d8a-96f8-a4aee10f9c40
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 9
reference_validation:
  total_references: 36
  verified: 36
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 36
  on_topic: 32
  validator_version: 0.3.0
term_validation:
  total_terms: 25
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 3
  labels_variant: 5
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SNRNP200-Related Dominant Retinopathy
- **MONDO ID:** MONDO:0800098 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SNRNP200-Related Dominant Retinopathy** covering all of the
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

Pulling the abstracts for the key SNRNP200 papers from Europe PMC, since PubMed is rate-limiting me.

# SNRNP200-Related Dominant Retinopathy (RP33): Research Report

**Scope and verification status.** I could reach PubMed search listings, a Frontiers full-text page, and web-search summaries. PubMed abstract pages returned 429 or cookie walls. A script to pull abstracts from Europe PMC needed an approval that did not come through, so I did not run it. Consequences:
- PMIDs below come from a PubMed result list (title, first author, journal, year). That list shows titles only, so PMIDs are reliable but content descriptions of papers I did not open are inferred from titles.
- The only verbatim quote I confirmed is one sentence from Zhang 2021 (Section 3). Everything else is paraphrase and is marked as such.
- Items marked **[unverified]** need checking before they go into the KB. Run `just fetch-reference PMID:…` and copy exact snippets from the cache.

## 0. Identifier discrepancy to resolve first

- The template gives **MONDO:0800098**. I could not confirm it.
- Searches (MedGen, DrugMap, Monarch/MGI mirrors) returned **MONDO:0012477** with **OMIM:610359**. These are for "retinitis pigmentosa 33" (RP33), defined as retinitis pigmentosa caused by mutation in SNRNP200. [MGI OMIM:610359](https://informatics.jax.org/disease/OMIM:610359), [LOVD RP33](https://databases.lovd.nl/shared/diseases/02933), [MedGen](https://ncbi.nlm.nih.gov/medgen/332080)
- Look up both CURIEs with `runoak` before binding. If MONDO:0800098 is a gene-defined "SNRNP200-related" umbrella term, check the lump/split and `mappings.mondo_mappings` predicate (`exactMatch` or `narrowMatch` only retire the stub).
- I found no Orphanet ORPHA code. Gene OMIM is 601664. [OMIM 601664](https://https.ncbi.nlm.nih.gov/omim/601664)

## 1. Disease information

- **Overview.** RP33 is nonsyndromic autosomal dominant retinitis pigmentosa (adRP). It is a rod-cone degeneration caused by heterozygous missense variants in SNRNP200 (2q11.2).
- **Gene function.** SNRNP200 encodes BRR2 (Brr2), a DEXH-box RNA helicase in the U5 snRNP and the U4/U6-U5 tri-snRNP. It unwinds the U4/U6 duplex to activate the spliceosome. [GeneCards](https://www.genecards.org/card/SNRNP200)
- **Discovery.** Zhao et al. 2009 (Am J Hum Genet, **PMID:19878916**) mapped RP33 to 2cen-q12.1. They found c.3260C>T (p.S1087L), segregating through four generations and absent in 400 controls (from search summary [AJHG 2009 abstract mirror](https://mobile.jci.org/references/scholar/28689/B85)). The title, from PubMed, describes a mutation affecting U4/U6 unwinding.
- **Synonyms.** RP33; retinitis pigmentosa 33; SNRNP200-related retinitis pigmentosa; BRR2/ASCC3L1-associated adRP (the older gene name ASCC3L1 appears in Li 2010, PMID:19710410).
- **Data type.** Aggregated disease-level resources (OMIM, MONDO, ClinVar) plus family and cohort reports.
- **Related spliceosomal adRP.** PRPF3, PRPF4, PRPF6, PRPF8, PRPF31 and SNRNP200 form a "splicing-factor RP" group. See reviews PMID:34395430 (Yang 2021) and PMID:27302685 (Růžičková 2017), and the GeneReviews overview PMID:20301590. This group is a candidate for a `Grouping` entry, not for lumping.

## 2. Etiology

- **Cause.** Monogenic, germline, dominant. No environmental cause is known.
- **Genetic risk.** Pathogenic or likely pathogenic missense variants in SNRNP200. Modifier genes are not established **[unverified]**.
- **Environmental, protective and gene-environment factors.** None reported in my searches.
- **Recessive alleles.** Gerth-Kahlert 2019 (**PMID:31260034**, title: "Recessive and dominant SNRNP200 variants causing RP") suggests some alleles act recessively. Read this paper before deciding whether the entry needs a recessive subtype.

## 3. Phenotypes

**Clinical features.** The terms below are suggested from MedGen's HPO listing for RP33 and from general adRP knowledge. Percentages, onset and severity are not extracted. Frequency data would come from PMID:31486839 (Yusuf 2019, JAMA Ophthalmol, "Clinical characterization of RP with SNRNP200 variants"), which I did not read.

| Phenotype | Suggested HPO | Notes |
|---|---|---|
| Night blindness (nyctalopia) | HP:0000662 | Early symptom; MedGen lists it |
| Rod-cone dystrophy / retinitis pigmentosa | HP:0000510 | Core feature |
| Optic disc pallor | HP:0000543 | MedGen lists it |
| Constriction of peripheral visual field | HP:0001133 | Expected in adRP |
| Reduced or absent ERG | HP:0000550 / HP:0000512 | Expected |
| Bone-spicule retinal pigmentation | HP:0007737 | Expected |
| Reduced visual acuity | HP:0007663 | Late |

All HPO CURIEs are from memory and must be looked up before use.

- **Onset.** In the one family I could read (Zhang 2021, **PMID:33553197**, Front Med), night-vision symptoms began at ages 5, 7 and 9. Children's onset is therefore possible.
- **Severity.** Reports suggest a severe, early-onset adRP spectrum **[unverified]**.
- **Quote (verified from the Frontiers page):** "Heterozygous SNRNP200c.C6088T (p.Arg2030Cys) mutation was ascertained in two members of this family." [Frontiers](https://www.frontiersin.org/articles/10.3389/fmed.2020.588991/full)
- **Family detail from the same page.** The variant was in the proband (27) and his father (48). A third affected relative (III-2) lacked the variant, suggesting a phenocopy or a second cause. This weakens simple segregation for p.R2030C.
- **Quality of life.** I found no data.

## 4. Genetic and molecular information

- **Gene.** SNRNP200 (HGNC symbol; KB form `hgnc:30`**[unverified, look up]**), OMIM 601664, 2q11.2.
- **Variants** (confirmed in search summaries):
  - c.3260C>T, p.S1087L: the original and recurrent hotspot. See Chen 2013 (**PMID:24499697**), whose title names the p.S1087L hotspot.
  - c.3269G>T, p.R1090L: reported in a 4-generation Chinese family (Li 2010, PMID:19710410, per the OMIM summary).
  - p.R2030C (Zhang 2021, PMID:33553197).
- **Other variant papers** (content inferred from titles only):
  - Benaglio 2011, PMID:21618346 (pooled sequencing, new SNRNP200 mutations).
  - Liu 2012, PMID:23029027 (novel missense in a Chinese family).
  - Zhang 2013, PMID:23887765 (southern Chinese cohort).
  - Bowne 2013, PMID:24319334, titled "SNRNP200 causes 1.6% of adRP" (a Mol Vis cohort study).
  - Pan 2014, PMID:24940031.
  - Coussa 2015, PMID:26720483 (French Canadian).
  - Van Cauwenbergh 2017, PMID:28076437 (Belgian).
  - Ezquerra-Inchausti 2017, PMID:28045043 (Spanish).
  - Wu 2018, PMID:30360737.
  - Xiao 2021, PMID:33598457 (138 Chinese adRP families).
  - Lee 2023, PMID:36856324.
  - Finnegan 2026, PMID:42405195 (Irish cohort).
- **Variant class.** Heterozygous missense, clustered in the helicase cassettes. S1087L and R1090L sit in the "ratchet" helix of the first Sec63 domain (search summary). No truncating variants are reported in my sources.
- **Allele frequency and ClinVar/ClinGen classification.** I did not look these up. Check ClinGen gene-disease validity with `just check-gene-validity`.
- **Functional consequence.** Not simple loss of function. Evidence is for impaired U4/U6 unwinding, altered splice-site fidelity and altered RNA binding. A dominant-negative mechanism is proposed on zebrafish evidence (Zhang 2021), and the Zimmann 2025 paper is worded as a partial loss/altered function **[unverified]**. Use `functional_impact_category` carefully (e.g. `DOMINANT_NEGATIVE` only if a source states it).
- **Somatic or germline.** Germline.
- **Epigenetics and chromosomal abnormalities.** Not applicable or not reported.

## 5. Environmental information

Not applicable. No toxins, lifestyle factors or infectious agents are reported as contributors. Separately, SNRNP200 has a role in viral RNA sensing and IRF3 activation (Tremblay 2016, **PMID:27454487**). That is an immune function of the protein, not an infectious cause of the retinopathy.

## 6. Mechanism and pathophysiology

**Causal chain** (steps marked *inferred* are not directly demonstrated in patient retina):

1. A heterozygous missense variant in SNRNP200 (e.g. S1087L, R1090L) changes the Brr2 helicase. These variants sit in the first Sec63 ratchet region (search summary).
2. The altered Brr2 is still incorporated into the spliceosome. snRNP assembly is not compromised (human-cell study, search summary of PMID:26968627 **[PMID from a DisGeNET index entry; verify]**).
3. U4/U6 unwinding is impaired. The yeast Brr2p equivalents show marked unwinding defects without assembly defects (search summary of Zhao 2009).
4. The mutant protein changes binding to U4 and U6 snRNAs (iCLIP, FRAP and helicase assays in HeLa and RPE cells, [PMC11883072](https://pmc.ncbi.nlm.nih.gov/articles/PMC11883072) = Zimmann 2025, PMID:40045025). Mutant Brr2 also spends less time on pre-mRNAs (Cvačková 2014, PMID:24302620, per OMIM summary).
5. Splicing fidelity falls, with more cryptic 5' splice-site use in a β-globin reporter (OMIM summary of Cvačková 2014) and altered splicing of cellular transcripts such as LDHA (NLK record summary).
6. *Inferred:* the altered splicing of retina-relevant transcripts, together with spliceosome stress in cells with a very high splicing load, causes rod photoreceptor and RPE dysfunction.
7. Rod photoreceptors degenerate, then cones, causing night blindness, field loss and eventual central vision loss.

**Open questions.** Why a ubiquitous protein harms mainly the retina is unresolved. Tissue-specificity reviews are PMID:40264708 (Kemal 2025) and PMID:27302685. A Brr2–Prp8 interaction is relevant, because the Prp8 C-terminal tail inhibits Brr2 (Mozaffari-Jovin 2013, **PMID:23704370**), and the Zimmann 2025 title concerns SNRNP200 variants and PRPF8 binding. Mozaffari-Jovin 2014 (**PMID:24643059**) covers Brr2 regulation and retinal disease.

**Suggested ontology terms** (look up before use; GO IDs from memory):
- GO: mRNA splicing, via spliceosome (GO:0000398); U4/U6 x U5 tri-snRNP complex (GO:0046540); RNA helicase activity (GO:0003724).
- CL: retinal rod cell (CL:0000604); retinal pigment epithelial cell (CL:0002586); retinal cone cell (CL:0000573).
- No transcriptomic, proteomic or metabolomic patient datasets were found. Zimmann 2025 contains iCLIP data from HeLa and RPE cells.

## 7. Anatomical structures affected

- **Organ.** Retina, bilateral; the optic disc is secondarily pale. UBERON suggestions (verify): retina (UBERON:0000966), eye (UBERON:0000970), optic disc (UBERON:0001789).
- **Cells.** Rod photoreceptors first, then cones; RPE is implicated.
- **Subcellular.** Nucleus, nuclear speckles and the spliceosome (GO:0005681 spliceosomal complex).
- **Extra-retinal.** Typically none (nonsyndromic).
- **Lateralization.** Bilateral; symmetry is not documented in my sources.

## 8. Temporal development

- **Onset.** Childhood to young adult (symptoms at 5–9 years in one family). Adult-onset families are also reported for other alleles **[unverified]**.
- **Progression.** Progressive rod-cone degeneration. Staging and quantification are in Yusuf 2019, PMID:31486839 (unread).
- **Remission.** None expected.

## 9. Inheritance and population

- **Inheritance.** Autosomal dominant (HP:0000006). Penetrance, expressivity and any anticipation were not verified.
- **Prevalence of the genetic cause.** Bowne 2013 (PMID:24319334): per its title, SNRNP200 accounts for about 1.6% of adRP in that cohort.
- **Population distribution.** Chinese cohorts report repeated findings, with S1087L a hotspot (PMID:24499697). Other cohorts are listed in Section 4. A founder effect is not established.
- **Overall disease prevalence and sex ratio.** No data found. Parent group: adRP in total is roughly 1 in 3,500–4,000 for all RP, which I am quoting from general knowledge **[unverified]**.

## 10. Diagnostics

- **Clinical.** Fundus exam, optical coherence tomography (OCT), fundus autofluorescence, visual fields and full-field ERG (rod-cone pattern). Retinal imaging details for SNRNP200 patients are in Yusuf 2019 (unread).
- **Genetic.** Retinal dystrophy gene panels or exome sequencing. SNRNP200 is on the Genomics England PanelApp retinal panels ([PanelApp](https://panelapp.genomicsengland.co.uk/panels/509/gene/SNRNP200/)). Copy-number analysis is of marginal use (Bujakowska 2017, PMID:27735924).
- **Differential.** Other adRP genes (RHO, PRPF31, PRPF8, PRPF3, PRPF6, PRPF4, RP1, PERIPHERIN/PRPH2, IMPDH1). The GeneReviews overview PMID:20301590 gives the standard approach.
- **Screening.** Cascade testing of relatives. No newborn screening.

## 11. Outcome and prognosis

No survival effect (nonsyndromic). Expected outcome is progressive vision loss with legal blindness in many older patients. Complications likely include cataract and cystoid macular edema, as in RP generally **[unverified for this gene]**. Genotype-specific prognosis is the focus of Yusuf 2019.

## 12. Treatment

- **No disease-modifying therapy for SNRNP200-RP is approved.**
- **Supportive care.** Low-vision rehabilitation, orientation and mobility training, and cataract or macular edema management. Suggested NCIT terms (verify): Supportive Care (NCIT:C15747), Rehabilitation (NCIT:C15315), Genetic Counseling (NCIT:C15240).
- **Gene therapy.** Not applicable to a dominant-negative or toxic-gain allele in the usual replacement approach. Allele-specific silencing or editing is theoretical. No SNRNP200 trial was found; I did not search ClinicalTrials.gov directly.
- **Experimental lead.** N-acetylcysteine reduced retinal defects in Drosophila SNRNP200 models (Mayer 2026, **PMID:42593897**, title only). Treat as preclinical.
- **Pharmacogenomics.** None.

## 13. Prevention

Genetic counselling and cascade testing; prenatal or preimplantation diagnosis is possible for a known familial variant. No primary prevention exists.

## 14. Other species and natural disease

No naturally occurring disease linked to SNRNP200 was found in my searches. I did not check OMIA. Orthologs exist in all model species below (NCBI Gene IDs not looked up).

## 15. Model organisms

- **Zebrafish.** snrnp200 is expressed in the retinal ciliary marginal zone. Mutant R2030C mRNA gave deformities in 53% of larvae versus 9% for wild type. Co-injection with morpholino raised mortality, interpreted as dominant-negative (Zhang 2021, PMID:33553197). **Caveat:** the text and Figure 6 legend disagree on mortality (77% vs 34%), and this is an overexpression model, so fidelity is low. Earlier work on Snrnp200 knockdown in rods is Liu 2015, **PMID:26137319**.
- **Mouse.** Graziotto 2011 (**PMID:20811066**) describes three splicing-factor RP mouse models (title: late-onset degeneration). Per the title these are Prpf3, Prpf8 and Prpf31 models, not Snrnp200, **[unverified]**. I found no Snrnp200 patient-allele mouse.
- **Drosophila.** SNRNP200 models (Mayer 2026, PMID:42593897).
- **C. elegans.** Splicing-related RP mutations modeled (Kukhtar 2020, **PMID:31919495**).
- **Yeast.** Brr2p mutants show U4/U6 unwinding defects (see Section 6).
- **Human cells and iPSC.** HeLa and RPE cells (Zimmann 2025). An iPSC line from an adRP patient exists (Zhang 2025, **PMID:40403403**, which I have not confirmed carries a SNRNP200 variant).
- **Dismech note.** Use `animal_models` for zebrafish, Drosophila and C. elegans, with `modeled_mechanisms` links. Use `experimental_models` for cell lines and iPSC. Cell-line splicing data should carry `evidence_source: IN_VITRO`.

## Curation recommendations

1. Verify MONDO:0800098 vs MONDO:0012477 first.
2. Fetch and read PMID:19878916, 31486839, 24319334, 31260034, 24302620, 40045025 before writing evidence; copy snippets from the cache, not from this report.
3. Consider a splicing-factor RP `Grouping`, and a module for spliceosome function (check `just list-modules splic` first).
4. Treat the R2030C family as weakly segregating, because of the affected non-carrier.
5. Record the dominant-negative claim as proposed, not established.

## Sources
- [Zhang 2021, Frontiers in Medicine (full text)](https://www.frontiersin.org/articles/10.3389/fmed.2020.588991/full)
- [Zimmann 2025, Cell Mol Life Sci (PMC11883072)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11883072)
- [OMIM 601664](https://https.ncbi.nlm.nih.gov/omim/601664)
- [AJHG 2009 abstract mirror](https://mobile.jci.org/references/scholar/28689/B85)
- [MGI OMIM:610359](https://informatics.jax.org/disease/OMIM:610359)
- [LOVD RP33](https://databases.lovd.nl/shared/diseases/02933)
- [MedGen](https://ncbi.nlm.nih.gov/medgen/332080)
- [PanelApp SNRNP200](https://panelapp.genomicsengland.co.uk/panels/509/gene/SNRNP200/)
- [GeneCards SNRNP200](https://www.genecards.org/card/SNRNP200)
- PubMed result list for "SNRNP200 retinitis pigmentosa" (source of all PMIDs above).

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 36 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 36 |
| On topic | 32 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 8 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 5 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000662` (1 mention) - the report calls it "Night blindness (nyctalopia)"; HP calls it **Nyctalopia**, and lists "Night blindness" among its other names
- `HP:0000510` (1 mention) - the report calls it "Rod-cone dystrophy / retinitis pigmentosa"; HP calls it **Rod-cone dystrophy**, and lists "Retinitis pigmentosa" among its other names
- `HP:0007737` (1 mention) - the report calls it "Bone-spicule retinal pigmentation"; HP calls it **Spicular pigmentation of the retina**, and lists "Bone corpuscle fundus pigmentation" among its other names
- `GO:0000398` (1 mention) - the report calls it "GO: mRNA splicing, via spliceosome"; GO calls it **mRNA splicing, via spliceosome**
- `CL:0000604` (1 mention) - the report calls it "CL: retinal rod cell"; CL calls it **retinal rod cell**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.

24 of 25 terms resolved to a current term; the rest could not be looked up either way.