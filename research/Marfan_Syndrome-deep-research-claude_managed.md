---
provider: claude_managed
model: claude-opus-5-5
cached: false
start_time: '2026-11-10T16:25:50.923353'
end_time: '2026-11-10T16:27:50.563740'
duration_seconds: 119.64
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Marfan Syndrome
  mondo_id: MONDO:0007947
  category: Genetic
  causal_genes: FBN1
  omim_id: OMIM:154700
  synonyms: MFS; MFS1; Marfan syndrome type 1; Marfan syndrome, type 1; Marfan's syndrome
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
    timeout: 3600
    session_id: sesn_01NbGWRhgsE8TAYKkkzugbnP
    delete_session: false
run_metadata:
  session_id: sesn_01NbGWRhgsE8TAYKkkzugbnP
  agent_id: agent_01K5k8H6H4Uxic777boZvtbf
  agent_version: 1
  environment_id: env_01NDhAwC4BsT39w6UteFeYkq
  retriever_model: claude-haiku-5-5
  stop_reason: budget_reached
  outcome_result: satisfied
  workflow_runs: 2
  tool_calls: 85
  outcome_iterations: 2
  grader_explanation: "An independent grader found all criteria met:\n\n- Research\
    \ report rubric (evidence, traceable/aligned citations, relevance, structure,\
    \ coverage) (met): I checked the files directly. Evidence: all 240 citation files\
    \ have the frontmatter fields key, identifiers, title, source_url and content,\
    \ and their bodies are verbatim abstracts, full-text excerpts or ontology lookup\
    \ tables. Spot checks found identifiers matching the source URLs (for example,\
    \ PMID:16601194 points to the PubMed URL for 16601194). Traceability: a script\
    \ found 202 distinct IDs cited in the report body, and every one is in an evidence\
    \ file. The only apparent misses were NCT IDs, which the files record as NCT:NCTxxxx,\
    \ and the report uses that same form. Every cited ID also appears in References.\
    \ Of 198 quotations, 192 matched their evidence-file body word for word. I checked\
    \ the other 6 by hand and they are artefacts of my script, not real mismatches.\
    \ They come from line wrapping in the UniProt flatfile, URLs containing parentheses,\
    \ or text that is not a quote. The MedlinePlus, CCS and UniProt quotes are confirmed\
    \ in their files. Alignment: I spot-checked about 15 numeric claims against their\
    \ sources and all matched. They were Danish prevalence 6.5/100,000 and incidence\
    \ 0.19; Taiwan 10.2; Korea 2.27; gnomAD 1 in 416, 243, 5185 and 8624; Murdoch\
    \ mean age at death 32; Silverman median survival 72; Norwegian SMR 5.24; Groth\
    \ 50 vs 60 years and HR 194.6; parental mosaicism 6.6%; Jondeau 4-fold risk at\
    \ \u226550 mm; and Dreher's sex-specific aneurysm rates. The report states where\
    \ sources disagree: TGF-\u03B2 vs no TGF-\u03B2 signature, US vs European pregnancy\
    \ thresholds, conflicting fluoroquinolone data, inconsistent genotype-guided ARB\
    \ benefit, and sex differences. Relevance: claims rest mostly on primary PubMed\
    \ literature, GeneReviews, guidelines and OMIM/Orphanet, and sections cite several\
    \ sources each. Structure: the template asks for 15 sections, and that requirement\
    \ takes precedence over the rubric's six-to-eight-section guidance. The report\
    \ follows the template, gives an interpretation/scope statement and a summary\
    \ of findings, and names FBN1 in the first paragraph. Section 6 opens with a numbered\
    \ causal chain that uses explicit causal verbs, marks branches, and says which\
    \ steps are demonstrated and which are inferred. Ontology CURIEs are backed by\
    \ OLS lookup files. Open Questions and References sections are present, with one\
    \ line per source giving its ID, citation and evidence file. Coverage: all 12\
    \ plan sub-questions are addressed, and gaps are stated explicitly, such as FBN1\
    \ pLI/LOEUF not retrieved, MGI records not retrieved, no founder variant, and\
    \ anticipation not applicable. Minor issues: the plan lists paternal-age effect\
    \ as a remaining gap, but the report does not mention it. Some sections are written\
    \ as dense bulleted or tabular content rather than narrative, but the template's\
    \ format allows this. Neither issue is material."
  input_tokens: 1086
  output_tokens: 580098
  cache_read_input_tokens: 64530446
  web_search_requests: 30
  web_fetch_requests: 0
  list_cost_usd: 20.14
  active_seconds: 4212.86
  evidence_check:
    evidence_files: 240
    cited_identifiers: 194
    cited_without_evidence: []
    quotes_checked: 185
    quotes_anchored: 185
    unanchored_quotes: []
  repair_rounds: 0
citation_count: 229
reference_validation:
  total_references: 211
  verified: 210
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.005
  quotes_checked: 170
  quotes_valid: 153
  quotes_unsupported: 17
  unsupported_quote_references:
  - PMID:20301510
  - PMID:28708846
  - PMID:33885997
  - PMID:34825999
  - PMID:34795948
  - PMID:27138491
  - PMID:26631233
  - PMID:28244281
  - PMID:15776436
  quotes_not_checkable: 15
  relevance_assessed: 210
  on_topic: 176
  unresolved_references:
  - PMID:21152435
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 176
  verified: 162
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 141
  labels_matching: 140
  labels_variant: 1
  not_configured: 10
  not_configured_terms:
  - OMIM:154700
  - ORPHA:558
  - ORPHA:284963
  - MeSH:D008382
  - UniProt:P35555
  - NCT:NCT00429364
  - NCT:NCT00763893
  - NCT:NCT00782327
  - NCT:NCT01949233
  - OMIA:000628
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  claude_managed: 1
artifacts:
- filename: PLAN.md
  path: Marfan_Syndrome-deep-research-claude_managed_artifacts/PLAN.md
  media_type: text/plain
  source: claude_managed
  data_storage_id: file_01QG4y7fbTcd357y1EGj6FJx
  description: null
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Marfan Syndrome
- **MONDO ID:** MONDO:0007947 (if available)
- **Causal gene(s):** FBN1
- **OMIM:** OMIM:154700
- **Synonyms:** MFS; MFS1; Marfan syndrome type 1; Marfan syndrome, type 1; Marfan's syndrome
- **Category:** Genetic

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Marfan Syndrome** covering all of the
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


## Ontology terms

Where a concept you discuss belongs to one of these ontologies, give its term as a CURIE followed by the term's label in brackets, in the form `PREFIX:ID (term label)`: MONDO, HP, GO, CL, UBERON, CHEBI, NCIT, NCBITaxon, HGNC. Put only the term's own label in the brackets, and any comment outside them. Use no other ontologies for this. Give only identifiers you have looked up, not ones recalled from memory, and leave a concept without a term rather than guess one.

## Output

# Marfan Syndrome — MONDO:0007947 (Marfan syndrome), OMIM:154700, causal gene FBN1: Disease Characteristics Review

**Interpretation and scope.** This report characterises Marfan syndrome (MFS) as defined by MONDO:0007947 (Marfan syndrome) and OMIM:154700, the autosomal dominant connective tissue disorder caused by heterozygous pathogenic variants in **FBN1** — HGNC:3603 (fibrillin 1), located on chromosome 15q21.1. Other entities that share the name or phenotype — Loeys–Dietz syndrome (TGFBR1/TGFBR2/SMAD3/TGFB2), the obsolete label "Marfan syndrome type 2", MASS phenotype, isolated ectopia lentis and the FBN1 acromelic dysplasias — are discussed only as differential diagnoses or allelic disorders. The report follows the 15 sections requested in the template, opens the mechanism section with an ordered causal chain, and ends with Open Questions and References. Every factual statement is drawn from the evidence files in `citations/`; where the evidence base retrieved for this report is silent, this is said explicitly rather than filled from memory. Ontology CURIEs are given only where they were looked up and recorded in an evidence file (`ols-hpo-terms-marfan.md`, `hpo-annotations-omim-154700.md`, `ols-mondo-hgnc-terms.md`, `ols-go-terms.md`, `ols-cl-terms.md`, `ols-uberon-terms.md`, `ols-chebi-ncit-terms.md`, `ncbitaxon-terms.md`). Evidence types are flagged as human clinical, model organism, in vitro or computational.

## Summary of main findings

Marfan syndrome is a pleiotropic, autosomal dominant disorder of fibrous connective tissue caused by pathogenic variants in FBN1, which encodes fibrillin-1, the main structural unit of extracellular microfibrils. Its cardinal manifestations are proximal aortic root aneurysm (with risk of dissection), ectopia lentis and long-bone overgrowth (PMID:16325700; PMID:34475413). Registry-based prevalence estimates range from roughly 2 to 10 per 100,000 depending on country, coding and diagnostic criteria (PMID:26631233; PMID:24388020; PMID:28244281), whereas a gnomAD-based estimate of predicted pathogenic FBN1 variants suggests the genotype is far more common than clinically diagnosed disease (PMID:40102521). About a quarter of cases are de novo (PMID:34475413). Diagnosis follows the 2010 revised Ghent nosology, in which aortic root dilatation and ectopia lentis are the cardinal features, supplemented by FBN1 testing and a systemic score (PMID:20591885). Mechanistically, fibrillin-1 deficiency perturbs microfibril-dependent sequestration of TGF-β and leads to dysregulated canonical and non-canonical (ERK) signalling in mouse models (PMID:12598898; PMID:21493862), although this model is contested by mouse and human data showing no detectable TGF-β signature, and newer work implicates nitric oxide–sGC–PRKG signalling, mitochondrial dysfunction and smooth muscle cell phenotypic modulation (PMID:28119285; PMID:35008861; PMID:33976159; PMID:33709773; PMID:32698686). Life expectancy has improved from a mean age at death of 32 years in 1972 (PMID:5011789) to a median survival probability of 72 years by 1993 (PMID:7810492), and GeneReviews states that with proper management life expectancy approximates that of the general population (PMID:20301510); however, national registries still show reduced lifespan (50 vs 60 years in Denmark) and a standardized mortality ratio of 5.24 in Norway, driven mainly by aortic disease (PMID:30149886; PMID:30393980). Angiotensin receptor blockers and β-blockers both modestly slow aortic root growth (PMID:36049495), and prophylactic aortic root replacement is the main life-saving intervention (PMID:22133496; PMID:29893811). Current guidelines recommend root replacement at ≥5.0 cm (≥50 mm), to be considered at ≥4.5 cm with risk factors, and before pregnancy above 4.5 cm (PMID:36322642; PMID:39210722; PMID:40878294). Additional evidence implicates aortic inflammation, oxidative stress and epigenetic regulation as modifiers of aortopathy (PMID:22479353; PMID:29471108; PMID:20829218), and men carry a greater aneurysm and surgical burden although dissection prevalence is similar by sex in several cohorts (PMID:42475821; PMID:23444191).

---

## 1. Disease Information

**Overview.** OMIM describes MFS as "A heritable disorder of fibrous connective tissue, Marfan syndrome (MFS) shows striking pleiotropism and clinical variability." (OMIM:154700), with "The cardinal features occur in 3 systems--skeletal, ocular, and cardiovascular" (OMIM:154700). Orphanet defines it as "a systemic disease of connective tissue characterized by a variable combination of cardiovascular, musculo-skeletal, ophthalmic and pulmonary manifestations" (ORPHA:558). A Nature Reviews Disease Primer states that MFS "is an autosomal dominant, age-related but highly penetrant condition with substantial intrafamilial and interfamilial variability" (PMID:34475413), and that "The most prominent manifestations of MFS are asymptomatic aortic root aneurysms, aortic dissections, dislocation of the ocular lens (ectopia lentis) and skeletal abnormalities that are characterized by overgrowth of the long bones" (PMID:34475413). GeneReviews describes "a broad phenotypic continuum ranging from mild (features of Marfan syndrome in one or a few systems) to severe and rapidly progressive neonatal multiorgan disease" (PMID:20301510).

**Key identifiers.** MONDO:0007947 (Marfan syndrome) (MONDO:0007947); OMIM:154700 (OMIM:154700); Orphanet ORPHA:558 "Marfan syndrome" and ORPHA:284963 "Marfan syndrome type 1" (clinical subtype exactly mapped to OMIM 154700) (ORPHA:558); ICD-10 Q87.4 and ICD-11 LD28.01 (both exact mappings in Orphanet) (ORPHA:558); MeSH D008382 "Marfan Syndrome" (MeSH:D008382); UMLS C0024796 and MedDRA 10026829 (ORPHA:558); NCIT:C34807 (Marfan Syndrome) (see `ols-chebi-ncit-terms.md`). The causal gene is FBN1, HGNC:3603 (fibrillin 1), OMIM gene entry 134797, Entrez Gene 2200, Ensembl ENSG00000166147, MANE transcript NM_000138.5, UniProt P35555 (HGNC:3603). Related MONDO terms: MONDO:0017309 (neonatal Marfan syndrome), MONDO:0017310 (Marfan and Marfan-related disorder), MONDO:0018954 (Loeys-Dietz syndrome) (see `ols-mondo-hgnc-terms.md`).

