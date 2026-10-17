---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5-5
cached: false
start_time: '2026-10-04T02:17:54.410820'
end_time: '2026-10-04T02:19:10.039043'
duration_seconds: 75.63
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Acrodermatitis Enteropathica
  mondo_id: MONDO:0008713
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
  - claude-sonnet-5-5
  web_search_requests: 3
  num_turns: 5
  total_cost_usd: 0.8411834
  session_id: 81562984-f39d-5787-be67-7015e0b1b678
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 10
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 6
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 14
  verified: 14
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 1
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0008713
    reported_labels:
    - given in the template
    ontology_label: acrodermatitis enteropathica
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acrodermatitis Enteropathica
- **MONDO ID:** MONDO:0008713 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Acrodermatitis Enteropathica** covering all of the
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

# Acrodermatitis Enteropathica (AE), Research Report

**Scope and verification status.**
- I ran three web searches. They confirmed the gene–disease link, the mouse model, and the existence of recent reviews.
- Search results returned PMC IDs and URLs, not PMIDs. I did not verify any PMID or snippet against `references_cache/`.
- Every PMC link below is a lead. Before use, run `just fetch-reference PMC…` or `just fetch-reference PMID:…` and quote snippets only from the cached text.
- Ontology CURIEs marked † were written from memory. Per the CLAUDE.md rule, confirm each with `runoak` or `just validate-terms` before binding.
- I give no direct quotes, because none were retrieved verbatim.

---

## 1. Disease Information

**Overview.**
- AE is an autosomal recessive disorder of intestinal zinc uptake.
- It presents as a triad: periorificial and acral dermatitis, alopecia, and diarrhea.
- Onset is typically in infancy, often at weaning from breast milk.
- Without zinc it is progressive and can be fatal.
- Lifelong zinc supplementation produces rapid remission.

**Identifiers.**
- MONDO:0008713 (given in the template).
- OMIM #201100.† OMIM is not reachable here, so check the number.
- NCBI Gene 55630 (SLC39A4) appeared in the search results.
- hgnc:17129† (lowercase prefix per repo convention).
- UniProt Q6P5W5† (ZIP4).
- Orphanet, ICD-10 (E83.2 "Disorders of zinc metabolism")† and ICD-11 codes were not checked. Use `ORPHA:` via `just fetch-reference` for citable rows.

**Synonyms.** Danbolt–Closs syndrome, hereditary zinc deficiency, congenital zinc malabsorption.

**Individual vs aggregate data.** This report draws on aggregate disease-level literature and reviews, not EHR data.

**Entry-granularity note.** Distinguish this entry from acquired or transient zinc deficiency that mimics AE:
- breast milk with low zinc, from maternal *SLC30A2* (ZnT2) variants causing transient neonatal zinc deficiency;
- parenteral nutrition;
- malabsorption.

These phenocopies are not AE. Several recent reviews conflate them, so keep the scope explicit.

**Key reviews (leads).**
- 2025 systematic review (190 articles, 231 patients; Frontiers in Nutrition): https://www.frontiersin.org/articles/10.3389/fnut.2025.1590075/full
- Pediatric literature review of real-world studies: https://pmc.ncbi.nlm.nih.gov/articles/PMC12202354
- StatPearls chapter: https://www.ncbi.nlm.nih.gov/books/NBK441835/ (point-of-care source; do not treat as a baseline).
- Acta Dermato-Venereologica 96(3) (DOI 10.2340/00015555-2240): https://medicaljournals.se/acta/download/10.2340/00015555-2240
- A GeneReviews chapter may not exist. Check with `just check-genereviews kb/disorders/Acrodermatitis_Enteropathica.yaml` before saying so in `notes`.

---

## 2. Etiology

