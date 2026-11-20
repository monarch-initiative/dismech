---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-03T19:18:34.188577'
end_time: '2026-11-03T19:22:48.901727'
duration_seconds: 254.71
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Neonatal Severe Primary Hyperparathyroidism
  mondo_id: MONDO:0009397
  category: Mendelian
  causal_genes: CASR
  omim_id: OMIM:239200
  synonyms: hyperparathyroidism, neonatal; NSHPT
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
  num_turns: 25
  total_cost_usd: 2.6131849750000007
  session_id: 5194d992-04a7-442b-b7ab-62c8c4ca24fc
  stop_reason: end_turn
  permission_denials: 6
  denied_tools:
  - Bash
  assistant_text_blocks: 2
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 13
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 21
  quotes_valid: 19
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:35566721
  relevance_assessed: 14
  on_topic: 8
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 12
  verified: 12
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0009397
    reported_labels:
    - stub
    ontology_label: neonatal severe primary hyperparathyroidism
  - term_id: NCIT:C15329
    reported_labels:
    - parathyroidectomy-specific term to be looked up
    ontology_label: Surgical Procedure
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neonatal Severe Primary Hyperparathyroidism
- **MONDO ID:** MONDO:0009397 (if available)
- **Causal gene(s):** CASR
- **OMIM:** OMIM:239200
- **Synonyms:** hyperparathyroidism, neonatal; NSHPT
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Neonatal Severe Primary Hyperparathyroidism** covering all of the
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

Checking the local reference cache for NSHPT papers, then running a web search.

Status: writing the report now. My PubMed and E-utilities fetches were blocked, so exact quotes come only from abstracts already in the repo's reference cache.

# Neonatal Severe Primary Hyperparathyroidism (NSHPT): research report

**Scope:** This report covers MONDO:0009397, OMIM #239200. The causal gene is ***CASR*** (calcium-sensing receptor, hgnc:1514). This is the biallelic loss-of-function end of the CaSR-inactivation spectrum. The heterozygous end is FHH1 (OMIM #145980), which the KB already curates as `Familial_Hypocalciuric_Hypercalcemia_1`.

## How sourced this is

- **Exact quotes (verified):** Every quoted string comes from a file in `references_cache/` that I read directly:
  - PMID:35566721, Höppner 2022 review, full text
  - PMID:7916660, Pollak 1993 *Cell*, abstract
  - PMID:11013439, Hendy 2000 *Hum Mutat* review, abstract
  - PMID:31189130, Gorvin 2019 *J Mol Endocrinol* review, abstract
- **Leads only (not quoted):** For PMIDs 8132750, 7493018, 31778168 and 9011580 I have no abstract text.
  - PubMed returned HTTP 429 or a cookie wall, and `just fetch-reference` and E-utilities calls needed approval that was not granted.
  - What I say about these four comes from web-search result summaries. Each needs `just fetch-reference` and an abstract check before it is cited in YAML.
- **Ontology IDs:**
  - Verified: MONDO:0009397 (stub), hgnc:1514 and the ClinGen assertion (`cache/clingen/gene_validity.csv`).
  - Unverified: every HP, GO, CL, UBERON, CHEBI and NCIT CURIE below is a *proposed lead from memory, not looked up*. Each must go through `runoak` or `just validate-terms` before it is bound.
- **Repo state:** `kb/disorders/Neonatal_Severe_Primary_Hyperparathyroidism.yaml` already exists in this worktree as an untracked 8-line skeleton (name, creation_date, disease_term). The stub `stubs/Neonatal_Severe_Primary_Hyperparathyroidism.yaml` is still present, with priority HIGH.

---

## 1. Disease information

NSHPT is a life-threatening hypercalcaemic hyperparathyroid disorder that presents in the first days of life. It is usually caused by biallelic inactivating *CASR* variants.

- Höppner 2022 (PMID:35566721, review): "NSHPT [OMIM #239200] is a clinically severe, ultra-rare disease associated with a high mortality usually caused by homozygous or compound heterozygous inactivating mutations in CaSR"
- Hendy 2000 (PMID:11013439, review): "The homozygous condition manifests itself as neonatal severe hyperparathyroidism (NSHPT), a rare disorder characterized by extreme hypercalcemia and the bony changes of hyperparathyroidism which occur in infancy."

**Identifiers**

