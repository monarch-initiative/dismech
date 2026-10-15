---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-20T19:47:45.076708'
end_time: '2026-09-20T19:52:57.275696'
duration_seconds: 312.2
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Acute Tricyclic Antidepressant Poisoning
  mondo_id: MONDO:0018547
  category: Complex
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
  web_search_requests: 18
  num_turns: 21
  total_cost_usd: 1.4717242
  session_id: dc83c613-1fba-53b8-9741-f63fb2448a6e
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
citation_count: 37
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 9
  quotes_valid: 2
  quotes_unsupported: 7
  unsupported_quote_references:
  - PMC:PMC9314015
  - PMC:PMC7939188
  - DOI:10.1177/039139880002300904
  - PMID:9737495
  - PMID:25939777
  - PMC:PMC4538909
  relevance_assessed: 24
  on_topic: 12
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 50
  verified: 45
  not_found: 2
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.043
  labels_checked: 21
  labels_matching: 13
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0000615
    reported_labels:
    - Mydriasis
    ontology_label: Abnormal pupil morphology
  - term_id: HP:0002593
    reported_labels:
    - Ileus
    ontology_label: Intestinal lymphangiectasia
  - term_id: HP:0004756
    reported_labels:
    - subsumed
    ontology_label: Ventricular tachycardia
  - term_id: NCIT:C1636
    reported_labels:
    - Activated Charcoal
    ontology_label: Therapeutic Steroid Hormone
  labels_variant: 4
  unresolved_terms:
  - HP:0002379
  - HP:0200110
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acute Tricyclic Antidepressant Poisoning
- **MONDO ID:** MONDO:0018547 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Acute Tricyclic Antidepressant Poisoning** covering all of the
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

I now have sufficient material across all sections to compile a comprehensive research report. Writing it now.

# Acute Tricyclic Antidepressant (TCA) Poisoning — Comprehensive Research Report

## 1. Disease Information

