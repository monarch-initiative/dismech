---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-16T13:11:55.757575'
end_time: '2026-10-16T13:13:15.978814'
duration_seconds: 80.22
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spermatogenic Failure 19
  mondo_id: MONDO:0054723
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
  num_turns: 6
  total_cost_usd: 0.8217439999999999
  session_id: e0e00ff6-67e7-5e60-9592-3e4cb1004f09
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 16
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:41341611
  relevance_assessed: 9
  on_topic: 8
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 10
  verified: 9
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 2
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0012206
    reported_labels:
    - Asthenozoospermia
    ontology_label: Abnormal sperm motility
  - term_id: HP:0012864
    reported_labels:
    - verify
    ontology_label: Abnormal sperm morphology
  - term_id: HP:0012207
    reported_labels:
    - verify
    ontology_label: Reduced sperm motility
  labels_variant: 1
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spermatogenic Failure 19
- **MONDO ID:** MONDO:0054723 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spermatogenic Failure 19** covering all of the
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

# Spermatogenic Failure 19 (SPGF19; CFAP43-related MMAF): Research Report

**Scope and verification.** This report rests on a limited web pass, not a full literature review. Each claim is marked **[verified]** (seen in a search result or page fetch this session) or **[background]** (from general knowledge, not re-checked here). Sections 7–15 are mostly [background] with no PMIDs, because I did not find primary sources for them. Check the PMIDs and quotes below against `references_cache/` (`just fetch-reference`) before using them as evidence snippets. Sources are linked in the text.

---

## 1. Disease information

