---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-10T17:41:33.841990'
end_time: '2026-09-10T17:48:15.023588'
duration_seconds: 401.18
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Factor XIII A Subunit Deficiency
  mondo_id: MONDO:0013187
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
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 20
  num_turns: 30
  total_cost_usd: 1.8373768
  session_id: 0ecd1216-33cc-58da-968d-9ba73b5b4eb1
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 31
reference_validation:
  total_references: 23
  verified: 23
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:11816711
  relevance_assessed: 23
  on_topic: 14
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 33
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 7
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0013187
    reported_labels:
    - MONDO ID discrepancy** between the brief
    ontology_label: factor XIII, A subunit, deficiency of
  labels_variant: 1
  unresolvable_prefixes:
  - MGI
  - RGD
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Factor XIII A Subunit Deficiency
- **MONDO ID:** MONDO:0013187 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Factor XIII A Subunit Deficiency** covering all of the
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

I'll research Factor XIII A Subunit Deficiency comprehensively across the requested domains. Let me start by loading search tools and querying key databases.

# Factor XIII A Subunit Deficiency: Comprehensive Research Report

**Scope note on identifiers:** The research brief names MONDO:0013187, but searches return **MONDO:0018029** for "factor XIII deficiency" (general term) in cross-reference tables (MalaCards, Wikidata). I could not independently confirm MONDO:0013187 resolves to this disease in the sources retrieved. **This is a lead requiring verification against the MONDO ontology browser directly before binding** — do not treat either ID as confirmed without that check.

---

## 1. Disease Information

