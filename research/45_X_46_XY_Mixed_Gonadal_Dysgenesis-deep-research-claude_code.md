---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-29T19:36:56.183694'
end_time: '2026-08-29T19:42:01.621445'
duration_seconds: 305.44
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: 45,X/46,XY Mixed Gonadal Dysgenesis
  mondo_id: ''
  category: Chromosomal
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
  web_search_requests: 13
  num_turns: 23
  total_cost_usd: 1.3163635999999996
  session_id: 947d87eb-a7bc-50ae-bd2b-57097ad6c44a
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 21
reference_validation:
  total_references: 29
  verified: 29
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 29
  on_topic: 18
  validator_version: 0.2.1
term_validation:
  total_terms: 51
  verified: 49
  not_found: 1
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.02
  labels_checked: 20
  labels_matching: 14
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0015779
    reported_labels:
    - 45,X/46,XY mixed gonadal dysgenesis
    - verify via `just validate-terms` before use
    ontology_label: 45,X/46,XY mixed gonadal dysgenesis
  - term_id: HP:0000053
    reported_labels:
    - Clitoral hypertrophy
    ontology_label: Macroorchidism
  - term_id: HP:0000407
    reported_labels:
    - 10% in one cohort
    ontology_label: Sensorineural hearing impairment
  - term_id: CL:0000501
    reported_labels:
    - approximate
    ontology_label: granulosa cell
  - term_id: UBERON:0000991
    reported_labels:
    - 'Suggested UBERON terms: gonad'
    ontology_label: gonad
  labels_variant: 1
  unresolved_terms:
  - HP:0000850
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** 45,X/46,XY Mixed Gonadal Dysgenesis
- **MONDO ID:**  (if available)
- **Category:** Chromosomal

## Research Objectives

Please provide a comprehensive research report on **45,X/46,XY Mixed Gonadal Dysgenesis** covering all of the
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

I now have sufficient material to compile a comprehensive report.