| System | ID | Status |
|---|---|---|
| MONDO | MONDO:0009397 "neonatal severe primary hyperparathyroidism" | verified (stub) |
| OMIM | 239200 | given in template; also stated in PMID:35566721 |
| HGNC | hgnc:1514 CASR | verified (ClinGen CSV row) |
| ClinGen | CASR / NSHPT / AR / **Definitive** / SOP9 / Tubulopathy GCEP / 2023-07-20, `CGGV:assertion_095b6507-5537-4017-b2b9-28715cc23df7-2023-07-20T160000.000Z` | verified (structured database) |
| Orphanet, ICD-10, ICD-11, MeSH | not looked up | **gap** |

- **Synonyms:** NSHPT; hyperparathyroidism, neonatal; neonatal severe hyperparathyroidism.
- **Data provenance:** All of this is aggregated disease-level information from reviews and case reports. No EHR data were used.

**Lump/split call to surface (not resolved here).** The literature uses three neonatal labels:
- **NSHPT:** biallelic variants. It is severe and persistent, and surgery is definitive.
- **NHPT (neonatal hyperparathyroidism):** usually heterozygous variants with a normocalcaemic mother. It is milder and often transient.
- **Severe heterozygous NSHPT:** heterozygous variants that give a full NSHPT picture, for example a de novo dominant-negative allele.

Höppner (PMID:35566721) says NHPT patients "usually carry heterozygous, LOF- mutations in CaSR" and that "spontaneous recovery should be expected in NHPT". The KB already has `Transient_Neonatal_Hyperparathyroidism`, so check that entry's scope before deciding:
- whether heterozygous NSHPT belongs here as a subtype, or
- whether it belongs in the transient entry, or
- whether it should be a `has_subtypes` row on FHH1.

MONDO's own scope for 0009397, biallelic only or biallelic plus severe heterozygous, was not checked.

## 2. Etiology

- **Primary cause:** germline inactivating *CASR* variants, biallelic in the classic form.
  - Pollak 1993 (PMID:7916660, primary, human plus in vitro): "We demonstrate that mutations in the human Ca(2+)-sensing receptor gene cause familial hypocalciuric hypercalcemia (FHH) and neonatal severe hyperparathyroidism (NSHPT)".
- **Gene dosage (lead):** Pollak 1994 *J Clin Invest* (PMID:8132750, lead). This was linkage work in four consanguineous families. Every NSHPT child was homozygous at FHH-linked 3q markers (LOD 5.56). It concluded that one defective allele causes FHH and two cause NSHPT.
- **Risk factors:**
  - Parental consanguinity (PMID:8132750, lead).
  - Two FHH-carrier parents.
  - For the heterozygous severe form, paternal or de novo inheritance with a normocalcaemic mother.
- **Maternal–fetal modifier:** Höppner (PMID:35566721) says severity in heterozygotes "is significantly modified by the parental origin of the mutation". It also says "the normocalcemic maternal environment is sensed as hypocalcemic by the fetus and thus induces fetal hyperparathyroidism to support increased fetal calcium levels at the expense of skeletal mineralization."
- **Maternal vitamin D:** this is a *proposed* modifier. Höppner: "The maternal vitamin D status during pregnancy may be a modifying factor".
- **Protective factors:** none reported. A heterozygote with an affected (hypercalcaemic) mother is effectively protected from fetal secondary hyperparathyroidism: "When the mutation is maternally derived … these pregnancies are likely uneventful" (PMID:35566721).
- **Gene–environment interaction:** the maternal calcium milieu acting on the fetal genotype, as above. This is the only one reported.

## 3. Phenotypes

Onset is neonatal throughout. No frequency data are available; the literature is case reports plus the Marx & Sinaii pooled review (lead).