**Causal factor.**
- Biallelic loss-of-function variants in *SLC39A4* (8q24.3) impair the apical enterocyte zinc importer ZIP4.
- Wang et al. (2001) mapped the locus by homozygosity mapping.
- Küry et al. (2002) and Wang et al. (2002) identified *SLC39A4* independently.
- Source for the timeline: https://pmc.ncbi.nlm.nih.gov/articles/PMC419995/ and https://pmc.ncbi.nlm.nih.gov/articles/PMC2995241.

**Genetic risk and modifiers.**
- Most cases are monogenic.
- A search result noted that standard zinc supplementation can fail in some cases, and that failure is frequent in AE-like presentations tied to metabolic disorders (Frontiers 2025 review above). I did not confirm the mechanism.
- Residual-function alleles may influence the age at presentation and the required zinc dose. This is inferred and needs a source.

**Environmental risk factors.**
- Dietary zinc intake interacts with the genotype.
- Breast milk contains bioavailable zinc, so symptoms often appear at weaning. Confirm with a primary source.
- Infection, diarrhea and increased demand (rapid growth) can unmask or worsen deficiency.

**Protective factors.** Breast feeding is described as delaying onset. High-dose zinc fully controls the disease.

**Gene–environment interaction.** Genotype sets the absorptive capacity, and dietary zinc availability and demand determine whether tissue zinc falls below threshold. The mouse intestinal knockout fits this: it is rescued by high dietary zinc (see Section 15).

---

## 3. Phenotypes

Frequencies were not retrieved. Mark them "not assessed" unless Orphanet's HPO table is cached (`ORPHA:` rows are quotable).

| Phenotype | HPO (verify†) | Notes |
|---|---|---|
| Periorificial dermatitis (eczematous, vesiculobullous, pustular, psoriasiform) | HP:0000988 Skin rash† or a more specific dermatitis term | Perioral, perianal, genital |
| Acral dermatitis | as above | Hands, feet, elbows, knees |
| Alopecia | HP:0001596† | Scalp, eyebrows, eyelashes |
| Diarrhea | HP:0002014† | Chronic |
| Failure to thrive | HP:0001508† | |
| Irritability and emotional lability | – | Often described in zinc deficiency |
| Paronychia, nail dystrophy | – | |
| Conjunctivitis, photophobia | – | |
| Immunodeficiency and recurrent infection (e.g., *Candida*) | – | Zinc-dependent T-cell function |
| Low plasma or serum zinc, low alkaline phosphatase | lab abnormality | Alkaline phosphatase is a zinc metalloenzyme; low activity is a known adjunct marker |

- **Onset:** infancy, typically from weeks to months of age, often at weaning.
- **Course:** progressive without treatment.
- **Severity:** variable.
- **Quality of life:** not assessed.
- Do not bind a coarse HPO term (e.g., "Abnormality of the skin") without `coarse_binding_basis`.

---

## 4. Genetic/Molecular Information

- **Gene:** *SLC39A4*, ZIP4, a member of the SLC39 (ZIP) family.
- **Variants:** about 30 variants were reported in the search summary. They affect the extracellular zinc-binding domain or one of eight transmembrane domains. Types include missense, nonsense, frameshift and splice-site variants, plus deletions.
- **Functional consequence:** loss of function and reduced zinc uptake.
- **ClinVar/ClinGen:** not queried. A ClinGen gene–disease validity assertion may exist. Check `cache/` for `CGGV:` records and copy the tier only from the source (see "Gene-Disease Validity Is Copied, Never Assigned").
- **Allele frequencies and founder variants:** not retrieved. Founder effects are reported in some populations (e.g., Middle Eastern and consanguineous families) but need a source.
- **Epigenetic and chromosomal abnormalities:** none known. Not applicable.

---

## 5. Environmental Information

- **Dietary zinc:** supply of zinc, and its bioavailability. Phytate-rich diets lower absorption.
- **Lifestyle:** not applicable beyond diet.
- **Infectious agents:** none causal. Secondary *Candida* and bacterial superinfection of skin lesions are common.
- **ECTO binding:** use `exposure to` terms only after searching ECTO. An unrecorded search is not a justification for omitting the binding.

