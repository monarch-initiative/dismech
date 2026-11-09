---
provider: claude_managed
model: claude-opus-5-5
cached: false
start_time: '2026-11-08T17:21:13.609407'
end_time: '2026-11-08T17:46:12.484877'
duration_seconds: 1498.88
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Birt-Hogg-Dube Syndrome
  mondo_id: MONDO:0800444
  category: Mendelian
  causal_genes: FLCN
  omim_id: not recorded
  synonyms: "BHD; Birt-Hogg-Dub\xE9 Syndrome"
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    save_artifacts: true
    artifact_max_bytes: 5242880
    artifact_keep_runtime: false
    artifact_extra_extensions: []
    artifact_include_globs: []
    artifact_exclude_globs: []
    retriever_model: claude-haiku-5-5
    max_iterations: 5
    max_cost_usd: 20.0
    allowed_hosts: []
    max_repair_rounds: 2
    poll_interval: 15.0
    timeout: 5400
    delete_session: false
run_metadata:
  session_id: sesn_01AMSoMCSVw8yXYJoEffJ5NK
  agent_id: agent_01K5k8H6H4Uxic777boZvtbf
  agent_version: 1
  environment_id: env_01NDhAwC4BsT39w6UteFeYkq
  retriever_model: claude-haiku-5-5
  stop_reason: end_turn
  outcome_result: satisfied
  workflow_runs: 2
  tool_calls: 58
  outcome_iterations: 2
  grader_explanation: "An independent grader found all criteria met:\n\n- Research\
    \ report quality (evidence, traceable and aligned citations, relevance, structure,\
    \ coverage) (met): I checked the deliverables with scripts and by spot-checking\
    \ sources.\n\n**Evidence files**\n- All 192 files in citations/ parse as YAML\
    \ and have the key, identifiers, title, source_url and content fields.\n- Every\
    \ PubMed source_url matches a PMID in that file's identifiers.\n- The bodies are\
    \ retrieved source text, not agent summaries. These include abstracts, full-text\
    \ excerpts, OLS4 JSON records and verbatim HPO/NCIT term records. Files that matched\
    \ words like 'summary' turned out to be source text, such as the Chinese consensus\
    \ recommendations and the abstract's 'KEY FINDINGS' heading.\n\n**Traceability**\n\
    - All 138 PMID/NCT identifiers cited in REPORT.md appear in an evidence file's\
    \ identifiers.\n- Every cited URL (Orphanet, MONDO, MeSH, NCBI Gene, NCI PDQ,\
    \ OMIA) is also listed as an identifier.\n- All 138 also appear in References,\
    \ one line each, with a full citation and the evidence file path.\n- I checked\
    \ about 256 quote-plus-citation pairs automatically. All matched word for word\
    \ in the cited evidence file. The few apparent failures were artifacts of my quote\
    \ parsing; I checked the Orphanet definition, the Hornstein-Knickenberg synonym\
    \ and the MONDO synonyms by hand.\n\n**Alignment**\nThe sources I spot-checked\
    \ support their sentences:\n- Nahorski 2010: higher colorectal neoplasia risk\
    \ with c.1285dupC than with c.610delGCinsTA, and 23% of MSI colorectal cancers.\n\
    - Steinlein 2022: 1.3% vs 11.4% (female vs male timely diagnosis).\n- Kijlertsuphasri:\
    \ older age and male sex predict renal tumours.\n- Matsui: eGFR fall of 10.7 mL/min/1.73m\xB2\
    \ after ablation.\n- Bai 2026: 693 LOVD variants.\n- Zhang 2024: 37% with no family\
    \ history and a 7.6-year diagnostic delay.\n- Korea claims study: 5.67 per 10\
    \ million and median age 51.\n- The NCT02504892 record: 'no proven systemic therapy.'\n\
    - The Orphanet prevalence figures are copied faithfully from the ORDO record.\n\
    \nThe report states where sources disagree rather than citing one side:\n- colorectal\
    \ cancer risk (Swedish register vs Dutch registry vs Zbar);\n- the direction of\
    \ mTORC1 change;\n- phenotype-based vs genotype-based prevalence;\n- the effect\
    \ of smoking;\n- air-travel advice (ERN vs Chinese consensus);\n- stable vs declining\
    \ lung function.\n\n**Relevance**\nClaims rest mostly on primary literature and\
    \ authoritative sources: the ERN GENTURIS 2024 guideline, GeneReviews, cohort\
    \ studies and model-organism papers. Each section draws on several sources.\n\n\
    **Structure**\n- The task specified a 15-section template, and the report follows\
    \ it. That overrides the rubric's default of six to eight sections.\n- It opens\
    \ with scope, interpretation and main findings, and names FLCN in the first paragraph.\n\
    - Section 6 opens with the requested numbered causal chain, with branches and\
    \ evidence-type and inferred labels.\n- Ontology terms (HPO, GO, CL, UBERON, NCIT,\
    \ CHEBI, VBO, NCBI Gene/Taxon) are backed by ontology evidence files.\n- The sections\
    \ are written as narrative paragraphs.\n- Open Questions and References sections\
    \ are present.\n\n**Coverage**\nAll 12 PLAN.md sub-questions are addressed. Items\
    \ with no data are marked explicitly, for example lipidomics, CRISPR screens,\
    \ gene therapy and incidence.\n\n**Minor issues**\nNone of these is substantive:\n\
    - Section 4 uses bold paragraph labels.\n- One remark about Fnip1 immune roles\
    \ is labelled 'not saved' and has no citation."
  input_tokens: 980
  output_tokens: 508726
  cache_read_input_tokens: 41564565
  web_search_requests: 41
  web_fetch_requests: 0
  list_cost_usd: 8.87
  active_seconds: 3317.0589999999997
  evidence_check:
    evidence_files: 192
    cited_identifiers: 133
    cited_without_evidence: []
    quotes_checked: 171
    quotes_anchored: 171
    unanchored_quotes: []
  repair_rounds: 1
  repair_history:
  - evidence_files: 192
    cited_identifiers: 133
    cited_without_evidence: []
    quotes_checked: 173
    quotes_anchored: 171
citation_count: 174
artifact_count: 1
artifact_sources:
  claude_managed: 1
artifacts:
- filename: PLAN.md
  path: Birt-Hogg-Dube_Syndrome-deep-research-claude_managed_artifacts/PLAN.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01FCUxv9cMgiMfWCDoWREA1R
  description: null
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Birt-Hogg-Dube Syndrome
- **MONDO ID:** MONDO:0800444 (if available)
- **Causal gene(s):** FLCN
- **OMIM:** not recorded
- **Synonyms:** BHD; Birt-Hogg-Dubé Syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Birt-Hogg-Dube Syndrome** covering all of the
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

# Birt-Hogg-Dubé Syndrome (MONDO:0800444; causal gene FLCN): a cited knowledge-base review

**Scope and interpretation.** This report characterises Birt-Hogg-Dubé syndrome (BHD; MONDO:0800444), the autosomal dominant disorder caused by germline heterozygous loss-of-function variants in **FLCN**, the gene encoding the tumour-suppressor protein folliculin (17p11.2). The request supplies its own 15-section template, so the report follows that template rather than a free-form review structure, and ends with Open Questions and References. The template records OMIM as not recorded; the OMIM numbers given below are those cross-referenced by MONDO, Orphanet and NCBI Gene evidence files, not taken from OMIM directly (OMIM pages could not be retrieved). Ontology term suggestions (HPO, GO, CL, UBERON, NCIT, CHEBI, HGNC, VBO, NCBI Gene/Taxon) are curator suggestions; every ontology CURIE given was confirmed against an ontology/database record saved in `citations/` (files prefixed `onto-` and `species-`), and the term-to-phenotype mapping is the author's suggestion unless stated as an HPO annotation. Evidence type is flagged as human clinical, model organism, in vitro or computational where it matters. Every specific number and quotation is taken from an evidence file in `citations/`.

**Main findings.** BHD is a rare, under-diagnosed, autosomal dominant cancer-predisposition genodermatosis with three cardinal organ manifestations: benign cutaneous fibrofolliculomas/trichodiscomas, multiple basal pulmonary cysts with spontaneous pneumothorax, and bilateral/multifocal renal tumours, typically hybrid oncocytic/chromophobe tumours (PMID:39085584; PMID:20301695). Germline FLCN variants are overwhelmingly truncating, with a hotspot in the exon 11 polycytosine tract (c.1285dupC/delC) (PMID:12204536; PMID:39085584). Renal tumours follow a two-hit tumour-suppressor model (PMID:15956655; PMID:26334087). Mechanistically, folliculin with FNIP1/FNIP2 acts as a GTPase-activating protein for RagC/RagD at the lysosome; its loss selectively prevents mTORC1 phosphorylation of TFEB/TFE3, whose constitutive nuclear activity drives kidney cystogenesis and tumorigenesis in models (PMID:24095279; PMID:32612235; PMID:40499782). Phenotype-based prevalence estimates (about 1–2 per million to 1 in 200,000) conflict with genotype-based carrier frequencies of roughly 1 in 2,700–4,200, implying substantial under-ascertainment and lower penetrance in unselected carriers (PMID:40210444; PMID:35639097; PMID:33987191). Management is surveillance-based: lifelong renal imaging (preferably MRI) from age 20, nephron-sparing intervention when the largest tumour reaches 3 cm, and individualised pneumothorax counselling; no systemic therapy is proven (PMID:39085584; NCT02504892).

---

## 1. Disease Information

**Overview.** The 2024 ERN GENTURIS guideline defines BHD as "a rare condition caused by pathogenic variants (PV) or likely pathogenic variants in the FLCN gene, encoding the tumour suppressor protein folliculin" with "major manifestations in three organs: benign cutaneous fibrofolliculomas/trichodischomas (FF/TD), pulmonary cysts with an associated increased risk of spontaneous pneumothorax (PTX) and, importantly, renal tumours" (PMID:39085584). The European BHD Consortium described it as "an autosomal dominant condition characterised" "clinically by skin fibrofolliculomas, pulmonary cysts, spontaneous pneumothorax," and renal cancer (PMID:19959076). Orphanet's definition is "A rare inherited cancer-predisposing syndrome characterized by skin lesions, benign and malignant kidney tumors, and pulmonary cysts that may be associated with pneumothorax." (https://www.orpha.net/en/disease/detail/122). The MeSH scope note describes an "Autosomal dominant neoplastic syndrome characterised by genodermatosis, lung" cysts and kidney tumours (https://id.nlm.nih.gov/mesh/D058249).

**History.** Birt, Hogg and Dubé (1977) described a kindred in which cutaneous tumours appeared after age 25; the lesions "proved to be a type of pilar tumor that we named" fibrofolliculoma, and "Fifteen of 37 members older than the age of 25 years exhibited the typical" lesions (PMID:596896). Two years earlier Hornstein and Knickenberg reported "a peculiar fibromatosis cutis in two siblings" with perifollicular fibromas and colon polyps (PMID:1200700). Happle has argued that the eponym reflects a historical error and proposed the alternative names Hornstein-Birt-Hogg-Dubé syndrome or Hornstein-Knickenberg syndrome (PMID:22581760; PMID:31923324); MeSH, Orphanet, NCI and GeneReviews continue to use the name Birt-Hogg-Dubé syndrome.