| Phenotype | Source (exact text) | Proposed HP lead (unverified) |
|---|---|---|
| Severe hypercalcaemia | "extreme hypercalcemia" (PMID:11013439); "marked hypercalcaemia" (PMID:31189130) | Hypercalcemia HP:0003072 |
| Elevated/inappropriate PTH | "inappropriately high PTH concentrations despite elevated serum calcium" (PMID:35566721, spectrum-wide) | Elevated circulating parathyroid hormone level HP:0003165 |
| Skeletal demineralization / hyperparathyroid bone disease | "skeletal demineralisation" (PMID:31189130); "bony changes of hyperparathyroidism" (PMID:11013439) | Generalized osteopenia / Abnormal bone mineral density (choose after lookup) |
| Fractures | "fractures" (PMID:35566721) | Recurrent fractures HP:0002757 |
| Hypotonia / muscle weakness | "muscular weakness" (PMID:35566721) | Neonatal hypotonia HP:0001319 / Muscle weakness HP:0001324 |
| Respiratory distress | "respiratory distress" (PMID:35566721) | Respiratory distress HP:0002098 |
| Failure to thrive | "failure to thrive in the early days of life" (PMID:35566721); "failure to thrive in early infancy" (PMID:31189130) | Failure to thrive HP:0001508 |
| Parathyroid hyperplasia | lead only (mouse model PMID:7493018; human pathology not quoted) | Parathyroid hyperplasia HP:0008208 |
| Poor feeding, dehydration, lethargy | stated for NHPT, not NSHPT (PMID:35566721) | assign to NSHPT only with a separate source |
| Hypocalciuria (relative) | spectrum-level mechanism (PMID:35566721) | not a reported NSHPT-specific finding here |
| Thoracic deformity / rib fractures, hypermagnesaemia, nephrocalcinosis | commonly reported in reviews (my recall, *unsourced*) | **gap**, needs a primary source |

- **Quality of life:** no instrument-based data found (**gap**).
- **Long-term problems:** long-term post-parathyroidectomy issues (hypoparathyroidism, need for calcitriol) are expected, but I did not source them.

## 4. Genetic and molecular information

- **Gene:** *CASR*, 3q21.1 (PMID:35566721), hgnc:1514. The protein is a class C GPCR that works as a homodimer: "functionally active as a homodimer and couples to multiple G-protein subtypes" (PMID:31189130).
- **Variant spectrum:** more than 400 germline loss- and gain-of-function *CASR* variants are known across disorders (PMID:31189130). In 1993 Pollak reported three nonconservative missense variants, two in the extracellular N-terminal domain and one in the final intracellular loop (PMID:7916660).
- **Variant clustering:** "clustering in locations important for structural integrity, receptor dimerisation and ligand binding" (PMID:31189130).
- **Functional consequence:** loss of function.
  - In oocytes the mutant receptor gave "a markedly attenuated response" (PMID:7916660, IN_VITRO).
  - A dominant-negative mechanism has been proposed for some heterozygous severe cases. Bai 1997 (PMID:9011580, lead from ClinVar or search): de novo heterozygous p.R185Q in a neonate with normocalcaemic parents, with attenuated inositol phosphate response in HEK293 cells and a dominant-negative effect when co-expressed with wild-type receptor.
- **Zygosity and mode:** autosomal recessive for classic NSHPT (ClinGen MOI = AR). The heterozygous severe form is dominant or de novo.
- **Gaps:**
  - founder alleles, carrier frequency and gnomAD frequencies were not assessed;
  - no ClinVar variant table was pulled;
  - no modifier genes are known;
  - epigenetics: none known;
  - chromosomal abnormalities: none reported as a cause; large *CASR* deletions were not checked.
- **Population polymorphism:** CASR p.A986S has a modest effect on serum calcium (PMID:11013439). It is not a disease variant.

## 5. Environmental information

There are no toxic, lifestyle or infectious causes. The only environmental factor is the intrauterine maternal calcium and vitamin D environment, which affects heterozygous fetuses (PMID:35566721, review-level, partly hypothesis).

## 6. Mechanism and pathophysiology

**Causal chain** (each step names its source; inferred steps are marked):

