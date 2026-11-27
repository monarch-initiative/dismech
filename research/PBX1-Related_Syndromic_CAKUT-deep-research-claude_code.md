---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-25T15:17:56.246500'
end_time: '2026-11-25T15:23:22.290626'
duration_seconds: 326.04
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: PBX1-Related Syndromic CAKUT
  mondo_id: MONDO:0060549
  category: Mendelian
  causal_genes: PBX1
  omim_id: OMIM:617641
  synonyms: not recorded
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
  web_search_requests: 3
  num_turns: 10
  total_cost_usd: 0.80110982
  session_id: 6923e767-f2a1-46ce-957e-f82582653b72
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 36
  retrieval_calls: 34
  assistant_text_blocks: 2
citation_count: 25
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 16
  quotes_valid: 15
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:28270404
  relevance_assessed: 21
  on_topic: 18
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 57
  verified: 33
  not_found: 0
  obsolete: 0
  unverifiable: 24
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 7
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0060549
    reported_labels:
    - MONDO
    ontology_label: congenital anomalies of kidney and urinary tract syndrome with
      or without hearing loss, abnormal ears, or developmental delay
  - term_id: DOID:0112359
    reported_labels:
    - Disease Ontology
    ontology_label: congenital anomalies of kidney and urinary tract syndrome with
      or without hearing loss, abnormal ears, or developmental delay
  labels_variant: 3
  unresolvable_prefixes:
  - OMIM
  - MGI
  service_unreachable: 21
  obsolescence_unchecked: 10
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PBX1-Related Syndromic CAKUT
- **MONDO ID:** MONDO:0060549 (if available)
- **Causal gene(s):** PBX1
- **OMIM:** OMIM:617641
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **PBX1-Related Syndromic CAKUT** covering all of the
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

Status: I've confirmed the core PBX1 papers and mouse models, and I'm now pulling verified abstracts through Europe PMC to fill in the clinical cohort details.

# PBX1-Related Syndromic CAKUT (CAKUTHED): Disease Characteristics Report

**How this report was built.** It covers MONDO:0060549 / OMIM:617641, the disorder caused by heterozygous loss-of-function variants or deletions of the **PBX1** gene (PBX homeobox 1, chromosome 1q23.3). It does not cover other CAKUT genes or other diseases with similar names. Bash and direct PubMed access were blocked in this session. The evidence comes from web searches and from Europe PMC and PMC abstract records fetched for this report. Quotes are verbatim but shortened to fragments of under about 125 characters because of copyright limits on the source pages. Any item marked **[unverified]** was not retrieved in this session and must be checked before use.

---

## 1. Disease Information