**Synonyms.** MONDO lists the exact synonyms "MFS, MFS1, Marfan syndrome type 1, Marfan syndrome, Marfan syndrome, type 1, Marfan's syndrome" (MONDO:0007947); MedlinePlus lists "Marfan's syndrome" and "MFS" (https://medlineplus.gov/genetics/condition/marfan-syndrome/). The term "Marfan syndrome type 2" is obsolete: GeneReviews notes "This term is no longer in use" and that the phenotype "is now known to be Loeys-Dietz syndrome" (PMID:20301510). GeneReviews also recommends abandoning "neonatal Marfan syndrome" as a discrete category in favour of "early onset" and "rapidly progressive" (PMID:20301510), whereas MONDO retains MONDO:0017309 (neonatal Marfan syndrome).

**Source of information.** The descriptive information in this report comes overwhelmingly from aggregated disease-level resources (OMIM, Orphanet, MONDO, GeneReviews, HPO annotations) and from published cohort studies, registries and trials, not from individual-patient EHR extraction. Several epidemiological studies did use national administrative registries built from individual records (Danish, Taiwanese and Korean health systems) (PMID:26631233; PMID:24388020; PMID:28244281).

## 2. Etiology

**Disease causal factors.** MFS is genetic. "MFS is caused by pathogenetic variants in FBN1, which encodes fibrillin-1, a major structural component of the extracellular matrix that provides support to connective tissues, particularly in arteries, the pericondrium and structures in the eye" (PMID:34475413). The link was established when "the fibrillin gene is linked to the Marfan phenotype (theta = 0.00; logarithm of the odds (lod) = 3.9)" and a de novo missense mutation was found in sporadic cases (PMID:1852208). No environmental, infectious or toxic primary cause exists.

**Genetic risk factors.** The causal factor is a heterozygous FBN1 pathogenic variant; "Up to 25% of individuals with MFS have de novo variants" (PMID:34475413). Variant class modifies risk: truncating/premature termination codon (haploinsufficient, HI) variants carry higher aortic and survival risk than dominant-negative (DN) missense variants (PMID:26787436; PMID:33731877; PMID:41309212), and cysteine-loss in-frame variants are more severe than other in-frame variants (PMID:33731877). Genome-wide modifier searches in 1,070 FBN1 carriers found "A polygenic model involving at least nine modifier loci (named gMod-M1-9)" (PMID:30087447) and a second pathogenic event in another thoracic aortic aneurysm gene or COL4A1 in nine individuals (PMID:30087447). A family history of severe cardiovascular disease is an independent risk marker: "aortic dilation is greater and life expectancy shorter in those with a family history of severe cardiovascular manifestations" (PMID:7560600).

**Non-genetic risk factors (modifiers of expression, not causes).** Male sex is associated with earlier and more frequent aortic events: in the Danish nationwide cohort, "Male patients had a significant higher risk of an aortic event at a younger age with a hazard ratio of 1.75" (PMID:27550511), and in GenTAC, adult males more often had root dilatation (92% vs 84%) and prophylactic root replacement (47% vs 24%) (PMID:28600386). In a Mayo Clinic cohort, "Among 783 patients (443 men, 340 women), men more often had ascending aortic aneurysm (89.1% vs 71.1%), any aneurysm (91.0% vs 75.3%), and any extra-aortic aneurysm (36.8% vs 25.9%) (all P ≤ 0.001)." while "Dissection prevalence was similar by sex." (PMID:42475821); a German single-centre series found that "Male patients had a significantly higher probability of experiencing an aortic event (P = 0.015) compared to female patients." (PMID:35543473), and across GenTAC conditions "Thoracic aortic dissections occurred with equal gender frequency" while women "had fewer total aortic surgeries" (PMID:23444191). Smoking is mentioned by the 2022 ACC/AHA guideline: "Most individuals with aortic disease distal to the root have had previous root replacement or smoke cigarettes." (PMID:36322642). Pregnancy increases dissection risk (rate ratio 8.4 vs non-pregnant periods) (PMID:27515814). Late diagnosis is itself a risk factor: "Multivariate Cox regression analysis confirmed late diagnosis as predictor of delayed RAA (hazard ratio, 8.01" (PMID:39306029). Hypertension prevalence was 28.8% among young MFS patients with type B dissection in GenTAC, and the authors concluded that control of hypertension is "an essential component of care to" decrease the risk of type B dissection (PMID:31376376). Age is a determinant of penetrance of several features (see Sections 3 and 8).

**Protective factors.** No protective genetic variant has been identified in the retrieved evidence. In mice, higher residual wild-type Fbn1 expression is protective: Lima et al. report "a strong negative correlation between overall levels of Fbn1 expression and the severity of the phenotypes, corroborating the suggested protective role of normal fibrillin-1" (PMID:21152435), and in C1039G/+ mice "introduction of a WT FBN1 transgene on a heterozygous C1039G background rescues aortic phenotype" (PMID:15254584). A sex-hormone mechanism has been proposed from human, mouse and in vitro data: "the female hormone 17β-estradiol stimulates aortic smooth muscle cells to produce fibrillin-1 in vitro" (PMID:28708846). Moderate aerobic exercise is protective in mice — "moderate, but not strenuous, exercise protects aortic structure and function in a mouse model of Marfan syndrome" (PMID:28385916), and in Fbn1 C1039G/+ mice trained on a treadmill "aortic root diameter was smaller than in their Sed littermates" (PMID:28947563) — but no human outcome trial exists. Protective environmental/therapeutic factors are β-blockers and ARBs (Section 12) and, observationally, ARB use was associated with fewer type B dissections (hazard ratio 0.3) (PMID:25614422). Early diagnosis is protective in the sense that "diagnosing MFS is lifesaving and improves mortality risk by reducing the risk of aorta dissection" (PMID:27550511).

**Gene–environment interactions.** The best-documented gene–drug interaction is with calcium channel blockers: "Marfan mice treated with CCBs show accelerated aneurysm expansion, rupture, and premature lethality" via a PKCβ/ERK1/2- and AT1R-dependent pathway, and "patients with Marfan syndrome and other forms of inherited thoracic aortic aneurysm taking CCBs display increased risk of aortic dissection and need for aortic surgery" (PMID:26506064). Fluoroquinolones accelerate aortic enlargement in Fbn1C1041G/+ mice, with dissection 25% vs 47% and rupture 5% vs 25% (vehicle vs ciprofloxacin) (PMID:34586071), but a Taiwanese case-crossover study of 550 patients (415 with MFS) found "Fluoroquinolone use was not associated with an increased risk of AA/AD in patients with congenital aortic disease, including Marfan syndrome" (PMID:36823078). Pregnancy is a physiological stressor that interacts with genotype (PMID:27515814). Genetic background modifies disease in mice: onset "is earlier in the 129/Sv than in C57BL/6 background, indicating the existence of genetic modifiers of MFS between these two mouse strains" (PMID:21152435). No entries for MFS in CTD or GxE databases were retrieved.

## 3. Phenotypes

The table lists principal phenotypes with HPO terms (all IDs and labels from `ols-hpo-terms-marfan.md` or `hpo-annotations-omim-154700.md`). Frequencies attributed to HPO annotations are the counts attached to OMIM:154700 in the HPO annotation file, which derive mostly from single cohorts and should be read as indicative (OMIM:154700).

| Phenotype (type) | HPO term | Frequency / characteristics | Evidence |
|---|---|---|---|
| Aortic root dilatation (clinical sign, imaging) | HP:0002616 (Aortic root aneurysm) | HPO annotation 45/58; 78% in an adult clinic cohort; 92% of adult men vs 84% of women in GenTAC; progressive | PMID:8487722; PMID:28600386 |
| Aortic dissection (acute event) | HP:0002647 (Aortic dissection) | 36.4% of a national cohort had an aortic event (dissection or prophylactic surgery); 44% of dissections in GenTAC were type B | PMID:27550511; PMID:28600386 |
| Mitral valve prolapse | HP:0001634 (Mitral valve prolapse) | HPO 67/111; 46/52 children by mean age 9.7 y; 65% of adults | PMID:11159287; PMID:8487722 |
| Mitral regurgitation | HP:0001653 (Mitral regurgitation) | HPO 33/58; 25/52 children | PMID:11159287 |
| Tricuspid valve prolapse | HP:0001704 (Tricuspid valve prolapse) | HPO 31/58 | OMIM:154700 |
| Aortic regurgitation | HP:0001659 (Aortic regurgitation) | 28% of adults; 55% of adult men vs 36% of women | PMID:8487722; PMID:28600386 |
| Arrhythmia / sudden death | HP:0011675 (Arrhythmia) | VT events 8% of 80 adults incl. 4% SCD over ~31 months | PMID:24349050 |
| Cardiomyopathy / heart failure | HP:0001635 (Congestive heart failure) | LVEF abnormal in 48% of children without significant volume load | PMID:38816063 |
| Pulmonary artery dilatation | HP:0004927 (Pulmonary artery dilatation) | listed in GeneReviews and HPO; no frequency | PMID:20301510 |
| Ectopia lentis (sign) | HP:0001083 (Ectopia lentis) | ~60% (GeneReviews); 62% of Ghent-positive adults; HPO 119/251; usually bilateral | PMID:20301510; PMID:19293838 |
| Myopia | HP:0000545 (Myopia) | >50% (GeneReviews); >3 D in 34–44% | PMID:20301510; PMID:40005367 |
| Retinal detachment, cataract, glaucoma | HP:0000541 (Retinal detachment); HP:0000518 (Cataract); HP:0000501 (Glaucoma) | increased risk; HPO glaucoma 29/625 | PMID:20301510 |
| Flat cornea / increased axial length | HP:0007720 (Flat cornea); HP:0007800 (Increased axial length of the globe) | OMIM ocular findings | OMIM:154700 |
| Strabismus | HP:0000486 (Strabismus) | 110/573 (19.2%) | OMIM:154700 |
| Tall stature / dolichostenomelia | HP:0000098 (Tall stature); HP:0001519 (Disproportionate tall stature) | HPO 38/53 for disproportionate tall stature | OMIM:154700 |
| Arachnodactyly | HP:0001166 (Arachnodactyly) | HPO 124/197 | OMIM:154700 |
| Pectus excavatum / carinatum | HP:0000767 (Pectus excavatum); HP:0000768 (Pectus carinatum) | chest wall deformity up to 70%; HPO 44/146 and 58/146 | PMID:34825999 |
| Scoliosis | HP:0002650 (Scoliosis) | >50% (Cobb >10°); more prevalent in adults than children | PMID:34825999; PMID:28600386 |
| Protrusio acetabuli | HP:0003179 (Protrusio acetabuli) | 16–100% depending on method; 58/87 hips on CT; stable over 10 y | PMID:40075421 |
| Joint hypermobility | HP:0001382 (Joint hypermobility) | HPO 11/53 | OMIM:154700 |
| Pes planus / hindfoot deformity | HP:0001763 (Pes planus) | HPO 27/53 | OMIM:154700 |
| Wrist and thumb signs | HP:0025091 (Wrist sign); HP:6001274 (Thumb sign) | systemic-score items | PMID:34825999 |
| Reduced elbow extension | HP:0001377 (Limited elbow extension) | HPO 29/199 | OMIM:154700 |
| Craniofacial features | HP:0000268 (Dolichocephaly); HP:0000490 (Deeply set eye); HP:0000494 (Downslanted palpebral fissures); HP:0000272 (Malar flattening); HP:0000278 (Retrognathia); HP:0000218 (High palate) | HPO 36/53, 25/63, 19/53, 31/53, –, 34/53 | OMIM:154700 |
| Dural ectasia | HP:0100775 (Dural ectasia) | 63–97%; 91% of Ghent-positive adults; may appear or worsen in adulthood | PMID:34825999; PMID:19293838; PMID:30998996 |
| Spontaneous pneumothorax | HP:0002108 (Spontaneous pneumothorax); HP:0002107 (Pneumothorax) | 11/100 in a hospital series; HPO 6/53 | PMID:6495247 |
| Emphysema / bullae | HP:0002097 (Emphysema) | HPO "Occasional" | PMID:6495247 |
| Obstructive sleep apnea | HP:0002870 (Obstructive sleep apnea) | 32–64% (review) | PMID:34795948 |
| Striae | HP:0001065 (Striae distensae) | HPO 11/53 | OMIM:154700 |
| Hernia | HP:0000023 (Inguinal hernia); HP:0004872 (Incisional hernia) | no reliable frequency | PMID:31825148 |
| Chronic pain, fatigue (symptoms) | — | pain 89% of 245 adults; fatigue 37–89% across studies | PMID:27862906; PMID:37208760 |
| Inheritance | HP:0000006 (Autosomal dominant inheritance) | — | OMIM:154700 |

**Cardiovascular.** Aortic root dilatation is the hallmark. In an Australian clinic, "Aortic root dilatation was present in 78% of patients, aortic regurgitation in" 28%, with mitral valve prolapse in 65% and mitral regurgitation in 35% (PMID:8487722). In children, "Mitral valve prolapse (MVP) was diagnosed in 46 patients at a mean age" of 9.7 years and "Both MVP and aortic dilatation developed at a constant" rate across ages 5–20 years (PMID:11159287). Non-aortic cardiovascular disease is substantial in Danish registry data: "Heart failure/cardiomyopathy was also more common in MFS [HR: 8.7 (CI 5.7-13.4)]" and "The risk of sudden cardiac death was increased [HR: 8.3 (CI 3.8-18.0)] but the etiology was unclear due to lack of autopsies" (PMID:33885997). In children, "Ventricular dilation and reduced EF are common in children with MFS" (PMID:38816063). Mitral annular disjunction was present in 34% of 142 FBN1-positive patients and was associated with arrhythmic events (PMID:34232254).

**Ocular.** OMIM lists "Myopia, increased axial globe length, corneal flatness, and subluxation of the lenses (ectopia lentis) are ocular findings" (OMIM:154700). GeneReviews: "Ocular findings include myopia (>50% of affected individuals); ectopia lentis (seen in approximately 60% of affected individuals); and an increased risk for retinal detachment, glaucoma, and early cataracts" (PMID:20301510). UniProt notes that ectopia lentis "occurs in most of the patients" and "is almost always bilateral" (UniProt:P35555). In a Danish ectopia lentis series, "Marfan syndrome (MFS) was found in 34 (47.2%)" of patients and 94.4% of cases were bilateral (PMID:36449672). In 87 Norwegian Ghent-1 adults, "EL was found in 108 eyes (62.1%)." and "Myopia above 3D occurred in 38.4% of the phakic eyes." (PMID:24853997). At 10-year follow-up of the same cohort, "Two patients (3 eyes) had developed EL over the decade, representing a 13% risk." and "There were 7% and 33% risks for development of retinal detachment and cataract between baseline and follow-up, respectively." (PMID:30260057). Corneal flattening is a measurable sign: "Fifteen MFS eyes (38%) and three control eyes (8%) had K(med) values below 41.5 D (p = 0.0012)." and "High corneal astigmatism is associated with subluxation in MFS." (PMID:21726424). Under the revised criteria, many FBN1-positive "isolated" ectopia lentis cases are MFS: "57/123 probands (46.3%) are now classified as MFS according to the revised Ghent nosology" (PMID:24635535).

**Skeletal, dural, pulmonary, skin.** "Scoliosis affects more than 50% of MFS patients, as defined using the Cobb method that considers an angle of > 10° significant" (PMID:34825999); "Chest wall deformity occurs in up to 70% of cases, usually becoming more evident during periods of accelerated growth in adolescence" (PMID:34825999); dural ectasia prevalence is estimated "between 63 and 97%" (PMID:34825999). Cohort data: "Scoliosis was identified in fifty-two of the eighty-two patients, and the prevalences for the sexes were equal." in skeletally immature patients, and curves over 50 degrees "had marked progression (mean, 3 +/- 4 degrees per year)" (PMID:7782359); in 131 adults, "Scoliosis with a Cobb angle of ≥10° was identified in 116 patients (88.5%)." with severe scoliosis in 40.5%, predicted by female sex and a positive wrist sign (PMID:34228694). Joint laxity is common: "Considerable joint hyperextensibility (> 3/9 of Beighton's criteria) was present in 85%." of children, and "In adult patients, locomotor symptoms had occurred in 96%" (PMID:7704457). Pectus excavatum and carinatum prevalences were 13.6% and 12.4% in a Mexican Ghent cohort (PMID:30532108). Craniofacially, "The high and narrow palatal vault as well as maxillary and mandibular retrognathy were strongly correlated to the syndrome." and "About 70% of the Marfan syndrome patients (n = 76) had been referred for orthodontic treatment" (PMID:10100050). In 87 Ghent-positive adults, "The most prevalent major criterion in Ghent-positive persons was dural ectasia (91%), followed by major genetic criterion (89%) and ectopic lenses (62 %)" (PMID:19293838). In 100 hospital patients, "Eleven patients had a history of spontaneous pneumothorax, which had been recurrent in 10 cases and bilateral in six" (PMID:6495247). "The prevalence of sleep apnea in patients with MFS is much higher than in age- and sex-matched controls, with a range of 32% to 64% of patients being affected" (PMID:34795948). Reduced bone mineral density is reported but "the clinical significance of this change has not been fully elucidated" (PMID:34825999).

**Behavioural/psychological and quality-of-life impact.** No primary behavioural phenotype is part of MFS, but psychosocial burden is substantial. A systematic review found "Decreased quality of life; challenges in education, work and family life, depression and anxiety" (PMID:24813698). SF-36 scores were "reduced scores on all eight subscales of Short Form 36 compared with the general population" in 84 Norwegian adults, and the reduction "does not seem to be related to biomedical criteria or symptoms of Marfan syndrome" (PMID:20613543). Over 10 years, "a significant decline was found in the physical domain. The mental domain was unchanged" (PMID:33256748). In GenTAC (n=389, SF-36 PCS), "health-related QOL was below the population norm" and "insurance status and employment remained significant predictors of QOL" (PMID:28595698). EQ-5D-5L data from 102 German adults showed lower scores "in the dimensions of pain/discomfort, anxiety/depression, mobility and usual activities" than adults with congenital heart disease (PMID:33968637). Per-phenotype QoL: pain — "Eighty-nine percent of respondents reported having pain with 28% of individuals reporting pain as a presenting symptom of Marfan syndrome" (PMID:27862906), with prevalence "varying from 47 to 92%" across studies and "chronic pain limits daily function" (PMID:26607862); fatigue — "Severe fatigue was experienced by 37% of the total MFS cohort (n = 155)" (PMID:36059006), and "only pain interference was associated with fatigue" in the French ComPaRe cohort (PMID:40646614); in a Norwegian study "chronic pain and employment status were significantly associated with fatigue" (PMID:24719044). Severe scoliosis was only weakly related to reduced physical HRQoL (PMID:33256748).

**Laboratory abnormalities.** MFS has no routine diagnostic laboratory abnormality; plasma homocysteine is measured to exclude homocystinuria (PMID:27778219). Research biomarkers include elevated plasma nitrated proteins and cGMP (PMID:33976159) and NT-proBNP, which was associated with ventricular arrhythmia (PMID:24349050).

## 4. Genetic/Molecular Information

**Causal gene.** FBN1 is HGNC:3603 (fibrillin 1), located at 15q21.1, with OMIM gene entry 134797 and MANE transcript NM_000138.5 (HGNC:3603). UniProt P35555 describes a 2871-amino-acid precursor, "Fibrillin-1", that also contains the C-terminal hormone "Asprosin" (UniProt:P35555). The UniProt feature table annotates 47 EGF-like domains (43 annotated as calcium-binding) and 9 TB domains, plus an N-terminal FUN domain and two hybrid domains (UniProt:P35555). Sakai et al. note that "FBN1 encodes the gene for fibrillin-1, a structural macromolecule that polymerizes into microfibrils" (PMID:27437668), and Sakai and Keene that "Marfan mutations can occur in any of the 56 domains that compose fibrillin-1" (PMID:30219651). No other gene causes MFS as defined by OMIM:154700; TGFBR1/TGFBR2 variants in Marfan-like patients represent Loeys–Dietz syndrome (PMID:20372188; PMID:24577266). Gene identifiers for other loci named in this report: TGFBR1 HGNC:11772 (transforming growth factor beta receptor 1), TGFBR2 HGNC:11773 (transforming growth factor beta receptor 2), TGFB1 HGNC:11766 (transforming growth factor beta 1) (see `ols-mondo-hgnc-terms.md`).

**Variant classes and spectrum.** More than 3000 FBN1 mutations are known, most causing MFS (PMID:30219651). In 1013 probands the distribution was "56% missense mutations; 17% frameshift mutations; 14% nonsense mutations; 11% splice mutations; 2% in-frame deletions" (PMID:20372188). In a 292-proband US laboratory series, "Testing yielded 207 pathogenic or likely pathogenic FBN1 variants, with 114/207 (55%) missense, 67/207 (32%) non-sense or frameshift, and 28/207 (13%) splicing" (PMID:25652356). Large deletions occur: one patient had a deletion of exons 1–5 and three had "a 542 Kb deletion spanning the whole FBN1 gene and five additional genes" (PMID:21936929); MLPA found FBN1 deletions in 2% of sequencing-negative patients (PMID:20372188).

**Classification (ACMG/AMP).** The ClinGen FBN1 Variant Curation Expert Panel adapted ACMG/AMP rules: "The developed specifications introduce modifications to 14 of the 28 ACMG/AMP evidence criteria and deem 6 criteria non-applicable", including an FBN1-specific PVS1 flowchart, and "this VCEP has curated 120 variants which have been deposited to ClinVar with the 3-star review status" (PMID:39741318). Before this, ClinVar submissions were discordant: "Conflicting variant classifications occurred in 30.7% of the missense variants that had multiple submitters", and cysteine critical-residue variants were more often classified (likely) pathogenic (91.3%) than non-cysteine critical residues (55.3%) (PMID:31227806).

**Population allele frequency.** Using gnomAD v2.1.1, "Our strategy identified predicted pathogenic FBN1 variants in one in 416 individuals", with the highest frequency in East Asians (one in 243) and lowest in Ashkenazim (one in 5185); ClinVar/LOVD-classified pathogenic variants gave frequencies of one in 718 and one in 1014, and "Null variants which are associated with aortic aneurysms affected only one in 8624" (PMID:40102521). These are computational predictions, and the authors note that "many of those affected still have a milder phenotype" (PMID:40102521). FBN1-specific constraint metrics (pLI/LOEUF) were not retrieved; only the general gnomAD constraint framework is in the evidence set (PMID:32461654).

**Somatic vs germline.** MFS is a germline disorder. Somatic mosaicism matters in transmitting parents: in 30 apparently de novo families, deep sequencing detected "somatic mosaicism in one of the progenitors, with a rate of 6.6% (2/30) of apparently de novo cases" (PMID:33910934), and recurrence in two sisters born to unaffected parents was attributed to maternal germline mosaicism (PMID:10090884). Somatic cancer databases (COSMIC) are not relevant.

**Functional consequences.** Two mechanistic classes are recognised. Franken et al. classified mutations as "(1) haploinsufficiency, decreased amount of normal fibrillin-1, or (2) dominant negative, normal fibrillin-1 abundance with mutant fibrillin-1 incorporated in the matrix" (PMID:25613431). Mouse data favour a dominant contribution of reduced wild-type protein: "These data are consistent with a model that invokes haploinsufficiency for WT fibrillin-1, rather than production of mutant protein, as the primary determinant of failed microfibrillar assembly" (PMID:15254584). In a cell-based assay, MFS-associated substitutions in TB4/TB5 "result in a loss of recombinant protein in the culture medium and no association with microfibrils", unlike stiff skin syndrome and acromelic dysplasia substitutions (PMID:25979247). No gain-of-function mechanism is established for MFS itself.

**Genotype–phenotype correlations.** HI variants carry higher cardiovascular risk: "patients with a haploinsufficient (HI) mutation had a 2.5-fold increased risk for cardiovascular death" (PMID:26787436); a 2025 meta-analysis found HI variants associated with "a 2.5-fold increased risk of developing an aortic presentation compared with dominant negative (DN) variants (pooled RR 2.62" and cysteine-involving missense with adverse aortic events (PMID:41309212). In 1,575 probands and relatives, "Premature termination codon variants were not only associated with a shorter life expectancy and a high lifelong risk of aortic event" but also with severe scoliosis and less ectopia lentis surgery (PMID:33731877). Aortic events occurred at a median age of 29 years with truncating/splicing variants vs 51 years with missense (PMID:25101912). Ectopia lentis is DN-associated: "Ectopia lentis was more frequent in patients with dominant-negative (DN) variants (61%) than in those with haploinsufficient variants (27%)" (PMID:35058154). In 1,013 probands, "A higher probability of ectopia lentis was found for patients with a missense mutation substituting or producing a cysteine, when compared with other missense mutations." and "Exon 24-32 mutations define a high-risk group for cardiac manifestations associated with severe prognosis at all ages." (PMID:17701892). The "neonatal region" is a classic correlation: "The so-called neonatal region in FBN1 exons 24-32 comprises one of the few generally accepted genotype-phenotype correlations described to date" (PMID:11175294), yet "It is not possible to predict whether a given mutation in exons 24-32 will be associated with classic, atypically severe, or neonatal Marfan syndrome" (PMID:11175294). In children, one study found "There was no difference in aortic root growth between children with dominant negative (DN) or haploinsufficient FBN1 mutations" but more severe disease with cysteine-loss DN variants (PMID:36543362) — a point of disagreement with adult data. In UMD-FBN1, neonatal MFS is a small minority: "a total of 1,318 different FBN1 mutations for MFS have been included to date, of which only 59 (4.8 %) including 37 missense mutations (2.8 %) are associated with nMFS" (PMID:27138491).

**Allelic disorders (same gene, different MONDO entities).** UniProt lists ectopia lentis 1 isolated, Weill–Marchesani syndrome 2, MASS/overlap connective tissue disease, stiff skin syndrome, geleophysic dysplasia 2, acromicric dysplasia and Marfanoid-progeroid-lipodystrophy syndrome (UniProt:P35555). Acromelic dysplasia variants are "confined to only certain domains" and produce phenotypes "the opposite of those found in Marfan syndrome" (PMID:30219651); MPL syndrome variants all "occurred in exon 64 of the FBN1 gene" (PMID:26860060).

**Modifier genes.** See Section 2: polygenic gMod loci, including gMod-M2 co-localising with PRKG1 and gMod-M3 with a metalloprotease cluster (PMID:30087447); mouse QTL mapping identified loci in which "Epistatic interactions between the QTL account for 47.4% and 53.5% of variation in the skeletal and cardiovascular phenotypes" (PMID:26927851). Pharmacogenetic modifiers are discussed in Section 12.

**Epigenetic information.** Human evidence is limited. In aortic SMCs from thoracic aneurysms (MFS n = 14, plus bicuspid and degenerative aneurysms), "the increases in H3K9/14 acetylation and H3K4 methylation are involved in Smad2 overexpression in TAA, in a cell-specific and transcription start site-specific manner" (PMID:20829218) — a shared, not MFS-specific, histone-mark mechanism. In Fbn1 C1039G/+ mice, the microRNA miR-29b "is increased in the ascending aorta of Marfan (Fbn1(C1039G/+)) mice" and "miR-29b blockade by locked nucleic acid antisense oligonucleotides prevented early aneurysm development, aortic wall apoptosis, and extracellular matrix deficiencies" (PMID:22116819). A 2025 review summarises DNA methylation work, noting "methylation changes in the FBN1 locus and their effects on fibrillin-1 expression" but that "tissue-specific methylation patterns, especially in smooth muscle cells of the aorta, remain poorly understood" (PMID:40370619). In mice, variability among congenic 129/Sv heterozygotes was taken to suggest "involvement of epigenetic factors in disease severity" (PMID:21152435). No ENCODE/Roadmap or MethBase MFS dataset was retrieved.

**Chromosomal abnormalities.** MFS is not a chromosomal disorder, but contiguous deletions of 15q21.1 encompassing FBN1 cause MFS (542 kb deletion including SLC24A5, MYEF2, CTXN2, SLC12A1 and DUT) (PMID:21936929).

## 5. Environmental Information

**Environmental factors.** None cause MFS. Agents that may aggravate aortic disease are pharmacological: calcium channel blockers (PMID:26506064) and, at least in mice, fluoroquinolones (PMID:34586071), with conflicting human data (PMID:36823078). The FDA issued a December 2018 warning on fluoroquinolone-associated aortic aneurysm/dissection that "specifically targeted older adults and patients with conditions such as hypertension, Marfan syndrome", but prescribing did not change afterwards (PMID:39053916). GeneReviews lists agents to avoid, including "agents that stimulate the cardiovascular system, including decongestants and excessive caffeine; agents that cause vasoconstriction, including triptans" and "fluoroquinolone antibiotics, which may exacerbate the predisposition for aneurysm and dissection" (PMID:20301510). No CTD, toxin, radiation or occupational exposure data specific to MFS were retrieved.

**Lifestyle factors.** GeneReviews advises avoiding "Contact sports, competitive sports, and isometric exercise" (PMID:20301510). Evidence is weak: "There are no outcomes studies to help guide recommendations" (PMID:26729892) and "The current guidelines for MFS and exercise are based on limited research" (PMID:41152210). Current guidance has moved toward individualised activity: the 2024 ESC guideline states "Regular moderate aerobic exercise with a level of intensity informed by aortic diameter is recommended in most patients with MFS." (PMID:39210722), and the 2020 ESC sports cardiology guideline that "Competitive sports are not recommended in individuals who are at high risk (Table 14)." while "Participation in competitive or leisure-time sports activities (except power sports) should be considered in low-risk individuals (Table 14)." (PMID:32860412). Mouse data support moderate exercise (PMID:28385916; PMID:28947563). The sedentary lifestyle that may follow exercise restriction is itself a concern (PMID:37208760). Blood-pressure control is emphasised (PMID:31376376). Smoking is linked by the ACC/AHA guideline to distal aortic disease (PMID:36322642); no diet data specific to MFS were retrieved, and for alcohol only the observation that moderate alcohol use was among bivariate correlates of better QoL in GenTAC (PMID:28595698).

**Infectious agents.** Not applicable; MFS has no infectious cause. Bacterial endocarditis appears only as a historical cause of cardiac death (PMID:5011789).

## 6. Mechanism / Pathophysiology

### 6.1 Ordered causal chain (initiating lesion → clinical manifestation)

1. **Heterozygous germline FBN1 pathogenic variant** (missense, often cysteine-affecting; truncating/splice; or deletion) **leads to** either reduced output of normal fibrillin-1 (haploinsufficiency) or incorporation of abnormal fibrillin-1 (dominant-negative) (PMID:25613431; PMID:15254584). *[Human genetic + mouse; demonstrated.]*
2. **Reduced/abnormal fibrillin-1 results in** defective microfibril assembly and deposition in the extracellular matrix (GO:0001527 (microfibril); GO:0030198 (extracellular matrix organization)) — "impaired microfibrillar deposition" in C1039G/+ mice (PMID:15254584) and "defects in fibrillin-1 accumulation" in patient iPSC-derived SMCs (PMID:27893734). *[Mouse + in vitro; demonstrated.]*
3. **Defective microfibrils lead to** weakened elastic fibre networks and loss of tissue homeostasis — GO:0048251 (elastic fiber assembly), particularly in the aortic tunica media — UBERON:0002522 (tunica media). Mouse targeting suggested "fibrillin-1 microfibrils are predominantly engaged in tissue homeostasis rather than elastic matrix assembly" (PMID:9326947), and a threshold model applies: "a threshold phenomenon for the functional collapse of the vessel wall that is based on the level and the integrity of microfibrils" (PMID:10097121). *[Mouse; demonstrated in models.]*
4. **Branch A — growth factor dysregulation.** Loss of microfibrillar sequestration **results in** excess TGF-β activation and signalling (GO:0007179 (transforming growth factor beta receptor signaling pathway); GO:0017015 (regulation of transforming growth factor beta receptor signaling pathway)): "matrix sequestration of cytokines is crucial to their regulated activation and signaling" (PMID:12598898). Angiotensin II type 1 receptor signalling feeds into this, and **leads to** non-canonical ERK1/2 activation — GO:0070371 (ERK1 and ERK2 cascade) —: "noncanonical (Smad-independent) TGFβ signaling is a prominent driver of aortic disease in MFS mice" (PMID:21493862), with AT2 signalling protective (PMID:21493863). MMP-2 contributes to TGF-β activation and Erk1/2 phosphorylation (PMID:22550139). The molecular basis of sequestration is direct binding: "Latent transforming growth factor (TGF) beta-binding proteins (LTBPs) interact with fibrillin-1. This interaction is important for proper sequestration and extracellular control of TGFbeta." and "in fibrillin-1 (Fbn1) null fibroblast cultures, LTBP-1 and LTBP-4 are not incorporated into microfibrils" (PMID:19349279) [GO:0050431 (transforming growth factor beta binding)]. Fibrillin-1 similarly confers latency on BMP-7: "upon binding to fibrillin-1, the BMP-7 complex is rendered into a closed ring shape, which also confers latency to the growth factor" (PMID:27059954). In patients, "circulating total TGF-beta1 concentrations were elevated in patients with MFS compared with control individuals" and fell with losartan or β-blockers (PMID:19635970). *[Mouse; demonstrated in models. Whether this is primary in human aorta is contested — see Branch caveat.]*
   - **Caveat/branch:** In young Fbn1C1039G/+ mice "aortopathy develops in the absence of detectable alterations in SMC TGF-β signaling" and loss of SMC TGF-β signalling worsens disease (PMID:28119285); TGF-β neutralisation "either exacerbated or mitigated TAA formation depending on whether treatment was initiated before" or after aneurysm formation (PMID:25614286); and human aortic RNA-seq "did not identify a distinctive TGF-β gene expression signature in MFS patients" (PMID:35008861). The TGF-β step is therefore best regarded as stage-dependent and partly inferred.
5. **Branch B — mechanosignalling and NO.** Abnormal matrix **leads to** excess nitric oxide signalling through soluble guanylate cyclase and PRKG1 in smooth muscle cells, which dysregulates the actin cytoskeleton: "NO-donors induce Marfan-like aortopathy in wild-type mice", and "Marfan aortopathy in mice is reverted by pharmacological inhibition of soluble guanylate cyclase and cGMP-dependent protein kinase" (PMID:33976159). *[Mouse + human plasma biomarkers; demonstrated in mice.]*
6. **Branch C — metabolic.** Fibrillin-deficient matrix **results in** VSMC mitochondrial dysfunction and mtDNA depletion: "Mitochondrial function of VSMCs is controlled by the extracellular matrix and drives the development of aortic aneurysm in Marfan syndrome" (PMID:33709773); human multi-omics likewise "pointed toward inflammation and mitochondrial dysfunction" (PMID:35008861). *[Mouse + human tissue; causal role shown with Tfam-deficient mice.]*
7. **Signalling/metabolic changes (4–6) lead to** smooth muscle cell phenotypic modulation, apoptosis and loss of contractility (CL:0002539 (aortic smooth muscle cell); GO:0006939 (smooth muscle contraction)): single-cell RNA-seq identified "A distinct cluster of transcriptomically modulated SMCs (modSMCs)" in aneurysm tissue (PMID:32698686); iPSC-SMCs show defects in "contraction and apoptosis", with apoptosis regulated by "the noncanonical p38 pathway" and KLF4 (PMID:27893734). *[Mouse + human scRNA-seq + in vitro.]*
8. **SMC dysfunction plus oxidative stress, inflammation and proteolysis lead to** medial degeneration, elastic fibre fragmentation and "inflammation-mediated elastolysis" (PMID:10097121). Relevant terms are GO:0006954 (inflammatory response) and CL:0000235 (macrophage); macrophage involvement is inferred from histopathology and multi-omics, not from cell-specific studies in the evidence set. Human tissue supports this step: MFS, familial and sporadic aneurysm aortas "had increased numbers of T lymphocytes and macrophages when compared with control aortas" (PMID:18954631), and in 55 patients "increased numbers of CD4+ T-cells were found in the media (p = 0.02) and increased number of CD8+ T-cells (p = 0.003) in the adventitia of the MFS patients" (PMID:22479353). Redox stress: "Increased tyrosine nitration and reactive oxygen species levels were found in the tunica media of human aortic aneurysms and in cultured VSMC." and NOX4 deficiency ameliorated aortic root enlargement in Fbn1C1039G/+ mice (PMID:29471108); xanthine oxidoreductase is increased in patient aortas and allopurinol "halted the progression of aortic root aneurysm in MFS mice" (PMID:36347404). Inflammation appears to be a modifier rather than a primary driver: in mice, "Anti-inflammatory agents do not reduce the aortic dilatation rate in Marfan mice, but possibly increase aortic damage." (PMID:25238161). *[Mouse histopathology; partly inferred.]*
9. **Medial degeneration results in** progressive aortic root dilatation — HP:0002616 (Aortic root aneurysm), which **leads to** aortic regurgitation and, when wall stress exceeds strength, aortic dissection or rupture — HP:0002647 (Aortic dissection); risk rises steeply with diameter ("The risk increased 4 times at diameters ≥50 mm") (PMID:22133496). *[Human clinical.]*
10. **Parallel branches in other tissues:** (a) TGF-β-dependent myxomatous mitral valve change — "TGF-beta antagonism in vivo rescued the valve phenotype" (PMID:15546004) → mitral valve prolapse/regurgitation; (b) impaired distal alveolar septation with TGF-β-driven apoptosis → emphysema and pneumothorax (PMID:12598898); (c) defective ciliary zonule support → ectopia lentis (UniProt defines isolated ectopia lentis as displacement of the lens owing to "defective zonule formation") (UniProt:P35555); (d) skeletal overgrowth and altered bone cell metabolism, inferred largely from mouse models such as Tsk (PMID:17705049). *[Mostly mouse; ocular step inferred from allelic disorder.]*

Upstream mechanisms are steps 1–3 (genetic lesion and matrix defect); steps 4–6 are intermediate signalling/metabolic responses whose relative weights remain debated; steps 7–9 are downstream cellular and tissue consequences that produce the clinical phenotype.

### 6.2 Detail by category

**Molecular pathways.** TGF-β canonical (Smad2) and non-canonical (ERK1/2, JNK1) signalling (PMID:21493862); AT1R/AT2R angiotensin signalling (PMID:16601194; PMID:21493863); PKCβ–ERK in the CCB interaction (PMID:26506064); NO–sGC–cGMP–PRKG1 (PMID:33976159); p38 MAPK and KLF4 in SMC apoptosis (PMID:27893734). Losartan "uniquely inhibited TGFβ-mediated activation of extracellular signal-regulated kinase (ERK), by allowing continued signaling through AT2" (PMID:21493863). KEGG/Reactome pathway mappings were not retrieved.

**Cellular processes.** SMC phenotype modulation with extracellular matrix modulation, collagen synthesis, adhesion and proliferation signatures (PMID:32698686); apoptosis in lung and aorta (PMID:12598898; PMID:27893734); increased proliferation and decreased apoptosis in mitral valve leaflets (PMID:15546004). Cell types: CL:0002539 (aortic smooth muscle cell), CL:0000359 (vascular associated smooth muscle cell), CL:0000057 (fibroblast), CL:0000115 (endothelial cell), CL:0000235 (macrophage), CL:0000138 (chondrocyte), CL:0000062 (osteoblast), CL:0000746 (cardiac muscle cell) (see `ols-cl-terms.md`).

**Protein dysfunction.** Loss of function through haploinsufficiency or dominant-negative interference with multimerisation; cysteine substitutions in cbEGF domains are high-risk (PMID:31227806; PMID:33731877). Cale et al. summarise that "Mutations in FBN1 result in reduced fibrillin-1 expression, or the production of two different fibrillin-1 monomers unable to interact to form functional microfibrils" (PMID:33801742).

**Metabolic changes.** Mitochondrial dysfunction with increased lactate and decreased oxygen consumption in Fbn1-silenced VSMCs, and reversal of aneurysm by nicotinamide riboside in mice (PMID:33709773). In a zebrafish model, RNA-seq showed upregulated leptin-related genes, suggesting links to lipid metabolism (PMID:40128660). No human metabolomic or lipidomic signature was retrieved.

**Immune involvement.** Inflammation is a downstream amplifier rather than an autoimmune cause; "Patients with progressive aortic disease had higher levels of Macrophage Colony Stimulating Factor (M-CSF) in blood." (PMID:22479353), aortic extracts from MFS patients induce macrophage chemotaxis related to elastin-binding protein (PMID:21647416), and mgR/mgR histology "implicates medial calcification, the inflammatory-fibroproliferative response, and inflammation-mediated elastolysis" (PMID:10097121), and human aortic multi-omics highlighted inflammatory pathways (PMID:35008861).

**Tissue damage mechanisms.** Elastic fibre fragmentation, MMP upregulation and apoptosis (PMID:34586071; PMID:22550139); oxidative stress is proposed as a therapeutic target (allopurinol) on the basis of preclinical data (PMID:42752801). NOX4 and xanthine oxidoreductase are the identified ROS sources (PMID:29471108; PMID:36347404); miR-29b links TGF-β/NF-κB signalling to apoptosis and elastin repression (PMID:22116819).

**Biochemical abnormalities.** Abnormal fibrillin metabolism was historically demonstrated in skin and fibroblasts (PMID:1852208). Plasma cGMP and nitrated proteins are elevated in patients (PMID:33976159).

**Molecular profiling.** Transcriptomics: mouse aortic scRNA-seq identified 481 differentially expressed genes between modSMC and SMC subsets and confirmed analogous SMC modulation in human MFS aortic root tissue (PMID:32698686); bulk RNA-seq of 6 human MFS aortas found FBN1 mRNA "highly variable" and no distinct TGF-β signature (PMID:35008861). Combined genome and SMC single-cell transcriptome analysis in patients found that "genes that were dysregulated in MFS were enriched for glycerophospholipid metabolism, immune, potassium channel, and extracellular matrix processes" (PMID:40678173). In 55 patients, "increased expression of inflammatory genes was associated with major clinical features within the MFS patients group" (PMID:22479353). Proteomics: Verhagen et al. used proteomics to confirm inflammatory and mitochondrial findings (PMID:35008861). Metabolomics/lipidomics: none retrieved. Genomic structural features: large deletions (PMID:21936929). Advanced technologies: scRNA-seq (PMID:32698686); CRISPR correction in iPSCs (PMID:27893734); functional genomics screens (CRISPR/RNAi) and spatial transcriptomics — none retrieved.

**GO term suggestions.** GO:0007179 (transforming growth factor beta receptor signaling pathway); GO:0017015 (regulation of transforming growth factor beta receptor signaling pathway); GO:0070371 (ERK1 and ERK2 cascade); GO:0048251 (elastic fiber assembly); GO:0030198 (extracellular matrix organization); GO:0006939 (smooth muscle contraction); GO:0006954 (inflammatory response); GO:0006915 (apoptotic process); GO:0038166 (angiotensin-activated signaling pathway); GO:0060395 (SMAD protein signal transduction); GO:0038060 (nitric oxide-cGMP-mediated signaling); GO:0009060 (aerobic respiration); GO:0022617 (extracellular matrix disassembly); molecular function GO:0050431 (transforming growth factor beta binding); cellular components GO:0001527 (microfibril), GO:0071953 (elastic fiber), GO:0031012 (extracellular matrix), GO:0005604 (basement membrane), GO:0005739 (mitochondrion) (see `ols-go-terms.md` and `ols-extra-terms-round2.md`; GO "extracellular space" was returned as obsolete and is not used).

## 7. Anatomical Structures Affected

**Organ level.** Primary: aorta (UBERON:0000947 (aorta); UBERON:0001496 (ascending aorta); aortic root, for which no UBERON exact label was found — NCIT:C127641 (Aortic Root)), heart valves — UBERON:0002135 (mitral valve), heart — UBERON:0000948 (heart), eye (UBERON:0000970 (eye); UBERON:0000965 (lens of camera-type eye); UBERON:0000966 (retina); zonule approximated by UBERON:0006762 (suspensory ligament of lens)), skeleton (UBERON:0001434 (skeletal system); UBERON:0001130 (vertebral column); UBERON:0000975 (sternum)), dura — UBERON:0002363 (dura mater), lung — UBERON:0002048 (lung) and skin — UBERON:0002097 (skin of body) — (see `ols-uberon-terms.md`). Secondary organ involvement includes the descending aorta (late events) — "The descending aorta is the location of most late clinical" events (PMID:21147864) — the pulmonary trunk, whose "mean diameter had increased significantly compared to baseline" over 10 years (PMID:31825148), and ventricular myocardium (PMID:38816063). Additional structures, with looked-up terms: UBERON:0002137 (aortic valve), UBERON:0002134 (tricuspid valve), UBERON:0002333 (pulmonary trunk), UBERON:0002345 (descending thoracic aorta), UBERON:0001515 (thoracic aorta), UBERON:0001508 (arch of aorta), UBERON:0000964 (cornea), UBERON:0001773 (sclera), UBERON:0001775 (ciliary body), UBERON:0001269 (acetabular part of hip bone) [near match for acetabulum], UBERON:0000977 (pleura), UBERON:0002414 (lumbar vertebra), UBERON:0001684 (mandible) (see `ols-extra-terms-round2.md`). Corneal involvement includes flattening and thinning: "The mean pachymetry value was lower in MFS eyes compared to the controls" (PMID:21726424). Body systems: cardiovascular, ocular, musculoskeletal, respiratory, integumentary and central nervous system coverings (dura) (ORPHA:558; PMID:34825999).

**Tissue and cell level.** Connective tissue, particularly the elastic arterial media, perichondrium and ocular structures (PMID:34475413); principal cells are aortic smooth muscle cells — CL:0002539 (aortic smooth muscle cell), fibroblasts — CL:0000057 (fibroblast), macrophages — CL:0000235 (macrophage), chondrocytes — CL:0000138 (chondrocyte) and osteoblasts — CL:0000062 (osteoblast). Other relevant cell types are CL:4030032 (valve interstitial cell) [near match for cardiac valve interstitial cell] in myxomatous mitral valves (PMID:15546004), CL:0000186 (myofibroblast cell) and CL:0000134 (mesenchymal stem cell); patient-derived induced pluripotent stem cells have no CL term (NCIT:C124144 (Induced Pluripotent Stem Cell) exists) (see `ols-extra-terms-round2.md`). T lymphocytes and macrophages infiltrate the aortic media and adventitia (PMID:18954631; PMID:22479353). Fibrillin-1 "contributes to the regulated activation of the cytokine TGF-beta" in valve tissue (PMID:15546004).

**Subcellular level.** The defect is extracellular: GO:0031012 (extracellular matrix) and GO:0001527 (microfibril). Mitochondria are secondarily involved (PMID:33709773) — GO:0005739 (mitochondrion) (see `ols-extra-terms-round2.md`).

**Localization and lateralization.** Aortic disease is centred on the sinuses of Valsalva/aortic root (PMID:20301510). Ectopia lentis is typically bilateral (UniProt:P35555; PMID:36449672); skeletal and dural features are generally symmetric/axial. Pneumothorax was bilateral in six of 11 patients with a history of pneumothorax in one series (PMID:6495247).

## 8. Temporal Development

**Onset.** Congenital to adult; MedlinePlus states "The features of Marfan syndrome can become apparent anytime between infancy and adulthood" (https://medlineplus.gov/genetics/condition/marfan-syndrome/). Median age at diagnosis was 19.0 years in Denmark (range 0–74) (PMID:26631233) and mean 27.2 years in Korea (https://www.pfmjournal.org/upload/pdf/pfm-2024-00142.pdf). Early-onset ("neonatal") disease presents in the perinatal period; in a systematic review of 55 cases, mortality "during the first 15 months after" birth was 73.68% for prenatally diagnosed cases (PMID:30652519). In 60 probands with cardiovascular features diagnosed before age 1 year, "Among the 60 individuals, 38 had died, 82% died before the age of 1 y, mostly because of congestive heart failure." and "Valvular insufficiencies and diaphragmatic hernia were predictive of shorter life expectancy." (PMID:21135753). In UMD-FBN1, "92.3 % (60/65) of nMFS mutations were de novo" (PMID:27138491). Onset of aortic disease is insidious and asymptomatic; "Average aortic root dilatation in patients with MFS became more pronounced after the age of 8 years" (PMID:36543362).

**Progression.** Progressive, lifelong, with no formal staging system. Aortic root growth averaged "1.9 mm per year" in an untreated-era adult cohort (PMID:8487722); in treated cohorts it is slower (e.g., 0.4 mm/year on losartan or atenolol over 6.7 years) (PMID:30261963). Features continue to emerge in adulthood: over 10 years, "New aortic root dilatation was detected in patients up to 70 years" and ascending aortic pathology rose from 72% to 93% (PMID:31825148); "In Marfan and Loeys-Dietz syndrome, dural ectasia may present or worsen during adulthood" (PMID:30998996); by contrast, "The prevalence and degree of PA remained unchanged after 10 years" (PMID:40075421). Adults are more likely than children to have pneumothorax, scoliosis and striae (PMID:28600386). Course: chronic, progressive, lifelong; episodic acute events (dissection, pneumothorax, lens dislocation) punctuate it.

**Remission.** No spontaneous remission. In treated children, aortic root z-scores decreased slightly ("significantly less than zero, indicating a decrease in the aortic-root diameter" relative to body size) (PMID:25405392), which is treatment-associated stabilisation rather than remission.

**Critical periods.** (1) Childhood and adolescent growth spurts for chest-wall and spinal deformity (PMID:34825999); (2) pregnancy and especially the postpartum period — "Five of 7 aortic dissections, including all 3 type B, and the coronary dissection (75% of all dissections) occurred in the postpartum period" (PMID:27515814); (3) the period after prophylactic root replacement, when type B and distal anastomotic dissection risk rises (PMID:25614422; PMID:42017320); (4) the window before diagnosis — "More than half of the total number of dissections was in patients undiagnosed with MFS at the time of their event" (PMID:27550511).

## 9. Inheritance and Population

**Epidemiology.**

| Population / source | Prevalence (per 100,000) | Incidence | Evidence |
|---|---|---|---|
| Denmark, Ghent-II verified, 1977–2014 | max 6.5 (end 2014) | median 0.19/100,000/year | PMID:26631233 |
| Taiwan NHI, 2000–2012 (ICD-coded) | 10.2 | minimal birth incidence 23.3/100,000 | PMID:24388020 |
| Korea NHIS 2013 (age-standardised) | 2.27 | — | PMID:28244281 |
| Korea NHIS 2017 | 5.70 | 0.51/100,000 | https://www.pfmjournal.org/upload/pdf/pfm-2024-00142.pdf |
| GeneReviews estimate | 1:5,000–1:10,000 | — | PMID:20301510 |
| gnomAD predicted pathogenic FBN1 genotypes | 1 in 416 (genotype, not disease) | — | PMID:40102521 |

Groth et al. caution that the Taiwanese figure was obtained "without any regard to diagnostic criteria or clinical presentation" (PMID:26631233). The Korean study is administrative-code-based (Q87.4) (PMID:28244281).

**Inheritance.** Autosomal dominant — HP:0000006 (Autosomal dominant inheritance). "Approximately 75% of individuals with Marfan syndrome have an affected parent; approximately 25% have a de novo FBN1 pathogenic variant. Each child of an individual with Marfan syndrome has a 50% chance of inheriting the pathogenic variant and the disorder" (PMID:20301510).

**Penetrance and expressivity.** High penetrance with variable expressivity: "Although intrafamilial clinical variability can be extensive, FBN1-related Marfan syndrome shows high clinical penetrance" (PMID:20301510). Penetrance is age-dependent: "The age-dependent penetrance of organ manifestations in Marfan syndrome (MFS) is not known" was the premise of a 10-year follow-up showing emergence of new features in adulthood (PMID:31825148). The 1991 linkage paper describes MFS as "inherited as an autosomal dominant with high penetrance, but has great clinical variability" (PMID:1852208).

**Genetic anticipation.** Not reported; MFS is not a repeat-expansion disorder and no evidence for anticipation was retrieved.

**Germline/somatic mosaicism.** Parental somatic mosaicism in 6.6% of apparently de novo cases (PMID:33910934); confirmed germline mosaicism (PMID:10090884). In cattle, "Bull A exhibited germline mosaicism for the mutation, and that the frequency of the mutant sperm was 14.9%" (PMID:22221020).

**Founder effects.** Most FBN1 mutations are private: "Almost all the identified FBN1mutations have been family specific, and the rate of new mutations is high" (PMID:10090884). No human founder variant was retrieved. No FBN1-specific evidence on a paternal-age effect for de novo variants was retrieved; this remains a gap.

**Consanguinity.** Not relevant to a dominant disorder; one zebrafish-validated FBN1 nonsense variant came from a consanguineous family, but transmission was dominant (PMID:40128660).

**Carrier frequency.** Not applicable in the recessive sense; heterozygotes are affected. Population frequency of predicted pathogenic genotypes is given above (PMID:40102521).

**Population demographics.** gnomAD-predicted pathogenic variants were "most common in East Asian people (one in 243, p < 0.0001) and least common in Ashkenazim (one in 5185" (PMID:40102521), but clinical studies describe MFS as occurring across populations "with no predilection for either sex or ethnicity" (PMID:34795948). **Sex ratio:** Denmark found "no gender differences" (PMID:26631233); Taiwan had 58% men (PMID:24388020); Korea 59.5% male (https://www.pfmjournal.org/upload/pdf/pfm-2024-00142.pdf), and "Males also showed slightly higher prevalence of MFS than females" (PMID:28244281). **Age distribution:** prevalence peaks in adolescence and young adulthood (ages 15–19, 10–14 and 20–24 in Taiwan) (PMID:24388020). **Geographic distribution of specific variants:** no human data; animal variants are breed-specific (Section 14).

## 10. Diagnostics

**Clinical criteria (revised Ghent nosology, 2010).** "aortic root aneurysm and ectopia lentis are the cardinal clinical features. In the absence of any family history, the presence of these two manifestations is sufficient for the unequivocal diagnosis of MFS. In absence of either of these two, the presence of a bonafide FBN1 mutation or a combination of systemic manifestations is required" (PMID:20591885). The seven diagnostic routes (Box 1) and the systemic score items (Box 2) are reproduced in Pollock et al.: e.g., "Wrist AND thumb sign: 3 (wrist OR thumb sign: 1)", pectus carinatum 2, hindfoot deformity 2, pneumothorax 2, dural ectasia 2, protrusio acetabuli 2, and "Myopia > 3 diopters: 1"; a systemic score ≥7 is required in the relevant routes (PMID:34825999). The earlier 1996 Ghent criteria required "skeletal involvement as a major criterion if at least 4 of 8 typical skeletal manifestations are present" (PMID:8723076). In 1009 FBN1-positive probands, "A total of 842 patients could be classified as MFS according to the new nosology (83%) as compared to 894 (89%) according to the 1996 Ghent criteria" (PMID:21564093); in adults, revised criteria retained the diagnosis in 91% and "Currently used Z-scores seem to underestimate aortic root dilatation, especially in patients with large body surface area (BSA)" (PMID:21332468). Ghent-1 and Ghent-2 perform similarly but "Ghent-2 is easier to use" (PMID:26124674).

**Laboratory tests and biomarkers.** No diagnostic blood test. Total plasma homocysteine excludes CBS deficiency: "We strongly recommend measuring the plasma total homocysteine concentrations in any patient whose clinical features suggest the diagnosis" (PMID:27778219) — CHEBI:17230 (homocysteine). Exploratory biomarkers: plasma cGMP and nitrated proteins (PMID:33976159); NT-proBNP for arrhythmic risk (PMID:24349050). Circulating total TGF-β1 has been proposed as a prognostic and therapeutic marker: it "might serve as a prognostic and therapeutic marker in MFS" (PMID:19635970), and plasma TGF-β was higher in patients with aortic root dilatation (124 pg/ml vs 10 pg/ml) (PMID:22479353). No FDA-qualified biomarker exists in the evidence set.

**Imaging.** Transthoracic echocardiography with BSA-indexed aortic root Z-scores is the primary tool; CT or MRI images the whole aorta and dura (NCIT:C16525 (Echocardiography Test); NCIT:C16809 (Magnetic Resonance Imaging)). The 2024 ESC commentary states that "Both genetic testing and imaging—mainly through transthoracic echocardiography, cardiovascular magnetic resonance, or cardiovascular computed tomography if the aortic root/ascending aorta is not well visualized—are essential for diagnosing hereditary thoracic aortic disease in patients and family members" (PMID:39210722). GeneReviews recommends annual echocardiography when dimensions are small and growth slow, more frequent imaging above about 4.5 cm or growth over 0.3 cm/year, and "Intermittent surveillance of the entire aorta with CT or MRA scans beginning in young adulthood" (PMID:20301510). The 2022 ACC/AHA guideline recommends "a TTE is recommended at the time of initial diagnosis, to determine the diameters of the aortic root and ascending aorta, and 6 months thereafter" with annual TTE if stable, CT or MRI of the thoracic aorta in adults, and after root replacement "surveillance imaging of the thoracic aorta by MRI (or CT) is recommended to evaluate for distal TAD, initially annually and then, if normal in diameter and unchanged after 2 years, every other year." (PMID:36322642). The 2024 ESC guideline recommends TTE "At least annually in patients with an aortic root diameter <45 mm in the absence of additional risk factors." and, after root replacement, CMR or CCT "at least every 3 years" (PMID:39210722). Relevant NCIT terms: NCIT:C17204 (Computed Tomography), NCIT:C75583 (Slit-lamp Examination), NCIT:C38064 (Holter Monitoring). Lumbosacral MRI/CT assesses dural ectasia; a dural sac ratio cut-off at S1 of 0.64 has been suggested (PMID:30998996). CT circle-wall distance (cut-off 2 mm) assesses protrusio acetabuli (PMID:40075421). Because ectopia lentis is a cardinal criterion (PMID:20591885), ophthalmological examination is part of the work-up; in a Norwegian cohort, lens position was assessed "by observing the eye in different gaze directions in maximal mydriasis during slit lamp examination" (PMID:24853997).

**Functional tests and electrophysiology.** Holter monitoring: "Twenty subjects (7%) had significant VE, 13 (5%)" had significant SVE, among 274 young patients (PMID:30115424); in adults, ventricular arrhythmia related to NT-proBNP, LV size, mitral regurgitation and QTc (PMID:24349050). Polysomnography detects sleep apnea (PMID:34795948). Pulmonary function testing data were not retrieved.

**Biopsy/pathology.** Not used diagnostically. Aortic histopathology shows medial degeneration with elastic fibre fragmentation; mouse and bovine studies describe "disorganized elastin and narrowed elastic lamina separated by widened spaces" (PMID:15776436).

**Genetic testing.** Recommended approach: FBN1 sequencing plus deletion/duplication analysis, typically within multigene heritable thoracic aortic disease panels. The gene card describes sequencing of exons with flanking introns and, when negative, "a search for FBN1 genomic rearrangements by MLPA or related techniques could be proposed in clinically convincing cases" (PMID:20372188). Yield in Ghent-positive patients: 82% (87/104) (PMID:25652356); 72.5%–93% in earlier series (PMID:20372188); 91% in a severe paediatric cohort using targeted resequencing and deletion/duplication testing (PMID:35058154). Testing is not mandatory for diagnosis but carries "greater weight in the diagnostic assessment" (PMID:20591885). Genetic testing "can help distinguish MFS from other heritable thoracic aortic disease syndromes" (PMID:34475413). Variant interpretation should use ClinGen FBN1 VCEP rules (PMID:39741318). WES/WGS: useful when panels are negative and in research; zebrafish-validated discovery of a novel FBN1 nonsense variant came from WES (PMID:40128660); no MFS-specific diagnostic-yield data for WES/WGS were retrieved. Relevant NCIT terms: NCIT:C116161 (Multiplex Ligation-dependent Probe Amplification), NCIT:C101295 (Whole Exome Sequencing), NCIT:C101294 (Whole Genome Sequencing); no NCIT exact term for "Gene Panel" was found. Chromosomal microarray can define whole-gene deletions (a chromosome 15 array defined a 542 kb deletion) (PMID:21936929). Karyotype, FISH, mitochondrial DNA testing and repeat-expansion testing are not applicable.

**Omics-based diagnostics.** None are clinically established; RNA-seq, proteomics, metabolomics and epigenomics are research tools only (PMID:35008861). Liquid biopsy is not applicable.

**Differential diagnosis.** Loeys–Dietz syndrome — "A major distinguishing feature from Marfan syndrome is the lack of lens dislocation in LDS" and LDS has widespread arterial tortuosity and aneurysms (PMID:24577266); patients "with LDS have a high risk of aortic dissection at small diameters" (https://onlinecjc.ca/article/S0828-282X(14)00112-3/fulltext). Homocystinuria (CBS deficiency) — ectopia lentis, learning difficulties, skeletal abnormalities and thromboembolism, distinguished by homocysteine (PMID:27778219). Shprintzen–Goldberg syndrome, MONDO:0008426 (Shprintzen-Goldberg syndrome), and vascular Ehlers–Danlos syndrome are named as exclusions in the Ghent caveat (PMID:34825999). MASS phenotype and ectopia lentis syndrome capture FBN1 carriers without aortic dilatation (PMID:21564093; PMID:21332468). Congenital contractural arachnodactyly is caused by FBN2 variants (PMID:37972149). Marfanoid hypermobility syndrome exists as MONDO:0007948 (marfanoid hypermobility syndrome) (see `ols-mondo-hgnc-terms.md`). Additional distinguishing features from primary sources: Shprintzen–Goldberg syndrome "has considerable phenotypic overlap with MFS and LDS, including aortic aneurysm" and is caused by variants in SKI (PMID:23023332); vascular Ehlers–Danlos syndrome (COL3A1) causes arterial, bowel and uterine rupture, with "The calculated median survival of the entire cohort was 48 years." (PMID:10706896), and molecular confirmation is required for all EDS types except hypermobile EDS (PMID:28306229); congenital contractural arachnodactyly (FBN2) is "characterized by crumpled ears, arachnodactyly, contractures, and scoliosis" and may also show aortic root dilatation, "a finding previously thought to differentiate the condition from Marfan syndrome (MFS)" (PMID:19006240); autosomal recessive isolated ectopia lentis is caused by ADAMTSL4 (PMID:19200529); ACTA2-related familial thoracic aortic aneurysm lacks the systemic features and "ACTA2 mutations are the major cause of familial thoracic aortic aneurysms and dissections" (PMID:25759435).

**Screening.** No newborn or population screening exists. Cascade screening of at-risk relatives is recommended: "It is recommended that the genetic status of at-risk relatives of any age be clarified" by familial variant testing or clinical criteria (PMID:20301510). Parental deep sequencing in apparently de novo cases is advised (PMID:33910934).

## 11. Outcome/Prognosis

**Survival and mortality.** Historical: "The average age at death for the 72 deceased patients was 32 years" and "Cardiac problems led to 52 of the 56 deaths of known cause, with aortic dilatation and its complications accounting for 80 per cent of these" (PMID:5011789). By 1993, "Median (50%) cumulative probability of survival in 1993 was 72 years compared with 48 years in 1972" (PMID:7810492); "Of 112 surgically treated patients, 10-year probability of survival was 70%" (PMID:7810492). UK genetic clinics: "50% median cumulative survival in the total cohort (n=206) was 53 years for males and 72 years for females" (PMID:9761390). Modern registries: Danish data showed a "significantly decreased lifespan of 50years compared with 60years among" controls, a mortality hazard ratio of 3.6, and aortic disease as the main reason for excess mortality ("mortality with a hazard ratio of 194.6") (PMID:30149886); Norwegian SMR "5.24 (3.00-8.51); for men: 8.20 (3.54-16.16); for women: 3.85 (1.66-7.58)" (PMID:30393980); Dutch CONCOR "After 10-year follow-up cumulative survival was 93.8% and dissection-free survival was 84.2%" (PMID:26787436); Korean 10-year survival 92.7% (https://www.pfmjournal.org/upload/pdf/pfm-2024-00142.pdf). Taiwan reported average annual mortality of 0.23%, mostly cardiac (PMID:24388020). A Chinese surgical referral cohort with large aortas had poor survival ("48.7%" at 10 years) (PMID:42288721), reflecting late presentation. GeneReviews states that "With proper management, the life expectancy of someone with Marfan syndrome approximates that of the general population" (PMID:20301510). **Disease-specific mortality:** In Norway, "Cardiovascular causes were found in 11 of 16 deceased, eight of these related to aortic pathology" (PMID:30393980); Danish data found unexplained excess respiratory mortality "not attributed to pneumothorax" (PMID:30149886).

**Morbidity and function.** Aortic events affected 36.4% of the Danish cohort, with 50% event-free at age 49.6 (PMID:27550511). At 10-year follow-up in Norway, "51% had new cardiovascular events; 59% had undergone aortic surgery" (PMID:30393980). Disability: pain-related disability is moderate (PMID:27862906); participants on disability benefits reported higher fatigue (PMID:24719044); unemployment associated with depressive symptoms (PMID:36059006). ICF-coded disability data were not retrieved.

**Quality-of-life measures.** SF-36 (PMID:20613543; PMID:33256748; PMID:28595698; PMID:18448780), EQ-5D-5L (PMID:33968637), FACIT-Fatigue (PMID:40646614), CIS and HADS (PMID:36059006), Fatigue Severity Scale (PMID:24719044), Brief Pain Inventory (PMID:40646614). Fusar-Poli et al. found impairment "in the psychological domain but not in the physical domain" in 36 Italian patients (PMID:18448780), whereas Norwegian data showed reduced scores on all subscales (PMID:20613543) — the instruments and populations differ.

**Complications.** Aortic dissection (type A and B), aortic regurgitation, mitral regurgitation, heart failure, ventricular arrhythmia and sudden death (PMID:33885997), distal anastomotic dissection after root surgery — "with prior root replacement) suffered a distal anastomosis dissection" in 11 patients (5.9% of those with root replacement) (PMID:42017320) — retinal detachment, glaucoma and cataract (PMID:41496654), pneumothorax, scoliosis progression, and obstetric complications ("a markedly increased combined fetal and neonatal mortality of 7.1%") (PMID:16236373).

**Recovery potential.** The connective tissue defect is lifelong and not reversible; outcomes depend on timely surveillance and prophylactic surgery. Elective root replacement has low risk: "There was no operative or hospital mortality among the 327 patients who underwent elective repair" (PMID:19379862). Lens surgery improves visual acuity (PMID:36449672).

**Prognostic factors and biomarkers.** Aortic root diameter (PMID:22133496; PMID:32130918); family history of dissection (PMID:7560600); male sex (PMID:27550511; PMID:28600386); FBN1 variant class (HI/PTC worse) (PMID:26787436; PMID:33731877; PMID:41309212); prior prophylactic root surgery and proximal descending aorta ≥27 mm for type B dissection — "occurrence of type B aortic dissection in low-, moderate-, and high-risk" patients over 10 years was 6%, 19% and 34% (PMID:25614422); late diagnosis (PMID:39306029); LVEDD ≥65 mm in surgical referrals (PMID:42288721); NT-proBNP and FBN1 exons 24–32 for ventricular tachycardia events (PMID:24349050); mitral annular disjunction (PMID:34232254). In a paediatric cohort, rate-of-dilation cut-points had high "specificity, but low sensitivity for predicting referral for aortic surgery" (PMID:29948025).

## 12. Treatment

**Pharmacotherapy.**

- *β-blockers* (CHEBI:35530 (beta-adrenergic antagonist); NCIT:C29576 (Beta-Adrenergic Antagonist); propranolol CHEBI:8499 (propranolol) / NCIT:C62073 (Propranolol); atenolol CHEBI:2904 (atenolol) / NCIT:C28836 (Atenolol)). The only placebo/no-treatment RCT: "The mean slope of the regression line for the aortic-root dimensions, which reflect the rate of dilatation, was significantly lower in the treatment group than in the control group (0.023 vs. 0.084 per year, P < 0.001)" (PMID:8152445). Cochrane judged the evidence low quality: "Beta-blocker therapy did not reduce the incidence of all-cause mortality (RR 0.24, 95% CI 0.01 to 4.75; participants = 70; low-quality evidence)" (PMID:29110304). Mechanism: reducing the rate of pressure change and heart rate (PMID:8152445).
- *Angiotensin II receptor blockers* (NCIT:C66930 (Angiotensin II Receptor Antagonist); losartan CHEBI:6541 (losartan) / NCIT:C66869 (Losartan); irbesartan CHEBI:5959 (irbesartan) / NCIT:C29130 (Irbesartan)). Rationale from mice (PMID:16601194). Trials: COMPARE (adults, open-label) — "Aortic root dilatation rate after 3.1 ± 0.4 years of follow-up was significantly lower in the losartan group than in controls (0.77 ± 1.36 vs. 1.35 ± 1.55 mm, P = 0.014)" (PMID:23999449); Pediatric Heart Network (NCT:NCT00429364) — no difference vs atenolol, z-score slopes −0.139 vs −0.107 per year (PMID:25405392); Marfan Sartan (NCT:NCT00763893) — "Losartan was able to decrease blood pressure in patients with MFS but not to limit aortic dilatation during a 3-year period" (PMID:25935877); Barcelona LOAT — losartan vs atenolol, 1.1 vs 1.4 mm over 3 years, no difference (PMID:26518245), confirmed over 6.7 years (PMID:30261963); Ghent add-on trial (NCT:NCT00782327) — underpowered, no added effect (PMID:28657492; PMID:21239069); AIMS (irbesartan) — "The mean rate of aortic root dilatation was 0·53 mm per year (95% CI 0·39 to 0·67) in the irbesartan group compared with 0·74 mm per year (0·60 to 0·89) in the placebo group" (PMID:31836196). The Marfan Treatment Trialists' IPD meta-analysis (7 trials, 1442 patients): ARB "approximately halved the annual rate of change in the aortic root Z score" vs control, ARB and β-blocker effects were similar, and combination therapy would be expected to provide even greater reductions (PMID:36049495). An earlier aggregate meta-analysis found a 0.13 mm smaller change with losartan but no difference in the composite clinical outcome (PMID:31606871). Long-term COMPARE follow-up suggested fewer clinical events with continued losartan (composite 14 vs 26), non-randomised (PMID:32548624).
- *Drugs to avoid or of uncertain value.* Calcium channel blockers (harm signal) (PMID:26506064); ACE inhibitors lack direct evidence (PMID:20301510); in mice enalapril "was less effective" than losartan (PMID:21493863). Doxycycline — CHEBI:50845 (doxycycline) — delayed manifestations in mice via MMP-2 inhibition (PMID:22550139); a pilot human trial of irbesartan, doxycycline or both (NCT:NCT01949233) has status unknown. Anti-inflammatory drugs (methylprednisolone, abatacept) did not reduce aortic dilatation in Marfan mice (PMID:25238161). Further CHEBI terms: CHEBI:38215 (calcium channel blocker) [NCIT:C333 (Calcium Channel Blocker)], CHEBI:4784 (enalapril), CHEBI:100241 (ciprofloxacin), CHEBI:5775 (hydralazine), CHEBI:15927 (N-ribosylnicotinamide) [nicotinamide riboside], CHEBI:27881 (resveratrol), CHEBI:40279 (allopurinol), CHEBI:61016 (angiotensin receptor antagonist), CHEBI:16480 (nitric oxide), CHEBI:16356 (3',5'-cyclic GMP) (see `ols-extra-terms-round2.md`).
- *Adverse events.* Irbesartan "was well tolerated with no observed differences in rates of serious adverse events" (PMID:31836196); in LOAT "No serious drug-related adverse effects were observed" (PMID:26518245). ARBs should be stopped in pregnancy "because of the increased risk for fetal loss, oligohydramnios, and abnormal development" (PMID:20301510).
- *Pharmacogenomics.* COMPARE substudy: "losartan reduced only aortic root dilatation rate in haploinsufficient patients" (PMID:25613431), and losartan improved biventricular volumes only in HI patients (PMID:27704402); however, LOAT found no differences by DN vs HI (PMID:30261963) and a paediatric cohort found "No difference in the therapeutic response was detected between genotypes" (PMID:35058154). The IPD meta-analysis found larger ARB effects in FBN1-variant carriers (PMID:36049495). ADRB1 rs1801253 CC genotype was associated with greater atenolol response (exploratory) (PMID:32586526), and non-Hispanic White patients responded better to atenolol than losartan (PMID:33845931). No CPIC/PharmGKB guideline exists in the evidence set.

**Advanced therapeutics.** Gene therapy, cell therapy and immunotherapy: none in clinical development in the retrieved evidence. RNA-based: proof-of-concept antisense exon-52 skipping in fibroblasts — "exon 52 can be excluded in up to 100% of FBN1 transcripts" but function of the shortened protein is unknown (PMID:33801742) (in vitro only). Targeted (pathway) candidates from mice: ERK/JNK inhibitors (PMID:21493862), sGC/PRKG inhibitors (PMID:33976159), nicotinamide riboside (PMID:33709773), hydralazine and the PKCβ inhibitor enzastaurin (PMID:26506064), p38/KLF4 (PMID:27893734). Allopurinol has received EMA orphan designation for MFS on the basis of antioxidant effects in mouse models (PMID:42752801). Resveratrol showed a trend to stabilised aortic growth in a single-arm trial (aortic root from 0.39 to −0.13 mm/year, p=0.072) (PMID:39317438).

**Surgical and interventional.** Prophylactic aortic root replacement is the principal intervention (NCIT:C50815 (Aortic Valve Replacement) applies to valve-replacing procedures; no NCIT term was found for "Bentall procedure", "Aortic Root Replacement" or "Valve-Sparing Aortic Root Replacement" — see `ols-chebi-ncit-terms.md`). Thresholds: a 50 mm root diameter "appears to be a reasonable threshold for prophylactic surgery" (PMID:22133496); the Canadian position statement supports "a size threshold of 5.0 cm" for root/ascending aorta and 5.5–6.0 cm for the descending aorta (https://onlinecjc.ca/article/S0828-282X(14)00112-3/fulltext); GeneReviews adds growth of 0.5–1.0 cm/year or progressive severe aortic regurgitation as indications (PMID:20301510). The 2022 ACC/AHA guideline: "In patients with Marfan syndrome and an aortic root diameter of ≥5.0 cm, surgery to replace the aortic root and ascending aorta is recommended." and surgery at ≥4.5 cm is reasonable with features associated with increased dissection risk; "Indications for earlier aortic surgery may include rapid aortic growth (≥0.3 cm/y), family history of aortic dissection, desire for pregnancy, severe valve regurgitation, and patient preference." (PMID:36322642). The 2024 ESC guideline: "Surgery is indicated in patients with MFS who have aortic root disease with a maximal aortic sinus diameter ≥50 mm. Class I, Level B", "Surgery should be considered in patients with MFS who have an aortic root aneurysm with a maximal aortic sinus diameter ≥45 mm and additional risk factors." and "Open surgery is preferred over endovascular procedures in patients with MFS." (PMID:39210722). Valve-sparing reimplantation (David) vs composite valve graft (Bentall): a meta-analysis of 2,156 patients found in-hospital mortality "favoured the RAV procedure with an odds ratio of 0.23" and long-term freedom from valve reintervention 97.6% vs 88.6% (PMID:29893811); another of 2,976 patients found VSRR reduced thromboembolism and bleeding with "no significant difference in reintervention rates" (PMID:29270369); single-centre David I outcomes were "91% at 10 years and 76% at 20 years" survival with freedom from aortic-valve reoperation of 86% and 80% (PMID:30169770); one US series noted greater valvular-structural deterioration after valve-sparing without survival impact (PMID:37554715). Endovascular repair (TEVAR) for type B dissection is a bridge or adjunct with "high rates of reintervention" (PMID:41609261). Non-cardiac surgery: lens extraction with or without IOL (PMID:36449672; PMID:41496654); scoliosis bracing/fusion and pectus repair (Ravitch/Nuss) (PMID:34825999; PMID:20301510). (NCIT:C157986 (Spinal Fusion); no NCIT term for Nuss procedure, lensectomy or thoracic endovascular aortic repair was found.)

**Supportive and rehabilitative care.** Multidisciplinary care (geneticist, cardiologist, ophthalmologist, orthopaedist, cardiothoracic surgeon) is "strongly recommended" (PMID:20301510). Physical therapy, analgesics or anti-inflammatories for protrusio acetabuli; orthotics for pes planus; orthodontia (PMID:20301510). (NCIT:C15302 (Physical Therapy).) Pain management may improve fatigue and QoL (PMID:40646614); psychological interventions such as cognitive behavioural therapy have been suggested (PMID:36059006); rehabilitation programmes are needed (PMID:26607862). (NCIT:C15240 (Genetic Counseling).)

**Experimental treatments (registered trials).** NCT:NCT00429364 (atenolol vs losartan, completed); NCT:NCT00763893 (Marfan Sartan, terminated); NCT:NCT00782327 (Ghent losartan add-on, completed); NCT:NCT01949233 (irbesartan/doxycycline pilot, status unknown); AIMS was ISRCTN90011794 (PMID:31836196); COMPARE was NTR1423 (PMID:25613431).

**Treatment strategy.** At diagnosis, start β-blocker and/or ARB: "In patients with MFS, treatment with either a BB or an ARB, in maximally tolerated doses (unless contraindicated), is recommended to reduce the rate of aortic dilatation. Class I, Level A" and the combination "should be considered" (Class IIa) (PMID:39210722); the ACC/AHA guideline similarly finds "the use of both a beta blocker and an ARB, in maximally tolerated doses (unless contraindicated), is reasonable to reduce the rate of aortic dilation" (PMID:36322642); serial imaging; prophylactic root surgery near 50 mm or with rapid growth; whole-aorta surveillance after root surgery; pregnancy counselling; avoidance of CCBs, fluoroquinolones, stimulants and isometric/contact sports (PMID:20301510). Combination ARB + β-blocker is supported by assumed additivity (PMID:36049495). Genotype-guided therapy remains investigational (PMID:25613431; PMID:32586526).

## 13. Prevention

**Primary prevention.** Not possible at population level (germline dominant disorder, ~25% de novo). Reproductive options for affected families: prenatal diagnosis by CVS "at about 10–12 weeks of gestation" when the familial variant is known (PMID:20372188), and preimplantation genetic testing — first reported live birth "free of a Marfan mutation" in 1996 (PMID:9239687); a review calls PGD "the technique of choice" to ensure an unaffected pregnancy (PMID:26903455). A multicentre series reported 15 prenatal/PGD procedures in nine families and noted that "molecular diagnosis cannot predict clinical severity of the disease" (PMID:11810645).

**Secondary prevention (early detection).** Cascade testing of relatives (PMID:20301510); early diagnosis matters because late diagnosis predicts death (PMID:39306029) and many dissections occur in undiagnosed patients (PMID:27550511; PMID:33052376). "Most pregnancy-related aortic dissection is due to an aortopathy often not diagnosed until after aortic dissection" (PMID:33052376). No newborn screening or USPSTF recommendation exists.

**Tertiary prevention.** Medical therapy, imaging surveillance and timely prophylactic surgery (Sections 10–12); pregnancy management with serial echocardiography "every two to three months during pregnancy" and postpartum monitoring (PMID:20301510). Guidelines differ on pregnancy thresholds: "caesarean delivery when the aortic root diameter is ≥40 mm in the 2010 American guidelines versus >45 mm in the 2011 European guidelines" (PMID:30243228); a dilated root of ">40 to 45 mm" is "considered a relative contraindication for pregnancy" (PMID:27788933). In a 169-woman cohort, "Pregnancy-related type A dissection only occurred in patients unaware of their diagnosis" and "Type B dissection remains an unpredictable complication" (PMID:34446158). Current guidelines: ACC/AHA — "In patients with Marfan syndrome and an aortic root diameter of >4.5 cm, aortic surgery before pregnancy is recommended." (PMID:36322642); ESC 2024 — "Prophylactic aortic root surgery is recommended in women desiring pregnancy with aortic diameters >45 mm." and "ARBs are not recommended during pregnancy." (PMID:39210722); ESC 2025 pregnancy guideline — "In women with MFS and aortic root diameters >45 mm, surgery before pregnancy is recommended." and "Beta-blocker therapy throughout pregnancy and in the post-partum period is recommended in women with MFS and other HTADs." with "In women with an aorta ≥45 mm, caesarean section should be considered." (PMID:40878294). It also notes "Aortic event rates can reach up to 10%." (PMID:40878294). (NCIT:C46088 (Cesarean Section); NCIT:C92755 (Chorionic Villus Sampling); NCIT:C52009 (Amniocentesis); no NCIT exact term for preimplantation genetic diagnosis was found.)

**Immunization.** Not applicable.

**Risk stratification.** Aortic diameter and growth, family history of dissection, FBN1 variant class, sex, prior root surgery, descending aorta size (Section 11) (PMID:25614422; PMID:33731877). Arnaud et al. state that "A risk chart could be established with clinical and genetic data" (PMID:33731877).

**Behavioural interventions.** Exercise moderation (avoid contact, competitive and isometric exertion) and avoidance of cardiovascular stimulants (PMID:20301510); evidence is limited (PMID:41152210).

**Counseling.** Genetic counselling (NCIT:C15240 (Genetic Counseling); NCIT:C15709 (Genetic Testing)) covers the 50% transmission risk, variable expressivity, parental mosaicism and reproductive options (PMID:20301510; PMID:33910934). Prenatal counselling is complicated because "Practical use of prenatal diagnosis remains difficult because of the extremely broad variability of clinical expression" (PMID:20372188).

**Public health and environmental interventions.** Awareness in emergency and cardiac settings is advocated because FBN1 variants are more common than diagnosed disease (PMID:40102521). Regulatory warnings (fluoroquinolones) have had limited effect on prescribing (PMID:39053916).

**Prophylaxis.** β-blockers/ARBs (pharmacological prophylaxis of aortic growth) and prophylactic aortic surgery (Section 12).

## 14. Other Species / Natural Disease

**Taxonomy and orthologs.** FBN1 orthologues (NCBI Gene IDs): human 2200, mouse Fbn1 14118 (aliases include Tsk), cattle 281154, dog 478293, horse 100055741, zebrafish fbn1 100330961, rabbit 100350931, pig 414836, rat Fbn1 83727 (https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&id=14118,2200,281154,478293,100055741,100330961,100350931,414836,83727). Taxa: NCBITaxon:9606 (Homo sapiens), NCBITaxon:10090 (Mus musculus), NCBITaxon:9913 (Bos taurus), NCBITaxon:9823 (Sus scrofa), NCBITaxon:7955 (Danio rerio), NCBITaxon:9615 (Canis lupus familiaris), NCBITaxon:9986 (Oryctolagus cuniculus) (see `ncbitaxon-terms.md`). Additional taxa: NCBITaxon:9796 (Equus caballus), NCBITaxon:10116 (Rattus norvegicus), NCBITaxon:6239 (Caenorhabditis elegans), NCBITaxon:9031 (Gallus gallus); a review lists "chicks, cattle, mice, pigs, zebrafishes, Caenorhabditis elegans, and rabbits" among species used in MFS research (PMID:39834548).

**Naturally occurring disease.** OMIA:000628 "Marfan syndrome, FBN1-related" lists dog, pig, taurine cattle and rabbit (pig and rabbit entries are engineered) (https://www.omia.org/OMIA000628/). *Cattle (Bos taurus):* Limousin calves carry a missense variant "3598G>A transition in exon 29, resulting in a likely substitution of a glutamic acid by lysine at position 1200" (PMID:15776436), with autosomal dominant inheritance and features including ectopia lentis and aortic dilatation, aneurysm and rupture (PMID:15776436); Japanese Black cattle carry "A G>A mutation at the intron64 splicing accepter site (c.8227-1G>A)" detected "in 31 of 36 affected animals (84.7%)" (PMID:22221020). VBO breed identifiers were not looked up. *Dog:* a 10-month-old Golden Retriever with cardiac enlargement, pneumothorax and joint hypermobility had "a 3618 base pair deletion encompassing exon 24 of the FBN1 gene" (PMID:42815455). *Horse:* a de novo FBN1 p.(Ala882Val) variant is "the likely cause of ectopia lentis in this foal, the first genetic explanation for this condition in the horse" (PMID:41136527).

**Veterinary relevance.** Rare; reported as sporadic cases or sire-line clusters (germline mosaic bulls) (PMID:22221020; PMID:15776436).

**Comparative pathology and conservation.** Bovine MFS "is closely related to its human's counterpart in its clinical signs and pathological lesions" (PMID:15776436). Fibrillin-like genes exist in C. elegans and zebrafish, and fibrillin-3 is degenerate in mice and rats (PMID:37972149).

**Transmission.** Not infectious; no zoonotic potential.

## 15. Model Organisms

| Model | Genetic lesion | Recapitulation | Limitations | Evidence |
|---|---|---|---|---|
| Mouse Fbn1 mgΔ | exons 19–24 replaced by neo; ~90% lower mutant transcript | homozygotes die ~3 weeks with aortic complications; heterozygotes normal | heterozygotes lack phenotype | PMID:9326947; PMID:39834548 |
| Mouse Fbn1 mgR (hypomorph) | underexpression | "underexpression of fibrillin-1 similarly leads to MFS-like manifestations", dissecting aneurysm | homozygous model of a dominant disease | PMID:10097121 |
| Mouse Fbn1 C1039G/+ | knock-in cbEGF cysteine missense | "impaired microfibrillar deposition, skeletal deformity, and progressive deterioration of aortic wall architecture"; MVP; lung septation defect | mild aneurysm, rarely dissects | PMID:15254584; PMID:15546004; PMID:16601194 |
| Mouse Fbn1 C1041G/+ | equivalent knock-in | aortic root aneurysm; scRNA-seq; ciprofloxacin studies | — | PMID:32698686; PMID:34586071 |
| Mouse mgΔloxPneo | mgΔ allele with floxed neo | "defective microfibrillar deposition, emphysema, deterioration of aortic wall and kyphosis"; strain-dependent severity | background effects | PMID:21152435; PMID:26927851 |
| Mouse GT-8, H1Δ | eGFP-tagged truncation; exon 7 deletion | GT-8 het: abnormal skin and dilated aorta; H1Δ: no aortopathy | review-level evidence only | PMID:39834548 |
| Mouse Tsk | intragenic Fbn1 duplication | skin tightness, emphysema, skeletal overgrowth, kyphosis, reduced BMD | models stiff-skin features | PMID:17705049 |
| Pig (Sus scrofa) | FBN1 +/Glu433AsnfsX98 (ZFN) | "scoliosis, pectus excavatum, delayed mineralization of the epiphysis and disrupted structure of elastic fibres of the aortic medial tissue" | haploinsufficiency hard to reproduce | PMID:27074716; PMID:35598970 |
| Rabbit | CRISPR C-terminal truncation | MFS features plus MPL features (lipodystrophy, dysglycemia) | models MPL more than classic MFS | PMID:29666143 |
| Zebrafish | fbn1+/- CRISPR frameshift or nonsense | decreased pigmentation, increased length, slender body, abnormal cardiac flow; variant pathogenicity testing | non-mammalian anatomy | PMID:34324266; PMID:40128660 |
| Human iPSC-SMC | patient-derived; CRISPR-corrected isogenic controls | "recapitulated the pathology seen in Marfan aortas" | in vitro, no haemodynamics | PMID:27893734 |
| Induced model | NO donors in wild-type mice | "NO-donors induce Marfan-like aortopathy in wild-type mice" | pharmacological | PMID:33976159 |

**Model types and characteristics.** Mammalian (mouse, pig, rabbit), vertebrate non-mammalian (zebrafish), cellular (iPSC-SMC, fibroblasts) and induced pharmacological models. Knock-out/hypomorph (mgΔ, mgR), knock-in (C1039G, C1041G), conditional (Tfam VSMC-specific deletion on a non-MFS background; SMC-specific Tgfbr2 deletion on C1039G/+) (PMID:33709773; PMID:28119285) and gene-edited large animals are available. A review concludes that "A number of mouse models have been created in an attempt to replicate the human phenotype, although all have limitations" (PMID:37972149), and Chen et al. note that knockout or dominant-negative mice "cannot recapitulate the genotype/phenotype relationship of Marfanoid-progeroid-lipodystrophy (MPL) syndrome" (PMID:29666143). Isogenic mice "do not address the effect of genetic background on the disease phenotype" (PMID:26927851). GT-8/+ mice show sex and pregnancy effects paralleling humans: "male MFS mice have more severe aortic disease than female mice and pregnancy adversely affects aortic disease" (PMID:28708846). Exercise models in Fbn1 mice: (PMID:28385916; PMID:28947563).

**Applications.** Mechanism dissection (TGF-β, ERK, NO, mitochondria), preclinical drug testing (losartan, CCB harm, fluoroquinolones, doxycycline, nicotinamide riboside), modifier mapping, variant pathogenicity testing (zebrafish) and human-relevant SMC biology (iPSC) (PMID:16601194; PMID:26506064; PMID:34586071; PMID:22550139; PMID:33709773; PMID:26927851; PMID:40128660; PMID:27893734). The translational gap is notable: losartan's dramatic mouse effect translated into only modest human benefit (PMID:16601194; PMID:36049495).

**Resources.** MGI, IMSR and MMRRC records were not retrieved for this report; model information comes from primary papers, OMIA and NCBI Gene.

## Open Questions

- **Which signalling events are primary in human aortopathy?** Mouse data support excess (and stage-dependent) TGF-β/ERK signalling, but young C1039G/+ mice develop aortopathy without detectable SMC TGF-β changes, and human aortic RNA-seq shows no TGF-β signature; NO–sGC–PRKG and mitochondrial pathways are newer contenders (PMID:21493862; PMID:28119285; PMID:35008861; PMID:33976159; PMID:33709773).
- **True prevalence and penetrance.** gnomAD predicts pathogenic FBN1 genotypes in 1 in 416 people, far above clinical prevalence of 2–10/100,000; how many carriers have mild or no disease is unknown (PMID:40102521; PMID:26631233).
- **Genotype-guided therapy.** Whether HI patients benefit more from ARBs is inconsistent across COMPARE, LOAT and paediatric data (PMID:25613431; PMID:30261963; PMID:35058154).
- **Type B and distal aortic disease.** Prediction and prevention of type B dissection after root replacement, which may occur at modest diameters (PMID:25614422; PMID:21147864; PMID:42017320).
- **Pregnancy thresholds.** US and European guidelines have differed (40 vs 45 mm), and type B dissection is unpredictable (PMID:30243228; PMID:34446158).
- **Exercise prescription.** No human outcome studies exist; guidelines now favour individualised moderate aerobic exercise, and mouse studies suggest benefit from moderate but not strenuous exercise (PMID:26729892; PMID:41152210; PMID:39210722; PMID:28385916).
- **Fluoroquinolone risk in humans** remains uncertain given contradictory mouse and human data (PMID:34586071; PMID:36823078).
- **Epigenetics, metabolomics and human single-cell atlases** remain thin: one histone-mark study of TAA SMCs, mouse miR-29b data, a methylation review and a small SMC single-cell study (PMID:20829218; PMID:22116819; PMID:40370619; PMID:40678173).
- **Role of inflammation and oxidative stress.** Human aortas show T-cell/macrophage infiltration and ROS, but anti-inflammatory drugs failed in mice while antioxidant allopurinol worked (PMID:22479353; PMID:25238161; PMID:36347404).
- **Sex effects.** Men have more aneurysm and surgery, but dissection prevalence is similar by sex in several cohorts (PMID:42475821; PMID:23444191; PMID:35543473).
- **Non-aortic morbidity** — cardiomyopathy, arrhythmia, sleep apnea, fatigue and pain — is common but has no disease-specific therapies (PMID:38816063; PMID:33885997; PMID:34795948; PMID:37208760).

## References

- OMIM:154700 McKusick VA (OMIM). #154700 Marfan syndrome; MFS. evidence: citations/omim-154700-marfan-syndrome.md
- ORPHA:558 Orphanet. Marfan syndrome (ORPHA:558) and Marfan syndrome type 1 (ORPHA:284963). evidence: citations/orphanet-558-marfan-syndrome.md
- MONDO:0007947 Mondo Disease Ontology (EBI OLS4). Marfan syndrome. evidence: citations/mondo-0007947-marfan-syndrome.md
- MeSH:D008382 NLM MeSH. Marfan Syndrome. evidence: citations/mesh-d008382-marfan-syndrome.md
- HGNC:3603 HGNC. FBN1 (fibrillin 1) gene record. evidence: citations/hgnc-3603-fbn1-gene-record.md
- UniProt:P35555 UniProt Consortium. FBN1_HUMAN Fibrillin-1. evidence: citations/uniprot-p35555-fbn1-domains-disease.md
- https://medlineplus.gov/genetics/condition/marfan-syndrome/ MedlinePlus Genetics. Marfan syndrome. evidence: citations/medlineplus-genetics-marfan-syndrome.md
- https://www.pfmjournal.org/upload/pdf/pfm-2024-00142.pdf Jang SY et al. 2024. Epidemiology of Marfan syndrome: a retrospective cohort study based on the Korean population. evidence: citations/jang-2024-epidemiology-marfan-korean-cohort.md
- https://onlinecjc.ca/article/S0828-282X(14)00112-3/fulltext Boodhwani M et al. 2014. Canadian Cardiovascular Society position statement on the management of thoracic aortic disease. evidence: citations/boodhwani-2014-ccs-thoracic-aortic-disease.md
- https://www.omia.org/OMIA000628/ Nicholas FW, Tammen I (OMIA). OMIA:000628 Marfan syndrome, FBN1-related. evidence: citations/omia-000628-overview.md
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&id=14118,2200,281154,478293,100055741,100330961,100350931,414836,83727 NCBI Gene. FBN1/Fbn1 orthologue records. evidence: citations/ncbi-gene-fbn1-orthologs.md
- PMID:20301510 Dietz H. 2001 (updated 2022). FBN1-Related Marfan Syndrome. GeneReviews. evidence: citations/dietz-2001-fbn1-related-marfan-syndrome.md
- PMID:34475413 Milewicz DM et al. 2021. Marfan syndrome. Nat Rev Dis Primers. evidence: citations/milewicz-2021-marfan-syndrome-review.md
- PMID:16325700 Judge DP, Dietz HC. 2005. Marfan's syndrome. Lancet. evidence: citations/judge-2005-marfans-syndrome-lancet.md
- PMID:1852208 Dietz HC et al. 1991. Marfan syndrome caused by a recurrent de novo missense mutation in the fibrillin gene. Nature. evidence: citations/dietz-1991-recurrent-de-novo-missense-fibrillin.md
- PMID:26631233 Groth KA et al. 2015. Prevalence, incidence, and age at diagnosis in Marfan Syndrome. evidence: citations/groth-2015-prevalence-incidence-age-marfan.md
- PMID:24388020 Chiu HH et al. 2014. Epidemiological profile of Marfan syndrome in a general population. evidence: citations/chiu-2014-epidemiological-profile-marfan-taiwan.md
- PMID:28244281 Jang SY et al. 2017. The Prevalence of Marfan Syndrome in Korea. evidence: citations/jang-2017-prevalence-marfan-korea.md
- PMID:40102521 Choi K et al. 2025. Population frequency of Marfan syndrome from predicted pathogenic FBN1 variants in gnomAD. evidence: citations/gnomad-marfan-population-frequency-fbn1-2025.md
- PMID:32461654 Karczewski KJ et al. 2020. The mutational constraint spectrum quantified from variation in 141,456 humans. evidence: citations/karczewski-2020-mutational-constraint-gnomad.md
- PMID:39741318 Drackley A et al. 2024. ClinGen FBN1 VCEP consensus recommendations. evidence: citations/clingen-fbn1-vcep-interpretation-classification.md
- PMID:31227806 Baudhuin LM et al. 2019. Variability in gene-based knowledge impacts variant classification: FBN1 missense variants in ClinVar. evidence: citations/variability-gene-knowledge-fbn1-missense-clinvar-2019.md
- PMID:25652356 Baudhuin LM et al. 2015. Decreased frequency of FBN1 missense variants in Ghent criteria-positive Marfan syndrome. evidence: citations/baudhuin-2015-ghent-positive-fbn1-variants.md
- PMID:25101912 Baudhuin LM et al. 2015. Increased frequency of FBN1 truncating and splicing variants in MFS patients with aortic events. evidence: citations/baudhuin-2015-truncating-splicing-aortic-events.md
- PMID:20372188 Arslan-Kirchner M et al. 2010. Clinical utility gene card for Marfan syndrome type 1 [FBN1]. evidence: citations/arslan-kirchner-2010-clinical-utility-gene-card-fbn1.md
- PMID:21936929 Furtado LV et al. 2011. Characterization of large genomic deletions in FBN1 using MLPA. evidence: citations/characterization-large-genomic-deletions-fbn1-mlpa-2011.md
- PMID:33910934 Fernández-Álvarez P et al. 2022. Parental somatic mosaicism of FBN1 pathogenic variants in Marfan syndrome. evidence: citations/parental-somatic-mosaicism-fbn1-2022.md
- PMID:10090884 Rantamäki T et al. 1999. Recurrence of Marfan syndrome as a result of parental germ-line mosaicism. evidence: citations/recurrence-marfan-parental-germline-mosaicism-1999.md
- PMID:30087447 Aubart M et al. 2018. Association of modifiers and other genetic factors explain Marfan syndrome clinical variability. evidence: citations/modifiers-genetic-factors-marfan-variability-2018.md
- PMID:35058154 Meester JAN et al. 2022. Molecular characterization of a large pediatric Marfan syndrome cohort. evidence: citations/meester-2022-genetic-variation-pediatric-marfan-cohort.md
- PMID:36543362 van Elsäcker E et al. 2022. Growth of the aortic root in children and young adults with Marfan syndrome. evidence: citations/van-elsacker-2022-aortic-root-growth-children.md
- PMID:41309212 Korukonda S et al. 2025. Genotype-aortic phenotype correlations in Marfan syndrome: meta-analysis. evidence: citations/korukonda-2025-genotype-aortic-phenotype-meta-analysis.md
- PMID:11175294 Tiecke F et al. 2001. Classic, atypically severe and neonatal Marfan syndrome: FBN1 exons 24-40. evidence: citations/tiecke-2001-classic-atypical-neonatal-fbn1-exons-24-40.md
- PMID:30219651 Sakai LY, Keene DR. 2019. Fibrillin protein pleiotropy: Acromelic dysplasias. evidence: citations/fibrillin-protein-pleiotropy-acromelic-dysplasias-2019.md
- PMID:25979247 Jensen SA et al. 2015. A microfibril assembly assay identifies different mechanisms of dominance. evidence: citations/microfibril-assembly-assay-dominance-sss-acromelic-2015.md
- PMID:26860060 Passarge E et al. 2016. Marfanoid-progeroid-lipodystrophy syndrome. evidence: citations/marfanoid-progeroid-lipodystrophy-fibrillinopathy-2016.md
- PMID:27437668 Sakai LY et al. 2016. FBN1: The disease-causing gene for Marfan syndrome and other genetic disorders. evidence: citations/sakai-2016-fbn1-disease-gene-review.md
- PMID:26787436 Franken R et al. 2016. Genotype impacts survival in Marfan syndrome. evidence: citations/franken-2016-genotype-impacts-survival.md
- PMID:33731877 Arnaud P et al. 2021. Genotype-phenotype correlations in 1500 Marfan syndrome patients. evidence: citations/arnaud-2021-genotype-phenotype-1500.md
- PMID:12598898 Neptune ER et al. 2003. Dysregulation of TGF-beta activation contributes to pathogenesis in Marfan syndrome. evidence: citations/neptune-2003-dysregulation-tgf-beta-activation.md
- PMID:16601194 Habashi JP et al. 2006. Losartan prevents aortic aneurysm in a mouse model of Marfan syndrome. evidence: citations/habashi-2006-losartan-aneurysm-marfan-mouse.md
- PMID:21493862 Holm TM et al. 2011. Noncanonical TGFβ signaling contributes to aortic aneurysm progression in MFS mice. evidence: citations/holm-2011-noncanonical-tgfb-signaling.md
- PMID:21493863 Habashi JP et al. 2011. Angiotensin II type 2 receptor signaling attenuates aortic aneurysm through ERK antagonism. evidence: citations/habashi-2011-at2-receptor-erk-antagonism.md
- PMID:25614286 Cook JR et al. 2015. Dimorphic effects of TGF-β signaling during aortic aneurysm progression. evidence: citations/cook-2015-dimorphic-tgfb-signaling.md
- PMID:28119285 Wei H et al. 2017. Aortopathy in a mouse model of MFS is not mediated by altered TGF-β signaling. evidence: citations/wei-2017-aortopathy-not-mediated-tgfb.md
- PMID:22550139 Xiong W et al. 2012. MMP-2 regulates Erk1/2 phosphorylation and aortic dilatation in MFS. evidence: citations/xiong-2012-mmp2-erk1-2-marfan.md
- PMID:33976159 de la Fuente-Alonso A et al. 2021. Aortic disease in MFS is caused by overactivation of sGC-PRKG signaling by NO. evidence: citations/de-la-fuente-alonso-2021-no-sgc-prkg.md
- PMID:33709773 Oller J et al. 2021. Extracellular tuning of mitochondrial respiration leads to aortic aneurysm. evidence: citations/oller-2021-extracellular-tuning-mitochondrial.md
- PMID:32698686 Pedroza AJ et al. 2020. Single-cell transcriptomic profiling of VSMC phenotype modulation in MFS. evidence: citations/pedroza-2020-single-cell-smc-modulation-mfs.md
- PMID:35008861 Verhagen JMA et al. 2021. Multi-omics profiling in Marfan syndrome. evidence: citations/verhagen-2021-multi-omics-mfs.md
- PMID:27893734 Granata A et al. 2017. An iPSC-derived vascular model of Marfan syndrome. evidence: citations/granata-2017-ipsc-vascular-model-marfan.md
- PMID:15254584 Judge DP et al. 2004. Haploinsufficiency in the pathogenesis of Marfan syndrome. evidence: citations/judge-2004-haploinsufficiency-marfan-pathogenesis.md
- PMID:15546004 Ng CM et al. 2004. TGF-beta-dependent pathogenesis of mitral valve prolapse in a mouse model of MFS. evidence: citations/ng-2004-tgf-beta-mitral-valve-prolapse-marfan-mouse.md
- PMID:9326947 Pereira L et al. 1997. Targetting of the gene encoding fibrillin-1 recapitulates the vascular aspect of MFS. evidence: citations/pereira-1997-targetting-fibrillin-1-mouse.md
- PMID:10097121 Pereira L et al. 1999. Pathogenetic sequence for aneurysm revealed in mice underexpressing fibrillin-1. evidence: citations/pereira-1999-pathogenetic-sequence-aneurysm-mice.md
- PMID:21152435 Lima BL et al. 2010. A new mouse model for Marfan syndrome (mgΔloxPneo). evidence: citations/lima-2010-new-mouse-model-mgdeltaloxpneo.md
- PMID:26927851 Fernandes GR et al. 2016. Loci modulating cardiovascular and skeletal phenotypes of MFS in mice. evidence: citations/fernandes-2016-loci-modulating-marfan-mice.md
- PMID:17705049 Barisic-Dujmovic T et al. 2007. Marfan-like skeletal phenotype in the tight skin (Tsk) mouse. evidence: citations/barisic-dujmovic-2007-marfan-like-tight-skin-mouse.md
- PMID:39834548 Jiang Y et al. 2024. Marfan syndrome: insights from animal models. evidence: citations/jiang-2024-marfan-insights-animal-models.md
- PMID:37972149 Summers KM. 2024. Genetic models of fibrillinopathies. evidence: citations/summers-2024-genetic-models-fibrillinopathies.md
- PMID:27074716 Umeyama K et al. 2016. Heterozygous fibrillin-1 mutant cloned pigs. evidence: citations/umeyama-2016-heterozygous-fibrillin-1-cloned-pigs.md
- PMID:35598970 Jack N et al. 2022. Genetically engineered animal models for MFS: pig models and haploinsufficiency. evidence: citations/jack-2022-genetically-engineered-marfan-pig-challenges.md
- PMID:29666143 Chen M et al. 2018. Truncated C-terminus of fibrillin-1 induces MPL syndrome in rabbit. evidence: citations/chen-2018-truncated-fibrillin-1-mpl-rabbit.md
- PMID:34324266 Yin X et al. 2021. CRISPR/Cas9 in zebrafish: a model for FBN1 genetic defects. evidence: citations/yin-2021-crispr-zebrafish-fbn1.md
- PMID:40128660 Huang S et al. 2025. Novel FBN1 variant validated in a zebrafish model. evidence: citations/huang-2025-zebrafish-novel-fbn1-variant.md
- PMID:22221020 Hirano T et al. 2012. Identification of an FBN1 mutation in bovine Marfan syndrome-like disease. evidence: citations/hirano-2012-fbn1-mutation-bovine-marfan-like.md
- PMID:15776436 OMIA curators (citing Singleton et al. 2005). OMIA:000628-9913 Marfan syndrome, FBN1-related in Bos taurus. evidence: citations/omia-000628-bovine-9913.md
- PMID:42815455 Lennertz HT et al. 2026. Marfan-like syndrome in a Golden Retriever puppy. evidence: citations/lennertz-2026-marfan-like-golden-retriever.md
- PMID:41136527 Esdaile E et al. 2025. A de novo FBN1 variant likely causes congenital bilateral ectopia lentis in a horse. evidence: citations/esdaile-2025-fbn1-ectopia-lentis-horse.md
- PMID:22133496 Jondeau G et al. 2012. Aortic event rate in the Marfan population. evidence: citations/jondeau-2012-aortic-event-rate.md
- PMID:32130918 Milleron O et al. 2020. Pathogenic FBN1 genetic variation and aortic dissection. evidence: citations/milleron-2020-fbn1-aortic-dissection.md
- PMID:25614422 den Hartog AW et al. 2015. The risk for type B aortic dissection in Marfan syndrome. evidence: citations/den-hartog-2015-type-b-dissection-risk.md
- PMID:28600386 Roman MJ et al. 2017. Associations of age and sex with Marfan phenotype: GenTAC. evidence: citations/roman-2017-age-sex-marfan-phenotype-gentac.md
- PMID:31376376 Shalhub S et al. 2020. Type B aortic dissection in young individuals with heritable thoracic aortic disease. evidence: citations/shalhub-2020-type-b-young-heritable.md
- PMID:30115424 Mah DY et al. 2018. Ventricular arrhythmias in children and young adults with MFS. evidence: citations/mah-2018-ventricular-arrhythmias-children.md
- PMID:24349050 Aydin A et al. 2013. Ventricular arrhythmia in adults with MFS caused by FBN1 mutations. evidence: citations/aydin-2013-ventricular-arrhythmia-adults.md
- PMID:34232254 Demolder A et al. 2021. Mitral annular disjunction and outcomes in MFS. evidence: citations/demolder-2021-mitral-annular-disjunction.md
- PMID:27550511 Groth KA et al. 2017. Aortic events in a nationwide Marfan syndrome cohort. evidence: citations/groth-2017-aortic-events-nationwide.md
- PMID:30149886 Groth KA et al. 2018. Causes of mortality in the Marfan syndrome. evidence: citations/groth-2018-causes-mortality-marfan.md
- PMID:11159287 van Karnebeek CD et al. 2001. Natural history of cardiovascular manifestations in MFS. evidence: citations/van-karnebeek-2001-natural-history-cardiovascular.md
- PMID:30652519 Veiga-Fernández A et al. 2020. Early-onset Marfan syndrome: case report and systematic review. evidence: citations/veiga-fernandez-2020-early-onset-marfan.md
- PMID:38816063 Weigand J et al. 2024. Evidence of cardiomyopathy associated with MFS in children. evidence: citations/weigand-2024-cardiomyopathy-marfan-children.md
- PMID:8487722 Hwa J et al. 1993. The natural history of aortic dilatation in Marfan syndrome. evidence: citations/hwa-1993-natural-history-aortic-dilatation.md
- PMID:42017320 Narula N et al. 2026. Outcomes of type B dissection in MFS: Cornell registry. evidence: citations/narula-2026-type-b-dissection-cornell.md
- PMID:21147864 Mimoun L et al. 2011. Dissection in Marfan syndrome: the importance of the descending aorta. evidence: citations/mimoun-2011-descending-aorta-dissection.md
- PMID:29948025 Hoskoppal A et al. 2018. Predictors of rapid aortic root dilation in MFS. evidence: citations/hoskoppal-2018-predictors-rapid-aortic-root-dilation.md
- PMID:33885997 Andersen NH et al. 2021. Non-aortic cardiovascular disease in Marfan syndrome. evidence: citations/andersen-2021-non-aortic-cardiovascular.md
- PMID:19293838 Rand-Hendriksen S et al. 2009. Prevalence data on all Ghent features in 87 adults. evidence: citations/rand-hendriksen-2009-prevalence-ghent-features.md
- PMID:20613543 Rand-Hendriksen S et al. 2010. Health-related quality of life in MFS: SF-36 in 84 adults. evidence: citations/rand-hendriksen-2010-sf36-quality-of-life.md
- PMID:33256748 Vanem TT et al. 2020. HRQoL in Marfan syndrome: a 10-year follow-up. evidence: citations/vanem-2020-hrqol-10-year-follow-up.md
- PMID:31825148 Vanem TT et al. 2020. Marfan syndrome: evolving organ manifestations, 10-year follow-up. evidence: citations/vanem-2020-evolving-organ-manifestations.md
- PMID:30393980 Vanem TT et al. 2018. Survival, causes of death, and cardiovascular events in MFS. evidence: citations/vanem-2018-survival-causes-death.md
- PMID:24813698 Velvin G et al. 2015. Psychosocial aspects of living with MFS: systematic review. evidence: citations/velvin-2015-psychosocial-systematic-review.md
- PMID:26607862 Velvin G et al. 2016. Chronic pain in persons with MFS: systematic review. evidence: citations/velvin-2016-chronic-pain-systematic-review.md
- PMID:37208760 Velvin G et al. 2023. Fatigue in syndromic heritable thoracic aortic disease. evidence: citations/velvin-2023-fatigue-syndromic-htad-review.md
- PMID:24719044 Bathen T et al. 2014. Fatigue in adults with Marfan syndrome. evidence: citations/bathen-2014-fatigue-adults-marfan.md
- PMID:27862906 Speed TJ et al. 2017. Pain, disability, and psychological burden in MFS. evidence: citations/speed-2017-pain-disability-psychological-burden.md
- PMID:33968637 Andonian C et al. 2021. Quality of life in 102 adults with MFS. evidence: citations/andonian-2021-quality-of-life-102-adults.md
- PMID:18448780 Fusar-Poli P et al. 2008. Determinants of quality of life in MFS. evidence: citations/fusar-poli-2008-determinants-quality-of-life.md
- PMID:36059006 van Andel MM et al. 2022. Fatigue, anxiety and depression in adult MFS. evidence: citations/van-andel-2022-fatigue-anxiety-depression-marfan.md
- PMID:40646614 Cavalier I et al. 2025. Determinants of fatigue in MFS using PROMs. evidence: citations/cavalier-2025-determinants-fatigue-proms.md
- PMID:28595698 Goldfinger JZ et al. 2017. Marfan syndrome and quality of life in the GenTAC registry. evidence: citations/goldfinger-2017-gentac-quality-of-life.md
- PMID:34825999 Pollock L et al. 2021. The musculoskeletal manifestations of Marfan syndrome. evidence: citations/pollock-2021-musculoskeletal-manifestations-review.md
- PMID:34795948 Tun MH et al. 2021. Respiratory manifestations of Marfan syndrome. evidence: citations/tun-2021-respiratory-manifestations-review.md
- PMID:6495247 Wood JR et al. 1984. Pulmonary disease in patients with Marfan syndrome. evidence: citations/wood-1984-pulmonary-disease-marfan.md
- PMID:40005367 Vakalopoulos DG et al. 2025. Refractive alterations in Marfan syndrome. evidence: citations/vakalopoulos-2025-refractive-alterations-review.md
- PMID:41496654 Cohen SA et al. 2026. Surgical approach to ocular complications of MFS. evidence: citations/cohen-2026-surgical-ocular-complications.md
- PMID:30998996 Böker T et al. 2019. Dural ectasia in MFS: 10-year follow-up. evidence: citations/boker-2019-dural-ectasia-10-year.md
- PMID:40075421 Böker T et al. 2025. Natural history of protrusio acetabuli in MFS. evidence: citations/boker-2025-protrusio-acetabuli-natural-history.md
- PMID:36449672 Rasul A et al. 2022. Ectopia lentis and outcomes after surgery in a Danish population. evidence: citations/rasul-2022-ectopia-lentis-danish-surgery.md
- PMID:20591885 Loeys BL et al. 2010. The revised Ghent nosology for the Marfan syndrome. evidence: citations/loeys-2010-revised-ghent-nosology.md
- PMID:8723076 De Paepe A et al. 1996. Revised diagnostic criteria for the Marfan syndrome. evidence: citations/de-paepe-1996-revised-diagnostic-criteria.md
- PMID:21564093 Faivre L et al. 2012. The new Ghent criteria for Marfan syndrome: what do they change? evidence: citations/faivre-2012-new-ghent-criteria.md
- PMID:21332468 Radonic T et al. 2011. Critical appraisal of the revised Ghent criteria. evidence: citations/radonic-2011-critical-appraisal-ghent.md
- PMID:26124674 von Kodolitsch Y et al. 2015. Perspectives on the revised Ghent criteria. evidence: citations/von-kodolitsch-2015-perspectives-revised-ghent.md
- PMID:27778219 Morris AA et al. 2017. Guidelines for cystathionine beta-synthase deficiency. evidence: citations/morris-2017-cbs-deficiency-guidelines.md
- PMID:24577266 MacCarrick G et al. 2014. Loeys-Dietz syndrome: a primer. evidence: citations/maccarrick-2014-loeys-dietz-primer.md
- PMID:39210722 Mazzolai L et al. 2024. 2024 ESC Guidelines for peripheral arterial and aortic diseases. evidence: citations/mazzolai-2024-esc-peripheral-arterial-aortic-diseases.md; citations/mazzolai-2024-esc-marfan-tables-60-64-fulltext.md
- PMID:36322642 Isselbacher EM et al. 2022. 2022 ACC/AHA Guideline for aortic disease. evidence: citations/isselbacher-2022-acc-aha-aortic-disease-guideline.md; citations/isselbacher-2022-acc-aha-aortic-disease-guideline-fulltext.md
- PMID:9239687 Harton GL et al. 1996. Preimplantation genetic testing for Marfan syndrome. evidence: citations/harton-1996-preimplantation-genetic-testing-marfan.md
- PMID:11810645 Loeys B et al. 2002. Strategies for prenatal and preimplantation genetic diagnosis in MFS. evidence: citations/loeys-2002-prenatal-preimplantation-diagnosis-mfs.md
- PMID:26903455 Child AH et al. 2016. Genetic testing in Marfan syndrome. evidence: citations/child-2016-genetic-testing-marfan.md
- PMID:5011789 Murdoch JL et al. 1972. Life expectancy and causes of death in the Marfan syndrome. evidence: citations/murdoch-1972-life-expectancy-causes.md
- PMID:7810492 Silverman DI et al. 1995. Life expectancy in the Marfan syndrome. evidence: citations/silverman-1995-life-expectancy-marfan.md
- PMID:7560600 Silverman DI et al. 1995. Family history of severe cardiovascular disease in MFS. evidence: citations/silverman-1995-family-history-cardiovascular.md
- PMID:9761390 Gray JR et al. 1998. Life expectancy in British Marfan syndrome populations. evidence: citations/gray-1998-life-expectancy-british.md
- PMID:42288721 Cheng YM et al. 2026. Prognostic factors in MFS referred to a cardiac surgery center. evidence: citations/cheng-2026-prognostic-factors-marfan.md
- PMID:39306029 Claus J et al. 2025. Late diagnosis of MFS is associated with unplanned aortic surgery and death. evidence: citations/claus-2025-late-diagnosis-unplanned-surgery.md
- PMID:8152445 Shores J et al. 1994. Progression of aortic dilatation and the benefit of long-term β-blockade. evidence: citations/shores-1994-progression-aortic-dilatation.md
- PMID:29110304 Koo HK et al. 2017. Beta-blockers for preventing aortic dissection in MFS (Cochrane). evidence: citations/koo-2017-beta-blockers-preventing-dissection.md
- PMID:25405392 Lacro RV et al. 2014. Atenolol versus losartan in children and young adults with MFS. evidence: citations/lacro-2014-atenolol-losartan-children.md
- PMID:23999449 Groenink M et al. 2013. Losartan reduces aortic dilatation rate in adults with MFS (COMPARE). evidence: citations/groenink-2013-losartan-reduces-aortic.md
- PMID:25613431 Franken R et al. 2015. Beneficial outcome of losartan therapy depends on type of FBN1 mutation. evidence: citations/franken-2015-beneficial-outcome-losartan.md
- PMID:27704402 den Hartog AW et al. 2016. Losartan and ventricular function by FBN1 mutation type. evidence: citations/den-hartog-2016-losartan-ventricular-function-fbn1.md
- PMID:25935877 Milleron O et al. 2015. Marfan Sartan trial. evidence: citations/milleron-2015-marfan-sartan-placebo.md
- PMID:26518245 Forteza A et al. 2016. Losartan vs atenolol for prevention of aortic dilation in MFS. evidence: citations/forteza-2016-efficacy-losartan-atenolol.md
- PMID:30261963 Teixido-Tura G et al. 2018. Losartan versus atenolol: long-term follow-up. evidence: citations/teixido-tura-2018-losartan-versus-atenolol.md
- PMID:32548624 van Andel MM et al. 2020. Long-term clinical outcomes of losartan (COMPARE follow-up). evidence: citations/van-andel-2020-long-term-losartan-compare.md
- PMID:31836196 Mullen M et al. 2019. Irbesartan in Marfan syndrome (AIMS). evidence: citations/mullen-2019-irbesartan-marfan-aims.md
- PMID:36049495 Pitcher A et al. 2022. ARBs and β blockers in MFS: individual patient data meta-analysis. evidence: citations/pitcher-2022-arb-beta-blocker-individual-patient.md
- PMID:31606871 Elbadawi A et al. 2019. Losartan for preventing aortic root dilatation: meta-analysis. evidence: citations/elbadawi-2019-losartan-meta-analysis.md
- PMID:28657492 Muiño-Mosquera L et al. 2017. Losartan as add-on therapy in MFS (Ghent trial). evidence: citations/muino-mosquera-2017-losartan-add-on-beta-blocker.md
- PMID:21239069 Möberg K et al. 2012. The Ghent Marfan Trial design. evidence: citations/moberg-2012-ghent-marfan-trial-losartan.md
- PMID:26506064 Doyle JJ et al. 2015. Deleterious gene-by-environment interaction imposed by calcium channel blockers. evidence: citations/doyle-2015-calcium-channel-blockers-marfan.md
- PMID:32586526 Van Driest SL et al. 2020. ADRB1 and CYP2C9 variants and response to atenolol and losartan. evidence: citations/van-driest-2020-adrb1-cyp2c9-atenolol-losartan.md
- PMID:33845931 Ayers R et al. 2021. Racial and ethnic differences in response to treatment for MFS. evidence: citations/ayers-2021-racial-ethnic-response-marfan.md
- PMID:33801742 Cale JM et al. 2021. Antisense oligonucleotide skipping of FBN1 exon 52. evidence: citations/cale-2021-antisense-exon52-fibrillin.md
- PMID:42752801 Egea G et al. 2026. Introducing allopurinol to the medical treatment of MFS. evidence: citations/egea-2026-allopurinol-marfan-medical-treatment.md
- PMID:39317438 van Andel MM et al. 2024. Effects of resveratrol on aortic growth in MFS. evidence: citations/van-andel-2024-resveratrol-aortic-growth.md
- NCT:NCT00429364 Pediatric Heart Network. Atenolol vs losartan trial record. evidence: citations/pediatric-heart-network-atenolol-losartan-clinicaltrials.md
- NCT:NCT00763893 AP-HP. Marfan Sartan trial record. evidence: citations/marfansartan-losartan-placebo-clinicaltrials.md
- NCT:NCT00782327 University Hospital Ghent. Losartan vs placebo on β-blockers trial record. evidence: citations/ghent-losartan-placebo-betablocker-clinicaltrials.md
- NCT:NCT01949233 University of Oxford. Irbesartan/doxycycline pilot trial record. evidence: citations/oxford-marfan-trial-irbesartan-doxycycline-clinicaltrials.md
- PMID:29893811 Burgstaller JM et al. 2018. Bentall versus David procedure in MFS: meta-analysis. evidence: citations/burgstaller-2018-bentall-vs-david-meta-analysis.md
- PMID:29270369 Flynn CD et al. 2017. Composite-valve graft vs valve-sparing root replacement in MFS: meta-analysis. evidence: citations/flynn-2017-composite-vs-valve-sparing-meta-analysis.md
- PMID:30169770 Martens A et al. 2019. David I procedure in Marfan disease: 20-year experience. evidence: citations/martens-2019-david-i-20-year-marfan.md
- PMID:37554715 Coselli JS et al. 2023. Valve-sparing and valve-replacing aortic root replacement in MFS. evidence: citations/coselli-2023-valve-sparing-vs-valve-replacing-root.md
- PMID:19379862 Cameron DE et al. 2009. Aortic root replacement in 372 Marfan patients. evidence: citations/cameron-2009-aortic-root-replacement-372-marfan.md
- PMID:41609261 Jacquemyn X et al. 2026. TEVAR for type B aortic dissections in MFS. evidence: citations/jacquemyn-2026-tevar-type-b-dissection-marfan.md
- PMID:27515814 Roman MJ et al. 2016. Aortic complications associated with pregnancy in MFS (GenTAC). evidence: citations/roman-2016-aortic-complications-pregnancy-nhlbi-registry.md
- PMID:34446158 Narula N et al. 2021. Pregnancy-related aortic complications in women with MFS. evidence: citations/narula-2021-pregnancy-aortic-complications-marfan.md
- PMID:16236373 Meijboom LJ et al. 2006. Obstetric complications in Marfan syndrome. evidence: citations/meijboom-2006-obstetric-complications-marfan.md
- PMID:30243228 Minsart AF et al. 2018. Obstetric and cardiac outcomes with aortic root ≤45 mm. evidence: citations/minsart-2018-obstetric-cardiac-outcomes-root-45mm.md
- PMID:27788933 Kuperstein R et al. 2017. Risk of aortic dissection in pregnant patients with MFS. evidence: citations/kuperstein-2017-risk-aortic-dissection-pregnant-marfan.md
- PMID:33052376 Braverman AC et al. 2021. Pregnancy-related acute aortic dissection (IRAD). evidence: citations/braverman-2021-pregnancy-related-acute-aortic-dissection.md
- PMID:26729892 Cheng A, Owens D. 2016. Marfan syndrome, inherited aortopathies and exercise. evidence: citations/cheng-2016-marfan-inherited-aortopathies-exercise.md
- PMID:41152210 Jayaratne N et al. 2026. Exercise recommendations for patients with MFS. evidence: citations/jayaratne-2026-exercise-recommendations-marfan.md
- PMID:36823078 Chen SW et al. 2023. Fluoroquinolones and risk of aortic aneurysm or dissection in MFS. evidence: citations/chen-2023-fluoroquinolones-aneurysm-dissection-marfan.md
- PMID:34586071 LeMaire SA et al. 2022. Ciprofloxacin accelerates aortic enlargement in Marfan mice. evidence: citations/lemaire-2022-ciprofloxacin-accelerates-aortic-enlargement-mice.md
- PMID:39053916 Rizk JG et al. 2024. Impact of the FDA fluoroquinolone warning on prescribing. evidence: citations/rizk-2024-fda-fluoroquinolone-warning-prescribing.md
- PMID:23023332 Doyle et al. 2012. Mutations in the TGF-β repressor SKI cause Shprintzen-Goldberg syndrome with aortic aneurysm. evidence: citations/doyle-2012-ski-shprintzen-goldberg-aortic-aneurysm.md
- PMID:36347404 Rodríguez-Rovira I et al. 2022. Allopurinol blocks aortic aneurysm in a mouse model of Marfan syndrome via reducing aortic oxidative stress. evidence: citations/rodriguez-rovira-2022-allopurinol-blocks-aortic-aneurysm.md
- PMID:19635970 Matt P et al. 2009. Circulating transforming growth factor-beta in Marfan syndrome. evidence: citations/matt-2009-circulating-tgf-beta-marfan.md
- PMID:7704457 Grahame et al. 1995. The Marfan syndrome: joint and skin manifestations are prevalent and correlated. evidence: citations/grahame-1995-marfan-joint-skin-manifestations.md
- PMID:40678173 Stanley KB et al. 2025. Combined genome and transcriptome analysis identifies molecular signatures of aortic disease in patients with Marfan syndrome. evidence: citations/stanley-2025-genome-transcriptome-marfan-aortic.md
- PMID:21135753 Stheneur et al. 2011. Prognosis factors in probands with an FBN1 mutation diagnosed before the age of 1 year. evidence: citations/stheneur-2011-prognosis-factors-fbn1-before-1-year.md
- PMID:27138491 Peng et al. 2016. A novel fibrillin-1 gene missense mutation associated with neonatal Marfan syndrome: a case report and review of the mutation spectrum evidence: citations/peng-2016-novel-fibrillin-1-neonatal-fulltext.md
- PMID:22479353 Radonic T et al. 2012. Inflammation aggravates disease severity in Marfan syndrome patients. evidence: citations/radonic-2012-inflammation-aggravates-disease-severity.md
- PMID:20829218 Gomez D et al. 2011. Epigenetic control of vascular smooth muscle cells in Marfan and non-Marfan thoracic aortic aneurysms. evidence: citations/gomez-2011-epigenetic-control-vsmc-marfan.md
- PMID:7782359 Sponseller et al. 1995. The thoracolumbar spine in Marfan syndrome. evidence: citations/sponseller-1995-thoracolumbar-spine-marfan.md
- PMID:28947563 Mas Stachurska et al. 2017. Cardiovascular Benefits of Moderate Exercise Training in Marfan Syndrome: Insights From an Animal Model evidence: citations/mas-stachurska-2017-moderate-exercise-marfan-mice-fulltext.md
- PMID:40878294 De Backer et al. 2025. 2025 ESC Guidelines for the management of cardiovascular disease and pregnancy. evidence: citations/de-backer-2025-esc-pregnancy-marfan-fulltext.md
- PMID:27059954 Wohl AP et al. 2016. Extracellular Regulation of Bone Morphogenetic Protein Activity by the Microfibril Component Fibrillin-1. evidence: citations/wohl-2016-bmp-activity-fibrillin-1.md
- PMID:10100050 Westling et al. 1998. Craniofacial manifestations in the Marfan syndrome: palatal dimensions and a comparative cephalometric analysis. evidence: citations/westling-1998-marfan-craniofacial-palatal-dimensions.md
- PMID:22116819 Merk DR et al. 2012. miR-29b participates in early aneurysm development in Marfan syndrome. evidence: citations/merk-2012-mir-29b-early-aneurysm.md
- PMID:19200529 Ahram et al. 2009. A homozygous mutation in ADAMTSL4 causes autosomal-recessive isolated ectopia lentis. evidence: citations/ahram-2009-adamtsl4-recessive-isolated-ectopia-lentis.md
- PMID:30260057 Sandvik et al. 2019. Ten-year reinvestigation of ocular manifestations in Marfan syndrome. evidence: citations/sandvik-2019-ten-year-ocular-reinvestigation-marfan.md
- PMID:21647416 Guo G et al. 2011. Induction of macrophage chemotaxis by aortic extracts from patients with Marfan syndrome is related to elastin binding protein. evidence: citations/guo-2011-macrophage-chemotaxis-aortic-extracts.md
- PMID:34228694 Taniguchi et al. 2021. Predictive Physical Manifestations for Progression of Scoliosis in Marfan Syndrome. evidence: citations/taniguchi-2021-predictive-physical-manifestations-scoliosis-marfan.md
- PMID:10706896 Pepin et al. 2000. Clinical and genetic features of Ehlers-Danlos syndrome type IV, the vascular type. evidence: citations/pepin-2000-ehlers-danlos-type-iv-vascular-type.md
- PMID:42475821 Dreher et al. 2026. Sex-Specific Cardiovascular Phenotypes in Marfan Syndrome. evidence: citations/dreher-2026-sex-specific-cardiovascular-phenotypes.md
- PMID:40370619 Zhang WZ et al. 2025. A Review on the Role of DNA Methylation in Aortic Disease Associated With Marfan Syndrome. evidence: citations/zhang-2025-review-dna-methylation-marfan-aortic.md
- PMID:24635535 Chandra et al. 2015. The revised ghent nosology; reclassifying isolated ectopia lentis. evidence: citations/chandra-2015-revised-ghent-reclassifying-isolated-ectopia-lentis.md
- PMID:35543473 Nucera et al. 2022. The impact of sex and gender on aortic events in patients with Marfan syndrome. evidence: citations/nucera-2022-sex-gender-aortic-events.md
- PMID:24853997 Drolsum et al. 2015. Ocular findings in 87 adults with Ghent-1 verified Marfan syndrome. evidence: citations/drolsum-2015-ocular-findings-87-adults.md
- PMID:17701892 Faivre et al. 2007. Effect of mutation type and location on clinical outcome in 1,013 probands with Marfan syndrome or related phenotypes and FBN1 mutations: an international study. evidence: citations/faivre-2007-mutation-type-location-1013.md
- PMID:19006240 Callewaert et al. 2009. Comprehensive clinical and molecular assessment of 32 probands with congenital contractural arachnodactyly: report of 14 novel mutations and review of the literature. evidence: citations/callewaert-2009-congenital-contractural-arachnodactyly-fbn2-32-probands.md
- PMID:25238161 Franken R et al. 2014. No beneficial effect of general and specific anti-inflammatory therapies on aortic dilatation in Marfan mice. evidence: citations/franken-2014-anti-inflammatory-therapies-marfan-mice.md
- PMID:18954631 He R et al. 2008. Characterization of the inflammatory cells in ascending thoracic aortic aneurysms in patients with Marfan syndrome, familial thoracic aortic aneurysms, and sporadic aneurysms. evidence: citations/he-2008-inflammatory-cells-ascending-aneurysms.md
- PMID:28306229 Malfait et al. 2017. The 2017 international classification of the Ehlers-Danlos syndromes. evidence: citations/malfait-2017-international-classification-ehlers-danlos.md
- PMID:32860412 Pelliccia et al. 2020. 2020 ESC Guidelines on sports cardiology and exercise in patients with cardiovascular disease. evidence: citations/pelliccia-2020-esc-sports-cardiology-aortopathy-fulltext.md
- PMID:29471108 Jiménez-Altayó F et al. 2018. Redox stress in Marfan syndrome: Dissecting the role of the NADPH oxidase NOX4 in aortic aneurysm. evidence: citations/jimenez-altayo-2018-nox4-redox-stress.md
- PMID:25759435 Regalado et al. 2015. Aortic Disease Presentation and Outcome Associated With ACTA2 Mutations. evidence: citations/regalado-2015-aortic-disease-acta2-mutations.md
- PMID:28385916 Gibson et al. 2017. Mild aerobic exercise blocks elastin fiber fragmentation and aortic dilatation in a mouse model of Marfan syndrome associated aortic aneurysm. evidence: citations/gibson-2017-mild-aerobic-exercise-marfan-mice.md
- PMID:30532108 Soto et al. 2018. [Pectus excavatum y carinatum en el síndrome de Marfan y síndromes similares: prevalencia e impacto clínico pulmonar y cardiovascular]. evidence: citations/soto-2018-pectus-excavatum-carinatum-marfan-mexico.md
- PMID:23444191 Holmes et al. 2013. GenTAC registry report: gender differences among individuals with genetically triggered thoracic aortic aneurysm and dissection. evidence: citations/holmes-2013-genTAC-gender-differences.md
- PMID:28708846 Renard et al. 2017. Sex, pregnancy and aortic disease in Marfan syndrome evidence: citations/renard-2017-sex-pregnancy-aortic-disease-fulltext.md
- PMID:21726424 Konradsen et al. 2012. Corneal curvature, pachymetry, and endothelial cell density in Marfan syndrome. evidence: citations/konradsen-2012-corneal-curvature-pachymetry-marfan.md
- PMID:19349279 Ono RN et al. 2009. Latent transforming growth factor beta-binding proteins and fibulins compete for fibrillin-1 and exhibit exquisite specificities in binding sites. evidence: citations/ono-2009-ltbp-fibulins-compete-fibrillin-1.md


## Artifacts

- [PLAN.md](Marfan_Syndrome-deep-research-claude_managed_artifacts/PLAN.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 211 |
| Resolved | 210 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 170 |
| Quoted claims found in source | 153 |
| Quoted claims **not** found in source | 17 |
| Quoted claims with nothing to check against | 15 |
| References weighed for topical relevance | 210 |
| On topic | 176 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:21152435` (6 mentions) - Identifier did not resolve to a record

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:20301510` *(abstract only)*: "is now known to be Loeys-Dietz syndrome"
  - closest text in source: "DIAGNOSIS/TESTING: The diagnosis of Marfan syndrome is established in a proband (by definition a person without a known family history of Marfan syndrome) who has an FBN1 pathogenic variant known to be associated with Marfan syndrome and EITHER of the following: Aortic root enlargement (z score ≥2.0)"
- `PMID:28708846` *(abstract only)*: "the female hormone 17β-estradiol stimulates aortic smooth muscle cells to produce fibrillin-1 in vitro"
  - closest text in source: "The effect of 17β-estradiol on fibrillin-1 protein synthesis was compared in vitro using human aortic smooth muscle cells and fibroblasts"
- `PMID:33885997` *(abstract only)*: "The risk of sudden cardiac death was increased [HR: 8.3 (CI 3.8-18.0)] but the etiology was unclear due to lack of autopsies"
  - closest text in source: "The risk of sudden cardiac death was increased [HR: 8.3 (CI 3.8-18.0)] but the etiology was unclear due to lack of autopsies"
- `PMID:34825999` *(abstract only)*: "Scoliosis affects more than 50% of MFS patients, as defined using the Cobb method that considers an angle of > 10° significant"
  - closest text in source: "The musculoskeletal manifestations of MFS, which to date have received less attention, can also have a significant impact on the quality of life and are likely to become more important as the age of the Marfan syndrome population increases (Hasan et al"
- `PMID:34825999` *(abstract only)*: "Chest wall deformity occurs in up to 70% of cases, usually becoming more evident during periods of accelerated growth in adolescence"
  - Text part not found as substring: 'Chest wall deformity occurs in up to 70% of cases, usually becoming more evident during periods of accelerated growth in adolescence' (note: only abstract available for PMID:34825999, full text may contain this excerpt)
- `PMID:34795948` *(abstract only)*: "The prevalence of sleep apnea in patients with MFS is much higher than in age- and sex-matched controls, with a range of 32% to 64% of patients being affected"
  - closest text in source: "OBJECTIVE: The prevalence of Marfan syndrome (MFS) is estimated to be 1 in 10,000 to 15,000 individuals, but the phenotype of MFS may not be apparent and hence its diagnosis may not be considered by clinicians"
- `PMID:34825999` *(abstract only)*: "the clinical significance of this change has not been fully elucidated"
  - Text part not found as substring: 'the clinical significance of this change has not been fully elucidated' (note: only abstract available for PMID:34825999, full text may contain this excerpt)
- `PMID:27138491` *(abstract only)*: "a total of 1,318 different FBN1 mutations for MFS have been included to date, of which only 59 (4.8 %) including 37 missense mutations (2.8 %) are associated with nMFS"
  - closest text in source: "As the only causal FBN1 mutation identified in the patient, the missense mutation c.3331 T > C (p.Cys1111Arg) was associated with the severe phenotype of MFS"
- `PMID:27138491` *(abstract only)*: "92.3 % (60/65) of nMFS mutations were de novo"
  - closest text in source: "Our review of the prominent characteristics of nMFS mutations relative to classic or incomplete MFS-related mutations will be helpful for the recognition of novel nMFS-associated variants."
- `PMID:26631233` *(abstract only)*: "without any regard to diagnostic criteria or clinical presentation"
  - closest text in source: "So far, only a few studies based on older diagnostic criteria have reported a wide range of prevalence and incidence"
- `PMID:20301510` *(abstract only)*: "Although intrafamilial clinical variability can be extensive, FBN1-related Marfan syndrome shows high clinical penetrance"
  - closest text in source: "CLINICAL CHARACTERISTICS: FBN1-related Marfan syndrome (Marfan syndrome), a systemic disorder of connective tissue with a high degree of clinical variability, comprises a broad phenotypic continuum ranging from mild (features of Marfan syndrome in one or a few systems) to severe and rapidly progressive neonatal multiorgan disease"
- `PMID:34795948` *(abstract only)*: "with no predilection for either sex or ethnicity"
  - Text part not found as substring: 'with no predilection for either sex or ethnicity' (note: only abstract available for PMID:34795948, full text may contain this excerpt)
- `PMID:28244281` *(abstract only)*: "Males also showed slightly higher prevalence of MFS than females"
  - closest text in source: "And the overall age-standardized prevalence of MFS increased between 2006 and 2013 especially in 15-19 years-old males and 10-14 years-old females."
- `PMID:15776436` *(abstract only)*: "disorganized elastin and narrowed elastic lamina separated by widened spaces"
  - Text part not found as substring: 'disorganized elastin and narrowed elastic lamina separated by widened spaces' (note: only abstract available for PMID:15776436, full text may contain this excerpt)
- `PMID:15776436` *(abstract only)*: "3598G>A transition in exon 29, resulting in a likely substitution of a glutamic acid by lysine at position 1200"
  - closest text in source: "In this study, Fbn1 cDNA from affected animals was sequenced and a heterozygous c.3598G > A transition was detected in exon 29, which predicted the substitution of an evolutionarily conserved glutamic acid by lysine at position 1200 (p.E1200K)"
- `PMID:15776436` *(abstract only)*: "is closely related to its human's counterpart in its clinical signs and pathological lesions"
  - closest text in source: "Several calves, all sired by a phenotypically normal bull, were found to exhibit the major clinical and pathological characteristics of human MFS (aortic dissection, joint laxity, lens dislocation), and were recognized as potential models of the human disease"
- `PMID:28708846` *(abstract only)*: "male MFS mice have more severe aortic disease than female mice and pregnancy adversely affects aortic disease"
  - closest text in source: "CONCLUSIONS: Pregnancy-related changes influence aortic disease severity in otherwise protected female MFS mice and patients"

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMID:21152435`: "a strong negative correlation between overall levels of Fbn1 expression and the severity of the phenotypes, corroborating the suggested protective role of normal fibrillin-1"
  - Reference did not resolve, so the quote could not be checked
- `PMID:21152435`: "is earlier in the 129/Sv than in C57BL/6 background, indicating the existence of genetic modifiers of MFS between these two mouse strains"
  - Reference did not resolve, so the quote could not be checked
- `PMID:20372188`: "56% missense mutations; 17% frameshift mutations; 14% nonsense mutations; 11% splice mutations; 2% in-frame deletions"
  - Reference resolved but exposes no abstract or full text to search
- `PMID:21152435`: "involvement of epigenetic factors in disease severity"
  - Reference did not resolve, so the quote could not be checked
- `PMID:39210722`: "Regular moderate aerobic exercise with a level of intensity informed by aortic diameter is recommended in most patients with MFS."
  - Reference resolved but exposes no abstract or full text to search
- `PMID:32860412`: "Participation in competitive or leisure-time sports activities (except power sports) should be considered in low-risk individuals (Table 14)."
  - Reference resolved but exposes no abstract or full text to search
- `PMID:39210722`: "Both genetic testing and imaging—mainly through transthoracic echocardiography, cardiovascular magnetic resonance, or cardiovascular computed tomography if the aortic root/ascending aorta is not well visualized—are essential for diagnosing hereditary thoracic aortic disease in patients and family members"
  - Reference resolved but exposes no abstract or full text to search
- `PMID:39210722`: "at least every 3 years"
  - Reference resolved but exposes no abstract or full text to search
- `PMID:20372188`: "a search for FBN1 genomic rearrangements by MLPA or related techniques could be proposed in clinically convincing cases"
  - Reference resolved but exposes no abstract or full text to search
- `PMID:5011789`: "Cardiac problems led to 52 of the 56 deaths of known cause, with aortic dilatation and its complications accounting for 80 per cent of these"
  - Reference resolved but exposes no abstract or full text to search
- `PMID:39210722`: "Open surgery is preferred over endovascular procedures in patients with MFS."
  - Reference resolved but exposes no abstract or full text to search
- `PMID:39210722`: "ARBs are not recommended during pregnancy."
  - Reference resolved but exposes no abstract or full text to search
- `PMID:40878294`: "In women with an aorta ≥45 mm, caesarean section should be considered."
  - Reference resolved but exposes no abstract or full text to search
- `PMID:40878294`: "Aortic event rates can reach up to 10%."
  - Reference resolved but exposes no abstract or full text to search
- `PMID:20372188`: "Practical use of prenatal diagnosis remains difficult because of the extremely broad variability of clinical expression"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 176 |
| Resolved | 162 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Not in the configured ontologies | 10 |
| Terms whose name was checked | 141 |
| Terms named correctly | 140 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0007947` (6 mentions) - the report calls it "Marfan syndrome", "MFS, MFS1, Marfan syndrome type 1, Marfan syndrome, Marfan syndrome, type 1, Marfan's syndrome"; MONDO calls it **Marfan syndrome**, and lists "Marfan syndrome type 1" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0007947` - called "Marfan syndrome", "MFS, MFS1, Marfan syndrome type 1, Marfan syndrome, Marfan syndrome, type 1, Marfan's syndrome"
- `OMIM:154700` - called "HPO 31/58", "OMIM ocular findings", "HPO 38/53 for disproportionate tall stature", "HPO 124/197", "HPO 11/53", "HPO 27/53", "HPO 29/199", "HPO 36/53, 25/63, 19/53, 31/53, –, 34/53"
- `UniProt:P35555` - called "is almost always bilateral", "Asprosin"

### Terms from ontologies the report was not asked to use

The report was asked for terms from a fixed set of ontologies, and these come from others, so they were not looked up. Nothing here is evidence of fabrication; it does mean the report reached outside the ontologies it was given:

- `OMIM:154700` (23 mentions), reported as "HPO 31/58", "OMIM ocular findings", "HPO 38/53 for disproportionate tall stature", "HPO 124/197", "HPO 11/53", "HPO 27/53", "HPO 29/199", "HPO 36/53, 25/63, 19/53, 31/53, –, 34/53"
- `ORPHA:558` (8 mentions)
- `ORPHA:284963` (2 mentions)
- `MeSH:D008382` (2 mentions), reported as "Marfan Syndrome"
- `UniProt:P35555` (7 mentions), reported as "is almost always bilateral", "Asprosin"
- `NCT:NCT00429364` (3 mentions), reported as "atenolol vs losartan, completed"
- `NCT:NCT00763893` (3 mentions), reported as "Marfan Sartan, terminated"
- `NCT:NCT00782327` (3 mentions), reported as "Ghent losartan add-on, completed"
- `NCT:NCT01949233` (3 mentions), reported as "irbesartan/doxycycline pilot, status unknown"
- `OMIA:000628` (3 mentions)

162 of 176 terms resolved to a current term; the rest could not be looked up either way.