1. **Biallelic inactivating *CASR* variants** lead to loss of functional cell-surface CaSR (PMID:7916660; PMID:11013439).
2. **Loss of CaSR in parathyroid chief cells** removes Ca²⁺-dependent G<sub>q/11</sub>–PLC–IP3 signalling. Höppner (PMID:35566721) describes the pathway as "couples to heterotrimeric G proteins (Ga11) leading to an increased phospholipase C activity with a subsequent elevation of inositol 1,4,5-trisphosphate (IP3)".
3. **Raised Ca²⁺ set-point** results in PTH secretion that is not suppressed by hypercalcaemia: "elevation of the body's calcium set point … it takes a higher level of plasma calcium to suppress PTH secretion" (PMID:35566721). Pollak 1993 says CaSR "'sets' the extracellular Ca2+ level" (PMID:7916660).
4. **Parathyroid hyperplasia.** In the human this step is inferred; it is demonstrated in Casr⁻/⁻ mice (PMID:7493018, lead). Hyperplasia amplifies the PTH excess.
5. **Branch A, bone:** PTH excess leads to osteoclastic bone resorption. The usual brake from hypercalcaemia on osteoclasts is lost because osteoclast CaSR is also inactive (PMID:35566721). The result is demineralisation and fractures.
6. **Branch B, kidney:** renal tubular CaSR loss raises the renal calcium threshold. This leads to low calcium excretion relative to filtered load (PMID:35566721), which amplifies the hypercalcaemia. The thick ascending limb and claudin-14 are relevant here (the FHH1 entry cites PMID:42261748). Applying this to NSHPT is inferred.
7. **Severe hypercalcaemia** leads to hypotonia, respiratory distress, poor feeding and failure to thrive (PMID:35566721). The step from hypercalcaemia to these specific signs is mechanistically inferred.
8. **Heterozygous modifier branch:** a heterozygous fetus with a normocalcaemic mother senses relative hypocalcaemia. This produces fetal secondary hyperparathyroidism and prenatal demineralisation (PMID:35566721). This drives the overlap between NHPT and NSHPT.

**Proposed term leads (all unverified):**
- **GO:**
  - cellular response to calcium ion
  - G protein-coupled receptor signalling (phospholipase C-activating GPCR pathway)
  - parathyroid hormone secretion (negative regulation, decreased)
  - bone resorption (increased)
  - renal calcium ion reabsorption
  - calcium ion homeostasis
  - calcium-sensing receptor activity (molecular function)
- **CL:** parathyroid chief cell; osteoclast; osteoblast; kidney loop of Henle thick ascending limb epithelial cell.
- **Biological scale tags:** step 1 MOLECULAR; steps 2–3 CELLULAR; step 4 TISSUE; steps 5–7 ORGANISM.

**Not available:** omics, single-cell, spatial or CRISPR-screen data specific to NSHPT. A search of GEO and similar repositories was not run.

## 7. Anatomical structures

All UBERON terms below are unverified leads.

- **Primary:** parathyroid gland.
- **Secondary:**
  - skeleton and bone tissue;
  - kidney, specifically the thick ascending limb of the loop of Henle;
  - respiratory system, through hypotonia and chest wall involvement (inferred).
- **Systems:** endocrine, skeletal, renal.
- **Subcellular:** plasma membrane, where the receptor sits. Proposed GO cellular component term: plasma membrane.
- **Laterality:** bilateral or systemic. All four parathyroid glands are affected; this follows from the requirement for total parathyroidectomy and is inferred.

## 8. Temporal development

- **Onset:** neonatal, "in the early days of life" (PMID:35566721). Prenatal skeletal involvement is possible in heterozygotes (PMID:35566721).
- **Course:** acute and life-threatening without treatment. Classic biallelic NSHPT does not remit spontaneously. This is my inference from surgery being called definitive, and it contrasts with NHPT, where recovery "should be expected" (PMID:35566721).
- **Critical period:** the neonatal window, before definitive surgery. Calcium and PTH must be lowered "until a diagnosis is established and a definite (surgical) treatment can be pursued" (PMID:35566721).

## 9. Inheritance and population

- **Inheritance:** autosomal recessive. Supported by ClinGen (AR, Definitive) and by Pollak 1994 (PMID:8132750, lead). Heterozygous de novo or paternal severe cases also occur (PMID:35566721; PMID:9011580, lead).
- **Prevalence:** described only as "ultra-rare" (PMID:35566721). No numeric NSHPT prevalence was found. The FHH figures (1 in 78,000 minimum; 74.1 per 100,000 *CASR* variant carriers in DiscovEHR, both cited in PMID:35566721) belong to FHH. Do not transfer them.
  - Suggested KB fields: `measure_type: UNKNOWN` or `CASES_IN_LITERATURE`, `prevalence_class: ULTRA_RARE`.
- **Consanguinity:** important (PMID:8132750, lead).
- **Penetrance:** expected to be complete for biallelic loss-of-function alleles. This is inferred and not directly sourced.
- **Founder effects, carrier frequency, sex ratio, geography:** not assessed (**gap**).

## 10. Diagnostics

