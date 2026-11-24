---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-23T12:21:47.482513'
end_time: '2026-11-23T12:27:03.895301'
duration_seconds: 316.41
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: MORM Syndrome
  mondo_id: MONDO:0012423
  category: Mendelian
  causal_genes: INPP5E
  omim_id: OMIM:610156
  synonyms: intellectual disability-truncal obesity-retinal dystrophy-micropenis syndrome;
    mental retardation, truncal obesity, retinal dystrophy, and micropenis; mental
    retardation-truncal obesity-retinal dystrophy-micropenis syndrome
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
  web_search_requests: 6
  num_turns: 13
  total_cost_usd: 0.9393230149999998
  session_id: 96709c3e-efc8-42e1-82ef-d2781a058b43
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 27
  retrieval_calls: 25
  assistant_text_blocks: 4
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 16
reference_validation:
  total_references: 32
  verified: 32
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 4
  quotes_valid: 2
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:16493448
  - PMID:19668215
  quotes_not_checkable: 1
  relevance_assessed: 32
  on_topic: 24
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 40
  verified: 38
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 0
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: HP:0100259
    reported_labels:
    - absent
    ontology_label: Postaxial polydactyly
  - term_id: HP:0000252
    reported_labels:
    - absent
    ontology_label: Microcephaly
  - term_id: UBERON:0000955
    reported_labels:
    - cognitive involvement
    ontology_label: brain
  - term_id: NCBITaxon:10090
    reported_labels:
    - Inpp5e
    - mouse *Inpp5e
    ontology_label: Mus musculus
  - term_id: NCBITaxon:7955
    reported_labels:
    - inpp5e
    - zebrafish *inpp5e
    ontology_label: Danio rerio
  labels_variant: 1
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MORM Syndrome
- **MONDO ID:** MONDO:0012423 (if available)
- **Causal gene(s):** INPP5E
- **OMIM:** OMIM:610156
- **Synonyms:** intellectual disability-truncal obesity-retinal dystrophy-micropenis syndrome; mental retardation, truncal obesity, retinal dystrophy, and micropenis; mental retardation-truncal obesity-retinal dystrophy-micropenis syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **MORM Syndrome** covering all of the
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

I'm collecting the abstracts for the key MORM and INPP5E papers so I can quote them exactly.

I can't give you the full abstracts verbatim. The efetch source is non-preapproved, so my reporting rules cap quotes at 125 characters and require paraphrase for the rest. The metadata and abstract summaries below come from the efetch output, which was not truncated. For the exact abstract text, fetch the efetch URL directly.

Efetch URLs read:
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=16826528,19668215,19668216,34211432,34188062,41465079,38806661,33711342,39871753&rettype=abstract&retmode=text
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42374981,26190144,26190145,23386033,26748598,29052317,31173343,42838451&rettype=abstract&retmode=text

**Two PMIDs are not what you expected**
- **16826528** is Kleefstra T et al., Am J Hum Genet 2006. Title: "Loss-of-function mutations in euchromatin histone methyl transferase 1 (EHMT1) cause the 9q34 subtelomeric deletion syndrome." It is not about INPP5E. It is in the PMID list only because it was returned by the earlier pages.
- **26190145** is Brown AC et al., Dev Cell 2015. Title: "A synthetic niche for nephron progenitor cells." It is unrelated to INPP5E.

**Records (PMID | title | first author | journal, year | abstract summary, paraphrased)**

