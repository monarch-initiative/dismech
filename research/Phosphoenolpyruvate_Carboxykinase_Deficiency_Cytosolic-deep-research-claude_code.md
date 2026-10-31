---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-16T03:43:53.972391'
end_time: '2026-10-16T03:45:35.905230'
duration_seconds: 101.93
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Phosphoenolpyruvate Carboxykinase Deficiency, Cytosolic
  mondo_id: MONDO:0009866
  category: Metabolic Disorder
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
  num_turns: 9
  total_cost_usd: 0.7804097
  session_id: 6f407ab6-10d8-510b-8a76-b165dbc02479
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 7
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 7
  on_topic: 4
  validator_version: 0.3.0
term_validation:
  total_terms: 26
  verified: 26
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 19
  labels_matching: 13
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0033360
    reported_labels:
    - Hyperglutaminemia
    ontology_label: Impaired ability to shift attention
  - term_id: NCIT:C15447
    reported_labels:
    - BEHAVIORAL
    ontology_label: Dietary Intervention
  - term_id: NCBITaxon:10090
    reported_labels:
    - 'Likely `animal_models:` fields: species Mus musculus'
    ontology_label: Mus musculus
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Phosphoenolpyruvate Carboxykinase Deficiency, Cytosolic
- **MONDO ID:** MONDO:0009866 (if available)
- **Category:** Metabolic Disorder

## Research Objectives

Please provide a comprehensive research report on **Phosphoenolpyruvate Carboxykinase Deficiency, Cytosolic** covering all of the
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

# Cytosolic Phosphoenolpyruvate Carboxykinase (PEPCK-C) Deficiency (PCK1)

**Scope and verification.** I fetched and read two papers in full (Burg 2024, PMID 40092582; Vasiļevska 2026, PMID 41608521). The other claims rest on search-result summaries or on the reference list of Burg 2024. Items marked **[unverified]** come from my background knowledge, or from sources I did not open, and need checking before they go into the KB. Every PMID was read from a fetched source, and none was typed from memory. Only abstract-level quotes were available, so snippets need re-verification with `just fetch-reference`.

## 1. Disease information