---

## 6. Mechanism / Pathophysiology

**Ordered causal chain.**
1. Biallelic *SLC39A4* loss-of-function variants lead to absent or defective ZIP4. This is demonstrated by genetics.
2. Loss of ZIP4 at the apical brush border of duodenal and jejunal enterocytes reduces uptake of dietary and endogenous luminal zinc. This is inferred from ZIP4's localization and function; the mouse model supports it.
3. Reduced absorption leads to systemic zinc depletion, with low plasma zinc and low alkaline phosphatase. In mice, zinc falls rapidly in intestine, liver and pancreas.
4. In the gut, zinc loss reprograms Paneth cells and disrupts the intestinal stem cell niche. Sox9 and lysozyme fall, mucin accumulates, and epithelial integrity fails. This is demonstrated in mice (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3380849/). It is a plausible contributor to human diarrhea and malabsorption, but not shown in humans.
5. Zinc is a cofactor for many enzymes and transcription factors (zinc-finger proteins). Rapidly renewing epithelia (skin, hair follicle, gut) and immune cells are most sensitive. This leads to dermatitis, alopecia and immune dysfunction. The skin and hair link is inferred from general zinc biology.
6. Gut barrier damage and diarrhea increase zinc loss and malabsorption of other nutrients. This makes a feed-forward loop and leads to failure to thrive. This step is inferred.
7. Zinc supplementation at pharmacological doses lets passive or ZIP4-independent uptake restore zinc, and the cycle reverses. The exact alternative uptake route is not established here.

**Branch.** Skin and hair disease (steps 5) and gut disease (steps 4 and 6) arise in parallel from step 3. Immune dysfunction is a third branch from step 5.

**Candidate annotations (verify†).**
- GO: zinc ion transport / zinc ion import across plasma membrane (GO:0071577†); cellular zinc ion homeostasis (GO:0006882†).
- CL: enterocyte of small intestine (CL:0002254†); Paneth cell (CL:0000510†); keratinocyte (CL:0000312†).
- CHEBI: zinc(2+) (CHEBI:29105†).
- Omics, single-cell and CRISPR-screen data for AE: none located. Do not claim any.

---

## 7. Anatomical Structures Affected

- **Primary:** small intestine (duodenum, jejunum), the site of zinc absorption.
- **Secondary:** skin (periorificial, acral), hair and nails, eyes, immune system, and growth overall. Mice also show losses in liver and pancreas.
- **Cells:** enterocytes (apical brush border), Paneth cells and intestinal stem cells, keratinocytes, T cells.
- **Subcellular:** apical plasma membrane.
- **Lateralization:** bilateral and symmetric.
- UBERON terms: look up (e.g., duodenum, jejunum, skin of body). Do not write them from memory.

---

## 8. Temporal Development

- **Onset:** infancy, from days to months after birth and often at weaning. Exclusively breast-fed infants may present later.
- **Pattern:** subacute to chronic.
- **Progression:** progressive and potentially fatal without zinc. With treatment, the course is stable.
- **Duration:** lifelong. Treatment is lifelong. A claim that treatment can be stopped later in life should be treated with caution; the search results did not address it.
- **Remission:** treatment-induced and rapid. Diarrhea and irritability improve within days, skin lesions within weeks. This is a commonly stated figure and needs a citation.
- **Critical periods:** infancy and weaning.

---

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive (HP:0000007†).
- **Prevalence:** approximately 1 per 500,000 live births is the figure usually quoted, with no known ethnic predilection. I did not verify this. Use the Orphanet epidemiology row (`ORPHA:` cache) and the structured `Prevalence` slots, with `measure_type: BIRTH_PREVALENCE` if the source supports it.
- **Penetrance and expressivity:** high penetrance, with variable expressivity.
- **Consanguinity:** enriches homozygous cases.
- **Carrier frequency, founder effects, anticipation, mosaicism:** not retrieved.
- **Sex ratio:** reported as equal, unverified.
- **Geographic distribution:** worldwide.