1. **16826528** | EHMT1 loss-of-function, 9q34 deletion syndrome | Kleefstra T | Am J Hum Genet, 2006. Screened 23 patients; found two de novo EHMT1 mutations, supporting haploinsufficiency as the cause.
2. **19668215** | INPP5E mutations cause primary cilium signaling defects, ciliary instability and ciliopathies in human and mouse | Jacoby M | Nat Genet, 2009. Inpp5e-deficient mice develop cilia defects; loss of INPP5E destabilizes cilia via PI3K and PDGFRα signaling. A MORM family mutation impairs ciliary localization.
3. **19668216** | Mutations in INPP5E, encoding inositol polyphosphate-5-phosphatase E, link phosphatidyl inositol signaling to the ciliopathies | Bielas SL | Nat Genet, 2009. INPP5E mutations in JBTS1-linked Joubert disease cluster in the phosphatase domain, impair its activity, and destabilize cilia.
4. **34211432** | Novel Insights Into Monogenic Obesity Syndrome Due to INPP5E Gene Variant: A Case Report of a Female Patient | Drole Torkar A | Front Endocrinol, 2021. A girl with a homozygous truncating INPP5E variant had early severe obesity, progressive cone-rod dystrophy and metabolic complications.
5. **34188062** | Broadening INPP5E phenotypic spectrum: detection of rare variants in syndromic and non-syndromic IRD | Sangermano R | NPJ Genom Med, 2021. 16 non-syndromic IRD patients from 10 families with biallelic INPP5E variants; 14 variants, 12 new; no clear genotype-phenotype correlation.
6. **41465079** | Longitudinal Multimodal Assessment of Structure and Function in INPP5E-Related Retinopathy | Cusumano A | Genes (Basel), 2025. Six-year follow-up of one patient showed progressive loss of ellipsoid zone width, inner nuclear layer thinning and falling cone flicker ERG amplitudes.
7. **38806661** | Utilization of automated cilia analysis to characterize novel INPP5E variants in patients with non-syndromic retinitis pigmentosa | Whiting KR | Eur J Hum Genet, 2024. Two patients with non-syndromic RP carried novel INPP5E variants; patient fibroblasts had shorter cilia and lost INPP5E localization.
8. **33711342** | Deletion of the phosphatase INPP5E in the murine retina impairs photoreceptor axoneme formation and prevents disc morphogenesis | Sharif AS | J Biol Chem, 2021. Retina-specific knockout mice had rapid rod-cone degeneration, with no axoneme or disc formation and suspected disrupted intraflagellar transport.
9. **39871753** | Inpp5e is crucial for photoreceptor outer segment maintenance | Gupta M | J Cell Sci, 2025. Conditional and inducible Inpp5e knockouts caused outer segment shortening, Golgi abnormalities, and photoreceptor loss.
10. **42374981** | Loss of INPP5E affects photoreceptor outer segment membrane biogenesis in iPSC-derived human retinal organoids | Whiting KR | J Cell Sci, 2026. INPP5E knockout retinal organoids showed altered ARL13B and rhodopsin localization and elongated outer segment membranes.
11. **26190144** | Modulation of Ciliary Phosphoinositide Content Regulates Trafficking and Sonic Hedgehog Signaling Output | Chávez M | Dev Cell, 2015. INPP5E loss raised ciliary PI(4,5)P2 and recruited TULP3/Gpr161, increasing cAMP and repressing Shh target Gli1.
12. **26190145** | A synthetic niche for nephron progenitor cells | Brown AC | Dev Cell, 2015. An in vitro culture niche that expands nephron progenitor cells from embryonic kidney or stem cells. Not related to INPP5E.
13. **23386033** | Phenotypic spectrum and prevalence of INPP5E mutations in Joubert syndrome and related disorders | Travaglini L | Eur J Hum Genet, 2013. INPP5E was screened in 483 probands; 12 mutations were found in 17 probands from 11 JSRD families. None were found in MKS fetuses.
14. **26748598** | Role of reverse phenotyping in interpretation of next generation sequencing data and a review of INPP5E related disorders | de Goede C | Eur J Paediatr Neurol, 2016. A family first attributed to a RABL6 variant was shown to carry a homozygous INPP5E mutation; the paper also reviews the INPP5E phenotypic spectrum.
15. **29052317** | Defective ciliogenesis in INPP5E-related Joubert syndrome | Hardee I | Am J Med Genet A, 2017. Two sisters with a novel homozygous INPP5E variant had Joubert features; patient fibroblasts had shorter or absent cilia.
16. **31173343** | BBS5 and INPP5E mutations associated with ciliopathy disorders in families from Pakistan | Khan S | Ann Hum Genet, 2019. Two Pakistani families: a BBS5 frameshift in one and an INPP5E nonsense variant in the other, suggesting a regional founder mutation.
17. **42838451** | Cell-type-specific repression reveals MC4R neurons as a site of action for ciliary obesity genes | Diener Blake A | Mol Metab, 2026. CRISPRi repression of Adcy3 or of ciliopathy genes Bbs10, Inpp5e and Ankrd26 in MC4R neurons was sufficient to promote obesity.

All four items are done, but two of them rest mainly on model summaries rather than verbatim text, and one URL is not the paper the coordinator named.

**1. PMID 16493448: confirmed as the Hampshire MORM paper**
- Title: "MORM syndrome (mental retardation, truncal obesity, retinal dystrophy and micropenis), a new autosomal recessive disorder, links to 9q34."
- Authors: Hampshire DJ, Ayub M, Springell K, Roberts E, Jafri H, Rashid Y, Bond J, Riley JH, Woods CG (last author Woods CG).
- Journal: Eur J Hum Genet. 2006 May;14(5):543-8. DOI 10.1038/sj.ejhg.5201577.
- Summary of the abstract (paraphrase): a consanguineous pedigree with 14 affected people had static moderate intellectual disability, truncal obesity, a congenital nonprogressive retinal dystrophy, and micropenis in males. Linkage to the BBS1-8 and Cohen loci was excluded. Autozygosity mapping found one homozygous subtelomeric region on 9q34.3.
- Short verbatim quotes from the abstract:
  - "A consanguineous pedigree is described where 14 individuals are affected with a novel autosomal recessive disorder"
  - "with a maximum LOD score of 5.64"
  - "It shows similarities to Bardet-Biedl syndrome and Cohen syndrome, but can be distinguished by clinical features"
- The distinguishing features the abstract lists include the age of onset and nonprogressive visual impairment, the lack of characteristic facies, microcephaly, "mottled retina", polydactyly, and small penis without testicular anomalies.

