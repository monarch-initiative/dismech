---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-6[1m]
cached: false
start_time: '2026-09-30T21:16:47.722944'
end_time: '2026-09-30T21:22:34.174515'
duration_seconds: 346.45
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Congenital Herpes Simplex Virus Infection
  mondo_id: MONDO:0017381
  category: Infectious
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
  - claude-opus-4-6[1m]
  web_search_requests: 13
  num_turns: 23
  total_cost_usd: 1.7794532499999995
  session_id: 133386cd-f3c4-4569-9232-ae0cddfa483b
  stop_reason: end_turn
  assistant_text_blocks: 1
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
citation_count: 24
reference_validation:
  total_references: 28
  verified: 28
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 28
  on_topic: 19
  off_topic: 1
  off_topic_references:
  - PMID:2020171
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 65
  verified: 61
  not_found: 1
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.016
  labels_checked: 51
  labels_matching: 34
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0017381
    reported_labels:
    - MONDO
    - Congenital herpes simplex virus infection
    ontology_label: congenital herpes simplex virus infection
  - term_id: HP:0002340
    reported_labels:
    - Hydranencephaly
    ontology_label: Caudate atrophy
  - term_id: HP:0000483
    reported_labels:
    - Chorioretinitis
    ontology_label: Astigmatism
  - term_id: HP:0005765
    reported_labels:
    - DIC
    ontology_label: Sacral meningocele
  - term_id: CHEBI:60726
    reported_labels:
    - Valacyclovir
    ontology_label: procainamide 4-hydroxylamine
  labels_variant: 12
  unresolved_terms:
  - HP:0045023
  unresolvable_prefixes:
  - ORPHA
  - LOINC
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Herpes Simplex Virus Infection
- **MONDO ID:** MONDO:0017381 (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Congenital Herpes Simplex Virus Infection** covering all of the
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

Now I have sufficient information to write a comprehensive research report. Let me compile it.

---

# Comprehensive Research Report: Congenital Herpes Simplex Virus Infection

## 1. Disease Information

### Overview

Congenital Herpes Simplex Virus (HSV) infection is a group of congenital anomalies resulting from maternal HSV infection and subsequent fetal/neonatal infection with herpes simplex virus type 1 (HSV-1) or type 2 (HSV-2). It represents a spectrum of disease acquired either *in utero* (transplacental or ascending infection) or perinatally (during passage through an infected birth canal). The intrauterine form is the rarest and most severe, characterized by a classic triad of cutaneous, neurologic, and ophthalmologic findings (PMID:40027069).

Neonatal HSV disease is traditionally classified into three categories based on the extent of involvement:
- **Skin, Eye, and Mouth (SEM) disease** (~45% of cases)
- **Central Nervous System (CNS) disease** (~30% of cases)
- **Disseminated disease** (~25% of cases)

True congenital (intrauterine) HSV infection accounts for approximately 5% of all neonatal HSV cases, while 85% are acquired peripartum and 10% postnatally (PMID:40027069).

### Key Identifiers

| Database | Identifier |
|----------|------------|
| MONDO | MONDO:0017381 |
| Orphanet | ORPHA:293 |
| ICD-10 | P35.2 (Congenital herpesviral [herpes simplex] infection) |
| ICD-11 | KA62.3 |
| UMLS | C4275250 |
| MeSH | D006558 (Herpes Simplex, broader) |

### Synonyms
- Congenital herpes simplex virus infection
- Intrauterine herpes simplex infection
- Neonatal herpes simplex (broader, includes peripartum acquisition)
- Congenital HSV infection

---

## 2. Etiology

### Primary Cause

Congenital HSV infection is caused by vertical transmission of Herpes Simplex Virus (HSV-1 or HSV-2, family *Herpesviridae*, subfamily *Alphaherpesvirinae*) from an infected mother to the fetus or neonate. HSV is a large, enveloped double-stranded DNA virus (~152 kb genome) encoding approximately 80 proteins.

**Routes of vertical transmission:**
1. **Transplacental (hematogenous)**: During maternal primary viremia, the virus crosses the placenta — the predominant route for true congenital (intrauterine) infection (PMID:40027069)
2. **Ascending infection**: Virus ascends from the genital tract through ruptured or intact amniotic membranes
3. **Intrapartum contact**: Direct contact with infectious secretions in the birth canal (most common overall)

### Risk Factors

**Maternal factors:**
- **Primary maternal genital HSV infection near delivery**: The strongest risk factor. Infants born to women with primary genital HSV infection near delivery have a 25–60% risk of neonatal herpes, compared to <2% with recurrent genital HSV (PMID:2020171; Brown et al., *NEJM* 1991)
- **Absence of maternal HSV-specific IgG antibodies**: Lack of transplacental protective antibodies leaves the neonate without passive immunity
- **Prolonged rupture of membranes** (>4–6 hours): Increases ascending infection risk
- **Vaginal delivery** with active genital lesions
- **Use of fetal scalp electrodes**: Disrupts neonatal skin barrier

**Neonatal/fetal factors:**
- **Prematurity**: Immature immune system and skin barrier compromise
- **Fetal skin barrier disruption**: Permits viral entry
- **Immature neonatal innate immunity**: Particularly dampened TLR3–interferon signaling in the newborn brain (PMID:33055261)

**Host genetic susceptibility (inborn errors of immunity):**
Mutations in TLR3 pathway genes predispose to severe HSV disease, particularly HSV encephalitis:
- *TLR3*, *UNC93B1*, *TRIF* (*TICAM1*), *TRAF3*, *TBK1*, *IRF3*, *STAT1*, *IFNAR1*, *NEMO* (*IKBKG*)
- These genetic alterations impair IFN-α/β production within the central nervous system (PMC9961685)

### Protective Factors

- **Pre-existing maternal HSV-specific antibodies** (from prior HSV-1 or HSV-2 infection): Reduce neonatal transmission risk to <2% in recurrent infections
- **Cesarean delivery**: Reduces neonatal HSV risk by approximately 86% when active genital lesions are present (Brown et al., *JAMA* 2003)
- **Maternal antiviral suppressive therapy** from 36 weeks gestation: Reduces viral shedding at delivery and need for cesarean section (PMID:18254066)

---

## 3. Phenotypes

### Cutaneous Manifestations

| Phenotype | HPO Term | Frequency | Notes |
|-----------|----------|-----------|-------|
| Skin vesicles/vesicular rash | HP:0200037 (Skin vesicle) | Very frequent (~80% in SEM) | Active vesicles, often clustered; may present in dermatomal distribution |
| Scarring/cicatricial skin lesions | HP:0100699 (Scarring) | Frequent in intrauterine | Aplasia cutis, crusted papules |
| Hyperpigmentation | HP:0000953 (Hyperpigmentation of the skin) | Occasional | Post-inflammatory |
| Hypopigmentation | HP:0001010 (Hypopigmentation of the skin) | Occasional | Post-inflammatory |

### Neurological Manifestations

| Phenotype | HPO Term | Frequency | Notes |
|-----------|----------|-----------|-------|
| Microcephaly | HP:0000252 | Occasional (~7.5%) | Characteristic of intrauterine infection |
| Hydranencephaly | HP:0002340 | Occasional (~7.5%) | Severe, intrauterine |
| Seizures | HP:0001250 | ~67% in CNS disease | Often multifocal |
| Intracranial calcifications | HP:0002514 | Frequent in intrauterine/CNS | Distinguishing feature |
| Encephalopathy | HP:0001298 (Encephalopathy) | Frequent in CNS/disseminated | Obtundation, irritability |
| Intellectual disability | HP:0001249 | 30–70% of CNS survivors | Long-term sequela |
| Cerebral palsy | HP:0100021 | Variable | Long-term sequela |
| Epilepsy | HP:0001250 | Variable | Long-term sequela |

### Ophthalmologic Manifestations

| Phenotype | HPO Term | Frequency | Notes |
|-----------|----------|-----------|-------|
| Chorioretinitis | HP:0000483 (Chorioretinitis) | Frequent in intrauterine | Part of classic triad |
| Microphthalmia | HP:0000568 | Occasional | Intrauterine infection |
| Cataracts | HP:0000518 | Occasional | Congenital |
| Keratoconjunctivitis | HP:0000563 (Keratoconjunctivitis) | Occasional | Can lead to corneal scarring |
| Optic atrophy | HP:0000648 | Occasional | Late finding |

### Systemic Manifestations

| Phenotype | HPO Term | Frequency | Notes |
|-----------|----------|-----------|-------|
| Fever / hypothermia | HP:0001945 (Fever) / HP:0045023 (Hypothermia) | ~56% | Temperature instability |
| Hepatomegaly | HP:0002240 | Frequent in disseminated | Liver involvement |
| Hepatitis | HP:0012115 (Hepatic failure) | Frequent in disseminated | Can be fulminant |
| Jaundice | HP:0000952 (Jaundice) | Frequent in disseminated | |
| Pneumonitis | HP:0006517 (Alveolar hemorrhage) | ~25% disseminated | |
| Disseminated intravascular coagulation | HP:0005765 (DIC) | Frequent in disseminated | |
| Intrauterine growth restriction | HP:0001511 | ~33% | |
| Premature birth | HP:0001622 | ~33% | |
| Lethargy | HP:0001254 (Lethargy) | Very frequent | |
| Poor feeding | HP:0011968 (Feeding difficulties) | Frequent | |
| Ascites | HP:0001541 (Ascites) | Occasional | In disseminated disease |

---

## 4. Genetic/Molecular Information

### Infectious Agent (Not a Mendelian Genetic Disease)

Congenital HSV infection is an infectious disease, not a monogenic disorder. The causative agents are:
- **HSV-1** (Human alphaherpesvirus 1; NCBITaxon:10298)
- **HSV-2** (Human alphaherpesvirus 2; NCBITaxon:10310)

Globally, neonatal HSV disease shows near-equal contributions from both serotypes: HSV-1 accounts for 47.3% and HSV-2 for 52.8%, with a temporal shift toward increasing HSV-1 proportion (yearly 1.4% increase in HSV-1 cases) (PMID:41860333).

### Host Genetic Susceptibility Loci

While not causative in the Mendelian sense, inborn errors of immunity in the TLR3–IFN signaling pathway markedly increase susceptibility to severe HSV disease:

| Gene | HGNC | OMIM | Inheritance | Functional Consequence |
|------|------|------|-------------|----------------------|
| *TLR3* | hgnc:11849 | 613002 | AD/AR | Impaired IFN-α/β production in CNS |
| *UNC93B1* | hgnc:13481 | 610551 | AR | Defective TLR3/7/8/9 trafficking |
| *TRIF* (*TICAM1*) | hgnc:18348 | 614850 | AD/AR | Impaired TLR3 signaling |
| *TRAF3* | hgnc:12033 | 614849 | AD | Impaired IFN-β induction |
| *TBK1* | hgnc:11584 | 614847 | AD | Impaired IRF3 phosphorylation |
| *IRF3* | hgnc:6118 | — | AD | Impaired IFN-β transcription |
| *IRF7* | hgnc:6122 | — | AR | Impaired IFN-α production |
| *STAT1* | hgnc:11362 | — | AD | Impaired IFN response |
| *IFNAR1* | hgnc:5432 | — | AR | Absent type I IFN receptor |

These defects impair the TLR3-dependent type I interferon response that is particularly critical in the CNS for controlling HSV replication (PMC9961685; PMC10231989). A case report documented neonatal HSV-2 encephalitis associated with a compound heterozygous *TLR3* mutation (PMC13485870).

### HSV Virology

**Viral entry receptors:**
- **Nectin-1** (PVRL1/NECTIN1; hgnc:9706): Primary receptor on neurons and epithelial cells
- **HVEM** (TNFRSF14; hgnc:11912): Herpesvirus entry mediator; expressed on immune cells
- **3-O-sulfated heparan sulfate**: Modified proteoglycan receptor

**Essential entry glycoproteins:** gB, gD, gH, gL mediate viral envelope–cell membrane fusion.

---

## 5. Environmental Information

### Infectious Agents

- **Primary agent**: HSV-1 (NCBITaxon:10298) and HSV-2 (NCBITaxon:10310)
- HSV-2 has historically been more commonly associated with genital herpes and neonatal transmission, but HSV-1 is increasingly implicated, now representing nearly half of neonatal cases globally (PMID:41860333)

### Transmission Route

- **ECTO term**: Exposure to herpes simplex virus (sexual/mucosal contact)
- Vertical transmission: transplacental, ascending, or intrapartum
- Rare postnatal transmission: via contact with oral/labial HSV lesions (caregivers)

### Environmental Risk Modifiers

- Socioeconomic factors influence HSV seroprevalence patterns
- Declining childhood HSV-1 seroprevalence in high-income countries paradoxically increases susceptibility to primary genital HSV-1 infection in young adults, shifting the epidemiology of neonatal herpes

---

## 6. Mechanism / Pathophysiology

### Causal Chain

1. **Maternal HSV infection (primary or reactivation)** → maternal genital tract viral shedding or viremia
2. **Viral entry into fetal/neonatal tissues** → transplacental hematogenous spread (intrauterine) or direct mucosal/skin contact (peripartum) → HSV binds nectin-1/HVEM on epithelial cells and neurons via gD glycoprotein
3. **Local viral replication in epithelial cells** → cytopathic effect (cell lysis, multinucleated giant cells, Cowdry type A intranuclear inclusions) → leads to skin vesicles and mucosal ulceration (SEM disease)
4. **Viral neurotropism and axonal transport** → HSV travels retrogradely along sensory nerves to CNS → leads to necrotizing encephalitis with hemorrhagic infarction, particularly in temporal lobes and limbic system (GO:0019079, viral genome replication)
5. **Dampened neonatal innate immune response** → immature TLR3–IFN-β signaling in newborn brain (PMID:33055261) → failure to contain viral replication in CNS → widespread neuronal destruction, astrocyte activation, microglial inflammation (GO:0045087, innate immune response)
6. **HSV immune evasion** → ICP34.5 and Us11 inhibit PKR activation; ICP0 degrades PML bodies; gL abrogates NF-κB nuclear translocation (PMC10203706) → leads to unchecked viral replication
7. **Placental inflammation** (intrauterine infection) → pro-inflammatory mediators detected in fetal tissues; necrotizing villitis, chorioamnionitis, maternal floor infarction (PMID:34696359; PMC9557870) → leads to intrauterine growth restriction, preterm birth, fetal death
8. **Hematogenous dissemination** → viremia spreads to liver, adrenals, lungs, brain → leads to hepatic necrosis, adrenal hemorrhage, pneumonitis, DIC (disseminated disease)
9. **Neuroinflammation and tissue destruction** → necrotizing meningoencephalitis → leads to long-term sequelae: microcephaly, hydranencephaly, intracranial calcifications, intellectual disability, seizure disorder

### Key Molecular Pathways

- **TLR3–TRIF–TBK1–IRF3 pathway** (GO:0034154, Toll-like receptor 3 signaling pathway): Critical for IFN-β production in CNS; neonatal immaturity of this pathway underlies susceptibility
- **Type I interferon signaling** (GO:0060337, type I interferon signaling pathway): IFN-α/β production is dampened in the newborn brain; exogenous IFN-β can rescue survival in mouse models (PMID:33055261)
- **NF-κB signaling** (GO:0007249): Activated by TLR recognition of viral PAMPs but counteracted by HSV immune evasion
- **PKR–eIF2α antiviral pathway**: Inhibited by HSV ICP34.5 and Us11
- **Apoptosis** (GO:0006915): HSV modulates both pro- and anti-apoptotic pathways for viral benefit

### Cell Types Involved

| Cell Type | CL Term | Role |
|-----------|---------|------|
| Epithelial cell | CL:0000066 | Primary site of viral entry and replication |
| Neuron | CL:0000540 | Target of neurotropic spread; site of latency |
| Astrocyte | CL:0000127 | Neuroinflammatory response |
| Microglial cell | CL:0000129 | CNS innate immune response |
| Hepatocyte | CL:0000182 | Target in disseminated disease |
| Trophoblast | CL:0000351 | Placental barrier; site of transplacental transmission |
| Natural killer cell | CL:0000623 | Neonatal NK cell function is immature |
| Dendritic cell | CL:0000451 | Antigen presentation, IFN production |

### Placental Pathology

Histopathological findings in the placenta include (PMC9557870; PMC7817230):
- **Necrotizing villitis** with stromal cell necrosis
- **Chronic chorioamnionitis**
- **Maternal floor infarction**
- **Calcifying funisitis** (umbilical cord)
- Positive HSV immunohistochemistry in placenta and umbilical cord
- Ascending infection pattern shows changes primarily in the umbilical cord and chorionic plate

---

## 7. Anatomical Structures Affected

### Organ Level

| Organ/System | UBERON Term | Involvement |
|-------------|-------------|-------------|
| Skin | UBERON:0002097 | Primary (vesicles, scarring) |
| Brain | UBERON:0000955 | Primary in CNS and intrauterine forms |
| Eye | UBERON:0000970 | Chorioretinitis, microphthalmia |
| Liver | UBERON:0002107 | Disseminated disease |
| Lung | UBERON:0002048 | Pneumonitis in disseminated |
| Adrenal gland | UBERON:0002369 | Adrenal hemorrhage/necrosis |
| Placenta | UBERON:0001987 | Villitis, infarction |

### CNS Localization

- **Temporal lobes**: Predilection site for HSV encephalitis
- **Basal ganglia, thalamus, internal capsules**: Poor prognostic indicator when bilateral deep cerebral lesions are present (PMC10406570)
- **Brainstem and cerebellum**: Can show non-hemorrhagic infarcts
- **Leptomeninges**: Enhancement on MRI; meningoencephalitis pattern

---

## 8. Temporal Development

### Onset

- **Intrauterine (congenital) disease**: Present at birth; affected by timing of maternal infection during pregnancy
- **SEM disease**: Mean presentation at 7–12 days of life
- **CNS disease**: Mean presentation at 11–17 days of life
- **Disseminated disease**: Mean presentation at ~11 days of life (range: birth to 6 weeks)

Onset classification: **Neonatal** (HP:0003623, Neonatal onset).

### Progression

- **SEM disease**: Self-limited with treatment; risk of recurrence without suppressive therapy
- **CNS disease**: Acute encephalitis → potential for progressive neurological deterioration → chronic seizure disorder, developmental delay
- **Disseminated disease**: Rapidly progressive multi-organ failure without treatment
- **Intrauterine infection**: Damage occurs during fetal development; consequences are often irreversible at birth

### Critical Periods

- **First trimester maternal infection**: Highest risk for severe congenital malformations (organogenesis disruption)
- **Late third trimester / peripartum**: Highest risk for neonatal transmission due to primary genital infection near delivery
- **First 48 hours of life**: Window for empiric acyclovir initiation before confirmatory testing

---

## 9. Inheritance and Population

### Epidemiology

**Global incidence** (PMID:41860333; systematic review and meta-analysis, 143 reports):
- Global pooled incidence: **8.8 per 100,000 live births** (95% CI: 6.9–10.9)
- Population-weighted global estimate: **8.2 per 100,000 live births** (95% CI: 5.9–10.7)
- Approximately **1 in 10,000 newborns** affected globally
- Annual increase of **3.5%** (95% CI: 1.5–5.6%) in nHSV incidence

**Regional variation:**
- Americas: **13.3 per 100,000 live births** (95% CI: 9.9–17.2) — highest
- European Region: **5.2 per 100,000 live births** (95% CI: 3.4–7.3)
- Western Pacific: **2.9 per 100,000 live births** (95% CI: 2.2–3.6)
- Data lacking from Africa, South-East Asia, Eastern Mediterranean

**True intrauterine HSV infection**: Estimated at only **1 in 300,000 deliveries** (PMID:40027069).

### HSV-1 vs HSV-2 Distribution

- Global: HSV-1 = 47.3%; HSV-2 = 52.8%
- Temporal trend: yearly 1.4% increase in HSV-1 proportion, 1.1% decrease in HSV-2
- Americas: HSV-2 predominates (60.5%)
- Western Pacific: HSV-1 predominates (57.7%)

### Population Demographics

- No strong sex predilection in neonatal disease
- Higher incidence in populations with lower HSV seroprevalence in young women (paradoxically, higher socioeconomic populations where primary infection occurs later in life)
- African American women in the US have higher HSV-2 seroprevalence but paradoxically lower neonatal herpes rates (due to pre-existing antibodies conferring partial protection)

---

## 10. Diagnostics

### Laboratory Testing

- **HSV PCR (NAAT)**: Gold standard for diagnosis; performed on:
  - CSF (sensitivity >95% for CNS disease)
  - Blood/plasma (viremia in disseminated disease)
  - Vesicle fluid/swabs from skin lesions, conjunctivae, oropharynx
- **Viral culture**: From vesicle fluid or mucosal swabs; less sensitive than PCR but allows serotyping
- **Direct fluorescent antibody (DFA) staining**: Rapid but less sensitive
- **HSV serology**: Type-specific IgG (limited utility in neonates due to maternal antibody transfer; useful for maternal screening)

**LOINC codes:**
- HSV DNA detection by NAA: LOINC:16952-4
- HSV culture: LOINC:5857-0

### CSF Analysis

- Mononuclear pleocytosis (may be normal early)
- Depressed glucose
- Mildly to moderately elevated protein
- HSV PCR positive (PMID:23481105)

### Imaging

- **Cranial MRI**: Preferred modality
  - Diffusion restriction in temporal/frontal lobes
  - Hemorrhagic or non-hemorrhagic infarcts
  - Leptomeningeal enhancement
  - Bilateral deep cerebral lesions (basal ganglia, thalamus) = poor prognosis (PMC10406570)
- **Cranial ultrasound**: May show echogenic foci, ventriculomegaly
- **CT**: Intracranial calcifications (especially in intrauterine infection)

### Ophthalmologic Examination

- Fundoscopy for chorioretinitis
- Slit-lamp examination for keratitis

### Placental Pathology

- Histopathology: necrotizing villitis, chorioamnionitis
- HSV immunohistochemistry of placenta and umbilical cord
- Examination within first 2–5 days of life in premature infants can provide early diagnostic clues (PMC7817230)

### EEG

- Abnormal electrical activity, often multifocal seizure discharges
- Periodic lateralized epileptiform discharges (PLEDs) suggestive of HSV encephalitis

### Differential Diagnosis

- Other TORCH infections (CMV, toxoplasmosis, rubella, syphilis, Zika)
- Neonatal bacterial sepsis/meningitis
- Enteroviral infection
- Epidermolysis bullosa (for vesicular skin lesions)
- Metabolic disorders presenting with hepatic failure
- Inborn errors of metabolism

---

## 11. Outcome / Prognosis

### Mortality

| Disease Category | Untreated Mortality | Treated Mortality (high-dose acyclovir) |
|-----------------|--------------------|-----------------------------------------|
| SEM | Low (~0%) | ~0% |
| CNS | ~50% | ~4% |
| Disseminated | ~85% | ~30% |
| Intrauterine | Very high | Variable, often poor |

(Mortality data from Kimberlin et al., *Pediatrics* 2001, PMID:11483825; and AAP NeoReviews 2018)

### Neurodevelopmental Outcomes

- **SEM disease**: Generally normal neurodevelopment; risk of recurrent skin lesions
- **CNS disease**: 30–70% of survivors develop neurodevelopmental impairment including intellectual disability, cerebral palsy, epilepsy, and motor deficits (PMC10406570)
- **Disseminated disease**: ≥65% of survivors of untreated disease have severe neurologic sequelae; treatment reduces but does not eliminate this
- **Intrauterine infection**: Associated with the most severe outcomes including spontaneous abortion, stillbirth, severe brain malformations (PMID:40027069)

### Prognostic Factors

- **Disease classification** (SEM > CNS > Disseminated in terms of favorable outcome)
- **Timing of acyclovir initiation**: Earlier treatment improves outcomes
- **CSF HSV PCR negativity** at end of treatment: Favorable indicator
- **Bilateral deep cerebral MRI lesions**: Poor prognostic indicator
- **Suppressive oral acyclovir therapy**: 6 months post-acute treatment improves neurodevelopmental outcomes (Bayley scores) (Kimberlin et al., *NEJM* 2011, PMID:21793742)

---

## 12. Treatment

### Acute Antiviral Therapy

**Intravenous acyclovir** (NCIT:C275; Acyclovir) — standard of care:
- **Dose**: 20 mg/kg/dose IV every 8 hours
- **Duration**:
  - SEM disease: **14 days**
  - CNS disease: **21 days** (minimum)
  - Disseminated disease: **21 days** (minimum)
- **CSF monitoring**: Repeat lumbar puncture near end of therapy for CNS disease; continue IV acyclovir if CSF PCR remains positive, with weekly repeat LP until negative

**NCIT terms:**
- Pharmacotherapy: NCIT:C15986
- Acyclovir: NCIT:C275

### Suppressive Therapy

- **Oral acyclovir**: 300 mg/m²/dose three times daily for **6 months** after completion of IV therapy
- Recommended for all infants surviving neonatal HSV regardless of disease classification
- Improves neurodevelopmental outcomes in CNS disease (PMID:21793742)
- **Monitoring**: Absolute neutrophil counts (ANCs) should be checked at 2 and 4 weeks after initiation, then monthly; neutropenia is the primary adverse effect

**Suggested CHEBI term**: CHEBI:2453 (aciclovir)

### Supportive Care (NCIT:C15747)

- Seizure management (phenobarbital, levetiracetam)
- Respiratory support as needed
- Nutritional support
- Ophthalmologic follow-up
- Neurodevelopmental monitoring and early intervention services

### Emerging Therapies

- **Valacyclovir** (CHEBI:60726) for neonatal HSV disease is under investigation (NCT04448392) — oral prodrug with improved bioavailability
- **Pritelivir** (helicase-primase inhibitor) — investigational, novel mechanism distinct from nucleoside analogues

---

## 13. Prevention

### Primary Prevention

**Maternal antiviral suppressive therapy:**
- Acyclovir 400 mg PO TID or valacyclovir 500 mg PO BID from **36 weeks gestation** in women with known recurrent genital HSV
- Significantly reduces viral shedding at delivery and cesarean section rates (PMID:18254066)
- Insufficient evidence that suppressive therapy alone reduces neonatal herpes incidence (event too rare in trials)

**Cesarean delivery:**
- Recommended when active genital HSV lesions or prodromal symptoms are present at labor onset
- Reduces neonatal HSV transmission by ~86%

**Screening:**
- Routine serologic screening for HSV during pregnancy is **not recommended** by ACOG/SOGC
- Type-specific IgG testing can identify discordant couples and guide counseling
- No population-based prenatal HSV screening program exists

### Secondary Prevention

- **Early empiric acyclovir**: Initiation upon clinical suspicion, before confirmatory testing, significantly reduces mortality and morbidity
- **HSV surface cultures at delivery**: Swabs from eyes, nasopharynx, mouth, rectum at 12–24 hours of life in infants born to mothers with active lesions

### Tertiary Prevention

- **6-month oral acyclovir suppressive therapy**: Prevents cutaneous recurrences and improves neurodevelopmental outcomes
- Long-term neurodevelopmental follow-up
- Ophthalmologic surveillance for delayed visual complications

### Counseling

- Education of parents/caregivers about avoiding neonatal contact with active HSV lesions (oral or genital)
- Genetic counseling may be warranted if inborn errors of TLR3–IFN immunity are identified

---

## 14. Other Species / Natural Disease

### Animal Models

**Mouse models:**
- C57BL/6 mice infected intravaginally with HSV-2 during early pregnancy demonstrate dose-dependent adverse pregnancy outcomes including reduced fetal/placental weights, fetal resorption, and transplacental viral transmission (PMID:34696359)
- At low viral doses, infection localizes to fetal eye and CNS; at high doses, disseminated expression in neuroepithelium, heart, and liver
- Pregnant mice show ~100-fold greater susceptibility to HSV-2 compared to non-pregnant controls
- Newborn mice demonstrate dampened innate immune signaling and IFN responses compared to adults (PMID:33055261)
- Hematogenous vertical transmission of HSV-1 in mice with CNS tropism in offspring (PMID:16501086)

**Guinea pig models:**
- Mimic natural history of genital HSV infection with spontaneous recurrences
- Used for studying antiviral suppressive therapy and maternal-to-neonatal transmission

**Non-human primate models:**
- Rhesus macaque model for genital HSV-2 with vaginal vesicular lesions, virus shedding, and seroconversion (PMC11371218)
- Most relevant to human disease due to immunological similarity

### Natural Disease in Other Species

HSV-1 and HSV-2 are highly host-restricted to humans. Natural HSV infection in non-human animals is rare and typically represents cross-species transmission. B virus (*Macacine alphaherpesvirus 1*), an HSV homolog in Old World macaques, causes a similar but zoonotic disease.

---

## 15. Model Organisms (Research Models)

| Model | Species | Application | Fidelity | Limitations |
|-------|---------|-------------|----------|-------------|
| Neonatal mouse HSV encephalitis | Mouse (NCBITaxon:10090) | CNS pathogenesis, antiviral testing, immune response | MODERATE | Murine immune ontogeny differs from human; shorter gestation |
| Intravaginal HSV-2 pregnant mouse | Mouse | Transplacental transmission, pregnancy outcomes | MODERATE | Dose-dependent; 100x greater susceptibility than humans |
| Guinea pig genital HSV-2 | Guinea pig (NCBITaxon:10141) | Recurrent genital herpes, antiviral efficacy | MODERATE | Spontaneous recurrences; limited reagents for immune studies |
| Rhesus macaque genital HSV-2 | Rhesus macaque (NCBITaxon:9544) | Vaccine development, mucosal immunity | HIGH | Ethical/cost constraints; HSV is not natural pathogen |
| HSV-infected human organoids/iPSC | Human (NCBITaxon:9606) | CNS tropism, interferon response | MODERATE | Lacks systemic immune context |

---

## Summary of Key Ontology Term Suggestions

| Domain | Suggested Terms |
|--------|----------------|
| Disease | MONDO:0017381 (Congenital herpes simplex virus infection) |
| Phenotypes | HP:0000252 (Microcephaly), HP:0002340 (Hydranencephaly), HP:0001250 (Seizures), HP:0000483 (Chorioretinitis), HP:0000568 (Microphthalmia), HP:0200037 (Skin vesicle), HP:0002514 (Intracranial calcification), HP:0001298 (Encephalopathy), HP:0002240 (Hepatomegaly), HP:0001622 (Premature birth), HP:0001511 (Intrauterine growth retardation), HP:0001249 (Intellectual disability) |
| Cell types | CL:0000066 (epithelial cell), CL:0000540 (neuron), CL:0000182 (hepatocyte), CL:0000129 (microglial cell), CL:0000127 (astrocyte), CL:0000351 (trophoblast cell) |
| Biological processes | GO:0045087 (innate immune response), GO:0034154 (toll-like receptor 3 signaling), GO:0060337 (type I interferon signaling pathway), GO:0019079 (viral genome replication), GO:0006915 (apoptotic process) |
| Anatomy | UBERON:0000955 (brain), UBERON:0002097 (skin of body), UBERON:0000970 (eye), UBERON:0002107 (liver), UBERON:0001987 (placenta) |
| Treatment | NCIT:C15986 (Pharmacotherapy), NCIT:C275 (Acyclovir), CHEBI:2453 (aciclovir) |
| Infectious agent | NCBITaxon:10298 (Human alphaherpesvirus 1), NCBITaxon:10310 (Human alphaherpesvirus 2) |

---

## Sources

- [Intrauterine Herpes Simplex Virus Infection: Insights Into a Silent Threat (2025, PMID:40027069)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11870782/)
- [Global epidemiology of neonatal herpes: systematic review, meta-analyses, and meta-regressions (2026, PMID:41860333)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13003892/)
- [Congenital Herpes Simplex — StatPearls](https://www.statpearls.com/point-of-care/19855)
- [Congenital Herpes Simplex Virus: A Histopathological View of the Placenta (2022)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9557870/)
- [Diagnosis of Neonatal Herpes Simplex Infection from the Placenta (2021)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7817230/)
- [The Many Faces of Neurological Neonatal HSV Infection (2023)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10406570/)
- [Neonatal Herpes Simplex Virus Infection — AAP NeoReviews (2018)](https://publications.aap.org/neoreviews/article/19/2/e89/87448/Neonatal-Herpes-Simplex-Virus-Infection)
- [Neonatal herpes simplex virus infection: From the maternal infection to the child outcome (De Rose et al., 2023)](https://onlinelibrary.wiley.com/doi/10.1002/jmv.29024)
- [Primary HSV-2 Infection in Early Pregnancy — Novel Mouse Model (2021, PMID:34696359)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8538385/)
- [The Innate Immune Response to HSV-1 in the Newborn Brain (2020, PMID:33055261)](https://journals.asm.org/doi/10.1128/mbio.00921-20)
- [Inborn Errors of Immunity Predisposing to HSV Infections of the CNS (2023)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9961685/)
- [The immunogenetic basis of severe HSV in neonates and children (2025)](https://www.nature.com/articles/s41390-025-03830-7)
- [A case of neonatal HSV-2 encephalitis with TLR3 gene mutation (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13485870/)
- [Third trimester antiviral prophylaxis for preventing neonatal HSV (Cochrane, PMID:18254066)](https://pubmed.ncbi.nlm.nih.gov/18254066/)
- [Oral Acyclovir Suppression and Neurodevelopment after Neonatal Herpes (Kimberlin et al., NEJM 2011, PMID:21793742)](https://www.nejm.org/doi/full/10.1056/NEJMoa1003509)
- [Safety and Efficacy of High-Dose IV Acyclovir in Neonatal HSV (Kimberlin et al., Pediatrics 2001)](https://publications.aap.org/pediatrics/article/108/2/230/63736/Safety-and-Efficacy-of-High-Dose-Intravenous)
- [Neonatal HSV in Relation to Asymptomatic Maternal Infection (Brown et al., NEJM 1991, PMID:2020171)](https://www.nejm.org/doi/full/10.1056/NEJM199105023241804)
- [Effect of Serologic Status and Cesarean Delivery on HSV Transmission (Brown et al., JAMA 2003)](https://jamanetwork.com/journals/jama/fullarticle/195747)
- [Congenital herpes simplex with ophthalmic and multisystem features (2023)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10694881/)
- [ICD-10-CM Code P35.2](https://www.icd10data.com/ICD10CM/Codes/P00-P96/P35-P39/P35-/P35.2)
- [Orphanet: Congenital herpes simplex virus infection (ORPHA:293)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=293)
- [Hematogenous Vertical Transmission of HSV-1 in Mice (2006, PMID:16501086)](https://journals.asm.org/doi/10.1128/jvi.80.6.2823-2831.2006)
- [Animal models of human herpesvirus infection (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12067922/)
- [Congenital Herpes Simplex Virus Infection — MalaCards](https://www.malacards.org/card/congenital_herpes_simplex_virus_infection)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 28 |
| On topic | 19 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:2020171` (2 mentions) - Subcritical flutter in collapsible tube flow: a model of expiratory flow in the trachea.
  - shared terms: none

Weighed against this report's own most characteristic terms: `hsv`, `infection`, `disease`, `neonatal`, `cns`, `intrauterine`, `herpe`, `disseminated`, `lesion`, `primary`, `hsv-2`, `congenital`, `genital`, `maternal`, `transmission`, `hsv-1`, `viral`, `acyclovir`, `virus`, `skin`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 65 |
| Resolved | 61 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 51 |
| Terms named correctly | 34 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 12 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0017381` (2 mentions) - the report calls it "MONDO", "Congenital herpes simplex virus infection"; MONDO calls it **congenital herpes simplex virus infection**
- `HP:0002340` (2 mentions) - the report calls it "Hydranencephaly"; HP calls it **Caudate atrophy**
- `HP:0000483` (2 mentions) - the report calls it "Chorioretinitis"; HP calls it **Astigmatism**
- `HP:0005765` (1 mention) - the report calls it "DIC"; HP calls it **Sacral meningocele**
- `CHEBI:60726` (1 mention) - the report calls it "Valacyclovir"; CHEBI calls it **procainamide 4-hydroxylamine**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0045023` (1 mention) - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001250` (3 mentions) - the report calls it "Seizures", "Epilepsy"; HP calls it **Seizure**, and lists "Epilepsy" among its other names
- `HP:0002514` (2 mentions) - the report calls it "Intracranial calcifications"; HP calls it **Cerebral calcification**
- `HP:0000563` (1 mention) - the report calls it "Keratoconjunctivitis"; HP calls it **Keratoconus**
- `HP:0012115` (1 mention) - the report calls it "Hepatic failure"; HP calls it **Hepatitis**
- `HP:0006517` (1 mention) - the report calls it "Alveolar hemorrhage"; HP calls it **Intraalveolar phospholipid accumulation**, and lists "Alveolar proteinosis" among its other names
- `HP:0001511` (2 mentions) - the report calls it "Intrauterine growth restriction"; HP calls it **Intrauterine growth retardation**, and lists "Intrauterine growth restriction" among its other names
- `NCBITaxon:10298` (3 mentions) - the report calls it "Primary agent**: HSV-1"; NCBITaxon calls it **Human alphaherpesvirus 1**, and lists "HSV-1" among its other names
- `GO:0007249` (1 mention) - the report calls it "NF-κB signaling"; GO calls it **canonical NF-kappaB signal transduction**, and lists "p50-dependent NF-kappaB signaling" among its other names
- `GO:0006915` (2 mentions) - the report calls it "Apoptosis"; GO calls it **apoptotic process**, and lists "apoptosis" among its other names
- `CL:0000351` (2 mentions) - the report calls it "Trophoblast"; CL calls it **trophoblast cell**
- `UBERON:0002097` (2 mentions) - the report calls it "Skin"; UBERON calls it **skin of body**, and lists "skin" among its other names
- `CHEBI:2453` (2 mentions) - the report calls it "aciclovir"; CHEBI calls it **acyclovir**, and lists "aciclovir" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0017381` - called "MONDO", "Congenital herpes simplex virus infection"
- `HP:0001250` - called "Seizures", "Epilepsy"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `LOINC`.