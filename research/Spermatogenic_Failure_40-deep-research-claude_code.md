---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-16T13:11:56.261948'
end_time: '2026-10-16T13:14:20.220797'
duration_seconds: 143.96
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spermatogenic Failure 40
  mondo_id: MONDO:0032859
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
  total_cost_usd: 0.8348876999999999
  session_id: e0e00ff6-67e7-5e60-9592-3e4cb1004f09
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 11
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 9
  on_topic: 7
  validator_version: 0.3.0
term_validation:
  total_terms: 8
  verified: 8
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 1
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0032859
    reported_labels:
    - MONDO
    ontology_label: spermatogenic failure 40
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spermatogenic Failure 40
- **MONDO ID:** MONDO:0032859 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spermatogenic Failure 40** covering all of the
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

I've confirmed the gene (CFAP65) and found the key papers. I'm now pulling their abstracts so I can quote them exactly.

# Research Report: Spermatogenic Failure 40 (SPGF40)

**Scope and verification.** I searched for sources and read PubMed-derived summaries of three primary papers, one 2026 case report, and database aggregators.
- I did not retrieve full verbatim abstracts. The only quotes below are short ones that the retrieval tools returned.
- Before using any snippet as evidence, re-check it with `just fetch-reference PMID:<id>` and `just count-verified-snippets`.
- OMIM, Orphanet, GeneReviews, ClinGen, gnomAD, MGI and OMIA were not directly accessed. Statements attributed to them come from secondary summaries or are marked "not verified".
- Every ontology identifier in this report is suggested from memory and unverified, so each must be looked up before binding. The only CURIEs confirmed by the searches are MONDO:0032859 and OMIM 618664.
- The Springer 2025 *Cell Mol Life Sci* paper on Cfap65 knockout mice was reachable only through a search snippet, because the full page redirected to a login.

## 1. Disease Information

