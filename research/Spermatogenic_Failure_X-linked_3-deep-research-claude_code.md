---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-16T13:11:56.097691'
end_time: '2026-10-16T13:13:47.243370'
duration_seconds: 111.15
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spermatogenic Failure X-linked 3
  mondo_id: MONDO:0025354
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
  web_search_requests: 4
  num_turns: 8
  total_cost_usd: 0.8895659
  session_id: e0e00ff6-67e7-5e60-9592-3e4cb1004f09
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 8
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 3
  validator_version: 0.3.0
term_validation:
  total_terms: 9
  verified: 8
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 1
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0025354
    reported_labels:
    - MONDO
    ontology_label: spermatogenic failure, X-linked, 3
  - term_id: DOID:0112274
    reported_labels:
    - DOID
    ontology_label: X-linked spermatogenic failure 3
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spermatogenic Failure X-linked 3
- **MONDO ID:** MONDO:0025354 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spermatogenic Failure X-linked 3** covering all of the
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

# Spermatogenic Failure, X-linked, 3 (SPGFX3; CFAP47-related MMAF): Research Report

**Scope and verification.** I verified the core facts below by search or fetch in this session. These are the OMIM, MONDO and DOID identifiers, the gene assignment, and the contents of two primary papers (Liu C 2021, PMID 33472045; Liu M 2023, DOI 10.3389/fendo.2023.1155639).

- Only those two primary papers were read. Other CFAP47 reports exist in the literature, and I did not retrieve them.
- Ontology IDs marked *(unverified)* are from memory. Look them up before binding them; do not copy them into a KB entry as written.
- I did not obtain a PMID for the 2023 Frontiers paper.
- OMIM, Orphanet, ClinVar, gnomAD and GeneReviews pages were not read directly. Claims attributed to them come from search snippets or from the primary papers' own text.
- The `fetch-reference` cache and `just validate-*` were not run, so none of the snippets below has been checked against `references_cache/`.

---

## 1. Disease Information

**Overview.** SPGFX3 is an X-linked recessive cause of male infertility. It is characterized by asthenoteratozoospermia with multiple morphological abnormalities of the sperm flagella (MMAF): flagella that are absent, short, coiled, bent or of irregular caliber. It is caused by hemizygous loss-of-function or missense variants in *CFAP47* at Xp21.1. Affected men are otherwise described as having isolated infertility. Neither paper reports a syndromic extra-reproductive phenotype.

**Identifiers.**

