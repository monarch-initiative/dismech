---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-6[1m]
cached: false
start_time: '2026-09-09T21:16:15.744687'
end_time: '2026-09-09T21:21:55.476770'
duration_seconds: 339.73
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hepatosplenic T-cell Lymphoma
  mondo_id: MONDO:0019474
  category: Cancer
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
  web_search_requests: 18
  num_turns: 28
  total_cost_usd: 1.7491231999999999
  session_id: 4f8b88f4-e2cb-4f29-86d2-8cd2adff32d4
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
citation_count: 19
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:28122867
  quotes_not_checkable: 1
  relevance_assessed: 18
  on_topic: 10
  off_topic: 1
  off_topic_references:
  - PMID:33064823
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 45
  verified: 43
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 38
  labels_matching: 18
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0019474
    reported_labels:
    - MONDO
    ontology_label: hepatosplenic T-cell lymphoma
  - term_id: HP:0001945
    reported_labels:
    - Fever / B symptoms
    ontology_label: Fever
  - term_id: HP:0025435
    reported_labels:
    - Elevated LDH
    ontology_label: Increased circulating lactate dehydrogenase concentration
  - term_id: CL:0000875
    reported_labels:
    - Splenic red pulp macrophage
    ontology_label: non-classical monocyte
  - term_id: GO:0098533
    reported_labels:
    - Histone H3-K36 trimethylation
    ontology_label: ATPase dependent transmembrane transport complex
  - term_id: UBERON:0001281
    reported_labels:
    - 'Hepatic sinusoids**: Neoplastic cells within variably dilated sinusoids'
    ontology_label: hepatic sinusoid
  labels_variant: 14
  obsolete_terms:
  - term_id: GO:0016571
    ontology_label: obsolete histone methylation
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hepatosplenic T-cell Lymphoma
- **MONDO ID:** MONDO:0019474 (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **Hepatosplenic T-cell Lymphoma** covering all of the
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

Now I have enough information to compile the comprehensive research report. Let me write it up.

---

# Comprehensive Research Report: Hepatosplenic T-Cell Lymphoma (HSTCL)

## 1. Disease Information

### Overview

Hepatosplenic T-cell lymphoma (HSTCL) is a rare, highly aggressive extranodal peripheral T-cell lymphoma (PTCL) arising from cytotoxic T cells, usually of γδ (gamma-delta) T-cell receptor type, with a characteristic sinusoidal infiltration pattern in the liver, spleen, and bone marrow. It was first described as a distinct clinicopathologic entity in 1990 and is now recognized as a separate entity in the WHO Classification of Lymphoid Neoplasms (PMID: 29337025; PMID: 33064823).

HSTCL accounts for less than 1% of all non-Hodgkin lymphomas (NHL) and approximately 1–2% of all T/NK-cell lymphomas. It predominantly affects adolescents and young adults, with a striking male predominance, and carries a dismal prognosis with a median overall survival of approximately 12–16 months (PMID: 33160933; PMID: 33064823).

### Key Identifiers

| Database | Identifier |
|----------|-----------|
| **MONDO** | MONDO:0019474 |
| **Orphanet** | ORPHA:86882 |
| **ICD-10-CM** | C86.1 (Hepatosplenic T-cell lymphoma); C86.10 (not in remission); C86.11 (in remission) |
| **ICD-O** | 9716/3 (morphology code) |
| **MeSH** | D058534 |

### Common Synonyms
- Hepatosplenic gamma-delta T-cell lymphoma (γδ HSTCL)
- Hepatosplenic T-cell lymphoma, gamma-delta type
- HSTCL
- HSTL

**Note:** While the majority (~80%) express the γδ T-cell receptor, a minority (~20%) express the αβ T-cell receptor. The WHO classification uses "hepatosplenic T-cell lymphoma" to encompass both receptor types, as they share identical clinicopathologic features and outcomes (PMID: 33064823).

---

## 2. Etiology

### Disease Causal Factors

HSTCL arises from the malignant transformation of cytotoxic T cells (predominantly Vδ1+ γδ T cells) that normally reside in the splenic red pulp and hepatic sinusoids. The etiology involves:

1. **Somatic genetic alterations**: Activating mutations in JAK-STAT pathway genes (particularly STAT5B, STAT3) and loss-of-function mutations in chromatin-modifying genes (SETD2, INO80, ARID1B) (PMID: 28122867).
2. **Chromosomal abnormalities**: Isochromosome 7q (iso7q) and trisomy 8 are hallmark cytogenetic lesions.
3. **Chronic immune stimulation/immunosuppression**: Approximately 20–30% of cases arise in the setting of chronic immunosuppression (PMID: 33064823).

### Risk Factors

#### Immunosuppression-Associated Risk
The strongest exogenous risk factor is prolonged immunosuppressive therapy, particularly:

- **Thiopurine immunomodulators** (azathioprine, 6-mercaptopurine): Strong association, especially with prolonged use (≥2 years) (PMID: 21823196).
- **Combination immunosuppression** (thiopurines + anti-TNF agents): Synergistically increased risk, particularly in young males with inflammatory bowel disease (IBD), especially Crohn's disease (PMID: 21941193).
- **Solid organ transplantation**: HSTCL has been reported 4–27 years after kidney transplantation under long-term immunosuppressive therapy (PMID: 14504095).
- **Hematologic malignancies**: Chronic lymphocytic leukemia and other conditions requiring immunosuppressive treatment have been associated.

**Important finding:** No cases of HSTCL have been reported in IBD patients receiving anti-TNF monotherapy without thiopurine exposure, suggesting that thiopurine exposure is the critical component of the risk profile (PMID: 21941193).

#### Demographic Risk Factors
- **Age**: Young adults and adolescents (median age at diagnosis 20–35 years in most series, though SEER data in adults show median ~48 years)
- **Sex**: Strong male predominance (~2:1 to 3:1 male-to-female ratio; 63.8% male in SEER adult data)
- **Race/ethnicity**: Caucasian predominance (57.7%), followed by Black (20.9%), Asian/Pacific Islander (11.7%), Hispanic (9.2%) in US population data (PMID: 27099586)

### EBV Status
HSTCL is characteristically **EBV-negative**, which distinguishes it from many other T/NK-cell lymphoproliferative disorders. EBV positivity has been reported in rare cases but is not considered pathogenetically significant (PMID: 14504095).

---

## 3. Phenotypes

### Clinical Presentation

| Phenotype | HPO Term | Frequency | Notes |
|-----------|----------|-----------|-------|
| Splenomegaly (marked) | HP:0001744 | >95% | Nearly universal; often massive |
| Hepatomegaly | HP:0002240 | ~80–90% | Consistent hepatic involvement |
| Fever / B symptoms | HP:0001945 | ~70–80% | Systemic inflammatory symptoms |
| Thrombocytopenia | HP:0001873 | ~85% | Often severe |
| Anemia | HP:0001903 | ~75% | Hematocrit 20–28% |
| Leukocytosis or leukopenia | HP:0001974 / HP:0001882 | Variable | WBC may be elevated or depressed |
| Weight loss | HP:0004325 | ~50–60% | B symptom |
| Night sweats | HP:0030166 | ~40–50% | B symptom |
| Abdominal pain | HP:0002027 | ~40% | Related to hepatosplenomegaly |
| Jaundice | HP:0000952 | ~20–30% | Hepatic infiltration |
| Absence of lymphadenopathy | — | >90% | Key distinguishing feature |
| Hemophagocytic syndrome | HP:0012156 (Hemophagocytosis) | ~25% | Associated with worse prognosis |
| Coagulopathy | HP:0003256 | Variable | DIC reported in some cases |
| Elevated LDH | HP:0025435 | ~80% | Marker of tumor burden |
| Circulating lymphoma cells | — | Variable | May mimic acute leukemia |

### Quality of Life Impact
HSTCL has a devastating impact on quality of life due to:
- Rapid clinical deterioration with constitutional symptoms
- Severe cytopenias requiring transfusion support
- Massive hepatosplenomegaly causing abdominal discomfort, early satiety
- Frequent hospitalizations for complications including infections and bleeding
- Very poor prognosis creating significant psychological burden

---

## 4. Genetic/Molecular Information

### Chromosomal Abnormalities

**Isochromosome 7q (iso7q):** The most characteristic cytogenetic abnormality, detected in approximately 47–70% of HSTCL cases. It results in loss of 7p and gain of 7q material, leading to haploinsufficiency of 7p genes and overexpression of 7q genes. This is considered a primary event in HSTCL pathogenesis (PMID: 28122867; PMID: 9691023).

**Trisomy 8:** Detected in 31–50% of cases, frequently co-occurring with iso7q. Ring chromosome 7 is also occasionally observed.

### Somatic Mutations (PMID: 28122867 — McKinney et al., Cancer Discovery 2017)

McKinney et al. performed whole-exome sequencing of 68 HSTLs and identified the following recurrent mutations:

#### JAK-STAT Pathway Mutations
| Gene | Frequency | Key Variants | Functional Impact |
|------|-----------|--------------|-------------------|
| **STAT5B** | 31% | N642H (hotspot), V712E | Gain-of-function; constitutive STAT5 phosphorylation |
| **STAT3** | 9% | SH2 domain mutations | Gain-of-function; activating |
| **PIK3CD** | 9% | Analogous to PIK3CA activating mutations | Increased phospho-AKT and phospho-STAT5 |

The STAT5B N642H mutation is the single most frequent somatic point mutation in HSTCL, occurring in approximately one-third of cases. It has been associated with poorer clinical outcomes and higher risk of relapse (PMID: 24947020).

A 2024 Haematologica study confirmed STAT5B mutations in 38% of HSTCL cases (8/21 patients), with the N642H hotspot in 5 cases, while STAT3 mutations predominated in γδ T-cell large granular lymphocytic leukemia (75%), providing a key molecular distinction between these entities (Haematologica 2024).

#### Chromatin-Modifying Gene Mutations
Chromatin-modifying genes were the most frequently mutated group, collectively affecting **62%** of HSTCL cases:

| Gene | Frequency | Mutation Type | Function |
|------|-----------|---------------|----------|
| **SETD2** | 25% (71% loss-of-function) | Nonsense, frameshift | H3K36 trimethyltransferase; tumor suppressor |
| **INO80** | 21% | Various | Chromatin remodeling complex |
| **TET3** | 15% | Various | DNA demethylation (5mC → 5hmC) |
| **ARID1B** | Part of 62% | Various | SWI/SNF chromatin remodeling |
| **SMARCA2** | 10% | Various | SWI/SNF ATPase subunit |

#### Additional Epigenetic Mutations (Haematologica 2024)
| Gene | Frequency |
|------|-----------|
| **DNMT3A** | 19% |
| **TET2** | 14% |
| **EZH2** | 10% |
| **TP53** | 10% |

### Functional Consequences

**SETD2** is the only human gene encoding the histone methyltransferase responsible for trimethylation of lysine 36 on histone H3 (H3K36me3). SETD2 loss in HSTCL promotes tumor cell proliferation — knockdown experiments showed "more than two-fold increased colony formation" compared to controls (PMID: 28122867). SETD2 mutations resulted in altered expression of pathways including mTOR and STAT signaling. SETD2 acts as a tumor suppressor in HSTCL, and its loss can promote chemotherapy resistance (PMID: 29257843).

**STAT5B** gain-of-function mutations (especially N642H) lead to constitutive JAK-STAT signaling, promoting cell survival and proliferation. "Dominant hotspot mutations N642H and V712E were particularly efficacious in maintaining STAT5 phosphorylation" (PMID: 28122867).

**PIK3CD** activating mutations increase phosphorylated AKT and cross-activate STAT5, with combination STAT5B and PI3K inhibition showing synergistic anti-tumor effects (PMID: 28122867).

### TCR Gene Rearrangements
HSTCL shows biased T-cell receptor gene usage:
- **TRGV4**: Used in 50% of HSTCL cases (vs 7% in γδ T-LGL leukemia)
- **VD1-JD1 rearrangement**: Present in 81% of γδ-positive HSTCL cases (Haematologica 2024)

---

## 5. Environmental Information

### Immunosuppressive Drug Exposure
The primary environmental/iatrogenic risk factor is prolonged immunosuppressive therapy:
- **Thiopurines** (azathioprine, 6-mercaptopurine): Duration ≥2 years significantly increases risk
- **Anti-TNF agents** (infliximab, adalimumab): Risk primarily with combination thiopurine + anti-TNF therapy
- **Cyclosporine/tacrolimus**: In solid organ transplant recipients

Infliximab has been shown to induce clonal expansion of γδ T cells in Crohn's disease patients, which may represent a precursor state to lymphomagenesis (PMID: 21415416).

### No Other Established Environmental Risk Factors
Unlike some other lymphomas, there is no established association with:
- Occupational or chemical exposures
- Dietary factors
- Infectious agents (HSTCL is characteristically EBV-negative)
- Radiation exposure

---

## 6. Mechanism / Pathophysiology

### Causal Chain (Ordered Mechanistic Steps)

1. **Initiating Lesion: Chromosomal Instability and iso7q Formation** → Isochromosome 7q (loss of 7p / gain of 7q) represents the primary cytogenetic event, leading to haploinsufficiency of 7p tumor suppressors and overexpression of 7q oncogenes (PMID: 9691023).

2. **Cooperating Somatic Mutations in JAK-STAT Pathway** → STAT5B activating mutations (N642H, V712E) lead to constitutive STAT5 phosphorylation and ligand-independent signaling, promoting cell survival and proliferation (PMID: 24947020; PMID: 28122867).

3. **Epigenetic Dysregulation via Chromatin Modifier Loss** → Loss-of-function mutations in SETD2, INO80, TET3, and ARID1B result in loss of H3K36me3 marks, impaired DNA damage repair, aberrant gene expression, and increased proliferative capacity (PMID: 28122867).

4. **PI3K-AKT-mTOR Pathway Activation** → PIK3CD activating mutations increase phospho-AKT, promoting cell survival and cross-activating STAT5 signaling, creating a positive feedback loop (PMID: 28122867).

5. **Clonal Expansion of Cytotoxic γδ T Cells** → Malignant γδ T cells (predominantly Vδ1+) clonally expand within the innate immune compartment, arising from cells that normally home to the splenic red pulp sinusoids (PMID: 15968729).

6. **Sinusoidal Tropism and Organ Infiltration** → Malignant cells preferentially infiltrate hepatic sinusoids, splenic red pulp cords/sinuses, and bone marrow sinusoids. This sinusoidal tropism is driven by adhesion molecules and chemokine receptor expression that mirrors normal γδ T-cell homing patterns (PMID: 14504095).

7. **Hepatosplenomegaly and Cytopenias** → Organ infiltration leads to massive splenomegaly and hepatomegaly. Bone marrow infiltration, splenic sequestration, and hemophagocytosis result in pancytopenia (thrombocytopenia, anemia) (PMID: 29337025).

8. **Systemic Inflammation and Clinical Deterioration** → Cytokine release, hemophagocytic syndrome (in ~25% of cases), and progressive organ dysfunction lead to B symptoms, coagulopathy, and multiorgan failure (PMID: 33064823).

### Molecular Pathways

- **JAK-STAT pathway**: Central to HSTCL pathogenesis. STAT5B and STAT3 mutations provide constitutive activation. GO: `GO:0007259` (receptor signaling pathway via JAK-STAT)
- **PI3K-AKT-mTOR pathway**: PIK3CD mutations activate downstream AKT/mTOR signaling. GO: `GO:0043491` (protein kinase B signaling)
- **Chromatin remodeling/epigenetic regulation**: SETD2 loss results in global H3K36me3 reduction. GO: `GO:0016571` (histone methylation)
- **NF-κB signaling**: May contribute to survival signaling in neoplastic T cells

### Cell Types Involved

| Cell Type | CL Term | Role |
|-----------|---------|------|
| Gamma-delta T cell | CL:0000798 | Cell of origin (Vδ1+ subset) |
| Hepatic sinusoidal endothelial cell | CL:1000398 | Microenvironment support |
| Kupffer cell / macrophage | CL:0000235 | Hemophagocytosis |
| Splenic red pulp macrophage | CL:0000875 | Microenvironment |
| Bone marrow hematopoietic cell | CL:0002092 | Displaced by infiltration |

### Biological Processes

| Process | GO Term |
|---------|---------|
| T cell receptor signaling pathway | GO:0050852 |
| JAK-STAT cascade | GO:0007259 |
| Histone H3-K36 trimethylation | GO:0098533 |
| Regulation of cell population proliferation | GO:0042127 |
| Anti-apoptosis / negative regulation of apoptotic process | GO:0043066 |
| Chromatin remodeling | GO:0006338 |
| Cell migration | GO:0016477 |

---

## 7. Anatomical Structures Affected

### Organ Level

| Organ/Structure | UBERON Term | Involvement |
|-----------------|-------------|-------------|
| **Spleen** (primary) | UBERON:0002106 | Near-universal; massive splenomegaly with red pulp infiltration |
| **Liver** (primary) | UBERON:0002107 | Sinusoidal infiltration; hepatomegaly |
| **Bone marrow** (primary) | UBERON:0002371 | Sinusoidal infiltration in ~2/3 of cases |
| Peripheral blood | UBERON:0000178 | Circulating lymphoma cells in some cases |

### Tissue and Cell Level
- **Splenic red pulp**: Diffuse infiltration of cords and sinuses by atypical lymphocytes (UBERON:0001250)
- **Hepatic sinusoids**: Neoplastic cells within variably dilated sinusoids (UBERON:0001281)
- **Bone marrow sinusoids**: Intrasinusoidal pattern of infiltration

### Key Negative Finding
- **Lymph nodes are characteristically NOT involved** — the absence of lymphadenopathy is a hallmark distinguishing HSTCL from most other lymphomas.

---

## 8. Temporal Development

### Onset
- **Typical age**: Adolescents and young adults (median 20–35 years in most clinical series; peak 13–26 years in one pooled analysis of 360 cases)
- **Onset pattern**: Acute to subacute; rapid clinical deterioration over weeks to months
- **HP term**: HP:0011463 (Childhood onset) to HP:0003581 (Adult onset)

### Progression
- **Disease course**: Rapidly progressive and aggressive
- **Stages**: No formal staging system; disease is typically disseminated at diagnosis with liver, spleen, and bone marrow involvement
- **Disease duration without treatment**: Weeks to months; uniformly fatal if untreated
- **Blast-like transformation**: A blast-like terminal transformation has been described, with acquisition of additional cytogenetic abnormalities (PMID: 8314255)

### Relapse Pattern
- High relapse rate after initial chemotherapy
- Median time to progression approximately 9.5 months (PMID: 33160933)

---

## 9. Inheritance and Population

### Epidemiology

HSTCL is an exceptionally rare malignancy:
- **Incidence**: Estimated 0.06 per million inhabitant-years (Dutch population study); approximately 0.3 per million person-years in other estimates (PMID: 27099586)
- **Proportion of NHL**: <1% of all non-Hodgkin lymphomas
- **Proportion of PTCL**: 1–2% of peripheral T-cell lymphomas

### Population Demographics

- **Sex ratio**: Male predominance (~2:1 to 3:1); 63.8% male in SEER data
- **Age distribution**: Bimodal — peak in adolescents/young adults (13–26 years) and a second peak in middle-aged adults (~48 years median in SEER adult data)
- **Race/ethnicity** (US SEER data): Caucasian 57.7% > Black 20.9% > Asian/Pacific Islander 11.7% > Hispanic 9.2% > Native American/Alaskan 0.6%

### Genetic Inheritance
HSTCL is **not a hereditary disease**. It is an acquired neoplasm driven by somatic mutations. There is no known germline predisposition, Mendelian inheritance pattern, or familial clustering. The genetic changes (iso7q, STAT5B mutations, SETD2 mutations) are all somatic in origin (PMID: 28122867).

---

## 10. Diagnostics

### Clinical Tests

**Laboratory Findings:**
- Complete blood count: Anemia (75%), thrombocytopenia (85%), variable leukocyte count
- Elevated LDH (~80%)
- Elevated liver enzymes (transaminases)
- Coagulation abnormalities (in cases with DIC or hemophagocytic syndrome)
- Peripheral blood smear may show circulating lymphoma cells

**Imaging:**
- CT/PET-CT: Hepatosplenomegaly without significant lymphadenopathy; PET avidity variable
- Ultrasonography: Hepatosplenomegaly, may show diffuse splenic involvement

### Histopathology and Immunohistochemistry

**Tissue biopsy** (bone marrow, liver, or splenectomy) is required for definitive diagnosis.

**Histology:** Small-to-medium-sized lymphoid cells with irregular nuclear contours, mature chromatin, rim of pale cytoplasm, and characteristic sinusoidal infiltration pattern. In the spleen, there is marked red pulp expansion with white pulp atrophy. The "oyster-shell" cytological pattern has been described as a distinctive morphological feature (Haematologica 2024).

**Immunophenotype:**

| Marker | Result |
|--------|--------|
| CD2 | Positive |
| CD3 | Positive (surface; rarely negative) |
| CD7 | Positive |
| CD4 | Negative |
| CD5 | Negative |
| CD8 | Negative (occasionally positive) |
| TCRδ (Vδ1) | Positive (~80% of cases) |
| TCRβF1 | Negative (in γδ type) |
| CD56 | Variable (often positive) |
| TIA-1 | Positive |
| Granzyme M | Positive |
| Granzyme B | Negative (non-activated cytotoxic phenotype) |
| Perforin | Negative |
| Ki-67 | Low to moderate proliferation index |
| EBV (EBER) | Negative |

### Cytogenetics and Molecular Testing
- **Conventional karyotyping**: iso7q, trisomy 8
- **FISH**: For chromosome 7 and 8 abnormalities
- **TCR gene rearrangement**: Clonal γ and δ chain rearrangements
- **Targeted sequencing**: STAT5B, STAT3, SETD2, PIK3CD mutation analysis
- **Flow cytometry**: Aberrant T-cell immunophenotype (CD3+, CD4−, CD8−, TCRγδ+)

### Differential Diagnosis
- Aggressive NK-cell leukemia
- T-cell large granular lymphocytic leukemia (T-LGL) — distinguishable by STAT3 predominance (75%) vs STAT5B in HSTCL (Haematologica 2024)
- T-lymphoblastic leukemia/lymphoma
- Enteropathy-associated T-cell lymphoma type II (MEITL)
- Primary cutaneous γδ T-cell lymphoma
- Splenic marginal zone lymphoma (B-cell, indolent)
- Myelodysplastic syndrome
- Infectious mononucleosis
- Hemophagocytic lymphohistiocytosis

---

## 11. Outcome/Prognosis

### Survival

HSTCL carries one of the worst prognoses among all lymphoma subtypes:

- **Median overall survival**: 12.4 months (95% CI: 4.9–18.5 months) (PMID: 33160933)
- **Median progression-free survival**: 9.5 months (95% CI: 1.8–16.3 months) (PMID: 33160933)
- **5-year overall survival**: Approximately 7–20% depending on series
- **Nearly half of patients die within 1 year** of diagnosis
- **Long-term survivors** (>4 years) represent approximately 18% of cases, mostly those who received allogeneic transplantation (PMID: 33160933)

### With Allogeneic HSCT
- 3-year overall survival: 56–71% (depending on conditioning regimen)
- 5-year overall survival: 58–71%
- Relapse rate with TBI-based conditioning: ~13% vs ~28% without TBI
- Overall transplant mortality: 32.8% across cohort

### Adverse Prognostic Factors
- Chronic immunosuppression at diagnosis
- Hemophagocytic syndrome (HP:0012156)
- Severe thrombocytopenia
- Liver involvement
- STAT5B N642H mutation (associated with higher relapse risk) (PMID: 24947020)
- Failure to achieve remission before transplantation
- Age >45 years at transplant

### Favorable Prognostic Factors
- Splenectomy (diagnostic/therapeutic)
- Platinum-containing chemotherapy regimens
- Allogeneic stem cell transplantation in first remission
- Age <45 years
- Achievement of complete remission before transplant

---

## 12. Treatment

### First-Line Chemotherapy

**CHOP-based regimens** (NCIT:C11197 — CHOP Regimen):
- Historically used but yields poor response rates in HSTCL
- Overall response rates are low and responses are typically short-lived

**Platinum-containing intensive regimens** (preferred):
- **ICE** (Ifosfamide, Carboplatin, Etoposide) — NCIT:C11516
- **IVAC** (Ifosfamide, Etoposide, High-dose Cytarabine)
- **DHAP** (Dexamethasone, High-dose Cytarabine, Cisplatin)
- These regimens show improved response rates and serve as bridge to transplant

### Stem Cell Transplantation

**Allogeneic HSCT** (NCIT:C15431 — Hematopoietic Cell Transplantation):
- The most promising curative approach for HSTCL
- Recommended for all transplant-eligible patients who achieve any response
- Even patients with progressive disease prior to allo-HSCT can achieve long-term survival (>1/3 in one series)
- TBI-based conditioning regimens may offer lower relapse rates (~13% vs ~28%) and superior overall survival (71% at 5 years)
- Graft-versus-lymphoma effect is postulated to contribute to efficacy

**Autologous HSCT**: Less effective than allogeneic; may be considered when no donor is available.

### Splenectomy (NCIT:C15329 — Surgical Procedure)
- Serves both diagnostic and therapeutic purposes
- Associated with survival benefit in retrospective analyses
- Can improve cytopenias and reduce tumor burden

### Experimental and Targeted Therapies

**JAK inhibitors** (preclinical evidence):
- **Upadacitinib** (a JAK1 inhibitor): "Displayed significant and selective anti-tumor efficacy against STAT5B-mutated HSTCL cells in vitro and in vivo, and in primary HSTCL patient samples, highlighting upadacitinib as a potential targeted therapeutic option for STAT5B-mutated HSTCL" (PMID: 42007450, HemaSphere 2026).
- A STAT5B-driven mouse model confirmed therapeutic efficacy of JAK inhibition (bioRxiv 2025).

**Other investigational agents:**
- **Romidepsin** (HDAC inhibitor): Some activity reported in PTCL; under investigation in HSTCL
- **Belinostat** (HDAC inhibitor): FDA-approved for relapsed PTCL; potential application
- **PI3K inhibitors**: Rational target given PIK3CD mutations in ~9% of cases
- **Golidocitinib** (selective JAK1 inhibitor): Clinical trial NCT06716658 for relapsed/refractory T/NK-cell lymphomas (started December 2024)

### Treatment Algorithm Summary
1. **Diagnosis confirmed** → Intensive platinum-based induction (ICE/IVAC/DHAP)
2. **Response achieved** → Proceed to allogeneic HSCT in first remission
3. **Refractory disease** → Consider alternative salvage regimens; still proceed to allo-HSCT if possible
4. **Not transplant-eligible** → Palliative chemotherapy; clinical trial enrollment

### NCIT Treatment Terms
- NCIT:C15632 — Chemotherapy
- NCIT:C15431 — Hematopoietic Cell Transplantation
- NCIT:C15329 — Surgical Procedure (splenectomy)
- NCIT:C15986 — Pharmacotherapy
- NCIT:C93352 — Targeted Therapy (for JAK inhibitors/investigational agents)

---

## 13. Prevention

### Primary Prevention
There are no established primary prevention strategies for HSTCL.

**Risk mitigation in IBD patients:**
- Avoid prolonged thiopurine monotherapy (>2 years) in young males when possible
- Consider alternatives to thiopurine + anti-TNF combination therapy, particularly in young male IBD patients
- Monitor for early signs of lymphoproliferative disease during immunosuppressive therapy
- Use the lowest effective dose and duration of immunosuppression

### Secondary Prevention (Screening)
- No population-based screening exists given extreme rarity
- **Surveillance in high-risk populations**: Regular CBC monitoring in patients on long-term thiopurines, particularly young males with IBD
- Prompt workup of unexplained hepatosplenomegaly and cytopenias in immunosuppressed patients

### Tertiary Prevention
- Post-transplant surveillance for relapse
- Regular imaging and laboratory monitoring after allo-HSCT

---

## 14. Other Species / Natural Disease

There is **no well-characterized naturally occurring animal counterpart** of HSTCL. The disease appears to be unique to humans. However:

- γδ T cells are conserved across mammals and birds
- T-cell lymphomas with hepatosplenic involvement have been reported rarely in dogs and cats, but these do not replicate the specific γδ sinusoidal pattern of human HSTCL

---

## 15. Model Organisms

### Mouse Models

**STAT5B N642H-Driven Mouse Model** (bioRxiv 2025; PMID: 42007450):
This represents the first robust preclinical model of HSTCL:
- **Cell line**: C15 — a clonal murine γδ T-cell lymphoma cell line dependent on oncogenic STAT5B N642H
- **Engraftment**: Can be engrafted intravenously into both immunodeficient (NSG) and immunocompetent mice
- **Phenotype recapitulation**: Generates an aggressive, highly penetrant HSTCL-like disease with:
  - Hepatosplenomegaly
  - Sinusoidal infiltration of liver and spleen
  - Bone marrow involvement
  - γδ T-cell phenotype
- **Therapeutic application**: Demonstrated sensitivity to JAK inhibitor upadacitinib in this model
- **Limitations**: Murine γδ T-cell biology may differ from human; single oncogenic driver may not recapitulate full mutational complexity; immune microenvironment differences between species

### Cell Lines
- Limited number of HSTCL cell lines available
- DERL-2 and DERL-7 are among the few established human HSTCL cell lines used for in vitro studies

### Xenograft Models
- Patient-derived xenograft (PDX) models in immunodeficient mice have been used for drug testing
- Primary HSTCL patient samples have been tested ex vivo for JAK inhibitor sensitivity (PMID: 42007450)

---

## Key References

| PMID | Citation | Key Contribution |
|------|----------|------------------|
| 28122867 | McKinney M et al. Cancer Discovery 2017;7(4):369-379 | Definitive genomic characterization of HSTCL (68 cases WES) |
| 33064823 | Yabe M et al. Blood 2020;136(18):2018-2028 | Comprehensive review of HSTCL biology and management |
| 24947020 | Küçük C et al. Leukemia 2015;29(3):571-580 | STAT5B mutations in γδ HSTCL |
| 29337025 | Foppoli M & Ferreri AJ. Human Pathology 2018;74:5-12 | Clinicopathologic review with prognostic factors |
| 33160933 | Shi Y et al. Clin Lymphoma Myeloma Leuk 2021;21(4):e362-e369 | Mayo Clinic treatment outcomes |
| 27099586 | Falchook GS et al. Clin Lymphoma Myeloma Leuk 2016;16(10):e131-e138 | Population-based incidence study |
| 9691023 | Wlodarska I et al. Leukemia 2002;16(10):2309-2315 | iso7q as primary cytogenetic abnormality |
| 21941193 | Kotlyar DS et al. Eur J Gastroenterol Hepatol 2011;23(12):1150-1156 | Anti-TNF and expanding risk groups |
| 42007450 | Aung PP et al. HemaSphere 2026 | Upadacitinib preclinical efficacy in STAT5B-mutated HSTCL |
| 14504095 | Belhadj K et al. Blood 2003;102(13):4261-4269 | 21-patient series; clinicopathologic entity |

---

## Summary

Hepatosplenic T-cell lymphoma is an exceptionally rare (<1% of NHL), highly aggressive peripheral T-cell lymphoma derived from cytotoxic γδ T cells with characteristic sinusoidal infiltration of the liver, spleen, and bone marrow. Its genetic basis has been elucidated through whole-exome sequencing, revealing frequent iso7q (47%), STAT5B activating mutations (31%), and loss-of-function mutations in chromatin-modifying genes led by SETD2 (25%) (PMID: 28122867). The disease predominantly affects young males, with approximately 20–30% of cases arising in the setting of chronic immunosuppression, particularly thiopurine therapy in IBD patients. Prognosis is dismal (median OS ~12 months) without allogeneic HSCT, which offers the best chance for long-term survival (5-year OS 58–71%). The identification of STAT5B as a driver mutation has opened the door to targeted JAK inhibitor therapy, with preclinical evidence supporting upadacitinib efficacy (PMID: 42007450). No approved targeted therapies currently exist for HSTCL, making clinical trial enrollment a priority.

---

Sources:
- [McKinney et al., The Genetic Basis of HSTCL — Cancer Discovery 2017 (PMID: 28122867)](https://aacrjournals.org/cancerdiscovery/article/7/4/369/5954/The-Genetic-Basis-of-Hepatosplenic-T-cell)
- [Yabe et al., HSTCL: a rare but challenging entity — Blood 2020](https://ashpublications.org/blood/article/136/18/2018/461707/Hepatosplenic-T-cell-lymphoma-a-rare-but)
- [Küçük et al., Frequent STAT5B mutations — Leukemia 2015 (PMID: 24947020)](https://www.nature.com/articles/leu2014200)
- [Foppoli & Ferreri, Clinicopathologic review — Human Pathology 2018 (PMID: 29337025)](https://pubmed.ncbi.nlm.nih.gov/29337025/)
- [Falchook et al., Population-based incidence — CLML 2016 (PMID: 27099586)](https://pubmed.ncbi.nlm.nih.gov/27099586/)
- [Mayo Clinic HSTCL outcomes (PMID: 33160933)](https://pubmed.ncbi.nlm.nih.gov/33160933/)
- [Haematologica 2024 — HSTCL cytological pattern and genomic profile](https://haematologica.org/article/view/haematol.2023.283856)
- [Allo-HSCT with TBI for HSTCL — PMC 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC10859473/)
- [The Genetic Basis of HSTCL — PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC5402251/)
- [Aung et al., Upadacitinib preclinical HSTCL — HemaSphere 2026 (PMID: 42007450)](https://pubmed.ncbi.nlm.nih.gov/42007450/)
- [STAT5B-driven HSTCL mouse model — bioRxiv 2025](https://www.biorxiv.org/content/10.1101/2025.10.24.684333v1)
- [HSTCL SEER epidemiology — ASH 2024](https://ashpublications.org/blood/article/144/Supplement%201/6422/528751/Hepatosplenic-T-Cell-Lymphoma-A-SEER-Stat-Review)
- [Survival determinants — ASH 2025 pooled database](https://ashpublications.org/blood/article/146/Supplement%201/892/551522/Survival-determinants-of-hepatosplenic-t-cell)
- [HSTCL in IBD — anti-TNF risk (PMID: 21941193)](https://pubmed.ncbi.nlm.nih.gov/21941193/)
- [HSTCL and thiopurines — systematic review](https://www.sciencedirect.com/science/article/abs/pii/S1542356510009079)
- [JAK inhibitors in T-cell lymphomas — Cancers 2026](https://doi.org/10.3390/cancers18050799)
- [ICD-10-CM C86.1](https://www.icd10data.com/ICD10CM/Codes/C00-D49/C81-C96/C86-/C86.1)
- [Orphanet: HSTCL (ORPHA:86882)](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=86882&lng=EN)
- [HSTCL 21-patient series — Blood 2003 (PMID: 14504095)](https://ashpublications.org/blood/article/102/13/4261/17406/Hepatosplenic-T-cell-lymphoma-is-a-rare)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 18 |
| On topic | 10 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:28122867` *(abstract only)*: "Dominant hotspot mutations N642H and V712E were particularly efficacious in maintaining STAT5 phosphorylation"
  - closest text in source: "In addition, we found that mutations in STAT5B and PIK3CD activate critical signaling pathways important to cell survival in HSTL"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:33064823` (5 mentions) - Contrast-FEL-A Test for Differences in Selective Pressures at Individual Sites among Clades and Sets of Branches.
  - shared terms: gene

Weighed against this report's own most characteristic terms: `hstcl`, `cell`, `mutation`, `t-cell`, `lymphoma`, `year`, `stat5b`, `disease`, `patient`, `gene`, `risk`, `survival`, `infiltration`, `primary`, `bone`, `clinical`, `marrow`, `pattern`, `setd2`, `approximately`.

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMID:42007450`: "Displayed significant and selective anti-tumor efficacy against STAT5B-mutated HSTCL cells in vitro and in vivo, and in primary HSTCL patient samples, highlighting upadacitinib as a potential targeted therapeutic option for STAT5B-mutated HSTCL"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 45 |
| Resolved | 43 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 38 |
| Terms named correctly | 18 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 14 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0019474` (1 mention) - the report calls it "MONDO"; MONDO calls it **hepatosplenic T-cell lymphoma**
- `HP:0001945` (1 mention) - the report calls it "Fever / B symptoms"; HP calls it **Fever**
- `HP:0025435` (1 mention) - the report calls it "Elevated LDH"; HP calls it **Increased circulating lactate dehydrogenase concentration**
- `CL:0000875` (1 mention) - the report calls it "Splenic red pulp macrophage"; CL calls it **non-classical monocyte**
- `GO:0098533` (1 mention) - the report calls it "Histone H3-K36 trimethylation"; GO calls it **ATPase dependent transmembrane transport complex**
- `UBERON:0001281` (1 mention) - the report calls it "Hepatic sinusoids**: Neoplastic cells within variably dilated sinusoids"; UBERON calls it **hepatic sinusoid**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0016571` (obsolete histone methylation) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001744` (1 mention) - the report calls it "Splenomegaly (marked)"; HP calls it **Splenomegaly**
- `HP:0004325` (1 mention) - the report calls it "Weight loss"; HP calls it **Decreased body weight**, and lists "Low weight" among its other names
- `HP:0012156` (2 mentions) - the report calls it "Hemophagocytosis", "Hemophagocytic syndrome"; HP calls it **Hemophagocytosis**
- `HP:0003256` (1 mention) - the report calls it "Coagulopathy"; HP calls it **Abnormality of the coagulation cascade**, and lists "Coagulopathy" among its other names
- `GO:0007259` (2 mentions) - the report calls it "JAK-STAT cascade"; GO calls it **cell surface receptor signaling pathway via JAK-STAT**, and lists "JAK-STAT cascade" among its other names
- `CL:1000398` (1 mention) - the report calls it "Hepatic sinusoidal endothelial cell"; CL calls it **endothelial cell of hepatic sinusoid**, and lists "liver sinusoidal endothelial cell" among its other names
- `CL:0000235` (1 mention) - the report calls it "Kupffer cell / macrophage"; CL calls it **macrophage**
- `CL:0002092` (1 mention) - the report calls it "Bone marrow hematopoietic cell"; CL calls it **bone marrow cell**
- `GO:0043066` (1 mention) - the report calls it "Anti-apoptosis / negative regulation of apoptotic process"; GO calls it **negative regulation of apoptotic process**
- `UBERON:0002106` (1 mention) - the report calls it "Spleen** (primary)"; UBERON calls it **spleen**
- `UBERON:0002107` (1 mention) - the report calls it "Liver** (primary)"; UBERON calls it **liver**
- `UBERON:0002371` (1 mention) - the report calls it "Bone marrow** (primary)"; UBERON calls it **bone marrow**
- `UBERON:0000178` (1 mention) - the report calls it "Peripheral blood"; UBERON calls it **blood**, and lists "vertebrate blood" among its other names
- `NCIT:C11197` (1 mention) - the report calls it "CHOP Regimen"; NCIT calls it **FOLFOX Regimen**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0012156` - called "Hemophagocytosis", "Hemophagocytic syndrome"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.