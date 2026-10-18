---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-16T03:54:34.135944'
end_time: '2026-10-16T03:55:36.946241'
duration_seconds: 62.81
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Myopathy Due To Myoadenylate Deaminase Deficiency
  mondo_id: MONDO:0014220
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
  num_turns: 5
  total_cost_usd: 0.17274309999999998
  session_id: 6f407ab6-10d8-510b-8a76-b165dbc02479
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 9
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 2
  validator_version: 0.3.0
term_validation:
  total_terms: 2
  verified: 2
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0014220
    reported_labels:
    - given in the task
    ontology_label: myopathy due to myoadenylate deaminase deficiency
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Myopathy Due To Myoadenylate Deaminase Deficiency
- **MONDO ID:** MONDO:0014220 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Myopathy Due To Myoadenylate Deaminase Deficiency** covering all of the
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

# Myopathy Due To Myoadenylate Deaminase Deficiency (AMPD1 deficiency, MADD): research report

**Scope and verification.** I ran three web searches. They confirmed the topics and URLs cited below, but they returned no PMIDs I could check. Papers that I cite from memory are given as author and year with the label **[PMID not verified]**. Run `just fetch-reference` on each before it becomes KB evidence. I give no abstract quotes here because I did not see any abstract text. The search summaries paraphrase their sources, so they are not usable as snippets either.

## 1. Disease information