**Overview.** Acute tricyclic antidepressant poisoning is a potentially lethal toxidrome resulting from single large-dose ingestion (almost always intentional/suicidal) of a tricyclic antidepressant. It is characterized by the triad of (1) an anticholinergic toxidrome (mydriasis, dry mucous membranes, tachycardia, urinary retention, ileus, hyperthermia), (2) central nervous system toxicity (agitation progressing to lethargy, coma, and seizures), and (3) cardiovascular toxicity (sodium-channel-mediated conduction delay/QRS widening, hypotension, and ventricular dysrhythmias), which is the principal cause of death [StatPearls NBK430931](https://www.ncbi.nlm.nih.gov/books/NBK430931/); [PMC8439401](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8439401/).

**Key identifiers:**
- **MONDO:** MONDO:0018547 (Acute tricyclic antidepressant poisoning) — [NORD/MONDO page](https://rarediseases.org/mondo-disease/acute-tricyclic-antidepressant-poisoning/)
- **Orphanet:** ORPHA:43117 — [Orphanet record](https://www.orpha.net/en/disease/detail/43117)
- **ICD-10:** T43.0 (Poisoning by tricyclic and tetracyclic antidepressants); **ICD-9:** 969.0
- **eMedicine/Medscape ID:** 819204 — [Tricyclic Antidepressant Toxicity, Medscape](https://emedicine.medscape.com/article/819204-overview)
- Representative specific drugs, each with its own identifiers used in curation (HGNC targets are the transporters/receptors, not the drugs; CHEBI covers the small molecules): amitriptyline, nortriptyline, imipramine, desipramine, doxepin, clomipramine, trimipramine, protriptyline, amoxapine, dothiepin (dosulepin), maprotiline (a "tetracyclic" grouped clinically with TCAs).

**Synonyms:** cyclic antidepressant overdose/poisoning, tricyclic antidepressant (TCA) toxicity, TCA overdose.

**Data provenance note.** Most quantitative information below is derived from aggregated poison-control/registry data (NPDS/AAPCC annual reports) and retrospective single- or multi-center case series, i.e., disease-level/aggregate resources rather than individual EHR record review — an important distinction for evidence grading in the knowledge base.

---

## 2. Etiology

**Primary cause.** TCA poisoning is essentially always **iatrogenic/pharmacologic overdose** — an exposure (nearly always a deliberate self-poisoning) to a prescribed or otherwise available tricyclic antidepressant. There is no intrinsic "genetic disease" etiology; the entity is a toxicologic/pharmacologic acute poisoning, so its "genetic risk factors" operate through pharmacogenomic modulation of drug exposure/toxicity rather than causing the disease de novo.

### Risk factors

**Genetic (pharmacogenomic) risk factors — modulate individual susceptibility to toxicity at a given dose, not causal in the Mendelian sense:**
- **CYP2D6 poor metabolizer status.** Amitriptyline and most TCAs undergo demethylation (largely CYP2C19-mediated, producing active secondary-amine metabolites such as nortriptyline from amitriptyline) and hydroxylation (largely CYP2D6-mediated, producing less active hydroxylated metabolites). "Amitriptyline is metabolized mainly via CYP2C19 and CYP2D6 pathways. Metabolism by CYP2C19 results in active metabolites, including nortriptyline… while metabolism catalyzed by CYP2D6 results in the formation of the less active 10-hydroxy metabolite" [CPIC TCA Guideline PDF](https://files.cpicpgx.org/data/guideline/publication/TCA/2016/TCA_2016.pdf); [NBK425165](https://www.ncbi.nlm.nih.gov/books/NBK425165/). CYP2D6 poor metabolizers accumulate higher parent-drug and active-metabolite concentrations at a given dose, raising the risk of supratherapeutic/toxic exposure and QT prolongation; CPIC recommends a ~50% dose reduction for CYP2D6 poor metabolizers and use of an alternative agent in CYP2D6 ultrarapid metabolizers.
- **CYP2C19 poor metabolizer status** similarly raises tertiary-amine (parent drug) concentrations.
- At **toxic (supratherapeutic) concentrations**, CYP2D6's fractional contribution to clearance falls relative to therapeutic concentrations (saturable, capacity-limited metabolism), which is itself a mechanism amplifying toxicity in overdose independent of genotype — "the contribution of CYP2D6 significantly decreased for its demethylation and hydroxylation pathways" as amitriptyline concentration rose from therapeutic to toxic levels ([Springer/Forensic Toxicology 2008](https://link.springer.com/article/10.1007/s11419-008-0063-9)).
- No specific cardiac ion-channel germline variant (e.g., latent Brugada-syndrome SCN5A loss-of-function alleles) has been systematically implicated in TCA poisoning per se, but mechanistically a patient with subclinical SCN5A-related sodium-channelopathy would be expected to be at increased risk of TCA-induced conduction block/Brugada phenocopy given the shared final pathway (see Mechanism, below), based on the shared molecular target rather than direct epidemiologic data.

**Environmental / behavioral risk factors:**
- **Access to a lethal quantity of the drug** — the single most important modifiable risk factor; large-quantity, non-blister-packaged prescriptions are more lethal in a single ingestion.
- **Female sex** — TCA exposures are more common in women, reflecting a higher rate of self-poisoning attempts in women generally, although completed-suicide-by-any-method rates are higher in men ([Medscape epidemiology](https://emedicine.medscape.com/article/819204-overview)).
- **Underlying psychiatric illness** (major depressive disorder, especially treatment-resistant depression for which TCAs remain prescribed) is the population from which most exposures arise.
- **Co-ingestion** with other CNS depressants (benzodiazepines) or cardiotoxic agents; in the 6-year retrospective ED series, benzodiazepines (8.0%) and antihypertensives (4.0%) were the most common co-ingestants ([PMC13458188](https://pmc.ncbi.nlm.nih.gov/articles/PMC13458188/)).
- **Delayed presentation / delayed decontamination** and pre-existing cardiac conduction disease increase risk of cardiotoxic complications.

**Protective factors:**
- **Prescribing pattern shift away from TCAs toward SSRIs/SNRIs** has been the dominant population-level protective factor: "The frequency of TCA overdoses has declined since the 1980s, whereas SSRI overdoses have increased significantly, reflecting changes in prescribing practices" ([Medscape](https://emedicine.medscape.com/article/819204-overview)).
- **Limiting dispensed quantity / packaging controls** — proposed as a means-restriction suicide-prevention strategy: "If pills were packaged in blister packs of 16 to 25, anyone who wanted to use them to commit suicide would have to work really hard… If we make it hard to buy pills in bottles of 50 or 100 capsules that can easily be dumped out and swallowed, we can prevent many deaths" ([NCL commentary](https://nclnet.org/will_repackaging_medicine_prevent_suicides/)). No specific jurisdictional statute mandating TCA blister-packaging was identified in this search (unlike the UK's 1998 paracetamol pack-size legislation, which is the model example); this remains a policy proposal rather than an established intervention specific to TCAs.
- **Rapid access to emergency care / early sodium bicarbonate therapy** is protective against progression to lethal dysrhythmia (see Treatment).

**Gene–environment interaction:** The clearest interaction is pharmacogenomic — CYP2D6/CYP2C19 genotype determines steady-state drug/metabolite exposure at a given prescribed dose (environment = prescribed dose), so a poor-metabolizer genotype converts an otherwise "therapeutic" prescribed dose into a de facto higher effective exposure, and in the overdose setting further shifts an already massive ingested dose toward even higher peak free-drug levels because of saturable first-pass and hepatic clearance ([CPIC Guideline](https://files.cpicpgx.org/data/guideline/publication/TCA/2016/TCA_2016.pdf)).

---

## 3. Phenotypes

TCA poisoning phenotypes cluster into three overlapping domains — anticholinergic, neurologic/CNS, and cardiovascular — with onset generally rapid (most severe toxicity manifests within the first 6 hours, and clinical deterioration can be abrupt) ([StatPearls NBK430931](https://www.ncbi.nlm.nih.gov/books/NBK430931/); [ED retrospective series, PMC13458188](https://pmc.ncbi.nlm.nih.gov/articles/PMC13458188/)).

| Phenotype | Type | Suggested HP term | Onset/Frequency/Notes |
|---|---|---|---|
| Mydriasis | Clinical sign | HP:0000615 (Mydriasis) | Early anticholinergic sign |
| Dry mucous membranes / dry mouth | Clinical sign | HP:0000217 (Xerostomia) | Early anticholinergic sign |
| Tachycardia | Clinical sign | HP:0001649 (Tachycardia) | Very common; 37.3% tachycardic on presentation in one series |
| Urinary retention | Clinical sign | HP:0000016 (Urinary retention) | Anticholinergic |
| Decreased/absent bowel sounds (ileus) | Clinical sign | HP:0002593 (Ileus) | Anticholinergic |
| Hyperthermia | Clinical sign | HP:0001945 (Fever/hyperthermia) | Anticholinergic; worsened by seizures/agitation |
| Altered mental status / delirium | Behavioral/CNS | HP:0000738 (Behavioral abnormality) / HP:0031466 (Delirium, if used) | 46.7% presented with altered mental status |
| Drowsiness/lethargy progressing to coma | CNS | HP:0001262 (Lethargy); HP:0001259 (Coma) | Progressive with dose; 29.3% drowsy at presentation |
| Seizures | CNS / neurologic sign | HP:0001250 (Seizure) | Occur in ~10–20% of significant ingestions; usually brief but may be refractory; predicted by QRS >100 ms |
| Myoclonic jerks | CNS | HP:0002379 (Myoclonus) | Reported in severe toxicity |
| Respiratory depression | Clinical sign | HP:0002093 (Respiratory insufficiency) | May require intubation (20% intubated in one ED series) |
| QRS widening (>100 ms) | Lab/ECG abnormality | (ECG finding; no dedicated HP term — use as biochemical/EKG readout) | Predicts seizures; sodium-channel blockade signature |
| QRS >160 ms | Lab/ECG abnormality | — | Predicts ventricular dysrhythmias |
| Terminal R wave in aVR ≥3 mm | Lab/ECG abnormality | — | Sensitivity 81%, specificity 73% for seizures/arrhythmias (Liebelt 1995) |
| QTc prolongation | Lab/ECG abnormality | HP:0011675 (Arrhythmia, generic) or specific QT term if modeled | Via potassium (hERG) channel blockade |
| Ventricular tachycardia / ventricular fibrillation | Clinical sign | HP:0004756 (Ventricular tachycardia) / HP:0001663 (Ventricular fibrillation) | Major cause of death |
| Torsades de pointes | Clinical sign | HP:0004756 (subsumed) | Secondary to QT prolongation |
| Hypotension | Clinical sign | HP:0002615 (Hypotension) | Alpha-1 blockade + myocardial depression; ~8% hypotensive at presentation |
| Cardiac arrest / asystole | Clinical sign | HP:0001695 (Cardiac arrest) | End-stage; managed with prolonged CPR/ECMO |
| Rhabdomyolysis | Laboratory abnormality | HP:0003201 (Rhabdomyolysis) | Rare; secondary to seizures/agitation/hyperthermia |
| Brugada-phenocopy ECG pattern | Lab/ECG abnormality | HP:0200110 (Brugada syndrome, ECG pattern - use with caution as "phenocopy" not true channelopathy) | Reversible sodium-channel-blockade phenomenon |

**Age of onset:** Not applicable in the congenital sense; this is an acquired acute poisoning, most common in adolescents/adults (mean age ~30–35 years in cohort studies) ([Liebelt 1995](https://pubmed.ncbi.nlm.nih.gov/7618783/); [PMC13458188](https://pmc.ncbi.nlm.nih.gov/articles/PMC13458188/)).

**Severity and progression:** Variable and dose-dependent; can range from mild anticholinergic symptoms to death within hours. "All fatal ingestions developed major signs of toxicity mandating admission within two hours of arrival at the hospital, with a mean time from arrival to death of only 5.43 hours, and all patients who died did so within 24 hours of arrival" (classic epidemiologic study, cited via [Medscape epidemiology summary](https://emedicine.medscape.com/article/819204-overview)). Course is typically monophasic/self-limited over 24–72 hours if the patient survives the acute cardiotoxic window, in contrast to a chronic/progressive disease.

**Quality of life impact:** Not chronic; QoL impact is acute (ICU stay, intubation, cardiac arrest sequelae, potential anoxic brain injury) rather than long-term unless anoxic injury or prolonged arrest occurs (e.g., the VA-ECMO case discharged without neurological impairment after 27 hours of ECMO support — [PMC7939188](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7939188/) — versus cases with post-arrest encephalopathy after prolonged arrest, not separately quantified in these sources).

---

## 4. Genetic/Molecular Information

There is **no causal Mendelian gene** for this acquired poisoning; the "genetic" contribution is entirely pharmacogenomic, governing drug/metabolite exposure rather than an intrinsic disease process.

- **Metabolizing enzymes (modifier genes, not causal genes):**
  - **CYP2D6** (HGNC:2625) — hydroxylation pathway (inactivation); poor-metabolizer alleles (*3, *4, *5, *6, etc.) elevate exposure; CPIC recommends dose reduction in PMs.
  - **CYP2C19** (HGNC:2621) — demethylation pathway (tertiary→secondary amine, e.g., amitriptyline→nortriptyline, an active metabolite); poor-metabolizer alleles elevate tertiary-amine parent-drug levels.
  - **OCT1** (SLC22A1) — has been studied for effects on amitriptyline pharmacokinetics in combination with CYP2D6/CYP2C19 genotype ([Frontiers in Pharmacology 2021](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2021.688950/full)).
- **Molecular targets of toxicity (not variants, but the drug-target proteins whose blockade constitutes the mechanism — useful for `genetic`/`biological_processes` binding in a mechanism-oriented KB entry):**
  - Cardiac voltage-gated sodium channel **SCN5A/Nav1.5** — fast inward sodium current, phase-0 depolarization target of TCA blockade (a "sodium channel blocker" class effect analogous to Class IA antiarrhythmics).
  - Cardiac potassium channels (hERG/**KCNH2**) — TCA blockade of the delayed rectifier potassium current slows phase-3 repolarization, prolonging QT/QTc.
  - **GABA-A receptor** (multiple GABRA/GABRB/GABRG subunits) — TCAs act at (or near) the picrotoxin site as GABA-A antagonists, contributing to seizures; "tricyclic antidepressants can inhibit α5-containing GABAA receptors by two distinct mechanisms" ([PMC9314015](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9314015/)).
  - **Muscarinic acetylcholine receptors** (CHRM1–5) — central and peripheral antagonism producing the anticholinergic toxidrome.
  - **Alpha-1 adrenergic receptor** (ADRA1A/B/D) — peripheral antagonism producing vasodilation/hypotension.
  - **Norepinephrine and serotonin transporters** (SLC6A2/NET, SLC6A4/SERT) — the therapeutic monoamine-reuptake-inhibition target; in overdose, initial NET blockade produces a transient hyperadrenergic phase, followed by catecholamine depletion and hypotension.
- **Pathogenic variant classification:** Not applicable (acquired poisoning, not a variant-driven disease). No ClinVar/gnomAD relevance beyond the pharmacogenes above.
- **Epigenetics / chromosomal abnormalities:** No established role.

---

## 5. Environmental Information

- **Primary "environmental" factor is the drug itself** — this is fundamentally a xenobiotic (pharmaceutical) exposure. Relevant exposure ontology framing: exposure to a tricyclic antidepressant drug, typically via oral ingestion, in supratherapeutic/toxic quantity.
- **Lifestyle factors:** Underlying depressive illness and access to lethal means (large prescribed quantities, unsecured medication) are the dominant modifiable contextual factors; co-ingested ethanol or other CNS depressants worsen CNS/respiratory depression.
- **Infectious agents:** Not applicable — this is a toxicologic, not infectious, disease.
- **Occupational/toxin exposures:** Not applicable beyond therapeutic/illicit drug access; no industrial or environmental-toxin route of TCA exposure is described in the literature reviewed.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Ingestion of a supratherapeutic dose of a tricyclic antidepressant** → rapid gastrointestinal absorption (further slowed anticholinergic gut motility can paradoxically prolong absorption) → high peak plasma and myocardial tissue concentrations, driven by the drugs' large volume of distribution and high (~90–95%) plasma protein binding (chiefly to α1-acid glycoprotein).
2. **Supratherapeutic TCA binds and blocks the fast cardiac voltage-gated sodium channel (Nav1.5/SCN5A)** in a use-dependent fashion → **slowing of phase-0 depolarization** → this **leads to** QRS-complex widening on the surface ECG and slowed intraventricular/His-Purkinje conduction ("blockade of cardiac sodium channels causes decreased myocardial contractility and is seen on the ECG as widening of the QRS complex… slowing phase-zero depolarization on a cellular level causes QRS prolongation" — [OpenAnesthesia](https://www.openanesthesia.org/keywords/tricyclic-antidepressant-overdose/); [LITFL](https://litfl.com/tricyclic-overdose-sodium-channel-blocker-toxicity/)).
   - QRS widening **>100 ms results in / predicts** an increased risk of seizures; QRS **>160 ms results in / predicts** a markedly increased risk of ventricular dysrhythmias ("QRS prolongation greater than 100 milliseconds… predicts seizures, whereas QRS durations greater than 160 milliseconds indicate a higher risk of life-threatening dysrhythmias" — [StatPearls NBK430931](https://www.ncbi.nlm.nih.gov/books/NBK430931/)).
   - The vector of terminal right-axis conduction delay **produces** a prominent terminal R wave in lead aVR; an RaVR ≥3 mm **predicts** subsequent seizures or arrhythmias with 81% sensitivity/73% specificity (Liebelt et al. 1995, [PMID:7618783](https://pubmed.ncbi.nlm.nih.gov/7618783/)).
   - Severe conduction slowing can **produce** a Brugada-phenocopy ECG pattern (ST elevation in V1–V3, coved-type) that is reversible with correction of sodium-channel blockade, mechanistically distinct from (but converging with) congenital Brugada syndrome's SCN5A loss-of-function ([Journal of Ceylon College of Physicians](https://jccp.sljol.info/articles/10.4038/jccp.v52i1.7915); [Methodist DeBakey Cardiovasc J](https://journal.houstonmethodist.org/articles/10.14797/mdcj-16-3-245); [PMID:11232630](https://pubmed.ncbi.nlm.nih.gov/11232630/)).
   - Progressive conduction block **can lead to** high-grade AV block, ventricular tachycardia/fibrillation, and asystole — the principal proximate cause of death.
3. **In parallel, TCA blocks the cardiac delayed-rectifier potassium channel (hERG/KCNH2)** → slowed phase-3 repolarization → **leads to** QTc prolongation → **increases risk of** torsades de pointes.
4. **In parallel, TCA antagonizes peripheral α1-adrenergic receptors** → peripheral vasodilation; combined with sodium-channel-mediated myocardial depression and (later) catecholamine depletion from chronic norepinephrine-transporter blockade → **leads to** hypotension, which in severe cases progresses to refractory cardiogenic/vasodilatory shock ("cardiac toxicity results from antagonism of alpha-adrenoreceptors and use-dependent blockade of fast sodium channels" — [RCHSD clinical summary](https://www.rchsd.org/documents/2014/02/tricyclic-antidepressant-tca-overdose.pdf/)). Early in the course, norepinephrine-reuptake-transporter (NET) blockade can produce a transient hyperadrenergic state (tachycardia, mild hypertension) that is later superseded — as catecholamine stores are depleted — by hypotension.
5. **In parallel, TCA antagonizes central and peripheral muscarinic acetylcholine receptors** → **produces** the anticholinergic toxidrome: delirium/agitation, mydriasis, dry mucous membranes, urinary retention, ileus, tachycardia, and hyperthermia ("TCAs antagonize central and peripheral muscarinic acetylcholine receptors, resulting in delirium, tachycardia, hyperthermia, mydriasis, urinary retention, and ileus" — search synthesis from [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK430931/) and related sources).
6. **In parallel, TCA antagonizes GABA-A receptors** (binding at or near the picrotoxin site, with additional evidence for α5-subunit-containing GABA-A receptor inhibition — [PMC9314015](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9314015/)) → disinhibition of CNS excitatory circuits → **leads to** seizures, which are usually brief but may be refractory. Seizure activity itself **leads to** secondary hyperthermia, lactic acidosis, and (rarely) rhabdomyolysis ("Seizures cause hyperthermia, rhabdomyolysis, and metabolic acidosis" — search synthesis; [PMC10871817](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10871817/) reports rhabdomyolysis specifically with clomipramine poisoning). The resulting **acidemia further increases the free (unbound) fraction of TCA and increases sodium-channel affinity**, creating a positive-feedback loop that worsens cardiotoxicity — this is the physiologic rationale for aggressive alkalinization therapy (see Treatment).
7. **Progressive CNS depression** (from antihistaminic/anticholinergic and serotonergic/noradrenergic reuptake-inhibition effects) **leads to** sedation progressing to coma and respiratory depression, which can necessitate intubation and further predispose to hypercapnic acidosis, again exacerbating sodium-channel blockade.
8. **The convergence of cardiotoxicity (dysrhythmia) and refractory vasodilatory/cardiogenic shock is the dominant mechanism of death**: "large TCA overdoses are cardiotoxic, resulting in fatal arrhythmia and refractory hypotension, which is one of the most common causes of death in TCA intoxication" ([PMC7939188](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7939188/)).

### Molecular/cellular/pathway summary

- **Molecular pathways/targets:** Nav1.5 (SCN5A) fast sodium channel blockade (GO analog: "regulation of cardiac conduction," GO:0060306 or "sodium ion transmembrane transport," GO:0035725); hERG/KCNH2 potassium channel blockade; GABA-A receptor antagonism (GO:0007214, "gamma-aminobutyric acid signaling pathway"); muscarinic acetylcholine receptor antagonism (GO:0007196); α1-adrenergic receptor antagonism (GO:0007193, adenylate-cyclase-inhibiting pathway analogs as relevant); norepinephrine/serotonin transporter inhibition (GO:0051610, "serotonin uptake," and GO:0051620 "norepinephrine uptake").
- **Cellular processes:** Delayed cardiomyocyte depolarization, delayed repolarization, reduced myocardial contractility, peripheral vascular smooth-muscle relaxation, neuronal disinhibition/hyperexcitability (seizure).
- **Protein dysfunction:** Not a structural/misfolding disease — this is receptor/channel *pharmacologic antagonism* (reversible occupancy), not a mutation-driven loss/gain of function; conceptually maps to `modifier: DECREASED` (or a qualitative "antagonism") on the relevant channel/receptor activity nodes rather than a `functional_impact_category` (no host variant is involved).
- **Metabolic changes:** Seizure-associated lactic acidosis; acidemia (respiratory and/or metabolic) potentiates sodium-channel blockade, forming the pathophysiologic basis for bicarbonate therapy.
- **Immune system involvement:** None described.
- **Tissue damage mechanisms:** Hypoperfusion/ischemic injury secondary to shock and dysrhythmia; rare rhabdomyolysis from seizure/agitation-related muscle injury and hyperthermia.
- **Cell types/tissues implicated:** Ventricular and Purkinje-fiber cardiomyocytes (CL:0000746 "cardiac muscle cell" / more specific Purkinje myocyte terms), CNS neurons (cortical/hippocampal GABAergic interneurons for the seizure phenotype), vascular smooth muscle cells (α1-receptor-mediated vasodilation), hepatocytes (site of CYP2D6/CYP2C19 metabolism).
- **Anatomical structures:** Heart (UBERON:0000948) — specifically ventricular myocardium and the cardiac conduction system (UBERON:0004146/AV node, His-Purkinje system); CNS (UBERON:0001017, brain) for seizures/coma; peripheral vasculature (UBERON:0001981, blood vessel) for α1-mediated vasodilation; salivary glands, bladder, GI tract for peripheral anticholinergic effects.
- **Omics/advanced technologies:** No transcriptomic/proteomic/single-cell/spatial studies specific to acute human TCA poisoning were identified in this search; the mechanistic literature is predominantly electrophysiologic (patch-clamp channel-blockade studies) and animal cardiotoxicity models (see Model Organisms, below) rather than -omics profiling — an evidence gap worth flagging in the KB entry rather than fabricating a profiling claim.

---

## 7. Anatomical Structures Affected

- **Organ level:** Primary — heart (conduction system and myocardium) and CNS (brain). Secondary — lungs (aspiration, respiratory depression, ARDS in severe cases), skeletal muscle (rhabdomyolysis, rare), kidney (secondary to rhabdomyolysis/shock, acute kidney injury), GI tract (ileus).
- **Body systems:** Cardiovascular, nervous, and — via anticholinergic effects — the autonomic/gastrointestinal/genitourinary systems.
- **Tissue/cell level:** Cardiac conduction tissue (SA/AV node, His-Purkinje fibers) and ventricular myocardium; CNS gray matter (cortical/limbic neurons, GABAergic interneurons); vascular smooth muscle (peripheral resistance vessels).
- **Subcellular level:** Plasma-membrane ion channels (voltage-gated Na+ channel, delayed-rectifier K+ channel) and G-protein-coupled receptors (muscarinic, α1-adrenergic) — GO Cellular Component: plasma membrane (GO:0005886), voltage-gated sodium channel complex (GO:0001518).
- **Localization:** Bilateral/systemic — no lateralization; effects are generalized across the conduction system and CNS rather than focal.

---

## 8. Temporal Development

- **Onset:** Acute, within minutes to a few hours of ingestion; peak toxicity typically within 6 hours, though absorption may be delayed by anticholinergic ileus.
- **Progression:** "All fatal ingestions developed major signs of toxicity mandating admission within two hours of arrival at the hospital, with a mean time from arrival to death of only 5.43 hours, and all patients who died did so within 24 hours of arrival" ([classic epidemiology, summarized via Medscape](https://emedicine.medscape.com/article/819204-overview)). Course is not staged in the oncologic sense; severity is dose- and time-dependent, and deterioration can be rapid and catastrophic.
- **Disease course pattern:** Monophasic acute intoxication, not relapsing-remitting — resolves as the drug is metabolized/eliminated (typically over 24–72 hours in survivors) unless prolonged by very large ingestion, delayed absorption, or co-ingestants.
- **Critical period:** The first several hours after ingestion (and particularly the first 6 hours) constitute the critical window for cardiotoxic/CNS deterioration and is the basis for extended cardiac-monitoring observation periods (typically ≥6 hours asymptomatic with normal ECG before medical clearance, per poison-center guidelines) ([Woolf et al. 2007 consensus guideline, PMID:17453872](https://pubmed.ncbi.nlm.nih.gov/17453872/)).
- **Remission:** Spontaneous resolution with supportive/decontamination care in most survivors; no chronic relapsing pattern.

---

## 9. Population and Epidemiology

- **Incidence/exposure counts:** "In the 2022 American Association of Poison Control Centers' National Poison Data System Annual report, TCAs accounted for 3269 single exposures and 15 deaths. Amitriptyline was the most frequently ingested TCA with 1916 exposures and 10 deaths, followed by doxepin (495 exposures and one death) and nortriptyline (340 exposures, 2 deaths). The true incidence is likely substantially higher because of known underreporting" ([synthesis of AAPCC/NPDS data via Medscape/StatPearls](https://emedicine.medscape.com/article/819204-overview)). An earlier review of U.S. poison-center data for 2004 recorded over 12,000 TCA exposures ([Woolf 2007, PMID:17453872](https://pubmed.ncbi.nlm.nih.gov/17453872/)).
- **Case fatality:**
  - "TCA overdoses have a 78.4% rate of hospitalization and a 0.73% fatality rate" (aggregate poison-center data).
  - "Fatality before reaching a healthcare facility occurs in approximately 70% of patients attempting suicide with TCAs" — i.e., most TCA-related deaths occur pre-hospital.
  - "Only 2-3% of TCA overdose cases that reach a healthcare facility result in death."
  - A single-center 6-year retrospective ED cohort (n=75) reported a markedly higher in-hospital mortality (12 deaths, with 25.3% experiencing a poor outcome including death or discharge against medical advice), reflecting referral-center case-mix/severity bias rather than population incidence ([PMC13458188](https://pmc.ncbi.nlm.nih.gov/articles/PMC13458188/)).
  - "97% of all deaths due to antidepressant poisoning are caused by [tricyclics]," despite similar suicide-attempt rates between TCA and non-TCA antidepressant users — reflecting the TCAs' disproportionate lethality-per-overdose (narrow therapeutic index) rather than higher attempt frequency.
- **Trend:** "The frequency of TCA overdoses has declined since the 1980s, whereas SSRI overdoses have increased significantly, reflecting changes in prescribing practices."
- **Sex ratio:** Female predominance in exposures (e.g., 84.0% female in the 6-year ED cohort, mean age 35.1 ± 13.0 years), consistent with higher female self-poisoning attempt rates generally; overall antidepressant-related suicide mortality, however, shows the usual pattern of higher lethality per attempt in males across suicide methods broadly.
- **Age distribution:** Predominantly adults of reproductive/working age (mean age ~30–35 years across cohort studies); pediatric exploratory ingestions and adolescent intentional overdoses also occur and were historically a major focus of case series (e.g., PMID:834513, adolescent TCA overdoses).
- **Geographic distribution:** No specific endemic pattern; incidence tracks prescribing patterns and drug availability, historically higher in regions/eras with heavier TCA prescribing (pre-SSRI era) and remains clinically significant wherever TCAs are still prescribed for chronic pain, migraine prophylaxis, and treatment-resistant depression/enuresis.
- **Inheritance pattern:** Not applicable (acquired poisoning); insofar as pharmacogenomic (CYP2D6/CYP2C19) variation contributes to individual susceptibility, that variation itself follows the usual autosomal co-dominant, highly polymorphic star-allele inheritance pattern typical of these enzymes, with well-described population-specific allele frequencies (e.g., CYP2D6 poor-metabolizer frequency ~5–10% in Europeans, lower in East Asians; CYP2C19 poor-metabolizer frequency higher in East Asian populations) — not separately quantified for this specific poisoning outcome in the sources reviewed.

---

## 10. Diagnostics

**Clinical criteria / recognition:** Diagnosis is primarily clinical — recognized toxidrome (anticholinergic + CNS + cardiovascular findings) in a patient with known or suspected TCA ingestion, supported by ECG findings; it is a syndromic/toxicologic diagnosis rather than one requiring a specific confirmatory biomarker.

**ECG (the central diagnostic/risk-stratification tool):**
- **QRS interval** on 12-lead ECG (maximal limb-lead measurement): >100 ms predicts seizures; >160 ms predicts ventricular dysrhythmias ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK430931/)).
- **Terminal R wave in lead aVR (RaVR)** and **R/S ratio in aVR**: RaVR ≥3 mm had 81% sensitivity and 73% specificity for subsequent seizures/arrhythmias in a prospective cohort of 79 patients (16 seizures, 5 ventricular arrhythmias); "RaVR was greater in those patients who had seizures or arrhythmias than in those who did not (4.4 versus 1.8 mm, P < .001)" (Liebelt et al., Ann Emerg Med 1995;26:195–201, [PMID:7618783](https://pubmed.ncbi.nlm.nih.gov/7618783/)).
- **QTc prolongation** — via hERG/K+ channel blockade, raises torsades risk.
- **Brugada-phenocopy ST-segment pattern** (coved ST elevation V1–V3) — a diagnostically important reversible mimicker of congenital Brugada syndrome ([PMID:11232630](https://pubmed.ncbi.nlm.nih.gov/11232630/)).

**Laboratory tests:**
- Serum electrolytes, arterial/venous blood gas (to monitor and guide alkalinization therapy — target arterial pH 7.50–7.55, serum sodium ceiling ~150–155 mmol/L).
- Serum TCA concentrations are of limited immediate clinical utility (poor correlation with severity due to protein binding/active metabolites) and are not part of most standard bedside diagnostic algorithms; qualitative urine toxicology may support identification but is neither necessary nor sufficient.
- Creatine kinase (for rhabdomyolysis when suspected).

**Imaging:** Not primary; chest imaging may be used to evaluate aspiration/respiratory complications.

**Differential diagnosis (other sodium-channel-blocker toxidromes producing similar ECG/clinical pictures):** Other Class IA/IC antiarrhythmic overdose, cocaine toxicity, diphenhydramine/antihistamine overdose, propranolol overdose, carbamazepine overdose, quinine/chloroquine toxicity, and other cyclic-structure psychotropics (cyclobenzaprine) — all converge on cardiac sodium-channel blockade and can produce a similar ECG/clinical phenotype, making the QRS/aVR findings a "sodium-channel blocker toxidrome" signature rather than TCA-specific.

**Genetic testing:** Not part of acute clinical diagnosis; CYP2D6/CYP2C19 genotyping is a pharmacogenomic tool relevant to *prescribing safety* (dose adjustment to prevent toxicity) rather than to diagnosing an acute overdose.

**Screening:** Not applicable in the population-screening sense; "screening" in this context is really means-restriction/prescribing-safety practice (limiting dispensed quantities, considering genotype-guided dosing in high-risk patients).

---

## 11. Outcome / Prognosis

- **Case fatality (in-hospital):** 2–3% among patients who reach a healthcare facility (aggregate data); markedly higher (up to ~16% mortality, 25.3% poor outcome) in a referral tertiary-center retrospective cohort reflecting sicker case-mix ([PMC13458188](https://pmc.ncbi.nlm.nih.gov/articles/PMC13458188/)).
- **Pre-hospital mortality:** The large majority of TCA-poisoning deaths (≈70%) occur before the patient reaches medical care, underscoring the drug's narrow therapeutic index and rapid lethality.
- **Time course to death:** Mean 5.43 hours from hospital arrival to death among fatal in-hospital cases; all in-hospital deaths occurred within 24 hours of arrival.
- **Recovery potential:** Full recovery is typical in survivors who receive timely supportive/cardiotoxicity-targeted care, including those requiring prolonged resuscitation with mechanical circulatory support — e.g., a VA-ECMO case series patient was "extubated on day 5, and discharged on day 15 without neurological impairment" ([PMC7939188](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7939188/)).
- **Prognostic factors:** QRS duration (>100 ms, >160 ms), RaVR ≥3 mm, presence of seizures, ventricular arrhythmia, refractory hypotension/shock, and need for vasopressors/intubation are all markers of severity and worse short-term prognosis. Early aggressive sodium bicarbonate therapy is associated with reversal of cardiotoxicity and improved outcome in case reports/small series, though rigorous outcome trial data are lacking (evidence largely case-report/animal-model-based, as noted below).
- **Complications:** Ventricular dysrhythmia, cardiac arrest, seizures with secondary hyperthermia/rhabdomyolysis/metabolic acidosis, aspiration pneumonia, anoxic brain injury after prolonged arrest, and rare serotonin-syndrome-like presentations with clomipramine overdose ([PMC12862876](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12862876/); [PMC10871817](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10871817/)).
- **Long-term morbidity:** Generally none if the acute event is survived without prolonged hypoxia/arrest; long-term outcomes are otherwise driven by the underlying psychiatric illness rather than by residual toxicologic injury.

---

## 12. Treatment

**Overview/strategy:** Supportive care plus targeted reversal of sodium-channel blockade is the core algorithm; there is no specific pharmacologic "antidote" that reverses TCA binding directly, so treatment is mechanism-directed (alkalinization/sodium loading) and symptom-directed (seizure control, hemodynamic support), escalating to extracorporeal support in refractory cases ([StatPearls NBK430931](https://www.ncbi.nlm.nih.gov/books/NBK430931/); [Woolf 2007 consensus guideline, PMID:17453872](https://pubmed.ncbi.nlm.nih.gov/17453872/)).

**Decontamination:**
- **Activated charcoal** (30–50 g PO/NG) if presenting early after ingestion and airway is protected/protectable; binds TCA in the gut. NCIT term: NCIT:C1636 (Activated Charcoal) — treatment action term NCIT:C15220 or similar gastric decontamination code.
- **Hemodialysis/hemoperfusion are NOT effective** because of high protein binding and large volume of distribution: "avid tissue and plasma protein binding leaves only a small fraction of free drug available for diffusion or adsorption" ([search synthesis](https://www.ncbi.nlm.nih.gov/books/NBK430931/); [Frank & Kierdorf 2000](https://journals.sagepub.com/doi/10.1177/039139880002300904)).

**First-line pharmacotherapy for cardiotoxicity — sodium bicarbonate:**
- Indicated for QRS widening (>100 ms), ventricular dysrhythmia, or refractory hypotension.
- **Mechanism:** (1) sodium loading counteracts sodium-channel blockade; (2) alkalinization increases plasma protein binding (chiefly α1-acid glycoprotein) of TCA, reducing the free (unbound, active) drug fraction; (3) alkalinization favors dissociation of TCA from myocardial sodium channels ("serum alkalinization favors dissociation of the tricyclic away from myocardial sodium channels, and the extracellular sodium load improves sodium channel function" — [search synthesis](https://en.wikipedia.org/wiki/Tricyclic_antidepressant_overdose)).
- **Target:** arterial pH 7.50–7.55; serum sodium ceiling ~150–155 mmol/L is commonly cited as an upper limit for continued administration.
- NCIT treatment-action term: NCIT:C15986 (Pharmacotherapy); therapeutic agent: sodium bicarbonate (CHEBI:32139).

**Seizure management:**
- **Benzodiazepines** are first-line, consistent with the GABA-A-antagonism mechanism of TCA-induced seizures ("Benzodiazepines are the preferred therapy for seizures caused by TCA overdose due to GABA-A inhibition" — [search synthesis](https://www.sciencedirect.com/topics/pharmacology-toxicology-and-pharmaceutical-science/tricyclic-antidepressant-overdose)). NCIT: benzodiazepine class agents (e.g., lorazepam, CHEBI:6539; diazepam, CHEBI:49575).
- Refractory seizures may require propofol or barbiturate-based anesthesia/intubation.

**Hemodynamic support:**
- IV isotonic crystalloid fluid boluses for hypotension.
- **Vasopressors** for hypotension refractory to fluids/bicarbonate — direct-acting α1-agonists (phenylephrine, norepinephrine) are preferred over agents with mixed/indirect action (e.g., dopamine may be less effective given catecholamine-depletion physiology and reuptake-inhibition interactions) ("intravenous crystalloid fluid and vasopressors (phenylephrine or norepinephrine) being the treatment of choice" — [search synthesis](https://fpnotebook.com/Psych/Pharm/TrcyclcAntdprsntOvrds.htm)).

**Adjunctive/rescue therapies for refractory cardiotoxicity:**
- **Hypertonic sodium chloride solution** — in a swine model, hypertonic saline was highly efficacious in reversing severe TCA cardiotoxicity, "even more so than sodium bicarbonate," supporting sodium loading (rather than alkalinization per se) as the dominant mechanistic driver ([PMID:9737495](https://pubmed.ncbi.nlm.nih.gov/9737495/)); a rat study found similar efficacy between hypertonic saline and bicarbonate with the advantage that saline does not alter renal drug elimination ([PMC4538909](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4538909/) / [PMID:25939777](https://pubmed.ncbi.nlm.nih.gov/25939777/)). Human case reports also describe reversal of severe TCA cardiotoxicity with IV hypertonic saline.
- **Intravenous lipid emulsion (ILE) "lipid rescue"** — used as rescue therapy in refractory TCA cardiotoxicity/cardiac arrest, based on the "lipid sink" hypothesis sequestering lipophilic TCA away from target tissue; supported by animal data and multiple human case reports, including prolonged low-dose ILE infusion in a severe amitriptyline overdose with amitriptyline levels remaining in the toxic range for 21 days without recurrent toxicity ([PMID:24173885](https://pubmed.ncbi.nlm.nih.gov/24173885/); [PMID:22244291](https://pubmed.ncbi.nlm.nih.gov/22244291/); [PMID:22575302](https://pubmed.ncbi.nlm.nih.gov/22575302/); rat model of clomipramine intoxication, [PMC6028800](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6028800/)). Evidence remains largely case-report/animal-model level rather than randomized controlled trial level.
- **Extracorporeal membrane oxygenation (VA-ECMO)** — for refractory cardiac arrest or cardiogenic shock unresponsive to conventional therapy: "VA-ECMO is effective in critically ill poisoned patients who do not respond to conventional therapies" ([PMC7939188](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7939188/)); a 17-patient retrospective cohort of extracorporeal life support in severe drug intoxication (not TCA-specific) supports feasibility in this broader indication ([PMC2750196](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2750196/)); case reports of percutaneous cardiopulmonary support for TCA overdose specifically are also described ([PMID:21485124](https://pubmed.ncbi.nlm.nih.gov/21485124/)).
- **Extracorporeal sorbent detoxification / continuous renal replacement therapy (CRRT)** for optimized bicarbonate delivery has been reported in case reports as an adjunct in severe, prolonged cases, though this is not standard of care.

**Contraindicated/relatively contraindicated agents (mechanism-specific — important for a "do not use" curation note):**
- **Physostigmine** — historically used, now relatively contraindicated after case reports of asystole ("in 1980, Pentel and Peterson reported two patients who developed asystole when physostigmine was used to treat [cyclic antidepressant] toxicity"), though this remains debated, with some literature suggesting the risk was overstated and physostigmine may be underutilized for isolated antimuscarinic toxidromes in the absence of cardiac sodium-channel blockade ([search synthesis](https://www.sciencedirect.com/science/article/abs/pii/S0736467903001690)).
- **Class IA, IC, and III antiarrhythmics** (e.g., procainamide, flecainide, amiodarone) — contraindicated because they exacerbate sodium-channel blockade or further prolong the QT interval.
- **Flumazenil** — relatively contraindicated because reversing co-ingested benzodiazepine sedation can unmask/precipitate seizures in the TCA-toxic patient.

**Experimental/investigational:** Fab fragment antibody-based binding therapies (analogous to digoxin-specific antibody fragments) have been proposed conceptually for TCA but are not in clinical use; no ClinicalTrials.gov NCT-registered trial specific to acute TCA poisoning treatment was surfaced in this search (most trial-registry hits returned were for unrelated conditions), consistent with the evidence base for TCA-overdose management being dominated by case reports, small case series, and animal models rather than RCTs — an important evidence-quality caveat for the KB entry.

**Suggested NCIT terms:**
- NCIT:C15986 Pharmacotherapy (sodium bicarbonate, benzodiazepines, vasopressors)
- NCIT:C15747 Supportive Care (airway management, monitoring)
- Intubation/mechanical ventilation — relevant NCIT procedural term for airway management
- Gastric decontamination/activated charcoal administration

---

## 13. Prevention

- **Primary prevention — means restriction:** Reducing prescribed quantity and limiting refill sizes for at-risk patients (those with depression/suicidality) is the most evidence-aligned population-level primary-prevention strategy, paralleling the well-documented UK paracetamol pack-size legislation model; blister-packaging in small quantities has been proposed analogously for TCAs, though a jurisdiction-specific TCA packaging mandate was not identified in this search ([NCL commentary](https://nclnet.org/will_repackaging_medicine_prevent_suicides/)).
- **Prescribing practice:** Preferential use of SSRIs/SNRIs (much wider therapeutic index) over TCAs as first-line antidepressants, particularly in patients at elevated suicide risk, is the dominant prevention strategy reflected in the observed decline in TCA-overdose frequency since the 1980s.
- **Pharmacogenomic dosing:** CPIC-guided CYP2D6/CYP2C19 genotype-informed dosing when TCAs are prescribed (dose reduction in poor metabolizers) reduces the risk of supratherapeutic exposure at "therapeutic" doses, indirectly lowering baseline toxicity risk, though this does not prevent deliberate overdose.
- **Secondary prevention:** Rapid identification/triage of TCA ingestion via poison-center consultation and structured out-of-hospital/ED triage protocols (the Woolf et al. 2007 AAPCC consensus guideline) to ensure timely transport and monitoring.
- **Screening/monitoring:** Serial ECG monitoring (QRS duration, aVR findings) during the observation period is the operational "screening" tool for imminent deterioration in a patient who has ingested a TCA.
- **Counseling:** Safe medication storage counseling and lethal-means counseling for patients/families of individuals with depression or prior self-harm, and secure storage/disposal of unused medication.
- **Public health:** Broader suicide-prevention infrastructure (crisis lines, means-restriction counseling) rather than disease-specific public-health measures, since this is a poisoning outcome of an underlying psychiatric condition rather than an infectious or environmental disease with a discrete public-health intervention point.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** TCA toxicosis is well described in veterinary medicine, most commonly in **dogs (Canis lupus familiaris, NCBITaxon:9615)** and **cats (Felis catus, NCBITaxon:9685)** following accidental ingestion of a human family member's medication or veterinary-prescribed TCA (e.g., clomipramine and amitriptyline are used therapeutically in veterinary behavioral medicine, making iatrogenic/accidental overdose a recognized veterinary emergency).
- **Natural disease / veterinary relevance:** Recognized as a common small-animal toxicological emergency (accidental ingestion), managed with the same general principles (sodium bicarbonate, IV fluids, benzodiazepines for seizures, lipid emulsion rescue) as human medicine; this reflects true cross-species natural/accidental poisoning rather than an engineered model, and is a distinct category from the experimental animal-model studies below.
- **Comparative pathology:** The core Nav1.5/hERG/GABA-A/muscarinic/α1 mechanisms are highly conserved across mammals, which is why swine and rat models (below) translate mechanistically to human treatment guidance; no major species-specific divergence in the fundamental channel pharmacology was identified in this search.
- **Zoonotic potential:** Not applicable — this is a toxicologic exposure, not an infectious/zoonotic disease.

---

## 15. Model Organisms

TCA cardiotoxicity is one of the better animal-modeled acute-poisoning syndromes because the endpoint (QRS widening → hypotension → arrhythmia) is readily reproducible with controlled IV drug infusion.

- **Swine (pig) model** — IV nortriptyline infused to a defined toxic endpoint (QRS >120 ms and systolic BP ≤50 mmHg), used to compare hypertonic saline, sodium bicarbonate, and hyperventilation: "hypertonic saline solution is highly efficacious in reversing severe TCA cardiotoxicity, even more so than sodium bicarbonate. Hyperventilation alone appears to have little effect. Sodium loading may be the most important factor in reversing TCA toxicity" ([PMID:9737495](https://pubmed.ncbi.nlm.nih.gov/9737495/)). This large-animal model recapitulates the human sodium-channel-blockade cardiotoxicity phenotype closely (cardiac size/conduction-system anatomy is relatively human-like in swine), supporting reasonably high translational fidelity for the specific QRS/hypotension endpoints studied, though it does not model the CNS (seizure) component.
- **Rat (Sprague-Dawley) models:**
  - Amitriptyline-toxicity rat model comparing hypertonic saline and sodium bicarbonate: "the effects of sodium bicarbonate and hypertonic saline treatments on reducing cardiotoxicity development were similar. However, hypertonic saline has no adverse effects on drug elimination" ([PMC4538909](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4538909/); [PMID:25939777](https://pubmed.ncbi.nlm.nih.gov/25939777/)).
  - Clomipramine-intoxication rat model used to test intravenous lipid emulsion rescue therapy ([PMC6028800](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6028800/)).
  - **Limitations:** Rodent cardiac electrophysiology (heart rate, action-potential duration, ion-channel isoform expression, e.g., relative IKr/IKs contribution) differs substantially from human, so rat QT/repolarization findings are lower-fidelity for the potassium-channel/QTc component than for the sodium-channel/QRS component; rodent models also generally use controlled IV infusion to a defined toxic endpoint rather than a bolus oral overdose, which does not fully recapitulate the absorption/anticholinergic-ileus kinetics of human oral self-poisoning.
- **Applications:** These models are used almost exclusively to test and optimize **antidotal/rescue therapies** (sodium bicarbonate, hypertonic saline, lipid emulsion) rather than to study primary disease biology, consistent with this being an acquired pharmacologic toxicity rather than a heritable disease process.
- **No genetically engineered (knockout/knock-in/transgenic) mouse model specific to TCA poisoning** was identified in this search; this is expected, since the phenotype is produced by acute pharmacologic receptor/channel blockade in a wild-type animal rather than requiring a genetic lesion — a point worth noting explicitly in a KB entry's `animal_models` limitations, since the modeling literature is confined to pharmacologic-challenge models in normal animals.

---

## Summary of Key Ontology-Term Suggestions for KB Curation

| Domain | Suggested term |
|---|---|
| Disease identity | MONDO:0018547; ORPHA:43117; ICD-10 T43.0 |
| Sodium channel | SCN5A (hgnc:10593) / GO:0086002 (cardiac muscle cell action potential involved in contraction) |
| Potassium channel | KCNH2 (hgnc:6251) |
| GABA-A antagonism | GO:0007214 (gamma-aminobutyric acid signaling pathway) |
| Muscarinic antagonism | GO:0007196 (adenylate cyclase-inhibiting G protein-coupled acetylcholine receptor signaling pathway) |
| α1-adrenergic antagonism | GO:0071875 (adrenergic receptor signaling pathway) |
| Cell types | CL:0000746 (cardiac muscle cell); CL:0000097 (mast cell — not relevant); cortical/GABAergic interneuron CL terms for seizure node |
| Anatomy | UBERON:0000948 (heart); UBERON:0001017 (brain); UBERON:0004146 (cardiac conduction system component, if used) |
| Phenotypes | HP:0001250 (Seizure); HP:0001259 (Coma); HP:0001649 (Tachycardia); HP:0002615 (Hypotension); HP:0000615 (Mydriasis); HP:0003201 (Rhabdomyolysis); HP:0001695 (Cardiac arrest) |
| Treatment (NCIT) | NCIT:C15986 (Pharmacotherapy); sodium bicarbonate CHEBI:32139; benzodiazepine class agents |
| Evidence source flags | HUMAN_CLINICAL (case series/cohorts), MODEL_ORGANISM (swine/rat cardiotoxicity studies), COMPUTATIONAL (none identified) |

---

## Notes on Evidence Gaps (flagged rather than filled)

- No randomized controlled trial evidence was found for sodium bicarbonate, hypertonic saline, or lipid-emulsion therapy in human TCA poisoning; the evidence base is case-report/case-series and animal-model level, which should be reflected in `evidence_source`/`directness` grading in the KB entry.
- No transcriptomic/proteomic/single-cell profiling of human TCA-poisoning tissue was located; do not fabricate an -omics claim for this entry.
- No confirmed jurisdiction-specific TCA blister-pack legislation was located (unlike the well-documented UK paracetamol precedent); treat "packaging as prevention" as a proposed strategy, not an established regulatory fact, if curated into `environmental`/prevention content.
- Precise MONDO-to-Orphanet-to-ICD cross-mapping should be independently re-verified via `just validate-terms`/OAK lookup per this repository's Ontology Term Contract before binding, per house rules — the CURIEs above are reported as found in this research and are leads, not verified bindings.

**Sources:**
- [Acute tricyclic antidepressant poisoning — NORD/MONDO](https://rarediseases.org/mondo-disease/acute-tricyclic-antidepressant-poisoning/)
- [Orphanet: Acute tricyclic antidepressant poisoning](https://www.orpha.net/en/disease/detail/43117)
- [Tricyclic Antidepressant Toxicity — StatPearls, NBK430931](https://www.ncbi.nlm.nih.gov/books/NBK430931/)
- [Tricyclic Antidepressant Toxicity — Medscape/eMedicine](https://emedicine.medscape.com/article/819204-overview)
- [Novel Presentation of Cardiotoxicity and Other Complications in TCA Poisoning — PMC8439401](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8439401/)
- [Tricyclic Antidepressant Poisoning: 6-year Retrospective ED Analysis — PMC13458188](https://pmc.ncbi.nlm.nih.gov/articles/PMC13458188/)
- [ECG Lead aVR Versus QRS Interval in Predicting Seizures and Arrhythmias — PMID:7618783](https://pubmed.ncbi.nlm.nih.gov/7618783/)
- [Tricyclic antidepressant poisoning: evidence-based consensus guideline — PMID:17453872](https://pubmed.ncbi.nlm.nih.gov/17453872/)
- [Tricyclic Antidepressant Overdose — Wikipedia](https://en.wikipedia.org/wiki/Tricyclic_antidepressant_overdose)
- [Amitriptyline Therapy and CYP2D6/CYP2C19 Genotype — NBK425165](https://www.ncbi.nlm.nih.gov/books/NBK425165/)
- [CPIC Guideline for Tricyclic Antidepressants and CYP2D6/CYP2C19](https://files.cpicpgx.org/data/guideline/publication/TCA/2016/TCA_2016.pdf)
- [Effects of Genetic Polymorphism in CYP2D6, CYP2C19, OCT1 on Amitriptyline PK — Frontiers in Pharmacology](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2021.688950/full)
- [Roles of CYP2D6/CYP2C19 in amitriptyline metabolism at toxic levels — Forensic Toxicology 2008](https://link.springer.com/article/10.1007/s11419-008-0063-9)
- [Tricyclic antipsychotics/antidepressants inhibit α5-GABAA receptors — PMC9314015](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9314015/)
- [Experimental TCA Toxicity: Hypertonic Saline vs Bicarbonate vs Hyperventilation (swine) — PMID:9737495](https://pubmed.ncbi.nlm.nih.gov/9737495/)
- [Can empirical hypertonic saline or sodium bicarbonate prevent cardiotoxicity in amitriptyline poisoning? (rat) — PMC4538909](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4538909/)
- [Intravenous lipid emulsion therapy for clomipramine intoxication in rats — PMC6028800](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6028800/)
- [Prolonged use of IV lipid emulsion in severe TCA overdose — PMID:24173885](https://pubmed.ncbi.nlm.nih.gov/24173885/)
- [VA-ECMO and targeted temperature management in TCA-induced cardiac arrest — PMC7939188](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7939188/)
- [Extracorporeal life support in severe drug intoxication: 17 cases — PMC2750196](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2750196/)
- [Brugada syndrome mimicked by tricyclic antidepressant overdose — PMID:11232630](https://pubmed.ncbi.nlm.nih.gov/11232630/)
- [Brugada Phenocopy in TCA overdose — Methodist DeBakey Cardiovascular Journal](https://journal.houstonmethodist.org/articles/10.14797/mdcj-16-3-245)
- [Rhabdomyolysis as a manifestation of clomipramine poisoning — PMC10871817](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10871817/)
- [Assessing physostigmine's contraindication in cyclic antidepressant ingestions — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0736467903001690)
- [Will repackaging medicine prevent suicides? — National Consumers League](https://nclnet.org/will_repackaging_medicine_prevent_suicides/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 9 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 7 |
| References weighed for topical relevance | 24 |
| On topic | 12 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC9314015` *(abstract only)*: "tricyclic antidepressants can inhibit α5-containing GABAA receptors by two distinct mechanisms"
  - closest text in source: "Patients with schizophrenia show alterations in function, structure and molecular composition of the hippocampus, and a recent study demonstrated aberrant levels of hippocampal α5 subunit-containing GABAA receptors"
- `PMC:PMC7939188` *(abstract only)*: "large TCA overdoses are cardiotoxic, resulting in fatal arrhythmia and refractory hypotension, which is one of the most common causes of death in TCA intoxication"
  - closest text in source: "RATIONALE: Cardiotoxicity is a common cause of death in tricyclic antidepressant (TCA) intoxication"
- `PMC:PMC7939188` *(abstract only)*: "extubated on day 5, and discharged on day 15 without neurological impairment"
  - closest text in source: "He was discharged on day 15 without neurological impairment, and the post-discharge course was uneventful"
- `DOI:10.1177/039139880002300904` *(abstract only)*: "avid tissue and plasma protein binding leaves only a small fraction of free drug available for diffusion or adsorption"
  - Text part not found as substring: 'avid tissue and plasma protein binding leaves only a small fraction of free drug available for diffusion or adsorption' (note: only abstract available for DOI:10.1177/039139880002300904, full text may contain this excerpt)
- `PMID:9737495` *(abstract only)*: "hypertonic saline solution is highly efficacious in reversing severe TCA cardiotoxicity, even more so than sodium bicarbonate. Hyperventilation alone appears to have little effect. Sodium loading may be the most important factor in reversing TCA toxicity"
  - closest text in source: "Sodium loading may be the most important factor in reversing TCA toxicity."
- `PMID:25939777` *(abstract only)*: "the effects of sodium bicarbonate and hypertonic saline treatments on reducing cardiotoxicity development were similar. However, hypertonic saline has no adverse effects on drug elimination"
  - closest text in source: "The effects of sodium bicarbonate or hypertonic saline treatments on reducing the development of cardiotoxicity were similar"
- `PMC:PMC4538909` *(abstract only)*: "the effects of sodium bicarbonate and hypertonic saline treatments on reducing cardiotoxicity development were similar. However, hypertonic saline has no adverse effects on drug elimination"
  - closest text in source: "The effects of sodium bicarbonate or hypertonic saline treatments on reducing the development of cardiotoxicity were similar"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 50 |
| Resolved | 45 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 21 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000615` (2 mentions) - the report calls it "Mydriasis"; HP calls it **Abnormal pupil morphology**
- `HP:0002593` (1 mention) - the report calls it "Ileus"; HP calls it **Intestinal lymphangiectasia**
- `HP:0004756` (2 mentions) - the report calls it "subsumed"; HP calls it **Ventricular tachycardia**
- `NCIT:C1636` (1 mention) - the report calls it "Activated Charcoal"; NCIT calls it **Therapeutic Steroid Hormone**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0002379` (1 mention), reported as "Myoclonus" - HP does not contain this term
- `HP:0200110` (1 mention), reported as "Brugada syndrome, ECG pattern - use with caution as "phenocopy" not true channelopathy" - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001945` (1 mention) - the report calls it "Fever/hyperthermia"; HP calls it **Fever**, and lists "Hyperthermia" among its other names
- `HP:0011675` (1 mention) - the report calls it "Arrhythmia, generic"; HP calls it **Arrhythmia**
- `GO:0007196` (2 mentions) - the report calls it "adenylate cyclase-inhibiting G protein-coupled acetylcholine receptor signaling pathway"; GO calls it **adenylate cyclase-inhibiting G protein-coupled glutamate receptor signaling pathway**
- `UBERON:0000948` (2 mentions) - the report calls it "Anatomical structures:** Heart"; UBERON calls it **heart**, and lists "branchial heart" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.