- **Biochemistry:** serum total and ionised calcium (severely high), intact PTH (high), urine calcium/creatinine. Magnesium and phosphate are often checked, but I did not source them for NSHPT.
- **Imaging:** skeletal survey for demineralisation, fractures and subperiosteal resorption (not sourced).
- **Genetic testing:** *CASR* sequencing, either single gene or a calcium/PTH panel including *GNA11* and *AP2S1*. Rapid exome or genome is also used. Höppner: "the differential diagnosis will be made based on molecular genetic findings" (PMID:35566721). Biallelic versus heterozygous status, together with parental calcium levels, drives management.
- **Differential diagnosis:**
  - NHPT, transient and heterozygous (PMID:35566721);
  - maternal hypoparathyroidism or hypocalcaemia causing fetal secondary hyperparathyroidism (not sourced);
  - neonatal hypercalcaemia from other causes, such as *CYP24A1* or *SLC34A1* variants, subcutaneous fat necrosis or Williams syndrome (not sourced);
  - primary hyperparathyroidism from adenoma: "has never been reported in neonates" (PMID:35566721).
- **Cascade testing:** parents (expected to be FHH carriers) and siblings.
- **Newborn screening:** none.
- **LOINC:** not looked up (**gap**).

## 11. Outcome and prognosis

- **Untreated:** "high mortality" (PMID:35566721). No numeric survival data were sourced.
- **Genotype–phenotype:** Marx & Sinaii 2020 (PMID:31778168, lead from search summary) report that homozygous dosage was generally more aggressive than heterozygous. A secondary news summary says they found serum calcium to be a marker of genetic severity. Verify this against the abstract.
- **After total parathyroidectomy:** permanent hypoparathyroidism is expected (inferred, not sourced). Long-term neurodevelopmental outcome was not found (**gap**).

## 12. Treatment

| Intervention | Source | NCIT lead (unverified) | Modality |
|---|---|---|---|
| Total parathyroidectomy (definitive); subtotal "ineffective and therefore not recommended" | PMID:35566721 | Surgical Procedure NCIT:C15329 (parathyroidectomy-specific term to be looked up) | SURGERY |
| Bisphosphonates (e.g. pamidronate) for bridging | "bisphosphonates are well established and their use has been reported in neonates with NSHPT" (PMID:35566721) | Pharmacotherapy NCIT:C15986 + CHEBI pamidronate (lookup) | SMALL_MOLECULE |
| Cinacalcet (calcimimetic, positive allosteric modulator of CaSR) | "infants with NHPT and NSHPT have also been treated successfully with cinacalcet" (PMID:35566721) | Pharmacotherapy + CHEBI cinacalcet (lookup) | SMALL_MOLECULE |
| IV hydration, loop diuretics, calcitonin, low-calcium formula | standard neonatal hypercalcaemia care; **not sourced** | Supportive Care NCIT:C15747 | — |
| Post-operative calcitriol and calcium | not sourced | — | — |

- **Effect modifier (candidate `effect_modifiers` with `GENOTYPE`):** cinacalcet response depends on the variant. Allosteric enhancement needs some residual receptor function. Case reports (search leads; PMIDs not captured) describe both outcomes:
  - homozygous patients who did not respond (a Sri Lankan infant: lack of response "should suggest homozygous mutations");
  - homozygous responders (a Turkish infant with p.G613E treated from day 2 to 18 months; a Chinese case that responded after bisphosphonates failed; a frameshift case controlled until 13 months).
  - Record only per-source rows. Do not infer.
- **Gene, cell and RNA therapies:** none. A ClinicalTrials.gov search was not run.

## 13. Prevention

- **Genetic counselling:** for FHH carriers, especially consanguineous couples and male carriers. Höppner: "it is advisable to offer genetic counseling to all pregnant women with confirmed FHH or a partner with FHH" (PMID:35566721). It also notes the "need to specifically instruct male patients with FHH".
- **Prenatal or preimplantation testing:** possible where both familial variants are known (not sourced).
- **Tertiary prevention:** early genotyping to choose between surgery and watchful waiting (PMID:35566721).

## 14. Other species

- No naturally occurring animal disease was found. OMIA was not searched (**gap**).
- Orthologs: mouse *Casr* (MGI) and others; IDs were not looked up.

## 15. Model organisms

- **Casr knockout mouse.** Ho 1995, *Nat Genet* 11:389–394 (PMID:7493018, lead).
  - Homozygous mice: high serum calcium and PTH, parathyroid hyperplasia, bone abnormalities, poor growth and early death. This recapitulates NSHPT.
  - Heterozygous mice: model FHH.
  - Suggested KB link: `RECAPITULATES` against the parathyroid set-point and hyperplasia nodes, `evidence_source: MODEL_ORGANISM`.
  - Limitation to record: the postnatal lethality was later partly attributed to extra-parathyroid effects. This comes from my recall and is **unsourced**; the knockout strategy left an alternatively spliced exon-5-lacking transcript. Check before using.