**Overview.** SPGF19 is an autosomal recessive form of male infertility. Sperm show multiple morphological abnormalities of the flagella (MMAF), described as absent, short, coiled, bent and irregular-caliber flagella. This is a non-syndromic asthenoteratozoospermia phenotype. [verified: [MalaCards/OMIM summary](https://malacards.org/card/spermatogenic_failure_19), [LOVD](https://databases.lovd.nl/shared/diseases/05567)]

**Identifiers.**
- OMIM: 617592. [verified: [LOVD](https://databases.lovd.nl/shared/diseases/05567), [MGI](https://informatics.jax.org/disease/OMIM:617592)]
- MONDO: MONDO:0054723. [verified: [DrugMap entry](https://drugmap.idrblab.net/data/disease/details/DIS2ZB4B)]
- Parent class: spermatogenic failure (MONDO:0004983). [verified: same DrugMap entry]
- UMLS CUI: C4539818. [verified: same DrugMap entry]
- DOID:0070170. [verified: [GlyCosmos](https://glycosmos.org/diseases/DOID:0070170)]
- MedGen: 1614356. [verified: appears in search results]
- Orphanet, ICD-10/11 and MeSH: not checked. Orphanet likely lists the MMAF/asthenoteratozoospermia group rather than a separate SPGF19 entry [background, unverified].

**Synonyms.** SPGF19; "spermatogenic failure, type 19"; MMAF associated with CFAP43 (cilia- and flagella-associated protein 43; the older gene name is WDR96). [verified]

**Data source.** The entry is a disease-level, gene-defined entity derived from patient exome studies. It is not aggregated EHR data.

**Gene attribution discrepancy.** The [LOVD page](https://databases.lovd.nl/shared/diseases/05567) lists the gene as WDR96. That is the old symbol for CFAP43, so it is a nomenclature difference, not a conflict. OMIM, MedGen and the Disease Ontology all link the disease to CFAP43. DrugMap lists the gene–disease relationship as definitive with AR inheritance. [verified]

**Sibling entities.** SPGF20 (MONDO:0054724) is the CFAP44 counterpart and is also AR. [verified: DrugMap] The two are clinically near-identical. Both belong to a wider MMAF family that includes DNAH1 and CFAP47 (X-linked).

---

## 2. Etiology

- **Causal factor: genetic.** Biallelic (homozygous or compound heterozygous) loss-of-function variants in *CFAP43* (10q25.1). [verified]
- **Foundational study.** Tang et al. 2017 ([PMID:28552195](https://pubmed.ncbi.nlm.nih.gov/28552195/)) found compound-heterozygous CFAP43 mutations in three Han Chinese men with MMAF (P003, P028, P029), plus a homozygous frameshift in CFAP44 in a fourth. The mutations were inherited from heterozygous carriers and absent from 984 Han Chinese controls. [verified]
- **Independent replication.** Auguste/Coutton et al. ([Nat Commun 2018](https://www.nature.com/articles/s41467-017-02792-7)) screened 78 MMAF patients by exome sequencing. They found bi-allelic mutations in DNAH1 (n=6), CFAP43 (n=10) and CFAP44 (n=6), and showed the proteins are needed for flagellogenesis in mouse and *Trypanosoma brucei*. [verified via search summary; PMID not retrieved]
- **Environmental risk factors.** None established for this monogenic form. General environmental and lifestyle factors affect sperm count and motility, but nothing specific to CFAP43 is known. [background]
- **Protective factors and gene–environment interactions.** None known. [not available]
- **Modifier genes.** No data located.

---

## 3. Phenotypes

| Phenotype | Suggested HPO | Notes |
|---|---|---|
| Male infertility | HP:0003251 | Primary presentation [verified] |
| Asthenozoospermia | HP:0012206 | Reduced motility; typically severe, often near-total immotility [background] |
| Teratozoospermia / abnormal sperm morphology | HP:0012864 (verify) | Short, absent, coiled, bent, irregular-caliber flagella [verified] |
| Abnormal sperm flagellum morphology / MMAF | HP:0012207 (verify) | Defining phenotype [verified] |
| Abnormal sperm head morphology | verify | Seen in some patients and the mouse model ([PMID:33046149](https://pubmed.ncbi.nlm.nih.gov/33046149/), title only) |

- **Frequency.** Essentially penetrant in affected males: by definition they have MMAF. Exact percentages of each flagellar subtype were not retrieved.
- **Onset and course.** Congenital genetic defect, recognized in adulthood on infertility work-up. Stable and non-progressive. [background]
- **Quality of life.** No data located. Infertility-related psychosocial burden is plausible but not documented for this disease.
- **Extra-genital features.** CFAP43 and CFAP44 are conserved axonemal proteins, and respiratory manifestations have been proposed. A 2025 paper is titled "CFAP43 mutations and familial male infertility with respiratory manifestations" ([PMID:41341611](https://pubmed.ncbi.nlm.nih.gov/41341611/); title only, content not read). Most reported cases are non-syndromic.
- **Female carriers/heterozygotes.** Unaffected. The mouse knockout females are fertile. [verified]

---

## 4. Genetic/molecular information

- **Gene:** *CFAP43* (HGNC symbol CFAP43; look up the CURIE in HGNC and write it in lowercase `hgnc:` form per repository convention. I did not retrieve it, so do not copy one from here).
- **Variant types.** Compound heterozygous splice-site, frameshift, nonsense and missense variants. Examples:
  - Novel compound heterozygous variants c.1859_1860+8delinsGT and c.3071A>G ([PMID:41549427](https://pubmed.ncbi.nlm.nih.gov/41549427/)). [verified]
  - Splice acceptor-site deletion in a patient ([PMID:29277146](https://pubmed.ncbi.nlm.nih.gov/29277146/)). [verified]
  - Biallelic loss-of-function variants in Pakistani families ([PMID:34100391](https://pubmed.ncbi.nlm.nih.gov/34100391/); title only).
- **Functional consequence.** Loss of function. [verified at the level of titles and summaries]
- **Classification.** ClinGen/DrugMap: definitive. Check for a CGGV record with `just check-gene-validity`. [verified for "definitive" via DrugMap]
- **Origin.** Germline.
- **Population frequency.** Not retrieved; query gnomAD directly.
- **Epigenetics and chromosomal abnormalities.** None reported.

---

## 5. Environmental information

None established for the causal mechanism. There is no known infectious agent. No gene–environment data were located.

---

## 6. Mechanism / pathophysiology

**Causal chain (the middle steps are partly inferred):**

1. Biallelic loss-of-function variants in *CFAP43* reduce or abolish CFAP43 protein. [verified]
2. CFAP43 is a conserved axonemal-associated protein. It is required for flagellogenesis in *Trypanosoma* and mouse; the evidence comes from Trypanosoma and knockout work. [verified]
3. In elongating spermatids, loss of CFAP43 disrupts axoneme assembly and flagellar elongation. In mice, CFAP43 is also implicated in intra-manchette transport, which affects sperm head shaping and flagellum formation ([PMID:33046149](https://pubmed.ncbi.nlm.nih.gov/33046149/); title only). This step is demonstrated in model organisms, not directly in human testis.
4. The result is MMAF sperm with absent, short, coiled or bent flagella. [verified]
5. These sperm are immotile (asthenozoospermia), so natural fertilization fails: male infertility. [inferred from phenotype]
6. Because the defect is confined to the late gamete's motility apparatus, sperm DNA and oocyte activation are largely preserved, so ICSI can bypass it (see §12). [inferred; supported by clinical outcomes]

**Where this branches.** CFAP43 is also expressed in motile cilia, so a respiratory arm is possible. The evidence is thin (see §3).

- **Suggested ontology terms** (look up each in a live source before binding; do not write from memory):
  - GO: sperm flagellum assembly, cilium assembly or axoneme assembly, spermatid differentiation, sperm axoneme assembly.
  - CL: spermatid (and elongated spermatid).
  - GO CC: sperm flagellum, axoneme.
- **Omics, single-cell and screens.** None located.

---

## 7. Anatomical structures affected

- **Organ:** testis (seminiferous epithelium); sperm flagellum.
- **Cell:** spermatid / spermatozoon (CL).
- **Subcellular:** axoneme and sperm flagellum (GO CC); manchette in the mouse.
- Secondary: possibly the respiratory tract (unconfirmed). Disease is bilateral. UBERON terms need lookup.

---

## 8. Temporal development

Congenital genetic defect that manifests at spermatogenesis (post-pubertal) and is diagnosed in adults presenting with infertility. It does not progress and is lifelong. There is no remission. The critical window is reproductive age, when ICSI is available. [background]

---

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007). [verified]
- **Prevalence.** Not found. MMAF overall is rare. CFAP43 accounted for 10 of 78 patients (about 13%) in the Auguste/Coutton cohort, and combined DNAH1/CFAP43/CFAP44 about 28% in that cohort. These numbers are cohort-selected, not population rates. [verified via search summary]
- **Populations.** Reported in Han Chinese (Tang 2017) and Pakistani families ([PMID:34100391](https://pubmed.ncbi.nlm.nih.gov/34100391/)), and in a European/North African cohort (Coutton). Consanguinity is relevant in homozygous families [background].
- **Sex.** Males only are affected; females are unaffected carriers. [verified in mouse; background in human]
- Founder variants, penetrance and carrier frequency: not retrieved.

---

## 10. Diagnostics

- **Semen analysis:** severe asthenozoospermia with a high proportion of MMAF-morphology sperm; sperm count is typically near-normal. [background]
- **Microscopy:** light microscopy and transmission electron microscopy show disorganized axoneme and fibrous sheath. [background]
- **Genetic testing:** exome sequencing or an MMAF/male-infertility gene panel including *CFAP43*, *CFAP44*, *DNAH1*, *CFAP47* and others. Single-gene CFAP43 testing is a reasonable follow-up. [background]
- **Differential:** other MMAF genes (DNAH1, CFAP44, CFAP69, WDR66 and others), primary ciliary dyskinesia (PCD), and acquired causes of asthenozoospermia.
- A LOINC code for semen analysis is available, but I did not look up one. Per repository rules, use `just loinc-seed-cache` and do not type a code or label from memory.

---

## 11. Outcome / prognosis

- No increased mortality is expected. [background]
- Fertility prognosis with ICSI is good (see §12).
- Sperm head defects in MMAF may affect embryo development; the mouse study is [PMID:40070084](https://pubmed.ncbi.nlm.nih.gov/40070084/) (title only).

---

## 12. Treatment

- **No curative or disease-modifying treatment exists.**
- **ICSI (intracytoplasmic sperm injection)** is the established route. Suggested NCIT term: look up *Intracytoplasmic Sperm Injection* or the closest assisted-reproduction term in a live source, rather than writing a code from memory.
  - [Sha et al. 2019, Andrologia](https://onlinelibrary.wiley.com/doi/10.1111/and.13151): retrospective cohort of six patients with CFAP44 or CFAP43 mutations versus DNAH1 patients and controls. The authors found no statistically significant differences in transferable embryo, implantation, clinical pregnancy or miscarriage rates, and concluded that MMAF patients with these mutations have a good ICSI prognosis. [verified via search summary; small cohort]
  - A newer report ([PMID:41549427](https://pubmed.ncbi.nlm.nih.gov/41549427/)) describes compound heterozygous CFAP43 variants with ICSI resulting in a live birth. [verified]
  - Fertility outcomes after ICSI are also described in [PMID:36960497](https://pubmed.ncbi.nlm.nih.gov/36960497/) (title only).
- **Pharmacotherapy and PGx.** Hormonal or antioxidant therapies are not established for genetic MMAF. [background]
- **Gene therapy, cell therapy and clinical trials.** None identified; I did not search ClinicalTrials.gov.
- **Oocyte activation:** not usually needed for this class of defect, but I have no source.

---

## 13. Prevention

- Genetic counseling: AR recurrence risk is 25% per pregnancy for carrier couples. Brothers of an affected man have a 25% chance of being affected. [background]
- Prenatal or preimplantation genetic testing is possible once the familial variants are known. Carrier screening for CFAP43 is not routine. [background]
- No primary prevention exists. Daughters of affected men are obligate carriers.

---

## 14. Other species / natural disease

- Orthologs exist in mouse and in *Trypanosoma brucei*. Gene IDs (NCBI Gene) and NCBITaxon CURIEs should be looked up rather than written from memory.
- No naturally occurring animal disease identified. I did not check OMIA.

---

## 15. Model organisms

- **Mouse:** CRISPR/Cas9 *Cfap43* knockout (and *Cfap44*). Male mice display MMAF; females are fertile. This recapitulates the human phenotype well. [verified, PMID:28552195]
- **Trypanosoma brucei** RNAi/knockout shows flagellar defects and supports evolutionary conservation of the flagellar function. [verified via search summary]
- Additional mouse work on manchette transport and sperm head shaping ([PMID:33046149](https://pubmed.ncbi.nlm.nih.gov/33046149/), title only).
- **Limitations.** Mouse and trypanosome data do not show whether human spermatogenesis proceeds identically. Respiratory and motile-cilia phenotypes are not clearly modeled.
- Resources to check: MGI, IMPC, Alliance of Genome Resources.

---

## Suggested direct quotes (from search-result excerpts; verify against cached abstracts)

- Tang 2017, PMID:28552195: compound-heterozygous mutations in CFAP43 in three subjects and a homozygous frameshift mutation in CFAP44 in one subject. The recessive mutations were parentally inherited from heterozygous carriers and absent in 984 individuals from three Han Chinese control populations. These two lines are paraphrases from the search summary, not exact quotes. Pull exact text with `just fetch-reference PMID:28552195`.

## Gaps and recommended next steps

1. Fetch PMID:28552195 and the Coutton/Auguste paper through `just fetch-reference`, and take exact snippets from those caches.
2. Look up the HGNC, GO, CL, UBERON, HPO and NCIT identifiers with the `dismech-terms` workflow.
3. Check ClinGen for a CFAP43 gene-validity record.
4. Run `just check-genereviews` for a chapter that might serve as a baseline. I did not look for one.
5. Review population frequency, founder variants, respiratory involvement and clinical trials, none of which I covered.

## Sources

- [LOVD disease #05567 (SPGF19, OMIM:617592)](https://databases.lovd.nl/shared/diseases/05567)
- [MalaCards: Spermatogenic Failure 19](https://malacards.org/card/spermatogenic_failure_19)
- [MGI: OMIM:617592](https://informatics.jax.org/disease/OMIM:617592)
- [DrugMap disease DIS2ZB4B](https://drugmap.idrblab.net/data/disease/details/DIS2ZB4B)
- [GlyCosmos DOID:0070170](https://glycosmos.org/diseases/DOID:0070170)
- [Tang et al. 2017, PubMed 28552195](https://pubmed.ncbi.nlm.nih.gov/28552195/)
- [Coutton/Auguste et al., Nat Commun](https://www.nature.com/articles/s41467-017-02792-7)
- [Sha et al. 2018, PubMed 29277146](https://pubmed.ncbi.nlm.nih.gov/29277146/)
- [Sha et al. 2019, Andrologia](https://onlinelibrary.wiley.com/doi/10.1111/and.13151)
- [PubMed 41549427](https://pubmed.ncbi.nlm.nih.gov/41549427/)
- [PubMed search: CFAP43 MMAF](https://pubmed.ncbi.nlm.nih.gov/?term=CFAP43+MMAF)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 9 |
| On topic | 8 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:41341611`: "CFAP43 mutations and familial male infertility with respiratory manifestations"
  - closest text in source: "Additionally, they highlight the potential expansion of the CFAP43 gene's phenotypic spectrum to include respiratory manifestations"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 10 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 6 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0012206` (1 mention) - the report calls it "Asthenozoospermia"; HP calls it **Abnormal sperm motility**
- `HP:0012864` (1 mention) - the report calls it "verify"; HP calls it **Abnormal sperm morphology**
- `HP:0012207` (1 mention) - the report calls it "verify"; HP calls it **Reduced sperm motility**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0004983` (1 mention) - the report calls it "Parent class: spermatogenic failure"; MONDO calls it **spermatogenic failure**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.