- **Overview.** The paper's abstract calls it "a rare autosomal recessive gluconeogenesis disorder caused by variants in the PCK1 gene" (Vasiļevska 2026, PMID 41608521). Typical findings are fasting hypoglycemia, lactic acidosis, and urinary excretion of TCA-cycle intermediates, particularly fumarate. Presentation ranges from the neonatal period, through the first acute illness of infancy, to stress later in life. ([PhenoDis summary](https://iegext02.helmholtz-munich.de/phenodis/disease/show/6522), [PMC11910243](https://pmc.ncbi.nlm.nih.gov/articles/PMC11910243/))
- **Identifiers.**
  - OMIM 261680 is confirmed by search results.
  - MONDO:0009866 comes from the task template. I did not verify it against MONDO.
  - Orphanet numbers conflict between sources: PhenoDis lists 79316, ClinVar lists 2880, and PhenoDis also gives 2880 for the broader PEPCK deficiency category. Check Orphanet directly. If it is cited as `ORPHA:`, fetch the record with `just fetch-reference`.
  - Gene: PCK1 at 20q13.31, HGNC symbol PCK1. In KB form the CURIE would be `hgnc:<n>`, which I did not look up. ([MedGen](https://ncbi.nlm.nih.gov/medgen/1801754))
- **Synonyms.** PEPCK-C deficiency, PEPCK1 deficiency, cytosolic PEPCK deficiency, PCKDC. Also called phosphoenolpyruvate carboxykinase 1 deficiency (soluble).
- **Data source.** The data are disease-level aggregated case reports, not EHR-derived.

## 2. Etiology

- **Cause.** Biallelic loss-of-function variants in PCK1 cause the disease. There is no known environmental cause.
- **Genetic risk factors.** None beyond biallelic PCK1 variants. Modifier genes have not been identified. Siblings with identical genotypes differ in severity (Vasiļevska 2026).
- **Environmental triggers of decompensation.** These are triggers, not causes:
  - prolonged fasting;
  - febrile or infectious illness with reduced intake, including gastroenteritis;
  - exercise or other periods of increased energy need.
  - Sources: PMID 41608521; AJCR case ([amjcaserep.com/abstract/full/idArt/943118](https://amjcaserep.com/abstract/full/idArt/943118)), where all four hypoglycemic decompensations were infection-triggered.
- **Protective factors and gene–environment interaction.** No data. The one gene-environment link is that a catabolic or fasting state exposes the gluconeogenic block. Carbohydrate supplementation mitigates it.

## 3. Phenotypes

Frequencies are not quantified in the literature I read. The systematic review cited by Vasiļevska counted 32 individuals. It reports a mean age at first manifestation of 2.6 years (range 0.5–13), with neonatal hypoglycemia being typical.

| Phenotype | HPO (verify by lookup) | Notes and source |
|---|---|---|
| Hypoglycemia, fasting- or illness-triggered | Hypoglycemia (HP:0001943) | Core feature. Glucose 21–25 mg/dL in Burg 2024. |
| Lactic acidosis | Lactic acidosis (HP:0003128) | Seen during decompensation (Burg 2024; AJCR). |
| Ketotic acidosis | Metabolic acidosis (HP:0001942) | Burg 2024. |
| Elevated transaminases / hepatic dysfunction | Elevated hepatic transaminase (HP:0002910) | AJCR; Vieira 2017. |
| Acute liver failure with coagulopathy | Acute hepatic failure (HP:0006554) | Neonatal in Burg 2024. Transient in Vasiļevska 2026, where the proband met pediatric ALF criteria. |
| Hepatic steatosis | Hepatic steatosis (HP:0001397) | Fatty infiltration on ultrasound at 7 months (Burg 2024). |
| Hyperferritinemia (extreme) | Hyperferritinemia (HP:0003281) | More than 40,000 ng/ml in the neonate. Normalized to 108 ng/ml. Mechanism speculative. |
| Hyperammonemia | Hyperammonemia (HP:0001987) | Reported in Burg 2024 and in the OJRD literature. Mild or normal in the Vasiļevska proband. |
| Elevated plasma/urine glutamine | Hyperglutaminemia (HP:0033360) | Vasiļevska 2026. |
| Seizures, cerebral edema, death | Seizure (HP:0001250) | Becker 2021 (PMID 33445193): hypoglycemia-induced seizure and death in a 3-year-old. |
| Growth failure | Failure to thrive (HP:0001508) | Oishi 2021 (PMID 32908218). |
| Mild motor delay | Motor delay (HP:0001270) | Burg 2024, at 15 months. |
| Hypertriglyceridemia, transient | Hypertriglyceridemia (HP:0002155) | 298 mg/dL in Burg 2024. |
| Acute kidney injury, transient | Acute kidney injury (HP:0001919) | Vasiļevska proband. |
| Urinary TCA intermediates (fumarate), dicarboxylic aciduria, glutaric and α-hydroxyglutaric aciduria | Abnormal urinary organic acid profile (HP:0003110 or similar) | Burg 2024. |

- **Variability.** The OJRD summary says some patients have hypoglycemia with normal development, while others develop liver failure, hyperammonemia and encephalopathy. Phenotypes differ even between relatives, and the authors suggest this may mean the disease is underdiagnosed.
- **Quality of life.** No data.

## 4. Genetic and molecular information

- **Gene and inheritance.** PCK1 encodes cytosolic PEPCK (EC 4.1.1.32). Inheritance is autosomal recessive, and the parents in Burg 2024 were heterozygous carriers.
- **Variant spectrum.** Burg 2024 states that fewer than 30 patients and six mutations had been reported, all missense or splice, before the first homozygous frameshift.

| Variant | Source and notes |
|---|---|
| c.925G>A, p.(Gly309Arg) | Vieira 2017 (PMID 28216384). Vasiļevska 2026 reports it in "84% of patients". Cell studies showed the mutant gene could not produce a normally functioning enzyme (Centogene-hosted copy). ClinVar variation ID 338886. |
| p.Gly430Asp and p.His496Gln | Oishi 2021 (PMID 32908218). Novel compound heterozygous missense variants. |
| c.978delC (1-bp deletion) | Burg 2024. First homozygous frameshift. Exon 7 of 10; translation terminates 15 amino acids downstream. Classified pathogenic under ACMG. |
| c.1833_1834del, p.(Glu611AspfsTer16) | Vasiļevska 2026. Last exon; predicted to escape nonsense-mediated decay and alter the last 12 amino acids. Likely pathogenic. Found in compound heterozygosity with p.Gly309Arg. |

- **Functional consequence.** Loss of function. In Burg 2024's words, "PEPCK-1 loss of function impedes cytosolic gluconeogenesis".
- **Not found.** I found no allele-frequency data (gnomAD), no epigenetic findings, no chromosomal abnormalities, and no ClinGen gene-disease validity record. Run `just check-gene-validity` and check `CGGV:` records before asserting a tier.
- **Variant origin.** Germline.

## 5. Environmental information

Triggers are fasting, intercurrent infection, and exertion (see section 2). There are no toxins, lifestyle causes, or infectious agents. No `infectious_agent` or exposure-term binding is warranted. Any environmental entry would be limited to fasting or infection as a trigger, and it should be tied to a decompensation node.

## 6. Mechanism and pathophysiology

**Causal chain**

1. Biallelic PCK1 loss-of-function variants reduce cytosolic PEPCK (PEPCK-C) activity. This is demonstrated for p.Gly309Arg in cells (Vieira 2017). For other alleles it is inferred.
2. PEPCK-C normally converts oxaloacetate to phosphoenolpyruvate, a rate-limiting gluconeogenic step in liver and kidney. Its loss "impedes cytosolic gluconeogenesis" (Burg 2024).
3. During fasting or illness, glycogen runs out and gluconeogenesis cannot compensate. The result is fasting or illness-triggered hypoglycemia.
4. A proximal gluconeogenic block would be expected to cause lactate accumulation (lactate and alanine feed gluconeogenesis) and to lead to ketosis through lipolysis. Ketotic and lactic acidosis were observed (Burg 2024). The causal link to the block is inferred.
5. TCA intermediates such as fumarate, along with glutaric and α-hydroxyglutaric acids, accumulate and are excreted in urine (observed; the mechanism is not demonstrated).
6. Hepatic injury and steatosis follow. The proposed drivers are energy failure and altered substrate flux during decompensation. This is inferred.
   - Extreme hyperferritinemia was seen in the neonate. The authors only hypothesize iron–glucose cross-talk.
7. Neuroglycopenia can cause seizures, cerebral edema and death (Becker 2021).

**Branch or modifier.** Mitochondrial PEPCK2 is "thought to be partially replaced by the mitochondrial isoenzyme" (Burg 2024). This is a hypothesis. It could explain why many patients are mild or asymptomatic between insults. I did not find evidence on what determines severity.

**Other categories.** I found no data on immune involvement, tissue-specific transcriptomics, proteomics, single-cell work, or CRISPR screens.

**Suggested ontology terms (to be looked up, not copied).**
- GO:
  - gluconeogenesis (GO:0006094);
  - phosphoenolpyruvate carboxykinase (GTP) activity (GO:0004613);
  - cytosol (GO:0005829).
- CL: hepatocyte (CL:0000182), renal proximal tubule epithelial cell.

## 7. Anatomical structures

- **Primary tissues.** Liver and kidney, the gluconeogenic organs. The affected organs are inferred from enzyme biology. Direct tissue enzyme assays were not in my sources.
- **Secondary involvement.** Brain (hypoglycemic seizures and edema), and kidney (transient injury in the Vasiļevska proband).
- **Subcellular.** Cytosol.
- **UBERON.** liver (UBERON:0002107), kidney (UBERON:0002113).
- **Lateralization.** Not applicable.

## 8. Temporal development

- **Onset.** Neonatal to childhood. The mean age at first manifestation is 2.6 years, range 0.5–13 (Vasiļevska 2026, citing the systematic review). Neonatal hypoglycemia is typical.
- **Course.** Episodic, with decompensations at times of fasting or infection and well-being in between. Burg 2024's patient had a neonatal ALF episode, a decompensation at 7 months, and was stable at 15 months apart from one hypoglycemic episode.
- **Remission.** Episodes resolve with glucose. Neonatal liver failure and ferritin resolved in Burg 2024. The ALF was reversible with continuous glucose in Vasiļevska 2026.
- **Critical periods.** Intercurrent illness is the window of vulnerability.
- **Stages.** None defined.

## 9. Inheritance and population

- **Prevalence.** Not established. "Fewer than 30" patients were reported before 2024. A review of 32 individuals is cited in Vasiļevska 2026. This is a case count, so use `CASES_IN_LITERATURE` and do not give a rate.
- **Inheritance.** Autosomal recessive (HP:0000007). The Burg 2024 parents were heterozygous carriers.
- **Penetrance and expressivity.** Expressivity is highly variable. Two sisters in Vasiļevska 2026 share the same compound heterozygous genotype, but one had acute liver failure and the other was asymptomatic.
- **Founder effects and geography.** The p.Gly309Arg allele is reported in 84% of patients. Whether this is a founder effect is not stated in what I read. I did not find sex ratio, carrier frequency, or consanguinity data.

## 10. Diagnostics

- **Laboratory.**
  - Critical-sample glucose, lactate, ketones, ammonia, transaminases and coagulation tests.
  - Urine organic acids: fumarate and other TCA intermediates, dicarboxylic acids.
  - Amino acids: glutamine, glutamate, aspartate.
  - Ferritin, which was extreme in the neonate.
  - LOINC codes should be seeded with `just loinc-seed-cache`, never typed.
- **Imaging.** Liver ultrasound can show fatty infiltration or increased echogenicity.
- **Genetic testing.** Exome sequencing made the diagnosis in Burg 2024, which calls the diagnosis "nearly impossible to diagnose at the pre-exome sequencing era." A gene panel or single-gene PCK1 sequencing is reasonable. The Vasiļevska siblings also had segregation analysis.
- **Enzyme assay and biopsy.** I found no information in my sources. The 2026 proband was not biopsied.
- **Differential diagnosis.** Other causes of ketotic or lactic hypoglycemia:
  - glycogen storage disease type I;
  - fructose-1,6-bisphosphatase deficiency;
  - pyruvate carboxylase deficiency;
  - fatty acid oxidation disorders;
  - hyperinsulinism.
  - Causes of neonatal liver failure with hyperferritinemia (neonatal hemochromatosis was initially suspected in Burg 2024). **[unverified]** as a distinguishing list, because it is from my background knowledge.
- **Screening.** No newborn screening program is described in the sources. The Burg 2024 family was offered prenatal diagnosis or PGT but did not pursue them, and a later daughter tested negative.

## 11. Outcome and prognosis

- **Survival.** There are no systematic data. Outcomes range from asymptomatic to fatal.
  - A hypoglycemia-induced seizure with cerebral edema and death in a 3-year-old (Becker 2021).
  - Reversible ALF in Burg 2024 and Vasiļevska 2026.
- **Morbidity.** Growth impairment, mild motor delay and recurrent decompensations in individual cases. The 2026 authors note that no follow-up guidelines exist.
- **Prognostic factors.** Not established.

## 12. Treatment

- **Core management.**
  - Avoid fasting.
  - Provide extra carbohydrate during illness, exercise, or other increased energy demand (PMC12834696).
  - Give IV dextrose or glucose at decompensation (Burg 2024). Continuous 5% glucose infusion reversed the ALF in Vasiļevska 2026.
  - Night-time glucose monitoring was recommended in Burg 2024.
  - The 2026 sisters are advised to limit sugar intake and avoid rapidly absorbed sugars. This runs partly against the extra-carbohydrate advice, so treat it as one group's practice.
- **KB mapping.**
  - Dietary intervention, NCIT:C15447 (`BEHAVIORAL`).
  - Glucose infusion: Pharmacotherapy, NCIT:C15986, with CHEBI glucose as `therapeutic_agent`.
  - Verify all CURIEs by lookup.
- **Other options.**
  - Liver transplant was considered, and the proband was transferred for evaluation, but she recovered without it.
  - IVIg was given empirically in Burg 2024 for suspected neonatal hemochromatosis. It is not a disease-specific treatment.
  - I found no gene therapy, enzyme replacement, or clinical trials (a ClinicalTrials.gov search was not run).
  - Pharmacogenomics: not applicable.

## 13. Prevention

- **Primary and secondary.** Genetic counseling, cascade testing of siblings, and prenatal diagnosis or PGT (offered in Burg 2024). Carrier screening is not described.
- **Tertiary.** Fasting avoidance, an emergency glucose plan for illness, and monitoring.
- **Immunization.** Standard vaccination to reduce infectious triggers is a reasonable inference. I found no direct statement in my sources.

## 14. Other species and natural disease

I found no OMIA entry or veterinary reports. Searching OMIA for PCK1 is a gap.

## 15. Model organisms

My searches did not retrieve a source on animal models, and Burg 2024 explicitly does not mention one. The following is from my background knowledge only and is **[unverified]**:

- A global *Pck1* knockout mouse reportedly dies in the first days of life with severe hypoglycemia, and liver-specific knockouts retain fasting glucose through other gluconeogenic tissues.
- Before using this in the KB, confirm the primary papers and the MGI record, and take PMIDs from a fetched record. Do not use this paragraph as evidence.
- Likely `animal_models:` fields: species Mus musculus (NCBITaxon:10090), a `modeled_mechanisms` link to the gluconeogenesis node, and a `fidelity` rating.

## Curation notes

- **Evidence.** Candidate sources, with PMIDs from Burg 2024's reference list, which I did not independently fetch:

| PMID | Source |
|---|---|
| 40092582 | Burg 2024 (fetched) |
| 41608521 | Vasiļevska 2026 (fetched) |
| 28216384 | Vieira 2017 |
| 26971250 | Santra 2016 |
| 32908218 | Oishi 2021 |
| 33445193 | Becker 2021 |
| 34622459 | Vieira 2022 (expanded phenotype) |
| 24863970 | Adams 2014 |
| 176867 | Hommes 1976 |
| 179269 | Vidnes and Sovik 1976 |

  - I did not locate the AJCR case's PMID or year. Fetch it before citing.
  - Hommes 1976 may be the first-case description. This is unconfirmed.
  - Santra is dated 2016 in that reference list, not 2019.
  - All snippets above come from abstracts or summaries. Rerun `just count-verified-snippets` before use.
- **Stub and MONDO check.** Confirm that MONDO:0009866 matches the entry name and `disease_term` before drafting.
- **Gaps to fill.** The mouse model, the true Orphanet ID, ClinGen validity, a full-text review of phenotype frequencies (the 32-patient systematic review, which I did not read), and HPO and LOINC lookups.

## Sources

- [Burg et al. 2024, Mol Genet Metab Rep, PMID 40092582](https://pmc.ncbi.nlm.nih.gov/articles/PMC11910243/)
- [Vasiļevska et al. 2026, JIMD Rep, PMID 41608521](https://pmc.ncbi.nlm.nih.gov/articles/PMC12834696/)
- [Am J Case Rep, article 943118](https://amjcaserep.com/abstract/full/idArt/943118)
- [Vieira 2017 (Centogene-hosted PDF)](https://centogene.com/fileadmin/pdf/Science_Education/Publications/Publication_Novel_homozygous_PCK1_mutation_cytosolic_phosphoenolpyruvate_carboxykinase_deficiency.pdf)
- [OJRD article s13023-023-02946-5](https://ojrd.biomedcentral.com/counter/pdf/10.1186/s13023-023-02946-5.pdf)
- [PhenoDis](https://iegext02.helmholtz-munich.de/phenodis/disease/show/6522)
- [MedGen](https://ncbi.nlm.nih.gov/medgen/1801754)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 7 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 19 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0033360` (1 mention) - the report calls it "Hyperglutaminemia"; HP calls it **Impaired ability to shift attention**
- `NCIT:C15447` (1 mention) - the report calls it "BEHAVIORAL"; NCIT calls it **Dietary Intervention**
- `NCBITaxon:10090` (1 mention) - the report calls it "Likely `animal_models:` fields: species Mus musculus"; NCBITaxon calls it **Mus musculus**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002910` (1 mention) - the report calls it "Elevated hepatic transaminase"; HP calls it **Elevated circulating hepatic transaminase concentration**, and lists "Elevated transaminases" among its other names
- `HP:0003281` (1 mention) - the report calls it "Hyperferritinemia"; HP calls it **Increased circulating ferritin concentration**, and lists "Hyperferritinemia" among its other names
- `CL:0000182` (1 mention) - the report calls it "CL: hepatocyte"; CL calls it **hepatocyte**