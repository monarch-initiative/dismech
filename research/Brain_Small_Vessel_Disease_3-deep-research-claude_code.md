---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-23T12:15:28.177174'
end_time: '2026-11-23T12:19:00.956536'
duration_seconds: 212.78
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Brain Small Vessel Disease 3 (COLGALT1)
  mondo_id: MONDO:0100105
  category: Mendelian
  causal_genes: COLGALT1
  omim_id: OMIM:618360
  synonyms: BSVD3
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
  web_search_requests: 9
  num_turns: 18
  total_cost_usd: 1.0330219999999999
  session_id: 00a80a9b-2f88-4c66-94a7-d26f2a2b077c
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 34
  retrieval_calls: 32
  assistant_text_blocks: 2
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
citation_count: 10
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 12
  validator_version: 0.8.0
term_validation:
  total_terms: 11
  verified: 7
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0100105
    reported_labels:
    - MONDO
    ontology_label: brain small vessel disease 3
  - term_id: DOID:0112315
    reported_labels:
    - DOID
    ontology_label: brain small vessel disease 3
  labels_variant: 1
  unresolvable_prefixes:
  - OMIM
  - MGI
  - RGD
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Brain Small Vessel Disease 3 (COLGALT1)
- **MONDO ID:** MONDO:0100105 (if available)
- **Causal gene(s):** COLGALT1
- **OMIM:** OMIM:618360
- **Synonyms:** BSVD3
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Brain Small Vessel Disease 3 (COLGALT1)** covering all of the
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

I'm collecting the primary sources now: the 2018 discovery paper, the follow-up case reports and the mouse-model papers. Then I'll write the report.

# Brain Small Vessel Disease 3 (BSVD3; COLGALT1-related cerebral small vessel disease): research report

**How I scoped this report:** It covers the disease with MONDO:0100105 and OMIM:618360, which is caused by **biallelic variants in *COLGALT1*** (collagen beta(1-O)galactosyltransferase 1; HGNC:26182; NCBI Gene 79709; gene OMIM 617531). It does not cover the similarly named BSVD1 (*COL4A1*) or BSVD2 (*COL4A2*).

**Limits on retrieval:**
- PubMed abstract pages and ClinVar blocked automated access (cookie wall or reCAPTCHA). Abstract text therefore comes from PMC full text, from database summaries, or from search-result snippets. Where a quote is short or partial, I say so.
- The literature is very small. About 5 affected individuals have been published, from 2018 to 2026. Many sections are therefore marked "not available".
- I give ontology IDs only where a retrieved source supplied them: GO IDs from UniProt, and MONDO, OMIM, MedGen, HGNC and DOID IDs. For HPO, CL, UBERON and NCIT I give the term labels only. Their IDs still need to be resolved, for example with a term validator.

---

## 1. Disease information