Sources:
- [45,X/46,XY mixed gonadal dysgenesis - NORD](https://rarediseases.org/mondo-disease/45x-46xy-mixed-gonadal-dysgenesis/)
- [45,X/46,XY mosaicism - Wikipedia](https://en.wikipedia.org/wiki/Mixed_gonadal_dysgenesis)
- [Genetics, Gonadal Dysgenesis - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK539886/)
- [Giri et al. 2025, Mixed Gonadal Dysgenesis: A Comprehensive Review, Clinical Endocrinology (PMC12757904)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12757904/)
- [Clinical and Reproductive Characteristics of Patients with Mixed Gonadal Dysgenesis (PMC8418569)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8418569/)
- [GARD - Mixed gonadal dysgenesis](https://rarediseases.info.nih.gov/diseases/2539/mixed-gonadal-dysgenesis)
- [Mixed Gonadal Dysgenesis: A Narrative Literature Review, Journal of Urology](https://www.auajournals.org/doi/10.1097/JU.0000000000004137)
- [Screening of Y chromosome microdeletions in 46,XY partial gonadal dysgenesis and 45,X/46,XY (PMC3827999)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3827999/)
- [Early Bilateral Gonadoblastoma in MGD: Case Report (PMC9799003)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9799003/)
- [Variation of Gonadal Dysgenesis and Tumor Risk in 45,X/46,XY Mosaicism - PubMed](https://pubmed.ncbi.nlm.nih.gov/31883875/)
- [Tumor risk of children with 45,X/46,XY gonadal dysgenesis - PubMed](https://pubmed.ncbi.nlm.nih.gov/27032613/)
- [45,X/46,XY mosaicism and gender incongruence - PubMed (2025)](https://pubmed.ncbi.nlm.nih.gov/40888655/)
- [Johansen et al. 2012, J Clin Endocrinol Metab 97(8):E1540](https://academic.oup.com/jcem/article-abstract/97/8/E1540/2823130)
- [Clinical and hormonal characteristics of 45,X/46,XY mosaicism in 38 Chinese patients (PMC10154695)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10154695/)
- [Alkhunaizi et al. 2024, AJMG Part A - Clinical manifestations and long-term follow-up](https://onlinelibrary.wiley.com/doi/abs/10.1002/ajmg.a.63451)
- [Mouse Gonad Development in the Absence of WNT4/SOX9 (PMC7291083)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7291083/)
- [A critical time window of Sry action in gonadal sex determination in mice](https://journals.biologists.com/dev/article/136/1/129/65122/)
- [Persistent Müllerian Duct Syndrome - AMH/AMHR2 pathway (PMC10411253)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10411253/)
- [45,X/46,XY mosaicism: report on 14 patients, Brazilian cohort - PubMed](https://pubmed.ncbi.nlm.nih.gov/25351753/)
- [Mixed Gonadal Dysgenesis: What Exactly Is This Condition? - AUA News 2024](https://auanews.net/issues/articles/2024/october-extra-2024/mixed-gonadal-dysgenesis-what-exactly-is-this-important-but-confusing-condition)
- [Monarch Initiative MONDO:0015779](https://monarchinitiative.org/MONDO:0015779)

---

# 45,X/46,XY Mixed Gonadal Dysgenesis: Comprehensive Research Report

## 1. Disease Information

**Overview.** 45,X/46,XY Mixed Gonadal Dysgenesis (MGD; also called 45,X/46,XY mosaicism) is a chromosomal disorder of sex development (DSD) caused by somatic mosaicism for a 45,X cell line and a 46,XY cell line arising from post-zygotic mitotic loss of the Y chromosome (or, more rarely, loss/structural rearrangement of the Y in a subset of cells). The defining anatomic feature is asymmetric gonadal development: classically a streak (undifferentiated fibrous) gonad on one side and a dysgenetic-to-normal testis on the other, with variably persistent Müllerian structures (hemi-uterus, fallopian tube remnant) reflecting incomplete anti-Müllerian hormone (AMH) action from the dysgenetic testis (Wikipedia; NORD; StatPearls — PMID:2294747, PMID:22605431, PMID:27064253).

**Identifiers.**
- **MONDO:** MONDO:0015779 (45,X/46,XY mixed gonadal dysgenesis) — Monarch Initiative record aggregates OMIM/Orphanet/UMLS cross-references, though the live page content could not be fully retrieved in this session; verify the CURIE against the dismech term-validation pipeline before curation use.
- **Orphanet:** A related, broader entry exists for "46,XY partial gonadal dysgenesis" (Orphanet ORPHA:251510); MGD itself (with the 45,X cell line) is generally indexed as a DSD-sex-chromosome-abnormality subtype distinct from pure 46,XY partial gonadal dysgenesis (PGD), which lacks the 45,X line (tp.amegroups.org case report; ScienceDirect "Genetics of 46,XY gonadal dysgenesis").
- **MedGen:** Concept ID CN279762 ("45,X/46,XY mixed gonadal dysgenesis") (NCBI MedGen).
- **GARD/NORD:** Listed as a rare disease; GARD notes detailed symptom/cause/treatment fields are still sparse in that particular resource, underscoring reliance on primary literature (rarediseases.info.nih.gov).
- **ICD‑10/ICD‑11:** Falls under Q99.1 (Chromosomal mosaic, sex chromosomes) / general "gonadal dysgenesis" categories in ICD-10-CM; ICD-11 codes it under disorders of sex development due to chromosome anomalies (LD2A.Y-type entries) — exact codes vary by coding system and were not independently confirmed against a primary ICD source in this pass.
- **Synonyms:** X0/XY mosaicism; 45,X/46,XY mosaicism; mixed gonadal dysgenesis; asymmetric gonadal dysgenesis (Wikipedia; GARD).

**Distinction from related entities.** MGD (with a 45,X line) is distinguished from:
- **46,XY partial gonadal dysgenesis (PGD):** karyotype is pure 46,XY (no 45,X line), typically due to monogenic causes (SRY, NR5A1/SF1, MAP3K1 variants) rather than chromosomal mosaicism, and lacks Turner-syndrome stigmata (PMC3827999; NORD PGD page).
- **Complete gonadal dysgenesis (Swyer syndrome):** 46,XY karyotype with bilateral streak gonads and female phenotype.
- **Persistent Müllerian Duct Syndrome (PMDS):** normal testicular differentiation with isolated failure of AMH/AMHR2 signaling; gonadal histology is normal testis (not dysgenetic), distinguishing it from MGD on biopsy (PMC10411253).

**Data provenance.** Information in the literature is drawn overwhelmingly from aggregated case series and retrospective single/multi-center cohorts (e.g., 10–38 patient series) rather than large-scale EHR/registry studies, reflecting the rarity of the condition; a 2025 systematic narrative review (Giri et al., *Clinical Endocrinology*, PMID:41208147) synthesizes literature from 2000–2024.

---

## 2. Etiology

### Disease Causal Mechanism
MGD arises from **postzygotic mitotic non-disjunction or anaphase lag** affecting the Y chromosome (or, less commonly, structural instability of a rearranged/dicentric Y) during early cleavage divisions, producing two (or more) cell lineages: 45,X and 46,XY, distributed in varying proportions across tissues, including the gonads themselves (Wikipedia, citing StatPearls mechanistic description; PMC11521797 case of idic(Y) mosaicism). This is fundamentally a **somatic mosaicism / chromosomal instability** mechanism rather than a single-gene Mendelian defect.

**Molecular consequence.** The presence or absence of a functional SRY-bearing Y chromosome in individual gonadal ridge cells determines whether that region differentiates toward testis (SRY⁺ Sertoli cell precursors activate SOX9, which establishes a SOX9–FGF9 positive-feedback loop while repressing the pro-ovarian WNT4/RSPO1/β-catenin pathway) or toward ovary/streak tissue (SRY-negative cells default toward WNT4-driven pre-granulosa fate) (PMC7291083; journals.biologists.com Sry critical-window study; PMC3735148). Because the two cell lines are admixed in variable ratios across and within the gonads, one gonad can differentiate predominantly along the testicular pathway (dysgenetic testis) while the contralateral gonad, dominated by the 45,X line, fails to organize (streak gonad) — the anatomic hallmark of MGD.

**Y-chromosome structural abnormalities.** A substantial subset of 45,X/46,XY cases actually involve a **structurally abnormal Y** (isodicentric Y, ring Y, Yp or Yq deletions) rather than a normal Y in the second line; such abnormal Y chromosomes are mitotically unstable and predispose to secondary loss of a normal-appearing X0 line, which is proposed as the origin mechanism for many 45,X/46,XY mosaics (PMC11521797; PMC3827999 on Y-microdeletion screening).

### Genetic Risk Factors
- **SRY gene status/dosage:** Presence and expression level of SRY on the retained Y chromosome is the principal driver of the degree of virilization; irregular/mosaic SRY and downstream SOX9 expression are implicated in the partial/mixed phenotype (WebSearch synthesis; PMC3055899 SOX9 regulation failure in 46,XY DSD).
- **Y-chromosome microdeletions (AZF regions):** A high frequency of Y-chromosome microdeletions has been reported specifically in males with 45,X/46,XY mosaicism presenting with infertility, and in 46,XY PGD patients screened alongside 45,X/46,XY variants (PMC3827999; PMC7025455 "High frequency of Y chromosome microdeletions in male infertility patients with 45,X/46,XY mosaicism").
- **SHOX haploinsufficiency:** The short-stature Turner-like phenotype is attributed to dosage loss of the SHOX gene (pseudoautosomal region) in the 45,X-predominant tissue fraction, analogous to classic Turner syndrome (Wikipedia; Giri et al. 2025 review).
- **DAX1 (NR0B1):** Proposed as an X-linked "anti-testis" gene whose relative dosage in 45,X/46,XY mosaics may suppress testicular differentiation, contributing to the streak-gonad phenotype (WebSearch synthesis of NORD/Malacards content; note this remains a hypothesis rather than an established mechanism and should be treated cautiously in curation).
- **MAP3K1:** Implicated in 13–18% of 46,XY gonadal dysgenesis broadly (not MGD-specific), acting via decreased SOX9 expression (StatPearls, PMC12757904 synthesis).
- **NR5A1 (SF1):** A recognized monogenic cause of 46,XY PGD, occasionally invoked in the differential/overlap literature for atypical MGD-like presentations (PMC10754607 case report).

### Environmental Risk Factors
No established environmental, toxin, or exposure-related risk factors were identified in the literature searched; MGD is understood as a stochastic, sporadic post-zygotic chromosomal event rather than an exposure-driven condition. Advanced parental age or other epidemiologic risk modifiers were not substantiated by the sources reviewed.

### Protective Factors
No specific genetic or environmental protective factors against MGD were identified in the literature. This reflects the mosaic/stochastic mitotic origin of the condition rather than absence of research — a de novo somatic event has no established "susceptibility-lowering" allele analog.

### Gene–Environment Interactions
Not applicable/not documented; no GxE data were found for this condition.

---

## 3. Phenotypes

The phenotypic spectrum of 45,X/46,XY mosaicism is **exceptionally broad** — from phenotypically normal males, through the full range of atypical/ambiguous genitalia, to phenotypically normal females with Turner-syndrome features (Wikipedia; PMC8418569; multiple case series PMID:3595646, PMID:10429013, PMID:25351753, PMID:26759215).

### Genital/Reproductive Phenotypes
| Phenotype | Frequency/Notes | Suggested HPO term |
|---|---|---|
| Ambiguous/atypical genitalia | Most reported presentation in DSD referral cohorts (~5–15% of atypical genitalia cases attributable to MGD) | HP:0000062 (Ambiguous genitalia) |
| Clitoromegaly | 80% of initial presentations in one 10-patient cohort (PMC8418569) | HP:0000053 (Clitoral hypertrophy) |
| Hypospadias (perineal/scrotal) | Common in phallus-predominant presentations | HP:0000047 (Hypospadias) |
| Bifid/labioscrotal fusion | Reported in neonatal presentation spectrum | HP:0000048 (Bifid scrotum) |
| Micropenis / ventral chordee | Part of the atypical-genitalia spectrum | HP:0000054 (Micropenis) |
| Cryptorchidism / non-palpable gonad | Streak gonad classically non-palpable; dysgenetic testis variably descended | HP:0000028 (Cryptorchidism) |
| Persistent Müllerian structures (hemi-uterus, fallopian tube) | Reflects incomplete AMH action; ultrasound under-detects vs. laparoscopy (~40% miss rate by US) | HP:0000130 (Uterus present in an individual with a Y chromosome) / HP:0008734 |
| Delayed puberty / primary amenorrhea | 20% of one cohort; common in undiagnosed female-reared cases presenting in adolescence | HP:0000823 (Delayed puberty) |
| Infertility (near-universal) | Testicular insufficiency in 60–70% of males by third decade; spontaneous fertility "extremely rare" | HP:0000789 (Infertility) |

### Turner-like Somatic Phenotypes
| Phenotype | Notes | HPO term |
|---|---|---|
| Short stature | Universal/near-universal finding; mean height SDS ≈ −3.77 in one cohort | HP:0004322 (Short stature) |
| Webbed neck | Classic Turner stigma | HP:0000465 (Webbed neck) |
| Shield chest / widely spaced nipples | Turner-overlap feature | HP:0000900 (Broad chest); HP:0006610 |
| Cubitus valgus | Reported Turner stigma | HP:0002967 (Cubitus valgus) |
| High-arched palate | Reported | HP:0000218 (High palate) |
| Low posterior hairline | Reported (Johansen 2012) | HP:0002162 (Low posterior hairline) |
| Renal anomalies (horseshoe kidney, unilateral agenesis) | 40% in one cohort (30% unilateral agenesis, 10% horseshoe kidney) | HP:0000085 (Horseshoe kidney); HP:0000122 |
| Cardiac defects (bicuspid aortic valve, coarctation of aorta) | Documented in reviews, though absent in some smaller cohorts | HP:0001647 (Bicuspid aortic valve); HP:0001680 (Coarctation of aorta) |
| Sensorineural hearing loss | 10% in one cohort | HP:0000407 |
| Autoimmune thyroid disease (Hashimoto's/Graves') | 40% in one cohort (autoimmune hypothyroidism + Graves') | HP:0000850 / HP:0100647 |
| Mild intellectual disability, autism, facial dysmorphism | Reported in a minority (Johansen 2012 synthesis) — "Normal psychomotor development" also reported in other series, indicating this is not a core/consistent feature | HP:0001256; HP:0000717 |

### Laboratory/Endocrine Phenotypes
- **Elevated gonadotropins (LH/FSH)** — hypergonadotropic state when gonads are non-functional.
- **Low or low-normal testosterone** in males, with **blunted hCG-stimulated testosterone response** reflecting Leydig cell dysfunction.
- **Low-to-normal AMH** — toward the lower end of the male reference range, reflecting Sertoli cell dysfunction in the dysgenetic testis.

### Onset, Severity, Progression
- **Onset:** Congenital (present from birth in genital phenotype), but diagnosis timing varies: prenatal (amniocentesis), neonatal (atypical genitalia), or later childhood/adolescence (short stature, delayed puberty) when genitalia are near-normal at birth.
- **Severity/course:** Highly variable and largely determined by the tissue distribution of the two cell lines; not a progressive degenerative disease per se, though gonadal function (Leydig/germ cell) can decline with age, and short stature/height-SDS reduction is progressive without growth hormone intervention.
- **Quality of life:** Long-term sex-of-rearing satisfaction reported at 80–85% in reviewed cohorts, with persistent body-image and short-stature-related dissatisfaction as leading QoL detractors; ~50% of parents report unmet psychosocial-support needs during the neonatal/diagnostic period (PMC12757904/Giri et al. 2025).

---

## 4. Genetic/Molecular Information

**Karyotype/chromosomal basis:** 45,X/46,XY mosaicism (most common); rarer variants include 45,X/47,XYY and 45,X/46,X,idic(Y), 45,X/46,X,der(Y) (ring or isodicentric Y), and higher-order mosaics such as 45,X/46,XY/47,XYY (multiple case reports: PMC11521797, PMC3625110). Low-level mosaicism can be missed by standard peripheral-blood karyotyping and requires chromosomal microarray, FISH, or tissue-specific (buccal/skin/gonadal) analysis to detect.

**Causal/associated genes:**
- **SRY** (Yp11.2) — master testis-determining switch; irregular expression across the mosaic cell population drives partial masculinization (no HGNC/OMIM number retrieved in this pass beyond general Y-linked SRY locus).
- **SOX9** — downstream of SRY, essential for Sertoli cell/testis-cord formation; failure of SOX9 up-regulation is implicated in 46,XY DSD broadly (PMC3055899).
- **AMH / AMHR2** — anti-Müllerian hormone and its receptor; reduced Sertoli-cell AMH output in the dysgenetic testis underlies persistent Müllerian structures (differentiates MGD from isolated PMDS, where testis histology is otherwise normal) (PMC10411253).
- **SHOX** (Xp22.33/Yp11.32, pseudoautosomal region) — haploinsufficiency from the 45,X cell fraction drives short stature.
- **MAP3K1** — implicated in a minority (13–18%) of 46,XY gonadal dysgenesis cases generally, via decreased SOX9 expression.
- **NR5A1/SF1** — monogenic cause in overlapping 46,XY PGD phenotypes; occasionally cited in atypical MGD differential work-ups.
- **DAX1/NR0B1** — hypothesized X-linked antagonist of testis differentiation whose relative dosage may influence the streak-gonad phenotype in 45,X/46,XY mosaics (hypothesis-level; treat cautiously).
- **WT1** — associated with complete gonadal dysgenesis/absence in related but distinct syndromes (Denys-Drash/Frasier spectrum), cited as part of the broader gonadal-dysgenesis gene landscape rather than MGD-specific.

**Variant classification/type:** The primary "variant" is chromosomal-scale mosaicism/aneuploidy rather than a discrete point variant; secondary contributory findings (Y microdeletions in AZF regions, structural Y rearrangements) are structural/copy-number in nature. No systematic ClinVar/gnomAD allele-frequency data apply, since this is not a classic single-locus Mendelian disorder.

**Somatic vs. germline origin:** The 45,X/46,XY mosaicism itself is **somatic** in origin (post-zygotic mitotic error), not inherited in a Mendelian sense — recurrence risk to future pregnancies is not elevated by parental carrier status. This is a key genetic-counseling point.

**Functional consequences:** Loss-of-function-like effect at the tissue level — SRY⁺ cells drive testis differentiation while SRY-negative (45,X) cells default to streak/ovarian-like tissue; net phenotype reflects the spatial/proportional mixture rather than a single gain- or loss-of-function allele.

**Epigenetics:** No disease-specific DNA methylation/chromatin literature was identified in this search; this remains an underexplored area for MGD specifically (in contrast to better-studied epigenetic regulation of Sox9/enhancer elements in general testis-determination biology).

**Chromosomal abnormality detail:** Structural Y anomalies (isodicentric Y, ring Y) are mitotically unstable and are hypothesized as a common upstream cause generating the associated 45,X cell line via secondary loss during subsequent divisions (PMC11521797).

---

## 5. Environmental Information

No environmental toxin, occupational, radiation, or infectious contributing factors were identified in the literature for 45,X/46,XY MGD — consistent with its origin as a stochastic post-zygotic mitotic chromosomal error rather than an environmentally triggered condition. No lifestyle risk-factor or infectious-agent data apply. (This is a genuine absence of evidence in the literature searched, not merely an unresearched gap — the mitotic-error mechanism does not have an established environmental trigger analogous to, e.g., maternal age in meiotic non-disjunction trisomies.)

---

## 6. Mechanism / Pathophysiology

### Causal Chain (Upstream → Downstream)
1. **Initiating event (molecular/chromosomal):** Post-zygotic mitotic non-disjunction or anaphase lag of the Y chromosome (often a structurally unstable Y — isodicentric/ring Y) during early cleavage divisions → generation of two coexisting cell lineages, 45,X and 46,XY, distributed stochastically across tissues including the bipotential gonadal ridge.
2. **Gonadal ridge patterning (cellular, ~E10.5–E12.5 equivalent in human development):** In SRY⁺ (46,XY) somatic-cell-dominant regions of the ridge, SRY expression in pre-Sertoli cells activates **SOX9**, establishing a SOX9–FGF9 positive-feedback loop that (a) drives Sertoli cell and testis-cord differentiation and (b) actively represses the pro-ovarian **WNT4/RSPO1/β-catenin** pathway. In SRY-negative (45,X-dominant) regions, the absence of this switch allows default WNT4-driven pre-granulosa-like differentiation, which under monosomy-X conditions fails to sustain a functional ovary and instead regresses to fibrous **streak gonad** tissue (PMC7291083; journals.biologists.com Sry critical-window paper; PMC3735148).
3. **Asymmetric gonadal outcome (tissue level):** Because the two cell lines are unevenly distributed left-to-right and within each gonadal primordium, one gonad differentiates along a (variably dysgenetic) testicular pathway while the contralateral gonad fails to organize — the defining **streak gonad + dysgenetic/normal testis** anatomy of MGD.
4. **Sertoli/Leydig cell dysfunction (endocrine level):** The dysgenetic testis has quantitatively reduced Sertoli cell mass, yielding **low-to-low-normal AMH** (insufficient to fully regress Müllerian ducts, hence persistent hemi-uterus/fallopian tube) and reduced Leydig cell steroidogenic capacity, yielding **low/low-normal testosterone with blunted hCG-stimulated response** — the proximate cause of incomplete virilization/ambiguous genitalia.
5. **Systemic (organism level) consequences of the 45,X cell fraction:** SHOX haploinsufficiency in 45,X-predominant tissue → short stature; broader Turner-like somatic phenotype (renal anomalies, cardiac defects, lymphatic-derived webbed neck, autoimmune thyroiditis) via mechanisms shared with classic Turner syndrome, though the degree of expression depends on the tissue-specific 45,X:46,XY ratio (mosaic "dilution" of the Turner phenotype).
6. **Neoplastic transformation risk (downstream, age-dependent):** Retained Y-chromosome material (specifically the **GBY locus**, containing TSPY, on the Y short arm — implicated generally in Y-bearing dysgenetic gonad tumorigenesis, though not explicitly detailed in the sources retrieved here) in a dysgenetic gonadal microenvironment predisposes resident primordial/immature germ cells to arrest and malignant transformation, driving the well-documented **gonadoblastoma → dysgerminoma** progression pathway, particularly in intra-abdominal (undescended) gonads (75% premalignant-neoplasm risk vs. 16% inguinal, 9% scrotal) (PMC12757904/Giri et al. 2025; PMID:31883875; PMID:27032613).

### Cell Types Involved
- Sertoli cells (dysfunctional/reduced in dysgenetic testis) — CL:0000216
- Leydig cells (steroidogenically impaired) — CL:0000178
- Primordial/immature germ cells (arrested, tumor-initiating population) — CL:0000670 / CL:0000586
- Granulosa-like/pre-granulosa cells (in streak gonad remnant tissue) — CL:0000501 (approximate)
- Gonadal stromal/supporting cells

### Biological Processes (suggested GO terms)
- Male sex determination: GO:0030238
- Testis development: GO:0009888 / GO:0001708 (cell fate specification)
- Sertoli cell differentiation: GO:0060008
- Anti-Müllerian hormone signaling / Müllerian duct regression: GO:0001880 (Müllerian duct regression)
- Wnt signaling pathway involved in female gonad development: GO:0060065
- Germ cell development: GO:0007281
- Positive regulation of transcription (SOX9-driven testis program): GO:0045893

### Molecular Profiling
No disease-specific transcriptomic/proteomic/single-cell atlases for MGD gonadal tissue were identified in this search (a plausible knowledge gap — human dysgenetic-gonad single-cell profiling is more developed for Turner-syndrome ovaries and general DSD cohorts than for MGD specifically). Mouse single-cell gonadal atlases (from the SRY/SOX9/WNT4 mechanistic studies cited above) are the closest available molecular-profiling proxy and would need explicit HUMAN_MODEL_MISMATCH framing if cited for MGD curation, since murine gonadal-ridge chimera/knockout models are not MGD per se but rather models of the underlying testis-vs-ovary determination pathway.

---

## 7. Anatomical Structures Affected

**Organ level:**
- Primary: Gonads (asymmetric — one streak, one dysgenetic/normal testis), internal genital ducts (Müllerian remnants: hemi-uterus, fallopian tube, prostatic utricle; Wolffian derivatives variably present), external genitalia (variable ambiguous phenotype).
- Secondary/associated: Kidneys (horseshoe kidney, unilateral agenesis), heart/great vessels (bicuspid aortic valve, coarctation of aorta), thyroid (autoimmune thyroiditis/Graves'), skeletal system (short stature via SHOX, cubitus valgus), inner ear (sensorineural hearing loss).
- Systems involved: Reproductive/endocrine (primary), renal, cardiovascular, musculoskeletal, immune (autoimmune thyroid disease).

**Tissue/cell level:**
- Gonadal ridge-derived tissue: dysgenetic seminiferous tubules with reduced Sertoli/Leydig cell content on the testicular side; fibrous streak tissue (devoid of germ cells, composed of ovarian-type stroma) on the contralateral side.
- Suggested UBERON terms: gonad (UBERON:0000991), testis (UBERON:0000473), ovary (UBERON:0000992), uterus (UBERON:0000995), Müllerian duct (UBERON:0003508), Wolffian duct/mesonephric duct (UBERON:0001301), kidney (UBERON:0002113), thyroid gland (UBERON:0002046).

**Subcellular level:** No MGD-specific subcellular pathology (e.g., organelle-level defect) was identified; the mechanism operates at the chromosomal/cell-fate-decision level rather than a subcellular organelle dysfunction.

**Localization/laterality:** By definition **asymmetric/unilateral** discordant gonadal differentiation is the hallmark finding (streak vs. testis, left vs. right variable), though bilateral streak or bilateral dysgenetic-testis variants also occur within the phenotypic spectrum.

---

## 8. Temporal Development

- **Onset:** Congenital (chromosomal mosaicism established at the post-zygotic cleavage stage; gonadal/genital phenotype is present from fetal development), but clinical recognition spans the full life course — prenatal (incidental karyotype finding at amniocentesis), neonatal (atypical genitalia), childhood (short stature, incidentally discovered), or adolescence (delayed puberty, primary amenorrhea).
- **Progression:** Not a classically "progressive" degenerative disease; however, individual components evolve with age — testicular (Leydig/germ cell) function commonly declines, with testicular insufficiency reported in 60–70% of males by the third decade; height-SDS deficit worsens over childhood without growth-hormone intervention; gonadal tumor risk rises with age (though cases before age 20 are described as rare, risk is cumulative and lifelong for retained dysgenetic gonadal tissue).
- **Disease course pattern:** Largely stable/static with respect to the core chromosomal mosaicism, but the endocrine and oncologic sequelae are age-dependent and require lifelong surveillance.
- **Critical periods:** The "mini-puberty" window (first ~3 months of life) is clinically important for assessing baseline Leydig cell (testosterone) function; the prenatal/early postnatal period is critical for sex-of-rearing and gonadectomy decision-making; puberty (age 11–13) is a critical window for hormone-replacement initiation and for gender-identity development/disclosure counseling.

---

## 9. Inheritance and Population

**Epidemiology:**
- Incidence estimates range from **1 in 15,000 to 1 in 30,000 live births** across sources (Wikipedia/StatPearls cite ~1/15,000; PMC12757904 cites the 1/15,000–1/30,000 range).
- Among infants presenting with atypical/ambiguous genitalia, MGD accounts for **~5–15% of cases** (Giri et al. 2025).
- 45,X/46,XY mosaic is described as the **most common karyotype** underlying the mixed-gonadal-dysgenesis phenotype.
- True population prevalence is likely underestimated because many individuals with near-normal male or female phenotypes are never karyotyped.

**Inheritance pattern:** Sporadic — arises from a **post-zygotic somatic mitotic error**, not inherited via a Mendelian mechanism; parental karyotypes are typically normal, and recurrence risk in subsequent pregnancies is not increased above general population risk. This is an important genetic-counseling distinction from single-gene 46,XY PGD causes (e.g., NR5A1, MAP3K1), which may have autosomal patterns.

**Penetrance/expressivity:** Effectively 100% "penetrant" in the sense that mosaicism is present from conception, but **expressivity is extremely variable** — phenotype is determined by the proportion and tissue distribution of the 45,X vs. 46,XY cell lines, which cannot be reliably predicted from a peripheral-blood karyotype or amniotic-fluid cell ratio alone (explicitly noted: "amniotic fluid 45,X cell proportion cannot predict phenotypic outcomes").

**Founder effects/consanguinity/carrier frequency:** Not applicable, given the somatic/sporadic mechanism.

**Population demographics:** No specific ethnic or geographic predilection was identified in the literature reviewed; cohorts span Danish (Johansen 2012), Chinese (PMC10154695, 38 patients), Brazilian (PMID:25351753, 14 patients), and other national referral-center series, suggesting a broadly similar global distribution, though systematic multi-population prevalence comparisons were not found.

**Sex ratio:** Not meaningfully applicable as a simple M:F ratio, since "sex" itself is the variable clinical outcome in this condition; cohorts show a spread across female-reared, male-reared, and intersex presentations (e.g., 9 female-reared : 1 male-reared in one 10-patient cohort, though this reflects referral/rearing patterns rather than an underlying biological ratio).

---

## 10. Diagnostics

**Chromosomal/genetic testing:**
- **QF-PCR:** first-line rapid screen for SRY presence.
- **Standard peripheral-blood karyotype:** confirms 45,X/46,XY mosaicism; sensitivity limited for low-level mosaicism.
- **Chromosomal microarray (CGH/SNP array):** detects low-level mosaicism and submicroscopic Y copy-number variation missed by standard karyotype.
- **FISH:** rapid (within 24h) detection of monosomy X; can be applied to buccal, skin, or gonadal tissue when blood karyotype is normal but clinical suspicion persists (tissue-specific mosaicism).
- **Y-chromosome microdeletion (AZF) screening:** recommended in males with 45,X/46,XY presenting with infertility, given high reported frequency of microdeletions in this subgroup (PMC3827999, PMC7025455).

**Imaging:**
- Pelvic ultrasound: gonadal localization, uterus/Müllerian structure identification (though ultrasound reportedly misses Müllerian remnants in ~40% of cases vs. 100% detection by laparoscopy).
- Abdominal ultrasound: renal anomaly screening.
- MRI: reserved for ultrasound-inconclusive cases.
- Echocardiography: cardiac anomaly screening (bicuspid aortic valve, coarctation of aorta).
- **Laparoscopy:** considered superior for definitive anatomic delineation and enables targeted gonadal biopsy/removal.

**Endocrine evaluation:**
- Serum electrolytes, cortisol, 17-hydroxyprogesterone: to exclude congenital adrenal hyperplasia as an alternative/co-existing cause of atypical genitalia.
- Testosterone (ideally within the "mini-puberty" window, first 3 months of life): indicates Leydig cell function.
- hCG stimulation test: assesses testicular testosterone reserve outside the mini-puberty window or when baseline is low.
- AMH: marker of testicular (Sertoli cell) tissue presence/function.
- LH/FSH: elevation indicates a hypergonadotropic state from non-functional gonadal tissue.

**Histopathology:** Gonadal biopsy remains important for distinguishing MGD (streak + dysgenetic testis) from related entities (e.g., PMDS, where testicular histology is normal) and for detecting occult germ cell neoplasia in situ/gonadoblastoma.

**Differential diagnosis:** 46,XY partial gonadal dysgenesis (no 45,X line), Swyer syndrome (complete gonadal dysgenesis, bilateral streaks), persistent Müllerian duct syndrome, congenital adrenal hyperplasia (as an alternative cause of atypical genitalia), NR5A1-related DSD.

**Screening:** No population-level newborn screening program exists for MGD specifically (unlike, e.g., metabolic newborn screening panels); detection is via prenatal incidental karyotype finding, or postnatal clinical suspicion (atypical genitalia, short stature, delayed puberty) prompting targeted karyotyping.

---

## 11. Outcome/Prognosis

- **Gonadal malignancy:** Lifetime risk estimated at **15–25%**, with strong risk-stratification by gonadal location: **~75%** premalignant-neoplasm risk for intra-abdominal (undescended) gonads, **~16%** for inguinal, **~9%** for scrotal position — underscoring why gonadal position drives management urgency (PMC12757904/Giri et al. 2025). Independent series report gonadal tumors (gonadoblastoma ± dysgerminoma) in ~18% of surgically assessed patients (6/34), rising to 37.5–54.5% in subgroups with significant genital ambiguity or female phenotype (PMID:31883875-related synthesis).
- **Testicular function:** Testicular insufficiency develops in an estimated **60–70%** of males by the third decade of life.
- **Fertility:** Spontaneous fertility is "extremely rare"; assisted reproduction (testicular sperm extraction, gonadal tissue cryopreservation in prepubertal patients) is an emerging but still largely experimental option.
- **Growth/height:** Progressive height-SDS reduction with age if untreated; recombinant human growth hormone therapy improves growth velocity and final height (reported improvement of 0.42 SDS), with response paralleling that seen in classic Turner syndrome; typically initiated age 4–6 years.
- **Metabolic/cardiovascular morbidity:** A population-based study cited in the 2025 review identified a Turner-like long-term morbidity pattern — hypertension, dyslipidemia, and type 2 diabetes emerging by around age 40.
- **Psychosocial/gender outcomes:** Long-term satisfaction with sex of rearing reported at **80–85%**; gender incongruence prevalence reported at **12–15%** in MGD cohorts; persistent body-image concerns (short stature prominent) are the most cited long-term dissatisfaction driver. A 2025 case-based ethics/psychology paper (PMID:40888655) specifically examines a child assigned female at birth who later expressed male gender identity, highlighting the complexity of early, potentially irreversible sex-assignment decisions.
- **Mortality:** No MGD-specific mortality/survival statistics (e.g., 5-/10-year survival rates) were identified — consistent with this being primarily a developmental/endocrine/oncologic-risk condition rather than one with an intrinsically shortened lifespan, aside from the malignancy risk mitigated by gonadal surveillance/gonadectomy.

---

## 12. Treatment

**Sex assignment/multidisciplinary management:** Modern practice has shifted from historical universal female assignment with prophylactic gonadectomy toward **individualized, patient/family-centered, multidisciplinary decision-making** that weighs genital anatomy, internal reproductive structures, gonadal function, fertility potential, prenatal androgen exposure, malignancy risk, and psychosocial/cultural factors, with a general trend toward **deferring irreversible interventions** where feasible (PMC12757904/Giri et al. 2025).

**Surgical management (NCIT-mappable):**
- **Gonadectomy** — bilateral for female-assigned patients with non-functional streak gonads (early childhood); early removal of a retained dysgenetic testis in most cases unless testosterone production is adequate and formal surveillance is feasible; preservation favored for a morphologically normal, fully descended testis (with lifelong self-exam/imaging surveillance). → NCIT:C15329 (Surgical Procedure) or a more specific gonadectomy/orchiectomy NCIT term if available.
- **Laparoscopic streak-gonad excision** — preferred approach given malignancy risk.
- **Hypospadias repair** — staged, typically after confirmation of male sex of rearing. → NCIT:C15329 / relevant urologic-procedure term.
- **Gonadal relocation** (intra-abdominal gonad repositioned to labioscrotal fold) to facilitate examination/surveillance.
- **Clitoral recession** — reported in female-reared cases with clitoromegaly.
- **Gonadal tissue cryopreservation** — emerging fertility-preservation strategy performed at the time of gonadectomy in patients with retained germ cells.

**Hormonal therapies (NCIT:C15986 Pharmacotherapy, generally):**
- **Growth hormone (recombinant human GH):** improves growth velocity/final height (paralleling Turner syndrome response); typical initiation age 4–6 years.
- **Puberty induction, males:** low-dose intramuscular testosterone injections (every 4–6 weeks) with gradual dose escalation over several years; transdermal formulations for maintenance.
- **Puberty induction, females:** low-dose transdermal or oral estradiol starting ~age 11–12, gradually increased over 2–3 years; progestogen added if breakthrough bleeding occurs and a uterus is present; long-term hormone replacement continued to approximate natural menopause age (~50 years).

**Assisted reproduction:** Testicular sperm extraction (TESE) reported in isolated cases; gonadal tissue cryopreservation for prepubertal fertility preservation is an active area of clinical development rather than standard-of-care.

**Supportive/psychosocial care:** Proactive psychological support for parents around diagnosis disclosure, and for patients around body image and evolving gender identity through childhood/adolescence, is increasingly emphasized given documented gaps in current provision (~50% of parents reporting unmet psychosocial-support needs).

**Emerging/experimental approaches:**
- **Biomarker-driven surveillance** — circulating microRNA markers (notably **miR-371a-3p**) are being investigated as liquid-biopsy tools for early germ cell tumor detection, potentially allowing more conservative (gonad-sparing) surveillance strategies instead of universal prophylactic gonadectomy.
- **Shared decision-making tools** — web-based decision aids for gonadal/genital surgery choices are in development and validation.

**Treatment strategy/algorithm:** Management is explicitly multidisciplinary team (MDT)-based (pediatric endocrinology, urology/surgery, genetics, psychology, and the family), with transition planning to adult care ideally beginning at age 12–13, and dedicated transition clinics or joint pediatric–adult MDT models cited as improving long-term follow-up adherence.

**Reported treatment outcomes:** In one 10-patient cohort, gonadectomy was followed by spontaneous partial regression of phallus size (0.5–1 cm reduction over 6 months–1 year) in female-reared cases; no patients in that cohort opted for GH therapy, illustrating real-world variability in uptake of available interventions.

---

## 13. Prevention

MGD arises from a **sporadic post-zygotic somatic chromosomal event**, so there is no established **primary prevention** (no known modifiable risk factor to intervene upon) — this parallels the absence of identified environmental/lifestyle risk factors in Section 5.

**Secondary prevention (early detection/treatment):**
- Prenatal detection via amniocentesis karyotype (incidental finding, e.g., in the context of NIPT flagging or other indications) allows early counseling and postnatal targeted evaluation, though **phenotype cannot be reliably predicted from amniotic-fluid cell-line ratios**, which is a significant counseling limitation.
- Postnatal clinical vigilance for atypical genitalia at birth, or short stature/delayed puberty in later childhood, prompts karyotype-based diagnosis.

**Tertiary prevention (preventing complications in diagnosed individuals):**
- **Gonadal malignancy prevention:** risk-stratified gonadectomy or biomarker-based surveillance (see Treatment section) is the primary tertiary-prevention strategy, directly reducing progression from gonadoblastoma/germ cell neoplasia in situ to invasive dysgerminoma.
- **Growth hormone therapy** as tertiary prevention of adult short stature.
- **Cardiovascular/renal/metabolic surveillance** (echocardiography, renal imaging, blood pressure, lipid/glucose monitoring into adulthood) to preempt the Turner-like long-term morbidity pattern (hypertension, dyslipidemia, type 2 diabetes by ~age 40).
- **Autoimmune thyroid screening** given the ~40% prevalence of autoimmune thyroid disease in some cohorts.

**Genetic counseling:** Central to prevention/family-planning discussion is communicating the **sporadic, non-heritable nature** of the mosaicism (low recurrence risk in future pregnancies) while managing the substantial uncertainty in prenatal phenotype prediction.

**Screening programs:** No population-based newborn or prenatal screening program specific to MGD exists; detection remains opportunistic (incidental prenatal karyotype, or postnatal clinical suspicion).

---

## 14. Other Species / Natural Disease

No literature was identified describing **naturally occurring 45,X/46,XY mosaic gonadal dysgenesis as a spontaneous veterinary disease** (e.g., in OMIA or companion-animal case series) in this search pass — this is a plausible gap rather than a confirmed absence, and a dedicated OMIA/veterinary-literature search would be needed to confirm whether analogous XX/XY chimerism-associated intersex conditions are documented in domestic species (freemartinism in cattle, driven by placental blood-chimerism rather than post-zygotic mosaicism, is a related but mechanistically distinct veterinary phenomenon and was not directly evaluated here).

**Comparative biology:** The core testis-determination pathway (SRY → SOX9 → FGF9, antagonized by WNT4/RSPO1/β-catenin) is evolutionarily conserved across mammals, and the mechanistic insight into MGD's cellular basis is drawn substantially from mouse developmental biology (see Section 15), rather than from naturally occurring disease in other species.

**Zoonotic potential / transmission:** Not applicable — MGD is a non-infectious, developmental chromosomal condition.

---

## 15. Model Organisms

**No direct animal model of 45,X/46,XY mosaic MGD** (i.e., a mouse engineered or arising spontaneously with somatic X0/XY mosaicism reproducing asymmetric gonadal dysgenesis) was identified in this search. Instead, the relevant model-organism literature addresses the **underlying testis-determination pathway** that MGD's asymmetric SRY-mosaic gonads perturb:

- **Sry/Sox9/Wnt4 mouse genetic models:** Studies of *Sox9* conditional knockout, *Wnt4* knockout, and *Sox9;Wnt4* double-mutant mice define how SRY-driven SOX9 activity antagonizes WNT4/RSPO1/β-catenin signaling to commit supporting cells to a testicular vs. ovarian fate (PMC7291083, "Mouse Gonad Development in the Absence of the Pro-Ovary Factor WNT4 and the Pro-Testis Factor SOX9," PMID:32365547). Key finding: *Sox9* deletion in XY gonads causes ovarian-like development with ectopic WNT/β-catenin signaling, and SRY-positive supporting-cell precursors can adopt a female-like (pre-granulosa) identity; SOX9 is required for early male-supporting-cell specification independently of its role repressing RSPO1/WNT4/β-catenin.
- **Sry timing/chimera studies:** "A critical time window of Sry action in gonadal sex determination in mice" (journals.biologists.com) defines the developmental window (~E10.5–E12.5) during which Sry must act to commit the gonad to a testicular fate — directly relevant to understanding how variable SRY⁺ cell proportion/timing in a mosaic human gonad could yield partial/asymmetric differentiation.
- **Other XY sex-reversal mouse models** (cited peripherally in search results, not detailed here): *Nedd4* loss-of-function causing complete XY gonadal sex reversal (PMC8786929); *Fgfr2* "hobbyhorse" mutant causing complete XY gonadal sex reversal (PMC4067367) — these illustrate the broader genetic network in which SRY/SOX9 operate but are models of complete, not mosaic/asymmetric, sex reversal, and are **not direct models of the human mosaic 45,X/46,XY karyotype**.

**Model limitations for dismech curation purposes:** None of the mouse models identified reproduce the defining **somatic chromosomal mosaicism** of human MGD (they are typically full-body monogenic knockouts, not mitotic-mosaic chimeras of 45,X vs. 46,XY cell lines). Any pathophysiology node curated from these mouse studies should be flagged with `evidence_source: MODEL_ORGANISM` and, given the mechanistic (not mosaic-karyotype) nature of the models, likely warrants a `HUMAN_MODEL_MISMATCH` discussion node under dismech's schema — the models establish the SRY/SOX9/WNT4 causal logic convincingly, but do not themselves recapitulate the human mosaic/asymmetric-gonad phenomenon.

**Applications:** These models are primarily used to dissect the transcriptional antagonism between testis- and ovary-determining pathways at the cell-fate-decision level, which is directly explanatory (if not literally recapitulative) for why a mosaic human gonad can differentiate asymmetrically depending on local SRY⁺ cell fraction and timing.

---

## Summary of Key Ontology-Term Suggestions for Curation

| Category | Suggested terms |
|---|---|
| MONDO | MONDO:0015779 (verify via `just validate-terms` before use) |
| HPO (phenotype) | HP:0000062 Ambiguous genitalia; HP:0000053 Clitoral hypertrophy; HP:0000047 Hypospadias; HP:0000028 Cryptorchidism; HP:0004322 Short stature; HP:0000465 Webbed neck; HP:0002967 Cubitus valgus; HP:0000085 Horseshoe kidney; HP:0001647 Bicuspid aortic valve; HP:0001680 Coarctation of aorta; HP:0000823 Delayed puberty; HP:0000789 Infertility; HP:0000850/HP:0100647 Autoimmune thyroid disease |
| GO (biological process) | GO:0030238 Male sex determination; GO:0060008 Sertoli cell differentiation; GO:0001880 Müllerian duct regression; GO:0060065 Wnt signaling involved in female gonad development; GO:0007281 Germ cell development |
| CL (cell type) | CL:0000216 Sertoli cell; CL:0000178 Leydig cell; CL:0000670/CL:0000586 Primordial/germ cell |
| UBERON (anatomy) | UBERON:0000991 gonad; UBERON:0000473 testis; UBERON:0000992 ovary; UBERON:0000995 uterus; UBERON:0003508 Müllerian duct; UBERON:0001301 mesonephric (Wolffian) duct |
| HGNC (genes) | SRY; SOX9; AMH; AMHR2; SHOX; MAP3K1; NR5A1; NR0B1 (DAX1); WT1 |
| NCIT (treatment) | NCIT:C15329 Surgical Procedure (gonadectomy, hypospadias repair); NCIT:C15986 Pharmacotherapy (testosterone/estradiol replacement, GH therapy) |

**Notable evidence gaps for curation:** (1) no MGD-specific molecular/single-cell profiling of human dysgenetic gonadal tissue was located; (2) the DAX1-suppression hypothesis and several Turner-overlap CNS features (mild intellectual disability, autism) are reported inconsistently across cohorts and should be curated with appropriate frequency/directness caveats; (3) no dedicated animal model reproduces the mosaic karyotype itself, only the downstream SRY/SOX9/WNT4 pathway logic — curate any mouse-derived pathophysiology nodes as `MODEL_ORGANISM` evidence with a `HUMAN_MODEL_MISMATCH` discussion where appropriate; (4) OMIM/Orphanet/ICD numeric identifiers should be independently re-verified against primary sources (OMIM.org, Orphanet, WHO ICD-11 browser) before being written into a `Disease.mappings` block, since this session's GARD/Monarch fetches did not return the specific codes.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 29 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 29 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 51 |
| Resolved | 49 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 20 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0015779` (4 mentions) - the report calls it "45,X/46,XY mixed gonadal dysgenesis", "verify via `just validate-terms` before use"; MONDO calls it **45,X/46,XY mixed gonadal dysgenesis**
- `HP:0000053` (2 mentions) - the report calls it "Clitoral hypertrophy"; HP calls it **Macroorchidism**
- `HP:0000407` (1 mention) - the report calls it "10% in one cohort"; HP calls it **Sensorineural hearing impairment**
- `CL:0000501` (1 mention) - the report calls it "approximate"; CL calls it **granulosa cell**
- `UBERON:0000991` (2 mentions) - the report calls it "Suggested UBERON terms: gonad"; UBERON calls it **gonad**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0000850` (2 mentions) - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0001880` (2 mentions) - the report calls it "Müllerian duct regression"; GO calls it **Mullerian duct regression**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0015779` - called "45,X/46,XY mixed gonadal dysgenesis", "verify via `just validate-terms` before use"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
