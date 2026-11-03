---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-16T13:11:56.083719'
end_time: '2026-10-16T13:13:42.293470'
duration_seconds: 106.21
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spermatogenic Failure 33
  mondo_id: MONDO:0029147
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
  num_turns: 10
  total_cost_usd: 0.7850305
  session_id: e0e00ff6-67e7-5e60-9592-3e4cb1004f09
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 13
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 6
  validator_version: 0.3.0
term_validation:
  total_terms: 6
  verified: 5
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 1
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0012864
    reported_labels:
    - '? verify'
    ontology_label: Abnormal sperm morphology
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spermatogenic Failure 33
- **MONDO ID:** MONDO:0029147 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spermatogenic Failure 33** covering all of the
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

Status: I've confirmed the gene (CFAP251/WDR66) and found the key papers. Next I'm pulling the Auguste 2018 and Li 2019 abstracts so the report can quote the cohort details, then I'll write it up.

# Research Report: Spermatogenic Failure 33 (SPGF33)

**Scope and evidence limits.** This report rests on a limited set of web searches and PubMed summaries gathered in this session. I could not retrieve full abstracts verbatim (the fetch tool returned paraphrases), so **no exact-quote snippets are provided**. Curators must run `just fetch-reference PMID:<id>` and copy the quotes from the cached abstracts. Where a fact came from a secondary aggregator rather than a primary paper, I say so. Sections 5, 13, 14 and 15 are mostly not covered because I did not search for them. I marked those gaps rather than filling them from memory.

---

## 1. Disease Information

**Overview.** SPGF33 is an autosomal recessive form of male infertility. It is caused by biallelic loss-of-function variants in *CFAP251*, formerly called *WDR66*. The defining finding is multiple morphological abnormalities of the sperm flagella (MMAF), which leave the spermatozoa immotile.

**Identifiers**
- MONDO:0029147
- OMIM 618152
- MedGen C4748395