---

## 10. Diagnostics

- **Laboratory:** low plasma or serum zinc (interpret with care; infection and low albumin affect the level). Low alkaline phosphatase is supportive. Check that the sample was collected in a zinc-free tube.
- **Genetic:** sequencing of *SLC39A4*, with deletion/duplication analysis. A panel for skin or immunodeficiency disorders, or exome sequencing, is an alternative. Biallelic pathogenic variants confirm the diagnosis.
- **Histopathology:** nonspecific, with pallor of the upper epidermis, keratinocyte necrosis and psoriasiform hyperplasia. A skin biopsy is not required.
- **Differential diagnosis:**
  - acquired zinc deficiency;
  - transient neonatal zinc deficiency from low zinc in maternal milk (*SLC30A2* variants);
  - cystic fibrosis;
  - biotin or multiple-carboxylase deficiency;
  - organic acidemias;
  - essential fatty acid deficiency;
  - candidiasis;
  - atopic or seborrheic dermatitis;
  - psoriasis;
  - Langerhans cell histiocytosis.
- **Therapeutic trial:** a prompt response to zinc supports the diagnosis but does not distinguish AE from acquired deficiency.
- **Screening:** there is no newborn screening. Prenatal or carrier testing is possible in known families.

---

## 11. Outcome/Prognosis

- **Treated:** excellent. Growth and development are normal with adherence.
- **Untreated:** the older literature describes high mortality from infection and malnutrition. Obtain a primary citation before using a number.
- **Complications:** failure to thrive, infections, and, with delayed treatment, residual growth and developmental effects.
- **Prognostic factors:** early diagnosis and adherence. Stopping zinc leads to relapse.
- **QoL:** not assessed.

---

## 12. Treatment