**Overview.** BSVD3 is an autosomal recessive cerebral small vessel disease caused by biallelic loss-of-function variants in ***COLGALT1***. This gene encodes the ER-luminal enzyme that adds galactose to hydroxylysine residues of collagens, including type IV collagen. The NCBI MedGen definition, which is derived from OMIM, describes it as follows ([MedGen C5193053](https://www.ncbi.nlm.nih.gov/medgen/1677948)):
- It is a disorder of fragile cerebral vessels that predisposes to intracranial haemorrhage.
- The phenotype depends on when and where the bleed happens.
- Some patients have onset in utero or early infancy, with global developmental delay, spasticity and porencephaly.
- Others develop normally or with mild delay until a sudden intracranial haemorrhage causes acute neurological decline.

The discovery paper frames it as a phenocopy of *COL4A1*/*COL4A2* disease. Partial abstract quote: *"Approximately 5% of cerebral small vessel diseases are hereditary, which include COL4A1/COL4A2-related disorders."* (Miyatake et al., Ann Neurol 2018; PMID 30412317; DOI 10.1002/ana.25367).

| Identifier | Value | Source |
|---|---|---|
| MONDO | MONDO:0100105 | [MedGen](https://www.ncbi.nlm.nih.gov/medgen/1677948) |
| OMIM (phenotype) | 618360 | MedGen; [PanelApp](https://panelapp.genomicsengland.co.uk/panels/50/gene/COLGALT1/) |
| OMIM (gene) | 617531 | HGNC REST; PanelApp |
| MedGen CUI | C5193053 | MedGen |
| DOID | DOID:0112315 | [MGI](https://www.informatics.jax.org/marker/MGI:1924348) |
| Orphanet | No BSVD3-specific ORPHA code was found. UniProt links COLGALT1 to Orphanet 99810 ("familial porencephaly"). | UniProt Q8NBJ5 |
| ICD-10 / ICD-11 / MeSH | No disease-specific codes were retrieved. Broader categories such as cerebrovascular disease or porencephaly would be used. | — |

**Synonyms:** BSVD3; brain small vessel disease 3; COLGALT1-related cerebral small vessel disease; "COLGALT1-related collagenopathy", the term used in [Chaisson et al. 2026, J Neurosurg Case Lessons, DOI 10.3171/CASE251029](https://digitalscholar.lsuhsc.edu/som_facpubs/4643).

**Source type:** All knowledge comes from individual case reports (human clinical data). There are no registry or EHR-derived aggregate data.

## 2. Etiology

- **Cause:** Monogenic. BSVD3 is caused by homozygous or compound-heterozygous loss-of-function variants in *COLGALT1* at 19p13.11 ([MedGen](https://www.ncbi.nlm.nih.gov/medgen/1677948); [HGNC](https://www.genenames.org)).
- **Genetic risk factors:** The causal variants are listed in §4. No modifier genes or susceptibility loci have been reported. The Indian adult patient carried a homozygous p.Gly377Arg allele with residual activity and had a mild, late-presenting course. This suggests that the amount of residual enzyme activity may modify severity, although the evidence is a single case ([Maramattom 2025, PMID 39785835](https://pmc.ncbi.nlm.nih.gov/articles/PMC12049204/)).
- **Environmental risk factors:** None have been established. For *COL4A1*-related disease, triggers such as birth trauma and anticoagulation are often discussed. No such data were found for COLGALT1 disease, so any extrapolation is inference.
- **Protective factors:** None are known, genetic or environmental.
- **Gene–environment interactions:** No data.

## 3. Phenotypes

Data come from about 5 published individuals: 2 in PMID 30412317, 1 in PMID 33709034, 1 in PMID 39785835 and 1 in Chaisson 2026. Frequencies are therefore counts, not percentages. The OMIM/MedGen HPO annotation list is: seizure; severe intellectual disability; cerebral atrophy; leukoencephalopathy; spastic quadriplegic cerebral palsy; global developmental delay; lacunar stroke; porencephalic cyst; hypotonia; cerebral calcification ([MedGen](https://www.ncbi.nlm.nih.gov/medgen/1677948)).

| Phenotype (suggested HPO label) | Type | Onset / course | Evidence |
|---|---|---|---|
| Porencephalic cyst | Imaging sign | Antenatal (fetal MRI at 21 weeks) to childhood; progressive | Teunissen 2021 (PMID 33709034): fetal MRI showed *"a cortical mantle defect, periventricular hemorrhage, and ventriculomegaly"*; MedGen |
| Intracranial / intracerebral haemorrhage; periventricular haemorrhage; cerebral microbleeds | Imaging sign / acute event | Fetal, childhood (age 14 in Chaisson 2026), or adult | PMID 33709034 (postnatal MRI showed "elaborate hemorrhages"); Maramattom 2025 ("scattered subcortical hemorrhages" on GRE); Chaisson 2026 (basal ganglia haemorrhage with intraventricular extension) |
| Leukoencephalopathy / white matter hyperintensities | Imaging sign | Childhood to adult; progressive | Miyatake 2018 (Patient 2 had subcortical infarcts and leukoencephalopathy, per abstract summary); Maramattom 2025 ("extensive leukoaraiosis") |
| Lacunar stroke | Clinical and imaging | Adolescence to adult; recurrent | Maramattom 2025 (left hemiplegia at 15, dysarthria at 29, acute lacune at 48) |
| Hydrocephalus / ventriculomegaly | Imaging sign | Antenatal to infancy; progressive | PMID 33709034 (VP shunt at about 10 months); Chaisson 2026 (obstructive hydrocephalus after haemorrhage) |
| Global developmental delay; severe intellectual disability | Neurodevelopmental | Infancy | PMID 33709034 ("severe psychomotor retardation"); MedGen |
| Spastic tetraplegia / spastic quadriplegic CP; axial hypotonia | Sign | Infancy | PMID 33709034 |
| Seizures; infantile spasms; drug-resistant epilepsy | Sign | Infancy (West syndrome at 6.5 months) | PMID 33709034 |
| Microcephaly | Physical sign | Birth (−3.12 SD) | PMID 33709034 |
| Megalocornea, strabismus, optic atrophy (bilateral pale optic nerves) | Ocular signs | Infancy | PMID 33709034 (1 patient). Fundus was normal in the adult case. |
| Cerebral calcification | Imaging sign | — | MedGen; PanelApp reviewer summary |
| Executive dysfunction (mild) | Cognitive / behavioural | Adult | Maramattom 2025 |
| Hemiparesis, dysarthria | Signs | Adolescence and adulthood; episodic | Maramattom 2025 |

**Severity:** Highly variable, from severe congenital porencephaly with death at about 4 years (PMID 33709034) to an adult who reached mRS 0 after a lacunar stroke (PMID 39785835).

**Quality of life:** No formal QoL instruments (EQ-5D, SF-36) have been reported. The impact is inferred from case descriptions: severe congenital cases have total dependence, with intractable epilepsy and shunt dependence.

## 4. Genetic and molecular information

**Gene.** *COLGALT1* (previous symbol GLT25D1; aliases ColGalT1, FLJ22329, procollagen galactosyltransferase, hydroxylysine galactosyltransferase).
- IDs: HGNC:26182; Ensembl ENSG00000130309; MANE Select ENST00000252599.9 / NM_024656.4 / NP_078932.2; UniProt Q8NBJ5; locus 19p13.11.
- Protein: 622 aa, signal peptide 1–29, ER-retention motif at 619–622, glycosyltransferase family GT25.
- Enzyme: EC 2.4.1.50. Reaction: 5-hydroxy-L-lysyl-[collagen] + UDP-α-D-galactose → 5-O-(β-D-galactosyl)-5-hydroxy-L-lysyl-[collagen] + UDP. It *"has no glucosyltransferase activity"*.
- Source: UniProt Q8NBJ5 (rest.uniprot.org).

The founding biochemistry is Schegg et al. 2009, Mol Cell Biol, PMID 19075007, "Core glycosylation of collagen is initiated by two beta(1-O)galactosyltransferases". Snippet: *"Amino acid analysis of the products of GLT25D1 and GLT25D2 reactions confirmed the transfer of galactose to hydroxylysine residues"*.

**Reported disease variants**

| Patient | Variants (NM_024656.3) | Zygosity | Type | Functional data |
|---|---|---|---|---|
| Miyatake P1 (PMID 30412317) | c.452T>G p.(Leu151Arg) + c.1096delG p.(Glu366Argfs*15) | Compound heterozygous | Missense + frameshift | No detectable ColGalT1 protein or activity; modelling predicts Leu151Arg destabilises folding |
| Miyatake P2 (PMID 30412317) | c.460G>C p.(Ala154Pro) + c.1129G>C p.(Gly377Arg) | Compound heterozygous | Missense ×2 | Ala154Pro predicted to destabilise folding; Gly377Arg has residual activity |
| Teunissen (PMID 33709034) | c.625-2A>C | Homozygous; parents not consanguineous | Canonical splice-acceptor | RT-PCR shows 2 cryptic splice sites. The major transcript gives p.(Gly209fs), which is subject to nonsense-mediated decay (NMD). The minor transcript gives in-frame p.(Gly209_Lys212del). Absent from gnomAD. |
| Maramattom (PMID 39785835) | c.1129G>C p.(Gly377Arg) | Homozygous | Missense | Classified by the authors as a VUS. The letter says it *"has a milder effect on ColGalT activity"*. |
| Chaisson 2026 (DOI 10.3171/CASE251029) | "Known biallelic COLGALT1 variant" | Biallelic | Not retrieved | — |

- **ACMG classification / ClinVar:** Not retrieved (ClinVar blocked automated access). The splice and frameshift alleles plus functional data would usually support Pathogenic/Likely pathogenic, but this is my assessment, not a ClinVar record.
- **Allele frequency:** c.625-2A>C is absent from gnomAD (PMID 33709034). No other frequencies were retrieved.
- **Origin:** Germline.
- **Mechanism class:** Loss of function (hypomorphic or null).
- **Gene–disease validity:** Genomics England PanelApp rates COLGALT1 **Green** (biallelic) on the Familial cerebral small vessel disease, Fetal anomalies, Inherited white matter disorders, Childhood-onset white matter disorders and cerebral calcification, and Early onset or syndromic epilepsy panels. Its cited PMIDs are 30412317, 33709034 and 31759980; I did not retrieve the content of 31759980 ([PanelApp](https://panelapp.genomicsengland.co.uk/panels/50/gene/COLGALT1/)).
- **Modifier genes, epigenetics, chromosomal abnormalities:** None reported.

**GO annotations (UniProt):**
- GO:0050211 procollagen galactosyltransferase activity
- GO:0005788 endoplasmic reticulum lumen
- GO:0030199 collagen fibril organization
- GO:1904028 positive regulation of collagen fibril organization
- GO:0180062 protein O-linked glycosylation via galactose
- Reactome R-HSA-1650814, Collagen biosynthesis and modifying enzymes

## 5. Environmental information

No environmental, lifestyle or infectious factors have been reported. The adult patient was a non-smoker without hypertension or diabetes (PMID 39785835).

## 6. Mechanism and pathophysiology

**Causal chain**

1. Biallelic *COLGALT1* loss-of-function variants (missense that destabilises folding, frameshift, or splice) **lead to** absent or reduced ColGalT1 protein and galactosyltransferase activity in the ER lumen. This is demonstrated in patient cells: ColGalT1 was undetectable in Miyatake P1 (PMID 30412317).
2. Loss of ColGalT1 activity **results in** failure to galactosylate hydroxylysine residues of procollagens, including COL4A1. This is directly demonstrated in mouse fibroblasts, where collagen IV shows a lower molecular mass, *"likely due to the loss of COLGALT1-mediated galactosylation of hydroxylysines"* (Geister 2019, PMID 31101663). In humans it is inferred.
3. Under-glycosylated COL4A1 **leads to** impaired trimer assembly or stability and reduced COL4A1 protein and secretion. This was shown in vitro by RNAi and rescue in Miyatake 2018. Teunissen summarises: *"reduced ColGalT1 activity results in decreased CoL4a1 protein, thereby resulting in reduced secretion of type IV collagen."*
   - **Branch A:** In mouse cells, collagen IV accumulates both inside cells and in the ECM, possibly through instability and degradation (PMID 31101663).
   - **Branch B:** Collagen I secretion is reduced and collagen VI glycosylation is altered (mouse; PMID 31101663). Any contribution to the human phenotype is unknown.
4. A deficient or abnormal type IV collagen network in the vascular basement membrane **leads to** fragile cerebral small vessels. This step is **inferred** by analogy with *COL4A1*/*COL4A2* disease. Miyatake 2018 concludes that the variants act through a molecular pathogenesis common with *COL4A1*/*COL4A2*-related disorders.
5. Fragile small vessels **result in** haemorrhage and ischaemia:
   - **Fetal or perinatal periventricular haemorrhage** leads to porencephalic cysts, ventriculomegaly and progressive hydrocephalus, then developmental delay, spastic tetraplegia and epilepsy (PMID 33709034).
   - **Later-life events** include deep or basal ganglia haemorrhage with intraventricular extension and hydrocephalus (Chaisson 2026), and lacunar infarcts, microbleeds and leukoaraiosis that lead to hemiparesis, dysarthria and mild executive dysfunction (PMID 39785835).

**Structural biology (in vitro).** ColGalT1 forms a complex with LH3/PLOD3, the lysyl hydroxylase / glucosyltransferase. Cryo-EM shows a 2:2 LH3:ColGalT1 tetramer (the "KOGG" complex), which suggests coupled lysyl hydroxylation, galactosylation and glucosylation (Peng et al., Nat Commun 2025;16:2436; [PMC11897130](https://pmc.ncbi.nlm.nih.gov/articles/PMC11897130); PDB 8ZGC, 8ZGE, 8ZGG, 8ZGH). X-ray structures 9EVJ, 9EVK and 9EVL also exist (UniProt). The ER colocalisation of ColGalT1 with PLOD3 is noted in UniProt (Liefhebber 2010, PMID 20470363). Domain mapping is in Perrin-Tricaud et al. 2011 (PMID 22216269).

**Other mechanism categories:**
- Immune involvement, metabolic changes and epigenetics: none reported.
- Omics: no transcriptomic, proteomic, metabolomic, single-cell or spatial data exist for patients.
- Knockout screen data: CRISPR knockout of GLT25D1 in osteosarcoma cells caused collagen accumulation (Baumann & Hennet 2016, PMID 27402836).

**Suggested ontology terms:**
- GO (with IDs from UniProt): procollagen galactosyltransferase activity (GO:0050211); protein O-linked glycosylation via galactose (GO:0180062); collagen fibril organization (GO:0030199).
- GO (labels only; IDs to resolve): basement membrane organization; collagen biosynthetic process.
- CL (labels only): brain vascular endothelial cell; pericyte; vascular smooth muscle cell; fibroblast. These are inferred as collagen IV producers.

## 7. Anatomical structures affected

- **Primary:** Brain, specifically the cerebral small vessels (arterioles and capillaries) and their basement membrane. Affected sites:
  - periventricular and deep white matter
  - basal ganglia and caudate
  - corona radiata and centrum semiovale
  - cerebellar white matter
  - ventricular system
- **Secondary:** Eye, with megalocornea, strabismus and optic atrophy (1 case). No kidney or muscle involvement has been documented in patients, although *COL4A1* disease and mouse Colgalt1 mutants (muscle) suggest these organs are worth checking.
- **Body systems:** Nervous and cardiovascular (cerebrovascular).
- **Subcellular:** Endoplasmic reticulum lumen (GO:0005788); extracellular basement membrane (label only, ID to resolve).
- **Laterality:** White matter changes are symmetrical and bilateral in the adult (PMID 39785835). Haemorrhages and infarcts can be unilateral or asymmetric.
- **Suggested UBERON labels (IDs to resolve):** brain; cerebral white matter; basal ganglia; lateral ventricle; cerebral arteriole; capillary basement membrane; eye.

## 8. Temporal development

- **Onset:** Ranges from antenatal (ventriculomegaly at a 20-week ultrasound) to adolescence (stroke at 15; haemorrhage at 14). The adult case was diagnosed at 48 after earlier events.
- **Onset pattern:** Either congenital and static-progressive, or acute and episodic (haemorrhage, lacunar stroke) on a background of chronic, insidious white matter disease.
- **Progression:** Hydrocephalus and white matter loss progressed in the severe infant. The adult had recurrent events over about 33 years.
- **Stages, remission and critical periods:** Not defined. The prenatal and perinatal period seems to be a window of vulnerability to haemorrhage. This is inferred from the fetal-onset case.

## 9. Inheritance and population

- **Inheritance:** Autosomal recessive (MedGen; PanelApp: "BIALLELIC, autosomal or pseudoautosomal").
- **Prevalence:** Unknown (ultra-rare). About 5 patients have been published worldwide: Japan (2, from a Japanese group, PMID 30412317), the Netherlands (1, ancestry not stated), India (1) and the USA (1).
- **Penetrance and expressivity:** Penetrance is unknown. Expressivity is highly variable.
- **Other inheritance features:**
  - Anticipation: not applicable.
  - Founder effects and carrier frequency: unknown.
  - Consanguinity: the Teunissen parents were not consanguineous; this was not stated for the Indian homozygote.
- **Sex:** 3 male (Teunissen boy, Indian man and at least one other), 1 female (Chaisson), others not recorded. The numbers are too small to estimate a sex ratio.

## 10. Diagnostics

- **Imaging (key):** Brain MRI with susceptibility-weighted or GRE sequences shows porencephaly, haemorrhages and microbleeds, leukoencephalopathy, lacunes, calcification (CT) and hydrocephalus. Fetal ultrasound and MRI can detect ventriculomegaly and porencephaly antenatally (PMID 33709034). MR angiography was normal in the adult.
- **Lab and biomarker tests:** No clinical biomarker exists. Research assays include ColGalT1 western blot and galactosyltransferase activity (PMID 30412317), and RT-PCR of lymphocyte RNA to confirm missplicing (PMID 33709034).
- **Genetic testing:**
  - Use exome or genome sequencing, or a cerebral small vessel disease / porencephaly panel that includes *COLGALT1*. PanelApp includes it on the 5 panels listed in §4.
  - *COL4A1*/*COL4A2* testing alone will miss it. In Teunissen 2021, COL4A1/2 Sanger sequencing was negative. Miyatake notes COL4A1/2 diagnostic yield of about 20% in suspected cases.
  - RNA studies help classify splice variants.
  - CMA, karyotype, FISH, mtDNA and repeat-expansion testing are not relevant, although mtDNA was sequenced in the adult to rule out mitochondrial disease.
- **Clinical criteria:** No standardised criteria exist.
- **Differential diagnosis:**
  - *COL4A1* (BSVD1) and *COL4A2* (BSVD2) disease. These are autosomal dominant and often include eye, kidney and muscle features.
  - Other monogenic small vessel diseases, such as CADASIL (*NOTCH3*) and CARASIL (*HTRA1*). This is a general differential, not specifically sourced here.
  - Acquired fetal or neonatal haemorrhage (alloimmune thrombocytopenia, trauma).
  - Vasculitis. The adult was misdiagnosed with "probable cerebral vasculitis" and given immunosuppression for about 6 years (PMID 39785835).
  - Chaisson 2026 recommends considering genetic small vessel disease in unexplained paediatric intracerebral haemorrhage.
- **Screening:** No population screening. Cascade testing of siblings and carrier testing of parents is possible once the familial variants are known.

## 11. Outcome and prognosis

- **Mortality:** One severe congenital case died *"some weeks before his fourth birthday"* after acute respiratory and haemodynamic decline (PMID 33709034). No survival statistics exist.
- **Morbidity:** Severe cases have severe intellectual disability, spastic tetraplegia, intractable epilepsy and shunt dependence. The mild adult case recovered to mRS 0 after a lacunar stroke but had cumulative white matter disease and mild executive dysfunction (PMID 39785835).
- **Complications:** Hydrocephalus requiring a shunt; intraventricular haemorrhage; recurrent stroke.
- **Prognostic factors:** Probably the timing of the first haemorrhage (fetal or later) and the residual enzyme activity of the alleles. Null alleles appear in the severe cases and the hypomorphic p.Gly377Arg in the mild one. This is inferred from a handful of cases.

## 12. Treatment

There is no disease-specific therapy, no pharmacogenomic data and no clinical trials. A ClinicalTrials.gov search was not performed. Given the literature, no COLGALT1-specific trials are expected.

| Intervention | Context | Source | Suggested NCIT label |
|---|---|---|---|
| Ventriculoperitoneal shunt | Progressive hydrocephalus | PMID 33709034 | Ventriculoperitoneal shunt placement |
| Prednisolone, zonisamide, nitrazepam | Infantile spasms / epilepsy | PMID 33709034 | Antiepileptic agent; corticosteroid |
| Neurosurgical management of ICH with hydrocephalus | Basal ganglia ICH with intraventricular extension | Chaisson 2026 (details not retrieved) | External ventricular drain (not confirmed) |
| Dual antiplatelets + atorvastatin | Acute lacunar stroke in an adult | PMID 39785835 | Antiplatelet agent; statin |
| Stopping immunosuppression | After the vasculitis misdiagnosis was corrected | PMID 39785835 | — |

**Caution on antiplatelets:** Giving antithrombotics to a patient with microbleeds and a haemorrhage-prone vasculopathy carries a theoretical bleeding risk. The source letter does not discuss this; it is my own note.

**Supportive and rehabilitative care:** Physiotherapy, occupational therapy and speech therapy for spasticity and developmental delay (general practice, not specifically sourced).

Gene, cell, RNA and targeted therapies: none.

## 13. Prevention

- **Primary prevention:** Not applicable beyond reproductive options. Genetic counselling gives a 25% recurrence risk for sibs (standard for autosomal recessive inheritance). Prenatal or preimplantation testing is possible once both familial variants are known.
- **Secondary prevention:** Early MRI of at-risk sibs, and fetal ultrasound or MRI in subsequent pregnancies. The latter is supported by antenatal detection in PMID 33709034.
- **Tertiary prevention:** This is extrapolated from *COL4A1* practice and is not established for COLGALT1:
  - control blood pressure
  - avoid head trauma and unnecessary anticoagulant or antithrombotic exposure
  - consider delivery mode for affected fetuses
- **Immunisation, public health and prophylaxis:** Not applicable.

## 14. Other species and natural disease

- No naturally occurring animal disease was found; an OMIA search was not performed.
- **Orthologues:**
  - Mouse *Colgalt1*: MGI:1924348; NCBI Gene 234407; synonyms Glt25d1, 2810024B22Rik.
  - Rat: RGD:1309002.
  - Zebrafish: duplicated *colgalt1a* and *colgalt1b* (PMID 31101663).
- **Conservation:** The function (collagen hydroxylysine galactosylation) is conserved across vertebrates. GO annotation also cites FlyBase evidence for O-linked galactosylation.
- **Zoonotic potential:** None.

## 15. Model organisms

| Model | Genetics | Phenotype | Recapitulation and limits |
|---|---|---|---|
| Mouse *Colgalt1^fosse* (ENU) | c.T388C p.W130R, missense in the catalytic domain; no detectable protein in MEFs | Perinatal lethality; disorganised, shorter muscle fibres; downward-bent forepaws; small carpals and rib cage; variable cleft palate and exencephaly; open eyelids; skin haemorrhages. Collagen IV accumulates intracellularly and in the ECM with reduced molecular mass; collagen I secretion is reduced; collagen VI secretion is normal. | Reproduces the biochemistry and a bleeding tendency (skin). No brain small vessel or haemorrhage phenotype was reported. The authors propose it as a model of connective tissue disorder or myopathy. Geister et al., Dis Model Mech 2019, PMID 31101663, [PMC6602307](https://pmc.ncbi.nlm.nih.gov/articles/PMC6602307/) |
| Mouse null alleles (targeted, e.g. Colgalt1^tm1.1Gpt, exon 2–3 deletion) | Knockout | *"lethality during organogenesis, growth retardation, and abnormalities of the placenta and liver"*. Heterozygotes show impaired growth and susceptibility to liver injury. Geister cites a knockout dying before E13.5 (Ye et al. 2018). | Too lethal to model the human cerebral disease. A PanelApp reviewer notes *"vascular network defects"* in null mice. [MGI](https://www.informatics.jax.org/marker/MGI:1924348); Ye et al. Mol Med Rep 2018, PMID 30132521 (liver injury) |
| Zebrafish *colgalt1a;colgalt1b* double mutants | Loss of function | Muscle disorganisation at 8–9 dpf; death before 10 dpf | Musculoskeletal only (PMID 31101663) |
| Cell models | Patient-derived cells; RNAi with rescue; CRISPR knockout of GLT25D1 in osteosarcoma cells | Loss of ColGalT activity; reduced COL4A1 secretion; collagen accumulation | PMID 30412317; PMID 27402836 |

**Resources:**
- MGI lists 6 alleles (ENU, chemically induced, endonuclease-mediated, gene trap, 2 targeted).
- A commercial knockout line, Cyagen S-KO-17029, is also available.
- No iPSC lines or brain organoid models have been reported.
- There is no conditional (vascular-specific) model, which is the main gap in modelling BSVD3.

---

### Key references
- Miyatake S et al. *Ann Neurol* 2018;84(6):843–853. PMID 30412317. DOI 10.1002/ana.25367. [Record](https://eld.bl.uk/catalog/100108980496_0x000001)
- Teunissen MWA et al. *Neurol Genet* 2021;7(2):e564. PMID 33709034. [PMC7943220](https://pmc.ncbi.nlm.nih.gov/articles/PMC7943220/)
- Maramattom BV. *Ann Indian Acad Neurol* 2025;28(2):287–289. PMID 39785835. [PMC12049204](https://pmc.ncbi.nlm.nih.gov/articles/PMC12049204/)
- Chaisson JM et al. *J Neurosurg Case Lessons* 2026;11(13). DOI 10.3171/CASE251029. PMID 41911597 (listed in PubMed search results; full text not retrieved). [Record](https://digitalscholar.lsuhsc.edu/som_facpubs/4643)
- Geister KA et al. *Dis Model Mech* 2019;12(6):dmm037176. PMID 31101663. [PMC6602307](https://pmc.ncbi.nlm.nih.gov/articles/PMC6602307/)
- Schegg B et al. *Mol Cell Biol* 2009;29(4):943–52. PMID 19075007
- Perrin-Tricaud C et al. *PLoS One* 2011;6:e29390. PMID 22216269
- Baumann S, Hennet T. *J Biol Chem* 2016;291:18514–24. PMID 27402836
- Peng et al. *Nat Commun* 2025;16:2436. [PMC11897130](https://pmc.ncbi.nlm.nih.gov/articles/PMC11897130)
- Hennet T. "Collagen glycosylation". *Curr Opin Struct Biol* 2019. PMID 30822656 (review; not read)
- Databases: [MedGen C5193053](https://www.ncbi.nlm.nih.gov/medgen/1677948); [PanelApp](https://panelapp.genomicsengland.co.uk/panels/50/gene/COLGALT1/); [MGI:1924348](https://www.informatics.jax.org/marker/MGI:1924348); UniProt Q8NBJ5; HGNC:26182

**Quote limits.** Several sources would only allow short quotes. Before you use quotes as evidence snippets in the knowledge base, check them against the full PubMed abstracts, for example with `MS_linkml-reference-validator`. This applies especially to the Miyatake 2018 abstract, which I only saw in part.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 11 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 3 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0100105` (2 mentions) - the report calls it "MONDO"; MONDO calls it **brain small vessel disease 3**
- `DOID:0112315` (1 mention) - the report calls it "DOID"; DOID calls it **brain small vessel disease 3**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005788` (2 mentions) - the report calls it "Subcellular:** Endoplasmic reticulum lumen"; GO calls it **endoplasmic reticulum lumen**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `MGI`, `RGD`.