The identifiers come from [MalaCards/LOVD](https://databases.lovd.nl/shared/diseases/05565), [MedGen](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/eade6ae6e46c5bc2a2228c4c8510309416c6194b/www.ncbi.nlm.nih.gov/medgen/C4748395/index.html) and [MGI](https://informatics.jax.org/disease/OMIM:618152).
- I did not verify Orphanet, ICD-10/11 or MeSH identifiers. They are unconfirmed here.

**Synonyms:** SPGF33; spermatogenic failure, type 33 (SPGF-33).

**Gene naming.** One search summary flagged a "gene conflict" between *WDR66* and *CFAP251*. This is not a real conflict. They are the same gene under old and new HGNC symbols. Curators must bind by HGNC ID and confirm the current symbol, because the KB checks label and CURIE only for self-consistency.

**Data source.** The entry is disease-level and aggregated, drawn from case series. It is not derived from EHR data.

**Parent term.** The disease sits under the broader "spermatogenic failure" concept ([MedGen](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/eade6ae6e46c5bc2a2228c4c8510309416c6194b/www.ncbi.nlm.nih.gov/medgen/C4748395/index.html)).

## 2. Etiology

- **Causal factor:** biallelic loss of function of *CFAP251* (12q24.31).
- **Genetic risk factors:** none beyond the recessive causal variants. I found no modifier genes.
- **Environmental risk factors, protective factors and gene-environment interactions:** none identified in what I retrieved.

## 3. Phenotypes

All items are from male patients with MMAF. Frequencies are not quantified in the sources I retrieved.

| Phenotype | Suggested HPO | Notes |
|---|---|---|
| Male infertility | HP:0003251 | Universal |
| Asthenozoospermia / immotile sperm | HP:0012206 (asthenozoospermia), HP:0011961 (? verify) | Immotile spermatozoa |
| Abnormal sperm flagellum morphology (MMAF: short, absent, coiled, bent, irregular-caliber flagella) | HP:0012864 (? verify) | Defining finding |
| Abnormal acrosome, head and base | none confirmed | Reported in the OMIM-derived description |

**The HPO IDs in this table are unverified suggestions.** I did not look any of them up. Per the CLAUDE.md rule, none may be bound until a lookup (OAK or `cache/hp/terms.csv`) confirms the CURIE and label.

- **Onset:** adult presentation, usually when a couple seeks fertility evaluation. This is inferred, not sourced.
- **Quality of life:** no data retrieved.
- **Extra-gonadal features:** none were reported in the sources I saw. Whether CFAP251 loss affects motile cilia elsewhere in humans is unresolved here. A 2026 paper title suggests ciliary defects in humans and mice ([PMID:41943837](https://pubmed.ncbi.nlm.nih.gov/41943837/)), but I only saw the title.

## 4. Genetic / Molecular Information

- **Gene:** *CFAP251* (*WDR66*), 12q24.31. HGNC ID not looked up. The KB uses the lowercase `hgnc:` form.
- **Inheritance:** autosomal recessive.
- **Mechanism class:** loss of function.

**Reported variants**

| Variant | Study | Notes |
|---|---|---|
| Homozygous deletion of the two penultimate exons, mediated by an SVA retrotransposon insertion | Kherraf 2018 ([PMID:30122540](https://pubmed.ncbi.nlm.nih.gov/30122540/)) | 7 of 78 MMAF men; each deletion carried a single chimeric SVA element at the breakpoint, and the authors describe it as "ancestral" |
| g.122359334delA, p.Asp42Metfs*4 (homozygous) | Auguste 2018 ([PMID:30122541](https://pubmed.ncbi.nlm.nih.gov/30122541/)) | Two brothers |
| g.122359542G>T, p.Glu111* | Auguste 2018 | Compound heterozygous with the next row |
| g.122395032_122395033delCT, p.Leu530Valfs*4 | Auguste 2018 | Compound heterozygous with the previous row |
| Biallelic loss-of-function variants (specific changes not retrieved) | Li 2019 ([PMID:30310178](https://pubmed.ncbi.nlm.nih.gov/30310178/)) | 3 of 65 Han Chinese MMAF men (about 5%) |
| c.1192-3C>G splicing variant causing exon skipping | Wang 2022 ([PMID:35087568](https://pubmed.ncbi.nlm.nih.gov/35087568/)) | The proband inherited it through maternal uniparental disomy |

- **Variant origin:** germline.
- **Allele frequency:** the Li 2019 summary described the variants as extremely rare or absent in population databases. I did not query gnomAD.
- **Chromosomal and epigenetic information:** none retrieved.

## 5. Environmental Information

Not covered. I found no environmental, lifestyle or infectious contributors, and I did not search for them.

## 6. Mechanism / Pathophysiology

**Causal chain**

1. Biallelic loss-of-function variants (SVA-mediated exon deletion, frameshift, nonsense or splice variants) in *CFAP251* abolish or truncate the protein. This is demonstrated by genetics. Reduced protein in a patient's sperm was shown by Western blot and immunofluorescence ([PMID:35087568](https://pubmed.ncbi.nlm.nih.gov/35087568/)).
2. CFAP251 is an axonemal protein, described in the Auguste title as associated with calmodulin and the radial-spoke complex. Its loss disrupts axoneme assembly or stability in the developing sperm tail. The mechanism here is partly inferred.
3. Disrupted axoneme assembly produces the MMAF flagellar phenotype: short, absent, coiled and irregular tails.
4. Transmission electron microscopy suggested that CFAP251 loss affects mitochondrial sheath formation. Auguste's title describes the spermatozoa as "lacking mitochondria", but I only saw a summary. This step is from a small family series.
5. The abnormal flagella give immotile spermatozoa and male infertility.

**Orthologue evidence**
- Kherraf 2018 localized the *Trypanosoma brucei* ortholog to the axoneme. Reproducing the human deletion there impaired flagellar movement. This is in vitro/model-organism evidence in a protist.
- Auguste 2018 used a *Tetrahymena* ortholog to show a role in coordinated ciliary beating.

**Suggested terms.** These are leads only and none has been looked up.
- GO terms for axoneme assembly, sperm flagellum assembly and motile cilium assembly.
- CL spermatid, plus the UBERON/GO components flagellum and axoneme.

**Not covered:** omics, single-cell and functional-genomics findings. I did not search for them.

## 7. Anatomical Structures Affected

- **Primary:** testis, with the seminiferous epithelium and the developing spermatid flagellum. The sperm tail and mitochondrial sheath are the structures involved.
- **Localization:** bilateral, because the cause is systemic germline. This is inferred.
- **Secondary organs:** none documented in the sources I saw. See the caveat on cilia in Section 3.

## 8. Temporal Development

Adult-onset recognition at fertility evaluation. The condition is non-progressive and lifelong, since it is structural and genetic. Both statements are inferred and not directly sourced.

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive.
- **Prevalence:** not retrieved. Penetrance and expressivity are not characterized in what I saw.
- **Frequency among MMAF cohorts:** about 9% (7 of 78) in the Kherraf cohort and about 5% (3 of 65) in the Li Han Chinese cohort.
- **Founder effect:** Kherraf describes the SVA-mediated deletion as "ancestral". The seven men carried the same deletion type, which is consistent with a founder allele. I did not retrieve population details, so confirm before asserting one. Kherraf's cohort included North African patients. This is from the author list and the Tunisian clinical centres, not from a stated cohort description.
- **Consanguinity:** not described in the sources I saw. The Wang 2022 case was nonconsanguineous.
- **Sex ratio:** affects males only. Female carriers are presumed unaffected, though I did not verify this.

## 10. Diagnostics

- **Semen analysis** shows immotile spermatozoa and MMAF morphology. Count and morphology details were not retrieved.
- **Genetic testing:** whole-exome sequencing identified the variants in all the cited studies. Note that Kherraf's deletion is a structural variant, so copy-number-aware analysis is needed, and a standard SNV/indel pipeline may miss it. This is an inference from the mechanism.
- **Electron microscopy and immunofluorescence** can show the axonemal and mitochondrial sheath defects.
- **Differential diagnosis:** other MMAF genes such as *DNAH1*, *CFAP43*, *CFAP44* and *CFAP69*. These are from general knowledge and were not verified. A review of spermatogenic failure genetics is at [PMID:30656449](https://pubmed.ncbi.nlm.nih.gov/30656449/).

## 11. Outcome / Prognosis

No survival or life-expectancy effect is expected. The disease is confined to fertility, as far as the retrieved sources show. Reproductive prognosis is addressed in Section 12.

## 12. Treatment

- **No curative treatment** is documented.
- **Assisted reproduction:** intracytoplasmic sperm injection (ICSI) is the reported route. Wang 2022 reports a successful pregnancy after ICSI in a man with a *CFAP251* splice variant ([PMID:35087568](https://pubmed.ncbi.nlm.nih.gov/35087568/)).
- A 2026 case report describes sperm selection by hypo-osmotic swelling before ICSI in two men with flagellar defects, one involving CFAP251 ([PMID:42871648](https://pubmed.ncbi.nlm.nih.gov/42871648/)). I saw only the title.
- **Suggested NCIT term:** an assisted-reproduction or ICSI term. None has been looked up. Per the CLAUDE.md rules, search for it and omit the binding if none is suitable.
- **Pharmacotherapy, gene therapy and clinical trials:** none found. I did not search ClinicalTrials.gov.
- The Wang 2022 pregnancy is a single case. Overall ICSI success rates in *CFAP251* MMAF are unknown here.

## 13. Prevention

Not covered, apart from genetic counseling for recurrence risk. The inheritance is autosomal recessive, so a carrier couple has a 25% risk per pregnancy. A male child of two carriers would be affected. I did not search for guidelines.

## 14. Other Species / Natural Disease

Not covered. I did not check OMIA, so I make no claim about naturally occurring disease in other species.

## 15. Model Organisms

- **Protists:** *T. brucei* ortholog (axonemal localization, motility impairment with the human deletion) and *Tetrahymena* ortholog (coordinated ciliary beating). See Section 6.
- **Mouse:** I found no mouse knockout data for *Cfap251*/*Wdr66*. The searches did not turn up any. A 2026 paper title mentions "humans and mice" ([PMID:41943837](https://pubmed.ncbi.nlm.nih.gov/41943837/)), which may include a mouse model. Check this paper directly, along with MGI and IMPC.
- **Model limitations:** protist models carry the axoneme but not mammalian spermiogenesis or the mitochondrial sheath. This is a likely `HUMAN_MODEL_MISMATCH` or `KNOWLEDGE_GAP` candidate until a mouse model is confirmed.

---

## Curation Notes and Open Items

1. **Retracted papers.** The *WDR66* literature includes cancer papers unrelated to SPGF33. [PMID:29717028](https://pubmed.ncbi.nlm.nih.gov/29717028/) is retracted ([PMID:36861483](https://pubmed.ncbi.nlm.nih.gov/36861483/)) and has an expression of concern ([PMID:33870408](https://pubmed.ncbi.nlm.nih.gov/33870408/)). Do not cite any of them for this disease.
2. **Verify before binding:** all HPO, GO, CL, UBERON and NCIT suggestions above, the HGNC ID for *CFAP251*, and the Orphanet, ICD and MeSH identifiers.
3. **Exact snippets:** none are given. Fetch the references for PMIDs 30122540, 30122541, 30310178 and 35087568, and copy quotes from the cached text.
4. **Evidence source:** the case series are `HUMAN_CLINICAL`. The *T. brucei* and *Tetrahymena* results are `MODEL_ORGANISM`, and the CFAP251 localization is `IN_VITRO` or `MODEL_ORGANISM`, depending on how the paper is graded.
5. **Gaps to close:** a mouse model, ICSI success rates, the HPO frequency of each phenotype, and the Orphanet and GeneReviews status (use `just check-genereviews`).

## Sources

- [LOVD disease record 05565 (SPGF33, OMIM:618152)](https://databases.lovd.nl/shared/diseases/05565)
- [MedGen C4748395 (mirror)](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/eade6ae6e46c5bc2a2228c4c8510309416c6194b/www.ncbi.nlm.nih.gov/medgen/C4748395/index.html)
- [MGI disease page OMIM:618152](https://informatics.jax.org/disease/OMIM:618152)
- Kherraf et al. 2018, Am J Hum Genet, [PMID:30122540](https://pubmed.ncbi.nlm.nih.gov/30122540/)
- Auguste et al. 2018, Am J Hum Genet, [PMID:30122541](https://pubmed.ncbi.nlm.nih.gov/30122541/)
- Li et al. 2019, J Hum Genet, [PMID:30310178](https://pubmed.ncbi.nlm.nih.gov/30310178/)
- Wang et al. 2022, Front Genet, [PMID:35087568](https://pubmed.ncbi.nlm.nih.gov/35087568/)
- Review of spermatogenic failure genetics, [PMID:30656449](https://pubmed.ncbi.nlm.nih.gov/30656449/)
- 2026 papers seen by title only: [PMID:41943837](https://pubmed.ncbi.nlm.nih.gov/41943837/), [PMID:42871648](https://pubmed.ncbi.nlm.nih.gov/42871648/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 6 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 2 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0012864` (1 mention) - the report calls it "? verify"; HP calls it **Abnormal sperm morphology**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.