**2. OMIM #610156 (MORMS): mostly model-summarized**
- The URL is a third-party mirror (git.lsit.ucsb.edu), not omim.org. The verbatim part I could read was page boilerplate. The entry content (about 76,600 characters) came only as a model-extracted summary, so the details below are unverified.
- Title and MIM: "Impaired intellectual development, truncal obesity, retinal dystrophy, and micropenis syndrome; MORMS", #610156. Inheritance is autosomal recessive. Gene INPP5E (MIM 613037), 9q34.3. Phenotype mapping key 3.
- Clinical features per the summary:
  - Visual: congenital nonprogressive retinal dystrophy, reduced acuity by age 3, cataracts in the second or third decade.
  - ERG: not reported.
  - Obesity: truncal, apparent in childhood.
  - Intelligence: moderate intellectual disability apparent by age 4, with delayed language.
  - Genital: micropenis in males.
  - Seizures: not reported.
  - Other: the summary says the family was Pakistani, which the abstract does not state.
- Mapping per the summary: linkage locus of about 1 cM with maximum LOD 5.64, between markers D9S158 and D9S905.
- Molecular genetics per the summary: Jacoby et al. (2009) found a homozygous nonsense mutation, Q627X (613037.0001), in INPP5E. The mutant protein did not localize properly to cilia.
- References per the summary: PMID 16493448 (Hampshire 2006) and PMID 19668215 (Jacoby 2009).

**3. PMC2746682 is Bielas et al. 2009, not Jacoby**
- The PMC article corresponds to PMID 19668216: "Mutations in the inositol polyphosphate-5-phosphatase E gene link phosphatidyl inositol signaling to the ciliopathies." First author Stephanie L Bielas, last author Joseph G Gleeson, Nat Genet 2009 Aug 9;41(9):1032-1036. The PMC version is the author manuscript (NIHMS130662).
- The Jacoby 2009 paper is PMID 19668215, which is a different article.
- Abstract quotes from the PMC version (this wording differs from the PubMed abstract):
  - "Mutations clustered in the phosphatase domain and impaired 5-phosphatase activity"
  - "mutations promoted premature destabilization of cilia in response to stimulation"
- Mechanism: the text I read covers PDGF and Akt, with the quote "Because overexpression of INPP5E was previously shown to block Akt phosphorylation in response to PDGF stimulation". CAAX is not in the text I read.
- The MORM family, Q627X, and mouse knockout phenotypes (anophthalmia, renal cysts, polydactyly, skeletal, brain, embryonic lethality) were not found in the text I read. The remaining 30,500 characters were summarized, and that summary said they were absent. I did not verify that.

**4. ClinVar: INPP5E[gene] AND MORM**
- esearch: Count 128, RetMax 100, so 28 records were not retrieved. I fetched esummary for the first 100 IDs.
- Records read verbatim (variant | classification | conditions):
  - 5007418 | NM_019892.6(INPP5E):c.657C>A (p.Tyr219Ter) | Likely pathogenic | MORM syndrome; Joubert syndrome 1
  - 3891390 | c.373G>A (p.Ala125Thr) | Uncertain significance | Joubert syndrome 1; MORM syndrome
  - 3891389 | c.1636A>G (p.Thr546Ala) | Uncertain significance | Joubert syndrome 1; MORM syndrome
  - 3651068 | c.1282G>A (p.Gly428Ser) | Uncertain significance (multiple submitters) | MORM syndrome; Joubert syndrome
  - 3596803 | c.29C>T (p.Pro10Leu) | Uncertain significance | Joubert syndrome 1; MORM syndrome
  - 3596802 | c.66dup (p.Leu23fs) | Likely pathogenic | Joubert syndrome 1; MORM syndrome
  - 3596800 | c.109G>A (p.Gly37Arg) | Uncertain significance | Joubert syndrome 1; MORM syndrome
  - 3596799 | c.177del (p.Ser59fs) | Likely pathogenic | Joubert syndrome 1; MORM syndrome
  - 3596798 | c.208_214dup (p.Pro72fs) | Likely pathogenic (multiple submitters) | Joubert syndrome 1; MORM syndrome; INPP5E-related disorder
- The remaining records (3596797 through 3596772) came only as a model summary. Those were 22 records, and the summary lists classifications and conditions, including Likely pathogenic for c.367_368delinsA (p.Ala123fs), c.1432_1433del (p.Phe478fs) and c.1483C>T (p.Gln495Ter). The rest were Uncertain significance.
- Most records list MORM syndrome as a condition alongside Joubert syndrome 1. Reading the verbatim portion, 9 records are shown; the other 91 were not read.

**Limits**
- Item 2 (OMIM) and the rest of item 4 (ClinVar) rest on model summaries; the verbatim parts I could read did not cover those details.
- Items 1 and 4's verbatim records come from the NCBI pages directly. Item 3's verbatim abstract comes from the PMC page.