- **Overview.** Myoadenylate deaminase deficiency is a deficiency of AMP deaminase 1 (AMPD1), the skeletal-muscle isoform. It is autosomal recessive and mostly harmless. Most people with complete enzyme deficiency are asymptomatic. Symptomatic cases present with exercise-related myalgia, cramps and early fatigue.
- **Prevalence and genotype.** The dominant allele is c.34C>T (p.Gln12Ter) in exon 2. Reported carrier frequency is about 1–2% in the general population ([PMC2278656](https://pmc.ncbi.nlm.nih.gov/articles/PMC2278656), citing Norman et al., not verified).
- **Identifiers.**
  - MONDO:0014220 (given in the task).
  - Gene AMPD1, with the HGNC ID to be looked up via OAK. Lowercase `hgnc:` is the KB convention.
  - OMIM, Orphanet and MeSH IDs not verified here. Look up the OMIM entries for MMDD (the disease) and AMPD1 (the gene) rather than writing them from memory.
- **Synonyms.** MADD, AMPD1 deficiency, AMP deaminase deficiency, muscle AMP deaminase deficiency, myoadenylate deaminase deficiency (MAD). GeneCards lists "Adenosine Monophosphate Deaminase Deficiency" as a related disorder name ([GeneCards AMPD1](https://www.genecards.org/card/AMPD1)).
- **Data source.** The information is aggregated at disease level. Individual-patient data are limited to muscle-biopsy series.
- **Existing KB material.** dismech already has an IEMbase comparison note for this disease: [IEMbase 0144](https://dismech.monarchinitiative.org/elements/curation-notes/iembase-vs-dismech/IEMBASE-0144-AMPD1_myoadenylate_deaminase_deficiency-2026-07-07/). Read it before curating.

## 2. Etiology

- **Cause.** Biallelic loss-of-function variants in AMPD1, mainly the common nonsense allele c.34C>T. Its rsID is rs17602729 ([Springer](https://link.springer.com/article/10.1007/s10557-013-6506-5), [PMC3955129](https://pmc.ncbi.nlm.nih.gov/articles/PMC3955129), both surfaced in search; contents not read in full).
- **Allele frequency.** Reported as about 10–14% in people of European ancestry. It is much rarer in East Asian populations (not verified here; check gnomAD).
- **Rarer alleles.** A second common allele, c.860C>T (p.Pro287Leu), is described in the older literature (Morisaki et al. 1992; Sabina et al. 1992; **PMIDs not verified**). It usually occurs in cis with c.34C>T.
- **Acquired secondary deficiency.** Reduced AMPD activity also occurs in other neuromuscular diseases. This is an inference from the older literature, not something I confirmed.
- **Why most carriers are asymptomatic.** The search results indicate that most homozygotes have no symptoms. The reason is not settled. Possible modifiers are co-existing metabolic or muscle disease and AMPD2/AMPD3 compensation. Treat both as hypotheses.
- **Protective factors and gene–environment effects.** None are established. One cardiac observation exists (see section 11). It is a modifier effect and is not a disease-protective factor.

## 3. Phenotypes (with HPO suggestions; verify each ID via lookup)

| Phenotype | Notes | Suggested HPO term (verify) |
|---|---|---|
| Exercise-induced myalgia | Most common symptomatic presentation | Exercise-induced muscle pain |
| Muscle cramps | After exertion | Muscle cramp |
| Exercise intolerance / early fatigue | Fatigue out of proportion to effort | Exercise intolerance |
| Myalgia | Can be more persistent | Myalgia |
| Elevated serum creatine kinase | Seen in some patients, not all | Elevated serum creatine kinase |
| Rhabdomyolysis | Rare, reported in case reports; the literature is unclear on whether it is causal | Rhabdomyolysis |

- **Onset.** Usually in childhood or adulthood. Many people stay asymptomatic. I did not verify onset ages.
- **Course.** Non-progressive and mild. Symptoms are exertional and recurrent.
- **Frequencies.** I have no verified percentages. Do not assign HPO frequency terms without a cited cohort. Use the prose "most are asymptomatic".
- **Quality of life.** Not available.
- **Ontology grounding.** CURIEs and labels must come from OAK or the cache lookup, not from memory.

## 4. Genetic and molecular information

- **Gene.** AMPD1, on chromosome 1p13.
- **Main variant.**
  - c.34C>T (p.Gln12Ter) creates a premature stop codon in exon 2 and gives an inactive enzyme ([Springer](https://link.springer.com/article/10.1007/s10557-013-6506-5)).
  - Protein notation varies across papers. One source writes it as Glu12Stop. The accepted form is p.Gln12Ter.
  - Mechanism: loss of function. Origin: germline.
- **Variant classification.** Check ClinVar and ClinGen. I have not seen a ClinGen gene–disease validity record. Use `just list-gene-validity` and do not assign a tier.
- **Modifier genes.** AMPD2 and AMPD3 are paralogs that may compensate. This is an inference and was not verified.
- **Epigenetics and chromosomal abnormalities.** None known.

## 5. Environmental information

None are established. Exercise provokes symptoms in patients but is not a cause. Statins and other myotoxic drugs may unmask symptoms. I did not verify that, so do not curate it without evidence.

## 6. Mechanism / pathophysiology

**Causal chain (the demonstrated and inferred steps are marked):**
1. Biallelic AMPD1 loss-of-function variants, mainly c.34C>T, mean muscle cells make no active AMPD1 (demonstrated).
2. Loss of AMPD1 impairs deamination of AMP to IMP, the first step of the purine nucleotide cycle in skeletal muscle (demonstrated).
3. During intense exercise AMP is not cleared by deamination. Knockout mouse muscle shows much larger rises in AMP and AMP:ATP ratio on stimulation than wild-type muscle, with only modest, soleus-limited AMPK enhancement ([PMC5121310](https://pmc.ncbi.nlm.nih.gov/articles/PMC5121310), summarized from the search; full text not read).
4. The classic hypothesis is that reduced purine nucleotide cycle flux limits fumarate anaplerosis of the TCA cycle, which causes early fatigue and myalgia. **This step is contested.** A 2001 human study (summarized by the search; authors and PMID not captured) reported that complete and partial AMPD deficiency did not affect TCA anaplerosis, phosphocreatine hydrolysis, energy charge or exercise performance.
5. Altered adenine-nucleotide handling or AMPK signaling may connect the biochemical defect to symptoms. This is inferred and has not been shown.
6. Symptoms appear in only a minority of people with the enzyme defect. Whether another factor is needed is unresolved.

**Candidate ontology terms (verify before use).**
- GO: AMP deaminase activity, IMP biosynthetic process, purine nucleotide metabolic process, response to muscle activity.
- CL: skeletal muscle fiber, preferably fast-twitch (type II). AMPD1 is expressed most in fast fibers (not verified).
- CHEBI: AMP, IMP, ammonia.

**Omics.** No data found. I did not search GEO or PRIDE.

## 7. Anatomical structures affected

- Skeletal muscle is the only primary site (UBERON skeletal muscle tissue, to be verified).
- Subcellular compartment: the sarcoplasm and myofibrillar-associated enzyme pool. I have not confirmed the localization.
- No lateralization. Involvement is generalized.
- Cardiac muscle expresses AMPD isoforms other than AMPD1. Do not describe the cardiac effect as an organ-level feature of this disease.

## 8. Temporal development

Onset is variable, from childhood to adulthood. The course is non-progressive. There are no stages and no known remission pattern. The literature I recall shows no critical period.

## 9. Inheritance and population

- **Inheritance.** Autosomal recessive. HP:0000007 is the HPO term, but verify it before binding.
- **Carrier and homozygote frequency.** About 1–2% for deficiency in the general population, from the PMC2278656 summary. The c.34C>T allele frequency is 10–14% in people of European ancestry, from the Springer review.
- **Penetrance.** Low. Most homozygotes have no symptoms, so penetrance is not the same as genotype frequency.
- **Population effects.** The c.34C>T allele is common in Europeans and rare in East Asians. The KB needs this recorded under `population_effects` with a HANCESTRO term and a cited source. I have no source yet, so treat it as unsourced.
- **Sex ratio and consanguinity.** Not found.

## 10. Diagnostics

- **Muscle biopsy.**
  - Histochemical or biochemical AMPD assay showing absent or very low AMPD activity. This was the historic gold standard.
  - Histology is otherwise unremarkable.
- **Genetic testing.** Targeted testing for c.34C>T, or an AMPD1 gene or myopathy panel. Whole-exome sequencing also covers it.
- **Forearm ischemic exercise test.** Ammonia fails to rise while lactate rises normally. This is the classic functional screen, and I recall it from the older literature. It is not verified here. Candidate LOINC codes must come from `just loinc-seed-cache`, not from memory.
- **Differential diagnosis.** Metabolic myopathies:
  - McArdle disease (glycogen phosphorylase deficiency)
  - Phosphofructokinase deficiency
  - Carnitine palmitoyltransferase II deficiency
  - Mitochondrial myopathy
- **Screening.** No newborn or population screening.
- **Incidental findings.** Because the allele is so common, the c.34C>T genotype alone does not establish the diagnosis. A variant found in an asymptomatic person is expected.

## 11. Outcome / prognosis

- **Mortality.** No excess mortality in the skeletal-muscle phenotype.
- **Heart failure association.** A 1999 study (Loh et al.; **PMID not verified**) reported that among 132 dilated cardiomyopathy patients, those carrying the c.34C>T allele had an 8.6-fold greater probability of surviving more than 5 years without transplantation ([Springer, via search summary](https://link.springer.com/article/10.1007/s10557-013-6506-5)).
  - Later work is mixed. A meta-analysis (Feng et al.) found no association with total or cardiac survival. A Christchurch cohort found poorer outcomes for the T allele in the subgroup with prior myocardial infarction ([PMC3955129](https://pmc.ncbi.nlm.nih.gov/articles/PMC3955129), summarized from the search).
  - This is a heart-failure modifier association, not a feature of the myopathy. Keep it out of the core disease phenotype list. If curated, record it with its conflicting evidence.
- **Function and complications.** I found no consistent disability. Rhabdomyolysis is rare and its causal link is unclear.

## 12. Treatment

- **Established treatment.** None. Management is supportive: reassurance, graded exercise, and avoiding provoking exertion.
- **Ribose.** D-ribose supplementation has been tried (my recollection; **no verified citation**). Do not curate it without a source. If you do, check CHEBI and NCIT terms through lookup and use `therapeutic_agent`.
- **Gene, cell and RNA therapies.** None are known. I did not search ClinicalTrials.gov, so do not assert that no trials exist.
- **Pharmacogenomics.** I know of none.

## 13. Prevention

There is no primary or secondary prevention. Genetic counseling is simple: recessive inheritance and a high carrier frequency mean most relatives are asymptomatic. Do not recommend screening.

## 14. Other species

- I have no verified information on naturally occurring disease, breeds or VBO terms. OMIA has not been checked.
- Orthologs exist in the mouse (Ampd1). NCBI Gene IDs must be looked up.

## 15. Model organisms

- **Ampd1 knockout mouse.** Described in the search as "a good metabolic phenocopy of human AMPD1 deficiency" with "no abnormalities in muscle performance in three different exercise protocols". Stimulated muscle shows larger AMP and AMP:ATP rises than wild-type ([PMC5121310](https://pmc.ncbi.nlm.nih.gov/articles/PMC5121310), summarized).
- **AMPD1 knockdown mice (2022).** Electroporation knockdown gave slower contraction and relaxation in EDL but not soleus. The authors noted that earlier fatigue findings are inconsistent ([IUPUI repository](https://scholarworks.indianapolis.iu.edu/items/6484a86f-b0e5-4722-a966-ea939a700dc8), summarized from the search).
- **Fidelity.** Limited. The mouse reproduces the biochemistry but not the human exertional symptoms. That fits a `PARTIALLY_RECAPITULATES` or `FAILS_TO_RECAPITULATE` link with `limitations` stated. It may justify a `HUMAN_MODEL_MISMATCH` discussion in the KB entry.
- **Pharmacological inhibition.** A Birmingham study of pharmacological AMP deaminase inhibition and AMPD1 deletion exists ([record](https://research.birmingham.ac.uk/en/publications/effects-of-pharmacological-amp-deaminase-inhibition-and-ampd1-del/)). I did not read it.

## Evidence quality and next steps for curation

1. **Fetch references first.** Candidate sources, none with a confirmed PMID: Fishbein, Morisaki and Sabina (1978 and 1992), Norman, Loh 1999, the 2001 human anaplerosis study, the Feng meta-analysis, the Ampd1 knockout paper, and the 2022 knockdown paper. Search PubMed for each, then run `just fetch-reference PMID:…` and quote only from the cached files.
2. **Points where the literature disagrees, to record as such:**
   - The anaplerosis hypothesis for the symptoms.
   - Whether the enzyme defect causes symptoms at all, given its high carrier frequency.
   - The direction of the heart-failure association.
3. **Gaps this report did not fill:** HPO frequencies, OMIM/Orphanet/HGNC identifiers, onset ages, GeneReviews coverage (use `just check-genereviews`), clinical trials, OMIA, and ClinGen validity.

**Sources used (search results only):**
- [PMC2278656](https://pmc.ncbi.nlm.nih.gov/articles/PMC2278656)
- [MedlinePlus AMPD1](https://medlineplus.gov/genetics/gene/ampd1)
- [GeneCards AMPD1](https://www.genecards.org/card/AMPD1)
- [Springer 10.1007/s10557-013-6506-5](https://link.springer.com/article/10.1007/s10557-013-6506-5)
- [PMC3955129](https://pmc.ncbi.nlm.nih.gov/articles/PMC3955129)
- [PMC5121310](https://pmc.ncbi.nlm.nih.gov/articles/PMC5121310)
- [IUPUI repository](https://scholarworks.indianapolis.iu.edu/items/6484a86f-b0e5-4722-a966-ea939a700dc8)
- [Birmingham record](https://research.birmingham.ac.uk/en/publications/effects-of-pharmacological-amp-deaminase-inhibition-and-ampd1-del/)
- [dismech IEMbase note](https://dismech.monarchinitiative.org/elements/curation-notes/iembase-vs-dismech/IEMBASE-0144-AMPD1_myoadenylate_deaminase_deficiency-2026-07-07/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014220` (1 mention) - the report calls it "given in the task"; MONDO calls it **myopathy due to myoadenylate deaminase deficiency**