| System | ID | Source |
|---|---|---|
| OMIM | 301059 | [LOVD disease #06940](https://databases.lovd.nl/shared/diseases/06940), [MalaCards](https://www.malacards.org/card/spermatogenic_failure_x_linked_3) |
| MONDO | MONDO:0025354 | [SAIL concept library](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0025354/) |
| DOID | DOID:0112274 | [Disease Ontology](https://disease-ontology.org/term/DOID:0112274) |
| UMLS / MedGen | C5542347 / 1784059 | [MedGen](https://ncbi.nlm.nih.gov/medgen/C5542347) |
| Gene | *CFAP47* (formerly *CXorf59*), Xp21.1, Entrez 286464 | GlyCosmos and LOVD |

- **Synonyms:** SPGFX3; X-linked spermatogenic failure 3.
- **Parent concept (Mondo):** spermatogenic failure, within male infertility.
- **OMIM cross-reference:** SPGF1 (258150) for genetic heterogeneity of spermatogenic failure.
- **Naming discrepancy:** the LOVD entry uses the obsolete symbol *CXorf59*, which is the old name of *CFAP47*.
- **Source level:** the evidence is from individual patients (exome sequencing, semen analysis, sperm electron microscopy). OMIM and MONDO are aggregated disease-level resources built on those reports.
- **Near-namesake caution:** an unofficial dismech-hosted report on SPGFX1/TEX11 exists. Search-result commentary flagged its SPGFX gene mappings as internally inconsistent. Do not take SPGFX2 or SPGFX4 assignments from it. Confirm each against OMIM.

## 2. Etiology

- **Causal factor:** genetic. Hemizygous *CFAP47* variants in males. Reported alleles are missense changes and one whole-gene deletion.
- **Genetic risk factors:** no modifier genes or susceptibility loci have been described in the papers I read.
- **Environmental risk factors, protective factors, gene-environment interactions:** none reported. I would not infer any.
- **Allele caution:** p.V472M (c.1414G>A) is reported at about 0.009 allele frequency in East Asian reference populations, per Liu M 2023. That is high for a fully penetrant X-linked recessive allele, so its pathogenicity rests on functional data, not rarity.

## 3. Phenotypes

All phenotypes are laboratory or sperm-morphology findings in adult males (human clinical evidence). Frequencies are the cohort counts in the primary papers. Four men were reported in 2021 and two in 2023, so no population-level frequency exists.

| Phenotype | Detail | Suggested HPO *(unverified)* |
|---|---|---|
| Male infertility (primary) | All reported men | Male infertility, HP:0003251 |
| Asthenozoospermia | Motility 10–23% (WHO limit 40%) in the 2021 men; 11–21% in the 2023 men | Asthenozoospermia, HP:0012206 |
| Teratozoospermia / MMAF | Absent, short, coiled flagella | Teratozoospermia, HP:0012864 |
| Oligozoospermia (variable) | 0.5–29.5 ×10⁶/mL (2021); 0.9 and 6.0 (2023) | Oligozoospermia, HP:0000798 |
| Abnormal sperm head morphology | Pyriform, round, small heads; small or absent acrosomes (2023 patients) | Look up |
| Abnormal axoneme ultrastructure | Disorganized outer dense fibers; missing peripheral doublets or central pair | Look up |

**2021 morphology by subject** (Liu C 2021, Table 2, as summarized by the fetch):

- T115: absent 37.5%, short 34%, coiled 18.5%.
- T176: absent 11%, short 17%, coiled 42%.
- H025: absent 22%, short 14%, coiled 50.5%.

**Onset, progression, quality of life.** Not reported. Presentation is in adulthood, as couple infertility. Nothing is known about progression or quality of life. Semen findings are presumably stable, but that is an inference.

**Hormones and testis.** The 2021 paper reports no FSH, LH, testosterone or testicular histology data. I would leave endocrine phenotypes uncurated.

## 4. Genetic/Molecular Information

- **Gene:** *CFAP47* (cilia- and flagella-associated protein 47). A very large X-linked gene highly expressed in testis.
- **Variants reported:**

| Variant | Type | Reference |
|---|---|---|
| c.7154T>A, p.Ile2385Asn | missense | Liu C 2021 |
| c.5224A>G, p.Ser1742Gly | missense | Liu C 2021 |
| c.8668C>A, p.Pro2890Thr | missense | Liu C 2021 |
| ~3.2 Mb Xp21.1 deletion removing all of *CFAP47* | deletion | Liu C 2021 (Australian man MA2603) |
| c.1414G>A, p.Val472Met | missense | Liu M 2023, two unrelated patients |

- **Screening yield (2021):** 243 men with MMAF (CITIC-Xiangya, Changsha) and 88 (Anhui Medical University), plus 24 Australian men with asthenoteratozoospermia. These yielded three missense carriers and the one deletion. The fetch did not give the exact per-cohort breakdown.
- **Origin:** germline, hemizygous in males.
- **Functional consequence:** CFAP47 protein is strongly reduced in patient sperm. Loss of function, or reduced function from missense variants, is the working model. I would not claim dominant negative or gain of function.
- **Modifier genes, epigenetics, chromosomal abnormalities:** none described, apart from the Xp21.1 deletion.
- **ClinGen / validity:** a search snippet showed a disease database linking CFAP47 to this MONDO term at only "limited" evidence. I did not find a ClinGen `CGGV:` record. If you record gene-disease validity, copy it from a source record. Do not assign it.

## 5. Environmental Information

None reported. No toxins, lifestyle factors or infectious agents are implicated.

## 6. Mechanism / Pathophysiology

**Causal chain.**

1. A hemizygous *CFAP47* variant (missense or deletion) arises in a male. Males have no second X allele to compensate (demonstrated genetically).
2. This leads to markedly reduced CFAP47 protein in sperm. Immunofluorescence shows the signal almost absent at the flagellar base (demonstrated for the 2021 men; Western blot reduction in the 2023 patients).
3. This is associated with reduced or mislocalized partner proteins. CFAP65 is mislocalized in mutant sperm and co-immunoprecipitates with CFAP47. CFAP69, SEPTIN4 and CFAP65 are reduced in the 2023 patients. These expression and localization changes are correlative. Whether CFAP47 regulates them, or is only co-lost with them, is **inferred, not demonstrated**.
4. This leads to defective axonemal and peri-axonemal assembly. TEM shows disorganized outer dense fibers and missing peripheral doublets or central pair. SPAG16 is reduced. The 2023 patients also show a defective annulus and a disorganized mitochondrial sheath.
5. This results in absent, short, coiled or bent flagella and impaired motility (MMAF, asthenoteratozoospermia).
6. This results in male infertility. Branch (2023 patients): abnormal head morphology and small or absent acrosomes. How a flagellar protein loss produces head defects is not explained and is not established.

**Mouse timing.** In the *Cfap47* mutant mouse, flagellar bending was first seen in the corpus epididymis, not the testis. That suggests a late structural defect, but this is one study.

**Cell types and processes.**

- Cell types: spermatid and spermatozoon, with Sertoli-cell context.
- Suggested terms *(unverified)*: spermatozoon (CL), spermatid (CL); GO terms for sperm flagellum assembly and axoneme assembly.

**Omics, single-cell, CRISPR screens, immune or metabolic involvement.** Not reported.

## 7. Anatomical Structures Affected

- **Organs:** testis and the male reproductive tract (UBERON testis, epididymis *(unverified)*).
- **Cells:** developing and mature sperm.
- **Subcellular:** sperm flagellum, axoneme, outer dense fibers, fibrous sheath, annulus, mitochondrial sheath, flagellar base (GO cellular component terms to be looked up).
- **Lateralization:** not applicable.

## 8. Temporal Development

- **Onset:** presumably congenital. It is clinically ascertained in adulthood by infertility.
- **Course:** lifelong. Spontaneous remission is not reported.
- **Critical period:** none identified.

## 9. Inheritance and Population

- **Inheritance:** X-linked recessive (HPO "X-linked recessive inheritance" *(verify ID)*). Males are affected, with hemizygous variants.
- **Carrier females:** no phenotype is reported in the sources I read.
- **Penetrance and expressivity:** semen parameters vary (concentration 0.5–29.5 ×10⁶/mL), but all reported men are infertile. I would not state a formal penetrance.
- **Prevalence:** not documented. This is a very rare, recently described condition. Do not assign a prevalence class beyond "not yet documented" without a source.
- **Populations:** reported cases are mostly Chinese, plus one Australian man. Founder effects, anticipation and mosaicism are not described.
- **Sex ratio:** affects males only.

## 10. Diagnostics

- **Semen analysis** shows asthenozoospermia or oligoasthenoteratozoospermia, with a high proportion of absent, short, coiled or irregular-caliber flagella.
- **Sperm TEM:** disorganized axoneme and outer dense fibers.
- **Immunofluorescence** of sperm for CFAP47 (and CFAP65, SPAG16) is a research tool, not a clinical test.
- **Genetic testing:** exome sequencing or an MMAF gene panel including *CFAP47*. Use chromosomal microarray or CNV analysis for deletions, because the whole-gene deletion was found that way.
- **Differential diagnosis:** other MMAF genes (for example *DNAH1*, *CFAP43*, *CFAP44*, *CFAP69*) and primary ciliary dyskinesia. I did not retrieve sources for these; confirm in the literature before curating.
- **Screening:** none established.

## 11. Outcome/Prognosis

No mortality or morbidity beyond infertility is reported. Reproductive prognosis with assisted reproduction (ICSI) appears favorable in the 2021 cohort and was mixed in the 2023 patients (see Treatment).

## 12. Treatment

**No curative therapy exists.** Sperm from these men is usable for ICSI.

NCIT terms to use, from your CLAUDE.md list:

- Assisted reproduction: bind the closest action term, or leave `term:` empty. NCIT:C15329 (Surgical Procedure) is not right for ICSI. Search NCIT for ICSI directly.
- Genetic counseling: NCIT:C15240.

**ICSI outcomes, Liu C 2021 (Table 3):**

| Subject | Oocytes injected | Fertilized | Blastocysts | Outcome |
|---|---|---|---|---|
| T115 | 1 | 0 | – | No pregnancy; partner aged 41 |
| T176 | 9 | 8 (89%) | 5 (63%) | Clinical pregnancy |
| H025 | 11 | 9 (82%) | 7 (78%) | Clinical pregnancy |
| MA2603 | 12 | 10 (83%) | 3 (30%) | Clinical pregnancy; one miscarriage |

Three of four couples achieved clinical pregnancy.

**ICSI outcomes, Liu M 2023:** no pregnancies in the cycles reported.

- Patient A: 3/5 fertilized, one 8-cell embryo transferred, no pregnancy.
- Patient B: first cycle 1/4 fertilized, second cycle 2/3 fertilized, embryos failed to develop.
- The authors attribute the failures possibly to female factors.

**Reconciliation.** Pooling both papers, ICSI achieved fertilization in most cycles but pregnancy in three of six couples. The small numbers and female-factor confounders mean this is not a success rate.

**Experimental treatments:** no NCT trials identified. I did not search ClinicalTrials.gov.

## 13. Prevention

- **Genetic counseling:** a carrier mother passes the variant to half of her sons. Daughters of an affected man are obligate carriers. This is standard X-linked reasoning, not drawn from the papers.
- **Prenatal and preimplantation testing:** possible once the family variant is known. Not discussed in the sources I read.
- **Primary prevention:** none.

## 14. Other Species / Natural Disease

I did not search OMIA, so I cannot confirm a naturally occurring animal disease. Treat this section as not assessed.

## 15. Model Organisms

**Mouse (Liu C 2021).** A *Cfap47* frameshift allele, c.2559insT (p.Gly855Profs*8), made hemizygous in males.

- **Fertility:** males were sterile over 3 months of breeding.
- **Sperm:** reduced total and progressive motility, abnormal "folding" movement, lower VCL, VSL and VAP. Sperm concentration was not significantly different.
- **Morphology:** bent flagella, first seen in the corpus epididymis, and unevenly distributed fibrous sheaths on TEM.
- **IVF:** lower two-cell and blastocyst rates. **ICSI:** rates comparable to wild type.
- **Localization:** Cfap47 signal is mainly in the midpiece in mouse sperm. In human control sperm it is at the flagellar base, which is a species difference.
- **Fidelity:** the mouse recapitulates infertility, asthenozoospermia and flagellar abnormalities. It differs from humans in having normal sperm concentration and, apparently, a milder morphology (bent flagella versus the human absent, short and coiled mix).
- **Suggested links:** `modeled_mechanisms` with `PARTIALLY_RECAPITULATES` against a flagellar-assembly node; `evidence_source: MODEL_ORGANISM`.
- **Resources:** IMPC and MGI entries exist (the search surfaced an MGI:3605549 phenotype page). I did not check them.

---

## Evidence and snippet candidates

Quotes below come from the fetch's paraphrase and summaries, not from verified abstract text. Re-copy exact snippets from `references_cache` after `just fetch-reference PMID:33472045`.

| Claim | Reference | Evidence source |
|---|---|---|
| Hemizygous CFAP47 variants cause X-linked MMAF and asthenoteratozoospermia | PMID:33472045 | HUMAN_CLINICAL |
| ICSI restores fertility in the mouse and in 3 of 4 men | PMID:33472045 | MODEL_ORGANISM (mouse); HUMAN_CLINICAL (men). Split these into separate items |
| p.V472M in two patients; CFAP47 binds CFAP69 and SEPTIN4 | DOI:10.3389/fendo.2023.1155639 (PMID not found) | HUMAN_CLINICAL (variant); IN_VITRO or ex vivo (co-IP in human testis) |

## Gaps and recommendations

1. Look up the PMID for Liu M 2023 and read any other CFAP47 papers (cohort studies, follow-ups) before finalizing prevalence, yield and variant spectrum.
2. Check OMIM 301059, GeneReviews and Orphanet directly.
3. Search NCIT for an ICSI term. Do not guess a CURIE.
4. Verify every HPO, GO, CL and UBERON term listed above with `runoak` or the term caches.
5. Check ClinGen for a CFAP47 validity record before filling `gene_disease_validity`.

Sources:
- [LOVD SPGFX3 disease #06940](https://databases.lovd.nl/shared/diseases/06940)
- [MalaCards SPGFX3](https://www.malacards.org/card/spermatogenic_failure_x_linked_3)
- [Disease Ontology DOID:0112274](https://disease-ontology.org/term/DOID:0112274)
- [MedGen C5542347](https://ncbi.nlm.nih.gov/medgen/C5542347)
- [MONDO:0025354 record](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0025354/)
- [Liu C et al., Am J Hum Genet 2021 (PMC7895902)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7895902)
- [Liu M et al., Front Endocrinol 2023](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2023.1155639/full)
- [The X chromosome and male infertility (PMC7864851)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7864851/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 9 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 3 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0025354` (5 mentions) - the report calls it "MONDO"; MONDO calls it **spermatogenic failure, X-linked, 3**
- `DOID:0112274` (5 mentions) - the report calls it "DOID"; DOID calls it **X-linked spermatogenic failure 3**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.