**Overview:** Congenital Factor XIII (FXIII) deficiency is a rare autosomal recessive bleeding disorder caused by biallelic loss-of-function variants in *F13A1* (encoding the catalytic A subunit) or, less commonly, *F13B* (encoding the carrier B subunit). FXIII is the "last enzyme" of the coagulation cascade — a transglutaminase that cross-links fibrin after clot formation rather than participating in clot initiation. Deficiency therefore produces a paradoxical presentation: **normal routine coagulation screening (PT, aPTT, thrombin time, fibrinogen, platelet count) with a clinically unstable, friable clot** prone to premature dissolution and rebleeding ([StatPearls NBK557467](https://www.ncbi.nlm.nih.gov/books/NBK557467/); [Altahan et al., Clin Hematol Int, PMC12825037/PMID:41583548](https://pmc.ncbi.nlm.nih.gov/articles/PMC12825037/)).

**Key identifiers:**
| System | ID |
|---|---|
| OMIM gene | *134570 (F13A1) |
| OMIM phenotype | #613225 (Factor XIII, A subunit, deficiency of) |
| Orphanet | ORPHA331 (Congenital factor XIII deficiency) |
| ICD-10-CM | D68.2 (Hereditary deficiency of other clotting factors) |
| ICD-11 | 3B14.Z |
| MeSH | D005177 |
| HGNC (gene) | HGNC:3531 (F13A1) |
| UniProt | P00488 (F13A1 protein) |

**Synonyms:** Fibrin-stabilizing factor (FSF) deficiency; congenital FXIII deficiency; FXIIIA deficiency; plasma transglutaminase deficiency.

**Evidence base:** Information is derived almost entirely from **aggregated disease-level resources** — case series, national/regional registries (notably the Iranian national FXIII deficiency registry), structured databases (OMIM, Orphanet, ClinVar), and individual case reports — rather than large EHR cohorts, reflecting the disorder's extreme rarity (<500 molecularly characterized families worldwide per recent reviews).

Sources: [OMIM *134570](https://omim.org/entry/134570) · [OMIM #613225](https://omim.org/entry/613225) · [Orphanet ORPHA331](https://www.orpha.net/en/disease/detail/331) · [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK557467/) · [Altahan et al. 2026, PMID:41583548](https://pmc.ncbi.nlm.nih.gov/articles/PMC12825037/)

---

## 2. Etiology

**Causal factors (congenital):** Biallelic (homozygous or compound heterozygous) loss-of-function variants in *F13A1* account for **~95% of congenital cases**; *F13B* variants account for the remainder and produce a generally milder phenotype because the catalytic A subunit is intact. More than 200 causative *F13A1* variants have been catalogued; missense variants predominate (>50%), with nonsense, splice-site, deep-intronic, and large structural deletions also described (Altahan et al., PMID:41583548; [PMC6950900 — deep intronic splicing variant](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6950900/); [PMC6657060 — large deletion via complex rearrangement](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6657060/)).

**Genetic risk factors:**
- **Founder mutations** create regional clustering: **Trp187Arg (c.562T>C)** is the dominant pathogenic allele in southeast Iran — in one series, 346 of 366 Iranian FXIIID patients resided in Sistan and Baluchestan Province and carried this single founder variant ([How to Assess Founder Effect..., PMC7876424](https://pmc.ncbi.nlm.nih.gov/articles/PMC7876424/); [Molecular Basis of Congenital FXIII Deficiency in Iran, PMC6714674](https://pmc.ncbi.nlm.nih.gov/articles/PMC6714674/)). **Arg77Cys** is reported as a recurrent variant in the Swiss population (search result; not independently verified against a primary source in this pass — flag as lead).
- **Consanguinity** is the dominant environmental/demographic risk amplifier for an autosomal recessive disorder of this rarity — Iran's ~12-fold elevated prevalence versus global estimates is attributed directly to consanguinity rates (StatPearls; Altahan et al.).

**Protective factors:** None specific to the *deficiency* state were identified — once activity falls below the disease threshold, no genetic or environmental factor mitigates bleeding risk other than replacement therapy. (Distinct from this disease entity: the common *F13A1* **Val34Leu** polymorphism, present in normal-activity individuals at 0–44% allele frequency across populations, is associated with a *different* clinical question — reduced risk of myocardial infarction and venous thromboembolism, OR for VTE as low as 0.16 in Leu34 homozygotes — via accelerated FXIII activation kinetics and altered fibrin fiber architecture that is more fibrinolysis-susceptible. **This is a separate phenotype of FXIII gain-of-function-type activation kinetics, not a modifier of the deficiency disease itself**, and should not be conflated with it in curation. ([Role of factor XIII polymorphisms in clot formation, Blood, search result]; ClinVar RCV000017996 "protection against myocardial infarction").

**Gene-environment interactions:** The clearest documented interaction is in **acquired (non-congenital) FXIII deficiency**, which is mechanistically distinct and more prevalent than the congenital form:
- *Autoimmune acquired FXIII deficiency*: anti-FXIII autoantibodies, with **HLA class I/II susceptibility alleles** implicated — a whole-exome sequencing study found HLA-B, MICA, BTNL2, HLA-DQB1, and HLA-DPB1 variants correlating with elevated anti-FXIII autoantibody titers, invoking a breakdown of immune tolerance analogous to acquired hemophilia A ([PMID:34506591, PLoS One 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8432773/)). Median age of onset ~75 years; ~50% idiopathic, remainder associated with autoimmune disease, diabetes, or malignancy.
- *Non-immune acquired deficiency* (more common than autoimmune): hyperconsumption (DIC, sepsis, major surgery; **ECMO carries an 80–90% reported incidence** of acquired deficiency), decreased synthesis (liver disease), and drug-associated (valproic acid, isoniazid, penicillin, phenytoin; checkpoint-inhibitor immunotherapy reported in a case report) (StatPearls; [A Rare Case of FXIII Deficiency in Cancer Immunotherapy, PMC8163106](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8163106/)).

---

## 3. Phenotypes

Severity correlates with residual FXIII activity (EN-RBD classification): **severe** (undetectable–≤1%, spontaneous major bleeding), **moderate** (<30%, heterogeneous bleeding), **mild** (≥30%, typically asymptomatic) (Altahan et al., PMID:41583548).

| Phenotype | Frequency (severe deficiency) | Onset | Suggested HP term |
|---|---|---|---|
| Delayed umbilical stump bleeding/cord separation | 70–80% of symptomatic neonates; classic earliest sign | Days–weeks after birth | HP:0031134 *(verify — candidate: delayed umbilical cord separation)* |
| Intracranial hemorrhage (spontaneous and post-traumatic) | 25–30% untreated | Infancy–childhood most common, can recur any age | HP:0002170 Intracranial hemorrhage |
| Easy bruising / subcutaneous hematoma | Bruising ~60%, hematoma ~55% | Childhood onward, with ambulation | HP:0000978 Bruising susceptibility |
| Mucosal bleeding (epistaxis, gingival bleeding, menorrhagia) | ~30% | Any age | HP:0000421 Epistaxis; HP:0000132 Menorrhagia |
| Impaired wound healing / dehiscence | 14–29% | Any age, esp. postoperative | HP:0001058 Poor wound healing *(verify exact term)* |
| Hemarthrosis | Uncommon — distinguishes from hemophilia | Any age | HP:0005261 Joint hemorrhage |
| Recurrent early pregnancy loss / placental abruption / preterm delivery | High risk without prophylaxis (see §6) | First trimester predominant | HP:0200067 Recurrent pregnancy loss *(verify exact term)* |
| Delayed postoperative/post-traumatic bleeding | Variable | Any age | HP:0031108 *(verify)* |

A single case report also describes **hydrocephalus in infancy** as a rare sequela of intracranial hemorrhage ([PMC12504050](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12504050/)) — not a primary phenotype but a downstream structural consequence.

**Quality-of-life impact:** Not quantified with standardized instruments (EQ-5D/SF-36) in the literature surfaced here — this appears to be a genuine evidence gap rather than a retrieval failure; prophylactic therapy trial reports (Mentor™ series, below) emphasize bleeding-rate reduction rather than formal QoL metrics.

*(Caveat, consistent with dismech practice: every HP term above is a candidate suggestion based on clinical description matching, not a verified OAK/HPO lookup — each must be independently confirmed against the HPO browser before binding, per the Ontology Term Contract.)*

---

## 4. Genetic/Molecular Information

**Causal gene:** *F13A1* — HGNC:3531, chromosome **6p24.3–p25.1** (sources vary slightly: 6p25.1 vs 6p24–p25; verify exact cytoband at curation time), 15 exons, encoding a 731-amino-acid catalytic subunit (UniProt P00488). The protein belongs to the transglutaminase superfamily, containing an N-terminal activation peptide (cleaved by thrombin), a β-sandwich domain, the catalytic core (containing the Cys-His-Asp catalytic triad), and two C-terminal β-barrel domains.

**Secondary gene:** *F13B* (chromosome 1q31–q32.1), encoding the non-catalytic B subunit (10 sushi/CCP domains), produced by hepatocytes; F13B deficiency accounts for ~5% of congenital cases and is generally milder.

**Variant landscape:**
- >200 *F13A1* pathogenic variants reported to date; missense variants >50% of cases, with nonsense, splice-site, deep-intronic, and gross deletion variants comprising the remainder.
- ClinVar-documented examples include nonsense variants (R171X, Y441X) and missense variants (R681H) (search-derived; individual ClinVar accessions not independently verified here — treat as leads pending direct ClinVar lookup).
- A novel **Cys328 nonsense variant** reported in a severe case ([PMC7650518](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7650518/)); eight novel *F13A1* variants with structural modeling reported by [PMC2878794](https://pmc.ncbi.nlm.nih.gov/articles/PMC2878794/).
- **Founder alleles**: Trp187Arg (Iran/southeast Iran), Arg77Cys (Switzerland, per search lead).

**Allele frequency / carrier frequency:** No specific gnomAD allele-frequency table for individual pathogenic *F13A1* variants was retrieved in this pass (a genuine gap — direct gnomAD query recommended at curation time). Aggregate carrier frequency for deficiency-causing alleles is estimated at **~1 in 1,000 globally** (~7.5 million heterozygous carriers worldwide per epidemiological extrapolation cited in search results), consistent with the homozygote prevalence of 1 in 2–3 million.

**Functional consequences:** Predominantly **loss of function** — reduced/absent catalytic transglutaminase activity, either through reduced protein synthesis/stability (Type I: concordant reduction of antigen and activity) or a qualitative catalytic defect (Type II: normal/near-normal antigen, reduced activity).

**Somatic vs. germline:** Congenital FXIII-A deficiency is exclusively germline/inherited; acquired (autoimmune or consumptive) deficiency is a distinct, non-genetic disease process (see §2).

**Epigenetics / chromosomal abnormalities:** No epigenetic mechanism (DNA methylation, histone modification) specific to FXIII-A deficiency was found in the sources retrieved — **this appears to be an absence of documented evidence rather than a negative finding**, and should not be asserted either way without a dedicated search of ENCODE/Roadmap/DiseaseMeth. Chromosomal-scale abnormalities (aneuploidy, translocation) are not a recognized disease mechanism here; point mutations and small-to-large intragenic deletions dominate.

---

## 5. Environmental Information

**Environmental/iatrogenic factors (relevant almost exclusively to *acquired* deficiency, not the congenital disease that is the primary curation target):**
- Extracorporeal membrane oxygenation (ECMO) — 80–90% reported incidence of acquired deficiency
- Sepsis, disseminated intravascular coagulation, major surgery (consumptive)
- Hepatic dysfunction (decreased synthesis)
- Medications: valproic acid, isoniazid, penicillin, phenytoin; immune checkpoint inhibitor therapy (case report, PMC8163106)
- Associated autoimmune conditions: systemic lupus erythematosus (~30% of immune-mediated acquired cases), IgA vasculitis, rheumatoid arthritis

**Lifestyle factors:** None identified as modifying congenital disease expression; trauma (including minor trauma and surgical trauma) is the principal precipitant of clinically apparent bleeding episodes in both congenital and acquired deficiency, rather than a "lifestyle" risk factor per se.

**Infectious agents:** Not a direct cause; sepsis is a recognized *trigger* of acquired consumptive deficiency but FXIII deficiency itself has no infectious etiology.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Initiating lesion:** Biallelic loss-of-function variant in *F13A1* (or, less commonly, *F13B*) → absent or structurally/catalytically defective FXIII-A protein synthesized in megakaryocytes, platelets, and monocytes/macrophages. *(Demonstrated — molecular/biochemical studies.)*
2. This **leads to** markedly reduced circulating and intracellular FXIII-A2B2 tetramer and/or reduced transglutaminase catalytic capacity, while the upstream coagulation cascade (thrombin generation, fibrinogen cleavage to fibrin monomer) proceeds entirely normally — **explaining the normal PT/aPTT/TT** that is the disorder's central diagnostic trap. *(Demonstrated.)*
3. During clot formation, thrombin (in the presence of Ca²⁺) still cleaves the FXIII-A activation peptide when substrate is present, but with insufficient functional FXIII-A, this **fails to generate adequate active FXIIIa transglutaminase** → failure of γ-glutamyl-ε-lysyl isopeptide cross-linking between fibrin γ-chains (dimerization) and α-chains (multimerization), and failure to cross-link α2-antiplasmin and fibronectin onto the fibrin network. *(Demonstrated biochemically — Reactome "Common Pathway of Fibrin Clot Formation"; [PMID search: Protransglutaminase-mediated crosslinking of fibrinogen and fibrin, PMID:11816711].)*
4. This **results in** an uncross-linked, mechanically weak, and fibrinolysis-susceptible clot — lacking the tensile strength, viscoelastic stability, and protection from plasmin-mediated degradation that cross-linking normally confers (the α2-antiplasmin cross-link specifically retards premature fibrinolysis). *(Demonstrated — [Understanding blood clot mechanical stability, 2025](https://www.sciencedirect.com/science/article/pii/S2475037925001955).)*
5. **Branch A — hemostatic plug failure:** The friable clot **leads to** delayed/recurrent hemorrhage at sites of vascular injury — classically the umbilical stump (minimal trauma, high vascular turnover site), soft tissue, and mucosa — and, most seriously, intracranial vasculature, where clot instability **results in** spontaneous or minor-trauma-triggered intracranial hemorrhage, the leading cause of death and neurological morbidity in untreated severe disease. *(Demonstrated clinically.)*
6. **Branch B — wound healing failure:** FXIIIa normally cross-links fibrin with fibronectin and collagen in the provisional wound matrix to support fibroblast migration and re-epithelialization; its absence **leads to** delayed re-epithelialization and wound dehiscence. *(Demonstrated in *F13a1*-knockout mice — [Inbal et al., Thromb Haemost 2005;94:432–437, DOI:10.1160/TH05-04-0291](https://www.thieme-connect.com/products/ejournals/pdf/10.1160/TH05-04-0291.pdf): wound closure reduced 15%/27%/27% at days 4/8/11 vs. controls; complete closure by day 11 in controls vs. 73.2% in FXIII-deficient mice.)*
7. **Branch C — reproductive/placental failure:** Maternal FXIII-A normally localizes to the maternal-fetal interface and is required, around gestational weeks 6–8, for fibrin-fibronectin cross-linking that forms the **cytotrophoblastic shell and Nitabuch's layer**, anchoring the placenta to the decidua; its absence **leads to** poorly formed cytotrophoblastic shells, placental detachment, and spontaneous miscarriage. *(Demonstrated histologically in human gestational tissue from FXIII-deficient pregnancies, and recapitulated in *F13a1*-knockout mice, which develop severe uterine bleeding and spontaneous miscarriage — [Koseki-Kuno et al., Blood 2003;102(13):4410–4412, DOI:10.1182/blood-2003-05-1467](https://ashpublications.org/blood/article/102/13/4410/17448/); human tissue study: [Maternal Blood Coagulation Factor XIII...Cytotrophoblastic Shell](https://www.sciencedirect.com/science/article/abs/pii/S0143400499904897).)*
8. **Upstream vs. downstream summary:** The genetic lesion (step 1) and loss of catalytic activity (steps 2–4) are strictly **upstream**, shared across all clinical branches; steps 5–7 are **parallel downstream branches** determined by the anatomical site of hemostatic/structural demand (vascular injury site, wound bed, maternal-fetal interface) rather than by distinct molecular mechanisms.

### Molecular pathways, processes, and profiling
- **Pathway:** Reactome "Common Pathway of Fibrin Clot Formation" (FXIII tetramer cleavage → FXIIIa → fibrin multimer cross-linking); candidate **GO terms**: GO:0003810 (protein-glutaminase gamma-glutamyltransferase activity — the core catalytic GO term for F13A1), GO:0007596 (blood coagulation), GO:0072378 (blood coagulation, fibrin clot formation), GO:0031639 (plasminogen activation) as a related/antagonized process.
- **Cellular processes / cell types:** FXIII-A is synthesized by **megakaryocytes** (CL:0000556) and stored in **platelet** (CL:0000233) α-granules/cytoplasm; also expressed in **monocytes/macrophages** (CL:0000576/CL:0000235). FXIII-B is synthesized by **hepatocytes** (CL:0000182). The placental mechanism implicates **trophoblast** (CL:0000351/CL:0000666 extravillous trophoblast) populations at the maternal-fetal interface.
- **Protein structure/dysfunction:** Predominantly simple loss of function via reduced protein stability/synthesis (Type I) or catalytic-site disruption (Type II); no prion-like aggregation or gain-of-function mechanism described.
- **Subcellular localization:** FXIII-A is a **cytoplasmic** transglutaminase lacking a classical secretory signal peptide; it reaches plasma via non-classical secretion from platelets/monocytes rather than conventional ER/Golgi trafficking — relevant GO Cellular Component candidate: GO:0005829 (cytosol).
- **Non-hemostatic roles (beyond the classic pathograph):** FXIII-A participates in macrophage function, innate immune regulation, angiogenesis, and broader extracellular-matrix cross-linking — reviewed in [Factor XIII-A in Diseases: Role Beyond Blood Coagulation, PMC7867190](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7867190/).
- **Omics/advanced technologies:** No transcriptomic, proteomic, metabolomic, or single-cell/spatial datasets specific to FXIII-A deficiency were surfaced in this pass. This is flagged as an evidence gap rather than confirmed absence; GEO/Human Protein Atlas should be queried directly for F13A1 expression data if module-level curation requires it.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Skin/soft tissue (bruising, hematoma), umbilical cord stump (neonatal bleeding), central nervous system/brain (intracranial hemorrhage — most severe complication), female reproductive tract/placenta (pregnancy loss, postpartum hemorrhage), mucosal surfaces (nose, gingiva, GI tract).
- **Secondary:** Joints (uncommon hemarthrosis, contrasting with hemophilia), muscle (intramuscular hematoma), surgical/wound sites generally (impaired healing, dehiscence).
- **Body systems:** Hematologic (primary), integumentary, reproductive, nervous (via ICH), musculoskeletal (uncommon).

**Tissue/cell level:** Vascular endothelium and perivascular connective tissue at sites of hemorrhage; dermal/epidermal wound bed (impaired re-epithelialization); placental cytotrophoblast shell and decidual interface (Nitabuch's layer).

**Subcellular level:** Cytoplasmic localization of FXIII-A in platelets/monocytes (candidate GO:0005829 cytosol); no organelle-specific pathology (e.g., no mitochondrial or lysosomal component to this disease).

**Anatomical term candidates (UBERON):** umbilical cord (UBERON:0002331), brain (UBERON:0000955), placenta (UBERON:0001987), skin (UBERON:0002097), uterus (UBERON:0000995). *(Candidates only — verify against OAK before binding.)*

**Lateralization:** Not applicable — bleeding events are determined by site of trauma/vascular demand, not a lateralized anatomical predisposition.

---

## 8. Temporal Development

**Onset:** Severe congenital disease classically presents in the **neonatal period** with delayed umbilical stump bleeding occurring days to weeks after cord separation — described as potentially "the earliest manifestation," in up to 80% of affected neonates. Moderate/mild disease may remain asymptomatic until a hemostatic challenge (surgery, trauma, pregnancy) unmasks it.

**Onset pattern:** Typically insidious/chronic bleeding tendency punctuated by acute bleeding episodes, rather than a single acute presentation — though intracranial hemorrhage itself is an acute, life-threatening event.

**Progression:** Untreated severe disease follows a **relapsing** pattern of recurrent hemorrhagic events across the lifespan; intracranial hemorrhage specifically carries a ~30% recurrence rate, and ~50% of recurrences are fatal (StatPearls). With prophylactic replacement, the disease course is effectively **stabilized**.

**Disease duration:** Lifelong (congenital form); acquired immune-mediated disease may remit with immunosuppression and autoantibody clearance.

**Critical periods:**
- **Neonatal period** — umbilical bleeding as sentinel event for diagnosis.
- **Gestational weeks 6–8** — cytotrophoblastic shell/Nitabuch's layer formation at the maternal-fetal interface is the specific developmental window in which FXIII-A deficiency precipitates early pregnancy loss.
- **Perioperative periods** and **late pregnancy/peripartum** — periods of heightened hemostatic demand requiring dose escalation of replacement therapy.

---

## 9. Inheritance and Population

**Epidemiology:**
- Prevalence of severe congenital FXIII deficiency: **~1 in 2–3 million** live births globally (multiple concordant sources).
- **Iran**: ~12-fold higher prevalence than the global estimate, attributed to consanguinity, with strong founder-effect clustering (Trp187Arg) in Sistan and Baluchestan Province.
- **Carrier frequency**: ~1 in 1,000 individuals globally (heterozygotes), translating to an estimated ~7.5 million carriers worldwide.
- No specific incidence (new-case) rate was identified distinct from birth prevalence — appropriate, since this is a congenital condition present from birth rather than one with a variable incident onset.

**Inheritance pattern:** Autosomal recessive.

**Penetrance/expressivity:** Phenotype severity correlates closely with residual FXIII activity level (severe <1%, moderate <30%, mild ≥30%), implying substantial genotype-phenotype correlation for biallelic null alleles, though no formal penetrance estimate (e.g., proportion of homozygotes who never bleed) was found in the sources retrieved.

**Anticipation / germline mosaicism:** No evidence of genetic anticipation (expected, as this is not a repeat-expansion disorder) or germline mosaicism specific to this condition was found.

**Founder effects:** Well documented — Trp187Arg (Iran/southeast Iran) is the clearest example, with a dedicated methodological paper on assessing founder effects in this disease (PMC7876424). Arg77Cys in the Swiss population is a secondary lead requiring independent verification.

**Population demographics:**
- **Sex ratio:** Equal (autosomal recessive; no sex-linked modifier identified for the bleeding phenotype itself, though pregnancy-related morbidity is obviously female-specific).
- **Geographic distribution:** Elevated prevalence wherever consanguinity rates are high — Iran most prominently; also historically documented clustering in other Middle Eastern and South Asian populations per the broader rare-bleeding-disorder literature (not independently itemized with PMIDs in this pass).
- **Age distribution:** Severe cases are predominantly diagnosed in infancy/early childhood (umbilical bleeding, early ICH); moderate/mild cases may be diagnosed incidentally in adulthood (surgical bleeding, recurrent miscarriage workup) or remain undiagnosed.

---

## 10. Diagnostics

**The central diagnostic principle:** PT, aPTT, thrombin time, fibrinogen, and platelet count are **all normal** in FXIII deficiency, because FXIII acts after fibrin polymer formation. High clinical suspicion — especially with a history of delayed umbilical bleeding, consanguinity, family history, or unexplained recurrent miscarriage — is required to trigger specific testing.

**Laboratory tests:**
1. **Clot solubility test** (5 mol/L urea or 1% monochloroacetic acid) — the traditional screening test; simple and cheap but **poor sensitivity/specificity**, missing mild-to-moderate deficiency; increasingly regarded as obsolete/"deprecated" in current reviews (Altahan et al.; PMID:42682775 review).
2. **Quantitative functional activity assays (preferred first-line):**
   - **Ammonia-release assay** (e.g., Berichrom®, Technochrom®) — most widely used; FXIII activated by thrombin/Ca²⁺, liberated ammonia measured via glutamate dehydrogenase-coupled NADH oxidation at 340 nm; lower limit of quantification ~3–5%.
   - **Isopeptidase/fluorogenic assay** (Technofluor® FXIII Activity) — direct fluorescence from isopeptide bond cleavage.
   - **Amine incorporation assay** — high sensitivity but more time-consuming, and notably **confounded by the Val34Leu polymorphism**, which accelerates activation and can cause overestimation of activity in this assay type (ammonia-release assays are unaffected by Val34Leu).
3. **Antigen assays** (ELISA, latex agglutination, chemiluminescence) — distinguish **Type I** (concordant reduction in antigen and activity) from **Type II** (isolated activity reduction with preserved antigen), and differentiate FXIII-A–specific from FXIII-B–specific deficiency — directly relevant to treatment selection (see §12).
4. **Inhibitor/mixing studies** — 1:1 mixing of patient plasma with pooled normal plasma, activity measured immediately and after 1–2 h incubation at 37 °C, to distinguish deficiency from acquired autoantibody inhibition; ELISA detects non-neutralizing antibodies.
5. **Preanalytical requirement:** Platelet-poor plasma is essential, since platelet-associated FXIII-A can spuriously elevate apparent plasma activity.
6. **Viscoelastic testing (TEG/ROTEM):** Standard tracings reflect thrombin-driven fibrin formation and **cannot reliably exclude clinically significant FXIII deficiency** — an important limitation given the increasing point-of-care use of these assays.

**Genetic testing:** Targeted NGS panels covering *F13A1* and *F13B*, with deletion/duplication analysis to capture structural variants and deep-intronic mutations, confirm a causative variant in the large majority (~95%) of congenital cases. Molecular confirmation has direct therapeutic implications (recombinant FXIII-A₂ is ineffective for *F13B*-driven disease — see §12).

**Differential diagnosis:** Afibrinogenemia/dysfibrinogenemia, hemophilia A/B, von Willebrand disease, platelet function disorders (Glanzmann thrombasthenia, Bernard-Soulier syndrome), and other rare factor deficiencies (FII, FV, FVII, FX, FXI) — all of which, unlike FXIII deficiency, typically show an abnormal screening coagulation profile.

**Screening:** FXIII deficiency is **not** part of standard newborn screening panels; diagnosis is case-finding, triggered by the clinical sentinel of delayed umbilical bleeding or a positive family history/consanguinity.

---

## 11. Outcome/Prognosis

**Untreated severe congenital disease:**
- **66.7%** experience a serious hemorrhagic event over their lifetime (StatPearls).
- Intracranial hemorrhage is the **primary cause of death**; recurrence risk ~30%, with **~50% mortality per recurrence**, and **~50% of survivors developing neurological sequelae**.

**With replacement prophylaxis:** Patients receiving regular replacement therapy can expect **life expectancy comparable to the general population** (StatPearls), and prophylaxis is reported to essentially eliminate spontaneous and intracranial bleeding.

**Quantified bleeding-rate outcomes (recombinant FXIII-A₂, Mentor™ trial series):**
- Monthly 35 IU/kg prophylaxis achieved an annualized bleeding rate (ABR) of **0.138**, versus **2.91** with historical on-demand treatment (Mentor™1).
- Mentor™2 long-term extension: ABR declined further to **0.043** (mean spontaneous ABR 0.011) over 186.5 patient-years.

**Acquired immune-mediated deficiency:** Carries a substantially worse near-term prognosis — **~25% mortality within the first year** of diagnosis, reflecting both the typically older, comorbid patient population (median age ~75) and diagnostic delay.

**Morbidity:** Recurrent miscarriage (reproductive morbidity) and impaired wound healing (surgical/procedural morbidity) are the dominant non-fatal outcomes; both are reported to be "dramatically improved" with prophylactic treatment, though formal quality-of-life instrument data were not found in this search pass.

---

## 12. Treatment

**Plasma-derived FXIII concentrate** — *Corifact* (US) / *Fibrogammin P* (EU/other regions): contains **both A and B subunits**, making it effective regardless of whether the causative gene is *F13A1* or *F13B*. Available in Europe since 1993; FDA-approved in the US as Corifact. Dosing: ~40 IU/kg initial/loading dose, maintenance dosing approximately every 28 days, titrated to a trough activity target of **5–20%**. Half-life ~7–9 days.

**Recombinant FXIII-A₂ (catridecacog)** — *Tretten* (US) / *NovoThirteen* (EU), Novo Nordisk: FDA-approved **December 2013** for routine prophylaxis in congenital FXIII **A-subunit** deficiency specifically; a homodimer of recombinant A subunits that binds endogenous B subunits in circulation; **not effective for *F13B*-driven (B-subunit) deficiency**. Monthly dosing 35 IU/kg; half-life ~11 days. Pediatric dosing validated down to age ≤6 years without age-based adjustment (Mentor™4 trial).

**On-demand/perioperative therapy:** 20–40 IU/kg targeting 20–30% activity for minor-to-moderate procedures, with proportionally higher targets for major surgery.

**Bridge therapies (when concentrate unavailable):** Fresh frozen plasma (~288 ± 77 IU/unit) and cryoprecipitate (~60 ± 30 IU/unit) — both have highly variable FXIII content between units/products and are regarded as second-line.

**Pregnancy management:** Early initiation (by 5 weeks' gestation in one described regimen); fortnightly or weekly dosing to maintain trough activity **≥10–20%** through early/mid gestation, escalating to **≥30%** in late pregnancy and peripartum; neuraxial anesthesia considered safe at ≥30% activity; tranexamic acid is emphasized for postpartum hemorrhage prevention; planned cesarean delivery is recommended in affected/potentially affected severe-deficiency pregnancies; multidisciplinary (obstetrics/hematology/anesthesia) management is recommended throughout.

**Acquired immune-mediated deficiency:** First-line immunosuppression with corticosteroids ± rituximab (response typically 4–8 weeks); cyclophosphamide or mycophenolate mofetil for non-responders; plasma exchange for short-term autoantibody removal in acute severe bleeding; FXIII replacement alongside immunosuppression; identification and treatment of the underlying trigger is emphasized as essential.

**Anticoagulation co-management:** No established guideline exists; a single case-report-level source (Bounaix et al., cited secondhand) suggests rivaroxaban may be used safely with adjusted FXIII replacement intensity (50% activity during anticoagulant loading, 30% maintenance, 20% prophylactic) — **this is case-report-level evidence only and should be labeled as such, not as a guideline-supported approach**.

**Adverse effects:** Both replacement products are generally well tolerated; reported adverse events (≥1%) include headache, leucopenia, joint inflammation, and skin reactions; rare serious events include hypersensitivity, thromboembolic complications, and (extremely rarely) neutralizing inhibitor development.

**NCIT mapping candidates:** `NCIT:C15986` (Pharmacotherapy) as the generic treatment_term, with `therapeutic_agent` bound to the specific product — a dedicated NCIT code for catridecacog/Corifact was not confirmed in this search pass and should be looked up directly in the NCIT browser at curation time (candidate search term: "Factor XIII Concentrate" / "Catridecacog").

**No gene therapy, cell therapy, or RNA-based therapeutics** for this disorder were identified — protein replacement remains the entire therapeutic armamentarium; this is consistent with the disease being a straightforward enzyme-replacement-amenable deficiency rather than one requiring correction at the genomic/transcript level.

---

## 13. Prevention

**Primary prevention:** Genetic counseling for known carrier couples, particularly in consanguineous unions or communities with known founder mutations (e.g., Iranian populations with Trp187Arg); carrier testing is the principal actionable primary-prevention lever given the condition's Mendelian, fully recessive architecture.

**Secondary prevention / early detection:** No population-based newborn screening program exists for this condition; early detection instead relies on clinical vigilance for the sentinel sign of delayed umbilical stump bleeding, prompting targeted FXIII activity testing. Cascade testing of siblings/relatives of an index case is a reasonable extrapolation from general AR-disorder practice, though a specific citation for FXIII deficiency cascade-screening programs was not retrieved in this pass (flagged as a gap, not a negative finding).

**Tertiary prevention:** Regular prophylactic replacement therapy is the dominant tertiary-prevention strategy, directly preventing recurrent and spontaneous bleeding (including the life-threatening ICH complication) and improving obstetric outcomes in affected women.

**Genetic counseling / prenatal options:** Once a familial pathogenic variant is known, prenatal diagnosis (chorionic villus sampling or amniocentesis) is mechanistically feasible by standard molecular genetics practice for AR disorders — **this specific application to FXIII deficiency was not independently documented by a retrieved source in this pass** and should be treated as a reasonable inference pending direct literature confirmation rather than an established citation.

**Immunization / public health / prophylactic medication beyond replacement therapy:** Not applicable — this is not a disease with a vaccine-preventable or public-health-intervention-amenable etiology.

---

## 14. Other Species / Natural Disease

**Naturally occurring disease in other species:**
- **Japanese Black cattle** — naturally occurring FXIII deficiency reported (cited in a 2026 comparative veterinary paper; primary citation not independently retrieved in this pass).
- **Domestic dog** — a 2026 case report describes a **4-month-old male Black and Tan Coonhound** presenting with spontaneous hemoperitoneum, thrombocytopenia, and persistent post-surgical bleeding, found to carry an ***F13A1* frameshift (deletion-insertion) variant** producing a premature stop codon; viscoelastic testing showed reduced clot firmness and enhanced fibrinolysis in high-urea conditions suggestive of FXIII deficiency ([PMID:42184124 / PMC13200534](https://pmc.ncbi.nlm.nih.gov/articles/PMC13200534/)). Search results explicitly note this is the first well-characterized canine case and did **not** identify a Dachshund-specific founder condition, despite that breed association appearing plausible a priori — **do not assume a Dachshund-specific form without further verification.**

**Comparative biology:** The transglutaminase cross-linking mechanism and thrombin-dependent activation are conserved across mammalian species studied (human, mouse, cattle, dog), consistent with FXIII's role as a terminal, highly conserved step of the coagulation cascade.

**Orthologous genes:** Mouse *F13a1* (MGI:1921395); rat *F13a1* (RGD:621495 / RGD:732286 per search results — two RGD entries appeared, requiring disambiguation at curation time).

**Zoonotic potential:** Not applicable — this is a non-infectious, genetically determined disorder with no cross-species transmission mechanism.

---

## 15. Model Organisms

**Primary model: *F13a1*-knockout mouse**
- **Original line:** Targeted inactivation of the mouse *F13a1* locus (deletion of exon 7), establishing hemostatic abnormalities and characterizing the coagulation deficit — [Lauer et al., PMID:12529747](https://pubmed.ncbi.nlm.nih.gov/12529747/).
- **Reproductive phenotype:** *F13a1*-deficient female mice develop **severe uterine bleeding events and subsequent spontaneous miscarriages**, directly recapitulating the human reproductive phenotype and supporting the cytotrophoblastic-shell mechanism described in §6 — [Koseki-Kuno et al., Blood 2003;102(13):4410–4412, DOI:10.1182/blood-2003-05-1467](https://ashpublications.org/blood/article/102/13/4410/17448/).
- **Wound-healing phenotype:** Knockout mice show delayed wound closure (15%, 27%, 27% reductions at days 4, 8, 11 vs. controls; 73.2% vs. 100% closure by day 11) with histologic evidence of delayed re-epithelialization and necrotized fissures, **rescued by exogenous FXIII treatment** (90.1% closure by day 11 in treated knockouts) — [Inbal et al., Thromb Haemost 2005;94:432–437, DOI:10.1160/TH05-04-0291](https://www.thieme-connect.com/products/ejournals/pdf/10.1160/TH05-04-0291.pdf).
- **Other reported phenotypes in this model:** impaired clot retraction ([Impaired clot retraction in FXIII A subunit–deficient mice, Blood 115(6):1277](https://www.bloodjournal.org/content/bloodjournal/115/6/1277.full.pdf)); aggravated cardiac rupture and impaired post-infarct wound healing/remodeling in a myocardial infarction model ([Circulation 2006, PMC4066325](https://ncbi.nlm.nih.gov/pmc/articles/PMC4066325)) — relevant to FXIII's broader tissue-repair role (§6) rather than to the bleeding-disorder phenotype per se; metabolic phenotype (signs of "metabolically healthy obesity" on high-fat diet) has also been reported, indicating pleiotropic non-hemostatic roles ([Sci Rep 2016, srep35574](https://www.nature.com/articles/srep35574)).
- **Phenotype recapitulation assessment:** The mouse model recapitulates the two best-characterized human mechanistic branches (reproductive loss, impaired wound healing) with good fidelity, including a histological and functional correlate of the human cytotrophoblastic-shell defect. **Limitation:** the model's relevance to the *intracranial hemorrhage* phenotype — arguably the most clinically important human complication — was not specifically described in the sources retrieved in this pass; this should be checked directly against the primary mouse-model literature before treating ICH as "recapitulated" in any computational-model link.

**Resource:** IMPC/MGI phenotype data for *F13a1* (MGI:1921395) is available via [mousephenotype.org](http://www.mousephenotype.org/data/genes/MGI:1921395) for further systematic phenotype mining.

**Other model systems (zebrafish, Drosophila, C. elegans, iPSC/organoid):** None were identified in this search pass. Given that FXIII-mediated fibrin cross-linking is a vertebrate-coagulation-specific mechanism, invertebrate models are mechanistically implausible; no evidence of a zebrafish or iPSC-derived model was found, and this is reported as an **absence of retrieved evidence**, not a confirmed non-existence.

---

## Summary of Evidence Gaps (flagged explicitly per attribution discipline)

1. **MONDO ID discrepancy** between the brief (MONDO:0013187) and what search results return (MONDO:0018029) — resolve against the ontology directly.
2. No gnomAD-level allele-frequency table for specific pathogenic *F13A1* variants was retrieved.
3. No epigenetic (DNA methylation/histone) data specific to this disease were found.
4. No formal QoL-instrument (EQ-5D/SF-36) data specific to FXIII deficiency were found.
5. No transcriptomic/proteomic/single-cell dataset specific to this disease was retrieved.
6. Prenatal diagnosis practice (CVS/amniocentesis) for FXIII deficiency specifically is inferred from general AR-disorder practice, not directly documented in a retrieved source.
7. The Swiss Arg77Cys founder-variant claim and several individual ClinVar accession numbers are search-engine-summarized leads, not independently verified against primary ClinVar/literature records.
8. Mouse-model fidelity for the intracranial hemorrhage phenotype specifically was not addressed in the sources reviewed.

---

### Sources (primary links retrieved in this research pass)

- [OMIM *134570 — F13A1](https://omim.org/entry/134570)
- [OMIM #613225 — Factor XIII, A Subunit, Deficiency Of](https://omim.org/entry/613225)
- [Orphanet ORPHA331 — Congenital factor XIII deficiency](https://www.orpha.net/en/disease/detail/331)
- [StatPearls — Factor XIII Deficiency, NBK557467](https://www.ncbi.nlm.nih.gov/books/NBK557467/)
- [StatPearls — Physiology, Factor XIII, NBK538271](https://www.ncbi.nlm.nih.gov/books/NBK538271/)
- [Altahan et al., "Factor XIII Deficiency: A Review of Biology, Testing, and Treatment," PMID:41583548 (PMC12825037)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12825037/)
- [PMID:42682775, Frontiers in Medicine 2026 — diagnosis and management update (PMC13530902)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13530902/)
- [PMID:11826242 — Delayed umbilical bleeding as presenting feature](https://pubmed.ncbi.nlm.nih.gov/11826242/)
- [Lauer et al., PMID:12529747 — Targeted inactivation of mouse F13a1](https://pubmed.ncbi.nlm.nih.gov/12529747/)
- [Koseki-Kuno et al., Blood 2003;102(13):4410 — uterine bleeding/miscarriage in F13a1-deficient mice](https://ashpublications.org/blood/article/102/13/4410/17448/)
- [Inbal et al., Thromb Haemost 2005;94:432 — impaired wound healing in FXIII-deficient mice](https://www.thieme-connect.com/products/ejournals/pdf/10.1160/TH05-04-0291.pdf)
- [PMID:34506591 — HLA associations in autoimmune FXIII deficiency (PMC8432773)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8432773/)
- [PMID:42184124 — F13A1 frameshift variant in a Coonhound dog (PMC13200534)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13200534/)
- [How to Assess Founder Effect in Congenital FXIII Deficiency, PMC7876424](https://pmc.ncbi.nlm.nih.gov/articles/PMC7876424/)
- [Molecular Basis of Congenital FXIII Deficiency in Iran, PMC6714674](https://pmc.ncbi.nlm.nih.gov/articles/PMC6714674/)
- [Factor XIII-A in Diseases: Role Beyond Blood Coagulation, PMC7867190](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7867190/)
- [GeneCards — F13A1](https://www.genecards.org/cgi-bin/carddisp.pl?gene=F13A1)
- [MGI — F13a1, MGI:1921395](https://www.informatics.jax.org/marker/MGI:1921395)
- [MalaCards — Factor XIII Deficiency](https://www.malacards.org/card/factor_xiii_deficiency)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 23 |
| On topic | 14 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:11816711` *(abstract only)*: "Common Pathway of Fibrin Clot Formation"
  - closest text in source: "Thus, factor XIII displays constitutive enzymatic activity with respect to fibrinogen and fibrin"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 9 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013187` (3 mentions) - the report calls it "MONDO ID discrepancy** between the brief"; MONDO calls it **factor XIII, A subunit, deficiency of**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0003810` (1 mention) - the report calls it "protein-glutaminase gamma-glutamyltransferase activity — the core catalytic GO term for F13A1"; GO calls it **protein-glutamine gamma-glutamyltransferase activity**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`, `RGD`.