**Identifiers.** MONDO:0800444 (label: Birt-Hogg-Dube syndrome) carries cross-references to GARD:0028061, MEDGEN:91070, NORD:858, the OMIM phenotypic series PS135150 and UMLS C0346010 (https://purl.obolibrary.org/obo/MONDO_0800444). Orphanet: ORPHA:122, with cross-references ICD-10 C64, ICD-11 LD27.5, MeSH D058249, MedDRA 10067736, OMIM 135150 and OMIM 620459, MONDO:0800445 (the FLCN-specific subtype term) and UMLS C0346010 (https://www.orpha.net/en/disease/detail/122). MeSH descriptor D058249, Birt-Hogg-Dube Syndrome (introduced 2011), (https://id.nlm.nih.gov/mesh/D058249). The causal gene FLCN is NCBI Gene 201163, OMIM 607273, on 17p11.2 (https://www.ncbi.nlm.nih.gov/gene/201163); HGNC:27310 (location 17p11.2) and UniProtKB Q8NFG4 (citations/onto-ncit-hgnc-flcn-fnip1-fnip2.md; citations/onto-ncit-uniprot-flcn-q8nfg4.md). NCIT concept for the disease: NCIT:C28244 (Birt-Hogg-Dube Syndrome) (citations/onto-ncit-nci-thesaurus-bhd-genetic-counseling.md). HPO disease annotations exist for OMIM:135150 (mapped to MONDO:0800445) and ORPHA:122 (citations/onto-hpo-bhd-annotations-omim-135150.md). Note that ICD-10 C64 (malignant neoplasm of kidney) is a manifestation code; a Korean claims-data study noted there is no specific ICD-10 code for BHD (PMID:35666727).

**Synonyms.** MONDO lists `"synonyms" : [ "BHD", "Birt-Hogg-Dubé Syndrome" ]` for MONDO:0800444 (https://purl.obolibrary.org/obo/MONDO_0800444). Orphanet lists "Hornstein-Knickenberg syndrome" (https://www.orpha.net/en/disease/detail/122), and MeSH entry terms include Hornstein-Knickenberg Syndrome and Fibrofolliculomas with Trichodiscomas and Acrochordons (https://id.nlm.nih.gov/mesh/D058249). Other abbreviations in use are BHDS (PMID:20301695) and FLCN-related BHD. FLCN gene aliases include BHD, DENND8B and FLCL (https://www.ncbi.nlm.nih.gov/gene/201163).

**Nature of the information.** The information summarised here is aggregated disease-level knowledge from ontologies (MONDO, Orphanet, MeSH), guidelines (ERN GENTURIS 2024; GeneReviews; 2023 Chinese consensus), cohort and registry studies (NIH/NCI, Dutch, French, Swedish, Chinese, Japanese, Korean cohorts; UK Biobank/100,000 Genomes; Geisinger MyCode EHR-linked exomes) and experimental studies; individual patient-level EHR data were not used except as summarised in those publications (e.g., PMID:35639097).

## 2. Etiology

**Disease causal factors.** BHD is genetic. "BHD syndrome is caused by monoallelic loss of function PVs in the FLCN gene [1, 3], and renal tumours are initiated by somatic mutations or loss of the wild-type allele (as in a classic tumour suppressor model)" (PMID:39085584). The FLCN locus was delineated "to 700 kb on chromosome 17p11.2", with protein-truncating mutations "with a 44% frequency of insertion/deletion mutations within a hypermutable C(8) tract" (PMID:12204536). A small fraction of clinically diagnosed cases lack an FLCN variant: GeneReviews attributes 96% of BHDS to FLCN and ~4% to unknown causes (PMID:20301695), and the ERN guideline notes "two recent reports of cases with cutaneous FF and renal cancer that were associated with rare missense variants in PRDM10 (p.Cys677Tyr and p.Cys677Arg)" (PMID:39085584). PRDM10-associated disease is a distinct entity and is outside MONDO:0800444/FLCN scope.

**Genetic risk factors.** The primary risk factor is a germline pathogenic FLCN variant (Section 4). Within FLCN carriers, organ-specific risk modifiers are largely unknown: "no other putative genotype-phenotype correlations have been confirmed to date" (PMID:39085584). Reported but unconfirmed associations include higher colorectal neoplasia risk with c.1285dupC than c.610delGCinsTA (PMID:20522427) and higher pneumothorax risk with the exons 1–3 deletion: "Higher risk of pneumothorax was associated with exons 1-3 deletion mutation" (PMID:39300538). The so-called "pneumothorax-only" variants are not a true genotype class: "Of the 194 pathogenic FLCN variants, 76 could be defined as 'pneumothorax-only'" but "The majority of POPVs (65/76) affected no more than three individuals" (PMID:34267338), and the ERN guideline recommends that FLCN variants "should not be considered as ‘pneumothorax-only’ variants" (PMID:39085584). Lung cyst burden predicts pneumothorax: "The presence of lung cysts was significantly associated with pneumothorax (p = 0.006)" (PMID:17322109), and in a LAM/BHD comparison "The maximum diameter of cysts was the sole independent risk factor for spontaneous pneumothorax" (PMID:30673341). Family history is a risk factor through autosomal dominant transmission, and first-degree adult relatives of carriers should be offered predictive testing (PMID:39085584).

**Environmental risk factors.** No environmental cause of BHD exists. Age is the strongest modifier of expression (age-dependent penetrance; PMID:39085584; PMID:36849229). Sex: women appear to have fewer skin lesions ("Women tend to have smaller and fewer lesions than men") and an earlier average pneumothorax onset (30.2 years in females vs 38.4 in males) (PMID:20301695). Smoking is discouraged by guidelines (PMID:39085584; PMID:37670643), but clinical evidence that smoking modifies BHD pneumothorax risk is weak: in a Chinese CT series "A total of 79% (11/14) of patients with a history of pneumothorax were non-smokers" (PMID:35125098). Experimentally, cigarette smoke lowers FLCN protein: "CS exposure is a secondary cause of FLCN deficiency due to the enhanced proteolysis" (PMID:35301243; mouse/in vitro and COPD lung tissue). Pressure changes (air travel, diving) are situational triggers of pneumothorax: estimated risks are 0.63% per flight and 0.33% per dive (PMID:27652079; PMID:39085584).

**Protective factors.** No protective genetic variants or modifier alleles have been identified, and no environmental factor has been shown to prevent BHD manifestations. Pleurodesis after pneumothorax "reduced the ipsilateral recurrence rate by half" in a recall-based survey (PMID:28248571), which is a tertiary-prevention measure rather than a protective factor.

**Gene–environment interactions.** No formal G×E study exists. The only plausible interactions are (i) mechanical: the stretch hypothesis proposes that respiration-induced stretch of alveoli with weakened FLCN-dependent cell–cell adhesion causes cysts (PMID:26877139; hypothesis, not demonstrated), and barometric changes during flights/diving may precipitate pneumothorax (PMID:27652079); and (ii) chemical: cigarette smoke reduces FLCN protein in airway epithelium (PMID:35301243). CTD lists no BHD-specific chemical–disease interactions in the retrieved evidence (not available).

## 3. Phenotypes

The ERN guideline summarises that BHD "is phenotypically heterogeneous", "Inheritance is autosomal dominant with age-dependent penetrance and variable expression. Inter- and intra-familial phenotypic variability is common." (PMID:39085584). GeneReviews Table 2 gives lifetime frequencies of cutaneous manifestations 87%–97%, pulmonary cysts 70%–85%, spontaneous recurrent pneumothorax 24%–48% and renal cell carcinoma 15%–30% (PMID:20301695). A pooled literature analysis gave "The prevalence of pneumothorax, pulmonary cysts, RCC and characteristic skin lesions in BHDS were 50.9% (n = 1038), 91.9% (n = 720), 22.5% (n = 929) and 47.9% (n = 989), respectively." (PMID:34267338). A segregation analysis of 204 families estimated that "By age 70 years, male carriers of the FLCN variant have an estimated 19% (95% CI 12% to 31%) risk of renal tumours, 87% (95% CI 80% to 92%) of lung involvement and 87% (95% CI 78% to 93%) of skin lesions, while female carriers had an estimated 21% (95% CI 13% to 32%) risk of renal tumours" (PMID:36849229). Frequencies in unselected genotype-first carriers are much lower (Section 9).

**3.1 Fibrofolliculomas / trichodiscomas (clinical sign; skin).** Fibrofolliculomas are "multiple small skin-colored, opaque, whitish or yellowish dome-shaped papules" that "start to appear between the second and fourth decade of life" and "often increase in size, number, and distribution with age, eventually involving the face, neck, and upper trunk" (PMID:20301695). "Fibrofolliculomas are the most common phenotypic features of BHD syndrome occurring in greater than 85% of BHD patients over the age of 25." and "Fibrofolliculomas, which develop after puberty, are generally neither painful nor pruritic." (PMID:26334087). In the NCI series, "Ninety per cent (46/51) of families with BHDS had individuals with multiple 1–5 mm white or skin coloured papules distributed over the face, neck and/or upper trunk and a histologically confirmed fibrofolliculoma (FF)." (PMID:18234728); in a French series "Eighteen of the 22 individuals affected by BHDS (82%) were diagnosed with five or more FFs." (PMID:19785621). Penetrance is "87 to 97% by age 70 years" (PMID:39085584). Onset is in adulthood, and lesions are rare before age 20 ("Cutaneous manifestations are unusual in persons age <20 yrs."; PMID:20301695). The lesions are medically mild, and their burden is mainly cosmetic. They progress slowly in number and size over time. Frequency is lower in East Asian cohorts (skin lesions 36.7% in 166 East Asian patients; PMID:33313181). Suggested HPO: Fibrofolliculoma (HP:0030436); Trichodiscoma (HP:0032228); Perifollicular fibroma (HP:0032225) (citations/onto-hpo-skin-lesions.md). HP:0030436 and HP:0032228 are part of the HPO annotation set for OMIM:135150 (citations/onto-hpo-bhd-annotations-omim-135150.md).

**3.2 Acrochordons, angiofibromas, oral papules, other skin lesions.** Other skin findings include acrochordons, angiofibromas, oral papules, cutaneous collagenomas and epidermal cysts (PMID:20301695). In the French cohort "Multiple epidermal cysts, severe facial hyperseborrhoea and oral papules were noted, respectively, in three of 22 (14%), nine of 22 (41%) and nine of 21 patients (43%)." (PMID:19785621). Acrochordons are nonspecific ("found in 25% of the general population"; PMID:20301695). Some families have "angiofibroma, perifollicular fibroma or both angiofibroma and perifollicular fibromas as their only BHDS cutaneous phenotype" (PMID:18234728). Suggested HPO: Skin tags (HP:0010609); Angiofibromas (HP:0010615); Oral mucosal papule (HP:6000957); Epidermoid cyst (HP:0200040); Collagenoma (HP:6000022) (citations/onto-hpo-skin-lesions.md).

**3.3 Pulmonary cysts (imaging sign; lung).** Cysts are "located mainly in the basal lung regions (subpleural and intrapulmonary areas)"; "The total number of lung cysts per individual ranges from zero to 166 (mean: 16). They are of irregular shape and variable size (1.0-30 mm)." (PMID:20301695). "Pulmonary cysts were the most frequent phenotypic manifestation of BHD, present in 85% of patients." (PMID:28248571); 99% in 100 consecutive Chinese patients (PMID:39300538); "Lower lobe predominant pulmonary cysts occur in up to 90% of patients" (PMID:31272105). In CT series, "Pulmonary cysts were bilateral and multiple, round, irregular, or willow-like." and "93.6% of the large cysts (long-axis diameter ≥ 20 mm) were under the pleura, and near the mediastinum and spine." (PMID:35125098). About a third of individuals with cysts have never had a pneumothorax (PMID:39085584). Age of onset is unknown ("childhood onset is likely"; PMID:20301695). Cysts are usually asymptomatic and lung function is largely preserved (Section 11). Suggested HPO: Multiple pulmonary cysts (HP:0005948; in the OMIM:135150 annotation set); Pulmonary cyst (HP:0032445) (citations/onto-hpo-lung-pneumothorax.md). Cysts may enlarge over time: in a longitudinal CT study of 43 patients "The size of pulmonary cysts progressed over time" (PMID:37221571).

**3.4 Spontaneous pneumothorax (symptom/acute event; pleura).** "Twenty-four percent (48/198) of patients with BHDS had a history of pneumothorax." (PMID:17322109); the age-adjusted odds ratio was "50.3 (95% confidence interval, 6.4-392)" versus unaffected relatives (PMID:11927500). Lifetime risk: "There is a substantial (24–48%) cumulative lifetime risk of pneumothorax" with a median age at first event of ~34 years (range 7–78) (PMID:39085584); Houweling reported "a pneumothorax risk of 29%" by age 70 (PMID:22146830). In a self-selected survey 76% had ≥1 pneumothorax and "Among patients with multiple pneumothoraces, 73% had an ipsilateral recurrence" (PMID:28248571); in a Chinese cohort pneumothorax occurred in 60% (PMID:39300538), and in East Asian aggregates 74.7% (PMID:33313181). Pneumothorax is "often the first manifestation in individuals with BHDS (onset range: age 13-69 years)" (PMID:20301695). Childhood pneumothorax is uncommon but documented: in a Danish cohort "three of 109 BHD cases experienced childhood pneumothorax, corresponding to a prevalence of 3%" (PMID:29439288), and two unrelated patients had "(recurrent) pneumothorax starting at age 14" (PMID:24994497). Pregnancy may increase risk: pneumothorax "incidence rates of 0.054 and 0.016" per patient-year were observed in BHDS women with versus without pregnancies (PMID:38020174). Pneumothorax follows an episodic, recurrent course. Suggested HPO: Spontaneous pneumothorax (HP:0002108); Repeated pneumothoraces (HP:0006522) (citations/onto-hpo-lung-pneumothorax.md).

**3.5 Renal tumours and cysts (neoplasm; kidney).** "The major renal manifestation of BHD syndrome is RCC which has a lifetime risk of 15–30% [10]." with "a median age of diagnosis of 46 years" and RCC reported as late as 83 years (PMID:39085584). In 130 resected tumours from 30 patients, tumours were "predominantly of chromophobe renal cell carcinomas (44 of 130, 34%) or of hybrid oncocytic neoplasms that had areas reminiscent of chromophobe renal cell carcinoma and oncocytoma (65 of 130, 50%)", and "Multiple and bilateral tumors were noted at an early age (mean 50.7 years)." (PMID:12459621). In a French series "Median age at diagnosis of first renal tumour was 46, and age varied from 20 to 83." and "Nevertheless, 9% had clear cell renal cell carcinoma." (PMID:25519458). Renal cysts are also part of the phenotype (PMID:20301695). The tumours usually grow slowly and are often indolent, but metastatic disease does occur (Section 11). Suggested HPO: Renal cell carcinoma (HP:0005584); Renal oncocytoma (HP:0011798); Renal neoplasm (HP:0009726); Renal cyst (HP:0000107); Multiple renal cysts (HP:0005562) (citations/onto-hpo-kidney.md); no dedicated chromophobe-RCC HPO term was retrieved.

**3.6 Possible additional features (unconfirmed).** Colorectal polyps (cumulative risk by age 70 "21% (95% CI 8% to 45%) for male carriers and 32% (95% CI 16% to 53%) for female carriers"; PMID:36849229), colorectal cancer, melanoma, parotid oncocytoma and thyroid cancer are reported but not confirmed as BHD features (Section 11; PMID:39085584). Suggested HPO (uncertain associations): Large intestinal polyposis (HP:0030255; present in the OMIM:135150 annotation set); Colorectal polyposis (HP:0200063); Salivary gland oncocytoma (HP:0031523) (citations/onto-hpo-colon-salivary.md). Inheritance/onset terms: Autosomal dominant inheritance (HP:0000006); Adult onset (HP:0003581) (citations/onto-hpo-inheritance-onset.md).

**Quality-of-life impact.** For skin, "Self-reported alteration in HQoL was reported in approximately one-third of the patients." and "The mean DLQI score (maximum 30) was low 2.2 (±4.3, range 0-18)." (PMID:21054573). The ERN guideline notes "the presence of multiple facial FF/TDs can have significant psychosocial impact on people living with BHD syndrome" (PMID:39085584). Pneumothorax causes acute morbidity and activity restrictions (flying/diving counselling; PMID:39085584), and the ERN guideline notes that potential psychological effects include "anxiety related to uncertainty about future health problems and/or fear of developing cancer" (PMID:39085584). A clinician's perspective piece notes that people with BHD "often share multiple non-medical ramifications ranging from economic and physical insecurity to interruptions in familial communication patterns and relationships" (PMID:23179794). No EQ-5D or SF-36 studies in BHD were found.

## 4. Genetic/Molecular Information

**Causal gene.** FLCN (folliculin; NCBI Gene 201163; OMIM 607273; 17p11.2) (https://www.ncbi.nlm.nih.gov/gene/201163). "BHD is predicted to encode a 579 amino acid protein, folliculin, which is highly conserved among species." and "BHD is composed of 14 exons." (PMID:18234728). Folliculin's C-terminus resembles DENN-domain Rab GEFs, and "FLCN forms a complex with folliculin interacting proteins 1 and 2 (FNIP1, FNIP2) and with 5' AMP-activated protein kinase (AMPK)." (PMID:28970150). HGNC:27310 (aliases BHD, DENND8B), UniProtKB Q8NFG4; partners FNIP1 (HGNC:29418, 5q31.1) and FNIP2 (HGNC:29280, 4q32.1) (citations/onto-ncit-hgnc-flcn-fnip1-fnip2.md); NCIT:C63518 Folliculin (citations/onto-ncit-nci-thesaurus-bhd-genetic-counseling.md).

**Variant spectrum and classes.** "The vast majority of PV are truncating variants (premature stop-codon, frameshift, canonical splice site variants) detected by DNA sequencing" and "Recurrent pathogenic variants (e.g. frameshift c.1285delC/dupC) have been described." (PMID:39085584). GeneReviews states that 20%–24% of families carry c.1285delC or c.1285dupC "in the polycytosine tract in exon 11, which is a mutational hot spot" (PMID:20301695). In the NCI cohort, "Exon 11 was the most frequent site of mutation representing 47% (24/51) of the BHDS families." (PMID:18234728), and Schmidt et al. found "Mutations were located along the entire length of the coding region, including 16 insertion/deletion, 3 nonsense, and 3 splice-site mutations." (PMID:15852235). In 297 Asian probands: "These variants consisted of duplications (46.4%), deletions (29.0%), substitutions (7.1%), insertions (0.7%), deletions-insertions (0.3%), large genomic deletions (4.0%), and variants affecting splicing (12.5%)." (PMID:37490463). In 120 Chinese probands the c.1285delC/dupC hotspot accounted for "25.0% (30/120)", truncating variants "a total frequency of 87.5% (105/120)", and missense/in-frame variants 11.7% (PMID:35637701). Intragenic deletions: "We identified six unique intragenic deletions in nine patients from six different BHDS families" (PMID:21412933); large deletions with "All deletion breakpoints are located in Alu repeats." (PMID:25807935); promoter/rare deletion events in "14/234, 6%" of families (PMID:40253282). A LOVD-based count cited in 2026 was 693 germline pathogenic FLCN mutations (PMID:42206645).

**Variant classification.** Missense variants are hard to interpret: "the vast majority of the identified missense variants are reported as variants of unknown significance (VUSs) (ClinVar database access March 2023: 787 missense variants, 688 uncertain" (PMID:39085584). A 2026 systematic review "identified a total of 29 pathogenic/likely pathogenic missense variants" (PMID:42206645). Functionally studied missense variants include H255Y (failed to rescue kidney phenotype in mice) and K508R (partial rescue) (PMID:28007907), Q201P with tumour second hit (PMID:35691222), and H255R expressed in UOK257 cells (PMID:20573232). VUSs "should be assessed according to international guidelines (e.g. ACMG/AMP)" (PMID:39085584).

**Allele frequency / population data.** For the Swedish founder splice variant c.779+1G>T, "According to population databases (gnomAD) this variant has a carrier frequency of 5/64548 in Europe and of these 4 are of Swedish origin." (PMID:35176117). Gene-level carrier frequencies are in Section 9 (1 in 2,654 in gnomAD v4, PMID:41896555; 1 in 2,710–4,190 in UK cohorts, PMID:40210444).

**Germline vs somatic.** BHD is caused by germline variants; renal tumours acquire somatic second hits. "Sequence alterations were detected in the majority of renal tumors (41 of 77, 53%), with loss of heterozygosity at the BHD locus in a minority of additional tumors (14 of 77, 17%)." (PMID:15956655). LOH is mostly copy-neutral: "Most of the loss of heterozygosity was because of uniparental disomy." (PMID:26776076). In contrast, "LOH cannot be detected in fibrofolliculomas from three patients" (PMID:17124507), and "no somatic variants or loss of heterozygosity has been detected in either skin [7] or pulmonary lesions" (PMID:37490463), suggesting haploinsufficiency in skin/lung. Somatic FLCN mutations also occur in sporadic tumours: "Somatic frameshift mutations in the FLCN exon 11 C(8) mononucleotide tract were detected in 23% of sporadic colorectal cancers with microsatellite instability" (PMID:20522427); somatic BHD mutations are rare in sporadic renal tumours (PMID:12907635); somatic FLCN variants occurred in 2 of 16 parathyroid carcinomas/atypical tumours (PMID:36935552).

**Functional consequence.** Loss of function (haploinsufficiency in skin/lung; biallelic loss in renal tumours). Mouse homozygous null alleles are embryonic lethal (PMID:19850877). No gain-of-function or dominant-negative mechanism has been established.

**Modifier genes.** None established. Chromatin-remodelling gene variants occur in BHD tumours ("17/29 tumors, 59%"; PMID:29767721) but are tumour-level co-alterations, not germline modifiers.

**Epigenetics.** FLCN promoter methylation was found in "11 of 39 (28%) sporadic renal tumors" (PMID:12907635), but "No evidence of FLCN promoter methylation was demonstrated." in pneumothorax/lung-cyst patients (PMID:26398834). No BHD-specific ENCODE/Roadmap analyses were found.

**Chromosomal abnormalities.** BHD is not caused by aneuploidy or translocation. FLCN lies within the 17p11.2 region; large intragenic/exonic deletions account for a few percent of variants (PMID:37490463; PMID:21412933). BHD renal tumours show copy-number changes distinct from sporadic tumours (PMID:29767721), and "All 3 occult syndromic cases demonstrated multiple chromosome losses and gains not seen in the 5 sporadic neoplasms." (PMID:40321032).

## 5. Environmental Information

BHD has no environmental, toxic, radiation, occupational or infectious cause. Relevant non-genetic factors are modifiers of manifestations only: smoking (discouraged; "Patients with BHD syndrome should avoid smoking" per the Chinese consensus, PMID:37670643; experimental FLCN depletion by cigarette smoke, PMID:35301243), barometric exposures (flying in unpressurised aircraft, piloting, diving; PMID:39085584; per-flight 0.63% and per-dive 0.33% pneumothorax risk, PMID:27652079), and medical radiation from repeated CT surveillance, which GeneReviews flags as a reason to prefer MRI (PMID:20301695). No infectious agent is involved. No association with diet, alcohol or exercise has been reported (not available).

## 6. Mechanism / Pathophysiology

**Ordered causal chain** (evidence type in brackets; "inferred" marks steps not directly demonstrated in humans):

1. A germline heterozygous loss-of-function FLCN variant (mostly truncating; exon 11 C8 hotspot) **results in** reduced folliculin dosage in all cells [human genetic; PMID:12204536; PMID:39085584].
2. Reduced folliculin **leads to** loss of the FLCN–FNIP1/FNIP2 GTPase-activating (GAP) activity toward RagC/RagD at the lysosomal surface [in vitro/structural; PMID:24095279; PMID:31704029; PMID:31672913].
3. *Branch A – kidney (two-hit):* A somatic second hit (frameshift or copy-neutral LOH) in renal tubular epithelium **results in** complete FLCN loss [human tumours; PMID:15956655; PMID:26776076].
4. Loss of RagC/D GAP activity **prevents** mTORC1-dependent phosphorylation of TFEB/TFE3, which — "unlike other substrates of mTORC1, such as S6K and 4E-BP1" — depends on RagC/RagD activation [in vitro/mouse; PMID:32612235; PMID:24081491].
5. Unphosphorylated TFEB/TFE3 **translocate** to the nucleus and constitutively activate lysosomal/autophagy and metabolic gene programmes (e.g., GPNMB) [cells, mouse kidney, human tumours; PMID:21209915; PMID:40321032].
6. Constitutive TFEB (and TFE3) activity **leads to** renal tubular hyperproliferation, cystogenesis and paradoxical TFEB-dependent mTORC1 hyperactivity: "constitutive activation of TFEB is the main driver of the kidney abnormalities and mTORC1 hyperactivity in a mouse model of Birt-Hogg-Dubé syndrome", and "depletion of TFEB in kidneys of these mice fully rescued the disease phenotype and associated lethality" (PMID:32612235); a nephron-specific Flcn/Tfeb double knockout likewise reversed most kidney phenotypes (PMID:40499782) [mouse], in parallel with increased mitochondrial biogenesis/oxidative metabolism through AMPK–PGC-1α [mouse/cells; PMID:24762438; PMID:23150719; PMID:25775561].
7. These changes, plus additional chromosomal and chromatin-remodelling alterations, **result in** hybrid oncocytic/chromophobe renal tumours (oncocytic = mitochondria-rich, consistent with step 6) that are multifocal and bilateral [human; PMID:12459621; PMID:29767721; PMID:37182269]; tumours with TFEB amplification or MITF alteration can metastasise [human; PMID:42315013].
8. *Branch B – lung (haploinsufficiency, inferred):* FLCN haploinsufficiency in alveolar epithelium and mesenchyme **is proposed to lead to** weakened cell–cell adhesion (FLCN–PKP4–E-cadherin) and reduced mesenchymal Wnt signalling via TFE3 [mouse/cells; PMID:26877139; PMID:31272105; PMID:32238524].
9. Respiration-induced cyclic stretch at points of weak pleural/septal anchorage **is hypothesised to result in** periacinar, subpleural, basal cysts (stretch hypothesis; not directly demonstrated) [human histology + hypothesis; PMID:26877139; PMID:24393238].
10. Rupture of subpleural cysts **leads to** spontaneous pneumothorax; larger cyst size/volume predicts pneumothorax [human; PMID:17322109; PMID:30673341].
11. *Branch C – skin (haploinsufficiency, inferred):* FLCN haploinsufficiency in hair follicle epithelium/perifollicular mesenchyme **is associated with** fibrofolliculoma formation without detectable LOH; the downstream mechanism is not established [human; PMID:17124507; PMID:37490463].

**Molecular pathways.** *Rag–mTORC1–MiT/TFE axis.* "We identify FLCN and its binding partners, FNIP1/2, as Rag-interacting proteins with GAP activity for RagC/D, but not RagA/B." (PMID:24095279). "FLCN regulates lysosome function by promoting the mTORC1-dependent phosphorylation and cytoplasmic sequestration of transcription factor EB (TFEB)." (PMID:24081491). TFEB "is phosphorylated by mTORC1 via a substrate-specific mechanism that is mediated by Rag GTPases." and "This mechanism has a crucial role in Birt-Hogg-Dubé syndrome" (PMID:32612235). "FLCN GAP activity on the Rags is required for the recruitment of mTORC1 and the transcriptional factors TFEB and TFE3 on the lysosome, where mTORC1 phosphorylates and inactivates these factors." (PMID:33981707). "Increased TFE3 activity is a downstream event induced by FLCN inactivation and is likely to be important for renal tumor development." (PMID:21209915). The ERN guideline summarises: "Biallelic FLCN inactivation leads to activation of the mTOR pathway in some contexts [6], although FLCN is implicated in additional cellular processes. A key role in the regulation of mTORC1 in kidney cells with FLCN inactivation is played by TFEB" (PMID:39085584). The direction of mTORC1 change has been contested: kidney-specific knockouts show Akt–mTOR activation (PMID:18182616; PMID:18974783), whereas "downregulation of BHD reduces the phosphorylation of ribosomal protein S6" in cultured cells (PMID:19234517), and bhd-null fission yeast suggests Bhd activates TOR (PMID:17556368); the substrate-specific model reconciles much of this (PMID:32612235). In TSC2-null cells, an mTORC1 feedback loop impairs lysosomal FLCN:FNIP2 recruitment, "resulting in unexpected TFEB hypophosphorylation and activation upon feeding" (PMID:36357396).

*Structural biology (protein dysfunction).* Cryo-EM of the lysosomal folliculin complex (FLCN, FNIP2, RagA-GDP:RagC-GTP, Ragulator) showed that "The RagC-GAP activity of FLCN was inhibited within the LFC, owing to displacement of a catalytically required arginine in FLCN from the RagC nucleotide." (PMID:31672913); a parallel structure identified the catalytic arginine finger (PMID:31704029). In the active complex, "FLCN reorients by 90°, breaks contact with RagA, and makes previously unseen contacts with RagC that position its Arg164 finger for catalysis." (PMID:36103527). Truncating BHD mutants lose FNIP binding: C-terminally truncated FLCN mutants cannot bind FNIP2 (PMID:18403135).

*AMPK and metabolism.* "The tumor suppressor folliculin regulates AMPK-dependent metabolic transformation." (PMID:24762438). "Muscle-targeted FLCN knockout mice underwent a pronounced metabolic shift toward oxidative phosphorylation" (PMID:23150719). In C. elegans, flcn-1 loss causes AMPK-dependent glycogen accumulation and "glycogen accumulates in kidneys from mice lacking FLCN and in renal tumors from a BHD patient" (PMID:26439621). Salivary-gland Flcn loss causes "metabolic reprogramming towards the pentose phosphate pathway" (PMID:31806376). BHD tumours show "Increased mitochondrial DNA (mtDNA) copy number with fewer variants" (PMID:37182269).

*Primary cilia, Wnt and TGF-β.* "FLCN is a ciliary protein that functions through primary cilia to regulate mTORC1." (PMID:27072130); ciliary localisation via a kinesin-2-binding motif is "required for its functions in mTOR regulation and tumor suppression" (PMID:33064845). FLCN loss reduces canonical Wnt signalling via TFE3, with "a 2.8-fold decrease in Wnt2" (PMID:31272105). Re-expression of FLCN in UOK257 cells altered TGF-β pathway genes (PMID:20573232).

**Cellular processes.** Lysosome biogenesis and autophagy (TFEB/TFE3 targets), mitochondrial biogenesis, cell proliferation (renal tubule), cell–cell adhesion (lung; hypothesis), alveolar development/maintenance ("Mesenchymal Flcn is an essential regulator during alveolar development and maintenance"; PMID:32238524). Suggested GO biological process terms (citations/onto-gocl-go-terms.md): regulation of TORC1 signaling (GO:1903432); positive regulation of GTPase activity (GO:0043547; Rag GAP); cellular response to amino acid stimulus (GO:0071230); lysosome organization (GO:0007040); autophagy (GO:0006914); mitochondrion organization (GO:0007005); negative regulation of cell population proliferation (GO:0008285); cilium assembly (GO:0060271); canonical Wnt signaling pathway (GO:0060070); cell-cell adhesion (GO:0098609). Existing GO annotations for human FLCN (UniProtKB Q8NFG4) are listed in citations/onto-gocl-uniprot-quickgo-q8nfg4.md.

**Immune involvement.** Not a primary feature. Lung cysts lack inflammation: "The BHDS cysts abutted on interlobular septa (88.2%) and had intracystic septa (13.6%) or protruding venules (39.5%) without cell proliferation or inflammation." (PMID:24393238). Fnip1 has immune-cell roles in mice (noted but not saved; not available). A BHD-associated epithelioid angiomyolipoma responded to checkpoint blockade (PMID:42527032), which says nothing about pathogenesis.

**Tissue damage mechanisms.** Lung: cyst enlargement and rupture; "The number of cysts diminished logarithmically and the proportion of cysts with inflammation increased as their individual sizes became greater (P < 0.05)." (PMID:24393238); cyst lining cells "stained positive for phospho-S6 ribosomal protein expression, suggesting activation of the mTOR pathway." (PMID:22441547). Kidney: neoplastic replacement and nephron loss after surgery.

**Molecular profiling.** *Transcriptomics:* "RNA-seq analysis revealed that BHD-associated renal tumours and sporadic renal tumours have totally different expression profiles." (PMID:37182269). *Genomics/CNV:* "BHD-associated kidney cancer displays unique molecular characteristics that are completely different from sporadic kidney cancer" (PMID:29767721). *Single-cell:* FLCN-mutated tumours contain "four distinct L1CAM-/FOXI1+ and two L1CAM+/FOXI1- cell populations that showed GPNMB overexpression" (PMID:40253282); L1CAM and LINC01187 are "expressed mutually exclusively in a unique checkered pattern in BHD-associated HOTs" (PMID:37994665). *Spatial transcriptomics:* "Spatial transcriptomic analysis identified distinct gene expression signatures in L1CAM+ and FOXI1+ FMT compartments independent of the local tumor compositions." (PMID:42754233). *Proteomics/metabolomics:* salivary-gland proteomics and metabolite profiling (PMID:31806376); redox metabolic reprogramming in tumours (PMID:29767721). *Lipidomics:* not available. *Functional genomic screens (CRISPR/RNAi):* no BHD-specific screen retrieved (not available).

**Cell types (suggested CL terms; citations/onto-gocl-cl-terms.md).** Kidney: renal intercalated cell (CL:0005010) and renal principal cell (CL:0005009) (tumour compartments FOXI1+ and L1CAM+; PMID:40253282; PMID:42754233), epithelial cell of proximal tubule (CL:0002306; model; PMID:26083655), kidney loop of Henle epithelial cell (CL:1000909; PMID:40499782). Lung: pulmonary alveolar type 2 cell (CL:0002063; cyst lining; PMID:22441547), fibroblast of lung (CL:0002553; PMID:32238524). Skin: hair follicle cell (CL:0002559), fibroblast (CL:0000057) (fibrofolliculoma stroma; PMID:26334087).

## 7. Anatomical Structures Affected

**Organ level.** Primary: skin (face, neck, upper trunk), lung, kidney (PMID:39085584). Secondary: pleura (pneumothorax), parotid gland (oncocytomas; PMID:29971177), possibly colon (polyps; PMID:36849229). Body systems: integumentary, respiratory, urinary/renal; possibly digestive and endocrine (unconfirmed). Suggested UBERON terms (citations/onto-gocl-uberon-terms.md): skin of face (UBERON:1000021); skin of neck (UBERON:0001417); lung (UBERON:0002048); lower lobe of lung (UBERON:0008949); pleura (UBERON:0000977); kidney (UBERON:0002113); renal tubule (UBERON:0009773); parotid gland (UBERON:0001831); colon (UBERON:0001155).

**Tissue and cell level.** Skin: hair follicle and perifollicular connective tissue; biopsies show "multiple anastomosing strands of 2-4 epithelial cells that emanate from a central aberrant hair follicle and frequently are continuous with sebaceous glands" (PMID:26334087). Lung: alveolar parenchyma; cysts "lined by epithelial cells, sometimes with a predominance of type II pneumocyte-like cuboidal cells" (PMID:22441547); "BHDS cysts are likely to develop in the periacinar region" (PMID:24393238). Kidney: distal-nephron epithelium (intercalated/principal cell signatures in tumours; PMID:42754233).

**Subcellular level.** Lysosomal surface (FLCN–FNIP–Rag–Ragulator complex; PMID:24081491; PMID:31672913), cytosol (amino-acid-starvation-dependent relocalisation), nucleus (TFEB/TFE3 translocation; PMID:21209915), primary cilium (PMID:27072130), mitochondria (biogenesis; PMID:23150719). Suggested GO cellular component terms (citations/onto-gocl-go-terms.md): lysosomal membrane (GO:0005765); cytosol (GO:0005829); nucleus (GO:0005634); cilium (GO:0005929); mitochondrion (GO:0005739).

**Localisation and lateralisation.** Lung cysts are bilateral, basal, subpleural and paramediastinal: "The majority of cysts were located in the basal lung fields below the level of the carina." (PMID:36028846); "the cysts tend to be basilar, subpleural and lentiform" (PMID:26877139). Renal tumours are often bilateral and multifocal ("Renal tumors can be bilateral and multifocal"; PMID:20301695). Skin lesions are symmetric, centrofacial early (PMID:20301695).

## 8. Temporal Development

**Onset.** Adult onset for most manifestations, with insidious skin and renal onset and acute pneumothorax events. Orphanet onset classes: Adolescent, Adult, Childhood, Elderly (https://www.orpha.net/en/disease/detail/122). Skin lesions appear between the second and fourth decades (PMID:20301695); median age at first pneumothorax ~34 years (range 7–78) (PMID:39085584); RCC "occurs after age 20 years with a median age of diagnosis of 46 years", the earliest case at 14 years (PMID:39085584). Lung cyst onset age is unknown (PMID:20301695).

**Progression.** Chronic, lifelong, slowly progressive. Skin lesions increase in number and size with age (PMID:20301695). Pneumothorax risk declines in later adulthood ("In most individuals the risk of pneumothorax decreases in later adulthood"; PMID:20301695) yet "The risk of a spontaneous pneumothorax in BHD syndrome is lifelong" (PMID:39085584); patients with multiple pneumothoraces present younger than those with one (mean 29.7 vs 38.9 years; PMID:39085584). Lung function is stable over 6 years (PMID:32448321) and over 2 years in a Danish cohort ("there were no significant declines in FEV1 and FVC"; PMID:39823110), although a longitudinal CT study reported that "pulmonary function had slightly deteriorated by longitudinal follow-up PFT" (PMID:37221571). Renal predisposition is lifelong; tumours grow slowly — "Growth rate analysis of 132 masses showed a growth rate of 0.04 cm per year" (PMID:41307675) — enabling the 3-cm surveillance strategy (PMID:23703644). There is no formal staging system for BHD itself; renal tumours are staged by standard RCC staging.

**Patterns.** No spontaneous remission. Treatment-induced control is local (surgery/ablation; pleurodesis). Critical periods: renal surveillance from age 20 (PMID:39085584); diagnostic delay is long — "The average delay in diagnosis was 7.6 years after initial symptoms." (PMID:39300538), with median 6 years when pneumothorax is the first feature (PMID:39085584). The first pneumothorax is a key window for diagnosis (PMID:36028846).

## 9. Inheritance and Population

**Inheritance, penetrance and expressivity.** BHD is inherited as an autosomal dominant trait (PMID:39085584; https://www.orpha.net/en/disease/detail/122), and its penetrance is age-dependent and incomplete for each organ (Section 3; PMID:36849229). For the kidney, Houweling et al. reported that "The estimated penetrance for renal cancer and pneumothorax was 16% (95% minimal confidence interval: 6–26%)" (PMID:22146830). Genotype-first population cohorts point to lower penetrance than family-based series: in the Geisinger MyCode cohort "P/LP truncating FLCN variants were identified in 35 individuals (1 in 3,234 unrelated individuals)", and only 2.9% had kidney cancer (PMID:35639097), while in UK Biobank "the lifetime risk of renal cancer was significantly lower in UKB than in BHDS patients (1% vs 32.1%)." (PMID:40210444). Expressivity is variable, including within a single family ("Disease severity can vary significantly even within the same family."; PMID:20301695).

**Anticipation, de novo variants, mosaicism and consanguinity.** Genetic anticipation has not been reported, which is consistent with the absence of a repeat-expansion mechanism. The de novo rate and the frequency of germline mosaicism have not been quantified, but de novo variants are documented: Menko et al. wrote "We identified a de novo FLCN mutation, c.499C>T (p.Gln167X), in a patient who presented with spontaneous pneumothorax", while judging that "Probably, de novo FLCN mutations are rare" (PMID:23264078). In a Chinese cohort, 37% of patients had no family history (PMID:39300538), which reflects de novo events, non-penetrance in relatives or incomplete family information. Consanguinity plays no role in this dominant disorder. Homozygous loss is presumed lethal, based on early embryonic lethality in homozygous null mice (PMID:19850877) and possible homozygous lethality in dogs (PMID:14532326).

**Epidemiology.** Orphanet records a European point prevalence average of 0.5 per million, range 1-9 / 1 000 000 (https://www.orpha.net/en/disease/detail/122); the guideline notes "A widely quoted figure is 1 in 200,000" but that genomic studies suggest FLCN LoF variants are "around fortyfold higher" (PMID:39085584). Bayesian estimation from pneumothorax epidemiology gave "a prevalence of BHD in the general population of 1.86 (1.16, 3.00) per million" (PMID:33987191). Korea: 5.67 per 10 million population (PMID:35666727). Genotype-based: "the frequency of clinically validated loss-of-function FLCN variants is 1 in 2710 to 4190." (PMID:40210444); gnomAD v4: "the carrier frequency of truncating FLCN variants is 1 in 2654." (PMID:41896555). Incidence data: not available.

**Founder effects and geography.** Finland: "92% of all identified deleterious FLCN variants in the Finnish population are c.1285dup, which suggests that c.1285dup is a founder mutation in this population." (PMID:41896555), with a Finnish carrier frequency of 1 in 614 (PMID:41896555). Sweden: "The most common variant among families was the splicing variant c.779+1G>T that was found in 57% (44 of 78) of the families" (PMID:35176117). China: "This report documents the first identification of founder mutations in FLCN" (Alu-mediated deletions; PMID:25807935), and a ΔE9–14 large deletion with founder effect (PMID:35637701). Phenotype differs by ancestry: East Asian cohorts report more lung and fewer skin/renal manifestations (pneumothorax 74.7%, skin 36.7%, RCC 7.2% in 166 East Asian patients; PMID:33313181); the Chinese consensus states "skin and renal lesions appear to be less common in Chinese subjects than those reported from European and American countries" (PMID:37670643); pneumothorax prevalence was higher in East Asian than North American/European cohorts (PMID:34267338). Ascertainment bias contributes.

**Sex ratio and age distribution.** No sex difference in the Bayesian estimate ("without difference between genders"; PMID:33987191), but several cohorts are female-predominant: "Among these 166 patients, 100 (60.2%) were females." (PMID:33313181); Korea 57.7% female (PMID:35666727); MyCode "Variant-positive participants were 62.9% female" (PMID:35639097). Renal tumour risk is similar by sex (19% vs 21% by 70; PMID:36849229). Women were diagnosed promptly less often than men (1.3% vs 11.4%; PMID:35875814). Median age at diagnosis in Korea was 51 (PMID:35666727).

## 10. Diagnostics

**Clinical criteria.** European BHD Consortium criteria, adopted by ERN GENTURIS: a clinical diagnosis can be made with "one major criterion ( >5 fibrofolliculomas or trichodiscomas, at least one histologically confirmed, of adult onset) or two minor criteria (1. Lung: bilateral basally located pulmonary cysts with no other apparent cause; 2. Kidney: early onset ( <50 years), multifocal or bilateral renal cancer, or renal cancer of mixed chromophobe and oncocytic histology; or 3. Family history: a first-degree relative with BHD syndrome) are present." (PMID:39085584). The guideline attributes these criteria to the European BHD Consortium (PMID:19959076). "A definitive diagnosis of BHD syndrome should be made when a genetic test is positive for a constitutive pathogenic/likely pathogenic variant in FLCN." (PMID:39085584). Indications to consider/test include primary spontaneous pneumothorax (testing if recurrent and/or familial), multiple bilateral lower-zone cysts, bilateral/multifocal renal neoplasia, familial or early-onset (≤45 years) RCC, and multiple fibrofolliculomas (PMID:39085584).

**Genetic testing.** "Sequence analysis of FLCN is performed first" and "If no variant is detected by the sequencing method used, the next step is to perform gene-targeted deletion/duplication analysis to detect exon and whole-gene deletions or duplications." (PMID:20301695). Sequencing detects ~88%–96% and deletion/duplication analysis <8% (PMID:20301695); "The FLCN mutation detection rate by bidirectional DNA sequencing in the National Cancer Institute BHDS cohort was 88%." (PMID:21412933). Multigene panels (hereditary RCC or pneumothorax panels) are most common in practice ("most testing is performed as part of a multigene panel"; PMID:39085584); exome/genome sequencing are options and may detect CNVs with lower sensitivity (PMID:20301695). In RCC cohorts, "Genes with the most frequent germline mutations were FLCN (n = 10, 3.1%)" (PMID:38127826); a population RCC panel found a P/LP variant in 1.7% (PMID:39272843). In apparent primary spontaneous pneumothorax, "Three patients were found to have a pathogenic variant in the FLCN gene (3.4%)." (PMID:36028846); in Japanese patients with cysts/pneumothorax "An FLCN germline mutation was found in 23 (63.9%) of the 36 patients" (PMID:20413710). CMA, karyotype, FISH, mtDNA and repeat-expansion testing have no routine role (not applicable), although MLPA/qPCR/targeted arrays detect intragenic deletions (PMID:20301695). Predictive testing in minors is generally deferred until 18 (PMID:39085584).

**Imaging.** HRCT is the key lung test; "Lung ultrasound should not be used as a diagnostic test for pulmonary cysts" (PMID:39085584). "Chest CT scan is the most informative noninvasive diagnostic modality to identify DCLDs." (PMID:39168181); "The number, shape, size, and distribution of the lung cysts can help to differentiate BHD syndrome from other diffuse cystic lung diseases." (PMID:28830849). Renal surveillance: MRI preferred; ultrasound misses small tumours: "Nine small tumours (7-27 mm) were visible on MRI or CT and not detected using ultrasound." (PMID:30845233).

**Functional tests.** Lung function is usually normal apart from "slightly increased residual volume and reduced carbon monoxide transfer factor (DLCO)"; routine testing is not required in asymptomatic patients (PMID:39085584; PMID:32448321). Electrophysiology: not applicable.

**Biopsy/pathology.** Skin biopsy confirms fibrofolliculoma (histology in Section 7; PMID:26334087), though "nowadays genetic testing can offer an alternative route to diagnosis" (PMID:39085584). Lung biopsy is not first-line (PMID:37670643); BHD lungs show "punch-out cysts with no inflammation, and lacked subpleural fibroelastotic scars and smoking changes" (PMID:24168179). Renal tumour immunohistochemistry: "GPNMB was an excellent immunohistochemistry screen showing diffuse positivity in all c-FMT" (PMID:42315013), GPNMB being "a downstream marker of TFE3/TFEB pathway activation" (PMID:40321032).

**Biomarkers / omics diagnostics.** No circulating biomarker exists. Tissue biomarkers: GPNMB, L1CAM/LINC01187 patterns (PMID:37994665). Liquid biopsy, metabolomic and epigenomic diagnostics: not available.

**Differential diagnosis.** Lymphangioleiomyomatosis (LAM, sporadic or TSC-associated): "Features atypical for BHDS are an even distribution of cysts throughout the lung, dyspnea on exertion, hemoptysis, and chylothorax." (PMID:20301695); BHD cysts are more irregular, lower and peripheral (PMID:30673341; PMID:21550193). Pulmonary Langerhans cell histiocytosis (smoking-related, nodules) and lymphoid interstitial pneumonia (PMID:20301695; PMID:39168181; PMID:37670643). Tuberous sclerosis complex (angiofibromas, LAM), Cowden syndrome (PTEN), multiple familial trichoepithelioma (CYLD), familial multiple discoid fibromas, hereditary leiomyomatosis and RCC (FH; usually solitary aggressive tumours), VHL, hereditary papillary RCC (MET), BAP1 and SDHx syndromes (PMID:20301695; PMID:39085584). Smoking-related pneumothorax/emphysema: bullae are apical whereas BHD cysts are basal (PMID:39085584).

**Screening.** No newborn or population screening. Cascade testing of first-degree adult relatives is recommended (PMID:39085584).

## 11. Outcome/Prognosis

**Survival and mortality.** No life-table study exists. The NCI PDQ summary states that among 70 BHD patients with renal tumours, "5 (7%) reportedly died from metastatic RCC" and that with surveillance "their life expectancy should not be significantly different from that of matched individuals in the general population." (https://www.cancer.gov/publications/pdq/information-summaries/genetics/bhd-syndrome-hp-pdq). In the NIH series, "Patients with BHD are at risk for multiple renal tumors that are often malignant and can metastasize." (PMID:15821464). Among 115 Dutch carriers, "Five symptomatic patients developed metastatic disease." (PMID:22146830); in a French series "Four cases had metastatic disease, although none died of it." (PMID:25519458). In a US single-centre cohort of 149 patients, all-cause mortality appeared shorter in those with renal tumours (log-rank P = 0.02), "though no deaths were from cancer or cancer-related complications." (PMID:39354434). The 3-cm rule is not absolute: a 2.8-cm chromophobe RCC was followed six years later by omental metastases, "the first report of metastasized chromophobe RCC, after complete resection of a primary tumor smaller than 3 cm, in a patient with BHD" (PMID:38900222).

**Morbidity and function.** Pneumothorax recurrence is the main morbidity (ipsilateral recurrence 73% in multiple-event patients; PMID:28248571). Lung function: "lung function parameters did not significantly decline over a follow-up period of 6" years (PMID:32448321). Nephron loss from repeated renal interventions (eGFR decrease 10.7 mL/min/1.73m² after ablation in one series; PMID:31302073). Skin QoL as in Section 3 (PMID:21054573). Psychosocial burden: "A diagnosis of BHD syndrome may be associated with psychological challenges and socioeconomic hardships" (PMID:39085584); patients share "multiple non-medical ramifications ranging from economic and physical insecurity to interruptions in familial communication patterns and relationships" (PMID:23179794).

**Complications.** Recurrent pneumothorax; metastatic RCC; chronic kidney disease after nephron loss; possible associated neoplasms. Colorectal cancer is contested: "The patients with BHDS showed a moderately but significantly increased rate of colorectal cancer (5.1% versus 1.5%, p-value .0068)." (PMID:34000505); a Swedish register study reported "a fivefold increase in risk of colorectal cancer (adjusted HR 5.44, 95% CI 2.74-10.81) and an almost threefold risk of malignant melanoma (adjusted HR 2.67, 95% CI 1.17-6.07)" (PMID:41193855), although its authors caution that "Further research is needed to validate the colorectal cancer association and assess its implications for screening and management." (PMID:41193855); a Dutch registry study concluded "Our data do not provide evidence for an increased risk for colorectal carcinoma in Birt-Hogg-Dubé syndrome, arguing against the need for colorectal surveillance." (PMID:31857718), and Zbar et al. found "Colon cancer and colon polyps were not related to the Birt-Hogg-Dubé syndrome." (PMID:11927500). The guideline concludes "Currently there is not sufficient evidence of an increased risk for other tumours" (PMID:39085584). Thyroid: "TCs are rare in BHD." (PMID:40658617). Parotid: "Bilateral multifocal parotid oncocytomas have been reported in eight patients with BHD." (https://www.cancer.gov/publications/pdq/information-summaries/genetics/bhd-syndrome-hp-pdq).

**Prognostic factors.** "Older age and male sex were predictive of renal tumor development" (PMID:39354434). Renal tumour size (3 cm threshold; PMID:23703644), histology (clear cell/papillary and TFEB/MITF-altered tumours more aggressive; PMID:42315013; https://www.cancer.gov/publications/pdq/information-summaries/genetics/bhd-syndrome-hp-pdq), cyst size/number for pneumothorax (PMID:30673341; PMID:39085584), timely diagnosis and surveillance compliance (PMID:30845233). Prognostic molecular biomarkers: TFEB amplification/MITF p.E318K in metastatic non-conventional tumours (PMID:42315013) — preliminary.

## 12. Treatment

**Renal tumours (surgical/interventional).** "Surgical intervention should usually be performed when the largest renal tumour reaches 3 cm in diameter." and "Nephron-sparing surgery should ideally be performed whenever possible, with percutaneous thermal ablation being an alternative." (PMID:39085584). Tumours "should be followed with interval imaging studies until the largest tumor reaches 3 cm in maximal diameter, at which point nephron-sparing surgery should be ideally pursued." (PMID:23703644). Thermal ablation series: "Technical success was achieved in all ablation sessions (primary success rate, 100%)." and "No local tumor progression was observed during a median follow-up period of 74 months" (PMID:36291753); a second series of 29 RCCs also reported "No local tumor progression was found." (PMID:31302073). Suggested NCIT (citations/onto-ncit-nci-thesaurus-procedures.md): Partial Nephrectomy (NCIT:C51928); Radiofrequency Ablation (NCIT:C15666); Cryosurgery (NCIT:C15215); Patient Observation (NCIT:C15722, for active surveillance).

**Systemic therapy for metastatic RCC.** "There are no proven systemic therapy options for BHD to date." (NCT02504892). The everolimus trial NCT02504892 was terminated ("Study was terminated due to slow, insufficient accrual.") with "Stable Disease: 3 (participants)" (NCT02504892). Case-level evidence: sequential "sunitinib, axitinib, everolimus, bevacizumab and pazopanib" in a slowly progressive metastatic patient (PMID:25519458); progression on ipilimumab+nivolumab in a young patient with metastatic clear cell RCC ("At the end of 4 cycles, imaging showed progressive disease, so treatment was discontinued."; PMID:33482948); partial response to anlotinib plus toripalimab in sarcomatoid BHD-RCC (PMID:40707936); durable complete pathologic response of an epithelioid angiomyolipoma to ipilimumab plus nivolumab (PMID:42527032). Preclinical rationale for mTOR inhibition: rapamycin "led to extended survival and inhibited further progression of cystogenesis" in kidney-specific knockout mice (PMID:18974783) and "Treatment of knockout mice with the mTOR inhibitor rapamycin for 10 months led to the suppression of tumor growth." (PMID:26083655). Suggested NCIT (citations/onto-ncit-nci-thesaurus-drugs.md): Everolimus (NCIT:C48387); Sirolimus (NCIT:C1212); Sunitinib (NCIT:C71622); Axitinib (NCIT:C38718); Pazopanib (NCIT:C74547); Nivolumab (NCIT:C68814); Ipilimumab (NCIT:C2654); Toripalimab (NCIT:C131334); Catequentinib (NCIT:C138997, the retrieved NCIT concept for the anlotinib-related agent). Suggested CHEBI: sirolimus (CHEBI:9168); everolimus (CHEBI:68478) (citations/onto-ncit-chebi-sirolimus-everolimus.md).

**Skin.** "Therapeutic management is available with standard dermatological approaches, including shave excison, punch excision, ablative electrosurgery [52] and laser therapy" and "Treatment is not curative and may need to be repeated." (PMID:39085584). A review of 17 articles found "Randomized controlled trials were absent" and "Recurrence varied from 3 to 48 months." (PMID:40331668). Topical rapamycin 0.1% in a split-face RCT (NCT00928798): "No change in cosmetic status of fibrofolliculomas was reported in the majority of cases for the rapamycin treated (79% by doctors, 53% by patients) as well as the placebo treated facial sides (both 74%)." and "This study provides no evidence that treatment of fibrofolliculomas with topical rapamycin in BHD results in cosmetic improvement." (PMID:24910976). Suggested NCIT: Laser Therapy (NCIT:C15466) (citations/onto-ncit-nci-thesaurus-procedures.md); Sirolimus (NCIT:C1212, topical use investigational and ineffective).

**Lung.** "Treatment of pneumothorax in BHD syndrome does not differ from that of pneumothorax for other reasons." and surgery (VATS, chemical or mechanical pleurodesis, pleurectomy or total pleural covering) "should be considered in case of recurrent pneumothorax" (PMID:39085584). The Chinese consensus recommends "early pleurodesis" (PMID:37670643). "In LAM and BHDS, total pleural covering has shown favorable outcomes" (PMID:42232039). Suggested NCIT: Pleurodesis (NCIT:C66899); Video-Assisted Thoracic Surgery (NCIT:C63704); Thoracoscopic Surgery (NCIT:C15726) (citations/onto-ncit-nci-thesaurus-procedures.md).

**Advanced therapeutics.** Gene therapy, cell therapy, RNA therapies: none (not available). Targeted: TFEB/TFE3 inhibition is preclinical — TFEB and TFE3 "are the main drivers of the kidney phenotypes observed in mouse models" (PMID:42816660); "Emerging therapeutic approaches targeting mTOR signaling, metabolic pathways, and transcriptional regulators show promising results in preclinical models" (PMID:42810013). Pharmacogenomics: not applicable.

**Clinical studies (NCT).** NCT02504892 (everolimus, terminated), NCT00928798 (topical rapamycin, completed), NCT03040115 (air-travel safety survey), NCT02916992 (BHD prevalence in pneumothorax), NCT06330324 (reproductive options in inherited skin diseases, not BHD-specific).

**Treatment strategy.** Lifelong multidisciplinary surveillance with a named coordinating clinician; renal intervention at 3 cm; pneumothorax treated conventionally with surgical prevention of recurrence; elective skin ablation for QoL (PMID:39085584).

## 13. Prevention

**Primary prevention.** The disease itself cannot be prevented except through reproductive choices. The Chinese consensus states that "Couples with BHD syndrome are advised to undergo prenatal genetic counseling when preparing for pregnancy" (PMID:37670643), and the use of prenatal and preimplantation testing is being studied in inherited skin diseases more broadly (NCT06330324). There is no immunisation, public-health, environmental or prophylactic-drug intervention for BHD.

**Secondary prevention (surveillance and early detection).** Renal surveillance is the core of secondary prevention. The ERN GENTURIS guideline states that "Surveillance for renal cell carcinoma should be started at age 20.", that it "should be conducted every 1–2 years" and that it "should be lifelong", preferably by MRI (PMID:39085584). GeneReviews advises annual MRI from age 20, or earlier when a relative had a renal tumour before 30, and screening every 2 years after 2–3 normal MRIs in people without such a family history (PMID:20301695). Stamatakis et al. instead recommend "abdominal imaging every 36 months in individuals without renal lesions" (PMID:23703644). The European BHD Consortium summarised that "Preventive measures are aimed mainly at early diagnosis and treatment of renal cancer." (PMID:19959076). A baseline HRCT may be offered from diagnosis, "but not usually to asymptomatic patients before 20 years of age" (PMID:39085584). Colorectal, thyroid, salivary and melanoma screening should follow population or family-history guidance only (PMID:39085584).

**Tertiary prevention and behavioural advice.** Pleurodesis after pneumothorax reduces recurrence (Section 12), and nephron-sparing surgery or ablation preserves renal function. Patients are advised to avoid smoking and to seek specialist advice before working as a pilot, flying in unpressurised aircraft or diving. The ERN guideline states that "Flights on commercial airlines are generally safe" (PMID:39085584), whereas the Chinese consensus states "Air travel is not recommended for patients with BHD syndrome who have experienced pneumothorax until it has been recovered." (PMID:37670643).

**Genetic counselling.** Genetic counselling (NCIT:C15240 Genetic Counseling) should cover cascade testing of first-degree relatives, so that relatives who test negative can be released from surveillance. Predictive testing is usually deferred until age 18 unless the result would change management (PMID:39085584).

## 14. Other Species / Natural Disease

**Dog (Canis lupus familiaris; German Shepherd Dog).** "Hereditary multifocal renal cystadenocarcinoma and nodular dermatofibrosis (RCND) is a naturally occurring canine kidney cancer syndrome that was originally described in German Shepherd dogs." Lingaas et al. described "a disease-associated mutation in exon 7 of canine BHD that leads to the mutation of a highly conserved amino acid of the encoded protein." (PMID:14532326). RCND comprises bilateral multifocal kidney tumours, uterine leiomyomas and dermal collagen nodules, paralleling human BHD (renal tumours plus skin fibrous lesions); lung involvement is not described in the retrieved abstract (PMID:14532326). OMIA records the trait as OMIA:001335-9615 (autosomal dominant), caused by "an A>G base substitution in exon 7 of the BHD (folliculin) gene" leading to an "H255R amino-acid substitution in a highly conserved region", and lists a candidate 9092-bp FLCN deletion in a Chihuahua (citations/species-omia-001335-9615-rcnd-dog.md; https://omia.org/OMIA001335/9615/). Breed: German Shepherd Dog, VBO:0200577 (citations/species-vbo-0200577-german-shepherd-dog.md). Canine tumours also follow the two-hit model: "Second hits with predicted functional implications for the wild-type FLCN allele were observed in 12 of 17 (71%) of the kidney tumor samples." (PMID:18219524), and FLCN LOH was found in early cystic lesions of 6–8-week-old puppies (PMID:19387735). Veterinary relevance: breed-specific inherited cancer in German Shepherds; dog NCBI Taxonomy 9615.

**Rat (Rattus norvegicus; Nihon rat).** A spontaneous Sprague-Dawley-derived strain: "The Nihon rat is an example of a Mendelian dominantly inherited predisposition for development of RCs like the Eker (Tsc2 gene mutant) rat." with a germline insertion "resulting in a frameshift and producing a stop codon 26 aa downstream" (PMID:14769940); it also shows extrarenal lesions (PMID:16447066).

**Orthologues and conservation.** Folliculin is "highly conserved among species" (PMID:18234728). Orthologues: mouse Flcn, rat Bhd/Flcn, dog FLCN, zebrafish flcn (PMID:27391801), Drosophila DBHD/Flcn (PMID:23799055), C. elegans flcn-1 (PMID:26439621), budding yeast Lst7 with its FNIP orthologue Lst4 ("Lst7, the yeast folliculin orthologue"; PMID:26631379), and fission yeast bhd (PMID:17556368). NCBI Gene IDs (citations/species-ncbi-gene-flcn-orthologs.md): human FLCN 201163; mouse Flcn 216805; rat Flcn 303185; dog FLCN 479529; zebrafish flcn 678628; Drosophila BHD 38793; C. elegans flcn-1 174134; S. cerevisiae LST7 852948; S. pombe bhd1 2540297. NCBI Taxonomy IDs (citations/species-ncbi-taxonomy-flcn-ortholog-species.md): Homo sapiens 9606, Mus musculus 10090, Rattus norvegicus 10116, Canis lupus familiaris 9615, Danio rerio 7955, Drosophila melanogaster 7227, Caenorhabditis elegans 6239, Saccharomyces cerevisiae 4932 (S288C 559292), Schizosaccharomyces pombe 4896. **Zoonotic potential / transmission:** not applicable.

## 15. Model Organisms

**Mouse.** *Germline Flcn knockout:* homozygous null mice "displayed early embryonic lethality at E5.5-E6.5"; heterozygotes "developed kidney cysts and solid tumors as they aged (median kidney-lesion-free survival = 23 months, median tumor-free survival = 25 months)" (PMID:19850877) — good recapitulation of renal two-hit tumorigenesis, but no skin or lung phenotype reported. *Kidney-specific (Ksp-Cre) knockouts:* "BHD(flox/flox)/Ksp-Cre mice developed enlarged kidneys characterized by polycystic kidneys, hyperplasia, and cystic renal cell carcinoma." (PMID:18974783); "Homozygous loss of BHD may initiate renal tumorigenesis in the mouse." (PMID:18182616) — early lethality limits tumour modelling. *Proximal-tubule (Sglt2-Cre) knockout:* tumours mostly chromophobe RCC under 1 year (PMID:26083655). *Nephron-specific (Six2-Cre) knockout with Tfe3/Tfeb double knockouts:* "Although the double Flcn/Tfe3 knockout only ameliorated the glomerular cysts, the double Flcn/Tfeb knockout largely reversed most of the phenotypes along the entire nephron." (PMID:40499782). *Fnip1/Fnip2:* "Heterozygous Fnip1/homozygous Fnip2 double-knockout mice developed kidney cancer at 24 mo of age, analogous to the heterozygous Flcn knockout mouse model" (PMID:25775561). *Missense BAC transgenics:* "Flcn H255Y mutant transgene expression in kidney-targeted Flcn knockout mice did not rescue the multi-cystic kidney phenotype." (PMID:28007907). *Lung:* "Deletion of Flcn in mesoderm-derived mesenchymal cells results in significant reduction of postnatal alveolar growth and subsequent alveolar destruction, leading to cystic lesions." (PMID:32238524). *Muscle:* oxidative shift (PMID:23150719). *Salivary gland:* metabolic reprogramming (PMID:31806376).

**Rat.** Nihon rat (above; PMID:14769940; PMID:16447066). **Dog.** RCND (PMID:14532326). **Zebrafish.** Morpholino knockdown suggests "zebrafish flcn is expressed in a non-uniform manner and is likely required for the maintenance of correct cell cycle regulation during embryonic development." (PMID:27391801) — developmental only. **Drosophila.** "Our work provides a new animal model of the BHD syndrome"; "the human FLCN could partially rescue the DBHD(-) phenotypes" (PMID:23799055). **C. elegans.** flcn-1 mutants: AMPK-dependent glycogen accumulation and stress resistance (PMID:26439621). **Yeast.** Lst7/Lst4 complex relocates to the vacuolar membrane on starvation (PMID:26631379); S. pombe bhd deletion (PMID:17556368).

**Cellular models.** UOK257 FLCN-null renal tumour line from a BHD patient: "tumor development was inversely dependent upon the level of wild-type FLCN expression" (PMID:20573232). Patient iPSC line CMCi009-A, "derived from peripheral blood mononuclear cells (PBMCs) of a 42-year-old woman" (PMID:33540282). HEK293T overexpression systems for missense variants (PMID:42206645).

**Limitations.** Mice reproduce renal cysts/tumours but not fibrofolliculomas; the lung model is mesenchymal-only; homozygous loss is embryonic lethal; complete kidney knockouts die early of renal failure, and cell-line results on mTORC1 direction conflict with in vivo data (PMID:19234517; PMID:18974783). **Resources:** MGI gene record MGI:2442184 (Flcn; NCBI Gene 216805) lists 27 alleles (targeted 7, gene-trapped 12, endonuclease-mediated 7, chemically induced 1), including Flcn<tm1.1Lss> (MGI:3774416), and 41 IMSR strains/lines (citations/species-mgi-2442184-flcn-mouse-marker-alleles.md).

## Open Questions

Several questions remain unresolved in the evidence. First, the true penetrance of FLCN loss-of-function variants: genotype-first cohorts (UK Biobank, MyCode) show far lower renal and skin penetrance than family-based clinical cohorts, and it is unclear whether incidentally detected carriers need the same surveillance (PMID:40210444; PMID:35639097; PMID:39085584). Second, the mechanism of lung cyst formation remains a hypothesis — "Critical questions remain." (PMID:26877139) — and why skin and lung lesions arise without a detectable second hit is unexplained (PMID:17124507). Third, the association with colorectal cancer and melanoma is contested (PMID:41193855; PMID:31857718). Fourth, the optimal renal surveillance interval (annual vs every 2–3 years) and the comparative effectiveness of ablation versus partial nephrectomy lack trial data (PMID:39085584). Fifth, no systemic therapy is proven for metastatic BHD RCC, and TFEB/TFE3-directed therapy is preclinical (NCT02504892; PMID:42816660). Sixth, the reasons for apparent ancestry-related differences in phenotype (more lung, less skin/renal involvement in East Asian cohorts) are unresolved and may reflect ascertainment (PMID:33313181; PMID:37670643). Finally, missense FLCN variants remain mostly VUSs, and validated functional assays are needed (PMID:39085584).

## References

- PMID:11927500 Zbar B et al. 2002. Risk of renal and colonic neoplasms and spontaneous pneumothorax in the Birt-Hogg-Dubé syndrome. evidence: citations/kidney-zbar-2002-renal-colonic-neoplasms.md
- PMID:1200700 Hornstein OP et al. 1975. Perifollicular fibromatosis cutis with polyps of the colon--a cutaneo-intestinal syndrome sui generis. evidence: citations/info-hornstein-1975-perifollicular-fibromatosis-colon-polyps.md
- PMID:12204536 Nickerson ML et al. 2002. Mutations in a novel gene lead to kidney tumors, lung wall defects, and benign tumors of the hair follicle in patients with the Birt-Hogg-Dubé syndrome. evidence: citations/genetics-nickerson-2002-novel-gene-folliculin.md
- PMID:12459621 Pavlovich CP et al. 2002. Renal tumors in the Birt-Hogg-Dubé syndrome. evidence: citations/kidney-pavlovich-2002-renal-tumors-bhd.md
- PMID:12907635 Khoo SK et al. 2003. Inactivation of BHD in sporadic renal tumors. evidence: citations/omics-khoo-2003-bhd-sporadic-renal-tumors.md
- PMID:14532326 Lingaas F et al. 2003. A mutation in the canine BHD gene is associated with hereditary multifocal renal cystadenocarcinoma and nodular dermatofibrosis in the German Shepherd dog. evidence: citations/models-lingaas-2003-canine-bhd-mutation-german-shepherd.md
- PMID:14769940 Okimoto K et al. 2004. A germ-line insertion in the Birt-Hogg-Dubé (BHD) gene gives rise to the Nihon rat model of inherited renal cancer. evidence: citations/models-okimoto-2004-germ-line-insertion-nihon-rat.md
- PMID:15821464 Pavlovich CP et al. 2005. Evaluation and management of renal tumors in the Birt-Hogg-Dubé syndrome. evidence: citations/kidney-pavlovich-2005-evaluation-management-renal.md
- PMID:15852235 Schmidt LS et al. 2005. Germline BHD-mutation spectrum and phenotype analysis of a large cohort of families with Birt-Hogg-Dubé syndrome. evidence: citations/genetics-schmidt-2005-germline-mutation-spectrum.md
- PMID:15956655 Vocke CD et al. 2005. High frequency of somatic frameshift BHD gene mutations in Birt-Hogg-Dubé-associated renal tumors. evidence: citations/omics-vocke-2005-somatic-frameshift-bhd-renal-tumors.md
- PMID:16447066 Kouchi M et al. 2006. Natural history of the Nihon (Bhd gene mutant) rat, a novel model for human Birt-Hogg-Dubé syndrome. evidence: citations/models-kouchi-2006-natural-history-nihon-rat.md
- PMID:17124507 van Steensel MA et al. 2007. Novel mutations in the BHD gene and absence of loss of heterozygosity in fibrofolliculomas of Birt-Hogg-Dubé patients. evidence: citations/genetics-vansteensel-2007-novel-bhd-mutations-no-loh.md
- PMID:17322109 Toro JR et al. 2007. Lung cysts, spontaneous pneumothorax, and genetic associations in 89 families with Birt-Hogg-Dubé syndrome. evidence: citations/epi-toro-2007-lung-cysts-89-families.md
- PMID:17556368 van Slegtenhorst M et al. 2007. The Birt-Hogg-Dube and tuberous sclerosis complex homologs have opposing roles in amino acid homeostasis in Schizosaccharomyces pombe. evidence: citations/models-vanslegtenhorst-2007-bhd-tsc-homologs-pombe.md
- PMID:18182616 Baba M et al. 2008. Kidney-targeted Birt-Hogg-Dube gene inactivation in a mouse model: Erk1/2 and Akt-mTOR activation, cell hyperproliferation, and polycystic kidneys. evidence: citations/models-baba-2008-kidney-targeted-bhd-inactivation.md
- PMID:18219524 Bønsdorff TB et al. 2008. Second hits in the FLCN gene in a hereditary renal cancer syndrome in dogs. evidence: citations/species-bonsdorff-2008-second-hits-flcn.md
- PMID:18234728 Toro JR et al. 2008. BHD mutations, clinical and molecular genetic investigations of Birt-Hogg-Dubé syndrome: a new series of 50 families and a review of published reports. evidence: citations/genetics-toro-2008-bhd-mutations-50-families.md
- PMID:18403135 Hasumi H et al. 2008. Identification and characterization of a novel folliculin-interacting protein FNIP2. evidence: citations/mechanism-gene-2008-novel-folliculin-interacting-protein.md
- PMID:18974783 Chen J et al. 2008. Deficiency of FLCN in mouse kidney led to development of polycystic kidneys and renal neoplasia. evidence: citations/models-chen-2008-flcn-mouse-kidney-polycystic.md
- PMID:19234517 Hartman TR et al. 2009. The role of the Birt-Hogg-Dubé protein in mTOR activation and renal tumorigenesis. evidence: citations/models-hartman-2009-bhd-protein-mtor-activation.md
- PMID:19387735 Bønsdorff TB et al. 2009. Loss of heterozygosity at the FLCN locus in early renal cystic lesions in dogs with renal cystadenocarcinoma and nodular dermatofibrosis. evidence: citations/species-bonsdorff-2009-loh-flcn-locus-early-cystic.md
- PMID:19785621 Kluger N et al. 2010. Birt-Hogg-Dubé syndrome: clinical and genetic studies of 10 French families. evidence: citations/skin-kluger-2010-bhd-10-french-families.md
- PMID:19850877 Hasumi Y et al. 2009. Homozygous loss of BHD causes early embryonic lethality and kidney tumor development with activation of mTORC1 and mTORC2. evidence: citations/models-hasumi-2009-homozygous-loss-bhd-embryonic.md
- PMID:19959076 Menko FH et al. 2009. Birt-Hogg-Dube syndrome: diagnosis and management. evidence: citations/info-menko-2009-birt-hogg-dube-diagnosis-management.md
- PMID:20301695 Elke C Sattler et al. 2024. Birt-Hogg-Dubé Syndrome. evidence: citations/diagnosis-sattler-2006-genereviews-birt-hogg-dube.md
- PMID:20413710 Kunogi M et al. 2010. Clinical and genetic spectrum of Birt-Hogg-Dube syndrome patients in whom pneumothorax and/or multiple lung cysts are the presenting feature. evidence: citations/lung-kunogi-2010-clinical-genetic-spectrum.md
- PMID:20522427 Nahorski MS et al. 2010. Investigation of the Birt-Hogg-Dube tumour suppressor gene (FLCN) in familial and sporadic colorectal cancer. evidence: citations/prognosis-nahorski-2010-flcn-familial-sporadic-colorectal.md
- PMID:20573232 Hong SB et al. 2010. Tumor suppressor FLCN inhibits tumorigenesis of a FLCN-null renal cancer cell line and regulates expression of key molecules in TGF-beta signaling. evidence: citations/models-hong-2010-flcn-null-renal-cell-line-uok257.md
- PMID:21054573 Kluger N et al. 2011. How much disability is caused by fibrofolliculomas during Birt-Hogg-Dubé Syndrome?. evidence: citations/prognosis-kluger-2011-disability-fibrofolliculomas-qol.md
- PMID:21209915 Hong SB et al. 2010. Inactivation of the FLCN tumor suppressor gene induces TFE3 transcriptional activity by increasing its nuclear localization. evidence: citations/mechanism-hong-2010-flcn-inactivation-tfe3-nuclear.md
- PMID:21412933 Benhammou JN et al. 2011. Identification of intragenic deletions and duplication in the FLCN gene in Birt-Hogg-Dubé syndrome. evidence: citations/genetics-benhammou-2011-intragenic-deletions-flcn.md
- PMID:21550193 Tobino K et al. 2012. Differentiation between Birt-Hogg-Dubé syndrome and lymphangioleiomyomatosis: quantitative analysis of pulmonary cysts on computed tomography of the chest in 66 females. evidence: citations/diagnosis-tobino-2012-bhd-vs-lam-quantitative-ct.md
- PMID:22146830 Houweling AC et al. 2011. Renal cancer and pneumothorax risk in Birt-Hogg-Dubé syndrome; an analysis of 115 FLCN mutation carriers from 35 BHD families. evidence: citations/kidney-houweling-2011-renal-cancer-pneumothorax.md
- PMID:22441547 Furuya M et al. 2012. Pulmonary cysts of Birt-Hogg-Dubé syndrome: a clinicopathologic and immunohistochemical study of 9 families. evidence: citations/lung-furuya-2012-pulmonary-cysts-clinicopathologic.md
- PMID:22581760 Happle R 2012. Hornstein-Birt-Hogg-Dube syndrome: a renaming and reconsideration. evidence: citations/info-happle-2012-hornstein-birt-hogg-dube-renaming.md
- PMID:23150719 Hasumi H et al. 2012. Regulation of mitochondrial oxidative metabolism by tumor suppressor FLCN. evidence: citations/omics-hasumi-2012-mitochondrial-oxidative-metabolism-flcn.md
- PMID:23179794 Middelton LA 2013. Birt-Hogg-Dubé: beyond the clinical manifestations. evidence: citations/prognosis-middelton-2013-beyond-clinical-manifestations.md
- PMID:23264078 Menko FH et al. 2013. A de novo FLCN mutation in a patient with spontaneous pneumothorax and renal cancer; a clinical and molecular evaluation. evidence: citations/clinical2-menko-2013-de-novo-flcn-pneumothorax.md
- PMID:23703644 Stamatakis L et al. 2013. Diagnosis and management of BHD-associated kidney cancer. evidence: citations/kidney-stamatakis-2013-diagnosis-management-kidney-cancer.md
- PMID:23799055 Liu W et al. 2013. Genetic characterization of the Drosophila birt-hogg-dubé syndrome gene. evidence: citations/models-liu-2013-genetic-characterization-drosophila-bhd.md
- PMID:24081491 Petit CS et al. 2013. Recruitment of folliculin to lysosomes supports the amino acid-dependent activation of Rag GTPases. evidence: citations/mechanism-petit-2013-folliculin-lysosome-rag.md
- PMID:24095279 Tsun ZY et al. 2013. The folliculin tumor suppressor is a GAP for the RagC/D GTPases that signal amino acid levels to mTORC1. evidence: citations/mechanism-tsun-2013-folliculin-gap-ragc-ragd.md
- PMID:24168179 Fabre A et al. 2014. Distinguishing the histological and radiological features of cystic lung disease in Birt-Hogg-Dubé syndrome from those of tobacco-related spontaneous pneumothorax. evidence: citations/diagnosis-fabre-2014-bhd-vs-tobacco-pneumothorax.md
- PMID:24393238 Kumasaka T et al. 2014. Characterization of pulmonary cysts in Birt-Hogg-Dubé syndrome: histopathological and morphometric analysis of 229 pulmonary cysts from 50 unrelated patients. evidence: citations/lung-kumasaka-2014-229-pulmonary-cysts.md
- PMID:24762438 Yan M et al. 2014. The tumor suppressor folliculin regulates AMPK-dependent metabolic transformation. evidence: citations/mechanism-2014-folliculin-ampk-metabolic.md
- PMID:24910976 Gijezen LM et al. 2014. Topical Rapamycin as a Treatment for Fibrofolliculomas in Birt-Hogg-Dubé Syndrome: A Double-Blind Placebo-Controlled Randomized Split-Face Trial. evidence: citations/skin-gijezen-2014-topical-rapamycin-split-face.md
- PMID:24994497 Johannesma PC et al. 2014. Spontaneous pneumothorax as indicator for Birt-Hogg-Dubé syndrome in paediatric patients. evidence: citations/clinical2-johannesma-2014-spontaneous-pneumothorax-paediatric.md
- PMID:25519458 Benusiglio PR et al. 2014. Renal cell tumour characteristics in patients with the Birt-Hogg-Dubé cancer susceptibility syndrome: a retrospective, multicentre study. evidence: citations/kidney-benusiglio-2014-renal-cell-tumour-characteristics.md
- PMID:25775561 Hasumi H et al. 2015. Folliculin-interacting proteins Fnip1 and Fnip2 play critical roles in kidney tumor suppression in cooperation with Flcn. evidence: citations/models-hasumi-2015-fnip1-fnip2-kidney-tumor-suppression.md
- PMID:25807935 Ding Y et al. 2015. FLCN intragenic deletions in Chinese familial primary spontaneous pneumothorax. evidence: citations/genetics-ding-2015-flcn-intragenic-deletions-chinese.md
- PMID:26083655 Chen J et al. 2015. Disruption of tubular Flcn expression as a mouse model for renal tumor induction. evidence: citations/models-chen-2015-disruption-tubular-flcn-renal-tumor.md
- PMID:26334087 Schmidt LS et al. 2015. Molecular genetics and clinical features of Birt-Hogg-Dubé syndrome. evidence: citations/omics-schmidt-2015-molecular-genetics-clinical-bhd-review.md
- PMID:26398834 Ding Y et al. 2015. Promoter methylation is not associated with FLCN irregulation in lung cyst lesions of primary spontaneous pneumothorax. evidence: citations/omics-ding-2015-promoter-methylation-flcn-lung-cyst.md
- PMID:26439621 Possik E et al. 2015. FLCN and AMPK Confer Resistance to Hyperosmotic Stress via Remodeling of Glycogen Stores. evidence: citations/models-possik-2015-flcn-ampk-hyperosmotic-stress.md
- PMID:26631379 Pacitto A et al. 2015. Lst4, the yeast Fnip1/2 orthologue, is a DENN-family protein. evidence: citations/models-pacitto-2015-lst4-yeast-fnip-orthologue.md
- PMID:26776076 Iribe Y et al. 2016. Genome-Wide Uniparental Disomy and Copy Number Variations in Renal Cell Carcinomas Associated with Birt-Hogg-Dubé Syndrome. evidence: citations/omics-iribe-2016-genome-wide-uniparental-disomy-cnv-bhd-rcc.md
- PMID:26877139 Kennedy JC et al. 2016. Mechanisms of pulmonary cyst pathogenesis in Birt-Hogg-Dube syndrome: The stretch hypothesis. evidence: citations/lung-kennedy-2016-stretch-hypothesis.md
- PMID:27072130 Zhong M et al. 2016. Tumor Suppressor Folliculin Regulates mTORC1 through Primary Cilia. evidence: citations/mechanism-yan-2016-folliculin-mtorc1-primary-cilia.md
- PMID:27391801 Kenyon EJ et al. 2016. Expression and knockdown of zebrafish folliculin suggests requirement for embryonic brain morphogenesis. evidence: citations/models-kenyon-2016-zebrafish-folliculin-brain-morphogenesis.md
- PMID:27652079 Johannesma PC et al. 2016. Risk of spontaneous pneumothorax due to air travel and diving in patients with Birt-Hogg-Dubé syndrome. evidence: citations/treatment-johannesma-2016-air-travel-diving-pneumothorax.md
- PMID:28007907 Hasumi H et al. 2017. H255Y and K508R missense mutations in tumour suppressor folliculin (FLCN) promote kidney cell proliferation. evidence: citations/models-hasumi-2017-h255y-k508r-flcn-kidney-proliferation.md
- PMID:28248571 Gupta N et al. 2017. Spontaneous Pneumothoraces in Patients with Birt-Hogg-Dubé Syndrome. evidence: citations/lung-gupta-2017-spontaneous-pneumothoraces.md
- PMID:28830849 Lee JE et al. 2017. Birt-Hogg-Dubé syndrome: characteristic CT findings differentiating it from other diffuse cystic lung diseases. evidence: citations/diagnosis-lee-2017-bhd-ct-findings.md
- PMID:28970150 Schmidt LS et al. 2018. FLCN: The causative gene for Birt-Hogg-Dubé syndrome. evidence: citations/mechanism-gene-2018-flcn-causative-gene-bhd.md
- PMID:29439288 Geilswijk M et al. 2018. Childhood pneumothorax in Birt-Hogg-Dubé syndrome: A cohort study and review of the literature. evidence: citations/clinical2-geilswijk-2018-childhood-pneumothorax-bhd.md
- PMID:29767721 Hasumi H et al. 2018. BHD-associated kidney cancer exhibits unique molecular characteristics and a wide variety of variants in chromatin remodeling genes. evidence: citations/omics-hasumi-2018-bhd-kidney-cancer-molecular-characteristics.md
- PMID:29971177 Yoshida K et al. 2018. Parotid Oncocytoma as a Manifestation of Birt-Hogg-Dubé Syndrome. evidence: citations/prognosis-yoshida-2018-parotid-oncocytoma-bhd.md
- PMID:30673341 Park HJ et al. 2019. Differentiation Between Lymphangioleiomyomatosis and Birt-Hogg-Dubé Syndrome: Analysis of Pulmonary Cysts on CT Images. evidence: citations/diagnosis-park-2019-lam-vs-bhd-ct.md
- PMID:30845233 Johannesma PC et al. 2019. Renal imaging in 199 Dutch patients with Birt-Hogg-Dubé syndrome: Screening compliance and outcome. evidence: citations/kidney-johannesma-2019-renal-imaging-199-dutch.md
- PMID:31272105 Kennedy JC et al. 2019. Loss of FLCN inhibits canonical WNT signaling via TFE3. evidence: citations/mechanism-2019-loss-flcn-wnt-tfe3.md
- PMID:31302073 Matsui Y et al. 2019. Percutaneous thermal ablation for renal cell carcinoma in patients with Birt-Hogg-Dubé syndrome. evidence: citations/treatment-matsui-2019-thermal-ablation-bhd-rcc.md
- PMID:31672913 Lawrence RE et al. 2019. Structural mechanism of a Rag GTPase activation checkpoint by the lysosomal folliculin complex. evidence: citations/mechanism-lawrence-2019-structural-rag-gtpase-checkpoint.md
- PMID:31704029 Shen K et al. 2019. Cryo-EM Structure of the Human FLCN-FNIP2-Rag-Ragulator Complex. evidence: citations/mechanism-shen-2019-cryoem-flcn-fnip2-rag-ragulator.md
- PMID:31806376 Isono Y et al. 2020. FLCN alteration drives metabolic reprogramming towards nucleotide synthesis and cyst formation in salivary gland. evidence: citations/omics-isono-2020-flcn-metabolic-reprogramming-salivary-gland.md
- PMID:31857718 van de Beek I et al. 2020. No evidence for increased prevalence of colorectal carcinoma in 399 Dutch patients with Birt-Hogg-Dubé syndrome. evidence: citations/prognosis-van-de-beek-2020-no-evidence-colorectal-carcinoma.md
- PMID:31923324 Happle R 2020. Hornstein-Knickenberg syndrome vs. Birt-Hogg-Dube syndrome: a critical review of an unjustified designation. evidence: citations/info-happle-2020-hornstein-knickenberg-vs-birt-hogg-dube.md
- PMID:32238524 Chu L et al. 2020. Mesenchymal folliculin is required for alveolar development: implications for cystic lung disease in Birt-Hogg-Dubé syndrome. evidence: citations/models-chu-2020-mesenchymal-folliculin-alveolar-development.md
- PMID:32448321 Daccord C et al. 2020. Lung function in Birt-Hogg-Dubé syndrome: a retrospective analysis of 96 patients. evidence: citations/treatment-daccord-2020-lung-function-bhd.md
- PMID:32612235 Napolitano G et al. 2020. A substrate-specific mTORC1 pathway underlies Birt-Hogg-Dubé syndrome. evidence: citations/mechanism-napolitano-2020-substrate-specific-mtorc1-bhd.md
- PMID:33064845 Zhang Y et al. 2021. Ciliary localization of folliculin mediated via a kinesin-2-binding motif is required for its functions in mTOR regulation and tumor suppression. evidence: citations/mechanism-2021-ciliary-folliculin-kinesin2.md
- PMID:33313181 Guo T et al. 2020. The clinical characteristics of East Asian patients with Birt-Hogg-Dubé syndrome. evidence: citations/epi-east-asian-2020-clinical-characteristics.md
- PMID:33482948 Boland J et al. 2020. Concurrent Birt-Hogg-Dubé Syndrome and Hereditary Paraganglioma-Pheochromocytoma Syndrome Presenting as Metastatic Renal Cell Carcinoma in a 25-Year-Old Man: A Case Report. evidence: citations/treatment-boland-2020-metastatic-rcc-bhd-case.md
- PMID:33540282 Ko EJ et al. 2021. Generation of the human induced pluripotent stem cell lines (CMCi009-A) from a patient with Birt-Hogg-Dubé syndrome (BHD) with heterozygous frameshift deletion mutation c.1285delC of the FLCN gene. evidence: citations/models-ko-2021-ipsc-line-cmci009-bhd.md
- PMID:33981707 Ramirez Reyes JMJ et al. 2021. Folliculin: A Regulator of Transcription Through AMPK and mTOR Signaling Pathways. evidence: citations/mechanism-review-2021-folliculin-transcription-ampk-mtor.md
- PMID:33987191 Muller ME et al. 2021. Prevalence of Birt-Hogg-Dubé Syndrome Determined Through Epidemiological Data on Spontaneous Pneumothorax and Bayes Theorem. evidence: citations/epi-muller-2021-prevalence-bayes-theorem.md
- PMID:34000505 Sattler EC et al. 2021. Colorectal cancer risk in families with Birt-Hogg-Dubé syndrome increased. evidence: citations/prognosis-sattler-2021-colorectal-cancer-risk-families.md
- PMID:34267338 Matsumoto K et al. 2021. A systematic review assessing the existence of pneumothorax-only variants of FLCN. Implications for lifelong surveillance of renal tumours. evidence: citations/lung-matsumoto-2021-pneumothorax-only-variants.md
- PMID:35125098 Yang J et al. 2022. Correlative analysis of lung CT findings in patients with Birt-Hogg-Dubé Syndrome and the occurrence of spontaneous pneumothorax: a preliminary study. evidence: citations/lung-yang-2022-correlative-lung-ct.md
- PMID:35176117 Lagerstedt-Robinson K et al. 2022. A retrospective two centre study of Birt-Hogg-Dubé syndrome reveals a pathogenic founder mutation in FLCN in the Swedish population. evidence: citations/genetics-lagerstedt-robinson-2022-swedish-founder-flcn.md
- PMID:35301243 Li X et al. 2023. Cigarette smoking is a secondary cause of folliculin loss. evidence: citations/lung-li-2023-cigarette-smoking-folliculin.md
- PMID:35637701 Zhou W et al. 2022. Clinical and Genetic Comparison of Birt-Hogg-Dubé Syndrome (Hornstein-Knickenberg Syndrome) in Chinese: A Systemic Review of Reported Cases. evidence: citations/genetics-zhou-2022-chinese-bhd-systematic-review.md
- PMID:35639097 Savatt JM et al. 2022. Frequency of truncating FLCN variants and Birt-Hogg-Dubé-associated phenotypes in a health care system population. evidence: citations/epi-savatt-2022-truncating-flcn-health-care.md
- PMID:35666727 Park HJ et al. 2022. Epidemiology and clinical features of Birt-Hogg-Dubé syndrome: A nationwide population-based study in South Korea. evidence: citations/epi-park-2022-nationwide-korea-epidemiology.md
- PMID:35691222 Sano T et al. 2022. A novel missense mutation in the folliculin gene associated with the renal tumor-only phenotype of Birt-Hogg-Dubé syndrome. evidence: citations/genetics-sano-2022-flcn-missense-q201p-renal.md
- PMID:35875814 Steinlein OK et al. 2022. Delayed diagnosis of Birt-Hogg-Dubé syndrome might be aggravated by gender bias. evidence: citations/diagnosis-steinlein-2022-delayed-diagnosis-bhd.md
- PMID:36028846 Sriram JD et al. 2022. Birt-Hogg-Dubé syndrome in apparent primary spontaneous pneumothorax patients; results and recommendations for clinical practice. evidence: citations/lung-sriram-2022-bhd-apparent-psp.md
- PMID:36103527 Jansen RM et al. 2022. Structural basis for FLCN RagC GAP activation in MiT-TFE substrate-selective mTORC1 regulation. evidence: citations/mechanism-jansen-2022-flcn-ragc-gap-mit-tfe.md
- PMID:36291753 Bodard Sylvain et al. 2022. Percutaneous Thermal Ablation for Renal Tumors in Patients with Birt–Hogg–Dubé Syndrome. evidence: citations/treatment-bodard-2022-percutaneous-thermal-ablation-bhd.md
- PMID:36357396 Asrani K et al. 2022. An mTORC1-mediated negative feedback loop constrains amino acid-induced FLCN-Rag activation in renal cells with TSC2 loss. evidence: citations/mechanism-asrani-2022-mtorc1-negative-feedback-flcn-rag.md
- PMID:36849229 Bruinsma FJ et al. 2023. Update of penetrance estimates in Birt-Hogg-Dubé syndrome. evidence: citations/kidney-bruinsma-2023-update-penetrance-estimates.md
- PMID:36935552 Jha S et al. 2023. Germline- and Somatic-Inactivating FLCN Variants in Parathyroid Cancer and Atypical Parathyroid Tumors. evidence: citations/genetics-jha-2023-flcn-parathyroid-cancer.md
- PMID:37182269 Jikuya R et al. 2023. Comparative analyses define differences between BHD-associated renal tumour and sporadic chromophobe renal cell carcinoma. evidence: citations/omics-jikuya-2023-comparative-analyses-bhd-chromophobe.md
- PMID:37221571 Cho SM et al. 2023. Progression of pulmonary cysts in Birt-Hogg-Dubé syndrome: longitudinal thoracic computed tomography study with quantitative assessment. evidence: citations/clinical2-cho-2023-progression-pulmonary-cysts-bhd.md
- PMID:37490463 Namba Y et al. 2023. Clinical and genetic features of 334 Asian patients with Birt-Hogg-Dubé syndrome (BHDS) who presented with pulmonary cysts with or without a history of pneumothorax, with special reference to BHDS-associated pneumothorax. evidence: citations/genetics-namba-2023-334-asian-patients-bhds.md
- PMID:37670643 Expert Consensus Group of the Expert Consensus on the Diagnosis and Management of Birt-Hogg-Dubé Syndrome et al. 2023. [Expert consensus on the diagnosis and management of Birt-Hogg-Dubé syndrome]. evidence: citations/diagnosis-expert-consensus-2023-bhd-china.md
- PMID:37994665 Wang XM et al. 2024. Hybrid Oncocytic Tumors (HOTs) in Birt-Hogg-Dubé Syndrome Patients-A Tale of Two Cities: Sequencing Analysis Reveals Dual Lineage Markers Capturing the 2 Cellular Populations of HOT. evidence: citations/omics-wang-2024-hybrid-oncocytic-tumors-bhd-sequencing.md
- PMID:38020174 Steinlein OK et al. 2023. Risk of pneumothorax in Birt-Hogg-Dubé syndrome during pregnancy and birth. evidence: citations/clinical2-steinlein-2023-pneumothorax-pregnancy-birth-bhd.md
- PMID:38127826 Nguyen CB et al. 2023. Pathogenic Germline Mutational Landscape in Patients With Renal Cell Carcinoma and Associated Clinicopathologic Features. evidence: citations/diagnosis-nguyen-2023-germline-rcc-landscape.md
- PMID:38900222 van Riel L et al. 2024. Metastatic disease after removal of a renal cell carcinoma smaller than 3 cm in a patient with Birt-Hogg-Dubé syndrome, a case report. evidence: citations/clinical2-van-riel-2024-metastatic-rcc-smaller-3cm.md
- PMID:39085584 Geilswijk M et al. 2024. ERN GENTURIS clinical practice guidelines for the diagnosis, surveillance and management of people with Birt-Hogg-Dubé syndrome. evidence: citations/kidney-ern-genturis-2024-bhd-guidelines.md
- PMID:39168181 Franciosi AN et al. 2025. Diffuse Cystic Lung Disease: A Clinical Guide to Recognition and Management. evidence: citations/diagnosis-franciosi-2025-diffuse-cystic-lung-disease.md
- PMID:39272843 Bruinsma F et al. 2024. Prevalence of Germline Pathogenic Variants in Renal Cancer Predisposition Genes in a Population-Based Study of Renal Cell Carcinoma. evidence: citations/diagnosis-bruinsma-2024-renal-cancer-predisposition-gene-panel.md
- PMID:39300538 Hu D et al. 2024. Clinical and genetic characteristics of 100 consecutive patients with Birt-Hogg-Dubé syndrome in Eastern Chinese region. evidence: citations/lung-zhang-2024-100-consecutive-chinese.md
- PMID:39354434 Kijlertsuphasri S et al. 2024. Diagnosis of renal tumors in Birt-Hogg-Dube syndrome: Clinical presentation and risk factors in a single-center retrospective cohort. evidence: citations/clinical2-kijlertsuphasri-2024-renal-tumors-diagnosis-bhd.md
- PMID:39823110 Holmager MM et al. 2025. Trends in pulmonary function in patients with Birt-Hogg-Dubé syndrome: a retrospective cohort study. evidence: citations/clinical2-holmager-2025-trends-pulmonary-function-bhd.md
- PMID:40210444 Yngvadottir B et al. 2025. Inherited predisposition to pneumothorax: estimating the frequency of Birt-Hogg-Dubé syndrome from genomics and population cohorts. evidence: citations/epi-yngvadottir-2025-pneumothorax-frequency-flcn.md
- PMID:40253282 Gupta S et al. 2025. Renal Neoplasia in Birt-Hogg-Dubé Syndrome: Integrated Histopathologic, Bulk, and Single-cell Transcriptomic Analysis. evidence: citations/omics-gupta-2025-renal-neoplasia-bhd-single-cell.md
- PMID:40321032 Argani P et al. 2025. Clinically Sporadic Folliculin -mutated Renal Epithelial Neoplasms Represent a Mixture of True Somatic Folliculin -mutated and Occult Birt-Hogg-Dubé Syndrome-associated Cases : Morphologic and Molecular Overlap With TSC/MTOR -mutated Eosinophilic Renal ﻿Neoplasms and MiT Family Translocation Renal Cell Carcinoma. evidence: citations/omics-argani-2025-clinically-sporadic-flcn-mutated-renal.md
- PMID:40331668 Fostier W et al. 2025. Cutaneous Fibrofolliculomas and Trichodiscomas in Birt-Hogg-Dubé Syndrome: A Review of Therapeutic Surgical Strategies. evidence: citations/treatment-fostier-2025-surgical-fibrofolliculoma-review.md
- PMID:40499782 Shalaby O et al. 2025. Folliculin Deletion in the Mouse Kidney Results in Cystogenesis of the Loops of Henle via Aberrant TFEB Activation. evidence: citations/models-shalaby-2025-flcn-deletion-loops-henle-tfeb.md
- PMID:40658617 Vaid S et al. 2025. Thyroid Carcinoma in Birt-Hogg-Dubé Syndrome: Case Series and Review of Literature. evidence: citations/prognosis-vaid-2025-thyroid-carcinoma-bhd-case-series.md
- PMID:40707936 Yi Liqi et al. 2025. Successful treatment of advanced Birt-Hogg-Dubé syndrome-associated renal cell carcinoma with sarcomatoid dedifferentiation using anlotinib combined with PD-1 inhibitor after first-line therapy failure: a case report. evidence: citations/treatment-yi-2025-anlotinib-sarcomatoid-bhd-rcc.md
- PMID:41193855 Skarin Nordenvall A et al. 2026. Risk of malignant melanoma and colorectal cancer in Birt-Hogg-Dubé syndrome - a matched cohort study. evidence: citations/prognosis-skarin-nordenvall-2026-melanoma-colorectal-bhds.md
- PMID:41307675 Golagha M et al. 2026. Birt-Hogg-Dubé: CT characteristics of renal tumors in a rare syndrome. evidence: citations/clinical2-golagha-2026-ct-renal-tumors-bhd.md
- PMID:41896555 Broniarek I et al. 2026. Genotype-based prevalence of Birt-Hogg-Dubé syndrome in the healthcare and genomic registry populations - breaking the 'rare disease' status?. evidence: citations/epi-marciniak-2026-genotype-based-prevalence.md
- PMID:42206645 Bai W et al. 2026. Novel FLCN mutations in Birt-Hogg-Dubé patients and potential intervention of FLCN mRNA. evidence: citations/genetics-bai-2026-novel-flcn-mutations-mrna.md
- PMID:42232039 Tsuboshima Kenji 2026. Surgical strategies for spontaneous pneumothorax: a narrative review. evidence: citations/treatment-tsuboshima-2026-surgical-strategies-spontaneous-pneumothorax.md
- PMID:42315013 Gupta S et al. 2026. A report of thirteen non-conventional FLCN-mutated (renal) tumors (FMT) and a discussion of proposed diagnostic criteria, convergent FLCN/TFEB and FLCN/MITF E318K signaling, and FLCN immunohistochemistry. evidence: citations/omics-gupta-2026-thirteen-nonconventional-flcn-tumors.md
- PMID:42527032 Viola Juliana et al. 2026. Complete response to dual immune checkpoint blockade in a patient with Birt-Hogg-Dubé syndrome and epithelioid angiomyolipoma. evidence: citations/treatment-viola-2026-immune-checkpoint-epithelioid-angiomyolipoma-bhd.md
- PMID:42754233 Wang XM et al. 2026. Disentangling the Cellular Composition of FLCN-Mutated Tumors in Birt-Hogg-Dubé Syndrome by Spatial Transcriptomics. evidence: citations/omics-wang-2026-spatial-transcriptomics-flcn.md
- PMID:42810013 Castañeda Pérez S et al. 2026. Birt-Hogg-Dubé syndrome: From molecular mechanisms to emerging systemic therapeutic strategies. evidence: citations/treatment-castaneda-perez-2026-systemic-therapeutic-strategies.md
- PMID:42816660 Ferniani M et al. 2026. Synergistic role of TFEB/TFE3 and mTORC1 in kidney cystogenesis and tumorigenesis. evidence: citations/treatment-ferniani-2026-tfeb-tfe3-mtorc1-kidney.md
- PMID:596896 Birt AR et al. 1977. Hereditary multiple fibrofolliculomas with trichodiscomas and acrochordons. evidence: citations/info-birt-1977-hereditary-multiple-fibrofolliculomas.md
- NCT00928798 ClinicalTrials.gov record 2010. Topical Rapamycin for Fibrofolliculomas (NCT00928798). evidence: citations/treatment-ctgov-nct00928798-topical-rapamycin-fibrofolliculomas.md
- NCT02504892 ClinicalTrials.gov record 2015. Everolimus Therapy in People With Birt-Hogg-Dube Syndrome (BHD)-Associated Kidney Cancer or Sporadic Chromophobe Renal Cancer (NCT02504892). evidence: citations/treatment-ctgov-nct02504892-everolimus-bhd-kidney-cancer.md
- NCT02916992 ClinicalTrials.gov record 2016. Prevalence of Spontaneous Pneumothorax in BHD (NCT02916992). evidence: citations/treatment-ctgov-nct02916992-pneumothorax-prevalence-bhd.md
- NCT03040115 ClinicalTrials.gov record 2015. Assessment of Safety of Air Travel in Patients With Birt-Hogg-Dube Syndrome (NCT03040115). evidence: citations/treatment-ctgov-nct03040115-air-travel-safety-bhd.md
- NCT06330324 ClinicalTrials.gov record 2024. Reproductive Options in Inherited Skin Diseases (NCT06330324). evidence: citations/treatment-ctgov-nct06330324-reproductive-options-inherited-skin.md
- https://id.nlm.nih.gov/mesh/D058249 National Library of Medicine (MeSH) 2011 (year introduced). Birt-Hogg-Dube Syndrome (MeSH descriptor D058249). evidence: citations/info-mesh-2011-birt-hogg-dube-syndrome-descriptor.md
- https://omia.org/OMIA001335/9615/ Nicholas FW et al. 2026. OMIA:001335-9615: Renal cystadenocarcinoma and nodular dermatofibrosis, FLCN-related in Canis lupus familiaris (dog). evidence: citations/species-omia-001335-9615-rcnd-dog.md
- https://purl.obolibrary.org/obo/MONDO_0800444 Mondo Disease Ontology n.d. (current release). MONDO:0800444 Birt-Hogg-Dube syndrome (OLS4 term record). evidence: citations/info-mondo-birt-hogg-dube-mondo-0800444.md
- https://www.cancer.gov/publications/pdq/information-summaries/genetics/bhd-syndrome-hp-pdq National Cancer Institute PDQ Cancer Genetics Editorial Board 2024 (updated 12/16/2024). Birt-Hogg-Dube Syndrome (PDQ) - Health Professional Version. evidence: citations/info-nci-pdq-2024-birt-hogg-dube-syndrome.md
- https://www.ncbi.nlm.nih.gov/gene/201163 NCBI Gene n.d. (current release). FLCN folliculin, NCBI Gene ID 201163 (esummary). evidence: citations/info-ncbi-gene-flcn-201163.md
- https://www.orpha.net/en/disease/detail/122 Orphanet n.d. (current release). ORDO:122 / ORPHA:122 Birt-Hogg-Dube syndrome (OLS4 term record, Orphanet cross-references). evidence: citations/info-orphanet-2024-ordo-122-birt-hogg-dube.md
- CL:0005010 EMBL-EBI Ontology Lookup Service (OLS4) 2026. Cell Ontology term records for kidney, lung, skin and hair follicle cell types. evidence: citations/onto-gocl-cl-terms.md
- GO:1903432 EMBL-EBI Ontology Lookup Service (OLS4) 2026. Gene Ontology term records for BHD/FLCN biological process and cellular component terms. evidence: citations/onto-gocl-go-terms.md
- UBERON:1000021 EMBL-EBI Ontology Lookup Service (OLS4) 2026. UBERON anatomy term records for skin, lung, pleura, kidney, renal tubule, parotid gland and colon. evidence: citations/onto-gocl-uberon-terms.md
- UniProtKB:Q8NFG4 UniProt Consortium 2026. Folliculin (FLCN_HUMAN, Q8NFG4) UniProt function and subcellular location text, with QuickGO GO annotations. evidence: citations/onto-gocl-uniprot-quickgo-q8nfg4.md
- OMIM:135150 Human Phenotype Ontology (HPO) consortium (annotations via Monarch/JAX ontology API) 2026. HPO disease-phenotype annotations for Birt-Hogg-Dube syndrome, OMIM:135150. evidence: citations/onto-hpo-bhd-annotations-omim-135150.md
- HP:0200063 Human Phenotype Ontology (HPO) consortium 2026. Human Phenotype Ontology term records: BHD colonic polyposis and salivary oncocytoma. evidence: citations/onto-hpo-colon-salivary.md
- HP:0000006 Human Phenotype Ontology (HPO) consortium 2026. Human Phenotype Ontology term records: inheritance and age of onset. evidence: citations/onto-hpo-inheritance-onset.md
- HP:0005584 Human Phenotype Ontology (HPO) consortium 2026. Human Phenotype Ontology term records: BHD renal phenotypes. evidence: citations/onto-hpo-kidney.md
- HP:0005948 Human Phenotype Ontology (HPO) consortium 2026. Human Phenotype Ontology term records: BHD lung cysts and pneumothorax. evidence: citations/onto-hpo-lung-pneumothorax.md
- HP:0030436 Human Phenotype Ontology (HPO) consortium 2026. Human Phenotype Ontology term records: BHD skin lesions. evidence: citations/onto-hpo-skin-lesions.md
- CHEBI:9168 NCI Thesaurus (NCIt) / ChEBI / HGNC / UniProt curators (ontology and database records) 2026. ChEBI entries: sirolimus (CHEBI:9168) and everolimus (CHEBI:68478). evidence: citations/onto-ncit-chebi-sirolimus-everolimus.md
- HGNC:27310 NCI Thesaurus (NCIt) / ChEBI / HGNC / UniProt curators (ontology and database records) 2026. HGNC records: FLCN (HGNC:27310), FNIP1 (HGNC:29418), FNIP2 (HGNC:29280). evidence: citations/onto-ncit-hgnc-flcn-fnip1-fnip2.md
- NCIT:C28244 NCI Thesaurus (NCIt) / ChEBI / HGNC / UniProt curators (ontology and database records) 2026. NCI Thesaurus concepts: Birt-Hogg-Dube Syndrome, Genetic Counseling, Folliculin. evidence: citations/onto-ncit-nci-thesaurus-bhd-genetic-counseling.md
- NCIT:C48387 NCI Thesaurus (NCIt) / ChEBI / HGNC / UniProt curators (ontology and database records) 2026. NCI Thesaurus concepts: everolimus, sirolimus, sunitinib, axitinib, pazopanib, nivolumab, ipilimumab, toripalimab, catequentinib (anlotinib-related). evidence: citations/onto-ncit-nci-thesaurus-drugs.md
- NCIT:C51928 NCI Thesaurus (NCIt) / ChEBI / HGNC / UniProt curators (ontology and database records) 2026. NCI Thesaurus concepts: partial nephrectomy, radiofrequency ablation, cryosurgery, video-assisted thoracic surgery, pleurodesis, laser therapy, patient observation (active surveillance), thoracoscopic surgery. evidence: citations/onto-ncit-nci-thesaurus-procedures.md
- UniProt:Q8NFG4 NCI Thesaurus (NCIt) / ChEBI / HGNC / UniProt curators (ontology and database records) 2026. UniProtKB/Swiss-Prot entry Q8NFG4 (FLCN_HUMAN) Folliculin, 579 aa. evidence: citations/onto-ncit-uniprot-flcn-q8nfg4.md
- MGI:2442184 Mouse Genome Informatics (The Jackson Laboratory) 2026. Flcn MGI Mouse Gene Detail - MGI:2442184 - folliculin (with mouse Flcn mutant allele records). evidence: citations/species-mgi-2442184-flcn-mouse-marker-alleles.md
- NCBI Gene:216805 NCBI 2026. NCBI Gene esummary records for FLCN orthologs (Mus musculus Flcn 216805, Rattus norvegicus Flcn 303185, Canis lupus familiaris FLCN 479529, Danio rerio flcn 678628, Drosophila melanogaster BHD 38793, C. elegans flcn-1 174134, S. cerevisiae LST7 852948, S. pombe bhd1 2540297, Homo sapiens FLCN 201163). evidence: citations/species-ncbi-gene-flcn-orthologs.md
- NCBI Taxonomy:10090 NCBI 2026. NCBI Taxonomy esummary records for species carrying FLCN orthologs (mouse 10090, rat 10116, dog 9615, zebrafish 7955, Drosophila 7227, C. elegans 6239, S. cerevisiae 4932 and strain S288C 559292, S. pombe 4896, human 9606). evidence: citations/species-ncbi-taxonomy-flcn-ortholog-species.md
- VBO:0200577 Monarch Initiative Vertebrate Breed Ontology contributors 2026. Vertebrate Breed Ontology term VBO:0200577 German Shepherd Dog (Dog) (vbo.obo, Monarch Initiative GitHub master). evidence: citations/species-vbo-0200577-german-shepherd-dog.md


## Artifacts

- [PLAN.md](Birt-Hogg-Dube_Syndrome-deep-research-claude_managed_artifacts/PLAN.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 133 |
| Resolved | 133 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 170 |
| Quoted claims found in source | 118 |
| Quoted claims **not** found in source | 52 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 133 |
| On topic | 113 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:39085584` *(abstract only)*: "major manifestations in three organs: benign cutaneous fibrofolliculomas/trichodischomas (FF/TD), pulmonary cysts with an associated increased risk of spontaneous pneumothorax (PTX) and, importantly, renal tumours"
  - closest text in source: "Patients with BHD syndrome are predisposed to benign cutaneous fibrofolliculomas/trichodischomas, pulmonary cysts with an associated risk of spontaneous pneumothorax, and renal cell carcinoma"
- `PMID:39085584` *(abstract only)*: "BHD syndrome is caused by monoallelic loss of function PVs in the FLCN gene [1, 3], and renal tumours are initiated by somatic mutations or loss of the wild-type allele (as in a classic tumour suppressor model)"
  - closest text in source: "Birt-Hogg-Dubé syndrome (BHD syndrome) is an autosomal dominant multisystem disorder with variable expression due to pathogenic constitutional variants in the FLCN gene"
- `PMID:39085584` *(abstract only)*: "two recent reports of cases with cutaneous FF and renal cancer that were associated with rare missense variants in PRDM10 (p.Cys677Tyr and p.Cys677Arg)"
  - closest text in source: "Patients with BHD syndrome are predisposed to benign cutaneous fibrofolliculomas/trichodischomas, pulmonary cysts with an associated risk of spontaneous pneumothorax, and renal cell carcinoma"
- `PMID:39085584` *(abstract only)*: "no other putative genotype-phenotype correlations have been confirmed to date"
  - Text part not found as substring: 'no other putative genotype-phenotype correlations have been confirmed to date' (note: only abstract available for PMID:39085584, full text may contain this excerpt)
- `PMID:39085584` *(abstract only)*: "should not be considered as ‘pneumothorax-only’ variants"
  - closest text in source: "Awareness of BHD syndrome needs to be raised and better knowledge of the clinical settings in which the diagnosis should be considered should enable earlier diagnosis"
- `PMID:35125098` *(abstract only)*: "A total of 79% (11/14) of patients with a history of pneumothorax were non-smokers"
  - closest text in source: "The clinical features of the patients included pneumothorax, renal lesions, and skin lesions"
- `PMID:39085584` *(abstract only)*: "Inheritance is autosomal dominant with age-dependent penetrance and variable expression. Inter- and intra-familial phenotypic variability is common."
  - closest text in source: "Birt-Hogg-Dubé syndrome (BHD syndrome) is an autosomal dominant multisystem disorder with variable expression due to pathogenic constitutional variants in the FLCN gene"
- `PMID:20301695` *(abstract only)*: "often increase in size, number, and distribution with age, eventually involving the face, neck, and upper trunk"
  - closest text in source: "Skin lesions typically appear between the second and fourth decades of life and typically increase in size and number with age"
- `PMID:26334087` *(abstract only)*: "Fibrofolliculomas, which develop after puberty, are generally neither painful nor pruritic."
  - closest text in source: "Birt-Hogg-Dubé (BHD) syndrome is an inherited renal cancer syndrome in which affected individuals are at risk of developing benign cutaneous fibrofolliculomas, bilateral pulmonary cysts and spontaneous pneumothoraces, and kidney tumours"
- `PMID:18234728` *(abstract only)*: "Ninety per cent (46/51) of families with BHDS had individuals with multiple 1–5 mm white or skin coloured papules distributed over the face, neck and/or upper trunk and a histologically confirmed fibrofolliculoma (FF)."
  - closest text in source: "10% (5/51) of the families had individuals without histologically confirmed fibrofolliculomas"
- `PMID:39085584` *(abstract only)*: "87 to 97% by age 70 years"
  - Text part not found as substring: '87 to 97% by age 70 years' (note: only abstract available for PMID:39085584, full text may contain this excerpt)
- `PMID:18234728` *(abstract only)*: "angiofibroma, perifollicular fibroma or both angiofibroma and perifollicular fibromas as their only BHDS cutaneous phenotype"
  - closest text in source: "CONCLUSION: BHDS is characterised by a spectrum of mutations, and clinical heterogeneity both among and within families."
- `PMID:20301695` *(abstract only)*: "The total number of lung cysts per individual ranges from zero to 166 (mean: 16). They are of irregular shape and variable size (1.0-30 mm)."
  - closest text in source: "Screening for lung cysts, fibrofolliculomas, and trichodiscomas can be performed if the pathogenic variant in the family is not known"
- `PMID:20301695` *(abstract only)*: "often the first manifestation in individuals with BHDS (onset range: age 13-69 years)"
  - closest text in source: "DIAGNOSIS/TESTING: The clinical diagnosis of BHDS is established in a proband with either one major criteria (>5 fibrofolliculomas/trichodiscomas; one histologically confirmed) or two minor criteria (bilateral basally located lung cysts without other cause, early-onset renal cell cancer [age <50 years], multifocal/bilateral renal cell cancer, renal cell cancer with mixed chromophobe/oncocytic histology, and/or a first-degree relative with BHDS)"
- `PMID:39085584` *(abstract only)*: "the presence of multiple facial FF/TDs can have significant psychosocial impact on people living with BHD syndrome"
  - closest text in source: "A requirement for updated International consensus recommendations for the diagnosis and management of BHD syndrome was identified"
- `PMID:39085584` *(abstract only)*: "anxiety related to uncertainty about future health problems and/or fear of developing cancer"
  - closest text in source: "Further details, including areas for future research topics are available at: https://www.genturis.eu/l=eng/Guidelines-and-pathways/Clinical-practice-guidelines.html ."
- `PMID:18234728` *(abstract only)*: "BHD is composed of 14 exons."
  - closest text in source: "Patients with a germline BHD mutation and family history of kidney cancer had a statistically significantly increased probability of developing renal tumours compared to patients without a positive family history (p = 0.0032)"
- `PMID:39085584` *(abstract only)*: "Recurrent pathogenic variants (e.g. frameshift c.1285delC/dupC) have been described."
  - closest text in source: "Birt-Hogg-Dubé syndrome (BHD syndrome) is an autosomal dominant multisystem disorder with variable expression due to pathogenic constitutional variants in the FLCN gene"
- `PMID:20301695` *(abstract only)*: "in the polycytosine tract in exon 11, which is a mutational hot spot"
  - Text part not found as substring: 'in the polycytosine tract in exon 11, which is a mutational hot spot' (note: only abstract available for PMID:20301695, full text may contain this excerpt)
- `PMID:18234728` *(abstract only)*: "Exon 11 was the most frequent site of mutation representing 47% (24/51) of the BHDS families."
  - closest text in source: "OBJECTIVE: To characterise the BHD mutation spectrum, novel mutations and new clinical features of one previously reported and 50 new families with BHDS"
- `PMID:37490463` *(abstract only)*: "These variants consisted of duplications (46.4%), deletions (29.0%), substitutions (7.1%), insertions (0.7%), deletions-insertions (0.3%), large genomic deletions (4.0%), and variants affecting splicing (12.5%)."
  - closest text in source: "We identified 70 unique FLCN germline variants, including duplications (46.4%), substitutions (7.1%), insertions/deletions (30.0%), and variants affecting splicing (12.5%)"
- `PMID:39085584` *(abstract only)*: "the vast majority of the identified missense variants are reported as variants of unknown significance (VUSs) (ClinVar database access March 2023: 787 missense variants, 688 uncertain"
  - closest text in source: "Birt-Hogg-Dubé syndrome (BHD syndrome) is an autosomal dominant multisystem disorder with variable expression due to pathogenic constitutional variants in the FLCN gene"
- `PMID:42206645` *(abstract only)*: "identified a total of 29 pathogenic/likely pathogenic missense variants"
  - closest text in source: "WES identified the FLCN variants p.W376R (previously classified as a Variant of Uncertain Significance, VUS) and a novel nonsense mutation p.Q44*"
- `PMID:39085584` *(abstract only)*: "should be assessed according to international guidelines (e.g. ACMG/AMP)"
  - closest text in source: "A requirement for updated International consensus recommendations for the diagnosis and management of BHD syndrome was identified"
- `PMID:35176117` *(abstract only)*: "According to population databases (gnomAD) this variant has a carrier frequency of 5/64548 in Europe and of these 4 are of Swedish origin."
  - closest text in source: "Moreover, according to gnomAD the carrier frequency of the c.779+1G>T variant has been estimated to be 1/3265 in the Swedish population, however our data suggest that the carrier frequency in the Swedish population may be significantly higher"
- `PMID:37490463` *(abstract only)*: "no somatic variants or loss of heterozygosity has been detected in either skin [7] or pulmonary lesions"
  - closest text in source: "METHODS: We reviewed the clinical and genetic data collected in 2006-2017, from the BHDS patients who were Asian and presented with pulmonary cysts with or without a history of PTX"
- `PMID:39085584` *(abstract only)*: "Biallelic FLCN inactivation leads to activation of the mTOR pathway in some contexts [6], although FLCN is implicated in additional cellular processes. A key role in the regulation of mTORC1 in kidney cells with FLCN inactivation is played by TFEB"
  - closest text in source: "Regular renal cancer surveillance is recommended in adulthood and life-long, but the evidence base for additional tumour surveillance is limited and further research warranted"
- `PMID:33064845` *(abstract only)*: "required for its functions in mTOR regulation and tumor suppression"
  - closest text in source: "These observations suggest that ciliary localization of FLCN is essential for its function as a tumor suppressor."
- `PMID:26334087` *(abstract only)*: "multiple anastomosing strands of 2-4 epithelial cells that emanate from a central aberrant hair follicle and frequently are continuous with sebaceous glands"
  - closest text in source: "Bilateral multifocal renal tumours that develop in BHD syndrome are most frequently hybrid oncocytic tumours and chromophobe renal carcinoma, but can present with other histologies"
- `PMID:36028846` *(abstract only)*: "The majority of cysts were located in the basal lung fields below the level of the carina."
  - closest text in source: "One of the characteristics is the increased risk for spontaneous pneumothorax, likely due to the presence of pulmonary cysts mainly distributed under the carina"
- `PMID:39085584` *(abstract only)*: "The risk of a spontaneous pneumothorax in BHD syndrome is lifelong"
  - closest text in source: "Patients with BHD syndrome are predisposed to benign cutaneous fibrofolliculomas/trichodischomas, pulmonary cysts with an associated risk of spontaneous pneumothorax, and renal cell carcinoma"
- `PMID:39085584` *(abstract only)*: "around fortyfold higher"
  - Text part not found as substring: 'around fortyfold higher' (note: only abstract available for PMID:39085584, full text may contain this excerpt)
- `PMID:41896555` *(abstract only)*: "the carrier frequency of truncating FLCN variants is 1 in 2654."
  - closest text in source: "However, we demonstrate that BHD-causing FLCN variants are 75 to 180 times more prevalent in the multi-ethnic large genomic registry population"
- `PMID:41896555` *(abstract only)*: "92% of all identified deleterious FLCN variants in the Finnish population are c.1285dup, which suggests that c.1285dup is a founder mutation in this population."
  - closest text in source: "However, we demonstrate that BHD-causing FLCN variants are 75 to 180 times more prevalent in the multi-ethnic large genomic registry population"
- `PMID:35176117` *(abstract only)*: "The most common variant among families was the splicing variant c.779+1G>T that was found in 57% (44 of 78) of the families"
  - closest text in source: "Splice variant c.779+1G>T was the most common pathogenic variant, found in 57% of the families, suggesting this may be a founder mutation in the Swedish population"
- `PMID:33313181` *(abstract only)*: "Among these 166 patients, 100 (60.2%) were females."
  - closest text in source: "A total of 166 patients were included in this study, and 100 of them (60.2%) were females"
- `PMID:35639097` *(abstract only)*: "Variant-positive participants were 62.9% female"
  - closest text in source: "Although most variant-positive individuals had BHD-related phenotypes, a minority were previously clinically diagnosed, likely because cutaneous manifestations, pneumothoraces, and kidney cancer were observed at lower frequencies than in clinical cohorts"
- `PMID:39085584` *(abstract only)*: "one major criterion ( >5 fibrofolliculomas or trichodiscomas, at least one histologically confirmed, of adult onset) or two minor criteria (1. Lung: bilateral basally located pulmonary cysts with no other apparent cause; 2. Kidney: early onset ( <50 years), multifocal or bilateral renal cancer, or renal cancer of mixed chromophobe and oncocytic histology; or 3. Family history: a first-degree relative with BHD syndrome) are present."
  - closest text in source: "Patients with BHD syndrome are predisposed to benign cutaneous fibrofolliculomas/trichodischomas, pulmonary cysts with an associated risk of spontaneous pneumothorax, and renal cell carcinoma"
- `PMID:39085584` *(abstract only)*: "A definitive diagnosis of BHD syndrome should be made when a genetic test is positive for a constitutive pathogenic/likely pathogenic variant in FLCN."
  - closest text in source: "Birt-Hogg-Dubé syndrome (BHD syndrome) is an autosomal dominant multisystem disorder with variable expression due to pathogenic constitutional variants in the FLCN gene"
- `PMID:20301695` *(abstract only)*: "If no variant is detected by the sequencing method used, the next step is to perform gene-targeted deletion/duplication analysis to detect exon and whole-gene deletions or duplications."
  - closest text in source: "Once the FLCN pathogenic variant has been identified in an affected family member, predictive testing for at-risk family members and prenatal/preimplantation genetic testing for BHDS are possible."
- `PMID:39085584` *(abstract only)*: "Lung ultrasound should not be used as a diagnostic test for pulmonary cysts"
  - closest text in source: "Patients with BHD syndrome are predisposed to benign cutaneous fibrofolliculomas/trichodischomas, pulmonary cysts with an associated risk of spontaneous pneumothorax, and renal cell carcinoma"
- `PMID:39085584` *(abstract only)*: "nowadays genetic testing can offer an alternative route to diagnosis"
  - closest text in source: "With the widespread availability of FLCN genetic testing, clinical scenarios in which a diagnosis should be considered and criteria for genetic testing were defined"
- `PMID:20301695` *(abstract only)*: "Features atypical for BHDS are an even distribution of cysts throughout the lung, dyspnea on exertion, hemoptysis, and chylothorax."
  - closest text in source: "DIAGNOSIS/TESTING: The clinical diagnosis of BHDS is established in a proband with either one major criteria (>5 fibrofolliculomas/trichodiscomas; one histologically confirmed) or two minor criteria (bilateral basally located lung cysts without other cause, early-onset renal cell cancer [age <50 years], multifocal/bilateral renal cell cancer, renal cell cancer with mixed chromophobe/oncocytic histology, and/or a first-degree relative with BHDS)"
- `PMID:39085584` *(abstract only)*: "A diagnosis of BHD syndrome may be associated with psychological challenges and socioeconomic hardships"
  - closest text in source: "Following a clinical and/or molecular diagnosis of BHD syndrome, a multidisciplinary approach to disease management is required"
- `PMID:39085584` *(abstract only)*: "Currently there is not sufficient evidence of an increased risk for other tumours"
  - closest text in source: "Regular renal cancer surveillance is recommended in adulthood and life-long, but the evidence base for additional tumour surveillance is limited and further research warranted"
- `PMID:39085584` *(abstract only)*: "Nephron-sparing surgery should ideally be performed whenever possible, with percutaneous thermal ablation being an alternative."
  - Text part not found as substring: 'Nephron-sparing surgery should ideally be performed whenever possible, with percutaneous thermal ablation being an alternative.' (note: only abstract available for PMID:39085584, full text may contain this excerpt)
- `PMID:36291753` *(abstract only)*: "No local tumor progression was observed during a median follow-up period of 74 months"
  - closest text in source: "All patients were alive with no distant metastasis during a median follow-up period of 74 months (range: 33-83 months)"
- `PMID:39085584` *(abstract only)*: "Treatment is not curative and may need to be repeated."
  - closest text in source: "Recommendations for the treatment of cutaneous, pulmonary and renal manifestations are provided"
- `PMID:39085584` *(abstract only)*: "should be considered in case of recurrent pneumothorax"
  - closest text in source: "With the widespread availability of FLCN genetic testing, clinical scenarios in which a diagnosis should be considered and criteria for genetic testing were defined"
- `PMID:39085584` *(abstract only)*: "but not usually to asymptomatic patients before 20 years of age"
  - closest text in source: "Patients with BHD syndrome are predisposed to benign cutaneous fibrofolliculomas/trichodischomas, pulmonary cysts with an associated risk of spontaneous pneumothorax, and renal cell carcinoma"
- `PMID:39085584` *(abstract only)*: "Flights on commercial airlines are generally safe"
  - Text part not found as substring: 'Flights on commercial airlines are generally safe' (note: only abstract available for PMID:39085584, full text may contain this excerpt)
- `PMID:18234728` *(abstract only)*: "highly conserved among species"
  - Text part not found as substring: 'highly conserved among species' (note: only abstract available for PMID:18234728, full text may contain this excerpt)

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMID:38900222`: "the first report of metastasized chromophobe RCC, after complete resection of a primary tumor smaller than 3 cm, in a patient with BHD"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 93 |
| Resolved | 80 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 13 |
| Terms whose name was checked | 3 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0800444` (10 mentions) - the report calls it "if available", "label: Birt-Hogg-Dube syndrome"; MONDO calls it **Birt-Hogg-Dube syndrome**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `VBO:0200577` (3 mentions) - the report calls it "citations/species-vbo-0200577-german-shepherd-dog.md"; VBO calls it **German Shepherd Dog (Dog)**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0800444` - called "if available", "label: Birt-Hogg-Dube syndrome"
- `HGNC:27310` - called "location 17p11.2", "aliases BHD, DENND8B"
- `MGI:2442184` - called "Flcn; NCBI Gene 216805", "folliculin"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `GARD`, `NORD`, `ORPHA`, `OMIM`, `OMIA`, `MGI`, `Gene`, `Taxonomy`.