- **Zinc supplementation:** elemental zinc, given as sulfate, gluconate or acetate (zinc acetate has been proposed for better tolerance). The systematic review (Frontiers 2025, linked above) reports that 159 of 174 patients (91.4%) responded. The most common effective dose was 1–3 mg/kg/day of elemental zinc. The optimal dose is not agreed upon.
- **Monitoring:** plasma zinc and alkaline phosphatase. Adjust dose for growth, and for increased needs during illness.
- **Refractory cases:** zinc supplementation was frequently ineffective in AE-like disease associated with metabolic disorders (same review). Re-examine the diagnosis in these patients.
- **Adverse effects:** gastric irritation and nausea. Excess zinc can cause copper deficiency, so monitor copper.
- **Surgical, gene and cell therapy:** none. No clinical trials were identified. Search ClinicalTrials.gov before stating that none exist.
- **Preclinical:** clioquinol augmented the zinc rescue in the mouse model (https://findanexpert.unimelb.edu.au/scholarlywork/587933-clioquinol-synergistically-augments-rescue-by-zinc-supplementation-in-a-mouse-model-of-acrodermatitis-enteropathica).
- **Historical:** diiodohydroxyquin was used before zinc. This is historical background and I did not confirm it.
- **NCIT annotation:**
  - `treatment_term`: NCIT:C15986 (Pharmacotherapy). It is listed in CLAUDE.md.
  - `therapeutic_agent`: a CHEBI term for zinc sulfate or zinc acetate, verified by lookup.
  - `therapeutic_modality`: `SMALL_MOLECULE`.
  - Do not bind Nutritional Support (NCIT:C15433) as `BEHAVIORAL`.

---

## 13. Prevention

- **Primary:** none for the genotype. Genetic counseling for families.
- **Secondary:** early recognition in infants with a family history, and prompt zinc supplementation.
- **Tertiary:** lifelong zinc, with monitoring and extra dosing during illness.
- **Prenatal and preimplantation testing:** possible when the familial variants are known.
- **Vaccination:** not applicable.

---

## 14. Other Species / Natural Disease

- **Lethal trait A46 in cattle** (Friesian and Holstein) is a naturally occurring zinc-malabsorption disease resembling AE. It is reported to arise from a different gene (*SLC39A4* not implicated in my recollection; the causal gene is *DGAT1*-unrelated and I could not confirm it). Check OMIA before curating, and do not assert the gene.
- Bull terrier lethal acrodermatitis is a canine disorder with a similar skin phenotype. Its gene was not confirmed here, so check OMIA.
- No zoonotic aspects.
- Mouse *Slc39a4* orthologue: confirm the NCBI Gene ID by lookup.

---

## 15. Model Organisms

| Model | Findings | Source |
|---|---|---|
| Global *Slc39a4* (Zip4) knockout mouse | Embryonic lethal, with death during early morphogenesis. | Dufner-Beattie et al. (see https://pmc.ncbi.nlm.nih.gov/articles/PMC2634863; I did not confirm that this PMC ID is that paper) |
| Inducible, intestine-specific knockout (villin-ErtCre, floxed *Zip4*) | Wasting and death unless the mice are nursed or fed excess dietary zinc. Zinc falls rapidly in small intestine, liver and pancreas. Paneth cells are reprogrammed (labile zinc lost, then Sox9 and lysozyme fall, mucin accumulates). The stem cell niche and intestinal integrity are disrupted. | Geiser et al., PLoS Genet 2012: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3380849/ |
| Same model with clioquinol plus zinc | Synergistic rescue. | Link in Section 12 |
| Heterozygous *Zip4* mice | Reported mild effects on embryonic zinc handling. Unverified. | – |

- **Limitations:** the global knockout is not viable, which does not match the human disease, where residual function appears to be retained. The intestine-specific model is an acquired and acute model of complete loss and does not reproduce the skin phenotype in the sources I saw. Record `fidelity` and `limitations` accordingly. Use `animal_models:` with `modeled_mechanisms` targeting the zinc depletion and Paneth cell nodes. Evidence source for all of this is `MODEL_ORGANISM`.
- **Other models:** zebrafish, *Drosophila* and cell lines expressing ZIP4 variants exist. I did not search for them.

---

## Gaps and recommended next steps

1. Fetch and cache the primary references: Wang 2001 and 2002, Küry 2002, Geiser 2012, the 2025 systematic review, and the Orphanet record (`ORPHA:`). Take all quotes from the cache.
2. Verify every CURIE marked † and every OMIM, ICD and UniProt identifier.
3. Check ClinGen (`CGGV:`), the Bookshelf index (`just check-genereviews`), and ClinicalTrials.gov.
4. Resolve open items: epidemiology, untreated mortality, the bovine and canine gene assignments, and the mechanism of zinc-refractory cases.
5. Add an ECTO search for zinc exposure, recording the exact query and result in `notes`.

## Sources

- https://pmc.ncbi.nlm.nih.gov/articles/PMC419995/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC2995241
- https://pmc.ncbi.nlm.nih.gov/articles/PMC2634863
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3380849/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12202354
- https://www.frontiersin.org/articles/10.3389/fnut.2025.1590075/full
- https://www.ncbi.nlm.nih.gov/books/NBK441835/
- https://medicaljournals.se/acta/download/10.2340/00015555-2240
- https://findanexpert.unimelb.edu.au/scholarlywork/587933-clioquinol-synergistically-augments-rescue-by-zinc-supplementation-in-a-mouse-model-of-acrodermatitis-enteropathica
- https://www.disgenet.org/browser/0/1/1/C0221036/source__ALL/_b./

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 3 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008713` (1 mention) - the report calls it "given in the template"; MONDO calls it **acrodermatitis enteropathica**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCIT:C15433` (1 mention) - the report calls it "Do not bind Nutritional Support"; NCIT calls it **Nutritional Support**