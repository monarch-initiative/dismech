---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-14T13:26:13.871309'
end_time: '2026-10-14T13:28:53.164358'
duration_seconds: 159.29
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: PLACK Syndrome
  mondo_id: MONDO:0014574
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
  - claude-opus-5-5
  web_search_requests: 4
  num_turns: 28
  total_cost_usd: 2.1813881000000004
  session_id: b91a5aba-3c6e-40af-be20-a442876bbd9b
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 10
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 18
  quotes_valid: 18
  quotes_not_checkable: 1
  relevance_assessed: 21
  on_topic: 14
  validator_version: 0.3.0
term_validation:
  total_terms: 31
  verified: 31
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
- **Disease Name:** PLACK Syndrome
- **MONDO ID:** MONDO:0014574 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PLACK Syndrome** covering all of the
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

I'm reading the cached PLACK reference abstracts in the repo; after that I'll fill gaps with a web search and write the report.

I'm checking a few ontology IDs against the repository's term caches, then I'll write the report.

# PLACK Syndrome (MONDO:0014574): Research Report

## How this was assembled and what it can support

- **Primary source:** 17 PubMed records already cached in this worktree's `references_cache/`, plus targeted web searches.
- **Usable quotes:** Every quotation below is copied exactly from a cached abstract or from cached PMC full text. Only those can serve as `snippet:` values.
- **Records with no content:** Seven cached records have no abstract text:
  - PMID:28851602
  - PMID:30656735
  - PMID:32918489
  - PMID:37140444
  - PMID:37317743
  - PMID:37387535
  - PMID:39931923 (has only a one-sentence abstract)

  What this report says about these papers comes from their titles, their MeSH headings, or other papers describing them. They cannot carry quoted evidence until full text is obtained.
- **Ontology IDs:** IDs marked ✔ were read from `cache/<prefix>/terms.csv` in this repo. IDs marked ⚠ are suggestions that have not been looked up yet and must be checked before binding.
- **No deep-research report exists** under `research/` for this disease.

---

## 1. Disease information

**What it is.** PLACK syndrome is an ultra-rare autosomal recessive genodermatosis (an inherited skin disorder). It is a form of generalized peeling skin syndrome caused by biallelic loss-of-function variants in *CAST*, which encodes calpastatin, the cell's own specific inhibitor of calpain. The acronym lists its five defining features:

- **P**eeling skin
- **L**eukonychia (white nails)
- **A**cral punctate keratoses (small hard spots on the hands and feet)
- **C**heilitis (inflamed lips)
- **K**nuckle pads

Since 2023, childhood-onset dilated cardiomyopathy (DCM) has emerged as a serious systemic manifestation.

> "loss-of-function mutations in calpastatin (CAST) are the genetic causes of an autosomal-recessive condition characterized by generalized peeling skin, leukonychia, acral punctate keratoses, cheilitis, and knuckle pads, which we propose to be given the acronym PLACK syndrome." (PMID:25683118, Lin et al., *Am J Hum Genet* 2015)

> "PLACK syndrome (OMIM 616295) is a form of generalized peeling skin syndrome (GPSS; OMIM 270300)." (PMID:33010050)