**Overview.** CAKUTHED is short for "congenital anomalies of kidney and urinary tract syndrome with or without hearing loss, abnormal ears, or developmental delay". It is an autosomal dominant, highly pleiotropic developmental disorder caused by heterozygous PBX1 variants. MedGen describes it as having "variable kidney and urinary tract anomalies, sometimes leading to renal dysfunction, dysmorphic facial features, and outer ear abnormalities, often with hearing loss," with global developmental delay in most patients ([MedGen C4539968 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/a3492137cada35c1427e5783c176e4344e6cbb56/www.ncbi.nlm.nih.gov/medgen/C4539968/index.html)). Disease Ontology defines it as caused by heterozygous PBX1 mutation or by deletion of a genomic region that includes PBX1 ([DOID:0112359](https://disease-ontology.org/term/DOID:0112359)).

**Identifiers**

| Resource | ID | Status |
|---|---|---|
| MONDO | MONDO:0060549 | retrieved |
| OMIM | 617641 (phenotype) | retrieved |
| UMLS / MedGen | C4539968 | retrieved |
| Disease Ontology | DOID:0112359 | retrieved |
| KEGG Disease | H01867 (CAKUT, parent group) | retrieved ([KEGG](https://www.kegg.jp/entry/H01867)) |
| LOVD | disease 06021 | retrieved ([LOVD](https://databases.lovd.nl/shared/diseases/06021)) |
| Orphanet, ICD-11, MeSH | — | not retrieved; no disease-specific code confirmed. ICD-10 Q60–Q64 (congenital malformations of the urinary system) would apply only generically. |

**Synonyms.** CAKUTHED; PBX1-related syndrome ([Arts 2020, PMID 32141698](https://pubmed.ncbi.nlm.nih.gov/32141698/)); "PBX1 haploinsufficiency syndromic CAKUT" ([Le Tanno 2017, PMID 28270404](https://pubmed.ncbi.nlm.nih.gov/28270404/)).

**Source of the information.** Everything here is aggregated from published case reports and case series (human clinical evidence) and from disease-level curation (OMIM, MedGen, DO). No EHR or registry data were found.

---

## 2. Etiology

**Causal factors (genetic).** The disorder is caused by monoallelic (heterozygous) loss of PBX1 function through any of these routes:

- **Microdeletions of 1q23.3q24.1.** Le Tanno et al. studied eight patients and defined "a 276-kb minimal common region (MCR) that only overlaps with the PBX1 gene" (PMID 28270404).
- **De novo truncating or missense variants.** Heidet et al. reported "five de novo heterozygous loss of function mutations/deletions in the PBX homeobox 1 gene (PBX1)" ([PMID 28566479](https://pubmed.ncbi.nlm.nih.gov/28566479/)). Slavotinek et al. reported eight patients with de novo deleterious variants ([PMID 29036646](https://pubmed.ncbi.nlm.nih.gov/29036646/)).

**Genetic risk factors**

- **Parental mosaicism.** This matters for recurrence risk:
  - Arts et al. found a father mosaic for p.(Arg107Trp) at VAF "in blood (10%) and sperm (20%)," with two affected children (PMID 32141698).
  - Huang et al. found "a paternal mosaic PBX1 variant in blood at 11.54%" ([PMID 39189629](https://pubmed.ncbi.nlm.nih.gov/39189629/)).
- **Familial transmission is rare.** A paternally inherited 1q23.3 deletion that includes PBX1 was reported by Luo 2022 (PMID 36544198; title-level record only). A Chinese family with renal hypoplasia was reported by Chen 2026 (PMID 43075297; title only).

**Environmental risk factors, protective factors, gene–environment interactions.** None were found. No environmental, protective-allele, or GxE data exist for this disease. The template's sources (CTD, GWAS Catalog, PheGenI) were not searched because Bash was blocked. Since this is a monogenic disorder caused mostly by de novo variants, none would be expected.

---

## 3. Phenotypes

**Cohort-level frequency data**

- Le Tanno: bilateral renal hypoplasia in 75% (6/8) of deletion carriers (PMID 28270404).
- Petzold et al. reviewed the literature (HGMD 2021.4) and found 31 CAKUTHED patients. Extrarenal features were present in 27/31 (87%) and mosaicism in 2/31 ([PMID 35756743](https://pmc.ncbi.nlm.nih.gov/articles/PMC9217644)).
- Slavotinek: "All patients but one had developmental delays" (7/8). Clinical findings "were observed in all patients with varying expressivity and severity" (PMID 29036646).

**Phenotype table.** All findings are congenital and non-progressive unless noted.

| Phenotype | Suggested HPO | Type / onset | Frequency / evidence |
|---|---|---|---|
| Renal hypoplasia (often bilateral) | HP:0000089 Renal hypoplasia | Structural sign; congenital, often prenatal | Most common (75% in deletion series; PMID 28270404) |
| Renal dysplasia | HP:0000110 | Congenital | Bilateral dysplastic kidneys (Riedhammer, [PMID 29226118](https://pubmed.ncbi.nlm.nih.gov/29226118/)) |
| Unilateral renal agenesis, horseshoe kidney | HP:0000122; HP:0000085 | Congenital | Case-level; horseshoe kidney in Scolari 2025 ([PMID 41300798](https://pubmed.ncbi.nlm.nih.gov/41300798/)) |
| Vesicoureteral reflux / urinary tract anomalies | HP:0000076 | Congenital | Part of the CAKUT spectrum (OMIM / MedGen); specific frequency not retrieved |
| Progressive CKD, proteinuria, FSGS | HP:0012622; HP:0000093; HP:0000097 | Lab/clinical; childhood to adult; progressive | Adult case with rising creatinine and proteinuria ([Han 2025, PMID 41255624](https://pubmed.ncbi.nlm.nih.gov/41255624/)) |
| Oligohydramnios | HP:0001562 | Prenatal | Prenatal cases (Sun 2019, PMID 30910156 **[unverified link]**) |
| Cryptorchidism | HP:0000028 | Congenital | Common; truncating variants are linked to "mostly cryptorchidism and deafness" ([Zou 2023, PMID 37006624](https://pubmed.ncbi.nlm.nih.gov/37006624/)) |
| Ambiguous genitalia; 46,XY DSD / sex reversal | HP:0000062; HP:0000032 (abnormality of male external genitalia) | Congenital | Slavotinek (PMID 29036646); Arts "complete sex reversal (46,XY female)" (PMID 32141698); Tsai 2026 ([PMID 41746858](https://pubmed.ncbi.nlm.nih.gov/41746858/)) |
| Hearing impairment | HP:0000365 | Congenital / childhood | Frequent (OMIM / MedGen; Zou 2023) |
| Outer ear abnormalities | HP:0000356 | Congenital | Frequent (MedGen) |
| Facial dysmorphism | HP:0001999 | Congenital | Frequent (MedGen) |
| Global developmental delay; intellectual disability | HP:0001263; HP:0001249 | Infancy / childhood; static | 7/8 (PMID 29036646) |
| Autism | HP:0000717 | Behavioral; childhood | LOVD single individual |
| Congenital heart defects (TOF, VSD) | HP:0001636; HP:0001629 | Congenital | TOF with p.R184P ([Alankarage 2020, PMID 31625560](https://pmc.ncbi.nlm.nih.gov/articles/PMC7206850)) |
| Hypoplastic clavicles; coracoclavicular ankylosis | HP:0000894 | Skeletal; congenital | PMID 29226118; Iwai 2026, three homeobox missense cases "who did not have CAKUT" ([PMID 41162587](https://pubmed.ncbi.nlm.nih.gov/41162587/)) |
| Respiratory failure | HP:0002878 | Neonatal | Iwai 2026 (PMID 41162587) |
| Diaphragmatic eventration; microsplenia | HP:0009110; — | Perinatal, lethal cases | Arts 2020 (PMID 32141698) |
| Congenital glaucoma; corneal clouding | HP:0001087; HP:0007957 | Infancy | Safgren 2022 ([PMID 34797033](https://pubmed.ncbi.nlm.nih.gov/34797033/)) |
| Intrauterine growth retardation | HP:0001511 | Prenatal | Sun 2019 **[unverified link]** |

**Severity.** Variable, ranging from perinatal lethality (recurrent neonatal death; PMIDs 32141698 and 39189629) to mild renal hypoplasia recognized only in adulthood (PMIDs 35756743 and 41255624).

**Quality of life.** No QoL instrument data (EQ-5D, SF-36) were found. The main expected burdens are CKD/ESKD, developmental disability, and hearing loss; this is inferred, not measured.

---

## 4. Genetic / Molecular Information

**Gene.** *PBX1*, PBX homeobox 1, at 1q23.3. Gene MIM 176310, HGNC:8632, and NCBI Gene 5087 are **[unverified]**. Reference transcript NM_002585 (used in PMIDs 39189629 and 41300798). PBX1 is a TALE ("three-amino acid loop extension") homeodomain transcription factor (PMID 37006624).

**Reported variants (all germline, heterozygous)**

| Variant | Type | Context | PMID |
|---|---|---|---|
| 1q23.3q24.1 deletions (276-kb MCR containing only PBX1) | CNV / deletion | 8 syndromic CAKUT patients | 28270404 |
| c.413_419del, p.Gly138Valfs*40 | Frameshift, de novo | Dysplastic kidneys, clavicles | 29226118 |
| c.400dupG, p.Ala134Glyfs*65 | Frameshift, de novo | Glaucoma, kidney anomalies, developmental delay | 34797033 |
| c.277C>T, p.Arg93Ter | Nonsense, de novo; "flagged as escaping nonsense-mediated decay" | Adult FSGS | 41255624 |
| c.992C>A, p.(Ser331*) | Nonsense, **somatic mosaic** (26% blood, 50% oral mucosa, 20% urinary cells) | Mild syndromic renal hypoplasia | 35756743 |
| p.(Arg107Trp) | Missense, paternal mosaic | Recurrent perinatal death, 46,XY sex reversal | 32141698 |
| c.551G>C, p.R184P | Missense, de novo | Tetralogy of Fallot | 31625560 |
| c.694G>C, p.D232H | Missense, paternal mosaic | Recurrent neonatal death | 39189629 |
| c.710G>C, p.R237T (nuclear localization sequence) | Missense | 46,XY DSD | 41746858 |
| c.712C>T, p.(Arg238Trp) | Missense, de novo | Horseshoe kidney | 41300798 |
| Homeobox C-terminal missense cluster | Missense, de novo | Coracoclavicular ankylosis, no CAKUT | 41162587 |

**Variant spectrum.** In the HGMD-based review of 31 patients there were 5 nonsense/frameshift/splice variants, 4 missense variants, and 22 indels/CNVs (PMID 35756743). Zou 2023 reported that truncating variants cause milder phenotypes (PMID 37006624).

**Evidence status for the remaining template items**

- **ACMG classification and allele frequency.** ClinVar and gnomAD were not queried in this session. All reported variants were absent from controls or de novo, as described in the source papers.
- **Functional consequence.** Mostly **loss of function / haploinsufficiency** (PMID 28270404). Missense variants act through two mechanisms:
  - reduced protein: "amounts of PBX1 protein are significantly decreased" (p.R184P; PMID 31625560);
  - impaired nuclear localization: p.R238W did "not affect protein expression" but variants increased "retention in the cytoplasm" (PMID 41300798), and p.R237T "reduced protein stability and hampered nuclear translocation" (PMID 41746858).
  - Slavotinek found "perturbation of intrinsic, PBX-dependent transactivation ability" (PMID 29036646).
  - The genotype–phenotype differences hint that some missense variants could act through dominant-negative or altered-function mechanisms, but this is not proven.
- **Modifier genes.** None reported.
- **Epigenetics.** No data.
- **Chromosomal abnormalities.** 1q23.3 microdeletions (PMIDs 28270404, 30910156 **[unverified]**, 36544198). In DECIPHER terms these are PBX1-containing CNVs. The DECIPHER database itself was not queried in this session.

---

## 5. Environmental Information

Not applicable. No environmental, lifestyle, or infectious contributors have been reported.

---

## 6. Mechanism / Pathophysiology

**Causal chain**

1. A heterozygous PBX1 deletion, truncating variant, or deleterious missense variant (germline de novo, inherited, or mosaic) **leads to** reduced functional PBX1 protein (haploinsufficiency). This is demonstrated in humans by deletions and truncating variants (PMID 28270404) and for missense variants in vitro (PMIDs 31625560, 41746858).
   - **Branch A:** a missense variant in the NLS or homeodomain **results in** cytoplasmic retention or reduced stability (in vitro; PMIDs 41300798, 41746858).
   - **Branch B:** a truncating variant **results in** NMD or a truncated protein (PMIDs 34797033, 41255624).
2. Reduced nuclear PBX1 **results in** impaired PBX-dependent transcriptional activation together with HOX and other partners (in vitro; PMID 29036646; review PMID 37006624).
3. Impaired PBX1/HOX transcriptional programs in metanephric mesenchyme/stroma **lead to** abnormal mesenchymal proliferation and signaling. This is inferred from the mouse model and review (PMIDs 12591246, 37006624).
4. Defective mesenchyme–ureteric bud crosstalk **results in** reduced ureteric branching and fewer nephrons. Pbx1⁻/⁻ mice show "decreased branching and elongation of the ureter" and "kidneys contained fewer nephrons" (mouse; PMID 12591246).
5. Reduced nephron endowment **leads to** renal hypoplasia or dysplasia, agenesis, or mispositioning (mouse, human; PMIDs 12591246, 28270404). From there the course branches:
   - Congenital low nephron mass **leads to** hyperfiltration, proteinuria, FSGS, and progressive CKD/ESKD. This is inferred, supported by an adult FSGS case (PMID 41255624).
   - Prenatally, it **leads to** oligohydramnios (case-level).
6. A parallel branch runs through urogenital ridge, adrenal, and gonad development. Loss of Pbx1 "markedly reduces urogenital ridge outgrowth," which **results in** absent adrenals and gonads with "rudimentary sexual differentiation" in mice (PMID 14595835). In humans this corresponds to cryptorchidism and 46,XY DSD (PMIDs 32141698, 41746858).
7. A further parallel branch runs through cardiac outflow tract, branchial arch/ear, skeletal (clavicle/scapula), and diaphragm/spleen development. These **lead to** CHD, ear anomalies and hearing loss, clavicular defects, and diaphragmatic eventration. Evidence: knock-in mouse VSDs (PMID 31625560) and human case reports. The ear and skeletal mechanism is inferred.
8. A neurodevelopmental branch **results in** DD/ID. The mechanism is not established.

**Detail**

- **Pathways.** HOX–PBX–MEIS TALE transcription factor complexes (review; PMID 37006624). Tsai 2026 found that targets including "MAP3K4, EMX2, KISS1R, and HOXA13" were dysregulated in p.R237T cells (PMID 41746858). Variant-expressing cells showed decreased proliferation.
- **Cellular processes.** In mice, cell proliferation was decreased in Pbx1⁻/⁻ genital ridges (PMID 14595835).
- **Suggested GO terms:** GO:0001822 kidney development; GO:0001658 branching involved in ureteric bud morphogenesis; GO:0072006 nephron development; GO:0008584 male gonad development; GO:0030325 adrenal gland development; GO:0006357 regulation of transcription by RNA polymerase II; GO:0008283 cell population proliferation.
- **Suggested CL terms:** metanephric mesenchyme / stromal cell (CL:1000692 kidney interstitial fibroblast **[verify]**); ureteric bud cell (CL:1000090 **[verify]**); Sertoli cell CL:0000216; adrenal cortical cell CL:0000417.
- **Not applicable or no data:** metabolic changes, immune involvement, omics profiling, single-cell studies.

---

## 7. Anatomical Structures Affected

- **Primary organs:** kidney (UBERON:0002113), ureter (UBERON:0000056), urinary bladder (UBERON:0001255).
- **Other organs and systems:** gonad/testis (UBERON:0000991 / UBERON:0000473), external genitalia (UBERON:0004176), external ear (UBERON:0001691), inner ear (UBERON:0001846), heart (UBERON:0000948), clavicle (UBERON:0001105), diaphragm (UBERON:0001103), spleen (UBERON:0002106), eye/anterior segment (glaucoma), brain (DD/ID), and adrenal (mouse only).
- **Subcellular:** nucleus (GO:0005634). Missense variants cause mislocalization to cytoplasm (GO:0005737) (PMIDs 41300798, 41746858).
- **Lateralization:** renal hypoplasia is mostly **bilateral** (75%; PMID 28270404). Unilateral agenesis occurs in mice (PMID 12591246).

---

## 8. Temporal Development

- **Onset:** congenital. Often detected **prenatally** through renal anomalies, oligohydramnios, or IUGR (PMID 28270404; Le Tanno recommends CMA "in cases of fetal renal anomalies").
- **Course:**
  - The structural anomalies are static.
  - Renal function may decline slowly, and ESKD in adulthood has been reported (PMID 41255624). Genomics England PanelApp lists PBX1 in its "Unexplained young onset end-stage renal disease" panel ([PanelApp](https://panelapp.genomicsengland.co.uk/panels/678/gene/PBX1/)).
  - Mild cases can present in adulthood (PMID 35756743, at age 20; PMID 41255624, at age 28).
- **Critical period:** embryonic organogenesis (nephrogenesis, gonadal differentiation).
- **Remission:** none expected.
- **Staging:** no disease-specific stages. CKD stages (KDIGO) apply.

---

## 9. Inheritance and Population

- **Inheritance:** autosomal dominant (OMIM; LOVD). Most cases are **de novo**; parental germline/somatic mosaicism is documented (PMIDs 32141698, 39189629).
- **Penetrance:** apparently high in heterozygotes, but mosaic carriers can be unaffected or mildly affected.
- **Expressivity:** markedly variable (PMID 29036646).
- **Not applicable:** anticipation, founder effects, consanguinity, carrier frequency.
- **Prevalence:** unknown. It is ultra-rare: 31 patients in the literature by 2021 (PMID 35756743). In a CAKUT cohort, Heidet found causal mutations in 36/204 (17.6%) patients overall, five of them in PBX1 (about 2.5% of the cohort) (PMID 28566479).
- **Demographics:** reported in European, Australian, US, Japanese, Chinese, and Korean patients. There is no ethnic predilection.
- **Sex ratio:** the genital phenotype is ascertained more readily in 46,XY individuals; there is no formal sex ratio.

---

## 10. Diagnostics

- **Imaging:** prenatal and postnatal renal ultrasound (hypoplasia, dysplasia, horseshoe kidney); VCUG for reflux; echocardiography; audiology.
- **Laboratory:** serum creatinine/eGFR, urine protein (PMID 41255624); karyotype and hormonal evaluation in DSD.
- **Genetic testing**
  - **Chromosomal microarray** for deletions. Le Tanno: "CMA should be recommended in cases of fetal renal anomalies" (PMID 28270404).
  - **Exome or genome sequencing**, ideally as a trio, for sequence variants (PMIDs 29226118, 32141698, 39189629).
  - **CAKUT gene panels:** PBX1 is included in the Genomics England and PanelApp Australia CAKUT panels ([PanelApp AUS](https://panelapp-aus.org/panels/63/gene/PBX1/); [GE PanelApp](https://panelapp.genomicsengland.co.uk/panels/234/gene/PBX1/)).
  - **Mosaicism testing:** consider testing multiple tissues and using deep sequencing. Petzold: "we suggest ruling out somatic mosaicism in sporadic CAKUT" (PMID 35756743).
  - Parental testing, including for low-level mosaicism, is essential for recurrence counseling.
- **Clinical criteria:** none established.
- **Differential diagnosis:** other syndromic CAKUT disorders, distinguished by genotype:
  - HNF1B-related disease (renal cysts, diabetes);
  - PAX2-related papillorenal syndrome (optic nerve coloboma);
  - EYA1/SIX1 branchio-oto-renal syndrome (branchial fistulae, hearing loss — the closest phenotypic overlap);
  - 22q11.2 deletion;
  - other DSD genes such as NR5A1 and WT1.

---

## 11. Outcome / Prognosis

- **Survival:** bimodal.
  - Perinatal lethality occurs in severe cases (recurrent neonatal death or stillbirth; PMIDs 32141698, 39189629). Prenatal series also included pregnancy terminations (PMID 39189629: "pregnancy termination at 17 weeks gestation").
  - Survival into adulthood occurs in milder cases.
- **Data gaps:** no survival statistics, life-expectancy data, or QoL measures were found.
- **Morbidity:** CKD progressing to ESKD; developmental and intellectual disability; hearing loss; DSD-related issues (gonadal dysgenesis, infertility, inferred).
- **Prognostic factors** (tentative):
  - severity of bilateral renal hypoplasia and presence of oligohydramnios;
  - truncating variants associated with milder phenotypes (PMID 37006624);
  - mosaicism with milder disease (PMID 35756743).

---

## 12. Treatment

No disease-specific, gene-targeted, or experimental therapies exist. No clinical trials were found; ClinicalTrials.gov was not directly searched. Management is supportive and follows CKD and CAKUT standards of care (inferred general practice, not PBX1-specific evidence):

- **CKD management:** RAAS blockade for proteinuria (NCIT: Angiotensin-Converting Enzyme Inhibitor; Angiotensin II Receptor Antagonist), anemia and mineral-bone management, growth support. Dialysis (NCIT: Dialysis) and kidney transplantation (NCIT: Kidney Transplantation) for ESKD.
- **Urology:** orchidopexy for cryptorchidism (NCIT: Orchiopexy), DSD multidisciplinary care, antibiotic prophylaxis for VUR when indicated.
- **Other:** cardiac surgery for CHD (e.g., TOF repair), hearing aids or cochlear implants, developmental, speech, physical, and occupational therapies, and glaucoma surgery (PMID 34797033).
- **Not applicable:** pharmacogenomics.

---

## 13. Prevention

- **Primary prevention:** not applicable.
- **Genetic counseling:**
  - De novo cases carry a low but non-zero recurrence risk because of parental gonadal mosaicism, which is documented twice (PMIDs 32141698, 39189629).
  - An affected individual has a 50% risk of transmission.
- **Prenatal and preimplantation options:**
  - CMA or exome sequencing for fetal renal anomalies (PMID 28270404).
  - Targeted prenatal or preimplantation testing once a familial or mosaic variant is known.
- **Tertiary prevention:** monitoring renal function and blood pressure, and screening for hearing loss, cardiac defects, and genital and eye anomalies.
- **Not applicable:** vaccination and public-health measures.

---

## 14. Other Species / Natural Disease

- **Naturally occurring disease:** no PBX1-related disease in animals was found. OMIA was not searched in this session.
- **Orthologs:** mouse *Pbx1* (MGI:97495 **[unverified]**) and zebrafish *pbx1a*/*pbx1b* **[unverified]**.
- **Conservation:** the mouse kidney, gonad, adrenal, and cardiac phenotypes parallel human disease (PMIDs 12591246, 14595835, 31625560). Slavotinek noted "Clinical findings similar to those in Pbx mutant mice" (PMID 29036646).
- **Zoonotic potential:** not applicable.

---

## 15. Model Organisms

| Model | Phenotype | Recapitulation | PMID |
|---|---|---|---|
| Pbx1⁻/⁻ mouse (constitutive KO; Mus musculus, NCBITaxon:10090) | Kidneys "reduced in size, axially mispositioned," with unilateral agenesis in severe cases; fewer nephrons; reduced ureteric branching | Good for renal hypoplasia and agenesis. Limitation: homozygous embryonic lethality, whereas the human disease is heterozygous. | 12591246 |
| Pbx1⁻/⁻ mouse (urogenital) | "complete lack of adrenal glands"; gonads with "rudimentary sexual differentiation"; reduced urogenital ridge outgrowth | Models DSD and cryptorchidism. Adrenal agenesis has not been reported in humans. | 14595835 |
| Pbx1 p.R184P knock-in mouse | Homozygotes not born alive; heterozygotes with 45% perinatal death and VSDs in 75% at E13.5 | Heterozygous model for CHD and perinatal lethality. "developmental anomalies in a proportion of heterozygous embryos." | 31625560 |
| Tet-inducible cell lines (p.R237T, p.R238W) | Cytoplasmic retention, reduced stability, decreased proliferation | In vitro functional validation | 41746858, 41300798 |
| Pbx1b expression mapping (mouse) | Expression during organogenesis | Developmental atlas | 11118899 (title-level) |

**Limitations:** human haploinsufficiency is not fully modeled by heterozygous null mice. In particular, heterozygous Pbx1⁺/⁻ renal phenotypes were not retrieved in this session. There are no iPSC or kidney-organoid models yet.

**Resources:** MGI, IMPC, and MMRRC were not queried in this session.

---

### Key Sources
- [Le Tanno et al. 2017, J Med Genet, PMID 28270404](https://pubmed.ncbi.nlm.nih.gov/28270404/) · [Heidet et al. 2017, JASN, PMID 28566479](https://pubmed.ncbi.nlm.nih.gov/28566479/) · [Slavotinek et al. 2017, Hum Mol Genet, PMID 29036646](https://pubmed.ncbi.nlm.nih.gov/29036646/)
- [Riedhammer 2017, PMID 29226118](https://pubmed.ncbi.nlm.nih.gov/29226118/) · [Alankarage 2020, PMID 31625560](https://pmc.ncbi.nlm.nih.gov/articles/PMC7206850) · [Arts 2020, PMID 32141698](https://pubmed.ncbi.nlm.nih.gov/32141698/) · [Safgren 2022, PMID 34797033](https://pubmed.ncbi.nlm.nih.gov/34797033/) · [Petzold 2022, PMID 35756743](https://pmc.ncbi.nlm.nih.gov/articles/PMC9217644)
- [Zou 2023 review, PMID 37006624](https://pubmed.ncbi.nlm.nih.gov/37006624/) · [Huang 2024, PMID 39189629](https://pubmed.ncbi.nlm.nih.gov/39189629/) · [Han 2025, PMID 41255624](https://pubmed.ncbi.nlm.nih.gov/41255624/) · [Scolari 2025, PMID 41300798](https://www.mdpi.com/2073-4425/16/11/1346) · [Iwai 2026, PMID 41162587](https://pubmed.ncbi.nlm.nih.gov/41162587/) · [Tsai 2026, PMID 41746858](https://pubmed.ncbi.nlm.nih.gov/41746858/)
- [Schnabel 2003 Dev Biol, PMID 12591246](https://pubmed.ncbi.nlm.nih.gov/12591246/) · [Schnabel 2003 Genesis, PMID 14595835](https://pubmed.ncbi.nlm.nih.gov/14595835/)
- [MGI OMIM:617641](https://informatics.jax.org/disease/OMIM:617641) · [MedGen C4539968](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/a3492137cada35c1427e5783c176e4344e6cbb56/www.ncbi.nlm.nih.gov/medgen/C4539968/index.html) · [DOID:0112359](https://disease-ontology.org/term/DOID:0112359) · [KEGG H01867](https://www.kegg.jp/entry/H01867) · [LOVD](https://databases.lovd.nl/shared/diseases/06021) · [PanelApp AUS](https://panelapp-aus.org/panels/63/gene/PBX1/) · [Genomics England PanelApp CAKUT](https://panelapp.genomicsengland.co.uk/panels/234/gene/PBX1/) · [Genomics England PanelApp young-onset ESRD](https://panelapp.genomicsengland.co.uk/panels/678/gene/PBX1/)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 16 |
| Quoted claims found in source | 15 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 21 |
| On topic | 18 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:28270404` *(abstract only)*: "PBX1 haploinsufficiency syndromic CAKUT"
  - Text part not found as substring: 'PBX1 haploinsufficiency syndromic CAKUT' (note: only abstract available for PMID:28270404, full text may contain this excerpt)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 57 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 24 |
| Terms whose name was checked | 12 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0060549` (2 mentions) - the report calls it "MONDO"; MONDO calls it **congenital anomalies of kidney and urinary tract syndrome with or without hearing loss, abnormal ears, or developmental delay**
- `DOID:0112359` (6 mentions) - the report calls it "Disease Ontology"; DOID calls it **congenital anomalies of kidney and urinary tract syndrome with or without hearing loss, abnormal ears, or developmental delay**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000076` (1 mention) - the report calls it "Vesicoureteral reflux / urinary tract anomalies"; HP calls it **Vesicoureteral reflux**
- `HP:0000356` (1 mention) - the report calls it "Outer ear abnormalities"; HP calls it **Abnormality of the outer ear**, and lists "Outer ear abnormality" among its other names
- `GO:0005634` (1 mention) - the report calls it "Subcellular:** nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names

### Terms the ontology service could not be reached for

21 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `HP:0000093` (1 mention)
- `HP:0000097` (1 mention)
- `HP:0001562` (1 mention)
- `HP:0001629` (1 mention)
- `HP:0000894` (1 mention)
- `HP:0001087` (1 mention)
- `GO:0008584` (1 mention)
- `GO:0030325` (1 mention)
- `GO:0008283` (1 mention)
- `CL:1000090` (1 mention)
- `CL:0000216` (1 mention)
- `UBERON:0002113` (1 mention)
- `UBERON:0000056` (1 mention)
- `UBERON:0001255` (1 mention)
- `UBERON:0000991` (1 mention)
- `UBERON:0001846` (1 mention)
- `UBERON:0001105` (1 mention)
- `UBERON:0001103` (1 mention)
- `UBERON:0002106` (1 mention)
- `GO:0005737` (1 mention)
- `NCBITaxon:10090` (1 mention)

### Terms whose obsolescence could not be checked

10 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `HP:0000085` (1 mention)
- `HP:0012622` (1 mention)
- `HP:0000717` (1 mention)
- `HP:0001636` (1 mention)
- `HP:0007957` (1 mention)
- `GO:0001658` (1 mention)
- `CL:0000417` (1 mention)
- `UBERON:0004176` (1 mention)
- `UBERON:0000948` (1 mention)
- `GO:0005634` (1 mention)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `MGI`.