- **Rescue and double-knockout models** (*Casr*⁻/⁻ with *Pth*⁻/⁻ or *Gcm2*⁻/⁻) are known to separate parathyroid-dependent from parathyroid-independent effects. This is unsourced recall; find the PMIDs.
- **Not NSHPT models:** activating *Casr* mice (PMID:15347804, cached) model hypocalcaemia. The Gα11 mouse (PMID:29046478, cached) models FHH2.

---

## What blocks writing the YAML

1. **Fetch four papers:** `just fetch-reference` on PMID:31778168, 8132750, 7493018 and 9011580 to get quotable abstracts. They are the primary support for gene dosage, the genotype–severity relationship, the mouse model and the dominant-negative mechanism.
2. **Lump/split decision:** check MONDO:0009397's definition and `Transient_Neonatal_Hyperparathyroidism` before deciding where heterozygous severe NSHPT goes.
3. **Look up every HP, GO, CL, UBERON, CHEBI and NCIT term above.** None was looked up; all are proposals.
4. **Find primary sources** for the unsourced phenotypes (thoracic deformity, hypermagnesaemia), the post-parathyroidectomy course and the cinacalcet case reports (PMIDs still needed).

Sources:
- [Ho et al. 1995 Nat Genet mouse model (via JCI Insight reference)](https://insight.jci.org/references/scholar/684/B12)
- [BVS MEDLINE record 7493018](https://pesquisa.bvsalud.org/ses/resource/pt/mdl-7493018)
- [Pollak et al. 1994 J Clin Invest](https://www.jci.org/articles/view/117062)
- [Pollak 1994 PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC294052)
- [Marx & Sinaii, PMC7111126](https://pmc.ncbi.nlm.nih.gov/articles/PMC7111126)
- [Medwire summary of Marx & Sinaii](https://paediatric-endocrinology.medwirenews.com/news/calcium-levels-serve-as-marker-of-genetic-severity-of-neonatal-severe-hyperparathyroidism/)
- [Bai et al. 1997 J Clin Invest](https://www.jci.org/articles/view/119137)
- [ClinVar RCV001804716](https://ncbi.nlm.nih.gov/clinvar/RCV001804716.1)
- [NSHPT homozygous case, PMC7262957](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7262957/)
- [Cinacalcet delaying parathyroidectomy, Termedia](https://termedia.pl/The-efficiency-of-cinacalcet-treatment-in-delaying-parathyroidectomy-in-a-case-with-neonatal-severe-hyperparathyroidism-caused-by-homozygous-mutation-in-the-CASR-gene,138,46767,0,1.html)
- [Cinacalcet first-line in NSHPT, Marmara](https://avesis.marmara.edu.tr/yayin/03561f46-041c-4b7b-96b4-862e1965c3d1/cinacalcet-as-a-first-line-treatment-in-neonatal-severe-hyperparathyroidism-secondary-to-calcium-sensing-receptor-casr-mutation)
- [ESPE 2019 abstract P3-296](https://abstracts.eurospe.org/hrp/0092/hrp0092p3-296)
- [ESPE 2024 abstract P1-243](https://abstracts.eurospe.org/hrp/0098/hrp0098p1-243)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 21 |
| Quoted claims found in source | 19 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 14 |
| On topic | 8 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:35566721`: "When the mutation is maternally derived … these pregnancies are likely uneventful"
  - closest text in source: "When the mutation is maternally derived, both the mother and fetus share a need for increased calcium levels and coincide in the regulation of calcium homeostasis [11]"
- `PMID:35566721`: "elevation of the body's calcium set point … it takes a higher level of plasma calcium to suppress PTH secretion"
  - closest text in source: "Patients with FHH display higher levels of plasma PTH and it takes a higher level of plasma calcium to suppress PTH secretion (Figure 3)"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009397` (4 mentions) - the report calls it "stub"; MONDO calls it **neonatal severe primary hyperparathyroidism**
- `NCIT:C15329` (1 mention) - the report calls it "parathyroidectomy-specific term to be looked up"; NCIT calls it **Surgical Procedure**