**Overview.** SPGF40 is an autosomal recessive male infertility disorder caused by biallelic variants in *CFAP65* (2q35). It is a sperm-specific flagellar disorder, classically "multiple morphological abnormalities of the sperm flagella" (MMAF). Sperm tails are absent, short, bent, coiled or of irregular caliber, so sperm motility is severely reduced or absent. Some patients also have sperm-head defects, including acrosomal hypoplasia or aplasia. Sources: [MalaCards](https://malacards.org/card/spermatogenic_failure_40) and [MedGen mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/medgen/C5231451/index.html).

| Item | Value | Source |
|---|---|---|
| MONDO | MONDO:0032859 | Search result; consistent with the template |
| OMIM | #618664 (phenotype); OMIM directs readers to SPGF1 (258150) for locus heterogeneity | Secondary summaries |
| UMLS / MedGen | C5231451 | MedGen mirror |
| Gene | *CFAP65* (cilia and flagella associated protein 65), 2q35 | Multiple |
| Orphanet, ICD-10/11, MeSH | Not verified | — |

- **Synonyms.** SPGF40; spermatogenic failure 40; CFAP65-related MMAF or asthenoteratozoospermia (informal).
- **Data type.** The knowledge is aggregated from case series and families, not from EHR data.
- **Gene-disease validity.** One aggregator lists "Limited" with AR inheritance. I did not confirm whether this is ClinGen, GenCC or another source, so do not record it as a ClinGen tier without checking the `CGGV:` record. Evidence has grown since the original 2019 reports, so a re-curated tier may differ.
- **Related disorders.** Other MMAF genes (*CFAP43*, *CFAP44*, *CFAP61*, *CFAP69*, *DNAH1*, *ARMC2*, *CFAP58*, *TTC29*) are separate OMIM spermatogenic failure entries ([Tang 2017, PMID:28552195](https://pubmed.ncbi.nlm.nih.gov/28552195/); [Coutton 2019, PMID:30686508](https://pubmed.ncbi.nlm.nih.gov/30686508/)).

## 2. Etiology

- **Causal factor.** Biallelic loss-of-function variants in *CFAP65* are the only established cause.
- **Genetic risk and modifiers.** None are described.
- **Environmental risk, protective factors and gene-environment interactions.** No evidence found; the relevant cohort papers did not report any.
- **Heterogeneity.** In the Chinese cohort reported by Li et al., biallelic CFAP-gene variants explained 15 of 80 MMAF cases (19%). Of these, 4 were in *CFAP65*, 7 in *CFAP43*, 2 in *CFAP44* and 2 in *CFAP69*. This figure came from a search snippet and should be checked against the source.

## 3. Phenotypes

All phenotypes are male-specific unless stated.

| Phenotype | Suggested HPO (verify) | Frequency and notes |
|---|---|---|
| Male infertility | HP:0003251 | All reported probands |
| Asthenozoospermia / absent motility | HP:0012206 | Very frequent; severely reduced or complete immotility. Wang et al. report "we are the first to report that CFAP65 mutations may cause spermatozoa to be completely immotile" (PMID:31413122) |
| Teratozoospermia, MMAF | HP:0012864 | Absent, short, bent, coiled flagella in >97% of sperm in the 2026 Pakistani family (PMID:42477516) |
| Abnormal sperm head, acrosomal hypoplasia | Search HPO ("Abnormal acrosome morphology") | Variable; reported in some patients (PMID:31413122), absent in others |
| Normal semen volume | — | Reported in the Pakistani family |
| Normal FSH, testosterone, karyotype | — | 46,XY, no Y microdeletion, FSH 9.4 and 5.83 mIU/mL in the two Pakistani brothers |

**Respiratory features are inconsistent across reports** (summarized in Table 2 of the 2026 paper, PMC13383139):
- Several compound heterozygotes had chronic cough, sinusitis or pneumonia (for example c.5341G>T, p.E1781X).
- One patient with c.5341G>T plus c.1775_1776del had PCD-like features, nasosinusitis and tympanitis.
- p.W892X and the 2026 frameshift were isolated MMAF with no PCD symptoms.
- Whether the respiratory findings are caused by *CFAP65* or are incidental is unresolved.

**Characteristics.**
- Onset is at reproductive age, when infertility is detected.
- The condition is stable, with no progression reported.
- No quality-of-life data were found.

## 4. Genetic/Molecular Information

- **Gene.** *CFAP65*, NM_194302.3, 35 exons, encoding a 1,925-amino-acid protein with an ASH domain, an MSP domain, a transmembrane helix (aa 187–209) and a coiled-coil region (PMC13383139). The HGNC ID was not retrieved; look it up, and use lowercase `hgnc:` in this repository.
- **Reported variants.** The list below is from Table 2 of the 2026 paper, so check each against its original paper.
  - c.5341G>T (p.E1781X)
  - c.2284C>T (p.R762X) with c.1751delC (p.P584fs)
  - c.3021C>A (p.N1007K) with c.5714_5721del (p.L1905fs)
  - c.1775_1776del (p.P527Rfs*74)
  - c.2675G>A (p.W892X)
  - c.582_587delinsCG (p.Q194Hfs*4); homozygous; first cousins; absent from gnomAD and 1000 Genomes; "likely pathogenic" by the authors' tools.
- **Types.** Predominantly nonsense, frameshift and splice variants, with a few missense (p.N1007K). The mechanism is presumed loss of function.
- **Somatic vs germline.** Germline.
- **Modifier genes, epigenetics and chromosomal abnormalities.** None reported.
- **Allele frequency.** Not retrieved apart from the absence of the 2026 variant from gnomAD.

**Key primary papers (all human unless noted):**
1. Wang W et al. 2019, *J Med Genet*, [PMID:31413122](https://pubmed.ncbi.nlm.nih.gov/31413122/). Whole-exome sequencing of 47 men with severe asthenozoospermia found CFAP65 variants in three. EM and immunostaining showed acrosome hypoplasia, mitochondrial sheath disruption and missing central pairs.
2. Li W et al. 2020, *J Med Genet*, [PMID:31501240](https://pubmed.ncbi.nlm.nih.gov/31501240/). Of 88 MMAF men, six families carried biallelic CFAP65 variants. A *Cfap65* frameshift mouse reproduced MMAF.
3. Zhang X et al. 2019, *Clin Genet*, [PMID:31571197](https://pubmed.ncbi.nlm.nih.gov/31571197/). A homozygous nonsense variant in one MMAF patient.
4. 2026, *Basic Clin Androl*, [PMID:42477516](https://pubmed.ncbi.nlm.nih.gov/42477516/). A Pakistani consanguineous family with the p.Q194Hfs*4 variant.

## 5. Environmental Information

No environmental, lifestyle or infectious contributors were identified.

## 6. Mechanism / Pathophysiology

**Causal chain** (steps 1 and 2 are demonstrated in patients and mouse; steps 3 to 5 are partly inferred):
1. Biallelic loss-of-function variants in *CFAP65* lead to loss of functional CFAP65 protein.
2. Loss of CFAP65 leads to axonemal defects. The mouse model shows loss of the C2a projection of the central apparatus (per the 2025 *Cell Mol Life Sci* abstract and the 2026 paper's citation of it); in patients, EM shows missing central pair or doublet microtubules and a disorganized fibrous sheath or outer dense fibers.
3. Axonemal disorganization results in short, absent, bent and coiled flagella (MMAF), which leads to severely impaired or absent sperm motility. This step is inferred rather than shown directly.
4. In a subset of patients, defective acrosome biogenesis causes head abnormalities. The knockout-mouse abstract also mentions manchette defects. The mechanism is not established, and CFAP65 localization (acrosome, midpiece or whole flagellum) is reported inconsistently across studies.
5. Sperm that cannot swim cannot reach or fertilize the oocyte, which results in male infertility.

**Branch: motile cilia.** The mouse data show hydrocephalus (ependymal cilia) but no significant respiratory cilia impairment. The human respiratory findings are inconsistent, so involvement of other motile cilia is unresolved.

**Suggested terms (verify before binding):**
- GO: sperm flagellum assembly, axoneme assembly, acrosome assembly, cilium movement (GO:0003341 or similar).
- CL: spermatid (CL:0000018), sperm (CL:0000019).
- GO CC: sperm flagellum, axoneme, motile cilium.

**Molecular profiling, single-cell, spatial and multi-omics data.** None found. Expression is reported in the 2025 paper only in the context of localization, so I cannot cite it.

## 7. Anatomical Structures Affected

- **Organs.** Testis (spermatogenesis, spermiogenesis); sperm.
- **Cells.** Elongating spermatids and spermatozoa.
- **Subcellular.** Sperm flagellum axoneme (central pair, C2a projection, doublet microtubules), fibrous sheath, outer dense fibers, mitochondrial sheath, acrosome.
- **Lateralization.** Bilateral; this is a systemic germ-cell defect.
- **Possible secondary involvement.** Respiratory epithelium and ependyma, which are unproven in humans.

## 8. Temporal Development

Onset is at puberty or adulthood and is usually detected through a fertility evaluation. The course is lifelong and non-progressive. No remission is reported. No critical periods are described.

## 9. Inheritance and Population

- **Inheritance.** Autosomal recessive, with homozygous and compound heterozygous cases.
- **Consanguinity.** Present in the Pakistani family and in other homozygous cases.
- **Sex.** Affects males; female carriers are unaffected.
- **Prevalence, incidence, carrier frequency, founder effects and geography.** Not retrieved. Cases are reported from Chinese, Pakistani and North African cohorts, but this is not a systematic distribution. MMAF overall is rare.
- **Penetrance, anticipation and germline mosaicism.** Not reported.

## 10. Diagnostics

- **Semen analysis.** Asthenoteratozoospermia with MMAF morphology; sperm concentration can be normal.
- **EM of sperm.** Axonemal disorganization, missing central pair or doublets, and fibrous sheath disorganization.
- **Genetic testing.** Whole-exome sequencing or an MMAF/male-infertility gene panel including *CFAP65*; confirm with Sanger sequencing and segregation.
- **Exclusions.** Karyotype (46,XY) and Y microdeletion testing; assess for PCD symptoms.
- **Differential diagnosis.** Other MMAF genes (*DNAH1*, *CFAP43*, *CFAP44*, *CFAP69*, *CFAP61*, *ARMC2*) and PCD.
- **Screening.** No population screening exists. Cascade testing of relatives is reasonable in consanguineous families.
- **LOINC.** None retrieved.

## 11. Outcome/Prognosis

No survival effect is reported. The main outcome is infertility. No quality-of-life, complication or prognostic-factor data were found apart from the unresolved respiratory question.

## 12. Treatment

No curative or disease-specific therapy exists. In the sources I read, the 2026 paper reports no ICSI outcomes for *CFAP65* carriers.
- **Assisted reproduction.** ICSI is the usual approach for MMAF. In a CFAP43/CFAP44 context, ICSI outcomes were discussed (ref. 4 in PMC13383139), but I could not verify success rates for CFAP65, so none are stated here.
- **Gene therapy and others.** None.
- **Counseling.** Genetic counseling is appropriate.
- **Suggested NCIT terms (verify).** Assisted reproductive technology and genetic counseling (the CLAUDE.md list gives `NCIT:C15240` for Genetic Counseling).
- **Clinical trials.** None identified.

## 13. Prevention

- **Primary and secondary prevention.** None.
- **Genetic counseling and reproductive options.** These include carrier testing of partners in consanguineous families and preimplantation genetic testing where applicable.
- **Lifestyle measures.** None are evidence-based for this condition.

## 14. Other Species / Natural Disease

- **Natural disease.** I found no OMIA entry. This was not checked directly.
- **Comparative biology.** The 2026 paper's discussion says chicken *CFAP65* is related to sperm motility (also noted in the Zhang 2019 summary). This is unverified.
- **Zoonotic aspects.** Not applicable.

## 15. Model Organisms

- **Mouse.** Two sources describe a *Cfap65* knockout or frameshift mouse:
  - Li et al. 2020 (PMID:31501240) reported a frameshift mutant that reproduced MMAF.
  - The 2025 *Cell Mol Life Sci* paper ([DOI 10.1007/s00018-025-05583-2](https://link.springer.com/article/10.1007/s00018-025-05583-2)) reports C2a projection loss, severe MMAF and hydrocephalus. It also describes acrosome malformation, abnormal head shape, manchette defects and disorganized axonemes.
- **Fidelity.** The mouse reproduces MMAF and, to a variable extent, head defects. It additionally shows hydrocephalus and no clear respiratory phenotype, which differs from the mixed human respiratory findings. This difference justifies a `HUMAN_MODEL_MISMATCH` discussion in the KB if the entry is curated.
- **Database resources.** MGI, IMPC and the Alliance of Genome Resources were not checked.

## Gaps for curators

1. Fetch and quote the four primary papers (PMIDs 31413122, 31501240, 31571197, 42477516) from `references_cache/`.
2. Look up the current ClinGen/GenCC record for *CFAP65* / SPGF40 and copy the tier. The "Limited" tier I found may be out of date.
3. Resolve every suggested HPO, GO, CL and NCIT term by lookup. None is verified.
4. Find the PMID for the 2025 mouse paper in PubMed.
5. Check GeneReviews and Orphanet for an MMAF chapter or entry, and run `just check-genereviews`.

## Sources

- [MalaCards: Spermatogenic Failure 40](https://malacards.org/card/spermatogenic_failure_40)
- [MedGen C5231451 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/medgen/C5231451/index.html)
- [PMC13383139: novel homozygous CFAP65 frameshift, Pakistani family (2026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13383139/)
- [PMID:31413122, Wang 2019](https://pubmed.ncbi.nlm.nih.gov/31413122/)
- [PMID:31501240, Li 2020](https://pubmed.ncbi.nlm.nih.gov/31501240/)
- [PMID:31571197, Zhang 2019](https://pubmed.ncbi.nlm.nih.gov/31571197/)
- [PMID:28552195, Tang 2017](https://pubmed.ncbi.nlm.nih.gov/28552195/)
- [PMID:30686508, Coutton 2019](https://pubmed.ncbi.nlm.nih.gov/30686508/)
- [Springer CMLS 2025, CFAP65 and the C2a projection](https://link.springer.com/article/10.1007/s00018-025-05583-2)
- [Diverse monogenic subforms of human spermatogenic failure (PMC9792524)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9792524/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 9 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 5 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032859` (2 mentions) - the report calls it "MONDO"; MONDO calls it **spermatogenic failure 40**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0012206` (1 mention) - the report calls it "Asthenozoospermia / absent motility"; HP calls it **Abnormal sperm motility**
- `HP:0012864` (1 mention) - the report calls it "Teratozoospermia, MMAF"; HP calls it **Abnormal sperm morphology**, and lists "Teratozoospermia" among its other names
- `CL:0000018` (1 mention) - the report calls it "CL: spermatid"; CL calls it **spermatid**