Final URLs read:
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=16493448
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=16493448&rettype=abstract&retmode=text
- https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/610156
- https://pmc.ncbi.nlm.nih.gov/articles/PMC2746682
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=clinvar&term=INPP5E[gene]+AND+MORM&retmax=100
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=clinvar (IDs from that esearch, first 100)

**Scope note:** This report covers MORM syndrome (MONDO:0012423; OMIM #610156). It is the autosomal recessive ciliopathy caused by biallelic variants in **INPP5E** (inositol polyphosphate-5-phosphatase E; OMIM *613037; chromosome 9q34.3). I could not open the PubMed article pages (they returned a cookie wall), so the abstracts were read through NCBI E-utilities. Quotes were kept short because of the fetch limits. All quotes marked "verbatim" were retrieved in this session. The OMIM text came from a third-party mirror and was available only as a model-made summary, so I flag those details as unverified. There is little MORM-specific literature: one original family, plus a few later case reports and studies of the broader INPP5E phenotype spectrum.

---

## 1. Disease Information

**Overview.** MORM syndrome was first described in 2006 in one consanguineous family with 14 affected members. The authors called it "a novel autosomal recessive disorder" with "static moderate mental retardation, truncal obesity, a congenital non-progressive retinal dystrophy and micropenis in males" (Hampshire et al., *Eur J Hum Genet* 2006;14(5):543-8, **PMID 16493448**, DOI 10.1038/sj.ejhg.5201577; [Nature](https://www.nature.com/articles/5201577), [Durham repository](https://durham-repository.worktribe.com/output/1507503/morm-syndrome-mental-retardation-truncal-obesity-retinal-dystrophy-and-micropenis-a-new-autosomal-recessive-disorder-links-to-9q34)). It overlaps clinically with Bardet–Biedl syndrome (BBS) and Cohen syndrome. Jacoby et al. 2009 (**PMID 19668215**) later identified a homozygous nonsense variant in INPP5E as the cause, which places MORM among the ciliopathies.

**Identifiers**

| Resource | ID |
|---|---|
| MONDO | MONDO:0012423 |
| OMIM (phenotype) | #610156, "Impaired intellectual development, truncal obesity, retinal dystrophy, and micropenis syndrome; MORMS" ([OMIM mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/610156)) |
| OMIM (gene) | *613037 INPP5E ([mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/613037)) |
| Orphanet | ORPHA:75858 ([GARD record](https://rarediseases.info.nih.gov/assets/singles/10121.json)) |
| GARD | 10121 (same source) |
| KEGG Disease | H02899 ([KEGG](https://www.kegg.jp/entry/H02899)) |
| ICD-10 / ICD-11 / MeSH | No disease-specific code found. It probably falls under general codes for congenital malformation syndromes or ciliopathies; not verified. |

**Synonyms:** MORMS; mental retardation, truncal obesity, retinal dystrophy, and micropenis; intellectual disability–truncal obesity–retinal dystrophy–micropenis syndrome; impaired intellectual development, truncal obesity, retinal dystrophy, and micropenis syndrome (current OMIM title).

**Source type:** The information comes from aggregated, disease-level resources (OMIM, Orphanet) built on a handful of family and case reports. No EHR-based or registry data exist.

## 2. Etiology

- **Causal factor:** The disease is genetic and autosomal recessive. It is caused by biallelic loss-of-function variants in INPP5E. The founding variant is c.1879C>T, p.(Gln627Ter) (Q627X; OMIM 613037.0001), homozygous in the original family (Jacoby 2009, PMID 19668215; OMIM mirror).
- **Genetic risk factors:**
  - Parental consanguinity: the index family was consanguineous (PMID 16493448).
  - Possible regional founder alleles: an INPP5E nonsense variant was reported in a Pakistani ciliopathy family, and the authors suggested a regional founder mutation (Khan et al., *Ann Hum Genet* 2019, **PMID 31173343**).
  - No GWAS susceptibility loci or modifier genes are established.
- **Environmental risk factors:** None known. Not applicable for a monogenic disorder.
- **Protective factors:** None reported, genetic or environmental.
- **Gene–environment interactions:** None documented. In principle, diet and activity could change how severe the obesity becomes, but there is no MORM-specific evidence.

## 3. Phenotypes

The frequencies below come from the single original family (n=14) unless stated otherwise. Later INPP5E patients with a MORM-like picture show that the features vary.

| Phenotype | Suggested HPO term | Onset / course | Frequency | Evidence |
|---|---|---|---|---|
| Intellectual disability, moderate, static | HP:0002342 Intellectual disability, moderate | Childhood (by age ~4 per OMIM summary, unverified); non-progressive | 14/14 (core feature) | PMID 16493448 |
| Delayed speech/language | HP:0000750 Delayed speech and language development | Childhood | Reported (Orphanet/GARD text, OMIM summary) | GARD; OMIM |
| Truncal obesity | HP:0001956 Truncal obesity | Childhood | Core feature | PMID 16493448 |
| Retinal dystrophy, congenital, non-progressive | HP:0000556 Retinal dystrophy; HP:0003577 Congenital onset; HP:0003680 Nonprogressive | Congenital; reduced acuity by about age 3 (OMIM summary, unverified) | Core feature | PMID 16493448 |
| Reduced visual acuity | HP:0007663 Reduced visual acuity | Early childhood | Common | OMIM summary |
| Cataract | HP:0000518 Cataract | 2nd–3rd decade (OMIM summary, unverified) | Some individuals | OMIM summary |
| Micropenis (males) | HP:0000054 Micropenis | Congenital | Affected males; no testicular anomalies | PMID 16493448 |
| Cone-rod dystrophy (progressive) in a MORM-like female | HP:0000548 Cone/cone-rod dystrophy | Childhood; progressive | Single case | Drole Torkar et al. 2021, **PMID 34211432** |
| Severe early-onset obesity with metabolic complications | HP:0001513 Obesity; HP:0000855 Insulin resistance (suggested) | Early childhood | Single case | PMID 34211432 |

**Negative findings that help separate MORM from BBS and Cohen syndrome.** The Hampshire abstract (verbatim) says it "shows similarities to Bardet-Biedl syndrome and Cohen syndrome, but can be distinguished by clinical features". The distinguishing features it lists are:
- age of onset and non-progressive visual impairment;
- no characteristic facies;
- no microcephaly;
- no "mottled retina";
- no polydactyly;
- small penis without testicular anomalies.

HPO terms for these exclusions: Postaxial polydactyly HP:0100259 (absent); Microcephaly HP:0000252 (absent).

**Course of the retinal disease.** The original family had non-progressive retinal disease. Later INPP5E patients with retinopathy, syndromic or non-syndromic, often show progression:
- A six-year follow-up of one patient found progressive loss of ellipsoid-zone width, thinning of the inner nuclear layer, and declining cone flicker ERG amplitudes (Cusumano et al., *Genes* 2025, **PMID 41465079**).
- Sangermano et al. reported 16 patients with non-syndromic inherited retinal disease (IRD) from 10 families with biallelic INPP5E variants. There was no clear genotype–phenotype correlation (*NPJ Genom Med* 2021, **PMID 34188062**).

**Quality of life.** No formal QoL data (EQ-5D, SF-36) were found. The expected main burdens are intellectual disability, which limits independence, and visual impairment. Obesity adds a cardiometabolic burden.

## 4. Genetic / Molecular Information

- **Gene:** INPP5E (HGNC:21474, as I recall; not retrieved this session, so verify), 9q34.3, OMIM *613037. It encodes a 72-kDa inositol polyphosphate 5-phosphatase that localizes to the primary cilium.
- **Founding variant:** NM_019892 c.1879C>T, p.Gln627Ter, in the last exon. Because it sits in the last exon, it is expected to escape nonsense-mediated decay and produce a truncated protein. The truncated protein lacks the C-terminal CaaX box, whose farnesylation tethers INPP5E to membranes ([OMIM 613037 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/613037); PMC3946372). In vitro, the mutant protein "had impaired localization in cilia and was unable to stabilize ciliary structures" (OMIM summary of PMID 19668215).
- **Variant classes:** nonsense, frameshift, and missense.
  - Joubert-associated missense variants "clustered in the phosphatase domain and impaired 5-phosphatase activity" (verbatim; Bielas et al. 2009, **PMID 19668216**).
  - The MORM variant instead leaves the catalytic domain intact and removes the ciliary-targeting C-terminus.
- **ClinVar** (query "INPP5E[gene] AND MORM", 128 records; 9 read verbatim). Most records list the conditions "MORM syndrome; Joubert syndrome 1". Examples:
  - c.657C>A p.(Tyr219Ter): Likely pathogenic
  - c.66dup p.(Leu23fs): Likely pathogenic
  - c.177del p.(Ser59fs): Likely pathogenic
  - c.208_214dup p.(Pro72fs): Likely pathogenic (multiple submitters)
  - c.1282G>A p.(Gly428Ser): VUS
  - several other missense variants: VUS
- **Allele frequency:** gnomAD data for Q627X were not retrieved. The variant is presumed very rare.
- **Origin:** germline.
- **Functional consequence:** loss of function (mislocalization and loss of ciliary function). No gain-of-function or dominant-negative effect has been shown.
- **Allelic disorders:** Joubert syndrome 1 (OMIM 213300) and non-syndromic retinitis pigmentosa / IRD (PMIDs 34188062, 38806661).
- **Modifier genes, epigenetics, chromosomal abnormalities:** none reported. Note that the separate 9q34 subtelomeric deletion syndrome is caused by EHMT1 haploinsufficiency (Kleefstra 2006, PMID 16826528). It is a different disorder and should not be confused with MORM.

## 5. Environmental Information

There are no known environmental, lifestyle, or infectious causes. Diet and physical activity probably affect how severe the obesity becomes, but this is inferred and has not been studied.

## 6. Mechanism / Pathophysiology

**Causal chain** (inferred steps are marked):

1. Biallelic INPP5E loss-of-function variants (for example, Q627X removing the CaaX box) **lead to** failure of INPP5E to localize to, or act in, the primary cilium (PMID 19668215; ciliary-targeting signals described in eLife 2022, PMID 36063381).
2. Loss of ciliary 5-phosphatase activity **results in** a build-up of the phosphoinositides PI(4,5)P2 and PI(3,4,5)P3 in the ciliary membrane (Chávez et al., *Dev Cell* 2015, **PMID 26190144**; Garcia-Gonzalo et al. 2015).
3. Higher ciliary PI(4,5)P2 **recruits** TULP3 and the GPCR Gpr161 into the cilium. This **raises** cAMP and **represses** Sonic Hedgehog output (lower Gli1) (PMID 26190144).
   - **3a (cilium-stability branch):** Unopposed PI3K/PDGFRα–Akt signaling **leads to** destabilization of the primary cilium. Bielas: mutations "promoted premature destabilization of cilia in response to stimulation" (verbatim, PMID 19668216); Jacoby (PMID 19668215). INPP5E also interacts with AURKA (PMID 25395580).
   - **3b (transition-zone branch):** Altered phosphoinositides **disrupt** transition-zone function and ciliary protein trafficking (PMID 27998989; PMID 27927754).
4. Retina: in photoreceptor connecting cilia, INPP5E loss **impairs** axoneme formation, disc morphogenesis, and outer-segment maintenance. This **leads to** photoreceptor dysfunction and degeneration, which presents as retinal dystrophy (mouse: Sharif et al. 2021, **PMID 33711342**, and Gupta et al. 2025, **PMID 39871753**; human iPSC retinal organoids: **PMID 42374981**). Mouse models degenerate rapidly, whereas the original MORM retinopathy was non-progressive. Why this differs is unexplained.
5. Hypothalamus (**inferred for MORM**): ciliary dysfunction in MC4R-expressing neurons **impairs** melanocortin and satiety signaling, which **leads to** hyperphagia and truncal obesity. Supporting evidence: CRISPRi repression of Inpp5e in MC4R neurons was sufficient to promote obesity in mice (Diener Blake et al., *Mol Metab* 2026, **PMID 42838451**).
6. Brain and gonadal axis (**inferred**): ciliary signaling defects during neurodevelopment **lead to** intellectual disability. Ciliary defects affecting the hypothalamic–pituitary–gonadal axis, or Hh-dependent genital development, are a plausible route to micropenis. Neither has been shown directly in MORM.

**Pathways:** primary-cilium phosphoinositide signaling; PI3K–Akt; Sonic Hedgehog; cAMP/PKA; melanocortin (MC4R).

**Other cellular roles:** INPP5E also supports autophagosome–lysosome fusion in neurons (PMID 27340123) and genomic stability during mitosis (PMID 28031327). Their relevance to MORM is unknown.

**Suggested GO terms:**
- Biological process: GO:0060271 cilium assembly; GO:0007224 smoothened signaling pathway; GO:0046856 phosphatidylinositol dephosphorylation; GO:0042462 eye photoreceptor cell development; GO:0035845 photoreceptor cell outer segment organization
- Molecular function: GO:0004439 phosphatidylinositol-4,5-bisphosphate 5-phosphatase activity
- Cellular component: GO:0005929 cilium; GO:0005930 axoneme; GO:0035869 ciliary transition zone

**Suggested CL terms:** CL:0000210 photoreceptor cell; CL:0000604 rod photoreceptor cell; CL:0000573 retinal cone cell; hypothalamic neuron (CL:0000540 neuron); CL:0000057 fibroblast (patient-cell assays).

**Omics:** no MORM-specific transcriptomic, proteomic, or metabolomic data were found. In patient fibroblasts with INPP5E variants, automated cilia analysis showed shorter cilia and loss of INPP5E ciliary localization (Whiting et al. 2024, **PMID 38806661**; Hardee et al. 2017, **PMID 29052317**).

## 7. Anatomical Structures Affected

- **Primary organs:**
  - retina: UBERON:0000966
  - brain: UBERON:0000955 (cognitive involvement)
  - hypothalamus (inferred): UBERON:0001898
  - adipose tissue / trunk (truncal fat distribution): UBERON:0001013
  - penis: UBERON:0000989
- **Secondary:** lens (cataract): UBERON:0000965
- **Systems:** nervous, visual, endocrine/metabolic, reproductive.
- **Cells:** photoreceptors and, by inference, hypothalamic neurons (see section 6).
- **Subcellular:** primary cilium, ciliary membrane, transition zone, photoreceptor connecting cilium and outer segment (GO:0001750 photoreceptor outer segment).
- **Laterality:** bilateral, symmetric retinal involvement is expected. One unilateral RP case linked to INPP5E has been reported, but its relevance is uncertain (PMID 42181425).

## 8. Temporal Development

- **Onset:** Congenital. The retinal dystrophy and micropenis are present early. Intellectual disability and obesity become apparent in early childhood.
- **Progression:** The original family showed static intellectual disability and non-progressive retinal dystrophy (PMID 16493448), with cataract later (OMIM summary). Other INPP5E-related retinopathies are progressive (PMIDs 34211432, 41465079).
- **Duration:** lifelong.
- **Remission:** none.
- **Critical periods:** early childhood, for vision support, educational intervention, and weight management (inferred).

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive (OMIM; PMID 16493448).
- **Penetrance:** appears complete in the homozygous family; expressivity is variable across the INPP5E spectrum.
- **Anticipation and mosaicism:** none reported.
- **Consanguinity:** central to the index family.
- **Founder effects:** possible in Pakistani families (PMID 31173343).
- **Prevalence:** not established; fewer than 1 in 1,000,000. Orphanet-derived text describes "14 individuals" (consistent with the index family) ([Qeios/Orphanet text](https://www.qeios.com/read/SAZL1Q/pdf)). A few additional MORM-like cases with INPP5E variants have been published, for example a female with severe obesity and cone-rod dystrophy (PMID 34211432).
- **Geography:** the index family was consanguineous and, per the OMIM summary, Pakistani.
- **Sex ratio:** both sexes are affected. Micropenis is male-specific.
- **Carrier frequency:** not determined.
- **Related prevalence data:** in Joubert syndrome and related disorders (JSRD), INPP5E mutations were found in 17 of 483 probands (Travaglini et al. 2013, **PMID 23386033**).

## 10. Diagnostics

- **Clinical evaluation:**
  - ophthalmology: fundoscopy, ERG, OCT, visual acuity (OCT and ERG findings in INPP5E retinopathy: PMID 41465079)
  - developmental and IQ assessment
  - anthropometry (BMI, waist)
  - genital exam and endocrine work-up (gonadotropins and testosterone are reasonable but not described in the literature)
  - metabolic labs: glucose/HbA1c, lipids, liver enzymes
  - brain MRI to look for the Joubert molar tooth sign, which separates MORM from Joubert syndrome
  - renal ultrasound to exclude the cystic kidney disease seen in ciliopathies (inferred)
- **Genetic testing:**
  - Exome or genome sequencing, or a ciliopathy/IRD/BBS/obesity gene panel that includes INPP5E, is the practical first approach.
  - Targeted testing for c.1879C>T can be used for families.
  - Exome sequencing has proved useful in JSRD (PMID 23034536).
  - Reverse phenotyping helped reclassify an INPP5E family (de Goede et al. 2016, **PMID 26748598**).
  - CMA, karyotype, FISH, mtDNA, and repeat-expansion testing are not indicated except to rule out other diagnoses, such as a 9q34 deletion (EHMT1).
- **Functional assays (research):** cilia length and INPP5E localization in fibroblasts (PMIDs 38806661, 29052317).
- **Differential diagnosis:**
  - Bardet–Biedl syndrome: polydactyly, renal disease, progressive rod-cone dystrophy
  - Cohen syndrome: microcephaly, characteristic facies, neutropenia, mottled retina
  - Alström syndrome
  - Joubert syndrome (INPP5E, molar tooth sign)
  - Prader–Willi syndrome
  - MC4R and other monogenic obesity
  - non-syndromic INPP5E retinopathy
- **No formal diagnostic criteria exist.**
- **Screening:** no newborn screening. Cascade carrier testing and prenatal or preimplantation testing are possible once familial variants are known.

## 11. Outcome / Prognosis

There are no survival or life-expectancy data. Survival into adulthood is implied by the multigenerational pedigree and the onset of cataract in the second or third decade (OMIM summary). The main morbidities are:
- lifelong intellectual disability;
- visual impairment, possibly progressive in some genotypes;
- obesity with metabolic complications such as insulin resistance (PMID 34211432);
- cataract.

There are no prognostic biomarkers and no QoL studies.

## 12. Treatment

No disease-specific therapy exists. Management is supportive. All items below are general standard of care, not trial-based:
- **Low-vision services and cataract surgery** when needed. NCIT terms: Cataract Extraction; Low Vision Rehabilitation (verify IDs).
- **Obesity:** diet, exercise, behavioral therapy.
  - MC4R agonist therapy (setmelanotide) is approved for BBS-associated obesity. Its use in MORM is **untested** but has mechanistic rationale (PMID 42838451, the MC4R-neuron link). I did not retrieve approval sources for setmelanotide in this session.
- **Micropenis:** endocrine evaluation and possible testosterone therapy (general practice, not MORM-specific).
- **Developmental and educational support, plus speech therapy.**
- **Gene therapy:** none. RPGR-type retinal gene therapy vectors exist for other IRDs (PMID 31106594), but nothing exists for INPP5E.
- **Clinical trials:** none found that are specific to MORM or INPP5E.
- **Pharmacogenomics:** not applicable.

## 13. Prevention

- **Primary prevention:** genetic counseling. Recurrence risk is 25% per pregnancy for carrier parents. Carrier testing, prenatal diagnosis, or PGT are options once the familial variant is known. Counseling is especially relevant for consanguineous families.
- **Tertiary prevention:**
  - early weight management to prevent diabetes and cardiometabolic complications;
  - regular ophthalmic surveillance, including for cataract;
  - early developmental intervention.
- **Vaccination, environmental, and public-health measures:** not applicable.

## 14. Other Species / Natural Disease

- No naturally occurring MORM-like disease is recorded in animals. I did not search OMIA specifically.
- Orthologs (NCBI Gene IDs not retrieved this session):
  - mouse *Inpp5e* (NCBITaxon:10090)
  - zebrafish *inpp5e* (NCBITaxon:7955); zebrafish data show a role in cilia formation (PMID 23022135)
- The ciliary phosphoinositide mechanism is conserved across vertebrates (mouse, zebrafish, and human cells; PMIDs 26190144, 23022135).
- Zoonotic potential: none.

## 15. Model Organisms

| Model | Phenotype / recapitulation | Ref |
|---|---|---|
| *Inpp5e* constitutive knockout mouse | Embryonic or perinatal lethality (about E18.5 per later papers), neural tube defects, polydactyly, polycystic kidneys (26/26 embryos per one follow-up). Closer to Joubert/Meckel than MORM. Cilia destabilization. Sources disagree on the timing of death. | Jacoby 2009, PMID 19668215 (as summarized in [PMC5223597](https://pmc.ncbi.nlm.nih.gov/articles/PMC5223597), [JCB 2017](https://rupress.org/jcb/article-split/216/1/247/46156/INPP5E-regulates-phosphoinositide-dependent-cilia)) |
| Retina-specific *Inpp5e* knockout mouse | Rapid rod-cone degeneration, no axoneme or disc formation | PMID 33711342 |
| Conditional / inducible adult *Inpp5e* knockout | Outer-segment shortening, Golgi abnormalities, photoreceptor loss | PMID 39871753 |
| Kidney-epithelium *Inpp5e* deletion | Defective ciliogenesis, apical phosphoinositide changes | PMID 27401686 |
| MC4R-neuron CRISPRi of *Inpp5e* (mouse) | Obesity, which models the truncal obesity feature | PMID 42838451 |
| Zebrafish *inpp5e* knockdown | Cilia formation defects, including in the eye | PMID 23022135 |
| Human iPSC-derived retinal organoids, INPP5E KO | Mislocalized ARL13B and rhodopsin, abnormal outer-segment membranes | PMID 42374981 |
| Patient fibroblasts; CRISPR cell models (RPE1, MEFs) | Short or absent cilia, phosphoinositide mislocalization | PMIDs 38806661, 29052317, 38514901, 36967147 |

**Limitations:** constitutive mouse knockouts are too severe to model the mild, viable MORM phenotype. No knock-in of Q627X has been reported. Cognitive and genital phenotypes have not been modeled.

**Resources:** MGI (*Inpp5e*), ZFIN, IMPC. Specific allele IDs were not retrieved.

---

### Main gaps
- There is still essentially one MORM family, so phenotype frequencies are not robust.
- OMIM clinical details (cataract timing, onset ages) and the setmelanotide and HGNC identifiers are unverified in this session.
- No epidemiology, QoL, or natural-history data exist.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 4 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 2 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 32 |
| On topic | 24 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:16493448` *(abstract only)*: "static moderate mental retardation, truncal obesity, a congenital non-progressive retinal dystrophy and micropenis in males"
  - closest text in source: "A consanguineous pedigree is described where 14 individuals are affected with a novel autosomal recessive disorder, which causes static moderate mental retardation, truncal obesity, a congenital nonprogressive retinal dystrophy and micropenis in males"
- `PMID:19668215` *(abstract only)*: "had impaired localization in cilia and was unable to stabilize ciliary structures"
  - closest text in source: "In human INPP5E, we identified a mutation affecting INPP5E ciliary localization and cilium stability in a family with MORM syndrome, a condition related to Bardet-Biedl syndrome"

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.1038/sj.ejhg.5201577`: "static moderate mental retardation, truncal obesity, a congenital non-progressive retinal dystrophy and micropenis in males"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 6 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0100259` (1 mention) - the report calls it "absent"; HP calls it **Postaxial polydactyly**
- `HP:0000252` (1 mention) - the report calls it "absent"; HP calls it **Microcephaly**
- `UBERON:0000955` (1 mention) - the report calls it "cognitive involvement"; UBERON calls it **brain**
- `NCBITaxon:10090` (1 mention) - the report calls it "Inpp5e", "mouse *Inpp5e"; NCBITaxon calls it **Mus musculus**
- `NCBITaxon:7955` (1 mention) - the report calls it "inpp5e", "zebrafish *inpp5e"; NCBITaxon calls it **Danio rerio**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0012423` (2 mentions) - the report calls it "MONDO"; MONDO calls it **MORM syndrome**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCBITaxon:10090` - called "Inpp5e", "mouse *Inpp5e"
- `NCBITaxon:7955` - called "inpp5e", "zebrafish *inpp5e"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.