| Identifier | Value | Status |
|---|---|---|
| MONDO | MONDO:0014574, "peeling skin-leukonuchia-acral punctate keratoses-cheilitis-knuckle pads syndrome" (MONDO's own spelling, "leukonuchia") | ✔ (stub and draft entry) |
| OMIM (phenotype) | 616295 | ✔ (quoted in PMID:31392520, 33010050, 38994911, 40387456) |
| OMIM (gene) | *CAST* 114090, chromosome 5q15 | from the OMIM search snippet; ⚠ confirm |
| Orphanet | not confirmed; orpha.net was blocked and the local ORPHA cache has no match | ⚠ |
| ICD-10 / ICD-11 / MeSH | no disease-specific code; MeSH indexes these papers under "Skin Diseases, Genetic" and "Dermatitis, Exfoliative" | — |

**Synonyms:**
- PLACK syndrome
- Peeling skin, leukonychia, acral punctate keratoses, cheilitis, and knuckle pads
- Generalized peeling skin syndrome, CAST-related
- "PLACK-C" has been proposed if cardiomyopathy is confirmed as a consistent feature (PMID:41300744)

**Data basis.** All evidence is aggregated case reports and small families. There are no registries or EHR cohorts.

---

## 2. Etiology

- **Cause:** biallelic germline loss-of-function variants in *CAST* (hgnc:1515 ✔). Every reported variant is truncating: nonsense, frameshift, splice-site, or a large deletion.
  > "Previously reported variants in CAST associated with PLACK syndrome have been truncating in nature (frameshift, splice-site, and nonsense mutations)." (PMID:41300744, full text)
- **Risk factor: consanguinity.** Most families are consanguineous (PMID:28851602 MeSH "Consanguinity"; PMID:33410500; PMID:41300744; PMID:42256365).
- **Environmental, protective, or gene–environment factors:** none documented.
- **Possible nutritional link.** Low vitamin A and essential fatty acids were reported in one patient (PMID:33410500), and severe protein-calorie malnutrition in another (PMID:42742298). Whether these are consequences of the disease or coincidental is unresolved.

---

## 3. Phenotypes

The phenotype is called "remarkably homogeneous" (PMID:30656735, title only). The table counts reported cases:
- 19 cases in 12 articles as of the 2025 review (PMID:40387456)
- 21 cases (PMID:41300744)
- 27 patients, including 7 with DCM (PMID:42256365)

Frequency estimates are qualitative because no curated per-feature table was accessible.

| Phenotype | HPO | Frequency | Onset and course | Key evidence |
|---|---|---|---|---|
| Generalized peeling skin (exfoliation) | HP:0025819 *Palmoplantar peeling* ✔ covers only the acral part; ⚠ look up a generalized exfoliation term | Defining (essentially all) | Infancy; chronic | PMID:25683118 |
| Leukonychia | HP:0001820 ✔ | Defining | Congenital or infancy | PMID:25683118, 42256365 ("Fingernails and toenails showed leukonychia") |
| Acral punctate keratoses | HP:0007530 *Punctate palmoplantar hyperkeratosis* ✔ | Defining | Childhood; progressive | PMID:25683118, 42256365 ("multiple hyperkeratotic papules on palms and soles") |
| Cheilitis, including angular | HP:0100825 ✔ / HP:0030318 ✔ | Defining | Childhood | PMID:25683118, 42256365 |
| Knuckle pads | HP:0032541 *Knuckle pad* ✔ | Defining but may appear later | Childhood | PMID:25683118 |
| Pruritus | HP:0000989 ✔ | Common | Chronic | PMID:33410500 ("pruritis disappeared" with treatment) |
| Follicular hyperkeratosis / xerosis | HP:0007502 ✔ | Reported | — | PMID:42256365 |
| Skin hypopigmentation | HP:0001010 ✔ | Reported (MeSH "Hypopigmentation") | — | PMID:28851602, 32918489, 33410500 |
| Blistering | HP:0008066 ✔ | Occasional; the first 1986 family was misdiagnosed as epidermolysis bullosa simplex | — | PMID:33410500 (MeSH "Blister") |
| Oral leukokeratosis | HP:0002745 *Oral leukoplakia* ✔ (approximate) | OMIM synopsis | — | OMIM (web) |
| Striate palmar hyperkeratosis | ⚠ | Rare | — | PMID:38994911 |
| Silver hair, cutaneous warts | HP:0002218 ✔, HP:0200043 ✔ | Rare | — | PMID:41300744 |
| Alopecia areata | ⚠ | Single case; likely coincidental | — | PMID:37317743 (title) |
| Mild cerebral atrophy, mild muscle involvement | HP:0002059 ✔ | Single case | — | PMID:31392520 |
| **Dilated cardiomyopathy** | HP:0001644 ✔ | About 7/27 (~26%) in the 2026 tally; age-dependent | Onset 4–15 years; rapidly progressive to heart failure | PMID:38994911, 41300744, 42256365 |
| Sudden cardiac death in family members | HP:0001645 ✔ | Multiple families | Childhood | PMID:41300744, 42256365 |

Evidence for the cardiac phenotype:

> "Four developed severe DCM, two of whom required orthotopic heart transplantation." (PMID:41300744)

> "To date, there are 27 patients with PLACK syndrome reported, including ours, with 7 patients developed DCM. Among these, 3 had heart transplantation, 1 required a biventricular assist device, and 3 succumbed to progressive heart failure. The reported age of onset of DCM ranged from 4 to 15 years." (PMID:42256365)

**Quality of life.** No formal quality-of-life measures (EQ-5D, DLQI) have been published. The burden described is chronic pruritus, cosmetic impact, and, where present, life-threatening heart failure.

**Inheritance term:** HP:0000007 Autosomal recessive inheritance ✔.

---

## 4. Genetic and molecular information

- **Gene:** *CAST*, calpastatin. hgnc:1515 ✔; OMIM 114090 ⚠; 5q15.
- **Variant spectrum:** all predicted loss-of-function and germline. Most are homozygous; one compound heterozygote is reported.

| Variant | Type | Families or ancestry | PMID |
|---|---|---|---|
| c.607dup p.(Ile203Asnfs\*8); c.424A>T p.(Lys142\*); c.1750delG p.(Val584Trpfs\*37) | frameshift / nonsense | 3 families of different ethnicities (founding paper) | 25683118 |
| c.544G>T p.(Glu182\*) | nonsense | Turkish boy and his aunt | 31392520 |
| c.571G>T p.(Gly191\*) | nonsense; **the only recurrent variant** | 2 patients | 40387456 |
| c.1209+2T>G (NM_001042440.5) | splice; +1 nt frameshift, then nonsense-mediated decay (NMD) | Iranian boy | 37221445 |
| c.1177dup p.(Arg393Profs\*4) (NM_001750.7) | frameshift | Saudi extended family, 5 affected, 4 with DCM | 41300744 |
| c.1054dup | frameshift | Saudi girl with DCM | 42256365 |
| c.1882C>T p.(Gln628\*) | nonsense | Turkish sibship with DCM and sudden deaths (Durmaz 2023, as described in 41300744) | 37387535 (no abstract) |
| Nonsense variant + 326.7 kb deletion chr5:96037538_96364237 (also removes *ERAP2* and *LNPEP*) | compound heterozygous | 15-year-old with DCM | cited in 41300744 (likely 38994911; ⚠ confirm) |
| Novel insertion variants | insertion | French; Afghan; Indian (exon 18) | 28851602, 32918489, 37317743 |
| Novel homozygous variants | — | Irish; Saudi; Chinese; Indian | 33010050, 33410500, 37140444, 39931923 |

Functional evidence for loss of function:

> "Real-time qRT-PCR and immunoblot analysis showed reduced calpastatin expression in skin fibroblasts derived from both affected individuals compared to heterozygous family members. In vitro calpastatin activity assays also showed decreased activity in affected individuals." (PMID:31392520)

- **Functional impact category:** LOSS_OF_FUNCTION. NMD is shown for the splice allele in PMID:37221445.
- **Population frequency:** no carrier-frequency data. gnomAD values were not checked here.
- **ClinVar / ClinGen:** no ClinGen gene–disease validity record was found in the local cache.
- **Genotype–phenotype:** no correlation for cardiac involvement.
  > "no distinct variant hotspots for cardiomyopathy can been identified" (PMID:41300744, full text)
- **Modifier or confounding genes.** One child with PLACK and DCM also carried a heterozygous *MYBPC3* variant (hgnc:7551 ✔) that the authors judged sufficient to explain the cardiomyopathy (PMID:42742298). This caveat matters when counting DCM in PLACK.
  > "Although the patient's cardiomyopathy is attributable to her MYBPC3 variant, this case adds to the growing list of reports describing PLACK syndrome with coinciding cardiomyopathy" (PMID:42742298)
- **Epigenetic or chromosomal findings:** none apart from the 326.7 kb deletion above.

---

## 5. Environmental information

No environmental, lifestyle, or infectious triggers have been described.

---

## 6. Mechanism and pathophysiology

### Causal chain

1. Biallelic truncating *CAST* variants lead to NMD or truncated protein, which **results in loss of calpastatin protein and inhibitory activity**. This is demonstrated by IHC (PMID:25683118), immunoblot and activity assays (PMID:31392520), and mRNA analysis (PMID:37221445).
2. Loss of calpastatin **leads to unopposed calpain (CAPN1/CAPN2) protease activity**. This is *inferred* from calpastatin's known biochemistry. Calpain activity has not been measured directly in patient tissue in the available abstracts.
3. Excess calpain proteolysis in the epidermis **results in impaired keratinocyte cell–cell adhesion**. The siRNA knockdown result is demonstrated; the identity of the cleaved substrates is not.
   > "Transmission electron microscopy revealed widening of intercellular spaces with chromatin condensation and margination in the upper stratum spinosum in lesional skin, suggesting impaired intercellular adhesion as well as keratinocyte apoptosis." (PMID:25683118)
   > "In vitro studies utilizing siRNA-mediated CAST knockdown revealed a role for calpastatin in keratinocyte adhesion." (PMID:25683118)
4. **Branch: keratinocyte apoptosis increases** in the upper stratum spinosum (demonstrated by TUNEL).
   > "A significant increase of apoptotic keratinocytes was also observed in TUNEL assays." (PMID:25683118)
5. Steps 3 and 4 together **lead to defective epidermal adhesion and barrier**, which manifests as generalized peeling, cheilitis, and pruritus. Repeated friction at acral sites and knuckles produces punctate keratoses and knuckle pads; nail-matrix involvement produces leukonychia. The site-specific step is *inferred*.
   > "we describe PLACK syndrome, as a clinical entity of defective epidermal adhesion, caused by loss-of-function mutations in CAST." (PMID:25683118)
6. **Cardiac branch (hypothesis).** Unopposed calpain activity in cardiomyocytes is proposed to degrade cytoskeletal and sarcomeric proteins such as desmin and titin, causing myocardial fibrosis and impaired contractility, and then DCM. Support comes from mouse calpain-overexpression models and from explant histology (hypertrophied cardiomyocytes, fibrosis, bizarre nuclei). It has **not** been shown in patient myocardium.
   > "Excessive calpain activity may also lead to the degradation of key cytoskeletal proteins such as desmin and titin in myocardial fibers, leading to myocardial fibrosis and impaired contractility." (PMID:42256365)
   > "Histopathological examination of the explanted heart demonstrated hypertrophied cardiomyocytes with nuclear enlargement, hyperchromasia, and fibrosis." (PMID:41300744)
7. **Possible secondary metabolic step (unproven).** Low vitamin A and essential fatty acids were found in one patient (PMID:33410500). Whether this is a consequence of barrier failure or a contributor is unknown.

### Suggested terms

**Cell types (CL):**
- keratinocyte CL:0000312 ✔
- skin fibroblast CL:0002620 ✔ (the cell type used in functional assays)
- cardiac muscle cell CL:0000746 ✔
- ventricular cardiac muscle cell CL:2000046 ✔

**Biological processes (GO):**
- apoptotic process GO:0006915 ✔ (modifier INCREASED)
- calcium-dependent cell-cell adhesion GO:0016339 ✔ or desmosome organization GO:0002934 ✔. Desmosomal involvement is *suggested* by the TEM findings but not demonstrated.
- keratinocyte differentiation GO:0030216 ✔
- Calpain inhibition: ⚠ search for a calpain-inhibitor-activity molecular function term and a "negative regulation of cysteine-type endopeptidase activity" process term.

**Anatomy (UBERON, ⚠ to look up):** epidermis, stratum spinosum, nail, lip, palm, sole, knuckle skin, heart left ventricle.

### Molecular profiling

No transcriptomic, proteomic, single-cell, or multi-omic data have been published for PLACK.

---

## 7. Anatomical structures affected

| Level | Structures |
|---|---|
| Primary organ | Skin and its appendages: epidermis (especially the upper stratum spinosum), nails, lips/oral mucosa, palms and soles, knuckles |
| Secondary organ | Heart: left ventricle, with atrial fibrosis in one explant (PMID:42256365) |
| Possible | Central nervous system and muscle (single case, PMID:31392520) |
| Subcellular | Cytosol (calpastatin and calpain), cell–cell junctions, nucleus (chromatin condensation in apoptosis) |
| Lateralization | Bilateral and symmetric |

---

## 8. Temporal development

- **Onset:** skin features appear in the first months of life ("since the first six months of life", PMID:41300744, full text). Some cases present at school age.
- **Course:** the skin disease is chronic and lifelong. The oldest reported patients were 54 and 58 years old and had no cardiac disease (PMID:25683118, as described in PMID:41300744).
- **Cardiac disease:** onset at 4–15 years and rapidly progressive. The 2025 family study suggests penetrance is age-dependent:
  > "Given the possibility of age-dependent penetrance, lifelong cardiac surveillance is for the affected individuals suggested." (PMID:41300744)
- **Remission:** none spontaneous. One case of treatment-induced improvement is described in Section 12.

---

## 9. Inheritance and population

- **Inheritance:** autosomal recessive, with complete penetrance for the skin phenotype. Heterozygous parents are unaffected (PMID:41300744).
- **Prevalence:** unknown. About 27 published patients by 2026. A suitable `prevalence_class` would be `CASES_IN_LITERATURE` / `ULTRA_RARE`.
- **Founder effects:** none established. The only recurrent variant is p.Gly191\* (PMID:40387456). There is a geographic cluster of DCM-associated families in Saudi Arabia.
- **Ancestries reported:** Chinese and others (founding families), French, Israeli, Turkish, Afghan, Irish, Saudi, Iranian, Indian, Canadian, and US.
- **Sex ratio:** both sexes are affected equally.
- **Anticipation and germline mosaicism:** not reported.

---

## 10. Diagnostics

- **Clinical recognition:** the pentad of features, plus consanguinity.
- **Histology:** epidermal acantholysis-like widening of intercellular spaces and apoptotic keratinocytes in the upper spinous layer. Calpastatin immunostaining is reduced:
  > "Immunohistochemistry shows that staining of calpastatin is reduced in skin from affected individuals." (PMID:25683118)
- **Genetic testing:** whole-exome or whole-genome sequencing is the usual route (PMID:31392520, 37221445, 41300744). The title of PMID:32918489 ("the penny dropped") reflects diagnosis by exome sequencing in an Afghan child. RNA studies help confirm splice and novel variants (PMID:33410500, 37221445). Chromosomal microarray or copy-number analysis should be considered because of the 326.7 kb deletion case.
- **Cardiac work-up:** echocardiography at diagnosis and throughout life (PMID:41300744).
- **Labs:** vitamin A and essential fatty acid levels, which were low in PMID:33410500.
- **Differential diagnosis:**
  - Other generalized peeling skin syndromes (*CDSN*, *FLG2*, *SERPINB8*, *CSTA*, *TGM5*)
  - Epidermolysis bullosa simplex
  - Pachyonychia congenita
  - Naxos and Carvajal syndromes (palmoplantar keratoderma with cardiomyopathy, distinguished by woolly hair, HP:0002224 ✔)
  - Vitamin A or zinc deficiency
  > "Naxos and Carvajal syndromes are characterized by woolly hair, palmoplantar keratoderma, and right arrhythmogenic cardiomyopathy or left dilated cardiomyopathy, respectively. Woolly hair was not seen in our patient. Leukonychia is not a feature of vitamin A nor zinc deficiencies." (PMID:42256365)
- **Screening:** carrier testing and cascade testing within families. There is no newborn screening.

---

## 11. Outcome and prognosis

- **Skin:** not life-limiting; chronic morbidity.
- **Heart:** the main determinant of mortality. Of 7 patients with DCM: 3 died, 3 received transplants, and 1 needed a biventricular assist device (PMID:42256365). Families also report sudden cardiac deaths between ages 2 and 14.
- **After transplant:** short-term outcome is favourable (alive and stable at 5 months and 1 year, PMID:41300744).
- **Prognostic factors:** none identified. There is no genotype–phenotype correlation.

---

## 12. Treatment

| Treatment | Evidence | NCIT suggestion |
|---|---|---|
| Emollients and keratolytics (symptomatic) | Standard of care (PMID:42256365) | NCIT:C15747 Supportive Care (listed in CLAUDE.md; ⚠ verify) |
| IV lipid emulsion plus fat-soluble vitamins (Vitalipid® + Lipofundin MCT/LCT 20%), monthly | Single case with dramatic response | NCIT:C15986 Pharmacotherapy (⚠ verify), or NCIT:C15433 Nutritional Support (⚠; do not assign BEHAVIORAL modality); `therapeutic_agent` ⚠ look up a soybean-oil / lipid emulsion term in CHEBI or NCIT |
| Orthotopic heart transplantation for DCM | 3 patients; good short-term outcome | NCIT:C15289 Organ Transplantation (⚠ verify; modality SURGERY) |
| Heart-failure pharmacotherapy and mechanical support | 1 biventricular assist device | — |

> "There is no established treatment for PLACK syndrome... we initiated this patient on intravenous lipid infusion (Vitalipid®; an emulsion of fat-soluble vitamins and lipofundin-MCT/LCT 20%) and the response was dramatic. Following the fourth monthly course of treatment, pruritis disappeared and the skin lesions showed remarkable objective improvement." (PMID:33410500)

**Not available:**
- Clinical trials: none (no NCT or ICTRP records found)
- Gene therapy, RNA-based, or targeted therapy: none
- Calpain inhibitors: a mechanistically logical idea, but untested in PLACK

---

## 13. Prevention

- **Primary:** genetic counselling for consanguineous families; carrier testing; prenatal or preimplantation diagnosis once the familial variants are known.
- **Secondary:** early molecular diagnosis in children with peeling skin and leukonychia.
- **Tertiary:** lifelong echocardiographic surveillance (PMID:41300744, 42256365); monitoring nutritional status and vitamin A (PMID:33410500, 42742298).

---

## 14. Other species and natural disease

- No naturally occurring CAST-deficiency skin disease has been found in animals. OMIA was not searched in depth.
- Bovine and ovine *CAST* polymorphisms are well known in meat science, where they affect post-mortem calpain-driven tenderization. They have no reported skin phenotype.
- Calpastatin is conserved across vertebrates.

---

## 15. Model organisms

- **Cast knockout mouse:** "essentially normal in terms of their reproduction, development, growth, anatomy, and cognition", with a modest abnormality in affective behaviour ([PMC2561015](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2561015/)). No skin phenotype has been reported. This is a candidate `FAILS_TO_RECAPITULATE` / `HUMAN_MODEL_MISMATCH` point, pending a published skin examination.
- **Calpastatin-overexpressing mouse:** delayed wound re-epithelialization ([PMC3353912](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3353912/)). This is the inverse genotype and is only indirectly informative.
- **Cardiac models:**
  - Mitochondria-targeted Capn1 transgenic and Tg-Capn2 mice develop DCM and fibrosis (cited in PMID:41300744). These support the calpain-excess cardiac hypothesis.
  - Calpastatin-transgenic hearts show sarcomeric disruption and autophagic vacuoles (cited in PMID:41300744).
- **In vitro systems:**
  - siRNA *CAST* knockdown in keratinocytes reduces adhesion (PMID:25683118). Evidence type: IN_VITRO.
  - Patient skin fibroblasts show reduced calpastatin expression and activity (PMID:31392520).
- **Not available:** iPSC, organoid, or zebrafish models specific to PLACK.

---

## Notes for the KB entry

- The stub is `stubs/Peeling_Skin-leukonuchia-acral_Punctate_Keratoses-cheilitis-knuckle_Pads_Syndrome.yaml`. The curation PR should delete it.
- Missing identifiers to fill in: the Orphanet code and the OMIM gene ID, ideally via `just fetch-reference ORPHA:…` once identified.
- Seven cached references have no abstract text. Fetch full text, or cite them only for non-snippet context.
- When counting cardiomyopathy as a PLACK feature, handle PMID:42742298 carefully, since that child's DCM is attributed to *MYBPC3*. The cardiac node is best modelled as an emerging hypothesis (a `mechanistic_hypotheses` entry with `status: EMERGING`). The mouse cardiac models fit a `HUMAN_MODEL_MISMATCH` or `KNOWLEDGE_GAP` discussion.

Sources:
- [PMC12652073 – Severe DCM with PLACK syndrome (Alkorashy 2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12652073)
- [PubMed 41300744](https://pubmed.ncbi.nlm.nih.gov/41300744/)
- [PubMed 38994911 – CASTing the net wider](https://pubmed.ncbi.nlm.nih.gov/38994911/)
- [PubMed 40387456 – Updated review (Haxho 2025)](https://pubmed.ncbi.nlm.nih.gov/40387456/)
- [Wiley – Haxho 2025 full text](https://onlinelibrary.wiley.com/doi/full/10.1111/pde.15987)
- [Hacettepe record – Durmaz 2023](https://avesis.hacettepe.edu.tr/yayin/e5757b3e-0e4b-42ed-b71d-808473c135f8/novel-nonsense-cast-mutation-in-two-siblings-with-plack-syndrome)
- [OMIM 616295 (mirror)](https://0-www-ncbi-nlm-nih-gov.brum.beds.ac.uk/omim/616295)
- [Comprehensive behavioral phenotyping of calpastatin-knockout mice](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2561015/)
- [Calpain activity is essential in skin wound healing](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3353912/)
- [Temel 2019 PDF](https://www.uludag.edu.tr/dosyalar/genetik/resim/10.1007_s00441-019-03077-9.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 18 |
| Quoted claims found in source | 18 |
| Quoted claims **not** found in source | 0 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 21 |
| On topic | 14 |
| Off topic | 0 |

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMID:30656735`: "remarkably homogeneous"
  - Reference resolved but exposes no abstract or full text to search

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.